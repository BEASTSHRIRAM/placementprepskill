# Low Level Design (LLD) Problems Reference

Pattern and SOLID theory lives in oops.md. This file is the applied playbook: how to run the round and 10 classic problems.

## How to Run an LLD Round (6 steps, ~45 min)

1. **Clarify requirements (5 min)** - Ask scope questions, list 4-6 functional requirements, state what is out of scope (payments, UI, persistence). Ask: single or multi-threaded? In-memory ok? Extensibility axes?
2. **Identify entities (5 min)** - Underline nouns in the requirements: these are classes/enums. Verbs become methods. Separate entities (data) from services/managers (behaviour).
3. **Relationships** - Decide HAS-A (composition/aggregation), IS-A, and 1:1 / 1:N / M:N. Prefer composition. Decide who owns what (e.g. Floor owns Spots).
4. **Patterns** - Apply a pattern only where a requirement varies: Strategy (swappable algorithm), Factory (create by type), Observer (notify many), State (behaviour depends on state), Singleton (one manager; mention testability cost). Justify each in one line.
5. **Class skeleton (15 min)** - Write interfaces, enums, fields, key method signatures. Code the core flow (park, book, move) fully; stub the rest. Keep fields private, depend on interfaces.
6. **Extend / edge cases (10 min)** - Walk one happy path, then edge cases (invalid input, full, not found), then concurrency, then the follow-ups: "how would you add X without modifying existing classes?"

Tips: speak your trade-offs aloud, do not over-pattern, name things from the domain, use enums not strings, and use IDs/maps for O(1) lookup.

---

## 1. Parking Lot

**Requirements**
- Multi-floor lot with spots of types (MOTORCYCLE, COMPACT, LARGE)
- Entry issues a ticket; exit computes fee and frees the spot
- Vehicle fits a spot by type compatibility
- Pricing per hour, varying by vehicle type
- Show availability; reject entry when full

**Classes**
- `Vehicle` (abstract; plate, VehicleType) with Car, Bike, Truck
- `ParkingSpot` (id, SpotType, isFree, vehicle) - park/unpark
- `ParkingFloor` - spots, findSpot(VehicleType)
- `Ticket` (id, vehicle, spot, entryTime)
- `ParkingLot` - floors, activeTickets map; `park()`, `unpark()`
- `SpotAllocationStrategy` - nearest-first, lowest-floor, etc.
- `PricingStrategy` - hourly, flat, per-vehicle-type

**Patterns**: Strategy (allocation and pricing vary independently), Factory (VehicleFactory), Singleton (ParkingLot instance, optional).

```java
enum VehicleType { MOTORCYCLE, CAR, TRUCK }
interface PricingStrategy { double fee(Ticket t, Instant exit); }
interface SpotAllocationStrategy { Optional<ParkingSpot> find(List<ParkingFloor> f, VehicleType t); }

class ParkingSpot {
    private final String id; private final SpotType type; private Vehicle vehicle;
    synchronized boolean tryPark(Vehicle v) { if (vehicle != null) return false; vehicle = v; return true; }
    synchronized void free() { vehicle = null; }
}
class ParkingLot {
    private final List<ParkingFloor> floors;
    private final Map<String, Ticket> active = new ConcurrentHashMap<>();
    private final SpotAllocationStrategy allocator; private final PricingStrategy pricing;
    Ticket park(Vehicle v);                 // find spot, tryPark, issue ticket
    double unpark(String ticketId);         // fee = pricing.fee(...), free spot, remove ticket
}
```

**Concurrency/edge**: two cars racing for one spot -> atomic tryPark (CAS/synchronized) and retry next spot. Lost ticket, duplicate plate already inside, lot full, spot-type fallback (bike in compact).

**Follow-ups**: (1) Add EV charging spots without touching ParkingLot? (2) Add multiple entry/exit gates and display boards (Observer)? (3) Dynamic/peak pricing?

---

