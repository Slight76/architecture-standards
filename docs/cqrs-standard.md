---
title: "CQRS and application execution"
status: proposed
version: 1.0.0
owner: "@Slight76"
supersedes: architecture-standards/backend/cqrs-standard.md@c1bda3d
---
# CQRS and application execution

Baseline: 1.0.0. Applies to the ASP.NET Core backend profile. Decision: [ADR-0025](../adr/0025-cqrs.md). Effective when adopted by the solution.


## How it relates to REST and CORS

CQRS separates read and write application models/operations. REST describes an API architectural style; a resource-oriented HTTP endpoint can invoke a CQRS handler. CORS governs browser cross-origin response access. These decisions are independent and may coexist.

## Default: logical separation in one application and database

Use lightweight command/query separation for business use cases: command handlers mutate authoritative state, query handlers return purpose-built projections. Keep one deployed backend and one owned relational store initially. Separate read/write databases, asynchronous projections, event sourcing, message buses, and a mediator library are not prerequisites. Simple CRUD may use distinct methods on an application service when handler classes would add no useful boundary; preserve read/write semantics and testability.

| Situation | Profile choice |
| --- | --- |
| Simple read/write feature | Separate command/query methods or handlers in the existing module |
| Complex invariants/workflows | Dedicated commands with domain behavior and transaction boundary |
| Queries with different shape from aggregates | Dedicated projections via owned query ports |
| Measured read scaling or specialized search requirement | Consider a separate read model/store through a solution ADR |
| Need complete event history/replay as authoritative model | Evaluate event sourcing separately; do not infer it from CQRS |

## Feature structure

| Location | Example contents |
| --- | --- |
| Application/Inventory/Commands/AdjustStock | AdjustStockCommand, AdjustStockHandler, validation and result |
| Application/Inventory/Queries/GetStockItem | GetStockItemQuery, GetStockItemHandler, StockItemView |
| Application/Inventory/Ports | IStockWriter, IStockQueries, unit-of-work port where required |
| Domain/Inventory | StockItem and stock invariants |
| Infrastructure/Inventory/Persistence | EF mappings, write adapter and projected query adapter |
| Api/Endpoints/Inventory | HTTP request-to-use-case mapping and response metadata |
| Contracts/Inventory | External request/response DTOs; no handler or persistence dependencies |

A query DTO is not automatically the public HTTP DTO. Map where their ownership or meaning differs. Handlers cannot depend on HttpContext, controller results, Swagger types, or persistence contexts. Query ports return bounded materialized projections; do not expose IQueryable to another layer.

## Command semantics

Name a command for business intent: AdjustStock, ReserveStock, CancelReservation. Carry only required inputs, expected version when relevant, and replay key where appropriate. Verified actor/tenant context comes through a trusted application abstraction; do not accept it from a body field without membership verification.

Commands may return a created ID, new version, or useful small result. They do not have to return void. Exactly one use case owns the transaction. Apply input validation, authorization/resource scope, invariant checks, and atomic concurrency controls. Commit domain writes, audit/replay records, and outbox entries together when required. A command handler must not call another command handler through a dispatcher and accidentally create nested transactions; extract shared domain/application collaborators instead.

A request cancellation or timeout does not prove rollback. If the database committed before the connection failed, replay/reconciliation must resolve the outcome using the idempotency protocol. Never automatically retry every command through a generic retry behavior.

## Query semantics

Queries do not modify business state or call SaveChanges. Diagnostic telemetry and replaceable cache population are allowed when they do not change business semantics. Query handlers authorize their scope, project only needed fields, bound/filter/sort results, and propagate cancellation. They may use efficient SQL/EF projections through Infrastructure ports without reconstructing write aggregates. A no-tracking query is not permission to ignore tenant isolation.

A command should enforce invariants against authoritative state inside its transaction, not depend on a possibly stale query/read model to authorize a write. Default reads go to the primary store for simple read-after-write behavior. If replicas or asynchronous projections are introduced, explicitly document lag, causal/read-your-writes strategy, UI pending state, and failure/rebuild behavior.

## Application pipeline versus HTTP middleware

Transport middleware handles HTTP concerns. Use-case decorators/behaviors handle application execution and must work for API and worker callers. A mediator is optional; direct DI handlers or explicit decorators are valid. Choose one dispatch mechanism per backend and pin any third-party library after compatibility/license review.

Recommended application stages: execution context/telemetry; shape validation; operation permission; command replay/transaction coordinator where applicable; handler with resource authorization and domain invariants; commit; result mapping at the transport boundary. Resource authorization must be checked before returning a replay result. Transaction and deduplication ordering must follow the durable atomic protocol rather than independent generic behaviors that each commit.

Queries bypass write transactions and replay storage. Domain validation is not duplicated mechanically into every layer: each layer enforces the rules it owns. Authentication/HTTP response writing never belongs in an application behavior.

## Handler contract sketch

Illustrative signatures only; not compiled in this standards repo. Types such as UseCaseResult and caller context are application-owned, not mandated library APIs.

```csharp
public sealed record AdjustStockCommand(
    Guid ItemId, int Delta, string Reason, long ExpectedVersion);
public sealed record GetStockItemQuery(Guid ItemId);

// On distinct handlers; implementations use owned ports and verified caller context.
Task<UseCaseResult<StockAdjustmentResult>> HandleAsync(
    AdjustStockCommand command, CancellationToken cancellationToken);
Task<UseCaseResult<StockItemView>> HandleAsync(
    GetStockItemQuery query, CancellationToken cancellationToken);
```

## Acceptance cases

Verify query execution leaves authoritative rows/versions unchanged; commands enforce invariants and rollback together; another tenant cannot query or mutate the item; duplicate command delivery produces one effect; two conflicting commands cannot overwrite each other; workers invoke the same authorization/business policy through a valid execution context. If a separate read model exists, test stale reads, replay, projection recovery, schema evolution, and rebuild from a documented source.

Avoid giant command/query classes serving every feature, mandatory mediator packages, one database per handler, event sourcing by default, and handlers invoking HTTP endpoints internally.

Source: [Microsoft CQRS pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs). Folder layout and default execution policy are repository design choices. Related: [persistence](https://github.com/Slight76/data-standards/blob/main/docs/persistence-standard.md), [idempotency and messaging](messaging-resilience.md).


## Rules and evidence

| Rule | Requirement | Verification |
| --- | --- | --- |
| CQRS-001 | Business use cases MUST distinguish commands from queries without requiring separate stores or a mediator. | Use-case classification and handler dependency review |
| CQRS-002 | Queries MUST NOT mutate authoritative business state; commands MUST own atomic invariant enforcement. | Read-side no-write and command rollback/concurrency tests |
| CQRS-003 | Separate read models MUST declare consistency, authorization, lag, and rebuild behavior. | Replica/projection lag, tenant isolation and rebuild tests when applicable |
| CQRS-004 | Application pipelines MUST preserve authorization, replay, and transaction semantics across HTTP and worker callers. | API/worker equivalence, replay authorization and single-transaction tests |

## Exceptions

Record a scoped, approved, time-bounded [exception](https://github.com/Slight76/standards-marketplace/blob/main/templates/exception.md) rather than silently changing the profile.
