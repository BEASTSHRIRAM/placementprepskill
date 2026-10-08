# CN Reference -- Computer Networks

## OSI Model (7 Layers)

| Layer | Name | Role | Key Protocols |
|---|---|---|---|
| 7 | Application | User-facing services | HTTP, FTP, DNS, SMTP, SSH |
| 6 | Presentation | Data formatting, encryption | SSL/TLS, JPEG, ASCII |
| 5 | Session | Session management | NetBIOS, PPTP |
| 4 | Transport | End-to-end delivery, reliability | TCP, UDP |
| 3 | Network | Logical addressing, routing | IP, ICMP, OSPF, BGP |
| 2 | Data Link | Node-to-node delivery, MAC addressing | Ethernet, Wi-Fi, ARP |
| 1 | Physical | Bit transmission over medium | Cables, Hubs, Repeaters |

**TCP/IP Model (4 Layers)**
Application (covers OSI 5,6,7) | Transport | Internet (Network) | Network Access (Data Link + Physical)

---

## TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Guaranteed delivery, retransmission | No guarantee |
| Ordering | Maintains order | No order guarantee |
| Speed | Slower (overhead) | Faster |
| Use cases | HTTP, FTP, email, SSH | DNS, video streaming, VoIP, gaming |
| Header size | 20 bytes minimum | 8 bytes |

**TCP 3-Way Handshake**
1. Client sends SYN (synchronize)
2. Server responds with SYN-ACK
3. Client sends ACK
Connection is established.

**TCP 4-Way Termination**
FIN, ACK, FIN, ACK

---

## IP Addressing

**IPv4**: 32-bit address, written as 4 octets. Example: 192.168.1.1
**IPv6**: 128-bit address, written as 8 groups of 4 hex digits.

**Private IP Ranges (not routable on public internet)**
- 10.0.0.0 to 10.255.255.255
- 172.16.0.0 to 172.31.255.255
- 192.168.0.0 to 192.168.255.255

**Subnetting**
CIDR notation: 192.168.1.0/24 means first 24 bits are network, last 8 are host.
Subnet mask /24 = 255.255.255.0, allows 254 hosts.

**NAT (Network Address Translation)**
Maps private IPs to a public IP. Allows multiple devices to share one public IP.

---

## DNS (Domain Name System)

Translates human-readable domain names (google.com) to IP addresses.

**Resolution Process**
1. Browser checks local cache
2. Checks OS hosts file
3. Queries Recursive Resolver (your ISP)
4. Resolver queries Root Name Server
5. Root refers to TLD Name Server (.com)
6. TLD refers to Authoritative Name Server
7. Authoritative returns IP
8. Resolver caches and returns to client

**Record Types**
- A: maps domain to IPv4
- AAAA: maps domain to IPv6
- CNAME: alias for another domain
- MX: mail server for domain
- NS: authoritative name server
- PTR: reverse DNS lookup

---

## HTTP and HTTPS

**HTTP Methods**: GET (retrieve), POST (create), PUT (replace), PATCH (partial update), DELETE (remove)

**HTTP Status Codes**
- 2xx: Success (200 OK, 201 Created, 204 No Content)
- 3xx: Redirection (301 Moved Permanently, 302 Found)
- 4xx: Client Error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)
- 5xx: Server Error (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable)

**HTTP vs HTTPS**
HTTPS uses TLS (Transport Layer Security) to encrypt traffic. TLS handshake establishes encryption keys before data transfer.

**HTTP/1.1 vs HTTP/2 vs HTTP/3**
- HTTP/1.1: one request per connection (keep-alive allows reuse but still sequential)
- HTTP/2: multiplexing (multiple requests over one connection), header compression
- HTTP/3: uses QUIC (UDP-based), eliminates head-of-line blocking, faster connection setup

---

## Routing Protocols

**RIP (Routing Information Protocol)**
Distance vector protocol. Uses hop count as metric (max 15 hops). Slow convergence. Bellman-Ford algorithm.

