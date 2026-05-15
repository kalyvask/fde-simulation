# FDE Simulation

> Hands-on simulations of the Forward Deployed Engineer role. Run a full customer engagement on synthetic but realistic case studies — identify problems, scope wedges, build working agent prototypes, ship eval suites, hand off to production.

## About

Forward Deployed Engineering (and its equivalents — Solutions Architect, AI Strategist, Agent Strategist, Deployed PM) is customer-embedded technical product work. The day-to-day is: scope an enterprise engagement, identify the highest-value workflow to automate, design a multi-agent system, build a prototype, validate with stakeholders, hand off to production.

There's almost no public material that simulates this end-to-end. Most "AI engineering" tutorials skip the customer-engagement work; most product courses skip the agent architecture. This repo fills the gap with runnable simulations grounded in the actual shape of the job.

What you can do with it:

- **Run a 4-week customer engagement** end-to-end on two fictional cases (insurance + finance), with synthetic data and working Python agent prototypes
- **Identify and scope problems** using six discovery frameworks on a real-feeling customer brief (12-stakeholder political maps, kill-criteria framing, 4-source convergence)
- **Build agents** by extending the prototype scaffolds — 5-7 specialized agents per case, hybrid deterministic + LLM, examiner-readable audit traces
- **Ship eval suites** with pass^k=5 production thresholds, weighted by failure cost, including adversarial cases
- **Practice the customer-facing craft** via Claude-roleplay stakeholder interviews and live customer-simulation rounds

The same material doubles as comprehensive interview prep for FDE-style roles at frontier AI labs and AI workforce platforms. That use is documented but secondary; the primary purpose is hands-on role simulation.

## Quickstart

90 seconds from clone to your first agent run: see [QUICKSTART.md](QUICKSTART.md).

```bash
git clone https://github.com/kalyvask/fde-simulation.git
cd fde-simulation
bash demo.sh        # macOS / Linux / WSL
.\demo.ps1          # Windows
```

Runs both prototypes end-to-end at pass^k=5 production threshold. No API key required.

## Two case studies — full 4-week engagements

| Case | Domain | Customer (fictional) | Wedge |
|---|---|---|---|
| **[Calder Insurance](simulations/1-full-engagement/calder-insurance/)** | Personal-lines auto insurance / FNOL | $300M GWP, 14 NE states, 600 claims/day | First-Notice-of-Loss agent workforce; replace one BPO contract + cut LAE ratio by 140bps |
| **[Helix Capital](simulations/1-full-engagement/helix-finance/)** | Long-short equity hedge fund | $2.3B AUM, 12 investment professionals, 80-name coverage book | Citation-grounded morning-after-earnings note drafter; 4h analyst task → 30min review |

Each case includes:

- **`CASE_BRIEF.html`** — consulting-style case-study reading page. Stakeholders, headline numbers, kill-criteria, working hypothesis. Open in browser; print-friendly.
- **`START_HERE.md`** — in-character engagement kickoff. The customer's email arrives at a specific timestamp; engagement clock starts.
- **`00_brief.md`** — formal customer brief in markdown.
- **4-week structure** — discovery → solution → validation → handoff. Each week has reference solutions you compare against AFTER your own attempt.
- **Working Python prototype** — 5-7 agents (Calder: 5; Helix: 7) running end-to-end on synthetic data. Hybrid deterministic + LLM. Falls back to mock mode without an API key.
- **Weighted eval suite** — pass^k=5 production threshold. Adversarial cases per major risk. Both prototypes verified at 100% weighted pass.
- **Stakeholder role-play prompts** — 8 (Calder) and 7 (Helix) Claude prompts you paste in to conduct interactive discovery interviews.

## What's in the repo

### Simulations

