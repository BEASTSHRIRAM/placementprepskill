# Core CS Reference -- COA, Compiler Design, TOC, Discrete Math

## 1. Computer Organization and Architecture

**Number systems**
- n-bit unsigned range: 0 to 2^n - 1. n-bit 2's complement range: -2^(n-1) to 2^(n-1) - 1.
- 2's complement negate: invert bits, add 1. Single zero, add/subtract use the same adder.
- Overflow (signed add): both operands same sign but result has different sign.
- Sign-magnitude and 1's complement have two zeros.

**Floating point (IEEE 754)**

| Format | Sign | Exponent | Mantissa | Bias |
|---|---|---|---|---|
| Single (32-bit) | 1 | 8 | 23 | 127 |
| Double (64-bit) | 1 | 11 | 52 | 1023 |

Value = (-1)^s x 1.mantissa x 2^(exp - bias) for normalized numbers. Exponent all 1s: Infinity (mantissa 0) or NaN. Exponent all 0s: zero or denormal. 0.1 cannot be stored exactly in binary, so 0.1 + 0.2 != 0.3.

**Endianness**: Little-endian stores least significant byte at the lowest address (x86, most ARM setups). Big-endian stores most significant byte first (network byte order).

**RISC vs CISC**

| Aspect | RISC | CISC |
|---|---|---|
| Instructions | Few, simple, fixed length | Many, complex, variable length |
| Memory access | Load/store only | Many instructions access memory |
| Registers | Many | Fewer |
| Control | Hardwired | Often microprogrammed |
| Pipelining | Easy | Harder |
| Examples | ARM, RISC-V, MIPS | x86 |

**Pipelining**
- Classic 5 stages: IF, ID, EX, MEM, WB.
- Ideal speedup = number of stages k. Time for n instructions = (k + n - 1) cycles.
- Hazards:
  - Structural: two instructions need same hardware. Fix: duplicate resources.
  - Data: RAW (true dependency), WAR, WAW. Fix: forwarding, stalls (bubbles), compiler scheduling. Load-use hazard still needs 1 stall.
  - Control: branches. Fix: branch prediction, delayed branch, flush.

**Memory hierarchy**: registers -> L1 -> L2 -> L3 -> RAM -> SSD/disk. Faster means smaller, costlier, closer to CPU. Works due to temporal and spatial locality.

**Cache**
- Mapping: Direct (block maps to exactly one line: index = block mod lines), Fully associative (any line, needs comparing all tags), Set-associative (k-way: block maps to one set, any line in it).
- Address split: tag | index (set) | block offset.
- Replacement: LRU, FIFO, random. Misses: compulsory, capacity, conflict.
- Write policies: write-through (write to cache and memory, simple, slower) vs write-back (write only cache, dirty bit, write on eviction). On write miss: write-allocate or no-write-allocate.
- Formulas:
  - Hit ratio = hits / accesses
  - AMAT = hit time + miss rate x miss penalty
  - Multi-level: AMAT = L1 hit + L1 miss rate x (L2 hit + L2 miss rate x memory penalty)
  - Number of sets = cache size / (block size x associativity)

**Interrupts and DMA**
- Interrupt: hardware signal making CPU save state and run an ISR. Maskable vs non-maskable. Vectored interrupts use a table of ISR addresses.
- I/O modes: Programmed I/O (CPU polls, wasteful), interrupt-driven, DMA (controller moves block between device and memory directly, CPU interrupted only when done; cycle stealing shares the bus).

**Amdahl's law**: Speedup = 1 / ((1 - f) + f / s), f = fraction enhanced, s = speedup of that part. Max speedup (s infinite) = 1 / (1 - f). CPU time = instruction count x CPI x clock cycle time.

**Common interview questions (COA)**
1. Q: Why is 2's complement used? A: One zero, simple hardware, same adder for signed and unsigned.
2. Q: What is a pipeline hazard and how is it handled? A: A condition preventing the next instruction from executing in its cycle. Structural, data, control. Handled with forwarding, stalls, branch prediction.
3. Q: Direct vs set-associative cache? A: Direct is fast and cheap but has conflict misses. Set-associative reduces conflicts at cost of more comparators and complexity.
4. Q: Write-through vs write-back? A: Write-through keeps memory consistent but generates more bus traffic. Write-back is faster, uses dirty bit, memory can be stale.
5. Q: Why does cache work? A: Locality of reference, temporal and spatial.
6. Q: What is DMA and why use it? A: Hardware controller transfers data to memory without CPU per-byte work, freeing the CPU.
7. Q: Compute AMAT for hit 1 ns, miss rate 5%, penalty 100 ns. A: 1 + 0.05 x 100 = 6 ns.
8. Q: 40% of a program is parallelizable on 4 cores? A: Speedup = 1 / (0.6 + 0.4/4) = 1.43.

---

