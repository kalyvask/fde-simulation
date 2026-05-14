# Company Calibration — What Different Employers Care About

> The frameworks in this repo are generic on purpose. But each employer has distinctive signals they grade on. This file documents what's publicly known about the major FDE-style employers — based on their own published material, candidate write-ups, and recruiter explanations available in 2026. Use it to tune your prep without changing the underlying frameworks.

## The 4 main employer archetypes

| Archetype | Role names | What they distinctively grade on |
|---|---|---|
| **Major AI lab — research-first** | Solutions Architect, Applied AI Engineer | Customer-facing technical depth + values alignment + safety / responsible scaling thinking |
| **Major AI lab — product-first** | Forward Deployed Engineer, Deployed PM | Production agent building + customer presentation + eval-quality differentiation |
| **AI workforce platform** | AI Strategist, Forward Deployed Strategist, Agent Strategist | Discovery rigor + contract-SLA discipline + multi-tenant input variance handling |
| **Enterprise AI vendor** | Solutions Engineer, Customer Engineer | Sales-adjacent technical + customer success + named accounts |

Most candidates underprepare for the distinctive signal of their target employer. Generic FDE prep gets you 70% there; calibration gets you the last 30%.

## Archetype 1 — Major AI lab, research-first

### What they hire FDEs for

Embedded technical work with their largest enterprise customers, often on safety-critical or research-adjacent applications. The role sits between research and product; the FDE is the field intelligence for the model team.

### Process shape (public info)

- 30-day average loop
- 5-6 rounds: recruiter screen → take-home (often coding-in-Colab) → tech deep dive → coding → solution design → leadership / values
- The values round is real — it's not pro forma. Candidates get rejected at this round despite strong technical performance.

### Distinctive signals they grade on

1. **Safety / responsible-scaling thinking** — what you'd refuse to deploy, why; how you'd handle the customer asking for something unsafe; familiarity with their published frameworks (Constitutional AI, RSP)
2. **First-principles reasoning** — the take-home is "real engineering work" style, not LeetCode. Defend time/space complexity. Implement data structures from scratch after solving with a standard library.
3. **Prompt engineering as a tested skill** — unique among AI labs. Expect explicit eval of your prompt-engineering process, not just outputs.
4. **Cultural fit** — alignment with their stated values matters more than at most companies. Generic ambition won't pass. Read their values page and their CEO's recent essays before the interview.

### What to read before

- The lab's published values document
- Constitutional AI paper / responsible scaling policy / safety framework
- CEO essays from the last 6 months
- Their published technical reports on agent capabilities

### Compensation reference (mid-to-senior, 2026)

Public sources cite total comp packages stabilized at **$350K-$550K** for major-lab FDE-equivalent roles.

## Archetype 2 — Major AI lab, product-first

### What they hire FDEs for

Building production AI systems with flagship customers. Less safety-research framing, more "ship the thing that the customer can use in their daily workflow."

### Process shape (public info)

- 3-5 week loop
- Recruiter call (heavy on "why FDE specifically, not just why this company")
- Take-home: ~5 hours, build something with their API, **submit a recorded video walkthrough** (this is the unique signal)
- Onsite: 3-4 hours, three sessions
- Hiring manager round (60 min) heavily focused on customer-facing experience

### Distinctive signals they grade on

1. **The video walkthrough is THE differentiator.** "FDEs present to executives weekly." The video is a direct simulation. Show your face. Live demo, not screenshots. End with what's NOT in v1.
2. **"How do you know your AI system is actually working?"** — the eval-quality question is their headline differentiator. Hand-waving here is a rejection trigger. Have pass^k=5, weighted evals, adversarial sets, production observability ready.
3. **Production thinking, not prototype thinking** — error handling, graceful degradation, logging, retry patterns. Demo code with no logging is a tell.
4. **Customer empathy + AI-specific depth equally weighted** — coding ability alone doesn't get you offers.

### What to read before

- Their published interview guide (if available)
- Their flagship customer case studies
- Their API documentation top-to-bottom (you should be able to discuss specific endpoints)
- The OpenAI Charter (or equivalent) for the product-first labs

### Compensation reference

Similar $350K-$550K band as research-first labs.

## Archetype 3 — AI workforce platform

### What they hire FDEs / Strategists for

Customer-engagement-lifecycle ownership: discovery → solution design → testing → deployment → maintenance. The role is more PM-flavored than pure engineering. They contract on outcomes, so the strategist is responsible for delivering the contracted metrics.

