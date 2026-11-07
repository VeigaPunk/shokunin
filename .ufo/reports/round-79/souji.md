# souji — round 79 report (L1 SoujiR79, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Base `e65538e73c7f1a8f7570bc24a2215da8a90043f3` (r78 admitted). Preregistration `census/round-79/preregistration.txt` (frozen at F `e98cd0c55b1d8aaec8af8ff3402a5856263923ed`).

## Work performed

Declared claims (two, causally separable; S79Connector: SEPARABLE):

- **C1 — operability (sourced on S325 and S326, both opened this round):** the pre-report gate answers a caller's TERM, INT or HUP by killing its running child's process group and exiting 128 + n with `check-signal=FAIL` / `RECEIPT-GATE-SIGNALED`. Frozen 11-row counter: **at the frozen measurement A, mismatches 10 → 1, orphans 10 → 1, EXIT=1 — C1 FAILS its frozen kill rule ("any mismatch") at A.** The one red row (s4, INT) is an instrument launch artefact, diagnosed after measurement: the receipt was launched with `&` from a script, so the counter and every gate it started inherited SIGINT ignored, which bash cannot trap. The same frozen counter on the same gate bytes, launched in the foreground: 10 → 0 in 3 of 3 runs. That re-run is post-measurement and is reported for the closure to rule on, not counted as the claim.
- **C2 — calibration (the lowest owned axis, 7):** the pointer-resolution counter refuses the five false ledger rows the r78 wave's S78MutCounter found the r78 counter accepts. Frozen 9-row harness: accepted 5 → 0, mismatches 5 → 0, EXIT=0; controls and regressions as preregistered.

Work items:

- Protocol load and inherited debts: r78 spot-check routed defects 1–6 and r78 lesson `## Routed to round 79` read first (`corpus/lessons/round-79.md` `## Inherited`). Defect 1 → LOG.md `## Round 79` pointer; 2 → disclosure only (frozen r78 prereg; the knowledge entry already disclaims); 3 → C2; 4 → the domain trial grades the filed report bytes (below); 5 → C1 (SIGTERM) taken, the backstop row carried; 6 → unchanged.
- Pre-freeze feasibility in scratch (Q70): base gate 10 orphan rows; draft candidate 11/11; draft regressions green (`census/round-79/records/prefreeze-feasibility.txt`).
- P `d7f40f764e6b25e32662384761d82d3032714eb1`: C1 counter `census/round-79/c1-signal-counter.py` + population; C2 harness `census/round-79/c2-false-row-harness.py` + pinned population `c2-false-rows.tsv`; control variants and every control receipt at the base; S325/S326 captures; census-before.
- F `e98cd0c55b1d8aaec8af8ff3402a5856263923ed`: preregistration; freeze-check `--substance --chronology` `SUMMARY claims=2 findings=0` (`census/round-79/records/freeze-check-at-F.txt`).
- W1 `c8c3fbca5ac44184feac3a01ee964139f86c02a4`: C1 candidate gate (blob sha256 `ae5022c5…7e1c`): `gate_run`/`gate_run_file` run every git, find, head and python child as an asynchronous job under `timeout`, output through a private mktemp dir; TERM/INT/HUP traps.
- W2 `17009fa1f9d335a1bdde1e22ff3894c5d571c250`: C2 candidate `census/round-79/c2-pointer-counter.py` (range = exact expansion; whole next-line run; MOVED needs `round-<N>`; QUARANTINED needs a committed declaration).
- A `b8d094299e06bc66352f5232cd7a75d1f503c0fa`: after-arms (C1 red on s4; regressions green; C2 green).
- R1 `4a9bbb303db7f1508e24f60d4b9feff80bcbc079`: a repair for a supposed pending-signal race, committed before the cause was probed (lesson M2). Its receipts (`census/round-79/records/repair/`) fail s4 identically 3/3. R2 `feebf2ba6f120903e45d31cf322751c052f2feb9` reverts it (gate bytes = W1). S79ScoutSources later confirmed from the bash 5.3.20 source that no such race exists (`wait.def:193` reads the pending trap before blocking).
- D `92cab9c782457c4256acc6f099375caf4056fca3`: `census/round-79/probes/sigint-inherit.sh` (background-launched bash: `trap -- '' SIGINT`; background python: SIGINT ignored) and the foreground re-measurement (`census/round-79/records/foreground/`).
- I `625c6d24a6911f0a8ccec8e294a685fdb8aa31e6`: S325/S326 rows + provenance, `corpus/knowledge/gate-signal-handling.md`, QUALITY Q142/Q143, README frontier r79, SKILL rows r79, SCORECARD r79 rows, LOG `## Round 79`, lesson draft; `2827fbe51274c93d35350e7c10fa25166892d84f` domain-trial script.
- Wave w1 (12 seats, 0 dead) → I2 `4bf467257b794cc48dce77bdc20ad4ad563b4f22`: mirror `census/round-79/records/wave-w1/`, the M09 response receipt, S325's second anchor, the knowledge entry restored after a seat overwrote it (M5) and corrected (M6), wording fixes, lesson `## Wave`/`## Mistakes (wave)`/`## Routed to round 80`. Census-after `8ecff7f677526ca671844ba318ff0ecfb96ade8e`.
- Domain trial (C1 conjunct): the W1 gate over the lane itself at the report tip, no-signal arm and a real-lane SIGTERM arm, through the committed `census/round-79/probes/domain-trial.py` (`census/round-79/records/c1-domain-trial.txt`, landed in the final lane commit).

