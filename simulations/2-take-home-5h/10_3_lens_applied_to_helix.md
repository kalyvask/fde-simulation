# 10 — 3-Lens Framework Applied to Helix

> The Customer | Product | Technical scaffolding from the  Agent Design round, applied directly to the Helix earnings-note wedge. Use this table as: (1) your Hour 1 wedge audit, (2) the structure for Slide 1's framing, (3) the Review opening 90-second restatement, (4) the anchor for architecture defense under pushback.

## Why a  framework belongs in Helix prep

Different artifact, same skill. the agent design round is a 5-min whiteboard. Helix is a 5-hour build + 60-min Review. Both test the same thing: can you defend an agent design under cross-examination by structuring it around the customer first, the technology last?

The 3-lens framework is the highest-leverage transfer because it forces every load-bearing decision through the same 3 questions before the interviewer asks them.

## The 3-lens table for Helix earnings-note wedge

### CUSTOMER column

| Cell | Helix answer |
|---|---|
| **Who** | Rachel Kim — senior TMT analyst, 9 years tenure, lead user. (David Park is champion; Sarah Mendez is economic buyer; Carmen Diaz is the hostile downstream reader.) |
| **Emotional state** | **Exhausted** (morning-after grind, 4 hours per name × 80 names × 4 quarters) AND **anxious** about reputational risk (hallucinated number → PM trade → SEC scrutiny). Two seniors quit in 2025 citing the grind. Different design from a stressed reservations customer or a curious loyalty customer. |
| **JTBD — top 3** | (1) Ship a defensible earnings note that survives Carmen's skeptical read in <30 min. (2) Capture management tone shifts + caveats accurately, not just KPIs. (3) Maintain the "zero MNPI incidents in 3 years" streak. |
| **Why failing today** | 4h × 80 names × 4 quarters = 1,280h/analyst/yr. Notes land hours after market open → alpha leak + customer-facing reputational drag. Senior-analyst attrition cited the grind explicitly. |
| **What's hard (root cause)** | Analyst can't distinguish "AI summary I have to verify line-by-line" from "AI-assisted draft I can actually defend." So they choose between speed (risk) and rigor (burnout) — both lose. |

### PRODUCT column

| Cell | Helix answer |
|---|---|
| **Intent** | Citation-grounded earnings draft + tone-shift detection. Rachel gets 30 minutes of senior-analyst review per note instead of 4 hours of from-scratch drafting. |
| **In scope** | (1) Pre-call read of consensus + prior quarter, (2) Real-time KPI extraction during/after call, (3) Citation-grounded draft (every number traces to a source), (4) Tone-shift flags for analyst review, (5) Audit trace as a first-class artifact |
| **Out of scope (equally explicit)** | (1) M&A commentary — Reg FD minefield, separate compliance architecture. (2) Position-sizing recommendations — Chinese wall + Reg FD violation. (3) Auto-publish to PMS or trader distribution. (4) Account or trade actions of any kind. (5) Multi-quarter retrieval — v1 = prior 1 quarter only. |
| **Trust levels** | **Act:** KPI extraction (deterministic), citation grounding (regex-bound), MNPI watch-list block (deterministic). **Ask:** drafter shows analyst the citation chain before editing; tone supervisor flags borderline calls for analyst decision. **Escalate:** any policy combination Compliance Critic flags, anything outside the consensus + prior-quarter scope. |
| **Fallback** | Confidence-low or citation-chain-broken → route to Rachel's queue with partial draft + reasoning trace + named ambiguity. Never silent-fail. Never auto-publish on uncertainty. |
| **Metric + tension** | **Primary:** 30-min senior-analyst review per note (from 4h). **TENSION: Speed vs zero-MNPI streak.** We protect the streak — would rather Rachel reviews a borderline note in 45 min than ship a wrong number in 25 min. The streak is the engagement's reputation. |

### TECHNICAL column (kept light)

| Cell | Helix answer |
|---|---|
| **Read access** | Earnings transcripts (FactSet), prior-quarter notes (internal sandbox), Bloomberg consensus (read-only), MNPI watch list (Mei-owned), audit-trace standard (Mei-owned), SubjECTive-QA labels (for eval calibration only) |
| **Write access** | **NONE in v1.** Drafts written to a holding queue, not the PMS, not the trader distribution list, not analyst's published-notes folder. Only writes are to the escalation queue + the immutable audit trace. |
| **Data freshness** | Transcripts: live during/after call. Consensus: live on Bloomberg sandbox. Policy docs (MNPI list, audit standard): pulled at start of every agent invocation (NOT cached at process startup). Prior-quarter notes: indexed corpus. |
| **ONE specific integration risk** | **MNPI watch list drift.** Mei updates the list weekly; if a name is added mid-quarter and our scrubber works off a stale cache, an MNPI leak becomes possible. **Mitigation:** scrubber pulls watch list at the start of every agent invocation + Mei-owned audit log of every scrubber decision + LLM-as-judge tier-2 check before draft leaves the holding queue. |
| **Validation plan** | PoC + weighted eval suite (50+ cases including MNPI-block + hallucinated-guidance + position-sizing-leak + tone-shift-miss) + **pass^k=5** production threshold + Mei MNPI sign-off + Rachel signs off on 20 sample drafts + Carmen hostile-mode review + closed beta with 1 sector (TMT) for 2 weeks |

