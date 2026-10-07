# ADR-0030: Multi-repository baseline (architecture-baseline.json schema v2)

Status: Accepted

Date: 2026-10-06

Owner: @Slight76

## Context

Baseline v1 pinned a single `standardsRepository` and `standardsRevision` and required `baselineVersion` to equal the one catalog's version. After [ADR-0029](0029-split-into-domain-handbooks.md) an application adopts several handbooks, each with its own revision and catalog version. ADR-0011 (agent consumption) still requires that agents read an immutable pinned revision, never latest `main`.

## Decision

Introduce schema v2 for `architecture-baseline.json`:

```json
{
  "schemaVersion": 2,
  "standards": [
    { "repository": "https://github.com/Slight76/data-standards", "revision": "<40-char sha>", "catalogVersion": "1.0.0" }
  ],
  "solutionDocument": "...", "applicationKind": "...", "adoptionRecord": {...},
  "applicableRules": [], "excludedRules": [], "acceptedExceptions": []
}
```

- `standards[]` lists every adopted handbook; coverage is checked against the union of their non-superseded rules.
- `implementation-evidence.json` carries a matching `standards[]` of repository/revision pins instead of `standardsRevision`/`baselineVersion`.
- `fetch_standards.py` checks out each entry into `.standards/<repo-name>/`; `check_adoption.py --standards-dir .standards` reads each `catalog/catalog.json`.
- The v1 shape remains accepted with a deprecation warning until the next minor release of the tooling.
- GOV-001 makes declaring this baseline mandatory for any repository that adopts a handbook.

## Alternatives

- Keep v1 and point it at the marketplace only: rejected; the marketplace holds no domain rules and consumers could not pin handbooks independently.
- One pin for all handbooks (a marketplace release SHA that resolves to handbook SHAs): rejected for v1.0.0 as indirection without a consumer asking for it; may be revisited.

## Consequences

Consumers migrate their baselines once. Tooling moved from `scripts/` here to `standards-marketplace/tooling/`. CI for consumers checks out multiple public repositories; no token is required.

## Traceability

GOV-001; ADR-0011; ADR-0024; standards-marketplace ADR-0001; templates in `standards-marketplace/templates/architecture-baseline.json` and `implementation-evidence.json`.

## Verification

`standards-marketplace/tooling/tests` cover v2 acceptance, v1 deprecation, pin mismatch, coverage, and missing catalogs. `agent-hub-api` and `agent-hub-web` pass `check_adoption.py` on v2 baselines.

## Approval

@Slight76, 2026-10-06, planning session.
