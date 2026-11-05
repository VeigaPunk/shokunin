# kengaku — round 91 (hyaku run 15, attempt 1, 2026-11-05)

Lane `kengaku-shokunin`, branch `master`. Lane tip at report time: `f06d0b65d85b650ba459f2db47e3bf10ffa4b732` (`git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin ls-remote origin refs/heads/master` prints the same hash; `jj-lane.sh state` shows `ahead=0`). Round verdict: **not admitted**. R91-C2 is met on its frozen predicate; R91-C1 and R91-C3 are not met; the R91-F1 companion (the R82-F1 repair) is met on its own predicate. No axis is harmed. The unmet claims are reported with their causes, not reshaped.

## Work performed

**Declared claims (frozen at commit `cd0c116e`, text in `plans/round-91-claims.md`).**
- **R91-C1 — coverage** (lowest non-retired axis, held at its L0 cap 7): a ninth located offline replay, `modernize-scientific-stack`, with counter `plans/round91_c1_replay.py`, probe `plans/round91_modernize_probe.py`, cases `plans/round91-cases.json`. **Not met** (instrument parser defect; see Mistake M7).
- **R91-C2 — calibration** (held at ceiling 10): the counters and the checker pinned externally in `plans/counter-pins-r91.json`, with the checker's own selftest in the predicate path, checked by `plans/round91_counter_pin.py`. **Met on its frozen predicate.**
- **R91-C3 — operability** (held at ceiling 10) with capability `routed-findings freeze gate v2`: `plans/round91_burndown.py` over `corpus/routed-findings.jsonl` at `--freeze-round 92`, plus triage of the 30 open and 7 blocked rows. **Not met** (gate refuses at tip; predicate identity break; see M8, M13).
- No exploratory claim. The companion `plans/round91_f1_counter.py` proves the R82-F1 QUOTE_RE repair (not a claim slot; named in the C3 Move).

