# Striver A2Z: Graphs, DP, Tries, Advanced Strings, Maths

## Pattern Playbook

| Pattern | Use when (clue in the problem statement) | Template/steps in 1-2 lines | Problem numbers |
|---|---|---|---|
| Graph traversal / components | "connected", "provinces", reachability, count groups | Build adjacency list, visited[]; loop all nodes, BFS/DFS from each unvisited, count starts | 340, 341, 342, 376 |
| BFS/DFS grid traversal | Grid of 0/1 or chars, 4/8-direction moves, islands, regions | For each unvisited cell, flood with BFS/DFS using dir arrays and bounds check | 343, 344, 345, 348, 349 |
| Multi-source BFS | "nearest", "minimum time to spread" from many starting cells | Push all sources at distance 0 into queue, BFS level by level | 346, 347 |
| Cycle detection | "cycle", "deadlock", "is it a DAG" | Undirected: DFS with parent or DSU. Directed: DFS with recursion-stack (path) visited, or Kahn count | 350, 353, 354 |
| Bipartite coloring | "two groups", "2-colorable", odd cycle | BFS/DFS color neighbors opposite; conflict means not bipartite | 351 |
| Topological sort / Kahn | Dependencies, prerequisites, ordering, DAG | Compute indegree, queue zero-indegree nodes, pop and decrement; order size < V means cycle | 352, 354, 355, 356, 357, 358 |
| BFS shortest path (unit weights) | Shortest path, all edges weight 1, transformations | BFS from source with dist[]; for word ladder treat each one-letter change as an edge | 359, 360, 361 |
| Dijkstra | Shortest path, non-negative weights, min cost/effort/time | Min-heap of (dist,node); pop, skip stale, relax neighbors; adapt cost function for minimax | 362, 363, 364, 365, 366, 367, 368, 372, 373 |
| Bellman-Ford | Negative edges, detect negative cycle, at most K edges | Relax all edges V-1 times; one more pass that still relaxes means negative cycle | 369 |
| Floyd-Warshall | All-pairs shortest path, small V (<=~400) | For k, i, j: d[i][j]=min(d[i][j], d[i][k]+d[k][j]) | 370, 371 |
| DSU (Union-Find) | Dynamic connectivity, merge groups, count components under unions | parent[]+rank/size, find with path compression, union by rank/size | 374, 376, 377, 378, 379, 380 |
| MST (Kruskal/Prim) | Connect all nodes with min total edge weight | Kruskal: sort edges, add if DSU finds different sets. Prim: min-heap from any node | 375 |
| Bridges / SCC / articulation points | Critical connections, strongly connected components, single points of failure | Kosaraju: DFS finish order, reverse graph, DFS in that order. Tarjan: tin[]/low[] and low[child] vs tin[node] | 381, 382, 383 |
| DP 1D | State depends on last 1-2 (or K) previous positions | dp[i] = f(dp[i-1], dp[i-2], ...); roll variables to O(1) space | 384, 385, 386, 387, 388 |
| DP with extra state (2D DP) | Choice at each step constrained by previous choice | dp[day][last] = best over last' != last | 389 |
| Grid DP | Move right/down in grid, path count/min cost, matrix subproblems | dp[i][j] from top/left (or top 3 cells); optionally 3D for two walkers | 390, 391, 392, 393, 394, 395 |
| DP on stocks | Buy/sell with limits on transactions, fee, cooldown | dp[i][canBuy][cap]; buy: -p+dp[i+1][0], sell: +p+dp[i+1][1] | 396, 397, 398, 399, 400, 401 |
| Subsequence pick/not-pick | Choose subset, sum equals target, count subsets | f(i,t)=f(i-1,t) or f(i-1,t-a[i]); tabulate as boolean/count table | 402, 403, 404, 405, 406, 409 |
| Knapsack 0/1 | Each item used at most once, maximize value under capacity | dp[i][w]=max(skip, val+dp[i-1][w-wt]); 1D loop w downwards | 407, 402, 403, 404, 405, 406, 409 |
| Unbounded knapsack | Items reusable unlimited times, coins, cuts | dp[i][w]=min/max/sum(skip, take staying on i); 1D loop w upwards | 408, 410, 411, 412 |
| LIS | Longest increasing/chain/divisible subsequence | dp[i]=1+max dp[j] (j<i, ok(j,i)) O(N^2); or tails array with binary search O(N log N) | 413, 414, 415, 416, 417, 418 |
| LCS / string DP | Two strings, match/mismatch, edit, palindrome subsequence | dp[i][j] over prefixes: match -> 1+dp[i-1][j-1], else max/min of neighbors | 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429 |
| Partition DP (MCM) | Split interval [i..j] at k, cost combines left and right | dp[i][j]=best over k of dp[i][k]+dp[k+1][j]+cost; fill by increasing length | 430, 431, 432, 433, 434, 435 |
| Trie | Prefix queries, word dictionary, XOR maximization | Nodes with child links + end flag/count; insert/search by char or bit walk | 436, 437, 438, 439, 440, 441 |
| String manipulation | Parse/transform string, bracket balance, run-length style | Two pointers/stack/counters; build result in a single pass | 442, 443, 444 |
| KMP / Z / rolling hash | Pattern in text, border/prefix-suffix, palindromic prefix | KMP: LPS array. Z: z[i]=LCP with prefix. Rabin-Karp: rolling hash then verify | 445, 446, 447, 448, 449 |
| Number theory (Sieve) | Many primes up to N, factorization of many queries, prime ranges | Sieve: mark multiples from i*i; SPF array gives O(log N) factorization; segmented sieve for [L,R] | 450, 451, 452 |

