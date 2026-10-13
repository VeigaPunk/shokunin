#!/usr/bin/env python3
"""freeze-snapshot.py -- generator for the closure gate's frozen baselines.

`closure-check.py --frozen <NAME>` consumes a *flat* snapshot directory:
`MANIFEST.json`, `watchdog.log`, `reports-index.txt`, `prompts-index.txt`,
`state-counters.txt` (and an optional `expected.json` baseline).  The round-12
snapshots under `.ufo/waves/round-12/frozen/{pre,post-actual,post}/` were
assembled by hand from the prose in `frozen/README.md`; this script is that
prose expressed once, deterministically, so a round-13 baseline can be
re-derived instead of re-implemented.

READ-ONLY OVER THE REPO.  The only writes are inside `--out` (plus a scratch
staging tree under the system temp dir that is removed again).  Never written:
the repo, `.ufo/waves/round-11/**`, `.ufo/waves/round-12/**`, `MANIFEST.json`,
`.ufo/state/**`.

    python3 .ufo/waves/round-13/freeze-snapshot.py --selftest
    python3 .ufo/waves/round-13/freeze-snapshot.py \
        --closed-at 2026-09-28T21:30:00-03:00 --manifest-source live \
        --out /path/to/new/frozen/pre

Freezing rule (see `frozen/README.md` §"One freezing rule"; one instant `C`):

  watchdog.log       lines whose leading ISO timestamp is <= C, byte-for-byte.
  reports-index.txt  `.ufo/reports/round-*/*.md` present at C, as
                     `rel<TAB>bytes<TAB>tracked<TAB>has_hash<TAB>has_shonen<TAB>landed_at`
                     with `landed_at` = add-commit committer time, `-` when the
                     file was not committed at C.
  prompts-index.txt  `.ufo/prompts/<lane>-round-N.md` present at C, one rel per line.
  state-counters.txt highest `launch`/`steer` round per lane among the *kept* log lines.
  CLOSED_AT.txt      C, the manifest source, main_HEAD, the four counts, the rule.
  MANIFEST.json      the pinned `rounds[]` blob, byte-for-byte as sourced.

"Present at C" is: the add-commit committer time is <= C (landed, `tracked=1`), or
-- for a file not committed at C -- the on-disk mtime is <= C (`tracked=0`,
`landed_at=-`).  `has_hash`/`has_shonen` are the checker's own `_grade_file`
predicates (`RE_HASH_RUN` / `RE_SHONEN`) over the file's current content.

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
from datetime import datetime, timezone

SCRIPT = os.path.abspath(__file__)
ROUND_13 = os.path.dirname(SCRIPT)
WAVES_DIR = os.path.dirname(ROUND_13)

# The checker's roster order, copied from closure-check.py:57 (lane_sort key).
LANES = ["protocol", "aggregator", "kasegi", "kengaku", "kake", "kumitate", "kotoba", "kagi"]

# Copied from closure-check.py:65,71-74 -- the index columns are the frozen mirror of
# load_live()/_grade_file(), so the predicates must be the checker's, not lookalikes.
ROUND_DIR_RE = re.compile(r"^round-(.+)$")
RE_DISPATCH = re.compile(r"^(\S+) (launch|steer) ([a-z]+) (?:-> round |round=)(\d+)\b")
RE_HASH_RUN = re.compile(r"(?<![0-9a-fA-F])[0-9a-f]{7,}(?![0-9a-fA-F])")
RE_SHONEN = re.compile(r"^#{1,6}\s*SHONEN", re.M)
RE_PROMPT = re.compile(r"^([a-z]+)-round-(\d+)\.md$")
RE_REPORT_REL = re.compile(r"^\.ufo/reports/round-[^/]+/[^/]+\.md$")

# Verbatim from the hand-assembled round-12 CLOSED_AT.txt files.
RULE_LINES = [
    "watchdog.log = lines with timestamp <= closed_at; reports-index/prompts-index = files with",
    "mtime <= closed_at (landed_at = add-commit committer time, '-' when untracked);",
    "state-counters = highest launch/steer round per lane among the kept log lines",
    "main_HEAD = newest commit with committer time <= closed_at ('-' when git cannot answer)",
]

FORBIDDEN_OUT_DIRS = ("round-11", "round-12")
DEFAULT_CHECKER = os.path.join(".ufo", "waves", "round-12", "closure-check.py")

EXIT_OK, EXIT_SELFTEST, EXIT_USAGE, EXIT_CHECKER = 0, 1, 2, 3

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
    """`.ufo/prompts/<lane>-round-N.md` with lane in LANES (the checker's own filter)."""
    out = []
    root = os.path.join(repo, ".ufo", "prompts")
    if not os.path.isdir(root):
        return out
    for name in sorted(os.listdir(root)):
        m = RE_PROMPT.match(name)
        if m and m.group(1) in LANES and os.path.isfile(os.path.join(root, name)):
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
    """Highest launch/steer round per lane among the kept lines, lanes sorted by id."""
    best = {}
    for line in kept:
        m = RE_DISPATCH.match(line)
        if not m:
            continue
        lane, n = m.group(3), int(m.group(4))
        if lane in LANES:
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

def _lane_sort(lane):
    """Copied from closure-check.py:102 (_sorted_debt's key)."""
    return LANES.index(lane) if lane in LANES else len(LANES) + 1


def canon_debt(rows):
    """The checker's `_canon_debt`: (lane, lane_round, class) triples, `_sorted_debt` order."""
    out = []
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("lane"), str):
            raise FreezeError("debt row is not an object with a lane id: %r" % (row,))
        n = row.get("lane_round")
        if not isinstance(n, int) or isinstance(n, bool):
            raise FreezeError("debt row has no integer lane_round: %r" % (row,))
        cls = row.get("class")
        if not isinstance(cls, str):
            raise FreezeError("debt row has no string class: %r" % (row,))
        out.append({"lane": row["lane"], "lane_round": n, "class": cls})
    return sorted(out, key=lambda r: (_lane_sort(r["lane"]), r["lane_round"], r["class"]))


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
                     if name not in ("expected.json", "DERIVED-FROM-LIVE-RUN.txt")}
    return json.dumps(doc, indent=1, sort_keys=True) + "\n"


