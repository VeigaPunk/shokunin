# revenger — round 95 report (attempt 1)

Lane: revenger (hyaku run 15). Lane repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`, branch `main`.
Lane tip at filing: `00c4ac2b6774d9ce385e14bd92fffc4cfd217ccb` (`git -C revenger-shokunin ls-remote origin refs/heads/main` prints the same hash before this report was written).
Base `cb5c26f73c99af268bc71e9f7417bfd7e7738d83` (round-94 tip). Freeze `6e0bf15fed58f357b7fa0c881371ac7616a116f7`. Landing `c0401d2036e8e3b3b210c67515d97bfef1c2a813`.
Attempt: 1. No earlier attempt of round 95 (`.ufo/watchdog.log`: only `launch revenger round=95 pgid=40092 driver=hyaku-inline attempt=1`; no `lane-dead-no-report revenger round=95`).

## Work performed

**Declared claims (2; frozen at `6e0bf15`, `reports/round-95/claims.md`):**
- **C1 — coverage K** (the lowest non-retired owned axis, `K_HELD_BACKED` 11/15 = 7.3): coverage-map row C10 (evidence-ledger discipline) `partial` → `held` through the v4 gate. Target 12/15.
- **C2 — calibration:** the v4 counter kills the eleven named vectors (ten tree vectors plus the registry-gate code mutant) that the frozen r94 v3 counter passes. Target: all eleven killed on their frozen legs; the code mutant dies on v4.
- No exploratory claim. No capability claim.

**Work items (evidence pointers):**
1. Load order: `skill://shokunin`, `skill://swarm`, canonical SKILL/PROTOCOL/MISSION/AXES/CORPUS/LEARNING, the round prompt, lane SCORECARD/LOG/SKILL/PROVINCE/QUALITY/README, `corpus/lessons/round-94.md`, `corpus/lessons/round-94-verifier-spotcheck.md` (the non-author check of round 94: six routed defects, its §6).
2. Round-start census: `reports/round-95/controls/census-round-start.log` → rc 0, `ok`.
3. Source opening (frontier step): S500 (`src/domain/evidence.ts`) and S501 (`src/application/investigation/EvidenceLedger.ts`) at REA revision `12f6e09`, fetched 2026-11-05, HTTP 200. Bodies 17010 B (sha256 `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f`) and 18784 B (sha256 `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac`). Receipts and bodies: `reports/round-95/quote-receipts/` (`S500.receipt.json`, `S501.receipt.json`, `raw/*.body`, `fetch-log.md`). `python3 -B corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts reports/round-95/quote-receipts --sid S500 --sid S501` → `SUMMARY rows=2 verified=2 unreachable=0 unresolved=0`, rc 0.
4. Superseding C10 candidate `corpus/knowledge/round-95-evidence-ledger-discipline.md` (documentation-only; §Supersession, §Q-map Q01–Q17). `corpus/lint_entry.py` → `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, rc 0. The round-74-rejected candidate `corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md` stays byte-preserved at `rejected`.
5. C1 counter `reports/round-95/c1_k_admit_counter4.py`: `--self-test` → `SELFTEST_C1V4=pass legs=24` (`controls/selftest-c1v4.log`, rc 0: honest fixture passes, 22 forged deltas each fail on their frozen leg). Do-nothing base `--rev cb5c26f` → `C1_C10_HELD=fail`, `C1_K_HELD_BACKED=11/15`, `C1_VERDICT=fail`, rc 1 (`controls/c1v4-do-nothing.log`).
6. C2 battery `reports/round-95/forge_battery4.py`. Red-before `--stage red-v3`: frozen v3 counter reaches **10/10** tree vectors (`V3_REACH_NEW=10/10`); the registry-gate code mutant **survives** the frozen v3 self-test (`MUTANT_V3_REGISTRY_SURVIVES=pass`); `RED_V3_VERDICT=pass` (`controls/battery4-red-v3.log`). Full at freeze: `SELFTEST_C1V4=pass`, `V4_KILLS=10/10`, `MUTANT_V4_REGISTRY_KILLED=pass`, `POS_C1V4=pass`, `DO_NOTHING_C1V4=fail-as-required`, `HOLD_R94_BATTERY=pass`, `BATTERY4_VERDICT=pass` (`controls/battery4-full-at-freeze.log`).
7. Wave `w1`: ONE v1 wave, 13 seats (`.ufo/waves/round-95/w1-spec.json`; `w1-plan.out` and `w1-run.out` rc 0; `w1-dispatch.json`; handoff `w1.ready` → `w1.ready.dispatched`; WAVE-DONE received; `w1-results.json` lists 13 settled seats). The orchestrator's kernel restarted mid-wave, so seat final text was not retained (`w1-results.json` notes this per seat); the seat report files in `.ufo/waves/round-95/w1/` are the evidence.
8. Independent reproduction (ExecBattery, `w1/ExecBattery/full.log` and `red-v3.log`): every verdict line matches `controls/battery4-full-at-freeze.log` and `battery4-red-v3.log`.
9. Receipts audit (ExecReceipts, `w1/ExecReceipts.md`): frozen verify rc 0; independent field audit `FIELD_AUDIT_VERDICT=pass`, 13/13 rows per sid. No findings.
10. Freeze-state (ExecFrozen, `w1/ExecFrozen.md`): working tree equals the freeze commit for the claims, counter, battery and entry; vote digest `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`.
11. Votes (lane-dispatched; `reports/round-95/votes/{ReviewerGate,ReviewerBlind,CriticR95}.json`, copied byte-exact from `w1/<Seat>/vote.json`): three accepted votes, each bound to the candidate digest; reviewer, reviewer, critic; each has PASS decisions and ≥6-token n/a reasons with Q cross-references.
12. Admission: after the votes passed, the entry status line flipped `candidate` → `admitted` (the digest normalizes that line, so the votes stay bound). Counter at the working tree: `C1_VERDICT=pass` (`.ufo/waves/round-95/c1-tree-postvote.log`). Counter at the landing commit: `C1_VERDICT=pass`, `C1_K_HELD_BACKED=12/15`, rc 0 (`controls/c1v4-landing.log`).
13. Critic attacks (CriticR95, `w1/CriticR95/findings.md`): seven new forged trees. A1 (stale log vs swapped body), A2 (symlink artifact), A3-old (used-by to superseded entry), A5 (escaped pipe), A6 (duplicate receipt key): killed. **A3-both** (used-by names both entries) and **A4** (an unreferenced shadow entry with an indented admission-status line) **survive**. Routed to r96; neither is in the frozen predicate.
14. Mutation audit (MutationR95, `w1/MutationR95.md`): 11 of 17 legs killed (the registry-gate mutant dies on v4, which is the M6 close). Six legs (`C1_ROWS_TOTAL`, `C1_TRIO`, `C1_LINT`, `C1_EMBEDDED`, `C1_QUOTES`, `C1_K_HELD_BACKED`) have no discriminating forged delta. Routed to r96.
15. Connector (ConnectorOverlap, `w1/ConnectorOverlap/connector.md`, `measurement-r95.tsv`): sibling-overlap scan (cross-domain items reported, not absorbed); proposal-2 re-measure over the r94 window; considerthese proposal-1 receipt check: the receipt set is partial (no stub-prints-the-pass-line control; twelve of twenty-two self-test deltas receipted only by the aggregate line). Recorded as a gap.
16. Scout (ScoutReopen, `w1/ScoutReopen.md`): S098 and S096 scope cells `no-drift` against the live bytes. ScoutCiteback (`w1/ScoutCiteback.md`): no unresolved S-token in the entry.
17. Sentinel (SentinelScope, `w1/SentinelScope.md`): (a) "unexpected dirty lane paths" are this L1's own landing writes (false positive against the seat bounds); (b) a gitignored `reports/round-94/__pycache__/…pyc` written by an inline debug import of mine without `-B`, removed (M8); (c) an untracked fleet-root `evb.ts` reported at 14:39:35 is absent at my sweep (see Sweep below).
18. Assimilation collision check (ExecCensus, `w1/ExecCensus/assimilation/`): `reg-ids` 501, `staged-ids` 155, `collisions` 155. Nothing adopted; L0 `revenger | round-91` stays open.
19. Round-end census: `reports/round-95/controls/census-round-end.log` → rc 0, no E-codes.
20. Corrections (round-94 spot-check §6): C-a (Gate reject recorded in round-95 §Gate, two rejects with reasons and flips); C-b (`corpus/lessons/round-94.md` appended correction: the S499 quote is 11 words, not 13); C-c (this report's Stale-lane line grades progress); C-d (SCORECARD r94 freshness row re-graded `unchanged` by an appended erratum in the r95 section); the six routed defects are worked or routed (see Landed changes and the lesson's §Corrections).
21. Lesson `corpus/lessons/round-95.md` `## Gate`, `## Mistakes` (M1–M9), `## Frontier and census`, `## Assimilation`, `## considerthese`.

