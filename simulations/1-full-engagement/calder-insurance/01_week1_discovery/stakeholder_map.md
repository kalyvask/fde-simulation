# Stakeholder Map — Week 1 Discovery

The principle: never start with the buyer alone. Map the workflow through every role that touches it. Identify the champion, the blocker, the silent skeptic.

## The 11 stakeholders for Calder

| # | Stakeholder | Role in this engagement | Power | Stance (hypothesis) |
|---|---|---|---|---|
| 1 | Maria Vasquez, CCO | Economic buyer | High | Sponsor — wants the number |
| 2 | Greg Hadley, SVP Claims Ops | Champion candidate | High | Pro — daily pain owner |
| 3 | Priya Shah, Director FNOL | Operator | Medium | Pro if respected, blocker if bypassed |
| 4 | Frontline adjusters (3-5) | Primary user | Low individually, high collectively | Skeptical — fear job loss |
| 5 | Tom Reilly, Quality / Audit | Definer of "bad close" | Medium | Skeptical — owns audit risk |
| 6 | Dana Kowalski, SIU Lead | Highest-risk reviewer | Medium | Pro if fraud detection improves, blocker if not |
| 7 | Anil Gupta, CIO | Integration owner | High | Neutral — overloaded |
| 8 | Rachel Nieman, CISO | Deployment blocker | High | Skeptical — default no |
| 9 | Marcus Hill, Compliance | Regulatory gate | High | Skeptical — career risk on her own |
| 10 | Lin Zhao, Finance / Actuary | Savings owner | Medium | Pro if model holds up |
| 11 | Kevin Park, BPO contract owner | Incumbent threat | Medium | Conflicted — owns BPO relationships |

## The non-obvious ones

Most demos ignore SIU and Compliance. They're the reason a real engagement either ships or rots in pilot purgatory. Spend one full interview on each.

The frontline adjusters are also routinely under-interviewed. Their fear-of-job-loss reaction is the political risk that kills production rollouts. You need them on side to get the workflow right and to land the rollout politically.

## Champion identification (do this in week 1)

Strongest champion is whoever:
1. Owns the metric you're moving (LAE ratio, $/claim, cycle time)
2. Has authority to clear blockers
3. Wants visible internal credit for the win

Greg Hadley fits all three. Default champion. But validate in interview.

## Blocker identification

Most likely blockers, in order of probability:
1. **CISO (Rachel Nieman)** — data residency, BAA, log retention. Default no until proven safe.
2. **Compliance (Marcus Hill)** — state DOI variance, NAIC market-conduct exposure.
3. **CIO (Anil Gupta)** — Guidewire integration queue is months long.

Strategy: bring CISO and Compliance into the design phase, not the approval phase. Their objections become your design constraints.

## Silent skeptic

Frontline adjusters as a group. They won't say no in a meeting. They will quietly fail to adopt and the system will get blamed. Mitigation: design the workforce so it elevates them rather than displacing them. Frame as "moving you off the soul-crushing tier-1 work."
