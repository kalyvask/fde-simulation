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

## Deterministic vs non-deterministic at the OUTPUT SCHEMA level (not just the agent level)

The agent-level split (this agent is deterministic, that one is LLM) is the obvious cut. The sharper cut is at the **output schema** level:

- **The output schema itself is deterministic.** The agent must produce a structured output with a fixed set of fields (e.g., "50 columns in this exact format"). The schema is hard-coded; the validation that the output matches the schema is deterministic.
- **The input parsing IS non-deterministic.** Customer-submitted emails, free-text descriptions, attached PDFs — these require LLM parsing to extract the structured fields that the deterministic output schema expects.
- **The human-in-the-loop sits at the seam.** A confidence-low parse routes to a human to confirm the extracted fields before they hit the deterministic output schema.

### Worked example: parsing unstructured customer requests into a fixed schema

A common enterprise pattern: customers submit requests in variable formats (email body, PDF attachment, form-field). The downstream system expects a structured record with a fixed set of fields.

| Layer | Deterministic or LLM? | Why |
|---|---|---|
| Output schema (fixed N-column record) | **Deterministic** | The downstream system requires this exact schema; any deviation breaks the integration |
| Validation that output matches schema (right types, required fields populated) | **Deterministic** | Schema validation is a rules problem |
| Parsing email body → structured fields | **LLM** | Free-text email with variable formatting; no rules can handle the variance |
| Parsing PDF attachment → structured fields | **LLM** + OCR | Same problem with worse input |
| Confidence threshold on the parse | **Deterministic** | The threshold is configured; below it → human queue |
| Human review on low-confidence parses | **Human-in-loop** | The seam between LLM extraction and deterministic schema |

### The defense if probed

When the interviewer asks "what's deterministic vs LLM in your design", the answer is:

> "I split it at the output schema level, not the agent level. The output schema is fixed and deterministic — every output has these N fields in this format, validated by rules. The parsing of unstructured inputs to fill that schema is where I use LLMs, because no rules can handle the variance in customer-submitted formats. The human-in-the-loop sits at the seam: confidence-low parses go to a human to confirm before the output is finalized."

This framing is shared by AI workforce platforms that contractually commit to output quality — they need the schema to be deterministic to enforce SLAs.

### When to use this framing

- Input analysis / ingestion agents (variable input formats → structured output)
- Document parsers (invoices, claims, contracts)
- Anywhere the input is unstructured and the output is structured by integration requirements

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
