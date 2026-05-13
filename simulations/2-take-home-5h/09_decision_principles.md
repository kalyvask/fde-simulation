# 09 — Decision Principles for Helix

> Seven portable principles transferred from the  interview prep, applied to the Helix case. Use these in Hour 1 (wedge selection), Hour 5 (deck framing), and the 60-min Review (architecture defense). They are the difference between a competent build and a frontier-lab final-round defense.

## When to read this

Read this **before** Hour 1 of the take-home, and again **the day before** the Review. The principles are abstract enough to forget under time pressure; reading them twice fixes that.

---

## Principle 1 — Confidence of outcome over size of outcome

The biggest wedge is rarely the right wedge. The right wedge is the one you can ship with the highest confidence of clean outcome.

For Helix, the candidate-wedge spectrum looks like:

| Wedge | Size | Confidence of clean outcome |
|---|---|---|
| Automate the entire note end-to-end | Biggest | Low — too many points of failure |
| Citation-grounded earnings draft (Rachel still reviews) | Medium | High — narrow scope, deterministic guardrails |
| KPI quick-extract only | Smallest | Highest — but value too low to justify the engagement |

**The wedge isn't "what's biggest" — it's "what's biggest that I can ship cleanly."**

When the Review probes "why didn't you go bigger?", this is the answer. Not "we'll get there in v2" — that's reactive. The principled answer: "I optimize wedge selection on confidence of outcome, not size. The bigger wedges have lower confidence on the kill-criteria — hallucinated numbers — and v1 is where we earn the right to v2."

## Principle 2 — Outcome Risk Matrix (the  transfer)

Score each candidate wedge on two dimensions before you pick one:

| | Low-risk failure (reversible, caught early) | High-risk failure (irreversible, caught late) |
|---|---|---|
| **High value (saves >2h/note)** | **Ship as v1** | Ship with hard guardrails + senior veto |
| **Low value (saves <30min/note)** | De-prioritize | Avoid entirely |

Applied to Helix's plausible wedges:

| Wedge | Value | Risk | Quadrant | Decision |
|---|---|---|---|---|
| Citation-grounded earnings draft | High (saves 3+ hours/note) | Medium-low (failure visible, Verifier catches before PM) | High value / Low risk | **Ship as v1** |
| KPI quick-extract only | Low (saves 30 min, Rachel still drafts) | Low | Low value / Low risk | De-prioritize |
| Auto-tone-shift detection in isolation | Medium (saves QA time) | High (mis-tagged tone shift becomes a trading signal) | Medium value / High risk | **Defer to v1.5** with judge calibration |
| MD&A diff with prior quarter | Medium (analyst-level synthesis value) | Medium (false alarms create noise) | Medium / Medium | Defer to v1.5 |
| Position-sizing decision support | High in theory | Catastrophic (Chinese wall + Reg FD) | Out of scope, permanently |
| Auto-publish to PMS / trade tickets | High in theory | Catastrophic (one bug = trading loss + audit) | Out of scope, permanently |

What this matrix forces you to name (and what the interviewer will probe):
- **Failure visibility**: who sees it fail, how badly, how fast
- **Failure reversibility**: can we catch and retry, or is the damage done
- **Stated risk explicitly**: not "we'll handle risks", but "I scored this at high-risk-irreversible and that's why it's out of v1"

**The matrix is the artifact.** Bring a literal table like the one above into your deck (slide 1 supplement or slide 3 risk section). It signals senior-FDE thinking in 10 seconds.

## Principle 3 — Sequencing, not single-choice

Don't pick one wedge and treat the rest as "future work." **Sequence them.**

