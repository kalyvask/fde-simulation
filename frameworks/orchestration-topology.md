# Framework 17: Orchestration Topology

> [Workflow decomposition](workflow-decomposition.md) tells you where the boundaries go. [Agent shapes](agent-shapes-catalog.md) tells you what each agent is. This tells you how they compose — and, more often than candidates expect, why the answer is one agent with good tools.

## The failure this framework prevents

Two opposite failures, and interviewers probe for both.

**The agentic monolith.** One agent accumulates dozens of tools, an ever-growing instruction block, several permission levels, a large context, and responsibilities spanning multiple business domains. Like a software monolith, it becomes hard to maintain, test, secure, evaluate, and evolve. Nobody can say which instruction is load-bearing, and every eval regression is a bisect across one enormous prompt.

**Multi-agent theater.** The candidate draws seven agents because seven agents look sophisticated. This is the [Unforgivable](essentials-unforgivables.md) of chasing trendy solutions, and it fails on the trade-off below.

**Multi-agent architecture does not eliminate complexity. It moves complexity from inside the agent into the orchestration layer.** With one agent you manage prompts, tools, context, and permissions. With several you manage all of that *plus* delegation, coordination, context sharing, state, failure handling, governance, and observability. That's a real bill, and it comes due in week 3 when something breaks and nobody can tell which agent decided what.

So the question is never *"how do we use more agents?"* It's:

> **Where does creating an independent reasoning boundary make the system easier to build, govern, evaluate, and operate?**

## The boundary test

Add a reasoning boundary when at least two of these are true. One alone is usually not enough.

| Signal | Why it justifies a boundary |
|---|---|
| **Different failure mode** | The existing [decomposition principle](workflow-decomposition.md) — regulatory leak and bad synthesis fail differently and need different gates |
| **Different permissions** | The retriever doesn't need write access; the policy reasoner doesn't need every customer record; the proposer doesn't need execute authority |
| **Different evaluation criteria** | If you'd score this capability on a different rubric, it wants its own eval suite and its own release gate |
| **Different model tier** | Extraction on Haiku, synthesis on Sonnet — a boundary makes the tier decision explicit and defensible |
| **Different lifecycle / owner** | A capability that changes weekly shouldn't be coupled to one that changes quarterly, especially across team boundaries |
| **Different business domain** | Billing policy and returns policy have different owners, different rules, and different rates of change |

If none of these hold, you have a tool, not an agent. Add it to the existing agent and move on.

## The six patterns

| Pattern | Shape | Use when | Cost |
|---|---|---|---|
| **Router / triage** | Classify, then hand to one specialist | Requests fall into clean, disjoint categories | Mis-routes are silent; needs a fallback class |
| **Supervisor / manager** | One orchestrator owns the interaction, delegates tasks, assembles the answer | Enterprise workflows where control must stay centralized and one voice reaches the user | Supervisor becomes the new monolith if it also does the work |
| **Sequential** | Fixed order; each stage feeds the next | Regulated or predictable processes where order is the control | Latency is the sum; one slow stage blocks all |
| **Parallel / fan-out** | Independent tasks run concurrently, results joined | Tasks share no dependency and latency matters | Partial-failure semantics: what does the join do when one branch fails? |
| **Generator–verifier** | One agent produces, another evaluates against explicit criteria | Irreversible or reputation-bearing output with a checkable bar | Doubles cost per item; the verifier needs its own calibration |
| **Hierarchical** | Orchestrators coordinating orchestrators | Large orgs where domains own their own agents, policies, and systems | Debugging, governance, and ownership get materially harder |

Patterns compose. Most real systems are a supervisor with a sequential spine and a couple of generator–verifier pairs hanging off the irreversible steps.

## What the reference prototypes actually use

Worth being concrete, because "which pattern did you use" is a live probe and the honest answer here is instructive.

