# mado — round 88 report (hyaku run 15, attempt 1, fresh start under Amendment 46)

Lane repo `mado-shokunin`, branch `master`; base `24ba2a9ddac21c1211579231e6ee1d98963f9988`; final lane hash
`8e8f7ea354cf23178ad08c400cd8aee9668d7bb3` (`git ls-remote origin refs/heads/master` prints it). L1: MadoR88.

## Work performed

Declared claims (2; frozen declaration `.ufo/waves/round-88/claims-declaration-r88.md`):
- **C1 — coverage, capability acquisition:** the mako resolver `tools/mado-mako.py` widened from 3 to 10 of mako 1.11.0's 12
  first-pass criteria fields (adds app-icon, summary, body, category, desktop-entry, actionable, expiring), with upstream's
  boolean grammar (`types.c parse_boolean`, which accepts the host's own DND lines `invisible=true/false` that r87 refused),
  upstream's urgency grammar and repeated-field last-wins. The stagnation nudge applies (no capability row since r82).
- **C2 — operability:** include= containment under declared read roots (`--home`, `--read-root`), closing r87 routed defect R2
  (a symlinked include escaping HOME was read).

Work items:
- Fresh-start reads: `corpus/lessons/round-85/86/87-verifier-spotcheck.md` routed defects; r87 R1 (five surviving mutants), R2
  (containment), R4 (pins at freeze) became the round's inputs (declaration §Fresh start).
- Motivating host evidence: the r87 resolver on the host chain refuses `core.ini:15/:18` and cannot resolve DND
  (`.ufo/waves/round-88/w1/receipt-base-host-config-r88.txt`; `w1/R88MExecSelftest.md` §5: Slack under DND → base `0`, candidate `1`).
- Built before the wave by the L1: tool changes, counters `quality/counters/c1-r88-mako-fields.py` and
  `c2-r88-include-containment.py` (both reuse the r87 machinery only after its sha pin matches), mutant lists.
- Wave w1 (12 seats, all settled): blind case authoring (scout for C1, scribe for C2), source opening (S494/S495), forgery,
  self-test and host-diff executors, knowledge/lesson/QUALITY drafts, connector overlap scan, two reviewers, critic,
  mutation-tester. Their findings became 7 listed draft revisions before the freeze (declaration `## Draft revisions`):
  anchor-absent → setup error, r87-case pin, `inputs-ignored` control, crash-is-not-a-kill, predicate boundary table and
  in-process `run()` pin tests, `--controls-only` receipts, urgency `high`/casefold (M20–M21), repeated-field last-wins (M22),
  NUL/`~//`/trailing-slash/relative-root hardening, K6–K7, cases k18–k26 and c60–c62 (L1-authored, disclosed, source-pinned).
- Controls executed and committed before the freeze (`receipts/c1-controls-prefreeze-r88.txt`, `c2-controls-prefreeze-r88.txt`).
- Freeze `9e36e3a3103349b939982e532feca443f02e660d` → C1 tool `650e18bdf0ae404ec9a80874c4503ecf3237e8e6` → C2 tool
  `7d3074865a9f5acfa0f1c9c66b460e73d4031331`; both measured TARGET_MET on the first scoring run.
- Residual r1 (4 attack seats on frozen/measured bytes): C1 VERIFIES, C2 VERIFIES (receipts reproduced byte-for-byte,
  `r1/R88MResidCasesC1.md`, `r1/R88MResidCasesC2.md`); critic `r1/R88MResidCritic.md` STANDS on both predicates, FALLS on the
  declaration's C2 "before" sentence (errata appended), WEAKENED on two stale ledger figures (fixed in `8e8f7ea3`).

## Landed changes

| commit (`landed`) | contents | LOG.md entry |
|---|---|---|
| `9e36e3a3103349b939982e532feca443f02e660d` | freeze: declaration, two counters, frozen cases/mutants, pre-freeze control receipts, census-start, w1 evidence, ledger rows | Round 88, "Landed" |
| `650e18bdf0ae404ec9a80874c4503ecf3237e8e6` | C1: `tools/mado-mako.py` (fields + grammar) | Round 88, "Landed" |
| `7d3074865a9f5acfa0f1c9c66b460e73d4031331` | C2: `tools/mado-mako.py` (containment + hardening) | Round 88, "Landed" |
| `498855cb327cd4e3debfa9446ea38398c216dda1` | records: `corpus/knowledge/mako-fields-containment-r88.md`, S494/S495, README row, `corpus/lessons/round-88.md`, QUALITY 146–147, SCORECARD Round 88 + capability row, LOG, measured receipts | Round 88, "Landed" |
| `8e8f7ea354cf23178ad08c400cd8aee9668d7bb3` | residual r1 evidence, post-measurement errata (declaration, SCORECARD), ledger row corrections, harm receipt | Round 88, "Residual r1" |

## Before → after measurements

- **C1** — `python3 -I quality/counters/c1-r88-mako-fields.py --repo . --rev 650e18bdf0ae404ec9a80874c4503ecf3237e8e6 --base-rev 24ba2a9ddac21c1211579231e6ee1d98963f9988 --cases .ufo/waves/round-88/controls/mako-cases-r88.json --expect-cases-sha256 a0e81b191fb0f80ca352699ede47962c1ac01c1ae8e9e15ccf50b1d7fab4a091 --expect-mutants-sha256 2a569770aa255cfaf0afc15c63136e8c261396ca280d5646c51171e9009864a1 --expect-r87-cases-sha256 0a9558743a721f70bb64b48d188b375f1468a140b00ca75ac93ab59c316d5fe3 --scratch-root DIR`.
  Before (r87 resolver as base-tool control on the frozen 62 cases): 33/62 = 5.3226 (21 of the 29 failures are CLI `exit=2`;
  inputs-ignored control 43/62). After at `650e18bd`: `TARGET_MET cases=62 correct=62 carried=22/22 mutants=22 killed=22
  naive_correct=14 globals_include_correct=15 base_tool_correct=33 inputs_ignored_correct=43 score=10.0000`, rc 0
  (`receipts/c1-measured-A-r88.txt`); fields modelled 3/12 → 10/12. Re-run at `7d307486`: identical verdict (`c1-harm-at-B-r88.txt`).
- **C2** — `python3 -I quality/counters/c2-r88-include-containment.py --repo . --rev 7d3074865a9f5acfa0f1c9c66b460e73d4031331 --base-rev 24ba2a9ddac21c1211579231e6ee1d98963f9988 --cases .ufo/waves/round-88/controls/containment-cases-r88.json --expect-cases-sha256 8b16c0cb0d73eb2e245b4b543db0a0396c824314cb8dbd26e5ad26214f20d039 --expect-mutants-sha256 ff76cd698875cfc1eff6f36d5997e3df79e3ef694c22c4feb720885179403616 --scratch-root DIR`.
  Before: the C1-revision tool scores 11/26 = 4.2308 (base-tool control with `--base-rev 650e18bd`, `receipts/c2-supp-base-is-A-r88.txt`;
  the counter itself exits 2 at `650e18bd`, erratum 1). After at `7d307486`: `TARGET_MET cases=26 correct=26 mutants=7 killed=7
  base_tool_correct=11 refuse_all_includes_correct=14 score=10.0000`, rc 0 (`receipts/c2-measured-B-r88.txt`).
- Harm watch at `498855cb` (`receipts/harm-final-r88.txt`): gate selftest 460/460, file plane CLEAN 29 pass, index 108 → 109/109,
  ledger 161 → 163 uncovered 0 (re-checked at `8e8f7ea3`: TARGET_MET), tool selftest 52/52, counter selftests 40/40 and 28/28.
  No axis harmed.

## Sources & frontier

- `SOURCES.md` rows 428 → 430 (`grep -c '^| S[0-9]' corpus/SOURCES.md` at `24ba2a9` and at the tip); added S494 (upstream mako
  v1.11.0 criteria.c/types.c/config.c, tag → `91c6b799…`, tier A, code) and S495 (path_resolution(7), man-pages 6.19-1, tier A,
  docs), both `mined`, opened 2026-11-06, Gate quotes in `corpus/lessons/round-88.md` §Gate. No row touched old→new.
- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`: start exit 0
  (`receipts/census-start-r88.txt`), end exit 0 (`receipts/census-end-r88.txt`); 55 `W04` + 1 `W01` before and after.
- Sourced claims: C1 rests on S494 (parse_boolean/parse_urgency/apply_criteria_field lines), C2 on S495.
- Mistakes mined (`corpus/lessons/round-88.md` `## Mistakes`): M88-1 (r87 encoded manual `0|1` and refused the host's DND lines;
  captured-by none → QUALITY 146), M88-2 (stance sentence and a blind-authored case typo; captured-by the loader for the typo →
  QUALITY 147), M88-3 (scratch root ownership, r85 R7).
