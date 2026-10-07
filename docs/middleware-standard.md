---
title: "HTTP middleware and host composition"
status: proposed
version: 1.0.0
owner: "@Slight76"
supersedes: architecture-standards/backend/middleware-standard.md@c1bda3d
---
# HTTP middleware and host composition

Baseline: 1.0.0. Applies to the ASP.NET Core backend profile. Decision: [ADR-0026](../adr/0026-middleware.md). Effective when adopted by the solution.


## Composition structure

Keep Program.cs as the readable composition root. Declare middleware order in one place; do not scatter Use... calls across modules that secretly reorder security. Registration extensions configure services, pipeline extensions configure ordered HTTP behavior, endpoint extensions map routes. These names are project conventions, not built-in framework functions.

| Path in Product.Api | Responsibility |
| --- | --- |
| Program.cs | Environment setup and visible composition sequence |
| Composition/ServiceCollectionExtensions.cs | AddApiServices and validated service/options registration |
| Composition/ApplicationBuilderExtensions.cs | UseApiPipeline with explicit tested order |
| Composition/EndpointRouteBuilderExtensions.cs | MapApiEndpoints and health/documentation routes |
| Middleware | Small custom HTTP concerns only |
| Errors/GlobalExceptionHandler.cs | Central safe unexpected-error mapping |
| Filters | Endpoint-bound transport validation/CSRF where needed |
| Authorization | API policies and resource-authorization adapters |
| OpenApi | Document registration and shared metadata transformers |
| Endpoints/<Module> | Route groups, HTTP mapping and operation metadata |

Use framework middleware before custom replacements. Prefer IExceptionHandler/ProblemDetails services for centralized exception handling in the selected .NET profile. Custom middleware must have a bounded responsibility and no domain transactions.

## Reference order and dependencies

The following is the recommended API/BFF profile; conditional stages appear only when configured. Incoming requests follow this order and response work unwinds through enclosing middleware. Edge-level abuse controls protect work performed before application authentication.

| Stage | Placement reason and limits |
| --- | --- |
| Trusted forwarded headers | Correct scheme/host/client interpretation before redirects; explicitly configured known proxies/networks |
| Safe request scope/completion logging | Establish correlation and wrap the exception handler so final error status is observable; exclude secrets |
| Exception handler | Catch downstream unexpected failures and return safe problem responses |
| HSTS/HTTPS policy where appropriate | Follow trusted proxy interpretation; coordinate with TLS termination to avoid loops |
| Status-code response formatting | Fill supported empty error responses without replacing existing bodies, challenges or redirects |
| Routing | Select endpoint metadata for later policies |
| CORS, only when required | After routing and before auth; allow valid preflight without requiring user authentication |
| Authentication | Establish a verified principal |
| Authorization | Enforce endpoint permission before protected execution |
| Application rate limiter | After routing; after authentication for identity-based partition keys; protect authorized operations |
| Antiforgery for cookie profile | After authentication/authorization; enforce on relevant endpoints |
| Endpoints | Bind DTO, invoke use case and map result |

A gateway/global pre-auth limiter is a separate defense against anonymous/authentication abuse; a post-auth limiter cannot protect earlier expensive stages. Use verified identity keys with bounded partition cardinality. Do not select a tenant limiter key from an unvalidated caller header.

Requests rejected before routing/CORS might not expose their bodies cross-origin. Specify behavior and test it; do not move identity controls merely to make a Swagger demo work. Static files and Swagger UI middleware may short-circuit; do not assume endpoint fallback authorization protects them. Serve protected downloads through authorized endpoints.

## Host sketch

The extension names below are application-owned pseudocode with required responsibilities described above; this is not a drop-in runnable sample.

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddApplication();
builder.Services.AddInfrastructure(builder.Configuration);
builder.Services.AddApiServices(builder.Configuration);
var app = builder.Build();
app.UseApiPipeline();       // Explicit ordering owned and tested by Composition/.
app.MapApiEndpoints();      // Per-module route groups and authorization metadata.
app.MapOperationalEndpoints();
app.MapDevelopmentDocumentation();
app.Run();
```

Inside UseApiPipeline, preserve the documented dependencies. AddAuthentication registers the actual selected scheme, AddAuthorization the policies, AddCors only the named conditional policy, and AddRateLimiter the actual limits/rejection response. Calling Use... without its services/configuration is not sufficient. Validate critical configuration at startup.

## Middleware, filters, and application behaviors

| Concern | Correct home |
| --- | --- |
| Forwarded headers, request scope, HTTP exception boundary | Middleware/host |
| DTO binding, endpoint-specific transport validation | Endpoint filter/controller conventions |
| Resource permission and domain invariant | Application/domain use case, with transport policy defense |
| Unit of work, command replay, business audit | Application coordinator and Infrastructure ports |
| OpenAPI response/security metadata | Endpoint metadata and OpenAPI transformers |

Use conventional middleware's InvokeAsync parameters for scoped services, or an appropriately registered IMiddleware implementation; never capture a scoped DbContext in singleton-like middleware construction. Await next exactly once unless intentionally short-circuiting. Do not write after response start or replace streaming output with a JSON error. Request bodies must not be buffered/logged indiscriminately; cancellation and streaming require bounded handling.

One boundary owns error mapping. Expected application results become documented 4xx responses at endpoints; unexpected exceptions receive safe 500 problems. Preserve WWW-Authenticate for 401, deliberate 403 behavior, and 429 retry metadata when available. Do not convert cancellation/client disconnect to a fake success or an automatic retry. Test framework automatic validation/auth/limiter responses too; AddProblemDetails alone does not guarantee every response follows our contract.

UseAntiforgery is not a blanket guarantee that all JSON endpoints are validated. Configure endpoint/filter enforcement for cookie-authenticated state changes and verify rejection with real requests. For bearer-only APIs, document CSRF non-applicability instead of enabling unexplained middleware.

## Pipeline tests

Boot the real host and prove: untrusted forwarded headers cannot alter redirect identity; valid preflight reaches CORS without auth challenge; unauthorized requests never reach use cases; authenticated quota exhaustion returns the documented 429; missing/invalid CSRF fails cookie mutations; downstream faults yield safe problems and a final-status log; existing error bodies/challenges survive; streaming/cancelled responses are not rewritten; production documentation routes are absent or explicitly protected. Tests should demonstrate behavior rather than only checking the order of strings in Program.cs.

Sources: [ASP.NET middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0), [rate limiting](https://learn.microsoft.com/en-us/aspnet/core/performance/rate-limit?view=aspnetcore-10.0). This composition profile is our design, not a claim of one universal ordering for every application type.


## Rules and evidence

| Rule | Requirement | Verification |
| --- | --- | --- |
| MW-001 | Backend hosts MUST centralize visible service/pipeline/endpoint composition and preserve documented ordering dependencies. | Real-host preflight, authentication and endpoint execution tests |
| MW-002 | Custom middleware MUST respect DI lifetimes, cancellation, response-start and streaming behavior. | Scoped-lifetime, disconnect and streaming failure tests |
| MW-003 | Exception, validation, authentication and throttling paths MUST retain safe consistent HTTP error behavior. | 500/400/401/403/429 body, challenge and logging assertions |
| MW-004 | Cookie mutation and identity-based throttling controls MUST be enforced by tested endpoint/pipeline behavior. | Invalid antiforgery and verified-identity quota tests |

## Exceptions

Record a scoped, approved, time-bounded [exception](https://github.com/Slight76/standards-marketplace/blob/main/templates/exception.md) rather than silently changing the profile.
