# souji — round 31 report (attempt 1)

Lane repo: `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`.

- Base: `9f17a1ef571f3a510a51ac233d7cf50ac0c871fc`.
- Final lane HEAD: `d999c596d389dbc710e939b340066297046f3204`.
- `git ls-remote origin refs/heads/master` prints that hash.
- `jj-lane.sh state` reads `ahead=0 behind=0 tracked=0 untracked=0`.
- Lane L1: SoujiR31.

## Work performed

The claims were frozen in `census/round-31/records/preregistration.txt` at commit `1d45496ae0e519b6fa0e9fa3b1f7e16130f4b525`. The controls were committed at `ed17ff6d95cc35d95038fdaef0e7e51c8e5d6bfc`. Both commits landed before any seat ran.

- **C1 — calibration** (the lowest non-retired axis, 7). Claim: every one of the 41 count literals in the SCORECARD capability cells is bound to an observable that shows it. That observable is either a command that prints the literal now, or an unchanged record from the row's own round. This answers routed r30 closure defect 2. **Verdict: MISSED by one item (34 → 1).**
- **C2 — operability** (8). Claim: `tools/souji-landing-gate.py` reads the committed record as written. That means three things:
  - the union of the force-added wave reports and the committed capture;
  - every `## Seat-reported failures` section, not only the first;
  - no tokenizer false positives.

  This answers routed defect 4 and the r30 residuals. **Verdict: MET.**
- **C3 — coverage** (8, the F1 frontier). Claim: a new entry on what keeps an abandoned commit's object present after its jj keep ref is dropped, and what removes it. It is measured with real jj 0.45.1 and git 2.56.0. It is the round's sourced claim, resting on S222 (git-reflog, opened this round). **Verdict: MET on its counters.** Wave-2 SwarmCritic21 judges the move to be depth rather than new coverage; that verdict is left for the closure.

Work items, each with its commit:

- Preregistration, the frozen counters (`tools/souji-capability-cells.py`, `census/round-31/c2-counter.py`, `census/round-31/c3-counter.py`), the enumeration `census/round-31/c1-cells.tsv` and the start census: `1d45496ae0e519b6fa0e9fa3b1f7e16130f4b525`.
- Controls (`census/round-31/records/controls.tsv`) and amendment A0 (C3 v2, PATH-shim leg), added before dispatch: `ed17ff6d95cc35d95038fdaef0e7e51c8e5d6bfc`.
- C1 base output and the M1 red-before receipt: `1b811368461785040e955f41f9c97e62f61fd67c`.
- Stricter amendments after the wave-1 attacks, with their controls: `26153a421374db2497e451230f33b2af78b3d128` and `6fdd69673e3aec5ef64ce4f9f25f452c4f4447d3`. A correction to the amendments record landed at `52ebd480461b481aeabadf143881223290c6fea2`.
  - A1: C3 v3, a remover-subtraction leg. It answers SwarmCritic30, who met the C3 v1/v2 targets with a fixture that cats a record.
  - A2: C1 count shape.
  - A3: C2 v2, a SHIFT oracle.
  - A4: C1 binding rules. It answers SwarmCritic28 and SwarmCritic31.
- C2 gate and fixture `tests/fixtures/r31-landing-gate-precision.py` (cases G1-G10): `8024b540b04d677d47cf51a0d1132ec8705ef14a`. The landing included an L1 patch for fence-aware section reading.
- C3 changes: `1baf4da02b71b012ee2426ea7c309496c0c3aca0`.
  - The entry `corpus/knowledge/jj-dropped-keep-object-lifetime.md` and the new row S222.
  - Fixture `tests/fixtures/r31-jj-object-clock.sh` and record `census/round-31/records/jj-object-clock-run.txt`.
  - Snapshots under `census/round-31/sources/`.
  - README, PROVINCE and SKILL text. This includes the routed r30 defect 1 fix to the SKILL keep-ref bullet (the packed-ref caveat, and `6 to 2`).
