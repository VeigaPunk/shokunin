# mado — round 66 (2026-11-03)

## Work performed

Declared **C1 calibration — register structural discrimination** and **C2 operability — landing child-status discrimination**. Both bounded numeric targets met; admission is left to the non-author closure because the chronology, control-construction ambiguity and compatibility restriction below remain disclosed.

- C1: new Git-object-only register successor checks heading/group uniqueness, row-local receipts and the exact live receipt. Baseline 1/4 → candidate 4/4; selftest 15/15. It does **not** verify state-cell truth. Evidence: `mado-shokunin/.ufo/waves/round-66/measurement-c1-after.txt` and `corpus/lessons/round-66.md` M66-2.
- C2: standing script now requires explicit round scope and distinguishes GREEN/0, genuine RED/1 and ERROR/2. Final committed run: four cases 4/4, selftest 58/58, extracted driver TARGET_MET, real four-leg GREEN. Evidence: `mado-shokunin/.ufo/waves/round-66/measurement-c2-after.txt` and its `measurement-evidence/c2-after/candidate/driver/` logs.
- Frontier: admitted S435 as scoped Bash exit-status documentation, mined mistakes M66-1..M66-6, added QUALITY 108 and registered the instruments in SKILL. No knowledge entry or desktop frontier promotion. Evidence: `corpus/SOURCES.md`, `corpus/QUALITY.md`, `corpus/lessons/round-66.md` in the lane.
- One validated v1 wave, **12 seats**, all settled; WAVE-DONE received before report. Roles: 4 executor, 2 scribe, 1 each scout/connector/reviewer/critic/mutation-tester/sentinel. Attack share 3/12=25%; one connector; planner is L1; residual calls 0; dead seats 0. Evidence: `.ufo/waves/round-66/{w1-spec.json,w1-results.json,wave-settlement.txt,wave-done-final-r66.txt}` in the lane.
- No host/config/service/compositor writes, screenshot capture, credential inspection or installs. Misroot sweep found no attributable mado file; unrelated `.scratch`, sibling reports and unattributed fleet-root `after` were left untouched. Evidence: lane `.ufo/waves/round-66/misroot-disposition-r66.txt`.

### Explicit limitations and conformance

1. Freeze commit followed registry/ready; the executable do-nothing baseline ran after freeze. Neither chronology condition is claimed passed. Evidence: lane `.ufo/waves/round-66/process-defects.txt`.
2. Frozen text remembered `MADO_TOOL_LEDGER`; actual child marker is `LEDGER:`. Named erratum, no fabricated alias: lane `.ufo/waves/round-66/marker-premise-erratum.md`.
3. C1's file-plane-only control omits the live receipt object. A stronger PROVINCE-only forgery retaining that object still passes; false state cells with valid receipts also pass. The construction choice was clarified after draft scoring. No claim that the stronger prior forge is fixed. Evidence: lane `w1/R66RevRegister.md` under this round.
4. C2 now refuses explicit citation paths outside the repository so dirty checking is consistent. This is a disclosed restriction versus r65, not backward compatibility; closure must judge the preserve-behavior/no-harm condition. Shared ledger/citation bookkeeping also couples landing order, although neither feature invokes the other. Evidence: lane `SKILL.md` round-66 section and `w1/R66ConnSiblings.md`.
5. Final mutation denominators: C1 4/5, C2 8/10 killed by the frozen subset; replacement-ref safety and zero-citation positivity need auxiliary probes. No universal fault-coverage claim. Evidence: lane `w1/R66MutHardening.md` and its retained JSON receipts.
6. Routing was delegated without any model parameter or configuration edit. End-of-round operator config shows executor/reviewer @m_zfl and scout/critic @m_flash, differing from the prompt's mandated scout @m_antigravity. Captured spawn/answering-model attestation was requested but not received; the mandated model mix is **not asserted**. Evidence: lane `.ufo/waves/round-66/route-observation.json`. No routing override or replacement wave was attempted.

Stale-lane: respawn-per-round; no other mission of this lane is open. Existing r57/r58/r59 rubric and r60 capture-scope L0 questions remain operator-owned; no waiver is inferred. Tool installs/updates: none; pacman pause honored.

## Landed changes

