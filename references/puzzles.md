# Puzzles Reference -- Interview Puzzles, Data Interpretation, Output Prediction

(Clocks, probability and P&C formulas are in aptitude.md; not repeated here.)

## 1. How to Approach Puzzles
- State the problem back aloud; confirm the rules and constraints (can I reuse the scale? do liars always lie?).
- Think aloud. Interviewers grade the process as much as the answer.
- Try small cases (n = 1, 2, 3) and look for a pattern, then generalise.
- Look for invariants (parity, a sum that never changes) and for what the worst case is.
- Halving / thirds: a balance has 3 outcomes, so split into 3 groups. Yes/no tests give binary, so think powers of 2.
- Use symmetry and reversal: work backwards from the goal (jugs, pirates).
- Use extremes and "what if everyone did the same thing" (ants, doors).
- Always state a final answer plus a quick verification.

---

## 2. Classic Interview Puzzles

### 1. Eight balls, one heavier (2 weighings)
Split 3 / 3 / 2. Weigh 3 vs 3. If they balance, the heavy ball is in the 2 left out; weigh those two. If not, take the heavier group of 3 and weigh any 1 vs 1: the heavier one, or the third if balanced.

### 2. Nine balls, one heavier (2 weighings)
Split 3 / 3 / 3. Weigh group A vs B; the heavier group (or C if balanced) holds the ball. Weigh 1 vs 1 from that group; heavier one, or the third if balanced. In general 3^n balls need n weighings.

### 3. Three switches, three bulbs (one visit to the room)
Turn on switch 1 and wait several minutes. Turn it off, turn on switch 2, enter the room. Lit bulb = switch 2. Unlit but warm = switch 1. Unlit and cold = switch 3.

### 4. 100 doors
100 doors closed; pass k toggles every k-th door, for k = 1..100. Which are open? Door n is toggled once per divisor. Only perfect squares have an odd number of divisors, so doors 1, 4, 9, ..., 100 are open (10 doors).

### 5. Two eggs, 100 floors (min worst-case drops)
Find the highest safe floor. Drop the first egg at floors 14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 100 (gaps shrink by 1). If it breaks, linear search with egg 2 in the gap. Reason: x + (x-1) + ... + 1 >= 100 gives x(x+1)/2 >= 100, so x = 14. Answer: 14 drops.

### 6. Bridge and torch (1, 2, 5, 10 min; max 2 at a time; one torch)
1+2 cross (2), 1 returns (1), 5+10 cross (10), 2 returns (2), 1+2 cross (2). Total 17 min. Key idea: send the two slowest together.

### 7. Water jugs 3L and 5L, get 4L
Fill 5, pour into 3 (5-jug has 2). Empty 3, pour the 2 into it. Fill 5, top up the 3-jug (needs 1 more). 5-jug now holds 4L.

### 8. Burning ropes, measure 45 minutes
Each rope burns in 60 min, non-uniformly. Light rope A at both ends and rope B at one end at the same time. A burns out at 30 min; then light B's other end. B's remaining half burns in 15 min. Total 45 min.

### 9. 25 horses, find top 3 (5 per race, no timer)
Races 1-5: each group of 5. Race 6: the 5 group winners; rank them and name groups in that order (A fastest winner, E slowest), with Ax = x-th fastest in group A. Groups D and E are out entirely; from group C only C1 can be top 3, from B only B1, B2, from A only A1, A2, A3. A1 is surely first. Race 7: A2, A3, B1, B2, C1; the top 2 of this race are 2nd and 3rd overall. Total 7 races.

### 10. Pirates and gold (5 pirates, 100 coins)
Senior proposes a split; needs at least 50% of votes (own included), else is thrown overboard. Pirates are rational and greedy, and a pirate votes no if it gains nothing by voting yes. Work backwards: 1 pirate keeps 100; with 2 the senior keeps 100; with 3: 99,0,1; with 4: 99,0,1,0; with 5: 98,0,1,0,1 (the proposer buys 2 votes with 1 coin each, from those who would get 0 otherwise). Answer: 98, 0, 1, 0, 1.

### 11. Hat puzzle (100 prisoners, black or white hats, in a line)
Each sees only the hats in front; the last (sees all 99) speaks first, then others speak their own colour. Strategy: the first says "black" if he sees an odd number of black hats, else "white". Each next person counts the blacks ahead and the earlier answers to deduce own hat from the parity. At least 99 survive for sure, the first has a 50% chance.

### 12. Poisoned wine (1000 bottles, 1 poisoned, 10 testers, results after 1 hour)
Number bottles 0..999 in binary (10 bits). Tester i drinks every bottle whose bit i is 1. After an hour, the set of testers who die gives the binary number of the poisoned bottle. 2^10 = 1024 >= 1000.

