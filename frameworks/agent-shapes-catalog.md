# Framework 5: Agent Shapes Catalog

> Don't invent agent types. There are 7 standard shapes; pick from the catalog. Every enterprise agent workforce is some combination of these.

## The catalog

| Shape | Job | Typical tier | Det / LLM | When to use |
|---|---|---|---|---|
| **Extractor** | Pull structured data from unstructured input | Haiku | Hybrid (regex when possible) | Invoice fields, KPI extraction, entity recognition |
| **Classifier** | Route input to one of N paths | Haiku or rules | Deterministic if possible | Intake triage, category routing, queue selection |
| **Synthesizer / drafter** | Produce natural-language output from structured input | Sonnet or GPT-4o | LLM | Drafts, summaries, explanations, recommendations |
| **Critic / judge** | Evaluate another agent's output | Sonnet | LLM-as-judge with calibration | Faithfulness check, tone check, quality check |
| **Compliance critic** | Enforce rules (regulatory, policy, business) | Deterministic | Rules-based | Kill-criteria enforcement, MNPI scrub, threshold checks |
| **Router** | Deterministic handoff logic between agents | Deterministic | Rules-based | Escalation, fallback, parallel fan-out |
| **Auditor** | Produce immutable, examiner-readable logs | Deterministic | Deterministic | Audit trace, reasoning chain, citation chain |

## Why this catalog matters

Three reasons the catalog beats "design from scratch":

1. **Consistency across cases**. Whether you're building for insurance claims, hedge-fund research, or support automation, the shapes are the same.
2. **Failure-mode coverage**. The 7 shapes together cover the failure modes that matter: extraction errors, routing errors, synthesis errors, judgment errors, compliance violations, audit failures.
3. **Tier discipline**. Each shape has a default tier. You only deviate from the default if you can defend the deviation.

## How to deploy it

1. After workflow decomposition (framework 4), you have N agent boundaries
2. For each boundary, pick a shape from the catalog
3. The shape tells you the default tier (Haiku / Sonnet / deterministic)
4. If you deviate from the default, defend the deviation

## Worked example (Helix Capital, 7 agents)

| Helix agent | Shape | Tier | Det / LLM | Why |
|---|---|---|---|---|
| 1. MNPI Scrubber | Compliance critic | Deterministic | Rules | Fund-shutting if missed; reliability is non-negotiable |
| 2. Intake classifier | Classifier | Haiku | Det-leaning | Routes by ticker / sector / call type |
| 3. KPI Extractor | Extractor | Haiku | Hybrid (regex + LLM for unstructured) | Reliability over creativity |
| 4. Note Drafter | Synthesizer / drafter | Sonnet | LLM | Synthesis is where LLMs uniquely win |
| 5. Tone Supervisor | Critic / judge | Sonnet | LLM-as-judge with SubjECTive-QA calibration | Soft errors the Drafter missed |
| 6. Citation Verifier | Compliance critic | Deterministic | Rules + regex | Hallucinated number = irreversible reputational hit |
| 7. Audit Trace Generator | Auditor | Deterministic | Deterministic | Examiner-readable log; reliability-critical for SEC review |

## The probe this defends against

When the interviewer asks "why these agents":

> "I picked from the 7-shape catalog by failure-mode boundary. Compliance critics around the irreversible failures (MNPI, citations). Synthesizer for the natural-language work. Auditor for examiner-readable logging. Configuration, not fine-tuning. The shapes are domain-portable."

## When to deviate from the default tier

The default tiers in the catalog are good for most cases. Deviate only when:
- **Cost prohibitive**: drop Sonnet to Haiku on a non-critical agent
- **Latency budget**: drop Sonnet to Haiku where speed > nuance
- **Reliability-critical**: drop LLM to deterministic where errors are irreversible

Don't deviate just to look sophisticated. "Sonnet because the drafter is synthesis-heavy and volume is 80 notes / quarter" beats "Sonnet because it's the best model."

## Quick reference

```
AGENT SHAPES (7 total):
  Extractor          → Haiku, hybrid
  Classifier         → Haiku or rules, deterministic-leaning
  Synthesizer        → Sonnet or GPT-4o, LLM
  Critic / judge     → Sonnet, LLM-as-judge with calibration
  Compliance critic  → Deterministic, rules
  Router             → Deterministic, rules
  Auditor            → Deterministic, deterministic

Senior move: name the shape before the agent.
  "I'd use a Classifier shape for intake" beats "I'd build an intake agent."
```
