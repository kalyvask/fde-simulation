# Carmen Hostile Review — Week 3 Thursday, 60 min, in-person

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Carmen Diaz is the silent skeptic — a senior trader, downstream of analyst notes, who's been burned twice in 5 years by hallucinated numbers in analyst notes. This session pre-empts her surfacing as a blocker in week 5 by making her surface as a hostile reviewer in week 3.

## Setup

Thursday week 3, 3:00 PM ET. Helix's trading-floor side, a conference room near her desk. Carmen has a printout of 10 drafts the system produced this week, sticky notes on the ones she's marked up. She's not warm. She's not hostile yet. She's testing.

David Park is invited but joins by video for the last 15 min only — Carmen wanted to do this without Research present, then bring David in for the wrap.

## Selected exchanges

**Carmen**: "Before we start. I'm not interested in pitching me. I'm interested in finding what's wrong. So let me run my list, you respond, then we talk about whether this gets near my desk."

**Alex**: "That's how I'd want to use the hour. Run it."

**Carmen** *(pulls the first marked draft)*: "SAMPLE_TMT Q3. Drafter wrote 'Management raised guidance, signaling confidence in Q4 momentum.' I went back to the source transcript. Management said: 'We're maintaining our prior range, with a bias to the upper half.' That's not raising guidance. That's saying 'no change but we're feeling slightly better.' The drafter inflated the management's actual statement."

**Alex**: "That's a real failure mode. Source said maintain, drafter said raise."

**Carmen**: "I trade on these notes. If a PM reads 'raised guidance' and trades on it, and the company didn't actually raise, we just bought into a position based on a fabrication. That's not a bug. That's an existential risk to the desk's trust in Research."

**Alex** *(notes)*: "Citation verifier needs to check semantic equivalence on directional language. 'Raised' vs 'maintained' vs 'lowered' — three distinct categorical claims. The drafter cannot escalate a 'maintain' into a 'raise.' Two fixes: (1) deterministic check on directional verbs against a controlled vocabulary that maps to source language, (2) Tone Supervisor specifically tests for 'directional escalation' between source and draft. I'll wire this by Friday morning."

**Carmen**: "Second one. SAMPLE_CONSUMER. Management mentioned a one-time charge of $35M. The drafter put this in the KPI table next to revenue and EPS, without flagging it as one-time. If a PM looks at the table and sees a $35M expense without context, they treat it as recurring. That's a different category."

**Alex**: "One-time items need a separate column or explicit tag. Right now the KPI Extractor pulls numbers without semantic categorization."

**Carmen**: "Three categories I care about: (1) recurring, (2) one-time, (3) non-cash. Every number in the KPI table should be tagged. If you can't tag it, don't put it in the table. Put it in the body with the context from the call."

**Alex** *(big note)*: "KPI Extractor gets a semantic tagger: each extracted number tagged as recurring / one-time / non-cash / forward-looking. Drafter only puts recurring numbers in the headline KPI table; one-time and non-cash go in a 'Notable items' section with source citations. Deterministic post-check: any number in the KPI table without a 'recurring' tag = block draft. By Friday."

**Carmen** *(picks up another)*: "Three. The note for SAMPLE_INDUSTRIAL Q3. Drafter quoted CEO saying 'we expect stronger margins in 2027.' I checked the transcript — the actual quote was 'we *expect* to see stronger margins in 2027 *if* the supply-side dynamic resolves.' Drafter dropped the conditional. A note that drops conditionals is worse than a note that doesn't make forward-looking claims at all."

**Alex**: "Conditional preservation. Every forward-looking statement keeps its qualifier. This is the same pattern as the directional-verbs check but for hypotheticals."

**Carmen**: "Yes. And if the drafter can't figure out how to render the conditional cleanly, it shouldn't include the statement at all. Skip the forward-looking quote rather than mangle it."

**Alex** *(notes)*: "Drafter prompt: forward-looking statements include all conditionals or are omitted. Deterministic post-check: any modal verb ('expect', 'anticipate', 'believe', 'should') in the draft must appear within 30 words of a conditional marker ('if', 'assuming', 'provided', 'subject to', etc.) OR be flagged for analyst review. By Friday."

*(After 40 min of similar findings — 8 of 10 drafts had at least one Carmen objection)*

**Alex**: "Carmen — for the record, what would make you confident enough to read AI-drafted notes the same way you read Rachel's notes?"

**Carmen** *(thinks)*: "Three things. One, the citation chain has to be visible to me, not just to the analyst. I want to see every numerical claim and its source line, like a footnote system. If I'm trading on it, I want to be able to verify it in 10 seconds. Two, the directional and conditional preservation has to be 100%, not 95%. I don't read 95%-confident notes. Three, when the agent flags something for analyst review, the published note has to say 'this section flagged for additional review' somewhere visible. If the analyst overrides the flag, I want to know that happened."

**Alex**: "Three commitments by Monday week 4:
1. **Visible citation system**: every numerical claim hyperlinked or footnoted to the source line in the transcript. Published note includes the citation panel.
2. **Directional and conditional preservation at 100%**: deterministic checks, no LLM judgment. If the deterministic check fails, the draft doesn't ship.
3. **Override transparency**: when an analyst overrides an agent flag, the published note carries a 'this section was reviewed and approved by [analyst] after agent flagged for review' annotation.

