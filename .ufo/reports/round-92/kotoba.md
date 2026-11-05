# kotoba — round 92 report (attempt 1, L1 KotobaR92; Linux host, omp 18.15.0)

Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`. Pushed lane tip at report time: **`0c545e1d8202fa553b0ac2dad801c66c1fc33514`** (`git ls-remote origin refs/heads/master` = this hash). Landing record commit: `010d3b8f7bd556815dc6261083bf3baaf4326677`. Landing code commit: `c679a631b3cc7f048a3627e2f79b0486190d45a4`. Freeze commit: `e073723ae667b64e534f8621bddb83ad12ad0e71` (plan, controls, pre-data red-before receipts). Round base: `5031a78215778525a7c777116ad6f6b89acac817`.

## Work performed

**Declared claims (2; distinct axes; frozen before data in `plans/round-92.md`):**

- **C1 — consistency (calibration sub-axis; score held 10).** The two round-91 pre-data controls that did not refuse the shortcut each names are replaced by committed shortcut worlds run through the public gates, plus two honest worlds, under one frozen counting command. Verdict: MET (measured at `c679a631`).
- **C2 — depth (lowest owned non-retired axis; score held 9).** (a) The battery's self-test pins the kill-set size, so a dropped kill row is a named self-test failure, not only a changed printed count. (b) The freeze gate's three same-class ladder rungs become fail-closed (work root under a regular file; duplicate control names; declared exit 127). Verdict: MET on both legs, with one disclosed naming gap on (a) (addendum A3).

Work items, each with its evidence pointer:

1. Pre-data: `plans/round-92.md`, `plans/round-92-controls.md` frozen at `e073723a`; `freeze gate: 6 control(s) held — freeze may proceed` — `.ufo/waves/round-92/receipts/freeze-gate-r92.txt`.
2. Red-before receipts committed at freeze: `receipts/redbefore-ctl-c2.txt` (old shortcut MET rc 0), `redbefore-ctl-c1.txt` (old UNMET rc 1, rows unread), `redbefore-m6-dropped-row.txt` (dropped row, self-test green 25, rc 0), `redbefore-ladder-{work,dup,127}.txt`, `redbefore-honest-fp-minimal.txt`.
3. Wave `r92-w1`: one v1 wave, 12 seats — `.ufo/waves/round-92/r92-w1-spec.json`, `r92-w1-dispatch.json` (`taskCall` 12 tasks), ready/dispatched markers, `r92-w1-results.json`. Seat outputs on disk: `.ufo/waves/round-92/w1/<Seat>/` and `w1/<Seat>.md` (12 of 12 wrote a report). Builders: ExecCtlWorlds (`ExecCtlWorlds.patch`, C1 worlds), ExecKillPin (`ExecKillPin.patch`, C2a), ExecLadderR92 (`ExecLadderR92.patch`, C2b and coupling), ScribeCorpusR92 (`ScribeCorpusR92.patch`, S265/S266/Q83); scout ScoutPyDocs (`ScoutPyDocs.md`); connector ConnectorOverlapR92 (`ConnectorOverlapR92.md`); attack seats ReviewerCtl, ReviewerFloors, MutTesterCtl, MutTesterBattery, CriticClaimsR92 (`CriticClaimsR92/CriticClaimsR92.md`), SentinelScopeR92 (`SentinelScopeR92.md`).
4. **Integration defect and repair.** The critic (`CriticClaimsR92/CriticClaimsR92.md` D1) and the mutation-tester (`MutTesterBattery.md` F-1) found that ExecLadderR92's rung-3 rewrite broke the frozen battery manifest anchor `fg-x1-parse-drop-exit-clause`; the candidate's honest C1 world read rc 2. The L1 moved the rung-3 check above the anchored line, restored the anchor byte-identical, and admitted the repaired blob in `INSTRUMENT_PINS` — `plans/round-92-addendum-1.md` A1, measured at `c679a631`.
5. Sentinel scope check (`SentinelScopeR92.md` S1–S8): patch scope, write containment, secrets/host, scratch discipline, SKILL.md freeze — all PASS on the candidate; no sysctl, pacman or credential material in any seat receipt.
6. Post-scoring errata and disclosed deviations (addendum A2–A6): the honest freeze-gate world is `r88-controls-fixed.md` (the plan named the refusal fixture); the landing corpus conjunct is the base DRIFT set (base reads 4 of 9, rc 1); the floors drift arm fires in the guard run, not `--self-test`; receipt pointers corrected; `KILL_SET_PINNED` is a literal read from the working-tree manifest (A3); late round-91 `ReviewerRepairs` files committed as wave evidence (A6). No predicate, counter, control, manifest row or PROBES entry changed.
7. Frontier step: S265 (correction row `supersedes S263 —`, anchor repaired), S266 (`NotADirectoryError`), Q83 criterion, lesson `corpus/lessons/round-92.md` (Gate, six Mistakes rows, Status changes, Considerthese, Settlement).

## Landed changes

| change | commit | LOG.md / record |
|---|---|---|
| C1 control worlds (`verifiers/fixtures/round-92/`: `ctl-c2-capline-only-v2.sh`, `ctl-c2-honest.sh`, `ctl-c1-manifest-only-v2.sh`, `ctl-c1-honest.sh`, `controls-run.sh`) | `c679a631` | LOG § Round 92 |
| C2a kill-set size pin (`verifiers/check_mutation_battery.py`, `kill-set-size` arm) | `c679a631` | LOG § Round 92 |
| C2b freeze-gate rungs, freeze_gate floor 31 → 34 (`verifiers/check_freeze_gate.py`, `verifiers/floors-registry.json`, `verifiers/check_assertion_floors.py` two cells, `verifiers/check_tip_battery.py` `INSTRUMENT_PINS` appends) | `c679a631` | LOG § Round 92 |
| A1 repair: rung-3 check moved above the fg-x1 anchored line; admission `0abfe8b1b3037cad614e99b7a0622a549cedf6e4` | `c679a631` | LOG § Round 92; addendum A1 |
| corpus: `corpus/SOURCES.md` S265 + S266 (190 → 192), `corpus/QUALITY.md` Q83, `corpus/README.md` lesson row (D6 hunk reverted to base) | `c679a631` | LOG § Round 92; `corpus/lessons/round-92.md` |
| plans: `plans/round-92.md`, `plans/round-92-controls.md`, `plans/round-92-addendum-1.md` | `c679a631` | addendum A1–A6 |
| wave evidence `.ufo/waves/round-92/` (dispatch, results, seat outputs, receipts); late round-91 seat files | `c679a631` | LOG § Round 92 |
| record: LOG § Round 92, SCORECARD round-92 annotations and round-93 intentions, lesson Settlement and Mistakes | `010d3b8f` | LOG § Round 92 |
| landing receipts (`receipts/landing/`: rungs, dropped row, corpus integrity at lane root, census validate at round end) | `0c545e1d` | LOG § Round 92 |

No change to SKILL.md (600 lines / 92 672 B, byte-identical); no change to any frozen instrument outside the touch list; no change to `corpus/lessons/round-*-verifier-spotcheck.md`; `verifiers/fixtures/round-91/` byte-identical.

## Before → after measurements

Counting commands are run from the lane root at the stated commit; the before column is the round-92 base (`5031a782`, checker bytes equal the freeze base's).

**C1 — controls refuse their named shortcuts (consistency; held 10).**
- Counting command: `bash verifiers/fixtures/round-92/controls-run.sh`
- Before: `redbefore-ctl-c2.txt` → `C2-PREDICATE-MET`, rc 0 on the cap-only shortcut; `redbefore-ctl-c1.txt` → `C1-PREDICATE-UNMET`, rc 1 with the appended rows never read. The round-91 pair refuses 0 of 2 named shortcuts.
- After (`c679a631`, `receipts/landing/controls-run.stdout`): `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, rc 0. Stages: C2-shortcut rc 1 (`instrument-pin admission missing`), C2-honest rc 0, C1-shortcut rc 1 (`rows committed and read; instrument cannot evaluate (rc 2)`), C1-honest rc 0 (`killed 17 of 17`).

