# Marcus Hill — Compliance Officer — Friday 2:00pm ET, in-person (45 min)

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** The disarmament technique is the most important moment of this engagement; constructed dialogue captures what it looks like in real time.

## Setup

Friday 2:00 PM ET. Marcus in his office. Polite but reserved. Calendar visibly blocked. Coffee, no notes — he's expecting to listen and react, not to give. Default-no posture.

## Selected exchanges

**Alex** *(opening — THE DISARMAMENT)*: "Marcus, thanks for the time. Maria asked me to bring you in at the design table from week 1, not the approval table at week 4. So I'm not here to show you a design. I'm here to learn your bar. After today I want you to feel I understand the rules well enough that nothing I propose later catches you off guard."

**Marcus** *(visibly relaxes — a beat of surprise)*: "OK. That's not the typical opening. Where do you want to start?"

*(That single line is the disarmament working in real time. Marcus has shifted from gatekeeper posture to design-partner posture in 20 seconds. The rest of the interview rests on this move.)*

**Alex**: "Bar elucidation. State by state if relevant. Where does the Unfair Claims Settlement Practices Act bite hardest for FNOL acknowledgment and first-status-update?"

**Marcus** *(now leaning in)*: "Four states will be your headache: NJ, PA, NY, MA. NJ has the strictest comms-timing rule — 24 hours to ack, 10 days to first substantive status update. PA is similar on timing but stricter on accuracy of stated terms — they'll cite you for any misleading number even if it's caught and corrected later. NY has the most aggressive enforcement — they'll come after you for what they call 'systemic' practice if they see a pattern across more than 2 files. MA is the most procedural — they want documentation of the process, not just the outcomes. The other 8 states are looser but I'd design to NJ standards across the board because that's the easiest mental model and the audit cost is lower."

**Alex**: "Exactly the kind of guidance I needed. Audit-trace standard for an AI-touched file — what does that look like for an examiner?"

**Marcus**: "Inputs the system saw, the rule it applied, the output, whether a human reviewed. Plus — and this is the AI-specific one — confidence at decision time and what the threshold for escalation was. Examiners are starting to ask 'why didn't this escalate' for AI-assisted decisions, and we need to be able to answer with the actual rule, not a post-hoc rationalization."

**Alex**: "Got it. So the routing decision needs a calibrated confidence + a stated threshold visible in the trace. What about the policy library — what's written, and what isn't?"

**Marcus**: "Written: SharePoint, I'll send you the link. State-specific policies organized by LOB. Last updated quarterly. Unwritten — and this is where it gets interesting — there are a few rules of the road that live in my head and Devorah's. (1) On any claim with a child or elderly party, default-conservative — escalate even if the model would auto-send. (2) On any first-time customer, the first comm reads warmer than the BPO standard. (3) On any claim where the policyholder has had a prior claim in the past 12 months, route to a human adjuster regardless of what the model says. Those three are firm policy that lives in my head. We'll get them written down for you as part of this engagement."

**Alex**: "Exactly what I needed. The unwritten rules are usually more important than the written ones because they're institutional knowledge. Two more. The HITL floor — where is a human-licensed adjuster legally required by state?"

**Marcus**: "Coverage decisions in NJ and NY. Nothing legally required for acknowledgment or status update — which is your v1 wedge. So you're clear there. Settlement decisions also require human in NJ, NY, and PA. Any of that, you must escalate."

**Alex**: "War story. Worst regulatory finding you've seen in your career — what changed because of it?"

**Marcus** *(longer pause)*: "2018. Different shop. We had a vendor doing automated claim categorization. It misclassified a hail damage claim as 'cosmetic' instead of 'structural' for a large agribusiness customer in Iowa. The customer's barn collapsed two weeks later because the underlying damage wasn't repaired. We paid $1.2M and got a finding from the IA DOI. What changed: nothing automated touches anything that affects coverage classification without a licensed-adjuster sign-off, ever. That's where my caution comes from. So when I push back hard on something, that's the case I'm thinking about."

**Alex**: "Understood. The wedge explicitly does not touch coverage decisions for that reason. I'll keep that boundary clear in everything we propose. Last one — Devorah is my design partner, you said earlier. What's the right cadence for you and me?"

**Marcus**: "Devorah weekly. You and me biweekly starting week 3, 30 minutes. Sooner if anything changes the design."

**Alex**: "Done. I'll get on Devorah's calendar today."

