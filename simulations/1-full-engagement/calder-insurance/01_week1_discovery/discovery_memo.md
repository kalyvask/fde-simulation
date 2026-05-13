# Discovery Memo — Calder Specialty Insurance / FNOL AI Workforce

**From**: FDE Lead
**To**: Maria Vasquez (CCO), Greg Hadley (SVP Claims Ops)
**Re**: Synthesis from Week 1-2 discovery; current state, opportunity, constraints, what's next
**Companion artifact**: `wedge_proposal.md`

> This memo synthesizes 8 stakeholder conversations + the kickoff with Maria. The wedge proposal lives in a separate document. Both arrive together as agreed.

## Headline

The asked problem (cut claims-ops cost 30% in 18 months) and the real problem (the comms-layer pattern that triggered Q4's two market-conduct findings) are the same problem viewed from different seats. The wedge that addresses both: an AI workforce that auto-acknowledges incoming FNOL claims and drafts first-status-updates, scoped to web + agent-portal channels for first-party physical damage. The wedge runs from intake to first-touch. It does not make coverage decisions in v1. The wedge directly attacks the failure mode eating the LAE ratio and exposing Calder to regulatory risk.

## What I heard, by stakeholder

### Maria Vasquez, CCO

The kill-criteria is concrete. **(1)** A market-conduct finding from any state DOI tied to an AI-assisted decision ends funding. **(2)** LAE ratio failing to move 50bps by year-end ends second-year scope. The first scares her more than the second: *"the number we can wait for, the finding we can't."*

Political map: Greg is the title, Priya is the day-to-day owner; Marcus must be at the design table from week 1; Kevin Park is a quiet operator with 22 years and BPO loyalty (do not lead with "we're replacing the BPO"). Rachel will not engage on data without the one-pager.

Adjuster framing: *"less time on routine intake means more time with the claimants who need the judgment call."* Never "automation," never "30% cost reduction" (translates internally to "headcount").

### Greg Hadley, SVP Claims Ops

Confirmed Maria's read on Priya. He's in budget cycle through July; Priya owns daily, he owns wedge sign-off. He flagged something Maria didn't: **the BPO sends "weird" claims back to internal staff without flagging**, which compounds the leakage problem and is invisible from the BPO QA reports. He volunteered Janet (senior adjuster, runs the team chat, 14 years) as the most influential frontline voice — she'll either champion or torpedo adoption.

### Priya Shah, Director FNOL Operations

The workflow walk surfaced three facts not visible from the strategic level:

1. **The BPO sends acknowledgments on a 4-6 hour delay.** The first state-DOI finding pattern was triggered there: a claimant filed via web at 2:14pm Friday, was acknowledged 96 hours later — against a 24-hour state SLA.
2. **Web and agent-portal claims have clean structured fields and narratives.** These are the easiest channels to start with both technically and politically (no phone-transcript dependence).
3. **Priya's team maintains a side spreadsheet** that flags claims sitting >24h with no status update. She'd love to retire it. It's a perfect baseline: replicate its catch rate first, then improve.

She named 4 adjusters for week 1: Janet (senior, skeptical, must win), Mark (mid-career, pro-tech, vocal advocate-in-waiting), Sarah (junior, will adopt anything that works), Hassan (mid-senior, runs BPO QA review meetings, has the institutional view of comms failures).

### The 4 adjusters (Janet, Mark, Sarah, Hassan)

Patterns across all four interviews:

- **The dragon**: bodily-injury claims. None would trust an AI to communicate with a claimant on a BI claim until 12+ months of clean track record. Comp/collision/PD they'd accept day one.
- **Trust criteria for an AI flag** were consistent: (1) show the source narrative span, (2) show the policy reference, (3) show model confidence, (4) one-click escalation that doesn't punish the adjuster for using it.
- **Repetitive work to retire**: routine acknowledgment messaging, status-update copying-and-pasting, asking the system for policy details that should auto-pull.
- **Judgment work to preserve**: total-loss decisions, BI severity calls, fraud-pattern recognition, anything where empathy with a distressed claimant matters.

Janet, verbatim: *"I don't mind if a bot sends the first message. I mind if the bot sends the wrong message. Show me you can write a comm that I'd be willing to put my name on."* This is the wedge's success criterion.

### Tom Reilly, Quality / Audit Lead

Walked through the two findings in detail.

**Finding 1 (NJ DOI, Q4)**: claimant filed FNOL via web, 2:14pm Friday. BPO sent acknowledgment Tuesday at 11:08am — 96-hour delay against 24h state SLA. Acknowledgment also gave a 30-day resolution timeline that was not policy-aligned (the policy was on a 14-day track for that LOB). Examiner cited "delayed and misleading communication."

**Finding 2 (PA DOI, Q4)**: similar pattern. BPO acknowledged within SLA but the ack referenced a wrong deductible amount, then was not corrected for 11 days.

Tom's audit standard for an AI-touched closed file: every comm needs (a) a verifiable reference to the policy field that supports any number cited, (b) a timestamp, (c) a tracked compliance flag for state-mandated SLA windows.

He named **Sienna** (analyst on his team) as the right week-to-week partner; she'll pull the 50-case eval set: 30 well-handled, 15 finding-pattern, 5 hardest-edge.

### Marcus Hill, Compliance Officer

Disarmament worked. Opening with "I'm here to learn your bar before I propose anything" reframed the conversation. The bar Marcus articulated:

- **State-by-state**: NJ, PA, NY, MA are the strictest on FNOL acknowledgment timing. CT and RI are stricter on bodily-injury comms specifically. The other 8 states are looser.
- **Unfair Claims Settlement Practices Act** bites hardest on (1) timeliness, (2) accuracy of stated policy terms, (3) good-faith attempt to resolve. The wedge must hit all three.
- **Human-in-the-loop floor**: NJ + NY require a human-licensed adjuster on the *coverage decision* — not the acknowledgment. v1 wedge does not touch coverage, so we're clear.
- **Audit-trace standard for an AI-touched file**: every decision must show inputs, rule applied, output, and the human who reviewed (if any).
- He volunteered to share his **policy-library document** in SharePoint.

He named **Devorah** (compliance liaison on his team) as the right week-to-week design partner. He committed to a 30-min biweekly with me starting week 3.

### Anil Gupta, CIO

Footprint summary:

- Guidewire ClaimCenter v10 with 4 major customizations (custom routing, BPO handoff, payment authority, fraud signals).
- **APIs exposed** via internal gateway: claim retrieval, policy lookup, status update.
- **APIs behind the gateway** (slow approval): direct DB, payment system, ClaimCenter admin endpoints. Not needed in v1.
- **Sandbox**: dev tenant exists, last refreshed 6 months ago. Usable for v1.
- **Integration queue**: 6 weeks. Anil will fast-track us if we scope read-only on Guidewire (no writes back). We will.
- **Scar tissue**: 2023 RPA project killed at month 9 because maintenance cost > savings. Anil is wary of any pattern that looks similar. Our differentiator: audit traces by design.
- **BAA**: Anthropic in place. OpenAI in procurement.
- **Observability**: Splunk for prompt/response logs; ELK for app logs.

He named **Kayla** (senior integration engineer, ex-Palantir) as the week-to-week partner.

## Current-state workflow (the actual map)

```
[FNOL channel]
    ↓
[Guidewire intake form / IVR / email parse]
    ↓
[Routing rule]
    ↓
[Tier-1 BPO  OR  internal queue]
    ↓
[Acknowledgment sent]   ← (state SLA: 24h. Current avg: 4.2h on phone, much worse on web/email)
    ↓                       (BOTH market-conduct findings happened here)
[First-status-update]
    ↓
[Adjuster touch]
    ↓
[Decision / payment / close]
```

The two market-conduct findings both occurred at the **acknowledgment + first-status-update** band — exactly where the wedge will sit.

## The opportunity (sized)

Web + agent portal = 37% of FNOL volume = **~220 claims/day**.

If the wedge gets median FNOL → first-touch from 4.2h to <30min on this slice and addresses the comms-layer audit-trace requirements:

- **LAE ratio**: estimated 15-25bps on the slice in v1, scaling to ~50bps when the pattern extends to email and phone in months 5-9.
- **BPO replacement potential**: ~$2.5M-$3.5M annual on the slice.
- **Regulatory exposure**: directly attacks the comms-layer finding pattern.

These are deliberately conservative estimates. We will replace estimates with eval-derived numbers by week 5.

## Constraints (named)

| Constraint | Source | Design implication |
|---|---|---|
| 4 strict state DOIs (NJ, PA, NY, MA) on comms timing | Marcus | State-aware policy library, deterministic rules per state |
| BI claims out of v1 | Adjusters + Marcus | Wedge excludes BI; expansion gated on track record |
| Read-only on Guidewire in v1 | Anil | Agent drafts; adjuster (or workflow) commits |
| RPA scar tissue | Anil | Lead with audit traces; differentiate from RPA |
| No PHI | Rachel + Marcus | BI exclusion handles this |
| Adjuster trust gap | All 4 adjusters, Janet specifically | Trust criteria designed in (source span, policy ref, confidence, one-click escalate) |
| 6-week integration queue | Anil | Fast-track via read-only scoping; on queue by week 3 |

## Risks already visible

1. **Janet's adoption** is the biggest political risk. She'll either champion or torpedo. Mitigation: she reviews 20 sample drafts in week 3; her sign-off becomes an internal milestone.
2. **State-by-state regulatory variance** is design complexity. Mitigation: state-aware policy library; rollout order from loose-state to strict-state.
3. **Hallucinated claim detail** is the #1 technical risk. Mitigation: deterministic field extraction; LLM only synthesizes narrative; tone supervisor; compliance critic; audit trace.
4. **6-week queue collision with Anil's other initiatives**. Mitigation: read-only scoping, demonstrably ship-ready by week 3.
5. **BPO political reaction (Kevin)**. Mitigation: positioned as augmenting (BPO retains phone overflow + the 20% adjuster queue); Kevin debrief in week 3.

## What we need next

| Ask | Owner | Date |
|---|---|---|
| Rachel sign-off on data one-pager | Maria → Rachel | Friday this week |
| Greg + data team: 500-claim pull | Greg + data team | EOD Tuesday next week |
| Marcus policy-library SharePoint access | Marcus | EOD Friday |
| Anil + Kayla integration scoping session | Anil | Wednesday next week |
| Sandbox access (Guidewire dev tenant) | Anil + Kayla | Wednesday next week |
| Sienna eval-set delivery (50 cases) | Tom → Sienna | end of next week |
| Janet 20-draft review | Priya → Janet | Week 3 |
| BPO comms volume + delay data, last 90d | Greg + Kevin | Wednesday next week |

## The wedge

Detailed in `wedge_proposal.md`. Headline: auto-acknowledgment + first-status-update for first-party physical damage FNOL claims, web and agent-portal channels first; 80% straight-through processing; full audit-trace artifact; ship-ready end of week 4.

— Alex
