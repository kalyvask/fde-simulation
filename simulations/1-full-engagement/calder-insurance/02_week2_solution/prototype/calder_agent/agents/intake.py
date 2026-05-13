"""IntakeAgent — deterministic field extraction from FNOL records.

Why deterministic: the FNOL form already has structured fields. Using an LLM
to re-extract structured data is the #1 hallucination source. We pass the
fields through unchanged so downstream agents get verified ground truth.

If the inbound channel were unstructured (phone transcript, free-text email),
this agent would have an LLM-backed sibling. v1 wedge is web + agent portal
only, so we don't need that yet.
"""
from __future__ import annotations

from typing import Any

from calder_agent.agents.base import BaseAgent, AgentResult


REQUIRED_FIELDS = [
    "claim_id", "policy_id", "channel", "lob", "state",
    "claimant_name", "incident_date", "incident_description",
]

OPTIONAL_FIELDS = [
    "vehicles", "injuries", "estimated_damage",
    "first_time_customer", "has_child_or_elderly_party",
    "has_prior_claim_in_12_months", "touches_coverage_decision",
    "touches_settlement_decision",
]


class IntakeAgent(BaseAgent):
    name = "intake"
    # No model_version — deterministic.

    def run(self, inputs: dict[str, Any]) -> AgentResult:
        fnol = inputs["fnol_record"]
        extracted: dict[str, Any] = {}

        for f in REQUIRED_FIELDS:
            if f not in fnol:
                # In real life this would route to an exception queue, not throw.
                # For the scaffold, fail loudly so we catch missing fields in tests.
                raise ValueError(f"Required field missing from FNOL: {f}")
            extracted[f] = fnol[f]

        for f in OPTIONAL_FIELDS:
            extracted[f] = fnol.get(f)

        return AgentResult(
            output=extracted,
            confidence=1.0,  # deterministic
            rule_applied="intake.deterministic_field_extraction",
        )
