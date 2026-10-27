# tameshi — round 51 report (attempt 3, L1 TameshiR51a3)

- **Lane and revisions.**
  - Lane `tameshi-shokunin`, branch `master`. Base `9962033fd7a75aa2f2847e979dd687a5d28505a1`.
  - Freeze `fe33538405cd97c2f386c10ea91f9cf399d67866`, with amendment 1 at `84aa673a` and amendment 2 at `9d023aed`.
  - Content (deciding) revision `7e548beecfbe872f931e84c2241522ea374c6bc3`.
  - Final lane hash `6a0d5d1e577b9c341760d0aa4eb003ac28f07ece`; `git -C tameshi-shokunin ls-remote origin refs/heads/master` prints it.
- **Attempts.** Attempt 1 (TameshiR51) stopped at its request budget. Attempt 2 (TameshiR51a2) and its running w2 seats were killed when the orchestrator session exited (2026-10-26 23:57:36 -03; `.ufo/watchdog.log` lane-dead line). The orchestrator committed attempt 2's tree as salvage `53afb4aa03ea`.
- **Salvage.** Attempt 3 re-verified the salvage before reusing any of it; the disposition is listed below.

## Work performed

The round declared three claims on distinct axes, frozen in `.ufo/evidence/round-51/contract.json` before any seat:

- **C1, calibration.** This is the lowest non-retired axis, at 8. The surface is the coverage map's stale frontier status table, plus a SOURCES row whose status contradicts its used-by (S022). Both were routed by the round-50 spot-check as defects 1 and 3. Label `C1_R51_PASS`.
- **C2, depth.** A tenth recorded mutation case in the `tools/mutate-and-run.sh` leg ledger, on kagi `corpus/drift-pins.sh` @ `e64e81b8`. The spec and ten predictions were pre-registered before any mutant ran. This is the round's sourced claim: its entry cites S272 and S273, both opened this round. Label `C2_R51_PASS`.
- **C3, operability.** One conforming, runnable registry row in SKILL.md for each of the 30 frozen self-testing tools. Routed by the round-50 spot-check as defect 2. Label `C3_R51_PASS`.

Work items:

- **Pre-registration and controls (attempt 1).**
  - Freeze `fe335384`.
  - Amendment 1 (`84aa673a`) repaired the controls harness, which had crashed before scoring anything.
  - Amendment 2 (`9d023aed`) re-based the tools-scope monitor to the four tools that pin the runner's leg panel. It came from a w1 finding (`.ufo/waves/round-51/w1/T51Row19.md`), before any claim was scored.
  - Controls: 10 of 10 as pre-registered (`.ufo/evidence/round-51/control/controls.stdout`, committed `f0129a55`, re-scored at `6d8c11e3`).
- **C2 build (attempt 1).**
  - Spec `.ufo/evidence/round-51/c2/bash-drift-pins.defects.spec`.
  - Sweep result: 2 of 10 killed, 7 of 10 predictions held (`.ufo/evidence/round-51/c2/sweep/sweep.txt`).
  - Neutral-path A/B test: three survivors are harness-masked, not equivalent (`.ufo/waves/round-51/w1/T51LabSandboxLeak.md`).
  - Runner and four panel tools updated; entry `corpus/knowledge/mutation-case-kagi-drift-pins.md` (all at `6d8c11e3`).
- **C1 build (attempt 1).** The appended round-51 frontier table in `corpus/README.md`; S022 `queued` → `mined` (`6d8c11e3`).
- **C3 build (attempt 1).** 30 rows under `#### Gate/probe registry — round 51`, at SKILL.md:2140-2171 (`6d8c11e3`).
- **Salvage disposition (attempt 3).** Full list in `corpus/lessons/round-51.md` § Attempt 3.
  - Reused after re-verification: the 20 w2 reader rows.
    - For 19 of the sections, the monitor's section sha is the same at `6d8c11e3`, the bytes the seats read, and at `f133b47f`, the bytes being re-keyed.
    - The 20th section differs by one row, the round21-measure disclosure sentence, which reader T51W2Read20's NOTE-B itself records.
    - The rows were copied byte-exact into `.ufo/evidence/round-51/coldread/reads/` (`02ec217c`).
  - Discarded: attempt 2's uncommitted `SKILL.md` pointer draft. It edited sections after their readers had read them, so the re-key could not bind those reads. SKILL.md was restored to its `f133b47f` bytes (`02ec217c`). The stale pointers are routed as R51.3.
  - Superseded: attempt 2's probes in `integrate/l1-probe-f133b47/`, which are non-deciding.
