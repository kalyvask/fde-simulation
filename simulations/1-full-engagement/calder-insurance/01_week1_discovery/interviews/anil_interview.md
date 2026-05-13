# Anil Gupta — CIO — Thursday 4:00pm ET, Zoom (45 min)

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Constructed dialogue; methodology authentic.

## Setup

Thursday 4:00 PM ET. Anil in his office, headset on. Engineer demeanor — direct, deeply technical, not interested in throat-clearing. Minimal small talk. He has a list of his own questions visible in his Notion.

## Selected exchanges

**Alex** *(opening, cuts to it)*: "Anil, before I ask anything — Maria said you have a 6-week integration queue and we need to get on it. The question I most need answered today is what we'd have to scope for you to put us on the queue this week instead of in 6."

**Anil** *(slight smile — appreciates the directness)*: "Cut to it, OK. If it's read-only on Guidewire — no writes back to ClaimCenter — I can put you on the queue this week. Read-write is 6 weeks because it goes through change control. So your wedge has to be: agent drafts, adjuster (or workflow) commits manually."

**Alex**: "Done. The wedge is drafts only. Adjuster review queue catches the 20% the agent isn't confident on; the 80% goes to a human one-click commit. No writes back from the agent."

**Anil**: "Then I can get you sandbox access by Wednesday next week and Kayla available 10h/week starting next week. Walk me through your design."

**Alex**: "Footprint walk first. Vanilla vs customized? APIs exposed?"

**Anil**: "ClaimCenter v10. Four major customizations: custom routing engine, BPO handoff via SOAP API, payment authority overrides for our specialty lines, fraud signals from Verisk. APIs exposed: claim retrieval (REST), policy lookup (REST), status update (REST). All behind our internal API gateway with OAuth client-credentials. The gateway has rate limits — 100 req/sec per client, which should be fine for your wedge. Behind the gateway, slow approval: direct DB, Guidewire admin, payment system. You don't need any of those."

**Alex**: "Sandbox?"

**Anil**: "Dev tenant exists. Last refreshed 6 months ago. Has synthetic data. For your prototype it's fine — for proving you handle real-world dirt, you'll want the real anonymized pull from Greg's team, not the sandbox synthetic data. So use the sandbox for integration tests and the real pull for accuracy evals."

**Alex**: "Scar tissue. What AI/ML projects have you tried in the past 2-3 years and what got blocked?"

**Anil** *(more animated)*: "2023 RPA project — UiPath. Killed at month 9. Three reasons: (1) maintenance cost > savings as the source systems changed, (2) Janet and her team routed around it because it was unreliable, (3) no one owned it after the consultant left. The reason I'm telling you this is your project will fail in the same ways unless you have answers for all three. Maintenance: how does your system handle when Guidewire's API changes? Adoption: how do you not become unreliable to the point where adjusters route around you? Ownership: who owns this on our side after week 4?"

**Alex**: "Fair questions. Maintenance: agent skills are version-controlled and the deterministic rules are testable, so a Guidewire schema change shows up as a failing test before it shows up as bad output. Adoption: confidence calibration plus the one-click escalate that doesn't punish the adjuster — that's a design choice from the adjuster interviews. Ownership: handoff to Hassan + Kayla, with Devorah on compliance. Hassan as the operational owner is something I'd want your buy-in on because he sits in Priya's org but he'd need a dotted line to your team for the integration maintenance."

**Anil** *(considers)*: "Hassan's a smart guy. Built that side spreadsheet that's basically a poor man's version of what you're building. I'd be fine with the dotted-line model. I'd want him in our weekly platform standup so the integration maintenance doesn't surprise us."

**Alex**: "Done. BAA status?"

**Anil**: "Anthropic in place. OpenAI is in procurement, probably another 6 weeks. Google not pursued. So Anthropic-only for v1 is the right call."

**Alex**: "Observability stack?"

**Anil**: "Splunk for everything customer-data adjacent. ELK for dev-side app logs. We'll plug your prompt/response logs into Splunk with a 90-day retention. I'll get Kayla on standing up the ingestion pipeline next week."

**Alex**: "Last one. What worries you most about this engagement that I haven't asked about?"

