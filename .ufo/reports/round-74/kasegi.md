# kasegi — round 74 (attempt 1)

Lane HEAD at filing: `dca80cf52c5d640ec8be3465fc4aa8e7c5648cc1` (pushed; `ls-remote origin refs/heads/master` = `dca80cf5…`). Freeze `847b5379` (`.ufo/waves/round-74/claims.json`); base and controls revision `ccd6a54bf392922495c4860332665499582e3213`; pre-freeze controls commit `654d877f`. Lesson `corpus/lessons/round-74.md`; LOG entry `LOG.md` § Round 74; SCORECARD section `SCORECARD.md` § Round 74.

## Work performed

Declared claims (2, both frozen before any candidate measurement):

- **C1 — depth:verifiability** (lowest non-retired axis, score 4, nominal per QUALITY R58). Counter amendment to `corpus/instruments/recheck-cwd-census.py` so that its own `--selftest` kills the four mutant classes that survived the round-73 selftest (RC-1 to RC-3: forced `conformant` result, hard-coded `/tmp` scratch parent, scratch leak, last-line reader). **Verdict: VERIFIED on the frozen after-predicate and kill rule (a)-(d); scope sentence WEAKENED as written (see M74-6).**
- **C2 — coverage** (score 8). Admit Frontier F52 on source S109, the Fuzzilli project's own README (`https://github.com/googleprojectzero/fuzzilli`), with one knowledge entry. **Verdict: VERIFIED on the frozen counters and kill rule; two registry/capture clauses lacked a measuring command at freeze (measured independently, not frozen).**

Work items, with evidence pointers:

- Load order, protocol files, lane state, prior-round evidence: `skill://shokunin`, `skill://swarm`, MISSION/AXES/CORPUS/LEARNING, `SCORECARD.md`, `corpus/lessons/round-70..73` spot-checks (the three rejected closures r70 to r72 and the r73 spot-check read before declaring; `.ufo/prompts/kasegi-round-74.md` §1-§7).
- Round-start census: `.ufo/waves/round-74/controls/census-before-r74.txt` (exit 0, `kasegi ok`, six inherited W04 warnings).
- Round-73 post-landing receipts committed (routed defect R73-V4): `.ufo/waves/round-73/controls/post-landing-frontier-census-r73.txt`, `post-landing-capture-binding-r73.txt`.
- Pre-freeze do-nothing and red-before controls: `.ufo/waves/round-74/controls/c1-redbefore-mutant-survival-r74.txt` (four mutants each exit 0 with `cases=1 failures=0` on the unamended counter); `c1-base-census-r74.txt`; `c2-base-counters-r74.txt`.
- Freeze `847b5379` and replay: `.ufo/waves/round-74/controls/freeze-check-replay-r74.txt` (R73-V6; first block corrected by an appended block, M74-2).
- One v1 wave `w1`, 12 seats (`.ufo/waves/round-74/w1-spec.json`, `w1-dispatch.json`, `w1-results.json`); seat reports under `.ufo/waves/round-74/w1/`.
- C1 implementation (`ExecC1Amend`, applied by the integrator from `.ufo/waves/round-74/w1/ExecC1Amend.patch`): selftest 1 → 5 cases; `first_recheck`, `run_foreign`, `census`, `main` byte-identical. Integrator measurements on the lane tree: `--selftest` `selftest cases=5 failures=0` exit 0; census `entries=89 noprefix=0 exit2_foreign=0 exit0_foreign=67 exit1_foreign=22 exit_other=0 norecheck=0`, `RECHECK-CWD-RESULT conformant`, exit 0.
- C1 kill battery: seat `ExecC1Amend` (`ExecC1Amend-kills.txt`) and an independent battery by `MutAuditC1` (`MutAuditC1-evidence.txt`; M4p, M4b, M5p, M6p, M7p, M8p, M11p all KILLED) and the integrator rebuild of M4-M7 from the amended lane file (each `--selftest` exit 1, `failures=1`).
- C1 parity: amended and base counters on the base export produce byte-identical stdout (sha256 `e1906b886e856fa688f01f08b28a5034e5979adc311d3a040e7642776770f241`, seat receipt `ExecC1Amend-parity.txt`), equal to `c1-base-census-r74.txt`.
- C2 capture: `corpus/source-snapshots/round-74/S109.txt` (`capture-source.py`, `fetched_utc` 2026-11-05T08:28:10Z, status 200, sha256 `c9a7adfbd34966cbd002a4c1da75e094de8db500ee77d4bce77bca6f0568d486`, 375 lines); capture integrity re-fetched byte-identical by `ScoutSurface` (`ScoutSurface.md`). The lead URL `https://github.com/google/fuzzilli` returns 404 (HTTP probe, recorded); the admitted URL is `googleprojectzero/fuzzilli`.
- C2 manifest: the seat's draft carried `fetched_utc: null` and a non-existent `path`; the integrator rebuilt `corpus/source-snapshots/round-74/manifest.json` from the capture tool's own fields, quotes byte-identical (M74-5). `source-recheck.py` exit 0, 16 of 16 `anchor=<n>-ok`, longest quote 22 words.
- C2 entry: `corpus/knowledge/fuzzilli-js-engine-fuzzing-framework.md` (provenance trio; `verified-at` 2026-11-05; cd-prefixed recheck; 57 quotes checked against the capture by `ScribeEntry-verify.txt`, BAD=0). Integrator edit before landing: the title, Claim 1 heading and ground line used the compound "coverage-guided"; changed to the printed `"(coverage-)guided"` (ReviewC2 §2.1). Entry recheck exit 0 from `/tmp`.
- Registry/leads/frontier/PROVINCE/QUALITY edits: `corpus/SOURCES.md` (S109 row; OSV overview and NDSS leads; registry note), `corpus/README.md` (`## Round-74 admission`, F52 row), `PROVINCE.md` (r74 F52 line), `corpus/instruments/knowledge-expected.txt` (+1 row, sort-clean), `corpus/QUALITY.md` (R119 Gate reject line; R120 supersession of the round-73 R33 row).
- Non-claim work (considerthese proposal 2, the end-to-end task requirement, R73-V5): a documentation-only claim-package trial on a disclosed, already-fixed curl CVE (CVE-2023-38545): `.ufo/waves/round-74/w1/trial/package/` (six files), `claim-package-check.py` → `rules=8 pass=8 fail=0 verdict=WELL-FORMED exit=0`; `status.json` `claimable: false`, blocker `operator-gated: no authorized live program`; pricing `.ufo/waves/round-74/w1/trial/pricing-note.md` against F13, F17 and F18 (no VSCS level, no CWE-122 crosswalk node, CVE absent from the pinned KEV feed). No live-target contact, no submission.
- Sentinel review: `SentinelCounter.md` — zero new exec sites in the amended counter; the `bash -c` call count is 1 before and after; no unredacted secret hits in the trial tree (R-NOSECRET lens). RC-8 unchanged (operator decision pending).

Hard bounds observed: write scope lane repo plus the fleet report and `l0-questions` only; no MANIFEST, `.ufo/state/`, watchdog, `templates/` or `scripts/` edit; no sibling repo write; no pacman transaction; live HTTP limited to public documentation pages named in the items (GitHub repository page, the OSV overview page as lead-only, curl.se advisory and policy pages).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Pre-freeze controls (red-before mutants, C1/C2 base counters, round-start census, round-73 post-landing receipts) | `LOG.md` § Round 74 | `654d877f` |
| Freeze: `claims.json` and the S109 capture | `LOG.md` § Round 74 | `847b5379` |
| Freeze-check replay receipt (R73-V6; untracked at the freeze, found by the critic) | `LOG.md` § Round 74 | `a5e814a1` |
| C1 counter amendment; C2 entry, manifest, registry, leads, F52 frontier, PROVINCE, knowledge-expected, QUALITY R119/R120; lesson; SCORECARD; LOG; wave evidence `w1` | `LOG.md` § Round 74 | **`dca80cf5`** (final; `landed dca80cf5…`) |