## 2. Elevator System

**Requirements**
- N elevators, M floors; hall calls (UP/DOWN) and in-car floor requests
- Dispatcher assigns a request to the best elevator
- Elevator moves, stops at requested floors, handles direction
- Door open/close, overload and emergency stop
- Minimise wait time

**Classes**
- `Elevator` (id, currentFloor, Direction, ElevatorState, stop sets)
- `Direction` enum UP, DOWN, IDLE
- `Request` (floor, Direction)
- `ElevatorController` / dispatcher - `submit(Request)`
- `SchedulingStrategy` - picks elevator (nearest, SCAN-based)
- `ElevatorState` - Idle, MovingUp, MovingDown, DoorOpen, Maintenance

**Patterns**: Strategy (scheduling: nearest-car vs SCAN/LOOK), State (behaviour per state), Observer (floor displays), Command (requests as objects, optional).

```java
enum Direction { UP, DOWN, IDLE }
interface SchedulingStrategy { Elevator pick(List<Elevator> cars, Request r); }

class Elevator {
    private int floor; private Direction dir = Direction.IDLE;
    private final TreeSet<Integer> upStops = new TreeSet<>(), downStops = new TreeSet<>();
    synchronized void addStop(int f);          // route into up/down set by direction
    void step();                               // move one floor; SCAN: finish dir, then reverse
}
class ElevatorController {
    private final List<Elevator> cars; private final SchedulingStrategy strategy;
    void requestPickup(int floor, Direction d) { strategy.pick(cars, new Request(floor, d)).addStop(floor); }
    void selectFloor(int carId, int floor);
}
```

**Concurrency/edge**: requests arrive while moving (thread-safe stop sets, one thread per car); same floor requested twice (sets dedupe); overload -> refuse, door stays open; request for current floor; car in maintenance excluded from dispatch.

**Follow-ups**: (1) Add priority (VIP/fire mode)? (2) Zoned elevators (express to floors 20+)? (3) Why SCAN over FCFS?

---

## 3. LRU Cache

**Requirements**
- get(key) and put(key, value) in O(1)
- Fixed capacity; evict least recently used on overflow
- Both get and put count as a "use"
- Thread-safe version on request
- Generic keys/values

**Classes**
- `Node` (key, value, prev, next) - doubly linked list node
- `LRUCache` - HashMap key->Node plus doubly linked list with dummy head/tail
- `EvictionPolicy<K>` interface (to generalise to LFU/FIFO)

**Patterns**: Strategy (pluggable eviction policy), Decorator/proxy (thread-safe wrapper). Core is a data-structure choice: hashmap for lookup + DLL for O(1) reorder and removal.

```python
class Node:
    def __init__(self, k=0, v=0): self.k, self.v, self.prev, self.next = k, v, None, None

class LRUCache:
    def __init__(self, capacity):
        self.cap, self.map = capacity, {}
        self.head, self.tail = Node(), Node()       # dummy sentinels
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, n): n.prev.next, n.next.prev = n.next, n.prev
    def _add_front(self, n):
        n.next, n.prev = self.head.next, self.head
        self.head.next.prev = n; self.head.next = n

    def get(self, key):
        if key not in self.map: return -1
        n = self.map[key]; self._remove(n); self._add_front(n); return n.v

    def put(self, key, value):
        if key in self.map: self._remove(self.map[key])
        elif len(self.map) == self.cap:
            lru = self.tail.prev; self._remove(lru); del self.map[lru.k]
        self.map[key] = n = Node(key, value); self._add_front(n)
```

**Concurrency/edge**: get mutates order, so even reads need a lock (use one mutex, or ReentrantLock; striped locks break global ordering). Capacity 0/1, updating existing key must not evict, storing the key in the node is needed to delete from the map on eviction. Java shortcut: `LinkedHashMap(cap, 0.75f, true)` with `removeEldestEntry`.

