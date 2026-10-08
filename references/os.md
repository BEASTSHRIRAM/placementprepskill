# OS Reference -- Operating Systems

## Process vs Thread

| Aspect | Process | Thread |
|---|---|---|
| Definition | Program in execution | Smallest unit of execution within a process |
| Memory | Separate memory space | Shares memory space with other threads in process |
| Communication | IPC (pipes, sockets, shared memory) | Direct sharing of variables |
| Creation cost | High (fork) | Low |
| Crash impact | One process crash does not affect others | One thread crash can crash the whole process |
| Context switch | Expensive | Cheaper |

**Multithreading vs Multiprocessing**
Multithreading: multiple threads in one process, share memory, good for I/O bound tasks.
Multiprocessing: multiple processes, separate memory, good for CPU bound tasks, true parallelism on multi-core.

---

## CPU Scheduling Algorithms

**FCFS (First Come First Serve)**
Non-preemptive. Simple but can cause convoy effect (short jobs wait behind long jobs).

**SJF (Shortest Job First)**
Non-preemptive or preemptive (SRTF). Optimal average waiting time but requires knowing burst time in advance.

**Round Robin**
Preemptive. Each process gets a time quantum. Fair but high context switch overhead if quantum is too small.

**Priority Scheduling**
Preemptive or non-preemptive. Can cause starvation of low-priority processes. Solved by aging (gradually increasing priority of waiting processes).

**Multilevel Queue Scheduling**
Different queues for different process types (foreground, background). Fixed priority between queues.

**Metrics**
- Turnaround Time = Completion Time minus Arrival Time
- Waiting Time = Turnaround Time minus Burst Time
- Response Time = First CPU Time minus Arrival Time
- Throughput = Number of processes completed per unit time

---

## Process Synchronization

**Race Condition**: multiple threads access shared data concurrently and outcome depends on execution order.

**Critical Section Problem**: only one process in the critical section at a time.
Requirements: Mutual Exclusion, Progress, Bounded Waiting

**Mutex (Mutual Exclusion Lock)**
Binary lock. Only the thread that locked it can unlock it.

**Semaphore**
Counter variable. wait() decrements, signal() increments.
- Binary Semaphore: works like a mutex but any thread can signal
- Counting Semaphore: controls access to a resource pool of n instances

**Monitor**
High-level synchronization construct. Methods are mutually exclusive. Condition variables (wait, signal) coordinate threads.

**Classic Synchronization Problems**
- Producer-Consumer: producer adds to buffer, consumer removes. Buffer has fixed size.
- Readers-Writers: multiple readers OK simultaneously, writer needs exclusive access.
- Dining Philosophers: 5 philosophers, 5 forks, must pick up both adjacent forks to eat. Deadlock if all pick left fork simultaneously.

---

## Deadlock

**Four Necessary Conditions (Coffman Conditions)**
1. Mutual Exclusion: resource held by one process at a time
2. Hold and Wait: process holds a resource while waiting for another
3. No Preemption: resources cannot be forcibly taken
4. Circular Wait: cycle in resource allocation graph

**Deadlock Prevention**: negate one of the four conditions
**Deadlock Avoidance**: Banker's Algorithm -- grant request only if system remains in safe state
**Deadlock Detection and Recovery**: allow deadlock, detect via resource allocation graph, recover by killing process or preempting resources
**Deadlock Ignorance**: (Ostrich Algorithm) pretend it does not happen. Used by most OS for rare cases.

---

## Memory Management

**Contiguous Allocation**
Memory divided into fixed or variable partitions.
Fragmentation: External (gaps between allocated blocks), Internal (wasted space within allocated block).

**Paging**
Physical memory divided into frames, logical memory into pages of same size.
No external fragmentation. Internal fragmentation possible.
Page Table maps page numbers to frame numbers.
TLB (Translation Lookaside Buffer): cache for page table entries, speeds up translation.

**Segmentation**
Memory divided into variable-size logical segments (code, data, stack).
External fragmentation possible.

**Virtual Memory**
Allows execution of processes not fully in memory. Uses disk as extension of RAM.
Demand Paging: load page only when needed.
Page Fault: referenced page not in memory, OS loads it from disk.

**Page Replacement Algorithms**
- FIFO: replace oldest page. Simple but Belady's Anomaly (more frames can cause more faults).
- LRU: replace least recently used. No Belady's Anomaly. Expensive to implement exactly.
- Optimal: replace page not used for longest time in future. Theoretical benchmark.

---

## File Systems

**File Allocation Methods**
- Contiguous: fast sequential access, external fragmentation
- Linked: no fragmentation, poor random access
- Indexed: uses index block, good random access, overhead for small files

