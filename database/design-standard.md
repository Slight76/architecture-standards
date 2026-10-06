# Logical and physical database design

Baseline: 0.2.0 recommended draft. Applies when: a solution persists structured business data

Decision: [ADR-0019](../adr/0019-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Storage selection

Default to relational storage for transactional records and integrity across related entities. The reference profile uses PostgreSQL. A document store requires evidence for document aggregate/query/scale needs; object storage owns large files; a search index is a derived model; a cache is replaceable. Record the source of truth and rebuild path for every derived store. Avoid adding a new engine to sidestep schema design.

Each service owns its database/schema model and runtime identity. Modules of one backend may share an instance with separately owned schemas. Cross-service database joins and writes are prohibited by default; use APIs/events or an explicitly governed analytical pipeline. Logical isolation does not imply separate hardware for every module.

## Naming and types

Use lower snake_case for PostgreSQL schemas, plural tables, and columns. Primary key `id`; references `<entity>_id`; timestamp columns `created_at`/`updated_at`. Avoid quoted case-sensitive identifiers. Constraint/index names use readable purpose prefixes and stay within engine limits. Map C# names explicitly rather than changing domain language to match SQL.

Use UUID identifiers by default for distributed creation needs; choose bigint identity for suitable local tables with a documented reason. Identifier type does not establish authorization. Use timestamptz for instants and date for calendar-only values; store a separate IANA time-zone identifier when future local scheduling requires it. Use numeric with explicit precision/scale for exact quantities/money; define rounding and currency semantics. Null means absence/unknown by contract, not zero or empty string.

Normalize transactional data by default. Denormalize only with an owner, consistency strategy, and rebuild process. Add primary/unique/foreign/check constraints for invariants expressible by the engine. Deliberately choose ON DELETE behavior; do not apply cascade everywhere. Index child foreign keys when access/deletion patterns require it; do not assume every engine creates those indexes for you.

## Tenant and lifecycle design

Choose shared schema with tenant keys versus dedicated stores from isolation requirements and operating cost. For shared tables, scoped unique keys and references must prevent cross-tenant association. Row-level security is a defense option, not a replacement for application authorization; test pooled-connection context reset if used. Define classification, retention clock, deletion/anonymization, legal holds where applicable, and how backups age out. Avoid universal soft-delete because it affects uniqueness, reads, storage, and erasure.

## Design evidence

For each aggregate provide a logical ER view, authoritative invariants, read/write access patterns, expected volume/growth, physical key/index choices, retention, and owning module. Validate a migration against representative distributions, not only ten rows. Review EXPLAIN plans safely; ANALYZE executes the statement, so use non-production data or an explicitly approved safe procedure.

An example stock table needs a unique tenant/SKU key, quantity constraint, concurrency version, and a tenant-consistent warehouse relationship. Do not specify arbitrary production capacity or retention periods without business inputs.

Source: [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html). Naming, identifier defaults, and ownership are our policy choices.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| DB-006 | Each store MUST document source-of-truth ownership, classification, lifecycle, and logical/physical design. | ER model, ownership and retention review |
| DB-007 | Relational models MUST use deliberate naming/types, integrity constraints, and tenant-consistent keys. | Constraint, precision, deletion, and tenant-link tests |
| DB-008 | Derived stores MUST document consistency, invalidation, and rebuild paths. | Source loss/cache flush/rebuild exercise |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
