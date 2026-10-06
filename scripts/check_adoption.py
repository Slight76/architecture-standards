"""Check declared baseline coverage/evidence shape; never attest runtime compliance."""
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r'[0-9a-f]{40}')
STATUSES = {'passed', 'failed', 'not_run', 'not_applicable', 'excepted'}


def substantive(value):
    return isinstance(value, str) and bool(value.strip()) and not any(
        marker in value.upper() for marker in ('REPLACE', 'YYYY-MM-DD', 'TODO'))


def validate_adoption(catalog, baseline, evidence, require_pass=False, today=None):
    errors = []
    today = today or date.today()
    if not isinstance(baseline, dict) or not isinstance(evidence, dict):
        return ['Baseline and evidence must be objects']
    known = {r['id'] for r in catalog['rules']}
    for name in ('standardsRepository', 'solutionDocument'):
        if not substantive(baseline.get(name)):
            errors.append(f'Baseline requires {name}')
    if not SHA.fullmatch(str(baseline.get('standardsRevision', ''))):
        errors.append('Baseline requires immutable 40-character standardsRevision')
    if baseline.get('baselineVersion') != catalog['version']:
        errors.append('Baseline version does not match this catalog')
    if baseline.get('applicationKind') not in {'frontend', 'backend', 'worker', 'infrastructure', 'solution'}:
        errors.append('Unknown applicationKind')
    record = baseline.get('adoptionRecord', {})
    if not isinstance(record, dict):
        record = {}
    for key in ('owner', 'date', 'evidence'):
        if not substantive(record.get(key)):
            errors.append(f'Adoption record requires {key}')
    try:
        adopted = date.fromisoformat(record.get('date', ''))
        if adopted > today:
            errors.append('Adoption date cannot be in the future')
    except (ValueError, TypeError):
        errors.append('Adoption date must be YYYY-MM-DD')
    applicable = baseline.get('applicableRules', [])
    excluded = baseline.get('excludedRules', [])
    exceptions = baseline.get('acceptedExceptions', [])
    checks = evidence.get('checks', [])
    for name, collection in [('applicableRules', applicable), ('excludedRules', excluded),
                             ('acceptedExceptions', exceptions), ('checks', checks)]:
        if not isinstance(collection, list):
            errors.append(f'{name} must be an array')
    if errors and not all(isinstance(x, list) for x in (applicable, excluded, exceptions, checks)):
        return errors
    if not all(isinstance(x, str) for x in applicable):
        return errors + ['applicableRules must contain rule IDs']
    if len(set(applicable)) != len(applicable):
        errors.append('Duplicate applicable rules')
    excluded_ids = []
    for item in excluded:
        if not isinstance(item, dict):
            errors.append('Each excluded rule must be an object')
            continue
        excluded_ids.append(item.get('rule'))
        if not substantive(item.get('reason')):
            errors.append(f"Excluded rule {item.get('rule')} requires a reason")
    if not all(isinstance(x, str) for x in excluded_ids):
        return errors + ['Excluded rule requires a rule ID']
    if len(set(excluded_ids)) != len(excluded_ids):
        errors.append('Duplicate excluded rules')
    declared = set(applicable) | set(excluded_ids)
    if set(applicable) & set(excluded_ids):
        errors.append('Rules cannot be both applicable and excluded')
    if declared != known:
        errors.append(f'Coverage mismatch: missing={sorted(known-declared)}, unknown={sorted(declared-known)}')
    exception_map = {}
    for item in exceptions:
        if not isinstance(item, dict):
            errors.append('Exception must be an object')
            continue
        eid = item.get('id')
        if not substantive(eid):
            errors.append('Exception requires an ID')
            continue
        if eid in exception_map:
            errors.append(f'Duplicate exception {eid}')
        exception_map[eid] = item
        for key in ('owner', 'approvalEvidence', 'reason', 'remediation'):
            if not substantive(item.get(key)):
                errors.append(f'Exception {eid} requires {key}')
        if item.get('status') != 'Accepted':
            errors.append(f'Exception {eid} is not Accepted')
        rules = item.get('rules', [])
        if not isinstance(rules, list) or not rules or not all(isinstance(r, str) and r in applicable for r in rules):
            errors.append(f'Exception {eid} must name applicable rules')
        try:
            if date.fromisoformat(item.get('expires', '')) <= today:
                errors.append(f'Exception {eid} is expired')
        except (ValueError, TypeError):
            errors.append(f'Exception {eid} requires a valid expiry')
    for key in ('standardsRevision', 'baselineVersion'):
        if evidence.get(key) != baseline.get(key):
            errors.append(f'Evidence {key} differs from baseline')
    if not SHA.fullmatch(str(evidence.get('applicationCommit', ''))):
        errors.append('Evidence requires a tested applicationCommit')
    seen = set()
    for check in checks:
        if not isinstance(check, dict):
            errors.append('Check must be an object')
            continue
        rid, status = check.get('rule'), check.get('status')
        if not isinstance(rid, str):
            errors.append('Check requires rule ID')
            continue
        if rid in seen:
            errors.append(f'Duplicate evidence for {rid}')
        seen.add(rid)
        if rid not in applicable:
            errors.append(f'Evidence for non-applicable rule {rid}')
        if status not in STATUSES:
            errors.append(f'Invalid status for {rid}')
        elif status == 'passed':
            if not substantive(check.get('method')) or not substantive(check.get('evidence')):
                errors.append(f'Passed rule {rid} requires method and evidence')
        elif status == 'excepted':
            ex = exception_map.get(check.get('exceptionId'), {})
            if rid not in ex.get('rules', []):
                errors.append(f'Rule {rid} lacks a covering accepted exception')
        elif not substantive(check.get('reason')):
            errors.append(f'Rule {rid} requires a reason for {status}')
        if require_pass and status in {'failed', 'not_run'}:
            errors.append(f'Release gate: {rid} is {status}')
    if seen != set(applicable):
        errors.append(f'Missing evidence for {sorted(set(applicable)-seen)}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', required=True, type=Path)
    parser.add_argument('--evidence', required=True, type=Path)
    parser.add_argument('--require-pass', action='store_true')
    args = parser.parse_args()
    try:
        catalog = json.loads((ROOT/'standards/catalog.json').read_text())
        baseline = json.loads(args.baseline.read_text())
        evidence = json.loads(args.evidence.read_text())
        errors = validate_adoption(catalog, baseline, evidence, args.require_pass)
    except (OSError, ValueError) as exc:
        print(f'Cannot validate adoption: {exc}')
        return 1
    if errors:
        print('\n'.join(errors))
        return 1
    print('Declared adoption/evidence structure passed; runtime compliance is not attested.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
