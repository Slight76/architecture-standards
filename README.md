# Enterprise architecture standards

Version 0.1.0: reviewable draft baseline for independently deployed applications and agent-assisted development. Application implementations and frontend/backend templates belong in separate repositories. This repository contains policy, decisions, templates, and illustrative designs.

## Start here

Read [agent instructions](AGENTS.md), [principles](ARCHITECTURE-PRINCIPLES.md), [adoption](governance/adoption.md), [ADR index](adr/README.md), and the [rule catalog](standards/catalog.json).

## Architecture domains

- [Enterprise architecture](enterprise/architecture.md)
- [Solution architecture](solution/architecture.md)
- [Frontend architecture](frontend/architecture.md)
- [Backend architecture](backend/architecture.md)
- [Database architecture](database/architecture.md)
- [Integration architecture](integration/architecture.md)
- [Platform architecture](platform/architecture.md)
- [Infrastructure architecture](infrastructure/architecture.md)
- [Security architecture](security/architecture.md)

## Reuse

Use [solution template](templates/solution-architecture.md), [baseline](templates/architecture-baseline.json), [agent bootstrap](templates/agent-bootstrap.md), and [ADR template](templates/adr.md). The [inventory example](solution/examples/inventory.md) demonstrates traceability without prescribing extra services.

## Validation

Run `python3 scripts/validate.py`. This checks document links, catalog identifiers, ADR references, and rule-document coverage. It does not validate application architecture. Application CI must implement the checks listed in its adopted catalog.

## Review status

Detailed technical rules are proposed unless explicitly accepted or adopted. Technology profile is proposed. This draft makes no claim of compliance with external frameworks. Identity provider, deployment target, actual owners, service levels, and specific supported runtime versions remain solution decisions. No license is granted until an owner-selected LICENSE is added.
