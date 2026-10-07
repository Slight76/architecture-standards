---
title: "Architecture decision records: when and how"
status: proposed
version: 1.0.0
owner: "@Slight76"
---
# Architecture decision records: when and how

Baseline: 1.0.0. Applies when: a change meets a review trigger in the team operating model or an engineer wants a decision to outlive the conversation that produced it

Decision: [ADR-0029](../adr/0029-split-into-domain-handbooks.md). This document describes process; it adds no rules. Decisions that affect rules are recorded in the catalog through the ADR they cite.

## What an ADR is for

An ADR captures one decision, the context that forced it, the options considered, and what it costs. It is short (one screen), written when the decision is made, and never edited to change history. A later decision supersedes it instead.

## When to write one

Write an ADR when a change:

- introduces or removes a trust boundary, persistent store, or communication style;
- breaks a public contract or splits/merges a service;
- changes a reliability tier, hosting platform, or core framework;
- departs from a handbook default for longer than one release (pair it with an [exception record](https://github.com/Slight76/standards-marketplace/blob/main/templates/exception.md));
- would otherwise be re-argued in every code review.

Do not write one for local refactoring inside an adopted boundary, naming choices covered by a handbook, or anything the handbook already decides.

## Where it lives

| Scope | Location | Numbering |
| --- | --- | --- |
| Team-wide architecture | this repository, `adr/` | `ADR-00NN`, continues from the index |
| A handbook's own policy | `<handbook>/adr/` | `ADR-00NN` local to that handbook |
| One application or solution | the application repository, `docs/adr/` | `ADR-NNNN` local to that repository |

Application ADRs that specialise a handbook rule must cite the rule ID; they cannot silently weaken it.

## Format

Use the marketplace [ADR template](https://github.com/Slight76/standards-marketplace/blob/main/templates/adr.md). Required headings: Context, Decision, Alternatives, Consequences, Traceability, Verification, Approval. `Status:` is one of Proposed, Accepted, Rejected, Superseded; a Superseded record names its successor (`Superseded by: ADR-00NN`). Date and owner are filled by a human; agents leave `Unassigned` rather than inventing a name.

## Lifecycle

1. Open a pull request with the ADR as Proposed. Link the issue or discussion that prompted it.
2. Reviewers challenge the alternatives, not the prose. A proposed ADR may ship with the code when the decision is reversible; irreversible decisions wait for Accepted.
3. Accept by recording approver, date, and evidence in Approval. Acceptance covers the decision's scope, not every detailed rule it enables.
4. Supersede rather than edit. The old record stays, gains `Status: Superseded` and a successor line, and may receive a short inline amendment note (as ADR-0001..0012 did in v1.0.0).
5. Add a row to `adr/README.md`; update any rule whose `adr` field should move to the new record.

## Agent guidance

Agents may draft ADRs but must not set `Status: Accepted` or fill Approval. Cite the handbook rules the decision touches by ID. When two accepted decisions conflict, raise it rather than choose.
