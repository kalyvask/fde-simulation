# 5-Minute Video Walkthrough Guide

> First take. Don't re-record. The interviewer is looking for clarity under time pressure, not polish.

## Why this matters

OpenAI specifically requires a video walkthrough on Deployed PM (Codex) and FDE take-homes. Per the JD: FDEs present to executives weekly. The video is testing whether you can communicate technical decisions to a non-technical stakeholder under time pressure.

Sierra often skips the video requirement but if you offer one, you score higher on the "Communication" rubric dimension.

## The 5-minute structure

| Time | Section | What you say |
|---|---|---|
| 0:00 - 0:30 | **Setup** | Your name + the case + the wedge in one sentence |
| 0:30 - 2:00 | **Architecture walk** | Show the diagram. Explain each agent in 10-15 seconds. Defend the model tier choices. |
| 2:00 - 3:30 | **Live demo** | Run your agent on one synthetic case. Show: input → agent flow → output → audit trace. Use the screen, not slides. |
| 3:30 - 4:30 | **What's NOT in v1** | Explicitly name 3-4 things you scoped out. Defend each. Show one adversarial eval case you caught. |
| 4:30 - 5:00 | **What I'd ship next** | One sentence on v1.5; one sentence on the field memo back to Anthropic/OpenAI. |

## Section-by-section playbook

### 0:00 - 0:30 — Setup

Open with:
> "Hi, I'm [Name]. The case is Helix Capital — a $2.3B hedge fund losing senior analysts to the morning-after-earnings grind. The wedge I built is a citation-grounded agent workforce that drafts the analyst note while making hallucinated-number risk architecturally impossible. Let me show you."

That's exactly 30 seconds at normal speech pace. Pace it.

### 0:30 - 2:00 — Architecture

Bring up the deck on screen. Slide 2 (the architecture diagram).

Talk through the agents in order. For each agent, in 10-15 seconds:
- What it does
- Model tier (Haiku / Sonnet / GPT-4o-mini / GPT-4o)
- Deterministic or LLM
- One sentence on why

Specifically defend:
- **Why MNPI Scrubber is first**: "MNPI handling is a hard architectural wall. If this agent fires, no LLM call ever happens. The cost of a single MNPI leak is potentially fund-shutting."
- **Why Note Drafter is the only synthesis LLM**: "Every other agent is deterministic or LLM-as-judge. The drafter is where we deliberately spend LLM cost — natural language synthesis is what LLMs are uniquely good at."
- **Why Citation Verifier is deterministic, not LLM**: "Sarah's kill-criteria is hallucinated numbers. The verifier is regex-grounded; it has to be reliable in the same way every time."

### 2:00 - 3:30 — Live demo

Switch to your terminal or run a script. Demo one synthetic earnings call going through the agent.

Show:
1. The input claim (5 seconds)
2. The agent log as it processes (15-20 seconds)
3. The output draft (15 seconds — read 2-3 lines aloud)
4. The audit trace (15-20 seconds — show it's examiner-readable)

If you have time: show ONE case where the system correctly blocks (e.g., MNPI watch-list case).

### 3:30 - 4:30 — What's NOT in v1

This is the most underrated section. Naming what you cut signals more than naming what you built.

> "Three things I scoped out of v1:
> 1. **Bodily-injury claims** — wait, that's Calder. Let me restate: M&A commentary — Reg FD minefield, requires separate compliance architecture
> 2. **Position-sizing recommendations** — cross-Chinese-wall risk, deterministically blocked by the compliance critic
> 3. **Multi-quarter context with full retrieval** — v1 uses prior 1 quarter; v2 expands to 4 quarters via embeddings"

If you have time: show one adversarial eval case that catches a real failure mode (e.g., the position-sizing-leak case).

### 4:30 - 5:00 — What's next

Close with:
> "What I'd ship in v1.5: better tone-shift detection calibrated against SubjECTive-QA labels. What I'd want from Anthropic/OpenAI: a first-class immutable-snapshot primitive for agent versioning — currently I'm rolling my own. Looking forward to the Review."

That's 25 seconds. Sign off. Don't add filler.

## What graders look for in the video

1. **Speech pace**: not rushed, not slow. Natural conversation speed.
2. **Screen clarity**: text readable, no busy backgrounds
3. **Live demo, not screenshots**: showing the agent actually running > showing a slide of "results"
4. **Honest scope**: "I cut X because Y" > "I built everything"
5. **Specificity**: "MNPI Scrubber blocks before any LLM call" > "good security"
6. **Confidence under self-cutoff**: ending at 5:00 cleanly > ending at 5:35 because you tried to cram in one more thing

## What you should NOT do

- Don't apologize ("sorry the demo is a bit messy")
- Don't over-explain ("let me first give you context on the AI industry...")
- Don't read the slide verbatim ("As you can see on slide 2...")
- Don't re-record more than twice (first take if possible)

## Tech check before recording

- Mic: clear, no background noise
- Screen: high resolution; close all Slack/email windows
- Camera: optional. If on, eye contact with camera (not screen) for the framing + closing sections
- Length: aim for 4:45-5:15. Loom will show you the time.

## When to record

Record at minute 50 of hour 5 (you've got 10 minutes for the video + 5 for upload + sharing). If you go over, you eat into your buffer. Don't.
