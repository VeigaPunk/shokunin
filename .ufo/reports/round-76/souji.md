# souji — round 76 report (attempt 1, L1 `SoujiR76`)

Lane `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Final lane hash: `1524bc8160784d030fb7c7122ae266ca77463981`. `git ls-remote origin refs/heads/master` prints that hash.

## Work performed

Declared claims (frozen in `census/round-76/preregistration.txt` at freeze `2ed6b179ef4aeb106488806b9f3dcacca29e2e60`, Q99 grammar; every control receipt committed one commit earlier at `6c9c2a8eaad2ee570e4f43517d1f437567bb9873`, `rev=` the lane base, before any candidate byte):

- **C1 — operability** (surface: the lane's own pre-report gate, `tools/souji-pre-report-gate.sh` check 4; **sourced claim** on S320 git-check-ignore(1), opened this round). Before, an untracked directory whose own untracked `.gitignore` ignores itself and a payload read `clean` (the r75 stated limit f7, Q136). Now the gate attributes every ignored untracked path to its deciding pattern (`check-ignore -v -n -z`, `core.excludesFile` attributed away) and refuses it unless that pattern comes from a tracked `.gitignore` in an ancestor directory. Target: frozen 30-route counter, mismatches 4 → 0; blanket and naive controls red; r27 4/4 and r36 21/21; domain trial `check-clean=PASS`.
- **C2 — calibration** (lowest owned axis, 7; surface: the lane's mutant-kill self-assessment instrument). Successor tally `census/round-76/c2-kill-tally.py` binds every receipt to the mutant it is filed under (derived counter sha256 from the frozen edit sets) and reads every `EXIT=` line. Target: frozen 10-case counter, mismatches 5 → 0; blanket reject-all red; honest r75 set still `killed=6`.

Work items:

- **Fresh state.** `.ufo/watchdog.log` has `launch souji round=76 … attempt=1` and no `lane-dead-no-report souji round=76`; `jj-lane.sh state` at start: `local=remote=ee59aa4d… ahead=0 tracked=0 untracked=0`. No inherited leftovers.
- **r75 spot-check** (`corpus/lessons/round-75-verifier-spotcheck.md`, routed defects 1-5), mapped in `corpus/lessons/round-76.md` `## Inherited`:
  - 1 (probe that cannot fail) → `census/round-76/probes/repro-coreworktree.sh` computes `VERDICT=FORGERY` exit 1 / `REFUSED` exit 0: `records/probe-coreworktree-at-r75W.txt` FORGERY EXIT=1 on the r75 W gate (blob `620ed97e…`), `-at-r76W.txt` REFUSED EXIT=0 (`eef6f30c`).
  - 2 (core.excludesFile arm) → open, routed r77.
  - 3 (domain-trial revision) → the prereg binds the C1 candidate's gate blob; the trial receipt carries the amendment line to the repaired blob.
  - 4 (routed items) → (b) taken as C2; (c) r27/r36 are a frozen C1 conjunct; (a), (d) routed.
  - 5 (self-ignoring `.gitignore` limit) → C1; QUALITY Q137 supersedes Q136's limit clause.
