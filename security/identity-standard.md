# Identity, authorization, and session design

Baseline: 0.3.0 recommended draft. Applies when: an application authenticates users or workloads

Decision: [ADR-0015](../adr/0015-implementation-decisions.md). Rules become binding when this baseline is adopted; examples explain the policy and do not establish business requirements.


## Choose a named identity profile

Default for a first-party sensitive business web application: a same-origin backend-for-frontend (BFF) session using an established OpenID Connect provider. The browser receives a Secure, HttpOnly cookie; tokens remain server-side. Web and API still build and deploy separately. A BFF adds operating cost; document whether it resides in the API host or its own independently owned service.

Use a direct SPA public-client profile only when static hosting or direct API access is justified. Use authorization code with PKCE through the provider SDK. Do not create client secrets in a browser or implement custom password/token cryptography. Default to in-memory browser access tokens; any persistent token storage needs a threat-model decision covering XSS and session recovery. Avoid the implicit and resource-owner-password flows for new applications.

For machine calls prefer workload/federated identity with audience-limited permissions; use the provider's supported client credentials flow where federation is unavailable. User delegation and workload identity are different grants. An ID token is not a bearer access token for a business API.

## Enforce access on every boundary

APIs validate issuer, audience, signature, time validity, and required permissions through a maintained authentication library. Configure schemes deliberately; a valid token for another API must fail. Fail closed on missing identity configuration. Mark anonymous endpoints explicitly and test their intended exposure.

Authorization combines operation permission with object/tenant scope. Establish the tenant from verified identity and membership; never trust a tenant header, URL, or body value alone. Filter reads by authorized scope and recheck mutations at the authoritative layer. An authenticated administrator role does not automatically grant every tenant. Background tasks carry verified scope and audit attribution.

## Browser session controls

Cookie sessions require antiforgery protection on state-changing requests, deliberate SameSite behavior, session expiry, logout invalidation, and CSRF tests. SameSite alone is not the complete control. Use narrow cookie paths/domains and a host-only cookie where practical. Cross-site cookies need a documented Secure/SameSite configuration and may still be blocked by browser privacy policies. Test actual target browsers.

Define idle and absolute lifetimes, renewal behavior, multi-device logout expectations, permission-change propagation, and account disablement. These durations are business/security inputs, not arbitrary constants chosen by an agent. CORS does not solve CSRF. Do not put tokens in URLs or logs.

## Example permission specification

| Operation | Permission | Resource condition |
| --- | --- | --- |
| View stock | inventory.read | Caller belongs to warehouse's tenant |
| Adjust stock | inventory.adjust | Caller is allowed to adjust that warehouse |
| Export audit | inventory.audit.read | Tenant scope and export policy both pass |

This illustrates a policy; it does not assign actual user permissions. Test missing, expired, wrong-audience, and insufficient-scope tokens; a valid user requesting another tenant's resource; disabled sessions; and anonymous access to protected routes. Never bypass these cases using a development-only authentication handler in production configuration.

Source: [OAuth security best current practice](https://www.rfc-editor.org/rfc/rfc9700). The default BFF choice and permission model are repository policy decisions.


## Rules and required evidence

| ID | Requirement | Verification |
| --- | --- | --- |
| IAM-001 | Each solution MUST select and document its browser/workload identity profile and session lifecycle. | Identity ADR, logout/expiry integration tests |
| IAM-002 | APIs MUST authenticate tokens for their intended audience and enforce resource/tenant authorization. | Wrong-audience and cross-tenant denial tests |
| IAM-003 | Cookie-authenticated mutations MUST include independently verified CSRF protection. | Missing, invalid, and cross-session antiforgery tests |
| IAM-004 | Agents MUST NOT introduce custom identity protocols or browser client secrets. | Dependency/configuration and browser bundle review |

## Exceptions

Use the [exception record](../templates/exception.md) for a departure. Record affected rules, scope, compensating controls, approval evidence, expiry, and migration path. Agents must not silently replace defaults.
