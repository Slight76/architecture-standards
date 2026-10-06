# Adopt v0.2 from v0.1

v0.2 expands the draft with implementation defaults and verification. This is a pre-1.0 baseline revision and includes policy changes; existing applications remain on their pinned revision until deliberately migrated.

1. Inventory current origins, identity, endpoints, generated clients, module imports, database ownership, migrations, and release checks.
2. Review new ADR-0013 through ADR-0024 and all applicable detailed standards.
3. Create a migration issue for actual differences. Do not enable CORS simply because the new document exists.
4. Fill the new manifest: immutable commit, adoption record, all catalog rules classified as applicable/excluded, and accepted exceptions.
5. Establish rule-to-check evidence. Not-yet-run checks remain not_run until executed.
6. Test mixed client/server versions, database compatibility, session behavior, and recovery before production rollout.
7. Pin v0.2 through the application's normal reviewed change process.

Changes include explicit HTTP/version/pagination defaults, named identity profiles, strict frontend state/import choices, backend composition-root enforcement, durable idempotency guidance, migration/restore procedures, and release evidence. Proposed/Accepted labeling is corrected for earlier scope-only approvals. No global migration or application edits occur merely by publishing this repository revision.