- **Staged chronology:** P `6c9c2a8e` → F `2ed6b179` → I `2c7c1ce6` (tally) → W `e827d2bf` (gate + `.gitignore`) → A `113b0072` (after-arms) → lesson fixes `eef6f30c` → wave repair R `9cbfd296` → repair receipts `1a6eaea8` → integration `5827817c` → wave mirror `03acf2cb` → census-after `27e5e289` → domain trial (final hash). `tools/souji-freeze-check.py --substance --chronology` at F: `SUMMARY claims=2 findings=0` (S76Reviewer re-ran it at F and A: same).
- **Wave w1, 12 seats, 0 dead.** Every frozen number was reproduced from committed bytes by S76ExecC1, S76ExecC2, S76Reviewer, S76Connector, S76CriticClaims, S76CriticDiscern and S76Scribe (`census/round-76/records/wave-w1/seats/`). Causal separation SEPARABLE (S76Connector, strace of both counters).
- **Wave repairs after measurement** (`9cbfd296`, receipts `census/round-76/records/wave-repair/`, `1a6eaea8`):
  - A repository-local fsmonitor hook ran inside the W block's `ls-files --cached` (the one call without `-c core.fsmonitor=false`), appended a rule to the tracked `.gitignore` after the byte-truth check, and the W gate printed `check-clean=PASS` (S76Sentinel HIGH-1). The tracked set is now read from HEAD's tree (`ls-tree -r -z --name-only --full-tree HEAD`; also closes LOW-1, staged-only `.gitignore`). Caller `GIT_EXEC_PATH` is unset (MEDIUM-1). The lane's `.gitignore` rules are anchored (`/.jj/`, `/.ruff_cache/`; S76CriticClaims: unanchored declared any nested `sub/.jj/`). The tally requires `--selftest` and the instrument path as whole argv tokens (S76Reviewer LOW).
  - `records/wave-repair/repair-probes.txt`: `SUMMARY arms=8 as_expected=8` (fsmonitor W PASS → R FAIL; GIT_EXEC_PATH W EXEC → R NO-EXEC; one-path arm R FAIL vs M09 mutant PASS; nested `.jj` W-gitignore PASS → R-gitignore FAIL). `records/wave-repair/tally-probes.txt`: 8/8.
  - Frozen counters at the repair: `c1-at-repair.txt` rows=30 mismatches=0 EXIT=0; `c2-at-repair.txt` cases=10 mismatches=0 EXIT=0; `regress-r36-at-repair.txt` 21/21; `regress-r27-at-repair.txt` 4/4.
