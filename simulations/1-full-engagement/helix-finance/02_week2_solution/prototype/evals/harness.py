"""Eval harness for the Helix workforce — pass^k + weighted grading.

Same pattern as Calder. Grades on decision_match + must_contain + must_not_contain
+ rules_fired + financial-grounding (every cited number traces to source).
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class EvalCase:
    case_id: str
    claim: dict[str, Any]
    expected: dict[str, Any]
    weight: int = 1


def load_cases(path: Path) -> list[EvalCase]:
    cases: list[EvalCase] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("//"):
            continue
        d = json.loads(line)
        cases.append(EvalCase(
            case_id=d["case_id"],
            claim=d["claim"],
            expected=d["expected"],
            weight=d.get("weight", 1),
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

    draft = output.get("draft") or ""
    for required in expected.get("must_contain", []):
        present = required.lower() in draft.lower()
        details[f"contains:{required[:30]}"] = present
        if not present:
            passes = False

    for forbidden in expected.get("must_not_contain", []):
        present = forbidden.lower() in draft.lower()
        details[f"absent:{forbidden[:30]}"] = not present
        if present:
            passes = False

    for required_rule in expected.get("rules_fired", []):
        present = required_rule in (output.get("rules_fired") or [])
        details[f"rule_fired:{required_rule}"] = present
        if not present:
            passes = False

    if expected.get("citation_must_pass"):
        cit = output.get("citation_check", {})
        citation_passed = cit.get("passes", False)
        details["citation_passes"] = citation_passed
        if not citation_passed:
            passes = False

    return {"passes": passes, "details": details}


def run_eval(workforce, cases: list[EvalCase], k: int = 1) -> list[dict]:
    results = []
    for case in cases:
        runs = []
        for _ in range(k):
            output, _trace = workforce.process_earnings_call(case.claim)
            grades = grade(case, output)
            runs.append({
                "decision": output["decision"],
                "rules_fired": output.get("rules_fired", []),
                "violations": output.get("violations", []),
                "grades": grades,
            })
        all_passed = all(r["grades"]["passes"] for r in runs)
        results.append({
            "case_id": case.case_id,
            "weight": case.weight,
            "all_passed": all_passed,
            "runs": runs,
        })
    return results


def summarize(results: list[dict]) -> dict[str, Any]:
    weighted_pass = sum(r["weight"] for r in results if r["all_passed"])
    total_weight = sum(r["weight"] for r in results)
    return {
        "pass_rate": (weighted_pass / total_weight) if total_weight else 0.0,
        "passed_weight": weighted_pass,
        "total_weight": total_weight,
        "case_count": len(results),
        "passed_count": sum(1 for r in results if r["all_passed"]),
        "failures": [r["case_id"] for r in results if not r["all_passed"]],
    }
