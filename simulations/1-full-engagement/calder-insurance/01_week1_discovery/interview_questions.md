# Interview Question Bank — Week 1 Discovery

Questions per stakeholder. Listen for what they don't volunteer. Notes column = what to write in your interview transcript.

## Maria Vasquez, CCO (economic buyer)

| Question | What to listen for |
|---|---|
| What does success look like in 18 months, in numbers and in narrative? | The board metric vs the personal motivation |
| If we hit the cost target but introduce one regulatory finding, did we win? | Risk tolerance |
| Who in the org is most threatened by this work, and how should we manage them? | Political map |
| If this works on FNOL, what's the second workflow you'd want to attack? | Scope of imagination |
| What would make you kill this project in month 6? | Failure modes that matter |

## Greg Hadley, SVP Claims Ops (champion)

| Question | What to listen for |
|---|---|
| Walk me through FNOL end to end. Where does it die today? | The actual workflow vs the diagram |
| Show me a claim that should have been auto-paid and wasn't. Why didn't it? | The real failure mode |
| What's your BPO doing well that we'd lose by replacing them? | Hidden value |
| If I could give you one report on Monday morning that would change how you run the team, what would be on it? | Operating reality |
| Who on your team would you trust to be the internal product owner of this AI workforce? | Champion's champion (= sustainability post-handoff) |

## Priya Shah, Director FNOL Operations (operator)

| Question | What to listen for |
|---|---|
| Walk me through one shift, hour by hour. | Where the time actually goes |
| What workaround has your team built that I'd never find in any process doc? | Tribal knowledge — gold for the agent |
| What's the most common reason a claim sits in your queue overnight? | Bottleneck |
| When the BPO sends something back wrong, how do you spot it? | The validator pattern you can encode |

## Frontline claims adjusters (3-5 of them, separately)

| Question | What to listen for |
|---|---|
| What's the most soul-crushing part of your shift? | What to automate first |
| What's the part of the job you wish you had more time for? | What to elevate them toward |
| What does a "bad" auto-pay decision look like, in your gut? | Fraud signals + edge cases |
| If a tool flagged a claim for you to review, what would make you trust the flag? | Explainability requirements |
| What part of the job are you afraid AI will get wrong? | Risk surface from the people closest to it |

## Tom Reilly, Quality / Audit Lead

| Question | What to listen for |
|---|---|
| What does a "bad close" look like? Walk me through three examples from the last 90 days. | The audit failure modes |
| What does an NAIC market-conduct examiner look for when they pull a claim file? | Audit-trail requirements |
| What's the worst regulatory finding the team has ever had, and what changed because of it? | Scar tissue → constraints |
| If an AI handles a claim end to end, what would the audit packet need to contain? | Trace requirements |

## Dana Kowalski, SIU Lead (fraud)

| Question | What to listen for |
|---|---|
| Walk me through three fraud cases from the last quarter. What did you spot first? | Signal patterns |
| Which fraud signals are obvious in narrative text and which require external data? | Tool-call requirements |
| What's a fraud case the team caught late, and what would have caught it earlier? | The eval set's hardest cases |
| What's the false-positive cost? How many SIU referrals can you process per week without overflow? | Calibration constraint |

## Anil Gupta, CIO

| Question | What to listen for |
|---|---|
| Walk me through the Guidewire footprint. What's customized, what's vanilla? | Integration surface |
| What APIs exist today, what's accessible via batch, what's locked behind a screen? | What you can integrate |
| Who owns the Guidewire integration queue, and how long is the wait? | Scheduling reality |
| What other AI experiments has the team tried, and what happened? | Existing scar tissue |

## Rachel Nieman, CISO

| Question | What to listen for |
|---|---|
| What's the bar for a vendor to handle PII and PHI from claim files? | The deployment gate |
| What logs do we need, retention period, who reviews? | Observability requirements |
| What's the org's stance on prompt-and-response logging by the model vendor? | Anthropic/OpenAI BAA terms |
| What would block a production deployment in your shop? | The list to design against |

## Marcus Hill, Compliance Officer

| Question | What to listen for |
|---|---|
| Which state DOI rules apply? Which are most restrictive? | The policy library you need to encode |
| Where in the workflow does the Unfair Claims Settlement Practices Act bite? | Deterministic guardrail requirements |
| Are there state-specific human-licensed-adjuster requirements for coverage decisions? | Where the agent must hand off |
| What documentation does an examiner expect for AI-assisted decisions? | Audit-trace requirements |

## Lin Zhao, Finance / Actuary

| Question | What to listen for |
|---|---|
| How is LAE ratio calculated for this line? What's the benchmark? | The savings model |
| What's the unit-economics target — $/claim or LAE % or both? | Success metric |
| How sensitive is the savings model to claim mix shift? | Sensitivity analysis |
| What's the depreciation/capitalization policy on this kind of project? | Procurement reality |

## Kevin Park, BPO Contract Owner

| Question | What to listen for |
|---|---|
| What's the BPO doing well that we'd lose by absorbing the work? | Hidden value |
| When does each contract end, and what are the exit terms? | Timing constraint |
| What % of claims do they handle without escalation today, by line? | Baseline for the agent's bar |
| If we kept one BPO and replaced one, which and why? | Fallback strategy |

## Cross-stakeholder check questions

Ask several of them the same question. Triangulation reveals the real picture.

- "If we get this 80% right, what does that look like in your role?"
- "What's the one thing about this engagement you'd change if you were running it?"
- "Who haven't I talked to that I should?"
