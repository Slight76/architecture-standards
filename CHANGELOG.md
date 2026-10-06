# Changelog

## Unreleased

- Added `CLAUDE.md` (`@AGENTS.md` import), a `consumer-kit/` for Copilot, Claude Code and Codex consumers, a shared `architecture-standards` skill with `scripts/sync_skills.py` drift check, `scripts/fetch_standards.py`, and validator checks for these files.

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
