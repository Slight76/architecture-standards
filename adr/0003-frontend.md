# ADR-0003: Frontend architecture

Status: Proposed

Date: 2026-10-05

Owner: Repository owner; named delegate unassigned.

> Amended 2026-10-06: this record predates the v1.0.0 split. "Enterprise" wording is historical; the team-level operating model now lives in [standards-marketplace](https://github.com/Slight76/standards-marketplace/blob/main/governance/team-operating-model.md) (see [ADR-0028](0028-retire-enterprise-layer.md) and [ADR-0029](0029-split-into-domain-handbooks.md)).

## Context

The owner is building an enterprise architecture standards repository consumed by application developers and coding agents. Frontend and backend applications must remain independent. Domain boundaries need usable, verifiable guidance.

## Decision

Independently deployed client application with feature boundaries, an application composition root, and shared generic utilities. Proposed React/TypeScript layout: src/app for routing/providers/configuration, src/features/<feature> for pages/components/hooks/api/models/schemas, src/shared for generic components/utilities, src/api/generated for contracts, src/api/client for transport, and src/auth for provider integration. app composes features; features use shared and api; shared never imports app/features. Keep server state in the selected query client, local state near components, and global client state only where justified. API DTOs are transport models; map them into UI models where semantics differ. Browser configuration is public. Authorization remains enforced on the server. Test behavior at component boundaries and critical user journeys.

## Alternatives

Keep informal guidance in conversation: rejected because it cannot be pinned or checked. Combine all domains into one document: rejected because ownership and applicability become unclear. Use domain documents linked through a solution baseline: selected for reviewable boundaries.

## Consequences

Each domain can evolve independently but changes require cross-domain review. Teams must maintain solution traceability and verification. More documentation is justified only when it changes design or operations.

## Traceability

See [Frontend architecture](../docs/frontend-architecture.md), [principles](../ARCHITECTURE-PRINCIPLES.md), and [adoption](https://github.com/Slight76/engineering-standards/blob/main/docs/adoption-process.md). Related: [ADR-0010](0010-independent-applications.md), [ADR-0011](0011-agent-consumption.md).

## Verification

Repository and pipeline review; Import boundary lint; Import lint and regeneration diff; Import boundary lint; Accessibility and component checks.

## Approval

Pending. This record is a recommendation, not evidence of owner approval.
