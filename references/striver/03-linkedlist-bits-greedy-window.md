# Striver A2Z: Linked List, Bit Manipulation, Greedy, Sliding Window

## Pattern Playbook

| Pattern | Use when (clue) | Template/steps | Problems |
|---|---|---|---|
| Pointer traversal/rewiring | Insert/delete/search by position or value in a list | Walk with cur (and prev); relink next (and prev for DLL); handle head/tail edge cases | 165-185, 205-207 |
| Dummy node | Head may change or be deleted; building a new list | dummy->next=head; operate via prev pointer; return dummy->next | 169, 186, 187, 188, 189, 191, 193, 201, 205 |
| Slow/fast pointers | Middle, Nth from end, cycle, kth gap | slow+=1, fast+=2 (or gap of n); stop when fast hits null | 189, 192, 193, 194, 196, 197, 198 |
| Floyd cycle detection | "Loop in list", start of loop, loop length | Meet point; reset one to head, move both by 1 to find start; count steps for length | 196, 197, 198 |
| In-place reversal | Reverse list/part of list, palindrome, group-wise, add-one | prev=null; loop: save next, cur->next=prev, advance | 185, 190, 191, 194, 199 |
| Two pointers, length-difference switch | Intersection of two lists | a,b walk; on null jump to other head; meet at intersection or null | 195 |
| Merge two sorted lists | Combine sorted lists, sort list, flatten | Compare heads, attach smaller to tail of dummy list | 201, 202, 203 |
| Rotate/split-and-join | Rotate by k, odd-even, segregate | Find length/tail, make circular or split, relink at new head | 187, 188, 200 |
| Hashing / pointer interleave clone | Deep copy with random pointer | Map old->new, or weave copies between nodes, set random, unweave | 204 |
| Two pointers on sorted DLL | Pairs with sum in sorted DLL, remove dups | left=head, right=tail; move by sum comparison | 206, 207 |
| Bit test/set/clear | Check/set i-th bit, odd, power of 2 | n>>i & 1; n|(1<<i); n&(n-1) clears lowest set bit; n&1 odd | 208-213 |
| Brian Kernighan set-bit counting | Count set bits, bit flips | while n: n&=n-1; count++ ; flips = popcount(a^b) | 211, 214 |
| XOR tricks | Find unique element, swap w/o temp, range XOR | a^a=0, a^0=a; XOR all; split by a set bit for two uniques | 213, 215, 217, 220 |
| Bit count per position | Every element repeats 3 times except one | Per bit, sum mod 3, or ones/twos state machine | 216 |
| Bit shifting (binary long division) | Divide/multiply without operators | Subtract largest (divisor<<k) <= dividend; accumulate 1<<k | 218 |
| Bit masking / subsets | Enumerate all subsets | For mask 0..2^n-1, include i if mask>>i & 1 | 219 |
| Greedy sort + two pointers | Match items by size/cost; take best-ratio first | Sort one/both arrays, greedily assign smallest sufficient / best ratio | 221, 223, 225 |
| Greedy counting | Simulate with limited resources (change) | Keep counts, prefer using bigger denomination first | 222 |
| Greedy reach/jump | Can reach end; min jumps | Track farthest reach; for min jumps expand level by level | 224, 234 |
| Activity selection / sort by end | Max non-overlapping meetings/intervals | Sort by end time; take if start >= last end | 227, 228 |
| Sort by deadline/profit (job scheduling) | Unit jobs with deadlines, max profit | Sort by profit desc; place in latest free slot <= deadline (array/DSU) | 226 |
| Interval merge (sort by start) | Merge/insert overlapping intervals | Sort by start; extend last interval end if overlap else push | 229, 230 |
| Two sorted arrays sweep | Min platforms/rooms at once | Sort arrivals and departures; sweep, track max concurrent | 231 |
| Greedy range tracking | Parenthesis with wildcard | Track min and max possible open count; min clamps at 0 | 232 |
| Two-pass greedy | Constraint from both neighbors (candy) | Left-to-right pass, right-to-left pass, take max | 233 |
| Constant sliding window | Fixed size k window, or total minus window | Compute first window; slide add new, drop old. Or take prefix+suffix | 235 |
| Variable window (longest) | Longest substring/subarray with constraint | Expand r; while invalid shrink l; track max length | 236-240 |
| Variable window (shortest/min cover) | Minimum window containing requirement | Expand until valid, then shrink l while valid; record min | 241, 242 |
| atMost(k) - atMost(k-1) counting | Count subarrays with exactly k | exactly(k)=atMost(k)-atMost(k-1); atMost via window, add r-l+1 per r | 244, 245, 246 |
| Last-seen index window | Count substrings containing all required chars | Track last index of each char; add min(last)+1 per right end | 243 |

