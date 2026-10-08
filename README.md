# Placement and Interview Prep Skill for Claude

**Your placement-prep coach inside Claude.** DSA with Striver's A2Z sheet taught pattern by pattern, CS fundamentals, LLD, aptitude, mock interviews, resume builder, and a GSoC org finder that matches your skills. It remembers where you stopped, even across chats.

> If this helps you, **star the repo** so other students can find it.

---

## Why students use it

- **Stuck on "what do I solve next?"** Say "continue Striver A2Z" and it picks the next problems, teaches the pattern first, then gives hints before the answer.
- **Studying for days, not hours?** It prints a `PREP CHECKPOINT`. Paste it into a new chat and you resume exactly where you left off.
- **Interview in two weeks?** Tell it your days and hours, and it builds a 30/60/90/180-day plan.
- **Want an honest interviewer?** Mock interviews are scored out of 10 on correctness, clarity, depth and communication.
- **Starting open source?** Tell it your language and interests, and it shortlists GSoC organizations from real 2016-2026 data.

## Get started in 2 minutes

**Claude.ai (web / desktop)**
1. Click **Code > Download ZIP** on this page.
2. In Claude, open **Customize > Skills** (or Settings > Capabilities > Skills) and upload the ZIP.
3. Start a new chat and type: `I have 60 days for placements, make me a plan`.

**Claude Code (terminal)**
```bash
git clone https://github.com/BEASTSHRIRAM/placementprepskill.git ~/.claude/skills/btech-cse-interview-prep
```
On Windows, clone into `%USERPROFILE%\.claude\skills\btech-cse-interview-prep`.

> Use the whole folder. `SKILL.md` alone is not enough, because it loads the files in `references/` only when you ask about that topic.

## How to turn it on

- **Claude Code**: type the slash command `/btech-cse-interview-prep` to load it on demand. The command is the skill's folder and `name`, so keep the folder name as is. After that, just talk normally.
- **Claude.ai**: after uploading, make sure the skill is switched on under Customize > Skills. There is no command to remember: Claude loads it automatically when you ask about interview prep, DSA, Striver, GSoC, resumes and so on. If it does not kick in, start with `Use my interview prep skill` and then your request.

## Try these prompts

| You type | What happens |
|---|---|
| `Continue Striver A2Z from problem 61` | Next 3-5 problems, pattern first, hint ladder, complexity |
| `Make me a 60 day plan, 4 hours a day` | Asks 6 quick questions, then a week-by-week plan |
| `Mock interview me for Amazon SDE-1` | One question at a time, scored out of 10 |
| `Explain deadlock like an interview answer` | Definition, mechanism, example, follow-ups |
| `Design a parking lot` | LLD round: classes, patterns, code skeleton, follow-ups |
| `I know Python and a bit of ML, which GSoC orgs?` | Shortlist of orgs from 2016-2026 data, plus a first-PR roadmap |
| `Build my resume` | Choose HTML or LaTeX (ATS) and get a ready resume |
| `Quick revision of OS` | Compact cheat sheet from `WARP.md` |
| `save` or `done for today` | Prints your PREP CHECKPOINT to paste next time |

## What is inside

