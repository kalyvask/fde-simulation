# Marcus Biweekly — Week 3 Wednesday, 30 min

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Constructed dialogue. Devorah has been on weekly cadence with Alex; this is the first Marcus check-in since the kickoff.

## Setup

Wednesday week 3, 4:00 PM ET. Marcus's office. Same posture as week 1 but visibly more relaxed — the cell-number gesture from the kickoff held. Devorah is on the line via Zoom. Marcus has the policy-library encoding doc open on his laptop.

## Selected exchanges

**Alex** *(opening)*: "Marcus, two things I want to walk through. The policy library encoding — Devorah and I have been through it twice; I want your sign-off on a couple of state nuances. And one architecture change Janet flagged this morning that has compliance implications."

**Marcus**: "Architecture change first. What is it?"

**Alex**: "Currently the drafter generates an ack; then the compliance critic decides routing. Janet flagged that for escalations, the drafter shouldn't generate the standard ack — should output an 'escalating to a person' comm or no comm at all. I'm shipping that change by Friday. Wanted to make sure that doesn't create a compliance gap from your seat."

**Marcus** *(thinks)*: "It's the right change. Two things. First, the escalation comm needs a timeline — even if it's 'within 4 business hours' rather than '10 days'. Claimants need a number. Second, the audit trace needs to show clearly that this was an escalation path, not a standard path. So the trace renderer needs an 'escalation route' marker."

**Alex** *(notes)*: "Both doable. Trace marker is a 1-line change to the examiner renderer. Timeline-on-escalation: I'll add a state-aware deterministic timeline for the escalation comm — probably 4 hours for NJ/NY/PA, 8 hours for the rest. Sound right?"

**Marcus**: "4 hours for NJ/PA/NY/MA. 8 hours for the rest. NY is the one to watch — they treat 'escalation without timeline' as a procedural failure even if the substantive handling is fine."

**Alex**: "Got it. Updating the StatePolicy struct to include an escalation_timeline_hours field. I'll send Devorah the diff this evening."

**Marcus**: "OK. State nuances — what did you find?"

**Alex**: "Two. First, the unwritten rule on first-time customers — warmer tone — Devorah and I encoded it as a tone flag, not an escalation. That's how you described it. But on review, MA's documentation-strict standard means we need to evidence the warmer tone in the trace, not just produce it. So the tone flag is now logged with reasoning. Second, the prior-claim rule — we currently look back 12 months from the new claim's incident_date. But your written policy says 'prior claim closed in past 12 months' — meaning it should be closed-date, not incident-date. We've been using the wrong field."

**Marcus** *(slight smile)*: "Good catch. Closed-date is right. The reason it matters: a claim opened 14 months ago and closed last week is still 'recent' to us; a claim opened 11 months ago that's still open is a different situation entirely."

**Alex**: "Updating. Devorah will write the change-rationale into the policy-library doc tonight so the source of truth tracks the code change."

**Marcus**: "Send me the diff before you ship. I want to see the rule change in code form, not in description."

**Alex**: "Will do. EOD Thursday at the latest."

**Marcus**: "Last thing from me. The wedge demo Friday week 4 — am I on the invite?"

**Alex**: "Yes. Maria, Greg, Priya, Tom, Anil, you. 60 min. I want you in the room when we walk through the trace artifact for an escalation case. If you'd want to flag anything before that, this is the time."

**Marcus**: "Send me the demo agenda Friday morning. If I see anything that would surprise me, I'll send back redlines before the meeting. I'd rather not surface a concern in front of Maria."

**Alex**: "Done. Friday morning, demo agenda + a sample escalation trace. Thanks for the cell number — Devorah and I have used it twice."

**Marcus**: "I noticed. Both times reasonable. Keep using it when needed."

*(Wraps at 28 min.)*

## Post-session captures

### What changed in the design

1. **Escalation comm needs a timeline** (4h NJ/PA/NY/MA, 8h other). Adds `escalation_timeline_hours` to StatePolicy.
2. **Audit-trace renderer needs an "escalation route" marker** so examiners can distinguish escalation paths from standard ones at a glance.
3. **Tone flag must be evidenced in trace** (MA documentation-strict requirement).
4. **Prior-claim window uses closed-date, not incident-date** — bug fix to rule_3.

### Pre-demo dependency

- Marcus wants the demo agenda + a sample escalation trace by Friday morning week 4
- Marcus will redline before the meeting if anything would surprise him
- Marcus does not want to surface a concern in front of Maria — strong political-trust signal

### Stakeholder map updates

- Marcus: stance held at DESIGN-PARTNER, with a clear pre-demo synchronization commitment
- Devorah: working pattern is now well-established (weekly + cell number for urgent)
- The "do not surprise Maria" signal is the trust-extension that comes from the cell-number gesture two weeks ago

## Recap email sent (4:35 PM)

Subject: `[Calder] Marcus biweekly W3 — 4 design changes + demo prep`

> Marcus — recap. Four changes by EOD Thursday:
>
> 1. **Escalation comm timeline** — 4h NJ/PA/NY/MA, 8h other states. Added to StatePolicy as escalation_timeline_hours.
> 2. **Trace renderer "escalation route" marker** so examiners distinguish path types.
> 3. **Tone flag evidenced in trace** (MA documentation requirement).
> 4. **Prior-claim window uses closed-date, not incident-date** — bug fix.
>
> Friday morning week 4: I'll send the demo agenda + a sample escalation trace before the meeting. If any of it would surprise you, redline back.
>
> Devorah weekly continues. Cell-number policy unchanged.
>
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Customer-political acuity | 5 | The "do not surprise Maria" signal is gold — surfaced because of trust earned in week 1 |
| Domain learning velocity | 5 | Caught the closed-date vs incident-date nuance; this is what speaking the domain natively looks like |
| Productionization discipline | 4 | Should have caught the closed-date bug in week 2 unit tests; the fix is good but late |
| Codification | 5 | Devorah will document the rule-change rationale in the policy library — matches Marcus's "design partner not approval table" frame |
| Outcome ownership | 5 | Pre-demo synchronization commit is the right move; surfaces issues 24h before they could be public |

**Keep**: opening with the architecture change first (the substantive one) before the policy nuances; not surprising Marcus.

**Fix**: closed-date vs incident-date is the kind of bug that should be caught in code review week 2. Need a rule-by-rule spec doc that Devorah signs off on so semantic mistakes can't ship.
