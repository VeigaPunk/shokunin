#!/usr/bin/env python3
"""root-ledgers -- protocol-lane gate: fleet-root ledger identity.

Asserts that a root's SCORECARD.md and LOG.md carry the main-repo fleet
identity (not a lane's bytes) and that the protocol-lane gate registry
sits above the aggregator section with the registered closure-check row.

Checks, in fixed emission order:

  1. ``scorecard_header_lost``    -- SCORECARD.md line 1 != pinned header
     (the seen header is reported, e.g. ``# kotoba-shokunin -- Scorecard``).
  2. ``log_header_lost``          -- LOG.md line 1 != pinned header.
  3. ``protocol_registry_lost``   -- no SCORECARD.md line is exactly the
     pinned registry heading.
  4. ``aggregator_section_lost``  -- no SCORECARD.md line starts with the
     pinned aggregator prefix.
  5. ``registry_below_aggregator``-- both headings exist but the registry
     heading's first occurrence is not strictly above the aggregator
     heading's first occurrence.
  6. ``closure_check_row_lost``   -- emitted only when both headings exist
     AND the registry is strictly above the aggregator: no table row
     starting with the pinned closure-check row prefix lies between them.

Check-6 gating is deliberate and documented in the registry row: when a
boundary is missing or inverted the window is undefined, and findings 3-5
already name the defect; emitting the row finding too would double-count a
single structural loss. Deterministic: first heading occurrence wins.

Exit map: 0 clean . 1 failed . 2 could-not-evaluate (missing input, git
error, snapshot_tampered, unreadable ledger, unreadable pinned values) .
64 usage.

All pinned strings, frozen replay revisions, verdicts and blob sha256
digests live exclusively in ``.ufo/gates/root-ledgers/expected.json`` --
never hardcoded here or in fixtures.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

GATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "root-ledgers")
EXPECTED_PATH = os.path.join(GATE_DIR, "expected.json")
FIXTURES_DIR = os.path.join(GATE_DIR, "fixtures")

LEDGERS = ("SCORECARD.md", "LOG.md")

# Finding ids that classify the run as could-not-evaluate (exit 2) rather
# than failed (exit 1).
ERROR_IDS = (
    "missing_input",
    "unreadable_ledger",
    "git_error",
    "pinned_values_unreadable",
    "snapshot_tampered",
)

VERDICT_BY_EXIT = {0: "clean", 1: "failed", 2: "could-not-evaluate"}


class UsageParser(argparse.ArgumentParser):
    """argparse with the contract's usage exit code."""

    def error(self, message):
        self.print_usage(sys.stderr)
        sys.stderr.write("%s: error: %s\n" % (self.prog, message))
        sys.exit(64)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()

def load_expected():
    """Return (pinned_dict_or_None, error_finding_or_None)."""
    try:
        with open(EXPECTED_PATH, "r", encoding="utf-8") as fh:
            return json.load(fh), None
    except (OSError, ValueError) as exc:
        return None, {
            "id": "pinned_values_unreadable",
            "file": os.path.relpath(EXPECTED_PATH),
            "detail": str(exc),
        }


def read_live(root, name):
    path = os.path.join(root, name)
    try:
        with open(path, "rb") as fh:
            return fh.read()
    except OSError:
        return None