- C1: 40 appended supersession rows in SCORECARD.md: `24f343c8ffc820c0f89b4252cbdc94ab9a673aab`.
- M1 (mined mistake): append-only carries for rounds 26, 27 and 28 (26, 29 and 19 entries): `c6108301cbf0ca0ad086ff0ece6b76adad6b74b6`.
- Wave-1 capture, A5 (C2 v3 with random SHIFT probes, after SwarmReviewer26 beat v2) and the A1-regex receipt for routed defect 3: `2c16d018e40db7c23420a2c3bb546b52957bcc25`.
- Wave-2 corrections, D1 disclosure and partial wave-2 capture: `76bb697cf17de2291ee7fc5ee4a3107ae1785e80`.
  - The C3 entry's corrections (18 bullets).
  - The README F1 frontier correction.
  - M1 disposition corrections from the wave-2 audits.
  - The D1 disclosure (the record carries a `reflog-only` arm outside the frozen arm list).
- Lesson `corpus/lessons/round-31.md`, QUALITY Q67-Q69, SKILL gate rows, SCORECARD r31 measurements, capability rows and planned r32, LOG entry, end census, and the per-commit gate receipt for routed defect 5: `f950267893340096964ae8ceb7116f6789d7c87b`.
- Final-tip receipt `census/round-31/records/final-tip-measure.txt`: `d999c596d389dbc710e939b340066297046f3204`.

Round shape: **two v1 waves**, dispatched inline by the orchestrator through ready files.

| wave | purpose | seats | role mix | flash / attack |
|---|---|---|---|---|
| W1 `souji-r31-w1` | build plus first falsifiers | 38 | executor 10, scribe 9, scout 4, critic 4, reviewer 3, mutation-tester 3, connector 2, revenger 1, sentinel 1, simplifier 1 | 26 / 10 |
| W2 `souji-r31-w2` | falsify what landed | 36 | critic 10, executor 6, scribe 6, reviewer 5, mutation-tester 3, scout 2, connector 2, sentinel 1, simplifier 1 | 24 / 18 |

- Round total: **74 seats**, no residual call, **0 dead seats**.
- Every seat wrote its report: W1 38/38 per `census/round-31/waves/w1-results.json`; W2 36/36 reports, captured under `census/round-31/waves/w2/`.
- The validator rejects `planner` as a swarm role, so the L1 held the canonical planner seat.
- One W1 reviewer (SwarmReviewer26) ran long and was nudged once by message.

## Landed changes

All rows tie to the LOG.md entry "2026-10-26 — Round 31 attempt 1: capability-cell binding, landing-gate reading precision, F1 dropped-keep-ref object lifetime".

| change | commit |
|---|---|
| preregistration, frozen counters, C1 enumeration, start census | `1d45496ae0e519b6fa0e9fa3b1f7e16130f4b525` |
| controls and A0 | `ed17ff6d95cc35d95038fdaef0e7e51c8e5d6bfc` |
| C1 base output and M1 red-before | `1b811368461785040e955f41f9c97e62f61fd67c` |
| A1-A3 and their controls | `26153a421374db2497e451230f33b2af78b3d128` |
| amendments record correction | `52ebd480461b481aeabadf143881223290c6fea2` |
| C2 gate and fixture | `8024b540b04d677d47cf51a0d1132ec8705ef14a` |
| C3 entry, S222, fixture, record, docs | `1baf4da02b71b012ee2426ea7c309496c0c3aca0` |
| A4, C3 measurements | `6fdd69673e3aec5ef64ce4f9f25f452c4f4447d3` |
| C1 supersession rows | `24f343c8ffc820c0f89b4252cbdc94ab9a673aab` |
| M1 carries, C1 measurements | `c6108301cbf0ca0ad086ff0ece6b76adad6b74b6` |
| wave-1 capture, A5, A1-regex receipt | `2c16d018e40db7c23420a2c3bb546b52957bcc25` |
| wave-2 corrections, D1 | `76bb697cf17de2291ee7fc5ee4a3107ae1785e80` |
| lesson, QUALITY, SKILL, SCORECARD, LOG, census, wave-2 capture | `f950267893340096964ae8ceb7116f6789d7c87b` |
| final-tip receipt | `d999c596d389dbc710e939b340066297046f3204` |

