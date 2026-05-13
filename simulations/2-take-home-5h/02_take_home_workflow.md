# Take-Home Workflow — 5-Hour Build Plan

> Hour-by-hour breakdown. Adjust if your build pace differs; the structure holds.

## Before you start (10 min)

- Block 5 contiguous hours (or 2 × 2.5h sessions max)
- Anthropic or OpenAI key configured
- Fresh repo or fork of existing scaffold (your call)
- Loom / QuickTime ready for the video at hour 5
- Paper or notes app for hour 1 thinking (resist opening the editor early)
- **Read `09_decision_principles.md` once before you start.** Seven portable principles transferred from the Sierra prep that apply directly to Helix. They are the difference between a competent build and a frontier-lab final-round defense.

## Hour 1 — Discovery + framing (NO CODE)

This is the hour most candidates skip. Don't. The interviewer can tell.

**What to do**:
1. Re-read the prompt. Highlight every constraint, every named stakeholder, every kill-criterion.
2. Draft your stakeholder map: champion / blocker / silent skeptic / user / tech / compliance.
3. Map the metric to the workflow stage. Where does the broken metric live?
4. Run the 4-source convergence test: Buyer / Brief / Industry / Operator — do all four point at the same stage?
5. **Score candidate wedges using the Outcome Risk Matrix** (see `09_decision_principles.md`, Principle 2). Draw the literal 2x2 — Value × Risk-of-irreversible-failure — and place 4-6 candidate wedges in it. The "Ship as v1" quadrant is your answer.
6. Apply **Principle 1: confidence of outcome over size of outcome**. If the matrix produces two candidates, the narrower one with higher outcome confidence wins. Write down why in one sentence.
7. Write the chosen wedge in one paragraph.
8. List 3-4 things the wedge does NOT do.
9. State the measurable "what working means" target — **but with two tracks**: Track A (output quality) and Track B (adoption/engagement). See `09_decision_principles.md`, Principle 4.

**Output**: a one-page handwritten / typed note that includes:
- The Outcome Risk Matrix (literal 2x2 with 4-6 wedges scored)
- The chosen wedge (one paragraph)
- 3-4 explicit exclusions
- Two metric tracks with targets

NO code yet.

**Common mistake**: opening the editor at minute 30. The interviewer asks "what did you choose to skip and why" — they want to hear you skipped scope, not discipline. The matrix is the artifact that proves you scoped on principles, not vibes.

## Hour 2 — Architecture sketch + eval seed (LOW CODE)

**What to do**:
1. Draw the agent architecture diagram (paper / Mermaid / Excalidraw). 5-8 specialized agents.
2. For each agent: name, job, model tier (Haiku / Sonnet / GPT-4o-mini / GPT-4o), deterministic-or-LLM, why.
3. Identify the integration surface: which systems, what permissions, what's read-only.
4. Draft the "what good looks like" measurable definitions (table: metric / target / baseline / owner).
5. Hand-write 5-7 seed eval cases. Don't put them in code yet. Just the case_id + expected behavior.
6. Identify the top 3-5 risks and their mitigation owners.

**Output**: architecture diagram + one-page table of agents + eval seed cases + risk register.

**Common mistake**: jumping into Python before knowing what the agents are. Spend 5 minutes on a whiteboard; save 90 minutes of refactoring.

## Hour 3-4 — Build the prototype (HEAVY CODE)

**What to do**:

You have two paths:

### Path A: Fork the existing scaffold
- Open `helix/week-2-solution/prototype/`
- Copy to a new repo (`my-helix-attempt/`)
- Adapt the agents to YOUR architecture (you may have chosen 6 agents vs the existing 7, or different decomposition)
- Wire up enough that one synthetic case runs end-to-end
- Time saved: ~1h on Python scaffolding. Time spent: actually thinking through architecture choices.

### Path B: Build cold
- New Python project
- requirements.txt: anthropic / openai / pydantic / python-dotenv / pytest
- 5-8 agent files, base class, workforce orchestrator, trace data model
- Synthetic data generator with 3-5 fake earnings calls
- End-to-end script that processes one call through all agents

**Output**: a working agent that processes one synthetic earnings call end-to-end and produces a draft + audit trace.

**Time check**: 30 minutes before end of hour 4, stop adding features. Move to eval + polish.

**Common mistake**: trying to build the full v2 architecture in 4 hours. Senior FDE move: ship the smallest credible thing that demonstrates the patterns. The interviewer will ask about the missing pieces; saying "I scoped this out of v1 because X" is the right answer.

## Hour 5 — Evals + deck + video

**Time budget within hour 5**:

| Minutes | Task |
|---|---|
| 0-15 | Code your 5-7 seed eval cases. Add 3 adversarial cases (one from each major risk). |
| 15-25 | Run the eval. Note the pass rate. Note 1-2 cases that fail (yes, even with real Claude they often do — diagnostic, not failure). |
| 25-50 | Build the 4-slide deck (see `04_deck_template.md`). Use a template; don't design pixels. |
| 50-65 | Record the 5-min video walkthrough (see `05_video_walkthrough_guide.md`). First take. Don't re-record. |

**Output**: repo + deck + video + eval results, ready to ship per `03_submission_spec.md`.

**Common mistake**: spending 60 minutes polishing the deck. The interviewer cares about content, not formatting.

## Time-tracking discipline

At the end of each hour, write down what you actually did. The interviewer may ask "what did you spend the first hour on?" — your honest answer is more impressive than a fabricated one.

## What if you finish early?

You probably didn't finish. Use the extra time on:
1. Adversarial eval cases (more is better)
2. The interviewer's likely pushback questions — pre-draft your defenses
3. One specific risk with a deeper mitigation (e.g., the MNPI scrubber design)

Do **not** use extra time on:
- Polishing the deck (diminishing returns)
- Adding a new agent you can't defend (more surface area for pushback)
- Re-recording the video (first take is fine)

## What if you run out of time?

Common. The 5-hour budget is intentionally tight.

**Skip in this order** if you have to:
1. Adversarial cases beyond 3 → ship with seed only
2. The video walkthrough → ship with deck + repo + a short written explanation
3. A non-critical agent → wire it as a stub; explain in the deck
4. Polish on the deck → use a single-color template

**Never skip**:
- The eval suite (skipping evals = automatic rubric downgrade)
- The audit trace (every cited number must trace to a source)
- The compliance critic (this is Sarah's kill-criteria)
- The video framing of the wedge (the architecture diagram in the deck IS the wedge for the interviewer)

## At hour 5, submit

Per `03_submission_spec.md`. Don't keep iterating. The longer you tweak past 5h, the more you signal lack of discipline. Ship and rest.
