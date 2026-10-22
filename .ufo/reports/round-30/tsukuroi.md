# tsukuroi — round 30 report (attempt 1, 2026-10-22, L1 TsukuroiR30)

Lane repo: `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin`.
- Claim base: `fbfec6bdf8833e7513732a06000801a8ee9b690b`.
- Lane branch `master` equals the remote at **`5bbd184185f77bba3e2f2eff1239348aa8ad0f18`**. This is the helper's last `landed` line; that commit adds the final-tip receipts only.
- Last content commit: `a26057cf4a39d743fd0fa287d6a9f8828552ef2d`.
- Timeline: dispatched 20:57Z, declaration landed 21:06Z, last lane commit 22:15Z.

## Work performed

The round declared two claims in `SCORECARD.md` section "Round 30 — declaration, attempt 1". They landed in `8fb2cef081787ccb52b38e9f74d95d2a480de18f` together with both counting tools and the C1 battery, before any counted run.

- **C1 (depth, 8, tied lowest; the sourced claim).** Ten frozen btrfs space questions, D01–D10, each answered by one row of `corpus/knowledge/btrfs-space-r30.json`.
  - Each row quotes a `mined` source opened this round, at a cited snapshot line.
  - Each row has one `| [R30-Dnn] ` decision-table line in `SKILL.md`.
  - The rows cover unallocated space and ENOSPC, the global reserve, balance usage filters, metadata DUP, block-group reclaim, the allocation sysfs directory, snapshot extent sharing, and three host readings.
  - Counter: `python3 tools/check-btrfs-space-r30.py --revision <REV>` → `verified`.
- **C2 (operability, 9).** Eleven frozen git-writing lane tools stop following the three residual git channels from round-29 routed defect 4: a PATH `git` wrapper, per-user git files under HOME/XDG_CONFIG_HOME, and an enclosing repository.
  - The measure is 33 (tool, channel) pairs.
  - Probe: `python3 tools/probe-git-env-residual-r30.py --revision <REV>` → `leaking`, `pairs`, `harness_errors`.

Work items:
- **Sources S152–S163** were opened by 12 wave-1 scribes. Ten are `mined`; two are rejected: S160, the archived btrfs wiki FAQ, and S161, the ArchWiki page. Snapshots are under `.ufo/waves/round-30/w1/<seat>/`.
- **Host capture.** A read-only, unprivileged capture of `/sys/fs/btrfs/<fsid>/allocation` is at `.ufo/waves/round-30/w1/ExecHostCapture/btrfs-allocation-capture.txt`:
  - metadata 91.5 percent full;
  - unallocated 690922455040 bytes;
  - global reserve 536870912 bytes, at the 512 MiB cap.
- **New knowledge entry and SKILL section.** `corpus/knowledge/btrfs-space-r30.md` and `.json`, plus the `SKILL.md` section "Btrfs space allocation and ENOSPC — round 30" (`a3f19372`, corrected through `a26057cf`). Mori's disk-runway boundary is recorded; nothing was absorbed.
- **GIT child environment contract** applied to all eleven tools (`a3f19372`). The contract is sourced from S162 and S163. `check-self-assessment.py --selftest` now runs before its repository check, which cleared the before harness error.
- **Counter v2 and battery v2** (`a3f19372`), after wave-1 attacks. The claim is still judged on the declared counter v1.
- **Receipt runner** `tools/run-receipt.py` (`8976ca92`, fixed in `a3f19372` and `32e5d848`):
  - runs tools from a sandbox clone;
  - writes a header naming the revision, the tool revision, the tool digest and the lane branch tips.
- **Report checker** `tools/check-report-receipts.py` (`29bf87fa`, repaired in `32e5d848`): the fix for the mined mistake.
- **Routed defects from the round-29 spot-check**, all recorded in `corpus/lessons/round-30.md`:
  1. Receipts: v4 batteries and the declared counter `5b6cf227…` at `8976ca92` (`w1/ExecReceiptsR29/`). Every gate row below cites a committed receipt.
  2. v4 reopenings were reproduced by RevV4Regression. `<!-->` was never reopened, and the asterisk id is a v3-era leak. Counter v5 and a v4-shapes battery landed in `85712671`: v4 accepts 11 of 11 shapes, v5 refuses 11 of 11 with 0 of 19 controls refused.
  3. Padding shapes landed in `7165f11e`: 53 of 53 refused, 19 of 19 variants accepted, live score 6 of 6.
  4. Claim C2.
  5. Depth framing: only O01–O04 of round 29 are depth.
  6. Sandbox mutant receipts are committed (`w1/MutReceiptsR29/`).
