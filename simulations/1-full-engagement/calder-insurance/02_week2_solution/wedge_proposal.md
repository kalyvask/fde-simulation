# Wedge Proposal — Calder FNOL AI Workforce v1

**Companion to**: `discovery_memo.md`
**From**: FDE Lead
**For**: Maria Vasquez (CCO), Greg Hadley (SVP Claims Ops), Priya Shah, Marcus Hill, Anil Gupta
**Decision needed**: sign-off to build by Friday-of-week-3

## The wedge in one paragraph

Build an AI workforce that auto-acknowledges incoming FNOL claims and drafts first-status-updates for claimants, scoped to first-party physical damage on web and agent-portal channels. The agent runs from intake to first-touch only — it does **not** touch coverage decisions, does **not** touch bodily-injury claims, and does **not** write back to Guidewire in v1. Every output ships with a decision-trace artifact designed for NAIC market-conduct examiner review. Target: 80% straight-through processing with an adjuster review queue for the 20%, FNOL → first-touch median <30min on the slice (today: 4.2h), zero state-DOI-violation patterns on the eval set.

## Why this slice (revising the original auto-pay-eligible hypothesis)

The original hypothesis (auto-pay triage) was builder-shaped: clean data, easy engineering. The discovery surfaced that the actual customer pain — the two market-conduct findings, the leakage, the BPO failure pattern — sits at the **comms layer**, not the coverage layer. The wedge that addresses customer pain and engineering tractability simultaneously is comms acknowledgment + status update.

Five reasons:

1. **Direct hit on Maria's regulatory kill-criteria.** Both Q4 findings were comms-layer. This wedge's central deliverable is auditable, accurate comms.
2. **No coverage decision** = lower regulatory exposure (no human-licensed-adjuster floor triggered in v1) and faster to ship.
3. **Web + agent portal channels = clean structured input** = engineering tractable. Phone-channel transcripts in v2 once trust is earned.
4. **High volume.** 37% of FNOL = 220 claims/day = meaningful LAE impact possible.
5. **Replaces Priya's side spreadsheet.** The first weekly demo is the spreadsheet's catch rate replicated; the second is improvement on it. Visible internal credibility.

## The agent workforce

7 specialized agents + a supervisor pattern. Each runs a single concern.

| Agent | Job | Tools | Model tier |
|---|---|---|---|
| Intake | Parse FNOL form, extract structured fields, classify channel + LOB | Form parsers, classifier | Haiku |
| Coverage validator | Read policy from Guidewire (read-only API), confirm coverage exists | Guidewire API | Haiku |
| Acknowledgment drafter | Draft claimant comm in claimant's language using extracted facts | Anthropic Sonnet | Sonnet |
| Tone / empathy supervisor | Check draft for empathy, factual accuracy, no overpromise | LLM-as-judge | Sonnet |
| Compliance critic | Apply Marcus's policy library (deterministic rules); state-by-state SLA windows | Rules engine + retrieval | Haiku + retrieval |
| Send agent | Route to channel (Twilio SMS / email gateway), confirm delivery | Twilio, email | n/a |
| Audit logger | Log every step (input, model version, retrieved context, output, examiner-readable trace) | Splunk integration | n/a |
| **Adjuster review queue** | Routes the 20% (low confidence, BI-adjacent, edge-case) to human with one-click escalation | Internal app | n/a |

## What "working" means (measurable)

