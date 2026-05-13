"""BaseAgent — same pattern as Calder. Trace integration is automatic via execute()."""
from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from helix_agent.trace import AuditTrace, TraceEntry


@dataclass
class AgentResult:
    output: Any
    confidence: Optional[float] = None
    rule_applied: Optional[str] = None
    retrieved_context: Optional[list[str]] = None
    escalation_threshold: Optional[float] = None


class BaseAgent(ABC):
    name: str = "unnamed_agent"
    model_version: Optional[str] = None

    @abstractmethod
    def run(self, inputs: dict[str, Any]) -> AgentResult:
        ...

    def execute(self, inputs: dict[str, Any], trace: AuditTrace) -> AgentResult:
        started = datetime.utcnow()
        result = self.run(inputs)
        completed = datetime.utcnow()
        trace.add(TraceEntry(
            step_id=str(uuid.uuid4()),
            agent_name=self.name,
            started_at=started,
            completed_at=completed,
            inputs=inputs,
            output=result.output,
            model_version=self.model_version,
            retrieved_context=result.retrieved_context,
            rule_applied=result.rule_applied,
            confidence=result.confidence,
            escalation_threshold=result.escalation_threshold,
        ))
        return result
