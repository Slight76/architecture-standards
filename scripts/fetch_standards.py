"""Check out the standards revision pinned in architecture-baseline.json into .standards/."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys


def git(*args, cwd=None):
    subprocess.run(['git', *args], cwd=cwd, check=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', default='architecture-baseline.json')
    parser.add_argument('--dest', default='.standards')
    args = parser.parse_args(argv)
    baseline = json.loads(Path(args.baseline).read_text())
    repo, rev = baseline.get('standardsRepository'), baseline.get('standardsRevision')
    if not re.fullmatch(r'https://[\w.-]+/[\w./-]+', repo or '') or not re.fullmatch(r'[0-9a-f]{40}', rev or ''):
        print('Baseline needs an https standardsRepository URL and a 40-character standardsRevision.')
        return 1
    dest = Path(args.dest)
    try:
        if not (dest/'.git').exists():
            git('clone', '--no-checkout', '--', repo, str(dest))
        git('fetch', repo, rev, cwd=dest)
        git('-c', 'advice.detachedHead=false', 'checkout', '--detach', rev, cwd=dest)
    except (subprocess.CalledProcessError, OSError) as exc:
        print(f'Could not retrieve standards revision {rev}: {exc}')
        return 1
    print(f'{dest} is at {rev}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
