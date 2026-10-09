"""Deterministic tooling tests, not an LLM efficacy benchmark."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'analyze_skill.py'
SPEC = importlib.util.spec_from_file_location('analyze_skill', SCRIPT)
analyzer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(analyzer)
HEADER = '---\nname: demo\ndescription: Inspect demo files.\n---\n'


class AnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.write('SKILL.md', HEADER + '# Demo\nUse the requested mode.\n')

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def codes(self, report):
        return {f['code'] for f in report['findings']}

    def cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), str(self.root), *args],
                              text=True, capture_output=True)

    def test_clean_skill(self):
        report = analyzer.analyze(self.root, include_metrics=True)
        self.assertEqual([], report['findings'])
        self.assertEqual(['SKILL.md'], report['scenario_files'])

    def test_frontmatter_body_partition(self):
        self.write('references/other.md', 'Other content must not contaminate the entrypoint metric.\n' * 10)
        report = analyzer.analyze(self.root, include_metrics=True)
        parts = report['entrypoint_parts']
        self.assertEqual(report['core']['characters'], parts['frontmatter_characters'] + parts['body_characters'])
        self.assertGreater(parts['frontmatter_estimated_tokens'], 0)
        self.assertGreater(parts['body_estimated_tokens'], 0)

    def test_no_reference_preloading_from_links(self):
        self.write('SKILL.md', HEADER + 'If repair fails, read [repair](references/repair.md).\n')
        self.write('references/repair.md', 'Recovery detail.\n' * 100)
        report = analyzer.analyze(self.root, include_metrics=True)
        self.assertEqual(report['core']['estimated_tokens'], report['scenario_estimated_tokens'])
        loaded = analyzer.analyze(self.root, ['references/repair.md', 'references/repair.md'], include_metrics=True)
        self.assertEqual(2, len(loaded['scenario_files']))
        self.assertGreater(loaded['scenario_estimated_tokens'], report['scenario_estimated_tokens'])

    def test_missing_link_is_structural_error(self):
        self.write('SKILL.md', HEADER + '[missing](references/missing.md)\n')
        report = analyzer.analyze(self.root, include_metrics=True)
        self.assertIn('missing_link', self.codes(report))
        self.assertEqual(1, self.cli('--strict').returncode)
        self.assertEqual(0, self.cli().returncode)

    def test_size_alone_does_not_fail(self):
        self.write('SKILL.md', HEADER + '\n'.join(f'Step {i} handles case {i}.' for i in range(501)))
        self.assertNotIn('size_review', self.codes(analyzer.analyze(self.root, include_metrics=True)))
        self.assertEqual(0, self.cli('--strict').returncode)

    def test_duplicate_prose_detected(self):
        sentence = 'Preserve the original identifiers during every import to prevent unrelated records from being merged.\n'
        self.write('SKILL.md', HEADER + sentence + sentence)
        self.assertIn('duplicate_prose', self.codes(analyzer.analyze(self.root, include_metrics=True)))

    def test_code_examples_do_not_become_findings(self):
        self.write('SKILL.md', HEADER + '```md\nRead all references before starting.\n[missing](bad.md)\n```\n')
        self.assertFalse(analyzer.analyze(self.root, include_metrics=True)['findings'])

    def test_preload_and_negation(self):
        self.write('SKILL.md', HEADER + 'Read all references before starting.\n')
        self.assertIn('possible_preload', self.codes(analyzer.analyze(self.root, include_metrics=True)))
        self.write('SKILL.md', HEADER + 'Do not read all references before starting.\n')
        self.assertNotIn('possible_preload', self.codes(analyzer.analyze(self.root, include_metrics=True)))

    def test_orphan_reference(self):
        self.write('references/orphan.md', 'Local knowledge.\n')
        self.assertIn('unlinked_reference', self.codes(analyzer.analyze(self.root, include_metrics=True)))

    def test_reference_cycles_terminate(self):
        self.write('SKILL.md', HEADER + '[a](references/a.md)\n')
        self.write('references/a.md', '[b](b.md)\n')
        self.write('references/b.md', '[a](a.md)\n')
        self.assertNotIn('unlinked_reference', self.codes(analyzer.analyze(self.root, include_metrics=True)))

    def test_external_and_anchor_links_not_missing_files(self):
        self.write('SKILL.md', HEADER + '[web](https://example.invalid/a) [mail](mailto:x@example.invalid) [part](#part)\n')
        self.assertFalse(analyzer.analyze(self.root, include_metrics=True)['findings'])

    def test_escaping_link_not_read(self):
        self.write('SKILL.md', HEADER + '[outside](../outside.md)\n')
        report = analyzer.analyze(self.root, include_metrics=True)
        self.assertIn('external_local_link', self.codes(report))
        with self.assertRaises(ValueError):
            analyzer.analyze(self.root, ['../outside.md'])

    def test_symlink_not_read(self):
        self.write('references/actual.md', 'Private reference.\n')
        (self.root / 'link.md').symlink_to(self.root / 'references/actual.md')
        self.write('SKILL.md', HEADER + '[linked](link.md)\n')
        self.assertIn('external_local_link', self.codes(analyzer.analyze(self.root, include_metrics=True)))
        with self.assertRaises(ValueError):
            analyzer.analyze(self.root, ['link.md'])

    def test_unicode_and_crlf(self):
        self.write('SKILL.md', (HEADER + 'Für Reparaturen: Größen prüfen. 日本語の説明。\n').replace('\n', '\r\n'))
        report = analyzer.analyze(self.root, include_metrics=True)
        self.assertGreater(report['core']['characters'], 0)
        self.assertFalse(report['findings'])

    def test_standalone_does_not_inventory_siblings(self):
        target = self.write('AGENTS.md', 'Use the local build command.\n')
        self.write('references/broken.md', '[bad](missing.md)\n')
        report = analyzer.analyze(target)
        self.assertEqual(['AGENTS.md'], list(report['files']))
        self.assertFalse(report['findings'])

    def test_spaces_encoded_paths_and_reference_definitions(self):
        self.write('SKILL.md', HEADER + '[guide](<references/a b.md>)\n[also](references/a%20b.md)\n[ref]: references/a%20b.md\n')
        self.write('references/a b.md', 'Details.\n')
        self.assertFalse(analyzer.analyze(self.root, include_metrics=True)['findings'])

    def test_unreadable_utf8_is_error(self):
        path = self.root / 'broken.md'
        path.write_bytes(b'\xff\xfe\xfa')
        self.assertIn('unreadable', self.codes(analyzer.analyze(self.root, include_metrics=True)))

    def test_missing_target_exit_two(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.root / 'absent')], capture_output=True)
        self.assertEqual(2, result.returncode)

    def test_json_output_and_no_mutation(self):
        before = {p.name: p.read_bytes() for p in self.root.iterdir() if p.is_file()}
        result = self.cli('--json', '--strict')
        self.assertEqual(0, result.returncode)
        self.assertEqual(2, json.loads(result.stdout)['schema_version'])
        after = {p.name: p.read_bytes() for p in self.root.iterdir() if p.is_file()}
        self.assertEqual(before, after)

    def test_frontmatter_missing_and_empty_fields(self):
        for content in ('# No frontmatter\n', '---\nname:\ndescription: demo\n---\n',
                        '---\nname: demo\ndescription: ""\n---\n'):
            with self.subTest(content=content):
                self.write('SKILL.md', content)
                self.assertIn('frontmatter', self.codes(analyzer.analyze(self.root, include_metrics=True)))

    def test_multiline_description_presence(self):
        self.write('SKILL.md', '---\nname: demo\ndescription: >-\n  Audit the demo.\n---\nDo the task.\n')
        self.assertNotIn('frontmatter', self.codes(analyzer.analyze(self.root, include_metrics=True)))

    def test_oversized_file_error(self):
        self.write('big.md', 'a' * (analyzer.MAX_BYTES + 1))
        self.assertIn('unreadable', self.codes(analyzer.analyze(self.root, include_metrics=True)))

    def test_explicit_script_output_scenario(self):
        self.write('sample-output.txt', 'Result: valid\n')
        report = analyzer.analyze(self.root, ['sample-output.txt'], include_metrics=True)
        self.assertEqual(['SKILL.md', 'sample-output.txt'], report['scenario_files'])

    def test_metrics_opt_in_and_content_review_always_required(self):
        for content in ('Be helpful.\n', '\n'.join(f'Unique rule {i}.' for i in range(600))):
            self.write('SKILL.md', HEADER + content)
            report = analyzer.analyze(self.root)
            self.assertEqual('required', report['content_review']['status'])
            self.assertEqual(['SKILL.md'], report['content_review']['files'])
            self.assertNotIn('core', report)
            self.assertNotIn('file_metrics', report)
            self.assertNotIn('size_review', self.codes(report))

    def test_compact_duplicates_not_exempt(self):
        self.write('SKILL.md', HEADER + 'Keep IDs.\nKeep IDs.\n')
        self.assertIn('duplicate_prose', self.codes(analyzer.analyze(self.root)))

    def test_cli_default_does_not_lead_with_size(self):
        result = self.cli()
        self.assertIn('Content review REQUIRED', result.stdout)
        self.assertNotIn('tokens', result.stdout)
        self.assertIn('tokens', self.cli('--metrics').stdout)

    def test_semantic_redundancy_can_have_no_static_finding(self):
        self.write('SKILL.md', HEADER + 'Keep identifiers unchanged.\nDo not alter IDs.\n')
        report = analyzer.analyze(self.root)
        self.assertFalse(report['findings'])
        self.assertEqual('required', report['content_review']['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