**Work items, with evidence pointers.**
- *Protocol and state load:* `skill://shokunin`, `skill://godspeed`, the canonical `PROTOCOL.md`, `MISSION.md`, `AXES.md`, `CORPUS.md`, `LEARNING.md` (kimi-shokunin checkout); lane `SCORECARD.md`, `PROVINCE.md`, `corpus/lessons/round-90.md`, `corpus/lessons/round-90-verifier-spotcheck.md` (its routed items are the basis of C3), `considerthese/2026-10-26.md` item 1; `/home/vgpnk/.omp/agent/RULES.md` read before any tool decision. `corpus/QUALITY.md` Q68 and Q69 read as the round-90 routing.
- *Freeze (commit A `cd0c116e`):* claims and the ten-case table, before any instrument. Predicted vectors `PP FP FP FP FP PP FP EP PF FP`, read from the captured grader (`corpus/evidence/round52/graders/modernize-scientific-stack/tests/test_outputs.py`, sha256 `0c24195f…02a977`).
- *Instruments (commit B `386184a6`) and corrected checker (B2 `b836a862`):* the checker's selftest at B was 4 of 8 red-for-named-reason (fixtures wrong: sha256 used for git blob ids, an "absent" path that existed, a self-pin case that never reached its check; lesson M3). The fixtures were corrected and the pin ledger regenerated at B2 before any measured tip. This is a disclosed move of the pin commit from B to B2 (see Landed changes).
- *Source (commit C `a8de3e69`):* S281 admitted (line 27 quote, 10 words; live HTTP 200, 2330 B, byte-identical to the capture) and S282 rejected (`tests/test.sh`, network-bound wrapper). Both fetched 2026-11-05 by the L1 and re-checked by wave seat ScoutS281 (`.ufo/waves/round-91/w1/ScoutS281/gate-note.md`).
- *Receipt and ledger flip (commit C):* `corpus/evidence/round91/modernize-probe.txt` (`LANE_TIP b836a862…`, `CASES 10 LEGS 20`, `mismatches=0`, `PREDICATE R91-PROBE pass`); `plans/grader-population-ledger.json` gains one executed row (round 91) and nothing else (`git diff --stat`: 5 insertions, 2 deletions).
- *Triage (commit D `cefabd44`):* 40 append-only resolution rows for the 30 open and 7 blocked effective rows, drafted by wave seats ExecC3TriageA and ExecC3TriageB (`.ufo/waves/round-91/w1/ExecC3Triage{A,B}/resolutions.jsonl`, `triage-A.md`, `triage-B.md`). Result: 13 closed (each check run by its seat and shown to fail on an absent token), 3 refused (quoted L0 or blocker), 24 blocked with a named owner (22 `kengaku`, 2 `kama`). Judgment closes are named in lesson M14.
- *Wave w1 — one v1 wave, 11 seats, policy band 8–16* (`w1-spec.json`, `w1-dispatch.json`, `w1.ready`, `w1-results.json`; validator registry `.ufo/scopes/kengaku-r91-w1/swarm-registry.json`). Seats and verdicts (their files at `.ufo/waves/round-91/w1/<seat>/`):
  - **ExecC1Battery** (executor): eight controls, each observed rc recorded (positive-at-C rc 1; ledger-only rc 1; forged tip rc 1; forged stamp rc 1; decorative HOST_PYTHON rc 1; probe tamper rc 1; executed-gating code path). The parser defect is witnessed: with the id token fixed in a scratch copy the same ten cases pass (`executed=1`, rc 0).
  - **ExecC2Battery** (executor): controls 1–8 and sub-controls 5b, 5c, 6b, 7b, 7c, each observed rc recorded. Residuals observed: a one-commit checker-plus-pin rewrite passes with `--skip-selftest` (control 6); a weakened red-case expectation with a regenerated pin passes the default run (7b). Control 5b (an uncommitted self-leg bypass) passes only with `--skip-selftest`.
  - **ExecC3TriageA / ExecC3TriageB** (executors): triage drafts, above.
  - **ScoutS281** (scout): both sources re-fetched; S281 byte-identical; quote and word count verified; the frozen claims' function line ranges (16–42, 45–48) differ from the bytes (definitions at 11 and 46).
  - **ConnectorOverlap** (connector): sibling scan; no sibling implements a freeze refusal on routed-finding age, and no sibling self-pins its checker (`.ufo/waves/round-91/w1/ConnectorOverlap/overlap.md`).
  - **ScribeR91** (scribe): drafts of the LOG, SCORECARD and sources sections; integrated by the L1 with its numbers checked against the measured outputs.
  - **ReviewerPredicate** (reviewer): findings F1–F11 (F1 = C1 parser; F2 = triage not landed at tip, now addressed; F3 = selftest not in the C3 predicate line (M8); F4 = R82-V8 sentence false (M6); F5 = one-level supersession (M13)).
  - **CriticFalsify** (critic): 16 findings; AGREE on every measured number at BASE and tip (C1, C2, C3, ledger, registry, census); DISAGREE only on the predicted counts, which are recorded as mispredicts.
  - **MutTesterR91** (mutation-tester): 14 mutants: 8 killed, 6 survived at tip, with the survivors and the real input each would need listed in `mutants.md`. C1 mutants survive the tip predicate because L5 is red there; the leg kills are read from the controls.
  - **SentinelForge** (sentinel): forgeries 1a–7. Holes: forgery 3 (a supersede row closed by `check: "true"` with a one-sentence reason is admitted) and forgery 4 (a blocked row with owner `x` is admitted) (M10); forgery 5b (in-tree pin rewrite passes, the disclosed residual). Diagnostics D1–D5: C1 `openssl` crash (M12), C3 selftest not in the predicate path (M8), C3 checks read the working tree, not the measured revision (M11), C1 id parse (M7), `--file` route.
- *Lesson:* `corpus/lessons/round-91.md` — Gate (S281 admit, S282 reject, located quotes), Mistakes M1–M14 (class · evidence · captured-by · fix), measured outcome table, routed items, honest limits.
- *Quality:* `corpus/QUALITY.md` Q70–Q72 (from M3, M4, M5); the Q68 and Q69 status line recording their executable halves as landed in B and B2.
- *Misroot sweep (before the report):* `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/run15-state.json` (orchestrator-owned; not touched). No seat wrote to the fleet root.
- *L0 questions:* four lines appended (`.ufo/l0-questions.md`, `kengaku | round-91`): C1 re-freeze route, C2 in-tree pin residual, C3 decided-state mapping, frozen-text divergences (M2, M6).

