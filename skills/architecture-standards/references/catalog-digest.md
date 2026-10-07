# Catalog digest: architecture-standards

Generated from `catalog/catalog.json` (version 1.0.0). One line per rule; read the linked document for verification and applies-when.

| ID | Status | Statement | Document |
| --- | --- | --- | --- |
| SA-001 | Proposed | Every production solution MUST document context, deployables, repositories, owners, and external dependencies. | [solution-architecture.md](../../../docs/solution-architecture.md) |
| SA-002 | Proposed | Trust boundaries, data flows, failure modes, and deployment topology MUST be documented. | [solution-architecture.md](../../../docs/solution-architecture.md) |
| SA-003 | Proposed | Solutions MUST pin their standards baseline and record scoped exceptions. | [solution-architecture.md](../../../docs/solution-architecture.md) |
| FE-001 | Accepted | Frontend and backend MUST have separate application repositories and release pipelines. | [frontend-architecture.md](../../../docs/frontend-architecture.md) |
| FE-002 | Proposed | Features MUST NOT import another feature’s internal implementation; use its documented public API or app-level composition. | [frontend-architecture.md](../../../docs/frontend-architecture.md) |
| FE-003 | Proposed | HTTP calls MUST pass through the approved API client layer; generated files MUST NOT be manually edited. | [frontend-architecture.md](../../../docs/frontend-architecture.md) |
| FE-004 | Proposed | Business-specific logic MUST stay in its feature and shared code MUST NOT depend on features. | [frontend-architecture.md](../../../docs/frontend-architecture.md) |
| FE-005 | Proposed | UI MUST provide accessible keyboard navigation, semantic controls, and loading, empty, and failure states. | [frontend-architecture.md](../../../docs/frontend-architecture.md) |
| BE-001 | Proposed | Domain MUST NOT depend on Application, Infrastructure, API, HTTP, or persistence frameworks. | [backend-architecture.md](../../../docs/backend-architecture.md) |
| BE-002 | Proposed | Application MUST NOT depend on Infrastructure or API. | [backend-architecture.md](../../../docs/backend-architecture.md) |
| BE-003 | Proposed | Infrastructure MUST implement ports owned by Application or Domain. | [backend-architecture.md](../../../docs/backend-architecture.md) |
| BE-004 | Proposed | Endpoints MUST delegate business decisions to application/domain code and enforce documented authorization. | [backend-architecture.md](../../../docs/backend-architecture.md) |
| BE-005 | Proposed | Module data MUST be accessed through its owned interfaces; cross-module writes MUST NOT bypass ownership. | [backend-architecture.md](../../../docs/backend-architecture.md) |
| INT-001 | Proposed | HTTP APIs MUST publish versioned OpenAPI artifacts and use a documented error contract. | [integration-architecture.md](../../../docs/integration-architecture.md) |
| INT-002 | Proposed | Breaking contract changes MUST retain a documented migration and supported compatibility window. | [integration-architecture.md](../../../docs/integration-architecture.md) |
| INT-003 | Proposed | Mutation retries MUST account for idempotency and ambiguous network outcomes. | [integration-architecture.md](../../../docs/integration-architecture.md) |
| INT-004 | Proposed | Trace context MUST propagate across supported boundaries without secrets or sensitive payloads in telemetry. | [integration-architecture.md](../../../docs/integration-architecture.md) |
| API-001 | Proposed | APIs MUST follow the resource, method, representation, and status conventions in this document. | [http-api-standard.md](../../../docs/http-api-standard.md) |
| API-002 | Proposed | Collection endpoints MUST bound results and allowlist query operations. | [http-api-standard.md](../../../docs/http-api-standard.md) |
| API-003 | Proposed | Application errors MUST use the documented problem contract and stable codes. | [http-api-standard.md](../../../docs/http-api-standard.md) |
| API-004 | Proposed | Updates vulnerable to lost writes MUST enforce an atomic concurrency policy. | [http-api-standard.md](../../../docs/http-api-standard.md) |
| CON-001 | Proposed | API consumers MUST pin reproducibly generated client contracts to immutable artifacts. | [contracts-standard.md](../../../docs/contracts-standard.md) |
| CON-002 | Proposed | Provider changes MUST assess structural and behavioral compatibility with supported consumers. | [contracts-standard.md](../../../docs/contracts-standard.md) |
| CON-003 | Proposed | Every operation MUST document auth, validation, errors, concurrency, and retry behavior. | [contracts-standard.md](../../../docs/contracts-standard.md) |
| RES-001 | Proposed | Outbound calls MUST declare bounded deadlines and operation-safe retry behavior. | [messaging-resilience.md](../../../docs/messaging-resilience.md) |
| RES-002 | Proposed | Replay-sensitive mutations MUST implement a durable scoped idempotency protocol. | [messaging-resilience.md](../../../docs/messaging-resilience.md) |
| EVT-001 | Proposed | Reliable database-to-event publication MUST coordinate through an outbox or documented equivalent. | [messaging-resilience.md](../../../docs/messaging-resilience.md) |
| EVT-002 | Proposed | Consumers MUST handle duplicates, poison messages, shutdown, and authorized redrive. | [messaging-resilience.md](../../../docs/messaging-resilience.md) |
| UX-001 | Proposed | User journeys MUST support keyboard, focus, labels, error announcements, and the adopted accessibility target. | [frontend-accessibility-performance.md](../../../docs/frontend-accessibility-performance.md) |
| UX-002 | Proposed | Applications MUST define measured performance budgets and asset/configuration caching behavior. | [frontend-accessibility-performance.md](../../../docs/frontend-accessibility-performance.md) |
| SA-004 | Proposed | Solution designs MUST resolve cross-domain implementation choices and document measurable quality scenarios. | [solution-design-standard.md](../../../docs/solution-design-standard.md) |
| SA-005 | Proposed | Production readiness MUST include failure, compatibility, security, operations, and recovery evidence. | [solution-design-standard.md](../../../docs/solution-design-standard.md) |
| CQRS-001 | Proposed | Business use cases MUST distinguish commands from queries without requiring separate stores or a mediator. | [cqrs-standard.md](../../../docs/cqrs-standard.md) |
| CQRS-002 | Proposed | Queries MUST NOT mutate authoritative business state; commands MUST own atomic invariant enforcement. | [cqrs-standard.md](../../../docs/cqrs-standard.md) |
| CQRS-003 | Proposed | Separate read models MUST declare consistency, authorization, lag, and rebuild behavior. | [cqrs-standard.md](../../../docs/cqrs-standard.md) |
| CQRS-004 | Proposed | Application pipelines MUST preserve authorization, replay, and transaction semantics across HTTP and worker callers. | [cqrs-standard.md](../../../docs/cqrs-standard.md) |
| MW-001 | Proposed | Backend hosts MUST centralize visible service/pipeline/endpoint composition and preserve documented ordering dependencies. | [middleware-standard.md](../../../docs/middleware-standard.md) |
| MW-002 | Proposed | Custom middleware MUST respect DI lifetimes, cancellation, response-start and streaming behavior. | [middleware-standard.md](../../../docs/middleware-standard.md) |
| MW-003 | Proposed | Exception, validation, authentication and throttling paths MUST retain safe consistent HTTP error behavior. | [middleware-standard.md](../../../docs/middleware-standard.md) |
| MW-004 | Proposed | Cookie mutation and identity-based throttling controls MUST be enforced by tested endpoint/pipeline behavior. | [middleware-standard.md](../../../docs/middleware-standard.md) |
| OAS-001 | Proposed | Backends MUST use one declared OpenAPI generator with stable document/audience/version ownership. | [openapi-swagger-standard.md](../../../docs/openapi-swagger-standard.md) |
| OAS-002 | Proposed | OpenAPI responses, schemas and security metadata MUST match implemented endpoint behavior. | [openapi-swagger-standard.md](../../../docs/openapi-swagger-standard.md) |
| OAS-003 | Proposed | Swagger UI and document exposure MUST follow explicit environment policy without weakening API security. | [openapi-swagger-standard.md](../../../docs/openapi-swagger-standard.md) |
| OAS-004 | Proposed | Build-time contract generation MUST be isolated from production effects and pass consumer generation checks. | [openapi-swagger-standard.md](../../../docs/openapi-swagger-standard.md) |