- **Cold-read re-key (attempt 3).**
  - `refresh.py` gave 20 targets; the monitor went 44/64 (score 6) → 64/64 (score 8).
  - Receipts: `.ufo/evidence/round-51/coldread/rekey-02ec217c/` and `integrate/a3/refresh-02ec217c.stdout`, landed `7e548bee`.
- **Deciding run (attempt 3).** Receipts are in `.ufo/evidence/round-51/after/`, landed `6a0d5d1e`.
  - Invocation 1, at freeze `9d023aed`, was refused at gate 0 with nothing run: `control-receipt-not-after-freeze controls.exit` (`integrate/a3/deciding-invocation-1-refused.txt`).
  - Invocation 2, at freeze `84aa673a`, ran to completion. `FROZEN_UNCHANGED=0`, and its diff is exactly amendment 2's three files. Mistakes row 1 explains this.
- **Placeholder guard** (the fix for the w2 `@P@` spec defect).
  - Guard: `.ufo/evidence/round-51/integrate/a3/placeholder-guard.sh`.
  - Shown able to fail: w2 gives `FAIL placeholders=95` (exit 1), w1 gives `PASS placeholders=0` (exit 0) (`integrate/a3/placeholder-guard.receipt`).

## Landed changes

| Commit | What | LOG.md entry |
|---|---|---|
| `fe335384`, `84aa673a`, `9d023aed`, `4e095c9`, `f0129a55` | pre-registration, amendments 1 and 2, controls, SCORECARD pre-registration, wave-1 spec | LOG 2026-10-26 round 51 |
| `f846ef9`, `6d8c11e3` | frozen selftests and wave-1 evidence; C1/C2/C3 content (frontier table, S022, S272/S273, tenth leg, panel tools, 30 registry rows) | same |
| `2140478`, `f133b47f` | wave-2 spec and dispatch, reader map, census end; lesson and re-key instrument | same |
| `53afb4aa` | orchestrator salvage of attempt 2 (w2 outputs, probes, SKILL draft) | LOG 2026-10-27 round 51 attempt 3 |
| `02ec217c` | SKILL.md restored to `f133b47f`; reader rows copied in; census start (attempt 3) | same |
| `7e548bee` | cold-read re-key, 20 ledger entries (content/deciding revision) | same |
| `6a0d5d1e` | deciding receipts; lesson § Attempt 3; SCORECARD deciding section; LOG; placeholder guard; census end | same |

## Before → after measurements

- **C1.** Command: `python3 .ufo/evidence/round-51/c1/measure.py --lane LANE --rev REV --explain`
  - Before (CTL_0 at `9d023aed`): `frontier_bad=10 status_conflicts=1 total=11 C1_R51_PASS=false`.
  - After (REV `7e548bee`): `frontier_rows=10 table_rows=10 frontier_bad=0 readme_prefix=1 sources_rows=133 status_conflicts=0 usedby_missing=0 total=0 C1_R51_PASS=true` (`after/c1.stdout`).
  - **Verdict: verifies (measured).** Calibration stays at 8, the monitor's ceiling; the claim moves the surface, not the score.
- **C2.** Command: `python3 .ufo/evidence/round-51/c2/measure.py --lane LANE --rev REV --work EMPTY_DIR --explain`
  - Before (CTL_0): `recorded_cases=9 wired_legs=9 depth_score=9 C2_R51_PASS=false`.
  - After (`7e548bee`): `recorded_cases=10 wired_legs=10 depth_score=10 new_legs=1 target_new=1 pin_ok=1 spec_prereg=1 sweep_ok=1 sweep_after_freeze=1 table_match=1 regression=1 entry=1 sourced=1 readme=1 predictions_held=7/10 C2_R51_PASS=true` (`after/c2.stdout`).
  - **Verdict: verifies (measured).** Depth 9 → 10.