**C2a — kill-set size pin (depth; held 9).**
- Counting command: `python3 -B verifiers/check_mutation_battery.py --self-test` and the dropped-row world (one `kill` row removed from the working-tree manifest, then the self-test).
- Before: `redbefore-m6-dropped-row.txt` → `kill rows before=17 after=16`, `0 failure(s) over 25 assertions`, rc 0.
- After (`c679a631`): self-test `receipts/landing/bat-selftest.txt` `0 failure(s) over 28 assertions`, rc 0; dropped row `landing-m6-dropped-row.txt` → `FAIL arm kill-set-size: … observed 16 kill rows, pinned 17`, `1 failure(s) over 28 assertions`, rc 1.
- Disclosed (addendum A3; CriticClaimsR92 D2): a committed-revision dropped row is refused by the battery baseline check with rc 2 and does not name the arm. Routed to round 93.

**C2b — three fail-closed rungs (depth; held 9).**
- Counting command: `python3 -B verifiers/check_freeze_gate.py --plan <fixture>` for `fp-minimal.md`, `fp-duplicate-names.md`, `fp-exit127.md` and the work-root probe; `--self-test`.
- Before (base, `redbefore-ladder-*.txt`): work root under a regular file → uncaught `NotADirectoryError`, rc 1; `--work` naming a regular file → uncaught `FileExistsError`, rc 1; duplicate control names both passing → `freeze gate: 2 control(s) held`, rc 0; declared `exit 127` → `COULD-NOT-EVALUATE … (rc=127)`, rc 2 (never compared); self-test 31.
- After (`c679a631`, `receipts/landing/landing-rungs.txt`): work root under a regular file → `COULD-NOT-EVALUATE --work …: not a directory`, rc 2; `--work` naming a regular file → same line, rc 2; duplicate → `INVALID SPEC: duplicate control dup (line 9): already declared at line 7`, rc 3; declared 127 → `INVALID SPEC … exit 127 is unobservable …`, rc 3. Self-test `receipts/landing/fg-selftest.txt` `0 failure(s) over 34 assertions`, rc 0. Floors `floors-selftest.txt` `0 failure(s) over 176 assertions`, rc 0; coupling 34 = 34 = 34.
- Honest worlds at landing: `fg-honest-fp-minimal.txt` rc 0 (`1 control(s) held`), `fg-honest-r88fixed.txt` rc 0 (`4 control(s) held`); refusal fixture `fg-r88-refusal-fixture.txt` still refuses (rc 1, `w_added_red`).
- The `rp-*.sh` probes exit 1 on the fixed candidate by construction; the readings above are the gate's printed lines.

