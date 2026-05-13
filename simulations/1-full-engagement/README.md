# Simulation 1: Full FDE Engagement (multi-week, ~20-40 hours)

> The end-to-end Forward Deployed Engineer experience. Cold-start customer engagement to production-ready prototype. The longest of the three simulations and the one with the most signal about real FDE skill.

## What this simulation tests

The full FDE lifecycle, in order:

| Phase | What you do | What you produce |
|---|---|---|
| **Week 1 — Discovery** | Map stakeholders; interview key roles; pull data on current state; triangulate via 4-source convergence; pick the wedge | Discovery memo + stakeholder map + interview notes |
| **Week 2 — Solution strategy** | Apply 3-lens scaffold; score wedge candidates on Outcome Risk Matrix; design the agent workforce (5-8 agents with shapes) | Wedge proposal + build plan + 4-slide deck draft |
| **Week 3 — Build + eval** | Implement the agents; build a weighted eval suite; calibrate LLM-as-judge agents; run pass^k=5 | Working prototype + 50-case eval suite + adversarial set |
| **Week 4 — Production gates + handoff** | Field memo; production observability; rollback procedure; named owner post-handoff | Field memo + production checklist + audit trace standard |

## Pick a case

Both cases use synthetic data and a fictional customer. Both have full prototype scaffolds. Pick the domain that matches the kind of FDE role you're interviewing for:

| Case | Domain | Use it when interviewing for... |
|---|---|---|
| [Calder Insurance](calder-insurance/) | Personal-lines insurance / claims | OpenAI Deployed PM at insurance customer, an FDE role at a retail-AI-deployment platform |
| [Helix Capital](helix-finance/) | Long-short equity hedge fund / earnings research | OpenAI Deployed PM at finance customer, Anthropic Solutions Engineer for hedge-fund deployment |

You can run both cases sequentially to test domain-portability — that's actually a signal of senior FDE skill.

## How to run this simulation

1. Read the case's `00_brief.md` (the customer prompt)
2. For each weekly phase, open the folder and read `EXERCISE.md` **first**
3. Do the exercise. Spend the suggested time. Don't peek at the reference solution.
4. After you've produced your own artifact, compare against `reference_solution/`
5. Note the gaps between your work and the reference. Those gaps are your prep targets.
6. By the end of 4 weeks, you should have a portfolio piece (your prototype + memo) and a clear sense of where your FDE skill is strong vs weak.

## The honest tradeoff

This simulation is long. Most candidates won't have 40 hours to spare. If you don't, do the 5-hour take-home simulation ([sim 2](../2-take-home-5h/)) instead — it covers ~80% of the same skill in 6 hours.

The full engagement matters when:
- You want a portfolio piece for your application
- You want to actually build agent expertise, not just interview prep
- You're switching into FDE from a different background and need reps
- You're prepping for a multi-week paid trial (some FDE roles include this)

## What "good" looks like

By the end of 4 weeks you should be able to:

1. Walk through your wedge selection in 90 seconds using the 3-lens scaffold
2. Defend every agent boundary by failure mode (not by feature)
3. Show a working prototype that processes synthetic data end-to-end
4. Show an eval suite weighted by failure cost with pass^k=5 results
5. Name 3 sign-off criteria with stakeholder owners
6. Produce a field memo that any future FDE could pick up

If you can do all 6, you're at the FDE final-round bar.
