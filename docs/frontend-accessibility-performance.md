---
title: "Accessible and resilient user interfaces"
status: proposed
version: 1.0.0
owner: "@Slight76"
supersedes: architecture-standards/frontend/accessibility-performance.md@c1bda3d
---
# Accessible and resilient user interfaces

Baseline: 1.0.0. Applies when: a solution presents a browser UI

Decision: [ADR-0017](../adr/0017-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.

## Accessibility baseline

Target WCAG 2.2 AA for the UI profile. This is a design/test target, not a certification claim. Prefer semantic HTML and native controls. Inputs need labels and accessible error associations; dialogs need focus entry, containment where appropriate, Escape handling, and focus return. All controls need visible focus and keyboard operation. Never rely on color alone for meaning.

Use the application design system before custom widgets. Record any chosen component library and verify the actual composed UI; a library's accessibility claim does not prove the application is accessible. Support zoom/reflow, reduced motion, and readable error/status announcements. Data tables require meaningful headers; virtualized content requires deliberate screen-reader and keyboard testing.

## Performance and resilience

Record a bundle and interaction budget for representative devices/networks in the solution. Route-level code splitting is the default for substantial features. Measure before memoizing or adding a global store. Optimize image dimensions/loading, avoid rendering massive collections, and paginate server queries. A failed optional widget must not blank the entire application; use appropriately scoped error boundaries and recovery UX.

Front-end telemetry records route templates and performance/error categories, not raw inputs, access tokens, or full URLs with personal query strings. Source maps are restricted to the approved error-reporting pipeline when they expose internals. Use content-hashed static assets with immutable caching and short-lived/revalidated HTML/runtime configuration to avoid stale entrypoints.

## Acceptance scenario

A user opens the inventory list using only a keyboard, changes the filter, opens an item, submits an invalid adjustment, hears/reads the field error, corrects it, and sees the server-confirmed result. Repeat at zoom, slow network, and after session expiry. Verify that form data is not silently lost and denied actions do not appear as successful.

Automated accessibility scanning runs in component/E2E checks, followed by keyboard and representative screen-reader review. Automated scans alone cannot establish conformance. Budget regressions require measured investigation, not arbitrary test-threshold increases.

Source: [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| UX-001 | User journeys MUST support keyboard, focus, labels, error announcements, and the adopted accessibility target. | Automated accessibility plus manual keyboard/screen-reader evidence |
| UX-002 | Applications MUST define measured performance budgets and asset/configuration caching behavior. | Production-build budget report and stale-asset deployment test |

## Exceptions

Use the [exception record](https://github.com/Slight76/standards-marketplace/blob/main/templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