**Directory Structures**: Single-level, Two-level, Tree, Acyclic Graph, General Graph

**Disk Scheduling Algorithms**
- FCFS: service requests in order of arrival
- SSTF (Shortest Seek Time First): service nearest request, can cause starvation
- SCAN (Elevator): head moves in one direction servicing requests, then reverses
- C-SCAN (Circular SCAN): head moves in one direction only, jumps back to start

---

## Common Interview Questions

1. What is the difference between kernel mode and user mode?
2. What is a context switch? What is saved/restored?
3. What is thrashing? How is it caused and prevented?
4. What is the difference between internal and external fragmentation?
5. Explain the working of fork() in Unix.
6. What is a zombie process? An orphan process?
7. What is the purpose of the OS scheduler?
8. How does the TLB improve memory access performance?
9. What is a system call? Give examples.
10. What is the difference between preemptive and non-preemptive scheduling?


---

## Advanced Topics and Interview Q Bank

### Processes: fork/exec/wait, zombie vs orphan
- fork(): clones the caller. Returns 0 in child, child PID in parent, -1 on error. Copy-on-write makes it cheap.
- exec*(): replaces the current process image with a new program (same PID). Code after a successful exec never runs.
- wait()/waitpid(): parent blocks until a child exits and reads its exit status (reaps it).
- Typical shell: fork -> child exec(cmd) -> parent wait.
- Zombie: child has exited but parent has not called wait(); only the PCB entry (PID, exit status) remains. Fix: parent calls wait, handles SIGCHLD, or parent dies (init reaps).
- Orphan: parent exits first while child still runs; child is adopted by init/systemd (PID 1) which reaps it. Orphans are harmless; many zombies exhaust the PID table.
- n sequential fork() calls (no conditions) create 2^n - 1 child processes (2^n total).

### System calls, kernel vs user mode
- System call: controlled entry from user code into the kernel (open, read, write, fork, exec, mmap, socket). Library wrappers (libc) load the syscall number into a register and execute a trap instruction (int 0x80 / syscall / svc).
- Flow: user code -> wrapper -> trap -> mode bit switches to kernel -> dispatch via syscall table -> run -> return to user mode.
- User mode: restricted, cannot run privileged instructions (I/O, page table changes, halt). Kernel mode: full hardware access. Mode bit in CPU status register. Illegal action in user mode -> trap/exception.
- Mode switch (user<->kernel) is cheaper than a full context switch (no change of address space needed).

### Context switch steps
1. Interrupt/trap or yield occurs; CPU enters kernel mode.
2. Save running process state (PC, registers, stack pointer, flags) into its PCB.
3. Set its state (ready/blocked); put it on the proper queue.
4. Scheduler picks next process.
5. Load the next PCB's registers/PC; switch page table (flush TLB unless ASID-tagged).
6. Return to user mode and resume. Pure overhead: no useful work done. Thread switch in same process skips the address-space switch.

### IPC mechanisms
| Mechanism | Direction | Notes |
|---|---|---|
| Pipe (anonymous) | Half-duplex byte stream | Related processes (parent/child), kernel buffer |
| Named pipe (FIFO) | Half-duplex | Unrelated processes, has a filesystem name |
| Message queue | Message oriented | Kernel-managed, typed messages, async |
| Shared memory | Both | Fastest (no copy after setup), needs explicit sync |
| Semaphore | Signaling | Synchronization, not data transfer |
| Signal | One-way, tiny | Async notification (SIGINT, SIGKILL, SIGCHLD) |
| Socket | Both, local or network | Unix domain or TCP/UDP; works across machines |

### Synchronization with semaphores
**Producer-Consumer (bounded buffer of size N)**
```
semaphore mutex = 1, empty = N, full = 0;
producer: wait(empty); wait(mutex); add item; signal(mutex); signal(full);
consumer: wait(full);  wait(mutex); remove item; signal(mutex); signal(empty);
```
Swapping wait(empty) and wait(mutex) in the producer can deadlock (holds mutex while buffer full).

**Readers-Writers (readers preference)**
```
semaphore rw = 1, mutex = 1; int readcount = 0;
reader: wait(mutex); if (++readcount == 1) wait(rw); signal(mutex);
        read;
        wait(mutex); if (--readcount == 0) signal(rw); signal(mutex);
writer: wait(rw); write; signal(rw);
```
Readers preference can starve writers; writers preference can starve readers.

**Dining Philosophers (5)**: naive "pick left then right" deadlocks. Fixes: allow at most 4 to sit (semaphore of 4); pick both forks atomically (under a mutex); asymmetric order (odd picks left first, even picks right first); resource ordering (always lower-numbered fork first); or monitor with states THINKING/HUNGRY/EATING.

