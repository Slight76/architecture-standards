# ADR-0018: Use-case backend and owned persistence

Status: Proposed

Date: 2026-10-05

## Context

Layer folders alone do not prevent endpoint data access or cross-module coupling.

## Decision

Use a modular monolith with inward dependencies, a composition-root exception, scoped EF Core adapters, explicit transaction ownership, and real-engine tests.

## Alternatives

Microservices add network and deployment complexity; direct endpoint DbContext access is simpler but violates this profile boundary; a generic repository can add abstraction without value.

## Consequences

Ports and mapping add code. Apply domain richness proportionally rather than creating ceremony for simple data operations.

## Traceability

- [Backend modules, use cases, and dependencies](https://github.com/Slight76/engineering-standards/blob/main/docs/backend-implementation-standard.md)
- [Persistence, transactions, and query behavior](https://github.com/Slight76/data-standards/blob/main/docs/persistence-standard.md)

Rules: BE-006, BE-007, BE-008, BE-009, DATA-001, DATA-002, DATA-003.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
