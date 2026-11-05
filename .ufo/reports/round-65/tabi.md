# tabi — round 65 (attempt 1), 2026-11-05, Linux host

Lane HEAD (landed, pushed, `git ls-remote origin refs/heads/master` = `897cde97169c99921c095478436dc3f8c06b2951`).
Stale-lane: no other mission of this lane is open.

## Work performed

Declared claims (frozen at `03f35fe7`, pins in `tabi-shokunin/.ufo/waves/round-65/claims.json`):

- **C1 — adjacency** (the lane's lowest owned axis, score 8): the adjacency-ledger meter refuses two different dispositions on one (lane, path, line) key. Round-62 v21 kept the first row and ignored the later contradictory row, so a sibling overlap labelled `contested-open` could be shadowed by `overlap-declared`.
- **C2 — calibration** (score 9): the receipt-provenance gate binds each matrix's named input by sha256 and selects the round-64 `*-matrix.json` population. v1 checked a matrix input only as a string path, and its selector missed the round-64 scored matrices.

Both claims are on distinct axes and are causally separable (C1 touches the adjacency meter; C2 touches the receipt gate).

Work items (each with its evidence pointer):

- Pre-freeze fixtures and red-before evidence: commit `ac0285ce` (`tabi-shokunin/.ufo/waves/round-65/controls/c1-fab/`, `c2-fixtures/`, `redbefore/`). The round-64 v1 gate accepts the 12-receipt, 2-matrix forgery population (`redbefore/v1-gate-on-c1-fab.json`: checked 14, matrices 2, failures 0); v21 accepts both conflicting-disposition ledgers (`redbefore/tmp-*.json`, predicate true, identical bytes).
- Pre-freeze do-nothing receipts: commit `39782a84` (`controls/c1-dn-a-v21-forgery-dup.command.json`, `c1-dn-b-v21-forgery-r62.command.json`, `c2-dn-v1-forgery-dir.command.json`), produced by `controls/dn-controls-r65.py`; every input is bound to its committed bytes at `ac0285ce` (`inputs unresolved 0`).
- Wave `w1` (12 seats, see Round shape). Instruments built by the executors: v22 meter (`R65Executor1/c1-adjacency-host-v22.mjs`, selftest 47/47 after the lead's three-row case); v2 gate (`R65Executor2/check-receipt-provenance-v2.mjs`, selftest 12/12, honest fixture `c1-honest/`); command-receipt runner (`R65Executor3/run-controls-r65.sh`).
- Lead-side corrections made before the freeze (all shown with red states in the lesson's `## Mistakes`):
  - v2 matrix selector widened to `*-matrix.json` (`scripts/check-receipt-provenance` v1 missed the round-64 population: `matrices 0`; v2 on the same population: `matrices 2`, `failures 0`).
  - v2 header carries the frozen predicate sentence; v22 selftest case `three-row-conflict-count` added (M8 reversal survivor from MutTester1 killed: `pass 46/47` under reversal, `47/47` under the frozen code).
  - C1 residual corrected: the Critic found the draft's residual (`delta-fab-label.tsv` accepted) false; v22 refuses it on three same-key conflicting pairs (`audio-shokunin PROVINCE.md:4/:25/:41`).
- Freeze: commit `03f35fe7` (`counters/c1-adjacency-host-v22.mjs`, `counters/check-receipt-provenance-v2.mjs`, `counters/run-controls-r65.sh`, `claims.json`).
- Freeze-revision scored pass: `scored-at-freeze-03f35fe7/`. Runner exit 3: one input (the honest C2 fixture) was uncommitted. All other rows were produced; C2-C was not freeze-valid.
- Honest fixture commit `4a348104`: `R65Executor2/c1-honest/` committed unchanged (no instrument or pin changed). Scored pass at `4a348104`: `scored-rev2/`, runner exit 0, no unresolved inputs.
- Round-64 errata: appended block in `corpus/lessons/round-64.md` (D1 phantom wave w2, D2 seat count, D3 Mistakes table, D4 mutation count verified by command; D5 acknowledged, not re-verified).
- S170: NIST FIPS 180-4 (SHA-256 digest semantics), tier A. Opened 2026-11-05 by the scout (`R65Scout/fips-quote.txt`, `sources/fips180-4.pdf` sha256 `0455b406…deb82`); the lesson Gate records the URL, date and both located quotes (PDF extraction lines 1095–1096 and 1014).
- Mutation tests: MutTester1 (C1, 8 mutants: 6 killed, 1 equivalent, 1 killed after the lead's case); MutTester2 (C2, 8 mutants: 5 killed, 3 survivors reported in `R65MutTester2/survivors.md`).
- Attacks: Reviewer (C1, 26 rows in `R65Reviewer/c1-attacks.md`: order-insensitive, case-sensitive, re-keying residuals K1/K2), Reviewer2 (C2, under-/over-refusal, `R65Reviewer2/c2-attacks.md`), Critic (both claims, `R65Critic.md`: C1 refused on axis, C2 amend-before-freeze; both amendments applied before the freeze).

## Landed changes

Lane commits, each tied to its LOG/SCORECARD entry:

- `ac0285ce` — round-65 pre-freeze fixtures, red-before evidence, do-nothing producer (LOG round 65, Caught-and-fixed).
- `39782a84` — do-nothing control receipts (LOG round 65, Caught-and-fixed).
- `03f35fe7` — freeze of C1 and C2 with pins (LOG round 65, C1 and C2 items; SCORECARD round 65 claims table).
- `4a348104` — honest C2 fixture committed unchanged (LOG round 65, Caught-and-fixed, `landing` row).
- `897cde97` — corpus and evidence landing: `corpus/SOURCES.md` S170; `corpus/knowledge/digest-binding-round-65.md`; `corpus/lessons/round-65.md`; `corpus/lessons/round-64.md` errata; `corpus/QUALITY.md` criteria 119–120; `corpus/README.md` round-65 coverage row; `SCORECARD.md` round 65; `LOG.md` round 65; `.ufo/waves/round-65/` wave evidence and scored receipts.

Fleet-root change: L0 question appended to `.ufo/l0-questions.md` (C1 axis ruling). Report committed with `fleet-commit.sh`.

## Before → after measurements

Counting commands are committed argv; each receipt records its rev and stdout digest.

| Claim | Measurement | Before (control) | After (`4a348104`) | Verdict |
|---|---|---|---|---|
| C1 | `node .ufo/waves/round-65/counters/c1-adjacency-host-v22.mjs --repo . --rev 4a348104 … --delta <A\|B\|C> --json`; `C1-A/B/C.command.json` | A: v21 exit 0 predicate true (do-nothing, `C1-DN-A`); B: v21 exit 0 predicate true (`C1-DN-B`) | A: v22 exit 1, `delta-disposition-conflict` ×1; B: exit 1, same finding; C (real ledger): exit 0 findings [] | VERIFIED on frozen predicate |
| C2 | `node .ufo/waves/round-65/counters/check-receipt-provenance-v2.mjs --dir <DIR> --repo . --rev 4a348104 --require-committed --min-receipts <N> --json`; `C2-A/B/C.command.json` | A (`c1-fab/`): v1 exit 0, failures 0 (`C2-DN`); B (round-64 scored): v1 matrices 0 | A: v2 exit 1, `matrix-input` ×3; B: exit 0, matrices 2, failures 0; C (honest): exit 0, failures 0 | VERIFIED on frozen predicate |

Scores: no change. The round is not admitted (see Trend verdicts and the open ruling), so every axis score is held (D10).

## Sources & frontier

- Counting command (run at round end, exit 0): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi` → `ok`, exit 0 (`tabi-shokunin/.ufo/waves/round-65/controls/census-end.txt`); row count `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Before → after at `58ed8c7a` → `897cde97`: rows 169 → 170; mined 144 → 145; queued 15 → 15; rejected 10 → 10; tier A 151 → 152; tier B 9; tier C 9. The 22 `W04` duplicate-URL warnings are unchanged (the pre-existing registry; census exit 0).
- Rows added by tier: S170 (tier A, `spec`, `mined`; cited by `corpus/knowledge/digest-binding-round-65.md` and `corpus/lessons/round-65.md`). Rows touched old→new: none.
- Frontier rows advanced: S170 opened and cited by the round's sourced claim (C2's digest reading). The sourced claim is recorded in the lesson Gate and in the knowledge note's `source:` line.
- Assimilation: none. The round-57 quarantine register shift is unresolved; `considerthese/` is absent for this lane (`ls considerthese` → no such directory).

## Trend verdicts

- **expansion — improved.** One admitted knowledge note on ground the coverage map did not hold: the digest reach of a receipt gate's matrix input (`corpus/knowledge/digest-binding-round-65.md`, citing S170, tier A). Coverage row in `corpus/README.md` (round-65 section). Evidence: census above; `SCORECARD.md` round 65 (Knowledge 76 → 77).
- **quality — improved.** The lane's own gate was overstated: round-64's C2 population and its v1 selector were vacuous. Measured on committed bytes: v1 on the round-64 population `matrices 0` → v2 `matrices 2`, `failures 0`; v1 accepts the matrix forgery exit 0, v2 refuses it exit 1 with `matrix-input` ×3. Four round-64 number-drift defects corrected by errata (D1–D4). Stated limit: the gate still accepts the 12 invented receipts (QUALITY 116).
- **discernment — unchanged.** The lesson's Gate sample has no non-author spot-check yet (`Spot-check: pending (non-author)`). The Reviewer, Reviewer2, Critic and MutTesters are dispatched seats of this lane and do not count as non-author (LEARNING: a subagent the lane dispatched is still the lane). The Critic's C1 refusal is recorded and is not resolved by the lane; it becomes a discernment datum only when the operator rules.

## SHONEN
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  `SKILL.md` §Approval table (`:697`), §Evidence ladder, §Runbook; not changed this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md
  `LOG.md` round-65 entry; the scored runner pass over committed bytes `tabi-shokunin/.ufo/waves/round-65/scored-rev2/`.
- [~] Instructions executable by an agent without oral context
  `corpus/knowledge/executor-test-sufficiency.md` §0, §4 (prior, unchanged); the round-65 runner `.ufo/waves/round-65/counters/run-controls-r65.sh` ran unattended at `4a348104`.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  `PROVINCE.md:3-19`; the C1 reading exposed contested sibling overlaps (kagi PROVINCE.md:41, kaidoku PROVINCE.md:55) that remain `contested-open` and are reported, not absorbed.

No box is `[x]`: no non-author verifier has checked a box this round.

## Round shape and seats

- Shape: one v1 wave `w1`, 12 seats: scout 1, connector 1, executor 3, scribe 2, reviewer 2, critic 1, mutation-tester 2. Attack seats 5 of 12 (reviewer, critic, mutation-tester). Connector 1. No residual call. The L1 holds the planner seat (the validator forbids `planner`).
- Dispatch: `w1.ready` (`tabi-shokunin/.ufo/waves/round-65/w1.ready`), dispatch `w1-dispatch.json`, settled `w1-results.json` (12 seats, 12 results). WAVE-DONE received from the parent.
- Dead seats: none. Every seat returned output.
- Seat routes: per the global `task.agentModelOverrides`; the answering model per seat is not recorded in the results, so no claim depends on it.

## Tool installs

None. No pacman, no package install, no PATH writes. Node v24.21.0 and Chromium 155.0.8059.84 were present before the round.

## Open questions and limits

- **L0 (appended):** C1's axis. The Critic refuses it as calibration; the lesson reads it as adjacency. Round 65 is not admitted until the operator rules.
- Surviving C2 mutant M5 (relative-path resolution, no fixture holds a relative path). Reported, not fixed.
- A conflict re-keyed to a trailing `:0` line or padded lane cell is refused under another finding id (`line-row-unscreened-file`, `orphan-line-row`). C1's kill counts `delta-disposition-conflict` only.
- The C2 gate cannot distinguish executed from invented receipts; the pin is producer-declared (QUALITY 116, 118).
- The inherited v21 `hostSelftest` writes to a hardcoded `/fast/scratch/hyaku/tabi-r62/` path (left unchanged to keep v21 cases byte-identical).
- Round-64 D5 (S169 quote form) acknowledged, not re-verified.

## Process notes (recorded, not hidden)

- Freeze-revision scored run was not freeze-valid (honest fixture uncommitted). The runner refused it (exit 3); the fixture was committed unchanged and the pass rerun at `4a348104`. Both runs are kept.
- A line-range edit overwrote the first line of the claim draft with `x` before the freeze; restored and checked before commit.
- The first-pass C2 residual and C1 residual were wrong and were corrected before the freeze (lesson Mistakes).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` → only `M .scratch/run15-state.json` (orchestrator-owned; not touched). No seat misrouted a file into the fleet root.

## Commit evidence

- Lane: `ls-remote origin refs/heads/master` = `897cde97169c99921c095478436dc3f8c06b2951`; `jj-lane.sh state` → `local=897cde97 remote=897cde97 ahead=0 behind=0`.
- Report and L0 line: committed with `fleet-commit.sh --as tabi`.
