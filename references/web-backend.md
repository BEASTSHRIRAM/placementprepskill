# Web and Backend Reference -- Development Fundamentals

## 1. REST vs GraphQL vs gRPC

| Feature | REST | GraphQL | gRPC |
|---|---|---|---|
| Style | Resources + HTTP verbs | Single endpoint, client-defined query | RPC over HTTP/2, Protocol Buffers |
| Payload | JSON (usually) | JSON | Binary (protobuf) |
| Over/under-fetching | Common | Solved (client picks fields) | Fixed by message schema |
| Caching | Easy (HTTP caching) | Harder (mostly POST) | Manual |
| Best for | Public APIs, CRUD | Many clients with varied data needs, mobile | Internal microservice calls, streaming, low latency |

**Q: When would you pick GraphQL over REST?**
A: When clients need different shapes of data and multiple round trips hurt (mobile, dashboards). Cost: harder caching, N+1 resolver problem, query-complexity limits needed.

**Q: Why is gRPC fast?**
A: Binary protobuf is smaller and faster to parse than JSON, and HTTP/2 gives multiplexing and streaming. Browsers cannot call it directly without a proxy (gRPC-Web).

**Q: What makes an API RESTful?**
A: Client-server, stateless requests, cacheable responses, uniform interface (resources identified by URIs, standard verbs), layered system.

---

## 2. HTTP Methods, Idempotency, Status Codes

| Method | Use | Safe | Idempotent |
|---|---|---|---|
| GET | Read | Yes | Yes |
| POST | Create / action | No | No |
| PUT | Replace whole resource | No | Yes |
| PATCH | Partial update | No | Not guaranteed |
| DELETE | Remove | No | Yes |
| HEAD / OPTIONS | Metadata / allowed methods (CORS preflight) | Yes | Yes |

Idempotent = repeating the call gives the same server state as calling once. Safe = does not modify state.

| Code | Meaning |
|---|---|
| 200 / 201 / 204 | OK / Created / No Content |
| 301 / 302 / 304 | Moved permanently / Found (temp redirect) / Not Modified |
| 400 / 401 / 403 / 404 | Bad request / Unauthenticated / Forbidden / Not found |
| 409 / 422 / 429 | Conflict / Unprocessable / Too many requests |
| 500 / 502 / 503 / 504 | Server error / Bad gateway / Unavailable / Gateway timeout |

**Q: PUT vs PATCH?** A: PUT replaces the entire resource; PATCH sends only changed fields.

**Q: 401 vs 403?** A: 401 = not authenticated (who are you?). 403 = authenticated but not allowed.

**Q: Is POST idempotent? How do you make payments safe to retry?** A: No. Use an idempotency key sent by the client; the server stores the result per key and returns it on retries.

**Q: HTTP vs HTTPS?** A: HTTPS is HTTP over TLS: encryption, integrity, server authentication via certificates.

---

## 3. Authentication vs Authorization

- Authentication (AuthN): verify identity (login). Authorization (AuthZ): decide what that identity may do (roles, permissions: RBAC, ABAC).
- Order: AuthN first, then AuthZ.

### Sessions vs JWT vs OAuth2

| | Session | JWT | OAuth2 |
|---|---|---|---|
| State | Server stores session, client holds session ID cookie | Stateless; signed token holds claims | Delegated-access framework |
| Revocation | Easy (delete session) | Hard until expiry (needs denylist) | Revoke tokens at auth server |
| Scaling | Needs shared store (Redis) | Any server can verify | Separate auth server |

- JWT = header.payload.signature (base64url). Signed, not encrypted: do not put secrets in it. Verify signature and `exp`.
- Pattern: short-lived access token + long-lived refresh token (store refresh in HttpOnly cookie).
- OAuth2 Authorization Code flow (with PKCE for public clients): app redirects to provider, user consents, app gets a code, exchanges it for an access token. OAuth2 is authorization; OpenID Connect adds authentication (ID token) on top.

**Q: Why use "Login with Google"?** A: OAuth2/OIDC: app never sees the user's password, gets scoped tokens.