## Landed changes

Each change is tied to the LOG.md entry `## Round 95 (hyaku run 15, attempt 1) — …` and to its commit.

| change | commit |
|---|---|
| Freeze: claims, v4 counter and battery, controls, red-before, the superseding C10 candidate, S500/S501 receipts | `6e0bf15` |
| `corpus/knowledge/round-95-evidence-ledger-discipline.md` (new entry; admitted at landing) | `c0401d2` |
| `corpus/README.md`: C10 coverage row `partial` → `held`; Frontier bullet retired to the admitted entry | `c0401d2` |
| `corpus/SOURCES.md`: S500, S501 appended (tier A, `mined`, opened 2026-11-05); `used-by` old→new on S002, S096–S109 (15 rows) | `c0401d2` |
| `corpus/lessons/round-94.md`: appended correction C-r95-1 (S499 word count) | `c0401d2` |
| `corpus/lessons/round-95.md`: Gate, Mistakes M1–M9, Frontier and census, Assimilation, considerthese | `c0401d2` |
| `SCORECARD.md`: round-95 section (two claims, measurements, routed items) and the r94 freshness erratum (C-d) | `c0401d2` |
| `SKILL.md`: gate-registry rows for `c1_k_admit_counter4` and `forge_battery4` | `c0401d2` |
| `LOG.md`: round-95 entry (append-only) | `c0401d2` |
| `reports/round-95/votes/*.json` (three votes, copied from the wave) and `quote-receipts/`, `controls/` | `c0401d2` |
| `.ufo/waves/round-95/` (wave spec, registry, dispatch, seat reports, attack receipts) | `c0401d2` |
| `reports/round-95/controls/c1v4-landing.log` (counter at the landing commit) | `00c4ac2` (final tip) |

