# mori — round 48 report (L1 MoriR48, attempt 1)

Lane HEAD (pushed): `14c5110d65a2f225e7316e1996e92090b9b8e7cb` — `git -C mori-shokunin ls-remote origin refs/heads/master` prints this hash.
Entering tip `e5dbac05459887d9597ea5d1da0d8e3d024e0d17`; freeze `4387cf94b69ddce455051a1ff38e93795c2e6cde`; data commit `e4dfff32d4f97c7ef250e9a7538fa75d4f284492` (tool and counter bytes unchanged since).

## Work performed

Declared claims, both on lowest (tied 5) axes, no stagnation waiver:

- **C1 (calibration):** the pin reconciler `tools/mori-pin-check.py` cannot be turned green by the junk found in round 47. Scored by `.ufo/waves/round-48/count-c1.py`: 8 frozen junk edits (must be `unmet`), 4 honest edits and the real registry (must be `met`).
- **C2 (depth):** FR2 filesystem-quota entry `corpus/knowledge/quota-observability-r48.md`, 15 claim rows, each a located quote in a committed copy; scored by `count-c2.py`.

Work items:

- **Freeze `4387cf94`** before any seat: contract, both counters, controls, v3 spec, four source copies (`.ufo/waves/round-48/contract.md`, `evidence/freeze-sha256.txt`). Controls: the entering v2 tool scores `junk_met=8`, `stub-always-met` `junk_met=8`, `stub-always-unmet` `honest_unmet=4 real=unmet` (`evidence/control-c1-*.txt`); C2 do-nothing is `unmet` (`evidence/control-c2-donothing.txt`). Counter selftests: `C1_SELFTEST pass=34`, `C2_SELFTEST pass=22`.
- **Tool v3** (`e4dfff32`): rules R1–R8 of `v3-spec.md` from the winning candidate of `ExecV3ImplB` plus the parity-aware pipe split from `ExecV3Residuals`, then R9/R10 added by me after wave-1 critic `CritJunkClasses` (tallies in other cells or on continuation lines are `hidden`, a tally outside backticks is `unparsed`, every digest binds to the nearest preceding in-tree path). Selftest 60/60 (`SKILL.md:938`). v3 found a stale pin, `SKILL.md:168` (r14 harness sha256 prefix `c39e5a73…` matched no file); repaired.
- **Quota entry and rows S479–S484** (`corpus/SOURCES.md`, `corpus/evidence/sources-r48/`). The entry corrects the staged one: the errno number is per architecture (122 generic, MIPS 1133, SPARC 69, read from v7.2 headers), the staged `dead_quota` link is false (provider quota), the RHEL 9 PDF stays out. One overclaim row (superuser exemption) was reworded after wave 2 (`w2/R48RevEntryXfs.md`).
- **Unlanded check** `tools/mori-unlanded-check.py` (selftest 13/13) written by me after `ExecUnlandedCheck` ended mid-debug; closes round-47 routed defect 1. At the final tip it prints `UNLANDED=clean round=48`.
- **Quality bar:** QUALITY 125–128 (`corpus/QUALITY.md:1050-1087`). **Lesson:** `corpus/lessons/round-48.md` (Gate, Mistakes M1–M7, wave findings, errata).
- **Round-47 closure routes** (`corpus/lessons/round-47-verifier-spotcheck.md` §5): defect 1 fixed (tool above), 2 carried (report filed after the last wave settled), 3 realised (successor C2 shape, v3 rules R5/R6, selftest arms), 4 cited, 5 noted in the Gate. LOG erratum for round 47 added.
- **Inherited state:** no earlier attempt of round 48. I deleted untracked round-47 scratch (67 `.scratch/r47*` directories) and round-40 conform-selftest debris created by seat runs; nothing there was tracked. No fleet-root misroot of this lane (`git -C /home/vgpnk/Projects/shokunin status --porcelain`: untracked `.ufo/waves/round-30/` and `round-41/w1/ExecQuarantineSlice.md` belong to other lanes, left alone).
- **Round shape: two v1 waves, 83 seats, no residual call.** I held the planner seat.
  - **w1 (build + first falsifiers): 49 seats.** Roles: executor 13, scribe 13, scout 6, critic 6, reviewer 4, mutation-tester 3, connector 2, sentinel 1, simplifier 1. m_flash roles (executor/scribe/simplifier) 55%, with critic/sentinel 69%; attack share 26%. 39 reports on disk; 10 seats produced none: `ExecV3ImplA` aborted after editing the tracked tool and restoring it, `ExecUnlandedCheck` ended mid-debug, and eight (`ScribeQuality`, `ScribeScorecard`, `ConnSiblings`, `ConnCrossClaim`, `RevC1Counter`, `RevC2Counter`, `MutC1Counter`, `MutC2Counter`) returned other lanes' seats' output under the same name (lesson M6). Dead seats stay dead; wave 2 used `R48`-prefixed names.
  - **w2 (falsify): 34 seats.** Roles: reviewer 10, executor 8, mutation-tester 6, critic 4, connector 2, scribe 1, sentinel 1, simplifier 1, scout 1. m_flash roles (executor/scribe/simplifier) are 29% (44% with critic/sentinel), below the run-7 target of 50%; attack share 59%. All 34 settled with 34 reports on disk.
