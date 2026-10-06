# ADR-0017: Feature-oriented typed frontend profile

Status: Proposed

Date: 2026-10-05

## Context

Agents need consistent state, transport, accessibility, and testing choices.

## Decision

Use strict React/TypeScript with feature boundaries, TanStack Query server state, scoped form state, generated API adapters, and accessible user journeys.

## Alternatives

Global stores for all state duplicate server truth; framework SSR can fit public pages but adds unnecessary runtime for some internal apps.

## Consequences

The selected libraries require pinned versions and upgrades. Dependency lint and browser evidence are additional maintenance.

## Traceability

- [Frontend structure, state, and data access](../frontend/implementation-standard.md)
- [Accessible and resilient user interfaces](../frontend/accessibility-performance.md)

Rules: FE-006, FE-007, FE-008, FE-009, UX-001, UX-002.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
