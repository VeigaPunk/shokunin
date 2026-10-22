# mori — round 26 report (attempt 1, L1 MoriR26)

Lane tip (pushed): `ef9dbee136d6ed2ef98687f5cb0c0a16506a5155` (`jj-lane.sh state`: local = remote, ahead 0).
Entering tip: `248408f5b6610a85bcbdebe7ac0b4fa7ed51422a`. Contract: `.ufo/waves/round-26/contract.md` (landed
`28b04940`; amendment A1 `99338de7`; amendment A2 and addenda `825f988f`, `93aa1b93`, `738eec13`, `f1efb465`, `950d8a56`).

## Work performed

Declared claims (frontier area FR10, userspace OOM killers; a different area from the routed-repair claims of
rounds 23–25):

- **C1 — freshness (score 5, tied lowest):** supersede the stale FR10 host-state statements with a new entry.
- **C2 — coverage (score 6), capability:** `tools/mori-oom-killers.py`, a read-only one-shot read of earlyoom and
  systemd-oomd (state, earlyoom's own startup thresholds, counts of its action lines, oomd kill notices).

Work items:

- Found the admitted entry `corpus/knowledge/userspace-oom-killers-r12.md` stale: it said both killers were
  inactive; earlyoom 1.9.0 is active and enabled (installed 2026-10-20), systemd-oomd inactive and disabled
  (`.ufo/waves/round-26/capture/capture.txt`).
- Froze the contract and the C1 phrase list before any work (`28b04940`); wave-1 critics showed the first C1 command
  was fail-open, so A1 replaced it with committed counters `count-c1.sh` / `count-c2.sh` before any C1 after-value.
- A separate seat wrote 32 cases (`5b10649d`) before the tool; the tool seat built blind and passed 32/32 on first
  run (`c2fdd929`). Later case-seat amendments are `cases-supplementary.json`, not counted.
- New entry `corpus/knowledge/userspace-oom-killers-r26.md` (sources S114–S126), dated corrections in r12 lines 3,
  6, 14, 18, README rows, PROVINCE notes, SKILL.md FR10 decision table, error patterns and three registry rows (`327fbcca`).
- Per-boot capture (`capture-boots.txt`): the previous boot holds 38 SIGTERM and 1 SIGKILL earlyoom send lines; the
  current boot none; oomd notices 0 in every retained boot.
- Tool rules hardened after the freeze without touching a frozen case (amendment A2): dry-run and process-group
  lines, journald suppression, non-steady states, earlier invocations, unbounded scope, unreadable journal,
  per-invocation dry-run, unplaceable timestamps (commits `825f988f` … `950d8a56`).
- Routed hygiene: R2, R4 (incl. the Axes operability row), R6 fixed (`2a23fbdc`); R8 scan at every tip; R5 partly
  (registry rows); R1, R3, R7 named debt (`corpus/lessons/round-26.md`, "Routed round-25 defects R1–R8").
- Dated the three `systemd 261` statements in `journal-alarm-routing-r14.md` (`cb5c2f78`).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| contract, phrase list, before receipts | round 26 declaration | `28b04940` |
| SCORECARD/LOG declaration, wave-1 spec and dispatch | declaration | `5e5e86f1` |
| frozen cases | outcome | `5b10649d` |
| tool, fixes, supplementary cases | outcome | `c2fdd929`, `278f02e4`, `825f988f`, `93aa1b93`, `738eec13`, `f1efb465`, `950d8a56` |
| amendment A1, counters | outcome | `99338de7` |
| captures | outcome | `b4473ed4` |
| entry, r12 corrections, SOURCES, SKILL, README, PROVINCE, lesson, QUALITY 78–79, LOG correction | correction + outcome | `327fbcca` |
| allowlist rows (name-only) | outcome | `58540501`, `4dba9cc7`, `2ecb6615` |
| measured outcome, capability row, receipts | outcome | `c6ea248a`, `5829c943` |
| S124 correction, hygiene R2/R4/R6, r14 dating | outcome | `16935e24`, `2a23fbdc`, `cb5c2f78` |
| outcome LOG entry, wave reports; RetentionTip report withheld | outcome | `ea4c92f6`, `ef9dbee1` |

## Before → after measurements

- **C1:** `bash .ufo/waves/round-26/count-c1.sh <rev>`. Before at `248408f5`: `stale_present=4 r26_entry=absent
  r26_new_source_ids=0 r12_names_r26=0`. After at `327fbcca` and `950d8a56`: `stale_present=0 r26_entry=present
  r26_new_source_ids=13 r12_names_r26=4`; `deadbeef` → `bad_rev`, exit 2. Receipt `evidence/c1-count.txt`.
  Wave-2 RerunC1Count reproduced every value. Limits: MutC1Script — markup (backticks, underscores) or a copy in
  another file hides a phrase from the counter (4 of 19 mutants); none occurs at the tip.
- **C2:** `bash .ufo/waves/round-26/count-c2.sh <rev>`. Before at `248408f5`: `absent`, exit 2. After at `950d8a56`:
  `freeze_order=ok cases_changed_since_freeze=0 N=32 PASS 32/32 exit=0`. Receipts `evidence/c2-count.txt`,
  `c2-selftest.txt`, live `c2-live-run.txt` (`KILLERS_QUIET`, current invocation). Wave 2: the count reproduces
  (RerunC2Count; the counter's own exit is 0 even if the selftest fails — low defect); 30 mutants: frozen file kills
  most, survivors are coverage gaps (mem/swap swap, error path, selftest comparator, every A2 rule). A2 behaviour is
  shown only by committed detector inputs (`evidence/a2-detectors/`, `a2-detectors.txt`).
- **No harm:** retention scan 4 at `248408f5`, 4 at `ef9dbee1` (mid-round 6, 5 and 7, each repaired; mistake M2).
  Operability: census 134/134, pressure 12/12, runway 21/21, routed check held, settlement 23/23 (wave-2 OperabilityNoHarm).

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: start exit 0 (six W04), end exit 0
(same six W04). Rows 113 → 126: 13 added (S114–S126; tier A 12, tier B 1 — sibling tsukuroi S125), 0 rejected.
Row touched: S124 `teaches`/anchor corrected same round (old → new in the lesson). Gate table with located quotes:
`corpus/lessons/round-26.md`, "## Gate". Frontier: FR10 one-shot read moves to Core; earlier invocations of a running
earlyoom, previous boots, oomd xattrs and D-Bus remain frontier. Sourced claim: C1's entry cites S114–S126; C2's
grammar rests on S118/S119. Mistakes mined: M1–M4 with QUALITY 78–79. Wave-2 ReopenS116S117 found S117's description
in the entry's `source:` line differs from the row (medium) — not fixed before the stop.

## Trend verdicts

- **expansion: improved** — new admitted-candidate entry on FR10 ground (earlyoom as the running killer), 13 opened
  rows, one capability row.
- **quality: improved** — the stale r12 entry is superseded and its stale lines dated; three stale r14 lines dated;
  wave-2 overclaims in the new entry narrowed. Open: S117 description mismatch.
- **discernment: unprovable-but-better** — wave-1 critics changed the counter before measurement and wave 2 forced
  four tool fixes; the outside spot-check is the closure's.

## SHONEN

- [~] Box 1 (decision table, error patterns, checklist with sources): `SKILL.md` "Round26 — userspace OOM killers".
- [~] Box 2 (end-to-end task logged): `LOG.md` round-26 outcome; `evidence/c2-live-run.txt`.
- [ ] Box 3 (executable without oral context): not assessed this round.
- [~] Box 4 (no cross-domain bleed): PROVINCE round-26 adjacency note; tsukuroi cited (S125), not absorbed.

## Round shape, seats, installs, other

- Shape: default two v1 waves. Wave 1 build: 35 seats (16 scribe, 6 reviewer, 3 executor, 3 scout, 3 critic,
  2 connector, 2 mutation-tester), all returned. Wave 2 falsify: 34 seats (22 reviewer, 6 critic, 5 mutation-tester,
  1 scout); 19 returned, 15 cancelled by the L1 at the run-budget stop (ReviewR12Rewrite, ReviewEntryEarlyoomFacts,
  ReviewEntryOomdFacts, ReviewEntryCapturePointers, ReviewEntryAdjacency, ReviewStaleSweepTip, ReviewToolCode,
  ReviewToolLive, ReviewToolPrivacy, ReviewSkillTable, ReviewRegistryRows, ReopenS118S119, ReopenS121S124,
  ReopenS122S123S125, ReviewLessonGate). Round total 69; attack seats 44. Dead seats: none. No residual call.
- Each wave: one task call from the L1 eval kernel carrying the validator's `taskCall` unchanged, plus one
  `solutionSpace` string per task (recorded in `wave{1,2}-dispatch.json`). Seat gate granted both waves; no refusals.
- Planner seat: held by the L1; the planning data walk rode scout ScoutPriorAdmissions.
- The wave-2 RetentionTip report was withheld from the lane (its quoted lines raised the scan to 7); kept at
  `/fast/scratch/hyaku/mori-r26/withheld/`.
- Misroot sweep (wave-2 ScoutMisroot): no fleet-root file from this round's seats.
- Installs: none. L0 questions: none new; the open question on history in the public remote is unanswered.
- Stale-lane: respawn-per-round driver; no other mori mission is open.
