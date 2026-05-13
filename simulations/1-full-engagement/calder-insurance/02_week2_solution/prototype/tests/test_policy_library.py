"""Unit tests for the deterministic policy library.

Pattern: every fixed bug becomes a test (the agent development lifecycle, Alhena death-spiral).
For new rules, add a test case here BEFORE adding the rule.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from calder_agent.policy_library import (
    policy_check,
    rule_1_child_or_elderly_party,
    rule_2_first_time_customer_warmth,
    rule_3_prior_claim_in_12_months,
    hitl_floor_check,
    get_state_policy,
    STATE_POLICIES,
)


def test_rule_1_child_or_elderly_escalates():
    claim = {"has_child_or_elderly_party": True, "state": "NJ"}
    must_escalate, rule = rule_1_child_or_elderly_party(claim)
    assert must_escalate
    assert rule == "policy.rule_1_child_or_elderly_party"


def test_rule_1_no_child_or_elderly_does_not_escalate():
    claim = {"has_child_or_elderly_party": False, "state": "NJ"}
    must_escalate, rule = rule_1_child_or_elderly_party(claim)
    assert not must_escalate
    assert rule is None


def test_rule_2_first_time_customer_warmer_tone():
    assert rule_2_first_time_customer_warmth({"first_time_customer": True})["tone_flag"] == "warmer"
    assert rule_2_first_time_customer_warmth({"first_time_customer": False})["tone_flag"] == "standard"


def test_rule_3_prior_claim_escalates():
    claim = {"has_prior_claim_in_12_months": True}
    must_escalate, rule = rule_3_prior_claim_in_12_months(claim)
    assert must_escalate
    assert rule == "policy.rule_3_prior_claim_in_12_months"


def test_hitl_floor_coverage_in_NJ_escalates():
    claim = {"touches_coverage_decision": True, "state": "NJ"}
    must_escalate, rule = hitl_floor_check(claim)
    assert must_escalate
    assert rule == "policy.hitl_floor_coverage_NJ"


def test_hitl_floor_coverage_in_PA_does_not_escalate():
    """PA does not require HITL on coverage (per Marcus's interview)."""
    claim = {"touches_coverage_decision": True, "state": "PA"}
    must_escalate, rule = hitl_floor_check(claim)
    assert not must_escalate
    assert rule is None


def test_aggregate_policy_check_all_clear():
    claim = {
        "state": "NJ",
        "has_child_or_elderly_party": False,
        "has_prior_claim_in_12_months": False,
        "first_time_customer": False,
        "touches_coverage_decision": False,
        "touches_settlement_decision": False,
    }
    result = policy_check(claim)
    assert not result["must_escalate"]
    assert "tone_standard" in result["flags"]
    assert result["rules_fired"] == []


def test_aggregate_policy_check_multiple_rules():
    claim = {
        "state": "NJ",
        "has_child_or_elderly_party": True,
        "has_prior_claim_in_12_months": True,
        "first_time_customer": True,
        "touches_coverage_decision": False,
        "touches_settlement_decision": False,
    }
    result = policy_check(claim)
    assert result["must_escalate"]
    assert "policy.rule_1_child_or_elderly_party" in result["rules_fired"]
    assert "policy.rule_3_prior_claim_in_12_months" in result["rules_fired"]
    assert "tone_warmer" in result["flags"]


def test_state_policy_default_falls_back_to_NJ():
    """Marcus's guidance: any state not explicitly mapped defaults to NJ standards."""
    nj = STATE_POLICIES["NJ"]
    assert get_state_policy("XX") == nj


def test_strict_states_marked_correctly():
    """Marcus's 4-state strict map."""
    assert STATE_POLICIES["NJ"].requires_hitl_on_coverage
    assert STATE_POLICIES["NY"].requires_hitl_on_coverage
    assert STATE_POLICIES["PA"].strict_on_accuracy
    assert STATE_POLICIES["NY"].strict_on_systemic_pattern
    assert STATE_POLICIES["MA"].strict_on_documentation
