# Database architecture

Baseline: 0.3.0 recommended draft. Scope/decision: [ADR-0005](../adr/0005-database.md).

## Purpose

First-class logical and physical design. Choose storage based on transactions, queries, scale, recovery, and data sensitivity.

## Design

Logical design records entities, relationships, cardinality, invariants, classification, retention, and ownership. Physical design records engine/version, schemas, keys, indexes, partitions where justified, connections, replication, backup storage, and network boundaries. Within one modular monolith, module-owned schemas may share an instance; this does not grant cross-module writes. Separate services own their persistence and integrate via contracts. Use UTC instants and deliberate numeric precision. Review nullable fields and deletion behavior. Run expand migration, deploy compatible code, backfill with resumable batches, verify, then contract after the rollback window. A migration down script is not a safe default for restoring deleted data. Replication is not backup; rehearse full restores and point-in-time recovery if required.

## Rules and verification

| Rule | Requirement | Evidence |
| --- | --- | --- |
| DB-001 | Every persistent store and schema MUST have a named owning application/module and data steward. | Ownership register review |
| DB-002 | Schema changes MUST use committed migrations with expand/contract compatibility across supported releases. | Migration rehearsal and mixed-version integration tests |
| DB-003 | Relational integrity MUST use constraints where applicable; indexes MUST be justified by measured access patterns. | Constraint tests and query plan review |
| DB-004 | Runtime database identities MUST have least privilege and MUST NOT perform production schema administration. | Grant inspection |
| DB-005 | Production stores MUST define RPO/RTO, retention, backup encryption, and restore-test evidence. | Recovery exercise review |

## Adoption

Read [governance](../governance/adoption.md). Proposed rules are not approved merely because they use MUST. Record solution-specific choices, tests, and exceptions in the pinned baseline.

## Implementation standards

- [Logical and physical database design](design-standard.md)
- [Schema delivery and recovery](migration-recovery-standard.md)
