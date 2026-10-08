# WARP.md — Quick Reference Cheatsheet

This file is loaded during Revision Mode or when the student asks for a cheat sheet. It contains the fastest lookup material across all subjects.

---

## DSA at a Glance

### Time Complexities to Memorize

| Operation | Array | Linked List | BST (avg) | Hash Map |
|---|---|---|---|---|
| Search | O(n) | O(n) | O(log n) | O(1) |
| Insert | O(1) end | O(1) head | O(log n) | O(1) |
| Delete | O(n) | O(n) | O(log n) | O(1) |

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n2) | O(n2) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n2) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

### Top 10 DSA Patterns for Interviews

1. Sliding Window
2. Two Pointers
3. Fast and Slow Pointers
4. Merge Intervals
5. Cyclic Sort
6. Binary Search on Answer
7. BFS and DFS
8. Dynamic Programming (Top Down + Bottom Up)
9. Backtracking
10. Monotonic Stack

---

## OS at a Glance

### Process States
New -> Ready -> Running -> Waiting -> Terminated

### CPU Scheduling Algorithms
- FCFS: Non preemptive, convoy effect problem
- SJF: Optimal average wait time, starvation possible
- Round Robin: Time quantum based, best for time sharing
- Priority Scheduling: Preemptive or non preemptive

### Deadlock Conditions (all four must hold)
1. Mutual Exclusion
2. Hold and Wait
3. No Preemption
4. Circular Wait

### Page Replacement Algorithms
- FIFO: Simple, Belady's anomaly possible
- LRU: Optimal in practice, costly to implement
- Optimal: Best performance, not implementable in real time

---

## OOPs at a Glance

### Four Pillars
| Pillar | One Line Definition |
|---|---|
| Encapsulation | Binding data and methods, hiding internals |
| Abstraction | Showing only necessary details |
| Inheritance | Child class inherits parent class properties |
| Polymorphism | One interface, many implementations |

### SOLID Principles
- S: Single Responsibility
- O: Open Closed
- L: Liskov Substitution
- I: Interface Segregation
- D: Dependency Inversion

### Common Design Patterns
- Singleton: One instance globally
- Factory: Create objects without specifying class
- Observer: Subscribe and notify pattern
- Decorator: Add behavior without changing class
- Strategy: Swap algorithms at runtime

---

## Computer Networks at a Glance

### OSI Layers (top to bottom)
7. Application (HTTP, FTP, DNS)
6. Presentation (SSL, encryption)
5. Session (session management)
4. Transport (TCP, UDP)
3. Network (IP, routing)
2. Data Link (MAC, switches)
1. Physical (cables, signals)

### TCP vs UDP
| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection oriented | Connectionless |
| Reliability | Guaranteed delivery | No guarantee |
| Speed | Slower | Faster |
| Use case | HTTP, FTP, Email | Video, DNS, Gaming |

### HTTP Status Codes to Know
- 200: OK
- 201: Created
- 301: Moved Permanently
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

---

## DBMS at a Glance

### Normal Forms
- 1NF: No repeating groups, atomic values
- 2NF: 1NF + no partial dependency
- 3NF: 2NF + no transitive dependency
- BCNF: Every determinant is a candidate key

### ACID Properties
- Atomicity: All or nothing
- Consistency: Valid state before and after
- Isolation: Transactions do not interfere
- Durability: Committed data persists

### SQL Commands by Category
- DDL: CREATE, ALTER, DROP, TRUNCATE
- DML: SELECT, INSERT, UPDATE, DELETE
- DCL: GRANT, REVOKE
- TCL: COMMIT, ROLLBACK, SAVEPOINT

---

## Aptitude Quick Formulas

### Time and Work
- If A finishes in n days, A's 1 day work = 1/n
- Combined work of A and B = 1/a + 1/b

### Speed, Distance, Time
- Distance = Speed x Time
- Average Speed (two legs) = 2ab / (a+b)

