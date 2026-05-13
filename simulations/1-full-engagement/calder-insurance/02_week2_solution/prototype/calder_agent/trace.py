"""AuditTrace data model.

Designed to satisfy Tom's audit-trace standard and Marcus's audit-trace standard
(both surfaced in week-1 discovery). The trace is a first-class artifact, not
an afterthought.

Tom's requirements:
- Inputs the agent saw
- Rule applied
- Output
- Whether human reviewed
- Timestamps on every step
- Model version IDs (immutable agent snapshots)
- Human-readable summary with drilldown — not JSON

Marcus's additions:
- Confidence at decision time
- Escalation threshold visible in trace
- Examiner-readable answer to "why didn't this escalate"
"""
from __future__ import annotations

import uuid
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Optional


@dataclass
class TraceEntry:
    step_id: str
    agent_name: str
    started_at: datetime
    completed_at: datetime
    inputs: dict[str, Any]
    output: Any
    model_version: Optional[str] = None
    retrieved_context: Optional[list[str]] = None
    rule_applied: Optional[str] = None
    confidence: Optional[float] = None
    escalation_threshold: Optional[float] = None
    human_reviewed: bool = False
    human_review_decision: Optional[str] = None
    human_review_reason: Optional[str] = None

    @property
    def duration_ms(self) -> int:
        return int((self.completed_at - self.started_at).total_seconds() * 1000)


@dataclass
class AuditTrace:
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    claim_id: str = ""
    started_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    entries: list[TraceEntry] = field(default_factory=list)
    final_output: Any = None
    final_decision: Optional[str] = None  # "auto_send" | "adjuster_review" | "escalate"
    final_decision_reason: Optional[str] = None

    def add(self, entry: TraceEntry) -> None:
        self.entries.append(entry)

    def close(self, final_output: Any, decision: str, reason: str = "") -> None:
        self.completed_at = datetime.utcnow()
        self.final_output = final_output
        self.final_decision = decision
        self.final_decision_reason = reason

    def to_examiner_summary(self) -> str:
        """Human-readable summary an NAIC examiner can read without specialized tools.

        This is the artifact Tom asked for: 'Don't give me JSON; give me a one-page
        summary with drilldown links.' For now we render the one-page summary; the
        drilldown links would point into the full trace JSON in a real deployment.
        """
        lines: list[str] = []
        lines.append(f"AUDIT TRACE — Claim {self.claim_id or '(unknown)'}")
        lines.append(f"Trace ID: {self.trace_id}")
        lines.append(f"Started: {self.started_at.isoformat()}Z")
        if self.completed_at:
            lines.append(f"Completed: {self.completed_at.isoformat()}Z")
            lines.append(f"Total duration: {int((self.completed_at - self.started_at).total_seconds() * 1000)} ms")
        lines.append("")
        lines.append("STEPS")
        lines.append("-" * 60)
        for i, e in enumerate(self.entries, 1):
            lines.append(f"{i}. {e.agent_name}  [{e.duration_ms} ms]")
            if e.model_version:
                lines.append(f"   Model: {e.model_version}")
            if e.rule_applied:
                lines.append(f"   Rule: {e.rule_applied}")
            if e.confidence is not None:
                lines.append(f"   Confidence: {e.confidence:.2f}")
            if e.escalation_threshold is not None:
                lines.append(f"   Escalation threshold: {e.escalation_threshold:.2f}")
            if e.human_reviewed:
                lines.append(f"   Human review: {e.human_review_decision} ({e.human_review_reason or '—'})")
        lines.append("")
        lines.append("DECISION")
        lines.append("-" * 60)
        lines.append(f"Final decision: {self.final_decision}")
        if self.final_decision_reason:
            lines.append(f"Reason: {self.final_decision_reason}")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        return asdict(self)
