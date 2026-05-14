# Calder Insurance — How to Run This Simulation

> A 4-week guided FDE engagement on the Calder Insurance case. You do the work; the reference solutions show what good looks like AFTER you've attempted each phase.

## To begin the engagement: open [`START_HERE.md`](START_HERE.md)

That's the in-character entry point — Maria's email lands in your inbox at 7:45 AM Tuesday, the engagement clock starts, the 9 AM kickoff is on the calendar. The reading list, the prep schedule, and the mindset reminders are there.

This file (`EXERCISE.md`) is the structural reference — the 4-week shape, the deliverables, the frameworks to deploy. Read it AFTER you've opened `START_HERE.md`.

## Before you start

1. **Open [`START_HERE.md`](START_HERE.md)** — the in-character kickoff
2. Read `00_brief.md` — the formal customer brief (Maria refers to this in her email)
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

Each week's folder contains:
- The exercise prompts (`current_state_template.md`, `interview_questions.md`, `stakeholder_map.md`)
- Reference solutions (completed memos, proposals, prototype code)

The discipline is: **attempt the exercise yourself before reading the reference solutions.** The reference is calibration, not a template to copy.

Suggested order for each week:
1. Read the exercise / template files first
2. Spend the suggested time producing your own artifact
3. Compare against the reference solution
4. Note the gaps. Those are your prep targets.

## Week 1 — Discovery (6-10 hours)

**Your goal**: identify the wedge (the narrow first workflow you'd automate) and write a 1-page discovery memo.

**What you should produce by end of week 1**:
- Stakeholder map (6-8 archetypes with names + roles + how to engage)
- Interview notes from 3-5 of the stakeholders (use the personas in `interviews/` to "interview" them; ask Claude to play each)
- Data pull request to the customer's tech team (what data you need, why)
- One-paragraph wedge hypothesis
- 1-page discovery memo to the customer

**Frameworks to deploy**:
- 4-source convergence (Buyer / Brief / Industry / Operator)
- Stakeholder archetypes (champion / blocker / silent skeptic / user / tech / compliance / operations)
- Pain ladder (symptom → cause → root cause)

**Reference solution**: `discovery_memo.md`, `stakeholder_map.md`, `recap_email_to_maria.md`, `rachel_one_pager.md`

## Week 2 — Solution Strategy (6-10 hours)

**Your goal**: pick the wedge, design the agent workforce, write the build plan.

**What you should produce**:
- Wedge selection defended on the Outcome Risk Matrix (Value × Risk of irreversible failure)
- 3-lens table filled in (Customer / Product / Technical)
- Agent decomposition: 5-8 specialized agents mapped to shapes
- Integration map: read patterns + write patterns + 3-tier ladder
- 4-week build plan with phase gates
- 4-slide deck draft

**Frameworks to deploy**:
- 3-lens scaffold (Customer / Product / Technical)
- Outcome Risk Matrix
- Workflow decomposition (5-step method to draw agent boundaries)
- Agent shapes catalog

**Reference solution**: `wedge_proposal.md`, `wedge_build_plan.md`, `prototype/` (the completed scaffold)

## Week 3 — Build + Eval (8-12 hours)

**Your goal**: ship a working prototype that processes synthetic data end-to-end, with a weighted eval suite.

**What you should produce**:
- Python prototype with 5-8 agent files implementing your architecture
- Synthetic data generator (3-5 fake claims)
- End-to-end script that processes one claim through all agents
- Audit trace per claim
- Eval suite with 30-50 weighted cases (happy path + adversarial)
- Pass^k=5 results with variance ≤5%

**Frameworks to deploy**:
- 5 principles of AI workforce design (decompose by failure mode, deterministic gates around dangerous calls, read before write, one job per agent, dumb orchestrator)
- 4-dimensional testing (static eval + pass^k + adversarial + production observability)

**Starter code**: see `prototype/SCAFFOLD_OVERVIEW.md` for the architecture you're building toward. You can either fork the existing scaffold or build cold.

**Reference solution**: `prototype/calder_agent/` (the completed agents), `prototype/evals/` (the eval suite), `prototype/scripts/run_e2e.py`

## Week 4 — Production Gates + Handoff (4-8 hours)

**Your goal**: production-readiness — observability, rollback, handoff documentation.

**What you should produce**:
- Field memo (1-2 pages) summarizing what was learned + what would change in the product
- Production checklist: drift detection, alerting, rollback procedure, named operational owner
- 3 sign-off criteria with stakeholder owners
- Risks organized by bucket (Business / UX / Technical) with detection signals
- Updated 4-slide deck (final version)

**Frameworks to deploy**:
- 3-level metrics (Technical / UX / Business) with tension named
- Risk buckets with detection signals

**Reference solution**: `field_memo_to_anthropic.md`, session notes in `sessions/`

## At the end of 4 weeks

You should have:
- A working agent prototype on synthetic data (your version)
- 30-50 case weighted eval suite with pass^k=5 results
- 4-slide deck defending the architecture
- 1-page discovery memo + field memo
- A clear sense of where your FDE skill is strong vs weak

## After the engagement

Three artifacts to produce after week 4 (each ~30-60 min):

1. **Fill in [`../RETRO_TEMPLATE.md`](../RETRO_TEMPLATE.md)** — be specific, be honest, subtract 1 point per dimension from your gut score
2. **Package using [`../PORTFOLIO_TEMPLATE.md`](../PORTFOLIO_TEMPLATE.md)** — the work becomes a real interview signal only if you package it
3. **Self-grade via [`../GRADE_YOUR_WORK.md`](../GRADE_YOUR_WORK.md)** — per-phase Claude-graded scores with specific feedback

This is a portfolio piece. Put it on GitHub. Show it to interviewers when they ask "have you ever built an agent workforce."

## Already done Calder once? Try the skip-ahead path on Helix

If you've completed Calder full-path, do Helix via [`../SKIP_AHEAD.md`](../SKIP_AHEAD.md) — 15-hour path that loads weeks 1-2 from reference and does weeks 3-4 cold on a new domain. Tests build + handoff craft without re-doing discovery reps.
