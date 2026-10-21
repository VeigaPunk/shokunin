# mori — round 20 report (L1 MoriR20, attempt 1)

Lane HEAD (landed, remote-verified): `b6be91670d6232ac8bf86db9bc51119d1247b9a6`. Entering tip
`2061780117e6ca637725004897bd288d3ba7e988` (round 19 admitted). Lane commits this round: `e4d9384`
(frozen contract + C2 cases + entering drift receipt, before any implementation), `2eeae04` (C2 tool,
oracle, live scans, wave-1 dispatch evidence), `8f8c58e` (C1 register + re-pin, corpus, wave-1
reports), `71abd41` (wave-2 falsification integrated, final evidence), `b6be916` (late wave-2
corrections: souji receipts are same-identity, not non-author; `resumeSends` members unread).

## Work performed

Declared claims (2):
- **C1 — freshness** (lowest-score tie depth/freshness/calibration at 5; calibration was chosen in
  rounds 17–19, freshness last moved round 10): classify every live census drift token against the
  r10 baseline into a closed class set with evidence, then re-pin. Sourced: S066, S076 (supersedes S067).
- **C2 — coverage, capability acquisition (FR3 advance)**: `tools/mori-wave-settlement.py`, per-seat
  report presence for every swarm dispatch file. Sourced: S068, S073, S074 (supersede S069/S071).

Work items:
- Frozen contract `.ufo/waves/round-20/contract.md` and `frozen/c2-expected.json` (14 cases) at `e4d9384`.
- Entering drift receipt `evidence/c1-drift-entering.json`: `--drift baseline-r10` rc 1, 50 tokens, 8
  unclassified against the round-13 register.
- Register `corpus/evidence/drift-classification-r20.json` (builder `.ufo/waves/round-20/build-register.py`):
  50/50 classified — census-schema-change 26, live-state 19, roster-change 5, census-regression 0; two
  `blind_spot` rows with recorded dissent.
- Re-pin `corpus/evidence/baseline-r20-20261021T1051Z.json` (pinned_ts 10:53:07Z, census sha
  `87b8d680…ab28` unchanged); r10 baseline byte-unchanged; timeline `evidence/c1-repin-timeline.txt`.
- C2 tool (final sha256 `79e7f9de…28f9`), independent oracle `build/OracleHarness/c2-oracle.py`
  (v0 fixture defect retained as red), refinements R1–R8 + vocabulary guard, selftest 23/23.
- Live: all ten historical mori waves reproduce wave-1 manual ground truth exactly (r19 W1 16/64,
  W2 48/70, r18 W1 53/68 = the 15 dead-seat names); fleet scan of 21 lanes / 196 dispatch files
  (`evidence/c2-live-fleet.json`, final `c2-live-fleet-final.json` at 11:17:57Z).
- Knowledge `corpus/knowledge/drift-repin-r20.md`, `corpus/knowledge/wave-settlement-r20.md`; SKILL.md
  r20 section; PROVINCE/README round-20 notes; QUALITY 64–68; lesson `corpus/lessons/round-20.md`.
- Planner seat: held by the L1 (validator rejects `planner`); planning data-walk rode the scout/reviewer
  items (TokPinFlap, CensusWavesSurface, FleetDispatchInventory).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Frozen contract, C2 cases, entering drift receipt | LOG.md "Round 20 (L1 MoriR20)" | `e4d9384` |
| C2 tool + oracle + live scans + wave-1 dispatch evidence | same | `2eeae04` |
| C1 register, baseline-r20, knowledge, SOURCES S066–S072, QUALITY 64–68, lesson, wave-1 reports | same | `8f8c58e` |
| Wave-2 corrections (R7/R8, vocab guard, 3 roster reclasses, S073–S076, SKILL/knowledge fixes), final evidence, SCORECARD/LOG | same | `71abd41` |
| Late wave-2 corrections (FamWavesIo, ReviewProvince F1) and remaining falsify reports | same | `b6be916` |

## Before → after measurements

- **C1** (measured at `71abd41`; census bytes identical since `2061780`): unclassified drift tokens
  **8 → 0** of 50 (entering) and **7 → 0** of 49 (pre-pin 10:51Z); post-pin `--drift baseline-r20`
  `MORI_DRIFT: none` rc 0 at 10:55:31Z (L1) and 11:00:57–11:02:06Z (wave-2 PostPinWindow).
  Command (receipt `evidence/c1-count.json`):
  `export LC_ALL=C; comm -23 <(tr ' ' '\n' < DRIFT | grep -v '^MORI_DRIFT:$' | grep . | sort -u) <(/usr/bin/jq -r '.tokens|keys[]' REG | sort -u) | wc -l`
  — the frozen text set `LC_ALL=C` on `comm` only and miscounts under en_US.UTF-8 (37/33); corrected, disclosed (lesson M9).
