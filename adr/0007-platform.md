# ADR-0007: Platform architecture

Status: Proposed

Date: 2026-10-05

Owner: Repository owner; named delegate unassigned.

> Amended 2026-10-06: this record predates the v1.0.0 split. "Enterprise" wording is historical; the team-level operating model now lives in [standards-marketplace](https://github.com/Slight76/standards-marketplace/blob/main/governance/team-operating-model.md) (see [ADR-0028](0028-retire-enterprise-layer.md) and [ADR-0029](0029-split-into-domain-handbooks.md)).

## Context

The owner is building an enterprise architecture standards repository consumed by application developers and coding agents. Frontend and backend applications must remain independent. Domain boundaries need usable, verifiable guidance.

## Decision

Developer and delivery capabilities, environments, artifact lifecycle, telemetry, and release controls. Separate development, test, and production identities and configuration. Build once and promote the same artifact; record provenance and dependency versions. Specify rollout strategy, deployment gates, smoke tests, and rollback commands per application. Limit pipeline credentials and third-party actions; pin reviewed dependencies. Define telemetry retention, alert ownership, and actionable runbooks. Readiness tests serving capability; liveness tests process health, avoiding dependency-triggered restart storms. Local orchestration such as Aspire is optional and does not become the production deployment platform by implication.

## Alternatives

Keep informal guidance in conversation: rejected because it cannot be pinned or checked. Combine all domains into one document: rejected because ownership and applicability become unclear. Use domain documents linked through a solution baseline: selected for reviewable boundaries.

## Consequences

Each domain can evolve independently but changes require cross-domain review. Teams must maintain solution traceability and verification. More documentation is justified only when it changes design or operations.

## Traceability

See [Platform architecture](https://github.com/Slight76/operations-standards/blob/main/docs/platform-architecture.md), [principles](../ARCHITECTURE-PRINCIPLES.md), and [adoption](https://github.com/Slight76/engineering-standards/blob/main/docs/adoption-process.md). Related: [ADR-0010](0010-independent-applications.md), [ADR-0011](0011-agent-consumption.md).

## Verification

Pipeline review; CI evidence review; Operational smoke tests; Secret scanning and deployment review.

## Approval

Pending. This record is a recommendation, not evidence of owner approval.