**Marcus** *(unprompted)*: "One more thing. Take my cell number. *(writes it on a notepad page, slides it across)* If you find yourself about to design something compliance-adjacent and Devorah's not reachable, call me. I'd rather be a 5-minute phone call now than a 5-week redesign in week 4."

*(That cell-number gesture is the strongest possible trust signal from a default-no compliance officer. The disarmament earned it.)*

*(Wraps at 38 minutes.)*

## Post-interview captures

### State-by-state bar (the regulatory map)
| State | Strictest on | Notes |
|---|---|---|
| NJ | Comms timing (24h ack, 10d status) | Design baseline |
| PA | Accuracy of stated terms | Cite even on caught-and-corrected errors |
| NY | Systemic practice patterns | "Pattern across >2 files" is the trigger |
| MA | Process documentation | Documentation > outcomes |
| Other 8 | Looser, but design to NJ standards | Easier mental model |

### The audit-trace standard (Marcus version, complementary to Tom's)
- Inputs the system saw
- Rule it applied
- Output
- Whether human reviewed
- **Confidence at decision time + escalation threshold visible in trace**
- Examiner-readable answer to "why didn't this escalate"

### The unwritten policy rules (newly extracted, will codify)
1. Child or elderly party present → default-conservative, escalate even if model would auto-send
2. First-time customer → first comm reads warmer than BPO standard
3. Prior claim in past 12 months → human adjuster regardless of model output

### HITL floor
- **Coverage decisions**: NJ, NY require human-licensed adjuster
- **Settlement decisions**: NJ, NY, PA require human-licensed adjuster
- **Acknowledgment + status update**: no HITL floor in any state — v1 wedge is clear

### War-story-derived design constraint
- Coverage classification automation killed a customer's barn in 2018 → $1.2M loss → IA DOI finding
- v1 wedge explicitly does not touch coverage; this boundary is non-negotiable
- Design implication: if v2 ever expands to coverage, every coverage decision routes to HITL with the licensed-adjuster floor encoded as a hard rule

### Glossary updates
- **HITL floor**: human-in-the-loop legal floor (state-mandated)
- **Systemic practice**: NY DOI term for patterns across >2 files
- **Cosmetic vs structural**: hail-damage claim classification (the 2018 failure mode)

### Stakeholder map updates
- Marcus: stance shifted from DEFAULT-NO BLOCKER to **DESIGN-PARTNER** (cell number is the proof)
- Devorah: TECHNICAL DESIGN PARTNER, weekly cadence
- Trust signal: Marcus offered cell number unprompted — strongest possible buy-in from compliance

### Working hypothesis updates
- The 4-state strictness map (NJ/PA/NY/MA) becomes the per-state policy library
- The 3 unwritten rules become deterministic guardrails in the compliance critic agent
- Designing-to-NJ-standards across the board simplifies the policy library
- v1 wedge is regulatorily clear (no HITL floor on acknowledgment)
- v2 expansion to coverage decisions is gated on encoding the HITL floor

## Recap email sent (2:55pm)

Subject: `[Calder] Marcus recap — bar I heard, design partnership confirmed`

> Marcus — thanks for the time. Capturing what you gave me, in your own framing:
>
> **You're at the design table, not the approval table.** Devorah weekly; you and me biweekly from week 3. Cell number captured for compliance-adjacent design moments before then.
>
> **The bar**: NJ/PA/NY/MA are the strict states; design to NJ standards across the board. Audit trace shows confidence + escalation threshold for every AI decision. HITL floor doesn't apply to v1 (acknowledgment + status update).
>
> **Three unwritten rules** I'll encode as deterministic guardrails: (1) child/elderly party → conservative, (2) first-time customer → warmer first comm, (3) prior claim in 12mo → human adjuster regardless of model output.
>
> **The 2018 hail-damage case is the line I won't cross**: v1 doesn't touch coverage classification.
>
> Wedge proposal lands Friday. You'll see compliance-relevant components first.
>
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Customer-political acuity | 5 | Disarmament landed; cell number is proof |
| Discovery rigor | 5 | Extracted the unwritten rules — gold |
| Risk awareness | 5 | War story informed wedge boundaries explicitly |
| Codification | 5 | Committed to documenting unwritten rules as part of policy library |
| Domain learning velocity | 5 | State map captured; HITL floor mapped to wedge scope |

**Keep**: the disarmament opening, verbatim; the "unwritten rules" question; not asking for a design opinion.

**Fix**: nothing — this was a textbook execution. Most important interview of the engagement and it landed.
