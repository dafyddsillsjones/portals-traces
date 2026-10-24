"""Refresh the self-contained interface after editing data.json. Python 3 only."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
data = json.loads((root / 'data.json').read_text(encoding='utf-8'))
items = data['items']
ids = [item['id'] for item in items]
if len(ids) != len(set(ids)):
    raise SystemExit('Duplicate record IDs: resolve them before rebuilding.')
known = set(ids)
for item in items:
    for target in item.get('links', []):
        if target not in known:
            raise SystemExit(f"Unknown connection: {item['id']} -> {target}")
    for contribution in item.get('contributions', []):
        if contribution['source'] not in known:
            raise SystemExit(f"Unknown contribution source in {item['id']}")
page = root / 'index.html'
html = page.read_text(encoding='utf-8')
payload = json.dumps(items, ensure_ascii=False).replace('<', '\\u003c')
html, count = re.subn(r'const items=\[.*?\];', lambda _: 'const items=' + payload + ';', html, count=1, flags=re.S)
if count != 1:
    raise SystemExit('Cannot locate the embedded data. index.html was not changed.')
page.write_text(html, encoding='utf-8')
print(f'Refreshed {len(items)} records. Open index.html to review.')
