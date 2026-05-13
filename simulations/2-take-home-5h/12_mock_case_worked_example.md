# 12 — Helix Mock Case Worked Example (the live Review response)

> An end-to-end "what I'd actually say" walkthrough of the 60-min Helix Review round. Mirrors the Sentinel mock case in the Qurrent playbook, but uses Helix's actual stakeholders (Sarah, David, Rachel, Mei, Aditya, James, Carmen) and content (MNPI, citation grounding, earnings notes). Made-up numbers where credible; framework choices defended throughout.
>
> **Stays true to:** OpenAI Deployed PM emphasis (pass^k=5, eval suite as deliverable, configuration not fine-tuning, customer-first framing, production thinking). Sierra Agent Strategist principles (3-lens framework, Outcome Risk Matrix, confidence over size, sequencing, engagement gap as parallel track, read-only v1 as the senior move, principles-before-reactive, out-of-scope equally explicit, metric tension named, "strong but flawed > polished mediocre" mindset).

## How to use this file

Read this **after** files 09 (decision principles), 10 (3-lens applied), and 11 (solution depth + bucket risks). This file ties them together into a single live response. Use it as:
1. **The dress rehearsal** the day before your Review
2. **The script** to internalize for the opening 3-lens restatement
3. **The defense-anchoring template** for architecture pushback

---

## The case (as the interviewer has read it — Sarah's brief from `01_take_home_prompt.md`)

> Helix Capital, $2.3B long-short equity hedge fund. 12 investment professionals. 80 names across TMT, consumer, industrials. Every senior analyst spends 4 hours per name × 4 quarters drafting morning-after earnings notes. Two senior analysts quit in 2025 citing the grind. Zero MNPI incidents in 3 years. Build something for demo in 4 weeks; Rachel signs off on 20 sample drafts before rollout.

---

## Phase 1 — Framing (0:00 – 0:05)

### The opening restatement (90 seconds, using the 3-lens scaffold from file 10)

> "Let me restate the wedge in 3 lenses before I take questions.
>
> **Customer**: Rachel — senior TMT analyst, 9 years tenure, exhausted by the morning grind, anxious about a hallucinated number reaching a PM. The org has zero MNPI incidents in 3 years and lost two senior analysts in 2025 over the grind.
>
> **Product**: citation-grounded earnings draft with tone-shift detection in scope. M&A commentary, position-sizing, and any write explicitly out. Trust levels are deterministic on the dangerous calls (MNPI block, citation verify), ask-the-analyst on the soft calls (tone shifts), escalate on policy combinations. Metric tension is speed vs the zero-MNPI streak — we protect the streak.
>
> **Technical**: read-only v1, with MNPI watch-list drift as the one specific risk — mitigated by pulling the list at every invocation, plus Mei-owned audit log. Validation via pass^k=5 on a 50-case weighted eval + Mei + Rachel + Carmen sign-offs.
>
> That's the wedge. Happy to take questions in any order."

### Likely first probe + the defense

**Probe**: "Why this wedge, not the bigger one — auto-publishing notes after the agent's done?"

**Defense (Principle 1, confidence over size)**:
> "I optimize wedge selection on confidence of outcome, not size. Auto-publish would land more value but the irreversibility of a bad note reaching a PM in week 2 isn't worth the upside. v1 protects the kill-criteria (the MNPI streak + hallucination zero); v2 earns auto-publish by shipping read-only first and getting 90 days of clean Tier 2 behavior. Sequencing, not single-choice."

---

## Phase 2 — Discovery + current state (0:05 – 0:20)

### Stakeholder map (what I'd draw)

| Archetype | Person | Why |
|---|---|---|
| Economic buyer | Sarah Mendez (CIO) | Kill-criteria + renewal logic + zero-MNPI streak owner |
| Champion | David Park (Head of Research) | Brought us in; runs the coverage book day-to-day |
| Lead user | Rachel Kim (Senior TMT Analyst) | Will quietly route around if she doesn't trust |
| Silent skeptic | Carmen Diaz (Senior Trader) | Reads any AI-assisted note with extra skepticism |
| Tech owner | Aditya Sharma (CTO) | Owns Snowflake + Bloomberg/FactSet; one junior engineer |
| Compliance | Mei Liu (Compliance Officer) | Default-no; 4-regulator stack |
| Operations | James O'Brien (COO) | Infosec at this size; post-handoff cadence |

