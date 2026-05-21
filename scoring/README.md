# scoring — verifiable grades + artifact bundling

> Two CLIs that turn "I ran the simulation" into "I scored 82/87 on Calder, and here's the bundle the interviewer can read in 10 minutes."

## Install

```bash
pip install -r scoring/requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...      # required for grading; not needed for bundling
```

Optional: pin a non-default model via `SCORING_MODEL=claude-opus-4-7` (the default). For grading, capability beats speed; Opus is the right call.

## scoring.grade — grade one engagement phase

Grades a candidate artifact against the reference solution in the case folder using a structured rubric (5 dimensions x 0-3, totaled out of 15; phase 4 is 4 dimensions x 0-3 out of 12). The rubric system prompt is cached via `cache_control: ephemeral`, so re-grading the same phase across iterations is cheap.

```bash
# Phase 1 — discovery memo (Calder reference)
python -m scoring.grade phase1 path/to/my_discovery_memo.md --case calder \
    -o grades/phase1.md --json-output grades/phase1.json

# Phase 2 — wedge proposal (Helix reference)
python -m scoring.grade phase2 path/to/my_wedge_proposal.md --case helix \
    -o grades/phase2.md --json-output grades/phase2.json

# Phase 3 — prototype + eval suite (point at your prototype dir)
python -m scoring.grade phase3 path/to/my_prototype/ --case calder \
    -o grades/phase3.md --json-output grades/phase3.json

# Phase 4 — field memo
python -m scoring.grade phase4 path/to/my_field_memo.md --case helix \
    -o grades/phase4.md --json-output grades/phase4.json
```

Output (Markdown report):

```
# Grade — Discovery memo
- Phase: `phase1`
- Submission: `/path/to/my_discovery_memo.md`
- Reference: `/path/to/calder-insurance/01_week1_discovery/discovery_memo.md`
- Max score: 15

**Total**: 11 / 15

Calibration: subtract 1 per dimension to land at the interviewer-grade score
(so this report's 11/15 reads as roughly 6/15 after the discipline adjustment).

---

| Dimension | Score | What worked | What was missing |
|---|---|---|---|
| Stakeholder mapping | 3/3 | Names 8 stakeholders by archetype with how-to-engage notes | — |
| Information needed | 2/3 | Organized by source | Missing external benchmarks (NHTSA, Kaggle) |
| 4-source convergence | 2/3 | Buyer, Brief, Operator named | Industry source absent |
| Wedge hypothesis | 3/3 | FNOL acknowledgment + first-status; coverage explicitly out | — |
| Discipline and quality | 1/3 | Some quoted stakeholder language | No tradeoffs named; deliverables unflagged |
| **TOTAL** | **11/15** | | |

- BIGGEST_GAP: Industry-source triangulation is missing — peer-insurer benchmarks would have surfaced the 30-min comms SLA pattern.
- BEST_THING: The stakeholder map names archetype emotional state (Marcus = career-risk default-no), which the reference does only implicitly.
- ONE_FIX: Add a 2-paragraph "industry source" section using NAIC market-conduct trend data and one peer-insurer benchmark before moving to Phase 2.
```

The JSON sidecar (`grades/phase1.json`) is the parseable structured output:

```json
{
  "phase": "phase1",
  "artifact": "Discovery memo",
  "max_score": 15,
  "scores": {
    "Stakeholder mapping": {"score": 3, "what_worked": "...", "what_was_missing": "..."},
    "...": {}
  },
  "total": 11,
  "biggest_gap": "...",
  "best_thing": "...",
  "one_fix": "..."
}
```

### What this gives you that GRADE_YOUR_WORK.md doesn't

| GRADE_YOUR_WORK.md (legacy) | scoring.grade (this) |
|---|---|
| Manual copy-paste of submission + reference into a chat | One CLI command |
| Free-text response, no parseable scores | JSON sidecar with per-dimension scores |
| Can't aggregate across phases | Aggregate via scoring.bundle --include-grades |
| Same prompt every time pays full tokens | Prompt-cached rubric; per-grade tokens drop ~80% after first call |
| No diff against the reference | Reference is loaded automatically per `--case` |

