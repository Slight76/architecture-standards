# Observability, health, and service objectives

Baseline: 0.2.0 recommended draft. Applies when: an application runs outside local development

Decision: [ADR-0021](../adr/0021-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Signal ownership

Use OpenTelemetry-compatible instrumentation for traces/metrics and structured logs with trace correlation. The solution selects exporters and a backend; do not hardwire one vendor into domain code. Record service name, environment, version, and instance identity. Trust trace headers only as correlation data, never as caller identity.

| Signal | Minimum useful coverage |
| --- | --- |
| HTTP | Request volume, latency distributions, failure rate by route template/status |
| Database | Query duration/failure, pool exhaustion, saturation and lock contention |
| Worker | Throughput, age of oldest pending work, retries, dead letters |
| Business | Relevant accepted/rejected operations with safe low-cardinality dimensions |
| Runtime | CPU, memory, restarts, queue/thread/connection pressure |

Use route templates rather than raw URLs as metric labels. User IDs, tenant IDs, request IDs, and arbitrary error text create high cardinality and may leak data; do not use them as metric labels. Logs and audit trails need classification, retention, access control, and redaction. Audit events record actor/action/target/outcome under restricted access; diagnostic logs are not automatically the audit system.

## Health semantics

Expose `/alive` for process liveness and `/health` for readiness through the platform's controlled network path. Liveness must not fail merely because the database is down and cause restart loops. Readiness reports whether the instance can serve its supported workload, with bounded checks and cached results where appropriate. A failed optional dependency should degrade the affected function rather than necessarily removing all capacity. Health output must not leak connection strings or internal topology.

## SLO specification

Define the user journey, good-event numerator, eligible-event denominator, measurement window, latency threshold where relevant, data source, and exclusion policy. An availability percentage without those definitions is incomplete. Targets require an accountable owner and business context. Use error-budget/burn-rate alerts tied to user harm; avoid paging on every transient exception.

Example format, without invented production targets: `successful eligible stock reads / all eligible stock reads over <window> >= <target>`, with latency measured separately at an approved percentile. Record whether throttles, client errors, scheduled maintenance, and downstream failures count. Keep the query and dashboard versioned.

## Operational validation

Trigger one synthetic failure and follow its trace across API and database/worker. Confirm the on-call alert routes correctly and links a runbook. Stop a dependency and observe readiness/liveness behavior. Simulate telemetry exporter loss: buffering is bounded and the app does not block indefinitely. Test redaction with synthetic secret-like inputs and sampling behavior under load.

Source: [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/). Health and SLO acceptance policy is defined here.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| OBS-001 | Production workloads MUST expose useful correlated signals with bounded cardinality and redaction. | Trace walkthrough, cardinality review, and telemetry failure test |
| OBS-002 | Readiness and liveness MUST have distinct bounded semantics and controlled exposure. | Dependency outage and restart-loop tests |
| SLO-001 | Production services MUST define measurable user-centered objectives, owners, and actionable alerts. | Versioned SLI query, alert exercise, and runbook evidence |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
