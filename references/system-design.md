# System Design Reference

## How to Approach Any System Design Question

**Step 1 -- Clarify Requirements (5 minutes)**
- Functional requirements: what the system should do
- Non-functional requirements: scale, latency, availability, consistency
- Ask: How many users? Read-heavy or write-heavy? Any specific SLA?

**Step 2 -- Estimate Scale (3 minutes)**
- Daily Active Users (DAU)
- Requests per second = DAU x requests per user per day / 86400
- Storage: messages per day x average size x retention period
- Bandwidth: requests per second x average payload size

**Step 3 -- Define API**
- Sketch the core REST endpoints the system exposes
- Example for URL shortener: POST /shorten {long_url}, GET /{short_code}

**Step 4 -- High Level Design**
Draw the major components and how data flows between them:
Client -> Load Balancer -> Application Servers -> Database / Cache / Message Queue

**Step 5 -- Deep Dive into One Component**
Your interviewer will guide this. Be ready to go deep on: database schema, caching strategy, consistency model, fault tolerance.

**Step 6 -- Discuss Tradeoffs**
Every design decision has a cost. Be explicit: "I chose SQL here for strong consistency, but if write throughput becomes a bottleneck, we can switch to NoSQL or add a write buffer."

---

## Key Concepts

### Load Balancing
Distributes incoming traffic across multiple servers.
- Round Robin: requests go to servers in rotation
- Least Connections: send to server with fewest active connections
- Consistent Hashing: maps requests to servers in a way that minimizes remapping when servers are added or removed

### Caching
Stores frequently accessed data in fast memory to reduce database load and latency.

**Cache Strategies**
- Cache Aside (Lazy Loading): application checks cache first, fetches from DB on miss, writes to cache
- Write Through: write to cache and DB simultaneously
- Write Back (Write Behind): write to cache immediately, write to DB asynchronously

**Cache Eviction Policies**: LRU (most common), LFU, FIFO

**Cache Invalidation Problem**: how to keep cache in sync with DB. Hardest problem in caching.

Popular tools: Redis, Memcached

### Databases

**Sharding**: horizontal partitioning of data across multiple databases.
- Range-based: split by range of key values
- Hash-based: hash the key to determine shard
- Directory-based: lookup service maps key to shard

**Replication**: copy data to multiple nodes for availability and read scaling.
- Master-Slave: writes go to master, reads from slaves
- Master-Master: writes go to either, more complex conflict resolution

### Message Queues
Decouple producers and consumers. Allow async processing.
Use for: notifications, order processing, event-driven architectures, buffering spikes.
Tools: Kafka (high throughput, log-based), RabbitMQ (flexible routing)

### Content Delivery Network (CDN)
Caches static assets (images, CSS, JS, videos) at edge servers geographically close to users.
Reduces latency for global users. Reduces origin server load.

### Rate Limiting
Prevents abuse and protects servers from overload.
- Token Bucket: tokens accumulate at a rate, each request consumes a token
- Leaky Bucket: requests enter a fixed-size queue, processed at a constant rate
- Fixed Window Counter: count requests in a fixed time window
- Sliding Window: more accurate, avoids boundary issues of fixed window

---

## Case Studies

### URL Shortener (bit.ly)
Core challenge: generate short unique codes, redirect to long URL at high speed.
- Hash function (MD5/SHA256) + take first 7 chars, handle collision
- Database: KV store like Redis or DynamoDB for mapping
- Read-heavy: cache popular short URLs aggressively
- Custom short codes: check availability before storing

### Twitter Feed
Core challenge: fan-out on write vs fan-out on read.
- Fan-out on write: when user tweets, push to all followers' feeds immediately (good for users with few followers)
- Fan-out on read: when user opens app, pull tweets from followed accounts (good for celebrities)
- Hybrid: push for regular users, pull for celebrities
- Timeline stored in Redis sorted set (by timestamp)

### WhatsApp / Chat System
- WebSockets for real-time bidirectional communication
- Message storage: one-to-one (simple table), group (fan-out problem)
- Presence (online/offline): heartbeat mechanism
- Message ordering: Lamport timestamps or vector clocks

### Ride-Sharing (Uber)
- Location updates: drivers send GPS every few seconds
- Matching: geospatial indexing (QuadTree, Google S2) to find nearby drivers
- Pricing: surge based on demand/supply ratio
- Consistency: booking must be atomic (no double booking)

---

## Low Level Design (LLD)

