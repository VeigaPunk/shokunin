# Souji round 35 — attempt 1 (operator wrap-up)

## Status

STATUS: PARTIAL — W1 settled (40 seats); W2 (32 seats) was dispatched, but wave closure was not received before operator wrap-up. Full frozen C1 and C2 measurements were red. The frozen C3 counter mechanically passed while its census data was falsified. No round admission or score increase is claimed; the closure registry marks round 35 rejected.

## Work performed

- Loaded the shokunin protocol, lane contract, scorecard, latest r34 verifier spot-check and routed defects. Frozen three distinct-axis claims, with C1 on the lowest-scoring non-retired axis.
- Landed the r34 uncommitted evidence receipts before moving the measurement base; froze counters, controls, source record and C3 candidate. A1 fixed the C3 SOURCES status-column index after its red-before measurement; no later counter edits were made.
- W1 dispatched 40 seats and settled. W2 dispatched 32 seats for falsification (planned round total 72); its running full-counter probes were allowed to complete. The W2 wave did not reach WAVE-DONE before operator stop. Its evidence remains under the ignored `.ufo/waves/round-35/w2/` tree; no complete `census/round-35/waves/` capture was produced.
- No packages/tools installed or updated; no pacman transaction. No pruning, locking, GC, or credential access.

## Evidence

- Lane base `1e9cad0b553891c41fe5b7ad1686decc147d76d4`; instrument `d1c940414087b606503662e4d115f51cb0fba40c`; freeze/list revision `4e9c295e9339cc2b13f7a0dd5ec9fc8213a9e18e`; C3 A1 counter fix `8788d5565f9e1cbc8cd6e4fe84222b5d6483612c`.
- **C1 red-before:** full frozen counter at instrument rev `d1c9404`, frozen list `4e9c295`: `SUMMARY items=60 agree=37 unresolved=23 mismatches=23 withdrawn=0 restated=5`, rc 1 (`w2/Probe04.md`; compared verdict/status pairs equal the committed control, whose receipt records the same C1 bytes at parent `f65753c`).
- **C1 post-W1 full reading:** frozen counter at `01dc784134ac03bf04db280383d0c70c39ac4837`: `SUMMARY items=60 agree=36 unresolved=24 mismatches=24 withdrawn=0 restated=5`, rc 1 (`w2/Probe05.md`). E33 alone changed AGREE→MISMATCH because the C3 candidate added an F1-grounded knowledge entry without adding it to the coverage map. No restatement or withdrawal rows were integrated; this was not a final post-integration reading.
- **C1 frozen-instrument defects:** R5 uses `git cat-file blob` on directory-valued pins, falsely returning `LIST-DEFECT` for E06b/E08b/E20 even though each path exists as a tree (`w2/Probe01.md`, `w2/SwarmExecutor17.md`, `w2/Mutation01.md`). G05's escaped `\t` pattern does not match tab-collapsed output (`w2/SwarmCritic03.md`). W1 proposed 11 distinct withdrawals against `WITHDRAW_MAX=4`; none of the nine cited witness paths existed at the lane tip, and conflicting dispositions were offered for G21/G24 (`w2/Probe03.md`).
- **C2 full frozen reading:** at rev `01dc784`, base `1e9cad0`, list `4e9c295`, all 13 legs: `SUMMARY legs=13 pass=10 fail=3 harm_measured=1`, rc 1. W1/W4/N4 and G1–G6 passed; W2, W3 and N3 failed (`w2/Probe07.md`, `w2/SwarmExecutor23.md`). W2's `norm` is an unbound free variable before the only binding branch; W3's normalization does not remove randomized scratch paths; N3's success detail contains lowercase `summary=` while the gate searches uppercase `SUMMARY`, and the observed sandbox `/proc` behavior also caused fixture timeouts (`w2/Probe06.md`, `w2/SwarmCritic05.md`). J1 printed `cases=5 pass=5 control=STUB-REJECTED`, but the fixture's stub selection covers W1/W2/W3/W4/N3, not J1; that control string is not a J1 verdict (`w1/SwarmScribe31.md`). No post-data counter edits were made.
- **C3 false-green:** frozen record `census/round-35/records/prune-census.tsv` says 26/27/0 (sha256 `8b37041ac1a954263c6f4e665a8105d37ac342c802fb11f596aadb69ec257177`). Independent boundary-checked read-only replays found 22 repos, 23 registrations, 1 prunable (sha256 `d8b95c00de8e2564d8ef8e9ac870004c2fa5edd51bc99f23f1aa840bb804e1c7`): four plain directories resolve upward to the fleet root, and `git worktree prune --dry-run -v` writes its removal line to stderr, while the frozen census counted stdout. The frozen C3 counter still printed `SUMMARY entries=1 legs=6 fail=0`, but L5 only tests whether digit substrings occur in the entry; it passes mismatched and synthetic record/entry pairings (`w1/SwarmExecutor25-recheck-receipt.txt`, `w2/Probe08.md`, `w2/Critic08.md`). The factual coverage claim is falsified; the mechanical PASS is not evidence of 26/27/0.
- **Frontier gate:** W1/W2 rejected three staged merge candidates. The r33 prune-census entry's same-basis growth figure is not the reason for rejection; its attribution of 10 of 14 new registrations is false, its present-tense figure is stale, and S212 binds to unrelated POSIX material. The GitLab settings entry is outside F2, has a missing base/S157 and two stale live pins. The staged trigger-set copy regresses the held r26 re-grounding; all six cited IDs are occupied. S167/S171 also violate the 11-column SOURCES contract (`w2/SwarmScribe29.md`).
- Axis scores remain calibration 7, operability 8, coverage 8. Certification OFF, K5 HELD, NAMESPACE hold unchanged. SHONEN was not changed.

