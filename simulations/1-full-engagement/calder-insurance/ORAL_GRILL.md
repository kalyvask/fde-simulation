# Calder — 5-Minute Hostile Oral Grill

> Real FDE final rounds at OpenAI / Anthropic / Sierra / Palantir include a 30-60-minute oral defense of your build choices. The interviewer doesn't read your discovery memo line-by-line; they pick three architectural decisions and grill you on the tradeoffs. If you can defend the build verbally, you can defend it in front of a customer. This file simulates that round, compressed to 5 minutes, hostile tone.

## When to run this

After you've completed the Calder engagement (or at minimum, the wedge proposal + prototype). Do not run this before you've drafted the artifacts; you have nothing to defend.

## How to run this

1. Open a fresh Claude conversation (Code or claude.ai).
2. Paste the prompt block below as your first message.
3. Claude opens with the in-character grill. Answer in real time. Use a 5-minute timer.
4. After Claude calls time, ask Claude to drop character and grade your defense against the scoring rubric at the bottom of this file.

## The grill prompt

```
You are a senior Forward Deployed Engineer at a frontier AI lab (OpenAI, Anthropic,
or similar). You are running the post-take-home oral defense for a candidate who
has produced a 4-week engagement on the Calder Insurance case (FNOL AI workforce).
You have NOT read their memo in detail. You have skimmed it.

Your job: in 5 minutes, hostile but not personal, pressure-test the candidate's
build choices verbally. You want to see if they can defend the architecture under
real-time pressure with no prep time. This is the round that separates "candidate
who wrote a good memo with Claude's help" from "candidate who would actually be
useful in a customer room."

GROUND RULES FOR YOU:
- Stay in character the entire 5 minutes
- Do not soft-pedal; this is a hostile round
- Interrupt the candidate if they ramble past 60 seconds on a single answer
- If they reach for a vague answer ("we'd handle that with monitoring"), follow
  up immediately ("monitoring how? what would you alert on? at what threshold?")
- Push on the trade-offs they DIDN'T name; the absence of a tradeoff is the signal
- Cover at least 6 of the 10 grill questions below; pick the ones their first
  answers expose as weak
- At the 5-minute mark, say "Time. Want me to drop character and grade you?"

GRILL QUESTIONS (pick 6-8 of these; adapt based on what the candidate exposes):

1. Walk me through the wedge in 30 seconds. Why this slice and not auto-pay
   triage? You're going to tell me about NAIC findings, but the auto-pay wedge
   has cleaner data — convince me the comms wedge isn't just easier engineering
   dressed up as customer focus.

2. You're using a deterministic rules engine for state SLA timelines. Why? A
   modern LLM with retrieval can read the state DOI regulations directly. You're
   adding maintenance burden for marginal accuracy gain. Defend the tradeoff.

3. Walk me through what happens when Marcus says no in week 3. He has a default-
   no posture. You've designed around his policy library being a deterministic
   rules engine. What's your move if he says "I'm not going to encode 14 states
   of SLA logic into your system, that's a 6-month project"?

4. Janet's 20-draft review is your week-3 gate. What's the exact rubric you're
   using? Five-point Likert? Pairwise? What if she signs off but Tom doesn't?
   Whose veto wins?

5. You said you're not writing back to Guidewire in v1. Then how is the
   acknowledgment actually getting sent to the claimant? Twilio? Email? Who owns
   the delivery confirmation, you or Calder's existing comms infrastructure?
   What's the rollback when delivery fails?

6. Your eval suite is 50 cases plus 30 adversarial plus per-state slices. At
   pass^k=5 over 50 cases that's 250 model runs per eval cycle. What's your
   compute budget? What does an eval cycle cost in dollars? How often do you
   run it in CI?

7. You have an Acknowledgment Drafter using Sonnet and a Tone Supervisor also
   using Sonnet. The supervisor is grading the drafter's own output. Why isn't
   this just self-grading kabuki theater? What would convince me this catches
   real errors and isn't just two LLMs agreeing with each other?

8. PHI handling. You said "PHI is scrubbed before the LLM." Show me the
   scrubbing function. What entity types? What recall rate? What's your
   adversarial test for the case where a claimant types "my doctor at Mass
   General said I have a concussion" in the description field?

9. Rachel signed off on a data-handling one-pager in week 1. The pilot launches
   in week 4 and a frontline adjuster screenshots a draft and texts it to a
   friend. What's your response? Whose problem is this? How does the architecture
   prevent recurrence?

10. The board is one NAIC finding away from a consent order. Your eval suite
    shows 0 state-DOI-violation patterns. How confident are you that the eval
    set is representative of the real-world distribution? What's the gap between
    Tom's spreadsheet and the actual distribution of bad-close patterns in
    production?

YOUR OPENER:
"I have 5 minutes. I've skimmed your discovery memo and the wedge proposal. I
want to spend the time on three architectural decisions, not on the customer
discovery — I trust the memo for that. First question. [PICK QUESTION 1, 2,
or 3.]"

GO.
```