Inherited state: the worktree was clean at start, and `.ufo/watchdog.log` holds no earlier attempt of this round. Nothing was inherited or discarded.

## Before → after measurements

### C1

Command: `python3 -B tools/souji-capability-cells.py --root <lane> --rev <full40> --base 9f17a1ef571f3a510a51ac233d7cf50ac0c871fc --list-rev 1d45496ae0e519b6fa0e9fa3b1f7e16130f4b525`. The v1 instrument is the blob at `1d45496`; the current file is v1 plus A2 and A4.

| when | revision | reading | record |
|---|---|---|---|
| base | `1d45496` | `items=41 bound_run=7 bound_record=0 unbound=22 mismatches=34` | `census/round-31/records/c1-before.txt` |
| landing | `24f343c8ffc820c0f89b4252cbdc94ab9a673aab` | `items=41 bound_run=20 bound_record=20 unbound=1 mismatches=1` under v1 and under A2+A4 | `c1-after-v1.txt`, `c1-after-a4.txt` |
| final tip | `f950267` | same reading | `final-tip-measure.txt` |

**MISSED** by the frozen kill rule. L29 (`remote-source-after.json18/18`, SCORECARD.md:170) has no honest binding: its record states the count only as separate scalar JSON fields. W1 SwarmExecutor04 and W2 SwarmCritic04 agree.

### C2

Commands: `python3 -B census/round-31/c2-counter.py --root <lane> --rev <full40> --base 9f17a1ef571f3a510a51ac233d7cf50ac0c871fc --fleet-root /home/vgpnk/Projects/shokunin`, plus `c2-counter-v2.py` (A3) and `c2-counter-v3.py` (A5, random probes) with the same arguments.

| when | revision | reading | record |
|---|---|---|---|
| base | `1d45496` | `fp=13 real=2 cne=0 r26=466 fixture=fail redarm=fail regress=same` | `census/round-31/records/controls.tsv` |
| landing | `8024b540b04d677d47cf51a0d1132ec8705ef14a` | `fp=0 real=2 cne=0 r26=495 fixture=ok redarm=ok regress=same`, plus `shift=ok` under v2 and two random v3 runs | `c2-after-v1.txt`, `c2-after-v2.txt`, `c2-after-v3.txt` |
| final tip | `f950267` | same reading | `final-tip-measure.txt` |

**MET.**

### C3

Commands: `python3 -B census/round-31/c3-counter.py --root <lane> --rev <full40> --base 9f17a1ef571f3a510a51ac233d7cf50ac0c871fc`, plus `c3-counter-v2.py` (A0) and `c3-counter-v3.py` (A1) with the same arguments.

| when | revision | reading | record |
|---|---|---|---|
| base | `1d45496` | `legs=11 fail=10 f1_entries=3` | `controls.tsv` |
| landing | `1baf4da02b71b012ee2426ea7c309496c0c3aca0` | v1 `legs=11 fail=0 f1_entries=4`, v2 `legs=12 fail=0`, v3 `legs=13 fail=0` | `c3-after-c3-counter*.txt` |
| final tip | `f950267` | same reading | `final-tip-measure.txt` |

**MET.**

### No harm

W2 SwarmExecutor27 re-ran 62 lane fixtures and selftests at base and at tip.

- 57 print the same exit code and last line.
- 5 differ, all benign, and none goes from green to red.
- The registry and coverage agreement counters read 0/0 at both revisions.
- The r30 capability counter reads `k1=0` at the tip.

## Sources & frontier

- **SOURCES rows**: 145 at base, 146 at the tip.
  - Count command: `git show <rev>:corpus/SOURCES.md | grep -cE '^[[:space:]]{0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`.
  - Rows added by tier: A=1, S222 (git `Documentation/git-reflog.adoc` at v2.56.0), `mined`, opened 2026-10-26.
