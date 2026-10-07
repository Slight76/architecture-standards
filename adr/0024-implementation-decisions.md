# ADR-0024: Rule-scoped agent execution and truthful evidence

Status: Proposed

Date: 2026-10-05

## Context

Agents consume incomplete context and can confuse generated work with verified behavior.

## Decision

Use immutable baseline retrieval, task-specific reading maps, explicit evidence states, bounded task scope, and structured handoff records.

## Alternatives

Loading every document wastes context; implicit latest-main inheritance changes policy unexpectedly; self-reported compliance without commands is unverifiable.

## Consequences

Additional manifests and evidence checks are needed, but normal authorized work should proceed without repeated permission requests.

## Traceability

- [Agent development protocol and evidence](https://github.com/Slight76/engineering-standards/blob/main/docs/agent-development-standard.md)

Rules: AGT-001, AGT-002, AGT-003, AGT-004.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