If we ship those three, you'll read the AI-drafted notes the same way?"

**Carmen** *(beat)*: "If you ship those three and we get 4 weeks of clean production with my eye on every note, yes. Until then, I'm reading them with extra skepticism."

**Alex**: "Fair. Set up biweekly check-ins with you starting week 5 — same shape as this one. You bring 10 drafts you flagged, we talk through them."

**Carmen**: "Done."

*(David joins by video for the wrap, 15 min)*

**Alex**: "David — Carmen and I just walked through 10 drafts. Eight had at least one finding. The three changes Carmen wants by Monday: visible citation system, directional + conditional preservation at 100%, override transparency. I'm shipping all three by Monday morning. Biweekly hostile review with Carmen continues from week 5."

**David**: "Are these blockers for the Friday rollout?"

**Alex**: "Not as Carmen framed them — she's accepting 4 weeks of production with her eye on every note before she stops reading skeptically. So we can roll out Friday with the three changes in place. The trust signal is Carmen showing up to the biweekly, not Carmen never finding a problem. If she stops showing up, that's worse."

**David**: "Good. Carmen — thanks for doing this. I want you in the biweeklies for the first 90 days."

**Carmen**: "I'll be there."

*(Wraps at 58 min.)*

## Post-session captures

### What changed in the design (3 commitments by Monday week 4)

1. **Visible citation system**: every numerical claim in the published note has a footnote or hyperlink to the source transcript line. The reader (PM, trader) can verify any number in 10 seconds. New deterministic post-processor; new HTML template for the published note.

2. **Directional + conditional preservation at 100%**: deterministic checks on directional verbs (raised/maintained/lowered) and modal verbs (expect/anticipate/believe). Any failure = draft doesn't ship. Adds two new rules to the policy library. Updates the test suite with adversarial cases per Carmen's findings.

3. **Override transparency**: when an analyst overrides an agent's flag, the published note carries an annotation. Builds on the existing trace; surfaces it in the published artifact, not just in compliance review.

### What Carmen signaled

- She moved from SILENT-SKEPTIC → ACTIVE-REVIEWER. The 4-week-production gate is the right ask from her; she's not asking us to be perfect, she's asking us to be inspectable.
- Her three asks are all about reader-side transparency, not author-side rigor. The note has to be defensible TO THE TRADER, not just to the analyst. That's a different bar than the one we've been optimizing for.
- The biweekly cadence is the relationship-preservation move. If she stops attending, the relationship has degraded. We monitor attendance + her finding-rate as a relationship-health metric.

### Stakeholder map updates

- **Carmen**: SILENT-SKEPTIC → ACTIVE-REVIEWER. Biweekly cadence locked through week 13. The "I'll be there" is the commitment-to-relationship signal.
- **David**: stable as CHAMPION. His "I want you in the biweeklies for the first 90 days" is the political insurance — Carmen's voice carries to David, not just to Rachel.

### Glossary updates

- **Reader-side transparency**: the note must be inspectable by the downstream consumer (PM, trader), not just defensible by the analyst-author.
- **Directional escalation**: when a drafter changes the categorical claim from "maintain" to "raise" or similar. Banned.
- **Conditional preservation**: forward-looking statements keep all qualifiers ("if", "assuming", "provided") or get omitted.
- **Override transparency**: published note carries annotation when analyst overrode an agent flag.

## Recap email sent (4:30 PM)

Subject: `[Helix] Carmen hostile review — 3 changes by Monday, biweekly from week 5`

> Carmen — thanks for the time and the sticky notes. Three changes I'm shipping by Monday morning:
>
> 1. **Visible citation system**: every numerical claim in the published note traces to a source transcript line. Reader can verify in 10 seconds.
> 2. **Directional + conditional preservation at 100%**: deterministic checks. Draft doesn't ship if these fail.
> 3. **Override transparency**: published note shows when an analyst overrode an agent flag.
>
> Biweekly hostile reviews start week 5. You bring 10 drafts you flagged; we walk through patterns.
>
> David is in the loop. He's asked you to attend the biweeklies for 90 days.
>
> Talk Monday.
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Customer-political acuity | 5 | Pre-empting Carmen surfacing as a blocker in week 5; surfacing her as a reviewer in week 3 |
| Discovery rigor | 5 | 40 min of pattern-finding with one of the highest-leverage stakeholders; got 3 design-level changes |
| Calibrated engineering | 4 | Should have built reader-side transparency from week 2; we optimized for analyst-defensibility, not trader-readability |
| Risk awareness | 5 | All three of Carmen's findings (directional escalation, one-time tagging, conditional drop) were real adversarial categories we'd have hit in week 5 production |
| Outcome ownership | 5 | Three changes pre-committed with a Monday deadline; biweekly cadence locked |

**Keep**: opening framing ("I'm not interested in pitching me, I'm interested in finding what's wrong"); absorbing all three findings as design-level changes, not edge cases; locking the biweekly cadence as the relationship-preservation move.

**Fix**: should have surfaced "reader-side transparency vs author-side rigor" as a design principle in week 2. We optimized for the analyst's signoff bar; we should have also optimized for the trader's verification bar. Two different bars. Both matter.

**Lesson**: silent skeptics become active reviewers when you invite them to find what's wrong, not when you ask them to validate what's right. The interview question is not "would you use this?" — it's "what would make you reject it?"
