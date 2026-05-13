# Framework 4: Workflow Decomposition (drawing agent boundaries)

> A 5-step method for going from a manual workflow to a set of agents. The boundaries aren't arbitrary; they follow failure modes.

## The 5-step method

| Step | What you do | Output |
|---|---|---|
| 1. Map the manual workflow as a swimlane | Draw the human's current process step by step, including decision points and handoffs | Linear sequence of 8-15 steps |
| 2. Identify decision points vs execution points | Decision = "should I do X or Y?". Execution = "do X." | Two lists: ~3-5 decisions, ~5-10 executions |
| 3. Group execution points by data + tier requirements | Steps that read from the same source and need the same model tier collapse into one agent | First cut at agent boundaries |
| 4. Add a critic agent at every irreversible step | Anywhere the output goes to a downstream system, add a deterministic critic in front | Compliance and audit layer |
| 5. Add routing for confidence-low cases | Decide which agent's output gets escalated, to whom | Trust-level structure |

## The principle behind it

**Decompose by failure mode, not by feature.** Agent boundaries go where the failure modes change. An MNPI scrubber is separate from a drafter because regulatory leak is irreversible; bad synthesis is reversible. Same with citation verification vs tone judgment.

## Worked example (Helix Capital earnings note)

### Step 1 — Manual workflow swimlane

Rachel's current process the morning after an earnings call:
1. Read prior quarter's note + consensus
2. Listen to call live (or read transcript after)
3. Extract KPIs (revenue, segment results, guidance)
4. Note tone shifts vs prior quarter
5. Draft note structure (headline + key takeaways + KPI table + tone commentary)
6. Verify every number against transcript or filings
7. Compliance self-check (no MNPI, no position-sizing, no M&A speculation)
8. Send to PM + trader desk

### Step 2 — Decisions vs executions

- **Decisions** (2): "Is this MNPI?" (binary, deterministic); "Does tone shift warrant a flag?" (graded)
- **Executions** (6): read prior, extract KPIs, draft structure, verify numbers, compliance check, send

### Step 3 — Group by data + tier requirements

- Extract KPIs (structured, transcript + consensus) → Haiku-tier Extractor
- Draft note (synthesis, transcript + KPIs + prior note) → Sonnet-tier Synthesizer
- Verify numbers (deterministic comparison) → Compliance critic

### Step 4 — Add critics at irreversible steps

- Before any LLM call: MNPI Scrubber (deterministic). Fund-shutting if missed.
- Before send: Citation Verifier (deterministic). Wrong number = trading loss.
- Before send: Tone Supervisor (LLM-as-judge). Soft errors the Drafter missed.

### Step 5 — Routing for confidence-low

- Drafter confidence threshold → Rachel's queue
- Tone Supervisor flag → Rachel review
- Compliance Critic flag → escalate to Mei

**Output**: 7 agents, derived mechanically from the 8-step workflow + 2 decisions + 4 critic / routing additions.

## The probe this defends against

When the interviewer asks "how did you decide on these agents", you say:

> "I decomposed by failure mode, not by feature. Step 1: mapped Rachel's manual workflow. Step 2: identified 2 decisions and 6 executions. Step 3: grouped executions by data + tier. Step 4: added a critic at every irreversible step. Step 5: added routing for confidence-low cases. That's how we got to 7 agents — mechanically, not by guessing."

## Quick reference

```
WORKFLOW DECOMPOSITION:
  Step 1: Map the manual workflow as a swimlane (8-15 steps)
  Step 2: Identify decision points (~3-5) vs execution points (~5-10)
  Step 3: Group executions by data + tier requirements
  Step 4: Add a critic at every irreversible step
  Step 5: Add routing for confidence-low cases

  Output: agent count and boundaries justified by failure mode
```