**OSPF (Open Shortest Path First)**
Link state protocol. Uses Dijkstra's algorithm. Fast convergence. Maintains full topology map.

**BGP (Border Gateway Protocol)**
Path vector protocol. Used between Autonomous Systems on the internet (inter-domain routing). The backbone of internet routing.

---

## Congestion Control (TCP)

**Slow Start**: begins with a small congestion window (cwnd), doubles each RTT until threshold.
**Congestion Avoidance**: after threshold, increase cwnd by 1 MSS per RTT (linear growth).
**Fast Retransmit**: if 3 duplicate ACKs received, retransmit lost segment without waiting for timeout.
**Fast Recovery**: after fast retransmit, reduce threshold and cwnd, then enter congestion avoidance (not slow start).

---

## Important Protocols and Their Ports

| Protocol | Port |
|---|---|
| HTTP | 80 |
| HTTPS | 443 |
| FTP | 21 |
| SSH | 22 |
| SMTP | 25 |
| DNS | 53 |
| DHCP | 67/68 |
| POP3 | 110 |
| IMAP | 143 |

---

## Common Interview Questions

1. What happens when you type a URL in a browser?
2. What is the difference between TCP and UDP? When would you use each?
3. Explain the 3-way handshake.
4. What is ARP and why is it needed?
5. What is the difference between a hub, switch, and router?
6. What is DHCP and how does it work?
7. What is a firewall? Types of firewalls?
8. What is the difference between HTTP and HTTPS?
9. What is a proxy server and a reverse proxy?
10. What is the difference between symmetric and asymmetric encryption in TLS?
11. What is a VPN and how does it work?
12. What is ICMP? What is ping?
13. Explain how a CDN works.
14. What is the difference between latency, bandwidth, and throughput?
15. What is socket programming? What is a socket?


---

## Advanced Topics and Interview Q Bank

### TCP 3-way handshake and 4-way teardown (flags and numbers)
Handshake:
1. Client -> Server: SYN, seq = x (client picks ISN)
2. Server -> Client: SYN+ACK, seq = y, ack = x+1
3. Client -> Server: ACK, seq = x+1, ack = y+1 (data may ride on this segment)

Client enters ESTABLISHED after step 2, server after step 3. SYN consumes one sequence number. SYN flood: attacker leaves half-open connections; mitigated by SYN cookies.
Teardown (each direction closes independently, half-close possible):
1. A -> B: FIN, seq = u (A: FIN_WAIT_1)
2. B -> A: ACK, ack = u+1 (A: FIN_WAIT_2, B: CLOSE_WAIT)
3. B -> A: FIN, seq = v (B: LAST_ACK)
4. A -> B: ACK, ack = v+1 (A: TIME_WAIT, then CLOSED after timer). B closes on receiving it.

Server may combine steps 2 and 3 (FIN+ACK) giving a 3-segment close. RST flag aborts a connection abruptly.

### TIME_WAIT
Side that sends the last ACK waits 2*MSL (Linux uses 60 s). Why: (1) if the last ACK is lost, the peer retransmits FIN and we can re-ACK; (2) lets old duplicate segments of the connection die out so they do not corrupt a new connection on the same 4-tuple. Many TIME_WAIT sockets on a busy host: use connection reuse/keep-alive, SO_REUSEADDR; do not just shorten the timer blindly.

### Flow control vs congestion control
| | Flow control | Congestion control |
|---|---|---|
| Protects | Receiver buffer | The network (routers) |
| Mechanism | Receiver window (rwnd) advertised in header | cwnd: slow start, congestion avoidance, fast retransmit/recovery |
| Scope | End to end, between two hosts | Global concern, inferred from loss/delay |

Sender window = min(rwnd, cwnd). Zero window: sender stops and sends window probes. Slow start: cwnd 1, 2, 4, 8 MSS per RTT until ssthresh, then +1 MSS per RTT. On timeout: ssthresh = cwnd/2, cwnd = 1 MSS. On 3 dup ACKs (Reno): ssthresh = cwnd/2, cwnd = ssthresh (+3), then linear growth. Example: cwnd = 16 at loss by timeout -> ssthresh = 8, cwnd = 1.

