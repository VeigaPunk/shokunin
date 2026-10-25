# source-freshness — `overdue` mode probe (labrat, round 12)

Seat: `KaikaAggregateR12.SourceFreshness`. Scope: one bounded probe of the committed
`sources-census.sh` `overdue` mode against the physical lane repos. Read-only against all
repos; the only repo write is this note. All counts below are **probe-window counts, not a
census total**; the parent's indented-row parser fix and `FINAL LANES READY` have not landed.

## Hypothesis (stated before execution)

For the lane repos that currently carry `corpus/SOURCES.md`, the committed `overdue` mode
correctly distinguishes the three numeric/cadence forms in the recheck column:

1. ISO date `YYYY-MM-DD` → due = that calendar date; reported `overdue` iff due <= `--today`,
   days = (today − due); **no** `cadence` line.
2. `NNd` → due = `opened` + N days; a `cadence` line is always emitted, and `overdue` iff
   due <= `--today`, days = (today − due).
3. Symbolic cadence (e.g. `on-release`) → `cadence` line only, never `overdue`.
4. The due-date boundary is inclusive (reported on the due date, silent the day before).

Expected observation at fixed date `2026-10-19` (all `opened` = `2026-10-19` in the present
files): 469 `cadence` lines (every NNd/symbolic row), 0 `overdue` lines, i.e. nothing is due
yet; and exit 2 if any lane lacks `SOURCES.md` (`missing`), exit 0 otherwise.

## Revision binding

Script probed (identical bytes in both checkouts):

```
$ git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate rev-parse HEAD
ee8ba85736ee7bdeda46ba8e0e1267a8366ee7f2        # branch kaika/aggregate
$ sha256sum /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/scripts/sources-census.sh
aed9ed65e42eaa5d372c380509e05f6fabbb39ec15cc75f06010898474ae8d1b  (28161 bytes)
$ git -C .../fleet-aggregate status --porcelain -- scripts/sources-census.sh | wc -l
0
$ git -C /home/vgpnk/Projects/shokunin rev-parse HEAD
dcf3b6484e02452fc7aec55d724744de188779b9        # master; same script sha256
$ git -C .../fleet-aggregate log -1 --format='%H %ad %s' -- scripts/sources-census.sh
ae7bf19c0fad398407be31add90574eaed1f5a2a Mon Oct 19 19:52:48 2026 -0300 scripts: sources-census.sh — ...
```

Script read first (all 653 lines). Overdue arm is lines 522–533: cadence emitted at 523–524
for `NNd` **or** symbolic; `NNd` due at 526–528 (`opened + N*86400`); symbolic forced
`INVALID_EPOCH` at 529; ISO `due=epoch(recheck)` at 530; report at 531–533 with
`int((today_s-due)/86400)`. Missing lane ⇒ `missing_error=1` (line 560) and exit 2 (line
651), which is tested **before** findings exit 1 (line 652).

## Inputs / environment

- Physical lane dirs: `/home/vgpnk/Projects/shokunin/*-shokunin` = **21** at probe start.
- `SOURCES.md` present at start: **17** (below); absent: `audio-shokunin`,
  `game-dev-2d-shokunin`, `kaidoku-shokunin`, `kumitate-shokunin`.
- Mid-probe drift: `kaidoku-shokunin/corpus/SOURCES.md` (mtime 2026-10-19 20:50:15 -03) and
  `kumitate-shokunin/corpus/SOURCES.md` (20:49:24 -03) appeared; at 23:52Z 19 lanes present,
  `audio` + `game-dev-2d` still absent. Runs R1–R4/R2b below used the pinned 17 only and are
  coherent; R1b/R5 are post-drift/current-state observations.
- Host TZ: `/etc/localtime -> /usr/share/zoneinfo/America/Sao_Paulo`, `date +%Z %z` = `-03
  -0300` (no DST in effect). gawk `mktime` day diffs verified exact (`2026-10-19`→`2027-04-17`
  = 180.000 days). DST-observing hosts were **not** exercised.
- Due-date anchors computed independently with coreutils `date -u -d`, not with the script:
  `2026-10-19 + 90d → 2027-01-17`, `+180d → 2027-04-17`, `+365d → 2027-10-19`,
  `+730d → 2028-10-18`; `2027-04-17 − 2027-01-17 = 90` days.