**Follow-ups**: (1) Convert to LFU in O(1)? (2) Add TTL expiry? (3) Make it distributed (consistent hashing, see system-design.md)?

---

## 4. Tic-Tac-Toe

**Requirements**
- N x N board, two players alternate, marks X and O
- Win = full row, column or diagonal; draw when board is full
- Reject move to an occupied or out-of-range cell
- Game status: IN_PROGRESS, WON, DRAW
- Extensible: N x N, K-in-a-row, more players, bot player

**Classes**
- `Board` (cells[][], size) - place(), isFull()
- `Cell`/`Symbol` enum X, O, EMPTY
- `Player` (name, Symbol) - interface with `nextMove(Board)` (human/bot)
- `Game` - players queue, board, status; `makeMove(r, c)`
- `WinningStrategy` - row/col/diagonal checkers

**Patterns**: Strategy (win-check rules; bot difficulty), State (game status, optional), Factory (player creation).

```java
enum Symbol { X, O }
enum GameStatus { IN_PROGRESS, WON, DRAW }
interface WinningStrategy { boolean isWin(Board b, Move last); }

class Game {
    private final Board board; private final Deque<Player> turns = new ArrayDeque<>();
    private final List<WinningStrategy> rules; private GameStatus status = GameStatus.IN_PROGRESS;
    GameStatus makeMove(int r, int c) {
        if (status != GameStatus.IN_PROGRESS) throw new IllegalStateException("over");
        Player p = turns.peekFirst();
        board.place(r, c, p.symbol());                  // throws if occupied/out of range
        if (rules.stream().anyMatch(w -> w.isWin(board, new Move(r, c, p)))) return status = GameStatus.WON;
        if (board.isFull()) return status = GameStatus.DRAW;
        turns.addLast(turns.pollFirst()); return status;
    }
}
```

**Concurrency/edge**: O(1) win check using per-row/col counters (+1 for X, -1 for O, win when |count| == N) plus 2 diagonal counters; moves after game over; wrong player's turn (online play -> lock per game).

**Follow-ups**: (1) Add undo? (Command + move stack) (2) Computer opponent with minimax? (3) 3+ players or K-in-a-row on large board?

---

## 5. BookMyShow (Movie Ticket Booking)

**Requirements**
- Browse cities, theatres, movies, shows
- Each show has a seat map; user selects seats and books
- No double booking under concurrent users
- Hold seats temporarily (e.g. 5 min) during payment; release on timeout
- Booking confirmation and cancellation

**Classes**
- `Movie`, `Theatre` (city), `Screen`, `Show` (movie, screen, time)
- `Seat` (id, SeatType) and `ShowSeat` (seat, show, SeatStatus AVAILABLE/LOCKED/BOOKED)
- `User`, `Booking` (id, user, show, showSeats, BookingStatus, amount)
- `BookingService` - lockSeats, confirm, cancel
- `PaymentStrategy` (UPI, Card), `NotificationService`
- `SeatLockProvider` - lock with expiry

**Patterns**: Strategy (payment, pricing by seat type), Observer (notify user/email on booking), Facade (BookingService), Factory (payment).

```java
enum SeatStatus { AVAILABLE, LOCKED, BOOKED }
class ShowSeat {
    private SeatStatus status = SeatStatus.AVAILABLE; private Instant lockedUntil; private String lockedBy;
    synchronized boolean tryLock(String userId, Duration ttl);   // AVAILABLE or expired lock -> LOCKED
    synchronized void book(String userId);                       // only if locked by same user
}
class BookingService {
    Booking createBooking(String userId, String showId, List<String> seatIds); // lock ALL or none
    Booking confirm(String bookingId, PaymentStrategy pay);
    void cancel(String bookingId);
}
```

**Concurrency/edge**: the classic. Lock seats atomically all-or-nothing, in sorted seat-id order to avoid deadlock; rollback already-locked seats if one fails; expiry via scheduled executor or lazy check on lockedUntil; payment fails -> release; in a DB use `UPDATE ... WHERE status='AVAILABLE'` (optimistic) or `SELECT FOR UPDATE`.

