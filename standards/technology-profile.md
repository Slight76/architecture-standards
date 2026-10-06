# Recommended technology profile

Status: Proposed; effective for applications that adopt v0.2.0 and select this profile. Version pins must be resolved against supported vendor releases at template creation and committed; this document intentionally does not invent package versions.

| Responsibility | Default | Alternative trigger |
| --- | --- | --- |
| Business web client | React + TypeScript + Vite | SSR/SSG or another framework has a documented requirement |
| Routing | React Router | Existing supported framework routing or explicit feature need |
| Server state | TanStack Query | Framework data layer meeting cache/cancellation requirements |
| Forms | Local React state; React Hook Form for complex forms | Existing supported design-system form solution |
| Runtime validation | Zod | Contract-generated validator or compatible established library |
| UI components | Adopt one maintained accessible design system per solution | Existing enterprise system; do not mix libraries arbitrarily |
| Backend | Supported ASP.NET Core LTS profile | Workload or enterprise platform constraints |
| Persistence | EF Core + compatible PostgreSQL provider | Measured query needs through SQL/Dapper ports |
| Relational engine | Supported PostgreSQL | Existing SQL Server/other enterprise requirement with equivalent controls |
| Testing | xUnit; Vitest/Testing Library; Playwright | Existing equivalent tested stack |
| Telemetry | OpenTelemetry-compatible signals | Exporter/backend selected by enterprise/solution |
| API client generation | OpenAPI-derived typed client | Select generator/version after compatibility spike |
| Local orchestration | Documented service startup; Aspire optional | Docker Compose or existing local platform |
| Hosting/messaging/cache | No universal vendor mandate | Select from measured solution requirements |

A default answers the normal choice; an alternative needs a recorded reason and equivalent evidence. Package support, licenses, runtime/provider compatibility, and security updates are checked when pinned. There is no hidden requirement for Kubernetes, Redis, RabbitMQ, or a particular cloud.
