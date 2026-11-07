# souji — round 74 report (attempt 1, L1 `SoujiR74`)

Lane `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Final lane hash: `0e1765a046cdb879df5e6ff242864311226491c0`. `git ls-remote origin refs/heads/master` prints that hash.

## Work performed

Declared claims (frozen in `census/round-74/preregistration.txt` at freeze `bcdf2d16f8158c9faf8b60e6bb1b98c1f4f25dce`, before any candidate byte; every control and before receipt committed in the same freeze):

- **C1 — operability** (surface: the lane's own pre-report gate, `tools/souji-pre-report-gate.sh` check 4; **sourced claim** on S317 gitformat-index(5), opened this round, with S315/S316). Before, check 4 passed `clean` whenever `git status` was empty, so an index stat-cache forgery passed. Now every status-clean tracked path is re-hashed against its index object name through the receipt writer's `_truth_refusal`. Target: frozen 9-row gate counter, mismatches 3 → 0.
- **C2 — calibration** (lowest owned axis, 7; surface: the counter's forgery witness and its own selftest). A successor counter, `census/round-74/c1-counter.py`, reads only the row's declared forged paths. Targets: defanged FWw/FC1/FC2 detected 0 → 3 of 3, with D1..D5 kept and the pristine control at 15/0. The r73 survivors M08/M14/M15/M17 are killed 0 → 4 of 4.

Work items:

- **Fresh state, no inherited leftovers.** `.ufo/watchdog.log` has no `lane-dead-no-report souji round=74`; the lane was clean at base `43cd74bb`.
- **r73 spot-check** (`corpus/lessons/round-73-verifier-spotcheck.md`, routed defects 1-6):
  - 1 → C2 + Q134.
  - 2 → C2 (iv).
  - 3 → C1 + Q135. The other tools are routed.
  - 4 → folded into the r74 counter.
  - 5 → this lesson's pointer check exits 0 (below). The r73 lesson is not edited.
  - 6 → seats now write their report file first; 12 of 12 delivered.
  - The mapping is in `corpus/lessons/round-74.md` `## Inherited`.
- **Staged chronology:**
  - F `bcdf2d16` (freeze, controls, probes, edit sets, S317 capture)
  - I `ac573032` (counter, selftest 62/62)
  - W `ec13ba7f` (gate)
  - A `8fe48c86` (after-arms)
  - wave integration `a50e0ce2`
  - census-after `b5e6d514`
  - domain trial `0e1765a0`
- **Wave w1, 12 seats, 0 dead.** Every frozen number was reproduced from committed bytes by S74ExecC1, S74ExecC2, S74Reviewer, S74CriticClaims, S74CriticDiscern, S74Connector and S74Scribe (`census/round-74/records/wave-w1/seats/`).
- **Wave repair of the gate after measurement** (lesson M4, `a50e0ce2`). The frozen rows held, but seats forged or stalled the stage-W gate outside them. The fixes:
  - scrub caller env config;
  - add the writer's pinned status and its filter/conversion witness;
  - run an isolated interpreter that compiles the writer source from the gate's real path;
  - echo no paths;
  - accept only a regular-file report.

  Each fix is shown able to fail (`census/round-74/records/wave-repair/`). Stage-W → repaired:
  - evasion FORGERY 6 → 2 (`evade-W.txt` vs `evade-R.txt`). The 2 that remain are ignored untracked files, a stated limit.
  - code-exec 3 → 0 (`sentinel-exec-*`)
  - report hangs 2 → 0 (`sentinel-resource-*`)
  - forged echo line present → absent (`sentinel-echo-*`)

  Fail-closed is now observable: without its writer the repaired gate fails GH1-4 and keeps GF1-3 red, while a fail-open mutant passes GF1-3 (`failclosed-no-writer*.txt`). The frozen counter at the repair still gives mismatches=0 EXIT=0 (`c1-at-repair.txt`). The r27 fixture passes 4/4 and r36 passes 21/21 (`regress-*-at-repair.txt`).