**Q: JWT downsides?** A: Cannot be revoked easily, larger than session IDs, risky if stored in localStorage (XSS).

**Q: Where to store tokens in a browser?** A: HttpOnly + Secure + SameSite cookie is safest against XSS; localStorage is readable by any injected script.

---

## 4. Web Security Basics

- **Cookies**: small data set by server (`Set-Cookie`), sent on each request. Flags: `HttpOnly` (no JS access), `Secure` (HTTPS only), `SameSite` (Strict/Lax/None), `Expires/Max-Age`.
- **CORS**: browser enforces same-origin policy (same scheme+host+port). Server opts in to cross-origin access via `Access-Control-Allow-Origin` etc. Non-simple requests trigger an OPTIONS preflight. CORS is browser-enforced; it does not protect your server from curl.
- **CSRF**: attacker site makes the victim's browser send an authenticated request (cookies attached automatically). Fix: SameSite cookies, CSRF tokens, check Origin header.
- **XSS**: attacker injects script that runs in victim's page (stored, reflected, DOM-based). Fix: output encoding/escaping, Content-Security-Policy, avoid `innerHTML`, HttpOnly cookies.
- **SQL injection**: user input concatenated into SQL. Fix: parameterized queries / prepared statements, ORMs, least-privilege DB user, input validation.

### Password hashing
- Never store plaintext or fast hashes (MD5, SHA-256 alone). Use slow, salted, adaptive hashes: bcrypt, scrypt, Argon2.
- Salt = unique random value per password; defeats rainbow tables. Hashing is one-way; encryption is reversible.

**Q: CSRF vs XSS?** A: CSRF abuses the server's trust in the browser's cookies; XSS abuses the browser's trust in the site by running attacker code. XSS can defeat CSRF tokens.

**Q: Why is CORS error shown when the request actually reached the server?** A: The server processed it, but the browser blocked the response for lacking the allow headers.

**Q: Why bcrypt over SHA-256?** A: SHA-256 is fast, so brute force is cheap; bcrypt has a tunable cost factor and built-in salt.

---

## 5. SQL vs NoSQL and ORMs

| | SQL (Postgres, MySQL) | NoSQL |
|---|---|---|
| Model | Tables, fixed schema, joins | Document (MongoDB), key-value (Redis), wide-column (Cassandra), graph (Neo4j) |
| Consistency | ACID | Often BASE / eventual (tunable) |
| Scaling | Vertical first, sharding is harder | Designed for horizontal scale |
| Use when | Relational data, transactions, complex queries | Flexible schema, huge scale, simple access patterns, caching |

- ACID: Atomicity, Consistency, Isolation, Durability. CAP: under a network partition choose consistency or availability.
- Indexes speed reads (B-tree) but slow writes and use space. Avoid N+1 queries (use joins/eager loading).
- **ORM** (Hibernate, Sequelize, Prisma, SQLAlchemy): maps tables to objects. Pros: productivity, injection safety, migrations. Cons: hidden inefficient queries, leaky abstraction on complex queries.

**Q: When pick MongoDB over MySQL?** A: Evolving or nested document-shaped data with few cross-document joins. For banking/orders needing multi-row transactions, prefer SQL.

**Q: What is the N+1 problem?** A: 1 query for a list plus N queries for each item's relation. Fix with join/prefetch.

**Q: Does NoSQL mean no ACID?** A: No. MongoDB supports multi-document transactions; the tradeoff is performance and design style.

---

## 6. REST API Design Best Practices

- Nouns for resources, plural, hierarchy: `GET /users/42/orders`. Verbs come from HTTP method, not URL.
- **Pagination**: offset/limit (simple, slow on deep pages, unstable under inserts) vs cursor/keyset (fast, stable; `?after=<id>&limit=20`).
- **Versioning**: URL (`/v1/users`), header, or media type. Do not break existing clients.
- **Rate limiting**: protect from abuse; return 429 with `Retry-After`. Algorithms: token bucket, leaky bucket, fixed/sliding window. Often enforced at gateway using Redis.
- Consistent error body (code, message), filtering/sorting via query params, validation, HTTPS, auth on every endpoint, idempotency for retries, OpenAPI docs.

