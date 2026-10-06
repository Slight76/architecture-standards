# Implementation evidence

Record application commit, standards repository/revision/version, adoption record, and task scope. Use implementation-evidence.json for machine validation.

| Rule | Status | Command or review | Evidence | Reason/exception |
| --- | --- | --- | --- | --- |
| Actual rule ID | passed / failed / not_run / not_applicable / excepted | Actual invocation or review method | Report path or reviewed URL | Required for non-pass |

Include changed API/schema contracts, supported old/new versions, migration/rollback behavior, and remaining risks. Do not mark a prose example as a test run. A documentation checker cannot verify application runtime controls.

Run `python3 scripts/check_adoption.py --baseline <manifest> --evidence <evidence>` from the pinned standards checkout. Add `--require-pass` for release eligibility. Passing validates shape/coverage, not truth of evidence; review the reports.
