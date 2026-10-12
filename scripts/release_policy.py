"""Check stable collection versions against committed distribution content."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess

# Repository tooling and human maintenance docs are not the installed plugin.
ARTIFACT_PATHS = ('skills', '.claude-plugin', '.codex-plugin', '.agents/plugins',
                  '.github/plugin', 'LICENSE', 'provenance.json')


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


def version_tuple(version):
    if not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', version):
        raise ValueError('VERSION must be a stable major.minor.patch version')
    return tuple(map(int, version.split('.')))


def release_notes(version, changelog):
    version_tuple(version)
    sections = re.split(r'^## ', changelog, flags=re.MULTILINE)[1:]
    matches = [s.partition('\n')[2].strip() for s in sections
               if s.partition('\n')[0].startswith(version + ' — ')]
    if len(matches) != 1 or not matches[0]:
        raise ValueError('Expected exactly one nonempty changelog section for VERSION')
    return matches[0] + '\n'


def artifact(ref):
    # Includes names, modes and blob IDs: additions, removals and chmod all count.
    return git('ls-tree', '-r', '-z', ref, '--', *ARTIFACT_PATHS)


def version_at(ref):
    return git('show', f'{ref}:VERSION')


def notes_at(ref):
    return release_notes(version_at(ref), git('show', f'{ref}:CHANGELOG.md'))


def check(base, head='HEAD'):
    old, new = version_at(base), version_at(head)
    if version_tuple(new) < version_tuple(old):
        raise ValueError('Collection version must not decrease')
    notes_at(head)
    if new == old:
        if artifact(base) != artifact(head):
            raise ValueError('Distributed content changed without a new VERSION')
        if notes_at(base) != notes_at(head):
            raise ValueError('Existing version notes changed; use a new version')
    return new


def event_base(event, event_name):
    if event_name == 'pull_request':
        return event['pull_request']['base']['sha']
    if event_name == 'push':
        before = event['before']
        if not before or set(before) == {'0'}:
            raise ValueError('No comparison baseline; initial release needs explicit review')
        return before
    if event_name == 'workflow_dispatch':
        return 'HEAD^'
    raise ValueError('Pass --base for a local release-policy check')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Committed baseline; local checks compare HEAD to it')
    args = parser.parse_args()
    base = args.base
    if not base:
        event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
        base = event_base(event, os.environ['GITHUB_EVENT_NAME'])
    print(f'Release policy passed for {check(base)}')


if __name__ == '__main__':
    main()
