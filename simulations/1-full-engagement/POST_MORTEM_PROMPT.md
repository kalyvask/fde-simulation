# Engagement Post-Mortem — Trap Detection Prompt

> Read your engagement artifacts, identify which expert traps you walked into, score the severity of each, and tell you what to fix before the next attempt. Run this once at the end of the engagement (after Week 4 field memo).

## When to use this

After you've drafted the discovery memo, wedge proposal, build plan, prototype, eval suite, and field memo for a case. Before you fill in `RETRO_TEMPLATE.md`. The post-mortem feeds the retro.

## How to use this

1. Open Claude (Code or claude.ai). Opus 4.7 preferred for detection accuracy.
2. Paste the full prompt below.
3. Attach (or paste) your artifacts AND the `EXPERT_TRAPS.md` from your case folder.
4. Claude returns: which traps you walked into, severity, evidence from your artifacts, and the fix.

## The prompt

```
You are a senior Forward Deployed Engineer running a post-mortem on a candidate's
FDE engagement. The engagement is one of two reference cases (Calder Insurance or
Helix Capital). The candidate has produced a discovery memo, wedge proposal, build
plan, prototype agent workforce, eval suite, and field memo.

Your job: detect which of the 5 expert traps the candidate walked into, with
evidence from their artifacts. Be honest. The candidate has explicitly asked for
the trap detection; vague encouragement helps them less than specific traps named
with quoted evidence.

INPUT YOU WILL RECEIVE:
1. The case (Calder or Helix)
2. The candidate's artifacts (discovery memo, wedge proposal, build plan,
   prototype tree + key files, eval suite, field memo)
3. The case's EXPERT_TRAPS.md file (the 5 traps + the bonus trap)

DETECTION METHODOLOGY:

For each trap (1 through 5, plus bonus Trap 0):
1. Read the trap's "Detection signal" section
2. Search the candidate's artifacts for that signal
3. Decide: WALKED_IN / PARTIAL / AVOIDED
   - WALKED_IN: the trap's detection signal is clearly present
   - PARTIAL: some elements of the trap are present but mitigated
   - AVOIDED: the trap is not present; the reference move (or equivalent) is in place
4. Quote the evidence from the candidate's artifact (file name + the line)
5. Rate severity if walked-in: HIGH (would fail the engagement) / MEDIUM (would
   require rework in week 5) / LOW (would surface in the lead-user review)

OUTPUT FORMAT:

## Trap detection summary

| Trap | Verdict | Severity | Evidence (file + quote) |
|---|---|---|---|
| Trap 0 — Pitching before scoping | WALKED_IN/PARTIAL/AVOIDED | HIGH/MEDIUM/LOW/n/a | `<file>`: "<quoted text>" |
| Trap 1 — Wedge mis-selection | ... | ... | ... |
| Trap 2 — LLM where rules win | ... | ... | ... |
| Trap 3 — Missing the eval-set authority (Calder) / Including forbidden content (Helix) | ... | ... | ... |
| Trap 4 — Data-pull or calibration miss | ... | ... | ... |
| Trap 5 — Silent skeptic or CISO miss | ... | ... | ... |

## What each WALKED_IN means for this engagement

For each trap marked WALKED_IN, write 3-4 sentences:
- What the candidate did (quoted from the artifacts)
- Why this would fail in a real engagement
- What the reference move would have been
- The single specific fix the candidate should make before the next iteration

## Pattern across traps

If multiple traps are WALKED_IN, what's the common upstream miss? Pick one of:
- "Customer-first framing": the candidate is solving a builder-shaped problem
- "Architecture judgment": the candidate is over-using LLMs vs deterministic gates
- "Production thinking": the candidate is treating evals / observability as polish
- "Risk surfacing": the candidate is leaving security / compliance to v2
- "Stakeholder reading": the candidate missed an interview-room signal

Name the pattern and quote the 2-3 strongest pieces of evidence.

## Fix-first list

Three concrete, single-paragraph fixes the candidate should make to their
artifacts before re-submitting to the rubric grader. Order by leverage (fix #1
unblocks fix #2 unblocks fix #3). Each fix is one paragraph, names the artifact
to edit, and quotes the specific line to change.

## Score impact

For each trap WALKED_IN, estimate the impact on the rubric scores from
GRADE_YOUR_WORK.md:
- Discovery memo (out of 15): ...
- Wedge proposal (out of 15): ...
- Prototype + eval (out of 15): ...
- Field memo (out of 12): ...

Then estimate the total engagement score (out of 57) before and after the fix-first
list is applied. Be honest; under-rate rather than over-rate. The candidate uses
the discipline rule of subtracting 1 point per dimension; do not do that for them
in this output.

CRITICAL GUIDELINES:
- Quote actual text from the candidate's artifacts. Don't paraphrase.
- If you can't find evidence for a trap, mark AVOIDED, not PARTIAL.
- Severity HIGH means "real engagement would fail" — be specific about why.
- Do not soften the verdicts. The candidate is using this to calibrate.

[Paste the case identifier and artifacts below]

CASE: [Calder | Helix]

ARTIFACT 1 — Discovery memo:
[...]

ARTIFACT 2 — Wedge proposal:
[...]

ARTIFACT 3 — Build plan:
[...]

ARTIFACT 4 — Prototype tree (output of `tree` or `find`) + key files (workforce.py + 1 critic + 1 eval case):
[...]

ARTIFACT 5 — Eval results (output of `python scripts/run_eval.py`):
[...]

ARTIFACT 6 — Field memo:
[...]

EXPERT_TRAPS.md FOR THIS CASE:
[Paste the case's EXPERT_TRAPS.md here]
```

## What to do with the output

1. **Read every WALKED_IN trap carefully.** The evidence quotes should ring true; if they don't, the post-mortem is wrong and you should push back.
2. **Apply the fix-first list in order.** Don't try to fix all traps at once.
3. **Re-run the rubric grader** (`GRADE_YOUR_WORK.md`) after applying fixes.
4. **Compare the before / after scores.** This is the calibration loop.
5. **Fill in `RETRO_TEMPLATE.md`** using the post-mortem pattern as your "what didn't work" section.

## What the post-mortem does NOT do

- It doesn't replace the rubric grader. Use both. The rubric scores dimensions; the post-mortem detects traps.
- It doesn't generalize to other cases. Calder traps don't apply to Helix and vice versa. If you run both cases, run the post-mortem twice with the case-specific `EXPERT_TRAPS.md`.
- It doesn't grade the prototype code in detail. That's the rubric Phase 3 grader's job. The post-mortem checks for architectural traps (e.g., "did you make the LLM source numbers"), not code quality.

## Common pattern across first-attempt candidates

If this is your first FDE engagement, expect to walk into 2-3 traps. That's normal. The candidates who land FDE offers are not the ones who walk in cleanly the first time; they're the ones who run the post-mortem, fix one trap per iteration, and arrive at trap-free artifacts by attempt 2 or 3.

Walking in 0 traps on attempt 1 either means you're already at the bar OR you spoiled the reference solutions before attempting. The post-mortem can't tell those apart. Be honest with yourself.
