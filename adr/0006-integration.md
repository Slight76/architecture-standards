# ADR-0006: Integration architecture

Status: Proposed

Date: 2026-10-05

Owner: Repository owner; named delegate unassigned.

## Context

The owner is building an enterprise architecture standards repository consumed by application developers and coding agents. Frontend and backend applications must remain independent. Domain boundaries need usable, verifiable guidance.

## Decision

Versioned contracts connect independently deployed applications and external systems. Backend owns the API contract artifact. Publish it with a version/checksum; consumers pin it and generate clients reproducibly. CI detects drift and assesses breaking changes. Preserve old consumers during expand/contract releases. Use structured problem responses with stable codes and safe details; never expose stack traces. Pagination, filtering, sorting, concurrency tokens, and validation failures must be explicit. Events require owner, schema/version, delivery semantics, ordering scope, retry/backoff, dead-letter handling, and idempotent consumers. Use a transactional outbox only when an atomic database update and eventual event publication are required. Queues and caches remain optional architecture decisions.

## Alternatives

Keep informal guidance in conversation: rejected because it cannot be pinned or checked. Combine all domains into one document: rejected because ownership and applicability become unclear. Use domain documents linked through a solution baseline: selected for reviewable boundaries.

## Consequences

Each domain can evolve independently but changes require cross-domain review. Teams must maintain solution traceability and verification. More documentation is justified only when it changes design or operations.

## Traceability

See [Integration architecture](../integration/architecture.md), [principles](../ARCHITECTURE-PRINCIPLES.md), and [adoption](../governance/adoption.md). Related: [ADR-0010](0010-independent-applications.md), [ADR-0011](0011-agent-consumption.md).

## Verification

Contract publication and API tests; Contract diff and consumer compatibility tests; Retry and duplicate-delivery tests; Trace integration and redaction checks.

## Approval

Pending. This record is a recommendation, not evidence of owner approval.
