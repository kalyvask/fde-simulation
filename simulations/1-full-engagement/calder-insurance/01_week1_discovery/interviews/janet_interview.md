# Janet — Senior Adjuster (representative interview) — Thursday 11:00am ET, Zoom (30 min)

> ⚠️ **SYNTHESIZED HYPOTHESIS-CONFIRMING PROXY.** Constructed dialogue; methodology authentic. Real Janet may surface different facts.

## Setup

Thursday 11:00 AM ET. Janet at her desk, second monitor visible with claim queue. Coffee mug. Watchful, slightly arms-crossed energy. 14 years here. Killed the 2023 RPA project quietly by getting her team to route around it. Priya warned she's the must-win.

## Selected exchanges

**Alex** *(opening)*: "Janet, thanks for taking the time. Priya said you've been here 14 years and the 2023 RPA thing didn't work out for reasons that mattered. I'm not here to make those mistakes again. I'd like to spend most of the 30 minutes on you walking me through actual claims and what you'd never trust an AI to handle. The opposite of selling you anything."

**Janet** *(small smile, brief)*: "Heh. OK. I've heard that opening before."

**Alex**: "Fair. I'll let the next 30 minutes tell you whether it's true. Last claim you handled — walk me through it."

**Janet** *(tests with brief answer)*: "Comm auto, fender bender, closed Tuesday. Routine."

