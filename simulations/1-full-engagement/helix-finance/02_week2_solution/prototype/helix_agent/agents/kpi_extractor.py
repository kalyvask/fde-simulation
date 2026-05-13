"""KPIExtractorAgent — structured extraction of financial KPIs from transcripts.

Extracts revenue, EPS, gross margin, operating margin, guidance ranges from
the earnings call transcript or 10-Q text. Returns structured fields plus
the source span each number was extracted from (for downstream citation
verification).

Mock mode does deterministic regex-based extraction; real mode uses Claude
with structured-output prompting.

This is the "narrow LLM use" pattern: the LLM does the extraction (because
language varies), but the output is structured + grounded in a span so the
downstream Citation Verifier can validate every number.
"""
from __future__ import annotations

import json
import os
import re
from typing import Any

from helix_agent.agents.base import BaseAgent, AgentResult

try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass

ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")


EXTRACTOR_SYSTEM_PROMPT = """You extract structured financial KPIs from earnings call transcripts.

Return ONLY a JSON object with this shape:
{
  "revenue": {"value": "$X.XB", "source_span": "exact substring from input"},
  "eps": {"value": "$X.XX", "source_span": "..."},
  "gross_margin_pct": {"value": "XX.X%", "source_span": "..."} OR null,
  "operating_margin_pct": {"value": "XX.X%", "source_span": "..."} OR null,
  "guidance": {"value": "$X.XB to $X.XB", "source_span": "..."} OR null
}

ABSOLUTE RULES:
- Every value must come from the input. Do not invent numbers.
- Every source_span must be a verbatim substring of the input.
- If a KPI is not mentioned, set the field to null.
- Output ONLY the JSON. No preamble, no markdown fences."""


class KPIExtractorAgent(BaseAgent):
    name = "kpi_extractor"
    model_version = ANTHROPIC_MODEL

    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if api_key:
            try:
                from anthropic import Anthropic
                self.client = Anthropic(api_key=api_key)
                self.mode = "anthropic"
            except ImportError:
                self.client = None
                self.mode = "mock"
        else:
            self.client = None
            self.mode = "mock"

    def run(self, inputs: dict[str, Any]) -> AgentResult:
        transcript = inputs.get("transcript", "")
        if self.mode == "anthropic":
            kpis = self._extract_via_anthropic(transcript)
        else:
            kpis = self._extract_via_mock(transcript)

        return AgentResult(
            output={"kpis_extracted": kpis, "extractor_mode": self.mode},
            confidence=1.0 if self.mode == "anthropic" else 0.8,
            rule_applied="kpi_extractor.structured_output_with_span_grounding",
        )

    def _extract_via_anthropic(self, transcript: str) -> dict[str, Any]:
        resp = self.client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=500,
            system=EXTRACTOR_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": f"Transcript:\n{transcript}"}],
        )
        text = resp.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1] if "\n" in text else text
            if text.endswith("```"):
                text = text.rsplit("```", 1)[0]
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"revenue": None, "eps": None, "_extraction_error": text[:120]}

    def _extract_via_mock(self, transcript: str) -> dict[str, Any]:
        """Deterministic regex extraction. Less accurate; runs without an API key."""
        result: dict[str, Any] = {}

        # Revenue: $X.XB or $XB or "revenue of $X.X" patterns
        rev = re.search(r"revenue\s+(?:of\s+)?(\$?\d+(?:\.\d+)?\s*(?:M|B|million|billion))", transcript, re.IGNORECASE)
        result["revenue"] = (
            {"value": rev.group(1).strip(), "source_span": rev.group(0)} if rev else None
        )

        # EPS: $X.XX
        eps = re.search(r"EPS\s+(?:of\s+)?(\$\d+\.\d+)", transcript, re.IGNORECASE)
        if not eps:
            eps = re.search(r"earnings\s+per\s+share\s+(?:of\s+)?(\$\d+\.\d+)", transcript, re.IGNORECASE)
        result["eps"] = (
            {"value": eps.group(1).strip(), "source_span": eps.group(0)} if eps else None
        )

        # Gross margin
        gm = re.search(r"gross\s+margin\s+(?:of\s+)?(\d+(?:\.\d+)?\s*%)", transcript, re.IGNORECASE)
        result["gross_margin_pct"] = (
            {"value": gm.group(1).strip(), "source_span": gm.group(0)} if gm else None
        )

        # Operating margin (also catches "X bps expansion")
        om = re.search(r"operating\s+margin\s+(?:of\s+)?(\d+(?:\.\d+)?\s*%)", transcript, re.IGNORECASE)
        if om:
            result["operating_margin_pct"] = {"value": om.group(1).strip(), "source_span": om.group(0)}
        else:
            bps = re.search(r"(\d+\s*basis\s*points?)", transcript, re.IGNORECASE)
            result["operating_margin_pct"] = (
                {"value": bps.group(1).strip(), "source_span": bps.group(0)} if bps else None
            )

        # Guidance: "guidance ... $X.XB to $X.XB"
        guide = re.search(
            r"guidance[^.]{0,60}?(\$?\d+(?:\.\d+)?\s*[BM])\s*(?:to|-|–)\s*(\$?\d+(?:\.\d+)?\s*[BM])",
            transcript, re.IGNORECASE,
        )
        if guide:
            result["guidance"] = {
                "value": f"{guide.group(1)} to {guide.group(2)}",
                "source_span": guide.group(0),
            }
        else:
            result["guidance"] = None

        return result
