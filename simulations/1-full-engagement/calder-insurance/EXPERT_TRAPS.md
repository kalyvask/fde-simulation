# Calder Engagement — Expert Traps

> Five places where a candidate's first instinct produces a defensible-looking artifact that a real FDE would reject in week 1. Read this AFTER you've drafted the discovery memo and wedge proposal. Do not read it before. The point is to discover which traps your draft walked into.

## How to use this file

1. Complete your discovery memo, wedge proposal, and build plan without reading below.
2. Run the post-mortem: open [`../POST_MORTEM_PROMPT.md`](../POST_MORTEM_PROMPT.md), paste in your artifacts + the trap list from this file. Claude tells you which traps you walked into.
3. Compare to the reference solutions in this case folder. Notice that the references explicitly avoid all 5 traps.
4. Fix the trap, then move to the next phase. One fix per iteration; don't try to fix all 5 at once.

## The 5 traps

Each trap has the same shape:
- **What the candidate does** (the seductive first instinct)
- **Why it looks fine** (so you understand the trap)
- **Why it fails** (the customer or regulatory consequence)
- **The detection signal** (something concrete in your artifact)
- **The reference move** (what the calibrated solution does instead)

---

### Trap 1 — Picking the auto-pay-triage wedge

**What the candidate does.** Picks "auto-approve eligible claims for payment" as the v1 wedge. Reasoning: clean structured data, easy engineering, visible savings.

**Why it looks fine.** Auto-pay is the most measurable wedge. The data is structured. Engineering is tractable. You can write the eval suite in a day.

**Why it fails.** It's builder-shaped, not customer-shaped. The customer pain isn't payment decisions; it's the two NAIC market-conduct findings on the **comms layer**. The board is one finding away from a state DOI consent order. Auto-pay touches the coverage-decision regulatory surface (state-by-state adjuster licensing minimums); comms drafting doesn't. Auto-pay also walks straight into Priya's hard "no coverage decisions" rule from her interview.

**Detection signal.** Your wedge proposal names "auto-pay" or "claim approval" or "payment triage" anywhere in the v1 scope. Or your wedge has a coverage-validator agent whose output influences payment, not just downstream routing.

