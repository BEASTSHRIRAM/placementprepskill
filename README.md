# Claude Interview Prep Skill

A comprehensive Claude skill designed for final-year and pre-placement BTech Computer Science students. This skill equips Claude to act as a dedicated interview preparation coach covering every subject and aptitude area that top tech companies test.

Open Claude.com go in customization and click on skill and upload the zip file by downloading it from here 
## What This Skill Covers

| Subject | Topics |
|---|---|
| Data Structures and Algorithms | Arrays, Linked Lists, Trees, Graphs, DP, Sorting, Searching |
| Operating Systems | Processes, Threads, Memory Management, Scheduling, Deadlocks |
| Object Oriented Programming | Classes, Inheritance, Polymorphism, Abstraction, Design Patterns |
| Computer Networks | OSI Model, TCP/IP, HTTP, DNS, Routing, Socket Programming |
| Database Management Systems | SQL, Normalization, Transactions, Indexing, Query Optimization |
| Aptitude and Reasoning | Quantitative, Logical, Verbal, Puzzles |
| System Design | LLD, HLD, Scalability, Caching, Load Balancing |
| Core CS Fundamentals | Compiler Design, Theory of Computation, Computer Architecture, Discrete Math |
| Striver A2Z Sheet | All 452 problems in sheet order with the pattern, key idea and complexity for each |
| Languages and Web | Java, Python, C++ internals; REST, auth, Docker, JS/React |
| LLD and Puzzles | 10 classic LLD problems, 25 puzzles, data interpretation, output prediction |
| Study Plans | 30/60/90/180-day plans, daily schedules, company-wise priorities |

## How to Use

Install the whole skill folder (SKILL.md plus `references/` and `resume-builder/`, zipped with the folder as the zip root) in Claude's skills settings or your Claude skills directory. SKILL.md alone is not enough, because it loads the reference files on demand. Once active, Claude will automatically detect interview prep related requests and respond with structured, exam and interview quality answers.

### Studying across several days

Claude does not remember previous chats. The skill prints a `PREP CHECKPOINT` block after each topic and when you say "save" or "done for today". Paste it as your first message in a new chat and say "continue" to resume exactly where you stopped. In Claude Code, it also saves the block to `prep-progress.md`.

### Example Triggers

- "Continue Striver A2Z from problem 61 and teach me the pattern first"
- "Make me a 60 day plan, I have 4 hours a day"
- "Design a parking lot (LLD) like an interviewer would ask"

- "Explain process scheduling algorithms for my OS interview"
- "Give me 10 DSA problems on trees with solutions"
- "What DBMS questions are asked in Amazon interviews?"
- "Practice aptitude questions on time and work"
- "Explain the four pillars of OOPs with code"
- "How does TCP handshake work? Interview style answer"

## Skill Structure

```
btech-cse-interview-prep/
├── LICENSE
├── README.md
├── SKILL.md              <- Core skill instructions for Claude
├── WARP.md               <- Quick reference cheatsheet
├── references/
│   ├── dsa.md            <- DSA patterns and problems
│   ├── striver-a2z.md    <- Striver A2Z index (452 problems, routes to chunks)
│   ├── striver/          <- 5 chunk files: per-problem pattern, idea, complexity + Pattern Playbook
│   ├── os.md             <- OS concepts and questions
│   ├── oops.md           <- OOP principles and design patterns
│   ├── cn.md             <- Computer Networks reference
│   ├── dbms.md           <- DBMS and SQL reference + SQL practice set
│   ├── core-cs.md        <- COA, Compiler Design, TOC, Discrete Math
│   ├── languages.md      <- Java, Python, C++ interview fundamentals
│   ├── web-backend.md    <- REST, auth, SQL vs NoSQL, Docker, JS/React
│   ├── lld-problems.md   <- 10 classic LLD interview problems
│   ├── puzzles.md        <- Puzzles, data interpretation, output prediction
│   ├── study-plans.md    <- 30/60/90/180-day plans mapped to Striver ranges
│   ├── aptitude.md       <- Aptitude formulas and tricks
│   ├── system-design.md  <- System design frameworks
│   ├── hr.md             <- HR and behavioural round prep
│   └── git-github-gsoc.md <- Git, GitHub and GSoC guide
└── resume-builder/
    └── templates/
        ├── html-template.md  <- HTML + CSS visual resume template
        └── latex-template.md <- LaTeX ATS resume template (Overleaf)
```

## Target Audience

BTech CSE students preparing for placements at product companies (FAANG, startups, service based companies), targeting roles like SDE 1, Software Engineer, and Graduate Engineer Trainee.

## Contributing

Pull requests are welcome. Please keep content accurate, concise, and interview focused.

## Thank You
A star would be appreciated if you get help from this.
