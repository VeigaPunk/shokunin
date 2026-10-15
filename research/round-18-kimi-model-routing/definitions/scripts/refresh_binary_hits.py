#!/usr/bin/env python3
"""Recompute the client-binary occurrence table inside audit-table.json.

The config-derived rows must stay pinned to the revision this audit was measured
against (the reviewer verified that revision). The binary table is a separate
measurement and was wrong in that revision, so it is refreshed in place rather
than by re-running the whole audit -- re-running audit_definitions.py re-reads
the live config and would silently rebase every row onto a newer revision.

Usage: python3 scripts/refresh_binary_hits.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_definitions as ad  # noqa: E402
import common  # noqa: E402


def main():
    path = os.path.join(common.DEFS_DIR, "audit-table.json")
    with open(path) as fh:
        audit = json.load(fh)
    before = audit.get("binary_field_hits")
    audit["binary_field_hits"] = ad.binary_field_hits()
    audit["binary_count_method"] = ad.BINARY_COUNT_METHOD
    audit["binary_identity"] = ad.binary_identity()
    with open(path, "w") as fh:
        json.dump(audit, fh, indent=2, sort_keys=False)
        fh.write("\n")
    print("refreshed binary table for the audited revision %s" % audit["config_json_digest_16"])
    for k in sorted(audit["binary_field_hits"]):
        new = audit["binary_field_hits"][k]
        old = (before or {}).get(k)
        if old != new:
            print("  %-18s %s -> %s" % (k, old, new))
    print("method: %s" % audit["binary_count_method"])
    bi = audit["binary_identity"]
    print("binary: sha256 %s mtime %s" % ((bi.get("sha256") or "?")[:16], bi.get("mtime")))


if __name__ == "__main__":
    main()
