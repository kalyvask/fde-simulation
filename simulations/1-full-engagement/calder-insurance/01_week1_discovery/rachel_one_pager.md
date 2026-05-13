# Data Handling One-Pager — Calder FNOL AI Workforce

> For: Rachel Nieman, CISO
> From: FDE Lead
> Sign-off requested by: Friday this week
> Length: half a page (per Maria)

## What we're building

An AI workforce that auto-acknowledges incoming FNOL claims and drafts first-status-updates to claimants, on first-party physical damage claims, web and agent-portal channels first. Goal: cut FNOL-to-first-touch from 4.2h to <30min while addressing the comms-layer pattern that triggered the two recent market-conduct findings. **No coverage decisions. No bodily-injury claims. No writes to Guidewire in v1.**

## Data we touch

| Type | Source | Sensitivity |
|---|---|---|
| Structured claim fields (policy ID, coverage, claim amount, dates) | Guidewire ClaimCenter, read-only API | Internal |
| Claimant narratives (loss description) | Guidewire FNOL records | PII |
| Claimant contact (name, phone, email) | Guidewire | PII |
| Bodily-injury medical refs | n/a — BI claims excluded from v1 | (PHI not touched) |

PII hashed at intake. Narratives preserved verbatim (required for accurate extraction). PHI not touched in v1.

## Where it lands

Our SOC2-Type-II vendor tenant, us-east region. No cross-border data movement. Encryption at rest and in transit, customer-managed keys.

## Access control

- **2 named engineers + 1 PM** (me) on the engagement team. SSO + MFA. Role-based; no admin.
- **Read-only** access to Calder claim data. Write access scoped to the agent's draft-output bucket only.
- All access logged to Calder's existing SIEM.

## Retention

- All ingested data deleted at end of engagement (target: end of week 4) unless converted to ongoing.
- Prompt + response logs: 90 days for audit/eval, then deleted.
- Ongoing-engagement retention policy negotiated separately if/when extension is agreed.

## Vendor + BAA

- **Anthropic Claude** (primary): BAA executed. Default opt-out from training-data sharing.
- **OpenAI** (secondary, possible): in Calder procurement review. Not used in v1.
- No other third-party AI services.

## Logging + auditability

- Every prompt and response logged to Calder's SIEM. 90d retention.
- Decision-trace artifact for every agent action (input, model version, retrieved context, output) — designed for NAIC market-conduct examiner review.
- Agent versioning: every release is an immutable snapshot tied to model version + knowledge-base hash.

## Risk mitigations

| Risk | Mitigation |
|---|---|
| Hallucinated claim detail in claimant comms | Deterministic field extraction; LLM synthesizes narrative only |
| Wrong timeline given to claimant | Deterministic timeline rule, not LLM |
| BI/PHI exposure | BI claims excluded from v1 |
| Data residency violation | All data stays in us-east, vendor-tenant only |
| Vendor BAA gap | OpenAI not used until Calder procurement clears |

## What I'm asking from you

- Sign-off on the above by EOD Friday this week
- Standing 15-min biweekly with me starting week 3 to review logs and any incident
- Veto authority on any data destination not listed above

Any concern, flag and I'll redesign before we touch any data.

— Alex
