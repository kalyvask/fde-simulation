# AI Logic Doc — Template

> The artifact a Strategist hands to a Forward Deployed Engineer to brief them on what to build. Common in AI workforce platforms where the FDE is far from discovery and needs a tight, structured handoff.
>
> Length: 1-2 pages. If it's longer than that, it's not a handoff doc — it's a status report.

## When to write this

After discovery is done, before engineering starts. The doc is the input contract for the FDE team. It's the artifact that lets engineering start building without re-doing discovery.

## When to reference this in an interview

If the interviewer asks "how would you communicate to the FDE what to build?", a strong answer is:

> "I'd write an AI Logic Doc — 1-2 pages. It has the input schema, the output schema, the trust levels per step, the eval cases, and what's explicitly out of scope. The eval suite is one part of the doc, not the whole thing."

## The template

```markdown
# AI Logic Doc — [Customer Name] / [Workflow Name]

**Strategist**: [Name]
**Date**: [Date]
**For**: [FDE lead + engineering team]
**Project length**: [N weeks; e.g., 8-10 weeks]

---

## 1. The wedge (one paragraph)

[1-3 sentences. What the agent does. What it does NOT do. The single sentence is more important than 3.]

Example: "Build a citation-grounded earnings-note drafter for senior TMT analysts. Agent reads transcript + KPIs + prior-quarter note; produces draft. Agent does NOT touch M&A commentary, position sizing, multi-quarter retrieval, or any write to the PMS. Human-in-loop on every borderline case."

## 2. Metrics in the contract

| Metric | Baseline (today) | Target (by end of engagement) | Owner of the number |
|---|---|---|---|
| [Primary KPI] | [Number] | [Number] | [Stakeholder name] |
| [Secondary KPI] | [Number] | [Number] | [Stakeholder name] |
| [Quality threshold] | [Number] | [Number] | [Stakeholder name] |

Example for change-management:
| Metric | Baseline | Target | Owner |
|---|---|---|---|
| Time from request to change order | 4 days | 4 hours | VP Global Services |
| Error rate on bill-of-materials updates | 12% | <2% | VP Global Services |
| Manual hours per change request | 90 min | <15 min | VP Global Services |

## 3. The 3-lens scaffold (filled in)

### Customer
- Who (specific persona): [Name + role + tenure]
- Emotional state: [stressed / anxious / exhausted / curious]
- JTBD top 3: [list]
- Why failing today: [specific friction]
- What's hard (root cause): [systemic issue]

### Product
- Intent: [what the agent does]
- In scope: [3-5 concrete capabilities]
- Out of scope (equally explicit): [3-5 things the agent will NOT do, with the reason for each]
- Trust levels: act / ask / escalate per capability
- Fallback: [what happens at low confidence]
- Metric + tension: [primary metric; the tension; which side you protect]

### Technical
- Read access: [specific data sources]
- Write access: [NONE in v1; what gets written and where after v1.5+]
- Data freshness: [live / cached / batched per source]
- One specific integration risk: [risk + mitigation]
- Validation plan: PoC + eval + compliance + closed beta

## 4. Agent architecture

### Workforce decomposition (5-8 agents)

| # | Agent | Shape (from catalog) | Tier | Det / LLM | Why |
|---|---|---|---|---|---|
| 1 | [Name] | [Shape] | [Tier] | [Det/LLM] | [Rationale] |
| 2 | ... | ... | ... | ... | ... |

### Orchestration pattern

[Sequential / Parallel fan-out / Conditional branching / Loop with retry]

Sketch:
```
[Agent 1] → [Agent 2] → [Agent 3] → [Critic + Validator parallel] → Branch:
  if any critic flags → human queue with reasoning trace
  else → holding queue + audit trace
