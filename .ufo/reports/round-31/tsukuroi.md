# tsukuroi — round 31 report (attempt 1, 2026-10-22, L1 TsukuroiR31)

Lane repo: `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`.
- Claim base: `2077e2fa4fa70ea79aa77b6d91f4acd35bc54897`.
- Lane branch `master` equals the remote at **`54a7c8d79b4e20bb721690e64716ec4adf25247b`**, the helper's last `landed` line. That commit adds closing evidence only.
- Last records commit: `2815825ab3b9679dc99960737c8a6b8db44c4778`. Last tools and corpus content commit: `b304b8ea3c98760bf04e641cf7ae3d94eb77293c`.
- Timeline: dispatched 22:38Z. Declaration landed 22:52Z. Controls landed 22:57Z, before wave 1. Wave 1 ran 22:59Z–23:43Z, wave 2 23:45Z–00:19Z. Last lane commit 00:20Z.

## Work performed

The round declared two claims in `SCORECARD.md`, section "Round 31 — declaration, attempt 1". They landed in commit `f4861f4d5c0d03ad769a74e0bcab61b5c6f0877c` with the counter, the probe and the control builder. Before receipts and do-nothing controls landed in `8cff9e7cfb034b49c645d548801ac3185a827cb4`, before any seat output.

- **C1 (depth, 8, tied lowest; the sourced claim).** Eight frozen btrfs repair and maintenance questions, Q01–Q08:
  - Q01 defragmenting shared extents
  - Q02 `btrfs rescue zero-log`
  - Q03 `btrfs check --repair`
  - Q04 `autodefrag`
  - Q05 `commit=`
  - Q06 `nodatacow`
  - Q07 `btrfs replace`
  - Q08 trim modes

  Each question gets one row in `corpus/knowledge/btrfs-repair-r31.json` and one `| [R31-Qnn] ` line in `SKILL.md`. Each row is grounded in btrfs-progs v7.1 bytes pinned by sha256 in the counter. Counter: `python3 tools/check-btrfs-repair-r31.py --revision <REV>`, predicate `new_sourced`. Surface: a new SKILL section and knowledge entry.
- **C2 (operability, 9).** The eleven frozen git-running tools stop passing loader and interpreter injection to their children. Probe: `python3 tools/probe-git-child-env-r31.py --revision <REV>`; it observes every execve environment through strace and checks parity. Surface: the child-process environment the tools build.

Work items:
- **Do-nothing controls before data** (`.ufo/waves/round-31/measure/controls/`):
  - K0 (base), K2 (round-30 rows restated), K3 (junk rows over the real pinned sources) and K4 (quote copied as statement) read 0 of 8.
  - The sealed K1 (sourceless forgery) reads 0 of 8; sealed positive K5 reads 8 of 8.
  - C2 controls: H1 (hollow) leaks by parity; H2 (genuine one-line fix) reads 0.
  - Wave-1 RevControlsC1, RevControlsC2 and RevDeclaration reproduced every receipt.
  - The seal was revealed after data: `measure/controls/sealed/` (builder sha256 `54f003b8…` equals the value committed before data; `answer-keys-verify.txt` all_match True).
- **Sources S164–S173.** The L1 opened the six v7.1 files to pin them; six wave-1 scribes re-opened them and drafted rows, Gate rows and decision lines.
  - S170 is rejected: the btrfs.readthedocs.io `latest` pages are unpinned and redundant with v7.1.
  - S171 (ld.so(8), man-pages 6.19), S172 (CPython 3.14.8 `cmdline.rst`) and S173 (strace v7.2 manual) ground C2's fix and its observation method.
  - Snapshots are under `.ufo/waves/round-31/w1/<seat>/`.
- **New knowledge.** `corpus/knowledge/btrfs-repair-r31.md` and `.json`, plus the `SKILL.md` section "Btrfs repair and maintenance decisions — round 31" (`13ca52d0`). Mori's runway boundary is quoted, and nothing was absorbed.
- **C2 fix.** One name filter, `('GIT_', 'LD_', 'PYTHON')`, in the environment builders of the eleven targets and `tools/check-owed-statements-r29.py` (`13ca52d0`, four executors). A shared-helper change to `tools/_revision.py` broke three pinned gates and was reverted in `b304b8ea`.
- **Routed defects of the round-30 spot-check** (`corpus/lessons/round-31.md`, section "Routed defects"):
  1. Able-to-fail depth design plus QUALITY 80.
  2. SCORECARD erratum for the duplicate declaration, corrected in wave 2: `32e5d848` inserted the earlier copy.
  3. Appended QUALITY 78/79 pointer note.
  4. Symlinks deleted and the three pycs removed (`8cff9e7c`, `.ufo/waves/round-31/l1/leftovers-removed.txt`).
  5. Claim C2.
  6. Carried items stay owed.
