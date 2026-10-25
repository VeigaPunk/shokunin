# revenger round 65 report — attempt 1 (fresh claim after stale-claim reset)

Lane: revenger · repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin` · round tip: `5b4d29eb28d3d77c26009a11bbc6a68c0f559c40` (pushed, ahead=0, working tree clean) · base: `3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f` · measured revision: `6f1761a9911dba1b78829416938a981a54b071bc` (measure-after receipt committed as `5b4d29eb`).

**Stale-lane:** no — respawn-per-round driver; no other mission of this lane is open.
**Tool installs:** none (no package installed or updated; curl/npm-pack/python3-3.14.8 used read-only).

## Work performed

Declared claims (frozen at `reports/round-65/claims.md`, inherited from the dead prior attempt at `5a2e7a0` and re-verified before use):

- **C1 — coverage K (lowest non-retired criterion, 8/14):** one independently gated admitted entry `corpus/knowledge/round-65-apk-axml-byte-evidence.md` over an authored known-truth APK fixture, covering README row C05 (Android packages). Target `K_HELD` 8/14 → 9/14; 8/14 falsifies; README C05 flips either way at admission. **Disposition this round: candidate landed; admission pending the orchestrator-dispatched wave** (see Sources & frontier and the round-shape note) — the frozen admission order requires named fresh-seat Q01–Q13 decisions, which this seat cannot self-supply.
- **C2 — calibration, new criterion C5 (evidence-id transplant guard):** `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED` 0/2 → 2/2 via one in-script forged-evidence control per receipt script. **Verified this round.**
- Registered counter repair (diagnostic, not scored): whole-file rejected-marker scan + `STRICT_REJECT_WINDOW_SELFTEST`. **Landed.**

Work items:

- Re-verified the inherited pre-registration: re-ran `reports/round-65/measure.py` on a `git archive` tree of base `3eebcdd7…` — reproduced the red-before exactly (K 8/14, C05 frontier, C5 0/2, `HOLDS_OK_V3=no`, exit 0). Evidence: `/tmp/revenger-r65-base-run.log` pattern at run time; committed red-before `reports/round-65/measure-before.log`.
- Authored fixture `corpus/fixtures/apk-r65/` (`generator.py`, `truth.json`, `readout.py`, `fixture.apk`): binary-AXML `AndroidManifest.xml` (string pool, resource map, namespace pair, one `<manifest>` element with three typed attributes), a dex *declared header* (Adler-32/SHA-1 self-consistent, inert), a jar manifest, in a ZIP_STORED container with fixed DOS date-time. Built twice in scratch — byte-identical; regen from the committed generator in scratch reproduced `fixture.apk` byte-for-byte (Python 3.14.8). Evidence: `corpus/fixtures/apk-r65/truth.json`; run logs in session; fixture sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`.
- Byte-walk readout `corpus/fixtures/apk-r65/readout.py`: 15 facts, exit 0, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`; every one of the 14 command blocks embedded in the entry matches the tool output byte-for-byte (scripted comparison, 14/14 MATCH).
- Drafted candidate entry `corpus/knowledge/round-65-apk-axml-byte-evidence.md` (provenance trio over S038/S039/S041, observation/inference/unknown, limitations, cross-lane note, full Q-map, S038-derived struct widths).
- Opened three external sources and snapshotted them (`.ufo/waves/round-65/source-snapshots/`); appended registry rows S038 (AOSP `ResourceTypes.h`, pinned `android-15.0.0_r1`), S039 (REA android reference at `rea-agents-6.5.0`), S040 (CPython zipfile docs, queued), S041 (own-work apk-r65 bundle). Census clean at 41 rows.
- C2 patch: one control per script in `corpus/verify_icon_languages.py` and `corpus/verify_multi_icon_states.py`, each transplanting the *other* family's real saved evidence id (round-42 / round-47 ids verified present in `corpus/live/runs/` bytes before patching); insertions only (3/0 each), `receipt_ok` untouched.
- Frozen C5 mutant kills verified on scratch tree copies: both exit non-zero, last line ends `forged receipt evidence accepted` (attributed); unmutated self-tests green. Evidence: `reports/round-65/measure-after.log` MUTANT lines.
- Prepared and validated the round wave: `.ufo/waves/round-65/wave-spec.json` (64 seats), `ufo-swarm-wave.mjs plan` exit 0 (counts 64, dispatch.calls 1), `plan-validated.json` committed. Dispatch deferred to the orchestrator per the accepted host mapping (below).
- Mined M38 with a runnable red-before (`.ufo/waves/round-65/m38-red-before.log`, sha256 `aaba8252…`: pre-fix generator's chunk-size desync dies `StopIteration`) and recorded the pre-registered M37 (STRICT window) fix.

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `5a2e7a0` (inherited, prior attempt) | pre-registration `reports/round-65/claims.md` + frozen counter + red-before | "Round 65 declaration — inherited pre-registration, re-verified" |
| `c7b7cf98ddeecbd5464e47396f224e6384b78905` | candidates: `corpus/fixtures/apk-r65/`, candidate entry, `corpus/SOURCES.md` (+S038–S041), `corpus/lessons/round-65.md`, C5 patches in both receipt verifiers, `.ufo/waves/round-65/` (spec, plan, snapshots, M38 receipt) | "Round 65 build — L1-seat construction under the accepted host mapping" |
| `6f1761a9911dba1b78829416938a981a54b071bc` | `LOG.md` + `SCORECARD.md` round-65 sections | "Round 65 measurement, disposition and trends" |
| `5b4d29eb28d3d77c26009a11bbc6a68c0f559c40` | `reports/round-65/measure-after.log` (final measurement receipt) | same |

Harms sweep over the full round diff (`git diff --name-status 3eebcdd..5b4d29e`): only round-65 paths; `corpus/live`, `fixtures/firmware-r63`, `fixtures/archive-r2`, `fixtures/js-r3` byte-identical (empty numstat); README, `QUALITY.md`, `SHONEN.md` untouched; verifier patches 3 insertions / 0 deletions each.

## Before → after measurements

Counting command (frozen): `git archive <commit> corpus | tar -x -C <tree>` then from `/`: `TMPDIR=<lane-owned> python3 -B reports/round-65/measure.py <tree>`.

- **C2 (claim):** `C5_CONTROL_PRESENT` 0/2 → **2/2**; `C5_RECEIPT_KILLED` 0/2 → **2/2**; `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED` 0/2 → **2/2** (attributed, endswith `forged receipt evidence accepted`); `C5_CONTROLS_PASS` 2/2 both. Measured: before `3eebcdd7…`, after `6f1761a9…` (`reports/round-65/measure-after.log`, exit 0). Regression holds: C2/C3/C4 attributed 2/2 each, `HOLD_CALIBRATION` 4/4, `HOLD_REPLAY` 10/10, `FRESH_ROWS` 18/18, `F_COVERAGE` 5/8, `README_TOKEN_LEGEND_MISMATCH` 0, `STRICT_REJECT_WINDOW_SELFTEST=pass`, `HOLDS_OK_V3=yes`.
- **C1 (claim):** `K_HELD` 8/14 → **8/14** (candidate state, admission pending — the target 9/14 verifies only when the README flip lands on the dispatched wave's all-criteria pass; the L1 admission dry-run on a scratch copy with the flip applied prints `K_HELD=K_HELD_BACKED=K_HELD_BACKED_STRICT=9/14`, `K_ROW C05 status=held`, `README_TOKEN_LEGEND_MISMATCH=0`, `HOLDS_OK_V3=yes`, exit 0).
- Do-nothing control: base archive meets no target (`measure-before.log`); a C5-only tree moves only C5 labels, a flipped tree moves only K labels (separability by construction; the dispatched wave's `R65ReviewSeparability`/`R65LabDoNothing` seats re-prove it).

## Sources & frontier

Census command: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` — **round start: exit 0** (37 rows; four disclosed W04s S024/S028/S029/S034); **round end: exit 0** (41 rows; same four W04s). Seven frozen manual census commands: 41 rows, malformed 0, `A=39 C=2`, `mined=35 queued=2 rejected=4`, no duplicate ids, no enum violations, no missing used-by paths.

