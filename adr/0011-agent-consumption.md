# ADR-0011: Agent consumption

Status: Accepted

Date: 2026-10-05

## Context

Applications need a reusable enterprise design and instructions that agents can apply consistently.

## Decision

Agents consume pinned standards, explicit rules, linked ADRs, and local application bootstrap instructions. Proposed decisions stay distinguishable from accepted ones. Checks and evidence accompany compliance claims.

## Alternatives

Implicit conventions reduce initial effort but allow drift. Explicit versioned decisions require maintenance but support repeatable implementation.

## Consequences

Maintain baseline pins and compatibility evidence. Do not confuse independent applications with independent business capabilities or require distributed systems without justification.

## Traceability

[Agent instructions](../AGENTS.md), [frontend](../frontend/architecture.md), [backend](../backend/architecture.md), [integration](../integration/architecture.md), [governance](../governance/adoption.md).

## Verification

Review repository separation, local bootstrap, immutable baseline reference, and applicable checks.

## Approval

Explicit owner direction in the supplied conversation.
