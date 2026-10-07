---
title: "OpenAPI generation and Swagger UI structure"
status: proposed
version: 1.0.0
owner: "@Slight76"
supersedes: architecture-standards/backend/openapi-swagger-standard.md@c1bda3d
---
# OpenAPI generation and Swagger UI structure

Baseline: 1.0.0. Applies to the ASP.NET Core backend profile. Decision: [ADR-0027](../adr/0027-openapi-swagger.md). Effective when adopted by the solution.


## Default toolchain

OpenAPI is the machine-readable API contract. Swagger UI renders and can exercise that contract; it does not implement authorization or prove correctness. For the ASP.NET Core profile, use Microsoft.AspNetCore.OpenApi as the single document generator and Swashbuckle.AspNetCore.SwaggerUi for the interactive UI. Choose pinned compatible package versions when the template is built. Verify the UI and TypeScript generator support the selected OpenAPI dialect; the recommended contract profile is OpenAPI 3.1.

Do not add Swashbuckle's SwaggerGen beside first-party generation for the same contract or manually maintain a second YAML document that can drift. An existing backend may use Swashbuckle generation through a scoped ADR with equivalent validation; that is a replacement generator, not a second source of truth. Scalar can be an explicitly selected UI alternative, but Swagger UI is this profile's default.

## Project structure and ownership

| Path in Product.Api | Owns |
| --- | --- |
| OpenApi/OpenApiRegistration.cs | Named documents, serializer dialect and transformer registration |
| OpenApi/Transformers/DocumentMetadataTransformer.cs | Title/version/contact and safe server metadata |
| OpenApi/Transformers/SecurityRequirementsTransformer.cs | Security schemes and per-operation requirements from actual endpoint metadata |
| OpenApi/Transformers/ProblemResponsesTransformer.cs | Reusable response conventions where actually supported |
| OpenApi/Transformers/SchemaConventionsTransformer.cs | Stable schema IDs, nullability/format overrides only where needed |
| OpenApi/SwaggerUiConfiguration.cs | UI document URLs, local auth behavior and environment restrictions |
| Endpoints/<Module> | Stable operationId, tags, summaries, real status/payload/header declarations |
| tests/ApiContractTests | Document schema validation, duplicate-ID detection, example and endpoint parity tests |

These are suggested application files, not files implemented in this standards-only repo. Group documents by contract major version and audience; use tags for business modules. A folder per CRUD endpoint is not a reason to publish a separate document. Internal/admin endpoints must not leak into a public document.

## Version and audience mapping

| Concern | Example |
| --- | --- |
| HTTP route family | /api/v1/stock-items |
| Named OpenAPI document | public-v1 |
| Document endpoint | /openapi/public-v1.json |
| Swagger UI route | /swagger |
| Business module tag | Inventory |
| Stable operationId | Inventory_GetStockItem_v1 |

Register explicit inclusion predicates/group metadata for each document. Document naming alone does not select endpoints or enforce API versions. The profile uses explicit route groups; if a versioning package is selected, configure its API-explorer integration and tests rather than assuming that a v1 label performs routing. Verify each operation appears in exactly the intended audiences/versions. Group names and tags have different responsibilities.

## Operation and schema rules

Every operation states purpose, permissions/scopes, parameter/body constraints, actual success and error responses, content types, concurrency/replay headers, and pagination when relevant. Use typed results or explicit response metadata so generated schemas match actual behavior. Describe 201 Location, ETag/If-Match where applicable, Idempotency-Key, 401 challenge, and 429 behavior rather than documenting only 200.

Keep request and response DTOs separate where writable/exposed fields differ. Use deterministic collision-free schema identities, explicit enum/nullability/format conventions, and synthetic schema-valid examples. Avoid exposing internal command classes merely because endpoints invoke them. Summaries explain business behavior; XML comments can supplement endpoint metadata but cannot repair an incorrect schema.

