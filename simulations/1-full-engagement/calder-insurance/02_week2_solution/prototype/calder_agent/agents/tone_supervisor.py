"""ToneSupervisorAgent — LLM-as-judge against Janet's 5-element comm-quality bar.

Janet's bar (sourced verbatim from her week-1 interview):
  1. Name spelled right
  2. Claim summarized in claimant's own words
  3. Plain-language next step
  4. Plannable timeline (specific days, not "soon")
  5. A person to call by name with phone number

Pattern: hybrid LLM-as-judge with deterministic fallback.
- Real Anthropic call when ANTHROPIC_API_KEY is set
- Substring-based mock judgment otherwise (so the scaffold runs without a key)

Returns per-element grade + overall pass/fail + plain-English confidence.
The workforce uses overall_pass to decide whether to escalate.

Why LLM-as-judge for tone: tone is fuzzy. A regex can verify the name appears;
it can't verify the comm reads like Janet's "the comp/collision ones I'd write
myself" vs "BPO templates." That's the work the LLM does.

Why a deterministic fallback: portability. Anyone reading the scaffold should
be able to run it without an API key. The mock checks shadow the LLM judgment
just enough to be useful in tests and code-walkthroughs.
"""
from __future__ import annotations

import json
import os
import re
from typing import Any

from calder_agent.agents.base import BaseAgent, AgentResult

try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass

ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")


JUDGE_SYSTEM_PROMPT = """You grade FNOL acknowledgment drafts against a strict comm-quality bar.

The bar is 5 elements (sourced from a senior adjuster's interview):
1. NAME_CORRECT — claimant's name appears, spelled exactly as in claimant_name
2. CLAIM_SUMMARIZED — draft summarizes the incident using language reflecting incident_description (not a generic placeholder)
3. PLAIN_LANGUAGE_NEXT_STEP — draft tells the claimant what happens next in plain, non-jargon language
4. PLANNABLE_TIMELINE — a specific number of days appears (matching timeline_days); never "soon" or "shortly"
5. PERSON_TO_CALL — a named person with a phone number is provided (matching contact_name and contact_phone)

Return ONLY a JSON object with this exact shape:
{
  "elements": {
    "name_correct": {"pass": true, "evidence": "string"},
    "claim_summarized": {"pass": true, "evidence": "string"},
    "plain_language_next_step": {"pass": true, "evidence": "string"},
    "plannable_timeline": {"pass": true, "evidence": "string"},
    "person_to_call": {"pass": true, "evidence": "string"}
  },
  "overall_pass": true,
  "confidence_plain": "very confident",
  "reasoning": "1-2 sentence summary"
}

overall_pass is true only if ALL 5 elements pass. confidence_plain is one of:
"very confident", "confident", "uncertain", "very uncertain".

Output ONLY the JSON. No preamble, no markdown fences, no explanation."""


CONFIDENCE_TO_NUMERIC = {
    "very confident": 0.95,
    "confident": 0.80,
    "uncertain": 0.50,
    "very uncertain": 0.25,
}


class ToneSupervisorAgent(BaseAgent):
    name = "tone_supervisor"
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
            grade = self._grade_via_anthropic(inputs)
        else:
            grade = self._grade_via_mock(inputs)

        confidence = CONFIDENCE_TO_NUMERIC.get(grade.get("confidence_plain", "uncertain"), 0.5)
        return AgentResult(
            output=grade,
            confidence=confidence,
            rule_applied="tone_supervisor.llm_as_judge_5_element_bar",
        )

    def _grade_via_anthropic(self, inputs: dict[str, Any]) -> dict[str, Any]:
        payload = {
            "draft": inputs["draft_text"],
            "claimant_name": inputs.get("claimant_name"),
            "incident_description": inputs.get("incident_description"),
            "timeline_days": inputs.get("timeline_days"),
            "contact_name": inputs.get("contact_name"),
            "contact_phone": inputs.get("contact_phone"),
        }
        user = "Inputs to grade:\n" + json.dumps(payload, indent=2)
        resp = self.client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=600,
            system=JUDGE_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user}],
        )
        text = resp.content[0].text.strip()
        # Strip optional markdown fences if the model adds them
        if text.startswith("```"):
            text = text.split("\n", 1)[1] if "\n" in text else text
            if text.endswith("```"):
                text = text.rsplit("```", 1)[0]
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # Fallback: mark uncertain so workforce escalates
            return {
                "elements": {},
                "overall_pass": False,
                "confidence_plain": "very uncertain",
                "reasoning": f"Could not parse grader output: {text[:120]}",
            }

    def _grade_via_mock(self, inputs: dict[str, Any]) -> dict[str, Any]:
        draft = (inputs.get("draft_text") or "").lower()
        name = (inputs.get("claimant_name") or "").strip()
        incident = inputs.get("incident_description") or ""
        timeline = inputs.get("timeline_days")
        contact_name = (inputs.get("contact_name") or "")
        contact_phone = (inputs.get("contact_phone") or "")

        # Pick a salient word from incident description (>= 5 chars)
        salient = next((w for w in incident.split() if len(w) >= 5), "")

        contact_first = contact_name.split(",")[0].strip().lower()

        elements = {
            "name_correct": {
                "pass": bool(name) and name.lower() in draft,
                "evidence": (
                    f"name '{name}' present in draft"
                    if name and name.lower() in draft else f"name '{name}' missing"
                ),
            },
            "claim_summarized": {
                "pass": bool(salient) and salient.lower() in draft,
                "evidence": (
                    f"keyword '{salient}' from incident present"
                    if salient and salient.lower() in draft else "incident keywords absent"
                ),
            },
            "plain_language_next_step": {
                "pass": any(w in draft for w in ["next", "appointment", "review", "contact", "reach", "happens"]),
                "evidence": "next-step language present" if any(
                    w in draft for w in ["next", "appointment", "review", "contact", "reach", "happens"]
                ) else "no next-step language",
            },
            "plannable_timeline": self._check_timeline(timeline, draft),
            "person_to_call": {
                "pass": (
                    (bool(contact_first) and contact_first in draft)
                    or (bool(contact_phone) and contact_phone in draft)
                ),
                "evidence": (
                    "contact info present"
                    if (contact_first and contact_first in draft) or (contact_phone and contact_phone in draft)
                    else "contact info missing"
                ),
            },
        }
        overall = all(e["pass"] for e in elements.values())
        return {
            "elements": elements,
            "overall_pass": overall,
            "confidence_plain": "very confident" if overall else "uncertain",
            "reasoning": "Mock grading via deterministic substring checks. Set ANTHROPIC_API_KEY for LLM-as-judge.",
        }

    @staticmethod
    def _check_timeline(timeline: int | None, draft: str) -> dict[str, Any]:
        """Look for the timeline number near a 'day' word, not just any digit substring.

        A phone number like '555-0100' contains '10' as a substring but is not
        a timeline reference. Require '<N> day' (or 'business day') within close
        proximity to count.
        """
        if timeline is None:
            return {"pass": False, "evidence": "timeline missing"}
        # Match "<N>" with word boundaries, followed within 24 chars by "day"
        pattern = re.compile(rf"\b{timeline}\b[^.\n]{{0,24}}?\bday", re.IGNORECASE)
        if pattern.search(draft):
            return {"pass": True, "evidence": f"timeline '{timeline}' present near 'day'"}
        return {"pass": False, "evidence": f"timeline '{timeline}' not found near 'day'"}
