# Schema delivery and recovery

Baseline: 0.2.0 recommended draft. Applies when: a solution changes or operates a production database

Decision: [ADR-0019](../adr/0019-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Migration workflow

Commit migrations with the application/module owning the schema. Run a dedicated deployment step with a schema identity; runtime identities cannot administer schema. Do not migrate production from every API instance on startup. Generate reviewable scripts or bundles and inspect the generated SQL for accidental drops, table rewrites, lock duration, and engine-specific transactional restrictions.

Rehearse both empty-database setup and upgrade from each supported release state. Record estimated row counts, lock budget, disk growth, timeout/abort behavior, backup verification, and operational owner. Serialize migration execution and make failure recovery observable. Never edit a migration that has already been applied in a shared environment; append a correction.

## Expand/contract example

To replace `name` with `display_name`: add a nullable new column; deploy code that can read old/new shapes and maintain required writes; backfill in resumable bounded batches; verify counts and semantics; switch reads; retire old consumers; remove the old column after the compatibility/rollback window. A schema removal cannot be hidden inside a supposedly safe application rollback.

Separate code rollback from data recovery. A down migration that deletes new data is not automatically safe. Prefer forward correction when rollback would lose writes. Document how to pause writes, reconcile partial backfills, and resume from a checkpoint. Test mixed application versions while compatible migrations are in place.

## Backup and restore

Choose logical dumps, physical backups, and continuous log archiving according to approved RPO/RTO and engine capability. Capture roles/configuration/extensions and encryption-key dependencies needed to restore. Replicas copy accidental deletion and are not backups. Protect backup access separately from application identities and record retention, immutability/offline controls where required, and restoration permissions.

For each production store, schedule restore exercises at an owner-defined interval and after material recovery changes. Restore to an isolated environment, verify consistency and application compatibility, measure actual data loss and recovery time, and record evidence against targets. A completed backup job alone is not proof of recovery. Recovery includes connection routing, identities, keys, images, migrations, and validation before reopening writes.

## Required runbook steps

Detect and classify corruption/outage; assign incident authority; preserve evidence; select recovery point; provision isolated target; restore and validate; reconcile data created after that point; switch traffic under controlled ownership; verify business operations; monitor; record actual RPO/RTO and follow-up work. Include abort points and contacts, not only commands.

Sources: [EF migration deployment](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying), [PostgreSQL backup overview](https://www.postgresql.org/docs/current/backup.html). The delivery/rehearsal lifecycle is our policy.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| MIG-001 | Production migrations MUST be reviewed, rehearsed, serialized, and executed by a separate deployment identity. | Fresh and upgrade migration runs plus grant checks |
| MIG-002 | Destructive schema changes MUST preserve the supported compatibility window and define data-safe recovery. | Mixed-version and interrupted-backfill tests |
| DR-001 | Production stores MUST demonstrate restoration against approved RPO/RTO using measured evidence. | Isolated restore report including keys, roles, and application validation |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
