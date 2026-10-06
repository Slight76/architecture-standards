# Network, compute, configuration, and infrastructure lifecycle

Baseline: 0.3.0 recommended draft. Applies when: a solution provisions runtime infrastructure

Decision: [ADR-0022](../adr/0022-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Platform selection

Default to the simplest managed/container/VM platform that satisfies workload, network, recovery, and operating-skill requirements. Kubernetes is conditional, not an enterprise prerequisite. A local lab may use VMs while a production solution uses managed services; document both without pretending their failure guarantees are identical.

Independently deployed web/API artifacts may share a public origin through an edge router. Static hosting never directly routes a browser to a database. A public API may be exposed through a gateway/load balancer with identity/rate controls; data stores stay on restricted paths. An internal hostname alone is not an access control.

## Mandatory deployment inventory

| Concern | Required record |
| --- | --- |
| Network | Ingress/egress source, destination, protocol, port, purpose, owner |
| DNS/TLS | Record owner, certificate issuance/renewal, expiry monitoring, recovery |
| Compute | Runtime/image, resource requests/limits, scaling and shutdown behavior |
| Data | Storage durability, encryption, backup identity, failure domain |
| Identity | Workload/deploy identities and least-privilege roles |
| Environment | Isolation, configuration provenance, secret source, drift policy |
| Recovery | Dependency order, artifact/IaC state access, RPO/RTO evidence |

Configure reverse-proxy forwarded headers only from trusted proxies and verify the public scheme/host used in redirects and callback URLs. Enforce HTTPS externally and encrypt internal sensitive traffic according to the trust model. Do not disable certificate verification to solve development routing issues.

## Runtime hardening and capacity

Containers run as non-root where supported, use a minimal runtime image pinned by digest, drop unnecessary capabilities, and avoid writable filesystems except declared paths. Define request/body/time limits at compatible edge and application layers. Set CPU/memory and connection budgets using representative load tests; resource exhaustion must fail predictably. Implement graceful shutdown and a termination allowance matched to draining behavior.

HA requires independent failure domains and tested traffic failover; two replicas on one host are not host-level redundancy. Horizontal scaling may require shared session state or stateless tokens, distributed idempotency storage, and coordinated scheduled jobs. Caches must tolerate flush/failure according to their declared role. Scale limits include database connections and downstream quotas.

## Infrastructure as code

Version resources and non-secret configuration. Protect and lock state; state can contain secrets. Review plans for replacement/deletion and conduct controlled applies with environment-specific identities. Detect drift and reconcile through review rather than blindly overwriting emergency fixes. Agent task authorization still governs destructive operations.

Promote versioned modules with migration notes. Avoid hand-edited production settings that cannot be reproduced. Test rebuild in a separate environment and include DNS, certificates, identity, secrets, and backup access. A successful plan is not evidence that disaster recovery works.

## Verification

From an untrusted path, confirm direct datastore access fails. Verify allowed application traffic, certificate renewal monitoring, proxy redirect correctness, resource-limit behavior, graceful draining, and zone/host loss for the chosen reliability tier. Record architecture differences between local, test, and production environments.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| INF-004 | Solutions MUST document and verify traffic boundaries, DNS/TLS ownership, and trusted proxy behavior. | Network reachability and redirect/certificate tests |
| INF-005 | Runtime deployments MUST define resource limits, scaling dependencies, and graceful termination. | Load/saturation and shutdown/failover tests |
| INF-006 | Infrastructure state/configuration MUST be protected, reproducible, and reviewed for drift and destructive changes. | IaC plan, state-access audit, and rebuild exercise |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
