# mado — round 89 report (hyaku run 15, attempt 1)

Lane repo `mado-shokunin`, branch `master`; base `af998dcc41d48618ffe7afe0efc9354755a9244e`; final lane hash
`16ee97b5a398d0d51b605670f35feb059a5487b6` (`git ls-remote origin refs/heads/master` prints it). L1: MadoR89 (holds the planner seat).

## Work performed

Declared claims (2; frozen declaration `.ufo/waves/round-89/claims-declaration-r89.md`):
- **C1 — coverage, capability acquisition:** mako `summary~`/`body~` criteria, refused by the round-88 tool, are now modelled the
  way mako 1.11.0 matches them: libc `regcomp(REG_EXTENDED | REG_NOSUB)` + unanchored `regexec` through ctypes, in the C locale
  (the v1.11.0 tree never calls setlocale), every occurrence compiled, "cannot set both", behind upstream's `parse_criteria`
  escape and space-only rules. MODELLED_FIELDS 10 → 12.
- **C2 — operability:** a new runnable survivor gate (`quality/counters/c2-r89-survivor-kills.py` + two supplementary case sets)
  kills 7 of round 88's 8 routed residual survivors; RM6C2 declared crash-only before data.

Work items:
- Fresh inputs: `corpus/lessons/round-88-verifier-spotcheck.md` routed R1–R5 and `.ufo/waves/round-88/r1/R88MResidMut.md` §3–§4
  became the claims' inputs (declaration §Inputs). R5 closed: the r88 `*.ready.dispatched` markers committed in the freeze `d8736135`.
- Built before the wave by the L1: candidate `.ufo/waves/round-89/build/mado-mako.c1.py`, independent C oracle
  `controls/posix-ere-oracle.c`, both counters, mutant/survivor lists, r01–r30 cases (generator with its own parse_criteria replica,
  `controls/gen-c1-cases-r89.py`), C2 supplementary sets.
- Wave w1 (12 seats, all settled, `w1-results.json`): blind cases b01–b45 (R89MScoutCases), sources S496–S500 opened
  (R89MScoutSources), entry + lesson drafts (R89MScribeEntry), host replay — base decides 4/9 host criteria sections, candidate 9/9
  (`w1/R89MExecHostDiff.md`), differential fuzz 12 800 candidate/oracle comparisons with 0 disagreements, Python `re` disagreeing on
  404/3200 (`w1/R89MExecFuzz.md`), forgeries (`w1/R89MExecForgery.md`), guards fail closed rc 2 (`w1/R89MExecSelftest.md`),
  `Assimilation: none` (`w1/R89MConnector.md` §2), two reviews, critic, mutation-tester. Findings became draft revisions before the
  freeze (declaration `## Draft revisions`): earlier-invalid-occurrence fix (ReviewC1 F1), M33–M37, cases r31/r32/n04/n07, the
  critic's axis/provenance/concrete-target/sequencing changes (F2–F11).
- Freeze `d87361354b4d142287aac05bb973315749ef1fce` with pre-freeze control receipts; C2 measured at the freeze; C1 tool landed at
  `099c662dc55521e365cd4126132cdcda4efc54b6` (candidate bytes unchanged, sha256 6b4bc409…) and measured; records; residual r1.
- Residual r1 (4 seats, all settled, `r1-results.json`): C1 VERIFIES (`r1/R89MResidC1.md`), C2 VERIFIES (`r1/R89MResidC2.md`), critic
  F1–F8 corrected in the final commit (`r1/R89MResidCritic.md`), mutation probe survivors RS01/RS05/RS12 routed to round 90
  (`r1/R89MResidMut.md` §7).

## Landed changes

