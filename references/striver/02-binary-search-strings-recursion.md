# Striver A2Z: Binary Search, Strings, Recursion (problems 105-164)

## Pattern Playbook
| Pattern | Use when (clue in the problem statement) | Template/steps in 1-2 lines | Problem numbers |
|---|---|---|---|
| BS Classic | Sorted array, find a target or position, O(log n) asked | lo=0, hi=n-1; mid=lo+(hi-lo)/2; compare, discard half | 105, 108 |
| Lower/Upper Bound | First index >= x or > x; count/first/last occurrence; floor/ceil | Find first index where predicate true; ans=n default; if pred(mid) ans=mid, hi=mid-1 else lo=mid+1 | 106, 107, 108, 109, 110, 116 |
| Rotated Array BS | Sorted array rotated at unknown pivot; find target/min/rotations | Find which half is sorted (arr[lo]<=arr[mid]); check if target/min lies there; else go other half | 111, 112, 113, 114 |
| BS on Index Property | Pairs/structure break at one index; O(log n) with no full sort order | Test a property at mid (parity, missing count) to decide the side | 115, 123 |
| BS on Answer (min feasible) | "Minimize the maximum" / "smallest X such that it works"; feasibility is monotonic | lo=min possible, hi=max possible; check(mid) via O(n) scan; if ok hi=mid-1 (record) else lo=mid+1 | 117, 118, 119, 120, 121, 122, 124, 126, 131 |
| BS on Answer (max feasible) | "Maximize the minimum" (distance, gap) | Sort; check(mid) greedy placement; if ok record and lo=mid+1 else hi=mid-1 | 125 |
| BS on Real Answer | Answer is a real number with precision (1e-6) | Binary search on doubles for ~100 iterations or until hi-lo<eps; count needed pieces | 130 |
| BS on Partition (Two Sorted Arrays) | Median / kth of two sorted arrays in O(log) | Binary search cut in smaller array; need L1<=R2 and L2<=R1 | 128, 129 |
| Peak Finding BS | Local maximum, neighbors smaller, O(log n) | If arr[mid]<arr[mid+1] go right else go left (1D); pick max of column/row for 2D | 127, 135 |
| 2D Matrix Search | Row/column sorted matrix, search or count | Fully sorted rows: flatten index mid -> (mid/m, mid%m). Row+col sorted: staircase from top-right | 132, 133, 134, 136 |
| BS on Value in Matrix | Median/kth of row-wise sorted matrix | BS on value range; count elements <= mid per row with upper bound; compare to (r*c+1)/2 | 136 |
| Counter / Stack Scan | Parentheses depth, outer/inner levels | Keep depth counter (or stack); update on '(' and ')' | 137, 138 |
| String Parsing Simulation | Convert string to number with rules (sign, overflow, whitespace) | Single pass with rules; clamp on overflow; roman uses subtract-if-smaller-than-next | 139, 140 |
| Substring Enumeration / Expand Around Center | Substring or palindromic substring questions with n <= ~1000-5000 | Fix start, extend end while updating freq; or expand from each center (odd and even) | 141, 142, 143 |
| Fast Exponentiation (Recursion) | Large power, mod 1e9+7, n up to 1e15 | pow(x,n)=pow(x*x,n/2) times x if odd; handle negative n | 144, 147 |
| Recursion Build (Generate Valid Strings) | Generate all valid strings/structures with constraints | Add char if constraint holds (open<n, close<open; previous not 1); recurse; length reached -> store | 145, 151 |
| Recursion Stack Manipulation | Reverse/sort stack without extra DS | Pop top, recurse on rest, insert at bottom (second recursion) | 148 |
| Subsequence Pick/Not-Pick | All subsets/subsequences, subsequence with sum K, count of them | f(i,sum): not-pick f(i+1) and pick f(i+1,sum+a[i]); base i==n | 146, 149, 150, 154 |
| Combination Sum (Reuse Element) | Combinations summing to target, elements reusable | Pick: stay at i with target-a[i]; not-pick: i+1 | 152 |
| Backtracking with Duplicate Skip | Unique combos/subsets from array with duplicates | Sort; loop from idx; skip if i>idx and a[i]==a[i-1]; recurse i+1 | 153, 155, 156 |
| Backtracking Mapping/Partition | Cut string into pieces, expand digits to letters | Loop over choices at each position; add choice, recurse, undo | 157, 158 |
| Grid Backtracking | Path in grid with visited marks, 4 directions | Mark visited, try all 4 neighbors, unmark on return | 159, 161 |
| Constraint Backtracking | Place items with row/col/box/adjacency constraints (N-Queen, Sudoku, coloring) | Try each choice, check validity (hash arrays or scan), recurse, undo | 160, 162, 163 |
| Expression Backtracking | Insert operators between digits to reach target | Recurse on cut position, track value, last operand (for multiplication undo) | 164 |

