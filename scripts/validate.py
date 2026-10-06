"""Validate documentation integrity, not application compliance."""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((root / 'standards/catalog.json').read_text())
seen = set()
for rule in catalog['rules']:
    if rule['id'] in seen:
        errors.append(f"Duplicate rule: {rule['id']}")
    seen.add(rule['id'])
    doc = root / rule['document']
    if not doc.is_file() or rule['id'] not in doc.read_text():
        errors.append(f"Rule absent from document: {rule['id']}")
    number = rule['adr'].split('-')[1]
    if len(list((root / 'adr').glob(f'{number}-*.md'))) != 1:
        errors.append(f"Invalid ADR reference: {rule['adr']}")
    if rule['status'] not in ('Accepted', 'Proposed'):
        errors.append(f"Invalid rule status: {rule['id']}")
for doc in root.rglob('*.md'):
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
        if '://' in link or link.startswith('#'):
            continue
        target = (doc.parent / link.split('#')[0]).resolve()
        if not target.is_relative_to(root) or not target.exists():
            errors.append(f"Broken local link: {doc.relative_to(root)} -> {link}")
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f"Validated {len(seen)} rules and all local Markdown links.")
