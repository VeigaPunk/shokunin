#!/usr/bin/env python3
"""Secrets hygiene scan for the R18 cascade-legorder artifacts (mission M7).

Scans every file under this directory for (1) the credential values configured in
the live ~/.kimi-code/config.toml, (2) the leg defaults the live shim.py carries,
and (3) generic credential shapes.

Credential values are read from the config and the shim inside this process and are
never printed, passed as arguments, or written to disk; only counts leave the
process. Exit status 0 = clean, 1 = hits found.
"""

from __future__ import annotations

import os
import re
import sys
import tomllib

ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.expanduser("~/.kimi-code/config.toml")
SHIM = os.path.expanduser("~/.local/share/ds-flash-shim/shim.py")

SHAPES = [
    ("credential prefix", re.compile(r"\bsk-[A-Za-z0-9_\-]{12,}")),
    ("opencode key", re.compile(r"\boc_sk[_\-][A-Za-z0-9_\-]{12,}")),
    ("bearer token", re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{12,}")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.")),
    ("assigned secret", re.compile(r"(?i)\b[A-Za-z0-9_]*(?:api[_-]?key|token|secret|password)[A-Za-z0-9_]*\s*[=:]\s*[\"'][^\"'\s]{16,}[\"']")),
]


def credential_values() -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    with open(CONFIG, "rb") as fh:
        cfg = tomllib.load(fh)
    for name, prov in sorted(cfg.get("providers", {}).items()):
        if not isinstance(prov, dict):
            continue
        if isinstance(prov.get("api_key"), str):
            out.append((f"config provider {name} api_key", prov["api_key"]))
        for hk, hv in (prov.get("custom_headers") or {}).items():
            if isinstance(hv, str) and any(t in hk.lower() for t in ("auth", "key", "session", "token")):
                out.append((f"config provider {name} header {hk}", hv))
    text = open(SHIM, encoding="utf-8").read()
    for env in ("DS_LEG1_KEY", "DS_LEG1_SESSION", "DS_LEG2_KEY", "DS_LEG3_KEY", "DS_LEG3_SESSION"):
        m = re.search(r'"%s",\s*\n\s*"([^"]+)"' % env, text)
        if m and len(m.group(1)) >= 8:
            out.append((f"shim default {env}", m.group(1)))
    return [(label, v) for label, v in out if isinstance(v, str) and len(v) >= 8]


def main() -> int:
    creds = credential_values()
    files = []
    for base, _dirs, names in os.walk(ROOT):
        for n in sorted(names):
            files.append(os.path.join(base, n))

    print(f"scan root:        {ROOT}")
    print(f"files scanned:    {len(files)}")
    print(f"distinct credential values tested: {len(creds)}")
    print()
    blobs = {}
    for path in files:
        try:
            blobs[path] = open(path, encoding="utf-8", errors="replace").read()
        except OSError as exc:
            print(f"read error {path}: {exc}")
            return 2
    total = 0
    for label, value in creds:
        hits = [os.path.relpath(p, ROOT) for p, b in blobs.items() if value in b]
        total += len(hits)
        print(f"exact  {label:<44} hits={len(hits)}{' ' + str(hits) if hits else ''}")
    for label, rx in SHAPES:
        hits = [os.path.relpath(p, ROOT) for p, b in blobs.items() if rx.search(b)]
        total += len(hits)
        print(f"shape  {label:<44} hits={len(hits)}{' ' + str(hits) if hits else ''}")
    print()
    print(f"TOTAL HITS: {total}")
    if total:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- no credential value or credential-shaped string in any artifact")
    return 0


if __name__ == "__main__":
    sys.exit(main())