# ADR-0027: OpenAPI generation and Swagger UI structure

Status: Proposed

Date: 2026-10-05

## Context

Agents need consistent document generation, endpoint grouping, UI configuration and security behavior.

## Decision

Use first-party ASP.NET Core OpenAPI generation with Swagger UI, shared transformers, per-endpoint metadata and explicit audience/version groups.

## Alternatives

Full Swashbuckle generation is an acceptable documented replacement for existing apps; duplicate generators drift. Scalar is an optional UI alternative. Hand-maintained specifications require a different declared source-of-truth workflow.

## Consequences

Package/dialect compatibility and document/runtime parity need tests. Runtime documentation exposure is independent of CI contract publication.

## Traceability

[OpenAPI generation and Swagger UI structure](../backend/openapi-swagger-standard.md). Rules: OAS-001, OAS-002, OAS-003, OAS-004. Related: [backend decisions](0018-implementation-decisions.md), [HTTP/contracts](0013-implementation-decisions.md), [identity](0015-implementation-decisions.md).

## Verification

Implement the linked standard’s positive, negative, and failure-path tests in the consuming backend. Documentation checks do not prove runtime behavior.

## Approval

Authored under the owner’s request for CQRS, middleware, and Swagger structure. The detailed defaults remain Proposed until solution adoption; this does not invent approval of deployment or business inputs.
