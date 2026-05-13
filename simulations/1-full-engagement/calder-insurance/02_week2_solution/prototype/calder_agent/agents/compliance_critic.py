"""ComplianceCriticAgent — deterministic policy + state-SLA check on the draft.

Two responsibilities:
1. Run the policy library checks (Marcus's unwritten rules + HITL floor)
2. Sanity-check the draft text for known-bad patterns (stale templates, wrong
   timelines, prohibited content)

Why deterministic: every check here is a regulator-readable rule. Failure costs
are regulatory. We do not let an LLM make these calls.
"""
from __future__ import annotations

from typing import Any

from calder_agent.agents.base import BaseAgent, AgentResult
from calder_agent.policy_library import policy_check, get_state_policy


# Patterns that historically appeared in the two market-conduct findings.
# Tom called these out: stale-template carry-over and misleading timelines.
STALE_TEMPLATE_PHRASES = [
    "30 days",
    "we will respond within 30",
    "thirty days",
]

PROHIBITED_PROMISE_PHRASES = [
    "we will cover",
    "your claim is approved",
    "guaranteed",
    "fully covered",
]


class ComplianceCriticAgent(BaseAgent):
    name = "compliance_critic"

    def run(self, inputs: dict[str, Any]) -> AgentResult:
        claim = inputs["claim_facts"]
        draft = inputs["draft_text"]
        timeline_days = inputs.get("timeline_days", 14)

        # 1. Policy library check (Marcus's rules)
        policy_result = policy_check(claim)

        # 2. Stale-template + prohibited-promise sanity checks
        violations: list[dict[str, Any]] = []

        state = claim.get("state", "NJ")
        state_policy = get_state_policy(state)

        # Stale template check — if state SLA is shorter than 30d, "30 days" is wrong
        if state_policy.first_status_sla_days < 30:
            for phrase in STALE_TEMPLATE_PHRASES:
                if phrase.lower() in draft.lower():
                    violations.append({
                        "rule": "stale_template_30day",
                        "severity": "high",
                        "detail": (
                            f"Draft mentions '{phrase}' but {state} first-status SLA is "
                            f"{state_policy.first_status_sla_days} days."
                        ),
                    })
                    break

        # Prohibited promise check — never promise coverage in an acknowledgment
        for phrase in PROHIBITED_PROMISE_PHRASES:
            if phrase.lower() in draft.lower():
                violations.append({
                    "rule": "prohibited_promise",
                    "severity": "critical",
                    "detail": f"Draft contains promise-shaped phrase: '{phrase}'",
                })

        # Timeline accuracy — if a different timeline appears, flag
        # (lightweight check; more sophisticated parser would be a follow-on)
        if f"{timeline_days}" not in draft and "business day" in draft.lower():
            violations.append({
                "rule": "timeline_drift",
                "severity": "medium",
                "detail": f"Draft references business days but not the configured {timeline_days}.",
            })

        passes = (len(violations) == 0) and (not policy_result["must_escalate"])

        # Confidence: 1.0 because all checks are deterministic.
        # Threshold: 1.0 so any violation drops below.
        return AgentResult(
            output={
                "must_escalate": policy_result["must_escalate"],
                "policy_flags": policy_result["flags"],
                "rules_fired": policy_result["rules_fired"],
                "violations": violations,
                "passes": passes,
            },
            confidence=1.0,
            escalation_threshold=1.0,
            rule_applied="compliance_critic.deterministic_policy_check",
        )