Pushed: `origin/main` = `00c4ac2b6774d9ce385e14bd92fffc4cfd217ccb` (verified by ls-remote). Commits went through `jj-lane.sh` only.

## Before → after measurements

**C1 — coverage K (lowest non-retired axis).** Counting command: `PYTHONUTF8=1 python3 -B reports/round-95/c1_k_admit_counter4.py --rev <rev>` (`C1_K_HELD_BACKED=n/15`; do-nothing base at `cb5c26f`, landing at `c0401d2`).
- before (`cb5c26f`, base): `C1_K_HELD_BACKED=11/15`; C10 `partial`; `C1_C10_HELD=fail`; verdict fail, rc 1 (`reports/round-95/controls/c1v4-do-nothing.log`). Score 7.3.
- after (`c0401d2`, landing): `C1_K_HELD_BACKED=12/15`; `C1_VERDICT=pass`, rc 0 (`reports/round-95/controls/c1v4-landing.log`). Score 8.0.
- Counter legs at landing: 17 of 17 pass (`C1_ROWS_TOTAL`, `C1_C10_HELD`, `C1_C10_CITES`, `C1_ONLY_C10`, `C1_ADMITTED`, `C1_TRIO`, `C1_REGISTRY`, `C1_VOTES`, `C1_RECEIPTS`, `C1_PYCACHE`, `C1_LINT`, `C1_EMBEDDED`, `C1_EMBED_NONVACUOUS`, `C1_SIDS`, `C1_SOURCES`, `C1_QUOTES`, `C1_K_HELD_BACKED`; `controls/c1v4-landing.log`). The `legs=24` in the self-test line counts its fixture cases, not the counter's legs.
- Measured commit: `c0401d2` (landing); the freeze `6e0bf15` is the pre-data state. Status: **met on the frozen counter; pending non-author closure.**