**What I'd say**:
> "Seven archetypes; the one most candidates miss for this case is Carmen. She's downstream of the note, not a primary user, but she's been burned by lazy analyst notes before and she's going to read agent-assisted notes with extra skepticism. If she flags one false-positive number to Sarah, the engagement narrative shifts overnight. I'd interview her in week 1 — not when she's already complaining."

### Information needed (organized by source)

| Source | What |
|---|---|
| People | Sarah's kill-criteria (already known); Rachel's 30-min workflow walkthrough with timestamps; Carmen's "what would make you reject this"; Mei's regulatory floor + audit standard |
| Data | 90 days of Rachel's earnings notes for voice samples; current cycle-time + accuracy benchmarks; ECTSum + SubjECTive-QA for eval calibration |
| Process | Existing compliance review process; MNPI watch list update cadence; current note distribution mechanism |
| External | SEC + FINRA + CFA examination patterns; Reg FD boundaries on M&A speculation |

### 4-source convergence (what I'd actually say)

> "I'd triangulate four sources before committing to the wedge. Sarah (buyer) says it's the morning grind + hallucination risk. The brief says it's earnings notes in 4 weeks. Industry says citation grounding + LLM-as-judge are the patterns that work for finance research. Rachel (operator) will tell me which of the 4 hours is genuinely productive analysis vs Zendesk navigation, formatting, verification. If all four converge on 'compress the verification + formatting time without losing the analysis', that's the wedge. If Rachel diverges — say she tells me the analysis itself is the slow part — I trust Rachel and re-scope."

### First 3 days

| Day | Interview | Output |
|---|---|---|
| Day 1 | David + Rachel | Stakeholder map; draft wedge hypothesis |
| Day 2 | Mei + Aditya | Regulatory boundary (MNPI watch list, audit standard); integration map |
| Day 3 | Carmen + James | Trust risk on the downstream reader; post-handoff ownership |
| End day 3 | Field memo to Sarah + internal | 1-page wedge proposal + 4-week plan |

---

## Phase 3 — Agent architecture (0:20 – 0:40)

### Step 1: 3-lens table (from file 10, restated quickly)

> "I filled the 3-lens table during discovery. Rachel is exhausted + anxious. In scope: citation-grounded draft + tone detection. Out of scope explicitly: M&A, position-sizing, auto-publish, multi-quarter. Read-only v1. MNPI watch-list drift as the one specific risk."

### Step 2: Candidate wedges + Outcome Risk Matrix (from file 09)

| Wedge | Value | Risk | Quadrant | Decision |
|---|---|---|---|---|
| Citation-grounded earnings draft (HITL) | High (4h → 30min) | Low (Rachel reviews) | High value / Low risk | **Ship as v1** |
| KPI quick-extract only | Low | Low | Low / Low | De-prioritize |
| Auto-tone-shift detection in isolation | Medium | High (mis-tagged tone = trading signal) | Med / High | Defer to v1.5 |
| MD&A diff with prior quarter | Medium | Medium | Med / Med | Defer to v1.5 |
| Position-sizing decision support | High in theory | Catastrophic (Chinese wall) | — | Out of scope permanently |
| Auto-publish to PMS | High in theory | Catastrophic (1 bug = trading loss + audit) | — | Out of scope permanently |

> "Wedge is option 1. Confidence over size. Auto-publish lives in v2."

### Step 3: 5 principles of AI workforce design (from file 11, named explicitly)

> "Before drawing agents, the 5 principles I'm applying: decompose by failure mode not feature; deterministic gates around dangerous calls; read before write; one job per agent; orchestrator is dumb / agents are smart."

### Step 4: Workforce decomposition (7 agents, mapped to shapes from file 11)

| Helix agent | Shape | Tier | Det / LLM | Why |
|---|---|---|---|---|
| 1. MNPI Scrubber | Compliance critic | Deterministic | Rules | Fund-shutting if missed; non-negotiable |
| 2. Intake classifier | Classifier | Haiku | Det-leaning | Routes by ticker / sector / call type |
| 3. KPI Extractor | Extractor | Haiku | Hybrid | Reliability over creativity |
| 4. Note Drafter | Synthesizer | Sonnet | LLM | Synthesis is where LLMs uniquely win |
| 5. Tone Supervisor | Critic / judge | Sonnet | LLM-as-judge with SubjECTive-QA calibration | Soft errors the Drafter missed |
| 6. Citation Verifier | Compliance critic | Deterministic | Rules + regex | Hallucinated number = irreversible reputational hit |
| 7. Audit Trace Generator | Auditor | Deterministic | Det | Examiner-readable log |

### Step 5: Orchestration + integration (from file 11)

