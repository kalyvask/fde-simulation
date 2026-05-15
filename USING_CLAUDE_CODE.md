# Using This Repo With Claude Code

> Practical guide for driving the simulations with Claude Code as your operating environment. Claude Code reads the repo's `CLAUDE.md` automatically when you open a session here, so it knows the structure, the stakeholders, and the conventions. This file documents the patterns you'll use most.

## Prerequisites

- Claude Code installed (instructions at [claude.com/claude-code](https://www.anthropic.com/claude-code))
- This repo cloned locally
- (Optional) `ANTHROPIC_API_KEY` set so the prototype agents call real Claude instead of mock mode
- (Optional) `OPENAI_API_KEY` for the OpenAI failover path in the Helix prototype

## Open a session

```bash
cd fde-simulation
claude
```

Claude Code reads `CLAUDE.md` on session start. You don't need to brief it on the repo — it already knows what the simulations are, where the prototypes live, and which files are reference solutions versus things you should write yourself.

## The patterns you'll use most

### Pattern 1 — Start an engagement

Best opener when you've just cloned the repo:

> "I'm starting the Calder full engagement. Walk me through day 1."

Claude will point you at `CASE_BRIEF.html`, `START_HERE.md`, and the day-1 schedule. It won't dump everything at once; it'll match the pace of the engagement.

Variant for Helix:

> "I'm starting Helix. I've already done Calder. Where should I cut corners?"

Claude will route you to `SKIP_AHEAD.md` and the 15-hour senior path.

### Pattern 2 — Stakeholder role-play

The 15 stakeholder prompts in `STAKEHOLDER_INTERVIEWS.md` are designed for Claude Code. Two ways to use them:

**(a) Paste-the-prompt** — open `01_week1_discovery/STAKEHOLDER_INTERVIEWS.md`, copy the block for the stakeholder you want, paste into Claude Code, conduct the interview.

**(b) Reference-by-name** — Claude already has the personas via `CLAUDE.md`:

> "Play Maria Vasquez for the 9 AM kickoff. Open the meeting."

> "Switch character. Play Marcus Hill (Compliance) now. I'm walking in at 2 PM for the disarmament conversation."

Claude stays in character, lets you probe, surfaces the kill-criteria language the persona would actually use.

**Tip**: at the end of each interview, ask:

> "Drop character. Grade my interview. What did I miss? What did I do well?"

You'll get specific feedback against the discipline checklist (4-source convergence, kill-criteria restatement, silent-skeptic surfacing, etc.).

### Pattern 3 — Per-phase grading

After you've produced a discovery memo, wedge proposal, build, or field memo, ask Claude to grade it against the reference:

> "I just finished my Calder discovery memo. Grade it against `01_week1_discovery/discovery_memo.md` using the Phase 1 grader in `GRADE_YOUR_WORK.md`. Be honest. Subtract 1 point per dimension from your gut score."

Claude returns a structured 5-dimension score (0-3 each, max 15), names the single biggest gap, and identifies the one thing to fix before phase 2.

**Discipline reminder baked in**: the prompt explicitly tells Claude to grade harshly. Don't soften this.

### Pattern 4 — Extend the prototype (pair programming)

The prototypes are starter scaffolds. Claude will help you extend them — but only after you've defended the architectural choice.

Example:

> "I want to add an SIU (Special Investigation Unit) triage agent to the Calder workforce. It should flag claims with fraud signals from Verisk before the drafter runs. Walk me through where it fits architecturally, then implement it as a new agent following the existing `BaseAgent` pattern."

Claude will:
1. Position the new agent in the orchestration flow (between Intake and Drafter)
2. Show the `BaseAgent` subclass pattern with proper trace integration
3. Write the agent code, update `workforce.py`, add eval cases
4. Tell you where to add tests

If you skip the architectural reasoning step ("just add an SIU agent"), Claude will ask why first. That's intentional.

### Pattern 5 — Run the 60-min take-home Review

The take-home pack (`simulations/2-take-home-5h/`) includes the Review-round trigger:

> "ready: helix review"
>
> [paste your submission: repo URL or deck text + eval results summary]

Claude takes the role of a senior FDE interviewer, runs 60 minutes of pushback through 5 phases per `07_interviewer_pack.md`, and grades at the end against the rubric.

This works best in a dedicated chat session — Claude maintains the interviewer character across the full 60 minutes.

### Pattern 6 — Run a client-simulation scenario

The 5 scenarios in `simulations/4-client-simulation/playbook.md` are designed for Claude Code:

> "Run scenario 1 from the client simulation playbook. You play the COO. I'm the FDE. Live-demo-is-failing setting. Start."

Claude opens the scene in character, pushes back per the playbook, drops character at 20 minutes to grade you against the 5-step de-escalation script.

### Pattern 7 — Engagement state coach

When you come back to the repo after a break:

> "I'm in week 2 of the Calder engagement. I finished the discovery memo last week (week 1) and started the wedge proposal yesterday. What should I be doing today? What do I keep skipping?"

Claude reads your work, compares to the week-2 deliverables, names what's missing. Useful for multi-week engagements where you lose context.

### Pattern 8 — Frameworks-applied review

After an engagement (or mid-engagement), ask Claude to grade which frameworks you actually deployed:

> "Read my discovery memo and wedge proposal. Which of the 11 frameworks in `frameworks/` did I actually use? Which did I name? Which did I skip? Score each as 'deployed / named / skipped'."

Useful before writing the `PORTFOLIO_TEMPLATE.md` `frameworks-applied.md` doc — Claude tells you what you actually did vs what you said you did.

## Tips for productive Claude Code sessions

### Use TodoWrite to track engagement state

Claude Code's `TodoWrite` tool is the right way to track multi-week engagement progress. Either let Claude initialize a todo list at the start of week 1, or paste your own.

Example session opener:

> "Initialize a todo list for my Calder engagement. Track all 4 weeks. Mark week-1 stakeholder interviews as the active todos."

Updates persist across the conversation. At end of week 1, Claude marks discovery todos complete and surfaces week 2.

### Have Claude save outputs as files

Claude will write your discovery memo, wedge proposal, run-book, etc. to disk in your work-repo when you ask. Keep your own work in a separate directory from the simulation repo:

> "Write my discovery memo to `~/my-fde-portfolio/calder/discovery_memo.md`. Use the structure from the reference but write it in my own voice based on the interviews we just ran. Don't copy the reference; synthesize from my notes."

### Ask Claude to RUN the prototypes for you

Instead of switching to a terminal:

> "Run the Calder eval suite at pass^k=5. If anything fails, explain root cause."

Claude shells out to `python scripts/run_eval.py`, reads the output, explains failures by referencing the agent code.

### Cross-session continuity

Each Claude Code session is a fresh context. To preserve engagement state across sessions, save it as a markdown file in your work-repo:

> "Save a checkpoint of where I am in the engagement to `~/my-fde-portfolio/calder/CHECKPOINT.md`. Include what's done, what's next, and the 3 things I should pick up on tomorrow."

Next session: `cat CHECKPOINT.md` to brief Claude.

## What NOT to do with Claude Code

| Don't | Why |
|---|---|
| Ask Claude to write your discovery memo from scratch | Defeats the simulation. The exercise is **you** synthesizing from stakeholder interviews. Use Claude to grade your draft, not to produce it. |
| Have Claude play both the interviewer AND the grader in the same session | The grader needs to be independent of the interviewer to be honest. Use separate sessions, or explicitly tell Claude to "drop character and grade as an external reviewer." |
| Paste reference solutions into Claude to "summarize" them before doing the exercise | You're spoiling your own learning. The reference solutions exist for post-hoc comparison only. |
| Open all 4 simulations in parallel sessions | Claude Code's value is sustained context per session. Pick one simulation per session; switch sessions when switching simulations. |
| Use Claude Code as a passive AI assistant ("what should I think about?") | Claude Code is most useful when you bring sharp questions, drafts, or specific work-in-progress. Vague prompts produce vague replies. |

## Slash commands (optional, advanced)

If you use the simulations repeatedly, consider wrapping common patterns as slash commands. The repo doesn't ship slash commands today (intentional — keeps the dependency surface zero), but you could build:

- `/fde-mock-helix` → runs the 60-min take-home Review with Claude as interviewer
- `/fde-stakeholder calder maria` → opens the Maria role-play directly
- `/fde-grade discovery` → grades the discovery memo at the current path against the reference

See Claude Code's [skill-creator documentation](https://github.com/anthropics/claude-cookbooks) for the pattern. Skills here would be customer-specific to your prep flow; the repo deliberately stays skill-free so you can wrap it your own way.

## Common sessions, end to end

### Session 1 — Calder kickoff day (90 minutes)

```
$ cd fde-simulation
$ claude

You: I'm starting Calder. Walk me through day 1.
Claude: [points at CASE_BRIEF.html, START_HERE.md, briefs you on Maria]

You: [reads CASE_BRIEF.html in browser]

You: OK ready. Play Maria for the 9 AM kickoff. Open the meeting.
Claude: [opens in character as Maria]

[45 minutes of interview]

You: Drop character. Grade my interview against the discovery rubric.
Claude: [graded feedback]

You: Save my Maria interview notes to ~/my-fde-portfolio/calder/maria_notes.md
Claude: [saves]
```

### Session 2 — Calder eval debugging (30 minutes)

```
$ cd fde-simulation
$ claude

You: Run the Calder eval suite at pass^k=5. Walk me through any failures.
Claude: [runs run_eval.py, explains the one borderline case]

You: Why is the policy_rule_elderly_NJ_10x case borderline?
Claude: [reads policy_library.py + the case + the trace, explains]

You: Suggest 2 specific changes to push this from borderline-pass to clean-pass.
Claude: [reads code, proposes targeted edits]

You: Make change #1. Don't touch the eval case itself; only the policy library.
Claude: [edits policy_library.py, re-runs eval, reports new score]
```

### Session 3 — Helix Carmen hostile review (25 minutes)

```
$ cd fde-simulation
$ claude

You: Run the Carmen hostile review session from the Helix week 3 sessions.
     You play Carmen. I'm the FDE. Start.
Claude: [opens in character, brings 10 sample drafts, finds 3 architectural gaps]

[20 minutes of pushback]

You: Drop character. Grade me on the 5-step de-escalation script and the
     4 strong-signal markers.
Claude: [graded feedback with specific moments where I missed signals]

You: Save the 3 architecture changes she surfaced as TODOs in
     ~/my-fde-portfolio/helix/week3_todos.md
Claude: [saves with context]
```

## A note on cost

If you run the Helix prototype at pass^k=5 with a real `ANTHROPIC_API_KEY`:

- 80 eval cases × 5 runs × ~$0.04 per agent invocation × 7 agents = ~$112 for a full eval suite run
- The Calder prototype is cheaper (5 agents): ~$80 for the equivalent run

These are real numbers; budget accordingly. Mock mode (no API key) is free and lets you see the architecture without LLM costs.

## Where to ask for help

- File-specific questions: ask Claude Code directly (it has the repo context)
- Repo-level questions or bug reports: open a GitHub issue
- Want to add a new case or framework: PR welcome; see `README.md` § Contributing
