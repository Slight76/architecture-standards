# Standards adoption and governance

The standards repository contains architecture policy and examples. Application code lives in separate repositories. A solution document links those repositories and records the deployed topology.

## Normative language

MUST is mandatory within an adopted baseline. SHOULD is a default whose departure requires documented reasoning. MAY is optional. Proposed rules become mandatory only when the solution owner adopts that baseline. An example is never a requirement by itself.

## Adoption

Commit architecture-baseline.json in each application using the template. Pin an immutable standards commit and document applicable rule IDs and accepted exceptions. Copy an agent bootstrap into the application's AGENTS.md so agents actually discover the external rules; an AGENTS.md in this repository alone will not load in other repositories. The [consumer kit](../consumer-kit/README.md) provides the bootstrap snippet, Claude and Copilot shims, a Copilot setup workflow, and `.standards/` retrieval (submodule or `scripts/fetch_standards.py`).

Use a reviewed PR to change the pinned revision. Summarize new, removed, and changed rules and migration work. Existing applications do not automatically inherit a change to main.

## Exceptions and precedence

System/user instructions govern agent behavior. Within adopted engineering policy, accepted time-bounded exceptions override their named rules; solution decisions specialize enterprise rules without silently weakening them. Domain standards specialize principles. Proposed ADRs and examples do not override accepted decisions. Unresolved contradictions must be raised rather than guessed.

Record an exception's rule, scope, rationale, alternative controls, owner, approving authority, approval evidence, expiry, and remediation issue. A proposed exception is not permission. Review exceptions at expiry and material topology changes.

## Ownership and release

The repository owner appoints domain maintainers; names are currently unassigned. Reviewers check cross-domain effects, compatibility, enforceability, and documentation links. Release with semantic versions: major for incompatible policy, minor for compatible additions, patch for clarifications. Preserve superseded ADRs and link replacements. Do not overwrite historical rationale.

## v0.2 application manifest and evidence

Use the baseline template and resolve every applicable domain against its `applies_when` conditions. List rule IDs in applicableRules; exclusions go in excludedRules with a concrete reason. Account for every catalog rule exactly once. A frontend-only repo can exclude database runtime rules because the separately owned API implements them, while still applying integration/client rules. Do not use exclusions to hide violations; a violation needs an accepted exception.

Adoption is a solution-owned decision, recorded in adoptionRecord with owner, date, and evidence. A baseline pin plus that record applies the recommended defaults; it does not globally change Proposed ADRs to Accepted. The catalog's status refers to enterprise decision provenance, while the manifest records application adoption.

The evidence file identifies the same standards revision/version and a tested application commit. Include every applicable rule once. `passed` needs a named command or review and evidence reference; failed/not_run/not_applicable need reasons; excepted needs an accepted unexpired exception whose named rules cover it. Use `--require-pass` in a release gate to reject failed/not_run checks. Evidence validation checks structure, not authenticity or completeness of runtime proof; reviewers inspect referenced reports.

Legacy v0.1 marked some detailed rules Accepted when only their domain scope was approved. v0.2 corrects those labels to Proposed without removing their policy content. FE-001 links directly to the accepted independent-application decision.
