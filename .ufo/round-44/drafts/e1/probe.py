#!/usr/bin/env python3
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
COMPARATOR = OUT / "compare-6fbbff5.py"
WORKTREE_COMPARATOR = ROOT / "verifiers/compare_harness_independent.py"
SCOPE_FILE = ROOT / "verifiers/harness-independent-scope.json"
LIVE_FILE = ROOT / ".ufo/round-41/evidence/live-b1be35f.json"
INDEPENDENT_FILE = ROOT / ".ufo/round-41/evidence/independent-b1be35f.json"
SCOPE_IDS = (
    "omp.catalogue.found",
    "omp.catalogue.matched",
    "omp.catalogue.missing_names",
    "omp.catalogue.total",
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def record_values(payload, values):
    for record in payload["results"]:
        cid = record["check"]
        if cid in values:
            record["re_derived"] = values[cid]
            record["value"] = values[cid]


def main():
    live = json.loads(LIVE_FILE.read_text(encoding="utf-8"))
    independent = json.loads(INDEPENDENT_FILE.read_text(encoding="utf-8"))
    live_values = {row["check"]: row["observed"] for row in live["results"]}
    scoped_live = {cid: live_values[cid] for cid in SCOPE_IDS}
    if set(SCOPE_IDS) != set(json.loads(SCOPE_FILE.read_text(encoding="utf-8"))["scope_out"]):
        raise SystemExit("scope fixture does not match the four committed rows")

    record_only = copy.deepcopy(independent)
    record_only.pop("checks")
    record_only.pop("rows")
    record_values(record_only, {"omp.catalogue.found": scoped_live["omp.catalogue.found"]})

    map_only = {"checks": copy.deepcopy(independent["checks"])}
    map_only["checks"].update(scoped_live)

    def mixed(value):
        payload = copy.deepcopy(independent)
        payload.pop("rows")
        payload["checks"]["omp.catalogue.found"] = value
        record_values(payload, {"omp.catalogue.found": value})
        return payload

    cases = {
        "honest-control": {
            "payload": independent,
            "expected_exit": 0,
            "expected_fragment": "",
        },
        "record-only-scoped-live-value": {
            "payload": record_only,
            "expected_exit": 2,
            "expected_fragment": "scope-out value laundering",
        },
        "map-only-scoped-live-values": {
            "payload": map_only,
            "expected_exit": 2,
            "expected_fragment": "derived-set overflow",
        },
        "record-map-coherent-nonlive-value": {
            "payload": mixed(False),
            "expected_exit": 2,
            "expected_fragment": "scope-out value laundering",
        },
        "record-map-coherent-live-value": {
            "payload": mixed(scoped_live["omp.catalogue.found"]),
            "expected_exit": 2,
            "expected_fragment": "scope-out value laundering",
        },
    }
    payload_paths = {}
    for name, case in cases.items():
        path = OUT / ("arm-" + name + ".json")
        write_json(path, case["payload"])
        payload_paths[name] = path

    tracked_inputs = (COMPARATOR, WORKTREE_COMPARATOR, SCOPE_FILE, LIVE_FILE, INDEPENDENT_FILE)
    start_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    start_tree = subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, text=True).strip()
    pins_before = {str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path): sha(path)
                   for path in tracked_inputs}
    results = {
        "started_at_utc": stamp(),
        "repo": str(ROOT),
        "head": start_head,
        "tree": start_tree,
        "frozen_target": "6fbbff5459e9ba5f851ce46fd4ced34c8cf9639a",
        "frozen_comparator": str(COMPARATOR.relative_to(ROOT)),
        "pins_before": pins_before,
        "cases": {},
    }
    all_passed = True
    for name, case in cases.items():
        payload_path = payload_paths[name]
        argv = [
            sys.executable,
            str(COMPARATOR),
            "--live-json", str(LIVE_FILE),
            "--independent-json", str(payload_path),
            "--expect-n", "28",
            "--cwd", str(ROOT),
            "--scope-file", str(SCOPE_FILE),
            "--no-stamp", "--json",
        ]
        started = stamp()
        proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=120)
        finished = stamp()
        try:
            output = json.loads(proc.stdout) if proc.stdout.strip() else None
        except json.JSONDecodeError:
            output = None
        if name == "honest-control":
            valid = (
                proc.returncode == 0
                and output is not None
                and output.get("headline", {}).get("n") == 24
                and output.get("headline", {}).get("total") == 24
                and output.get("agreement", {}).get("n_agree_strict") == 20
                and output.get("agreement", {}).get("n_adjudicated") == 4
                and output.get("agreement", {}).get("n_scoped_out") == 4
            )
        else:
            valid = proc.returncode == case["expected_exit"] and case["expected_fragment"] in proc.stderr
        all_passed = all_passed and valid
        results["cases"][name] = {
            "started_at_utc": started,
            "finished_at_utc": finished,
            "argv": argv,
            "process_cwd": str(ROOT),
            "payload": str(payload_path.relative_to(ROOT)),
            "payload_sha256": sha(payload_path),
            "payload_bytes": payload_path.stat().st_size,
            "exit": proc.returncode,
            "expected_exit": case["expected_exit"],
            "expected_class": case["expected_fragment"],
            "matched_expectation": valid,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "output": output,
        }

    pins_after = {str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path): sha(path)
                  for path in tracked_inputs}
    end_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    end_tree = subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, text=True).strip()
    results["finished_at_utc"] = stamp()
    results["head_after"] = end_head
    results["tree_after"] = end_tree
    results["pins_after"] = pins_after
    results["pins_unchanged"] = pins_before == pins_after
    results["git_state_unchanged"] = start_head == end_head and start_tree == end_tree
    results["probe_sha256"] = sha(Path(__file__))
    results["all_expectations_passed"] = all_passed and results["pins_unchanged"] and results["git_state_unchanged"]
    write_json(OUT / "probe-results.json", results)
    return 0 if results["all_expectations_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
