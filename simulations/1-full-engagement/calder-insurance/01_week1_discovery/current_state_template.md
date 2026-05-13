# Current-State Information Request

This is what you'd hand the customer at the end of kickoff and ask them to fill within 5 business days. Five buckets, named owners.

## Bucket 1 — Volume & cost (Owner: Finance + Operations)

- [ ] Claims per day, last 12 months, by line of business and by state
- [ ] Channel mix (phone / web / app / agent portal / email), trended
- [ ] $/claim by handling tier (BPO L1, internal L2, complex, SIU)
- [ ] BPO spend by vendor with contract terms and end dates
- [ ] Internal claims FTE cost by tier
- [ ] Current LAE ratio by line, vs industry benchmark
- [ ] Last 12 months of catastrophe-driven claim spikes (volume + duration)

## Bucket 2 — Workflow trace (Owner: Operations + IT)

- [ ] FNOL channel inventory + the routing rules per channel
- [ ] System of record (Guidewire ClaimCenter version + customizations summary)
- [ ] Document handling flow (where police reports, repair estimates, photos, medical bills land)
- [ ] Adjuster authority thresholds (auto-pay limit, settle limit, by tier)
- [ ] Hand-off rules to SIU, total-loss, litigation
- [ ] Communication touchpoints with claimants (template inventory)

## Bucket 3 — Quality baseline (Owner: Quality + Compliance)

- [ ] Cycle-time distributions: FNOL → first-touch, FNOL → first-payment, FNOL → close
- [ ] Estimated leakage % (over and under-payment)
- [ ] NPS at FNOL and at close, last 4 quarters
- [ ] Last 12 months: regulatory complaints (state DOI), market-conduct findings, large-loss surprises
- [ ] Internal audit findings on claims handling, last 12 months

## Bucket 4 — Tech & data (Owner: CIO + CISO)

- [ ] Integration inventory: Guidewire APIs available, fraud tools (Verisk, Shift Tech), comms (Twilio, etc.), CRM
- [ ] PII / PHI map: which fields exist where, HIPAA exposure on bodily-injury claims
- [ ] Data residency requirements
- [ ] BAA status with Anthropic, OpenAI, Google
- [ ] Existing model-vendor approvals, procurement timeline for new ones
- [ ] Logging stack and retention policy

## Bucket 5 — Failure log (Owner: Claims + SIU + Quality)

- [ ] 10 historical claims where adjusters caught something subtle (positive eval examples)
- [ ] 10 historical claims where something material was missed (hardest-case eval examples)
- [ ] 5 fraud cases that should have been flagged earlier (SIU eval seed)
- [ ] 5 customer complaints traceable to a workflow failure (process eval seed)

## Why this list works

- It's organized by **owner**, so the customer can parallelize the gathering.
- Every item maps to a downstream artifact (eval set, integration design, savings model, risk register).
- The "failure log" bucket is the single most underrated ask — it gives you eval data the customer's training data won't.

## Use

Hand to the customer at kickoff. Track completion. Anything missing by day 5 is a signal: either the customer doesn't have it (real constraint) or the political will isn't there (different problem).
