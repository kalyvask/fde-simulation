"""Workforce — orchestrates the Helix earnings-note workforce end-to-end.

Pipeline:
  1. MNPI Scrubber — first; deterministic; if fires, halt before any LLM call
  2. Intake — extract structured fields
  3. KPI Extractor — structured extraction with span grounding (LLM with fallback)
  4. Note Drafter — LLM draft using ONLY extracted KPIs
  5. Tone Supervisor — LLM-as-judge against Rachel's 5-element bar
  6. Citation Verifier — deterministic check that every cited number traces to source
  7. Compliance Critic — deterministic policy check (Mei's 3 rules)
"""
from __future__ import annotations

from typing import Any

from helix_agent.agents.mnpi_scrubber import MNPIScrubberAgent
from helix_agent.agents.intake import IntakeAgent
from helix_agent.agents.kpi_extractor import KPIExtractorAgent
from helix_agent.agents.note_drafter import NoteDrafterAgent
from helix_agent.agents.tone_supervisor import ToneSupervisorAgent
from helix_agent.agents.citation_verifier import CitationVerifierAgent
from helix_agent.agents.compliance_critic import ComplianceCriticAgent
from helix_agent.trace import AuditTrace


class Workforce:
    def __init__(self):
        self.mnpi = MNPIScrubberAgent()
        self.intake = IntakeAgent()
        self.kpi = KPIExtractorAgent()
        self.drafter = NoteDrafterAgent()
        self.tone = ToneSupervisorAgent()
        self.citation = CitationVerifierAgent()
        self.critic = ComplianceCriticAgent()

    def process_earnings_call(self, claim: dict[str, Any]) -> tuple[dict, AuditTrace]:
        trace = AuditTrace(
            note_id=claim.get("note_id", "unknown"),
            ticker=claim.get("ticker", "UNKNOWN"),
            quarter=claim.get("quarter", "UNKNOWN"),
        )

        # 1. MNPI Scrubber — FIRST, before any LLM call
        mnpi_result = self.mnpi.execute({"claim": claim}, trace)
        if mnpi_result.output["must_block"]:
            trace.close(
                final_output=None,
                decision="compliance_block",
                reason=f"MNPI watch-list block: {mnpi_result.output['rule_fired']}",
                mnpi_block=True,
            )
            return (
                {
                    "draft": None,
                    "decision": "compliance_block",
                    "reason": "MNPI watch-list block — no LLM call made",
                    "rules_fired": [mnpi_result.output["rule_fired"]],
                    "engagement_ending_path_avoided": True,
                },
                trace,
            )

        # 2. Intake
        intake_result = self.intake.execute({"claim": claim}, trace)
        claim_facts = intake_result.output

        # 3. KPI Extractor (LLM with span grounding)
        kpi_result = self.kpi.execute({"transcript": claim_facts.get("transcript", "")}, trace)
        kpis_extracted = kpi_result.output["kpis_extracted"]

        consensus = {
            "revenue": claim_facts.get("consensus_revenue"),
            "eps": claim_facts.get("consensus_eps"),
        }

        # 4. Note Drafter (LLM, structured inputs only)
        drafter_inputs = {
            **claim_facts,
            "kpis_extracted": _kpi_values_only(kpis_extracted),
            "consensus": consensus,
        }
        draft_result = self.drafter.execute(drafter_inputs, trace)
        draft_text = draft_result.output["draft_text"]

        # 5. Tone Supervisor (LLM-as-judge against Rachel's 5-element bar)
        tone_inputs = {
            "draft_text": draft_text,
            "ticker": claim_facts.get("ticker"),
            "quarter": claim_facts.get("quarter"),
            "kpis_extracted": kpis_extracted,
            "consensus": consensus,
            "prior_quarter_note": claim.get("prior_quarter_note"),
        }
        tone_result = self.tone.execute(tone_inputs, trace)

        # 6. Citation Verifier (deterministic)
        citation_inputs = {
            "draft_text": draft_text,
            "kpis_extracted": kpis_extracted,
            "consensus": consensus,
        }
        citation_result = self.citation.execute(citation_inputs, trace)

        # 7. Compliance Critic (deterministic) — use the extracted KPI values
        cited_values = list(_kpi_values_only(kpis_extracted).values()) + [v for v in consensus.values() if v]
        critic_inputs = {
            "draft_text": draft_text,
            "citations": claim.get("citations", []),
            "cited_values": cited_values,
            "claim_facts": claim_facts,
        }
        critic_result = self.critic.execute(critic_inputs, trace)

        # Aggregate violations
        violations: list[dict[str, Any]] = []
        if not tone_result.output.get("overall_pass", True):
            failed = [k for k, v in tone_result.output.get("elements", {}).items() if not v.get("pass")]
            violations.append({"rule": "tone_quality_bar", "severity": "high", "detail": f"Failed: {', '.join(failed)}"})
        if not citation_result.output["passes"]:
            violations.append({
                "rule": "citation_uncited_numbers",
                "severity": "critical",
                "detail": f"Uncited: {citation_result.output['uncited_numbers']}",
            })

        if critic_result.output["must_block"] or violations:
            decision = "compliance_block" if critic_result.output["must_block"] else "analyst_review"
            reason = "; ".join(critic_result.output.get("rules_fired", []) + [v["rule"] for v in violations]) or "Quality / compliance flags raised"
        else:
            decision = "analyst_review"
            reason = "All deterministic + LLM-as-judge checks passed; ready for senior analyst review."

        trace.close(final_output=draft_text, decision=decision, reason=reason)

        return (
            {
                "draft": draft_text,
                "decision": decision,
                "reason": reason,
                "kpis_extracted": kpis_extracted,
                "tone_grade": tone_result.output,
                "citation_check": citation_result.output,
                "violations": violations,
                "rules_fired": critic_result.output.get("rules_fired", []),
            },
            trace,
        )


def _kpi_values_only(kpis: dict[str, Any]) -> dict[str, str]:
    """Flatten {kpi_key: {value, source_span}} into {kpi_key: value} for the drafter."""
    out: dict[str, str] = {}
    for k, v in (kpis or {}).items():
        if isinstance(v, dict) and v.get("value"):
            out[k] = v["value"]
        elif isinstance(v, str):
            out[k] = v
    return out
