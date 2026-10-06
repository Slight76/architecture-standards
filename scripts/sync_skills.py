"""Copy the canonical skill to per-agent locations; --check fails on drift. Copies, not symlinks (Windows-safe)."""
import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = 'architecture-standards'
SOURCE = ROOT/'skills'/SKILL/'SKILL.md'
TARGETS = [ROOT/d/'skills'/SKILL/'SKILL.md' for d in ('.claude', '.agents', '.github')]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args(argv)
    expected = SOURCE.read_bytes()
    drift = [t for t in TARGETS if not t.is_file() or t.read_bytes() != expected]
    if args.check:
        for t in drift:
            print(f'Out of sync: {t.relative_to(ROOT)} (run scripts/sync_skills.py)')
        return 1 if drift else 0
    for t in drift:
        t.parent.mkdir(parents=True, exist_ok=True)
        t.write_bytes(expected)
        print(f'Updated {t.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
