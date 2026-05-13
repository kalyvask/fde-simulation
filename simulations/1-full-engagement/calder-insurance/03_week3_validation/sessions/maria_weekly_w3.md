# Maria Weekly — Week 3 Friday 4:15 PM, 15 min

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Constructed dialogue showing the standing weekly cadence in motion.

## Setup

Friday week 3, 4:15 PM ET. Standing 15-min slot Maria reserved on her calendar from kickoff. Zoom, camera off, Maria multitasking. Same posture as kickoff — efficient, board-savvy, low-bandwidth-for-fluff.

## Selected exchanges

**Alex** *(opening)*: "Maria, three things in 15 minutes. Status, one decision I need from you, one risk I want you to know about."

**Maria**: "Go."

**Alex**: "Status. Eval suite is at 25 cases, passing 91% weighted on real Claude. Janet reviewed 20 drafts Tuesday; she had 4 concrete changes I'm shipping by EOD today, then 20 fresh drafts Monday. Her 18-of-20 sign-off is the rollout gate for week 4. Marcus biweekly was Wednesday; 4 design tweaks shipping by EOD today including a closed-date fix on the prior-claim rule. Anil's sandbox is live; integration tests green. End-to-end demo on dev data passes. We're on track for the Friday week-4 demo."

**Maria**: "Decision?"

**Alex**: "Janet wants to send the all-hands rollout message herself, not Priya. I support that — strongest possible adoption signal — but it changes who owns the rollout narrative internally. Want your sign-off before I tell Priya."

**Maria** *(immediate)*: "Yes. Janet sending it is the right call. I'll mention it to Priya at our 1:1 Monday — leave it with me."

**Alex**: "Done. Risk: the wedge currently passes 91% on adversarial cases. Three failures: two are cases where the system is being correctly conservative — escalating when input is degraded — and the expected was wrong. One is a real prompt bug — Claude using 'soon' in a draft when it shouldn't. The bug is fixed; eval is back to 100%. I'm flagging because if I had not run adversarial cases, the bug would have shipped. The risk you should know about: there are likely more bugs of this shape we haven't found because the eval suite isn't yet at 50 cases. Sienna's set lands next week; that's when we'll know."

**Maria**: "Honest. Appreciate you flagging it. What's your hedge if Sienna's set surfaces a category we missed?"

**Alex**: "Two paths. If it's a class of cases we can fix with a prompt change or a deterministic rule, we ship by demo. If it's a class that needs architecture work, we narrow the wedge in v1 — exclude that class — and put it in v2. The gate is: can we fix it in 5 days without compromising the rest?"

**Maria**: "Reasonable. Don't extend the wedge demo for a single bug class. Better to ship narrow than ship late. The board doesn't care about the boundary; they care about whether something works. Show me something that works on a clear slice."

**Alex** *(note)*: "Got it. Narrow over late. I'll build the demo agenda around the cases we know we handle, with the boundary explicit."

**Maria**: "Anil told me about the 90-days-after question?"

**Alex**: "Yes. Hassan-as-operational-owner is my proposed answer; Anil's on board with it. I want to walk you through the handoff structure in the demo, not separately. Would prefer to bake it into the rollout proposal so the question is answered, not surfaced."

**Maria**: "Fine. Last thing — my chief of staff is going to be on the demo. Alicia. Don't be thrown by her. She tracks risks and asks blunt questions. If she doesn't push back, I get worried."

**Alex**: "Understood. I'll prepare for blunt questions."

**Maria**: "Talk Friday."

*(Wraps at 13 min.)*

## Post-session captures

### What changed

1. **Janet sends the all-hands** — confirmed by the buyer
2. **Wedge demo strategy: narrow over late** — explicit "if it doesn't work yet, we exclude it from v1 and put it in v2"
3. **Alicia, Maria's chief of staff**, will be on the demo. New stakeholder.
4. **Hassan handoff baked into the rollout proposal**, not a separate conversation.

### What stayed the same

- Demo Friday week 4
- Standing weekly Fridays 4:15
- Cell-number-equivalent (Marcus) pattern continues

### Stakeholder map updates

- Alicia (Maria's chief of staff): NEW. Power: high (proxies Maria). Stance: tracks risks. Operating note: blunt questions = she's engaged; silent = she's worried.

## Recap email sent (4:35 PM)

Subject: `[Calder] Friday W3 weekly — Janet sends all-hands; demo narrows over late`

> Maria — recap.
>
> 1. **Janet sends the all-hands rollout message** (you'll mention to Priya at Monday 1:1).
> 2. **Demo strategy: narrow over late.** If Sienna's set surfaces a class of cases we can't fix in 5 days, we exclude from v1 and explicitly put in v2. Boundary is explicit.
> 3. **Hassan as operational owner** baked into the rollout proposal at the demo, not separately.
> 4. Adversarial eval surfaced 1 real bug (fixed) + 2 cases where the system was correctly conservative. Documenting the pattern.
>
> Adding Alicia to my prep list.
>
> Talk Friday.
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Outcome ownership | 5 | "Narrow over late" is the kind of strategic frame the buyer wants from the FDE, not the other way |
| Customer-political acuity | 5 | "Don't be thrown by Alicia" is the kind of detail the buyer only shares with someone she trusts; the cell-number-equivalent in the buyer relationship |
| Risk awareness | 5 | Surfacing the "we may not know what we don't know" risk before the demo is the senior move |
| Discovery rigor | 4 | Should have asked about Alicia at kickoff; she's been in the wings for 3 weeks |

**Keep**: structure (status / decision / risk), the "narrow over late" framing absorbed cleanly, surfacing the eval-coverage risk honestly.

**Fix**: ask the "anyone else who'll be in the demo?" question 2 weeks earlier. Surprises about Alicia at this stage would have been costly.
