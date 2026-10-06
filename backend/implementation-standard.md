# Backend modules, use cases, and dependencies

Baseline: 0.2.0 recommended draft. Applies when: an application uses the ASP.NET Core backend profile

Decision: [ADR-0018](../adr/0018-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Default architecture

Use a modular monolith until independent scaling, ownership, fault isolation, or delivery needs justify a service split. Separate frontend/backend repositories do not require one API per entity. Organize by business capability and use case within layers. Keep the model proportional: simple CRUD does not require aggregates, event sourcing, a mediator, or a generic repository framework.

| Project | Allowed project references | Responsibility |
| --- | --- | --- |
| Product.Domain | None of the application projects | Invariants and domain types |
| Product.Application | Domain | Use-case orchestration and ports |
| Product.Contracts | No Domain/Infrastructure/API references | External transport DTOs |
| Product.Infrastructure | Application, Domain | Persistence and remote adapters |
| Product.Api | Application, Contracts; Infrastructure at composition root only | HTTP, authentication, mapping, DI |
| Product.Worker if needed | Application; Infrastructure at composition root only | Durable background execution |

The API's Infrastructure reference exists to wire implementations; endpoint classes cannot use its database context. Mapping HTTP contracts into application inputs happens at the API boundary. Domain entities never serialize directly as API responses. A module's tables are private even if they share a physical database. Cross-module access uses a public module contract; forbid circular module dependencies.

## Use-case execution

An endpoint parses/binds a constrained DTO, authenticates and authorizes, invokes a use case, and maps its outcome to HTTP. Input-shape validation belongs at the boundary; invariants live in the domain; uniqueness/concurrency also require database enforcement. Do not rely on a preliminary query to prevent a race.

Use cases own the unit-of-work boundary. Default EF Core implementations live in Infrastructure behind use-case-specific query/write ports. Domain repository interfaces belong in Domain only if domain behavior needs the abstraction; otherwise put them in Application. Read ports return projections rather than loading large graphs. Do not return IQueryable across layers or require a generic repository merely to wrap every DbSet method.

A use case can use a concrete application service instead of mediator dispatch. Introduce mediator/pipeline libraries only when repeated behavior warrants them. Expected validation/conflict/not-found outcomes use explicit result types; unexpected faults go through one exception boundary. Do not catch every exception and return success/null.

## Runtime conventions

Enable nullable reference types, analyzers, and async I/O end-to-end. Public asynchronous operations use the Async suffix and accept cancellation where useful. Pass request cancellation to database/HTTP calls; do not use `.Result`, `.Wait()`, or Task.Run to hide synchronous I/O. DbContext has a unit-of-work scope, is not shared concurrently, and is not injected into singletons.

Validate typed configuration at startup. Separate environment configuration from secrets. Structured logging uses named fields and bounded values; log exceptions once at the accountable boundary. Carry verified actor/tenant scope separately from user-supplied DTOs. Use UTC instants and injected clock/ID abstractions when business tests need deterministic behavior.

## Example adjustment use case

`AdjustStock` receives item ID, delta, reason, expected version, and verified caller context. It checks operation permission and warehouse scope, loads the owned aggregate/version, applies the nonnegative-stock invariant, writes using atomic optimistic concurrency, and commits the adjustment/audit/idempotency result together. If publication is required, it writes an outbox entry in that transaction. It never performs an ERP HTTP call while holding the local transaction.

## Verification

Architecture checks assert forbidden assembly/package dependencies and the composition-root exception at namespace/type level. Assembly-only tests are insufficient to distinguish endpoints from bootstrap code in the same API project. Module boundary tests detect illegal imports and access paths. Unit tests exercise domain/use-case outcomes; database tests use the actual engine; API tests verify auth, validation, mapping, and error behavior. See [persistence](persistence-standard.md).


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| BE-006 | Backend implementations MUST enforce the project/module dependency matrix, including composition-root-only Infrastructure access. | Assembly plus namespace/type boundary checks |
| BE-007 | Use cases MUST own transaction scope and distinguish expected outcomes from unexpected failures. | Rollback, conflict, and error-mapping tests |
| BE-008 | Runtime code MUST use scoped persistence, async I/O, cancellation, and validated configuration. | Lifetime review, cancellation test, and invalid-config startup test |
| BE-009 | Input DTOs MUST NOT expose persistence entities or caller-controlled security context. | Contract and overposting/tenant-spoofing tests |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