# --------------------------------------------------------------- live-run derivation

FAR_FUTURE = datetime(2999, 1, 1, tzinfo=timezone.utc)


def _synth_report(text_bytes, has_hash, has_shonen):
    """Bytes of exactly `text_bytes` length satisfying the pinned predicates.

    Live `_grade_file` grades the *content* (hash run / SHONEN heading) and the size; the
    mirror must reproduce both so the derived run sees the same rows as the snapshot does.
    """
    head = b""
    if has_shonen:
        head += b"## SHONEN\n"
    if has_hash:
        head += b"commit abc1234\n"
    if len(head) > text_bytes:
        return head[:text_bytes]
    return head + b"." * (text_bytes - len(head))


def stage_mirror(snapshot, closed):
    """Materialize a live-decodable tree from the flat snapshot (checker `--repo` layout).

    `closure-check.py --repo` cannot read a flat snapshot: its live loader wants
    `.ufo/watchdog.log` and grades worktree files (`load_live`, closure-check.py:216-254).
    The mirror is still built from the snapshot's own bytes -- the pinned sizes, the pinned
    hash/SHONEN flags, the pinned landed_at (as git-trackedness, which is the live
    loader's own landed predicate) -- and it is thrown away after the run.
    """
    stage = os.path.join(tempfile.gettempdir(), "freeze-stage-" + os.path.basename(snapshot.rstrip(os.sep)))
    if os.path.isdir(stage):
        shutil.rmtree(stage)
    for sub in (("",), (".ufo",), (".ufo", "reports"), (".ufo", "prompts"), (".ufo", "state")):
        os.makedirs(os.path.join(stage, *sub), exist_ok=True)
    shutil.copyfile(os.path.join(snapshot, "MANIFEST.json"), os.path.join(stage, "MANIFEST.json"))
    shutil.copyfile(os.path.join(snapshot, "watchdog.log"), os.path.join(stage, ".ufo", "watchdog.log"))

    landed = []
    for line in read_text(os.path.join(snapshot, "reports-index.txt")).splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 5:
            raise FreezeError("malformed reports-index.txt line: %r" % line)
        rel, nbytes, tracked, has_hash, has_shonen = parts[:5]
        dst = os.path.join(stage, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "wb") as fh:
            fh.write(_synth_report(int(nbytes), has_hash == "1", has_shonen == "1"))
        # mtimes are pinned far-future: the live loader's `report_seen_by` is the one place
        # mtime is read (closure-check.py:189-197) and the frozen loader always answers False
        # from a snapshot ("snapshots carry no mtimes"), so this reproduces frozen semantics.
        os.utime(dst, (FAR_FUTURE.timestamp(), FAR_FUTURE.timestamp()))
        if tracked == "1":
            landed.append(rel)
    for line in read_text(os.path.join(snapshot, "prompts-index.txt")).splitlines():
        rel = line.strip()
        if not rel:
            continue
        dst = os.path.join(stage, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8") as fh:
            fh.write("prompt (mirrored from prompts-index.txt)\n")
    for line in read_text(os.path.join(snapshot, "state-counters.txt")).splitlines():
        parts = line.split("\t")
        if len(parts) >= 2 and parts[1].strip().isdigit():
            with open(os.path.join(stage, ".ufo", "state", parts[0] + ".round"), "w",
                      encoding="utf-8") as fh:
                fh.write(parts[1].strip() + "\n")
    if git(stage, ["init", "-q"])[0] is None:
        raise FreezeError("git is not usable; the derived run needs a mirror git index")
    if landed:
        code, out = git(stage, ["add", "--"] + landed)
        if code != 0:
            raise FreezeError("mirror git add failed: %s" % out.strip())
    return stage


def default_checker(repo):
    """The round-12 checker the baselines are pinned against; this wave's copy as fallback."""
    committed = os.path.join(repo, DEFAULT_CHECKER)
    if os.path.isfile(committed):
        return committed
    return os.path.join(ROUND_13, "closure-check.py")


def run_checker(stage, checker):
    """The checker's live run over the mirror; (cmd, exit, debt triples) or FreezeError."""
    if not os.path.isfile(checker):
        raise FreezeError("no checker at %s" % checker, EXIT_CHECKER)
    cmd = [sys.executable, checker, "--repo", stage, "--no-citations", "--json"]
    try:
        done = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    except (OSError, subprocess.SubprocessError) as exc:
        raise FreezeError("checker invocation failed: %s" % exc, EXIT_CHECKER)
    try:
        result = json.loads(done.stdout)
    except ValueError as exc:
        raise FreezeError("checker did not emit JSON (%s): %s" % (exc, done.stdout[:400]), EXIT_CHECKER)
    if result.get("verdict") == "error":
        raise FreezeError("checker refused the mirror: %s" % result.get("error"), EXIT_CHECKER)
    return cmd, int(result.get("exit", -1)), canon_debt(result.get("debt") or [])


def derive_expected(snapshot, checker):
    """Write expected.json from a checker run over a mirror of this snapshot."""
    closed_line = ""
    for line in read_text(os.path.join(snapshot, "CLOSED_AT.txt")).splitlines():
        if line.startswith("closed_at\t"):
            closed_line = line.split("\t", 1)[1]
    stage = stage_mirror(snapshot, iso_dt(closed_line))
    try:
        cmd, exit_code, debt = run_checker(stage, checker)
        with open(os.path.join(snapshot, "expected.json"), "w", encoding="utf-8") as fh:
            fh.write(expected_json_text(exit_code, debt))
        with open(os.path.join(snapshot, "DERIVED-FROM-LIVE-RUN.txt"), "w", encoding="utf-8") as fh:
            fh.write("\n".join([
                "DERIVED-FROM-LIVE-RUN",
                "closed_at\t%s" % closed_line,
                "staging\t%s (removed after the run)" % stage,
                "command\t%s" % " ".join(cmd),
                "checker_exit\t%d" % exit_code,
                "mirror_rule\treports re-materialized at the pinned bytes/has_hash/has_shonen; mtimes far-future",
                "mirror_rule\tlanded_at != '-' staged in the mirror's git index; landed_at == '-' left untracked",
                "mirror_rule\tstate/*.round and prompts/ mirrored from the two indexes",
                "derived_debt\t%s" % json.dumps(debt, sort_keys=False),
                "warning\texpected.json pins the debt set of THIS run; the baseline is only as good",
                "warning\tas that run - re-check it, then pin --expected-exit/--expected-debt explicitly",
            ]) + "\n")
        sys.stderr.write(
            "freeze-snapshot: DERIVED-FROM-LIVE-RUN -- expected.json came from a checker run over a\n"
            "freeze-snapshot: materialized mirror of this snapshot (%s), not from a reviewed\n"
            "freeze-snapshot: baseline. The baseline is only as good as that run.\n" % stage)
    finally:
        shutil.rmtree(stage, ignore_errors=True)
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
        files["DERIVED-FROM-LIVE-RUN.txt"] = derived_note.encode("utf-8")
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
        fh.write("2025-12-31T22:59:59+00:00 launch kagi round=1\n"
                 "2025-12-31T23:00:00+00:00 steer kagi -> round 2\n"
                 "2025-12-31T23:00:01+00:00 launch kagi round=3\n")
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
    with open(os.path.join(repo, ".ufo/prompts/kagi-round-1.md"), "w", encoding="utf-8") as fh:
        fh.write(FX_REPORT_1)
    with open(os.path.join(repo, ".ufo/prompts/kagi-round-5.md"), "w", encoding="utf-8") as fh:
        fh.write("# prompt kagi round 5\n")
    _fixture_git(repo, ["add", "--", ".ufo/reports/round-1/kagi.md", ".ufo/prompts/kagi-round-1.md"])
    _fixture_git(repo, ["commit", "-q", "-m", "fixture: backdated landing"], dates=FX_LANDED_AT)
    _fixture_git(repo, ["add", "--", ".ufo/reports/round-2/kagi.md"])
    _fixture_git(repo, ["commit", "-q", "-m", "fixture: post-C landing"])
    os.utime(os.path.join(repo, ".ufo/reports/round-3/kagi.md"),
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
        # log boundary: the line exactly at C is kept, the one second after is dropped
        check("log-boundary", files["watchdog.log"].decode(),
              "2025-12-31T22:59:59+00:00 launch kagi round=1\n"
              "2025-12-31T23:00:00+00:00 steer kagi -> round 2\n")
        # landed_at / presence rule
        check("reports-index", files["reports-index.txt"].decode(),
              ".ufo/reports/round-1/kagi.md\t%d\t1\t1\t1\t%s\n"
              ".ufo/reports/round-3/kagi.md\t%d\t0\t0\t0\t-\n" % (
                  len(FX_REPORT_1.encode()), FX_LANDED_AT, len(FX_REPORT_3.encode())))
        check("reports-exclude-post-C", ".ufo/reports/round-2/kagi.md" in files["reports-index.txt"].decode(), False)
        check("reports-exclude-post-C-untracked", ".ufo/reports/round-4/kagi.md" in files["reports-index.txt"].decode(), False)
        check("prompts-index", files["prompts-index.txt"].decode(), ".ufo/prompts/kagi-round-1.md\n")
        check("counters", files["state-counters.txt"].decode(), "kagi\t2\n")
        closed_lines = dict(l.split("\t", 1) for l in files["CLOSED_AT.txt"].decode().splitlines()
                            if l.startswith(("closed_at", "log_lines", "manifest_entries",
                                             "reports", "prompts", "main_HEAD", "manifest_source")))
        check("closed-at-line", closed_lines["closed_at"], FX_CLOSED)
        check("closed-at-log-lines", closed_lines["log_lines"], "2")
        check("closed-at-entries", closed_lines["manifest_entries"], "1")
        check("closed-at-reports", closed_lines["reports"], "2")
        check("closed-at-prompts", closed_lines["prompts"], "1")
        check("closed-at-source", closed_lines["manifest_source"], "live MANIFEST.json")
        exp_doc = json.loads(files["expected.json"].decode())
        check("expected-json-exit-debt", [exp_doc["exit"], exp_doc["debt"]], [0, []])
        check("expected-json-inputs", sorted(exp_doc["inputs"]),
              ["CLOSED_AT.txt", "MANIFEST.json", "prompts-index.txt",
               "reports-index.txt", "state-counters.txt", "watchdog.log"])
        check("expected-json-input-digest", exp_doc["inputs"]["MANIFEST.json"],
              hashlib.sha256(files["MANIFEST.json"]).hexdigest())
        check("manifest-verbatim", files["MANIFEST.json"], read_bytes(os.path.join(fixture, "MANIFEST.json")))
        # refusals: wave dirs, then a non-empty --out without --force
        for name in ("round-11", "round-12"):
            path = os.path.join(fixture, ".ufo", "waves", name, "snap")
            try:
                check_out_dir(path, fixture)
                check("refuse-%s" % name, "accepted", "refused")
            except FreezeError as exc:
                check("refuse-%s" % name, "inside" in str(exc), True)
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

        if args.expected_exit is not None:
            text = expected_json_text(args.expected_exit, parse_expected_debt(args.expected_debt))
            with open(os.path.join(out_real, "expected.json"), "w", encoding="utf-8") as fh:
                fh.write(text)
            exit_code, debt = args.expected_exit, parse_expected_debt(args.expected_debt)
        else:
            checker = args.checker or default_checker(repo)
            temp_root = os.path.realpath(tempfile.gettempdir())
            if temp_root == os.path.realpath(repo) or temp_root.startswith(os.path.realpath(repo) + os.sep):
                raise FreezeError("temp dir %s is inside the repo; point TMPDIR outside it "
                                  "(derive mode stages a mirror there)" % temp_root)
            exit_code, debt = derive_expected(out_real, checker)
    except FreezeError as exc:
        return die(str(exc), exc.code or EXIT_USAGE)

    print("freeze-snapshot: %s" % out_real)
    print("  closed_at\t%s" % closed.isoformat())
    print("  manifest_source\t%s" % " ".join(source))
    print("  main_HEAD\t%s" % main_head(repo, closed))
    print("  log_lines\t%d kept, %d dropped (> closed_at or unparsable)" % (len(kept), dropped))
    print("  reports\t%d\tprompts\t%d" % (len(rows_reports), len(rows_prompts)))
    print("  expected\t%s\tdebt rows\t%d\texit\t%d" % (
        "pinned" if args.expected_exit is not None else "derived from a live run", len(debt), exit_code))
    return EXIT_OK


if __name__ == "__main__":
    try:
        sys.exit(main())
    except FreezeError as exc:            # pragma: no cover - defensive
        sys.exit(die(str(exc)))
    except BrokenPipeError:
        os._exit(0)