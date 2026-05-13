# Calder Specialty Insurance — Customer Brief

> Calder is a fictional composite based on real PE-backed mid-market specialty auto carriers. All numbers, names, and quotes are illustrative.

## At a glance

| | |
|---|---|
| Industry | Specialty Property & Casualty insurance |
| Lines of business | Commercial auto, non-standard personal auto |
| GWP | ~$300M |
| Footprint | 14 Northeast US states |
| Headcount | 800 (180 in claims) |
| Ownership | PE-backed; acquired 2023 by mid-market sponsor |
| Tech stack | Guidewire ClaimCenter (v10), Salesforce, Twilio, Verisk fraud, two BPOs |
| Why now | Board EBITDA target: 30% claims-ops cost reduction in 18 months |

## The presenting problem (COO's words on the kickoff call)

> "Our claims-handling cost is up 18% in two years. FNOL-to-first-touch is averaging 4.2 hours against a 1-hour SLA. We're paying two BPOs $42 a claim and the quality is uneven — last quarter we had two market-conduct findings tied to BPO mishandling. The board wants a number, not a pilot. I need 30% out of claims ops within 18 months and I'd rather absorb work back in-house with AI than renew the BPO contracts."

## Stakeholders

| Role | Name (illustrative) | Why they matter |
|---|---|---|
| Chief Claims Officer | Maria Vasquez | Economic buyer. Owns the 30% target. |
| SVP Claims Operations | Greg Hadley | Champion candidate. Owns daily workflow. |
| Director, FNOL Operations | Priya Shah | Operator. Knows where the workflow actually breaks. |
| Frontline claims adjusters | (3-5 to interview) | Primary users. Know the soul-crushing parts. |
| Quality / Audit Lead | Tom Reilly | Defines a "bad close." Owns regulator-facing exposure. |
| SIU Lead (fraud) | Dana Kowalski | Highest-risk reviewer. Defines the fraud-flag bar. |
| CIO | Anil Gupta | Owns Guidewire footprint and integrations. |
| CISO | Rachel Nieman | Decides whether claim data can leave the tenant. |
| Compliance Officer | Marcus Hill | State DOI rules, Unfair Claims Settlement Practices Act. |
| Finance / Actuary | Lin Zhao | Owns the LAE ratio and the savings model. |
| BPO Contract Owner | Kevin Park | Knows BPO economics and exit terms. |

## Current-state numbers (the shape of the problem)

- Claims/day: ~600 (peaks of 1,200 after weather events)
- Channel mix: 55% phone, 25% web/app, 12% agent portal, 8% email
- Cost/claim handled by tier: $42 (BPO L1), $78 (internal L2), $310 (complex/SIU)
- BPO spend: ~$11M/yr across two vendors
- Internal claims FTE cost: ~$22M/yr (180 staff)
- LAE ratio: 12.4% of premium (industry benchmark for line: ~10.8%)
- Cycle time: median FNOL → first-touch 4.2h, FNOL → first-payment 9.1 days
- Quality: estimated 4-6% claim leakage (over/underpayment)
- Customer: NPS at FNOL = 31

## The opportunity (back-of-envelope)

Cutting LAE ratio from 12.4% to 11.0% on $300M GWP = $4.2M annual savings.
Replacing one BPO contract ($6M/yr) with an in-house AI workforce + 30% retained human review = ~$3.5M net annual savings.
Combined target: ~$7-8M/yr, sustainable, before reinvestment in new lines.

## The constraints (named upfront)

- **Regulatory**: 14 state DOIs; Unfair Claims Settlement Practices Act applies in all of them. Some states require human licensed adjusters to make coverage decisions.
- **Data residency**: PII + medical records (PHI) on bodily-injury claims. Anthropic BAA needed; OpenAI BAA in procurement review.
- **System**: Guidewire ClaimCenter is heavily customized. Any integration goes through a slow internal API gateway team.
- **Political**: Two BPO contracts have ~12 months left. Replacing them is the easiest sell. Replacing internal staff is not.
- **Audit**: All AI-assisted decisions need a human-readable trace for the next NAIC market-conduct exam.

## The bet (working hypothesis going into Week 1)

The narrowest, highest-impact wedge is **auto-pay-eligible triage** on first-party physical damage claims under $2,500: ingest FNOL narrative + photos + repair estimate, validate against policy, route to auto-pay or to a human adjuster. Estimated 25% of claim volume, currently sent to BPO L1 at $42/claim. If we get to 80% straight-through processing on this slice with audit-grade traces, we replace ~$2.5M of BPO spend and prove the workforce pattern for harder slices.

This is the hypothesis. Discovery's job is to confirm or break it.