**C2 — calibration.** Counting command: `PYTHONUTF8=1 python3 -B reports/round-95/forge_battery4.py --stage full` (predicate `BATTERY4_VERDICT`); `--stage red-v3` is the red-before.
- before (frozen v3 counter, `reports/round-94/c1_k_admit_counter3.py`): `V3_REACH_NEW=10/10` (the v3 counter passes all ten tree vectors, so it kills none); the registry-gate code mutant survives its self-test (`MUTANT_V3_REGISTRY_SURVIVES=pass`). `controls/battery4-red-v3.log`.
- after (v4 counter): `V4_KILLS=10/10` (each vector killed on its frozen leg), `MUTANT_V4_REGISTRY_KILLED=pass`, `POS_C1V4=pass`, `DO_NOTHING_C1V4=fail-as-required`, `HOLD_R94_BATTERY=pass`, `BATTERY4_VERDICT=pass` (`controls/battery4-full-at-freeze.log`).
- Measured commit: freeze `6e0bf15` (the battery reads the frozen base archive `cb5c26f` plus the frozen instruments; ExecFrozen confirms the same bytes at `c0401d2`). Independent re-run by ExecBattery matches every verdict line. Status: **met on the frozen predicate; pending non-author closure.** Routed beyond the predicate: A3-both, A4, and six legs with no discriminating delta (see work item 13–14).

## Sources & frontier

