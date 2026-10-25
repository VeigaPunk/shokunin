#!/usr/bin/env python3
"""freeze-snapshot.py -- generator for the closure gate's frozen baselines.

`closure-check.py --frozen <NAME>` consumes a *flat* snapshot directory:
`MANIFEST.json`, `watchdog.log`, `reports-index.txt`, `prompts-index.txt`,
`state-counters.txt` (and an optional `expected.json` baseline).  The round-12
snapshots under `.ufo/waves/round-12/frozen/{pre,post-actual,post}/` were
assembled by hand from the prose in `frozen/README.md`; this script is that
prose expressed once, deterministically, so a round-15 baseline can be
re-derived instead of re-implemented.

READ-ONLY OVER THE REPO.  The only writes are inside `--out` (plus the `--selftest`
run's own temp tree, which it creates and removes again).  Never written:
the repo, `.ufo/waves/round-11/**`, `.ufo/waves/round-12/**`,
`.ufo/waves/round-13/**`, `MANIFEST.json`, `.ufo/state/**`.  A round-15 `--out`
(for example `.ufo/waves/round-15/frozen/pre`) is the intended target.

    python3 .ufo/waves/round-15/freeze-snapshot.py --selftest
    python3 .ufo/waves/round-15/freeze-snapshot.py \
        --closed-at 2026-09-28T21:30:00-03:00 --manifest-source live \
        --out .ufo/waves/round-15/frozen/pre

Freezing rule (see `frozen/README.md` §"One freezing rule"; one instant `C`):

  watchdog.log       lines whose leading ISO timestamp is <= C, byte-for-byte
                     (every driver verb, `wrap <lane> round=N complete`
                     included: a wrap line is termination evidence, and the
                     frozen log is what the checker re-parses).
  reports-index.txt  `.ufo/reports/round-*/*.md` present at C, as
                     `rel<TAB>bytes<TAB>tracked<TAB>has_hash<TAB>has_shonen<TAB>landed_at`
                     with `landed_at` = add-commit committer time, `-` when the
                     file was not committed at C.
  prompts-index.txt  `.ufo/prompts/<lane>-round-N.md` present at C, one rel per line.
  state-counters.txt highest `launch`/`steer` round per lane among the *kept* log lines.
  CLOSED_AT.txt      C, the manifest source, main_HEAD, the four counts, the rule.
  MANIFEST.json      the pinned `rounds[]` blob, byte-for-byte as sourced.

Derived baseline (`expected.json`, when `--expected-exit/--expected-debt` are not
given): the checker's OWN frozen projection of the snapshot it was just written --
`closure-check.py --frozen-root <parent> --frozen <name> --json --no-citations`
-- so the baseline is the analysis of the very bytes that will be replayed.
There is no mirror and no live-only check in it: frozen mode has neither the
untracked-prompt sweep nor the history-pin read, so a derived baseline cannot
pin rows that only a materialized live tree could manufacture.  The baseline
exit follows the checker's own precedence (debt -> 1, else could-not-evaluate
-> 2, else 0), never the CLI's "no-baseline" 3.  A derived baseline is
self-pinning and unreviewed; `DERIVED-FROM-FROZEN-PROJECTION.txt` in the
snapshot says so.

"Present at C" is: the add-commit committer time is <= C (landed, `tracked=1`), or
-- for a file not committed at C -- the on-disk mtime is <= C (`tracked=0`,
`landed_at=-`).  `has_hash`/`has_shonen` are the checker's own `_grade_file`
predicates (`RE_HASH_RUN` / `RE_SHONEN`) over the file's current content.

Lane universe (the closure-check.py `_lane_universe` rule, A:42): which lanes
reach `prompts-index.txt` and `state-counters.txt` is decided by the lane-id
grammar `[a-z][a-z0-9_-]*` (closure-check.py `LANE_ID_RE`) applied to prompt
filenames and `launch`/`steer` lines -- never by a fixed lane roster.  A lane
the driver mints mid-round (`kama`, a hyphenated sibling) is a first-class row
the moment its prompt file or dispatch line exists, so the snapshot cannot go
silent about a lane the gate itself adjudicates.  Ordering inside both indexes
is deterministic lexical order; base-lane roster order is not part of the frozen
schema (the checker compares baselines as a set -- `_compare_baseline`).

Exit codes: 0 ok, 1 selftest failures, 2 usage/refusal, 3 checker invocation failed.
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
from datetime import datetime

SCRIPT = os.path.abspath(__file__)
ROUND_15 = os.path.dirname(SCRIPT)

# The checker's lane-id grammar, verbatim from closure-check.py `LANE_ID_RE`.  It is the
# *only* gate on which lanes this generator captures: the checker's lane universe is
# `base LANES u roster ids u driver counters u lanes named by a dispatch/complete line or a
# prompt file` (A:42), so a fixed roster list here would silently drop a lane the gate
# adjudicates (round 15: `kama`, and any hyphenated sibling id).
LANE_ID_RE = r"[a-z][a-z0-9_-]*"

# Copied from closure-check.py:65,71-74 -- the index columns are the frozen mirror of
# load_live()/_grade_file(), so the predicates must be the checker's, not lookalikes.
ROUND_DIR_RE = re.compile(r"^round-(.+)$")
RE_DISPATCH = re.compile(r"^(\S+) (launch|steer) (%s) (?:-> round |round=)(\d+)\b" % LANE_ID_RE)
RE_HASH_RUN = re.compile(r"(?<![0-9a-fA-F])[0-9a-f]{7,}(?![0-9a-fA-F])")
RE_SHONEN = re.compile(r"^#{1,6}\s*SHONEN", re.M)
RE_PROMPT = re.compile(r"^(%s)-round-(\d+)\.md$" % LANE_ID_RE)
RE_REPORT_REL = re.compile(r"^\.ufo/reports/round-[^/]+/[^/]+\.md$")

# Verbatim from the hand-assembled round-12 CLOSED_AT.txt files.
RULE_LINES = [
    "watchdog.log = lines with timestamp <= closed_at; reports-index/prompts-index = files with",
    "mtime <= closed_at (landed_at = add-commit committer time, '-' when untracked);",
    "state-counters = highest launch/steer round per lane among the kept log lines",
    "main_HEAD = newest commit with committer time <= closed_at ('-' when git cannot answer)",
]

FORBIDDEN_OUT_DIRS = ("round-11", "round-12", "round-13")
DEFAULT_CHECKER = os.path.join(".ufo", "waves", "round-15", "closure-check.py")

EXIT_OK, EXIT_SELFTEST, EXIT_USAGE, EXIT_CHECKER = 0, 1, 2, 3

# The checker's own exit precedence for an analysis (closure-check.py:1508):
# debt -> 1, else could-not-evaluate -> 2, else 0.  The frozen CLI returns 3
# ("no-baseline") while the snapshot carries no expected.json yet, so a derived
# baseline computes its exit from the analysis and never from that code.
PROJECT_EXIT_OK, PROJECT_EXIT_DEBT, PROJECT_EXIT_CNE = 0, 1, 2

# The checker's own exit codes (closure-check.py:98-101), named so a note that carries one
# says what it means: 3 is "no-baseline", the answer while the snapshot has no expected.json.
EXIT_NOBASELINE = 3
CLI_EXIT_NAMES = {0: "ok", 1: "debt", 2: "could-not-evaluate", 3: "no-baseline"}

# The note a derived snapshot carries: it names where the baseline came from and
# that it is unreviewed and self-pinning.  The claim, not an input: excluded from
# the pinned input digests.
DERIVED_NOTE = "DERIVED-FROM-FROZEN-PROJECTION.txt"
DERIVED_MARKER = "DERIVED-FROZEN-PROJECTION"

# Classes only a live tree can produce: the untracked-prompt sweep and the
# history-pin read (closure-check.py:1402, :1011).  A derived baseline must never
# carry them -- they are what a materialized mirror used to manufacture.
LIVE_ONLY_CLASSES = ("prompt_untracked", "history_pin", "history_pin_unavailable")

# git runs with a minimal environment so an ambient GIT_DIR / GIT_WORK_TREE cannot
# redirect a read, and so the output is locale-stable.
GIT_ENV = {
    "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
    "HOME": os.path.expanduser("~"),
    "LC_ALL": "C",
}


# --------------------------------------------------------------------------- helpers

def die(message, code=EXIT_USAGE):
    sys.stderr.write("freeze-snapshot: %s\n" % message)
    return code


def read_text(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError as exc:
        raise FreezeError("cannot read %s: %s" % (path, exc))


def read_bytes(path):
    try:
        with open(path, "rb") as fh:
            return fh.read()
    except OSError as exc:
        raise FreezeError("cannot read %s: %s" % (path, exc))


class FreezeError(Exception):
    """A refusal or a missing input: reported on stderr, exit code chosen by the caller."""

    def __init__(self, message, code=None):
        Exception.__init__(self, message)
        self.code = code


def iso_dt(text):
    try:
        return datetime.fromisoformat(text)
    except (ValueError, TypeError):
        return None


def as_aware(dt, ref):
    """Compare two instants even when one side carries no offset (assume ref's zone)."""
    if dt is None:
        return None
    if dt.tzinfo is None and ref is not None and ref.tzinfo is not None:
        return dt.replace(tzinfo=ref.tzinfo)
    if dt.tzinfo is not None and ref is not None and ref.tzinfo is None:
        return dt.replace(tzinfo=None)
    return dt


def le(dt, ref):
    dt = as_aware(dt, ref)
    return dt is not None and ref is not None and dt <= ref


def git(repo, args, binary=False):
    """(returncode, stdout).  Never raises; None returncode when git is unusable."""
    try:
        done = subprocess.run(["git", "-C", repo] + args, capture_output=True,
                              env=GIT_ENV, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None, b""
    if binary:
        return done.returncode, done.stdout
    return done.returncode, done.stdout.decode("utf-8", errors="replace")


def walk_up_repo(script_path):
    """Default --repo: nearest ancestor holding MANIFEST.json + .ufo/ (as the checker)."""
    d = os.path.dirname(os.path.abspath(script_path))
    for _ in range(10):
        if os.path.isfile(os.path.join(d, "MANIFEST.json")) and os.path.isdir(os.path.join(d, ".ufo")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    raise FreezeError("no ancestor of %s holds MANIFEST.json + .ufo/ (pass --repo)" % script_path)


def posix_rel(repo, path):
    return os.path.relpath(path, repo).replace(os.sep, "/")


def enumerate_reports(repo):
    """`.ufo/reports/round-*/*.md`, sorted -- mirrors the hand index's rel ordering."""
    out = []
    root = os.path.join(repo, ".ufo", "reports")
    if not os.path.isdir(root):
        return out
    for name in sorted(os.listdir(root)):
        rd = os.path.join(root, name)
        if not os.path.isdir(rd) or not ROUND_DIR_RE.match(name):
            continue
        for fname in sorted(os.listdir(rd)):
            if fname.endswith(".md") and os.path.isfile(os.path.join(rd, fname)):
                rel = posix_rel(repo, os.path.join(rd, fname))
                if RE_REPORT_REL.match(rel):
                    out.append(rel)
    return sorted(out)


def enumerate_prompts(repo):
    """`.ufo/prompts/<lane>-round-N.md` for every lane id the grammar can read.

    Inclusion is the lane-id grammar alone (`LANE_ID_RE`, the checker's own): a lane minted
    mid-round makes its prompt file a snapshot row the round it is dispatched, instead of
    being filtered out by membership in a hard-coded roster.
    """
    out = []
    root = os.path.join(repo, ".ufo", "prompts")
    if not os.path.isdir(root):
        return out
    for name in sorted(os.listdir(root)):
        if RE_PROMPT.match(name) and os.path.isfile(os.path.join(root, name)):
            out.append(".ufo/prompts/" + name)
    return sorted(out)


def tracked_paths(repo, rels):
    """One `git ls-files` call for the whole candidate set."""
    if not rels:
        return set()
    code, out = git(repo, ["ls-files", "-z", "--"] + rels)
    if code != 0:
        return set()
    return set(p for p in out.split("\0") if p)


def add_commit_time(repo, rel):
    """The add-commit committer time -- `git log -1 --diff-filter=A --format=%cI -- <rel>`."""
    code, out = git(repo, ["log", "-1", "--diff-filter=A", "--format=%cI", "--", rel])
    if code != 0:
        return None
    return iso_dt(out.strip()) if out.strip() else None


def mtime_of(path):
    try:
        return datetime.fromtimestamp(os.path.getmtime(path)).astimezone()
    except OSError:
        return None


def index_rows(repo, closed, rels, graded):
    """Rows present at `closed`: (tracked, landed_at, bytes, has_hash, has_shonen) per rel.

    `tracked` is 1 only when the file was committed at C (add-commit time <= C);
    a file that exists on disk at C but was committed later is present with
    `tracked=0, landed_at=-`, which is what the committed round-12 snapshots pin.
    """
    tracked = tracked_paths(repo, rels)
    rows = []
    for rel in rels:
        landed_at = None
        if rel in tracked:
            add = add_commit_time(repo, rel)
            if add is not None and le(add, closed):
                landed_at = add
        if landed_at is None:
            mt = mtime_of(os.path.join(repo, rel))
            if mt is None or not le(mt, closed):
                continue
        row = {"rel": rel, "tracked": 1 if landed_at is not None else 0,
               "landed_at": landed_at.isoformat() if landed_at is not None else "-"}
        if graded:
            text = read_text(os.path.join(repo, rel))
            row["bytes"] = os.path.getsize(os.path.join(repo, rel))
            row["has_hash"] = 1 if RE_HASH_RUN.search(text) else 0
            row["has_shonen"] = 1 if RE_SHONEN.search(text) else 0
        rows.append(row)
    return rows


def reports_index_text(rows):
    return "".join("%s\t%d\t%d\t%d\t%d\t%s\n" % (
        r["rel"], r["bytes"], r["tracked"], r["has_hash"], r["has_shonen"], r["landed_at"])
        for r in rows)


def prompts_index_text(rows):
    return "".join("%s\n" % r["rel"] for r in rows)


def kept_log_lines(repo, closed):
    """Lines whose leading ISO timestamp parses and is <= C, order and bytes preserved."""
    path = os.path.join(repo, ".ufo", "watchdog.log")
    if not os.path.isfile(path):
        raise FreezeError("no watchdog log at %s" % path)
    kept, dropped = [], 0
    for line in read_text(path).splitlines():
        head = line.split(" ", 1)[0]
        dt = iso_dt(head)
        if dt is not None and le(dt, closed):
            kept.append(line)
        else:
            dropped += 1
    return kept, dropped


def counters_text(kept):
    """Highest `launch`/`steer` round per lane among the kept lines, lanes sorted by id.

    Every lane the grammar reads gets a counter row -- the fixed roster is not consulted.
    `wrap <lane> round=N complete` is preserved verbatim in watchdog.log (it is kept, not
    rewritten) but is not a dispatch verb, so it never raises a counter: counters are
    launch/steer evidence only.
    """
    best = {}
    for line in kept:
        m = RE_DISPATCH.match(line)
        if not m:
            continue
        lane, n = m.group(3), int(m.group(4))
        best[lane] = max(best.get(lane, 0), n)
    return "".join("%s\t%d\n" % (lane, best[lane]) for lane in sorted(best))


def main_head(repo, closed):
    """Newest commit with committer time <= C, short-hashed; '-' when undecidable."""
    code, out = git(repo, ["rev-list", "-1", "--before=" + closed.isoformat(), "HEAD"])
    if code != 0:
        return "-"
    return (out.strip() or "-")[:7]


def manifest_blob(repo, args):
    """(bytes, source_label) for the pinned rounds[] blob -- always byte-for-byte."""
    if args.manifest_file:
        path = os.path.abspath(args.manifest_file)
        return read_bytes(path), ["manifest-file", path]
    if args.manifest_source == "git":
        if not args.git_ref:
            raise FreezeError("--manifest-source git requires --git-ref REF")
        code, data = git(repo, ["show", args.git_ref + ":MANIFEST.json"], binary=True)
        if code != 0:
            raise FreezeError("git show %s:MANIFEST.json failed in %s" % (args.git_ref, repo))
        return data, ["git-ref", args.git_ref]
    return read_bytes(os.path.join(repo, "MANIFEST.json")), ["live", "MANIFEST.json"]


def manifest_rounds(blob):
    try:
        doc = json.loads(blob.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise FreezeError("pinned MANIFEST.json is not JSON: %s" % exc)
    rounds = doc.get("rounds")
    if not isinstance(rounds, list):
        raise FreezeError("pinned MANIFEST.json has no rounds[] list")
    return rounds


# ------------------------------------------------------------------- expected.json

def canon_debt(rows):
    """The checker's `_canon_debt` unit: (lane, lane_round, class) triples, deterministic order.

    `lane_round` may be null: the round-15 checker emits lane-less findings -- its
    `history_pin_*` classes carry `lane="-"`, `lane_round=None` -- and copies both fields into
    the compared triple verbatim, so a pinned baseline has to be able to carry them too.
    Ordering is lexical by lane id and carries no base-roster order: the frozen schema does not
    compare sequence (`_compare_baseline` matches rows as a set).
    """
    out = []
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("lane"), str):
            raise FreezeError("debt row is not an object with a lane id: %r" % (row,))
        n = row.get("lane_round")
        if n is not None and (not isinstance(n, int) or isinstance(n, bool)):
            raise FreezeError("debt row has no integer-or-null lane_round: %r" % (row,))
        cls = row.get("class")
        if not isinstance(cls, str):
            raise FreezeError("debt row has no string class: %r" % (row,))
        out.append({"lane": row["lane"], "lane_round": n, "class": cls})
    return sorted(out, key=lambda r: (r["lane"],
                                      -1 if r["lane_round"] is None else r["lane_round"],
                                      r["class"]))


def parse_expected_debt(text):
    try:
        doc = json.loads(text)
    except ValueError as exc:
        raise FreezeError("--expected-debt is not JSON: %s" % exc)
    if isinstance(doc, dict) and "debt" in doc:
        doc = doc["debt"]
    if not isinstance(doc, list):
        raise FreezeError("--expected-debt must be a JSON list of {lane,lane_round,class}")
    return canon_debt(doc)


def expected_json_text(exit_code, debt):
    return json.dumps({"exit": exit_code, "debt": debt}, indent=1) + "\n"


def with_input_digests(expected_text, files):
    """Pin the snapshot's own inputs inside expected.json.

    The checker verifies these digests *before* it compares verdicts, so editing a snapshot's
    MANIFEST.json or watchdog.log reads `snapshot_tampered` (exit 2) instead of a green
    `baseline: match` -- the hole labrat H2 measured in the round-12 baselines, which pin only
    the debt set. `expected.json` and the derived-run note are excluded: they are the claim,
    not an input."""
    doc = json.loads(expected_text)
    doc["inputs"] = {name: hashlib.sha256(data).hexdigest()
                     for name, data in sorted(files.items())
                     if name not in ("expected.json", DERIVED_NOTE, "DERIVED-FROM-LIVE-RUN.txt")}
    return json.dumps(doc, indent=1, sort_keys=True) + "\n"


# --------------------------------------------------- frozen-projection derivation

def clear_stale_claim(out):
    """Drop a stale producer-owned claim from a rewritten output directory.

    A rewritten snapshot must not keep the previous expected.json or derived note:
    the frozen replay would compare against stale input digests, and a stale note would
    misdescribe the new baseline.  Only the given output directory is touched."""
    for name in ("expected.json", DERIVED_NOTE, "DERIVED-FROM-LIVE-RUN.txt"):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)


def run_checker_frozen(repo, snapshot, checker):
    """The checker's OWN frozen analysis of this snapshot.

    The snapshot is a flat directory and `closure-check.py --frozen` reads it directly
    (`load_frozen`, closure-check.py:429-473), so this is the analysis of the very bytes
    that will be replayed -- no mirror, no git index, no live-only check.  The snapshot is
    named by `--frozen-root <parent> --frozen <name>`: an absolute root resolves the
    snapshot by path, so a bare name can never be ambiguous across wave roots
    (`_resolve_frozen`, closure-check.py:1085-1090).

    Returns the run's command, the CLI exit code, the debt rows, the could-not-evaluate
    rows and the checker's own result dict.  The CLI exit is 3 ("no-baseline") while the
    snapshot carries no expected.json yet, so the baseline exit is computed from the
    analysis, never from that code."""
    if not os.path.isfile(checker):
        raise FreezeError("no checker at %s" % checker, EXIT_CHECKER)
    cmd = [sys.executable, checker, "--repo", repo,
           "--frozen-root", os.path.dirname(snapshot),
           "--frozen", os.path.basename(snapshot),
           "--json", "--no-citations"]
    try:
        done = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    except (OSError, subprocess.SubprocessError) as exc:
        raise FreezeError("checker invocation failed: %s" % exc, EXIT_CHECKER)
    try:
        result = json.loads(done.stdout)
    except ValueError as exc:
        raise FreezeError("checker did not emit JSON (%s): %s | stderr: %s"
                          % (exc, done.stdout[:400], done.stderr[-400:]), EXIT_CHECKER)
    if not isinstance(result, dict):
        raise FreezeError("checker did not return an analysis object: %s | stderr: %s"
                          % (done.stdout[:400], done.stderr[-400:]), EXIT_CHECKER)
    if result.get("verdict") == "error":
        raise FreezeError("checker refused the snapshot: %s" % result.get("error"), EXIT_CHECKER)
    # the projection is the analysis: both lists must be there.  A missing list is not an
    # empty one -- an incomplete result would project as a clean zero.
    for key in ("debt", "could_not_evaluate"):
        if not isinstance(result.get(key), list):
            raise FreezeError("checker result carries no %s list: %s | stderr: %s"
                              % (key, done.stdout[:400], done.stderr[-400:]), EXIT_CHECKER)
    verdict = result.get("verdict")
    if verdict not in ("ok", "debt", "could-not-evaluate", "no-baseline"):
        raise FreezeError("checker returned an unsupported verdict %r" % (verdict,), EXIT_CHECKER)
    reported_exit = result.get("exit")
    if not isinstance(reported_exit, int) or isinstance(reported_exit, bool):
        raise FreezeError("checker result carries no exit code: %s" % done.stdout[:400],
                          EXIT_CHECKER)
    if done.returncode != reported_exit:
        raise FreezeError("checker exited %d but reported exit %d" % (done.returncode, reported_exit),
                          EXIT_CHECKER)
    # the exit must be the frozen mode's own: a baseline-less snapshot answers 3
    # ("no-baseline"), otherwise it is the analysis exit (debt -> 1, else
    # could-not-evaluate -> 2, else 0).  A mismatch means the run is not the analysis
    # it claims to be, and a baseline is then refused rather than written.
    analysis_exit = (PROJECT_EXIT_DEBT if result["debt"]
                     else (PROJECT_EXIT_CNE if result["could_not_evaluate"] else PROJECT_EXIT_OK))
    if verdict == "no-baseline":
        if reported_exit != EXIT_NOBASELINE:
            raise FreezeError("checker answered verdict no-baseline with exit %d" % reported_exit,
                              EXIT_CHECKER)
    elif reported_exit != analysis_exit:
        raise FreezeError("checker answered verdict %s with exit %d, the analysis says %d"
                          % (verdict, reported_exit, analysis_exit), EXIT_CHECKER)
    return {
        "cmd": cmd,
        "cli_exit": reported_exit,
        "process_exit": done.returncode,
        "debt": canon_debt(result["debt"]),
        "cne": result["could_not_evaluate"],
        "analysis_exit": analysis_exit,
        "baseline_status": (result.get("baseline") or {}).get("status"),
        "baseline_inputs_status": (result.get("baseline_inputs") or {}).get("status"),
        "result": result,
    }


def default_checker(repo):
    """The round-15 checker the baselines are pinned against; this wave's copy as fallback."""
    committed = os.path.join(repo, DEFAULT_CHECKER)
    if os.path.isfile(committed):
        return committed
    return os.path.join(ROUND_15, "closure-check.py")




def derive_expected(repo, snapshot, checker, files):
    """Write expected.json from the checker's own frozen projection of this snapshot.

    The projection is the checker's analysis of the very bytes the snapshot holds
    (`--frozen-root <parent> --frozen <name>`), so the live-only classes -- the
    untracked-prompt rows and the history-pin row a materialized mirror used to
    manufacture -- cannot appear: frozen mode has neither check
    (closure-check.py:1402, :1011).

    `files` is the produced snapshot file list (what write_snapshot wrote): the digests
    pin exactly those inputs, never a leftover in the output directory.

    The baseline exit follows the checker's own precedence (debt -> 1, else
    could-not-evaluate -> 2, else 0), not the CLI's "no-baseline" 3, and expected.json
    pins the digests of the snapshot's own inputs, so an edited snapshot reads
    `snapshot_tampered` instead of a green match."""
    closed_line = ""
    for line in read_text(os.path.join(snapshot, "CLOSED_AT.txt")).splitlines():
        if line.startswith("closed_at\t"):
            closed_line = line.split("\t", 1)[1]
    run = run_checker_frozen(repo, snapshot, checker)
    debt = run["debt"]
    cne = run["cne"]
    exit_code = PROJECT_EXIT_DEBT if debt else (PROJECT_EXIT_CNE if cne else PROJECT_EXIT_OK)
    with open(os.path.join(snapshot, "expected.json"), "w", encoding="utf-8") as fh:
        fh.write(with_input_digests(expected_json_text(exit_code, debt), files))
    with open(os.path.join(snapshot, DERIVED_NOTE), "w", encoding="utf-8") as fh:
        fh.write("\n".join([
            DERIVED_MARKER,
            "closed_at\t%s" % closed_line,
            "projection\tnative frozen analysis of this snapshot (closure-check.py --frozen)",
            "command\t%s" % " ".join(run["cmd"]),
            "checker_exit\t%d" % run["cli_exit"],
            "checker_exit_note\t%d = %s" % (run["cli_exit"], CLI_EXIT_NAMES.get(run["cli_exit"], "unknown")),
            "projected_exit\t%d" % exit_code,
            "projected_exit_rule\tdebt -> 1, else could-not-evaluate -> 2, else 0",
            "scope\ta frozen projection cannot see prompt durability or the live history pin:",
            "scope\tthis baseline is a weaker verdict than a live run's, and it is self-pinning",
            "derived_debt\t%s" % json.dumps(debt, sort_keys=False),
            "warning\texpected.json pins the debt set of THIS projection; the baseline is only as good",
            "warning\tas that projection - re-check it, then pin --expected-exit/--expected-debt explicitly",
            "warning\tit is self-pinning: it pins the digests of the very inputs it was derived from",
        ]) + "\n")
    sys.stderr.write(
        "freeze-snapshot: %s -- expected.json came from the checker's own frozen\n"
        "freeze-snapshot: projection of this snapshot, not from a reviewed baseline. The\n"
        "freeze-snapshot: baseline is only as good as that projection.\n" % DERIVED_MARKER)
    return exit_code, debt


# ------------------------------------------------------------------------- emission

def snapshot_files(closed, manifest, rows_reports, rows_prompts, kept, counters, source,
                   main_head_value, expected_text, derived_note):
    files = {}
    files["MANIFEST.json"] = manifest
    files["watchdog.log"] = ("\n".join(kept) + "\n" if kept else "").encode("utf-8")
    files["reports-index.txt"] = reports_index_text(rows_reports).encode("utf-8")
    files["prompts-index.txt"] = prompts_index_text(rows_prompts).encode("utf-8")
    files["state-counters.txt"] = counters.encode("utf-8")
    lines = [
        "closed_at\t%s" % closed.isoformat(),
        "manifest_source\t%s" % " ".join(source),
        "main_HEAD\t%s" % main_head_value,
        "log_lines\t%d" % len(kept),
        "manifest_entries\t%d" % len(manifest_rounds(manifest)),
        "reports\t%d" % len(rows_reports),
        "prompts\t%d" % len(rows_prompts),
    ] + ["rule\t%s" % r for r in RULE_LINES]
    files["CLOSED_AT.txt"] = ("\n".join(lines) + "\n").encode("utf-8")
    if expected_text is not None:
        files["expected.json"] = with_input_digests(expected_text, files).encode("utf-8")
    if derived_note is not None:
        files[DERIVED_NOTE] = derived_note.encode("utf-8")
    return files


def check_out_dir(out, repo):
    """Refuse the wave dirs this generator must never write, and non-empty dirs."""
    real = os.path.realpath(out)
    for name in FORBIDDEN_OUT_DIRS:
        forbidden = os.path.realpath(os.path.join(repo, ".ufo", "waves", name))
        if real == forbidden or real.startswith(forbidden + os.sep):
            raise FreezeError("refusing to write inside %s (--out %s)" % (forbidden, out))
    return real


def write_snapshot(out, files, force):
    real = os.path.realpath(out)
    if os.path.isdir(out) and os.listdir(out) and not force:
        raise FreezeError("--out %s is not empty (pass --force to overwrite)" % out)
    os.makedirs(real, exist_ok=True)
    for name, data in sorted(files.items()):
        path = os.path.join(real, name)
        with open(path, "wb") as fh:
            fh.write(data)


# -------------------------------------------------------------------------- selftest

# Fixture instants: C is fixed; the "after C" commits/mtimes are the clock the fixture
# repo is actually built with, so no expected value is read back out of the code under test.
FX_CLOSED = "2025-12-31T23:00:00+00:00"
FX_LANDED_AT = "2025-12-31T21:00:00+00:00"
FX_UNTRACKED_MTIME = "2025-12-31T22:00:00+00:00"
FX_REPORT_1 = "# kagi round 1\ncommit abc1234\n## SHONEN\n"      # 35 B, has_hash + has_shonen
FX_REPORT_3 = "plain untracked report, no hash and no heading\n"  # 44 B, neither
# Lines <= C.  `kama` and `kagi-x2` are named by no roster row and by no base lane list, so a
# generator that filters on a fixed list drops them and fails these checks.  `kiri` exists only
# as a `wrap` line: a wrap verb that leaked into the counters would show up as `kiri 4`.
FX_LOG_LINES = [
    "2025-12-31T22:58:00+00:00 launch kama round=1",
    "2025-12-31T22:58:20+00:00 wrap kiri round=4 complete; NOT respawning (fleet-wrap)",
    "2025-12-31T22:58:30+00:00 launch kagi-x2 round=1",
    "2025-12-31T22:59:59+00:00 launch kagi round=1",
    "2025-12-31T23:00:00+00:00 steer kagi -> round 2",
]
FX_LOG_POST_C = "2025-12-31T23:00:01+00:00 launch kagi round=3"
# The prompt rels present at C, in the order prompts-index.txt must carry them.
FX_PROMPTS_PRESENT = [
    ".ufo/prompts/kagi-round-1.md",
    ".ufo/prompts/kagi-x2-round-1.md",
    ".ufo/prompts/kama-round-1.md",
]


def _fixture_git(repo, args, dates=None):
    env = dict(GIT_ENV)
    env.update({
        "GIT_AUTHOR_NAME": "fixture", "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
        "GIT_COMMITTER_NAME": "fixture", "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
    })
    if dates:
        env["GIT_AUTHOR_DATE"] = dates
        env["GIT_COMMITTER_DATE"] = dates
    done = subprocess.run(["git", "-C", repo] + args, capture_output=True, text=True, env=env)
    if done.returncode != 0:
        raise FreezeError("fixture git %s failed: %s" % (" ".join(args), done.stderr.strip()))
    return done.stdout


def build_fixture(tmp_root):
    repo = os.path.join(tmp_root, "repo")
    os.makedirs(os.path.join(repo, ".ufo"), exist_ok=True)
    for sub in ("reports/round-1", "reports/round-2", "reports/round-3", "reports/round-4", "prompts"):
        os.makedirs(os.path.join(repo, ".ufo", sub), exist_ok=True)
    _fixture_git(repo, ["init", "-q"])
    with open(os.path.join(repo, "MANIFEST.json"), "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"version": 1, "repo": "fixture", "roster": [{"id": "kagi"}],
                             "rounds": [{"round": 1, "date": "2025-12-31", "type": "closure",
                                         "closed_at": FX_CLOSED, "lanes": {"kagi": "ok"}}]}, indent=1))
    with open(os.path.join(repo, ".ufo", "watchdog.log"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(FX_LOG_LINES + [FX_LOG_POST_C]) + "\n")
    # round-1: committed at 21:00 (<= C) -> present, landed.
    with open(os.path.join(repo, ".ufo/reports/round-1/kagi.md"), "w", encoding="utf-8") as fh:
        fh.write(FX_REPORT_1)
    # round-2: committed now (>> C) -> excluded.
    with open(os.path.join(repo, ".ufo/reports/round-2/kagi.md"), "w", encoding="utf-8") as fh:
        fh.write("# kagi round 2\ncommit abc1234\n")
    # round-3: never committed, mtime 22:00 (<= C) -> present, unlanded.
    with open(os.path.join(repo, ".ufo/reports/round-3/kagi.md"), "w", encoding="utf-8") as fh:
        fh.write(FX_REPORT_3)
    # round-4: never committed, mtime now (>> C) -> excluded.
    with open(os.path.join(repo, ".ufo/reports/round-4/kagi.md"), "w", encoding="utf-8") as fh:
        fh.write("# kagi round 4\n")
    for name in ("kagi-round-1.md", "kama-round-1.md"):
        with open(os.path.join(repo, ".ufo", "prompts", name), "w", encoding="utf-8") as fh:
            fh.write(FX_REPORT_1)
    # never committed, mtime 22:00 (<= C): present through the mtime leg, unlanded
    with open(os.path.join(repo, ".ufo/prompts/kagi-x2-round-1.md"), "w", encoding="utf-8") as fh:
        fh.write("# prompt kagi-x2 round 1\n")
    # never committed, mtime now (>> C): excluded by presence whatever its lane id
    with open(os.path.join(repo, ".ufo/prompts/kagi-round-5.md"), "w", encoding="utf-8") as fh:
        fh.write("# prompt kagi round 5\n")
    # on disk at C, but its lane token is outside the lane-id grammar: not a lane this
    # generator may claim (closure-check.py would call it an unreadable lane id, A:42)
    with open(os.path.join(repo, ".ufo/prompts/Kama-round-9.md"), "w", encoding="utf-8") as fh:
        fh.write("# prompt Kama.1 round 9\n")
    _fixture_git(repo, ["add", "--", ".ufo/reports/round-1/kagi.md", ".ufo/prompts/kagi-round-1.md",
                        ".ufo/prompts/kama-round-1.md"])
    _fixture_git(repo, ["commit", "-q", "-m", "fixture: backdated landing"], dates=FX_LANDED_AT)
    _fixture_git(repo, ["add", "--", ".ufo/reports/round-2/kagi.md"])
    _fixture_git(repo, ["commit", "-q", "-m", "fixture: post-C landing"])
    for rel in (".ufo/reports/round-3/kagi.md", ".ufo/prompts/kagi-x2-round-1.md",
                ".ufo/prompts/Kama-round-9.md"):
        os.utime(os.path.join(repo, rel),
                 (datetime.fromisoformat(FX_UNTRACKED_MTIME).timestamp(),) * 2)
    return repo


def _emit(repo, out, closed, expected_text=None):
    closed_dt = iso_dt(closed)
    manifest, source = manifest_blob(repo, argparse.Namespace(manifest_file=None,
                                                              manifest_source="live", git_ref=None))
    rows_reports = index_rows(repo, closed_dt, enumerate_reports(repo), graded=True)
    rows_prompts = index_rows(repo, closed_dt, enumerate_prompts(repo), graded=False)
    kept, _ = kept_log_lines(repo, closed_dt)
    return snapshot_files(closed_dt, manifest, rows_reports, rows_prompts, kept,
                          counters_text(kept), source, main_head(repo, closed_dt),
                          expected_text, None)


def run_selftest():
    checks = []

    def check(name, got, want):
        checks.append((name, got == want, got, want))

    def call(fn, *a, **kw):
        """Pure helper -> value, with a refusal reported as its message instead of aborting.

        A generator that refuses an input the checker really emits must show up as one named
        FAIL, not as a selftest that dies before it prints anything.
        """
        try:
            return fn(*a, **kw)
        except FreezeError as exc:
            return "refused: %s" % exc

    tmp_root = tempfile.mkdtemp(prefix="freeze-selftest-")
    try:
        if os.path.realpath(tmp_root).startswith(os.path.realpath(walk_up_repo(SCRIPT)) + os.sep):
            raise FreezeError("temp dir %s is inside the repo; refusing to run the selftest" % tmp_root)
        fixture = build_fixture(tmp_root)
        # the fixture must not be a repo the walk-up default would mistake for the real one
        out = os.path.join(tmp_root, "snapshot")
        files = _emit(fixture, out, FX_CLOSED,
                      expected_text=expected_json_text(0, canon_debt([])))
        check("file-set",
              sorted(files),
              ["CLOSED_AT.txt", "MANIFEST.json", "expected.json", "prompts-index.txt",
               "reports-index.txt", "state-counters.txt", "watchdog.log"])
        # log boundary: the line exactly at C is kept, the one second after is dropped, and
        # every kept line survives byte-for-byte -- the `wrap ... complete` verb included
        check("log-boundary", files["watchdog.log"].decode(), "\n".join(FX_LOG_LINES) + "\n")
        check("log-exclude-post-C", FX_LOG_POST_C in files["watchdog.log"].decode(), False)
        check("log-wrap-verbatim", FX_LOG_LINES[1] in files["watchdog.log"].decode(), True)
        # landed_at / presence rule
        check("reports-index", files["reports-index.txt"].decode(),
              ".ufo/reports/round-1/kagi.md\t%d\t1\t1\t1\t%s\n"
              ".ufo/reports/round-3/kagi.md\t%d\t0\t0\t0\t-\n" % (
                  len(FX_REPORT_1.encode()), FX_LANDED_AT, len(FX_REPORT_3.encode())))
        check("reports-exclude-post-C", ".ufo/reports/round-2/kagi.md" in files["reports-index.txt"].decode(), False)
        check("reports-exclude-post-C-untracked", ".ufo/reports/round-4/kagi.md" in files["reports-index.txt"].decode(), False)
        # the lane universe is the lane-id grammar, not a roster: `kama` is off-roster and
        # `kagi-x2` is a hyphenated sibling, and both are prompt rows a fixed list would drop
        check("prompts-index", files["prompts-index.txt"].decode(),
              "".join(p + "\n" for p in FX_PROMPTS_PRESENT))
        check("prompts-off-roster-lane-captured",
              ".ufo/prompts/kama-round-1.md" in files["prompts-index.txt"].decode(), True)
        check("prompts-hyphen-lane-captured",
              ".ufo/prompts/kagi-x2-round-1.md" in files["prompts-index.txt"].decode(), True)
        check("prompts-exclude-post-C",
              ".ufo/prompts/kagi-round-5.md" in files["prompts-index.txt"].decode(), False)
        check("prompts-exclude-unreadable-lane-id",
              ".ufo/prompts/Kama-round-9.md" in files["prompts-index.txt"].decode(), False)
        # ...and the same two lanes carry counters, while a wrap-only lane carries none
        check("counters", files["state-counters.txt"].decode(), "kagi\t2\nkagi-x2\t1\nkama\t1\n")
        check("counters-off-roster-lane-captured",
              "kama\t1\n" in files["state-counters.txt"].decode(), True)
        check("counters-hyphen-lane-captured",
              "kagi-x2\t1\n" in files["state-counters.txt"].decode(), True)
        check("counters-exclude-wrap-only-lane", "kiri" in files["state-counters.txt"].decode(), False)
        # debt triples are the compared unit; the order is lexical and carries no roster order
        check("canon-debt-lexical-order",
              [r["lane"] for r in canon_debt([
                  {"lane": "protocol", "lane_round": 1, "class": "stale_in_flight"},
                  {"lane": "kagi", "lane_round": 2, "class": "stale_in_flight"}])],
              ["kagi", "protocol"])
        # the round-15 checker also emits lane-less findings (`history_pin_*`, lane_round None):
        # the compared triple carries them, so the pinned unit must round-trip them
        check("canon-debt-lane-less-row",
              call(canon_debt, [{"lane": "kama", "lane_round": 2, "class": "stale_in_flight"},
                                {"lane": "-", "lane_round": None, "class": "history_pin"}]),
              [{"lane": "-", "lane_round": None, "class": "history_pin"},
               {"lane": "kama", "lane_round": 2, "class": "stale_in_flight"}])
        check("expected-debt-lane-less-row",
              call(parse_expected_debt, '[{"lane": "-", "lane_round": null, "class": "history_pin"}]'),
              [{"lane": "-", "lane_round": None, "class": "history_pin"}])
        try:
            canon_debt([{"lane": "kama", "lane_round": "2", "class": "stale_in_flight"}])
            check("canon-debt-rejects-non-integer-round", "accepted", "refused")
        except FreezeError:
            check("canon-debt-rejects-non-integer-round", "refused", "refused")
        closed_lines = dict(l.split("\t", 1) for l in files["CLOSED_AT.txt"].decode().splitlines()
                            if l.startswith(("closed_at", "log_lines", "manifest_entries",
                                             "reports", "prompts", "main_HEAD", "manifest_source")))
        check("closed-at-line", closed_lines["closed_at"], FX_CLOSED)
        check("closed-at-log-lines", closed_lines["log_lines"], "5")
        check("closed-at-entries", closed_lines["manifest_entries"], "1")
        check("closed-at-reports", closed_lines["reports"], "2")
        check("closed-at-prompts", closed_lines["prompts"], "3")
        check("closed-at-source", closed_lines["manifest_source"], "live MANIFEST.json")
        exp_doc = json.loads(files["expected.json"].decode())
        check("expected-json-exit-debt", [exp_doc["exit"], exp_doc["debt"]], [0, []])
        check("expected-json-inputs", sorted(exp_doc["inputs"]),
              ["CLOSED_AT.txt", "MANIFEST.json", "prompts-index.txt",
               "reports-index.txt", "state-counters.txt", "watchdog.log"])
        check("expected-json-input-digest", exp_doc["inputs"]["MANIFEST.json"],
              hashlib.sha256(files["MANIFEST.json"]).hexdigest())
        # the derived baseline is the checker's OWN frozen projection of the snapshot it
        # was written for: the fixture's own contract (exit 0, no debt), no live-only rows
        # (prompt_untracked, history_pin -- a materialized mirror used to manufacture one
        # per prompt), exactly the six produced inputs pinned, a native replay that reads
        # the baseline back as a match, and a --force rewrite that regenerates the baseline
        # instead of inheriting a stale claim or a stale note
        derived_out = os.path.join(tmp_root, "snapshot-derived")
        derived_files = dict(files)
        derived_files.pop("expected.json", None)
        write_snapshot(derived_out, derived_files, force=True)
        checker_path = default_checker(fixture)
        contract = (exp_doc["exit"], exp_doc["debt"])
        expected_inputs = {name: hashlib.sha256(data).hexdigest()
                           for name, data in sorted(derived_files.items())
                           if name not in ("expected.json", DERIVED_NOTE)}
        with open(os.path.join(derived_out, "expected.json"), "w", encoding="utf-8") as fh:
            fh.write(json.dumps({"exit": 7, "debt": [{"lane": "stale", "lane_round": 1,
                                                       "class": "stale"}]}, indent=1) + "\n")
        write_snapshot(derived_out, derived_files, force=True)   # the --force rewrite
        clear_stale_claim(derived_out)
        derived = call(derive_expected, fixture, derived_out, checker_path, derived_files)
        if isinstance(derived, str):
            check("derived-frozen-projection", derived, "a projected baseline")
        else:
            replay = call(run_checker_frozen, fixture, derived_out, checker_path)
            if isinstance(replay, str):
                check("derived-frozen-projection", replay, "a replayable baseline")
            else:
                doc = json.loads(read_text(os.path.join(derived_out, "expected.json")))
                inputs = doc.get("inputs") or {}
                observed = {
                    "exit_is_the_fixture_contract": doc["exit"] == contract[0],
                    "debt_is_the_fixture_contract": doc["debt"] == contract[1],
                    "no_live_only_rows": not [row for row in doc["debt"]
                                              if row.get("class") in LIVE_ONLY_CLASSES],
                    "inputs_are_the_six_produced_files": sorted(inputs) == sorted(expected_inputs),
                    "inputs_digest_every_file": all(inputs.get(name) == digest
                                                     for name, digest in expected_inputs.items()),
                    "replay_baseline_matches": replay["baseline_status"] == "match",
                    "replay_inputs_match": replay["baseline_inputs_status"] == "match",
                    "replay_exit_is_the_pinned_exit": replay["cli_exit"] == doc["exit"],
                }
                check("derived-frozen-projection", observed,
                      {name: True for name in observed})
        check("manifest-verbatim", files["MANIFEST.json"], read_bytes(os.path.join(fixture, "MANIFEST.json")))
        # refusals: the read-only wave dirs, then a non-empty --out without --force
        for name in ("round-11", "round-12", "round-13"):
            path = os.path.join(fixture, ".ufo", "waves", name, "snap")
            try:
                check_out_dir(path, fixture)
                check("refuse-%s" % name, "accepted", "refused")
            except FreezeError as exc:
                check("refuse-%s" % name, "inside" in str(exc), True)
        # ...while this generator's own wave is exactly where --out is meant to land
        try:
            check_out_dir(os.path.join(fixture, ".ufo", "waves", "round-15", "frozen", "pre"), fixture)
            check("permit-round-15-frozen", "accepted", "accepted")
        except FreezeError as exc:
            check("permit-round-15-frozen", "refused: %s" % exc, "accepted")
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, "leftover.txt"), "w", encoding="utf-8") as fh:
            fh.write("a previous run's file\n")
        try:
            write_snapshot(out, files, force=False)
            check("refuse-nonempty", "accepted", "refused")
        except FreezeError as exc:
            check("refuse-nonempty", "not empty" in str(exc), True)
        write_snapshot(out, files, force=True)
        check("force-overwrite", sorted(os.listdir(out)), sorted(set(files) | {"leftover.txt"}))
        # the written snapshot must be readable by the corpus it is written for
        closed_dt = iso_dt(FX_CLOSED)
        check("round-trip-report-row",
              [r["rel"] for r in index_rows(fixture, closed_dt, enumerate_reports(fixture), True)],
              [".ufo/reports/round-1/kagi.md", ".ufo/reports/round-3/kagi.md"])
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)

    passed = sum(1 for c in checks if c[1])
    for name, ok, got, want in checks:
        print("%-34s %s" % (name, "pass" if ok else "FAIL"))
        if not ok:
            print("    got:  %r" % (got,))
            print("    want: %r" % (want,))
    print("selftest: %d/%d checks passed" % (passed, len(checks)))
    return passed == len(checks)