**Q: Offset vs cursor pagination?** A: Cursor is O(log n) with an index and consistent while data changes; offset scans and skips rows.

**Q: How would you rate-limit per user?** A: Key by user ID or IP in Redis, token bucket with atomic increments and TTL.

**Q: Where does a new field go without breaking clients?** A: Adding optional fields is backward compatible; removing/renaming needs a new version.

---

## 7. Caching and Redis

- Redis: in-memory key-value store with strings, hashes, lists, sets, sorted sets, TTL, pub/sub. Single-threaded command execution, persistence via RDB snapshots / AOF.
- Uses: caching, sessions, rate limiting, leaderboards (sorted sets), queues, locks.
- Patterns: cache-aside, write-through, write-back. Eviction: LRU/LFU/TTL. Layers: browser, CDN, app cache, DB cache.
- Problems: stale data; **cache stampede** (many misses at once: use locking/jittered TTL); **penetration** (keys that never exist: cache nulls, bloom filter); **avalanche** (mass expiry: stagger TTLs).

**Q: Why is Redis fast?** A: Data in RAM, simple data structures, efficient I/O multiplexing, no disk on read path.

**Q: How do you keep cache and DB consistent?** A: TTL plus invalidate/update on write; perfect consistency is not guaranteed, so accept bounded staleness.

**Q: Redis vs Memcached?** A: Redis has rich types, persistence, replication; Memcached is simple multi-threaded string cache.

---

## 8. Message Queues (Overview)

- Decouple producers from consumers; absorb traffic spikes; enable async work (emails, video processing) and retries.
- **RabbitMQ**: broker with exchanges/queues, routing, acks; message removed after consumption. Good for task queues.
- **Kafka**: distributed append-only log; topics split into partitions; consumers track offsets in consumer groups; messages retained and replayable; ordering guaranteed per partition. Good for event streaming, high throughput.
- Delivery: at-most-once, at-least-once (common; make consumers idempotent), exactly-once (hard, limited).
- Dead-letter queue holds messages that repeatedly fail.

**Q: Kafka vs RabbitMQ?** A: Kafka = durable replayable log for streams at scale; RabbitMQ = smart broker routing messages to workers, deleted once acked.

**Q: How do you handle duplicate messages?** A: Idempotent consumers (dedupe by message ID).

**Q: Why partitions?** A: Parallelism: each partition is consumed by one consumer in a group; order only within a partition.

---

## 9. Docker, CI/CD

| | Container (Docker) | VM |
|---|---|---|
| Isolation | Process-level, shares host kernel | Full guest OS on hypervisor |
| Size/startup | MBs, seconds | GBs, minutes |
| Use | Packaging apps, microservices | Strong isolation, different OS kernels |

- Image = read-only template built from a Dockerfile (layered); container = running instance. Registry (Docker Hub) stores images. Docker Compose runs multi-container setups. Kubernetes orchestrates containers (scaling, healing, rollout).
- Data in containers is ephemeral: use volumes.
- **CI** (Continuous Integration): merge often, automatically build + test each commit. **CD**: Delivery (deploy-ready, manual release) or Deployment (auto to production). Tools: GitHub Actions, Jenkins, GitLab CI. Strategies: rolling, blue-green, canary.

**Q: Why Docker?** A: Same environment from dev to prod ("works on my machine" solved), lightweight, fast deploys.

**Q: CMD vs ENTRYPOINT?** A: ENTRYPOINT is the fixed executable; CMD gives default arguments, overridable at `docker run`.

**Q: Blue-green vs canary?** A: Blue-green switches all traffic between two full environments; canary shifts a small percent first and watches metrics.

---

## 10. Basic Linux Commands

