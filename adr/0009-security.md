# ADR-0009: Security architecture

Status: Proposed

Date: 2026-10-05

Owner: Repository owner; named delegate unassigned.

> Amended 2026-10-06: this record predates the v1.0.0 split. "Enterprise" wording is historical; the team-level operating model now lives in [standards-marketplace](https://github.com/Slight76/standards-marketplace/blob/main/governance/team-operating-model.md) (see [ADR-0028](0028-retire-enterprise-layer.md) and [ADR-0029](0029-split-into-domain-handbooks.md)).

## Context

The owner is building an enterprise architecture standards repository consumed by application developers and coding agents. Frontend and backend applications must remain independent. Domain boundaries need usable, verifiable guidance.

## Decision

Cross-domain identity, authorization, threat modeling, data classification, and secure operations. Select the identity provider and browser session design through a solution ADR. Evaluate a backend-for-frontend cookie session versus a public-client authorization-code flow with PKCE using the actual threat model. Avoid universal token-storage prescriptions. Cookie sessions require deliberate CSRF protection and cookie settings; cross-origin deployments require narrowly scoped CORS. Validate token issuer, audience, expiry, and permissions on APIs. Apply object-level authorization independently of UI state. Define rate limiting, upload validation, dependency updates, incident handling, key rotation, and audit retention based on exposure and classification.

## Alternatives

Keep informal guidance in conversation: rejected because it cannot be pinned or checked. Combine all domains into one document: rejected because ownership and applicability become unclear. Use domain documents linked through a solution baseline: selected for reviewable boundaries.

## Consequences

Each domain can evolve independently but changes require cross-domain review. Teams must maintain solution traceability and verification. More documentation is justified only when it changes design or operations.

## Traceability

See [Security architecture](https://github.com/Slight76/security-standards/blob/main/docs/security-architecture.md), [principles](../ARCHITECTURE-PRINCIPLES.md), and [adoption](https://github.com/Slight76/engineering-standards/blob/main/docs/adoption-process.md). Related: [ADR-0010](0010-independent-applications.md), [ADR-0011](0011-agent-consumption.md).

## Verification

Positive and negative authorization tests; Threat model review; Bundle inspection and identity tests; Security and data lifecycle review.

## Approval

Pending. This record is a recommendation, not evidence of owner approval.
