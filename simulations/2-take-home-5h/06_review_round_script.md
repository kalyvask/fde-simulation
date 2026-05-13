# 60-Minute Review Round — Helix Specific Script

> The 60-minute presentation round. The interviewer has watched your video, read your deck, and is now going to push on every architectural choice. You defend, revise, or absorb — whatever the substance demands.

## The structure

| Time | Phase | What you do |
|---|---|---|
| 0-5 min | Framing | Restate the case + your wedge in 90 seconds **using the 3-lens structure** (Customer → Product → Technical), then field the interviewer's framing questions |
| 5-20 min | Discovery + current state | Walk through the user journey, current process, where AI fits, political map |
| 20-40 min | Agent architecture | Defend the architecture, walk through the live demo, take pushback on tier choices and tradeoffs — **anchor every defense to which lens it serves** |
| 40-55 min | Risk + path to production | List risks, show eval, show observability, name sign-off criteria |
| 55-60 min | Your questions back | 2-3 sharp questions referencing the interviewer's public work |

## The opening 90-second restatement (Sierra 3-lens transfer)

Open the Review with the 3-lens framing. It primes the interviewer for every architectural choice you've made and tells them which lens to probe first:

> "Let me restate the wedge in 3 lenses.
>
> **Customer**: Rachel — senior TMT analyst, exhausted by the morning grind, anxious about a hallucinated number reaching a PM. The org has zero MNPI incidents in 3 years and two senior analysts quit in 2025 over the grind.
>
> **Product**: citation-grounded earnings draft + tone-shift detection in scope. M&A, position-sizing, and any write explicitly out. Trust levels are deterministic on the dangerous calls, ask-the-analyst on the soft calls, escalate on policy combinations. Metric tension is speed vs zero-MNPI streak — we protect the streak.
>
> **Technical**: read-only v1, with MNPI watch-list drift as the one specific risk — mitigated by per-invocation list pulls plus Mei-owned audit log. Validation via pass^k=5 + Mei, Rachel, Carmen sign-offs."

This is 75-90 seconds. It frames every architecture decision before the interviewer probes. See `10_3_lens_applied_to_helix.md` for the full table.

## Anchoring architecture defense to the lens it serves

When the interviewer probes a specific agent or choice, anchor the answer to which lens it serves:

