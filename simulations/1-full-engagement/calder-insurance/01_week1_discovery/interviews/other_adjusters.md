# Other Adjuster Interviews — Brief Notes

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXIES.** Three short interviews captured as compressed notes — Janet's interview was the deep one; these add range and triangulation.

---

## Hassan (mid-senior, 7 years, runs BPO QA review meetings)
**30 min, Wednesday 2pm**

Built the side spreadsheet Priya described. Walks me through it: pulls FNOL records hourly via internal SQL access, flags anything sitting >24h without status update, color-codes by state-SLA window. Spends ~3h/week working the queue manually.

**Key takeaways**:
- The spreadsheet catches ~80% of the worst BPO drops, misses the ~20% where the BPO does send something but it's wrong
- He'd retire the spreadsheet "the day your thing actually works"
- Worried about: the prior-claim flag (his policy: any claim with a prior in 12 months gets human-touch regardless — matches Marcus's unwritten rule #3)
- Wants: read access to whatever the agent flags so he can sanity-check the patterns

Confirms: the wedge addresses his pain. Volunteered to be the operational owner post-handoff, before I asked.

**Trust criteria addition** (beyond Janet's 4): "Tell me what the agent didn't do — show me the negative space. If it auto-sent on 8 of 10 claims and held 2, I want to know why those 2 specifically."

---

## Mark (mid-career, 6 years, pro-tech adjuster)
**30 min, Wednesday 4pm**

Mark is the advocate-in-waiting Priya named. He's been pushing for more automation tooling for 18 months and frustrated by the BPO situation.

**Key takeaways**:
- Agrees the wedge is the right slice; would not start with phone
- Worried about: Janet's reaction; suggests we run his test claims first (he'll be a friendlier adopter who can model good usage in the team chat)
- Wants: a personal usage dashboard (his own claims through the agent, his own escalation rate, his own time saved)
- Volunteered to be the "first 100 claims" beta user in week 3

**Confirms**: the trust criteria Janet articulated. Adds:
- The dashboard request — the agent should also be a tool for adjuster self-improvement, not just a workforce replacement
- **Concern about "shadow metrics"**: if the agent's escalation rate becomes a manager-visible adjuster KPI, adjusters will under-escalate to look good. He wants escalation explicitly NOT a manager-facing metric.

---

## Sarah (junior, 18 months tenure)
**30 min, Thursday 9am**

Junior perspective. Her view of the workflow is shaped by training, not 14-year institutional knowledge. Useful as a calibration on what an entry-level adjuster needs vs a senior.

**Key takeaways**:
- Spends ~40% of her shift on routine acknowledgment messaging and status update copy-paste — exactly the work the wedge retires
- Would adopt a working tool day one without hesitation
- Worried about: getting blamed for the agent's mistakes ("if it auto-sends and the customer complains, do I get the QA hit?")
- Wants: clear delineation in the audit trace between "I drafted this" and "the agent drafted this"

**Confirms**: the wedge is the right cost target. Adds:
- The accountability-attribution requirement — every comm trace must clearly show whether it was agent-generated or human-edited
- Junior adjusters need the agent to explain WHY in plain English, not just WHAT (more onboarding-friendly)

---

## Cross-stakeholder triangulation

| Question | Janet | Hassan | Mark | Sarah |
|---|---|---|---|---|
| BI in v1? | NO (12mo trust period) | NO | Agree | Agree |
| Trust criteria (4 elements) | Articulated | Confirmed + adds "negative space" | Confirmed + dashboard | Confirmed + accountability attribution |
| Web/agent-portal as first wedge? | Trial it on routine | Agree | Agree | Agree |
| Concern about agent | Hallucinated comms on BI | Misses on prior-claim flag | Janet's reaction; shadow metrics | Blame attribution |

## Working hypothesis updates from this set

- **Trust-criteria UX requirement now has 6 elements** (Janet's 4 + Hassan's "negative space" + Sarah's accountability attribution)
- Mark's dashboard request becomes a v1.5 feature — adjuster-self-view of their own claims through the agent
- Mark's "no shadow metrics" warning is a deployment guideline (escalation rate visible to adjuster, NOT to their manager)
- Hassan as operational owner is now confirmed by the man himself
- Sarah's concern reinforces the audit-trace design: every output clearly attributed (agent / human-edited / human-only)

## Stakeholder map updates

| Person | Power | Stance | Operating note |
|---|---|---|---|
| Hassan | MEDIUM-HIGH (technical) | ALLY + future operational owner | Beta user; weekly platform standup; sanity-checks flagged claims |
| Mark | MEDIUM | ADVOCATE | "First 100 claims" beta user week 3; helps land Janet politically |
| Sarah | LOW (individual) | EARLY ADOPTER | Junior calibration; informs onboarding-friendliness |