| | Time | Output | Use |
|---|---|---|---|
| **[`1-full-engagement`](simulations/1-full-engagement/)** | 20-40 hrs over 2-4 weeks | Discovery memo, wedge proposal, working Python prototype, weighted eval suite, field memo, retrospective | The headline simulation. Run the FDE role end-to-end on Calder + Helix. |
| **[`2-take-home-5h`](simulations/2-take-home-5h/)** | 6 hrs (5h build + 1h Review) | Repo + 4-slide deck + 5-min video + eval results | Compressed version. Build under a real clock, then defend the build live. |
| **[`3-recommendation-60min`](simulations/3-recommendation-60min/)** | 1 hr | Structured live conversation | The 60-min recommendation-only format. No artifact, just live structuring. |
| **[`4-client-simulation`](simulations/4-client-simulation/)** | 20-30 min × 5 scenarios | Live de-escalation transcript | Hostile-customer role-play (failing demo, SLA breach, scope dispute). Practice ownership language and composure. |

### Working prototypes

Both prototypes run end-to-end without an API key. Drafters fall back to deterministic mock output; set `ANTHROPIC_API_KEY` for real LLM calls.

```bash
# Calder
cd simulations/1-full-engagement/calder-insurance/02_week2_solution/prototype
python scripts/run_e2e.py    # processes one synthetic FNOL through 5 agents
python scripts/run_eval.py   # 5-case weighted eval at pass^k=5

# Helix
cd simulations/1-full-engagement/helix-finance/02_week2_solution/prototype
python scripts/run_e2e.py    # processes one synthetic earnings call through 7 agents
python scripts/run_eval.py   # 5-case weighted eval at pass^k=5
```

Each agent run produces an examiner-readable audit trace.

### Frameworks (used across all simulations)

11 portable frameworks that show up in every FDE engagement:

1. [4-source convergence](frameworks/4-source-convergence.md) — Buyer / Brief / Industry / Operator triangulation for discovery
2. [3-lens scaffold](frameworks/3-lens-scaffold.md) — Customer / Product / Technical for any agent design; AI-capability-relationship segmentation
3. [Outcome Risk Matrix](frameworks/outcome-risk-matrix.md) — Value × Risk-of-irreversible-failure for wedge selection
4. [Workflow decomposition](frameworks/workflow-decomposition.md) — 5-step method for drawing agent boundaries from a manual process
5. [Agent shapes catalog](frameworks/agent-shapes-catalog.md) — 7 standard agent shapes (Extractor, Classifier, Synthesizer, Critic, Compliance critic, Router, Auditor)
6. [Model-vs-application-layer](frameworks/model-vs-application-layer.md) — Tag every solution as model-layer vs application-layer vs both (sequenced)
7. [4-dimensional testing](frameworks/4-dimensional-testing.md) — Static eval + Pass^k + Adversarial + Production observability
8. [Behavioral story types](frameworks/behavioral-story-types.md) — 5 required story templates for the customer-facing craft
9. [Ownership language guide](frameworks/ownership-language-guide.md) — Action verb + first person + specific outcome + business consequence
10. [Company calibration](frameworks/company-calibration.md) — Employer archetypes + comp bands
11. [Consulting & strategy frameworks](frameworks/consulting-frameworks.md) — Trusted Advisor formula, the Delta Concept (Palantir-origin), Three Whys, Cost-of-Inaction, C.A.S.E. and DASME meta-structures

### Tools

- [`tools/agent_design_practice.html`](tools/agent_design_practice.html) — interactive 3-lens whiteboard. Case-aware: select Calder or Helix to load the case study in-character with stakeholder + numbers populated. Or pick one of 5 generic practice prompts. Single-file HTML, opens offline.
  - Deep-link: `tools/agent_design_practice.html?case=calder` or `?case=helix`

### Reading list

A curated set of books, papers, and blogs for deeper FDE craft: see [READING.md](READING.md). The Trusted Advisor (Maister), Pyramid Principle (Minto), Designing Data-Intensive Applications (Kleppmann), Good Strategy / Bad Strategy (Rumelt), plus papers (Attention, ReAct, Constitutional AI) and active blogs. Structured as a 30-day sprint or a 3-month / 6-month arc.

## Repo structure

