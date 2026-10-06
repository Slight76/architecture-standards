# ADR-0008: Infrastructure architecture

Status: Proposed

Date: 2026-10-05

Owner: Repository owner; named delegate unassigned.

## Context

The owner is building an enterprise architecture standards repository consumed by application developers and coding agents. Frontend and backend applications must remain independent. Domain boundaries need usable, verifiable guidance.

## Decision

Compute, network, DNS, routing, edge, storage, environments, capacity, and recovery beneath platform services. Choose managed services, containers, or VMs from requirements and operating capacity. Kubernetes is optional. Document zones/regions or local failure domains, public/private boundaries, routing, DNS ownership, certificate renewal, firewall rules, storage classes, and resource limits. Verify redundant components do not share an unrecognized single point of failure. IaC state contains sensitive material and requires protection. Plans require review for replacements and deletions. Recovery includes DNS, identities, secret access, images, configuration, and data; test reconstruction in an isolated environment.

## Alternatives

Keep informal guidance in conversation: rejected because it cannot be pinned or checked. Combine all domains into one document: rejected because ownership and applicability become unclear. Use domain documents linked through a solution baseline: selected for reviewable boundaries.

## Consequences

Each domain can evolve independently but changes require cross-domain review. Teams must maintain solution traceability and verification. More documentation is justified only when it changes design or operations.

## Traceability

See [Infrastructure architecture](../infrastructure/architecture.md), [principles](../ARCHITECTURE-PRINCIPLES.md), and [adoption](../governance/adoption.md). Related: [ADR-0010](0010-independent-applications.md), [ADR-0011](0011-agent-consumption.md).

## Verification

IaC plan and drift review; Network policy verification; Deployment and recovery review.

## Approval

Pending. This record is a recommendation, not evidence of owner approval.
