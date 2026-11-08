"""Write files.json: every servable file in the repo with its size, for the index.html browser."""
import json, os, subprocess, time

SKIP_PREFIX = ('.',)
SKIP_FILES = {'index.html', 'CNAME', 'files.json'}

paths = subprocess.run(['git', 'ls-files', '-z'], capture_output=True, check=True).stdout.decode().split('\0')
files = []
for p in sorted(filter(None, paths)):
    if p in SKIP_FILES or any(part.startswith(SKIP_PREFIX) for part in p.split('/')):
        continue
    files.append({'path': p, 'size': os.path.getsize(p)})

with open('files.json', 'w') as f:
    json.dump({'generated': int(time.time()), 'files': files}, f, separators=(',', ':'))
print(f'files.json: {len(files)} files')
