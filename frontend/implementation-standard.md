# Frontend structure, state, and data access

Baseline: 0.3.0 recommended draft. Applies when: an application uses the React/TypeScript client profile

Decision: [ADR-0017](../adr/0017-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Project boundaries

Use a separately built client repository. Default to a client-rendered Vite application for authenticated business tools; SSR/SSG requires a documented public-content, performance, or SEO requirement. Runtime and library versions belong in lockfiles and the solution technology profile.

| Path | Owns | May import |
| --- | --- | --- |
| src/app | Bootstrap, routes, providers, configuration | Feature public APIs, shared, api, auth |
| src/features/<name> | Feature UI, hooks, forms, adapters, use cases | Own internals, shared, api, auth |
| src/shared/ui | Generic visual primitives | Other generic shared modules |
| src/shared/lib | Pure generic utilities | Generic libraries; no features/app |
| src/api/generated | Generated transport types/client | Generator runtime only |
| src/api/client | Transport configuration and error mapping | Generated code, generic config |
| src/auth | Identity integration/session access | Provider SDK, generic api transport/config |

Prefer app-level composition across features. A feature-to-feature public import is allowed only when declared in the dependency map and acyclic. Export a deliberately small public API from each feature. Enforce imports with lint/dependency rules, not a folder-naming convention alone. Tests may inspect their own feature internals; production modules cannot import test helpers.

Use PascalCase for React component/type names and camelCase for variables/functions. Name hooks `use...`. Avoid catch-all `helpers.ts` and `types.ts` dumping grounds; name modules for responsibility. Colocate feature tests; reserve root end-to-end tests for cross-feature journeys.

## State ownership

| State | Default |
| --- | --- |
| Input focus, disclosure, temporary selection | Local React state |
| Derived display values | Compute from source state; do not synchronize duplicates |
| Search/filter/page that must survive navigation | URL state with validation |
| API query results | TanStack Query through feature adapters |
| Form drafts | Form-local state; React Hook Form for complex forms |
| Cross-route client-only preferences | Small context/reducer; larger store requires need |
| Identity/session | Approved auth provider, separate from cached business data |

These library choices are the recommended profile, not claims that React requires them. Query keys include tenant and every server query input. Clear sensitive caches on logout/tenant switch. Mutations invalidate or update affected keys deliberately. Avoid copying query results into a second global store. Define freshness per data type; do not choose one stale-time for all data.

## Transport and runtime validation

Components call feature hooks/adapters; adapters call the generated API client through configured transport. Central transport applies base URL, auth integration, timeout/cancellation, and safe problem mapping. Do not add raw fetch/axios calls in random components. Pass AbortSignal through supported clients and protect against outdated responses. Unknown network response shapes require validation at trust boundaries; TypeScript alone does not validate them. Use Zod as the profile default for runtime form/config validation, avoiding duplicate schema ownership when generation can supply it.

TypeScript uses strict mode and noUncheckedIndexedAccess. Narrow unknown values; avoid broad `any`, unchecked casts, and non-null assertions as error suppression. The same tsconfig must apply in CI and local builds. Validate public environment config at startup. Never store secrets in build-time browser variables.

## Mutations and UI behavior

Every data screen handles loading, empty, error, forbidden, and success states. Use optimistic updates only when reversal is safe and concurrency conflicts are handled. Default to confirmed server state for stock, financial, and permission changes. Prevent duplicate UI submission for usability, but rely on backend idempotency for correctness. Preserve user input on recoverable failure and provide an accessible retry path.

## Verification

Test rendered behavior, network states, tenant cache separation, stale responses, and failed mutations. Use Vitest plus Testing Library for component behavior and Playwright for critical journeys in this profile. Mock transport at the boundary; do not duplicate the hook implementation in tests. API contract and real-server integration tests complement mocks. Run build, typecheck, import lint, tests, and production bundle inspection before release.

Sources: [React state design](https://react.dev/learn/choosing-the-state-structure), [TypeScript strict](https://www.typescriptlang.org/tsconfig/strict.html). Package selections are proposed enterprise defaults, resolved and pinned when templates are built.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| FE-006 | Frontend code MUST enforce the documented import matrix and acyclic feature dependencies. | Import lint and intentional forbidden-import fixture |
| FE-007 | Server, form, URL, identity, and local UI state MUST have explicit owners. | State review plus logout/tenant-switch tests |
| FE-008 | TypeScript MUST use strict checking and validate untrusted runtime inputs. | Typecheck and malformed payload/config tests |
| FE-009 | Feature API adapters MUST provide cancellation, error mapping, and deliberate cache updates. | Abort, stale response, and mutation-failure tests |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
