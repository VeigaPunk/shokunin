# kagi — round 36 (attempt 2)

Lane: `kagi-shokunin` (secrets & vault ops; owned axes freshness + calibration). Round shape: **one v1 wave, 13 seats** (executor 3, scribe 2, scout 2, connector 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1; 5 attack seats = 38 %), validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16, `maxLanes` 256), dispatched through the inline handoff (`build.ready` → `build-dispatch.json`, 13 spawns, 0 resumes). Round total 13 seats; no residual call. Frozen BASE `cb8cb659e84240a8db12e4f7b4a0def5068baf7e`; frozen plan `09f27e2e16c26484b2675aa2a2b1e2ca4d3d1d8d`.

## Work performed

The round declared **two claims on two distinct axes** (`plans/round-36.md`): **C1 calibration** — SCORECARD self-assessment mismatches 4 → 0, measured by `bash plans/round-36-c1.sh` (SD5 red-id omissions + stale self-count declarations); **C2 freshness** — declared release clocks re-observed, drift 15 → 0, measured by `bash plans/round-36-c2.sh` (rows disagreeing with a committed live observation receipt). Both are causally separable: C1 reads only SCORECARD/self-counts bytes, C2 only `corpus/release-clocks.tsv` against the receipt. **Verdicts: C1 measured 4 → 0 with its frozen kill rules intact, but admission is withheld — a dispatched reviewer REJECTs the instrument as a proxy and demonstrates four executable shortcuts that reach 0 without the work (detailed below). C2 measured 15 → 0 and is admitted on its reviewer's conditions.**

