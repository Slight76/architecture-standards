# Threat modeling and secure application behavior

Baseline: 0.3.0 recommended draft. Applies when: an application accepts untrusted data or handles protected information

Decision: [ADR-0015](../adr/0015-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Threat model scope

For each trust boundary identify the actor, data, entry point, asset, misuse case, mitigation, residual risk, and verification. Include browser-to-edge, API-to-store, service-to-service, queues, CI/CD, external webhooks, and agent tooling where present. Revisit on identity, data classification, dependency, or topology changes. Avoid claiming framework compliance without a scoped assessment.

## Required boundary controls

Validate shape, length, ranges, and content type at input boundaries; authorize before disclosing resource details. Apply request size and rate limits by a trustworthy identity/key with bounded anonymous handling. Avoid rate limiting only by attacker-supplied headers. Output-encode for context; do not insert untrusted HTML without a reviewed sanitizer. Use an explicit Content Security Policy and frame-embedding policy suited to the application; introduce changes with browser testing, not blindly copied header lists.

Prevent SSRF by limiting outbound destinations for URL-fetching features, rejecting unsafe schemes, and controlling resolved/private/link-local destinations and redirects. Network egress policy complements validation. File uploads require byte-size limits, content inspection, safe generated storage names, isolated object storage, download authorization, and scanning/quarantine appropriate to risk. Never execute uploaded content or trust filename extensions alone.

Secrets use approved stores, scoped identities, rotation, and incident revocation. Redact authorization/cookie headers and sensitive request bodies. An incident response record identifies who revokes credentials, preserves evidence, informs stakeholders, and validates recovery. New dependencies need provenance/license/security review, not just popularity.

## Webhooks and external input

Verify signatures using the provider's documented raw-byte canonicalization, apply timestamp/replay controls, and scope each source to its authorized operations. Authentication secrets never appear in webhook URLs. Durable processing uses the same deduplication/queue rules as internal events. Malformed signatures fail before side effects.

## Negative test matrix

Cross-tenant IDs, mass assignment of privileged fields, malicious sort/SQL values, oversized payloads, expired/replayed webhook signatures, arbitrary URL fetches, unsupported file types, and secret-bearing errors all receive explicit tests when applicable. Map each mitigation to a test or review owner. Do not create tests that merely confirm a security option is set without demonstrating the intended denial.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| SEC-005 | Exposed boundaries MUST validate inputs and mitigate applicable injection, SSRF, upload, and abuse risks. | Threat-linked negative tests |
| SEC-006 | Secrets and sensitive telemetry MUST have scoped access, rotation, redaction, and incident procedures. | Synthetic leak tests and revocation exercise |
| SEC-007 | Webhooks MUST authenticate payloads and prevent unauthorized replay before side effects. | Bad-signature, expired-timestamp, and replay tests |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