| commit (`landed`) | contents | LOG.md entry |
|---|---|---|
| `d87361354b4d142287aac05bb973315749ef1fce` | freeze: declaration, two counters, frozen cases (141) / mutants (37) / survivor sets, oracle, generator, pre-freeze receipts, census-start, w1 evidence, ledger rows, r88 dispatch markers | Round 89, "Landed" |
| `099c662dc55521e365cd4126132cdcda4efc54b6` | C1: `tools/mado-mako.py` (summary~/body~ via libc ERE, tokenizer escapes) | Round 89, "Landed" |
| `51bf076fd970106da854e11873b886528c3cffaf` | records: `corpus/knowledge/mako-regex-criteria-r89.md`, S496–S500, S493/S494 used-by, README rows, `corpus/lessons/round-89.md`, QUALITY 148–149, ledger, SCORECARD Round 89 + capability row, LOG, measured receipts | Round 89, "Landed"/"Measured" |
| `16ee97b5a398d0d51b605670f35feb059a5487b6` | residual r1 evidence, harm and end-census receipts, errata (declaration, SCORECARD), critic corrections | Round 89, "Residual r1" |

## Before → after measurements

- **C1** — `python3 -I quality/counters/c1-r89-mako-regex.py --repo . --rev 099c662dc55521e365cd4126132cdcda4efc54b6 --base-rev af998dcc41d48618ffe7afe0efc9354755a9244e --cases .ufo/waves/round-89/controls/mako-cases-r89.json --expect-cases-sha256 5fdca7dbcce6687d81aa31548e935a49fa39cee03117db41358068a0ded15672 --expect-mutants-sha256 5471bee29b4ba5da7fa7e55d8b11003028b0eb4c7937bd8d114062491338e35f --expect-r88-cases-sha256 a0e81b191fb0f80ca352699ede47962c1ac01c1ae8e9e15ccf50b1d7fab4a091 --scratch-root DIR`, measured at `099c662d`.
  Before: round-88 tool (base-tool control) 78/141; fields 10. After: `MADO_MAKO_REGEX: TARGET_MET cases=141 correct=141 carried=61/61
  mutants=37 killed=37 naive_correct=34 globals_include_correct=35 base_tool_correct=78 python_re_correct=127`, rc 0
  (`.ufo/waves/round-89/receipts/c1-measured-A-r89.txt`); fields 12 (count command in the declaration).
- **C2** — `python3 -I quality/counters/c2-r89-survivor-kills.py --repo . --rev d87361354b4d142287aac05bb973315749ef1fce --expect-survivors-sha256 9f25df3cac28d9085d2e7d2a89e6002df24f76e6c5264df98f83d4d32c8104f0 --expect-c1side-sha256 c710a3e5a2a0e88692de68c6dec9815f14f5964099ec7ef6fdb8cb20bb743c1a --expect-c2side-sha256 e02e2b4de83410ab16fcf7ad92f5374c5178a3e49c80d6aa2c4994e0d04e612e --scratch-root DIR`, measured at the freeze `d8736135` (tool = round-88 tool, `tool_sha256=c374d715…`).
  Before: round-88 frozen sets kill 0/7 (`receipts/c2-controls-prefreeze-r89.txt`), tool `--selftest` 3/7
  (`receipts/c2-selftest-control-r89.txt`). After: `MADO_MAKO_SURVIVORS: TARGET_MET cases=95 correct=95 counted=7 killed=7
  do_nothing_B_only_killed=0`, rc 0 (`receipts/c2-measured-F-r89.txt`); re-run at `099c662d` identical verdict (`receipts/c2-harm-at-A-r89.txt`).
- Harm watch at `51bf076f` (`receipts/harm-final-r89.txt`): gate selftest 460/460, file plane CLEAN 29 pass, index 109 → 110/110,
  ledger 163 → 165 uncovered 0, tool selftest 59/59, counter selftests 27/27, 18/18, 40/40, 28/28. No axis harmed.

## Sources & frontier

