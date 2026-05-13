"""Death-spiral monitor — Tom's third sign-off criterion.

Tracks rolling 7-day metrics and alerts on >10% drift. Three metrics:
- accuracy (eval pass rate)
- timeliness (latency p95)
- escalation rate (% routed to adjuster_review)

Pattern: stateless aggregation over a list of run records. State persistence
is optional and lives in a JSON file the caller manages. In production, run
records come from the audit trace stream; for now, the caller emits them.

Tom's quote: "alerts me if any of three things drift — accuracy, timeliness,
or escalation rate — by more than 10% over a rolling 7-day window."
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import median
from typing import Any, Iterable


@dataclass
class RunRecord:
    """One claim processed end-to-end."""
    timestamp: datetime
    claim_id: str
    decision: str  # "auto_send" | "adjuster_review" | "escalate"
    duration_ms: int
    eval_passed: bool | None = None  # None when unknown (production); True/False during eval


def _to_iso(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.isoformat()


def _from_iso(s: str) -> datetime:
    return datetime.fromisoformat(s)


@dataclass
class WindowMetrics:
    window_start: datetime
    window_end: datetime
    n: int
    pass_rate: float | None  # None if no eval-graded runs in window
    p95_latency_ms: int
    escalation_rate: float

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["window_start"] = _to_iso(self.window_start)
        d["window_end"] = _to_iso(self.window_end)
        return d


@dataclass
class Alert:
    metric: str          # "pass_rate" | "p95_latency_ms" | "escalation_rate"
    direction: str       # "drop" | "spike"
    severity: str        # "warning" | "critical"
    drift_pct: float     # absolute percentage points relative to baseline
    baseline_value: float
    current_value: float
    detail: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def compute_window(records: Iterable[RunRecord], window_end: datetime, window_days: int = 7) -> WindowMetrics:
    cutoff = window_end - timedelta(days=window_days)
    in_window = [r for r in records if cutoff <= r.timestamp <= window_end]
    if not in_window:
        return WindowMetrics(cutoff, window_end, 0, None, 0, 0.0)

    eval_runs = [r for r in in_window if r.eval_passed is not None]
    pass_rate = (sum(1 for r in eval_runs if r.eval_passed) / len(eval_runs)) if eval_runs else None

    durations = sorted(r.duration_ms for r in in_window)
    p95_idx = max(0, int(len(durations) * 0.95) - 1)
    p95_latency = durations[p95_idx]

    escalations = sum(1 for r in in_window if r.decision == "adjuster_review")
    escalation_rate = escalations / len(in_window)

    return WindowMetrics(cutoff, window_end, len(in_window), pass_rate, p95_latency, escalation_rate)


def detect_drift(
    current: WindowMetrics,
    baseline: WindowMetrics,
    drift_threshold_pct: float = 0.10,
) -> list[Alert]:
    """Compare two windows and emit alerts if any metric drifted beyond threshold.

    Tom asked for >10% drift over a rolling 7-day window. We interpret that as
    absolute change (e.g. pass_rate dropping from 95% to 84% = 11 percentage
    points = alert). Latency uses relative change (p95 going from 6s to 9s =
    50% relative = alert).
    """
    alerts: list[Alert] = []

    if current.pass_rate is not None and baseline.pass_rate is not None:
        delta = baseline.pass_rate - current.pass_rate
        if delta > drift_threshold_pct:
            severity = "critical" if delta > drift_threshold_pct * 2 else "warning"
            alerts.append(Alert(
                metric="pass_rate",
                direction="drop",
                severity=severity,
                drift_pct=delta * 100,
                baseline_value=baseline.pass_rate,
                current_value=current.pass_rate,
                detail=f"Pass rate dropped {delta:.1%} (from {baseline.pass_rate:.1%} to {current.pass_rate:.1%}).",
            ))

    if baseline.p95_latency_ms > 0:
        relative = (current.p95_latency_ms - baseline.p95_latency_ms) / baseline.p95_latency_ms
        if relative > drift_threshold_pct:
            severity = "critical" if relative > drift_threshold_pct * 3 else "warning"
            alerts.append(Alert(
                metric="p95_latency_ms",
                direction="spike",
                severity=severity,
                drift_pct=relative * 100,
                baseline_value=baseline.p95_latency_ms,
                current_value=current.p95_latency_ms,
                detail=f"p95 latency rose {relative:.0%} ({baseline.p95_latency_ms} -> {current.p95_latency_ms} ms).",
            ))

    delta = current.escalation_rate - baseline.escalation_rate
    if abs(delta) > drift_threshold_pct:
        direction = "spike" if delta > 0 else "drop"
        severity = "critical" if abs(delta) > drift_threshold_pct * 2 else "warning"
        alerts.append(Alert(
            metric="escalation_rate",
            direction=direction,
            severity=severity,
            drift_pct=delta * 100,
            baseline_value=baseline.escalation_rate,
            current_value=current.escalation_rate,
            detail=f"Escalation rate {direction}: {baseline.escalation_rate:.1%} -> {current.escalation_rate:.1%}.",
        ))

    return alerts


def save_records(records: list[RunRecord], path: Path | str) -> None:
    payload = [
        {
            "timestamp": _to_iso(r.timestamp),
            "claim_id": r.claim_id,
            "decision": r.decision,
            "duration_ms": r.duration_ms,
            "eval_passed": r.eval_passed,
        }
        for r in records
    ]
    Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_records(path: Path | str) -> list[RunRecord]:
    if not Path(path).exists():
        return []
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return [
        RunRecord(
            timestamp=_from_iso(r["timestamp"]),
            claim_id=r["claim_id"],
            decision=r["decision"],
            duration_ms=r["duration_ms"],
            eval_passed=r.get("eval_passed"),
        )
        for r in payload
    ]