### Mutex vs semaphore vs monitor vs spinlock
| | Mutex | Semaphore | Monitor | Spinlock |
|---|---|---|---|---|
| Value | locked/unlocked | integer >= 0 | language construct | flag |
| Ownership | owner must unlock | none (any thread can signal) | implicit (one thread inside) | owner |
| Waiting | sleeps (blocked) | sleeps | sleeps on condition variables | busy-waits (burns CPU) |
| Use | protect critical section | resource counting, signaling | encapsulated shared object | very short critical sections, multiprocessor, kernel/interrupt context |

Spinlock is bad on a single CPU (spinner blocks the lock holder). Condition variable: wait() releases the monitor lock and sleeps atomically; always re-check the condition in a while loop (spurious wakeups).

### Race condition and critical section
- Race condition example: counter++ is load, add, store; two threads can both load 5 and both store 6 (lost update).
- Critical section solution must satisfy: (1) Mutual Exclusion, (2) Progress (decision of who enters cannot be postponed indefinitely, only processes wanting in take part), (3) Bounded Waiting (limit on how many times others enter after a request). No assumption about relative speeds.
- Peterson's solution (2 processes): flag[i]=true; turn=j; while(flag[j] && turn==j); CS; flag[i]=false. Software only; satisfies all three. Hardware: test-and-set, compare-and-swap.

### Banker's algorithm (worked example)
5 processes, resource types A,B,C with totals 10, 5, 7.

| Proc | Allocation A B C | Max A B C | Need = Max - Alloc |
|---|---|---|---|
| P0 | 0 1 0 | 7 5 3 | 7 4 3 |
| P1 | 2 0 0 | 3 2 2 | 1 2 2 |
| P2 | 3 0 2 | 9 0 2 | 6 0 0 |
| P3 | 2 1 1 | 2 2 2 | 0 1 1 |
| P4 | 0 0 2 | 4 3 3 | 4 3 1 |

Allocated totals = 7, 2, 5 so Available = (10,5,7) - (7,2,5) = (3,3,2).
Safety check (find process with Need <= Work, then Work += its Allocation):
- P1: (1,2,2) <= (3,3,2) -> Work = (5,3,2)
- P3: (0,1,1) <= (5,3,2) -> Work = (7,4,3)
- P4: (4,3,1) <= (7,4,3) -> Work = (7,4,5)
- P0: (7,4,3) <= (7,4,5) -> Work = (7,5,5)
- P2: (6,0,0) <= (7,5,5) -> Work = (10,5,7)

Safe sequence: <P1, P3, P4, P0, P2> (not unique).
Resource request: P1 requests (1,0,2). Check Request <= Need (1,2,2) yes; Request <= Available (3,3,2) yes. Pretend grant: Available = (2,3,0), P1 Alloc = (3,0,2), P1 Need = (0,2,0). Safety rerun succeeds (P1, P3, P4, P0, P2 again), so the request is granted. Unsafe state does not mean deadlock, only that deadlock is possible.

### Page replacement (worked example, 3 frames)
Reference string: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1 (20 references)

| Algorithm | Page faults | Hit ratio |
|---|---|---|
| FIFO | 15 | 5/20 = 25% |
| LRU | 12 | 8/20 = 40% |
| Optimal | 9 | 11/20 = 55% |

Trace start (FIFO): 7, 7 0, 7 0 1 (3 faults); ref 2 evicts 7 -> [2 0 1]; ref 0 hit; ref 3 evicts 0 -> [2 3 1]; ref 0 evicts 1 -> [2 3 0] ...
Belady's anomaly with FIFO, string 1 2 3 4 1 2 5 1 2 3 4 5: 3 frames -> 9 faults, 4 frames -> 10 faults. LRU and Optimal are stack algorithms (no anomaly).
Approximations of LRU: reference bit, second chance (clock), NRU, aging.

### Thrashing
CPU spends more time paging than executing. Cause: too many processes, each with too few frames; page fault rate rises, CPU utilization drops, OS (wrongly) admits more processes, making it worse. Fixes: reduce multiprogramming degree (swap out processes), working-set model (give each process its working set of recent pages), page-fault-frequency control (add frames if fault rate above upper bound, remove if below lower bound), local replacement, more RAM.

### TLB and effective access time
EAT with TLB = h*(t_tlb + t_mem) + (1-h)*(t_tlb + 2*t_mem) for single-level page table.
Example: h = 90%, t_tlb = 10 ns, t_mem = 100 ns: EAT = 0.9*110 + 0.1*210 = 99 + 21 = 120 ns.
(If TLB lookup time is ignored: h*t_mem + (1-h)*2*t_mem = 110 ns.) With n-level paging a miss costs n memory accesses for translation plus 1 for data.
Context switch needs TLB flush unless entries carry ASID/PID tags.

