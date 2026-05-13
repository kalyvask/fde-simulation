"""Death-spiral monitor demo.

Simulates 14 days of claim runs (with a deliberate drift in the second week)
and shows the monitor catching it. In production these RunRecords come from
the live audit trace stream.
"""
from __future__ import annotations

import random
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from calder_agent.observability.death_spiral import (
    RunRecord, compute_window, detect_drift, save_records, load_records,
)


def simulate_runs(start: datetime, days: int, drift_after_day: int | None = None) -> list[RunRecord]:
    """Generate synthetic run records.

    Days 1-N pre-drift: pass rate ~98%, latency p95 ~6500ms, escalation ~30%.
    Days drift_after_day+1 onward: pass rate drops, latency spikes,
    escalation jumps (the death-spiral pattern).
    """
    rng = random.Random(42)
    records: list[RunRecord] = []
    for day in range(days):
        date = start + timedelta(days=day)
        in_drift = drift_after_day is not None and day > drift_after_day
        n_today = 50 + rng.randint(-10, 10)

        pass_target = 0.80 if in_drift else 0.98
        latency_base = 9500 if in_drift else 5800
        escalation_target = 0.55 if in_drift else 0.30

        for i in range(n_today):
            ts = date + timedelta(minutes=rng.randint(0, 60 * 14))
            decision = "adjuster_review" if rng.random() < escalation_target else "auto_send"
            duration = max(800, int(rng.gauss(latency_base, 1500)))
            eval_passed = rng.random() < pass_target
            records.append(RunRecord(
                timestamp=ts,
                claim_id=f"CL-SIM-{day:02d}-{i:03d}",
                decision=decision,
                duration_ms=duration,
                eval_passed=eval_passed,
            ))
    return records


def main() -> int:
    state_path = Path(__file__).parent.parent / "monitor_state.json"

    start = datetime(2026, 5, 1, tzinfo=timezone.utc)
    records = simulate_runs(start, days=14, drift_after_day=6)
    save_records(records, state_path)
    print(f"Wrote {len(records)} simulated records to {state_path.name}")

    # Compare day-7 baseline vs day-14 current
    baseline = compute_window(records, start + timedelta(days=7), window_days=7)
    current = compute_window(records, start + timedelta(days=14), window_days=7)

    print()
    print("BASELINE WINDOW (days 1-7)")
    print("-" * 60)
    for k, v in baseline.to_dict().items():
        print(f"  {k}: {v}")
    print()
    print("CURRENT WINDOW (days 8-14)")
    print("-" * 60)
    for k, v in current.to_dict().items():
        print(f"  {k}: {v}")
    print()

    alerts = detect_drift(current, baseline)
    print("ALERTS")
    print("-" * 60)
    if not alerts:
        print("  (none — system is healthy)")
    for a in alerts:
        print(f"  [{a.severity.upper()}] {a.metric} {a.direction} -- {a.detail}")

    print()
    print("In production: these alerts would page Tom + Devorah within minutes.")
    return 0 if not alerts else 1


if __name__ == "__main__":
    sys.exit(main())
