#!/usr/bin/env python3
"""Re-grade every raw capture from scratch and compare with the stored verdict.

    python3 scripts/regrade.py

Grading is deterministic and data-driven, so a second pass over the same raw
files must reproduce the same verdicts. This is the check that proves it: it
rebuilds every verdict from `raw/responses/**` and reports any disagreement.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import grade  # noqa: E402
import probes  # noqa: E402


def probe_for(record):
    probe_id = record.get("probe_id")
    if probe_id == "perf":
        return {"id": "perf", "kind": "perf", "grade": None}
    if probe_id == "warmup":
        return {"id": "warmup", "kind": "warmup",
                "grade": {"type": "exact", "expect": "READY"}}
    return probes.by_id(probe_id)


def main():
    root = common.RESP_DIR
    records = grade.load_records()
    checked = mismatches = skipped = ungraded = 0
    detail = []
    for record in records:
        probe = probe_for(record)
        if record.get("skipped"):
            rebuilt = {"pass": False, "failure_class": "skipped_after_fatal",
                       "detail": record.get("skip_reason") or "skipped",
                       "request_level": True}
        elif probe is None or probe.get("grade") is None:
            ungraded += 1
            continue
        else:
            body_text = (record.get("raw_preview") or "")[:1000]
            rebuilt = grade.grade(probe, record, record.get("status"),
                                  record.get("error_kind"), body_text)
        checked += 1
        stored = record.get("grade") or {}
        if rebuilt.get("failure_class") != stored.get("failure_class") or \
                rebuilt.get("pass") != stored.get("pass"):
            mismatches += 1
            detail.append({
                "file": os.path.relpath(record.get("_file") or record.get("probe_id"), root),
                "model": record.get("pool_id"), "probe": record.get("probe_id"),
                "stored": stored.get("failure_class"), "regraded": rebuilt.get("failure_class"),
                "stored_pass": stored.get("pass"), "regraded_pass": rebuilt.get("pass"),
                "stored_detail": (stored.get("detail") or "")[:160],
                "regraded_detail": (rebuilt.get("detail") or "")[:160],
            })
    report = {"records": len(records), "checked": checked, "mismatches": mismatches,
              "ungraded_perf_or_warmup": ungraded, "detail": detail}
    common.write_json(os.path.join(common.RAW_DIR, "regrade-check.json"), report)
    print("re-graded %d of %d records: %d mismatches (%d perf/warm-up rows carry no grade)"
          % (checked, len(records), mismatches, ungraded))
    for item in detail[:20]:
        print("  MISMATCH %s %s: stored=%s regraded=%s"
              % (item["model"], item["probe"], item["stored"], item["regraded"]))
    return 1 if mismatches else 0


if __name__ == "__main__":
    sys.exit(main())
