# Coverage Map — What This Repo Exercises vs Real Interview Loops

> One page. Read in 3 minutes. Find the simulation that targets the round you're prepping for.

## Why this exists

The repo has 4 simulation formats and 11 frameworks. Candidates ask: "I have an OpenAI Deployed PM final round in 2 weeks — which simulation should I actually run?" This map answers that.

Two axes:
1. **Which simulation format covers which interview signal** (the matrix below)
2. **Which company/role each format calibrates against best** (the second table)

If a row is empty in the matrix, that signal is not covered by that format. Pick the format that covers the most signals on your loop.

---

## Coverage matrix — simulation format × interview signal

Legend: `█` = primary coverage (deliverable proves it), `▒` = secondary coverage (touched but not the main test), blank = not covered.

| Interview signal | 1. Full engagement (20-40h) | 2. Take-home 5h + Review | 3. Recommendation 60min | 4. Client simulation 20-30m |
|---|---|---|---|---|
| Customer discovery + stakeholder mapping | █ | ▒ | ▒ | |
| 4-source convergence (Buyer / Brief / Industry / Operator) | █ | █ | ▒ | |
| Wedge selection on Outcome Risk Matrix | █ | █ | █ | |
| 3-lens scaffold application | █ | █ | █ | |
| Agent workforce decomposition (5-8 agents with shapes) | █ | █ | █ | |
| Model-vs-application-layer tagging | █ | █ | █ | |
| Hybrid deterministic + LLM discipline | █ | █ | | |
| Working prototype that runs end-to-end | █ | █ | | |
| Weighted eval suite + pass^k=5 | █ | █ | ▒ | |
| Adversarial eval cases per risk | █ | █ | | |
| Audit trace + observability design | █ | ▒ | ▒ | |
| Production sign-off criteria + named owners | █ | ▒ | █ | |
| Field memo / lab-feedback synthesis | █ | | ▒ | |
| Defending build choices verbally (Review round) | █ (via oral grill) | █ | █ | █ |
| Hostile customer de-escalation | ▒ | | | █ |
| Silent-skeptic stakeholder conversion | █ | ▒ | | █ |
| Behavioral story bank (5 required types) | ▒ | ▒ | ▒ | █ |
| Strategy and competitive positioning under pressure | ▒ | ▒ | █ | █ |
| Speed under a hard clock | ▒ | █ | █ | █ |
| Portfolio artifact suitable to submit | █ | █ | | |

**How to read this**: if your loop is "60-min final round only," sim 3 covers everything you need. If your loop is "5-hour take-home then 1-hour review," sim 2 was built for that exact shape. If your loop is "4-week paid trial" or "two onsites with a take-home", sim 1 is the only option that produces a portfolio piece deep enough to defend.

---

## Calibration — which role each simulation targets best

| Role / company archetype | Best sim format | Best case | Why |
|---|---|---|---|
| OpenAI Deployed Product Manager (Codex) | Sim 1 full engagement | Calder | Multi-stakeholder regulated deployment; closest to a strategic-account Codex rollout |
| OpenAI Deployed Product Manager (any vertical customer) | Sim 1 full engagement | Calder or Helix | Both cases test deployment craft; pick the domain that matches the customer the role targets |
| Anthropic Applied AI / Solutions Architect | Sim 2 take-home + sim 4 client simulation | Helix | Anthropic loops are known to include take-homes plus a customer-handling round |
| Anthropic Forward Deployed Engineer | Sim 1 full engagement | Both, sequentially | The FDE role assesses end-to-end ownership; running both cases proves domain portability |
| Sierra AI Agent Engineer | Sim 2 take-home + sim 4 client simulation | Calder | Sierra's product is voice/text customer ops; Calder's FNOL workflow is the closest analog |
| Palantir Forward Deployed Engineer | Sim 1 full engagement | Both, sequentially | FDE-archetype role; Palantir originated The Delta Concept used in this repo |
| Scale AI Forward Deployed | Sim 2 take-home | Either | Scale loops are eval-heavy; the take-home Review round mirrors their format |
| Generic AI startup Solutions Engineer | Sim 3 recommendation 60min | Either | Most startup interviews are conversation-only; sim 3 is the dress rehearsal |
| Internal AI platform PM at a Fortune 500 | Sim 1 full engagement (skip-ahead) | Match the domain | Internal deployments rhyme with FDE work; use SKIP_AHEAD to compress |

---

## Coverage gaps the repo does NOT close

Be honest about what this repo doesn't simulate. If your loop has these signals, prep for them separately.

| Gap | Why this repo doesn't cover it | What to do instead |
|---|---|---|
| Live whiteboard system design (60 min, one prompt, drawn architecture) | The repo's design work happens at desk pace, not whiteboard pace | Practice DASME / C.A.S.E. on a whiteboard with a friend; use `tools/agent_design_practice.html` standalone |
| Algorithmic coding (LeetCode-style) | The repo's coding is product code, not interview puzzles | LeetCode / NeetCode separately; not a real FDE signal anyway |
| Live API design under a clock | The prototypes have APIs but they're built at desk pace | Pair with a partner and design an API for a thrown-in customer brief in 45 min |
| Pure ML modeling depth (training, eval design, paper-reading) | The repo is application-layer first | Read the papers in [`READING.md`](READING.md) and practice the Annotated Transformer |
| Compensation negotiation | Out of scope | levels.fyi + a recruiter conversation |
| Executive-presence / C-suite stakeholder presentation skills | The role-play covers it partially via Maria and Sarah personas | Toastmasters; record yourself on a 4-slide deck delivery; the Review round in sim 2 is the closest in-repo proxy |

---

## How to actually use this map for a real loop

Two-step decision:

**Step 1 — pick the matching sim format**: find your loop shape in the calibration table above. If the loop is hybrid (e.g., 1 take-home + 1 onsite + 1 final), use the format that matches the heaviest round.

**Step 2 — pick the matching case**: domain match beats domain mismatch by a lot. Insurance loop, run Calder. Finance / research / data-product loop, run Helix. Cross-domain loop, run both sequentially (sim 1 first, then SKIP_AHEAD the second).

If you have less than a week, sim 2 take-home is the highest signal per hour. If you have 4 weeks, sim 1 full engagement on the domain-matched case produces a portfolio piece the interviewer can read in 10 minutes.

---

## Where each new feature lives in the repo

The features that turn this repo from "practice" into "credential":

| Feature | Lives in | What it does |
|---|---|---|
| **Verifiable scoring per artifact** | [`scoring/grade.py`](scoring/grade.py) | Numeric score per phase (out of 15) + structured diff vs reference |
| **Expert traps per case** | [`simulations/1-full-engagement/<case>/EXPERT_TRAPS.md`](simulations/1-full-engagement/) | 5 traps a real FDE catches; post-mortem reveals which ones you walked into |
| **5-minute hostile oral grill** | [`simulations/1-full-engagement/<case>/ORAL_GRILL.md`](simulations/1-full-engagement/) | Rapid-fire defense of your build choices under pressure |
| **Artifact bundle exporter** | [`scoring/bundle.py`](scoring/bundle.py) | Packages your engagement into a single submittable Markdown pack |
| **Post-mortem checker** | [`simulations/1-full-engagement/POST_MORTEM_PROMPT.md`](simulations/1-full-engagement/POST_MORTEM_PROMPT.md) | Claude prompt that reads your artifacts and flags which traps you walked into |

Each of these is referenced from the simulation it serves so you don't have to remember they exist.
