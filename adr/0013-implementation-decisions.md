# ADR-0013: Resource-oriented HTTP and owned contracts

Status: Proposed

Date: 2026-10-05

## Context

Separate frontend/backend release cycles require stable, machine-readable behavior.

## Decision

Use JSON resource-oriented HTTP, a major-version path, Problem Details, concurrency preconditions where needed, and immutable OpenAPI client artifacts.

## Alternatives

GraphQL adds query flexibility but requires query cost/auth governance; gRPC fits controlled service clients; ad-hoc RPC is simple initially but weakens uniform contracts. Select alternatives through a scoped ADR.

## Consequences

Uniform clients and compatibility checks cost tooling and consumer-window maintenance. Not every compatibility issue is machine-detectable.

## Traceability

- [HTTP API design](../docs/http-api-standard.md)
- [Contract ownership, generation, and compatibility](../docs/contracts-standard.md)

Rules: API-001, API-002, API-003, API-004, CON-001, CON-002, CON-003.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
