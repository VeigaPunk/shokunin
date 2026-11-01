# kumitate round 70 (attempt 3) — control-replay capability landed and receipted; C2 verified; both counters honestly unmet with named mechanisms

Lane: kumitate-shokunin · branch `master` · integration `3b1483801fe67eadc3cf48874a5a8f8150d1b72f`, budget commit `89cbd998ff956965634b14368231c6d117d6437e`, measured at M = `89cbd998ff956965634b14368231c6d117d6437e`, close commit `648c6876c07912246fb211f8150948462bd7c3d6`. Attempt 2 ended in an honest stop with C1 unlanded and the frozen counter's print-stub hole routed (K70AttackPrintStub); this attempt lands the capability, preserves every frozen byte, and answers the routed defect with a versioned ratchet whose remaining counter-side defects are themselves routed with anatomy. New host: Windows (Git Bash, node 24); no `/home/vgpnk`, no ufo-fsd-alpha origin, no `omp`.

## Work performed

- **C1 — operability (lowest non-retired axis, 9, integer held): capability `control-replay` + versioned counter ratchet.** `scripts/control-replay.mjs` (contract `kumitate-control-replay-v1`): private versioned replay of the five frozen round-69 controls — LANE/PROBE/W/S substituted exactly once each, the known unused `/tmp` write removed in the private copy only, frozen originals never executed, exclusive-create receipt with canonical-JSON inner digest, unique mkdtemp child, allow-list child environment with disclosed host adapters, selftest 21/21. Evidence: `.ufo/waves/round-70/close/replay/` (five CONTROL-PASS receipts), `close/control-replay-selftest.txt`. Counter: `.ufo/waves/round-70/probe/replay70-probe-v2.mjs` — 17 arms closing the seat-demonstrated v1 holes. The frozen v1 counter's bytes are unchanged (sha `63f52b75…` verified at base and at M).
- **C2 — coverage frontier (isolation band): sourced output-path isolation entry.** Opened CWE-59 and CWE-367 this round (S218/S219, tier A, captures pinned under `close/captures/`), landed `corpus/knowledge/replay-output-isolation-link-following.md` binding the seat attacks (K70AttackOutputSymlink / K70AttackWorkSymlink / K70AttackTmpLiteral) and v2 arms V10–V12 to the named weakness classes.
- Host bookkeeping: PROVINCE.md round-70 host correction (absent origin surfaces dated; kimi substrate present with a different 7-top-level-path shape; `~/.omp/agent` recorded as a new surface); L0 answer appended (print-stub defect resolved by ratchet, frozen v1 preserved; no wave this attempt — this host has no AgentSwarm dispatch surface); assimilation completed for considerthese/2026-10-26.md idea 4 (Q69): observed wave census from committed evidence — 64 dispatched (executor 13, critic 16, reviewer 16, scout 6, scribe 6, connector 2; attack 37/64 = 58%), 64 report files, `w1-results.json` still absent, no WAVE-DONE (settlement explicitly incomplete).
- Mistakes mined: 4 rows in `corpus/lessons/round-70.md` `## Mistakes` (attempt 3) — the writeReceipt landing defect, the three host-adapter environment faults, the dangling-link libuv crash, the v2 recursion/detail-template crash — each with class, evidence pointer, captured-by, fix.

## Landed changes

- `3b148380` — control-replay instrument, v2 counter, pins (counter-pins 40 CLEAN; source-captures +2; readme-map covered 170), SKILL registry row, SCORECARD declarations + capability row + claims table, SOURCES 156→158, corpus README row, knowledge entry, PROVINCE host correction, CWE captures.
- `89cbd998` — host-calibrated 900 s replay budget (tool + v2), repin.
- `648c6876` — five replay receipts + selftest + v1 base/tip/M and M2 counter outputs + v2 counter output at M, census-end and gates receipts, SCORECARD attempt-3 verdict section, LOG round-70 entry, lesson Gate/Mistakes appends.

## Before → after measurements