**Anil** *(long pause — actually thinking)*: "Honestly? That you'll do good work in 4 weeks and then nobody owns it after you leave and it'll be the 2023 RPA story all over again. The 4-week sprint isn't the problem. The 90 days after is the problem. Talk to Maria about ongoing-engagement structure before you ship — not after."

**Alex**: "I'll have that conversation with Maria at the next standing weekly. Good steer. Thank you."

*(Wraps at 39 minutes.)*

## Post-interview captures

### Integration scope (the deal that unlocked the queue)
- **v1 = read-only on Guidewire**. Agent drafts; adjuster commits.
- Sandbox access by Wednesday next week
- Kayla 10h/week starting next week

### Guidewire footprint
- ClaimCenter v10
- 4 major customizations: routing engine, BPO handoff (SOAP), payment authority, Verisk fraud signals
- APIs exposed (REST, behind gateway, OAuth client-credentials, 100 req/sec rate limit): claim retrieval, policy lookup, status update
- APIs slow-approval: direct DB, Guidewire admin, payment system — none needed in v1
- Dev tenant: 6 months stale, fine for integration tests, NOT fine for accuracy evals (use real pull)

### Scar tissue (must engineer against)
- 2023 RPA killed at month 9 due to: (1) maintenance cost > savings, (2) Janet's team routed around it, (3) no ownership post-consultant-departure
- Our differentiators: version-controlled skills + testable deterministic rules + Hassan as operational owner

### Stack details
- BAA: Anthropic in place; OpenAI in procurement (6 weeks); Google not pursued
- Observability: Splunk for customer-data-adjacent logs (90d retention); ELK for app logs
- Kayla owns the Splunk ingestion pipeline standup

### Glossary updates
- **SOAP**: legacy API protocol (Guidewire BPO handoff)
- **OAuth client-credentials**: machine-to-machine auth pattern
- **Splunk**: enterprise log/SIEM platform

### Stakeholder map updates
- Anil: ALLY (negotiated read-only deal in real time, offered Hassan-as-owner buy-in)
- Kayla: TECHNICAL PARTNER (named, 10h/week, owns Splunk ingestion)
- Hassan: now formally proposed as ongoing operational owner, with dotted line to Anil's team

### Working hypothesis updates
- v1 wedge integration architecture: read-only Guidewire APIs through gateway; agent drafts; adjuster commits via existing UI or new minimal review queue UI
- Sandbox = integration tests; real anonymized pull = accuracy evals
- Splunk = the observability + audit-trace artifact storage
- Hassan operational ownership is the answer to the scar-tissue ownership gap
- The 90-days-after question is now a Maria conversation for the next standing weekly

### Open question (escalated to Maria)
- Ongoing-engagement structure post-week-4: who owns, how is funded, what's the cadence?

## Recap email sent (5:05pm)

Subject: `[Calder] Anil recap — read-only deal + sandbox + Hassan ownership`

> Anil — thanks for the time. Three things for the wedge proposal:
>
> **1. Read-only on Guidewire** unlocks the queue this week. Agent drafts, adjuster commits. No writes from the agent in v1.
>
> **2. Sandbox access by Wednesday next week**; Kayla 10h/week from then. Splunk ingestion for prompt/response logs (90d retention) — Kayla owns standup.
>
> **3. Hassan as ongoing operational owner**, dotted line to your team, in your weekly platform standup. Buys us against the scar-tissue ownership gap.
>
> Surfacing your 90-day-after question with Maria at the next standing weekly.
>
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Integration savvy | 5 | Read-only scoping unlocked the queue in real time |
| Customer-political acuity | 5 | "What worries you most" closer surfaced the ownership gap |
| Reusability instinct | 4 | Hassan-as-owner is right; should have been my proposal earlier than week-1 |
| Outcome ownership | 4 | The Maria 90-days conversation is now a deliverable, not vague intent |
| Calibrated engineering | 4 | Read-only constraint shapes architecture cleanly |

**Keep**: opening with the queue question; the cell-number-equivalent ("what worries you most") closer.

**Fix**: should have proactively raised Hassan-as-owner before Anil pushed; let me put the right answer in his mouth.
