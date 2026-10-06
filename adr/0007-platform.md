# ADR-0007: Platform architecture

Status: Proposed

Date: 2026-10-05

Owner: Repository owner; named delegate unassigned.

## Context

The owner is building an enterprise architecture standards repository consumed by application developers and coding agents. Frontend and backend applications must remain independent. Domain boundaries need usable, verifiable guidance.

## Decision

Developer and delivery capabilities, environments, artifact lifecycle, telemetry, and release controls. Separate development, test, and production identities and configuration. Build once and promote the same artifact; record provenance and dependency versions. Specify rollout strategy, deployment gates, smoke tests, and rollback commands per application. Limit pipeline credentials and third-party actions; pin reviewed dependencies. Define telemetry retention, alert ownership, and actionable runbooks. Readiness tests serving capability; liveness tests process health, avoiding dependency-triggered restart storms. Local orchestration such as Aspire is optional and does not become the production deployment platform by implication.

## Alternatives

Keep informal guidance in conversation: rejected because it cannot be pinned or checked. Combine all domains into one document: rejected because ownership and applicability become unclear. Use domain documents linked through a solution baseline: selected for reviewable boundaries.

## Consequences

Each domain can evolve independently but changes require cross-domain review. Teams must maintain solution traceability and verification. More documentation is justified only when it changes design or operations.

## Traceability

See [Platform architecture](../platform/architecture.md), [principles](../ARCHITECTURE-PRINCIPLES.md), and [adoption](../governance/adoption.md). Related: [ADR-0010](0010-independent-applications.md), [ADR-0011](0011-agent-consumption.md).

## Verification

Pipeline review; CI evidence review; Operational smoke tests; Secret scanning and deployment review.

## Approval

Pending. This record is a recommendation, not evidence of owner approval.
