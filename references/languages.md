# Language Fundamentals Reference -- Java, Python, C++

---

# JAVA

## Memory Model
| Area | Holds | Notes |
|---|---|---|
| Stack | Frames, local primitives, references | Per thread; StackOverflowError on deep recursion |
| Heap | All objects, arrays | Shared; GC managed; OutOfMemoryError |
| Metaspace | Class metadata | Native memory (replaced PermGen in Java 8) |
| String pool | Interned String literals | Lives on heap since Java 7 |

- JDK = JRE + dev tools (javac, jdb). JRE = JVM + core libraries. JVM runs bytecode (JIT compiles hot code).
- GC: reachability-based. Generational: Young (Eden + S0/S1, minor GC) -> Old (major/full GC). Collectors: Serial, Parallel, G1 (default since Java 9), ZGC.
- Java is always pass-by-value (references are passed by value).

## Key Gotchas
- `new String("a") != "a"`; `intern()` returns the pooled instance.
- Integer cache: `Integer a=127,b=127; a==b` true; 128 -> false.
- Override `equals` => must override `hashCode`.
- `finally` runs even after return; skipped only on System.exit or JVM crash.
- Modifying a collection while iterating => ConcurrentModificationException (fail-fast).
- Generics are invariant: `List<Object>` is not a supertype of `List<String>`.

## Q&A
**Q: JVM vs JRE vs JDK?** JVM executes bytecode; JRE = JVM + libraries to run; JDK = JRE + compiler and tools to develop.

**Q: Stack vs heap?** Stack: per-thread, LIFO frames, auto freed on method exit, fast. Heap: shared, objects, reclaimed by GC.

**Q: How does GC work?** Finds objects unreachable from GC roots (thread stacks, statics) and reclaims them. Generational hypothesis: most objects die young, so minor GCs on Young are cheap. Cannot be forced; System.gc() is only a hint.

**Q: Why is String immutable?** Enables the string pool, thread safety, safe use as HashMap keys (hash cached), and security (class names, paths). Use StringBuilder (not thread safe) or StringBuffer (synchronized) for mutation.

**Q: == vs equals?** `==` compares references (values for primitives). `equals` compares logical content if overridden; default is `==`.

**Q: hashCode/equals contract?** Equal objects must have equal hashCodes; same object must return a consistent hashCode; unequal objects may collide. Breaking it makes HashMap/HashSet lookups fail.

**Q: HashMap internals?** Array of buckets (default 16). index = (n-1) & hash (hash is spread by h ^ h>>>16). Collisions chain in a linked list; when a bucket reaches 8 nodes and table size >= 64, it treeifies into a red-black tree (O(log n)); untreeifies at 6. Resizes (doubles) when size > load factor 0.75 * capacity. Average O(1) get/put. Allows one null key. Not thread safe.

**Q: ArrayList vs LinkedList?** ArrayList: dynamic array, O(1) get, amortized O(1) append, O(n) middle insert, cache friendly. LinkedList: doubly linked, O(n) get, O(1) insert/delete given the node; more memory. ArrayList is usually faster in practice.

**Q: HashMap vs ConcurrentHashMap?** HashMap is unsynchronized and allows null key/values. ConcurrentHashMap is thread safe (CAS plus per-bucket synchronized in Java 8+, not one global lock), allows no null keys/values, and iterators are weakly consistent. Hashtable locks the whole map.

**Q: Abstract class vs interface?** Abstract: state, constructors, any access modifiers, single inheritance. Interface: contract, multiple implementation, fields are public static final; default/static/private methods since Java 8/9. Use abstract for shared base state, interface for capability.

**Q: Checked vs unchecked exceptions?** Checked (Exception minus RuntimeException, e.g. IOException): compiler forces handle or declare. Unchecked (RuntimeException, Error): not enforced; usually programming bugs (NPE, IndexOutOfBounds).

**Q: final vs finally vs finalize?** final: constant variable / non-overridable method / non-extendable class. finally: block that always runs after try. finalize: Object method called before GC; deprecated (since 9, for removal), use try-with-resources/Cleaner.

**Q: Generics and type erasure?** Generic types are checked at compile time then erased to bounds (Object) in bytecode; casts inserted. Hence no `new T()`, no `List<int>`, no `instanceof List<String>`; overloads differing only in type args clash.

