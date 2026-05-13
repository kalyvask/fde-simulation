# Wedge Build Plan — Helix Capital Earnings-Note AI Workforce v1

> Companion to `wedge_proposal.md`. Tactical task roadmap from discovery through Friday-week-4 demo.

## The wedge (one-line)

Citation-grounded earnings-note AI workforce for Helix Capital's morning-after analyst note workflow. Drafts only; MNPI architectural wall; full audit trace. Senior analyst + compliance review before publication.

## Critical path (the spine)

```
James one-pager sign-off → Mei MNPI watch list → MNPI Scrubber wired
                                                      ↓
David note pull → Sienna-equivalent eval set → Eval suite v1
                                                      ↓
Aditya + Kayla-equivalent → Sandbox + Snowflake access → Agent integration
                                                      ↓
Rachel 20-draft review → Production gate
                                                      ↓
Carmen hostile review → Trader-side acceptance
```

## Week 1 — Discovery + alignment (in progress)

| # | Task | Owner | Status |
|---|---|---|---|
| 1.1 | Sarah kickoff | Alex | DONE |
| 1.2 | Recap email to Sarah | Alex | DONE |
| 1.3 | Discovery memo | Alex | DONE |
| 1.4 | Wedge proposal | Alex | DONE |
| 1.5 | James data-handling one-pager | Alex | DUE Friday this week |
| 1.6 | Mei MNPI watch-list spec request | Alex | DUE EOD Friday |
| 1.7 | David interview + note-pull request | Alex | TODO |
| 1.8 | Rachel interview | Alex | TODO |
| 1.9 | Mei interview (with disarmament) | Alex | TODO |
| 1.10 | Aditya interview | Alex | TODO |
| 1.11 | Carmen relationship-only call | Alex | TODO (Wed next week) |
| 1.12 | Standing weekly Sarah locked, Friday 4:30 | Sarah | DONE |

## Week 2 — Eval first, foundation built

| # | Task | Owner | Critical path |
|---|---|---|---|
| 2.1 | James sign-off on data one-pager | James | YES |
| 2.2 | Mei MNPI watch list received | Mei | YES |
| 2.3 | David: 30 historical notes for seed eval | David | YES |
| 2.4 | Aditya + Kayla-eq scoping → Snowflake sandbox | Aditya | YES |
| 2.5 | Eval suite v1: 30 cases + 20 adversarial + per-sector slices | Alex | YES |
| 2.6 | Public-data augmentation: EDGAR + ECTSum + SubjECTive-QA | Alex | no |
| 2.7 | MNPI Scrubber wired with real watch list | Alex | YES |
| 2.8 | KPI Extractor wired with span-grounding | Alex | YES |
| 2.9 | Glossary v1 (finance-specific terms) | Alex | no |
| 2.10 | Note Drafter wired | Alex | YES |
| 2.11 | Friday standing with Sarah | Sarah | no |

## Week 3 — Production hardening, integration, first end-to-end

| # | Task | Owner | Critical path |
|---|---|---|---|
| 3.1 | Tone Supervisor wired (LLM-as-judge) | Alex | YES |
| 3.2 | Citation Verifier wired (deterministic) | Alex | YES |
| 3.3 | Compliance Critic wired with Mei's 3 rules | Alex + Mei-deputy | YES |
| 3.4 | Snowflake + Bloomberg/FactSet read-only ingestion live | Aditya + Kayla-eq | YES |
| 3.5 | First end-to-end run on dev data (one note, all 7 agents, full trace) | Alex | YES |
| 3.6 | Pass^k regression suite running, k=5 over 50+ cases | Alex | YES |
| 3.7 | Calibration: Brier score on tone-supervisor; reliability diagram on citation routing | Alex | no |
| 3.8 | State-aware (sector-aware) policy library version-controlled | Alex | no |
| 3.9 | **Rachel 20-draft review session — rollout gate** | Rachel | YES |
| 3.10 | **Carmen hostile review session** | Carmen | YES |
| 3.11 | Mei biweekly check-in | Mei + deputy | no |
| 3.12 | Friday standing with Sarah | Sarah | no |

## Week 4 — Production hardening + handoff

