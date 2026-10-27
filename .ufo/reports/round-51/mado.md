# mado — round 51 report

Lane: `/home/vgpnk/Projects/shokunin/mado-shokunin`; final lane tip `bb32ee29761cf49f0104383c080b925c8706eac0` (verified on `origin/master`).

## Work performed

Declared claims: **C1 — operability/capability:** a tracked lane-level instrument ledger and checker. **C2 — coverage/sourced:** Hyprland 0.56.2 dispatcher-execution knowledge beyond the round-50 key-match surface. The two claims target distinct axes and are causally separable (`.ufo/waves/round-51/claims.md:9-69`; freeze commit `d2740281`).

- C1 landed `quality/tool-ledger.md`, `quality/check-tool-ledger.py` and `quality/counters/c1-r51-ledger.py`; exact population is 82 at the freeze, and the checker selftest is 50/50 (`.ufo/waves/round-51/receipts/c1-at-integration.txt`; `quality/check-tool-ledger.py`; commit `56026fcb`). W2 found that generic descriptions and a ledger-wide self-pointer pass the frozen lexical predicate; these are bounded limitations, not proof of contextual accountability (`.ufo/waves/round-51/w2/CritC1GenericDesc/generic-descriptions.md`; `w2/CritTrendEvidence.md`; `registration.md:27-31`).
- C2 landed `corpus/knowledge/hyprland-dispatcher-dispatch-r51.md`, registry rows S364-S369 and the README coverage/frontier rows (`corpus/SOURCES.md:313-318`; `corpus/README.md:78,116`; commit `a0e34387`). W2 source-truth review identified overclaims in the first wording; append-only errata now withdraw/narrow them (`corpus/knowledge/hyprland-dispatcher-dispatch-r51.md:318-357`; commit `b742d54c`). The unchanged counter still returns 4/4 after correction (`.ufo/waves/round-51/receipts/c2-at-integration.txt`, measured at `485bdfd`).
- W1 build/first-attack wave: 43 seats, all settled; W2 falsification wave: 33 seats, all settled; total 76, no dead seats (`.ufo/waves/round-51/w1-results.json`, `w2-results.json`, `.ufo/waves/round-51/receipts/wave-done-final.txt`). W1 roles: reviewer 11, executor 8, critic 6, scribe 5, mutation-tester 4, scout 4, sentinel 2, connector 1, revenger 1, simplifier 1. W2 roles: reviewer 12, critic 9, mutation-tester 7, sentinel 2, connector 2, scout 1. Planner was held by the L1 as required by the frozen validator topology; no residual task call.
- W2 corrected one W1 attack claim: `tokens=[the]` did not parse and the `keys=the` control missed, so no generic-held-token bypass was reproduced (`w2/CritC2HeldTokens/held-token-attack.md:9-15`). This is M51-3 / QUALITY 105, not a C2 falsification. The broader token-specificity concern remains a future design question.
- Frontier work: census-before/after, six tier-A rows, one new frontier bullet and mistake mining are in `receipts/census-before.txt`, `receipts/census-after-final.txt`, `corpus/README.md:116`, and `corpus/lessons/round-51.md`. D1 from the round-50 verifier spot-check is M51-1 / QUALITY 103; source-truth overreach is M51-2 / QUALITY 104.
- Assimilation scan and proposal disposition: no separate `merge/mado/` entry was adopted (`w1/ScoutAssim/assimilation-scan.md`); assimilation is none. `considerthese/2026-10-26.md` proposal 2 partially aligns with the inventory, but its last-live-run/verdict freshness component is not implemented (`w1/ScoutConsiderthese/considerthese-row.md`; lesson §Gate). The absent-defect-register mado slice has 13 `unverifiable` rows; no rows were appended and adoption remains closed (`w1/ScoutQuarantine/quarantine-verdicts.md`).
- Inherited `.ufo/wakes` (388 B scratch note) was removed at round start, addressing round-50 spot-check D3. No earlier `lane-dead-no-report mado round=51` line was present at launch. The required pre-report fleet sweep found `M scripts/hyaku/inline-dispatcher.py` and `?? .scratch/closure-mado-r50.json`; neither is a round-51 seat misroot (the latter is orchestrator-owned scratch), so both were left untouched. The round-50 verifier spot-check was read-only.
- `Stale-lane: respawn-per-round driver; no other mission of this lane is open.`

## Landed changes

All entries below are recorded under the Round 51 LOG entry (`LOG.md:2563-2586`); each commit is the lane-helper verified landed hash.

