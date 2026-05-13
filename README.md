# FDE Simulation

> Open-source training material for Forward Deployed Engineer / Deployed PM interviews at frontier AI labs (Anthropic, OpenAI, Sierra, and similar).
>
> Three simulations of increasing depth. Pick the one that matches the interview format you're preparing for.

## What this is

Most FDE prep is generic PM interview advice plus "build something with LLMs." This repo gives you three concrete, runnable simulations grounded in real interview shapes:

1. **Full engagement** — a multi-week FDE engagement, end-to-end. You do real discovery, scope a wedge, build a working agent prototype with an eval suite, and produce a field memo. ~20-40 hours.
2. **5-hour take-home + 60-min Review** — the actual final-round format used by Anthropic, OpenAI Deployed PM, and Sierra Agent Strategist. ~6 hours total.
3. **60-min recommendation interview** — high-level structural conversation covering Discovery / Solution Strategy / Risk & Validation. ~1 hour.

All three are designed to be runnable in Claude Code (with Claude as the simulated interviewer for round 2 and 3), but the artifacts themselves are general-purpose study material.

## Pick your simulation

| Simulation | Time | What you produce | When to use it |
|---|---|---|---|
| [`1-full-engagement`](simulations/1-full-engagement/) | 20-40 hours | Discovery memo, wedge proposal, working agent prototype + eval suite, field memo | Portfolio piece. Practice the full FDE skill from cold-start to production. |
| [`2-take-home-5h`](simulations/2-take-home-5h/) | 6 hours (5h build + 1h Review) | Repo + 4-slide deck + 5-min video + eval results, then a 60-min Review transcript | Dress rehearsal for Anthropic / OpenAI / Sierra final round. |
| [`3-recommendation-60min`](simulations/3-recommendation-60min/) | 1 hour | A structured live conversation (no artifact) | Recruiter screens, early-stage onsites, any 60-min Review without a take-home. |

## Two case studies (both included in sim 1)

| Case | Domain | Customer | Wedge |
|---|---|---|---|
| **Calder Insurance** | Personal-lines insurance / FNOL | Mid-market insurer with 1M+ claims/year | First Notice of Loss agent workforce |
| **Helix Capital** | Long-short equity hedge fund | $2.3B fund, 12 investment professionals | Citation-grounded earnings-note drafter |

Both use synthetic data (no real customers were harmed). Both have working Python prototype scaffolds.

## Frameworks (use across all three sims)

Six portable frameworks that show up in every FDE engagement. Internalize these and they generalize to any case:

1. [4-source convergence](frameworks/4-source-convergence.md) — Buyer / Brief / Industry / Operator triangulation for discovery
2. [3-lens scaffold](frameworks/3-lens-scaffold.md) — Customer / Product / Technical for any agent design
3. [Outcome Risk Matrix](frameworks/outcome-risk-matrix.md) — Value × Risk-of-irreversible-failure for wedge selection
4. [Workflow decomposition](frameworks/workflow-decomposition.md) — 5-step method for drawing agent boundaries from a manual process
5. [Agent shapes catalog](frameworks/agent-shapes-catalog.md) — 7 standard agent shapes (Extractor, Classifier, Synthesizer, Critic, Compliance critic, Router, Auditor)
6. [4-dimensional testing](frameworks/4-dimensional-testing.md) — Static eval + Pass^k + Adversarial + Production observability

## Tools

- [`tools/agent_design_practice.html`](tools/agent_design_practice.html) — interactive 3-lens whiteboarding study tool. Single-file HTML, opens offline in any browser. 5-min timer, practice / reference mode toggle, 6 practice prompts.

## How to run each simulation in Claude Code

### Simulation 1 (full engagement)
Open the case folder (Calder or Helix). Each phase has an `EXERCISE.md` that tells you what to do this week. Work through the phases. Use the `reference_solution/` only after you've attempted the phase yourself.

### Simulation 2 (5-hour take-home + Review)
Set a 5-hour timer. Open `01_take_home_prompt.md` and don't look at anything else until you've spent 90 minutes thinking. Work through `02_take_home_workflow.md` hour by hour. Submit per `03_submission_spec.md`.

When ready for the Review, paste `ready: helix review` plus your submission into a Claude Code chat. Claude will play the interviewer per `07_interviewer_pack.md` and grade against the rubric.

### Simulation 3 (60-min recommendation)
Read `playbook.md` for the structure. To simulate live, paste the playbook plus a case prompt (the included Sentinel mock case, or your own) into Claude Code and ask it to play the interviewer.

## What this is NOT

- Not endorsed by Anthropic, OpenAI, Sierra, or any other company
- Not based on confidential interview content from any specific company
- Not a guarantee of interview success — frameworks are a tool, not a substitute for substance
- Not actively maintained against changing interview formats — material reflects the public state of the field as of mid-2026

## Contributing

Issues and PRs welcome. Particularly interested in:
- Additional case studies (different domains)
- Eval suite improvements for the prototype scaffolds
- Better stakeholder personas / discovery exercises
- Translations of frameworks into other languages

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgments

Built with Claude Code. The 3-lens framework draws on patterns common in product design and customer-discovery literature; this repo applies them specifically to agent-workforce design. The case studies, prototype scaffolds, and frameworks are original to this repo.
