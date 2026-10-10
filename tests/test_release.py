from contextlib import contextmanager
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import release
import release_policy as policy


@contextmanager
def repository():
    previous = Path.cwd()
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        try:
            policy.git('init', '-q')
            policy.git('config', 'user.name', 'Synthetic Maintainer')
            policy.git('config', 'user.email', 'maintainer@example.invalid')
            Path('skills/sample').mkdir(parents=True)
            Path('skills/sample/SKILL.md').write_text('Original instruction')
            Path('VERSION').write_text('1.1.1\n')
            Path('CHANGELOG.md').write_text('## 1.1.1 — date\nNotes\n')
            Path('scripts').mkdir()
            Path('scripts/release.py').write_text('# Synthetic publisher fixture\n')
            commit()
            yield
        finally:
            os.chdir(previous)


def commit():
    policy.git('add', '.')
    policy.git('commit', '-qm', 'Synthetic fixture')
    return policy.git('rev-parse', 'HEAD')


def item(version='1.1.1', **kwargs):
    return dict(tag_name='v' + version, draft=False, prerelease=False, body='Notes', **kwargs)


def tag(sha, version='1.1.1'):
    return {'name': 'v' + version, 'commit': {'sha': sha}}


class PolicyTests(unittest.TestCase):
    def test_notes_select_exact_version_and_reject_invalid_sections(self):
        self.assertEqual(policy.release_notes('1.1.1', '## 1.1.10 — date\nWrong\n## 1.1.1 — date\nNotes'), 'Notes\n')
        for version, text in [('01.1.0', ''), ('1.0.0', ''), ('1.0.0', '## 1.0.0 — date\n'),
                              ('1.0.0', '## 1.0.0 — date\nA\n## 1.0.0 — date\nB')]:
            with self.subTest(version=version, text=text), self.assertRaises(ValueError):
                policy.release_notes(version, text)

    def test_artifact_changes_need_bump_but_internal_changes_do_not(self):
        with repository():
            base = policy.git('rev-parse', 'HEAD')
            Path('README.md').write_text('Internal maintenance explanation')
            commit()
            self.assertEqual(policy.check(base), '1.1.1')
            Path('skills/sample/SKILL.md').write_text('Changed instruction')
            commit()
            with self.assertRaisesRegex(ValueError, 'without a new VERSION'):
                policy.check(base)
            Path('VERSION').write_text('1.1.2')
            Path('CHANGELOG.md').write_text('## 1.1.2 — date\nFix\n## 1.1.1 — date\nNotes\n')
            commit()
            self.assertEqual(policy.check(base), '1.1.2')

    def test_manifest_license_provenance_additions_deletions_and_modes_count(self):
        for path in ['.claude-plugin/plugin.json', '.codex-plugin/plugin.json',
                     '.agents/plugins/marketplace.json', '.github/plugin/plugin.json',
                     'LICENSE', 'provenance.json']:
            with self.subTest(path=path), repository():
                base = policy.git('rev-parse', 'HEAD')
                p = Path(path)
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('Changed distribution file')
                commit()
                with self.assertRaises(ValueError):
                    policy.check(base)
        for operation in ['delete', 'mode']:
            with self.subTest(operation=operation), repository():
                base = policy.git('rev-parse', 'HEAD')
                p = Path('skills/sample/SKILL.md')
                if operation == 'delete':
                    p.unlink()
                else:
                    p.chmod(0o755)
                commit()
                with self.assertRaises(ValueError):
                    policy.check(base)

    def test_numeric_progression_and_unchanged_version_notes(self):
        with repository():
            base = policy.git('rev-parse', 'HEAD')
            Path('VERSION').write_text('1.0.9')
            Path('CHANGELOG.md').write_text('## 1.0.9 — date\nNotes')
            commit()
            with self.assertRaisesRegex(ValueError, 'decrease'):
                policy.check(base)
        self.assertGreater(policy.version_tuple('1.10.0'), policy.version_tuple('1.9.9'))
        with repository():
            base = policy.git('rev-parse', 'HEAD')
            Path('CHANGELOG.md').write_text('## 1.1.1 — date\nDifferent notes')
            commit()
            with self.assertRaisesRegex(ValueError, 'notes changed'):
                policy.check(base)

    def test_event_baselines(self):
        self.assertEqual(policy.event_base({'pull_request': {'base': {'sha': 'abc'}}}, 'pull_request'), 'abc')
        self.assertEqual(policy.event_base({'before': 'abc'}, 'push'), 'abc')
        self.assertEqual(policy.event_base({}, 'workflow_dispatch'), 'HEAD^')
        with self.assertRaises(ValueError):
            policy.event_base({'before': '0' * 40}, 'push')
        with self.assertRaises(ValueError):
            policy.event_base({}, 'unexpected')


