# tsukuroi — round 34 report (attempt 1, 2026-10-23)

Lane tip `6aad5b12c9f7a1f288971d36f150c9339f1fa14c` (pushed; `jj-lane.sh state`: local = remote, ahead 0). Claim base `2641591e`.

## Work performed

Declared claims (`SCORECARD.md` "Round 34 — declaration", commit `6de666c4`):
- **C1 (operability):** nine harness-viable lane tools that copied the ambient environment minus `GIT_*` into their children now build it from a fixed allow-list. Counter: `tools/probe-child-env-allowlist-r34.py` (label `leaking`). After-value: 0 of 27, `harness_errors` empty, exit 0.
- **C2 (depth, exploratory):** what the census `coredump=` count and the ADJ-04 `class=coredumps value=` count. The note is `corpus/knowledge/coredump-count-unit-r34.md`.

Work items:
- Declaration, the round-33 amendment-2 correction and L1 dev runs: `6de666c4`.
- Wave w1 (39 seats) scored eighteen pre-data controls under the declaration bytes. None reached 0 of 27 (`.ufo/waves/round-34/w1/`, landed `15c9ac0e` and `3457f287`).
- **Pre-data amendment 1** (`15c9ac0e`): adds a claim-base parity clause. CritC1AxisFit found that a dummy target with its work replaced reads 0 of 27 under the declaration bytes. Residual call R1 confirmed it: 0 of 27 under the declaration bytes, 18 of 27 under amendment 1.
- Residual pre-data call `res` (6 seats):
  - before: 27
  - dummy: 18
  - replay dummy: 18
  - positive control: 0
  - junk/label re-scores: 27/27
  - R5 review: re-design before data, but the disclosure was incomplete. A correction is appended to `SCORECARD.md`.
- **Pre-data amendment 2** (`3457f287`): adds an any-name ambient-value clause and an execveat/unparseable-record clause. The code-reading items (round-33 defect 4: ReadRunChannels, ReadScanAmbientReads, ReadScanSpawnShapes) found 9, 4 and 4 classes outside the named limit. The same commit fixed the kill-rule reading.
- C1 change: `df661507`. After receipt: `.ufo/waves/round-34/after/c1-after-df661507.jsonl`, 0 of 27, exit 0.
- Repairs and C2 note: `879daa95`. Measured outcome, lesson, S189/S190, wave-2 evidence: `a8b46ac8`. Late wave-2 evidence: `6aad5b12`.
- Wave w2 (43 seats, falsify) reran C1 independently:
  - RerunAfterA: 0/27
  - RerunAfterB: 0/27
  - RerunBeforeIndependent: 27/27
- w2 after-mutants: **MutAttrgetterCopy and MutPathCopy SURVIVED** (0 of 27, exit 0, while an ambient name or value reaches a child in an ordinary run). MutMutatedValue (2), MutPythonReexecInherit (3) and MutOneTargetSkipWork (2) were killed.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Declaration, r33 amendment-2 correction, probe r34 | Round 34 entry, first paragraph | `6de666c4` |
| Pre-data amendment 1 + w1 receipts | "Amendment (pre-data, 08:52Z)" | `15c9ac0e` |
| Pre-data amendment 2 + residual receipts | "Amendment 2" | `3457f287` |
| C1 change (nine tools) | "C1 change" | `df661507` |
| Repairs (QUALITY-8 header, three C2 wordings, `check-knowledge-header.py`, nine cadence tokens), C2 note, S186-S188, SKILL reading rule and round34 registry | "Repairs and C2" | `879daa95` |
| Outcome, axes table, lesson, S189/S190, note corrections, disclosure correction, census end | "Result" | `a8b46ac8` |
| Late wave-2 evidence | (evidence only) | `6aad5b12` |

## Before → after measurements

- **C1:** `python3 tools/run-receipt.py --revision <REV> --tool-revision 3457f287 --out <f> -- tools/probe-child-env-allowlist-r34.py --revision '{rev}' --lane '{lane}'`.
  - Before: 27 of 27, exit 1 at `3457f287`.
  - After: 0 of 27, exit 0 at `df661507`.
  - Verdict: **not verified**. The declared kill rule fires on the two surviving after-mutants, so this is an honest stop. The counter is not changed after data.
