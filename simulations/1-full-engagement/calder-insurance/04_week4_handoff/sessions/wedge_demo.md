# Wedge Demo — Week 4 Friday, 60 min

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Constructed dialogue showing the live wedge demo. The biggest single moment of the engagement.

## Setup

Friday week 4, 1:00 PM ET. In-person at Calder HQ in Newark, with one Zoom feed for Anil and Tom (Anil from his office, Tom dialed in from a conference). In the room: Maria (CCO), Greg (SVP), Priya (Director FNOL Ops), Marcus (Compliance), Janet (senior adjuster — present as the rollout-gate owner), Alicia (Maria's chief of staff). Alex projecting from his laptop to the room screen.

Marcus already saw the agenda + sample escalation trace this morning per their pre-demo agreement.

## The agenda Alex distributed Wednesday

> 1. The wedge in 30 seconds (1 min)
> 2. Two live cases (10 min) — one auto_send + one escalation
> 3. The audit trace artifact (10 min) — examiner-readable demo
> 4. Eval results + adversarial coverage (8 min)
> 5. Death-spiral monitor + 4-week metrics so far (5 min)
> 6. Rollout structure + Hassan as operational owner (10 min)
> 7. Janet's sign-off + decision request (10 min)
> 8. Q&A (6 min)

## Selected exchanges

**Alex** *(opening, slide 1, the wedge in 30 seconds)*: "Auto-acknowledgment plus first-status-update for first-party physical damage FNOL claims, web and agent-portal channels first. Drafts only — no writes back to Guidewire. 80% straight-through, 20% to adjuster review. Both Q4 market-conduct findings sat at the comms layer; this wedge directly addresses that pattern. Live demo in 60 seconds — let me show you."

*(He runs the scaffold against a synthetic FNOL routed to web channel. ~12s end to end. Output is a draft + auto_send decision + audit trace.)*

**Greg**: "12 seconds. What was 4 hours."

**Alex**: "Right. Now the escalation case. Same shape, but with the elderly-party flag set."

*(Runs a second case — claim with elderly party. 14 seconds end-to-end. Decision: adjuster_review. Reason: rule_1_child_or_elderly_party fired. Draft is the escalation comm: 'A claims specialist will reach you within 4 hours.')*

**Marcus** *(speaks first)*: "Two things to call out. The escalation comm has a 4-hour timeline because this was NJ. The trace banner says 'escalation route' — distinct from the standard route. Both were design choices we made together in week 3."

**Alicia** *(blunt, on cue)*: "What happens if it routes to a person and the person doesn't pick it up?"

**Alex**: "Adjuster review queue has a 30-min SLA before re-escalation. If Janet's team doesn't pick it up in 30 minutes, it pages a supervisor. We didn't simulate that today; want me to walk through the queue dashboard?"

**Alicia**: "Yes."

*(Alex shows the queue dashboard — separate Streamlit-style screen, mocked but functional.)*

**Alicia**: "How would I know if the system is silently sending bad comms over time?"

**Alex** *(advances to slide 5, death-spiral)*: "This is the monitor. Three rolling 7-day metrics: pass rate, p95 latency, escalation rate. Alerts fire if any drift more than 10%. I ran a 14-day simulation against this last week — it caught all three drift patterns. Here's the demo."

*(Runs run_monitor.py output projected. Three alerts fire on the simulated drift.)*

**Tom** *(on Zoom)*: "That covers two of my three sign-off criteria. The third is the audit trace. Can we look at one in the format an examiner would see?"

**Alex** *(opens the rendered HTML trace from the escalation case)*: "This is the artifact. Inputs the agent saw at every step, rule applied, model version, confidence, escalation threshold, human-readable summary at the top. Drilldown on each step. Self-contained HTML — email-attachable, print-friendly."

**Tom**: "That's right. I want to be able to forward that to a state DOI in a bcc situation. It works."

*(Eval results section.)*

**Alex**: "Eval suite. Sienna's 50 cases plus 30 adversarial plus state slices — 80 cases total. 96% weighted pass rate on the real Claude path with k=5 consistency. Three cases failed; all three are documented and tracked in the regression backlog. Two are state edges in CT and RI we're putting in v2; one is a known prompt fragility in long narratives we have a fix for next week."

**Maria**: "What's the ratio in production traffic of the v2-deferred cases?"

**Alex**: "Less than 0.4% of the v1 channel slice. Maria, this is the 'narrow over late' you flagged — these are out of v1 explicitly."

**Maria**: "Good."

**Janet** *(when invited)*: "I reviewed 20 fresh drafts on Tuesday. 19 were send-ready. The one that wasn't was a multi-vehicle pile-up where the agent over-summarized and lost the second car's role. We agreed that's an over-narrow incident_description case, fixable. I'm signing off on rolling out to my team starting Monday. I'll send the all-hands tonight."

**Maria** *(directly to the room)*: "OK. We're going. Greg — coordinate with Janet on the all-hands timing. Marcus — I want one biweekly with you to me directly, separate from the team's, for the first 90 days. Anil — Hassan in the platform standup starting next week. Tom — Sienna's review weekly through end of Q4. Alex — let's discuss the 90-days-after structure separately Monday."

**Alex**: "Done."

**Alicia**: "What's your single biggest worry right now?"

**Alex** *(without hesitation)*: "Janet's review held up the rollout gate, but my real worry is that the BPO political reaction (Kevin) is quiet because he hasn't seen this run. Once the rollout starts cutting his volume, he may try to route claims away. The mitigation: we positioned this as augmenting BPO for week 1, but the reality is we're going to take 25% of their volume by week 8. That conversation has to happen with Kevin, with you in the room, before the rollout gets visible in the BPO QA reports."

**Maria**: "I'll set it up. Next week."

*(Wraps at 56 min — 4 min under, which Maria notices approvingly.)*

## Post-session captures

### Decisions made in the room

1. **Rollout proceeds** starting Monday week 5
2. **Janet sends the all-hands** tonight
3. **Marcus biweekly direct to Maria** for the first 90 days
4. **Hassan in Anil's platform standup** starting next week
5. **Sienna weekly review** through end of Q4
6. **Kevin (BPO) conversation** to happen next week with Maria in the room
7. **90-days-after structure** discussion Monday with Maria

### What worked in the demo

- The two live cases at the front (auto_send + escalation) — concrete in 60 seconds
- Marcus speaking first on the escalation case — signal that compliance is on board
- Alicia's blunt questions answered directly with concrete artifacts (queue dashboard, monitor demo)
- Janet's specific number (19/20) cited verbatim
- The "narrow over late" frame Maria gave week 3 reflected back as the v2-deferred ratio

### What didn't work / what's exposed

- Should have anticipated Alicia's "what if no one picks it up" — the 30-min SLA was real but not in the demo deck
- The Kevin/BPO political risk surfaced for the first time in the demo, not earlier — should have been in the wedge proposal week 2

## Recap email sent (2:30 PM)

Subject: `[Calder] Wedge demo recap — rollout proceeds Monday + 6 follow-ups`

> Maria, Greg, Priya, Marcus, Anil, Tom, Janet, Alicia —
>
> Demo notes. Rollout proceeds Monday. 6 follow-ups in the next 7 days:
>
> 1. **Janet** — all-hands tonight
> 2. **Marcus + Maria** — biweekly direct, first 90 days
> 3. **Hassan in Anil's platform standup** — starting Monday
> 4. **Sienna weekly review** — through end of Q4
> 5. **Kevin / BPO conversation** with Maria in the room — Tuesday or Wednesday
> 6. **90-days-after structure** — Maria + Alex Monday
>
> Field memo to Anthropic Research/Product going out tomorrow; will share.
>
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Outcome ownership | 5 | Closed on rollout decision in 56 min; 4 min under time |
| Customer-political acuity | 5 | Marcus speaking first on escalation, Alicia probing answered with artifacts, Kevin risk surfaced before BPO QA reports |
| Productionization discipline | 5 | Audit trace + monitor demo + queue dashboard + eval all green |
| Calibrated engineering | 5 | Live cases at the front, not slides; demo as a proof, not a pitch |
| Eval-driven discipline | 5 | 96% on 80 cases with documented failures + backlog |
| Codification | 4 | The 6 follow-ups are clean; should have asked Alicia about her usual stakeholder pattern earlier |

**Keep**: opening with two live cases in 60 seconds; letting Marcus narrate the escalation; Janet's specific number; "narrow over late" frame.

**Fix**: anticipate Alicia next time — the chief-of-staff is a known pattern, should have asked about her at kickoff; Kevin/BPO political risk surfaced too late and only because Alicia asked the right question.