class ReleaseTests(unittest.TestCase):
    def test_existing_release_checks_actual_content_and_notes(self):
        with repository():
            sha = policy.git('rev-parse', 'HEAD')
            Path('README.md').write_text('Internal change')
            newer = commit()
            with patch.object(release, 'pages', side_effect=[[item()], [tag(sha)]]), patch.object(release, 'gh') as gh:
                release.publish('example/skills', newer, '1.1.1', 'Notes\n')
                gh.assert_not_called()
            Path('skills/sample/SKILL.md').write_text('Unversioned content')
            bad = commit()
            with patch.object(release, 'pages', side_effect=[[item()], [tag(sha)]]), self.assertRaises(ValueError):
                release.publish('example/skills', bad, '1.1.1', 'Notes\n')
            bad_notes = item()
            bad_notes['body'] = 'Unreviewed notes'
            with self.assertRaisesRegex(ValueError, 'notes'):
                release.verify_existing(bad_notes, sha, newer, '1.1.1', 'Notes\n')

    def test_missing_tag_draft_prerelease_and_unrelated_history_fail(self):
        with repository():
            sha = policy.git('rev-parse', 'HEAD')
            with self.assertRaises(ValueError):
                release.verify_existing(item(), None, sha, '1.1.1', 'Notes')
            for flag in ['draft', 'prerelease']:
                existing = item()
                existing[flag] = True
                with self.assertRaises(ValueError):
                    release.verify_existing(existing, sha, sha, '1.1.1', 'Notes')
            # Same bytes on unrelated history do not establish release identity.
            tree = policy.git('rev-parse', 'HEAD^{tree}')
            unrelated = policy.git('commit-tree', tree, '-m', 'Unrelated fixture')
            with self.assertRaises(subprocess.CalledProcessError):
                release.verify_existing(item(), unrelated, sha, '1.1.1', 'Notes')

    def test_new_release_and_partial_tag_recovery_verify_exact_commit(self):
        for existing_tag in [False, True]:
            with self.subTest(existing_tag=existing_tag), repository():
                sha = policy.git('rev-parse', 'HEAD')
                states = [[], [tag(sha)] if existing_tag else [], [item()], [tag(sha)]]
                def create(*args):
                    self.assertEqual(args[:3], ('release', 'create', 'v1.1.1'))
                    self.assertEqual(args[args.index('--target') + 1], sha)
                    self.assertEqual(Path(args[args.index('--notes-file') + 1]).read_text(), 'Notes\n')
                    self.assertIn('--latest=true', args)
                    return 'created'
                with patch.object(release, 'pages', side_effect=states), patch.object(release, 'gh', side_effect=create) as gh:
                    release.publish('example/skills', sha, '1.1.1', 'Notes\n')
                    gh.assert_called_once()

    def test_conflicting_tag_is_preserved(self):
        with repository():
            sha = policy.git('rev-parse', 'HEAD')
            with patch.object(release, 'pages', side_effect=[[], [tag('other')]]), patch.object(release, 'gh') as gh:
                with self.assertRaisesRegex(ValueError, 'another commit'):
                    release.publish('example/skills', sha, '1.1.1', 'Notes')
                gh.assert_not_called()

    def test_backfill_does_not_replace_newer_latest(self):
        with repository():
            sha = policy.git('rev-parse', 'HEAD')
            states = [[item('1.2.0')], [], [item('1.2.0'), item()], [tag(sha)]]
            with patch.object(release, 'pages', side_effect=states), patch.object(release, 'gh') as gh:
                release.publish('example/skills', sha, '1.1.1', 'Notes')
                self.assertIn('--latest=false', gh.call_args.args)

    def test_api_error_timeout_and_failed_postcondition_never_claim_success(self):
        with repository():
            sha = policy.git('rev-parse', 'HEAD')
            with patch.object(release, 'pages', side_effect=RuntimeError('API unavailable')), patch.object(release, 'gh') as gh:
                with self.assertRaises(RuntimeError):
                    release.publish('example/skills', sha, '1.1.1', 'Notes')
                gh.assert_not_called()
            with patch.object(release, 'pages', side_effect=[[], []]), patch.object(release, 'gh', side_effect=TimeoutError):
                with self.assertRaises(TimeoutError):
                    release.publish('example/skills', sha, '1.1.1', 'Notes')
            with patch.object(release, 'pages', side_effect=[[], [], [item()], [tag('wrong')]]), patch.object(release, 'gh'):
                with self.assertRaisesRegex(ValueError, 'not verified'):
                    release.publish('example/skills', sha, '1.1.1', 'Notes')

    def test_missing_versions_detected_since_automation_start(self):
        with repository():
            first = policy.git('rev-parse', 'HEAD')
            Path('VERSION').write_text('1.1.2')
            second = commit()
            Path('VERSION').write_text('1.2.0')
            third = commit()
            self.assertEqual(release.missing_versions(third, []), [('1.1.1', first), ('1.1.2', second)])
            self.assertEqual(release.missing_versions(third, [item(), item('1.1.2')]), [])

    def test_untrusted_events_and_checkout_mismatch_never_publish(self):
        cases = [('refs/pull/1/merge', 'pull_request'), ('refs/heads/main', 'pull_request'),
                 ('refs/heads/main', 'push')]
        with repository():
            for ref, event in cases:
                with self.subTest(ref=ref, event=event), patch.dict(os.environ, {
                    'GITHUB_REF': ref, 'GITHUB_EVENT_NAME': event, 'GITHUB_SHA': 'wrong'
                }), patch.object(release, 'publish') as publish:
                    with self.assertRaises(ValueError):
                        release.main()
                    publish.assert_not_called()


if __name__ == '__main__':
    unittest.main()
