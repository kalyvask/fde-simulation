# Simulation 3: 60-Min Recommendation Interview (~1 hour)

> The high-level structural conversation format. No build, no take-home. One hour to demonstrate FDE thinking on a cold case.

## What this simulation tests

Whether you can deploy the FDE frameworks (4-source convergence, 3-lens scaffold, Outcome Risk Matrix, 4-dimensional testing) on a fresh case in 60 minutes, structuring Discovery + Solution Strategy + Risk under time pressure.

## The format

| Time | Section | What you do |
|---|---|---|
| 0:00–0:03 | Open | Propose time allocation; restate the case in one sentence |
| 0:03–0:23 | Discovery Approach | Stakeholder map; information needed; 4-source convergence; first 3 days plan |
| 0:23–0:48 | Solution Strategy | 3-lens scaffold; wedge selection on the Outcome Risk Matrix; agent decomposition; integration patterns; cost/latency budget |
| 0:48–0:55 | Risk & Validation | 5-7 risks bucketed (Business / UX / Technical) with detection signals; 4-dimensional testing framework; 3 sign-off criteria |
| 0:55–1:00 | Reverse Q&A | 2-3 sharp questions referencing the interviewer's team / company |

## What's in this folder

| File | Purpose |
|---|---|
| `playbook.md` | The full 60-minute playbook with frameworks, points to land, predictable probes, anti-patterns, PM behavioral probes, a Sentinel Software (B2B SaaS support automation) mock case worked end-to-end, and a "common case shapes" section that covers the 5 structural patterns most FDE cases fall into |
| `ai_logic_doc_template.md` | Template for the strategist-to-FDE handoff artifact. 1-2 page structured doc that engineering uses as the input contract. Common in AI workforce platforms where the FDE is far from discovery. |

## How to run this simulation

### Solo, with Claude as the interviewer

1. Read `playbook.md` once end-to-end to internalize the structure
2. Open a fresh Claude Code chat
3. Paste the playbook content, plus a case prompt (use the Sentinel mock case at the end of the playbook, or write your own)
4. Ask Claude: "Play a Forward Deployed Engineer interviewer at [company]. Run a 60-min Recommendation Interview on this case. Push back on every load-bearing choice. Score me against the rubric at the end."
5. Run the interview
6. Self-grade against the rubric

### With a peer

1. Both read `playbook.md`
2. Peer picks a fresh case (any domain)
3. They run the 60-min interview; you defend
4. They grade against the rubric

## What "good" looks like

By 60 minutes you should have:

1. Restated the case in one sentence at the open
2. Named 6-8 stakeholder archetypes including the silent skeptic
3. Used 4-source convergence by name
4. Filled a 3-lens table out loud
5. Scored 3-5 candidate wedges on the Outcome Risk Matrix
6. Named 5-8 specialized agents with shapes
7. Named 3 integration tiers (read-only → approval-gated → autonomous)
8. Listed risks in 3 buckets (Business / UX / Technical) with named owners
9. Named pass^k=5 as the production threshold
10. Closed with 2-3 sharp questions about the interviewer's team

If you hit all 10, you're at the FDE final-round bar for this format.

## Note on the format

This is the format the company and similar AI-workforce platforms use. It's also the format for early-stage onsites at OpenAI / Anthropic / frontier AI labs (before the take-home round). The 5-hour take-home version (sim 2) is the next round up; the full engagement (sim 1) is what the actual job looks like.
