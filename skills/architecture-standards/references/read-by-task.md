# Read by task: architecture-standards

Paths are relative to the repository root. Read the listed documents and the ADR each links; do not read the whole handbook.

| Task | Documents | Key rules |
| --- | --- | --- |
| Start a new solution; define outcome, applications, stores | `docs/solution-architecture.md`, `docs/solution-design-standard.md`, `templates/solution-architecture.md` | SA-* |
| Split or merge a service; change a boundary | `docs/solution-architecture.md`, `docs/backend-architecture.md`, `docs/integration-architecture.md` | SA-*, BE-*, INT-* |
| Choose synchronous call vs event/message | `docs/integration-architecture.md`, `docs/messaging-resilience.md` | INT-*, EVT-*, RES-* |
| Design or change an HTTP endpoint | `docs/http-api-standard.md` | API-* |
| Generate or publish OpenAPI / Swagger UI | `docs/openapi-swagger-standard.md` | OAS-* |
| Own a contract; generate a client; break compatibility | `docs/contracts-standard.md` | CON-* |
| Add retries, timeouts, idempotency keys, replay handling | `docs/messaging-resilience.md` | EVT-*, RES-* |
| Add a use case, command, or query handler | `docs/backend-architecture.md`, `docs/cqrs-standard.md` | BE-*, CQRS-* |
| Change middleware order, error handling, host composition | `docs/middleware-standard.md` | MW-* |
| Structure a frontend feature, state, or routing | `docs/frontend-architecture.md` | FE-* |
| Accessibility, performance budget, failure states in UI | `docs/frontend-accessibility-performance.md` | UX-* |
| Record a decision | `adr/README.md`; marketplace `templates/adr.md` | - |
| Review a solution document | `docs/solution-design-standard.md`, `docs/examples/inventory.md`, `docs/examples/stock-adjustment.md` | SA-* |

Related handbooks: engineering (implementation, tests, branching), operations (delivery, observability, infrastructure), data (schemas, migrations, caching), security (identity, CORS, secrets). Routing table: <https://github.com/Slight76/standards-marketplace#read-by-task>.