LLD focuses on class diagrams, design patterns, and object-oriented modeling.
Common LLD problems:
- Design a Parking Lot
- Design an Elevator System
- Design a Chess Game
- Design an ATM
- Design a Library Management System
- Design a Hotel Booking System

**LLD Approach**
1. Identify entities (objects)
2. Define their attributes and relationships
3. Identify behaviours (methods)
4. Apply SOLID principles and relevant design patterns
5. Handle edge cases and constraints

---

## CAP Theorem

A distributed system can guarantee at most two of:
- **Consistency**: every read gets the most recent write
- **Availability**: every request gets a (non-error) response
- **Partition Tolerance**: system continues despite network partitions

In reality, partition tolerance is non-negotiable in distributed systems. So the choice is between CP and AP.
- CP systems: HBase, Zookeeper (sacrifice availability under partition)
- AP systems: Cassandra, DynamoDB, CouchDB (sacrifice consistency, use eventual consistency)

---

## More Case Studies and Concepts

### Consistent Hashing
- Place servers (and keys) on a hash ring; a key goes to the first server clockwise. Adding/removing a node remaps only about K/N keys (vs nearly all with `hash % N`).
- Virtual nodes: each server gets many ring positions to even out load and handle heterogeneous capacity.
- Used in: Dynamo, Cassandra, memcached clients, CDN/load balancers. Hot keys still need separate handling (replication, local cache).

### Sharding Strategies
- Range: easy range queries, risk of hotspots (monotonic keys like timestamps).
- Hash: even spread, bad range scans, resharding painful unless consistent hashing.
- Directory/lookup: flexible, lookup service is a SPOF/bottleneck.
- Geo/tenant based: data locality and isolation, uneven sizes.
- Costs: cross-shard joins and transactions, resharding, hot shards, global unique IDs (Snowflake IDs). Pick shard key by query pattern and cardinality.

### Replication
- Leader-follower: writes to leader, async/sync replication to followers; reads scale on followers (may be stale). Failover needs leader election; async replication can lose recent writes.
- Multi-leader: each region has a leader, low write latency, offline/multi-DC friendly; needs conflict resolution (last-write-wins, vector clocks, CRDTs).
- Leaderless (Dynamo-style): quorum W + R > N for read-your-write consistency; read repair, hinted handoff.
- Sync vs async trade-off: durability vs latency.

### SQL vs NoSQL Choice
- SQL: structured data, joins, multi-row ACID transactions, mature tooling. Scales mostly vertically + read replicas; sharding is manual.
- NoSQL: key-value (Redis, DynamoDB), document (MongoDB), wide-column (Cassandra), graph (Neo4j). Horizontal scale, flexible schema, usually weaker joins/transactions.
- Pick by access pattern: relations and consistency -> SQL; massive write scale, simple lookups, flexible schema -> NoSQL. Polyglot persistence is common.

### Indexing at Scale
- B-tree (read-heavy, range queries) vs LSM tree (write-heavy: memtable -> SSTables, compaction; used by Cassandra, RocksDB).
- Every index slows writes and uses space; use composite indexes in leftmost-prefix order, covering indexes to avoid table lookups.
- At scale: local (per-shard) indexes are cheap to write but need scatter-gather reads; global indexes read fast but writes are cross-shard. Inverted index (Elasticsearch) for text search; Bloom filters to skip disk lookups.

### ACID vs BASE
- ACID: Atomicity, Consistency (invariants), Isolation, Durability. Single-node or distributed transactions (2PC is blocking and slow).
- BASE: Basically Available, Soft state, Eventually consistent. Favors availability and scale.
- Cross-service workflows: Saga (sequence of local transactions with compensating actions) instead of 2PC.

### Eventual Consistency
- If no new writes occur, all replicas converge. Stronger useful guarantees: read-your-writes, monotonic reads, causal consistency.
- Convergence tools: read repair, anti-entropy (Merkle trees), gossip, CRDTs.
- Choose for feeds, likes, counters, catalogs; avoid for balances and checkout inventory counts.

### Idempotency and Exactly-Once
- Idempotent: repeating an operation gives the same result as doing it once. PUT/DELETE are idempotent by definition; POST needs an idempotency key.
- Pattern: client sends unique key; server stores key -> result (with TTL) and returns the stored result on retry; use a unique constraint or atomic insert to avoid races.
- Delivery: at-most-once (may lose), at-least-once (may duplicate), exactly-once = at-least-once + idempotent consumer (or transactional dedup like Kafka transactions). True exactly-once over a network is not possible; it is effectively-once.