## Graphs (id 2009)
### Theory and traversals (id 2083)
Sub-pattern focus: BFS uses a queue (level order), DFS uses recursion/stack; both O(V+E). Loop over all nodes to handle disconnected graphs.
340. Traversal Techniques | Pattern: Graph traversal / components | Idea: BFS with queue or DFS with recursion plus visited array; adjacency list | TC O(V+E) SC O(V)
341. Connected Components | Pattern: Graph traversal / components | Idea: Start DFS/BFS from every unvisited node; count number of starts | TC O(V+E) SC O(V)
### Traversal Problems (id 2084)
Sub-pattern focus: Grid is an implicit graph; cells are nodes, 4 neighbors are edges.
342. Number of provinces | Pattern: Graph traversal / components | Idea: Adjacency matrix; DFS from each unvisited city, count components (LC 547) | TC O(V^2) SC O(V)
343. Number of islands | Pattern: BFS/DFS grid traversal | Idea: DFS/BFS from each unvisited '1', mark visited, count starts (LC 200) | TC O(N*M) SC O(N*M)
344. Flood fill algorithm | Pattern: BFS/DFS grid traversal | Idea: DFS from start cell recoloring cells of original color (LC 733) | TC O(N*M) SC O(N*M)
345. Number of enclaves | Pattern: BFS/DFS grid traversal | Idea: Traverse from boundary land cells, mark reachable; count unmarked land (LC 1020) | TC O(N*M) SC O(N*M)
346. Rotten Oranges | Pattern: Multi-source BFS | Idea: Queue all rotten cells; BFS by minutes; fresh left means -1 (LC 994) | TC O(N*M) SC O(N*M)
347. Distance of nearest cell having one | Pattern: Multi-source BFS | Idea: Push all 1-cells at dist 0, BFS to fill distances (like LC 542) | TC O(N*M) SC O(N*M)
348. Surrounded Regions | Pattern: BFS/DFS grid traversal | Idea: DFS from boundary 'O's to mark safe; flip remaining 'O' to 'X' (LC 130) | TC O(N*M) SC O(N*M)
349. Number of distinct islands | Pattern: BFS/DFS grid traversal | Idea: DFS recording shape relative to base cell; store shape in a set | TC O(N*M) SC O(N*M)
### Cycles (id 2085)
Sub-pattern focus: Undirected cycle = visited neighbor that is not parent. Directed cycle needs path-visited or indegree.
350. Detect a cycle in an undirected graph | Pattern: Cycle detection | Idea: BFS/DFS carrying parent; visited neighbor not equal parent means cycle (or DSU) | TC O(V+E) SC O(V)
351. Bipartite graph | Pattern: Bipartite coloring | Idea: BFS/DFS 2-coloring each component; same-color edge means not bipartite (LC 785) | TC O(V+E) SC O(V)
352. Topological sort or Kahn's algorithm | Pattern: Topological sort / Kahn | Idea: Indegree array; pop zero-indegree nodes, decrement neighbors, append to order | TC O(V+E) SC O(V)
353. Detect a cycle in a directed graph | Pattern: Cycle detection | Idea: DFS with path-visited array, or Kahn: order size < V means cycle | TC O(V+E) SC O(V)
### Hard Problems (id 2086)
Sub-pattern focus: "Dependencies" means topological order; "reverse graph" trick for safe states.
354. Find eventual safe states [P] | Pattern: Topological sort / Kahn | Idea: Reverse edges, run Kahn; nodes popped are safe; or DFS cycle check (LC 802) | TC O(V+E) SC O(V)
355. Course Schedule I [P] | Pattern: Topological sort / Kahn | Idea: Kahn on prerequisites; possible iff all courses processed (LC 207) | TC O(V+E) SC O(V+E)
356. Course Schedule II [P] | Pattern: Topological sort / Kahn | Idea: Kahn order is the answer; empty if cycle (LC 210) | TC O(V+E) SC O(V+E)
357. Alien Dictionary [P] | Pattern: Topological sort / Kahn | Idea: Compare adjacent words for first differing char to build edges, then topo sort | TC O(total chars + K) SC O(K)
358. Shortest path in DAG | Pattern: Topological sort / Kahn | Idea: Topo order, then relax edges in that order from source | TC O(V+E) SC O(V)
359. Shortest path in undirected graph with unit weights | Pattern: BFS shortest path (unit weights) | Idea: BFS from source with dist array; unreachable is -1 | TC O(V+E) SC O(V)
360. Word ladder I [P] | Pattern: BFS shortest path (unit weights) | Idea: BFS; change each letter a-z, check in word set, count levels (LC 127) | TC O(N*L*26) SC O(N*L)
361. Word ladder II [P] | Pattern: BFS shortest path (unit weights) | Idea: BFS by levels tracking parents, then backtrack all shortest paths (LC 126) | TC exponential worst case SC O(N*L)
### Shortest Path Algorithms (id 2087)
Sub-pattern focus: Non-negative weights use Dijkstra; negative edges use Bellman-Ford; all pairs uses Floyd-Warshall.
362. Dijkstra's algorithm | Pattern: Dijkstra | Idea: Min-heap (dist,node); pop, relax neighbors, push improved distances | TC O((V+E) log V) SC O(V+E)
363. Print Shortest Path | Pattern: Dijkstra | Idea: Dijkstra with parent[]; backtrack from destination to source and reverse | TC O((V+E) log V) SC O(V+E)
364. Shortest Distance in a Binary Maze | Pattern: Dijkstra | Idea: BFS (unit cost) over 0/1 grid with dist[][]; Dijkstra also works | TC O(N*M) SC O(N*M)
365. Path with minimum effort | Pattern: Dijkstra | Idea: Dijkstra where cost is max abs height difference along path (LC 1631) | TC O(N*M log(N*M)) SC O(N*M)
366. Cheapest flight within K stops [P] | Pattern: Dijkstra | Idea: BFS/queue on (stops,node,cost) with stops-ordering, or Bellman-Ford K+1 rounds (LC 787) | TC O(E*K) SC O(V)
367. Minimum multiplications to reach end [P] | Pattern: BFS shortest path (unit weights) | Idea: Nodes are values mod 100000; BFS multiplying by each array element | TC O(100000*N) SC O(100000)
368. Number of ways to arrive at destination [P] | Pattern: Dijkstra | Idea: Dijkstra with ways[]; equal distance adds ways, shorter resets (LC 1976) | TC O((V+E) log V) SC O(V+E)
369. Bellman ford algorithm [P] | Pattern: Bellman-Ford | Idea: Relax all edges V-1 times; extra pass relaxing means negative cycle | TC O(V*E) SC O(V)
370. Floyd warshall algorithm [P] | Pattern: Floyd-Warshall | Idea: Triple loop via intermediate k; negative diagonal means negative cycle | TC O(V^3) SC O(V^2)
371. Find the city with the smallest number of neighbors [P] | Pattern: Floyd-Warshall | Idea: All-pairs distances, count cities within threshold, pick min (ties: larger id) (LC 1334) | TC O(V^3) SC O(V^2)
372. Network Delay Time | Pattern: Dijkstra | Idea: Dijkstra from K; answer is max distance, -1 if any unreachable (LC 743) | TC O(E log V) SC O(V+E)
373. Swim in Rising Water [P] | Pattern: Dijkstra | Idea: Dijkstra minimizing max cell value along path (or binary search + BFS) (LC 778) | TC O(N^2 log N) SC O(N^2)
### Minimum Spanning Tree (id 2088)
Sub-pattern focus: DSU is the building block for Kruskal.
374. Disjoint Set | Pattern: DSU | Idea: parent[] with path compression and union by rank/size | TC O(alpha(N)) per op SC O(N)
375. Find the MST weight | Pattern: MST | Idea: Kruskal: sort edges, union if different components; or Prim with heap | TC O(E log E) SC O(V)
### Hard Problems II (id 2089)
Sub-pattern focus: Group merging and dynamic connectivity are DSU problems.
376. Number of operations to make network connected | Pattern: DSU | Idea: Need E >= V-1; answer is components-1 (LC 1319) | TC O(V+E) SC O(V)
377. Accounts merge | Pattern: DSU | Idea: Union accounts sharing an email via email-to-owner map; group and sort emails (LC 721) | TC O(N*K log(N*K)) SC O(N*K)
378. Number of islands II [P] | Pattern: DSU | Idea: Online add land; union with 4 neighbors, track component count (LC 305) | TC O(Q*alpha(N*M)) SC O(N*M)
379. Making a large island [P] | Pattern: DSU | Idea: DSU sizes of islands; for each 0 sum distinct neighbor component sizes +1 (LC 827) | TC O(N*M) SC O(N*M)
380. Most stones removed with same row or column [P] | Pattern: DSU | Idea: Union row with column nodes; answer is stones minus components (LC 947) | TC O(N*alpha) SC O(N)
### Additional Algorithms (id 2090)
Sub-pattern focus: Tarjan low-link: bridge if low[child] > tin[node]; articulation if low[child] >= tin[node] (root needs >1 child).
381. Kosaraju's algorithm [P] | Pattern: Bridges / SCC / articulation points | Idea: DFS finish-order stack, reverse graph, DFS in stack order; each DFS is one SCC | TC O(V+E) SC O(V+E)
382. Bridges in graph [P] | Pattern: Bridges / SCC / articulation points | Idea: DFS with tin/low; edge is bridge if low[child] > tin[node] (LC 1192) | TC O(V+E) SC O(V)
383. Articulation point in graph [P] | Pattern: Bridges / SCC / articulation points | Idea: Tarjan tin/low; low[child] >= tin[node] marks cut vertex; root needs 2+ children | TC O(V+E) SC O(V)
## Dynamic Programming (id 2010)
### 1D DP (id 2093)
Sub-pattern focus: Recipe: recursion, memoize, tabulate, space-optimize. State is the index; transition looks back 1-2 steps.
384. Climbing stairs | Pattern: DP 1D | Idea: dp[i]=dp[i-1]+dp[i-2]; keep two variables (LC 70) | TC O(N) SC O(1)
385. Frog Jump | Pattern: DP 1D | Idea: dp[i]=min(dp[i-1]+|h[i]-h[i-1]|, dp[i-2]+|h[i]-h[i-2]|) | TC O(N) SC O(1)
386. Frog jump with K distances | Pattern: DP 1D | Idea: dp[i]=min over j in 1..K of dp[i-j]+|h[i]-h[i-j]| | TC O(N*K) SC O(N)
387. Maximum sum of non adjacent elements | Pattern: DP 1D | Idea: dp[i]=max(dp[i-1], a[i]+dp[i-2]) | TC O(N) SC O(1)
388. House robber | Pattern: DP 1D | Idea: Non-adjacent max; circular variant: best of skipping first or last (LC 198/213) | TC O(N) SC O(1)
### 2D DP (id 2094)
389. Ninja's training | Pattern: DP with extra state (2D DP) | Idea: dp[day][last]=points[day][task]+max dp[day-1][other task] | TC O(N*4*3) SC O(4)
### DP on grids (id 2095)
Sub-pattern focus: State dp[i][j] = answer for the cell; transitions from up/left (or 3 cells above).
390. Grid unique paths | Pattern: Grid DP | Idea: dp[i][j]=dp[i-1][j]+dp[i][j-1]; or nCr(m+n-2,m-1) (LC 62) | TC O(M*N) SC O(N)
391. Unique paths II [P] | Pattern: Grid DP | Idea: Same recurrence, obstacle cell has 0 paths (LC 63) | TC O(M*N) SC O(N)
392. Minimum Falling Path Sum | Pattern: Grid DP | Idea: dp[i][j]=a[i][j]+min of three cells above (LC 931) | TC O(N^2) SC O(N)
393. Triangle | Pattern: Grid DP | Idea: Bottom-up dp[j]=t[i][j]+min(dp[j],dp[j+1]) (LC 120) | TC O(N^2) SC O(N)
394. Cherry pickup II [P] | Pattern: Grid DP | Idea: State (row,c1,c2) both robots move together; 9 transitions (LC 1463) | TC O(R*C*C*9) SC O(C*C)
395. Count Square Submatrices with All Ones | Pattern: Grid DP | Idea: dp[i][j]=1+min(up,left,diag) if 1; sum all dp (LC 1277) | TC O(N*M) SC O(N*M)
### DP on stocks (id 2096)
Sub-pattern focus: State (index, canBuy, transactions left); buy consumes a transaction slot in IV.
396. Best time to buy and sell stock | Pattern: DP on stocks | Idea: Track min price so far, best profit = price - min (LC 121) | TC O(N) SC O(1)
397. Best time to buy and sell stock II | Pattern: DP on stocks | Idea: Unlimited transactions: sum of all positive day-to-day differences (LC 122) | TC O(N) SC O(1)
398. Best time to buy and sell stock III [P] | Pattern: DP on stocks | Idea: dp[i][canBuy][cap<=2], or four running variables buy1,sell1,buy2,sell2 (LC 123) | TC O(N) SC O(1)
399. Best time to buy and sell stock IV [P] | Pattern: DP on stocks | Idea: dp[i][canBuy][k]; if k>=N/2 reduces to unlimited (LC 188) | TC O(N*K) SC O(K)
400. Best time to buy and sell stock with transaction fees | Pattern: DP on stocks | Idea: hold/free states; sell adds price minus fee (LC 714) | TC O(N) SC O(1)
401. Best Time to Buy and Sell Stock with Cooldown | Pattern: DP on stocks | Idea: After sell jump to i+2; states hold, sold, rest (LC 309) | TC O(N) SC O(1)
### DP on subsequences (id 2097)
Sub-pattern focus: pick/not-pick with dp[i][target]; counting uses sum, optimization uses min/max. Unbounded: stay on same index after take.
402. Subset sum equals to target | Pattern: Subsequence pick/not-pick | Idea: dp[i][t]=dp[i-1][t] OR dp[i-1][t-a[i]] | TC O(N*K) SC O(K)
403. Partition equal subset sum | Pattern: Knapsack 0/1 | Idea: Total must be even; subset sum to total/2 (LC 416) | TC O(N*S) SC O(S)
404. Partition a set into two subsets with minimum absolute sum difference [P] | Pattern: Knapsack 0/1 | Idea: Subset-sum table up to total; minimize |total-2*s| over reachable s | TC O(N*S) SC O(S)
405. Count subsets with sum K | Pattern: Subsequence pick/not-pick | Idea: dp[i][t]=dp[i-1][t]+dp[i-1][t-a[i]]; handle zeros | TC O(N*K) SC O(K)
406. Count partitions with given difference | Pattern: Knapsack 0/1 | Idea: s1=(total+D)/2 must be integer and >=0; count subsets with sum s1 | TC O(N*S) SC O(S)
407. 0 and 1 Knapsack | Pattern: Knapsack 0/1 | Idea: dp[i][w]=max(dp[i-1][w], val+dp[i-1][w-wt]); 1D loop w downward | TC O(N*W) SC O(W)
408. Minimum coins | Pattern: Unbounded knapsack | Idea: dp[t]=min(dp[t-c]+1); infinity means impossible (LC 322) | TC O(N*T) SC O(T)
409. Target sum | Pattern: Subsequence pick/not-pick | Idea: Assign +/-; reduces to count subsets with given difference (LC 494) | TC O(N*S) SC O(S)
410. Coin change II [P] | Pattern: Unbounded knapsack | Idea: Count combinations: outer loop coins, inner loop amounts ascending (LC 518) | TC O(N*T) SC O(T)
411. Unbounded knapsack | Pattern: Unbounded knapsack | Idea: dp[i][w]=max(skip, val+dp[i][w-wt]) staying on same item | TC O(N*W) SC O(W)
412. Rod cutting problem [P] | Pattern: Unbounded knapsack | Idea: Piece lengths 1..N reusable; dp[len]=max(price[i]+dp[len-i]) | TC O(N^2) SC O(N)
### LIS (id 2098)
Sub-pattern focus: dp[i]= best subsequence ending at i; sort first for divisible subset and string chain.
413. Longest Increasing Subsequence | Pattern: LIS | Idea: Tails array with binary search (lower_bound); length of tails (LC 300) | TC O(N log N) SC O(N)
414. Print Longest Increasing Subsequence [P] | Pattern: LIS | Idea: O(N^2) dp with prev[] pointers, backtrack from best index | TC O(N^2) SC O(N)
415. Largest Divisible Subset | Pattern: LIS | Idea: Sort; dp[i]=1+dp[j] when a[i]%a[j]==0; backtrack via prev (LC 368) | TC O(N^2) SC O(N)
416. Longest String Chain | Pattern: LIS | Idea: Sort by length; dp over words differing by one inserted char (LC 1048) | TC O(N*L^2) SC O(N)
417. Longest Bitonic Subsequence | Pattern: LIS | Idea: LIS ending at i plus LDS starting at i, minus 1; maximize | TC O(N^2) SC O(N)
418. Number of Longest Increasing Subsequences | Pattern: LIS | Idea: Track length[i] and count[i]; merge counts on equal best length (LC 673) | TC O(N^2) SC O(N)
### DP on strings (id 2099)
Sub-pattern focus: dp[i][j] over prefixes of two strings; match diagonal, else neighbors. Many problems reduce to LCS.
419. Longest common subsequence | Pattern: LCS / string DP | Idea: match: 1+dp[i-1][j-1], else max(dp[i-1][j],dp[i][j-1]) (LC 1143) | TC O(N*M) SC O(M)
420. Longest common substring | Pattern: LCS / string DP | Idea: match: 1+dp[i-1][j-1], else 0; answer is max cell | TC O(N*M) SC O(M)
421. Longest palindromic subsequence | Pattern: LCS / string DP | Idea: LCS of string and its reverse (LC 516) | TC O(N^2) SC O(N)
422. Minimum insertions to make string palindrome [P] | Pattern: LCS / string DP | Idea: N minus longest palindromic subsequence (LC 1312) | TC O(N^2) SC O(N)
423. Minimum insertions or deletions to convert string A to B | Pattern: LCS / string DP | Idea: Deletions = |A|-LCS, insertions = |B|-LCS | TC O(N*M) SC O(M)
424. Shortest common supersequence [P] | Pattern: LCS / string DP | Idea: Length N+M-LCS; build by walking LCS table, adding non-matching chars (LC 1092) | TC O(N*M) SC O(N*M)
425. Distinct subsequences [P] | Pattern: LCS / string DP | Idea: match: dp[i-1][j-1]+dp[i-1][j], else dp[i-1][j] (LC 115) | TC O(N*M) SC O(M)
426. Edit distance [P] | Pattern: LCS / string DP | Idea: match: dp[i-1][j-1], else 1+min(insert,delete,replace) (LC 72) | TC O(N*M) SC O(M)
427. Wildcard matching [P] | Pattern: LCS / string DP | Idea: '?' matches one; '*' = dp[i-1][j] or dp[i][j-1] (LC 44) | TC O(N*M) SC O(M)
428. Word Break | Pattern: LCS / string DP | Idea: dp[i]=true if some j<i has dp[j] and s[j..i) in dictionary (LC 139) | TC O(N^2 * L) SC O(N)
429. Count Palindromic Subsequences [P] | Pattern: LCS / string DP | Idea: Interval dp: s[i]==s[j] gives dp[i+1][j]+dp[i][j-1]+1, else minus overlap | TC O(N^2) SC O(N^2)
### MCM DP (id 2100)
Sub-pattern focus: dp[i][j] over interval, try every split k; "last operation" thinking (last balloon burst, last cut).
430. Matrix chain multiplication [P] | Pattern: Partition DP (MCM) | Idea: dp[i][j]=min over k of dp[i][k]+dp[k+1][j]+a[i-1]*a[k]*a[j] | TC O(N^3) SC O(N^2)
431. Burst balloons [P] | Pattern: Partition DP (MCM) | Idea: k is the LAST balloon burst in (i,j); pad array with 1s (LC 312) | TC O(N^3) SC O(N^2)
432. Palindrome partitioning II [P] | Pattern: Partition DP (MCM) | Idea: dp[i]=min cuts for suffix/prefix using palindrome check; front partition (LC 132) | TC O(N^2) SC O(N)
433. Partition Array for Maximum Sum [P] | Pattern: Partition DP (MCM) | Idea: dp[i]=max over block length j<=K of j*blockMax+dp[i-j] (LC 1043) | TC O(N*K) SC O(N)
434. Minimum cost to cut the stick [P] | Pattern: Partition DP (MCM) | Idea: Sort cuts, add 0 and n; dp[i][j]=min over k of cost+dp[i][k]+dp[k][j] (LC 1547) | TC O(C^3) SC O(C^2)
435. Different Ways to Evaluate a Boolean Expression [P] | Pattern: Partition DP (MCM) | Idea: dp[i][j][isTrue] split at operators combining left/right counts (mod) | TC O(N^3) SC O(N^2)
## Tries (id 2011)
### Theory (id 2102)
Sub-pattern focus: Node = array of 26 children + end flag (optionally prefix count).
436. Trie Implementation and Operations | Pattern: Trie | Idea: insert, search, startsWith by walking child links per char (LC 208) | TC O(L) per op SC O(total chars*26)
437. Trie Implementation and Advanced Operations | Pattern: Trie | Idea: Keep prefix count and end count per node; support erase and count queries | TC O(L) per op SC O(total chars*26)
### Problems (id 2103)
438. Longest Word with All Prefixes | Pattern: Trie | Idea: Insert all words; DFS only through end-flag nodes; take longest, lexicographically smallest | TC O(total chars) SC O(total chars)
439. Number of distinct substrings in a string [P] | Pattern: Trie | Idea: Insert every suffix into trie; count new nodes created (+1 for empty) | TC O(N^2) SC O(N^2)
440. Maximum XOR of two numbers in an array | Pattern: Trie | Idea: Binary trie of bits; for each number greedily take opposite bit (LC 421) | TC O(32*N) SC O(32*N)
441. Maximum Xor with an element from an array [P] | Pattern: Trie | Idea: Sort queries by limit; insert numbers <= limit offline, then query XOR (LC 1707) | TC O((N+Q)*32 + sorting) SC O(32*N)
## Strings (Advanced Algo) (id 2012)
### Medium Problems (id 2104)
442. Reverse every word in a string | Pattern: String manipulation | Idea: Split on spaces ignoring extras, reverse word order, join with single space (LC 151) | TC O(N) SC O(N)
443. Minimum number of bracket reversals to make an expression balanced | Pattern: String manipulation | Idea: Stack cancel matched; leftover a '}' and b '{' gives ceil(a/2)+ceil(b/2); odd length is -1 | TC O(N) SC O(1)
444. Count and say | Pattern: String manipulation | Idea: Iteratively run-length encode previous term N-1 times (LC 38) | TC O(N * term length) SC O(term length)
### Advanced Problems (Less asked) (id 2105)
Sub-pattern focus: LPS/Z both precompute prefix matches; concatenate pattern+'#'+text to search.
445. Rabin Karp Algorithm [P] | Pattern: KMP / Z / rolling hash | Idea: Rolling polynomial hash of window; compare hashes then verify on match | TC O(N+M) avg, O(N*M) worst SC O(1)
446. Z function [P] | Pattern: KMP / Z / rolling hash | Idea: Maintain [l,r] box, reuse earlier z values, extend by comparison | TC O(N) SC O(N)
447. KMP Algorithm or LPS array [P] | Pattern: KMP / Z / rolling hash | Idea: LPS = longest proper prefix that is also suffix; on mismatch fall back via LPS | TC O(N+M) SC O(M)
448. Shortest Palindrome [P] | Pattern: KMP / Z / rolling hash | Idea: LPS of s+'#'+reverse(s); prepend reverse of remaining suffix (LC 214) | TC O(N) SC O(N)
449. Longest happy prefix [P] | Pattern: KMP / Z / rolling hash | Idea: Last value of LPS array is the answer length (LC 1392) | TC O(N) SC O(N)
## Maths (id 2013)
### Sieve of Eratosthenes (id 2107)
Sub-pattern focus: Sieve marks multiples starting at i*i for i up to sqrt(N); SPF sieve factorizes queries fast.
450. Print all primes till N | Pattern: Number theory (Sieve) | Idea: Sieve of Eratosthenes boolean array, mark multiples from i*i | TC O(N log log N) SC O(N)
451. Prime factorisation of a Number | Pattern: Number theory (Sieve) | Idea: Smallest-prime-factor sieve then divide repeatedly; single number: trial division to sqrt | TC O(log N) per query SC O(N)
452. Count primes in range L to R [P] | Pattern: Number theory (Sieve) | Idea: Segmented sieve using primes up to sqrt(R); mark multiples within [L,R] | TC O((R-L) log log R + sqrt(R)) SC O(R-L+sqrt(R))