- **SOURCES.md rows before → after** (counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` on `cb5c26f` and `c0401d2`): **499 → 501**; malformed rows (`awk -F'|' … NF!=13`): 0 → 0.
- Tier histogram (`awk` over the same bytes): before A=450 B=21 C=28; after A=452 B=21 C=28. Status histogram: before mined=463 queued=16 rejected=20; after mined=465 queued=16 rejected=20.
- Rows added by tier: A +2 (S500, S501; `opened 2026-11-05`; `mined`; `used-by` the entry).
- Rows touched old→new (`used-by` only; `status`/`recheck` unchanged): S002, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109 — each gains `corpus/knowledge/round-95-evidence-ledger-discipline.md` (the previous cell is kept). Logged in `corpus/lessons/round-95.md` §Frontier.
- Census: round start `reports/round-95/controls/census-round-start.log` → rc 0; round end `reports/round-95/controls/census-round-end.log` → rc 0, no E-codes.
- Frontier rows advanced: C10 coverage row (partial → held); the Frontier bullet for C10 is retired to the admitted entry with its open follow-ups (non-author re-fetch of S500/S501; a fixture-scoped residual-unknown run, not claimed here).
- Sourced claim: C1 rests on S500 and S501 (§2b.4), opened and quoted this round.
- Mistake mined: `corpus/lessons/round-95.md` `## Mistakes` M1–M9 (the frozen battery3 scratch dependency, the self-test catch of a helper-only delta, a red-stage re-bind miss, the v3 registry mutant survival, a revision label, a SOURCES closing-pipe miss, an over-listed C10 cell, a debug-import pycache, and a sentinel false positive with an unattributed fleet-root file).
- Assimilation: none (155/155 staged-id collisions; nothing adopted; L0 `revenger | round-91` unanswered).
- considerthese: proposal 1 of `considerthese/2026-11-05.md` adopted as practice, with a partial receipt set (the connector's gap, lesson §considerthese). Proposal 2 re-measured, not adopted.

## Trend verdicts

- **expansion: improved.** One admitted entry on ground the coverage map did not hold (C10 `partial` → `held`), sourced from two rows opened this round (S500, S501) and cited by the entry. Caveat: the entry re-grounds an earlier candidate's ground; the earlier candidate remains `rejected` and is not counted as expansion. Pending the non-author closure.
- **quality: improved.** The rejected candidate is superseded by an entry with a full Q-map, located receipts and lint clean at `c0401d2`; the schema-side sources re-opened this round show no drift (ScoutReopen `no-drift`, `w1/ScoutReopen.md`); no admitted entry failed a re-check.
- **discernment: improved (frozen calibration predicate), with the outside check still pending.** The round's gate records two rejects with reasons and flip conditions (lesson §Gate). The v4 counter kills the ten tree vectors and the registry mutant that v3 passed, a disagreement that came from the outside spot-check of round 94. Caveat: this round's votes are lane-dispatched, not non-author; no outside agreement is recorded yet. The critic's residual survivors (A3-both, A4) and the six legs with no discriminating delta are routed to r96.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` §Gate registry (`c1_k_admit_counter4`, `forge_battery4` rows; commit `c0401d2`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` `## Round 95` entry (commit `c0401d2`); end-to-end run = fetch → receipt → counter → votes → admission at `reports/round-95/`.
- [~] Instructions executable by an agent without oral context — pointer: `reports/round-95/claims.md` (frozen predicates) and `corpus/knowledge/round-95-evidence-ledger-discipline.md` §Q-map.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `git diff --stat cb5c26f..c0401d2 -- PROVINCE.md corpus/QUALITY.md` is empty; the connector's cross-domain items (chousa, kotodama, tabi) are reported, not absorbed (`w1/ConnectorOverlap/connector.md`).

No `[x]` is claimed: no non-author verifier has checked any box.

## Round shape, seats and routing

- Shape: ONE v1 wave, 13 seats (band 8–16, `scripts/hyaku/ufo-wave-policy.json`), no residual call, no second wave. The planner seat is held by the L1 (the validator rejects planner).
- Seat-role mix (from the registry): scout 2 (ScoutReopen, ScoutCiteback), scribe 1 (ScribeLesson), executor 4 (ExecReceipts, ExecBattery, ExecCensus, ExecFrozen), reviewer 2 (ReviewerGate, ReviewerBlind), critic 1 (CriticR95), mutation-tester 1 (MutationR95), connector 1 (ConnectorOverlap), sentinel 1 (SentinelScope).
- Attack share: reviewer 2 + critic 1 + mutation-tester 1 = 4/13 = 30.8 % (≥25 %). Connector: 1 (≤2).
- Round total: 13 seats. Dead seats: none (all 13 settled; their final text was lost in the orchestrator's kernel restart, so the evidence is their report files). Provider errors: none recorded in `w1-results.json`.
- Routing: `task.agentModelOverrides` only; no model was passed. The answering model per seat is not recorded by this L1.

## Stale-lane

Progressing. Two lane commits by `revenger-shokunin` after the launch line (`c0401d2` 14:56:32, `00c4ac2` 14:56:45, `git log --since='2026-11-05 13:58:31'`), and 121 lane files newer than the launch line (`find . -newermt '2026-11-05 13:58:31' -type f -not -path './.git/*' -not -path './.jj/*' | wc -l`). No other mission of this lane is open.

## Tool installs

None. Tools used were already present: `git`, `jj-lane.sh`, `fleet-commit.sh`, `python3`, `curl`, `sources-census.sh`, `audit_source_quotes.py`, `lint_entry.py`, `check_embedded_outputs.py`. In this wave, no seat ran a pacman, sudo or sysctl action (SentinelScope check 3 PASS); this L1 ran none.

## Host needs named (not acted on)

- The orchestrator's sysctl incident (`user.max_user_namespaces` set to 0 by wave seats, restored to the kernel default) is recorded in the prompt. This wave did not use bwrap sandboxes, so no seat needed the setting; the need is named for the operator: sandboxed seats need the default value, and seats must not write host sysctls.

## Sweep (misroot) and open questions

- Misroot sweep before this report: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `M .scratch/run15-state.json` (orchestrator-owned). The sentinel's untracked `evb.ts` (14:39:35) is absent at the sweep; no revenger-attributable fleet-root file exists, so nothing was copied or deleted by this L1 (lesson M9).
- Fleet root contents belonging to other lanes (`.ufo/closure-kaidoku-r92.json`, `.ufo/reports/round-94/kotodama.md`) were not touched.
- L0: no new question appended this round. Open: `revenger | round-91` (assimilation id collision, 155/155); route-around in place (nothing adopted).

## Pre-report gates

- `git -C revenger-shokunin ls-remote origin refs/heads/main` → `00c4ac2b6774d9ce385e14bd92fffc4cfd217ccb refs/heads/main`.
- `grep -c '^## SHONEN'` on this report → `1`, followed by four `- [~]` box lines (one per SHONEN.md box; no `[x]`).
