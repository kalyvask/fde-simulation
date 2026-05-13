"""MNPIScrubberAgent — FIRST agent in the pipeline.

If this fires, NO LLM call ever happens. The note is blocked at compliance and
the engagement-ending scenario is prevented. This is the architectural
implementation of Mei's hardest wall.

This is deterministic by design. The cost of a single MNPI leak through an
LLM is potentially fund-shutting. No LLM judgment is involved.
"""
from __future__ import annotations

from typing import Any

from helix_agent.agents.base import BaseAgent, AgentResult
from helix_agent.policy_library import is_mnpi_watch_list_violation


class MNPIScrubberAgent(BaseAgent):
    name = "mnpi_scrubber"
    # No model_version — deterministic.

    def run(self, inputs: dict[str, Any]) -> AgentResult:
        claim = inputs.get("claim", {})
        must_block, rule = is_mnpi_watch_list_violation(claim)
        return AgentResult(
            output={
                "must_block": must_block,
                "rule_fired": rule,
                "ticker": claim.get("ticker"),
            },
            confidence=1.0,
            rule_applied=rule or "policy.mnpi_watch_list_clear",
        )
