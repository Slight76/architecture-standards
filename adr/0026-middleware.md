# ADR-0026: HTTP middleware and host composition

Status: Proposed

Date: 2026-10-05

## Context

Host setup needs stable ordering and responsibility boundaries; cross-cutting concerns otherwise drift into business code.

## Decision

Use one explicit composition root with framework-first HTTP middleware, endpoint transport concerns, and separate application behaviors.

## Alternatives

Scattered module pipeline registration hides order; a universal custom middleware class becomes a business/service locator; applying every optional stage to all apps creates unsafe assumptions.

## Consequences

Integration tests must cover short-circuits and failures as well as the happy path. Proxy, auth and browser profiles remain explicit inputs.

## Traceability

[HTTP middleware and host composition](../backend/middleware-standard.md). Rules: MW-001, MW-002, MW-003, MW-004. Related: [backend decisions](0018-implementation-decisions.md), [HTTP/contracts](0013-implementation-decisions.md), [identity](0015-implementation-decisions.md).

## Verification

Implement the linked standard’s positive, negative, and failure-path tests in the consuming backend. Documentation checks do not prove runtime behavior.

## Approval

Authored under the owner’s request for CQRS, middleware, and Swagger structure. The detailed defaults remain Proposed until solution adoption; this does not invent approval of deployment or business inputs.
