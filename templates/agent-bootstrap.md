# Application agent bootstrap

Read architecture-baseline.json and local instructions. Retrieve the exact standardsRevision from the named standardsRepository using approved repository access into a read-only checkout. Read its AGENTS.md task map, adoption policy, applicable detailed standards and linked ADRs. Resolve this solution's declared inputs and accepted exceptions before implementation.

Do not substitute latest main, treat examples as production configuration, or infer enterprise approval from a Proposed ADR. An adopted profile provides defaults for ordinary authorized work. Raise material unresolved business/security requirements while continuing independent work.

Before finishing, record application commit, rule IDs, actual commands/reviews and evidence in implementation-evidence.json. Run the pinned standards adoption checker plus this application's own checks. Distinguish failed/not_run/not_applicable/excepted from passed. Never claim that the adoption checker proves runtime compliance.
