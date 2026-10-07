# ADR-0029: Split into five domain handbooks plus a marketplace

Status: Accepted

Date: 2026-10-06

Owner: @Slight76

## Context

At v0.3.0 this repository held ~70 files across nine domain folders, one 111-rule catalog, 27 ADRs, and three mirrored skill directories. Readers had to understand the whole tree to find one standard, agents loaded one oversized skill, and every domain shared one version number. The team wants handbooks that are easy to read and that agents can pull selectively.

## Decision

Split the content by audience domain into five public repositories, each versioned independently and installable as an agent skill, indexed by a sixth hub repository:

| Repository | Content moved from v0.3.0 |
| --- | --- |
| `architecture-standards` (this repo) | solution/*, frontend architecture and accessibility, backend architecture, CQRS, middleware, OpenAPI, integration/* (HTTP API, contracts, messaging), ADRs, principles |
| `engineering-standards` | agent-development, testing, backend/frontend implementation, adoption process |
| `operations-standards` | platform architecture, delivery, observability, infrastructure/*, operational runbook template |
| `data-standards` | database architecture/design, migration and recovery, persistence, caching |
| `security-standards` | security architecture, application security, CORS, identity, threat-model template |
| `standards-marketplace` | operating model, technology profile, sources, shared templates, consumer kit, tooling, rule index, marketplace manifest |

Mechanics: fresh repositories with copied files (history stays here, tagged `v0.3.0-pre-split`); rule IDs and historic ADR numbers unchanged; each domain catalog carries the subset of rules and declares the historic ADRs it depends on under `externalDecisions`; cross-repository links are absolute GitHub URLs; the shared validator plus `catalog/rule-index.json` keep rule mentions resolvable across repositories. Moved paths are listed in [MOVED.md](../MOVED.md).

## Alternatives

- Reorganise folders inside one repository: rejected; no selective install or independent versioning.
- Five repositories with no hub: rejected; tooling and templates would be duplicated and consumers would have no single routing table.
- `git filter-repo` per domain to keep history: rejected for v1.0.0 as unnecessary complexity; the pre-split tag preserves history.

## Consequences

Cross-domain changes may need pull requests in more than one repository. Release requires tagging each repository and recording SHAs in the marketplace manifest. Readers get a focused handbook per domain and agents load only the skills they need.

## Traceability

[ADR-0028](0028-retire-enterprise-layer.md), [ADR-0030](0030-multi-repository-baseline.md), [ADR-0031](0031-skill-distribution.md); standards-marketplace ADR-0001; engineering/operations/data/security-standards ADR-0001.

## Verification

Every rule from catalog 0.3.0 appears exactly once across the six catalogs (105 active, 6 superseded); `validate.py` passes in every repository; `MOVED.md` lists every removed path.

## Approval

@Slight76, 2026-10-06, split approved in the planning session.
