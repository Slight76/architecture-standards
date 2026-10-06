# ADR-0014: Conditional exact-origin CORS

Status: Proposed

Date: 2026-10-05

## Context

Agents otherwise add permissive CORS middleware to every API.

## Decision

Prefer same-origin browser routing when suitable; enable exact-origin CORS only for required cross-origin consumers, with explicit environment capabilities.

## Alternatives

Wildcard policies simplify demos but are unsuitable for our protected application profile. Requiring different origins for separate repos creates unnecessary browser policy work.

## Consequences

Cross-origin deployments need browser tests and coordinated headers. CORS does not authenticate or prevent all side effects.

## Traceability

- [CORS and browser origin policy](../security/cors-standard.md)

Rules: CORS-001, CORS-002, CORS-003.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
