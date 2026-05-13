# Solo Coach Mode — Running the Review with Me

> How to use this Claude instance (or any AI) as your interviewer for the 60-minute Review. Same value as a peer review, available at 11pm on a Sunday.

## When to use this

- Final dress rehearsal before the real interview
- After your take-home submission, when you need an external read
- Whenever you want to test a specific defense (e.g., "what if they push hard on hallucinated guidance — how do I respond?")

## How to trigger it

When you're ready to run the Review, type in chat:

```
ready: helix review
```

I'll:
1. Confirm I've read your take-home submission (deck + video script + repo notes — paste these in the trigger message if I don't have context)
2. Open the Review by asking you to restate the wedge in 90 seconds
3. Run all 5 phases per `06_review_round_script.md`
4. Push back on every architectural choice with substance, not generic challenges
5. Score you against the rubric at the end

## What to share with me before "ready: helix review"

For the most realistic simulation, paste:

1. **Your wedge statement** (1 paragraph)
2. **Your architecture diagram** (text description or ASCII art if you can)
3. **Your agent decomposition table** (which agents, model tiers, det/LLM)
4. **Your eval results** (pass rate, k value, named failures)
5. **Your 3 sign-off criteria**
6. **What's NOT in v1** (the 3-4 exclusions you defended)

If you don't have all these yet, I'll work from what you do have. If you have none, I'll prompt you for each in real time — which is itself a useful experience because you'll discover what you haven't thought through.

## What I'll do during the Review

- Stay in character as a senior FDE interviewer
- Push back specifically and substantively on your choices
- Vary the pushback intensity based on how you're handling earlier questions
- Track time per phase (and call out if you're going over)
- Score after the Review, not during

## What I'll NOT do

- Give you the answer to my own pushback
- Tell you what to defend before you defend it
- Score generously
- Stop pushing back when you get defensive — that's the test

## Multiple sessions

Pattern over multiple Reviews beats any single Review. Try this sequence:

| Session | Variation | What it tests |
|---|---|---|
| 1 | Standard Helix Review with me | Baseline performance |
| 2 | Helix Review with me playing "hostile Carmen mode" — extra-aggressive pushback | Composure ceiling |
| 3 | Calder Review with me (different domain) | Domain-portability |
| 4 | Codex coding-assistant Review with me | Different deliverable shape |
| 5 | Helix Review again with me playing "warm Sarah mode" — friendly probes | What you actually retained from sessions 1-4 |

If you can score 12+ on the rubric in 3 of 5 sessions, you're at the frontier-lab final-round bar.

## After each session

Within 10 minutes, write down:
1. Your honest score per rubric dimension (be 1 point lower than your gut)
2. The 2 questions you fluffed
3. The 1 architectural defense you'd revise

Patterns across sessions matter more than absolute scores. Watch for:
- Are you getting better at the same rubric dimension over time?
- Where do you reliably struggle? (That's the next prep focus)
- What's the "hard pushback" that consistently throws you?

## What this can't replace

I'm a useful proxy but not the real thing. What I miss:

- Body language during your defense (interviewer reads this constantly)
- The way a senior FDE asks questions (subtle, with longer pauses, more context-shifting)
- The interpersonal warmth of a real conversation (or its absence — both signal)
- The pressure of "this is the actual interview, my career is on the line"

For those, you need real peer mocks. But for sessions 1-5 of practice, I'm a good first pass.

## Trigger phrase

When you're ready:

```
ready: helix review
```

Optionally with your submission details pasted in the same message.

I'll take it from there.
