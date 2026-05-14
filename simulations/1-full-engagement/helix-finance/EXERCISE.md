# Helix Capital — How to Run This Simulation

> A 4-week guided FDE engagement on the Helix Capital case (hedge fund earnings-note automation). Different domain from Calder, same FDE skill. You do the work; the reference solutions show what good looks like AFTER you've attempted each phase.

## To begin the engagement: open [`START_HERE.md`](START_HERE.md)

That's the in-character entry point — Sarah's email lands in your inbox at 6:15 AM Monday, the engagement clock starts, the 9 AM kickoff is on the calendar. The reading list, the prep schedule, and the mindset reminders are there.

This file (`EXERCISE.md`) is the structural reference — the 4-week shape, the deliverables, the frameworks to deploy. Read it AFTER you've opened `START_HERE.md`.

## Before you start

1. **Open [`START_HERE.md`](START_HERE.md)** — the in-character kickoff
2. Read `00_brief.md` — the formal customer brief (Sarah refers to this in her email)
3. Pick your work cadence: 4 weeks at ~10 hours/week, or a compressed 2-week sprint at 20 hours/week
4. Set up a fresh repo for your work (don't edit this one)
5. Have an Anthropic or OpenAI API key configured (for the build phases)

## The 4-week structure

| Week | Folder | Your time |
|---|---|---|
| 1 | `01_week1_discovery/` | 6-10 hours |
| 2 | `02_week2_solution/` | 6-10 hours |
| 3 | `03_week3_validation/` | 8-12 hours |
| 4 | `04_week4_handoff/` | 4-8 hours |

## Discipline: do the exercise before reading the reference

Each week's folder contains exercise prompts and reference solutions. Attempt the exercise yourself before reading the reference. The reference is calibration, not a template.

## Week 1 — Discovery (6-8 hours)

**Your goal**: identify the wedge for the morning-after earnings-note workflow.

**What you should produce**:
- Stakeholder map for Helix's 7-person investment professional team (the brief names them; their archetypes are your job)
- Interview notes from 3-5 stakeholders (use Claude to play each persona)
- Data pull request to the CTO (what you need from Bloomberg / FactSet / internal systems)
- Wedge hypothesis: which earnings-note sub-task to automate first
- 1-page discovery memo

**Frameworks to deploy**:
- 4-source convergence
- Stakeholder archetypes (including the silent skeptic — for Helix this is the senior trader who reads notes with extra skepticism)
- Pain ladder

**Reference solution**: `discovery_memo.md`

## Week 2 — Solution + Build + Eval (10-14 hours)

**Your goal**: design the agent workforce, build a prototype, ship a weighted eval suite.

### Phase 2a — Solution design (3-4 hours)

What you should produce:
- Wedge selection defended on Outcome Risk Matrix
- 3-lens table filled in
- 7-agent workforce mapped to shapes (Extractor / Classifier / Synthesizer / Critic / Compliance critic / Router / Auditor)
- Integration map: read patterns + write patterns + 3-tier ladder
- Wedge proposal (1-2 pages)

Reference: `wedge_proposal.md`, `wedge_build_plan.md`

### Phase 2b — Build (5-7 hours)

What you should produce:
- Python prototype with 7 agent files
- Synthetic earnings-call generator (3-5 fake calls)
- MNPI Scrubber (deterministic, fires before any LLM call)
- KPI Extractor (Haiku)
- Note Drafter (Sonnet)
- Tone Supervisor (LLM-as-judge with calibration against SubjECTive-QA)
- Citation Verifier (deterministic)
- Audit Trace Generator (deterministic)
- End-to-end script that processes one earnings call through all 7 agents

**Starter code**: see `prototype/README.md` for the architecture. You can fork the scaffold or build cold.

Reference: `prototype/helix_agent/`, `prototype/scripts/run_e2e.py`

### Phase 2c — Eval (2-3 hours)

What you should produce:
- 30-50 case eval suite weighted by failure cost (MNPI block 10x, hallucinated number 5x, tone misread 2x)
- Adversarial set: MNPI smuggling, position-sizing slip, ambiguous tone
- Pass^k=5 results with variance ≤5%
- Production observability plan

Reference: `prototype/evals/`

## Week 3 — Validation (8-12 hours)

**Your goal**: validate the prototype with stakeholders. Rachel's 20-draft review is the political gate.

**What you should produce**:
- 20 sample drafts curated for Rachel's review (mix of routine + adversarial)
- Stakeholder session notes (Rachel 20-draft review, Mei biweekly compliance check, Sarah weekly status, Carmen hostile review)
- Updated eval suite incorporating findings from the review sessions
- 3 sign-off criteria status update — green / yellow / red with named owners
- Architecture revisions from the validation sessions

**Frameworks to deploy**:
- Hostile review pattern (invite the skeptic to find what's wrong, not validate what's right)
- 3 sign-off criteria with named owners
- Trusted Advisor formula (especially for Mei + Carmen, who go from default-no to active partner)

**Reference solution**: `03_week3_validation/sessions/` (4 stakeholder session notes)

## Week 4 — Production Gates + Handoff (4-8 hours)

**Your goal**: ship the wedge to production with named operational ownership.

**What you should produce**:
- Field memo (1-2 pages) summarizing what was learned + what would change in the AI lab product
- Run-book + rollback decision tree + platform-boundary doc
- Wedge demo session (all stakeholders, including downstream consumer Carmen)
- Handoff to operational owner Aditya (CTO) with named cadence through week 13
- Risks remaining, bucketed Business / UX / Technical with detection signals

**Frameworks to deploy**:
- Field-back-to-product memo structure
- 3-level metrics (Technical / UX / Business) with tension named
- Bucket-organized risks with detection signals
- Quick Win Milestone retrospectively reviewed

**Reference solution**: `04_week4_handoff/field_memo.md`, session notes in `04_week4_handoff/sessions/`

## At the end of 4 weeks

You should have:
- A working earnings-note agent prototype on synthetic data (your version)
- 50+ case weighted eval suite with pass^k=5 results
- 4-slide deck defending the architecture
- 1-page discovery memo + 1-page wedge proposal + 2-page field memo
- 4 stakeholder session notes (validation phase)
- Run-book + rollback procedure + platform-boundary doc
- Working knowledge of citation grounding + MNPI scrubbing + LLM-as-judge calibration + hostile-review pattern

This is the same skill set the 5-hour take-home (sim 2) tests under time pressure. Doing the full engagement first builds the muscle memory; doing the 5-hour version next tests whether you can execute under a clock.

## At the end of week 4

After your engagement completes:
1. Fill in [`../RETRO_TEMPLATE.md`](../RETRO_TEMPLATE.md) — be specific, subtract 1 point per dimension from your gut score
2. Package the artifacts using [`../PORTFOLIO_TEMPLATE.md`](../PORTFOLIO_TEMPLATE.md) — the work becomes a real interview signal only if you package it
3. Use [`../GRADE_YOUR_WORK.md`](../GRADE_YOUR_WORK.md) per phase to get a structured Claude-graded score before moving on

## Why two cases (Calder + Helix)?

Running both cases sequentially tests **domain portability** — a real FDE skill. The frameworks (3-lens, Outcome Risk Matrix, agent shapes, workflow decomposition) are the same in insurance and finance. The specific stakeholders, kill-criteria, and integration risks differ. If you can produce defensible work in both domains, that's a strong signal.

The senior FDE move: **do Calder full-path first, then Helix skip-ahead**. See [`../SKIP_AHEAD.md`](../SKIP_AHEAD.md) for the 15-hour skip-ahead path that does Helix weeks 3-4 cold while loading weeks 1-2 from the reference. Tests build + handoff craft on a new domain without re-doing discovery reps. Total time across both cases: ~45-50 hours.