- **C3.** Command: `python3 .ufo/evidence/round-51/c3/measure.py --lane LANE --rev REV --work EMPTY_DIR --explain`
  - Before (CTL_0): `rows=2 covered=0 missing=30 total=30 C3_R51_PASS=false`.
  - After (`7e548bee`): `tools=30 rows=32 covered=29 missing=1 deleted=0 selftest_fail_rows=2 total=1 C3_R51_PASS=false` (`after/c3.stdout`). The missing row is `C3_TOOL tools/round21-measure.py: MISSING (line 2157 selftest-exit=1 last=)`.
  - **Verdict: does not verify; honest stop.** The tool's truthful selftest resolves sibling fleet repos at `ROOT.parent`, so it exits 1 in the counter's fresh clone (`.ufo/waves/round-51/w2/T51W2ScoutC3Provenance.md`). The predicate was not narrowed and the row was not massaged.
- **No-harm** (`after/no-harm.stdout`):
  - 11/11 monitors ok:
    - commandD: 10.
    - Cold-read: score 8, 64 credited.
    - Freshness: population 74, fresh 71, score 9.
    - Coverage monitors r45, r46 and r47: ok.
    - S160 count: ok.
    - Registry: 133 rows.
    - Tools scope: only the five allowed paths changed.
    - r49 generator: ok.
    - r50 shrinker: ok.
  - QUALITY 98 precheck: `64 → 64 lost=0 ok`.
  - Census exit 0.
  - `DECIDING_RUN_EXIT=1`, from C3 and from `FROZEN_UNCHANGED=0`.
- **Harm outside the frozen monitors (R51.1).** The `mte-interop-check` row in `tools/registry.json` still expects `legs_conforming=9/9`. The ten-leg tool prints 10/10 (`tools/mte-interop.py:343`), so that registry gate cannot pass at REV.
  - The evidence is static: w2 `T51W2Read20.md` HIGH-2. The L1 did not run that gate.
  - The frozen tools-scope monitor does not allow `tools/registry.json` to change. This is a trade; it is reported, and the operator rules on it.

## Sources & frontier

- **Rows.** 131 → 133. Counting command: `git -C tameshi-shokunin show REV:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3,} \|'`; it prints 133 at `7e548bee` and the no-harm registry monitor confirms it.
  - Added: S272 (kagi `corpus/drift-pins.sh` @ `e64e81b8`, tier A, code) and S273 (GNU Bash Reference Manual, Chet Ramey author copy, tier A, docs). Both were opened 2026-10-26, with a located quote each in `corpus/lessons/round-51.md` `## Gate`.
  - Rows touched: S022 status `queued` → `mined`; its used-by already named `corpus/knowledge/fixture-shrinking-pilot.md`.
- **Census.**
  - Start: exit 0 (attempt 1 `.ufo/evidence/round-51/census-start.exit`; attempt 3 `integrate/a3/census-start-a3.exit`).
  - End: exit 0 (`.ufo/evidence/round-51/after/census.exit` and `integrate/a3/census-end-a3.exit`).
- **Frontier.** No coverage-map ground advanced. C1 re-states the frontier status table; it is not a frontier move.
- **Sourced claim.** C2 (S272, S273).
- **Mined mistakes** (`corpus/lessons/round-51.md`).
  - From attempt 1: `oracle-leak`, whose falsifier is the red/green pair `T51LabSandboxLeak/`, and `status-usedby-conflict`.
  - From attempt 3:
    - `receipt-recency-by-last-touch`: routed, not yet shown able to fail.
    - `misroot`: T51W2Read14's fleet-root copy, which the orchestrator quarantined in `.tower/quarantine/fleet-root-strays-20261027T0020/`.
    - `unfilled-placeholder`: the guard was shown able to fail.
- **Assimilation: none.** The F6 package theme was consumed in round 50, and no staged entry serves these claims.
- **considerthese.** No proposal was mined this round.
- **Round-50 spot-check** (`corpus/lessons/round-50-verifier-spotcheck.md`). Routed defects 1 and 3 became C1 (verified); routed defect 2 became C3 (not verified, 29 of 30).

