# mori — round 34 (attempt 3, L1 MoriR34A3)

Lane tip `3a7a89eadd83296fdc8fea5b4e9186f2c957a58f` (entering `f10a320d`). Attempts 1 (MoriR34, died 05:25:25Z) and 2
(MoriR34A2, died 06:19:06Z, omp SIGSEGV) died with the orchestrator (`.ufo/watchdog.log:847,867`). Their commits
`24603186`..`fd252135` are part of this round. Their uncommitted files were treated as untrusted: they were re-derived
by attempt-3 seats or moved out of the lane. Round shape: default v1. Attempt 3 ran one validated 41-seat wave (wave B)
and a 3-seat residual call.

## Work performed

Declared claims (2, frozen before any seat at `24603186`; Amendment A1 before data at `b9fb029e`):
**C1 — coverage (6)**: FR6's two-sample write-rate arm becomes the lane tool operation `tools/mori-disk-rate.py`,
judged by P-C1-A1. **C2 — calibration (5, tied lowest), exploratory**: QUALITY 98, the pre-data shortcut battery.
Sourced claim: C1's rules rest on S191–S193 (and S180–S187). These rows were opened this round and re-opened live in
attempt 3. Routed round-33 defects 2–8 are repairs, not claims.

- Repair first (round-33 spot-check §8): the attempt-3 judges re-judged every routed item, each from the bytes before
  auditing the attempt-2 judge. Results:
  - Rows 6r, 7r and 13r are supported.
  - **Row 3r is unsupported**: four facts are not stated by its cited lines (`wb/ReJudgeRow3r.md`). Row 3r2 was
    appended at `5c3e2dde` and is supported (`wb/residual/MoriR34A3.JudgeRow3r2.md`).
  - Row 8 correction: 8/8 sentences supported.
  - SKILL :820 correction: supported.
  - Lesson Items 5 and 6: repaired. Items 7 and 8 each carry one wrong detail, now corrected in
    `corpus/lessons/round-34.md` (M4).
- C1 measured (L1): `count-c1-a1.py` at the tip gives `C1=met` (`evidence/c1-tip-a3.txt`, 06:47:48Z); ExecCloneRerun
  got 4/4 `C1=met`. Post-data probe `ef936fb4` skips the two-sample read and rule R3, and also gives `C1=met` (L1
  re-score `evidence/ctl-postdata-shortcut/rescore-a3.txt`, 06:48:06Z; `wb/CritShortcutRescore.md`). CritQ99Gap built
  two more skip programs that meet it. **C1 is not verified (honest stop, §9).** Counter, rules and target are unchanged.
- C2: named non-author reviewer **ReviewC2Judge3** gives `unprovable-but-better` (`wb/ReviewC2Judge3.md`):
  - 98 fails round 33's contract and passes round 34's.
  - It forced the pre-data A1 re-design.
  - Against it: §8 item 1's second clause is unanswered, plus defects D1, D2 and D4.
- Sources: the L1 re-fetched S191–S198 and S182 live at 06:48Z; all match their committed copies
  (`evidence/sources-refetch-a3.txt`). One reviewer per row re-opened it and judged it (`wb/GateS191.md`…`GateS198.md`,
  `GateS182Anchor.md`). 7 rows admitted; **S193's teaches cell rejected** (a reparent path removes and creates the link
  with no partition check). The cell was rescoped at `406d91a4` and re-admitted (`wb/residual/ReGateS193.md`).
- Census conformance: the registry committed at `8d56809a` fails the census with nine `E11` lines (ExecCensusE11).
  Fixed at `ff334073`: `mori ok`, exit 0.
- QUALITY 99 (mistake M2) landed at `7161a738`:
  - It was revised after MutQ99 (two variants of the first draft survived) and after ReviewQ99 (admit with fixes).
  - CritQ99Revised's fixes were applied after its review and were not re-judged.
- FR6 frontier note landed at `699090c1`:
  - Wall time re-measured (`wb/ExecLatencyRemeasure.md`).
  - A dm-0 write appears three times in a sum over every line, not twice (`wb/ExecStackedRemeasure.md`).
- Mistakes M1–M7 mined in `corpus/lessons/round-34.md` `## Mistakes`. M3 was re-derived with eight mutants
  (`wb/ExecM3Mutants.md`). M5 was corrected (`wb/CritM5Audit.md`). M7 is new: attempt 2 left its integration
  uncommitted.

## Landed changes

| Commit | LOG entry | What |
|---|---|---|
| `24603186` | `LOG.md` Round 34 | freeze: contract, `count-c1.py`, before receipt, census start (attempt 1) |
| `b9fb029e` | same | C0 control receipts, Amendment A1 (attempt 1, pre-data) |
| `ba525e1a` | same | C1 tool and provenance receipt (attempt 2) |
| `8d56809a` | same | S191–S198, entry rows 3r/6r/7r/13r and row-8 correction, SKILL Round34, QUALITY 98, round-33 lesson corrections (attempt 2) |
| `fd252135` | same | wave-A spec/dispatch (attempt 2) |
| `5216d78d` | same | wave-B spec/dispatch, before dispatch |
| `ff334073` | same | SOURCES used-by cells to single paths (census E11 fix) |
| `406d91a4` | same | S193 teaches cell scoped (gate reject → re-admit) |
| `699090c1` | same | FR6 frontier note |
| `7161a738` | same | QUALITY 99; QUALITY 98 citation correction |
| `5c3e2dde` | same | entry row 3r2 |
| `3a7a89ea` | same | lesson, SCORECARD/LOG outcome, wave-B and residual reports, 31 audited wave-A reports, attempt-3 receipts, census end |

All lane commits went through `jj-lane.sh`. Each line above is the helper's `landed <hash>` for attempt 3. Attempts 1–2
hashes are from `git log`.

