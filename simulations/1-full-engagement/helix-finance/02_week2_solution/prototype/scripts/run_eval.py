"""Run the Helix eval harness.

Run from prototype/:
    python scripts/run_eval.py [--k=N] [--cases evals/cases/seed.jsonl]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from helix_agent.workforce import Workforce
from evals.harness import load_cases, run_eval, summarize


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, default=1, help="pass^k consistency runs per case")
    parser.add_argument("--cases", default="evals/cases/seed.jsonl")
    args = parser.parse_args()

    cases_path = Path(__file__).parent.parent / args.cases
    cases = load_cases(cases_path)
    print(f"Loaded {len(cases)} eval cases from {cases_path.name}")
    print(f"Running with k={args.k}")
    print()

    wf = Workforce()
    print(f"Drafter mode: {wf.drafter.mode}")
    print(f"KPI extractor mode: {wf.kpi.mode}")
    print(f"Tone supervisor mode: {wf.tone.mode}")
    print()

    results = run_eval(wf, cases, k=args.k)
    summary = summarize(results)

    print("RESULTS")
    print("-" * 60)
    print(f"Pass rate (weighted): {summary['pass_rate']:.0%}  ({summary['passed_weight']}/{summary['total_weight']})")
    print(f"Cases passed: {summary['passed_count']}/{summary['case_count']}")
    if summary["failures"]:
        print(f"Failures: {', '.join(summary['failures'])}")
    print()
    print("PER-CASE")
    print("-" * 60)
    for r in results:
        status = "PASS" if r["all_passed"] else "FAIL"
        print(f"  [{status}] {r['case_id']:45s} weight={r['weight']}")
        if not r["all_passed"]:
            for run in r["runs"]:
                for k, v in run["grades"]["details"].items():
                    if not v:
                        print(f"           - failed: {k}")
    return 0 if summary["pass_rate"] == 1.0 else 1


if __name__ == "__main__":
    sys.exit(main())
