# Frontend architecture

Baseline: 0.1.0 draft. Scope/decision: [ADR-0003](../adr/0003-frontend.md).

## Purpose

Independently deployed client application with feature boundaries, an application composition root, and shared generic utilities.

## Design

Proposed React/TypeScript layout: src/app for routing/providers/configuration, src/features/<feature> for pages/components/hooks/api/models/schemas, src/shared for generic components/utilities, src/api/generated for contracts, src/api/client for transport, and src/auth for provider integration. app composes features; features use shared and api; shared never imports app/features. Keep server state in the selected query client, local state near components, and global client state only where justified. API DTOs are transport models; map them into UI models where semantics differ. Browser configuration is public. Authorization remains enforced on the server. Test behavior at component boundaries and critical user journeys.

## Rules and verification

| Rule | Requirement | Evidence |
| --- | --- | --- |
| FE-001 | Frontend and backend MUST have separate application repositories and release pipelines. | Repository and pipeline review |
| FE-002 | Features MUST NOT import another feature’s internal implementation; use its documented public API or app-level composition. | Import boundary lint |
| FE-003 | HTTP calls MUST pass through the approved API client layer; generated files MUST NOT be manually edited. | Import lint and regeneration diff |
| FE-004 | Business-specific logic MUST stay in its feature and shared code MUST NOT depend on features. | Import boundary lint |
| FE-005 | UI MUST provide accessible keyboard navigation, semantic controls, and loading, empty, and failure states. | Accessibility and component checks |

## Adoption

Read [governance](../governance/adoption.md). Proposed rules are not approved merely because they use MUST. Record solution-specific choices, tests, and exceptions in the pinned baseline.
