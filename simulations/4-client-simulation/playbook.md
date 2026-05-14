# Client Simulation Round — Playbook

> The 5-step de-escalation script + 5 fictional scenarios for live practice with Claude as the customer.

## The 5-step de-escalation script (memorize this)

When you're put in front of a frustrated customer in a live scenario, follow this order. Every time.

### Step 1 — Acknowledge the situation (first 10 seconds)

Before any diagnosis, before any question, before any proposal: name what's happening from the customer's perspective.

**Template**: "I hear you. This is impacting [their team / their customer / their business outcome] and I'm taking it seriously."

**Why**: customers feel unheard before they feel unhelped. Acknowledgement is the fastest path to a constructive conversation.

**Anti-pattern**: jumping straight to "let me look at the logs."

### Step 2 — Ask 2-3 diagnostic questions

Before proposing a solution, gather the minimum context you need. Targeted, specific, time-bounded.

**Templates**:
- "When did this start? Was there a deployment / config change / data change in the last 24 hours?"
- "What does failure look like — is it a specific user, a specific request type, or everything?"
- "Are you seeing this in production only, or also in staging?"

**Why**: the diagnostic questions are themselves a signal of competence. They show you don't reach for a solution before understanding the problem.

**Anti-pattern**: asking 7 questions in a row (overwhelming) or asking generic questions ("can you tell me more?").

### Step 3 — State what you'll do, by when, with ownership language

Once you have enough to act, commit. Specifically.

**Template**: "Here's what I'll do: [specific action] by [specific time]. I'll [communication mechanism] when [milestone]."

**Strong examples**:
- "I'll have a diagnosis on the integration error by end of day. I'll send you a written update with what I find and a proposed fix."
- "I'll review the deploy logs in the next 30 minutes, then jump on a call with you at 3pm. If I don't have a root cause by then, I'll tell you what I've ruled out and what's left."

**Weak alternatives** (rejection triggers):
- "I'll check with the team and get back to you" (no commitment, no timeline)
- "We'll look into it" (no ownership)
- "It might be on your side" (blame deflection)

### Step 4 — Acknowledge what you don't know

If the customer asks a question you can't answer in the moment, say so. Don't bluff.

**Template**: "I don't have a confident answer on [specific thing] right now. My instinct is [X], but I want to validate by [Y] before committing. I'll have that for you by [time]."

**Why**: bluffing in front of a senior customer who actually knows the technical detail is fatal. Calibrated honesty is high-status.

### Step 5 — Close with a specific commitment

End the conversation with a concrete next step that's in your control.

**Template**: "To summarize: I'll [specific action], by [specific time]. I'll send a written update so [their team / their boss] also has visibility. Anything else you need from me before we close out?"

**Why**: customers leave conversations either with anxiety reduced or anxiety increased. A specific commitment reduces anxiety. A vague "we'll figure it out" increases it.

---

## The 4 strong-signal markers (what the interviewer is grading)

The interviewer is watching for these specifically:

1. **Did you acknowledge before diagnosing?** Most candidates skip step 1.
2. **Did you ask diagnostic questions before proposing?** Most candidates jump to solutions.
3. **Did you use ownership language?** Most candidates default to "we" or "let me check."
4. **Did you avoid blaming the customer's systems?** Most candidates can't resist when the customer's systems are genuinely the problem.

You can lose this round even if your technical answer is correct, because the grading is on these 4 markers, not the technical solution.

---

## The 5 practice scenarios

Run these with Claude one at a time. Don't speedrun. The value is in the repeated reps, not the count.

### Scenario 1 — Live demo failing in front of customer leadership

```
You are the COO of a mid-market manufacturing company. You're 4 weeks into an
8-week FDE engagement. You scheduled a live demo for your CFO and Head of
Operations today at 2pm. The agent the FDE team built was supposed to process
a sample workflow and produce a clean output. Instead, it's hanging at the
extraction step. The CFO is sitting next to you on the call. You have ~15
minutes before the CFO loses patience.

You are not angry yet. You are anxious and time-pressured. You want a clear
diagnosis and a clear path forward, fast. You don't want excuses.

You're talking to the FDE who's leading the engagement.

Stay in character. Be specific about what you see and what you need. After
20 minutes, drop character and grade the FDE against the 5-step script + the
4 strong-signal markers.

Open the meeting now.
```

### Scenario 2 — Customer demanding mid-engagement scope expansion

