# Wedge Build Plan — Calder FNOL AI Workforce v1

> Companion to `wedge_proposal.md`. Tactical task roadmap from discovery through Friday-week-4 demo.

## The wedge (one-line)

Auto-acknowledgment + first-status-update agent for first-party physical damage FNOL claims, web + agent-portal channels first, with full audit trace. 80% straight-through. FNOL → first-touch <30min on the slice.

## How to use this plan

- **Critical path** is marked. Slip on a critical-path task = slip the demo.
- Each task has an **owner** (Alex unless noted) and a **dependency**.
- Re-baseline weekly at the standing Friday 4:15 with Maria.

---

## Critical path (the spine)

```
Rachel sign-off → Data pull → Eval suite → Agent prototype → Janet review → Ship
                                ↑
                                Marcus policy library → Compliance critic
                                ↑
                                Anil queue + sandbox → Integration tests
```

Anything on the critical path slipping by >2 days triggers a re-scope conversation with Maria.

---

## Week 1 — Discovery + alignment (in progress)

| # | Task | Owner | Depends on | Status |
|---|---|---|---|---|
| 1.1 | Maria kickoff | Alex | — | DONE |
| 1.2 | Recap email to Maria | Alex | 1.1 | DONE |
| 1.3 | Discovery memo draft | Alex | 1.4-1.10 | DONE (worked example; refresh after real interviews) |
| 1.4 | Wedge proposal draft | Alex | 1.4-1.10 | DONE (worked example) |
| 1.5 | Rachel data one-pager | Alex | 1.1 | DONE — submit Friday |
| 1.6 | Data-pull spec to Greg | Alex | 1.5 | DONE — send EOD tomorrow |
| 1.7 | Adjuster intro email draft for Maria's redline | Alex | 1.1 | DUE Friday this week |
| 1.8 | Priya interview | Alex | 1.1 | TODO |
| 1.9 | 4 adjuster interviews (Janet / Mark / Sarah / Hassan) | Alex | 1.8 | TODO |
| 1.10 | Tom interview + 50-case eval-set request | Alex | 1.1 | TODO |
| 1.11 | Marcus interview (with disarmament) | Alex | 1.1 | TODO |
| 1.12 | Anil interview + queue commitment | Alex | 1.1 | TODO |
| 1.13 | Standing 15-min Maria locked, Fri 4:15 | Maria | 1.1 | DONE |

**Week 1 exit criteria**: 6 stakeholders interviewed; recap emails sent; eval-set request with Sienna; data pull on the way; Rachel signed; sandbox path known.

---

## Week 2 — Eval first, foundation built

| # | Task | Owner | Depends on | Critical path |
|---|---|---|---|---|
| 2.1 | Receive Rachel sign-off | Maria | 1.5 | YES |
| 2.2 | Receive 500-claim data pull | Greg's data team | 1.6, 2.1 | YES |
| 2.3 | Receive Sienna's 50-case eval set | Tom + Sienna | 1.10 | YES |
| 2.4 | Anil + Kayla scoping session → sandbox commitment | Anil | 1.12 | YES |
| 2.5 | Sandbox access live | Anil + Kayla | 2.4 | YES |
| 2.6 | Eval suite v1: 50 cases + 30 adversarial + state slices | Alex + Sienna | 2.3 | YES |
| 2.7 | Public-data augmentation: NHTSA CRSS narratives loaded as extraction stress tests | Alex | — | no |
| 2.8 | Marcus policy library extracted from SharePoint, encoded as deterministic rules | Alex + Devorah | 1.11 | YES |
| 2.9 | Glossary v1 finalized (every term from interviews) | Alex | 1.8-1.12 | no |
| 2.10 | Base agent skeleton: Intake + Coverage validator + Drafter (Sonnet, no tools yet) | Alex | 2.5, 2.8 | YES |
| 2.11 | Wedge proposal sent to Maria + Greg | Alex | discovery refresh | YES |
| 2.12 | Friday standing weekly with Maria | Maria | 1.13 | no |

**Week 2 exit criteria**: eval suite running; agent skeleton live in sandbox; policy library encoded; wedge signed off by Maria; Janet's 20-draft review scheduled.

---

## Week 3 — Hybrid architecture, integration, first end-to-end

| # | Task | Owner | Depends on | Critical path |
|---|---|---|---|---|
| 3.1 | Tone/empathy supervisor agent wired | Alex | 2.10 | YES |
| 3.2 | Compliance critic agent wired (rules engine + retrieval over policy library) | Alex + Devorah | 2.8 | YES |
| 3.3 | Send agent: Twilio SMS + email gateway integration | Alex + Kayla | 2.5 | YES |
| 3.4 | Audit logger → Splunk integration | Alex + Kayla | 2.5 | no |
| 3.5 | First end-to-end run on dev data (one claim, all agents, full trace) | Alex | 3.1-3.4 | YES |
| 3.6 | Pass^k regression suite running, k=5 over 80 cases | Alex | 2.6 | YES |
| 3.7 | Adjuster review queue UI (basic — list view + one-click escalate) | Alex | 2.10 | no |
| 3.8 | Calibration: Brier score on confidence; reliability diagram on routing | Alex | 3.5, 3.6 | no |
| 3.9 | State-aware policy library version-controlled in repo | Alex | 2.8 | no |
| 3.10 | Janet 20-draft review session | Janet (Priya schedules) | 3.5 | YES |
| 3.11 | Marcus biweekly check-in | Marcus + Devorah | 1.11 | no |
| 3.12 | BPO comms volume + delay data analysis | Alex | 1.6 follow-on | no |
| 3.13 | Friday standing weekly with Maria | Maria | — | no |

