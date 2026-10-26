# souji — round 32 report (attempt 2)

Lane repo: `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`.

- Base: `85b61a151923986e7e6b48f7084b9122561b5f3d`.
- Final lane HEAD: `04b9221347073b9c58624b36e8d849481e4dacd6` (final-tip receipt). `git ls-remote origin refs/heads/master` prints that hash; `jj-lane.sh state` reads `ahead=0 behind=0 tracked=0 untracked=0`.
- Lane L1: SoujiR32a2 (attempt 2), integrating attempt 1 (SoujiR32).
- Attempt 1's L1 died in the orchestrator host crash (2026-10-26 ~08:50 -03). By then it had run wave `w1` and landed C2, C3 and the C1 rows. Its falsify wave `w2` was never spawned and is marked ABANDONED. The orchestrator salvage commit `4e56c48b8fc828f9aba2746e324dc46aa538bdbf` committed its five after-records unverified (`.ufo/watchdog.log` line 1512, `lane-dead-no-report souji round=32`).

## Work performed

Three claims were frozen in `census/round-32/records/preregistration.txt` at `3ec84fc81b3243429c834a051880b0bcde06291c`, with controls at `7a6667cd27652baf8d704b5cdb8e3200bd6e27a1`. Both commits landed before any seat ran, and attempt 2 ran them unchanged.

- **C1 — calibration** (the lowest non-retired axis, 7). Bind each of 44 SCORECARD capability-cell count integers to an observable, or withdraw it, with at most 8 withdrawals. The 44 are the integers the r31 notation skipped, plus r31's unbound L29 (routed r31 defect 1). **Verdict: MISSED** (`unbound=6`, `withdrawn=17`).
- **C2 — operability** (8). 27 lane tool and fixture commands run with `/tmp`, `/var/tmp` and `/dev/shm` read-only, take scratch from `TMPDIR`, and still print their base result. This is prompt §7 item 4. **Verdict: MISSED** (`fail=2` at the landing, `fail=3` at the tip).
- **C3 — coverage** (8, F1 frontier; the sourced claim, S223). A measured entry on how an abandoned jj commit's own mtime decides its fate under `git gc`, including inside a cruft pack. **Verdict: MET on its counters.** Its prose was corrected append-only after the falsify wave.

Work items:

- Preregistration, frozen counters, enumerations, C3 contract, the M1 tool and its red-before receipt, and the start census: `3ec84fc81b3243429c834a051880b0bcde06291c` (attempt 1).
- Controls and amendment A0 (C1 v2: cited evidence and count adjacency), added before any seat ran: `7a6667cd27652baf8d704b5cdb8e3200bd6e27a1`.
- C2 landing: 26 tools and fixtures take scratch from `TMPDIR`. Commit `98e5203d45b4e419a9e72801733d93303acc7ebd`.
- C3 landing, commit `a92e1aae91dbf46c2d7eff713932cfc820186970`:
  - entry `corpus/knowledge/jj-abandoned-object-mtime-clock.md` and row S223;
  - fixture `tests/fixtures/r32-jj-mtime-clock.sh` and record `census/round-32/records/jj-mtime-clock-run.txt`;
  - snapshots, amendment A1 (C3 v2: legs L15-L17), and the routed r31 defect 2 fix.
