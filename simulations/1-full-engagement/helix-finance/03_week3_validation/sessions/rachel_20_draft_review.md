# Rachel 20-Draft Review — Week 3 Wednesday, 60 min, in-person

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Constructed dialogue showing what the senior version of this session would look like. The 20-draft review is the political gate that determines whether the wedge ships in week 4. Per Sarah's brief at engagement kickoff: "Our senior TMT analyst — Rachel — will not roll this out unless she signs off on 20 sample drafts she'd be willing to put her name on."

## Setup

Wednesday week 3, 3:00 PM ET. Rachel's office. She's reviewed 20 sample drafts the night before — printed each on its own page with the source transcript stapled behind, marked up with a pencil. Stack of 20 sets on her desk. She's tired (Q3 earnings season just ended) but engaged.

David Park (Head of Research) was invited but is on a flight; Rachel will brief him after.

## Selected exchanges

**Alex** *(opening)*: "Rachel, I asked Aditya to give you the 20 hardest cases we have — mix of beat-and-raise, miss-and-cut, mixed signals, and three on the watch list that should have triggered the MNPI scrubber. I want you to walk me through the ones that didn't work for you. The ones that did, we can skip."

**Rachel** *(picks up the stack, fans through, finds the dividers she's made)*: "I put them in three piles. Send-ready: eleven. Close: six. No: three. Want to start with the three?"

**Alex**: "Yes. Patterns first."

**Rachel** *(pulls one)*: "This. SAMPLE_TMT Q3 2026. Strong beat, EPS $1.45 vs $1.30. Drafter caught the headline. KPI table is fine. But the tone-shift summary says 'notably more confident than prior call, markers: momentum, inflection, strong, raising guidance.' That's wrong. Prior call was the bullish one. THIS call was MORE cautious than the prior call. The drafter inverted the comparison."

**Alex**: "How can you tell from the draft? The tone supervisor pulled markers from the current transcript."

**Rachel**: "Because I know the company. The drafter doesn't have the prior-call baseline. It scored this transcript in isolation and called it 'confident.' It needs to compare against last quarter's note to actually detect a shift. Right now it's detecting tone, not tone *shift*."

**Alex** *(big note)*: "Yeah. That's a real architecture gap. The Tone Supervisor reads only the current-call transcript. It needs the prior-quarter note as input to actually do delta detection. Right now it's mis-named — it's a 'tone classifier', not a 'tone-shift detector.' I'll wire prior-quarter note into the supervisor's context by Thursday and rerun the suite."

**Rachel**: "Yes. And while you're at it — when management says 'we feel good about momentum into Q4', that's a positive statement. When management said the same thing last quarter and is now saying 'we feel good about momentum into Q4 *despite the supply environment*' — that's a tone shift, but the words are 80% identical. The supervisor needs to weight the qualifier, not the verb."

**Alex**: "Noted. Calibration data point: the SubjECTive-QA labels we used to train the judge are scored on individual calls, not pairs. We need pairwise labels for the supervisor to detect deltas vs absolute tone. I'll generate 50 pairwise calibration samples from your 18-quarter coverage history this week."

**Rachel** *(nods, pulls the next no-pile draft)*: "This one. SAMPLE_CONSUMER. Beat on revenue, miss on EPS, mixed bag. Drafter's headline says 'revenue beat, EPS miss; tone notably more confident.' Two problems. First, the tone read is wrong same as the last one — the call was actually more guarded than Q2. Second, the headline frames a mixed quarter as 'more confident.' That's a buy-side trap. PMs read the headline and skip the body. If they trade on 'more confident', they're wrong."

**Alex**: "So the headline shouldn't include tone characterization at all. Tone belongs in its own section where it's qualified."

**Rachel**: "Right. The headline is for facts. KPIs, beats/misses. Tone goes in a 'Management commentary' section, with markers cited. Never in the headline."

**Alex** *(notes)*: "Drafter prompt change: headline = factual KPIs only. Tone analysis in its own section with explicit marker citations. By Thursday."

**Rachel** *(pulls the third no)*: "This one is fine actually — I put it in no because the drafter referenced 'guidance of $3.4B to $3.5B' but the transcript said 'we're targeting the high end of our previously communicated range.' The draft fabricated the dollar range. It probably pulled from last quarter's guidance and didn't notice that this call didn't restate specific numbers."

**Alex**: "Citation chain. The number $3.4B-3.5B doesn't appear in the current-call transcript, so the citation verifier should have caught this. Either the verifier didn't fire on guidance ranges, or the drafter inherited from prior-quarter context and the verifier doesn't check inheritance. Let me look at the trace."

**Rachel**: "While you're checking — this is the single most dangerous category. A PM reading 'guidance $3.4B to $3.5B' will trade on it. If we ever cite numbers that weren't in the current call's source material, the engagement is dead. Period."

**Alex**: "Agreed. This is the kill-criteria failure mode Sarah named on day one. Two changes: (1) the verifier explicitly checks every number against current-call sources only, no inheritance from prior quarter; (2) when guidance is referenced as 'high end of range' without restatement, the drafter writes 'Management referenced prior-quarter guidance without restating specific numbers — see Q2 prepared remarks for the range' instead of inheriting the numbers. By Thursday."

*(After more case-by-case feedback, ~35 min in)*

**Alex**: "If we make these changes — tone supervisor gets prior-quarter context, headline drops tone characterization, citation verifier enforces current-call-only number grounding — would you sign off on rolling this out to your coverage in week 4?"

**Rachel** *(thinks for a long beat)*: "Make the changes. Run another 20 fresh drafts across TMT + consumer. If 18 of 20 are send-ready by my bar — meaning I'd put my name on each — yes. If 16 or 17, we keep iterating. Below 16, we step back and re-scope."

**Alex**: "Deal. I'll have the changes by EOD Thursday and 20 fresh drafts for you Friday morning. We meet again Friday 4 PM. If 18 of 20 pass, you back the rollout."

**Rachel**: "One more thing. When this rolls out, I want it to be opt-in for the first two weeks. Each analyst can choose whether to use the draft or write from scratch. I don't want a top-down mandate that turns into resentment. Adoption should be voluntary, then mandatory after we've proven it on engagement metrics."

**Alex**: "Agreed. Phase 1 is opt-in with an adoption metric we track separately from quality. Target: 70% adoption by end of week 6. Below that, we treat it as an adoption problem, not a quality problem."

**Rachel**: "Good. And David should send the all-hands, not Sarah. The analysts trust David more than they trust executive-comms."

**Alex**: "Right. I'll draft the all-hands message for David's redline; David sends it."

*(Wraps at 58 min.)*

## Post-session captures

### What changed in the design

1. **Tone Supervisor gets prior-quarter context**: now takes the prior-quarter note + current call. Detects *deltas* in tone, not absolute tone. Drives a real architecture change in workforce.py — the supervisor's `run()` signature gets a `prior_note` parameter.
2. **Headline factual only**: drafter prompt updated. Tone analysis in its own section with citation markers.
3. **Citation verifier blocks inheritance from prior quarter**: numbers must trace to current-call source material only. New deterministic check: any numeric value in the draft must appear verbatim in the current-call transcript or KPI extraction output.
4. **Guidance non-restatement handling**: when management references guidance as "the high end of range" without restating, drafter writes the explicit non-restatement phrasing instead of inheriting numbers.
5. **Pairwise calibration**: 50 pairwise samples generated from Rachel's 18-quarter coverage history this week, used to retrain the tone-shift supervisor.

### What the rollout gate became

- 20 fresh drafts across TMT + consumer, Rachel-reviewed, **≥18 send-ready** = green light for rollout
- Phase 1 (weeks 4-5): opt-in adoption, target 70% by end of week 6
- Phase 2 (week 6+): mandatory if adoption + quality metrics hold
- David (not Sarah) sends the all-hands rollout message; Alex drafts, David redlines

### Glossary updates

- **Send-ready**: a draft Rachel would attach her name to without modification
- **Tone shift vs tone classification**: shift requires prior-quarter baseline; classification is single-call
- **Number inheritance**: when drafter pulls a number from prior-quarter context into a current-quarter note. Banned.
- **Pairwise calibration**: tone-shift supervisor calibrated on pairs of consecutive-quarter notes, not on individual notes.

### Stakeholder map updates

- **Rachel**: stance moved from CONDITIONAL → ALMOST-CHAMPION. The 18/20 contract is the final gate.
- The "David sends the all-hands" detail is the strongest political signal yet; Rachel is claiming Research-team ownership of the rollout, which is the opposite of route-around.
- **Opt-in adoption phase**: a stronger gate than mandatory rollout. If voluntary adoption is low, we have a quality problem masquerading as adoption resistance.

## Recap email sent (4:15 PM)

Subject: `[Helix] Rachel review — 4 changes by Friday, 20 fresh drafts Friday morning`

> Rachel — thanks for the time and the pencil marks. Five changes I'm shipping by EOD Thursday:
>
> 1. **Tone Supervisor takes prior-quarter context**: detects deltas, not absolute tone. Pairwise calibration with 50 fresh samples from your 18-quarter history.
> 2. **Headline factual only**: KPIs + beats/misses only. Tone analysis moves to its own section with cited markers.
> 3. **Citation verifier blocks number inheritance**: every number traces to current-call source material, never prior-quarter context.
> 4. **Guidance non-restatement phrasing**: when management says "high end of range" without specific numbers, draft says so explicitly rather than inheriting.
> 5. **Opt-in adoption phase 1**: weeks 4-5 voluntary, 70% adoption target by week 6.
>
> Friday morning: 20 fresh drafts, randomized across TMT + consumer. Friday 4 PM: review session. ≥18 send-ready = rollout proceeds week 4. <18 = we iterate.
>
> When rollout proceeds, David sends the all-hands. I'll draft for his redline.
>
> Talk Friday morning.
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Customer-political acuity | 5 | "David sends the all-hands, not Sarah" was Rachel's gesture; absorbed cleanly |
| Discovery rigor | 5 | Asked her to walk through patterns, not points; got architecture-level feedback on prior-quarter context gap |
| Calibrated engineering | 4 | The tone-shift-vs-classification gap is a real architecture revision; should have anticipated in week 2 |
| Risk awareness | 5 | The number-inheritance failure mode is exactly the kill-criteria; the eval suite missed it because the seed cases don't include inheritance scenarios |
| Outcome ownership | 5 | The 18-of-20 rollout-gate contract is now a hard milestone with a date |

**Keep**: opening framing ("walk me through the ones that didn't work — patterns matter more than count"), absorbing architecture feedback without defense, the rollout-gate contract.

**Fix**: should have shipped the tone-shift-vs-classification distinction from week 2; this was a known weakness in the architecture but I deferred it. Don't defer architecture decisions that touch the kill-criteria layer.

**Lesson**: the Tone Supervisor was named correctly ("tone shift") but implemented incorrectly (tone classification). A name that describes the right behavior but the wrong implementation is worse than a name that describes the wrong behavior — it makes the gap invisible.
