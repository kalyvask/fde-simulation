# 11 — Solution Strategy Depth + Bucket Risks for Helix

> Companion to file 10 (`10_3_lens_applied_to_helix.md`). File 10 has the 3-lens table for the Helix earnings-note wedge. This file goes a layer deeper on Solution Strategy: workflow decomposition, agent shapes, orchestration patterns, integration read/write patterns, cost/latency budget. It also reorganizes the risk discussion into Business / UX / Technical buckets with detection signals.
>
> **Stays true to:** OpenAI Deployed PM emphasis (pass^k=5, eval suite as deliverable, configuration not fine-tuning, customer-first framing, production thinking). Forward Deployed Engineer principles (3-lens framework, Outcome Risk Matrix, confidence over size, sequencing, engagement gap as parallel track, read-only v1 as the senior move, principles-before-reactive, out-of-scope equally explicit, metric tension named).

## The 5 principles of AI workforce design (Helix application)

When the interviewer says "walk me through the architecture", these 5 principles are what you're applying. Name them out loud before drawing agents. Each one defends a specific probe.

| Principle | Helix application | Probe it defends against |
|---|---|---|
| **1. Decompose by failure mode, not by feature** | MNPI Scrubber is separate from Drafter because regulatory leak is irreversible; bad synthesis is reversible. Citation Verifier is separate from Tone Supervisor for the same reason. | "Why these agent boundaries?" |
| **2. Deterministic gates around the dangerous calls** | MNPI Scrubber + Citation Verifier are both deterministic. LLMs handle the soft work (drafting, tone judgment); rules handle the kill-criteria calls. the agent development lifecycle discipline: configuration over fine-tuning. | "Why not LLM-as-judge for citation?" |
| **3. Read before write, always** | Read freely from Bloomberg + FactSet + prior-quarter notes. Write only to a holding queue Rachel approves. Never to the PMS, trader distribution, or analyst's published folder in v1. | "Why no auto-publish?" |
| **4. Each agent has ONE job** | KPI Extractor only extracts. Drafter only drafts. Verifier only verifies. Splitting prevents one agent from cascading failures across responsibilities. | "Why so many agents?" |
| **5. Orchestrator is dumb; agents are smart** | Orchestration is sequential + branching + retry. Intelligence lives in the agents. The Drafter doesn't know about MNPI rules; the Scrubber doesn't know about KPIs. | "How does this scale to 10x volume?" |

## Workflow decomposition for the Helix earnings note (5-step method)

How Helix's 7 agents were derived from Rachel's manual workflow. The senior FDE move is showing the decomposition is mechanical, not improvised.

### Step 1 — Map the manual workflow as a swimlane

Rachel's current process the morning after an earnings call:
1. Read prior quarter's note + consensus estimates
2. Listen to call live (or read transcript after)
3. Extract KPIs (revenue, segment results, guidance figures)
4. Note tone shifts vs prior quarter's management commentary
5. Draft note structure (headline + key takeaways + KPI table + tone commentary)
6. Verify every number against transcript or filings
7. Compliance self-check (no MNPI, no position-sizing, no M&A speculation)
8. Send to PM + trader desk

### Step 2 — Identify decision points vs execution points

- **Decisions (2)**: "Is this MNPI?" (binary, deterministic), "Does tone shift warrant a flag?" (graded, LLM)
- **Execution (6)**: read prior, extract KPIs, draft structure, verify numbers, compliance check, send

### Step 3 — Group execution points by data + tier requirements

- Extract KPIs (transcript + consensus, structured data) → **Haiku** / Extractor shape
- Draft note (transcript + KPIs + prior note, synthesis) → **Sonnet** / Synthesizer shape
- Verify numbers (draft + transcript, deterministic comparison) → **Deterministic** / Compliance critic shape

### Step 4 — Add critics at every irreversible step

- **Before any LLM call**: MNPI Scrubber (deterministic) — fund-shutting if missed
- **Before send**: Citation Verifier (deterministic) — wrong number = trading loss
- **Before send**: Tone Supervisor (LLM-as-judge) — soft error catch with SubjECTive-QA calibration

