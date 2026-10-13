#!/usr/bin/env python3
"""closure-check.py -- executable closure gate for the shokunin fleet (protocol lane, round 15).

Reads the durable closure evidence and reports the `rounds[]` ledger rows that are
unresolved, contradicted, or missing:

  inputs (live mode, relative to the repo root)
    MANIFEST.json                    rounds[] statuses                (P:202-290 §Round-robin)
    .ufo/watchdog.log                launch/steer/complete lines      (P:217-235 §Round-robin)
    .ufo/reports/round-*/<lane>.md   completion evidence / markers    (P:110-125, 147-155)
    .ufo/state/<lane>.round          counter corroboration, lane universe (P:224-231)
    .ufo/prompts/<lane>-round-N.md   dispatch corroboration / durability   (P:217-221)
    .ufo/history-pin.json            append-only pin over rounds[0:k] (P:271-274)

  not an input
    .ufo/watchdog-driver.log         the driver holds fd1/fd2 on it (launcher redirect) and
                                     never writes evidence there; every dispatch/complete line
                                     goes to .ufo/watchdog.log. It is a reserved error sink,
                                     empty when healthy -- reading it as evidence would let a
                                     stray traceback line fabricate a dispatch.

Semantics implemented (PROTOCOL.md anchors: line numbers against the 470-line compacted file,
plus the stable section heading; `A:<row>` is a PROTOCOL-APPENDIX.md first-column rule row):
  * a row names lane-round (lane, entry.round); `lane_rounds[lane]` is the counter the lane
    held at closed_at -- an annotation, never a re-key. (P:247-256 "A row names the lane-round")
  * last row for a (lane, lane_round) wins; `rounds` is append-only after closure.
    (P:263-270 "`rounds` is append-only after closure")
  * entries typed scaffold/work/ops are fleet-keyed legacy rows -> `unadjudicable`, never a
    status (live: entries #0/#1 pre-fleet-2); a `type: "mint"` entry is a *recognized
    non-closure entry*: reported, excluded from lane-status tallies, never silently skipped.
    (P:208-211 "Non-closure entry types are recognized, never silent"; A:43)
  * dispatch evidence = `launch <lane> round=N` or `steer <lane> -> round N`; a prompt with no
    dispatch line is an attempted dispatch -> `failed`.                         (P:217-223)
  * completion evidence = a report at the contract path; a contentless marker -> `failed`; a
    marker naming a real committed hash -> `ok` + minimum-content defect. (P:110-125, 147-155)
  * termination evidence = `complete <lane> round=N` or the lane counter passing N, and the
    driver's third completion verb `wrap <lane> round=N complete; NOT respawning (fleet-wrap)`,
    which is a completed mission the driver does not respawn.            (P:224-231)
  * `in-flight` is decided from the absence of both a `complete` line and a *landed* report -
    never from a liveness probe. (P:226-236, "Liveness probes are not evidence")
  * no `not-dispatched` while dispatch evidence exists, no `in-flight` unless the mission was
    live at closed_at, `lane_rounds` required on every `not-dispatched` row, `closed_at`
    required on any entry carrying not-dispatched/in-flight, `supersedes` required on every
    closure-correction.                                     (P:212-216, 237-246, 263-270)
  * stale-lane actuator: mission open > 2 driver ticks (900 s from the launch timestamp), age
    from the launch line, graded progressing / progressing-weak / silent.       (P:129-141)
  * lane universe: MANIFEST `roster` ids ∪ base LANES ∪ driver counters ∪ every lane named by
    a dispatch/complete line or a prompt file. A lane minted and wired into the watchdog
    mid-round is adjudicated before its roster row lands (roster rows are operator-only;
    probation lives in `rounds[].notes`), and a lane whose only trace is log lines stays
    adjudicable rather than invisible (A:42, the m10 residual). A lane id that appears
    *nowhere* -- an unparseable dispatch line, or a `lane_rounds` annotation naming a lane no
    evidence source knows -- is an `unknown_lane` finding (could-not-evaluate), never a crash
    and never a silent drop.
  * append-only history pin: rounds[0:k] must hash to the digest committed at
    `.ufo/history-pin.json`, anchored to a commit whose own MANIFEST.json bytes still hash to
    it and which is an ancestor of HEAD -- an in-place edit of closed history is
    `history_pin_mismatch`, a regenerated pin is `history_pin_unanchored`. (P:271-274, A:44)
  * frozen baselines: --frozen NAME resolves under any `.ufo/waves/*/frozen` root and fails
    closed on a duplicate name; expected.json pins the snapshot's own input digests, and a
    mismatch is `snapshot_tampered` (could-not-evaluate) rather than a compared verdict, while
    a baseline carrying no digests is reported `unpinned (legacy)`.    (P:339-353, A:45)

Exit map (the fleet verdict-gate convention this round standardises):
  0  clean                 no debt and no contradictions (live in-flight rows are compliant)
  1  debt/contradiction    stale_in_flight / unrowed_terminated / prompt_orphan / prompt_untracked /
                           keying_violation / contradiction /
                           history_pin_{unavailable,invalid,mismatch,unanchored,orphan,unverifiable}
  2  could-not-evaluate    missing input, parse error, bad usage, snapshot_tampered,
                           unknown_lane (an id no evidence source knows)
  3  no-baseline           a pinned expected-value baseline is absent (--selftest / --frozen)

A could-not-evaluate finding never masks debt: findings the gate *cannot* adjudicate are kept
out of `debt` (so a frozen baseline's pinned debt set stays comparable) and raise the exit code
to 2 only when there is no debt at all.

The run is read-only: it writes nothing outside stdout/stderr.
"""

import argparse
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime

EXIT_OK = 0
EXIT_DEBT = 1
EXIT_ERROR = 2
EXIT_NOBASELINE = 3

LANES = ["protocol", "aggregator", "kasegi", "kengaku", "kake", "kumitate", "kotoba", "kagi"]
MAIN_LANES = ("protocol", "aggregator")   # main-repo lane roles; every other lane owns <id>-shokunin/
STATUSES = ("ok", "failed", "not-dispatched", "in-flight")
ADJUDICATED_TYPES = ("closure", "closure-correction", "retroactive-closure")
# Non-closure entry types the protocol recognizes: reported, never silently skipped (P:208-211).
# `mint` records a lane-initiated sibling mint (no `lanes` map); scaffold/work/ops are the
# pre-fleet-2 fleet-keyed rows. A type outside this set is `unknown_entry_type`.
NONCLOSURE_TYPES = ("mint", "scaffold", "work", "ops")
HISTORY_PIN_REL = os.path.join(".ufo", "history-pin.json")
# Class of findings the gate cannot adjudicate: excluded from `debt`, exit 2 when alone. The
# constant is the single source of the taxonomy -- `analyze` classifies every finding by it.
COULD_NOT_EVALUATE_CLASSES = ("unknown_lane", "unknown_entry_type")

TWO_TICKS_S = 900
MARKER_MAX_BYTES = 400          # record: markers 101-254 B, smallest real report 4370 B
ROUND_DIR_RE = re.compile(r"^round-(.+)$")
# Operator-owned read-only trees: searched for citation identity, never fetched or written.
EXTERNAL_READONLY = ["~/Projects/bounties", "~/Projects/origin-work/open-bug-bounties",
                     "~/Projects/webzites", "~/Projects/origin-work/ufo-fsd-alpha",
                     "~/Projects/charter-ufo-fsd"]

LANE_ID_RE = r"[a-z][a-z0-9_-]*"
RE_DISPATCH = re.compile(r"^(\S+) (launch|steer) (%s) (?:-> round |round=)(\d+)\b" % LANE_ID_RE)
RE_COMPLETE = re.compile(r"^(\S+) complete (%s) round=(\d+)\b" % LANE_ID_RE)
RE_TICK = re.compile(r"^(\S+) tick=(\d+)\b")
# Third driver verb: the fleet-wrap line `wrap <lane> round=N complete; NOT respawning (fleet-wrap)`
# records a completed mission the driver does not respawn. It says `complete`, so it is
# termination evidence exactly like RE_COMPLETE (P:224-231).
RE_WRAP = re.compile(r"^(\S+) wrap (%s) round=(\d+) complete\b" % LANE_ID_RE)
# Loose variants: the same line grammar but any non-space lane token, used only to catch an id
# the strict grammar cannot read (uppercase, punctuation, `Kama.1`) so it becomes an
# `unknown_lane` finding instead of an invisible line (the "never silently blind" rule).
RE_DISPATCH_LOOSE = re.compile(r"^(\S+) (launch|steer) (\S+) (?:-> round |round=)(\d+)\b")
RE_COMPLETE_LOOSE = re.compile(r"^(\S+) complete (\S+) round=(\d+)\b")
RE_WRAP_LOOSE = re.compile(r"^(\S+) wrap (\S+) round=(\d+) complete\b")
RE_HASH_RUN = re.compile(r"(?<![0-9a-fA-F])[0-9a-f]{7,}(?![0-9a-fA-F])")
RE_SHONEN = re.compile(r"^#{1,6}\s*SHONEN", re.M)
RE_PLACEHOLDER = re.compile(r"\b(LANE_HASH|<lane-hash>|<hash>|<sha>|TODOHASH)\b")
# A prompt filename is a universe source too: any non-space lane token, classified after the match.
PROMPT_NAME_RE = re.compile(r"^(\S+)-round-(\d+)\.md$")

MAIN_SCOPE = {
    "protocol": [
        ".ufo/waves/*", ".ufo/waves/*/*", ".ufo/waves/*/*/*", ".ufo/waves/*/*/*/*",
        ".ufo/prompts/protocol-*", ".ufo/history-pin.json",
        ".ufo/reports/round-*/protocol.md",
        "PROTOCOL.md", "SCORECARD.md", "LOG.md", "ROADMAP.md",
        "PROTOCOL-APPENDIX.md",
    ],
    "aggregator": [
        ".ufo/reports/AGGREGATE.md", ".ufo/reports/round-*/aggregator.md",
        ".ufo/prompts/aggregator-*", "*/corpus/*", "*/corpus/*/*", "*/corpus/*/*/*",
    ],
}

HELP_EPILOG = """exit map:
  0  clean              no debt, no contradictions
  1  debt/contradiction stale_in_flight / unrowed_terminated / prompt_orphan / contradiction /
                        history_pin_* (append-only history pin)
  2  could-not-evaluate missing input, parse error, bad usage, snapshot_tampered,
                        unknown_lane (a lane id no evidence source knows)
  3  no-baseline        pinned expected values absent (--selftest / --frozen)

lane universe: MANIFEST roster ids u base LANES u .ufo/state/*.round counters u lanes named by
a dispatch/complete line or a prompt file, so a lane wired into the driver mid-round is
adjudicated before its roster row lands. A lane id no source knows is an unknown_lane finding.

row keying: a rounds[] row names lane-round (lane, entry.round); lane_rounds[lane] is the
counter the lane held at closed_at and never re-keys the row. --show-keying prints both
tallies; the entry-keyed one is authoritative.

history pin: .ufo/history-pin.json pins sha256(rounds[0:k]) plus the commit whose
MANIFEST.json bytes hash to it, so an in-place edit of closed history is a finding and
regenerating the pin to bless one shows up in that commit's own diff. Live mode only;
frozen snapshots are pinned by their expected.json input digests instead. --pin overrides.

frozen roots: --frozen NAME searches every .ufo/waves/*/frozen root newest-first and fails
closed (exit 3) when a bare NAME matches more than one; disambiguate with --frozen
<wave>/<NAME> or --frozen-root DIR."""


# ----------------------------------------------------------------------------- helpers

def lane_sort(lane):
    """Sort key that tolerates a lane id outside the fixed roster (never raises)."""
    return LANES.index(lane) if lane in LANES else len(LANES) + 1


def iso(text):
    try:
        return datetime.fromisoformat(text)
    except (ValueError, TypeError):
        return None


def epoch(dt):
    return dt.timestamp() if dt is not None else None


def walk_up_repo(script_path):
    """Default repo: nearest ancestor of the script holding MANIFEST.json + .ufo/."""
    d = os.path.dirname(os.path.abspath(script_path))
    for _ in range(10):
        if os.path.isfile(os.path.join(d, "MANIFEST.json")) and os.path.isdir(os.path.join(d, ".ufo")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    # fallback: the directory containing the script's great-great-grandparent
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(script_path)))))


def run_git(repo, args, timeout=15):
    try:
        done = subprocess.run(["git", "-C", repo] + args, capture_output=True,
                              text=True, timeout=timeout)
    except (OSError, subprocess.SubprocessError):
        return None, ""
    return done.returncode, done.stdout