| Area | What you get |
|---|---|
| **Striver A2Z sheet** | All **452** problems in sheet order, each with a **pattern**, key idea and TC/SC, plus a Pattern Playbook for every topic |
| **DSA** | Data structures, patterns, a pattern-recognition cheat sheet, constraint-to-complexity table, 50 must-solve problems |
| **Operating Systems** | Scheduling, sync, deadlock, memory, plus worked numeric examples (Banker's, page replacement, disk scheduling) |
| **Computer Networks** | OSI, TCP/UDP, DNS, HTTP, plus subnetting and handshake worked examples |
| **DBMS and SQL** | Normalization, transactions, indexing, and a 12-query SQL practice set |
| **OOPs and design** | Four pillars, SOLID, design patterns, advanced Q bank |
| **LLD and system design** | 10 classic LLD problems, HLD concepts, 9+ case studies |
| **Core CS** | Computer architecture, compilers, theory of computation, discrete math |
| **Languages and web** | Java, Python, C++ internals; REST, auth, Docker, JS/React |
| **Aptitude and puzzles** | Quant, reasoning, verbal, 25 puzzles, data interpretation, tricky code snippets |
| **HR and resume** | STAR stories, common questions, resume builder (HTML or LaTeX/ATS) |
| **GSoC and open source** | Guide plus **509 organizations** (2016-2026) by technology, year and directory |
| **Study plans** | 30/60/90/180-day plans mapped to Striver problem ranges |

## Studying across several days

Claude does not remember previous chats. This skill works around it:

1. After each topic, and when you say "save" or "done for today", Claude prints a block like this:

```
PREP CHECKPOINT (updated 2026-10-08)
Goal: SDE-1 at product companies, Jan 2027   Level: intermediate   Language: Java
Striver A2Z: done 1-104, 105-136; current topic Strings (id 17176); weak patterns: sliding window
Revise later: 111, 119, 133
Mocks: 1 (6/10, needs to state complexity earlier)
Next up: problem 137
```

2. Copy it and paste it as your **first message** in the next chat, then say `continue`.
3. In Claude Code, the same block is also saved to `prep-progress.md` automatically.

## Repository layout

```
btech-cse-interview-prep/
├── SKILL.md              <- Core instructions and routing for Claude
├── WARP.md               <- 5-minute revision cheat sheet
├── CLAUDE.md             <- Rules for contributors using Claude Code
├── CONTRIBUTING.md       <- How to contribute
├── scripts/
│   └── build_gsoc.py     <- Refreshes references/gsoc/ from api.gsocorganizations.dev
├── references/
│   ├── dsa.md            <- DSA patterns and problems
│   ├── striver-a2z.md    <- Striver A2Z index (452 problems, routes to chunks)
│   ├── striver/          <- 5 chunk files: per-problem pattern, idea, complexity + Pattern Playbook
│   ├── os.md, cn.md, dbms.md, oops.md   <- CS subjects with Q banks
│   ├── core-cs.md        <- COA, Compiler Design, TOC, Discrete Math
│   ├── languages.md      <- Java, Python, C++ interview fundamentals
│   ├── web-backend.md    <- REST, auth, SQL vs NoSQL, Docker, JS/React
│   ├── system-design.md  <- HLD frameworks and case studies
│   ├── lld-problems.md   <- 10 classic LLD interview problems
│   ├── aptitude.md       <- Aptitude formulas and tricks
│   ├── puzzles.md        <- Puzzles, data interpretation, output prediction
│   ├── hr.md             <- HR and behavioural round prep
│   ├── study-plans.md    <- 30/60/90/180-day plans
│   ├── git-github-gsoc.md <- Git, GitHub and GSoC basics
│   ├── gsoc.md           <- GSoC starter guide (skill-based org picking)
│   └── gsoc/             <- Generated data: directory, by technology, by year
└── resume-builder/
    └── templates/        <- HTML+CSS and LaTeX (Overleaf) resume templates
```

## Data sources and honesty notes

- The problem list and order of the **Striver A2Z sheet** come from takeUforward's public sheet page. The **pattern names, key ideas and complexities** were written for this skill and are not Striver's official tags, so check them against the videos if they differ. This project is not affiliated with takeUforward.
- **GSoC data** comes from [gsocorganizations.dev](https://www.gsocorganizations.dev/) (`api.gsocorganizations.dev`). It is a snapshot: confirm the current year's accepted organizations and dates on the official GSoC site. Refresh it with `python -I scripts/build_gsoc.py`.
- Content was drafted with AI assistance and checked, but errors are possible. If you find one, please open an issue or a PR.

## Who it is for

Any student or fresher preparing for tech placements and interviews: BTech, BE, BCA, MCA, MSc or self-taught, in any branch. It targets product companies, service companies and startups (SDE-1, Software Engineer, Graduate Engineer Trainee), and also helps anyone starting open source or GSoC.

## Contributing

Found a mistake, want a new company question bank or a topic added? Read [CONTRIBUTING.md](CONTRIBUTING.md) and open a PR. Small fixes are very welcome.

## Support

If this helped you land an interview or an offer, **star the repo** and share it with your batch.

Licensed under the MIT License.