### 13. Wolf, goat, cabbage
Take goat across. Return alone. Take wolf across, bring goat back. Take cabbage across, return alone, take goat across. 7 crossings.

### 14. Truth teller and liar (fork in the road, one person, one question)
Ask: "If I asked you whether the left road goes to the city, would you say yes?" Both the truth teller and the liar answer "yes" iff the left road really goes to the city (the liar's lie is applied twice and cancels).

### 15. Clock hands angle
Angle = |30H - 5.5M|, take 360 minus it if over 180. At 3:15: |90 - 82.5| = 7.5 degrees. At 3:00: 90. At 6:00: 180.

### 16. Handshakes
n people, everyone shakes hands once with everyone else: nC2 = n(n-1)/2. For 10 people: 45.
### 17. Cutting cake / cube
- 3 planar cuts give at most 8 pieces of a cube/cake (2 vertical + 1 horizontal give 8 equal pieces). Max pieces with n cuts in 3D = (n^3 + 5n + 6)/6.
- Max pieces of a flat pancake with n straight cuts = (n^2 + n + 2)/2 (3 cuts: 7).
- A 3x3x3 cube into 27 unit cubes needs a minimum of 6 cuts, even if pieces are rearranged between cuts (each of the 3 axes needs 2 cuts, because the centre cube has 6 faces and each cut makes at most one of them).

### 18. Ants on a triangle (3 ants, one per corner, each moves along an edge randomly)
Collision occurs unless all move the same way (all clockwise or all anticlockwise). Total outcomes 2^3 = 8, safe outcomes 2. P(no collision) = 2/8 = 1/4, P(collision) = 3/4. For n ants on an n-gon: 1 - 2/2^n = 1 - 1/2^(n-1).

### 19. Birthday paradox
P(at least two share a birthday among n people) = 1 - (365/365)(364/365)...((365-n+1)/365). For n = 23 it is about 50.7%; for n = 57 about 99%. Counterintuitive because pairs grow as n(n-1)/2 (253 pairs at n = 23).

### 20. Monty Hall
3 doors, 1 car. You pick one, the host (who knows) opens a goat door, offers a switch. Staying wins 1/3; switching wins 2/3, because your first pick is wrong with probability 2/3 and then the host's reveal leaves only the car to switch to.

### 21. Three mislabelled boxes (Apples, Oranges, Mixed; every label is wrong)
Pick one fruit from the box labelled "Mixed". It must be pure; say it is an apple, so that box is Apples. The box labelled "Oranges" cannot be Oranges nor Apples, so it is Mixed; the remaining box is Oranges. One draw suffices.

### 22. Last person standing (Josephus, every 2nd person eliminated)
n people in a circle, 1 skips, 2 is eliminated, and so on. Survivor J(n) = 2L + 1 where n = 2^m + L, 0 <= L < 2^m. Equivalent: rotate the binary of n left by one bit. n = 100: 64 + 36, J = 73. n = 41: 32 + 9, J = 19.

### 23. Weighing coins (10 bags of coins; one bag has coins weighing 1 g less than the 10 g genuine ones; one weighing on a digital scale)
Take 1 coin from bag 1, 2 from bag 2, ..., 10 from bag 10 (55 coins). Expected weight 550 g. If the reading is short by d grams, bag d has the light coins.

### 24. Counterfeit coin (12 coins, one odd -- heavier or lighter, unknown -- 3 weighings)
W1: coins 1-4 vs 5-8.
- Balanced: odd is in 9-12. W2: 9,10,11 vs 1,2,3. Balanced means 12 is odd; W3: 12 vs a genuine coin tells heavy or light. Unbalanced: direction tells if the odd coin is heavy or light among 9-11; W3: 9 vs 10 (the odd one is the one tipping the scale; if balanced it is 11).
- Say 1-4 is heavier (1-4 may be heavy, or 5-8 may be light; 9-12 are genuine). W2: {1,2,5} vs {3,6,9}.
  - Left heavier: 1 heavy, 2 heavy or 6 light. W3: 1 vs 2 (heavier is odd; balanced means 6 is light).
  - Balanced: 4 heavy, 7 light or 8 light. W3: 7 vs 8 (lighter is odd; balanced means 4 is heavy).
  - Right heavier: 3 heavy or 5 light. W3: 3 vs genuine (heavier means 3, else 5).
- If 1-4 is lighter, mirror the argument.

### 25. Heaven and hell door (two guards, one always lies, one always tells the truth, you do not know which; one question to either)
Ask either guard: "What would the other guard say is the door to heaven?" Whatever the answer, take the other door. (Truth teller reports the liar's false answer; the liar falsifies the truth teller's true answer. Both point to hell.)

---

## 3. Data Interpretation Basics

### Quick formulas
- Percentage of total = part/total x 100
- Percentage change = (new - old)/old x 100
- Percentage point difference = difference of two percentages (not a percent change)
- Average = sum/count; ratio a:b = a/b simplified
- Pie chart: angle = (value/total) x 360; 1% = 3.6 degrees; value = (angle/360) x total
- Stacked / grouped bar: read the correct series and the scale (units, thousands, lakh)
- CAGR approx = (final/initial)^(1/years) - 1; for small rates approx average annual %
- Approximate: use rounded numbers (49.8 as 50) and compare answer options first; eliminate by ratio
- Check units, "in lakh", and "of what" (percent of total or of a particular year)

### Worked example 1 (table)
Sales (Rs lakh): 2021: A 40, B 50. 2022: A 50, B 55. 2023: A 60, B 66.
- Growth of A from 2021 to 2023 = (60-40)/40 = 50%.
- Ratio A:B in 2023 = 60:66 = 10:11.
- Average sales of B = (50+55+66)/3 = 171/3 = 57 lakh.

### Worked example 2 (pie chart)
Monthly expenditure Rs 7200: Rent 25%, Food 30%, Travel 15%, Savings 20%, Misc 10%.
- Angle for Food = 30% x 360 = 108 degrees.
- Travel amount = 15% of 7200 = Rs 1080.
- Savings is more than Misc by (20-10)/10 = 100%, in money Rs 720.

### Worked example 3 (bar chart)
Students appeared / passed: 2019: 200 / 150, 2020: 250 / 200, 2021: 300 / 210.
- Pass %: 2019 = 75%, 2020 = 80%, 2021 = 70%. Highest in 2020.
- Increase in number passed, 2019 to 2021 = (210-150)/150 = 40%.
- Overall pass % = (150+200+210)/(200+250+300) = 560/750 = 74.67%.

---

## 4. Output Prediction / Tricky Code Snippets

### 1. Post vs pre increment (C)
```c
int i = 5;
int j = i++;   // j = 5, then i = 6
int k = ++i;   // i = 7, then k = 7
printf("%d %d %d", i, j, k);
```
Output: `7 5 7`. Post-increment yields the old value, pre-increment the new. Avoid `i++ + ++i` or `printf("%d %d", i++, ++i)`: modifying a variable twice without a sequence point is undefined behaviour, so never claim a fixed answer.

### 2. Integer overflow (Java)
```java
int x = Integer.MAX_VALUE;
System.out.println(x + 1);
```
Output: `-2147483648`. Java int is 32-bit two's complement and wraps silently (Math.addExact would throw). In C, signed overflow is undefined behaviour.

### 3. Unsigned wrap-around (C, 32-bit unsigned int)
```c
unsigned int u = 0;
u = u - 1;
printf("%u", u);
```
Output: `4294967295`. Unsigned arithmetic is modulo 2^32 and well-defined.

### 4. String immutability (Java)
```java
String s = "hi";
s.concat(" there");
System.out.println(s);
```
Output: `hi`. Strings are immutable; concat returns a new String that was discarded. Use `s = s.concat(...)` or StringBuilder.

### 5. Mutable default argument (Python)
```python
def f(x, lst=[]):
    lst.append(x)
    return lst
print(f(1)); print(f(2))
```
Output: `[1]` then `[1, 2]`. The default list is created once, at function definition, and shared across calls. Fix: `lst=None` and create inside.

### 6. == vs equals (Java)
```java
String a = new String("abc");
String b = new String("abc");
System.out.println((a == b) + " " + a.equals(b) + " " + ("abc" == "abc"));
```
Output: `false true true`. `==` compares references; `new` makes two objects. `equals` compares content. Identical literals share one object from the string pool.

### 7. Integer cache (Java)
```java
Integer a = 127, b = 127, c = 128, d = 128;
System.out.println((a == b) + " " + (c == d));
```
Output: `true false`. Autoboxing uses `Integer.valueOf`, which caches -128..127, so a and b are the same object; 128 creates new objects. Compare boxed values with equals.

### 8. Short-circuit evaluation (C)
```c
int a = 0, b = 1;
if (a && ++a) { }
if (b || ++b) { }
printf("%d %d", a, b);
```
Output: `0 1`. `&&` stops at the first false operand; `||` stops at the first true one, so the increments never run.

### 9. Integer division and modulus
```c
printf("%d %d %d", 5/2, -7/2, -7%2);
```
Output (C, Java): `2 -3 -1`. Division truncates toward zero; the sign of `%` follows the dividend. In Python, `5//2 = 2`, `-7//2 = -4`, `-7 % 2 = 1` (floor division, the sign follows the divisor).

### 10. Floating point equality (Python)
```python
print(0.1 + 0.2 == 0.3, 0.1 + 0.2)
```
Output: `False 0.30000000000000004`. Binary floating point cannot represent 0.1 or 0.2 exactly. Compare with a tolerance (`math.isclose`) instead of `==`.
