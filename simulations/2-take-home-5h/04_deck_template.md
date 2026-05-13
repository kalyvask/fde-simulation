# 4-Slide Deck Template

> Fill in the brackets. Don't add more slides. Don't design pixels.

> Before you fill this in, read `09_decision_principles.md`. Principles 1, 3, 4, 6, and 7 shape what goes on each slide.

---

## Slide 1 — The Wedge

**Headline (one sentence) — lead with the INSIGHT, not the activity** (Principle 7): [Frame the kill-criteria, not the agent. "Hallucinated numbers reaching a PM is the kill-criteria; this build makes that architecturally impossible" beats "we built a 7-agent workforce."]

**Wedge in one paragraph — use the 3-lens synthesis template** (Principle 8, see `10_3_lens_applied_to_helix.md`):
> "We're building [intent — Product] for [who — Customer] who's [emotional state — Customer]. The agent acts [trust-level summary — Product] and explicitly does not [out-of-scope — Product]. Architecturally it's [read/write — Technical] with [one specific risk — Technical] as the mitigated failure mode."
>
> Filled in for Helix:
> "We're building a citation-grounded earnings draft + tone-shift detector for Rachel — an exhausted senior analyst anxious about hallucinated numbers reaching a PM. The agent acts deterministically on the dangerous calls (MNPI block, citation verify) and asks the analyst on the soft calls; it explicitly does not touch M&A, position-sizing, or any write. Architecturally it's read-only v1 with MNPI watch-list drift as the one specific risk, mitigated by per-invocation list pulls + Mei-owned audit log."
>
> Target on **Track A** (output quality): [hallucination rate, citation precision, faithfulness]. Target on **Track B** (adoption/engagement): [% of covered names where Rachel ships the agent's draft without re-drafting] — see Principle 4.

**Why this wedge, not the obvious one — apply Principle 1**: [The obvious wedge is "automate the whole note end-to-end." Yours is narrower because **confidence of outcome wins over size of outcome**. The narrower wedge has lower hallucination surface and a clearer "what good looks like" definition. State this explicitly — the interviewer will probe it.]

**Outcome Risk Matrix (optional inset on this slide, or move to slide 3)**:

| | Low-risk failure | High-risk failure |
|---|---|---|
| **High value** | [Your v1 wedge here] | [v1.5 candidate with guardrails] |
| **Low value** | [De-prioritized] | [Permanently out of scope] |

**Out of v1 explicitly**:
- [Exclusion 1, with reason — tie to the matrix quadrant it falls in]
- [Exclusion 2, with reason]
- [Exclusion 3, with reason]

---

## Slide 2 — Agent Architecture

**Headline**: [One sentence describing the architecture pattern, e.g., "Seven specialized agents, hybrid det+LLM, MNPI as architectural first-line"]

**Diagram**: a single block-and-arrow diagram showing the agents in order. Use Mermaid or a quick drawing tool. Keep it readable.

**Agent decomposition table**:

| Agent | Job | Model tier | Det / LLM | Why this choice |
|---|---|---|---|---|
| [Agent 1] | [Job] | [Tier] | [Det/LLM] | [Rationale] |
| [Agent 2] | [Job] | [Tier] | [Det/LLM] | [Rationale] |
| ... | ... | ... | ... | ... |

**Integration map**:
- [System 1]: [Permissions] (read-only/write/etc)
- [System 2]: [Permissions]
- [System 3]: [Permissions]

**Why hybrid, not single-prompt**: [1 sentence — single-prompt fails on [specific failure mode]. Hybrid contains LLM variance to the natural-language layer.]

**Why this model tier breakdown**: [1 sentence — Haiku for deterministic-ish extraction, Sonnet for synthesis, etc. Or your reasoning.]

---

## Slide 3 — Risks + Testing Framework

**Headline**: [E.g., "Hallucinated numbers are the kill-criteria; citation grounding is the deterministic defense"]

**Top 3-5 risks with mitigations**:

| Risk | Mitigation | Owner |
|---|---|---|
| [Risk 1] | [Mitigation] | [Stakeholder] |
| [Risk 2] | [Mitigation] | [Stakeholder] |
| [Risk 3] | [Mitigation] | [Stakeholder] |

**Testing framework — 4 dimensions**:

1. **Static eval**: [Composition + weighting + grading dimensions]
2. **Pass^k**: [k value + variance tolerance]
3. **Adversarial set**: [What failure modes you stress-test]
4. **Production observability**: [Drift detection + alerting plan]

**Eval results so far**:
- Pass rate (weighted): [X% at k=Y]
- Cases passed: [X/Y]
- Top 1-2 failures + diagnostic [name them honestly]

**Three sign-off criteria for production rollout**:
1. [Criterion 1 with stakeholder owner]
2. [Criterion 2]
3. [Criterion 3]

---

## Slide 4 — Path to Production + Sequencing (Principle 3)

**Headline**: [E.g., "4 weeks to demo; ship-or-pivot decision week 4 Friday. Phase 2 + Phase 3 are sequenced, not deferred."]

**4-week plan (Phase 1)**:

| Week | Focus | Deliverable |
|---|---|---|
| 1 | Discovery + alignment | [Memo + wedge proposal + Mei MNPI watch list + James one-pager] |
| 2 | Eval + agent foundation | [Eval suite v1, MNPI Scrubber + Intake + KPI Extractor + Note Drafter wired] |
| 3 | Hardening + integration | [Sandbox live, Tone Supervisor + Citation Verifier wired, Rachel 20-draft review] |
| 4 | Production gates + handoff | [Production observability live, Mei sign-off, Carmen hostile review, live demo, field memo] |

**Operational owner post-handoff**: [Name; how the cadence works post-engagement]

**Phase sequencing — name the gates between phases** (Principle 3):

| Phase | Weeks | Scope | Gate to next phase |
|---|---|---|---|
| **Phase 1 (v1)** | 1-4 | [Citation-grounded earnings draft, read-only, Rachel reviews 100%] | Pass^k=5 + Mei MNPI sign-off + Rachel signs 20 sample drafts |
| **Phase 2 (v1.5)** | 5-12 | [MD&A diff + tone-shift detection calibrated against SubjECTive-QA] | Adoption metric ≥70% (Rachel ships agent's draft without re-drafting) |
| **Phase 3 (v2)** | 13+ | [Expanded coverage: more sectors, draft variants per recipient] | Cost-per-note <$X + zero MNPI incidents in prior 90 days |

This frames the wedge as the start of a portfolio, not a one-off. The Review probe "what's after v1?" gets a named answer with named gates, not "we'll figure it out."

---

## Quality checklist before sending

- [ ] 4 slides, not 5
- [ ] No screenshots of code (the repo has the code)
- [ ] One architecture diagram you'd defend
- [ ] Numbers on slide 3 (eval results) — **two tracks: output quality + adoption**
- [ ] Sign-off criteria named with stakeholder owners
- [ ] What's NOT in v1 is explicit on slide 1, tied to Outcome Risk Matrix quadrants
- [ ] Slide 1 headline leads with **insight (kill-criteria)**, not activity (Principle 7)
- [ ] Slide 4 has Phase 1 → 2 → 3 sequencing with named gates between phases (Principle 3)
- [ ] Read-only v1 framed defensively, not apologetically (Principle 6)

If you have all 9, ship.