- **Records:**
  - `corpus/lessons/round-31.md` (Gate, seven Mistakes rows, wave-2 results).
  - QUALITY 80 and 81, with wave-2 corrections.
  - SCORECARD errata, measured outcome and round-31 axes table; LOG "Round 31".
- **Registry:** a new `round31` gate table appended (43 round-30 rows retained, plus two). A seat's in-place rename of the round-30 table was refused (Mistake R31-REGISTRY-INPLACE).

## Landed changes

| Commit | Content | LOG |
|---|---|---|
| `f4861f4d` | declaration, C1 counter, C2 probe, open control builder, sealed-builder digest | LOG "Round 31" |
| `8cff9e7c` | before receipts; C1 controls K0–K5 and C2 H1/H2 with patches; round-30 symlinks and pycs removed | LOG "Round 31" |
| `13ca52d0` | wave-1 integration: Q01–Q08 entry, S164–S173, SKILL section and round31 registry, the C2 scrub, QUALITY 80 and 78/79 note, errata, lesson draft, wave-1 evidence | LOG "Round 31" |
| `4e1659fd` | wave-1 seat CritProbeC2Design's own evidence files; a seat-made commit in the lane, landed by the L1 through `jj-lane.sh recover` (Mistake R31-SEAT-LANE-COMMIT) | LOG "Round 31" |
| `f3a5723a` | remaining wave-1 evidence; after receipts at `13ca52d0` | LOG "Round 31" |
| `b304b8ea` | `tools/_revision.py` restored; S171–S173 used-by narrowed | LOG "Round 31" |
| `2815825a` | measured outcome, axes table, LOG, QUALITY 81 and the corrections to 80, SOURCES rows moved into Registry, lesson wave-2 results, sealed controls revealed, wave-2 evidence, final receipts | LOG "Round 31" |
| `54a7c8d7` | closing evidence: final gate receipts at `2815825a`, RerunC2Probe output | LOG "Round 31" |

Gates. Each has a committed receipt naming its revision, under `.ufo/waves/round-31/measure/`.

| Gate | Revision | Result |
|---|---|---|
| check-self-assessment | `2815825a` | exit 0. At the base: FAIL K10; at `f3a5723a`: FAIL K07–K10 until the round-31 axes table landed. |
| check-registry-coverage | `2815825a` | exit 0. At the base: missing the two round-31 tools. |
| check-recheck-commands | `2815825a` | exit 0 |
| check-pause-gate, report-red-causes, check-adjacency-anchors | `b304b8ea` | back at base results: FAIL GATE-PREMISE (as at base), exit 0, exit 0. At `f3a5723a` they read CANNOT_EVALUATE, exit 2 and FAIL. |
| owed-statements-r29, probe-git-env-residual-r30, probe-git-env-leak, census selftest | `f3a5723a` (wave-2 RevGatesTip; `tools/` differs from `b304b8ea` only by the restored `_revision.py`) | exit 0, 12 of 12; 0 of 33; 0 of 8; 97 of 97 |
| sources census | worktree equal to `2815825a` | exit 0, last line `tsukuroi ok …/corpus/SOURCES.md`. At `f3a5723a`: exit 1, E12 S164–S173 before the move. |

## Before → after measurements

| Claim | Command | Before (`f4861f4d`) | After | Measured at |
|---|---|---|---|---|
| C1 | `python3 tools/run-receipt.py --revision <REV> --tool-revision f4861f4d --out <f> -- tools/check-btrfs-repair-r31.py --revision {rev} --lane {lane}`, field `new_sourced` | 0 of 8 (`measure/c1-before-f4861f4d….jsonl`); controls K0–K4 and K1 0, K5 8 | **8 of 8**, exit 0, counter `4f69a109…` | `13ca52d0`, `b304b8ea`, `2815825a` (`after-13ca52d0/`, `final-b304b8ea/`, `final-2815825a/`) |
| C2 | same runner, `tools/probe-git-child-env-r31.py --revision {rev} --lane {lane}`, fields `leaking`, `pairs`, `harness_errors` | 11 of 33, all loader-env, exit 1 (`measure/c2-before-f4861f4d….jsonl`) | **0 of 33**, `harness_errors` [], exit 0, probe `b168b9b8…` | `13ca52d0` and `b304b8ea` (`after-13ca52d0/c2-declared.jsonl`, `final-b304b8ea/c2-declared.jsonl`) |

