# Enterprise architecture

Baseline: 0.1.0 draft. Scope/decision: [ADR-0001](../adr/0001-enterprise.md).

## Purpose

Document capabilities, application landscape, ownership, technology lifecycle, dependencies, and investment priorities. Separate current state from target state and migration stages.

## Design

Business capabilities → solutions → independent applications → owned data and infrastructure. Maintain a register with capability, solution, repository, owner, lifecycle, criticality, and dependencies. Do not invent enterprise facts; the register begins empty.

## Rules and verification

| Rule | Requirement | Evidence |
| --- | --- | --- |
| EA-001 | Each solution MUST identify its business capability and accountable owner. | Solution document review |
| EA-002 | Applications MUST communicate through documented contracts and identify data owners. | Dependency and data ownership review |
| EA-003 | Technology selections SHOULD follow a supported lifecycle and require justification for new platforms. | Technology register review |

## Adoption

Read [governance](../governance/adoption.md). Proposed rules are not approved merely because they use MUST. Record solution-specific choices, tests, and exceptions in the pinned baseline.
