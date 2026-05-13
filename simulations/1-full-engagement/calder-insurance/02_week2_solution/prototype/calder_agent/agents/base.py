"""BaseAgent — every agent inherits from this. Trace integration is automatic.

Pattern: subclasses implement run(); the framework wraps run() with trace
bookkeeping via execute(). This means every agent automatically produces an
audit trace entry on every call without the agent author having to remember.
"""
from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from calder_agent.trace import AuditTrace, TraceEntry


@dataclass
class AgentResult:
    output: Any
    confidence: Optional[float] = None
    rule_applied: Optional[str] = None
    retrieved_context: Optional[list[str]] = None
    escalation_threshold: Optional[float] = None


class BaseAgent(ABC):
    """Every agent has a name, an optional model_version, and a run() method.

    The framework wraps run() with execute() to enforce trace bookkeeping —
    you don't have to remember to log; you can't forget."""
    name: str = "unnamed_agent"
    model_version: Optional[str] = None  # set if LLM-backed

    @abstractmethod
    def run(self, inputs: dict[str, Any]) -> AgentResult:
        """Subclasses implement business logic here. Do NOT touch trace directly;
        the framework does it via execute()."""
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
