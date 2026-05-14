# Quickstart

> 5 minutes from clone to your first agent run. Pick the simulation that matches your time budget.

## Prerequisites

- **Python 3.10+** (check with `python --version`)
- **Git**
- **Optional**: an Anthropic API key for live LLM calls (prototypes fall back to deterministic mock output if no key is set)
- **Optional**: Claude Code or claude.ai access for the interactive Review rounds

## Clone

```bash
git clone https://github.com/kalyvask/fde-simulation.git
cd fde-simulation
```

---

## Path A: Full engagement (sim 1) — 5 min to first agent run

Best if: you want to actually run code today and see an agent workforce process synthetic data.

```bash
cd simulations/1-full-engagement/calder-insurance/02_week2_solution/prototype

# Create a virtualenv
python -m venv .venv
.venv/Scripts/activate           # Windows
# source .venv/bin/activate      # macOS/Linux

# Install
pip install -r requirements.txt

# (Optional) Add an API key
export ANTHROPIC_API_KEY=sk-ant-...   # macOS/Linux
$env:ANTHROPIC_API_KEY="sk-ant-..."   # Windows PowerShell

# Run end-to-end on one synthetic FNOL claim
python scripts/run_e2e.py

# Run the eval harness on 5 weighted seed cases
python scripts/run_eval.py
```

You should see a synthetic claim processed through 5 specialized agents (Intake → Drafter → Tone Supervisor → Compliance Critic → Audit) and a pass^k=5 eval run with 100% pass rate on the seed cases.

Then open the case folder and follow `EXERCISE.md` for the 4-week guided experience.

### Helix variant

Same shape, different domain. Replace `calder-insurance` with `helix-finance` and run:

```bash
cd simulations/1-full-engagement/helix-finance/02_week2_solution/prototype
pip install -r requirements.txt
python scripts/run_e2e.py
```

You'll see a synthetic earnings call processed through 7 agents including MNPI Scrubber + Citation Verifier.

---

## Path B: 5-hour take-home + Review (sim 2)

Best if: you have one weekend day and want to dress-rehearse the real OpenAI / Anthropic FDE final round.

```bash
cd simulations/2-take-home-5h
```

1. Open `01_take_home_prompt.md`. Set a 5-hour timer.
2. **Don't read anything else for the first 90 minutes.** Think.
3. Work through `02_take_home_workflow.md` hour by hour.
4. At hour 5, submit per `03_submission_spec.md`.
5. Open Claude Code (or claude.ai with artifacts). Paste:
   ```
   ready: helix review
   ```
   Plus your submission (repo link, deck text, eval results).
6. Claude plays the interviewer per `07_interviewer_pack.md` for 60 minutes.
7. Claude grades you against the rubric at the end.

Total time: 6 hours.

---

## Path C: 60-min recommendation interview (sim 3)

Best if: you have an hour and want to drill the Discovery / Solution / Risk framework on a cold case.

```bash
cd simulations/3-recommendation-60min
```

1. Read `playbook.md` once end-to-end (~20 min)
2. Open Claude Code (or claude.ai). Paste the playbook content followed by:
   ```
   Play a senior FDE interviewer. Run a 60-min recommendation interview on this case: [paste the Sentinel mock case from the playbook, OR write your own]. Push back on every load-bearing choice. Score me against the rubric at the end.
   ```
3. Run the 60 minutes.
4. Self-grade against the rubric in the playbook.

Total time: ~90 min including prep.

---

## Path D: Client simulation round (~20-30 min per scenario)

Best if: you're preparing for the FDE-loop round that's a live customer role-play (frustrated client, scope dispute, SLA breach).

```bash
cd simulations/4-client-simulation
```

1. Read `playbook.md` once (~15 min)
2. Open a fresh Claude conversation
3. Copy one of the 5 scenarios from the playbook
4. Run it live for 20-30 min — Claude plays the customer
5. At the end, ask Claude to grade you against the 5-step de-escalation script + the 4 strong-signal markers

Do one scenario per evening over a week. By scenario 5, the de-escalation script should be muscle memory.

## Path E: Just the frameworks (no time at all)

Best if: you have an interview tomorrow and want the cheat sheet.

```bash
cd frameworks
```

Read all 6 framework files (~30 min total). They generalize to any FDE case.

For the agent design / whiteboarding round specifically, also open:

```bash
tools/agent_design_practice.html
```

Single-file HTML, opens in any browser, works offline. 5-min timer + practice/reference mode toggle + 6 practice prompts. Print-friendly.

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'anthropic'`** — you didn't activate the venv or didn't run `pip install -r requirements.txt` from the `prototype/` folder.

**`ImportError: cannot import name 'X' from 'calder_agent.Y'`** — you ran a script from the wrong directory. All scripts assume you're in the `prototype/` folder.

**Drafter outputs are repetitive** — you don't have an API key set, so the Drafter is using deterministic mock output. Set `ANTHROPIC_API_KEY` for real LLM responses.

**`python` command not found on Windows** — try `py` instead, or use the Python launcher.

**Eval harness reports "API key missing" warnings** — expected without a key; the eval still runs in mock mode and reports pass^k against the deterministic outputs. Set a key for realistic pass rates.

---

## Where to go next

- **Repo overview**: [README.md](README.md)
- **Frameworks**: [`frameworks/`](frameworks/)
- **Full engagement guide**: [`simulations/1-full-engagement/README.md`](simulations/1-full-engagement/README.md)
- **5-hour take-home pack**: [`simulations/2-take-home-5h/README.md`](simulations/2-take-home-5h/README.md)
- **60-min recommendation playbook**: [`simulations/3-recommendation-60min/README.md`](simulations/3-recommendation-60min/README.md)