**Q: Multithreading basics?**
- Lifecycle: NEW -> RUNNABLE -> (BLOCKED / WAITING / TIMED_WAITING) -> TERMINATED.
- `synchronized`: mutual exclusion plus visibility (monitor lock on object/class). `volatile`: visibility and ordering only, not atomicity (`count++` still unsafe; use AtomicInteger).
- `ExecutorService`: thread pool (`Executors.newFixedThreadPool`), submit Runnable/Callable, returns Future; call shutdown(). Prefer over raw threads.
- `start()` creates a new thread; `run()` just calls on the current thread. wait/notify need the monitor held.
- Deadlock needs: mutual exclusion, hold and wait, no preemption, circular wait.

**Q: Java 8 features?** Lambdas (functional interface implementations), method references, Streams (lazy pipeline: intermediate filter/map/sorted, terminal collect/reduce/forEach; single use; parallelStream uses ForkJoin common pool), Optional (container to avoid null: map, orElse, orElseGet, ifPresent; not for fields/params), default methods, java.time.

---

# PYTHON

## Memory Model
- Everything is an object; variables are names bound to objects (references). Assignment never copies.
- CPython memory: private heap, reference counting plus a cyclic garbage collector (generational) for cycles. `del` removes a name, not necessarily the object.
- Small ints (-5..256) and some strings are interned/cached.
- Immutable: int, float, str, tuple, frozenset, bytes. Mutable: list, dict, set, bytearray, user objects.

## Key Gotchas
- Mutable default argument: `def f(x, l=[])` shares one list across calls. Fix: `l=None` then `l = [] if l is None else l`.
- `[[0]*3]*3` makes 3 references to the same inner list; use a comprehension.
- Late-binding closures in loops (`lambda: i`); bind with default arg `lambda i=i: i`.
- A tuple holding a list is still mutable inside; tuples are hashable only if all items are.
- `a += b` on lists mutates in place; on tuples/strings rebinds.

## Q&A
**Q: Mutable vs immutable?** Mutable objects change in place with the same id; immutable ones cannot, so "changes" create new objects. Only hashable (immutable) objects can be dict keys/set items.

**Q: List vs tuple?** List: mutable, dynamic, more memory. Tuple: immutable, hashable if elements are, slightly faster/smaller, used for fixed records and dict keys.

**Q: How is dict implemented?** Hash table with open addressing (compact layout with a separate entries array). Average O(1) get/set/delete. Insertion order guaranteed from Python 3.7 (CPython 3.6 implementation detail). Keys must be hashable.

**Q: What is the GIL?** Global Interpreter Lock: only one thread executes Python bytecode at a time in CPython, protecting reference counts. CPU-bound threads gain nothing; use multiprocessing. I/O-bound work is fine with threads or asyncio (GIL is released during blocking I/O). Free-threaded builds exist from 3.13 (experimental).

**Q: Shallow vs deep copy?** Shallow (`copy.copy`, `list[:]`, `.copy()`) copies the container but shares nested objects. Deep (`copy.deepcopy`) recursively copies everything.

**Q: Generators vs iterators?** Iterator implements `__iter__` and `__next__`. A generator function uses `yield` and returns an iterator that lazily produces values and keeps its state; O(1) memory vs building a list. Generator expression: `(x*x for x in r)`.

**Q: What is a decorator?** A callable that takes a function and returns a replacement, applied with `@`. Use `functools.wraps` to preserve metadata. Uses: logging, caching (`lru_cache`), auth, timing.

**Q: *args and **kwargs?** `*args` collects extra positional args into a tuple; `**kwargs` collects extra keyword args into a dict. At call sites they unpack sequences/dicts.

**Q: is vs ==?** `is` tests identity (same object); `==` tests equality (`__eq__`). Use `is None`. `a=256;b=256` is True but unreliable for big ints/strings.

**Q: List comprehension?** `[x*x for x in data if x%2==0]`: concise, usually faster than an append loop; the loop variable does not leak in Python 3. Also dict/set comprehensions.

**Q: How is memory managed?** Reference counting frees objects at count 0 immediately; the cyclic GC (`gc` module) collects reference cycles; pymalloc handles small-object allocation.

**Q: Python's time complexity cheat?** list append O(1) amortized, insert(0) O(n), `in` list O(n), `in` set/dict O(1) average, sort O(n log n) (Timsort, stable), deque popleft O(1).