## Binary Search (id 1999)
### Fundamentals (id 2035)
Sub-pattern focus: master the invariant "ans = n default, shrink to first true"; every bound problem reuses it.
105. Search X in sorted array [B] | Pattern: BS Classic | Idea: Compare mid with target, discard half; return index or -1 (LC 704) | TC O(log n) SC O(1)
106. Lower Bound | Pattern: Lower/Upper Bound | Idea: First index with arr[i] >= x; default n if none | TC O(log n) SC O(1)
107. Upper Bound | Pattern: Lower/Upper Bound | Idea: First index with arr[i] > x; default n if none | TC O(log n) SC O(1)
### Logic Building (id 2036)
Sub-pattern focus: bounds give first/last/count/floor/ceil; rotated arrays: identify the sorted half each step.
108. Search insert position [B] | Pattern: Lower/Upper Bound | Idea: Answer is lower bound of target (LC 35) | TC O(log n) SC O(1)
109. Floor and Ceil in Sorted Array | Pattern: Lower/Upper Bound | Idea: Floor = largest <= x, ceil = smallest >= x; one BS each | TC O(log n) SC O(1)
110. First and last occurrence | Pattern: Lower/Upper Bound | Idea: First = lower bound; last = upper bound minus 1; verify value (LC 34) | TC O(log n) SC O(1)
111. Search in rotated sorted array-I | Pattern: Rotated Array BS | Idea: Find sorted half, check if target lies inside, else other half (LC 33) | TC O(log n) SC O(1)
112. Search in rotated sorted array-II | Pattern: Rotated Array BS | Idea: Same as I; if lo,mid,hi equal shrink both ends (LC 81) | TC O(log n) avg, O(n) worst SC O(1)
113. Find minimum in Rotated Sorted Array | Pattern: Rotated Array BS | Idea: If arr[mid]>arr[hi] go right else go left, tracking min (LC 153) | TC O(log n) SC O(1)
114. Find out how many times the array is rotated | Pattern: Rotated Array BS | Idea: Rotation count equals index of the minimum element | TC O(log n) SC O(1)
115. Single element in sorted array | Pattern: BS on Index Property | Idea: Before the single, pairs start at even index; use parity of mid (LC 540) | TC O(log n) SC O(1)
116. Count Occurrences in a Sorted Array | Pattern: Lower/Upper Bound | Idea: Count = upper bound minus lower bound | TC O(log n) SC O(1)
### On answers (id 2037)
Sub-pattern focus: identify monotonic check(x); write check as an O(n) scan; BS between min and max/sum of the array.
117. Find square root of a number | Pattern: BS on Answer (max feasible) | Idea: Largest x with x*x <= n, BS on 1..n; use long to avoid overflow | TC O(log n) SC O(1)
118. Find Nth root of a number | Pattern: BS on Answer (min feasible) | Idea: BS on 1..m, compute mid^n with early exit above m; return -1 if none | TC O(n log m) SC O(1)
119. Find the smallest divisor | Pattern: BS on Answer (min feasible) | Idea: BS divisor 1..max; sum of ceil(a/d) must be <= threshold (LC 1283) | TC O(n log max) SC O(1)
120. Koko eating bananas [P] | Pattern: BS on Answer (min feasible) | Idea: BS speed 1..max pile; hours = sum ceil(pile/speed) <= h (LC 875) | TC O(n log max) SC O(1)
121. Minimum days to make M bouquets [P] | Pattern: BS on Answer (min feasible) | Idea: BS days; count adjacent bloomed groups of size k >= m; -1 if m*k>n (LC 1482) | TC O(n log max) SC O(1)
122. Capacity to Ship Packages Within D Days [P] | Pattern: BS on Answer (min feasible) | Idea: BS capacity max(w)..sum(w); greedily count days (LC 1011) | TC O(n log sum) SC O(1)
123. Kth Missing Positive Number [P] | Pattern: BS on Index Property | Idea: Missing before i = arr[i]-(i+1); BS first i with missing>=k; ans = k+lo (LC 1539) | TC O(log n) SC O(1)
124. Painter's Partition [P] | Pattern: BS on Answer (min feasible) | Idea: Minimize max segment sum over k painters; same as split array | TC O(n log sum) SC O(1)
### FAQs (id 2038)
Sub-pattern focus: "minimize the max" and "maximize the min" are the two BS-on-answer flavors; median of two arrays is the hardest BS partition.
125. Aggressive Cows [P] | Pattern: BS on Answer (max feasible) | Idea: Sort stalls; BS min distance; greedily place cows, check count >= k | TC O(n log n + n log maxd) SC O(1)
126. Book Allocation Problem [P] | Pattern: BS on Answer (min feasible) | Idea: Minimize max pages per student; greedy count students; -1 if m>n | TC O(n log sum) SC O(1)
127. Find peak element | Pattern: Peak Finding BS | Idea: If a[mid]<a[mid+1] go right else left (LC 162) | TC O(log n) SC O(1)
128. Median of 2 sorted arrays [P] | Pattern: BS on Partition (Two Sorted Arrays) | Idea: BS cut on smaller array so left halves <= right halves (LC 4) | TC O(log min(m,n)) SC O(1)
129. Kth element of 2 sorted arrays [P] | Pattern: BS on Partition (Two Sorted Arrays) | Idea: BS how many taken from smaller array, left size = k; same cut checks | TC O(log min(m,n)) SC O(1)
130. Minimize Max Distance to Gas Station [P] | Pattern: BS on Real Answer | Idea: BS distance d; stations needed = sum ceil(gap/d)-1 <= k (LC 774 is similar) | TC O(n log(range/eps)) SC O(1)
131. Split array - largest sum [P] | Pattern: BS on Answer (min feasible) | Idea: BS max(a)..sum(a); greedily count subarrays <= k (LC 410) | TC O(n log sum) SC O(1)
### 2D Arrays (id 2039)
Sub-pattern focus: fully sorted matrix = flatten; row and column sorted = staircase walk from top-right; median = BS on value.
132. Find row with maximum 1's | Pattern: 2D Matrix Search | Idea: Rows sorted; lower bound of first 1 per row, max count wins | TC O(n log m) SC O(1)
133. Search in a 2D Matrix | Pattern: 2D Matrix Search | Idea: Treat as flattened sorted array, row=mid/m, col=mid%m (LC 74) | TC O(log(n*m)) SC O(1)
134. Search in 2D matrix - II | Pattern: 2D Matrix Search | Idea: Start top-right; move left if too big, down if too small (LC 240) | TC O(n+m) SC O(1)
135. Find Peak Element - II | Pattern: Peak Finding BS | Idea: BS on column; take max row in mid column, move toward bigger neighbor (LC 1901) | TC O(n log m) SC O(1)
136. Matrix Median [P] | Pattern: BS on Value in Matrix | Idea: BS value range; count elements <= mid per row via upper bound; need > half | TC O(32 * r log c) SC O(1)
## Strings (Basic and Medium) (id 17176)
### Parentheses (id 17177)
Sub-pattern focus: a depth counter replaces the stack when only depth matters.
137. Remove Outermost Parentheses | Pattern: Counter / Stack Scan | Idea: Skip '(' when depth becomes 1 and ')' when depth becomes 0 (LC 1021) | TC O(n) SC O(n)
138. Maximum Nesting Depth of the Parentheses | Pattern: Counter / Stack Scan | Idea: Increment on '(', decrement on ')', track max (LC 1614) | TC O(n) SC O(1)
### String Conversions (id 17178)
139. Roman to Integer [B] | Pattern: String Parsing Simulation | Idea: Add value; subtract if smaller than next symbol (LC 13) | TC O(n) SC O(1)
140. String to Integer (atoi) | Pattern: String Parsing Simulation | Idea: Skip spaces, read sign, digits, clamp to int range while building (LC 8) | TC O(n) SC O(1)
### Substring Problems (id 17179)
Sub-pattern focus: palindromic substring = expand around center; counting with constraints may need sliding window.
141. Count Number of Substrings | Pattern: Substring Enumeration / Expand Around Center | Idea: Likely count substrings with exactly K distinct chars: atMost(k) minus atMost(k-1) | TC O(n) SC O(1)
142. Longest Palindromic Substring | Pattern: Substring Enumeration / Expand Around Center | Idea: Expand from each center (odd and even), keep longest (LC 5) | TC O(n^2) SC O(1)
143. Sum of Beauty of All Substrings | Pattern: Substring Enumeration / Expand Around Center | Idea: Fix start, extend end, keep 26-size freq, beauty = max-min nonzero (LC 1781) | TC O(26 n^2) SC O(26)
## Recursion (id 2000)
### Implementation Problems (id 2041)
144. Pow(x,n) | Pattern: Fast Exponentiation (Recursion) | Idea: Halve exponent each step; for negative n invert x, use long n (LC 50) | TC O(log n) SC O(log n)
145. Generate Parentheses | Pattern: Recursion Build (Generate Valid Strings) | Idea: Add '(' if open<n, ')' if close<open (LC 22) | TC O(4^n / sqrt(n)) SC O(n)
146. Power Set | Pattern: Subsequence Pick/Not-Pick | Idea: Pick/not-pick each element, or bitmask 0..2^n-1 | TC O(n * 2^n) SC O(n)
147. Count Good Numbers | Pattern: Fast Exponentiation (Recursion) | Idea: 5^ceil(n/2) * 4^floor(n/2) mod 1e9+7 using fast power (LC 1922) | TC O(log n) SC O(log n)
148. Reverse a Stack | Pattern: Recursion Stack Manipulation | Idea: Pop top, reverse rest, insert top at bottom recursively | TC O(n^2) SC O(n)
### Subsequence Pattern Problems (id 2042)
Sub-pattern focus: pick/not-pick; return true early for existence, return count for counting.
149. Check if there exists a subsequence with sum K | Pattern: Subsequence Pick/Not-Pick | Idea: Pick/not-pick, return true as soon as sum==K; DP gives O(n*K) | TC O(2^n) SC O(n)
150. Count all subsequences with sum K | Pattern: Subsequence Pick/Not-Pick | Idea: Return count of pick + not-pick paths; memoize on (i,sum) for O(n*K) | TC O(2^n) SC O(n)
151. Generate Binary Strings Without Consecutive 1s | Pattern: Recursion Build (Generate Valid Strings) | Idea: Always add 0; add 1 only if previous char is not 1 | TC O(2^n) SC O(n)
### FAQs (Medium) (id 2043)
Sub-pattern focus: unlimited reuse = stay on index; duplicates = sort and skip same value at same level.
152. Combination Sum | Pattern: Combination Sum (Reuse Element) | Idea: Pick (stay at i, reduce target) or move to i+1 (LC 39) | TC O(2^t) approx SC O(t/min)
153. Combination Sum II | Pattern: Backtracking with Duplicate Skip | Idea: Sort; loop from idx, skip a[i]==a[i-1] when i>idx, recurse i+1 (LC 40) | TC O(2^n) SC O(n)
154. Subsets I | Pattern: Subsequence Pick/Not-Pick | Idea: Pick/not-pick each element, add at base case (LC 78) | TC O(n * 2^n) SC O(n)
155. Subsets II | Pattern: Backtracking with Duplicate Skip | Idea: Sort; add current subset at every node; skip duplicates at same level (LC 90) | TC O(n * 2^n) SC O(n)
156. Combination Sum III [P] | Pattern: Backtracking with Duplicate Skip | Idea: Choose k distinct numbers from 1..9 summing to n, increasing order (LC 216) | TC O(C(9,k) * k) SC O(k)
### Hard (id 2044)
157. Letter Combinations of a Phone Number [P] | Pattern: Backtracking Mapping/Partition | Idea: Digit-to-letters map; recurse per digit appending each letter (LC 17) | TC O(4^n * n) SC O(n)
### FAQs (Hard) (id 2045)
Sub-pattern focus: always "choose, recurse, undo"; use hash arrays for O(1) validity checks in N-Queen.
158. Palindrome partitioning [P] | Pattern: Backtracking Mapping/Partition | Idea: Try each prefix that is palindrome, recurse on remainder (LC 131) | TC O(n * 2^n) SC O(n)
159. Word Search [P] | Pattern: Grid Backtracking | Idea: DFS from each cell matching word chars; mark visited, unmark on return (LC 79) | TC O(m*n*4^L) SC O(L)
160. N Queen [P] | Pattern: Constraint Backtracking | Idea: Place per row; track column, diagonal, anti-diagonal in hash arrays (LC 51) | TC O(n!) SC O(n)
161. Rat in a Maze [P] | Pattern: Grid Backtracking | Idea: Try D, L, R, U with visited; record path at destination | TC O(4^(n*n)) worst SC O(n*n)
162. M Coloring Problem [P] | Pattern: Constraint Backtracking | Idea: Color each node 1..m if no adjacent node has that color | TC O(m^n) SC O(n)
163. Sudoku Solver [P] | Pattern: Constraint Backtracking | Idea: For each empty cell try 1-9 valid in row/col/box, backtrack (LC 37) | TC O(9^(empty cells)) SC O(1)
164. Expression Add Operators [P] | Pattern: Expression Backtracking | Idea: Recurse on cut, track value and last operand to undo multiplication (LC 282) | TC O(4^n) approx SC O(n)
