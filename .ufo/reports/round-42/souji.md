# souji — Round 42 (attempt 1) — outcome: honest-stop (operator wrap-up, run 11)

The operator ended hyaku run 11 while wave 2 was running. This report lists what landed with full hashes, what did not, and the open claims. Verdicts on the claims belong to the non-author closure; the lane claims no admission.

## Work performed

**Declared claims (frozen before any wave file, `census/round-42/preregistration.txt`, first added at `afe17f416eec04dcf3f480b580a8f928de61d19d`; instruments `b7408095543579ac71b33ecf7b80b0cb8ef45036`; do-nothing and partial controls in `census/round-42/controls/`):**
C1 — calibration (lowest axis, 7): account for the 70 unresolvable declared-evidence tokens the lane's own instrument `tools/souji-declared-evidence.py` reads in `SCORECARD.md` at the base. C2 — operability: `tools/souji-freeze-check.py` grows KEY-DUPLICATE, HEADING-MALFORMED, symlink classes, widened dispatch names and a real `--selftest`. C3 — coverage: a fixture observing 13 condition-level mutants of `tools/souji-worktree-drift.py` that survive all eight earlier drift fixtures. Residual R1 (not a claim): R41-D-LG-DANGLING.

- Read first: `corpus/lessons/round-41-verifier-spotcheck.md` (R41-D-REJECT-REASON, -C3-CONDITION, -C2-SELFTEST, -LG-DANGLING); disposition table at the top of `corpus/lessons/round-42.md`.
- Pre-freeze survey (`census/round-42/records/survey-prior.txt`): six mutants of the r41 wave-2 survivor list (D3 F2 H3 J5 N1, and the spot-check's T2) are killed by older fixtures and were left out of the C3 population.
- Control receipts (committed at the freeze): C1 do-nothing `registered=0`, forged all-resolved register `class_ok=42`; C2 r41 tool `pass=24/37 selftest=FAIL patches=0/3`, always-green selftest stub `patches=0/3`; C3 absent fixture `survived=13`, always-pass stub `survived=13`, byte-sniffing stub `equiv_killed=6`; R1 `findings=3`. `census/round-42/controls/*.txt`.
- Planner seat held by the L1 (the validator rejects `planner`); recon rode scouts and connectors.

## Landed changes

All pushed; `git ls-remote origin refs/heads/master` prints `6a3f75941d3604e3459011d599c2c16f3a97b44c`.

| change | LOG.md entry | commit |
|---|---|---|
| start census receipt, counters, populations, stubs, score harness, S259 snapshot | Round 42 entry | `410316c9810b0c59f360e5a20f36c99469c6d43d`, `b7408095543579ac71b33ecf7b80b0cb8ef45036` (C1 counter duplicate-token fix, pre-freeze) |
| preregistration freeze, C2 population, controls | Round 42 entry | `afe17f416eec04dcf3f480b580a8f928de61d19d` |
| C2 tool (candidate R42executor06) | Round 42 entry | `133206705f32d785277c1fdf69abd4c73066ba7c` |
| C3 fixture (candidate R42executor10) | Round 42 entry | `5ad7046d44c3be81ffdb5b2b448cb95a6b03fc96` |
| R1 repoint of the two fleet-report citations to byte-exact lane copies | Round 42 entry | `e95b13beb5b690f0bf80034c12c1ac7b6650bb45`, wording `51f204fb7c633b691a3ca9cd8c0bf025f6e0a093` |
| C1 register, lesson, S259 row, QUALITY Q103-Q105, SKILL gate rows `r42-*`, README update, wave-1 capture, score-candidate allowlist | Round 42 entry | `34e33a662cd0d6931e5aa006bd90364e7852c0d5` |
| SCORECARD and LOG round-42 entries, C1 receipt | Round 42 entry | `3105a63b23481fccf7df58e74d14a6681e0ea0c8` |
| honest stop: wave-2 evidence capture, lesson errata E-1..E-10, SCORECARD errata, end census | Round 42 entry (stop note in SCORECARD) | `d39e3453fed1d258a6bf6731d47ed4d0477debb3` |
| errata wording (marker token out of prose, `junk=1 -> 0`) | — | `6a3f75941d3604e3459011d599c2c16f3a97b44c` |

**Landed work vs the claims.** The measurements below were run by the L1 and the C1 line again at the final tip.

**Did not land / not completed.**
- Wave 2 was stopped by the operator: 32 of 34 seats left a report; `R42w2critic08` (axis-harm audit) and `R42w2mutationtester03` (fixture mutation) left none; `R42w2mutationtester01` has no report either. Wave 1: 39 of 40 seats left a report (`R42mutationtester03` left a harness directory only). No `w2-results.json` exists; the seat counts come from the report files.
- The wave-2 axis-harm audit (SKILL gate rows at base vs tip) did not run; no non-author check of "no axis harmed" exists. The lane makes no harm claim beyond the probes in lesson E-6/E-9 and R42w2critic07 row 23.
- The R1 frozen target (`rows_added=3`) is not met and cannot be: the lesson (E-2) records why (gate exemption grammar cannot name `../` pointers; the frozen counter ignores the gate exit). The landed repoint reads `findings=0` in both gate modes.
- No superseding S260 for the narrowed S259 scope (R42w2reviewer07) was landed.
- No QUALITY criterion for the load-sensitivity of the C3 reading was added (named limit only).

## Before → after measurements

Counting commands paste as given; commit = the revision measured.

| claim | before | after | counting command | commit |
|---|---|---|---|---|
| C1 calibration | do-nothing `registered=0`; forged register `class_ok=42` | `SUMMARY items=70 population=ok registered=70 class_ok=70 unresolved=5 corrected=5 junk=0 rewritten=0 new_mismatches=0` rc 0 (re-run by the L1 at the final tip `6a3f759…`; first receipt `census/round-42/records/c1-after.txt` at `34e33a6…`, with `junk=1` caught at `d39e345…` and repaired at the final tip) | `python3 -B census/round-42/c1-counter.py --root . --rev <full40> --scratch <dir>` | `6a3f75941d3604e3459011d599c2c16f3a97b44c` |
| C2 operability | r41 tool `cases=37 pass=24 fail=13 ... selftest=FAIL patches=0/3` | `cases=37 pass=37 fail=0 control_clean=REJECTED control_findings=REJECTED real=ok retro=red retro_clean=ok selftest=ok patches=3/3` rc 0 (three more independent runs by R42w2reviewer04; L1 re-run at the final tip) | `python3 -B census/round-42/c2-counter.py --root . --rev <full40> --scratch <dir>` | `6a3f75941d3604e3459011d599c2c16f3a97b44c` (tool landed at `133206705f32…`) |
| C3 coverage | absent: `survived=13`; stubs `survived=13` / `equiv_killed=6` | `mutants=13 killed=13 survived=0 pristine=ok prior=8/8 old_killed=0 equiv=6 equiv_killed=0 anchors=ok` rc 0 on the idle-host measurement `census/round-42/records/c3-after.txt` at `5ad7046…`; **not stable under load** (R42w2critic07, R42w2reviewer05: one of three tip runs `killed=9`; a loaded run `killed=5`, another `old_killed=1`) | `python3 -B census/round-42/c3-counter.py --root . --rev <full40> --scratch <dir>` | `5ad7046d44c3be81ffdb5b2b448cb95a6b03fc96` |
| R1 (residual) | `findings=3` plain mode, `0` with `--fleet-root` | frozen counter `findings=0 deleted=2 rows_added=0 stale=0` = red by its letter; landing gate `findings=0` in both modes with `--round 42` at the final tip | `python3 -B tools/souji-landing-gate.py --root . --rev <full40> --round 42 [--fleet-root /home/vgpnk/Projects/shokunin]`; `census/round-42/r1-counter.py` | `6a3f75941d3604e3459011d599c2c16f3a97b44c` |

Owned scores unchanged (calibration 7, operability 8, coverage 8); no reproducible 0-10 mapping, so no score delta is claimed. All three frozen counters score shape (lesson N-C1a, N-C2a/b, N-C3a); wave 1 built artifacts that reach the targets without the substance, and the lane's compensating checks are listed in the lesson. The C3 reading is an idle-host value.

## Sources & frontier

- Census command (both ends): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`. **Before:** `souji ok`, exit 0, rows=182, W04=52 (`census/round-42/records/census-before.txt`). **After:** `souji ok`, exit 0, rows=183, W04=52 (`census/round-42/records/census-final.txt`, taken at `3105a63…`, before the stop commits, which touch no registry file).
- Rows added: S259 (tier A, `mined`, Python `site` docs, quote "an attempt is made to import a module named sitecustomize, which can perform arbitrary site-specific customizations", snapshot `census/round-42/sources/python-3-library-site.html` sha256 `620581fe5440952a9b62554526f6fe613b030b2c7a1521e1e57495f22e5d546a`). Sourced claim: C2 (patches leg). Re-opened by R42scribe06, R42w2reviewer07 and R42w2critic07: bytes and quote verified; R42w2reviewer07's verdict is NARROW SCOPE (the page documents the `site` import, not the PYTHONPATH channel) — recorded in lesson E-5, not superseded. No older row changed status, recheck or used-by.
- Mistakes mined: M42-1 .. M42-6 in the lesson, each with a captured-by and a fix (C1 register and counter leg, Q103-Q105), and wave-2 errata E-1..E-10 correcting this round's own text (notably E-2: the M42-2 "mode trade" diagnosis was wrong).
- Frontier: F1 stays frontier; no knowledge entry added; no coverage-map ground promoted. Assimilation: none (`/home/vgpnk/Projects/shokuknow` not read); `considerthese/` does not exist in this lane.

## Trend verdicts

- **expansion — unchanged.** One tier-A row on held ground; 17 new non-equivalent drift-tool survivors named (the r43 population); no entry, no ground promoted.
- **quality — unprovable-but-better.** The lane's own text was attacked by wave-2 reviewers and nine-plus misstatements were corrected append-only (E-1..E-10); QUALITY Q103-Q105 added; but the C3 target flips under load and the frozen counters score shape, and no non-author closure has judged it.
- **discernment — unprovable-but-better.** The round found a wrong diagnosis of its own (E-2) and a flaky reading (E-1) through wave 2; no non-author spot-check of this round exists yet.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md gate rows `r42-c1-counter` .. `r42-r1-counter`; QUALITY Q103-Q105; S259.
- [~] At least one end-to-end domain task executed and logged — LOG.md Round 42 entry (instrument and accounting work; no deletion authority exercised).
- [~] Instructions executable by an agent without oral context — `census/round-42/preregistration.txt`, the four counters, `score-candidate.sh` with its allowlist.
- [~] No cross-domain bleed — `census/round-42/waves/w1/R42connector01.md`; sibling freeze and mutation tools reported, not absorbed.

## Round shape, seats, open claims

- **Shape:** two v1 waves (policy v1, band 32-64). W1 = 40 seats (executor 12, scribe 7, critic 6, scout 4, reviewer 4, mutation-tester 3, sentinel 2, connector 2; attack 15 = 37.5 %). W2 = 34 seats (reviewer 10, critic 8, mutation-tester 7, executor 4, scout 2, sentinel 2, connector 1; attack 27 = 79 %). **Total 74** (band 64-128). No residual call. Dead/stopped seats: W2 `R42w2critic08`, `R42w2mutationtester03`, `R42w2mutationtester01` (no report; stopped by the operator wrap-up); W1 `R42mutationtester03` (harness only; `R42mutationtester02` reported). No error text recorded; no `results.json` exists for either wave.
- **Deviations:** (1) the C1 counter was fixed once before the freeze (duplicate-token counting, `b740809`), and the preregistration's own sentences about adding commits and control receipts are wrong (lesson M42-5); (2) `score-candidate.sh` got a destination allowlist after wave 1 (landed with `34e33a6`), a harness change, not a counter change; (3) the frozen R1 predicate was found unsatisfiable (E-2) and a different repair landed.
- **Open for r43:** the C1 counter's defects (blank-line sentinel, `> 840` threshold, extra register rows, fences, marker-in-prose junk) and a counter that reads correction prose (N1-N4); a load-stable C3 reading (timeouts read as survivors; `killed()`/`old_killed` timing); the 17 non-equivalent condition survivors (R42w2critic04) and the 60+ mutant survey (R42w2mutationtester06 left no report); C2 expectation readings and the unclosed holes (zero-padded or fullwidth `Round:`, Control symlink text, FROZEN-EDITED not covering the Control or the preregistration itself, malformed-heading block boundary); S259 narrowing (`using/cmdline`); the axis-harm audit and fixture mutation that did not run; tool defect N10, registry K1 `S146`, R39-D1/D2. Certification OFF, K5 HELD.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no entry naming souji or round 42; nothing moved. **Scratch:** `/fast/scratch/hyaku/souji-r42` removed (two seat sandboxes needed `chmod -R u+rwX` first and were removed).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open. **Tools installed:** none; pacman stayed paused. **Open L0:** none.

---

# Round 42 — resume (hyaku run 12, 2026-10-29): outcome complete, awaiting non-author closure

This section is appended by the run-12 re-dispatch of the same round (the L1 agent `SoujiR42`, attempt 2). It supersedes the `outcome: honest-stop (operator wrap-up, run 11)` headline above and corrects it (errata below); the filed bytes above are history, not rewritten. The run-11 wrap-up had released the round's claim without a closure; the inherited landed work was re-verified at the final tip and the two genuinely stopped wave-2 items were completed by a residual wave. **Lane final hash: `34343a39ffab8029b06e8e6c9ac699ebcbd65f8a`** (`git ls-remote origin refs/heads/master` prints it).

## Work performed (resume)

The declared claims are unchanged from the freeze (`census/round-42/preregistration.txt`): C1 calibration (declared-evidence accounting), C2 operability (freeze-check hardening), C3 coverage (condition-level drift fixture), plus residual R1 — all landed in run 11 and untouched this attempt. Resume work items:

- **Inherited-work re-verification at the final tip** (`6a3f75941d3604e3459011d599c2c16f3a97b44c` at start of this attempt): c1 `SUMMARY items=70 population=ok registered=70 class_ok=70 unresolved=5 corrected=5 junk=0 rewritten=0 new_mismatches=0` rc 0; c2 `SUMMARY cases=37 pass=37 fail=0 ... selftest=ok patches=3/3` rc 0; c3 `SUMMARY mutants=13 killed=13 survived=0 ... anchors=ok` rc 0; landing gate `findings=0` rc 0 in both modes with `--round 42`; receipt `census/round-42/records/resume-remeasure-l1.txt` (landed `17a6d0b5…`).
- **Wave 3 — residual call, 4 attack seats, one batched dispatch via the inline spawn handoff** (`w3.ready` → `w3.ready.dispatched` 17:21:17; `w3-results.json` written by the dispatcher; WAVE-DONE received). Seats: R42w3critic01 (axis-harm audit; re-issues the never-started R42w2critic08), R42w3mutationtester02 (fixture mutation; re-issues the never-started R42w2mutationtester03), R42w3mutationtester01 (tool part-A mutation; corroborates/extends the inherited R42w2mutationtester01 report), R42w3reviewer01 (independent tip re-measurement). All 4 settled, 0 dead. Round total: 74 + 4 = **78 seats** (band 64–128; w1 40, w2 34, w3 4; attack seats w3 4/4). Reports captured at `census/round-42/waves/w3/` (evidence capture `records=3510 renames=0 excluded=1`, verify green).
- **Axis-harm audit (R42w3critic01): no durable calibration, operability or coverage regression** at base `bf618f6c…` vs tip `6a3f7594…`; mismatches stayed 70; C2 retained 21/21 with the new legs 37/37 + selftest 31/31; C3 13/13; three pre-r42 gate-row differences each explained (r41 C2 expected tool_sha; registry echoed revision; landing-gate 3→0 of the favourable R1 repoint); one differing leak-count pair passed 3 serial reruns per revision (`census/round-42/waves/w3/R42w3critic01.md`). The "no axis is harmed" side of admission now has a completed non-L1 audit.
- **Fixture mutation (R42w3mutationtester02): the landed C3 fixture is mutation-robust for its frozen target** — 1050 grid cells (75 fixture mutants × 14 tools, none missing, no crash), 0 disagreements with the wave-2 partial grid over 634 shared cells, harness verdicts cross-validated against the frozen counter (exact match), G3 kill reproduced serially at load 16–290; 11/13 cases individually load-bearing, 2 mutually necessary; findings F1–F4 are coverage observations, not defects (`census/round-42/waves/w3/R42w3mutationtester02.md`).
- **Tool part-A mutation (R42w3mutationtester01): 136 mutants of lines 1–187** (64 inherited M re-verified + 72 new W) against tool bytes `9ddd596b…` (identical at landing and tip): counter cases kill 65, `--selftest` 4 more, 63 both, 2 counter-only; 67 survivors = 35 equivalent + 30 gaps + 2 real-leg-only, all re-verified one at a time (agree=67). The 30 gaps extend C2's named part-A coverage limits — r43 material, no frozen instrument touched (`census/round-42/waves/w3/R42w3mutationtester01.md`).
- **Independent re-measurement (R42w3reviewer01): all three claims reach their frozen targets at the tip; every SUMMARY field identical to the committed receipts** (`census/round-42/waves/w3/R42w3reviewer01.md`). Caveat kept honest: the shared host never dropped below load1 8, so that run corroborates but does not replace the canonical idle-host receipt `c3-after.txt`.
- **Errata recorded (append-only; lesson `## Wave 3` section):** E-11 — the honest-stop list above wrongly says R42w2mutationtester01 left no report (it landed 22:57:14, before the 23:45 filing, and is in the receipt; the stopped set was two seats); E-12 — the two routed pointer fixes recorded, not edited; E-13 — the kama-r64 `pkill -f mut-.*\.py` caveat (three souji seats' run-11 mutant processes matched near 22:03; wave-3 runs are fresh and unaffected).
- **Misroot sweep (this attempt):** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/goal-20261029-hyaku-run12.md` (orchestrator run state, never a misroot); nothing moved.

## Landed changes (resume attempt)

| change | LOG.md entry | commit |
|---|---|---|
| wave-3 record + errata E-11..E-13 in the round lesson; L1 tip re-measurement receipt; wave-3 evidence capture (reports, spec, dispatch, results.json); LOG + SCORECARD resume sections | Round 42 attempt 2 entry | `17a6d0b519ac174073d3454417cf349d969785ef` |
| end-of-round SOURCES census receipt (resume) | Round 42 attempt 2 entry | `34343a39ffab8029b06e8e6c9ac699ebcbd65f8a` |

## Before → after measurements (resume re-verification)

The claims' before→after table above stands unchanged (frozen). This attempt's measurement is a re-derivation at the final tip: counting commands as declared (`python3 -B census/round-42/<claim>-counter.py --root . --rev 6a3f7594… --scratch <dir>`; landing gate with `--round 42` both modes), run independently by R42w3reviewer01 and by the L1 — **every SUMMARY field identical to `census/round-42/records/{c1-after,c2-after,c3-after,gate-both-modes}.txt`; commit measured: `34343a39ffab8029b06e8e6c9ac699ebcbd65f8a`** (identical at `6a3f7594…`; the two resume commits touch no counter, tool, fixture or registry bytes).

## Sources & frontier (resume)

- Census command (both ends of this attempt): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` — start of attempt: `souji ok`, exit 0, rows=183, W04=52; end of attempt: `souji ok`, exit 0, rows=183, W04=52 (receipt `census/round-42/records/resume-census-final.txt`, landed `34343a39…`). Rows added by this attempt: none (S259 stands as filed per E-5; the registry is unchanged). No status/recheck/used-by cell changed.
- Mistakes mined: none new this attempt (M42-1..M42-6 and the wave-2 errata stand; wave-3 findings are coverage observations and errata E-11..E-13, recorded in the lesson).
- Frontier: unchanged; no knowledge entry added; no coverage-map ground promoted. Assimilation: none (the frozen claims serve no staged theme; `/home/vgpnk/Projects/shokuknow` not read); `considerthese/` does not exist in this lane.

## Trend verdicts (resume update)

- **expansion — unchanged** (as filed): one tier-A row on held ground; no entry, no ground promoted; wave 3 added findings, not ground.
- **quality — unprovable-but-better**, now stronger: the C2/C3 artifacts survived two further attack passes (136 tool mutants, 1050 fixture cells) without a defect finding, and the axis-harm audit is complete; still no non-author closure has judged the round.
- **discernment — unprovable-but-better**: the round found and corrected its own filing error (E-11) through the resume re-check; the outside spot-check remains the closure's duty.

## Resume note on the SHONEN assessment

The four `## SHONEN` lines above stand; this attempt strengthens their `[~]` evidence without re-filing them: the end-to-end task line gains the completed axis-harm audit and mutation attacks (LOG Round 42 attempt 2 entry, commits `17a6d0b5…`, `34343a39…`); the executable-instructions line gains the wave-3 spec/dispatch/results trio. No box is claimed `[x]` — that needs the non-author verifier.

## Round shape, seats, closure state

- **Shape (final):** two v1 waves (run 11: 40 + 34 seats) + one residual call (run 12: 4 seats; validator plan under the default band, min 2, 4/4 attack roles) = **78 seats total** (band 64–128). Dead seats (final): run-11 wave 1 `R42mutationtester03` (harness only); run-11 wave 2 none beyond the two seats that never reported (re-issued in wave 3); wave 3 none. `w3-results.json` exists; the run-11 waves' results files do not (seat counts from report files, as filed above).
- **Routing note:** wave 3 seats were spawned by the orchestrator through the run-7 handoff; no `model` was passed; per-seat answering models are not cited by any claim.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open. **Tools installed (this attempt):** none; pacman stayed paused. **Open L0:** none new; the historical souji lines (r17/r18/r20/r40) stand routed-around; the kama r64 line is recorded as caveat E-13, no decision requested.
- **Scratch:** `/fast/scratch/hyaku/souji-r42` removed by the L1 after landing (receipts first copied into `census/round-42/records/` and `census/round-42/waves/`).
