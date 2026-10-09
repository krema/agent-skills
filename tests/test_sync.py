import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from sync_skills import sync


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.source = base / "source"
        self.source.mkdir()
        self.repo = base / "repo"
        self.repo.mkdir()
        self.original = "---\nname: original\ndescription: Example skill.\n---\n# Original\nUse original.\n"
        (self.source / "SKILL.md").write_text(self.original)
        self.config = {"public-name": {"source_name": "original", "title": "Public Name", "path": str(self.source)}}

    def test_rename_idempotency_and_source_preservation(self):
        self.assertEqual(["public-name"], sync(self.config, self.repo, write=True))
        self.assertEqual([], sync(self.config, self.repo, write=True))
        self.assertEqual(self.original, (self.source / "SKILL.md").read_text())
        self.assertIn("name: public-name", (self.repo / "skills/public-name/SKILL.md").read_text())
        self.assertNotIn(str(self.source), (self.repo / "provenance.json").read_text())

    def test_preserves_independent_edits(self):
        sync(self.config, self.repo, write=True)
        published = self.repo / "skills/public-name/SKILL.md"
        published.write_text("User edit")
        with self.assertRaisesRegex(ValueError, "edited independently"):
            sync(self.config, self.repo, write=True)
        self.assertEqual("User edit", published.read_text())

    def test_rejects_symlinks_and_private_paths(self):
        link = self.source / "leak.md"
        link.symlink_to(self.source / "SKILL.md")
        with self.assertRaisesRegex(ValueError, "symlink"):
            sync(self.config, self.repo, write=True)
        link.unlink()
        link.write_text("Private path: /Users/someone/work")
        with self.assertRaisesRegex(ValueError, "private path"):
            sync(self.config, self.repo, write=True)
        self.assertFalse((self.repo / "skills").exists())

    def test_does_not_remove_omitted_skills(self):
        sync(self.config, self.repo, write=True)
        with self.assertRaisesRegex(ValueError, "omits"):
            sync({}, self.repo, write=True)

    def test_skips_unfinished_sources(self):
        sync(self.config, self.repo, write=True)
        self.config['unfinished'] = {'path': '/nonexistent', 'source_name': 'unfinished', 'title': 'Unfinished'}
        (self.source / 'SKILL.md').write_text(self.original + 'Completed update.\n')
        self.assertEqual(['public-name'], sync(self.config, self.repo, write=True, only=['public-name']))
        self.assertNotIn('unfinished', json.loads((self.repo / 'provenance.json').read_text()))

    def test_removes_stale_files_and_dry_run_does_not_write(self):
        extra = self.source / "obsolete.md"
        extra.write_text("Old guidance")
        sync(self.config, self.repo, write=True)
        extra.unlink()
        self.assertEqual(["public-name"], sync(self.config, self.repo))
        published = self.repo / "skills/public-name/obsolete.md"
        self.assertTrue(published.exists())
        sync(self.config, self.repo, write=True)
        self.assertFalse(published.exists())


if __name__ == "__main__":
    unittest.main()