- **QUALITY 77–79**; lesson `corpus/lessons/round-30.md` with five Mistakes rows; LOG "Round 30"; SCORECARD measured outcome; axes table for round 30.

## Landed changes

| Commit | Content | LOG |
|---|---|---|
| `8fb2cef0` | declaration, counter v1, battery v1, residual probe, census start | LOG "Round 30" |
| `8976ca92` | before receipts; `tools/run-receipt.py` | LOG "Round 30" |
| `a3f19372` | wave-1 integration: knowledge entry, S152–S163, SKILL section and round30 registry, contract in 11 tools, counter v2 and battery v2, runner fixes, QUALITY 77–79, wave-1 evidence | LOG "Round 30" |
| `29bf87fa` | `tools/check-report-receipts.py`, registry rows, receipts at `a3f19372` | LOG "Round 30" |
| `7165f11e` | padding repair, lesson draft, w2 spec | LOG "Round 30" |
| `85712671` | owed-statements counter v5 and v4-shapes battery | LOG "Round 30" |
| `b0cf50b9` | wave-2 corrections (depth count, re-read sources, D05, mori wording), C2 and round-29 repair receipts | LOG "Round 30" |
| `32e5d848` | wave-2 repairs, measured outcome, axes table, LOG, lesson | LOG "Round 30" |
| `a26057cf` | last row and source corrections, QUALITY 79 pin, wave-2 evidence | LOG "Round 30" |
| `5bbd1841` | final-tip receipts | LOG "Round 30" |

Gates, each with a committed receipt naming its revision. Receipts are in `.ufo/waves/round-30/measure/final/` (at `32e5d848`) and `measure/final-a26057cf/`. `tools/` is byte-identical between the two revisions (`git diff --stat 32e5d848 a26057cf -- tools/` is empty).

| Gate | Revision | Result |
|---|---|---|
| check-self-assessment | `a26057cf` | exit 0 (FAIL at the base: K10) |
| check-registry-coverage | `a26057cf` | exit 0, 43 of 43 |
| check-recheck-commands | `a26057cf` | exit 0 |
| memory-pressure, storage-health, kernel-taint, adjacency-overlap, freshness-r17 | `32e5d848` | all exit 0 |
| owed-statements-r29 (v5) | `32e5d848` | marked 12 of 12 |
| probe-git-env-leak (round 29) | `32e5d848` | 0 of 8 |
| census selftest | `32e5d848` | 97 of 97 |
| report-receipts selftest | `32e5d848` | 2 of 2 |
| sources census | `a26057cf` | exit 0 (`final-a26057cf/census-end.txt`) |

## Before → after measurements

| Claim | Command | Before (`8fb2cef0`) | After | Measured at |
|---|---|---|---|---|
| C1 | `python3 tools/run-receipt.py --revision <REV> --tool-revision 8fb2cef0 --out <f> -- tools/check-btrfs-space-r30.py --revision {rev} --lane {lane}` → `verified` | 0 of 10, counter v1 `1bf7ee14…` (`measure/c1-before-8fb2cef0….jsonl`) | **10 of 10**, exit 0, under the declared v1. v2 `4953203d…` also gives 10 of 10. | `a3f19372`, `32e5d848`, `a26057cf` (`measure/after-a3f19372/`, `final/`, `final-a26057cf/`) |
| C2 | same runner with `--tool-revision 8fb2cef0` on `tools/probe-git-env-residual-r30.py --revision {rev} --lane {lane}` | 17 of 30 pairs leaking plus 1 harness error, exit 2 (`measure/c2-before-8fb2cef0….jsonl`); honest before at least 19 of 33 | **0 of 33**, `harness_errors` [], exit 0, probe `c8f61996…` | `a3f19372` and `32e5d848` (tools unchanged to `a26057cf`) |

