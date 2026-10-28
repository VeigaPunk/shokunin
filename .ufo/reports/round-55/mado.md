# mado — round 55 report (hyaku run 11, attempt 1)

Lane tip `63f48dc1b240b707c5ab9d634e2395ab90e1540c` (pushed; `git ls-remote origin refs/heads/master` prints it). Measured content revision `d3fc9ac14a673a7d56f11b6d4956d754179067bf`. Base `3b55b6e91e40f455dd56b2985e4ffc087ada92d5`. Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Work performed

Declared claims: **C1 coverage** (sourced entry: keyboard repeat rate, repeat delay, numlock on Hyprland 0.56.2), **C2 operability** (capability acquisition: `tools/mado-kbdopts.py`), **C3 freshness** (append-only correction of the false P19). Stagnation nudge applied (saturation 9.0, N=3; last capability r51), recorded in SCORECARD. Mistake-fix item (not a claim): `quality/check-freeze-order.py` + QUALITY 106. L1 held the planner seat (data walk, frozen tables, fixtures, sealed hold-out).

- Freeze committed before any wave: `54dacbd8` (committer 2026-10-28T18:46:52-03; `.ready` written 18:50:27). The lane helper had rewritten it from `59e3763f` two seconds earlier (disclosed, QUALITY 106). Evidence: `.ufo/waves/round-55/claims-frozen.md`, `registration.md`, `frozen-tables.json`, `fixtures/c2`, `ctl/`, `receipts/before.txt`.
- Wave 1 (build + first falsifiers): 40 seats, 38 settled, 2 dead (R55ScoutCallers, R55ScoutHyprlang: provider "Weekly usage limit reached", operator-confirmed; re-issued in w2). Candidates committed `3c868d82` before the hold-out reveal; four independently written tools tied 18/18 + 8/8, chosen on robustness probes.
- Pre-data errata `registration-v2.md` + `frozen-tables-v2.json` (`5a43d67f`), written after w1 attacks and before the real entry/counters existed. **Disclosure: v1 PRED-C1 as literally written could not be met by any entry** (K16 quote contains `||` vs "no `|` in a cell"; K17 source leg unsatisfiable for S052); also a contract sentence contradicted fixture F10. Predicate sentences, targets and control counts are unchanged; the closure should judge whether v2 counts as pre-data.
- Wave 2 (falsify): 37 seats, 0 dead. Findings applied: entry wording (clamp→floor, E03, E07, second seat-push route E14, join section), P23 overload/scope wording, supersession rows S381/S382 for S379/S380 scope cells, tool docstring divergence list (8 constructs), C1 harness `/7` denominator, C2 run dir outside export ancestry, C1 counter repo-root check, 24 survivor-derived extra C2 fixtures, QUALITY 106 limits. Reports: `.ufo/waves/round-55/w{1,2}/`.
- Assimilation: none (no shokuknow package entry). considerthese: `2026-10-26.md:50` proposal 4 mined in the lesson (live read-only tool run, `receipts/live-kbdopts.txt`).
- Tool installs/updates: none. Residual call: none.

Round shape and size: two v1 waves, **w1 40 + w2 37 = 77 seats**. w1 roles: executor 12, reviewer 8, scribe 7, scout 6, critic 4, connector 2, sentinel 1 (attack share reviewer+critic 12/40). w2 roles: reviewer 14, critic 9, mutation-tester 9, scout 4, sentinel 1 (attack 32/37). Dead seats: 2 (w1, provider). One seat-name collision (R55RevC1Contract/-2) plus 10 registry renames. Missing sidecars: R55ScoutCallers, R55ScoutHyprlang (w1).

## Landed changes

| Change | LOG | Commit |
|---|---|---|
| freeze, claims, fixtures, controls, baseline | LOG r55 | `54dacbd8` |
| w1 spec/dispatch; w1 results + candidates | LOG r55 | `dbc2eefe`, `3c868d82` |
| registration v2 + tables v2 | LOG r55 | `5a43d67f` |
| integration: entry, rows S378-S380, tool, harnesses, counters, P23 block, README/PROVINCE/ledger | LOG r55 | `ebd66fbf` |
| harness fix, QUALITY 106 | LOG r55 | `57584ed6` |
| w2 spec/dispatch | LOG r55 | `721ba9c1` |
| wave-2 findings applied (rows S381-S382, docs, hardening) | LOG r55 | `187003d0` |
| w2 results, entry pointer | LOG r55 | `d3fc9ac1` |
| LOG, SCORECARD, lesson, final receipts | LOG r55 | `63f48dc1` |

