# souji — round 69 (attempt 1) — battery outcome split (C1), ambient clean environment (C2), declared-protection coverage (C3)

Lane: souji (repo /home/vgpnk/Projects/shokunin/souji-shokunin). Lane base 893b8ef4e73b3fde45f712df3437a032b1d92d42 (r68 admitted). Freeze 1412037c9fac1cd18381075d22fefbac06ae5bac. After-arm and wave evidence 89fea6be. Lane tip at report time: a7f34e159da38dff651d471e004a683c27f69bb9. Round shape: one v1 wave `w1`, 12 seats (4 executor, 1 scout, 1 connector, 1 scribe, 1 reviewer, 2 critic, 1 mutation-tester, 1 sentinel); attack seats 4 of 12 (33%); connector 1; L2 floor met (connector, executor x4, scribe, scout, reviewer, critic; planner held by the L1). Wave dispatch document: `.ufo/waves/round-69/w1-dispatch.json` (schema ufo-swarm-wave-dispatch-v1, counts spawn 12, policy band 8–16). Routing: task.agentModelOverrides only; no model passed.

## Work performed

Declared claims (1–3; axes calibration, operability, coverage; no exploratory claim, no capability other than the one recorded below):

- **C1 — calibration (lowest owned axis, score 7; bookkeeping file).** Outcome-class split of the writer battery: every refutation classified forgery / echo-violation / over-refusal / label-only / survived / error; only forgery counts as a declared-protection kill (QUALITY Q131). Evidence: `census/round-69/c1-counter.py` (`classify_outcome`, battery branch of `main()`), `census/round-69/records/c1-after-battery.txt`, `census/round-69/battery-manifest.tsv`, `census/round-69/battery/` (28 committed members, `SHA256SUMS`).
- **C2 — operability (bookkeeping file).** The counter's clean environment under a wider ambient tuple (HOME, XDG_CONFIG_HOME, GIT_TRACE, GIT_TRACE2_EVENT, GIT_TRACE2_PERF, env -i): 0 flips. Evidence: `census/round-69/records/c2-clean.txt`, `census/round-69/records/c2-ambient.txt`, `census/round-69/controls/c2-do-nothing-ambient.txt`, before arm `census/round-69/probes/c2-before-r68-ambient.txt`.
- **C3 — coverage (bookkeeping table).** Declared writer protections with a battery row: 0 of 14 → 12 of 14, with 2 named limits (D18, D29). Evidence: `census/round-69/records/declared-coverage.tsv`, `census/round-69/controls/c3-do-nothing.txt`, `census/round-69/controls/d18-limit-battery.txt`, `census/round-69/controls/d29-limit-battery.txt`.

