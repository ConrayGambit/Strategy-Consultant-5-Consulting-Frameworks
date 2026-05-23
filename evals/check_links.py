#!/usr/bin/env python3
"""Check that every local Markdown link in the repo resolves. Exit 1 if any broken."""
from __future__ import annotations
import os, re

LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')

def main() -> int:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bad: list[str] = []; n = 0
    for dp, _dn, fn in os.walk(root):
        if (os.sep + '.git') in dp:
            continue
        for f in fn:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            with open(p, encoding='utf-8', errors='replace') as fh:
                txt = fh.read()
            for m in LINK.findall(txt):
                t = m.strip().split()[0]                      # drop optional "title"
                if t.startswith(('http://', 'https://', 'mailto:', '#', 'tel:')):
                    continue
                t = t.split('#', 1)[0]
                if not t:
                    continue
                n += 1
                if not os.path.exists(os.path.normpath(os.path.join(dp, t))):
                    bad.append(f"{os.path.relpath(p, root)} -> {m}")
    print(f"checked {n} local links; {len(bad)} broken")
    for b in bad:
        print("BROKEN:", b)
    return 1 if bad else 0

if __name__ == "__main__":
    raise SystemExit(main())