| Change | Commit |
|---|---|
| Claims freeze, census-before receipt, remove inherited `.ufo/wakes` | `d2740281` |
| W1 spec/dispatch evidence | `3ac31642` |
| W1 results, freeze registration, ledger/checker/counters, ledger table and pins | `56026fcb` |
| Dispatcher entry, S364-S369 rows, index/frontier, initial lesson and QUALITY 103 | `a0e34387` |
| W2 spec and dispatch; W2 ready marker | `6366c314`, `caf52271` |
| Append-only source-truth errata | `b742d54c` |
| W2 reports/results; M51-2, QUALITY 104 and scorecard integration | `485bdfd4` |
| Additional recorded changes: interim scorecard, C1/C2 receipts, C2 lesson measurement, PROVINCE inventory | `22ab80bc`, `f2a612ae`, `ad578633`, `58f4d4fc` |
| Final counters/index/census/WAVE-DONE receipts; final LOG/scorecard/lesson/QUALITY records and commit map | `2b1e337a`, `ed84051d`, `a4e13d98` |
| Correct W1 held-token attack overclaim; M51-3 / QUALITY 105; registration correction | `bb32ee29` |

The final lane hash is `bb32ee29761cf49f0104383c080b925c8706eac0`; `jj-lane.sh state` reports local=remote, ahead=0, and `git ls-remote origin refs/heads/master` returns this hash. Final WAVE-DONE recheck at this hash: w1 43/43, w2 33/33, `waves=2 settled=2 verdict=OK`, exit 0.

## Before → after measurements

- **C1 — operability/capability, PRED-C1-r51.** Counting command: `python3 -I quality/counters/c1-r51-ledger.py --repo . --rev <rev> --work <scratch>`. At base `6ca8c559a4a3d6d361101592116eea2bc7452437`: `ledger=absent population=79 verdict=TARGET_MISSED`, exit 1 (`w1/ExecLedgerCounter/receipts/base-and-setup.txt`). At integration revision `485bdfd4159cfad0434eba851f744f076b54ccc2`: `population=82 ledger_rows=82 uncovered=0 dangling=0 bad_pointer=0 empty_desc=0 selftest=ok verdict=TARGET_MET`, exit 0 (`receipts/c1-at-integration.txt`). Checker selftest: 50/50. Bounded claim rubric 0/1→1/1; score delta +10.0000 on this finite capability measure. The frozen predicate is literal; self-pointer and generic-description passes mean the result is not proof of contextual accountability.
- **C2 — coverage/sourced, PRED-C2-r51.** Counting command: `TMPDIR=<scratch> python3 -I quality/counters/c2-r51-dispatch-entry.py --repo . --rev <rev> --work <scratch>`. At base `6ca8c559a4a3d6d361101592116eea2bc7452437`: entry absent, `admitted=0/1 verdict=TARGET_MISSED`, exit 1 (`w1/ExecCounterC2/receipt-base.txt`). At corrected integration revision `485bdfd4159cfad0434eba851f744f076b54ccc2`: `clauses=abcd clauses_met=4 admitted=1/1 verdict=TARGET_MET`, exit 0, 3,364 body shingles and 0.1% maximum overlap (`receipts/c2-at-integration.txt`). Index at the same revision: 67/67, missing=0, dangling=0, duplicates=0, exit 0 (`receipts/index-final.txt`). Bounded frontier rubric 0/1→1/1; score delta +10.0000 on this finite surface measure. The predicate is lexical/structural, not a semantic truth oracle.

## Sources & frontier