Apply security requirements per operation using endpoint authorization and anonymous metadata. Do not attach bearer requirements to every operation blindly. Describing a security scheme only adds metadata; it does not protect the endpoint. Document BFF cookie/CSRF behavior accurately rather than displaying a misleading bearer Authorize button. OAuth interactive flows use a public client with PKCE and approved redirect URIs where applicable; no client secrets, persistent tokens, or shared production credentials in UI configuration.

## Development UI fragment

This illustrates first-party document generation with a separate Swagger UI package. It omits required audience inclusion predicates, auth, DTOs, transformers, and dialect configuration; it has not been compiled here.

```csharp
builder.Services.AddOpenApi("public-v1");
// ... register the application and construct app ...
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
    app.UseSwaggerUI(options =>
    {
        options.RoutePrefix = "swagger";
        options.SwaggerEndpoint("../openapi/public-v1.json", "Public API v1");
    });
}
```

The relative document URL is intended for the default `/swagger/index.html` location; test it behind the actual PathBase/reverse proxy. API server URLs and OAuth redirects must also work under the deployment prefix. Do not copy localhost production server URLs into published artifacts. Hosted documentation should use approved environment/audience configuration.

## Environment and exposure policy

Enable runtime JSON and Swagger UI by default only in Development. CI can still generate/publish approved contract artifacts for consumers without serving runtime docs publicly. Production documentation is an explicit opt-in decision: protect both UI assets and JSON endpoints through a verified gateway/authenticated route strategy and audience control. A fallback endpoint authorization policy does not automatically protect Swagger UI middleware assets. Restrict or disable interactive mutations as required; disabling Try it out is not API access control.

Do not ship tokens in example requests, enable persistent authorization by default, or put real customer data into examples. The UI running in a browser still follows CORS and CSRF rules; never weaken either to make a documentation request succeed.

## Build and publication

Use the selected first-party build-time generation tooling, including Microsoft.Extensions.ApiDescription.Server where required by the pinned runtime. Configure an explicit artifact directory and document names. Generation can execute application startup; isolate it from production secrets, migrations, external calls, and hosted-worker side effects. Use deterministic synthetic configuration and test that generation works without live production infrastructure.

CI sequence: generate all intended documents; validate syntax/spec and local references; lint required metadata and unique operationIds; validate synthetic examples; compare compatibility against the supported artifact; generate/build the TypeScript client; publish immutable artifacts/checksums. Do not normalize away meaningful differences to force a clean diff. Regeneration must preserve documented status/auth semantics.

## Acceptance cases

Verify each intended endpoint is present once in the right audience/version; private endpoints are absent from public docs; operation IDs are unique/stable; validation/authorization/conflict responses match the running API; security declarations match anonymous/protected endpoints; document/UI URLs work under a proxy prefix; production docs follow the exposure decision; generation does not execute migrations or require live services; a changed contract rebuilds a pinned client successfully. A rendered Swagger page alone passes none of these contract gates.

Sources: [OpenAPI overview](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/openapi/overview?view=aspnetcore-10.0), [document customization](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/openapi/customize-openapi?view=aspnetcore-10.0), [Swagger UI integration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/openapi/using-openapi-documents?view=aspnetcore-10.0). Related: [contract lifecycle](contracts-standard.md), [middleware](middleware-standard.md).


## Rules and evidence

| Rule | Requirement | Verification |
| --- | --- | --- |
| OAS-001 | Backends MUST use one declared OpenAPI generator with stable document/audience/version ownership. | Document inclusion, duplicate operationId and reproducibility tests |
| OAS-002 | OpenAPI responses, schemas and security metadata MUST match implemented endpoint behavior. | Runtime-contract parity, example validation and anonymous/protected operation tests |
| OAS-003 | Swagger UI and document exposure MUST follow explicit environment policy without weakening API security. | Production UI/JSON exposure, proxy-path and auth/CSRF tests |
| OAS-004 | Build-time contract generation MUST be isolated from production effects and pass consumer generation checks. | Offline-safe generation, lint/diff and generated client build |

## Exceptions

Record a scoped, approved, time-bounded [exception](https://github.com/Slight76/standards-marketplace/blob/main/templates/exception.md) rather than silently changing the profile.