- C1 rows: 38 appended binding rows. Commit `9e8982b7a6ac57dffa415f9db43cf7cd6e829c93`.
- Orchestrator salvage of the attempt-1 after-records: `4e56c48b8fc828f9aba2746e324dc46aa538bdbf`. These records are re-verified, not authored, by attempt 2.
- Attempt 2 dispatched falsify wave `a2w1` (38 seats). It re-measured every claim and verified the salvage. It also ran the no-harm sweep the preregistration had promised for wave 2. That sweep found four harms in the landed C2 bytes. Attempt 2 repaired them, with receipts in `census/round-32/records/a2-repairs.txt`:
  - two registered gates pinned `tools/souji-evidence-cache.py`'s digest; the file was reverted to its base bytes;
  - the r15 preservation frozen pin went stale; the record was regenerated with its own script, `verdict=clean`;
  - `tools/souji-receipt-run.py`'s `--out` guard followed a caller-set `TMPDIR`; it gained `OUT-IN-GIT-TREE`;
  - two SKILL pointers carried `../` and resolved outside the lane; the prefix was dropped.

  Landed in the integration commit `9da5e9a559f76ecbd275a9685226883d334dc8f9`, which also carries the lesson, QUALITY Q70-Q74, SCORECARD r32 measurements, capability rows and planned r33, the LOG entry, the C3 entry's 15 append-only correction bullets, SKILL/README/PROVINCE corrections, the salvage re-measure and the end census.
- Wave evidence capture (180 records: `w1`, `a2w1`, the abandoned `w2` plan) and the lesson's `## Seat-reported failures` carry (18 paragraphs): `4ea897fe95d5163b0a0674ee803daf8ee21d5e23`.
- Final-tip receipt `census/round-32/records/final-tip-measure.txt`: `04b9221347073b9c58624b36e8d849481e4dacd6`. It covers all frozen counters plus C3 v2 and the landing gate, measured at `4ea897f`.

Reused after re-verification:

- The frozen contract, controls, amendments and counters. Their blobs are unchanged since freeze; a2w1 `SwarmReviewer36` checked this.
- The three claim landings.
- Four of the five salvaged records, reproduced byte-for-byte by `SwarmReviewer36` and by the L1 (`census/round-32/records/a2-l1-salvage-tip-measure.txt`).
- The w1 reports and deliveries, adjudicated per finding (`census/round-32/waves/a2w1/deliver-w1-adjudication-a.md`, `-b.md`).
- The attempt-1 `w2` spec generator. It was re-dispatched as `a2w1` with four added items.

Discarded:

- The `w2` dispatch (never spawned).
- The salvaged `c2-after-v1.txt` reading `T12 PASS`. It does not reproduce: a2w1 `SwarmExecutor08` read `pass=25 fail=2` twice at the C2 landing commit.

Round shape: **two v1 waves**, dispatched inline by the orchestrator through ready files.

| wave | purpose | seats | role mix | flash / attack |
|---|---|---|---|---|
| attempt 1 `souji-r32-w1` | build plus first falsifiers | 44 | executor 19, scribe 7, critic 5, reviewer 3, mutation-tester 3, scout 2, connector 2, revenger 1, sentinel 1, simplifier 1 | 34 / 11 |
| attempt 2 `souji-r32-a2w1` | falsify what landed; verify the salvage | 38 | reviewer 13, critic 8, executor 6, scribe 3, mutation-tester 2, scout 2, connector 2, sentinel 1, simplifier 1 | 19 / 23 |

- Round total: **82 seats**, no residual call.
- Dead seats: 3, all in w1. `SwarmReviewer30`, `SwarmReviewer31` and `SwarmMutationTester40` left no report, and w1 has no results file because its L1 died before WAVE-DONE.
- a2w1: 38 reports and 38 result payloads (`census/round-32/waves/a2w1-results.json`), 0 dead.
- Attempt-1 `w2` (34 seats planned) never spawned and is not counted.
- The L1 held the canonical planner seat; the validator rejects `planner` as a swarm role.

## Landed changes

Every row ties to the LOG.md entry "2026-10-26 — Round 32 attempt 2: capability-count binding, lane-tool scratch discipline, F1 abandoned-object mtime clock".

