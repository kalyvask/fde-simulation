"""Machine-readable rubric definitions for the engagement scoring system.

Each phase has a 5-dimension rubric (4 for phase 4) scored 0-3 per dimension.
The rubric prompts mirror simulations/1-full-engagement/GRADE_YOUR_WORK.md but
are structured so the grader returns parseable JSON alongside the Markdown
report.

The rubrics are case-agnostic; the per-case reference solutions live in each
case folder and are passed in at grade time.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Dimension:
    name: str
    description: str
    anchors: dict[int, str]  # 0..3 -> anchor text


@dataclass(frozen=True)
class Rubric:
    phase: str
    artifact_label: str
    max_score: int
    dimensions: list[Dimension]
    reference_filename: Optional[str]  # path under case folder; may be a glob
    grader_role: str  # used in the system prompt


_DISCOVERY_DIMENSIONS = [
    Dimension(
        name="Stakeholder mapping",
        description="Stakeholders identified by archetype (buyer, champion, operator, blocker, silent skeptic), with how-to-engage notes.",
        anchors={
            0: "Generic list of titles, no archetypes.",
            1: "Names individuals but not archetypes.",
            2: "Names individuals + archetypes for most stakeholders.",
            3: "All 7-8 archetypes covered including the silent skeptic, each with a how-to-engage note.",
        },
    ),
    Dimension(
        name="Information needed",
        description="Discovery data needed, organized by source (people / data / process / external).",
        anchors={
            0: "Generic 'we'd talk to stakeholders'.",
            1: "Lists data needed but not by source.",
            2: "Organized by source (people / data / process / external).",
            3: "Specific data items + specific interview questions + specific external benchmarks.",
        },
    ),
    Dimension(
        name="4-source convergence",
        description="Triangulation across Buyer / Brief / Industry / Operator with a convergence point identified.",
        anchors={
            0: "Not mentioned.",
            1: "Mentioned but not applied.",
            2: "Applied with 2-3 sources named.",
            3: "All 4 sources named (Buyer / Brief / Industry / Operator) with convergence point identified.",
        },
    ),
    Dimension(
        name="Wedge hypothesis",
        description="Specific wedge with scope boundary and kill-criteria-aligned justification.",
        anchors={
            0: "No wedge proposed.",
            1: "Generic wedge (e.g., 'automate the workflow').",
            2: "Specific wedge with scope boundary.",
            3: "Specific wedge + explicit out-of-scope items + justification on the kill-criteria.",
        },
    ),
    Dimension(
        name="Discipline and quality",
        description="Concrete specifics, quoted stakeholder language, named tradeoffs, week-3 deliverables flagged.",
        anchors={
            0: "Generic, no specifics.",
            1: "Some specifics but inconsistent.",
            2: "Concrete specifics throughout.",
            3: "Quoted stakeholder language, named tradeoffs, week-3 deliverables flagged.",
        },
    ),
]

_WEDGE_DIMENSIONS = [
    Dimension(
        name="Wedge framing",
        description="Wedge defended on Outcome Risk Matrix + 3-lens scaffold + explicit out-of-scope.",
        anchors={
            0: "No wedge or generic.",
            1: "Wedge named, no defense.",
            2: "Wedge defended with 'confidence over size' or similar principle.",
            3: "Wedge defended on Outcome Risk Matrix + 3-lens scaffold + explicit out-of-scope.",
        },
    ),
    Dimension(
        name="3-lens scaffold",
        description="Customer / Product / Technical columns all filled with emotional state, out-of-scope = in-scope, metric tension, one specific risk.",
        anchors={
            0: "Not used.",
            1: "Customer column only.",
            2: "Customer + Product columns.",
            3: "All 3 columns filled with emotional state, out-of-scope = in-scope, metric tension, one specific risk.",
        },
    ),
    Dimension(
        name="Architecture",
        description="Agent shapes from catalog + workflow decomposition method + orchestration pattern + integration patterns.",
        anchors={
            0: "Single mega-prompt or no architecture.",
            1: "5-8 agents named, no defense.",
            2: "5-8 agents + tier choices + det/LLM split, mostly defended.",
            3: "Agent shapes (Extractor / Classifier / Synthesizer / Critic / Compliance critic / Router / Auditor) + workflow decomposition method + orchestration pattern + read/write integration patterns.",
        },
    ),
    Dimension(
        name="Production thinking",
        description="Eval suite weighted by failure cost + pass^k=5 + observability + immutable audit trace + sign-off criteria with owners.",
        anchors={
            0: "Demo-only, no eval, no observability.",
            1: "Eval mentioned but no specifics.",
            2: "Eval + pass^k=5 + adversarial set.",
            3: "Eval suite weighted by failure cost + pass^k=5 + production observability + immutable audit trace + 3 sign-off criteria with named owners.",
        },
    ),
    Dimension(
        name="Risk surfacing",
        description="Risks organized in Business / UX / Technical buckets with detection signals and named owners per risk.",
        anchors={
            0: "'We'll handle risks.'",
            1: "3-4 risks named.",
            2: "5-7 risks with mitigations.",
            3: "Risks organized in Business / UX / Technical buckets with detection signals and named owners per risk.",
        },
    ),
]

_PROTOTYPE_DIMENSIONS = [
    Dimension(
        name="Architecture fidelity",
        description="Agents map to shapes, each with one job, deterministic gates around dangerous calls.",
        anchors={
            0: "Single mega-prompt with no agent boundaries.",
            1: "Multiple agents but no separation of concerns.",
            2: "5-8 specialized agents with proper boundaries.",
            3: "Agents map to shapes; each has ONE job; deterministic gates around dangerous calls.",
        },
    ),
    Dimension(
        name="Hybrid det+LLM discipline",
        description="Deterministic where reliability is non-negotiable; LLM where creativity is value; LLM-as-judge for soft errors.",
        anchors={
            0: "Everything LLM.",
            1: "Some deterministic but inconsistent.",
            2: "Critic / compliance work is deterministic; synthesis is LLM.",
            3: "Deterministic where reliability is non-negotiable (citation verify, MNPI scrub, audit); LLM where creativity is value (drafting); LLM-as-judge for soft errors.",
        },
    ),
    Dimension(
        name="Eval suite",
        description="20+ cases weighted by failure cost; pass^k=5 with variance ≤5%; per-major-risk adversarial; observability plan documented.",
        anchors={
            0: "No evals or trivial happy-path only.",
            1: "Has evals but no weighting.",
            2: "Weighted by failure cost; happy + adversarial.",
            3: "20+ cases weighted by failure cost; pass^k=5 with variance ≤5%; per-major-risk adversarial case; production observability plan documented.",
        },
    ),
    Dimension(
        name="Audit trace + observability",
        description="Immutable trace + drift detection + per-agent latency/cost + weekly review cadence with named owner.",
        anchors={
            0: "No trace, no observability.",
            1: "Per-request log but not examiner-readable.",
            2: "Examiner-readable trace per request.",
            3: "Immutable trace + 7-day rolling drift detection + per-agent latency/cost tracking + weekly review cadence with named operational owner.",
        },
    ),
    Dimension(
        name="Read-only discipline",
        description="Read-only v1 + 3-tier integration ladder with named gates.",
        anchors={
            0: "Agents write to external systems in v1.",
            1: "Writes are gated by approval but still in v1.",
            2: "Read-only v1 with holding queue.",
            3: "Read-only v1 + 3-tier integration ladder (read-only, approval-gated, autonomous) + each tier has named gate.",
        },
    ),
]

_FIELD_MEMO_DIMENSIONS = [
    Dimension(
        name="Field-back-to-product feedback",
        description="Specific lab-relevant feedback items + the customer context that motivated each.",
        anchors={
            0: "No specific feedback to lab Research / Product.",
            1: "Generic feedback (e.g., 'LLMs should be better').",
            2: "Specific lab-relevant feedback (eval primitives, immutable snapshots, etc.).",
            3: "3-5 specific lab feedback items + the customer context that motivated each.",
        },
    ),
    Dimension(
        name="Production gates",
        description="Sign-off criteria + rollback procedure + drift detection plan + named operational owner.",
        anchors={
            0: "No named gates.",
            1: "Pass^k mentioned.",
            2: "3 sign-off criteria with stakeholder owners.",
            3: "3 sign-off criteria + rollback procedure + drift detection plan + 90-day operational owner.",
        },
    ),
    Dimension(
        name="Risks remaining",
        description="Bucketed risks with detection signals + named owners + go-no-go criteria.",
        anchors={
            0: "'We're good.'",
            1: "Generic remaining risks.",
            2: "Specific remaining risks bucketed (Business / UX / Technical).",
            3: "Bucketed risks with detection signals + named owners + go-no-go criteria for each.",
        },
    ),
    Dimension(
        name="Handoff documentation",
        description="Named operational owner + weekly cadence + escalation runbook + audit-trace standard + customer-side ownership confirmation.",
        anchors={
            0: "No handoff plan.",
            1: "Generic handoff plan.",
            2: "Named operational owner + weekly cadence.",
            3: "Named owner + weekly cadence + escalation runbook + audit-trace standard + customer-side ownership confirmation.",
        },
    ),
]


RUBRICS: dict[str, Rubric] = {
    "phase1": Rubric(
        phase="phase1",
        artifact_label="Discovery memo",
        max_score=15,
        dimensions=_DISCOVERY_DIMENSIONS,
        reference_filename="01_week1_discovery/discovery_memo.md",
        grader_role="a senior Forward Deployed Engineer grading a candidate's Week 1 discovery memo against the reference solution",
    ),
    "phase2": Rubric(
        phase="phase2",
        artifact_label="Wedge proposal",
        max_score=15,
        dimensions=_WEDGE_DIMENSIONS,
        reference_filename="02_week2_solution/wedge_proposal.md",
        grader_role="a senior Forward Deployed Engineer grading a candidate's Week 2 wedge proposal + build plan against the reference",
    ),
    "phase3": Rubric(
        phase="phase3",
        artifact_label="Prototype + eval suite",
        max_score=15,
        dimensions=_PROTOTYPE_DIMENSIONS,
        reference_filename="02_week2_solution/prototype/",
        grader_role="a senior Forward Deployed Engineer grading a candidate's Week 3 prototype + eval suite against the reference",
    ),
    "phase4": Rubric(
        phase="phase4",
        artifact_label="Field memo",
        max_score=12,
        dimensions=_FIELD_MEMO_DIMENSIONS,
        reference_filename="04_week4_handoff/field_memo.md",
        grader_role="a senior Forward Deployed Engineer grading a candidate's Week 4 field memo against the reference",
    ),
}


def build_system_prompt(rubric: Rubric) -> str:
    """Compose the grader system prompt from the rubric definition."""
    lines = [
        f"You are {rubric.grader_role}.",
        "",
        f"Grade the candidate's {rubric.artifact_label.lower()} against the reference solution provided.",
        f"Use {len(rubric.dimensions)} dimensions, 0-3 per dimension, max {rubric.max_score}.",
        "",
        "GRADING DIMENSIONS:",
        "",
    ]
    for i, dim in enumerate(rubric.dimensions, 1):
        lines.append(f"{i}. {dim.name} (0-3)")
        lines.append(f"   What it tests: {dim.description}")
        for score, anchor in sorted(dim.anchors.items()):
            lines.append(f"   - {score}: {anchor}")
        lines.append("")
    lines.extend(
        [
            "OUTPUT FORMAT — produce both a Markdown table and a JSON block.",
            "",
            "First the Markdown table:",
            "",
            "| Dimension | Score | What worked | What was missing |",
            "|---|---|---|---|",
            *[
                f"| {dim.name} | X/3 | ... | ... |"
                for dim in rubric.dimensions
            ],
            f"| **TOTAL** | **X/{rubric.max_score}** | | |",
            "",
            "Then three bullets:",
            "- BIGGEST_GAP: the single biggest gap between the submission and the reference",
            "- BEST_THING: the single best thing the submission does that the reference doesn't",
            "- ONE_FIX: the one thing to fix before the next phase",
            "",
            "Then a JSON block (parseable, fenced as ```json):",
            "",
            "```json",
            "{",
            f'  "phase": "{rubric.phase}",',
            f'  "artifact": "{rubric.artifact_label}",',
            f'  "max_score": {rubric.max_score},',
            '  "scores": {',
            *[
                f'    "{dim.name}": {{"score": <0-3>, "what_worked": "<one sentence>", "what_was_missing": "<one sentence>"}}'
                + ("," if i < len(rubric.dimensions) - 1 else "")
                for i, dim in enumerate(rubric.dimensions)
            ],
            "  },",
            '  "total": <integer 0-' + str(rubric.max_score) + ">,",
            '  "biggest_gap": "<one sentence>",',
            '  "best_thing": "<one sentence>",',
            '  "one_fix": "<one sentence>"',
            "}",
            "```",
            "",
            "DISCIPLINE: graders are typically too generous. When in doubt between two adjacent",
            "scores, pick the lower one. The candidate's calibration rule is to subtract 1 per",
            "dimension from your score; do not do that subtraction yourself.",
            "",
            "Quote actual text from the submission where possible. If the submission is missing",
            "something the reference has, name it specifically.",
        ]
    )
    return "\n".join(lines)


def list_phases() -> list[str]:
    return list(RUBRICS.keys())