## Landed changes

| commit | content | LOG / lesson pointer |
|---|---|---|
| `cd0c116e` | freeze: `plans/round-91-claims.md`, `plans/round91-cases.json` (commit A) | LOG Round 91 entry |
| `386184a6` | instruments: probe, C1 counter, C2 checker, C3 gate v2, F1 counter, anchor repair, pin ledger (commit B) | lesson M3 (B selftest 4/8) |
| `b836a862` | corrected checker selftest fixtures and regenerated pin ledger (B2; the pin commit moves from B to B2 before any measured tip) | lesson M3 |
| `a8de3e69` | receipt `corpus/evidence/round91/modernize-probe.txt`, ledger flip (executed 35 of 88), S281 admit and S282 reject, lesson (tip C) | LOG Round 91; lesson Gate |
| `cefabd44` | 40 append-only triage rows in `corpus/routed-findings.jsonl` (commit D) | LOG Round 91, Triage bullet; lesson M13, M14 |
| `f06d0b65` | LOG Round 91 entry, SCORECARD Round 91 section, lesson measured outcome and M7–M14, QUALITY Q70–Q72, wave-1 settled evidence and the L1 transcript (closing commit E = lane tip) | LOG Round 91; SCORECARD Round 91 |

## Before → after measurements

Counting commands are listed per claim. BASE `59764383`; tip C `a8de3e69`; triage D `cefabd44`. Transcript: `.ufo/waves/round-91/L1/measured.txt`.

**R91-C1 (coverage).** `python3 plans/round91_c1_replay.py --lane . --rev REV --work DIR`. Before (BASE): `TARGET executed_rows=34 member=modernize-scientific-stack located=1 executed=0 cases=0 legs=0 mismatches=0 defects=9`, `PREDICATE R91-C1 fail`, rc 1. Predicted before defects: not stated as a count in the claim; the do-nothing control is the measurement. After (tip C): `TARGET executed_rows=35 … executed=0 cases=10 legs=20 mismatches=10 defects=10`, `PREDICATE R91-C1 fail`, rc 1, all ten DEFECT lines `L5 receipt names unknown case ?`. Mispredict: the claim predicted `executed=1 defects=0` at tip; the counter's `parse_receipt()` reads the case id from the wrong token (M7). Ledger: executed 34 → 35 of 88; `file-artifact` 25 → 26 of 76; `filesystem-metadata` 2 → 3 of 10; `numeric-band` 3 → 4 of 10; `stdout-inspection` 10 → 11 of 29; `subprocess-exec` 12 → 13 of 45. **Verdict: not met on its frozen predicate.** The counter is not patched after its first measurement; the defect is routed to round 92.

**R91-C2 (calibration).** `python3 plans/round91_counter_pin.py --lane . --rev REV --work DIR`. Before (BASE): `DEFECT SETUP unreadable plans/counter-pins-r91.json`, `PREDICATE R91-C2 could-not-evaluate`, rc 2 (fail-closed). After (tip C): `PINS checked=16 matched=16 mismatched=0`, `SELFTEST cases=8 red-green-ok=8`, `PREDICATE R91-C2 pass`, rc 0. Predicted: 16 pins and 6 selftest cases; measured 16 and 8 (the selftest count is a mispredict, recorded). Controls: one-byte counter mutation rc 1; pinned path absent rc 1; record-table blob rc 1; checker-only edit rc 1 (self-pin, default run); absent ledger rc 2; one-commit checker-plus-pin rewrite rc 0 with `--skip-selftest` (residual, measured); selftest weakening with regenerated pin rc 0 (second residual, measured). **Verdict: met on the conjunction its frozen predicate states**, with both residuals disclosed (M9).

