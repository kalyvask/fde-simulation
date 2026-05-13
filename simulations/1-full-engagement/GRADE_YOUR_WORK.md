# Grade Your Work — Automated Rubric (Claude as Grader)

> A self-graded rubric is fine. An LLM-graded rubric calibrated against the reference solution is better. This file gives you a Claude prompt that takes your submission and grades it against the reference, with specific feedback per dimension.

## When to use this

After each phase of the full engagement simulation, when you've produced your own artifact (discovery memo, wedge proposal, prototype, field memo). Don't peek at the reference solution before this step — the grader does the comparison for you.

## How to use this

1. Open Claude Code or claude.ai (Opus 4.x or Sonnet 4.x preferred for grading quality)
2. Copy ONE of the grader prompts below (one per phase)
3. Attach (or paste) two things:
   - Your submission for this phase
   - The reference solution file from the case folder (`discovery_memo.md`, etc.)
4. Send. Claude grades your work and returns a structured score + feedback.

## The grader prompts

### Phase 1 — Discovery memo grader

```
You are a senior Forward Deployed Engineer grading a candidate's Week 1 discovery memo against a reference solution. The candidate is preparing for FDE / Deployed PM interviews at frontier AI labs.

GRADING CRITERIA (5 dimensions, 0-3 each, max 15):

1. Stakeholder mapping (0-3)
   - 0: Generic list of titles, no archetypes
   - 1: Names individuals but not archetypes
   - 2: Names individuals + archetypes (buyer, champion, operator, blocker, etc.)
   - 3: All 7-8 archetypes covered including the silent skeptic, with how-to-engage notes

2. Information needed (0-3)
   - 0: "We'd talk to stakeholders"
   - 1: Lists data needed but not by source
   - 2: Organized by source (people / data / process / external)
   - 3: Specific data items + specific interview questions + specific external benchmarks

3. 4-source convergence (0-3)
   - 0: Not mentioned
   - 1: Mentioned but not applied
   - 2: Applied with 2-3 sources named
   - 3: All 4 sources named (Buyer / Brief / Industry / Operator) with convergence point identified

4. Wedge hypothesis (0-3)
   - 0: No wedge proposed
   - 1: Generic wedge ("automate FNOL drafting")
   - 2: Specific wedge with scope boundary
   - 3: Specific wedge + explicit out-of-scope items + justification on the kill-criteria

5. Discipline and quality (0-3)
   - 0: Generic, no specifics
   - 1: Some specifics but inconsistent
   - 2: Concrete specifics throughout
   - 3: Quoted stakeholder language, named tradeoffs, week-3 deliverables flagged

OUTPUT FORMAT:

| Dimension | Score | What worked | What was missing |
|---|---|---|---|
| Stakeholder mapping | X/3 | ... | ... |
| Information needed | X/3 | ... | ... |
| 4-source convergence | X/3 | ... | ... |
| Wedge hypothesis | X/3 | ... | ... |
| Discipline and quality | X/3 | ... | ... |
| **TOTAL** | **X/15** | | |

Then 3 bullets:
- The single biggest gap between your submission and the reference
- The single best thing your submission does that the reference doesn't
- The one thing to fix before Phase 2

INPUT: I'll paste my submission first, then the reference solution.

Be honest. Strong feedback beats vague encouragement.

[Paste your discovery memo here]

---REFERENCE---

[Paste the contents of discovery_memo.md here]
```

### Phase 2 — Wedge proposal grader

```
You are a senior Forward Deployed Engineer grading a candidate's Week 2 wedge proposal against a reference solution.

GRADING CRITERIA (5 dimensions, 0-3 each, max 15):

1. Wedge framing (0-3)
   - 0: No wedge or generic
   - 1: Wedge named, no defense
   - 2: Wedge defended with "confidence over size" or similar principle
   - 3: Wedge defended on Outcome Risk Matrix + 3-lens scaffold + explicit out-of-scope

2. 3-lens scaffold (0-3)
   - 0: Not used
   - 1: Customer column only
   - 2: Customer + Product columns
   - 3: All 3 columns filled (Customer / Product / Technical) with emotional state, out-of-scope = in-scope, metric tension, one specific risk

3. Architecture (0-3)
   - 0: Single mega-prompt or no architecture
   - 1: 5-8 agents named, no defense
   - 2: 5-8 agents + tier choices + det/LLM split, mostly defended
   - 3: Agent shapes from catalog (Extractor / Classifier / Synthesizer / Critic / Compliance critic / Router / Auditor) + workflow decomposition method + orchestration pattern + read/write integration patterns

4. Production thinking (0-3)
   - 0: Demo-only, no eval, no observability
   - 1: Eval mentioned but no specifics
   - 2: Eval + pass^k=5 + adversarial set
   - 3: Eval suite weighted by failure cost + pass^k=5 + production observability + immutable audit trace + 3 sign-off criteria with named owners

5. Risk surfacing (0-3)
   - 0: "We'll handle risks"
   - 1: 3-4 risks named
   - 2: 5-7 risks with mitigations
   - 3: Risks organized in Business / UX / Technical buckets with detection signals and named owners per risk

OUTPUT FORMAT: same table as Phase 1 + the 3 closing bullets.

[Paste your wedge proposal here]

---REFERENCE---

[Paste wedge_proposal.md and wedge_build_plan.md here]
```

