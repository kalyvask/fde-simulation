# Framework 16: Trust Surface Design

> The eval passes and nobody uses it. Five decisions define the contract between your agent and the customer's end users: attribution, transparency depth, the publish gate, the permission model, and stakes routing. Name all five before week 3.

## The failure this framework prevents

The repo's other frameworks get you to an agent that *works*: the right wedge ([Outcome Risk Matrix](outcome-risk-matrix.md)), the right boundaries ([workflow decomposition](workflow-decomposition.md)), the right shapes ([agent shapes catalog](agent-shapes-catalog.md)), the right proof ([4-dimensional testing](4-dimensional-testing.md)), the right gates ([agent exploitation taxonomy](agent-exploitation-taxonomy.md)).

None of them get you to an agent that gets *used*. That's a different failure, and it's the more common one on real engagements:

- Rachel Kim quietly routes around the system because she can't tell which numbers in the draft came from the transcript and which the model produced.
- Janet reviews all 20 drafts line-by-line at week 4 exactly as carefully as at week 1, so the 4.2h → 1h SLA win never lands.
- Marcus blocks the rollout because "the agent did it" and "the adjuster did it" look identical in the Guidewire record.

Every one of those is a **trust surface** failure, not a model failure. Pass^k=5 doesn't touch any of them. The Product column of the [3-lens scaffold](3-lens-scaffold.md) has one line for this — *trust levels (act / ask / escalate)* — and this framework is the method behind that line.

The senior framing: **trust is infrastructure you scope and staff, not a property that emerges from a good model.** If it isn't a line in the week-2 build plan, it isn't a requirement.

## The five decisions

| # | Decision | The question | Default if you don't decide |
|---|---|---|---|
| 1 | **Attribution** | Can the user tell which changes were the agent's vs. a human's, and reverse exactly those? | Undifferentiated record → compliance blocks the rollout |
| 2 | **Transparency depth** | How much of the agent's process is shown, and to whom? | Everyone gets everything → lead user drowns, customer-facing user waits |
| 3 | **The publish gate** | Where does the agent's work cross from producing to reaching another human? | Gate placed by action type, not by who sees the output |
| 4 | **Permission model** | What can the agent reach, and who decides? | A second permission system that drifts from the customer's real one |
| 5 | **Stakes routing** | Which moments go straight to a person, and by what rule? | Routed by task type, so the emotionally loaded cases get the routine path |

### 1. Attribution — delineate human from agent

The requirement: every agent-produced change is labeled as agent-produced **in the record where it lives**, not in a separate log, and reversible at the granularity the agent worked at.

"Undo the whole run" is not attribution. It punishes the user for the agent's one bad step, so they stop using the run rather than the step.

This is the one decision that is simultaneously a *user* requirement (Janet needs to see what to check) and a *regulator* requirement (Marcus and Mei need an examiner-readable answer to "who did this"). The [Auditor shape](agent-shapes-catalog.md) is how you build it; this is why it's non-optional even in a read-only v1.

**Engagement test:** open one output the agent touched. Can you point at the agent's contribution and revert only that? If not, you have a week-4 blocker, not a v2 nice-to-have.

### 2. Transparency depth — calibrate to accountability, not to capability

The instinct is to show the full reasoning chain. That's right for some users and actively wrong for others, and the variable is **who carries the consequence of the output**:

