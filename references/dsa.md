# DSA Reference -- Data Structures and Algorithms

## Core Data Structures

### Arrays and Strings
- Most common interview structure. Know two-pointer, sliding window, prefix sum.
- Prefix sum: precompute cumulative sums to answer range queries in O(1)
- Kadane's algorithm: maximum subarray sum in O(n)

### Linked Lists
- Singly vs Doubly vs Circular
- Key operations: reverse, detect cycle (Floyd's), find middle (slow/fast pointer), merge two sorted lists
- Dummy node trick avoids edge cases for head deletion

### Stacks and Queues
- Stack: LIFO. Use for: balanced parentheses, next greater element, infix to postfix, undo operations
- Queue: FIFO. Use for: BFS, sliding window maximum (deque), task scheduling
- Monotonic stack: maintains increasing or decreasing order, useful for span/histogram problems

### Trees
- Binary Tree vs BST vs AVL vs Red-Black Tree
- BST property: left < root < right. Inorder traversal of BST gives sorted array.
- Tree traversals: Inorder (LNR), Preorder (NLR), Postorder (LRN), Level Order (BFS)
- Height of tree: max depth from root to leaf
- Balanced tree: |height(left) minus height(right)| <= 1 for all nodes

### Heaps
- Max-Heap: parent >= children. Min-Heap: parent <= children.
- Used for: top-K elements, merge K sorted lists, median in a stream
- Heapify: O(n). Insert/Delete: O(log n). Peek: O(1)
- Python: heapq is a min-heap. Negate values for max-heap.

### Hash Maps and Hash Sets
- Average O(1) for get, put, delete
- Collision resolution: chaining (linked list), open addressing (linear probing)
- Use for: frequency counting, two-sum, anagram detection, caching

### Graphs
- Representations: Adjacency Matrix (O(V^2) space), Adjacency List (O(V+E) space)
- BFS: level-by-level, uses a queue, shortest path in unweighted graphs
- DFS: depth-first, uses a stack or recursion, detects cycles, topological sort
- Topological Sort: for DAGs, ordering of tasks with dependencies (Kahn's or DFS)
- Dijkstra: shortest path in weighted graphs with non-negative weights, O((V+E) log V)
- Bellman-Ford: handles negative weights, O(VE)
- Union-Find: detect cycles, Kruskal's MST
- Kruskal vs Prim: both for MST. Kruskal sorts edges, Prim grows from a node.

### Tries
- Prefix tree for strings. Insert and search in O(L) where L is word length
- Used for: autocomplete, word search, prefix matching

---

## Algorithm Patterns

### Sliding Window
Use when: subarray/substring problems with a size or condition constraint
Template:
```python
left = 0
for right in range(len(arr)):
    # expand window: add arr[right]
    while window_condition_violated:
        # shrink window: remove arr[left]
        left += 1
    # update answer
```

### Binary Search
Use when: sorted array or a search space with a monotonic property
```python
lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return -1
```
Binary search on answer: "find minimum X such that condition(X) is True"

### Dynamic Programming
Two signals: optimal substructure + overlapping subproblems
Steps:
1. Define dp[i] clearly in words
2. Write the recurrence relation
3. Identify base cases
4. Decide top-down (memoization) or bottom-up (tabulation)

Classic DP problems:
- Fibonacci, Climbing Stairs (1D DP)
- Longest Common Subsequence (2D DP)
- 0/1 Knapsack (2D DP)
- Coin Change (1D DP, unbounded)
- Longest Increasing Subsequence (O(n^2) DP or O(n log n) with patience sorting)
- Edit Distance (2D DP)

### Backtracking
Use when: generating all combinations, permutations, or valid configurations
```python
def backtrack(state):
    if is_complete(state):
        results.append(state[:])
        return
    for choice in get_choices(state):
        make_choice(state, choice)
        backtrack(state)
        undo_choice(state, choice)
```

### Greedy
Use when: locally optimal choices lead to globally optimal solution
Examples: Activity Selection, Huffman Coding, Minimum number of platforms

---

## Top 50 Must-Solve Problems

**Arrays**
1. Two Sum
2. Best Time to Buy and Sell Stock
3. Maximum Subarray (Kadane's)
4. Product of Array Except Self
5. Container With Most Water
6. Merge Intervals
7. Find the Duplicate Number
8. Trapping Rain Water

**Binary Search**
9. Search in Rotated Sorted Array
10. Find Minimum in Rotated Sorted Array
11. Koko Eating Bananas (binary search on answer)

**Linked Lists**
12. Reverse a Linked List
13. Detect Cycle in Linked List
14. Merge Two Sorted Lists
15. Find Middle of Linked List
16. LRU Cache

**Trees**
17. Inorder, Preorder, Postorder Traversal
18. Maximum Depth of Binary Tree
19. Validate BST
20. Lowest Common Ancestor
21. Diameter of Binary Tree
22. Level Order Traversal
23. Serialize and Deserialize Binary Tree

**Graphs**
24. Number of Islands (BFS/DFS)
25. Clone Graph
26. Course Schedule (Topological Sort)
27. Word Ladder
28. Dijkstra Shortest Path
29. Detect Cycle in Directed and Undirected Graph

**DP**
30. Climbing Stairs
31. House Robber
32. Longest Common Subsequence
33. 0/1 Knapsack
34. Coin Change
35. Longest Increasing Subsequence
36. Edit Distance
37. Partition Equal Subset Sum
38. Word Break

**Heaps and Priority Queues**
39. Kth Largest Element in an Array
40. Top K Frequent Elements
41. Merge K Sorted Lists
42. Median from Data Stream

**Strings**
43. Valid Anagram
44. Longest Substring Without Repeating Characters
45. Longest Palindromic Substring
46. Group Anagrams
47. Minimum Window Substring

**Backtracking**
48. Subsets
49. Permutations
50. N-Queens

---

## Complexity Cheat Sheet

| Algorithm | Best | Average | Worst | Space |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n^2) | O(n^2) | O(1) |
| Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n^2) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| BFS / DFS | O(V+E) | O(V+E) | O(V+E) | O(V) |
| Dijkstra | O(E) | O((V+E) log V) | O((V+E) log V) | O(V) |


---

## Pattern Recognition Cheat Sheet

For a step-wise full roadmap see references/striver-a2z.md

| Problem clue | Technique | Typical complexity |
|---|---|---|
| Sorted array / search space | Binary search | O(log n) |
| Pair/triplet with target in sorted array | Two pointers | O(n) / O(n^2) |
| Subarray/substring with size or condition | Sliding window | O(n) |
| Subarray with sum K (negatives allowed) | Prefix sum + hashmap | O(n) |
| Cycle in list, middle of list | Fast/slow pointers | O(n), O(1) space |
| k-th largest / top K / stream median | Heap | O(n log k) |
| Next greater/smaller, histogram | Monotonic stack | O(n) |
| Shortest path, unweighted | BFS | O(V+E) |
| Shortest path, weighted non-negative | Dijkstra | O((V+E) log V) |
| Dependencies / ordering of tasks | Topological sort | O(V+E) |
| Connected components, dynamic connectivity | Union-Find / DFS | ~O(alpha(n)) per op |
| All combinations / permutations / subsets | Backtracking | O(2^n) / O(n!) |
| Minimum/maximum/count with choices, overlapping subproblems | Dynamic programming | O(n*m) typical |
| Locally best choice is provably safe | Greedy (often sort first) | O(n log n) |
| "Minimum X such that feasible" | Binary search on answer | O(n log range) |
| Overlapping ranges | Sort by start + merge | O(n log n) |
| Array of 1..n, find missing/duplicate | Cyclic sort / XOR | O(n), O(1) space |
| Prefix matching, dictionary of words | Trie | O(L) per op |
| Range query with updates | Segment tree / Fenwick | O(log n) |
| Substring search | KMP / Z / Rabin-Karp | O(n+m) |

---

## Missing Patterns

### Two Pointers
Sorted array pair sum; also partitioning and removing duplicates in place.
```python
l, r = 0, len(a) - 1
while l < r:
    s = a[l] + a[r]
    if s == target: return [l, r]
    if s < target: l += 1
    else: r -= 1
```

### Fast/Slow Pointers
Cycle detection, middle node, cycle start (reset one pointer to head, move both by 1).
```python
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
    if slow is fast: return True
return False
```

### Prefix Sum + HashMap
Count subarrays with sum K: seen[prefix - K] gives number of valid starts.
```python
seen = {0: 1}; pre = ans = 0
for x in a:
    pre += x
    ans += seen.get(pre - k, 0)
    seen[pre] = seen.get(pre, 0) + 1
```

### Monotonic Stack
Next greater element: stack holds indices with decreasing values.
```python
res = [-1] * len(a); st = []
for i, x in enumerate(a):
    while st and a[st[-1]] < x:
        res[st.pop()] = x
    st.append(i)
```

### Bit Manipulation Tricks
- n & (n-1) clears lowest set bit; n & (n-1) == 0 (n > 0) means power of two
- n & -n isolates lowest set bit; (n >> i) & 1 tests bit i
- XOR: a^a = 0, a^0 = a, commutative. XOR of all elements finds the single non-duplicate.
- Swap without temp: a ^= b; b ^= a; a ^= b
- Subsets via mask: for mask in range(1 << n)
```python
def count_bits(n):
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c
```

### Union-Find (Path Compression + Union by Size)
```python
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    a, b = find(a), find(b)
    if a == b: return False
    if size[a] < size[b]: a, b = b, a
    parent[b] = a; size[a] += size[b]
    return True
```

### Topological Sort (Kahn's)
Result shorter than V means a cycle exists.
```python
indeg = [0] * n
for u in range(n):
    for v in g[u]: indeg[v] += 1
q = deque(i for i in range(n) if indeg[i] == 0); order = []
while q:
    u = q.popleft(); order.append(u)
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)
```

### Segment Tree / Fenwick Tree (Overview)
- Segment tree: range query (sum/min/max) and point or range update, O(log n), O(4n) space.
- Fenwick (BIT): prefix sums with point updates, smaller and simpler, O(log n).
```python
def update(i, d):          # 1-indexed
    while i <= n: bit[i] += d; i += i & -i
def query(i):              # sum of [1..i]
    s = 0
    while i > 0: s += bit[i]; i -= i & -i
    return s
```

### String Matching: KMP / Z / Rabin-Karp (Overview)
- KMP: build LPS (longest proper prefix that is also suffix) array, never move back in text. O(n+m).
- Z-algorithm: z[i] = longest match of s[i:] with prefix of s. Search pattern + "$" + text. O(n+m).
- Rabin-Karp: rolling hash of window, compare hash then verify. Average O(n+m), worst O(nm). Good for multi-pattern.

### Binary Search on Answer
Use when feasibility is monotonic (Koko bananas, ship packages, split array).
```python
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid): hi = mid
    else: lo = mid + 1
return lo
```

### Intervals
Sort by start, then merge or sweep. For meeting rooms use a min-heap of end times.
```python
intervals.sort(); out = [intervals[0]]
for s, e in intervals[1:]:
    if s <= out[-1][1]: out[-1][1] = max(out[-1][1], e)
    else: out.append([s, e])
```

### Cyclic Sort
For values in 1..n: place each value at index value-1. O(n) time, O(1) space. Finds missing/duplicate numbers.
```python
i = 0
while i < len(a):
    j = a[i] - 1
    if a[i] != a[j]: a[i], a[j] = a[j], a[i]
    else: i += 1
```

---

## How to Approach a Coding Interview

1. **Clarify**: restate the problem; ask about input size, duplicates, negatives, empty input, sorted or not, expected output. Say: "Let me confirm I understand. Can the array be empty? What are the constraints on n?"
2. **Examples and edge cases**: walk through a small example, then edge cases (empty, single element, all same, max size). Say: "Let me try an example, and I will note edge cases as I go."
3. **Brute force first**: state the obvious solution and its complexity. Say: "The brute force is O(n^2) by checking all pairs. Let me see if we can do better."
4. **Optimize**: name the bottleneck and match a pattern (see cheat sheet above). Say: "The repeated work is the lookup, so a hashmap makes it O(1) at the cost of O(n) space."
5. **Code**: confirm the approach with the interviewer, then write clean code with meaningful names, narrating key lines. Say: "I will use left and right pointers; left moves when the window is invalid."
6. **Test and analyze**: dry-run the code on the example and an edge case, fix bugs, then state time and space complexity and possible improvements. Say: "Tracing [2,7,11] with target 9 returns [0,1]. Time O(n), space O(n)."

Tips: think aloud, never go silent for more than a minute, ask for a hint rather than freezing.

---

## Constraint to Complexity

| Constraint on n | Target complexity | Typical approach |
|---|---|---|
| n <= 10 | O(n!) | Permutations, brute-force backtracking |
| n <= 20 | O(2^n) | Subsets, bitmask DP, meet in the middle |
| n <= 500 | O(n^3) | Floyd-Warshall, 3D/interval DP |
| n <= 10^4 | O(n^2) | 2D DP, nested loops |
| n <= 10^6 | O(n log n) | Sorting, heap, binary search, segment tree |
| n <= 10^8 | O(n) | Single pass, two pointers, hashing |
| n > 10^8 | O(log n) or O(1) | Binary search, math formula |

Rule of thumb: about 10^8 simple operations per second.
