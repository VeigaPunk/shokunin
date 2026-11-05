# kagi — round 39 report (attempt 2)

Lane HEAD at filing: `368991952b57e8425a6e441ee53830eb5a35cd2a` (`git ls-remote origin refs/heads/master` prints the same). Measured commit for every counter and gate below: `4776f71ff85cb53f11e1a7a70fbc596043bcc92f` (landing). Commits after it, `943815afdce71c43c460b7f95794296a57ea1b07` and `368991952b57e8425a6e441ee53830eb5a35cd2a`, change only `corpus/lessons/round-39.md` (`git diff --stat 4776f71 368991952b57e8425a6e441ee53830eb5a35cd2a`: one file, 2 insertions, 2 deletions), so the instrument inputs are the measured ones.

## Work performed

Declared claims (frozen in `plans/round-39.md`, plan commit `7c11e769cd7c2450cf46faabcd3b43fca993f388`; predeclaration `1909e3876341cc90246516886def37a7c9ea92f9`):

- **C1 — freshness (owned axis).** An anchor-pin drift gate, `corpus/anchor-pins.sh`, binds the anchor cells of the three superseded feed rows S034, S035, S039 to committed sha256 pins. Frozen counter `plans/round-39-c1.sh`; target 3; claim BASE 0.
- **C2 — calibration (owned axis).** A declared-axis conformance gate, `corpus/claims-declared.sh`, checks each round-39 claim's plan heading and tagged SCORECARD row against the frozen manifest `corpus/claims-declared.tsv`. Frozen counter `plans/round-39-c2.sh`; target 3; claim BASE 0.
- Capability rows entered by this round (SCORECARD `## Capabilities`, first-working round 39): `anchor-pin drift detection`, `declared-axis conformance`.
- Exploratory claims: none. The lowest-axis obligation is met by C1 (both owned axes stand at 9).

Work items, with evidence:

- Predeclaration `1909e38`: instruments, pins, frozen counters, controls; `PREFREEZE: CLEAN (controls=4 mismatch=0)` over `plans/round-39.controls.tsv` (LOG.md:1747).
- Frozen plan `7c11e76` (`plans/round-39.md`), committed alone after the pre-freeze gate.
- Candidate `6742fde`: S094 registry row, lesson, SCORECARD round-39 sections, laneguard usage correction (R38-EG-1). Attempt 1 produced this commit; attempt 2 re-verified it.
- Wave `build`: one v1 wave of 10 seats, reports under `.ufo/waves/round-39/build/` (eight `K39*.md` reports plus receipt directories), results `.ufo/waves/round-39/build-results.json`. Seat outcomes in §Round shape.
- Landing `4776f71` and corrections `943815a`, `368991952`: capability rows, SD5 reds restored, S040/S041 recheck marked, census receipts, wave evidence committed, lesson corrections (`corpus/lessons/round-39.md` §Landing corrections).
- Frozen-counter and gate re-runs at the landing commit from a pristine `git archive 4776f71` (not the working tree), results in §Before → after measurements.
- Inherited from attempt 1: the candidate, plan, predeclaration and the uncommitted wave directory. The wave dispatch and seat outputs were re-read and re-verified here; nothing inherited was discarded. The attempt-1 L1 `KagiR39` (parked) acknowledged the handoff and stopped round work.

## Landed changes

| Commit | Change | Entry |
|---|---|---|
| `1909e3876341cc90246516886def37a7c9ea92f9` | predeclaration: C1/C2 instruments, pins, frozen counters, controls | LOG.md:1747 |
| `7c11e769cd7c2450cf46faabcd3b43fca993f388` | frozen plan `plans/round-39.md` | LOG.md:1747 |
| `6742fdef0e261dd06a38a0fb0b66b1bc027d1bee` | candidate: S094 row (`corpus/SOURCES.md`), lesson, SCORECARD round-39 sections, `corpus/laneguard.sh` usage | LOG.md:1748–1751 |
| `4776f71ff85cb53f11e1a7a70fbc596043bcc92f` | landing: SCORECARD capability rows (lines 710–711), "latest first-working round" = 39 (line 713), calibration row restores reds `R25-02`, `R29-01`, `R29-02` (line 1492), coverage row states the non-migration (line 1495); `corpus/SOURCES.md` S040 and S041 `recheck` `on-release` → `2026-11-05` (lines 47–48); wave evidence and census receipts under `.ufo/waves/round-39/`; lesson §Landing corrections and mistake rows M39-4 to M39-12 | LOG.md:1752–1755 |
| `943815afdce71c43c460b7f95794296a57ea1b07` | lesson M39-9 row reworded so it no longer quotes a missing migration path (self-description SD6) | lesson §Mistakes |
| `368991952b57e8425a6e441ee53830eb5a35cd2a` | lesson discernment bullet: reviewer false-clean count corrected from eleven to twelve | lesson §Landing corrections |