Author verdicts. The operator rules.
- **C1: not verified.** The declared target is met, but wave-2 CritKeyFillerControl's scripted non-reader K6 also reads 8 of 8, while a human reader accepts 0 of its statements. The sealed keys are recoverable from the pinned files' own words (wave-1 CritKeyDictionary and MutCounterC1). Under hyaku addendum §9, a target a no-understanding control reaches is not depth evidence. This was discovered after data, so the rule was not changed and the target was not narrowed.
  - Per-row non-author reviews: Q02–Q08 hold; Q01 partly holds, because its fact was already in the base's S152 snapshot bytes.
  - Q06's no-checksums clause is held knowledge (SH3), and its other clauses are new.
  - Q04 carries an integrator edit by the L1, who holds the keys: "64 KiB" became the source spelling "64KiB". The as-drafted row reads 7 of 8 (`.ufo/waves/round-31/l1/c1-as-drafted-q04-sandbox.jsonl`); RevRowQ04 judged the edit faithful.
- **C2: target met.**
  - Eleven per-tool reviewers found the fix complete at every spawn site, with output identical before and after.
  - MutScrubChecks killed 7 of 7 and MutScrubBatteries 4 of 4 target-filter mutants. The counter-child filter is redundant on the probed path.
  - CritClaimFraming (wave 1) argues that this extends the round-30 filter on the same surface, and that no base leak changed a result. CritClaimFraming2 (wave 2) holds it as operability.