Both prototypes are a **sequential pipeline with a deterministic gate in front and generator–verifier pairs at the irreversible steps**. Helix runs MNPI Scrubber → Intake → KPI Extractor → Note Drafter → Tone Supervisor → Citation Verifier → Compliance Critic. The Scrubber fires *before any LLM call*, so a watch-list hit halts the run at zero token spend. Drafter→Tone Supervisor and Drafter→Citation Verifier are generator–verifier pairs.

There is deliberately **no router, no fan-out, and no A2A** in v1. That is a defensible choice, not an omission:

- The workflow has one entry point and a fixed regulatory order, so a router would add a mis-route failure mode and buy nothing.
- Fan-out would cut latency on a workflow whose SLA is "before market open," not milliseconds — the wrong thing to optimize.
- Every stage is owned by the same team on the same release cadence, so the lifecycle signal in the boundary test doesn't fire.

**Where an interviewer will push:** at 10x volume with several note types, the intake step earns a router; if consensus and filings lookups are independent, they earn a fan-out. Say what would *change your mind*, and the answer reads as judgment rather than defensiveness.

## MCP vs. A2A — capability or reasoning boundary?

The question underneath every orchestration decision:

> **Does this task need a capability, or another reasoning boundary?**

- **MCP (Model Context Protocol)** — *"I need access to this capability."* Standardized access to tools, data, and systems. If the task is deterministic (retrieve a record, call an API, execute an operation), it's a tool. You don't need another agent. Tool-design discipline and the injection surface MCP widens are in [`system-design-round.md`](system-design-round.md).
- **A2A (agent-to-agent)** — *"I need another agent to own this task."* Delegating an *objective* to an autonomous agent that reasons, holds its own context, chooses its own capabilities, and reports completion.

They're complementary, not competing: an agent that receives work over A2A still uses MCP to reach the systems it needs. The FDE-relevant point is that they're different boundaries with different blast radii. A tool call is bounded by its signature; a delegated objective is bounded only by the contract you wrote for it.

## Delegation contracts

Once agents delegate to agents, *"figure this out"* is not an interface. Every delegated task needs six fields:

| Field | The question | Failure if you skip it |
|---|---|---|
| **Objective** | What outcome, stated so completion is checkable | The sub-agent optimizes something adjacent |
| **Context** | The minimum needed — nothing more | Context bloat, cost, and leaked data across boundaries |
| **Permissions** | What it may read, write, and execute | The sub-agent inherits the caller's full authority |
| **Expected output** | Shape and schema of the result | The caller parses prose and guesses |
| **Completion criteria** | How both sides know it's done | Silent partial completion, reported as success |
| **Failure behavior** | Retries, timeout, escalation target | Infinite loops, or a failure that vanishes |

Four rules that go with it:

1. **Pass only the context required.** Context is a permission — this is least privilege from [`agent-exploitation-taxonomy.md`](agent-exploitation-taxonomy.md) applied to data rather than tools.
2. **Give every task a single owner.** Shared ownership across agents means no ownership at failure time.
3. **Bound recursive delegation.** A depth limit, or the graph is unbounded and so is the bill.
4. **Separate instructions from untrusted data.** A delegated payload carrying retrieved content is an injection vector; the delegation contract is where you fence it.

**More autonomy requires stronger contracts.** Autonomy and contract strength move together, or the system is under-specified exactly where it's most dangerous.

## Governance and observability

Two layers that become mandatory the moment agents take actions rather than answer questions.

**Governance — what agents are *allowed* to do.** Permissions, tool access, approval gates, delegation limits, auditability. The load-bearing separation:

> The model proposes what should happen. The policy layer determines what is allowed to happen.

An agent that decides its own authority has no governance, however well it reasons. This is the deterministic-gate discipline from [`agent-exploitation-taxonomy.md`](agent-exploitation-taxonomy.md) and the publish gate from [`trust-surface-design.md`](trust-surface-design.md), stated as an architectural layer rather than a per-action rule.