### Sliding window: Go-Back-N vs Selective Repeat
| | Go-Back-N | Selective Repeat |
|---|---|---|
| Sender window | up to 2^m - 1 | up to 2^(m-1) |
| Receiver window | 1 (in-order only) | same as sender (buffers out of order) |
| ACK | Cumulative | Individual |
| On loss | Resend lost frame and all after it | Resend only the lost frame |
| Complexity | Low | Higher (buffering, per-frame timers) |

m = sequence number bits. Example: m = 3 -> GBN window max 7, SR window max 4. Stop-and-wait is window 1.
Efficiency = N / (1 + 2a), a = propagation delay / transmission delay (capped at 1). Example: Tt = 1 ms, Tp = 49.5 ms -> a = 49.5, 1+2a = 100, so N = 100 frames fill the pipe; stop-and-wait gives 1%.

### Subnetting worked examples
- /26: mask 255.255.255.192. Block size 64, 62 usable hosts (2^6 - 2). Splitting 192.168.1.0/24 gives 4 subnets:
  - 192.168.1.0/26: hosts .1-.62, broadcast .63
  - 192.168.1.64/26: hosts .65-.126, broadcast .127
  - 192.168.1.128/26: hosts .129-.190, broadcast .191
  - 192.168.1.192/26: hosts .193-.254, broadcast .255
- Which subnet is 10.1.2.77/28? Mask 255.255.255.240, block 16: 77 lies in 64-79 -> network 10.1.2.64, broadcast 10.1.2.79, hosts .65-.78 (14).
- 172.16.0.0/16 into 8 subnets: borrow 3 bits -> /19, mask 255.255.224.0, block 32 in third octet (172.16.0.0, 172.16.32.0, ...), hosts per subnet 2^13 - 2 = 8190.
- VLSM: 192.168.10.0/24 for 100, 50, 20 hosts. 100 -> /25 (126 hosts): 192.168.10.0/25. 50 -> /26 (62): 192.168.10.128/26. 20 -> /27 (30): 192.168.10.192/27. Allocate largest first.
- Route summarization: 192.168.0.0/24 to 192.168.3.0/24 -> 192.168.0.0/22 (mask 255.255.252.0).
- Quick table: /24=254 hosts, /25=126, /26=62, /27=30, /28=14, /29=6, /30=2 (point-to-point). Usable = 2^h - 2 (network and broadcast reserved). /31 allowed for point-to-point links (RFC 3021).
- Classful: A 1-126 (/8), B 128-191 (/16), C 192-223 (/24), D multicast 224-239, E reserved.

### NAT / PAT
- Static NAT: 1 private <-> 1 public. Dynamic NAT: pool of public IPs. PAT (NAT overload): many private IPs share one public IP, distinguished by port.
- Example: 192.168.1.10:51000 -> router rewrites to 203.0.113.5:40001; table entry maps the reply back. Router edits IP/TCP headers and recomputes checksums.
- Drawbacks: breaks end-to-end principle, inbound connections need port forwarding, trouble for protocols embedding IPs (active FTP). IPv6 removes the need for NAT.

### ARP, RARP, DHCP step by step
**ARP** (IP -> MAC, same LAN): host wants to reach 192.168.1.20. (1) Check ARP cache. (2) Broadcast ARP request (dest MAC ff:ff:ff:ff:ff:ff): "who has 192.168.1.20?". (3) Owner replies unicast with its MAC. (4) Sender caches it. For an off-subnet destination, ARP for the default gateway's MAC instead. Gratuitous ARP announces/detects IP conflicts; ARP spoofing is a known attack.
**RARP**: MAC -> IP; obsolete, replaced by BOOTP and DHCP.
**DHCP (DORA)**, UDP server 67 / client 68:
1. Discover: client broadcasts (src 0.0.0.0, dst 255.255.255.255)
2. Offer: server proposes IP, mask, gateway, DNS, lease time
3. Request: client broadcasts which offer it accepts
4. Acknowledge: server confirms lease