### Process shape (public info)

- 20-30 day loop
- Recruiter call → case-study interview (60 min, structured around Discovery / Solution Strategy / Risk & Validation) → hiring manager → behavioral / leadership round
- Smaller companies do fewer rounds; bigger ones add a values round

### Distinctive signals they grade on

1. **Contract-SLA discipline** — these platforms contractually commit to outcomes. Discovery isn't learning the customer's KPIs; it's identifying the 1-3 metrics you'd commit to in the contract by week N.
2. **Deterministic vs LLM at the output schema level** — distinctive framing for input-analysis agents. The output schema is deterministic (downstream-system required); the LLM lives in the input parsing; HITL at the seam.
3. **The strategist-to-FDE handoff** — these companies often separate the strategist (discovery + scope) from the engineering team (build). You should name the handoff artifact (an "AI Logic Doc" or equivalent) and what's in it.
4. **Project length discipline** — typical engagements are 8-12 weeks. Discovery is week 1, build is weeks 2-3, hardening is week 4. Naming the cadence signals operational maturity.

### What to read before

- The company's published case studies (read 3-5)
- Their published methodology / customer-success blog
- Public job descriptions for both the Strategist and FDE titles (the split tells you who owns what)
- Their customers' industries — if they primarily serve manufacturing or retail or finance, your case will likely be in those domains

### Compensation reference

Variable. Public sources cite **$150K-$210K base for AI Strategist roles** at well-funded AI workforce platforms in 2026, with total comp meaningfully below the major-lab band.

## Archetype 4 — Enterprise AI vendor

### What they hire for

Customer-success technical work, often named accounts. The role sits between sales and engineering — you don't sell, but you're often in pre-sales technical validation and post-sales deployment.

### Process shape (public info)

- 2-3 week loop
- Recruiter → technical screen → customer scenario round → final round
- Less rigorous than major labs but more emphasis on customer-facing soft skills

### Distinctive signals they grade on

1. **Named-account ownership** — comfort with a customer relationship that lasts 12+ months
2. **Cross-functional muscle** — comfort working with sales, product, engineering, customer success simultaneously
3. **Pre-sales technical** — can you walk a prospect's CTO through your architecture in a way that closes deals?
4. **Customer story library** — they expect you to have references from prior named accounts

### What to read before

- Their customer logos
- Their G2 / Gartner reviews to understand customer pain points
- Their public partnership announcements

### Compensation reference

**$200K-$320K total comp** depending on the company's stage and named-account size.

## The Tier 1 / 2 / 3 landscape for AI Product Sense rounds

For AI PM roles specifically (not pure FDE), there's a related interview shape called "AI Product Sense" that's spreading across the industry. It tests whether you can think about AI products as systems — data flows, model trade-offs, agent architectures, failure modes — not just user personas and feature lists.

If you're interviewing for AI PM (not just FDE), you'll likely face this round. The interview shape varies by company:

| Tier | Companies | What it looks like |
|---|---|---|
| **Tier 1 — embedded in every round** | OpenAI, Anthropic, Google DeepMind | AI product sense is part of nearly every interview. Sample questions: "double ChatGPT image creation WAU with 3 engineers", "increase Claude Code WAU 10x". No dedicated round; AI fluency tested continuously. |
| **Tier 2 — named round added** | Meta (IC6+/M1/M2 in Central Products), Figma | Explicit "Product Sense with AI" or "AI Product Sense" round added to the loop. Often features a vibe-coding component where you prototype while the interviewer evaluates judgment. |
| **Tier 3 — woven into 1-2 rounds** | LinkedIn, Stripe, Uber, Netflix | Not a dedicated round. AI Product Sense embedded inside the regular product-sense round. The sneaky one — recruiter email won't mention "AI product sense" but the bar has moved. |

**What this means for your prep**: even at companies that don't list "AI Product Sense" as a round, **AI fluency is being evaluated inside the regular product-sense round**. If your recruiter doesn't mention it, prepare anyway.