| # | Task | Owner | Critical path |
|---|---|---|---|
| 4.1 | Rollback runbook | Alex | YES |
| 4.2 | On-call doc with Tier 1/2/3 paging | Alex | YES |
| 4.3 | Observability dashboard (Splunk-equivalent) | Alex + Kayla-eq | YES |
| 4.4 | Audit-trace examiner-summary renderer | Alex | YES |
| 4.5 | Death-spiral monitor (rolling metrics + alerting) | Alex | no |
| 4.6 | Rachel sign-off (18/20 send-ready) | Rachel | YES |
| 4.7 | Mei sign-off on audit-trace standard | Mei | YES |
| 4.8 | Carmen sign-off on trader-side quality | Carmen | YES |
| 4.9 | Live wedge demo with Sarah, David, Rachel, Mei, Aditya, Carmen, James | Alex | YES |
| 4.10 | Handoff packet: runbook + eval docs + change-log | Alex | no |
| 4.11 | Field memo to OpenAI Research / Product on model behaviors that blocked us | Alex | no |
| 4.12 | Discovery memo refresh with real numbers from eval data | Alex | no |

## Workstream view

### WS1 — Eval suite
- 1.7 David interview → 2.3 30-case seed → 2.5 v1 suite + 30 adversarial → 2.6 public augmentation → 3.6 pass^k regression → 3.7 calibration → 4.4 audit-trace validation

### WS2 — Agent build
- 2.7 MNPI Scrubber → 2.8 KPI Extractor → 2.10 Drafter → 3.1 Tone Supervisor → 3.2 Citation Verifier → 3.3 Compliance Critic → 3.5 first e2e

### WS3 — Integration
- 1.10 Aditya interview → 2.4 sandbox commitment → 3.4 Bloomberg/FactSet ingestion → 4.3 observability dashboard

### WS4 — Compliance
- 1.9 Mei disarm → 2.2 watch list → 3.3 Compliance Critic + Mei's rules → 3.11 biweekly → 4.7 Mei sign-off

### WS5 — User trust
- 1.8 Rachel interview → 3.9 20-draft review → 4.6 Rachel sign-off

### WS6 — Trader-side acceptance
- 1.11 Carmen relationship-only → 3.10 hostile review → 4.8 Carmen sign-off

### WS7 — Buyer alignment
- 1.1 Sarah kickoff → 1.12 standing weekly → 2.11 / 3.12 weekly check-ins → 4.9 live demo

## Risks visible from the plan

| Risk | Mitigation built into the plan |
|---|---|
| James sign-off slips → MNPI Scrubber blocks | Tight one-pager (half page); Mei aligned in advance |
| David's 30-note pull late | Public EDGAR data as fallback for eval suite |
| Aditya bandwidth (one engineer) | Pair-program approach; explicit Kayla-equivalent named in week 2 scoping |
| Rachel won't sign off | Week 3 review leaves week 4 for redesign; if no path, narrow wedge to TMT sector only |
| Carmen still hostile after week 3 review | Sarah escalation; trader-side acceptance is week-4 sign-off, not pre-existing |
| Tone-shift LLM-as-judge variance under pass^k | Calibrate weekly against SubjECTive-QA; Rachel-hand-graded held-out set |
| OpenAI BAA delay | Anthropic-only in v1; swap-ready architecture |

## What you'll learn at each phase

| Phase | What you actually learn |
|---|---|
| Week 1 discovery | The problem behind the asked problem (it's analyst retention + alpha capture, not just hours saved) |
| Week 2 eval | Where citation grounding breaks on real data (likely on subtle paraphrases of guidance) |
| Week 3 prototype | Where Mei's compliance bar differs from your synthesized version (likely stricter on specific phrases) |
| Week 4 hardening | What Carmen finds in week-3 hostile review (likely tone-shift detection accuracy) |

The build plan is the artifact you ship to Sarah. The lessons-learned memo is the artifact you ship to OpenAI Research / Product.

## What ships post-week-4

End-of-engagement deliverables:
1. Working wedge in Helix's Snowflake-Python environment
2. Rachel + Mei + Carmen signoffs documented
3. Runbook + on-call doc + observability dashboard
4. Handoff to David + Aditya for ongoing operations
5. Field memo to OpenAI Research / Product on what blocked us + what would help
6. Recommendation for v2 scope (likely: Tone-Shift Detector enhancement, multi-quarter context retrieval, expansion to mid-cap names beyond covered universe)
