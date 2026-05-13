# Take-Home Prompt — Helix Capital

> This is the case as you'd see it from the interviewer. Read it; don't read anything else yet.

---

## The Prompt

You've been invited to a final-round interview as a Forward Deployed Engineer / Deployed PM. Your take-home is to spend up to 5 hours preparing a build and presentation for a fictional customer. You'll ship a deck, a video walkthrough, and a working prototype 24 hours before the onsite Review round.

### The customer: Helix Capital

> "We're a $2.3B long-short equity hedge fund. Twelve investment professionals — 5 senior analysts, 4 associates, 3 traders — plus me and the COO. We cover roughly 80 names across TMT, consumer, and industrials.
>
> Here's our problem. Every senior analyst spends about 4 hours per covered name the morning after that company's earnings call drafting a one-pager that goes to me, our PMs, and the trading desk. 80 names × 4 quarters × 4 hours = 1,280 hours per analyst per year. We lost two senior analysts in 2025 — both exit interviews flagged the morning-after grind as unsustainable. We're losing alpha because notes land hours after market open, and we're losing people.
>
> What kills me about this engagement: if you build something that hallucinates a number into one of those notes, and a portfolio manager trades on it, we're looking at trading losses, fund-reputation damage, and potentially SEC scrutiny. We had zero MNPI incidents in three years. I'd like to stay that way.
>
> The CTO will give you read-only access to our Bloomberg + FactSet integrations on a Snowflake-Python sandbox. Compliance will give you our MNPI watch list and the audit-trace standard our internal reviewer applies. Our senior TMT analyst — Rachel — will not roll this out unless she signs off on 20 sample drafts she'd be willing to put her name on.
>
> Build me something we can demo in 4 weeks. I want 30 minutes of senior-analyst review time per note, down from 4 hours, without ever letting a hallucinated number reach a PM."
>
> — Sarah Mendez, CIO & Managing Partner

### Stakeholders you can interview (in your imagination — they don't actually exist; you'll fill in their views based on the prompt + your judgment)

- **Sarah Mendez** — CIO. Economic buyer. Kill-criteria above.
- **David Park** — Head of Research. Champion. Runs the coverage book day-to-day.
- **Rachel Kim** — Senior Analyst, TMT. 9 years tenure. Lead user. Will quietly route around if she doesn't trust.
- **Mei Liu** — Compliance Officer. Default-no. SEC + FINRA + CFA + internal review.
- **Aditya Sharma** — CTO. Owns Snowflake + Bloomberg/FactSet integrations. One junior engineer.
- **James O'Brien** — COO. Handles infosec (no separate CISO at this size).
- **Carmen Diaz** — Senior trader. Downstream user. Has been burned by lazy analyst notes; reads any AI-assisted note with extra skepticism.

### Constraints you can assume

- 4-regulator stack: SEC + FINRA + CFA Institute + internal compliance
- MNPI handling: hard wall — never enters an LLM prompt
- Chinese wall: research and trading separated logically
- Sandbox: read-only Bloomberg + FactSet on a Snowflake-Python research stack
- BAAs: Anthropic in place; OpenAI in evaluation
- Senior-analyst veto: Rachel + one other senior must sign off on 20 sample drafts before rollout
- Procurement cycle: 6 weeks for new AI vendor

### Public data you can use

To simulate Helix's earnings-call inputs without real customer data:

- **EDGAR-CORPUS** — Apache 2.0, SEC filings 1993-2020, 40GB on HuggingFace
- **ECTSum** — earnings-call transcript summarization benchmark (Reuters-derived expert summaries)
- **SubjECTive-QA** — earnings-call Q&A with 6-dimensional subjectivity labels (rare and valuable)
- **FINOS EarningsCallTranscript** — transcripts + audio
- **Yahoo Finance** — consensus estimates (free tier)

### What you ship 24 hours before the Review

1. **Repo URL** (public or shared with the interviewer's email)
2. **4-slide deck** (PDF or PPTX) — see structure in your prep materials
3. **5-minute video walkthrough** (Loom or YouTube unlisted)
4. **Eval results summary** — 1 paragraph + screenshot

Less than that = under-prepared. More than that = optimizing the wrong thing.

### The 60-minute Review round

You'll present to a senior FDE / Solutions Engineer. They've watched your video and read your deck. They have 60 minutes. They will push back on every load-bearing architectural choice. Your job is to defend with substance or revise with composure — both are acceptable; defensiveness is not.

### What's being tested

Per the rubric (in `training/interview_60min/rubric.md`):

1. Customer-first framing
2. Agent architecture judgment
3. Production thinking
4. Risk surfacing
5. Communication

15 points total. 12+ is the frontier-lab bar.

### The 5-hour clock

5 hours. Set a timer. The interviewer knows what 5 hours looks like — going over signals weak prioritization. Going under signals you skipped something important. What you skip is signal.

---

When you're ready, open `02_take_home_workflow.md` for the hour-by-hour plan.
