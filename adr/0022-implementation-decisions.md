# ADR-0022: Requirement-led infrastructure and failure boundaries

Status: Proposed

Date: 2026-10-05

## Context

Enterprise labels can cause agents to add orchestration and HA without justified needs.

## Decision

Select the simplest platform meeting requirements, document traffic and failure domains, and use protected reproducible IaC with measured capacity.

## Alternatives

Kubernetes everywhere increases operations; unmanaged manual resources drift; replicas sharing a host do not protect against host loss.

## Consequences

Infrastructure requires ownership, state protection, drift response, and recovery exercises.

## Traceability

- [Network, compute, configuration, and infrastructure lifecycle](../infrastructure/implementation-standard.md)

Rules: INF-004, INF-005, INF-006.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
