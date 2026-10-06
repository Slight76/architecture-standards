# Build, release, and supply-chain controls

Baseline: 0.2.0 recommended draft. Applies when: an application or infrastructure artifact is delivered

Decision: [ADR-0020](../adr/0020-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Repository and artifact lifecycle

Frontend, backend, and worker repositories own independent pipelines. Default to short-lived branches and reviewed pull requests into main. Releases use immutable artifact identifiers and semantic application versions; do not require a long-lived release branch unless multiple maintained lines need it. Pin the standards baseline separately from package versions.

Build once from a known commit, retain test reports and dependency manifests, and promote the same artifact digest across environments. Browser runtime configuration can vary by environment through an explicitly public config artifact; secrets never enter the browser build. Database migrations are versioned deployment artifacts with their own controlled step.

## Required pipeline stages

| Change | Minimum evidence |
| --- | --- |
| Frontend | Frozen dependency install, format/lint/import checks, typecheck, behavior tests, build, accessibility and critical E2E |
| Backend | Locked restore, analyzers/build, domain/use-case tests, dependency tests, real-engine integration and HTTP tests |
| API contract | Schema validation, regeneration drift, compatibility diff and supported-consumer tests |
| Persistence | Clean/upgrade/mixed-version migration tests and destructive-change review |
| Infrastructure | Format/validate, policy checks, plan review, drift and recovery implications |
| All production artifacts | Secret/dependency scanning, provenance, immutable ID and release evidence |

Path filters may reduce cost only if shared changes cannot skip affected checks. Set required check names in repository protection when supported; adding a workflow file alone does not make it a merge gate. Treat flaky/quarantined tests as an explicit risk with owner/expiry, not a passing suite.

## Workflow security

Use minimum token permissions, pin third-party actions to reviewed full commit SHAs, and prefer short-lived OIDC credentials for cloud access. Do not execute untrusted pull-request code with production secrets or privileged pull_request_target contexts. Treat branch names, issue text, and PR titles as untrusted data rather than shell code. Dependabot/update tooling must preserve pin review and compatibility checks.

Produce an SBOM where the artifact ecosystem supports it; define severity/exploitability remediation ownership rather than a scanner badge alone. Document exceptions and expiry. Do not automatically weaken checks to make a release pass.

## Deployment protocol

Record artifact digest, source commit, configuration version, schema state, and supported client/server versions. Run preflight checks, expand migration if needed, deploy a canary or rolling update appropriate to the platform, test a business smoke path, then promote. Monitor meaningful error/latency signals during the rollout. Roll back to a known compatible artifact; never assume old code can read the current schema.

Production rollout policy is owned by the solution and platform. This document does not authorize an agent to deploy to an environment outside its task authorization. Provide actual deployment and rollback commands in the application runbook and test them in staging.

## Failure cases

Dependency install fails without network; artifact provenance mismatches commit; migration succeeds but API rollout fails; new frontend hits an old API; client caches old HTML; signing/deployment credentials expire. Each needs a documented response. Never retag a different image under an immutable release identifier.

Source: [GitHub secure use](https://docs.github.com/en/actions/reference/security/secure-use). Pipeline matrix and release behavior are enterprise policy.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| CICD-001 | Pipelines MUST produce immutable artifacts and retain traceable build/test evidence. | Artifact digest, source commit, lockfile, and report audit |
| CICD-002 | Privileged workflows MUST isolate untrusted code and use least-privilege short-lived access where available. | Workflow permissions and fork/PR threat review |
| CICD-003 | Release plans MUST test client/server/schema compatibility and a concrete rollback path. | Staging rollout/rollback and compatibility matrix |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