GRADE_YOUR_WORK.md is still useful for one-off conversational grading. `scoring.grade` is what you use during iteration when you want the score to mean something across attempts.

## scoring.bundle — package the portfolio

Walks a portfolio directory and emits a single Markdown file with sections for each engagement artifact, the prototype tree + key files, optional eval output, and an optional grade-report summary.

```bash
# Minimal: just the artifacts
python -m scoring.bundle ~/my-fde-portfolio/calder/ -o calder_bundle.md

# Full bundle: artifacts + captured eval output + grade summary
cd ~/my-fde-portfolio/calder/3-build
python scripts/run_eval.py > /tmp/eval_output.txt

cd ~
python -m scoring.bundle ~/my-fde-portfolio/calder/ \
    --include-eval-output /tmp/eval_output.txt \
    --include-grades ~/my-fde-portfolio/calder/grades/ \
    -o calder_bundle.md
```

### What goes in the bundle

The bundler looks for these section files (in order of preference per section):

| Section | Filename candidates (first found wins) |
|---|---|
| Discovery memo | `1-discovery.md`, `discovery_memo.md`, `case-study/1-discovery.md`, `01_week1_discovery/discovery_memo.md` |
| Stakeholder map | `stakeholder_map.md`, `case-study/stakeholder_map.md`, `01_week1_discovery/stakeholder_map.md` |
| Wedge proposal | `2-wedge-proposal.md`, `wedge_proposal.md`, ... |
| Build plan | `wedge_build_plan.md`, ... |
| Prototype overview | `3-build/README.md`, ... |
| Eval results | `4-results.md`, `results.md`, `eval_results.md` |
| Field memo | `5-field-memo.md`, `field_memo.md`, ... |
| Retrospective | `retrospective.md`, `RETRO.md` |
| Frameworks applied | `frameworks-applied.md`, `frameworks_applied.md` |

Plus a prototype tree + inlined key agent files (workforce, base agent, key critics, eval harness), so the reader can assess the architecture without cloning the repo.

The output is a single Markdown file suitable for attaching to a take-home submission or sharing as a public portfolio artifact.

## End-to-end flow

```bash
# 1. Do the engagement; produce your artifacts in ~/my-fde-portfolio/calder/
# 2. Grade each phase
python -m scoring.grade phase1 ~/my-fde-portfolio/calder/case-study/1-discovery.md \
    --case calder --json-output ~/my-fde-portfolio/calder/grades/phase1.json
# (repeat for phase2, phase3, phase4)

# 3. Bundle everything
python -m scoring.bundle ~/my-fde-portfolio/calder/ \
    --include-grades ~/my-fde-portfolio/calder/grades/ \
    -o calder_submission_bundle.md

# 4. Attach calder_submission_bundle.md to your take-home submission
```

## When NOT to use scoring.grade

- Before you've drafted your own artifact. The grader compares against the reference; if you've copied the reference, the grade is meaningless.
- For the very first iteration if you don't want a numeric anchor yet. Sometimes the right move is to do a qualitative self-read first, fix one obvious gap, then run the grader.
- For phases that aren't covered by the rubric (e.g., the 60-min recommendation; the client simulation). Those are scored via different mechanisms (the recommendation has a playbook; the client simulation has its own grading rubric in sim 4).

## Cost notes

Per grade run with `claude-opus-4-7` and the cached system prompt: roughly 0.10 USD on a typical phase-1 grade with a 5KB submission + 5KB reference. Subsequent grades of the same phase drop to ~0.04 USD because the rubric prompt is cached.

You can drop to `claude-sonnet-4-6` via `SCORING_MODEL=claude-sonnet-4-6` for ~5x cheaper at the cost of some grader calibration. Opus is recommended for grading; sonnet is fine for iteration.

## Programmatic use

The scoring module is importable:

```python
from scoring.grade import grade
from pathlib import Path

result = grade(
    phase="phase1",
    submission_path=Path("my_discovery.md"),
    case="calder",
)
print(result.total)              # 11
print(result.parsed_json)        # full structured scores
```
