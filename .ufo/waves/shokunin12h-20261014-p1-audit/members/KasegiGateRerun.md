# Kasegi gate rerun — advisory data

Lane: `/home/vgpnk/Projects/shokunin/kasegi-shokunin`
Landed HEAD observed before the runs: `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc`
Parent: `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1` (round-19 census commit)
Record compared: `corpus/lessons/round-20-recensus.md` (not trusted; re-measured)
Cwd for every command: the lane root. `KASEGI_MIRROR`, `KASEGI_ORIGIN_ROOT`, `KASEGI_LANE_ROOT`, and `UFO_SRC` were unset. No lane file was left modified.

Axes used: freshness (live re-run, not the lesson's numbers), operability (argv + exit + last line), calibration (quoted counters vs raw output), adjacency (stay on the three safe gates; do not edit the lane).

## Commands

| argv | exit | stderr | last stdout line |
|---|---:|---:|---|
| `python3 corpus/instruments/anchorcheck.py SKILL.md` | 0 | empty | `LOST-RECORDED md:989 [lost-base] check-freshness.mjs:61 (not checked)` |
| `python3 corpus/instruments/density.py SKILL.md --label audit` | 0 | empty | `Total path-citation instances: 645 across 18 blocks.` |
| `python3 corpus/instruments/resolve.py .` | 0 | empty | `wrote /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/instruments/citation-survival.md` |

`anchorcheck` printed 315 stdout lines (1 blank + summary + 313 per-cite rows) in 0.017s. `density` printed 30 lines in 0.020s. `resolve` printed 3 lines in 5.183s and rewrote the two census files; those writes were restored (below).

`anchorcheck` summary is not the last line. It is stdout line 2, printed before the per-cite dump:

```
== SKILL.md: 7 in-range cite instances, 0 bad; 7 distinct anchors; LOST-RECORDED=306 PIN-BROKEN=0 ORIGIN=0 OUTSIDE-BASE=0 BASE-ABSENT=0
```

Per-cite rows after that line: `LOST-RECORDED` 306, `OK` 7. No `MISSING-FILE`, `PAST-EOF`, `PIN-BROKEN`, `OUTSIDE-BASE`, or `BASE-ABSENT` rows.

`density` header (label-only): `# Density census — audit (1012 lines, 18 blocks)`. Mean row: `**154.0**`. Last line as in the table.

`resolve` stdout, all three lines:

```
distinct=1480 resolves=10 mirror=0 internal=123 other=0 gone=1347 skill=32/506 corpus=117/1153 all=133/1480
wrote /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/instruments/citation-survival.tsv
wrote /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/instruments/citation-survival.md
```

Derived mirror recorded by that run: `/home/vgpnk/Projects/the-bounty-hunter` (ABSENT — mirror fallback disabled). `isdir` checks this session: `~/Projects/the-bounty-hunter` false, `~/Projects/origin-work/open-bug-bounties` false, `~/Projects/ufo-fsd-alpha` true.

## Claim-by-claim vs `corpus/lessons/round-20-recensus.md`

### anchorcheck — agree on quoted counters; disagree that the quoted string is the raw verdict line

Lesson: exit 0, `7 in-range / 0 bad / LOST-RECORDED=306 / PIN-BROKEN=0 / OUTSIDE-BASE=0 / BASE-ABSENT=0`.

Observed exit 0. Every quoted counter is in the summary and matches. The raw summary also has `7 distinct anchors` and `ORIGIN=0`, which the lesson omits. The last stdout line is a `LOST-RECORDED` detail row, not that summary. Exit 0 here is "process finished"; this run had `bad=0`, so the exit code does not separately prove a fail-closed gate.

### density — agree

Lesson argv uses `--label r20-recensus` and claims exit 0, `645` path-citation instances across 18 blocks.

This rerun used the prescribed `--label audit`, not the lesson's label. `density.py` interpolates the label only into the header. Observed last line: `Total path-citation instances: 645 across 18 blocks.` Exit 0. 18 blocks. Mean `154.0` matches the round-19 LOG/SCORECARD figure; the round-20 lesson does not restate the mean.

### resolve — disagree that the landed census is what this command emits

Lesson: exit 0, regenerated `citation-survival.tsv` / `citation-survival.md`. Debt section calls the regenerated census `116/1144` and `132/1471`.

Observed exit 0, and the command does write those two paths. The bytes it wrote are not the committed bytes.

| | committed (restored) | fresh run, then discarded |
|---|---|---|
| md sha256 | `483c14112ea6a1ade07fdf7377755d7c6d2d638734e8cce04abf7de41d616c98` (15231 bytes) | `e25f27bd2a0a596c4335294a79007e3df690c88a4bbf0035caa717aab8b04417` (15237 bytes) |
| tsv sha256 | `d12387cff5516429ea9fb62a70a6445d54ec6dc1de2190c525c8d3bdd677b22f` (93767 bytes) | `6093adca894eb8baecc190034dde5339afb39a0d6fb1a7b01674dda9d904193d` (94303 bytes) |
| git blob | md `f1cf734b0243d74c65a25b44ca684bbcefe3bcf7`, tsv `bd94affa3abc157057d5b5dcf71bb5a980975ef9` | not committed |

Those git blobs are identical at `HEAD` and `HEAD^`. `git show --stat HEAD` touches only `LOG.md`, `SCORECARD.md`, and `corpus/lessons/round-20-recensus.md` (48 insertions). Round 20 did not change the census paths. Last commit that did is `d1e6e8f` (round 19).

Committed census header (what the lesson's `116/1144` / `132/1471` matches): scope 49 files, distinct 1471, SKILL `32/506 = 6.32%`, corpus `116/1144 = 10.14%`, lane `132/1471 = 8.97%`, RESOLVES 9, GONE 1339.

Fresh run on the landed tree: scope 50 files, distinct 1480, occurrences 2925, SKILL still `32/506`, corpus `117/1153 = 10.15%`, lane `133/1480 = 8.99%`, RESOLVES 10, GONE 1347, mirror 0, internal 123.

No pre-existing citation changed class. TSV-only additions, each `files_citing_count=1`, scope `+CORPUS`:

| citation | class | why it appeared |
|---|---|---|
| `.ufo/waves/shokunin12h-20261014-p1-repair/members/Kasegi*.md` | GONE | lesson line 4; `*` makes it synthetic |
| `116/1142` | GONE | lesson line 32; `/` makes the fraction path-like; no noise flag |
| `116/1144` | GONE | lesson line 33; same |
| `132/1469` | GONE | lesson line 32; same |
| `132/1471` | GONE | lesson line 33; same |
| `python3 corpus/instruments/anchorcheck.py SKILL.md` | GONE | lesson line 8; shell flag |
| `python3 corpus/instruments/density.py SKILL.md --label r20-recensus` | GONE | lesson line 11; shell flag |
| `python3 corpus/instruments/resolve.py ` | GONE | lesson line 13. Trailing `.` is stripped by `rstrip(".,;:")`, leaving a trailing space; shell flag |
| `~/Projects/ufo-fsd-alpha/` | RESOLVES | lesson line 21; directory exists (`literal` → `/home/vgpnk/Projects/ufo-fsd-alpha/`) |

The 50th scanned file is tracked `corpus/lessons/round-20-recensus.md`. Walk is `SKILL.md` plus `corpus/**/*.md` excluding generated `corpus/instruments/citation-survival.md` (`resolve.py` `collect`). 49 other tracked md files plus that lesson = 50. `citation-survival.md` itself went from 1 citing file / 3 occurrences to 2 / 4 because the lesson cites it.

Second md-only drift, not a class change: anchor row `` `SCORECARD.md:23` `` recorded file length 180 in the committed census and 186 on the fresh run. `wc -l SCORECARD.md` is 186. `HEAD` adds 6 lines to `SCORECARD.md`. Anchor 23 is still in range. So the committed census is also stale against the round-20 scorecard edit, even apart from the new tokens.

Noise counters moved with those nine tokens: shell 49→52, synthetic 484→485, any-noise GONE 602→606, genuine GONE 737→741, glob/placeholder 551→552. The four fraction tokens are in the genuine-GONE bucket.

### "No gate change" / derived roots — partial; not a counterexample to absence

Lesson: both instruments already derive roots; explicit bad overrides stay bad; `$UFO_SRC` is not a real consumer because the anchor regex does not match `~/Projects/ufo-fsd-alpha/`.

Observed this run: mirror derived to the canonical absent path, not an env override. `anchorcheck.py` `CITE` has prefixes for `~/Projects/origin-work/open-bug-bounties/` and `~/Projects/the-bounty-hunter/`, not `~/Projects/ufo-fsd-alpha/`. That matches the regex claim. This rerun did not set `$UFO_SRC` and did not mutation-test "explicit bad overrides stay bad". `resolve.py` is a different instrument: the lesson's own `` `~/Projects/ufo-fsd-alpha/` `` token classified RESOLVES.

### Scorecard fraction debt — agree about the landed files; the "regenerated" side is not the live run

Lesson: scorecard corpus/lane rates (`116/1142`, `132/1469`) do not match the regenerated census (`116/1144`, `132/1471`).

Agree that landed `SCORECARD.md` round-19 verifiability cell still says corpus `116/1142 = 10.16 %` and lane `132/1469 = 8.99 %`, and that landed `citation-survival.md` says `116/1144 = 10.14%` and `132/1471 = 8.97%`. Those are different fractions. Disagree that `116/1144` and `132/1471` are what `python3 corpus/instruments/resolve.py .` emits on this tree. Live run: `117/1153` and `133/1480`. Three-way mismatch. SKILL `32/506 = 6.32%` is stable across the committed census, the round-19 LOG, and this run.

### Named in the lesson, not re-tested here

No agree/disagree from this gate set:

- `TRIAGE-LOST-BASE-MISPREFIX`, `CLAIM-CHECK-96-MIRROR-MISBASE`, `BLOB-PIN-LOWERCASE-PATH`, `CENSUS-NOTE-NEVER-LANDED`, `UFO-DOT-LISTING-DRIFT`, `UFO-HISTORY-NOT-INTACT`
- standing `RECEIPT-STORE-LOST`, `MIRROR-SOURCE-LOST`, `ORIGIN-REPO-LOST` (still the names in `SCORECARD.md`; roots still absent as checked above)
- the 50-file-deletion sentence / orphan `72ab84a8` / cross-history delete count 970
- suffix-join onto derived override roots left unlanded

## Restoration

`resolve.py` writes `citation-survival.tsv` and `citation-survival.md` next to itself (`here = dirname(__file__)`). Before the run those files were copied; after the run they were copied back and `utime` restored the prior nanosecond mtimes.

| file | sha256 before = after restore | mtime_ns restored |
|---|---|---|
| `corpus/instruments/citation-survival.md` | `483c14112ea6a1ade07fdf7377755d7c6d2d638734e8cce04abf7de41d616c98` | `1792023245662841702` |
| `corpus/instruments/citation-survival.tsv` | `d12387cff5516429ea9fb62a70a6445d54ec6dc1de2190c525c8d3bdd677b22f` | `1792023245658128516` |

`git status --short` on those two paths after restore: empty. Whole-tree `git status --short` after restore: `?? plans/wwkd-round-20-recensus.md` only. That untracked file was already present; this run did not create it; `resolve.py` does not walk `plans/`. No commit, no push, no lane edit left behind.

## Named debt (this rerun)

1. `RESOLVE-CENSUS-NOT-FIXED-POINT`
   Owner: kasegi record at `a5cbf77` (census blobs unchanged since `d1e6e8f`).
   Unblock: run `python3 corpus/instruments/resolve.py .` only after the recording lesson is frozen, and commit the new `citation-survival.md` / `.tsv`, or keep that lesson outside the walk before calling the census regenerated. Until then, do not treat `116/1144` or `132/1471` as the live instrument output. Live output is `skill=32/506 corpus=117/1153 all=133/1480`.
   Counterexample: the nine citations in the table above, plus `SCORECARD.md:23` file length 180 vs 186.

2. `SCORECARD-R19-FRACTION-STALE` (already named by the lesson; live run adds a third pair)
   Owner: `SCORECARD.md` round-19 verifiability cell, still quoting `116/1142` and `132/1469`.
   Unblock: mark that cell historical or replace it from a census generated after the round-20 text is stable. Not done here.

3. `RESOLVE-GATE-WRITES-LANE`
   Owner: `corpus/instruments/resolve.py` (writes beside the script on every successful run).
   Unblock: a non-writing mode, or any auditor snapshots and restores. This rerun restored exact bytes and mtimes. The prescribed gate is not side-effect free.