- **C2** (measured at `71abd41`, tool sha `79e7f9de…`): independent oracle `capability_absent` **14 → 0**,
  matched 0 → 14. `/usr/bin/jq -s '[.[].counts.capability_absent]' .ufo/waves/round-20/evidence/c2-before.json .ufo/waves/round-20/evidence/c2-after.json`
  → `[14,0]`. Capability, not 14 historical defects.
- No-harm (L1, 10:59Z): census selftest 134/134, silence oracle 28/28; wave-2 NoHarmRun: 20/20 battery
  commands rc 0 (r13 24/24, r14 44/44, r15, r16 64/64, r17 66/66 + 17/17, r19 pass, r18 selftests).

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: start rc 0, end rc 0
(W04 only: S035/S037 pre-existing, S073/S074 same-URL supersession rows). Rows 65 → 76
(A55/B3/C7 → A62/B6/C8; mined/queued/rejected 34/23/8 → 42/25/9). Added: A S066, S068, S069, S070,
S073, S074, S075; B S067, S071, S076; C S072 (rejected). Same-round corrections after wave-2
re-openings: S073 supersedes S069, S074 S071 (tier B→A, teaches), S075 S070, S076 S067. In-place
used-by appends of `corpus/lessons/round-20.md` on S066, S067, S068, S071 (logged in the lesson).
Round-12 Bash lead: source admitted (S070/S075), linkage pending. Non-author spot-check: Main agreed
S068 admit and S072 reject. Frontier: FR3 per-seat filesystem settlement moved to Core; hygiene vs
never-written, dispatch authenticity, successors, JSON-only discovery stay Frontier. Mined mistakes:
lesson M1–M10 (M1 r19 48 hand-counted reports → C2 shown failing on that wave).

## Trend verdicts

- **expansion: improved** — two admitted knowledge entries citing mined rows; `wave-settlement-r20.md`
  covers uncovered FR3 ground (CriticTrends agrees for that entry; questions the drift note as new ground).
- **quality: improved** — the stale r10 behavioral reference re-verified token-by-token and superseded
  by a classified pin; four over-reaching source rows superseded the same round (CriticTrends proposed
  `unchanged`; operator to rule).
- **discernment: improved** — non-author Main agree on S068 admit / S072 reject; disputed classes kept
  as recorded dissent rather than self-resolved.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `[~]` evidence `SKILL.md:471-500` (no non-author verifier)
- [~] At least one end-to-end domain task executed and logged — `LOG.md` round 20 (fleet settlement scan), not outside-verified
- [ ] Instructions executable by an agent without oral context — untouched (wave-2 ReviewSkill PARTIAL, fixed)
- [ ] No cross-domain bleed — untouched by a non-author

## Waves, seats, routing

- W1 build `mori-r20-build`: 76 seats (executor 5, scout 39, reviewer 10, critic 4, revenger 2,
  connector 4, sentinel 1, scribe 11); 76/76 reports, 0 dead, 0 replacements
  (`evidence/wave1-settlement-scan.json`).
- W2 falsify `mori-r20-falsify`: 67 seats (mutation-tester 4, reviewer 40, critic 6, scout 12,
  sentinel 1, revenger 1, connector 1, scribe 2); at the 11:17:57Z scan 59 reports + 8 start-stubs
  (FamWavesIo, LiveKama, LiveMoriR19W2, LiveTameshi, LiveTsukuroi, ReviewProvince, ReviewQuality,
  SelftestC2; LiveMoriR19W2 and LiveTsukuroi had delivered results by task output). No seat death
  observed, no replacements. Round total 143 ≤ 200. Each wave dispatched by one validated `task` call.
- Wave-2 verdicts that changed the round: AdjudicateWaves BROKEN (WAVE_UNSETTLED_AGE class — kept,
  dissent recorded), FamRosterLanes (3 reclasses), MutTraversalAllowed survived (R7 added),
  VocabFleet mutant A survived (guard added), SeparationCheck BROKEN on incidental counters only
  (oracle and historical waves are C1-independent), Reopen S067/S069/S070/S071 (superseded rows).

Open residuals routed to the closure: `resumeSends` members unread (ReviewProvince F1), registry-only
waves invisible (souji r19 w1, LiveSouji), exit 0 with zero discovered waves, STALE/WAVE class dispute.

## Misroot sweep, inherited state, installs

- `git -C /home/vgpnk/Projects/shokunin status --porcelain`: only `?? .ufo/waves/round-20/` (souji's
  AuditCase07 tree [INFERENCE], not mori's; untouched). No mori misroot remains (wave-2 FleetMisrootEnd).
  One seat (DraftProvince) misrooted and self-removed (lesson M7).
- No inherited uncommitted mori outputs (clean entering state). Seat scratch fixtures that were
  unreadable or dispatch-shaped (`falsify/NoHarmRun/r17-seat`, `falsify/SentinelTool/probe-*`) were
  deleted before commit; scratch HistR*/TokSilenceB/TrailerVariants copies were left uncommitted.
- Tool installs: none (all seats reported none).
- Stale-lane: respawn-per-round driver; no other mori mission open.
- Open L0 questions: none.
