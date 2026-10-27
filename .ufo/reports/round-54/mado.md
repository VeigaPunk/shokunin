# mado — round 54 (attempt 2)

## Work performed

Declared claims: **C1 — operability/capability**, an r53 errata source-truth verifier; **C2 — coverage**, an admitted `uwsm-app` environment entry on the owned launcher chain. Both are reported as honest stops; their frozen predicates and targets were not changed after dispatch.

- Re-read the inherited freeze, source pins, lane state, prior verifier spot-check and canonical protocol. The claim/registration/pin bundle eventually landed as `350d30e4ec5531f65ce99a57efeb8216f38e678a`. W1 evidence records launch/ready at 14:05:25/14:05:28 and this freeze commit at 14:11:10, so the freeze was not committed before launch (`.ufo/waves/round-54/w1/R54Seat08.md`, F1; `R54Seat31.md`, dispatch timestamps). This repeats the M53-4 class; no post-score re-registration was attempted.
- L1 held the canonical planner seat. Two validated v1 waves settled: **w1 37 + w2 32 = 69 seats**. W1 role mix: executor 10, scribe 7, scout 4, reviewer 7, critic 3, mutation-tester 2, connector 2, sentinel 1, simplifier 1; attack share 12/37. W2 role mix: reviewer 11, critic 10, mutation-tester 6, scout 3, connector 2; attack share 27/32. Both waves have results files and WAVE-DONE handoffs; no dead seats. Three terminal seat outputs have no assigned report sidecar (`R54Seat06`, `R54Seat19`, `R54W2Seat06`); their outputs remain in the result JSON, and no reports were fabricated.
- W1 falsified the C1 quote judge as written: exact byte matching yields 1/4, while whitespace-collapsed matching yields 4/4; the frozen registration does not consistently authorize that normalization (`w1/R54Seat01.md` F1; `R54Seat02.md` F1; `w1/R54Seat29.md` B29-5). The pinned P19 prose is also contradicted by the adjacent `else` branch sending a PRESSED key (`w1/R54Seat28.md` F2; round-52 pin `fetch/Hyprland-ConfigActions.cpp:1566-1569`). W1/W2 further found control self-attestation and hash/pin-laundering gaps (`w1/R54Seat17.md`; `w2/R54W2Seat11.md`). The incomplete L1 C1 stub was removed; no counter was landed.
- W1 falsified C2's source and host-join basis: S375's frozen locator omits line 119; S376's registered quote omits scdoc emphasis; S375/S377 describe adjacent systemd manager/unit ground; the registered autostart range conflicts with the opened file (`w1/R54Seat08.md`, F3/F7; `w1/R54Seat09.md`, F1-F5; `w1/R54Seat26.md`, S26-1–3). The candidate knowledge entry was withdrawn and README row/frontier promotion removed. S375/S377 remain rejected and S376 is mined only for the narrow client-transport fact in the lesson.
- Re-opened the pinned uwsm sources and static host declarations; recorded exact URLs, access date and located quotes in `corpus/lessons/round-54.md` Gate. No host runtime, package, compositor or service probe was run.
- No shokuknow package entry or considerthese proposal was adopted; no tool was installed or updated.

## Landed changes

- Frozen round evidence and w1 dispatch: `350d30e4ec5531f65ce99a57efeb8216f38e678a` (helper `landed` line). The commit timing defect is disclosed above and in `corpus/lessons/round-54.md` M54-2/M54-4.
- Wave specs, dispatches, registries, terminal results, reports, census receipts, sources registry, lesson, round log and scorecard: final lane content/measurement commits `9ea87392857d26ae023512979ea1bea8b66bbb61` and `fe03bb3b2ec05fbf906b83096c637fd6a05b3dc8`; all are tied to `LOG.md` round 54. Cited round files are under `.ufo/waves/round-54/`.
- Three opened tier-A SOURCES rows were retained as two rejections and one narrow mined lesson citation; old→new status/`used-by` transitions are recorded in `corpus/lessons/round-54.md`. No knowledge entry/capability was admitted.

## Before → after measurements

- **C1 — operability/capability.** At base `e25149fec8152a3aabd2b18a0ee8663b23cf65aa`, the r54 counter count is 0; at measured content revision `9ea87392857d26ae023512979ea1bea8b66bbb61`, it remains 0. Counting command: `git -C . ls-tree -r --name-only <rev> quality/counters | awk 'index($0,"c1-r54-errata-truth.py"){n++} END{print n+0}'` → `0` before / `0` after. No production counter predicate was run; W1 scratch prototypes are evidence of the ambiguity, not landed claim measurements. **Verdict: unprovable / honest stop; score delta 0.**
- **C2 — coverage.** The frozen entry count is 0 at base and 0 at measured content revision `9ea87392857d26ae023512979ea1bea8b66bbb61`. Counting command: `git -C . ls-tree -r --name-only <rev> corpus/knowledge | awk 'index($0,"uwsm-app-environment-r54.md"){n++} END{print n+0}'` → `0` before / `0` after. The candidate was withdrawn; no `admitted=1/1` counter result exists. **Verdict: unprovable / honest stop; coverage score delta 0.**
- No capability row entered. `bash tools/mado-verify.sh --selftest` → `MADO_SELFTEST: 460/460 assertions passed`, exit 0 at content revision `9ea87392857d26ae023512979ea1bea8b66bbb61`.

