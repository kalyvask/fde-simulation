# Wedge Proposal — Helix Capital Earnings-Note AI Workforce v1

**Companion to**: `HELIX_BRIEF.md`
**From**: FDE Lead
**For**: Sarah Mendez (CIO), David Park (Head of Research), Rachel Kim (lead user), Mei Liu (Compliance), Aditya Sharma (CTO)
**Decision needed**: sign-off to build by Friday-of-week-3

## The wedge in one paragraph

Build an AI workforce that drafts the morning-after-earnings analyst note for portfolio managers, scoped to coverage names with standard earnings call format. The agent ingests the call transcript + the latest 10-Q + prior 4 quarters of notes + consensus estimates, then produces a 1-page draft note covering: KPI extraction with per-number citations, prior-quarter deltas on key metrics, tone-shift detection vs prior calls, MD&A risk-factor diff, and a draft commentary section. The agent does **not** include M&A commentary, position-sizing recommendations, or any content touching names on the MNPI watch list. Every output ships with a citation-faithful audit trail. The senior analyst reviews + edits + signs before compliance review and publication.

## Why this slice

Five reasons:

1. **Direct hit on Sarah's kill-criteria #1**: hallucinated numbers. By making citation-grounding deterministic and forbidding LLM-sourced numbers, we engineer out the worst-case from day 1.
2. **No MNPI exposure**: by scoping to public earnings-call + filing data, the agent never sees MNPI. Mei's biggest concern is addressed architecturally, not procedurally.
3. **Highest leverage in the firm's workflow**: 1,120 hours saved per analyst per year × 5 senior analysts = 5,600 hours/year = the entire engagement pays for itself in week 1.
4. **Senior-analyst-veto-friendly**: drafts only. Rachel keeps full ownership of the published artifact. The agent is her tool, not her replacement.
5. **Reusable across funds**: every long-short equity fund has this workflow. The patterns from Helix port directly to Morgan Stanley, Bridgewater, Citadel — Sarah's first ask after success will be "can we run this for the consumer book too?"

## The agent workforce

9 specialized agents + a supervisor pattern. Each runs a single concern.

| Agent | Job | Tools | Model tier | Det / LLM |
|---|---|---|---|---|
| 1. MNPI Scrubber | Block any prompt touching the watch list; first-line defense | Watch-list lookup | n/a | Deterministic |
| 2. Intake | Parse transcript + 10-Q + prior notes + consensus into a normalized claim object | Document parsers | Haiku | Deterministic (LLM only as fallback) |
| 3. KPI Extractor | Extract revenue, EPS, gross margin, guidance with span-level citations | Structured output | gpt-4o-mini / Haiku | LLM with span grounding |
| 4. Consensus Comparator | Diff extracted KPIs against consensus estimates | Refinitiv lookup | n/a | Deterministic |
| 5. Tone-Shift Detector | Compare management language vs prior calls; flag shifts | Embeddings + SubjECTive-QA rubric | gpt-4o / Sonnet | LLM with calibrated rubric |
| 6. Risk-Factor Diff | MD&A risk-section diff vs prior quarter | Text diff + LLM summary | gpt-4o-mini / Haiku | Det diff + LLM summary |
| 7. Note Drafter | Synthesize the 1-page draft from extracted facts only | Anthropic Sonnet / gpt-4o | Sonnet / gpt-4o | LLM |
| 8. Citation Verifier | Every number in the draft must trace to a source span | Span matcher | n/a | Deterministic |
| 9. Compliance Critic | Run Mei's rules (no M&A, no position sizing, no MNPI watch list) | Rules engine | n/a | Deterministic |

Supervisors:
- **Tone-Shift Calibration** (LLM-as-judge): grades Tone-Shift Detector against held-out human-graded samples
- **Draft Quality** (LLM-as-judge): grades note against Rachel's quality rubric (analogue to Janet's 5-element bar in Calder)

## What "working" means (measurable)

| Metric | Target | Baseline | Source |
|---|---|---|---|
| Time analyst spends per note | <30 min review | 4 hours | Sarah's stated goal |
| Note publication latency (post-call) | <1h | 4-18h | David's process audit |
| Citation faithfulness on numbers | 100% | n/a | Sarah's kill-criteria #1 |
| KPI extraction precision (vs human grader) | ≥95% | n/a | Rachel's bar |
| Hallucinated guidance rate | 0% | n/a | Sarah's kill-criteria #1 |
| MNPI watch-list violations | 0 | n/a | Mei's bar |
| Senior analyst acceptance rate | ≥18/20 send-ready | n/a | Rachel's review |
| Tone-shift detection F1 (vs SME labels) | ≥0.80 | n/a | Rachel + David |
| Compliance review pass rate (first-pass) | ≥90% | n/a | Mei |
| Latency p95 (full pipeline) | <120s | n/a | FDE craft default |

