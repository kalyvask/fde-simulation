# Portfolio Piece — Template

> How to package the artifacts from your engagement so they're ready to present in a real FDE interview. The work you produce in this simulation IS a portfolio piece — but only if you package it correctly.

## Why this matters

Most candidates either:
- Show up to FDE interviews with no portfolio at all (rejection signal: "have you ever built an agent workforce in production?")
- Show up with a portfolio that's a code dump (rejection signal: "the interviewer can't tell what you actually owned vs what was scaffolded")

A well-packaged portfolio piece beats 10 hours of LeetCode practice. It signals **you've done this work before**, which is the single most important hiring signal for FDE roles.

## What goes in the portfolio

After running an engagement (Calder, Helix, or your own), you should have:

| Artifact | Where it lives in the engagement |
|---|---|
| Discovery memo | `01_week1_discovery/discovery_memo.md` |
| Stakeholder map | `01_week1_discovery/stakeholder_map.md` |
| Wedge proposal | `02_week2_solution/wedge_proposal.md` |
| Build plan | `02_week2_solution/wedge_build_plan.md` |
| Working agent prototype | `02_week2_solution/prototype/` |
| Weighted eval suite | `02_week2_solution/prototype/evals/` |
| Pass^k=5 eval results | output of `python scripts/run_eval.py` |
| Audit trace renderer + examples | `02_week2_solution/prototype/calder_agent/examiner_renderer.py` |
| Field memo (lab feedback) | `04_week4_handoff/field_memo.md` |
| Stakeholder session notes (week 3 + 4) | `03_week3_validation/sessions/` + `04_week4_handoff/sessions/` |
| Engagement retrospective | `RETRO.md` (from `RETRO_TEMPLATE.md`) |

That's 11 artifacts. Don't put all of them in the portfolio. Curate.

## The portfolio repo structure

Create a separate public repo (e.g., `your-name-fde-portfolio`). Recommended structure:

```
your-name-fde-portfolio/
├── README.md                  # 1-page overview + how to navigate
├── case-study/                # The main artifact
│   ├── 1-discovery.md         # Polished discovery memo
│   ├── 2-wedge-proposal.md    # Polished wedge proposal
│   ├── 3-build/               # The prototype (your code, your prompt iterations)
│   │   ├── README.md          # How to run it
│   │   ├── agent/             # Your agent code
│   │   ├── evals/             # Your eval cases
│   │   └── scripts/           # run_e2e.py, run_eval.py
│   ├── 4-results.md           # Eval results + what you shipped
│   └── 5-field-memo.md        # Lessons + lab feedback
├── frameworks-applied.md      # Which frameworks from fde-simulation you used + how
├── retrospective.md           # Filled-out RETRO.md
└── docs/                      # Supporting artifacts
    ├── deck.pdf               # 4-slide deck
    ├── audit-trace-sample.html # One examiner-readable trace
    └── walkthrough.mp4        # 5-min video walkthrough (optional but high-impact)
```

## The portfolio README — the 1-page pitch

This is what an interviewer reads first. It's the headline. It should answer 4 questions in <60 seconds of reading:

1. **What did you build?** (one sentence)
2. **Why does it matter?** (one sentence — name a customer-side metric)
3. **What's the technical signal?** (one sentence — name the architecture)
4. **What's the FDE signal?** (one sentence — name the customer-engagement craft)

### Template

