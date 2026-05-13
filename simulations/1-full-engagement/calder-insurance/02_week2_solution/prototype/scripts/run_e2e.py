"""End-to-end demo — one synthetic FNOL through the workforce.

Run from prototype/ directory:
    python scripts/run_e2e.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Add prototype/ to path so relative imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from calder_agent.workforce import Workforce
from calder_agent.data.synthetic import generate_fnol


def main() -> None:
    print("=" * 60)
    print("Calder FNOL Workforce — E2E Demo")
    print("=" * 60)
    print()

    fnol = generate_fnol(state="NJ", channel="web", lob="comm_auto", seed=42)

    print("FNOL INPUT")
    print("-" * 60)
    print(json.dumps(fnol, indent=2, default=str))
    print()

    wf = Workforce()
    print(f"Drafter mode: {wf.drafter.mode}")
    print()

    output, trace = wf.process_fnol(fnol)

    print("AGENT OUTPUTS")
    print("-" * 60)
    print(f"Decision: {output['decision']}")
    print(f"Reason:   {output['reason']}")
    print(f"Policy flags: {output['policy_flags']}")
    print(f"Rules fired:  {output['rules_fired']}")
    print(f"Violations:   {output['violations']}")
    print()
    print("DRAFT")
    print("-" * 60)
    print(output["draft"])
    print()

    print("AUDIT TRACE (examiner summary)")
    print("-" * 60)
    print(trace.to_examiner_summary())


if __name__ == "__main__":
    main()
