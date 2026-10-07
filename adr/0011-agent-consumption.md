# ADR-0011: Agent consumption

Status: Accepted

Date: 2026-10-05

> Amended 2026-10-06: this record predates the v1.0.0 split. "Enterprise" wording is historical; the team-level operating model now lives in [standards-marketplace](https://github.com/Slight76/standards-marketplace/blob/main/governance/team-operating-model.md) (see [ADR-0028](0028-retire-enterprise-layer.md) and [ADR-0029](0029-split-into-domain-handbooks.md)).

## Context

Applications need a reusable enterprise design and instructions that agents can apply consistently.

## Decision

Agents consume pinned standards, explicit rules, linked ADRs, and local application bootstrap instructions. Proposed decisions stay distinguishable from accepted ones. Checks and evidence accompany compliance claims.

## Alternatives

Implicit conventions reduce initial effort but allow drift. Explicit versioned decisions require maintenance but support repeatable implementation.

## Consequences

Maintain baseline pins and compatibility evidence. Do not confuse independent applications with independent business capabilities or require distributed systems without justification.

## Traceability

[Agent instructions](https://github.com/Slight76/standards-marketplace/blob/main/README.md), [frontend](../docs/frontend-architecture.md), [backend](../docs/backend-architecture.md), [integration](../docs/integration-architecture.md), [governance](https://github.com/Slight76/engineering-standards/blob/main/docs/adoption-process.md).

## Verification

Review repository separation, local bootstrap, immutable baseline reference, and applicable checks.

## Approval

Explicit owner direction in the supplied conversation.
