"""Unit tests for the Helix policy library."""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("ANTHROPIC_API_KEY", "")
sys.path.insert(0, str(Path(__file__).parent.parent))

from helix_agent.policy_library import (
    policy_check,
    is_mnpi_watch_list_violation,
    rule_1_no_position_sizing,
    rule_2_no_m_and_a_commentary,
    rule_3_all_numbers_must_cite,
    WATCH_LIST,
)


def test_mnpi_watch_list_blocks():
    claim = {"ticker": "MSFT_PENDING_ACQUISITION", "transcript": "Quarter results."}
    block, rule = is_mnpi_watch_list_violation(claim)
    assert block
    assert "MSFT_PENDING_ACQUISITION" in (rule or "")


def test_mnpi_watch_list_clean_passes():
    claim = {"ticker": "SAMPLE_TMT", "transcript": "Quarter results."}
    block, rule = is_mnpi_watch_list_violation(claim)
    assert not block


def test_rule_1_blocks_position_sizing():
    draft = "Strong quarter, $3.2B revenue. Recommend a long position at 3% of book."
    block, rule = rule_1_no_position_sizing(draft)
    assert block


def test_rule_1_clean_passes():
    draft = "Strong quarter, revenue $3.2B exceeded consensus $3.1B."
    block, rule = rule_1_no_position_sizing(draft)
    assert not block


def test_rule_2_blocks_acquirer_speculation():
    draft = "Strong quarter. Acquisition target speculation circulating."
    block, rule = rule_2_no_m_and_a_commentary(draft)
    assert block


def test_rule_3_blocks_uncited_number():
    draft = "Revenue was $3.2B and consensus was $3.1B, but we estimate true revenue at $5.20B."
    citations = ["transcript:line_1"]
    cited_values = ["$3.2B", "$3.1B"]
    block, rule = rule_3_all_numbers_must_cite(draft, citations, cited_values)
    assert block
    assert "$5.20" in (rule or "")


def test_rule_3_clean_passes():
    draft = "Revenue $3.2B vs consensus $3.1B."
    citations = ["transcript:line_1"]
    cited_values = ["$3.2B", "$3.1B"]
    block, rule = rule_3_all_numbers_must_cite(draft, citations, cited_values)
    assert not block


def test_rule_3_ignores_calendar_references():
    """Q3 and 2026 should NOT be flagged as uncited financial numbers."""
    draft = "Revenue $3.2B in Q3 2026."
    citations = []
    cited_values = ["$3.2B"]
    block, rule = rule_3_all_numbers_must_cite(draft, citations, cited_values)
    assert not block, f"Calendar refs falsely flagged: {rule}"


def test_aggregate_policy_check_mnpi_short_circuits():
    """If MNPI fires, no other rules are evaluated."""
    claim = {"ticker": "MSFT_PENDING_ACQUISITION", "transcript": ""}
    result = policy_check(draft="", citations=[], claim=claim)
    assert result["must_block"]
    assert result["engagement_ending"]


def test_aggregate_policy_check_all_clear():
    claim = {"ticker": "SAMPLE_TMT", "transcript": ""}
    draft = "Revenue $3.2B vs consensus $3.1B."
    result = policy_check(draft, citations=[], claim=claim, cited_values=["$3.2B", "$3.1B"])
    assert not result["must_block"]
    assert not result["engagement_ending"]
