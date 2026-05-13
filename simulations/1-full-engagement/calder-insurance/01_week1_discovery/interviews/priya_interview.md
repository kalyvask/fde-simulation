# Priya Shah — Director, FNOL Operations — Wednesday 9:00am ET, Zoom (45 min)

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** This is a constructed dialogue showing what the senior version of this interview would look like IF the comms-layer wedge hypothesis holds. The methodology (workflow walk, political map question, locking the wedge validation) is the template. The dialogue itself is constructed. Real Priya may surface different facts. Use as "what good looks like" learning material, not as engagement data.

## Setup

Wednesday 9:00 AM ET. Priya picked the time herself — between her 8am ops standup and her 10am BPO check-in. Zoom; she has her camera on. Second monitor visible behind her with what looks like a Kanban board of open claims. Friendly but visibly busy.

## Selected exchanges

**Alex** *(opening)*: "Priya, thanks for the time. Maria told me the actual workflow lives in your head, not in any deck. So I'd like to spend most of the 45 minutes on a workflow walk. If we don't get to anything else, that's fine — that's the most valuable thing I'd take from this. Sound OK?"

**Priya**: "Sounds great. Maria's exact words about you were 'he respects the work.' We'll see. Where do you want to start?"

**Alex**: "Pick a real claim from yesterday. Walk me through every step it went through, every system it touched, every decision someone made. Take as long as you need; I'm going to mostly listen and write."

**Priya** *(15-min walk, with detail)*: "OK. Real one from yesterday. Commercial auto, fleet customer in NJ, fender bender at a UPS distribution center. Came in via the agent portal at 11:42am. Routing rule kicked it to BPO L1 because it was under $5K estimated and not bodily-injury. BPO timestamped 'received' at 11:43, which is automatic. The actual human at the BPO opened the file at 3:18pm — 3.5 hours later. They sent the acknowledgment at 4:02. So claimant submitted at 11:42, got acknowledged at 4:02. Four hours twenty minutes. State SLA in NJ is 24 hours so technically we're fine, but the customer experience is awful. For comparison, our internal team would have acknowledged within 30 minutes of opening it. Then the BPO ran the policy check, confirmed coverage, queued the auto repair shop assignment for tomorrow morning's batch — so the customer waited overnight for that touch too..."