- **Assimilation:** theme FR2 (quota) from `shokuknow/merge/mori/`; **considerthese:** `2026-10-25` suggestion 2 (host-path portability count) → QUALITY 127 and the scoped counting command (13 = 3 tools + 10 rounds-40–43 instruments; 395 over all tracked `.py`/`.sh`).
- **Tool installs:** none.

## Landed changes

Each tied to the `LOG.md` "Round 48" entry (`LOG.md:2689-2722`):

- `4387cf94` — freeze.
- `e4dfff32` — data: tool v3, unlanded check, quota entry, rows S479–S484, QUALITY 125–128, lesson, README/SKILL/SCORECARD/LOG, w1 evidence.
- `91fbbc2a` — wave 2 settled: results, entry overclaim reworded, errata, SCORECARD outcome, SHONEN, lesson wave-2 findings.
- `14c5110d` — end receipts (C2 final, census end, append-only gate).

## Before → after measurements

- **C1.** Command: `python3 .ufo/waves/round-48/count-c1.py --tool tools/mori-pin-check.py --rev R`, flags `--min-tally-pins 26 --baseline-rev 2d85e33d…`.
  - Before (entering tool, measured against `e5dbac05`): `C1=unmet junk_met=8 honest_unmet=0 real=met errors=0 variants=12`, rc 1 (`evidence/control-c1-tool-v2-entering.txt`).
  - After at `e4dfff32` (tool bytes identical at the final tip, `git diff` empty): `C1=met junk_met=0 honest_unmet=0 real=met errors=0 variants=12`, rc 0 (`evidence/after-c1-at-e4dfff32.txt`; re-run `w2/R48ExecRerunC1.md`; replay in a clone at another path `w2/R48ExecRerunC1Clone.md`).
  - **Verdict: verified (proposed) on the frozen counter, with limits.** The frozen counter is also met by a tool that sniffs the harness's variant filename (`w1/CritC1Counter.md` F1, `w2/R48CritFreeze.md`); the landed tool holds no such branch (`w2/R48RevHarnessLeak.md`). The landed v3 still scores `met` on seven of fourteen new junk probes (`w2/R48CritV3Junk1.md`) and on seven further command-binding classes (`w2/R48CritV3Junk2.md`): the claim is about the frozen eight, not the class of all junk. Selftest mutation seats found arm gaps (`R48MutV3Header` 3/6, `R48MutV3Bind` 2/8, `R48MutV3Hidden` 6/12 survivors).
