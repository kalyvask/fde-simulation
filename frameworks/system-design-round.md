# System Design Round — Method, AI-Architecture Depth & Drills

> The FDE loop is roughly half judgment and half technical, and the technical half has a signature round: a 60-minute system-design interview where you architect a real AI deployment under real customer constraints (VPC, HIPAA, identity, cost, latency, failure modes). This framework gives you the round *method*, the *AI-architecture depth* the round probes (the topics candidates most often can't go deep on), and a *drill set*.
>
> Source note: the round breakdown and several drill archetypes are adapted from the open FDE interview guide in [`aishwaryanr/awesome-generative-ai-guide`](https://github.com/aishwaryanr/awesome-generative-ai-guide) (see [`../READING.md`](../READING.md)); the method framing and the mapping to this repo's other frameworks are original.

## Part 1 — The round method

The failure mode this round screens for is the same one the decomposition round screens for: solving before scoping. The method:

1. **Start from requirements, not architecture.** Pin five things out loud before drawing anything: accuracy bar, latency budget, data sensitivity/compliance, scale, and the escalation/fallback policy. "What's the acceptable wrong-answer rate, and what happens when we're wrong?" is a stronger opening than a boxes-and-arrows diagram.
2. **Propose a thin walking skeleton first.** The MVP that runs end-to-end on one slice, then harden. Designing the perfect system with no MVP sequencing is the single most common rejection in this round.
3. **Name trade-offs explicitly and pick.** Every choice gives something up. Say what, and commit. "I'd use a smaller model for routing and pay the accuracy cost because the latency budget is 200ms" beats an un-defended choice.
4. **Cover the four things candidates skip:** identity/permissions, observability (log / alert / dashboard), rollback, and **evaluation as release infrastructure** (the eval suite is what gates a deploy, not an afterthought).

This maps onto the repo's existing meta-structures — **DASME** (Define scope / Architect / Specify data+models / Map metrics / Edge cases) and **C.A.S.E.** (Clarify / Architect / Solve / Evaluate) in [`consulting-frameworks.md`](consulting-frameworks.md). Use one of those as the spine; this framework is the AI-specific depth you hang on it.

**The frame to name out loud: the system you're designing is a control plane** — the boundary between a probabilistic model and deterministic enterprise systems. The full component model (context, state, tools, verification, recovery) and the long-horizon depth live in [`agent-harness.md`](agent-harness.md); in the design round, naming the frame ("the model reasons; the harness constrains, persists, and verifies it") reframes a boxes-and-arrows question as an architecture-judgment one. Its **earn-autonomy** principle — start read-only, measure reliability, expand authority on evidence — is the answer to the autonomy question.

## Part 2 — The AI-architecture depth the round probes

These are the four topics where candidates go shallow. Going one level deeper on each is the differentiator.

### RAG — pipeline and failure modes
Know the pipeline end to end: chunk → embed → retrieve → (rerank) → assemble context → generate → cite. But the senior signal is the **failure modes** — being able to answer *"why might a model do worse with retrieved context than with none?"*:
- Low-precision retrieval injects noise the model then anchors on
- Conflicting or outdated documents (the model can't tell which is current)
- Chunk boundaries split the answer across two chunks, so neither is sufficient
- Top-k too high dilutes signal; "lost in the middle" buries the relevant chunk
- The model over-trusts retrieved text — including any indirect injection in it (see [`agent-exploitation-taxonomy.md`](agent-exploitation-taxonomy.md))

Fixes: reranking, better chunking, lower top-k, dedup/recency filters, and a retrieval-quality eval (precision@k on a labeled set) as its own metric.

### Agent tool design + MCP
*"How do you design tools so an agent uses them reliably?"* — clear single-purpose tools, few over many, typed and validated arguments, minimal parameters, idempotent side effects, and **error messages the model can act on** ("amount exceeds limit of 500" not "400 Bad Request"). This is the read/write discipline from [`agent-shapes-catalog.md`](agent-shapes-catalog.md) at the tool boundary.

**MCP (Model Context Protocol)** is the emerging standard for exposing tools, resources, and prompts to a model across clients. Why it matters for an FDE: it standardizes plugging an agent into a customer's systems without bespoke glue per integration — and it widens the indirect-injection surface, because every tool result is untrusted input.

MCP answers *"I need access to this capability"*; **A2A** answers *"I need another agent to own this task."* Knowing which boundary a requirement calls for — and defending why most of them are tools — is [`orchestration-topology.md`](orchestration-topology.md).

### Trajectory evaluation
Pass^k on the *final output* (see [`4-dimensional-testing.md`](4-dimensional-testing.md)) is necessary but not sufficient for agents. **Trajectory evaluation** scores the *steps*: did the agent call the right tools in the right order, recover from a tool error, and avoid unnecessary or unsafe actions? A correct answer reached through a wrong path (it exfiltrated data, then summarized correctly) is still a failure. Evaluate both the destination and the route.

### Cost-latency-quality
Latency is covered in [`production-debugging.md`](production-debugging.md); the third axis is **cost**, and the round often asks for the levers to cut an LLM bill without cutting quality:
- Smaller/cheaper model for routing, extraction, and classification; reserve the big model for synthesis
- Prompt caching and semantic caching
- Shorter prompts / prune retrieved context; cap output tokens
- Lower top-k; batch where latency allows
- Route by difficulty (cheap model first, escalate on low confidence)
- Cut unnecessary agent loops (the biggest hidden cost)

**Cutting cost is half of it; proving it is the other half.** An FDE has to show the customer the deployment pays for itself, so know the *measurement* layers, not just the levers:
- **Unit economics, not total cost.** Cost per user / per 1K requests / per 1M tokens, tokens per request, and prompt-cache hit rate. Total spend rising is fine if cost *per outcome* is falling because adoption grew — unit economics separate "more usage" from "less efficient." Attribute every request (tool / agent / user / tenant / model) or none of this is possible.
- **Outcome-denominated cost** is the number that survives a skeptical exec: cost per merged PR, per review, per resolved alert — paired with a quality signal (revert rate, F1, MTTR), because a cheaper cost-per-outcome at worse quality is *not* cheaper. This is the cost-side analogue of "measure business-task success, not model accuracy" ([`4-dimensional-testing.md`](4-dimensional-testing.md)).
- **Driver decomposition** answers *why* the bill moved with no hand-waving: Δcost ≈ adoption × engagement (requests/user) × input tokens/request × output tokens/request, reconciling to the total with **no unexplained residual**. "Cost up 30%" is useless; "up 30% = +18% adoption, +9% requests/user, +3% longer outputs, ~0 residual" is exec-review credible.
- Re-run this before/after a **model migration** — the migration is a win only if outcome-denominated cost fell *and* the quality signals held.

### Long-horizon task state & recovery
The design round increasingly asks about the **long-horizon worker** that owns an outcome across hours and hundreds of steps (rerouting shipments, reconciling ledgers, running a migration), where failures are inevitable and the goal is a system *resilient to imperfect steps*. That whole layer — explicit task state, checkpoints, idempotency, re-planning, and outcome verification — is its own framework: [`agent-harness.md`](agent-harness.md). Reach for it when the prompt is long-horizon; this repo's cases are deliberately short-horizon and don't exercise it.

## Part 3 — Drill set

Six prompts. For each: run the Part 1 method, reach for the Part 2 depth, and name what you'd measure. (Originals, in the shape of real design-round prompts.)

1. **Compliance RAG.** Design a private, VPC-deployed RAG system for a healthcare customer under HIPAA over ~50M documents. *Probes:* identity/permission-aware retrieval, PII handling, the accuracy-vs-latency bar, eval on a labeled clinical set.
2. **Fragmented ingestion.** Design ingestion + transformation for ~12 retail data sources with no clean schema, feeding a forecasting model. *Probes:* the messy-data reality, schema reconciliation, data-quality gates. (Rhymes with the Calder discovery data-pull.)
3. **Agent eval harness.** Design an eval harness for an agent that reroutes shipments, targeting 99% on-time delivery. *Probes:* trajectory eval, weighted failure cost, pass^k, adversarial cases — this is [`4-dimensional-testing.md`](4-dimensional-testing.md) applied live.
4. **Latency budget.** A naive RAG endpoint returns in 1.5s; get it under 100ms. What changes? *Probes:* the latency decomposition tree — send them to [`production-debugging.md`](production-debugging.md) for the full method (retrieval vs inference vs tool spans, caching, smaller model, streaming).
5. **Prompt release safety.** Design how you version, A/B test, and roll back prompts in production. *Probes:* evaluation as release infrastructure, observability, rollback — the four things candidates skip.
6. **Observability architecture.** Design observability for an agent system: what do you log, alert on, and put on a dashboard? *Probes:* immutable audit trace, per-agent latency/cost, drift detection, the named operational owner (the repo's audit-trace standard).

## How to deploy this framework

- **In the system-design round:** open with requirements (Part 1), spine it on DASME or C.A.S.E., and when the interviewer probes AI depth, go one level deeper using Part 2 rather than hand-waving.
- **As practice:** run the Part 3 drills on a whiteboard against a 45-60 min clock with a partner playing the interviewer; the standalone [`../tools/agent_design_practice.html`](../tools/agent_design_practice.html) works as the canvas.
- **At handoff / in the ROI conversation:** hand the customer outcome-denominated cost (cost per outcome + quality held), not a raw token bill — and lead with it if a skeptical exec asks "is this worth it," backing it with the driver decomposition.

## Quick reference

```
METHOD:
  1. Requirements first: accuracy bar / latency budget / data sensitivity /
     scale / escalation-fallback policy
  2. Thin walking-skeleton MVP, then harden
  3. Name each trade-off and PICK
  4. Cover the 4 skipped: identity · observability · rollback · eval-as-release
  (spine it on DASME or C.A.S.E.)

DEPTH (go one level deeper than the candidate who fails):
  RAG           -> pipeline + failure modes (why retrieved context can hurt)
  Tools + MCP   -> single-purpose, typed args, actionable errors; MCP standardizes
  Trajectory eval -> score the steps, not just the final output
  Cost          -> CUT: small model for routing, caching, prune context, cut loops
                   PROVE: unit economics + cost-per-OUTCOME (at held quality);
                   decompose Δcost = adoption × engagement × input × output, no residual

FAILURE MODE THAT REJECTS YOU: a perfect design with no MVP sequencing.
```
