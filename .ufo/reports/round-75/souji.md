# souji — round 75 report (attempt 1, L1 `SoujiR75`)

Lane `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Final lane hash: `a4554ca19f991f24a58077fc43c787c19750d413`. `git ls-remote origin refs/heads/master` prints that hash.

## Work performed

Declared claims (frozen in `census/round-75/preregistration.txt` at freeze `be599cbb02854b9d669a1a2699f15657fd70b336`, in Q99 grammar; every control receipt committed one commit earlier at `7ba5217d6fc754201615e04e8dfc88cf07c33fd3`, before any candidate byte):

- **C1 — operability** (surface: the lane's own pre-report gate, `tools/souji-pre-report-gate.sh` check 4; **sourced claim** on S318 gitignore(5) and S319 git-ls-files(1), both opened this round). Before, an untracked file hidden by `$GIT_COMMON_DIR/info/exclude` read `clean`. Now the gate lists ignored untracked paths under `--exclude-standard` and under `--exclude-per-directory=.gitignore` alone and fails on a non-empty difference. Target: frozen 25-route counter, mismatches 2 → 0, blanket control red, domain trial `check-clean=PASS`.
- **C2 — calibration** (lowest owned axis, 7; surface: the witness counter's own selftest). Successor counter `census/round-75/c1-counter.py` (selftest only; no verdict code changed). Target: mutant kills 4 → 6 of 6 (X09 and X15∘M17 added; M08/M14/M15/M17 kept), pristine selftest green.

Work items:

- **Fresh state.** `.ufo/watchdog.log` has no `lane-dead-no-report souji round=75`; `jj-lane.sh state` at start: `local=remote=52d3f07d… ahead=0 tracked=0 untracked=0`. No inherited leftovers.
- **r74 spot-check** (`corpus/lessons/round-74-verifier-spotcheck.md`, routed defects 1-4), mapped in `corpus/lessons/round-75.md` `## Inherited`:
  - 1 (domain-trial gate revision) → the prereg names the gate revision the trial binds and requires an amendment line for a later blob (below).
  - 2 (undisclosed OVER-REFUSAL on `n-filemode-config`) → ruled FAIL in the prereg; the r75 counter freezes an expected verdict per route (lesson M3).
  - 3 (routed items) → (b) X09/X15 taken as C2; (e) the Q99 freeze grammar is met (`census/round-75/records/freeze-check.txt`: `SUMMARY claims=2 findings=0`, EXIT=0 with `--substance --chronology`; NOT MET r72-r74); the rest stay routed.
  - 4 (ignored-untracked forgeries a stated limit) → C1 + QUALITY Q136, which supersedes Q135's ignored-files limit clause.
- **Staged chronology:** P `7ba5217d` (instruments, populations, controls, variants, S318/S319 captures, census-before) → F `be599cbb` (prereg) → I `f6ec0d71` (C2 counter) → W `1ad737b4` (C1 gate) → A `5d10e09e` (after-arms) → integration `3564e925` → census-after `c8dabbd7` → domain trial `a4554ca1`.
- **Wave w1, 12 seats, 0 dead.** Every frozen number was reproduced from committed bytes by S75ExecC1, S75ExecC2, S75Reviewer, S75CriticClaims and S75CriticDiscern (`census/round-75/records/wave-w1/seats/`).
- **Wave repairs after measurement** (lesson M5, `3564e925`, receipts in `census/round-75/records/wave-repair/`):
  - A repository-local `core.worktree` redirects status and both listings to another tree; the lane-base and W gates both printed `check-clean=PASS` with an info/exclude-hidden payload (S75ExecEvade HIGH-1, S75Sentinel F1, S75CriticClaims 3). The repaired gate requires `git rev-parse --show-toplevel` to be the lane: `coreworktree-W.txt` PASS → `coreworktree-R.txt` `RECEIPT-WORKTREE-REDIRECTED`.
  - The W gate red the r36 report-gate fixture (S75MutGate HIGH F1: 17/21; L1 re-run `regress-r36-original-at-W.txt` 18/21, EXIT=1), because the fixture hid its harness `tools` symlink with info/exclude. The fixture now declares it in a committed `.gitignore`: 21/21 on the lane-base gate and on the repaired gate (`regress-r36-amended-at-base.txt`, `regress-r36-amended-at-repair.txt`). r27 fixture 4/4 at the repair.
  - The frozen counter at the repaired gate: `c1-at-repair.txt` mismatches=0, EXIT=0.
