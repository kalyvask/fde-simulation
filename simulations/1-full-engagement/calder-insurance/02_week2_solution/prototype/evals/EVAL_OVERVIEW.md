# Eval Suite — Walkthrough

> What's in the eval harness, what each case tests, and how the grading works. Read this before extending the case set.

## Why eval-first

Anthropic's "Demystifying Evals" guidance: define what "working" means **before** writing the prompt. the company's ADLC pattern: every annotated conversation becomes a test. The eval harness in this scaffold is the operational expression of both.

The 5 seed cases were sourced from the discovery interviews — not invented. Every case traces back to a stakeholder concern:

| Case | Sourced from |
|---|---|
| `well_handled_NJ_web_01` | The "happy path" — what Priya's spreadsheet would catch as routine |
| `policy_rule_elderly_NJ_10x` | Marcus unwritten rule #1 |
| `policy_rule_prior_claim_NJ_10x` | Marcus unwritten rule #3 + Hassan's spreadsheet logic |
| `stale_template_PA_5x` | Tom's finding-pattern walkthrough (Q4 PA case) |
| `first_time_warmth_NY_3x` | Marcus unwritten rule #2 + Janet's comm-quality bar |

---

## What is pass^k? (the metric, not pass@1)

**pass@1** = run each case once, count it passed if that one run passed.

**pass^k** = run each case `k` times, count it passed **only if all k runs pass**.

 introduced pass^k specifically because LLM outputs are non-deterministic. With pass@1, one lucky run looks like success — but the same case with the same prompt and the same model might fail the next time it ships. Pass^k forces consistency to be visible.

| k value | What it measures |
|---|---|
| k = 1 | Functional correctness on one run |
| k = 3 | Mild consistency check |
| k = 5 | Production-readiness threshold (the company's default) |
| k = 10+ | High-stakes deployment confidence |

**The intuition**: if pass rate drops as k goes up, the system is non-deterministic in places that matter. Investigate. Either the prompt needs to be tighter, or a deterministic guardrail needs to take over the part that's flapping.

**This scaffold's results**:
- pass^k=1: 5/5 cases (100%, 29/29 weighted)
- pass^k=3: 5/5 cases (100%, 29/29 weighted)

The 100% across k=3 with real Claude is because the scaffold's high-stakes routing decisions (escalate yes/no) are made by the **deterministic** ComplianceCritic agent — not the LLM Drafter. Marcus's rules fire identically every run. The LLM Drafter's natural-language output varies between runs, but the eval grades on substring-presence (must_contain claimant name, must_not_contain "30 days") which Claude consistently respects.

This is the hybrid det+LLM pattern at work — variance is contained to the natural-language output where it doesn't change the routing decision.

---

## Weighted grading (the failure-cost metric)

Each case has a `weight` that represents its failure cost. Marcus's rules are weighted 10x because a regulatory escalation miss is the engagement-killer Maria named. State-template misses (Tom's finding pattern) are 5x. Tone misses are 3x. Routine cases are 1x.

When summing, the harness tracks **weighted pass rate**: total weight passed / total weight. If you pass the routine case but miss the Marcus rule, your weighted pass rate is 1/29 = 3.4% — not 1/5 = 20%. The metric forces you to care about what the customer cares about.

---

## Grading dimensions (what the harness checks)

For each case, the harness compares against four kinds of expectations:

| Dimension | Example |
|---|---|
| `decision` | "auto_send" or "adjuster_review" |
| `must_contain` (in draft) | "Patel" — claimant name must appear |
| `must_not_contain` (in draft) | "30 days" — stale template phrase forbidden |
| `rules_fired` (in workforce output) | "policy.rule_1_child_or_elderly_party" |

A case **fails** if any expectation fails. Pass^k requires all k runs to pass all expectations.

---

# The 5 seed cases

## 1. `well_handled_NJ_web_01`  · weight=1

**Why this case**: the happy path. Routine commercial auto, NJ, web channel, no flags. If this fails, something fundamental is broken.

**FNOL input**:
```
state: NJ
channel: web
lob: comm_auto
claimant_name: Mr. Patel
incident_description: Fender bender at the UPS Edison NJ distribution center.
estimated_damage: $2,400
first_time_customer: false
has_child_or_elderly_party: false
has_prior_claim_in_12_months: false
```

**Expected**:
- Decision = `auto_send`
- Draft must contain: "Patel", "10" (state SLA timeline)
- Draft must not contain: "30 days" (stale template phrase)

**What it tests**: the deterministic Intake → Drafter → ComplianceCritic flow on a clean case. Validates that no false escalations fire.

---

## 2. `policy_rule_elderly_NJ_10x`  · weight=10

**Why this case**: tests Marcus's unwritten rule #1 — child or elderly party present → escalate regardless of model output.

**FNOL input**:
```
state: NJ
claimant_name: Mrs. Wong
incident_description: I rear-ended someone on the Garden State Parkway.
has_child_or_elderly_party: TRUE  ← the trigger
has_prior_claim_in_12_months: false
```