## 2. Compiler Design

**Phases**

| Phase | Input -> Output | Notes |
|---|---|---|
| Lexical analysis | chars -> tokens | Regex/DFA, removes whitespace and comments |
| Syntax analysis | tokens -> parse tree/AST | Uses a CFG, reports syntax errors |
| Semantic analysis | AST -> annotated AST | Type checking, scope, declared-before-use |
| Intermediate code | AST -> IR | Three-address code, machine independent |
| Optimization | IR -> better IR | Machine independent and dependent |
| Code generation | IR -> target code | Instruction selection, register allocation |

The symbol table (names, types, scope, addresses) and error handler are used by all phases. Front end = lexer, parser, semantic, IR. Back end = optimization and codegen.

**Lexer vs parser**: lexer groups characters into tokens (identifier, keyword, number) using regular languages. Parser checks token sequence against grammar structure (nesting, precedence) using context-free grammars. Regular languages cannot match nested parentheses, hence the split.

**LL vs LR**

| Aspect | LL(1) (top-down) | LR (bottom-up) |
|---|---|---|
| Scan / derivation | Left-to-right, leftmost derivation | Left-to-right, reverse rightmost derivation |
| Builds tree | From root | From leaves |
| Power | Weaker | Stronger, handles more grammars |
| Grammar issues | No left recursion, needs left factoring | Handles left recursion |
| Variants | Recursive descent, predictive | LR(0), SLR, LALR, CLR |
| Tools | Hand-written, ANTLR | yacc, bison (LALR) |

Power order: LR(0) < SLR < LALR < CLR(1).

**FIRST and FOLLOW**
- FIRST(A): set of terminals that can begin a string derived from A (include epsilon if A derives epsilon).
- FOLLOW(A): set of terminals that can appear immediately after A in some derivation. $ is in FOLLOW of the start symbol.
- Used to build the LL(1) parsing table: for A -> alpha, put it under each terminal in FIRST(alpha); if alpha derives epsilon, also under FOLLOW(A).

**Compiler vs interpreter vs JIT**
- Compiler: translates the whole program to machine code ahead of time. Fast execution, errors reported up front (C, C++, Go).
- Interpreter: executes source/bytecode line by line. Slower, easy to debug (early Python, shell).
- JIT: compiles hot code to native code at runtime using profiling (JVM HotSpot, V8). Startup cost, then near-native speed.

**Common optimizations**: constant folding, constant propagation, common subexpression elimination, dead code elimination, loop-invariant code motion, strength reduction (x*2 -> x<<1), function inlining, loop unrolling, peephole optimization.

**Common interview questions (Compiler)**
1. Q: Name compiler phases. A: Lexical, syntax, semantic, IR generation, optimization, code generation.
2. Q: Why separate lexer from parser? A: Simpler design, regular vs context-free power, faster tokenizing, portability.
3. Q: What is ambiguity in a grammar? A: More than one parse tree for a string, for example dangling else. Fix by rewriting or precedence rules.
4. Q: Why is LR stronger than LL? A: LR decides after seeing the full right side of a production, LL must predict early with limited lookahead.
5. Q: What does the symbol table store? A: Identifier name, type, scope, memory location, and so on.
6. Q: Compiler vs interpreter? A: Whole-program translation ahead of time vs executing step by step.
7. Q: What is a three-address code? A: IR where each instruction has at most one operator and three addresses, such as t1 = a + b.
8. Q: What is JIT? A: Runtime compilation of frequently executed code to native machine code.

---

## 3. Theory of Computation

