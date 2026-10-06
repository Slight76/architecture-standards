# Cache selection, ownership, and invalidation

Baseline: 0.3.0 recommended draft. Applies when: a solution caches business or identity-related data

Decision: [ADR-0016](../adr/0016-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Decision rule

Begin without a distributed cache. Introduce one for a measured latency/load requirement with a named owner and explicit staleness tolerance. In-process cache is per instance and disappears on restart; distributed cache adds a network dependency and operating cost. Neither becomes the source of truth accidentally.

Use cache-aside for replaceable read models by default. Keys include tenant, permission-relevant scope where necessary, resource version/representation, and normalized query parameters. Values have bounded size and TTL. Avoid embedding raw personal data in keys. Cache hits must not bypass current authorization.

Invalidate or update after the authoritative transaction commits. Document the race where an old concurrent read repopulates a stale value after invalidation; mitigate with versioned keys, bounded TTL, coordination, or accepting explicitly bounded staleness. Use single-flight/locking or jittered expiration to control stampedes. Negative caching has a short deliberate lifetime and cannot conceal newly created data indefinitely.

## Failure behavior

If the cache is unavailable, fail over to the source only within a safe database load budget; otherwise shed load or degrade the affected operation. Do not retry a failed cache on every request without limits. Test total cache loss and cold start under load. A cached permission decision requires expiry/revocation semantics; default to fresh authoritative decisions for sensitive actions.

Idempotency, sessions, and locks may use a distributed store only when its durability/eviction/failover behavior satisfies their correctness requirements. A best-effort evicting cache cannot guarantee critical deduplication. Do not call every Redis use a cache; identify its actual responsibility.

## Example

A product description read may tolerate an explicitly approved staleness window. An available-stock check used to approve an adjustment cannot trust that cached description/read model; the write enforces current inventory constraints in the database. Monitor hit/miss, age, evictions, source pressure, and failures with safe labels.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| CACHE-001 | Caches MUST define ownership, scoped keys, staleness, invalidation, and loss behavior. | Cross-tenant key, stale-fill race, eviction, and outage tests |
| CACHE-002 | Correctness-critical state MUST NOT rely on best-effort cache durability. | Architecture review and restart/failover tests |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