Every row is tied to `mado-shokunin/LOG.md` **Round 66** and its committed-measurement subsection.

| Landed commit | Changes |
|---|---|
| `ed980316e330703030d0c17b2a7098e058295b99` | Frozen declaration and validated wave dispatch |
| `043b9af13c0af23e5ee7d48e8cda00e6d3207ad9` | Register successor, hardened standing script, extracted driver, ledger/docs/lesson, S435 and seat evidence |
| `739a01c5191a1b5bb21ef2a5f7792aab6e152328` | Settled wave results/receipt; **measured content revision** |
| `ecfc8ac376ea3152d552496b75f5ae059571943f` | Frozen-command outputs, source arithmetic, wave/conformance receipts, SCORECARD results and LOG/lesson addenda |

Final lane `master`: **ecfc8ac376ea3152d552496b75f5ae059571943f**. Pre-report remote command `git -C /home/vgpnk/Projects/shokunin/mado-shokunin ls-remote origin refs/heads/master` printed that exact hash. All cited landed hashes came from successful `jj-lane.sh` helper output. Measurements name the content revision, not an uncommitted worktree.

## Before → after measurements

Run from the lane. `BASE=eafd500fa7be76dca59e729435e231a5032cc037`; `MEASURE=739a01c5191a1b5bb21ef2a5f7792aab6e152328`.

```sh
python3 .ufo/waves/round-66/check-controls.py --repo . --rev "$BASE" --claim c1 --scratch-root /fast/scratch/hyaku/mado-r66/measure
python3 .ufo/waves/round-66/check-controls.py --repo . --rev "$MEASURE" --claim c1 --scratch-root /fast/scratch/hyaku/mado-r66/measure
python3 .ufo/waves/round-66/check-controls.py --repo . --rev "$BASE" --claim c2 --scratch-root /fast/scratch/hyaku/mado-r66/measure
python3 .ufo/waves/round-66/check-controls.py --repo . --rev "$MEASURE" --claim c2 --scratch-root /fast/scratch/hyaku/mado-r66/measure
```

| Claim | Before | After | Verdict |
|---|---|---|---|
| C1 calibration | 1/4 TARGET_MISSED, rc1 | 4/4 TARGET_MET, selftest rc0, rc0 | bounded target met; 2.5/10→10/10 on this finite rubric |
| C2 operability | 1/4 TARGET_MISSED, rc1 | 4/4, selftest rc0, actual extracted driver rc0 TARGET_MET, final rc0 | bounded target met; 2.5/10→10/10; compatibility qualification above |

Full output/exit status: lane `.ufo/waves/round-66/measurement-{c1,c2}-{before,after}.txt`. Baseline is the real r65 instruments; doing nothing cannot meet either target. C2's counted command includes the real driver gate, not draft diagnostic mode.

Actual committed landing at MEASURE: navigation **78/78**, used-by **missing=0**, ledger **108/108**, citations **4/4**, all four rc0. Selftest **58/58**. Raw log: lane `.ufo/waves/round-66/measurement-evidence/c2-after/candidate/driver/c2r66-o52_1j4l.landing.log`; companion selftest log in the same directory. Wave checker: one wave, 12 dispatched/12 settled, OK rc0 (`wave-done-final-r66.txt`). These bounded checks do not establish global no-harm or promotion.

## Sources & frontier

SOURCES **371→372**; tiers A357→358, B7 unchanged, C7 unchanged; mined350→351, queued10/rejected11 unchanged; malformed0 both ends. New row: **S435 A/docs/mined**, canonical GNU Bash Exit Status page, used-by `corpus/lessons/round-66.md`. No existing status/recheck/used-by/opened cell changed. Located ≤25-word quote and access date are in that lesson's Gate.

Counting command (run for BASE and MEASURE):
```sh
python3 .ufo/waves/round-66/count-sources.py --repo . --rev REV
```
Exact invocation/output: lane `.ufo/waves/round-66/sources-shape-r66.txt`.

