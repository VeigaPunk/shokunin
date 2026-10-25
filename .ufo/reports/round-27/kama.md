# kama — round 27 report (attempt 3, L1 KamaR27A3)

Lane repo `/home/vgpnk/Projects/shokunin/kama-shokunin`, base `a720399e`, lane
tip `8057282c6d16f5b8471457ba15265dcae51d502a` (pushed; `jj-lane.sh state`:
`local=remote=8057282c… ahead=0 behind=0 tracked=0 untracked=0`).
Attempts 1 (KamaR27, died 05:25:25Z) and 2 (KamaR27A2, died 06:19:06Z) ended
with the orchestrator; their landed commits `530eaa99`, `6020243e`,
`a712902c`, `1471f676`, `0ec32cac` are part of this round. `.ufo/watchdog.log`
lines 843 and 863 hold the two `lane-dead-no-report kama round=27` entries.

## Work performed

Declared claims (frozen in `.ufo/waves/round-27/a3/plan.json`, landed `324d5d62`
before any attempt-3 seat):

- **C1 (measured, depth)**: the attempt-1 preregistration
  (`.ufo/waves/round-27/preregistration.json`, target `counted >= 15`).
  It was withdrawn before data and is reported as a **miss** under its
  frozen kill rule.
- **X1 (exploratory, calibration)**: the surface is the lane's
  claim-measurement method. It landed as
  `corpus/knowledge/echo-discriminating-counters.md` plus `corpus/QUALITY.md`
  KQ37 and two appended qualifications. It is sourced on S136, S137 and S139.

Work items:

- **Repair first (round-26 spot-check, `corpus/lessons/round-26-verifier-spotcheck.md:231-240`)**:
  - Defect 1: appended LOG correction entry `324d5d62`; its own errors are fixed by a second appended correction `d183ec57`. ReviewRepairD1Log and ReviewLogSecondCorrection checked them.
  - Defect 3: `.ufo/waves/round-27/repairs/d3-r26-shortcut-pins/`. Help and version sha256 equal what the pinned binary prints today (ReviewRepairD3Pins `holds`).
  - Defect 4: the raw 429 `errorMessage` lines of KamaR26CtlDoNothing, Junk and NoReader, in `repairs/d4-r26-dead-seat-errors/`. They are byte-identical to the transcript lines (ReviewRepairD4Bytes `holds`).
  - Defects 5 and 6: lesson §Repairs (ReviewRepairD5D6Notes `holds`).
  - Defect 7: S138 supersedes S133 with anchor 1810-1835 (ReviewRepairD7S138 `holds`, `sources-append-only.py` clean).
  - Defect 2: met by the frozen A3 counter and KQ37, with shortfalls recorded. The leg "one non-author receipt per class before data" is met only vacuously, because no data seat ran.
  - Defect 8 (`count-c2.py` reads receipt cells): **open**. ReviewRepairD2Status confirmed `count-c2.py:166-171`.
- **C1 disposition**:
  - The attempt-2 control wave (37 seats, 05:41:33Z, `.ufo/waves/round-27/w1-controls/`) died with no committed receipts. A dead seat's task is not resent, so C1 was withdrawn before data.
  - CriticC1Withdrawal: no data dispatch exists in `a720399e..324d5d62`, and the A3 counter and preregistration are byte-identical since `0ec32cac`. The seat also rejected my first wording "neither meets nor misses", so C1 is reported as a miss.
  - Tip receipt: `.ufo/waves/round-27/a3/c1-final.out`.
- **X1 build**:
  - Two sources opened by the L1: RFC 8259 §7 (`rfc8259.txt`, sha256 `61a5378f…2d7`) and llama.cpp `server-common.cpp:1375` @704366d76 (sha256 `b4f4aae7…d442`).
  - Knowledge entry and KQ37 landed `324d5d62`. They were revised from wave findings in `d183ec57` and `4d2e74f4`.
- **X1 evidence (wave w1a3)**, with reports under `.ufo/waves/round-27/w1a3/advice/` and receipts under `w1a3/out/`:
  - **Live probe (ExecLiveEchoProbe)**: on b11755, plain, first-character-escaped and fully escaped spellings return byte-identical 400 bodies holding the decoded value. Two values share one frame, and the control request returns 200.
  - **Offline replay (ExecOfflineEchoReplay)**: on the 12 round-26 shortcut rows, the round-26 echo test flags 0/12. A3 clause (f) as written flags 0/12 because the bodies are stored strings, the A3 shape check refuses 12/12, and A3 (f) on the decoded bodies flags 12/12.
  - **Echo mutation (MutEchoDecodedLoadBearing)**: the raw-body mutant flags 0/12 and is killed.
  - **Frame mutation (MutFrameLoadBearing)**: the frame mutant goes from 1/12 to 12/12 and is killed.
  - **Frame replay (ExecOfflineFrameReplay)**: shortcut 1/12; E26 17/17 with 0 collisions.
  - **Echo sites (ScoutEchoSitesSnapshot)**: 12 request-string frames plus 14 request-JSON dumps in the snapshot.
  - **Sibling lanes (ScoutSiblingEchoRules)**: KQ37 is lane-new.