| Task | Commands |
|---|---|
| Navigate/list | `pwd`, `ls -la`, `cd` |
| Files | `cp`, `mv`, `rm -r`, `mkdir -p`, `touch`, `cat`, `less`, `head`, `tail -f` |
| Search | `grep -rn "text" .`, `find . -name "*.log"` |
| Permissions | `chmod 755 f`, `chown user f` (rwx = 4,2,1 for owner/group/others) |
| Processes | `ps aux`, `top`, `kill -9 PID`, `bg`, `fg` |
| Network | `curl`, `ping`, `netstat -tulpn` / `ss`, `ssh` |
| Disk/system | `df -h`, `du -sh`, `free -m` |
| Pipes | `cmd1 | cmd2`, `>` overwrite, `>>` append, `2>&1`, `xargs` |

**Q: What does chmod 644 mean?** A: Owner rw, group r, others r.

**Q: How to find the process using port 8080?** A: `lsof -i :8080` or `ss -tulpn | grep 8080`.

**Q: Hard link vs soft link?** A: Hard link = another name for same inode; soft (symbolic) link = a path pointer that can dangle.

**Q: Count lines containing "ERROR" in a log?** A: `grep -c ERROR app.log`.

---

## 11. What Happens When You Type a URL

1. Browser checks cache, then DNS resolution (browser/OS cache, resolver, root, TLD, authoritative) gives IP.
2. TCP 3-way handshake; TLS handshake for HTTPS.
3. Browser sends HTTP request; may pass CDN, load balancer, reverse proxy, app server, DB.
4. Server returns response (status, headers, HTML).
5. Rendering: parse HTML to DOM, CSS to CSSOM, combine into render tree, layout (reflow), paint, composite. JS blocks parsing unless `async`/`defer`; further resources (CSS, JS, images) fetched.

**Q: Reflow vs repaint?** A: Reflow recalculates geometry/layout (expensive); repaint redraws pixels without layout change. Reflow always triggers repaint.

**Q: `async` vs `defer`?** A: Both download in parallel; `async` runs as soon as ready (any order), `defer` runs after HTML parsing, in order.

**Q: What does a CDN do?** A: Serves static content from edge servers near the user, cutting latency and origin load.

---

## 12. Frontend Basics (JS and React)

**var / let / const**: `var` is function-scoped, hoisted (initialized as undefined), redeclarable. `let`/`const` are block-scoped, hoisted but in temporal dead zone until declaration. `const` forbids reassignment, not mutation.

**== vs ===**: `==` coerces types (`0 == "0"` true, `null == undefined` true); `===` compares type and value. Prefer `===`.

**Closure**: a function that remembers variables from its enclosing scope even after that scope returns. Used for private state, callbacks, currying. Classic bug: `var` in a loop with setTimeout prints the final value; `let` fixes it (new binding per iteration).

**Event loop**: JS is single-threaded. Call stack runs sync code; async callbacks wait in queues. After the stack empties, all microtasks (promise `.then`, `queueMicrotask`) run before the next macrotask (`setTimeout`, I/O, events).

**Promises / async-await**: a Promise is pending, fulfilled or rejected. `async` functions return promises; `await` pauses the function (not the thread) until resolved; use try/catch. `Promise.all` fails fast; `allSettled` waits for all.

**React**
- Virtual DOM: in-memory tree; on state change React builds a new tree, diffs it against the previous (reconciliation, `key` props identify list items), and updates only changed real DOM nodes.
- Hooks: `useState` (state), `useEffect` (side effects; dependency array controls re-run; return cleanup), `useRef` (mutable value, DOM ref), `useMemo`/`useCallback` (memoize), `useContext`. Rules: call at top level, only in components/custom hooks.
- Props flow down (read-only); state is local and triggers re-render. Controlled input = value driven by state.

**Q: Output of `console.log(1); setTimeout(()=>console.log(2),0); Promise.resolve().then(()=>console.log(3)); console.log(4);`?**
A: 1, 4, 3, 2 (microtask before macrotask).

**Q: Why do lists need keys in React?** A: Stable identity lets the diff reorder/update items correctly instead of re-creating them.

**Q: `this` in arrow vs normal functions?** A: Arrow functions capture `this` lexically; normal functions get `this` from how they are called.

**Q: Is the Virtual DOM always faster?** A: Not always; it makes updates declarative and batched, with acceptable cost. Direct DOM can beat it when hand-tuned.