Pinned 17 files (sha256 at probe time; unchanged from first enumeration through R4/R2b):

```
chousa-shokunin     6428e46aa69d8554c09e06c5384ce2664ae3db79b6c9f3a072c07a11a957bbbf
game-dev-3d-shokunin dc95c043da258003dddc8957f168e3635fbd9fc587bace5232c7bdd3a824936f
kagi-shokunin       db134917dab989f24c3e33b5983fdac7240fd412c9ebdf94a77c76a8fe55b332
kake-shokunin       e1f07eb4929903c422946dca1617939dc1ea2aebdceb807a224e182704b98042
kama-shokunin       9dc40d25a595b3d42b39649e17094cfa4e7190cfbf340331252dd29dea22093a
kasegi-shokunin     0e8378bceb01f1c26045059044e85e9417bc933e15b4c774ec53ee34359dc940
kengaku-shokunin    fb57569835c4f1c6a55decbf4a36b5f6dac8f6c3d3b2a961d3dfba4f48cf5cc5
kotoba-shokunin     ef331658e398dd552f8df992aade49d25025eb7b0309e7f2d3c00a7fd92e16d3
kotodama-shokunin   662f962687717fa9cc66ec365c2c3e85ec79fc5ae5cd9fbc9df33dce3baa8e34
lore-shokunin       9fc435e8095f8f867c18bd3b048c9d1f6c6040c9a60f6de5cb4d9d9e4dae9249
mado-shokunin       9b175fa9925a7b7230ccb02cc121a0c5e932b5af4569f6c8b6df367540e07e23
mori-shokunin       efe349d580266b8499d783d94b707012639d73173b57e09168a5a9df1d823ab6
revenger-shokunin   c1573b2fbc284493096ddb20af506122aea0bcf7bc6b5a037b7dc31988f55f30
souji-shokunin      1b7cc681084e9e5efcb3a89ff0f7943758d3040926c22f4cf5c58046ca548127
tabi-shokunin       000053ccfc4e61f2dae220213ed42f59c25d168d8e0b64a07c28f1770abd5c77
tameshi-shokunin    6b34e8991f56d78d561512d71c7eaeaf4f548f1d7f12eec8eb2b896bf6d72827
tsukuroi-shokunin   3e06c2ebb36f5feaf84978238a9bd36d76a2313c017a0f9916fbc0bf0259b2e2
```

Row-shape facts **within the pinned 17** (probe-internal expectation basis, not a census
total): 488 parser-visible registry rows; `opened` = `2026-10-19` for all; recheck classes:
19 ISO (all `kengaku-shokunin`, all `2027-01-17`), 469 NNd (90/180/365/730d) or symbolic
(`on-release`, `on-commit`, `on-change`, `on-gate-change`, `every round`), 0 other/invalid.

## Row-start gate checks (why no completeness claim)

The parser only reads lines whose first character is `|` (`$0 !~ /^\|/ next`), inside the
exact `## Registry` section, minus header/separator. Measured on the pinned 17:

```
$ for f in /home/vgpnk/Projects/shokunin/*-shokunin/corpus/SOURCES.md; do
    grep -cE '^[[:space:]]+\|' "$f"; done            # indented pipe rows
0   (all 17; no indented `|` row exists in the pinned set)
$ grep -nE '[|][[:space:]]*S[0-9]{3,}[[:space:]]*[|]' "$f" | grep -cvE '^[0-9]+:\|'
0   (no non-pipe-start S-row)
```

Also 0 pipe rows outside `## Registry` (awk total `^|` == in-Registry count for every file).
So for the pinned 17 the gate is currently lossless for row starts — but this says nothing
about the parser fix's new semantics or the final corpus, and no final total is claimed.

## Commands and observed outputs

`S=/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/scripts/sources-census.sh`,
`P=/home/vgpnk/Projects/shokunin`. No `--out` used; stdout/stderr captured to `/tmp` only.

**R1 — primary fixed date, all 21 dirs (start state: 4 lanes missing):**