The citation-faithfulness and hallucinated-guidance metrics are weighted 10x in the eval suite — they directly map to Sarah's kill-criteria.

## Eval design (the intellectual content)

- **Seed set**: 30 historical Helix-covered earnings calls (David sources from research archive) — 20 well-handled + 10 hard-cases-where-analyst-caught-something
- **Public augmentation**: EDGAR-CORPUS (40GB, 6+ billion tokens) for narrative-extraction stress tests; ECTSum for tone-shift benchmarks; SubjECTive-QA for 6-dimensional subjectivity labels
- **Adversarial set**: 30 hand-built failures targeting hallucinated guidance, mid-narrative entity drops, MNPI smell-tests (e.g., a name on watch list smuggled into prompt), citation-misalignment edge cases, post-Q&A tone-shift detection
- **Regression**: every fixed bug → permanent case (the agent development lifecycle)
- **Calibration**: Brier score on hallucinated-guidance routing; reliability diagram per analyst sector slice
- **Per-name slicing**: separate eval slices per sector (TMT / consumer / industrials) and per-analyst owner

## 4-week plan

| Week | Deliverable | Owners |
|---|---|---|
| 1 (in progress) | Discovery memo + this proposal + Mei's MNPI scrubber spec + James's data-handling one-pager | Alex |
| 2 | Eval suite v1 (30 cases + adversarial 30 + per-sector slices); sandbox access on Helix's Snowflake-Python | Alex + David + Sienna-equivalent |
| 3 | Prototype agent workforce; Rachel 20-draft review; Mei policy library encoded | Alex + Aditya |
| 4 | Production hardening: citation-trace renderer, hallucination death-spiral monitor, on-call doc; Rachel sign-off; field memo to OpenAI | Alex + David |

End-of-week-4: live wedge demo + handoff to David's team + ongoing operational owner (Helix's equivalent of Hassan TBD in discovery).

## What we need from Helix

| Ask | Owner | Date |
|---|---|---|
| James one-pager sign-off on data handling | James (COO) | Friday this week |
| Mei MNPI watch-list export + escalation rules | Mei | EOD Friday |
| David: 30 historical notes pull for seed eval set | David | EOD Tuesday next week |
| Aditya: Snowflake schema review + Python research-stack credentials | Aditya | EOD Wednesday next week |
| Bloomberg/FactSet API documentation | Aditya | Wednesday next week |
| Sample earnings call transcripts (already-published names, 5 names) | David | Friday next week |
| Rachel 20-draft review session (week 3) | David → Rachel | Week 3 |
| Standing weekly with Sarah | Sarah | Fridays 4:30 (or her slot) |

## Risks + mitigations

| Risk | Mitigation |
|---|---|
| Hallucinated guidance reaching draft | Citation Verifier deterministic; LLM cannot source numbers; every cited value traces to source span; 10x eval weighting |
| MNPI smuggled into prompt | MNPI Scrubber first agent; watch-list deterministic check; blocks before LLM call |
| Tone-shift detector miscalibration | SubjECTive-QA labels + Rachel-graded held-out set; LLM-as-judge calibration before trust |
| Multi-document context loss (10-K + 4 prior quarters + transcript) | Chunked retrieval over EDGAR-CORPUS embeddings; explicit entity-preservation prompts; long-context audit |
| Vendor BAA gap (OpenAI in evaluation) | Anthropic-only in v1; OpenAI added once BAA closes |
| Senior analyst veto (Rachel) | Her 20-draft review in week 3 = the rollout gate; her quality bar is the eval rubric |
| Chinese-wall breach (research agent gains trading-system access) | Hard architectural separation; agents run in research VPC; no DNS path to trading systems |
| RPA-style ownership-after-handoff failure | Hassan-equivalent named in discovery (TBC); daily 15s for 14 days; weekly through Q4 |

## What this wedge does NOT do (explicitly out of v1)

- Does not write M&A commentary (regulatory minefield)
- Does not include position-sizing recommendations (cross-Chinese-wall)
- Does not touch names on the MNPI watch list
- Does not generate independent investment theses (the analyst still owns the thesis)
- Does not auto-publish (always senior-analyst-reviewed + compliance-approved)
- Does not handle non-equity asset classes (fixed income, FX, commodities)
- Does not run on real-time market data (transcript + filing data only)
- Does not cover names outside Helix's coverage book

## Decision request

Sign-off to build the v1 wedge as scoped, with the 4-week plan and the asks above. By end of week 3 we will have eval data on the citation-faithfulness and hallucinated-guidance dimensions; we can renegotiate scope or extend if signal warrants.

— Alex
