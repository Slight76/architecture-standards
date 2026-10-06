# Platform architecture

Baseline: 0.1.0 draft. Scope/decision: [ADR-0007](../adr/0007-platform.md).

## Purpose

Developer and delivery capabilities, environments, artifact lifecycle, telemetry, and release controls.

## Design

Separate development, test, and production identities and configuration. Build once and promote the same artifact; record provenance and dependency versions. Specify rollout strategy, deployment gates, smoke tests, and rollback commands per application. Limit pipeline credentials and third-party actions; pin reviewed dependencies. Define telemetry retention, alert ownership, and actionable runbooks. Readiness tests serving capability; liveness tests process health, avoiding dependency-triggered restart storms. Local orchestration such as Aspire is optional and does not become the production deployment platform by implication.

## Rules and verification

| Rule | Requirement | Evidence |
| --- | --- | --- |
| PL-001 | Application pipelines MUST independently build, test, and release immutable artifacts. | Pipeline review |
| PL-002 | Changes MUST run applicable unit, architecture, integration, contract, security, and critical journey checks. | CI evidence review |
| PL-003 | Production workloads MUST emit structured logs, useful metrics, traces, and readiness/liveness signals without exposing sensitive data. | Operational smoke tests |
| PL-004 | Secrets MUST be supplied through approved secret management and MUST NOT appear in source, images, or logs. | Secret scanning and deployment review |

## Adoption

Read [governance](../governance/adoption.md). Proposed rules are not approved merely because they use MUST. Record solution-specific choices, tests, and exceptions in the pinned baseline.
