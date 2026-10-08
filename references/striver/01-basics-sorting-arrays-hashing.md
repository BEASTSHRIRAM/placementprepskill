# Striver A2Z: Basics, Sorting, Arrays, Hashing

## Pattern Playbook
| Pattern | Use when (clue) | Template/steps | Problem numbers |
|---|---|---|---|
| Nested-loop printing | Print a star/number/letter shape for given N | Outer loop = rows, inner loop = columns/spaces; derive counts from row index | 1-22 |
| Digit extraction | Operate on digits of an integer | while n>0: d=n%10; use d; n/=10 | 23, 24, 25, 26, 27, 29, 59 |
| Math/number theory | Factors, primes, gcd, lcm, perfect numbers | Loop to sqrt(n) for divisors/primes; Euclid for gcd; lcm=a*b/gcd | 28, 30, 31, 32, 33, 34, 35 |
| Single pass scan | Aggregate/check over an array in one traversal | Keep running variable(s) (sum, count, max, prev); update per element | 36, 37, 38, 68, 69, 70, 71, 76 |
| Two pointers | Reverse, partition, merge sorted, pair search in sorted data | l=0, r=n-1 swap/move inward; or i,j walk two arrays | 39, 43, 44, 57, 74, 75, 77, 78, 99 |
| Frequency map / counting | Count occurrences, anagram, top frequency | Array[26/256] or HashMap of counts; then scan counts | 40, 41, 42, 49, 50 |
| Hash map for matching | Need O(1) lookup of seen value / mapping | Store value->index/count; check complement or mapping as you scan | 47, 88, 101, 102, 103, 104, 100 |
| String scan / compare | Prefix, suffix, rotation, parity of last char | Scan from needed end; compare char by char; rotation via s+s | 45, 46, 48 |
| Simple recursion | Problem reduces to smaller same problem with base case | f(n)=op(f(n-1)); base case first; or two-pointer recursion | 51, 52, 53, 54, 55, 56, 58, 60 |
| Elementary sorting | Implement sort by hand | Selection: pick min; Bubble: swap adjacent; Insertion: shift into place | 61, 62, 63, 66, 67 |
| Divide and conquer sort | Need O(n log n) sort | Merge: split, sort halves, merge; Quick: partition around pivot | 64, 65, 96, 97 |
| Rotation (reversal trick) | Rotate array/matrix in place | Reverse parts then whole: rev(0..k-1), rev(k..n-1), rev(all) | 72, 73, 86 |
| Moore's voting | Element appearing > n/2 or > n/3 times | Keep candidate(s)+count; cancel on mismatch; verify | 79, 94 |
| Suffix/right-to-left scan | Element compared to everything on its right | Scan from right keeping running max | 80 |
| Matrix traversal / in-place marker | Spiral, rotate, zero rows/cols | Keep 4 boundaries; or use first row/col as markers | 82, 86, 87 |
| Pascal's triangle formula | nCr, rows of Pascal | C(r,c) computed iteratively: ans=ans*(r-c)/c | 83, 84, 85 |
| Kadane / DP subarray | Max sum or product subarray | cur=max(a[i],cur+a[i]); for product track max and min | 92, 98 |
| Sort then two pointers | k-sum, remove duplicates by sorting | Sort; fix i (and j); two pointers for remainder; skip duplicates | 89, 90 |
| Dutch national flag | Sort values from small fixed set in place | low, mid, high pointers; swap by value | 91 |
| Next permutation | Next lexicographic arrangement | Find break from right, swap with next greater, reverse suffix | 93 |
| Math equations (sum, sum of squares) | One missing and one repeating in 1..N | Solve S-Sn and S2-S2n equations (or XOR) | 76, 95 |
| Prefix sum + hashmap | Subarray with given sum/xor/zero sum | Store first index (or count) of each prefix; look up prefix-K | 101, 102, 103, 104 |
| Hash set sequence | Longest consecutive run, unsorted | Put all in set; start counting only at x where x-1 absent | 100 |
| Merge-sort counting | Count pairs (i<j) with order condition | During merge, count cross pairs using sorted halves | 96, 97 |
| Interleave by index | Rearrange by sign/parity keeping order | Two write indices (even/odd slots) filled from one scan | 81 |

