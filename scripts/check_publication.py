"""Scan tracked publication files without printing potentially sensitive values."""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "personal filesystem path": re.compile(
        r"/(?:Users|home)/[\w.-]+/[^\s\"'<>|)]+|[A-Za-z]:\\Users\\[^\s\"'<>]+"
    ),
    "private conversation link": re.compile(
        r"https?://(?:chatgpt\.com|chat\.openai\.com)/c/[^\s)]+|codex:" r"//threads/[^\s)]+"
    ),
    "private key": re.compile(r"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----"),
    "credential pattern": re.compile(
        r"\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b|"
        r"\bAKIA[A-Z0-9]{16}\b|\bxox[baprs]-[A-Za-z0-9-]{15,}\b|"
        r"\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{32,}\b"
    ),
}


def scan_file(relative, data):
    """Return only file, line and category; never include source text."""
    path = Path(relative)
    findings = []
    if (any(part in {".agent-learnings", ".local", "privacy-audit"} for part in path.parts)
            or path.name.endswith(".local.json")
            or ((path.name == ".env" or path.name.startswith(".env.")) and path.name not in {".env.example", ".env.template"})
            or path.suffix.lower() in {".pem", ".key", ".p12", ".pfx", ".bundle"}):
        findings.append((relative, 0, "private artifact filename"))
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return findings + [(relative, 0, "binary file requires explicit publication review")]
    for number, line in enumerate(text.splitlines(), 1):
        for category, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                # The importer's synthetic rejection fixture is intentional.
                if (relative == "tests/test_sync.py"
                        and category == "personal filesystem path"
                        and match.group() == "/Users/" + "someone/work"):
                    continue
                findings.append((relative, number, category))
    return findings


def check(root=ROOT):
    paths = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=root
    ).decode().split("\0")
    findings = []
    for name in filter(None, paths):
        path = root / name
        if path.is_symlink():
            findings.append((name, 0, "symlink requires explicit publication review"))
        elif path.is_file():
            findings.extend(scan_file(name, path.read_bytes()))
        else:
            findings.append((name, 0, "tracked file is missing or unsupported"))
    return findings


if __name__ == "__main__":
    results = check()
    for name, line, category in results:
        print(f"{name}:{line}: {category}")
    print(f"Publication check: {len(results)} finding(s).")
    sys.exit(bool(results))
