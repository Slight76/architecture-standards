# Technical source register

Checked 2026-10-05. These primary sources ground protocol/framework facts. Enterprise choices such as library defaults, route naming, pagination limits, and approval workflow are this repository's recommendations, not requirements imposed by the sources. Check versioned documentation again when implementing or upgrading a runtime.

| Topic | Source | Scope used |
| --- | --- | --- |
| HTTP | [RFC 9110](https://httpwg.org/specs/rfc9110.html) | Methods, status and preconditions |
| Errors | [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457) | Problem details format |
| CORS | [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/cors?view=aspnetcore-10.0) | Origin policy and middleware order |
| OAuth | [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700) | Modern OAuth security practices |
| CSRF | [ASP.NET antiforgery](https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery?view=aspnetcore-10.0) | Cookie-authenticated request protection |
| Contracts | [OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html) | Machine-readable operation contracts |
| React | [State structure](https://react.dev/learn/choosing-the-state-structure) | Avoid duplicated state |
| TypeScript | [Strict](https://www.typescriptlang.org/tsconfig/strict.html) | Strict compiler option |
| Query client | [TanStack Query keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys) | Query identity and inputs |
| Forms | [React Hook Form](https://github.com/react-hook-form/react-hook-form) | Form-library capability |
| Runtime validation | [Zod](https://zod.dev/) | Schema validation capability |
| Frontend tests | [Vitest](https://vitest.dev/guide/), [Playwright](https://playwright.dev/docs/api/class-test) | Unit and browser testing capabilities |
| Concurrency | [EF Core](https://learn.microsoft.com/en-us/ef/core/saving/concurrency) | Optimistic concurrency conflicts |
| Migrations | [EF Core deployment](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying) | Script/bundle review and identities |
| Constraints | [PostgreSQL](https://www.postgresql.org/docs/current/ddl-constraints.html) | Integrity constraints |
| Recovery | [PostgreSQL backup](https://www.postgresql.org/docs/current/backup.html) | Backup categories |
| CI security | [GitHub secure use](https://docs.github.com/en/actions/reference/security/secure-use) | Workflow permissions and untrusted inputs |
| Telemetry | [OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/) | Signal concepts |
| Accessibility | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Accessibility target and testing scope |
