#!/usr/bin/env python3
"""Read-only structural checks. Content review is required at every size; Python 3.10+.

Not a YAML/CommonMark validator, semantic rule counter, or runtime profiler.
"""
import argparse
from collections import defaultdict
import json
import math
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

MAX_BYTES = 2_000_000
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}
LINK = re.compile(r'\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+"[^"\n]*")?\s*\)')
DEFINITION = re.compile(r'^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)')
PRELOAD = re.compile(r'\b(read|load|open)\s+(all|every)\s+(?:the\s+)?(?:reference|file|document)', re.I)
NEGATION = re.compile(r"\b(do not|don't|never|avoid|not to)\b", re.I)


def estimate(text):
    return math.ceil(len(text) / 4)


def prose_lines(text):
    """Exclude initial frontmatter and fenced blocks, retaining source line numbers."""
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() in {"---", "..."}:
                start = i + 1
                break
    fence = None
    for n, line in enumerate(lines[start:], start + 1):
        match = re.match(r'^\s*(`{3,}|~{3,})(.*)$', line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not match[2].strip():
                fence = None
            continue
        if fence is None:
            yield n, line


def read_text(path):
    if path.stat().st_size > MAX_BYTES:
        raise ValueError(f"file exceeds {MAX_BYTES} byte inspection limit")
    return path.read_text(encoding="utf-8-sig")


def safe_target(root, source, target):
    """Resolve local links without allowing reads outside package or through symlinks."""
    split = urlsplit(target.strip("<>"))
    if split.scheme or split.netloc or not split.path:
        return None
    candidate = source.parent / unquote(split.path)
    resolved = candidate.resolve()
    if not resolved.is_relative_to(root):
        raise ValueError("target is outside package root")
    # Check lexical ancestors too: a symlink may resolve back inside the root.
    if any(part.is_symlink() for part in [candidate, *candidate.parents]):
        raise ValueError("symlink target is not inspected")
    return resolved


def inventory(root, entry, directory_mode):
    if not directory_mode:
        return [entry]
    paths = []
    for base, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')
                         and not (Path(base) / d).is_symlink())
        for name in sorted(files):
            path = Path(base) / name
            if path.suffix.lower() == '.md' and not path.is_symlink():
                paths.append(path)
    return sorted(paths)