**Observability — what actually happened.** Multi-agent changes the debugging question:

> From *"what did the model say?"* to *"what happened across the execution graph?"*

That is a different instrumentation requirement, and it's why the repo's audit-trace standard is per-agent rather than per-run: you need the decision, the inputs, the delegation edges, and the policy verdicts, or a post-incident review can't answer which boundary failed. [`production-debugging.md`](production-debugging.md) has the latency decomposition; the same span discipline carries the causal one.

## The decision ladder

```
Need a deterministic capability?      -> Tool / MCP
Need specialized reasoning?           -> Agent (run the boundary test)
Need autonomous delegation?           -> A2A + a delegation contract
Need multiple agents coordinated?     -> Orchestration (pick a pattern)
Can agents take consequential actions? -> Governance (policy layer)
Need to know what happened?           -> Observability (execution graph)
```

Walk it top-down and stop at the first rung that answers the problem. Most enterprise problems stop at rung one or two.

## The probe this defends against

When the interviewer asks *"why not one agent?"* — or the inverse, *"why not split this up?"* — the weak answer treats agent count as a design goal. The strong answer:

> "I don't optimize for agent count. I add a reasoning boundary only where at least two things differ — failure mode, permissions, eval criteria, model tier, lifecycle, or domain. On Helix, MNPI and drafting differ on all six, so they're separate; extraction and drafting differ on tier and eval, so they're separate. Everything else is a tool, not an agent. The topology is a sequential pipeline with a deterministic gate in front and generator–verifier pairs at the irreversible steps — no router, because there's one entry point and a fixed regulatory order, so a router would add a mis-route failure mode and buy nothing. What would change that: several note types at 10x volume earns a router at intake. And I'd say plainly that multi-agent doesn't remove complexity, it moves it into orchestration — which is why the audit trace is per-agent and every delegated task has an owner, a permission scope, and a failure behavior."

## Quick reference

```
FIRST QUESTION: capability or reasoning boundary?
  Deterministic (retrieve / call / execute) -> TOOL (MCP)
  Needs to reason, hold context, choose      -> AGENT (A2A)

BOUNDARY TEST (need >=2 to justify a new agent):
  different failure mode | permissions | eval criteria
  model tier | lifecycle-owner | business domain
  ...none? It's a tool. Add it to the existing agent.

PATTERNS:
  Router      simple, disjoint categories
  Supervisor  centralized control, one voice to the user
  Sequential  order IS the control (regulated)
  Fan-out     independent tasks, latency-bound
  Gen-verify  irreversible output with a checkable bar
  Hierarchical  domains own their own agents (governance cost is real)

DELEGATION CONTRACT (all six, every time):
  Objective -> Context -> Permissions -> Expected Output
            -> Completion Criteria -> Failure Behavior

GOVERNANCE:    model PROPOSES, policy layer DISPOSES
OBSERVABILITY: "what did the model say?" -> "what happened across the graph?"

Senior move: multi-agent doesn't remove complexity, it MOVES it into orchestration.
Sometimes the right answer is still one agent with good tools.
```

## See also

- [`workflow-decomposition.md`](workflow-decomposition.md) — where the boundaries go (bottom-up, from the manual workflow); this framework is the composition layer above it
- [`agent-shapes-catalog.md`](agent-shapes-catalog.md) — what each agent *is*; the Router shape is the deterministic implementation of the router pattern
- [`trust-surface-design.md`](trust-surface-design.md) — the publish gate and permission inheritance are the governance layer at the user boundary
- [`agent-exploitation-taxonomy.md`](agent-exploitation-taxonomy.md) — least privilege and the untrusted-input rule, which delegation contracts enforce across boundaries
- [`system-design-round.md`](system-design-round.md) — tool-design discipline, MCP's injection surface, and trajectory evaluation (which is how you eval a graph, not a call)
