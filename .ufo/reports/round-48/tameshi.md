# tameshi — round 48 report (attempt 3, L1 TameshiR48a3)

Lane `tameshi-shokunin`, branch `master`. Base `473336d9d789f6081195e7376d17836a24666bc3`; content (deciding) revision `c7586b9a10effc63b4bd327f976edc094c1bdc17`; final lane hash `98e6304451f789413a21d30f16abf21bb7033c21`. Attempt history: attempt 1 (TameshiR48) died in the orchestrator host crash, salvaged at `15b1521e`; attempt 2 (TameshiR48a2) stalled after its wave returned and was killed at wrap-up, salvaged at `8f2922b8` (`.ufo/watchdog.log` lines `lane-dead-no-report tameshi round=48`). Attempt 3 inherited both salvages, re-verified them (below), and ran the claims unchanged.

## Work performed

Declared claims (frozen at `e73389c0` / `f1cfaad3`, amendments 1-10 in `.ufo/evidence/round-48/contract.json`, counters frozen at `755298415f8c`, `freeze-2.json`):

- **C1, calibration** (lowest non-retired axis, monitor 6): for each of the 22 frozen statements, the last `runs 3` SCORECARD row declares a value set, class, tool sha256 and deps set that three observation rounds of six profiles confirm, `C1_R48_PASS=true` (total=0).
- **C2, freshness** (the round's sourced claim): held rows S026, S048, S093, S108 each superseded by a row opened 2026-10-26 with committed snapshot, fetch receipt, located phrase-bearing Gate quote and re-pointed entries, `C2_R48_PASS=true` (refreshed=4, census exit 0).

Work items:

- Pre-registration, amendments and counter freeze (attempt 1): `e73389c0`, `f1cfaad3`, `7552984`; selftests `C1_R48_SELFTEST: cases=76 failed=0`, `C2_R48_SELFTEST: cases=43 failed=0` (`.ufo/evidence/round-48/selftest/c{1,2}-r48-selftest.stdout`).
- C2 records (attempt 1): rows S265-S268 at `corpus/SOURCES.md:140-143`; snapshots and fetch receipts `.ufo/evidence/round-48/freshness/sources/`; Gate lines `corpus/lessons/round-48.md:21-24`; four entries re-pointed (`5054532`).
- C1 rows (attempt 2): the 22 standing rows restated from the counter's own `--emit` at `15b1521e` (`.ufo/evidence/round-48/calibration/emit-15b1521.stdout`), `SCORECARD.md:2330-2356` (`c7586b9a`).
- Controls: C2 CTL_F/G/H at freeze bytes `F=0 G=0 H=2 ok=true` (`.ufo/evidence/round-48/control/c2-controls.stdout`); C1 CTL_A at freeze bytes `total=22 unparsed=22 C1_R48_PASS=false` (`control/c1-controls.stdout`, attempt 2, harness stopped before B-E); **attempt 3 scored CTL_B-E** with the frozen harness's own functions (`control/run-controls-a3.py`, harness sha256 `f5732f18` checked at load): CTL_B `total=5 mismatches=1 dep_mismatch=4 C1_R48_PASS=false` (the round-47 rows relabelled `runs 3 stable` with no re-observation are refused); CTL_C `total=26 unattested=21 attested_extra=126 C1_R48_PASS=false` (superset cheat refused as unattested); CTL_D `total=23 dep_mismatch=22 C1_R48_PASS=false` (deps-everything refused); CTL_E `total=0 C1_R48_PASS=true` (positive control: the counter can pass). Exit 0, 3h14m (`control/c1-controls-a3.start`, `.end`), per-control stdout `control/c1-CTL_{B,C,D,E}-a3.stdout`. The cheapest control (CTL_B) does not reach the target.
- Deciding runs at `c7586b9a`: C2 once, by attempt 2's `deciding-run.sh` (`after/c2.stdout:5`, `C2_R48_PASS=true`); C1 by attempt 3 (`after/c1-a3.stdout:96`, `C1_R48_PASS=true`, exit 0, 46m34s, landed `c6295cb0`). Attempt 2's C1 step was killed and left a zero-byte `after/c1.stdout`; see the C1 verdict below.
- Frozen-bytes check: `after/frozen.stdout` prints `FROZEN_UNCHANGED=0`; the only frozen-path differences freeze→content are four *added* receipt files under `control/` (`git diff --name-status 75529841 c7586b9a -- .ufo/evidence/round-48/control` → `A c2-controls.{exit,meta,stderr,stdout}`); contract, both counters and both control scripts re-hash equal to `freeze-2.json` at `c7586b9a` (contract `4fff75db`, `572a5670`, `faefe9b4`, `f5732f18`, `46b8c039`). A false red of the script's path list, disclosed.
- No-harm at `c7586b9a`: 8/8 monitors ok (`after/no-harm.stdout`), census exit 0 (`after/census.exit`), **cold-read credited sections 57 < 60 (RED)** (`after/coldread-sections.stdout`), caused by C2's entry re-pointing (three ledger-credited sections lost their pinned inputs; `quality/coldread-precheck-red-c7586b9.stdout`).
- Mined mistake + fix (attempt 3): `quality/coldread-precheck.sh` (red at `c7586b9a` exit 1, ok at freeze exit 0) and QUALITY criterion 98 (`corpus/QUALITY.md`, round-48 block); lesson section `## Attempt 3` in `corpus/lessons/round-48.md` (erratum for the S267/S268 line pointers, the mistake row, the deciding-rule process defect, spot-check routing).
- Record checks at the tip `e438777e`: QUALITY round-48 block `pointer-check.py` → `checked=15 missing=0`, exit 0 (criterion 97; `quality/pointer-check-tip-a3.stdout`); lesson `## Attempt 3` → `checked=20 missing=1`, the one MISSING being `after/c1.exit`, cited deliberately as absent (`quality/pointer-check-lesson-a3.stdout`). Criterion 95's falsifier block reads the attempt-2 receipt and stays `VACUOUS` there (`quality/c94-96-falsifiers.stdout`); the conditions it checks (CTL_B total>0, CTL_E total=0) hold in `control/c1-controls-a3.stdout`. Cold-read at the tip: `cand_credited=57 lost=3 RED` (no further drop from attempt-3 edits).
- Round-47 spot-check routing: correction C1-R48-1/2 and criteria 94-97 (attempts 1-2); the two untraced items (located-name check, append-only seat reports; `a2w1/T48A2RevSpotcheckR47.md` F1/F2) carried into `Planned (round 49)` in SCORECARD.
- Swarm: wave `w1` (attempt 1, v1, 32 seats) and wave `a2w1` (attempt 2, v2, 64 seats); attempt 3 dispatched no wave (frozen claims, data already gathered). Seat reports: `.ufo/waves/round-48/w1/`, `.ufo/waves/round-48/a2w1/`.

## Landed changes

| Commit | What | LOG.md entry |
|---|---|---|
| `e73389c0` | pre-registration contract, census start | round 48 (`LOG.md` 2026-10-26 round 48) |
| `f1cfaad3` | amendments 1-3, wave-1 spec and dispatch | same |
| `7552984` | counter freeze, selftests, controls harnesses, deciding script | same |
| `5054532` | C2 rows S265-S268, snapshots, receipts, entries, lesson draft | same |
| `15b1521e` | orchestrator salvage of attempt 1 (not a landing) | same, corrected by the attempt-2 entry |
| `c7586b9a` | content revision: C1 standing rows, SCORECARD round-48 block, QUALITY 97, lesson integration | round 48, attempt 2 |
| `17cc5ce1` | `a2w1` spec and dispatch | round 48, attempt 2 |
| `8f2922b8` | orchestrator salvage of attempt-2 receipts and `a2w1` (not a landing) | round 48, attempt 3 |
| `c6295cb0` | C1 deciding receipt, cold-read precheck and receipts, control driver | round 48, attempt 3 |
| `e438777e` | C1 control receipts CTL_B-E, SCORECARD deciding section, QUALITY 98, lesson `## Attempt 3`, LOG entry | round 48, attempt 3 |
| `98e63044` | end receipts: census end, pointer-checks at the tip | round 48, attempt 3 |

## Before → after measurements

- **C1** — `python3 .ufo/evidence/round-48/calibration/measure.py --lane LANE --rev REV --base 473336d9d789f6081195e7376d17836a24666bc3 --work EMPTY_DIR`. Before (base tree, CTL_A at freeze bytes): `total=22 unparsed=22 C1_R48_PASS=false` (`control/c1-controls.stdout`). After (REV `c7586b9a`): `self_pin=1 stmts_pin=1 statements=22 rounds=3 append_only=1 unpinned=0 total=0 … fleet_drift=0 … C1_R48_PASS=true` (`after/c1-a3.stdout:96`).
- **C2** — `python3 .ufo/evidence/round-48/freshness/measure.py --lane LANE --rev REV`. Before (base, CTL_F): `refreshed=0` (`control/c2-controls.stdout`). After (REV `c7586b9a`, live): `self_pin=1 targets=4 refreshed=4 census_exit=0 live=on C2_R48_PASS=true` (`after/c2.stdout:5`).
- **Census** — `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`: start exit 0 (`.ufo/evidence/round-48/census-start.exit`), end exit 0 at `e438777e` (`.ufo/evidence/round-48/census-end-a3.exit`; last line `tameshi ok …/corpus/SOURCES.md`).

### Verdicts

- **C1: measured true, procedurally contestable.** The counter prints `C1_R48_PASS=true` at the content revision. Amendment 8 says "a second deciding invocation of either counter at the content revision is a miss"; attempt 2's invocation was killed during C1 and printed nothing (zero-byte `after/c1.stdout`, no `after/c1.exit`), so no value was seen and none selected, but under the literal rule attempt 3's run is a second invocation. Both readings are stated; the closure rules. Calibration score stays 6 (no raise claimed).
- **C2: measured true, not admissible as a pure improvement.** The counter prints `C2_R48_PASS=true`, but its record edits turned a pre-registered no-harm monitor red (cold-read credited sections 60 → 57). Under the admission rule a trade is not an improvement: C2 is reported as **harmed (trade)**. Freshness score stays 9.

## Sources & frontier

- Rows: 124 → 128 (`git show REV:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3,} \|'`: base 124, `c7586b9a` 128). Added by tier: A 3 (S265, S266, S267), B 1 (S268). Rows touched old→new: none (supersession by new rows; S026/S048/S093/S108 bytes unchanged). Frontier advanced: four held rows re-anchored with receipts; the round-45 S048/S093 quote disputes answered by phrase-bearing quotes.
- Census start exit 0 (`.ufo/evidence/round-48/census-start.exit`); end exit 0 (`.ufo/evidence/round-48/census-end-a3.exit`, at `e438777e`; rows 128).
- Sourced claim: C2 (S265-S268 opened 2026-10-26).
- Mined mistake: `corpus/lessons/round-48.md` `## Mistakes` (rows from attempts 1-2) and `## Attempt 3` (cold-read trade; fix shown able to fail).
- Assimilation: none — every staged `merge/tameshi/` row touching the four C2 documents is already held or adopted (`.ufo/waves/round-48/w1/T48ScoutPackage.md`); the Gate records the rejects.
- considerthese: `considerthese/2026-10-25.md` idea 5 mined (lesson `## considerthese`); `considerthese/2026-10-26.md` arrived mid-round (`41c1bc0`) and is left for round 49.

## Trend verdicts

- **expansion: unchanged** — the four new rows supersede held documents; no new coverage-map ground.
- **quality: harmed** — held-row anchors improved (C2), but the cold-read monitor lost three credited sections (60 → 57) as a direct cost; a trade is not an improvement.
- **discernment: improved** — the 22 standing statements now carry a value class backed by three observation rounds and confirmed by the counter at the content revision (C1 `total=0`), where round 47's one-shot row was refuted (`total=2`); subject to the C1 procedural ruling above.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `reports/round-1-calibration.md#box-1` (lane assertion; no independent verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `reports/round-1-calibration.md#box-2`
- [~] Instructions executable by an agent without oral context — `.ufo/evidence/round-21/coldread/ledger.json` (input-keyed monitor; 57/64 sections credited at `c7586b9a`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `reports/round-1-calibration.md#box-4`

## Round shape, seats, hygiene

- Shape: two waves across attempts — `w1` (v1, 32 seats: executor 11, critic 4, scribe 4, scout 4, reviewer 3, revenger 2, connector 2, mutation-tester 1, sentinel 1) and `a2w1` (v2, 64 seats: executor 19, reviewer 12, critic 11, mutation-tester 6, scout 4, connector 4, revenger 3, scribe 3, sentinel 2). Round total 96; no residual call. The §3 planner seat is held by the L1.
- Dead seats: `w1` 7 with no output (T48ExecObs1, T48ExecObs3, T48CritC2Design, T48CritMistakeFix, T48RevC1Predicate, T48RevC2Predicate, T48MutC1Core — host crash; `a2w1/T48A2ScoutDeadSeats.md`); `a2w1` 4 cancelled by the orchestrator at wrap-up (T48W2ExecC1ProbeD, T48W2CritC1Controls, T48A2ExecC1SerialB, T48A2ExecC1SerialD; `a2w1-results.json`).
- Inherited state: both salvage commits re-verified (frozen bytes re-hashed; deciding receipts read); reused: all of `after/` except the empty `c1.stdout` (kept as evidence of the killed run). Discarded: none.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → ` M scripts/hyaku/inline-dispatcher.py` only (orchestrator-owned, not a seat file); no misroot.
- Scratch: `/fast/scratch/hyaku/tameshi-r48` removed after landing.
- Tool installs: none.
- Open L0 questions: none filed.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