| change | commit |
|---|---|
| preregistration, frozen counters, enumerations, C3 contract, M1 tool and red-before, start census | `3ec84fc81b3243429c834a051880b0bcde06291c` |
| controls, A0 | `7a6667cd27652baf8d704b5cdb8e3200bd6e27a1` |
| C2 scratch discipline (26 tools and fixtures) | `98e5203d45b4e419a9e72801733d93303acc7ebd` |
| C3 entry, S223, fixture, record, snapshots, A1, routed r31 defect 2 | `a92e1aae91dbf46c2d7eff713932cfc820186970` |
| C1 binding rows | `9e8982b7a6ac57dffa415f9db43cf7cd6e829c93` |
| orchestrator salvage of attempt-1 after-records | `4e56c48b8fc828f9aba2746e324dc46aa538bdbf` |
| attempt-2 integration: lesson, QUALITY Q70-Q74, SCORECARD, LOG, C3 corrections, C2 harm repairs, end census | `9da5e9a559f76ecbd275a9685226883d334dc8f9` |
| wave capture, seat-failure carry | `4ea897fe95d5163b0a0674ee803daf8ee21d5e23` |
| final-tip receipt | `04b9221347073b9c58624b36e8d849481e4dacd6` |

## Before → after measurements

### C1

Command: `python3 -B census/round-32/c1-counter.py --root <lane> --rev <full40> --base 85b61a151923986e7e6b48f7084b9122561b5f3d --list-rev 3ec84fc81b3243429c834a051880b0bcde06291c`. `census/round-32/c1-counter-v2.py` (A0) takes the same arguments.

| when | revision | reading (v1 and v2 alike) | record |
|---|---|---|---|
| base | `3ec84fc` | `items=44 bound_run=0 bound_record=0 bound_field=0 withdrawn=0 unbound=44 mismatches=44` | `census/round-32/records/controls.tsv`, `controls-a0.tsv` |
| landing | `9e8982b7a6ac57dffa415f9db43cf7cd6e829c93` | `bound_run=3 bound_record=9 bound_field=9 withdrawn=17 unbound=6 mismatches=6` | `c1-after-v1.txt`, `c1-after-v2.txt` |
| final tip | `4ea897fe95d5163b0a0674ee803daf8ee21d5e23` | same | `final-tip-measure.txt` |

**MISSED** on two counts:

- N28-N31, N33 and N34 have no row (`SCORECARD.md:422`).
- 17 withdrawals exceed the cap of 8.

The miss is in the enumeration rules, not stale counts. One item per digit run, a one-row-per-line cap, and digit-bearing unit words `k1` and `r26` make honest bindings impossible (w1 `SwarmExecutor04/05`). a2w1 audited all 38 rows: every MATCH row is honest, and N25 is one wrong withdrawal (`SwarmCritic04`).

### C2

Command: `python3 -B census/round-32/c2-counter.py --root <lane> --rev <full40> --base 85b61a151923986e7e6b48f7084b9122561b5f3d --list-rev 3ec84fc81b3243429c834a051880b0bcde06291c`.

| when | revision | reading | record |
|---|---|---|---|
| base | `3ec84fc` | `items=27 pass=1 fail=26` | `controls.tsv` |
| landing | `98e5203d45b4e419a9e72801733d93303acc7ebd` | attempt-1 record `pass=26 fail=1` (T18); a2w1 re-measure `pass=25 fail=2` (T12, T18), twice | `c2-after-v1.txt`; `census/round-32/waves/a2w1/SwarmExecutor08.md` |
| salvage tip | `4e56c48` | `pass=25 fail=2` (T12, T18) | `a2-l1-salvage-tip-measure.txt` |
| final tip | `4ea897fe95d5163b0a0674ee803daf8ee21d5e23` | `pass=24 fail=3` (T08, T12, T18) | `final-tip-measure.txt` |

**MISSED.** The three failing items fail for three different reasons:

- T18's anchor counts closure files changed since a pinned revision, so the round's own edits move it (26 → 31).
- T12's timed census selftest flips under strace even at the base revision.
- T08 fails at the tip because attempt 2 reverted `tools/souji-evidence-cache.py` to repair harms H1-H2.

**No harm at the tip, after repair.** The landed C2 had turned three gate surfaces red:

- `r22-result-oracle` and `census/round-22/mutation-adequacy.py` (a2w1 `SwarmExecutor16` H1-H2);
- `souji-preservation-evidence --frozen` and landing-gate `LG-FROZEN-PIN` (`SwarmExecutor17`).

It had also widened the receipt `--out` guard (`SwarmReviewer13`). All four were repaired; `census/round-32/records/a2-repairs.txt` has before and after runs. At the tip the landing gate reads `findings=0` for round 32.

Two LOW edge regressions remain: with a trailing-slash `TMPDIR`, the census and round-9 selftests fail (`SwarmReviewer12`).

### C3

Command: `python3 -B census/round-32/c3-counter.py --root <lane> --rev <full40> --base 85b61a151923986e7e6b48f7084b9122561b5f3d --list-rev 3ec84fc81b3243429c834a051880b0bcde06291c`. `census/round-32/c3-counter-v2.py` (A1) takes the same arguments.

| when | revision | reading | record |
|---|---|---|---|
| base | `3ec84fc` | `legs=14 fail=13 f1_entries=4` | `controls.tsv` |
| landing | `a92e1aae91dbf46c2d7eff713932cfc820186970` | v1 `legs=14 fail=0 f1_entries=5`; v2 `legs=17 fail=0 f1_entries=5` | `c3-after-v1.txt`, `c3-after-v2.txt` |
| final tip | `4ea897fe95d5163b0a0674ee803daf8ee21d5e23` | same | `final-tip-measure.txt` |

**MET.** Independent replication supports the verdict:

- a2w1 `SwarmExecutor18` replayed the fixture twice and rebuilt the clock by hand in plain git and in fresh jj.
- `SwarmCritic19` reproduced all 22 `RESULT` lines in plain git.

The C3 counters are weaker than this replication. A hybrid fixture that prints constants beats both v1 and v2 (`SwarmMutationTester22`). The entry's prose overclaimed, and 15 append-only correction bullets now stand in it (`SwarmCritic19/20/21`). The novelty is narrower than first stated: the survivor's location under cruft packing and the per-object clock are new; the recent/old pair was held at base.

## Sources & frontier

- **SOURCES rows**: 146 at base, 147 at the tip.
  - Count command: `git show <rev>:corpus/SOURCES.md | grep -cE '^[[:space:]]{0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`.
  - Rows added by tier: A=1. S223 is git `Documentation/gitformat-pack.adoc` at v2.56.0, `mined`, opened 2026-10-26.
- **Rows touched**, logged old→new in `corpus/lessons/round-32.md` `### SOURCES touched-row log`:
  - S002 used-by;
  - S051 used-by (routed r31 defect 2);
  - S063 anchor (CONFIGURATION, `config/gc.adoc` lines 96-147) and used-by.
- **Census**: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
  - Start: `souji ok`, exit 0, 36 W04 (`census/round-32/records/census-start.txt`).
  - End: `souji ok`, exit 0, 36 W04 (`census/round-32/records/census-end.txt`).
- **Frontier advanced**: F1, the abandoned object's own mtime clock and its cruft-pack location (`corpus/README.md` `## Round 32`, F1 map row). Wave a2w1 `SwarmScout23` re-fetched all three sources live, and 23 of 23 Gate quotes matched.
- **Sourced claim**: C3 (S223).
- **Mined mistake**: M1 (r31 D1, contract class). `tools/souji-record-contract.py` fails the r31 record, `lines=17 bad=4`, exit 1 (`census/round-32/records/m1-red-before.txt`).
  - Further rows in the lesson's `## Mistakes`: enumeration, anchor selection, cheatable instruments, digest-pinned consumers, write-scope widening, a flaky anchor, and an L1 misroot.
- **Assimilation: none.**
  - 20 staged `merge/souji/` entries were rejected per entry in the lesson's `## Gate`; none covers cruft packs or a per-object clock.
  - The id-collision guard (w1 `SwarmScout21`, scratch): 146 lane ids, 134 staged ids, 38 collisions (S109-S132, S152, S210-S222). Nothing was appended.