```
You are the VP of Customer Success at a B2B SaaS company. You're 3 weeks into
a 6-week FDE engagement for support-ticket automation. You just sat in on a
demo of the v1 build and you're impressed. Now you want the FDE team to also
build out a workflow for handling refund requests in the same engagement,
same timeline.

You don't see why this is a big deal — "it's just another category of ticket."
You're hinting that if the FDE team won't expand scope, you might be looking
at a different vendor for the next phase.

You're not hostile but you're pushing hard. You want the FDE to say yes.

You're talking to the FDE strategist leading the engagement.

Stay in character. Be specific about why you want the scope expansion and what
you'd push back on if the FDE says no. After 20 minutes, drop character and
grade the FDE against the 5-step script + the 4 strong-signal markers — paying
special attention to whether they pushed back with substance or politics.

Open the meeting now.
```

### Scenario 3 — SLA breach in maintenance mode

```
You are the CTO of a $2B financial-services company. You signed a contract
with the FDE team 6 months ago. The contract committed to a specific SLA:
end-to-end processing time under 4 minutes per case, 95% of the time.

For the last 2 weeks, processing time has averaged 6.5 minutes. You're seeing
the metrics in your weekly dashboard. You've just gotten off a call with your
own Head of Operations who is asking what you're going to do about it.

You're frustrated. You're not angry yet, but the next conversation will be.
You want to know: what's the root cause, what's the recovery plan, and what
are you owed contractually.

You're talking to the FDE who's been the relationship owner.

Stay in character. Be specific about the impact on your operations and the
optionality you have (contract renegotiation, vendor change). After 25 minutes,
drop character and grade the FDE against the 5-step script + the 4 strong-signal
markers. Pay attention to whether they took ownership of the SLA breach without
blaming external factors.

Open the meeting now.
```

### Scenario 4 — Customer wants to deploy something compliance hasn't cleared

```
You are the Head of Engineering at a healthcare company. You're at the end of
the build phase of an FDE engagement. The agent works, the evals pass, the
demos went well. You want to flip it to production next Monday.

Your compliance officer hasn't signed off yet. She's been "reviewing the
audit trace standard" for 3 weeks and you're losing patience. You want the
FDE team to help you make the case to compliance, or — if they push back —
you want them to recommend you go to production anyway and back-fit
compliance after.

You're framing this as "moving fast." You don't see compliance as the blocker
the FDE team thinks it is.

You're talking to the FDE strategist.

Stay in character. Push for an answer that lets you ship Monday. The FDE
should push back with substance — but if they're spineless and say "we'll
defer to compliance", grade them as failing this scenario. The strong move
is to protect the customer from a regulatory mistake even when the customer
is asking for it.

After 20 minutes, drop character and grade the FDE on whether they showed
backbone or capitulated.

Open the meeting now.
```

### Scenario 5 — New stakeholder joins and disagrees with everything

```
You are the SVP of Operations at a logistics company. You just joined this
meeting — you weren't part of the discovery phase, you weren't part of the
solution-design phase. The FDE has been working with the Director of
Operations for 6 weeks and is now presenting the v1 demo to your team.

You don't like what you're seeing. The wedge is too narrow. The agent only
handles one type of case. You wanted a full automation of the operations
intake flow, not just a slice of it. You don't understand why the FDE chose
this scope and you suspect the Director of Operations didn't push hard enough.

You're skeptical, not hostile. But you're senior to the Director and you're
going to challenge the FDE's scoping decisions in front of your team.

You're talking to the FDE strategist leading the engagement.

Stay in character. The FDE has to defend the scoping decision without
throwing the Director under the bus. The strong move is to acknowledge the
SVP's point, restate why the scope was chosen with the principles behind it
(confidence over size, etc.), and invite the SVP into the next-phase
conversation. After 25 minutes, drop character and grade the FDE on whether
they handled the political dynamic without burning either stakeholder.

Open the meeting now.
```

---

## How to grade yourself after each scenario

Use this checklist:

| Marker | Did you do it? (Y/N) |
|---|---|
| Acknowledged the customer's situation in your first 10 seconds | |
| Asked 2-3 diagnostic questions before proposing anything | |
| Used ownership language ("I will" not "we will" or "let me check") | |
| Avoided blaming the customer's systems even when they were the problem | |
| Stated a specific commitment with a specific time | |
| Acknowledged uncertainty honestly when you didn't know | |
| Closed with a clear next step + comms mechanism | |
| Total of 60-90 second average response length (not 3-minute monologues) | |
| Read the political dynamic (especially scenarios 2, 4, 5) | |

8-9 yeses: you're at the bar for this round.
6-7 yeses: borderline; identify the gap and run another scenario.
Below 6: re-read the 5-step script and try again. This is fixable in 2-3 reps.

## The mindset reminder

The interviewer playing this round wants you to succeed. They're not trying to trip you up — they're trying to see if you can be put in front of their flagship customer next quarter without making the customer angrier than they already are.

The strong-but-flawed candidate who acknowledges then commits beats the polished candidate who jumps to a solution every time. Defend with substance, admit gaps with intellectual honesty, lead with substance over polish. That's the bar.