- `SOURCES.md` rows 430 → 435 (`grep -c '^| S[0-9]' corpus/SOURCES.md` at `af998dcc` and at `16ee97b5`). Added (all tier A, `mined`,
  opened 2026-11-06, Gate quotes in `corpus/lessons/round-89.md` §Gate): S496 regex(3), S497 regex(7), S498 setlocale(3), S499 glibc
  `<regex.h>`, S500 mako v1.11.0 tag tarball (docs 3, code 2). Touched old→new: S493 and S494 `used-by` + the r89 entry (logged).
  Considered, not appended: POSIX Issue 8 ch. 9 and `regcomp()` pages (no admitted entry cites them).
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`: start exit 0
  (`receipts/census-start-r89.txt`), end exit 0 (`receipts/census-end-r89.txt`); 55 `W04` before and after.
- Sourced claim: C1 rests on S496/S498/S499/S500 opened this round (entry `corpus/knowledge/mako-regex-criteria-r89.md` source line).
- Mistakes mined (`corpus/lessons/round-89.md` `## Mistakes`): M89-1 (r88 residual seat routed a crash as a distinguishing probe;
  captured-by none → QUALITY 148), M89-2 (r88 tokenizer kept `\` inside quotes and split on any whitespace; captured-by no r88 case
  → QUALITY 149, killed by r14/r16 via M30/M31), M89-3 (symbolic N / old-row sourcing in the draft; captured by the w1 critic),
  M89-4 (records cited uncommitted receipts — repeat of r88 R4; check proposed for r90, not claimed).
- considerthese: `considerthese/2026-11-06.md` proposal 1 (survivor ledger) → C2; proposal 3 (host theme check) → R89MExecHostDiff.
- Assimilation: none (no regex/notification-criteria theme in `merge/mado/`, `w1/R89MConnector.md` §2).
- Frontier advanced: notification-daemon criteria fields 10/12 → 12/12 of MODELLED_FIELDS (core); group-index/grouped stay frontier.

## Trend verdicts

- **expansion — improved:** one admitted entry (109 → 110) on ground the coverage map did not hold (regex criteria, C locale,
  tokenizer), five new mined rows, one capability row; host criteria sections decided 4/9 → 9/9.
- **quality — improved:** case set 62 → 141 with 37/37 mutants killed incl. two independent forgery classes (python-re 127/141,
  base 78/141); 7 of 8 routed r88 survivors killed by a runnable gate; QUALITY 148–149 each with a shown failure; r1 corrections landed.
- **discernment — unchanged** (pending the non-author closure spot-check): the Gate records admits (entry) and rejects (Python `re`,
  unpinned locale, anchored match, assimilation) for sampling.

## Round shape and extras

- Shape: ONE v1 wave w1 of 12 seats (scout 2, scribe 1, executor 4, connector 1, reviewer 2, critic 1, mutation-tester 1; attack 4/12
  = 33 %) + one residual call r1 of 4 attack seats (reviewer 2, critic 1, mutation-tester 1; hand-built dispatch, the v1 validator
  refuses <8 lanes: `r1-run.err`). Round total 16; dead seats 0. Planner seat held by the L1. Spawned via the inline handoff.
- Routed to round 90: R89MResidMut survivors RS01 (body~ earlier-invalid), RS05 (quoted bare token), RS12 (group-index accepted);
  M89-4 receipt-presence check.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/` (orchestrator-owned); none misrooted.
- Scratch: `$HYAKU_SCRATCH/mado-r89` removed after landing.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `corpus/knowledge/mako-regex-criteria-r89.md` §2 decision table (glibc ERE vs Python `re`, S496–S500); SKILL.md unchanged; no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` Round 89 (host mako chain replay, 9/9 sections decided, `w1/R89MExecHostDiff.md`); no non-author verifier.
- [~] Instructions executable by an agent without oral context — pointer: `tools/mado-mako.py` header (criteria.c/regex.h line map) and the declaration's exact measurement argv; no non-author verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` unchanged; the tool stays read-only within the mako config chain; no non-author verifier.