### Phase 3 — Prototype + eval suite grader

```
You are a senior Forward Deployed Engineer grading a candidate's Week 3 prototype + eval suite against the reference.

GRADING CRITERIA (5 dimensions, 0-3 each, max 15):

1. Architecture fidelity (0-3)
   - 0: Single mega-prompt with no agent boundaries
   - 1: Multiple agents but no separation of concerns
   - 2: 5-8 specialized agents with proper boundaries
   - 3: Agents map to shapes (Extractor / Classifier / Synthesizer / Critic / Compliance critic / Router / Auditor); each has ONE job; deterministic gates around dangerous calls

2. Hybrid det+LLM discipline (0-3)
   - 0: Everything LLM
   - 1: Some deterministic but inconsistent
   - 2: Critic / compliance work is deterministic; synthesis is LLM
   - 3: Deterministic where reliability is non-negotiable (citation verify, MNPI scrub, audit); LLM where creativity is value (drafting); LLM-as-judge for soft errors

3. Eval suite (0-3)
   - 0: No evals or trivial happy-path only
   - 1: Has evals but no weighting
   - 2: Weighted by failure cost; happy + adversarial
   - 3: 30+ cases weighted by failure cost; pass^k=5 with variance ≤5%; per-major-risk adversarial case; production observability plan documented

4. Audit trace + observability (0-3)
   - 0: No trace, no observability
   - 1: Per-request log but not examiner-readable
   - 2: Examiner-readable trace per request
   - 3: Immutable trace + 7-day rolling drift detection + per-agent latency/cost tracking + weekly review cadence with named operational owner

5. Read-only discipline (0-3)
   - 0: Agents write to external systems in v1
   - 1: Writes are gated by approval but still in v1
   - 2: Read-only v1 with holding queue
   - 3: Read-only v1 + 3-tier integration ladder (read-only → approval-gated → autonomous) + each tier has named gate

OUTPUT FORMAT: same table + 3 closing bullets. Also: 5 specific code-level suggestions the candidate should make to improve.

INPUT: I'll paste my repo's tree structure + 3-5 representative files (workforce.py, base agent, one critic, eval harness, one eval case). The reference is in the prototype/ folder.

[Paste your tree structure + key files here]
```

### Phase 4 — Field memo grader

```
You are a senior Forward Deployed Engineer grading a candidate's Week 4 field memo against the reference.

GRADING CRITERIA (4 dimensions, 0-3 each, max 12):

1. Field-back-to-product feedback (0-3)
   - 0: No specific feedback to lab Research / Product
   - 1: Generic feedback ("LLMs should be better")
   - 2: Specific lab-relevant feedback (eval primitives, immutable snapshots, etc.)
   - 3: 3-5 specific lab feedback items + the customer context that motivated each

2. Production gates (0-3)
   - 0: No named gates
   - 1: Pass^k mentioned
   - 2: 3 sign-off criteria with stakeholder owners
   - 3: 3 sign-off criteria + rollback procedure + drift detection plan + 90-day operational owner

3. Risks remaining (0-3)
   - 0: "We're good"
   - 1: Generic remaining risks
   - 2: Specific remaining risks bucketed (Business / UX / Technical)
   - 3: Bucketed risks with detection signals + named owners + go-no-go criteria for each

4. Handoff documentation (0-3)
   - 0: No handoff plan
   - 1: Generic handoff plan
   - 2: Named operational owner + weekly cadence
   - 3: Named owner + weekly cadence + escalation runbook + audit-trace standard + customer-side ownership confirmation

OUTPUT FORMAT: same table + 3 closing bullets.

[Paste your field memo]

---REFERENCE---

[Paste field_memo.md]
```

## Self-grading discipline (the rule)

When Claude grades you, **subtract 1 point per dimension from the score it gives you.** Graders are typically too generous. Interviewers grade harshly. Calibrate by being more skeptical than the LLM.

The candidates who land FDE offers consistently under-rate themselves and target the gap.

## Iterating

Don't just grade once and move on. Pattern:

1. Submit your Phase X work to Claude grader
2. Read the feedback
3. Make ONE specific improvement
4. Re-submit
5. Compare scores
6. Move to Phase X+1 once you've closed at least one gap

The grader is calibration, not finality. Use it to identify the gap, then close it.

## Optional: Python script to automate

If you want a CLI version that takes your file and the reference file as args and produces a graded markdown report, here's the shape:

```python
# grade.py — usage: python grade.py phase1 my_memo.md
import sys
import anthropic
from pathlib import Path

PHASE_PROMPTS = {
    "phase1": "Phase 1 — Discovery memo grader prompt above",
    "phase2": "Phase 2 — Wedge proposal grader prompt above",
    # etc.
}

def main():
    phase = sys.argv[1]
    my_file = sys.argv[2]
    ref_file = sys.argv[3]
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4000,
        messages=[{
            "role": "user",
            "content": f"{PHASE_PROMPTS[phase]}\n\n[MY SUBMISSION]\n{Path(my_file).read_text()}\n\n[REFERENCE]\n{Path(ref_file).read_text()}"
        }]
    )
    print(response.content[0].text)

if __name__ == "__main__":
    main()
```

Not built into the repo (would require API key + dependencies for users who just want to read the files). Build it locally if you want CLI grading.