Battery v2 runs: with v2, 0 of 72 should-fail shapes accepted and 0 of 11 should-pass shapes refused; with v1, 20 of 72 accepted and 5 of 11 refused. Control is 10 in every run.

Non-author re-derivation in wave 2:
- C1: RerunC1Counters reproduced every number.
- C2: RerunC2Probe reproduced the result, and eleven per-tool reviewers held each fix with byte-identical output.
- MutScrubChannels: each fix is load-bearing per channel, except freshness-r17's HOME override, because that channel never leaked.

Disclosed limits:
- **What C1 measures.** C1's count measures provenance and format, not depth. CritClaimFraming2 got a sourceless fixture to 10 of 10.
- **New depth is 4 firm rows plus 1 thin.** D01, D02, D03 and D07 are firm new depth; D05 is thin. D04 and D06 restate round-26 facts. D08–D10 are captures.
- **Re-read sources.** S154, S155 and S158 are the same bytes as round-26 files (S155 = S130, S158 = S133). Their rows now say so.
- **Counter v2 is still porous.** It accepts 33 new shapes and refuses 9 legitimate layouts (CritCounterV2). MutCounterV2 found 4 surviving mutants. No v3 this round.
- **Probe blind spots.** The C2 probe does not compare stdout. It does not cover LD_PRELOAD, a dropped `.git` pointer, or repository-local config (SentinelGitEnv3, SentinelProbeHollow, CritProbeDesign).

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
- Start: exit 0, 151 rows, 26 W04 (`measure/census-start-fbfec6bd.txt`).
- End: exit 0, last line `tsukuroi ok …/corpus/SOURCES.md`, 163 rows, 28 W04 (`measure/final-a26057cf/census-end.txt`). The two new W04 advisories are S155 and S158, which duplicate the URLs of S130 and S133.

Rows added:
- Tier A, `mined`: S152–S159 (btrfs-progs v7.1 docs; Linux v7.2 `block-rsv.c`, `sysfs.c`, `space-info.c`), S162 and S163 (git v2.56.0 docs).
- Rejected: S160 (tier C; archived, unpinned) and S161 (tier B; redundant with tier A). Both have a flip condition.

Rows touched old → new, all on this round's own rows and logged in the lesson:
- S154, S155, S158 scope cells gain a "same bytes as round 26" sentence.
- S160, S161 teaches: `. Flip:` → `; flip:`.
- S160 reason corrected: v7.1 does document `limit`.
- S160, S161, S162, S163 used-by cells set to the files that cite them.

Every new row was re-opened by a non-author wave-2 seat. All live sha256 values match. One shared defect was found: `used-by` named `corpus/lessons/round-30.md` one commit before that file landed. It is true at the tip.

Frontier and mistakes:
- Sourced claim: C1 (S152–S159).
- Mistakes mined: R30-UNRECEIPTED-GATES, R30-DECLARATION-OVERCLAIM, R30-UNSCREENED-TARGET, R30-SEAT-MISROOT, R30-CHECKER-SELF-SATISFY. Each fix is shown able to fail; the evidence is in the lesson.
- PROVINCE frontier rows: none advanced.

## Trend verdicts

- **expansion: improved.** A new surface for the lane: btrfs space allocation and ENOSPC mechanism. It brings seven new tier-A authorities and new host readings. The runway boundary with mori is kept (CritAdjacencyMori: adjacency unchanged).
- **quality: improved.**
  - Four firm, sourced depth rows, plus a decision table checked row by row in wave 2.
  - Eleven tools closed to three residual git channels: 17 or more → 0.
  - Round-29 routed defects 1, 2, 3 and 6 closed with committed receipts.
  - The self-assessment gate moves from FAIL at the base to PASS.
  - Limits: depth ordinal 8 → 8, and the counters remain porous.
- **discernment: unchanged.**
  - In favour: two real rejects (S160, S161); the round's own overclaims corrected before closure (novelty sentence, "eight of ten new", re-read sources, D05 direction, D07 uncited advice); the battery shipped with the counter this time.
  - Against: the declaration's novelty sentence was false; the C2 target set was not screened from an export; the first receipt checker self-satisfied on seat reports.

## SHONEN

