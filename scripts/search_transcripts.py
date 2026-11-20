"""Optional offline lookup. Uses only the packaged originals, no network or paid calls."""
from pathlib import Path
import argparse, json, re
p=argparse.ArgumentParser()
p.add_argument('query', help='Space-separated English or original-language search terms')
p.add_argument('--source', default='', help='Optional T01..T09')
p.add_argument('--limit', type=int, default=6)
a=p.parse_args()
ref=Path(__file__).resolve().parents[1]/'references/knowledge'
terms=[t.casefold() for t in a.query.split() if t]
results=[]
for c in json.loads((ref/'transcript-chunk-catalog.json').read_text()):
 if a.source and c['source_id']!=a.source:continue
 text=(ref/c['path']).read_text(encoding='utf-8').split('## Verbatim transcript extract\n',1)[1]
 score=sum(text.casefold().count(t) for t in terms)
 if score:
  hit=min((text.casefold().find(t) for t in terms if t in text.casefold()),default=0)
  results.append((score,{**c,'excerpt':text[max(0,hit-150):hit+900]}))
results.sort(key=lambda x:x[0],reverse=True)
print(json.dumps([x[1] for x in results[:max(1,min(a.limit,20))]],ensure_ascii=False,indent=2))
