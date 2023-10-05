import hashlib
from pathlib import Path
from collections import defaultdict

# for path in filter(lambda p: p.is_file(), Path(".").rglob("*")):
# for path in (p for p in Path(".").rglob("*") if p.is_file()):
# for path in [p for p in Path(".").rglob("*") if p.is_file()]:

groups = defaultdict(list)

for path in Path(".").rglob("*"):
    try:
        hash = hashlib.sha256(path.read_bytes()).hexdigest()
        groups[hash].append(path)
    except IsADirectoryError:
        pass

print({
    k: v
    for k, v in groups.items() if len(v) > 1
})
