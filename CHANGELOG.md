# Changelog

## 1.0.0 - 2026-10-06

Repository split (ADR-0028..0031). History before this release is tagged `v0.3.0-pre-split`.

- Retired the "enterprise" layer; the team operating model, governance rules (GOV-*), templates, consumer kit, and tooling now live in [standards-marketplace](https://github.com/Slight76/standards-marketplace). EA-001..EA-006 are Superseded by GOV-001.
- Moved engineering, operations, data, and security standards to their own handbooks; see [MOVED.md](MOVED.md) for every old path and its new home.
- Remaining documents moved under `docs/` with frontmatter; rule IDs unchanged. Catalog is now `catalog/catalog.json` (44 rules: SA, FE, UX, BE, CQRS, MW, OAS, API, CON, EVT, RES, INT) with `externalDecisions` pointing at marketplace ADR-0001.
- Added `plugin.json` (Agent Plugins 1.0) and `skills/architecture-standards/`; removed mirrored `.agents/`, `.claude/`, `.github/skills/` copies and `scripts/sync_skills.py`.
- CI uses the reusable `standards-marketplace` docs-lint workflow. Added MIT license; repository is public.
- Amended ADR-0001..0012 and ADR-0022 with historical notes; ADR-0001 and ADR-0023 superseded by ADR-0028.

## 0.3.0 — 2026-10-05

- Added logical CQRS defaults, command/query structure and application execution boundaries.
- Defined middleware composition, ordering, lifetime/error/security behavior and real-host acceptance tests.
- Selected first-party OpenAPI generation plus Swagger UI, with transformers, audience/version organization, exposure policy and contract-generation checks.
- Added ADR-0025 through ADR-0027 and 12 rules; retained conditional browser CORS guidance.
- Updated agent reading paths and application baseline templates.

## 0.2.0 — 2026-10-05

- Added detailed implementation standards across all nine domains, plus an agent execution/evidence protocol.
- Defined HTTP API conventions, conditional CORS, named identity profiles, generated contracts, concurrency, idempotency, asynchronous delivery, and cache limits.
- Specified frontend state/import ownership, backend dependency/transaction rules, schema design, migration/recovery, and operational acceptance cases.
- Added ADR-0013 through ADR-0024, task reading maps, technology defaults, adoption/exception/evidence templates, and a worked stock adjustment.
- Strengthened catalog/link/ADR checks and added consumer manifest/evidence validation with negative tests.
- Corrected approval labels that previously confused accepted documentation scope with acceptance of detailed technical rules.

## 0.1.0 — 2026-10-05

Initial domain architecture documents, foundational ADRs, agent bootstrap, and documentation integrity workflow.