## Before → after measurements

- **C1**:
  - Command: `python3 /home/vgpnk/Projects/shokunin/mori-shokunin/.ufo/waves/round-34/count-c1-a1.py <rev>`.
  - Before, at `f10a320d`: `tool=absent C1=unmet`, exit 1 (`evidence/c1-before.txt`).
  - After, at `5216d78d` (tool and counter byte-identical at `3a7a89ea`): `fixed_pass=12/12 random_pass=300/300
    coverage=ok live=ok C1=met`, exit 0 (`evidence/c1-tip-a3.txt`).
  - Shortcut control under the same command (`ef936fb4 --repo <probe clone>`): `C1=met`, exit 0. The claim is not
    verified.
- **C2**: exploratory, no counting command. ReviewC2Judge3 gives `unprovable-but-better`.

## Sources & frontier

- Rows: `grep -c '^| S[0-9]' corpus/SOURCES.md` went from 190 → 198. Added: 8 tier A (S191–S198, `mined`).
- Rows touched old→new:
  - S182 anchor gained the `__add_disk`/`device_add_disk` lines; its used-by is unchanged net.
  - S193 anchor and teaches cell rescoped.
  - S191–S198 used-by cells set to single paths.
  - All logged in the lesson `## Gate`.
- Census: start `mori ok` exit 0 (`evidence/census-start.txt`; attempt-3 start `evidence/census-a3-start.txt`). End
  `mori ok` EXIT=0 over committed bytes (`evidence/census-a3-end.txt`, 12 W04).
- Frontier: FR6 is narrowed, not closed. The FR6 note in `corpus/README.md` says why: a census arm does not fit the 50 ms
  bar, and the dm double count is still unsourced.

## Trend verdicts

- **expansion: unprovable-but-better.** Eight new tier-A rows, each re-opened live twice. A new read-only tool
  operation exists. But its claim did not verify, because cheap skip programs meet its counter.
- **quality: improved.**
  - Unsupported repair row 3r was caught and superseded (3r2 supported).
  - S193's overclaim was rescoped.
  - The census-failing registry at `8d56809a` was fixed.
  - Frontier-note numbers were corrected by re-measurement.
  - QUALITY 99 was mutation-tested before landing.
- **discernment: improved.**
  - Real rejects at the gate (S193 cell, row 3r).
  - The judged object was never amended after the shortcut met it.
  - Every attempt-2 report the round relies on was audited, with disagreements on record.

## SHONEN

- [~] SKILL.md decision tables, error patterns, cited sources: `SKILL.md:826-842` (Round34 rules; ReJudgeSkillR34 4/4
  supported, ReJudgeSkillCorr supported).
- [~] End-to-end domain task logged: `LOG.md` Round 34. Live tool runs are in `wb/ExecStackedRemeasure.md` and
  `wb/ExecLatencyRemeasure.md`.
- [~] Instructions executable without oral context: `SKILL.md:831` (CLI and both modes), exercised by ReJudgeSkillR34.
- [~] No cross-domain bleed: `git diff f10a320d 3a7a89ea -- PROVINCE.md` is empty. The tool reads only `/proc` and
  `/sys`.

## Gate

Real rejects, each with its reason:
- S193 teaches cell: a universal "only when" is falsified by `device_move_class_links`, `S193.src:4653-4657`.
- Row 3r unsupported: four facts are not stated by its cited lines.
- The attempt-1 tool draft: `live=fed-no-interval C1=unmet`.
- Five seat-proposed quotes: not contiguous, under 3 words, or contain `"`.

## Round mechanics

| Attempt | Waves | Seats | Dead seats / no report |
|---|---|---|---|
| 1 | C0 + wave 1 | 10 + 35 | 5 (ExecDiskRateTool, ReviewRuleR3, ReviewRuleR5, ReviewRuleR7, CriticC1AxisFit) |
| 2 | wave A | 52 | 1 (LabScaleHost) |
| 3 | wave B + residual | 41 + 3 = 44 | none (all returned) |

- **Total**: 141 seats over three attempts, against the 128 band. The excess comes from re-deriving the dead attempts'
  uncommitted work; attempt 3 alone ran 44 seats.
- **Wave B roles**: 27 reviewer, 5 executor, 3 critic, 2 mutation-tester, 1 connector, 1 scout, 1 scribe, 1 sentinel.
- **Residual roles**: 2 reviewer, 1 critic.
- **Planner**: the L1 holds the planner seat.
- **Wave-B dispatch**:
  - The 41-seat gate acquire waited 52 min and was terminated at 07:38:48Z without a grant.
  - The validated tasks were then sent unchanged in four chunks of ≤12 under Main's ruling (`wb-dispatch-log.txt`).
- **Containment**:
  - AuditM3Reports briefly edited the lane tool and reverted it; the tool sha256 `370932de…` was verified unchanged
    after the wave.
  - No misroot: the fleet-root untracked files do not name mori or round 34.
- **Untrusted files moved out of the lane**: attempt 1 `w1/` and `wave1-*`; attempt 2's unaudited `wa/` reports,
  `c1-after.txt` and `census-end.txt`. They are in `/fast/scratch/hyaku/mori-r34/a3-L1/removed-untrusted/`.
- **Privacy**: SentinelPrivacy found an OMP setting value at `LOG.md:1801`, committed in an earlier round. It is left
  for the operator.
- **Tool installs**: hyperfine 2.0.0, official GitHub release binary into `~/.local/bin`, by seat ExecLatencyRemeasure
  (`/usr/bin/time` was absent). No pacman.
- **Stale-lane**: respawn-per-round driver; no other mission of this lane is open.
- **L0 questions**: none.
