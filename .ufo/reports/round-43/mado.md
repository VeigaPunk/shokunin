# mado — round 43 report (hyaku run 8, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash **`58466627de847d6502283c3bb9e652caea97b411`** (`git ls-remote origin refs/heads/master` prints it; `jj-lane.sh state`: `local=remote=58466627… ahead=0 behind=0 tracked=0 untracked=0`). Base `a35cfdfcdeb3bd42d1a2cd960faf22ceac1bef3f` (the round-42 tip). Round shape: **two v1 waves** — `w1` 38 seats (build + first falsifiers) and `w2` 32 seats (falsify the landed data); round total **70**; no residual call; dead seats **0** (one degraded: `w2/ScoutRowsD` returned only its summary). Planner seat: held by the L1 (`MadoR43`); the planning data-walk rode `w1/ScoutStagedGkeep`. Open L0 questions: none. No earlier attempt of round 43 existed (no `lane-dead-no-report mado round=43` line).

## Work performed

Declared claims (round 42's frozen, never-scored claims, re-registered before any data — `.ufo/waves/round-43/registration.md`, freeze `b2e2efd6e268920d31f3c32cf52dc097dd6e1d22`; C2 re-registered again before data as v2 — `registration-v2.md`, freeze `496340dd53fabd800be42e8fb19090f35e2c235c`):
- **C1 — operability (capability acquisition): `tools/mado-geometry.py`**, a read-only join of `windowrule = size W H, match:class RX` lines and one `hyprctl clients -j` dump (AGREE / DIFFER / TILED / BADSIZE), judged by `PRED-C1-r42` unchanged.
- **C2 — coverage (sourced; assimilation of the gkeep-geometry theme of `merge/mado/`): `corpus/knowledge/hyprland-gkeep-geometry-r43.md`**, what sets the host gkeep window's size end to end, judged by `PRED-C2-r43-v2`.

Lowest-axis rule: every published axis tied at its maximum at base (`receipts/axis-base.txt`: navigation 59/59, calibration 63/63, operability 12/12, `MADO_AXIS checked=3 mismatched=0`), so each is a lowest axis. (All receipt paths below are under `mado-shokunin/.ufo/waves/round-43/`.)

- Protocol load done; round-42 closure items routed: locator correction appended as the first bullet of LOG.md Round 43 (`LOG.md:2487`: `Hyprland-HyprCtl.cpp:427-428`/`:448`, `Hyprland-RegexMatchEngine.cpp:7-8`/`:16`); C1 tally stated once with its definition (`registration.md:59-61`); SHONEN box 2 now points at a committed run receipt (`receipts/live-geometry-host.txt`, `verdict=NO_MATCHING_CLIENT`, exit 3); the lesson exists (`corpus/lessons/round-43.md`).
- Pre-wave pins re-fetched 2026-10-26: seven Hyprland files at `efb50993…` byte-identical to round 42; `host-gkeep.conf` identical; `host-clients-r43.json` re-captured; `gkeep-ui-excerpt.py` regenerated because round 42's header claimed lines 446-495 of a 488-line file (`receipts/fetch-sha256.txt`).
- Freeze controls at the round-43 base: `receipts/ctl-c1.txt` `CTL_C1: … controls=46` (REF and BASE-absent are anchors; 3 do-nothing, 5 cheats, 38 mutants), `CTL_C1 VERDICT: PASS (controls scoring TARGET_MET: 0 of 47; reference met: 1)`; `receipts/ctl-c2.txt` `CTL_C2: controls=74 correct=74/74`.
- w1 found the C2 v1 target reachable without the claimed coverage (`w1/CritClaimSizing.md` finding 2: a 17-line entry citing four of ten pins admitted; `w1/CritC2Cheat.md`: 16 forgeries admitted). C2 re-registered as `PRED-C2-r43-v2` before data (all ten pins cited, unique quotes outside comments, true raw URLs, every naming line bound, exact package paths, flip words): `receipts/ctl-c2-v2.txt` 74/74; `ctl/v2-forgeries/forge-v2.log`, `more-v2.log`: P admitted, B1 B2 C1 C2 E1 F1 F2 G1 G2 X2 X3 rejected, claim-binding forgeries A1 A2 D1 E2 H1 X1 still admitted (declared residual). C1 kept as registered (`registration-v2.md` §C1: every w1 cheat that reaches MET carries the full model).
- C1 deliverable: the round-42 reference installed byte-identically (sha256 `e3c2e471…`); falsified by three independent implementations from the contract alone (`w1/ExecIndepA.md`, `ExecIndepB.md`, `ExecIndepC.md`: each 37/37 TARGET_MET), mutation (`w1/MutRefSelftest.md`, `ExecC1ExtraMutants.md`, `MutC1CounterGates.md`), RE2 differential fuzz (`LabRe2Fuzz.md`: 466,189 pairs, 0 engine divergences), and security seats (`w1/SentReDoS.md`, `w1/RevRefTool.md` V1: backtracking hang on `(a|aa)+$` — documented in SKILL.md with a `timeout 5` guard, tool unchanged).
- C2 deliverable built from w1 drafts (`w1/ScrEntryA`, `ScrEntryB`, `ScrRowsDraft`, `ScrLessonSkeleton`, `ExecSrcChain`); the drafts' S291/S296 rows were dropped because their commit-form URLs already belong to held S155/S158, which the entry cites instead (receipts are the pinned bytes). Isolated-oracle observation added (`w1/ExecOracleGkeep/20-observation.txt`: `"size": [420, 500]`, `"floating": true` for app id `org.omarchy.gkeep` in a nested Hyprland 0.56.2, with size/float controls).
- Frontier-step fix shown able to fail: `quality/check-locators.py` (from `w1/ExecLocatorGate`): `w1/ExecLocatorGate/receipt.txt:60-61` `verdict=MISS … miss=1` on round 42's LOG bytes; it then caught the L1's own first draft (four single-line locators for two-line quotes, M43-7) and a wrong SKILL locator.
- w2 re-ran every counting command and agreed (`w2/RerunC1Data.md`, `w2/RerunC2Data.md`, `w2/RerunControlsV2.md`, `w2/RerunCensus.md`), confirmed separability both ways (`w2/ExecSeparability.md`), no harm (`w2/ExecHarmTip.md`), 0 calibration mismatches (`w2/ConnCalibration.md`); its content attacks led to the correction commit `875001662c69feeefa98699883da67de1bdb56ac` (entry tiled/pseudo path — `w2/CritEntryInf.md` F1, first-map scope F2, oracle scope `w2/CritOracleClaim.md`, the `setBox` link `w2/CritAssimilation.md` F2; r30 refusal withdrawn F1; SKILL TILED row and support ceiling `w2/CritC1Capability.md` F3; PROVINCE `--selftest` sentence `w2/SentLiveRun.md` F3; lesson fixes `w2/RevLesson.md`).
- considerthese: `considerthese/2026-10-25.md` proposal 2 ("count dead attempts and dirty closures") landed as QUALITY criterion 81 with its re-runnable check (`w1/ScrConsiderthese/check78.sh`; `w2/ScribeClosureTable.md`: `TALLY rounds=7 launches=8 dead=1 complete=7 clean=3 dirty=4 relayed=7`, `TABLE_COMPLETE`, exit 0).

## Landed changes

| Commit | Change | LOG.md Round 43 bullet |
|---|---|---|
| `b2e2efd6e268920d31f3c32cf52dc097dd6e1d22` | freeze: registration, `quality/counters/c2-r43-gkeep-entry.py`, C2 controls, pins, before/control receipts | 2 (Freeze) |
| `5add5b45a65ddaa18fad00c6afa9dbfda29ee0b0` | w1 spec, dispatch, registry (38 seats) | 3 (Wave w1) |
| `496340dd53fabd800be42e8fb19090f35e2c235c` | C2 v2 freeze before data: counter v2, controls v2, forgery receipts, `registration-v2.md` | 5 (w1 findings) |
| `1959770657f1f8665097c1aed4be6c1cbb07139f` | **data**: `tools/mado-geometry.py`; entry; rows S290-S297; S155/S158 used-by; lesson; README index + Frontier; PROVINCE/SKILL rows; QUALITY 77-81; `quality/check-locators.py`; live host receipt | 6 (Data commit) |
| `a47efeb37d61ea6ec7fe7c12887ff4a94e674d2b` | after-data receipts; w2 spec/dispatch (32 seats) | 6 |
| `2a3707c83d55eb1333e1bf6ff1c5c38001c11eaa` | w1 evidence (38 reports, results), assimilation receipts, SKILL ReDoS note, SCORECARD Round 43 + axis publication, LOG | 1-8 |
| `875001662c69feeefa98699883da67de1bdb56ac` | w2 corrections (entry, lesson post-data corrections + M43-9, SKILL, PROVINCE) | 9 (Wave w2) |
| `58466627de847d6502283c3bb9e652caea97b411` | w2 evidence (32 reports, results), tip receipts, SCORECARD w2 outcome, handoff markers (lane tip) | 9 |

Inherited state: none (tree clean at start). The stray `.ufo/waves/round-43/LabRe2Fuzz.md` (a later revision of `w1/LabRe2Fuzz.md` a seat wrote one directory up) was committed as found.

## Before → after measurements

- **C1** — `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c1-r42-geometry.py --repo . --rev <rev>`: base `a35cfdf` `PRED-C1-r42: fixtures=0/37 tool=absent verdict=TARGET_MISSED`, exit 1 (`receipts/c1-before-base.txt`) → data commit `1959770` `fixtures=37/37 tool=present verdict=TARGET_MET`, exit 0 (`receipts/c1-after-data.txt`) → tip `8750016` same, exit 0 (`receipts/c1-after-tip.txt`); re-run at the final tip `5846662`: `fixtures=37/37 tool=present verdict=TARGET_MET`. Self-verdict **TARGET_MET**. Open predicate defects: w1 `CritC1Cheat` cheats 4 (source-pin selftest) and 6 (sandbox detection) reach MET; the TILED verdict's premise is false for pseudo-tiled windows (`w2/CritEntryInf.md` F1). Provenance: the tool is the round-42 reference installed byte-identically.
- **C2** — `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c2-r43-gkeep-entry-v2.py --repo . --rev <rev>`: base `PRED-C2-r43-v2: admitted=0/1 verdict=TARGET_MISSED`, exit 1 (`receipts/c2-v2-before-base.txt`) → data commit `admitted=1/1 verdict=TARGET_MET`, exit 0 (`receipts/c2-after-data.txt`; v1 `PRED-C2-r43` also 1/1, `receipts/c2-v1-after-data.txt`) → tip `8750016` `admitted=1/1`, exit 0 (`receipts/c2-after-tip.txt`); final tip `5846662` `admitted=1/1 verdict=TARGET_MET`. Self-verdict **TARGET_MET under v2**, with an honest limit: w2 `ExecDoNothingV2` shows 14 of 14 shape-keeping do-nothing controls (the landed entry plus or minus prose) admitted and `MutC2V2` 6 of 16 weakening mutants surviving every control — v2 scores the bookkeeping of a sourced entry; whether the entry's claims are its receipts' claims is the non-author reading.
- Harm watch: `python3 -I quality/check-axis-scores.py --rev 5846662… --repo .` → `MADO_AXIS: checked=3 mismatched=0` (navigation 60/60, calibration 68/68, operability 12/12); tool selftests at the data commit unchanged (`w2/ExecHarmTip/harm.txt`: verify 460/460, options 211/211, globals 63/63, geometry 73/73); the only red gate, the axis publication in the window `[1959770, 2a3707c)`, is the lane's two-phase publication (`w2/ExecHarmTip.md` F1). No axis harmed.

## Sources & frontier

Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`:

```
round start (receipts/census-before.txt)                  round end (receipts/census-after.txt)
mado W04 S030, S042, S045, S097, S119, S120, S121 (7)     identical set
mado W01 S277 tierC mined                                 identical
mado ok …/mado-shokunin/corpus/SOURCES.md                 mado ok …/mado-shokunin/corpus/SOURCES.md
exit=0                                                    exit=0
```

- Rows 226 → **234** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Added by tier: **A ×8** — S290-S294 (`code`, Hyprland v0.56.2 at `efb5099`: RegexMatchEngine.cpp, DefaultFloatingAlgorithm.cpp, Target.cpp, WindowTarget.cpp, GeometricMovableAnimated.cpp) and S295-S297 (`own-work`: host-gkeep.conf, host-clients-r43.json, gkeep-ui-excerpt.py), all `mined`, opened 2026-10-26; Gate lines with access date, sha256 and ≤25-word located quotes in `corpus/lessons/round-43.md` `## Gate`.
- Rows touched old→new: S155 `used-by` `corpus/knowledge/rule-attribution-r24.md` → `…, corpus/knowledge/hyprland-gkeep-geometry-r43.md`; S158 `used-by` `…, corpus/knowledge/hyprctl-getoption-native-forms-r40.md` → `…, corpus/knowledge/hyprland-gkeep-geometry-r43.md` (logged in the lesson). Row wording defects found by w2 (S290, S291, S292, S293, S294, S296, S297 cells) are recorded for supersession; CORPUS rule 2 allows no in-place edit.
- Frontier advanced: `corpus/README.md` "Round-43 rule-size versus reported-size route" — a new edge class (rule size ↔ reported goal box), with a new coverage-map index row; knowledge entries 59 → 60.
- Sourced claim: C2 rests on S290-S297, opened this round.
- **Assimilation: theme gkeep geometry (`merge/mado/`).** Id guard (0-3-space pattern) in scratch: `reg-ids` 226, `staged-ids` 147, **collisions 34** (`assimilation/collisions`); proof on a scratch registry with an indented `  | S203 |` row fired (`assimilation/id-guard.md` §2); ids mapped by document (S290-S297 new, S155/S158 held, `renumber-map.tsv`; `w2/RevIdGuardQuarantine.md` lists where w1's provisional map differs from the landed one). Quarantine slice: 13 data rows (`assimilation/quarantine-slice`); the one row the theme cites is `unverifiable` (unreachable, not fabrication), none adopted (`assimilation/quarantine-verdicts.md`; w2 spot-check: S199, S200 hold, S189 falsified). ADMIT `gkeep-size-to-real-size-r11.md`; REFUSE `gkeep-size-rule-application-r10.md`, `gkeep-geometry-unobservable-r8.md`, `gkeep-observation-route-r11.md` (reasons + flips in the lesson); the `gkeep-element-rules-r30.md` refusal was withdrawn after w2 because its flip had fired (`apps/system.conf:4`), not adopted this round.
- Mistakes mined: M43-1..9 in `corpus/lessons/round-43.md` `## Mistakes` (fixes shown able to fail; M43-2's and M43-6's checks are stated as open).
- considerthese: `considerthese/2026-10-25.md` proposal 2 → QUALITY 81.

## Trend verdicts

- **expansion: improved** — one capability row (rule size versus reported size join, `SCORECARD.md` Round 43 capabilities), one knowledge entry on ground the lane did not hold (`git grep -ciE 'set_default_size|GEOMETRIC_GOAL|RE2::FullMatch|rendered geometry' a35cfdf -- corpus/knowledge PROVINCE.md SKILL.md tools` → none), rows 226 → 234, a new README Frontier route.
- **quality: improved** — the C2 instrument was tightened before data (v2, `receipts/ctl-c2-v2.txt`), round 42's wrong locators were corrected and a locator checker now fails on them (`w1/ExecLocatorGate/receipt.txt:60-61`), and every w2 content finding on the landed entry, SKILL and PROVINCE text was corrected in `8750016`; limit: the registry cells w2 found imprecise wait for supersession.
- **discernment: improved** — the lane refused four staged files and then withdrew one refusal on w2 evidence, re-registered its own frozen predicate when w1 showed it could be met without the work, and records the v2 do-nothing residual (`w2/ExecDoNothingV2.md`) instead of claiming coverage content the counter cannot see; outside confirmation is the non-author closure's.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — new decision row, probe row and the "Rule size versus reported size" subsection with a per-verdict licence table (`SKILL.md`, commit `8750016`); no non-author verifier.
- [~] At least one end-to-end domain task executed and logged — the tool's live read-only host run: `.ufo/waves/round-43/receipts/live-geometry-host.txt` (`verdict=NO_MATCHING_CLIENT`, exit 3; reproduced by `w2/SentLiveRun.md`); LOG.md Round 43; no non-author verifier.
- [~] Instructions executable by an agent without oral context — three seats built working tools from the contract text alone (`w1/ExecIndepA.md`, `ExecIndepB.md`, `ExecIndepC.md`: 37/37 each); dispatched seats are not outside-lane verifiers.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE tool row added and corrected (`w2/SentLiveRun.md` F3); sibling scans found no overlap (`w1/ConnSiblingOverlap/overlap.md`, `w2/ConnSiblingDup.md`); no non-author verifier.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs (by seats, official channels, no pacman): meson 1.12.1 via `uv tool install --force meson` (`w1/ExecOracleGkeep`, to build wlroots 0.20.2 tinywl for the isolated oracle; the existing shim was dangling); `google-re2` 1.1.20251105 via `uv pip install` into scratch venvs (`w1/LabRe2Fuzz`, `w2/CritEntryOverreach`, RE2 comparison); ninja 1.13.2 and strace 7.2 were already present.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` before filing lists only orchestrator/driver files (`.ufo/state/*`, `.ufo/watchdog.log`, `scripts/hyaku/*`, staged `.scratch/` and `.tower/` entries) — none written by this round's seats; nothing moved or deleted.
