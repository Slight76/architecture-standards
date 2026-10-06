# ADR-0021: Operational signals and explicit service objectives

Status: Proposed

Date: 2026-10-05

## Context

Logs alone do not reveal reliability or demonstrate recoverability.

## Decision

Use correlated structured signals, safe cardinality, distinct health probes, user-centered objectives, and alert/runbook exercises.

## Alternatives

Vendor-specific instrumentation everywhere couples domain code; raw high-cardinality telemetry adds cost and exposure.

## Consequences

Operational owners must set thresholds and maintain dashboards. Telemetry failure must not destabilize the application.

## Traceability

- [Observability, health, and service objectives](../platform/observability-standard.md)

Rules: OBS-001, OBS-002, SLO-001.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