Census command at both ends:
```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

### Start output

```text
$ scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
mado	W04	S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado	W04	S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S097 duplicate url raw.githubusercontent.com/basecamp/omarchy/v3.8.4/themes/matte-black/colors.toml across scopes
mado	W04	S119 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Lib/imaplib.py across scopes
mado	W04	S120 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W04	S121 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W01	S277 tierC mined used-by=corpus/knowledge/request-socket-live-bound-r8.md, corpus/knowledge/request-limits-upstream-r31.md
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
mado	W04	S380 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/devices/IKeyboard.hpp across scopes
mado	W04	S381 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/protocols/core/Seat.cpp across scopes
mado	W04	S382 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/devices/IKeyboard.hpp across scopes
mado	W04	S384 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/values/ConfigValues.cpp across scopes
mado	W04	S387 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S388 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/helpers/MiscFunctions.cpp across scopes
mado	W04	S389 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S392 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/shared/inotify/ConfigWatcher.cpp across scopes
mado	W04	S393 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/helpers/MiscFunctions.cpp across scopes
mado	W04	S394 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S395 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	ok	/home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
exit=0
```

### End output

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
mado	W04	S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado	W04	S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado	W04	S097 duplicate url raw.githubusercontent.com/basecamp/omarchy/v3.8.4/themes/matte-black/colors.toml across scopes
mado	W04	S119 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Lib/imaplib.py across scopes
mado	W04	S120 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W04	S121 duplicate url raw.githubusercontent.com/python/cpython/v3.14.8/Doc/reference/executionmodel.rst across scopes
mado	W01	S277 tierC mined used-by=corpus/knowledge/request-socket-live-bound-r8.md, corpus/knowledge/request-limits-upstream-r31.md
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
mado	W04	S380 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/devices/IKeyboard.hpp across scopes
mado	W04	S381 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/protocols/core/Seat.cpp across scopes
mado	W04	S382 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/devices/IKeyboard.hpp across scopes
mado	W04	S384 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/values/ConfigValues.cpp across scopes
mado	W04	S387 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	W04	S388 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/helpers/MiscFunctions.cpp across scopes
mado	W04	S389 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S392 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/shared/inotify/ConfigWatcher.cpp across scopes
mado	W04	S393 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/helpers/MiscFunctions.cpp across scopes
mado	W04	S394 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/debug/HyprCtl.cpp across scopes
mado	W04	S395 duplicate url raw.githubusercontent.com/hyprwm/Hyprland/efb50993780079460b0cbed1363e2166a2de1d9f/src/config/legacy/ConfigManager.cpp across scopes
mado	ok	/home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md

exit=0
```

Both exit0; 37 pre-existing warnings remain. A mid-integration missing-lesson E11 was observed and cleared by landing the lesson, not suppressed (`w1/R66ScribeSources/census-post-integration-r66.txt` in the lane). Sourced claim is **C2**: S435 grounds exit-status vocabulary, not marker authenticity. C1 has no external truth-binding source.

Frontier rows advanced: **none**. Knowledge entries added: **0**. Assimilation: **none**; connector screened the package/considerthese fit without adopting a theme into these claims. Python return-code documentation was opened but not selected, not judged false. Reject: structural marker/receipt checks prove state truth or honest invocation; flip requires independently authenticated observation. No fresh outside-lane admit/reject spot-check is claimed. Prior art is attributed to kumitate NO_CHILD, tsukuroi could-not-evaluate and tameshi ARM_DEAD; no cross-domain implementation was absorbed.

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry, frontier move or desktop surface.
- **quality: improved on the bounded instruments** — both finite controls improve 1/4→4/4, real committed landing GREEN and source census exit0; compatibility restriction and proof limits remain for closure's no-harm judgment.
- **discernment: unchanged pending fresh outside sample** — prior routed defects were mined into QUALITY 108, but this lane's seats do not supply independent admit/reject or promotion clearance.

## SHONEN

- [~] Tables, patterns and cited instructions: lane `SKILL.md`; historical `corpus/knowledge/executor-test-sufficiency.md`; no new non-author promotion verifier.
- [~] Historical end-to-end domain task: lane `corpus/knowledge/config-health-report-r3.md`, LOG round3; this round executes lane record checks, not a new desktop task.
- [~] Executable instructions: lane `SKILL.md` round66, committed measurement commands/logs; dispatched seats remain authoring-lane evidence.
- [~] Province boundary: lane `PROVINCE.md` round66 read-only instrument inventory; no outside-lane promotion attestation.
