#!/usr/bin/env python3
"""Read-only library checks; generation is explicit."""
import argparse
import subprocess
import sys
from pathlib import Path
sys.dont_write_bytecode = True
from generated_artifacts import check_generated, generate

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--check-generated', action='store_true', help='Also compare all generated contents without rewriting.')
    group.add_argument('--generate', action='store_true', help='Explicitly regenerate ignored artifacts before comparison.')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()
    steps = [
        ('packages', ['validate_skills.py']),
        ('static routing', ['check_skill_routing.py'] + (['--verbose'] if args.verbose else [])),
        ('recorded behavior evidence', ['check_skill_behavior.py'] + (['--verbose'] if args.verbose else [])),
        ('regression tests', ['-m', 'unittest', 'discover', '-s', 'scripts', '-p', 'test_*.py']),
        ('canonical root parity', ['check_mirror_parity.py', '--agents-root', str(ROOT)]),
    ]
    for label, command in steps:
        command = [sys.executable, '-B', *command] if command[0] == '-m' else [sys.executable, '-B', str(ROOT / 'scripts' / command[0]), *command[1:]]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if args.verbose or result.returncode:
            print(result.stdout + result.stderr)
        print(f'{label}: ' + ('PASS' if result.returncode == 0 else 'FAIL'))
        if result.returncode:
            return result.returncode
    if args.generate:
        generate()
    if args.generate or args.check_generated:
        errors = check_generated()
        if errors:
            print('; '.join(errors))
            print('Regenerate explicitly: python3 scripts/check_all_skills.py --generate')
            return 1
        print('generated catalog, manifest and reports: PASS')
    print('Static checks complete. Unrun/stale behavioral evaluations are not passes.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
