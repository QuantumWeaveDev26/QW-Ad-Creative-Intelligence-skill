"""Retrieve an exact, hash-checked transcript passage and its context offline."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def passages(text):
    heading = re.search(r'^## Transcript\s*$', text, re.MULTILINE)
    if not heading:
        raise ValueError('Original has no Transcript heading')
    matches = list(re.finditer(r'^\[(\d{1,3}:\d{2}(?::\d{2})?)\]', text[heading.end():], re.MULTILINE))
    rows = []
    for i, match in enumerate(matches):
        start = heading.end() + match.start()
        end = heading.end() + matches[i + 1].start() if i + 1 < len(matches) else len(text)
        rows.append({'timestamp': match.group(1), 'line': text.count('\n', 0, start) + 1,
                     'original': text[start:end].strip()})
    return rows


def retrieve(source, timestamp, context=1, quote=None, root=ROOT):
    if not 0 <= context <= 3:
        raise ValueError('Context must be between 0 and 3 adjacent passages')
    knowledge = Path(root) / 'references/knowledge'
    manifest = json.loads((knowledge / 'source-manifest.json').read_text(encoding='utf-8'))
    records = [row for row in manifest if row['id'] == source]
    if len(records) != 1:
        raise ValueError('Unknown or ambiguous source ID; use T01 through T09')
    record = records[0]
    raw = (knowledge / 'originals' / record['file']).read_bytes()
    if hashlib.sha256(raw).hexdigest() != record['sha256']:
        raise ValueError('Original byte hash mismatch; do not attribute this file as the verified source')
    rows = passages(raw.decode('utf-8').replace('\r\n', '\n'))
    indices = [i for i, row in enumerate(rows) if row['timestamp'] == timestamp]
    if not indices:
        raise ValueError('Timestamp not found exactly; no nearest passage substituted')
    if len(indices) != 1:
        raise ValueError('Timestamp occurs more than once; inspect the original and disambiguate by opening words')
    index = indices[0]
    if quote is not None:
        normalize = lambda value: ' '.join(value.split())
        if not normalize(quote) or normalize(quote) not in normalize(rows[index]['original']):
            raise ValueError('Quote does not match the selected original passage')
    return {'source_id': source, 'file': record['file'], 'sha256': record['sha256'],
            'original_bytes_verified': True, 'selected': rows[index],
            'context': rows[max(0, index-context):index] + rows[index+1:index+context+1],
            'quote_verified': True if quote is not None else None,
            'limitation': 'Verbatim retrieval verifies provenance, not translation, claim truth or logical support. Read the context.'}


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--timestamp', required=True)
    parser.add_argument('--context', type=int, default=1)
    parser.add_argument('--quote', help='Optional verbatim quote to verify, ignoring whitespace only')
    args = parser.parse_args()
    try:
        result = retrieve(args.source, args.timestamp, args.context, args.quote)
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({'passed': False, 'error': str(error)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
