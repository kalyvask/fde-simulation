# FDE Recommendation Interview Playbook (60-minute format)

> A structural playbook for the Forward Deployed Engineer recommendation interview. The interview is high-level (recommendation-shape, no take-home build) and tests three explicit topics: Discovery, Solution Strategy, Risk & Validation. This document gives you the order in which to deploy frameworks, the points to land in each section, the predictable probes per topic, and the anti-patterns to avoid.

## What the company is testing

A 60-min FDE interview probes the same skill as OpenAI and Anthropic's Forward Deployed roles, with a tighter format:

- 60 minutes total
- High-level recommendation, not build
- Three explicit topics, in order: Discovery → Solution → Risk

The three topics map cleanly to the FDE engagement lifecycle: scope discovery → solution design → production readiness. They are testing whether you can lead an enterprise AI engagement from cold-start to production-grade without a senior FDE supervising you.

## The 60-minute structure

| Time | Section | Topic | What you are proving |
|---|---|---|---|
| 0:00–0:03 | Open | Framing | You can structure the conversation |
| 0:03–0:23 | Section 1 | Discovery Approach | You scope before you solution |
| 0:23–0:48 | Section 2 | Solution Strategy | You design agent workflows that ship to production |
| 0:48–0:55 | Section 3 | Risk & Validation | You think production-first, not demo-first |
| 0:55–0:60 | Reverse Q&A | Your questions back | You researched the team and the role |

## The opening (first 30 seconds)

Don't pretend you don't know the structure. Open by proposing time allocation:

> "Thanks for the framing. I'd suggest about 20 minutes on Discovery, 25 on Solution Strategy, 10 on Risk & Validation, and the last 5 for my questions. Want to start with the case?"

