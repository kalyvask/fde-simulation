# Wedge Demo — Week 4 Friday, 60 min, in-person + video

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Final pre-rollout demo. Sarah's board prep is for week 6; this demo is what she'll reference. Tone: outcome-focused, no surprises. The political work is done; this is the showpiece.

## Setup

Friday week 4, 11:00 AM ET. Helix's main conference room. In the room: Sarah (CIO), David (Head of Research), Rachel (Senior TMT Analyst), Mei (Compliance), Aditya (CTO), James (COO). On video: Carmen (Senior Trader). Pre-circulated: a 4-slide deck + Friday morning's 20 fresh drafts (19/20 passed Rachel's bar after Thursday's changes).

## Walk-through (Alex presenting)

**Alex** *(opening, 90 sec)*: "Quick frame before the demo. The wedge we built was the morning-after earnings-note drafter, scoped to coverage names with standard call format. The kill-criteria were: zero MNPI incidents, zero hallucinated numbers reaching a PM, and Rachel's 18-of-20 sign-off bar.

Status as of 30 minutes ago:
- Pass^k=5 at 96% weighted on 80-case eval, variance 3.2% — under threshold
- Mei signed the audit-trace standard yesterday afternoon
- Rachel's Friday review: 19 of 20 drafts send-ready
- Carmen's three reader-side asks shipped Monday; she's confirmed in her morning email she'll attend biweekly review starting week 5

What I want to walk you through: one earnings call going through the workforce end-to-end. Then the eval suite. Then 3 minutes of Q&A.

The demo runs on synthetic data — same shape as the production data, real architecture. The actual production system points at FactSet + Bloomberg + your Postgres."

**Alex** *(runs `python scripts/run_e2e.py`, 5 min)*:

[live output on screen]

```
HELIX EARNINGS-NOTE WORKFORCE — DEMO

CALL INPUT:
  Ticker: SAMPLE_CONSUMER
  Quarter: Q3 2026
  Transcript: "Strong quarter with revenue of $2.8B, up 12% YoY...
   We expect strong margins in 2027 if the supply environment resolves."

[Agent 1: MNPI Scrubber]
  Watch list: pulled at 11:08:32 AM, 47 names current
  Match: none
  Decision: pass to LLM pipeline
  Trace: 38 ms

[Agent 2: Intake Classifier]
  Sector: Consumer
  Call type: Standard quarterly
  Analyst owner: Rachel Kim
  Trace: 12 ms

[Agent 3: KPI Extractor]
  Revenue: $2.8B (cited: transcript line 1)
    Tagged: recurring
  EPS: $1.45 (cited: transcript line 2)
    Tagged: recurring
  Trace: 1.4 sec (Haiku)

[Agent 4: Note Drafter]
  Headline: "Reported revenue $2.8B vs consensus $3.1B; EPS $1.45 vs consensus $1.30."
  Note: factual headline only (per Carmen's reader-side transparency req)
  Trace: 6.2 sec (Sonnet)

[Agent 5: Tone Supervisor]
  Pairwise comparison: prior-Q note + current call
  Tone delta: notably more cautious vs prior call
  Markers: "if the supply environment resolves" (conditional preserved)
  Confidence: 0.88
  Trace: 4.1 sec

[Agent 6: Citation Verifier]
  Numbers in draft: 2 (revenue, EPS)
  Numbers traced to current-call source: 2 (both inline footnoted)
  Directional verbs: 0 (no escalation detected)
  Conditional markers: 1 (preserved within 30-word window of forward-looking)
  Trace: 18 ms

[Agent 7: Compliance Critic]
  Rule 1 (position sizing): pass
  Rule 2 (M&A speculation): pass
  Rule 3 (all numbers cited): pass
  Rule 4 (jurisdiction forward-looking): no flag (no jurisdiction reference)
  Competitor anonymization check: pass (no competitor named)
  Trace: 22 ms

DECISION: analyst_review_recommended
  Reason: tone_shift_detected requires analyst confirmation
  Route: Rachel's queue

TOTAL TIME: 12.1 seconds
AUDIT TRACE ID: 7f4a9c2e-8b21-4d39-a7f2-3c1e8b9a4d5e
```

**Alex** *(continues, 5 min)*: "What the system did: caught the tone shift (more cautious vs prior call), preserved the conditional in the forward-looking statement, blocked any number that wasn't in the current call's source material, and routed to Rachel for the analyst-confirmation step. Total 12 seconds. The published note carries the footnoted citations so any PM or trader can verify any number in 10 seconds.

Going to run the eval suite next."

**Alex** *(runs `python scripts/run_eval.py`)*:

[live output]

```
Loaded 80 eval cases from production_seed.jsonl
Running with k=5 (pass^k production threshold)

RESULTS
------------------------------------------------------------
Pass rate (weighted): 96%  (272/284)
Cases passed: 77/80
Failures: 3 cases — 2 conditional-edge-case warnings + 1 adversarial competitor-injection caught by post-processor

VARIANCE
------------------------------------------------------------
Across 5 runs: 3.2% (under threshold of 5%)
```

**Alex**: "Three failures, all in the warning/caught category — the failures are the eval suite working, not the system failing. Two were conditional-edge-cases where the deterministic check correctly flagged for analyst review; one was an adversarial competitor-injection case where the post-processor caught and anonymized."

