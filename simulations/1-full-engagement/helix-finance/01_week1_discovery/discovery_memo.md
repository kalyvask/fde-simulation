# Discovery Memo — Helix Capital / Earnings-Note AI Workforce

**From**: FDE Lead
**To**: Sarah Mendez (CIO), David Park (Head of Research)
**Re**: Synthesis from Week 1-2 discovery; current state, opportunity, constraints, what's next
**Companion artifact**: `week-2-solution/wedge_proposal.md`

> Synthesis from 8 stakeholder conversations + the kickoff with Sarah. Wedge proposal lives in a separate document. Both arrive together.

## Headline

The asked problem (compress morning-after cycle from 4h to 30min) and the real problem (the analyst burnout + hallucination-risk pattern that's killing senior-analyst retention and threatening fund reputation) are the same problem viewed from different seats. The wedge that addresses both: a citation-grounded AI workforce that drafts the morning-after analyst note while making hallucinated-number risk architecturally impossible. Drafts only; senior analyst reviews + compliance approves before publication. Scoped to coverage names + standard earnings call format. Directly attacks Sarah's kill-criteria #1 (hallucinated numbers reaching trading decisions) and David's retention problem.

## What I heard, by stakeholder

### Sarah Mendez, CIO / Managing Partner (real call)

Two kill-criteria. **(1)** Hallucinated number in a draft that leaks into a trading decision — fund-reputation damage and potential SEC scrutiny. **(2)** MNPI-handling violation tied to AI processing — 3 years clean, wants to stay that way. The first scares her more: "I can see the path from a single hallucination to a $20M trading loss."

Political map: David runs research day-to-day; Rachel is the must-win senior analyst. Mei is the default-no compliance officer. Aditya owns Snowflake + integrations; James handles infosec without a separate CISO. Carmen on the trading side is downstream user (sees the note; trades against it).

Adoption framing: "less time on routine drafting, more time on the thesis work that PMs actually pay analysts for." Never "headcount reduction" — that lost her 2 senior analysts to BurnoutTransformations Inc already. Standing weekly Fridays 4:30.

### David Park, Head of Research

Confirmed Sarah's read. He runs the coverage book; Rachel sets the bar for what a good note looks like. He flagged that the BPO equivalent at Helix is the **outsourced research support shop** that produces preliminary KPI extracts but with quality issues — extraction errors of 5-10% on edge cases. The senior analyst spends time correcting the support shop's output before drafting.

Volunteered Carmen (head trader, downstream user) as someone who'd be hostile in an early demo: she's been burned by lazy analyst notes before and reads any AI-assisted note with extra skepticism.

### Rachel Kim, Senior Analyst, TMT (simulated — full interview pending)

The Janet of this engagement. 9 years at Helix. The lead user. Will quietly route around the system if she doesn't trust it.

Trust criteria for an AI-generated note (modeled on Janet's bar at Calder):
1. Every number cited must show the exact source span (transcript or 10-Q line reference)
2. KPIs vs consensus must show actual / consensus / delta explicitly
3. Tone-shift summary must name the specific language change, not generic ("more cautious")
4. Risk-factor diff must distinguish new from carry-over risk
5. The note must be one page she'd be willing to send to Sarah without redlining

She'll review 20 sample drafts in week 3 as the rollout gate. <18 send-ready = redesign.

Adversarial inputs she named:
- **Hallucinated guidance**: model invents a guide-up that wasn't given
- **Lawyered-up paragraphs**: management language too clean → suggests legal review → real signal
- **Tone-shift miss**: model gives generic "solid quarter" when management language shifted notably

### Mei Liu, Compliance Officer (simulated — disarmament required)

Default-no per Sarah's warning. Disarmament technique critical (same Marcus pattern from Calder, finance-flavored).

Regulatory bar:
- **SEC**: Reg FD (Fair Disclosure), Reg BI (Best Interest), Section 10(b)
- **FINRA**: research analyst rules (FINRA 2241), communication standards, recordkeeping (3yr min)
- **CFA Institute**: research integrity, fair dealing
- **Internal**: Chinese wall between research and trading; pre-publication review

Three unwritten rules (modeled on Marcus's pattern):
1. **No position-sizing language in drafts** — even hedged. "Recommend long position at 3%" → blocked
2. **No M&A speculation** — even when management hints. Reg FD risk
3. **Every cited number must trace to a source span** — Sarah's kill-criteria #1 enforced architecturally

War story: 2019 case at a different firm where automated KPI extraction missed a guidance update embedded in Q&A. Analyst missed it. Trading desk acted on stale guidance. SEC noticed. $850K consent order + 6-month consent decree. Mei has been gun-shy on AI extraction since.

HITL floor: every note must be reviewed by a senior analyst AND by Mei (or her deputy) before publication. Non-negotiable.

### Aditya Sharma, CTO (simulated)

Helix runs on a Python research stack on Snowflake. Bloomberg + FactSet integrations exist. Slack-based collaboration. No real DevOps team — Aditya does most of it himself with one junior engineer.

Footprint:
- Bloomberg API access (B-PIPE) — read-only via licensed terminal
- FactSet integration — read-only data feeds into Snowflake
- Refinitiv (Eikon) — research-side only
- Snowflake-Python research stack: data ingestion → notebooks → Streamlit dashboards
- No Guidewire-equivalent core system — research is the system

Integration constraint: **read-only on Bloomberg / FactSet** (vendor licensing). MNPI watch list lives in compliance, not in the research stack. **Critical architectural rule**: the AI workforce never touches the trading system. Strict Chinese-wall separation in code.

Scar tissue: 2024 attempt at automated KPI extraction via OpenAI gpt-4 failed because the extraction confidence calibration was wrong — extraction "confidence high" → wrong KPI → analyst missed it. Cost them $4M on a single trade. Aditya is structurally skeptical of LLM extraction without per-number citation grounding.

### James O'Brien, COO (simulated — handles infosec without separate CISO)

PII + MNPI handling. No PHI in scope (no medical). BAA with Anthropic in place; OpenAI in evaluation. Audit retention: 3-year minimum (FINRA standard).

Key concern: **prompt log retention vs MNPI**. If any MNPI accidentally enters a prompt, the logs themselves become contaminated. Mitigation: MNPI Scrubber must run before any LLM call.

Wants a half-page data-handling one-pager (like Rachel one-pager for Calder). Will sign off after review.

### Carmen Diaz, Senior Trader (simulated)

The downstream user / hostile-demo persona. Reads notes; trades against them.

Quality bar from the trader seat:
- "If the note says revenue beat by 3%, I need to know the 3% is real-real, not extracted-from-a-transcript-paragraph-the-model-may-have-misread."
- "The most useful note is one I can trade on at 9:30am without re-reading the transcript myself."
- "Tone shifts matter more to my book than any single KPI miss. If management's language shifted, that's the trade."

She's not a stakeholder I asked to interview, but Sarah will want her in the wedge demo.

## Current-state workflow (the actual map)

```
[Earnings call ends 5pm]
    ↓
[Transcript published ~10pm by Bloomberg / Seeking Alpha / FactSet]
    ↓
[Senior analyst reads at 5-6am: transcript + 10-Q + prior 4 quarters of own notes]
    ↓
[Manual KPI extraction (1-1.5h)] — outsourced shop does this poorly; analyst re-does
    ↓
[Consensus comparison (15 min)] — Refinitiv / FactSet manual lookup
    ↓
[Tone-shift detection (30-45 min)] — cross-quarter manual review
    ↓
[Risk-factor diff (15-30 min)] — MD&A section diff
    ↓
[Draft note (45-60 min)] — synthesis writing
    ↓
[Compliance review (varies: 30 min - 4h depending on Mei's queue)]
    ↓
[Publish to PMs + traders] — target by 9:30am market open
```

Total: 4-5h per name. Often delayed past market open. Sarah's window of alpha decays.

## The opportunity (sized)

- **Direct cost saving**: 1,120 hours/year/analyst × 5 senior analysts × $300/hr fully-loaded = **$1.68M/year**
- **Indirect alpha capture**: median note publication time 4h → <1h post-call = analysts hit the 9:30 trading window
- **Retention saving**: 2 senior analysts lost in 2025; $500-1M ramp cost per replacement = **~$1-2M/year** at current attrition
- **Combined target**: **$2-3M/year** in cost + alpha + retention

These are conservative. Replace with eval-derived numbers by week 5.

## Constraints (named)

| Constraint | Source | Design implication |
|---|---|---|
| 4 regulator stack (SEC + FINRA + CFA + internal) | Mei | Compliance Critic must encode all 4; per-regulator slicing in eval |
| MNPI as hard wall | Mei + James | MNPI Scrubber as FIRST agent; deterministic; blocks before LLM call |
| Chinese wall | Mei + Aditya | Agents architecturally separated from trading systems |
| Hallucinated number = engagement-ending | Sarah's kill-criteria #1 | Citation Verifier enforces every number traces to a source span |
| Read-only Bloomberg/FactSet | Aditya | No writes to data feeds; drafts saved to Snowflake research only |
| Senior-analyst veto | Rachel + David | Her 20-draft review = rollout gate |
| BAA: Anthropic only in v1 | James | OpenAI added once BAA closes |
| 5-person research team capacity | David | Daily cadence with Aditya; weekly with David; Rachel as user trust gate |

## Risks already visible

1. **Carmen's hostility in the wedge demo** — she's been burned. Mitigation: bring her into a focused review session in week 2, not as a surprise stakeholder in week 4.
2. **Mei's calibration on the citation verifier** — false positives could kill analyst trust quickly. Mitigation: per-number type calibration; conservative on dollar values, looser on percentages.
3. **OpenAI BAA delay** — Sarah wants OpenAI in evaluation; if BAA slips, we can't add OpenAI to the workforce. Mitigation: design model-agnostic; swap-ready architecture.
4. **Snowflake-Python research stack lock-in** — Aditya's environment is bespoke. Mitigation: stick to plain Python with minimal Snowflake-specific glue.
5. **Tone-shift detection variance under pass^k** — LLM-as-judge is the noisiest layer. Mitigation: calibrate against SubjECTive-QA + Rachel's hand-graded sample.

## What we need next

| Ask | Owner | Date |
|---|---|---|
| James data-handling one-pager sign-off | James | Friday this week |
| Mei MNPI watch-list export + escalation rules | Mei + Devorah-equivalent | EOD Friday |
| David: 30 historical Helix notes for seed eval set | David | EOD Tuesday next week |
| Aditya: Snowflake schema review + research-stack credentials | Aditya | Wednesday next week |
| Bloomberg + FactSet API doc walkthrough | Aditya | Wednesday next week |
| 5 sample earnings call transcripts (covered names) | David | Friday next week |
| Rachel 20-draft review session | David → Rachel | Week 3 |
| Carmen hostile-review session | Sarah → Carmen | Week 3 |
| Standing weekly with Sarah | Sarah | Fridays 4:30 |

## The wedge

Detailed in `wedge_proposal.md`. Headline: citation-grounded earnings-note AI workforce; drafts only; MNPI architectural wall; Rachel + Mei review before publication; target 4h → 30min on the covered-names slice, with hallucinated-number risk eliminated architecturally.

— Alex