This frames the conversation, asks for assent (which they'll give), and signals you understand FDE time budgets.

---

## Section 1: Discovery Approach (~20 min)

> "You will be presented with a customer use case and asked to identify the stakeholders to engage, and the information needed to evaluate the current state."

### The question shape

Likely prompt: "An enterprise customer at [insurance / banking / legal / healthcare / manufacturing] needs AI agents that automate [specific workflow]. Walk me through how you'd approach discovery."

### What to land in this section

1. Restate the customer use case in one sentence before doing anything else
2. Identify stakeholders by archetype, not by name (you don't know the names yet)
3. List the information needed, organized by source (people / data / process / external)
4. Name the 4-source convergence test explicitly (signals process maturity)
5. Close with what you'd deprioritize in the first 2 weeks (signals scope discipline)

### Stakeholder archetypes to identify

Always present these as a map, not a list. Six-to-eight archetypes is the right density.

| Archetype | Role | What you need from them |
|---|---|---|
| Economic buyer | Signs the contract | Kill-criteria, ROI threshold, renewal logic |
| Champion | Brought you in | Political map, internal opposition, real timeline |
| Lead user | Daily operator of the workflow | Current pain, workaround patterns, "what good looks like" |
| Silent skeptic | The hostile downstream user | What they'd reject the agent for in week 4 |
| Tech owner | CTO / IT lead | System access, integration constraints, security posture |
| Compliance | Default-no | Regulatory surface, audit standards, MNPI / PII handling |
| Operations | Owns the post-handoff cadence | Who owns this in 90 days |

The **silent skeptic** is the move that separates senior from mid FDE candidates. Most candidates identify the champion and the user; few identify the person who will route around the agent in week 4 if not handled in week 1. Name them in your stakeholder map.

### Information needed (organized by source)

**From people (interviews)**
- Champion: political map + real (not stated) timeline
- Lead user: current workflow walkthrough with timestamps + pain points + workarounds
- Silent skeptic: "what would make you not use this?"
- Compliance: kill-criteria, regulatory surface, what auditors look at

**From data**
- Current process metrics (cycle time, accuracy, error rates, throughput)
- Volume distribution (long tail vs concentration)
- Existing logs / tickets for the workflow

**From process and documentation**
- SOPs, training docs, policy library
- Past automation attempts (what failed, why)
- Current tech stack (databases, integrations, APIs)

**From external**
- Industry benchmarks for the workflow
- Regulatory framework (SEC, HIPAA, GDPR, etc.)
- Competing solutions the customer has evaluated

### The 4-source convergence test (framework to name explicitly)

The senior FDE move: don't trust any single source. Triangulate.

| Source | What it tells you |
|---|---|
| Buyer (CIO / VP) | What they think the problem is |
| Brief (RFP / written prompt) | What they wrote down to formalize it |
| Industry (benchmarks / peers) | What's actually possible |
| Operator (lead user) | What's actually broken |

If all four sources point at the same workflow stage, you have the wedge. If they diverge, the operator usually has the truth and the buyer usually has the budget. You'll need both.

### The first 3 days (concrete day-by-day plan)

| Day | Interview | Output |
|---|---|---|
| Day 1 | Champion + lead user | Stakeholder map + draft wedge hypothesis |
| Day 2 | Compliance + tech owner | Regulatory boundary + integration map |
| Day 3 | Silent skeptic + operations | Adoption risk + post-handoff ownership plan |
| End of day 3 | Field memo to the platform team + customer | One-page wedge proposal + 4-week plan |

This is the senior FDE move. Naming a day-by-day plan beats "I'd talk to stakeholders."

### Predictable probes (Discovery)

| Probe | The answer |
|---|---|
| "What if you can only interview one person — who?" | Lead user. The buyer gives you budget; the operator gives you the wedge. |
| "What if compliance is unavailable for 6 weeks?" | Pull their audit standard + recent regulatory framework + interview champion on their behalf. Don't ship without their sign-off, but don't block discovery. |
| "Walk me through your first 3 days." | (Use the table above.) |
| "What if the buyer is wrong about the problem?" | Document the divergence. Bring the data to the next meeting. Don't argue in the first session. |
| "How would you handle a stakeholder who refuses to meet?" | Try once with the champion's intro; if still no, work around them and document the gap in the field memo. The interview is one of the artifacts the engagement produces, not a precondition. |

### Anti-patterns to avoid in Discovery

- Listing stakeholders without archetypes ("CEO, CTO, head of ops")
- Asking for "all the data" without scope
- Forgetting compliance entirely
- Forgetting the silent skeptic
- Starting with the tech ("I'd want to see their data warehouse first")
- Saying "I'd do a discovery phase" without naming what's IN it

---

## Section 2: Solution Strategy (~25 min)

> "You are expected to describe your approach for designing an AI workforce that automates manual workflows and integrates with core business systems."

### The question shape

Likely: "Now that you've done discovery, sketch how you'd design the AI workforce for this customer."

### What to land in this section

1. **The wedge**: the narrow first workflow you'd automate
2. **Wedge selection principle**: confidence over size, plus the Outcome Risk Matrix
3. **Agent decomposition**: 5-8 specialized agents, not a single mega-prompt
4. **Hybrid deterministic + LLM architecture**: tell them which agents are which and why
5. **Integration map**: which core systems, what permissions, three-tier ladder
6. **Trust levels**: act / ask / escalate per agent
7. **Read-only v1**: defensive framing, not apologetic
8. **Out-of-scope explicit**: equally explicit as in-scope

### The wedge selection principle (lead with this)

> "I'd pick the wedge using two principles: confidence of outcome over size of outcome, and the Outcome Risk Matrix on value × risk-of-irreversible-failure."

Then describe 3-4 candidate wedges, score them on the 2x2, pick one.

The 2x2:

| | Low-risk failure (reversible) | High-risk failure (irreversible) |
|---|---|---|
| **High value** | **Ship as v1** | Ship with hard guardrails + senior veto |
| **Low value** | De-prioritize | Avoid entirely |

The wedge isn't "what's biggest". It's "what's biggest that you can ship cleanly."

### The 3-lens scaffold (Customer / Product / Technical)

This is the single most useful framework for this section. It forces you to design the wedge through 3 lenses before getting into tech.

```
| CUSTOMER (the user) | PRODUCT (the agent) | TECHNICAL (the build) |
|--------------------|---------------------|----------------------|
| Who (specific)     | Intent (top 3)      | Read access          |
| Emotional state    | In scope (3-5)      | Write access (NONE   |
| JTBD top 3 intents | Out of scope        |   in v1)             |
| Why failing today  |   (equally explicit)| Data freshness       |
| What's hard        | Trust (act/ask/     | ONE specific risk    |
|   (root cause)     |   escalate)         | Validation plan      |
|                    | Fallback            |                      |
|                    | Metric + tension    |                      |
```

When asked "design the AI workforce", walk through all 3 columns out loud. Name the emotional state. Name out-of-scope as explicitly as in-scope. Name the metric tension.

### From the 3-lens table to the wedge to the build (worked example)

The 3-lens table by itself isn't the answer. It's the discovery artifact. The wedge comes from running the table through the Outcome Risk Matrix, and the build comes from translating the wedge into specific agents + integration tiers.

**The 4-step flow**:

1. **Fill the 3-lens table** (Customer / Product / Technical) using what you got from Discovery
2. **Derive 3-5 candidate wedges** from what the table reveals about scope, trust, and risk
3. **Score the candidates on the Outcome Risk Matrix** (Value × Risk-of-irreversible-failure)
4. **Translate the chosen wedge** into specific agents + integration tier + validation plan

#### Worked example: AP invoice processing for a mid-market manufacturer

The customer is a mid-market manufacturer with 1000 invoices/month across 200 vendors, processed by 4 AP analysts. Each invoice takes about 5 min of manual entry. The CFO wants to automate. The CFO is the buyer; the AP analyst (Maria) is the lead user; the Controller is the silent skeptic (audit-anxious).

#### Step 1 — Fill the 3-lens table

| CUSTOMER | PRODUCT | TECHNICAL |
|---|---|---|
| **Who**: Maria, AP analyst, 7 yrs tenure, lead user | **Intent**: Match-classify-route invoices through the AP workflow | **Read**: ERP (vendor master, PO data), invoice intake folder, GL chart of accounts |
| **Emotional state**: Exhausted (80 hrs/mo manual entry) + anxious (audit risk on misclassification) | **In scope**: PO matching, GL classification for top 80% of invoices, routing to approver | **Write**: NONE in v1; stage to a holding queue for analyst approval |
| **JTBD**: (1) Match invoice to PO, (2) Classify GL code, (3) Route for approval | **Out of scope**: New vendor onboarding, split-coding exceptions, auto-approve over $X | **Data freshness**: ERP live; PO data live; GL chart cached daily |
| **Why failing today**: 5 min × 1000 invoices = 80 hrs/mo per analyst; backlog grows month-end | **Trust**: Act on confident PO matches; ask analyst on ambiguous GL; escalate on exceptions | **ONE specific risk**: GL code drift (controller adds new accounts mid-quarter; classifier cites stale chart) |
| **What's hard (root cause)**: Invoice variability (each vendor's format differs) + company-specific GL rules buried in playbook docs | **Fallback**: Push to Maria's queue with reasoning trace; never silent-fail | **Validation plan**: PoC + 100-invoice eval suite + audit sign-off + 50-sample analyst review + 1-month closed beta with 1 vendor segment |
|  | **Metric + tension**: Throughput vs accuracy. Protect accuracy (audit risk is the kill-criteria). |  |

#### Step 2 — Derive candidate wedges from the table

The filled table surfaces 5 candidate wedges. Each one is a different slice of the in-scope cells:

1. **PO matching only** — narrow, takes one of the 3 JTBD steps
2. **GL classification only** — medium, takes the second JTBD step
3. **PO matching + GL classification, with human-in-loop approval** — medium-broad, takes 2 of 3 steps with safety net
4. **Full match-classify-route + auto-approve under $X** — biggest, removes Maria from the loop on small invoices
5. **Exception triage only** — different angle, hardest cases first

The "what's in scope" row of the Product column tells you what the candidate wedges should be. The "trust levels" row tells you how aggressive each can be.

#### Step 3 — Score on the Outcome Risk Matrix

| Wedge | Value | Risk of irreversible failure | Quadrant | Decision |
|---|---|---|---|---|
| 1. PO matching only | Low (1 of 3 steps, ~15% time saved) | Low | Low value / Low risk | De-prioritize |
| 2. GL classification only | Medium (saves 30% of time) | Medium (wrong GL = financial-statement restatement risk) | Med / Med | Defer to v1.5 |
| **3. PO matching + GL with HITL** | **High (saves 60% of analyst time)** | **Low (Maria reviews every output before it touches ERP)** | **High value / Low risk** | **Ship as v1** |
| 4. Full + auto-approve under $X | High (saves 80%) | High (auto-approval = audit risk, irreversible until quarterly review) | High value / High risk | Defer to v2 with hard guardrails |
| 5. Exception triage only | Medium (handles the hardest cases) | Medium (exceptions are inherently risky to automate first) | Med / Med | Defer to v1.5 |

**The wedge is option 3.** It's the smallest wedge that hits the high-value, low-risk quadrant. Confidence of outcome over size of outcome.

The defense if the interviewer probes "why not option 4?": Option 4 is high value but high risk. Auto-approval is an irreversible action with audit consequences. We earn auto-approval by shipping option 3 first, getting Maria's sign-off on 50+ samples, then promoting individual invoice categories to auto-approve based on confidence scores measured in production.

#### Step 4 — Translate the wedge into the build

From "PO matching + GL classification with HITL" to specific agents:

| Agent | Job | Tier | Det / LLM | Why this choice |
|---|---|---|---|---|
| 1. Invoice intake | OCR + structured field extraction from PDF | Haiku + OCR library | Hybrid | Reliability > creativity on extraction |
| 2. PO matcher | Match invoice to existing PO by vendor + amount + line items | Haiku | Deterministic with LLM fallback | Most matches are deterministic; LLM handles vendor name variations |
| 3. GL classifier | Classify line items to GL codes using company playbook | Sonnet | LLM | Synthesis problem: playbook + invoice content + GL chart |
| 4. Compliance critic | Flag invoices that hit kill-criteria (over $X, new vendor, audit flag, split-coding) | Deterministic | Rules | Reversible failures only; reliability is the requirement |
| 5. Routing agent | Route flagged-clean invoices to approver queue by amount + category | Deterministic | Rules | Predictable; no synthesis needed |
| 6. Audit trace generator | Examiner-readable log per invoice with citation chain | Deterministic | Deterministic | Reliability-critical; audit is the kill-criteria |

Integration ladder for this wedge:

| Tier | What it does | When |
|---|---|---|
| Tier 1 (v1, weeks 1-4) | Read from ERP; write only to holding queue. Maria approves in the queue. | Ship after Mei + Maria + Controller sign-off |
| Tier 2 (v1.5, weeks 5-12) | Write to ERP after analyst approval (one-click). Confidence threshold tracked. | Pass^k=5 on weighted eval suite |
| Tier 3 (v2, weeks 13+) | Auto-approve invoices under $X with confidence > Y% (still flagged for audit review) | Pass^k=5 + 90 days of clean Tier 2 + audit sign-off |

#### What this example demonstrates

The translation from 3-lens table to build is mechanical once the table is filled well:

- The **Customer column** tells you who suffers and how, which drives the wedge's value
- The **Product column** tells you what's in scope (the wedge candidates) and what trust levels apply (the risk per candidate)
- The **Technical column** tells you where the integration risk lives and what to test
- The **Outcome Risk Matrix** picks the wedge from the candidates
- The **chosen wedge** decomposes into 5-8 agents based on which cells in the Product column it covers
- The **integration ladder** sequences read-only → one-way → two-way based on the trust progression

If you can do this translation live in the interview — fill a 3-lens table for the customer's case, derive 3-5 candidate wedges, score them on the matrix, pick one, and sketch the agent decomposition — you'll demonstrate the full FDE skill in 15 minutes of the Solution section.

### The 5 principles of AI workforce design

When the interviewer says "design the AI workforce", these 5 principles are what you're applying. Name them out loud before drawing agents.

| Principle | What it means | The probe it defends against |
|---|---|---|
| **1. Decompose by failure mode, not by feature** | Boundaries between agents go where the failure modes change, not where the product capabilities change. The MNPI scrubber is a separate agent because its failure mode (regulatory leak) is different from the drafter's (bad synthesis). | "Why these agent boundaries?" |
| **2. Deterministic gates around the dangerous calls** | Any irreversible action (write, regulatory check, citation grounding) gets a deterministic agent in front of it. LLMs do the soft work; rules do the hard work. | "Why not LLM-as-judge for everything?" |
| **3. Read before write, always** | Agents read freely from source systems; agents do not write to source systems in v1. Write paths go through a holding queue with human approval. | "Why no auto-write?" |
| **4. Each agent has ONE job** | If you can't describe an agent in 8 words, split it. "GL classifier" is one job; "GL classifier + audit trace" is two. | "Why so many agents?" |
| **5. The orchestrator is dumb; the agents are smart** | Orchestration is sequential + branching + retry logic. The intelligence is in the agents. Don't put business logic in the orchestrator. | "How does this scale to 10x volume?" |

### Workflow decomposition: how to draw agent boundaries

When the interviewer asks "walk me through how you'd design the agents", use this 5-step method. It's the senior FDE move because it forces an explicit boundary-drawing exercise.

| Step | What you do | The output |
|---|---|---|
| 1. Map the manual workflow as a swimlane | Draw the human's current process step by step, including decision points and handoffs | A linear sequence of 8-15 steps |
| 2. Identify decision points vs execution points | Decision = "should I do X or Y?". Execution = "do X." | Two lists: ~3-5 decisions, ~5-10 executions |
| 3. Group execution points by data + tier requirements | Steps that read from the same source and need the same model tier collapse into one agent | The first cut at agent boundaries |
| 4. Add a critic agent at every irreversible step | Anywhere the output goes to a downstream system, add a deterministic critic in front | The compliance and audit layer |
| 5. Add a routing layer for confidence-low cases | Decide which agent's output gets escalated and to whom | The trust-level structure |

For the AP invoice example from above:

- **Manual workflow steps** (swimlane): receive invoice → OCR → look up vendor → match to PO → classify GL → check policies → route to approver → record in ERP
- **Decision points** (2): "does this match a PO?", "what GL code applies?"
- **Execution points** (6): OCR, vendor lookup, PO match, GL classify, policy check, route
- **Grouped agents** (3): Invoice intake (OCR + vendor lookup), PO matcher (PO match), GL classifier (GL classify)
- **Critics added** (2): Compliance critic (policy check), Audit trace generator (irreversible logging)
- **Routing added** (1): Routing agent (queue selection by amount + flag)

That's the 6 agents in the AP example, derived mechanically from the manual workflow.

### Agent shapes (the catalog to deploy from)

Don't invent agent types. There are ~7 common shapes; pick from the catalog.

| Shape | Job | Typical tier | Det / LLM | When to use |
|---|---|---|---|---|
| **Extractor** | Pull structured data from unstructured input | Haiku | Hybrid (regex when possible) | Invoice fields, KPI extraction, entity recognition |
| **Classifier** | Route input to one of N paths | Haiku or rules | Deterministic if possible | Intake triage, category routing, queue selection |
| **Synthesizer / drafter** | Produce natural-language output from structured input | Sonnet or GPT-4o | LLM | Drafts, summaries, explanations, recommendations |
| **Critic / judge** | Evaluate another agent's output | Sonnet | LLM-as-judge with calibration | Faithfulness check, tone check, quality check |
| **Compliance critic** | Enforce rules (regulatory, policy, business) | Deterministic | Rules-based | Kill-criteria enforcement, MNPI scrub, threshold checks |
| **Router** | Deterministic handoff logic between agents | Deterministic | Rules-based | Escalation, fallback, parallel fan-out |
| **Auditor** | Produce immutable, examiner-readable logs | Deterministic | Deterministic | Audit trace, reasoning chain, citation chain |

The senior move is naming the shape before naming the agent. "I'd use a Classifier shape for intake — Haiku, deterministic where possible" beats "I'd build an intake agent."

### Orchestration patterns (how agents coordinate)

There are 4 orchestration patterns. Name the one your design uses.

| Pattern | When to use | Example |
|---|---|---|
| **Sequential pipeline** | Most workflows. Each agent's output is the next agent's input. | Invoice intake → PO matcher → GL classifier → Compliance critic → Routing agent |
| **Parallel fan-out** | When agents are independent and you want speed | PO matcher + GL classifier run in parallel (they don't depend on each other) |
| **Conditional branching** | When the next agent depends on a decision | If Compliance critic flags → escalation queue; else → Routing agent |
| **Loop with retry** | When confidence-low cases need re-processing | Drafter produces output → Critic flags → re-prompt drafter with critic's feedback (max 2 retries) |

The orchestrator owns: state management, retry policy, idempotency (can a request be re-run safely), and observability (logging per-agent inputs/outputs to the audit trace).

**The defense if probed**: "The orchestrator is intentionally dumb — sequential + branching + retry. Business logic lives in the agents. This keeps the orchestrator stable while the agents iterate." 

### Agent decomposition (5-8 specialized agents)

Describe the workforce, not a single agent. Each agent has a job, a model tier, and a det-or-LLM choice.

A typical 5-8 agent workforce for an enterprise workflow:

| Agent | Job | Tier | Det / LLM | Why |
|---|---|---|---|---|
| 1. Intake / classifier | Route incoming request to right path | Haiku or rule-based | Deterministic if possible | Failure is silent — keep it predictable |
| 2. Data extractor | Pull structured data from sources | Haiku | Deterministic regex when possible, LLM for unstructured | Reliability > creativity |
| 3. Synthesizer / drafter | Produce the natural-language output | Sonnet or GPT-4o | LLM | Synthesis is what LLMs are uniquely good at |
| 4. Quality critic | Check synthesizer's output | Sonnet | LLM-as-judge with calibration | Catches failure modes the drafter missed |
| 5. Compliance critic | Enforce regulatory rules | Deterministic | Rules-based | Reversible failures only |
| 6. Audit trace generator | Produce examiner-readable log | Deterministic | Deterministic | Needs reliability |
| 7. (Optional) Tone / faithfulness supervisor | Catch soft errors | Sonnet | LLM-as-judge | Calibrated against labeled corpus |
| 8. (Optional) Human-handoff agent | Route confidence-low cases | Deterministic | Rules-based | Predictable escalation |

**The defensible answer to "why not a single mega-prompt":** Single prompt has one set of failure modes. Decomposition lets you swap out the failing agent without touching the others. It also lets you put deterministic gates around the dangerous calls.

### Integration with core business systems

Don't say "we'd integrate." Name the read pattern, the write pattern, and the tier ladder.

#### Read patterns (how agents pull data from core systems)

| Pattern | When to use | Example |
|---|---|---|
| **API-based (REST / GraphQL)** | Default for SaaS systems (Salesforce, ServiceNow, Workday) | CRM read via SF API |
| **DB direct (read-only replica)** | Lower latency, high-volume reads, on-prem | ERP via read-replica of the Postgres warehouse |
| **Event stream (Kafka / Snowpipe)** | Real-time signals, append-only workflows | Order events, transaction stream |
| **File ingestion (S3 / SFTP)** | Batch workflows, legacy systems, document inputs | Invoice PDFs dropped in S3 bucket |

The defense if probed "why API vs DB direct": API is the default unless latency or volume forces you to a read-replica. API gives you the system's permission model for free; DB direct means you're maintaining your own permission layer.

#### Write patterns (how agents push outputs back)

| Pattern | When to use | Risk level |
|---|---|---|
| **Holding queue (v1)** | Default for any write in week 1-4. Agent writes to a staging area; human approves before the system of record sees it. | Low — analyst catches errors |
| **Approval-gated write (v1.5)** | Agent writes to system of record only after human one-click approval | Medium — write happens, but with explicit consent |
| **Direct write with audit (v2)** | Agent writes autonomously; every write is logged immutably | High — only after pass^k=5 + 90 days clean Tier 2 |
| **Event emission (v2+)** | Agent emits events that downstream systems consume; preferred for distributed workflows | Medium — events are usually idempotent |

#### The 3-tier integration ladder (sequencing the write capability)

| Tier | What it does | When to ship | Gate to next tier |
|---|---|---|---|
| Tier 1: Read-only | Read freely; write only to a holding queue or staging table | v1, weeks 1-4 | Pass^k=5 on weighted eval + 20-sample analyst sign-off |
| Tier 2: One-way approval-gated write | Write to system of record after human approval (one-click) | v1.5, weeks 5-12 | 90 days clean Tier 2 + audit sign-off |
| Tier 3: Two-way autonomous write with audit | Autonomous write to system of record for confidence-above-threshold cases; everything logged | v2, weeks 13+ | Customer-specific gates (regulatory, business, board-level) |

The 3-tier ladder shows you understand enterprise security posture and earn-the-right-to-write thinking. The interviewer's probe "what about auto-publish?" gets the answer: "Tier 3 conversation, gated on Tier 2 stability."

### Cost and latency budget (the production-thinking move)

When the interviewer asks "how does this scale", or "what's your cost story", have a per-agent budget ready.

| Dimension | What to name |
|---|---|
| **Token cost per agent run** | Order of magnitude: extractor ~$0.001, drafter ~$0.05, critic ~$0.02 |
| **P95 latency per agent** | Extractor <1s, drafter 3-8s, critic 2-5s, deterministic <100ms |
| **Total workflow cost** | Sum of agent costs × volume; for AP example: ~$0.10 × 1000/mo = $100/mo for the LLM layer |
| **Total workflow latency** | Sum of P95 latencies; sequential pipelines bottleneck on the slowest agent |
| **Tier-down options** | If cost is a blocker, tier down non-critical agents (Sonnet → Haiku on extraction, but not on synthesis) |
| **Cache-eligible operations** | Vendor master, policy library, GL chart — these change slowly, cache them |

The probe "what's your cost ceiling" gets the answer: "Per-workflow $0.10 in v1, with tier-down + caching giving us 50% room. For AP at 1000/month that's $100; well below the $50K savings."

The probe "what's your latency budget" gets: "End-to-end P95 under 15 seconds for the synchronous path; async path (audit trace, eval logging) doesn't block."

### Trust levels (act / ask / escalate)

For each agent, define:

- **Act autonomously**: deterministic gates + low-stakes LLM calls (e.g., reading data, doing extraction)
- **Ask the user**: confidence-low cases, edge cases, anything the customer would want a human in the loop on
- **Escalate**: regulatory edge cases, policy combinations, ambiguity outside the trained scope

The trust-level table is the answer to "where's the human in the loop?"

### Predictable probes (Solution Strategy)

| Probe | The answer |
|---|---|
| "Why not a single mega-prompt?" | Single prompt fails on specific failure modes (e.g., hallucinated number reaching a downstream system). Hybrid contains LLM variance to the natural-language layer where LLMs are uniquely good. Deterministic gates around the dangerous calls. |
| "Why these tier choices?" | I split on synthesis vs extraction. Synthesis → Sonnet or GPT-4o. Extraction → Haiku. Reliability-critical → deterministic. The drafter's volume isn't usually cost-prohibitive for Sonnet at enterprise scale. |
| "Why read-only v1?" | Write access in v1 means a wrong action becomes a wrong record in the customer's core system. Read-only caps the failure mode at "user catches it in review." We earn write access by shipping read-only first. |
| "How does this scale to 10x volume?" | Agent decomposition makes the scaling problem about which agent's bottleneck. Identify the tier change per agent, not for the whole workforce. The drafter usually scales linearly with cost; the critic scales sub-linearly because eval re-runs are amortized. |
| "What if Anthropic / OpenAI has an outage?" | Failover to the other on the synthesizer (BAA permitting); degraded mode on the critic (more human review). Don't auto-fail; degrade gracefully. |
| "What about fine-tuning?" | I'd not fine-tune in v1. Configuration + prompt engineering + retrieval handles 90% of enterprise use cases. Fine-tuning adds operational surface (data pipeline, eval, retraining cadence) that's premature for v1. v2 conversation. |
| "What if the customer asks for autonomous trade execution / publish / send?" | Out of scope for v1. The failure mode goes from 'reversible draft' to 'irreversible action.' We ship read-only first and earn the autonomy. |

### Anti-patterns to avoid in Solution Strategy

- Single mega-prompt with no architecture
- Generic "RAG + guardrails" without specifics
- Promising fine-tuning in v1 without justification
- Auto-publish or two-way write in v1
- Skipping the trust-level structure
- Not naming the metric tension
- Not naming out-of-scope items explicitly

---

## Section 3: Risk & Validation (~10 min)

> "You must identify potential technical limitations of the solution and outline a comprehensive testing framework to ensure accuracy."

### The question shape

Likely: "What could go wrong, and how would you test for it before production?"

### What to land in this section

1. Identify 5-7 risks proactively (don't wait to be asked)
2. Each risk has a named mitigation + stakeholder owner
3. Name a 4-dimensional testing framework (static eval + pass^k + adversarial + production observability)
4. Name pass^k explicitly (k=5 is the production threshold)
5. Name 3 sign-off criteria with stakeholder owners
6. Name the drift-detection plan (technical + UX + business levels)

### The 5-7 risks to surface proactively

Order matters. Lead with the risks that match the customer's named kill-criteria.

| Risk category | Example | Mitigation pattern |
|---|---|---|
| Hallucination | Wrong number / fabricated fact reaches a downstream system | Citation grounding (deterministic) + LLM-as-judge faithfulness check |
| Regulatory | MNPI / PII / Reg FD violation | Deterministic scrubber fires before any LLM call |
| Drift | Model behavior changes over weeks | Eval suite re-run on every release + 5% rolling-window drift detection |
| Integration failure | Source-system schema change breaks extraction | Versioned schema contract + alerting on extraction failure |
| Adoption / engagement | Users route around the agent | Engagement metric tracked separately from quality metric |
| Cost / latency | LLM cost or P95 latency spikes | Tier-down (Sonnet → Haiku) on non-critical agents + caching |
| Vendor outage | LLM provider has incident | Failover provider configured + degraded mode |

**Each risk needs a stakeholder owner.** "Compliance owns the regulatory risk. The tech owner owns the integration risk. The champion owns the adoption risk." This is the senior FDE move.

### The 4-dimensional testing framework

When asked "how would you test this", name 4 dimensions, not 1:

1. **Static eval suite**
   - Weighted by failure cost (regulatory block weighted 10x higher than tone shift)
   - 50+ cases minimum for v1
   - Composition: happy path + adversarial + edge cases

2. **Pass^k production threshold**
   - k=5 (not pass@1)
   - Variance tolerance ≤5% across runs
   - Re-run on every release

3. **Adversarial set**
   - One case per major risk surfaced
   - Includes the customer's specific kill-criteria

4. **Production observability**
   - Rolling 7-day drift detection on output distribution
   - Alerts on extraction-failure spikes
   - Immutable audit trace per request
   - Weekly review with operational owner

### The 3-level metrics framework (technical / UX / business)

When asked "how do we know this is working", answer at 3 levels:

| Level | Metrics |
|---|---|
| Technical | Pass^k, latency P95, extraction accuracy, cost per request |
| UX | Time-to-resolve, escalation rate, repeat-contact rate, adoption % |
| Business | Cost per resolved, retention signal, NPS, $ saved per workflow |

Then name the **tension** between two metrics. Pass^k vs latency. Adoption vs accuracy. Pick which you protect in v1.

### Three sign-off criteria for production rollout

Always name 3 sign-off gates with stakeholder owners:

| Criterion | Stakeholder owner |
|---|---|
| Pass^k=5 with variance ≤5% on weighted eval | Tech owner |
| Compliance sign-off on audit trace standard | Compliance / Mei-equivalent |
| Senior user reviews 20 sample outputs and signs off | Lead user / Rachel-equivalent |

These three gates are non-negotiable. Naming them with owners shows you've thought about who blocks production.

### Predictable probes (Risk & Validation)

| Probe | The answer |
|---|---|
| "What's your k value and why?" | k=5. Real production needs to distinguish "flaky on a specific case" from "broken." Pass@1 hides flakiness. |
| "What's your eval set sourced from?" | Synthetic for v1 (covers known failure modes), production-labeled subset for v1.5 (covers real distribution). |
| "What if your eval passes but production fails?" | The eval composition is wrong. Either weight is off or distribution doesn't match reality. Diagnostic: re-weight by failure cost; expand adversarial set with the production failures. |
| "What if compliance changes mid-engagement?" | Versioned policy library + LLM-as-judge tier-2 check on every release. Compliance owner signals the policy update; we re-run evals before next release. |
| "Who owns this in 90 days?" | Operational owner named pre-handoff. Weekly cadence for first 30 days post-handoff. Field memo back to the platform product team monthly. |
| "What's the rollback procedure?" | Immutable snapshots of every agent version + traffic-shift back to prior version + 24h smoke test. Rollback is a feature, not an emergency. |

### Anti-patterns to avoid in Risk & Validation

- "We'd thoroughly test" without specifics
- Pass@1 thinking
- No observability story
- No named ownership post-handoff
- Risks without mitigations
- Mitigations without stakeholder owners
- "Drift detection" without a specific window or threshold

---

## Reverse Q&A (last 5 min)

What to ask:

| Strong | Weak |
|---|---|
| "What's the typical FDE engagement at the company look like in the first 90 days?" | "What's the team culture like?" |
| "What's the field-back-to-product loop in practice?" | "Tell me about a fun project." |
| "What's the failure mode of a new FDE you've seen most often?" | (no questions) |
| "What would I be doing 6 months in?" | "What do you like about working here?" |
| "What's a customer engagement that surprised you this year?" | "Is there flexibility?" |

If you can, reference something specific from the company's public material (their docs, a blog post, a recent product launch). Signals preparation.

---

## The 4 frameworks to memorize cold

| Framework | Where to deploy | One-line definition |
|---|---|---|
| **4-source convergence** | Discovery | Triangulate Buyer / Brief / Industry / Operator to find the real wedge |
| **3-lens scaffold** | Solution | Customer / Product / Technical columns; fill before designing tech |
| **Outcome Risk Matrix** | Solution | Score wedges on Value × Risk-of-irreversible-failure 2x2 |
| **4-dimensional testing** | Risk & Validation | Static eval + Pass^k=5 + Adversarial + Production observability |

If you can deploy these four frameworks with calibration on this customer's specifics, you'll hit the FDE bar.

---

## What "good" looks like at the 60-minute mark

The interviewer should leave with the impression that:

1. You scoped before you solutioned (Discovery)
2. You named a wedge with a defended principle (Solution)
3. You designed an architecture, not a prompt (Solution)
4. You named risks proactively (Risk)
5. You named production gates with stakeholder owners (Risk)
6. You closed with questions that show you read about their team (Reverse Q&A)

If you hit all six, you're at the FDE final-round bar.

---

## The mindset (one paragraph)

You don't have to be perfect. Frontier labs and AI-workforce platforms reward strong-but-flawed candidates over polished mediocre ones. Defend with substance. Admit gaps with intellectual honesty. Lead with substance over polish. When you don't know an answer, say "I don't have a good answer for that yet; my instinct is X, but I'd want to validate by Y" — that's a stronger signal than a fabricated answer.

---

## Quick reference card (print before the interview)

```
0:00-0:03 OPEN
  Propose time allocation: 20 / 25 / 10 / 5
  Restate the customer use case in one sentence before doing anything else

0:03-0:23 DISCOVERY (~20 min)
  4-source convergence: Buyer / Brief / Industry / Operator
  Stakeholder archetypes (6-8): include silent skeptic
  Information by source: people / data / process / external
  First 3 days plan, day by day
  Anti-pattern: starting with the tech

0:23-0:48 SOLUTION STRATEGY (~25 min)
  Wedge selection: confidence > size; Value × Risk 2x2
  3-lens scaffold: Customer / Product / Technical
  5-8 specialized agents, hybrid det + LLM
  3-tier integration ladder: read-only → one-way → two-way
  Trust levels: act / ask / escalate
  Read-only v1 (defensive, not apologetic)
  Out-of-scope = in-scope (equally explicit)

0:48-0:55 RISK & VALIDATION (~10 min)
  5-7 risks proactively, each with mitigation + owner
  4-dimensional testing: static eval + pass^k=5 + adversarial + production observability
  3-level metrics: technical / UX / business
  Name the metric tension
  3 sign-off criteria with stakeholder owners

0:55-0:60 REVERSE Q&A
  First-90-days at the company FDE
  Field-back-to-product loop
  Failure mode of a new FDE
  Reference the company's public material

THE SUB-RULES THROUGHOUT:
  Name the emotional state of the user
  Out-of-scope as explicit as in-scope
  Name the metric tension explicitly
  Read vs write distinguished
  One specific risk, not a generic list
  Never jump topics under pressure
  Read-only v1 is the senior move
```

---

## Mock case worked example: Sentinel Software (B2B SaaS support automation)

> A fictional case end-to-end. Shows you what to actually say in each of the three sections. Read this after the rest of the playbook. It's the worked example that brings the frameworks together. Customer details are made up.

### The case (as the interviewer would present it)

> "Sentinel Software is an $80M ARR B2B SaaS company, vertical CRM for car dealerships, 450 employees. Customer Success handles 2,500 support tickets per week across 8 reps. Tier 1 tickets (about 60% of volume) are repetitive: password resets, config questions, billing inquiries. Avg ticket takes 12 minutes. Two reps quit in Q4 citing burnout. The CS Director wants an AI workforce to handle Tier 1. Walk us through how you'd approach this."

### How I'd open (15 seconds)

> "Let me restate it in one sentence: Sentinel wants to deflect 60% of support volume by automating Tier 1, without trashing CSAT or losing the institutional knowledge of senior reps. Time-wise, I'd spend ~20 min on Discovery, ~25 on Solution, ~10 on Risk, last 5 for my questions. Sound good?"

---

### Section 1 — Discovery Approach (~20 min)

#### Stakeholders to engage (the table I'd draw)

| Archetype | Person | Why |
|---|---|---|
| Economic buyer | Sarah Chen, Director of CS | Owns the budget; ROI threshold; renewal impact |
| Champion | Marcus Webb, Support Manager | Brought us in; owns the rep team day-to-day |
| Lead user | Priya Patel, Sr Support Rep (6 yrs) | Knows good-vs-bad; her sign-off is the bar |
| Silent skeptic | Carlos Diaz, Account Exec | Worried agent answers will hit CSAT → renewals |
| Tech owner | Devin Lee, Head of Engineering | Owns Zendesk + Salesforce + product DB integrations |
| Compliance | Alex Kim, Data Privacy | GDPR (EU dealerships) + SOC2 + PII in tickets |
| Operations | TBD post-handoff | Whoever owns the agent in 90 days |

**What I'd say**:
> "Seven archetypes. The one most candidates miss is the silent skeptic. Carlos is the AE — his CSAT numbers feed renewals, so if the agent ships and CSAT drops 5%, he's going to surface it before Sarah does. I'd interview him in week 1, not when he's already complaining."

#### Information needed (organized by source)

| Source | What |
|---|---|
| People | Sarah's ROI threshold; Marcus's real timeline; Priya's 30-min workflow walkthrough with timestamps; Carlos's "what would make you reject this"; Alex's regulatory floor |
| Data | 90 days Zendesk tickets with categories + resolution time + CSAT; volume distribution by intent; past automation attempts |
| Process | Tier 1 SOPs; existing Zendesk macros; product DB schema |
| External | Zendesk-published deflection benchmarks; GDPR + SOC2 audit requirements |

#### 4-source convergence (what I'd actually say)

> "I'd triangulate four sources: Sarah (buyer) says it's volume, the brief says it's Tier 1, industry says password resets + billing are the deflection sweet spot, and Priya (operator) will tell me which 2-3 intents are scripted vs need judgment. If all four converge, that's the wedge. If Priya diverges from the brief — say she tells me billing inquiries are actually 50% nuanced not 50% scripted — I trust Priya."

#### First 3 days

| Day | Interview | Output |
|---|---|---|
| Day 1 | Sarah + Priya | Stakeholder map; draft wedge hypothesis |
| Day 2 | Alex + Devin | Regulatory boundary; integration map |
| Day 3 | Carlos + a dealership customer (via Marcus intro) | Adoption risk; CSAT floor |
| End day 3 | Field memo to Sentinel + internal | 1-page wedge proposal + 4-week plan |

---

### Section 2 — Solution Strategy (~25 min)

#### Step 1: The 3-lens table (what I'd draw on the whiteboard)

| CUSTOMER | PRODUCT | TECHNICAL |
|---|---|---|
| **Who**: Priya (lead user), Sarah (buyer), dealership owner (end customer) | **Intent**: Auto-resolve top 3 Tier 1 intents with human-in-loop | **Read**: Zendesk, Salesforce, product DB, KB articles |
| **State**: Exhausted (500 hrs/wk demand vs 320 capacity) + anxious (Carlos's CSAT concern) | **In scope**: Password reset (15%), simple config (25%), billing inquiry (20%) = 60% of volume | **Write**: NONE in v1; drafts to Zendesk private comment Priya approves |
| **JTBD**: (1) Classify ticket intent, (2) Pull customer context, (3) Draft response | **Out of scope**: Tier 2/3, refund decisions, account changes, negative-sentiment tickets | **Freshness**: Zendesk live, Salesforce live, product DB 5-min cache, KB daily index |
| **Why failing today**: 12 min × 2500/wk = 500 hrs demand vs 320 hrs rep capacity | **Trust**: Act on high-confidence KB answers; ask Priya on edges; escalate on Tier 2 or negative tone | **ONE risk**: PII leak — tickets contain emails, dealership info |
| **Hard**: Reps can't context-switch fast; 12 min floor even for password resets due to verification + navigation overhead | **Fallback**: Draft + reasoning trace to Priya queue; never auto-send | **Validation**: PoC + 200-ticket eval + Alex PII sign-off + Priya signs 50 sample drafts + 2-wk closed beta |
|  | **Metric tension**: Deflection rate vs CSAT — protect CSAT (Carlos's veto) |  |

#### Step 2: Candidate wedges + Outcome Risk Matrix

| Wedge | Value | Risk | Decision |
|---|---|---|---|
| Password reset only | Low (15%) | Low | De-prioritize |
| Classifier-only (route, don't draft) | Medium | Low | Defer to v1.5 |
| **Top-3 intents + draft + HITL approval** | **High (60% deflection ceiling)** | **Low (Priya approves)** | **Ship as v1** |
| Full Tier 1 auto-resolve no HITL | High | High (CSAT + GDPR exposure) | Defer to v2 |
| Tier 2 escalation triage | Medium | Medium | Defer to v1.5 |

**What I'd say**:
> "The wedge is option 3. Confidence over size. Auto-resolve would land more value, but the irreversibility of a bad customer-facing message in week 2 isn't worth the upside. We earn auto-resolve by shipping HITL first."

#### Step 3: Workforce design (6 agents)

| Agent | Job | Tier | Det / LLM | Why |
|---|---|---|---|---|
| 1. Intake classifier | Route to one of 3 intents or escalate | Haiku | Deterministic-leaning | Failure mode is silent if wrong → keep predictable |
| 2. PII scrubber | Strip email / phone / dealership name before LLM call | Deterministic | Rules | Reg failure is irreversible |
| 3. Context fetcher | Pull account state from Salesforce + product DB | Haiku + APIs | Hybrid | Reliability > creativity |
| 4. Drafter | Generate response from intent + context + KB | Sonnet | LLM | Synthesis is where LLMs win |
| 5. Quality + tone critic | LLM-as-judge with calibration on Priya's 50 labels | Sonnet | LLM | Catches what drafter misses |
| 6. Audit trace | Examiner-readable log per ticket | Deterministic | Det | Reliability-critical |

**Orchestration**: sequential pipeline with one branch (if PII scrubber or critic flags → Priya queue with reasoning trace; else → Priya for approval as normal).

**Integration**:
- Read pattern: API-based (Zendesk + Salesforce + product DB)
- Write pattern: holding queue (Zendesk private comment, not customer-visible)
- 3-tier ladder: v1 read-only + holding queue → v1.5 one-click approval write → v2 autonomous send for >Y% confidence

**Cost / latency**:
> "Per-ticket cost ~$0.08 on LLM layer; 1500 tickets/wk = ~$500/mo. P95 latency <10s. Sentinel saves ~150 hrs/wk × $40/hr loaded = $24K/wk. Pays back the engagement in week 1."

---

### Section 3 — Risk & Validation (~10 min)

#### Risks organized by bucket: Business | UX | Technical

Mirrors the 3-level metrics framework. Order matters in the interview: lead with Business (where the customer's pain lives), then UX (where adoption is won or lost), then Technical (where the engineering risk lives).

**What I'd say**:
> "I split risks into three buckets matching the metrics framework. Business risks are where renewal or audit exposure lives. UX risks are where the customer-facing experience breaks. Technical risks are where the system itself fails. Each has a mitigation, a named owner, and a detection signal."

##### Business risks (revenue, brand, regulatory exposure)

| Risk | Mitigation | Owner | Detection signal |
|---|---|---|---|
| PII leak into LLM prompt | Deterministic scrubber before any LLM call; immutable audit log of every scrub decision; 10x weighting on PII cases in eval | Alex (compliance) | Scrubber log shows untrusted tokens; quarterly Alex-led mock audit |
| CSAT drop → renewal risk | CSAT tracked as protected floor (≥4.0); v1 HITL catches regressions; rolling 7-day window; alerts on >2% drop | Sarah (buyer) | Weekly CSAT report; Carlos surfaces before Sarah does |
| Adoption failure (reps route around) | Track engagement separately from quality: "% drafts shipped without rep re-write"; target 70% by v1.5 | Marcus (champion) | Engagement <50% in week 2 means adoption problem, not quality |
| Regulatory audit failure (GDPR / SOC2) | Immutable audit trace per ticket; Alex-led mock audit before v2 promotion; versioned policy library | Alex (compliance) | Audit trace coverage <100% on sample request |

##### UX risks (customer-facing experience)

| Risk | Mitigation | Owner | Detection signal |
|---|---|---|---|
| Hallucinated answer reaches customer | Citation grounding to KB + Salesforce; critic flags ungrounded claims; deterministic guard against numbers not in source | Devin (tech) | Critic flag rate; customer correction reply; downstream re-open |
| Tone misread on negative-sentiment ticket | Sentiment classifier on intake; auto-escalate to human on negative sentiment; tone critic calibrated against Priya's 50 labels | Marcus (champion) | Per-intent CSAT below category baseline by >5% |
| Tier 2 ticket misclassified as Tier 1 | Classifier returns confidence score; below threshold routes to human; sentiment-based escalator on top of intent classifier | Marcus (champion) | Re-open rate; escalation-after-resolution rate; rep flag rate |
| Robotic / generic feel ("doesn't sound like us") | Drafter prompt includes Sentinel voice samples + Priya's style notes; tone critic checks for Sentinel phrasing | Priya (lead user) | Priya's edit rate on draft (high edit rate = robotic) |

##### Technical risks (system reliability)

| Risk | Mitigation | Owner | Detection signal |
|---|---|---|---|
| Model drift over weeks | Eval suite re-run every release; 7-day rolling drift detection on intent distribution; per-intent accuracy alert at >5% deviation | Devin (tech) | Drift >5% on any intent in rolling window |
| Vendor outage (Anthropic / OpenAI) | Failover to alternate provider on drafter (both BAAs in place); degraded mode = more direct-to-Priya routing | Devin (tech) | Provider status page; per-agent failure rate spike |
| Cost / latency spike | Per-agent cost + latency monitoring; tier-down option (Sonnet → Haiku on context fetcher); caching of KB queries + Salesforce data | Devin (tech) | P95 latency >15s; daily token spend >2x baseline |
| Integration schema change (Zendesk / Salesforce API) | Versioned schema contracts; alerting on extraction failure; weekly contract-test job | Devin (tech) | Extraction failure rate >2% |

#### 4-dimensional testing framework

1. **Static eval**: 200 cases (50 per intent + 50 adversarial) weighted by failure cost (PII leak 10x; wrong billing 5x; tone misread 2x)
2. **Pass^k=5**: variance ≤5% on production threshold
3. **Adversarial set**: PII smuggling cases, ambiguous-intent, hostile-customer-tone, multi-issue tickets
4. **Production observability**: drift on intent distribution + per-intent CSAT + escalation rate; weekly review with Priya

#### 3 sign-off criteria

1. Pass^k=5 with variance ≤5% on weighted eval — **Devin**
2. PII scrubber + audit trace sign-off — **Alex**
3. Priya reviews 50 sample drafts and confirms she'd put her name on each — **Priya**

**What I'd say to close**:
> "The metric tension is deflection vs CSAT. We protect CSAT — Carlos's veto is non-negotiable for the renewal book. The 3 sign-offs are the gate to production. After v1 ships, we promote to Tier 2 (one-click write) only after 90 days clean."

---

### Reverse Q&A (last 5 min)

- "What's the typical first-90-day FDE engagement at the company look like?"
- "What's the field-back-to-product loop in practice?"
- "What's a customer engagement that surprised you this year?"

---

### What this worked example demonstrates

- Restating the case in one sentence before doing anything else
- Naming the silent skeptic explicitly (the move most candidates miss)
- Using the 4-source convergence test by name
- Filling the 3-lens table fast, with the metric tension named
- Deriving 5 candidate wedges and scoring them on the Outcome Risk Matrix
- Naming the wedge with the "confidence over size" defense
- 6-agent decomposition with the shape catalog (classifier / scrubber / fetcher / drafter / critic / auditor)
- 3-tier integration ladder named
- 7 risks named proactively, each with a stakeholder owner
- 4-dimensional testing framework with weighted eval composition
- 3 named sign-off criteria with owners

If you can do this end-to-end in 60 minutes on whatever case the company throws at you, you'll hit the FDE bar.
