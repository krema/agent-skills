"""Publish the validated checkout's version once, using its changelog section."""
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


def release_notes(version, changelog):
    if not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', version):
        raise ValueError('VERSION must be a stable major.minor.patch version')
    sections = re.split(r'^## ', changelog, flags=re.MULTILINE)[1:]
    matches = [s.split('\n', 1)[1].strip() for s in sections
               if s.split('\n', 1)[0].startswith(version + ' — ')]
    if len(matches) != 1 or not matches[0]:
        raise ValueError('Expected exactly one nonempty changelog section for VERSION')
    return matches[0] + '\n'


def gh(*args):
    return subprocess.check_output(['gh', *args], text=True)


def pages(repo, resource):
    return [item for page in json.loads(gh('api', '--paginate', '--slurp',
            f'repos/{repo}/{resource}?per_page=100')) for item in page]


def publish(repo, sha, version, notes):
    tag = 'v' + version
    for release in pages(repo, 'releases'):
        if release['tag_name'] == tag:
            if release['draft'] or release['prerelease']:
                raise ValueError('Existing draft/prerelease needs maintainer review')
            print(f'{tag} is already published; nothing to do.')
            return
    for existing in pages(repo, 'tags'):
        if existing['name'] == tag and existing['commit']['sha'] != sha:
            raise ValueError('Existing tag targets another commit; refusing to release or move it')
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / 'notes.md'
        path.write_text(notes)
        print(gh('release', 'create', tag, '--repo', repo, '--target', sha,
                 '--title', tag, '--notes-file', str(path)))


def main():
    if os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise ValueError('Releases are allowed only from main')
    if os.environ.get('GITHUB_EVENT_NAME') not in ('push', 'workflow_dispatch'):
        raise ValueError('Unsupported release event')
    sha = os.environ['GITHUB_SHA']
    if subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() != sha:
        raise ValueError('Checkout does not match the validated workflow commit')
    version = Path('VERSION').read_text().strip()
    notes = release_notes(version, Path('CHANGELOG.md').read_text())
    publish(os.environ['GITHUB_REPOSITORY'], sha, version, notes)


if __name__ == '__main__':
    main()
