# ADR-0028: Retire the enterprise layer

Status: Accepted

Date: 2026-10-06

Owner: @Slight76

## Context

Versions 0.1 through 0.3 framed this repository as an "enterprise architecture standards" program with a dedicated enterprise layer (`enterprise/architecture.md`, `enterprise/operating-model.md`, rules EA-001..EA-006, ADR-0001, ADR-0023). The actual audience is a small team and its coding agents. The enterprise framing added a governance tier nobody staffs, encouraged agents to over-build (see ADR-0022), and made the documents harder to read. Supersedes [ADR-0001](0001-enterprise.md) and [ADR-0023](0023-implementation-decisions.md).

## Decision

Remove the enterprise layer and its wording from every standards document:

- The surviving content (role table, registers, change and review triggers, adoption outcomes) becomes the team operating model in `standards-marketplace/governance/team-operating-model.md`.
- Rules EA-001..EA-006 are retired with `status: Superseded` and `superseded_by: GOV-001` in the marketplace catalog. IDs are never reused.
- "Enterprise" wording is permitted only in historic ADRs, changelogs, migration notes, and catalogs; the shared validator rejects it elsewhere. Documents say "team" where they previously said "enterprise".
- Anything that genuinely belongs to a larger organisation (portfolio funding, cross-company policy) is out of scope for these handbooks and will live elsewhere if it is ever needed.

## Alternatives

- Keep the layer but rename it: rejected; the tier still had no owner or consumer.
- Delete the content outright: rejected; ownership and traceability expectations are still useful and are kept in the operating model.

## Consequences

Consumers whose baselines list EA-* rules must move those rows to `excludedRules` or drop them when they adopt catalog 1.0.0. GOV-001 (declare pinned standards in `architecture-baseline.json`) replaces the intent of EA-006.

## Traceability

EA-001..EA-006 (Superseded); GOV-001; [ADR-0029](0029-split-into-domain-handbooks.md); standards-marketplace ADR-0001.

## Verification

`validate.py` enterprise-wording gate passes in all six repositories; marketplace catalog lists EA-* as Superseded with successor GOV-001.

## Approval

@Slight76, 2026-10-06, direction given in the planning session that produced the v1.0.0 split ("we shouldn't call any portion of it enterprise").
