# Tom Reilly — Quality / Audit Lead — Friday 10:00am ET, in-person (45 min)

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Constructed dialogue; methodology authentic.

## Setup

Friday 10:00 AM ET. Tom in his office, two banker's boxes of case files visible behind him, dual monitors. Quieter, more structured than Priya. Methodical. He has prepared notes for this meeting — a sign he takes the work seriously.

## Selected exchanges

**Alex** *(opening)*: "Tom, thanks for the time. I know Sienna will be on the eval set with us so this is mostly about you walking me through the audit standard and the two findings in detail. Sound OK?"

**Tom**: "That's the right scope. Where do you want to start?"

**Alex**: "Findings first. Walk me through finding 1 — the NJ one. Customer experience, what the regulator actually objected to, and where in the workflow it could have been caught."

**Tom** *(15-min walk)*: "OK. Claim filed via web at 2:14pm on a Friday. Customer was a fleet manager for a parts distributor. BPO sent the acknowledgment Tuesday at 11:08am — 96 hours delay against the NJ 24-hour SLA. The acknowledgment also gave a 30-day resolution timeline that wasn't policy-aligned — the policy was on a 14-day track for that LOB. Examiner cited 'delayed and misleading communication' on both counts.

Root cause: the claim came in on the Friday batch but missed the 1pm BPO triage cycle by 14 minutes. So it rolled into Monday's triage queue. By Monday they had a backlog from the weekend, so it actually got opened Tuesday morning. The misleading 30-day timeline was a copy-paste from a template that hadn't been updated when the LOB-specific policy was changed in Q2 2024. We'd asked operations to refresh templates after that policy change. They did most of them; this LOB got missed.

Could have been caught at: (1) the triage cycle itself if it ran hourly instead of every 4 hours; (2) the template-refresh ownership if anyone owned it end-to-end; (3) the comm itself if there were a real-time check against current policy."

**Alex**: "Two systemic patterns I'm hearing. Triage delays compounding into SLA violations. Stale templates carrying old policy timelines. Are those representative of what an examiner usually objects to, or specific to those two findings?"

**Tom**: "Both. NAIC market-conduct exam findings nationally cluster around three things: timeliness, accuracy of stated terms, misleading communications. The two we got hit Pattern 1 and Pattern 2 simultaneously. If I had to predict the next one, I'd say Pattern 2 again — we still have stale templates in 4 LOBs, I've flagged it three times to operations, no one owns the template refresh end-to-end."

**Alex**: "Useful. The template-refresh ownership gap is something the agent could close — every comm goes through a deterministic policy lookup, so stale templates can't make it into outbound. Now the audit-trace question. If a market-conduct examiner pulls a closed file that had AI-assisted handling, what does she look for?"

**Tom**: "Inputs the agent saw. The rule it applied. The output. Whether a human reviewed and what they did. Time stamps on every step. And — this is the one most people miss — versioning. If the model behind the agent changed three times during the file's life, the examiner wants to know which version made which decision. Plus the trace has to be readable by a human auditor without specialized tools. Don't give me JSON; give me a one-page summary with drilldown links."

**Alex**: "Got it. Immutable agent snapshots with version IDs visible in the trace, human-readable summary with drilldown. Now the eval set. What would the best 50 cases look like?"

**Tom**: "30 well-handled, where the comms were textbook. 15 finding-pattern, where something went wrong — 8 from the actual two findings + 7 near-misses we caught internally. 5 hardest-edge: complex multi-party, comparative negligence, edge-of-policy coverage. Sienna can pull these by EOD next week. She'll need 2 days because she's also closing Q1 audit reports."

**Alex**: "Cadence with Sienna once we have the eval set?"

**Tom**: "Weekly 30-min reviewing what your evals are catching and what they're missing. Sienna's good at pattern-spotting. She'll tell you when the eval set has gone stale."

**Alex**: "Last one — what would make you, personally, sign off on a production rollout?"