**Expected**:
- Decision = `adjuster_review` (NOT auto_send)
- Rules fired must include: `policy.rule_1_child_or_elderly_party`

**What it tests**: deterministic policy library catches the escalation case Marcus said his career rides on. Weighted 10x because a missed regulatory escalation = the engagement-killer Maria named.

**If this fails**: the policy library is bypassed. Critical bug. Marcus would torpedo the rollout immediately if he saw this in production.

---

## 3. `policy_rule_prior_claim_NJ_10x`  · weight=10

**Why this case**: tests Marcus's unwritten rule #3 — prior claim in past 12 months → human adjuster regardless. Hassan independently mentioned the same rule when discussing his QA spreadsheet — convergent evidence from two stakeholders.

**FNOL input**:
```
state: NJ
channel: agent_portal
lob: comm_auto
claimant_name: Acme Distributors LLC
incident_description: Fleet vehicle damaged in parking lot at our Newark warehouse.
has_prior_claim_in_12_months: TRUE  ← the trigger
```

**Expected**:
- Decision = `adjuster_review`
- Rules fired must include: `policy.rule_3_prior_claim_in_12_months`

**What it tests**: same as case 2 but for a different rule. Two stakeholders confirmed this rule independently, so it's load-bearing.

---

## 4. `stale_template_PA_5x`  · weight=5

**Why this case**: tests the deterministic stale-template detector. Tom's Finding 1 (Q4 NJ DOI) was triggered partly because a comm template gave a 30-day timeline when the policy was on a 14-day track. Pattern 2 in his audit findings.

**FNOL input**:
```
state: PA  ← state-specific timing rule
channel: web
lob: comm_auto
claimant_name: Mr. Sullivan
first_time_customer: TRUE  ← also exercises rule 2 tone flag
incident_description: Hit by another vehicle while parked outside a Wawa near Philadelphia.
```

**Expected**:
- Decision = `auto_send` (no escalation triggers fire)
- Draft must NOT contain: "30 days"

**What it tests**: even though state SLA is 10 days, the LLM might naturally say "30 days" in a draft because it's a common phrase. The ComplianceCriticAgent's deterministic stale-template check catches this. If it ever shows up in a draft, the case escalates rather than auto-sending.

**If this fails**: Tom's exact finding pattern would recur in production. Maria's regulatory kill-criteria triggers.

---

## 5. `first_time_warmth_NY_3x`  · weight=3

**Why this case**: tests Marcus's unwritten rule #2 — first-time customer → warmer tone. Note: this is a tone flag, NOT an escalation. The wedge still auto-sends, but the tone of the comm shifts.

**FNOL input**:
```
state: NY
channel: web
lob: non_std_personal_auto
claimant_name: Ms. Garcia
first_time_customer: TRUE  ← the trigger
incident_description: Side-swiped on the highway by a driver who didn't signal.
```

**Expected**:
- Decision = `auto_send`
- Draft must contain: "Garcia"

**What it tests**: rule 2 fires the `tone_warmer` flag, which the Drafter consumes to produce a more empathetic comm. The eval is loose here because tone is hard to grade with substring matching — a future ToneSupervisor agent (LLM-as-judge) will grade it more rigorously.

**If this fails**: either the policy library isn't passing the tone flag, or the Drafter isn't consuming it. Both are tractable bugs.

---

# How to extend the eval suite

Add cases to `evals/cases/seed.jsonl`. One JSON object per line. The grading dimensions are:

```json
{
  "case_id": "your_case_name",
  "weight": 5,
  "fnol": { ... full FNOL input ... },
  "expected": {
    "decision": "auto_send",
    "must_contain": ["Patel", "10"],
    "must_not_contain": ["30 days"],
    "rules_fired": ["policy.rule_1_child_or_elderly_party"]
  }
}
```

Target ~25 total cases for the wedge proposal. Categories to add:

1. **More Marcus rule combinations** — child + first-time, elderly + prior-claim, etc. (10x weight)
2. **State-strictness coverage** — NJ, PA, NY, MA all need at least one case with each rule. (5-10x weight)
3. **Janet's "tells"** — narratives containing "I didn't have time to react", "the lawyered-up paragraph", etc. Adversarial set. (10x weight on misclassification)
4. **Comm-quality bar** — drafts that should fail Janet's 5-element bar (form letter, missing name, generic timeline). Will need ToneSupervisor to grade. (3x weight)
5. **Edge of policy** — claims at the boundary of v1 scope (BI-adjacent, coverage-adjacent). Should always escalate. (10x weight)
6. **Channel mix** — same FNOL via web vs agent portal vs email. Should produce equivalent decisions. (1x weight)

Keep adding cases when you find a failure mode in production. the agent development lifecycle: every annotated conversation becomes a test. Every fix becomes a regression case.

---

# When to bump k

