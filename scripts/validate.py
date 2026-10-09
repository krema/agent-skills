"""Check distribution metadata, source integrity, and links without extra packages."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from catalog import ROOT, manifests
from sync_skills import snapshot, digest


def validate(root=ROOT):
    version = (root / "VERSION").read_text().strip()
    assert re.fullmatch(r"\d+\.\d+\.\d+", version), "Expected semantic version"
    for name, expected in manifests(root).items():
        assert json.loads((root / name).read_text()) == expected, f"Stale manifest: {name}"
    registry = json.loads((root / "provenance.json").read_text())
    actual = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    assert actual == set(registry), "Skill inventory differs from provenance"
    for public, record in registry.items():
        files = snapshot(root / "skills" / public)
        assert {name: digest(data) for name, data in files.items()} == record["published_sha256"], public
        entry = files["SKILL.md"].decode()
        assert entry.startswith("---\n"), public
        header = entry.split("---", 2)[1]
        assert f"name: {public}\n" in header, public
        assert re.search(r"(?m)^description: .+", header), public
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        # Ignore fenced examples: their deliberately broken links are test inputs.
        content = re.sub(r"(?ms)^```.*?^```[^\n]*$", "", path.read_text())
        for match in re.finditer(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
            href = match.group(1).split(' "', 1)[0].strip("<>")
            if urlsplit(href).scheme or href.startswith("#"):
                continue
            link = unquote(href.split("#", 1)[0])
            assert (path.parent / link).exists(), f"Broken link in {path.relative_to(root)}: {link}"
    print(f"Validated {len(registry)} skills, six native manifests, provenance hashes, and Markdown links (v{version}).")


if __name__ == "__main__":
    validate()