The difference from FDE Recommendation interviews (our sim 3): AI Product Sense focuses on a single AI product / feature growth / design. FDE Recommendation focuses on customer-engagement scoping. Both share frameworks (3-lens, ORM, 4-dim testing) but the framing is different. See [`../simulations/3-recommendation-60min/`](../simulations/3-recommendation-60min/) for the FDE shape and [`consulting-frameworks.md`](consulting-frameworks.md#8-the-dasme-framework--ai-pm-specific-alternative-to-case) for the DASME framework specifically tuned to AI Product Sense.

### Compensation reference for AI PM / FDE roles at frontier labs (mid-2026)

Public Levels.fyi medians for PM roles at the major AI labs. AI PM roles tend to cluster at or above these medians.

| Company | Median total comp (PM) | Range |
|---|---|---|
| **OpenAI** | ~$860K | $300K (Manager) → $950K+ (Staff). Mostly PPU-driven equity. |
| **Meta** | ~$515K | $173K (L3) → $2.24M (Senior Director). L7 PMs at $987K median. |
| **Google** | ~$473K | $182K (APM1) → $2.45M (L9/L10). Group PM at $757K median. Public equity. |
| **Anthropic** | ~$468K | $468K-$651K range. Pre-IPO equity at $60B+ valuation (subject to repricing). |

These are PM medians, not specifically AI PM. AI PM roles cluster at or above these per recent coaching data. AI workforce platforms (Sierra-tier and below) operate on a lower curve, typically $200K-$350K total comp. Enterprise AI vendor Solutions Engineer / Customer Engineer roles: $200K-$320K.

**Negotiation anchor**: if you're at Tier 1 (OpenAI / Anthropic / DeepMind for an AI PM or FDE role), the upper end of the band is real for senior candidates with prior production-AI experience. Don't anchor too low.

## Cross-cutting calibration: small / medium / large

### Small company (< 100 people)

- The hiring manager interviews you and is your future boss
- Less structure, more "vibe check"
- The case study probably comes from a real customer they're working with right now
- You'll likely meet the CEO or a co-founder
- Calibrate: be specific about how you'd be a force-multiplier on a small team

### Medium company (100-500)

- More structured loop, multiple interviewers per round
- The case study is calibrated to test specific competencies
- Behavioral rounds are real — they're filtering for culture
- Calibrate: balance technical signal with cultural fit signal

### Large company (500+, especially major AI labs)

- Bar-raiser style — each interviewer has independent veto
- Values round is rigorous
- Compensation negotiation is tighter than at smaller companies (band-locked)
- Calibrate: lean into the technical + values signal; cultural mismatch will kill it

## What to do with this calibration

### Before the recruiter call

1. Identify which archetype your target employer falls into
2. Read the specific distinctive signals for that archetype
3. Audit your existing prep against those signals

### Before each round

- Tech deep dive: tune to archetype's tech depth (research-first = first principles; product-first = production patterns; AI workforce = discovery rigor)
- Behavioral: tune to archetype's cultural signal (research-first = safety thinking; product-first = customer empathy; AI workforce = SLA discipline)

### Before the values / culture round

- Read the company's published values
- Don't memorize them — internalize 2-3 that map to your real stories
- Have one specific example for each value you cite

## The non-obvious calibration: titles

A title named **"Forward Deployed Engineer"** at one company can be functionally identical to **"Solutions Architect"**, **"AI Strategist"**, **"Customer Engineer"**, or **"Deployed PM"** at another. Don't get hung up on titles. The work is the same: customer-embedded, deployment-focused, hybrid PM/engineer/strategist. If the job description includes any of:

- "Forward deployed"
- "Customer-embedded"
- "Solutions architect"
- "AI strategist"
- "Deployed PM" / "Deployed Engineer"
- "Applied AI" + customer-facing language

It's the same archetype. Prep applies.

## Quick reference

```
MAJOR AI LAB - RESEARCH-FIRST:
  Distinctive signal: safety / values / first-principles
  Comp band: $350K-$550K
  Unique: prompt engineering eval, values round can reject strong tech

MAJOR AI LAB - PRODUCT-FIRST:
  Distinctive signal: video walkthrough, eval quality
  Comp band: $350K-$550K
  Unique: take-home + video, "how do you know it works" question

AI WORKFORCE PLATFORM:
  Distinctive signal: contract-SLA, det-at-output-schema, AI Logic Doc handoff
  Comp band: $200K-$350K
  Unique: outcomes-contracted, 8-12 week engagements

ENTERPRISE AI VENDOR:
  Distinctive signal: named-account, pre-sales, cross-functional
  Comp band: $200K-$320K
  Unique: 12+ month customer relationships, partnership thinking

CROSS-CUTTING:
  Small co: hiring manager = future boss, real customer case
  Medium: structured loop, balance tech + cultural fit
  Large: bar-raiser, values round rigorous
```
