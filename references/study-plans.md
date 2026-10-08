# Study Plans (30 / 60 / 90 / 180 days)

Problem numbers (e.g. "165-175") are the sheet's own numbering in references/striver-a2z.md (452 problems). Subject files: dsa.md, os.md, oops.md, cn.md, dbms.md, aptitude.md, system-design.md, core-cs.md, languages.md, web-backend.md, git-github-gsoc.md, hr.md.
Abbreviations: Apt = aptitude, CP = competitive programming, LLD/HLD = low/high level design, Rev = revision.

## 1. Quick Diagnostic (ask these 6, one at a time, then pick a plan)

| # | Question | How the answer changes the plan |
|---|---|---|
| 1 | How many months/days until your first interview or drive? | <=45 days: 30-day plan. 45-75: 60. 75-130: 90. >130: 180 |
| 2 | Current level: can you solve easy problems alone? Do you know arrays/recursion? | Beginner: start the plan at sheet problem 1 and add 1 week. Intermediate: as written. Advanced: skip problems 1-60 |
| 3 | Target company type: service (TCS/Infosys), mid-tier product, FAANG-like, startup? | Picks the plan and the time split in section 4 |
| 4 | Language: Java, Python or C++? | Java/C++ suit the sheet; Python is fine. Add languages.md slot weekly |
| 5 | Hours per day (2, 4, 6+)? | Picks the daily template (section 3). If under 2h, stretch the plan by 1.5x |
| 6 | Weak areas (DP, graphs, OS, SQL, aptitude, communication)? | Add 1 extra slot per week for each weak area and push it earlier in the plan |

Rule: if months left and target disagree (e.g. 30 days but FAANG-like), say so honestly and aim for the best achievable tier (mid-tier product), then continue with the 90-day plan after the first offer.

## 2. Plans

### 2.1 30-Day Crash Plan (service / mass recruiters)

Goal: clear aptitude + online test + basic coding + CS fundamentals + HR. DSA depth is limited to easy/medium core.

| Week | DSA topic and problems | CS subject focus | Apt / HR slot | Checkpoint |
|---|---|---|---|---|
| 1 | Basics 23-39 (maths, arrays), Arrays 68-93 | DBMS: keys, normalization, SQL joins (dbms.md) | Apt: percentages, ratios, time and work (aptitude.md), 45 min/day | Sat: 20-question timed Apt quiz; log errors |
| 2 | Strings 43-50, Hashing 100-103, Binary Search 105-112 | OOPs: 4 pillars, SOLID basics (oops.md); language basics (languages.md) | Apt: probability, P and C, logical reasoning; HR: tell me about yourself | Sat: 2 coding problems in 60 min |
| 3 | Recursion 51-60, Linked List 165-175, Stack 247-253 | OS: process vs thread, scheduling, deadlock (os.md); CN: OSI, TCP/IP, HTTP (cn.md) | Apt: data interpretation, verbal; HR: strengths, weaknesses, why this company | Sat: full mock online test (Apt + 2 coding + 20 MCQ) |
| 4 | Binary Trees 277-288 (traversals), Sorting 61-65 | Rev all subjects with short notes; DBMS SQL practice | HR: STAR stories, resume walk-through (hr.md); mock HR x2 | Days 29-30: final mock test + error-log review |

Days 1-2 of week 1: fix the resume (see SKILL.md Resume Builder) and pick one language.

### 2.2 60-Day Plan (mixed: service + mid-tier product)

