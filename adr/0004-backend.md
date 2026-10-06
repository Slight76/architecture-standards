# ADR-0004: Backend architecture

Status: Proposed

Date: 2026-10-05

Owner: Repository owner; named delegate unassigned.

## Context

The owner is building an enterprise architecture standards repository consumed by application developers and coding agents. Frontend and backend applications must remain independent. Domain boundaries need usable, verifiable guidance.

## Decision

Independently deployable API or worker. Proposed baseline: a modular monolith with inward dependencies and explicit module ownership. Proposed project layout: Product.Api, Product.Application, Product.Domain, Product.Infrastructure, and Product.Contracts. Application depends on Domain; Infrastructure depends on Application/Domain. API may reference Infrastructure only in its composition root to register implementations; endpoint code uses Application/Contracts. Organize each layer by business module and use case. Domain entities enforce invariants. Application orchestrates transactions and ports. Infrastructure owns database and remote integrations. Contracts contain external transport DTOs and remain free of persistence entities. Avoid generic repositories by default; choose use-case-specific ports. Do not create microservices solely to mirror domains. Unit-test invariants and use cases; integrate against real selected storage; test authorization and contract behavior at HTTP boundaries.

## Alternatives

Keep informal guidance in conversation: rejected because it cannot be pinned or checked. Combine all domains into one document: rejected because ownership and applicability become unclear. Use domain documents linked through a solution baseline: selected for reviewable boundaries.

## Consequences

Each domain can evolve independently but changes require cross-domain review. Teams must maintain solution traceability and verification. More documentation is justified only when it changes design or operations.

## Traceability

See [Backend architecture](../backend/architecture.md), [principles](../ARCHITECTURE-PRINCIPLES.md), and [adoption](../governance/adoption.md). Related: [ADR-0010](0010-independent-applications.md), [ADR-0011](0011-agent-consumption.md).

## Verification

Assembly and package architecture tests; Assembly architecture tests; Architecture tests and design review; API tests and endpoint review; Module dependency tests and data review.

## Approval

Pending. This record is a recommendation, not evidence of owner approval.
