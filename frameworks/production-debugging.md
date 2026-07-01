# Production Debugging — Components, Latency & Log Triage

> An operate-time framework, built around the most common FDE case there is: "deploy a customer-support agent for a client. What components does it have? The client says it's too slow — what's the root cause? Here are the request logs — what do you look for?" That's three questions in sequence, and they share one substrate: the component map. You debug against the architecture. This file gives you the reference architecture, the latency decomposition, and a worked log-triage drill.
>
> Pairs with [`agent-shapes-catalog.md`](agent-shapes-catalog.md) (the shapes these components are built from) and [`4-dimensional-testing.md`](4-dimensional-testing.md) (production observability as a test dimension).

## Part 1 — Reference architecture: a customer-support agent

When asked "what components does the agent have," don't list model + prompt. Walk the request path. A production CS agent is a pipeline of specialized components, each with one job and its own failure and latency profile:

| # | Component | Job | Deterministic or LLM |
|---|---|---|---|
| 1 | Gateway / auth | Authenticate the user, load their entitlements/tenant | Deterministic |
| 2 | Intake / PII scrub | Normalize the message; redact PII before it hits the model | Deterministic |
| 3 | Router / classifier | Intent + urgency; route to self-serve, agent, or human | LLM or small classifier |
| 4 | Retriever | Pull relevant KB articles / account context (RAG) | Deterministic (vector + keyword) |
| 5 | Context builder | Assemble the prompt: policy, retrieved docs, account state | Deterministic |
| 6 | Drafter | Generate the response | LLM |
| 7 | Policy / compliance critic | Check the draft against policy (refunds, promises, tone) | Deterministic + LLM-as-judge |
| 8 | Tool executor | Take gated actions (order lookup, refund, ticket update) | Deterministic, per-tool authz |
| 9 | Escalation / HITL | Hand off to a human when confidence or risk fails a threshold | Deterministic gate |
| 10 | Response gate | Final output scan (PII, secrets, forbidden content) before send | Deterministic |
| 11 | Observability / trace | Immutable per-request trace: inputs, spans, latencies, decisions | Deterministic |

The senior signal: naming the **deterministic gates** (2, 7, 8, 9, 10) as separate from the **LLM synthesis** (6) — the same hybrid discipline the rest of the repo teaches. The trace (11) is what makes Parts 2 and 3 possible; you can't debug what you didn't instrument.

## Part 2 — Latency root-cause: the decomposition tree

"It's slow" is not a diagnosis. Decompose end-to-end latency by component and find the tail. The buckets, roughly in request order:

| Bucket | Where the time goes | How to confirm | Common fix |
|---|---|---|---|
| Network / ingress | Client↔server round trips, TLS, payload size | Compare server-side span sum vs client-observed total | CDN/edge, smaller payloads, keep-alive |
| Auth / entitlement | Slow authz lookup or downstream identity call | Auth span duration in the trace | Cache entitlements per session |
| Retrieval | Vector search + KB fetch; large top-k; cold index | Retrieval span; top-k size; index warm state | Lower top-k, cache hot docs, warm the index |
| Model inference | **Time-to-first-token + generation**; model size; output length | TTFT vs total generation in the trace | Smaller/faster model for routing; stream tokens; cap output length |
| Tool / API calls | External systems (order DB, payments); **sequential vs parallel** | Per-tool span; are calls serialized? | Parallelize independent calls; timeout + cache |
| Orchestration overhead | Agent loops, re-planning, retries | Step count per request; retry count | Cap steps; fix the retry trigger |
| Cold start | First request after a scale-to-zero idle | Latency correlated with a preceding idle gap | Warm pool / min replicas |
| Queueing / concurrency | Requests waiting on a saturated worker pool or rate limit | Queue-wait span; concurrency vs limit | Scale workers; raise/shard rate limits |
| Guardrail / critic passes | Extra LLM calls for the critic or a re-draft loop | Critic span; re-draft count | Make the critic deterministic; single-pass |

