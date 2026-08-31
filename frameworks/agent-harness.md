# The Agent Harness — Control Plane for Production Agents

> The model provides intelligence. The **harness** — the execution and control layer around it — is what makes that intelligence reliable, operational, and safe to point at a customer's systems. This is the organizing framework for everything the repo's other frameworks touch in pieces: it names the whole control layer, and fills the parts the short-horizon cases don't exercise (long-horizon state, recovery, outcome verification).
>
> Use it when the question moves from "which model?" to "what surrounds the model while it works?" — increasingly the real FDE system-design question.

## The frame: the harness is a control plane

Enterprise systems are deterministic. Models are probabilistic. You do not want probabilistic decisions flowing straight into a CRM, an ERP, or a payments API. The harness is the **architectural boundary** between the two — it takes the model's reasoning and constrains, persists, verifies, and gates it into deterministic, auditable action.

```
        BUSINESS GOAL
             │
             ▼
   ┌────────────────────┐
   │    AGENT HARNESS    │  context · state · tools · policy
   │   (control plane)   │  planning · verify · recover · observe
   └─────────┬──────────┘
       ┌─────┴─────┐
       ▼           ▼
     MODEL       HUMAN
   (reasoning)  (approval)
       └─────┬─────┘
             ▼
     ENTERPRISE SYSTEMS  (CRM · ERP · DB · APIs)
```

Every deterministic gate in this repo's prototypes — the MNPI Scrubber, the Compliance Critic, the read-only integration tier — is a piece of that control plane. Naming the boundary is the senior move: *"the model decides; the harness is what I trust."*

## The component model

A production harness provides eleven capabilities. Most are already covered elsewhere in the repo — this framework is the map, not a re-teach. The four in **bold** are the ones the short-horizon cases don't exercise, covered in full below.

| Capability | What it does | Where it's covered |
|---|---|---|
| Context | Curate what the model needs *now* for the next decision | [`system-design-round.md`](system-design-round.md) (RAG) |
| Tools | Narrow, task-oriented action surface | [`agent-shapes-catalog.md`](agent-shapes-catalog.md), [`system-design-round.md`](system-design-round.md) (tool design + MCP) |
| Permissions & guardrails | Separate what the agent can *see* from what it can *do* | [`agent-exploitation-taxonomy.md`](agent-exploitation-taxonomy.md) |
| Observability | Trace every attempt, tool call, retry, cost, outcome | [`production-debugging.md`](production-debugging.md), [`4-dimensional-testing.md`](4-dimensional-testing.md) |
| Evaluation | Measure business-task success, not just model accuracy | [`4-dimensional-testing.md`](4-dimensional-testing.md) (incl. trajectory eval) |
| **State & memory** | Persist task progress outside the model | *below* |
| **Planning & execution** | Goal → plan → execute → verify → update, with re-planning | *below* |
| **Verification** | Verify external side effects, not the model's claims | *below* |
| **Recovery** | Checkpoints, retries, idempotency, escalation | *below* |
| Permissions ladder | Autonomy proportional to risk and proven reliability | *earn autonomy, below* |
| Human intervention | Approval gates on high-impact actions | [`agent-exploitation-taxonomy.md`](agent-exploitation-taxonomy.md) (unsafe autonomy) |

## The four the short-horizon cases don't exercise

This repo's Calder and Helix cases are deliberately **short-horizon**: single-request pipelines (intake → draft → critic → send). The industry is moving to the **long-horizon worker** that owns an outcome across hours and hundreds or thousands of steps. At that scale failures are inevitable, and the whole game changes from "make each step perfect" to "make the system resilient to imperfect steps."

### 1. State & memory — the model is not the system of record
Persist the task as an explicit record, not as conversation history:

```
Goal
 ├── Completed        ├── Artifacts
 ├── In progress      ├── Decisions
 ├── Blocked          └── Next action
```

If the agent crashes after step 37 of 100, the system resumes from step 37 — it does not reconstruct the task from a transcript. The transcript is lossy and unauditable; the state record is neither.

### 2. Planning & execution — a loop, not a single call
Long work runs a loop: **goal → plan → execute → verify → update state → (continue | re-plan)**. The plan is not fixed. Tools fail, new information appears, assumptions turn out wrong. The harness lets the agent **re-plan from current state without losing prior progress** — which is only possible because state (1) is explicit.

### 3. Verification — verify outcomes, not intentions
The single biggest tell of a demo vs. a production agent. An agent saying *"Updated 500 customer records"* is a **claim**, not a fact. The harness validates the resulting external state:

```
Agent: "Updated 500 records" → VERIFY → read the DB / check business rules / compare expected state
                                        → success | retry | escalate | rollback
```

The repo's critics verify the *draft* before it's sent; this is the write-side analogue — verify the *side effect* after it's attempted. It's why the repo defaults to read-only v1: you only take an action you can verify and reverse.

### 4. Recovery — design for failure
Assume tools, models, APIs, and plans will fail. The resilience kit:
- **Checkpoints** — every meaningful unit of progress is recoverable
- **Idempotency** — re-running a step produces the same result (dedupe keys, deterministic seeds), so retries are safe
- **Retry policies + timeouts** — bounded, not infinite
- **Human escalation + cost controls** — the ceiling on an autonomous loop

## Earn autonomy

Autonomy is not granted; it is earned. Start the agent **constrained** (read-only), **measure** its reliability against the eval suite, and **expand** its authority only as evidence supports it. This is the read → recommend → execute ladder the repo's wedge proposals already use — now with the principle named: autonomy proportional to risk *and* to demonstrated reliability. Low-risk, reversible actions automate early; high-impact, irreversible actions stay approval-gated until the evidence clears them. [`trust-surface-design.md`](trust-surface-design.md) works the same ladder from the *adoption* side (launch over-gated, widen on override rate); this framework is the *control-plane* side (what the harness enforces at each rung).

## How to deploy this framework

- **In a system-design round** ("design an agent that reroutes shipments at 99% on-time across 500 warehouses"): name the control-plane frame, then walk the components — but spend your depth on the four the junior candidate forgets (state, re-planning, outcome verification, recovery). That's the long-horizon signal.
- **In an architecture review:** for every action the agent takes, ask "where is this state persisted, how is it verified, and what happens when it fails halfway?" Ungated, unverified, unrecoverable actions are findings.
- **As the organizing layer:** when the other frameworks feel like scattered production-thinking checklists, this is the frame that unifies them — they are all capabilities of the harness.

## Quick reference

```
FRAME: the harness is the control plane between a PROBABILISTIC model
       and DETERMINISTIC enterprise systems.

COVERED ELSEWHERE: context · tools · permissions · observability · evaluation
THE FOUR TO GO DEEP ON (long-horizon):
  1. State      -> explicit task record, not conversation history; resume from step N
  2. Planning   -> goal→plan→execute→verify→update loop; re-plan without losing progress
  3. Verify     -> verify external SIDE EFFECTS, not the agent's claim
  4. Recovery   -> checkpoints · idempotency · retry/timeout · escalation

EARN AUTONOMY: start read-only, measure reliability, expand authority on evidence.
GOAL: not perfect steps — a system resilient to imperfect steps.
```
