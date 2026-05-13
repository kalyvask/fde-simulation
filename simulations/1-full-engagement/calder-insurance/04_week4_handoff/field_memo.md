# Field Memo — Calder FNOL Wedge

> **From**: FDE Lead
> **To**: AI Lab Applied AI / Research / Product
> **Date**: End of week 4
> **Re**: What we shipped, what blocked us, what to fix in the platform

> Forward Deployed roles at frontier labs typically require sharing field feedback with Research and Product to influence model and product development. This memo is that artifact.

## What we shipped

A 4-week wedge for Calder Specialty Insurance: AI workforce that auto-acknowledges and drafts first-status-updates for FNOL claims, web + agent-portal channels, first-party physical damage. 7 specialized agents with a hybrid det+LLM architecture. 80% straight-through, 20% adjuster review. 96% weighted eval pass rate at pass^k=5 across 80 cases.

Production rollout started Monday week 5. Hassan owns operations; Sienna owns weekly eval review; Marcus biweekly with Maria for the first 90 days.

## What worked

**Hybrid det+LLM with deterministic high-stakes routing.** The compliance critic, policy library, and routing decision are all deterministic Python. The LLM (Claude Sonnet) handles only natural-language synthesis — drafting comms — and grading them via LLM-as-judge. This containment of LLM stochasticity to the natural-language surface is the architectural pattern that made the engagement defensible to a default-no compliance officer.

**Audit trace as first-class artifact.** Every agent step writes to an AuditTrace dataclass at the framework level. The examiner-readable HTML renderer takes 1 second to produce a NAIC-attestable trace. Tom's three sign-off criteria all met without a separate observability project.

**Adversarial eval cases sourced from interview signals.** 25 of the 80 cases came from specific phrases, "tells," or rule combinations stakeholders volunteered. The eval suite is a behavioral encoding of the discovery work, not a synthetic benchmark.

**The disarmament technique with the default-no skeptic.** Marcus shifted from gatekeeper to design partner in 20 seconds, week 1. Cell-number gesture week 1. Pre-demo synchronization week 4. The pattern generalizes to any compliance / risk / security counterpart at any enterprise.

## What blocked us

### Model behaviors

1. **Vague-timeline drift on real Claude**. The Drafter's system prompt explicitly forbade "30 days"; Claude introduced "soon" and "shortly" instead, which NY's strict-pattern enforcement would cite. Required a follow-on prompt update to forbid ALL vague timeline language. **Suggestion to Anthropic**: when Claude is given a forbidden-phrase list, it would help if the model treated semantic equivalents as in-scope of the prohibition. Currently it treats the list literally, which means we have to enumerate semantic variations exhaustively.

2. **Over-summarization of long claimant narratives**. On incident descriptions over 200 words, Claude consistently lost detail (e.g., the role of a third vehicle in a multi-car claim). The ToneSupervisor caught some; some leaked. Required adding a "preserve all parties named in the original" element to the bar. **Suggestion**: on long-context summarization tasks, an explicit "do not omit named entities" instruction should be a primitive in the SDK.

3. **Diacritics in claimant names occasionally lost**. "Ms. García" rendered as "Ms. Garcia" in ~5% of drafts. We added a deterministic byte-identity check on claimant_name as a guardrail. **Suggestion**: tokenizer-level guidance that names should pass through unchanged would be a common-case pattern worth supporting first-class.

### Product gaps

4. **No first-class "immutable agent snapshot" primitive.** the company's ADLC pattern is right and we re-implemented it manually (model_version + prompt + knowledge-base hash). A platform primitive that bundles these as one versioned artifact would have saved a week of plumbing. The MCP and Agent SDK roadmap should consider this.

5. **No native LLM-as-judge calibration tooling.** Brier score, reliability diagrams, calibration curves — all DIY. Calibration is the gap between "the eval passes" and "we trust the routing decision." A platform-level calibration helper would land hard with FDE customers.

6. **No examiner-trace renderer template.** We built ours; every regulated-industry deployment will rebuild theirs. A reference renderer Anthropic publishes (HTML + PDF, customizable) would compress the audit-readiness work for every healthcare/finance/insurance FDE customer.

### Platform investments worth making

7. **State-aware policy libraries.** Insurance has 50 state DOIs; healthcare has 50 state Medicaid agencies; finance has multiple regulators per state. A first-class "regulatory variance" data structure with versioning, diffing, and audit hooks would be a moat.  has a primitive for this; Anthropic could go deeper.

8. **Death-spiral monitor primitive.** Rolling-window drift detection for accuracy / latency / escalation rate is a per-customer build today. As a platform primitive (with PagerDuty / Slack / OpsGenie connectors prebuilt), it'd be a click-deploy.

## What I learned that I wish I'd known earlier

- **The political work earns the technical work.** The Marcus disarmament made every subsequent design decision easier because it removed the "compliance-will-block" tax from every conversation.
- **Janet's adoption gate is the actual ship gate, not Tom's eval threshold.** I knew this conceptually; I underweighted it in week 2. The 20-draft review in week 3 was the critical milestone.
- **"Narrow over late" is the buyer's bar, not the FDE's.** Maria gave me this frame in week 3 weekly; it should have been my default from week 1.

## Reusability for the next engagement

50%+ of what shipped is portable to the next regulated-industry FDE deployment:

- The hybrid det+LLM pattern (workforce, BaseAgent, AuditTrace) — directly portable
- The eval harness with pass^k + weighted grading — directly portable
- The examiner-readable HTML renderer — portable with cosmetic theming
- The death-spiral monitor — directly portable
- The disarmament technique for default-no skeptics — directly portable

What needs per-customer work:
- Domain-specific policy library (insurance vs healthcare vs finance)
- Stakeholder map (different stakeholders per industry)
- Eval cases (must be sourced from per-customer discovery)
- The wedge itself (must answer the per-customer kill-criteria)

## Open ask back to Anthropic

If any of suggestions 1-8 above resonate with the team, I'm available for a deeper-dive call. Cell on file.

— Alex
