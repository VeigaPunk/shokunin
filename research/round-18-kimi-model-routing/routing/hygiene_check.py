#!/usr/bin/env python3
"""Secrets hygiene scan for the R18 routing artifacts (mission M4).

Scans every file under this directory plus .ufo/reports/round-18/kengaku.md for
(1) the exact credential values configured in the live ~/.kimi-code/config.toml
and (2) generic credential shapes.

Credential values are read from the config inside this process and are never
printed, passed as arguments, or written to disk; only counts leave the process.
Exit status 0 = clean, 1 = hits found.
"""

from __future__ import annotations

import os
import re
import sys
import tomllib

ROOT = os.path.dirname(os.path.abspath(__file__))
# ROOT is <wt>/research/round-18-kimi-model-routing/routing; the fleet report lives
# three levels up from here.
EXTRA = [os.path.join(ROOT, "..", "..", "..", ".ufo", "reports", "round-18", "kengaku.md")]
CONFIG = os.path.expanduser("~/.kimi-code/config.toml")

SHAPES = [
    ("credential prefix", re.compile(r"\bsk-[A-Za-z0-9_\-]{12,}")),
    ("bearer token", re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{20,}")),
    ("assigned secret", re.compile(r"(?i)\b[A-Za-z0-9_]*(?:api[_-]?key|token|secret|password)[A-Za-z0-9_]*\s*[=:]\s*[\"'][^\"'\s]{16,}[\"']")),
]


def credential_values(cfg: dict) -> list[tuple[str, str]]:
    out = []
    for name, prov in sorted(cfg.get("providers", {}).items()):
        if isinstance(prov, dict):
            if isinstance(prov.get("api_key"), str):
                out.append((f"provider {name} api_key", prov["api_key"]))
            headers = prov.get("headers") or {}
            for hk, hv in headers.items():
                if isinstance(hv, str) and any(t in hk.lower() for t in ("auth", "key", "session", "token")):
                    out.append((f"provider {name} header {hk}", hv))
    return [(label, v) for label, v in out if isinstance(v, str) and len(v) >= 8]


def main() -> int:
    with open(CONFIG, "rb") as fh:
        cfg = tomllib.load(fh)
    creds = credential_values(cfg)

    files = [os.path.join(ROOT, f) for f in sorted(os.listdir(ROOT)) if os.path.isfile(os.path.join(ROOT, f))]
    files += [p for p in (os.path.normpath(e) for e in EXTRA) if os.path.isfile(p)]

    total = 0
    print(f"scan root:        {ROOT}")
    print(f"files scanned:    {len(files)}")
    print(f"distinct configured credential values tested: {len(creds)}")
    print()
    blobs = {}
    for path in files:
        try:
            blobs[path] = open(path, encoding="utf-8", errors="replace").read()
        except OSError as exc:
            print(f"read error {path}: {exc}")
            return 2
    for label, value in creds:
        hits = [os.path.basename(p) for p, b in blobs.items() if value in b]
        total += len(hits)
        print(f"exact  {label:<52} hits={len(hits)}{' ' + str(hits) if hits else ''}")
    for label, rx in SHAPES:
        hits = [os.path.basename(p) for p, b in blobs.items() if rx.search(b)]
        total += len(hits)
        print(f"shape  {label:<52} hits={len(hits)}{' ' + str(hits) if hits else ''}")
    print()
    print(f"TOTAL HITS: {total}")
    if total:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- no credential value or credential-shaped string in any artifact")
    return 0


if __name__ == "__main__":
    sys.exit(main())