**Week 3 exit criteria**: agent workforce running end-to-end on dev data; regression suite green; Janet's feedback incorporated; calibration baseline established.

---

## Week 4 — Production hardening + handoff

| # | Task | Owner | Depends on | Critical path |
|---|---|---|---|---|
| 4.1 | Rollback runbook | Alex | 3.5 | YES |
| 4.2 | On-call doc | Alex | 4.1 | YES |
| 4.3 | Observability dashboard live (volume, latency, accuracy, escalation rate, drift) | Alex + Kayla | 3.4 | YES |
| 4.4 | Audit-trace artifact: examiner-readable trace generated for any sample claim, validated by Tom | Alex + Sienna | 3.5 | YES |
| 4.5 | Death-spiral monitor: auto-alert on accuracy regression / latency drift / escalation spike | Alex | 4.3 | no |
| 4.6 | Janet sign-off on the comms quality | Janet | 3.10 | YES |
| 4.7 | Marcus sign-off on the audit-trace standard | Marcus | 4.4 | YES |
| 4.8 | Live wedge demo with Maria, Greg, Priya, Marcus, Anil | Alex | 4.6, 4.7 | YES |
| 4.9 | Handoff packet: runbook + eval docs + change-log + COE org chart for ongoing | Alex | 4.8 | no |
| 4.10 | Field memo to Anthropic Research/Product on model behaviors that blocked us | Alex | 3.5-3.10 learnings | no |
| 4.11 | Discovery memo refresh with real numbers from eval data | Alex | 3.6, 3.8 | no |
| 4.12 | Wedge expansion proposal v2 (phone channel? coverage decisions? BI track-record?) | Alex | 4.8 | no |

**Week 4 exit criteria**: live demo passed; signoffs from Janet + Marcus + Maria; handoff packet delivered; ongoing-engagement decision made.

---

## Workstream view (alternative cut)

### Workstream 1 — Eval suite (the intellectual content)
- 1.10 Tom interview + eval-set request
- 2.3 Sienna 50 cases received
- 2.6 Eval v1 (50 + 30 adversarial + state slices)
- 2.7 Public-data augmentation (NHTSA)
- 3.6 Pass^k regression
- 3.8 Calibration metrics
- 4.4 Audit-trace artifact validated

### Workstream 2 — Agent build
- 2.10 Skeleton (Intake + Coverage + Drafter)
- 3.1 Tone supervisor
- 3.2 Compliance critic
- 3.3 Send agent (Twilio + email)
- 3.5 First end-to-end
- 3.7 Adjuster review queue UI

### Workstream 3 — Integration
- 1.12 Anil interview
- 2.4 Scoping session
- 2.5 Sandbox live
- 3.3 Send-channel integration
- 3.4 Splunk logger
- 4.3 Observability dashboard

### Workstream 4 — Compliance
- 1.11 Marcus disarm
- 2.8 Policy library encoded
- 3.2 Compliance critic
- 3.9 State-aware library version-controlled
- 3.11 Marcus biweekly
- 4.7 Marcus sign-off

### Workstream 5 — Adjuster trust
- 1.7 Intro email
- 1.9 4 adjuster interviews
- 3.10 Janet 20-draft review
- 4.6 Janet sign-off

### Workstream 6 — Buyer alignment
- 1.1 Kickoff
- 1.2 Recap email
- 1.13 Standing weekly
- 2.11 Wedge proposal sent
- 2.12 / 3.13 Weekly checkpoints
- 4.8 Live demo

---

## Risks visible from the plan

| Risk | Mitigation built into the plan |
|---|---|
| Rachel sign-off slips → data pull slips | Rachel one-pager kept tight (half-page); offer biweekly cadence as carrot |
| Eval set late (Tom/Sienna capacity) | Public-data fallback (NHTSA + Kaggle) keeps eval work moving |
| Sandbox not refreshed in 6 months | Use real anonymized pull data for prototyping; sandbox for integration only |
| Janet won't sign off | Her review in week 3 leaves week 4 to incorporate; if she still won't sign, escalate to Priya, then Maria |
| Marcus changes the bar mid-build | Biweekly cadence catches it; state-aware library is version-controlled |
| Phone channel pressure to expand v1 scope | "What this wedge does NOT do" section in proposal is the explicit boundary |

## What you'll learn at each phase

| Phase | What you actually learn |
|---|---|
| Week 1 discovery | The problem behind the asked problem (it was comms-layer, not auto-pay) |
| Week 2 eval | Where the model fails on real data (you'll be surprised; that's the point) |
| Week 3 prototype | Where the integration friction actually lives (almost always different from the diagram) |
| Week 4 hardening | What "production ready" means in this org's specific risk tolerance |

The build plan is the artifact you ship to Maria. The lessons-learned memo is the artifact you ship to Anthropic.