def read_rev(repo, rev, name):
    proc = subprocess.run(
        ["git", "-C", repo, "show", "%s:%s" % (rev, name)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def decode_ledger(data):
    try:
        return data.decode("utf-8"), None
    except UnicodeDecodeError as exc:
        return None, str(exc)


FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


def mask_fences(lines):
    """Blank fenced-code lines (fences included), keeping line indices.

    CommonMark-style: a fence opens on 3+ backticks or tildes indented at most
    3 spaces and closes on a run of the same character at least as long. A
    heading or row inside a fence is quoted text, not a ledger section.
    """
    out, fence = [], None
    for line in lines:
        m = FENCE_RE.match(line)
        if fence is None:
            if m:
                fence = m.group(1)
                out.append("")
                continue
            out.append(line)
        else:
            if (m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence)
                    and not line.strip().lstrip(fence[0])):
                fence = None
            out.append("")
    return out


def evaluate(scorecard_text, log_text, pinned):
    """Return ordered finding dicts for decoded ledger contents."""
    findings = []
    sc_lines = mask_fences(scorecard_text.splitlines())
    log_lines = log_text.splitlines()

    sc_header = sc_lines[0] if sc_lines else ""
    if sc_header != pinned["scorecard_header"]:
        findings.append({
            "id": "scorecard_header_lost",
            "file": "SCORECARD.md",
            "detail": "line 1 is %r; pinned %r"
                      % (sc_header, pinned["scorecard_header"]),
        })

    log_header = log_lines[0] if log_lines else ""
    if log_header != pinned["log_header"]:
        findings.append({
            "id": "log_header_lost",
            "file": "LOG.md",
            "detail": "line 1 is %r; pinned %r"
                      % (log_header, pinned["log_header"]),
        })

    reg_heading = pinned["registry_heading"]
    agg_prefix = pinned["aggregator_prefix"]
    row_prefix = pinned["closure_row_prefix"]

    reg_idx = next(
        (i for i, l in enumerate(sc_lines) if l == reg_heading), None)
    agg_idx = next(
        (i for i, l in enumerate(sc_lines) if l.startswith(agg_prefix)),
        None)

    if reg_idx is None:
        findings.append({
            "id": "protocol_registry_lost",
            "file": "SCORECARD.md",
            "detail": "no line exactly %r" % reg_heading,
        })
    if agg_idx is None:
        findings.append({
            "id": "aggregator_section_lost",
            "file": "SCORECARD.md",
            "detail": "no line starting %r" % agg_prefix,
        })
    reg_count = sum(1 for l in sc_lines if l == reg_heading)
    if reg_count > 1:
        findings.append({
            "id": "protocol_registry_duplicated",
            "file": "SCORECARD.md",
            "detail": "%d lines exactly %r; the registry home must be one section"
                      % (reg_count, reg_heading),
        })

    # The closure-row window is defined only when both boundaries exist in
    # the required order; otherwise the boundary findings already carry the
    # defect and a row verdict would be undefined rather than lost.
    if reg_idx is not None and agg_idx is not None:
        if reg_idx >= agg_idx:
            findings.append({
                "id": "registry_below_aggregator",
                "file": "SCORECARD.md",
                "detail": "registry heading line %d not above aggregator "
                          "line %d" % (reg_idx + 1, agg_idx + 1),
            })
        else:
            window = sc_lines[reg_idx + 1:agg_idx]
            row = next(
                (l for l in window if l.startswith(row_prefix)), None)
            if row is None:
                findings.append({
                    "id": "closure_check_row_lost",
                    "file": "SCORECARD.md",
                    "detail": "no row starting %r between registry line %d "
                              "and aggregator line %d"
                              % (row_prefix, reg_idx + 1, agg_idx + 1),
                })
    return findings


def collect_ledger_bytes(root, rev):
    """Return (findings, {name: bytes}). Missing/unreadable => findings."""
    findings = []
    blobs = {}
    for name in LEDGERS:
        if rev is None:
            data = read_live(root, name)
            origin = os.path.join(root, name)
        else:
            data = read_rev(root, rev, name)
            origin = "%s:%s" % (rev, name)
        if data is None:
            findings.append({
                "id": "missing_input" if rev is None else "git_error",
                "file": name,
                "detail": "could not read %s" % origin,
            })
        else:
            blobs[name] = data
    return findings, blobs


def describe_revision(root, rev):
    """Name what was measured: the git revision, or the worktree + HEAD + dirt."""
    if rev is not None:
        return rev
    root_abs = os.path.abspath(root)
    head = subprocess.run(["git", "-C", root_abs, "rev-parse", "--short", "HEAD"],
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    dirty = subprocess.run(["git", "-C", root_abs, "status", "--porcelain", "--"]
                           + list(LEDGERS), stdout=subprocess.PIPE,
                           stderr=subprocess.DEVNULL, text=True)
    head_s = head.stdout.strip() if head.returncode == 0 else "no-git"
    n_dirty = len(dirty.stdout.splitlines()) if dirty.returncode == 0 else -1
    return "worktree %s @%s dirty_ledgers=%d" % (root_abs, head_s, n_dirty)


def run_check(root, rev):
    """Live/--rev mode. Return (exit, findings, revision)."""
    pinned, err = load_expected()
    rev_label = describe_revision(root, rev)
    if err is not None:
        return 2, [err], rev_label

    findings, blobs = collect_ledger_bytes(root, rev)
    if findings:
        return 2, findings, rev_label

    decoded = {}
    for name in LEDGERS:
        text, dec_err = decode_ledger(blobs[name])
        if dec_err is not None:
            findings.append({
                "id": "unreadable_ledger",
                "file": name,
                "detail": "utf-8 decode failed: %s" % dec_err,
            })
        else:
            decoded[name] = text
    if findings:
        return 2, findings, rev_label

    findings = evaluate(decoded["SCORECARD.md"], decoded["LOG.md"], pinned)
    return (1 if findings else 0), findings, rev_label


def run_frozen(root):
    """Replay every pinned revision from expected.json against git."""
    pinned, err = load_expected()
    if err is not None:
        return 2, [err], None, []

    findings = []
    replays = []
    for replay in pinned["frozen"]:
        name = replay["name"]
        rev = replay["rev"]
        read_findings, blobs = collect_ledger_bytes(root, rev)
        entry = {"name": name, "rev": rev}
        if read_findings:
            entry["ok"] = False
            for f in read_findings:
                f = dict(f)
                f["detail"] = "frozen %s: %s" % (name, f["detail"])
                findings.append(f)
            replays.append(entry)
            continue

        tampered = False
        for ledger in LEDGERS:
            got = sha256_bytes(blobs[ledger])
            want = replay["sha256"][ledger]
            if got != want:
                tampered = True
                findings.append({
                    "id": "snapshot_tampered",
                    "file": ledger,
                    "detail": "frozen %s: %s:%s sha256 %s != pinned %s"
                              % (name, rev, ledger, got, want),
                })
        if tampered:
            entry["ok"] = False
            replays.append(entry)
            continue

        exit_code, eval_findings, _ = run_check(root, rev)
        got_ids = sorted(f["id"] for f in eval_findings)
        want_ids = sorted(replay["expected_findings"])
        ok = (exit_code == replay["expected_exit"] and got_ids == want_ids)
        entry["ok"] = ok
        entry["exit"] = exit_code
        entry["findings"] = got_ids
        if not ok:
            findings.append({
                "id": "baseline_mismatch",
                "file": "frozen:%s" % name,
                "detail": "%s: exit %d want %d; findings %s want %s"
                          % (rev, exit_code, replay["expected_exit"],
                             got_ids, want_ids),
            })
        replays.append(entry)

    if any(f["id"] == "snapshot_tampered" or f["id"] in ERROR_IDS
           for f in findings):
        exit_code = 2
    elif findings:
        exit_code = 1
    else:
        exit_code = 0
    return exit_code, findings, None, replays


def run_selftest():
    """Copy each fixture to a temp dir and assert exit + finding ids."""
    if not os.path.isdir(FIXTURES_DIR):
        return 2, [{
            "id": "missing_input",
            "file": os.path.relpath(FIXTURES_DIR),
            "detail": "fixtures directory absent",
        }], []

    names = sorted(
        d for d in os.listdir(FIXTURES_DIR)
        if os.path.isdir(os.path.join(FIXTURES_DIR, d)))
    results = []
    for name in names:
        src = os.path.join(FIXTURES_DIR, name)
        expected_file = os.path.join(src, "expected.json")
        try:
            with open(expected_file, "r", encoding="utf-8") as fh:
                want = json.load(fh)
        except (OSError, ValueError) as exc:
            results.append({"name": name, "ok": False,
                            "detail": "expected.json unreadable: %s" % exc})
            continue

        with tempfile.TemporaryDirectory(
                prefix="root-ledgers-fixture-") as tmp:
            dest = os.path.join(tmp, name)
            shutil.copytree(src, dest)
            proc = subprocess.run(
                [sys.executable, os.path.abspath(__file__),
                 "--root", dest, "--json"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                out = json.loads(proc.stdout.decode("utf-8"))
            except ValueError:
                results.append({"name": name, "ok": False,
                                "detail": "gate output not JSON: %s"
                                          % proc.stderr.decode(
                                              "utf-8", "replace")[:200]})
                continue
        got_ids = sorted(f["id"] for f in out["findings"])
        want_ids = sorted(want["findings"])
        ok = (out["exit"] == want["exit"] and got_ids == want_ids)
        results.append({
            "name": name,
            "ok": ok,
            "exit": out["exit"],
            "findings": got_ids,
            "detail": "" if ok else
                      "exit %d want %d; findings %s want %s"
                      % (out["exit"], want["exit"], got_ids, want_ids),
        })
    passed = sum(1 for r in results if r["ok"])
    return (0 if passed == len(results) else 1), [], results


def emit(result, as_json):
    """Print per contract: JSON shape, or one line per finding + VERDICT."""
    if as_json:
        print(json.dumps(result, indent=2, sort_keys=True))
        return
    for f in result["findings"]:
        print("%s %s -- %s" % (f["id"], f["file"], f["detail"]))
    if "replays" in result:
        for r in result["replays"]:
            print("frozen %s (%s): %s" % (
                r["name"], r["rev"], "ok" if r.get("ok") else "FAILED"))
    if "selftest" in result:
        for r in result["selftest"]["results"]:
            line = "selftest %s: %s" % (r["name"],
                                      "ok" if r["ok"] else "FAILED")
            if r.get("detail"):
                line += " -- " + r["detail"]
            print(line)
        print("selftest %d/%d" % (result["selftest"]["passed"],
                                result["selftest"]["total"]))
    print("VERDICT %s" % result["verdict"])


def main(argv=None):
    parser = UsageParser(
        prog="root-ledgers.py",
        description="fleet-root ledger identity gate (protocol lane)")
    parser.add_argument("--root", default=".",
                        help="repository root (default: cwd)")
    parser.add_argument("--rev", default=None,
                        help="read ledgers via `git -C ROOT show REV:FILE`")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--frozen", action="store_true",
                      help="replay pinned revisions from expected.json")
    mode.add_argument("--selftest", action="store_true",
                      help="run fixture assertions")
    parser.add_argument("--json", action="store_true",
                        help="print {verdict, exit, findings, revision}")
    args = parser.parse_args(argv)

    if args.rev is not None and (args.frozen or args.selftest):
        parser.error("--rev cannot combine with --frozen/--selftest")

    findings = []
    if args.selftest:
        exit_code, findings, results = run_selftest()
        passed = sum(1 for r in results if r["ok"])
        result = {
            "verdict": VERDICT_BY_EXIT[exit_code],
            "exit": exit_code,
            "findings": findings,
            "revision": None,
            "selftest": {"passed": passed, "total": len(results),
                         "results": results},
        }
    elif args.frozen:
        exit_code, findings, rev, replays = run_frozen(args.root)
        result = {
            "verdict": VERDICT_BY_EXIT[exit_code],
            "exit": exit_code,
            "findings": findings,
            "revision": rev,
            "replays": replays,
        }
    else:
        exit_code, findings, rev = run_check(args.root, args.rev)
        result = {
            "verdict": VERDICT_BY_EXIT[exit_code],
            "exit": exit_code,
            "findings": findings,
            "revision": rev,
        }

    emit(result, args.json)
    return result["exit"]


if __name__ == "__main__":
    sys.exit(main())
