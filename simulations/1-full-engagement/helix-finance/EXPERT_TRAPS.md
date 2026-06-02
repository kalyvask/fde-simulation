# Helix Engagement — Expert Traps

> Five places where a candidate's first instinct produces a defensible-looking artifact that a real FDE would reject in week 1. Read this AFTER you've drafted the discovery memo and wedge proposal. Do not read it before. The point is to discover which traps your draft walked into.

## How to use this file

1. Complete your discovery memo, wedge proposal, and build plan without reading below.
2. Run the post-mortem: open [`../POST_MORTEM_PROMPT.md`](../POST_MORTEM_PROMPT.md), paste in your artifacts + the trap list from this file. Claude tells you which traps you walked into.
3. Compare to the reference solutions in this case folder.
4. Fix the trap, then move to the next phase. One fix per iteration.

## The 5 traps

---

### Trap 1 — Picking the trade-idea-generation wedge

**What the candidate does.** Picks "agent that generates short-thesis ideas" or "agent that screens for asymmetric setups" as the v1 wedge. Reasoning: highest-value workflow, most defensible AI use case, headline-worthy.

**Why it looks fine.** Idea generation is what analysts do. It's the visible output of the investment process. LLMs are good at synthesis. The wedge sounds ambitious.

**Why it fails.** Idea generation isn't the time bottleneck — note drafting is (4 hours per analyst per note × 5 senior analysts × 56 notes/year = 1,120 hours/analyst/year). It's also the regulatory minefield: a trade-idea agent crosses into MNPI territory the moment it touches a watch-list name, and it walks into Carmen's silent skepticism ("I got burned twice by hallucinated numbers in past analyst notes" — and her objection scales fast when the agent is generating, not transcribing). Sarah's kill-criteria #1 is hallucinated numbers, not slow ideation.

**Detection signal.** Your wedge proposal names "idea generation," "thesis generation," "screening," or "asymmetric setups" in v1. Or your agent workforce doesn't have a Note Drafter as the primary synthesis agent. Or your metric forecast doesn't include "time analyst spends per note."

**The reference move.** The wedge is the morning-after-earnings analyst note drafter. The agent ingests transcript + 10-Q + prior notes + consensus, drafts a 1-page note, and hands off to the senior analyst for review. The agent does NOT generate independent investment theses (Rachel still owns the thesis). The metric is 4 hours → 30 minutes review time per note.

---

### Trap 2 — Letting the LLM source numbers

**What the candidate does.** Builds a Note Drafter that takes the call transcript + filings and writes the draft including the numerical KPIs (revenue, EPS, guidance). Trusts the LLM to extract correctly and cite. Adds a downstream "verify citations" check.

**Why it looks fine.** Modern LLMs are good at extraction. The Citation Verifier catches misalignment. The architecture is clean: drafter → verifier → ship.

**Why it fails.** This is Sarah's kill-criteria #1, hand-delivered. The moment the LLM is the source of a number, the system is one prompt injection / one parsing error / one hallucination away from publishing a wrong guidance figure to a PM who acts on it. Carmen's burns came from exactly this pattern. The verifier-as-second-pass design is fragile because the verifier has to catch the LLM's mistakes; the architecturally-safe design is to never let the LLM source the number in the first place.

**Detection signal.** Your agent workforce has the Note Drafter writing numbers without a deterministic KPI Extractor agent feeding it span-grounded values. Or the Citation Verifier is described as "LLM-as-judge" or "LLM checks cites" instead of deterministic span matching. Or your eval suite doesn't weight hallucinated-guidance failures 10x.

**The reference move.** KPI Extractor is its own agent, produces structured `{value, span, source_doc}` objects, and the Note Drafter receives those structured values, never the raw transcript for numbers. The Citation Verifier is deterministic span matching: every number in the draft must trace to a `(value, span, source_doc)` tuple from the Extractor's output. The eval suite weights `citation_faithfulness_on_numbers` and `hallucinated_guidance_rate` 10x.

---

### Trap 3 — Adding M&A commentary or position sizing

**What the candidate does.** The draft note includes a section on M&A speculation ("management's comments on consolidation in the space suggest...") or a position-sizing tag ("we'd add to the position at this level"). Reasoning: analysts write this stuff; the agent should too.

**Why it looks fine.** A complete analyst note includes both. Leaving them out feels like an incomplete product. The senior analyst can always edit out what they don't want.

**Why it fails.** M&A commentary is a regulatory minefield (selective disclosure rules, Reg FD); position sizing is a Chinese-wall breach (research agent producing trading-desk-actionable content). Mei runs mock-audits on weekends; either of these will get the system pulled in week 1 of pilot. The "senior analyst edits out" defense fails because the agent has already produced the content into the audit trail; the existence of an M&A-speculation paragraph in the trace is the violation.

**Detection signal.** Your wedge proposal's "what this does" or "agent capabilities" list includes M&A, deal commentary, consolidation, position sizing, target prices, or trade recommendations. Or your scope-out section doesn't explicitly carve these out.

**The reference move.** The wedge proposal has an explicit "what this wedge does NOT do" section that names: M&A commentary (regulatory minefield), position sizing (cross-Chinese-wall), independent investment theses, names on the MNPI watch list. The Compliance Critic agent runs Mei's rules deterministically and blocks any draft containing forbidden content categories before it reaches Rachel for review.

---

### Trap 4 — Tone-shift detection without calibration

**What the candidate does.** Adds a Tone-Shift Detector agent that uses an LLM with embeddings to compare management's call language vs prior calls and flag shifts. Calls it done. Ships v1.

**Why it looks fine.** Tone shift is a known alpha signal. Embedding-based comparison is a textbook pattern. The LLM produces nuanced flags.

