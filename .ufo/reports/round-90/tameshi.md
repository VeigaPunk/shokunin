# tameshi — round 90 report (attempt 1, L1 TameshiR90)

Lane HEAD (pushed): `ec8d2a6ea2296310a801283a8f10df5a9b033bc4` (`git ls-remote origin refs/heads/master`).
Fresh start under Amendments 46/47 (post-fresh rejections r88, r89). Round shape: one v1 wave `r90-w1`, 14 seats, no residual call. Round total: 14.

## Work performed

Declared claims (frozen at `3485ceb0`, `plans/round-90.plan.md`): **R90-C1 — coverage** (sourced: S316, S317): a reproducible mutation case on the fleet's own registry gate `scripts/sources-census.sh` @ `f47ad6ba`, re-executed by an independent counter; **R90-C2 — calibration** (lowest non-retired axis): the round-89 closure's routed record defects 1-4 closed over committed bytes. Both predicates are met at landing; **both are killed by their own frozen kill rule (a)** — honest stop.

- Fresh-start reads: round-87/88/89 closures and spot-checks; the shared root (an instrument certifying a subject, passed by a counterfeit) is named in `plans/round-90.plan.md` § Fresh-start reads and `corpus/lessons/round-90.md` § Fresh-start reads.
- Pre-registration: predictions and control expectations committed ALONE first (`33dd6e47`), amendment alone before any control receipt (`dd0ddce9`) — T90R2 confirmed both (`.ufo/waves/round-90/w1/T90R2.md:15-21`).
- C1 instrument: `.ufo/evidence/round-90/c1/measure.py` (sha256 `d7365bbb…b528`) materializes the pinned gate and fixtures from the fleet object store, runs its own `selftest` per mutant twice, a canary, validity/trivial checks and a witness registry per mutant; 16 committed control states (`pre-freeze/controls/CTL*.out`, `C1-summary.txt`): positive control PASS, every forgery refused by its named conjunct.
- C1 measurement: 12 mutants, 5 KILLED / 7 SURVIVED, 12/12 pre-registered predictions held, 7/7 survivors witnessed non-equivalent (`pre-freeze/controls/CTL1b-nowork-A.out`); reproduced 12/12 outside the counter in an ordinary shell (T90E1, `w1/T90E1.md`), invariant across six environments (T90L1, `w1/T90L1.md`).
- Domain work for the fleet (report-only, never pushed): seven survivor-killing selftest arms for the census gate, each proven in scratch (pristine green, survivor red, killed stay killed): `w1/T90E3-arms.patch`, `T90E3-prove.out`, `VERDICT: arms-kill-7/7`. Fleet impact (T90CN1, `w1/T90CN1.md:37-45`): survivor C12 (dropped per-path `trim_cell`) would add 1695 false E11 findings and turn 20 lanes' census red while `selftest ok` still prints; C03 15 lanes; C10 2 lanes.
- C1 landing `bc2c85a6`: case note `corpus/knowledge/mutation-case-fleet-sources-census.md`, S316/S317, coverage-map row (`corpus/README.md` § Round 90 — coverage map: the fleet's own registry gate), PROVINCE Core append. Counter: `C1_R90_PASS=true` (`.ufo/evidence/round-90/landing/c1-at-bc2c85a6.out`).
- C1 kill: T90R1 K2 — counter git reads honour `refs/replace`, so a committed note with a false C02 verdict prints PASS under a local replace ref (`w1/T90R1-probe-defects.out` V4-replace-env vs V4-replace-sealed); K1 — an id-keyed row with two verdict tokens is skipped silently (V1-dup-row). T90C1's prediction-copy objection (`w1/T90C1.md` §2) is recorded as disputed: that state holds the true verdicts, so rule (a) does not fire by its letter.
- C2 instrument: manifest `tools/defect-bind-r90.json` v2 (5 rows) + `.ufo/evidence/round-90/c2/measure-c2.sh`; v1 failed its own positive control before the freeze and was repaired (lesson M1; `pre-freeze/controls/superseded-manifest-v1/`).
- C2 landing `9b5dde78` (append-only repairs: README coverage-map row and entry citation for `kernel-witnessed-ledger.md`, round-89 lesson corrections, SKILL and `tools/registry.json` rows for `tools/ledger-witness.py`, marked not admitted). Counter: `C2_R90_PASS=true` (`landing/c2-at-9b5dde78.out`). T90R2: all four routed items actually repaired.
- C2 kill: T90C2 K1 — a registry row whose argv only `print`s the needle holds and passes the frozen counter (`w1/T90C2-forge-registry.out`); K2 — a correction asserting the wrong count passes (`T90C2-wrong-count.out`); K3 — neutered checker tools pass (`T90C2-tool-neuter.out`).
- Counter battery strength (T90M1, `w1/T90M1.md:53-72`): 9/20 single-edit weakenings of the C1 counter killed by the 16 controls; four survivors reachable by a committed state (lesson M8).
- Safety audit (T90SN1, `w1/T90SN1.md`): 11 findings in the round's drivers (F1 unvalidated `--target`, F2 receipt truncation on re-run, F3 empty path → cwd); routed.
- No-harm (C2 rule b): T90E2 base/freeze/freeze+fixes (`w1/T90E2.md:44-51`) and the L1 at `ff31f72a` (`landing/noharm-ff31f72a.txt`): selfstate `26/24/2/0`, pins `26/26`, registry-figure `9/9`, pointers `12/12` — unchanged.

## Landed changes

Lane `tameshi-shokunin` (all through `jj-lane.sh`, each printed `landed <hash>`):

| Commit | Content | LOG.md entry |
|---|---|---|
| `33dd6e47` | C1 spec + pre-registered predictions + census start receipt (alone) | § Round 90 |
| `dd0ddce9` | expectations amendment 1 (alone) | § Round 90 |
| `a90218cc` | pre-freeze instruments (C1 counter + controls driver, C2 manifest v1 + counter) | § Round 90 |
| `3cf905bc` | C1 control receipts; C2 manifest v2, fixes generator, controls driver | § Round 90 |
| `a4797ebe` | C2 v2 control receipts | § Round 90 |
| `3485ceb0` | freeze: `plans/round-90.plan.md` | § Round 90 |
| `0e5a39ed` | wave `r90-w1` spec + validated dispatch | § Round 90 |
| `9b5dde78` | C2 record repairs (routed r89 items 1-4) | § Round 90 |
| `bc2c85a6` | C1 landing: case note, S316/S317, coverage-map row, PROVINCE Core append | § Round 90 |
| `ff31f72a` | lesson, QUALITY 139-142, SCORECARD § Round 90, LOG § Round 90, landing receipts | § Round 90 |
| `ccea99a6` | lesson addenda (gnu.org correction, M8), no-harm receipt | § Round 90 |
| `ec8d2a6e` | wave `r90-w1` seat deliverables + results | § Round 90 |

## Before → after measurements

| Claim | Counting command | Before (rev) | After (rev) | Verdict |
|---|---|---|---|---|
| R90-C1 coverage | `python3 -I .ufo/evidence/round-90/c1/measure.py --repo <lane> --rev REV --work <empty>` | `4e1c10e0`: `C1_SETUP spec-absent-at-rev`, exit 2; `33dd6e47`: `note=false … C1_R90_PASS=false`, exit 1 | `bc2c85a6`: `n=12 killed=5 survived=7 … witnessed=7/7 note=present mismatched=0`, all conjuncts true, `C1_R90_PASS=true`, exit 0 | predicate met; killed by rule (a) (T90R1 K2, K1); not admitted |
| R90-C2 calibration | `bash .ufo/evidence/round-90/c2/measure-c2.sh <lane> REV <empty> [MANIFEST_SRC]` | `4e1c10e0` (manifest from `3cf905bc`): `rows=fail registry=fail`, `C2_R90_PASS=false`, exit 1 | `9b5dde78`: `rows=ok registry=held`, `C2_R90_PASS=true`, exit 0 | predicate met; killed by rule (a) (T90C2 K1, K2, K3); not admitted |

Scores unchanged: depth 10, calibration 8, freshness 9 (`SCORECARD.md` § Round 90).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi` — start exit 0 (`.ufo/evidence/round-90/pre-freeze/census-start.txt`), end exit 0 (`.ufo/evidence/round-90/landing/census-end.txt`). Defect noted: at the intermediate commit `bc2c85a6` the census printed E11 (S316/S317 `used-by` named the not-yet-written lesson; lesson M6), repaired by `ff31f72a`.
- Rows (`grep -c '^| S[0-9]' corpus/SOURCES.md`): 175 → 177. Added by tier: A ×2 — S316 gawk(1) `sub()` replacement `&` (mined), S317 bash(1) `-e`/`-f` (mined), both opened by the L1 this round (snapshots `.ufo/evidence/round-90/sources/`). Rows touched old→new: none.
- Rejected/not appended: the www.gnu.org manual pages (the L1's connections failed, `sources/gnu-unreachable.txt`; T90S2 reached them during the same window — reason narrowed, lesson Gate addendum); T90S2's three proposed rows (redundant; placeholder ids collided) and T90S1's three gawk-manual rows (fetched through a public relay, not first-hand; lesson Gate addendum).
- Frontier advanced: the first fleet-root gate measured (case 12), placed in the coverage map and PROVINCE Core.
- Sourced claim: R90-C1's note cites S316 and S317 (opened this round).
- Mistakes mined: M1-M8 in `corpus/lessons/round-90.md` `## Mistakes` (+ addendum); QUALITY 139-142, each with a committed state that shows the check can fail.
- Assimilation: none (no staged `merge/tameshi/` theme serves a fleet-gate mutation case). considerthese `2026-11-05.md` idea 4 (survivor table) applied to one gate.
- Round-89 spot-check: routed items 1-4 repaired (`9b5dde78`); item 5 carried (`corpus/lessons/round-90.md` § Routed).
- Misroot sweep (`git status --porcelain` on the fleet root): no files from this round's seats.

## Trend verdicts

- **expansion: improved** — one entry on ground the lane did not hold (the fleet's own registry gate), citing two mined rows opened this round, with a coverage-map row and a PROVINCE Core append (`bc2c85a6`). Its verdict table is independent of the killed counter: reproduced by T90E1 outside the counter.
- **quality: improved** — the held round-89 entry gained its missing coverage-map row and the round-89 lesson's count and wording defects were corrected by append; T90R2 judged all four routed items actually repaired (`w1/T90R2.md` § 3).
- **discernment: improved** — the wave killed both claims; the kills became QUALITY 139-142 with committed failing states (T90R1 V1/V4, T90C2 forge/wrong-count, v1 C2-pos), and the control-battery gap is measured (T90M1 9/20).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `tameshi-shokunin/SKILL.md` (§ Gate registry — round 90 appended)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `tameshi-shokunin/LOG.md` § Round 90 (mutation case on the fleet census gate)
- [~] Instructions executable by an agent without oral context — `tameshi-shokunin/.ufo/evidence/round-21/coldread/ledger.json`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `tameshi-shokunin/PROVINCE.md` § Core — round 90 append

## Round extras

- Wave: `r90-w1`, 14 seats — executor 4 (T90E1, T90E2, T90E3, T90L1 labrat-class probe), scribe 1, scout 2, reviewer 2, critic 2, mutation-tester 1, connector 1, sentinel 1; attack share 5/14. Dead seats: 0 (14/14 settled with deliverables) (`.ufo/waves/round-90/r90-w1-results.json`). Planner seat: held by the L1 (validator rejects `planner`; `labrat` is not a swarm role, so the probe rode an executor).
- Upstream (report-only, never pushed): `tameshi-shokunin/.ufo/waves/round-90/w1/T90E3-arms.patch` — seven selftest arms for fleet `scripts/sources-census.sh`, C12 first (guards the fleet's multi-path `used-by` convention on 20 lanes).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. pacman untouched.
- Open L0 questions: none.
