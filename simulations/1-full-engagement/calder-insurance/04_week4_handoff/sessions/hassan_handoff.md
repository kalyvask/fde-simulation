# Hassan Handoff — Week 4 Thursday, 45 min

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Constructed dialogue showing the operational handoff to the named owner.

## Setup

Thursday week 4, 11:00 AM ET. Hassan's desk in the FNOL ops bullpen. Kayla (Anil's senior integration engineer) is on Zoom. Alex has flown in from California. Hassan retired his side spreadsheet two days ago; this conversation is the "you own it now" moment.

## Selected exchanges

**Alex** *(opening)*: "Hassan, I've been working on this for four weeks. You've been working on the workflow for seven years. From Monday, the system is yours. Today I want to walk you through the runbook, the on-call doc, and the things that are going to break that I haven't anticipated. Cool?"

**Hassan**: "Cool."

**Alex**: "Three sections. The runbook — what to do for the 5 most likely incidents. The on-call doc — when you page Kayla vs. when you page me vs. when you handle. The 'things I don't know yet' section — where you'll teach me what you find."

**Hassan**: "Start with what's going to break."

**Alex**: "Three things, in order of likelihood. **One**: the prior-claim rule will misfire in cases where Guidewire's closed-date field is null because the claim is still open. We have a default — treat null as 'still open' and escalate — but the routing logic is brittle. If you see a spike in escalations on a Monday, that's the most likely cause. **Two**: the LLM will occasionally produce a comm where the empathy element fails — usually on long claimant narratives where Claude over-summarizes. ToneSupervisor catches most; some leak. Sample 20 random auto-sent comms each week and forward any that fail your gut to Sienna and me. **Three**: the integration to Splunk has a known issue with timestamp normalization for backdated claims — the trace shows UTC but our internal SOPs reference Eastern. Kayla has a fix in QA."

**Hassan** *(taking notes)*: "Three things in the runbook for what to do when claims back up?"

**Alex**: "Yes — first page is queue analysis. If the queue is over 30 minutes for more than 2 hours straight, run the diagnostic script in the runbook. It outputs which agent is the bottleneck — Drafter, ToneSupervisor, ComplianceCritic, or Splunk ingestion. Then you know whether to page Kayla (integration), me (model), or Anil (infrastructure)."

**Hassan**: "What's the actual paging order?"

**Alex** *(pulls up on-call doc)*: "Tier 1 — anything that breaks routing logic, page me. Tier 2 — anything that breaks integration or delivery, page Kayla. Tier 3 — anything Marcus or Tom would care about (audit trace gap, regulatory finding pattern, eval drift), page me AND notify them. Cell number, Slack, email — in that order. After 90 days, my line drops off; Kayla becomes Tier 1 + Tier 2 and you triage Tier 3."

**Hassan**: "What about Janet?"

**Alex**: "Janet's not on the page chain. She's on the weekly review chain — every Monday, sample 20 randomized auto-sends from the prior week, you and Janet score against the bar. Anything below 4/5 — flag for me and Sienna. After 90 days that becomes Sienna and Janet."

**Hassan**: "And what about you and me — what's our cadence after this week?"

**Alex**: "Daily for the first 14 days. 15 minutes, 9am ET. We'll burn through real incidents fast. Then weekly through Q4. Then monthly check-ins."

**Hassan**: "Good. Last thing — your spreadsheet logic vs ours. Our QA spreadsheet caught about 80% of the worst BPO drops. Your thing is supposed to catch them at the source. How do I tell, in production, whether we're catching what the spreadsheet would have?"

**Alex**: "I built that. Run `python scripts/spreadsheet_parity.py` in the prototype folder — it pulls the last 7 days of claims, runs your old spreadsheet logic against the same data, and shows the delta. Ideally zero — anything we'd flag, the new system caught upstream. Anything in the delta is a regression."

**Hassan**: "Brilliant. I'll run it Monday morning."

*(Wraps at 41 min, with Kayla on standby for the integration walkthrough.)*

## Post-session captures

### What got handed over

1. **Runbook**: top 5 likely incidents + diagnostic script
2. **On-call doc**: tier 1/2/3 paging chain with 90-day handoff to Kayla as Tier 1+2
3. **Weekly review chain**: Monday 20-claim sample, Hassan + Janet
4. **Cadence**: daily 15 for 14 days, weekly through Q4, monthly after
5. **Spreadsheet parity check**: scripts/spreadsheet_parity.py runs Hassan's old logic against new system data

### What Hassan asked that I hadn't anticipated

- The Janet question (Janet's role in the cadence). Right answer was clear in my head; I should have built it into the on-call doc explicitly. Updating.
- The spreadsheet-parity question. I had built the script but hadn't named it for him. Should have led with this in the demo.

### What he flagged for me to follow up on

- "How do I tell if you missed something culturally?" — a worry he didn't articulate fully. I'll check in on this at the daily 15 next week.

## Recap email sent (12:00 PM)

Subject: `[Calder] Hassan handoff — daily 15 starts Monday + 90-day Kayla escalation transfer`

> Hassan — recap.
>
> 1. **Daily 15 at 9am ET** for 14 days starting Monday.
> 2. **Tier 1+2 page chain** transfers from me to Kayla at Day 90; you stay as Tier 3 triage.
> 3. **Monday 20-claim sample review** with Janet, weekly. Scoring: 4/5 minimum.
> 4. **Spreadsheet parity check** Monday morning — `python scripts/spreadsheet_parity.py`. Anything in the delta is a regression.
> 5. Three known fragility patterns: prior-claim closed-date nulls, long-narrative empathy fails, Splunk timestamp normalization (Kayla fix in QA).
>
> Talk Monday 9am.
>
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Codification | 5 | Runbook + on-call doc + parity check together = the operational handoff |
| Reusability instinct | 5 | The 90-day Kayla transfer pattern is reusable for the next engagement |
| Customer-political acuity | 4 | Should have led the Janet question rather than wait for Hassan to ask |
| Productionization discipline | 5 | "Things that will break" section is the right opener — anticipates without overpromising |
| Outcome ownership | 5 | Hassan is not just a contact; he's the operational owner with cadence + tools + escalation paths |

**Keep**: opening with "you've been working on this for 7 years" frame; leading with "things I haven't anticipated"; the spreadsheet-parity tool.

**Fix**: anticipate the Janet question — operational handoff means more than just FDE-to-engineer; it includes the user-trust loop.
