# Standards adoption and governance

The standards repository contains architecture policy and examples. Application code lives in separate repositories. A solution document links those repositories and records the deployed topology.

## Normative language

MUST is mandatory within an adopted baseline. SHOULD is a default whose departure requires documented reasoning. MAY is optional. Proposed rules become mandatory only when the solution owner adopts that baseline. An example is never a requirement by itself.

## Adoption

Commit architecture-baseline.json in each application using the template. Pin an immutable standards commit and document applicable rule IDs and accepted exceptions. Copy an agent bootstrap into the application's AGENTS.md so agents actually discover the external rules; an AGENTS.md in this repository alone will not load in other repositories.

Use a reviewed PR to change the pinned revision. Summarize new, removed, and changed rules and migration work. Existing applications do not automatically inherit a change to main.

## Exceptions and precedence

System/user instructions govern agent behavior. Within adopted engineering policy, accepted time-bounded exceptions override their named rules; solution decisions specialize enterprise rules without silently weakening them. Domain standards specialize principles. Proposed ADRs and examples do not override accepted decisions. Unresolved contradictions must be raised rather than guessed.

Record an exception's rule, scope, rationale, alternative controls, owner, approving authority, approval evidence, expiry, and remediation issue. A proposed exception is not permission. Review exceptions at expiry and material topology changes.

## Ownership and release

The repository owner appoints domain maintainers; names are currently unassigned. Reviewers check cross-domain effects, compatibility, enforceability, and documentation links. Release with semantic versions: major for incompatible policy, minor for compatible additions, patch for clarifications. Preserve superseded ADRs and link replacements. Do not overwrite historical rationale.