> "Pattern: sequential pipeline with parallel critics and one conditional branch. Scrubber fires first — if it triggers, no LLM call happens. Then Intake → Extractor → Drafter → Tone + Citation Verifier in parallel → if any critic flags, route to Rachel with reasoning; else, holding queue + audit trace. The orchestrator is dumb — state, retry, idempotency, observability. Business logic in the agents."

> "Integration: read-only first. API on Bloomberg + Mei's compliance system; file ingestion on transcripts; DB direct on prior-quarter notes. Write only to a Postgres holding queue Rachel approves. No writes to PMS, trader distribution, or analyst's published folder in v1. 3-tier ladder: v1 holding queue → v1.5 approval-gated write to PMS → v2 autonomous publish for highest-confidence single-sector cases. Each tier gated on the prior tier being clean for 90 days."

### Step 6: Cost / latency

> "Per-note ~$0.40 on the LLM layer. 80 names per quarter = $32 per quarter. Immaterial vs the engagement value. P95 latency end-to-end ~45 seconds, mostly Drafter; Verifier and Tone parallelized. The constraint isn't LLM cost — it's analyst review time and compliance review cycles."

### Predictable architecture probes + the defenses

| Probe | Defense |
|---|---|
| "Why MNPI Scrubber first?" | Principle 2 (deterministic gates around dangerous calls). MNPI leak is fund-shutting; the Scrubber fires before any LLM call. If it triggers, no LLM call ever happens. |
| "Why Sonnet for Drafter and Haiku for Extractor?" | I split tier choices on synthesis vs extraction. Drafter is synthesis-heavy (transcript + KPIs + prior note); volume is 80 notes / quarter so Sonnet's cost is immaterial. Extraction is structured; Haiku is sufficient and reliable. |
| "Why deterministic Citation Verifier, not LLM-as-judge?" | Failure-mode reversibility. Hallucinated number reaching a PM is irreversible; tone misread is reversible. Verifier guards the irreversible failure, so it has to be deterministic. Tone Supervisor can be LLM-as-judge because tone errors get caught in review. |
| "Why not fine-tune on Helix's historical notes?" | Configuration over fine-tuning. Prompt engineering with Rachel's last 20 notes as voice samples + LLM-as-judge calibration handles 90% of the voice match. Fine-tuning adds operational surface (data pipeline, eval, retraining cadence) that's premature for v1. v2 conversation if v1 voice-match is genuinely insufficient. |
| "What if Anthropic has an outage?" | Failover to OpenAI on Drafter + Tone Supervisor (both BAAs in place per the brief — Anthropic active, OpenAI in evaluation). Degraded mode = more direct-to-Rachel routing. Don't auto-fail; degrade gracefully. |
| "How does this scale to 10x volume?" | Decomposition makes the scaling problem about which agent's bottleneck. Drafter scales linearly with cost (still immaterial at 800 notes/qtr = $320). Verifier scales sub-linearly (deterministic, cached). Tone Supervisor is the variable cost; could tier-down to Haiku if needed. The architecture supports 10x without redesign. |

---

## Phase 4 — Risk + path to production (0:40 – 0:55)

### Risks organized by bucket (from file 11)

**What I'd say**:
> "I split risks into three buckets matching the metrics framework. Business risks are where SEC scrutiny + reputational damage live. UX risks are where Rachel either trusts the agent or routes around it. Technical risks are where the system fails. Each has a mitigation, a named owner, and a detection signal."

#### Business risks

| Risk | Mitigation | Owner | Detection |
|---|---|---|---|
| MNPI leak | Deterministic Scrubber; per-invocation watch-list pull; audit log; 10x eval weight | Mei | Scrubber bypass; quarterly mock audit |
| Hallucinated number reaches PM | Citation Verifier (det) on every number; no number leaves without source link | Sarah + Aditya | Verifier flag rate; PM post-trade question |
| Adoption failure — Rachel re-drafts | Engagement metric separate from quality: "% notes Rachel ships without re-draft"; target 70% by v1.5 | David | Engagement <50% in week 2 = adoption issue |
| SEC / FINRA audit failure | Immutable audit trace; Mei-led mock audit before v2 | Mei | Audit trace coverage <100% on sample |

#### UX risks

