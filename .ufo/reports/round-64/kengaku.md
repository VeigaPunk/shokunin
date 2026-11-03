# kengaku — round 64 report (hyaku run 15, attempt 1, 2026-11-03)

Lane repo `kengaku-shokunin`; lane branch `master`; **final lane hash `21b13dc70fae6645ce0d6c7cdec5117ca397d071`** (`git ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` → `local=remote`, `ahead=0`). Code and evidence landing: `7c2217ed8018d480d6e4b4cb948adcdb357944c1` (the round's commit; the cited measurements were re-run on it). Frozen claims: `plans/round-64-claims.md` at freeze `859ac24f41061bffde588b9ed5d5adfea5ca8e27`, with dated Amendment A1. Lesson: `corpus/lessons/round-64.md`.

## Work performed

**Declared claims (3), each with a frozen predicate and a counting command:**

- **R64-C1 — coverage (lowest owned axis, L0-capped at 7), capability acquisition `offline-network-service-grader-probe`.** Execute the TB2 `kv-store-grpc` grader offline against a lane-built gRPC server under the frozen five-case × seven-leg table. **Verdict: predicate met; the capability enters; coverage held at 7 (L0 cap, nothing assumed answered).**
- **R64-C2 — operability (held at ceiling 10, exercised), routed defect 3.** Repair the depth gate so receipt-pointer paths resolve only inside the lane root. **Verdict: predicate met; operability held at 10.**
- **R64-C3 — freshness (held at ceiling 10, exercised), routed defects 1+2.** Provenance-trio sweep over the 29 frozen trio-red knowledge entries, plus lesson-index rows for rounds 57–62. **Verdict: predicate met after a counter correction made before any after-receipt was scored (Amendment A1 item 2); freshness held at 10.** The predicate sentence itself is unchanged.

No claim is an exploratory claim. C1 and C3 are measured; C2 is a repair whose before and after are measured.

**Work items with evidence pointers:**

- Protocol load and standing gates at round start: `.ufo/waves/round-64/frontier/gates-at-start.txt` (grader.py `CHECKS n=733 mismatches=0`; depth `PREDICATE R63-C2 pass`); `landcheck-start.txt` (**FAIL**: registry closure `MISSING 2`, the two round-63 instruments advertised without registry rows — repaired by registration, Amendment A1 item 1). End-of-round `LANDCHECK PASS n=4` was run at `7c2217ed`; that output is not committed, and its command is in the before → after table below.
- Pre-freeze before-state and controls: `corpus/evidence/round64/k2-empty-capture.txt` (`LEGS F P F F F F F`, sha `ae0a78ee…`), `k4-protoonly-capture.txt` (`P P F F F F F`, sha `b262cfe5…`), `control-k4-kv-store.proto`; `.ufo/waves/round-64/claims/before-state.txt` (grep and trio before counts); `escape-before.txt`.
- Grader identity and S230/S231 opened live by two seats each: GraderRecon and SourceReview — grader sha `115de2e9…` = `SHA256SUMS` line 80, `cmp` byte-identical; S231 quotes located (`.ufo/waves/round-64/w1/GraderRecon/s231-quotes.txt`).
- Wave (`.ufo/waves/round-64/w1`, 15 seats; dispatched per the inline spawn handoff, `w1.ready` and `w1-results.json`): ProbeBuild (probe + two batteries + determinism + check-receipt), GateScopePatch (R64-C2 patch, `gate-scope.patch`), SweepBuild (sweep tool), SweepRepairA and SweepRepairB (29 addendum blocks, 15 + 14, all re-verification commands re-run), IndexParity (six lesson rows, counts verified), KnowledgeDraft (entry), SiblingOverlap (5 contested items routed), FreezeReview (**Major on C3**: the pass path did not price clause (a); reproduced in `openedit-sim.txt`), SourceReview (both sources VERIFIED), ClaimFalsifier (C1 vectors independently derived, cell-for-cell equal; seven forged receipts rejected), ProbeMutate (six mutants; m5 and m6 on the pre-fix tool, m4 named survivor), ControlOrigin (K2 and K4 re-derived, 14/14 legs exact), SecurityScan (1 high, 2 medium, 2 low: all triaged in Amendment A1 items 3, 4, 6 — see Landed changes).
- Post-freeze corrections, dated in Amendment A1 (no predicate, leg vector, control, kill rule or counting-command sentence edited): (1) registration of the round-63 instruments; (2) sweep counter corrected to the frozen sentence — pass path requires every frozen entry to be `TRIO-ADDENDUM`, `result:` line required, absolute fallback removed (fail closed), frozen list sha-pinned, two selftest legs added (round-63 heading; opening-edit form); (3) addendum-shape normalization (45 bullet strips, 14 timestamp moves; `corpus/evidence/round64/addenda-normalization-diff.txt`; byte-prefix check 29/29); (4) probe install environment hardened (`_tool_env`), receipt of record re-run under it, pre-hardening pair kept under `corpus/evidence/round64/prehardening/`; (5) freeze citation path fixed by a byte copy; (6) named limits.
- Scope of the sourced claim: C1 rests on S230 (the grader) and S231 (grpc.RpcError), both cited in `corpus/knowledge/tb2-kv-store-grpc-offline.md`.
- Mistakes mined: nine `## Mistakes` rows plus environment and newline rows in `corpus/lessons/round-64.md`; QUALITY **Q46** added (pass paths price every clause of the frozen sentence; each instrument's forbidden form is a red fixture).

## Landed changes

Every change below is in commit `7c2217ed` unless marked `21b13dc7` (the tip receipt).

| change | LOG.md entry | commit |
|---|---|---|
| Freeze: claims doc, controls K2/K4, before-state receipts, wave spec (`plans/round-64-claims.md`, `corpus/evidence/round64/{k2,k4}-*`, `.ufo/waves/round-64/claims`, `frontier`) | round 64 (freeze, plus LOG round 64 entry) | `859ac24f` (freeze) |
| R64-C1: `plans/round64_c1_kvstore_probe.py`, receipt of record `corpus/evidence/round64/kvstore-probe.txt` + `.server-log`, `selftest.txt`, `prehardening/` | round 64 | `7c2217ed` |
| R64-C1: knowledge entry `corpus/knowledge/tb2-kv-store-grpc-offline.md` (trio green); SOURCES rows S230, S231 | round 64 | `7c2217ed` |
| R64-C1: SKILL network-service decision row flip (executed 1 of 8, dated), registry rows `round64-c1-kvstore-probe`, `round64-trio-sweep`, `round63-gate-checks` updated; registry rows `round63-c1-pypi-probe` (round-start repair) | round 64 | `7c2217ed` |
| R64-C2: `plans/round63_gate_checks.py` (escape-aware `_resolves`, `DETAIL escape=`, four-case selftest), byte-identical to the GateScopePatch seat's file | round 64 | `7c2217ed` |
| R64-C3: `plans/round64_trio_sweep.py` (counter corrected per Amendment A1 item 2); 29 appended dated addenda in `corpus/knowledge/*.md` | round 64 | `7c2217ed` |
| R64-C3: `corpus/README.md` rows for lessons round-57..62, round-64, the round-64 knowledge entry, the round-64 evidence and wave dirs | round 64 | `7c2217ed` |
| Standing: `plans/round54-entrytruth.json` ledger rows (round63 ×2, round64 ×2) | round 64 | `7c2217ed` |
| Quality: `corpus/QUALITY.md` Q46 | round 64 | `7c2217ed` |
| Lesson `corpus/lessons/round-64.md`; SCORECARD round-64 section and capability entry; LOG round 64; PROVINCE round64 admission | round 64 | `7c2217ed` |
| Tip re-run receipt of the sweep (files=66 after the kv-store entry landed; frozen 29 all addended) | round 64 | `21b13dc7` |

Not landed, by design: `executed17.lst` (the round-62 census's executed set, unchanged — the kv-store execution is recorded in the SKILL row and the entry; the census receipt is not re-derived). The 29 frozen knowledge entries' openings are unchanged (CORPUS.md prohibits in-place rewrites; the trio gate's red on those openings is recorded drift, not repaired).

## Before → after measurements

Counting commands are the frozen ones, re-run on `7c2217ed` (the round commit) and `21b13dc7` (the tip) from the lane root.

| claim | before | after | counting command | measured against |
|---|---|---|---|---|
| R64-C1 | `grep -c kv-store-grpc corpus/evidence/round52/graders/executed17.lst` → 0 (rc 1); network-service executed 0 of 8 | `CHECK ok cases=5`, `PREDICATE R64-C1 pass`, rc 0; vectors K1 P/P/P/P/P/P/P, K2 F/P/F/F/F/F/F, K3 P/P/P/P/P/F/F, K4 P/P/F/F/F/F/F, K5 P/P/P/P/F/P/F | `python3 plans/round64_c1_kvstore_probe.py --check-receipt corpus/evidence/round64/kvstore-probe.txt; echo $?` | `7c2217ed` |
| R64-C2 | committed gate on the out-of-root fixture: `PREDICATE R63-C2 pass`, rc 0, `resolved=2` (`escape-red-before.txt`) | `DETAIL escape=/home/vgpnk/.config/uv/uv-receipt.json`, `PREDICATE R63-C2 fail`, rc 1 (`escape-after.txt`); selftest `SELFTEST pass` 4/4; real section `PREDICATE R63-C2 pass` (26/26 after the SKILL flip) | `python3 plans/round63_gate_checks.py --selftest --work <scratch>; echo $?` and `python3 plans/round63_gate_checks.py depth --skill SKILL.md --receipt corpus/evidence/round62/class-survey.txt --root .; echo $?` | `7c2217ed` |
| R64-C3 | `SWEEP files=65 trio_open=36 addendum=0 red=29`, `PREDICATE R64-C3 fail`, rc 1 (`sweep-red-before.txt`, clean clone at `859ac24f`); README rows for 57–62: 0 each | `SWEEP files=65 trio_open=36 addendum=29 red=0`, `PREDICATE R64-C3 pass`, rc 0 (`sweep-after.txt`); at the tip `files=66 trio_open=37 addendum=29 red=0`, `PREDICATE R64-C3 pass` (`sweep-at-tip.txt`); README rows 1 each for 57–62 | `python3 plans/round64_trio_sweep.py --sweep --lane .; echo $?`; `for n in 57 58 59 60 61 62; do grep -c "lessons/round-$n.md" corpus/README.md; done` | `7c2217ed` / `21b13dc7` |
| Standing | `landcheck` FAIL (`MISSING 2`) | `LANDCHECK PASS n=4`; `PREDICATE R52-C2 pass`, `MISSING 0`; `grader.py` `CHECKS n=733 mismatches=0`; census exit 0 | `python3 plans/round56_landcheck.py --lane .; echo $?`; `python3 plans/round52_c2_registry.py --lane .`; `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` | `7c2217ed` |

Rows in `corpus/SOURCES.md`: before 222, after 224 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Census: `validate` exit 0 at round start (`frontier/census-start.txt`) and at round end (`frontier/census-end.txt`); 22 W04 duplicate-URL warnings both times (pre-existing; the two new rows add none).

## Sources & frontier

- **SOURCES rows before → after:** 222 → 224 (`grep -cE` above). **Rows added by tier:** A = 2 (S230 `code`, S231 `docs`), B = 0, C = 0. **Rows touched old→new:** none (no status, recheck or used-by change to an existing row). **Rows opened and verified live this round:** S230 (curl at the pin, sha `115de2e9…`, `cmp` byte-identical) and S231 (curl, sha `d6867610…`). Both re-opened by a second seat (SourceReview), verdict VERIFIED.
- **Sourced claim:** C1 rests on S230 and S231; the knowledge entry opens with `source:` citing both.
- **Frontier rows advanced:** the Frontier entry "Agentic benchmark task-spec audits" gains a partial discharge for the `kv-store-grpc` scoring code (one task, one class); the network-service class moves from 0 to 1 executed member of 8. The `pypi-server` member stays not counted (R63-C1 MISS of record, unchanged).
- **Assimilation:** none. Reason: `merge/kengaku` mass id drift (L0 `kengaku | round-54`) remains open; the considerthese 2026-10-26 proposal 3 is served by the round-62 census and this round's probe, so it was not re-adopted.
- **Lesson:** `corpus/lessons/round-64.md` (Gate; Mistakes; carried).

## Trend verdicts

These are the lane's verdicts, subject to the non-author closure.

- **expansion: improved.** One TB2 grader of a new mechanism class (a gRPC service) executed offline end to end with a frozen predicate, and two sources admitted. Evidence: `corpus/knowledge/tb2-kv-store-grpc-offline.md`; `corpus/evidence/round64/kvstore-probe.txt`; SOURCES 222 → 224. Caveat: one of eight class members.
- **quality: improved.** Twenty-nine knowledge entries that were stale at round 62 (the trio gate's red list) each carry a dated re-verification addendum with the command and observed result, and every re-verification re-runs on the committed bytes (`sweep-after.txt`, `addenda-normalization-diff.txt`). No admitted entry was found false. Named, not repaired: the openings stay red under the trio gate (CORPUS.md forbids in-place rewrites).
- **discernment: improved.** The non-author FreezeReview caught a counter that passed the forbidden repair before any after-data existed (`openedit-sim.txt`); the round's gate decisions were spot-checked by non-author seats (agree on admits, one disagreement on C3 that became a lesson and QUALITY Q46 with its selftest leg, shown red). Evidence: `corpus/lessons/round-64.md` `## Gate`, `corpus/QUALITY.md` Q46.

Scores: depth 10 (held), calibration 10 (held), operability 10 (held), freshness 10 (held), adjacency 9 (held), novelty 8 (held), coverage 7 (held at the L0 cap). **One capability enters** (`offline-network-service-grader-probe`). No axis harmed.

## Landed changes — integrity notes

- Post-freeze changes are dated in Amendment A1 (`plans/round-64-claims.md`). No predicate sentence, leg vector, control, kill rule or counting command was changed.
- Two tool-environment facts changed the receipt of record for C1: the install step was hardened and the battery re-run under it. The pre-hardening receipts are kept; the entry and the lesson say so, and state that determinism is claimed only for the pre-hardening pair.
- One entry (`bench-arena-round12-ladder.md`) gained a final newline on its last line by the append; its prior bytes remain a byte-prefix (`append-only-prefix-check.txt`).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` → only `.scratch/` entries (`run13-state.json`, `run15-kernel.py`, and the modified `goal-20261103-hyaku-run15.md`, `run15-state.json`). These are orchestrator-owned run state and were not touched. No misroot from this round's seats; no fleet-root file was copied or deleted.

## Round shape and seats

- **Shape:** one v1 wave, 15 seats (`w1-results.json`; `seats` 15), inside the band 8–16. The L2 floor is met inside the wave. The validator refuses a planner seat; the L1 holds the planner role (orchestrator ruling). No residual call; no replacement seats.
- **Role mix:** executor 5, scribe 2, scout 1, connector 1, reviewer 2, critic 1, mutation-tester 1, revenger 1, sentinel 1.
- **Attack share:** reviewer 2 + critic 1 + mutation-tester 1 + labrat 0 = 4/15 = 26.7% (≥25%). The revenger and sentinel seats are not counted as attack roles under the frozen rule.
- **Connectors:** 1 (≤2).
- **Dead seats:** none. 15/15 settled with output. Every seat's report is in `.ufo/waves/round-64/w1/`.
- **Routing:** no model was passed by the L1; seats kept their captured routes.

## Stale-lane

Stale-lane: none. The round's mission closes with this report; no other mission of this lane is open.

## Tool installs (RULES.md: tool, version, channel, reason)

- `grpcio` 1.85.1 and `grpcio-tools` 1.85.1 — PyPI via `uv pip install` into scratch venvs (`uv` 0.13.0 at `~/.local/bin/uv`, pre-existing). Reason: the grader's runtime for the offline run; a scratch-only venv, not a system install. The installs are the probe's one network-touching step, now under a scratch-rooted environment.
- No pacman transaction (paused host-wide). No other installs. `bwrap` 0.13.1, python 3.14.8, `ss`, `curl` 8.23.0 pre-existing.

## Open L0 questions (carried, routed around)

- `kengaku | round-25/33/51` — coverage cap; nothing assumed answered.
- `kengaku | round-56` — the L2 surface on this host and the ledger host column.
- `kengaku | round-63` — admit the amended K2 stderr detector? R63-C1 stays MISS; run 1 is not re-scored.

No new L0 question is needed this round. The SiblingOverlap seat routed five contested-scope items to siblings; none is an operator decision (`.ufo/waves/round-64/w1/SiblingOverlap/sibling-overlap.md`).

## Inherited state

- The round-63 orchestrator marker `.ufo/waves/round-63/w1.ready.dispatched` and the round-64 markers `w1.ready.dispatched` and `w1.ready.partial` are orchestrator-owned and untracked; not committed.
- No uncommitted lane-authored work remains (`git status` → clean except those markers).

## Verifications this round

- Frozen counting commands re-run on the round commit and the tip (table above).
- `sources-census.sh validate` exit 0 at round start and end.
- The 29 appended addenda: byte-prefix check 29/29; re-verification commands re-run by the repair seats on committed bytes (`SweepRepairA/`, `SweepRepairB/` `*.reverify.txt`).
- The probe's selftest on the landed bytes: `SELFTEST pass`, rc 0 (`corpus/evidence/round64/selftest.txt`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  SKILL.md (grader-class decision table, 16 rows; network-service row flipped with dated evidence this round)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  LOG.md (round 64 entry: trigger = R64-C1 predicate; action = hardened offline battery of the kv-store-grpc grader; outcome = `PREDICATE R64-C1 pass`; pointer = `corpus/evidence/round64/kvstore-probe.txt`)
- [~] Instructions executable by an agent without oral context
  corpus/lessons/round-8-aggregator-box3-coldrun.md:48 (unchanged this round; not re-run)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  PROVINCE.md (round64 admission paragraph; the gRPC-in-sandbox pattern routed as non-overlapping with kama)

No `[x]` is written: no non-author verifier has checked any box.
