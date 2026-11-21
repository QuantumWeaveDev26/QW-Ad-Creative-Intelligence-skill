"""Offline integrity checks; no provider calls. Not a test of model quality."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote


def verify(root):
    root = Path(root).resolve()
    knowledge = root / 'references/knowledge'
    errors = []
    counts = {}
    for manifest, folder, expected in [
        ('source-manifest.json', 'originals', 9),
        ('supplemental-source-manifest.json', None, 1),
    ]:
        rows = json.loads((knowledge / manifest).read_text(encoding='utf-8'))
        if len(rows) != expected:
            errors.append(f'{manifest}: expected {expected} sources')
        for row in rows:
            path = knowledge / folder / row['file'] if folder else knowledge / row['relative_path']
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != row['sha256']:
                errors.append(f'{row["id"]}: missing or changed original bytes')
        counts[manifest] = len(rows)
    catalog = json.loads((knowledge / 'transcript-chunk-catalog.json').read_text(encoding='utf-8'))
    if len(catalog) != 127:
        errors.append('Expected 127 transcript extracts')
    for row in catalog:
        original = (knowledge / 'originals' / row['file']).read_bytes().decode('utf-8')
        excerpt = original[row['start']:row['end']]
        extract = (knowledge / row['path']).read_text(encoding='utf-8').split('## Verbatim transcript extract\n', 1)[1]
        if hashlib.sha256(excerpt.encode('utf-8')).hexdigest() != row['sha256_excerpt']:
            errors.append(f'{row["path"]}: catalog excerpt differs from original')
        if extract != excerpt.replace('\r\n', '\n'):
            errors.append(f'{row["path"]}: packaged extract differs from original')
    for path in [root / 'SKILL.md', *root.glob('references/**/*.md')]:
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            target = target.split('#', 1)[0]
            if not target or re.match(r'[a-zA-Z][\w+.-]*:', target):
                continue
            resolved = (path.parent / unquote(target)).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f'{path.relative_to(root)}: invalid local link {target}')
    for required in ['SKILL.md', 'agents/openai.yaml', 'scripts/search_transcripts.py', 'scripts/read_source.py']:
        if not (root / required).is_file():
            errors.append(f'Missing {required}')
    counts['transcript_extracts'] = len(catalog)
    return {'passed': not errors, 'checks': counts, 'errors': errors}


if __name__ == '__main__':
    try:
        result = verify(Path(__file__).resolve().parents[1])
    except (OSError, ValueError, KeyError, IndexError) as error:
        result = {'passed': False, 'errors': [str(error)]}
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['passed'] else 1)
