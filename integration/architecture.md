# Integration architecture

Baseline: 0.1.0 draft. Scope/decision: [ADR-0006](../adr/0006-integration.md).

## Purpose

Versioned contracts connect independently deployed applications and external systems.

## Design

Backend owns the API contract artifact. Publish it with a version/checksum; consumers pin it and generate clients reproducibly. CI detects drift and assesses breaking changes. Preserve old consumers during expand/contract releases. Use structured problem responses with stable codes and safe details; never expose stack traces. Pagination, filtering, sorting, concurrency tokens, and validation failures must be explicit. Events require owner, schema/version, delivery semantics, ordering scope, retry/backoff, dead-letter handling, and idempotent consumers. Use a transactional outbox only when an atomic database update and eventual event publication are required. Queues and caches remain optional architecture decisions.

## Rules and verification

| Rule | Requirement | Evidence |
| --- | --- | --- |
| INT-001 | HTTP APIs MUST publish versioned OpenAPI artifacts and use a documented error contract. | Contract publication and API tests |
| INT-002 | Breaking contract changes MUST retain a documented migration and supported compatibility window. | Contract diff and consumer compatibility tests |
| INT-003 | Mutation retries MUST account for idempotency and ambiguous network outcomes. | Retry and duplicate-delivery tests |
| INT-004 | Trace context MUST propagate across supported boundaries without secrets or sensitive payloads in telemetry. | Trace integration and redaction checks |

## Adoption

Read [governance](../governance/adoption.md). Proposed rules are not approved merely because they use MUST. Record solution-specific choices, tests, and exceptions in the pinned baseline.
