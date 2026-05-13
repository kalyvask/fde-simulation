"""ComplianceCriticAgent — Mei Liu's deterministic policy check on the draft.

Three responsibilities:
1. Verify no position-sizing recommendations leaked in (rule 1)
2. Verify no M&A speculation (rule 2)
3. Verify every cited financial number traces to a cited value or source span (rule 3)

All deterministic. Same architectural pattern as Calder's ComplianceCritic.
"""
from __future__ import annotations

from typing import Any

from helix_agent.agents.base import BaseAgent, AgentResult
from helix_agent.policy_library import policy_check


class ComplianceCriticAgent(BaseAgent):
    name = "compliance_critic"

    def run(self, inputs: dict[str, Any]) -> AgentResult:
        draft = inputs["draft_text"]
        citations = inputs.get("citations", [])
        cited_values = inputs.get("cited_values", [])
        claim = inputs.get("claim_facts", {})

        result = policy_check(draft, citations, claim=claim, cited_values=cited_values)
        passes = not result["must_block"]

        return AgentResult(
            output={
                "passes": passes,
                "must_block": result["must_block"],
                "engagement_ending": result.get("engagement_ending", False),
                "flags": result["flags"],
                "rules_fired": result["rules_fired"],
            },
            confidence=1.0,
            escalation_threshold=1.0,
            rule_applied="compliance_critic.deterministic_policy_check",
        )