Renewal attempts at 50% of lease (T1), rebinding at 87.5% (T2).

### ICMP, ping, traceroute
- ICMP (network layer, carried in IP, protocol number 1) reports errors and diagnostics: Destination Unreachable, Time Exceeded, Redirect, Echo Request/Reply.
- ping: sends Echo Request (type 8), expects Echo Reply (type 0); reports RTT and loss.
- traceroute: sends packets with TTL 1, 2, 3...; each router that decrements TTL to 0 returns ICMP Time Exceeded (type 11), revealing the hop. Final host replies (ICMP Port Unreachable for UDP probes on Linux, Echo Reply for ICMP probes in Windows tracert). Max TTL typically 30 hops.
- TTL stops routing loops; each router decrements it by 1.

### HTTP/1.1 vs HTTP/2 vs HTTP/3
| | HTTP/1.1 | HTTP/2 | HTTP/3 |
|---|---|---|---|
| Transport | TCP | TCP (usually TLS) | QUIC over UDP (TLS 1.3 built in) |
| Format | Text | Binary frames | Binary frames |
| Concurrency | One request at a time per connection (browsers open ~6 connections) | Multiplexed streams on one connection | Multiplexed, streams independent |
| Head-of-line blocking | At HTTP level | Fixed at HTTP, remains at TCP level | Removed (per-stream loss recovery) |
| Headers | Plain, repeated | HPACK compression | QPACK compression |
| Setup | TCP + TLS handshakes | TCP + TLS | 1 RTT (0-RTT on resume), connection migration via connection ID |

HTTP/2 server push exists but is largely deprecated. HTTP/3 default port is UDP 443.

### TLS handshake overview (TLS 1.2 style, then 1.3)
1. ClientHello: supported versions, cipher suites, client random.
2. ServerHello: chosen cipher suite, server random, plus certificate (chain signed by a CA).
3. Client validates certificate (CA trust, domain, expiry, revocation).
4. Key exchange: (TLS 1.2 with RSA) client encrypts a pre-master secret with the server public key; (ECDHE) both sides derive a shared secret, giving forward secrecy.
5. Both derive the same symmetric session keys; Finished messages verify integrity.
6. Application data flows encrypted with symmetric crypto (AES-GCM, ChaCha20).

Asymmetric crypto only authenticates and agrees on keys (slow); symmetric does bulk data (fast). TLS 1.3: 1 RTT handshake, removes weak ciphers, mandates forward secrecy, 0-RTT resume possible (replay risk).

### Cookies and sessions
HTTP is stateless. Cookie: small data the server sets via `Set-Cookie`, browser returns in `Cookie` header on matching requests. Attributes: Expires/Max-Age, Domain, Path, Secure (HTTPS only), HttpOnly (no JS access, mitigates XSS theft), SameSite (Strict/Lax/None, mitigates CSRF). Session: server stores state keyed by a session ID kept in a cookie; client holds only the ID. JWT/token alternative: stateless signed token in the Authorization header. Cookie limit about 4 KB each. localStorage is not sent automatically.

### Firewall, proxy, reverse proxy, VPN
- Firewall types: packet filter (L3/L4, IP/port rules), stateful (tracks connections), application/proxy firewall and WAF (L7), next-gen (deep inspection, IPS).
- Forward proxy: sits in front of clients; hides client identity, caching, content filtering, access control.
- Reverse proxy: sits in front of servers; hides backend, load balancing, TLS termination, caching, compression (Nginx, HAProxy).
- VPN: encrypted tunnel over the public internet (IPsec, OpenVPN, WireGuard); client traffic is encapsulated and exits from the VPN gateway. Site-to-site vs remote-access. Gives confidentiality and private addressing.

