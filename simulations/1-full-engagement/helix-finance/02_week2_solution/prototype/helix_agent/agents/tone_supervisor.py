"""ToneSupervisorAgent — LLM-as-judge against Helix's note-quality bar.

Rachel Kim's note-quality bar (analogue of Janet's 5-element bar in Calder):
  1. Headline reflects what actually changed this quarter (not generic)
  2. KPIs vs consensus stated factually with deltas
  3. Tone-shift summary captures management's language change
  4. Risk-factor diff identifies new items vs prior quarter
  5. Outlook section is factual, no recommendations, no MNPI-adjacent speculation

Hybrid LLM-as-judge with deterministic fallback. Same pattern as Calder's
ToneSupervisor — finance-specific rubric.
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


JUDGE_SYSTEM_PROMPT = """You grade buy-side earnings-note drafts against a strict 5-element bar.

The 5 elements (from senior analyst Rachel Kim):
1. HEADLINE_SPECIFIC — headline reflects what actually changed this quarter (not generic like "solid quarter")
2. KPIS_WITH_DELTAS — actual vs consensus stated factually with explicit deltas
3. TONE_SHIFT_CAPTURED — management's language change vs prior calls is named (e.g. "robust" → "solid")
4. RISK_FACTOR_DIFF — new risk factors from MD&A diff are identified (or explicitly noted as "no new risks")
5. OUTLOOK_FACTUAL — outlook section is factual, no BUY/SELL/position-sizing, no M&A speculation

Return ONLY a JSON object with this exact shape:
{
  "elements": {
    "headline_specific": {"pass": true|false, "evidence": "string"},
    "kpis_with_deltas": {"pass": true|false, "evidence": "string"},
    "tone_shift_captured": {"pass": true|false, "evidence": "string"},
    "risk_factor_diff": {"pass": true|false, "evidence": "string"},
    "outlook_factual": {"pass": true|false, "evidence": "string"}
  },
  "overall_pass": true|false (true only if all 5 elements pass),
  "confidence_plain": "very confident" | "confident" | "uncertain" | "very uncertain",
  "reasoning": "1-2 sentence summary"
}

Output ONLY the JSON. No preamble, no markdown fences."""


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
            "draft": inputs.get("draft_text"),
            "ticker": inputs.get("ticker"),
            "quarter": inputs.get("quarter"),
            "kpis": inputs.get("kpis_extracted"),
            "consensus": inputs.get("consensus"),
            "prior_quarter_note_excerpt": inputs.get("prior_quarter_note", "")[:500] if inputs.get("prior_quarter_note") else None,
        }
        resp = self.client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=600,
            system=JUDGE_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": "Inputs to grade:\n" + json.dumps(payload, indent=2, default=str)}],
        )
        text = resp.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1] if "\n" in text else text
            if text.endswith("```"):
                text = text.rsplit("```", 1)[0]
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {
                "elements": {},
                "overall_pass": False,
                "confidence_plain": "very uncertain",
                "reasoning": f"Could not parse grader output: {text[:120]}",
            }

    def _grade_via_mock(self, inputs: dict[str, Any]) -> dict[str, Any]:
        draft = (inputs.get("draft_text") or "").lower()
        ticker = (inputs.get("ticker") or "").lower()
        kpis = inputs.get("kpis_extracted") or {}

        elements = {
            "headline_specific": {
                "pass": bool(ticker) and ticker in draft and "headline" in draft,
                "evidence": "ticker + headline keyword present" if (ticker and ticker in draft and "headline" in draft) else "generic headline",
            },
            "kpis_with_deltas": {
                "pass": any(k in draft for k in ["consensus", "vs consensus", "delta"]) and any(
                    s in draft for s in ["$", "%"]
                ),
                "evidence": "consensus comparison present" if "consensus" in draft else "no consensus delta",
            },
            "tone_shift_captured": {
                "pass": any(w in draft for w in ["tone", "shift", "language", "prior quarter", "vs q"]),
                "evidence": "tone-shift language present" if any(w in draft for w in ["tone", "shift", "language"]) else "no tone-shift",
            },
            "risk_factor_diff": {
                "pass": any(w in draft for w in ["risk factor", "new risk", "no new risk", "mda", "md&a"]),
                "evidence": "risk-factor language present" if any(w in draft for w in ["risk factor", "no new risk"]) else "no risk-diff",
            },
            "outlook_factual": {
                "pass": not any(w in draft for w in ["buy ", "sell ", "long ", "short ", "position size"]),
                "evidence": "no recommendation language" if not any(w in draft for w in ["buy ", "sell "]) else "recommendation leak",
            },
        }
        overall = all(e["pass"] for e in elements.values())
        return {
            "elements": elements,
            "overall_pass": overall,
            "confidence_plain": "very confident" if overall else "uncertain",
            "reasoning": "Mock grading via deterministic substring checks. Set ANTHROPIC_API_KEY for LLM-as-judge.",
        }