| Risk | Mitigation | Owner | Detection |
|---|---|---|---|
| Tone misread (bullish frame on cautious guidance) | Tone Supervisor calibrated on 100 SubjECTive-QA examples; auto-escalate on confidence-low | David | Per-call analyst-trust metric below baseline |
| Citation chain broken | Verifier requires source-line link for every number; broken chain = block, not warn | Rachel | Rachel's verification time per note |
| Multi-quarter context missing | Explicitly out of v1; v1.5 retrieval | Rachel | Rachel flags missing context > X% |
| Robotic / non-Helix voice | Drafter prompt includes Rachel's last 20 notes; Tone Supervisor checks Helix phrasing | Rachel | Rachel's edit rate on draft body |

#### Technical risks

| Risk | Mitigation | Owner | Detection |
|---|---|---|---|
| Model drift on KPI extraction | Eval re-run every release; 7-day rolling drift detection; >5% deviation alert | Aditya | Drift >5% on any KPI |
| MNPI watch list drift | Per-invocation pull (not cached); Mei-owned audit log | Mei | Watch-list-pull frequency vs Mei's updates |
| Vendor outage | Failover Anthropic ↔ OpenAI; degraded mode = more Rachel routing | Aditya | Provider status; failure rate spike |
| Bloomberg / FactSet API change | Versioned schema contracts; weekly contract-test | Aditya | Extraction failure rate >2% |
| Cost / latency spike | Per-agent monitoring; tier-down options analyzed | Aditya | P95 >60s; daily cost >2x baseline |

### 4-dimensional testing framework

1. **Static eval**: 50+ cases (10 per major risk) weighted by failure cost (MNPI leak 10x, hallucinated number 5x, tone misread 2x)
2. **Pass^k=5**: variance ≤5% across runs as production threshold (the OpenAI emphasis)
3. **Adversarial set**: MNPI smuggling cases, ambiguous-tone management commentary, position-sizing slip, multi-issue earnings calls
4. **Production observability**: 7-day rolling drift on KPI extraction; per-name CSAT-equivalent (analyst trust); weekly review with Rachel

### 3 sign-off criteria with stakeholder owners

1. **Pass^k=5 with variance ≤5% on weighted eval** — Aditya
2. **MNPI Scrubber + audit trace standard sign-off** — Mei
3. **Rachel reviews 20 sample drafts and confirms she'd put her name on each** — Rachel

### Metric tension named

> "The tension is speed vs the zero-MNPI streak. We protect the streak. Rachel reviews a borderline note in 45 min rather than ship a wrong number in 25 min. The streak is the engagement's reputation."

---

## Phase 5 — Reverse Q&A (0:55 – 1:00)

What I'd ask:

- "What's the typical FDE engagement at OpenAI / Sierra / Anthropic look like in the first 90 days?"
- "What's the field-back-to-product loop in practice? When I find a config-vs-fine-tune insight, how does that get back to the product team?"
- "What's the failure mode of a new FDE you've seen most often?"
- "What's a customer engagement that surprised you this year?"

---

## What this worked example demonstrates

A condensed checklist of moves it executes:

- Opens with the 3-lens restatement (Sierra principle: insight first, not activity)
- Defends the wedge with "confidence over size" before any probe (file 09, Principle 1)
- Names Carmen as the silent skeptic in stakeholder mapping (file 09: relationship over headcount)
- Uses 4-source convergence by name (process maturity signal)
- Walks through the 3-lens table from file 10 fast
- Scores 6 candidate wedges on the Outcome Risk Matrix (file 09, Principle 2)
- Names the 5 principles of AI workforce design before drawing agents (file 11)
- Maps 7 agents to shapes from the catalog (file 11)
- Names orchestration pattern + read/write patterns explicitly (file 11)
- Defends with "configuration, not fine-tuning" (Sierra ADLC + OpenAI emphasis)
- Names the engagement gap as the parallel track (file 09, Principle 4)
- Risks organized into Business / UX / Technical buckets with detection signals (file 11)
- Pass^k=5 named explicitly (OpenAI emphasis)
- 3 sign-off criteria with named owners (file 09)
- Metric tension named: speed vs zero-MNPI streak (Sierra principle)
- Read-only v1 framed defensively, not apologetically (file 09, Principle 6)
- Closes with the strong-but-flawed mindset reminder (Sierra + OpenAI shared culture)

If you can do this end-to-end on the Helix case (or any structurally similar case), you'll hit the FDE final-round bar.

## The mindset reminder

You don't have to be perfect. Frontier labs reward strong-but-flawed candidates over polished mediocre ones. Defend with substance. Admit gaps with intellectual honesty. Lead with substance over polish. The interviewer is looking for whether you'd be safe to put in front of their flagship customer next quarter, not whether you can recite a perfect script.