**No-harm at landing (`c679a631`).** Gate registry `receipts/landing/gate-registry.txt` `74 of 74 … phantom 0`, rc 0 (before 74 of 74). Tip battery `tip-battery.txt` `guards 5 of 5; tip battery exit 0: 3 of 6`, rc 1 from the three carried reds (same as base). Corpus integrity at the lane root `corpus-integrity-laneroot.txt` `4/9 checks pass`, DRIFT set identical to base (`base-corpus-integrity.txt`). Census `corpus/SOURCES.md` 190 → 192 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`), `sources-census.sh validate --root … kotoba` rc 0 (`census-validate-root.txt`). Carried red, unchanged: sibling census `province rows 20 matched 4` rc 1; province core `0 of 2` rc 1; checklist `governance.citation_resolves` rc 1.

## Sources & frontier

- **SOURCES.md rows before → after:** 190 → 192 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; validate rc 0 at round start `census-before.txt` and round end `census-validate-root.txt`).
- **Rows added by tier:** tier A ×2 (S265 correction row, S266); tier B 0; tier C 0. Status `mined` ×2.
- **Rows touched old→new:** S263 status unchanged (`mined`), `used-by` unchanged; its anchor is corrected by S265, which opens `supersedes S263 —` (append-only, SOURCES contract rule 2). S265 `used-by` `corpus/knowledge/timeout-calibration-round91.md,corpus/lessons/round-92.md`; S266 `used-by` `corpus/lessons/round-92.md`.
- **Frontier rows advanced:** the `NotADirectoryError` / path-component exception class (S266) now grounds the freeze gate's work-root rung; subprocess timeout contract (S265) re-grounded for the cap calibration.
- **Assimilation:** none — the shokuknow package stays unadopted; L0 `kotoba | round-88` (55-id collision) is still open and no claim depends on it.
- **Considerthese:** `considerthese/2026-10-26.md` re-read; nothing implemented; proposal 3 carried (600/600 SKILL.md ceiling).
- **Corpus contract:** Q83 added to `corpus/QUALITY.md`, grounded in `lessons/round-92.md` § Mistakes (vacuous row).

## Trend verdicts

- **expansion: unchanged.** No `knowledge/` entry was admitted this round (CORPUS rule 4: expansion is knowledge, not rows). Two rows were admitted (S265, S266) and cited by the lesson, not by a new knowledge entry.
- **quality: improved.** Evidence: a control that read MET on the shortcut it named now refuses it through the public path (`controls-run.stdout`, `redbefore-ctl-c2.txt`); the battery self-test refuses a dropped kill row by name (`landing-m6-dropped-row.txt`); three freeze-gate rungs that crashed or silently held are fail-closed (`landing-rungs.txt`). No admitted entry was found false; the integration regression (the battery anchor, A1) was caught and repaired before landing, and is mined as a Mistakes row.
- **discernment: improved, conditional.** A disagreement from the round-91 non-author spot-check (routed defect 1: a control that does not refuse its own shortcut) became a lesson-backed `QUALITY.md` criterion (Q83 ← `lessons/round-92.md` § Mistakes `vacuous`). The non-author closure still owes the spot-check of this round's gate decisions (the two admits S265/S266; the lesson's Gate has no reject this round; the closure may sample the S264 reject from round 91).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SHONEN.md` box 1 pointers (unchanged this round; SKILL.md byte-identical at 600 lines, `git diff --stat e073723 c679a631 -- SKILL.md` empty).
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md` § Round 92 (landing of the C1 and C2 instruments, measured at `c679a631`; `receipts/landing/`).
- [~] Instructions executable by an agent without oral context — evidence: `plans/round-92-controls.md` and `verifiers/fixtures/round-92/controls-run.sh` run as pasted (`controls-run.stdout`, rc 0); `SHONEN.md` box 3 pointer `corpus/lessons/round-8-aggregator-box3-coldrun.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` § Adjacent; the sibling census stays red at `province rows 20 matched 4` (carried, unchanged this round); no sibling file touched.

## Round shape, seats, and lane status

- **Shape:** ONE v1 wave `r92-w1`, band 8–16, 12 seats: executor 3, scout 1, scribe 1, connector 1, reviewer 2, critic 1, mutation-tester 2, sentinel 1. Attack seats 6 of 12 (50 %, ≥ 25 %); connectors 1 (≤ 2). The L1 holds the § 3 planner seat (the validator rejects `planner`). No residual call; no second wave. Round total: 12 seats.
- **Dead seats:** none. All 12 seats wrote a report. `results.json` records no per-seat outputs (`note`: orchestrator kernel restarted mid-wave); the on-disk seat reports are the evidence.
- **Stale-lane:** none — no other mission of this lane is open; the round ran to landing in one L1 session.
- **Tooling:** no tool installed or upgraded this round; no pacman, no sysctl, no kernel change. Read-only use of `timeout`/`mktemp`/`git` in scratch.
- **Scratch:** all clones under `/fast/scratch/hyaku/kotoba-r92/` (seat-named dirs and `L1-integ`); removed after landing per §7.
- **Wave-evidence budget (Q82):** `du -sb .ufo/waves/round-92` = 565 191 B (2026-11-05, after the landing receipts); prior rounds on the same measure: round 91 = 1 011 138 B, round 90 = 1 344 634 B. Largest artifact: the wave's per-seat receipts; none over 1 MiB.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time shows only the orchestrator's `M .scratch/run15-state.json` and the shared `M .ufo/l0-questions.md`; no untracked file written by a kotoba seat sits at the fleet root. No misroot to move.
- **Commits:** through `scripts/hyaku/jj-lane.sh commit … --as kotoba` only; `landed` lines: `c679a631…`, `010d3b8f…`, `0c545e1d…`.

## Open items and L0

- **L0 appended:** `kotoba | round-92 | Operator ruling wanted on addendum A3 …` (`.ufo/l0-questions.md`). The fleet L0 file carried another lane's uncommitted line (revenger round-97 assimilation) at append time; the sanctioned `fleet-commit.sh` path commits the whole file, so that line is committed with this report under the helper's serialization. Disclosed here, not edited.
- **Routed to round 93 (not claimed closed):** F1 (the frozen counting does not pin a refused world's exit code; stub arm needed), F-4 (removing a whole `INSTRUMENT_PINS` key is silent in the tip battery), D2 (committed-revision kill naming; A3).
- **Carried, unchanged:** L0 `kotoba | round-88` (assimilation collision), `kotoba | round-73`; sibling census red; province core red; checklist `governance.citation_resolves` red; corpus integrity DRIFT set (five names, base-identical).
- **Inherited state at round start:** `.ufo/waves/round-91/r91-w1-results.json` already tracked (commit `931746a`); round-91 `ReviewerRepairs` late files committed as evidence (A6). No `corpus/lessons/operator-*.md` present.
- **Verdicts are measured, not admitted:** the claim verdicts above are the L1's measured readings at `c679a631`; the non-author closure rules the round (`plans/round-92-addendum-1.md`, `corpus/lessons/round-92.md` § Settlement).