## Landed changes

Every change below is tied to LOG.md `## Round 79` and to the commit that carries it.

| change | commit |
|---|---|
| counters, populations, control variants and receipts, captures, census-before, pre-freeze feasibility | `d7f40f764e6b25e32662384761d82d3032714eb1` |
| preregistration | `e98cd0c55b1d8aaec8af8ff3402a5856263923ed` |
| C1 candidate gate | `c8c3fbca5ac44184feac3a01ee964139f86c02a4` |
| C2 candidate counter | `17009fa1f9d335a1bdde1e22ff3894c5d571c250` |
| after-arms | `b8d094299e06bc66352f5232cd7a75d1f503c0fa` |
| misdiagnosed repair and its revert (with R1 receipts) | `4a9bbb303db7f1508e24f60d4b9feff80bcbc079`, `feebf2ba6f120903e45d31cf322751c052f2feb9` |
| diagnosis probe, foreground re-measurement, wave spec | `92cab9c782457c4256acc6f099375caf4056fca3` |
| corpus, SKILL, SCORECARD, LOG, QUALITY, README, lesson draft | `625c6d24a6911f0a8ccec8e294a685fdb8aa31e6` |
| domain-trial script | `2827fbe51274c93d35350e7c10fa25166892d84f` |
| wave mirror and wave-driven corrections | `4bf467257b794cc48dce77bdc20ad4ad563b4f22` |
| census-after | `8ecff7f677526ca671844ba318ff0ecfb96ade8e` |
| domain-trial receipt | final lane hash below |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | `census/round-79/controls/c1-K-a-do-nothing.txt`: `SUMMARY rows=11 mismatches=10 errors=0 orphans=10`, EXIT=1; K-b trap-only 10, K-c no-kill 10 | **A** `census/round-79/records/c1-after.txt`: `SUMMARY rows=11 mismatches=1 errors=0 orphans=1`, EXIT=1 (s4 INT; kill rule met — C1 fails at A). Post-measurement foreground re-run, same counter and gate bytes: `census/round-79/records/foreground/c1-at-W1-fg-run1.txt` (and run2, run3) `mismatches=0 orphans=0`, EXIT=0. Regressions r78 17/17, r77 16/16, r76 30/30, r36 21/21, r27 4/4 | `python3 -B census/round-79/c1-signal-counter.py --gate-dir DIR --work WORK` | `c8c3fbca5ac44184feac3a01ee964139f86c02a4` (gate blob `ae5022c5…7e1c`); A receipt in `b8d094299e06bc66352f5232cd7a75d1f503c0fa`, foreground receipts in `92cab9c782457c4256acc6f099375caf4056fca3` |
| C2 | `census/round-79/controls/c2-K-a-r78-counter.txt`: `SUMMARY rows=9 mismatches=5 accepted=5 errors=0`, EXIT=1 | `census/round-79/records/c2-after.txt`: `SUMMARY rows=9 mismatches=0 accepted=0 errors=0`, EXIT=0; K-b refuse-all 9/9 but `resolved=3` of 22 on the r78 regression (EXIT=1); ablations range 2, nextline 1, moved 1, quarantine 1 (all EXIT=1); regressions r78 22/22 + 12/12, r77 35/35 + 7/7 | `python3 -B census/round-79/c2-false-row-harness.py --counter census/round-79/c2-pointer-counter.py --lane LANE --fleet-root FLEET --work WORK` | `17009fa1f9d335a1bdde1e22ff3894c5d571c250` (after-arm commit `b8d094299e06bc66352f5232cd7a75d1f503c0fa`) |

