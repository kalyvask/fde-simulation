"""Specialized agents that compose the FNOL workforce."""

from calder_agent.agents.base import BaseAgent, AgentResult
from calder_agent.agents.intake import IntakeAgent
from calder_agent.agents.drafter import DrafterAgent
from calder_agent.agents.tone_supervisor import ToneSupervisorAgent
from calder_agent.agents.compliance_critic import ComplianceCriticAgent

__all__ = [
    "BaseAgent",
    "AgentResult",
    "IntakeAgent",
    "DrafterAgent",
    "ToneSupervisorAgent",
    "ComplianceCriticAgent",
]