### Step 5 — Add routing for confidence-low cases

- Drafter confidence threshold → Rachel's queue with reasoning trace
- Tone Supervisor flag → Rachel review
- Compliance Critic flag → escalate to Mei

**Output**: 7 agents, derived mechanically from the 8-step workflow + 2 decisions + 4 critic / routing additions.

## Agent shapes catalog (mapping Helix's 7 agents to standard shapes)

| Helix agent | Shape | Tier | Det / LLM | Why this shape |
|---|---|---|---|---|
| MNPI Scrubber | **Compliance critic** | Deterministic | Rules | Fund-shutting failure; reliability is non-negotiable |
| Intake classifier | **Classifier** | Haiku | Deterministic-leaning | Routes by ticker / sector / call type |
| KPI Extractor | **Extractor** | Haiku | Hybrid (regex + LLM for unstructured fields) | Reliability over creativity on numbers |
| Note Drafter | **Synthesizer / drafter** | Sonnet | LLM | Synthesis across transcript + KPIs + prior note is where LLMs uniquely win |
| Tone Supervisor | **Critic / judge** | Sonnet | LLM-as-judge with SubjECTive-QA calibration | Soft errors the Drafter missed |
| Citation Verifier | **Compliance critic** (specialized) | Deterministic | Rules + regex | Hallucinated number = irreversible reputational hit |
| Audit Trace Generator | **Auditor** | Deterministic | Deterministic | Examiner-readable log; reliability-critical for SEC review |

**The senior move when probed "why these agents"**: "I picked from the 7-shape catalog by failure-mode boundary. Compliance critics around the irreversible failures (MNPI, citations); synthesizer for the natural-language work; auditor for examiner-readable logging. Configuration, not fine-tuning."

## Orchestration pattern (how Helix's agents coordinate)

**Pattern**: Sequential pipeline with parallel critics and one conditional branch.

```
MNPI Scrubber → Intake → KPI Extractor → Drafter → (Tone Supervisor || Citation Verifier) → Branch:
   if any critic flags → Rachel's review queue with reasoning trace + Audit Trace
   else → Holding queue + Audit Trace
```

### Orchestrator responsibilities

| Responsibility | What it does |
|---|---|
| State | Per-call session ID; every agent output persisted to the audit trace |
| Retry | Max 1 retry on transient failures (timeout, rate limit); no retry on critic flags (those go to Rachel) |
| Idempotency | Re-running the workflow on the same earnings call produces the same draft (deterministic seed on Drafter; cached source pulls) |
| Observability | Every agent's input + output + latency + cost logged for the audit trace + drift detection |

**The defense if probed**: "The orchestrator is intentionally dumb. Sequential + parallel critics + one branch + retry. Business logic lives in the agents. Keeps the orchestrator stable while the agents iterate. This is the the agent development lifecycle pattern."

## Integration patterns (reads and writes for Helix)

### Read patterns

