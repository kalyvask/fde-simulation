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