---

# C++

## Memory Model
| Area | Holds | Lifetime |
|---|---|---|
| Stack | Locals, call frames | Auto, scope-based |
| Heap (free store) | `new`/`malloc` memory | Manual until delete/free |
| Static/global | Globals, statics | Program duration |
| Code | Instructions, constants | Program duration |

- No GC. RAII: tie resource lifetime to object lifetime (destructor releases).
- Undefined behavior: dangling pointers, double delete, out-of-bounds, use after free, uninitialized reads.

## Key Gotchas
- Mismatch `new[]` with `delete` (needs `delete[]`); never mix new/free or malloc/delete.
- Base class destructor must be virtual if deleted via base pointer.
- Object slicing when passing derived by value to a base parameter.
- Virtual calls in constructors/destructors do not dispatch to derived.
- Returning a reference/pointer to a local is dangling.
- `map[key]` inserts a default element if missing; use `find`/`count`.
- vector reallocation invalidates iterators/pointers/references.

## Q&A
**Q: Pointer vs reference?** Pointer: holds an address, can be null, reassignable, supports arithmetic. Reference: alias, must be initialized, cannot be reseated, no null. Prefer references for params; pointers when optional/reseatable.

**Q: new/delete vs malloc/free?** `new` allocates and calls the constructor, throws bad_alloc, returns a typed pointer; `delete` calls the destructor. `malloc` only allocates raw bytes, returns void* (NULL on failure); `free` does no destruction. malloc is a library function; new is an operator and can be overloaded.

**Q: Stack vs heap?** Stack: fast, automatic, limited size (stack overflow). Heap: flexible size/lifetime, slower, manual (or smart-pointer) management, can leak or fragment.

**Q: Virtual functions and vtable?** A virtual function is resolved at runtime. Each class with virtuals has a vtable (array of function pointers); each object holds a hidden vptr to its class's vtable. Calls via base pointer go through the vptr. Pure virtual (`= 0`) makes the class abstract.

**Q: Constructors/destructors?** Constructor initializes (default, parameterized, copy, move); use initializer lists (required for const/reference members and base classes). Destructor cleans up; order: construction base -> members -> derived, destruction in reverse.

**Q: Rule of three/five/zero?** If you define any of destructor, copy constructor, copy assignment, you likely need all three (rule of three). C++11 adds move constructor and move assignment (rule of five). Rule of zero: use RAII members (vector, smart pointers) and define none.

**Q: Smart pointers?** `unique_ptr`: sole ownership, move-only, zero overhead. `shared_ptr`: reference-counted shared ownership (control block; thread safe count). `weak_ptr`: non-owning observer, breaks shared_ptr cycles. Prefer `make_unique`/`make_shared`; avoid raw owning pointers.

**Q: STL containers and complexity?**
| Container | Structure | Access | Insert/Erase | Find |
|---|---|---|---|---|
| vector | dynamic array | O(1) | O(1) amort. at end, O(n) middle | O(n) |
| deque | chunked array | O(1) | O(1) both ends | O(n) |
| list | doubly linked | O(n) | O(1) at iterator | O(n) |
| map / set | red-black tree, sorted | - | O(log n) | O(log n) |
| unordered_map / set | hash table | - | O(1) avg, O(n) worst | O(1) avg |
| priority_queue | binary heap (max by default) | top O(1) | push/pop O(log n) | - |
- Use `greater<>` for a min-heap. Use map when ordered iteration is needed.

**Q: const correctness?** `const int* p` (data const), `int* const p` (pointer const), `const` member function promises not to modify the object; pass big args as `const T&`; const objects can call only const methods. Catches bugs at compile time.

**Q: Memory leaks and how to avoid them?** Allocated memory never freed (lost pointer, missing delete, exception before delete). Avoid via RAII, smart pointers, containers; detect with Valgrind or AddressSanitizer.

**Q: Templates basics?** Compile-time generic code: `template<typename T> T mx(T a, T b)`. Instantiated per type (no runtime cost, larger binary); supports class templates, specialization, and non-type params. Errors appear at instantiation. Definitions usually live in headers.

**Q: Virtual destructor why?** Deleting a derived object through a base pointer without a virtual destructor is undefined behavior (derived part not destroyed).
