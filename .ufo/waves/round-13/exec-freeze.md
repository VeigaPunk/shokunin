# exec-freeze — the frozen-baseline generator for the closure gate

Artifact under test: `.ufo/waves/round-13/freeze-snapshot.py` (python3 stdlib only, deterministic,
no network, no env vars, read-only over the repo).
Written by the `ExecFreeze` seat of the round-13 `protocol` wave. Write scope: this file and
`freeze-snapshot.py` only — never `PROTOCOL.md`, `MANIFEST.json`, `SCORECARD.md`, `LOG.md`,
`scripts/`, `.ufo/state/`, `.ufo/reports/`, `.ufo/prompts/`, and never `.ufo/waves/round-11/**` or
`.ufo/waves/round-12/**`.

Until now the only definition of a frozen baseline was the prose in
`.ufo/waves/round-12/frozen/README.md` (§"One freezing rule", §"Re-deriving a snapshot"); the three
committed snapshots were assembled by hand from it. This script is that prose expressed once, so a
round-13 baseline is *generated* and re-derived instead of re-implemented. It emits exactly the
seven files `closure-check.py --frozen` consumes, in the layout its `load_frozen()`
(closure-check.py:258-306) reads: `MANIFEST.json`, `watchdog.log`, `reports-index.txt`,
`prompts-index.txt`, `state-counters.txt`, `CLOSED_AT.txt`, `expected.json` — plus
`DERIVED-FROM-LIVE-RUN.txt` when `expected.json` was derived rather than pinned (§4).

---

## 1. CLI contract

```
python3 .ufo/waves/round-13/freeze-snapshot.py --selftest
python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at <ISO8601> --out DIR
        [--repo PATH] [--manifest-source {live,git} | --manifest-file PATH] [--git-ref REF]
        [--expected-exit N --expected-debt JSON] [--checker PATH] [--force]
```