## Before → after measurements

All at `d3fc9ac14a67…` (`.ufo/waves/round-55/receipts/at-final.txt`, exit codes verbatim).

- **C1** before (`receipts/before.txt`): entry/counter/harness 0/0/0. After: `MADO_KBD_ENTRY: … rows=18/18 hosts=6/6 sources=18/18 new_rows=3/3 verdict=TARGET_MET missed=none` (rc 0) and `MADO_R55_CONTROLS: claim=c1 good=ok controls=7/7 verdict=OK`. Command: `python3 -I quality/counters/c1-r55-kbd-entry.py --repo . --rev <rev> --work <s>`. TARGET_MET as quote identity; junk and false-proposition entries also pass (declared limit; R55W2CritC1Forge). Seat sentence-to-pin audits: 0 UNSUPPORTED, overreaches corrected.
- **C2** before: tool absent. After: `MADO_R55_C2: … fixtures=18/18 holdout=8/8 holdout_commit=ok controls=3/3 verdict=TARGET_MET`; extra 24/24 informational. Command: `python3 -I quality/check-r55-controls.py --claim c2 --repo . --rev <rev> --work <s>`. Tool is an approximation (docstring lists divergences from hyprlang).
- **C3** before: `grep -c P23` → 0. After: `MADO_P19_FIX: … prefix=identical rows=13/13 pin=ok p23=ok readme=ok verdict=TARGET_MET` and `claim=c3 … controls=6/6 OK`. Lexical `p23` leg proves vocabulary; truth rests on R55W2RevP23.
- Mistake fix: `check-freeze-order.py` round 54 w1 → `FAIL freeze_after_launch` (rc 1); round 55 w1/w2 → `OK`.
- Harm watch: `MADO_SELFTEST: 460/460`; `MADO_INDEX … 70/70`; `LEDGER: population=90 … TARGET_MET`; `MADO_WAVE_DONE: round=55 waves=2 settled=2 verdict=OK` (committed receipt); census exit 0.

## Sources & frontier

Census before (`.ufo/waves/round-55/receipts/census-before.txt`): `mado ok`, 314 rows, exit 0. After (`receipts/at-final.txt`): `mado ok`, 319 rows, exit 0 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Rows added: tier A ×5 (S378-S380 opened 2026-10-28; S381/S382 supersession rows). Touched old→new: `used-by` of S052, S316-S319 (appended the entry path), logged in `corpus/lessons/round-55.md`. New W04 warnings: S380-S382 (same IKeyboard.hpp/Seat.cpp URLs; QUALITY 17 distinct-scope review in lesson). Frontier advanced: input-device per-keyboard repeat/numlock chain (README Frontier bullets). Assimilation: none. Mined mistake: M55-1 (freeze after launch), fix shown able to fail on round-54 objects.

## Trend verdicts

- **expansion: improved** — a sourced chain from config to `wl_keyboard.repeat_info` on ground that held 0 corpus hits for `repeat_info`/`m_repeatRate`; the host readback itself was already held.
- **quality: improved** — false P19 corrected append-only; entry overreaches found by seat audits fixed; but wave 2 BROKE content-blindness of the counters (junk/false entries pass) and the tool's fidelity (8 divergences), disclosed not fixed.
- **discernment: unchanged** — no non-author admit/reject sample at filing (all seats are lane authors); ready for closure: admit S378, narrow admit S380, reject numlock-range-as-source.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — historical `corpus/knowledge/executor-test-sufficiency.md`; no new outside-lane verification this round.
- [~] At least one end-to-end domain task executed and logged — LOG.md round 55 + `receipts/live-kbdopts.txt` (read-only live run); no outside-lane verifier.
- [~] Instructions executable by an agent without oral context — entry "How to verify" commands were run by R55W2CritEntryProse; dispatched seats are not independent.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE round-55 paragraph corrected after R55W2CritCoverage; adjacency sweep `w1/R55ScoutAdjacency.md`.

Open L0 questions: none. Misroot sweep: fleet-root `git status --porcelain` shows no mado/r55 files (only `.scratch/closure-mado-r50.json`, orchestrator-owned).
