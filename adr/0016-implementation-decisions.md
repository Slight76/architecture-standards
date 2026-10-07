# ADR-0016: Explicit replay and asynchronous delivery semantics

Status: Proposed

Date: 2026-10-05

## Context

Retries after timeouts can duplicate committed side effects; distributed delivery creates crash windows.

## Decision

Use scoped durable idempotency, bounded safe retries, outbox/inbox when needed, and replaceable caches with declared correctness limits.

## Alternatives

No retry reduces duplication but harms availability; blind retry duplicates effects; distributed transactions impose coupling and operational constraints.

## Consequences

At-least-once delivery needs deduplication, retention, dead-letter operations, and reconciliation of remote ambiguity.

## Traceability

- [Idempotency, messaging, and resilience](../docs/messaging-resilience.md)
- [Cache selection, ownership, and invalidation](https://github.com/Slight76/data-standards/blob/main/docs/caching-standard.md)

Rules: RES-001, RES-002, EVT-001, EVT-002, CACHE-001, CACHE-002.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
