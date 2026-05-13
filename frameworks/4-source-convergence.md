# Framework 1: 4-Source Convergence

> Triangulate four sources to find the real wedge in a new customer engagement. Don't trust any single source.

## The four sources

| Source | What it tells you | Failure mode if you rely only on this |
|---|---|---|
| **Buyer** (CIO / VP / Director) | What they *think* the problem is | Buyers describe the problem from one altitude up; they often miss the actual failure mode |
| **Brief** (RFP / written prompt) | What they *wrote down* to formalize it | Briefs are sanitized; they leave out the political map and the real timeline |
| **Industry** (benchmarks / peers) | What's *actually possible* with the technology | Industry benchmarks generalize; your customer's data quality and integration constraints may not match |
| **Operator** (lead user / daily practitioner) | What's *actually broken* | Operators are close to the work but may not see the strategic frame |

## How to deploy it

1. List the four sources for the case
2. For each, write 1-2 sentences on what they tell you about the problem
3. Look for **convergence**: do all 4 sources point at the same workflow stage?
4. If yes, that's the wedge
5. If they diverge:
   - Operator usually has the truth about *where* it's broken
   - Buyer usually has the budget for *what* to fix
   - You'll need both

## Worked example (Helix Capital)

- **Buyer (Sarah, CIO)**: "Senior analysts are burning out on the morning-after grind. We lost two in 2025."
- **Brief**: "Build something that compresses the 4-hour earnings-note drafting time to 30 minutes."
- **Industry**: Morgan Stanley, BlackRock, and peers have built citation-grounded LLM drafters with HITL approval. Anthropic's Claude is BAA-cleared. the company's deployment patterns apply.
- **Operator (Rachel, senior analyst)**: "Most of my 4 hours is actually verification and formatting. The analysis itself is maybe 45 minutes. If you compress verification, you save 2+ hours."

**Convergence**: all four point at the verification + formatting layer, not the analysis layer. The wedge is citation-grounded drafting + verification, not "automate the analysis."

## The probe this defends against

When the interviewer asks "how did you decide what to build first", you say:

> "I triangulated four sources. Buyer said X, brief said Y, industry pattern said Z, operator said W. They converged on [specific workflow stage]. That's why the wedge is [narrow scope]."

This beats "I'd talk to stakeholders" by 10x in interview signal.

## When sources diverge

If sources diverge, the rule is:

- **Operator > Buyer on "what's broken"** — operators see the daily failure modes
- **Buyer > Operator on "what's worth fixing"** — buyers control budget and strategic priority
- **Brief sets the formal scope** — don't violate it without surfacing the violation
- **Industry tells you what's feasible** — if industry hasn't done it, you probably can't either in v1

The senior FDE move when sources diverge: document the divergence in the field memo. Don't argue with the buyer in week 1; bring the data to week 2.

## Quick reference

```
DISCOVERY (week 1):
  Source 1 — Buyer: ____________________
  Source 2 — Brief: ____________________
  Source 3 — Industry: __________________
  Source 4 — Operator: __________________

  Do all 4 converge on the same workflow stage? Y/N
  If yes → that's the wedge
  If no → operator has truth, buyer has budget; you need both
```