### Percentages
- X% of Y = (X x Y) / 100
- Percentage change = (New - Old) / Old x 100

### Probability
- P(A) = Favorable outcomes / Total outcomes
- P(A and B) = P(A) x P(B) for independent events
- P(A or B) = P(A) + P(B) - P(A and B)

### Permutations and Combinations
- nPr = n! / (n-r)!
- nCr = n! / (r! x (n-r)!)

---

## System Design Quick Framework

### For any system design question, follow RESHADED:

**R** — Requirements (functional and non functional)
**E** — Estimation (scale, storage, bandwidth)
**S** — Storage schema (DB choice, schema design)
**H** — High level design (components, services)
**A** — APIs (define key APIs)
**D** — Data flow (how data moves through system)
**E** — Explain bottlenecks and how to handle them
**D** — Deep dive into one component

### Common System Design Components
- Load Balancer: Distributes traffic
- Cache (Redis): Reduces DB load
- CDN: Serves static content fast
- Message Queue (Kafka): Async communication
- Database Sharding: Horizontal scaling
- Replication: High availability

---

## Striver A2Z Pattern Quick Map

| Pattern | Clue in problem | One-line template | Example # |
|---|---|---|---|
| Two pointers | sorted, pair, reverse, partition | l=0,r=n-1; move by comparison | 39, 57, 77 |
| Prefix sum + hashmap | subarray sum/xor = K | map prefix->count; look up pref-K | 101, 102, 104 |
| Kadane | max sum/product subarray | cur=max(a[i],cur+a[i]) | 92, 98 |
| Moore voting | majority > n/2 or n/3 | candidate+count, cancel, verify | 79, 94 |
| Binary search bound | sorted, first >= x, floor/ceil | ans=n; if pred(mid) ans=mid,hi=mid-1 | 106, 107, 110 |
| Rotated array BS | sorted then rotated | find sorted half, test target there | 111, 113 |
| BS on answer | "minimize the max", monotonic check | lo..hi range, check(mid) O(n) scan | 117, 122, 125 |
| Subsets pick/not-pick | all subsets, sum K | f(i): skip f(i+1) / take f(i+1) | 146, 149, 150 |
| Backtracking dup skip | unique combos with duplicates | sort; skip if i>idx && a[i]==a[i-1] | 153, 155, 156 |
| Constraint backtracking | N-Queen, Sudoku, colouring | try, validate, recurse, undo | 160, 162, 163 |
| Slow/fast pointers | middle, cycle, Nth from end | slow+=1, fast+=2 | 192, 196, 197 |
| In-place list reversal | reverse, palindrome, k-group | prev=null; save next; relink | 190, 194, 199 |
| Sliding window var | longest/shortest substring with rule | expand r; while invalid shrink l | 236, 241, 242 |
| Exactly K | count subarrays with exactly k | atMost(k)-atMost(k-1) | 244, 245, 246 |
| Greedy sort by end | max non-overlapping intervals | sort by end; take if start>=last end | 227, 228 |
| Merge intervals | overlapping ranges | sort by start; extend last end | 229, 230 |
| Monotonic stack | next greater/smaller, histogram | pop while top violates order | 260, 262, 270 |
| Monotonic deque | window max/min | deque of indices, drop out-of-window | 268 |
| Tree DFS return value | height, diameter, balanced, path | return from children, update global | 282, 283, 285 |
| Level-order BFS | level, views, zigzag | queue; process level size per round | 280, 289, 292 |
| LCA / BST bounds | ancestor; validate BST | return node if p/q; pass (low,high) | 296, 313 |
| Heap top-K / K-way | kth largest, merge K lists | size-k heap; heap of (val,list,pos) | 329, 331, 337 |
| Two heaps | running median | max-heap low half, min-heap high half | 338 |
| Graph BFS/DFS grid | islands, flood, regions | visited + dir arrays, count starts | 343, 344, 348 |
| Topological sort | prerequisites, DAG order | Kahn: indegree queue; size<V = cycle | 352, 355, 357 |
| Dijkstra | shortest path, weights >= 0 | min-heap (dist,node); skip stale | 362, 365, 372 |
| DSU | dynamic connectivity, MST | find w/ compression, union by rank | 374, 375, 377 |
| DP 1D / grid | depends on last 1-2 cells | dp[i]=f(dp[i-1],dp[i-2]); roll vars | 384, 385, 390 |
| Knapsack 0/1 vs unbounded | subset sum, coins, reuse | 0/1: w down; unbounded: w up | 402, 407, 410 |
| LIS / LCS | increasing subseq; two strings | LIS tails+BS; LCS dp[i][j] on prefixes | 413, 419, 420 |
| Partition DP (MCM) | split interval at k | dp[i][j]=best_k dp[i][k]+dp[k+1][j]+cost | 430, 431 |
| Trie | prefix queries, max XOR | child links + end flag | 436, 437, 441 |
| Bit tricks | unique element, power of 2, subsets | n&(n-1); XOR all; mask 0..2^n-1 | 211, 213, 219 |

