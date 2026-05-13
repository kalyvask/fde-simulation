# Data Pull Spec for Greg — Calder FNOL Discovery Sample

> Sub-deliverable referenced in the kickoff recap email to Maria. Send to Greg, CC Maria.
> **By**: EOD tomorrow (so the data team has 5 business days to pull)

## Subject

`[Calder] Data pull spec for FNOL discovery — 500 claims, last 6mo`

## Body

Greg,

Per the recap email to Maria, here are the specs for the 500-claim historical pull I'd like the data team to put together. Anything not feasible as scoped, flag back and I'll re-scope.

### Specifics

| | |
|---|---|
| **Volume** | 500 claims |
| **Time window** | Last 6 months from today |
| **Lines of business** | First-party physical damage — both commercial auto and non-standard personal auto |
| **Channel mix** | Stratified to match production: ~55% phone, ~25% web/app, ~12% agent portal, ~8% email |
| **Composition** | 70% routine, 20% complex/escalated, 10% with quality flags. Tom + Sienna can help select the 10%. |
| **Anonymization** | PII (name, address, phone, email) hashed at source. Claim numbers replaced with synthetic IDs. Free-text narratives preserved verbatim — no scrubbing of incident detail. |
| **Format** | CSV with structured policy/claim fields + JSON with the narrative blob and any associated docs. Whichever is easier for the data team — both is fine. |
| **Where it lands** | Calder's secure file transfer initially. Will move into our SOC2-Type-II tenant once Rachel signs off on the data one-pager (Friday this week). Bucket details to follow. |

### Why this composition

- **500** is enough for a defensible eval suite without burdening the data team
- The **10% quality-flagged** slice is the most valuable — it lets us calibrate the agent on the cases that actually matter
- **Stratified channel mix** ensures the wedge slice (web + agent portal first) has enough data without losing visibility on phone for v2

### Owner-side action

| Step | Owner | Date |
|---|---|---|
| Confirm pull is feasible as scoped | Greg + data team | EOD Friday this week |
| Rachel sign-off on data destination | Maria → Rachel | Friday this week |
| Data delivered | Greg's data team | EOD Tuesday next week |

If 500 is too high a lift in 5 days, 250 is acceptable provided the 10% quality-flagged slice is preserved at full count.

Thanks,
Alex