- [~] SKILL.md real decision tables, error patterns, checklists, cited sources. `SKILL.md` section "Btrfs space allocation and ENOSPC — round 30" adds a sourced decision table and error patterns. Author evidence plus wave-2 per-row reviewers (RevRowD01–D10); no promotion verifier.
- [~] One end-to-end domain task executed and logged. A read-only host capture plus decision reading for btrfs space (`w1/ExecHostCapture/`, `corpus/knowledge/btrfs-space-r30.md` section "Host readings"). Author evidence only.
- [~] Instructions executable without oral context. `tools/run-receipt.py` and the C1 and C2 tools document their usage in docstrings, and the recheck line in the knowledge entry passes `check-recheck-commands`. No non-author replay.
- [~] No cross-domain bleed. The mori runway boundary is stated, with no handoff claimed (CritAdjacencyMori). ConnSiblingOverlap lists sibling tools with unscrubbed git writes for the integrator (`w1/ConnSiblingOverlap.md`); this lane did not act on them.

## Round shape, seats and process

**Shape: two v1 waves. Round total: 81 seats. No residual call.**

| Call | Seats | Role mix | Dispatched |
|---|---|---|---|
| Wave 1, build | 35 | 14 scribe, 9 executor, 3 mutation-tester, 3 critic, 3 reviewer, 1 sentinel, 1 connector, 1 scout | about 21:13Z, `.ufo/waves/round-30/w1-spec.json` |
| Wave 2, falsify | 46 | 40 reviewer, 3 critic, 2 mutation-tester, 1 sentinel; one item per row, source, tool fix, counter and record | 21:37Z, `w2-spec.json` |

- Both waves were validated under policy v1 and each was dispatched as one `task` call carrying the validator's `taskCall`.
- Seat gate: acquired for each wave and released.
  - The w1 slot was released while ExecV4Shapes and ExecPaddingShapes were still running (about 15 minutes). That under-reported 2 live seats; disclosed here.
  - The w2 acquire waited about 5.7 minutes for capacity.
- Planner seat: held by the L1, which wrote the counter, battery, probe and runner before any counted run. ScoutSurface carried the planning data-walk.
- Dead seats: none; all 81 returned. Refusals: none.
- Answering models observed:

  | Model | Seats |
  |---|---|
  | opencode-go/deepseek-v4.1-flash | scribes, a sentinel |
  | openai-codex/gpt-6-luna | executors, mutation-testers |
  | zai/glm-5.3-flash and devin/swe-2 | reviewers |
  | openai-codex/gpt-6.1-sol | connector |

  Several seats did not expose a model.
- Containment:
  - All seat git ran in clones under `/fast/scratch/hyaku/tsukuroi-r30/`.
  - SentinelGitEnv3 disclosed one relative-path write into the fleet repo and repaired it itself (Mistake R30-SEAT-MISROOT).
  - L1 integration fix: the v4-shapes battery's scratch was redirected away from the fleet root.
  - The keep-refs `refs/jj/keep/ee430cdf…` and `refs/jj/keep/a080e4efd961…` were not touched.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists no untracked file from this lane. The untracked files are other lanes' (`AGENTS.md`, `*.html`, `bm.json`, `s395.txt`, a pyc), and `.ufo/waves/round-30/` is absent at the fleet root.
- Three wave-1 symlink fixtures stay uncommitted in the lane, one of them pointing outside the tree: `w1/CritCounterShapes/gitwork/G1–G3`. Their targets are listed in the CritCounterShapes report.
- Inherited state: none. The lane was clean at dispatch, and the watchdog shows only `launch tsukuroi round=30`.
- Installs: none by the L1. Seat CritCounterV2 installed `cmarkgfm` 2025.10.22 with `uv pip` into a private venv under its scratch directory, as a renderer oracle. No pacman transaction; the pause held.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- L0 questions: none new. The lowest-axis framing dispute (round-28 routed 7) stays with the operator.
- Owed to the next round:
  - counter v2 mechanical gaps (CritCounterV2);
  - stdout comparison in the probe, plus the LD_PRELOAD, `.git`-pointer and repository-local config channels;
  - `check-report-receipts.py` over-reports legacy receipts;
  - merging the S155/S130 and S158/S133 duplicate authorities;
  - `run-receipt.py` LOW findings (RevRunnerV2).
