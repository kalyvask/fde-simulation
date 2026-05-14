# Framework 3: Outcome Risk Matrix

> Score candidate wedges on Value × Risk-of-irreversible-failure. The 2x2 picks the wedge.

## The 2x2

| | Low-risk failure (reversible, caught early) | High-risk failure (irreversible, caught late) |
|---|---|---|
| **High value (saves >2h / workflow)** | **Ship as v1** | Ship with hard guardrails + senior veto |
| **Low value (saves <30min / workflow)** | De-prioritize | Avoid entirely |

## The principle behind it

**Confidence of outcome over size of outcome.** The biggest wedge is rarely the right wedge. The right wedge is the one you can ship with the highest confidence of clean outcome. v1 protects the kill-criteria; v2 earns autonomy.

## How to deploy it

1. List 3-5 candidate wedges for the customer's case
2. For each, score:
   - **Value**: how much time / cost / risk does it remove if it works?
   - **Risk-of-irreversible-failure**: if it fails, can the user catch it before it does harm?
3. Place each candidate in one of the 4 quadrants
4. The wedge is the highest-value cell in the high-value, low-risk quadrant
5. Defend the choice with "confidence over size"

## Worked example (Helix Capital)

| Wedge | Value | Risk | Quadrant | Decision |
|---|---|---|---|---|
| Citation-grounded earnings draft (HITL) | High (4h → 30min) | Low (Rachel reviews) | High value / Low risk | **Ship as v1** |
| KPI quick-extract only | Low | Low | Low / Low | De-prioritize |
| Auto-tone-shift detection in isolation | Medium | High (mis-tagged = trading signal) | Med / High | Defer to v1.5 with calibration |
| MD&A diff with prior quarter | Medium | Medium | Med / Med | Defer to v1.5 |
| Position-sizing decision support | High in theory | Catastrophic (Chinese wall) | — | Out of scope permanently |
| Auto-publish to PMS | High in theory | Catastrophic (1 bug = trading loss + audit) | — | Out of scope permanently |

**Result**: option 1 ships. Largest in the high-value, low-risk quadrant.

## The probe this defends against

When the interviewer asks "why this wedge, not the bigger one", you don't say "we'll get there in v2." You say:

> "I optimize wedge selection on confidence of outcome, not size. Auto-publish would land more value, but the irreversibility of a bad note reaching a PM in week 2 isn't worth the upside. v1 protects the kill-criteria; v2 earns autonomy by shipping v1 clean for 90 days."

## What this matrix forces you to name

Three things the interviewer will probe:
- **Failure visibility**: who sees it fail, how badly, how fast
- **Failure reversibility**: can we catch and retry, or is the damage done
- **Stated risk explicitly**: not "we'll handle risks", but "I scored this at high-risk-irreversible and that's why it's out of v1"

## Bring the matrix to the meeting

The senior FDE move: literally draw this table on a whiteboard or include it on Slide 1 of your deck. The matrix is the artifact that proves you scoped on principles, not vibes.

## Complementary lens: Cost-of-Inaction (CoI)

The ORM frames wedges on *what you gain if you build it* (Value) × *what you risk if it goes wrong* (Risk). The **Cost-of-Inaction** lens (see [`consulting-frameworks.md`](consulting-frameworks.md)) frames the third question: *what does it cost the customer if you DON'T build this wedge?*

CoI matters when:
- The customer is skeptical the engagement is worth the budget (CoI defends the spend)
- You need to argue for sequencing (Phase 1 CoI < Phase 2 CoI ⇒ Phase 1 is still the right starting wedge)
- The customer has alternative vendors (CoI vs. delay-while-they-switch)

For each wedge in your matrix, add an annual CoI estimate. Example:

| Wedge | Value | Risk | CoI per year if not built |
|---|---|---|---|
| Wedge A (HITL drafter) | $500K saved | Low | $1.2M (2 senior analysts quit + alpha leak) |
| Wedge B (auto-publish) | $1.5M saved | High | Same as A — already covered by v1 |
| Wedge C (different workflow) | $200K saved | Low | $50K (minor annoyance) |

CoI makes wedge comparison fair across different value bands. It also gives the customer a number to defend the engagement to their board.

## Quick reference

```
WEDGE SELECTION:
  List 3-5 candidate wedges
  Score each on:
    - Value (time / cost saved if successful)
    - Risk of irreversible failure
  Place in 2x2 quadrant
  Wedge = highest-value cell in High value / Low risk quadrant
  Defend with "confidence over size"
```