---

## Core CS in 1 minute

### COA
- Pipeline hazards: structural (resource), data (RAW/WAR/WAW), control (branch). Fix: forwarding, stalls, prediction.
- AMAT = Hit time + Miss rate x Miss penalty. Multilevel: L1 hit + m1 x (L2 hit + m2 x mem).
- CPU time = IC x CPI x cycle time. Ideal pipeline speedup ~ k stages.
- Amdahl: Speedup = 1 / ((1-f) + f/s); limit = 1/(1-f).
- Cache mapping: direct (1 line/block), fully assoc (any), k-way (set = block mod sets). Misses: compulsory, capacity, conflict.
- Write policy: write-through (simple, slow) vs write-back (dirty bit, fast).

### Compiler phases
Lexical -> Syntax -> Semantic -> Intermediate code -> Optimization -> Code generation. Symbol table + error handler span all.
- Lexer: regex/DFA, tokens. Parser: CFG. LL(1) top-down (no left recursion, left-factored). LR family bottom-up: LR(0) < SLR < LALR < CLR in power.
- FIRST/FOLLOW build the LL(1) table. Shift-reduce and reduce-reduce are LR conflicts.
- Optimizations: constant folding, dead code elimination, CSE, loop invariant motion, strength reduction.

### TOC
| Type | Grammar | Machine | Closed under |
|---|---|---|---|
| 3 Regular | A->aB or a | DFA/NFA | union, concat, star, complement, intersect |
| 2 Context-free | A->alpha | PDA | union, concat, star (NOT intersect, complement) |
| 1 Context-sensitive | alpha A beta->alpha gamma beta | LBA | most ops |
| 0 Recursively enumerable | any | Turing machine | union, concat (NOT complement) |
- Pumping lemma proves NON-regular / non-CFL. a^n b^n is CFL not regular; a^n b^n c^n is CSL not CFL.
- NFA->DFA up to 2^n states. Halting problem undecidable. P subset NP; NP-complete = NP and NP-hard (SAT first).
- Decidable = recursive; semi-decidable = RE.

---

## Languages in 1 minute

### Java
- == compares references, equals() content; override hashCode with equals.
- Strings immutable and pooled; use StringBuilder in loops (StringBuffer is synchronized).
- Integer cache -128..127: == true inside, false outside.
- Pass by value always (reference copied); no multiple class inheritance, interfaces ok.
- Checked vs unchecked exceptions; finally runs even after return; try-with-resources closes AutoCloseable.
- HashMap not thread safe (use ConcurrentHashMap); generics erased at runtime; final vs finally vs finalize.

### Python
- Mutable default arg (def f(x=[])) is shared across calls; use None.
- is vs ==; small ints and interned strings are cached.
- GIL: one thread runs bytecode at a time; multiprocessing for CPU work, threads for IO.
- Late-binding closures in loops (lambda captures variable, not value).
- Shallow vs deep copy (copy.deepcopy); [[0]*n]*m shares rows.
- Lists/dicts/sets mutable, tuples/str/frozenset immutable; dict keeps insertion order; generators are lazy.