| Week | DSA topic and problems | CS subject focus | Apt / HR slot | Checkpoint |
|---|---|---|---|---|
| 1 | Arrays 68-99 | OOPs (oops.md) | Apt: percentages, ratios, profit/loss | Sun: re-solve 5 problems from the error log |
| 2 | Hashing 100-104, Binary Search 105-124 | DBMS: normalization, transactions, indexing (dbms.md) | Apt: time/work, speed/distance | Sun: Apt sectional test (30 Qs) |
| 3 | Strings 137-143, Recursion 144-157, Sorting 61-67 | OS: processes, scheduling, sync (os.md) | Apt: P and C, probability | Sun: mock coding round, 2 problems/60 min |
| 4 | Linked List 165-175, 186-204 | OS: deadlock, paging, segmentation | HR: intro, strengths, weaknesses | Sun: Rev weeks 1-4 + 1 full mock test |
| 5 | Sliding Window 235-246, Stack/Queue 247-253, 260-276 | CN: OSI, TCP/UDP, HTTP, DNS (cn.md) | Apt: logical reasoning, DI | Sun: timed 3-problem set |
| 6 | Binary Trees 277-301, BST 308-321 | DBMS: SQL practice set | HR: STAR stories (hr.md) | Sun: mock technical interview (Mock Interview Mode) |
| 7 | Graphs 340-353, 362-373 (BFS/DFS, cycles, Dijkstra) | OOPs LLD basics: design patterns, SOLID (oops.md); web-backend.md REST basics | Apt: mixed mock | Sun: Rev weeks 5-7 |
| 8 | DP 384-412 (pick the [B]/core ones first) | System design intro (system-design.md); core-cs.md highlights | HR: mock HR x2 | Sun: full-length mock (Apt + coding + CS MCQ) |
| 9 | Rev only: error log problems, Heaps 322-329, Greedy 221-231 | Rev cheat sheets for OS/DBMS/CN/OOPs | HR final polish; resume check | 2 mocks, one per 3 days |

### 2.3 90-Day Plan (product companies; Striver A2Z by week)

| Week | DSA topic and problems | CS subject focus | Apt / HR slot | Checkpoint |
|---|---|---|---|---|
| 1 | Beginner 1-60 (patterns light: 1-22; maths 23-35; hashing/strings/recursion 40-60) | languages.md: pick one language, learn STL/collections | Apt: 20 min/day, percentages | Sun: Rev + start error log |
| 2 | Sorting 61-67, Arrays 68-99 | OOPs part 1 (oops.md) | Apt: ratios, time/work | Sun: 5 random re-solves from week 1-2 |
| 3 | Hashing 100-104, Binary Search 105-136 | DBMS part 1: keys, normalization, ER (dbms.md) | Apt: P and C, probability | Sun: Apt sectional + mini coding contest |
| 4 | Strings 137-143, Recursion 144-164 | OS part 1: processes, threads, scheduling (os.md) | HR: intro + strengths | Sun: mock coding (2 problems, 60 min) |
| 5 | Linked List 165-207 | OS part 2: sync, deadlock, memory, paging | Apt: logical reasoning | Sun: Rev weeks 1-5 (spaced, section 5) |
| 6 | Bit Manipulation 208-220, Greedy 221-234 | DBMS part 2: transactions, indexing, SQL practice | HR: STAR stories (hr.md) | Sun: mock round 1 (DSA + CS) |
| 7 | Sliding Window 235-246, Stack/Queue 247-276 | CN: OSI, TCP/IP, HTTP, DNS, subnetting (cn.md) | Apt: DI, verbal | Sun: timed contest, 3 problems |
| 8 | Binary Trees 277-307, BST 308-321 | OOPs part 2 + LLD: SOLID, patterns, 2 LLD problems (oops.md, system-design.md) | HR: weaknesses, conflict | Sun: mock round 2 |
| 9 | Heaps 322-339, Graphs 340-353 | core-cs.md: architecture, compiler, TOC highlights; web-backend.md | Apt: mixed mock | Sun: Rev weeks 6-9 |
| 10 | Graphs 354-383 (hard, shortest path, MST) + Tries 436-441 | LLD: 3 more problems (parking lot, LRU, rate limiter style) | HR: why this company | Sun: mock round 3 |
| 11 | DP 384-412 (1D, 2D, grids, stocks, subsequences) | System design intro: scaling, caching, DB choice (system-design.md) | Apt: weekly timed set | Sun: DP pattern recap sheet |
| 12 | DP 413-435 (LIS, strings, MCM) + Strings Adv 442-449 + Maths 450-452 (skim) | System design: 2 HLD case studies; git-github-gsoc.md basics | HR: mock HR | Sun: mock round 4 |
| 13 | Rev: error-log problems + [P] problems left | Rev all cheat sheets (OS, DBMS, CN, OOPs) | Resume final; company-specific prep (SKILL.md) | 3 full mocks (days 85, 88, 90) |

### 2.4 180-Day Plan (deep: finish sheet + CP + projects + system design)

Weeks 1-13 follow the 90-day plan's DSA order at a slower pace; extra time goes to CP, projects and depth.