Rows added by tier: S038 spec tier A **mined** (AOSP `ResourceTypes.h`, pinned, opened+fetched+snapshotted this round); S039 docs tier A **mined** (REA android reference at tag rea-agents-6.5.0, opened via `npm pack`, snapshotted); S040 docs tier A **queued** (CPython zipfile docs, opened+snapshotted; resolves the round-64 zipfile lead as an honestly non-load-bearing row); S041 own-work tier A **mined** (the apk-r65 bundle). Rows touched old→new: none (append-only). Frontier rows advanced: none admitted this round; C05 moved from pure frontier to *covered-by-candidate* (admission deferred, disposition recorded in `SCORECARD.md` and the lesson).

The frontier step's three other items: census before→after recorded above; mistake mined (M38, with red-before; plus pre-registered M37 recorded); sourced claim — C1 rests on S038/S039/S041 opened this round (the entry header cites them; the lesson `## Gate` records URL, access date and ≤25-word located quotes for each).

**Prepared-but-undispatched wave (accepted host mapping):** this seat prepares waves; the orchestrator dispatches them between rounds (operator mapping 2026-10-23; reported as the mapping, never as a conformance defect). Prepared: ONE v2 wave, exactly **64 seats** (policy v2 band 64–128), validated `plan` exit 0, `dispatch.calls=1`, spec + per-seat briefs + validated plan committed at `.ufo/waves/round-65/`. Seat-role mix: executor 10, scribe 3, scout 9, reviewer 20, critic 10, mutation-tester 7 (incl. both probe seats), sentinel 1, simplifier 1, revenger 1, connector 1; attack roles (reviewer+critic+mutation-tester+sentinel) 38/64 = 59% ≥ 25%; §3 floor roles all present (connector 1; executors 3+; scribe 1+; scout 1+; reviewer/critic 1+); **planner seat held by the L1** (the validator rejects `planner` as a swarm role — frozen topology). Dead seats: none (zero dispatched). Residual: none. Receipts for the orchestrator's dispatch: 64 distinct attack/build items each naming its target artifact and absolute report path; every seat writes only its own file under `.ufo/waves/round-65/`.