### C++
- Dangling pointer/reference, leaks: prefer unique_ptr/shared_ptr (RAII).
- Rule of 3/5: define dtor, copy ctor, copy assign (+ move ctor, move assign) together.
- Virtual destructor needed in polymorphic base; slicing when copying derived into base by value.
- Reference cannot be null or reseated; pointer can; const correctness (const T*, T* const).
- Undefined behaviour: signed overflow, out-of-bounds, uninitialised read, use after free.
- vector resize invalidates iterators; operator[] unchecked vs at() checked; map ordered O(log n), unordered_map O(1) avg.

---

## Web/Backend in 1 minute

### HTTP status codes
| Range | Meaning | Common |
|---|---|---|
| 1xx | Info | 101 Switching Protocols |
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirect | 301 Permanent, 302 Found, 304 Not Modified |
| 4xx | Client error | 400 Bad Req, 401 Unauthenticated, 403 Forbidden, 404, 409 Conflict, 429 Too Many |
| 5xx | Server error | 500, 502 Bad Gateway, 503 Unavailable, 504 Gateway Timeout |
- Idempotent: GET, PUT, DELETE, HEAD. POST and PATCH are not necessarily. Safe: GET, HEAD.

### Auth vs Authz
- Authentication = who are you (login, 401). Authorization = what may you do (roles/permissions, 403).

### JWT vs Session
| | JWT | Session |
|---|---|---|
| State | stateless, token holds claims | server stores session, client holds ID cookie |
| Scale | easy across servers | needs shared store (Redis) |
| Revoke | hard (short expiry + refresh token) | easy (delete session) |
| Risk | XSS if in localStorage; payload is readable, only signed | CSRF (use SameSite, tokens) |

### REST vs GraphQL
- REST: many endpoints, fixed shapes, HTTP caching easy, over/under-fetching.
- GraphQL: one endpoint, client picks fields, no over-fetch, N+1 risk, caching harder.

### SQL vs NoSQL
- SQL: fixed schema, joins, ACID, vertical scale; relational/transactional data.
- NoSQL: flexible schema, horizontal scale, BASE/eventual consistency; key-value, document, column, graph.
- CAP: pick 2 of consistency, availability, partition tolerance (P is mandatory in distributed systems).

---

## Last 24 hours before interview

- [ ] Re-read this WARP.md once; do not start new topics.
- [ ] Redo 5 to 8 problems you got wrong earlier, one per major pattern (use the Quick Map above).
- [ ] Rehearse 2 projects: problem, your role, tech choices, one hard bug, one metric.
- [ ] Prepare "Tell me about yourself" (60-90 s) and 3 STAR stories (conflict, failure, leadership).
- [ ] Skim OS, DBMS, CN, OOPs one-liners; SQL joins/group by; one LLD (parking lot or LRU).
- [ ] Check company, role, interview format; prepare 3 questions to ask them.
- [ ] Setup: laptop charged, IDE/online editor, internet, ID, resume copies, quiet room, link tested.
- [ ] Sleep 7+ hours, eat light, stop studying 2 hours before bed; no all-nighter.
- [ ] On the day: short walk, water, log in 10 min early.

---

## Interview communication template (coding round)

1. Clarify: restate the problem; ask constraints, input size, duplicates, sorted or not, edge cases.
2. Examples: walk one small example plus one edge case by hand.
3. Brute force first: state it and its complexity, say why it is too slow.
4. Optimize: name the pattern and the clue ("sorted + pair -> two pointers"); give the idea before coding.
5. Code: narrate while writing with clean names and edge handling; then dry-run the example.
6. Wrap up: state time and space complexity, test edges, mention trade-offs; if stuck, think aloud and ask for a hint.
