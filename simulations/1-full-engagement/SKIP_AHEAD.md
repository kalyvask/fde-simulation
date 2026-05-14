# Skip-Ahead Path: Weeks 3 + 4 Cold

> A guide for senior candidates who have run engagements before and want to spend their time on the harder, more rep-worthy phases. Skip discovery + solution-strategy reps; do build + handoff cold. ~15 hours instead of 30-40.

## Who this is for

You should consider this path if **two or more** apply:

- You've shipped at least one production AI agent workforce before
- You've done at least one customer-embedded engagement (FDE, Solutions Architect, Customer Engineer, technical consulting)
- You can sketch a 3-lens scaffold from memory in under 5 minutes
- You've already done the Calder OR Helix engagement once and want a faster rep on the other one
- You're 1-2 weeks from a real FDE interview and want to focus on the highest-leverage prep

If **none** of these apply, do the full engagement instead. The discovery and solution-strategy phases are where most of the FDE craft lives — skipping them for speed makes you faster at the wrong things.

## What you skip vs what you do

| Phase | Full path | Skip-ahead path |
|---|---|---|
| Week 1 (Discovery) | Run all 7 stakeholder interviews with Claude; write your own discovery memo | **Skip** — read the reference `discovery_memo.md` as given context |
| Week 2 (Solution) | Score wedges on Outcome Risk Matrix; draw 3-lens; write build plan | **Skip** — read the reference `wedge_proposal.md` + `wedge_build_plan.md` as given context |
| Week 3 (Build + Eval) | Build the prototype from scratch on a clean repo; write eval cases | **Do cold** — extend the scaffolded prototype with 3-5 new agents OR refactor 2 existing agents to a different architecture pattern |
| Week 4 (Handoff) | Run the demo + handoff sessions; write the field memo | **Do cold** — write your own field memo + run-book; design the rollback procedure |

The skip-ahead path keeps the **engineering judgment + handoff craft** but drops the **discovery + scoping reps**.

## The self-test before skipping

Don't skip until you can answer all 5 of these in under 30 seconds each. If you can't, do the full engagement.

### Test 1 — Wedge defense

Without reading the reference solution, defend the wedge choice for Calder:

> "Why is the wedge 'auto-acknowledge + draft first-status updates' instead of 'automate the whole claims-resolution workflow'?"

Strong answer: confidence over size, Outcome Risk Matrix puts auto-acknowledge in High-value / Low-risk because the analyst reviews before send, and the kill-criteria is NAIC market-conduct findings on the comms layer specifically.

If you can't deliver that in 30 seconds, do week 1-2.

### Test 2 — Architecture defense

Without looking at the prototype, sketch the agent decomposition for Helix:

> "Walk me through the 7 agents and why each one exists."

Strong answer: MNPI Scrubber (deterministic, fires first), Intake Classifier (Haiku, routes), KPI Extractor (Haiku, hybrid), Note Drafter (Sonnet, LLM), Tone Supervisor (Sonnet, LLM-as-judge), Citation Verifier (deterministic), Audit Trace Generator (deterministic). Justify each with failure-mode reversibility.

If you can't, do week 2.

### Test 3 — Stakeholder political map

Without reading the reference, name the silent skeptic for both cases:

> "For Calder, the silent skeptic is [who]? For Helix, [who]? Why does it matter?"

Strong answer: Calder = Compliance Officer Marcus Hill; Helix = Senior Trader Carmen Diaz. Silent skeptics surface as blockers in week 5+ if not engaged in week 1-3.

If you can't, do week 1.

### Test 4 — Sign-off gates

Name the 3 sign-off gates with named owners for one of the cases:

> "What does production-ready actually mean for this engagement?"

Strong answer: Pass^k=5 with variance ≤5% (Aditya/Anil), compliance + audit-trace standard signed (Mei/Marcus), lead user reviews 20 sample outputs and signs off (Rachel/Janet).

If you can name these in under 30 seconds, you can skip.

### Test 5 — Compliance failure mode