# ------------------------------------------------------------------------------- cli

def build_parser():
    p = argparse.ArgumentParser(
        description="Deterministic generator for the closure gate's frozen baselines "
                    "(read-only over the repo; writes only --out).",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--repo", default=None,
                   help="repo root (default: nearest ancestor of this script holding MANIFEST.json + .ufo/)")
    p.add_argument("--closed-at", metavar="ISO8601", default=None,
                   help="the instant C the snapshot is pinned to (required unless --selftest)")
    p.add_argument("--manifest-source", choices=("live", "git"), default="live",
                   help="which rounds[] blob the snapshot pins (default: live MANIFEST.json)")
    p.add_argument("--git-ref", metavar="REF", default=None,
                   help="with --manifest-source git: `git show REF:MANIFEST.json`")
    p.add_argument("--manifest-file", metavar="PATH", default=None,
                   help="pin the blob from an arbitrary file instead of --manifest-source")
    p.add_argument("--out", metavar="DIR", default=None,
                   help="snapshot directory to create (required unless --selftest)")
    p.add_argument("--expected-exit", metavar="N", type=int, default=None,
                   help="pin the baseline exit code (with --expected-debt)")
    p.add_argument("--expected-debt", metavar="JSON", default=None,
                   help='pin the baseline debt set, e.g. \'[{"lane":"kagi","lane_round":12,"class":"stale_in_flight"}]\'')
    p.add_argument("--checker", metavar="PATH", default=None,
                   help="checker used by the derived baseline (default: %s)" % DEFAULT_CHECKER)
    p.add_argument("--force", action="store_true", help="write into a non-empty --out")
    p.add_argument("--selftest", action="store_true",
                   help="run over fixture inputs this script creates in a temp dir; never touches the repo")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.selftest:
        try:
            return EXIT_OK if run_selftest() else EXIT_SELFTEST
        except FreezeError as exc:
            return die(str(exc), EXIT_SELFTEST)

    if not args.closed_at:
        return die("--closed-at is required")
    if not args.out:
        return die("--out is required")
    if args.manifest_file and (args.git_ref or args.manifest_source != "live"):
        return die("--manifest-file is exclusive with --manifest-source/--git-ref")
    if (args.expected_exit is None) != (args.expected_debt is None):
        return die("--expected-exit and --expected-debt must be given together")
    closed = iso_dt(args.closed_at)
    if closed is None:
        return die("--closed-at is not ISO8601: %s" % args.closed_at)

    try:
        repo = os.path.abspath(args.repo) if args.repo else walk_up_repo(SCRIPT)
        if not os.path.isfile(os.path.join(repo, "MANIFEST.json")):
            raise FreezeError("no MANIFEST.json under %s (pass --repo)" % repo)
        check_out_dir(args.out, repo)

        manifest, source = manifest_blob(repo, args)
        rows_reports = index_rows(repo, closed, enumerate_reports(repo), graded=True)
        rows_prompts = index_rows(repo, closed, enumerate_prompts(repo), graded=False)
        kept, dropped = kept_log_lines(repo, closed)
        files = snapshot_files(closed, manifest, rows_reports, rows_prompts, kept,
                               counters_text(kept), source, main_head(repo, closed), None, None)
        write_snapshot(args.out, files, args.force)
        out_real = os.path.realpath(args.out)
        # A rewritten --out must not keep the previous producer-owned claim: comparisons
        # would use old input digests and a stale derived note would misdescribe the baseline.
        # Only this --out is touched, after check_out_dir has vetted it.
        clear_stale_claim(out_real)

        if args.expected_exit is not None:
            text = with_input_digests(
                expected_json_text(args.expected_exit, parse_expected_debt(args.expected_debt)), files)
            with open(os.path.join(out_real, "expected.json"), "w", encoding="utf-8") as fh:
                fh.write(text)
            exit_code, debt = args.expected_exit, parse_expected_debt(args.expected_debt)
        else:
            checker = args.checker or default_checker(repo)
            exit_code, debt = derive_expected(repo, out_real, checker, files)
    except FreezeError as exc:
        return die(str(exc), exc.code or EXIT_USAGE)

    print("freeze-snapshot: %s" % out_real)
    print("  closed_at\t%s" % closed.isoformat())
    print("  manifest_source\t%s" % " ".join(source))
    print("  main_HEAD\t%s" % main_head(repo, closed))
    print("  log_lines\t%d kept, %d dropped (> closed_at or unparsable)" % (len(kept), dropped))
    print("  reports\t%d\tprompts\t%d" % (len(rows_reports), len(rows_prompts)))
    print("  expected\t%s\tdebt rows\t%d\texit\t%d" % (
        "pinned" if args.expected_exit is not None else "derived from the checker's frozen projection",
        len(debt), exit_code))
    return EXIT_OK


if __name__ == "__main__":
    try:
        sys.exit(main())
    except FreezeError as exc:            # pragma: no cover - defensive
        sys.exit(die(str(exc)))
    except BrokenPipeError:
        os._exit(0)