## How to use this table across the engagement

### As the Hour 1 wedge audit

After you pick your wedge (Hour 1, per `02_take_home_workflow.md`), fill in the 3-lens table for your wedge. If any cell is empty or generic, your wedge isn't defensible yet — go back and sharpen. The table itself is also a useful artifact to keep open during Hours 2-4.

### As Slide 1 structure

Slide 1's "Wedge in one paragraph" can be the synthesis of the 3 lenses:

> "We're building [intent — from Product] for [who — from Customer] who's [emotional state — from Customer]. The agent acts [trust level summary — from Product] and explicitly does not [out of scope — from Product]. Architecturally it's [read/write — from Technical] with [one specific risk — from Technical] as the mitigated failure mode."

For Helix:

> "We're building a citation-grounded earnings draft + tone-shift detector for Rachel — an exhausted senior analyst anxious about hallucinated numbers reaching a PM. The agent acts deterministically on the dangerous calls (MNPI block, citation verify) and asks the analyst on the soft calls (tone, edge cases); it explicitly does not touch M&A, position-sizing, or any write. Architecturally it's read-only v1 with MNPI watch-list drift as the one specific risk, mitigated by per-invocation list pulls + Mei-owned audit log."

That's the entire wedge framing in one paragraph. Defensible against any probe.

### As the Review opening (90-second restatement)

> "Let me restate the wedge in 3 lenses.
>
> **Customer**: Rachel — senior TMT analyst, exhausted by the morning grind, anxious about a hallucinated number reaching a PM. The org has zero MNPI incidents in 3 years and two senior analysts quit in 2025 over the grind. That's the customer.
>
> **Product**: citation-grounded draft with tone-shift detection in scope. M&A, position-sizing, and any write explicitly out. Trust levels are deterministic on the dangerous calls, ask-the-analyst on the soft calls, escalate on policy combinations. Metric tension is speed vs zero-MNPI streak — we protect the streak.
>
> **Technical**: read-only v1, with MNPI watch-list drift as the one specific risk — mitigated by pulling the list at every invocation, plus Mei-owned audit log of scrubber decisions. Validation through pass^k=5 on a 50-case eval suite plus Mei, Rachel, and Carmen sign-offs before any production rollout."

That's 75-90 seconds, frames every architecture decision before the interviewer probes, and tells the interviewer which lens to challenge first.

### As architecture defense under pushback

When the interviewer probes a specific agent ("why MNPI Scrubber first?"), anchor your answer to which lens it serves:

| Probe | Anchor your answer to... | Example response |
|---|---|---|
| "Why MNPI Scrubber first?" | Technical column (the one specific risk) | "It serves the Technical lens — MNPI watch-list drift is the one specific risk I named. The scrubber fires before any LLM call. If MNPI is detected, no LLM call ever happens. Cost of a leak is fund-shutting." |
| "Why Sonnet for the drafter?" | Product column (the trust level structure) | "Drafter is the 'ask the analyst' tier — synthesis quality matters because Rachel will edit but won't re-draft. Sonnet's synthesis vs Haiku, at ~80 notes/quarter the cost difference is immaterial." |
| "Why citation-grounded?" | Customer column (Rachel's anxiety) | "Citation grounding eliminates Rachel's named anxiety — hallucinated numbers reaching a PM. The architecture has to make that failure mode impossible, not just unlikely." |
| "Why no M&A coverage?" | Product column (out of scope) | "M&A is in the explicit out-of-scope set. It's a Reg FD minefield that needs separate compliance architecture; trying to ship it in v1 means we don't ship anything in v1." |
| "Why no auto-publish?" | Technical column (write access) | "Write access in v1 means a wrong draft becomes a wrong record in the PMS. Read-only v1 keeps the failure mode at 'Rachel catches it in review' — recoverable." |

The pattern: anchor every architectural choice to a lens, then to a specific cell within that lens. Generalizes to any probe the interviewer surfaces.

## The 6 rules that matter most for Helix specifically

| Rule | Helix application |
|---|---|
| **Name the emotional state** | Rachel is exhausted + anxious. Different design from a frustrated, time-pressured, or curious customer. Name this explicitly in your opening. |
| **Out-of-scope = in-scope** | M&A out, position-sizing out, auto-publish out, multi-quarter out. Each with a compliance or scope reason. List them on Slide 1 with equal weight to in-scope. |
| **Name the metric tension** | Speed vs zero-MNPI streak. Pick which you protect. (You protect the streak — that's the senior move.) |
| **Read-only v1** | Zero writes to PMS, trading distribution, analyst's published folder. Defensive framing, not apologetic. |
| **One specific risk** | MNPI watch-list drift + per-invocation pull as the mitigation. Beats "we handle MNPI carefully." |
| **Never jump columns** | When probed on Technical first ("why Sonnet?"), park it: "Let me note that and close the Product question first." Re-anchors the conversation. |

## Cross-references

- The standalone framework (without Helix): `../../training/sierra_specific/03_agent_design_round_prep.md`
- The interactive practice tool prompt: `../../training/sierra_specific/09_claude_design_prompt_agent_design.md`
- Other Helix decision principles (outcome risk matrix, sequencing, engagement gap): `09_decision_principles.md`
- The Review pushback script: `06_review_round_script.md`