*(Detail continues: the $5K threshold logic, the routing rule's blind spot for fleet customers with multiple recent claims, the comm template that hasn't been updated since Q1, the manual override Priya's team has to do when a claim crosses tier thresholds mid-week.)*

**Alex** *(after she's done, taking a beat)*: "Two things I want to dig into. First — the bottleneck isn't the writing of the acknowledgment, it's the time between submit and someone opening it. What drives that on the BPO side?"

**Priya**: "Their queue triage. They batch claims by LOB and have one person who triages every 4 hours. So a claim that comes in at 11:42 doesn't get looked at until the 1pm or 4pm triage cycle. We've asked them to go to hourly. They won't because it would require staffing changes."

**Alex**: "And on the comms quality — you said your internal acknowledgment is better. Show me a side-by-side?"

**Priya** *(pulls two examples on screen, reads aloud)*: "BPO version: 'Dear Customer, We have received your claim. A representative will contact you within 30 days. Reference number: CL-2025-NJ-44218.' Generic. The 30 days is wrong for this LOB — should be 14. Internal version: 'Hi Mr. Patel, this is Sarah from Calder Claims. I've received your fleet incident from yesterday at the Edison distribution center. I'll have an estimate appointment scheduled for you by Wednesday morning. Call me at 555-1234 if anything about your fleet operations changes in the meantime.' Named, references the actual incident, real timeline, a person."

**Alex**: "OK that's super useful. Question — does your team maintain anything to manually catch where the BPO drops the ball?"

**Priya** *(small pause)*: "Yeah. We have a side spreadsheet. Hassan built it. It pulls FNOL records every hour and flags anything that's been sitting more than 24 hours without a status update. We work down the queue manually. Catches maybe 80% of the worst ones. But it's a Hassan-only system — if he's out, it doesn't run. And the spreadsheet doesn't catch comms-quality issues, only timing."

**Alex**: "That's gold. The first version of what we build should at minimum replicate that catch rate so you can retire the spreadsheet. Hassan should be the first adjuster I talk to."

**Priya**: "He'd love that. He's the one who's going to make this work or not, honestly. Janet has the seniority but Hassan has the institutional knowledge of what's broken."

**Alex**: "Tell me about Janet. Maria mentioned her name with weight."

**Priya**: "Janet's been here 14 years. Runs the team chat. Senior in years and in influence. Also the most skeptical person on my floor. We had an RPA project in 2023 — Anil was involved — and she effectively killed it. Quietly. People kept routing around it until adoption was 12% and they killed the project. If she doesn't trust your thing, it's dead. If she does, she'll make sure her team uses it."

**Alex**: "So Janet's the must-win. Who would you put in front of me first — Hassan because he knows what's broken, or Janet because winning her sets the political path?"

**Priya**: "Hassan first. You'll learn more from one Hassan conversation than three Janet conversations. Then Janet, after you have something concrete to show her."

**Alex**: "Of your 180 adjusters, who else should be in the first 5 I talk to?"

**Priya**: "Janet (must-win, senior, skeptical). Hassan (institutional, your tech ally). Mark (mid-career, pro-tech, will be your vocal advocate in the team chat once he's bought in). Sarah (junior, 18 months tenure, will adopt anything that works and gives you the early-career view). And Linda, who handles the BI claims. We won't touch BI in v1 but she'll tell you the rules of the road for when you eventually do."

**Alex**: "Anyone about to leave? Energy I shouldn't invest in?"

**Priya**: "Janet's been talking about retirement for two years. Probably another 12-18 months. The other four are stable."

**Alex**: "Last one. From your seat — what's the wedge that would make the biggest difference in 60 days?"

**Priya**: "Web and agent-portal claims sit in the queue too long. If you can move time-to-first-touch on those from 4 hours to half an hour, my LAE leaks shut down and customer NPS pops. Phone is a different beast — the BPO call agents are decent at the live ack on phone, the failure mode there is the follow-up status update. So I'd say first wedge is web and agent-portal acknowledgment + first status update."

*(That validates the wedge hypothesis Maria steered toward.)*

**Alex**: "That matches what Maria signaled. I'll go test it with Hassan and Janet, then come back to you Friday with the wedge proposal. Housekeeping — should our standing weekly mirror Maria's Friday 4:15, or pick a different slot?"

**Priya**: "Mirror is fine. I'll be on hers anyway."

**Alex**: "And — send me the adjuster intro email by Thursday EOD before I send it to anyone. I want to make sure the language doesn't trigger Janet's union antenna."

**Priya**: "Will do. Talk Friday."

*(Call wraps at 43 minutes.)*

## Post-interview captures

### Glossary updates
- **LOB**: line of business
- **FNOL**: first notice of loss
- **BPO L1**: tier-1 BPO handler
- **LAE**: loss adjustment expense
- **Triage cycle**: BPO's batched 4-hour intake review
- **BI**: bodily injury
- **Comp / Collision / PD**: coverage types
- **Routing rule**: deterministic logic that sends claims to BPO L1, internal L2, complex, or SIU based on dollar threshold and LOB
- **Subro**: subrogation (recovery from at-fault third party)

### Stakeholder map updates
| Person | Power | Stance | Operating note |
|---|---|---|---|
| Priya | HIGH (daily operator) | ALLY | Validated as champion. Mirror Maria's Friday 4:15 |
| Janet | HIGH (informal) | SILENT SKEPTIC, possible blocker | Killed RPA 2023; possible retirement 12-18mo. Must win. |
| Hassan | MEDIUM | TECH ALLY | Built the side spreadsheet. Talk to first. |
| Mark | MEDIUM | ADVOCATE-IN-WAITING | Mid-career, pro-tech |
| Sarah | LOW (individual) | PROBABLE EARLY ADOPTER | Junior, 18mo, will adopt what works |
| Linda | LOW (for v1) | FUTURE-STATE EXPERT | Handles BI; relevant when v2 expands |

### Working hypothesis updates
- Wedge confirmed: web + agent-portal acknowledgment + first status update for first-party physical damage
- Hassan's spreadsheet is the v0 baseline. First demo replicates its catch rate; second demo improves on it
- Sequencing: Hassan (technical reality) → Janet (political win) → Mark, Sarah, Linda (breadth)
- Adjuster intro email needs Priya's redline before going out

### Open questions
- BPO triage staffing economics — what would hourly triage cost vs current 4-hour batch? Relevant to BPO replacement math
- The 2023 RPA project failure detail — Anil interview
- Hassan's spreadsheet logic — direct interview

## Recap email sent (9:55am)

Subject: `[Calder] Priya recap — workflow + adjuster picks`

> Priya — thanks for the time. Three things I'm taking forward:
>
> **1. Wedge confirmation.** Web and agent-portal acknowledgment + first status update for first-party physical damage. You said this would shut the LAE leak; matches what Maria flagged on regulatory exposure. I'll formalize in the Friday wedge proposal.
>
> **2. Adjuster sequence.** Hassan first, then Janet (after I have something concrete to show), then Mark, Sarah, Linda. I'll send the intro email to you for redline before reaching out.
>
> **3. Hassan's spreadsheet is the v0 baseline.** First demo replicates its catch rate; second improves on it.
>
> Adjuster intro email to you EOD Thursday for redline. Standing weekly mirroring Maria's Friday 4:15.
>
> Talk Friday.
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Discovery rigor | 5 | Let her workflow-walk uninterrupted for 15 min |
| Domain learning velocity | 4 | Picked up most terms in real time; missed PD meaning until later |
| Customer-political acuity | 5 | Janet political map landed; sequencing earned via her recommendation |
| Calibrated engineering | 4 | Validated wedge without leading; spreadsheet baseline a smart anchor |
| Outcome ownership | 4 | Locked Friday deliverables; standing weekly should have been my proposal not her question |

**Keep**: opening framing ("the workflow lives in your head"); silence after the workflow walk; the political map question.

**Fix**: should propose standing weekly cadence in the call, not the recap email.