**C1** — counting command `python3 -B census/round-79/c1-signal-counter.py --gate-dir DIR --work WORK`; measured against W1 `c8c3fbca5ac44184feac3a01ee964139f86c02a4`.

- Verdict on the frozen predicate: **fails at A** (1 mismatch, 1 orphan). The frozen Stated limits do not name "a signal ignored on entry"; the claim as written reads unconditional, and the A receipt's `command=` line does not record the `&` launch it ran under (S79CriticDiscern F3, S79CriticClaims MEDIUM-2).
- Cause, reproduced by four non-author seats: launched with `&`, 13 of 13 runs fail only s4 with the A signature; launched in the foreground, 13 of 13 runs score 11/11 (S79ExecC1; also S79ScoutSources, S79Reviewer, S79CriticClaims). bash 5.3 refuses to trap a signal ignored on entry (S325 node Bourne Shell Builtins lines 3942-3943; `trap.c:851-854` per S79ScoutSources).
- Qualifications: rows s3/s4 block at check 0's first `git config` read, not at `ls-remote` (the shim's pattern matches the row directory name; lesson M1); the rows cannot tell a group kill from a pid kill, because timeout's own child also gets PR_SET_PDEATHSIG (S79MutGate M01/M02 survive); a grandchild left by an earlier, finished child survives (S79ExecEvade MEDIUM-1); the control receipts' INT rows are launch artefacts too. S79MutGate's HIGH M09 (no `<&0`) is killed by the round's own r76 regression conjunct (`census/round-79/records/wave-responses/m09-vs-r76.txt`, 13 mismatches).

**C2** — counting command `python3 -B census/round-79/c2-false-row-harness.py --counter census/round-79/c2-pointer-counter.py --lane LANE --fleet-root FLEET --work WORK`; measured against W2 `17009fa1f9d335a1bdde1e22ff3894c5d571c250`.

- Verdict on the frozen predicate: **verified** (5 → 0; K-a 5, K-b red on its regression conjunct, all four ablations red; both regressions green; S79ExecC2 reproduced every receipt and found the r77/r78 ITEM lines identical under both counters).
- Qualifications (S79MutCounter): 8 of 13 mutants of the four new rules survive the frozen population, and the r79 counter still accepts NF6b (token and target matched as substrings of other paths), NF8 (a range member that is a directory), NF10 (a byte-equal MOVED copy in an unrelated subtree) and NF6a (the preregistered limit: a declaration in prose). Routed to round 80.

No owned axis score changed (calibration 7, coverage 8, operability 8).

## Sources & frontier

- **Census.** Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
  - Before: `census/round-79/records/census-before.txt`, `souji ok`, EXIT=0.
  - After: `census/round-79/records/census-after.txt`, `souji ok`, EXIT=0.
- **Rows** (`grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`): 247 → 249.
  - Added: tier A ×2. S325 GNU Bash 5.3 manual node Signals as installed (bash 5.3.20-1; docs, `mined`) and S326 coreutils `src/timeout.c` at v9.12 (code, `mined`), both cited by `corpus/knowledge/gate-signal-handling.md` and QUALITY Q142/Q143; C1 rests on them (sourced claim).
  - Rejected (lesson Gate): the gnu.org bash and timeout manual pages (unreachable, curl exit 28); the bminor/bash mirror path for doc/bashref.texi (HTTP 404 ×3); coreutils timeout.c at master (replaced by the installed v9.12 tag).
  - Rows touched old→new: S325's teaches cell gained the second anchor (lines 3942-3943, "signals ignored upon entry to a non-interactive shell cannot be trapped or reset"; S79ScoutSources F2) and its source cell says "node excerpt … lines 3243-3290" instead of "node text" (S79CriticDiscern F6), both before landing. No existing row's status, recheck or used-by cell changed.
  - Non-L1 re-open: S79ScoutSources re-fetched/re-hashed both (sha256 match), located every quote, and admitted both; S79CriticDiscern agreed (code is the right citation for the process-group behaviour; the manual rows cover exit statuses only).