### API Gateway
Single entry point for clients: routing, authN/authZ, rate limiting, TLS termination, request aggregation, protocol translation, caching, logging.
- Trade-offs: extra hop and potential SPOF (run it redundant), risk of logic creep. BFF (backend for frontend) pattern for per-client gateways. Examples: Kong, AWS API Gateway, Envoy.

### Service Discovery
- Services register with a registry (Consul, etcd, Eureka, ZooKeeper) with heartbeats/health checks; callers look up healthy instances.
- Client-side (client queries registry, load balances itself) vs server-side (LB/DNS does lookup; Kubernetes Services). Service mesh (Istio, Linkerd) moves it into sidecars.

### Circuit Breaker
- States: Closed (calls pass, count failures) -> Open (fail fast after threshold/timeouts) -> Half-Open (trial calls; success closes, failure reopens).
- Prevents cascading failure and retry storms. Pair with timeouts, retries with exponential backoff + jitter, bulkheads, and fallbacks. Libraries: Resilience4j (Hystrix is in maintenance mode).

### Back-of-Envelope Estimation Cheat Sheet
**Useful numbers**
- 1 day = 86,400 s (~10^5). 1M req/day ~ 12 QPS. 1B req/day ~ 12K QPS.
- Peak QPS ~ 2-3x average. Read:write ratio matters.
- Powers: 2^10 ~ 10^3 (KB), 2^20 ~ 10^6 (MB), 2^30 ~ 10^9 (GB), 2^40 ~ 10^12 (TB), 2^50 ~ 10^15 (PB).
- Latency: memory ~100 ns, SSD read ~100 us, same-DC round trip ~0.5 ms, disk seek ~10 ms, cross-continent RTT ~150 ms.
- Rough single-node capacity: web server ~1-10K QPS, DB ~1-10K QPS (simple queries), Redis ~100K QPS.
- Availability: 99.9% = ~8.8 h downtime/yr; 99.99% = ~52 min/yr.

**Formulas**
- QPS = DAU x actions per user per day / 86,400
- Storage = writes per day x object size x 365 x years x replication factor
- Bandwidth = QPS x payload size (in bits for Mbps)
- Servers = peak QPS / QPS per server (add headroom)
- Cache size ~ 20% of daily hot data (80/20 rule)

**Worked example: photo sharing app**
- 100M DAU, each uploads 0.1 photos/day and views 20 photos/day; photo = 2 MB, 5 years retention, 3x replication.
- Write QPS = 100M x 0.1 / 86,400 = 10M / 86,400 ~ 116 QPS (peak ~350).
- Read QPS = 100M x 20 / 86,400 ~ 23K QPS (peak ~70K). Read:write = 200:1, so cache + CDN.
- Storage/day = 10M x 2 MB = 20 TB; 5 years = 20 TB x 365 x 5 ~ 36.5 PB; x3 replication ~ 110 PB.
- Egress = 23K x 2 MB = 46 GB/s ~ 370 Gbps average, so CDN is mandatory (in practice smaller thumbnails are served).
- Ingress = 116 x 2 MB ~ 232 MB/s ~ 1.9 Gbps.

---

### Case Study: Notification System
**Requirements**: push, SMS, email, in-app; templating; user preferences/opt-out; scheduled and bulk sends; at-least-once with dedup; priority (OTP vs marketing).
**Estimates**: 10M users, 5 notifications/user/day = 50M/day ~ 580 QPS avg, bursts 10-50x for campaigns.
**Components**: API/event producers -> validation + preference/rate check -> priority message queues (Kafka/SQS, one per channel and priority) -> channel workers -> providers (APNs/FCM, Twilio, SES) -> delivery status store; template service, scheduler, retry + dead letter queue, analytics.
**Trade-offs**: at-least-once + idempotency key (dedup store) vs exactly-once; separate queues so marketing never blocks OTP; provider failover; per-user rate caps to avoid spam; push vs pull for in-app.
**Follow-ups**: (1) How to avoid duplicate sends on retries? (2) How to handle provider outages and throttling? (3) How to support user timezones and scheduled campaigns for 10M users?