| Phase | Engagement weeks | Scope | Gate to next phase |
|---|---|---|---|
| **Phase 1** | Weeks 1-4 | Citation-grounded earnings draft, read-only, Rachel reviews 100%. Target: 30-min senior review/note. | Pass^k=5 on eval suite + Mei MNPI sign-off + Rachel signs off on 20 sample drafts |
| **Phase 2** | Weeks 5-12 | Add MD&A diff + tone-shift detection (calibrated against SubjECTive-QA labels). Target: 20-min senior review. | Adoption metric ≥70% (Rachel ships agent's draft without re-drafting) |
| **Phase 3** | Weeks 13+ | Expand coverage: more sectors, draft variants per recipient (CIO vs trader-desk). Target: 15-min review + 10x volume. | Cost-per-note <$X + zero MNPI incidents in prior 90 days |

What sequencing buys you:
- Frames the wedge as the start of a portfolio, not a one-off
- The "what's after v1?" probe gets a named answer with named gates
- Shows judgment under constraint — you protected the kill-criteria in v1 and earn capability in v2
- Senior FDE move: each phase has an explicit gate, not "we'll see how v1 goes"

The principle: **the wedge is the first node in a sequence, not the answer.**

## Principle 4 — Engagement gap as a parallel track

Most case studies optimize one thing — accuracy, containment, latency. Senior thinking names two parallel tracks.

**Track A — output quality** (the obvious one):
- Hallucination rate, citation precision, faithfulness scores, KPI extraction accuracy
- Easy to measure, sits in the eval suite

**Track B — adoption / engagement** (the silent killer):
- Are Rachel and David actually shipping the agent's draft, or re-drafting from scratch?
- Are analysts working around the agent (drafting in Word, ignoring the agent's output)?
- Is Carmen reading the agent's notes with the same trust as Rachel's?

An agent that hits 98% accuracy but 15% adoption is a failed engagement. The the prep material hammers this. So does OpenAI.

In your Helix deck and Review:
- Name the engagement metric explicitly: **"% of covered names where Rachel ships the agent's draft without re-drafting from scratch"**
- Target: 70% by end of Phase 2
- Sign-off criterion: not just Mei's compliance gate, but Rachel's "would put my name on it" gate (already in the brief — make it explicit as a metric)

The probe this defends against: "What's your adoption story? How do you know analysts won't just route around this?"

## Principle 5 — Principles before reactive answers

The Review will probe specific decisions ("why Sonnet for the drafter?"). The reactive answer walks through that one choice. The principled answer **names the criterion first**, then applies it.

| Reactive | Principled |
|---|---|
| "I picked Sonnet because the drafter needs to synthesize across the transcript and KPI extracts, and Haiku doesn't reliably handle the synthesis depth." | "I triage tier choices on two questions: (1) does the task require synthesis or extraction, and (2) what's the latency vs cost budget at this agent's volume? Applying that here, the drafter is synthesis-heavy and volume is ~80 notes/quarter — Sonnet wins on synthesis quality, and the volume doesn't make cost prohibitive." |
| "I picked deterministic Citation Verifier because LLMs hallucinate on numbers." | "I split deterministic vs LLM by failure-mode reversibility. Hallucinated numbers reaching a PM is irreversible; tone misread is reversible. Citation Verifier guards the irreversible failure, so it has to be deterministic. The Tone Supervisor can be LLM-as-judge with calibration because tone errors get caught in review." |
| "I made the MNPI Scrubber first because MNPI is the biggest risk." | "I sequenced the architecture by failure cost — the first agent should be the one whose failure costs the most. MNPI leak is fund-shutting; that's why the Scrubber fires before any LLM call. If it ever fires, no LLM call ever happens." |

What the principled answer buys you:
- Gives the interviewer 2 surfaces to probe (the principle AND the application)
- Shows you have a framework, not just opinions
- Generalizes to other architecture choices (the interviewer doesn't have to re-probe each one)

**Pre-rehearse 4-5 of these reframes** for your most load-bearing decisions before the Review. They are the highest-leverage prep you can do.

## Principle 6 — Read-only v1 is the senior move (defensively, not apologetically)

For Helix, every write capability is a v2 conversation:
- Draft to email: **NO** (deck push only)
- Auto-publish to PMS: **NO**
- Modify the watch list: **NO**
- Update compliance policy: **NO**
- Send to trading desk distribution list: **NO**

Read-only v1 caps the failure mode. The deck should call this out — defensively, not apologetically.

**Apologetic framing (weak)**: "We'd want to add write access in v2 once we have more confidence."

**Defensive framing (strong)**: "Write access in v1 means spending the first 4 weeks on permission architecture instead of the citation-grounded drafting. And the failure mode of a wrong write goes from 'wrong draft Rachel catches in 30 seconds' to 'wrong record in the PMS that triggers an audit.' Not worth the trade in v1. We earn write access by shipping read-only first."

The Review probe this defends against: "Why no write access? Aren't you under-scoping?"

## Principle 7 — Insight first, not activity (the deck + opening discipline)

In your deck and in the Review opening, lead with the **insight**, not the **activity**.

**Activity-first (weak)**:
> "We built a 7-agent workforce that processes earnings transcripts and generates analyst notes with citation grounding and an MNPI scrubber."

**Insight-first (strong)**:
> "The kill-criteria is hallucinated numbers reaching a PM. Every architectural choice in this build — the MNPI Scrubber as the first gate, the deterministic Citation Verifier, the read-only output, the senior-analyst veto in week 4 — is downstream of that single risk. Let me walk you through the wedge."

The insight-first version gives the interviewer the **frame** before the activity. They can then probe whether each choice actually serves the frame — which is a fair test and one you can defend.

Applies to:
- Slide 1 headline (insight, not feature list)
- Video opening (0:00-0:30)
- Review opening (the 90-second restatement)
- The first sentence of every Review answer when probed on architecture

## Principle 8 — The 3-lens scaffold ( Agent Design transfer)

The Customer | Product | Technical scaffold from the the agent design whiteboarding round applies directly to Helix as the structuring backbone for: (a) your Hour 1 wedge audit, (b) Slide 1's wedge framing, (c) the Review opening 90-second restatement, (d) anchoring architecture defense under pushback.

**Don't duplicate the content here — see `10_3_lens_applied_to_helix.md` for the full filled-in table** with Rachel's emotional state, the in-scope/out-of-scope split, trust levels, the one specific integration risk (MNPI watch-list drift), and the validation plan.

Key sub-rules from the 3-lens scaffold that matter for Helix:

| Sub-rule | Helix application |
|---|---|
| Name the emotional state | Rachel is exhausted + anxious. Drives every architecture decision. Different design from frustrated / time-pressured / curious customer types. |
| Out-of-scope = in-scope | M&A out, position-sizing out, auto-publish out, multi-quarter out — each on Slide 1 with equal weight to in-scope |
| Name the metric tension | Speed vs zero-MNPI streak. Protect the streak. |
| One specific risk | MNPI watch-list drift + per-invocation pull. Beats "we handle MNPI carefully." |
| Never jump columns | When probed on Technical first, park it and close Customer/Product first |

## How to use this file across the engagement

| Phase | Principles to apply |
|---|---|
| **Hour 1 — Discovery + wedge** | Principle 1 (confidence over size), Principle 2 (Outcome Risk Matrix table), Principle 4 (engagement gap metric), **Principle 8 (3-lens audit — file `10_3_lens_applied_to_helix.md`)** |
| **Hour 2 — Architecture sketch** | Principle 6 (read-only defense baked into architecture diagram) |
| **Hour 5 — Deck** | Principle 7 (slide 1 insight-first), **Principle 8 (slide 1 wedge paragraph = 3-lens synthesis)**, Principle 3 (slide 4 sequencing), Principle 4 (slide 3 dual-track metrics) |
| **Hour 5 — Video** | Principle 7 (opening 30 seconds) |
| **Review prep** | Principle 5 (rehearse 4-5 reframes), Principle 6 (read-only defense), Principle 3 (phase sequencing answer), **Principle 8 (3-lens opening + architecture-defense anchoring)** |

## Quick reference card (print for the Review)

```
WEDGE SELECTION (Hour 1):
  Outcome Risk Matrix: score Value × Risk in a 2x2
  Confidence over size — narrower wedge wins if outcome certainty is higher
  3-lens audit: fill Customer | Product | Technical for your wedge
  Bring the literal matrix table into slide 1 or 3

DECK FRAMING (Hour 5):
  Slide 1: lead with insight (kill-criteria), then 3-lens wedge synthesis
  Slide 3: name two metric tracks — output quality + adoption/engagement
  Slide 4: Phase 1 → 2 → 3 sequencing with named gates between phases

REVIEW DEFENSE (60-min):
  Open with the 3-lens restatement (~90 sec)
  Every architectural choice — name the principle + which lens it serves
  Read-only v1: defensive framing, not apologetic
  Adoption (Track B) named explicitly as parallel to quality (Track A)
  Pre-rehearse 4-5 Principle 5 reframes for load-bearing decisions

THE 6 SUB-RULES (from the 3-lens scaffold):
  Name the emotional state (Rachel: exhausted + anxious)
  Out-of-scope = in-scope (M&A, position-sizing, auto-publish, multi-quarter)
  Name the metric tension (speed vs zero-MNPI streak — protect streak)
  Read vs write distinguished (write = NONE v1)
  One specific risk, not generic (MNPI watch-list drift)
  Never jump columns under pressure — park and re-anchor

THE MINDSET:
  Strong-but-flawed > polished-mediocre.
  Defend with substance. Admit gaps with intellectual honesty.
  Lead with substance over polish.
```

## What NOT to do with these principles

- **Don't recite them verbatim** in the Review. Internalize them; the principle leads, the application follows.
- **Don't apply all seven to every decision** — that's over-engineering. Pick the 2-3 that fit the question.
- **Don't pretend you used the matrix retroactively** if you didn't. The interviewer can tell. If you didn't score wedges on Value × Risk in Hour 1, say so and demonstrate it on the spot when probed.

## The senior FDE mindset

You don't have to be perfect. Frontier labs reward strong-but-flawed candidates over polished mediocre ones. **Defend with substance, admit gaps with intellectual honesty, lead with substance over polish.** That's the bar.
