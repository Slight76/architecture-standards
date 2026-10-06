# Solution design and production readiness

Baseline: 0.2.0 recommended draft. Applies when: multiple applications form a business solution

Decision: [ADR-0023](../adr/0023-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Design packet

A solution packet must answer: who uses it, what outcome matters, which components deploy independently, what data they own, how identity flows, how failure is handled, and who operates it. Reference enterprise rules rather than copy them. Pin the baseline and distinguish current, target, and transition states.

Required views: system context (people/external systems), container (deployables/stores), critical sequence/data flow (protocol, identity, transaction and trust boundaries), and deployment (network and failure domains). Add component/ER diagrams where they resolve complexity; do not draw every class. Label optional/future components as such.

## Concrete required decisions

Record public origins/CORS, browser identity profile, authorization model, API/versioning strategy, client generation, data ownership, concurrency, retry/idempotency, migrations, hosting, release compatibility, telemetry, and recovery. Use the profile defaults unless a requirement warrants a departure. The solution supplies origins, actual roles, deadlines, capacities, retention, SLO/RPO/RTO, and owners; agents cannot infer these from a code sample.

## Requirement format

Each quality requirement has a scenario and measurable acceptance: stimulus, environment/load, affected journey, expected response, threshold, and verification. Example: after an API instance terminates during an adjustment, retrying the same scoped idempotency key produces one committed adjustment. The solution then supplies its response-time/load targets.

## Failure matrix

| Failure | Design question |
| --- | --- |
| Database unavailable | Which operations fail, how quickly, and do readiness signals behave safely? |
| Response lost after commit | How does caller discover/replay the committed outcome? |
| Identity provider down | What happens to existing/new sessions and revocation expectations? |
| Old browser release remains cached | Which API/schema versions remain compatible? |
| Queue duplicate/poison event | Where is deduplication and how is authorized redrive performed? |
| Region/host/storage loss | What restores first and what loss/downtime is measured? |

## Production readiness gate

Readiness requires approved business targets, named operations ownership, tested deployment/rollback, compatibility evidence, security negative tests, working alerts/runbooks, and measured recovery. Unknowns are tracked with owner and due date. Not every unknown blocks a prototype, but absent identity, data authorization, or recovery decisions block corresponding production claims.

Use the [solution template](../templates/solution-architecture.md) and [evidence template](../templates/implementation-evidence.md). Review against applicable rules; do not sign off a system solely because the documentation checker passes.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| SA-004 | Solution designs MUST resolve cross-domain implementation choices and document measurable quality scenarios. | Design packet with baseline, decision table, and acceptance scenarios |
| SA-005 | Production readiness MUST include failure, compatibility, security, operations, and recovery evidence. | Readiness review linked to actual test reports/runbooks |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
