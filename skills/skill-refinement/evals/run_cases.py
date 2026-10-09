#!/usr/bin/env python3
"""Materialize local fixtures and verify static expectations, not model behavior."""
import argparse
import importlib.util
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('analyze_skill', ROOT / 'scripts/analyze_skill.py')
analyzer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(analyzer)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare', type=Path, help='Write fresh behavioral input workspaces (no rubrics); destination must not exist')
    args = parser.parse_args()
    cases = json.loads((ROOT / 'evals/cases.json').read_text(encoding='utf-8'))
    if args.prepare:
        destination = args.prepare.absolute()
        destination.mkdir(parents=True, exist_ok=False)
        for case in cases:
            folder = destination / case['id']
            folder.mkdir()
            (folder / 'REQUEST.txt').write_text(case['user_request'], encoding='utf-8')
            for name, content in case['files'].items():
                path = folder / name
                if not path.resolve().is_relative_to(folder.resolve()):
                    raise ValueError('Fixture path escapes case directory')
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding='utf-8')
        print(f'Prepared {len(cases)} input cases at {destination}; no model evaluations executed.')
        return 0
    failures = []
    ids = set()
    for case in cases:
        assert case['id'] not in ids, 'Duplicate case ID'
        ids.add(case['id'])
        assert case['user_request'] and case['rubric'], 'Missing behavioral specification'
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            for name, content in case['files'].items():
                path = root / name
                if not path.resolve().is_relative_to(root):
                    raise ValueError('Fixture path escapes temporary root')
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding='utf-8')
            report = analyzer.analyze(root)
            assert report['content_review']['status'] == 'required', 'Content review must never be skipped'
            codes = {item['code'] for item in report['findings']}
            missing = set(case['expected_codes']) - codes
            forbidden = set(case['forbidden_codes']) & codes
            errors = {f['code'] for f in report['findings'] if f['severity'] == 'error'}
            unexpected_errors = errors - set(case['expected_codes'])
            if missing or forbidden or unexpected_errors:
                failures.append(case['id'])
                print(f"FAIL {case['id']}: missing={sorted(missing)} forbidden={sorted(forbidden)} errors={sorted(unexpected_errors)}")
            else:
                print(f"PASS {case['id']} (static expectations only)")
    print(f'{len(cases) - len(failures)}/{len(cases)} static fixture cases passed; model rubric not executed.')
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