Census command at both boundaries: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`.

Before: 300 source rows; exit 0. Full output is committed at `.ufo/waves/round-51/receipts/census-before.txt`; it records the existing W01 S277 tier warning and W04 duplicate-URL-across-scopes warnings.

```text
mado W04 S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado W04 S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado W04 S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado W04 S097 duplicate url raw.githubusercontent.com/basecamp/omarchy/v3.8.4/themes/matte-black/colors.toml across scopes
mado W04 S119 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Lib/imaplib.py across scopes
mado W04 S120 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado W04 S121 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado W01 S277 tierC mined used-by=corpus/knowledge/request-socket-live-bound-r8.md
mado W04 S303 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado W04 S307 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado W04 S317 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado W04 S318 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/values/ConfigValues.cpp across scopes
mado W04 S320 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado W04 S321 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/helpers/MiscFunctions.cpp across scopes
mado W04 S324 duplicate url raw.githubusercontent.com/hyprwm/hyprlang/v0.6.8/src/config.cpp across scopes
mado W04 S326 duplicate url raw.githubusercontent.com/Vladimir-csp/xdg-terminal-exec/v0.14.3/xdg-terminal-exec across scopes
mado W04 S327 duplicate url raw.githubusercontent.com/Vladimir-csp/xdg-terminal-exec/v0.14.3/README.md across scopes
mado W04 S332 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/desktop/rule/matchEngine/RegexMatchEngine.cpp across scopes
mado W04 S353 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado W04 S354 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/managers/input/InputManager.cpp across scopes
mado ok /home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
EXIT=0
```
 
After: 306 rows; exit 0. Full output is committed at `.ufo/waves/round-51/receipts/census-after-final.txt`; it retains the pre-existing warnings and reports W04 warnings for S364, S366 and S368 (duplicate URL across scopes), not validation errors.



```text
mado W04 S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado W04 S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado W04 S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado W04 S097 duplicate url raw.githubusercontent.com/basecamp/omarchy/v3.8.4/themes/matte-black/colors.toml across scopes
mado W04 S119 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Lib/imaplib.py across scopes
mado W04 S120 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado W04 S121 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado W01 S277 tierC mined used-by=corpus/knowledge/request-socket-live-bound-r8.md
mado W04 S303 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado W04 S307 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado W04 S317 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado W04 S318 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/values/ConfigValues.cpp across scopes
mado W04 S320 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado W04 S321 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/helpers/MiscFunctions.cpp across scopes
mado W04 S324 duplicate url raw.githubusercontent.com/hyprwm/hyprlang/v0.6.8/src/config.cpp across scopes
mado W04 S326 duplicate url raw.githubusercontent.com/Vladimir-csp/xdg-terminal-exec/v0.14.3/xdg-terminal-exec across scopes
mado W04 S327 duplicate url raw.githubusercontent.com/Vladimir-csp/xdg-terminal-exec/v0.14.3/README.md across scopes
mado W04 S332 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/desktop/rule/matchEngine/RegexMatchEngine.cpp across scopes
mado W04 S353 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado W04 S354 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/managers/input/InputManager.cpp across scopes
mado W04 S364 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/managers/KeybindManager.cpp across scopes
mado W04 S366 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado W04 S368 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado ok /home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
EXIT=0
```

Rows added by tier: A=6 (S364-S369); B=0; C=0. Existing row status/recheck/used-by changes: none. Frontier advanced by one `corpus/README.md` bullet (dispatcher execution; row at line 116); no runtime key press, socket request or UI effect is claimed. Assimilation: none. Considerthese proposal 2 was partially aligned; the live-run freshness component remains open. Quarantine: 13 rows remain unverifiable; no sourced rows were appended for them.

## Trend verdicts

- **Expansion — improved (narrowly).** One indexed, sourced dispatcher-execution entry was added on ground not held by the round-50 key-match entry; six opened tier-A rows S364-S369 support it (`corpus/README.md:78,116`; `SOURCES.md:313-318`; C2 receipt). No runtime behavior is claimed.
- **Quality — unprovable-but-better.** W2 source review found initial overclaims; append-only errata and QUALITY 104 were added, and the corrected entry still meets the unchanged counter. The corrected prose has no outside non-author review, while C1's lexical pointer and C2's semantic-sufficiency limits remain; therefore an unqualified quality improvement is not asserted (`w2/RevC2EntryTruth/entry-truth.md`; entry `## Errata`; lesson M51-2).
- **Discernment — unprovable-but-better.** The internal falsification wave caught the source-truth overreach and corrected the W1 non-reproducing held-token attack claim (M51-2/M51-3; QUALITY 104/105). These seats are still the lane, and no independent non-author admit/reject spot-check of the corrected entry was performed; outside discernment remains unestablished.

## SHONEN

[~] SKILL.md contains decision tables, error patterns and checklists — `corpus/knowledge/executor-test-sufficiency.md` (MADO-R3-4).
[~] End-to-end domain task executed and logged — `corpus/knowledge/config-health-report-r3.md`; `LOG.md` round 3 (VER-M3).
[~] Instructions executable without oral context — `corpus/knowledge/executor-test-sufficiency.md` (MADO-R3-4).
[~] No cross-domain bleed; PROVINCE accurate — `corpus/knowledge/province-accuracy-selfaudit.md` round-5 receipt (VER-M4B); `PROVINCE.md` boundary remains read-only.

Tool installs/upgrades: none (RULES.md read; pacman remained paused). Open L0 questions: none filed this round.
