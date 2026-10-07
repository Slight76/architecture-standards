---
title: "Architecture styles and trade-offs"
status: proposed
version: 1.0.0
owner: "@Slight76"
---
# Architecture styles and trade-offs

Baseline: 1.0.0. Applies when: choosing or revisiting the shape of a solution (how many deployables, how they talk, where state lives)

Decision: [ADR-0029](../adr/0029-split-into-domain-handbooks.md). This document is guidance; it adds no rules. Boundary and integration rules live in [solution architecture](solution-architecture.md) (SA-*), [backend architecture](backend-architecture.md) (BE-*), and [integration architecture](integration-architecture.md) (INT-*).

## Default for this team

Start with a **modular monolith per solution**: one .NET API container with clear internal modules, one PostgreSQL database it owns, one independent React SPA, and background work in the same deployable (or a second worker container when scheduling or scaling demands it). Split only when a measured reason appears (see [service boundaries](service-boundaries-reference.md)). This keeps a small team's operational surface small while preserving the module seams needed to split later.

## Styles compared

| Style | Choose when | Costs you accept | Watch for |
| --- | --- | --- | --- |
| Modular monolith | Default; one team, one deploy cadence | Shared release; module discipline enforced by review and tests | Modules leaking into each other through shared tables or static helpers |
| Separate frontend and backend (always) | Always; see ADR-0010 | Contract ownership and generated clients | Frontend coupling to persistence shapes |
| Few services (2-5) | Independent scaling, isolation, or cadence is measured, not assumed | Network failure modes, versioned contracts, distributed tracing | Chatty synchronous chains; shared databases |
| Event-driven | Work is naturally asynchronous, must survive consumer downtime, or fans out | Idempotency, replay, ordering, dead-letter handling (EVT-*, RES-*) | Using events for request/response; hidden coupling through event schemas |
| CQRS inside a service | Read and write models diverge or reads need different storage/scaling | Two models to keep consistent (CQRS-*) | Introducing eventual consistency the UI does not expect |
| Serverless functions | Rare, spiky, isolated jobs | Cold starts, vendor runtime limits, harder local dev | Spreading business logic across many tiny units |

## Trade-off checklist

Record the answers in the solution document or an ADR:

1. **Change cadence** - do parts need to ship independently? Evidence: release history, not intuition.
2. **Scaling shape** - which part saturates first and on what axis (CPU, memory, connections, I/O)?
3. **Failure isolation** - what must keep working when something else is down?
4. **Data ownership** - can each proposed unit own its data outright? If two units need the same tables, they are one unit.
5. **Team shape** - who is on call for each unit? One person cannot own five services well.
6. **Cost** - containers, databases, queues, telemetry, and egress all multiply with units.
7. **Reversibility** - how hard is it to merge back? Prefer steps that are cheap to undo.

## Anti-patterns

- Distributed monolith: many deployables that must release together.
- Shared database between services.
- Synchronous chains more than two hops deep on a user request.
- Choosing a style because a reference architecture used it; the operating model forbids importing targets the solution did not measure.

## Related

[Integration architecture](integration-architecture.md), [messaging and resilience](messaging-resilience.md), [C4 views](c4-views.md), operations handbook [platform architecture](https://github.com/Slight76/operations-standards/blob/main/docs/platform-architecture.md).
