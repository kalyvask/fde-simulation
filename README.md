# FDE Simulation

> Open-source training material for Forward Deployed Engineer / Deployed PM / Agent Strategist interviews at frontier AI labs and AI workforce platforms.
>
> Four simulations of increasing depth. Pick the one that matches the interview format you're preparing for.

## About

FDE interviews at frontier AI labs are unlike traditional PM or SWE loops. They test a hybrid skill: scoping an enterprise customer engagement, designing a multi-agent workforce, building a defensible prototype with an eval suite, and presenting all of it to a senior interviewer who will push back on every architectural choice.

There's almost no public material that simulates this. Most guides are generic PM advice plus "build something with LLMs." This repo fills that gap with three concrete, runnable simulations grounded in the real interview shapes used by OpenAI's Deployed PM team, Anthropic's Forward Deployed team, and AI workforce platforms hiring Agent Strategists.

It's structured for self-study, peer mocks, or Claude-Code-as-interviewer.

## Quickstart

5 minutes from clone to your first agent run: see [QUICKSTART.md](QUICKSTART.md).

## Pick your simulation

| Simulation | Time | What you produce | When to use it |
|---|---|---|---|
| [`1-full-engagement`](simulations/1-full-engagement/) | 20-40 hours, 2-4 weeks | Discovery memo + wedge proposal + working Python agent prototype + weighted eval suite + field memo | Portfolio piece. Practice the full FDE skill from cold-start to production. |
| [`2-take-home-5h`](simulations/2-take-home-5h/) | 6 hours (5h build + 1h Review) | Repo + 4-slide deck + 5-min video + eval results, then a 60-min Review transcript | Dress rehearsal for the actual final round at frontier labs. |
| [`3-recommendation-60min`](simulations/3-recommendation-60min/) | 1 hour | A structured live conversation, no artifact required | Recruiter screens, early-stage onsites, any 60-min Review without a take-home. |
| [`4-client-simulation`](simulations/4-client-simulation/) | 20-30 min per scenario × 5 | Live role-play transcript with self-grading | The round that eliminates technically-strong candidates. Practice de-escalation, ownership language, composure under pressure. |

All four are designed to be runnable in Claude Code (with Claude as the simulated interviewer / customer). The artifacts themselves are general-purpose study material.

## Two case studies (both included in sim 1)

| Case | Domain | Fictional customer | Wedge |
|---|---|---|---|
| **Calder Insurance** | Personal-lines insurance / FNOL | Mid-market insurer with 1M+ claims/year | First-Notice-of-Loss agent workforce |
| **Helix Capital** | Long-short equity hedge fund | $2.3B fund, 12 investment professionals | Citation-grounded earnings-note drafter |

Both use synthetic data. Both have working Python prototype scaffolds with eval suites.

## Frameworks (used across all simulations)

Ten portable frameworks that show up in every FDE engagement. Internalize these and they generalize to any case:

1. [4-source convergence](frameworks/4-source-convergence.md) — Buyer / Brief / Industry / Operator triangulation for discovery
2. [3-lens scaffold](frameworks/3-lens-scaffold.md) — Customer / Product / Technical for any agent design
3. [Outcome Risk Matrix](frameworks/outcome-risk-matrix.md) — Value × Risk-of-irreversible-failure for wedge selection
4. [Workflow decomposition](frameworks/workflow-decomposition.md) — 5-step method for drawing agent boundaries from a manual process
5. [Agent shapes catalog](frameworks/agent-shapes-catalog.md) — 7 standard agent shapes (Extractor, Classifier, Synthesizer, Critic, Compliance critic, Router, Auditor)
6. [4-dimensional testing](frameworks/4-dimensional-testing.md) — Static eval + Pass^k + Adversarial + Production observability
7. [Behavioral story types](frameworks/behavioral-story-types.md) — The 5 stories you must have, with a 6-section template per story
8. [Ownership language guide](frameworks/ownership-language-guide.md) — Action verb + first person + specific outcome + business consequence. The single most-cited differentiator in FDE interview write-ups.
9. [Company calibration](frameworks/company-calibration.md) — What different employer archetypes care about with compensation reference bands
10. [Consulting & strategy frameworks](frameworks/consulting-frameworks.md) — Trusted Advisor formula, the Delta Concept (Palantir-origin), Three Whys diagnostic (SoR / CoI / Day 2), Cost-of-Inaction lens, Quick Win Milestone, Shadow IT awareness, C.A.S.E. meta-structure

## Reading list

A curated short list of books, papers, and blogs structured by prep stage: see [READING.md](READING.md). Includes *The Trusted Advisor*, *Pyramid Principle*, *Good Strategy / Bad Strategy*, *Designing Data-Intensive Applications*, plus key papers and blogs. Structured as a 30-day sprint / 3-month / 6-month prep arc.

## Tools

- [`tools/agent_design_practice.html`](tools/agent_design_practice.html) — interactive 3-lens whiteboarding study tool. Single-file HTML, opens offline in any browser. 5-min timer, practice / reference mode toggle, 6 practice prompts including a worked example.

## How to run each simulation in Claude Code

### Simulation 1 (full engagement)

Open the case folder (Calder or Helix). Each case has an `EXERCISE.md` at the top that tells you what to do each week. Work through the phases sequentially. Use the reference solutions only after you've attempted the phase yourself.

### Simulation 2 (5-hour take-home + Review)

Set a 5-hour timer. Open `01_take_home_prompt.md` and don't look at anything else until you've spent 90 minutes thinking. Work through `02_take_home_workflow.md` hour by hour. Submit per `03_submission_spec.md`.

When ready for the Review, paste `ready: helix review` plus your submission into a Claude Code chat. Claude will play the interviewer per `07_interviewer_pack.md` and grade against the rubric in `06_review_round_script.md`.

### Simulation 3 (60-min recommendation)

Read `playbook.md` for the structure. To simulate live, paste the playbook plus a case prompt (the included Sentinel mock case in the playbook, or your own) into Claude Code and ask Claude to play the interviewer for 60 minutes.

## Repo structure

```
fde-simulation/
├── README.md                          # This file
├── LICENSE                            # MIT
├── simulations/
│   ├── 1-full-engagement/             # 20-40 hours, multi-week
│   │   ├── calder-insurance/          # FNOL case
│   │   └── helix-finance/             # Earnings notes case
│   ├── 2-take-home-5h/                # 6 hours total
│   └── 3-recommendation-60min/        # 1 hour
├── frameworks/                        # 6 portable frameworks
└── tools/                             # Interactive HTML study tool
```

## What this is NOT

- Not endorsed by any AI company
- Not based on confidential interview content from any specific company
- Not a guarantee of interview success — frameworks are a tool, not a substitute for substance
- Not actively maintained against changing interview formats — material reflects the public state of the field as of mid-2026

## Contributing

Issues and PRs welcome. Particularly interested in:
- Additional case studies (different domains: legal, healthcare, manufacturing)
- Eval suite improvements for the prototype scaffolds
- Better stakeholder personas for the discovery exercises
- Translations of frameworks into other languages

If you've used the repo for your own interview prep and have feedback, an issue with "what worked" + "what was confusing" is gold.

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgments

Built with Claude Code. The 3-lens framework draws on patterns common in product design and customer-discovery literature; this repo applies them specifically to agent-workforce design. The case studies, prototype scaffolds, frameworks, and worked examples are original to this repo.

If this material helps you land an FDE role, please consider:
- Opening an issue with your story (anonymous if you prefer) so others can learn from your prep
- Adding a case from your new employer's domain to the simulations
- Contributing a translation
