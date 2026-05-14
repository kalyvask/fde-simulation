# Model-Layer vs Application-Layer

> Every solution you propose in an FDE interview should be tagged as: model-layer change, application-layer change, or both (sequenced). This is the single most-missed distinction in AI PM and FDE interviews, and the one that signals whether you've actually worked on AI products versus read about them.

## Why it matters

In a traditional product company, when you propose a feature, the engineering team figures out implementation. You don't need to specify which system does what.

In an AI product company, the PM/FDE needs to know whether a solution:

- Requires the **research/model team** — expensive, 3-6 month timelines, cross-team dependency, you don't own the roadmap
- Can be shipped by the **application/product team** — faster, lower risk, you own the roadmap
- Needs **both** — and in what sequence

If you can't tag your solution at this level, you signal that you've never had to make this decision in production. That's a high-leverage rejection trigger at frontier-lab FDE interviews.

## The distinction

| Model-layer | Application-layer |
|---|---|
| The model itself learns something new (fine-tuning, RLHF, new training data) | The product builds something around the model (UX, integrations, deterministic gates, retrieval) |
| Owner: research team / model team | Owner: product team / FDE team |
| Timeline: 3-6 months minimum | Timeline: days to weeks |
| Risk: alignment / safety review / regression on other capabilities | Risk: integration, UX, performance |
| Examples: train a new judge, fine-tune for a customer's voice, RLHF on a new task | Examples: add a deterministic critic, build a citation panel, wire a retrieval system, ship a new agent |

## How to deploy in an FDE interview

After you've sketched a solution, immediately tag it:

> "On the **model layer**, we'd need [X]. On the **application layer**, my team would ship [Y]. The model work is the longer dependency, so I'd sequence the application layer first and re-evaluate model investment after we have production signal."

That sentence shape signals three things:
1. You know there's a distinction
2. You know who owns what (and therefore the political map)
3. You know how to sequence — application-layer first because it's reversible, model-layer second because it's expensive

## Worked example: Helix Capital tone-shift detector

When Rachel's week-3 review surfaced that the Tone Supervisor was a tone *classifier* not a tone *shift detector*, the fix had two layers:

### Application-layer changes (shipped in 2 days)

- Wire prior-quarter note into the Tone Supervisor's input context
- Restructure the supervisor's prompt to do pairwise comparison instead of single-call sentiment scoring
- Add a "confidence threshold" routing rule for analyst escalation
- Update the trace renderer to show pairwise input

### Model-layer changes (deferred to v1.5, 6-week timeline)

- Generate 50+ pairwise calibration samples from Rachel's 18-quarter coverage history
- Calibrate the LLM-as-judge against the pairwise samples
- (If calibration is insufficient) Fine-tune a smaller model on the pairwise dataset

**The senior move**: I shipped the application-layer changes Thursday, validated against Rachel's Friday review (19/20), and **explicitly deferred the model-layer calibration** to v1.5 with a documented gate (50 pairwise samples + Brier score < 0.15 before model investment).

If I had defaulted to "we need to retrain the tone classifier" in week 1, that would have been a 6-week model-layer commitment for a problem that turned out to be solvable in 2 days at the application layer.

## Worked example: Calder FNOL warmth gap

When Janet's 20-draft review surfaced that drafts were "B-minus comms" (technically correct but missing emotional empathy), the fix had two layers:

### Application-layer changes (shipped same week)

- Add a 6th element to the Tone Supervisor's bar ("empathy that reflects emotional content of claimant narrative")
- Update the Drafter's prompt to include 3 example claims with empathetic phrasing
- Add a deterministic check for "Welcome to Calder" → flag for removal
- Add deterministic diacritic preservation check on claimant name

### Model-layer changes (NOT pursued)

- (Considered) Fine-tune a small model on Janet's preferred draft style
- (Considered) Train a separate empathy-detection model

**The senior move**: every fix was application-layer. The model-layer options were considered and rejected — fine-tuning would add operational surface (data pipeline, retraining cadence, regression risk on other capabilities) that's premature for v1. Application-layer prompt + deterministic guardrails got to 19/20 send-ready without touching the model.

## The defense when probed in interview

**Interviewer**: "Walk me through how you'd build a tone-shift detector for an earnings-note workflow."

**Weak answer (rejection trigger)**:
> "I'd fine-tune Claude on the customer's historical notes to detect tone shifts."

This signals model-first thinking, doesn't differentiate model vs application work, and commits to the longer/riskier path before justifying it.

