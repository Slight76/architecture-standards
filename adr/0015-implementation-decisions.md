# ADR-0015: Named identity profiles and threat-linked controls

Status: Proposed

Date: 2026-10-05

## Context

Browser sessions, API access, and workload identity have different risks.

## Decision

Default sensitive first-party web apps to a BFF session; allow a documented SPA public-client PKCE profile. Enforce object/tenant authorization and threat-specific boundary controls.

## Alternatives

Direct SPA tokens simplify static hosting but expose tokens to browser code. Custom auth increases security maintenance. API keys are not a substitute for delegated user identity.

## Consequences

BFF operation adds hosting/session costs. Neither profile removes XSS, CSRF, or resource-authorization obligations.

## Traceability

- [Identity, authorization, and session design](https://github.com/Slight76/security-standards/blob/main/docs/identity-standard.md)
- [Threat modeling and secure application behavior](https://github.com/Slight76/security-standards/blob/main/docs/application-security-standard.md)

Rules: IAM-001, IAM-002, IAM-003, IAM-004, SEC-005, SEC-006, SEC-007.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
