# Interviewer Pack — For Whoever Role-Plays the Review

> If a peer / coach / Claude / GPT is playing the interviewer for this Helix case, this is their script. Do NOT show this to the candidate before the Review.

## Your role

You're a senior FDE / Solutions Engineer running the 60-minute Review round. You've:
- Watched the candidate's 5-min video
- Read their 4-slide deck
- Skimmed their repo

You have 60 minutes. You're warm but not deferential. Your job is to surface gaps, not to validate the candidate.

You will push back on every load-bearing architectural choice. At AI workforce platforms and OpenAI, the Review is structured to test whether candidates fold under pressure or defend with substance.

## Phase 1 — Framing (0:00 - 0:05, 5 min)

After their opening framing (~90 sec), ask 1-2 of:
- "What did you assume about Sarah that wasn't in the prompt?"
- "What did you choose to skip in your take-home, and why?"
- "Why this wedge, not the obvious one?"
- "Who's the buyer here? Who signs the renewal?"

If they restate the wedge in <60 seconds and address the kill-criteria: good signal.
If they ramble or open with the tech: weak signal — mark them down on customer-first framing.

## Phase 2 — Discovery probes (0:05 - 0:20, 15 min)

Ask 4-5 of:
- "Walk me through Rachel. What 3 questions would you ask her in your first 30 minutes?"
- "Mei is default-no. What's your disarmament script?"
- "Carmen is hostile. How do you handle her?"
- "Why did you exclude M&A commentary specifically?"
- "What evidence makes you confident the wedge is on the right slice?"
- "Who's the silent skeptic in this org?"
- "What if the operator (David) says coverage decisions are actually the bottleneck?"
- "Who haven't you talked to that you should?"

**Good signal**: cites verbatim stakeholder language ("Sarah said 'the deck moves from operational improvement to regulatory exposure overnight'"); names the disarmament pattern with Mei explicitly; addresses Carmen as a separate test case, not lumped in with users.

**Weak signal**: generic ("I'd ask about their workflow"); doesn't address the political map; treats Mei as procedural rather than a relationship.

## Phase 3 — Architecture probes (0:20 - 0:40, 20 min) — the most aggressive phase

The biggest pushback phase. Ask 6-8 of these. Drill until they revise or defend with substance.

- "Why split into 7 agents? Why not one mega-prompt?"
- "Why MNPI Scrubber first? What if MNPI gets into the transcript itself?"
- "Why deterministic Citation Verifier? Why not LLM-as-judge on faithfulness?"
- "Why Sonnet for the drafter and Haiku for the KPI extractor?"
- "Why not fine-tune on Helix's historical notes for the drafter?"
- "What happens if Anthropic has an outage? What's your fallback?"
- "Show me where this breaks. Walk me to a case the agent produces a wrong note."
- "Why not use OpenAI's structured outputs API instead of Anthropic's JSON-mode prompting?"
- "What if Mei updates the policy library mid-engagement?"
- "How does this scale to 10x volume?"
- "Where's the Chinese-wall enforcement in code?"
- "How do you know KPI extraction is accurate vs a regex baseline?"

**Specific push-back patterns**:
- If they say "deterministic" anywhere: push "what's the failure mode of deterministic in this domain?"
- If they say "LLM-as-judge" anywhere: push "what's your calibration data for the judge?"
- If they say "Sonnet" anywhere: push "why not Haiku? what's your latency budget?"
- If they say "audit trace" anywhere: push "show me what an SEC examiner sees"

**Good signal**: defends with "I considered X and rejected because [specific reason]" or "yes, that's a gap — I'd revise to Y". Cites tradeoff explicitly. Doesn't get defensive.

**Weak signal**: "we'd handle that" / "the framework supports that" / talks over you / goes silent for >5 sec.

## Phase 4 — Risk + production probes (0:40 - 0:55, 15 min)

After they list risks, push 3-5 of:
- "What's your eval set sourced from? Real data or synthetic?"
- "Pass^k vs pass@1 — what's your k value and why?"
- "How do you catch a 5% drift over a single day?"
- "Carmen says the agent missed a tone shift in week 3. How do you investigate?"
- "What's the rollback procedure if a release breaks?"
- "Who owns this 90 days post-handoff?"
- "What's the audit-trace artifact for an SEC examiner — actually show me?"
- "What does Mei need to sign off? In a specific number."
- "What does Rachel need to sign off? In a specific number."

**Good signal**: names specific eval-case categories (MNPI block, hallucinated guidance, policy combinations); cites pass^k=5 as the production threshold; has 3 named sign-off criteria with stakeholder owners; can pull up an examiner trace from the repo on screen.

**Weak signal**: "we'll thoroughly test"; pass@1 thinking; no rolling window detail; can't show the audit trace artifact.

## Phase 5 — Reverse Q&A (0:55 - 1:00)

Let them ask. Notice:
- Quality of questions (specific to your team /  / OpenAI vs generic)
- Evidence of preparation (do they reference your team's public work?)
- Composure after 55 minutes of pushback

**Strong**: 2-3 specific questions referencing your team's published content / a recent customer engagement / a real career-trajectory concern.

**Weak**: "What do you like about working here?" / "What's the team culture?" / no questions.

## Scoring (use this rubric after they leave)

Per `training/interview_60min/rubric.md`. Score after the Review, not during. Memory blurs once you start grading mid-conversation.

| Dimension | Score (0-3) | Note |
|---|---|---|
| Customer-first framing | | |
| Agent architecture judgment | | |
| Production thinking | | |
| Risk surfacing | | |
| Communication | | |
| **TOTAL** | **/ 15** | |

## How to give feedback after the Review

Three-part feedback:
1. **What worked** (2-3 things, specific, with quotes from their talk)
2. **What didn't work** (2-3 gaps, specific, tied to rubric dimensions)
3. **The one pattern to fix before the next round**

Don't give the score verbally — write it down after they leave. Verbal scores anchor too hard.

## If you're using Claude / GPT as the interviewer

Open a fresh chat. Paste:

> "You are a senior Forward Deployed Engineer at OpenAI conducting a 60-minute Review round on a Helix Capital case study take-home submission. I'll paste my deck, my video transcript, and my repo structure. You will push back on every load-bearing architectural choice for 60 minutes — substance, not generic challenges. Be warm but not deferential. After the 60 minutes, score me against this rubric: [paste rubric.md content]. Start by asking me to restate the wedge in 90 seconds."

Then paste your deck text, your video script, and your README. The AI will run the Review.

This is a good way to get 5-7 mock interviews in before the real thing. Pattern over multiple sessions matters more than any single attempt.