| Source | Pattern | Why |
|---|---|---|
| Earnings transcripts | **File ingestion** (FactSet S3 drop) | Batch, post-call; reliability over latency |
| Bloomberg consensus | **API-based** (read-only sandbox per the brief) | Real-time, structured |
| Prior-quarter notes | **DB direct** (internal Postgres on Snowflake-Python sandbox) | Internal data; lower latency |
| MNPI watch list | **API-based** (Mei's compliance system) | Auth-controlled; **per-invocation pull, not cached** |
| Audit standard | **DB direct** (internal) | Reliable, slow-changing |
| SubjECTive-QA labels | **File ingestion** (one-time, for eval calibration) | Static reference data for LLM-as-judge calibration |

### Write patterns

| Target | Pattern | When |
|---|---|---|
| Draft note | **Holding queue** (Postgres staging table, Rachel-approver UI) | v1 |
| Audit trace | **Direct write to immutable log** (append-only) | v1 (always on) |
| Approved note → PMS | **Approval-gated** (Rachel one-click after review) | v1.5 |
| Approved note → trader distribution | **Approval-gated** (Rachel + Carmen one-click on the first 90 days post-promotion) | v1.5 |
| High-confidence cases auto-publish | **Direct write with audit** | v2, after pass^k=5 + 90 days clean Tier 2 + Mei external-audit pass |

### The 3-tier integration ladder ( sequencing applied)

| Tier | What it does | When | Gate to next tier |
|---|---|---|---|
| **Tier 1 (v1, weeks 1-4)** | Read freely; write to holding queue + audit trace only | Ship after Mei + Rachel + Carmen sign-off | Pass^k=5 on 50-case weighted eval + 20-sample analyst sign-off |
| **Tier 2 (v1.5, weeks 5-12)** | Approval-gated write to PMS + trader distribution | After 90 days Tier 1 clean | Engagement metric ≥70% adoption (Rachel ships agent's draft without re-write) |
| **Tier 3 (v2, weeks 13+)** | Autonomous publish for highest-confidence cases (single-sector, single-quarter, clean MNPI) | After 90 days Tier 2 clean + external audit pass | Customer-specific gates (Sarah + Mei + board-level) |

**The defense if probed "why no auto-publish in v1"**: "Write access in v1 means a wrong draft becomes a wrong PMS record. Read-only keeps the failure mode at 'Rachel catches it in review' — recoverable. We earn auto-publish by shipping read-only first. best-practice sequencing."

## Cost and latency budget

| Dimension | Helix number |
|---|---|
| **Cost per earnings note (LLM layer)** | ~$0.40 (Sonnet Drafter $0.20, Sonnet Tone Supervisor $0.10, Haiku KPI Extractor $0.05, deterministic agents + audit ~$0.05) |
| **Notes per quarter** | 80 names × 1 quarter = 80 |
| **Total LLM cost per quarter** | ~$32 (immaterial vs $5M+ savings from 1,280 hr/yr/analyst recovered) |
| **P95 latency end-to-end** | ~45 seconds (Drafter ~15s, Verifier ~5s, Tone Supervisor ~10s parallelized, others <5s combined) |
| **Cache-eligible** | Prior-quarter notes (changes once per quarter), SubjECTive-QA reference data; **NOT MNPI watch list** (per-invocation pull) |
| **Tier-down options if needed** | Drafter Sonnet → Haiku (degrades synthesis quality — NOT recommended); Tone Supervisor Sonnet → Haiku (degrades calibration); deterministic agents already at floor |

**The defense if probed "what's your cost ceiling"**: "Per-note $0.40 in v1. Immaterial vs the engagement value. The constraint isn't LLM cost. It's compliance review cost and analyst review time. Cost stays predictable because deterministic agents handle the irreversible failures; LLMs handle the soft work."

## Risks organized by bucket: Business | UX | Technical

Mirrors the 3-level metrics framework already in `09_decision_principles.md`. Lead with Business (where SEC scrutiny + fund-shutting lives), then UX (where Rachel's trust is won or lost), then Technical (where engineering breaks).

**What to say in the Review**:
> "I split risks into three buckets matching the metrics framework. Business risks are where SEC scrutiny and reputational damage live. UX risks are where Rachel either trusts the agent or routes around it. Technical risks are where the system itself fails. Each has a mitigation, a named owner, and a detection signal."

### Business risks (revenue, brand, regulatory exposure)

| Risk | Mitigation | Owner | Detection signal |
|---|---|---|---|
| **MNPI leak** into LLM prompt | Deterministic MNPI Scrubber pulls watch list at every invocation; immutable audit log of every scrub decision; 10x weighting on MNPI cases in eval | Mei (Compliance) | Scrubber bypass; quarterly Mei-led mock audit |
| **Hallucinated number reaches PM** → trading loss + SEC scrutiny | Citation Verifier (deterministic) on every numerical claim; no number leaves the agent without a transcript / filing source line | Sarah (CIO) + Aditya (CTO) | Verifier flag rate; PM raises a question post-trade |
| **Adoption failure** — Rachel re-drafts from scratch | Engagement metric tracked separately from quality: "% covered names where Rachel ships agent's draft without re-write"; target 70% by v1.5 (per `09_decision_principles.md`, Principle 4) | David (Head of Research) | Engagement <50% in week 2 = adoption problem, not quality problem |
| **Audit failure** (SEC / FINRA examination of v2 autonomous publishing) | Immutable audit trace per note; quarterly external review; Mei-led mock audit before v2 promotion | Mei | Audit trace coverage <100% on sample request |

### UX risks (analyst-facing experience)

| Risk | Mitigation | Owner | Detection signal |
|---|---|---|---|
| **Tone misread on management commentary** (bullish framing of cautious guidance) | Tone Supervisor calibrated against 100 SubjECTive-QA labeled examples; auto-escalate on confidence-low cases | David (Head of Research) | Per-call analyst-trust metric below baseline |
| **Citation chain broken** (analyst forced to verify line-by-line) | Citation Verifier requires source-line link for every number; broken chain = block, not warn | Rachel (Lead User) | Rachel's verification time per note (high = chain broken) |
| **Multi-quarter context missing** (v1 limitation) | Explicitly out-of-scope for v1; v1.5 adds prior 4 quarters via retrieval | Rachel | Rachel flags missing context > X% of notes |
| **Robotic / non-Helix voice** (doesn't sound like Rachel's notes) | Drafter prompt includes Rachel's last 20 notes as voice samples; Tone Supervisor checks for Helix-style phrasing | Rachel | Rachel's edit rate on draft body (high = robotic) |

### Technical risks (system reliability)

| Risk | Mitigation | Owner | Detection signal |
|---|---|---|---|
| **Model drift on KPI extraction** (LLM behavior changes over weeks) | Eval suite re-run every release; 7-day rolling drift detection on extraction accuracy; per-KPI alert at >5% deviation | Aditya (CTO) | Drift >5% on any KPI in rolling window |
| **MNPI watch list drift** (Mei updates mid-quarter, Scrubber works off stale cache) | Scrubber pulls watch list at start of every invocation (not at startup); Mei-owned audit log of Scrubber decisions | Mei | Watch-list-pull frequency vs Mei's update frequency |
| **Vendor outage** (Anthropic / OpenAI) | Failover to alternate provider on Drafter + Tone Supervisor (both BAAs in place; OpenAI in evaluation per the brief); degraded mode = more direct-to-Rachel routing | Aditya (CTO) | Provider status page; per-agent failure rate spike |
| **Bloomberg / FactSet API change** | Versioned schema contracts; alerting on extraction failure; weekly contract-test job | Aditya (CTO) | Extraction failure rate >2% |
| **Cost / latency spike** | Per-agent cost + latency monitoring; tier-down options analyzed; cache prior-quarter notes (not MNPI watch list) | Aditya (CTO) | P95 latency >60s; daily cost >2x baseline |

## How this file flows into the deck and the Review

| Use this for... | What goes where |
|---|---|
| Slide 2 (architecture) | Agent shapes mapping + orchestration pattern + read/write patterns |
| Slide 3 (risks + testing) | Bucket-organized risks (Business / UX / Technical) with detection signals |
| Hour 2 of the take-home | Use the 5-step workflow decomposition to derive the agents |
| Review opening | 3-lens restatement from file 10, then drill into agent shapes |
| Review architecture defense | Anchor every probe to a principle from the 5 + a lens from file 10 |
| Review risk defense | Bucket-organized risks with detection signals; "I'd know X was going wrong because Y" |

## The mindset (reaffirmed)

You don't have to be perfect. Frontier labs reward strong-but-flawed candidates over polished mediocre ones. Defend with substance. Admit gaps with intellectual honesty. Lead with substance over polish. When the interviewer probes a depth you don't have, say "I don't have a good answer for that yet; my instinct is X, but I'd want to validate by Y before committing." That's a stronger signal than fabricated certainty.