- **Domain trial (C1 iii).** The repaired gate over the lane itself with this report: `census/round-75/records/c1-domain-trial.txt` — `check-tip=PASS check-report=PASS check-shonen=PASS check-clean=PASS check-prereg=PASS`, `check-report-contract=SKIPPED`, `EXIT=0`; lane master = ls-remote = `c8dabbd7` (the tip `a4554ca1` only adds this receipt), 19459 tracked files, ignored untracked 26133 under both listings (difference 0). The report the trial read was this file before its final-hash fill-in (one `## SHONEN` heading then and now). Amendment line in the receipt: W gate blob sha256 `620ed97e…2b96` → repaired blob `ef3b04e4…356a`.
- **Frontier step.** S318/S319 opened, re-fetched by S75ScoutSources (sha256 equal) and re-anchored before landing; six mistakes mined (`## Mistakes` M1–M6); sourced claim C1.
- **Pointer check.** `python3 -B tools/souji-pointer-check.py --root . --rev c8dabbd7ff7e7526cb201d5e16f7237a8e8bb04a corpus/lessons/round-75.md` → `SUMMARY files=1 checked=28 missing=0 skipped=1 dead_declared=0`, EXIT=0.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain`: `.scratch/*` (orchestrator-owned), `?? trail-ids.txt` (present since r74, not this lane's, not touched), this report. No seat wrote into the fleet root.

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `7ba5217d6fc754201615e04e8dfc88cf07c33fd3` | P: C1 counter + population, C2 kill counter + mutant set, rec.sh, controls K-a/K-b, C2 before receipts + do-nothing/blanket tallies, variants, S318/S319 captures, census-before | LOG "## Round 75", bullet "Controls … freeze" |
| `be599cbb02854b9d669a1a2699f15657fd70b336` | F: preregistration (Q99 grammar) | same bullet |
| `f6ec0d7140e0976b8128af803520b895a14a64e0` | I: r75 counter, two selftest detectors | bullet "Candidates" |
| `1ad737b4a9ac71bd44b6ac849f73387fdc3ab9c5` | W: gate ignore-source rule | bullet "Candidates" |
| `5d10e09ed7749f5706eade39ac9a0ae2355aa1f3` | A: c1-after, c2-after-* receipts, variants, c2-after tally, freeze-check | bullet "Candidates" |
| `3564e925f64c0fb56bb4b38d3c7b93caba0b3b2d` | gate work-tree repair, r36 fixture rule, wave-repair receipts, S318/S319, Q136, knowledge r75, README frontier, SKILL rows, SCORECARD, LOG, lesson, wave evidence mirror | bullets "Wave w1", "Frontier" |
| `c8dabbd7ff7e7526cb201d5e16f7237a8e8bb04a` | census-after, lesson pointer repair | bullet "Frontier" |
| `a4554ca19f991f24a58077fc43c787c19750d413` | domain-trial receipt (C1 iii) | bullet "Domain trial" |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | `census/round-75/controls/c1-K-a-do-nothing.txt`: `SUMMARY rows=25 mismatches=2 errors=0` (f-info-exclude, f5-info-exclude-dir `clean=PASS`), EXIT=1; blanket `c1-K-b-blanket-ignored.txt` mismatches=3, EXIT=1 | `census/round-75/records/c1-after.txt`: `SUMMARY rows=25 mismatches=0 errors=0`, EXIT=0; at the repair `records/wave-repair/c1-at-repair.txt` identical; domain trial `check-clean=PASS` | `grep -E '^(SUMMARY\|EXIT=)' census/round-75/records/c1-after.txt` | `5d10e09ed7749f5706eade39ac9a0ae2355aa1f3` (gate blob of `1ad737b4`; repair `3564e925`) |
| C2 | `census/round-75/controls/c2-K-do-nothing-r74.txt`: `SUMMARY mutants=6 killed=4 survived=2 unread=0 pristine=PASS` (X09, P1 SURVIVED), EXIT=1; blanket `c2-K-blanket-pristine-red.txt` pristine=FAIL, EXIT=1 | `census/round-75/records/c2-after.txt`: `SUMMARY mutants=6 killed=6 survived=0 unread=0 pristine=PASS`, EXIT=0; pristine `records/c2-after-pristine-selftest.txt` 64/64 | `grep -E '^(SUMMARY\|EXIT=)' census/round-75/records/c2-after.txt` | `5d10e09ed7749f5706eade39ac9a0ae2355aa1f3` (counter of `f6ec0d71`) |

Both frozen predicates are met, and each beat its committed do-nothing control. No owned axis score changed (calibration 7, coverage 8, operability 8).

Qualifications from the wave:

- **C1's measured move is the info/exclude arm.** f3 (core.excludesFile) was already refused at the lane base by the receipt writer's pinned status (`-c core.excludesFile=/dev/null`), so an info/exclude-only gate would also meet the target (S75MutGate F2, S75CriticClaims 2, S75Reviewer O1).
- **The target's 0 rests on two frozen label rulings** (f2 PASS, n-filemode FAIL), both of which the lane-base gate already satisfied (S75CriticClaims 1); the 2 → 0 delta is exactly the two info/exclude rows.
- **Repaired after measurement:** the core.worktree route and the r36 fixture regression (M5). The fixture's bytes changed (harness rule committed), stated here.
- **Stated limits:** an untracked self-ignoring `.gitignore` at any level (the `.jj/` shape; about half the lane's ignored paths sit under one), and a broad committed rule, still hide content (S75CriticDiscern, S75ScoutSources, S75CriticClaims). The prereg's description "committed .gitignore rules only" was wrong on that count (lesson M6); the predicate is unaffected.
- **Unmeasured:** the gate's ls-files failure branch and its refusal class/order (S75MutGate F3/F4).
- **C2's detectors are selftest units**, not fixture probes: post-only and base-aliased new-slot witnesses survive (S75ExecC2 Y4/Y5); four selftest-block mutants survive while still killing X09/P1 (S75MutCounter); the tally's UNREAD boundary has no committed receipt and it does not bind a receipt to its mutant (S75MutCounter M1/M2, S75Reviewer O2). Routed to r76.

## Sources & frontier

- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`:
  - before: `census/round-75/records/census-before.txt`, `souji ok`, 86 W04, EXIT=0
  - after: `census/round-75/records/census-after.txt`, `souji ok`, 86 W04, EXIT=0
- **Rows** (`grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`): 240 → 242.
  - Added: tier A ×2 — S318 gitignore(5) and S319 git-ls-files(1), both at git v2.56.0, `mined`, cited by `corpus/knowledge/filter-filemode-witness.md` r75.
  - Rejected: the first-filed anchors of both rows (each stopped before the clause the claim rests on; S75ScoutSources MEDIUM), and one 27-word S318 anchor over the bar.
  - Rows touched old→new: none.
- **Frontier advanced.** README "Frontier (r75 ignore sources and the witness counter's second detectors)". It stays frontier, not Core.
- **Mistake mined:** six (`corpus/lessons/round-75.md` `## Mistakes` M1–M6; M3 and M4 mined from r74).
- **Assimilation: none.** `considerthese/` is absent in this lane, and no shokuknow theme fits the frozen claims.

## Trend verdicts

- **expansion: improved.** Two new tier-A rows on ground the lane did not hold (which exclude sources are policy, and how ls-files composes them); the lane's own gate gained an ignore-source rule and a work-tree check; QUALITY Q136, knowledge r75, two SKILL gate rows, two capability rows.
- **quality: improved.** Seats forged the W gate through core.worktree and red the r36 fixture; both repaired in-round, each shown able to fail on committed receipts (`coreworktree-W/-R`, `regress-r36-original-at-W` vs `-amended-at-*`). The frozen counter stays 0 at the repair; r27/r36 green.
- **discernment: improved.** The r74 probe's two mislabels were turned into frozen rulings; Q135's lumped limit was split by Q136; both first-filed source anchors were replaced on a seat's falsification; the prereg's over-strong description and the core.excludesFile attribution are disclosed, not prettified.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md gate rows "r75 pre-report gate ignore-source counter (C1)" and "r75 witness-counter kill tally, mutants X09/X15/P1 (C2)" (`3564e925`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md "## Round 75"; the repaired gate ran over the lane itself at the final tip (`census/round-75/records/c1-domain-trial.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: five seats re-ran the prereg commands as written and reproduced every predicate (`census/round-75/records/wave-w1/seats/S75ExecC1.md`, `S75ExecC2.md`, `S75Reviewer.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: sibling gates (12 sites, 9 lanes) documented, not edited (`census/round-75/records/wave-w1/seats/S75Connector.md`); no fleet misroot.

## Other

- **Round shape: one v1 wave `w1` of 12 seats**, validated under `ufo-wave-policy.json` (band 8–16) and dispatched via the inline handoff (`census/round-75/records/wave-w1/w1.ready.dispatched`). WAVE-DONE was received. No residual call; round total 12.
  - Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1.
  - Attack seats: 5 of 12 (42 %).
  - The L1 holds the §3 planner seat.
- **Dead seats: 0.** `w1-results.json` holds output for all 12.
- **Routed to r76:** lesson "Routed to round 76" (a)–(d).
- **Open L0 questions:** none new.
- **Stale-lane:** respawn-per-round driver; this lane has no other open mission.
- **Tool installs:** none. No pacman transaction, and no sysctl, sudo or kernel change.
- **Scratch:** `/fast/scratch/hyaku/souji-r75/` removed at landing.
