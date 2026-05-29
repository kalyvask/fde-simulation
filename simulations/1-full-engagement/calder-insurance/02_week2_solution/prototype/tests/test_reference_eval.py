"""Regression guard: the reference workforce must pass its own eval suite.

Runs the seed + adversarial suites through the workforce in mock mode and
asserts that every non-`requires_llm` case passes pass^k with zero flakiness.
This locks the shipped reference as a baseline — if a refactor breaks the
policy library or routing, this fails loudly instead of the eval suite
silently rotting.

Mock mode is deterministic, so k=2 is enough to exercise the pass^k plumbing
without paying for repeated identical runs. Cases marked `requires_llm` are
skipped here; the real-key CI job is what exercises them.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from calder_agent.workforce import Workforce
from evals.harness import load_cases, run_eval, summarize

PROTOTYPE_ROOT = Path(__file__).parent.parent
CASE_FILES = [
    PROTOTYPE_ROOT / "evals" / "cases" / "seed.jsonl",
    PROTOTYPE_ROOT / "evals" / "cases" / "adversarial.jsonl",
]


@pytest.mark.parametrize("case_file", CASE_FILES, ids=lambda p: p.name)
def test_reference_passes_its_own_suite(case_file: Path) -> None:
    wf = Workforce()
    assert wf.drafter.mode == "mock", (
        "This regression test must run in mock mode; unset ANTHROPIC_API_KEY."
    )

    cases = load_cases(case_file)
    assert cases, f"no cases loaded from {case_file}"

    k = 2
    results = run_eval(wf, cases, k=k, mock_mode=True)
    summary = summarize(results, k=k)

    assert summary["pass_rate"] == 1.0, (
        f"{case_file.name}: reference failed its own suite — "
        f"failures={summary['failures']}, flaky={summary['flaky']}"
    )
    assert not summary["flaky"], (
        f"{case_file.name}: flaky cases in deterministic mock mode "
        f"(this should be impossible): {summary['flaky']}"
    )