| Week | DSA topic and problems | CS subject focus | Projects / CP / Apt / HR | Checkpoint |
|---|---|---|---|---|
| 1 | Beginner 1-35 (patterns, maths) | languages.md: one language deeply | Apt: start, 20 min/day | Sun: error log set up |
| 2 | 36-67 (basics, hashing, strings, recursion, sorting) | OOPs part 1 | Git/GitHub setup (git-github-gsoc.md) | Sun: Rev |
| 3 | Arrays 68-99 | OOPs part 2 | CP: join 1 weekly contest (Div 3/4 or LeetCode) | Sun: re-solve 5 |
| 4 | Hashing 100-104, Binary Search 105-124 | DBMS part 1 | Apt weekly | Sun: mini contest |
| 5 | Binary Search 125-136, Strings 137-143 | DBMS part 2 + SQL set | Project 1: pick idea, design | Sun: mock round 1 |
| 6 | Recursion 144-164 | OS part 1 | CP weekly | Sun: Rev weeks 1-6 |
| 7 | Linked List 165-207 | OS part 2 | Project 1: build core | Sun: timed 3-problem set |
| 8 | Bits 208-220, Greedy 221-234 | CN part 1 | Apt + HR intro | Sun: mock round 2 |
| 9 | Sliding Window 235-246 | CN part 2 | CP weekly | Sun: Rev |
| 10 | Stack/Queue 247-276 | OOPs LLD: SOLID, patterns | Project 1: finish, deploy, README | Sun: mock round 3 |
| 11 | Binary Trees 277-307 | LLD problems x2 | HR: STAR stories | Sun: Rev weeks 7-11 |
| 12 | BST 308-321, Heaps 322-339 | core-cs.md part 1 (architecture, compiler) | CP weekly | Sun: mock round 4 |
| 13 | Graphs 340-353 | web-backend.md: REST, auth, SQL vs NoSQL | Project 2: design (full-stack or backend) | Sun: timed contest |
| 14 | Graphs 354-373 | core-cs.md part 2 (TOC, discrete math) | CP weekly | Sun: Rev |
| 15 | Graphs 374-383, Tries 436-441 | LLD problems x2 | Project 2: build | Sun: mock round 5 |
| 16 | DP 384-401 (1D, 2D, grids, stocks) | system-design.md: fundamentals | Apt weekly | Sun: DP recap sheet |
| 17 | DP 402-418 (subsequences, LIS) | HLD: caching, load balancing | CP weekly | Sun: mock round 6 |
| 18 | DP 419-435 (strings, MCM) | HLD: DB sharding, queues (Kafka, Redis in web-backend.md) | Project 2: finish, deploy | Sun: Rev weeks 12-18 |
| 19 | Strings Adv 442-449, Maths 450-452 | HLD case study 1 (URL shortener) | HR mock | Sun: sheet complete, tag weak problems |
| 20 | Re-solve [P] problems and error-log items (topic A: trees/graphs) | OS/DBMS rapid Rev | CP: aim 1 contest/week | Sun: mock round 7 |
| 21 | Re-solve (topic B: DP/greedy/binary search) | CN/OOPs rapid Rev | Resume v1 (SKILL.md Resume Builder) | Sun: timed contest |
| 22 | LeetCode company-tagged problems (medium) 10/day | HLD case study 2 (chat/feed) | Project polish | Sun: mock round 8 |
| 23 | LeetCode company-tagged (medium/hard) | LLD x2 timed (45 min each) | HR: full STAR bank | Sun: mock round 9 |
| 24 | Mixed random mediums, timed | HLD case study 3 | Open source / GSoC-style PR (git-github-gsoc.md) | Sun: mock round 10 |
| 25 | Weak-area sprint | Weak-subject sprint | Apt maintenance; company-specific prep | Sun: 2 full mocks |
| 26 | Light daily practice only | Cheat-sheet Rev | Resume final, sleep, logistics | Final mock + error-log review |

## 3. Daily Schedule Templates

| Block | 2h day | 4h day | 6h day |
|---|---|---|---|
| Rev (error log, spaced items) | 15 min | 30 min | 45 min |
| DSA new problems (hint ladder) | 60 min | 120 min | 150 min |
| CS subject (one topic + 5 Qs) | 30 min | 60 min | 90 min |
| Apt / reasoning | 15 min | 20 min | 30 min |
| Project / LLD / CP | - | 20 min | 60 min |
| HR / communication (speak aloud) | - | 10 min | 15 min |
| Wrap-up: log errors, write tomorrow's list | - | - | 10 min |

