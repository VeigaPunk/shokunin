# souji — round 97 report (attempt 1)

Lane: souji-shokunin. Lane base `210084b24de1dd1f1fd499f49b0c70744f099f5f` (r96 closed `ok`). Lane final: `ff254387005e35ff442555451374ff079dafc2db` (= `git ls-remote origin refs/heads/master`). L1: SoujiR97. Wave: one v1 wave, 13 seats, all settled (WAVE-DONE received; `.ufo/waves/round-97/w1-results.json`).

## Work performed

Declared claims (2; both on distinct axes; at least one on the lowest owned axis, calibration 7):
- **C1 — calibration 7.** A RERAISE-aware pending-clear latch in the r96 survivor search keeps the 14-shape declared-exit table at `mismatched=0` (`census/round-97/c1-survivor-search.py`, shapes `census/round-97/shapes/`). **Verdict: harmed (trade).** The latch regresses `q1q` (caught-at-module then a direct terminating `helper()`) from 70 to 1 and leaves `q1o` (saved exception re-raised by bare `raise`) at 1. Not admitted; score stays 7. Evidence: `.ufo/waves/round-97/w1/R97ReviewerC1.md` Q1 (receipts `R97ReviewerC1/receipts/q1o.py`, `q1q.py`); `plans/round-97.md` A9.
- **C2 — operability 8.** The r97 probe caps captured output and the r97 counter reaps the T1 setsid grandchild by argv identity, printing `survivors=<n>`. **Verdict: not admitted.** The reap signals own-uid processes the counter did not plant (30 of 42 foreign decoys killed in a continuous run; `planted-killed 31`). That is a refusal-boundary violation (PROVINCE), so the claim cannot verify. Evidence: `.ufo/waves/round-97/w1/R97Sentinel.md` Finding 1 (receipts `R97Sentinel/repro_foreign_pid_kill.out`, `continuous_decoy_42_planted.out`); `plans/round-97.md` A12. The hang leg (r95 probe `ARM T1 exit=hung`, conform 19 → r97 probe `exit=2`, conform 20) is measured and real but is not separable from the reap in the predicate.

Work items (evidence pointers):
1. Pre-freeze protocol load and claim choice: `plans/round-97.md` A0.0–A0.3; SCORECARD `### Planned (r97)` (read at `SCORECARD.md`).
2. Instruments P1 `053287d4` (`census/round-97/*.py`, `shapes/` 14 scripts, `c1-targets.json`, `srcs/monitoring.html` = S372 capture sha256 `2b281793…`, `run-receipt.sh`).
3. Controls P2 `677a6cbb` (`census/round-97/controls/`: `c1-control-r95-rule.txt`, `c1-forgery-controls.txt`, `shapes-r95/r96/r97.txt`, `c2-control-r95-probe.txt`, `c2-control-r96-probe.txt`, `c2-forgery-controls.txt`, `prefreeze-feasibility-note.txt`).
4. Freeze F `5314d01d` (`census/round-97/preregistration.txt` only in F; the P2 commit also carried `plans/round-97.md`, `c2-setup-arms.py`, `c2-forgery-controls.py`).
5. Wave w1 (13 seats; see §Wave shape); attack verdicts collected in `.ufo/waves/round-97/claim-falsification.tsv` (copy `census/round-97/claim-falsification.tsv`).
6. Sourced claim: C1 rests on S372 (sys.monitoring RERAISE), opened 2026-11-09 (`R97ScoutSources.md` §2 re-verified it live and byte-identical).
7. Integration: amendments A7-correction and A9–A17 in `plans/round-97.md`; S372 row repaired in-round (A16); knowledge corrections appended in `corpus/knowledge/crash-channels-beyond-excepthook.md` and `deadline-owned-reaping.md`; `corpus/lessons/round-97.md` (Gate, Mistakes M1–M5, trend verdicts); QUALITY Q173 and Q174; SCORECARD `### Round 97 measurements`, `### Planned (r98)`; LOG `## Round 97`.
8. Wave evidence capture: `census/round-97/wave-evidence/` (402 files, `MANIFEST.sha256` verified `sha256sum -c` from its directory: OK), because `.ufo/waves/` is git-ignored in the lane (`.gitignore:1`).
9. L0 question (operator decision on the reap): appended to `.ufo/l0-questions.md` (line `souji | round-97 | C2 counter …`).