**Follow-ups**: (1) Add coupons/dynamic pricing? (2) Handle 100k users hitting one hot show? (3) Refund policy by time-to-show?

---

## 6. Splitwise

**Requirements**
- Users, groups, expenses paid by one user and shared among others
- Split types: EQUAL, EXACT, PERCENT
- Track per-pair balances; show who owes whom
- Settle up between users
- Simplify debts (minimise number of transactions)

**Classes**
- `User`, `Group` (members, expenses)
- `Expense` (id, paidBy, amount, `List<Split>`, SplitType)
- `Split` (user, amount) - subclasses EqualSplit, ExactSplit, PercentSplit
- `ExpenseService` - addExpense, validate
- `BalanceSheet` - Map<User, Map<User, Double>>; getBalances, settle
- `SplitStrategy` / `ExpenseFactory`

**Patterns**: Strategy (split computation + validation), Factory (create expense by SplitType), Observer (notify members of new expense).

```java
enum SplitType { EQUAL, EXACT, PERCENT }
interface SplitStrategy { List<Split> compute(double total, List<User> users, List<Double> values); }

class ExpenseService {
    private final Map<SplitType, SplitStrategy> strategies;
    private final BalanceSheet sheet;
    Expense addExpense(User paidBy, double total, SplitType t, List<User> users, List<Double> vals) {
        List<Split> splits = strategies.get(t).compute(total, users, vals); // validates sum == total / 100%
        for (Split s : splits) if (!s.user().equals(paidBy)) sheet.owe(s.user(), paidBy, s.amount());
        return new Expense(paidBy, total, splits);
    }
}
class BalanceSheet { void owe(User from, User to, double amt); /* net opposite direction */ List<String> show(User u); }
```

**Concurrency/edge**: use `BigDecimal` or integer paise, not double; equal split remainder (100/3) goes to the first user; exact sum mismatch -> reject; payer included in splits; concurrent updates to the same pair -> lock on ordered pair. Simplify debts: compute net balance per user, then greedily match max creditor with max debtor using two heaps.

**Follow-ups**: (1) Implement debt simplification? (2) Multi-currency? (3) Undo/edit an expense?

---

## 7. Vending Machine

**Requirements**
- Slots holding products with price and quantity
- Insert coins/notes, select product, dispense, return change
- Cancel returns inserted money
- Handle out-of-stock and insufficient funds
- Admin: restock, collect cash

**Classes**
- `Product`, `Slot`/`Inventory` (code -> product, count)
- `Coin` enum (value)
- `VendingMachine` - holds current `State`, balance, inventory
- `State` interface: `insertMoney`, `selectProduct`, `dispense`, `cancel`
- States: `IdleState`, `HasMoneyState`, `DispensingState`, `OutOfServiceState`

**Patterns**: State (the textbook case; kills big if-else on status), Singleton (machine, optional), Strategy (change-making algorithm).

```java
interface State {
    void insertMoney(VendingMachine m, Coin c);
    void selectProduct(VendingMachine m, String code);
    void cancel(VendingMachine m);
}
class HasMoneyState implements State {
    public void insertMoney(VendingMachine m, Coin c) { m.addBalance(c.value()); }
    public void selectProduct(VendingMachine m, String code) {
        Slot s = m.inventory().get(code);
        if (s == null || s.isEmpty()) throw new SoldOutException(code);
        if (m.balance() < s.price()) throw new InsufficientFundsException();
        m.setState(new DispensingState()); m.dispense(code);     // then refund change, go Idle
    }
    public void cancel(VendingMachine m) { m.refund(); m.setState(new IdleState()); }
}
```

**Concurrency/edge**: single user at a time (synchronize machine methods); cannot make exact change -> refuse or ask exact coins; dispense hardware failure -> refund; invalid transitions (select in Idle) throw a clear error; keep money in integer units.

