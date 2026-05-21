"""CLI: walk a portfolio directory and emit a single submittable Markdown pack.

Usage:
    python -m scoring.bundle <portfolio_dir> [-o bundle.md] [--include-eval-output PATH] [--include-grades DIR]

Produces a single Markdown file with sections for each engagement artifact
(discovery memo, wedge proposal, build plan, prototype tree + key files,
eval results, field memo, retrospective). Optionally appends any grade JSON
reports produced by scoring.grade.

Designed so the candidate can attach the bundle to a take-home submission or
share as a portfolio sample without sending a tar of the full directory.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

# Each section: (label, list of candidate filenames or globs in order of preference)
SECTIONS = [
    ("Discovery memo", ["1-discovery.md", "discovery_memo.md", "case-study/1-discovery.md", "01_week1_discovery/discovery_memo.md"]),
    ("Stakeholder map", ["stakeholder_map.md", "case-study/stakeholder_map.md", "01_week1_discovery/stakeholder_map.md"]),
    ("Wedge proposal", ["2-wedge-proposal.md", "wedge_proposal.md", "case-study/2-wedge-proposal.md", "02_week2_solution/wedge_proposal.md"]),
    ("Build plan", ["wedge_build_plan.md", "case-study/build_plan.md", "02_week2_solution/wedge_build_plan.md"]),
    ("Prototype overview", ["3-build/README.md", "case-study/3-build/README.md", "02_week2_solution/prototype/README.md"]),
    ("Eval results", ["4-results.md", "case-study/4-results.md", "results.md", "eval_results.md"]),
    ("Field memo", ["5-field-memo.md", "field_memo.md", "case-study/5-field-memo.md", "04_week4_handoff/field_memo.md"]),
    ("Retrospective", ["retrospective.md", "RETRO.md"]),
    ("Frameworks applied", ["frameworks-applied.md", "frameworks_applied.md"]),
]

# Key prototype files to inline (relative to the prototype root)
KEY_PROTOTYPE_FILES = (
    "README.md",
    "requirements.txt",
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
    "evals/EVAL_OVERVIEW.md",
    "evals/harness.py",
)


@dataclass
class FoundFile:
    label: str
    path: Path


def _resolve_section(root: Path, candidates: Iterable[str]) -> Optional[Path]:
    for rel in candidates:
        candidate = root / rel
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def _find_prototype_dir(root: Path) -> Optional[Path]:
    """Find the prototype directory: look for a workforce.py somewhere below root."""
    for path in sorted(root.rglob("workforce.py")):
        # Prototype root is the dir containing the *agent package, i.e., 2 levels up
        # from workforce.py if it sits inside <case>_agent/workforce.py
        if path.parent.name.endswith("_agent"):
            return path.parent.parent
    # Fallback: any directory named "prototype"
    for path in sorted(root.rglob("prototype")):
        if path.is_dir():
            return path
    return None


def _render_tree(root: Path, max_depth: int = 4) -> str:
    exclude = {"__pycache__", ".pytest_cache", ".venv", "node_modules", ".git"}
    lines = ["```", str(root.name) + "/"]
    for p in sorted(root.rglob("*")):
        if any(part in exclude for part in p.parts):
            continue
        rel = p.relative_to(root)
        depth = len(rel.parts)
        if depth > max_depth:
            continue
        indent = "  " * depth
        label = rel.name + ("/" if p.is_dir() else "")
        lines.append(f"{indent}{label}")
    lines.append("```")
    return "\n".join(lines)


def _render_file(path: Path, *, max_bytes: int = 16_000, prefix: str = "") -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return f"_(could not read {path}: {e})_"
    truncated = ""
    if len(text) > max_bytes:
        text = text[:max_bytes]
        truncated = f"\n\n_(truncated at {max_bytes} bytes; full file is {path.stat().st_size} bytes)_"
    ext = path.suffix.lstrip(".") or "txt"
    return f"{prefix}```{ext}\n{text}\n```{truncated}"


def _render_grades(grade_dir: Path) -> str:
    """Read JSON sidecars produced by scoring.grade and render a summary table."""
    rows = []
    for jpath in sorted(grade_dir.glob("*.json")):
        try:
            data = json.loads(jpath.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        rows.append(
            (
                data.get("phase", jpath.stem),
                data.get("artifact", "?"),
                data.get("total"),
                data.get("max_score"),
                data.get("biggest_gap", ""),
            )
        )
    if not rows:
        return "_(no grade JSON files found in this directory)_"
    out = [
        "| Phase | Artifact | Score | Biggest gap |",
        "|---|---|---|---|",
    ]
    for phase, artifact, total, max_score, gap in rows:
        score_str = f"{total} / {max_score}" if total is not None else "?"
        out.append(f"| {phase} | {artifact} | {score_str} | {gap} |")
    return "\n".join(out)


def bundle_portfolio(
    root: Path,
    output: Optional[Path] = None,
    eval_output_file: Optional[Path] = None,
    grade_dir: Optional[Path] = None,
) -> str:
    root = root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(f"Portfolio root must be a directory: {root}")

    title = root.name.replace("-", " ").replace("_", " ").title()
    lines: list[str] = [
        f"# Engagement Bundle — {title}",
        "",
        f"_Generated from `{root}` by `scoring.bundle`._",
        "",
        "## Table of contents",
        "",
    ]
    sections_found: list[FoundFile] = []
    for label, candidates in SECTIONS:
        found = _resolve_section(root, candidates)
        if found:
            sections_found.append(FoundFile(label=label, path=found))
            anchor = label.lower().replace(" ", "-")
            lines.append(f"- [{label}](#{anchor})")
    prototype_dir = _find_prototype_dir(root)
    if prototype_dir:
        lines.append("- [Prototype](#prototype)")
    if eval_output_file:
        lines.append("- [Eval run output](#eval-run-output)")
    if grade_dir:
        lines.append("- [Grade reports](#grade-reports)")
    lines.append("")
    lines.append("---")
    lines.append("")

    for sec in sections_found:
        lines.append(f"## {sec.label}")
        lines.append("")
        lines.append(f"_Source: `{sec.path.relative_to(root)}`_")
        lines.append("")
        lines.append(sec.path.read_text(encoding="utf-8", errors="replace"))
        lines.append("")
        lines.append("---")
        lines.append("")

    if prototype_dir:
        lines.append("## Prototype")
        lines.append("")
        lines.append(f"_Prototype root: `{prototype_dir.relative_to(root)}`_")
        lines.append("")
        lines.append("### Tree")
        lines.append("")
        lines.append(_render_tree(prototype_dir))
        lines.append("")
        lines.append("### Key files")
        lines.append("")
        for fname in KEY_PROTOTYPE_FILES:
            p = prototype_dir / fname
            if p.exists():
                lines.append(f"#### `{fname}`")
                lines.append("")
                lines.append(_render_file(p))
                lines.append("")
        lines.append("---")
        lines.append("")

    if eval_output_file:
        lines.append("## Eval run output")
        lines.append("")
        if eval_output_file.exists():
            lines.append(f"_Captured from: `{eval_output_file}`_")
            lines.append("")
            lines.append("```")
            lines.append(eval_output_file.read_text(encoding="utf-8", errors="replace"))
            lines.append("```")
        else:
            lines.append(f"_(eval output file not found: {eval_output_file})_")
        lines.append("")
        lines.append("---")
        lines.append("")

    if grade_dir:
        lines.append("## Grade reports")
        lines.append("")
        lines.append(_render_grades(grade_dir))
        lines.append("")

    bundle_text = "\n".join(lines)
    if output:
        output.write_text(bundle_text, encoding="utf-8")
    return bundle_text


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="scoring.bundle",
        description="Walk a portfolio directory and emit a single submittable Markdown pack.",
    )
    parser.add_argument("portfolio", type=Path, help="Path to your portfolio directory.")
    parser.add_argument("-o", "--output", type=Path, help="Write to this file (default: stdout).")
    parser.add_argument(
        "--include-eval-output",
        type=Path,
        help="Append the contents of this file as the eval run output (e.g., the captured stdout of `python scripts/run_eval.py`).",
    )
    parser.add_argument(
        "--include-grades",
        type=Path,
        help="Directory containing JSON sidecars from `scoring.grade --json-output`; appends a grade summary table.",
    )
    args = parser.parse_args(argv)

    try:
        text = bundle_portfolio(
            root=args.portfolio,
            output=args.output,
            eval_output_file=args.include_eval_output,
            grade_dir=args.include_grades,
        )
    except NotADirectoryError as e:
        sys.stderr.write(f"error: {e}\n")
        return 1

    if args.output:
        sys.stderr.write(f"wrote {args.output} ({len(text):,} bytes)\n")
    else:
        # Windows consoles default to cp1252; the bundle contains Unicode arrows
        # and box-drawing characters that crash that codec. Force utf-8 on stdout.
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except AttributeError:
            pass
        sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