```
fde-simulation/
├── README.md                          # This file
├── QUICKSTART.md                      # 90-sec on-ramp
├── READING.md                         # Curated reading list
├── LICENSE                            # MIT
├── demo.sh / demo.ps1                 # One-command tour
│
├── simulations/
│   ├── 1-full-engagement/             # 20-40 hours, multi-week
│   │   ├── RETRO_TEMPLATE.md          # End-of-engagement retrospective
│   │   ├── PORTFOLIO_TEMPLATE.md      # How to package as a portfolio piece
│   │   ├── SKIP_AHEAD.md              # 15-hour senior path for second case
│   │   ├── GRADE_YOUR_WORK.md         # Per-phase Claude-graded scoring
│   │   ├── calder-insurance/          # Full 4-week engagement on the FNOL case
│   │   └── helix-finance/             # Full 4-week engagement on the earnings-note case
│   ├── 2-take-home-5h/                # 6 hours (5h build + 1h Review)
│   ├── 3-recommendation-60min/        # 1 hour live conversation
│   └── 4-client-simulation/           # Live customer-handling role-play
│
├── frameworks/                        # 11 portable FDE frameworks
└── tools/                             # Interactive 3-lens whiteboard
```

## How the engagement actually plays out

For Calder (Helix follows the same shape with different numbers):

1. **`CASE_BRIEF.html` opens in your browser** — the case study. Maria's quote, 11 stakeholders, the 9-row metrics table, the working hypothesis.
2. **`START_HERE.md` sets the clock** — Maria's email arrives at 7:45 AM Tuesday. 9 AM kickoff in 70 minutes.
3. **Pre-fill your 3-lens whiteboard** — open `tools/agent_design_practice.html?case=calder`, draft your stakeholder map and wedge hypothesis in Practice mode.
4. **Run the kickoff with Claude playing Maria** — paste Prompt 1 from `STAKEHOLDER_INTERVIEWS.md` into a Claude chat. Maria opens the meeting; you conduct discovery.
5. **Run the other 7 interviews** through the week — Greg, Priya, Tom, Marcus, Rachel, frontline adjuster, Anil. Claude plays each in character.
6. **Synthesize a discovery memo** of your own. Compare to the reference. Score per-phase via `GRADE_YOUR_WORK.md`.
7. **Week 2-3: design + build** — apply the 3-lens scaffold, score wedge candidates on the Outcome Risk Matrix, decompose the workflow into 5-7 agents, extend the prototype scaffold, ship a weighted eval suite.
8. **Week 4: validate + handoff** — run the 20-draft review with Rachel/Janet (Claude plays them), the hostile-review with Carmen/Tom, the operational handoff to Aditya/Anil. Write the field memo.
9. **End of week 4**: fill in `RETRO_TEMPLATE.md`; package via `PORTFOLIO_TEMPLATE.md`.

The deliverable is real: a working agent workforce, a weighted eval suite, a discovery memo, a field memo, and a retrospective. All on synthetic data, all reusable as a portfolio piece.

## Why this is useful

- **For people doing FDE work today**: a reference set of frameworks and reusable scaffolds. Both prototype patterns (Calder + Helix) port to roughly any regulated-industry deployment.
- **For people learning the role**: end-to-end simulations that show what the job actually involves, with reference solutions per phase that calibrate against senior performance.
- **For people interviewing for FDE roles**: the same engagement work doubles as portfolio-grade prep. See `simulations/2-take-home-5h/` for the dress-rehearsal version and `simulations/1-full-engagement/PORTFOLIO_TEMPLATE.md` for how to package the work.

## Contributing

Issues and PRs welcome. Particularly interested in:

- Additional case studies in new domains (healthcare prior-auth, legal contract review, manufacturing change-management, customer-support automation)
- Eval suite improvements for the prototype scaffolds (more adversarial cases, multi-tenant variance tests)
- Better stakeholder personas for the discovery role-play
- Cross-language translations of the frameworks

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgments

Built with Claude Code. The 3-lens framework draws on patterns common in product design and customer-discovery literature; this repo applies them to agent-workforce design. The case studies, prototype scaffolds, frameworks, and reference solutions are original to this repo.
