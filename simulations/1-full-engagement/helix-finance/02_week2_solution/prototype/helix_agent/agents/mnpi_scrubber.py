"""MNPIScrubberAgent — FIRST agent in the pipeline.

If this fires, NO LLM call ever happens. The note is blocked at compliance and
the engagement-ending scenario is prevented. This is the architectural
implementation of the hardest compliance wall.

Two deterministic checks:
1. MNPI watch-list pattern match in any input field
2. Position-sizing / M&A speculation language in input transcript or filing

Either check firing means we block the workflow and escalate to compliance.
No LLM call ever happens. The cost of a single MNPI leak or position-sizing
recommendation flowing through is potentially fund-shutting.
"""
from __future__ import annotations

from typing import Any

from helix_agent.agents.base import BaseAgent, AgentResult
from helix_agent.policy_library import (
    is_mnpi_watch_list_violation,
    is_input_compliance_violation,
)


class MNPIScrubberAgent(BaseAgent):
    name = "mnpi_scrubber"
    # No model_version — deterministic.

    def run(self, inputs: dict[str, Any]) -> AgentResult:
        claim = inputs.get("claim", {})

        # Layer 1: MNPI watch-list (hardest wall)
        must_block, rule = is_mnpi_watch_list_violation(claim)
        if must_block:
            return AgentResult(
                output={
                    "must_block": True,
                    "rule_fired": rule,
                    "ticker": claim.get("ticker"),
                },
                confidence=1.0,
                rule_applied=rule,
            )

        # Layer 2: input compliance violations (position-sizing, M&A in source)
        must_block, rule = is_input_compliance_violation(claim)
        if must_block:
            return AgentResult(
                output={
                    "must_block": True,
                    "rule_fired": rule,
                    "ticker": claim.get("ticker"),
                },
                confidence=1.0,
                rule_applied=rule,
            )

        # Both layers clear — proceed to LLM pipeline
        return AgentResult(
            output={
                "must_block": False,
                "rule_fired": None,
                "ticker": claim.get("ticker"),
            },
            confidence=1.0,
            rule_applied="policy.mnpi_watch_list_clear",
        )
