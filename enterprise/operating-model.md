# Enterprise governance, portfolio, and technology lifecycle

Baseline: 0.2.0 recommended draft. Applies when: a solution adopts enterprise architecture standards

Decision: [ADR-0023](../adr/0023-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Decision layers and ownership

Enterprise architecture defines business capability boundaries, investment direction, shared services, technology lifecycle, and cross-domain policy. Solution architecture maps one business outcome to applications and stores. Domain standards define how each application is implemented. A decision belongs at the narrowest level that resolves its effects; changing one screen does not need an enterprise ADR.

| Role | Responsibility |
| --- | --- |
| Business owner | Outcome, criticality, acceptable loss/downtime and funding |
| Solution owner | End-to-end design, dependencies, compatibility, operational readiness |
| Domain maintainer | Technical standards, examples, validation and upgrades |
| Application owner | Implementation, runtime, incidents, evidence and baseline pin |
| Data steward | Classification, quality, retention and authorized use |

Names remain unassigned until the owner supplies them; do not fabricate an approval chain. Small teams may combine roles but cannot omit responsibilities.

## Registers

Maintain a capability/application register, dependency map, data ownership register, and technology register. For each technology record purpose, selected version/range, support end, owner, status (evaluate/adopt/hold/retire), upgrade plan, and exception. A product being named in an example does not add it to the technology register.

Classify system criticality from actual business impact. Each tier needs measurable recovery/service expectations and controls justified by that impact; do not assign invented enterprise-wide uptime percentages. Record costs including operations, storage growth, backup retention, telemetry, licenses, and exit/migration work. Review duplication before adopting another platform.

## Change and review triggers

A new trust boundary, persistent store, communication style, public contract break, service split, or reliability tier change requires a solution ADR and affected-owner review. Local refactoring within an adopted boundary requires normal code review. Emergency changes need a subsequent record and reconciliation; an emergency is not permission for permanent undocumented drift.

Accept, supersede, or reject ADRs with evidence. Preserve historical rationale and trace successor decisions. Rule IDs never get reused for different meanings. Track which applications adopt each immutable baseline; notify owners of material changes through their approved process.

## Adoption outcomes

A standards document is useful when an engineer/agent can select a default, understand its limits, implement it, and produce evidence. Evaluate adoption using escaped failures, onboarding time, exception age, and upgrade lag—not documentation volume. Maintain a migration path so an improved policy can actually reach existing applications.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| EA-004 | Solutions MUST record accountable business, technical, operational, and data ownership responsibilities. | Ownership register with actual names before production |
| EA-005 | Adopted technologies MUST have lifecycle, cost, and migration ownership. | Technology register and upgrade review |
| EA-006 | Material cross-boundary changes MUST maintain decision and application-baseline traceability. | ADR impact and adoption register review |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