No instrument, pin, plan, control, or ledger byte changed after `7c11e76`: `git diff --stat 1909e38 4776f71 -- corpus/anchor-pins.sh corpus/anchor-pins.tsv corpus/claims-declared.sh corpus/claims-declared.tsv plans/round-39-c1.sh plans/round-39-c2.sh plans/round-39.controls.tsv plans/round-39-controls.sh` is empty; `git diff --stat 7c11e76 4776f71 -- plans/round-39.md` is empty; `git diff --stat 0614451 4776f71 -- corpus/claim-ledger.tsv` is empty.

## Before → after measurements

**C1 freshness — anchor-pin drift gate.**

- Counting command: `bash plans/round-39-c1.sh` (frozen counter, prints one integer).
- Before (claim BASE `0614451`, instrument absent): `0`. The do-nothing control `c1_nowork` reads 0 at `1909e38` (`PREFREEZE: CLEAN (controls=4 mismatch=0)`).
- After (landing `4776f71`, pristine archive): `3`, rc 0.
- Gate: `bash corpus/anchor-pins.sh --root .` → `ANCHOR_PINS: CLEAN (pins=3)`, rc 0.
- Score: freshness 9 → 9. The move is instrument coverage, not a re-derived score.
- Verdict: **verified under the frozen predicate and kill rules** (counter 3; gate CLEAN; pins and anchor cells unchanged). Ceilings and defects, all recorded and routed (see below): S036 is a fourth superseded feed anchor and is unpinned; a pin rewritten together with its row passes (QM40); the counter can be made to return 3 from a constant (M39-6, mutation-tester C1-CT2); C1's new BASE coverage is one cell, S039, because `corpus/release-clock.py` already reports M1 and M2 as DERIVATION findings at BASE (M39-8, scout D2).

**C2 calibration — declared-axis gate.**

- Counting command: `bash plans/round-39-c2.sh`.
- Before (claim BASE, instrument absent): `0` (`c2_nowork`, `1909e38`).
- After (landing `4776f71`, pristine archive): `3`, rc 0.
- Gate: `bash corpus/claims-declared.sh --root .` → `CLAIMS_DECLARED: CLEAN (claims=2)`, rc 0.
- Score: calibration 9 → 9.
- Verdict: **verified under the frozen predicate and kill rules.** Ceilings and defects, routed: the gate does not judge axis fit (QM41); duplicate manifest rows pass CLEAN (`claims=3`); a heading inside a code fence or HTML comment passes; a padded axis cell passes (reviewer D1–D5, `.ufo/waves/round-39/build/K39ReviewDeclared.md`); the round-38 relabel stays outside the manifest, unrecorded as a mismatch (named).

**Other measurements at `4776f71` (pristine archive):**

