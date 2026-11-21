"""Install this downloaded skill locally. No network, credentials or paid calls."""
from pathlib import Path
import argparse
import os
import shutil
import sys
from verify_package import verify


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, help='Exact destination skill folder; must not exist')
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1]
    home = Path(os.environ.get('CODEX_HOME', Path.home() / '.codex'))
    destination = (args.dest or home / 'skills/qw-adcreative-intelligence').expanduser().resolve()
    if destination.exists():
        parser.error(f'Destination already exists: {destination}. Back up and review the existing skill before updating.')
    if destination == source or destination.is_relative_to(source):
        parser.error('Destination must be outside the downloaded source folder')
    result = verify(source)
    if not result['passed']:
        parser.error('Source integrity check failed: ' + '; '.join(result['errors']))
    destination.mkdir(parents=True)
    for name in ['SKILL.md', 'agents', 'references', 'scripts']:
        item = source / name
        if item.is_dir():
            shutil.copytree(item, destination / name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        else:
            shutil.copy2(item, destination / name)
    installed = verify(destination)
    if not installed['passed']:
        print('Installation is incomplete; inspect destination: ' + str(destination), file=sys.stderr)
        return 1
    print('Installed and integrity-checked: ' + str(destination))
    print('Start a new Codex chat and invoke $qw-adcreative-intelligence. Host tools remain subject to availability.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