Weekly pattern: Mon-Fri follow the template; Saturday = timed contest or mock; Sunday = weekly review (section 5) + light rest. Take 10-minute breaks every 90 minutes.

## 4. Company-Type Priority Matrix (share of study time)

| Subject | Service (TCS/Infosys/Wipro) | Mid-tier product | FAANG-like | Startups |
|---|---|---|---|---|
| DSA | 20% | 40% | 50% | 30% |
| Aptitude and verbal | 30% | 10% | 0-5% | 5% |
| OS/DBMS/CN/OOPs | 20% | 20% | 10% | 15% |
| LLD / HLD | 0-5% | 10% | 15% | 15% |
| Projects / web-backend | 5% | 10% | 5% | 25% |
| Language and SQL | 10% | 5% | 5% | 5% |
| HR / communication | 10% | 5% | 5% | 5% |
| Mocks (counted inside above, minimum) | 1 per week | 1 per week | 2 per week | 1 per week |

Notes: service tests are timed MCQs, so speed on Apt matters most. FAANG-like adds CP-style thinking and clean communication while coding. Startups ask for a shipped project and practical backend/frontend knowledge.

## 5. Revision Strategy

Spaced repetition schedule (apply to every solved problem or concept):

| Review | When | What to do |
|---|---|---|
| R1 | Next day | Re-explain approach from memory (5 min) |
| R2 | Day 3 | Re-code without looking |
| R3 | Day 7 | Re-solve cold, timed |
| R4 | Day 21 | Re-solve only if wrong or slow before |
| R5 | Day 45 | Random pick; stop reviewing a problem after 2 clean passes |

Error log method: keep one table with columns Problem/Concept | Date | Why I failed (pattern missed, edge case, syntax, time out) | Fix in one line | Next review date. Tag the cause, not the problem; after 2 weeks count tags and train the top one. Add every wrong MCQ and every mock mistake.

Weekly review (Sunday, 60-90 min): (1) re-solve 5 items from the log, (2) skim the week's notes, (3) count problems done against the plan, (4) decide to catch up or compress next week (never carry more than 1 week of backlog), (5) update the PREP CHECKPOINT block (SKILL.md Session Continuity).

## 6. Common Mistakes and Fixes

| Mistake | Fix |
|---|---|
| Tutorial hell: watching videos without coding | Rule: 30% watch, 70% code. Try 20-30 min before any hint or video |
| Skipping CS fundamentals (OS/DBMS/CN/OOPs) | Fixed weekly slot; these decide service and many product rounds |
| No mocks until the last week | Mock every week from week 4; use Mock Interview Mode |
| Jumping topics, leaving the sheet half done | Follow sheet order; [P] problems are last |
| Copying solutions without understanding | Re-code from memory next day (R1/R2); explain aloud |
| Ignoring aptitude for service companies | Daily 20 min; timed sectional tests |
| Ignoring edge cases and complexity | State time/space and one edge case for every solution |
| Resume claims you cannot defend | Know every line; prepare 2 deep project stories |
| Burnout from marathon days | Fixed hours, one rest half-day weekly, sleep 7h |
| Comparing with others' problem counts | Track your own error-log trend instead |

## 7. Free Resource Pointers (names only)

| Subject | Resources |
|---|---|
| DSA | takeUforward (Striver A2Z sheet and videos), LeetCode, GeeksforGeeks, NeetCode |
| CP | Codeforces, CodeChef, AtCoder, CSES Problem Set |
| OS | Gate Smashers (YouTube), Neso Academy, Operating System Concepts (Galvin) |
| DBMS | Gate Smashers, Knowledge Gate, SQLZoo, HackerRank SQL |
| CN | Gate Smashers, Neso Academy, Computer Networking: A Top-Down Approach |
| OOPs and LLD | Refactoring Guru (design patterns), Head First Design Patterns, Concept and Coding (YouTube) |
| System design | ByteByteGo, Gaurav Sen (YouTube), System Design Primer (GitHub) |
| Aptitude | IndiaBIX, R.S. Aggarwal, PrepInsta, Freshersworld |
| Core CS / TOC | NPTEL, Neso Academy, Gate Smashers |
| Web/backend | MDN Web Docs, roadmap.sh, freeCodeCamp |
| Git/open source | Pro Git book, GitHub Skills, GSoC archive |
| HR/communication | Mock sessions with friends, Pramp, recorded self-practice |
