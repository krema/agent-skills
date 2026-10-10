import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('release', Path(__file__).parents[1] / 'scripts/release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def test_notes_select_only_exact_version(self):
        text = '# Changelog\n\n## 1.1.10 — date\nWrong\n## 1.1.1 — date\n\n- Correct\n\n## 1.0.0 — date\nOld\n'
        self.assertEqual(release.release_notes('1.1.1', text), '- Correct\n')

    def test_invalid_or_missing_notes_fail(self):
        for version, text in [('01.1.0', ''), ('1.0.0', ''), ('1.0.0', '## 1.0.0 — date\n')]:
            with self.assertRaises(ValueError):
                release.release_notes(version, text)

    @patch.object(release, 'gh')
    @patch.object(release, 'pages')
    def test_published_version_is_noop(self, pages, gh):
        pages.return_value = [{'tag_name': 'v1.1.1', 'draft': False, 'prerelease': False}]
        release.publish('example/skills', 'abc', '1.1.1', 'Notes')
        gh.assert_not_called()

    @patch.object(release, 'gh')
    @patch.object(release, 'pages')
    def test_conflicting_tag_is_preserved(self, pages, gh):
        pages.side_effect = [[], [{'name': 'v1.1.1', 'commit': {'sha': 'other'}}]]
        with self.assertRaises(ValueError):
            release.publish('example/skills', 'abc', '1.1.1', 'Notes')
        gh.assert_not_called()

    @patch.object(release, 'gh')
    @patch.object(release, 'pages', return_value=[])
    def test_new_release_uses_exact_commit_and_notes(self, pages, gh):
        def inspect(*args):
            self.assertEqual(args[:3], ('release', 'create', 'v1.1.1'))
            self.assertEqual(args[args.index('--target') + 1], 'abc')
            self.assertEqual(Path(args[args.index('--notes-file') + 1]).read_text(), 'Notes\n')
            return 'created'
        gh.side_effect = inspect
        release.publish('example/skills', 'abc', '1.1.1', 'Notes\n')
        gh.assert_called_once()

    @patch.object(release, 'gh')
    @patch.object(release, 'pages')
    def test_existing_draft_is_not_published(self, pages, gh):
        pages.return_value = [{'tag_name': 'v1.1.1', 'draft': True, 'prerelease': False}]
        with self.assertRaises(ValueError):
            release.publish('example/skills', 'abc', '1.1.1', 'Notes')
        gh.assert_not_called()
