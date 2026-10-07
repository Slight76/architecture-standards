# architecture-standards

Team architecture standards for developers and AI agents: solution design, frontend and backend architecture, CQRS, middleware, OpenAPI, HTTP APIs, contracts, messaging and resilience, and the architecture decision record (ADR) process.

Part of the Slight76 standards handbooks indexed at [standards-marketplace](https://github.com/Slight76/standards-marketplace) alongside [engineering](https://github.com/Slight76/engineering-standards), [operations](https://github.com/Slight76/operations-standards), [data](https://github.com/Slight76/data-standards), and [security](https://github.com/Slight76/security-standards). Written for a small team and its agents. Version 1.0.0 is the first release after the repository split; see [CHANGELOG.md](CHANGELOG.md) and [MOVED.md](MOVED.md).

## Documents

| Document | Covers | Rule prefixes |
| --- | --- | --- |
| [Architecture principles](ARCHITECTURE-PRINCIPLES.md) | The principles every handbook specialises | - |
| [Solution architecture](docs/solution-architecture.md) | Mapping one outcome to applications, stores, and boundaries | SA |
| [Solution design and production readiness](docs/solution-design-standard.md) | What a solution document must decide before production | SA |
| [Frontend architecture](docs/frontend-architecture.md) | Independent SPA structure, state, routing, API access | FE |
| [Accessible and resilient user interfaces](docs/frontend-accessibility-performance.md) | Accessibility, performance budgets, failure states | UX |
| [Backend architecture](docs/backend-architecture.md) | Use-case oriented services, boundaries, ownership | BE |
| [CQRS and application execution](docs/cqrs-standard.md) | Command/query separation, handlers, pipelines | CQRS |
| [HTTP middleware and host composition](docs/middleware-standard.md) | Middleware order, lifetimes, errors, security headers | MW |
| [OpenAPI generation and Swagger UI](docs/openapi-swagger-standard.md) | First-party OpenAPI, transformers, exposure | OAS |
| [Integration architecture](docs/integration-architecture.md) | Synchronous vs asynchronous integration, ownership | INT |
| [HTTP API design](docs/http-api-standard.md) | Resource-oriented APIs, versioning, errors, pagination | API |
| [Contract ownership, generation, and compatibility](docs/contracts-standard.md) | Owned contracts, generated clients, compatibility | CON |
| [Idempotency, messaging, and resilience](docs/messaging-resilience.md) | Replay, delivery semantics, retries, timeouts | EVT, RES |
| [Architecture decision records](docs/architecture-decision-records.md) | When and how to write an ADR, where it lives, lifecycle | - |
| [Architecture views with C4](docs/c4-views.md) | Which diagrams to produce and how | - |
| [Architecture styles and trade-offs](docs/architecture-styles-and-tradeoffs.md) | Modular monolith default, when to split, checklist | - |
| [Service boundaries reference](docs/service-boundaries-reference.md) | Finding, enforcing, and promoting boundaries | - |
| [Examples](docs/examples/inventory.md) | Worked solution examples (inventory, stock adjustment) | - |
| [ADR index](adr/README.md) | All decisions, including historic ADR-0001..0027 and the v1.0.0 split (ADR-0028..0031) | - |

## Read by task

See [skills/architecture-standards/SKILL.md](skills/architecture-standards/SKILL.md). For tasks outside architecture (branching, tests, CI/CD, schemas, auth) start at the marketplace [routing table](https://github.com/Slight76/standards-marketplace#read-by-task).

## Install as an agent skill

| Agent | Command |
| --- | --- |
| Copilot CLI | `copilot plugin marketplace add Slight76/standards-marketplace` then `copilot plugin install architecture-standards@slight76-standards` |
| GitHub CLI (any agent) | `gh skill install Slight76/architecture-standards architecture-standards --scope user --pin v1.0.0` |
| Claude Code | `/plugin marketplace add Slight76/standards-marketplace` then `/plugin install architecture-standards@slight76-standards` |

Application repositories pin this handbook in `architecture-baseline.json` (`standards[]`, schema v2); see the marketplace [consumer kit](https://github.com/Slight76/standards-marketplace/blob/main/consumer-kit/README.md).

## Layout

| Path | Purpose |
| --- | --- |
| `docs/` | Standards documents (frontmatter, applies-when, rule table) |
| `catalog/catalog.json` | Machine-readable rules for this handbook; `externalDecisions` points at marketplace ADR-0001 |
| `adr/` | Architecture decision records (the team's ADR history lives here) |
| `skills/architecture-standards/` | Agent skill and references |
| `templates/solution-architecture.md` | Solution document template (shared templates live in the marketplace) |
| `governance/migration-*.md` | Historic migration notes for 0.2 and 0.3 |

Validation: `py ../standards-marketplace/tooling/validate.py --root .` (CI runs the same through the reusable marketplace workflow). License: [MIT](LICENSE).
