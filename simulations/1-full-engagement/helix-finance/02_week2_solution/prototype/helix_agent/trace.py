"""AuditTrace data model — same pattern as Calder, finance-specific naming.

Designed to satisfy FINRA / SEC / internal-compliance audit-trace standards.
Pattern: every agent writes to a TraceEntry on every call. Trace is a
first-class artifact for the compliance officer's pre-publication review.
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
    note_id: str = ""  # finance equivalent of claim_id
    ticker: str = ""
    quarter: str = ""  # e.g., "Q3 2026"
    started_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    entries: list[TraceEntry] = field(default_factory=list)
    final_output: Any = None
    final_decision: Optional[str] = None  # "publish_ready" | "analyst_review" | "compliance_block"
    final_decision_reason: Optional[str] = None
    mnpi_block: bool = False  # critical flag for compliance audit

    def add(self, entry: TraceEntry) -> None:
        self.entries.append(entry)

    def close(self, final_output: Any, decision: str, reason: str = "", mnpi_block: bool = False) -> None:
        self.completed_at = datetime.utcnow()
        self.final_output = final_output
        self.final_decision = decision
        self.final_decision_reason = reason
        self.mnpi_block = mnpi_block

    def to_compliance_summary(self) -> str:
        """Human-readable summary for Mei's pre-publication compliance review."""
        lines: list[str] = []
        lines.append(f"NOTE TRACE — {self.ticker} {self.quarter}")
        lines.append(f"Note ID: {self.note_id}")
        lines.append(f"Trace ID: {self.trace_id}")
        lines.append(f"Started: {self.started_at.isoformat()}Z")
        if self.completed_at:
            lines.append(f"Completed: {self.completed_at.isoformat()}Z")
        if self.mnpi_block:
            lines.append("")
            lines.append("*** MNPI WATCH-LIST BLOCK ***")
            lines.append("This note was blocked at the MNPI Scrubber. No LLM call occurred.")
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
        lines.append("")
        lines.append("DECISION")
        lines.append("-" * 60)
        lines.append(f"Final decision: {self.final_decision}")
        if self.final_decision_reason:
            lines.append(f"Reason: {self.final_decision_reason}")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        return asdict(self)