**Tom** *(no hesitation)*: "Three things. One: every closed file produces a human-readable audit trace I can hand to an examiner without translation. Two: pass rate on the 50-case eval set above 85% with zero state-DOI-violation patterns. Three: a death-spiral monitor that pings me if any of three things drift — accuracy, timeliness, or escalation rate — by more than 10% over a rolling 7-day window."

**Alex**: "Done. Those become the week-4 sign-off criteria. Wedge proposal lands Friday and you'll be copied. Specifics on Sienna's cadence will be in the proposal."

*(Wraps at 41 minutes.)*

## Post-interview captures

### The audit-trace standard for AI-touched files
- Inputs the agent saw
- Rule applied
- Output
- Whether human reviewed; if yes, what they did
- Timestamps on every step
- **Model version IDs** for every decision (immutable agent snapshots)
- Human-readable summary with drilldown — not JSON

### The eval set composition (50 cases via Sienna by EOD next week)
- 30 well-handled (textbook comms)
- 15 finding-pattern (8 from the actual findings + 7 near-misses)
- 5 hardest-edge (multi-party, comparative negligence, edge coverage)

### Tom's three sign-off criteria for production rollout
1. Human-readable audit trace for every closed file (no translation needed)
2. >85% pass rate on 50-case eval set + zero state-DOI-violation patterns
3. Death-spiral monitor: alerts on >10% drift over 7-day rolling window for accuracy / timeliness / escalation rate

### Glossary updates
- **NAIC**: National Association of Insurance Commissioners
- **Market-conduct exam**: NAIC-led periodic exam of an insurer's claim-handling practices
- **Stale template**: outbound communication template not updated after policy change
- **Death-spiral monitor**: production-monitoring pattern alerting on cross-metric drift

### Stakeholder map updates
- Tom: ALLY (engaged, prepared notes for the meeting)
- Sienna: TECHNICAL PARTNER (named, weekly 30-min cadence)

### Working hypothesis updates
- The audit-trace standard now drives the agent design: every step traced, model version visible, human-readable
- Tom's 3 sign-off criteria become the explicit week-4 production gate
- The template-refresh ownership gap (Pattern 2) is something the agent inherently solves — every comm goes through a deterministic policy lookup, so stale templates can't sneak through

### Open questions
- SharePoint location of policy templates? (Marcus interview will likely answer)
- Sienna's actual capacity beyond the 50-case set — can she sustain weekly review through week 4?

## Recap email sent (10:55am)

Subject: `[Calder] Tom recap — audit-trace standard + eval set + sign-off criteria`

> Tom — thanks for the time. Three things going into the wedge proposal:
>
> **Audit-trace standard**: inputs, rule, output, human reviewer, timestamps, model version IDs, human-readable summary with drilldown. This drives the agent's logging design.
>
> **50-case eval set**: 30 well-handled / 15 finding-pattern / 5 hardest-edge. Sienna delivers EOD next week. Weekly 30-min review starting then.
>
> **Sign-off criteria for rollout**: (1) human-readable audit trace for every closed file, (2) >85% on the 50-case eval + zero state-DOI-violation patterns, (3) death-spiral monitor on accuracy / timeliness / escalation drift.
>
> Wedge proposal lands Friday. Copying you.
>
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Discovery rigor | 5 | Didn't ask "help me design"; let him own the audit standard |
| Eval-driven discipline | 5 | Locked the 50-case composition + the sign-off criteria explicitly |
| Productionization discipline | 5 | Immutable snapshots + version IDs in trace = senior-grade requirement |
| Calibrated engineering | 4 | Death-spiral monitor will need real implementation, not a slide |
| Codification | 4 | Recap email captures 3 sign-off criteria — engagement contract for week 4 |

**Keep**: didn't solutionize; let Tom own the audit standard articulation.

**Fix**: should have asked for the SharePoint location of templates directly; let it slide assuming Marcus would surface it.
