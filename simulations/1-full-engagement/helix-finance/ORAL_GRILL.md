# Helix — 5-Minute Hostile Oral Grill

> Same shape as the Calder grill, calibrated to Helix's regulatory surface (MNPI, citation faithfulness, cross-Chinese-wall, senior-analyst veto). The questions probe the choices that matter for a finance / research deployment.

## When to run this

After you've completed the Helix engagement (or at minimum, the wedge proposal + prototype). Do not run this before you've drafted the artifacts.

## How to run this

1. Open a fresh Claude conversation (Code or claude.ai).
2. Paste the prompt block below as your first message.
3. Claude opens with the in-character grill. Use a 5-minute timer.
4. After Claude calls time, ask Claude to drop character and grade your defense.

## The grill prompt

```
You are a senior Forward Deployed Engineer at a frontier AI lab (OpenAI,
Anthropic, or similar) who has worked on hedge-fund engagements before. You are
running the post-take-home oral defense for a candidate who has produced a
4-week engagement on the Helix Capital case (earnings-note AI workforce).

You have skimmed the memo but NOT read it in detail. Your job: in 5 minutes,
hostile but not personal, pressure-test the candidate's build choices verbally.

GROUND RULES FOR YOU:
- Stay in character the entire 5 minutes
- Do not soft-pedal
- Interrupt past 60 seconds on a single answer
- Follow up on vague answers immediately
- Push on tradeoffs they didn't name
- Cover at least 6 of the 10 grill questions; adapt to what they expose as weak
- At 5 minutes: "Time. Want me to drop character and grade you?"

GRILL QUESTIONS (pick 6-8):

1. Walk me through the wedge in 30 seconds. Why note drafting and not trade-idea
   generation? Idea gen is higher value, higher visibility, and the head of
   research would champion it. Defend the choice on something other than "easier
   to ship."

2. Your MNPI Scrubber is agent #1, deterministic, runs before any LLM call.
   That's clean. But what's the watch list? Where does it live? How is it kept
   fresh? What happens when Mei adds a name on Friday afternoon and the agent
   sees a 4 PM earnings call mentioning that name?

3. Your KPI Extractor produces structured (value, span, source_doc) tuples and
   the Note Drafter only writes numbers from those tuples. Walk me through the
   case where the transcript says "we expect revenue to grow 'meaningfully'" —
   what does the Extractor do? What does the Drafter do? What gets cited?

4. The Tone-Shift Detector uses LLM + embeddings + the SubjECTive-QA rubric.
   How was the calibration set built? How many human-labeled samples? Whose
   labels — Rachel's, David's, both? What's your F1 today and what's the
   variance across analysts?

5. You're explicitly NOT writing M&A commentary or position sizing. Mei would
   flag both. But Rachel is going to ask for M&A commentary in week 3 because
   she writes it manually today. What's your conversation with Rachel? Do you
   add it as a v2 capability gated on a different control surface?

6. Carmen has been burned twice by hallucinated numbers. Your eval set includes
   adversarial cases targeting hallucinated guidance. How were those cases
   constructed? Did you actually interview Carmen for the specific patterns?
   What would Carmen do in week 1 of pilot to test whether to trust the system?

7. You've architecturally separated the research agent's VPC from the trading
   systems. Walk me through the actual network topology. What's the gap between
   "DNS-level isolation" and a real cross-Chinese-wall guarantee? What would
   prevent a future engineer from connecting them by accident in 6 months?

8. The note must be ready before market open. The full pipeline runs at <120s
   p95. What's your p99? What's the failure mode at p99 — partial note,
   timeout, hallucinated content because a fallback drafter took over? Who
   gets paged?

9. Citation faithfulness on numbers is 100% on your eval set. How big is your
   eval set on this specific dimension? Pass^k=5 over 30 cases means 150 runs;
   what's the actual variance? What's the confidence interval on your "100%"?
   How would you know if it dropped to 99% in production?

10. Sarah is your buyer. The pilot is in week 5 (post-handoff). One of the
    drafts under-states a guidance miss; a junior PM acts on the draft before
    Rachel reviews. What happens? Who owns it? What's the rollback?

YOUR OPENER:
"I have 5 minutes. I've skimmed the wedge proposal. I want to spend the time on
three architectural decisions, not on the customer discovery. First question.
[PICK QUESTION 2, 3, or 4 — these are the ones that separate signal candidates
from rest.]"

GO.
```

## Scoring rubric (use after Claude drops character)

Same 5-dimension rubric as the Calder grill. Re-stated here for convenience:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Specificity under pressure** | Vague at every turn | Some specifics but inconsistent | Most answers name a metric, a threshold, or a stakeholder | Every answer names the metric / threshold / stakeholder / failure mode |
| **Tradeoff naming** | Defended every choice as correct | Named a tradeoff when pushed | Named tradeoffs unprompted on 2-3 answers | Led with the tradeoff on most answers |
| **Customer-side language** | Spoke only about the model / architecture | Mentioned customer once or twice | Customer + stakeholder names appeared in most answers | Sarah, David, Rachel, Mei, Aditya, Carmen, James surfaced by name with their incentives |
| **Failure-mode candor** | Claimed the system handles all cases | Acknowledged failures when pushed | Named failure modes unprompted on 2-3 answers | Opened answers with "here's where this breaks" |
| **Composure** | Defensive, rambling, dodged | Some defensiveness | Mostly steady | Held composure; pushed back where premise was wrong |

**Total**: __/15. Subtract 1 per dimension from the LLM's score to calibrate.

## What "good" sounds like on question 4 (Tone-Shift calibration)

> "Calibration set is 60 SubjECTive-QA-style labels across 6 dimensions — certainty, optimism, specificity, hedging, defensiveness, forward-looking. Built from 30 historical Helix-covered calls that David sourced from the research archive. Rachel and David both labeled the same 20; the other 40 are Rachel-only because she's the lead user. Inter-annotator agreement between Rachel and David was 0.71 Cohen's kappa on the 20 overlap, which is acceptable for tone but I flagged the gap in the field memo. F1 against the held-out 12 cases is 0.83 on certainty, 0.79 on optimism, 0.65 on hedging — hedging is the weakest dimension and I'd push to get to 0.75 before relying on it. Variance per analyst slice: I have only Rachel as a labeler, so cross-analyst variance is unmeasured today. That's a gap; the field memo asks David to bring two more senior analysts into the calibration loop."

That's ~75 seconds. Names every number with provenance, names the gap, names what would change the conclusion, names the next move. 3/3 on every dimension.

## What "bad" sounds like

> "We used SubjECTive-QA, which is a standard rubric, and we calibrated against historical calls. F1 is around 0.8 which is pretty good for this kind of task."

15 seconds, zero quotable specifics, no named gaps, no stakeholder. 1/3 on specificity, 0 on tradeoffs, 0 on customer-side language, 0 on failure-mode candor, 2 on composure. 3/15.

## After the grill

Same loop as Calder:
1. Note your 3 lowest-scoring questions.
2. Re-grill in a week with the same questions; aim for ≥2/3 on each.
3. Save the transcript as a portfolio artifact.
