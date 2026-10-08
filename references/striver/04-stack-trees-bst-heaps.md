# Striver A2Z: Stack/Queues, Binary Trees, BST, Heaps

## Pattern Playbook

| Pattern | Use when (clue) | Template/steps | Problems |
|---|---|---|---|
| Array/LL implementation of stack/queue | "implement X using Y", design a data structure | Keep top/front/rear pointers or head node; guard overflow/underflow; O(1) ops | 247-252 |
| Stack via queues / queue via stacks | Implement one structure using the other | Queue-as-stack: rotate after push. Stack-as-queue: in/out stacks, move lazily | 249, 250 |
| Stack bracket matching | Parentheses/nesting validity | Push openers; on closer pop and compare; stack empty at end | 253 |
| Stack for expression conversion | infix/prefix/postfix | Operand stack or operator stack with precedence; pop while top precedence >= current | 254-259 |
| Monotonic stack next greater/smaller | "next/previous greater/smaller element", span, collision-like cancel | Scan, pop while top violates order, answer = top (or none), push; circular: loop 2n | 260, 261, 262, 265, 266, 272, 276 |
| Monotonic stack contribution count | Sum over all subarrays of min/max | Find prev/next smaller (and greater) per index; contribution = a[i]*left*right | 263, 264 |
| Monotonic stack histogram | Largest rectangle, area with bars | Stack of increasing heights; on pop width = i - newTop - 1 | 270, 271 |
| Two-pointer / prefix-max trapping | Water between bars | Two pointers with leftMax/rightMax, move smaller side | 269 |
| Monotonic deque sliding window | Max/min of every window of size k | Deque of indices, decreasing values; drop out-of-window front | 268 |
| Stack with aux info | Get min/state in O(1) | Store (value, min so far) or encoded value per push | 267 |
| Hashmap + doubly linked list design | LRU/LFU, O(1) get/put with eviction | Map key->node; DLL by recency (LFU: freq buckets + minFreq) | 274, 275 |
| Candidate elimination (two pointers) | Find the one who satisfies a pairwise rule | Compare two candidates, discard one each step, verify survivor | 273 |
| Tree DFS traversal | Inorder/preorder/postorder visit | Recursion or explicit stack; one-stack/two-stack iterative variants | 277-279, 281 |
| Level-order BFS | Level by level, width, views, zigzag | Queue; process level size per round; per-level logic | 280, 289, 292-294, 297 |
| Tree DFS return-value (height/diameter) | Depth, balance, diameter, path sum, same/mirror | Recurse children, combine returned value, update global answer | 282-288, 300 |
| Boundary/vertical coordinate traversal | Views, boundary, vertical order | Left boundary + leaves + right boundary; or BFS with (row, col) map | 290, 291, 292, 293 |
| Root-to-leaf path | Print/track a path, ancestors | DFS with path list, backtrack on return | 295 |
| LCA | Lowest common ancestor | DFS: return node if equals p/q; both sides non-null -> current is LCA | 296, 315 |
| Parent map + BFS from node | Nodes at distance K, burn time | Map child->parent, BFS outward in 3 directions with visited | 298, 299 |
| Tree rewiring in place | Flatten, convert structure | Reverse preorder with prev pointer, or Morris-like right-threading | 301 |
| Construct tree from traversals | Build tree from two orders | Inorder map for index; preorder/postorder root picks; recurse on ranges | 302-304, 316 |
| Tree serialization | Encode/decode a tree | Level-order with null markers (or preorder with markers) | 305 |
| Morris traversal | O(1) extra space traversal | Thread inorder predecessor to current, remove thread on second visit | 306, 307 |
| BST search/navigation | Use BST ordering to go left/right | Compare key, descend one side; track candidate for floor/ceil/successor | 308-311, 317 |
| BST insert/delete | Modify BST | Insert at null leaf; delete: 0/1 child splice, 2 children use inorder successor | 311, 312 |
| BST bounds/inorder | Validate BST, kth element, order-based tasks | Pass (low, high) bounds, or inorder gives sorted order | 313, 314, 320, 321 |
| BST iterator / two-sum on BST | Controlled inorder, pair sum | Stack holds left spine; forward + reverse iterators for two pointers | 318, 319 |
| Heap implementation/heapify | Build or maintain heap in array | Sift down from n/2-1 to 0 (O(n)); push sift-up, pop sift-down | 322-328 |
| Heap top-K | K-th largest/most frequent, running K-th | Size-k min-heap, evict smallest; or quickselect | 329, 330, 339 |
| K-way merge | Merge K sorted lists/arrays | Min-heap of (value, list idx, pos); pop smallest, push next | 331, 337 |
| Greedy with heap | Always take the best/cheapest next item | Pop min/max, process, push result back | 333, 336 |
| Heap/map grouping greedy | Consecutive groups, ranking | Sort keys then take from smallest; or sort + rank map | 332, 334 |
| Two heaps | Running median | Max-heap lower half, min-heap upper half, sizes differ by <= 1 | 338 |
| Design with heap | Feed/merge of K streams | Per-user lists + heap merge of latest tweets | 335 |

