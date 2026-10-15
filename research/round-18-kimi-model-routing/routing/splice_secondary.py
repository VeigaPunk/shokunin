#!/usr/bin/env python3
"""Splice the R18 routing table into ~/.kimi-code/config.toml.

Operator tool for mission M4 (r18-routing). The mission itself never writes the
live config; this script is the exact, reviewable splice the operator runs.

Default is a DRY RUN: it prints the unified diff and changes nothing.
With --apply it (1) verifies the live pool against the pinned hash, (2) writes a
timestamped backup next to the config (host convention:
config.toml.YYYYmmdd-HHMMSS.bak), (3) builds the new file in memory, parses it
with tomllib, checks that every pool id still resolves to a [models.*] entry,
and only then replaces the file atomically.

Usage:
  python3 splice_secondary.py                        # dry run against the live config
  python3 splice_secondary.py --apply                # perform the splice
  python3 splice_secondary.py --config /path/to/cfg  # alternate target
  python3 splice_secondary.py --no-hash-guard        # skip the pinned-hash guard
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import shutil
import sys
import tempfile
import tomllib
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TABLE = os.path.join(HERE, "kimi-secondary-models-round18.toml")
DEFAULT_CONFIG = os.path.expanduser("~/.kimi-code/config.toml")

# Pinned at M4 run start, 2026-10-15. The guard fails loudly if the live file
# has moved: re-derive the pool and re-check the table before splicing.
PINNED_FILE_SHA256 = "c5f12997f7cee456eacddbaf03c95e598ca5911cb18d6e6cf7821909b6fc9ebf"
PINNED_POOL_SHA256 = "9dcbc7d2549a911588fb15a8163a5732f00eeaf4ea29b8015415ed749322858d"

SECTION = "[secondary_model]"
SUB_TABLE = "[secondary_model.models]"


def pool_sha256(models: dict) -> str:
    canon = json.dumps(models, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def extract_section(text: str, section: str) -> str:
    """Return the TOML text of `section` up to the next top-level header.

    The caller guarantees `section` is not itself nested under another table.
    A `# SPLICE-END` sentinel stops the payload early, so the evidence footer of
    the routing-table file is never copied into the live config.
    """
    lines = text.splitlines()
    try:
        start = lines.index(section)
    except ValueError:
        raise SystemExit(f"section {section} not found in the routing table file")
    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped.startswith("# SPLICE-END"):
            end = i
            break
        if stripped.startswith("[") and stripped != SUB_TABLE:
            end = i
            break
    return "\n".join(lines[start:end]).rstrip() + "\n"


def find_region(lines: list[str]) -> tuple[int, int]:
    """Locate the live [secondary_model] region: [start, end) line indices."""
    try:
        start = lines.index(SECTION)
    except ValueError:
        raise SystemExit("live config has no [secondary_model] section")
    end = len(lines)
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped.startswith("[") and stripped != SUB_TABLE:
            end = i
            break
    # keep one blank separator line before the next header
    while end > start and lines[end - 1].strip() == "":
        end -= 1
    return start, end


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", default=DEFAULT_TABLE, help="routing table TOML to splice in")
    ap.add_argument("--config", default=DEFAULT_CONFIG, help="target config.toml")
    ap.add_argument("--apply", action="store_true", help="perform the splice (default: dry run)")
    ap.add_argument("--no-hash-guard", action="store_true", help="skip the pinned pool-hash guard")
    args = ap.parse_args()

    with open(args.table, encoding="utf-8") as fh:
        table_text = fh.read()
    new_section = extract_section(table_text, SECTION)
    new_cfg = tomllib.loads(table_text)
    new_pool = new_cfg["secondary_model"]["models"]

    with open(args.config, "rb") as fh:
        raw = fh.read()
    live_text = raw.decode("utf-8")
    live = tomllib.loads(live_text)
    live_models = live.get("models", {})
    live_pool = live["secondary_model"]["models"]

    file_sha = hashlib.sha256(raw).hexdigest()
    live_pool_sha = pool_sha256(live_pool)
    print(f"target config     {args.config}")
    print(f"file sha256       {file_sha}")
    print(f"pool sha256       {live_pool_sha}   ({len(live_pool)} entries)")
    print(f"new pool          {pool_sha256(new_pool)}   ({len(new_pool)} entries)")
    print()

    problems = []
    if file_sha != PINNED_FILE_SHA256 and not args.no_hash_guard:
        problems.append(
            f"live file sha256 differs from the pin ({PINNED_FILE_SHA256[:16]}...) -- "
            "the config moved since the table was written; re-check the table against the current pool"
        )
    if live_pool_sha != PINNED_POOL_SHA256 and not args.no_hash_guard:
        problems.append(
            f"live pool sha256 differs from the pin ({PINNED_POOL_SHA256[:16]}...) -- "
            "bucket assignments were derived from the pinned pool"
        )
    missing = sorted(k for k in new_pool if k not in live_models)
    if missing:
        problems.append(f"new pool ids with no [models.*] entry: {missing}")
    if problems:
        print("GUARD FAILURES:")
        for p in problems:
            print(f"  - {p}")
        print("\nRe-run with --no-hash-guard only after re-checking the table by hand.")
        return 2

    lines = live_text.splitlines()
    start, end = find_region(lines)
    print(f"live region: lines {start + 1}-{end} ({end - start} lines)")
    removed = [l for l in lines[start:end] if l.strip().startswith('"')]
    added = new_section.count(" = ")
    print(f"pool entries removed: {len(removed)} -> added: {added}")
    print()
    diff = difflib.unified_diff(
        lines[start:end] + [""],
        new_section.splitlines() + [""],
        fromfile=f"{args.config}:{start + 1}",
        tofile=f"{os.path.basename(args.table)}:{SECTION}",
        lineterm="",
    )
    print("\n".join(diff))
    print()

    if not args.apply:
        print("DRY RUN -- nothing written. Re-run with --apply to splice.")
        return 0

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = f"{args.config}.{stamp}.bak"
    shutil.copy2(args.config, backup)
    print(f"backup written: {backup}")

    new_lines = lines[:start] + new_section.splitlines() + [""] + lines[end:]
    new_bytes = ("\n".join(new_lines).rstrip() + "\n").encode("utf-8")
    parsed = tomllib.loads(new_bytes.decode("utf-8"))
    if parsed["secondary_model"]["models"] != new_pool:
        print("ERROR: re-parsed spliced file does not carry the expected pool; nothing written")
        return 3
    print(f"spliced pool re-parsed: {len(parsed['secondary_model']['models'])} entries")

    d = os.path.dirname(os.path.abspath(args.config))
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".config.toml.r18-")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(new_bytes)
        os.chmod(tmp, 0o600)
        os.replace(tmp, args.config)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)

    new_raw = open(args.config, "rb").read()
    print(f"applied. new file sha256 {hashlib.sha256(new_raw).hexdigest()}")
    print(f"rollback: cp -p {backup} {args.config}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
