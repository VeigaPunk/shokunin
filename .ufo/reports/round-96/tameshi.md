# tameshi round 96 — the sealed revision identity (calibration) and the hardened write path (operability)

Lane `tameshi` (verification-fixture craft), round 96, attempt 1. Base
`c8de77f3de0fd4bf619ebe78fa0b28adaf320d3e`; lane tip after this round
`d8f135d24361fd31870a8d47caa6e2212e70fb1b` (branch `master`). Report filed by
`fleet-commit.sh --as tameshi`.

**Declared claims (2).** R96-C1 targets **calibration**: the disposition audit binds its
verdict to a commit identity — the revision is checked as 40 hex, resolved to a commit,
printed, and refused before any read when it is a ref, a shorthand, an empty string or an
unresolvable id — and its git calls run under an explicit environment with a pinned `PATH`
and an absolute `git`, so a hostile `git` earlier in the inherited `PATH` cannot answer for
it. R96-C2 targets **operability**: the pins tool refuses an empty, relative or
toplevel-mismatched lane and a symlink at its destination, writes atomically, and the
battery driver grades the receipt it wrote (never a planted index-0 file), validates the
`counter_sha=` line it grades, and refuses a symlinked `--outdir`/`--work`.

Both claims answer the round-95 sentinel's live findings F1-F8 (`w1/R95SN1.md` of round 95)
and were frozen before any scored receipt: `plans/round-96.plan.md` §Claims and
`.ufo/waves/round-96/claims.json` at `de6db8c9`. **The round's own wave falsified nine of
their atomic assertions before any receipt existed**; each was amended pre-data (A1-A9,
`plans/round-96.plan.md` §Amendments) with its artifact cited. No target moved and no
predicate was narrowed after data.

## Work performed

- **Protocol load.** `skill://shokunin`, `kimi-shokunin/skills/shokunin/SKILL.md`,
  `protocol/` PROTOCOL, MISSION.md, AXES.md, CORPUS.md, LEARNING.md, `skill://swarm`,
  `skill://godspeed`; lane SKILL.md, PROVINCE.md, SCORECARD.md (its `planned` row),
  `corpus/QUALITY.md`, `corpus/README.md` `## Frontier`, the newest lessons, the
  round-95 non-author spot-check (`corpus/lessons/round-95-verifier-spotcheck.md`, D1-D5),
  and `.ufo/waves/defect-autopsy/tameshi.md`.
- **C1 instrument and its seal.** `.ufo/evidence/round-96/conjunct-disposition-v96.py`
  (sha256 `02a5482a…`): `--rev` checked as 40 hex, resolved with
  `rev-parse --verify --quiet --end-of-options <rev>^{commit}`, printed as `rev=` in
  `DISPOSITION_INSTRUMENT`, empty and branch values refused `rev-not-a-commit-id`, dead ids
  `rev-unresolvable`; `sealed_env()` is explicit (`PATH` pinned, `HOME`/`TMPDIR` under
  scratch), `GIT = "/usr/bin/git"`, `refs/replace` refused at setup, and the manifest blob
  is bound to `claims.json`'s `manifest_sha256` (`manifest-sha-mismatch`). Selftest 13/13,
  and its two new cases now run the real main path (poisoned `PATH`; `--rev master`).
- **C2 tooling.** `.ufo/evidence/round-96/c1/make-pins96.py` (sha256 `544166e1…`): refuses
  `lane-empty`, `lane-not-absolute`, `rev-not-a-commit-id`, a toplevel mismatch, a symlink
  at `pins.json` (`pins-symlink-refused`) and at its temp name (`tmp-symlink-refused`), and
  writes `tmp-pins` → `fsync` → `os.replace`; `git` resolved absolutely.
  `.ufo/evidence/round-96/c1/controls-v96.py` (sha256 `88bcca86…`): resolves each clone's
  `HEAD` to a 40-hex id, refuses a symlinked `--outdir`/`--work`, records the path it wrote
  and grades **that** path, requiring a `counter_sha=<64 hex>` line on what it grades.
