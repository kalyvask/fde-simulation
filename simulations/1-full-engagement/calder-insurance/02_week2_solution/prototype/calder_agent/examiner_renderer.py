"""Examiner-readable trace renderer.

Tom asked specifically for "a one-page summary with drilldown links" — readable
by a NAIC market-conduct examiner without specialized tools. Marcus added that
the trace must show confidence and escalation threshold for AI decisions.

This module renders an AuditTrace as standalone HTML (no JS dependency, inline
CSS) suitable for handing to an examiner, attaching to an audit packet, or
viewing in a browser.

Pattern: pure-Python HTML generation. Each AuditTrace step becomes a card with
inputs, output, model version, rule, and confidence. The decision summary is
prominent at the top. Color-coded: green = auto_send, amber = adjuster_review.
"""
from __future__ import annotations

import html
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from calder_agent.trace import AuditTrace


CSS = """
* { box-sizing: border-box; }
body {
  font-family: 'Cambria', 'Georgia', serif;
  max-width: 920px;
  margin: 36px auto;
  padding: 0 24px 64px;
  color: #1a1a1a;
  background: #faf8f3;
}
h1, h2, h3 { font-family: 'Calibri', 'Inter', sans-serif; }
h1 { font-size: 26px; margin: 0 0 4px; letter-spacing: -0.01em; }
.subtitle { color: #6b6b6b; font-family: 'Calibri', sans-serif; font-size: 13px;
  text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 28px; }
.decision-banner {
  padding: 18px 22px; border-radius: 6px; margin-bottom: 24px;
  border-left: 6px solid;
  font-family: 'Calibri', sans-serif;
}
.decision-auto_send { background: #eaf5ea; border-left-color: #3a7d3a; }
.decision-adjuster_review { background: #fdf3e3; border-left-color: #c79331; }
.decision-banner .label { font-size: 11px; text-transform: uppercase;
  letter-spacing: 0.12em; color: #6b6b6b; margin-bottom: 6px; }
.decision-banner .value { font-size: 22px; font-weight: 700; }
.decision-banner .reason { margin-top: 8px; font-size: 14px; color: #404040; }
h2 { font-size: 18px; margin: 32px 0 14px; padding-bottom: 6px;
  border-bottom: 1px solid #d8d8d2; }
.kv { display: grid; grid-template-columns: 180px 1fr; gap: 6px 18px;
  font-size: 14px; margin-bottom: 22px; }
.kv .k { color: #6b6b6b; font-family: 'Calibri', sans-serif;
  text-transform: uppercase; font-size: 11px; letter-spacing: 0.08em;
  padding-top: 3px; }
.kv .v { color: #1a1a1a; }
.step {
  border: 1px solid #d8d8d2; background: #fff; border-radius: 6px;
  margin-bottom: 14px; overflow: hidden;
}
.step-head {
  padding: 10px 16px; background: #f3ede0;
  display: flex; justify-content: space-between; align-items: center;
  font-family: 'Calibri', sans-serif; font-size: 14px;
  border-bottom: 1px solid #d8d8d2;
}
.step-head .name { font-weight: 600; }
.step-head .meta { color: #6b6b6b; font-size: 12px; }
details summary {
  padding: 8px 16px; cursor: pointer; font-family: 'Calibri', sans-serif;
  font-size: 13px; color: #6b1c1c; user-select: none;
}
details[open] summary { border-bottom: 1px solid #d8d8d2; }
details pre { margin: 0; padding: 12px 16px; font-size: 12px;
  background: #f5f2eb; color: #1f1f1f; overflow-x: auto;
  font-family: 'Consolas', monospace; }
.step-body { padding: 12px 16px; font-size: 14px; }
.step-body .row { margin-bottom: 6px; }
.step-body .row .k { font-family: 'Calibri', sans-serif;
  text-transform: uppercase; font-size: 11px; letter-spacing: 0.06em;
  color: #6b6b6b; margin-right: 8px; }
.rules { font-family: 'Consolas', monospace; font-size: 12px;
  background: #f5f2eb; padding: 8px 12px; border-radius: 4px; }
footer { margin-top: 48px; padding-top: 16px; border-top: 1px solid #d8d8d2;
  font-family: 'Calibri', sans-serif; font-size: 11px; color: #6b6b6b;
  text-transform: uppercase; letter-spacing: 0.1em; }
"""


