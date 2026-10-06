# Persistence, transactions, and query behavior

Baseline: 0.2.0 recommended draft. Applies when: a backend accesses relational data

Decision: [ADR-0018](../adr/0018-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Default

Use EF Core for the .NET relational profile, with provider-compatible pinned versions. Use explicit entity configurations in Infrastructure. SQL/Dapper may implement a query port when measurements justify it; retain parameterization, ownership, cancellation, and tests. No direct database access from the browser or unrelated service.

One business operation uses one deliberate local transaction. A single SaveChanges transaction can suffice; use an explicit transaction for multiple statements that must commit together. Set the isolation level based on invariants and contention rather than universally selecting serializable. Retry a transient transactional failure only by rerunning a safe whole unit of work with idempotency, not an arbitrary failed statement.

## Concurrency

Configure a version/concurrency token for mutable aggregate state. EF Core reports detected optimistic conflicts; map them intentionally rather than blindly retrying an outdated user edit. For invariant-sensitive quantity updates, use a conditional database update with expected version and check affected rows, or an appropriate locking/isolation strategy. Database constraints guard the final invariant. A query followed by an unconditional update is unsafe.

## Query discipline

Project only required columns, use no-tracking reads where modification tracking is unnecessary, and materialize within the owned port. Bound result sizes and avoid implicit lazy loading. Inspect generated SQL and query plans for critical paths. Define connection pool, command timeout, and query budgets with load evidence; do not fix exhaustion by indefinitely increasing pool size. Avoid N+1 round trips and unbounded Include graphs.

Use parameters for all data values and allowlists for dynamic identifiers. Never concatenate request values into SQL. Stored procedures are allowed when ownership, migrations, contracts, and performance evidence are maintained; they are not an alternate undocumented business layer. Use provider error classification to distinguish duplicate constraints from generic persistence failures.

## Example test requirements

Two callers read version 7. Caller A commits version 8. Caller B's version-7 update affects no row or raises the configured conflict and cannot overwrite A. An outbox or audit insert failure rolls back the entire intended transaction. Killing the process after commit but before response produces an idempotent replay, not a second adjustment.

An in-memory fake cannot prove relational constraint, collation, isolation, or migration behavior. Integration tests use the same engine family and relevant version/configuration as production, with isolated synthetic data and deterministic cleanup.

Sources: [EF Core concurrency](https://learn.microsoft.com/en-us/ef/core/saving/concurrency), [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| DATA-001 | Persistence MUST parameterize queries, bound results, and preserve module-owned access. | Injection, query-count, and maximum-result integration tests |
| DATA-002 | Multi-write business operations MUST have tested atomicity and concurrency behavior. | Rollback and competing-write tests on the actual engine |
| DATA-003 | Critical queries MUST have measured plans, indexes, and connection/timeout budgets. | Representative query/load report without sensitive data |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