def analyze(target, loaded=(), include_metrics=False):
    raw = Path(target).expanduser().absolute()
    if any(p.is_symlink() for p in [raw, *raw.parents]):
        raise ValueError("target or ancestor is a symlink; use its real path")
    directory_mode = raw.is_dir()
    entry = raw / 'SKILL.md' if directory_mode else raw
    if not entry.is_file() or entry.is_symlink():
        raise ValueError("target must be a readable instruction file or directory containing SKILL.md")
    root = entry.parent.resolve()
    entry = entry.resolve()
    findings, contents, metrics, graph, routes = [], {}, {}, defaultdict(set), []

    def add(code, severity, path, line, message):
        findings.append(dict(code=code, severity=severity, file=str(path.relative_to(root)),
                             line=line, message=message))

    for path in inventory(root, entry, directory_mode):
        try:
            text = read_text(path)
        except (OSError, UnicodeError, ValueError) as exc:
            add('unreadable', 'error', path, None, str(exc))
            continue
        contents[path] = text
        prose = [(n, line) for n, line in prose_lines(text) if line.strip()]
        metrics[str(path.relative_to(root))] = dict(
            lines=len(text.splitlines()), characters=len(text), estimated_tokens=estimate(text),
            prose_lines=len(prose))
        for n, line in prose:
            targets = [m[1] for m in LINK.finditer(line)]
            definition = DEFINITION.match(line)
            if definition:
                targets.append(definition[1])
            for link in targets:
                try:
                    dest = safe_target(root, path, link)
                except ValueError as exc:
                    add('external_local_link', 'review', path, n, f'{link}: {exc}')
                    continue
                if dest is None:
                    continue
                if not dest.exists():
                    add('missing_link', 'error', path, n, f'Missing local target: {link}')
                else:
                    graph[path].add(dest)
                    if path == entry:
                        routes.append(dict(target=str(dest.relative_to(root)), line=n,
                                           text=line.strip()))
            if path == entry and PRELOAD.search(line) and not NEGATION.search(line):
                add('possible_preload', 'review', path, n,
                    'Possible unconditional loading; inspect wording and observed reads.')

    entry_text = contents.get(entry, '')
    front = re.match(r'\A---[ \t]*\n(.*?)\n(?:---|\.\.\.)[ \t]*(?:\n|\Z)', entry_text, re.S)
    if entry.name == 'SKILL.md':
        if not front:
            add('frontmatter', 'error', entry, 1, 'Missing or unclosed YAML frontmatter.')
        else:
            for key in ('name', 'description'):
                # Presence only: full YAML syntax and semantic validation belongs to skills-ref.
                field = re.search(rf'^{key}:[ \t]*(\S[^\n]*)', front[1], re.M)
                if not field or field[1].strip() in {"''", '""'}:
                    add('frontmatter', 'error', entry, 1, f'Missing/nonempty {key} field required.')
    # Only the entrypoint and references are instruction-duplicate candidates.
    repeats = defaultdict(list)
    for path, text in contents.items():
        if path != entry and 'references' not in path.relative_to(root).parts:
            continue
        for n, line in prose_lines(text):
            normalized = re.sub(r'\s+', ' ', line.strip()).casefold()
            if normalized and not normalized.startswith(('#', '|', '>')):
                repeats[normalized].append((path, n))
    for places in repeats.values():
        if len(places) > 1:
            path, n = places[0]
            where = ', '.join(f'{p.relative_to(root)}:{i}' for p, i in places)
            add('duplicate_prose', 'review', path, n, f'Exact repeated prose; assess function before editing: {where}')

    # Reachability is structural; it deliberately does not claim conditional execution.
    seen, stack = set(), [entry]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(graph[node] - seen)
    if directory_mode:
        for path in contents:
            if 'references' in path.relative_to(root).parts and path not in seen:
                add('unlinked_reference', 'review', path, None,
                    'No detected Markdown-link path from entrypoint; check other callers.')

    selected = {entry}
    for name in loaded:
        dest = safe_target(root, entry, name)
        if dest is None or not dest.is_file():
            raise ValueError(f'--loaded must name an existing local file: {name}')
        if dest not in contents:
            contents[dest] = read_text(dest)
        selected.add(dest)
    front_text = front[0] if front else ''
    body_text = entry_text[len(front_text):]
    report = dict(schema_version=2, entrypoint=entry.name,
                  files=sorted(metrics),
                  content_review=dict(status='required', files=sorted(metrics),
                                      reason='Every requested document needs semantic review, regardless of size or static findings.'),
                  routes=routes, findings=findings,
                  limitations=['No semantic relevance, obligation count, content quality, or success score.',
                               'Markdown subset only; inline and reference-definition file links outside fences.',
                               'Fragments, external URLs, plain paths, HTML links, and complex nested destinations are not validated.',
                               'Frontmatter field presence only; use an actual YAML/spec validator.',
                               'Symlinks and excluded directories are not traversed; files over 2 MB are inspection errors.'])
    if include_metrics:
        report.update(
            measurement='Static Unicode characters / 4 rounded up; not actual tokens or runtime load.',
            core=metrics.get(entry.name, {}), file_metrics=metrics,
            entrypoint_parts=dict(frontmatter_characters=len(front_text),
                                  frontmatter_estimated_tokens=estimate(front_text),
                                  body_characters=len(body_text), body_estimated_tokens=estimate(body_text),
                                  note='Frontmatter measurement, not the host-rendered discovery listing.'),
            scenario_files=sorted(str(p.relative_to(root)) for p in selected),
            scenario_estimated_tokens=sum(estimate(contents.get(p, '')) for p in selected))
    return report



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', help='Skill directory or standalone instruction file')
    parser.add_argument('--loaded', action='append', default=[], metavar='RELATIVE_FILE',
                        help='Add a file to the estimated load scenario; repeatable, deduplicated')
    parser.add_argument('--json', action='store_true', help='Emit machine-readable JSON')
    parser.add_argument('--strict', action='store_true', help='Exit 1 for structural errors, never review signals')
    parser.add_argument('--metrics', action='store_true', help='Include optional size and hypothetical load measurements; never a quality verdict')
    args = parser.parse_args()
    try:
        report = analyze(args.target, args.loaded, args.metrics)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f'error: {exc}\n')
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Structural inspection: {len(report['files'])} Markdown file(s).")
        print('Content review REQUIRED for every requested document; no size gate or quality verdict.')
        if args.metrics:
            print(f"Optional measurements: {report['core'].get('lines', 0)} entrypoint lines; ~{report['core'].get('estimated_tokens', 0)} tokens")
            print(f"Scenario: ~{report['scenario_estimated_tokens']} tokens ({', '.join(report['scenario_files'])})")
            print(report['measurement'])
        for item in report['findings']:
            print(f"{item['severity']}: {item['code']} {item['file']}:{item['line'] or '-'} — {item['message']}")
        if not report['findings']:
            print('No static findings; semantic and behavioral review still required.')
    return int(args.strict and any(f['severity'] == 'error' for f in report['findings']))


if __name__ == '__main__':
    sys.exit(main())
