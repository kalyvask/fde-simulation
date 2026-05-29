"""Eval harness — pass^k discipline with weighted failure cost.

Loads cases from JSONL, runs them k times each through the workforce, grades
each run, applies pass^k (a case passes only if all k runs pass), and
summarizes weighted pass rate.

Grade dimensions per case:
- decision: did the workforce route the claim correctly?
- must_contain: every listed substring appears in the draft (case-insensitive)
- must_not_contain: every listed substring is absent (case-insensitive)
- rules_fired: every named policy rule fired (validates the policy library)
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class EvalCase:
    case_id: str
    fnol: dict[str, Any]
    expected: dict[str, Any]
    weight: int = 1
    # Cases whose expected output depends on content only the real LLM generates
    # (e.g. catching a recommendation the mock drafter never writes). The mock
    # pipeline cannot satisfy these, so the harness skips them in mock mode and
    # the real-key CI job is what actually exercises them.
    requires_llm: bool = False


def load_cases(path: Path) -> list[EvalCase]:
    cases: list[EvalCase] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("//"):
            continue
        d = json.loads(line)
        cases.append(EvalCase(
            case_id=d["case_id"],
            fnol=d["fnol"],
            expected=d["expected"],
            weight=d.get("weight", 1),
            requires_llm=d.get("requires_llm", False),
        ))
    return cases


def grade(case: EvalCase, output: dict[str, Any]) -> dict[str, Any]:
    expected = case.expected
    details: dict[str, Any] = {}
    passes = True

    if "decision" in expected:
        match = output["decision"] == expected["decision"]
        details["decision_match"] = match
        if not match:
            passes = False

    for required in expected.get("must_contain", []):
        present = required.lower() in output["draft"].lower()
        details[f"contains:{required[:30]}"] = present
        if not present:
            passes = False

    for forbidden in expected.get("must_not_contain", []):
        present = forbidden.lower() in output["draft"].lower()
        details[f"absent:{forbidden[:30]}"] = not present
        if present:
            passes = False

    for required_rule in expected.get("rules_fired", []):
        present = required_rule in output.get("rules_fired", [])
        details[f"rule_fired:{required_rule}"] = present
        if not present:
            passes = False

    return {"passes": passes, "details": details}


def run_eval(workforce, cases: list[EvalCase], k: int = 1, mock_mode: bool = False) -> list[dict]:
    results = []
    for case in cases:
        if mock_mode and case.requires_llm:
            results.append({
                "case_id": case.case_id,
                "weight": case.weight,
                "skipped": True,
                "all_passed": False,
                "run_pass_count": 0,
                "runs": [],
            })
            continue
        runs = []
        for _ in range(k):
            output, trace = workforce.process_fnol(case.fnol)
            grades = grade(case, output)
            runs.append({
                "draft": output["draft"],
                "decision": output["decision"],
                "violations": output["violations"],
                "rules_fired": output["rules_fired"],
                "grades": grades,
            })
        run_pass_count = sum(1 for r in runs if r["grades"]["passes"])
        all_passed = run_pass_count == k
        results.append({
            "case_id": case.case_id,
            "weight": case.weight,
            "skipped": False,
            "all_passed": all_passed,
            "run_pass_count": run_pass_count,
            "runs": runs,
        })
    return results


def summarize(results: list[dict], k: int = 1) -> dict[str, Any]:
    scored = [r for r in results if not r.get("skipped")]
    skipped = [r for r in results if r.get("skipped")]
    weighted_pass = sum(r["weight"] for r in scored if r["all_passed"])
    total_weight = sum(r["weight"] for r in scored)
    # A case is flaky if some-but-not-all of its k runs passed: direct evidence
    # of run-to-run non-determinism (the thing pass^k is supposed to catch).
    flaky = [r["case_id"] for r in scored if 0 < r.get("run_pass_count", 0) < k]
    return {
        "pass_rate": (weighted_pass / total_weight) if total_weight else 0.0,
        "passed_weight": weighted_pass,
        "total_weight": total_weight,
        "case_count": len(scored),
        "passed_count": sum(1 for r in scored if r["all_passed"]),
        "failures": [r["case_id"] for r in scored if not r["all_passed"]],
        "skipped": [r["case_id"] for r in skipped],
        "flaky": flaky,
    }