*(Alex doesn't push. Holds the silence for a beat.)*

**Alex**: "Tell me about a claim where your judgment changed the outcome. Where without you, the system would have done the wrong thing."

**Janet** *(thinks)*: "Three weeks ago. Multi-vehicle on the Garden State Parkway, three cars. Fault chain was complex — first car braked for an animal, second car hit it, third car hit the second. The estimating system wanted to assign primary fault to the second car because they had the contact-loss damage. But under NJ comparative negligence, the third car's distance was the primary cause — they were following too close. If I'd let the system route, we'd have paid out wrong on subro and we'd have a very angry second-car customer. I caught it because I read the police narrative twice."

**Alex**: "What in the narrative tipped you off?"

**Janet**: "The third-car driver said 'I didn't have time to react' in their statement. That's the tell. Anyone who didn't have time to react was following too close. Most adjusters wouldn't have read the narrative — they'd have looked at the damage photos and routed."

**Alex**: "Walk me through more of those tells. I'd rather build a system that surfaces what makes you suspicious than build a system that tries to replace the suspicion."

**Janet** *(warming up)*: "OK. Tells. 'I didn't have time to react.' 'I never saw them.' 'They came out of nowhere.' Three different fault patterns. Then the words people use about the other driver — 'the lady in the SUV' versus 'the elderly woman' tells you about empathy and sometimes about demographics in the report. There's also missing tells — when someone gives a really clean narrative, that's actually suspicious, real people don't talk in clean narratives. Adjusters call it 'the lawyered-up paragraph.'"

**Alex**: "That's gold. So if I were building something to assist you, what would it have to do for you to trust a flag from it?"

**Janet** *(no hesitation)*: "Four things. One: show me the exact words from the narrative that triggered the flag, highlighted in the original. Two: tell me what coverage clause it's invoking. Three: tell me how confident the model is, in plain English, not a percentage. Four: let me one-click escalate or one-click dismiss with a reason, and don't punish me in some metric for using either button."

**Alex**: "If I built that tomorrow, would you use it?"

**Janet**: "I'd try it on my comp/collision/PD claims, the routine stuff. I would not use it on bodily injury. Not for at least a year. The 2023 RPA thing assumed BI was just like comp/collision and routed something it shouldn't have, and we ended up with a $40K underpayment that came back as a complaint. I will not be the adjuster who lets that happen again."

**Alex**: "BI is out of v1 explicitly. I'll put that in writing in the wedge proposal."

**Janet** *(visibly relaxes)*: "OK then we might be friends."

**Alex**: "Last topic. The first comm a claimant gets after FNOL — what makes it good versus bad?"

**Janet**: "Good comm: name spelled right, claim summarized in their own words back to them so they know we listened, plain-language next step, timeline they can plan around, person to call if anything changes. Bad comm: form letter, claim number that means nothing to them, generic 'we'll get back to you in 30 days' when their car's in the shop and they need it back. We do bad comm a lot. The BPO is worse."

**Alex**: "When the wedge produces drafts, would you be willing to review 20 of them in week 3 before we ship anything broader?"

**Janet** *(considers)*: "Yes. If you're really serious about the trust criteria I just gave you, send me 20 drafts and I'll mark them up the way I'd want them. If they read like the comp/collision ones I'd write myself, I'll back the rollout. If they read like BPO templates, I'll tell you and you'll have to redesign."

**Alex**: "Fair deal. Priya will set up the 20-draft review for week 3."

*(Wraps at 28 minutes.)*

## Post-interview captures

### The four trust criteria (the eval-design source)
1. Show the exact words from the narrative that triggered the flag, highlighted in the original
2. Show the coverage clause invoked
3. Confidence in plain English, not a percentage
4. One-click escalate / dismiss with a reason, with no metric punishment

### The five comm-quality criteria
1. Name spelled right
2. Claim summarized in claimant's own words
3. Plain-language next step
4. Timeline the claimant can plan around
5. A person to call if things change

### The "tells" (adversarial eval inputs)
- "I didn't have time to react" → following-too-close fault pattern
- "I never saw them" / "They came out of nowhere" → different fault patterns
- The "lawyered-up paragraph" → too-clean narrative as suspicion signal
- Empathy-language tells in claimant statements

### Glossary updates
- **Subro**: subrogation
- **Comparative negligence**: NJ-specific fault apportionment
- **Lawyered-up paragraph**: adjuster slang for too-clean narrative

### Stakeholder map updates
- Janet: stance shifted from SILENT SKEPTIC to **CONDITIONAL SUPPORT** (will champion if 20-draft review goes well)
- Trust signal: explicit BI-exclusion commitment was the trust-earning moment
- Risk: still a hard NO on BI for v1+; plan accordingly

### Working hypothesis updates
- Trust criteria (4 elements) become a **UX requirement** for the agent: source span, policy ref, plain-English confidence, one-click controls without metric punishment
- Comm-quality criteria (5 elements) become the **comm-quality eval rubric** (LLM-as-judge will grade against these)
- The "tells" Janet named become **adversarial eval inputs** — claims with these phrases test whether the agent picks them up
- Janet's 20-draft review in week 3 is now an **explicit gate on rollout**

## Recap email sent (11:35am)

Subject: `[Calder] Janet recap — trust criteria, comm-quality bar, 20-draft review`

> Janet — thanks for the time. Capturing the things you gave me that will land in design:
>
> **Trust criteria for an AI flag** (4 elements): source span highlighted, coverage clause invoked, plain-English confidence, no-punishment escalate/dismiss. These become UX requirements.
>
> **Comm-quality bar** (5 elements): name spelled right, claim summarized in claimant's words, plain-language next step, plannable timeline, person-to-call. These become the LLM-as-judge eval rubric.
>
> **BI excluded from v1**. Confirmed in writing in the wedge proposal.
>
> **Week 3 20-draft review** with you, scheduled via Priya. If drafts pass your bar, you back the rollout. If they don't, we redesign.
>
> Talk in week 3.
> Alex

## Self-grade

| Dimension | Score | Note |
|---|---|---|
| Discovery rigor | 5 | Held the silence after her test answer; let her open at her pace |
| Domain learning velocity | 5 | Subro, comparative negligence, the "tells" — captured verbatim |
| Customer-political acuity | 5 | BI-exclusion commitment was the trust-earning moment |
| Risk awareness | 5 | The 4-element trust criteria become the agent's design constraints |
| Outcome ownership | 5 | The 20-draft review in week 3 is now a hard milestone |

**Keep**: opening framing (acknowledged the 2023 RPA history without selling); silence after her brief answer; explicit BI-exclusion commitment.

**Fix**: nothing major; this was a clean execution.