| Check | Command | Result | Rc |
|---|---|---|---|
| Lane census, BASE `0614451` | `bash corpus/sources-census.sh` in `git archive 0614451` | `SOURCES_CENSUS: CLEAN (rows=93 A=89 B=2 C=2 queued=1 mined=89 rejected=3 entries_sourced=14 legacy=21 captures=93 inrow=16 inrow_only=0 inrow_nonreproducing=12)` | 0 (`.ufo/waves/round-39/census/start-lane-0614451.txt`) |
| Lane census, landing | `bash corpus/sources-census.sh` | `SOURCES_CENSUS: CLEAN (rows=94 A=90 B=2 C=2 queued=1 mined=90 rejected=3 entries_sourced=14 legacy=21 captures=94 inrow=16 inrow_only=0 inrow_nonreproducing=12)` | 0 (`census/landing-lane.txt`) |
| Fleet census, landing | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi` | `kagi ok`; 19 W04 duplicate-URL warnings | 0 (`census/landing-fleet.txt`) |
| Round-36 counter | `bash plans/round-36-c1.sh` (pristine archive of `368991952`) | `0` (ledger `R36-01` passes); candidate `6742fde` read `3` | 0 |
| Round-37 counter | `bash plans/round-37-c2.sh` (pristine archive of `368991952`) | `0` (unchanged) | 0 |
| Self-description sweep | `bash corpus/self-description-sweep.sh` at `943815a` | `SELF_DESCRIPTION: MISMATCH n=3 (SD6=3)` = BASE; SD6 rows are verifier-owned (`round-30/32/33-verifier-spotcheck.md`); candidate `6742fde` read `n=9` | not captured (prints MISMATCH for the verifier-owned residue) |
| Frozen anchor gate, claims gate | as above | CLEAN (pins=3); CLEAN (claims=2) | 0 |

Counter exit codes captured at the final tip `368991952` (pristine archive, `$?` of the counter itself): `plans/round-39-c1.sh` stdout `3`, rc 0; `plans/round-39-c2.sh` stdout `3`, rc 0; `plans/round-37-c2.sh` `0`, rc 0; `plans/round-36-c1.sh` `0`, rc 0.
**Ledger, named debt (not migrated).** Six `corpus/claim-ledger.tsv` rows fail at the landing tree because they pin pre-round values: `R13-01` (`grep -c '^## Round ' SCORECARD.md` now 52, expects `^50$`); `R24-06` (`bash corpus/row-identity.sh scorecard-rounds` → `count=52`, expects 50; the two added headings are a pure append, verified by diff against `0614451`); `R21-02`, `R31-02`, `R33-02`, `R34-03` (census rows 94, expects 93). The plan deferred ledger rebinding to a round-38-style migration; this round does not perform it. The candidate's citation of a migration journal is removed (no such file was committed).

## Sources & frontier

- SOURCES rows before → after: `93 → 94` (`bash corpus/sources-census.sh` at BASE and landing; rc 0 both; receipts in `.ufo/waves/round-39/census/`). Fleet validate rc 0 at landing; round-start fleet validate rc 0 per attempt-1 lesson §Census.
- Rows added by tier: tier A, 1 (S094, `own-work`, status `mined`, `corpus/CORPUS.md` §SOURCES.md rule 2, line 116 "Only `status`, `recheck` and `used-by` change in place"). Its located quote is in `corpus/lessons/round-39.md` §Gate.
- Rows touched old → new: S040 `recheck` `on-release` → `2026-11-05`; S041 `recheck` `on-release` → `2026-11-05` (lesson §Landing corrections). `status`, `used-by` and every other cell unchanged. S027 and S028 are superseded and keep `on-release`.
- Frontier rows advanced: S094 is cited by C1 (the sourced claim, §2b rule 4). S040 and S041 are marked due after the live Python documentation check.
- Mined mistakes: M39-4 to M39-12 in `corpus/lessons/round-39.md` §Mistakes. Captured-by is `none` for all but M39-9 (`R36-01`). Fix red/green witnesses are in each row, for example M39-4 (grep red before the table rows, green after) and M39-9 (round-36 counter 3 at candidate, 0 at landing).
- Frontier step conformance: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi` exit 0 at round end.
- Assimilation: none. Nothing appended from `merge/kagi/` or the absent-defect register (the eight `kagi` rows stay quarantined).
- considerthese: not taken this round. `considerthese/` holds dated files (2026-10-19 to 2026-10-23); both claims are frozen in the plan, and the item cannot widen a frozen target. Not claimed.

## Trend verdicts

- **expansion: improved.** Two capability rows entered SCORECARD `## Capabilities` (`anchor-pin drift detection`, `declared-axis conformance`), each demonstrated by its frozen counter and gate at `4776f71`. One own-work registry row (S094). No knowledge entry admitted, so this is capability growth, not admitted-entry growth.
- **quality: unchanged.** Two Python registry rows (S040, S041) found stale against the served documentation (3.15.2) are marked due, not re-verified. S012's rendered-text quote does not locate (`count=0`), an existing census class recorded and routed, not newly marked. No admitted entry failed a re-check and none was superseded.
- **discernment: unchanged.** No non-author spot-check exists for this round; the integrator closure is pending. The wave's critic, reviewer and mutation-tester seats (lane-dispatched, lane evidence) recorded eight claim-layer defects (critic D1–D8) and twelve gate false-clean paths (reviewer F1–F7, D1–D5), and the claim-layer defects were corrected or routed. No `unprovable-but-better` is claimed: no named non-author reviewer is on record.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md` unchanged this round; prior evidence as in `LOG.md` earlier rounds; not re-verified here.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: this round's live recheck of five vendor surfaces and the Python documentation (`.ufo/waves/round-39/build/K39ScoutFired.md` §2; `corpus/lessons/round-39.md` §Landing corrections "Trial on real domain work").
- [~] Instructions executable by an agent without oral context — evidence: `bash corpus/anchor-pins.sh --root .` and `bash corpus/claims-declared.sh --root .` run from a pristine archive of `4776f71` in this attempt (§Before → after).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `.ufo/waves/round-39/build/K39ConnOverlap.md` (read-only sibling overlap scan; no overlap; sibling surfaces reported, not absorbed).

