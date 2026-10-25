#!/usr/bin/env python3
"""Record the applied change as masked diff artifacts.

    python3 record_diffs.py

Writes raw/shim-py-diff-masked.txt and raw/unit-diff-masked.txt (unified diffs of
backup -> current, every credential-shaped token replaced by a prefix + <masked>)
and prints a per-file sha256 table. It re-derives the diffs from disk rather than
from the apply run, so the artifacts are verifiable against the live files at any
later time.
"""

from __future__ import annotations

import difflib
import hashlib
import os
import re
import sys
import tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIRS = [
    ("shim-py-diff-masked.txt",
     os.path.expanduser("~/.local/share/ds-flash-shim/shim.py"),
     "20261015-112620"),
    ("unit-diff-masked.txt",
     os.path.expanduser("~/.config/systemd/user/ds-flash-shim.service"),
     "20261015-112620"),
]


def credential_values() -> list[str]:
    """Every credential the live config and the live shim carry (values never printed)."""
    out: list[str] = []
    with open(os.path.expanduser("~/.kimi-code/config.toml"), "rb") as fh:
        cfg = tomllib.load(fh)
    for _name, prov in sorted(cfg.get("providers", {}).items()):
        if not isinstance(prov, dict):
            continue
        if isinstance(prov.get("api_key"), str):
            out.append(prov["api_key"])
        for hv in (prov.get("custom_headers") or {}).values():
            if isinstance(hv, str):
                out.append(hv)
    with open(os.path.expanduser("~/.local/share/ds-flash-shim/shim.py"), encoding="utf-8") as fh:
        shim = fh.read()
    for env in ("DS_LEG1_KEY", "DS_LEG1_SESSION", "DS_LEG2_KEY", "DS_LEG3_KEY", "DS_LEG3_SESSION"):
        m = re.search(r'"%s",\s*\n\s*"([^"]+)"' % env, shim)
        if m:
            out.append(m.group(1))
    return [v for v in out if isinstance(v, str) and len(v) >= 8]


def mask(line: str, secrets: list[str]) -> str:
    for value in secrets:
        if value in line:
            line = line.replace(value, "%s...<masked:%d chars>" % (value[:4], len(value)))
    line = re.sub(r"\b(?:oc_sk|sk)[_\-][A-Za-z0-9_\-]{6,}",
                  lambda m: m.group(0)[:4] + "...<masked>", line)
    line = re.sub(r"(Bearer )\S{6,}", r"\1<masked>", line)
    return line


def sha256(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main() -> int:
    out_dir = os.path.join(ROOT, "raw")
    os.makedirs(out_dir, exist_ok=True)
    secrets = credential_values()
    print("credential values masked by exact match: %d" % len(secrets))
    rows = []
    for name, current, ts in PAIRS:
        backup = "%s.%s.bak" % (current, ts)
        if not os.path.exists(backup):
            print("missing backup %s" % backup, file=sys.stderr)
            return 1
        with open(backup) as fh:
            before = fh.read()
        with open(current) as fh:
            after = fh.read()
        diff = difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                    fromfile=backup, tofile=current, n=3)
        text = "".join(mask(l, secrets) for l in diff)
        path = os.path.join(out_dir, name)
        with open(path, "w") as fh:
            fh.write(text)
        hunks = sum(1 for l in text.splitlines() if l.startswith("@@"))
        added = sum(1 for l in text.splitlines() if l.startswith("+") and not l.startswith("+++"))
        removed = sum(1 for l in text.splitlines() if l.startswith("-") and not l.startswith("---"))
        rows.append((name, hunks, added, removed, sha256(backup), sha256(current)))
        print("%-26s hunks=%-3d +%-3d -%-3d  sha_before=%s sha_after=%s" % rows[-1])
    print("wrote %s" % out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())