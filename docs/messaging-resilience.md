---
title: "Idempotency, messaging, and resilience"
status: proposed
version: 1.0.0
owner: "@Slight76"
supersedes: architecture-standards/integration/messaging-resilience.md@c1bda3d
---
# Idempotency, messaging, and resilience

Baseline: 1.0.0. Applies when: operations retry, publish events, or call remote dependencies

Decision: [ADR-0016](../adr/0016-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Timeouts and retries

Every outbound dependency has an overall deadline, per-attempt timeout, cancellation propagation, and a bounded retry budget. Set concrete values from the caller's latency budget in the solution record. Retry only classified transient failures and only when the operation is safe to replay. Honor server retry guidance within the remaining deadline; use backoff and jitter. Avoid retries at every layer multiplying attempts. Circuit breaking protects a failing dependency; it does not make unsafe mutations replayable.

## POST idempotency protocol

For financially or operationally significant repeatable mutations, require `Idempotency-Key` under this profile. This is an application contract, not a promise of exactly-once networking. Scope keys to authenticated tenant/principal and operation. Bound key length and request size. Compute a canonical request fingerprint including semantically relevant inputs; never treat a reused key with different content as success.

Atomically reserve a unique scoped key. Commit domain changes, the completed response reference, and any outbox message in the same local transaction. A concurrent duplicate reads the completed result or receives documented in-progress behavior; it must not perform the mutation again. Different content under the same key returns 409. Persist enough safe response metadata to replay the original outcome. Authentication and authorization still run on replays.

The solution sets key retention from the maximum retry/replay window; expiry means the deduplication guarantee ends. If the operation calls a remote payment/ERP service, a local transaction cannot make that side effect atomic. Forward a stable remote idempotency key if supported, or use a durable state machine with reconciliation and ambiguous-outcome handling. Do not hold a database transaction open across network calls.

## Events and workers

Use events only for a real asynchronous requirement. Name facts in past tense, such as `inventory.stock-adjusted.v1`; distinguish commands requesting work. The envelope includes eventId, type/version, occurredAt, producer, trace context, and tenant scope where applicable. Publish only necessary data, with schema and retention ownership.

When database commit and publish must be coordinated, write an outbox row in the local transaction. A dispatcher publishes with broker acknowledgement and marks progress; crashes can still cause duplicates. Consumers use a durable inbox/unique event key and commit their local side effect with deduplication. Acknowledge only after durable completion. Document ordering per aggregate/partition; do not promise global ordering casually.

Bound retries, dead-letter poison messages, alert on oldest message age and backlog, and provide a reviewed redrive runbook. Redriving a message must preserve its identity and tenant scope. Shutdown stops fetching work, finishes or relinquishes leases, and avoids acknowledging incomplete work. Schedule execution also needs overlap prevention and missed-run behavior.

## Example failure sequence

Database commits an adjustment and outbox entry. Dispatcher publishes, then crashes before marking it sent. On restart it publishes again. The consumer recognizes the same eventId and does not apply the adjustment twice. A test must force that crash window rather than merely assert that Publish was called.

Prohibit fire-and-forget tasks inside request handlers for durable work, unbounded retries, blanket retry of POST, queue-as-database assumptions, and a cache as the sole record of idempotency for critical writes.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| RES-001 | Outbound calls MUST declare bounded deadlines and operation-safe retry behavior. | Timeout, cancellation, and retry-budget tests |
| RES-002 | Replay-sensitive mutations MUST implement a durable scoped idempotency protocol. | Concurrent duplicate, changed payload, restart, and expiry tests |
| EVT-001 | Reliable database-to-event publication MUST coordinate through an outbox or documented equivalent. | Crash after commit/before publish and after publish tests |
| EVT-002 | Consumers MUST handle duplicates, poison messages, shutdown, and authorized redrive. | Inbox, dead-letter, redrive, and shutdown integration tests |

## Exceptions

Use the [exception record](https://github.com/Slight76/standards-marketplace/blob/main/templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
