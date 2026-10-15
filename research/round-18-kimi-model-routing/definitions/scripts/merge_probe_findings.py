#!/usr/bin/env python3
"""Fold probe-derived findings into audit-table.json.

Two finding classes cannot be seen from the config alone, because they compare a
declaration against what a lane actually returned:

  DEF-9   reasoning_key declared, but the lane returned reasoning under a
          different field name (opencode-go's `reasoning` + `reasoning_details`
          where the config says `reasoning_content`)
  DEF-10  no reasoning_key declared, but the lane returned `reasoning_content`
          (the hyper lane, the cascades, xai-oauth)

It also writes `reasoning_key_corrections`, the per-alias fix, so
build_corrections.py can splice it. Idempotent: previous DEF-9/DEF-10 rows are
dropped before recomputing.

Usage: python3 scripts/merge_probe_findings.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

PROBE_FILES = ("raw/probes-effort.json", "raw/probes-effort-pass2.json",
               "raw/probes-tool.json", "raw/probes-tool-pass2.json",
               "raw/probes-tool-pass3.json", "raw/probes-image.json",
               "raw/probes-image-pass2.json")

REASONING_KEYS = ("reasoning_content", "reasoning", "reasoning_details", "thinking")


def main():
    path = os.path.join(common.DEFS_DIR, "audit-table.json")
    with open(path) as fh:
        audit = json.load(fh)
    entries = {e["alias"]: e for e in audit["entries"]}

    # alias -> Counter of reasoning-ish keys actually seen in responses
    seen = {}
    for f in PROBE_FILES:
        p = os.path.join(common.DEFS_DIR, f)
        if not os.path.exists(p):
            continue
        with open(p) as fh:
            for r in json.load(fh)["results"]:
                keys = (r.get("derived") or {}).get("message_keys") or []
                got = [k for k in keys if k in REASONING_KEYS]
                if not got:
                    continue
                seen.setdefault(r["alias"], {}).setdefault(frozenset(got), 0)
                seen[r["alias"]][frozenset(got)] += 1

    findings = []
    corrections = {}
    for alias in sorted(seen):
        e = entries.get(alias)
        if e is None:
            continue
        declared = e.get("reasoning_key")
        observed = sorted({k for fs in seen[alias] for k in fs})
        if declared and declared not in observed and observed:
            alt = "reasoning" if "reasoning" in observed else observed[0]
            findings.append({
                "id": "DEF-9", "class": "reasoning_key mismatch", "triage": "defect",
                "alias": alias, "field": "reasoning_key", "value": declared,
                "detail": ("config declares reasoning_key=%r but the lane returned %s; "
                           "the declared key never appeared" % (declared, observed)),
                "evidence": ["probe", "raw/probes-*.json"],
            })
            corrections[alias] = {"action": "set", "key": alt,
                                  "because": "lane returns %s" % observed}
        elif not declared and "reasoning_content" in observed:
            findings.append({
                "id": "DEF-10", "class": "missing reasoning_key", "triage": "defect",
                "alias": alias, "field": "reasoning_key", "value": None,
                "detail": ("no reasoning_key declared, but the lane returned "
                           "reasoning_content in %d/%d captured responses"
                           % (sum(n for fs, n in seen[alias].items() if "reasoning_content" in fs),
                              sum(seen[alias].values()))),
                "evidence": ["probe", "raw/probes-*.json"],
            })
            corrections[alias] = {"action": "add", "key": "reasoning_content",
                                  "because": "lane returns reasoning_content"}

    audit["defects"] = [d for d in audit["defects"] if d["id"] not in ("DEF-9", "DEF-10")]
    audit["defects"].extend(findings)
    audit["reasoning_key_corrections"] = corrections
    from collections import Counter
    audit["triage_counts"] = dict(Counter(d["triage"] for d in audit["defects"]))
    with open(path, "w") as fh:
        json.dump(audit, fh, indent=2, sort_keys=False)
        fh.write("\n")

    print("DEF-9 (mismatch): %d" % sum(1 for f in findings if f["id"] == "DEF-9"))
    for f in findings:
        if f["id"] == "DEF-9":
            print("   %-42s declared %r -> lane returns %s"
                  % (f["alias"], f["value"], f["detail"].split("returned ")[1].split(";")[0]))
    print("DEF-10 (missing): %d" % sum(1 for f in findings if f["id"] == "DEF-10"))
    print("   aliases: %s" % ", ".join(sorted(
        f["alias"] for f in findings if f["id"] == "DEF-10")))
    print("triage now:", audit["triage_counts"])


if __name__ == "__main__":
    main()
