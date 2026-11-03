# mado round 65 — returned host, measured landing checks

## Work performed

Declared claims: **C1 freshness**, eight-group returned-host register re-derivation;
**C2 operability**, a standing four-leg landing instrument (capability acquisition).
Both frozen counters meet their targets; counter weaknesses remain explicitly disclosed.
This is a lane self-verdict, not independent admission.

- Frozen declaration and base controls: `cb63ab13ccaf85191318701d5db5ace050bd5bd4`,
  `.ufo/waves/round-65/claims-declaration-r65.md` and receipts. Base
  `524fa1f90b1f2de44b3019bacf833d54e0af13a0`; no inherited attempt-65 residue.
- C1 appended PROVINCE register, preserved historical Windows rows; live gate
  CLEAN 52 pass; file plane 29 pass; unchanged gate selftest 460/460.
  Evidence: `.ufo/waves/round-65/measurement-final-r65.txt`.
- C2 integrated `quality/landing-counters.sh` and two revision-reading counters;
  ledger 104 → 106. Instrument selftest 19/19; landing GREEN with four rc=0.
- ONE validated v1 wave, w1, 12 seats, all settled before this report (WAVE-DONE).
  Role mix: 4 executor, 2 scout, 2 reviewer, 1 critic, 1 mutation-tester,
  1 scribe, 1 connector. Attack share 4/12; connectors 1; residual calls 0;
  total 12; no dead seats reported. Planner seat: L1. Routing came from host
  overrides, no model parameter. Evidence: `w1-spec.json`, `w1-dispatch.json`,
  `w1.ready.dispatched`, `w1-results.json` under `.ufo/waves/round-65/`.
- Attack findings: C1 accepts forged state cells (reviewer A3); independent
  seat probes reproduced rows, but do not make this a truth-binding counter.
  C2 critic B1/B2/B4 addressed by dirty-receipt refusal, nonempty-citation
  guard, and git-env stripping; B3 by ledger rows. Mutation survivors and
  remaining hermeticity weaknesses are preserved in the lesson and seat reports.
  No universal robustness or independent admission claimed.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  showed only orchestrator-owned `.scratch` state; no mado seat misroots found.

## Landed changes

- `cb63ab13ccaf85191318701d5db5ace050bd5bd4`: freeze and before receipts.
- `c6b8ec301ac54c2c082ad228cbacabecbd15b48e`: register, instruments, ledger,
  source reopened dates, lesson, wave evidence.
- `23fbc174d02fa44662e9aee735bbf6de5cad3f1d`: measured SCORECARD and LOG,
  measurement outputs and honest limitation addendum. Each change is tied to
  `LOG.md` **Round 65**, beginning line 3148.
- Final lane hash above was verified by `git ls-remote origin refs/heads/master`.

## Before → after measurements

Measured content revision: `c6b8ec301ac54c2c082ad228cbacabecbd15b48e`.
Both base controls still MISS at the original base; predicates did not change.

| Claim | Counting command (lane cwd; REV selects base or measured content) | Before → after |
|---|---|---|
| C1 freshness | `python3 quality/counters/c1-r65-register.py --repo . --rev REV` | rows=0 groups=0/8 receipts=0 gate=missing TARGET_MISSED rc=1 → rows=8 groups=8/8 receipts=4 resolved=4 gate=ok TARGET_MET rc=0 |
| C2 operability | `python3 quality/counters/c2-r65-landing-instrument.py --repo . --rev REV --scratch-root /fast/scratch/hyaku/mado-r65/c2` | instrument absent TARGET_MISSED rc=1 → selftest=0 landing=0 green=yes TARGET_MET rc=0 |

Exact outputs: `.ufo/waves/round-65/measurement-final-r65.txt`.
First measurement red is preserved in `measurement-first-r65.txt`: writing the
output inside the receipts scan dirtied that scope. Moving it outside restored
the landing measurement without code changes. C1's dated Windows rows are
preserved, not erased. Re-derived live health is environmental observation,
not a causal repair by this round.

Harm watch: navigation 78/78, used-by missing=0, ledger 106/106,
citations 10/10, fail-closed selftests 54/54 and 62/62, citecheck 12/12,
new instrument 19/19, unchanged gate 460/460. All relevant verdicts green.
Some measurement wrappers for hermetic checker selftests capture tail's rc;
the passing assertion totals are observed, not replaced with fabricated producer rcs.

## Sources & frontier

Registry command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`.
Rows 371 → 371; rows added by tier A/B/C: 0/0/0. Rows touched: S028 opened
2026-10-19 → 2026-11-03; S097 opened 2026-10-20 → 2026-11-03. Recheck cadence
on-release, status mined and used-by are unchanged. Declaration's wrong-column
wording is corrected in lesson M65-4. Gate quotes and access dates are in
`corpus/lessons/round-65.md` and scout `gate-quotes.md`.
Frontier advanced: returned-host observation currency, not new corpus ground.

Assimilation: none — package reachable, no theme fits these frozen claims;
connector screened 69 staged entries / 147 rows, closest surface-state groups
held for re-grounding. No append selection, so no adopted-id collision or renumber map.
Considerthese: nine files unchanged since previous screen; no new adoptable proposal.
Mistakes M65-1–M65-4 and landing-output recursion mined; failure demonstrations
and remaining counter limits recorded in `corpus/lessons/round-65.md`.

Start census (exit 0):
```
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
census-exit=0
```
End census (exit 0):
```
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
```

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry or domain ground admitted;
  register refresh and instrument are quality work, not coverage growth.
- **quality: improved** — standing four-leg instrument demonstrated GREEN;
  source re-opens, returned-host probes, and executable register check landed.
- **discernment: unchanged** — adversarial findings are named, but no new
  independent admit/reject agreement sample exists; forged-cell weakness remains.

Stale-lane: this assignment owns round 65 only; no other mado mission is open here.
L0: r57 freshness/Windows L2 waiver, r58 gate-selftest disposal, r59 calibration
re-derivability and r60 screenshot-scope questions remain operator-owned and open.
Returned Linux host allows this round's dispatch and omarchy remeasurement; it
is not a retrospective waiver or answer. No tool installs or host service changes.

## SHONEN

- [~] Real tables and cited instructions — `SHONEN.md`, `corpus/knowledge/executor-test-sufficiency.md`; no new outside-lane promotion verifier.
- [~] End-to-end domain task — historical `corpus/knowledge/config-health-report-r3.md`; live round-65 gate is not an independent promotion judgment.
- [~] Instructions without oral context — historical executor-test note; dispatched seats are not outside-lane promotion authority.
- [~] No cross-domain bleed — `PROVINCE.md` returned-host register and boundary; no new outside-lane approval.
