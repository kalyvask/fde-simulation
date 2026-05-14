# Consulting & Strategy Frameworks

> 8 frameworks an FDE inherits from the consulting + AI-PM worlds. The first 7 came from the consulting tradition (originally surfaced from Palantir's "Delta" role definition + the broader management-consulting canon). The 8th (DASME) is the AI-PM-specific alternative to C.A.S.E. These complement the agent-design frameworks (3-lens, ORM, 4-dimensional testing) by giving you the customer-relationship + stakeholder-management muscle to deploy them.

## When to use this file

The other frameworks in this folder tell you how to design the agent. These tell you how to navigate the customer engagement around the agent. Both matter. Most candidates over-prepare on the former and under-prepare on the latter.

---

## 1. The Trusted Advisor formula

From David Maister's *The Trusted Advisor* (the canonical text on consultative client relationships).

```
Trust = (Credibility + Reliability + Intimacy) / Self-Orientation
```

| Element | What it means | How to demonstrate it in an FDE engagement |
|---|---|---|
| **Credibility** | The customer believes you know what you're talking about | Specific technical claims with named tradeoffs; admit gaps with calibration |
| **Reliability** | The customer believes you do what you say | Hit every commitment you make. If you say "by end of day", be done by end of day. |
| **Intimacy** | The customer feels safe being vulnerable with you | Treat their messy reality as normal. Don't react with disgust to shadow IT, brittle code, or missing data. |
| **Self-Orientation** | The DENOMINATOR. How much you're optimizing for your own outcome vs. theirs | This is the multiplier that destroys trust. Any moment where you visibly prioritize your billable hours, your demo, your timeline, your career — trust collapses. |

### Why it's a fraction, not a sum

You can have perfect Credibility + Reliability + Intimacy and still be untrusted if your Self-Orientation is high. A senior consultant with deep expertise who visibly cares more about closing the contract than solving the problem is untrusted. An earnest junior who admits not knowing but consistently puts the customer's interest first is trusted.

### How to apply in the interview

When asked "tell me about a time you built trust with a customer", structure the answer around the four variables:
- Specific Credibility move (technical decision they couldn't have made themselves)
- Specific Reliability move (commitment kept that they weren't expecting)
- Specific Intimacy move (vulnerable moment from their side that you absorbed without judgment)
- Specific Low-Self-Orientation move (something you did that wasn't in your interest)

The interviewer will recognize the formula even if they don't name it. It signals you've thought about this dimension explicitly.

---

## 2. The Delta Concept

Palantir's original framing of the FDE role: there's the product (what the platform does out of the box) and there's the customer's need (what they actually need to solve their problem). The gap between them is **the Delta**. The FDE's job is to bridge that gap with engineered solutions, not to ask the product team to build features for one customer.

```
The Delta = (What the customer needs) - (What the product does out of the box)
```

### Why Delta thinking matters

Most engineering candidates default to "the platform should support this." Senior FDEs default to "the platform supports this enough; here's the glue that bridges the gap for this customer." The Delta is the FDE's value-add.

### How to articulate the Delta in an interview

After you've named your wedge, name the Delta:

> "The customer needs [specific outcome]. The platform provides [specific capability]. The Delta is [specific gap]. The FDE work is to bridge that Delta with [specific engineering — usually 2-5 agents, custom integration, customer-specific eval suite]. We're not asking the platform team to add a feature; we're building the bridge."

### The Delta vs the wedge — they're not the same

- **The wedge** (our existing framework): the narrow first workflow you'd automate
- **The Delta**: the engineered gap between platform and customer need

The wedge selects what to build. The Delta names what's missing in the platform that you have to build yourself. Both go in your Solution Strategy answer.

### Anti-pattern

If your proposed solution is "add this feature to the platform", you've failed Delta thinking. The interviewer wants to hear "here's what I'd build on top of the platform, for this customer." Platform feature requests come from FDE field-back-to-product memos, not from in-engagement solutions.

---

## 3. The Three Whys diagnostic

Three discovery questions that surface the non-obvious. Ask all three in week 1.

### Why #1 — Where's the System of Record?

The "system of record" (SoR) is the authoritative source for the data you'll work with. The non-obvious answer is often:
- It's not the official system the IT team named
- It's a shadow Excel spreadsheet maintained by one person
- It's spread across three systems with reconciliation problems
- Nobody has clearly defined which system wins on conflict

**The diagnostic question**: "If two systems disagree on the data, which one is right?"

If the customer can't answer that confidently in 30 seconds, you've found a major scope risk. Document it and surface it in the field memo.

### Why #2 — What's the Cost of Inaction?

Cost-of-Inaction (CoI) is the financial argument for the engagement. If the customer doesn't build this thing, what does it cost them in 12 months?

**The diagnostic question**: "If we walked away today, what's the cost of this problem persisting for another year?"

Concrete CoI examples:
- "We lose 2 analysts per year to burnout. Replacement cost = $500K each. Year-1 cost of inaction = $1M."
- "We pay $40K/month for a manual BPO that we'd cancel after automation. Year-1 CoI = $480K."
- "Compliance audit penalty risk = 1% × $10M = $100K expected value."

The number gives the customer a way to defend the engagement budget to their board. It also gives YOU the upper bound on what they should pay you. Senior FDE move: name the CoI in week 1 even if the customer didn't.

### Why #3 — Who Owns Day 2?

"Day 2" is the operational period after you (the FDE) leave. The engagement is doomed if nobody owns it post-handoff.

**The diagnostic question**: "Who runs this system 90 days after I leave? Specifically — named person, named team, named cadence."

If nobody is named, the answer is "we'll figure it out" — which means "it'll be orphaned." Surface this in the field memo with a recommended ownership model. Some customers will hire someone to fill the role; others will assign to an existing team. Either is fine. No-named-owner is not fine.

### How to deploy the Three Whys

Ask all three in your first 3 stakeholder interviews. The answers reveal more about the engagement than 90% of standard discovery questions. Add the answers to the discovery memo, even if (especially if) the customer hadn't thought about them before.

---

## 4. Cost-of-Inaction as complement to the Outcome Risk Matrix

The [Outcome Risk Matrix](outcome-risk-matrix.md) frames wedge selection on value × risk-of-irreversible-failure. **Cost-of-Inaction is the complementary lens**: the cost of NOT doing the wedge at all.

### When CoI matters more than ORM

- When the customer is skeptical the engagement is worth it (CoI defends the budget)
- When you need to argue for sequencing (Phase 1 CoI < Phase 2 CoI; therefore Phase 1 is the right starting wedge even if its absolute value is lower)
- When the customer has alternative vendors (CoI vs them: what does it cost to wait while we onboard with a different vendor?)

### CoI in the wedge selection conversation

After you've scored candidate wedges on Value × Risk, add a third column: **CoI per quarter the wedge stays not-built**.

| Wedge | Value (savings if built) | Risk | CoI (annual cost if not built) | Verdict |
|---|---|---|---|---|
| Wedge A (HITL-approved drafter) | $500K/yr | Low | $1.2M/yr (2 senior analysts quit + alpha leak) | Ship as v1 |
| Wedge B (auto-publish) | $1.5M/yr | High | Same as A (we're already in v1) | Defer to v2 |
| Wedge C (different workflow) | $200K/yr | Low | $50K/yr | De-prioritize |

CoI makes the wedge comparison fair across different value bands.

---

## 5. The Quick Win Milestone (Week 2)

A specific operational discipline: by end of week 2 of an FDE engagement, deliver a small visible proof-of-value that demonstrates the agent works on one realistic case.

### Why Week 2 specifically

- Week 1 is discovery; nothing is visible to the customer yet
- Week 2 ends with "is this engagement going to work?" — the customer is forming an opinion
- A working end-to-end demo on one synthetic case (with citation chain, audit trace, all the right shapes) tells the customer "yes, this is real"
- A 4-week timeline with no visible output until week 4 is the recipe for an engagement death-spiral

### What counts as a Quick Win

- One synthetic case running through the full agent workforce, end-to-end
- Citation chain visible to the customer
- Audit trace examiner-readable
- Honest framing: "this is one case, not yet calibrated against your real data, but the architecture works"

### What does NOT count

- A slide deck about what you'll build (every customer has seen this; it's the opposite of a Quick Win)
- A working prototype on YOUR test data without their context
- A demo of someone else's reference architecture

### How to mention in an interview

When asked about the 4-week plan, name the Quick Win explicitly:

> "By end of week 2 I'd ship a Quick Win: one synthetic case running through the full workforce, end-to-end, with the citation chain and audit trace visible. The point isn't perfection — it's that the customer sees a working architecture by week 2, not by week 4. Engagements where the customer doesn't see anything visible until late are the ones that die."

This signals operational maturity. Most candidates don't name week-2 deliverables specifically.

---

## 6. Shadow IT awareness

A specific discovery insight: the cleanest, most authoritative data at a customer often lives in **undocumented systems** — a senior analyst's local Excel sheet, a one-off Python script run quarterly, a "temporary" database from 2019 that became permanent.

### Why this matters

If you only ask IT for "the data", you get the IT-blessed system, which is often:
- Stale (last updated when IT got involved)
- Wrong (the analyst stopped trusting it and built their own)
- Missing the operational nuance (the Excel sheet has columns the database doesn't)

Senior FDE move: ask the operator, not just IT. The diagnostic question is:

> "Where do you actually look when you want to know X? Not the official system — the one you actually trust."

The answer is often shadow IT. Document it. Treat it as a real data source even when IT is uncomfortable. Then propose a path to bring it into compliance / governance over the course of the engagement.

### What this signals in an interview

When asked about discovery, mentioning shadow IT awareness signals you've actually done customer-embedded work. The candidates who haven't will name systems, integrations, and databases. The candidates who have will name "the Excel sheet Maria maintains" or "the SQL script Bob runs every quarter."

---

## 7. The C.A.S.E. Framework — meta-structure for the interview answer

A 4-step structure for answering any deployment-scenario or case-study question. Maps to the engagement lifecycle. Same logical shape as our Discovery → Solution → Risk structure, but compressed into an acronym.

| Letter | Step | What you do |
|---|---|---|
| **C** | **Clarify** | Ask 2-3 diagnostic questions before proposing anything. Restate the problem in one sentence. Get explicit on the constraints and the metric. |
| **A** | **Architect** | Sketch the solution at the right altitude. Name the wedge. Name the agent shapes. Name the integration tier. Don't go deeper than the question requires. |
| **S** | **Solve (the Delta)** | Specifically address what the customer needs that the platform doesn't do. This is where the FDE adds value vs a generalist consultant. |
| **E** | **Evaluate** | Name the testing framework, the sign-off criteria, the production observability plan. Close with "how would we know this is working." |

### How to deploy

In any case-study question, the C.A.S.E. acronym gives you a 4-step structure you can deploy without having to remember which framework to use. Each letter maps to a part of our existing frameworks:

- C → 4-source convergence + restate
- A → 3-lens scaffold + workflow decomposition + agent shapes catalog
- S → Delta articulation + integration pattern + read/write split
- E → 4-dimensional testing + 3 sign-off criteria

It's not a NEW framework — it's a meta-structure that orders the existing ones for a time-pressured interview answer.

### Anti-pattern

Don't use C.A.S.E. as a literal recitation. ("Step 1: Clarify. Step 2: Architect.") That reads as memorized. Use it as the silent structure you're following while you speak conversationally.

---

## 8. The DASME framework — AI-PM-specific alternative to C.A.S.E.

A 5-step structure specifically tuned for AI product sense / AI system design interviews. More AI-specific than C.A.S.E.; use when the question explicitly tests AI-product judgment (e.g., "design a churn-reduction agent", "10x Claude Code WAU", "design content-safety classification for a social platform").

| Letter | Step | What you do |
|---|---|---|
| **D** | **Define scope** | Clarify the goal, the user, the constraint set, the metric you'd commit to. Same as Clarify in C.A.S.E. but more emphasis on naming the AI-specific success metric early (pass^k, recall@X precision, latency P95) |
| **A** | **Architect the agents** | Sketch the system. Multi-agent if appropriate. Name which agents are LLM-based vs deterministic. Specify the orchestration pattern. |
| **S** | **Specify data and models** | Name the model tier (Haiku/Sonnet/Opus/GPT-4o-mini/GPT-4o), the data sources, the training/eval split. Tag model-layer vs application-layer for each proposed solution (see [`model-vs-application-layer.md`](model-vs-application-layer.md)). |
| **M** | **Map metrics** | 3-level metrics framework (technical / UX / business) with explicit tension named. Eval composition: weighted, pass^k, adversarial. |
| **E** | **Edge cases + scale** | Adversarial attacks, drift, multi-region, multi-tenant variance, 10x scale bottleneck. Surface failure modes proactively. |

### C.A.S.E. vs DASME — when to use which

| Use C.A.S.E. when | Use DASME when |
|---|---|
| The question is shaped like a customer engagement ("walk me through how you'd approach this customer") | The question is shaped like a product/system design ("design X feature for Y product") |
| You're in an FDE / Solutions Architect interview | You're in an AI PM / AI Product Sense interview |
| The interviewer expects you to lead with stakeholders + scope | The interviewer expects you to lead with data flows + model trade-offs |
| The customer/Delta framing matters | The system architecture framing matters |

**For frontier-lab FDE interviews, C.A.S.E. is the default; DASME is the backup when the question is more product-design-shaped than engagement-shaped.** For AI PM interviews (OpenAI Deployed PM, Meta "Product Sense with AI"), DASME is the default.

### Worked example: DASME on "design a content-safety classifier for a social platform"

**D — Define scope (1 min)**: Goal is to detect harmful content (hate speech, harassment, self-harm). Users are creators (don't want false positives suppressing them) and advertisers (don't want brand safety incidents). Metric: harmful-content exposure rate (the north star); supplementary: creator satisfaction, advertiser brand-safety score, regulatory-compliance incidents per quarter.

**A — Architect the agents (5 min)**: 3-tier system. Tier 1: Fast classifier (small specialized model, runs on every post, ~10ms). Tier 2: Review agent (LLM, runs on borderline cases from Tier 1, ~2s). Tier 3: Human moderator (runs on Tier 2 escalations + adversarial / novel patterns). Plus a feedback loop: human flags become Tier 1 training data on a weekly cadence.

**S — Specify data + models (4 min)**:
- Tier 1 Fast classifier: distilled small model, application-layer fine-tuning on labeled posts, retrained weekly
- Tier 2 Review agent: LLM-as-judge (Sonnet-equivalent), no fine-tuning in v1
- Tier 3 Human moderator: existing team, augmented with new-pattern detection
- Training data: 10K seed labels + weekly human feedback loop = 50K+ labels by year 1
- Model-layer work: Tier 1 retraining cadence; everything else is application-layer

**M — Map metrics (3 min)**:
- Technical: recall@95% precision, P95 latency under 10ms for Tier 1
- UX: creator satisfaction (false positive rate), human moderator time per case
- Business: harmful-content exposure rate (north star), advertiser brand-safety score, regulatory incidents
- TENSION: cranking recall to 99.9% spikes false positives, creators leave. Threshold is a product decision, not a model decision. Protect creator satisfaction floor.

**E — Edge cases + scale (3 min)**:
- Adversarial: users modify images with noise to fool classifiers. Mitigation: ensemble models; if they disagree, escalate to Review Agent.
- New patterns: novel hate symbol the classifier hasn't seen. Mitigation: human feedback loop with weekly retraining.
- Cultural context: benign in English, slur in another language. Mitigation: language-specific classifiers with region-aware thresholds.
- 10x scale (5B posts/day): bottleneck is Tier 1 GPU fleet. Horizontal scaling with sharding; pre-filter obvious-non-violations (high-trust accounts) to reduce classifier load 40-50%.

That's DASME in 16 minutes. C.A.S.E. would have taken the same time but spent more on customer / stakeholder framing — wrong shape for this question.

---

## How these 8 frameworks fit together

The agent-design frameworks (3-lens, ORM, 4-dim testing) tell you what to build. These tell you how to navigate the engagement:

```
DISCOVERY (week 1):
  - Trusted Advisor (build credibility / reliability / intimacy / low-self-orientation)
  - Three Whys diagnostic (SoR, CoI, Day 2)
  - Shadow IT awareness (ask the operator, not just IT)
  - 4-source convergence (Buyer / Brief / Industry / Operator)

SOLUTION DESIGN (week 2):
  - Delta articulation (what the platform doesn't do)
  - 3-lens scaffold (Customer / Product / Technical)
  - Outcome Risk Matrix + CoI lens (which wedge first)
  - Workflow decomposition + agent shapes
  - Quick Win shipped by end of week 2

BUILD + EVAL (weeks 3-4):
  - Agent shapes catalog + integration patterns
  - 4-dimensional testing (eval + pass^k + adversarial + observability)
  - 3 sign-off criteria with named owners

HANDOFF:
  - Day 2 ownership defined
  - Field memo to product team
  - Trusted Advisor relationship preserved

INTERVIEW META:
  - C.A.S.E. as the silent answer-structure
```

## Attribution

Items 1-2 (Trusted Advisor, Delta) trace to David Maister and Palantir's published role definition respectively. Items 3-7 are common patterns across the consulting and FDE communities, surfaced clearly in [Pierpaolo Ippolito's Awesome-FDE-Roadmap](https://github.com/pierpaolo28/Awesome-FDE-Roadmap) which is worth reading alongside this repo for the data-engineering and GCP-specific complement to our interview-methodology focus.
