"""Input isolation checks for fresh-agent evaluation preparation."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


class PreparationTests(unittest.TestCase):
    def test_prepare_raw_inputs_without_rubrics_and_refuse_overwrite(self):
        cases = json.loads((ROOT / 'cases.json').read_text())
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'inputs'
            command = [sys.executable, str(ROOT / 'run_cases.py'), '--prepare', str(target)]
            result = subprocess.run(command, text=True, capture_output=True)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertEqual({case['id'] for case in cases}, {p.name for p in target.iterdir()})
            for case in cases:
                folder = target / case['id']
                actual_files = {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
                self.assertEqual({'REQUEST.txt', *case['files']}, actual_files)
                self.assertEqual(case['user_request'], (folder / 'REQUEST.txt').read_text())
                for name, content in case['files'].items():
                    self.assertEqual(content, (folder / name).read_text())
            request = target / cases[0]['id'] / 'REQUEST.txt'
            request.write_text('Existing evaluator work must survive.')
            second = subprocess.run(command, text=True, capture_output=True)
            self.assertNotEqual(0, second.returncode)
            self.assertEqual('Existing evaluator work must survive.', request.read_text())


if __name__ == '__main__':
    unittest.main()
