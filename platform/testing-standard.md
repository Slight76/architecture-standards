# Verification boundaries and test evidence

Baseline: 0.2.0 recommended draft. Applies when: an application implements adopted architecture rules

Decision: [ADR-0020](../adr/0020-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Test at the boundary that can prove the claim

| Claim | Required kind of evidence |
| --- | --- |
| Domain invariant | Fast domain unit test over valid/invalid transitions |
| Use-case orchestration | Unit tests of outcomes and port failures; real transaction tests separately |
| Relational integrity | Integration tests with the selected database engine |
| HTTP behavior/auth | Real API host tests with controlled identity/claims |
| CORS | Header/preflight tests plus a browser reading/denied response |
| Frontend usability | Component behavior and keyboard/accessibility checks |
| Contract compatibility | Provider/consumer tests for supported versions |
| Recovery | Actual restore/rebuild exercise in an isolated environment |
| Architecture dependency | Assembly/import/namespace rules and forbidden-dependency fixtures |

The reference profile uses xUnit for .NET, Vitest/Testing Library for React, and Playwright for browser journeys. Select pinned supported versions when building templates. Containers for database tests are useful but the engine and configuration matter more than the container library choice.

## Determinism and isolation

Use synthetic fixtures, controlled clocks where needed, unique data namespaces, and deterministic cleanup. Parallel tests must not share mutable global rows. Avoid real email, payment, or customer endpoints; sandbox integrations require explicit configuration and bounded cost. Never leak secrets through failure snapshots or HTTP recordings.

Test observable behavior rather than internal call counts unless the boundary contract is the subject. Snapshot tests cannot replace authorization or concurrency assertions. Keep unit suites fast; use a targeted integration/E2E suite for critical behavior. Coverage percentages are diagnostic, not proof of correctness or a reason to test trivial getters.

## High-value negative cases

A second tenant requests the first tenant's resource; two writers race; the response is lost after commit; an event is delivered twice; the database is unavailable; a client uses the previous contract; a migration stops midway; a form submission fails; a malicious origin attempts to read a protected response. Choose cases applicable to the change and record exclusions.

## Commands and evidence

Every application README must document reproducible install/build/test commands and required local services. A command that needs unavailable infrastructure is `not_run`, not passed. CI attaches reports to the tested commit/artifact. Changes to tests and acceptance thresholds receive the same review as implementation. Failing rules cannot be bypassed by relabeling them not applicable without a reason.

This standards repository checks documentation/catalog integrity and evidence shape only. It ships no application runtime, so it cannot prove that a consuming application's CORS, authentication, SQL, or UI complies. Consumers must implement the listed checks.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| TEST-001 | Verification MUST exercise the boundary capable of proving each compliance claim. | Rule-to-test matrix with real-engine/browser evidence where required |
| TEST-002 | Tests MUST use isolated synthetic data and reproducible setup without real production side effects. | Fixture/configuration and parallel-isolation review |
| TEST-003 | Applications MUST document executable verification commands and retain commit-linked reports. | Clean setup execution and report provenance |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