- **The battery.** 50 states at the records revision: `C1_CONTROLS states=50 matched=50
  mismatches=0 missing=0`
  (`.ufo/evidence/round-96/pre-freeze/controls/C1-summary.txt`), every receipt carrying a
  `counter_sha=` line.
- **Frontier step (§2b).** S320-S323 re-opened this round with fresh fetch headers and
  located quotes (`w1/R96S1.md`, `w1/R96S1-quotes.txt`, `w1/R96S1-census.txt`); one source
  **refused** with a measured reason and a flip condition (GitHub REST "Get a commit" —
  a hosted-API statement, not the `<rev>` grammar; `w1/R96S1.md` §4). One mistake class
  mined into `## Mistakes` (M4, renderer drift), and the round-95 spot-check's D1 is closed
  in the registry: the S323 `anchor` cell moves `2355` → `2358` with the renderer named.
  Census before and after both exit 0, rows 183 / mined 149 / queued 23 / rejected 11.
- **Wave `w1`, one v1 wave, 13 seats** (`.ufo/waves/round-96/w1-spec.json`, dispatch
  `.ufo/waves/round-96/w1-dispatch.json`, `counts.total=13`): executor 4 (R96E1-E4),
  scribe 1 (R96SC1), scout 1 (R96S1), reviewer 2 (R96R1, R96R2), critic 1 (R96C1),
  mutation-tester 1 (R96M1), sentinel 1 (R96SN1), connector 1 (R96CN1), revenger 1 (R96L1).
  Attack share 4/13 = 31 % by the addendum §6 named set (reviewer×2, critic,
  mutation-tester), 7/13 = 54 % including sentinel, connector and revenger. **All 13 seats
  settled** (orchestrator `WAVE-DONE tameshi r96 w1`; `.ufo/waves/round-96/w1-results.json`
  carries 13 results) and all 13 landed a report in `.ufo/waves/round-96/w1/`. R96SC1
  delivered five drafts (`SC1-lesson.md`, `SC1-sources.append.md`, `SC1-quality.md`,
  `SC1-log.md`, `R96SC1.md`); its two record repairs are integrated (below). R96L1 landed
  late (≈10:45, after the L1's 10:39 absence record) with `R96L1.md` + `R96L1-runs/` and a
  `partly refuted` verdict that independently reproduces A1/A2/A6: the guards are inert on
  the twelve `C1_ROW` cells and the 19-row disposition, but a guard-only variant of the
  round-95 bytes turns the battery into `matched=44 mismatches=6 [D01-D05, replace-honest]`
  — the `--rev HEAD` class A6 fixed. The L1 holds the planner seat (§3 mapping); no planner
  seat was dispatched.
- **Wave accounting handoff.** The dispatcher stalled: its log's last pre-WAVE-DONE entry
  is `2026-11-08T10:30:11 closure CloseTsukuroiR98` and there is no `done tameshi w1` line
  before the handoff. At 10:39 -03, with twelve reports on disk, the L1 wrote
  `.ufo/waves/round-96/w1-results.json` itself (`"_source": "l1-constructed"`) and recorded
  the revenger seat as dead. That call was **wrong**: the seat landed at ≈10:45, the
  orchestrator then delivered `WAVE-DONE tameshi r96 w1` and its own 13-result
  `w1-results.json` (which replaced the constructed file), and the absence record now opens
  with its correction (`w1/R96L1-absent.md`; lesson M5). The round is filed on the
  orchestrator's handoff, not on the L1's guess.
- **Adversarial outcome.** R96R1 falsified two C1 sentences (`FALSIFIES-WORDING ×2`: the
  checker's default `COUNTER` still named round 95's file; `rev-unresolvable` was dead code
  because a bare `rev-parse` echoes any 40-hex with rc 0). R96C1 falsified five atomic
  assertions (the unprinted revision, the no-op selftest cases, the before-rev citation,
  the `--rev ''` token, the vacuous "findings=0 honest" clause) and confirmed five. R96SN1
  measured ten findings — F1 counter-sha hand-writing (declared limit), F2 alternates, F3
  pins `git` by name, F4 planted index-0 receipt, F5 the driver's `--rev HEAD` break, F6/F7
  rev tokens, F8 the counter path, F9 outdir symlink, F10 unpinned manifest, F11 the
  "instrument revision" wording. R96E4 independently measured `44/50` (the `--rev HEAD`
  break) before A6 and the records run then measured 50/50. R96M1 ran a 41-row mutation
  matrix: `defects=41 killed=28 survived=13 inconclusive=0`, with the two new seal guards
  killed by their own states and no round-95 survivor left live. R96R2 measured all five C2
  sentences **holding** after A6-A9. R96L1 `partly refuted` the guard-inertness hypothesis
  and reproduced A1/A2/A6 from an independent guard-only construction. All findings were
  amended pre-data or declared as limits; nothing was smoothed.
- **Pre-file falsification ledger.** `.ufo/waves/round-96/claim-falsification.tsv`, 11 rows,
  both claims, all seven attack seats present; two `falsifies-wording` and one
  `falsifies-number` row point at amendments A1/A2/A3/A5/A6/A7/A9, and one row cites the
  dead-seat record. Gate: `PREFILE-FALSIFICATION: pass claims=2 rows=11 attack_seats=7
  findings=0`, exit 0
  (`python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane
  tameshi --round 96`); selftest `PREFILE-FALSIFICATION-SELFTEST: PASS`.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Plan + instruments copy + source snapshots + census before | Round 96 §Shape | `10d8fa5d52c0674038beb2eb2328e42162bb4b56` |
| Claims freeze C1/C2 (wording, shas, kill rules) | Round 96 §Shape | `be6c22b6d8a94f07eee6b0fa79edab7df228c0b0` |
| Wave `w1` spec (13 seats) + dispatch + ready file | Round 96 §Shape | `de6db8c92f2997e5fafbf5c4c760a48adb8898ff` |
| Pre-data amendments A1-A8 (seal repairs) + wave seat reports | Round 96 §Motivating evidence | `933df6765a921d5480bd7cac8fbaf8de699f0e39` |
| A9 driver grades its own receipts; 50/50 battery receipts; claims shas | Round 96 §R96-C2 | `8ed9c5262bd2f36f3cc8a64550897f4d1adb3a3b` |
| Landing receipts (C1 positive, rev refusals, hostile-PATH, forge 8/8; C2 pins/rank/outdir; nowork; selftest) + QUALITY 173-174 + LOG entry | Round 96 §R96-C1/§R96-C2 | `9b89c68d8ad63a82b5873ca1ec7a3cebbe8aa2e9` |
| Lesson + SCORECARD r96 + capability row + census after | Round 96 (whole entry) | `ffb41c8f8a6018a71c7c9ee932010438c01af944` |
| D1 closed (S323 anchor), Gate spans, falsification ledger | Round 96 §Frontier | `1aaf9d20e6264fe83395a93cfc4d09f1f1032ddc` |
| M4 renderer-drift row; SC1's two record repairs; L1-constructed wave accounting | Round 96 §R96-C2 | `cdc7f1b2675e5267d27e1fcc032bd8eaa3eefd3e` |
| `R96L1-absent.md` dead-seat record + ledger row; prefile gate pass | Round 96 §Shape | `b9783abbdb1f90798c3646c396940958e2c861bf` |
| `.ufo/evidence/round-96/c2-forge.py` committed as wave evidence | Round 96 §R96-C1 after | `07e50d6d0142b21e8443b5417b8edc4d1dd76455` |
| WAVE-DONE received; R96L1 record corrected, ledger repointed, M5 row | Round 96 §Shape | `d8f135d24361fd31870a8d47caa6e2212e70fb1b` |

LOG.md entry: `## Round 96 (2026-11-08) — two claims: the sealed audit's revision identity
(calibration) and the hardened write path (operability)`. QUALITY 173-174 appended;
SCORECARD round-96 record + the `revision-identity seal` capability row appended.

## Before → after measurements

### R96-C1 (calibration) — verified under the amended wording (A1-A5)

Counting command:

    python3 -I .ufo/evidence/round-96/conjunct-disposition-v96.py --lane /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev 8ed9c5262bd2f36f3cc8a64550897f4d1adb3a3b --min-falsifiable 17

Before: at base `c8de77f3` the successor checker does not exist —
`DISPOSITION_SETUP counter-absent-at-rev`, exit 2
(`.ufo/evidence/round-96/landing/c2-nowork-base.out`). The round-95 checker accepted a
movable revspec and a hostile `git` (`w1/R96C1.md` C1.10, `w1/R96R1.md` before-witness).

After: `DISPOSITION_INSTRUMENT rev=8ed9c5262bd2f36f3cc8a64550897f4d1adb3a3b
sha256=69ee68b6… conjuncts=19` and
`DISPOSITION rows=19 falsifiable=17 unfalsifiable=2 findings=0`, exit 0
(`landing/c1-positive.out`). Refusals: `landing/c1-rev-branch.out` (`--rev master`) and
`landing/c1-rev-empty.out` (`--rev ''`) print `DISPOSITION_SETUP rev-not-a-commit-id` exit
2; `landing/c1-rev-unresolvable.out` prints `DISPOSITION_SETUP rev-unresolvable` exit 2.
Hostile `PATH`: `landing/c1-hostile-path.out` prints 17 `receipt-absent-at-rev` findings,
`DISPOSITION rows=19 … findings=17`, exit 1 — never green, and the shim never answered.
Forge matrix `landing/forge-matrix.txt`: `summary: 8 checks, 0 failed` (hand-written receipt
exit 1 `receipt-absent-at-rev`; wrong `counter_sha=` exit 1
`receipt-counter-sha-mismatch`; `refs/replace` exit 2 `replace-refs-present`; the round-95
checker printed `findings=0` exit 0 on all three). Selftest
`landing/c2-selftest.out`: `DISPOSITION_SELFTEST: 13/13 pass`, exit 0.

Measured commit: `8ed9c5262bd2f36f3cc8a64550897f4d1adb3a3b` (records revision: instruments,
manifest and 50 receipts committed together). The do-nothing control (`c2-nowork-base`)
does not meet the target.

### R96-C2 (operability) — verified under the amended wording (A6-A9)

Counting commands:

    python3 -I .ufo/evidence/round-96/c1/make-pins96.py --lane <lane> --rev <REV> [--check]
    python3 -I .ufo/evidence/round-96/c1/controls-v96.py --lane <lane> --rev 8ed9c526… --base c8de77f3… --work <empty dir> --outdir <dir> --jobs 8

Before: at base the successor tool does not exist; the round-95 `make-pins95.py` wrote into
the CWD on `--lane ''` and through a symlink at `pins.json`, exit 0, and the round-95 driver
graded a planted `.rerun-9.out` and followed a symlinked receipt (`w1/R96R2.md`,
`w1/R96E2.md`, `w1/R96SN1.md` F4/F5/F9).

After: `landing/c2-pins-positive.out` prints `PINS_WRITTEN …/pins.json` and `PINS_CHECK OK`;
`landing/c2-pins-empty-lane.out` prints `PINS_SETUP lane-empty` exit 2, writing nothing;
`landing/c2-pins-symlink.out` prints `PINS_SETUP pins-symlink-refused` exit 2 with
`target_before == target_after == 9660b330…`; `landing/c2-rerun-plant.out` prints
`pos-real MATCH exit=0`, `C1_CONTROLS states=1 matched=1 mismatches=0 missing=0` while the
planted receipt (`w1/R96R2-out-rerun9-planted.out`, `counter_sha=000000…0`, `exit=1`) sat
beside the driver's own write; `landing/c2-outdir-symlink.out` prints
`outdir-symlink-refused`. Battery at the records revision: `C1_CONTROLS states=50 matched=50
mismatches=0 missing=0`, exit 0
(`.ufo/evidence/round-96/pre-freeze/controls/C1-summary.txt`).

Measured commit: `8ed9c5262bd2f36f3cc8a64550897f4d1adb3a3b` (receipts), instruments at
`933df676`. The do-nothing control for the battery is the pre-A6 run at `44/50`
(`w1/R96E4.md`), which does not meet the target.

## Sources & frontier

`SOURCES.md` rows before → after, counting command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`:

- before: exit 0, rows 183 (A 165 · B 14 · C 4), status mined 149 · queued 23 · rejected 11
  (`.ufo/waves/round-96/census-before.txt`);
- after: exit 0, rows 183, mined 149 · queued 23 · rejected 11
  (`.ufo/waves/round-96/census-after.txt`).

Rows added by tier: **none** (no ground was opened that the lane did not already hold).
Rows re-opened this round: S320, S321, S322, S323 — fresh fetches with HTTP dates and
located quotes (`w1/R96S1.md` §1-2, `w1/R96S1-quotes.txt`); `used-by` had already gained
`corpus/lessons/round-96.md` at the freeze. Rows refused: **one** — GitHub REST "Get a
commit" (`w1/R96S1.md` §4), refused for the revision-identity ground with a flip condition.
Rows touched old → new: the S323 `anchor` cell `line 2355` → `line 2358` with the canonical
renderer named (commit `1aaf9d20`; census exit 0 after). Frontier rows advanced: none —
F1-F11 in `corpus/README.md` are unchanged; this round's new ground is in the lane's own
instrument line, not in a frontier row. Assimilation: **none** from
`/home/vgpnk/Projects/shokuknow` this round (no theme fits the seal/write-path work, and
CONSIDERTHESE has no unimplemented proposal bearing on it).

## Trend verdicts

- **expansion — unchanged.** No new domain surface and no frontier row moved: the round
  hardened two surfaces the lane already governed (its own audit and pins tool). The one
  source opened for admission was refused. Evidence: census rows 183 → 183;
  `corpus/README.md` `## Frontier` unchanged.
- **quality — improved.** Two instrument classes are now governed that were not: a verdict
  is bound to a resolved, printed commit id and to a pinned `PATH`/absolute `git`
  (`landing/c1-positive.out`, `landing/c1-hostile-path.out`, forge matrix 8/8), and a write
  path refuses empty/relative lanes, symlinked destinations and symlinked outdirs while
  grading only the receipt it wrote (`landing/c2-*.out`, battery 50/50). QUALITY 173-174
  record both as criteria with failing receipts.
- **discernment — improved.** The round's own wave falsified nine of its atomic assertions
  before any scored receipt, and every one was amended pre-data with its artifact cited
  rather than filed as written: R96R1 ×2 `FALSIFIES-WORDING`, R96C1 ×5, R96E4 a number
  (44/50), R96SN1 F4/F5/F9/F10/F11. SC1's independent re-measurement also caught two
  unbacked citations in the L1's own QUALITY 174 and lesson text, repaired at `cdc7f1b`.
  `corpus/lessons/round-96.md` M1-M5, including M5 — the L1's own premature dead-seat call,
  corrected when the seat landed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  — lane assertion; the round added QUALITY 173-174 as criteria, not SKILL.md prose; no
  independent promotion verifier (`corpus/QUALITY.md:2750-2790`).
- [~] At least one end-to-end domain task executed and logged in LOG.md
  — the round's two claims executed end to end and are logged (`LOG.md` Round 96);
  no independent promotion verifier.
- [~] Instructions executable by an agent without oral context
  — the instruments run from committed bytes with documented commands
  (`.ufo/evidence/round-96/landing/c1-positive.out`, `c2-pins-positive.out`);
  R96E1/E2/E3 reproduced them from receipts alone; no independent promotion verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  — the round touched only the lane's own instruments and corpus; the connector's sibling
  sweep found no duplicate implementation (`w1/R96CN1.md`); no independent promotion
  verifier.

**Stale-lane:** respawn-per-round driver; this report closes round 96 and no other mission of
this lane is open. No L0 question was opened this round. Tool installs: none (python3
3.14.8, git 2.56.0, curl 8.23.0 as installed); pacman untouched per the addendum guard.

## Filing record

Lane tip at filing: `d8f135d24361fd31870a8d47caa6e2212e70fb1b` (branch `master`,
`jj-lane.sh state` → `local=d8f135d2 remote=d8f135d2 ahead=0 behind=0`; `git ls-remote
origin refs/heads/master` prints the same). Pre-file gate:
`PREFILE-FALSIFICATION: pass claims=2 rows=11 attack_seats=7 findings=0`, exit 0
(`python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane
tameshi --round 96`); gate selftest `PREFILE-FALSIFICATION-SELFTEST: PASS`.