- considerthese: `considerthese/2026-11-04.md` proposal 5 (coverage gaps from João's own desktop, notifications) — C1's host DND cases.
- Assimilation: none (no mako config-grammar or containment theme in `merge/mado/`; its S238 is the DND state indicator, R88MConnector §2).
- Frontier advanced: notification-daemon plane criteria fields 3/12 → 10/12 (core); summary~/body~ remain frontier.

## Trend verdicts

- **expansion — improved:** one admitted knowledge entry on ground no held note resolved (fields beyond app-name/urgency/mode,
  upstream grammar, containment), two new mined rows (S494, S495), one capability row.
- **quality — improved:** r87's five surviving mutants are killed by a superseding frozen case set; counters gained pin-before-exec,
  crash-is-not-a-kill and a boundary-tested predicate; two QUALITY criteria (146–147) each shown able to fail.
- **discernment — unchanged** (pending the non-author closure spot-check): the gate's admit (entry) and rejects (summary~ via Python
  `re`; containment as a mako rule) are recorded in the lesson's Gate for sampling.

## Round shape and extras

- Shape: ONE v1 wave w1 of 12 seats (scout 2, scribe 2, executor 3, connector 1, reviewer 2, critic 1, mutation-tester 1; attack
  4/12 = 33 %) + one residual call r1 of 4 attack seats (reviewer 2, critic 1, mutation-tester 1). Round total 16; dead seats 0
  (`w1-results.json`, `r1-results.json`). Planner seat held by the L1. Spawned via the inline handoff (`w1.ready`, `r1.ready`).
- Routed to round 89: R88MResidMut survivors — app-name casefold, `!` on a string field, mode casefold, include inside a criteria
  section (C1); opening the unresolved target, trailing-slash refusal dropped, `~//` re-join dropped, root-equality refused (C2).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/` (orchestrator-owned); no seat file misrooted.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `corpus/knowledge/mako-fields-containment-r88.md` §1 field table and §4 decision table (S493/S494/S495 lines); no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` Round 88 (host DND chain resolved by the candidate, `w1/R88MExecSelftest.md` §5; measured receipts); no non-author verifier.
- [~] Instructions executable by an agent without oral context — pointer: `tools/mado-mako.py` header (manual/upstream line map, containment stance) and the entry's decision table; no non-author verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` unchanged; the tool stays read-only within the mako config chain; no non-author verifier.
