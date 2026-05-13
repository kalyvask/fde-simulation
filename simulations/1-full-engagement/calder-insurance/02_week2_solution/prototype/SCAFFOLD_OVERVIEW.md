# Calder FNOL Scaffold — Overview Document

> Companion to the **Week 2 Build Playbook**. The playbook describes the methodology; this document shows the actual code patterns. Read in pairs: read the playbook section, then read the corresponding code below to see what the pattern looks like in practice.

---

# Section 1 — Project layout

```
week-2-solution/prototype/
├── README.md
├── requirements.txt
├── calder_agent/
│   ├── __init__.py
│   ├── trace.py                  # AuditTrace — Tom + Marcus standard
│   ├── policy_library.py         # Marcus's 3 unwritten rules + state SLAs
│   ├── workforce.py              # Orchestration
│   ├── agents/
│   │   ├── base.py               # BaseAgent w/ auto trace
│   │   ├── intake.py             # Deterministic field extraction
│   │   ├── drafter.py            # LLM (Claude) + mock fallback
│   │   └── compliance_critic.py  # Deterministic policy + SLA check
│   └── data/synthetic.py         # Synthetic FNOL generator
├── evals/
│   ├── harness.py                # Pass^k + weighted grading
│   └── cases/seed.jsonl          # 5 hand-crafted cases
├── tests/test_policy_library.py  # 10 unit tests
└── scripts/
    ├── run_e2e.py
    └── run_eval.py
```

# Section 2 — How to run

```
cd week-2-solution/prototype
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
python scripts/run_e2e.py        # one synthetic FNOL through the workforce
python scripts/run_eval.py       # eval pass against the 5 seed cases
python -m pytest tests/ -v       # unit tests for the policy library
```

Set `ANTHROPIC_API_KEY` to use real Claude calls; otherwise drafter falls back to a deterministic mock.

# Section 3 — Validation results

| Command | Result |
|---|---|
| `python scripts/run_e2e.py` | Produces draft + decision + 3-step audit trace |
| `python scripts/run_eval.py` | 5/5 cases pass, 100% weighted (29/29) |
| `python -m pytest tests/ -v` | 10/10 unit tests pass |

---

# Section 4 — Key code patterns

The next sections show four code files that demonstrate the most important patterns. Read each pattern alongside the corresponding playbook section.

---

## Pattern A — Audit Trace (trace.py)

**Why this pattern matters**: Tom asked for inputs, rule, output, human reviewer, timestamps, model version, human-readable summary. Marcus added confidence + escalation threshold visible in trace. Both surfaced this in week-1 discovery. The trace is a first-class artifact, not logging.