- **C2.** Command: `python3 .ufo/waves/round-48/count-c2.py R`.
  - Before (`e5dbac05`): `C2=unmet claims=0 … failed=entry_absent,pins`, rc 1.
  - After at `91fbbc2a` (final entry bytes): `C2=met claims=15 located=15 quote_missing=0 bad_rows=0 sources=4 source_rows=ok pins=ok provenance=ok`, rc 0 (`evidence/after-c2-final.txt`; re-runs `w2/R48ExecRerunC2.md`).
  - **Verdict: verified (proposed).** Limits: a located quote proves location, not entailment, and script/JSON text also passes (`w1/CritC2Counter.md`); no quote of the 15 sits in script text (`w2/R48RevC2Counter.md`). Reviewers HOLD 14 of 15 rows; the 15th was reworded and re-measured.
- **No harm across axes:** `w2/R48RevSkillScore.md` found the Axes table unchanged; no score change is claimed.

## Sources & frontier

- **Registry rows: 251 → 257.** Command: `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'` at `e5dbac05` and `91fbbc2a`.
- **Tier counts:** A 220 → 226, B 14, C 17. **Status:** mined 201 → 207. **Added:** S479, S480 (docs A), S481, S483, S484 (code A), S482 (docs A, scope-limited); all `mined`, opened 2026-10-25.
- **Touched old→new:** none (S478's recheck stays `180d`; its browser-User-Agent re-open note is in the Gate).
- **Frontier:** FR2 advanced (user-space reporting and error surface documented); a live per-id probe stays frontier; this host's quota state is unread, no quota command was run.
- **Census:** start `mori ok`, rc 0, 19 W04 warnings (`evidence/census-start.txt`); end `mori ok`, rc 0 (`evidence/census-end.txt`). Append-only gate: `round_changed=[]` (`evidence/after-appendonly.txt`).
- **Assimilation:** theme FR2. Collisions: 8 (S471–S478), guard proven on an indented fixture; renumber map by document: staged S477 → S479, S478 → S480, S482 → S481, S479 → S482. Admit: staged `quota-observability-r38` (rewritten). Reject with flip: `quota-id-mapping-files-r41` (12-cell rows, dangling references), `quota-path-listing-r42`, `quota-counter-freshness-r39`, `quota-id-to-path-r40`, `alarm-latency-model-r39`, Solaris `errno=49`, the RHEL 9 PDF (unreachable at the freeze). Quarantine slice S244, S262, S268: all PRESENT, none appended. `MERGE-REPORT.md`'s Adopt checklist conflicts with §10; §10 was followed.
- **considerthese:** suggestion 2 of `considerthese/2026-10-25.md` → QUALITY 127.

## Trend verdicts

- **expansion: improved.** One admitted entry on FR2 ground the lane did not hold, citing mined S479–S484 (`corpus/README.md` Round-48 block; `w2/R48ScribeTrends.md`).
- **quality: unchanged.** The stale r14 pin was repaired and live re-fetch confirmed the six sources (`w2/R48ExecLiveRefetch.md`), but no earlier entry was re-verified or superseded; one entry row was corrected before the final measurement.
- **discernment: unchanged, pending the non-author spot-check.** QUALITY 125–128 are lesson-backed (`R48RevQuality` HOLDS); the gate's own errors (M7, "four rows") were caught by wave-2 reviewers and corrected as errata.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:941-980`; `corpus/QUALITY.md:1050-1087`
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:2689-2722`
- [~] Instructions executable by an agent without oral context — `python3 tools/mori-pin-check.py --selftest` (60/60); `python3 tools/mori-unlanded-check.py --selftest` (13/13)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-16` unchanged; `w2/R48ConnSiblings.md` (no contested scope)

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Open L0 questions: none.

Routed to round 49: the seven v3 survivors of `R48CritV3Junk1` and the K2–K8 classes of `R48CritV3Junk2`; rule R11 for D7 (`R48ExecD7`); the selftest arms the mutation seats named; a successor C1 counter that hides the variant identity from the tool and adds an honest edit that updates a pin; unique seat names in wave 1 (lesson M6).
