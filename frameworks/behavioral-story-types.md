# Behavioral Story Types — The 5 You Must Have

> Behavioral questions are not confined to a single "behavioral round" in FDE interviews. They're embedded throughout every technical round, every system design round, and the client simulation round. You don't get a section to prepare for; you get probed continuously. Means: you need polished stories ready that you can deploy in 30-90 seconds without thinking about structure.

## The underlying lens: the Trusted Advisor formula

Behavioral interviewers are grading one underlying question: *can we put you in front of our flagship customer next quarter and trust you'll preserve the relationship?* The framework they (often implicitly) score against is Maister's:

```
Trust = (Credibility + Reliability + Intimacy) / Self-Orientation
```

See [`consulting-frameworks.md`](consulting-frameworks.md) for the full breakdown. The 5 story types below each map to one or more of these dimensions:

| Story type | What dimension it primarily signals |
|---|---|
| 1. Live production fix you owned | Reliability + Credibility |
| 2. Pushing back on customer request | Low Self-Orientation (you put their long-term interest over short-term comfort) |
| 3. Deployment failure with public consequences | Intimacy + Reliability (you handled vulnerability transparently) |
| 4. Explaining technical limit to non-technical stakeholder | Credibility + Intimacy |
| 5. Decision with incomplete information | Credibility (calibrated honesty under ambiguity) |

When polishing each story below, ask: *which trust dimension am I demonstrating? Is it visible to the interviewer?*

## The 5 required stories

Public sources consistently flag these 5 story types as the ones FDE interviewers ask for across rounds. Have one polished, specific, outcome-tied story for each.

| # | Story type | Common question shapes |
|---|---|---|
| 1 | Live production fix you owned | "Tell me about a deployment failure and how you handled it." / "Walk me through the worst on-call incident you led." |
| 2 | Pushing back on a customer request | "Tell me about a time you said no to a customer." / "Walk me through a scope dispute you navigated." |
| 3 | Deployment failure with public consequences | "When did your work cause a customer-visible problem? How did you handle it?" |
| 4 | Explaining a technical limit to a non-technical stakeholder | "Tell me about explaining a complex technical decision to a non-engineer." / "When did you have to translate engineering tradeoffs to a CEO/CFO?" |
| 5 | Making a decision with incomplete information | "Tell me about a high-stakes decision you made with incomplete data." / "When did you have to commit to a path under ambiguity?" |

## The story template (use this exact structure)

Length target: 90-120 seconds. Not 3 minutes. Not 30 seconds.

```
1. THE PRINCIPLE (10 sec)
   One sentence: the portable lesson you took from this experience.

2. THE SITUATION (15 sec)
   Specific company / team / time / role. No background fluff.

3. THE COMPLICATION (15 sec)
   What made it hard. Constraints. Stakes. Why a generic answer wouldn't work.

4. WHAT YOU DID + THE TRADEOFF (45 sec)
   Specific actions in first person. Named tradeoff you made. Why.

5. THE OUTCOME (10 sec)
   Specific number if you have one. Qualitative if not.

6. THE PORTABLE LESSON (5 sec)
   The principle reinforced. Same one sentence as Step 1.
```

The bookending with the principle in step 1 and step 6 is intentional. The interviewer remembers what you say first and last; the middle is the supporting evidence.

## Story type 1 — Live production fix you owned

### The probe (typical phrasing)

- "Tell me about a deployment failure you handled."
- "Walk me through the worst production incident you led."
- "A deployment fails at 2 AM. What happens?"

### What the interviewer is testing

- **Radical ownership**: did you fix it yourself, or did you file a ticket?
- **Diagnostic discipline**: did you find root cause or just patch?
- **Communication**: did the customer know what was happening?
- **Prevention**: did you fix the systemic gap, not just the incident?

### Template — fill this in for one specific story

```
PRINCIPLE: "Production incidents are 30% technical fix and 70% communication."

SITUATION: At [company], I was the on-call FDE for [customer]. [Time of day],
the [system] failed in production.

COMPLICATION: [Specific failure mode]. [Customer impact, e.g., 50K daily users
unable to complete checkout]. [Specific deadline pressure, e.g., customer's
CEO board meeting in 6 hours].

ACTIONS + TRADEOFF: I diagnosed root cause as [specific cause]. The tradeoff
was [quick patch vs. proper fix]. I chose [the patch] and immediately sent a
written update to [customer stakeholders] with the timeline and follow-up plan.
By [time], I had the proper fix shipped and a written post-mortem to the
customer's team.

OUTCOME: [Specific recovery time]. [Customer-stated outcome — "they expanded
the contract" / "they referred us to two other customers" / etc.]

LESSON: "Production incidents are 30% technical fix and 70% communication.
The customer doesn't care about the root cause analysis — they care about
when it's fixed and what we learned. Lead with the timeline."
```

