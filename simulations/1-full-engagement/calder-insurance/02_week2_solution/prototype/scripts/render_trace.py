"""Render an audit trace as examiner-readable HTML.

Run from prototype/:
    python scripts/render_trace.py

Generates a synthetic FNOL, runs it through the workforce, then writes the
examiner HTML to traces/<claim_id>.html. Open the file in any browser.
"""
from __future__ import annotations

import sys
import webbrowser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from calder_agent.workforce import Workforce
from calder_agent.data.synthetic import generate_fnol
from calder_agent.examiner_renderer import render_to_file


def main() -> int:
    fnol = generate_fnol(state="NJ", channel="web", lob="comm_auto", seed=42)
    fnol["has_child_or_elderly_party"] = True  # force escalation for demo

    wf = Workforce()
    print(f"Drafter mode: {wf.drafter.mode}")
    output, trace = wf.process_fnol(fnol)

    summary = {
        "Claim ID": fnol["claim_id"],
        "Claimant": fnol["claimant_name"],
        "State": fnol["state"],
        "Line of business": fnol["lob"],
        "Channel": fnol["channel"],
        "Incident date": fnol["incident_date"],
        "Estimated damage": f"${fnol['estimated_damage']:,}",
    }

    out_dir = Path(__file__).parent.parent / "traces"
    out_path = out_dir / f"{fnol['claim_id']}.html"
    render_to_file(trace, out_path, claim_summary=summary)

    print(f"Wrote {out_path}")
    print(f"Decision: {trace.final_decision}")
    print(f"Reason:   {trace.final_decision_reason}")

    # Open in default browser
    try:
        webbrowser.open(out_path.as_uri())
    except Exception:
        print("(open the path manually if it didn't auto-launch)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
