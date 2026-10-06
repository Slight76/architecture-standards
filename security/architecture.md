# Security architecture

Baseline: 0.1.0 draft. Scope/decision: [ADR-0009](../adr/0009-security.md).

## Purpose

Cross-domain identity, authorization, threat modeling, data classification, and secure operations.

## Design

Select the identity provider and browser session design through a solution ADR. Evaluate a backend-for-frontend cookie session versus a public-client authorization-code flow with PKCE using the actual threat model. Avoid universal token-storage prescriptions. Cookie sessions require deliberate CSRF protection and cookie settings; cross-origin deployments require narrowly scoped CORS. Validate token issuer, audience, expiry, and permissions on APIs. Apply object-level authorization independently of UI state. Define rate limiting, upload validation, dependency updates, incident handling, key rotation, and audit retention based on exposure and classification.

## Rules and verification

| Rule | Requirement | Evidence |
| --- | --- | --- |
| SEC-001 | Every exposed operation MUST define authentication and server-enforced authorization, including resource ownership. | Positive and negative authorization tests |
| SEC-002 | Solutions MUST document threats, trust boundaries, data classification, and mitigation owners. | Threat model review |
| SEC-003 | Browser applications MUST NOT contain confidential credentials and token/session handling MUST follow the documented identity design. | Bundle inspection and identity tests |
| SEC-004 | Sensitive data MUST have defined encryption, retention, deletion, and telemetry redaction controls. | Security and data lifecycle review |

## Adoption

Read [governance](../governance/adoption.md). Proposed rules are not approved merely because they use MUST. Record solution-specific choices, tests, and exceptions in the pinned baseline.