| Metric | Target | Baseline |
|---|---|---|
| FNOL → first-touch median (web + agent portal) | <30min | 4.2h |
| % straight-through processing | 80% | n/a |
| Acknowledgment accuracy on policy fields | 100% | (every cited number must be traceable) |
| State-DOI-violation patterns on eval set | 0 | (Tom's eval set + 30-case adversarial) |
| Adjuster trust score on comms quality (sample 50) | >4/5 | (Janet + 3 reviewers) |
| Customer first-touch NPS uplift on slice | +10 pts | 31 |
| Audit-trace completeness | 100% | (every decision: input, rule, output, reviewer) |
| Latency p95 (acknowledgment send) | <60s | n/a |

## Eval design (the intellectual content)

- **Seed set**: 50 cases from Tom (30 well-handled / 15 finding-pattern / 5 hardest-edge)
- **Public augmentation**: NHTSA CRSS narratives for narrative-extraction stress tests; Kaggle Auto Insurance Claims for routing/fraud-flag baseline; FUNSD for any document-OCR needs
- **Adversarial set**: 30 hand-built gotchas — wrong policy fields, edge BI cases, multi-vehicle, partial-fault, unusual phrasings
- **Regression**: every fixed bug becomes a conversation-test (the agent development lifecycle pattern). Pass^k consistency over k=5 runs.
- **Calibration**: Brier score on confidence; reliability diagram on the routing decision (auto-send vs adjuster review queue)
- **State-aware**: separate eval slice per state where Marcus's policy library shows variance

## 4-week plan

| Week | Deliverable | Owners |
|---|---|---|
| **1** (in progress) | Discovery memo + this proposal + Rachel one-pager | Alex |
| **2** | Eval suite v1 (50 cases + adversarial 30 + state slices); sandbox access live | Alex + Sienna (Tom's team) |
| **3** | Prototype agent workforce on sandbox; Janet 20-draft review; Marcus policy library encoded | Alex + Kayla (Anil's team) + Devorah (Marcus) |
| **4** | Production hardening: rollback runbook, observability dashboard, audit-trace verification, on-call doc; Janet sign-off; field memo to Anthropic | Alex + customer team |

End-of-week-4: live wedge demo + handoff packet.

## What we need from Calder

| Ask | Owner | Date |
|---|---|---|
| Rachel sign-off on data one-pager | Maria → Rachel | Friday this week |
| 500-claim data pull | Greg + data team | EOD Tuesday next week |
| Marcus policy library SharePoint access | Marcus | EOD Friday this week |
| Anil + Kayla integration scoping session | Anil | Wednesday next week |
| Sandbox access (Guidewire dev tenant) | Anil + Kayla | Wednesday next week |
| Sienna eval-set delivery (50 cases) | Tom → Sienna | end of next week |
| Janet 20-draft review | Priya → Janet | Week 3 |
| BPO comms volume + delay data, last 90d | Greg + Kevin | Wednesday next week |

## Risks + mitigations

| Risk | Mitigation |
|---|---|
| Hallucinated claim detail in claimant comms | Deterministic field extraction; LLM synthesizes narrative only; tone supervisor; compliance critic |
| Wrong timeline given to claimant | Deterministic timeline rule keyed on state + LOB, not LLM |
| State-by-state regulatory variance | State-aware policy library encoded as rules; rollout from loose to strict states |
| RPA scar-tissue political reaction (Anil) | Lead every demo with the audit trace; differentiate explicitly from RPA |
| BPO political reaction (Kevin) | Position as augmenting BPO; BPO retains phone overflow + the 20% adjuster review |
| Janet adoption | Her week-3 sample-draft review gates rollout; sign-off as internal milestone |
| Adjuster review queue overload | Calibrated routing; sized to current adjuster capacity; review-queue analytics from day 1 |
| Sandbox refresh staleness (6mo old) | Use real anonymized data from Greg's pull; sandbox is for integration testing only |

## What this wedge does NOT do (explicitly out of v1)

- Does not make coverage decisions
- Does not handle bodily-injury claims
- Does not write back to Guidewire (drafts only; adjuster or workflow commits)
- Does not handle phone channel (web + agent portal first)
- Does not handle non-English claimant comms (English-first; multi-language post-launch)
- Does not replace BPO entirely (BPO retains phone overflow + the 20% routing)

## Decision request

Sign-off to build the v1 wedge as scoped, with the 4-week plan and the asks above. By end of week 3 we will have eval data; we can renegotiate scope or extend if signal warrants.

— Alex