| User | Show | Why |
|---|---|---|
| Accountable for the output (Janet signs the claim; Rachel's name is on the note) | Process: sources touched, steps taken, what was skipped, what was low-confidence | They have to defend it, so they have to check it — and checking is only possible if the process is legible |
| Receiving a service (a claimant, a support caller) | Outcome, plus a visible route to a human | Process detail is friction between them and resolution; feeling stuck behind an agent is the negative experience |
| Delegating a reversible chore | Outcome, process available on demand | Nobody reads a trace for work they don't care about |

The tell that you got this wrong: the lead user starts skimming the trace instead of reading it. Skimmed transparency is worse than none, because it manufactures the appearance of review — this is the [3-lens scaffold](3-lens-scaffold.md)'s "auto-trust adjuster" segment, and over-showing is what creates them.

**Engagement test:** for each user segment in your Customer column, one line — accountable or served? Then the transparency depth follows from the answer, not from what's easy to render.

### 3. The publish gate — producing is not publishing

Draw the boundary at the point where the agent's work reaches a human other than its operator. An agent drafting, exploring, and revising in a holding queue needs no gate. The same agent sending the email, filing the record, or shipping the note to the PM needs a person.

This is the discipline already embodied in both reference prototypes (v1 is read-only, output lands in Rachel's / Janet's queue, never auto-sends). This framework names *why* so you can defend the line rather than just having drawn it, and so you can place it correctly on a case where the write path isn't obviously catastrophic.

**Where the gate lives matters as much as where it sits.** The approval belongs *next to the object the agent is shaping*, in the system the user already works in — not in a separate console, review queue, or chat panel. Charlie Sutton, Chief Design Officer at Atlassian, builds agent interactions directly into Jira and Confluence rather than a side panel, and treats chat as *"a session log and a guardrail, rather than the primary method of interaction."*

For an FDE this is an integration requirement, not a UX preference. An approval queue in a separate surface is where approvals go to be rubber-stamped: the reviewer has lost the context that would let them catch the problem, so you get the compliance artifact without the compliance. On Calder that means the gate is in Guidewire next to the claim, not in a standalone review app — and it is the difference between Janet actually reviewing 20 drafts and Janet clicking through 20 drafts.

**Engagement test:** list every action the agent can take. For each, name who sees the result. Any action whose result reaches someone other than the operator, without a human approving, is an ungated publish. Then: is each approval rendered in the customer's system of record, or in something you built alongside it?

### 4. Permission model — inherit, don't invent

The agent should inherit the permissions of the account it acts in, not carry its own permission set. Two reasons, and the second is the one that closes the CISO conversation:

- The agent can never reach anything its user couldn't reach — the blast radius is bounded by an access model the customer already trusts and already audits.
- There's no second permission surface to drift out of sync with the first. A parallel permission system is a standing entitlement-review finding from day one.

This is the least-privilege principle from the [agent exploitation taxonomy](agent-exploitation-taxonomy.md) expressed as an *integration* decision rather than a security one. On Calder it's the answer to Rachel Nieman's PHI question; on Helix it's most of James O'Brien's one-pager.

**Engagement test:** name the existing system whose permission model the agent inherits. If the answer is "we'd define roles for the agent," you've invented the second system.

### 5. Stakes routing — "can it?" vs. "should it?"

Route by the **emotional and consequential weight of the moment**, not by task type. The same task type spans both: a routine claim and a claim filed after a death in the family are the same Guidewire object and a completely different human moment.

The rule to write down: functional, low-stakes, reversible → agent handles it. Emotionally loaded, irreversible, or reputation-bearing → straight to a person, with the handoff visible to the user rather than silent.

The formulation to use in the room: *the question isn't just "can AI do it?" but "should AI do it?"* — this is the [Outcome Risk Matrix](outcome-risk-matrix.md) applied per-request at runtime rather than per-wedge at design time.

**Engagement test:** name the two request classes in the customer's workflow that share a task type but not a stakes level. If you can't, you haven't talked to the lead user enough.

## Autonomy is earned, not launched

The five decisions above define v1's contract. The upgrade path is the same principle as the Outcome Risk Matrix's *"v1 protects the kill-criteria; v2 earns autonomy"*, made measurable:

The mental model to give the customer is **onboarding, not configuration**. Sheta Chatterjee compares building trust with an agent to onboarding a team member: a new hire doesn't have enough context to work autonomously yet, and neither does a new agent. Gemini Enterprise deliberately starts with *more* checkpoints and approvals than it may ultimately need, then expands autonomy as the relationship proves itself in practice.

Deliberate over-gating at launch is the move, and it inverts the usual instinct to launch at the autonomy level you hope to reach. Walking autonomy back after an incident costs trust you don't get returned; walking it forward costs nothing. It's also the honest answer to a buyer who reads v1's conservatism as timidity: this is the onboarding period, and here is what ends it.

1. Ship gated. Every publish action requires approval.
2. Instrument the **override rate** per action class — how often the human changes or rejects what the agent produced.
3. Widen the gate only where the override rate is near zero over a named window (the reference engagements use 90 days).
4. A persistently high override rate is not a prompt-tuning problem. It's evidence that this task shouldn't have been delegated, and the honest move is to say so in the field memo.

This gives the customer a written answer to "when do we get to turn the human off," which is the question the economic buyer asks in week 4 and the one FDEs most often answer with vibes.

## The gate is not the finish line

Dimension 4 of [4-dimensional testing](4-dimensional-testing.md) is production observability. This is the reason it's load-bearing rather than a nice-to-have: an agent's real behavior distribution doesn't exist until real people use it on real work, so pre-launch validation has a ceiling that arrives well before confidence does. Rachel Been's team at Expedia releases agents before they're ready and learns from actual usage: *"You're not going to launch something that's perfect on day one, because that's not how building agents works."* Her conclusion generalizes — you can't script an agent perfectly, you can only build the conditions for it to get better.

Two translations for a regulated engagement, because "release before it's ready" does not port directly to Calder or Helix:

- **Early release is about polish, not safety.** The five decisions above are what make it survivable. Shipping early *behind the gates* is a different act from shipping early with autonomy.
- **Where a bad output lands on someone other than the operator, the equivalent of "release early" is a small supervised cohort with full observability** — Janet's queue, Rachel's 20-draft review — not general availability. Same learning loop, contained blast radius. This is what week 3 validation already is; name it as the mechanism rather than a checkpoint.

The handoff consequence: the field memo needs an owner for the refinement loop, not just an operational owner for the running system. Instrument for where the agent gets stuck and where users drop off *before* go-live, because that's the data the customer's team needs in month two and cannot backfill. An engagement that hands over a working agent with no loop hands over a decaying asset.

**Engagement test:** what will the customer learn in the first 30 days of real use that your eval suite structurally cannot produce, who owns acting on it, and is the instrumentation in place before handoff?

## Worked example (Calder, FNOL drafting wedge)

| Decision | Calder v1 |
|---|---|
| Attribution | Every draft field tagged agent-generated vs. adjuster-edited in the Guidewire record; adjuster can revert per field, not per draft. Auditor agent writes the examiner-readable chain (Tom + Marcus both consume it) |
| Transparency depth | Janet (accountable, signs the close): full trace — policy clauses cited, NHTSA lookups, what the tone supervisor flagged. Claimant (served): outcome only, plus "reach a human" on every touch |
| Publish gate | Agent drafts into Janet's queue. Nothing reaches the claimant without Janet's approval. No auto-close, no auto-send — the gate is at the claimant boundary, not the draft boundary |
| Permission model | Agent runs as the adjuster's Guidewire identity; sees exactly that adjuster's book of claims. No agent-specific role. Closes Rachel Nieman's PHI-scope question |
| Stakes routing | Routine auto-glass / minor collision → agent drafts. Fatality, minor claimant, litigation flag, or coverage denial → straight to a senior adjuster, and the adjuster is told why it routed |
| Approval placement | Approval rendered in Guidewire on the claim itself, not a standalone review console — Janet approves in the system she already lives in, with the claim context on screen |
| Autonomy ladder | Deliberately over-gated at launch (every draft approved, including classes we expect to clear). Override rate tracked per claim class. Gate widens on a class only after 90 days near-zero override, and Marcus signs each widening |
| Refinement loop | Stuck-points and drop-off instrumented pre-go-live; Greg's team owns the monthly review of override reasons; named in the field memo alongside the operational owner |

## The probe this defends against

When the interviewer asks *"the eval passes — how do you know the adjusters will actually use it?"*, the weak answer is "we'd do training and change management." The strong answer:

> "The eval proves the agent is right. It doesn't prove anyone will delegate to it, and those fail differently. I scoped the trust surface as five explicit decisions in week 2. Attribution: agent edits are tagged per-field in Guidewire and reversible per-field, which is simultaneously Janet's review affordance and Marcus's audit answer. Transparency: full trace for Janet because she signs the close, outcome-only for the claimant because they want resolution, not process. The publish gate sits at the claimant boundary, not the draft boundary — the agent produces freely, a human publishes. Permissions inherit the adjuster's Guidewire identity, so there's no second access model for Rachel to review. And routing is by stakes, not task type: a fatality claim and a fender-bender are the same object and a different human moment. Autonomy widens per claim class on a measured override rate, not on a launch date — and the approval renders in Guidewire on the claim, because an approval in a separate console is one that gets rubber-stamped. I'd also tell Maria plainly that day-one won't be the final version: I instrument stuck-points and drop-off before go-live and hand over the refinement loop with a named owner, because an agent's real behavior distribution doesn't exist until adjusters use it."

This is also the answer to *"why is your v1 so conservative"* — it isn't conservatism, it's a gate with a written removal condition.

## Where this comes from

Field practice from design leaders shipping agentic products in production, collected in Figma's *Writing the rules of agentic design*: human-vs-agent attribution and process "thinking states" (Sheta Chatterjee, Google, on Gemini Enterprise), trust as deliberate infrastructure and the can-it/should-it routing rule (Thomas Vidal, Accor), transparency calibrated to context in financial services (Deidre Kolarick, Capital One), the producing-vs-publishing distinction, agent interactions built into existing interfaces with chat as session log (Charlie Sutton, Atlassian), permission inheritance (Atlassian), the onboarding metaphor for autonomy, and learning from real usage (Rachel Been, Expedia). The mapping onto FDE engagement decisions and the interview defenses is this repo's.

## Quick reference

```
TRUST SURFACE (name all five in week 2, before the build plan):

  1. ATTRIBUTION      Agent vs. human, in the record, reversible per-step
                      (not "undo the whole run")
  2. TRANSPARENCY     Accountable user -> show process
                      Served user      -> show outcome + route to human
  3. PUBLISH GATE     Producing is free; reaching another human needs approval
  4. PERMISSIONS      Inherit the customer's identity model; never invent a second
  5. STAKES ROUTING   Route by emotional/consequential weight, not task type
                      "Can AI do it?" vs "SHOULD AI do it?"

  WHERE THE GATE LIVES  Next to the object, in the customer's system of record.
                        Separate console = rubber stamp. Chat = session log, not front door.

  AUTONOMY LADDER     Onboard, don't configure. Launch with MORE gates than you need.
                      Ship gated -> measure override rate -> widen per class
                      High override rate = wrong task to delegate, not a prompt bug

  REFINEMENT LOOP     Pre-launch instrumentation + named owner in the field memo.
                      Regulated = supervised cohort, not GA. Ship early behind gates.

Senior move: the eval proves it's right; the trust surface proves it gets used.
```

## See also

- [`3-lens-scaffold.md`](3-lens-scaffold.md) — the Product column's *trust levels (act / ask / escalate)* line; this framework is the method behind it
- [`outcome-risk-matrix.md`](outcome-risk-matrix.md) — the same reversibility logic applied at wedge-selection time rather than per-request
- [`agent-exploitation-taxonomy.md`](agent-exploitation-taxonomy.md) — least privilege as a security gate; decision 4 is its integration-side expression
- [`agent-shapes-catalog.md`](agent-shapes-catalog.md) — the Auditor and Router shapes are how decisions 1 and 5 get built
- [`4-dimensional-testing.md`](4-dimensional-testing.md) — dimension 4 (production observability) is the instrumentation the refinement loop runs on