## Landed changes

| change | file(s) | LOG entry | commit |
|---|---|---|---|
| P1 instruments, plan A0, S372 row (first form), capture | `census/round-97/*`, `plans/round-97.md`, `corpus/SOURCES.md`, knowledge r97 sections | `LOG.md` `## Round 97` (written at verdict commit) | `053287d4` |
| P2 controls + freeze F | `census/round-97/controls/`, `preregistration.txt`, `c2-setup-arms.py`, `c2-forgery-controls.py` | (same) | `677a6cbb`, `5314d01d` |
| Wave spec + claims + dispatch record (ignored paths captured) | `.ufo/waves/round-97/*` (copied to evidence) | (same) | `fd0be377` |
| Verdicts, amendments A7-correction, A9–A17, lesson, Q173/Q174, SCORECARD r97, S372 repair (11 cells), knowledge corrections, wave-evidence capture, ledger | see table in §Work performed | `LOG.md` `## Round 97` | `ff254387` (lane final) |

## Before → after measurements

Counting commands are re-runnable at the cited revisions. Exit codes shown.

- **C1 declared-exit table (14 shapes).** Before (r96 hook): `python3 -B census/round-97/declared-shapes.py --search census/round-96/c1-survivor-search.py --scripts census/round-97/shapes --work <empty>` → `SHAPES-SUMMARY shapes=14 mismatched=2` (x1/x2 at 1), EXIT 1 (`census/round-97/controls/shapes-r96.txt`). After (r97 hook, `053287d4`): same command with `census/round-97/c1-survivor-search.py` → `SHAPES-SUMMARY shapes=14 mismatched=0`, EXIT 0 (`shapes-r97.txt`). r95 hook (control): `mismatched=2` (t1/t4 at 70), EXIT 1 (`shapes-r95.txt`). **Trade:** q1q 70 → 1 (`R97ReviewerC1` Q1). Not admitted.
- **C1 ten-target search (non-discriminating, prereg limit v).** `python3 -B census/round-97/c1-survivor-search.py --counter census/round-87/c1-pointer-counter.py --harness census/round-93/c1-false-row-harness.py --population census/round-93/c1-false-rows.tsv --lane . --fleet-root /home/vgpnk/Projects/shokunin --work <empty> --jobs 5 --ids census/round-97/c1-targets.json` → `SEARCH-SUMMARY generated=10 … errored=7 killed=2 survived=1`, EXIT 0 (r95 control: same line, `c1-control-r95-rule.txt`).
- **C1 no-harm on the generated population (278 mutants, not a claim).** r97 vs r96 search, `--jobs 5`: both `SEARCH-SUMMARY generated=278 ambiguous=9 uncompiled=0 hung=1 scored=268 errored=53 killed=139 survived=76`; 0 verdict differences; survivor sets byte-identical (`R97ExecCensus/survivors-r97.json` vs `survivors-r96.json`).
- **C2 arms, r97 probe + committed counter (`677a6cbb`/`053287d4`).** `python3 -B census/round-97/c2-setup-arms.py --probe census/round-97/c2-forgery-probe.py --fixture-pass tests/fixtures/r93-k4-flagfail.py --fixture-fail tests/fixtures/r92-k4-flagfail.py --tool tools/souji-record-agreement.py --before census/round-92/controls/c2-before-tool.py --work <empty> --jobs 4` → `ARM T1 exit=2 want=2 line=yes conform=yes survivors=0`, `ARMS-SUMMARY arms=20 conform=20`, EXIT 0 (`R97ExecC2.md` §1a). Before (r95 probe, same counter): `ARM T1 exit=hung … conform=no`, `ARMS-SUMMARY arms=20 conform=19`, EXIT 1 (`c2-control-r95-probe.txt`).
- **C2 survivor count (reap leg).** r96 committed counter with r96 probe: `survivors=1` (r96 records, A4). r97 counter with r96 probe: `survivors=0`; reap-removed mutant of the r97 counter: `survivors=1` (`R97Scribe.md` §1 M2). The reap moves the count, and the reap is the harmful part (A12).
- **C2 forgery controls (`c2-forgery-controls.py`, 4 forgeries).** Prereg: `refused=4`, EXIT 0. Measured: `C2-FORGERY-CTL-SUMMARY forgeries=4 refused=3`, EXIT 1. GA, GB, GC refused; **GD not refused** (the counter reaps regardless of the probe's message; A14). GC's forged probe is a SyntaxError (`unexpected indent`, line 129), so it is refused for a syntax reason (A14).
- **C2 basename cheat (critic).** A 3-line probe edit that exits 2 for non-verdict fixtures reaches `ARMS-SUMMARY arms=20 conform=20`, `survivors=0`, EXIT 0 in 54.6 s, with no cap, no selector wait and no reap by the probe (`R97Critic.md` §2). The predicate does not bind the mechanism (A15).
- **Frontier / registry.** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` → at lane base: 293 rows, EXIT 0; at P1 (before repair): `E01 S372 fields=7`, EXIT 1; at `ff254387` (after repair): 294 rows, EXIT 0, no E01. Malformed rows (`awk … NF!=13`): 0 at round end.

## Sources & frontier

- `SOURCES.md` rows before → after: 293 (lane base `210084b2`) → 294 (`ff254387`). Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Census exit 0 at round end.
- Rows added by tier: A +1 (S372, sys.monitoring RERAISE). B +0. C +0.
- **Rows touched old → new:** S372 row shape 7 → 11 cells; anchor word count 14 → 13; `used-by` moved out of `teaches` (A16). No other row was touched in the round (per the P1 and verdict commits; not yet diffed row-by-row in this report).
- Knowledge entries: `crash-channels-beyond-excepthook.md` (r97 section, S372) and `deadline-owned-reaping.md` (r97 section); both carry appended corrections (A9, A11, A12, A13) that withdraw the falsified sentences.
- Frontier rows advanced: none (no frontier row moved to core; F5 process residue and F1–F4 unchanged).
- Candidate sources screened by the scout seat (`R97ScoutSources.md` §6–7, not appended): `write(2)` §ERRORS EAGAIN (man7.org, tier A, admitted by the seat for the errno clause only; not appended — the L1 defers it to r98 with a Gate); `proc_pid_cmdline(5)` (lead: a zombie reads 0 bytes, which an argv-identity scan would miss); `prctl(2)` PR_SET_CHILD_SUBREAPER (non-candidate).
- Assimilation: none (no `merge/souji/` theme; no `considerthese/` dir).

## Trend verdicts

- **expansion: unchanged.** One tier-A row (S372) and two knowledge sections; no new admitted entry on uncovered ground. Evidence: `corpus/lessons/round-97.md` §Trend verdicts; registry 293 → 294.
- **quality: harmed.** Two knowledge entries shipped sentences that the wave falsified (the "closes the trade" sentence in crash-channels; the "signals only processes it planted" sentence in deadline-owned-reaping). Both are corrected by appended notes in this round, but the shipped text was wrong. Evidence: `plans/round-97.md` A9, A11–A13; the appended corrections in both entries.
- **discernment: harmed.** The lane's pre-freeze gate missed three overclaims (C1 closure, C2 ownership, the A8 signal exit) that the wave's reviewers, critic, sentinel and scribe found. The disagreements are recorded and turned into M1–M5 and Q173/Q174. Evidence: `corpus/lessons/round-97.md` §Mistakes and §Gate (discernment spot-check: the non-author seats agree with the lane on the S372 admit; they disagree with the C1/C2 closure sentences).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md Decision tables/Error patterns/Checklists/Gate registry; corpus/SOURCES.md S100-S103, S372; corpus/lessons/round-97.md Gate.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 97` (wave w1 run end to end; verdicts recorded; the r95 and r96 controls were run with the bytes recorded in `controls/`, with the r96-control counter caveat in A7-correction).
- [~] Instructions executable by an agent without oral context — census/round-97/preregistration.txt (predicate commands, exit codes); census/round-97/wave-evidence/MANIFEST.sha256.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md Adjacency; `R97Connector.md` (seat report: no sibling owns the crash-sentinel or probe-timeout surface; not independently re-verified by the L1); the reap finding touches signalling rules (PROVINCE Refuses), recorded in A12.

No box is `[x]`: no non-author verifier has checked a promotion-relevant claim to the protocol's standard, and two claims were withdrawn this round.

## Wave shape and seats

- Shape: one v1 wave, 13 seats (`ufo-wave-policy.json` band 8–16). Roles: 3 executor (R97ExecC1, R97ExecC2, R97ExecCensus), 3 reviewer (R97ReviewerC1, R97ReviewerC2, R97ReviewerShapes), 1 critic (R97Critic), 2 mutation-tester (R97MutC1, R97MutC2), 1 sentinel (R97Sentinel), 1 connector (R97Connector), 1 scout (R97ScoutSources), 1 scribe (R97Scribe). Attack seats (reviewer, critic, mutation-tester, labrat): 6 of 13 (46 %). The L1 holds the planner seat (the validator rejects `planner`).
- Seat spec: 13 seats, matching the dispatch record. No other spec correction is recorded.
- Dead seats: none. All 13 settled.
- Late seats: R97Sentinel and R97ExecCensus were slow; the L1 messaged each (`write agent://<id>`) and they finished. R97ExecCensus's trailer-path file (`.ufo/waves/round-97/w1/R97ExecCensus.md`) remained a 3-line skeleton; its full report is in the seat dir (`w1/R97ExecCensus/R97ExecCensus.md`) and the results JSON carries the verdict. R97Sentinel reported `status complete` through an IRC message that named another lane's scratch and artifacts; that message was not used. The seat's on-disk report was verified directly (`w1/R97Sentinel.md`, 290 lines, FALSIFIES-WORDING) before any verdict was taken from it.
- Scratch: `/fast/scratch/hyaku/souji-r97/` removal is pending at the time of this report and is performed after the report is filed; the seat-scratch statement is per each seat's own report.

## Stale-lane line

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Round 97 is the only open mission; no sibling lane's round is in this lane's scope.

## Tool installs

None. The round needed only `python3`, `curl`, `git` (read-only), `awk`, `grep`, `sha256sum`. No pacman, no sudo, no `~/.local/bin` writes.

## Gates run (main-agent verification)

- `python3 scripts/hyaku/prefile-falsification.py --lane souji --round 97` (before this report existed): `FINDING report-missing …`, `PREFILE-FALSIFICATION: SETUP findings=1`, EXIT 2. All ledger rules passed (16 rows, 8 attack seats read, every falsifying row has a narrowing pointer); the only finding is the report itself.
- `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`: EXIT 0 at round end (294 rows, no E01).
- `sha256sum -c MANIFEST.sha256` (from `census/round-97/wave-evidence/`): OK, 402 files.
- Shape table, ten-target search, forgery runners, arms counter: numbers are taken from the seat reports (`.ufo/waves/round-97/w1/<seat>.md` and their receipts) and from the committed `census/round-97/controls/*` receipts. The L1 did not re-run these at round end; the executor seats ran them on committed bytes (see the seat reports for command lines).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec) at round end: no untracked file named for souji or round 97 outside `.scratch/` (orchestrator-owned, never a misroot). No fleet-root deletion was made by the L1.

## L0 questions

- `souji | round-97 | C2 counter (census/round-97/c2-setup-arms.py) reap kills own-uid processes it did not plant …` — open. The lane routes around it: the reap is not cited as a safe mechanism anywhere; the r98 repair is ownership by recorded spawn pid and ppid chain.

## Pre-report gate

`git -C /home/vgpnk/Projects/shokunin/souji-shokunin ls-remote origin refs/heads/master` → `ff254387005e35ff442555451374ff079dafc2db`, which is the lane's final commit (verdicts commit). No later lane commit exists.
