from pathlib import Path
import importlib.util
import json
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('read_source', ROOT / 'scripts/read_source.py')
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)


class SourceRetrievalTests(unittest.TestCase):
    def test_exact_original_quote_context_and_line(self):
        result = source.retrieve('T08', '04:35', quote='specific, relatable hook')
        self.assertTrue(result['quote_verified'])
        self.assertEqual(result['selected']['line'], 80)
        self.assertIn('एक core message', result['selected']['original'])
        self.assertIn('04:49', [p['timestamp'] for p in result['context']])
        self.assertTrue(any('100% sure' in p['original'] for p in result['context']))

    def test_missing_timestamp_is_not_substituted(self):
        with self.assertRaisesRegex(ValueError, 'not found exactly'):
            source.retrieve('T08', '04:36')

    def test_wrong_quote_rejected_even_if_in_adjacent_passage(self):
        with self.assertRaisesRegex(ValueError, 'Quote does not match'):
            source.retrieve('T08', '04:35', quote='100% sure')

    def test_summary_is_not_timestamp_evidence(self):
        text = '## Summary\n[04:35] summary only\n## Transcript\n[04:49] original\n[110:05] unusual original\n'
        self.assertEqual([r['timestamp'] for r in source.passages(text)], ['04:49', '110:05'])

    def test_unknown_source_and_empty_quote_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unknown'):
            source.retrieve('T99', '04:35')
        with self.assertRaisesRegex(ValueError, 'Quote does not match'):
            source.retrieve('T08', '04:35', quote=' ')

    def test_changed_original_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            knowledge = Path(folder) / 'references/knowledge'
            (knowledge / 'originals').mkdir(parents=True)
            shutil.copy2(ROOT / 'references/knowledge/source-manifest.json', knowledge)
            name = '08 - Improving Ad Scripts.txt'
            (knowledge / 'originals' / name).write_bytes(b'changed source')
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                source.retrieve('T08', '04:35', root=Path(folder))


if __name__ == '__main__':
    unittest.main()