## Before → after measurements

**C1 (depth:verifiability, nominal 4 → 4).** Counting commands:

- Before (base `ccd6a54`, unamended counter): `TMPDIR=<scratch> python3 corpus/instruments/recheck-cwd-census.py --selftest` → `selftest cases=1 failures=0`, exit 0; M4, M5, M6, M7 mutants each the same, exit 0 (`controls/c1-redbefore-mutant-survival-r74.txt`).
- After (`dca80cf5`, amended counter): `--selftest` → `selftest cases=5 failures=0`, exit 0; the four mutants → exit 1 each; census `entries=89 noprefix=0 exit2_foreign=0 exit0_foreign=67 exit1_foreign=22 exit_other=0 norecheck=0`, `RECHECK-CWD-RESULT conformant`, exit 0; parity byte-identical (`ExecC1Amend-parity.txt`).
- Frozen kill rule: (a) four classes killed, PASS; (b) parity byte difference 0, PASS; (c) conformant positive control prints `conformant` exit 0, PASS; (d) `bash -c` count 1 before, 1 after, PASS.
- Score: held at 4 (nominal per QUALITY R58; the scored `resolve.py` census is not read by this gate).

**C2 (coverage, 8 → 8).** Counting commands and values:

- Before (`ccd6a54`): `frontier-recheck-count.py` `FRONTIER-CENSUS rows=51 admitted=51 closed=51 problem-rows=0 registry=108`, `entries=54 pass=54 exit=0`; `capture-binding-check.py` `records=87 bound=87 unbound=0`; registry rows 108; knowledge 89; knowledge-expected 91 lines / 89 rows.
- After (`dca80cf5`): `FRONTIER-CENSUS rows=52 admitted=52 closed=52 problem-rows=0 registry=109`, `PASS F52 ids=S109 exit=0`, `entries=55 pass=55 exit=0`; `capture-binding-check.py` `records=88 bound=88 unbound=0` exit 0; registry rows 109 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); knowledge 90; knowledge-expected 92 lines / 90 rows, `LC_ALL=C sort -c` exit 0, set-equal to the knowledge files; `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` exit 0.
- Pre-existing registry rows unchanged: `git diff ccd6a54 -- corpus/SOURCES.md` → 0 removed lines, 4 added.
- Score: held at 8 (the coverage denominator is operator-owned).

## Sources & frontier