## Round shape and settlement

- Shape: one v1 wave `build`, 10 seats (band 8–16; L2 floor 8 met). Spec `.ufo/waves/round-39/build-spec.json`; dispatch `build-dispatch.json`; ready `build.ready` (written by attempt 1 at 08:09, `l1` = `KagiR39`); dispatched by the orchestrator 08:15:13 (`build.ready.dispatched`); results `build-results.json`. Attempt 2 dispatched no seat of its own.
- Roles: executor ×3 (`K39ExecAnchor`, `K39ExecDeclared`, `K39ExecSources`); scribe ×1 (`K39ScribeTrial`); scout ×1 (`K39ScoutFired`); connector ×1 (`K39ConnOverlap`); reviewer ×2 (`K39ReviewAnchor`, `K39ReviewDeclared`); critic ×1 (`K39CriticClaims`); mutation-tester ×1 (`K39MutInstruments`).
- Attack seats: reviewer 2 + critic 1 + mutation-tester 1 = 4 of 10 = 40% (≥25% met). Connector seats: 1 (≤2).
- Planner: held by the L1 (the validator rejects `planner`; same deviation as rounds 33, 37, 38).
- Dead seats: 2. `K39ExecAnchor` (executor, C1 re-execution) and `K39ScribeTrial` (scribe, trial drafting) produced no report file; `build-results.json` records `output` null for all ten seats after an orchestrator kernel restart mid-wave. Not replaced (protocol). Their claims carry no seat evidence here; C1 is reproduced by the other seats and by this L1.
- Residual calls: none. No second falsification wave was dispatched; attacks came inside wave 1.
- Round total: 10 seats. Seat routes are not recorded in `build-results.json`; no claim depends on a seat's answering model.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. The attempt-1 L1 `KagiR39` is parked; it acknowledged the transfer and stopped round work.

## Open L0 questions

- `kagi | round-39 | build wave (.ufo/waves/round-39/build.ready, dispatched 08:15:13) names l1=KagiR39 …` is appended at `.ufo/l0-questions.md` line 349 and is in fleet history (`36546f0f`). Routed around: attempt 2 owns the round; no operator decision is needed to land.
- No other open question. Operator-owned items unchanged: `R25-02` FAIL, `R29-01`/`R29-02` POLICY, `R38-03` POLICY (SCORECARD lane-status line).

## Routed to round 40 (not claimed)

- S036 pin as a new claim with its own predicate (fourth superseded feed anchor, M39-7).
- Frozen-counter amendments: the constant-return survivor (M39-6); the C2 counter's ceilings.
- Gate false-clean paths: C1 F1–F7 and C2 D1–D5 with red witnesses (M39-12).
- Six-row ledger migration (`R13-01`, `R21-02`, `R24-06`, `R31-02`, `R33-02`, `R34-03`), round-38 style.
- S012 rendered-text locate failure (`count=0`); S040/S041 documentation refresh as a new row or a recheck result.
- R38-D4 frozen-counter amendments (V1, V2, V4, V5, V6; M2, M3, M5, M6, G3); R37-V2 release-clock re-point.
- Seat-receipt path check: `/tmp` fixtures are not citable (M39-10); routed to the orchestrator.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at filing: `M .scratch/run15-state.json` (orchestrator-owned; not touched). No untracked file names this lane or round. Nothing copied and nothing deleted at the fleet root. A fleet-root `"report written"` file seen earlier names `agent://TabiR68a2` (another lane's seat) and is not this lane's; it was no longer present at the check.

## Conformance

- Tools installed or upgraded: none (no installs; no pacman; no sysctl or service change by this L1). The seats' receipts record no sysctl or service mutation (`K39ExecDeclared.md` Housekeeping; `K39MutInstruments.md` Boundaries). `RULES.md` was not consulted because nothing was installed.
- Scratch: attempt-2 measurement trees under `$HYAKU_SCRATCH/kagi-r39/l1` were removed after use. Seat receipts cite `/tmp` paths (M39-10); this report cites none.
- L0: no operator decision blocks landing (above).
- Report and L0 line committed through `fleet-commit.sh --as kagi`; lane tip pushed through `jj-lane.sh`.