**The method, said out loud:** "First I'd look at whether the p50 is slow or only the p99 — a slow p50 is systemic (model, retrieval, cold start); a slow tail is usually queueing, retries, or a fallback to a bigger model. Then I'd decompose one slow trace by span and find which component owns the time. Averages lie; I'd work off p95/p99, not the mean." Naming p50-vs-tail and averages-lie is the differentiator.

## Part 3 — Log / trace triage drill

**Prompt (what an interviewer hands you): "Here are per-request trace logs. The client says the agent got slow this week. What do you look for?"**

Sample (each line is one request's span breakdown, ms):

```
req  total  auth  retrieval  ttft  gen   tools           steps  model
001   1,420  30    180        220   640   order:150        1     sonnet
002   1,380  28    170        210   610   order:160        1     sonnet
003   9,850  31    175        215   630   order:145        1     sonnet   <-- outlier
004   1,510  35    240        230   660   order:160        1     sonnet
005  14,200  29    182        980   5,900 order:150,kb:120 4     opus     <-- outlier
006   1,460  30    190        225   640   order:155        1     sonnet
007   8,900  33    170        —     —     —                6     sonnet   <-- outlier
```

**What you look for (the reference checklist):**

1. **p50 vs tail.** p50 is ~1.4s and healthy; only some requests blow up. So it's a **tail problem**, not systemic. Don't touch the model or retrieval baseline.
2. **Decompose each outlier by span:**
   - **req 003** — every span is normal but `total` is 9.8s. The time is *unaccounted* by the spans, which means it's *outside* the instrumented work: **queue wait** or a cold start. Check concurrency vs worker limit at that timestamp.
   - **req 005** — `model=opus` (not sonnet), `gen=5,900ms`, `steps=4`. This request **fell back to a bigger model and looped**. Root cause is an escalation/fallback trigger firing when it shouldn't, or a re-plan loop. Both the model swap and the step count are the smoking gun.
   - **req 007** — `steps=6`, and `ttft/gen/tools` are blank (`—`): the request **never completed a generation** — likely a **retry storm** or a tool timeout causing re-planning. Look at the retry/timeout logs for that request.
3. **Correlate to "this week."** What changed? A deploy, a prompt change that raised the fallback rate, a KB re-index that cooled the cache, a traffic increase that saturated the pool. The logs point at *which* component; the change-log tells you *why now*.
4. **What's missing from the logs that you'd add:** queue-wait span, retry count, cache hit/miss, and cost per request. If req 003's slowness is unaccounted, the instrumentation itself has a gap — and "add the missing span" is a legitimate answer.

**The one-sentence diagnosis:** "Baseline is healthy; the tail is three distinct causes — queue/cold-start (003), an over-eager model-fallback-and-loop (005), and a retry storm (007) — so I'd fix the fallback trigger and the retry policy first since those are self-inflicted, then add queue-wait and retry-count to the trace to confirm 003."

That answer — separating baseline from tail, attributing each outlier to a *named component*, and flagging the instrumentation gap — is what a senior FDE sounds like on this case.

## How to deploy this framework

- **"What components?"** → walk the 11-row request path (Part 1), grouping deterministic gates vs LLM synthesis.
- **"Why is it slow?"** → p50 vs tail first, then decompose one trace by the Part 2 buckets, then correlate to what changed this week.
- **"Read these logs."** → run the Part 3 checklist: baseline vs outliers, attribute each outlier to a span/component, name the missing instrumentation.

## Quick reference

```
COMPONENTS (debug against these):
  gateway/auth · PII-scrub · router · retriever · context-builder ·
  drafter(LLM) · policy-critic · tool-executor · escalation/HITL ·
  response-gate · trace
  (name the deterministic GATES separately from the LLM drafter)

LATENCY ROOT-CAUSE:
  1. p50 slow = systemic (model / retrieval / cold start)
     tail slow = queueing / retries / model-fallback
  2. decompose ONE trace by span; find the component that owns the time
  3. correlate to what changed this week (deploy, reindex, traffic)
  work off p95/p99 — averages lie

LOG TRIAGE:
  baseline vs outliers -> attribute each outlier to a named span ->
  flag the missing instrumentation (queue-wait, retries, cache, cost)
```
