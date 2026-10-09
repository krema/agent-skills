from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_publication import check, scan_file


class PublicationTests(unittest.TestCase):
    def test_public_identity_and_synthetic_examples_are_allowed(self):
        self.assertEqual([], scan_file("README.md", b"krema <gestro@krema.dev> https://github.com/krema"))
        self.assertEqual([], scan_file("tests/test_sync.py", b"/Users/" + b"someone/work"))
        self.assertTrue(scan_file("README.md", b"/Users/" + b"someone/work"))

    def test_private_paths_and_links(self):
        for value in [b"/Users/" + b"person/work", b"/home/" + b"person/work",
                      b"C:\\Users\\person\\work", b"https://chatgpt.com/" + b"c/private-session"]:
            with self.subTest(value=value):
                self.assertTrue(scan_file("example.md", value))

    def test_credentials_are_detected_without_disclosure(self):
        for value in [b"ghp_" + b"a" * 36, b"github_pat_" + b"a" * 40,
                      b"-----BEGIN " + b"RSA PRIVATE KEY-----"]:
            findings = scan_file("example.md", value)
            self.assertTrue(findings)
            self.assertNotIn(value.decode(), str(findings))

    def test_private_artifacts_and_nontext(self):
        for name in [".env", "keys/private.pem", "sources.local.json",
                     ".agent-learnings/observations.jsonl", "recovery.bundle"]:
            self.assertTrue(scan_file(name, b"data"))
        self.assertEqual([], scan_file(".env.example", b"EXAMPLE=placeholder"))
        self.assertTrue(scan_file("unknown.bin", b"\xff\x00"))

    def test_tracked_files_and_symlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q", tmp], check=True)
            (root / "safe.md").write_text("Public material")
            (root / "untracked.md").write_text("/home/" + "person/private")
            subprocess.run(["git", "add", "safe.md"], cwd=root, check=True)
            self.assertEqual([], check(root))
            (root / "link.md").symlink_to("untracked.md")
            subprocess.run(["git", "add", "link.md"], cwd=root, check=True)
            self.assertEqual(1, len(check(root)))
            (root / "safe.md").write_text("/home/" + "person/private")
            self.assertEqual(2, len(check(root)))


if __name__ == "__main__":
    unittest.main()
