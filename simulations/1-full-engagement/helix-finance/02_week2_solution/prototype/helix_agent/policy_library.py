"""Mei Liu's compliance policy library — encoded as deterministic Python.

Three layers of policy:
1. MNPI watch list (the hard wall — first agent in pipeline)
2. Mei's 3 compliance rules (analogous to Marcus's unwritten rules at Calder)
3. SEC / FINRA structural constraints (Chinese wall, fair-dealing, no-M&A-commentary)

The principle: in finance, policy is not judgment. Every rule that touches MNPI,
fair-dealing, or compliance review MUST be expressed as deterministic code.
The cost of any single failure is potentially fund-shutting.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


# ----------------------------------------------------------------------------
# MNPI Watch List
# ----------------------------------------------------------------------------
# In production: pulled from Mei's compliance system on each engagement.
# Here: synthetic 10-name watch list for the scaffold.

WATCH_LIST: set[str] = {
    "MSFT_PENDING_ACQUISITION",  # synthetic codes; in prod these are real ticker patterns
    "AAPL_REG_INVESTIGATION",
    "META_PERSONNEL_CHANGE",
    "NVDA_PENDING_SETTLEMENT",
    "TSLA_INTERNAL_AUDIT",
}


def is_mnpi_watch_list_violation(claim: dict[str, Any]) -> tuple[bool, str | None]:
    """Hard block. If any input field contains a watch-list pattern, refuse to proceed.

    Returns (must_block, rule_id) — if must_block is True, no LLM call ever happens.
    """
    text_fields = [
        str(claim.get("ticker", "")),
        str(claim.get("transcript", "")),
        str(claim.get("filing", "")),
    ]
    combined = " ".join(text_fields).upper()
    for pattern in WATCH_LIST:
        if pattern in combined:
            return True, f"policy.mnpi_watch_list:{pattern}"
    return False, None


# ----------------------------------------------------------------------------
# Mei's 3 unwritten compliance rules
# ----------------------------------------------------------------------------

def rule_1_no_position_sizing(draft: str) -> tuple[bool, str | None]:
    """Rule 1: drafts must not include position-sizing recommendations.

    Cross-Chinese-wall risk. Research informs trading via the published note,
    not via specific BUY/SELL/QUANTITY recommendations in the draft.
    """
    bad_patterns = ["buy ", "sell ", "long ", "short ", "% position", "position size", "sized at"]
    found = [p for p in bad_patterns if p.lower() in draft.lower()]
    if found:
        return True, f"policy.rule_1_position_sizing:{','.join(found)}"
    return False, None


def rule_2_no_m_and_a_commentary(draft: str) -> tuple[bool, str | None]:
    """Rule 2: drafts must not include M&A speculation.

    Regulatory minefield. Even speculation can trigger Reg FD issues if the
    speculation contains specific dollar amounts or named acquirers.
    """
    bad_patterns = ["acquisition target", "potential acquirer", "merger speculation", "bid likely"]
    found = [p for p in bad_patterns if p.lower() in draft.lower()]
    if found:
        return True, f"policy.rule_2_m_and_a:{','.join(found)}"
    return False, None


def rule_3_all_numbers_must_cite(draft: str, citations: list[str], cited_values: list[str] | None = None) -> tuple[bool, str | None]:
    """Rule 3: every financial number in the draft must trace to a cited value.

    Sarah's kill-criteria #1. Hallucinated numbers are the #1 risk.
    Deterministic enforcement of citation faithfulness.

    Looks only for financial-typed numbers (with $, %, basis-point, or unit
    suffix) — not bare year numbers like "Q3 2026" which are calendar refs.
    """
    import re

    cited_values = cited_values or []

    # Match financial-typed numbers only
    financial_patterns = [
        r"\$\d+(?:\.\d+)?(?:\s*(?:M|B|K|million|billion|trillion))?",  # $X.XB
        r"\d+(?:\.\d+)?\s*(?:%|percent)",                              # X.X%
        r"\d+(?:\.\d+)?\s*(?:basis\s*points|bps)",                     # X bps
        r"\d+(?:\.\d+)?\s*(?:million|billion|trillion)\b",             # X million
    ]
    found_numbers: list[str] = []
    for pattern in financial_patterns:
        found_numbers.extend(re.findall(pattern, draft, re.IGNORECASE))

    # A number is cited if its normalized form appears in cited_values
    # OR appears in any citation source span string
    def _norm(s: str) -> str:
        return re.sub(r"\s+", "", s.lower())

    norm_citations = [_norm(c) for c in citations]
    norm_cited_values = [_norm(v) for v in cited_values]

    uncited: list[str] = []
    for num in found_numbers:
        n = _norm(num)
        if n in norm_cited_values:
            continue
        if any(n in c for c in norm_citations):
            continue
        if any(n in c for c in norm_cited_values):
            continue
        uncited.append(num)

    if uncited:
        return True, f"policy.rule_3_uncited_numbers:{','.join(uncited[:3])}"
    return False, None


# ----------------------------------------------------------------------------
# Aggregate check used by ComplianceCriticAgent
# ----------------------------------------------------------------------------

def policy_check(
    draft: str,
    citations: list[str],
    claim: dict[str, Any] | None = None,
    cited_values: list[str] | None = None,
) -> dict[str, Any]:
    """Run all deterministic policy checks on a drafted note + citations."""
    rules_fired: list[str] = []
    flags: list[str] = []
    must_block = False

    if claim is not None:
        block, rule = is_mnpi_watch_list_violation(claim)
        if block:
            return {
                "must_block": True,
                "flags": ["mnpi_watch_list_block"],
                "rules_fired": [rule],
                "engagement_ending": True,  # this is the catastrophic case
            }

    block, rule = rule_1_no_position_sizing(draft)
    if block:
        must_block = True
        rules_fired.append(rule)
        flags.append("position_sizing_violation")

    block, rule = rule_2_no_m_and_a_commentary(draft)
    if block:
        must_block = True
        rules_fired.append(rule)
        flags.append("m_and_a_commentary_violation")

    block, rule = rule_3_all_numbers_must_cite(draft, citations, cited_values)
    if block:
        must_block = True
        rules_fired.append(rule)
        flags.append("uncited_numbers")

    return {
        "must_block": must_block,
        "flags": flags,
        "rules_fired": rules_fired,
        "engagement_ending": False,
    }