| Probe | Anchor lens | Defense |
|---|---|---|
| "Why MNPI Scrubber first?" | Technical (the one specific risk) | "It serves the Technical lens — MNPI watch-list drift is the named risk. Scrubber fires before any LLM call. If MNPI is detected, no LLM call ever happens." |
| "Why Sonnet for the drafter?" | Product (trust level structure) | "Drafter is the 'ask-the-analyst' tier — Rachel edits but won't re-draft. Sonnet's synthesis quality at ~80 notes/quarter makes the cost delta immaterial." |
| "Why citation-grounded?" | Customer (Rachel's anxiety) | "Citation grounding eliminates Rachel's named anxiety — hallucinated numbers reaching a PM. The architecture has to make that failure mode impossible, not unlikely." |
| "Why no auto-publish?" | Technical (write access) | "Write access in v1 = wrong draft becomes wrong PMS record. Read-only keeps the failure mode at 'Rachel catches it in review' — recoverable." |

The pattern: every architectural choice maps to a specific cell in a specific lens. Shows you have a framework, not opinions.

## What the interviewer probably already knows

Coming in, the interviewer has:
- Watched your 5-min video
- Read your 4-slide deck
- Cloned your repo and looked at the structure (maybe ran the e2e)
- Read your eval results summary
- Formed 5-10 questions specifically targeting your architecture

They are NOT trying to trick you. They ARE trying to find the soft spots in your design. Your job is to acknowledge soft spots when they're real and defend with substance when they're not.

## Helix-specific probes you should rehearse defending

These are the questions an experienced FDE interviewer would likely throw at this case specifically:

### Framing phase probes (0-5 min)

- "What did you assume about Sarah that wasn't in the prompt?"
- "What's the difference between Sarah's kill-criteria and David's day-to-day pain?"
- "Why did you pick this slice and not auto-generating the whole note?"
- "What's the 90-day-after question Anil-equivalent asked you?" (testing whether you thought about handoff)

### Discovery probes (5-20 min)

- "Walk me through Rachel. What 3 questions would you ask her in your first 30 minutes?"
- "Mei is default-no. What's your disarmament script?"
- "Carmen is hostile in the wedge demo. How do you handle her?"
- "What evidence makes you confident this is the right slice and not, say, MD&A diff?"
- "What about M&A commentary — why is that out, and would Sarah agree?"

### Architecture probes (20-40 min) — the most aggressive phase

- "Why split into 7 agents? Why not one mega-prompt with structured output?"
- "Why MNPI Scrubber first? What if MNPI gets into the transcript itself?"
- "Why deterministic Citation Verifier? Why not LLM-as-judge on faithfulness?"
- "Why Sonnet for the drafter? Why not Haiku for cost?"
- "Why not fine-tune on Helix's historical notes for the drafter?"
- "What happens if Anthropic has an outage? What's your fallback?"
- "Show me where this breaks. Walk me to a case where the agent produces a wrong note."
- "Why not use OpenAI? You mentioned both BAAs."
- "What if Mei updates the policy mid-engagement?"
- "How does this scale to 10x volume?"
- "Where's the Chinese-wall enforcement in code?"

### Risk + production probes (40-55 min)

- "What's your eval set sourced from?"
- "Pass^k vs pass@1 — what's your k value and why?"
- "How do you catch a 5% drift over a single day?"
- "Carmen says the agent missed a tone shift in week 3. How do you investigate?"
- "What's the rollback procedure?"
- "Who owns this in 90 days?"
- "What's the audit-trace artifact look like for an SEC examiner?"
- "What does Mei need to sign off?"
- "What does Rachel need to sign off?"

### Reverse Q&A probes (55-60 min)

The interviewer will let you ask. What good candidates ask:

- "What's the typical Forward Deployed engagement at your team look like in the first 90 days?"
- "What's the field-back-to-Research loop look like in practice for your team?"
- "What's the failure mode of a new FDE you've seen most often?"
- "What's a customer engagement that surprised you this year?"
- "What would I be doing 6 months in if I joined?"

What graders mark down:
- "What's the team culture like?" (generic)
- "Tell me about a fun project" (generic)
- No questions (red flag)

## Pacing discipline

If you're behind:
- **End of phase 1 (5 min)**: cut philosophical framing, get into discovery
- **End of phase 2 (20 min)**: cut political map detail, move to architecture
- **End of phase 3 (40 min)**: cut at least one architecture defense; move to risk
- **End of phase 4 (55 min)**: skip one risk; get to questions

Going over your time signals weak prioritization. Going under signals you're skipping the conversation. Aim for 55-58 minutes of substance + 2-3 questions.

## Composure under pushback

The interviewer WILL push on something you said. Three valid responses:

1. **Defend with substance**: "I considered that and rejected it because [specific reason]. The tradeoff is [X]; I chose [Y] because [specific factor about this customer]."

2. **Acknowledge and revise**: "That's a fair push. Yes, [their concern]. I'd revise to [new approach]. The tradeoff is [Z], but [reason it's still worth the change]."

3. **Acknowledge as a gap**: "You're right — I don't have a good answer for that yet. My instinct is [X], but I'd want to talk to [stakeholder] before committing. What I'd commit to is finding out by [time]."

NEVER valid:
- Defensiveness ("I don't think that's actually a problem because...")
- Talking over the interviewer
- Going silent for >5 seconds
- Saying "I don't know" without a "but here's how I'd find out"

## Principles before reactive answers (the R1 discipline)

See `09_decision_principles.md`, Principle 5. For every load-bearing architectural choice, the principled answer beats the reactive one. **Name the criterion first, then apply it.**

| Reactive (weak) | Principled (strong) |
|---|---|
| "I picked Sonnet because the drafter needs to synthesize and Haiku doesn't handle synthesis depth." | "I triage tier choices on two questions: synthesis vs extraction, and latency vs cost at this volume. Applying that here, the drafter is synthesis-heavy and volume is ~80 notes/quarter — Sonnet wins on quality and the volume doesn't make cost prohibitive." |
| "I picked deterministic Citation Verifier because LLMs hallucinate on numbers." | "I split deterministic vs LLM by failure-mode reversibility. Hallucinated numbers reaching a PM is irreversible; tone misread is reversible. The Verifier guards the irreversible failure, so it has to be deterministic." |
| "I made MNPI Scrubber first because MNPI is the biggest risk." | "I sequence the architecture by failure cost — the first agent should be the one whose failure costs the most. MNPI leak is fund-shutting; that's why the Scrubber fires before any LLM call." |

The principled answer gives the interviewer 2 surfaces to probe (the principle AND the application), shows you have a framework not just opinions, and generalizes to other architecture choices so they don't have to re-probe each one.

**Pre-rehearse 4-5 of these reframes** for your most load-bearing decisions before the Review. Highest-leverage prep you can do.

## The principles you should be ready to name on demand

| If they probe... | Name this principle |
|---|---|
| "Why this wedge, not the bigger one?" | **Principle 1**: confidence of outcome over size of outcome |
| "How did you decide what's in vs out of v1?" | **Principle 2**: Outcome Risk Matrix (value × risk-of-irreversible-failure) |
| "What's after v1? What does v2 look like?" | **Principle 3**: Phase 1/2/3 sequencing with named gates |
| "How do you know analysts will use it, not route around it?" | **Principle 4**: engagement gap as parallel track (Track B alongside Track A) |
| "Why no write access? Aren't you under-scoping?" | **Principle 6**: read-only v1 defensively — failure mode goes from 'wrong draft Rachel catches' to 'wrong record in PMS that triggers audit' |
| "Walk me through your opening framing" | **Principle 7**: insight first (kill-criteria), then activity |

Internalize them. Don't recite them verbatim. The principle leads, the application follows.

## After the Review

Within 10 minutes:
1. Self-grade against the rubric (`training/interview_60min/rubric.md`)
2. Note 2-3 questions you fluffed
3. Pattern over multiple runs > any single run

Within 24 hours:
- Run the Review on a different case (Calder or Codex prompt) to test domain-portability
- Note where you struggled in the Helix Review that you wouldn't in Calder

## The point of this round

Sierra and OpenAI use the 60-minute Review to test ONE thing: **can you defend technical decisions to a senior peer under sustained pushback for an hour, while staying calibrated about what's known vs unknown?**

The take-home shows what you can build. The Review shows what you can defend. Both matter. The Review matters more for offer decisions.

## The senior FDE mindset

You don't have to be perfect. Frontier labs reward strong-but-flawed candidates over polished mediocre ones. Defend with substance, admit gaps with intellectual honesty, lead with substance over polish. That's the bar.