- **BASE re-measured from the frozen bytes, independently.** A clean `git archive cb8cb65` extraction prints C1 `4`, C2 `15`, sweep `SD5=3 SD6=3`, `SELF_COUNTS: POLICY (claims=63 stale=1 …)` with `STALE SA-CAP-CENSUS-SELFTEST SCORECARD.md:701 claimed=59 live=70`. Evidence: `.ufo/waves/round-36/build/ExecBase/base.tsv`, `build/ExecBase/receipts/`.
- **The eight pre-freeze controls re-executed and reproduced byte-identically (8/8).** No-work 4 / 15; stale forgery (capability set to 71) 4; early-row SD5 forgery 4; C2 version forgery 16; empty-receipt 20; missing sweep and missing receipt `SETUP` exit 2. Evidence: `.ufo/waves/round-36/build/ExecControls/reproduction.tsv`.
- **C1 fixed at both populations.** This round's calibration row names `R25-02` (FAIL), `R29-01` and `R29-02` (POLICY) with their state, and the capability-table census count is bound to the live `70` (59 kept as the round-21 record). Evidence: `SCORECARD.md` §Round 36 post-move; `bash corpus/sources-census.sh --selftest` → `SOURCES_CENSUS_SELFTEST: PASS (70 cases)`.
- **C2 fixed at both the table and the pin.** The fifteen drifting `clock=feed` rows take the receipt's observed version, date and verdict; the fifteen non-drifting bound rows take the receipt's `observed_at` (required by `receipt_matches` and by the frozen operability kill rule); `DEFAULT_RECEIPT_SHA256` and `receipt_path` move to the round-36 receipt. Evidence: `corpus/release-clocks.tsv`, `corpus/release-clock.py:28,547,2105`.
- **Candidate rehearsed before landing, and the literal plan §Fix was shown insufficient.** Two seats and the L1 each measured that re-dating only the 15 drifting rows leaves `release-clock.py` at `RELEASE_CLOCK: FAILED` with 15 `RECEIPT-MISMATCH`; re-dating all 30 bound rows yields `CLEAN (observed=30 fired=15 derived=15)` with C2 still `0`. Evidence: `build/ExecRehearsal/report.md`, `build/MutCounter/report.md`, `build/ReviewC2/review.md`.
- **Five mutants killed, plus a fail-closed probe.** S014 reverted to `2.7.1/not-fired` → C2 `1`; `R29-02` deleted from the calibration row → C1 `1`; capability cell back to 59 → C1 `1`; receipt moved aside → `C2 SETUP` exit 2; `lane-status:` line deleted → `C1 SETUP: sweep verdict missing` exit 2 (never a zero). Unmutated control `0/0`. Evidence: `build/MutCounter/report.md`, `build/MutCounter/raw/`.
- **Connector sweep over all 20 sibling lanes: sole ground on all three surfaces** (the four feed URLs, the release-clock/receipt mechanism, the self-assessment-population instrument). Two siblings explicitly concede the ground (`kama` r82: "the pin-watch register capability is already kagi's"; `kotoba` r62 credits kagi with the `self-counts` technique class). Evidence: `build/ConnScope/ConnOverlap.md`.
- **Sources re-opened in-round with located quotes** (S034, S035, S040, S041; access date 2026-11-04, body sha256 per row, anchor-presence verdict per row), plus a credential-shape and execution-surface review of every byte the round would push. Evidence: `build/ScribeGate/gate.md`, `corpus/lessons/round-36.md` §Gate, `build/SentinelBound/review.md`.
- **Reconnaissance pinned the exact readers**: SD5 reads only the *last* `## Round` section's calibration row; `SA-CAP-CENSUS-SELFTEST` reads `SCORECARD.md` against ledger `R21-03`; `receipt_matches` compares each bound row's `observed_at` date with its record; `derived:` notes are pinned to their feed row's anchor cell. Evidence: `build/ScoutSweep/recon.md`, `build/ScoutClock/recon.md`.
- **Three stale prose citations of the old default receipt corrected** (`SKILL.md:48`, `SKILL.md:787`, `PROVINCE.md:75`), found by the clock scout rather than by any counter. Evidence: `git show 00bbe66 -- SKILL.md PROVINCE.md`.
- **Inherited attempt-1 state resolved and named**: its committed predeclaration controls were reused after re-execution; its uncommitted post-freeze instrument edit (jj keep ref `404a7b94`, not an ancestor of `master`) was discarded; its never-committed plan is committed here before any candidate scoring.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| C1 populations closed: round-36 calibration row names the three routed reds; capability count 59 → 70 | `LOG.md` §Round 36, bullets 2 and 6 | `00bbe667aead4096268785e80f5b7464bb511573` |
| C2: 15 drifting rows + 15 re-dated rows take the 2026-11-04 receipt; default receipt pin repointed | `LOG.md` §Round 36, bullet 3 | `00bbe667aead4096268785e80f5b7464bb511573` |
| `R36-01..R36-03` appended; `R13-01`, `R21-04`, `R24-06`, `R24-14`, `R25-04` migrated with old→new records; `SKILL.md`/`PROVINCE.md`/`corpus/README.md` counts rebound 79 → 82 | `LOG.md` §Round 36, bullet 6 | `00bbe667aead4096268785e80f5b7464bb511573` |
| `corpus/stamps.tsv` re-pinned (112 rows, same membership; also corrects the arming commit's un-re-pinned `corpus/self-counts.tsv`) | `LOG.md` §Round 36, bullet 7 (`corpus/lessons/round-36.md` M36-4) | `00bbe667aead4096268785e80f5b7464bb511573` |
| `corpus/lessons/round-36.md` (claims, gate, five mistakes, migrations, debt) and `plans/round-36-c3.sh` (the C2 operability reading) | `LOG.md` §Round 36, bullet 8 | `00bbe667aead4096268785e80f5b7464bb511573` |
| Plan and claims frozen before candidate scoring (`plans/round-36.md`, `plans/round-36.controls.tsv`) | `LOG.md` §Round 36, bullet 1 | `09f27e2e16c26484b2675aa2a2b1e2ca4d3d1d8d` |
| Frozen counters, armed population and eight executed predeclaration controls (attempt 1, re-verified this attempt) | `LOG.md` §Round 36, bullet 1 | `cb8cb659e84240a8db12e4f7b4a0def5068baf7e` |
| Wave evidence: spec, dispatch, ready marker, 13 seat results, 12 seat work products, final gate receipts, and the measured landing record | `LOG.md` §Round 36, bullet 5 | `4a32d2c99b02a842a36c612ab5315021116da287` |

## Before → after measurements

**C1 calibration** — counting command `bash plans/round-36-c1.sh` (one unsigned integer; `SETUP` exit 2 on any missing reading).
- BASE `4` at `cb8cb659e84240a8db12e4f7b4a0def5068baf7e` (clean extraction; `.ufo/waves/round-36/build/ExecBase/receipts/c1.out`).
- After `0` at `00bbe667aead4096268785e80f5b7464bb511573` (tree `229f37e11ed703935a4e1947dce1c667ff9b4d19`; `.ufo/waves/round-36/final/c1-at-landing.txt`).
- Decomposition: SD5 3 → 0, stale 1 → 0; SD6 unchanged at its BASE lane-tree value of 5 (non-owned verifier spot-check citations, none edited).

**C2 freshness** — counting command `bash plans/round-36-c2.sh` (one unsigned integer; `SETUP` exit 2 on a missing or malformed receipt).
- BASE `15` at `cb8cb659e84240a8db12e4f7b4a0def5068baf7e` (same extraction; `build/ExecBase/receipts/c2.out`).
- After `0` at `00bbe667aead4096268785e80f5b7464bb511573` (`.ufo/waves/round-36/final/c2-at-landing.txt`).
- Operability kill rule: `bash plans/round-36-c3.sh` → `RELEASE_CLOCK: CLEAN (on_release=30 bound=30 unbound=0 observed=30 fired=15 derived=15)`, exit 0, against the repointed default receipt.
- Re-confirmed at the pushed lane tip `4a32d2c99b02a842a36c612ab5315021116da287` (which adds only wave evidence and the lesson): `bash plans/round-36-c1.sh` → `0` rc0, `bash plans/round-36-c2.sh` → `0` rc0, `bash plans/round-36-c3.sh` → `RELEASE_CLOCK: CLEAN (…)` rc0, sweep `SELF_DESCRIPTION: MISMATCH n=5 (SD1=0 SD2=0 SD3=0 SD4=0 SD5=0 SD6=5 SD7=0 SD8=0 SD9=0)` — SD6 at its BASE lane-tree value, unchanged.

**Gate state at the landing tree** (all from `.ufo/waves/round-36/final/`): `sources-census.sh` `CLEAN rows=88 A=84 B=2 C=2 queued=1 mined=84 rejected=3 entries_sourced=14 legacy=21 captures=88`; `self-counts.py` `POLICY (claims=63 stale=0 unlocated=0 ambiguous=0 policy=2 setup=0)`; `claim-ledger.sh cells` `POLICY (cells=270 row_pointed=198 stamp_pointed=129 policy=2)`; `claim-ledger.sh verify` `POLICY (claims=82 policy=2 stamped=112)` with `R25-02` FAIL and `R29-01`/`R29-02` POLICY (all three operator-owned, all three present at BASE); `claim-ledger.sh citations` `BROKEN (cites=2349 docs=97 unresolved=5 …)` — the five non-owned SD6 citations, unchanged.

## Claim verdicts and admission

**C1 calibration — measured 4 → 0, admission withheld.** The frozen predicate, counter, target and kill rules are `plans/round-36.md` §C1 and none was changed after data. The counter prints `0` at the landing revision, `SD6` is unchanged at its BASE lane-tree value of 5, and none of the frozen forgery controls is read as zero. A dispatched reviewer nevertheless rejects the claim as an *instrument*:

- `.ufo/waves/round-36/build/ReviewC1/review.md` — verdict **REJECT**, with executed shortcuts: deleting the `lane-status:` id list **and** the armed self-counts row together reads `0` while the SCORECARD still asserts the stale count (`shortcutAB`); dropping `R25-02` from the `lane-status:` list reads `0` while `cells` still prints `FAIL R25-02` (`t5`); a false state (`R25-02 (PASS)`) reads `0` (`t6`); a `POLICY`-refused binding (`PV-FEEDTOKEN-SELFTEST` declared 9, live 4) is never compared and the counter reads `stale` from a producer that exits 2 (`t7`). SD5 checks token presence, never state, and never consults `cells`, so its reference set is self-declared.
- The candidate's *content* is independently correct: `bash corpus/claim-ledger.sh cells` at BASE names exactly `R25-02` FAIL and `R29-01`/`R29-02` POLICY, and ledger `R21-03` prints `SOURCES_CENSUS_SELFTEST: PASS (70 cases)`. Correctness of the row is not what the counter establishes.
- **Disposition: not admitted.** The lane does not rebook the rule after data. `ReviewC1`'s conditions are routed to round 37 and recorded in `corpus/lessons/round-36.md` §"C1 disposition": bind the red reference to the live `cells` FAIL/POLICY set, compare states not tokens, treat an empty red list as `SETUP`, fail closed on a non-zero `self-counts.py` exit, count `POLICY`-refused bindings as unverified, and measure SD6 in one fixed layout (lane tree 5 vs archive 3) or drop it from the kill rule.

**C2 freshness — measured 15 → 0, admitted.** `.ufo/waves/round-36/build/ReviewC2/review.md` — verdict **ADMIT-WITH-CONDITIONS** for the landed bytes (the whole table re-dated to the observation) and **REJECT** for the literal plan §Fix (which leaves `release-clock.py` at `FAILED`). Conditions verified: the round-26 receipt is superseded, not rewritten (`sha256sum` `13b8540c…`, now pinned by `R25-04`), the receipt is gate output rather than hand-edited (structure, per-record digests and byte-identical re-fetch), and the landed table passes both the counter and the gate's own `CLEAN` verdict. `ExecRehearsal` and `MutCounter` reached the same conclusion on the literal F3 independently.

## Sources & frontier

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi` — **exit 0 at round start and exit 0 at round end** (warnings only: five pre-existing `W04 duplicate url across scopes`). Lane-side `bash corpus/sources-census.sh` → `SOURCES_CENSUS: CLEAN (rows=88 …)`.

- **Rows before → after: 88 → 88.** Rows added by tier: **none** (A 84, B 2, C 2 unchanged). No knowledge entry was admitted, so no row was appended: expansion is knowledge, not rows.
- **Rows touched old → new: none landed.** The plan's §Frontier step named `recheck`/`used-by`/observation cells on S034/S035/S040/S041; the round opened all four and found their `recheck` cells hold a cadence (`90d` / `on-release`), not a date, and no `status` or `used-by` cell changed. An in-round edit that wrote 2026-11-04 into their `opened` cell (the wrong column) was reverted; `git diff corpus/SOURCES.md` is empty and the file's sha256 equals `HEAD`. Recorded as `corpus/lessons/round-36.md` M36-4 and in the lesson's Migrations table.
- **Frontier rows advanced: 0.** No frontier→core move this round; the OIDC/workload-identity and NIST ground stays where round 31/33 left it.
- **Sourced claim satisfied:** C2 rests on rows S034, S035, S040 and S041, all re-opened 2026-11-04 with the lane's own access date, body sha256 and a located ≤25-word quote in `corpus/lessons/round-36.md` §Gate.
- **Assimilation: none.** `merge/kagi/` staged nothing this round; `considerthese/2026-10-26.md` was read and its proposals 2 and 3 are already implemented (D1 discharged), so no unimplemented proposal was taken.

## Trend verdicts

- **expansion — unchanged.** Coverage and adjacency stay at 9: no registry row, no knowledge entry, no frontier→core move, no capability-table row (C1 and C2 repair declared surfaces; neither acquires a new ability). The connector sweep re-confirmed sole ground on all three surfaces.
- **quality — improved.** Freshness and operability moved measurably: the clock table now agrees with a committed 2026-11-04 observation (`15 → 0`), the gate's own verify prints `CLEAN` against the repointed default pin, `fired` goes 3 → 15 on the same table, and three prose sites that still described the round-26 default were corrected. Depth is unchanged: the round adds no mechanism claim.
- **discernment — improved.** Calibration `4 → 0` by a counter that fails closed: the lane's own `lane-status:` red set is now named by the row that must name it, and a capability count that had drifted for fifteen rounds is bound to the live gate. The three operator-owned reds are named, not cleared.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md:48` and `SKILL.md:787` (release-clock decision rows, corrected this round to the round-36 default pin), `corpus/claim-ledger.sh citations` `cites=2349 docs=97 unresolved=5`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` §Round 36 bullet 3 (the 30-row re-observation against a committed receipt, `RELEASE_CLOCK: CLEAN … fired=15 derived=15`).
- [~] Instructions executable by an agent without oral context — pointer: `plans/round-36-c1.sh`, `plans/round-36-c2.sh`, `plans/round-36-c3.sh` re-run from a clean extraction of `00bbe66` with the printed integers in this report.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `build/ConnScope/ConnOverlap.md` (20-lane sweep, sole ground, nothing absorbed) and the unchanged ownership partition row `R17-02`.

## Round notes

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none. No package manager was invoked; pacman stayed paused per the host-wide guard.
- **Seat settlement:** all 13 seats settled; **no dead seat**. Twelve delivered work product. `CriticClaims` settled with a 110-character output ("I'll start by reading the required files.") and wrote no file — it produced no critique, so none of its assigned falsification questions is answered by this round and the report does not pretend otherwise. No seat was replaced; no residual call was made.
- **Inherited attempt 1:** reused — its committed controls (all 8 re-executed and reproduced), its armed `self-counts.tsv` population row, its committed observation receipt; discarded — its uncommitted post-freeze `LANE_ROOT` instrument edit (jj keep ref `404a7b94b09af4df692e6d5b04f59b143531462c`, not an ancestor of `master`); committed for the first time — its plan (`plans/round-36.md`), before any candidate scoring.
- **Open L0:** none appended this round. The `R29-01`/`R29-02` `PYTHON_SCRIPT_RE` registration gap and the `R25-02` self-count binding remain operator-owned and are unchanged; the SD6 extraction-vs-lane reading difference and the S034/S035 anchor-cell supersession are recorded as retained debt in the lesson rather than raised as questions.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no seat-written file at the fleet root; nothing to move, nothing deleted.
