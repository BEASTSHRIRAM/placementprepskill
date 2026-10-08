# GSoC and Open Source Starter Guide (Data-Driven)

Instructions for Claude when a student asks about GSoC, open source, "which org", or "how do I start contributing". Basic Git/GitHub commands, the general GSoC overview and the unwritten rules are already in `references/git-github-gsoc.md`; read that for basics and do not repeat it here. This file adds org selection from data, a beginner heuristic, a roadmap, and proposal craft.

Data files (generated, a snapshot, in `references/gsoc/`):
- `orgs-directory.md`: every org with technologies, years participated, latest-year project count, ideas link.
- `by-technology.md`: orgs per technology/language active in 2024-2026.
- `by-year.md`: year-wise org lists 2016-2026.

---

## 1. How Claude Should Use the GSoC Data

Never load the whole `references/gsoc/` directory unless the student asks for it. Follow this flow.

**Step 1 - Ask the student (one or two questions at a time):**
- Languages and skills (Python, Java, C++, JS, Rust, Go, ...)
- Interests: web, ML, systems, security, mobile, science, data
- Hours per week they can give (be honest: under 10 vs 20+)
- Experience with Git and open source (never used / forked a repo / merged PRs)
- Timeline: months left before the next application window; current year of study

**Step 2 - Read `references/gsoc/by-technology.md`, ONLY the sections matching their languages/interests.** Shortlist 5 orgs, applying the heuristic in section 2. Mix: 3 safe (stable, beginner-friendly), 2 stretch (interest-driven).

**Step 3 - Open `references/gsoc/orgs-directory.md`, only the rows for those 5 orgs.** Report per org: technologies, years participated, latest-year project count, ideas link. Use `by-year.md` only if the student asks "who participated in year X" or "is this org new".

**Step 4 - Verify.** Tell the student: "This data is a snapshot. Check the current year's accepted organizations and timeline on the official site, summerofcode.withgoogle.com, before investing time."

**Step 5 - Save.** Write the shortlist and progress into the PREP CHECKPOINT (see SKILL.md), for example under "Other subjects covered" or as an extra line: `GSoC: shortlist <org1..org5>; stage <week N of roadmap>; first PR <status>; Next up <action>`. Keep the checkpoint under 25 lines.

If the data files are missing, say so, fall back to the orgs listed in `git-github-gsoc.md`, and still send the student to the official site.

---

## 2. Beginner Suitability Heuristic

This is a heuristic Claude applies to the data. It is NOT an official rating and not a guarantee of acceptance.

| Signal in data | Reading |
|---|---|
| Years participated >= 4 and projects in every recent year | Stable, known process, mentors used to newcomers. Prefer. |
| Years participated = 1 (or 2 with gaps) | Unproven. Do not recommend to a first-timer. |
| Large latest-year project count | More student slots, so more chances. Small count (1-3) means very competitive. |
| Has an ideas link | Prefer. No ideas link means harder to scope a proposal. |
| Technology matches the student's strongest language | Prefer strongly. Match language, not prestige. |
| Famous name, student's stack does not match | Do not recommend as a first target. Mention as a later goal. |

Rules of thumb:
- Rank by (language match) > (stability) > (project count) > (interest fit).
- A 5-year org with 15 projects in a matching language beats a famous org in a language the student does not know.
- State the reasoning per org in one line so the student can challenge it.

---

## 3. Roadmap

### 12-Week "Zero to First PR"
| Week | Goal | Done when |
|---|---|---|
| 1 | Git/GitHub basics: fork, clone, branch, commit, push, PR (see git-github-gsoc.md). Practice on a personal repo. | Opened a PR to your own repo |
| 2 | Pick 2 orgs from the shortlist. Read their README, docs, ideas page. Run the project locally. | Project builds and runs on your machine |
| 3 | Read CONTRIBUTING.md and code of conduct fully. Join chat (Discord/Slack/Matrix/IRC) and mailing list. Lurk, then introduce yourself. | Introduction posted |
| 4 | Find issues: filter `good first issue`, `help wanted`, `documentation`. Pick 3, read comments to see if claimed. | One issue chosen and claimed politely |
| 5 | Reproduce the bug or understand the task. Read the related code. Ask a question with your research shown. | Written plan in the issue |
| 6 | First small PR (typo, docs, tiny bug, test). Follow commit and PR template exactly. | PR opened |
| 7 | Handle review: reply to each comment, push fixes, do not argue, say thanks. | PR merged or clearly progressing |
| 8 | Second PR, slightly larger (small bug fix or test coverage). | Second PR opened |
| 9 | Read the ideas list for the next cycle. Pick 2 ideas that fit your skills. Read past work on them. | Idea shortlist |
| 10 | Medium issue related to an idea area. Start talking to the idea's mentor in public channels. | Medium PR opened |
| 11 | Draft proposal outline (section 4). Ask for feedback publicly or from the mentor. | Draft v1 shared |
| 12 | Iterate on feedback, keep contributing, review other people's PRs lightly, plan the next 3 months. | Draft v2 plus 2+ merged PRs |