def _escape(value: Any) -> str:
    if value is None:
        return "—"
    return html.escape(str(value))


def _truncate_dict(d: dict[str, Any], max_chars: int = 400) -> str:
    s = json.dumps(d, indent=2, default=str)
    if len(s) > max_chars:
        return s[:max_chars] + "\n... (truncated)"
    return s


def _render_step(idx: int, entry) -> str:
    rule_html = _escape(entry.rule_applied)
    confidence_html = (
        f"{entry.confidence:.2f}" if entry.confidence is not None else "—"
    )
    threshold_html = (
        f"{entry.escalation_threshold:.2f}" if entry.escalation_threshold is not None else "—"
    )
    model_html = _escape(entry.model_version) if entry.model_version else "—"

    # Drilldown: full input + output (truncated to keep one-page)
    inputs_pretty = _truncate_dict(entry.inputs)
    output_pretty = _truncate_dict(entry.output if isinstance(entry.output, dict) else {"value": entry.output})

    return f"""
    <div class="step">
      <div class="step-head">
        <span class="name">{idx}. {_escape(entry.agent_name)}</span>
        <span class="meta">{entry.duration_ms} ms</span>
      </div>
      <div class="step-body">
        <div class="row"><span class="k">Rule</span><span>{rule_html}</span></div>
        <div class="row"><span class="k">Model</span><span>{model_html}</span></div>
        <div class="row"><span class="k">Confidence</span><span>{confidence_html}</span></div>
        <div class="row"><span class="k">Escalation threshold</span><span>{threshold_html}</span></div>
      </div>
      <details>
        <summary>Drilldown — inputs / output</summary>
        <pre>{html.escape(inputs_pretty)}

OUTPUT
------
{html.escape(output_pretty)}</pre>
      </details>
    </div>
    """


def render_html(trace: AuditTrace, claim_summary: dict[str, Any] | None = None) -> str:
    decision = trace.final_decision or "unknown"
    decision_class = f"decision-{decision}"
    started = trace.started_at.isoformat() + "Z"
    completed = (trace.completed_at or datetime.utcnow()).isoformat() + "Z"
    total_ms = sum(e.duration_ms for e in trace.entries) if trace.entries else 0

    summary_block = ""
    if claim_summary:
        rows = "".join(
            f'<div class="k">{_escape(k)}</div><div class="v">{_escape(v)}</div>'
            for k, v in claim_summary.items()
        )
        summary_block = f"<h2>Claim summary</h2><div class=\"kv\">{rows}</div>"

    steps_html = "\n".join(
        _render_step(i, e) for i, e in enumerate(trace.entries, 1)
    )

    rules_html = ", ".join(
        sorted({e.rule_applied for e in trace.entries if e.rule_applied})
    ) or "—"

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Audit Trace — Claim {_escape(trace.claim_id)}</title>
<style>{CSS}</style>
</head>
<body>
  <h1>Audit Trace</h1>
  <div class="subtitle">Claim {_escape(trace.claim_id)} · Trace {_escape(trace.trace_id)}</div>

  <div class="decision-banner {decision_class}">
    <div class="label">Final decision</div>
    <div class="value">{_escape(decision)}</div>
    <div class="reason">{_escape(trace.final_decision_reason or "")}</div>
  </div>

  {summary_block}

  <h2>Timing</h2>
  <div class="kv">
    <div class="k">Started</div><div class="v">{started}</div>
    <div class="k">Completed</div><div class="v">{completed}</div>
    <div class="k">Total agent time</div><div class="v">{total_ms} ms</div>
    <div class="k">Steps</div><div class="v">{len(trace.entries)}</div>
  </div>

  <h2>Steps</h2>
  {steps_html}

  <h2>Rules invoked</h2>
  <div class="rules">{_escape(rules_html)}</div>

  <footer>
    Calder FNOL Workforce · v1 wedge · Examiner-readable audit trace
  </footer>
</body>
</html>
"""


def render_to_file(trace: AuditTrace, path: Path | str, claim_summary: dict[str, Any] | None = None) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(render_html(trace, claim_summary), encoding="utf-8")
    return p
