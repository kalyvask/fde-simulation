# Simulation 4: Client Simulation Round (~20-30 min per scenario)

> The round that eliminates more technically-strong candidates than any other. Live role-play of a frustrated, impatient, or hostile customer in a high-stakes moment. Tests whether you can handle real client dynamics under pressure: ownership language, de-escalation, technical-to-non-technical translation, and composure.

## What this simulation tests

Whether you can be put in front of a $10M+ customer at the worst moment of an engagement and not make it worse.

Public sources consistently flag this as the round that "eliminates many technically strong candidates" who passed the system design + coding + take-home rounds. The reason: technical chops don't help when the customer's exec demo is failing in real time.

| Common scenario | What it tests |
|---|---|
| Live demo failing in front of customer leadership | Composure; diagnostic discipline under pressure |
| Customer demanding mid-engagement scope expansion | Pushback with substance, not politics |
| SLA breach in maintenance mode, angry CTO on the call | Root-cause framing; transparent comms |
| Customer wants to deploy something compliance hasn't cleared | Backbone; protecting the customer from themselves |
| New stakeholder joins meeting and disagrees with everything done so far | Reading the room; stakeholder re-mapping live |

## When this round shows up

- Round 3 in the typical 4-round FDE loop (after technical + deployment scenario, before behavioral)
- Sometimes embedded in the take-home Review round (a live curveball mid-defense)
- Rarely standalone — usually framed as "I'm going to play the customer for the next 20 minutes"

## What's in this folder

| File | Purpose |
|---|---|
| `playbook.md` | The 5-step de-escalation script + 5 fictional scenarios to practice with Claude as the customer |

## How to run this simulation

### Solo, with Claude as the customer

1. Read `playbook.md` once end-to-end (~15 min)
2. Open a fresh Claude conversation
3. Copy a scenario prompt (each has Claude playing a specific customer role)
4. Run the simulation live for 20-30 min
5. At the end, ask Claude to grade you against the 5-step script + the 4 strong-signal markers

### With a peer

1. Peer reads the playbook scenario in advance
2. They play the customer with the persona context provided
3. You handle it cold
4. They debrief with you against the rubric

### Cadence

Don't grind through all 5 in one sitting. One scenario per evening over a week. Pattern: the first scenario will feel terrible. The second will be 30% better. By scenario 5 you'll have muscle memory for the de-escalation script.

## What "good" looks like

By the end of 5 scenarios, you should be able to:

1. Name the customer's situation back to them in your first 10 seconds (acknowledgement before diagnosis)
2. Ask 2-3 diagnostic questions before proposing anything
3. Use ownership language consistently ("I will" not "we will check")
4. Never blame the customer's systems even when they're the problem
5. End every scenario with a specific commitment (what you'll do, by when, who else needs to know)

If you can do all 5 in any scenario thrown at you, you've cleared this round.

## What "bad" looks like

The patterns that get candidates rejected:

| Pattern | Why it fails |
|---|---|
| Jumping to a solution without asking diagnostic questions | Signals you don't actually listen to customers |
| "Let me check with the team" without a specific time | Signals you don't own outcomes |
| Defending your design when the customer is upset | Signals you prioritize ego over outcomes |
| Going silent for >5 seconds when pushed | Signals you can't think under pressure |
| Promising a fix you can't guarantee | Signals you don't understand consequences |
| Blaming the customer's data / systems / users | Even when true, this is the rejection trigger |

## Why this round matters more than the technical rounds

Public sources are consistent on this:

> "Forward Deployed Engineers spend more time in customer conversations than in code. A candidate who can't handle a frustrated customer can't do the job, no matter how good their code is."

The technical rounds test whether you CAN do the job. This round tests whether you can do it on the worst day. Both matter; this one is harder to fake.
