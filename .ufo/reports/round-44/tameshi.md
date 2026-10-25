# Tameshi — round 44

author: tameshi L1 (hyaku run 6, attempt 1)
date: 2026-10-25
lane HEAD: `df000ab79a4c526bcb5cbf03a356c1a44fb32e27` (`master`, remote verified equal)

## Work performed

Declared claims: **C1 — calibration** (the lowest non-retired axis at freeze; repair the round-43 m7 false citation and reach zero across the seven frozen classes); **C2 — freshness** (add a current, opened S160 snapshot row superseding S089's stale anchor only). Freshness is newly tracked this round with a document-scoped 0→1 unit; no universal corpus-freshness claim is made.

- Replaced the round-43 m7 prose-only mask with assignment-value masking for `key=S###`; added four T6 selftests. The old counter still reports `m7=1` for the historical `safe_floor=S256`, while the successor clears that false hit and its unknown/unmined controls remain load-bearing. Evidence: `.ufo/evidence/round-44/before/c2-old-at-base.stdout`, `control/mask-removed.selftest.stdout`, `w1/RevSelftestAudit.md`.
- Re-opened the live Stryker page and committed its byte-identical 38,687-byte snapshot (sha256 `79f6501ad8f2a74e647532dba8f77f17482afa70ccbe6821d2368092454079ce`); appended mined S160 to supersede S089's stale digest anchor only. S089's row was not edited. Evidence: `corpus/lessons/round-44.md` `## Gate`, `corpus/SOURCES.md:130`, `.ufo/evidence/round-44/sources/stryker-equivalent-mutants.html`.
- Corrected the round-43 verifier's three routed defects: S256 assignment false alarm, the dirty reviewer note, and S089's stale anchor. The modified `.ufo/waves/round-43/w1/RevC2Classes.md` was retained with its A13/A14 line/pin corrections and committed under this round. Evidence: `corpus/lessons/round-43-verifier-spotcheck.md:12,63-65`; landed change commit `83beaf980f246412368f89fbe7758375c8ca21e0`.
- Mined mistakes into the round lesson: assignment-vs-citation scope, the incorrect staged-id premise in the wave item, and the initially stale standing count (m6=1 at the first content tip). Each fix has a red-before receipt or a guard/counter failure; see `corpus/lessons/round-44.md:79-97` and `.ufo/evidence/round-44/after/c1-at-83beaf9.stdout`.
- Frontier step: no shokuknow package entry was adopted (`Assimilation: none`). The staged package actually contains ids through S255, including staged S160 (PIT FAQ) already held as lane S156; the guard's by-document mapping is `staged:S160` → S156. The guard reported 8 intersecting ids S153–S160, unmapped 0, safe floor `safe_floor=S256`, and refusal of the cascading naive map. The initial wave item's claim that staged ids ended below S160 was wrong; it is corrected in the lesson/report, not hidden. Evidence: `w1/SentinelIdGuard.md`, `w1/CritC2Target.md`, `corpus/lessons/round-44.md` `## Gate`.
- Re-derived the quarantine slice read-only: 17 rows, 14 `payload-absent`, 3 `could-not-be-fetched`, byte-identical to the round-40 lesson; no new verdicts. Mined considerthese proposal 2 (unreachable-provenance check) as a future idea, not an implemented feature; m11 checks object existence, not branch reachability. Evidence: `w1/ScoutQuarantine.md`, `w1/ScoutConsiderthese.md`, `corpus/lessons/round-44.md`.
- Fleet-root misroot sweep used `git -C /home/vgpnk/Projects/shokunin status --porcelain` with no pathspec. No untracked file written by a round-44 tameshi seat was found; the untracked `.ufo/waves/round-24/w2/RevUnlandedResolution.md` is Tabi round 24 and was left untouched. Evidence: `w1/ScoutMisroot.md` and that file's header lines 1-6.
- One v1 wave: 32 seats, policy band 32–64; one batched task dispatch. Roles: 6 reviewer, 6 scout, 5 critic, 4 executor, 3 mutation-tester, 3 scribe, 2 sentinel, 1 simplifier, 1 connector, 1 revenger. The planner seat was held by the L1 per frozen-topology policy. All 32 completed; 0 dead seats observed; 32 seat reports plus settlement receipt are under `.ufo/waves/round-44/w1/`. Only 14 attack-role seats/items (reviewer/critic/mutation-tester) returned, below the 32-item wave-2 threshold; all checks were assigned and no residual items remained, so no wave 2 or residual call was needed. Evidence: `spec-w1.json`, `dispatch-w1.json`, `w1/summary.md`.

## Landed changes

- Counter, contract, Stryker snapshot and base receipts: freeze/update commits `05b3bd222c928694f768a80fa8a3fd2f05cd5d46` and `ba01973c73ad7de60e5bd19ae08255a1b7ef917e`; corresponding round-44 `LOG.md` entry at `LOG.md:2265+`.
- Validated wave spec, dispatch payload and registry: `8bffd9b5d4f014e449d55e970639aeac69255a3e`; census-start receipt: `315453b821e4c7732ea4de09f0478ff5976c2c42`.
- S160 row, knowledge entry, round lesson, full seat findings, retained round-43 wave note and first scorecard/log entry: `83beaf980f246412368f89fbe7758375c8ca21e0`.
- Corrected the stale m6 standing count and recorded its observed failure: `ef990aaea3f6546db20feccbff89ac9ab78c5405`.
- Recorded the seven-class pass, no-harm receipts, census exit codes and scorecard/log outcome: `224084879aa9c687d6c6bc6e8eb14196fddf39fb`.
- Wave settlement accounting: `df000ab79a4c526bcb5cbf03a356c1a44fb32e27`.

All lane changes are tied to the round-44 `LOG.md` entry/addendum; `jj-lane.sh state` and `git ls-remote origin refs/heads/master` both reported `df000ab79a4c526bcb5cbf03a356c1a44fb32e27`, `ahead=0`.

## Before → after measurements

- **C1 calibration.** Frozen command: `python3 .ufo/evidence/round-44/calibration/measure.py --lane LANE --rev REV --freeze ba01973c73ad7de60e5bd19ae08255a1b7ef917e`. At base `506e99c7b73c85711f066895984d501fcf7539cd`, the round-43 counter found `m7=1 total=1`, first hit the historical floor-value assignment; the round-44 counter removed that false m7 (`m7=0`) but correctly reported m12=1 because the newest scorecard block was still round 43. The first content-tip run at `83beaf980f246412368f89fbe7758375c8ca21e0` found `m6=1 standing=114 actual=115`; the new standing row fixed this without changing the target. At the final lane tip `df000ab79a4c526bcb5cbf03a356c1a44fb32e27`, the command exited 0 and printed:

  ```
  C2_R44: self_pin=1 classes=7 m6=0 m7=0 m8=0 m10=0 m11=0 m12=0 m13=0 total=0 records=4 sources_rows=115 standing=115 receipts=17 revisions=4 m13_probe=standing=8_column0=114_valid=115 rev=df000ab79a4c526bcb5cbf03a356c1a44fb32e27 freeze=ba01973c73ad7de60e5bd19ae08255a1b7ef917e C2_R44_PASS=true
  ```

  Red-before: removing only the `ASSIGN_ID` mask makes T6 fail twice with `['r unknown S256']`, exit 1; receipt `.ufo/evidence/round-44/control/mask-removed.selftest.stdout`. Full 16-case selftest was PASS; `w1/RevSelftestAudit.md` mutation-tested every case.
  Scope note: `w1/RevPredicateSame.md` flagged that the frozen C1 sentence is wider than the seven-class `C2_R44_PASS` label (which is the counter's inherited class name, not the scorecard claim number). The output proves the seven-class zero-hit predicate; the assignment-specific behavior is separately supported by the 16-case selftest, mask-removal red-before, and per-case mutation audit. No predicate was changed after the wave/data.
- **C2 freshness.** `grep -cE '^ {0,3}\| S160 ' corpus/SOURCES.md`: 0 (exit 1) at base `506e99c7b73c85711f066895984d501fcf7539cd` → 1 (exit 0) in the final lane revision `df000ab79a4c526bcb5cbf03a356c1a44fb32e27`. Root census: start exit 0, 114 rows; end exit 0, 115 rows, no E-codes and one added expected W04 duplicate-URL warning for S160. Receipts: `.ufo/evidence/round-44/before/s160-count.*`, `after/s160-count.*`, `census-start.{stdout,stderr,exit}`, `census-end.{stdout,stderr,exit}`.
- No-harm: command D printed `recorded_cases=9 depth_score=9` at base and measured revision; the coldread monitor returned calibration restraint 6 and 60/64 sections at both. Depth remains 9; calibration restraint remains 6. Receipts: `.ufo/evidence/round-44/{before,after}/commandD.*` and `coldread.*`.

## Sources & frontier

`SOURCES.md` census-valid rows: 114 → 115. Added by tier: A=1 (S160, docs, mined), B=0, C=0. Existing rows touched old→new: none; S089's status, recheck, anchor and used-by cells are unchanged. Its stale digest is superseded by S160's fresh snapshot anchor only. Frontier rows advanced: none. Assimilation: none. Package quarantine remains the 17 round-40 verdicts (14 payload-absent, 3 could-not-be-fetched); no package rows were appended. New row S160 was opened this round and cited by `corpus/knowledge/r44-anchor-refresh-rule.md`; its located quotes, access date and digest are in `corpus/lessons/round-44.md` `## Gate`.

Start census command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`
(exit 0; receipt `.ufo/evidence/round-44/census-start.stdout`):

```
tameshi	W04	S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S075 duplicate url man7.org/linux/man-pages/man1/strace.1.html across scopes
tameshi	W04	S076 duplicate url docs.jj-vcs.dev/latest/git-compatibility across scopes
tameshi	W04	S077 duplicate url man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html across scopes
tameshi	W04	S078 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
tameshi	W04	S081 duplicate url bazel.build/reference/test-encyclopedia across scopes
tameshi	W04	S092 duplicate url bazel.build/remote/caching across scopes
tameshi	W01	S101 tierC mined used-by=corpus/knowledge/witness-equivalence-rule.md
tameshi	W04	S104 duplicate url cgit.git.savannah.gnu.org/cgit/bash.git/plain/doc/bashref.texi?id=b8c60bc9ca365f8261fa97900b6fa939f6ebc303 across scopes
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
```

End census command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`
(exit 0; receipt `.ufo/evidence/round-44/census-end.stdout`):

```
tameshi	W04	S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S075 duplicate url man7.org/linux/man-pages/man1/strace.1.html across scopes
tameshi	W04	S076 duplicate url docs.jj-vcs.dev/latest/git-compatibility across scopes
tameshi	W04	S077 duplicate url man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html across scopes
tameshi	W04	S078 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
tameshi	W04	S081 duplicate url bazel.build/reference/test-encyclopedia across scopes
tameshi	W04	S092 duplicate url bazel.build/remote/caching across scopes
tameshi	W01	S101 tierC mined used-by=corpus/knowledge/witness-equivalence-rule.md
tameshi	W04	S104 duplicate url cgit.git.savannah.gnu.org/cgit/bash.git/plain/doc/bashref.texi?id=b8c60bc9ca365f8261fa97900b6fa939f6ebc303 across scopes
tameshi	W04	S160 duplicate url stryker-mutator.io/docs/mutation-testing-elements/equivalent-mutants across scopes
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
```

## Trend verdicts

- **expansion: unchanged** — no uncovered coverage-map ground or frontier row moved; the new entry is an anchor-refresh correction, not new domain coverage.
- **quality: improved** — the stale Stryker digest is re-opened and superseded with a fresh, byte-verified snapshot; S089 remains preserved as history and the new row cites its replacement knowledge entry.
- **discernment: unchanged** — the lane recorded its admit and duplicate-package refusal, but no independent closure spot-check had landed at report time; no self-assessed taste improvement is claimed.

## SHONEN

- [~] SKILL.md contains decision tables, error patterns, checklists and cited sources — prior pointer `reports/round-1-calibration.md#box-1`; no new non-author verifier this round.
- [~] At least one end-to-end domain task executed and logged — prior pointer `reports/round-1-calibration.md#box-2`; no new promotion verdict this round.
- [~] Instructions executable without oral context — prior pointer `.ufo/evidence/round-21/coldread/ledger.json`; no independent promotion verifier this round.
- [~] No cross-domain bleed — prior pointer `reports/round-1-calibration.md#box-4`; no new PROVINCE adjudication this round.

Stale-lane: respawn-per-round; no other mission of tameshi is open.
Tools installed/updated: none.
Open L0 questions filed this round: none.
