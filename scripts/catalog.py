"""Generate the three native manifests from one collection version (stdlib only)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = "https://github.com/krema/agent-skills"
DESCRIPTION = "Krema's growing collection of reusable skills for Claude Code, Codex, and GitHub Copilot."


def manifests(root=ROOT):
    version = (root / "VERSION").read_text().strip()
    plugin = dict(name="skills", version=version, description=DESCRIPTION,
                  author={"name": "krema", "url": "https://github.com/krema"},
                  homepage=URL, repository=URL, license="MIT")
    marketplace = dict(name="krema", owner={"name": "krema"},
                       metadata={"description": DESCRIPTION, "version": version},
                       plugins=[dict(name="skills", source="./", description=DESCRIPTION, version=version)])
    codex_plugin = dict(plugin, skills="./skills/", interface={
        "displayName": "Krema Skills", "shortDescription": "Reusable skills for everyday agent work.",
        "category": "Productivity"})
    codex_marketplace = dict(name="krema", interface={"displayName": "Krema"}, plugins=[{
        "name": "skills", "source": {"source": "local", "path": "./"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity"}])
    return {".claude-plugin/plugin.json": plugin,
            ".claude-plugin/marketplace.json": marketplace,
            ".github/plugin/plugin.json": dict(plugin, skills="./skills/"),
            ".github/plugin/marketplace.json": marketplace,
            ".codex-plugin/plugin.json": codex_plugin,
            ".agents/plugins/marketplace.json": codex_marketplace}


def write(root=ROOT):
    for name, data in manifests(root).items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + "\n")


if __name__ == "__main__":
    write()
