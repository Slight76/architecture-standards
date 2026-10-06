# CORS and browser origin policy

Baseline: 0.3.0 recommended draft. Applies when: a browser interacts with an API

Decision: [ADR-0014](../adr/0014-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Decision table

| Deployment | Required behavior |
| --- | --- |
| Web and API share scheme, host, and port via routing | CORS is unnecessary; keep authentication and CSRF controls |
| Browser directly calls a different API origin | Named, environment-specific allowlist policy |
| Server-to-server call or worker | CORS does not enforce access; authenticate and restrict network paths |
| Local UI dev server calls local API | Explicit local origins in development configuration only |

Separate repositories do not require separate public origins. An edge can serve independently released web assets at `/` and route `/api` to the API. Different subdomains are cross-origin even if they share a parent domain.

## Policy

Allow only approved exact origins, methods, and request headers needed by that client. Reject unknown configuration at startup: no wildcard origins, no `null`, no path/query/fragment or trailing slash in origin values. Require HTTPS outside local development. An allowlisted origin is not evidence of an authenticated caller.

Enable credentials only for an explicitly designed cross-origin cookie/session flow. Never combine wildcard origins with credentials. Authorization bearer headers do not justify `AllowCredentials` by themselves. Expose only response headers JavaScript actually reads, such as ETag and Location. If browser tracing is enabled, allow its required request headers explicitly. Keep API and edge configuration consistent; choose one CORS policy authority.

CORS governs browser access to responses; it is neither API authentication nor CSRF protection. Some cross-origin requests can still execute even when their responses are unreadable. A server or script outside the browser can ignore CORS entirely.

## ASP.NET Core configuration fragment

This fragment assumes the host already validates `Browser:Origins`, registers the selected authentication scheme, and maps its endpoints. It is illustrative, not a standalone runnable application.

```csharp
var origins = builder.Configuration.GetSection("Browser:Origins").Get<string[]>()
    ?? throw new InvalidOperationException("Browser origins are required.");
builder.Services.AddCors(options => options.AddPolicy("BrowserClient", policy =>
    policy.WithOrigins(origins)
          .WithMethods("GET", "POST", "PUT", "PATCH", "DELETE")
          .WithHeaders("Content-Type", "Authorization", "If-Match", "Idempotency-Key")
          .WithExposedHeaders("ETag", "Location")));
// After builder.Build(); auth configuration is supplied by the identity profile.
app.UseRouting();
app.UseCors("BrowserClient");
app.UseAuthentication();
app.UseAuthorization();
```

Scope methods/headers to the real API; add antiforgery or tracing headers only if used. Do not attach additional overlapping endpoint CORS policies. Preflight is handled by CORS middleware before authorization. Configure clients with the HTTPS API address directly rather than depending on a preflight redirect.

## Verification matrix

| Case | Required evidence |
| --- | --- |
| Approved origin and supported request | Browser reads response; exact allow-origin value |
| Unapproved origin | No granting allow-origin header; browser cannot read response |
| Unapproved method/header preflight | Requested capability is not granted |
| Protected actual request without credentials | Authentication still fails independently of CORS |
| Credentialed cookie profile | Correct allow-credentials, exact origin, and separate CSRF tests |
| Same-origin deployment | Requests work without CORS allowances |
| Production config contains localhost or wildcard | Deployment/configuration validation fails |

Do not require every rejected CORS request to return 403: implementations may simply omit access-control headers. Use HTTP header assertions plus a real browser test. curl alone cannot prove browser enforcement.

Source: [Microsoft CORS guidance](https://learn.microsoft.com/en-us/aspnet/core/security/cors?view=aspnetcore-10.0). The stricter environment/configuration controls are our policy.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| CORS-001 | Solutions MUST decide whether browser access is same-origin or cross-origin before enabling CORS. | Deployment origin matrix and browser integration test |
| CORS-002 | Cross-origin policies MUST use validated exact per-environment origins and explicit required capabilities. | Positive/negative preflight and production configuration tests |
| CORS-003 | CORS MUST NOT substitute for authentication, authorization, or CSRF protection. | Unauthorized actual request and CSRF negative tests |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.

## Related backend structure

CQRS is a separate application design concern; see [CQRS](../backend/cqrs-standard.md). This browser origin policy remains conditional on deployment and is not a command/query pattern.
