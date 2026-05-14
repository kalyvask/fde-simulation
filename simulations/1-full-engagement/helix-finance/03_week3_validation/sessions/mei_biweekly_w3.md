# Mei Biweekly Compliance Check — Week 3 Tuesday, 45 min, video

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Mei is the default-no compliance officer. This is the second biweekly. The first (week 1) was about scope; this one is about evidence.

## Setup

Tuesday week 3, 11:00 AM ET. Video. Mei has a printed copy of the MNPI Scrubber's policy library, the audit-trace renderer output for 5 sample notes, and the eval suite composition document. She has questions written in margin.

## Selected exchanges

**Mei**: "Three things I want to walk through. First, the watch-list pull cadence. Second, the audit trace standard. Third, my own mock-audit results — I ran 10 cases against the system over the weekend and want to talk through what I saw."

**Alex**: "Let's start with watch-list pull. The Scrubber pulls from your compliance system at the start of every agent invocation — not at process startup, not cached. We logged 280 pulls this week. If you add a name to the watch list at 9:01 AM, the next 9:02 AM agent run will see it. That's the contract."

**Mei**: "I tested this Friday at 4:55 PM — added a synthetic name, ran a test note at 4:56 PM, the Scrubber blocked it. Good. My concern: what happens if your pull endpoint to my system is slow? Does the agent fail open or fail closed?"

**Alex**: "Fail closed. If the watch-list pull times out or errors, the Scrubber returns must_block=True with a `policy.mnpi_watch_list_pull_failure` rule fired. The agent doesn't run. The note goes to your queue for manual review."

**Mei**: "What's the timeout?"

**Alex**: "Five seconds. Configurable in `policy_library.py:WATCH_LIST_PULL_TIMEOUT`. Five seconds is well within your compliance-system SLA but generous enough that transient network issues don't fail-closed too aggressively."

**Mei**: "OK. Audit trace next. I read the example you sent. The Trace ID is good. The per-agent step-list is good. The model_version on the LLM agents is good. But I want to see the *input* to each LLM call captured, not just the output."

**Alex**: "Currently we capture the input and output. The renderer only shows the output for readability. I can add an 'expand inputs' toggle on the HTML view, and the JSON trace always has both. Want me to do that for next week?"

**Mei**: "Yes. And the JSON trace — I want a sample. Send me 10 traces in JSON. I'll have my compliance counsel review the schema."

**Alex** *(notes)*: "Done. I'll send 10 traces by EOD today. JSON schema is documented in `helix_agent/trace.py`."

**Mei**: "Mock-audit results. I ran 10 cases. 8 passed cleanly. 2 I have concerns about."

**Alex**: "Tell me the two."

**Mei**: "Case one: a SAMPLE_CONSUMER call where management said 'we expect strong growth in our European business.' Your drafter wrote 'Management expressed confidence about European growth opportunity.' That's accurate. But — Europe is a regulated geography. Any forward-looking statement about Europe specifically should be flagged for review because of MiFID II reporting requirements. The drafter doesn't know that. The Compliance Critic didn't catch it."

**Alex**: "Right — we have a generic Reg FD check but no jurisdiction-specific check. I'd add a 'forward-looking statement about regulated geography' rule to the Compliance Critic. Let me list the jurisdictions you care about and I'll wire them as deterministic patterns."

**Mei**: "Europe (MiFID II), UK (FCA), Hong Kong (SFC), Japan (JFSA), Australia (ASIC). For each, the rule is: if the draft contains forward-looking language *plus* a regulated-jurisdiction reference, flag for analyst review with the specific jurisdiction cited. Not a block; just a flag. Analysts can decide whether to send."

**Alex** *(notes)*: "Done. New rule_4 in the policy library: `regulated_jurisdiction_forward_looking`. Deterministic. Flag-only, not block."

**Mei**: "Case two: the drafter referenced a competitor by name — 'unlike SAMPLE_COMPETITOR, our margin profile is improving.' That's a direct competitive comparison made by management in the call. The drafter quoted it. The concern: under Reg FD, a buy-side firm citing a competitor by name in a published note can create selective-disclosure issues if the comparison is interpreted as material non-public information about the competitor."

**Alex**: "So competitor names in management's commentary should be anonymized or removed in our draft."

**Mei**: "Anonymized. Replace with 'a peer' or 'a competitor.' Preserves the substance, removes the specific Reg FD exposure."

