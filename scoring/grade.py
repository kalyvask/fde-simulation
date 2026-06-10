"""CLI: grade an engagement artifact against the reference solution.

Usage:
    python -m scoring.grade <phase> <submission_path> [--case calder|helix] [--reference PATH] [-o OUTPUT.md]

Phases: phase1 (discovery), phase2 (wedge), phase3 (prototype), phase4 (field memo).

The script:
  1. Loads the rubric for the requested phase
  2. Reads the candidate's submission
  3. Reads the reference solution (auto-resolved from --case or explicit --reference)
  4. Calls Claude with the rubric system prompt + submission + reference
  5. Prints (or writes) a Markdown grade report; saves a JSON sidecar with the scores

Env vars:
  ANTHROPIC_API_KEY (required)
  SCORING_MODEL (optional, default: claude-opus-4-8)

Prompt caching: the rubric system prompt is cached so subsequent grades of the
same phase only pay tokens for the variable parts (the submission + reference).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .rubrics import RUBRICS, Rubric, build_system_prompt, list_phases

DEFAULT_MODEL = os.environ.get("SCORING_MODEL", "claude-opus-4-8")
REPO_ROOT = Path(__file__).resolve().parent.parent
ENGAGEMENT_DIR = REPO_ROOT / "simulations" / "1-full-engagement"

CASE_DIRS = {
    "calder": ENGAGEMENT_DIR / "calder-insurance",
    "helix": ENGAGEMENT_DIR / "helix-finance",
}


@dataclass
class GradeResult:
    markdown: str
    parsed_json: Optional[dict]
    raw_response: str

    @property
    def total(self) -> Optional[int]:
        if not self.parsed_json:
            return None
        return self.parsed_json.get("total")


def _resolve_reference(rubric: Rubric, case: Optional[str], explicit_ref: Optional[str]) -> Path:
    if explicit_ref:
        path = Path(explicit_ref).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"Reference not found: {path}")
        return path
    if not case:
        raise ValueError(
            "Either --case (calder|helix) or --reference PATH must be provided"
        )
    if case not in CASE_DIRS:
        raise ValueError(f"Unknown case '{case}'. Choices: {list(CASE_DIRS.keys())}")
    case_dir = CASE_DIRS[case]
    ref_path = case_dir / rubric.reference_filename
    if not ref_path.exists():
        raise FileNotFoundError(
            f"Reference solution not found at {ref_path}. "
            f"Check that the engagement repo is at {REPO_ROOT}."
        )
    return ref_path


def _read_artifact(path: Path) -> str:
    if path.is_dir():
        # For phase 3 (prototype), produce a synthesized representation of the
        # tree + selected key files so the grader has enough to grade.
        return _summarize_prototype_dir(path)
    return path.read_text(encoding="utf-8")


_KEY_PROTOTYPE_FILES = (
    "README.md",
    "SCAFFOLD_OVERVIEW.md",
    "requirements.txt",
    # Agent surface
    "calder_agent/workforce.py",
    "calder_agent/policy_library.py",
    "calder_agent/agents/base.py",
    "calder_agent/agents/compliance_critic.py",
    "calder_agent/agents/tone_supervisor.py",
    "calder_agent/agents/drafter.py",
    "helix_agent/workforce.py",
    "helix_agent/policy_library.py",
    "helix_agent/agents/base.py",
    "helix_agent/agents/citation_verifier.py",
    "helix_agent/agents/mnpi_scrubber.py",
    "helix_agent/agents/note_drafter.py",
    # Eval surface
    "evals/EVAL_OVERVIEW.md",
    "evals/harness.py",
    "evals/cases/seed.jsonl",
    "evals/cases/adversarial.jsonl",
)


def _summarize_prototype_dir(root: Path) -> str:
    """Produce a tree + selected key files dump for prototype grading."""
    lines: list[str] = []
    lines.append(f"# Prototype directory: {root}")
    lines.append("")
    lines.append("## Tree (top 4 levels, excluding caches and venvs)")
    lines.append("```")
    exclude_dirs = {"__pycache__", ".pytest_cache", ".venv", "node_modules", ".git"}
    for p in sorted(root.rglob("*")):
        if any(part in exclude_dirs for part in p.parts):
            continue
        rel = p.relative_to(root)
        depth = len(rel.parts)
        if depth > 4:
            continue
        indent = "  " * (depth - 1)
        label = rel.name + ("/" if p.is_dir() else "")
        lines.append(f"{indent}{label}")
    lines.append("```")
    lines.append("")
    lines.append("## Key files")
    lines.append("")
    for fname in _KEY_PROTOTYPE_FILES:
        candidate = root / fname
        if not candidate.exists():
            continue
        lines.append(f"### `{fname}`")
        lines.append("")
        text = candidate.read_text(encoding="utf-8", errors="replace")
        if len(text) > 16_000:
            text = text[:16_000] + "\n... (truncated; file is " + str(len(text)) + " bytes total)"
        ext = candidate.suffix.lstrip(".") or "txt"
        lines.append(f"```{ext}")
        lines.append(text)
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


def _extract_json_block(text: str) -> Optional[dict]:
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def grade(
    phase: str,
    submission_path: Path,
    case: Optional[str] = None,
    reference_path: Optional[Path] = None,
    model: str = DEFAULT_MODEL,
) -> GradeResult:
    if phase not in RUBRICS:
        raise ValueError(f"Unknown phase '{phase}'. Choices: {list_phases()}")
    rubric = RUBRICS[phase]

    if not submission_path.exists():
        raise FileNotFoundError(f"Submission not found: {submission_path}")
    submission_text = _read_artifact(submission_path)

    ref_path = (
        Path(reference_path).resolve()
        if reference_path
        else _resolve_reference(rubric, case, None)
    )
    reference_text = _read_artifact(ref_path)

    system_prompt = build_system_prompt(rubric)

    user_message = (
        f"## CANDIDATE SUBMISSION\n\n{submission_text}\n\n"
        f"---\n\n## REFERENCE SOLUTION\n\n{reference_text}\n\n"
        f"---\n\nGrade the candidate submission per the rubric in the system prompt. "
        f"Produce the Markdown table, the three bullets (BIGGEST_GAP, BEST_THING, ONE_FIX), "
        f"and the JSON block."
    )

    try:
        import anthropic
    except ImportError as e:
        raise RuntimeError(
            "Missing dependency: pip install anthropic. "
            "See scoring/README.md for setup."
        ) from e

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=4000,
        system=[
            {
                "type": "text",
                "text": system_prompt,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_message}],
    )

    body = "".join(block.text for block in response.content if block.type == "text")
    parsed = _extract_json_block(body)
    return GradeResult(markdown=body, parsed_json=parsed, raw_response=body)


def _format_report(result: GradeResult, rubric: Rubric, submission_path: Path, ref_path: Path) -> str:
    header = [
        f"# Grade — {rubric.artifact_label}",
        "",
        f"- Phase: `{rubric.phase}`",
        f"- Submission: `{submission_path}`",
        f"- Reference: `{ref_path}`",
        f"- Max score: {rubric.max_score}",
        "",
    ]
    if result.parsed_json and result.parsed_json.get("total") is not None:
        header.append(f"**Total**: {result.parsed_json['total']} / {rubric.max_score}")
        header.append("")
        header.append(
            "Calibration: subtract 1 per dimension to land at the interviewer-grade "
            f"score (so this report's {result.parsed_json['total']}/{rubric.max_score} reads "
            f"as roughly {max(0, result.parsed_json['total'] - len(rubric.dimensions))}/{rubric.max_score} "
            f"after the discipline adjustment)."
        )
        header.append("")
    header.append("---")
    header.append("")
    header.append(result.markdown)
    return "\n".join(header)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="scoring.grade",
        description="Grade an engagement artifact against the reference solution.",
    )
    parser.add_argument("phase", choices=list_phases(), help="Phase to grade.")
    parser.add_argument("submission", type=Path, help="Path to your submission file (or prototype directory for phase3).")
    parser.add_argument("--case", choices=list(CASE_DIRS.keys()), help="Case identifier; auto-resolves the reference solution.")
    parser.add_argument("--reference", type=Path, help="Explicit path to the reference solution (overrides --case).")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Anthropic model (default: {DEFAULT_MODEL}).")
    parser.add_argument("-o", "--output", type=Path, help="Write Markdown report to this file (default: stdout).")
    parser.add_argument("--json-output", type=Path, help="Write parsed JSON scores to this file.")
    args = parser.parse_args(argv)

    if "ANTHROPIC_API_KEY" not in os.environ:
        sys.stderr.write("error: ANTHROPIC_API_KEY environment variable is not set.\n")
        return 2

    try:
        result = grade(
            phase=args.phase,
            submission_path=args.submission.resolve(),
            case=args.case,
            reference_path=args.reference,
            model=args.model,
        )
    except (FileNotFoundError, ValueError) as e:
        sys.stderr.write(f"error: {e}\n")
        return 1

    rubric = RUBRICS[args.phase]
    ref_path = (
        Path(args.reference).resolve()
        if args.reference
        else _resolve_reference(rubric, args.case, None)
    )
    report = _format_report(result, rubric, args.submission.resolve(), ref_path)

    if args.output:
        args.output.write_text(report, encoding="utf-8")
        sys.stderr.write(f"wrote {args.output}\n")
    else:
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except AttributeError:
            pass
        sys.stdout.write(report + "\n")

    if args.json_output and result.parsed_json:
        args.json_output.write_text(
            json.dumps(result.parsed_json, indent=2), encoding="utf-8"
        )
        sys.stderr.write(f"wrote {args.json_output}\n")
    elif args.json_output and not result.parsed_json:
        sys.stderr.write(
            "warning: could not parse JSON block from grader response; "
            "no JSON sidecar written.\n"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