**Automata**
- DFA: exactly one transition per state and symbol. NFA: multiple or epsilon transitions allowed. NFA and DFA recognize the same languages (subset construction; DFA can have up to 2^n states).
- Regular expressions = DFA = NFA in power (Kleene's theorem). Operations: union, concatenation, star.
- Regular languages are closed under union, intersection, complement, concatenation, star.
- Minimal DFA is unique. Min states found by partitioning equivalent states.
- CFG: productions A -> string. PDA = finite automaton + stack. Nondeterministic PDA = CFG in power; DPDA is strictly weaker.
- Turing machine: finite control + infinite tape, read/write/move L or R. Models what is computable (Church-Turing thesis).

**Chomsky hierarchy**

| Type | Grammar | Language | Machine | Example |
|---|---|---|---|---|
| 3 | Regular | Regular | DFA/NFA | a*b |
| 2 | Context-free | CFL | PDA | a^n b^n |
| 1 | Context-sensitive | CSL | Linear bounded automaton | a^n b^n c^n |
| 0 | Unrestricted | Recursively enumerable | Turing machine | Halting-type languages |

Each type is a proper subset of the one above it.

**Pumping lemma (regular) idea**: for a regular language, any long enough string w (length >= p) splits into xyz with |xy| <= p, |y| >= 1, and x y^i z in L for all i >= 0. Used to prove non-regularity by contradiction (a^n b^n is not regular). It cannot prove a language is regular.

**Decidability**
- Decidable: a TM always halts with yes/no. Recognizable (RE): TM halts on yes, may loop on no.
- Halting problem: no TM can decide, for every program and input, whether it halts (proof by diagonalization). It is recognizable but not decidable. Rice's theorem: any non-trivial semantic property of programs is undecidable.

**P vs NP**
- P: solvable in polynomial time. NP: solution verifiable in polynomial time (equivalently, solvable by a nondeterministic TM in polynomial time). P is a subset of NP; whether P = NP is open.
- NP-hard: at least as hard as every NP problem. NP-complete: in NP and NP-hard. Proof: show it is in NP and reduce a known NP-complete problem to it in polynomial time.
- First NP-complete problem: SAT (Cook-Levin theorem).
- NP-complete examples: 3-SAT, Clique, Vertex Cover, Hamiltonian Cycle, Subset Sum, 0/1 Knapsack (decision), Graph 3-Coloring, TSP (decision). 2-SAT, shortest path, MST are in P. The halting problem is NP-hard but not in NP.

**Common interview questions (TOC)**
1. Q: DFA vs NFA? A: DFA has one deterministic move; NFA can branch. Same expressive power, NFA can be exponentially smaller.
2. Q: Can a regex match balanced parentheses? A: No, it needs unbounded memory; use a PDA/CFG.
3. Q: Why is a^n b^n not regular? A: Pumping y inside the a's breaks the count equality.
4. Q: What is the halting problem? A: Deciding if a program halts on given input; proven undecidable.
5. Q: Define P, NP, NP-complete. A: See above; NPC problems are the hardest in NP.
6. Q: If one NP-complete problem is solved in polynomial time? A: Then P = NP.
7. Q: Which machine recognizes context-free languages? A: Pushdown automaton.
8. Q: Is every decidable language also recognizable? A: Yes, decidable is a subset of recognizable.

---

## 4. Discrete Math and Digital Logic (short)

**Logic gates**: AND, OR, NOT, NAND, NOR, XOR, XNOR. NAND and NOR are universal (any circuit can be built from just one). De Morgan: (A.B)' = A' + B', (A+B)' = A'.B'. Half adder: sum = A xor B, carry = A.B. Full adder: sum = A xor B xor Cin.
- Combinational circuits (no memory): adder, mux, decoder, encoder. Sequential (has state): latch, flip-flop (SR, D, JK, T), counter, register.
- K-map: grid with Gray-code ordering (adjacent cells differ by one bit). Group 1s in powers of two (1, 2, 4, 8) to minimize SOP; larger groups mean fewer literals. Don't-cares can be used in groups.

**Combinatorics**
- Permutations P(n,r) = n!/(n-r)!. Combinations C(n,r) = n!/(r!(n-r)!).
- Binomial: (a+b)^n = sum C(n,k) a^(n-k) b^k. Total subsets of n-set = 2^n.
- Inclusion-exclusion: |A U B| = |A| + |B| - |A n B|.
- Pigeonhole: placing n+1 items into n boxes means some box has at least 2. Generalized: some box has at least ceil(m/n) of m items.

**Graph theory basics**
- Handshake lemma: sum of degrees = 2|E|. Tree with n nodes has n-1 edges. Complete graph K_n has n(n-1)/2 edges.
- Bipartite iff no odd cycle. Euler circuit iff connected with all degrees even. Euler path iff exactly 0 or 2 odd-degree vertices.
- Planar graph (Euler's formula): V - E + F = 2 for connected planar graphs.

**Modular arithmetic**: a = b (mod n) means n divides (a - b). (a+b) mod n and (a*b) mod n can be taken term by term. Modular inverse of a mod n exists iff gcd(a, n) = 1 (Extended Euclid). Fermat: a^(p-1) = 1 (mod p) for prime p not dividing a. gcd(a,b) = gcd(b, a mod b).

**Common interview questions (Discrete / Logic)**
1. Q: Why are NAND and NOR universal? A: Each can build NOT, AND and OR.
2. Q: Combinational vs sequential circuit? A: Output depends only on current inputs vs on inputs and stored state.
3. Q: Why does a K-map use Gray code? A: So adjacent cells differ in one variable and can be merged.
4. Q: Number of ways to choose 3 from 5? A: C(5,3) = 10.
5. Q: Among 13 people, must two share a birth month? A: Yes, 13 people into 12 months (pigeonhole).
6. Q: Can a graph have an odd number of odd-degree vertices? A: No, by the handshake lemma.
7. Q: Compute 2^10 mod 7. A: 2^3 = 8 = 1 (mod 7), so 2^10 = 2^9 x 2 = 2 (mod 7).
8. Q: Edges in a tree with 10 nodes? A: 9.