## Trend verdicts

- **expansion: improved.** A new recorded mutation case on a gate class the ledger did not hold (a host-drift gate with committed baselines), with a sourced entry (S272/S273) and two new tier-A rows. Depth went 9 → 10 by command D (`after/c2.stdout`).
- **quality: harmed.**
  - Improvements:
    - The frontier table now matches the lane's declarations, and the S022 conflict is cleared (C1).
    - 29 of 30 tools have conforming registry rows (`after/c3.stdout`).
    - The cold-read monitor is restored to 64/64.
  - Harms:
    - The `mte-interop-check` registry row cannot pass at REV (R51.1, static evidence).
    - Stale SKILL statements: "nine ledger legs", the runner's `/tmp` write scope, and runner line pointers (R51.2 and R51.3).
    - The re-key entries record `wrong_expectations: 0` by construction although a reader logged false statements (R51.2).
  - Under "a trade is not an improvement", this is reported as harmed; the operator rules.
- **discernment: improved.**
  - The oracle-leak finding: three "survivors" were shown to be harness-masked by a one-variable A/B test.
  - C3 was reported false rather than forced green.
  - Attempt 2's unread SKILL.md draft was refused, because landing it would have voided the reads.
  - Three mistakes were mined, one with a guard shown able to fail.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `reports/round-1-calibration.md#box-1`; round-51 registry table SKILL.md:2138-2171 at `7e548bee` (lane assertion; no independent verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `reports/round-1-calibration.md#box-2`; LOG round-51 entries (tenth-leg sweep `.ufo/evidence/round-51/c2/sweep/sweep.txt`, regression `cases=10 passed=10` in `after/c2.stdout`)
- [~] Instructions executable by an agent without oral context — `.ufo/evidence/round-21/coldread/ledger.json` (64/64 credited at `7e548bee`, `after/no-harm.stdout`; lane-dispatched readers, reading-bound re-key, not independent)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `reports/round-1-calibration.md#box-4`; `.ufo/waves/round-51/w2/T51W2ConnSibling.md` (runner-panel migration kept lane-local)

## Round shape, seats, hygiene

- **Shape: two v1 waves.** Both were dispatched in attempts 1 and 2 through the inline handoff. Attempt 3 dispatched no new wave: the round total was already 124, and only the deciding run remained.
  - `w1` (build): 60 seats. Roles: scribe 35, mutation-tester 11, critic 7, executor 3, connector 2, scout 1, reviewer 1. All 60 settled (`.ufo/waves/round-51/w1-results.json`); none dead.
  - `w2` (falsify): 64 seats. Roles: executor 32, reviewer 20, critic 7, connector 2, mutation-tester 1, scribe 1, scout 1. Attack share is 28/64 = 44 %. 61 settled, with outputs recovered (`w2-results.json`).
  - Dead w2 seats, killed in the session exit with no report: `T51W2MutC3Counter`, `T51W2ExecFinalCounters`, `T51W2ExecC2Replay`. None was replaced. The deciding run supersedes the last two. The C3 counter's mutation attack never ran (R51.5).
  - Round total: 124 seats, all from earlier attempts and reused, with 3 dead. Attempt 3 dispatched 0 seats. There was no residual call.
  - The L1 held the §3 planner seat.
- **Conformance defects.**
  - The w2 spec builder left `@P@` placeholders in deliverable paths: 95 in `w2-dispatch.json`, and 41 files landed under literal `@P@…` names. They are kept as append-only evidence.
  - Seat T51W2Read14 misrooted a byte-identical copy to the fleet root (sha256 `9b17352c…`); the orchestrator quarantined it.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `?? .ufo/reports/round-45/kengaku.md`, which is another lane's file and was left untouched.
- **Scratch.** `/fast/scratch/hyaku/tameshi-r51` is removed after landing.
- **Tool installs:** none. `/home/vgpnk/.omp/agent/RULES.md` was read, and pacman stayed paused.
- **Open L0 questions:** none.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