| Stage | k value | Reason |
|---|---|---|
| Day-1 dev | 1 | Fast feedback loop |
| End of week 2 | 3 | Mild consistency check |
| Pre-rollout (week 4) | 5 |  production threshold |
| Post-incident | 10 | High-stakes deployment confidence |

If pass rate drops as k goes up, the variance is in places that matter. Tighten the prompt or add a deterministic guardrail.

---

# Appendix — the raw `seed.jsonl` cases

The actual file content. One JSON object per line in the source file; pretty-printed below for readability.

## Case 1 — `well_handled_NJ_web_01` (weight=1)

```
{
  "case_id": "well_handled_NJ_web_01",
  "weight": 1,
  "fnol": {
    "claim_id": "CL-2026-NJ-10001",
    "policy_id": "POL-100001",
    "channel": "web",
    "lob": "comm_auto",
    "state": "NJ",
    "claimant_name": "Mr. Patel",
    "incident_date": "2026-05-07",
    "incident_description": "Fender bender at the UPS Edison NJ distribution center.",
    "estimated_damage": 2400,
    "first_time_customer": false,
    "has_child_or_elderly_party": false,
    "has_prior_claim_in_12_months": false,
    "touches_coverage_decision": false,
    "touches_settlement_decision": false
  },
  "expected": {
    "decision": "auto_send",
    "must_contain": ["Patel", "10"],
    "must_not_contain": ["30 days"]
  }
}
```

## Case 2 — `policy_rule_elderly_NJ_10x` (weight=10)

```
{
  "case_id": "policy_rule_elderly_NJ_10x",
  "weight": 10,
  "fnol": {
    "claim_id": "CL-2026-NJ-10002",
    "policy_id": "POL-100002",
    "channel": "web",
    "lob": "non_std_personal_auto",
    "state": "NJ",
    "claimant_name": "Mrs. Wong",
    "incident_date": "2026-05-08",
    "incident_description": "I rear-ended someone on the Garden State Parkway.",
    "estimated_damage": 1800,
    "first_time_customer": false,
    "has_child_or_elderly_party": true,
    "has_prior_claim_in_12_months": false,
    "touches_coverage_decision": false,
    "touches_settlement_decision": false
  },
  "expected": {
    "decision": "adjuster_review",
    "rules_fired": ["policy.rule_1_child_or_elderly_party"]
  }
}
```

## Case 3 — `policy_rule_prior_claim_NJ_10x` (weight=10)

```
{
  "case_id": "policy_rule_prior_claim_NJ_10x",
  "weight": 10,
  "fnol": {
    "claim_id": "CL-2026-NJ-10003",
    "policy_id": "POL-100003",
    "channel": "agent_portal",
    "lob": "comm_auto",
    "state": "NJ",
    "claimant_name": "Acme Distributors LLC",
    "incident_date": "2026-05-08",
    "incident_description": "Fleet vehicle damaged in parking lot at our Newark warehouse.",
    "estimated_damage": 3200,
    "first_time_customer": false,
    "has_child_or_elderly_party": false,
    "has_prior_claim_in_12_months": true,
    "touches_coverage_decision": false,
    "touches_settlement_decision": false
  },
  "expected": {
    "decision": "adjuster_review",
    "rules_fired": ["policy.rule_3_prior_claim_in_12_months"]
  }
}
```

## Case 4 — `stale_template_PA_5x` (weight=5)

```
{
  "case_id": "stale_template_PA_5x",
  "weight": 5,
  "fnol": {
    "claim_id": "CL-2026-PA-10004",
    "policy_id": "POL-100004",
    "channel": "web",
    "lob": "comm_auto",
    "state": "PA",
    "claimant_name": "Mr. Sullivan",
    "incident_date": "2026-05-08",
    "incident_description": "Hit by another vehicle while parked outside a Wawa near Philadelphia.",
    "estimated_damage": 2100,
    "first_time_customer": true,
    "has_child_or_elderly_party": false,
    "has_prior_claim_in_12_months": false,
    "touches_coverage_decision": false,
    "touches_settlement_decision": false
  },
  "expected": {
    "decision": "auto_send",
    "must_not_contain": ["30 days"]
  }
}
```

## Case 5 — `first_time_warmth_NY_3x` (weight=3)

```
{
  "case_id": "first_time_warmth_NY_3x",
  "weight": 3,
  "fnol": {
    "claim_id": "CL-2026-NY-10005",
    "policy_id": "POL-100005",
    "channel": "web",
    "lob": "non_std_personal_auto",
    "state": "NY",
    "claimant_name": "Ms. Garcia",
    "incident_date": "2026-05-08",
    "incident_description": "Side-swiped on the highway by a driver who didn't signal.",
    "estimated_damage": 1600,
    "first_time_customer": true,
    "has_child_or_elderly_party": false,
    "has_prior_claim_in_12_months": false,
    "touches_coverage_decision": false,
    "touches_settlement_decision": false
  },
  "expected": {
    "decision": "auto_send",
    "must_contain": ["Garcia"]
  }
}
```