**Follow-ups**: (1) Add card/UPI payment (Strategy)? (2) Change-making with limited coin denominations (greedy vs DP)? (3) Remote monitoring of low stock (Observer)?

---

## 8. Logger / Logging Framework

**Requirements**
- Levels: DEBUG < INFO < WARN < ERROR < FATAL; filter by minimum level
- Multiple destinations (console, file, DB) simultaneously
- Configurable message format
- Thread-safe; non-blocking for callers
- Global access via getLogger

**Classes**
- `LogLevel` enum (ordered)
- `LogMessage` (timestamp, level, text, thread)
- `Logger` - level, list of appenders; `info()`, `error()`...
- `LogAppender` interface (Console, File, Db) with a `Formatter`
- `LogFormatter` interface
- Chain of handlers per level (alternative design)

**Patterns**: Singleton (LoggerManager/registry), Strategy (formatter, appender), Observer (appenders subscribe to the logger), Chain of Responsibility (level-based handlers), Factory (getLogger(name)).

```java
enum LogLevel { DEBUG, INFO, WARN, ERROR, FATAL }
interface LogAppender { void append(LogMessage m); }

class Logger {
    private volatile LogLevel min = LogLevel.INFO;
    private final List<LogAppender> appenders = new CopyOnWriteArrayList<>();
    void log(LogLevel lvl, String msg) {
        if (lvl.compareTo(min) < 0) return;                       // cheap early filter
        LogMessage m = new LogMessage(Instant.now(), lvl, msg, Thread.currentThread().getName());
        for (LogAppender a : appenders) a.append(m);
    }
    void info(String msg) { log(LogLevel.INFO, msg); }
}
class LoggerFactory { private static final Map<String, Logger> loggers = new ConcurrentHashMap<>();
    static Logger getLogger(String name) { return loggers.computeIfAbsent(name, n -> new Logger()); } }
```

**Concurrency/edge**: async logging via BlockingQueue + a single writer thread (preserves order, caller never blocks on I/O); queue full -> drop low levels or block; flush on shutdown; file rotation by size/date; appender throwing must not break others.

**Follow-ups**: (1) Add a Slack appender for ERROR only? (2) Log rotation design? (3) Lazy message building (supplier) to avoid cost when filtered?

---

## 9. Rate Limiter

**Requirements**
- Allow at most N requests per time window per client (user/IP/API key)
- Reject excess with a clear result (HTTP 429)
- Pluggable algorithm: token bucket, fixed window, sliding window
- Per-client config / tiered limits
- Thread-safe, low latency

**Classes**
- `RateLimiter` interface: `boolean allowRequest(String clientId)`
- `TokenBucketLimiter`, `FixedWindowLimiter`, `SlidingWindowLogLimiter`
- `RateLimitConfig` (capacity, refillRate/window)
- `RateLimiterFactory` - builds limiter by type
- `RateLimiterManager` - Map<clientId, limiter state>

**Patterns**: Strategy (algorithm), Factory (create by config), Singleton (manager, optional), Decorator/Filter (wrap API handler).

```java
interface RateLimiter { boolean allowRequest(String clientId); }

class TokenBucketLimiter implements RateLimiter {
    private final int capacity; private final double refillPerSec;
    private final ConcurrentHashMap<String, Bucket> buckets = new ConcurrentHashMap<>();
    private static class Bucket { double tokens; long lastRefillNanos;
        Bucket(double t, long n) { tokens = t; lastRefillNanos = n; } }
    public boolean allowRequest(String id) {
        Bucket b = buckets.computeIfAbsent(id, k -> new Bucket(capacity, System.nanoTime()));
        synchronized (b) {                                  // per-client lock, not global
            long now = System.nanoTime();
            b.tokens = Math.min(capacity, b.tokens + (now - b.lastRefillNanos) / 1e9 * refillPerSec);
            b.lastRefillNanos = now;
            if (b.tokens >= 1) { b.tokens--; return true; }
            return false;
        }
    }
}
```