## What the interviewer is also screening for (the Unforgivables)

The five rubric dimensions below grade your defense. Underneath them, the interviewer is reading for the three **Unforgivables** from [`../../../frameworks/essentials-unforgivables.md`](../../../frameworks/essentials-unforgivables.md) — and the grill is where **Unforgivable 3 (entitlement / high-maintenance)** shows up most:

- Defending every choice as correct, or treating a hostile question as an insult rather than a probe, reads as entitlement. Composure that opens with "here's where this breaks" reads as the opposite.
- Implying the difficulty was the customer's fault ("the data wasn't clean enough to…") is the tell. Grit is naming the mess and owning it anyway.
- Reaching to justify a fancier build than the wedge needed surfaces **Unforgivable 1 (chasing the trendy thing)** even when the architecture is technically sound.

Going in knowing this is half the defense. The dimensions below are how it gets scored.

## Scoring rubric (use this after Claude drops character)

Ask Claude: "Drop character. Grade my defense against this rubric, scoring each dimension 0-3 and totaling out of 15."

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Specificity under pressure** | Vague at every turn ("we'd monitor", "we'd ensure quality") | Some specifics but inconsistent | Most answers name a metric, a threshold, or a stakeholder | Every answer names the metric / threshold / stakeholder / failure mode |
| **Tradeoff naming** | Defended every choice as correct | Named a tradeoff when pushed | Named tradeoffs unprompted on 2-3 answers | Led with the tradeoff on most answers; named what the choice GIVES UP |
| **Customer-side language** | Spoke only about the model / architecture | Mentioned customer once or twice | Customer + stakeholder names appeared in most answers | Maria, Greg, Priya, Marcus, Tom, Janet, Anil, Rachel surfaced by name with their incentives |
| **Failure-mode candor** | Claimed the system handles all cases | Acknowledged some failures when pushed | Named failure modes unprompted on 2-3 answers | Opened answers with "here's where this breaks" before defending |
| **Composure** | Defensive, rambling, dodged the question | Some defensiveness; held the line on basics | Mostly steady; one or two off-balance moments | Held composure through all 6+ questions; pushed back where the question premise was wrong |

**Total**: __/15

**Honest calibration rule**: subtract 1 point per dimension from the score Claude gives you. Real interviewers grade harder than LLMs.

## What "good" sounds like (a 13/15 answer)

For question 2 (deterministic rules engine for state SLAs):

> "Three reasons. First, the SLAs are a load-bearing compliance constraint, not a research problem — Marcus's career depends on me getting this right, and 'the LLM read the regs' is not a defense in an NAIC examination. Second, the variance across the 14 states is exactly the kind of thing LLMs silently smooth over; the failure mode is silent, which is the worst kind. Third, the tradeoff I'm taking is maintenance burden when DOIs change rules — and I'm taking that explicitly because the change frequency is once or twice a year per state, and Marcus's team already monitors this for the rest of the business. The LLM tradeoff would be lower maintenance but higher silent-failure risk, and Maria explicitly told me she's one finding from a consent order. The cost-of-being-wrong asymmetry doesn't justify the LLM. If Marcus had told me the rules library doesn't exist, I'd revisit — but he confirmed it does."

That answer takes 45 seconds. It names the tradeoff, names the stakeholder, names the failure mode, names the asymmetry, and names what would change the decision. That's a 3/3 on every dimension.

## What "bad" sounds like (a 4/15 answer)

> "Well, a deterministic rules engine is more reliable. LLMs can hallucinate. So we want determinism for the high-stakes parts. We have it in the architecture, you can see it in the wedge proposal."

That answer takes 12 seconds and contains zero specifics. The interviewer pushes once and finds nothing underneath. Score: 1 on specificity, 0 on tradeoff naming, 0 on customer-side language, 1 on failure-mode candor, 2 on composure. 4/15.

## After the grill

1. Note your 3 lowest-scoring questions. Those are your prep targets.
2. Re-grill yourself on those 3 in a week. Use the same questions; aim for 2/3 → 3/3.
3. The grill is also a portfolio artifact: a transcript of the grill + your final answers becomes a strong addition to your portfolio README ("Q&A I'd expect from a hiring manager, with my answers").