### CDN
Geographically distributed edge servers cache static (and some dynamic) content near users. Request is routed to the nearest edge via DNS (CNAME to CDN, geo/latency-based answers) or anycast. Cache hit: served from edge. Miss: edge fetches from origin, caches per Cache-Control/TTL. Benefits: lower latency, less origin load, DDoS absorption. Purge or version URLs to update content.

### WebSocket vs HTTP polling
| | Short polling | Long polling | SSE | WebSocket |
|---|---|---|---|---|
| Model | Client asks every n sec | Server holds request until data | Server -> client stream over HTTP | Full-duplex over one TCP connection |
| Overhead | High (headers each time, empty replies) | Medium | Low | Lowest after handshake |
| Direction | Client pull | Client pull | One way | Both ways |

WebSocket starts as an HTTP/1.1 request with `Upgrade: websocket`; server replies 101 Switching Protocols; then framed messages flow (ws:// port 80, wss:// port 443). Use for chat, live dashboards, games.

### What happens when you type a URL (short)
1. Parse URL; check HSTS/cache. 2. DNS lookup (browser/OS cache, then recursive resolver -> root -> TLD -> authoritative). 3. ARP for gateway MAC if needed; route packets. 4. TCP 3-way handshake to port 443. 5. TLS handshake. 6. Send HTTP request (GET /). 7. Server (via load balancer/reverse proxy) processes, returns response (e.g. 200 + HTML, or 301 redirect). 8. Browser parses HTML, builds DOM/CSSOM, fetches CSS/JS/images, renders. 9. Connection kept alive or closed.

### 15 more tricky Q&As
1. TCP is reliable, yet DNS and QUIC use UDP. Why? Lower latency, no connection setup; reliability is done at application layer (QUIC) or by retry (DNS).
2. Why does the handshake need 3 steps, not 2? To confirm both sides can send and receive and to synchronize both ISNs; also stops old duplicate SYNs from opening connections.
3. Why random ISN? Avoid confusion with old segments, and make sequence prediction (spoofing) hard.
4. Max TCP payload per segment on Ethernet? MTU 1500 - 20 IP - 20 TCP = 1460 bytes MSS. IP fragmentation occurs if packet > MTU (and DF not set).
5. Hub vs switch vs router? Hub: L1, repeats to all, one collision domain. Switch: L2, learns MACs, one collision domain per port, one broadcast domain. Router: L3, separates broadcast domains.
6. Collision vs broadcast domain? Switch ports split collision domains; routers (and VLANs) split broadcast domains.
7. Ethernet frame minimum size? 64 bytes (so a sender detects collision during transmission in CSMA/CD); max payload 1500.
8. 127.0.0.1 and 169.254.x.x? Loopback; APIPA link-local address assigned when DHCP fails.
9. MAC vs IP? MAC: L2, flat, hardware, changes per hop. IP: L3, hierarchical, end to end (constant except NAT).
10. 301 vs 302 vs 307/308? 301 permanent, 302 temporary (method may change to GET), 307 temporary and 308 permanent both preserve the method.
11. Idempotency? GET, HEAD, PUT, DELETE are idempotent (GET/HEAD also safe); POST is not; PATCH is not guaranteed.
12. Latency vs bandwidth vs throughput? Latency: delay (ms). Bandwidth: max capacity. Throughput: actual achieved rate. Bandwidth-delay product = bandwidth * RTT = bytes in flight needed to fill the pipe (100 Mbps * 40 ms = 4 Mb = 500 KB).
13. Distance vector vs link state? DV (RIP): share table with neighbors, count-to-infinity, eased by split horizon/poison reverse. LS (OSPF): flood topology, each node runs Dijkstra.
14. Why does DNS use both UDP and TCP? UDP 53 for normal queries (small); TCP 53 for zone transfers and truncated/large responses.
15. Symmetric vs asymmetric encryption? Symmetric: one shared key, fast (AES). Asymmetric: key pair (RSA, ECC), slower, solves key distribution and enables signatures. TLS uses both (hybrid).