- **Domain trial (C1 conjunct).** The repaired gate over the lane itself with this report: `census/round-76/records/c1-domain-trial.txt` (`1524bc81`), `check-clean=PASS`, `EXIT=0`. A first run wrote its receipt inside the lane and read that file as uncommitted (`check-clean=FAIL`, `?? census/round-76/records/c1-domain-trial.txt`); the receipt was re-recorded in scratch and copied in, as the receipt's note line says. The report the trial read was this file before its final-hash fill-in (one `## SHONEN` heading then and now).
- **Frontier step.** S320 opened by the L1, re-fetched by S76Scribe and S76ScoutSources (sha256 equal); four mistakes mined (`## Mistakes` M1–M4); sourced claim C1.
- **Pointer check.** `python3 -B tools/souji-pointer-check.py --root . --rev <final> corpus/lessons/round-76.md` → see `## Other`.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain`: `.scratch/*` (orchestrator-owned), `?? trail-ids.txt` (present since r74, not this lane's, not touched), this report. No seat wrote into the fleet root.

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `6c9c2a8eaad2ee570e4f43517d1f437567bb9873` | P: C1 counter + population, C2 binding counter + population + forged cases, rec.sh, controls K-a/K-b/K-c (C1) and do-nothing/blanket (C2), variants, S320 capture, census-before | LOG "## Round 76", bullet "Controls … freeze" |
| `2ed6b179ef4aeb106488806b9f3dcacca29e2e60` | F: preregistration | same bullet |
| `2c7c1ce6f91062f497ffbbc7fcc9e9c19e2511ce` | I: r76 tally | bullet "Candidates" |
| `e827d2bf53f71470bfc1fce6aa4633549b018270` | W: gate attribution block; `.gitignore` declares `.jj/` `.ruff_cache/` | bullet "Candidates" |
| `113b007202d79275ca2debaaaa719551eaa35198` | A: c1-after, c2-after, r27/r36 regression receipts | bullet "Candidates" |
| `eef6f30c7be607d7590898da53496408f5fa9545` | computed-verdict core.worktree probe + receipts; rec.sh missing-BIND refusal + control | bullet "Lesson fixes" |
| `9cbfd29630f04799cb72b17a53df860c1f503275` | wave repair R: gate tracked set from HEAD, `GIT_EXEC_PATH` unset; anchored `.gitignore`; tally token check | bullet "Wave w1" |
| `1a6eaea8acc14c23e13269429ab2699dde8e112f` | wave-repair receipts and probes | bullet "Wave w1" |
| `5827817c1db3b795eb15ff8d486793ca2c891de0` | S320, Q137, knowledge r76, README frontier, SKILL rows, SCORECARD, LOG, lesson | bullet "Frontier" |
| `03acf2cb85af50f0a6154df39436693af6842de3` | wave evidence mirror, lesson Gate (S76ScoutSources), knowledge parent-rule citation | bullet "Wave w1" |
| `27e5e289a22a3edaf42b094377bb7e80cf916ef1` | census-after, lesson pointers | bullet "Frontier" |
| `1524bc8160784d030fb7c7122ae266ca77463981` | domain-trial receipt (C1 conjunct) | bullet "Domain trial" |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | `census/round-76/controls/c1-K-a-do-nothing.txt`: `SUMMARY rows=30 mismatches=4 errors=0` (f7 f9 f10 f14 `clean=PASS`), EXIT=1; blanket `c1-K-b-blanket-ignored.txt` mismatches=4, naive `c1-K-c-naive-untracked-gitignore.txt` mismatches=1, both EXIT=1 | `census/round-76/records/c1-after.txt`: `SUMMARY rows=30 mismatches=0 errors=0`, EXIT=0; `c1-regress-r36.txt` 21/21, `c1-regress-r27.txt` 4/4; at the repair `records/wave-repair/c1-at-repair.txt` identical; domain trial `records/c1-domain-trial.txt`: `check-tip=PASS check-report=PASS check-shonen=PASS check-clean=PASS check-prereg=PASS`, `EXIT=0`, wall 13.3 s, lane master = ls-remote = `27e5e289` (the tip only adds this receipt), 26497 ignored untracked paths, every one attributed to a tracked `.gitignore`; amendment line: W gate blob `18587bd2…` → repaired blob `90bdd8c7…` | `grep -E '^(SUMMARY\|EXIT=)' census/round-76/records/c1-after.txt` | `113b007202d79275ca2debaaaa719551eaa35198` (gate blob of `e827d2bf`; repair `9cbfd296`) |
| C2 | `census/round-76/controls/c2-K-do-nothing-r75.txt`: `SUMMARY cases=10 mismatches=5 errors=0` (b-swap-x09-gets-m08, b-swap-p1-gets-x09, b-pristine-r74, b-unknown-id, b-exit-disagree accepted), EXIT=1; blanket `c2-K-b-blanket-reject-all.txt` mismatches=2, EXIT=1 | `census/round-76/records/c2-after.txt`: `SUMMARY cases=10 mismatches=0 errors=0`, EXIT=0, h-honest `killed=6`; at the repair `records/wave-repair/c2-at-repair.txt` identical | `grep -E '^(SUMMARY\|EXIT=)' census/round-76/records/c2-after.txt` | `113b007202d79275ca2debaaaa719551eaa35198` (tally of `2c7c1ce6`; repair `9cbfd296`) |

Both frozen predicates are met, and each beat its committed do-nothing control. No owned axis score changed (calibration 7, coverage 8, operability 8).

Qualifications from the wave (the operator rules):

- **C1 candidate forged outside the frozen rows, repaired after measurement:** the fsmonitor hook route (S76Sentinel HIGH-1). The frozen counter cannot see the repair; `repair-probes.txt` shows W forged and R refused.
- **C1 kill power:** every forging row carries exactly two undeclared paths, so a gate refusing only above one passes the frozen counter, r27 and r36 (S76MutGate M09; lesson M2). The repair probe's one-path arm kills it; no frozen row does. Ten other block mutants survive (M02-M08, M11, M13, M15); the seat judges them equivalent or unreachable on constructible inputs.
- **C1 domain trial rests on the `.gitignore` declaration** (S76Connector, S76CriticClaims): without `/.jj/` the same gate refuses the lane, whose `.jj` paths (13,621 at S76Connector's reading) are otherwise decided by the untracked `.jj/.gitignore`. That declaration is the rule working (a tracked rule decides), and it is a lane change committed in W.
- **C2 counter discrimination:** the frozen population is separable by file name (S76CriticClaims: a tally matching six basenames scores 0); the binding counter compares exit codes only (S76MutTally K03/K04 HIGH: a counter that accepts every rejection reads the r75 control as 0). The r76 tally itself binds bytes (`tally-probes.txt` arm by-name: M08's bytes under X09's file name refused).
- **C2 stated limit:** binding names the instrument, it does not prove the run (S76CriticDiscern F5); rec.sh's `command=` line loses quoting, so a `--selftest` token inside a quoted path cannot be told apart (lesson M3).
- **Disagreed:** S76ExecEvade b-neg "FORGERY HIGH" is the declared broad-committed-rule limit (the tracked root rule `hidden/` decides), not a forgery of the r76 rule.
- **Sourced-claim scope** (S76ScoutSources HIGH h1): the one anchored sentence grounds attribution; the source-form sentence (over 25 words) and gitignore(5)'s parent rule (S318) carry the rest.

## Sources & frontier

- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`:
  - before: `census/round-76/records/census-before.txt`, `souji ok`, 86 W04, EXIT=0
  - after: `census/round-76/records/census-after.txt`, `souji ok`, 86 W04, EXIT=0
- **Rows** (`grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`): 242 → 243.
  - Added: tier A ×1 — S320 git-check-ignore(1) at git v2.56.0, `mined`, cited by `corpus/knowledge/filter-filemode-witness.md` r76.
  - Rejected: two over-bar anchors on the same page (the `-n` sentence, 27 words; the source-form sentence, 29-30 words), paraphrased only.
  - Rows touched old→new: none.
- **Frontier advanced.** README "Frontier (r76 ignore-source attribution and receipt-bound kill tallies)". It stays frontier, not Core.
- **Mistake mined:** four (`corpus/lessons/round-76.md` `## Mistakes` M1–M4), each with a fix shown able to fail.
- **Assimilation: none.** `considerthese/` is absent in this lane, and no shokuknow theme fits the frozen claims.

## Trend verdicts

- **expansion: improved.** One new tier-A row (S320) on ground the lane did not hold (which file decided an ignore match); the gate gained an attribution rule, the lane gained a receipt-bound kill tally; QUALITY Q137, knowledge r76, two SKILL gate rows, two capability rows.
- **quality: improved.** Seats forged the W gate through a repository fsmonitor hook and a caller `GIT_EXEC_PATH`, and found the unanchored tool-dir rules; each repaired in-round with W-vs-R receipts that can fail (`repair-probes.txt` 8/8). The r75 probe that could not fail now computes its verdict. The frozen counters stay 0 at the repair; r27/r36 green.
- **discernment: improved.** The lane disagreed with one seat HIGH (b-neg) on stated grounds, caught its own mis-reading of another seat's forgery through a probe that failed (M3), recorded the instruments' kill-power gaps (M09, K03/K04, filename separability) instead of re-scoring, and accepted the scout's narrowing of the sourced claim.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md gate rows "r76 pre-report gate ignore-source attribution counter (C1)" and "r76 receipt-bound mutant-kill tally and its binding counter (C2)" (`5827817c`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md "## Round 76"; the repaired gate ran over the lane itself at the final tip (`census/round-76/records/c1-domain-trial.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: seven seats re-ran the prereg commands as written and reproduced every predicate (`census/round-76/records/wave-w1/seats/S76ExecC1.md`, `S76ExecC2.md`, `S76Reviewer.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: sibling gates and tallies documented, not edited (`census/round-76/records/wave-w1/seats/S76Connector.md`, `S76Sentinel.md` LOW-2); no fleet misroot.

## Other

- **Round shape: one v1 wave `w1` of 12 seats**, validated under `ufo-wave-policy.json` (band 8–16) and dispatched via the inline handoff (`census/round-76/records/wave-w1/w1.ready.dispatched`). WAVE-DONE was received. No residual call; round total 12.
  - Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1.
  - Attack seats: 5 of 12 (42 %).
  - The L1 holds the §3 planner seat.
- **Dead seats: 0.** All 12 seats wrote their report files. `w1-results.json` carries no inline output for any seat (note: "orchestrator kernel restarted mid-wave; seat output was delivered to the orchestrator session but not retained"); the seat files are the evidence.
- **Pointer check at the final tip:** `python3 -B tools/souji-pointer-check.py --root . --rev 1524bc8160784d030fb7c7122ae266ca77463981 corpus/lessons/round-76.md` → `SUMMARY files=1 checked=27 missing=0 skipped=0 dead_declared=0`, EXIT=0.
- **Routed to r77:** lesson "Routed to round 77" (a)–(c); SCORECARD "r77 (planned)".
- **Open L0 questions:** none new.
- **Stale-lane:** respawn-per-round driver; this lane has no other open mission.
- **Tool installs:** none. No pacman transaction, and no sysctl, sudo or kernel change.
- **Scratch:** `/fast/scratch/hyaku/souji-r76/` removed at landing.

## Stale-lane

Stale-lane: respawn-per-round driver; this lane has no other open mission.