```markdown
# [Your Name] — FDE Case Study: [Customer Name]

> [One-sentence problem statement that names the customer's kill-criteria]
>
> [One-sentence solution statement that names the wedge]
>
> Built solo over [N hours] across [domain]. The repo is reviewable in 10 minutes;
> the deeper artifacts are linked below.

## TL;DR (60 seconds)

- **Wedge**: [Specific narrow workflow you automated]
- **Customer-side metric**: [Pre / post baseline, e.g., "Senior-analyst review time: 4 hours → 30 minutes per note"]
- **Architecture**: [Specific pattern, e.g., "7 specialized agents, hybrid deterministic + LLM, with MNPI Scrubber as the first deterministic gate"]
- **FDE signal**: [Specific customer-engagement move, e.g., "Used the hostile-review pattern to move the silent-skeptic stakeholder from blocker to active reviewer in week 3"]

## What's in this repo

| File | What it is | Reading time |
|---|---|---|
| [`case-study/1-discovery.md`](case-study/1-discovery.md) | Week 1 stakeholder map + discovery memo | 4 min |
| [`case-study/2-wedge-proposal.md`](case-study/2-wedge-proposal.md) | Week 2 wedge selection + agent architecture | 5 min |
| [`case-study/3-build/`](case-study/3-build/) | Working Python prototype + eval suite | 10 min |
| [`case-study/4-results.md`](case-study/4-results.md) | Pass^k=5 results + customer-side metrics | 2 min |
| [`case-study/5-field-memo.md`](case-study/5-field-memo.md) | What I'd ask AI lab Product team for | 3 min |
| [`retrospective.md`](retrospective.md) | What worked, what didn't, what I'd change | 4 min |

## How to evaluate this work in 10 minutes

If you have 10 minutes to assess my FDE skill from this repo:

1. **Minute 0-2**: This README + the TL;DR
2. **Minute 2-5**: [`case-study/4-results.md`](case-study/4-results.md) — the metrics + the architecture summary
3. **Minute 5-8**: `cd case-study/3-build/ && python scripts/run_e2e.py` — see the workforce run on a synthetic case
4. **Minute 8-10**: [`retrospective.md`](retrospective.md) — what I'd change about the engagement structure

## Frameworks I used

This case study deploys frameworks documented in [github.com/kalyvask/fde-simulation](https://github.com/kalyvask/fde-simulation):
- 4-source convergence for discovery
- 3-lens scaffold for wedge framing
- Outcome Risk Matrix for wedge selection
- Workflow decomposition for agent boundary drawing
- 4-dimensional testing for eval suite design
- Trusted Advisor formula for customer-relationship work

See [`frameworks-applied.md`](frameworks-applied.md) for how each was used in this specific engagement.

## What I'd build next

[One paragraph — what's the next wedge for this customer, the next domain you'd port the pattern to, or the next skill you'd build before the next engagement]

## License

MIT. Synthetic data only — no real customer information.
```

## What NOT to put in the portfolio

| Don't | Why |
|---|---|
| Raw discovery interview transcripts | Process artifact, not interview signal. Synthesize into the discovery memo. |
| Every stakeholder session note | Too much; pick 2-3 representative ones (e.g., the lead-user 20-draft review + the hostile-skeptic session) |
| Sensitive customer info | Synthetic data only. Generic personas. |
| Your half-finished v2 ideas | The portfolio is what you shipped, not what you imagined |
| Boilerplate scaffolding | The interviewer is looking for what YOU owned vs what was pre-existing. Make this explicit. |
| Vendor-pitch language | "Revolutionary AI-powered insights" reads as marketing. State what the agent does plainly. |

## The "frameworks-applied" doc

This is the single most distinctive doc in your portfolio. Most candidates have a case study; few have a frameworks-applied doc.

### Template

```markdown
# Frameworks Applied — [Customer Case Name]

> Specific moments in the engagement where I deployed each framework, what
> the framework forced me to do, and what I learned about the framework's
> limits.

## 4-Source Convergence (Discovery)

**Where I used it**: Day 1, before any solutioning. I triangulated 4 sources:
- Buyer ([CCO Maria]): said the problem was [X]
- Brief: said the problem was [Y]
- Industry: peers were solving [Z]
- Operator ([senior analyst Priya]): said the bottleneck was [W]

**What it forced**: I rejected the buyer's framing of the problem because
the operator's framing pointed at a different bottleneck. The wedge I picked
was [the operator's framing].

**What I learned**: [Specific limit or insight about the framework]

## 3-Lens Scaffold (Solution Strategy)

**Where I used it**: [...]

**What it forced**: [...]

**What I learned**: [...]

## [Continue for each framework you used]
```