- **Domain trial (C1 iii).** The repaired gate ran over the lane itself at the final tip, with this report: `census/round-74/records/c1-domain-trial.txt` gives `check-clean=PASS` (all six check lines PASS/SKIPPED, `EXIT=0`, lane master = ls-remote = `b5e6d514`, 19304 tracked files, ~3 s).
- **Frontier step.**
  - S317 opened, re-fetched by S74ScoutSources and re-anchored before landing.
  - Four mistakes mined (`## Mistakes` M1–M4).
  - Sourced claim C1.
- **Pointer check.** `python3 -B tools/souji-pointer-check.py --root . --rev <final> corpus/lessons/round-74.md` → `SUMMARY files=1 checked=59 missing=0 skipped=0 dead_declared=0`, `EXIT=0` (rev `0e1765a0`).
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows:
  - `.scratch/*`: orchestrator-owned.
  - `?? trail-ids.txt`: written 20:36, before this wave dispatched (20:53); one byte `,`; not this lane's, not touched.
  - this report.

  No seat wrote into the fleet root.

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `bcdf2d16f8158c9faf8b60e6bb1b98c1f4f25dce` | freeze: prereg, C1 gate counter + K-a/b/c, C2 defang D6-D8 + survivor set, probe, before receipts, S317 capture, census-before | LOG "## Round 74", bullet "Frozen at" |
| `ac57303295371f34befc36d34f78c6715f7341a0` | C2 counter (mk-counter.py) + selftest 62/62 | bullet "Candidates" |
| `ec13ba7fac9085005dca2e69ee12a2933d2c22a5` | C1 gate byte-truth check | bullet "Candidates" |
| `8fe48c863d353da8e26140b132afba00de71ba61` | after-arms (c1-after, c2-after-D1..D8, pristine, M-selftests) | bullet "Candidates" |
| `a50e0ce241f9cd2dea71d30235cb77bd2c41c74b` | gate wave repairs + wave-repair receipts, S317, Q134, Q135, knowledge r74, README frontier, SKILL rows, SCORECARD, LOG, lesson, regress receipts, wave evidence mirror | bullets "Wave w1", "Frontier" |
| `b5e6d514bf6c0eafad842d7fc2094986df1c86ae` | census-after receipt, lesson wording | bullet "Frontier" |
| `0e1765a046cdb879df5e6ff242864311226491c0` | domain-trial receipt (C1 iii) | bullet "Domain trial" |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | `census/round-74/controls/c1-K-a-do-nothing.txt`: `SUMMARY rows=9 mismatches=3 errors=0` (GF1 GF2 GF3 `clean=PASS`), EXIT=1; K-b blanket 4, K-c regular-only 1, EXIT=1 | `census/round-74/records/c1-after.txt`: `SUMMARY rows=9 mismatches=0 errors=0`, `EXIT=0`; at repair `records/wave-repair/c1-at-repair.txt` identical; domain trial `check-clean=PASS` | `grep -E '^(SUMMARY\|EXIT=)' census/round-74/records/c1-after.txt` | `8fe48c863d353da8e26140b132afba00de71ba61` (repair `a50e0ce2`, domain trial `0e1765a0`) |
| C2 | `controls/c2-before-r73-D6.txt`/`-D7`/`-D8`: `base_unwitnessed=0`, EXIT=0 (0 of 3); `controls/c2-before-r73-M08..M17-selftest.txt` 52/52 EXIT=0 (0 of 4) | `records/c2-after-D6..D8.txt`: `base_unwitnessed=1`, edited row `base_witness=no` (3 of 3); D1..D5 5/5; `records/c2-after-pristine.txt` `base_unwitnessed=0 base_forgeries=15` EXIT=0; M08/M14/M15/M17 selftest fail=1/1/2/1 EXIT=1 (4 of 4); `records/counter-selftest.txt` 62/62 | `for k in 6 7 8; do grep -cE '^SUMMARY .*base_unwitnessed=1( \|$)' census/round-74/records/c2-after-D$k.txt; done`; `for m in M08 M14 M15 M17; do grep -E '^SELFTEST' census/round-74/records/c2-after-$m-selftest.txt; done` | `8fe48c863d353da8e26140b132afba00de71ba61` |

Both frozen predicates are met, and each beat its committed do-nothing control. No owned axis score changed (calibration 7, coverage 8, operability 8).