## Linked-List (id 2001)
### Fundamentals (Single LL) (id 2047)
Sub-pattern focus: always handle empty list, single node, head and tail edge cases.
165. Traversal in Linked List [B] | Pattern: Pointer traversal | Idea: Move cur=cur->next until null, processing each node | TC O(n) SC O(1)
166. Deletion of the head of LL | Pattern: Pointer rewiring | Idea: Move head to head->next, free old head | TC O(1) SC O(1)
167. Deletion of the tail of Linked List | Pattern: Pointer rewiring | Idea: Stop at second-last node, set its next to null | TC O(n) SC O(1)
168. Deletion of the Kth element of Linked List | Pattern: Pointer rewiring | Idea: Walk to (k-1)th node, bypass kth; handle k=1 as head | TC O(k) SC O(1)
169. Delete the element with value X | Pattern: Pointer rewiring | Idea: Track prev while scanning; bypass first node equal to X | TC O(n) SC O(1)
170. Insertion at the head of Linked List | Pattern: Pointer rewiring | Idea: New node's next=head; head=new node | TC O(1) SC O(1)
171. Insertion at the tail of Linked List | Pattern: Pointer rewiring | Idea: Walk to last node, link new node (or keep tail pointer for O(1)) | TC O(n) SC O(1)
172. Insertion at the Kth position of Linked List | Pattern: Pointer rewiring | Idea: Walk to (k-1)th node, splice new node in; k=1 is head insert | TC O(k) SC O(1)
173. Insertion before the value X in Linked List | Pattern: Pointer rewiring | Idea: Find node with value X via prev, insert between prev and it | TC O(n) SC O(1)
174. Find the length of the Linked List [B] | Pattern: Pointer traversal | Idea: Count nodes while traversing to null | TC O(n) SC O(1)
175. Search in Linked List | Pattern: Pointer traversal | Idea: Linear scan comparing each node value to target | TC O(n) SC O(1)
### Fundamentals (Doubly LL) (id 2048)
Sub-pattern focus: update both next and prev; set new node's links before fixing neighbors.
176. Convert Array to Doubly Linked List | Pattern: Pointer rewiring | Idea: Keep prev pointer; link new node's prev and prev's next per element | TC O(n) SC O(n)
177. Delete Tail of Doubly Linked List | Pattern: Pointer rewiring | Idea: Go to tail, tail->prev->next=null, free tail | TC O(n) SC O(1)
178. Delete Kth Element of Doubly Linked List | Pattern: Pointer rewiring | Idea: Walk to kth node, link its prev and next to each other | TC O(k) SC O(1)
179. Removing given node in Doubly Linked List | Pattern: Pointer rewiring | Idea: Given node pointer, join prev and next directly; no traversal needed | TC O(1) SC O(1)
180. Insert node before head in Doubly Linked List | Pattern: Pointer rewiring | Idea: new->next=head; head->prev=new; head=new | TC O(1) SC O(1)
181. Insert node before tail in Doubly Linked List | Pattern: Pointer rewiring | Idea: Walk to tail, splice new node between tail->prev and tail | TC O(n) SC O(1)
182. Insert node before (kth node) in Doubly Linked List | Pattern: Pointer rewiring | Idea: Walk to kth node, insert between its prev and itself | TC O(k) SC O(1)
183. Insert before given node in Doubly Linked List | Pattern: Pointer rewiring | Idea: Given node pointer, splice using its prev in O(1) | TC O(1) SC O(1)
184. Delete head of Doubly Linked List | Pattern: Pointer rewiring | Idea: head=head->next; set new head's prev to null | TC O(1) SC O(1)
185. Reverse a Doubly Linked List | Pattern: In-place reversal | Idea: Swap next and prev of every node; new head is old tail | TC O(n) SC O(1)
### Logic Building (id 2049)
186. Add two numbers in Linked List | Pattern: Dummy node | Idea: Digit-wise add with carry on digits stored in reverse order (LC 2) | TC O(max(m,n)) SC O(max(m,n))
187. Segregate odd and even nodes in Linked List | Pattern: Rotate/split-and-join | Idea: Build odd and even chains in place, attach even after odd (LC 328 is by position) | TC O(n) SC O(1)
188. Sort a Linked List of 0's 1's and 2's | Pattern: Dummy node | Idea: Three dummy lists by value then concatenate; or count and overwrite | TC O(n) SC O(1)
189. Remove Nth node from the back of the LL | Pattern: Slow/fast pointers | Idea: Advance fast n steps, then move both; slow stops before target (LC 19) | TC O(n) SC O(1)
190. Reverse a LL | Pattern: In-place reversal | Idea: Iterate flipping next to prev with three pointers (LC 206) | TC O(n) SC O(1)
### FAQs (Medium) (id 2050)
Sub-pattern focus: slow/fast pointer family (middle, palindrome, cycle) plus reversal.
191. Add one to a number represented by LL | Pattern: In-place reversal | Idea: Reverse, add 1 with carry, reverse back; or recursion/last-non-9 trick | TC O(n) SC O(1)
192. Find Middle of Linked List [B] | Pattern: Slow/fast pointers | Idea: Slow moves 1, fast moves 2; slow at middle when fast ends (LC 876) | TC O(n) SC O(1)
193. Delete the middle node in LL | Pattern: Slow/fast pointers | Idea: Start fast two ahead so slow stops just before middle (LC 2095) | TC O(n) SC O(1)
194. Check if LL is palindrome or not | Pattern: In-place reversal | Idea: Find middle, reverse second half, compare halves (LC 234) | TC O(n) SC O(1)
195. Find the intersection point of Y LL | Pattern: Two pointers, length-difference switch | Idea: Switch each pointer to other head at end; they meet at intersection (LC 160) | TC O(m+n) SC O(1)
196. Detect a loop in LL | Pattern: Floyd cycle detection | Idea: Fast and slow pointers meet iff a cycle exists (LC 141) | TC O(n) SC O(1)
197. Find the starting point in LL | Pattern: Floyd cycle detection | Idea: After meeting, reset slow to head; move both by 1 to start (LC 142) | TC O(n) SC O(1)
198. Length of loop in LL | Pattern: Floyd cycle detection | Idea: At meeting point, walk around the cycle counting nodes | TC O(n) SC O(1)
### FAQs (Hard) (id 2051)
199. Reverse LL in group of given size K [P] | Pattern: In-place reversal | Idea: Check k nodes exist, reverse the group, link to recursion/next group (LC 25) | TC O(n) SC O(1)
200. Rotate a LL | Pattern: Rotate/split-and-join | Idea: Make circular, k%=len, break at (len-k)th node (LC 61) | TC O(n) SC O(1)
201. Merge two Sorted Lists | Pattern: Merge two sorted lists | Idea: Dummy node; attach smaller head repeatedly, append remainder (LC 21) | TC O(m+n) SC O(1)
202. Flattening of LL [P] | Pattern: Merge two sorted lists | Idea: Merge bottom-linked sorted lists pairwise from the right | TC O(total nodes * N) SC O(N) recursion
203. Sort LL | Pattern: Merge two sorted lists | Idea: Merge sort: split at middle via slow/fast, sort halves, merge (LC 148) | TC O(n log n) SC O(log n)
204. Clone a LL with random and next pointer [P] | Pattern: Hashing / pointer interleave clone | Idea: Interleave copies after originals, set random, then split lists (LC 138) | TC O(n) SC O(1)
### FAQS (DLL) (id 2052)
205. Delete all occurrences of a key in DLL | Pattern: Dummy node | Idea: Traverse; unlink nodes equal to key using prev and next, fix head | TC O(n) SC O(1)
206. Remove duplicates from sorted DLL | Pattern: Two pointers on sorted DLL | Idea: Duplicates are adjacent; skip next nodes with same value | TC O(n) SC O(1)
207. Find Pairs with Given Sum in Doubly Linked List | Pattern: Two pointers on sorted DLL | Idea: Left at head, right at tail; move by sum vs target (sorted list) | TC O(n) SC O(1)
## Bit Manipulation (id 2002)
### Bit Fundamentals (id 17180)
208. Check if the i-th bit is Set or Not [B] | Pattern: Bit test/set/clear | Idea: Test (n >> i) & 1 or n & (1 << i) | TC O(1) SC O(1)
209. Check if a Number is Odd or Not [B] | Pattern: Bit test/set/clear | Idea: Odd iff n & 1 equals 1 | TC O(1) SC O(1)
210. Check if a Number is Power of 2 or Not [B] | Pattern: Bit test/set/clear | Idea: n > 0 and n & (n-1) == 0 (LC 231) | TC O(1) SC O(1)
211. Count the Number of Set Bits [B] | Pattern: Brian Kernighan set-bit counting | Idea: Repeat n &= n-1 until zero, counting iterations | TC O(set bits) SC O(1)
212. Set the Rightmost Unset Bit | Pattern: Bit test/set/clear | Idea: n | (n+1) sets the lowest zero bit; if all ones, return n | TC O(1) SC O(1)
213. Swap Two Numbers [B] | Pattern: XOR tricks | Idea: a^=b; b^=a; a^=b swaps without temp | TC O(1) SC O(1)
### Problems (id 2055)
Sub-pattern focus: XOR cancels pairs; split-by-set-bit separates two uniques.
214. Minimum Bit Flips to Convert Number [B] | Pattern: Brian Kernighan set-bit counting | Idea: Answer is popcount(start ^ goal) (LC 2220) | TC O(log n) SC O(1)
215. Single Number - I [B] | Pattern: XOR tricks | Idea: XOR all elements; pairs cancel, leaving the unique one (LC 136) | TC O(n) SC O(1)
216. Single Number - II | Pattern: Bit count per position | Idea: Per bit sum mod 3, or ones/twos state trick (LC 137) | TC O(32n) SC O(1)
217. Single Number - III [P] | Pattern: XOR tricks | Idea: XOR all, isolate lowest set bit, split into two groups, XOR each (LC 260) | TC O(n) SC O(1)
218. Divide two numbers without multiplication and division | Pattern: Bit shifting (binary long division) | Idea: Subtract largest divisor<<k each round, add 1<<k to quotient (LC 29) | TC O(log^2 N) SC O(1)
219. Power Set Bit Manipulation | Pattern: Bit masking / subsets | Idea: For each mask 0..2^n-1, pick elements whose bit is set (LC 78) | TC O(n * 2^n) SC O(1) extra
220. XOR of numbers in a given range | Pattern: XOR tricks | Idea: f(R)^f(L-1), where f(n) from n%4 cycle: n,1,n+1,0 | TC O(1) SC O(1)
## Greedy Algorithms (id 2003)
### Easy (id 2057)
221. Assign Cookies | Pattern: Greedy sort + two pointers | Idea: Sort both; give smallest sufficient cookie to each child (LC 455) | TC O(n log n + m log m) SC O(1)
222. Lemonade Change | Pattern: Greedy counting | Idea: Track $5 and $10 counts; for $20 prefer 10+5 over three 5s (LC 860) | TC O(n) SC O(1)
223. Fractional Knapsack | Pattern: Greedy sort + two pointers | Idea: Sort by value/weight desc; take whole items, then fraction of last | TC O(n log n) SC O(1)
224. Jump Game - I | Pattern: Greedy reach/jump | Idea: Track farthest reachable index; fail if i exceeds it (LC 55) | TC O(n) SC O(1)
### Scheduling and Interval Problems (id 2058)
Sub-pattern focus: decide the sort key first (end time, start time, deadline, profit).
225. Shortest Job First | Pattern: Greedy sort + two pointers | Idea: Sort burst times ascending; average the accumulated waiting times | TC O(n log n) SC O(1)
226. Job sequencing Problem | Pattern: Sort by deadline/profit (job scheduling) | Idea: Sort by profit desc; put each job in latest free slot (array or DSU) | TC O(n log n + n*maxDeadline) SC O(maxDeadline)
227. N meetings in one room | Pattern: Activity selection / sort by end | Idea: Sort by end time; take meeting if start > last end | TC O(n log n) SC O(n)
228. Non-overlapping Intervals | Pattern: Activity selection / sort by end | Idea: Sort by end, keep max non-overlapping; answer is n minus kept (LC 435) | TC O(n log n) SC O(1)
229. Insert Interval | Pattern: Interval merge (sort by start) | Idea: Add intervals ending before, merge overlapping with new, add the rest (LC 57) | TC O(n) SC O(n)
230. Merge Intervals | Pattern: Interval merge (sort by start) | Idea: Sort by start; extend last end if overlapping else push (LC 56) | TC O(n log n) SC O(n)
231. Minimum number of platforms required for a railway | Pattern: Two sorted arrays sweep | Idea: Sort arrivals and departures; sweep counting concurrent trains, track max | TC O(n log n) SC O(1)
### Hard (id 2059)
232. Valid Paranthesis Checker [P] | Pattern: Greedy range tracking | Idea: Track min/max open count with '*' wildcard; valid if min is 0 at end (LC 678) | TC O(n) SC O(1)
233. Candy [P] | Pattern: Two-pass greedy | Idea: Left pass for left neighbor, right pass for right neighbor, take max (LC 135) | TC O(n) SC O(n)
234. Jump Game II [P] | Pattern: Greedy reach/jump | Idea: Level-wise BFS in array: jump when current range end is reached (LC 45) | TC O(n) SC O(1)
## Sliding Window / 2 Pointer (id 2004)
### Constant Window (id 2062)
235. Maximum Points You Can Obtain from Cards | Pattern: Constant sliding window | Idea: Take k from ends; slide split point from left prefix to right suffix (LC 1423) | TC O(k) SC O(1)
### Longest and Smallest Window Problems (id 2063)
Sub-pattern focus: longest = shrink only when invalid; smallest = shrink while still valid.
236. Longest Substring Without Repeating Characters | Pattern: Variable window (longest) | Idea: Map char to last index; jump left past duplicate; track max (LC 3) | TC O(n) SC O(min(n, charset))
237. Max Consecutive Ones III | Pattern: Variable window (longest) | Idea: Window with at most k zeros; shrink when zeros exceed k (LC 1004) | TC O(n) SC O(1)
238. Fruit Into Baskets | Pattern: Variable window (longest) | Idea: Longest subarray with at most 2 distinct values (LC 904) | TC O(n) SC O(1)
239. Longest Substring With At Most K Distinct Characters [P] | Pattern: Variable window (longest) | Idea: Frequency map; shrink left while distinct count exceeds k (LC 340) | TC O(n) SC O(k)
240. Longest Repeating Character Replacement [P] | Pattern: Variable window (longest) | Idea: Valid if window size - max freq <= k; never shrink max freq (LC 424) | TC O(n) SC O(26)
241. Minimum Window Substring [P] | Pattern: Variable window (shortest/min cover) | Idea: Need-count map; when all covered, shrink left and record min (LC 76) | TC O(m+n) SC O(charset)
242. Minimum Window Subsequence [P] | Pattern: Variable window (shortest/min cover) | Idea: Forward scan to match, backward scan to shorten; or DP (LC 727) | TC O(m*n) SC O(1)
### Counting Subarrays / Substrings Problems (id 2064)
Sub-pattern focus: "exactly k" turns into atMost(k) - atMost(k-1).
243. Number of Substrings Containing All Three Characters | Pattern: Last-seen index window | Idea: Per right end add 1+min(last a,b,c) valid starts (LC 1358) | TC O(n) SC O(1)
244. Binary Subarrays With Sum | Pattern: atMost(k)-atMost(k-1) counting | Idea: count(atMost(goal)) - count(atMost(goal-1)); prefix-sum map also works (LC 930) | TC O(n) SC O(1)
245. Count number of Nice subarrays [P] | Pattern: atMost(k)-atMost(k-1) counting | Idea: Treat odds as 1s; atMost(k) minus atMost(k-1) (LC 1248) | TC O(n) SC O(1)
246. Subarrays with K Different Integers [P] | Pattern: atMost(k)-atMost(k-1) counting | Idea: atMost(k) distinct minus atMost(k-1) distinct with frequency map (LC 992) | TC O(n) SC O(k)