**R91-C3 (operability and capability).** `python3 plans/round91_burndown.py --lane . --rev REV --work DIR --freeze-round 92`. Before (BASE): `freeze=refused oldest_pending_round=82 pending=30 parked=7 unowned_blocked=0 malformed_unresolved=0 seeds_83_91=46 resolutions=34 checks_run=114 overrides=3`, `DEFECT override-unjustified R42-R3-37`, `PREDICATE R91-C3 fail`, rc 1. After tip C: identical. After triage D: `freeze=refused oldest_pending_round=82 pending=1 parked=26 unowned_blocked=0 malformed_unresolved=0 seeds_83_91=46 resolutions=74 checks_run=123 overrides=3`, `DEFECT override-unjustified` for R42-R2, R42-R3-33 and R42-R3-37, `PREDICATE R91-C3 fail`, rc 1. Predicted after: `freeze=admitted pending=<round-91 only>`; mispredict. Causes: (i) eight triage rows supersede round-90 rows, and the gate's one-level supersession ignores them (M13), so the only effective open row is `R82-F1` through `R82-F1-R90`; (ii) the three round-90 override rows lack `override_reason` and cannot be superseded at a second level; (iii) the PREDICATE line does not compute the selftest clause (M8): the separate run is `SELFTEST cases=13 red-green-ok=13`, rc 0. Triage verdicts: 13 closed, 3 refused, 24 blocked with owner (22 `kengaku`, 2 `kama`); the parked states follow the frozen mapping and are not fixes (L0 `kengaku | round-91`). **Verdict: not met.** No capability enters the table.

**R91-F1 (companion; the R82-F1 repair the C3 Move names).** `python3 plans/round91_f1_counter.py --lane . --work DIR`. BASE (`plans/anchor_line_check.py` pre-repair): `PARSE-ABSENT` for S260, S261, S265, S266; `PREDICATE R91-F1 fail`, rc 1. Tip C: `PARSED S260=1,S261=2,S265=1,S266=2`; `ANCHORLINE rows=272 cited=84 captured=71 uncaptured=13 defective=10 repaired=10 live=0`; `WRONG-LINE-CAUGHT True`; `PREDICATE R91-F1 pass`, rc 0. Cited rose 72 → 84. The four rows parse but carry no capture pin, so their quotes are uncaptured (M5). **Met on its own predicate.**

**Mutations and attacks (wave).** Mutants 14: 8 killed, 6 survived at tip (`MutTesterR91/mutants.md`). Forgeries: holes 3 and 4 (M10); the in-tree pin residual (5b). Critic: agreement with all measured numbers.

## Sources & frontier

