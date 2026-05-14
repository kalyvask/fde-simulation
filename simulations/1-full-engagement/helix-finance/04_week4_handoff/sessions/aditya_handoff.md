# Aditya Handoff — Week 4 Thursday, 90 min, in-person

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Operational handoff to Aditya (CTO). After this, Aditya owns the run-book, rollback, and on-call. The engagement transitions from FDE-led to customer-led on Monday.

## Setup

Thursday week 4, 2:00 PM ET. Aditya's office. He has the run-book draft I sent Wednesday, marked up with questions. His junior engineer (Priya — different Priya than the Calder one) is sitting in. Tone: businesslike, no surprises. This is the third operational handoff session over the engagement.

## Selected exchanges

**Aditya**: "Three things. Run-book. Rollback. On-call. Then 15 min on what stays mine forever vs what the FDE platform owns."

**Alex**: "Run-book first. Five sections in the doc you've got. Section 1, normal-operations cadence: per-call processing, daily checks, weekly eval re-run on every release. Section 2, alerting: what triggers a page, who gets paged. Section 3, common-mode failures and how to diagnose. Section 4, rollback. Section 5, the boundary between operational fixes (you) vs design changes (escalate)."

**Aditya**: "On section 2 — I want the alerting tied to the production monitoring dashboard, not a separate system. We already pay for Datadog; the agent's logs already ship there. Set up the alerts in Datadog, not in something new."

**Alex**: "Done. Two alerts: (1) pass-rate-drift >5% over rolling 7-day window per ticker, page on-call; (2) latency P95 >60 seconds, page on-call. Both wired to Datadog with PagerDuty integration. I'll send the alert config by EOD tomorrow."

**Aditya**: "Section 3 — common-mode failures. The one I'm most worried about is upstream data freshness. If Bloomberg or FactSet returns stale data, the agent can produce a draft that looks fine but is based on old facts. Walk me through what catches that."

**Alex**: "Two layers. First, the KPI Extractor has a timestamp check on every source pull — if the data is older than 24 hours for a current-quarter call, the agent flags the draft for analyst review with a 'data-freshness-warning' annotation. The analyst can confirm it's the right data or kick it back. Second, the Citation Verifier checks that every cited line in the source material is from the current call (matched against the call's recorded date), not from a prior call. Both deterministic."

**Aditya**: "Good. And if the upstream is completely down?"

**Alex**: "Fail closed. The KPI Extractor returns an error, the workforce stops, the note goes to a 'data-unavailable' queue with the specific error message. No draft generated. The on-call engineer's job is to diagnose whether it's the upstream or our integration. Run-book section 3 walks through both."

**Aditya**: "Rollback. Walk me through it."

**Alex**: "Every release ships with an immutable snapshot — model version, prompt hash, policy library version, watch-list version. Three layers of rollback: (1) instant — traffic shift back to the prior snapshot, automated, takes <60 seconds; (2) prompt-only rollback — revert just the drafter prompt while keeping new policy rules, takes 5 minutes; (3) full rollback — revert to a prior-week snapshot, takes 15 minutes. The decision tree for which one to use is in section 4."

**Aditya**: "Walk me through scenario one. Production is in trouble. The pass rate has dropped from 96% to 82% over 12 hours. What do I do?"

**Alex**: "First, check the dashboard for which ticker or analyst is driving the drop. If it's a single ticker (say SAMPLE_TMT, which had a one-time charge that messed with KPI extraction), no rollback — patch the policy library for that ticker only, ship as a hot-fix. If it's across the board (say a Claude model update messed with tone classification), instant rollback to the prior snapshot. Take 60 seconds. Then triage."

**Aditya**: "And if I make the wrong call?"

**Alex**: "Then the worst case is one more pass-rate dip while the second rollback is applied. The decision tree is conservative — when in doubt, rollback first, triage after. The cost of an unnecessary 5-min rollback is small; the cost of staying in degraded mode is the engagement's trust budget."

**Aditya**: "On-call. Who pages when?"

**Alex**: "First 90 days: me (FDE) on-call for design issues; you (CTO) on-call for operational issues; you and Priya share the rotation 1-week intervals. After 90 days: you and Priya own on-call entirely; I'm reachable for design escalations only, response within 24 hours, not page-able."

**Aditya**: "Design vs operational — define."

**Alex**: "Operational: anything in the run-book. Anything where the fix is a config change, a hot-fix to a single policy rule, a prompt-only rollback, or a known-pattern triage. Design: anything that requires changing the workforce orchestration, adding an agent, redesigning a deterministic check, or revisiting the trust-level structure. If you're not sure, default to operational and consult me on the next biweekly. I'd rather you ship a hot-fix than wait 24 hours."

