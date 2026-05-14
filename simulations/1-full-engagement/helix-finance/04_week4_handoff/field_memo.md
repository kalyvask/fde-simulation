# Field Memo — Helix Earnings-Note Wedge

> **From**: FDE Lead
> **To**: AI Lab Applied AI / Research / Product
> **Date**: End of week 4
> **Re**: What we shipped, what blocked us, what to fix in the platform

> Forward Deployed roles at frontier AI labs typically require sharing field feedback with Research and Product to influence model and product development. This memo is that artifact.

## What we shipped

A 4-week wedge for Helix Capital, a $2.3B long-short equity hedge fund: AI workforce that drafts the morning-after-earnings analyst note. **7 specialized agents** with a hybrid deterministic + LLM architecture, scoped to coverage names with standard earnings call format. Read-only on Bloomberg / FactSet / internal Postgres; write-only to a holding queue for senior-analyst approval.

The agent does **not** include M&A commentary, position-sizing recommendations, multi-quarter retrieval, or anything touching names on the MNPI watch list. Every output ships with a citation-grounded audit trace examiner-readable by Mei (compliance) and inspectable by Carmen (trading desk).

**Rollout shipped Monday week 5**, opt-in for first 2 weeks then expanding to mandatory if adoption + quality hold. Aditya (CTO) owns operations; Rachel + David lead the weekly draft review; Mei runs biweekly compliance review for the first 90 days; Carmen runs biweekly hostile review for the first 90 days.

**Metrics at end of week 4** (4-day production data):
- **Pass^k=5** with variance 3.2% on 80-case weighted eval, **96% pass rate** weighted
- **30-min senior-analyst review per note**, down from baseline 4 hours
- **70% adoption** in opt-in phase (8 of 12 investment professionals tried the system within 48 hours of rollout; 6 used the draft as a starting point on >50% of their notes)
- **Zero MNPI incidents** in 4 days (continuing the 3-year streak)

## What worked

**Hybrid det+LLM with deterministic high-stakes routing.** The MNPI Scrubber, Citation Verifier, and Compliance Critic are all deterministic Python. The LLM (Claude Sonnet) handles only natural-language synthesis — drafting notes — and grading them via LLM-as-judge. This containment of LLM stochasticity to the natural-language surface is the architectural pattern that made the engagement defensible to a default-no compliance officer.

**The MNPI Scrubber as the first deterministic gate.** Per-invocation watch-list pull (not cached at process startup) with fail-closed on pull failure. If a name is added to the watch list at 9:01 AM, the 9:02 AM agent invocation blocks. This was Sarah's named kill-criteria; the architecture makes the failure mode impossible, not just unlikely.

**Citation grounding as the second deterministic gate.** Every numerical claim in a draft must trace to a transcript line or filing item in the *current call* (no inheritance from prior-quarter context). The deterministic check is what gives the trading desk (Carmen) confidence to trade on the notes — she can verify any number in 10 seconds.

**Pairwise tone-shift detection.** The Tone Supervisor takes the prior-quarter note + current call and detects *deltas* in tone, not absolute tone. Calibrated against 50 pairwise samples from Rachel's 18-quarter coverage history. This was a real architecture revision from week 3 — the system as initially designed was a tone *classifier*, not a tone-*shift* detector.

**Reader-side transparency, not just author-side rigor.** Per Carmen's week-3 hostile review: the published note is inspectable by the downstream consumer (PM, trader), not just defensible by the analyst-author. Citation panels + override transparency + directional/conditional preservation deterministic checks. Different bar than analyst signoff; both bars met.

**The hostile review pattern with the silent skeptic.** Carmen went from silent-skeptic to active-reviewer in one 60-min session in week 3. The pattern: invite the skeptic to find what's wrong, not to validate what's right. Three architecture changes came out of that session that would have surfaced as week-5 production failures otherwise.

**Adoption tracked separately from quality.** The engagement metric — % of covered names where Rachel ships the agent's draft without re-write — is tracked separately from the pass^k eval. Quality at 96% without adoption above 50% would be a failed engagement; the dual track caught this before it became a relationship problem.

## What blocked us

### Model behaviors

1. **Directional language inflation on real Claude.** The Drafter inflated "maintaining guidance with a bias to the upper half" into "raising guidance" in one draft (caught by Carmen in week 3). The model treats semantically close phrases as interchangeable, but in financial language, "maintain" and "raise" are categorically different. Required deterministic post-processing against a controlled vocabulary of directional verbs.
   **Suggestion to AI lab**: when Claude is given a domain-specific controlled-vocabulary mapping (e.g., directional verbs in finance), the model should treat semantic equivalents as bound by the vocabulary, not collapsing them. A first-class "controlled vocabulary preservation" instruction would help.

2. **Conditional dropping on forward-looking statements.** The Drafter dropped the qualifier in "we *expect* stronger margins in 2027 *if* the supply environment resolves," producing "we expect stronger margins in 2027." Required a deterministic post-check that every modal verb appears within 30 words of a conditional marker.
   **Suggestion**: in regulated-industry contexts (finance, healthcare, legal), conditional preservation should be a primitive. The agent SDK could expose a "preserve qualifying clauses" instruction that the model treats as a hard constraint.

3. **Number inheritance across calls.** The Drafter pulled "$3.4B to $3.5B" from the prior-quarter note context and inserted it into a current-quarter draft where management had said "high end of range" without restating the numbers. Required a deterministic citation verifier that blocks any number not appearing in current-call source material.
   **Suggestion**: for RAG-grounded synthesis, when retrieving from temporally-ordered sources, the model should treat older context as background not as citable claims unless explicitly instructed. A "temporal context boundary" primitive would compress this work.

