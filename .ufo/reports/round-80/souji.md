# souji — round 80 report (L1 SoujiR80, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Base `f80f9368a8a20679438b1dffd72d0faab0ccf194` (r79 closed `rejected-honest-stop`, spot-check committed). Preregistration `census/round-80/preregistration.txt` (frozen at F `aaad410f4de2c1b0e98f1a7f305736dfcee5c5ab`; freeze-check `SUMMARY claims=2 findings=0`).

## Work performed

Declared claims (two, causally separable; S80Connector: SEPARABLE — no C1 receipt binds a quarantine-tool byte, no C2 receipt binds a C1 counter byte):

- **C1 — calibration (the lowest owned axis, 7; sourced on S327, opened this round):** a successor pointer-resolution counter `census/round-80/c1-pointer-counter.py` refuses the three false ledger rows the r79 wave's S79MutCounter showed the r79 counter accepts (NF6b declaration matched only as path prefixes, NF8 a range member that is a directory, NF10 a MOVED copy under another tree). Frozen 18-row harness: **accepted 3 → 0, mismatches 3 → 0, EXIT=0**; controls and regressions as preregistered.
- **C2 — operability (sourced on S328, opened this round):** `tools/souji-quarantine.sh --dry-run` answers a caller's TERM/INT/HUP by killing every process it started (a front shell + `setsid` worker; the front kills the worker's session) and exiting 128 + n with `SIGNAL<TAB>SIG<name><TAB>RECEIPT-QUARANTINE-SIGNALED`. Frozen 15-row counter (a new instrument carrying the r79 lesson's fixes): **mismatches 12 → 0, orphans 12 → 0, EXIT=0** at A on the W2 bytes. Two regression conjuncts were first replayed defectively at A and re-measured (below), and the wave found a harm at W2 outside the frozen rows (a job-control launch made the tool exit 0 with no verdict), repaired after the wave behind failing-before probes. Both facts are stated for the closure to rule on.

Work items:

- Protocol load and inherited debts: r79 spot-check routed defects 1–7 and r79 lesson `## Routed to round 80` read first (`corpus/lessons/round-80.md` `## Inherited`). Defect 1 → `census/round-80/rec.sh` writes a `launch=` line on every receipt and the C2 counter resets dispositions per child; 2 → not taken (the r79 capability row stays closure-gated); 3 → C2 Stated limits name the inherited-INT condition; 4 → every post-wave repair sits behind a probe that fails on the earlier bytes; 5 → wave context forbids lane paths by name (no seat wrote a lane file); 6 → C1; 7 → `souji-quarantine.sh` taken as C2, the rest carried.
- Pre-freeze feasibility in scratch (Q70): `census/round-80/records/prefreeze-feasibility.txt` (an NF10 draft that refused the real captures L15/P31 was replaced before P; a forking session scan that missed the 5 s settle on 9/15 rows was replaced before P).
- P `515d57c8c559d64d0c071cc25b07df0b815bd77a`: C1 harness + 18-row population (fixture F0 reproduces the r79 fixture commit `6436db6a`), C2 counter + 15-row population, control variants and every control receipt, `rec.sh`, S327/S328 captures under `census/round-80/srcs/` and rows, census-before.
- F `aaad410f4de2c1b0e98f1a7f305736dfcee5c5ab`: preregistration (`census/round-80/records/freeze-check-at-F.txt`).
- W1 `bd263c3f7d376e617c2fde5b99793622b0908b53`: C1 candidate counter (sha256 `90ed9031…69f1`).
- W2 `836dac3e336863c57d9d7125837ed22b22d8d044`: C2 candidate tool (blob sha256 `67ec160b…7181`).
- A `a4aa888037922b7b5ccfac7150f156f92af5916e`: after-arms, regressions, diagnosis receipts (`census/round-80/records/diagnosis/`).
- I `60c7f50eb803a6ee6d887fabdd32ab0e9e8102bc`: knowledge `corpus/knowledge/gate-signal-handling.md` r80 section, QUALITY Q144/Q145, README frontier r80, SKILL rows r80, SCORECARD r80 rows, LOG `## Round 80`, lesson draft, wave spec.
- Wave w1 (12 seats, 0 dead) → probes and repairs: D `37ab234e11de7436d268447bae79ccb535cff8f9` → R `8ba93218ce4e531651d754821e9c569a6509a2d2` (+ receipts `e1b5caf94312022e5a8dd9da3fe223829f3fb4de`); D2 `330197b99b8ba751635009df52adbe36327f4c52` → R2 `97289f81c08804090143008937bdbdb3d5fae9b7` (+ receipts and text fixes `79fcc73dba05b038caf77c9285766bc57a4efa99`); D3 `f6fcddb5d8998b091f267b65bac398377a55bd6f` → R3 `4a499e9a7d0eeb853cc55e68fb3f453fff74de90` (+ receipts and S80ScoutSources fixes `242744750e6a067fb55a33d6c70c944405e3737b`); wave mirror and registry receipts `499f7415bfea92a49954a1efd151937d82699fb2`; census-after `5865301b20b1d8ee9751c157e944b06999e9a70e`.
- Domain trial (C2 conjunct, real lane bytes): base and candidate `--dry-run` over three real lane targets in one layout, `TRIAL identical=yes`, 3 RESULT lines per arm (`census/round-80/records/c2-domain-trial.txt`; at R3 `census/round-80/records/repair3/domain-trial-at-R3.txt`).

## Landed changes

Every change below is tied to LOG.md `## Round 80` and to the commit that carries it.

| change | commit |
|---|---|
| counters, populations, control variants and receipts, rec.sh launch line, S327/S328 captures and rows, census-before, pre-freeze feasibility | `515d57c8c559d64d0c071cc25b07df0b815bd77a` |
| preregistration | `aaad410f4de2c1b0e98f1a7f305736dfcee5c5ab` |
| C1 candidate counter (+ freeze-check receipt) | `bd263c3f7d376e617c2fde5b99793622b0908b53` |
| C2 candidate tool | `836dac3e336863c57d9d7125837ed22b22d8d044` |
| after-arms, regressions, diagnosis receipts | `a4aa888037922b7b5ccfac7150f156f92af5916e` |
| knowledge, QUALITY Q144/Q145, README, SKILL, SCORECARD, LOG, lesson, v3-trial negative receipt, wave spec | `60c7f50eb803a6ee6d887fabdd32ab0e9e8102bc` |
| probe D (job control, spoofed session) failing at W2 | `37ab234e11de7436d268447bae79ccb535cff8f9` |
| repair R (set +m, worker parent check, nested-branch check, post-wait signals ignored) and its receipts | `8ba93218ce4e531651d754821e9c569a6509a2d2`, `e1b5caf94312022e5a8dd9da3fe223829f3fb4de` |
| probe D2 (worker killed, TMPDIR missing) failing at R | `330197b99b8ba751635009df52adbe36327f4c52` |
| repair R2 (session sweep after a killed worker, exit 1 on front mktemp failure) | `97289f81c08804090143008937bdbdb3d5fae9b7` |
| R2 receipts; S328 quote, knowledge precondition/limits, M1 cause, Q145, SKILL exit codes | `79fcc73dba05b038caf77c9285766bc57a4efa99` |
| probe D3 (newline in comm) failing at R2, racy v1 kept as diagnosis | `f6fcddb5d8998b091f267b65bac398377a55bd6f` |
| repair R3 (whole-file stat read; cite S075) | `4a499e9a7d0eeb853cc55e68fb3f453fff74de90` |
| R3 receipts; S075 citation and used-by, S294 used-by, S327/S328 cells restored to P; lesson Wave/Mistakes/Routed | `242744750e6a067fb55a33d6c70c944405e3737b` |
| wave mirror, w1 results, registry-agreement receipts | `499f7415bfea92a49954a1efd151937d82699fb2` |
| census-after | `5865301b20b1d8ee9751c157e944b06999e9a70e` |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | `census/round-80/controls/c1-K-a-r79-counter.txt`: `SUMMARY rows=18 mismatches=3 accepted=3 errors=0`, EXIT=1 (NF6b, NF8, NF10) | `census/round-80/records/c1-after.txt`: `SUMMARY rows=18 mismatches=0 accepted=0 errors=0`, EXIT=0; K-b refuse-all 18/18 but `resolved=3` of 22 on the r78 regression (EXIT=1); ablations without-regular / -capture-root / -whole accept 1 each (EXIT=1); r78 22/22 + 12/12, r77 35/35 + 7/7, r79 harness 9/9 | `python3 -B census/round-80/c1-false-row-harness.py --counter census/round-80/c1-pointer-counter.py --lane LANE --fleet-root FLEET --work WORK` | `bd263c3f7d376e617c2fde5b99793622b0908b53` (after-arm commit `a4aa888037922b7b5ccfac7150f156f92af5916e`) |
| C2 | `census/round-80/controls/c2-K-a-do-nothing.txt` (base tool `e2f2d083…`): `SUMMARY rows=15 mismatches=12 errors=0 orphans=12`, EXIT=1; K-b trap-only 12/12, K-c no-session-kill 12/12 | **A** `census/round-80/records/c2-after.txt`: `SUMMARY rows=15 mismatches=0 errors=0 orphans=0`, EXIT=0 (launched with `&`; every signal row's `ign=` at delivery is SIGQUIT only); r13 `total=5 failed=0 hung=0`; r17 `total=35 failed=0 skipped=2`; selftest `108 checks, 0 failed` on the committed file (`c2-regress-selftest-committed-mode.txt`) after a first replay on a copy read `81 checks, 51 failed` (`c2-regress-selftest.txt`); domain trial v3 identical | `python3 -B census/round-80/c2-signal-counter.py --tool-dir DIR --work WORK` | `836dac3e336863c57d9d7125837ed22b22d8d044` (tool blob `67ec160b…7181`; after-arm commit `a4aa888037922b7b5ccfac7150f156f92af5916e`) |

**C1** — counting command above; measured against W1 `bd263c3f7d376e617c2fde5b99793622b0908b53`.

- Verdict on the frozen predicate: **verified** (3 → 0; K-a 3; K-b red on its regression conjunct; all three ablations red; all three regressions green). S80ExecC1 reproduced every receipt byte-for-byte, the fixture revisions are deterministic, and no r77/r78 ITEM verdict moves between the r79 and r80 counters; S80Reviewer, S80CriticClaims and S80MutCounter re-derived the same numbers.
- Qualifications: the frozen artefacts kill only 3 of 9 rule mutants (S80MutCounter: no row holds a symlink member, so the 100644/100755 mode arm is unseen); a byte-equal decoy elsewhere under `census/round-32/` is still accepted (NF12, inside the preregistered "census/round-<N>" wording but unmeasured) and a path in parentheses is accepted (NF14); S327's page names no mode constants — the whitelist is grounded by S294 (git-fast-import(1) mode list), which the frozen counter's docstring does not cite (S80ScoutSources MEDIUM-1); the 18 rows are the previous wave's own findings (a regression statement, S80CriticClaims). The census carve-out is required by 14 real MOVED rows (S80CriticClaims), not tuned to the false rows. All routed to r81.

**C2** — counting command above; measured against W2 `836dac3e336863c57d9d7125837ed22b22d8d044`.

- Frozen predicate at A: the 15 rows, both controls and r13/r17 are met as written. Two conjuncts were first replayed with defective instruments and re-measured, which the closure must rule on: (1) the selftest conjunct on a `git show` copy outside the lane read 81/51 for the candidate **and identically for the base copy** (`records/diagnosis/selftest-base-mode0644-copy.txt`; S80ExecC2 reproduced it from the true base blob) — the cause is the copy's mode (4 checks) and layout (sibling engine, round-9 selftest, derived fleet root), not the candidate; the committed file reads 108/0 (S80Reviewer: "re-measurements of the FROZEN predicate, not a changed rule"; S80CriticClaims gives the strictest reading as red). (2) The domain-trial probe was rewritten twice after A (v1 compared two empty outputs; v2 ran the arms from different locations); v3 is identical with 3 RESULT lines per arm and is shown able to fail (`records/diagnosis/domain-trial-v3-refuses-empty.txt`).
- Harm at W2, found by three non-author seats (S80CriticDiscern F1 HIGH, S80CriticClaims item 10, S80Sentinel F1): with job control on in the tool's shell (`SHELLOPTS=monitor` exported, `bash -m`), the worker job is a group leader, setsid forks, the front exits 0 at once and the worker dies on its deleted TMPDIR — no verdict, where the base runs correctly (`records/repair/front-launch-modes-at-W2.txt`, 3/3 arms fail). **The W2 bytes therefore harm the no-signal behaviour under that launch; "no axis harmed" does not hold at W2.** Repaired after the wave (R/R2/R3), each behind a probe that fails on the earlier bytes; at R3 the frozen counter is 15/15 and 15/15 with `SHELLOPTS=monitor`, the three probes pass, r13 5/5, selftest 108/0, r17 35/0, trial identical (`census/round-80/records/repair3/`). These are post-wave repairs, not the claim's measurement.
- Qualifications: SIGKILL to the front leaves the worker session (untrappable; S80Sentinel F2); a signal in the instant between the launch and `$!` (S80Reviewer); the STOP pass and repeat passes are unmeasured (S80MutTool M01/M02 survive, likely equivalent); stage-2 signals leave the source moved with no RESULT line (S80ExecEvade F3, not a row).

No owned axis score changed (calibration 7, coverage 8, operability 8).

## Sources & frontier

- **Census.** Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
  - Before: `census/round-80/records/census-before.txt`, `souji ok`, EXIT=0 (87 W04 lines).
  - After: `census/round-80/records/census-after.txt`, `souji ok`, EXIT=0 (87 W04 lines).
- **Rows** (`grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`): 249 → 251.
  - Added: tier A ×2 — S327 git-ls-tree(1) as installed (git 2.56.0-1; docs, `mined`, grounds C1) and S328 setsid(1) as installed (util-linux 2.42.4-1; docs, `mined`, grounds C2). Both captured byte-for-byte under `census/round-80/srcs/`; located quotes and access date 2026-11-07 in `corpus/lessons/round-80.md` Gate.
  - Rejected: draft S329 (installed proc_pid_stat(5)) as a within-scope duplicate of S068/S075 (lesson Gate).
  - Rows touched old→new (used-by only): S075 `…round-18.md, …process-residue-observations.md` → `+ corpus/knowledge/gate-signal-handling.md`; S294 `corpus/lessons/round-63.md` → `+ corpus/lessons/round-80.md`. The S327/S328 anchor cells, edited in place during integration, were restored to their P bytes (S80ScoutSources LOW-2); corrections live in the lesson Gate.
  - Non-L1 re-open: S80ScoutSources (sha256 MATCH both, quotes verbatim, util-linux `setsid.c` fork condition confirmed) and S80CriticDiscern (3/3 decisions agree).
  - Registry gate: `tools/souji-registry-agreement.py` K1 base 7 → at I 8 (the entry cited the superseded S068; S80ScoutSources HIGH-1) → tip 7 (`census/round-80/records/registry-agreement-{base,at-I,tip}.txt`).
- **Frontier advanced.** README "Frontier (r80 quarantine signal handling and the r79 wave's false ledger rows)". It stays frontier.
- **Mistakes mined:** eight (`corpus/lessons/round-80.md` `## Mistakes` M1–M3, `## Mistakes (wave)` M4–M8), each with captured-by and a fix; M2's fix is shown able to fail (`records/diagnosis/domain-trial-v3-refuses-empty.txt`, EXIT=1), M4's probe fails on W2, M6's gate fails on the I bytes, M8's v2 probe fails 3 of 3 at R2.
- **Sourced claims:** C1 rests on S327, C2 on S328 (both opened this round).
- **Assimilation: none.** `considerthese/` is absent in this lane; no `merge/souji/` theme fits the frozen claims.

## Trend verdicts

- **expansion: improved** — two mined tier-A rows on ground the lane did not hold (tree-entry type and mode; setsid's exec-in-place condition), a new knowledge section on session fronts for `$(...)`-heavy tools, QUALITY Q144/Q145, two closure-gated capability rows, and a reusable disposition-controlled signal counter.
- **quality: unprovable-but-better** — the quarantine tool now leaves nothing running on a caller's signal (15/15 at A, at R3 also under job control, three probes), and the pointer counter refuses three more false rows; but C2's W2 bytes carried a harm the frozen rows could not see, two A-arm conjuncts needed re-measurement, and the C1 frozen set binds only 3 of 9 rule mutants. No single counter carries the net; the operator rules.
- **discernment: improved** — the L1 withdrew its own duplicate row (S329), refuted one seat finding with a measured counter-example (S80ScoutSources MEDIUM-2: a comm holding `) ` parses correctly) while accepting and repairing the others, restored append-only cells it had edited, recorded the harm at W2 against its own claim, and kept every defective receipt (selftest copy, v1/v2 trials, the racy v1 probe) as evidence rather than replacing it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md gate rows "r80 false-ledger-row harness (C1)" and "r80 quarantine signal counter (C2)" and the souji-quarantine exit-code row (`60c7f50e`, `242744750e`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md `## Round 80` — the quarantine dry-run on three real lane targets, base vs repaired tool byte-identical (`census/round-80/records/c2-domain-trial.txt`, `census/round-80/records/repair3/domain-trial-at-R3.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: twelve seats re-ran the prereg commands as written and reproduced every receipt (`census/round-80/records/wave-w1/seats/S80ExecC1.md`, `S80ExecC2.md`, `S80Reviewer.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: sibling tools were documented, not edited (`census/round-80/records/wave-w1/seats/S80Connector/sibling-overlap.tsv`); the misroot sweep found no file of this lane.

## Other

- **Round shape:** one v1 wave `w1` of 12 seats, validated under `ufo-wave-policy.json` (band 8–16; `ufo-swarm-wave-dispatch-v1`, spawn 12) and dispatched via the inline handoff (`w1.ready.dispatched` 04:39:56). WAVE-DONE received (`w1-results.json`, 12 results). No residual call; round total 12.
  - Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1. Attack seats 5 of 12 (42 %). The L1 holds the §3 planner seat.
- **Dead seats:** 0; all 12 wrote report files. S80ScoutSources ran ~90 min; the L1 messaged it once to write its report (it did).
- **Seat scratch defect:** a copy of the tool (`S80Sentinel-check.sh`) was left directly under `/fast/scratch/hyaku/souji-r80/`; removed with the round scratch root.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists orchestrator `.scratch/*`, the pre-existing `?? trail-ids.txt` and `?? f.txt` (04:40:38, content `x`); no souji seat script or report writes `f.txt` with that content (`grep -r 'f\.txt'` over the wave dir hits only the r17 fixture's own receipt, which writes `v1`/`v2` inside its `/var/tmp` fixture), so it is not attributed to this lane and was left untouched.
- **Routed to r81:** lesson `## Routed to round 81` (a)–(d) and SCORECARD "r81 (planned)".
- **Open L0 questions:** none new.
- **Tool installs:** none. No pacman transaction, no sysctl, sudo or kernel change.
- **Scratch:** `/fast/scratch/hyaku/souji-r80/` removed at landing.

## Stale-lane

Stale-lane: respawn-per-round driver; this lane has no other open mission.

Final lane hash: 5865301b20b1d8ee9751c157e944b06999e9a70e