**Strong answer**:
> "Two layers. On the **application layer**, I'd ship pairwise comparison — the supervisor gets the prior-quarter note + the current call, prompts Claude to score tone *delta* not absolute tone, with a confidence threshold for analyst escalation. That ships in 2 days. On the **model layer**, I'd defer fine-tuning until I have 50+ pairwise calibration samples from the lead analyst's coverage history — and even then, I'd use the samples to calibrate the LLM-as-judge before considering fine-tuning. The application-layer change is reversible and cheap; the model-layer change is expensive and slow. Always sequence application-first unless the application layer is structurally insufficient — which is rare for content tasks."

That answer signals:
- You distinguish the two layers
- You know the cost / timeline / reversibility tradeoffs
- You sequence correctly
- You know when fine-tuning is justified vs premature

## When model-layer work IS justified

Application-first is the default, but model-layer work IS the right call when:

| When | Why |
|---|---|
| The task requires capability the model doesn't have at all (e.g., a novel domain language the base model doesn't speak) | No amount of prompting closes the gap; you need new training data |
| You need pass^k=5 with variance ≤1% at high stakes and prompt-engineering plateaued at 92% | Fine-tuning collapses the variance distribution |
| The customer has 10K+ labeled examples of their desired behavior | The data is already there; not collecting it is leaving signal on the table |
| You need a small / cheap / fast model that matches frontier-model behavior on a narrow task | Distillation pattern; the engineering and ops are worth it |
| You need offline / on-prem / air-gapped deployment | Fine-tuned small model can run where API calls can't |

If **none** of these applies, default to application-layer. That's the senior FDE bias.

## Common probes and how to defend

| Probe | Defense |
|---|---|
| "Why not fine-tune Claude on the customer's data?" | Application-layer first. Fine-tuning adds operational surface (pipeline, retraining, regression risk) and 6-week timeline. Justified only when [list the 5 conditions above]; none applies here. |
| "What's the model team's role in this engagement?" | Minimal in v1. Application-layer first. Model-team escalation only on [specific narrow ask, with documented justification]. |
| "When would you go to the research team?" | When prompt + retrieval + deterministic gates have plateaued AND I have ≥5K labeled examples of the gap AND the gap is in a measurable failure mode AND the customer can wait 6 weeks. All four conditions; not any one. |
| "How does this scale across customers?" | Application-layer code is portable (BaseAgent, AuditTrace, deterministic critics). Model-layer fine-tunes are customer-specific and don't transfer. Another reason to prefer application-layer in early customer engagements. |

## How this framework interacts with our other frameworks

| With this framework | Use it for |
|---|---|
| [3-lens scaffold](3-lens-scaffold.md) | Technical column should specify which proposed changes are model-layer vs application-layer |
| [Workflow decomposition](workflow-decomposition.md) | When you decompose into agents, tag each agent as "application-layer construct" — the model is shared infrastructure across all agents |
| [Outcome Risk Matrix](outcome-risk-matrix.md) | Model-layer changes are higher risk + longer timeline; bias toward application-layer wedges for v1 |
| [Consulting frameworks — Delta Concept](consulting-frameworks.md) | The Delta you bridge is usually application-layer work; the model is the platform's contribution, the application-layer code is yours |
| [Company calibration](company-calibration.md) | Research-first AI labs respect well-justified model-layer asks; product-first labs default to application-first |

## Quick reference

```
MODEL-LAYER vs APPLICATION-LAYER

Application-layer (default):
  - Prompt engineering, retrieval, deterministic gates
  - Trust levels, confidence thresholds, routing
  - UX, integration, observability, audit trace
  - Owner: product team / FDE team
  - Timeline: days-to-weeks; reversible

Model-layer (justified only when application plateaus):
  - Fine-tuning, RLHF, new training data
  - Calibration of LLM-as-judge against labeled pairs
  - Owner: research team / model team
  - Timeline: 3-6 months; harder to reverse

DEFAULT SEQUENCE:
  1. Application-layer first (reversible, cheap, fast)
  2. Measure: does the application layer get us to the bar?
  3. If yes: ship, defer model-layer
  4. If no: justify model-layer investment with the 5-condition test

THE INTERVIEW MOVE:
  Every solution: tag layer explicitly.
  "On the model layer we'd need X. On the application layer my team would
  ship Y. The application layer ships first; we re-evaluate model
  investment after production signal."
```