- **considerthese/**: absent in this lane.

## Trend verdicts

- **expansion — improved.** One admitted F1 entry with a new edge class: the survivor's location under cruft packing and the per-object clock inside a cruft pack. It rests on S223, opened this round, and was replicated independently (a2w1 `SwarmExecutor18`, `SwarmCritic19`). Against this: the recent/old half was already held, and 15 correction bullets were needed.
- **quality — improved, with disclosed residual edge regressions.**
  - 24 of 27 lane commands now honour `TMPDIR` under a read-only `/tmp` (base 1).
  - Four harms found by the no-harm sweep were repaired before the round closed. Every registered gate that a2w1 checked is green at the tip, and the landing gate reads `findings=0`.
  - Against this: two LOW trailing-slash `TMPDIR` regressions remain (`SwarmReviewer12`).
- **discernment — unchanged.** C1 missed again, and C2 missed. The frozen C2 and C3 counters were shown gameable (w1 `SwarmCritic34`, a2w1 `SwarmMutationTester22`). The salvaged T12 reading did not reproduce. Q70, Q73 and Q74 encode the lessons, but no outside spot-check exists yet.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md `## Gate registry` rows `r32-c1-counter`, `r32-c2-counter`, `r32-c3-counter`, `r32-jj-mtime-clock`, `souji-record-contract`; error-pattern bullet "jj: an unreferenced object dies by its own mtime"; corpus/SOURCES.md S223
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:362 (2026-10-19 operator sweep); the round-32 attempt-2 LOG entry at the end of LOG.md
- [~] Instructions executable by an agent without oral context — census/round-32/records/final-tip-measure.txt (every claim re-measured from committed bytes by documented commands); census/round-32/measure.sh
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md `## Round 32 boundary note (F1 mtime clock)` with its attempt-2 corrections; census/round-32/waves/a2w1/SwarmConnector28.md (0 contested scope across 960 sibling-lane files)

## Other report lines

- **Cross-domain evidence**: none contested (a2w1 `SwarmConnector28`; w1 `SwarmConnector41`).
- **Misroot sweep**: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file from a souji round-32 seat; the only untracked file is `.ufo/state/disk-guard.log`, which belongs to the driver.
  - One misroot was the L1's own. While reproducing `SwarmReviewer13`'s attack with the old receipt tool, the L1 wrote `/home/vgpnk/Projects/shokunin/zz-probe-souji.receipt`, a receipt of `--help`.
  - It was deleted at once and recorded in the lesson's `## Mistakes` and in `a2-repairs.txt` R1. QUALITY Q74 now requires a fake fleet root inside scratch for such reproductions.
- **Stale-lane**: this attempt launched at `2026-10-26T09:23:46-03:00` (`.ufo/watchdog.log` line 1513, respawn-per-round driver, attempt 2). It made 3 lane commits; the round has 9 in total, counting attempt 1 and the salvage. No other mission of this lane is open.
- **Tool installs**: none by the L1. No seat reported one. pacman stayed paused.
- **Scratch**: `/fast/scratch/hyaku/souji-r32` and the L1's mis-rooted measure dir `/fast/scratch/hyaku/l1` were removed after landing. `/fast/scratch/hyaku/souji-r31` is from round 31 and was left to the driver's purge.
- **Open L0 questions**: none filed.
- **Residuals routed to r33** (SCORECARD `### Planned (appended at round 32)`; lesson `## Residuals`):
  - C1's per-statement enumeration, a pre-freeze feasibility leg (Q70), and the 6 unbound and 17 withdrawn items.
  - C2's predicate gaps.
  - The cache-tool digest pin in `census/round-21/run-acceptance.py`.
  - The trailing-slash regressions.
  - Two remaining literal `/var/tmp` scripts.
  - The receipt guard for a non-repository `TMPDIR`.
  - M1's literal-prefix scope.
  - C3's beatable counters.
  - Wave-spec hygiene.