Work items (each with its evidence):
- Pre-freeze probes, labelled as probes (`census/round-69/probes/`): the candidate run P1 (`candidate-run-p1.txt`, EXIT=0); a partial six-mutant battery and a 27-mutant battery, both superseded (`battery-probe-27-prefix.txt`: K7, D10, D18, D19, D29 and D30 defects); the fsmonitor hook probe (`fsmonitor-hook-probe.txt`); the index.lock and relative-GIT_COMMON_DIR probe (`lock-and-commondir-probe.txt`); the D10 read-through repro (`d10-repro.txt`).
- Freeze commit `1412037c` (instruments, controls, probes, sources, prereg). Controls before after-data: c1 do-nothing EXIT=1 (`controls/c1-do-nothing.txt`: SUMMARY matrix=47 base_forgeries=3 new_forgeries=3 class_mismatches=4 regress=PASS), c2 do-nothing EXIT=1, c3 do-nothing 14 'none'.
- Fixes made before the freeze after the probes exposed them: W4 rebuilt at `main/main/.git` (Q132); D18 row removed (unobservable; named limit); D19 hook prints a timestamp token; D10 seed `tools/notes-copy.txt`; PK7 clears the NOSYSTEM pin in its caller env; D30 replacement made valid Python; battery guard removed; SHA256SUMS regenerated. Each fix is in the probe trail and in the lesson `## Mistakes` M1–M9.
- After-arm `89fea6be`: battery receipt (26 mutants), C2 clean and ambient receipts.
- Wave `w1` (12 seats): one v1 wave, 12 seats (`.ufo/waves/round-69/w1-spec.json`, `w1-dispatch.json`, `w1.ready`, dispatched by the orchestrator). Settled at filing: S69ExecBattery, S69ExecCoverage, S69ExecAmbient, S69ExecD10, S69Connector, S69CriticClaims, S69CriticDiscern, S69MutTester, S69ScoutSources, S69Sentinel. NOT settled at filing (WAVE-DONE not received; the budget notice ended the wait): S69Reviewer and S69Scribe, still running at ~25 min; their outputs are not used in this report and must be read by the next closer. Dead seats: none observed. Findings and per-seat verdicts are in `corpus/lessons/round-69.md` `## Gate` and summarized below.
- Frontier: S302 (git-status(1)) and S303 (git(1)) opened and quoted this round (`census/round-69/srcs/`); knowledge entry `corpus/knowledge/battery-outcome-split.md` (provenance trio; cites S302, S303); corpus/README.md frontier section `### Frontier (r69 battery outcome split)`.
- Corpus: `corpus/lessons/round-69.md` (`## Mistakes` M1–M9, `## Gate`); SOURCES rows S302, S303 appended (registry 224 → 226); LOG.md append (`## Round 69`); SCORECARD.md updated (round 69 measurements, capability row, planned bullet).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: counter, matrix, battery members, manifest, controls, probes, sources, prereg | `## Round 69` (LOG.md) | `1412037c9fac1cd18381075d22fefbac06ae5bac` |
| after-arm receipts and wave w1 evidence (spec, dispatch, ready) | `## Round 69` | `89fea6be` |
| knowledge entry, sources rows, lesson, README frontier, SCORECARD, LOG | `## Round 69` | a7f34e159da38dff651d471e004a683c27f69bb9 |

The writer `tools/souji-receipt-write.py` is unchanged this round (blob at base = blob at tip).

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 outcome split | r68 records: 0 `MUTANT`/`BATTERY` lines; hand classification 10 forgery / 2 over-refusal / 2 label-only | `BATTERY mutants=26 kills=18 label_only=5 over_refusal=2 echo_violation=1 survived=0 error=0` EXIT=0 | `grep -c '^MUTANT .* outcome=forgery' census/round-69/records/c1-after-battery.txt` (18); `grep -c 'outcome=label-only'` (5); `grep -c 'outcome=over-refusal'` (2); `grep -c 'outcome=echo-violation'` (1); `grep '^EXIT='` (0) | `89fea6be` (counter bytes `1412037c`) |
| C1 W4 base arm (Q132) | r68 CAND W4 `base=refuse` ×1 (unrelated fixture failure) | `CASE W4 … base=accept` ×26; candidate W4 `new=refuse` unchanged | `grep -c '^CASE W4 .* base=accept' census/round-69/records/c1-after-battery.txt` (26); `grep -c '^CASE W4 .* base=refuse' census/round-68/records/c1-after/CAND.txt` (1) | `89fea6be` |
| C2 ambient flips | r68 counter, wider tuple: 6 flips, ambient EXIT=1, REGRESS=FAIL | 0 flips; clean EXIT=0; ambient EXIT=0 | `diff <(grep -E '^(CASE\|SUMMARY\|REGRESS\|EXIT=)' census/round-69/records/c2-clean.txt) <(… c2-ambient.txt) \| grep -c '^[<>]'` (0) | `89fea6be` |
| C3 coverage | 0 of 14 U-rows with a battery mutant (`controls/c3-do-nothing.txt`) | 12 mutant, 2 limit | `awk -F'\t' 'NR>1{print $5}' census/round-69/records/declared-coverage.tsv \| sort \| uniq -c` | `89fea6be` |