- **C2:** exploratory, no counter. The dated reconciliation at 08:44Z was 1621 entries: 183 "dumped core", 69 null-printed, 1365 "without generating a coredump" and 4 handler errors (`.ufo/waves/round-34/w1/ExecCoredumpReconcile/capture.txt`).
- Gates at `a8b46ac8`, all exit 0: knowledge-header, self-assessment, registry-coverage, recheck-commands. Knowledge-header was exit 1 at `6de666c4`; self-assessment and registry-coverage were exit 1 at base.

## Sources & frontier

- Census command: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`. Start: exit 0 (`.ufo/waves/round-34/l1/census-start.txt`). End: exit 0 (`census-end.txt`).
- Row count went from 185 to 190 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- Added, all tier A:
  - S186, S187, S188, S189 (`mined`, used by the C2 note)
  - S190 (`rejected`, redundant with S188): the Gate reject
- S177 was re-opened and is unchanged. No existing row was changed.
- Sourced claim: C2 (S186-S189).
- Mined mistakes (lesson `## Mistakes`):
  - R33-QUALITY8-NOTE-HEADER
  - R34-SWEEP-TRUNCATED
  - R34-COUNTER-SELF-BASELINE
  - R34-DISCLOSURE-RACE
  - R34-COUNTER-READ-SIDE-GAPS
- Frontier: the counter needs an untraced observation view before any re-claim.

## Trend verdicts

- **expansion: `unchanged`.** No new surface is held. One note was added that passes QUALITY 8 by gate, and all 54 notes pass.
- **quality: `improved`.** All of the following:
  - Nine tools no longer copy the ambient environment: three receipts and selftests 31/31 with no harm.
  - Round-33 defects 1-6 were repaired, including the QUALITY-8 gate, red at base and green at the tip.
  - Self-assessment and registry-coverage went from 1 to 0.
  - C1 itself is not verified.
- **discernment: `improved`.** The pre-data controls caught the self-baseline gap and the code-reading gaps before data. The kill rule was applied against the author's own claim. Against this: CritC1Amendments judges both amendments a breach of the after-any-seat freeze, CritKillRuleReading judges the fork exclusion a narrowing, and the amendment-1 disclosure needed a correction.

## SHONEN

- [~] SKILL.md tables, patterns, sources: `SKILL.md` round-34 reading rule and round34 registry (`879daa95`).
- [~] End-to-end task: unchanged (`corpus/knowledge/host-health-report-r3.md`).
- [~] No-oral-context instructions: unchanged.
- [~] No cross-domain bleed: C2 classifies no crash by cause; wave-2 CritC2Absorb2 found no adjacency crossing (`.ufo/waves/round-34/w2/CritC2Absorb2.md`).

## Gate

- Real reject: **S190** (`logs-show.c`), redundant with S188 (lesson `## Gate`).

## Round shape, seats, holds

- Shape: two v1 waves plus one residual call. The residual call carried code-running controls (mutation-tester/executor), per Main's 08:12 note.
- Waves:
  - w1: 39 seats (17 mutation-tester, 8 executor, 4 reviewer, 4 scribe, 2 scout, 2 critic, 1 connector, 1 sentinel)
  - res: 6 seats
  - w2: 43 seats
- Round total: 88. The L1 held the planner seat.
- Dead seats: none.
- Holds (provider refusal `cyber_policy`, not retried): MutCensusV5Shortcut, MutExecveatSpawn, MutBinGitAlias.
- Unsettled when the lesson was written: 15 w2 seats are listed in the lesson. Three of them later delivered and were landed in `6aad5b12`: SelftestsAfterNoHarm (no harm), RevCadenceEdits, CritC1Amendments. The other 12 were still running at filing and are not evidence: MutHomeKeep, MutRenamedExpanduser, MutNestedNoneBuilder, MutKeptDrop, RegressionAfter, RevC1Diff, CritC1AxisFitAfter, RevAmendment2, RerunCoredumpReconcile, RevHeaderGate, RevR33NoteRepairs, RevCensusV5, ConnSiblingAfter.
- Misroot sweep (w2 ScoutMisroot): 0 files.
- Installs: none.
- L0 questions: none.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
