---
title: "Contract ownership, generation, and compatibility"
status: proposed
version: 1.0.0
owner: "@Slight76"
supersedes: architecture-standards/integration/contracts-standard.md@c1bda3d
---
# Contract ownership, generation, and compatibility

Baseline: 1.0.0. Applies when: separate repositories exchange HTTP contracts

Decision: [ADR-0013](../adr/0013-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.

## Publication flow

The backend owns its OpenAPI source or generated artifact, with one declared source of truth. The default .NET profile generates OpenAPI from the implementation in CI, normalizes deterministic output, and publishes a versioned artifact with checksum and source commit. Frontend builds pin an artifact version/checksum, not a running developer server. Commit generated client code by default for review; record generator name/version/configuration so regeneration is reproducible.

Contract versions are independent of web/API application package versions. The `/v1` path denotes a major compatibility family; it does not change on every deployment. Never edit generated TypeScript to fix a server mismatch. Change the owned contract, regenerate, and update its consumer adapter.

## Required operation metadata

Every operation has a stable operationId, description of authorization, request constraints, success/error schemas, content types, pagination, and concurrency/retry semantics. Explain omissions and nulls. Use explicit request DTOs to prevent overposting. Examples use synthetic data and valid schema instances. Do not expose internal health or administration APIs accidentally in the public client artifact.

## Compatibility rules

Removal/rename, new required input, narrowed ranges, changed meaning/status, and stricter permission requirements can break clients. Adding an enum response value can break exhaustive clients; assess it explicitly. Adding a nullable response field is usually compatible only when clients tolerate unknown fields. A diff tool catches structural changes, not every behavioral change.

For a breaking change: introduce a new major contract or compatible expansion; publish client support; measure old consumer use; agree a retirement date; remove old behavior only after the support window. Consumer-owned compatibility tests run against the provider build. Keep the last supported web artifact usable after API rollback; record a compatibility matrix.

## Example delivery sequence

1. API adds optional `displayName`, continuing to supply the old field.
2. CI checks the old contract/consumer fixture against the new API.
3. A new contract artifact is published and the web repo pins it.
4. Web switches display behavior with fallback.
5. Removal is separately versioned after old consumers retire.

## Verification and failure modes

Regenerate twice and compare; CI must fail on uncommitted generated drift. Parse the OpenAPI document with a real validator and run request/response contract tests. Build the frontend with the pinned artifact. Do not fetch `latest` during a build, publish an untested client, assume all clients deploy simultaneously, or treat TypeScript types as runtime validation of untrusted JSON.

Source: [OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html). Artifact lifecycle and compatibility gates are our policy.

## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| CON-001 | API consumers MUST pin reproducibly generated client contracts to immutable artifacts. | Clean regeneration diff and checksum verification |
| CON-002 | Provider changes MUST assess structural and behavioral compatibility with supported consumers. | Contract diff plus consumer compatibility evidence |
| CON-003 | Every operation MUST document auth, validation, errors, concurrency, and retry behavior. | OpenAPI validation and operation review |

## Exceptions

Use the [exception record](https://github.com/Slight76/standards-marketplace/blob/main/templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.

## Related backend structure

For backend document registration, transformers, audience/version grouping and Swagger UI exposure, follow the [OpenAPI/Swagger standard](openapi-swagger-standard.md).
