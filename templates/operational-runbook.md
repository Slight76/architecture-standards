# Operational runbook

Service, owner/on-call route, environment, last tested commit and date.

## Trigger and impact

Alert, user harm, detection query, scope and severity.

## Diagnosis

Safe read-only checks; dashboards/traces; dependency and artifact/config/schema versions. Exclude sensitive payloads.

## Recovery

Ordered actions, required authority/identity, stop/abort conditions, expected outcomes, validation and rollback. Include exact environment-specific commands in the consuming repository.

## Verification

Business smoke path, data consistency, recovery targets, alert clearance and monitoring period.

## Evidence and follow-up

Actual exercise/incident result, measured RPO/RTO where relevant, discrepancies, remediation owners and next review.
