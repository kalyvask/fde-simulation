# Janet 20-Draft Review — Week 3 Tuesday, 45 min, in-person

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Constructed dialogue showing what the senior version of this session would look like. The 20-draft review is the political gate that determines whether the wedge ships in week 4.

## Setup

Tuesday week 3, 2:00 PM ET. Janet's desk. She's reviewed 20 sample drafts the night before — printed them out, marked them up with a red pen. Stack of papers visible, several with extensive margin notes. Priya is sitting in. Coffee. No screens.

## Selected exchanges

**Alex** *(opening)*: "Janet, thanks for taking the time. I asked Priya to give you the 20 hardest cases we have — mix of routine, prior-claim escalations, and a couple where the system held a draft for review. I want you to walk me through the ones that didn't work for you. The ones that did, we can skip."

**Janet** *(picks up the stack)*: "Six of these I'd be willing to send. Eight are close. Six need work. Want to start with the worst?"

**Alex**: "Yes. The patterns matter more than the count."

**Janet** *(pulls one)*: "This one. NJ web claim, Mr. Hassan. Says 'I didn't have time to react and I rear-ended them.' The draft says: 'Hi Mr. Hassan, I've received your claim regarding the rear-end collision on the GSP. We'll have an estimate appointment scheduled within 10 days. Sarah Cole is your contact at 555-0100.' That's a B-minus comm. It hits the 5 elements technically. But Janet wouldn't write it that way."

**Alex**: "Why?"

**Janet**: "He told us he didn't have time to react. That's an emotional confession — he's worried about his fault. A senior adjuster acknowledges that. Something like 'sounds like that came up fast on you' or 'these things happen at highway speeds in a blink.' Just one phrase that says we read what he wrote, not just summarized it. The bot summarized. It didn't read."

**Alex** *(notes)*: "Got it. The 5-element bar is necessary but not sufficient. There's a sixth implicit element — empathy that reflects the claimant's emotional content. Is that consistent across the 6 you're calling 'need work'?"

**Janet** *(leafs through)*: "Five of the six, yes. One is different — this one, the elderly party case. Drafter shouldn't have generated anything at all here; it should have routed to a human and said 'we're routing this to a person who'll call you within the hour.' Instead it generated a comm that mentions the elderly mother. That's worse than no comm — implies we're handling it, when we're actually escalating. The escalation path needs its own comm."

**Alex**: "So escalation cases need a separate comm template that says 'we're routing you to a person', not the standard ack. Let me play that back. The current architecture generates an ack first, then the compliance critic decides routing. The order should be reversed for escalations: when policy says escalate, drafter writes a different comm."

**Janet**: "Yes. Or skip the comm entirely and let the human adjuster send their own. Either is fine. What's not fine is sending a 'normal' ack on a claim we're flagging."

**Alex** *(big note)*: "OK, that's a real architecture change. Sub-issue: when the workforce decides to escalate, it currently runs the drafter first then critic. We need to swap the order or add a separate escalation-comm path. I'll get that fixed by Friday."

**Janet**: "Two more patterns. The first-time customer one — 'Welcome to Calder' opening. Sounds salesy. We're not selling them anything; they bought already. Drop 'welcome'. Just be warmer in the body. Second: the diacritic one — 'Ms. García' became 'Ms. Garcia' in one of the drafts. We do not Anglicize names. Ever. That's a culture-thing."

**Alex**: "Both fixable. The diacritic one is a deterministic check — name passes through unchanged. The 'welcome' phrasing is a prompt change. By Friday."

*(After more case-by-case feedback, ~30 min in)*

**Alex**: "If we make the changes we've discussed — escalation-aware drafter, drop 'welcome', preserve diacritics, add an empathy element to the prompt — would you sign off on rolling this out to your team in week 4?"

**Janet** *(thinks)*: "If you make those changes and we run another 20 drafts and at least 18 are send-ready, yes. If not, we keep iterating."

**Alex**: "Deal. I'll have the changes by EOD Thursday and 20 fresh drafts for you Friday morning. We meet again Friday afternoon. If 18 of 20 pass your bar, you back the rollout."

**Janet**: "OK. And one more thing — when we roll out to my team, I want to be the one who tells them about it, not Priya. They listen to me different."

**Alex**: "That's right. I'll draft the all-hands message; you redline it; you send it."

*(Wraps at 42 min.)*

## Post-session captures

### What changed in the design

1. **Escalation-aware drafter**: when policy library indicates escalation, the drafter generates a *different* comm (or no comm), not the standard ack. Architecture change in workforce.py.
2. **Empathy element**: add to the ToneSupervisor's bar (now 6 elements, not 5). LLM-as-judge prompt updated.
3. **Drop "Welcome to Calder"**: prompt change in DrafterAgent.
4. **Diacritic preservation**: explicit deterministic check that claimant_name passes through byte-identical.

### What the rollout gate became

- 20 fresh drafts, Janet-reviewed, ≥18 send-ready = green light for adjuster rollout
- Janet (not Priya) sends the all-hands rollout message
- Janet's red-pen reviewers becomes the regression-test source for week 4

### Glossary updates

- **B-minus comm**: technically correct but misses what made the claim distinctive. Janet's term.
- **Empathy element**: the implicit sixth element of comm-quality.
- **Escalation comm**: separate template for cases where the policy library routes to a human.

### Stakeholder map updates

- Janet: stance moved from CONDITIONAL SUPPORT → ALMOST-CHAMPION. The 18/20 contract is the final gate.
- The "Janet sends the all-hands" detail is the strongest political signal yet; she's claiming ownership of the rollout, which is the opposite of route-around.

## Recap email sent (3:00 PM)

Subject: `[Calder] Janet review — 4 changes by Friday, 20 fresh drafts Friday morning`

> Janet — thanks for the time and the red pen. Four changes I'm shipping by EOD Thursday:
>
> 1. **Escalation-aware drafter**: when policy library escalates, drafter outputs a "we're routing you to a person" comm or no comm. Standard ack only on auto-send paths.
> 2. **Empathy element**: ToneSupervisor's bar now 6 elements. New element: drafted comm reflects emotional content of the claimant's narrative, not just facts.
> 3. **Drop "Welcome to Calder"**: prompt change.
> 4. **Diacritic preservation**: deterministic check on claimant_name byte-identity.
>
> Friday morning: 20 fresh drafts, randomized mix. Friday afternoon: review session. ≥18 send-ready = rollout proceeds week 4. <18 = we iterate.
>
> When rollout proceeds, you send the all-hands. I'll draft it for your redline.
>
> Talk Friday morning.
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Customer-political acuity | 5 | "You send the all-hands, not Priya" was Janet's gesture; absorbed cleanly |
| Discovery rigor | 5 | Asked her to walk through patterns, not points; got architecture-level feedback |
| Calibrated engineering | 4 | The escalation-aware drafter change is a real architecture revision; should have anticipated |
| Risk awareness | 5 | The "routing comm" gap is the kind of thing that would have triggered a regulatory finding in week 6 |
| Outcome ownership | 5 | The 18-of-20 rollout-gate contract is now a hard milestone with a date |

**Keep**: opening framing ("walk me through the ones that didn't work — patterns matter more than count"), absorbing the architecture feedback without defensiveness, the rollout-gate contract.

**Fix**: should have shipped the escalation-aware drafter from week 2; this was a known weakness in the architecture but I deferred it. Don't defer architecture decisions that touch the comms layer.
