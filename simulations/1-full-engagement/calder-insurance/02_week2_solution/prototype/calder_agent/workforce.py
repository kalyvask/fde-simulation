"""Workforce — orchestrates the agents end-to-end for one FNOL claim.

In v1 the chain is:
  Intake → Drafter → ToneSupervisor → ComplianceCritic → Routing decision

Why this order:
- Intake produces verified structured fields
- Drafter synthesizes a natural-language acknowledgment
- ToneSupervisor (LLM-as-judge) grades against Janet's 5-element comm-quality bar
- ComplianceCritic runs deterministic policy + state-SLA + draft sanity checks
- Routing decision is deterministic over upstream outputs

Future agents (left as exercises):
  - SendAgent (Twilio + email gateway integration)
  - AuditLoggerAgent (Splunk ingestion of the trace)
"""
from __future__ import annotations

from typing import Any

from calder_agent.agents.intake import IntakeAgent
from calder_agent.agents.drafter import DrafterAgent
from calder_agent.agents.tone_supervisor import ToneSupervisorAgent
from calder_agent.agents.compliance_critic import ComplianceCriticAgent
from calder_agent.policy_library import get_state_policy, rule_2_first_time_customer_warmth
from calder_agent.trace import AuditTrace


DEFAULT_CONTACT_NAME = "Sarah Cole, Calder Claims"
DEFAULT_CONTACT_PHONE = "555-0100"


class Workforce:
    def __init__(self):
        self.intake = IntakeAgent()
        self.drafter = DrafterAgent()
        self.tone = ToneSupervisorAgent()
        self.critic = ComplianceCriticAgent()

    def process_fnol(self, fnol_record: dict[str, Any]) -> tuple[dict, AuditTrace]:
        trace = AuditTrace(claim_id=fnol_record.get("claim_id", "unknown"))

        # 1. Intake — deterministic field extraction
        intake_result = self.intake.execute({"fnol_record": fnol_record}, trace)
        claim_facts = intake_result.output

        # 2. Build drafter inputs
        state_policy = get_state_policy(claim_facts.get("state", "NJ"))
        tone_signal = rule_2_first_time_customer_warmth(claim_facts)
        drafter_inputs = {
            **claim_facts,
            "timeline_days": state_policy.first_status_sla_days,
            "contact_name": DEFAULT_CONTACT_NAME,
            "contact_phone": DEFAULT_CONTACT_PHONE,
            "tone_flag": tone_signal["tone_flag"],
        }

        # 3. Draft (LLM-backed)
        draft_result = self.drafter.execute(drafter_inputs, trace)
        draft_text = draft_result.output["draft_text"]

        # 4. ToneSupervisor — LLM-as-judge against Janet's 5-element bar
        tone_inputs = {
            "draft_text": draft_text,
            "claimant_name": claim_facts.get("claimant_name"),
            "incident_description": claim_facts.get("incident_description"),
            "timeline_days": drafter_inputs["timeline_days"],
            "contact_name": DEFAULT_CONTACT_NAME,
            "contact_phone": DEFAULT_CONTACT_PHONE,
        }
        tone_result = self.tone.execute(tone_inputs, trace)

        # 5. Compliance check (deterministic)
        critic_result = self.critic.execute(
            {
                "claim_facts": claim_facts,
                "draft_text": draft_text,
                "timeline_days": drafter_inputs["timeline_days"],
            },
            trace,
        )

        # Build the comm-quality violation list from tone supervisor
        tone_violations: list[dict[str, Any]] = []
        if not tone_result.output.get("overall_pass", True):
            failed_elements = [
                k for k, v in tone_result.output.get("elements", {}).items()
                if not v.get("pass")
            ]
            tone_violations.append({
                "rule": "comm_quality_bar",
                "severity": "high",
                "detail": f"Tone supervisor failed elements: {', '.join(failed_elements)}",
                "evidence": tone_result.output.get("reasoning", ""),
            })

        all_violations = critic_result.output["violations"] + tone_violations

        # 6. Routing decision
        if critic_result.output["must_escalate"]:
            decision = "adjuster_review"
            reason = "Policy library required escalation: " + ", ".join(
                critic_result.output["rules_fired"]
            )
        elif all_violations:
            decision = "adjuster_review"
            reason = "Quality/compliance critics surfaced violations: " + "; ".join(
                v["rule"] for v in all_violations
            )
        else:
            decision = "auto_send"
            reason = "All deterministic checks + tone supervisor passed; no policy escalation triggered."

        trace.close(final_output=draft_text, decision=decision, reason=reason)

        return (
            {
                "draft": draft_text,
                "decision": decision,
                "reason": reason,
                "violations": all_violations,
                "policy_flags": critic_result.output["policy_flags"],
                "rules_fired": critic_result.output["rules_fired"],
                "tone_grade": tone_result.output,
            },
            trace,
        )
