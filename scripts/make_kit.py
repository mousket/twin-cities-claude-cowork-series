#!/usr/bin/env python3
"""Build birchwood-starter-kit.zip for Session 1 from the repo tree.
Includes: START-HERE.md, before-you-come/ (2 HTML guides), prompts/, birchwood-folder/ (the synthetic inputs).
Excludes: expected-outputs/ (answer keys) and instructor docs.
The zip is deterministic (fixed timestamps, sorted order), so rebuilding gives identical bytes."""
import zipfile, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
s1 = root / "series-01-process-factory" / "session-01-cowork-101"
kit = s1 / "starter-kit"
pre = s1 / "pre-session"
inputs = s1 / "synthetic-data" / "property-management" / "inputs"
out = root / "birchwood-starter-kit.zip"
top = "birchwood-starter-kit"
FIXED = (2026, 10, 2, 12, 0, 0)

def add(z, src, arc):
    info = zipfile.ZipInfo(arc, FIXED)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    z.writestr(info, pathlib.Path(src).read_bytes())

entries = [(kit / "START-HERE.md", f"{top}/START-HERE.md")]
for p in sorted(pre.glob("*.html")):
    entries.append((p, f"{top}/before-you-come/{p.name}"))
for p in sorted((kit / "prompts").glob("*.md")):
    entries.append((p, f"{top}/prompts/{p.name}"))
entries.append((kit / "scheduled-task" / "monday-digest-prompt.md", f"{top}/prompts/scheduled-task-prompt.md"))
for p in sorted(inputs.rglob("*")):
    if p.is_file() and p.name != ".DS_Store":
        entries.append((p, f"{top}/birchwood-folder/{p.relative_to(inputs).as_posix()}"))
entries.sort(key=lambda e: e[1])
with zipfile.ZipFile(out, "w") as z:
    for src, arc in entries:
        add(z, src, arc)
print("wrote", out, len(entries), "files")
