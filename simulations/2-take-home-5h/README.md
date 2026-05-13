# Simulation 2: 5-Hour Take-Home + 60-Min Review (~6 hours total)

> The actual final-round format used by OpenAI Deployed PM, Anthropic Forward Deployed, and Sierra Agent Strategist. A real 5-hour clock followed by a real Review round.

## What this simulation tests

Whether you can ship a defensible build under a real clock and then defend every architectural choice under sustained pushback from a senior interviewer.

| Phase | Time | What it tests |
|---|---|---|
| **Take-home** | 5 hours | Build a working agent prototype, 4-slide deck, 5-min video, eval results — under a real clock |
| **Submission** | 24h before Review | Repo + deck + video + eval summary, 4 artifacts no more |
| **Review round** | 60 min | Defend every architectural choice; revise gracefully when challenged; acknowledge gaps with intellectual honesty |

## What's in this folder

| File | Purpose |
|---|---|
| `01_take_home_prompt.md` | The case as the candidate sees it. **Read this first; don't read anything else for 90 minutes.** |
| `02_take_home_workflow.md` | Hour-by-hour build plan for the 5 hours |
| `03_submission_spec.md` | The 4 artifacts you ship 24h before the Review |
| `04_deck_template.md` | The 4-slide structure to fill in |
| `05_video_walkthrough_guide.md` | What to cover in the 5-minute video |
| `06_review_round_script.md` | The 60-minute Review structure + probe list |
| `07_interviewer_pack.md` | For whoever (peer / Claude) role-plays the interviewer |
| `08_solo_coach_mode.md` | How to run the Review with Claude as the AI interviewer |
| `09_decision_principles.md` | 8 portable principles to deploy throughout |
| `10_3_lens_applied_to_helix.md` | 3-lens scaffold filled in for the Helix case |
| `11_solution_strategy_depth.md` | Workflow decomposition, agent shapes, orchestration, integration patterns, cost/latency budget, bucket risks |
| `12_mock_case_worked_example.md` | End-to-end "what I'd actually say" for all 5 phases of the Review |

## How to run this simulation

### Solo, with Claude as the interviewer

1. Set a 5-hour timer
2. Open `01_take_home_prompt.md`. That's the case as presented cold.
3. Don't look at anything else for the first 90 minutes
4. Work through `02_take_home_workflow.md` hour by hour
5. At hour 5, submit per `03_submission_spec.md`
6. Optional: wait 24h to simulate the real gap
7. When ready, paste `ready: helix review` plus your submission into a Claude Code chat
8. Claude plays the interviewer per `07_interviewer_pack.md` for 60 minutes
9. Claude grades you against the rubric at the end

### With a peer

1. Same take-home work
2. Peer reads `07_interviewer_pack.md` in advance
3. They run the 60-minute Review; you defend
4. They grade you using the rubric

### As a hostile-environment dry-run

1. Don't fork the prototype scaffold from the full engagement (sim 1). Build cold.
2. Submit, then run the Review with Claude playing a *skeptical* interviewer (ask Claude to push harder than the default).

## What "good" looks like at the end

You will have produced:
- A working earnings-note agent prototype (your version)
- 4-slide deck defending the architecture
- 5-min video walkthrough
- An eval suite with weighted cases
- A 60-minute interview transcript (your defense + Claude's probes)
- A scored rubric (max 15 points)

A 12+ score on the rubric is the frontier-lab final-round bar.

## Note on the case

The take-home prompt is set in the Helix Capital case (fictional hedge fund). The structure transfers to any FDE case — if you want to practice on a different domain, swap the prompt and follow the same workflow. The 12-file structure here is the playbook; the case is the input.
