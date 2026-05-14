# Framework 2: 3-Lens Scaffold

> Customer / Product / Technical. Fill these three columns before designing any technology. The single most useful framework for solution-strategy conversations.

## The three columns

```
| CUSTOMER (the user) | PRODUCT (the agent) | TECHNICAL (the build) |
|--------------------|---------------------|----------------------|
| Who (specific)     | Intent (top 3)      | Read access          |
| Emotional state    | In scope (3-5)      | Write access (NONE   |
| JTBD top 3 intents | Out of scope        |   in v1)             |
| Why failing today  |   (equally explicit)| Data freshness       |
| What's hard        | Trust (act/ask/     | ONE specific risk    |
|   (root cause)     |   escalate)         | Validation plan      |
|                    | Fallback            |                      |
|                    | Metric + tension    |                      |
```

## Why this order matters

Customer first, technical last. The reason: the technology is downstream of what the user actually needs. Most candidates start with technology ("I'd use RAG") and have to walk back when the interviewer asks "what does the user actually want."

The 3-lens scaffold forces you to:
1. Name the user and their emotional state (drives every design decision)
2. Name what the product does AND doesn't do
3. Only then think about the build

## Customer column — segmentation pattern for AI products

The Customer column says "specific persona, not 'users'." For AI products specifically, the segmentation heuristic that separates strong from weak candidates is **how users relate to the AI capability**, not their demographics.

| Demographic segmentation (weak for AI products) | AI-capability segmentation (strong) |
|---|---|
| Junior dev vs senior dev | Power user (pushes the tool's limits) vs aspiring builder (can't yet) vs knowledge automator (just wants the friction gone) |
| Big-co vs small-co customer | Customer that integrates LLM into core workflow vs customer that uses LLM as adjunct vs customer that uses LLM only when blocked |
| US vs international users | Customer with high-trust relationship to AI output vs customer with low-trust relationship (reads with skepticism) |
| Casual vs daily user | Customer who reviews every AI output before publishing vs customer who reviews on a sample basis vs customer who trusts and ships |

The AI-capability segmentation is stronger because it directly determines:
- **Which product surface they use** (CLI vs web vs API vs embedded)
- **What friction they hit** (rate limits vs cost vs intimidation vs blank-slate)
- **What growth lever matters for them** (activation vs retention vs trust-building)

If your segmentation could apply equally to a non-AI product, you've done it wrong. The senior move is: name the AI-capability relationship before the demographic.

### Worked example: Calder FNOL adjusters

Bad segmentation: "junior adjusters vs senior adjusters."

Good AI-capability segmentation:
- **The auto-trust adjuster** (3-5% of the team): reads the AI draft, sends it without modification, ships >20 claims/day. Risk: silent acceptance of subtly wrong drafts.
- **The verify-every-line adjuster** (~50%): reads the AI draft, line-by-line verification, often re-writes ~30%. The actual-quality-gate group. Engagement metric depends on whether they trend toward shipping more or rewriting more.
- **The route-around adjuster** (~10-15%): doesn't use the AI draft, starts from scratch. The engagement-failure group. Their behavior is the silent killer.

Each segment has different risk, different metric, different product surface need. Demographics ("senior vs junior") didn't tell us any of this.

### Worked example: Helix earnings-note analysts

Bad: "TMT analysts vs consumer analysts."

Good:
- **The voice-keeper analyst** (Rachel): expects the draft to match her style; if it doesn't, re-drafts. Her engagement is driven by voice match, not by KPI accuracy.
- **The verification-time analyst**: ships the draft if every number traces in <10 seconds; re-drafts if she can't verify fast. Citation panel UX is her primary gate.
- **The tone-shift-listener analyst**: validates the agent's tone-shift call against her own read of the call; if the agent over-flags or under-flags, she stops trusting it. Calibration is her gate.

Same three analysts (junior / mid / senior by demographics) might fall into any of these AI-capability segments. The segmentation determines which product feature investment matters per segment.

## The 5 rules within the scaffold

| Rule | Why |
|---|---|
| **Always name the emotional state** | Stressed customer ≠ curious customer ≠ anxious customer. Drives design. |
| **Define out-of-scope as explicitly as in-scope** | Shows judgment, not laziness |
| **Name the metric tension** | Containment vs CSAT. Speed vs accuracy. Pick which you protect in v1. |
| **Distinguish read vs write** | Write almost always NONE in v1. Read-only v1 is the senior move. |
| **One specific risk, not generic list** | "Policy-version pinning" beats "we'd use guardrails." |

## How to deploy it

In a 60-min interview: walk through the 3 columns out loud, ~90 seconds per column, after you've restated the case.

In a 5-hour take-home: fill the table in Hour 1; reference it on Slide 1 of the deck.

In a full engagement: fill the table in week 1; revisit it weekly as new information surfaces.

## Worked example (Helix Capital)

### Customer column
- Who: Rachel — senior TMT analyst, 9 years tenure, lead user
- Emotional state: Exhausted + anxious about hallucinated number reaching a PM
- JTBD: (1) Ship defensible earnings note in <30 min, (2) Capture tone shifts accurately, (3) Maintain zero-MNPI streak
- Why failing today: 4 hours × 80 names × 4 quarters = 1280 hours/yr; two seniors quit citing grind
- What's hard: Analyst can't tell "AI summary" from "AI-assisted draft I can defend" — picks speed or rigor, both lose

### Product column
- Intent: Citation-grounded earnings draft + tone-shift detection
- In scope: KPI extraction, citation grounding, tone flags, audit trace
- Out of scope: M&A commentary, position-sizing, auto-publish, multi-quarter (all 4 explicit)
- Trust: Act on deterministic (MNPI, citation); ask on soft (tone); escalate on policy combinations
- Fallback: Draft to Rachel's queue with reasoning; never auto-send
- Metric + tension: 30-min review per note. TENSION: Speed vs zero-MNPI streak. Protect the streak.

### Technical column
- Read: FactSet transcripts, Bloomberg consensus, prior-quarter notes, MNPI watch list
- Write: NONE in v1 (holding queue only)
- Data freshness: Transcripts live; consensus live; MNPI list pulled per invocation (not cached)
- ONE specific risk: MNPI watch-list drift; mitigation = per-invocation pull + Mei-owned audit log
- Validation: PoC + 50-case weighted eval + Mei + Rachel + Carmen sign-offs

## The probe this defends against

When the interviewer asks "design the AI workforce", you don't draw agents. You walk through the 3-lens scaffold first. **The framework is the answer.**

## Quick reference

```
SOLUTION STRATEGY (in the interview, 4-5 min on this alone):

  CUSTOMER (90 sec):
    Who, emotional state, JTBD top 3, why failing today, what's hard

  PRODUCT (90 sec):
    Intent, in scope, out of scope (equally explicit),
    trust levels (act / ask / escalate), fallback, metric + tension

  TECHNICAL (60 sec, keep light):
    Read access, write access (NONE v1), data freshness,
    ONE specific risk, validation plan

  ALWAYS:
    Name emotional state
    Out-of-scope as explicit as in-scope
    Metric tension named
    Read vs write distinguished
    One specific risk, not a generic list
```