**Concurrency/edge**: per-client locking (or AtomicLong/CAS) avoids a global bottleneck; use monotonic clock (nanoTime), not wall clock; memory growth from idle clients -> evict stale buckets; fixed window allows 2x burst at the boundary (sliding window fixes it); distributed: Redis with Lua script for atomic check-and-decrement (see system-design.md).

**Follow-ups**: (1) Make it distributed across servers? (2) Compare token bucket vs sliding window log vs sliding window counter (memory/accuracy)? (3) Different limits per API endpoint and per tier?

---

## 10. Library Management System

**Requirements**
- Catalog of books (many copies per title, each copy a BookItem)
- Members search by title/author/ISBN; checkout, return, renew, reserve
- Limits: max 5 books per member, 14-day loan; fine for late return
- Librarian adds/removes books and members
- Notify member when a reserved book is available or due soon

**Classes**
- `Book` (isbn, title, authors), `BookItem` (barcode, BookStatus AVAILABLE/LOANED/RESERVED/LOST)
- `Member`, `Librarian` (extend `Account`), `Catalog`
- `Loan` (bookItem, member, issueDate, dueDate, returnDate)
- `Reservation` (book, member, queue position)
- `LibraryService` - checkout, return, reserve
- `SearchStrategy`, `FineStrategy`, `NotificationObserver`

**Patterns**: Strategy (search by field, fine calculation), Observer (reservation available, due reminders), Factory (Account creation), Facade (LibraryService).

```java
enum BookStatus { AVAILABLE, LOANED, RESERVED, LOST }
interface SearchStrategy { List<Book> search(Catalog c, String query); }
interface FineStrategy { long fine(Loan loan, LocalDate returned); }

class LibraryService {
    private final Catalog catalog; private final FineStrategy fines;
    private final Map<String, Deque<Reservation>> waitlist = new HashMap<>();
    Loan checkout(Member m, String barcode);        // check limit, no unpaid fines, item AVAILABLE
    long returnItem(String barcode);                // close loan, fine, notify next reservation
    void reserve(Member m, String isbn);
}
```

**Concurrency/edge**: two members checking out the same copy -> synchronize on the BookItem or use DB row lock; member at limit; returning an item not loaned; renew blocked if reserved by someone else; lost book charges replacement cost; reservation expires if not collected.

**Follow-ups**: (1) Add e-books with unlimited copies (new BookItem subtype, check LSP)? (2) Scale to many branches? (3) Recommendation or popular-book report without changing core classes?

---

## SOLID Checklist (self-review any LLD answer)

- [ ] **S** - Does each class have one reason to change? (Parking lot should not compute fees itself; the pricing strategy does.)
- [ ] **O** - Can I add a new type (vehicle, payment, split, algorithm) by adding a class, with zero edits to existing logic? No `switch` on type in core code.
- [ ] **L** - Can every subclass replace its parent without surprises? No subclass throwing UnsupportedOperationException or weakening a contract.
- [ ] **I** - Are interfaces small and role-based? No class forced to implement methods it never uses.
- [ ] **D** - Do high-level classes depend on interfaces (Strategy, Appender, Payment), injected via constructor, not `new ConcreteClass()` inside?
- [ ] Encapsulation: fields private, invariants enforced inside the class, no leaked mutable collections.
- [ ] Composition over inheritance; inheritance only for true IS-A.
- [ ] Enums for fixed sets; no magic strings/numbers.
- [ ] Every pattern used is justified by a requirement that varies; no pattern for its own sake.
- [ ] Concurrency addressed: shared state identified, lock granularity stated, check-then-act made atomic.
- [ ] Error paths covered: invalid input, not found, capacity full, illegal state transition.
- [ ] Extensibility demonstrated: can answer "how would you add X?" by pointing at one extension point.
