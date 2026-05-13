# Framework 6: 4-Dimensional Testing

> When asked "how would you test this", name 4 dimensions, not 1. Static eval + Pass^k + Adversarial + Production observability. The fourth dimension is what separates production thinking from demo thinking.

## The 4 dimensions

| Dimension | What it tests | Detection signal |
|---|---|---|
| **1. Static eval suite** | Known-input → known-output correctness | Weighted by failure cost; 50+ cases minimum |
| **2. Pass^k** | Stability across runs (k=5 is the production threshold) | Variance ≤5% across runs |
| **3. Adversarial set** | Known failure modes that should be caught | One case per major risk surfaced |
| **4. Production observability** | What you don't know yet | Rolling drift detection + alerts + audit trace |

## Why pass^k=5 specifically

LLM outputs are not deterministic. A single pass (pass@1) can succeed by luck or fail by luck. Pass^k=5 means: run the same case 5 times, count it as "passing" only if it passes in all 5 (or the threshold you define).

Why 5: enough to surface flakiness, few enough to be tractable on a 50+ case suite. Variance tolerance ≤5% — if pass rate varies more than 5% across runs, the agent isn't ready for production.

Pass@1 hides flakiness. Pass^k=5 exposes it.

## Static eval composition

A good static eval suite for v1:

| Slice | % of cases | Purpose |
|---|---|---|
| Happy path | 40% | Validate core functionality |
| Edge cases | 30% | Validate boundary behavior |
| Adversarial | 20% | Validate failure-mode handling |
| Regression | 10% | Catch known issues that resurfaced |

Weight cases by failure cost. A regulatory leak case is weighted 10x a tone-misread case. The weighting forces the eval to surface the failures that actually matter.

## Adversarial set construction

For each risk surfaced in the risk register, build one adversarial case:

- MNPI leak risk → adversarial: ticker just added to watch list mid-quarter
- Hallucinated number risk → adversarial: transcript with similar-but-different numbers
- Position-sizing slip risk → adversarial: customer commentary that implies a sizing recommendation
- Tone misread risk → adversarial: bullish management framing of cautious guidance

The adversarial set is the ground truth for whether your guardrails actually work.

## Production observability

The fourth dimension is what most candidates skip. It's the difference between "we built it and it works on the eval" and "we built it and we'll know if it stops working."

Three things to name:

1. **Rolling drift detection**: 7-day window on a specific signal (e.g., intent classification accuracy). Alert if drift > 5%.
2. **Per-request audit trace**: immutable log of every agent's input + output + latency + cost. Examiner-readable.
3. **Weekly operational review**: cadence with the operational owner (named pre-handoff). Review 20 sample outputs + escalation rate + cost trend.

## How to deploy it

When the interviewer asks "how would you test this":

> "I'd test on 4 dimensions. First, a static eval suite of 50+ cases weighted by failure cost — regulatory blocks weighted 10x. Second, pass^k=5 as the production threshold with variance ≤5%. Third, an adversarial set with one case per major risk — for this customer that's [list specific adversarial cases]. Fourth, production observability — 7-day rolling drift detection, immutable audit trace per request, weekly review with the operational owner."

That's ~30 seconds. Covers all 4 dimensions. Lands the senior FDE signal.

## Worked example (Helix Capital)

| Dimension | Helix specifics |
|---|---|
| Static eval | 50 cases (10 per major risk) weighted by failure cost (MNPI leak 10x, hallucinated number 5x, tone misread 2x) |
| Pass^k=5 | Variance ≤5% on production threshold; re-run on every release |
| Adversarial set | MNPI smuggling, position-sizing slip, ambiguous-tone management commentary, multi-issue earnings calls |
| Production observability | 7-day rolling drift on KPI extraction accuracy; per-call analyst-trust metric; weekly review with Rachel |

## Quick reference

```
TESTING FRAMEWORK (4 dimensions):

  1. STATIC EVAL
     50+ cases, weighted by failure cost
     Composition: happy / edge / adversarial / regression

  2. PASS^K
     k=5 (variance tolerance ≤5%)
     Re-run on every release

  3. ADVERSARIAL SET
     1 case per major risk
     Customer-specific kill-criteria represented

  4. PRODUCTION OBSERVABILITY
     7-day rolling drift detection
     Immutable audit trace per request
     Weekly review with named operational owner
```
