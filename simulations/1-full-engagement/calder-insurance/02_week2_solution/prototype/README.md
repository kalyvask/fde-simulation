# Calder FNOL AI Workforce — Prototype Scaffold

> Week 2 build artifact. Eval-first agent workforce that auto-acknowledges incoming FNOL claims and routes the 20% to an adjuster review queue. Drafts only — no writes back to Guidewire in v1.

## How to use this scaffold

This is a **learning scaffold**, not a production system. It's deliberately small. You should:
1. Read the code patterns first (don't run anything yet)
2. Then run `python scripts/run_e2e.py` to see one synthetic FNOL flow end to end
3. Then run `python scripts/run_eval.py` to see the eval harness on the seed cases
4. Then extend it: add agents, expand the policy library, add eval cases

The point is to internalize the **patterns** — once you have the scaffold pattern in your head, you can rebuild it from scratch in a different language for a different customer. That's the FDE muscle.

## Setup

```bash
cd week-2-solution/prototype
python -m venv .venv
.venv/Scripts/activate     # Windows
# source .venv/bin/activate # mac/linux
pip install -r requirements.txt
```

Optionally set an Anthropic API key to use real Claude calls:

```bash
export ANTHROPIC_API_KEY=sk-ant-...    # mac/linux
$env:ANTHROPIC_API_KEY="sk-ant-..."   # windows powershell
```

If no key is set, the Drafter agent falls back to a deterministic mock response so you can still run the scaffold end-to-end.

## Run

```bash
# End-to-end demo on one synthetic FNOL
python scripts/run_e2e.py

# Eval harness against seed cases
python scripts/run_eval.py
```

## Layout

```
prototype/
├── calder_agent/
│   ├── trace.py                  # AuditTrace data model (Tom + Marcus's standard)
│   ├── policy_library.py         # Marcus's 3 unwritten rules + state SLAs
│   ├── workforce.py              # Orchestrates the agents
│   ├── agents/
│   │   ├── base.py               # BaseAgent class with trace integration
│   │   ├── intake.py             # Deterministic field extraction
│   │   ├── drafter.py            # LLM-backed acknowledgment writer
│   │   └── compliance_critic.py  # Deterministic policy + state-SLA check
│   └── data/
│       └── synthetic.py          # Synthetic FNOL generator (placeholder for Greg's pull)
├── evals/
│   ├── harness.py                # Eval runner with pass^k discipline
│   └── cases/
│       └── seed.jsonl            # 5 hand-crafted cases from discovery
├── scripts/
│   ├── run_e2e.py                # End-to-end demo
│   └── run_eval.py               # Eval pass against seed
├── tests/
│   └── test_policy_library.py    # Unit tests for deterministic guardrails
└── requirements.txt
```

## Design decisions worth knowing

1. **Hybrid det+LLM**. Intake = deterministic. Drafter = LLM. Compliance critic = deterministic. The decision tree is in `training/week2_build_playbook.md`.

2. **Trace-first**. Every agent writes to `AuditTrace` on every call. The trace is a first-class artifact, not an afterthought. Tom's and Marcus's audit standards drove this.

3. **Marcus's 3 unwritten rules are deterministic Python code**, not LLM prompts. Policy is not judgment.

4. **Eval-driven**. The harness exists before any prompt. Every eval case has a weight; rare-but-critical cases have 10x weight on misses.

5. **Pass^k, not pass@1**. the agent development lifecycle pattern. Default `k=1` for fast feedback; bump to `k=5` before any rollout decision.

6. **Mock fallback** for the LLM. Lets the scaffold run without a key for code-reading; real Anthropic calls when the key is set.

## Where the public data fits

The `data/synthetic.py` generator produces FNOL records that mirror the structure we'll get from Greg's 500-claim pull. While we wait for the real pull, you can:

- Augment with NHTSA CRSS narratives (set the `incident_description` field from real crash narratives) to stress-test extraction
- Pull Kaggle Auto Insurance Claims for `fraud_reported` ground truth on routing
- Pull FUNSD for OCR stress on attached docs

See `data/README.md` at the project root for fetch instructions.

## What's NOT in v1

- Coverage decisions (Marcus's HITL floor)
- Bodily-injury claims (Janet's hard NO)
- Writes to Guidewire (Anil's read-only deal that unlocked the queue)
- Phone-channel transcripts (web + agent portal first)
- Multi-language comms (English first)

## What to extend next

In rough order of priority:
1. **Add 25 more eval cases** targeting the "tells" Janet named (lawyered-up paragraph, "didn't have time to react")
2. **Add the ToneSupervisor agent** (LLM-as-judge against the 5-element comm-quality bar)
3. **Add state-SLA timing checks** properly (currently a single rule)
4. **Wire up Splunk-equivalent local logging** (JSON lines for now)
5. **Add the adjuster-review-queue UI** (Streamlit; can come from Calder eval feedback)
6. **Write the audit-trace examiner-summary renderer** (Tom's "human-readable, drilldown-able")