### Case Study: Web Crawler
**Requirements**: crawl billions of pages, politeness (robots.txt, per-host rate), dedup, freshness/recrawl, extensibility (HTML, images), robustness to spider traps.
**Estimates**: 1B pages/month ~ 400 pages/s; avg 100 KB -> 100 TB/month raw; 5-year retention ~ 6 PB.
**Components**: Seed URLs -> URL Frontier (priority queues + per-host politeness queues) -> DNS resolver (cached) -> Fetcher workers -> Content parser -> Dedup (content hash/simhash) -> Storage (blob store) + link extractor -> URL filter/seen-set (Bloom filter) -> back to frontier.
**Trade-offs**: BFS vs priority (PageRank/freshness) crawl; Bloom filter saves memory but has false positives (skips some new URLs); distribute by hashing host to crawler (keeps politeness local); depth limits and URL normalization for spider traps.
**Follow-ups**: (1) How do you detect near-duplicate pages? (2) How to decide recrawl frequency? (3) How to scale the frontier and keep politeness across many machines?

### Case Study: Search Autocomplete / Typeahead
**Requirements**: top 5-10 suggestions per prefix, <100 ms latency, ranked by popularity/recency, personalisation optional.
**Estimates**: 10M DAU x 10 searches x ~5 keystroke requests ~ 500M/day ~ 6K QPS avg, peak ~12K+; store ~100M distinct queries x ~50 B ~ 5 GB (fits in memory per replica).
**Components**: Client (debounce, local cache) -> API/LB -> Suggestion service (trie with top-k cached at each node, or Redis sorted sets per prefix) -> offline pipeline (query logs -> Kafka/MapReduce aggregation -> rebuild trie periodically) -> trie snapshots pushed to serving nodes; filter service for offensive terms.
**Trade-offs**: precomputed top-k per node (fast reads, more memory) vs compute on query; rebuild hourly/daily vs real-time updates; shard by prefix (hot prefixes) vs by hash; CDN/browser caching of popular prefixes.
**Follow-ups**: (1) How to reflect trending queries quickly? (2) How to shard the trie without hot shards? (3) How to support typo tolerance and multiple languages?

### Case Study: YouTube / Netflix Video Streaming
**Requirements**: upload, process, and stream video to millions; adaptive quality; global low latency; resume playback; (recommendations usually out of scope).
**Estimates**: assume 500 hours uploaded/min = 30K hours/hour; at ~1 GB per hour of raw video ~ 720 TB/day raw uploads, times several encoded renditions; egress in Tbps, so CDN dominates cost.
**Components**: Upload service (chunked/resumable) -> blob storage -> message queue -> transcoding pipeline (DAG: split into chunks, encode multiple resolutions/codecs, thumbnails, DRM) -> store segments + manifests -> CDN edge -> player using adaptive bitrate streaming (HLS/DASH, segments of 2-10 s); metadata DB (SQL/NoSQL) + cache; view counts via async stream.
**Trade-offs**: pre-transcode all renditions (storage) vs on demand; push popular content to CDN/ISP caches (Netflix Open Connect) vs pull on miss; chunk size vs latency; eventual consistency for view counts and likes.
**Follow-ups**: (1) How does adaptive bitrate work? (2) How to make transcoding fast and fault tolerant? (3) How to reduce CDN cost for the long tail?

### Case Study: Dropbox / Google Drive
**Requirements**: upload/download, sync across devices, sharing and permissions, versioning, offline edits, large files, conflict handling.
**Estimates**: 50M users, 10 GB avg stored = 500 PB logical; 10% daily active, 2 file changes/day ~ 10M changes/day ~ 115 QPS (bursty); dedup can cut storage significantly.
**Components**: Client sync agent (watcher, chunker) -> block server (split into ~4 MB chunks, hash each, upload only new chunks) -> blob store (S3-like); metadata service/DB (file tree, chunk list, versions; SQL for transactions); notification/long-poll service pushes changes to other devices; sharing/ACL service; cold storage tiering.
**Trade-offs**: chunk-level dedup and delta sync save bandwidth but add CPU/metadata; strong consistency for metadata vs eventual for blobs; conflict policy (keep both copies, "conflicted copy") vs last-write-wins; client-side encryption blocks server dedup.
**Follow-ups**: (1) How to sync only the changed part of a large file? (2) How to resolve edit conflicts? (3) How to handle sharing a folder with millions of users?

