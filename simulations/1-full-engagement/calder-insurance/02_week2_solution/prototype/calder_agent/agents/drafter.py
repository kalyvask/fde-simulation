"""DrafterAgent — LLM-backed acknowledgment writer.

This is the only agent in v1 where an LLM gets to synthesize natural language.
Everything else is deterministic. The drafter takes verified structured fields
from Intake plus tone signals from the policy library and produces a draft
acknowledgment that follows Janet's 5-element comm-quality bar.

Falls back to a deterministic mock if ANTHROPIC_API_KEY is not set, so the
scaffold runs without a key for code-reading.
"""
from __future__ import annotations

import json
import os
from typing import Any

from calder_agent.agents.base import BaseAgent, AgentResult

# Load .env from cwd (so running scripts from prototype/ picks it up).
# override=True ensures empty-string env vars don't block the .env value.
try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass

ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")


SYSTEM_PROMPT = """You draft FNOL acknowledgments for Calder Specialty Insurance.

You MUST follow this comm-quality bar (sourced from senior adjuster interviews):
1. Address the claimant by their actual name (provided in fields)
2. Summarize the claim in their own words from the incident description
3. Plain-language next step
4. Plannable timeline — use exactly the timeline_days value provided
5. A person to call by name with phone number (use exactly contact_name and contact_phone)

You MUST NOT:
- Invent any number not in the inputs (deductible amount, policy limits, settlement value)
- Promise an outcome (coverage decision, settlement, repair authorization)
- Use generic timelines like "30 days" — use exactly timeline_days
- Use form-letter phrasing

Tone: warm if tone_flag is "warmer", professional otherwise.

Output ONLY the acknowledgment text. No preamble, no explanation, no markdown."""


class DrafterAgent(BaseAgent):
    name = "drafter"
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
        if self.mode == "anthropic":
            text = self._draft_via_anthropic(inputs)
        else:
            text = self._draft_via_mock(inputs)

        return AgentResult(
            output={"draft_text": text, "drafter_mode": self.mode},
            confidence=None,  # the tone supervisor (not yet built) will assign
            rule_applied="drafter.llm_synthesis_from_structured_fields",
        )

    def _draft_via_anthropic(self, inputs: dict[str, Any]) -> str:
        user = "Inputs:\n" + json.dumps(inputs, indent=2, default=str)
        resp = self.client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=600,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user}],
        )
        return resp.content[0].text.strip()

    def _draft_via_mock(self, inputs: dict[str, Any]) -> str:
        """Deterministic fallback so the scaffold runs without an API key."""
        name = inputs.get("claimant_name", "there")
        timeline_days = inputs.get("timeline_days", 14)
        contact_name = inputs.get("contact_name", "the Calder Claims Team")
        contact_phone = inputs.get("contact_phone", "555-0100")
        incident_desc = inputs.get("incident_description", "your recent incident")
        is_warmer = inputs.get("tone_flag") == "warmer"

        opening = (
            f"Hi {name},\n\nWelcome to Calder. I'm sorry you're dealing with this — "
            if is_warmer else f"Hi {name},\n\n"
        )

        return (
            f"{opening}"
            f"I've received your claim regarding the following: \"{incident_desc}\". "
            f"Here's what happens next: I'll have an estimate appointment scheduled for you "
            f"within {timeline_days} business days. "
            f"If anything changes in the meantime, please reach me directly at {contact_phone}.\n\n"
            f"Best,\n{contact_name}"
        )