## Stack / Queues (id 2005)
### Implementation (id 2066)
247. Implement Stack using Arrays | Pattern: Array/LL implementation of stack/queue | Idea: Array plus top index; push/pop/peek move top, check overflow and underflow | TC O(1) per op SC O(n)
248. Implement Queue using Arrays | Pattern: Array/LL implementation of stack/queue | Idea: Circular array with front, rear, size counters to reuse slots | TC O(1) per op SC O(n)
249. Implement Stack using Queue | Pattern: Stack via queues / queue via stacks | Idea: Single queue: after push, rotate previous n-1 elements behind new one | TC push O(n), pop O(1) SC O(n)
250. Implement Queue using Stack | Pattern: Stack via queues / queue via stacks | Idea: Input and output stacks; refill output only when empty, amortized O(1) | TC amortized O(1) SC O(n)
251. Implement stack using Linkedlist | Pattern: Array/LL implementation of stack/queue | Idea: Push and pop at head node; no capacity limit | TC O(1) per op SC O(n)
252. Implement queue using Linkedlist | Pattern: Array/LL implementation of stack/queue | Idea: Keep head and tail pointers; enqueue at tail, dequeue at head | TC O(1) per op SC O(n)
253. Balanced Paranthesis | Pattern: Stack bracket matching | Idea: Push openers; closer must match popped top; stack empty at end (LC 20) | TC O(n) SC O(n)
### Prefix, Infix and Postfix Conversions (id 17181)
Sub-pattern focus: operator stack with precedence (^ right-associative); postfix/prefix to anything uses an operand stack of strings.
254. Infix to Postfix Conversion | Pattern: Stack for expression conversion | Idea: Operator stack; pop while top precedence >= current (strictly > for ^); parens group | TC O(n) SC O(n)
255. Infix to Prefix Conversion | Pattern: Stack for expression conversion | Idea: Reverse infix, swap parens, convert to postfix (pop on strictly >), reverse result | TC O(n) SC O(n)
256. Prefix to Infix Conversion | Pattern: Stack for expression conversion | Idea: Scan right to left; operand stack; operator pops two: "(a op b)" | TC O(n) SC O(n)
257. Prefix to Postfix Conversion | Pattern: Stack for expression conversion | Idea: Scan right to left; operator pops a,b and pushes a+b+op | TC O(n) SC O(n)
258. Postfix to Infix Conversion | Pattern: Stack for expression conversion | Idea: Scan left to right; operator pops b then a, pushes "(a op b)" | TC O(n) SC O(n)
259. Postfix to Prefix Conversion | Pattern: Stack for expression conversion | Idea: Scan left to right; operator pops b then a, pushes op+a+b | TC O(n) SC O(n)
### Monotonic Stack (id 2067)
Sub-pattern focus: decide scan direction and whether stack is increasing or decreasing; equal-element handling decides strict vs non-strict pops.
260. Next Greater Element | Pattern: Monotonic stack next greater/smaller | Idea: Scan right to left, pop smaller-or-equal, top is answer; map for nums1 (LC 496) | TC O(n) SC O(n)
261. Next Greater Element - 2 | Pattern: Monotonic stack next greater/smaller | Idea: Circular array: iterate 2n-1 down to 0 using index mod n (LC 503) | TC O(n) SC O(n)
262. Asteroid Collision | Pattern: Monotonic stack next greater/smaller | Idea: Stack of survivors; right-mover vs incoming left-mover compare sizes, pop smaller (LC 735) | TC O(n) SC O(n)
263. Sum of Subarray Minimums | Pattern: Monotonic stack contribution count | Idea: Previous-smaller and next-smaller-or-equal give span; add a[i]*left*right (LC 907) | TC O(n) SC O(n)
264. Sum of Subarray Ranges | Pattern: Monotonic stack contribution count | Idea: Sum of subarray maxes minus sum of subarray mins, each via contribution (LC 2104) | TC O(n) SC O(n)
265. Remove K Digits | Pattern: Monotonic stack next greater/smaller | Idea: Greedy increasing stack; pop larger top while k>0; trim leftover and leading zeros (LC 402) | TC O(n) SC O(n)
266. Next Smaller Element | Pattern: Monotonic stack next greater/smaller | Idea: Scan right to left, pop greater-or-equal, top is next smaller | TC O(n) SC O(n)
### FAQs (id 2068)
Sub-pattern focus: histogram stack feeds Maximum Rectangles; LRU/LFU are hashmap + linked-list designs.
267. Implement Min Stack | Pattern: Stack with aux info | Idea: Push (value, current min) pairs, or encode min in a single stack (LC 155) | TC O(1) per op SC O(n)
268. Sliding Window Maximum [P] | Pattern: Monotonic deque sliding window | Idea: Deque of indices with decreasing values; pop front when out of window (LC 239) | TC O(n) SC O(k)
269. Trapping Rainwater [P] | Pattern: Two-pointer / prefix-max trapping | Idea: Two pointers; move side with smaller max, add max minus height (LC 42) | TC O(n) SC O(1)
270. Largest rectangle in a histogram [P] | Pattern: Monotonic stack histogram | Idea: Increasing stack; on pop width uses new top and i; track max area (LC 84) | TC O(n) SC O(n)
271. Maximum Rectangles [P] | Pattern: Monotonic stack histogram | Idea: Per row build histogram heights, apply largest-rectangle each row (LC 85) | TC O(R*C) SC O(C)
272. Stock span problem | Pattern: Monotonic stack next greater/smaller | Idea: Stack of (price, span); pop prices <= current and add their spans (LC 901) | TC O(n) amortized SC O(n)
273. Celebrity Problem | Pattern: Candidate elimination (two pointers) | Idea: Two pointers: if A knows B, A not celebrity else B not; verify candidate | TC O(n) SC O(1)
274. LRU Cache [P] | Pattern: Hashmap + doubly linked list design | Idea: Map key->node; DLL moves used node to front, evict tail (LC 146) | TC O(1) per op SC O(capacity)
275. LFU Cache [P] | Pattern: Hashmap + doubly linked list design | Idea: Map key->node plus freq->DLL buckets and minFreq; evict LRU in min bucket (LC 460) | TC O(1) per op SC O(capacity)
276. Number of Greater Elements to the Right | Pattern: Monotonic stack next greater/smaller | Idea: Count of greater elements per index (queries variant); offline BIT/merge sort, not plain stack | TC O(n log n) SC O(n)
## Binary Trees (id 2006)
### Theory/Traversals (id 2070)
Sub-pattern focus: recursive is O(h) stack; Morris (306-307) is the O(1) space version.
277. Inorder Traversal [B] | Pattern: Tree DFS traversal | Idea: Iterative: push left spine, pop, visit, go right (LC 94) | TC O(n) SC O(h)
278. Preorder Traversal [B] | Pattern: Tree DFS traversal | Idea: Stack: pop, visit, push right then left (LC 144) | TC O(n) SC O(h)
279. Postorder Traversal [B] | Pattern: Tree DFS traversal | Idea: Two stacks (reverse of root-right-left) or one stack with last-visited pointer (LC 145) | TC O(n) SC O(h)
280. Level Order Traversal | Pattern: Level-order BFS | Idea: Queue; process queue size nodes per level (LC 102) | TC O(n) SC O(n)
281. Pre, Post, Inorder in one traversal | Pattern: Tree DFS traversal | Idea: Stack of (node, state 1/2/3); state decides preorder, inorder or postorder add | TC O(n) SC O(n)
### Medium Problems (id 2071)
Sub-pattern focus: most are post-order recursion returning a value (height) while updating a global answer.
282. Maximum Depth in BT | Pattern: Tree DFS return-value (height/diameter) | Idea: 1 + max(left, right) height recursion, or count BFS levels (LC 104) | TC O(n) SC O(h)
283. Check if two trees are identical or not | Pattern: Tree DFS return-value (height/diameter) | Idea: Recurse on both: values equal and left/right subtrees identical (LC 100) | TC O(n) SC O(h)
284. Check for balanced binary tree | Pattern: Tree DFS return-value (height/diameter) | Idea: Return height or -1 if unbalanced; avoids repeated height calls (LC 110) | TC O(n) SC O(h)
285. Diameter of Binary Tree | Pattern: Tree DFS return-value (height/diameter) | Idea: At each node update best = leftH + rightH; return height (LC 543) | TC O(n) SC O(h)
286. Maximum path sum [P] | Pattern: Tree DFS return-value (height/diameter) | Idea: Return max(0,gain) of child sides; update best with node + both gains (LC 124) | TC O(n) SC O(h)
287. Check for symmetrical BTs | Pattern: Tree DFS return-value (height/diameter) | Idea: Mirror compare: left.left with right.right and left.right with right.left (LC 101) | TC O(n) SC O(h)
288. Children Sum Property in Binary Tree | Pattern: Tree DFS return-value (height/diameter) | Idea: Going down push parent value to children; on return set node = sum of children | TC O(n) SC O(h)
### FAQs (id 2072)
Sub-pattern focus: views use BFS or DFS with depth/column; 298 and 299 need a child->parent map.
289. Zig Zag or Spiral Traversal | Pattern: Level-order BFS | Idea: Level order with a direction flag; reverse level on alternate levels (LC 103) | TC O(n) SC O(n)
290. Boundary Traversal | Pattern: Boundary/vertical coordinate traversal | Idea: Left boundary (no leaf), all leaves, right boundary reversed (no leaf) | TC O(n) SC O(h)
291. Vertical Order Traversal [P] | Pattern: Boundary/vertical coordinate traversal | Idea: BFS/DFS with (row, col); sort by col, then row, then value (LC 987) | TC O(n log n) SC O(n)
292. Top View of BT | Pattern: Boundary/vertical coordinate traversal | Idea: BFS with column index; first node seen per column wins | TC O(n) SC O(n)
293. Bottom view of BT | Pattern: Boundary/vertical coordinate traversal | Idea: BFS with column index; last node seen per column overwrites | TC O(n) SC O(n)
294. Right/Left View of BT | Pattern: Level-order BFS | Idea: Last (right) or first (left) node of each level; or DFS by depth (LC 199) | TC O(n) SC O(h)
295. Print root to leaf path in BT | Pattern: Root-to-leaf path | Idea: DFS with path list; record at leaf, backtrack pop (LC 257 is path strings) | TC O(n) SC O(h)
296. LCA in BT [P] | Pattern: LCA | Idea: Return node if null or equals p/q; both sides found means current is LCA (LC 236) | TC O(n) SC O(h)
297. Maximum Width of BT [P] | Pattern: Level-order BFS | Idea: Index nodes 2i+1, 2i+2 (normalize by level min); width = last - first + 1 (LC 662) | TC O(n) SC O(n)
298. Print all nodes at a distance of K in BT [P] | Pattern: Parent map + BFS from node | Idea: Build parent map; BFS from target over left, right, parent for K levels (LC 863) | TC O(n) SC O(n)
299. Minimum time taken to burn the BT from a given Node [P] | Pattern: Parent map + BFS from node | Idea: Parent map; BFS from start node with visited; answer = number of levels | TC O(n) SC O(n)
300. Count total nodes in a complete BT | Pattern: Tree DFS return-value (height/diameter) | Idea: Compare leftmost and rightmost heights; equal gives 2^h-1 else recurse (LC 222) | TC O(log^2 n) SC O(log n)
301. Flatten Binary Tree to Linked List [P] | Pattern: Tree rewiring in place | Idea: Reverse preorder with prev pointer, or Morris-style rewiring for O(1) space (LC 114) | TC O(n) SC O(h)
### Construction Problems (id 2073)
302. Requirements needed to construct a unique BT | Pattern: Construct tree from traversals | Idea: Inorder plus either preorder or postorder is unique; preorder+postorder is not | TC O(1) concept SC O(1)
303. Construct a BT from Preorder and Inorder | Pattern: Construct tree from traversals | Idea: Preorder gives root; inorder index map splits left/right sizes (LC 105) | TC O(n) SC O(n)
304. Construct a BT from Postorder and Inorder | Pattern: Construct tree from traversals | Idea: Postorder last is root; inorder map splits subtrees; build right first (LC 106) | TC O(n) SC O(n)
305. Serialize and De-serialize BT [P] | Pattern: Tree serialization | Idea: Level-order with "#" for null; rebuild with a queue (LC 297) | TC O(n) SC O(n)
### Traversal in Constant Space (id 2074)
Sub-pattern focus: Morris threads inorder predecessor's right pointer to current; always restore the tree.
306. Morris Inorder Traversal [P] | Pattern: Morris traversal | Idea: Find predecessor; no thread: create and go left; thread exists: remove, visit, go right | TC O(n) SC O(1)
307. Morris Preorder Traversal [P] | Pattern: Morris traversal | Idea: Same threading as inorder but visit node when thread is created | TC O(n) SC O(1)
## Binary Search Trees (id 2007)
### Theory and Basics (id 2076)
308. Search in BST [B] | Pattern: BST search/navigation | Idea: Go left if key smaller, right if larger, until match or null (LC 700) | TC O(h) SC O(1)
309. Floor and Ceil in a BST | Pattern: BST search/navigation | Idea: Descend; when node fits as candidate record it, then go closer side | TC O(h) SC O(1)
310. Minimum and Maximum in BST | Pattern: BST search/navigation | Idea: Min is leftmost node, max is rightmost node | TC O(h) SC O(1)
### Medium (id 2077)
Sub-pattern focus: inorder of a BST is sorted; use bounds or inorder for validation and kth queries.
311. Insert a given node in BST | Pattern: BST insert/delete | Idea: Descend by value to null spot and attach new node (LC 701) | TC O(h) SC O(1)
312. Delete a node in BST | Pattern: BST insert/delete | Idea: 0 or 1 child: splice; 2 children: replace with inorder successor, delete it (LC 450) | TC O(h) SC O(h)
313. Kth Smallest and Largest element in BST | Pattern: BST bounds/inorder | Idea: Inorder counts to k (kth largest: reverse inorder or n-k+1); Morris for O(1) space (LC 230) | TC O(h+k) SC O(h)
314. Check if a tree is a BST or not | Pattern: BST bounds/inorder | Idea: Recurse with (low, high) bounds, strict inequalities (LC 98) | TC O(n) SC O(h)
315. LCA in BST | Pattern: LCA | Idea: If both keys smaller go left, both larger go right, else current is LCA (LC 235) | TC O(h) SC O(1)
316. Construct a BST from a preorder traversal | Pattern: Construct tree from traversals | Idea: Recurse with upper bound, consume preorder index while value < bound (LC 1008) | TC O(n) SC O(h)
317. Inorder successor and predecessor in BST | Pattern: BST search/navigation | Idea: Descend from root; going left records successor, going right records predecessor | TC O(h) SC O(1)
### FAQs (id 2078)
318. BST iterator | Pattern: BST iterator / two-sum on BST | Idea: Stack of left spine; next pops and pushes left spine of right child (LC 173) | TC O(1) amortized next SC O(h)
319. Two sum in BST | Pattern: BST iterator / two-sum on BST | Idea: Two iterators (forward inorder, reverse inorder) as two pointers (LC 653) | TC O(n) SC O(h)
320. Correct BST with two nodes swapped [P] | Pattern: BST bounds/inorder | Idea: Inorder: find first and second order violations; swap their values (LC 99) | TC O(n) SC O(h)
321. Largest BST in Binary Tree [P] | Pattern: BST bounds/inorder | Idea: Post-order return (min, max, size, isBST); combine children (LC 333 is premium) | TC O(n) SC O(h)
## Heaps (id 2008)
### Theory and Implementation (id 2080)
Sub-pattern focus: array heap with children 2i+1, 2i+2; build-heap is O(n), not O(n log n).
322. Heapify Algorithm | Pattern: Heap implementation/heapify | Idea: Sift-down: swap with larger (max-heap) child until property holds | TC O(log n) SC O(1)
323. Build heap from a given Array | Pattern: Heap implementation/heapify | Idea: Heapify from index n/2-1 down to 0 | TC O(n) SC O(1)
324. Implement Min Heap | Pattern: Heap implementation/heapify | Idea: Push: append and sift-up; pop: move last to root and sift-down | TC O(log n) per op SC O(n)
325. Implement Max Heap | Pattern: Heap implementation/heapify | Idea: Same as min heap with reversed comparisons | TC O(log n) per op SC O(n)
326. Check if an array represents a min heap | Pattern: Heap implementation/heapify | Idea: For each i up to n/2-1, check a[i] <= both children | TC O(n) SC O(1)
327. Convert Min Heap to Max Heap | Pattern: Heap implementation/heapify | Idea: Treat array as arbitrary and run build max-heap heapify | TC O(n) SC O(1)
328. Heap Sort [P] | Pattern: Heap implementation/heapify | Idea: Build max-heap, repeatedly swap root to end and sift-down shrunk heap | TC O(n log n) SC O(1)
329. K-th Largest element in an array [P] | Pattern: Heap top-K | Idea: Min-heap of size k, top is answer; quickselect gives avg O(n) (LC 215) | TC O(n log k) SC O(k)
### FAQs (id 2081)
330. Kth largest element in a stream of running integers [P] | Pattern: Heap top-K | Idea: Maintain min-heap of size k; add, pop if larger than k; top is answer (LC 703) | TC O(log k) per add SC O(k)
331. Merge K sorted Lists [P] | Pattern: K-way merge | Idea: Min-heap of list heads; pop smallest, push its next (LC 23) | TC O(N log k) SC O(k)
332. Replace Elements by Their Rank | Pattern: Heap/map grouping greedy | Idea: Sort copy, map distinct values to rank 1.., replace (LC 1331 is similar) | TC O(n log n) SC O(n)
333. Task Scheduler | Pattern: Greedy with heap | Idea: Count frequencies; formula (maxFreq-1)*(n+1)+countMax, or max-heap with cooldown queue (LC 621) | TC O(n) SC O(1)
334. Hand of Straights | Pattern: Heap/map grouping greedy | Idea: Count map; repeatedly start group at smallest card, need consecutive W (LC 846) | TC O(n log n) SC O(n)
335. Design Twitter | Pattern: Design with heap | Idea: Per-user tweet lists with timestamps; news feed merges followees' latest 10 via heap (LC 355) | TC O(F log F) feed SC O(n)
336. Minimum Cost to Connect Sticks | Pattern: Greedy with heap | Idea: Min-heap; repeatedly merge two smallest, add cost, push sum (Huffman style) (LC 1167 premium) | TC O(n log n) SC O(n)
337. Maximum Sum Combination | Pattern: K-way merge | Idea: Sort both arrays desc; max-heap of index pairs with visited set; pop K times | TC O(K log K) SC O(K)
338. Find Median from Data Stream [P] | Pattern: Two heaps | Idea: Max-heap low half, min-heap high half; rebalance sizes; median from tops (LC 295) | TC O(log n) add, O(1) median SC O(n)
339. Top K Frequent Elements | Pattern: Heap top-K | Idea: Frequency map; min-heap of size k over counts, or bucket sort by frequency (LC 347) | TC O(n log k) SC O(n)
