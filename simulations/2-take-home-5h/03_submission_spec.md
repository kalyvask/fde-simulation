# Submission Spec — What You Ship 24h Before the Review

> 4 artifacts, no more. Less than this = under-prepared. More than this = optimizing the wrong thing.

## 1. Repo URL

- Public GitHub repo, OR private repo shared with `[email protected]` placeholder (in real engagements, the interviewer's email)
- README at the top with:
  - One-paragraph problem framing
  - How to run (one terminal command)
  - Where the agent code lives
  - Where the eval suite lives
  - Any caveats (e.g., "uses mock-mode fallback if no API key")
- `.env.example` showing what keys are needed
- `requirements.txt` pinned

**Quality bar**: an interviewer can clone your repo and run your e2e demo in under 3 minutes.

## 2. 4-slide deck (PDF or PPTX)

See `04_deck_template.md` for the structure.

**Quality bar**:
- 4 slides, not 5
- Each slide has a one-sentence headline that stands alone
- No screenshots of code (the repo has the code)
- One architecture diagram (slide 2) that you'd be willing to defend
- Numbers on slide 3 (eval results) and slide 4 (path to production)

## 3. 5-minute video walkthrough (Loom / YouTube unlisted)

See `05_video_walkthrough_guide.md` for the structure.

**Quality bar**:
- 5 minutes, not 4 or 6
- Show your face if you can — increases interviewer signal
- Include at least one live demo of the agent running
- End with what's NOT in v1 and what you'd ship next

## 4. Eval results summary (1 paragraph + 1 screenshot)

Either at the bottom of the README or as a separate `eval_results.md` in the repo.

**Quality bar**:
- Pass rate (weighted)
- Pass^k value
- 1-2 failures named (yes — graders prefer honest failures to hidden ones)
- Why each failure is informative (mock limitation vs real bug vs design choice)

## Optional: a written explanation document

If you have time and want to include your design rationale beyond the deck, drop a 1-2 page `decisions.md` in the repo covering:
- What you chose to scope out of v1, and why
- What you'd ship next (v1.5 / v2)
- Where you departed from the existing scaffold (if you forked one)
- Anything you want the interviewer to know before the Review

Don't make this longer than 2 pages. The interviewer reads it as a signal of operational maturity, not as exhaustive documentation.

## Example submission email

```
Subject: Helix take-home submission — [Your Name]

Hi [Interviewer],

My take-home for the Helix Capital case:

- Repo: https://github.com/yourname/helix-take-home
- Deck: [attached PDF]
- Video: https://loom.com/share/xxx (5 min)
- Eval results: 87% weighted pass at k=3 on 12 cases. Two failures documented in the deck.

To run the demo: `cd helix-take-home && pip install -r requirements.txt && python scripts/run_e2e.py`

Looking forward to the Review.

[Your Name]
```

That's it. No essay. No extended thank-you. Sign off and send.

## What graders look for in the submission

Even before the Review:

1. **Did they hit the 4 artifacts?** Missing one = automatic rubric downgrade.
2. **Does the repo actually run?** Failed clone-and-run is unforgivable.
3. **Is the video the right length?** 4-min = rushed; 7-min = no discipline.
4. **Is the eval honest?** Hidden failures > admitted failures.
5. **Did they scope ruthlessly?** A v1 that's clearly bounded > a v1 that tries to do everything.

If you hit all 5, you've earned the Review. The Review is the interview; the take-home is the entry ticket.
