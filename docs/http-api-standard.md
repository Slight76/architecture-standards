---
title: "HTTP API design"
status: proposed
version: 1.0.0
owner: "@Slight76"
supersedes: architecture-standards/integration/http-api-standard.md@c1bda3d
---
# HTTP API design

Baseline: 1.0.0. Applies when: an application exposes an HTTP API

Decision: [ADR-0013](../adr/0013-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Default and rationale

Use resource-oriented JSON HTTP APIs for browser-facing business operations. REST is the architectural style; RESTful describes adherence, not another protocol. This profile chooses concrete HTTP conventions without claiming full REST constraint compliance or requiring hypermedia-driven clients. GraphQL needs a query/composition use case and cost controls; gRPC needs a supported service-to-service use case; events suit asynchronous propagation. Record such departures in a solution ADR.

Use `/api/v1/` for the initial major contract. Use lower-case plural kebab-case resource segments and opaque identifiers: `/api/v1/stock-items/{id}`. Nest one ownership relationship when useful; use filters instead of long chains. Describe business actions as resources where natural, such as `POST /api/v1/stock-items/{id}/adjustments`. Do not force every action into CRUD or expose database table structure as the public contract.

## Method and response contract

| Operation | This profile's convention |
| --- | --- |
| GET collection | 200 with `items` and `nextCursor`; an empty collection is 200 |
| GET item | 200 or 404; no business mutation |
| POST create | 201 with representation and Location identifying the new resource |
| POST long operation | 202 with operation-status URL; document terminal failure/cancellation |
| PUT | Replace the complete writable representation; no implicit create unless documented |
| PATCH | Explicit patch media type/schema and field allowlist; define absent versus null |
| DELETE | 204 after deletion; repeat deletion may return 404 without violating idempotency |
| HEAD | GET metadata without response content |

Use 400 for malformed input and field validation in this profile, 401 for absent/invalid authentication, 403 for denied authorization, 404 for missing resources, 409 for business-state conflicts, 412 for a stale If-Match precondition, 415 for unsupported content type, and 429 for throttling. 401 includes the appropriate challenge. Selective 404 concealment requires a consistent security policy. Never encode an error as a successful 200 response. Gateway failures can precede application error formatting; clients must handle non-JSON failures.

## Representation conventions

JSON properties use camelCase; enumerations use stable documented strings. IDs serialize as strings, including integers beyond JavaScript's safe range. Instants use ISO 8601/RFC 3339 UTC strings; dates without time use `YYYY-MM-DD`. Money uses a decimal string plus currency or integer minor units with currency-specific precision; do not use binary floating point. Define nullability, max lengths, numeric ranges, and writable fields in the contract. Never expose ORM entities or password/token material.

Collection default: `limit=25`, maximum 100. These are profile defaults, not workload guarantees. Use opaque cursor pagination with stable ordering and a unique tie-breaker; allowlisted filters and sort fields only. Bind the cursor to its filters and tenant context and validate it; encoding is not authorization. Totals are optional because they can be expensive. Document consistency during concurrent changes and require snapshots when a stable export is needed.

Example response:

```json
{"items":[{"id":"item-17","sku":"WIDGET-A","quantity":12}],"nextCursor":null}
```

## Errors and concurrency

Use `application/problem+json` with `type`, `title`, HTTP-matching `status`, safe `detail`, and optional `instance`; add stable application `code` and a non-sensitive `traceId`. Validation uses an `errors` map of field paths to messages. Clients branch on codes, not localized prose. Treat problem type identifiers as stable contracts. Do not put request bodies or identifiers with sensitive data into instance URLs.

```json
{"type":"https://example.invalid/problems/stock-conflict","title":"Stock changed","status":409,"code":"stock.conflict","detail":"Refresh the item and try again.","traceId":"opaque-trace-reference"}
```

The example type URL must be replaced with a maintained documentation URI. For editable resources, return a strong ETag and require If-Match on updates susceptible to lost writes. Return 428 when this profile requires a missing precondition, 412 when it fails. Database concurrency enforcement remains atomic; an HTTP header alone does not prevent races. For replayable POST operations use the [idempotency protocol](messaging-resilience.md).

## Verification and prohibited patterns

Contract tests cover each response, empty lists, invalid payloads, unsupported media types, unknown enum values, unauthorized IDs, and stale concurrent edits. Verify URLs/headers and behavior, not merely DTO compilation. Prohibit side-effecting GETs, unlimited lists, arbitrary SQL sort expressions, and automatic mutation retries without a replay contract.

Sources: [HTTP semantics](https://httpwg.org/specs/rfc9110.html), [problem details](https://www.rfc-editor.org/rfc/rfc9457). Route naming, pagination limits, version paths, and money representation are our policy choices.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| API-001 | APIs MUST follow the resource, method, representation, and status conventions in this document. | HTTP contract tests for successful and failing operations |
| API-002 | Collection endpoints MUST bound results and allowlist query operations. | Limit, cursor tampering, tenant scope, and sort-injection tests |
| API-003 | Application errors MUST use the documented problem contract and stable codes. | Validate media type, status agreement, codes, and redaction |
| API-004 | Updates vulnerable to lost writes MUST enforce an atomic concurrency policy. | Two competing updates: one succeeds and the stale write fails |

## Exceptions

Use the [exception record](https://github.com/Slight76/standards-marketplace/blob/main/templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
