# Infrastructure architecture

Baseline: 0.2.0 recommended draft. Scope/decision: [ADR-0008](../adr/0008-infrastructure.md).

## Purpose

Compute, network, DNS, routing, edge, storage, environments, capacity, and recovery beneath platform services.

## Design

Choose managed services, containers, or VMs from requirements and operating capacity. Kubernetes is optional. Document zones/regions or local failure domains, public/private boundaries, routing, DNS ownership, certificate renewal, firewall rules, storage classes, and resource limits. Verify redundant components do not share an unrecognized single point of failure. IaC state contains sensitive material and requires protection. Plans require review for replacements and deletions. Recovery includes DNS, identities, secret access, images, configuration, and data; test reconstruction in an isolated environment.

## Rules and verification

| Rule | Requirement | Evidence |
| --- | --- | --- |
| INF-001 | Infrastructure MUST be version-controlled with reviewed plans and controlled production apply identities. | IaC plan and drift review |
| INF-002 | Data stores MUST use restricted network access and documented ingress/egress paths. | Network policy verification |
| INF-003 | Production topology MUST document failure domains, capacity assumptions, DNS, certificates, and recovery dependencies. | Deployment and recovery review |

## Adoption

Read [governance](../governance/adoption.md). Proposed rules are not approved merely because they use MUST. Record solution-specific choices, tests, and exceptions in the pinned baseline.

## Implementation standards

- [Network, compute, configuration, and infrastructure lifecycle](implementation-standard.md)