| flag | meaning |
|---|---|
| `--repo PATH` | repo root. Default: walk up from the script to the nearest ancestor holding `MANIFEST.json` + `.ufo/` (the checker's own `walk_up_repo`, closure-check.py:118). |
| `--closed-at ISO8601` | required (unless `--selftest`): the instant `C` every rule below is pinned to. Offset-aware; a timestamp without offset is read in `C`'s zone. |
| `--manifest-source live\|git` | which `rounds[]` blob the snapshot pins. `live` = `<repo>/MANIFEST.json` verbatim (default); `git` = `git show REF:MANIFEST.json` verbatim, requires `--git-ref REF`. The blob is always copied **byte-for-byte** — the snapshot never re-serializes JSON. |
| `--manifest-file PATH` | pin the blob from an arbitrary file (exclusive with `--manifest-source`/`--git-ref`). This is the path for a *target end state* like round-12's `frozen/post`, whose bytes exist nowhere in git history. |
| `--out DIR` | required (unless `--selftest`). Refused when it is inside `.ufo/waves/round-11/` or `.ufo/waves/round-12/` (realpath containment), and refused when non-empty unless `--force`. With `--force` the generator overwrites its own seven files and leaves anything else in the directory alone. |
| `--expected-exit N` + `--expected-debt JSON` | both or neither. When given, `expected.json` is `{"exit": N, "debt": [{"lane","lane_round","class"}, …]}` — the checker's pinned unit (`_canon_debt`, closure-check.py:1369), normalized to those three keys and sorted exactly as `_sorted_debt` sorts (lane roster order, `lane_round`, `class`; closure-check.py:1087). The `JSON` argument may be a list of triples or a checker result object with a `debt` list. |
| `--checker PATH` | checker used by the derived baseline. Default `<repo>/.ufo/waves/round-12/closure-check.py`, falling back to `closure-check.py` beside this script. |
| `--force` | allow a non-empty `--out`. |
| `--selftest` | run over fixture inputs the script creates itself in a temp dir; touches no repo file. |

When `--expected-*` is **omitted**, `expected.json` is derived instead from a checker run over the
snapshot that was just written (see §4), and a loud `DERIVED-FROM-LIVE-RUN` warning is printed plus
recorded in `DERIVED-FROM-LIVE-RUN.txt` inside the snapshot.

Exit codes: `0` ok · `1` selftest failures · `2` usage or refusal (nothing written) · `3` the
checker could not be run / did not answer JSON.

Observed usage refusals (nothing is written before each of these):

```
$ python3 .ufo/waves/round-13/freeze-snapshot.py --out /tmp/x
freeze-snapshot: --closed-at is required
EXIT=2
$ python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at 2026-09-28T21:20:00-03:00 --manifest-source git --out /tmp/x
freeze-snapshot: --manifest-source git requires --git-ref REF
EXIT=2
$ python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at 2026-09-28T21:20:00-03:00 --out /tmp/x --expected-exit 1
freeze-snapshot: --expected-exit and --expected-debt must be given together
EXIT=2
$ python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at 2026-09-28T21:20:00-03:00 --out /tmp/fz-r13/post-actual-gitref
freeze-snapshot: --out /tmp/fz-r13/post-actual-gitref is not empty (pass --force to overwrite)
EXIT=2
```

The write-path refusals, against the real repo (nothing is written, and note that `.ufo/waves/round-13/`
is *not* forbidden — that is where the round-13 snapshots are meant to go):

```
$ python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at 2026-09-28T21:20:00-03:00 --out .ufo/waves/round-12/frozen/pre
freeze-snapshot: refusing to write inside /home/vgpnk/projects/shokunin/.ufo/waves/round-12 (--out .ufo/waves/round-12/frozen/pre)
EXIT=2
$ python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at 2026-09-28T21:20:00-03:00 --out .ufo/waves/round-11/frozen/pre
freeze-snapshot: refusing to write inside /home/vgpnk/projects/shokunin/.ufo/waves/round-11 (--out .ufo/waves/round-11/frozen/pre)
EXIT=2
$ python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at 2026-09-28T21:20:00-03:00 --out .ufo/waves/round-12/frozen/sub/dir
freeze-snapshot: refusing to write inside /home/vgpnk/projects/shokunin/.ufo/waves/round-12 (--out .ufo/waves/round-12/frozen/sub/dir)
EXIT=2
$ python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at 2026-09-28T21:20:00-03:00 --out .ufo/waves/round-12/frozen/../frozen/pre
freeze-snapshot: refusing to write inside /home/vgpnk/projects/shokunin/.ufo/waves/round-12 (--out .ufo/waves/round-12/frozen/../frozen/pre)
EXIT=2
$ ln -sfn /home/vgpnk/projects/shokunin/.ufo/waves/round-12 /tmp/fzlink/r12
$ python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at 2026-09-28T21:20:00-03:00 --out /tmp/fzlink/r12/snap
freeze-snapshot: refusing to write inside /home/vgpnk/projects/shokunin/.ufo/waves/round-12 (--out /tmp/fzlink/r12/snap)
EXIT=2
```

The containment test is realpath-based, so a symlinked or `..`-laden path into those two directories is
refused as well; the selftest pins the same behaviour for a synthetic repo (`refuse-round-11`,
`refuse-round-12`, §3).

---

## 2. The freezing rule as implemented

For instant `C`:

- **`watchdog.log`** — the lines of `<repo>/.ufo/watchdog.log` whose leading token parses as ISO8601
  and is `<= C`, order and bytes preserved, terminated with `\n`. A line whose timestamp is exactly
  `C` is kept; one second after `C` is dropped (§3, `log-boundary`). A line with an unparsable
  leading token is dropped (the checker's `_parse_log` ignores it too) and counted in the run
  report's `dropped` number.
- **`reports-index.txt`** — `.ufo/reports/round-*/*.md` **present at `C`**, one line per file:
  `rel<TAB>bytes<TAB>tracked<TAB>has_hash<TAB>has_shonen<TAB>landed_at`, rel-sorted.
  `landed_at` is the add-commit committer time (`git log -1 --diff-filter=A --format=%cI -- <rel>`),
  or `-`. `has_hash`/`has_shonen` are the checker's own `_grade_file` predicates over the file's
  content (`RE_HASH_RUN` / `RE_SHONEN`, closure-check.py:73-74, 316-317), and `bytes` is the on-disk
  size, because `load_frozen` reconstructs rows from those columns alone (closure-check.py:283-291).
- **`prompts-index.txt`** — the same presence rule for `.ufo/prompts/<lane>-round-N.md` with
  `lane ∈ LANES`; one rel per line (the frozen loader regexes the rel back out, closure-check.py:299).
- **`state-counters.txt`** — highest `launch`/`steer` round per lane among the **kept** log lines,
  lanes sorted by id (the counter files under `.ufo/state/` are driver-written and can be mid-write;
  the kept log is the durable source).
- **`CLOSED_AT.txt`** — `closed_at`, `manifest_source`, `main_HEAD`, the four counts, and the rule
  lines. The three hand-written rule lines are reproduced verbatim; two lines are new
  (`manifest_source` as the round-13 contract requires, and the `main_HEAD` definition).
- **`MANIFEST.json`** — the chosen blob, verbatim.

### "Present at C" — the one reading the committed snapshots actually pin

A file is present at `C` when its add-commit committer time is `<= C` (`tracked=1`, `landed_at` = that
time), **or** — for a file not committed at `C` — its mtime is `<= C` (`tracked=0`, `landed_at = -`).
Read the README's second branch literally and evaluate it against *today's* git state and the branch
inverts: a file that was on disk at `C` but committed later is tracked *now*, so "tracked" would send
it to the add-commit test, which excludes it. The committed snapshots prove the present-at-`C`
reading, including the case that separates the two:

```
$ grep -c -F .ufo/prompts/kasegi-round-15.md .ufo/waves/round-12/frozen/pre/prompts-index.txt
1
$ git log -1 --diff-filter=A --format=%cI -- .ufo/prompts/kasegi-round-15.md
2026-09-28T21:11:33-03:00
$ date -d @$(stat -c %Y .ufo/prompts/kasegi-round-15.md) -Iseconds
2026-09-28T20:50:53-03:00

$ grep -c -F .ufo/prompts/kotoba-round-13.md .ufo/waves/round-12/frozen/pre/prompts-index.txt
1
$ git log -1 --diff-filter=A --format=%cI -- .ufo/prompts/kotoba-round-13.md
2026-09-28T21:11:33-03:00
$ date -d @$(stat -c %Y .ufo/prompts/kotoba-round-13.md) -Iseconds
2026-09-28T20:28:22-03:00

$ grep -c -F .ufo/prompts/aggregator-round-9.md .ufo/waves/round-12/frozen/post-actual/prompts-index.txt
1
$ git log -1 --diff-filter=A --format=%cI -- .ufo/prompts/aggregator-round-9.md
2026-09-28T21:35:25-03:00
$ date -d @$(stat -c %Y .ufo/prompts/aggregator-round-9.md) -Iseconds
2026-09-28T21:14:05-03:00
```

Both files carry `add-commit 21:11:33 > 20:55:00` (committed by the 21:11 closure pass) yet are in
`frozen/pre/prompts-index.txt`: the snapshot's row came from the mtime branch, and the generator's
recomputation puts them back there for the same reason. Had the literal branch structure been the
rule, `pre` would have 70 prompt rows instead of the committed 74 (and `post-actual` 74 instead of
77); the generator reproduces 74/77/79 exactly as §3 and §6 show. The same refinement decides five
prompt rows of the round-13 `pre` rehearsal (§6) — the prompts the 21:35 commit landed but which were
already on disk at 21:30.

---

## 3. `--selftest`

```
$ python3 .ufo/waves/round-13/freeze-snapshot.py --selftest
file-set                           pass
log-boundary                       pass
reports-index                      pass
reports-exclude-post-C             pass
reports-exclude-post-C-untracked   pass
prompts-index                      pass
counters                           pass
closed-at-line                     pass
closed-at-log-lines                pass
closed-at-entries                  pass
closed-at-reports                  pass
closed-at-prompts                  pass
closed-at-source                   pass
expected-json                      pass
manifest-verbatim                  pass
refuse-round-11                    pass
refuse-round-12                    pass
refuse-nonempty                    pass
force-overwrite                    pass
round-trip-report-row              pass
selftest: 20/20 checks passed
EXIT=0
```

The fixture is a git repo the selftest builds in `/tmp/freeze-selftest-*` (never in this repo; the
selftest refuses to run at all if the temp dir resolves inside it) with `C = 2025-12-31T23:00:00+00:00`:

| fixture input | what it pins |
|---|---|
| `.ufo/reports/round-1/kagi.md` — committed with committer date `2025-12-31T21:00:00Z` | landed: `tracked=1`, `landed_at=2025-12-31T21:00:00+00:00` |
| `.ufo/reports/round-2/kagi.md` — committed with the real clock | **excluded** (add-commit > C) |
| `.ufo/reports/round-3/kagi.md` — untracked, mtime `2025-12-31T22:00:00Z` | present, unlanded: `tracked=0`, `landed_at=-` |
| `.ufo/reports/round-4/kagi.md` — untracked, mtime = now | **excluded** (mtime > C) |
| `.ufo/prompts/kagi-round-1.md` (committed, ≤ C) / `kagi-round-5.md` (mtime = now) | prompt include / exclude |
| log lines at `22:59:59`, **`23:00:00`**, `23:00:01` | the `<= C` boundary: exactly-at-C kept, +1 s dropped |
| `launch kagi round=1` at `22:59:59`, `steer kagi -> round 2` at `23:00:00` | `state-counters.txt == "kagi\t2\n"` (highest round among the *kept* lines; the dropped `launch kagi round=3` must not win) |

Every expected value is a literal inside the script (`FX_CLOSED`, `FX_LANDED_AT`, `FX_REPORT_1/3`
with their byte counts, the exact index/log/counter/CLOSED_AT/expected strings) — no assertion is
computed by the code path it tests. The exclusion checks additionally assert the *absence* of the
round-2/round-4 rels, and `round-trip-report-row` re-derives the report rows from the fixture to
prove the two "present at C" branches both fire.

---

## 4. Deriving `expected.json` when `--expected-*` is omitted

`closure-check.py`'s live loader cannot read a flat snapshot — it wants `<repo>/.ufo/watchdog.log`
and grades worktree files (closure-check.py:216-254). Observed, verbatim:

```
$ python3 .ufo/waves/round-12/closure-check.py --repo .ufo/waves/round-12/frozen/post-actual --no-citations --json
{
  "error": "no .ufo/ under /home/vgpnk/projects/shokunin/.ufo/waves/round-12/frozen/post-actual (pass --repo)",
  "exit": 2,
  "meta": {
    "repo": "/home/vgpnk/projects/shokunin/.ufo/waves/round-12/frozen/post-actual"
  },
  "verdict": "error"
}
EXIT=2
```

So the literal `--repo <snapshot>` form of the brief is unsatisfiable and the generator runs the
checker over a **materialized mirror** of the snapshot it just wrote, in the temp dir
(`$TMPDIR/freeze-stage-<out-basename>`, removed again in a `finally`), with
`--no-citations --json`:

- `MANIFEST.json` and `watchdog.log` are copied; `state/<lane>.round` comes from `state-counters.txt`;
  `prompts/` from `prompts-index.txt`.
- Each indexed report is re-materialized at its **pinned byte size** with content containing a hash
  run and/or a `## SHONEN` heading exactly when `has_hash`/`has_shonen` say so (nothing else about
  report content is graded, closure-check.py:312-320).
- `landed_at != '-'` rows are staged in the mirror's git index (`git init` + `git add`) and
  `landed_at == '-'` rows are left untracked, because the live loader's landed predicate *is*
  git-trackedness (closure-check.py:743).
- Report mtimes are pinned far-future, so the live loader's one mtime test (`report_seen_by`,
  closure-check.py:189-197) can never fire — the frozen loader answers `False` there unconditionally
  ("snapshots carry no mtimes").

`expected.json` then carries that run's own debt set and exit; the exact command, the mirror rules,
the raw derived debt and the trust warning are written to `DERIVED-FROM-LIVE-RUN.txt`. Observed:

```
$ python3 .ufo/waves/round-13/freeze-snapshot.py --closed-at 2026-09-28T21:20:00-03:00 \
      --manifest-source git --git-ref df1b2c6 --out /tmp/fz-r13/post-actual-derived
freeze-snapshot: DERIVED-FROM-LIVE-RUN -- expected.json came from a checker run over a
freeze-snapshot: materialized mirror of this snapshot (/scratch/tmp/vgpnk/tmp/freeze-stage-post-actual-derived), not from a reviewed
freeze-snapshot: baseline. The baseline is only as good as that run.
freeze-snapshot: /tmp/fz-r13/post-actual-derived
  closed_at	2026-09-28T21:20:00-03:00
  manifest_source	git-ref df1b2c6
  main_HEAD	e0170cd
  log_lines	215 kept, 29 dropped (> closed_at or unparsable)
  reports	85	prompts	77
  expected	derived from a live run	debt rows	4	exit	1
EXIT=0
$ cat /tmp/fz-r13/post-actual-derived/DERIVED-FROM-LIVE-RUN.txt
DERIVED-FROM-LIVE-RUN
closed_at	2026-09-28T21:20:00-03:00
staging	/scratch/tmp/vgpnk/tmp/freeze-stage-post-actual-derived (removed after the run)
command	/usr/bin/python3 /home/vgpnk/projects/shokunin/.ufo/waves/round-12/closure-check.py --repo /scratch/tmp/vgpnk/tmp/freeze-stage-post-actual-derived --no-citations --json
checker_exit	1
mirror_rule	reports re-materialized at the pinned bytes/has_hash/has_shonen; mtimes far-future
mirror_rule	landed_at != '-' staged in the mirror's git index; landed_at == '-' left untracked
mirror_rule	state/*.round and prompts/ mirrored from the two indexes
derived_debt	[{"lane": "aggregator", "lane_round": 8, "class": "stale_in_flight"}, {"lane": "kengaku", "lane_round": 11, "class": "stale_in_flight"}, {"lane": "kumitate", "lane_round": 12, "class": "stale_in_flight"}, {"lane": "kotoba", "lane_round": 13, "class": "stale_in_flight"}]
warning	expected.json pins the debt set of THIS run; the baseline is only as good
warning	as that run - re-check it, then pin --expected-exit/--expected-debt explicitly
```

The derived baseline is not an approximation of the hand-pinned one on the evidence available: its
triples and exit equal `frozen/post-actual/expected.json`'s, and re-reading the derived snapshot
through `--frozen` says `baseline: match` (§5). Raw debt rows, evidence paths, contradictions and
unlanded lists are all present in the checker's JSON; the generator keeps only the pinned unit.

---

## 5. Regeneration proofs against the committed round-12 snapshots

Three regenerations, all into `/tmp` (never into `.ufo/waves/round-12/`):

```
A  --closed-at 2026-09-28T21:20:00-03:00 --manifest-source git --git-ref df1b2c6 \
   --out /tmp/fz-r13/post-actual-gitref --expected-exit 1 --expected-debt "$(cat /tmp/debt-post.json)"
B  --closed-at 2026-09-28T21:20:00-03:00 \
   --manifest-file .ufo/waves/round-12/frozen/post-actual/MANIFEST.json \
   --out /tmp/fz-r13/post-actual-manifestfile --expected-exit 1 --expected-debt "$(cat /tmp/debt-post.json)"
C  --closed-at 2026-09-28T20:55:00-03:00 --manifest-source git --git-ref 3ea42cb \
   --out /tmp/fz-r13/pre-gitref --expected-exit 1 --expected-debt "$(cat /tmp/debt-pre.json)"
```

`/tmp/debt-post.json` is the four `(lane, lane_round, class)` triples of
`frozen/post-actual/expected.json`; `/tmp/debt-pre.json` the five of `frozen/pre/expected.json`.

Run A and run C (stdout, verbatim):

```
### A: post-actual, --git-ref df1b2c6
freeze-snapshot: /tmp/fz-r13/post-actual-gitref
  closed_at	2026-09-28T21:20:00-03:00
  manifest_source	git-ref df1b2c6
  main_HEAD	e0170cd
  log_lines	215 kept, 24 dropped (> closed_at or unparsable)
  reports	85	prompts	77
  expected	pinned	debt rows	4	exit	1
EXIT=0
### C: pre, --git-ref 3ea42cb
freeze-snapshot: /tmp/fz-r13/pre-gitref
  closed_at	2026-09-28T20:55:00-03:00
  manifest_source	git-ref 3ea42cb
  main_HEAD	50b2179
  log_lines	206 kept, 33 dropped (> closed_at or unparsable)
  reports	80	prompts	74
  expected	pinned	debt rows	5	exit	1
EXIT=0
```

Counts equal the committed `CLOSED_AT.txt` fields in every column (`215/30/85/77` and `206/22/80/74`).
Byte-level comparison of all seven files (`cmp -s`, sha256 prefixes and sizes):

| file | A (post-actual, git-ref) | B (post-actual, manifest-file) | C (pre, git-ref) |
|---|---|---|---|
| `MANIFEST.json` | differs, 40187→37932 B (`b95f9f7f` → `507bffc2`) | **IDENTICAL** | **IDENTICAL** |
| `watchdog.log` | **IDENTICAL** | **IDENTICAL** | **IDENTICAL** |
| `reports-index.txt` | differs, 5833→5833 B (`03dabe50` → `92cf84bb`) | differs, same | differs, 5503→5503 B (`d0219004` → `bb76f27f`) |
| `prompts-index.txt` | **IDENTICAL** | **IDENTICAL** | **IDENTICAL** |
| `state-counters.txt` | **IDENTICAL** | **IDENTICAL** | **IDENTICAL** |
| `CLOSED_AT.txt` | differs, 374→499 B (`be8d79d2` → `843f76f6`) | differs, 374→580 B | differs, 374→499 B (`ffbb893a` → `44f894c4`) |
| `expected.json` | differs, 1684→359 B (`fbf88062` → `ce4b19cf`) | differs, same | differs, 2459→447 B (`a905c439` → `f2798008`) |

`diff -r` output for the two regeneration runs, restricted to the differing hunks:

```
$ diff -r .ufo/waves/round-12/frozen/post-actual /tmp/fz-r13/post-actual-gitref
diff -r .ufo/waves/round-12/frozen/post-actual/CLOSED_AT.txt /tmp/fz-r13/post-actual-gitref/CLOSED_AT.txt
1a2
> manifest_source	git-ref df1b2c6
9a11
> rule	main_HEAD = newest commit with committer time <= closed_at ('-' when git cannot answer)
diff -r .ufo/waves/round-12/frozen/post-actual/MANIFEST.json /tmp/fz-r13/post-actual-gitref/MANIFEST.json
2,733c2,46
<  "version": 1,
<  "repo": "shokunin",
   … 731 lines of the whole-file re-serialization …
>   "version": 1,
>   "repo": "shokunin",
diff -r .ufo/waves/round-12/frozen/post-actual/expected.json /tmp/fz-r13/post-actual-gitref/expected.json
3d2
<  "verdict": "debt",
8,10c7
<    "class": "stale_in_flight",
<    "source": "entry #23 in-flight; complete aggregator round=8 21:14:05 (<= 21:20) + landed report .ufo/reports/round-8/aggregator.md (add a5d6a7e, 24058 B, added 21:13:01)",
<    "evidence": "mission terminated inside the snapshot instant"
---
>    "class": "stale_in_flight"
   … the same shape for the other three rows …
33,36c24,25
<  ],
<  "pin": "(lane, lane_round, class) triples; the four rows the pass's own 21:20:00 evidence instants",
<  "note": "post-actual = the pass's actual bytes (30 entries). Every row rests on evidence inside the snapshot instant, so this is real debt, not post-window leakage. frozen/post pins the TARGET end state (the same MANIFEST plus these four corrections), which is why it is green."
< }
\ No newline at end of file
---
>  ]
> }
diff -r .ufo/waves/round-12/frozen/post-actual/reports-index.txt /tmp/fz-r13/post-actual-gitref/reports-index.txt
73c73
< .ufo/reports/round-8/kake.md	2424	1	0	0	2026-09-28T17:38:25-03:00
---
> .ufo/reports/round-8/kake.md	2424	1	1	0	2026-09-28T17:38:25-03:00
```

```
$ diff -r .ufo/waves/round-12/frozen/pre /tmp/fz-r13/pre-gitref
diff -r .ufo/waves/round-12/frozen/pre/CLOSED_AT.txt /tmp/fz-r13/pre-gitref/CLOSED_AT.txt
2c2,3
< main_HEAD	e0170cd
---
> manifest_source	git-ref 3ea42cb
> main_HEAD	50b2179
9a11
> rule	main_HEAD = newest commit with committer time <= closed_at ('-' when git cannot answer)
diff -r .ufo/waves/round-12/frozen/pre/expected.json /tmp/fz-r13/pre-gitref/expected.json
3,9d2
<  "verdict": "debt",
<  "pin": "the debt set as (lane, lane_round, class) triples; evidence strings are prose and are not compared",
<  "sources": {
<   "scout-closure.md": "\u00a7Required appends (measured 20:45-20:47; wc -l log 201) - 5 closure-corrections",
<   "reviewer.md": "\u00a7Status recommendations (measured 20:40) - ok / in-flight-re-confirm calls",
<   "derivation": "rows 1,3,4 below are demanded by both independent artifacts; row 2 (kumitate r11) is demanded by them too, but as `ok` on a landed report / `in-flight` re-confirm - this checker classes it stale_in_flight because the complete line 20:50:56 exists in the snapshot log; row 5 (kasegi r14) postdates both sibling clocks (complete 20:50:53) and is added by the checker alone"
<  },
   … per-row "source"/"evidence" prose dropped, and the debt rows re-sorted into lane-roster order …
diff -r .ufo/waves/round-12/frozen/pre/reports-index.txt /tmp/fz-r13/pre-gitref/reports-index.txt
68c68
< .ufo/reports/round-8/kake.md	2424	1	0	0	2026-09-28T17:38:25-03:00
---
> .ufo/reports/round-8/kake.md	2424	1	1	0	2026-09-28T17:38:25-03:00
```

Nothing else differs: `watchdog.log`, `prompts-index.txt`, `state-counters.txt` are byte-identical in
both runs, `MANIFEST.json` is byte-identical in run B (and in run C), and run B's only extra
difference against run A is the `manifest_source` value in `CLOSED_AT.txt`.

Determinism: re-running A and C with the final script into fresh directories reproduces all seven
files byte-for-byte (`sha256sum` of each file equal to the earlier run's, in both instants) — the
snapshot depends only on `(C, blob, repo git state)`, and the run's `dropped` counter is the only
field that moves with wall-clock time. Every difference and its verdict:

### Finding 1 — `reports-index.txt`: the hand snapshot is **wrong** on one column
`frozen/{pre,post-actual}/reports-index.txt` say `has_hash=0` for `.ufo/reports/round-8/kake.md`; the
generator says `1`. The generator is right: the file contains the 7-character hex run `9544914`, which
`RE_HASH_RUN` — the checker's own `_grade_file` predicate — matches, and the file has exactly one
commit, so there is no amended/later content to explain the hand value:

```
$ git log --format='%h %cI %s' -- .ufo/reports/round-8/kake.md
609ecb6 2026-09-28T17:38:25-03:00 fleet-2: AXES.md framework, MISSION.md SSOT, watchdog v4, protocol conventions
$ git show 609ecb6:.ufo/reports/round-8/kake.md | grep -oE '[0-9a-f]{7,}' | head -3
9544914
$ git show 609ecb6:.ufo/reports/round-8/kake.md | wc -c
2424
```
Both sides agree on the other five columns (`2424`, `1`, `-`, `2026-09-28T17:38:25-03:00`), i.e. it is
the same blob. The column is **inert for the verdict**: `load_frozen` computes
`marker = bytes < 400 and not has_hash and not has_shonen` (closure-check.py:289) and this report is
2424 B, so `marker` is `False` either way — and both readings read back green:

```
$ python3 .ufo/waves/round-12/closure-check.py --frozen post-actual --no-citations | tail -1
baseline: match  expected exit=1  analyzed exit=1
$ python3 .ufo/waves/round-12/closure-check.py --repo /tmp/fz-r13/root --frozen post-actual --no-citations | tail -1
baseline: match  expected exit=1  analyzed exit=1
```
(the second points `--repo` at a throwaway root shaped `<root>/.ufo/waves/round-12/frozen/post-actual`,
which is how `do_frozen` resolves a snapshot without writing inside the real `round-12/`, closure-check.py:1330.)

### Finding 2 — `CLOSED_AT.txt`: two added lines, and for `pre` the hand `main_HEAD` is **wrong**
Lines added by the generator (both absent from the hand files, present in the round-13 contract):
`manifest_source` and the `main_HEAD` definition line. The generator's `main_HEAD` is the newest commit
with committer time `<= C` on `HEAD`:

```
$ git rev-list -1 --before=2026-09-28T21:20:00-03:00 HEAD | cat   # -> e0170cd33850016beb53cbe9066fefcd3ef17712
e0170cd33850016beb53cbe9066fefcd3ef17712
$ git rev-list -1 --before=2026-09-28T20:55:00-03:00 HEAD | cat   # -> 50b2179ee2501c38d9b6f38898950a2950551118
50b2179ee2501c38d9b6f38898950a2950551118
$ git log --format='%h %cI %s' -1 e0170cd | cat
e0170cd 2026-09-28T21:18:11-03:00 kengaku round-11 report
```

For `post-actual` the commitment coincides with the hand value (both `e0170cd`). For `pre` the hand
file says `main_HEAD e0170cd`, a commit whose committer time is **21:18:11 — 23 minutes after that
snapshot's `closed_at` of 20:55:00**: it is the assembler's HEAD, not the snapshot's. A frozen
baseline exists to bound what existed at its instant, so citing it is wrong (or, at best, the field is
undefined); the reconstructable value at 20:55:00 is `50b2179` (kasegi round-14 report, 20:48:46).
Verdict: **hand file wrong for `pre`, and incomplete for both** (no `manifest_source`).

### Finding 3 — `MANIFEST.json` (run A): cosmetic re-serialization, neither side wrong
The hand `post-actual/MANIFEST.json` is not the source blob — it is a re-serialization with
`json.dump(…, indent=1)`, which is byte-verified here, and it is exactly the JSON the blob parses to:

```
$ diff <(git show df1b2c6:MANIFEST.json | python3 -c "import json,sys;print(json.dumps(json.load(sys.stdin),indent=1),end='')") .ufo/waves/round-12/frozen/post-actual/MANIFEST.json && echo IDENTICAL
IDENTICAL
$ diff <(git show df1b2c6:MANIFEST.json) /tmp/fz-r13/post-actual-gitref/MANIFEST.json && echo IDENTICAL
IDENTICAL
$ python3 -c "import json; h=json.load(open('.ufo/waves/round-12/frozen/post-actual/MANIFEST.json')); m=json.load(open('/tmp/fz-r13/post-actual-gitref/MANIFEST.json')); print('parsed equal:', h==m, '| rounds:', len(h['rounds']))"
parsed equal: True | rounds: 30
```
The generator pins the blob verbatim (`--manifest-source git`/`live`), which is the stronger provenance
claim; run B shows it can also reproduce the hand bytes exactly when the hand file *is* the source
(`MANIFEST.json IDENTICAL`). `frozen/pre/MANIFEST.json` and `frozen/post/MANIFEST.json` follow the same
convention (`pre` is verbatim `git show 3ea42cb`, and `cmp` says so; `post` is `pre` + the appended
corrections re-dumped with `indent=1`, so it is a hand-built blob that no `--git-ref` can supply —
`--manifest-file` is the supported path for it).

### Finding 4 — `expected.json`: pin shape only, neither side wrong
The hand baselines carry prose the checker never reads: `verdict`, `pin`, `note`, `sources`, and a
`source`/`evidence` pair on every row. `_canon_debt` projects each row to `(lane, lane_round, class)`
and `_compare_baseline` compares only those triples plus `exit` (closure-check.py:1355-1374). The
generator emits exactly that unit, in `_sorted_debt` order. Equality of the pinned content:

```
$ python3 -c "
import json
for name, hand in (('post-actual-gitref','post-actual'), ('pre-gitref','pre')):
    a = json.load(open('/tmp/fz-r13/%s/expected.json' % name))['debt']
    b = json.load(open('.ufo/waves/round-12/frozen/%s/expected.json' % hand))['debt']
    ta = {(r['lane'], r['lane_round'], r['class']) for r in a}
    tb = {(r['lane'], r['lane_round'], r['class']) for r in b}
    print(name, 'triple-sets equal:', ta == tb, '| generated order:', [(r['lane'], r['lane_round']) for r in a])"
post-actual-gitref triple-sets equal: True | generated order: [('aggregator', 8), ('kengaku', 11), ('kumitate', 12), ('kotoba', 13)]
pre-gitref triple-sets equal: True | generated order: [('protocol', 11), ('aggregator', 7), ('kasegi', 14), ('kumitate', 11), ('kotoba', 12)]
```
(the `pre` hand file happens to list `aggregator r7`/`kasegi r14` last; `_canon_debt` sorts both sides,
so the order is not part of the match — the generator nevertheless emits the sorted order.)

### Consumability proof
Both regenerated snapshots were read back through the checker's own frozen path, `baseline: match` in
each case (run A's expected.json was pinned from the hand file's triples; the third line is run B):

```
$ mkdir -p /tmp/fz-r13/root/.ufo/waves/round-12/frozen
$ cp -r /tmp/fz-r13/pre-gitref /tmp/fz-r13/root/.ufo/waves/round-12/frozen/pre
$ cp -r /tmp/fz-r13/post-actual-gitref /tmp/fz-r13/root/.ufo/waves/round-12/frozen/post-actual
$ python3 .ufo/waves/round-12/closure-check.py --repo /tmp/fz-r13/root --frozen pre --no-citations | tail -1
baseline: match  expected exit=1  analyzed exit=1
$ python3 .ufo/waves/round-12/closure-check.py --repo /tmp/fz-r13/root --frozen pre --no-citations >/dev/null; echo "EXIT=$?"
EXIT=1
$ python3 .ufo/waves/round-12/closure-check.py --repo /tmp/fz-r13/root --frozen post-actual --no-citations >/dev/null; echo "EXIT=$?"
EXIT=1
```
with the debt sets the committed baselines claim: 4 `stale_in_flight` rows (aggregator r8, kengaku r11,
kumitate r12, kotoba r13) for `post-actual`, and 5 rows for `pre` (protocol r11, kumitate r11,
kotoba r12 `stale_in_flight`; aggregator r7, kasegi r14 `unrowed_terminated`).

---

## 6. Round-13 baselines: the commands the integrator runs

Prerequisites: `python3` (3.8+, stdlib only) and `git` on PATH. Both commands are read-only over the
repo; they write only under `--out`, and both refuse `--out` inside `.ufo/waves/round-11|12/`.

**`pre`** — the round-12 end state at `closed_at 2026-09-28T21:30:00-03:00` with the 36-entry blob
(`git show cab25dd:MANIFEST.json`; `cab25dd` is the commit that carried it, committer time 21:35:25):

```sh
cd /home/vgpnk/projects/shokunin
python3 .ufo/waves/round-13/freeze-snapshot.py \
  --closed-at 2026-09-28T21:30:00-03:00 \
  --manifest-source git --git-ref cab25dd \
  --out .ufo/waves/round-13/frozen/pre
```

Rehearsed exactly as written, but with `--out /tmp/fz-r13/r13-pre` (the rehearsal output is the only
reason the run report below names that path). Every integer below except `dropped` is what the real run
will print, provided the index-relevant state of files present at 21:30 (trackedness, mtimes, contents)
has not changed in the meantime — the generation-time dependence §7 spells out. `dropped` counts the log
lines *after* `C`, and the driver keeps appending to `.ufo/watchdog.log`, so it grows with time while
`kept` and the index counts do not move at all:

```
freeze-snapshot: DERIVED-FROM-LIVE-RUN -- expected.json came from a checker run over a
freeze-snapshot: materialized mirror of this snapshot (/scratch/tmp/vgpnk/tmp/freeze-stage-r13-pre), not from a reviewed
freeze-snapshot: baseline. The baseline is only as good as that run.
freeze-snapshot: /tmp/fz-r13/r13-pre
  closed_at	2026-09-28T21:30:00-03:00
  manifest_source	git-ref cab25dd
  main_HEAD	e0170cd
  log_lines	221 kept, 23 dropped (> closed_at or unparsable)
  reports	85	prompts	79
  expected	derived from a live run	debt rows	0	exit	0
EXIT=0
$ cat /tmp/fz-r13/r13-pre/CLOSED_AT.txt
closed_at	2026-09-28T21:30:00-03:00
manifest_source	git-ref cab25dd
main_HEAD	e0170cd
log_lines	221
manifest_entries	36
reports	85
prompts	79
rule	watchdog.log = lines with timestamp <= closed_at; reports-index/prompts-index = files with
rule	mtime <= closed_at (landed_at = add-commit committer time, '-' when untracked);
rule	state-counters = highest launch/steer round per lane among the kept log lines
rule	main_HEAD = newest commit with committer time <= closed_at ('-' when git cannot answer)
$ cat /tmp/fz-r13/r13-pre/expected.json
{
 "exit": 0,
 "debt": []
}
```
`exit 0 / debt 0` agrees with `cab25dd`'s own message ("rounds 22->36; live gate exit 0 debt=0") and
with the round-12 README's claim that the 21:30 pass closed the four rows. The `prompts` count is 79
rather than `post-actual`'s 77 because of the present-at-`C` rule (§2): the five prompts the 21:35
commit landed (`aggregator-round-9`, `kagi-round-13`, `kengaku-round-12`, `kotoba-round-14`,
`kumitate-round-13`) were on disk at 21:30 and enter the index with `tracked=0`. Reading the rehearsal
back through the frozen path with its derived baseline:

```
$ cp -r /tmp/fz-r13/r13-pre /tmp/fz-r13/root2/.ufo/waves/round-12/frozen/r13pre
$ python3 .ufo/waves/round-12/closure-check.py --repo /tmp/fz-r13/root2 --frozen r13pre --no-citations | tail -3
debt set (0):
  none
baseline: match  expected exit=0  analyzed exit=0
EXIT=0
```

**`post`** — the same instant with the round-13 entries appended (the target end state; the integrator
supplies the blob, so pin it by file):

```sh
cd /home/vgpnk/projects/shokunin
python3 .ufo/waves/round-13/freeze-snapshot.py \
  --closed-at 2026-09-28T21:30:00-03:00 \
  --manifest-file .ufo/waves/round-13/frozen/post.MANIFEST.json \
  --out .ufo/waves/round-13/frozen/post
```

(The blob is a **sibling** of the snapshot directory: a blob placed inside `--out` would make that
directory non-empty and trip the `--force` refusal.)

`--manifest-file` is proven sufficient for a blob that exists in no commit: it wrote run B's
`MANIFEST.json` byte-identically to the committed hand-assembled file
(`MANIFEST.json IDENTICAL`, sha256 `b95f9f7f04ee578f` on both sides, 40187 B), i.e. a `post` blob
built by appending `grand_entries` to the `pre` blob (the round-12 recipe:
`json.dump(pre + appended, indent=1)`) is pinned verbatim. After the run, `expected.json` is the
derived end-state baseline and `DERIVED-FROM-LIVE-RUN.txt` records how it was produced; if the pass
wants a *reviewed* pin instead, re-run with the observed values explicitly:
`--expected-exit <N> --expected-debt '<the DERIVED-FROM-LIVE-RUN debt JSON>'`.

Verification after both runs (the committed round-12 checker resolves `--frozen` under
`<repo>/.ufo/waves/round-12/frozen/<name>`, so a round-13 snapshot is read through a throwaway root;
if the round-13 checker moves `do_frozen` to `round-13/frozen`, the same command works directly):

```sh
mkdir -p /tmp/r13read/.ufo/waves/round-12/frozen
cp -r .ufo/waves/round-13/frozen/pre  /tmp/r13read/.ufo/waves/round-12/frozen/pre
cp -r .ufo/waves/round-13/frozen/post /tmp/r13read/.ufo/waves/round-12/frozen/post
python3 .ufo/waves/round-12/closure-check.py --repo /tmp/r13read --frozen pre  --no-citations
python3 .ufo/waves/round-12/closure-check.py --repo /tmp/r13read --frozen post --no-citations
```
Re-deriving a snapshot later repeats the generation and diffs: the generated index is a function of the
repo's git state at generation time, so `diff -r` against the committed baseline is the regression test
for both the generator and the snapshot (§7).

---

## 7. Residual trust assumptions

- **Who may write a snapshot.** The generator is the only writer it defends against; anyone with write
  access to `.ufo/waves/round-13/frozen/` can still hand-edit a snapshot afterwards. The guards are
  mechanical and local (refuse `round-11`/`round-12` containment, refuse a non-empty `--out` without
  `--force`, write only the seven files) — they are not a signature. The only detector of a later
  hand-edit is regenerating at the same `(C, blob)` and `diff -r`-ing; on the round-12 instants that
  diff is exactly the four findings above and nothing else.
- **What pins `expected.json`.** In explicit mode, a human-pinned value (the reviewed baseline). In
  derived mode, one checker run over a materialized mirror, with the exact command, mirror rules and
  raw debt recorded in `DERIVED-FROM-LIVE-RUN.txt`; the file says in its own text that the baseline is
  only as good as that run. Either way the checker compares `(lane, lane_round, class)` triples and the
  exit code only — prose, ordering and any extra keys are not pinned, so a baseline can be green while
  its evidence prose rots.
- **The mirror is not evidence.** Deriving inverts the checker's own limitation: it fabricates report
  *content* at the pinned size/flags because the live loader grades worktree files. The fabricated bytes
  exist only in the temp staging tree (removed in a `finally`), never in a snapshot; the snapshot's
  reports are the index rows, and the round-12 baselines' prose continues to be the only record of what
  the reports actually said.
- **Index columns are a function of generation time, not of history.** `landed_at` is history-faithful
  (add-commit committer time), but `bytes`, `has_hash` and `has_shonen` are read from the file *as it is
  on disk now*, and presence for a never-committed file rests on a mutable mtime. So: a report amended
  after `C` shifts its `bytes`/`has_hash` columns (round-8/kake.md is the one file in these snapshots
  where the generator and the hand assembler disagree, and the generator is the one that matches the
  blob); a file that was present at `C` but is deleted later disappears from a re-derivation (the
  generator cannot recover it — for the two round-12 instants every indexed path still exists, verified
  by the probe that found no hand row without a file); and a file checked out or touched moves its
  mtime. `tracked`/`landed_at` survive all of that.
- **`main_HEAD` is provenance, not evidence.** It is the newest commit with committer time `<= C` on the
  current `HEAD` — the same formula the hand `post-actual` value happens to satisfy and the `pre` value
  does not. With lanes committing concurrently to this repo, the historical tip at `C` is not fully
  recoverable from committer times alone, and `--before` is a strict comparison.
- **Scope of what the baseline checks.** A frozen snapshot disables the citation/ancestry sweep
  (`citation_scope = "frozen snapshot: citation/ancestry checks disabled"`, closure-check.py:305), and
  the derive run adds `--no-citations` on top; a derived baseline therefore never exercises the hash
  sweep, and `has_hash`/`has_shonen` in the index exist for the marker rule and for prose, not for
  identity verification.
- **Environment.** The generator reads no environment variable for its own behaviour (a minimal
  `PATH`/`HOME`/`LC_ALL` environment is handed to `git` so that an ambient `GIT_DIR`/`GIT_WORK_TREE`
  cannot redirect a read); the selftest is the only place that sets `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE`,
  for its own backdated fixture commit. The temp staging path is `$TMPDIR`-derived and therefore appears
  in `DERIVED-FROM-LIVE-RUN.txt` (`tempfile.gettempdir()` is an environment read); the snapshot's seven
  files and `expected.json` are unaffected by it. If `TMPDIR` resolves inside the repo, the selftest and
  derive mode both refuse to run (staging a mirror there would write into the repo).