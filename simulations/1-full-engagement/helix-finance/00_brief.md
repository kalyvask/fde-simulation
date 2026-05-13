# Helix Capital — Customer Brief

> Fictional composite based on real mid-market long-short equity hedge funds. All names, numbers, and quotes are illustrative.

## At a glance

| | |
|---|---|
| Industry | Buy-side equity research; long-short hedge fund |
| AUM | $2.3B |
| Strategy | Fundamental long-short, US large-cap + mid-cap, sector-focused (TMT + consumer + industrials) |
| Coverage universe | ~80 names |
| Team | 12 investment professionals (5 senior analysts + 4 associates + 3 traders) + CIO + COO |
| Ownership | Independent partnership, partners are GPs |
| Tech stack | Bloomberg Terminal, FactSet, Refinitiv, Alphasense, internal Python research stack on Snowflake, Slack |
| Why now | Each senior analyst burns 4h per covered name on the morning-after-earnings note. 80 names × 4 quarters × 4h = 1,280 hours per analyst per year. Earnings season = systematic burnout. Two senior analysts left in 2025 citing this specifically. |

## The presenting problem (Sarah Mendez, CIO / Managing Partner)

> "Our research process is broken at the seam between earnings call and portfolio decision. Senior analysts spend 4 hours per covered name the morning after an earnings call drafting a one-pager that goes to me and the trading team. By the time the note's in my hands, market has moved and our edge is decayed. We're seeing this kill alpha on positions where we were early. I lost two senior analysts last year and the exit interviews both said 'the morning-after grind is unsustainable.' I want to compress that 4-hour task to 30-minute review. The note still gets written. The analyst still owns it. The first draft is just not theirs anymore."

## Stakeholders

| Role | Name (illustrative) | Why they matter |
|---|---|---|
| CIO / Managing Partner | Sarah Mendez | Economic buyer. Owns the burnout problem. PnL pressure from delayed alpha. |
| Head of Research | David Park | Champion. Owns the research process and the analyst team's coverage. |
| Senior Analyst, TMT (lead user) | Rachel Kim | 9 years at Helix. The "Janet" of this engagement — must-win, will quietly route around the system if she doesn't trust it. |
| Senior Analysts (4 others) | sector-divided | Primary users. Will judge by quality of the draft. |
| Associates (4) | various | Currently do parts of the workflow; will need new ownership boundaries |
| Compliance Officer | Mei Liu | Default-no skeptic. SEC + FINRA + CFA Standards. Equivalent of Marcus in Calder. |
| CTO | Aditya Sharma | Owns Snowflake / Python research stack + Bloomberg / FactSet integrations |
| COO | James O'Brien | Handles infosec (no separate CISO at this size). Will demand a one-pager. |
| Senior trader | Carmen Diaz | Downstream user. Receives the note; trades against it. Has views on note quality. |
| External: prime broker / counsel | — | Out of scope for week 1 |

## Current-state numbers

| Metric | Value | Source |
|---|---|---|
| Coverage universe | 80 names | David's coverage book |
| Earnings cycle | 4× per year | SEC filing calendar |
| Notes per analyst per quarter | ~16 (each analyst covers ~16 names) | David |
| Time per note (current) | 4 hours | Sarah's exit-interview data |
| Time per note (target) | 30 min review of a draft | Sarah's stated goal |
| Hours saved per analyst per year | 1,280 → 160 = **1,120 hours** | Math |
| Total team hours saved | 5 analysts × 1,120 = **5,600 hours/year** | Math |
| Note publication latency | Median 4 hours post-call; some up to 18h | David's process audit |
| MNPI incidents | 0 in last 3 years; Mei's job is to keep it 0 | Mei |
| Analysts lost to burnout | 2 in 2025 (out of 7 at start of year) | Sarah's HR data |

## The opportunity (back-of-envelope)

- **Direct cost saving**: 5,600 hours × $300/hr fully-loaded = $1.68M/year in analyst time
- **Indirect alpha capture**: notes published <1h post-call instead of 4-18h post-call → analysts hit the trading window
- **Retention**: stopping the burnout-driven exits saves recruiting + ramp ($500K-1M per senior analyst)
- **Combined target**: **$2-3M/year** in cost + alpha + retention value

## The constraints (named upfront)

- **Regulatory**: SEC (Reg FD, Reg BI), FINRA (research-conduct rules), CFA Institute Standards (research integrity). Internal compliance review required for any published note.
- **MNPI handling**: Material Non-Public Information must never appear in an AI prompt or in any LLM-accessible context. Strict.
- **Chinese wall**: research and trading must remain logically separated. Note generation is on the research side; trading sees the note only after compliance approval.
- **Hallucinated guidance**: a single fabricated revenue number reaching a trading decision = potentially-fund-shutting event. Numerical accuracy is non-negotiable.
- **Citation requirement**: every claim in the note must be traceable to a source span (transcript, filing, or consensus database).
- **Vendor risk**: Anthropic BAA signed (post-Calder learnings); OpenAI in evaluation. Bloomberg + FactSet data licenses constrain what can leave Helix's environment.
- **Senior analyst veto**: Rachel + 1 other senior analyst can veto rollout if drafts don't meet quality bar. Must-win user.

## The kill-criteria (Sarah's words)

> "Two things end this engagement for me. **One**: a hallucinated number in a draft that leaks into a trading decision and costs us money. That's a fireable mistake for the analyst, fund-reputation damage for me, possibly SEC scrutiny if patterns emerge. **Two**: an MNPI-handling violation tied to AI processing. We're 3 years clean. I want to stay that way. The first scares me more — I can see the path from a single hallucination to a $20M trading loss. The MNPI risk is procedural; we can engineer around it. The hallucination risk requires the agent to never invent numbers, full stop."

## The bet (working hypothesis going into Week 1)

The narrowest, highest-impact wedge is the **morning-after-earnings analyst note draft**, scoped to coverage names with standard earnings call format. The agent ingests the call transcript + 10-Q + prior 4 quarters of notes + consensus estimates, then produces a 1-page draft with:
- KPI extraction with citation per number
- Prior-quarter delta on key metrics
- Tone-shift detection (management's language vs prior calls)
- New risk-factor changes (MD&A diff)
- Draft commentary section
- Senior analyst reviews/edits → compliance reviews → published

Excludes:
- M&A commentary (regulatory minefield)
- Position-sizing recommendations (cross-Chinese-wall risk)
- Anything involving non-public information

Target: 4h analyst task → 30-min review. Drafts only — analyst still owns the publication.

This hypothesis is to be confirmed or broken in Week 1 discovery. See `week-1-discovery/discovery_memo.md`.
