"""Run the eval harness against the seed cases.

Run from prototype/ directory:
    python scripts/run_eval.py           # default: k=5 (production threshold)
    python scripts/run_eval.py --k 1     # demo / fast feedback
    python scripts/run_eval.py --k 10    # high-confidence pre-release gate
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from calder_agent.workforce import Workforce
from evals.harness import load_cases, run_eval, summarize


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Pass^k eval harness. Default k=5 is the production-deploy threshold; "
                    "variance tolerance is ≤5% across runs."
    )
    parser.add_argument("--k", type=int, default=5, help="pass^k consistency runs per case (default: 5)")
    parser.add_argument("--cases", default="evals/cases/seed.jsonl")
    args = parser.parse_args()

    cases_path = Path(__file__).parent.parent / args.cases
    cases = load_cases(cases_path)
    print(f"Loaded {len(cases)} eval cases from {cases_path.name}")
    print(f"Running with k={args.k} (pass^k production threshold = 5)")
    print()

    wf = Workforce()
    print(f"Drafter mode: {wf.drafter.mode}")
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
        print(f"  [{status}] {r['case_id']:35s} weight={r['weight']}")
        if not r["all_passed"]:
            for run in r["runs"]:
                for k, v in run["grades"]["details"].items():
                    if not v:
                        print(f"           - failed: {k}")
    print()

    return 0 if summary["pass_rate"] == 1.0 else 1


if __name__ == "__main__":
    sys.exit(main())
