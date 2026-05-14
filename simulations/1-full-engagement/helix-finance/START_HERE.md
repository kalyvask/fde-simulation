# Start Here — Helix Engagement Kickoff

> Open this file when you're ready to begin the Helix engagement. The clock starts when you finish reading.

---

## 6:15 AM Monday — your inbox

```
From: Sarah Mendez <smendez@helixcapital.com>
To: FDE Lead <you@fde-team>
Cc: David Park, Aditya Sharma
Date: Monday, 6:15 AM ET
Subject: Helix engagement — kickoff Monday 9 AM, before market open

[FDE Lead] —

Looking forward to the 9 AM. Before-market on Mondays is the only sane time
for a 45-min meeting in our shop, so I'm using it.

The shape of what we're trying to solve:

Helix Capital. $2.3B long-short equity. 12 investment professionals — 5
senior analysts, 4 associates, 3 traders — plus me and the COO. We cover
~80 names across TMT, consumer, and industrials.

Every senior analyst spends about 4 hours per covered name the morning after
that company's earnings call drafting a one-pager that goes to me, our PMs,
and the trading desk. 80 names × 4 quarters × 4 hours = 1,280 hours per
analyst per year.

We lost two senior analysts in 2025. Both exit interviews flagged the
morning-after grind as unsustainable. We're losing alpha because notes land
hours after market open. We're also losing people.

What kills me about this engagement: if you build something that
hallucinates a number into one of those notes, and a PM trades on it, we're
looking at trading losses, fund-reputation damage, and potentially SEC
scrutiny. We had zero MNPI incidents in three years. I'd like to stay that
way.

Three things up front:

1. Zero MNPI incidents is THE kill criteria. Any architecture that
   doesn't make MNPI leak architecturally impossible — not just unlikely —
   doesn't pass our compliance gate. Mei will own that gate.

2. Senior-analyst veto. Our senior TMT analyst Rachel will not roll this
   out unless she signs off on 20 sample drafts she'd be willing to put
   her name on. Make her your friend, not your hostage.

3. 4 weeks to demo. I want something live by week 5. Not a pilot. Not a
   POC. Something a PM can actually use. If you can't get there, tell me
   in week 1, not week 4.

Aditya (CTO) will give you read-only access to our Bloomberg + FactSet
integrations on a Snowflake-Python sandbox. Compliance (Mei) will give you
our MNPI watch list and the audit-trace standard our internal reviewer
applies.

For 9 AM today, I'd rather you arrive with questions than answers. Tell me
what you'd ask me, and who else you'd want to talk to, to figure out if
this engagement is real.

The 9 AM is in my office. Aditya's joining for the second half.

Sarah

----------------------------------------------------------------
Sarah Mendez · CIO & Managing Partner
Helix Capital
smendez@helixcapital.com · direct: 212-555-0142
```

---

## The clock has started

It's now **6:20 AM Monday, your engagement week 1**. You have ~2.5 hours before the kickoff with Sarah.

### What to do in the next 2.5 hours

1. **Read [`00_brief.md`](00_brief.md)** (10 min) — the formal customer context. The fund, the 80-name coverage book, the IT landscape, the constraints.

2. **Read [`EXERCISE.md`](../helix-finance/EXERCISE.md)** if you haven't (5 min) — the 4-week structure and what you'll produce.

3. **Skim [`01_week1_discovery/STAKEHOLDER_INTERVIEWS.md`](01_week1_discovery/STAKEHOLDER_INTERVIEWS.md)** (5 min) — the 7 stakeholder role-play prompts. Sarah first this morning. David afternoon. Rachel tomorrow.

4. **Pre-pick 8-10 questions for Sarah** (15 min) — sharp ones, framed around her three named kill-criteria. Don't ask anything that's already in her email.

5. **Don't peek at the reference solutions yet.** `01_week1_discovery/discovery_memo.md` is the reference; open it only AFTER you've produced your own.

### The 9 AM meeting with Sarah

When ready, open a fresh Claude conversation and paste **Prompt 1 — Sarah Mendez** from [`01_week1_discovery/STAKEHOLDER_INTERVIEWS.md`](01_week1_discovery/STAKEHOLDER_INTERVIEWS.md). Claude will play Sarah. You're the FDE.

Sarah is sharp, time-pressured, and skeptical of pitches. She'll reward principled questions and punish vague framing. The role-play is designed to be conversational — she'll push back when you go wide.

### Today's full schedule (Day 1)

| Time | What | Output |
|---|---|---|
| 6:20 - 8:45 AM | Prep: read brief, EXERCISE, pre-pick questions for Sarah | 8-10 pre-selected questions |
| 9:00 - 9:45 AM | Sarah kickoff — Claude plays Sarah | Notes; restated kill-criteria; political-map starter |
| 9:45 - 10:30 AM | Synthesize Sarah notes | Stakeholder map first draft |
| 10:30 AM - 12:00 PM | Lunch + prep for David | Pre-questions for David |
| 1:00 - 2:00 PM | David Park (Head of Research / champion) — 60 min | Workflow understanding; political insight on Rachel |
| 2:00 - 3:30 PM | Synthesize + write recap email to Sarah | Recap email + 1-page wedge hypothesis draft |
| End of day | Compare to reference (or save for end of week) | Note gaps |

### Tomorrow (Day 2) and the rest of the week

Per the cadence in `STAKEHOLDER_INTERVIEWS.md`:
- **Day 2 AM**: Rachel Kim (Senior TMT Analyst — the lead user). The most important interview of the week.
- **Day 2 PM**: Mei Liu (Compliance) + Aditya Sharma (CTO) back to back.
- **Day 3 AM**: Carmen Diaz (Senior Trader — the silent skeptic). Pre-empt her by inviting her in week 1, not week 5.
- **Day 3 PM**: James O'Brien (COO) — 20 min on operations + post-handoff.
- **End of Day 3**: Field memo with baseline metrics, target metrics, and wedge hypothesis. Signed off by Sarah before week 2.

---

## Mindset reminders before you walk in

- **Restate the case in one sentence before doing anything else** when Sarah asks. Signals you listened to her email.
- **Ask questions, don't pitch.** Sarah named three kill-criteria. The first interview is about confirming you understand them, not solutioning.
- **Name the kill-criteria back to her in your own words** in the first 5 minutes. Especially the zero-MNPI streak — that's the bottom floor.
- **Get explicit on the metrics that go in the contract.** Sarah's framing: 4 hours of senior-analyst time → 30 minutes per note. That's a target. What's the baseline? What's the analyst-trust metric? Validate both numbers through her.
- **Don't promise auto-publish.** Sarah will respect a "read-only v1, earn write access in v2" framing. She'll punish a "we'll automate the whole pipeline by week 4" pitch.
- **Carmen is the silent skeptic.** Sarah hasn't mentioned her in the email. Bring her up. Surface her in week 1, not week 5.

---

## When you're stuck

- Need the framework? See [`../../../frameworks/`](../../../frameworks/) — 10 portable frameworks. 4-source convergence first.
- Need to know what good looks like? See [`GRADE_YOUR_WORK.md`](../GRADE_YOUR_WORK.md) — Claude grading prompt per phase.
- Want a senior shortcut? See [`../SKIP_AHEAD.md`](../SKIP_AHEAD.md) — if you've done this before, do weeks 3-4 cold.
- Done? See [`../RETRO_TEMPLATE.md`](../RETRO_TEMPLATE.md) at end of week 4.

---

**The clock is running. Open `00_brief.md` and get to work.**