- **Frontier advanced.** README "Frontier (r79 gate signal handling and false ledger rows)". It stays frontier.
- **Mistakes mined:** six (`corpus/lessons/round-79.md` `## Mistakes` M1–M4, `## Mistakes (wave)` M5–M6), each with captured-by and a fix; M2's fix is shown able to fail (`census/round-79/records/foreground/sigint-inherit-under-ignored-int.txt`, EXIT=1); M1's is not yet (stated in the lesson).
- **Assimilation: none.** `considerthese/` is absent in this lane; no shokuknow theme fits the frozen claims.

## Trend verdicts

- **expansion: improved** — two mined tier-A rows on ground the lane did not hold (bash trap deferral and signal dispositions; timeout's process group), a new knowledge entry `corpus/knowledge/gate-signal-handling.md`, QUALITY Q142/Q143, a new harness and two capability rows each backed by a receipt.
- **quality: unprovable-but-better** — the gate now kills its running child on a caller's signal (foreground 13/13 runs at four seats, 171 timing probes without a kill-rule violation, a real-lane SIGTERM arm in the domain trial), and C2's instrument refuses five false rows it accepted; but C1's frozen measurement is red, a misdiagnosed repair was committed and reverted, and a seat overwrote a lane file. No single counter carries the net; the operator rules.
- **discernment: improved** — the L1 recorded its own misdiagnosis (M2/M4) and reverted it rather than re-running until green; it accepted S79CriticClaims HIGH-1 (ambiguous "kill rule met") and S79CriticDiscern F1/F6/F7 against its own text; four non-author seats independently confirmed the launch-artefact diagnosis and the source re-opens agree 2/2.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md gate rows "r79 pre-report gate signal counter (C1)" and "r79 false-ledger-row harness (C2)" (`625c6d24`), with the run-in-the-foreground rule.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md `## Round 79` — the gate run on the lane itself with a real SIGTERM while a child runs (`census/round-79/records/c1-domain-trial.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: twelve seats re-ran the prereg commands as written and reproduced every receipt, including the s4 launch artefact (`census/round-79/records/wave-w1/seats/S79ExecC1.md`, `S79ExecC2.md`, `S79Reviewer.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: sibling gates were documented, not edited (`census/round-79/records/wave-w1/seats/S79Connector.md`); the fleet misroot sweep found no file of this round.

## Other

- **Round shape:** one v1 wave `w1` of 12 seats, validated under `ufo-wave-policy.json` (band 8–16; `schema ufo-swarm-wave-dispatch-v1`, spawn 12) and dispatched via the inline handoff (`census/round-79/records/wave-w1/w1.ready.dispatched`). WAVE-DONE received (`w1-results.json`, 12 results). No residual call; round total 12.
  - Role mix: connector 1, scout 1, executor 3, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1. Attack seats 5 of 12 (42 %). The L1 holds the §3 planner seat.
- **Dead seats:** 0; all 12 wrote report files.
- **External delay:** the dispatcher held the wave 02:28–03:20 because a finished kama r93 seat had leaked 200 busy-loop processes and the host load stayed above the spawn gate (orchestrator's incident, per Main).
- **Seat incident:** S79Scribe wrote its knowledge draft over the tracked `corpus/knowledge/gate-signal-handling.md` (lesson M5); caught by `git status` before integration and restored from master.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only orchestrator `.scratch/*` and the pre-existing `?? trail-ids.txt`; nothing of this round.
- **Routed to r80:** lesson `## Routed to round 80` (a)–(d) and SCORECARD "r80 (planned)".
- **Open L0 questions:** none new.
- **Tool installs:** none. No pacman transaction, no sysctl, sudo or kernel change.
- **Scratch:** `/fast/scratch/hyaku/souji-r79/` removed at landing.

## Stale-lane

Stale-lane: respawn-per-round driver; this lane has no other open mission.

Domain trial (C1 conjunct): `census/round-79/records/c1-domain-trial.txt`, run through the committed `census/round-79/probes/domain-trial.py` at the report tip. Its receipt grades every byte of this report except the `Final lane hash:` line (report_sha256 over the filed bytes with that line removed) and binds the gate bytes it ran against the W1 blob (`amendment=none` when equal).
Final lane hash: 35b208cc72b014fa5af68101c0561e7974f1fe76
