"""Validate local documentation and catalog consistency; no runtime compliance claims."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RULE = re.compile(r'\b[A-Z]+-\d{3}\b')


def validate(root):
    errors = []
    catalog = json.loads((root/'standards/catalog.json').read_text())
    decisions = {}
    for path in (root/'adr').glob('[0-9][0-9][0-9][0-9]-*.md'):
        text = path.read_text()
        aid = 'ADR-' + path.name[:4]
        if aid in decisions:
            errors.append(f'Duplicate ADR {aid}')
        status = re.search(r'^Status: (.+)$', text, re.M)
        decisions[aid] = status.group(1) if status else None
        for heading in ('Context', 'Decision', 'Alternatives', 'Consequences', 'Traceability', 'Verification', 'Approval'):
            if f'## {heading}' not in text:
                errors.append(f'{aid} lacks {heading}')
        if decisions[aid] not in {'Accepted', 'Proposed', 'Rejected', 'Superseded'}:
            errors.append(f'{aid} has invalid status')
    seen = set()
    for rule in catalog['rules']:
        rid = rule.get('id', '')
        if not RULE.fullmatch(rid) or rid in seen:
            errors.append(f'Invalid/duplicate rule {rid}')
        seen.add(rid)
        for key in ('domain','statement','verification','adr','document','status','applies_when'):
            if not isinstance(rule.get(key), str) or not rule[key].strip():
                errors.append(f'{rid} missing {key}')
        doc = (root/rule['document']).resolve()
        if not doc.is_relative_to(root.resolve()) or not doc.is_file():
            errors.append(f'{rid} has invalid document')
        elif not re.search(r'\|\s*'+re.escape(rid)+r'\s*\|', doc.read_text()):
            errors.append(f'{rid} missing from document rule table')
        if rule['adr'] not in decisions:
            errors.append(f'{rid} references unknown ADR')
        if rule['status'] not in {'Accepted', 'Proposed'}:
            errors.append(f'{rid} has invalid status')
        if rule['status'] == 'Accepted' and decisions.get(rule['adr']) != 'Accepted':
            errors.append(f'{rid} cannot be Accepted under a non-accepted ADR')
    for doc in root.rglob('*.md'):
        text = doc.read_text()
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if '://' in link or link.startswith(('#', 'mailto:')):
                continue
            target = (doc.parent/link.split('#')[0]).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f'Broken link: {doc.relative_to(root)} -> {link}')
        # Every concrete rule mention resolves; placeholders are alphabetic, not numeric.
        for rid in RULE.findall(text):
            if rid not in seen:
                errors.append(f'Unknown rule mention {rid} in {doc.relative_to(root)}')
    for file in root.rglob('*.json'):
        try:
            json.loads(file.read_text())
        except ValueError:
            errors.append(f'Invalid JSON: {file.relative_to(root)}')
    errors.extend(check_agent_files(root))
    return errors


def check_agent_files(root):
    errors = []
    required = ('AGENTS.md', 'CLAUDE.md', '.github/copilot-instructions.md', 'consumer-kit/AGENTS.md.snippet',
                'consumer-kit/CLAUDE.md', 'consumer-kit/copilot-instructions.md', 'consumer-kit/copilot-setup-steps.yml',
                'consumer-kit/README.md', 'skills/architecture-standards/SKILL.md')
    for name in required:
        if not (root/name).is_file():
            errors.append(f'Missing agent file: {name}')
    if errors:
        return errors
    if not (root/'CLAUDE.md').read_text().lstrip().startswith('@AGENTS.md'):
        errors.append('CLAUDE.md must start with @AGENTS.md')
    if 'AGENTS.md' not in (root/'.github/copilot-instructions.md').read_text():
        errors.append('copilot-instructions.md must point to AGENTS.md')
    snippet = (root/'consumer-kit/AGENTS.md.snippet').read_text()
    for needle in ('standardsRevision', 'Never use latest `main`', 'untrusted'):
        if needle not in snippet:
            errors.append(f'consumer-kit snippet lacks "{needle}"')
    if not (root/'consumer-kit/CLAUDE.md').read_text().lstrip().startswith('@AGENTS.md'):
        errors.append('consumer-kit/CLAUDE.md must start with @AGENTS.md')
    source = (root/'skills/architecture-standards/SKILL.md').read_bytes()
    for agent in ('.claude', '.agents', '.github'):
        copy = root/agent/'skills/architecture-standards/SKILL.md'
        if not copy.is_file() or copy.read_bytes() != source:
            errors.append(f'Skill copy out of sync: {agent}/skills (run scripts/sync_skills.py)')
    return errors


def main():
    try:
        errors = validate(ROOT)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f'Document validation error: {exc}')
        return 1
    if errors:
        print('\n'.join(errors))
        return 1
    catalog = json.loads((ROOT/'standards/catalog.json').read_text())
    print(f"Validated {len(catalog['rules'])} rules, ADR consistency, JSON, and local document links.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