This doc is 1-2 pages and reads in 4 minutes. It signals **methodological maturity** — you didn't improvise the engagement, you applied a known pattern with judgment about its limits.

## The "FDE signal" — what interviewers grade

The portfolio is graded on 5 dimensions (same as the rubric in this repo):

| Dimension | What the portfolio should show |
|---|---|
| Customer-first framing | Discovery memo names stakeholders by archetype + emotional state |
| Agent architecture judgment | Prototype shows hybrid det+LLM with named tier choices |
| Production thinking | Eval suite with pass^k=5 + audit trace + run-book |
| Risk surfacing | Field memo names risks in 3 buckets with detection signals |
| Communication | The README is scannable; the artifacts are reviewable in 10 minutes |

If you're missing one of these, that's your highest-leverage polish work.

## Using the portfolio in an interview

### When the interviewer asks "tell me about a relevant project"

Open with the FDE signal, then walk them through the README:

> "I built a 4-week engagement for a fictional hedge fund — Helix Capital — to automate the morning-after-earnings analyst note. The wedge was citation-grounded drafting with senior-analyst review; the architecture was 7 agents, hybrid det+LLM, MNPI Scrubber as the first deterministic gate. The interesting non-obvious move was the hostile-review session with the silent-skeptic trader in week 3, which surfaced three architecture changes that would have hit production in week 5 otherwise.
>
> Full case study is at [github URL]. I can walk you through the architecture or the customer-engagement work — your call."

That's 45 seconds. It opens with the architecture (technical signal), names the engagement structure (FDE signal), and offers the interviewer the choice of deep dive (signals you're comfortable in either direction).

### When the interviewer says "show me where this breaks"

Walk them to the failures section of your eval results + the retrospective. Be specific:

> "Three places this breaks today. First, the eval suite passes 96% weighted, but the 4% failure is on adversarial competitor-injection cases — the deterministic post-processor catches them but the upstream pattern-detection in the drafter doesn't. Second, the tone-shift detection is calibrated against 50 pairwise samples; below 100 samples the calibration has high variance per ticker. Third, the run-book covers the 8 common-mode failures we found in week 3-4; the rare-mode failures (a Bloomberg API contract change, for example) would require operational triage that's not documented."

This is high-status. You're telling the interviewer where to push without being asked.

## Common interview probes the portfolio defends

| Probe | Defense |
|---|---|
| "What did you actually own vs scaffold?" | The README distinguishes; the architecture decisions are documented in the wedge proposal; the agent code commit history shows you wrote it |
| "How do you know it works?" | Point at the eval results + audit trace renderer output |
| "Walk me through a specific decision" | Pick one architecture choice and walk through tradeoffs (e.g., why deterministic citation verifier vs LLM-as-judge) |
| "What would you do differently?" | The retrospective + the field memo answer this with structure |
| "How would this scale?" | Point at the platform-boundary doc + the per-tier integration ladder |

## How long packaging the portfolio takes

If you've completed a full 4-week engagement: **4-6 hours**.

- 1 hour: polish discovery memo (remove process noise; emphasize the moves)
- 1 hour: polish wedge proposal (lead with the principle, then the architecture)
- 1 hour: prototype README + scripts cleanup
- 1 hour: write the case study README (the 1-page pitch)
- 1 hour: write the frameworks-applied doc
- 0.5 hour: filled-out retrospective
- 0.5 hour: optional 5-min video walkthrough

If you haven't run the engagement: the portfolio packaging time is 0 hours because there's nothing to package. Run the engagement first.

## License + IP considerations

If you used this repo's scaffolds as a starting point:
- Add a "Built on top of [github.com/kalyvask/fde-simulation](https://github.com/kalyvask/fde-simulation) — MIT" line in your README
- Make sure your own contributions are clearly distinguished (commit history works)
- Synthetic data only — never put real customer information in the portfolio

If you ran the engagement on your own case (not Calder/Helix):
- Anonymize all customer details
- Use fictional company names + personas
- The repo at fde-simulation is MIT; your derivative work can be any license you want