**Key choices**:
- `TraceEntry` is a dataclass — every field is explicit, every field is part of the contract
- `AuditTrace.to_examiner_summary()` produces a one-page text artifact (Tom's specific format request)
- `BaseAgent.execute()` automatically writes a TraceEntry on every call — agents can't forget

**The class structure**:
```
TraceEntry:
  step_id, agent_name, started_at, completed_at,
  inputs, output, model_version, retrieved_context,
  rule_applied, confidence, escalation_threshold,
  human_reviewed, human_review_decision, human_review_reason

AuditTrace:
  trace_id, claim_id, started_at, completed_at,
  entries: list[TraceEntry],
  final_output, final_decision, final_decision_reason
  
  add(entry)
  close(final_output, decision, reason)
  to_examiner_summary() -> str
  to_dict() -> dict
```

---

## Pattern B — Policy Library (policy_library.py)

**Why this pattern matters**: Marcus's 3 unwritten rules + state-by-state SLAs. These MUST be deterministic Python — never LLM judgment. Failure cost is regulatory; you cannot let stochasticity in.

**Key choices**:
- Each rule is a small function — unit-testable, version-controllable
- State policies are a frozen dictionary keyed on state code; default falls back to NJ standards (Marcus's guidance)
- The aggregate `policy_check()` returns flags + the rules that fired (so the trace shows what triggered escalation)

**Rule 1 — child or elderly party**:
```python
def rule_1_child_or_elderly_party(claim) -> tuple[bool, str | None]:
    if claim.get("has_child_or_elderly_party"):
        return True, "policy.rule_1_child_or_elderly_party"
    return False, None
```

**Rule 2 — first-time customer warmth** (note: this is a tone flag, not an escalation):
```python
def rule_2_first_time_customer_warmth(claim) -> dict:
    if claim.get("first_time_customer"):
        return {"tone_flag": "warmer"}
    return {"tone_flag": "standard"}
```

**Rule 3 — prior claim in 12 months**:
```python
def rule_3_prior_claim_in_12_months(claim) -> tuple[bool, str | None]:
    if claim.get("has_prior_claim_in_12_months"):
        return True, "policy.rule_3_prior_claim_in_12_months"
    return False, None
```

**State policies (excerpt)**:
```python
STATE_POLICIES = {
    "NJ": StatePolicy("NJ", 24, 10, requires_hitl_on_coverage=True, requires_hitl_on_settlement=True),
    "PA": StatePolicy("PA", 24, 10, requires_hitl_on_settlement=True, strict_on_accuracy=True),
    "NY": StatePolicy("NY", 24, 10, requires_hitl_on_coverage=True, strict_on_systemic_pattern=True),
    "MA": StatePolicy("MA", 24, 10, strict_on_documentation=True),
    # 8 looser states default to NJ via get_state_policy() fallback
}
```

---

## Pattern C — BaseAgent with auto-trace (agents/base.py)

**Why this pattern matters**: every agent must produce a trace entry. If we left it to the agent author, someone would forget. The framework wraps `run()` with `execute()`, which handles trace bookkeeping automatically. Agent authors implement only `run()`.

**The pattern**:
```python
class BaseAgent(ABC):
    name: str = "unnamed_agent"
    model_version: Optional[str] = None  # set if LLM-backed

    @abstractmethod
    def run(self, inputs) -> AgentResult:
        # subclasses implement business logic
        ...

    def execute(self, inputs, trace) -> AgentResult:
        # framework wraps run() with trace bookkeeping
        started = datetime.utcnow()
        result = self.run(inputs)
        completed = datetime.utcnow()
        trace.add(TraceEntry(
            step_id=str(uuid.uuid4()),
            agent_name=self.name,
            started_at=started,
            completed_at=completed,
            inputs=inputs,
            output=result.output,
            model_version=self.model_version,
            retrieved_context=result.retrieved_context,
            rule_applied=result.rule_applied,
            confidence=result.confidence,
            escalation_threshold=result.escalation_threshold,
        ))
        return result
```

**The principle**: do not make the agent author responsible for observability. Make observability a framework property.

---

## Pattern D — Workforce orchestration (workforce.py)

**Why this pattern matters**: the workforce is the conductor. It composes agents in sequence, builds intermediate inputs (state policy → drafter inputs), enforces routing decisions deterministically (not via LLM).

**The flow**:
```
1. Intake — deterministic field extraction
2. Build drafter inputs:
     facts (from intake) +
     timeline_days (from state policy) +
     contact info +
     tone_flag (from rule 2)
3. Drafter — LLM-backed natural language synthesis
4. ComplianceCritic — deterministic policy + SLA + draft sanity check
5. Routing decision (deterministic):
     if must_escalate → adjuster_review
     elif violations → adjuster_review
     else → auto_send
6. Trace.close() → final output + decision + reason
```

**The principle**: routing is too important to be an LLM call. It's a `must_escalate or has_violations` decision over deterministic outputs of upstream agents.

---

## Pattern E — Eval harness (evals/harness.py)

**Why this pattern matters**: pass^k discipline (the agent development lifecycle). Weighted by failure cost (Marcus's rules → 10x weight). Grades on decision + must_contain + must_not_contain + rules_fired.

**Case format (JSONL, one per line)**:
```json
{
  "case_id": "policy_rule_elderly_NJ_10x",
  "weight": 10,
  "fnol": { ... },
  "expected": {
    "decision": "adjuster_review",
    "rules_fired": ["policy.rule_1_child_or_elderly_party"]
  }
}
```

**Pass^k logic**:
```python
def run_eval(workforce, cases, k=1):
    results = []
    for case in cases:
        runs = [workforce.process_fnol(case.fnol) for _ in range(k)]
        graded = [grade(case, output) for output, trace in runs]
        all_passed = all(g["passes"] for g in graded)
        results.append({"case_id": case.case_id, "weight": case.weight, "all_passed": all_passed})
    return results

def summarize(results):
    weighted_pass = sum(r["weight"] for r in results if r["all_passed"])
    total_weight = sum(r["weight"] for r in results)
    return {"pass_rate": weighted_pass / total_weight, ...}
```

**The principle**: pass@1 misleads on agents (one lucky run looks like success). Pass^k forces consistency — only count a case as passed if all k runs pass. The weighting forces the eval to care more about the failure modes that hurt.

---

# Section 5 — How to use this document for cross-check

For each of the 5 patterns above:
1. Read the pattern in this overview
2. Open the corresponding file in the prototype folder (`trace.py`, `policy_library.py`, etc.)
3. Read the actual code
4. Find the playbook section that names this pattern in **`week2_build_playbook.md`** (now in the kickoff playbook docx)
5. Confirm the playbook's prescription matches the implementation

**Where any of those three (overview / actual code / playbook) diverge — that's a bug or a gap in your understanding.** Find which it is.

---

# Section 6 — What's deliberately missing (left as exercises)

Not in the v1 scaffold, on purpose:

1. **ToneSupervisorAgent** — LLM-as-judge against Janet's 5-element comm-quality bar. Stub it out by Day 5.
2. **AuditLoggerAgent** — Splunk ingestion of the trace. Currently the trace is just an in-memory object; route it to Splunk in week 3.
3. **Adjuster review queue UI** — Streamlit app that surfaces the 20%. Day 6+.
4. **State-SLA timing checks** for the response timeline — currently a single deterministic phrase check in compliance_critic.py; expand to per-state per-LOB.
5. **Real Guidewire integration** — currently no API calls. Read-only adapter to be built once Anil + Kayla deliver sandbox access.
6. **Pass^k variance tracking over time** — currently k defaults to 1; bump and graph as eval suite grows.

Building these is the Day 5 + Week 3 work. The scaffold is intentionally incomplete so you can extend it as a learning exercise.