## Sources & frontier

`corpus/SOURCES.md`: **311 → 314 rows**, three tier-A sources opened this round; S375/S377 rejected, S376 mined by the lesson only. Final statuses and `used-by` transitions are in `corpus/lessons/round-54.md`. No existing-row `recheck` change. The `uwsm-app` environment remains open frontier; no new knowledge entry or frontier ground moved into core. **Assimilation: none** — no `merge/mado/` entry or considerthese proposal was adopted.

Counting command at start and end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`

Before output (full receipt `.ufo/waves/round-54/receipts/census-before.txt`):
```text
mado	W04	S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado	W04	S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S097 duplicate url raw.githubusercontent.com/basecamp/omarchy/v3.8.4/themes/matte-black/colors.toml across scopes
mado	W04	S119 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Lib/imaplib.py across scopes
mado	W04	S120 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W04	S121 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W01	S277 tierC mined used-by=corpus/knowledge/request-socket-live-bound-r8.md
mado	W04	S303 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S307 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S317 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S318 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/values/ConfigValues.cpp across scopes
mado	W04	S320 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S321 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/helpers/MiscFunctions.cpp across scopes
mado	W04	S324 duplicate url raw.githubusercontent.com/hyprwm/hyprlang/v0.6.8/src/config.cpp across scopes
mado	W04	S326 duplicate url raw.githubusercontent.com/Vladimir-csp/xdg-terminal-exec/v0.14.3/xdg-terminal-exec across scopes
mado	W04	S327 duplicate url raw.githubusercontent.com/Vladimir-csp/xdg-terminal-exec/v0.14.3/README.md across scopes
mado	W04	S332 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/desktop/rule/matchEngine/RegexMatchEngine.cpp across scopes
mado	W04	S353 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S354 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/managers/input/InputManager.cpp across scopes
mado	W04	S364 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/managers/KeybindManager.cpp across scopes
mado	W04	S366 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S368 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S370 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/DispatcherTranslator.cpp across scopes
mado	W04	S371 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/shared/actions/ConfigActions.cpp across scopes
mado	W04	S373 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/managers/KeybindManager.cpp across scopes
mado	ok	/home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
```
Exit code: 0 (full receipt: `.ufo/waves/round-54/receipts/census-before.txt`).

After output (full receipt `.ufo/waves/round-54/receipts/census-after.txt`):
```text
mado	W04	S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado	W04	S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S097 duplicate url raw.githubusercontent.com/basecamp/omarchy/v3.8.4/themes/matte-black/colors.toml across scopes
mado	W04	S119 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Lib/imaplib.py across scopes
mado	W04	S120 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W04	S121 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W01	S277 tierC mined used-by=corpus/knowledge/request-socket-live-bound-r8.md
mado	W04	S303 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S307 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S317 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S318 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/values/ConfigValues.cpp across scopes
mado	W04	S320 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S321 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/helpers/MiscFunctions.cpp across scopes
mado	W04	S324 duplicate url raw.githubusercontent.com/hyprwm/hyprlang/v0.6.8/src/config.cpp across scopes
mado	W04	S326 duplicate url raw.githubusercontent.com/Vladimir-csp/xdg-terminal-exec/v0.14.3/xdg-terminal-exec across scopes
mado	W04	S327 duplicate url raw.githubusercontent.com/Vladimir-csp/xdg-terminal-exec/v0.14.3/README.md across scopes
mado	W04	S332 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/desktop/rule/matchEngine/RegexMatchEngine.cpp across scopes
mado	W04	S353 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S354 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/managers/input/InputManager.cpp across scopes
mado	W04	S364 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/managers/KeybindManager.cpp across scopes
mado	W04	S366 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S368 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S370 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/DispatcherTranslator.cpp across scopes
mado	W04	S371 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/shared/actions/ConfigActions.cpp across scopes
mado	W04	S373 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/managers/KeybindManager.cpp across scopes
mado	ok	/home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
```
Exit code: 0.

## Trend verdicts

- **expansion: unchanged** — no admitted knowledge entry on the uncovered uwsm-app environment frontier.
- **quality: harmed** — the r53 P19 proposition remains uncorrected despite a pinned adjacent branch contradicting its “only when” statement; M54-5 records the defect.
- **discernment: unchanged** — no outside-lane admit/reject review was available at report time; dispatched seats are lane authors. The closure spot-check remains pending.

Stale-lane: respawn-per-round driver; no other mado mission is open. Tooling: no installs or updates. Open L0 questions: none.

## SHONEN

- [~] SKILL.md has domain tables, error patterns and checklists — `SKILL.md:47-159`; author assertion, no non-author promotion verification.
- [~] End-to-end desktop task — historical `corpus/knowledge/config-health-report-r3.md` and `LOG.md` round 3; no new independent verification.
- [~] Instructions executable without oral context — `corpus/knowledge/executor-test-sufficiency.md`; no outside-lane verification in this round.
- [~] Province boundary — `PROVINCE.md:1-16` and `corpus/knowledge/province-accuracy-selfaudit.md`; no outside-lane promotion verifier.
