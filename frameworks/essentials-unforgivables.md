# Essentials & Unforgivables — The Hiring-Side Lens

> Every other framework in this repo is *candidate-side*: how you do the work, how you prep the story. This one flips the table. It's the rubric the hiring manager is scoring you against while you do the work — the traits they're trying to confirm (Essentials) and the anti-signals that get you rejected no matter how strong the rest of the loop was (Unforgivables).
>
> Source: the "Essentials vs. Unforgivables" model from Palantir-origin FDE-hiring writing (anjor.xyz, *Forward Deployed Engineers and how to hire them*, 2024). The framing is theirs; the mapping to the simulation moments below is this repo's.

## Why this framework exists

The other frameworks tell you what a good artifact looks like. They don't tell you what the person across the table is actually deciding. That decision is simpler and more brutal than the rubric suggests:

> "At the end of the day it's about getting to know the person — what makes them tick, what keeps them going, and why."

An FDE gets dropped into a hostile, ambiguous customer room with no playbook and is expected to produce business impact. The interviewer is running one test: *will this person create value in the chaos, or will they freeze, chase the shiny thing, or become a maintenance burden?* The Essentials are what they want to see. The Unforgivables are the three ways smart candidates fail anyway.

A related calibration from the same source: **learning velocity beats raw experience.** They're plotting ability-over-time, not years-on-resume. A candidate who visibly gets sharper across the engagement (picks up the domain language, tightens the wedge after pushback) outscores one who arrived more polished but flat. This is already a live grading dimension in the discovery interviews ("Domain learning velocity").

## The Essentials — what they're confirming

| Essential | What it means | Where the simulation exercises it | What "confirmed" looks like in an artifact |
|---|---|---|---|
| **Outcome-oriented** | Always keep the goal in mind; solve the actual problem, not the interesting one | Wedge selection (Outcome Risk Matrix); every "why this slice" defense | The wedge is tied to the customer's kill-criteria, not to engineering tractability. The metric forecast names the business consequence, not a vanity number. |
| **Critical thinking / comfort with ambiguity** | Structure a mess no one has structured for you | Week-1 discovery on a 12-stakeholder political map with no clean brief | A discovery memo that converges 4 sources into one wedge hypothesis, naming what's still unknown rather than pretending it's resolved. |
| **Grit** | Willingness to take on the *hard* problem (not just to work hard) | The integration/data-pull layer; the deterministic compliance engine no one wants to build | You went after the load-bearing-but-unglamorous problem (the swivel-chair data hunt, the per-state SLA encoding) instead of the demo-friendly one. |
| **High chaos tolerance** | Stay productive when the demo fails and the customer is angry | The client-simulation (sim 4); the hostile oral grill (sim 1) | You hold composure under a failing-demo / SLA-breach scenario and keep moving toward the outcome instead of freezing or deflecting. |

## The Unforgivables — the three ways strong candidates still fail

These are disqualifiers. A candidate can ace the technical rounds and still get a no on one of these, because each one predicts a specific failure in a real customer room.

### Unforgivable 1 — Chasing trendy solutions disconnected from impact

The candidate reaches for the impressive architecture — the 7-agent workforce, the embedding-based tone detector, the autonomous trade-idea generator — because it's headline-worthy, not because it's what the customer's kill-criteria demands. In a real engagement this burns the budget on the wrong thing and the metric never moves.

**This is the single most common Unforgivable in this simulation**, and several Expert Traps are concrete instances of it:
- Calder **Trap 1** (picking auto-pay because the data is clean) and **Trap 2** (LLM for state SLAs because "it can read the regs")
- Helix **Trap 1** (idea-generation wedge because it's ambitious) and **Trap 4** (shipping a textbook tone-shift detector with no calibration)
- The generic version: a 7-agent decomposition where a 3-agent one wins. Complexity as a flex.

**Artifact anti-signal:** the wedge is defended on *technical interest or tractability*, not on the customer's named kill-criteria. The scope-out section is thin (nothing was consciously left out).

### Unforgivable 2 — Passivity / waiting for direction

The candidate waits to be told what the wedge is, what data to ask for, who to talk to. An FDE who needs a backlog handed to them is useless in a room where no backlog exists. The job *is* to manufacture direction from ambiguity.

**Trap instances:**
- Calder **Trap 3** (didn't think to ask Tom for the eval set) and **Trap 5** (treated Rachel as a week-4 checkbox instead of driving her sign-off in week 1)
- Helix **Trap 5** (didn't book Carmen because she "isn't a buyer")

**Artifact anti-signal:** no proactive "asks" table with owners and dates. Stakeholders are listed but not *driven* — no one is being pulled toward a sign-off. The candidate's moves are all reactions to what the brief stated, with nothing surfaced that the brief didn't.

### Unforgivable 3 — Entitlement / high-maintenance

The candidate expects clean data, a defined scope, a cooperative customer, and credit. They get defensive under pushback and treat the messy parts as someone else's job. This one rarely shows in the written artifacts — it shows in **how you handle the hostile oral grill (sim 1) and the client-simulation (sim 4).**

**Behavioral anti-signal:** under the grill, defends every choice as correct, treats the premise of a hostile question as an insult rather than a probe, or implies the difficulty was the customer's fault. The tell is the opposite of grit: "the data wasn't good enough for me to..."

## How to deploy this framework

- **Before you start a case:** read the four Essentials. They're the lens you want every artifact to confirm.
- **During the post-mortem:** after the Expert-Traps post-mortem flags which traps you walked into, translate each trap into its Unforgivable. "I picked the idea-generation wedge" isn't just Trap 1 — it's *Unforgivable 1, chasing the trendy thing*. That's the framing the interviewer uses, so it's the framing you should self-diagnose in.
- **Before the oral grill:** Unforgivable 3 lives here. Going in knowing the interviewer is reading your composure for entitlement is half the defense.
- **Reverse practice:** ask Claude to interview *you* as the hiring manager and score the conversation against the Essentials and Unforgivables, not the artifact rubric. ("Interview me as Sarah's hiring manager. Probe my A→B→C decisions on the Helix wedge. Score me on the four Essentials and flag any Unforgivable.")

## Quick reference

```
ESSENTIALS (what they confirm):
  1. Outcome-oriented        -> wedge tied to kill-criteria, not tractability
  2. Critical thinking /     -> 4-source convergence from a messy brief
     comfort with ambiguity
  3. Grit                    -> went after the unglamorous load-bearing problem
  4. High chaos tolerance    -> composure in the failing-demo / hostile grill

  + Learning velocity > raw experience (got sharper across the engagement)

UNFORGIVABLES (instant no):
  1. Chasing trendy, impact-disconnected solutions
     -> Calder Traps 1, 2 ; Helix Traps 1, 4 ; over-engineered decomposition
  2. Passivity / waiting for direction
     -> Calder Traps 3, 5 ; Helix Trap 5 ; no proactive asks table
  3. Entitlement / high-maintenance
     -> shows in the oral grill + client simulation, not the written artifacts

THE INTERVIEWER'S ONE TEST:
  "Will this person create value in the chaos?"
```