4. **Competitor anonymization not handled by prompt alone.** The Drafter quoted "unlike SAMPLE_COMPETITOR, our margins are improving" verbatim from a transcript, creating a Reg FD exposure on the buy-side firm. Required a deterministic post-processor to replace specific competitor names with anonymized phrasing ("a peer", "a competitor").
   **Suggestion**: domain-specific text-redaction primitives (Reg FD, MNPI, PII, PHI) as first-class agent components, rather than per-customer reimplementation.

### Product gaps

5. **No first-class "immutable agent snapshot" primitive.** The same pattern as Calder: re-implemented manually with model_version + prompt + knowledge-base hash + watch-list-version. A platform primitive that bundles these as one versioned artifact would have saved 4-5 days of plumbing work. **Highest-priority platform investment.**

6. **No native LLM-as-judge calibration tooling for pairwise comparison.** The tone-shift detector required pairwise calibration on consecutive-quarter notes, which we did manually with 50 samples. A platform-level "pairwise calibration helper" — Brier score, reliability diagrams, kappa — would have compressed the calibration work and made the eval suite more defensible to Mei.

7. **No examiner-trace renderer template for finance.** We built ours for Mei's audit-trace standard; every regulated-finance FDE deployment will rebuild theirs. A reference renderer (HTML + PDF, customizable, with regulatory-jurisdiction filters) would compress audit-readiness work for every finance / healthcare / insurance FDE customer.

8. **No "reader-side transparency" primitives.** Carmen's three asks (visible citation, directional preservation, override transparency) are all reader-side requirements that apply to any agent producing artifacts consumed downstream. Currently per-customer rebuilds. A reference set of reader-side transparency components would generalize across domains.

### Platform investments worth making

9. **Regulatory-jurisdiction-aware policy libraries.** Finance has SEC + FINRA + state regulators + jurisdictional overlays (MiFID II, FCA, SFC, JFSA, ASIC). Each has different forward-looking-statement disclosure rules. A first-class "regulatory variance" data structure with versioning, diffing, and audit hooks would be a moat. Healthcare has 50 state Medicaid agencies + HIPAA + state-level variations; same pattern.

10. **Death-spiral monitor for agent quality**. Rolling-window drift detection per ticker / per analyst / per agent. Carmen's "what if you slip from 96% to 92% over 8 weeks and nobody notices" is the real risk. As a platform primitive (with PagerDuty / Slack / OpsGenie connectors prebuilt), it'd be a click-deploy across customers.

## What I learned that I wish I'd known earlier

- **The reader-side transparency / author-side rigor distinction is two bars, not one.** I optimized for Rachel's signoff bar in weeks 1-2; Carmen's verification bar surfaced in week 3 as a parallel requirement. Should have asked Carmen in week 1: "what would you need to see in a draft to trade on it?"
- **The hostile review pattern works for any skeptic, not just downstream traders.** Carmen's pattern (invite the skeptic to find what's wrong) applied also to Mei's mock-audit in week 3. Two of the strongest engagements (Mei + Carmen) came from the same pattern: stakeholder runs their own adversarial test and reports findings to the FDE.
- **The 18/20 contract with the lead user is the actual ship gate, not the eval threshold.** I knew this conceptually from the Calder engagement; underweighted it in week 2 here. Rachel's 20-draft review in week 3 was the critical political milestone, not the pass^k threshold.
- **Adoption tracked separately from quality is non-negotiable.** The dual track ("% drafts shipped without re-write") caught a real risk: an engagement that hits 96% pass rate but has 20% adoption is a failed engagement, and the failure looks like a quality problem until you measure adoption separately.

## Reusability for the next engagement

60%+ of what shipped is portable to the next regulated-industry FDE deployment:

- **The hybrid det+LLM pattern** (workforce, BaseAgent, AuditTrace, MNPI Scrubber → Compliance Critic) — directly portable
- **The 3 sign-off criteria + named owners pattern** — directly portable
- **The hostile review session script** (60 min, "find what's wrong", 3 commitments by next gate) — directly portable
- **The dual-track adoption + quality measurement** — directly portable
- **Reader-side transparency primitives** (citation panels, override annotations) — directly portable to healthcare reports, legal contracts, any regulated-industry content
- **Pairwise tone-shift calibration pattern** — applies anywhere domain experts grade against a baseline (medical second opinions, legal precedent, etc.)

The Calder + Helix wedges together have validated this pattern across 2 regulated industries (insurance + finance). The next 2 should be healthcare prior-auth (HIPAA + state variance) and legal contract review (Reg FD analog + jurisdiction). Same shape, different content.

## What I'd ask AI Lab Product Team for, in priority order

1. **Immutable agent snapshot primitive** (5+ days of plumbing per engagement, every time)
2. **Reader-side transparency components** (citation panels, override annotations, directional-preservation deterministic checks)
3. **Regulatory-jurisdiction-aware policy library structure**
4. **Pairwise calibration tooling for LLM-as-judge**
5. **Domain-specific text-redaction primitives** (Reg FD, MNPI, PII, PHI)

Each of these is currently a per-customer build. Each one becomes a click-deploy if the platform takes it on. The total time saved across the next 5 regulated-industry engagements would be 4-6 weeks per engagement — meaningful compression on a 12-week budget.

## Closing note to Product

The Helix engagement validated the same architecture pattern we shipped at Calder, in a different regulated industry with different kill-criteria and different stakeholder dynamics. **The pattern travels.** What doesn't travel cleanly is the platform-specific plumbing (immutable snapshots, reader-side transparency, regulatory variance). Investing in those primitives is where the next 5 customers' acceleration lives.

— FDE Lead, end of week 4