**The reference move.** The wedge is FNOL acknowledgment + first-status-update drafting on web + agent-portal channels. The agent never decides coverage and never writes back to Guidewire. The coverage-validator agent is read-only (confirms coverage exists; doesn't approve).

---

### Trap 2 — Using an LLM for state SLA timelines

**What the candidate does.** Uses an LLM to figure out "when must we respond to claimant X in state Y for line-of-business Z." Reasoning: state SLAs are documented; the LLM can read them.

**Why it looks fine.** It's a natural language task on natural language input. LLMs handle this all day. The agent shape is "synthesizer" or "extractor" from the catalog.

**Why it fails.** State SLAs are the load-bearing constraint for NAIC compliance. An LLM that hallucinates a 24-hour window when the actual SLA is 10 days (or, much worse, the reverse) is a finding waiting to happen. Marcus's job exists to enforce these. The 14 states have **variance** that the LLM will silently smooth over. This is the textbook "LLM where rules win" failure.

**Detection signal.** Your wedge proposal has an agent named "compliance" or "state-rules" that uses an LLM. Or your prototype's policy library is empty or stubbed. Or your eval suite doesn't have per-state slices.

**The reference move.** Compliance critic uses a **deterministic rules engine** loaded from Marcus's policy library (encoded as data, not LLM context). State SLA windows are keyed on `(state, line_of_business, channel)` lookup. The eval suite has per-state slices for the states where Marcus's library shows variance. LLM never sources a timeline.

---

### Trap 3 — Forgetting Tom (QA) is the eval set

**What the candidate does.** Builds a 50-case eval suite using synthetic data or by scanning the brief. Calls it done. Maybe asks Greg or Priya to review.

**Why it looks fine.** 50 cases is the right size. Adversarial set covers the obvious failure modes. The pass^k=5 results look defensible.

**Why it fails.** Tom keeps a private spreadsheet of every "bad close" pattern. That spreadsheet IS the calibrated eval set, written by the person who defines "bad" for NAIC examiners. A candidate who doesn't ask Tom for it is shipping evals calibrated against the wrong rubric. When the agent goes live and Tom's spreadsheet patterns start showing up, the candidate has no audit trail to defend the architecture.

**Detection signal.** Your wedge proposal or build plan doesn't name Tom as an owner of the eval set. Or your eval cases don't trace back to a Tom-validated failure pattern. Or your stakeholder map lists Tom only as "QA" without flagging him as the eval-set authority.

**The reference move.** The seed set is 50 cases from Tom (30 well-handled / 15 finding-pattern / 5 hardest-edge). Tom (via Sienna on his team) is named as the eval-set owner in the wedge proposal. Every regression case traces to a Tom-validated failure pattern. Marcus's policy library and Tom's spreadsheet are the two ground-truth artifacts of the engagement.

---

### Trap 4 — Auto-drafting without solving the data-pull layer

**What the candidate does.** Builds an FNOL drafter that produces beautiful acknowledgment text from the FNOL form fields. Demos it to Priya. Demo lands; pilot fails to move the 4-hour metric.

**Why it looks fine.** The acknowledgment text is exactly what Priya asked for. The eval shows 95% acceptance from Janet's 20-draft review. The architecture is clean: parse, classify, draft, supervise, send.

**Why it fails.** Priya told you in week 1 that the 4-hour grind isn't drafting — it's **hunting down information across 6 swivel-chair tools**. A drafter that only ingests the FNOL form ignores the actual bottleneck. The metric doesn't move because the adjuster still spends 3.5 hours hunting before they can confidently draft. The pilot looks like an adoption failure when it's actually a scope failure.

**Detection signal.** Your wedge proposal's "agent workforce" table has an Intake agent that only parses the FNOL form. No agent talks to Guidewire (even read-only) or the BPO comms history or the prior-claim history. Your metric forecast says "FNOL → first-touch median <30min" but you don't have an agent that retrieves the prior-claim or coverage context that's required to draft accurately.

**The reference move.** The Intake agent is paired with a Coverage Validator agent (read-only Guidewire API) that pulls policy + prior claim history. The acknowledgment drafter uses BOTH the FNOL form AND the retrieved context. The build plan calls out "sandbox access (Guidewire dev tenant)" as a Week 2 ask. Anil is named as the integration owner.

---

### Trap 5 — Treating Rachel (CISO) as a checkbox

**What the candidate does.** Writes a data-handling one-pager in week 4 as a handoff artifact. Calls Rachel "we'll loop in Rachel for security review."

**Why it looks fine.** Security review is a standard handoff step. The wedge proposal mentions PII handling. The one-pager will get written.

**Why it fails.** Rachel is a default-no skeptic on data residency + PHI. If she gets the one-pager in week 4, she has 1 week to red-team a 4-week design and her path of least resistance is to block. The candidate has now spent 4 weeks on architecture that Rachel rejects in 30 minutes. The pilot is dead. The CCO loses confidence in the engagement.

**Detection signal.** Your week-1 "asks" table doesn't have "Rachel sign-off on data one-pager" with a Friday-of-week-1 date. Your discovery memo lists Rachel under "stakeholders" but not under "kill criteria gatekeepers." Your architecture doesn't name where PHI is scrubbed (or worse: doesn't acknowledge that auto FNOLs contain PHI at all).

**The reference move.** Rachel's one-pager sign-off is the first ask in the asks table, dated Friday-of-week-1. The architecture explicitly states which agents see PHI and where it's scrubbed. The discovery memo names Rachel as a default-no archetype with a how-to-engage note ("lead with audit trace; data residency answers in writing; never ask her to trust LLMs verbally"). PHI handling is a v1 design constraint, not a v2 hardening item.

---

## Bonus trap (free, no extra detection signal)

### Trap 0 — Pitching Maria before scoping

**What the candidate does.** Walks into the 9 AM kickoff with Maria, opens with "Based on the brief, I'd recommend an AI workforce that handles..."

**Why it fails.** Maria explicitly says in her interview prompt: "you expect the FDE to scope before solutioning." Solutioning before discovery signals you're builder-shaped, not customer-shaped. Maria has seen four vendors do this and shown them the door.

**The reference move.** Open with "Before I'd recommend anything, I want to make sure I understand your kill-criteria correctly. The two market-conduct findings — both on the comms layer, right? And you've said another would mean a consent order. Can you walk me through what the third finding pattern would have to look like for that to happen?" Then 30 minutes of discovery before any solution language.

---

## Why these 5 (and not others)

These are the traps where a senior FDE on the OpenAI / Anthropic / Sierra / Palantir interview panel would silently downgrade you. They're not the only traps in the engagement; they're the ones with the highest probability of catching someone who's smart, motivated, and pattern-matching from a non-FDE background (typical AI PM, traditional consultant, ML engineer pivoting to deployed work).

The traps map to the 5 FDE skill dimensions in the rubric:
- Trap 1 → customer-first framing (wedge selection)
- Trap 2 → architecture judgment (model-vs-application-layer)
- Trap 3 → production thinking (eval suite calibration)
- Trap 4 → systems thinking (workflow decomposition + integration)
- Trap 5 → risk surfacing (security as a v1 constraint)

If you walked into 4 of 5, the rubric score will reflect it. If you walked into 0 of 5, the post-mortem checker will say so, and you're at the FDE final-round bar on this case.
