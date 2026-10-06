# ADR-0020: Independent immutable delivery with boundary-specific verification

Status: Proposed

Date: 2026-10-05

## Context

A passing unit suite cannot prove browser, database, or deployment behavior.

## Decision

Build immutable per-application artifacts and require risk-appropriate checks at the boundary being claimed. Retain commit-linked evidence and protected release credentials.

## Alternatives

Simultaneous full-system deployment is simpler but undermines independence; testing everything only end-to-end is slow and poor at diagnosis.

## Consequences

Test environments and evidence retention cost time and resources. Protection settings must actually be configured in each implementation repo.

## Traceability

- [Build, release, and supply-chain controls](../platform/delivery-standard.md)
- [Verification boundaries and test evidence](../platform/testing-standard.md)

Rules: CICD-001, CICD-002, CICD-003, TEST-001, TEST-002, TEST-003.

Related foundational decisions: [ADR-0010](0010-independent-applications.md) and [ADR-0011](0011-agent-consumption.md). These records elaborate the earlier domain drafts without rewriting their history.

## Verification

Each linked standard defines acceptance cases and evidence. Documentation CI verifies link/catalog consistency; applications implement runtime checks.

## Approval

Recommended baseline authored under the requested full revision. Pending explicit solution adoption; publication is not a claim of production certification or approval of unspecified business targets.
