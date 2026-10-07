# ADR-0019: Data integrity and compatible schema delivery

Status: Proposed

Date: 2026-10-05

## Context

Independent releases and concurrent users require enforced invariants and a recovery path.

## Decision

Use owned relational models with constraints, expand/contract migrations, separate schema identity, and measured restoration.

## Alternatives

Shared service tables couple releases; application-only constraints race; startup production migrations mix serving and administration.

## Consequences

Compatibility periods and backfills cost storage/operations. Recovery targets must be supplied by the business owner.

## Traceability

- [Logical and physical database design](https://github.com/Slight76/data-standards/blob/main/docs/design-standard.md)
- [Schema delivery and recovery](https://github.com/Slight76/data-standards/blob/main/docs/migration-recovery-standard.md)

Rules: DB-006, DB-007, DB-008, MIG-001, MIG-002, DR-001.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
