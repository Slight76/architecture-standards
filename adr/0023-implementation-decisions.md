# ADR-0023: Measurable solution and enterprise ownership (historical)

Status: Superseded

Superseded by: ADR-0028

Date: 2026-10-05

> Amended 2026-10-06: this record predates the v1.0.0 split. "Enterprise" wording is historical; the team-level operating model now lives in [standards-marketplace](https://github.com/Slight76/standards-marketplace/blob/main/governance/team-operating-model.md) (see [ADR-0028](0028-retire-enterprise-layer.md) and [ADR-0029](0029-split-into-domain-handbooks.md)).

## Context

Documents need business context and accountable adoption rather than invented targets.

## Decision

Maintain ownership/technology registers and solution packets with measurable scenarios, cross-domain choices, and production-readiness evidence.

## Alternatives

A fixed universal tier can overbuild small systems; unstructured prose hides missing decisions; copying enterprise text into every app causes drift.

## Consequences

Owners must supply business inputs and maintain impact records. This does not require a large architecture board.

## Traceability

- [Enterprise governance, portfolio, and technology lifecycle](https://github.com/Slight76/standards-marketplace/blob/main/governance/team-operating-model.md)
- [Solution design and production readiness](../docs/solution-design-standard.md)

Rules: EA-004, EA-005, EA-006, SA-004, SA-005.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