Review etiquette: respond within 1-2 days, keep PRs small and single-purpose, run tests and linters before pushing, never force-push over a reviewer's discussion without saying so, accept "no" gracefully.

### Typical Yearly GSoC Calendar (typical, confirm dates on the official site)
| Month (typical) | Phase | Student action |
|---|---|---|
| Oct - Jan | Off-season | Learn the stack, pick orgs, start contributing (this is the best time to begin) |
| Jan - Feb | Org applications / mentoring org announcements (about Feb) | Check which orgs are accepted; read their ideas pages |
| Feb - Mar | Org announcement, discussion period | Talk to mentors, refine ideas, send draft proposals for feedback |
| Mar - Apr | Contributor application window and proposal period | Finalize and submit proposal early, not on deadline day |
| Apr - May | Review and selection; accepted contributors announced (about May) | Keep contributing while waiting |
| May | Community bonding | Set up env, align with mentor, finalize timeline |
| Jun - Aug | Coding period; midterm evaluation; final evaluation | Weekly public updates, push code often |
| Aug - Sep | Final evaluation and results | Write final report, stay in the community |

Calendar structure and lengths can change between years (for example project sizes and coding duration). Always confirm.

---

## 4. Proposal Writing

Fits with the structure already in `git-github-gsoc.md`; use this version as the working template.

### Template
1. **Title and abstract** (5-8 lines): what, why, outcome.
2. **Problem**: current state, who is affected, link issues.
3. **Approach**: design, key files/modules, libraries, alternatives you rejected and why.
4. **Timeline by week**: community bonding plus each coding week with a measurable output; include midterm and final milestones, a buffer week, and exam/holiday gaps.
5. **Deliverables**: code, tests, docs, demo; say what "done" means.
6. **About me**: skills, availability (hours/week), time zone, other commitments.
7. **Prior contributions**: PR/issue links with one line each, community participation.

### What mentors look for
- Evidence you understand the codebase (specific files, functions, issues).
- Realistic scope with testable milestones.
- Communication: clear writing, public questions, responds to feedback.
- Reliability: merged PRs, consistent presence, availability that matches the timeline.

### Common rejection reasons
- Generic proposal copied from the ideas page.
- No contributions or no community contact before applying.
- Over-ambitious or vague timeline.
- Too many students on one idea and no differentiation.
- Late submission, no feedback taken, AI-generated text the student cannot defend in a call.
- Low availability that clashes with exams or an internship.

### Talking to mentors
- Introduce yourself in the public channel first; use DMs only if invited.
- Post specific questions: what you tried, what you expected, what happened, logs.
- Ask for proposal feedback early with a 1-page draft before the full one.
- One mentor message answered well beats ten pings; do not ping repeatedly.

### Choosing between ideas
Score each idea 1-5 on: skill match, interest, mentor responsiveness, size of scope vs your hours, number of other students on it, quality of past work. Pick the highest total, not the most impressive title.

### Calibrating with an org's past projects
The data includes `project_url` / `code_url` for past projects. Use them to:
- See the size of a funded project: lines of code, number of PRs, what "done" looked like.
- Read past proposals/reports to copy the level of timeline detail (not the content).
- Check if past students stayed active (signal of a healthy mentoring culture).
- Judge whether an idea you like is of similar size to what was accepted before; shrink or expand your scope to match.

---

## 5. Eligibility

Say: "Check the current eligibility rules on the official site (summerofcode.withgoogle.com)." Do not state specific age, enrollment, country, or stipend rules from memory; they change between years. If the student asks "am I eligible", direct them to the official FAQ and the org's own requirements.

---

## 6. Alternatives and Complements

- **Outreachy**: paid remote internships in open source, for people underrepresented in tech; has its own eligibility and timeline.
- **MLH Fellowship**: structured, mentored open source or engineering fellowship run by Major League Hacking.
- **LFX Mentorship**: Linux Foundation mentorship across CNCF/LF projects, with paid terms.
- **Hacktoberfest**: October event to make PRs; a low-pressure way to get the first PRs.
- **Season of Docs**: documentation-focused program for technical writers and docs contributors, run by Google.
- **Other GSoC-like programs**: for example summer/winter programs run by individual foundations or communities; search for the project's own programs.
- **IIT/college programs**: campus open source programs and club-run mentoring programs; check your college and nearby IIT cells.
- **Always available**: contributing year-round to any project you use; no program is needed to start.

---

## 7. Data Source Credit

Org data comes from gsocorganizations.dev (api.gsocorganizations.dev). Refresh once a year by running `scripts/build_gsoc.py`, which regenerates the files in `references/gsoc/`. The data is a snapshot; the official site is the source of truth.
