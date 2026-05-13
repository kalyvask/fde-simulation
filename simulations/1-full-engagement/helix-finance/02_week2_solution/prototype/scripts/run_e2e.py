"""End-to-end demo — one synthetic earnings call through the workforce.

Run from prototype/:
    python scripts/run_e2e.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from helix_agent.workforce import Workforce
from helix_agent.data.synthetic import generate_earnings_claim


def main() -> None:
    print("=" * 60)
    print("Helix Earnings-Note Workforce — E2E Demo")
    print("=" * 60)
    print()

    claim = generate_earnings_claim(seed=42)

    print("CLAIM INPUT")
    print("-" * 60)
    print(json.dumps(claim, indent=2, default=str))
    print()

    wf = Workforce()
    print(f"Drafter mode: {wf.drafter.mode}")
    print()

    output, trace = wf.process_earnings_call(claim)

    print("AGENT OUTPUTS")
    print("-" * 60)
    print(f"Decision: {output['decision']}")
    print(f"Reason:   {output['reason']}")
    if output.get("rules_fired"):
        print(f"Rules fired: {output['rules_fired']}")
    print()
    print("DRAFT")
    print("-" * 60)
    print(output.get("draft") or "(no draft — blocked)")
    print()
    print("COMPLIANCE TRACE (Mei-readable)")
    print("-" * 60)
    print(trace.to_compliance_summary())


if __name__ == "__main__":
    main()
