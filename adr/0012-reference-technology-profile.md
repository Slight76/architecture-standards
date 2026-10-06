# ADR-0012: Reference technology profile

Status: Proposed

Date: 2026-10-05

## Context

Applications need a reusable enterprise design and instructions that agents can apply consistently.

## Decision

Consider React/TypeScript for the client, ASP.NET Core for APIs, and PostgreSQL for relational persistence. Select supported versions and lockfiles when creating templates. No runtime version, identity provider, UI library, cloud, orchestrator, or messaging product is approved by this record.

## Alternatives

Implicit conventions reduce initial effort but allow drift. Explicit versioned decisions require maintenance but support repeatable implementation.

## Consequences

Maintain baseline pins and compatibility evidence. Do not confuse independent applications with independent business capabilities or require distributed systems without justification.

## Traceability

[Agent instructions](../AGENTS.md), [frontend](../frontend/architecture.md), [backend](../backend/architecture.md), [integration](../integration/architecture.md), [governance](../governance/adoption.md).

## Verification

Review repository separation, local bootstrap, immutable baseline reference, and applicable checks.

## Approval

Pending owner review.
