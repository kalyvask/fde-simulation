"""CitationVerifierAgent — deterministic check that every cited number traces to a source span.

Sarah's kill-criteria #1 enforcement. Every monetary, percentage, or
basis-point number in the draft must:
1. Be present in the kpis_extracted output (with its source span), OR
2. Be present in the consensus comparison (with its source), OR
3. Be a calendar reference (Q3, 2026) — these are not financial numbers

Deterministic. No LLM judgment.
"""
from __future__ import annotations

import re
from typing import Any

from helix_agent.agents.base import BaseAgent, AgentResult


FINANCIAL_NUMBER_PATTERNS = [
    r"\$\d+(?:\.\d+)?(?:\s*(?:M|B|K|million|billion|trillion))?",
    r"\d+(?:\.\d+)?\s*(?:%|percent)",
    r"\d+(?:\.\d+)?\s*(?:basis\s*points|bps)",
    r"\d+(?:\.\d+)?\s*(?:million|billion|trillion)\b",
]


def _normalize(s: str) -> str:
    return re.sub(r"\s+", "", s.lower())


def _extract_financial_numbers(text: str) -> list[str]:
    found: list[str] = []
    for pattern in FINANCIAL_NUMBER_PATTERNS:
        found.extend(re.findall(pattern, text, re.IGNORECASE))
    return found


class CitationVerifierAgent(BaseAgent):
    name = "citation_verifier"

    def run(self, inputs: dict[str, Any]) -> AgentResult:
        draft = inputs["draft_text"]
        kpis = inputs.get("kpis_extracted", {})
        consensus = inputs.get("consensus", {})

        # Gather all values that ARE allowed to be cited
        allowed_values: list[str] = []
        for kpi_key, kpi_data in (kpis or {}).items():
            if isinstance(kpi_data, dict) and kpi_data.get("value"):
                allowed_values.append(str(kpi_data["value"]))
            elif isinstance(kpi_data, str):
                allowed_values.append(kpi_data)
        for cons_key, cons_val in (consensus or {}).items():
            if cons_val:
                allowed_values.append(str(cons_val))

        norm_allowed = {_normalize(v) for v in allowed_values}

        draft_numbers = _extract_financial_numbers(draft)
        uncited: list[str] = []
        for num in draft_numbers:
            n = _normalize(num)
            if n in norm_allowed:
                continue
            if any(n in a for a in norm_allowed):
                continue
            uncited.append(num)

        passes = len(uncited) == 0

        return AgentResult(
            output={
                "passes": passes,
                "draft_numbers_found": draft_numbers,
                "allowed_values": allowed_values,
                "uncited_numbers": uncited,
            },
            confidence=1.0,
            rule_applied="citation_verifier.deterministic_number_grounding",
        )