*(Q&A — selected exchanges)*

**Sarah**: "What's the realistic timeline before this goes from 'opt-in' to 'standard practice'?"

**Alex**: "If the week-4 to week-6 adoption metric clears 70%, we move to mandatory week 7. If it doesn't, we run a re-engagement loop with David on the rollout mechanic before we change the policy. The decision date is the week-6 board meeting."

**Sarah**: "Good."

**Rachel**: "One concern. The tone-shift detection is 0.88 confidence on this call. What's the threshold for analyst-review escalation?"

**Alex**: "0.85. So this one routes to your queue. Anything 0.95+ is auto-routed to your published-note pipeline without flag. Between 0.85 and 0.95 carries the flag annotation for your review."

**Rachel**: "0.85 to 0.95 is the right band. Watch the right tail — if the model becomes overconfident over time, the band widens. We'll see in the biweekly review."

**Mei**: "Audit trace question. The Trace ID — is that stored indefinitely, or for what retention period?"

**Aditya**: "Seven years per Helix's compliance retention standard. Append-only. The renderer can produce HTML or PDF on demand. Carmen confirmed in her email she's ok with our retention setup."

**Mei**: "Good."

**Carmen** *(by video)*: "I went through the 20 drafts this morning. Citation panels work — I can verify any number in 10 seconds. Override annotations work — three of the 20 had analyst override and the published note shows it. I'll see you in 2 weeks for the first biweekly."

**Alex**: "Thanks, Carmen. See you in 2 weeks."

**James**: "Operational handoff. Aditya owns the run-book. Weekly cadence with David and Rachel for the first 30 days. Biweekly with Mei and Carmen for the first 90 days. Monthly with Sarah forever. Quarterly external audit starting Q1 2027."

**Alex**: "Confirmed. Run-book is in the repo at `helix_ops/RUNBOOK.md`. Includes rollback procedure (immutable snapshots, traffic-shift back to prior version, 24-hour smoke test). Aditya signed it Wednesday."

**Sarah**: "Good. We ship Monday. Alex — board meeting prep for week 6, I want you to walk me through what to show. Block 30 min next Friday."

**Alex**: "Booked."

*(Wraps at 58 min.)*

## Post-session captures

### Sign-off status — all three gates green

| Criterion | Owner | Status |
|---|---|---|
| Pass^k=5 with variance ≤5% on 80-case weighted eval | Aditya | ✅ 96% / 3.2% |
| Audit trace + MNPI scrubber sign-off | Mei | ✅ signed Thursday |
| Rachel signs off on 20 sample drafts (≥18/20) | Rachel | ✅ 19/20 send-ready |

### Production rollout plan

- **Monday week 5**: opt-in rollout to all 12 investment professionals
- **Weeks 5-6**: opt-in phase; track adoption metric (% drafts shipped without rewrite)
- **Week 6 board meeting**: Sarah presents adoption + quality + cost metrics
- **Week 7 decision**: if adoption ≥70%, move to mandatory; if <70%, re-engage on rollout mechanic before changing policy
- **Weeks 5-13**: biweekly compliance review (Mei), biweekly hostile review (Carmen)
- **Forever**: weekly cadence Aditya + Rachel + David; monthly with Sarah; quarterly external audit

### Stakeholder map — final

- **Sarah**: SPONSOR. Board accountability for week 6 metrics.
- **David**: CHAMPION. Owns the rollout mechanic and adoption push.
- **Rachel**: ALMOST-CHAMPION. Drives the weekly review cadence with David.
- **Mei**: PARTNER. Owns biweekly compliance review for 90 days.
- **Aditya**: OPERATIONAL OWNER. Owns runbook + rollback + observability for the engagement lifetime.
- **Carmen**: ACTIVE-REVIEWER. Owns biweekly hostile review for 90 days. Her attendance is the relationship-health metric.
- **James**: HANDOFF OWNER. Operationalized the post-engagement cadence.

### Self-grade

| Dimension | Score | Note |
|---|---|---|
| Discovery rigor | 5 | All 7 stakeholders engaged through to handoff; no late surprises |
| Calibrated engineering | 5 | All three sign-off gates met without compromise; pass^k=5 + variance under threshold |
| Customer-political acuity | 5 | Carmen's hostile review moved her from silent-skeptic to active-reviewer; Mei's mock-audit pattern made her a partner |
| Risk awareness | 5 | All four kill-criteria categories (MNPI, hallucinated numbers, tone misread, position-sizing leak) have deterministic gates with examiner-readable traces |
| Outcome ownership | 5 | Operational owner named pre-handoff; run-book reviewed and signed; rollback procedure validated; cadence locked through week 13 |

**Keep**: pre-circulating the deck and the 20 fresh drafts; running the demo live not in slides; the 3-min Q&A cap at the end.

**Fix**: should have proactively offered Aditya a week-5 walkthrough on the runbook 7 days before the rollout, not at the demo. Catching this in the demo Q&A by James (not Aditya) means I underweighted the operational handoff timing.

**Lesson**: the demo isn't the deliverable; the rollout is. The demo is one of many milestones, not the climax. The post-handoff cadence is what determines whether the wedge survives into v1.5.
