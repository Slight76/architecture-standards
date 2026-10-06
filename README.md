# Enterprise architecture standards

**v0.3.0 — implementation baseline for agent-assisted development.** Frontend and backend applications remain separate repositories with independent releases. This repository defines enterprise, solution, frontend, backend, database, integration, security, platform, and infrastructure design.

## Start here

1. Read [AGENTS.md](AGENTS.md) and [principles](ARCHITECTURE-PRINCIPLES.md).
2. Read the [implementation standards index](standards/README.md) and task-specific documents.
3. Apply the [adoption process](governance/adoption.md), pin a commit, and record required solution inputs.
4. Use the [solution template](templates/solution-architecture.md) and [agent bootstrap](templates/agent-bootstrap.md).
5. Verify applicable rules and report [implementation evidence](templates/implementation-evidence.md).

Using the handbook from an application repo with Copilot, Claude Code or Codex: copy the [consumer kit](consumer-kit/README.md). Edit the canonical skill in `skills/` and run `python3 scripts/sync_skills.py` to refresh the per-agent copies.

## What the baseline decides

| Concern | Recommended default | Detailed standard |
| --- | --- | --- |
| HTTP APIs | Resource-oriented JSON, explicit verbs/statuses, bounded collections, Problem Details | [API design](integration/http-api-standard.md) |
| Browser origins | Same-origin where appropriate; exact-origin CORS only when needed | [CORS](security/cors-standard.md) |
| Identity | BFF for sensitive first-party web; documented SPA PKCE alternative | [Identity](security/identity-standard.md) |
| Frontend | Strict TypeScript, feature boundaries, owned server/form/UI state | [Frontend](frontend/implementation-standard.md) |
| Backend | Modular monolith, inward dependencies, scoped use cases/persistence | [Backend](backend/implementation-standard.md) |
| CQRS | Logical command/query separation in one backend/store | [CQRS](backend/cqrs-standard.md) |
| Middleware | Explicit host order and separate transport/application behaviors | [Middleware](backend/middleware-standard.md) |
| Swagger/OpenAPI | One generator, version/audience documents, development UI default | [OpenAPI/Swagger](backend/openapi-swagger-standard.md) |
| Database | Owned relational models, constraints, compatible migrations, restore evidence | [Design](database/design-standard.md), [recovery](database/migration-recovery-standard.md) |
| Contracts | Versioned OpenAPI artifacts and pinned generated clients | [Contracts](integration/contracts-standard.md) |
| Retry/events/cache | Bounded safe retry, durable replay handling, optional asynchronous patterns | [Resilience](integration/messaging-resilience.md), [caching](backend/caching-standard.md) |
| Delivery | Independent immutable artifacts and boundary-specific checks | [Delivery](platform/delivery-standard.md), [testing](platform/testing-standard.md) |
| Operations | Correlated signals, distinct probes, measurable objectives | [Observability](platform/observability-standard.md) |
| Infrastructure | Requirement-led platform, explicit network/failure boundaries, reproducible IaC | [Infrastructure](infrastructure/implementation-standard.md) |
| Agent behavior | Task-scoped reading, pinned baseline, honest evidence and handoff | [Agent protocol](governance/agent-development-standard.md) |

Runtime/library versions, real origins, identity provider, owners, business permissions, capacities, retention and SLO/RPO/RTO values are supplied by the consuming solution. See [technology profile](standards/technology-profile.md).

## Decisions and enforcement

The [rule catalog](standards/catalog.json) maps every rule to its document, applicability, ADR, and verification. The [ADR index](adr/README.md) preserves foundational choices and includes CQRS, middleware, and OpenAPI/Swagger implementation decisions. Recommended technical choices remain Proposed until adopted by a solution; this is a usable baseline, not a production certification.

Run with Python 3.10 or later:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/check_adoption.py --baseline /path/to/architecture-baseline.json --evidence /path/to/implementation-evidence.json
```

The first two commands validate repository integrity and the validation tools. The adoption checker validates evidence structure and declared rule coverage; `--require-pass` rejects failed or unexecuted applicable checks. None proves that another application's runtime complies. Code fragments are illustrative and were not compiled as .NET/TypeScript applications here.

## Reuse and migration

See the [worked stock-adjustment design](solution/examples/stock-adjustment.md), [v0.1 migration guide](governance/migration-v0.2.md), [v0.3 adoption notes](governance/migration-v0.3.md), [changelog](CHANGELOG.md), and [primary-source register](standards/sources.md). No third-party application repo was changed by this revision. Select a license before authorizing broader redistribution.
