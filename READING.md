# Reading List

> A curated short list of books, papers, and blogs for FDE / Deployed PM / Solutions Architect prep. Structured by what stage of prep each is for.

The full prep arc takes ~3-6 months if you start cold. This list gets you to the bar in ~40-60 hours of reading, spread across the stages.

---

## Stage 1 — Before you start studying (1-2 weeks)

Read these to understand what you're signing up for. If after these you're still excited, the rest of the prep is worth it.

### Books

| Book | Why | Time |
|---|---|---|
| ***The Trusted Advisor*** — David Maister | The canonical text on consultative client relationships. The trust formula (in `frameworks/consulting-frameworks.md`) is from here. | 4-6 hours |
| ***Good Strategy / Bad Strategy*** — Richard Rumelt | Teaches the difference between a strategy (a coherent action plan) and a wish-list (most companies' "strategies"). The diagnosis → guiding policy → coherent action structure maps directly to FDE wedge selection. | 5-7 hours |

### Blog posts

- **"Dev vs. Delta"** — Palantir's original framing of the FDE role. Defines "the Delta" concept used throughout this repo's `consulting-frameworks.md`.
- **OpenAI's interview guide** — official; sets the expectation for what they grade on.
- **Sierra's "AI-Native Interview"** blog — same idea from a smaller AI-workforce platform; shows the shape of the conversation-first interview style.

---

## Stage 2 — Foundations (3-5 weeks)

Read these to internalize the technical and consulting muscle. By end of Stage 2 you should feel comfortable in any FDE conversation.

### Technical books

| Book | Why | Time |
|---|---|---|
| ***Designing Data-Intensive Applications*** — Martin Kleppmann | The textbook for production data systems. You don't need to read all of it — chapters 2 (data models), 5 (replication), 7 (transactions), and 10 (batch processing) are the must-reads for FDE interview prep. | 12-15 hours (4 chapters) |
| ***Enterprise Integration Patterns*** — Hohpe & Woolf | The pattern catalog for integrating heterogeneous systems. Useful when designing read/write patterns for an FDE engagement. Skim the table of contents and read the 6-8 patterns most relevant to your target customer (CRM → ERP, event-stream, etc.) | 4-6 hours (skim mode) |
| ***Staff Engineer*** — Will Larson | What the senior-IC track looks like. The "engineer + influence" framing maps directly to FDE work. | 5-7 hours |

### Consulting books

| Book | Why | Time |
|---|---|---|
| ***The Pyramid Principle*** — Barbara Minto | The canonical bottom-line-up-front writing structure. Apply directly to your interview deck and field memos. | 4-6 hours |
| ***The McKinsey Way*** — Ethan Rasiel | The classic on how management consultants structure problem-solving. MECE, hypothesis-driven, 80/20. Light but high-density. | 2-3 hours |

### Papers

| Paper | Why |
|---|---|
| **"Attention Is All You Need"** (Vaswani et al., 2017) | The Transformer paper. You don't need to implement it; you need to be able to discuss it. |
| **"ReAct: Synergizing Reasoning and Acting in Language Models"** (Yao et al., 2023) | The agentic-pattern paper. Tools-and-reasoning loops are now the dominant agent architecture. |
| **"Constitutional AI: Harmlessness from AI Feedback"** (Bai et al., 2022) | Anthropic's safety framing. Required reading if you're interviewing at Anthropic; useful for "what would you refuse to deploy" questions everywhere else. |

### Blogs / Newsletters

- **Eugene Yan's blog** — production ML patterns, evals, agent design. Top-quality writing on the boring-and-correct stuff.
- **Latent Space** podcast + newsletter — the best survey of what's shipping in agent + applied AI right now.
- **Import AI** (Jack Clark) — weekly newsletter on AI research and policy. Useful for values-round prep.
- **The Pragmatic Engineer** — Gergely Orosz on engineering management and IC growth. The "ladder" framing helps you talk about your career.

---

## Stage 3 — Calibration (1-2 weeks before the interview)

Read these to calibrate against the specific employer you're interviewing at.

### Employer-specific (do at least 4-6 hours per target employer)

For the company you're interviewing at, read:

1. **The company's published values / charter / mission**
2. **The CEO's recent public essays / posts** (last 6 months)
3. **Their flagship customer case studies** (3-5 of them)
4. **Their API or product documentation** top-to-bottom — you should be able to discuss specific endpoints
5. **Glassdoor + interview-experience write-ups** for the role you're applying for

### Operational books (skim mode)

- **SRE Workbook** (Google) — chapters on monitoring, incident response, and on-call. Skim only — useful for "tell me about a production incident" stories.
- **How to Win Friends and Influence People** — Carnegie. Strongly recommended for the client-simulation round even if it feels dated. The "talk in terms of the other person's interests" principle is gold.

### Papers — agent evaluation specifically

- **"Pass^k for LLM evaluation"** (search any recent OpenAI / Anthropic eval paper) — formalizes the pass^k=5 production threshold this repo references
- Recent papers on **LLM-as-judge calibration** — useful for the eval-quality differentiator question

---

## Stage 4 — Day-of (the morning of)

Don't read anything new. Re-read these:

- Your own discovery memo + wedge proposal from your portfolio piece (if you have one)
- The 5-step de-escalation script in `simulations/4-client-simulation/playbook.md`
- The ownership language guide in `frameworks/ownership-language-guide.md` — read out loud
- The 6 frameworks one-line summaries in `frameworks/README.md`
- Your own behavioral story principles (from `frameworks/behavioral-story-types.md` — your filled-in templates)

If you've done the prep, day-of reading is for state management, not for learning new material.

---

## What's deliberately NOT on this list

| Resource | Why we skip |
|---|---|
| LeetCode | FDE interviews are not algorithmic-puzzle interviews. LeetCode prep substitutes for real prep. |
| Books on AI hype (*Power and Prediction*, etc.) | Useful for general AI literacy; not differentiating for FDE prep specifically. |
| Cloud-vendor certifications (GCP, AWS) | Useful for the job; rarely tested in the interview. |
| Long ML textbooks (*Deep Learning* by Goodfellow et al.) | The interview doesn't test ML theory at this depth. Useful only if you came from a non-ML background. |
| Entrepreneurship books (*The Lean Startup*, etc.) | FDE work has some startup-like discovery shape but the books generalize too far. The McKinsey Way is more directly applicable. |

---

## How much to read

A realistic timeline:

| Prep arc | What you read | Approximate time |
|---|---|---|
| **30-day sprint** (recommended minimum) | Stage 1 + 1 book from Stage 2 + 1 paper + employer-specific calibration for your target | 25-35 hours |
| **3-month prep** (the high-bar prep) | All of Stage 1, 2, 3 + 5-6 papers + multi-employer calibration | 60-80 hours |
| **6-month prep arc** (career transition into FDE) | Above + the technical books (DDIA, Enterprise Integration Patterns) end-to-end + 2-3 portfolio engagements (sim 1 in this repo) | 150-250 hours |

The marginal book after Stage 2 has rapidly diminishing returns. After ~5 books + 5 papers, the next-best use of time is mock interviews (sim 2, sim 4) and writing your own field memos.

---

## How to read these efficiently

| Resource | Read mode |
|---|---|
| Maister / Pyramid Principle / Good Strategy | Linear, with note-taking. These are short and dense. |
| DDIA / Enterprise Integration Patterns / Staff Engineer | Topic-driven skim. Pick the chapters relevant to your case domain. |
| Papers | Read the abstract + intro + conclusion. Skim the methods section unless you specifically need it. |
| Blogs | Subscribe; read in your weekly research time, not in your interview-prep block. |
| Employer-specific material | Linear, with annotations. Highlight specific phrases you'd reuse in your "why this company" answer. |

---

## A final note on book ROI

The frameworks in this repo distill ~80% of the actionable content from the books listed. **If you're time-constrained, read the frameworks first; read the books to deepen the frameworks you're already using.**

The books matter most for:
- **Behavioral story preparation** — *The Trusted Advisor* and *Good Strategy* give you the vocabulary
- **Communication discipline** — *Pyramid Principle* changes how you write field memos
- **Long-term FDE craft** — DDIA, Enterprise Integration Patterns, Staff Engineer are 10-year investments, not interview-week investments

Don't try to read everything before the interview. Pick the 2-3 that map most directly to your weakest dimension and read those well.