**Why it fails.** Without human-labeled calibration, tone-shift is the highest-variance agent in the workforce. The LLM will silently produce false-positive flags ("management seems less confident") that Rachel checks, finds nothing to support, and stops trusting. By note 5 she's ignoring tone flags entirely; by note 10 she's routing around the system. Carmen-class silent-skeptic failure mode. Tone-shift is also the agent most likely to embed implicit MNPI inference if you let it (e.g., "tone shift on the consumer-segment call suggests an undisclosed channel issue" — that's literally MNPI generation, not detection).

**Detection signal.** Your wedge proposal has a Tone-Shift Detector but no calibration agent or held-out labeled set. Or your eval suite doesn't have a `tone_shift_detection_F1` metric. Or your prototype's tone-shift output is a free-text LLM judgment, not a structured `{dimension, direction, confidence, supporting_spans}` object.

**The reference move.** Tone-Shift Detector uses embeddings + SubjECTive-QA rubric (6 dimensions: certainty, optimism, specificity, hedging, defensiveness, forward-looking). A Tone-Shift Calibration agent (LLM-as-judge) grades the detector against a held-out set Rachel + David graded. The eval metric is F1 ≥ 0.80 vs SME labels. Output is structured, not free-text. Calibration runs before Rachel sees any production flags.

---

### Trap 5 — Treating Carmen as someone you can ignore

**What the candidate does.** Maps stakeholders, lists Carmen as "Senior Trader" or "silent skeptic," doesn't book a 1:1 with her. Reasoning: she's not a buyer, not a user, not a gate. Focus on Sarah, David, Rachel, Mei.

**Why it looks fine.** Resource-constrained engagement. Skip the non-essential stakeholders. Get the core 5 on side.

**Why it fails.** Carmen got burned twice. She's the firm's institutional memory of "AI got a number wrong, we lost money." She talks to other traders in the kitchen. If she's not part of the early validation, the moment a junior trader complains about a draft note, Carmen amplifies it and the system loses trader trust. Trader trust is what makes Rachel's notes useful (notes that no one trades on are notes no one uses). Skipping Carmen is the most common political failure in this kind of engagement.

**Detection signal.** Your discovery memo doesn't have a Carmen interview note. Or your stakeholder map lists her without a how-to-engage move. Or your week-3 validation plan doesn't include a hostile-review session with Carmen as a deliberate scheduled event.

**The reference move.** Carmen gets a 1:1 in week 1 with a specific question: "what did the past hallucinated-numbers incidents actually look like, and what would I have had to show you to prevent them?" Her answer becomes 2-3 adversarial eval cases. Week 3 includes a deliberately-scheduled hostile-review session with Carmen on the draft notes; her sign-off (or explicit unblock) is a gate. Her past burns are quoted in the field memo to OpenAI / Anthropic Research as why citation-faithfulness is a kill-criteria signal, not a polish item.

---

## Bonus trap

### Trap 0 — Building before the MNPI Scrubber

**What the candidate does.** Builds the agent workforce starting with the Intake / KPI Extractor / Drafter, plans to add MNPI handling later. Reasoning: "we'll never actually feed it MNPI; the scrubber is belt-and-suspenders."

**Why it fails.** The MNPI Scrubber is the first deterministic agent, before any LLM call. If it's added later, the architecture has been wrong from day 1 and the audit trail can't prove the system never saw MNPI. Mei's mock-audits will surface this and the engagement dies. Architecturally, MNPI handling is a v1 design constraint, not a v2 hardening item.

**The reference move.** MNPI Scrubber is Agent #1. Deterministic. Watch-list lookup. Blocks any prompt touching a watch-list name before the LLM is called. Mei signs off on the scrubber spec in week 1. James (COO) gets the data-handling one-pager in week 1, not week 4.

---

## Why these 5 (and not others)

These are the traps where a senior FDE at a hedge fund engagement, or an Anthropic / OpenAI Solutions panel reviewing a Helix-shaped case, would silently downgrade. They map to the rubric dimensions:

- Trap 1 → wedge framing (idea generation vs note drafting)
- Trap 2 → architecture judgment (deterministic-where-reliability-is-non-negotiable)
- Trap 3 → risk surfacing (regulatory + cross-wall)
- Trap 4 → production thinking (calibration before trust)
- Trap 5 → customer-first framing (silent-skeptic conversion)

A clean Helix engagement avoids all 5. A typical first-attempt walks into 2-3 of them. The post-mortem checker tells you which.

## What each trap signals to the hiring manager

The rubric grades the artifact. The interviewer is also reading each trap as one of the three **Unforgivables** — the anti-signals that get a candidate rejected regardless of technical strength. See [`../../../frameworks/essentials-unforgivables.md`](../../../frameworks/essentials-unforgivables.md). When you run the post-mortem, translate each trap you walked into:

- Trap 1 (idea-generation wedge because it's ambitious) → **Unforgivable 1: chasing the headline-worthy thing over the actual bottleneck**
- Trap 4 (textbook tone-shift detector shipped without calibration) → **Unforgivable 1: shiny pattern over the reliability Rachel needs to trust it**
- Trap 5 (didn't book Carmen because she "isn't a buyer") → **Unforgivable 2: passivity — didn't drive the silent skeptic who controls trader trust**
- Trap 0 (building before the MNPI Scrubber) → **Unforgivable 2: deferred the load-bearing constraint instead of owning it in week 1**

Trap 2 (letting the LLM source numbers) and Trap 3 (adding M&A / position sizing) read primarily as risk-surfacing misses, but a candidate who *defends* them under the grill — "the verifier catches it" — tips into **Unforgivable 3: entitlement**, treating the kill-criteria as someone else's problem. Self-diagnosing in the interviewer's vocabulary is the point.
