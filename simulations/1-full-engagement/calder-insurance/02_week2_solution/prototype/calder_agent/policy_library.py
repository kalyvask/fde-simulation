"""Marcus's policy library — encoded as deterministic Python.

Three unwritten rules surfaced from the Marcus interview become deterministic
guardrails (NOT prompts). State-by-state SLAs and HITL floors are also encoded
as data structures, never as LLM judgment.

The principle: policy is not judgment. If a rule can be expressed as a check,
it MUST be expressed as a check. Reserve LLM judgment for synthesis tasks where
the desired output is natural language and the rule space is unbounded.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class StatePolicy:
    state: str
    ack_sla_hours: int
    first_status_sla_days: int
    requires_hitl_on_coverage: bool
    requires_hitl_on_settlement: bool
    strict_on_accuracy: bool = False
    strict_on_documentation: bool = False
    strict_on_systemic_pattern: bool = False


# Marcus's 4-state strict map. Other states default to NJ standards (his guidance).
STATE_POLICIES: dict[str, StatePolicy] = {
    # Strict states (Marcus's headache list)
    "NJ": StatePolicy("NJ", 24, 10, True, True),
    "PA": StatePolicy("PA", 24, 10, False, True, strict_on_accuracy=True),
    "NY": StatePolicy("NY", 24, 10, True, True, strict_on_systemic_pattern=True),
    "MA": StatePolicy("MA", 24, 10, False, False, strict_on_documentation=True),
    # Looser states — design to NJ standards anyway
    "CT": StatePolicy("CT", 24, 10, False, False),
    "RI": StatePolicy("RI", 24, 10, False, False),
    "VT": StatePolicy("VT", 24, 10, False, False),
    "NH": StatePolicy("NH", 24, 10, False, False),
    "ME": StatePolicy("ME", 24, 10, False, False),
    "DE": StatePolicy("DE", 24, 10, False, False),
    "MD": StatePolicy("MD", 24, 10, False, False),
    "WV": StatePolicy("WV", 24, 10, False, False),
}


def get_state_policy(state: str) -> StatePolicy:
    """Default to NJ standards for any state not explicitly mapped."""
    return STATE_POLICIES.get(state, STATE_POLICIES["NJ"])


# ----------------------------------------------------------------------------
# Marcus's 3 unwritten rules. Each is a small function so it is unit-testable
# and separately versioned.
# ----------------------------------------------------------------------------

def rule_1_child_or_elderly_party(claim: dict[str, Any]) -> tuple[bool, str | None]:
    """Rule 1: claim with a child or elderly party → default-conservative, escalate.

    Marcus quote: 'Default-conservative, escalate even if the model would auto-send.'
    """
    if claim.get("has_child_or_elderly_party"):
        return True, "policy.rule_1_child_or_elderly_party"
    return False, None


def rule_2_first_time_customer_warmth(claim: dict[str, Any]) -> dict[str, Any]:
    """Rule 2: first-time customer → first comm reads warmer than BPO standard.

    Note: this is a comm-style flag, NOT an escalation. It modifies the drafter
    inputs rather than routing the claim to a human.
    """
    if claim.get("first_time_customer"):
        return {"tone_flag": "warmer"}
    return {"tone_flag": "standard"}


def rule_3_prior_claim_in_12_months(claim: dict[str, Any]) -> tuple[bool, str | None]:
    """Rule 3: prior claim in past 12 months → human adjuster regardless.

    Marcus quote: 'Route to a human adjuster regardless of what the model says.'
    Hassan's QA spreadsheet has the same rule baked in independently — convergent
    evidence from two stakeholders.
    """
    if claim.get("has_prior_claim_in_12_months"):
        return True, "policy.rule_3_prior_claim_in_12_months"
    return False, None


# ----------------------------------------------------------------------------
# HITL floor — state-mandated human-in-the-loop requirements.
# v1 wedge does NOT touch coverage decisions, so this rarely triggers in v1.
# Encoded so v2 expansion is safe.
# ----------------------------------------------------------------------------

def hitl_floor_check(claim: dict[str, Any]) -> tuple[bool, str | None]:
    state = claim.get("state", "NJ")
    policy = get_state_policy(state)
    if claim.get("touches_coverage_decision") and policy.requires_hitl_on_coverage:
        return True, f"policy.hitl_floor_coverage_{state}"
    if claim.get("touches_settlement_decision") and policy.requires_hitl_on_settlement:
        return True, f"policy.hitl_floor_settlement_{state}"
    return False, None


# ----------------------------------------------------------------------------
# Aggregate check used by the ComplianceCriticAgent.
# ----------------------------------------------------------------------------

def policy_check(claim: dict[str, Any]) -> dict[str, Any]:
    """Run all deterministic policy checks. Returns flags, escalation requirement,
    and the rules that fired (for the audit trace)."""
    rules_fired: list[str] = []
    flags: list[str] = []
    must_escalate = False

    escalate, rule = rule_1_child_or_elderly_party(claim)
    if escalate:
        must_escalate = True
        rules_fired.append(rule)
        flags.append("conservative_mode")

    tone = rule_2_first_time_customer_warmth(claim)
    flags.append(f"tone_{tone['tone_flag']}")

    escalate, rule = rule_3_prior_claim_in_12_months(claim)
    if escalate:
        must_escalate = True
        rules_fired.append(rule)
        flags.append("prior_claim_route_to_human")

    escalate, rule = hitl_floor_check(claim)
    if escalate:
        must_escalate = True
        rules_fired.append(rule)
        flags.append("hitl_floor")

    return {
        "must_escalate": must_escalate,
        "flags": flags,
        "rules_fired": rules_fired,
    }
