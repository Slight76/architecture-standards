# Solution architecture

Baseline: 0.1.0 draft. Scope/decision: [ADR-0002](../adr/0002-solution.md).

## Purpose

Describe a particular business system using enterprise policies. Link separately deployed frontend, backend, workers, data stores, and external systems.

## Design

Maintain context, container, deployment, and critical sequence views. A context view treats the entire solution as one system; a container view expands applications and stores. Update views when topology or trust boundaries change. Record measurable availability, latency, throughput, RPO, RTO, retention, and capacity requirements with owner approval.

## Rules and verification

| Rule | Requirement | Evidence |
| --- | --- | --- |
| SA-001 | Every production solution MUST document context, deployables, repositories, owners, and external dependencies. | Solution release review |
| SA-002 | Trust boundaries, data flows, failure modes, and deployment topology MUST be documented. | Threat and deployment review |
| SA-003 | Solutions MUST pin their standards baseline and record scoped exceptions. | Baseline and exception review |

## Adoption

Read [governance](../governance/adoption.md). Proposed rules are not approved merely because they use MUST. Record solution-specific choices, tests, and exceptions in the pinned baseline.
