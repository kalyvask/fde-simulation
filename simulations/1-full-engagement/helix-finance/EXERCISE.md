# Helix Capital — How to Run This Simulation

> A 2-week guided FDE engagement on the Helix Capital case (hedge fund earnings-note automation). Different domain from Calder, same FDE skill. You do the work; the reference solutions show what good looks like AFTER you've attempted each phase.

## Before you start

1. Read `00_brief.md` — the customer prompt
2. Allocate ~20 hours over 2 weeks (or compressed sprint)
3. Set up a fresh repo for your work
4. Have an Anthropic or OpenAI API key configured (for the build phase)

## The 2-week structure

| Week | Folder | Your time |
|---|---|---|
| 1 | `01_week1_discovery/` | 6-8 hours |
| 2 | `02_week2_solution/` (includes build + eval) | 10-14 hours |

The Helix engagement is faster than Calder because the customer brief is more constrained (4-week demo target; one specific workflow).

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

## At the end of 2 weeks

You should have:
- A working earnings-note agent prototype on synthetic data
- 30-50 case weighted eval suite with pass^k=5 results
- 4-slide deck defending the architecture
- 1-page discovery memo
- Working knowledge of citation grounding + MNPI scrubbing + LLM-as-judge calibration

This is the same skill set the 5-hour take-home (sim 2) tests under time pressure. Doing the full engagement first builds the muscle memory; doing the 5-hour version next tests whether you can execute under a clock.

## Why two cases (Calder + Helix)?

Running both cases sequentially tests **domain portability** — a real FDE skill. The frameworks (3-lens, Outcome Risk Matrix, agent shapes, workflow decomposition) are the same in insurance and finance. The specific stakeholders, kill-criteria, and integration risks differ. If you can produce defensible work in both domains, that's a strong signal.

The senior FDE move: do Helix second after Calder. By Helix you should be deploying frameworks in your sleep and spending your time on the case specifics, not on framework selection.
