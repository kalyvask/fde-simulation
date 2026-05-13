# Helix Earnings-Note Workforce — Prototype Scaffold

> Week 2 build artifact. Eval-first agent workforce that drafts morning-after-earnings analyst notes for portfolio managers. Drafts only — no auto-publishing, no trading-system access.

## How to use this scaffold

A **learning scaffold**, not production. The structure mirrors Calder's prototype intentionally — patterns port across domains, content swaps.

1. Read the code patterns first (don't run anything yet)
2. Run `python scripts/run_e2e.py` to see one synthetic earnings call flow end to end
3. Run `python scripts/run_eval.py` to see the eval harness on the seed cases
4. Then extend: add agents, expand the policy library, add eval cases

## Setup

```bash
cd week-2-solution/prototype
python -m venv .venv
.venv/Scripts/activate     # Windows
pip install -r requirements.txt
```

Optionally set an API key:

```bash
# Anthropic
$env:ANTHROPIC_API_KEY="sk-ant-..."

# Or OpenAI (preferred for Helix; matches OpenAI FDE muscle memory)
$env:OPENAI_API_KEY="sk-..."
```

Without a key, agents fall back to deterministic mock outputs.

## Layout

```
prototype/
├── helix_agent/
│   ├── trace.py                  # AuditTrace data model (FINRA / SEC ready)
│   ├── policy_library.py         # MNPI watch list + Mei's compliance rules
│   ├── workforce.py              # 9-agent orchestration
│   ├── agents/
│   │   ├── base.py               # BaseAgent w/ auto trace
│   │   ├── mnpi_scrubber.py      # FIRST agent in pipeline; deterministic
│   │   ├── intake.py             # Transcript + 10-Q parser
│   │   ├── note_drafter.py       # LLM-backed note writer
│   │   └── compliance_critic.py  # Mei's rule library check
│   └── data/synthetic.py         # Synthetic earnings call generator
├── evals/
│   ├── harness.py                # Pass^k + weighted grading
│   └── cases/seed.jsonl          # 5 hand-crafted cases
├── scripts/
│   ├── run_e2e.py
│   └── run_eval.py
└── requirements.txt
```

## Design decisions worth knowing

1. **MNPI Scrubber is the FIRST agent.** Before any LLM call. Deterministic. Block-or-proceed. Failure here = engagement-ending event.
2. **Citation grounding is non-negotiable.** Every number in the draft traces to a source span. No exceptions. Enforced deterministically post-draft.
3. **Trace-first.** Every agent writes to AuditTrace on every call. Same pattern as Calder. The trace is examiner-readable for FINRA compliance review.
4. **Hybrid det+LLM** with even more deterministic guardrails than Calder. Finance regulatory cost is higher; engineer more deterministic guards.
5. **Pass^k=5 production gate.** Same as Sierra ADLC default.

## What's NOT in v1

- M&A commentary (regulatory minefield)
- Position-sizing recommendations (cross-Chinese-wall)
- MNPI watch-list names (architecturally blocked)
- Auto-publishing (always senior-analyst-reviewed + compliance-approved)
- Non-equity asset classes
- Real-time market data (transcript + filing data only)

## What to extend next

1. **Add 25 more eval cases** — Hallucinated-guidance adversarial, MNPI smell-tests, multi-quarter context preservation
2. **Tone-Shift Detector agent** (LLM-as-judge against SubjECTive-QA labels)
3. **Consensus Comparator** with Yahoo Finance / Refinitiv integration
4. **Citation Verifier** that checks every number maps to a source span
5. **Examiner-readable trace renderer** for FINRA + internal compliance review
6. **Tone-shift calibration tooling** (Brier score across SME-graded samples)

## Cross-reference

If you've read Calder's scaffold, the patterns will feel familiar. Specifically:
- `helix_agent/trace.py` mirrors `calder_agent/trace.py`
- `helix_agent/agents/base.py` is identical pattern
- `helix_agent/workforce.py` follows the same orchestration shape
- `policy_library.py` is finance-specific (MNPI watch list, Mei's 3 rules) but follows Calder's deterministic-rule pattern

The skill is the pattern; the content is the variable. That's the OpenAI FDE interview moat.