- **C1, frozen v1 predicate:** before = committed base receipt `REPLAY70_UNMET held=2/10 … rev=78b98d76…` (`.ufo/waves/round-70/base/replay70-base.txt`), reproduced line-for-line on this host at round start (`close/replay70-v1-AT-BASE-win32.txt`; modulo one capture blank line). After at M2: **`REPLAY70_UNMET held=6/10 … live=exercised`** (`close/replay70-v1-AT-M2-win32.txt`) — R1/R2/R7/R8/R9/R10 PASS; R3–R6 MISS `exit=null receipt=0`: the frozen counter's own 300 s per-mode budget kills the tool mid-replay (measured standalone control costs 643 s / 787 s / 312 s / 274 s / 264 s — `close/replay/ctl-*.txt` `durationMs`). The declared "v1 HELD 10/10" after-state therefore does **not** hold on this host; the mechanism is the frozen budget, not the capability — every mode replays to CONTROL-PASS given time. Command: `node .ufo/waves/round-70/probe/replay70-probe.mjs <lane> 89cbd998…` (win32: under the disclosed PATH `tar`-shim adapter).
- **C1, v2 ratchet at M:** **`REPLAY70V2_UNMET held=8/17`** (`close/replay70-v2-AT-M-win32.txt`). PASS: V01 frozen bytes, V02 selftest, V10 invalid-args matrix, V11 existing+dangling-link output (the K70AttackOutputSymlink hole, closed: refusal exit 3, link intact, nothing written), V14 registration triad, and the three live attack arms **V15/V16/V17 — print-only stub, canned-receipt writer, mutate-then-refuse R8 mock each read UNMET as fixtures**. MISS, with anatomy: V03–V07 on a counter-side expectation bug (the counter required `childExit===1`; the frozen controls exit **0** on CONTROL-PASS), V09 on a normalization gap (the ledger probe's L4 failing-mutant set is seed-dependent), V12/V13 resource-bound. The v2 bytes are NOT amended after scoring; the three counter-side fixes are routed to round 71.
- **C2:** SOURCES rows `grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` → 156 before (at `fb60afc`) → **158** after; entry absent → present with provenance trio; gates at close: SOURCES_CHECK CLEAN rows=158, SOURCE_CAPTURE CLEAN captures=51, README_MAP CLEAN files=170 rows=170, CITE_SOURCES CLEAN, COUNTER_PINS CLEAN pins=40 (`close/gates.txt`).

## Sources & frontier

- SOURCES rows before → after: **156 → 158** (S218 CWE-59, S219 CWE-367; both tier A, status mined, opened 2026-11-01, captures committed and pinned). No existing row touched.
- Census: `bash scripts/sources-census.sh validate --root <fleet> kumitate` — round start **exit 0** (`close/census-end.txt` records the end run; start output in the round log): six carried W04 duplicate-URL warnings both times; two pre-existing USED_BY_ASYMMETRY warns (S028/S124) verified present at base `fb60afc`.
- Frontier: the isolation band gains the output/work-path half (entry + S218/S219); no other band advanced.

## Trend verdicts

- **expansion: improved** — one new sourced knowledge entry on previously uncovered ground (weakness-class vocabulary for instrument output isolation), two new tier-A rows, pinned captures.
- **quality: improved** — the replay capability runs end-to-end on this host with a fail-closed receipt format and a hermetic allow-list child environment; the frozen predicate's host limit is measured and named, not papered over; four landing-class defects were caught by the lane's own instruments before scoring.
- **discernment: improved** — counter forgeability stays disclosed while v2 raises the bar without claiming forgery-resistance; the attempt routed its own counter defects with anatomy instead of tuning them green after scoring.

## SHONEN

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — new `| control-replay |` gate row with exit map, selftest, pin and source pointers; verifier: pending non-author closure judge.
[~] At least one end-to-end domain task executed and logged in LOG.md — the five frozen controls replayed end-to-end with receipts and both counter verdicts logged (LOG.md round 70 attempt 3); verifier: pending non-author closure judge.
[~] Instructions executable by an agent without oral context — the instrument runs from its usage text and SKILL row alone; all host adapters are recorded in receipts and the lesson; verifier: pending non-author closure judge.
[x] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE corrected for this host with dated absent/present records; CWE pages used as weakness-class vocabulary for the lane's own instruments, security-audit absorption stays routed to kasegi/kagi. Evidence: the PROVINCE round-70 band and the L0 note.

## Assimilation

considerthese/2026-10-26.md idea 4 (round-size accounting) — mined as Q69 in attempt 1; the remaining "observed census" step completed this attempt from committed evidence (lesson `## Gate`): 64 dispatched against the 64–128 band, 64 reports, results file still absent, attack share 58%. No other proposal adopted. Assimilation: none beyond this — shokuknow unreachable.

## Limits

- The frozen v1 counter remains forgeable by a canned-receipt writer (seat evidence, preserved by freeze); v2 raises the bar and claims no universal forgery-resistance.
- R3–R6 of the frozen counter cannot pass on this host inside its frozen 300 s per-mode budget; a faster host could re-read v1 at 10/10 with zero byte changes.
- The frozen deprec probe's M9 census arm is vacuous here (its hardcoded `/home/vgpnk/.../sources-census.sh` is absent; receipts record `census-exit=127`).
- Control receipt CONTENT differs from the old-host committed receipts (c1 modes now read `held=4/7`; L1/L7 details differ) — the controls' expectation (UNMET + exit 1 + CONTROL-PASS) is unchanged; deltas are host behavior, recorded in receipts.
- No wave was dispatched this attempt: no AgentSwarm surface on this host (L0 noted). The round's wave evidence remains the attempts-1/2 committed `w1/` evidence, unsettled.
- **admitted_self=false**: C1's declared after-state included the frozen v1 counter reading HELD 10/10 at the landed rev; the honest measurement is 6/10 with the budget mechanism named, and the new counter reads 8/17 with its own defects routed. C2 verifies in full. The admission call belongs to the non-author closure judge.

## Round shape

No new wave (no dispatch surface on this host). Attempt totals: 3 lane commits (integration, budget, close); all work L1-authored; probe/instrument budgets and adapters disclosed in receipts.