## Sources & frontier

- SOURCES registry: before 224 rows (`git show 893b8ef4:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` = 224); after 226 rows (`grep -cE …` on the working tree = 226). Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` rc 0 before and after; malformed 0; duplicate ids 0; tier histogram A=216 B=7 C=3; status histogram mined=188 queued=14 rejected=24.
- Rows added by tier: S302 tier A (git-status(1), scope background optional-lock advice), S303 tier A (git(1), scope --no-optional-locks). Rows touched old→new: none.
- Frontier rows advanced: battery outcome split (`corpus/README.md` `### Frontier (r69 battery outcome split)`; knowledge `battery-outcome-split.md`). No promotion to Core.
- Assimilation: none. `considerthese/` is absent in the lane (`test -d considerthese` false). The shokuknow `merge/souji/` package (134 rows, 68 entries) has 0 knowledge entries or rows matching optional-lock, index.lock, fsmonitor, GIT_COMMON_DIR or receipt-writer topics (`grep -ilE` count 0). The quarantine slice (`absent-defect-register.md`, lane souji) has 8 data rows, all `payload-absent` or unchecked; none adopted, none appended.

## Claim verdicts

- **C1 (calibration, Q131 outcome split): VERIFIED on its frozen predicate.** Reproduced byte-identically by S69ExecBattery and S69CriticClaims (MUTANT/BATTERY/EXIT and CASE lines diff 0); do-nothing red (EXIT=1, new_forgeries=3). Qualified, not counted as passes: the Q131 precedence is untested by selftest and battery (S69MutTester, MEDIUM); the battery expectation gate is not run by the selftest (MEDIUM); the receipt binds no member, manifest or battery-dir hash and the arm does not verify members against SHA256SUMS (S69Sentinel F-3, MEDIUM).
- **C2 (operability, ambient tuple): VERIFIED on its frozen tuple only; NOT ambient immunity.** 0 flips under the frozen tuple. HIGH, routed: GIT_TEMPLATE_DIR executes host hooks inside the fixtures and flips verdicts (S69Sentinel F-1); GIT_LITERAL_PATHSPECS=1 makes the writer forge receipts over skip-worktree, gitlink, absent and unmerged rows (S69CriticClaims, HIGH; the base writer does the same, so it predates this round); GIT_ATTR_SOURCE, GIT_EXEC_PATH give 100 flips (S69ExecAmbient). The writer is unchanged and these are not repaired here.
- **C3 (coverage, declared protections): VERIFIED on its counting predicate (12 mutant, 2 limit).** Reproduced by S69ExecCoverage. Qualified: of the 12, 8 are declared-protection kills by forgery, 3 label-only, 1 echo (covered=12 is honest only under the frozen refutation wording); D06 is carried by D08/D10 rows (MEDIUM); the D29 limit is false under GIT_LITERAL_PATHSPECS=1 (MEDIUM).

**Admission.** Each claim verifies on its frozen predicate and no owned axis score moved (writer unchanged). The wave's qualifications are reported above and are not counted as passes. Whether this round is admitted is for the non-author closure and the operator to rule.

## Trend verdicts