- **Attacks that changed the landed text**:
  - CriticEntryFactsSources: the six-character escape claim is wrong outside the BMP. S139 now supersedes S136.
  - CriticKQ37Wording: boundary-shifted signatures pass the echo and frame legs 12/12. This added the boundary leg.
  - CriticEntryRuleVsCode: `lower()` is not case folding, and the frame is positional.
  - CriticEntryLimits, CriticNoveltyAtBase and CriticMistakeRow (w1a3) and CriticRevisedEntry, CriticKQ37Qualification and CriticBoundaryLegProbe (residual) found further overclaims. Every one is listed with its decision in lesson §Gate.
- **Frontier step**:
  - Census before and after (below).
  - Four new SOURCES rows.
  - Mined mistake: unbounded repeated fixture growth (ReviewA3Diff, 262 GB). The fix is shown able to fail by ExecFixtureBoundDemo: a 2 MiB cap stops at 2,097,152 bytes, while the 20 MiB arm reaches 20,971,520.
  - Three self-errors were caught in-round (lesson §Mistakes).
  - Sourced claim: X1 cites S136, S137 and S139.
- **Housekeeping**:
  - 1846 untrusted attempt-2 files were moved unread to `/fast/scratch/hyaku/kama-r27/attempt2-untracked-w1-scratch/`. ReviewUntrackedDisposal verified that none is cited.
  - Three orphan llama-server processes from attempt-2 seats (ports 47636, 47637 and 47644; cwd `/fast/scratch/hyaku/kama-r27b/CtlLogHelpWarning` and `CtlEnvPathDecoy`) were killed at 07:18Z. Ports confirmed closed.
  - Misroot sweep (`git status --porcelain` at the fleet root): no file written by a kama seat. The untracked root files are pre-round and carry no kama content.

## Landed changes

| commit (`landed` line) | LOG.md entry | content |
|---|---|---|
| `324d5d62e61276af312c8eb42f678004aec245d1` | "Correction (appended round 27) — the round-26 entry was rewritten in place" | plan, X1 entry, KQ37, S136-S138, repairs d3/d4, lesson draft, start census |
| `d183ec572a5eed5bedeb4bce0da02707d51df3dd` | "Correction … — to the correction entry above"; "Round 27 — echo-discriminating counters …" | wave w1a3 evidence, entry revision, KQ37 qualification, S139, SCORECARD/README/LOG round-27 sections |
| `52632caa2ed813c1c12f7a9dcab3556b4f0bd9eb` | Round 27 entry (C1 miss) | C1 receipt at `d183ec57` |
| `4d2e74f421bc78915301bc37da7038dba3a3a4b7` | Round 27 entry | residual evidence, entry corrections, KQ37 residual qualification, SCORECARD fix, lesson Gate |
| `8057282c6d16f5b8471457ba15265dcae51d502a` | Round 27 entry | final C1 receipt at `4d2e74f4`, final census, SOURCES append-only output |

Round-27 commits from earlier attempts, re-checked by CriticC1Withdrawal and ReviewRepairD2Status: `530eaa99` (A0 freeze), `6020243e` (A1), `a712902c` (A2), `1471f676` (A3, counter sha256 `49491b80…2765`), `0ec32cac` (attempt-2 wave record).

## Before → after measurements

- **C1** (`/usr/bin/python3 .ufo/waves/round-27/count-c1.py --out <receipt>` from a fresh clone of the lane remote):
  - base `a720399e` (`before/c1-base.out`): `registered 0 counted 0 target 15 met False`.
  - tip content commit `4d2e74f4` (`a3/c1-final.out`, exit 0): `registered 0 counted 0 target 15 met False not-counted []`.
  - `8057282c` adds only receipt files.
  - Target missed: C1 is a **miss** (honest stop, not amended, not re-scaled).
- **X1**: exploratory, with no counting command. The SCORECARD row reads `unprovable` until a named non-author reviewer rules. A dispatched subagent does not count (`AXES.md:43-51`).
- **Self-assessment check (calibration, non-author seat ReviewSelfAssessment at `52632caa`)**: 1 mismatch in 57 checkable statements, in the SCORECARD C1 measured-commit cell. Fixed in `4d2e74f4`.

## Gate

Real rejects, with reasons (full table in `corpus/lessons/round-27.md` §Gate):

