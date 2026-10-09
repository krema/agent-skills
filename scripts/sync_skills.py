"""Import explicitly selected, validated local packages. Never contacts GitHub.

The source map contains private paths and must stay outside the repository.
Usage: python3 scripts/sync_skills.py /outside/repo/sources.local.json [--write]
Without --write, report which published packages would change.
"""
import argparse
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {"__pycache__", ".DS_Store"}
SUFFIXES = {".md", ".py", ".json", ".txt", ".yaml", ".yml", ".toml"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def snapshot(source):
    source = Path(source)
    if source.is_symlink() or not source.is_dir():
        raise ValueError(f"Expected a real package directory: {source}")
    files = {}
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        if any(part in IGNORED for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Refusing symlink: {path}")
        if path.is_dir():
            continue
        if path.suffix not in SUFFIXES:
            raise ValueError(f"Review unsupported publication file: {path}")
        files[relative.as_posix()] = path.read_bytes()
    if "SKILL.md" not in files:
        raise ValueError(f"Missing SKILL.md: {source}")
    return files


def prepare(public, entry):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", public):
        raise ValueError(f"Invalid public name: {public}")
    original = snapshot(entry["path"])
    old = entry["source_name"]
    if not re.search(rf"(?m)^name: {re.escape(old)}$", original["SKILL.md"].decode()):
        raise ValueError(f"Unexpected source skill name for {public}")
    exported = {}
    for name, data in original.items():
        # Update self-references along with the entrypoint. Sources stay untouched.
        value = data.decode("utf-8").replace(old, public)
        if name == "SKILL.md":
            value = re.sub(r"(?m)^# .+$", "# " + entry["title"], value, count=1)
        if re.search(r"/Users/|/home/|/private/|file://|-----BEGIN .*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16}", value):
            raise ValueError(f"Review private path or credential-like content: {public}/{name}")
        exported[name] = value.encode("utf-8")
    if snapshot(entry["path"]) != original:
        raise ValueError(f"Package changed while reading: {public}")
    provenance = {"source_name": old, "title": entry["title"],
                  "transformation": "Public identifier replacement and entrypoint heading; no rule changes.",
                  "source_sha256": {name: digest(data) for name, data in original.items()},
                  "published_sha256": {name: digest(data) for name, data in exported.items()}}
    return exported, provenance


def sync(config, root=ROOT, write=False, only=None):
    registry_path = root / "provenance.json"
    previous = json.loads(registry_path.read_text()) if registry_path.exists() else {}
    # An omitted mapping must not silently remove a published package.
    if set(previous) - set(config):
        raise ValueError("Source map omits published skills; resolve removals explicitly.")
    for public, record in previous.items():
        current = snapshot(root / "skills" / public)
        if {name: digest(data) for name, data in current.items()} != record["published_sha256"]:
            raise ValueError(f"Published files were edited independently: {public}. Reconcile before syncing.")
    selected = set(config) if only is None else set(only)
    if selected - set(config):
        raise ValueError("Selected skill is missing from the source map.")
    prepared = {public: prepare(public, entry) for public, entry in sorted(config.items()) if public in selected}
    changed = [name for name, (_, record) in prepared.items() if previous.get(name) != record]
    if not write or not changed:
        return changed
    # Finish all source reads and guards before touching the published tree.
    with tempfile.TemporaryDirectory() as temp:
        staging = Path(temp)
        for public, (files, _) in prepared.items():
            for name, data in files.items():
                target = staging / public / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
        (root / "skills").mkdir(exist_ok=True)
        for public in changed:
            target = root / "skills" / public
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(staging / public, target)
        updated = dict(previous)
        updated.update({name: record for name, (_, record) in prepared.items()})
        registry_path.write_text(json.dumps(updated, indent=2, sort_keys=True) + "\n")
    return changed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_map", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--only", nargs="+", help="Import only these completed skills; preserve the others.")
    args = parser.parse_args()
    try:
        if args.source_map.resolve().is_relative_to(ROOT):
            raise ValueError("Keep the private source map outside this repository.")
        changed = sync(json.loads(args.source_map.read_text()), write=args.write, only=args.only)
        print(json.dumps({"changed": changed, "written": args.write and bool(changed)}, indent=2))
    except (ValueError, OSError) as error:
        parser.exit(1, f"Sync stopped: {error}\n")