### Anti-patterns

- "We rolled back the deploy" (no ownership signal — who is "we"?)
- "I filed a P0 ticket and the SRE team handled it" (you didn't handle it)
- "We have post-mortems for this" (process answer, not story answer)
- No customer-facing communication described (FDE-specific signal: did the customer know?)

## Story type 2 — Pushing back on a customer request

### The probe

- "Tell me about a time you said no to a customer."
- "Walk me through a scope dispute."
- "When did you push back on a high-level stakeholder?"

### What the interviewer is testing

- **Backbone**: can you push back, or do you capitulate?
- **Substance vs politics**: did you push back with data, alternatives, named tradeoffs — or just "our team can't"?
- **Relationship preservation**: did the customer stay on the engagement after the no?

### Template

```
PRINCIPLE: "Pushing back well preserves the relationship; capitulating destroys
it 3 weeks later when the broken commitment ships."

SITUATION: At [company], [customer] asked for [specific request] mid-engagement.

COMPLICATION: The request was [why it was a problem — scope creep / compliance
risk / engineering capacity / technical infeasibility]. Saying yes would have
caused [specific downstream consequence].

ACTIONS + TRADEOFF: I pushed back in writing with: (1) the specific reason
the request was a problem, (2) what the actual underlying need seemed to be,
(3) two alternative paths that addressed the underlying need without the
problem. The tradeoff: short-term customer disappointment vs. medium-term
engagement success.

OUTCOME: Customer agreed to [alternative path]. Result: [specific outcome —
they renewed, they referred, the engagement shipped clean].

LESSON: "The customer is paying for your judgment, not your compliance. The
strongest customer relationships are built on pushback with substance, not
on saying yes to everything."
```

### Anti-patterns

- "I told them no and they understood" (no substance, no specifics)
- "We had a tough conversation" (no detail on what made it tough)
- The story ends with the no, not with the resolution and outcome
- You pushed back on a low-stakes ask, not a high-stakes one

## Story type 3 — Deployment failure with public consequences

### The probe

- "When did your work cause a customer-visible problem?"
- "Tell me about a time something you shipped failed in front of the customer."
- "Walk me through a failure that hurt the customer relationship."

### What the interviewer is testing

- **Calibrated honesty**: do you own the failure or deflect?
- **Recovery quality**: did you turn the failure into a strengthened relationship?
- **Systemic learning**: did you fix the class of problem, not just the instance?

### Template

```
PRINCIPLE: "The strongest customer relationships I've ever had came after I
failed publicly and recovered transparently."

SITUATION: At [company], I shipped [specific thing] for [customer]. It failed
in [specific way] visible to [customer stakeholder or end-users].

COMPLICATION: [Why it was bad — customer's own customer was affected, exec
was watching, demo was happening, etc.]. The customer was [specific
emotional state — angry, anxious, ready to cancel].

ACTIONS + TRADEOFF: I owned the failure in writing immediately, no hedging.
Tradeoff: short-term embarrassment vs. long-term trust. I [specific recovery
action] within [specific time]. I shipped a post-mortem to the customer's
team and proposed [specific systemic fix].

OUTCOME: Customer [specific positive outcome that came AFTER the failure —
they renewed, they expanded, they became a reference customer]. The systemic
fix prevented [specific category of future failures].

LESSON: "Failure isn't the relationship killer. Hidden failure or blamed
failure is the relationship killer. Owned and recovered failure is sometimes
the strongest relationship-builder there is."
```

### Anti-patterns

- The failure was small / low-stakes (interviewer can tell)
- You're the hero who saved the day with no fault (low credibility)
- No transparent customer comms described
- No systemic fix — just an incident fix

## Story type 4 — Explaining a technical limit to a non-technical stakeholder

### The probe

- "Tell me about explaining a complex technical decision to a non-engineer."
- "When did you have to translate engineering tradeoffs to a senior business leader?"
- "How do you explain LLM limitations to a customer who thinks they're magic?"

### What the interviewer is testing

- **Translation skill**: can you make technical concepts accessible without being condescending?
- **Customer-first framing**: do you anchor on business outcomes or technical specs?
- **Honesty under pressure**: do you over-promise to a non-technical audience?

### Template

```
PRINCIPLE: "Translating technical to business is about anchoring on the
customer's outcome, not simplifying the technical."

SITUATION: At [company], I had to explain [specific technical concept — LLM
hallucination risk, eval gap, integration constraint] to [specific
stakeholder — CFO, board member, customer's CEO].

COMPLICATION: They had [specific expectation/misconception]. The wrong
explanation would have [specific consequence — over-commitment, missed
expectation, lost trust].

ACTIONS + TRADEOFF: I explained it by [specific framing — analogy to their
business, specific scenario walkthrough, named tradeoff in business terms].
Tradeoff: nuance lost vs. accurate understanding. I chose accurate
understanding even though the answer was less impressive than the magic
they wanted.

OUTCOME: They [specific outcome — re-scoped expectations, asked the right
follow-up question, supported the engagement instead of canceling].

LESSON: "Non-technical stakeholders don't want simpler explanations — they
want their question answered in their domain language. Translate the
business consequence, not the technical detail."
```

### Anti-patterns

- "I used an analogy" without saying what the analogy was
- You sound condescending in the retelling
- You over-promised in the explanation (interviewer can spot this)

## Story type 5 — Decision with incomplete information

### The probe

- "Tell me about a high-stakes decision you made with incomplete data."
- "When did you commit to a path under ambiguity?"
- "Walk me through a 'we don't have enough info but we have to choose' moment."

### What the interviewer is testing

- **Decisiveness**: can you commit when committing is hard?
- **Calibration**: did you name what you didn't know?
- **Bias toward action**: did you decide, or did you study indefinitely?

### Template

```
PRINCIPLE: "In ambiguity, the cost of waiting for full information usually
exceeds the cost of being wrong on a smaller decision earlier."

SITUATION: At [company], I had to decide on [specific decision] by
[specific deadline]. I had [partial information — A, B, C]. I didn't have
[critical missing information — X, Y].

COMPLICATION: Waiting for X and Y would have meant [specific downstream
cost — missing the launch window, losing the customer, slipping a
contractual SLA]. Acting without them risked [specific downside].

ACTIONS + TRADEOFF: I decided to [specific decision] based on [reasoning
that combined what I knew with what I assumed]. I named the assumptions
in writing to [specific stakeholder] and committed to [a recovery path
if the assumptions turned out wrong]. Tradeoff: speed vs. certainty.
I chose speed because [specific reason this case demanded it].

OUTCOME: [Specific outcome — the decision was correct / partially correct /
wrong but recoverable]. [What you learned about the calibration].

LESSON: "Being wrong fast and recovering is usually cheaper than being
right slow. The discipline is naming what you're guessing on, so the
recovery is bounded."
```

### Anti-patterns

- The decision wasn't actually high-stakes (interviewer can tell)
- You hedged the decision so much it wasn't actually a decision
- You don't name what you didn't know (signals false confidence)

## How to prepare your 5 stories

### Step 1 — Extract candidates from your career

For each story type, write 1-3 candidate stories from your real experience. Don't worry about format yet — just dump.

### Step 2 — Pick the best one per type

Criteria:
- Specific (named time / customer / number)
- High-stakes (the interviewer can feel why it mattered)
- Recent (last 5 years if possible)
- You were the protagonist (not a teammate)

### Step 3 — Fill the template

For each chosen story, fill out all 6 sections of the template above. Write it out. Don't trust yourself to wing it.

### Step 4 — Time yourself

Read each story out loud. Time it. Cut until it's 90-120 seconds. If it's longer, the interviewer will lose interest. If shorter, you don't have enough specifics.

### Step 5 — Practice the principle bookends

The first sentence (principle) and last sentence (lesson) are the ones the interviewer remembers. Make them identical or near-identical. This is the single move that turns "memorable story" into "portable framework."

## The meta-pattern

The candidates who land FDE offers don't have 5 great stories — they have 5 stories with 5 portable principles. The principle is the asset. The story is the evidence for the principle.

When you're deep in your interview prep and you've stopped getting better, the next move is: extract another principle from a story you've already prepped. Two principles per story × 5 stories = 10 principles. That's enough material for any FDE behavioral probe.

## Quick reference

```
THE 5 STORIES YOU NEED:

1. LIVE PRODUCTION FIX
   - Specific incident, specific recovery time, customer-facing comms
2. PUSHING BACK ON CUSTOMER REQUEST
   - Specific ask, specific reason, specific alternative, specific outcome
3. DEPLOYMENT FAILURE WITH PUBLIC CONSEQUENCES
   - Owned the failure, transparent comms, systemic fix
4. EXPLAINING TECHNICAL LIMIT TO NON-TECHNICAL STAKEHOLDER
   - Specific concept, specific stakeholder, specific framing
5. DECISION WITH INCOMPLETE INFORMATION
   - Named what was unknown, committed anyway, named the recovery path

STORY TEMPLATE (90-120 sec each):
  Principle (10s) → Situation (15s) → Complication (15s) →
  Actions + Tradeoff (45s) → Outcome (10s) → Lesson (5s)

THE BOOKEND:
  Open with the principle. Close with the same principle.
  This is what makes the story portable.
```