### Case Study: Distributed Cache
**Requirements**: low-latency get/put (<1 ms), horizontally scalable, highly available, TTL and eviction, configurable consistency.
**Estimates**: 1M QPS, 100 GB data, 1 KB avg value -> ~100M keys; each node ~ 100K QPS and 32 GB -> ~10 nodes + replicas.
**Components**: Clients with consistent hashing (or proxy / cluster slot map like Redis Cluster's 16384 slots) -> cache nodes (hash map + LRU doubly linked list) -> replicas per shard with failover -> config/coordination service (ZooKeeper/etcd) -> metrics; optional write-behind to DB.
**Trade-offs**: LRU vs LFU eviction; cache aside vs write through vs write back; async replication (may lose writes) vs consistency; hot key mitigation (local replicas, key splitting); stampede protection (request coalescing, locks, jittered TTL); penetration (cache null results / Bloom filter).
**Follow-ups**: (1) How do you add/remove nodes without an invalidation storm? (2) How to handle a hot key? (3) How to keep cache and DB consistent?

### Case Study: Rate Limiter at Scale
**Requirements**: limit per user/IP/API key/endpoint, low overhead (few ms), accurate enough, distributed across many gateway nodes, clear 429 with Retry-After, fail-open or fail-closed policy.
**Estimates**: 1M QPS at gateway; 10M active keys x ~100 B state = ~1 GB, fits in a Redis cluster.
**Components**: Gateway middleware -> rules service (config, cached locally) -> counter store (Redis, atomic Lua script / INCR + EXPIRE) -> response headers (X-RateLimit-Remaining). Algorithms: token bucket (burst friendly, 2 values per key), sliding window counter (approximation, low memory), sliding window log (exact, heavy memory).
**Trade-offs**: centralised Redis (accurate, extra hop, SPOF risk) vs local counters with periodic sync (fast, approximate); race conditions solved by atomic scripts; clock skew; fail-open favors availability; shard keys by user id; multi-region limits approximate.
**Follow-ups**: (1) How to avoid race conditions between gateway nodes? (2) Token bucket vs sliding window: when each? (3) How to rate limit across multiple regions?

### Case Study: E-commerce / Order System
**Requirements**: catalog browse/search, cart, checkout, inventory, orders, payments, shipping status; no overselling; flash-sale surges.
**Estimates**: 10M DAU, 100 page views each = 1B/day ~ 12K QPS reads (peak 50K+); 1M orders/day ~ 12 QPS avg, flash sale peaks 1-10K QPS on a few SKUs; order row ~2 KB -> ~2 GB/day.
**Components**: API gateway -> microservices (Catalog, Search via Elasticsearch, Cart in Redis, Inventory, Order, Payment, Shipping, Notification) -> DB per service (SQL for orders/inventory) -> event bus (Kafka) for order events -> CDN for images; caches for catalog.
**Trade-offs**: reads cached and eventually consistent, but inventory decrement must be strongly consistent (conditional update `stock > 0`, optimistic locking, or Redis atomic decrement then async reconcile); reserve stock with TTL at checkout; Saga with compensations (cancel order, release stock, refund) vs 2PC; order state machine (CREATED -> PAID -> SHIPPED -> DELIVERED / CANCELLED); idempotent order placement.
**Follow-ups**: (1) How to prevent overselling in a flash sale? (2) What if payment succeeds but order service fails? (3) How to keep search results and prices consistent with the catalog DB?

### Case Study: Payment System
**Requirements**: pay-in (charge), pay-out, refunds, multiple methods/PSPs, strong correctness (no double charge, no lost money), auditability, reconciliation, PCI compliance.
**Estimates**: 1M transactions/day ~ 12 TPS avg, peak 100-1,000 TPS; correctness matters more than throughput; ledger rows retained for years.
**Components**: Payment API (idempotency key required) -> payment service (state machine) -> PSP/bank integration (Stripe, Razorpay, card networks; tokenization so raw card data never touches own servers) -> double-entry ledger (immutable, append-only SQL) -> async webhook/callback handler -> reconciliation job (compare internal ledger vs PSP settlement files) -> retry queue, fraud/risk service, audit log.
**Trade-offs**: strong consistency and ACID DB for the ledger (CP over AP); at-least-once calls to PSP with idempotency keys to get effectively-once; sync response vs async confirmation via webhooks (timeouts leave unknown state: query PSP status, do not blindly retry); Saga for multi-step flows; multi-PSP routing for availability vs complexity.
**Follow-ups**: (1) How to guarantee a customer is never charged twice on a timeout/retry? (2) How does reconciliation catch inconsistencies? (3) How to design the ledger for refunds and partial captures?
