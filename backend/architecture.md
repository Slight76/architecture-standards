# Backend architecture

Baseline: 0.2.0 recommended draft. Scope/decision: [ADR-0004](../adr/0004-backend.md).

## Purpose

Independently deployable API or worker. Proposed baseline: a modular monolith with inward dependencies and explicit module ownership.

## Design

Proposed project layout: Product.Api, Product.Application, Product.Domain, Product.Infrastructure, and Product.Contracts. Application depends on Domain; Infrastructure depends on Application/Domain. API may reference Infrastructure only in its composition root to register implementations; endpoint code uses Application/Contracts. Organize each layer by business module and use case. Domain entities enforce invariants. Application orchestrates transactions and ports. Infrastructure owns database and remote integrations. Contracts contain external transport DTOs and remain free of persistence entities. Avoid generic repositories by default; choose use-case-specific ports. Do not create microservices solely to mirror domains. Unit-test invariants and use cases; integrate against real selected storage; test authorization and contract behavior at HTTP boundaries.

## Rules and verification

| Rule | Requirement | Evidence |
| --- | --- | --- |
| BE-001 | Domain MUST NOT depend on Application, Infrastructure, API, HTTP, or persistence frameworks. | Assembly and package architecture tests |
| BE-002 | Application MUST NOT depend on Infrastructure or API. | Assembly architecture tests |
| BE-003 | Infrastructure MUST implement ports owned by Application or Domain. | Architecture tests and design review |
| BE-004 | Endpoints MUST delegate business decisions to application/domain code and enforce documented authorization. | API tests and endpoint review |
| BE-005 | Module data MUST be accessed through its owned interfaces; cross-module writes MUST NOT bypass ownership. | Module dependency tests and data review |

## Adoption

Read [governance](../governance/adoption.md). Proposed rules are not approved merely because they use MUST. Record solution-specific choices, tests, and exceptions in the pinned baseline.

## Implementation standards

- [Backend modules, use cases, and dependencies](implementation-standard.md)
- [Persistence, transactions, and query behavior](persistence-standard.md)
- [Cache selection, ownership, and invalidation](caching-standard.md)
