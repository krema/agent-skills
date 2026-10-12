"""Publish a validated collection version, preserving existing release identity."""
import json
import os
from pathlib import Path
import subprocess
import tempfile

from release_policy import artifact, git, notes_at, version_at, version_tuple


def gh(*args):
    return subprocess.check_output(['gh', *args], text=True)


def pages(repo, resource):
    return [item for page in json.loads(gh('api', '--paginate', '--slurp',
            f'repos/{repo}/{resource}?per_page=100')) for item in page]


def stable_version(item):
    if item['draft'] or item['prerelease'] or not item['tag_name'].startswith('v'):
        return None
    try:
        return version_tuple(item['tag_name'][1:])
    except ValueError:
        return None


def verify_existing(item, tag_sha, sha, version, notes):
    if item['draft'] or item['prerelease']:
        raise ValueError('Existing draft/prerelease needs maintainer review')
    if not tag_sha:
        raise ValueError('Published release is missing its tag')
    # Full checkout includes history. Fetch a newly created tag commit if this job
    # waited in the queue after checkout; never update or overwrite a local tag.
    if subprocess.run(['git', 'cat-file', '-e', f'{tag_sha}^{{commit}}'],
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode:
        git('fetch', '--no-tags', 'origin', tag_sha)
    git('merge-base', '--is-ancestor', tag_sha, sha)
    if version_at(tag_sha) != version or artifact(tag_sha) != artifact(sha):
        raise ValueError('Published version differs from this artifact; bump VERSION')
    if notes_at(tag_sha).strip() != notes.strip() or (item.get('body') or '').strip() != notes.strip():
        raise ValueError('Published release notes do not match the approved version')


def missing_versions(sha, releases):
    # Start at introduction of this publisher, not older pre-automation releases.
    additions = git('log', '--first-parent', '--diff-filter=A', '--format=%H',
                    sha, '--', 'scripts/release.py').splitlines()
    if not additions:
        return []
    start = additions[-1]
    commits = [start] + git('rev-list', '--first-parent', '--reverse',
                            f'{start}..{sha}', '--', 'VERSION').splitlines()
    published = {r['tag_name'] for r in releases if stable_version(r) is not None}
    current = version_at(sha)
    pending = {}
    for commit in commits:
        version = version_at(commit)
        version_tuple(version)
        if version != current and 'v' + version not in published:
            pending.setdefault(version, commit)
    return sorted(pending.items(), key=lambda pair: version_tuple(pair[0]))


def publish(repo, sha, version, notes):
    candidate = version_tuple(version)
    releases = pages(repo, 'releases')
    tags = {t['name']: t['commit']['sha'] for t in pages(repo, 'tags')}
    tag = 'v' + version
    for missed, commit in missing_versions(sha, releases):
        print(f'::warning::Missing release v{missed} at {commit}; rerun that commit\'s validated main workflow.')
    for item in releases:
        if item['tag_name'] == tag:
            verify_existing(item, tags.get(tag), sha, version, notes)
            print(f'{tag} already matches the approved artifact; nothing to do.')
            return
    if tag in tags and tags[tag] != sha:
        raise ValueError('Existing tag targets another commit; refusing to release or move it')
    newer = any(v is not None and v > candidate for v in map(stable_version, releases))
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / 'notes.md'
        path.write_text(notes)
        gh('release', 'create', tag, '--repo', repo, '--target', sha,
           '--title', tag, '--notes-file', str(path),
           '--latest=false' if newer else '--latest=true')
    # Do not claim success solely from a successful create request.
    created = next((r for r in pages(repo, 'releases') if r['tag_name'] == tag), None)
    actual = next((t['commit']['sha'] for t in pages(repo, 'tags') if t['name'] == tag), None)
    if not created or actual != sha:
        raise ValueError('Release creation not verified; inspect state before retrying')
    verify_existing(created, actual, sha, version, notes)
    print(f'Published and verified {tag} at {sha}')


def main():
    if os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise ValueError('Releases are allowed only from main')
    if os.environ.get('GITHUB_EVENT_NAME') not in ('push', 'workflow_dispatch'):
        raise ValueError('Unsupported release event')
    sha = os.environ['GITHUB_SHA']
    if git('rev-parse', 'HEAD') != sha:
        raise ValueError('Checkout does not match the validated workflow commit')
    version = version_at(sha)
    publish(os.environ['GITHUB_REPOSITORY'], sha, version, notes_at(sha))


if __name__ == '__main__':
    main()
