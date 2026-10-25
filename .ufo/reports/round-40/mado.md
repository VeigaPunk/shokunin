# mado — round 40 report (hyaku run 7, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash **`fb49621074518333d855a2664ba5884c381079ad`** (`git ls-remote origin refs/heads/master` prints it). Round shape: one v2 wave `w1`, **64 seats** (executor 20, scribe 12, reviewer 8, scout 6, connector 5, critic 4, mutation-tester 4, sentinel 2, revenger 2, simplifier 1), no residual call, **round total 64**; no second wave ran (request budget). Planner seat held by the L1. Dead seats: none dead; one report misrouted (`ConnCrossClaim` wrote to `.ufo/waves/round-49/…`, absent; its returned text is in `w1-results.json`; lesson M40-6).

## Work performed

Declared claims: **C1 operability (capability acquisition)** — `tools/mado-options.py --live`; **C2 coverage (sourced)** — `corpus/knowledge/hyprctl-getoption-native-forms-r40.md`.
- Freeze `5e7e88525cc539563de7746361b2650802e81809` (v1 predicates, controls, base receipts); wave `w1` spec/dispatch `e2b51d3`.
- **The wave falsified the v1 predicates before any data**: a 204-line tool with no conversion scored 13/13 by exec'ing the counter's model (`w1/CritC1Cheat.md`), a forged call log, an echo selftest, seed replay, a fifth native form `vec2` (6 of 353 options; `w1/ExecAllOptionsForms.md`), a critical `x/--batch` key injection (`w1/SentLiveVerbs.md`), a 1.4 kB fabrication admitted by C2 (`w1/CritC2Cheat.md`). The L1 re-registered as **v2** (`registration-v2.md`, freeze `8122293930f42ea2011e7c2b0b80a297e2ce6cdd`, before any data commit): sandboxed (bwrap) counter with a judge-held fake compositor, per-run nonce, selftest mutation check, `vec2`, security fixtures; C1 controls `CTL_C1V2 57/57`, C2 controls `CTL_C2V2 33/33` (`receipts/ctl-c1-v2.txt`, `ctl-c2-v2.txt`). Honest ordering: two seats had scored a candidate under v1 before v2 existed; v2 is strictly stronger; the operator rules which predicate binds.
- Data commit `91f0a2b8b3d396b23376700ecbad6e8b07f062ee`: delivered tool (byte-identical to the freeze-time reference `c1/ctl-ref-tool-v2.py.txt`, sha256 `63b5ebd9…ef13`, selftest 211/211), the two entries, rows S278–S282, census receipt, lesson, QUALITY 65–68, wave evidence.
- Host finding: gradient angle inheritance (`general:col.active_border` reads `ffe68e0d 45deg`, theme declares one colour; `receipts`/`fetch/census-receipt.txt`); live census 62 agreement / 8 agreement* / 0 mismatch; `set` true for exactly the 70 declared of 353 options.
- Assimilation (bar-producers theme, `merge/mado/`): K1 refused (held), K2 refused as written (five defects, `w1/ScrAssimK2`), re-grounded successor `host-bar-producer-census-r40.md` admitted (rows S280–S282); id guard 214/147/22 collisions, proved on an indented row; quarantine slice 13 rows with verdicts (S224 unverifiable, not fabrication — corrects the round-39 label; S209 no quote exists). considerthese `2026-10-25` proposal 2 mined as a table (lesson).
- Misroot sweep: no stray fleet-root file of this lane observed; `.ufo/state/mado.report-baseline` modified by the driver, not touched.

## Landed changes

| Commit | Change | LOG |
|---|---|---|
| `5e7e885…` | v1 freeze | Round 40 bullet 1 |
| `e2b51d3…` | wave spec/dispatch | bullet 1 |
| `3721d54`, `212d811`, `c96cf6d` | v2 pre-freeze (counters, harnesses, capture, cheats, reference) | bullet 1 |
| `8122293930f42ea2011e7c2b0b80a297e2ce6cdd` | v2 freeze (registration-v2, control receipts, before-measurements) | bullet 1 |
| `91f0a2b8b3d396b23376700ecbad6e8b07f062ee` | data | bullet 2 |
| `3c80537…`, `fb49621074518333d855a2664ba5884c381079ad` | after receipts/census; axis line | bullet 2 |