- **SentinelCommittedBytesSecrets: redact `credentialId`, message ids, paths and quota values from the d4 bytes. Rejected.**
  - Defect 4 asks for raw bytes.
  - The sentinel found no credential, token, key or URL; `credentialId` is the slot index `18`.
  - Redacting would break the verified byte identity.
- **CriticEntryRuleVsCode: switch the frozen counter to `casefold()`. Rejected for this round.** The counter is frozen and C1 did not run. The gap is recorded in the entry and the KQ37 qualification.
- **ConnectorShortcutClasses: widen KQ37 into a general pre-data control rule. Rejected as KQ37 scope.** The rule already stands in prompt §9 and in seven sibling QUALITY files.
- **CriticKQ37Qualification: template-provenance spans. Rejected for this round.** It needs per-site template knowledge the lane lacks, so it is the round-28 counter design question.

Admitted findings (15 rows) changed the entry, KQ37's qualifications, S139, LOG and the lesson.

## Sources & frontier

Count command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.

| Measurement | Before | After |
|---|---|---|
| SOURCES rows | 135 at `a720399e` and at `0ec32cac` | 139 at the tip |
| Rows added by tier | — | A: 4 (S136 spec, S137 code, S138 code, S139 spec, the last superseding S136); B: 0; C: 0 |

- Rows touched old→new: none. No status, recheck or used-by change. S133 and S136 are superseded by new rows, not edited.
- Census before: `scripts/sources-census.sh validate --root <clone@0ec32cac> kama` gave exit 0, `kama ok` (`a3/census-start-0ec32cac.out`). ReviewCensusStart reproduced it.
- Census after: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` gave exit 0, `kama ok`, 50 W04 advisories (`a3/census-final.out`).
- Append-only check: `tools/sources-append-only.py --from a720399e --to 4d2e74f4` reports "no append-only violations".
- Frontier: README `## Frontier disposition — round 27` adds the method entry. K05 beyond the fixture, router-mode errors, other engines and consumer reconciliation stay open.

## Trend verdicts

- **expansion: unchanged.** There is no new coverage ground or capability. The entry is method knowledge on a surface the lane owns.
- **quality: unchanged.** C1 missed, so there is no depth move. The repairs fix round-26 defects and are not counted as a quality gain.
- **discernment: unchanged.** X1 is the round's discernment move. It stays `unprovable` until a named non-author reviewer rules. Its own seats caught and corrected four of the round's first-landed errors before filing.

## Round shape, seats and holds

- **Shape**: one v1 wave plus one residual call.
  - Wave `w1a3`: 34 seats, validated under `ufo-wave-policy.json` (`w1a3/spec.json`, `dispatch.json`), dispatched 07:07:16Z as one task call. Role mix: executor 4, mutation-tester 2, critic 9, reviewer 10, scout 5, connector 1, sentinel 1, scribe 2.
  - Residual call: 7 seats (critic 3, reviewer 4; `residual/dispatched-payload.json`). Three sends were refused with `Background job limit reached (100). Wait for running jobs to finish or cancel one.` The unchanged payload spawned on the 4th send at about 07:27Z; the harness suffixed the seat names `-4`.
  - No wave 2: fewer than 32 attack items remained.
- **Totals**: 41 seats in attempt 3. Attempt 2's 37 seats are dead with the orchestrator, and attempt 1's seats are recorded in its commits.
- **§3 floor**:
  - Planner: the L1 (the validator rejects `planner`).
  - Connector: ConnectorShortcutClasses.
  - 4 executors, 2 scribes, 5 scouts, reviewers and critics.
- **Dead seats this attempt**: none. **Holds** (provider refusals): none.
- **Seat gate**: `kama-r27-w1a3` granted 34 at 07:07:10Z. I released it at 07:21Z while 2 of its seats were still running. The residual acquisition (`kama-r27-res`, 9 seats) counted those 2.
- **Settle**: every seat returned before its deadline. None was cancelled.

## Open items at report time

- X1 verdict needs a named non-author reviewer (the hyaku closure).
- Round-26 defect 8 (`count-c2.py` cell trust) is open.
- KQ37 is only partly implemented by the frozen A3 counter: ASCII-only folding, positional frame, no request-span overlap check.
- L0 questions: none.
- Tool installs: none by the L1. No seat reported an install.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → `SKILL.md`. Unchanged this round; no non-author mark.
- [~] At least one end-to-end domain task executed and logged in LOG.md → `LOG.md` §round 16/17. This round's live probe (`.ufo/waves/round-27/w1a3/out/ExecLiveEchoProbe/receipt.json`) is evidence for X1, not a promotion mark.
- [~] Instructions executable by an agent without oral context → `SKILL.md` §Checklist. Unchanged; no non-author mark.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md`. Unchanged.
