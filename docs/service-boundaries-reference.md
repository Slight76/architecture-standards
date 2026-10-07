---
title: "Service boundaries reference"
status: proposed
version: 1.0.0
owner: "@Slight76"
---
# Service boundaries reference

Baseline: 1.0.0. Applies when: deciding what becomes a module, a container, or a separate service, or when reviewing a proposed split or merge

Decision: [ADR-0029](../adr/0029-split-into-domain-handbooks.md). This document is guidance; it adds no rules. Binding requirements are SA-*(solution), BE-* (backend ownership), INT-*(integration), and DB-* in the [data handbook](https://github.com/Slight76/data-standards/blob/main/docs/database-architecture.md) (store ownership).

## Boundary candidates

Good boundaries usually line up with several of these at once:

| Signal | Question to ask |
| --- | --- |
| Business capability | Would a domain expert name this as one thing (orders, inventory, billing)? |
| Data ownership | Is there a set of tables only this part writes? |
| Consistency need | Do these operations need one transaction? If yes, same boundary. |
| Change together | Do these files change in the same pull requests? Check git history. |
| Language of the domain | Does the same word mean different things on either side (a "customer" to billing vs support)? |
| Lifecycle | Do these things get created, updated, and archived together? |

A boundary that satisfies only "it is a different noun" is a module at most, not a service.

## Module first, service later

1. Make the boundary a **module** inside the modular monolith: its own folder, its own schema or table prefix, public interface in one place, no reaching into another module's tables or internals.
2. Enforce it: architecture tests (for example, dependency rules in the test suite), separate EF Core `DbContext` per module where practical, and review.
3. Promote to a **service** only when a measured driver appears: independent scaling, isolation of a risky dependency, a different release cadence, or a different owner. Record the driver in an ADR.
4. When promoting, the module already owns its data and exposes one interface, so the split is mostly packaging plus a contract ([contracts standard](contracts-standard.md)) and an integration choice ([integration architecture](integration-architecture.md)).

## Cross-boundary interaction

| Need | Prefer | Avoid |
| --- | --- | --- |
| Read another boundary's data | Its API or a published read model | Querying its tables |
| Trigger work elsewhere after a change | Event with an idempotent consumer ([messaging](messaging-resilience.md)) | Synchronous call inside the transaction |
| Shared reference data | One owner publishes; others cache ([caching](https://github.com/Slight76/data-standards/blob/main/docs/caching-standard.md)) | Copying tables by hand |
| Shared code | Small versioned package or duplication | A "common" project that every boundary depends on for business logic |

## Smells that a boundary is wrong

- Two boundaries need a distributed transaction to do one user action.
- A change to one almost always requires a change to the other.
- One boundary's API is mostly CRUD passthrough of its tables for another boundary.
- Names only make sense with the other boundary's context.

Merging two boundaries is a valid outcome; record it the same way as a split.

## Related

[Architecture styles and trade-offs](architecture-styles-and-tradeoffs.md), [solution architecture](solution-architecture.md), [backend architecture](backend-architecture.md), [C4 views](c4-views.md).