- **Rows touched** (`used-by` only, logged old→new in `corpus/lessons/round-31.md` `### SOURCES touched-row log`): S002, S054, S063, S117 and S220 each gained `corpus/knowledge/jj-dropped-keep-object-lifetime.md`.
- **Census**: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`. It printed `souji ok`, exit 0 and 36 W04 at both start and end (`census/round-31/records/census-start.txt`, `census-end.txt`).
- **Frontier advanced**: F1, object lifetime behind a dropped keep ref (`corpus/README.md` `## Round 31` section and the F1 map row). The remaining F1 item is the fleet exposure numerator re-census.
- **Sourced claim**: C3 (S222).
- **Mined mistake**: M1. The lessons of rounds 26, 27 and 28 carried no seat failures.
  - Base gate before: 18, 29 and 19 `LG-SEAT-UNCARRIED`. After: 0 (`census/round-31/records/m1-red-before.txt`, `m1-after.txt`).
  - Wave-2 audits found the carries' dispositions partly wrong: 10/26, 3/29 and 5/19 entries.
  - Append-only audit corrections landed at `76bb697`. This is recorded as a second mistake row in the lesson.
- **Assimilation: none.** W1 SwarmScout14 swept 68 staged `merge/souji/` entries.
  - None measures object lifetime behind a jj keep ref.
  - Per-entry rejects are in the lesson's `## Gate`.
  - The id-collision guard found 37 collisions, but nothing was appended.
- **considerthese/**: absent in this lane.

## Trend verdicts

- **expansion — unprovable-but-better.** One admitted F1 entry, measured with 17 RESULT lines across three arms and replicated independently by W2 SwarmExecutor17. It cites S222, opened this round. Against it: W2 SwarmCritic21 judges it depth on held ground, and 18 sentences were corrected append-only after wave 2.
- **quality — improved.**
  - The landing gate drops 13 false dangling pointers.
  - It reads 29 hidden round-26 reports.
  - It reads append-only carry sections.
  - The SKILL keep-ref bullet is corrected (routed defect 1).
  - 74 seat failures from rounds 26-28 are carried.
  - The landing gate is clean (0 findings) for rounds 26-31 at the tip.
- **discernment — unchanged.** C1 missed. Every frozen counter except C1's v1 was shown gameable by wave-1 seats before landing (C2's v1 to v3 included, per W2 SwarmCritic12). Stricter amendments A1-A5 were added and disclosed. No outside spot-check exists yet.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md `## Gate registry` rows `souji-capability-cells`, `r31-landing-gate-precision`, `r31-jj-object-clock`; error-pattern bullet "jj: an object outlives its keep ref"; corpus/SOURCES.md S222
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:362 (2026-10-19 operator sweep); round 31 LOG entry at the end of LOG.md
- [~] Instructions executable by an agent without oral context — census/round-31/records/final-tip-measure.txt (every claim re-measured from committed bytes by documented commands)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md `## Round 31 boundary note (F1 object lifetime)`; census/round-31/waves/w2/SwarmConnector28.md (no sibling holds the round's surfaces)

## Other report lines

- **Cross-domain evidence**: none contested; 20 sibling lanes were scanned (W1 SwarmConnector35, W2 SwarmConnector28). `scripts/hyaku/jj-lane.sh` runs neither `jj util gc` nor `git reflog expire`; that is reported, not absorbed.
- **Misroot sweep**: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file written by a souji round-31 seat. The two untracked fleet files belong to other lanes or the driver, and were left alone.
- **Stale-lane**: this mission launched at `2026-10-26T02:55:57-03:00` (`.ufo/watchdog.log`, respawn-per-round driver). It has made 14 lane commits and is landing now. No other mission of this lane is open.
- **Tool installs**: none by the L1. No seat reported one. pacman stayed paused.
- **Scratch**: `/fast/scratch/hyaku/souji-r31` is removed after landing.
- **Open L0 questions**: none filed.
- **Residuals routed to r32** (SCORECARD `### Planned (appended at round 31)`; lesson `## Residuals`):
  - L29's binding.
  - The enumeration gap: count statements outside the C1 notation.
  - The file-granular record rule.
  - The C2 oracle envelope: randomize the heading, order and round, and use an orphan probe commit.
  - The letters-only prose blind spot.
  - Two surviving gate mutants (M4 fence awareness, M10 digit prose).
  - Rounds 15, 19, 23, 24 and 25 still carry uncarried seat failures.
  - `/var/tmp` snapshots in the gate (§7 item 4).