```
all=(/home/vgpnk/Projects/shokunin/*-shokunin)      # 21
"$S" overdue --today 2026-10-19 "${all[@]}" >/tmp/sf-probe-r1.out 2>/tmp/sf-probe-r1.err
# exit 2; 473 lines; stderr 0 bytes; missing=4 cadence=469 overdue=0
audio-shokunin        missing /home/vgpnk/Projects/shokunin/audio-shokunin/corpus/SOURCES.md
game-dev-2d-shokunin  missing /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin/corpus/SOURCES.md
kaidoku-shokunin      missing /home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/SOURCES.md
kumitate-shokunin     missing /home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/SOURCES.md
```

**R2 — same date, 17 pinned dirs (the 17 paths passed explicitly):**

```
"$S" overdue --today 2026-10-19 <the-17-paths> >/tmp/sf-probe-r2.out 2>/tmp/sf-probe-r2.err
# exit 0; 469 lines; stderr 0; cadence=469; overdue=0
chousa-shokunin  cadence  S001 recheck=on-release opened=2026-10-19
chousa-shokunin  cadence  S002 recheck=365d opened=2026-10-19
...
tsukuroi-shokunin cadence S034 recheck=on-release opened=2026-10-19
```

**R3 — fixed date 2027-01-17 (first due date), 17 pinned dirs:**

```
"$S" overdue --today 2027-01-17 <the-17-paths> >/tmp/sf-probe-r3.out 2>/tmp/sf-probe-r3.err
# exit 1; 585 lines; stderr 0; cadence=469; overdue=116; every overdue token "0d"
kengaku-shokunin  overdue  S025 0d recheck=90d opened=2026-10-19
kengaku-shokunin  overdue  S022 0d recheck=2027-01-17 opened=2026-10-19
```

`kengaku-shokunin S022` (ISO form) appears with **no** `cadence` line; `S025` (90d) has both
`cadence` and `overdue`.

**R4 — fixed date 2027-04-17 (180d due), 17 pinned dirs:**

```
"$S" overdue --today 2027-04-17 <the-17-paths> >/tmp/sf-probe-r4.out 2>/tmp/sf-probe-r4.err
# exit 1; 665 lines; stderr 0; cadence=469; overdue=196
# day-token histogram over overdue lines: 80 x 0d, 116 x 90d
tsukuroi-shokunin overdue S033 90d recheck=90d opened=2026-10-19   # first overdue line
game-dev-3d-shokunin overdue S020 0d recheck=180d opened=2026-10-19 # last overdue line
```

**R2b — boundary, one day before due, 17 pinned dirs:**

```
timeout 20 "$S" overdue --today 2027-01-16 $P/<17 explicit dirs> >/tmp/sf-probe-r2b.out 2>&1
# exit 0; 469 lines; overdue=0; cadence=469
```

**R1b — post-drift check, 21 dirs at 2027-01-17 (kaidoku/kumitate files had appeared):**

```
timeout 20 "$S" overdue --today 2027-01-17 $P/*-shokunin >/tmp/sf-probe-r1b.out 2>&1
# exit 2; 633 lines; missing=2; cadence=511; overdue=120
# kaidoku: cadence=22 overdue=1; kumitate: cadence=20 overdue=3  (= 511 / +4 vs R3)
```

Exit 2 was returned **despite 120 overdue findings**, confirming the missing-lane exit 2
precedence over findings exit 1 (script lines 651–652).

**R5 — current state, 21 dirs, primary date (hash-stable during run):**

```
timeout 20 "$S" overdue --today 2026-10-19 $P/*-shokunin >/tmp/sf-probe-r5.out 2>&1
# window 2026-10-19T23:52:13Z .. 23:52:14Z; exit 2; 513 lines;
# missing=2; cadence=511; overdue=0; SOURCES.md hashes identical before/after: YES
```

## Independent expectation check (arithmetic, not row selection)

Expectations were generated from the pinned files with an awk classifier that uses the same
row gate **by design** (so it cannot detect indented-row misses) but hard-coded due dates
anchored by `date -u -d` above. Sets of expected `(lane, id, days)` were compared to the
actual overdue lines extracted from R3/R4:

```
comm -3 /tmp/sf-probe-expect-t2.sorted.txt /tmp/sf-probe-actual-t2.txt   # R3: empty, rc=0
comm -3 /tmp/sf-probe-expect-t3.sorted.txt /tmp/sf-probe-actual-t3.txt   # R4: empty, rc=0
# cross-check: overdue lines with recheck not in {90d,180d,2027-01-17} = 0 (R3+R4)
```

- R3 expectation 116 rows, all due `2027-01-17`, expected/observed days `0` — exact match.
- R4 expectation 196 rows: 116 due `2027-01-17` → `90d`, 80 due `2027-04-17` → `0d` — exact
  match on membership and day tokens.

## Conclusion (established / not established)

Established for the pinned 17-file snapshot (script `aed9ed65…`, files as hashed above):

- ISO dates are judged by calendar date only: no `cadence` line; overdue iff date <= today;
  days = calendar difference (R3/R4).
- `NNd` is judged as `opened + N days`: `cadence` line always, `overdue` iff due <= today,
  days = difference (R3: 90d→0d; R4: 90d→90d, 180d→0d).
- Symbolic cadences are reported as `cadence` only and never appear as `overdue` (0 such
  lines across R3+R4, including `every round` with a space).
- Boundary is exact: silent on `2027-01-16`, reports `0d` on `2027-01-17`.
- Exit semantics: all lanes present and nothing due → 0; findings → 1; any missing
  `SOURCES.md` → 2 (observed masking 120 findings).
- Behavior note: header line 34 describes `cadence` output for symbolic cadences, but the
  code (522–524) also emits it for `NNd`; observed. Not a correctness claim either way.
- Observed output shape: `cadence` lines stream in roster order, then the `overdue` block is
  appended, sorted by day count descending (R4 first `90d`, last `0d`).

Not established / explicitly bounded:

- **No completeness claim.** The gate skips any indented row; measured 0 such rows in the
  pinned 17, but the parent's fix is in progress and final files are not ready. No total here
  is a census result.
- 4 of 21 lanes lacked `SOURCES.md` at start; 2 still absent (`audio`, `game-dev-2d`);
  `kaidoku`/`kumitate` appeared mid-probe and are covered only by post-drift runs R1b/R5.
- Invalid-recheck handling in `overdue` mode was not exercised (0 invalid rows in the pinned
  set); only code-read: invalid values yield `INVALID_EPOCH` and are silently skipped.
- DST-observing timezones not exercised; host `-03` has no DST and day diffs are exact.
- No claim about symbolic-cadence policy correctness, SHONEN truth, or corpus-gate semantics.

## MUST rerun after parser fix + `FINAL LANES READY`

1. Rebind revisions: `git -C <lane> rev-parse HEAD` for all 21 lanes plus full `sha256sum`
   of each `corpus/SOURCES.md` and of `scripts/sources-census.sh`. If the script hash differs
   from `aed9ed65…`, every observation above is void.
2. Confirm all 21 lanes carry `SOURCES.md`; expect zero `missing` lines. Re-run the primary
   fixed-date command (`overdue --today 2026-10-19 $P/*-shokunin`) and record exit; with no
   due rows expect exit 0, with findings expect exit 1. Exit 2 now also means missing lanes.
3. Re-scan indentation on the final files (`grep -cE '^[[:space:]]+\|'`, plus the
   non-pipe-start S-row scan). If the fix changes the row-start gate, recompute the expected
   `cadence` count as "parser-visible rows whose recheck is `NNd` or symbolic" — do not reuse
   469.
4. Rebuild the independent expectation sets from the final files (recompute due dates with
   `date -u -d "<opened> + N days"`; do not reuse this note's date map if `opened` or recheck
   forms changed), then re-run `2027-01-16`, `2027-01-17`, `2027-04-17` over all 21 lanes and
   re-diff with `comm -3` including day tokens. All three dates derive from `opened =
   2026-10-19`; recompute anchors if any final `opened` differs.
5. Re-run the boundary pair (one day before / on due) and the exit-precedence check (missing
   vs findings) on the final lane set.
6. If the fix alters `cadence` emission or symbolic handling, repeat all four date points.

## Cleanup

No repo was modified (script writes stdout only; no `--out`; no git/state changes). Scratch
files `/tmp/sf-probe-*.out|err|txt` were removed after this note was written. Only artifact
left by this seat: this note.