Qualifications from the wave:

- **C1's rows did not cover the gate wrapper.** Before the repair, six routes forged the stage-W gate: env and repo filters, the fileMode split status, interpreter injection, and a report FIFO hang. These were repaired after measurement (M4). Two routes remain as stated limits: ignored untracked files, and the caller's `PATH`/`BASH_ENV` (S74Sentinel E1/E2). S74Sentinel's fsmonitor split route did not reproduce in the L1's environment (stage-W FAIL too).
- **C2's witness is path-keyed and declared.**
  - S74ExecC2 X4 shows an SY2 defang credited (`base_forgeries` 15→16), caught only by `base_mismatches`.
  - S74CriticClaims shows a spec-declared unwitnessing counter passes all five conjuncts, so the claim rests on the code and the pre-freeze probe as well as the predicate.
  - S74MutCounter X09 and X15 survive.
  - All of this is routed to r75 (M3).
- **Q99 freeze-check grammar is NOT MET** (S74CriticDiscern; also r72/r73). It is routed.

## Sources & frontier

- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`:
  - before: `census/round-74/records/census-before.txt`, `souji ok`, 86 W04, EXIT=0
  - after: `census/round-74/records/census-after.txt`, `souji ok`, 86 W04, EXIT=0
- **Rows** (`grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`): 239 → 240.
  - Added: tier A ×1, S317 gitformat-index(5) at v2.56.0. It is `mined` and cited by `corpus/knowledge/filter-filemode-witness.md` r74.
  - Rejected: the first S317 anchor (type field only; S74ScoutSources F1).
  - Rows touched old→new: none.
- **Frontier advanced.** README "Frontier (r74 pre-report gate byte truth and row-specific witness)". It stays frontier, not Core.
- **Assimilation: none.** `considerthese/` is absent in this lane, and no shokuknow theme fits the frozen claims.

## Trend verdicts

- **expansion: improved.** A new tier-A row on new ground (index entry layout). The lane's own gate gained a byte-truth check, two QUALITY rows, a knowledge r74 section, two SKILL gate rows and two capability rows.
- **quality: improved.** Seats forged the gate on six routes outside the frozen rows. All were repaired in-round, and each fix is shown able to fail on committed probes (stage-W vs repaired receipts). The frozen counter and the r27/r36 fixtures are unchanged green.
- **discernment: improved.** Q133's overstatement was corrected by Q134. My own Q134/Q135 drafts were tightened on a critic's evidence before landing ("never a false kill" dropped; limits stated). The S317 anchor was replaced on a seat's falsification. Remaining over-claims are disclosed and routed (M3).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md gate rows "r74 pre-report gate byte-truth counter (C1)" and "r74 row-specific witness counter, defang D6-D8 and survivor set (C2)" (`a50e0ce2`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md "## Round 74". The repaired gate ran over the lane itself at the final tip (`census/round-74/records/c1-domain-trial.txt`, 19k tracked files).
- [~] Instructions executable by an agent without oral context. Evidence: seven seats re-ran the prereg commands as written and reproduced every predicate (`census/round-74/records/wave-w1/seats/S74ExecC1.md`, `S74ExecC2.md`, `S74Reviewer.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: the sibling gate findings (kama, mado) were documented, not edited (`census/round-74/records/wave-w1/seats/S74Connector.md`), and there was no fleet misroot.

## Other

- **Round shape: one v1 wave `w1` of 12 seats**, validated under `ufo-wave-policy.json` (band 8–16) and dispatched via the inline handoff. WAVE-DONE was received. No residual call; round total 12.
  - Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1.
  - Attack seats: 5 of 12 (42 %).
  - The L1 holds the §3 planner seat.
- **Dead seats: 0.** `w1-results.json` holds output for all 12.
- **Routed to r75:** lesson "Routed to round 75" items (a)–(e).
- **Open L0 questions:** none new.
- **Stale-lane:** respawn-per-round driver; this lane has no other open mission.
- **Tool installs:** none. No pacman transaction, and no sysctl, sudo or kernel change.
- **Scratch:** `/fast/scratch/hyaku/souji-r74/` was removed at landing.
