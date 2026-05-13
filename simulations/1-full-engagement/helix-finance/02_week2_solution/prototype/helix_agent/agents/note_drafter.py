"""NoteDrafterAgent — LLM-backed earnings-note writer.

Drafts a 1-page analyst note from extracted KPIs and verified consensus data.
The drafter NEVER sources its own numbers — every cited number must come from
the Intake or KPI Extractor outputs. The Citation Verifier downstream will
deterministically check this.

Falls back to a deterministic mock if no API key is set.
"""
from __future__ import annotations

import json
import os
from typing import Any

from helix_agent.agents.base import BaseAgent, AgentResult

try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass

ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")


SYSTEM_PROMPT = """You draft morning-after-earnings analyst notes for a buy-side equity hedge fund.

The note format is 1 page, structured as:
1. Headline (1 sentence — what changed this quarter)
2. KPIs vs consensus (table format: actual / consensus / delta, exactly as provided)
3. Tone-shift summary (1-2 sentences, neutral)
4. New risk factors (from MD&A diff if provided)
5. Outlook (1 paragraph, factual, no recommendations)

ABSOLUTE RULES:
- Use ONLY the numbers provided in the inputs. Never invent a number.
- Every number you cite must already be in the kpis_extracted or consensus inputs.
- Never include position-sizing recommendations (no BUY/SELL/quantity).
- Never include M&A speculation.
- Use exact figures from the inputs — do not round, paraphrase, or interpret.
- Tone is factual, not promotional. Buy-side analysts publish to portfolio managers, not to retail.

Output the note text only. No preamble. No markdown headers — plain text suitable for direct compliance review."""


class NoteDrafterAgent(BaseAgent):
    name = "note_drafter"
    model_version = ANTHROPIC_MODEL  # default to Anthropic; OpenAI swap is an option

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
        if self.mode == "anthropic":
            text = self._draft_via_anthropic(inputs)
        else:
            text = self._draft_via_mock(inputs)

        return AgentResult(
            output={"draft_text": text, "mode": self.mode},
            confidence=None,
            rule_applied="note_drafter.llm_synthesis_from_structured_inputs",
        )

    def _draft_via_anthropic(self, inputs: dict[str, Any]) -> str:
        user = "Inputs for note:\n" + json.dumps(inputs, indent=2, default=str)
        resp = self.client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=800,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user}],
        )
        return resp.content[0].text.strip()

    def _draft_via_mock(self, inputs: dict[str, Any]) -> str:
        ticker = inputs.get("ticker", "TICKER")
        quarter = inputs.get("quarter", "QX")
        kpis = inputs.get("kpis_extracted", {})
        consensus = inputs.get("consensus", {})

        revenue = kpis.get("revenue", "N/A")
        eps = kpis.get("eps", "N/A")
        cons_revenue = consensus.get("revenue", "N/A")
        cons_eps = consensus.get("eps", "N/A")

        return (
            f"{ticker} {quarter} — Earnings note\n\n"
            f"Headline: Reported revenue {revenue} vs consensus {cons_revenue}; "
            f"EPS {eps} vs consensus {cons_eps}.\n\n"
            f"KPIs vs consensus:\n"
            f"  Revenue: {revenue} actual / {cons_revenue} consensus\n"
            f"  EPS:     {eps} actual / {cons_eps} consensus\n\n"
            f"Tone-shift summary: (mock — Tone-Shift Detector not yet wired)\n\n"
            f"New risk factors: (mock — Risk-Factor Diff not yet wired)\n\n"
            f"Outlook: Management's guidance was provided in the prepared remarks. "
            f"See cited sections in the source transcript for specifics."
        )