- **`corpus/SOURCES.md` rows, before → after:** 108 → 109 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; `sources-census.sh` exit 0 before and after).
- **Rows added by tier:** S109 — tier A (docs, scoped to the project's own README statements), status `mined`, opened 2026-11-05, recheck 90d, used-by `corpus/knowledge/fuzzilli-js-engine-fuzzing-framework.md`. No tier B or C row added. (Two leads added without rows: the OSV.dev overview page and the NDSS 2023 paper, both recorded in `## Leads (unopened)` only.)
- **Rows touched old → new:** none. No pre-existing `status`, `recheck`, `used-by`, `id` or `URL` cell changed (`git diff ccd6a54 -- corpus/SOURCES.md`: 0 removed lines). The Fuzzilli lead (base line 172, tip line 173) is kept byte-identical and retired as opened in the registry note.
- **Frontier rows advanced:** F52 (Fuzzilli tool documentation) admitted; 51 → 52 admitted. Frontier amendment lines in `corpus/README.md` `## Round-74 admission` and `PROVINCE.md` (r74 F52).
- **Assimilation:** none. `merge/kasegi/` was not adopted; the staged package's id collision (`.ufo/waves/round-74/assimilation/collisions`: 78 of 94 staged ids collide with the 108-row registry at base) keeps adoption closed under the r70/r71 L0 rows. `considerthese/` proposal 2 was mined as the non-claim trial; no considerthese candidate was admitted to the corpus.
- **Frontier step (§2b):** mistake mined (M74-1 to M74-8 in `corpus/lessons/round-74.md` `## Mistakes`); a sourced claim (C2 rests on S109, opened and captured this round); SOURCES row S109 opened this round; the lesson's `## Gate` records one admit and rejects (the OSV overview page as a row; the NDSS paper not opened; the considerthese candidate).
- **Census (round end):** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` exit 0 (`kasegi ok`).

## Trend verdicts

- **expansion: improved.** One net new admitted knowledge entry (F52) on ground the coverage map did not hold: the Fuzzilli tool's own documentation (`corpus/README.md` `## Round-74 admission`; `corpus/knowledge/fuzzilli-js-engine-fuzzing-framework.md`, source S109). The distinctness screen is recorded per clause (`claims.json` `distinctness_screen`; `ScoutSurface.md`; sibling scan `ConnectorSweep.md` §2).
- **quality: unchanged.** No admitted entry was superseded or re-verified against a changed source this round, and none was found false. The C1 counter repair closes four measured survivors of its own selftest, which is evidence about the instrument (depth:verifiability), not a re-verification of corpus entries. R33 is still held twice in `corpus/QUALITY.md` (line 292 and 550; M74-3, recorded not repaired).
- **discernment: improved.** The round-73 non-author spot-check disagreed with the gate on the Gate's reject lines (R73-V1); that disagreement became a lesson (M74-1) and a grounded criterion (QUALITY R119). Its other findings were routed or fixed: the receipt's pipe exit (M74-2), the entry's compound "coverage-guided" wording (fixed before landing), and the seat manifest's null provenance (M74-5, rebuilt). Caveat: the non-author spot-check of this round's own gate decisions is pending (see `corpus/lessons/round-74.md` closing note); no agreement is recorded here.

## Round shape, seats, dead seats

- **Shape:** one v1 wave, `w1`, 12 seats (band 8-16). Roles: executor×3 (`ExecC1Amend`, `ExecC2Manifest`, `ExecTrial`), scout×1 (`ScoutSurface`), scribe×2 (`ScribeEntry`, `ScribeLesson`), connector×1 (`ConnectorSweep`), reviewer×2 (`ReviewC1`, `ReviewC2`), critic×1 (`CriticClaims`), mutation-tester×1 (`MutAuditC1`), sentinel×1 (`SentinelCounter`). Attack share 5/12 (41.7%), at least 25%. Connector seats 1 (at most 2). No residual call. L2 floor (8) met inside the wave.
- **Planner seat:** the L1 (`KasegiR74`) holds the §3 planner seat; the validator rejects `planner` as a swarm role. A bounded planning data-walk rode `ScoutSurface` (the surface and distinctness walk) and `ConnectorSweep` (sibling overlap); recorded as the mapping.
- **Dead seats:** 0. Every seat wrote its report file under `.ufo/waves/round-74/w1/` (`w1-results.json` carries no status field; presence of the report is the record). The first draft of the lesson counted 13 seats; the results file carries 12 (M74-4).
- **Routing:** per the run-15 map in `task.agentModelOverrides`. Answering model recorded where the seat reported it: `ExecTrial` provenance records `zai/glm-5.3-flash` for its resolved agent steps. No claim depends on another seat's answering model.
- **Wave evidence:** `.ufo/waves/round-74/w1-spec.json`, `w1-dispatch.json`, `w1-results.json`, `w1.ready`, `w1.ready.dispatched`, `swarm-registry.json`.
- **WAVE-DONE:** received (`WAVE-DONE kasegi r74 w1: all 12 seats settled`) before this report was filed.

## Landed-state checks (L1, after integration)

- `corpus/instruments/recheck-cwd-census.py --selftest` → `selftest cases=5 failures=0`, exit 0 (lane tree).
- Census on the lane tree → conformant, exit 0; `entries=89` = `ls corpus/knowledge/*.md` = 89.
- `frontier-recheck-count.py` → `FRONTIER-CENSUS rows=52 admitted=52 closed=52 problem-rows=0 registry=109`, `entries=55 pass=55 exit=0`.
- `capture-binding-check.py` → `records=88 bound=88 unbound=0`, exit 0.
- `source-recheck.py --manifest corpus/source-snapshots/round-74/manifest.json --source S109` from `/tmp` → `S109:sha256 OK`, 16 of 16 `anchor=<n>-ok`, exit 0.
- `claim-package-check.py` on the trial package → `WELL-FORMED`, exit 0.

## Mistakes

Mined into `corpus/lessons/round-74.md` `## Mistakes` (class · evidence · captured-by · fix · able-to-fail): M74-1 (r73 Gate with no reject line; captured-by none; R119 added), M74-2 (instrument exit recorded as the exit of a pipe; receipts corrected by appended block), M74-3 (criterion id R33 held twice; R120 recorded, not repaired), M74-4 (seat count from prose, 13 vs 12), M74-5 (seat manifest with null `fetched_utc` and a non-existent `path`; rebuilt by the integrator), M74-6 (C1 scope sentence falsified at file level for `restoration-recheck:`-only files; routed), M74-7 (C2 sibling-distinctness sentence overbroad: revenger holds DecFuzzer and mishegos README documentation; routed), M74-8 (a shell tool hid one nonzero-exit output; repeated as single commands).

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows two modified fleet files that are not this lane's (`.scratch/run15-state.json`, `.ufo/l0-questions.md`); no untracked file was written by a seat into the fleet root; nothing was copied or deleted. An empty `.ufo/reports/round-74` directory was created in the lane tree by mistake and removed (git does not track it). Misroots: none.

## Open (for the operator)

- **RC-8 (pending since r73):** may knowledge recheck values run through `bash -c` in a counter? Unchanged this round; the amendment neither expands nor reroutes it.
- **C2 api_key clause (r72, pending):** `corpus/lessons/round-72.md` narrowed-target amendment still awaits accept or reject.
- **Assimilation id drift (r70, r71):** staged `merge/kasegi/SOURCES.append.md`: 78 of 94 ids collide; decision needed on re-staging or a lane-side renumber by document.
- **Trial source conflict (observation, no decision asked):** the curl CVE-2023-38545 advisory records a 4660 USD bounty; the curl policy states none. Recorded in the package; not resolved.

No new L0 question was appended this round: each open decision above already has its L0 row (r70, r71, r72, r73).

## Tools

None installed or upgraded. Stock `curl`, `python3` (3.14), `patch`, `git`, `jj`, `bash` sufficed. No pacman transaction (host-wide pause observed).

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Pre-report gate

- `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin ls-remote origin refs/heads/master` → `dca80cf52c5d640ec8be3465fc4aa8e7c5648cc1	refs/heads/master` (equal to the final lane hash; cited above).
- `grep -c '^## SHONEN'` on this report → 1 (checked before commit).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `SKILL.md` unchanged this round; `corpus/knowledge/fuzzilli-js-engine-fuzzing-framework.md` (decision-shaped claims with located quotes; `source-recheck.py` exit 0).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: `LOG.md` § Round 74 (non-claim trial); `.ufo/waves/round-74/w1/trial/package/` (`claim-package-check.py` WELL-FORMED, exit 0) and `trial/pricing-note.md`. Documentation-only: no authorized bounty task, no live-target contact, no submission; not verified by a non-author, so not `[x]`.
- [~] Instructions executable by an agent without oral context. Evidence: `corpus/instruments/recheck-cwd-census.py --selftest` → `selftest cases=5 failures=0`, exit 0 (`corpus/lessons/round-74.md` § Counters).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `PROVINCE.md` r74 F52 line (scope limit: the project's own README only; the comparison post F41 and Big Sleep F40/F42 stay out); `ConnectorSweep.md` §2 (no sibling overlap on the Fuzzilli-specific ground; M74-7 overbreadth routed).