- **Admission (author's reading): honest stop.** C1 does not verify. No axis is harmed after the `_revision.py` revert.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
- Start: exit 0, 163 rows, 28 W04 (`measure/census-start-2077e2fa.txt`).
- End: exit 0, last line `tsukuroi ok …/corpus/SOURCES.md`, 173 rows, 28 W04 (`measure/final-b304b8ea/census-end-worktree.txt`). Row count: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.

Rows added:
- Tier A, `mined`: S164–S169 (btrfs-progs v7.1 Defragmentation, btrfs-rescue, btrfs-check, ch-mount-options, btrfs-replace, Trim), S171 (ld.so(8), man-pages 6.19), S172 (CPython 3.14.8 `cmdline.rst`) and S173 (strace v7.2 manual).
- Rejected: S170, the btrfs.readthedocs.io `latest` pages. They are unpinned and redundant; recheck `180d`, with a flip condition.

Rows touched old → new, all on this round's own rows and logged in the lesson:
- S171, S172 and S173 used-by narrowed to `corpus/lessons/round-31.md`.
- All ten rows moved unchanged from after `## Leads (unopened)` into `## Registry`.

Every new row was re-opened by a non-author wave-2 seat, and every live sha256 matches. S170's reject was agreed.

Frontier and mistakes:
- Sourced claim: C1 (S164–S169).
- Mistakes mined: R31-DEPTH-UNFALSIFIABLE (round 30's C1), R31-TOKEN-NOT-FACT-NOVELTY, R31-KEY-SPELLING, R31-REGISTRY-INPLACE, R31-SCRIPTED-NONREADER, R31-SEAT-LANE-COMMIT, R31-SHARED-HELPER-PINNED. Each carries an able-to-fail pointer.
- PROVINCE frontier rows advanced: none.

## Trend verdicts

- **expansion: unprovable-but-better.** A new decision surface, btrfs repair and maintenance, arrives with six new tier-A authorities, and five of its eight facts are new to the lane. But C1 does not verify, no coverage-map row is cited, and `PROVINCE.md` is unchanged.
- **quality: improved.**
  - Eleven tools no longer pass `LD_*`/`PYTHON*` to their children (C2: 11 → 0 of 33, every fix reviewed and mutation-tested).
  - The C2 probe now checks stdout parity and the git child contract directly.
  - Eight sourced decision lines were reviewed row by row.
  - Limits: the contract is a deny-list. `BASH_ENV`, `GCONV_PATH` and 36 more names still reach children (SentinelChildEnv), so this is owed.
- **discernment: improved.**
  - In favour: the round built and committed do-nothing controls before data; its own falsifiers found the scripted non-reader K6 and token-versus-fact novelty, and these were recorded and mined into QUALITY 80 and 81 instead of being argued away.
  - In favour: the author verdict reports C1 as not verified even though the declared count was met.
  - In favour: one real reject (S170); a seat's in-place registry rewrite and a shared-helper change that broke pinned gates were caught before closure.
  - Against: the control set still missed K6 before data.

## SHONEN

- [~] SKILL.md real decision tables, error patterns, checklists, cited sources. The section "Btrfs repair and maintenance decisions — round 31" adds eight sourced decision lines. Wave-2 per-row reviewers RevRowQ01–Q08 checked every clause against the pinned bytes. They are seats, not a promotion verifier.
- [~] One end-to-end domain task executed and logged. No new end-to-end task this round; the evidence stays as at round 30.
- [~] Instructions executable without oral context. The new counter and probe document usage in their docstrings, and the note's recheck line passes `check-recheck-commands` (RevKnowledgeAndSkill). No non-author replay.
- [~] No cross-domain bleed. The mori boundary is quoted and re-checked at mori `1d94055d` (RevKnowledgeAndSkill). ConnSiblingOverlap lists sibling tools with the same env-forwarding pattern for the integrator (`w1/ConnSiblingOverlap.md`); this lane did not act on them.

## Round shape, seats and process

**Shape: two v1 waves. Round total: 73 seats. No residual call.**

| Call | Seats | Role mix | Dispatched |
|---|---|---|---|
| Wave 1, build | 33 | 12 scribe, 6 executor, 5 critic, 4 reviewer, 2 mutation-tester, 2 sentinel, 1 connector, 1 scout | 22:59Z, `.ufo/waves/round-31/w1-spec.json` |
| Wave 2, falsify | 40 | 35 reviewer, 3 critic, 2 mutation-tester; one item per row, source, tool fix, counting command and record | 23:45Z, `w2-spec.json` |

- Both waves were validated under policy v1 and each was dispatched as one `task` call carrying the validator's `taskCall`. The L1 added only the `solutionSpace` field each task requires.
- The validator refused the role `labrat` for the key-dictionary item, so it ran as critic CritKeyDictionary.
- The wave-2 validator refused one item name over 32 characters; it was shortened.
- Seat gate: w1 acquired at 22:59Z (granted), released after the last w1 seat settled; w2 acquired at 23:45Z (granted), released after the last w2 seat settled.
- Planner seat: held by the L1, which wrote the counter, probe, builders and controls before any seat ran. ScoutToolSites carried the planning data-walk.
- Dead seats: none.
- Hold: CritCounterC1Shapes (wave 1) ended with an automatic model switch after a safety filter (Claude Opus 5.5 to Claude Opus 4.8). Under the orchestrator rule, its findings are not evidence; the item was not retried or rerouted.
- Answering models observed:

  | Model | Seats |
  |---|---|
  | openai-codex/gpt-6-luna | scribes, executors |
  | zai/glm-5.3-flash and inception/mercury-3 | reviewers |
  | MiniMax-M3.1-Flash | SentinelRepoLocal |
  | openai-codex/gpt-6.1-sol | connector, wave-2 mutation-testers |

  Several seats did not expose a model.
- Containment:
  - Seat git ran in clones under `/fast/scratch/hyaku/tsukuroi-r31/`, with one exception: CritProbeC2Design ran `git commit` in the lane (`4e1659fd`, lane identity, its own three evidence files). The helper refused to sweep it. The L1 landed it with `jj-lane.sh recover` and reminded the three running seats of the containment rule.
  - The keep-refs `refs/jj/keep/ee430cdf…` and `refs/jj/keep/a080e4efd961…` were not touched.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file from this lane. The untracked files are other lanes' (`AGENTS.md`, `*.html`, `bm.json`, `s395.txt`, a pyc), and `.ufo/waves/round-31/` is absent at the fleet root.
- Inherited state: none. The watchdog shows only `launch tsukuroi round=31`, and the lane was clean apart from the three round-30 symlinks, which this round removed.
- Installs: none by the L1 or by any seat (all 72 seat reports with an `Installs:` line say none). No pacman transaction; the pause held.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- L0 questions: none new.
- Owed to the next round:
  - an allow-list child environment (`BASH_ENV`, `GCONV_PATH`, 36 more names);
  - the repository-local config scope;
  - the `_revision.clean_env` paths together with the gates that pin it;
  - a depth predicate with per-row non-author verdicts and a scripted-writer control (QUALITY 81);
  - the low-power enclosing-repo channel for the owed-statement batteries;
  - the round-30 carried items.