def read_text(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return None


def read_json(path):
    text = read_text(path)
    if text is None:
        return None, "missing %s" % path
    try:
        return json.loads(text), None
    except ValueError as exc:
        return None, "parse error in %s: %s" % (path, exc)


# ----------------------------------------------------------------------------- inputs

class Inputs(object):
    """Evidence bundle, either live from a repo or frozen from a snapshot directory."""

    def __init__(self, kind, root):
        self.kind = kind
        self.root = root
        self.entries = []
        self.manifest_path = ""
        self.log_path = ""
        self.log_lines = []
        self.raw_dispatch = {}   # (lane, n) -> [events], every lane on the log
        self.raw_completes = {}  # (lane, n) -> [events], every lane on the log
        self.dispatch = {}       # (lane, n) -> [event dicts], lanes inside the universe
        self.completes = {}      # (lane, n) -> [event dicts], lanes inside the universe
        self.foreign = {}        # (lane-id-token, n) -> [events] the grammar cannot read
        self.ticks = []
        self.reports = {}        # rel path -> grade dict
        self.counters = {}       # lane -> int
        self.prompts = set()     # (lane, n) inside the universe
        self.foreign_prompts = set()   # (lane-id-token, n) outside it
        self.citations = []
        self.citation_scope = "disabled"
        self.allowed = list(LANES)        # the lane universe, assembled in the loaders
        self.roster_ids = []              # MANIFEST.json `roster` ids, for the universe report
        self.counter_only = []            # lanes the driver counts but no roster row lists
        self.instant = None               # the snapshot's closed_at (frozen mode)

    # -- report helpers ------------------------------------------------------
    def contract_rel(self, lane, n):
        return ".ufo/reports/round-%s/%s.md" % (n, lane)

    def report(self, lane, n):
        return self.reports.get(self.contract_rel(lane, n))

    def report_seen_by(self, lane, n, closed_at):
        """Was a report at the contract path on disk at/before closed_at?"""
        rep = self.report(lane, n)
        if rep is None:
            return False
        if self.kind == "frozen":
            return False   # snapshots carry no mtimes: presence is not "seen by closed_at"
        mt = rep.get("mtime")
        return mt is not None and closed_at is not None and mt <= closed_at


def _roster_ids(manifest):
    """MANIFEST.json `roster` ids (objects with `id`, or bare strings)."""
    ids = []
    for item in ((manifest or {}).get("roster") or []):
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            ids.append(item["id"])
        elif isinstance(item, str) and item:
            ids.append(item)
    return sorted(set(i for i in ids if i))


def _lane_universe(manifest, counters, log_lanes, prompt_lanes):
    """The lane universe: MANIFEST `roster` ids, the base LANES, every lane the driver keeps a
    `.ufo/state/<lane>.round` counter for, and every lane named by a dispatch/complete line or a
    prompt file (A:42 "Lane universe", mutant m10).

    The union is closed over every source this gate reads, so a lane minted mid-round -- wired
    into the watchdog before the operator lands its roster row -- is adjudicated from its first
    dispatch, and a lane whose counter file was deleted stays adjudicable from its log lines
    instead of going invisible. Roster rows are operator-only; `rounds[].notes` carries the
    probation state meanwhile."""
    ids = set(LANES) | set(counters) | set(log_lanes) | set(prompt_lanes)
    ids |= set(_roster_ids(manifest))
    ids = set(i for i in ids if i)
    return [l for l in LANES if l in ids] + sorted(i for i in ids if i not in LANES)


def _open_lane_universe(inp, manifest, counters, prompt_keys):
    """Assemble the universe, then open the event buckets and prompt set against it."""
    inp.counters = counters
    inp.roster_ids = _roster_ids(manifest)
    log_lanes = set(lane for lane, _ in list(inp.raw_dispatch) + list(inp.raw_completes))
    prompt_lanes = set(lane for lane, _ in prompt_keys)
    inp.allowed = _lane_universe(manifest, counters, log_lanes, prompt_lanes)
    inp.counter_only = sorted(set(counters) - set(LANES) - set(inp.roster_ids))
    inp.dispatch = {k: v for k, v in inp.raw_dispatch.items() if k[0] in inp.allowed}
    inp.completes = {k: v for k, v in inp.raw_completes.items() if k[0] in inp.allowed}
    inp.prompts = set(k for k in prompt_keys if k[0] in inp.allowed)
    inp.foreign_prompts = set(k for k in prompt_keys if k[0] not in inp.allowed)
    return inp


def _read_counters(state_dir):
    """`.ufo/state/<lane>.round` -> int. Driver-written; the universe's counter source."""
    counters = {}
    if os.path.isdir(state_dir):
        for name in sorted(os.listdir(state_dir)):
            if name.endswith(".round"):
                text = read_text(os.path.join(state_dir, name))
                if text is not None and text.strip().isdigit():
                    counters[name[:-len(".round")]] = int(text.strip())
    return counters


def _scan_prompts(inp, prompts_dir):
    """`.ufo/prompts/<lane>-round-N.md` -> {(lane, n)}. A prompt file is both a universe source
    and dispatch corroboration: it names a lane-round the driver attempted to dispatch, so a
    prompt whose id the grammar cannot read becomes an `unknown_lane` finding, never a skip."""
    keys = set()
    if not os.path.isdir(prompts_dir):
        return keys
    for name in sorted(os.listdir(prompts_dir)):
        m = PROMPT_NAME_RE.match(name)
        if not m:
            continue
        lane, n = m.group(1), int(m.group(2))
        if re.match(r"^%s$" % LANE_ID_RE, lane):
            keys.add((lane, n))
        else:
            inp.foreign.setdefault((lane, n), []).append(
                {"ts": None, "text": ".ufo/prompts/%s" % name, "line": 0, "verb": "prompt",
                 "kind": "lane-id-unreadable"})
    return keys


def load_live(root):
    inp = Inputs("live", root)
    inp.manifest_path = os.path.join(root, "MANIFEST.json")
    inp.log_path = os.path.join(root, ".ufo", "watchdog.log")
    manifest, err = read_json(inp.manifest_path)
    if err:
        return None, err
    inp.entries = manifest.get("rounds") or []
    counters = _read_counters(os.path.join(root, ".ufo", "state"))
    log_text = read_text(inp.log_path)
    if log_text is None:
        return None, "missing %s" % inp.log_path
    inp.log_lines = log_text.splitlines()
    # the log and the prompt set are parsed BEFORE the universe is assembled: both are sources
    # of it (A:42), so filtering them first would drop the lanes the universe exists to find
    _parse_log(inp)
    prompt_keys = _scan_prompts(inp, os.path.join(root, ".ufo", "prompts"))
    _open_lane_universe(inp, manifest, counters, prompt_keys)
    reports_dir = os.path.join(root, ".ufo", "reports")
    if os.path.isdir(reports_dir):
        for name in sorted(os.listdir(reports_dir)):
            rd = os.path.join(reports_dir, name)
            if not os.path.isdir(rd):
                continue
            m = ROUND_DIR_RE.match(name)
            if not m:
                continue
            for fname in sorted(os.listdir(rd)):
                path = os.path.join(rd, fname)
                if not os.path.isfile(path):
                    continue
                rel = ".ufo/reports/%s/%s" % (name, fname)
                inp.reports[rel] = _grade_file(path, rel, is_lane_report=fname.endswith(".md"))
    return inp, None


def load_frozen(frozen_dir):
    inp = Inputs("frozen", frozen_dir)
    inp.manifest_path = os.path.join(frozen_dir, "MANIFEST.json")
    inp.log_path = os.path.join(frozen_dir, "watchdog.log")
    manifest, err = read_json(inp.manifest_path)
    if err:
        return None, err
    inp.entries = manifest.get("rounds") or []
    counters = {}
    ctext = read_text(os.path.join(frozen_dir, "state-counters.txt"))
    if ctext:
        for line in ctext.splitlines():
            parts = line.split("\t")
            if len(parts) >= 2 and parts[1].strip().isdigit():
                counters[parts[0]] = int(parts[1].strip())
    log_text = read_text(inp.log_path)
    if log_text is None:
        return None, "missing %s" % inp.log_path
    inp.log_lines = log_text.splitlines()
    # the log and the prompt index are parsed before the universe is assembled (see load_live)
    _parse_log(inp)
    prompt_keys = set()
    pindex = read_text(os.path.join(frozen_dir, "prompts-index.txt"))
    for line in (pindex or "").splitlines():
        m = re.match(r"^\.ufo/prompts/(.+)-round-(\d+)\.md$", line.strip())
        if not m:
            continue
        lane, n = m.group(1), int(m.group(2))
        if re.match(r"^%s$" % LANE_ID_RE, lane):
            prompt_keys.add((lane, n))
        else:
            inp.foreign.setdefault((lane, n), []).append(
                {"ts": None, "text": line.strip(), "line": 0, "verb": "prompt",
                 "kind": "lane-id-unreadable"})
    _open_lane_universe(inp, manifest, counters, prompt_keys)
    index = read_text(os.path.join(frozen_dir, "reports-index.txt"))
    if index is None:
        return None, "missing reports-index.txt in %s" % frozen_dir
    for line in index.splitlines():
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 5:
            continue
        rel, nbytes, tracked, hashash, hasshonen = parts[:5]
        landed_at = parts[5] if len(parts) > 5 else ""
        try:
            nbytes = int(nbytes)
        except ValueError:
            continue
        inp.reports[rel] = {
            "rel": rel, "bytes": nbytes, "tracked": tracked == "1",
            "landed_at": iso(landed_at) if landed_at and landed_at != "-" else None,
            "has_hash": hashash == "1", "has_shonen": hasshonen == "1",
            "marker": nbytes < MARKER_MAX_BYTES and hashash != "1" and hasshonen != "1",
            "mtime": None,
        }
    inp.instant = _newest_closed_at(inp.entries)
    inp.citation_scope = "frozen snapshot: citation/ancestry checks disabled"
    return inp, None


def _grade_file(path, rel, is_lane_report):
    text = read_text(path) or ""
    try:
        nbytes = os.path.getsize(path)
        mtime = datetime.fromtimestamp(os.path.getmtime(path)).astimezone()
    except OSError:
        nbytes, mtime = len(text.encode()), None
    has_hash = bool(RE_HASH_RUN.search(text))
    has_shonen = bool(RE_SHONEN.search(text))
    marker = is_lane_report and nbytes < MARKER_MAX_BYTES and not has_hash and not has_shonen
    return {"rel": rel, "bytes": nbytes, "has_hash": has_hash, "has_shonen": has_shonen,
            "marker": marker, "mtime": mtime, "tracked": None, "path": path}


def _parse_log(inp):
    """Every dispatch/complete/wrap/tick line, keys unfiltered.

    The lane universe is closed over this log, so lanes are collected here and the buckets are
    opened against the assembled universe by `_open_lane_universe`. A line matching the grammar
    with a lane token the lane-id grammar cannot read (uppercase, punctuation) is kept as an
    `unknown_lane` finding rather than dropped: a blind spot is the failure mode this exists to
    prevent (A:42).
    """
    for idx, line in enumerate(inp.log_lines):
        m = RE_DISPATCH.match(line)
        if m:
            ts, verb, lane, n = m.group(1), m.group(2), m.group(3), int(m.group(4))
            inp.raw_dispatch.setdefault((lane, n), []).append(
                {"ts": iso(ts), "text": line, "line": idx + 1, "verb": verb})
            continue
        m = RE_COMPLETE.match(line)
        if m:
            ts, lane, n = m.group(1), m.group(2), int(m.group(3))
            inp.raw_completes.setdefault((lane, n), []).append(
                {"ts": iso(ts), "text": line, "line": idx + 1, "verb": "complete"})
            continue
        m = RE_WRAP.match(line)
        if m:
            ts, lane, n = m.group(1), m.group(2), int(m.group(3))
            inp.raw_completes.setdefault((lane, n), []).append(
                {"ts": iso(ts), "text": line, "line": idx + 1, "verb": "wrap"})
            continue
        m = RE_TICK.match(line)
        if m:
            inp.ticks.append({"ts": iso(m.group(1)), "tick": int(m.group(2)), "line": idx + 1})
            continue
        m = RE_DISPATCH_LOOSE.match(line)
        if m:
            ts, verb, lane, n = m.group(1), m.group(2), m.group(3), int(m.group(4))
            inp.foreign.setdefault((lane, n), []).append(
                {"ts": iso(ts), "text": line, "line": idx + 1, "verb": verb,
                 "kind": "lane-id-unreadable"})
            continue
        m = RE_COMPLETE_LOOSE.match(line)
        if m:
            ts, lane, n = m.group(1), m.group(2), int(m.group(3))
            inp.foreign.setdefault((lane, n), []).append(
                {"ts": iso(ts), "text": line, "line": idx + 1, "verb": "complete",
                 "kind": "lane-id-unreadable"})
            continue
        m = RE_WRAP_LOOSE.match(line)
        if m:
            ts, lane, n = m.group(1), m.group(2), int(m.group(3))
            inp.foreign.setdefault((lane, n), []).append(
                {"ts": iso(ts), "text": line, "line": idx + 1, "verb": "wrap",
                 "kind": "lane-id-unreadable"})
    for bucket in (inp.raw_dispatch, inp.raw_completes, inp.foreign):
        for key in bucket:
            bucket[key].sort(key=lambda e: (epoch(e["ts"]) or 0.0, e["line"]))


# ----------------------------------------------------------------------------- ledger

def build_ledger(entries, allowed):
    """Structural validation first (never a traceback), then the last-wins ledger.

    Shape rules (each violation -> a `contradiction` row naming the entry index):
    unknown lane id, `lanes` not a map (a list also exposes duplicate lane rows), missing
    `lanes`, non-string status, status outside ok|failed|not-dispatched|in-flight,
    `not-dispatched` without `lane_rounds[id]`, non-integer `lane_rounds` values,
    `closed_at` missing on an entry carrying not-dispatched/in-flight, `supersedes` missing
    on a closure-correction, `supersedes` naming no existing entry, an ambiguous `supersedes`
    (several candidates and no `supersedes.entry`), and a `supersedes.entry` whose round/type
    do not match.

    Non-closure entries are reported, never silently skipped (P:208-211): every entry whose
    `type` is not a closure type lands in `nonclosure` with its type and whether that type is
    recognized (`mint` + the pre-fleet-2 scaffold/work/ops rows), and keeps its lane rows out of
    the ledger as `unadjudicable`. A type outside that vocabulary is an `unknown_entry_type`
    finding (could-not-evaluate). A `lane_rounds` key naming a lane outside the universe is an
    `unknown_lane` finding (could-not-evaluate): an annotation for a lane no evidence source
    knows (A:42).

    Returns a dict: rows, all_rows, unadjudicable, unadj_keys, shape, nonclosure,
    unadjudicable_ids (findings naming an id outside the lane universe, classified by the
    caller against COULD_NOT_EVALUATE_CLASSES)."""
    rows = {}
    all_rows = []
    unadjudicable = []
    unadj_keys = {}
    shape = []
    nonclosure = []
    id_findings = []
    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            shape.append(_finding("*", None, "*", "contradiction", "entry-malformed",
                                  "entry #%d is not an object (P:202-207)" % i))
            continue
        r = e.get("round")
        t = e.get("type")
        raw = e.get("lanes")
        if isinstance(raw, list):
            pairs = []
            for item in raw:
                if isinstance(item, dict):
                    pairs.extend(sorted(item.items()))
            dupes = sorted({k for k, _ in pairs if [x for x, _ in pairs].count(k) > 1})
            shape.append(_finding("*", r, "*", "contradiction", "lanes-not-a-map",
                                  "entry #%d `lanes` is a list, not a map%s (P:206-207)" % (
                                      i, "; duplicate lane rows: %s" % ",".join(dupes) if dupes else "")))
            raw = dict(pairs)
        elif raw is not None and not isinstance(raw, dict):
            shape.append(_finding("*", r, "*", "contradiction", "lanes-not-a-map",
                                  "entry #%d `lanes` is %s, not a map (P:206-207)" % (i, type(raw).__name__)))
        if t not in ADJUDICATED_TYPES:
            nonclosure.append({"entry": i, "round": r, "type": t,
                               "recognized": t in NONCLOSURE_TYPES,
                               "lanes": raw if isinstance(raw, dict) else {},
                               "notes": bool(e.get("notes"))})
            if t not in NONCLOSURE_TYPES:
                id_findings.append(_finding("*", r, "*", "unknown_entry_type", "entry-type-unrecognized",
                                    "entry #%d type=%r is neither a closure type (%s) nor a recognized "
                                    "non-closure type (%s): the gate cannot tell whether it carries lane "
                                    "rows (P:202-211)" % (i, t, "|".join(ADJUDICATED_TYPES),
                                                          "|".join(NONCLOSURE_TYPES))))
            if isinstance(raw, dict) and raw:
                unadjudicable.append({"entry": i, "round": r, "type": t, "lanes": raw})
                for lane in raw:
                    unadj_keys[(lane, r)] = i
            continue
        if raw is None:
            shape.append(_finding("*", r, "*", "contradiction", "entry-missing-lanes",
                                  "entry #%d type=%s has no `lanes` map (P:202-207)" % (i, t)))
            continue
        if not isinstance(raw, dict):
            continue          # `lanes-not-a-map` already recorded above
        lanes = raw
        raw_lr = e.get("lane_rounds")
        if raw_lr is None:
            lr = {}
        elif isinstance(raw_lr, dict):
            lr = raw_lr
        else:
            shape.append(_finding("*", r, "*", "contradiction", "lane_rounds-not-a-map",
                                  "entry #%d `lane_rounds` is %s, not a map (P:244-247)" % (i, type(raw_lr).__name__)))
            lr = {}
        ca = e.get("closed_at")
        needs_ca = any(isinstance(v, str) and v in ("not-dispatched", "in-flight") for v in lanes.values())
        if not ca and needs_ca:
            shape.append(_finding("*", r, "*", "contradiction", "entry-missing-closed_at",
                                  "entry #%d type=%s carries not-dispatched/in-flight without closed_at (P:211-213)" % (i, t)))
        elif ca is not None and iso(ca) is None:
            shape.append(_finding("*", r, "*", "contradiction", "entry-invalid-closed_at",
                                  "entry #%d type=%s carries an unparseable closed_at %r (P:211-213)"
                                  % (i, t, ca)))
        if t == "closure-correction" and "supersedes" not in e:
            shape.append(_finding("*", r, "*", "contradiction", "closure-correction-missing-supersedes",
                                  "entry #%d type=closure-correction lacks supersedes (P:256-258)" % i))
        elif t == "closure-correction":
            shape.extend(_supersedes_findings(entries, i, e.get("supersedes")))
        for lane, v in sorted(lr.items()):
            if not isinstance(v, int) or isinstance(v, bool):
                shape.append(_finding(lane, r, lane, "contradiction", "lane_rounds-value-not-an-integer",
                                      "entry #%d lane_rounds[%s]=%r is not an integer counter (P:244-247)" % (i, lane, v)))
                continue
            if lane not in allowed:
                id_findings.append(_finding(lane, r, lane, "unknown_lane", "lane_rounds-outside-universe",
                                    "entry #%d lane_rounds[%s]=%d annotates a lane no evidence source "
                                    "knows: not in the roster, the base lanes, the driver counters, the "
                                    "log, or the prompt set (A:42)" % (i, lane, v)))
        for lane in sorted(lanes):
            st = lanes[lane]
            if lane not in allowed:
                shape.append(_finding(lane, r, lane, "contradiction", "unknown-lane",
                                      "entry #%d names lane=%r outside the roster %s (P:207)" % (
                                          i, lane, ",".join(allowed))))
                continue
            if not isinstance(st, str):
                shape.append(_finding(lane, r, lane, "contradiction", "status-not-a-string",
                                      "entry #%d lane=%s status=%r is not a string (P:206-207)" % (i, lane, st)))
                continue
            if st not in STATUSES:
                shape.append(_finding(lane, r, lane, "contradiction", "status-outside-vocabulary",
                                      "entry #%d lane=%s status=%r not in %s (P:206-207)" % (i, lane, st, "|".join(STATUSES))))
                continue
            if st == "not-dispatched" and lane not in lr:
                shape.append(_finding(lane, r, lane, "contradiction", "not-dispatched-without-lane_rounds",
                                      "entry #%d (round %s) lane_rounds=%s lacks %s (P:244-247)" % (i, r, json.dumps(lr), lane)))
            row = {"lane": lane, "round": r, "status": st, "entry": i,
                   "entry_type": t, "closed_at": ca, "counter": lr.get(lane)}
            rows[(lane, r)] = row
            all_rows.append(row)
    return {"rows": rows, "all_rows": all_rows, "unadjudicable": unadjudicable,
            "unadj_keys": unadj_keys, "shape": shape, "nonclosure": nonclosure,
            "unadjudicable_ids": id_findings}


def _supersedes_findings(entries, i, sup):
    """`supersedes` must name one existing row: a unique (round,type[,date]) match, or an
    explicit `supersedes.entry` array index whose round/type agree (PROTOCOL: append-only,
    corrections name the row they replace; the array index is stable for that purpose)."""
    out = []
    if not isinstance(sup, dict):
        return [_finding("*", entries[i].get("round"), "*", "contradiction", "supersedes-malformed",
                         "entry #%d supersedes=%r is not an object (P:256-258)" % (i, sup))]
    want_r, want_t, want_d = sup.get("round"), sup.get("type"), sup.get("date")
    matches = []
    for j, e in enumerate(entries):
        if j >= i or not isinstance(e, dict):
            continue          # a correction can only supersede an EARLIER row: the annotation
                              # must be unambiguous at write time, and the array is append-only
        if e.get("round") == want_r and e.get("type") == want_t and (want_d is None or e.get("date") == want_d):
            matches.append(j)
    idx = sup.get("entry")
    if idx is not None:
        if not isinstance(idx, int) or isinstance(idx, bool) or idx < 0 or idx >= len(entries):
            out.append(_finding("*", entries[i].get("round"), "*", "contradiction", "supersedes-entry-out-of-range",
                                "entry #%d supersedes.entry=%r is not an existing array index (P:256-260)" % (i, idx)))
        else:
            tgt = entries[idx]
            if not isinstance(tgt, dict) or tgt.get("round") != want_r or tgt.get("type") != want_t:
                out.append(_finding("*", entries[i].get("round"), "*", "contradiction", "supersedes-entry-mismatch",
                                    "entry #%d supersedes.entry=%d is round=%s type=%s, expected round=%s type=%s (P:256-260)" % (
                                        i, idx, tgt.get("round") if isinstance(tgt, dict) else "?",
                                        tgt.get("type") if isinstance(tgt, dict) else "?", want_r, want_t)))
        return out
    if not matches:
        out.append(_finding("*", entries[i].get("round"), "*", "contradiction", "supersedes-names-no-entry",
                            "entry #%d supersedes {round:%s,type:%s,date:%s} matches no existing entry (P:256-260)" % (
                                i, want_r, want_t, want_d)))
    elif len(matches) > 1:
        out.append(_finding("*", entries[i].get("round"), "*", "contradiction", "ambiguous-supersedes",
                            "entry #%d supersedes {round:%s,type:%s,date:%s} matches entries %s and no supersedes.entry disambiguates (P:256-260)" % (
                                i, want_r, want_t, want_d, ",".join("#%d" % j for j in matches))))
    return out


def _finding(lane, lane_round, key, cls, kind, evidence, suggested=None):
    return {"lane": lane, "lane_round": lane_round, "key": key, "class": cls, "kind": kind,
            "evidence": evidence, "suggested_status": suggested}


# ----------------------------------------------------------------------------- activity

def lane_repo(inp, lane):
    if lane not in MAIN_LANES:
        return os.path.join(inp.root, lane + "-shokunin")
    return inp.root


def fs_activity(root, since, patterns=None, limit=10):
    if since is None or not os.path.isdir(root):
        return []
    hits = []
    since_epoch = epoch(since)
    for dirpath, dirnames, filenames in os.walk(root):
        if ".git" in dirnames:
            dirnames.remove(".git")
        for fname in sorted(filenames):
            path = os.path.join(dirpath, fname)
            try:
                if os.path.getmtime(path) <= since_epoch:
                    continue
            except OSError:
                continue
            rel = os.path.relpath(path, root)
            if patterns is not None and not any(fnmatch.fnmatch(rel, p) for p in patterns):
                continue
            hits.append(rel)
            if len(hits) >= limit:
                return sorted(hits)
    return sorted(hits)


def git_activity(root, since):
    """All commits authored since `since` (sha, author-name, iso-date); identity comparison
    is done by the caller so a sibling's commit is never read as the lane's activity."""
    if since is None or not os.path.isdir(root):
        return []
    code, out = run_git(root, ["log", "--since=%s" % since.isoformat(),
                               "--format=%h\t%an\t%cI"])
    if code != 0:
        return []
    rows = []
    for ln in out.splitlines():
        parts = ln.split("\t")
        if len(parts) >= 2:
            rows.append((parts[0], parts[1], parts[2] if len(parts) > 2 else ""))
    return rows[:20]


def file_author(root, rel):
    """Author of the newest commit touching `rel` in `root` (None when untracked)."""
    code, out = run_git(root, ["log", "-1", "--format=%an", "--", rel])
    if code != 0:
        return None
    return out.strip().splitlines()[-1] if out.strip() else None


def hash_identity_note(inp, lane, rel):
    """Do the report's cited hashes belong to the lane's own repo?"""
    rep = inp.reports.get(rel)
    path = rep.get("path") if rep else None
    if not path:
        return "file not readable"
    text = read_text(path) or ""
    toks = sorted({t for t in RE_HASH_RUN.findall(text) if any(c in "abcdef" for c in t)})
    if not toks:
        return "no hash-shaped token cited"
    own = _resolve_hashes(toks, [lane_repo(inp, lane)])
    others = _resolve_hashes(toks, [inp.root] + [os.path.join(inp.root, c + "-shokunin")
                                                for c in sorted(inp.allowed) if c not in MAIN_LANES])
    foreign = sorted({os.path.basename(r) for t, (r, ty) in others.items() if t not in own})
    authors = []
    lane_owned = 0
    for t in sorted(own):
        r, ty = own[t]
        if ty != "commit":
            authors.append("%s (%s)" % (t, ty))
            continue
        code, out = run_git(r, ["show", "-s", "--format=%an", t])
        who = out.strip().splitlines()[-1] if code == 0 and out.strip() else "?"
        authors.append("%s by %s" % (t, who))
        if who.startswith(lane + "-") or who == lane:
            lane_owned += 1
    return "cited %d token(s): %d resolve in %s [%s], %d in other repos%s; lane-authored %d/%d" % (
        len(toks), len(own), os.path.basename(lane_repo(inp, lane)), "; ".join(authors) or "-",
        len(foreign), (" (" + ", ".join(foreign) + ")") if foreign else "", lane_owned, len(own))


SIBLING_OWNED_RE = re.compile(r"corpus/(README\.md|lessons/round-.*aggregator)")


def sibling_owned(rel):
    return bool(SIBLING_OWNED_RE.search(rel))


# ----------------------------------------------------------------------------- citations

def citation_sweep(inp, repo, targets):
    """Classify the hashes cited in the reports of `targets` ((lane, round) pairs).

    Mechanics (recovered from the round-11 verify2 spec, items 12-13):
      token extract on maximal hex runs >= 7 chars (>= 1 a-f letter, so runIds/dates are
      skipped); a token that resolves nowhere across main + the 6 child repos is `dead`;
      a commit that is not an ancestor of that repo's HEAD is `orphan`; a non-commit object
      (a sha256/md5 pin, blob, or abbreviated blob) is `non-commit`; >= 40-hex unresolved is
      a `pin` (a content hash, not a commit). A literal placeholder token is reported too.
    """
    findings = []
    seen = set()
    reports = []
    for lane, n in sorted(set(targets), key=lambda k: (lane_sort(k[0]), k[1])):
        rel = inp.contract_rel(lane, n)
        rep = inp.reports.get(rel)
        if rep is not None and "path" in rep and rel not in seen:
            seen.add(rel)
            reports.append((rel, rep["path"]))
    repos = [repo] + [os.path.join(repo, c + "-shokunin")
                      for c in sorted(inp.allowed) if c not in MAIN_LANES]
    repos += [os.path.expanduser(p) for p in EXTERNAL_READONLY]
    repos = [r for r in repos if os.path.isdir(r)]
    tokens = []
    runid_seen = [0]
    for rel, path in reports:
        text = read_text(path) or ""
        for lineno, line in enumerate(text.splitlines(), 1):
            if RE_PLACEHOLDER.search(line):
                key = (rel, "placeholder")
                if key not in seen:
                    seen.add(key)
                    findings.append({"report": rel, "line": lineno, "token": "placeholder",
                                     "kind": "placeholder-hash",
                                     "detail": "literal placeholder where a round-work hash belongs"})
            for run in RE_HASH_RUN.findall(line):
                # a bare 8-digit calendar date or a >=10-digit runId is not a hash; a 7-9 digit
                # token IS a commit abbreviation in this fleet (4028846, 7483333 are real/absent)
                if run.isdigit() and (re.match(r"^20\d{6}$", run) or len(run) >= 10):
                    runid_seen[0] += 1
                    continue
                if (rel, run) in seen:
                    continue
                seen.add((rel, run))
                tokens.append((rel, lineno, run))
    resolved = _resolve_hashes([t for _, _, t in tokens], repos)
    tally = {"commit": 0, "pin": 0, "runId/date": 0, "dead": 0, "orphan": 0, "non-commit": 0,
             "placeholder": 0}
    for rel, lineno, tok in tokens:
        kind, detail = _classify(tok, resolved.get(tok), repos)
        tally[kind] = tally.get(kind, 0) + 1
        if kind == "commit":
            continue
        findings.append({"report": rel, "line": lineno, "token": tok, "kind": kind, "detail": detail})
    tally["runId/date"] = runid_seen[0]
    tally["placeholder"] = tally.get("placeholder", 0) + len(
        [f for f in findings if f["kind"] == "placeholder-hash"])
    def _order(f):
        m = ROUND_DIR_RE.match(f["report"].split("/")[2] if f["report"].count("/") > 2 else "")
        return (-float(m.group(1)) if m else 0.0, f["report"], f["line"], f["token"])
    return {"findings": sorted(findings, key=_order),
            "tally": tally, "lane_rounds": len(set(targets)), "reports": len(reports),
            "tokens": len(tokens), "repos": len(repos)}


def _resolve_hashes(tokens, repos):
    """One `git cat-file --batch-check` per repo; returns token -> (repo, objtype)."""
    out = {}
    if not tokens:
        return out
    uniq = sorted(set(tokens))
    payload = "\n".join(uniq) + "\n"
    for r in repos:
        code, text = _git_input(r, ["cat-file", "--batch-check"], payload)
        if code != 0:
            continue
        # `--batch-check` prints one line per input name, in order; a resolved line carries
        # the FULL object id, so the mapping must be positional, not by the printed name.
        for tok, line in zip(uniq, text.splitlines()):
            parts = line.split()
            if len(parts) >= 2 and parts[1] in ("commit", "tree", "blob", "tag"):
                out.setdefault(tok, (r, parts[1]))
    return out


def _git_input(repo, args, payload):
    try:
        done = subprocess.run(["git", "-C", repo] + args, input=payload,
                              capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return -1, ""
    return done.returncode, done.stdout


def _classify(token, resolved, repos):
    if resolved is None:
        if len(token) >= 12:
            # long hex that is no object: a sha1/sha256 content pin (or an abbreviated pin),
            # not a commit citation -- informational, never a defect
            return "pin", "%s unresolved: a content hash/pin, not a commit" % token
        return "dead", "cat-file resolves %s in no local odb (main + 6 child repos + external read-only trees)" % token
    r, objtype = resolved
    if objtype != "commit":
        return "non-commit", "%s resolves to a %s object in %s" % (token, objtype, os.path.basename(r))
    code, _ = run_git(r, ["merge-base", "--is-ancestor", token, "HEAD"])
    if code == 0:
        return "commit", "ancestor of HEAD in %s" % os.path.basename(r)
    return "orphan", "%s resolves in %s but is not an ancestor of its HEAD" % (token, os.path.basename(r))


# ----------------------------------------------------------------------------- analysis

def _canon_sha(obj):
    """Canonical JSON digest: the pin's unit, so byte formatting of the manifest cannot matter."""
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def _file_sha(path):
    try:
        with open(path, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()
    except OSError:
        return None


def _history_pin_check(inp, pin_path=None):
    """Append-only history pin ("`rounds` is append-only after closure").

    rounds[0:k] must hash to the committed digest, and the digest must be anchored to a real
    commit whose own MANIFEST.json bytes still hash to it -- so blessing an in-place edit
    needs a second commit rewriting published bytes, which is reviewable in the pin's diff.
    Appends never invalidate it: rounds[0:k] is unchanged by rounds[k:]. Live mode only.
    Returns (findings, note)."""
    if inp.kind != "live":
        return [], "skipped: a frozen snapshot is pinned by its expected.json input digests"
    path = pin_path or os.path.join(inp.root, HISTORY_PIN_REL)
    pin, err = read_json(path)
    if err:
        return [_finding("-", None, "history-pin", "history_pin", "history_pin_unavailable",
                         "the append-only history pin cannot be evaluated: %s" % err)], None
    k, want = pin.get("k"), pin.get("sha256")
    if not isinstance(k, int) or isinstance(k, bool) or k < 0 or k > len(inp.entries) \
            or not isinstance(want, str) or not re.match(r"^[0-9a-f]{64}$", want):
        return [_finding("-", None, "history-pin", "history_pin", "history_pin_invalid",
                         "pin needs an integer 0 <= k <= len(rounds)=%d and a 64-hex sha256 (got k=%r)"
                         % (len(inp.entries), pin.get("k")))], None
    got = _canon_sha(inp.entries[:k])
    findings = []
    if got != want:
        findings.append(_finding(
            "-", None, "history-pin", "history_pin", "history_pin_mismatch",
            "rounds[0:%d] hashes to %s but the committed pin says %s: closed history was edited in "
            "place (append a closure-correction instead)" % (k, got[:12], want[:12])))
    commit = pin.get("manifest_commit")
    if not commit:
        return findings, "unanchored (no manifest_commit): k=%d prefix=%s" % (k, got[:12])
    code, out = run_git(inp.root, ["show", "%s:MANIFEST.json" % commit])
    if code != 0 or not out:
        findings.append(_finding(
            "-", None, "history-pin", "history_pin", "history_pin_unverifiable",
            "cannot read %s:MANIFEST.json (git exit %s): the pin's anchor cannot be checked"
            % (commit, code)))
        return findings, None
    try:
        anchored = (json.loads(out).get("rounds") or [])[:k]
    except ValueError:
        anchored = None
    if anchored is None:
        findings.append(_finding(
            "-", None, "history-pin", "history_pin", "history_pin_unverifiable",
            "%s:MANIFEST.json does not parse: the pin's anchor cannot be checked" % commit))
        return findings, None
    if _canon_sha(anchored) != want:
        findings.append(_finding(
            "-", None, "history-pin", "history_pin", "history_pin_unanchored",
            "pin names %s but that commit's rounds[0:%d] hashes to %s, not the pinned %s: the pin was "
            "regenerated to bless an edit" % (commit, k, _canon_sha(anchored)[:12], want[:12])))
        return findings, None
    code, _ = run_git(inp.root, ["merge-base", "--is-ancestor", commit, "HEAD"])
    if code != 0:
        findings.append(_finding(
            "-", None, "history-pin", "history_pin", "history_pin_orphan",
            "pin anchor %s is not an ancestor of HEAD: the pinned commit was rewritten or never landed"
            % commit))
        return findings, None
    return findings, "anchored at %s k=%d prefix=%s" % (commit[:9], k, want[:12])


def _frozen_roots(repo):
    """Every committed frozen-baseline root, newest wave first: .ufo/waves/<wave>/frozen."""
    base = os.path.join(repo, ".ufo", "waves")
    roots = []
    if not os.path.isdir(base):
        return roots
    for wave in sorted(os.listdir(base)):
        d = os.path.join(base, wave, "frozen")
        if os.path.isdir(d):
            m = re.search(r"(\d+)", wave)
            roots.append((-(int(m.group(1)) if m else -1), wave, d))
    roots.sort(key=lambda r: (r[0], r[1]))
    return [{"wave": w, "dir": d} for _, w, d in roots]


def _resolve_frozen(repo, which, override=None):
    """-> (frozen_dir, error). A bare NAME matching more than one root fails closed."""
    if override:
        root = override if os.path.isabs(override) else os.path.join(repo, override)
        cand = os.path.join(root, which)
        if os.path.isdir(cand):
            return cand, None
        return None, "no frozen snapshot at %s (--frozen-root %s)" % (cand, override)
    if "/" in which:
        wave, name = which.split("/", 1)
        cand = os.path.join(repo, ".ufo", "waves", wave, "frozen", name)
        if os.path.isdir(cand):
            return cand, None
        return None, "no frozen snapshot at %s" % cand
    roots = _frozen_roots(repo)
    hits = [r for r in roots if os.path.isdir(os.path.join(r["dir"], which))]
    if not hits:
        return None, ("no frozen snapshot named %s under any root (%s)"
                      % (which, ", ".join(r["dir"] for r in roots) or "no .ufo/waves/*/frozen"))
    if len(hits) > 1:
        return None, ("frozen name %s is ambiguous across %d roots (%s): pass --frozen <wave>/%s or "
                      "--frozen-root DIR" % (which, len(hits), ", ".join(h["wave"] for h in hits), which))
    return os.path.join(hits[0]["dir"], which), None


def _prompt_key_from_rel(rel):
    m = re.match(r"^\.ufo/prompts/([a-z]+)-round-(\d+)\.md$", rel)
    return (m.group(1), int(m.group(2))) if m else None


def _untracked_prompts(repo):
    """Generated dispatch evidence that is not durable: `git ls-files -o` under .ufo/prompts.
    Committing them is an integrator-of-record duty (step 4 write scope), so an untracked prompt
    is gate debt, not a note -- the round-10..12 record swept them by hand each round."""
    code, top = run_git(repo, ["rev-parse", "--show-toplevel"])
    if code != 0 or os.path.realpath(top.strip()) != os.path.realpath(repo):
        return None      # not a repo root (e.g. a fixture tree inside another repo): cannot evaluate
    code, out = run_git(repo, ["ls-files", "-o", "--exclude-standard", ".ufo/prompts"])
    if code != 0:
        return None
    return sorted(rel for rel in (l.strip() for l in out.splitlines())
                  if rel.endswith(".md") and _prompt_key_from_rel(rel) is not None)


def _unknown_lane_findings(inp):
    """A lane id no evidence source knows: a dispatch/complete line or a prompt whose lane token
    the lane-id grammar cannot read, so the lane-round cannot join the universe and the line
    cannot be adjudicated. Reported as `unknown_lane` (could-not-evaluate) instead of dropped --
    a blind spot is the failure mode the universe exists to prevent (A:42)."""
    out = []
    for key in sorted(inp.foreign, key=lambda k: (str(k[0]), k[1])):
        lane, n = key
        evs = inp.foreign[key]
        kinds = sorted({e.get("kind", "unreadable") for e in evs})
        lines = "; ".join(sorted({e["text"].strip() for e in evs if e.get("text")}))
        out.append(_finding(lane, n, "lane-universe", "unknown_lane", "lane-outside-universe",
                            "lane-round (%s,%d): lane id %r is in no universe source (roster u base "
                            "lanes u driver counters u dispatch lines u prompts) and the line cannot "
                            "be read as a lane id (%s): %s" % (lane, n, lane, ",".join(kinds), lines or "-")))
    for key in sorted(inp.foreign_prompts, key=lambda k: (str(k[0]), k[1])):
        lane, n = key
        out.append(_finding(lane, n, "lane-universe", "unknown_lane", "prompt-lane-outside-universe",
                            "prompt names lane-round (%s,%d), a lane outside the universe: the "
                            "attempted dispatch cannot be adjudicated (A:42)" % (lane, n)))
    return out


def analyze(inp, opts):
    led = build_ledger(inp.entries, inp.allowed)
    rows, all_rows = led["rows"], led["all_rows"]
    unadjudicable, unadj_keys = led["unadjudicable"], led["unadj_keys"]
    nonclosure = led["nonclosure"]
    pin_findings, pin_note = _history_pin_check(inp, opts.get("pin"))
    # `debt` is the unit a frozen baseline pins, and an unadjudicable id must not read as a
    # defect of the ledger: every finding is classified by COULD_NOT_EVALUATE_CLASSES, and a
    # could-not-evaluate finding raises the exit code to 2 only when there is no debt at all.
    findings = (list(led["shape"]) + pin_findings + list(led["unadjudicable_ids"])
                + _unknown_lane_findings(inp))
    cne = [f for f in findings if f["class"] in COULD_NOT_EVALUATE_CLASSES]
    debt = [f for f in findings if f["class"] not in COULD_NOT_EVALUATE_CLASSES]
    contradictions = [f for f in debt if f["class"] == "contradiction"]
    live_in_flight = []
    pending_round = []
    unlanded = []
    unrowed = []
    after_closure = []
    row_findings = {}     # (lane, round) -> finding dict (dedup)

    # closure instant per round (latest closed_at among entries naming that round)
    closure = {}
    for e in inp.entries:
        if isinstance(e, dict) and e.get("closed_at"):
            dt = iso(e["closed_at"])
            r = e.get("round")
            if dt is not None and (r not in closure or dt > closure[r]):
                closure[r] = dt

    def first_dispatch(lane, n):
        evs = inp.dispatch.get((lane, n))
        return evs[0] if evs else None

    def complete_ts(lane, n):
        evs = inp.completes.get((lane, n))
        return evs[0]["ts"] if evs else None

    def landed_report(lane, n):
        """A report at the contract path counts as evidence only when LANDED (PROTOCOL "Lands
        last"): an uncommitted file from a live mission is not termination evidence, even
        though it fires the driver's existence-only report_of() signal. A frozen snapshot uses
        the pinned add-commit time (`landed_at`) against the snapshot's closed_at, so evidence
        that arrived after the snapshot instant never leaks in."""
        rep = inp.report(lane, n)
        if rep is None:
            return False
        if inp.kind == "frozen":
            la = rep.get("landed_at")
            return bool(la is not None and inp.instant is not None and la <= inp.instant)
        code, _ = run_git(inp.root, ["ls-files", "--error-unmatch", rep["rel"]])
        return code == 0

    def terminated(lane, n):
        return (complete_ts(lane, n) is not None or inp.counters.get(lane, 0) > n
                or landed_report(lane, n))

    def report_status(lane, n):
        rep = inp.report(lane, n)
        if rep is None:
            return "failed", "no report at %s" % inp.contract_rel(lane, n)
        if rep.get("marker"):
            return "failed", "marker at %s (%s B, no commit hash, no SHONEN heading)" % (
                rep["rel"], rep["bytes"])
        return "ok", "report %s (%s B)" % (rep["rel"], rep["bytes"])

    # ---- lane_rounds identity (the naive-re-keying trap) -------------------
    dispatch_keys = set(inp.dispatch)
    complete_keys = set(inp.completes)
    seen_keying = set()
    for row in sorted(all_rows, key=lambda x: (lane_sort(x["lane"]), x["round"], x["entry"])):
        lane, r, v, st = row["lane"], row["round"], row["counter"], row["status"]
        if not isinstance(v, int) or isinstance(v, bool):
            continue                      # already a shape contradiction
        if st == "not-dispatched" and v >= r:
            f = _finding(lane, r, "row", "keying_violation", "not-dispatched-counter-not-behind",
                         "not-dispatched row (entry #%d) but lane_rounds[%s]=%d is not behind the entry round %d (P:241-247)" % (
                             row["entry"], lane, v, r))
            debt.append(f)
            row_findings.setdefault((lane, r), f)
            continue
        if v == r:
            continue
        if (lane, v) not in dispatch_keys and (lane, v) not in complete_keys \
                and (lane, v) not in rows and (lane, v) not in unadj_keys:
            f = _finding(lane, r, "row", "keying_violation", "lane_rounds-identity-absent",
                         "lane_rounds[%s]=%d names lane-round (%s,%d) with no dispatch/complete line and no ledger row (P:244-249)" % (
                             lane, v, lane, v))
            debt.append(f)
            row_findings.setdefault((lane, r), f)
            continue
        if st in ("ok", "in-flight") and row["entry_type"] != "retroactive-closure":
            ca = iso(row["closed_at"]) if row["closed_at"] else None
            mx = 0
            if ca is not None:
                for (l2, n2), evs in inp.dispatch.items():
                    if l2 == lane and evs[0]["ts"] is not None and evs[0]["ts"] <= ca:
                        mx = max(mx, n2)
            if mx > v:
                f = _finding(lane, r, "row", "keying_violation", "lane_rounds-behind-counter",
                             "entry #%d lane_rounds[%s]=%d but the lane's counter at closed_at (%s) was already %d by dispatch evidence (P:244-249)" % (
                                 row["entry"], lane, v, row["closed_at"] or "-", mx))
                debt.append(f)
                row_findings.setdefault((lane, r), f)
                continue

    # ---- ledger rows -------------------------------------------------------
    for key in sorted(rows, key=lambda k: (lane_sort(k[0]), k[1])):
        row = rows[key]
        lane, n, st, ca = row["lane"], row["round"], row["status"], iso(row["closed_at"])
        if st == "ok":
            rep = inp.report(lane, n)
            if rep is None:
                f = _finding(lane, n, "row", "contradiction", "ok-without-report",
                             "ok row (entry #%d) but no report at %s (P:247-248)" % (row["entry"], inp.contract_rel(lane, n)))
                debt.append(f)
                contradictions.append(f)
                row_findings[key] = f
            elif rep.get("marker"):
                f = _finding(lane, n, "row", "contradiction", "ok-vs-marker",
                             "ok row (entry #%d) but %s is a marker: %s B, no commit hash, no SHONEN heading (P:150-155)" % (
                                 row["entry"], rep["rel"], rep["bytes"]))
                debt.append(f)
                contradictions.append(f)
                row_findings[key] = f
        elif st == "failed":
            rep = inp.report(lane, n)
            if rep is not None and not rep.get("marker") and inp.report_seen_by(lane, n, ca):
                f = _finding(lane, n, "row", "contradiction", "failed-vs-report",
                             "failed row (entry #%d) but %s is a real report present at/before closed_at (P:150-155)" % (
                                 row["entry"], rep["rel"]))
                debt.append(f)
                contradictions.append(f)
                row_findings[key] = f
        elif st == "in-flight":
            cts = complete_ts(lane, n)
            ev = None
            if cts is not None and ca is not None and cts <= ca:
                ev = "in-flight row (entry #%d) but `%s` predates closed_at" % (
                    row["entry"], inp.completes[(lane, n)][0]["text"].strip())
            elif inp.report_seen_by(lane, n, ca):
                ev = "in-flight row (entry #%d) but report %s was present at/before closed_at (P:224-228)" % (
                    row["entry"], inp.contract_rel(lane, n))
            elif ca is not None:
                d = first_dispatch(lane, n)
                if d is None or d["ts"] is None or d["ts"] > ca:
                    ev = "in-flight row (entry #%d) but no dispatch line at/before closed_at (P:241-243)" % row["entry"]
            if ev is not None:
                f = _finding(lane, n, "row", "contradiction", "in-flight-terminated", ev)
                debt.append(f)
                contradictions.append(f)
                row_findings[key] = f
            else:
                d = first_dispatch(lane, n)
                ptr = d["text"].strip() if d else "(no launch line)"
                if terminated(lane, n):
                    sug, why = report_status(lane, n)
                    rep_u = inp.report(lane, n)
                    if rep_u is not None and not landed_report(lane, n):
                        unlanded.append({"lane": lane, "lane_round": n, "entry": row["entry"],
                                         "status": "terminated (complete line / counter) but the report at the path is UNLANDED",
                                         "report": rep_u["rel"], "bytes": rep_u["bytes"],
                                         "marker": bool(rep_u.get("marker")),
                                         "shonen_heading": bool(rep_u.get("has_shonen")),
                                         "tracked": False,
                                         "driver_signal": "the driver's report_of() completed on this file's existence; PROTOCOL Lands-last does not",
                                         "hash_identity": hash_identity_note(inp, lane, rep_u["rel"])})
                    f = _finding(lane, n, "row", "stale_in_flight", "in-flight-terminated-since",
                                 "in-flight row (entry #%d); mission terminated since closed_at: %s" % (
                                     row["entry"], why), sug)
                    f["launch"] = ptr
                    debt.append(f)
                    row_findings[key] = f
                else:
                    live_in_flight.append({"lane": lane, "lane_round": n, "entry": row["entry"],
                                           "closed_at": row["closed_at"], "launch": ptr})
                    rep = inp.report(lane, n)
                    if rep is not None:
                        unlanded.append({"lane": lane, "lane_round": n, "entry": row["entry"],
                                         "status": "live_in_flight -> re-confirm", "report": rep["rel"],
                                         "bytes": rep["bytes"], "marker": bool(rep.get("marker")),
                                         "shonen_heading": bool(rep.get("has_shonen")),
                                         "tracked": bool(rep.get("tracked")) if inp.kind == "frozen" else False,
                                         "driver_signal": "the driver's report_of() completes on this file's existence",
                                         "hash_identity": hash_identity_note(inp, lane, rep["rel"])})
        elif st == "not-dispatched":
            d = first_dispatch(lane, n)
            if d is not None and ca is not None:
                if d["ts"] is not None and d["ts"] <= ca:
                    f = _finding(lane, n, "row", "contradiction", "not-dispatched-vs-dispatch",
                                 "not-dispatched row (entry #%d) but dispatch evidence exists at/before closed_at: `%s` (P:241-243)" % (
                                     row["entry"], d["text"].strip()))
                    debt.append(f)
                    contradictions.append(f)
                    row_findings[key] = f
                else:
                    if terminated(lane, n):
                        sug, why = report_status(lane, n)
                        f = _finding(lane, n, "row", "unrowed_terminated", "superseded-not-dispatched",
                                     "dispatched after round %s closed (row entry #%d; dispatch %s); termination evidence present (%s, %s): %s" % (
                                         n, row["entry"], d["text"].strip(), _complete_note(inp, lane, n),
                                         _counter_note(inp, lane, n), why), sug)
                        f["launch"] = d["text"].strip()
                        debt.append(f)
                        unrowed.append(f)
                        row_findings[key] = f
                    else:
                        f = _finding(lane, n, "row", "pending_round", "superseded-not-dispatched",
                                     "dispatched after round %s closed (row entry #%d); no termination yet -> rides the next closure-correction for %s" % (
                                         n, row["entry"], n))
                        f["launch"] = d["text"].strip()
                        pending_round.append(f)
                        unrowed.append(f)
                        row_findings[key] = f

    # ---- dispatch keys / prompt orphans -----------------------------------
    for key in sorted(set(inp.dispatch) | set(inp.prompts), key=lambda k: (lane_sort(k[0]), k[1])):
        lane, n = key
        if key in rows or key in row_findings:
            continue
        if key in unadj_keys:
            continue       # legacy-typed row: unadjudicable, not a missing row
        d = first_dispatch(lane, n)
        if d is None:
            f = _finding(lane, n, "prompt", "prompt_orphan", "prompt-no-dispatch",
                         "prompt .ufo/prompts/%s-round-%d.md with no dispatch line -> attempted dispatch, records `failed` (P:218-221)" % (lane, n),
                         report_status(lane, n)[0])
            debt.append(f)
            unrowed.append(f)
            row_findings[key] = f
        else:
            if terminated(lane, n):
                sug, why = report_status(lane, n)
                f = _finding(lane, n, "dispatch", "unrowed_terminated", "no-row",
                             "dispatch `%s` with termination evidence and no row: %s, %s" % (
                                 d["text"].strip(), _complete_note(inp, lane, n), _counter_note(inp, lane, n)), sug)
                debt.append(f)
                unrowed.append(f)
                row_findings[key] = f
            else:
                f = _finding(lane, n, "dispatch", "pending_round", "no-row",
                             "dispatched `%s` and no row written; round %s has %s -> informational (partial-entries rule, P:209-213)" % (
                                 d["text"].strip(), n, "an entry" if closure.get(n) else "no entry yet"))
                f["launch"] = d["text"].strip()
                pending_round.append(f)
                unrowed.append(f)
                row_findings[key] = f

    # ---- untracked dispatch evidence (durability duty) ---------------------
    untracked_prompts = _untracked_prompts(inp.root) if inp.kind == "live" else None
    for rel in (untracked_prompts or []):
        key = _prompt_key_from_rel(rel)
        if key is None:            # defensive: keep parser/filter refactors fail-safe
            continue
        lane, n = key
        try:
            nbytes = os.path.getsize(os.path.join(inp.root, rel))
        except OSError:
            nbytes = -1
        f = _finding(lane, n, "prompt", "prompt_untracked", "prompt-not-durable",
                     "%s (%d B) is untracked: generated dispatch evidence is non-durable until the "
                     "integrator commits it (step-4 write scope)" % (rel, nbytes))
        debt.append(f)
        unrowed.append(f)

    # ---- dispatched after their round's closure ---------------------------
    for key in sorted(inp.dispatch, key=lambda k: (lane_sort(k[0]), k[1])):
        lane, n = key
        c = closure.get(n)
        d = first_dispatch(lane, n)
        if c is None or d is None or d["ts"] is None or d["ts"] <= c:
            continue
        f = {"lane": lane, "lane_round": n, "dispatched": d["text"].strip(),
             "round_closed_at": c.isoformat(), "rides": n}
        after_closure.append(f)

    # ---- tallies ----------------------------------------------------------
    entry_keyed = _tally(rows.values())
    lane_round_keyed = _lane_round_keying_tally(inp.entries)
    all_entry_keyed = _all_entries_keying_tally(inp.entries)

    # ---- stale missions ---------------------------------------------------
    stale = []
    live_missions = []
    if inp.kind == "frozen":
        now = _newest_closed_at(inp.entries) or datetime.now().astimezone()
    else:
        now = datetime.now().astimezone()
    for lane in inp.allowed:
        keys = [k for k in inp.dispatch if k[0] == lane]
        if not keys:
            continue
        key = max(keys, key=lambda k: (epoch(inp.dispatch[k][0]["ts"]), k[1], inp.dispatch[k][0]["line"]))
        if terminated(lane, key[1]):
            continue
        d = first_dispatch(lane, key[1])
        if d is None:
            continue
        age = None if d["ts"] is None else (now - d["ts"]).total_seconds()
        root = lane_repo(inp, lane)
        pats = MAIN_SCOPE.get(lane) if lane in MAIN_LANES else None
        commits = git_activity(root, d["ts"])
        lane_commits = [c for c in commits if c[1].startswith(lane + "-") or c[1] == lane]
        files = fs_activity(root, d["ts"], pats)
        file_authors = {}
        for f in files[:4]:
            file_authors[f] = file_author(root, f)
        own_files = [f for f in files if (file_authors.get(f) or "").startswith(lane)]
        unattr = [f for f in files if file_authors.get(f) is None and not sibling_owned(f)]
        sibling_authors = sorted({a for a in file_authors.values()
                                  if a and not a.startswith(lane)})
        if lane_commits:
            verdict = "progressing"
            ev = ["lane commit: %s %s" % (lane_commits[0][0], lane_commits[0][1])]
        elif own_files or unattr:
            verdict = "progressing"
            ev = ["lane file: %s" % (own_files or unattr)[0]]
        elif sibling_authors:
            verdict = "progressing-weak"
            lanes_of = [a for a in sibling_authors if a.endswith("-shokunin")]
            others = [a for a in sibling_authors if not a.endswith("-shokunin")]
            parts = []
            if lanes_of:
                parts.append("sibling-lane activity by %s" % ", ".join(lanes_of))
            if others:
                parts.append("activity by %s, not a lane identity (lane-identity defect, not a sibling)"
                             % ", ".join(others))
            ev = ["%s; no lane-authored commit/file since launch: %s" % (
                "; ".join(parts), files[0] if files else "-")]
        else:
            verdict = "silent"
            ev = ["no lane-authored commit and no file newer than the launch"]
        rec = {"lane": lane, "lane_round": key[1], "launch": d["text"].strip(),
               "age_seconds": None if age is None else int(age), "verdict": verdict,
               "evidence": "; ".join(ev)}
        live_missions.append(rec)
        if age is not None and age > TWO_TICKS_S:
            stale.append(rec)

    # ---- citations --------------------------------------------------------
    citation_tally = {}
    if opts.get("citations") and inp.kind == "live":
        # closure step 1 verifies EVERY lane report: sweep every lane-round in the ledger,
        # plus the non-ledger findings (pending dispatches, re-confirmations).
        targets = {(row["lane"], row["round"]) for row in rows.values()}
        for f in debt + live_in_flight + pending_round:
            if f.get("lane") in inp.allowed and isinstance(f.get("lane_round"), int):
                targets.add((f["lane"], f["lane_round"]))
        sweep = citation_sweep(inp, inp.root, targets)
        inp.citations = sweep["findings"]
        citation_tally = sweep["tally"]
        inp.citation_scope = ("%d lane-rounds / %d reports on disk / %d tokens / %d repos, identity "
                              "resolved by full-odb cat-file per repo" % (
                                  sweep["lane_rounds"], sweep["reports"], sweep["tokens"], sweep["repos"]))

    exit_code = EXIT_DEBT if debt else (EXIT_ERROR if cne else EXIT_OK)
    verdict = "debt" if debt else ("could-not-evaluate" if cne else "ok")
    result = {
        "verdict": verdict,
        "exit": exit_code,
        "debt": _sorted_debt(debt),
        "could_not_evaluate": _sorted_debt(cne),
        "nonclosure": nonclosure,
        "live_in_flight": sorted(live_in_flight, key=lambda f: (lane_sort(f["lane"]), f["lane_round"])),
        "pending_round": sorted(pending_round, key=lambda f: (lane_sort(f["lane"]), f["lane_round"])),
        "unadjudicable": unadjudicable,
        "history_pin": {"note": pin_note, "findings": pin_findings},
        "untracked_prompts": untracked_prompts or [],
        "lane_universe": {"allowed": list(inp.allowed), "roster_ids": list(inp.roster_ids),
                          "counter_only": list(inp.counter_only),
                          "unreadable_ids": sorted("%s r%s" % k for k in inp.foreign)},
        "tallies": entry_keyed,
        "keying_tallies": {"entry_keyed": entry_keyed, "lane_round_keyed": lane_round_keyed,
                          "all_entries_entry_keyed": all_entry_keyed},
        "contradictions": [f for f in _sorted_debt(debt) if f["class"] == "contradiction"],
        "unrowed": sorted(unrowed, key=lambda f: (lane_sort(f["lane"]), f["lane_round"])),
        "unrowed_terminated": [f for f in _sorted_debt(debt) if f["class"] == "unrowed_terminated"],
        "unlanded_report_at_path": unlanded,
        "counts": _counts({"debt": debt, "contradictions": contradictions, "unrowed": unrowed,
                           "live_in_flight": live_in_flight, "pending_round": pending_round,
                           "could_not_evaluate": cne, "nonclosure": nonclosure}),
        "after_closure": after_closure,
        "stale_missions": stale,
        "live_missions": live_missions,
        "citations": inp.citations,
        "citation_tally": citation_tally,
        "citation_scope": inp.citation_scope,
        "ledger": [rows[k] for k in sorted(rows, key=lambda k: (lane_sort(k[0]), k[1]))],
        "meta": {"repo": inp.root, "kind": inp.kind, "entries": len(inp.entries),
                 "log_lines": len(inp.log_lines),
                 "dispatch_events": sum(len(v) for v in inp.dispatch.values()),
                 "complete_events": sum(len(v) for v in inp.completes.values()),
                 "lanes_with_counters": sorted(inp.counters)},
    }
    return result


def _newest_closed_at(entries):
    best = None
    for e in entries:
        if isinstance(e, dict) and e.get("closed_at"):
            dt = iso(e["closed_at"])
            if dt is not None and (best is None or dt > best):
                best = dt
    return best


def _complete_note(inp, lane, n):
    evs = inp.completes.get((lane, n))
    if evs:
        return "complete at %s" % evs[0]["text"].strip().split(" ")[0]
    return "no complete line"


def _counter_note(inp, lane, n):
    c = inp.counters.get(lane)
    if c is None:
        return "counter unknown"
    return "counter %d%s" % (c, "" if c > n else " (not past %d)" % n)


def _sorted_debt(debt):
    return sorted(debt, key=lambda f: (lane_sort(f["lane"]),
                                       f["lane_round"] if isinstance(f.get("lane_round"), int) else -1,
                                       f.get("class", ""), f.get("kind", "")))


def _tally(rows):
    counts = {s: 0 for s in STATUSES}
    other = 0
    for row in rows:
        st = row.get("status")
        if st in counts:
            counts[st] += 1
        else:
            other += 1
    return {"ok": counts["ok"], "failed": counts["failed"], "in_flight": counts["in-flight"],
            "not_dispatched": counts["not-dispatched"], "invalid": other,
            "rows": sum(counts.values()) + other}


def _entry_lane_items(e):
    """(lane, status) pairs of an entry, tolerant of a list-shaped `lanes` (malformed, still
    adjudicated defensively so a mutant on it produces a verdict, never a traceback)."""
    raw = e.get("lanes") if isinstance(e, dict) else None
    if isinstance(raw, dict):
        return list(raw.items())
    if isinstance(raw, list):
        out = []
        for item in raw:
            if isinstance(item, dict):
                out.extend(item.items())
        return out
    return []


def _lane_round_keying_tally(entries):
    rows = {}
    for e in entries:
        if not isinstance(e, dict):
            continue
        lr = e.get("lane_rounds") if isinstance(e.get("lane_rounds"), dict) else {}
        for lane, st in _entry_lane_items(e):
            rows[(lane, lr.get(lane, e.get("round")))] = st
    return _tally([{"status": s} for s in rows.values()])


def _all_entries_keying_tally(entries):
    rows = {}
    for e in entries:
        if not isinstance(e, dict):
            continue
        for lane, st in _entry_lane_items(e):
            rows[(lane, e.get("round"))] = st
    return _tally([{"status": s} for s in rows.values()])


# ----------------------------------------------------------------------------- render

def _render_open_findings(out, result):
    """The two buckets that are neither a status row nor debt: findings the gate cannot
    adjudicate (exit-2 drivers) and non-closure entries (reported, never skipped)."""
    out.append("")
    cne = result.get("could_not_evaluate") or []
    out.append("== Could not evaluate (exit-%d drivers): %d ==" % (EXIT_ERROR, len(cne)))
    if not cne:
        out.append("none")
    for f in cne:
        out.append("%-22s %-10s r%-4s %s" % (f["class"], f["lane"], f["lane_round"], f["evidence"]))
    nc = result.get("nonclosure") or []
    out.append("")
    out.append("== Non-closure entries (recognized types: reported, excluded from lane-status tallies) ==")
    if not nc:
        out.append("none")
    for e in nc:
        out.append("entry #%-4s round=%-6s type=%-9s recognized=%-3s lanes=%d notes=%s" % (
            e["entry"], e["round"], e["type"], "yes" if e.get("recognized") else "NO",
            len(e.get("lanes") or {}), "yes" if e.get("notes") else "no"))
    return out


def render_text(result, opts):
    out = []
    counts = _counts(result)
    out.append(verdict_line(result))
    meta = result["meta"]
    out.append("repo: %s  mode: %s  manifest entries: %d  log lines: %d  dispatches: %d  completes: %d" % (
        meta["repo"], meta["kind"], meta["entries"], meta["log_lines"],
        meta["dispatch_events"], meta["complete_events"]))
    out.append("keying: entry-keyed (a row names (lane, entry.round); lane_rounds annotates, never re-keys)")
    lu = result.get("lane_universe") or {}
    out.append("lane universe: %d lanes (%s)%s" % (
        len(lu.get("allowed") or []), ", ".join(lu.get("allowed") or []),
        "  counter-only (probation, no roster row): %s" % ", ".join(lu["counter_only"])
        if lu.get("counter_only") else ""))
    hp = result.get("history_pin") or {}
    if hp.get("findings"):
        out.append("history pin: %d finding(s) - see Debt" % len(hp["findings"]))
    else:
        out.append("history pin: %s" % (hp.get("note") or "not evaluated"))

    out.append("")
    if opts.get("no_ledger"):
        out.append("== Ledger (last-wins, entry-keyed): %d status rows (table suppressed by --no-ledger; use --json for rows) ==" % len(result["ledger"]))
    else:
        out.append("== Ledger (last-wins, entry-keyed): %d status rows ==" % len(result["ledger"]))
        out.append("%-10s %5s  %-14s %5s  %-19s %-25s %s" % ("lane", "round", "status", "entry", "type", "closed_at", "counter"))
        for row in result["ledger"]:
            out.append("%-10s %5s  %-14s %5d  %-19s %-25s %s" % (
                row["lane"], row["round"], row["status"], row["entry"], row["entry_type"],
                row["closed_at"] or "-", row["counter"] if row["counter"] is not None else "-"))

    if result["unadjudicable"]:
        out.append("")
        out.append("== Unadjudicable (legacy-typed entries: fleet-keyed, never a lane-round status) ==")
        out.append("statuses inside these entries are not integrity-protected: a status edit here is "
                   "mutant not-applicable, not a gate blind spot")
        for u in result["unadjudicable"]:
            lanes = ", ".join("%s=%s" % (k, u["lanes"][k]) for k in sorted(u["lanes"]))
            out.append("entry #%d round=%s type=%s  %s" % (u["entry"], u["round"], u["type"], lanes))

    out.append("")
    out.append("== Debt (exit-%d drivers): %d ==" % (EXIT_DEBT, counts["debt"]))
    if not result["debt"]:
        out.append("none")
    for f in result["debt"]:
        out.append("%-22s %-10s r%-4s entry=%-4s %s" % (
            f["class"], f["lane"], f["lane_round"], _entry_of(result, f), f["evidence"]))
        if f.get("suggested_status"):
            out.append("    suggested status: %s" % f["suggested_status"])
        if f.get("launch"):
            out.append("    launch pointer: %s" % f["launch"])
    _render_open_findings(out, result)

    out.append("")
    out.append("== Live in-flight (compliant: re-confirm next pass with the launch pointer) ==")
    if not result["live_in_flight"]:
        out.append("none")
    for f in result["live_in_flight"]:
        out.append("%-10s r%-4s entry=%-4s %s" % (f["lane"], f["lane_round"], f["entry"], f["launch"]))

    out.append("")
    out.append("== Unlanded report at the contract path (driver signal vs ledger) ==")
    if not result.get("unlanded_report_at_path"):
        out.append("none")
    for u in result.get("unlanded_report_at_path", []):
        out.append("%-10s r%-4s entry=%-4s %s (%s B, marker=%s, SHONEN=%s, tracked=%s)" % (
            u["lane"], u["lane_round"], u["entry"], u["report"], u["bytes"], u["marker"],
            u.get("shonen_heading"), u.get("tracked")))
        out.append("    status: %s" % u["status"])
        out.append("    %s" % u["driver_signal"])
        out.append("    %s" % u["hash_identity"])

    out.append("")
    out.append("== Pending rounds (informational: no termination yet) ==")
    if not result["pending_round"]:
        out.append("none")
    for f in result["pending_round"]:
        out.append("%-10s r%-4s %s" % (f["lane"], f["lane_round"], f["evidence"]))

    out.append("")
    out.append("== Contradictions (rows vs evidence): %d ==" % counts["contradictions"])
    if not result["contradictions"]:
        out.append("none")
    for f in result["contradictions"]:
        out.append("%-10s r%-4s %-32s %s" % (f["lane"], f["lane_round"], f["kind"], f["evidence"]))

    out.append("")
    out.append("== Dispatched, no valid row (unrowed=%d; pending rows are informational, terminated ones are debt) ==" % counts["unrowed"])
    if not result["unrowed"]:
        out.append("none")
    for f in result["unrowed"]:
        out.append("%-22s %-10s r%-4s %s" % (f["class"], f["lane"], f["lane_round"], f["kind"]))

    out.append("")
    out.append("== Dispatched after their round's closure (rides the next closure-correction for N) ==")
    if not result["after_closure"]:
        out.append("none")
    for f in result["after_closure"]:
        out.append("%-10s r%-4s dispatched %s after round %s closed %s -> rides the next closure-correction for %s" % (
            f["lane"], f["lane_round"], f["dispatched"].split(" ")[0], f["rides"],
            f["round_closed_at"], f["rides"]))

    out.append("")
    out.append("== Tallies ==")
    ek = result["keying_tallies"]["entry_keyed"]
    ak = result["keying_tallies"]["all_entries_entry_keyed"]
    lk = result["keying_tallies"]["lane_round_keyed"]
    out.append("entry-keyed, adjudicated (closure*) entries only: %s" % _tally_text(ek))
    out.append("entry-keyed, all entries incl. legacy fleet-keyed rows: %s" % _tally_text(ak))
    if opts.get("show_keying"):
        out.append("lane_rounds-keyed (non-authoritative, --show-keying): %s" % _tally_text(lk))
    out.append("unadjudicable rows: %d (entries %s)" % (
        sum(len(u["lanes"]) for u in result["unadjudicable"]),
        ", ".join("#%d" % u["entry"] for u in result["unadjudicable"])))
    out.append("live missions: %d (stale > %d s: %d)" % (
        len(result["live_missions"]), TWO_TICKS_S, len(result["stale_missions"])))

    out.append("")
    out.append("== Stale missions (> %d s since launch; activity probe, not a verdict) ==" % TWO_TICKS_S)
    if not result["stale_missions"]:
        out.append("none")
    else:
        out.append("%-10s %5s  %-25s %8s  %-12s %s" % ("lane", "round", "launched", "age_s", "verdict", "evidence"))
        for m in result["stale_missions"]:
            out.append("%-10s %5s  %-25s %8s  %-12s %s" % (
                m["lane"], m["lane_round"], m["launch"].split(" ")[0], m["age_seconds"],
                m["verdict"], m["evidence"]))

    if result["citations"] or result["citation_scope"] != "disabled":
        out.append("")
        out.append("== Report citations (%s) ==" % result["citation_scope"])
        t = result.get("citation_tally") or {}
        out.append("token classes: commit=%s pin=%s runId/date=%s dead=%s orphan=%s non-commit=%s placeholder=%s" % (
            t.get("commit", 0), t.get("pin", 0), t.get("runId/date", 0), t.get("dead", 0),
            t.get("orphan", 0), t.get("non-commit", 0), t.get("placeholder", 0)))
        def _rnd(f):
            parts = f["report"].split("/")
            m = ROUND_DIR_RE.match(parts[2]) if len(parts) > 2 else None
            return (-float(m.group(1)) if m else 0.0, f["report"], f["line"])
        findings = sorted(result["citations"], key=_rnd)
        if not findings:
            out.append("no dead/orphan/non-commit/placeholder citations")
        for c in findings[:25]:
            out.append("%-14s %s:%d %s  (%s)" % (c["kind"], c["report"], c["line"], c["token"], c["detail"]))
        if len(findings) > 25:
            out.append("... %d more findings (--json for the full list)" % (len(findings) - 25))
    return "\n".join(out)


def verdict_line(result):
    """The one-line machine-readable verdict: debt classes drive the exit code, could-not-evaluate
    findings raise it to 2 only when there is no debt (non-closure entries are informational)."""
    c = _counts(result)
    return ("closure-check: %s debt=%d contradictions=%d unrowed_terminated=%d pending_round=%d "
            "cne=%d nonclosure=%d" % (
                result["verdict"], c["debt"], c["contradictions"], c["unrowed_terminated"],
                c["pending_round"], c["could_not_evaluate"], c["nonclosure"]))


def _tally_text(t):
    return "ok=%d failed=%d in-flight=%d not-dispatched=%d rows=%d" % (
        t["ok"], t["failed"], t["in_flight"], t["not_dispatched"], t["rows"])


def _entry_of(result, f):
    for row in result["ledger"]:
        if row["lane"] == f["lane"] and row["round"] == f["lane_round"]:
            return row["entry"]
    return "-"


def _counts(result):
    debt = result["debt"]
    by_class = {}
    for f in debt:
        by_class[f["class"]] = by_class.get(f["class"], 0) + 1
    cne = result.get("could_not_evaluate") or []
    cne_class = {}
    for f in cne:
        cne_class[f["class"]] = cne_class.get(f["class"], 0) + 1
    nonclosure = result.get("nonclosure") or []
    return {"debt": len(debt), "contradictions": by_class.get("contradiction", 0),
            "unrowed_terminated": by_class.get("unrowed_terminated", 0),
            "prompt_orphan": by_class.get("prompt_orphan", 0),
            "stale_in_flight": by_class.get("stale_in_flight", 0),
            "history_pin": by_class.get("history_pin", 0),
            "unknown_lane": cne_class.get("unknown_lane", 0),
            "unknown_entry_type": cne_class.get("unknown_entry_type", 0),
            "could_not_evaluate": len(cne),
            "nonclosure": len(nonclosure),
            "nonclosure_unrecognized": sum(1 for e in nonclosure if not e.get("recognized")),
            "unrowed": len(result["unrowed"]), "live_in_flight": len(result["live_in_flight"]),
            "pending_round": len(result["pending_round"]), "by_class": by_class}


# ----------------------------------------------------------------------------- modes

def do_live(repo, opts):
    inp, err = load_live(repo)
    if err:
        return _error_result(repo, err)
    result = analyze(inp, opts)
    return result


def _error_result(root, message):
    return {"verdict": "error", "exit": EXIT_ERROR, "error": message, "meta": {"repo": root}}


def do_frozen(repo, which, opts, root_override=None):
    frozen_dir, err = _resolve_frozen(repo, which, root_override)
    if err:
        return {"verdict": "no-baseline", "exit": EXIT_NOBASELINE, "error": err,
                "meta": {"repo": repo, "frozen": which}}
    inp, err = load_frozen(frozen_dir)
    if err:
        return _error_result(repo, err)
    result = analyze(inp, opts)
    baseline, err = read_json(os.path.join(frozen_dir, "expected.json"))
    result["meta"]["frozen"] = which
    result["meta"]["frozen_dir"] = frozen_dir
    if err:
        result["verdict"] = "no-baseline"
        result["exit"] = EXIT_NOBASELINE
        result["baseline"] = {"status": "missing", "detail": err}
        return result
    # A baseline that pins its own inputs is verified first: an edited snapshot proves nothing.
    digests = baseline.get("inputs")
    if not isinstance(digests, dict) or not digests:
        result["baseline_inputs"] = {"status": "unpinned",
                                     "detail": "expected.json carries no input digests (legacy baseline)"}
    else:
        bad = []
        for rel in sorted(digests):
            got = _file_sha(os.path.join(frozen_dir, rel))
            if got != digests[rel]:
                bad.append("%s: pinned %s, snapshot has %s"
                           % (rel, str(digests[rel])[:12], (got or "<missing>")[:12]))
        if bad:
            result["verdict"] = "could-not-evaluate"
            result["exit"] = EXIT_ERROR
            result["baseline_inputs"] = {"status": "snapshot_tampered", "detail": bad}
            result["baseline"] = {"status": "snapshot_tampered", "diffs": bad}
            return result
        result["baseline_inputs"] = {"status": "match", "files": len(digests)}
    match, diffs = _compare_baseline(result, baseline)
    result["baseline"] = {"status": "match" if match else "MISMATCH", "expected": baseline, "diffs": diffs}
    if match:
        result["exit"] = int(baseline.get("exit", result["exit"]))
    else:
        result["exit"] = EXIT_DEBT
    return result


def _compare_baseline(result, baseline):
    actual = _canon_debt(result["debt"])
    expected = _canon_debt(baseline.get("debt") or [])
    diffs = []
    for row in expected:
        if row not in actual:
            diffs.append("expected, not found: %s" % json.dumps(row, sort_keys=True))
    for row in actual:
        if row not in expected:
            diffs.append("found, not expected: %s" % json.dumps(row, sort_keys=True))
    if int(baseline.get("exit", -1)) != result["exit"]:
        diffs.append("exit: expected %s, analyzed %s" % (baseline.get("exit"), result["exit"]))
    return (not diffs), diffs


def _canon_debt(debt):
    """The pinned unit is the debt set as (lane, lane_round, class) triples; the evidence
    strings are prose and are printed beside the baseline, not compared."""
    return [{"lane": f["lane"], "lane_round": f["lane_round"], "class": f["class"]}
            for f in _sorted_debt(debt)]


def do_selftest(script_dir, opts):
    root = os.path.join(script_dir, "fixtures", "closure-sample")
    if not os.path.isdir(root):
        return {"verdict": "no-baseline", "exit": EXIT_NOBASELINE,
                "error": "no fixture root at %s" % root, "cases": [], "passed": 0, "total": 0,
                "meta": {"repo": root}}
    cases = []
    missing_baseline = []
    for name in sorted(os.listdir(root)):
        case_dir = os.path.join(root, name)
        if not os.path.isfile(os.path.join(case_dir, "MANIFEST.json")):
            continue
        cases.append((name, case_dir))
    if not cases:
        return {"verdict": "no-baseline", "exit": EXIT_NOBASELINE,
                "error": "no fixture cases under %s" % root, "cases": [], "passed": 0, "total": 0,
                "meta": {"repo": root}}
    reports = []
    passed = 0
    for name, case_dir in cases:
        inp, err = load_live(case_dir)
        if err:
            reports.append({"case": name, "status": "ERROR", "detail": err})
            continue
        result = analyze(inp, {"citations": False})
        baseline, berr = read_json(os.path.join(case_dir, "expected.json"))
        if berr:
            missing_baseline.append("%s: %s" % (name, berr))
            reports.append({"case": name, "status": "NO-BASELINE", "detail": berr})
            continue
        want = {}
        for k in ("exit", "debt", "contradictions", "unrowed_terminated", "pending_round",
                  "could_not_evaluate", "unknown_lane", "unknown_entry_type",
                  "nonclosure", "nonclosure_unrecognized"):
            if k in baseline:
                want[k] = int(baseline[k])
        counts = _counts(result)
        got_all = {"exit": result["exit"], "debt": counts["debt"],
                   "contradictions": counts["contradictions"],
                   "unrowed_terminated": counts["unrowed_terminated"],
                   "pending_round": counts["pending_round"],
                   "could_not_evaluate": counts["could_not_evaluate"],
                   "unknown_lane": counts["unknown_lane"],
                   "unknown_entry_type": counts["unknown_entry_type"],
                   "nonclosure": counts["nonclosure"],
                   "nonclosure_unrecognized": counts["nonclosure_unrecognized"]}
        got = {k: got_all[k] for k in want}
        ok = want == got
        passed += 1 if ok else 0
        reports.append({"case": name, "status": "pass" if ok else "FAIL",
                        "expected": want, "observed": got, "counts": got_all})
    unit_checks = [
        ("prompt-key-hyphen",
         {"prompt_key": "%s:%s" % _prompt_key_from_rel(".ufo/prompts/kagi-x2-round-1.md")},
         {"prompt_key": "kagi-x2:1"}),
        ("prompt-key-non-round-ignored",
         {"prompt_key": _prompt_key_from_rel(".ufo/prompts/operator-L1.md")},
         {"prompt_key": None}),
    ]
    for name, got, want in unit_checks:
        ok = got == want
        passed += 1 if ok else 0
        reports.append({"case": name, "status": "pass" if ok else "FAIL",
                        "expected": want, "observed": got, "counts": {}})
    total = len(cases) + len(unit_checks)
    verdict = "ok" if (passed == total and not missing_baseline) else "debt"
    exit_code = EXIT_NOBASELINE if missing_baseline else (EXIT_OK if passed == total else EXIT_DEBT)
    if missing_baseline and passed < total:
        verdict = "no-baseline"
    return {"verdict": verdict, "exit": exit_code, "cases": reports, "passed": passed,
            "total": total, "meta": {"repo": root}}


def render_selftest_text(result):
    lines = []
    failed = sum(1 for rep in result["cases"] if rep["status"] not in ("pass",))
    lines.append("closure-check: %s selftest passed=%d/%d failed=%d" % (
        result["verdict"], result["passed"], result["total"], failed))
    for rep in result["cases"]:
        if rep["status"] == "pass":
            o = rep["observed"]
            extra = "".join(" %s=%s" % (k, o[k]) for k in
                            ("could_not_evaluate", "unknown_lane", "unknown_entry_type",
                             "nonclosure", "nonclosure_unrecognized") if k in o)
            lines.append("  %-38s pass  exit=%s debt=%s contradictions=%s unrowed_terminated=%s pending_round=%s%s" % (
                rep["case"], o.get("exit", "-"), o.get("debt", "-"), o.get("contradictions", "-"),
                o.get("unrowed_terminated", "-"), o.get("pending_round", "-"), extra))
        else:
            lines.append("  %-38s %s  expected=%s observed=%s %s" % (
                rep["case"], rep["status"], json.dumps(rep.get("expected"), sort_keys=True),
                json.dumps(rep.get("observed"), sort_keys=True), rep.get("detail", "")))
            if rep.get("counts"):
                lines.append("      all counts: %s" % json.dumps(rep["counts"], sort_keys=True))
    lines.append("selftest: %d/%d passed" % (result["passed"], result["total"]))
    return "\n".join(lines)


def render_frozen_text(result):
    counts = _counts(result)
    lines = [verdict_line(result)]
    base = result.get("baseline", {})
    frozen = result.get("meta", {}).get("frozen")
    lines.append("frozen snapshot: %s  root: %s  mode: %s  entries: %d  log lines: %d" % (
        frozen, result["meta"].get("frozen_dir", "-"), result["meta"]["kind"],
        result["meta"]["entries"], result["meta"]["log_lines"]))
    lines.append("debt set (%d):" % counts["debt"])
    if not result["debt"]:
        lines.append("  none")
    expected = {(r.get("lane"), r.get("lane_round"), r.get("class")): r
                for r in (base.get("expected") or {}).get("debt", [])}
    for f in result["debt"]:
        lines.append("  %-18s %-10s r%-4s %s" % (f["class"], f["lane"], f["lane_round"], f["evidence"]))
        src = expected.get((f["lane"], f["lane_round"], f["class"]), {}).get("source")
        if src:
            lines.append("      pinned from: %s" % src)
    _render_open_findings(lines, result)
    base = result.get("baseline", {})
    lines.append("baseline: %s  expected exit=%s  analyzed exit=%s" % (
        base.get("status"), (base.get("expected") or {}).get("exit"), result["exit"]))
    bi = result.get("baseline_inputs") or {}
    if bi:
        lines.append("snapshot inputs: %s%s" % (
            bi.get("status"), "" if bi.get("status") == "match" else "  %s" % (bi.get("detail") or "")))
    for line in base.get("diffs", []):
        lines.append("  diff: %s" % line)
    return "\n".join(lines)


# ----------------------------------------------------------------------------- main

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Executable closure gate for the shokunin fleet (rounds[] ledger integrity).",
        epilog=HELP_EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", default=None,
                        help="repo root (default: directory containing the script's ancestor holding MANIFEST.json)")
    parser.add_argument("--json", action="store_true", help="emit the result as one JSON object on stdout")
    parser.add_argument("--show-keying", action="store_true",
                        help="print both keying tallies (entry-keyed is authoritative)")
    parser.add_argument("--selftest", action="store_true",
                        help="run against the committed fixture (never the live repo)")
    parser.add_argument("--frozen", metavar="NAME", default=None,
                        help="re-run against a committed frozen baseline NAME (or <wave>/NAME) under any "
                             ".ufo/waves/*/frozen root, and diff its pinned expected.json")
    parser.add_argument("--frozen-root", metavar="DIR", default=None,
                        help="frozen root to read --frozen NAME from (default: search .ufo/waves/*/frozen "
                             "newest-first, fail closed on a duplicate name)")
    parser.add_argument("--pin", metavar="PATH", default=None,
                        help="history pin to verify (default: <repo>/.ufo/history-pin.json)")
    parser.add_argument("--no-ledger", action="store_true", help="suppress the ledger table in text output")
    parser.add_argument("--no-citations", action="store_true", help="skip the git hash-class sweep")
    args = parser.parse_args(argv)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.abspath(args.repo) if args.repo else walk_up_repo(__file__)
    opts = {"citations": not args.no_citations, "no_ledger": args.no_ledger,
            "show_keying": args.show_keying, "pin": args.pin}

    if args.selftest:
        result = do_selftest(script_dir, opts)
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            print(render_selftest_text(result))
        return result["exit"]

    if args.frozen:
        result = do_frozen(repo, args.frozen, opts, root_override=args.frozen_root)
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True, default=str))
        elif result["verdict"] in ("error", "no-baseline") or \
                (result.get("baseline") or {}).get("status") == "snapshot_tampered":
            c = _counts(result) if "debt" in result else {
                "debt": 0, "contradictions": 0, "unrowed_terminated": 0, "pending_round": 0,
                "could_not_evaluate": 0, "nonclosure": 0}
            print("closure-check: %s debt=%d contradictions=%d unrowed_terminated=%d pending_round=%d "
                  "cne=%d nonclosure=%d" % (
                      result["verdict"], c["debt"], c["contradictions"], c["unrowed_terminated"],
                      c["pending_round"], c["could_not_evaluate"], c["nonclosure"]))
            print("error: %s" % (result.get("error")
                                 or (result.get("baseline") or {}).get("status") or "no baseline"))
            for line in (result.get("baseline") or {}).get("diffs", []):
                print("  %s" % line)
        else:
            print(render_frozen_text(result))
            if args.show_keying:
                print(render_text(result, opts))
        return result["exit"]

    if not os.path.isdir(os.path.join(repo, ".ufo")):
        result = _error_result(repo, "no .ufo/ under %s (pass --repo)" % repo)
    else:
        result = do_live(repo, opts)
    if result["verdict"] == "error":
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            print("closure-check: error debt=0 contradictions=0 unrowed_terminated=0 pending_round=0")
            print("error: %s" % result["error"])
        return EXIT_ERROR
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
    else:
        print(render_text(result, opts))
    return result["exit"]


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:          # `| head` and friends
        os._exit(0)