Name the most expensive single failure mode for either case:

> "What's the failure mode that would end the engagement?"

Strong answer: Calder = third NAIC market-conduct finding = state DOI consent order; Helix = hallucinated number in a published note that a PM trades on = trading loss + SEC inquiry.

If you can, skip.

---

## The skip-ahead playbook (15 hours)

### Hour 0-1: Load context

- Read `00_brief.md` (the customer prompt)
- Read `01_week1_discovery/discovery_memo.md` (the reference)
- Read `02_week2_solution/wedge_proposal.md` + `wedge_build_plan.md` (the reference)
- Read `02_week2_solution/prototype/README.md` + `SCAFFOLD_OVERVIEW.md`

**You now have**: the same context the full-path candidate had at end of week 2. From here you do everything they did in weeks 3-4, faster.

### Hour 1-4: Extend the prototype (the engineering rep)

Pick ONE of these (don't do all):

**Option A — Add an agent you'd argue is missing.** Look at the existing 5-7 agents and propose a missing one. Build it. Defend why it's necessary in your write-up.

Candidate additions for Calder:
- A SIU triage agent (special investigation unit, fraud routing)
- A multi-claim correlation agent (looks across recent FNOLs for the same claimant)

Candidate additions for Helix:
- A consensus-trend tracker (across multiple analysts' notes)
- A peer-call comparator (cross-references current call against same-sector calls from prior 90 days)

**Option B — Refactor an existing agent to a different architecture.** Pick one of the LLM agents (e.g., Drafter or Tone Supervisor) and:
- Convert it from single-prompt to multi-step reasoning
- Add a self-critique loop
- Replace it with a deterministic-leaning version + reduce LLM calls by 50%
- Add tool-use (calculator, retrieval) to the agent's loop

Defend the refactor in your write-up: what got better, what got worse, what tradeoff you made.

**Option C — Add an adversarial eval set.** Build a 20-case adversarial eval suite that targets failure modes the seed set doesn't cover. Examples:
- For Calder: state-DOI variance cases per state, multi-vehicle complications, bodily-injury edge cases at scope boundary
- For Helix: cross-quarter inheritance attacks, tone-shift edge cases (e.g., a CEO change mid-quarter), regulated-jurisdiction forward-looking statements

Run it. Note which cases fail. Diagnose root cause. Propose fixes (don't implement them all; the diagnosis is the artifact).

### Hour 4-8: Run the full eval suite cold

Without looking at the reference run, set up the eval suite:

1. Run `python scripts/run_eval.py` with the default cases. Note baseline.
2. Add 10 of your own eval cases targeting specific risks you identified
3. Re-run with `--k 5` (pass^k production threshold)
4. If pass rate <90%, diagnose root cause (drafter prompt? policy rule? extractor confidence?)
5. Iterate: fix one thing, re-run, repeat

The discipline: don't lower the threshold to pass. Either fix the system or document why the failure is acceptable (e.g., expected adversarial-block behavior).

By end of hour 8 you should have:
- Pass^k=5 results documented (your version, not the reference)
- 10+ new eval cases you wrote
- A list of failures you diagnosed but didn't fix (the v1.5 backlog)

### Hour 8-11: Design the production handoff (the FDE rep)

Three artifacts to produce:

**1. Run-book** (1-2 pages). What does the customer's CTO do when:
- Pass rate drops 5% over 7 days?
- A new state regulation changes the disclosure rules?
- The LLM provider has a 30-min outage?
- An analyst flags a draft as misleading?
- The compliance officer wants to audit a specific note from 3 months ago?

The run-book documents the operational procedure for each. See the Calder/Helix reference handoff sessions in `04_week4_handoff/sessions/` for shape.

**2. Rollback decision tree** (1 page). Three layers (instant / prompt-only / full) with a decision tree for which to use when. The scenario you walk through: pass rate has dropped from 96% to 82% over 12 hours. What do you do?

**3. Platform-boundary doc** (1 page). What stays with the customer forever vs what comes from the FDE platform. Critical for "the customer can take a model update without re-engaging us."

These are the artifacts that show production-readiness. They're rare in candidate portfolios.

### Hour 11-14: Write the field memo (the lab-feedback rep)

The field memo is the artifact that signals you've thought about platform-level investments, not just customer-specific ones. See `04_week4_handoff/field_memo.md` for shape.

Cover:
- What you shipped (concrete)
- What worked (with the architectural principle that made it work)
- What blocked you (specific platform gaps with suggestions)
- What you'd ask AI lab Product team for, in priority order

Length: 1-2 pages. The exercise is the prioritization, not the wishlist.

### Hour 14-15: Fill out the retrospective + portfolio packaging

Open [`RETRO_TEMPLATE.md`](RETRO_TEMPLATE.md). Fill it out honestly.

Open [`PORTFOLIO_TEMPLATE.md`](PORTFOLIO_TEMPLATE.md). Package the prototype + your new agent / refactor / eval suite + the run-book + the field memo into a portfolio-ready repo.

By end of hour 15 you have a portfolio piece. Not as deep as the full-engagement version, but it covers the build + handoff craft that interviewers grade hardest.

---

## What you've gained vs the full path

| Capability | Full path (30-40 hrs) | Skip-ahead path (~15 hrs) |
|---|---|---|
| Stakeholder interview craft | ✅ deep | ⏳ borrowed from reference |
| Wedge selection from cold | ✅ deep | ⏳ borrowed from reference |
| 3-lens scaffold practice | ✅ deep | ⏳ borrowed from reference |
| Outcome Risk Matrix practice | ✅ deep | ⏳ borrowed from reference |
| Prototype extension judgment | ⚖ moderate | ✅ deep |
| Eval suite design + diagnosis | ⚖ moderate | ✅ deep |
| Run-book + rollback design | ⚖ moderate | ✅ deep |
| Field memo / platform-feedback craft | ⚖ moderate | ✅ deep |
| Portfolio-readiness | ✅ ready | ✅ ready |

Skip-ahead trades discovery-craft reps for build-craft reps. Right trade if discovery is already strong.

## Anti-patterns of the skip-ahead path

| Anti-pattern | Why it's a trap |
|---|---|
| Skipping discovery because "I know the case" | You don't. Reading the reference and running the interviews are different reps. |
| Adding a new agent for its own sake | The agent should defend a missing failure-mode coverage. "More agents" is not better. |
| Building the eval suite from the seed cases only | Adversarial cases are the rep. Add at least 10. |
| Writing the run-book in the abstract | Walk through 5 specific scenarios. Generic run-books are not portfolio-grade. |
| Skipping the retrospective | The retro is the highest-leverage hour. Don't skip it. |
| Skipping the portfolio packaging | The build work is invisible without packaging. The packaging is half the portfolio value. |

## When to NOT skip ahead

Even if you pass the self-test, do the full path if:

- You've never done a customer-embedded engagement in a regulated industry
- You're prepping for OpenAI Deployed PM or Anthropic Solutions Architect specifically — these companies hire heavily on customer-engagement craft, not just engineering
- You have time (>30 hours available before the interview); the full path is strictly higher-signal
- You're doing Helix as your second case after Calder; the discovery-craft transfer between cases is itself a rep

The skip-ahead path is an optimization, not the default. Most candidates should do the full engagement at least once.

## After the skip-ahead engagement

By the end you have:
- Extended prototype + new architecture decision documented
- Pass^k=5 eval results on cases you wrote
- Run-book + rollback procedure + platform-boundary doc
- Field memo with prioritized platform-feedback
- Filled-out retrospective
- Portfolio-ready repo

That's 6 artifacts in 15 hours. The same artifacts as the full path produces, with weaker discovery context but stronger build context.

For maximum benefit: **do Calder full-path first, then Helix skip-ahead.** That gets you discovery craft once + build craft twice across 2 domains, in ~45-50 hours total. The combination is what most candidates need to clear the FDE bar.