**Alex** *(notes)*: "Drafter prompt update: when the source transcript names a specific competitor, the draft uses anonymized phrasing ('a peer', 'a competitor', 'a comparable name in the sector'). Deterministic post-processor to catch any name that passed through the prompt. By Thursday."

**Mei**: "Good. With those two changes, I can sign the audit-trace standard."

**Alex**: "By Friday morning. I'll send the updated traces, the new rule_4 implementation, and the competitor-anonymization post-processor. We talk Friday afternoon."

*(Wraps at 42 min.)*

## Post-session captures

### What changed in the design

1. **Watch-list pull fail-closed**: Scrubber must_block=True on pull timeout / error. Timeout configurable; default 5 seconds.
2. **Audit trace input capture**: JSON always includes input; HTML renderer adds expand-input toggle.
3. **New compliance rule_4: regulated-jurisdiction forward-looking flag**: Europe / UK / HK / Japan / Australia. Flag-only, not block.
4. **Competitor anonymization**: drafter prompt + deterministic post-processor. Replace specific competitor names with anonymized phrasing.

### Three sign-off criteria — status update

| Criterion | Owner | Status as of week 3 |
|---|---|---|
| Pass^k=5 with variance ≤5% on weighted eval | Aditya | ✅ 96% pass on 50 cases, variance 3.2% |
| Audit trace + MNPI scrubber sign-off | Mei | ⏳ pending Friday — depends on rule_4 + competitor anonymization |
| Rachel signs off on 20 sample drafts | Rachel | ⏳ pending Friday — depends on tone-shift architecture revision |

Two of three gates pending the same Friday review. High-leverage day.

### Glossary updates

- **Watch-list pull fail-closed**: timeout/error blocks rather than allows. The conservative default.
- **Regulated jurisdiction forward-looking**: forward-looking statement about a specific regulated geography (Europe/UK/HK/Japan/Australia). Flag, not block.
- **Competitor anonymization**: replacing specific competitor names with generic phrasing in published research notes. Reg FD discipline.

### Stakeholder map updates

- **Mei**: stance moved from DEFAULT-NO → CONDITIONAL-YES. Two changes from blocking to passing. The mock-audit-on-weekend gesture (she tested this herself, found two real gaps) is the strongest engagement signal. She's now invested in the system working.

## Recap email sent (12:00 PM)

Subject: `[Helix] Mei mock-audit findings — 4 changes by Friday`

> Mei — thanks for the mock-audit work over the weekend. Two real findings, plus three follow-ups I'm shipping by Friday:
>
> 1. **Fail-closed on watch-list pull failure**: Scrubber blocks if the compliance-system pull times out (5s default) or errors. Default behavior. Configurable.
> 2. **Audit trace inputs always in JSON**: HTML adds expand-input toggle. Sending you 10 sample JSON traces today for your compliance counsel.
> 3. **New rule_4: regulated-jurisdiction forward-looking flag**: forward-looking statement + Europe/UK/HK/Japan/Australia = flag for analyst review.
> 4. **Competitor anonymization**: drafter prompt + deterministic post-processor. Specific competitor names → "a peer" / "a competitor" in published draft.
>
> Friday 11 AM: I'll send the updated traces + the new policy library + the post-processor diff. Friday afternoon: your sign-off review.
>
> Both your findings were exactly the kind of thing that would have triggered a Reg FD inquiry in week 8 if we hadn't caught them in week 3. Thank you.
>
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Calibrated engineering | 4 | Mei found two gaps I should have caught: regulated-jurisdiction flag was a known regulatory pattern; competitor anonymization is in every Reg FD primer |
| Customer-political acuity | 5 | Mei went from default-no to invested. The weekend mock-audit is her gesture |
| Risk awareness | 4 | The two findings are real adversarial cases; the eval suite missed both |
| Outcome ownership | 5 | Four specific changes with a Friday deadline, all reproducible commits |

**Keep**: opening with her agenda not mine; treating her findings as gifts not problems; immediate commit to dates.

**Fix**: should have added rule_4 (jurisdiction-specific) and competitor anonymization to the eval suite from week 2. The seed cases were not adversarial enough on Reg FD. Update the seed: 5 new adversarial cases per regulated jurisdiction.

**Lesson**: compliance officers who run their own mock audits are the strongest sign-off counterparts. Mei's pattern is: she does the work to find the gaps, then she signs off. Compliance officers who only ask questions but don't run their own tests are higher-risk because their sign-off doesn't reflect actual due diligence.