- **expansion: improved.** Evidence: knowledge entry `battery-outcome-split.md` on the battery-classification ground (grounded in S302, S303; expansion credit is on ground the coverage map did not hold: corpus/README.md has no battery-classification row before this round).
- **quality: unchanged.** Evidence: the writer's declared-protection set is measured for 12 of 14 U-rows; the measured limits are named; the frozen r68 predicate is not amended (Q131 is mechanized by a successor, not a rewrite).
- **discernment: unchanged (no non-author spot-check landed; the in-wave discernment seat is lane-dispatched and does not count, LEARNING.md).** Evidence: S69CriticDiscern agreed with the S302 and S303 admits and the git-status variable reject, and disagreed with the held-lock reject reason (amended). Its own F1 (HIGH) is correct: it is not the non-author check. The discernment trend needs a fresh non-author reviewer or the operator to check this gate.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` (existing tables); round-69 contribution: `corpus/knowledge/battery-outcome-split.md` (outcome table, precedence, cited S302/S303).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` `## Round 69` (battery run `census/round-69/records/c1-after-battery.txt`, C2 clean/ambient receipts).
- [~] Instructions executable by an agent without oral context — pointer: `census/round-69/preregistration.txt` counting commands; `census/round-69/records/c1-after-battery.txt` reproducible via the frozen command.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` (unchanged this round); connector seat result in `.ufo/waves/round-69/w1/S69Connector.md`.

## Stale-lane

None. The respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. No pacman transaction. No sysctl, sudo or kernel parameter change by any seat or by the L1. Seats were instructed not to change host state.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` before the report: ` M .scratch/run15-state.json` (orchestrator-owned; not a misroot) and ` M .ufo/l0-questions.md` (other lanes' lines appended by their L1s; not this round's; not committed by this lane). No untracked file at the fleet root names souji or round 69.

## L0

No new L0 line appended by this round. Open questions from earlier rounds remain (souji round-66 line on the honest-run refusal trade; souji round-67 relative-value trade; souji round-68 kill-rule split, now answered in part by Q131 mechanized; souji round-68 writer verifier), routed around, not answered here.

## Mistakes

See `corpus/lessons/round-69.md` `## Mistakes` (M1–M9). Sweep for mistakes that found none: `grep -c 'base=refuse' census/round-68/records/c1-after/CAND.txt` (1) and `grep -E '^EXIT=' census/round-69/records/c1-after-battery.txt` (EXIT=0), both run before the freeze.

## Inherited state

Attempt 1 of round 69; no prior attempt. No uncommitted lane-authored leftovers at round start (`jj-lane.sh state` local=ahead=0 at 893b8ef4). No file authored by another lane was edited.

## Erratum (appended after filing; supersedes the "NOT settled at filing" text above and the stale lane-tip line)

WAVE-DONE for wave `w1` arrived after this report was filed: all 12 seats settled, none dead. `w1-results.json` and the seat reports are in `.ufo/waves/round-69/w1/`.

- **S69Scribe** (settled after filing): reproduced every C1/C2/C3 number independently, then filed one HIGH finding incorporated as errata in lane commit `751f268562d374dfd2a4193b1317c08a7536be19`: the D18 named limit is also a **harness artefact** — the counter's `clean_env()` pins `GIT_OPTIONAL_LOCKS=0` into every writer slot, so the D18 mutant inherits the counter's pin and no row in this harness could observe a lock-contingent verdict. The limit stands on that ground plus the probed git behaviour. The knowledge entry and the round lesson state both grounds. It also corrected the D29 reason (the mutant drops `:(top)` from the flag-check call only) and recorded prereg pointer errata (M14) and the coverage-table chronology erratum (M15).
- **S69Reviewer** (settled after filing): **SOUND on every review axis; no HIGH or MEDIUM findings.** The W4 rebuild, no-echo judge, classifier precedence, manifest loader, battery branch, selftest checks 4-6, all five new fixture kinds (comment-vs-build, Q132) and the preserved clean_env tuple all check out; its independent battery run reproduced `BATTERY mutants=26 kills=18 label_only=5 over_refusal=2 echo_violation=1 survived=0 error=0`, EXIT=0, 26/26 outcomes matching the manifest. Two LOW informational notes (echo evidence subsumed by the forgery precedence; battery `--work` residue not self-deleted). Its verdict contradicts nothing in this report.
- Lane tip after these commits: `0d8c8c7b465506e71ffa3c57134a6b615c7d2e0f` (LOG append for the reviewer verdict; pushed).

This erratum supersedes: the sentence in Work performed beginning "NOT settled at filing (WAVE-DONE not received…)", and the Claim-verdicts/SHONEN context implying two seats were unread — both are now read; no claim verdict changes.
