"""IntakeAgent — parses earnings transcript + 10-Q into normalized fields.

Deterministic by design. Field extraction over structured inputs, not over
free-text claims. Same pattern as Calder's intake — finance-specific fields.
"""
from __future__ import annotations

from typing import Any

from helix_agent.agents.base import BaseAgent, AgentResult


REQUIRED_FIELDS = [
    "ticker", "quarter", "transcript", "prepared_remarks", "qa_section",
    "consensus_revenue", "consensus_eps",
]

OPTIONAL_FIELDS = [
    "filing_10q_text", "prior_quarter_note", "sector", "analyst_owner",
    "report_date", "guidance_section", "mda_section",
]


class IntakeAgent(BaseAgent):
    name = "intake"

    def run(self, inputs: dict[str, Any]) -> AgentResult:
        claim = inputs["claim"]
        extracted: dict[str, Any] = {}

        for f in REQUIRED_FIELDS:
            if f not in claim:
                raise ValueError(f"Required field missing from claim: {f}")
            extracted[f] = claim[f]

        for f in OPTIONAL_FIELDS:
            extracted[f] = claim.get(f)

        return AgentResult(
            output=extracted,
            confidence=1.0,
            rule_applied="intake.deterministic_field_extraction",
        )