## Before → after measurements

- **C1** `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c1-r40-live-v2.py --repo . --rev <rev>`: before (base `9fc511d`) `fixtures=0/19 TARGET_MISSED`, exit 1; after at `91f0a2b`: `fixtures=19/19 tool=present verdict=TARGET_MET` nonce `239e2809b1850614`, exit 0 (`receipts/c1-v2-after-data.txt`); reference runs at three other nonces `19/19`. Under the superseded v1 counter the same tool scores `fixtures=13/13` but `TARGET_MISSED` (v1's frozen clause-g allowlist refuses the `struct`/`threading` imports the security repairs added; `receipts/c1-v1-after-data.txt`). Verdict: **met under v2**; v1 not met (clause g) — operator rules.
- **C2** `python3 -I quality/counters/c2-r40-forms-entry-v2.py --repo . --rev <rev>`: before `admitted=0/1`; after `admitted=1/1 TARGET_MET` at `91f0a2b` (v1 counter also `1/1`). Residual: a fabricated self-consistent set passes; admitted=1/1 measures admission wiring.
- Harm watch: `MADO_SELFTEST 460/460`, `MADO_OPTIONS_SELFTEST 211/211` (base 71), index `58/58`, index rows `errors=0`, `MADO_AXIS checked=3 mismatched=0` at `fb49621` (navigation 58/58, calibration 55/55, operability 12/12). The round-39 counter `c4-r39` clause e binds the tool sha at its own rev: measure it at its named rev, not this tip.

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`. Start (`receipts/census-before.txt`): `mado ok`, W04 ×7 + W01 S277, exit 0. End (`receipts/census-after.txt`): identical, `mado ok`, **exit 0**. Rows 214 → 219 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); added tier A +5 (S278 docs, S279 own-work, S280/S281 code, S282 own-work). Touched old→new: used-by +native-forms entry on S158, S162, S173, S180, S181, S215 (re-opened byte-identical). Sourced claim: C2 cites S158/S162/S173/S180/S181/S215/S278/S279. Mined mistakes: M40-1…M40-6. Assimilation: one theme (bar producers), see above. considerthese: `2026-10-25.md` proposal 2.

## Trend verdicts

- **expansion: improved** — new edge classes (native reply forms, `vec2`, angle inheritance), one capability row, two entries, five rows.
- **quality: improved** — the wave's cheats and survivors turned into v2 predicates with 90 controls; but the v1 predicates were wrong and re-registered after seats scored: disclosed, not a clean pass.
- **discernment: improved** — K1/K2 refused with reasons, successor admitted, S224 label corrected, criteria 65–68 each backed by a lesson mistake; non-author spot-check still owed (no second wave).

## SHONEN

- [~] SKILL.md real decision tables — historical (`SHONEN.md:5`); `w1/ScrSkillTable/skill-rows.md` drafted, SKILL.md not edited this round; no outside-lane verifier.
- [~] End-to-end domain task logged — live census of the host option table (`fetch/census-receipt.txt`, LOG.md Round 40); no non-author verifier yet.
- [~] Instructions executable without oral context — `python3 -I tools/mado-options.py --selftest`, `--live`; dispatched seats are not outside verification.
- [~] No cross-domain bleed — gkeep/ai-usage packages kept as chain evidence only (`corpus/knowledge/host-bar-producer-census-r40.md` §4); `ScrProvinceRow` draft not applied to PROVINCE.md.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none by the L1; seats report none.
Open L0 questions: none. Not done (budget): second falsify wave, SKILL.md/PROVINCE.md rows (drafts in `w1/ScrSkillTable`, `w1/ScrProvinceRow`).