**Aditya**: "Good. Last thing — what stays mine forever vs what the FDE platform owns?"

**Alex**: "Yours forever: run-book, alert config, rollback decision tree, on-call rotation, weekly eval re-run on every release, biweekly compliance review with Mei, biweekly hostile review with Carmen, weekly cadence with David and Rachel.

FDE platform owns: the workforce framework (BaseAgent, AuditTrace, Workforce orchestrator), the immutable-snapshot tooling, the deterministic-check primitives, the LLM-as-judge calibration helpers, the eval harness. Those are upstream. When the platform ships an update to any of those, you take it via the immutable-snapshot mechanism — you can pin a version forever if you want.

Customer-specific code (your policy library, your eval cases, your runbook) stays in your repo, your responsibility, your release cadence."

**Aditya**: "And the model itself?"

**Alex**: "Your responsibility on choice (which model, which version). FDE platform's responsibility on availability (failover between providers, BAA management). When Anthropic ships a model update, you decide whether to upgrade; the platform tells you the eval pass rate before and after; you sign off or you don't."

**Aditya**: "Clear. Where does the documentation for that live?"

**Alex**: "`helix_ops/PLATFORM_BOUNDARY.md` in your repo. I'll send by EOD."

*(15 min wrap on the 90-day transition cadence)*

**Aditya**: "Monday. We rollout. From Tuesday I'm primary. You're in slack for design escalations only. Biweekly with you for the first 90 days, then we step down."

**Alex**: "Confirmed. I'll be in the room Monday morning for the rollout but I'm not on the keyboard. From Tuesday it's your show."

*(Wraps at 87 min.)*

## Post-session captures

### What got signed off

- Run-book v1.0: 5 sections, all approved
- Alert config: 2 alerts in Datadog with PagerDuty integration
- Rollback decision tree: 3 layers, instant / prompt-only / full
- On-call rotation: 90-day shared, then customer-owned
- Platform-boundary document: customer code vs FDE platform code, model choice vs availability

### What I committed to ship by EOD Friday

1. **Alert config in Datadog**: 2 alerts wired with PagerDuty
2. **PLATFORM_BOUNDARY.md**: customer-vs-platform responsibility doc in customer's repo
3. **Run-book v1.0 final**: incorporates Aditya's edits from this session
4. **Rollback decision tree**: standalone 1-page document with the scenario walk-through

### Post-handoff cadence (locked through week 13)

| Cadence | Participants | Purpose |
|---|---|---|
| Weekly Monday standup | Aditya, Priya, Rachel, David | Production status, eval re-runs, weekly observations |
| Biweekly Tuesday review | Mei + Alex + Aditya | Compliance trace audit, policy library updates |
| Biweekly Thursday review | Carmen + David + Alex | Hostile review, reader-side transparency findings |
| Weekly Friday status | Aditya → Sarah (written) | Real numbers: pass rate, adoption, cost per note |
| Monthly all-hands | Everyone | Engagement health check |
| Quarterly external audit | Mei + outside counsel | Compliance trace standard verification |

### Stakeholder map — operational state

- **Aditya**: OPERATIONAL OWNER. From Monday primary on the keyboard. FDE design-escalation only.
- **Priya** (his junior eng): SECOND OPERATIONAL OWNER. Shared on-call rotation.
- **All other stakeholders**: stable as of demo session.

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Operational handoff rigor | 5 | All 5 run-book sections approved; rollback decision tree validated with scenario; on-call rotation locked |
| Calibrated engineering | 5 | Platform boundary doc separates customer vs FDE responsibilities clearly — Aditya can take a model update without re-engaging us |
| Risk awareness | 5 | Data-freshness failure mode caught in walk-through; rollback decision tree includes the right edge cases |
| Customer ownership | 5 | Aditya is ready to be primary from Monday. He owns the run-book, he owns the on-call, he owns the cadence |
| Trust transfer | 5 | The "I'll be in the room but not on the keyboard" gesture is the trust-transfer moment. He gets to ship; I get to watch |

**Keep**: scenario walk-throughs for rollback (not just doc); platform-boundary doc that makes the customer-vs-FDE-platform split explicit; locked cadence through week 13 with named owners.

**Fix**: should have offered the walk-through 7 days before the demo, not at the demo. James (COO) flagged this in the demo Q&A; should have heard it from Aditya in the handoff session, not the demo. The post-handoff cadence document should have been pre-circulated week 3, not week 4.

**Lesson**: operational handoff is a sequence of small disclosures, not a single big session. Every commitment I make about post-handoff support should be in writing the week before the demo, not the week of.