## Landed changes

- Base `1e9cad0` committed the six r34 evidence receipts before the measured window.
- Instrument G2 allowed-set fix `d1c9404` includes `corpus/` and the legitimate round files.
- Freeze `4e9c295` records preregistration, controls, source snapshot and C3 candidate. A1 `8788d55` corrects the C3 registry status-cell index; C3 readings and receipts are recorded.
- C3 candidate/README frontier changes were included in lane history, but the candidate's figures were falsified; no C3 improvement is claimed. No C1 restatement/withdrawal rows or C2 counter repairs were landed.
- Current lane tip and remote `origin/master` were read as `0ab5231f2f25d90abc8e7036afc73ce306ea6f36`. No further lane edit was made after the operator's closure notice.

## Before→after

| Claim | Before | Measured result | Verdict |
|---|---|---|---|
| C1 calibration, 60 items | `agree=37 unresolved=23` at instrument rev | `agree=36 unresolved=24` at post-W1 tip; E33 flipped due to C3 cross-claim interference | MISSED; worse than red-before at that candidate tip |
| C2 operability, 13 legs | CNE rc 2 at pre-instrument tip | `pass=10 fail=3 harm_measured=1`, rc 1 | MISSED; W2/W3/N3 remain frozen failures |
| C3 sourced F1 census | frozen candidate `26/27/0` | independent replay `22/23/1`; frozen counter's `fail=0` is nondiscriminating | SUBSTANTIVE CLAIM FALSIFIED; mechanical PASS not admitted |

## Sources & frontier

S231/S232 were opened for the C3 entry, but the cited census is falsified and the entry is not treated as a valid sourced improvement. The corrected 22/23/1 record remains separate evidence, not a replacement for the frozen record or a post-data change to the C3 target. No staged merge candidate was admitted. The direct-root prune numerator remains frontier work; C1 R5/tree handling, escaped-tab normalization, witness binding/cap, and C2 W2/W3/N3 require a future preregistered round.

## Trend verdicts

- Calibration: no improvement; C1 is red at the instrument rev and regressed at the post-W1 candidate tip.
- Operability: no improvement; the full frozen measurement misses 3 legs and measures harm.
- Coverage: no improvement; the frozen C3 data is false and its counter cannot arbitrate numeric equality.
- Overall: no admissible round-level move and no owned score increase. C3's entry harmed C1 at the post-W1 tip through E33; this cross-axis interference is evidence against admission, not a trade to accept.

## Attack log

- The C1 R5 tree-pin false `LIST-DEFECT`, G05 escaped-tab mismatch, withdrawal cap/witness gap, and competing-row behavior are detailed in W1/W2 counter reports. The frozen counters were not patched after data.
- C2 W2/N3 gate defects and W3 scratch normalization are in `w2/Probe06.md` and `w2/Probe07.md`; the full C2 result is preserved above.
- C3 producer and L5 falsifications are in `w1/SwarmExecutor25.md`, `w2/Probe08.md`, and `w2/Critic08.md`. No mutating prune was run.
- W2 did not reach WAVE-DONE before operator wrap-up. Its reports/dispatch artifacts were not captured into `census/round-35/waves/`; this is an evidence-retention residual, not a claim of completed wave closure.

## Deliveries

- This fleet report is amended via `fleet-commit.sh --as souji`; prior report commit: `fca0f3f0ea81a9a28041ce76d50a761602ea093f`.
- Lane current tip/remote: `0ab5231f2f25d90abc8e7036afc73ce306ea6f36` (read-only `ls-remote` match).
- Frozen contract and controls: `souji-shokunin/census/round-35/preregistration.txt` and `census/round-35/records/`.
- W1/W2 evidence resides under `souji-shokunin/.ufo/waves/round-35/` (mostly gitignored and not fully captured); selected counter receipts are `w2/Probe04.md`, `Probe05.md`, `Probe06.md`, `Probe07.md`, `Probe08.md`.
- Lesson/scorecard/readme files exist at `souji-shokunin/corpus/lessons/round-35.md`, `SCORECARD.md`, and `corpus/README.md`; they are not represented here as a completed closure assessment.

## SHONEN

All four checklist boxes remain unchanged; no promotion decision was made:

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Gate registry; `corpus/SOURCES.md`; prior evidence `corpus/lessons/round-21.md` Gate.
- [~] At least one end-to-end domain task executed and logged in `LOG.md` — prior evidence `LOG.md:362` (2026-10-19 operator sweep).
- [~] Instructions executable without oral context — prior evidence `census/round-21/run-acceptance.py`, `accepted-matrix.json`, `remote-source-after.json`.
- [~] No cross-domain bleed — `PROVINCE.md` Round21 privacy boundary and prior Round21 overlap evidence.