## Trend verdicts

- **expansion: unchanged** — no knowledge admission this round; C05 is covered by a measurement-ready candidate, not an admitted row (`K_HELD` 8/14 both ends, re-measured on committed archives). The candidate + opened sources are the expansion work queued one gate away.
- **quality: improved** — C2 calibration guard landed with attributed mutant kills on both scripts and zero regressions across C2/C3/C4 and the ten-verifier replay census; M38 mined with a runnable red-before (layout-from-intent caught by byte verification); the STRICT rejected-marker scan-window repair is registered with a self-test (`STRICT_REJECT_WINDOW_SELFTEST=pass`).
- **discernment: improved** — the round declined to self-certify C1: the README flip is explicitly deferred to named fresh-seat decisions per the frozen admission order rather than claimed; M38's captured-by names Q06 as the check that should have caught it; S040 is recorded as queued-and-non-load-bearing rather than inflated into support.

## SHONEN

- [x] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged this round; round-64 verifier `R64ReviewSkill` on record (per the round-64 closure routing, a non-lane re-confirmation of the `[x]` remains the integrator's duty; this round makes no lane-side flip).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 65 measurement, disposition and trends"; `reports/round-65/measure-after.log` (frozen counter over archived corpus, exit 0); candidate readout executed end-to-end (`507d79f8…` stdout).
- [~] Instructions executable by an agent without oral context — the fixture's `generator.py`/`readout.py` reproduce from committed bytes in a scratch copy (regen byte-compare PASS); no independent outside instruction verifier this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — entry `## Cross-lane scope note (Q10)` + README C05 candidate parenthetical report-not-absorb ADJ-06 (fleet `.ufo/l0-questions.md:42` open); no province sentence edited; the validated wave carries the connector overlap scan (`R65ConnectorOverlap`) for the dispatched round.

## Open items

- L0 questions: none appended this round (nothing blocked on an operator decision; the C1 deferral is dispositioned in-round, not punted).
- For the closure: C1's verdict should be recorded as **pending-dispatch** (not falsified): the candidate, the validated wave, and the admission dry-run are committed evidence; the flip itself awaits the orchestrator's between-round dispatch per the accepted host mapping.
