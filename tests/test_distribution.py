"""Test complete installation and failures that would silently lose knowledge."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('verify_package', ROOT / 'scripts/verify_package.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class DistributionTests(unittest.TestCase):
    def test_clean_install_integrity_search_and_existing_destination(self):
        with tempfile.TemporaryDirectory(prefix='qw-skill-test-') as folder:
            destination = Path(folder) / 'qw-adcreative-intelligence'
            command = [sys.executable, str(ROOT / 'scripts/install.py'), '--dest', str(destination)]
            first = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertTrue(verifier.verify(destination)['passed'])
            self.assertFalse((destination / '.git').exists())
            search = subprocess.run([sys.executable, str(destination / 'scripts/search_transcripts.py'),
                                     'CTA', '--source', 'T08', '--limit', '1'], capture_output=True, text=True,
                                    encoding='utf-8', env={**__import__('os').environ, 'PYTHONUTF8': '1'})
            self.assertEqual(search.returncode, 0, search.stderr)
            results = json.loads(search.stdout)
            self.assertTrue(results, 'Installed search must retrieve original knowledge')
            self.assertEqual(results[0]['source_id'], 'T08')
            before = (destination / 'SKILL.md').read_bytes()
            duplicate = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(duplicate.returncode, 0)
            self.assertEqual(before, (destination / 'SKILL.md').read_bytes())
            original = next((destination / 'references/knowledge/originals').glob('01*.txt'))
            original.write_bytes(original.read_bytes() + b'changed')
            self.assertFalse(verifier.verify(destination)['passed'], 'Changed originals must fail integrity')

    def test_source_complete(self):
        result = verifier.verify(ROOT)
        self.assertTrue(result['passed'], result['errors'])


if __name__ == '__main__':
    unittest.main()
