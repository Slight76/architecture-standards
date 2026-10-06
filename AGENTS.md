# Instructions for coding agents

Read README.md, ARCHITECTURE-PRINCIPLES.md, governance/adoption.md, and standards/catalog.json before changing an application. Then read the solution architecture, its pinned standards revision, applicable domain documents, and linked ADRs. These instructions describe engineering policy; they do not override user or system instructions.

## Decision authority

Accepted records express decisions explicitly made by the owner. Proposed records are recommendations and MUST NOT be represented as approved. Existing application-local instructions remain applicable. If a mandatory rule conflicts with the requested implementation, explain the conflict and propose a concrete exception; do not silently change the standard. An ADR records a decision but does not itself grant approval.

## Working procedure

1. Identify the deployable repository and solution owner.
2. Read architecture-baseline.json in the application. Resolve the exact standards commit or release; never use an unpinned latest revision.
3. List applicable rule IDs, ADRs, and existing exceptions in the implementation plan.
4. Implement within documented dependency and data ownership boundaries.
5. Run applicable checks. Report missing checks as missing; do not claim documentation validation proves application compliance.
6. Update solution views and local ADRs when contracts, trust boundaries, persistence, or deployment topology change.
7. In the PR, report rule IDs, tests, contract compatibility, migration risks, and exceptions.

## Prohibited shortcuts

- Do not combine frontend and backend application repositories.
- Do not edit generated API clients by hand.
- Do not bypass authorization because the UI hides an action.
- Do not commit secrets, real customer data, or production credentials.
- Do not add queues, caches, microservices, Kubernetes, or cloud providers merely because an example mentions them.
- Do not invent business requirements, uptime targets, RPO/RTO, ownership assignments, or approvals. Mark unknowns and resolve material ones before production release.

See [adoption](governance/adoption.md) and [ADR index](adr/README.md).