---

## Beginner Problems (id 1995)
### Patterns (id 2017)
Sub-pattern focus: all are nested loops; find the relation between row index and counts of spaces/symbols.
1. Pattern 1 [B] | Pattern: Nested-loop printing | Idea: N x N square of stars; inner loop prints N | TC O(N^2) SC O(1)
2. Pattern 2 [B] | Pattern: Nested-loop printing | Idea: Row i prints i stars (right triangle) | TC O(N^2) SC O(1)
3. Pattern 3 [B] | Pattern: Nested-loop printing | Idea: Row i prints numbers 1..i | TC O(N^2) SC O(1)
4. Pattern 4 [B] | Pattern: Nested-loop printing | Idea: Row i prints number i, i times | TC O(N^2) SC O(1)
5. Pattern 5 [B] | Pattern: Nested-loop printing | Idea: Inverted star triangle; row i prints N-i+1 stars | TC O(N^2) SC O(1)
6. Pattern 6 [B] | Pattern: Nested-loop printing | Idea: Inverted number triangle; row i prints 1..N-i+1 | TC O(N^2) SC O(1)
7. Pattern 7 [B] | Pattern: Nested-loop printing | Idea: Star pyramid; N-i-1 spaces, 2i+1 stars, spaces | TC O(N^2) SC O(1)
8. Pattern 8 [B] | Pattern: Nested-loop printing | Idea: Inverted pyramid; i spaces, 2(N-i)-1 stars | TC O(N^2) SC O(1)
9. Pattern 9 [B] | Pattern: Nested-loop printing | Idea: Diamond = pyramid followed by inverted pyramid | TC O(N^2) SC O(1)
10. Pattern 10 [B] | Pattern: Nested-loop printing | Idea: Half diamond; rows grow to N then shrink | TC O(N^2) SC O(1)
11. Pattern 11 [B] | Pattern: Nested-loop printing | Idea: Binary triangle; start bit alternates by row parity | TC O(N^2) SC O(1)
12. Pattern 12 [B] | Pattern: Nested-loop printing | Idea: Number crown; left numbers, middle spaces, right numbers mirrored | TC O(N^2) SC O(1)
13. Pattern 13 [B] | Pattern: Nested-loop printing | Idea: Number triangle with a running counter across rows | TC O(N^2) SC O(1)
14. Pattern 14 [B] | Pattern: Nested-loop printing | Idea: Row i prints letters A..(A+i) | TC O(N^2) SC O(1)
15. Pattern 15 [B] | Pattern: Nested-loop printing | Idea: Inverted letter triangle; row length shrinks | TC O(N^2) SC O(1)
16. Pattern 16 [B] | Pattern: Nested-loop printing | Idea: Row i prints same letter, i+1 times | TC O(N^2) SC O(1)
17. Pattern 17 [B] | Pattern: Nested-loop printing | Idea: Letter pyramid; ascending then descending letters per row | TC O(N^2) SC O(1)
18. Pattern 18 [B] | Pattern: Nested-loop printing | Idea: Reverse-letter triangle; row i prints letters ending at fixed char | TC O(N^2) SC O(1)
19. Pattern 19 [B] | Pattern: Nested-loop printing | Idea: Symmetric star shape; stars and spaces mirrored top and bottom | TC O(N^2) SC O(1)
20. Pattern 20 | Pattern: Nested-loop printing | Idea: Butterfly shape; stars grow then shrink, spaces opposite | TC O(N^2) SC O(1)
21. Pattern 21 | Pattern: Nested-loop printing | Idea: Hollow rectangle; print star only on border cells | TC O(N^2) SC O(1)
22. Pattern 22 | Pattern: Nested-loop printing | Idea: Value at (i,j) = N - min(i,j,N-1-i,N-1-j) | TC O(N^2) SC O(1)
### Basic Maths (id 2021)
Sub-pattern focus: digit extraction with %10 and /10; divisor/prime checks only need to go to sqrt(n).
23. Count all Digits of a Number [B] | Pattern: Digit extraction | Idea: Divide by 10 until zero, count steps (or log10(n)+1) | TC O(log10 N) SC O(1)
24. Count number of odd digits in a number [B] | Pattern: Digit extraction | Idea: Extract each digit, count if d%2==1 | TC O(log10 N) SC O(1)
25. Reverse a number | Pattern: Digit extraction | Idea: rev=rev*10+d for each digit; watch overflow | TC O(log10 N) SC O(1)
26. Palindrome Number [B] | Pattern: Digit extraction | Idea: Reverse the number, compare with original (negatives are not palindromes) | TC O(log10 N) SC O(1)
27. Return the Largest Digit in a Number [B] | Pattern: Digit extraction | Idea: Track max of digits while extracting | TC O(log10 N) SC O(1)
28. Factorial of a given number [B] | Pattern: Math/number theory | Idea: Multiply 1..N iteratively; use long, overflow beyond 20 | TC O(N) SC O(1)
29. Check if the Number is Armstrong [B] | Pattern: Digit extraction | Idea: Sum of digit^k (k=digit count) equals number | TC O(log10 N * log10 N) SC O(1)
30. Check for Perfect Number [B] | Pattern: Math/number theory | Idea: Sum proper divisors up to sqrt(N), compare to N | TC O(sqrt N) SC O(1)
31. Check for Prime Number | Pattern: Math/number theory | Idea: Test divisors 2..sqrt(N); exactly two divisors means prime | TC O(sqrt N) SC O(1)
32. Count of Prime Numbers till N [B] | Pattern: Math/number theory | Idea: Sieve of Eratosthenes, mark multiples from i*i | TC O(N log log N) SC O(N)
33. GCD of Two Numbers | Pattern: Math/number theory | Idea: Euclid: gcd(a,b)=gcd(b,a%b) until b=0 | TC O(log(min(a,b))) SC O(1)
34. LCM of two numbers | Pattern: Math/number theory | Idea: lcm=(a/gcd)*b via Euclid; divide first to avoid overflow | TC O(log(min(a,b))) SC O(1)
35. Divisors of a Number | Pattern: Math/number theory | Idea: Loop to sqrt(N), add i and N/i; sort if needed | TC O(sqrt N) SC O(sqrt N)
### Basic Arrays (id 2022)
36. Sum of Array Elements [B] | Pattern: Single pass scan | Idea: Accumulate sum in one traversal | TC O(N) SC O(1)
37. Count of odd numbers in Array [B] | Pattern: Single pass scan | Idea: Count elements with a[i]%2!=0 | TC O(N) SC O(1)
38. Check if the Array is Sorted I [B] | Pattern: Single pass scan | Idea: Verify a[i]>=a[i-1] for all i | TC O(N) SC O(1)
39. Reverse an array [B] | Pattern: Two pointers | Idea: Swap a[l], a[r] moving inward | TC O(N) SC O(1)
### Basic Hashing (id 2023)
Sub-pattern focus: build frequency map first, then scan it for max/second max/min.
40. Highest Occurring Element in an Array | Pattern: Frequency map / counting | Idea: Count frequencies in map; pick max frequency (smallest value on tie) | TC O(N) SC O(N)
41. Second Highest Occurring Element | Pattern: Frequency map / counting | Idea: Count frequencies, track top two distinct frequencies in one scan | TC O(N) SC O(N)
42. Sum of Highest and Lowest Frequency | Pattern: Frequency map / counting | Idea: Count frequencies; add max freq and min freq | TC O(N) SC O(N)
### Basic Strings (id 2024)
43. Reverse a String II [B] | Pattern: Two pointers | Idea: Reverse first k chars of every 2k block (LC 541) | TC O(N) SC O(1)
44. Palindrome Check | Pattern: Two pointers | Idea: Compare ends inward, skipping non-alphanumerics, ignoring case (LC 125) | TC O(N) SC O(1)
45. Largest Odd Number in a String | Pattern: String scan / compare | Idea: Scan from right to first odd digit; return prefix up to it | TC O(N) SC O(1)
46. Longest Common Prefix | Pattern: String scan / compare | Idea: Compare first and last of sorted strings, or char-by-char vertical scan | TC O(N*M) SC O(1)
47. Isomorphic Strings [B] | Pattern: Hash map for matching | Idea: Two maps (or arrays) enforcing one-to-one char mapping both ways | TC O(N) SC O(1)
48. Rotate String | Pattern: String scan / compare | Idea: Equal length and goal is substring of s+s (LC 796) | TC O(N) SC O(N)
49. Valid Anagram [B] | Pattern: Frequency map / counting | Idea: Count 26 letters up for s, down for t; all zero | TC O(N) SC O(1)
50. Sort Characters by Frequency | Pattern: Frequency map / counting | Idea: Count chars, bucket by frequency, output from highest (LC 451) | TC O(N) SC O(N)
### Basic Recursion (id 2025)
Sub-pattern focus: write base case first, then reduce n to n-1 (or shrink range l..r).
51. Sum of First N Numbers [B] | Pattern: Simple recursion | Idea: f(n)=n+f(n-1), f(0)=0 (formula n(n+1)/2 is O(1)) | TC O(N) SC O(N)
52. Factorial of a Given Number [B] | Pattern: Simple recursion | Idea: f(n)=n*f(n-1), f(0)=1 | TC O(N) SC O(N)
53. Sum of Array Elements II [B] | Pattern: Simple recursion | Idea: sum(i)=a[i]+sum(i+1), base at i==n | TC O(N) SC O(N)
54. Reverse a String I [B] | Pattern: Simple recursion | Idea: Swap s[l], s[r] then recurse on l+1, r-1 | TC O(N) SC O(N)
55. Check if String is Palindrome or Not [B] | Pattern: Simple recursion | Idea: Compare s[l], s[r] then recurse inward | TC O(N) SC O(N)
56. Check if a Number is Prime or Not | Pattern: Simple recursion | Idea: Recursively test divisors from 2 up to sqrt(N) | TC O(sqrt N) SC O(sqrt N)
57. Reverse an array 2 | Pattern: Two pointers | Idea: Recursive swap of ends, move inward (iterative is O(1) space) | TC O(N) SC O(N)
58. Check if the Array is Sorted II [B] | Pattern: Simple recursion | Idea: a[i]<=a[i+1] and recurse on i+1 | TC O(N) SC O(N)
59. Sum of Digits in a Given Number [B] | Pattern: Digit extraction | Idea: f(n)=n%10+f(n/10), f(0)=0 | TC O(log10 N) SC O(log10 N)
60. Fibonacci Number | Pattern: Simple recursion | Idea: Naive f(n-1)+f(n-2) is O(2^N); memoize or iterate for O(N) | TC O(2^N) SC O(N)
## Sorting (id 1996)
### Algorithms (id 2026)
Sub-pattern focus: O(N^2) sorts (61-63, 66, 67) vs O(N log N) divide and conquer (64, 65).
61. Selection Sort | Pattern: Elementary sorting | Idea: Each pass select min of unsorted part, swap to front | TC O(N^2) SC O(1)
62. Bubble Sort | Pattern: Elementary sorting | Idea: Swap adjacent out-of-order pairs; early exit if no swap gives O(N) best | TC O(N^2) SC O(1)
63. Insertion Sorting | Pattern: Elementary sorting | Idea: Insert a[i] into sorted prefix by shifting larger elements | TC O(N^2) SC O(1)
64. Merge Sorting | Pattern: Divide and conquer sort | Idea: Split in halves, sort recursively, merge with two pointers | TC O(N log N) SC O(N)
65. Quick Sorting | Pattern: Divide and conquer sort | Idea: Partition around pivot, recurse both sides; worst case O(N^2) | TC O(N log N) avg SC O(log N)
66. Recursive Bubble Sort | Pattern: Elementary sorting | Idea: One bubble pass puts max at end, recurse on n-1 | TC O(N^2) SC O(N)
67. Recursive Insertion Sort | Pattern: Elementary sorting | Idea: Sort first n-1 recursively, then insert a[n-1] | TC O(N^2) SC O(N)
## Arrays (id 1997)
### Fundamentals (id 2027)
68. Linear Search [B] | Pattern: Single pass scan | Idea: Scan until target found, return index or -1 | TC O(N) SC O(1)
69. Largest Element [B] | Pattern: Single pass scan | Idea: Track running max | TC O(N) SC O(1)
70. Second Largest Element [B] | Pattern: Single pass scan | Idea: Track largest and second largest strictly less, one pass | TC O(N) SC O(1)
71. Maximum Consecutive Ones [B] | Pattern: Single pass scan | Idea: Count current run of 1s, reset on 0, track max (LC 485) | TC O(N) SC O(1)
72. Left Rotate Array by One [B] | Pattern: Rotation (reversal trick) | Idea: Save a[0], shift all left, put at end | TC O(N) SC O(1)
73. Left Rotate Array by K Places | Pattern: Rotation (reversal trick) | Idea: k%=n; reverse first k, reverse rest, reverse all | TC O(N) SC O(1)
### Logic Building (id 2028)
74. Move Zeros to End [B] | Pattern: Two pointers | Idea: Slow pointer writes non-zeros; fill remaining with zeros (LC 283) | TC O(N) SC O(1)
75. Remove duplicates from sorted array [B] | Pattern: Two pointers | Idea: Write pointer; copy a[i] when it differs from last kept (LC 26) | TC O(N) SC O(1)
76. Find missing number [B] | Pattern: Math equations (sum, sum of squares) | Idea: Expected sum n(n+1)/2 minus actual sum, or XOR (LC 268) | TC O(N) SC O(1)
77. Union of two sorted arrays | Pattern: Two pointers | Idea: Merge with two pointers, skip duplicates against last added | TC O(N+M) SC O(N+M)
78. Intersection of two sorted arrays | Pattern: Two pointers | Idea: Advance smaller pointer; on equal add and move both, skip duplicates | TC O(N+M) SC O(1) extra
### FAQs(Medium) (id 2029)
Sub-pattern focus: classic interview set; many have a brute O(N^2) and an optimal single-pass or hash/pointer version.
79. Majority Element-I | Pattern: Moore's voting | Idea: Boyer-Moore: candidate+count cancellation, element > N/2 (LC 169) | TC O(N) SC O(1)
80. Leaders in an Array | Pattern: Suffix/right-to-left scan | Idea: Scan from right keeping max; element >= max is a leader | TC O(N) SC O(1)
81. Rearrange array elements by sign | Pattern: Interleave by index | Idea: Two indices: positives to even slots, negatives to odd slots (LC 2149) | TC O(N) SC O(N)
82. Print the matrix in spiral manner | Pattern: Matrix traversal / in-place marker | Idea: Shrink four boundaries top/bottom/left/right layer by layer (LC 54) | TC O(N*M) SC O(1) extra
83. Pascal's Triangle I | Pattern: Pascal's triangle formula | Idea: Compute single element C(r-1,c-1) iteratively in O(min(c,r-c)) | TC O(c) SC O(1)
84. Pascal's Triangle II | Pattern: Pascal's triangle formula | Idea: Generate one row using ans=ans*(row-i)/i incrementally | TC O(N) SC O(1) extra
85. Pascal's Triangle III | Pattern: Pascal's triangle formula | Idea: Build N rows, each row from generated row formula (LC 118) | TC O(N^2) SC O(N^2)
86. Rotate matrix by 90 degrees | Pattern: Rotation (reversal trick) | Idea: Transpose, then reverse each row (clockwise) (LC 48) | TC O(N^2) SC O(1)
87. Set Matrix Zeroes | Pattern: Matrix traversal / in-place marker | Idea: Use first row and column as markers, handle them separately (LC 73) | TC O(N*M) SC O(1)
88. Two Sum [B] | Pattern: Hash map for matching | Idea: Store value->index; look up target-a[i] as you scan (LC 1) | TC O(N) SC O(N)
89. 3 Sum | Pattern: Sort then two pointers | Idea: Sort, fix i, two pointers on rest, skip duplicates (LC 15) | TC O(N^2) SC O(1) extra
90. 4 Sum [P] | Pattern: Sort then two pointers | Idea: Sort, fix i and j, two pointers; skip duplicates (LC 18) | TC O(N^3) SC O(1) extra
91. Sort an array of 0's 1's and 2's | Pattern: Dutch national flag | Idea: low/mid/high pointers, swap 0 left and 2 right in one pass (LC 75) | TC O(N) SC O(1)
92. Kadane's Algorithm | Pattern: Kadane / DP subarray | Idea: cur=max(a[i],cur+a[i]); track best (LC 53) | TC O(N) SC O(1)
93. Next Permutation | Pattern: Next permutation | Idea: Find pivot from right, swap with next larger, reverse suffix (LC 31) | TC O(N) SC O(1)
### FAQs(Hard) (id 2030)
94. Majority Element-II | Pattern: Moore's voting | Idea: Two candidates and counts for elements > N/3, then verify (LC 229) | TC O(N) SC O(1)
95. Find the repeating and missing number | Pattern: Math equations (sum, sum of squares) | Idea: Solve sum and sum-of-squares differences, or XOR bit split | TC O(N) SC O(1)
96. Count Inversions [P] | Pattern: Merge-sort counting | Idea: In merge, if left[i]>right[j] add remaining left count | TC O(N log N) SC O(N)
97. Reverse Pairs [P] | Pattern: Merge-sort counting | Idea: Before merge, count i<j with a[i]>2*a[j] via two pointers (LC 493) | TC O(N log N) SC O(N)
98. Maximum Product Subarray in an Array | Pattern: Kadane / DP subarray | Idea: Track max and min product ending here, swap on negative (LC 152) | TC O(N) SC O(1)
99. Merge two sorted arrays without extra space | Pattern: Two pointers | Idea: Gap method (shell sort style) or swap from ends then sort both | TC O((N+M) log(N+M)) SC O(1)
## Hashing (id 1998)
### FAQs (id 2033)
Sub-pattern focus: prefix sum + hashmap of first occurrence solves 101-104; 100 uses a set.
100. Longest Consecutive Sequence in an Array | Pattern: Hash set sequence | Idea: Set of values; count run only from numbers whose x-1 is absent (LC 128) | TC O(N) SC O(N)
101. Longest subarray with sum K | Pattern: Prefix sum + hashmap | Idea: Map first index of each prefix; length = i - map[prefix-K] (negatives OK) | TC O(N) SC O(N)
102. Largest Subarray with Sum 0 | Pattern: Prefix sum + hashmap | Idea: Same as sum K with K=0; repeated prefix means zero-sum segment | TC O(N) SC O(N)
103. Count subarrays with given sum | Pattern: Prefix sum + hashmap | Idea: Map prefix->count; add count of prefix-K at each step (LC 560) | TC O(N) SC O(N)
104. Count subarrays with given xor K [P] | Pattern: Prefix sum + hashmap | Idea: Prefix xor map; add count of (prefix xor K) each step | TC O(N) SC O(N)