```

### Integration map

| Source | Read pattern | Write pattern | Tier |
|---|---|---|---|
| [System 1] | API / DB direct / Event stream / File ingestion | NONE / Holding queue / Approval-gated / Direct | 1 / 1.5 / 2 |
| ... | ... | ... | ... |

## 5. The deterministic / non-deterministic split (output-schema framing)

| Layer | Det or LLM | Why |
|---|---|---|
| Output schema (target format) | Deterministic | Required by downstream system |
| Validation of output against schema | Deterministic | Rules problem |
| Parsing input → structured fields | LLM | Variable input formats |
| Human-in-loop on low-confidence parses | Human | Trust seam |

## 6. Eval suite (10-15 representative cases — full suite is in `evals/cases/`)

| Case ID | Input | Expected output | Weight | Notes |
|---|---|---|---|---|
| `happy_01` | [Example input] | [Expected] | 1 | Common case |
| `adversarial_mnpi_01` | [Adversarial input] | [Expected: block] | 10 | Tests MNPI scrubber |
| `edge_split_coding` | [Edge case] | [Expected: escalate] | 5 | Split-coding scenario |
| ... | ... | ... | ... | ... |

Pass^k target: **k=5, variance ≤5%** before production deploy.

## 7. Sign-off criteria (the 3 gates)

| Criterion | Owner | Status |
|---|---|---|
| Pass^k=5 with variance ≤5% on weighted eval | [Tech owner] | [ ] |
| Compliance / regulatory sign-off | [Compliance owner] | [ ] |
| Senior-user review of N sample outputs | [Lead user] | [ ] |

No production deploy until all 3 are ✓.

## 8. Out of scope (explicit — what NOT to build in v1)

- [Item 1, with reason]
- [Item 2, with reason]
- [Item 3, with reason]

These are v1.5 or v2 conversations, gated on Tier 1 being clean for 90 days.

## 9. Risks the FDE should know about

| Risk | Bucket | Mitigation | Owner | Detection signal |
|---|---|---|---|---|
| [Risk 1] | Business / UX / Technical | [Mitigation] | [Owner] | [How we detect it's happening] |
| ... | ... | ... | ... | ... |

## 10. Open questions for engineering

1. [Specific question for FDE]
2. [Specific question for FDE]
3. [Specific question for FDE]

## 11. Project plan

| Week | Phase | Deliverable | Sign-off |
|---|---|---|---|
| 1 | Discovery + alignment | Discovery memo + wedge proposal + this AI Logic Doc | Strategist + customer champion |
| 2 | Build foundation | Agents 1-3 implemented + initial eval suite | Tech lead |
| 3 | Build remaining + integration | All agents wired; passing happy-path eval | Tech lead |
| 4 | Hardening + sign-offs | Pass^k=5 + compliance + senior-user review | All 3 sign-off owners |

---

**This doc is the input contract.** Changes after the FDE starts building require a written addendum. Scope changes mid-engagement are the #1 cause of slipped deadlines.
```

## How to use this template

1. Copy the entire template into a new file in your repo at `ai_logic_doc.md`
2. Fill it in based on your discovery + solution work
3. Review it with your customer champion BEFORE handing to the FDE team
4. Hand it off at the start of week 2 (or whenever build starts)
5. Treat it as the source of truth for scope

## What good AI Logic Docs do that bad ones don't

| Good | Bad |
|---|---|
| 1-2 pages, scannable in 5 min | 10+ pages, unreadable |
| Out-of-scope is explicit and weighted equally to in-scope | Only describes what TO build |
| Has the baseline + target metrics from the contract | Generic "improve efficiency" |
| Names the trust levels per capability | "Human-in-the-loop" without specifics |
| Has 10-15 representative eval cases | Promises a full eval suite "later" |
| Names the 3 sign-off criteria with owners | "Compliance sign-off" without naming Mei/Alex/equivalent |
| Lists open questions for engineering | Pretends discovery answered everything |

## The handoff meeting

After writing the doc, run a 60-min handoff meeting with the FDE team:
1. Walk through the wedge in 5 min
2. Walk through the architecture in 15 min
3. Walk through the eval cases in 15 min
4. Take questions for 20 min
5. Capture open questions in writing in the doc

The doc + handoff meeting are what good FDE engagements run on. Skip either and the engineering team is doing discovery you should have done.