### Virtual memory and demand paging
- Process is split into pages; only needed pages are loaded. Valid/invalid bit in each page table entry says whether page is in memory.
- Page fault steps: (1) trap to OS, (2) check reference legal else terminate, (3) find free frame (else run replacement, write victim back if dirty bit set), (4) schedule disk read, (5) update page table and valid bit, (6) restart the faulting instruction.
- EAT with faults = (1-p)*t_mem + p*t_fault. Example: t_mem = 200 ns, t_fault = 8 ms = 8,000,000 ns, p = 0.001: EAT = 0.999*200 + 0.001*8,000,000 = 199.8 + 8000 = 8199.8 ns (about 41x slowdown).
- Benefits: programs larger than RAM, higher multiprogramming, copy-on-write, shared libraries.

### Disk scheduling (worked example)
Request queue: 98, 183, 37, 122, 14, 124, 65, 67. Head at 53, cylinders 0-199.

| Algorithm | Service order | Total head movement |
|---|---|---|
| FCFS | 98,183,37,122,14,124,65,67 | 45+85+146+85+108+110+59+2 = 640 |
| SSTF | 65,67,37,14,98,122,124,183 | 12+2+30+23+84+24+2+59 = 236 |
| SCAN (toward 0 first) | 37,14,(0),65,67,98,122,124,183 | 53 + 183 = 236 |
| C-SCAN (moving up) | 65,67,98,122,124,183,(199),(0),14,37 | 146 up to 199, +199 return jump, +37 = 382 (183 if return jump not counted) |

LOOK/C-LOOK are like SCAN/C-SCAN but reverse at the last request instead of the disk end. SSTF can starve far requests. C-SCAN gives more uniform wait times. SSDs do not need seek-based scheduling.

### inode vs FAT
| | inode (Unix/ext) | FAT |
|---|---|---|
| Metadata | Per-file inode: owner, perms, size, timestamps, block pointers (no name) | Directory entry holds name, attrs, first cluster |
| Block map | 12 direct + single/double/triple indirect pointers | Single File Allocation Table of next-cluster links (linked allocation) |
| Random access | Good (index) | Poor unless FAT cached in memory |
| Hard links | Yes (names map to inode number) | No |
| Max file size | Large (4 KB blocks, 4-byte ptrs: 12 + 1K + 1M + 1G blocks) | Limited by FAT width (FAT32: 4 GB - 1) |

Directory in Unix = table of (name, inode number). Hard link = another name for same inode; symbolic link = file holding a path.

### 15 more tricky Q&As
1. Does fork() copy the whole address space? No, copy-on-write: pages copied lazily on first write.
2. What does `fork(); fork(); printf("x");` print? "x" 4 times (2^2 processes).
3. Can a zombie be killed with kill -9? No, it is already dead; only the parent reaping (or parent's death) removes it.
4. Mutex vs binary semaphore? Mutex has ownership (and often priority inheritance); binary semaphore is a signaling tool anyone can release.
5. What is priority inversion? Low-priority holder blocks a high-priority waiter while a medium one preempts the holder. Fix: priority inheritance (Mars Pathfinder).
6. Why is SJF optimal for average waiting time? Running shorter jobs first reduces the number of jobs waiting behind long ones (exchange argument). SRTF is the preemptive version.
7. Round Robin with quantum -> infinity? Becomes FCFS. Quantum -> 0? Overhead dominates. Rule of thumb: ~80% of bursts shorter than the quantum.
8. Paging vs segmentation? Paging: fixed size, invisible to programmer, no external fragmentation. Segmentation: variable, logical view, external fragmentation.
9. Page size trade-off? Large: smaller page table, more internal fragmentation. Small: bigger page table, less internal fragmentation. Optimal size ~ sqrt(2*s*e) (s = avg process size, e = bytes per page table entry).
10. Page table size for 32-bit address, 4 KB pages, 4-byte entry? 2^20 entries * 4 B = 4 MB per process. Hence multi-level or inverted page tables.
11. Deadlock vs starvation? Deadlock: set of processes all waiting on each other forever. Starvation: one process waits indefinitely while others progress (fix by aging).
12. Deadlock detection via RAG: single instance per resource -> cycle is necessary and sufficient. Multiple instances -> cycle is necessary only.
13. Semaphore initial value 0 used for? Ordering/signaling (B runs only after A signals). Initial value n: n concurrent users.
14. Process vs thread stack/heap? Each thread has own stack and registers; threads share heap, globals, code, open files.
15. Address bits: logical address 13 bits, page size 1 KB -> 3 bits page number (8 pages), 10 bits offset. Internal fragmentation fix: smaller units; external fragmentation fix: compaction or paging.