- **SOURCES census, before → after** (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`): before (round start, measured 2026-11-05) exit 0, `kengaku ok`, 272 rows; after (tip C and at the closing commit) exit 0, `kengaku ok`, 274 rows. Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 272, then 274. The `W04` duplicate-URL warnings are pre-existing (rows ≤ S270).
- **Rows added by tier:** S281 tier A (member replay only, `mined`); S282 tier A (tool, rejected). Tier A 242 → 244; B 24; C 6. Status: mined 246 → 247; rejected 18 → 19.
- **Rows touched old→new:** none.
- **Frontier rows advanced:** S281 `mined`, cited by `corpus/lessons/round-91.md`, `corpus/evidence/round91/modernize-probe.txt` and the C1 claim (the sourced claim of the round). The ledger's `modernize-scientific-stack` `executed`.
- **Assimilation:** none. `merge/kengaku/` stays held by L0 `kengaku | round-54`. **considerthese:** none implemented this round (item 1 of `considerthese/2026-10-26.md` was mined in round 90; its freeze-wiring residual is C3 here, not met).
- **Mistake mined:** M1–M14 in `corpus/lessons/round-91.md`; M7 (parser token) and M13 (chain supersession) are the live ones.

## Trend verdicts

- **expansion: unchanged.** No `corpus/knowledge/` entry was admitted; `git diff --stat dcdd494e..f06d0b65 -- corpus/knowledge` prints nothing. The ninth member is coverage counted by the ledger, not expansion.
- **quality: unchanged.** Q70–Q72 are criteria grounded in M3–M5 with executable halves; the Q68/Q69 halves were recorded as landed. Criterion growth is not a measured quality move over entries.
- **discernment: unchanged.** The round's gate decisions (S281 admit, S282 reject) and the triage closes have no non-author verdict yet; the wave seats are lane-dispatched and, per LEARNING.md, are the lane. The wave's measured holes (M8, M10, M13) are calibration evidence for the next round's closure, not a non-author judgment.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md (lane author assessment; no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md Round 91 entry; receipt `corpus/evidence/round91/modernize-probe.txt`
- [~] Instructions executable by an agent without oral context — corpus/lessons/round-8-aggregator-box3-coldrun.md
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md (Adjacent section; this round's connector scan absorbed nothing)

## Stale-lane

Stale-lane: no other mission of this lane is open. Attempt 1 of round 91 is the only open mission; no `lane-dead-no-report kengaku round=91` line has been written. No mission is open longer than two driver ticks.

## Tool installs

None. `RULES.md` was read first. This round installed nothing: `bwrap` 0.13.1, `python3` 3.14.8 and `openssl` 3.6.5 were already on the host. No pacman transaction, no sysctl change, no host-service change.

## Host and environment

- `/proc/sys/user/max_user_namespaces` read 122865 at every receipt and every run. The lane changed no host setting. The seats were instructed not to touch host sysctls; none reported a change.
- Scratch under `/fast/scratch/hyaku/kengaku-r91/`; seats removed their trees after copying receipts; the L1 removes `kengaku-r91/` after this report lands.

## Wave shape and seats

- One v1 wave, **11 seats** (band 8–16). Roles: executor 4 (ExecC1Battery, ExecC2Battery, ExecC3TriageA, ExecC3TriageB), scout 1, connector 1, scribe 1, reviewer 1, critic 1, mutation-tester 1, sentinel 1. Attack seats (reviewer, critic, mutation-tester, sentinel) 4 of 11 = 36 %, meeting the ≥ 25 % floor. Connector seats 1 (≤ 2). The planner seat is the L1 (the validator rejects planner as a swarm role). No residual call.
- **Dead seats: none.** All eleven seats wrote their output files; `w1-results.json` settled.
- The frozen claims' round-shape line (executor 3, labrat 1, attack 5 of 12) does not match the dispatched spec; the spec is the one dispatched. Recorded as a frozen-text divergence (L0 `kengaku | round-91`).
- Answering models are not recorded in the results file and are not claimed here.

## Round admission and open claims

- R91-C1: **not met** (instrument parser defect, M7). R91-C2: **met** on its frozen predicate (residuals M9). R91-C3: **not met** (M8, M13, and the override defects).
- No axis harmed: coverage held at 7, calibration at 10, operability at 10; novelty 8, depth 10, freshness 10, adjacency 9 held (no move claimed).
- Round not admitted. Honest stop: the unmet claims' fixes are routed to round 92 under new frozen predicates; nothing was reshaped after a measurement.

## Open L0 questions (appended to `.ufo/l0-questions.md`, committed in the fleet commit with this report)

- `kengaku | round-91` — C1 measured NOT MET on a parser defect; ruling on the re-freeze route for instrument defects found by a first measurement.
- `kengaku | round-91` — C2 in-tree pin residual (restated from round 90); ruling on in-tree pins or an anchor outside the tree.
- `kengaku | round-91` — C3 decided-state mapping (restated); ruling on refused and owned-blocked as decided.
- `kengaku | round-91` — frozen-text divergences: function line ranges (M2) and the R82-V8 sentence (M6); clerical or reopening C3?

## Routed to round 92

1. C1: fix `parse_receipt()` case-id token under a new frozen predicate, with the probe receipt's ten `ok=True` lines as witness; guard every host probe to `DEFECT SETUP` (M7, M12).
2. C3: run the selftest in the gate's predicate path (M8); chain-aware supersede with its own selftest case (M13); closing checks reference the row's own evidence path, and blocked owners resolve to a lane id (M10); checks run at the measured revision via a worktree (M11).
3. C2: pin the selftest's expected-rc table in the predicate path (M9).
4. Capture-pin S260, S261, S265, S266 through supersede rows (M5); R82-V8 clone-path dependence (M6).
5. C1 coverage: the next offline member from the ledger's class arithmetic (`filesystem-metadata` is 3 of 10).

## Work not done (named)

- The C1 counter fix and the C3 gate fix are not done this round (routed; frozen-rule reasons above).
- The four blind-spot rows' quotes are not captured-verified (M5).
- The LOG Round 91 wave bullet says "14 controls" for ExecC2Battery; the seat's `controls.txt` (authoritative) lists controls 1–8 plus sub-controls 5b, 5c, 6b, 7b, 7c.
