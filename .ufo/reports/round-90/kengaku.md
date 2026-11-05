# kengaku — round 90 (hyaku run 15, attempt 1, 2026-11-05)

Lane `kengaku-shokunin`, branch `master`. Lane tip at report time: `8f5f9afda9489700cf6429122d10d3add3df63c0` (`git -C kengaku-shokunin ls-remote origin refs/heads/master` prints the same hash). Round verdict: **not admitted** — R90-C1 and R90-C2 verify on their frozen predicates; R90-C3 is not met (honest stop; the claim is reported, not reshaped).

## Work performed

**Declared claims (frozen at commit `45171d23`, text in `plans/round-90-claims.md`).**
- **R90-C1 — coverage** (lowest non-retired axis, held at its L0 cap 7): an eighth located offline replay of the Terminal-Bench 2.0 grader `merge-diff-arc-agi-task` over eight frozen cases (`plans/round90-cases.json`, counter `plans/round90_c1_replay.py`, probe `plans/round90_polydiff_probe.py`). Count move: ledger executed 33 → 34 of 88.
- **R90-C2 — calibration** (held at ceiling 10): the counters' pins moved out of the counter bytes into `plans/counter-pins-r90.json`, checked by `plans/round90_counter_pin.py` over the six frozen instruments and the round-89 record-table blob `163f2843…`.
- **R90-C3 — operability** (held at ceiling 10) with capability row `routed-findings freeze gate`: `plans/round90_burndown.py` over `corpus/routed-findings.jsonl`, the freeze rule for round N (refuse while a finding opened before N−2 is pending), and the triage of every pending row. Considerthese item 1 (`considerthese/2026-10-26.md`) mined and implemented here.
- No exploratory claim. Frontier step: S279 admitted and S280 rejected; C1 rests on S279.

**Work items, with evidence pointers.**
- *Protocol and state load:* `skill://shokunin`, the canonical `PROTOCOL.md`, `MISSION.md`, `AXES.md`, `CORPUS.md`, `LEARNING.md` (kimi-shokunin checkout), the lane `SCORECARD.md`, `PROVINCE.md`, `corpus/lessons/round-89.md`, `corpus/lessons/round-89-verifier-spotcheck.md` (the outside spot-check of round 89: its six routed defects R89-D1…D6 are answered in LOG.md, below), the operator's `RULES.md` (read; no installs were made).
- *Frozen claims and case table:* commit `45171d23`, before any instrument. Eight predicted vectors derived from the captured grader bytes (`corpus/evidence/round52/graders/merge-diff-arc-agi-task/tests/test_outputs.py`, sha256 `2754ba6c…85c149`): `PPPPP, FFPPP, PFPPP, PPFEE, PPPEE, PPPPF, PPPPE, PPPPF`.
- *Instruments and pin ledger:* commit `664435cf` (`plans/round90_polydiff_probe.py`, `plans/round90_c1_replay.py`, `plans/round90_counter_pin.py`, `plans/round90_burndown.py`, `plans/counter-pins-r90.json`). The probe's first smoke returned `observed=P/P/P/P/P` with a `/` separator and rc 1: a format bug, fixed with `"".join`, not a verdict (lesson M6).
- *Receipt and ledger flip:* commit `a2b22609`. `corpus/evidence/round90/merge-diff-probe.txt`: `LANE_TIP 664435cf…`, `WORKTREE clean`, `EXIT 0`, `cases=8 legs=40 mismatches=0`, `PREDICATE R90-PROBE pass`; `plans/grader-population-ledger.json` gains one row (`merge-diff-arc-agi-task`, executed, round 90) and nothing else (`git diff --stat`: 5 insertions, 2 deletions).
- *Sources:* S279 (the grader, admitted; fetched live today, HTTP 200, 3034 B, byte-identical to the capture by `cmp`; located quote line 13 `assert git_path.exists(), "Git repository does not exist in /app/repo"`), and S280 (`tests/test.sh`, rejected: a network-bound verifier wrapper with no grader semantics beyond S279; fetched live, HTTP 200, 620 B, byte-identical). Commit `9cf98d90`.
- *Triage of the routed-findings ledger (C3):* 34 resolution rows (6 closed with evidence, 23 refused as the lane's own recorded `accepted-risk` dispositions, 4 blocked on other owners, 1 open) and 46 seed rows for rounds 83–89 (14 closed with a located evidence string, 29 open, 3 blocked), appended to `corpus/routed-findings.jsonl` (133 → 213 rows; 80 insertions, 0 deletions). The drafts are the wave's ExecC3Triage output (`.ufo/waves/round-90/w1/ExecC3Triage/`), and this lane took them as its record; the six closes are the seat's re-derivations and were not independently re-verified by the L1 (the round spot-check samples them). Commit `9cf98d90`.
- *Lesson:* `corpus/lessons/round-90.md` — Gate (S279 admit with located quote, S280 reject with flip), Mistakes M1–M11 (class · evidence · captured-by · fix), the triage record, routed items, and honest limits. Commit `9cf98d90`.
- *Wave w1 — one v1 wave, 12 seats, policy band 8–16* (`w1-spec.json`, `w1-dispatch.json`, `w1.ready`; results `.ufo/waves/round-90/w1-results.json`; validator registry `.ufo/scopes/kengaku-r90-w1/swarm-registry.json`). Seats: ExecC1Battery, ExecC2Battery, ExecC3Triage, ExecNoWork, ExecLedgerFlip (executors); ScoutS279 (scout); ConnectorOverlap (connector); ScribeR90 (scribe); ReviewerPredicate (reviewer); CriticFalsify (critic); MutTesterR90 (mutation-tester); SentinelForge (sentinel). Verdicts (each seat's own output at `.ufo/waves/round-90/w1/<seat>/`):
  - **ExecC1Battery**: all seven controls match their expectation; findings F1 (`executed=` printed 1 under a failing predicate; the verdict stays `fail`) and F5 (a probe-observed L1–L6 pass on a forged probe; L8 is the only catch, as the claim's honest limit says).
  - **ExecC2Battery**: eleven controls ran with observed rc matching their stated expectation, except the BASE mispredict (rc 2, not 1); F3: "external" overstates an anchor that is in-tree.
  - **ExecC3Triage**: triage drafts; "C3 PASS IS UNREACHABLE" under the frozen gate (a superseded malformed row still emits DEFECT; reproduced in a fixture).
  - **ExecNoWork**: do-nothing controls at BASE fail as frozen (C1 rc 1, C2 rc 2, C3 rc 1); ledger-only C3 variants: `freeze=admitted` printed with check failures; `seeds_83_89` counts unverified rows (HIGH, both routed).
  - **ExecLedgerFlip**: ledger flip verified (only the merge-diff row changes; 34 executed; the five class cells match); census note: `--file` resolves `used-by` against the file's directory, so the census must run with `--root`.
  - **MutTesterR90**: 35 single mutants (C1 17, C2 7, C3 11) plus two composites; 15 killed by the committed batteries, 20 survive them; the C3 `closed-check-fails` selftest case is red by `AttributeError`, not by its check (F-C3-1).
  - **SentinelForge**: forgeries through the production path: H-1 (checker-only edit passes C2, undisclosed); H-2 (check override and any-blocker `refused` admit a freeze, 35 fabricated closes → `freeze=admitted`); H-3 (one-commit echo probe plus `TRUSTED_TOOL_SHA` rewrite passes C1, disclosed class); H-4 (one-commit pin-ledger rewrite passes C2, disclosed residual).
  - **ConnectorOverlap**: 20 sibling lanes scanned; no sibling implements a freeze refusal on routed-finding age; sha pins exist in kumitate, tameshi, kaidoku and revenger (none absorbed); route-outs listed in its overlap file.
  - **ScribeR90**: drafts with named placeholders; placeholders were filled by this lane from measured facts, not from the drafts.
  - **ReviewerPredicate**: traced its own red selftest to its invocation from the fleet-root cwd (not an instrument defect), and found the fail-open fallback below.
  - **CriticFalsify**: critique at `.ufo/waves/round-90/w1/CriticFalsify/critique.md` (findings F-1…F-17; C2 and C3 "not admit as written"; F-13: an unblocked open row opened after round 88 can yield `PREDICATE pass`).
  - **ScoutS279**: gate note at `.ufo/waves/round-90/w1/ScoutS279/gate-note.md`; its line-13 quote, byte comparison and `test.sh` reject match this lane's own fetch.
- *Misroot sweep (before the report; lesson M12):* two seat probe files (`run_check_probe.py`, `run_check_probe2.py`, ReviewerPredicate) were at the fleet root; copied byte-exact into `kengaku-shokunin/` (`cmp` ok), committed under the lane (`a0d57153`), fleet copies deleted. Recorded as lesson M12. `.scratch/run15-state.json` (orchestrator) and another lane's `.ufo/l0-questions.md` line were not touched.
- *Measurement tip:* all counters were run at `9cf98d90` (see Before → after). Counter and pin bytes in `plans/` are byte-identical to commit B at that tip (the only `plans/` change after B is the ledger flip that C1 requires; `git diff --stat 664435cf 9cf98d90 -- plans/round90_*.py plans/round89_*.py plans/round88_claim_figures.py plans/counter-pins-r90.json` prints nothing).

## Landed changes

| commit | content | LOG / SCORECARD pointer |
|---|---|---|
| `45171d23` | freeze: `plans/round-90-claims.md`, `plans/round90-cases.json` (commit A) | LOG Round 90 entry (`LOG.md:3408`) |
| `664435cf` | instruments and external pin ledger (commit B) | LOG Round 90 entry |
| `a2b22609` | receipt `corpus/evidence/round90/merge-diff-probe.txt`; ledger row executed (commit C) | LOG Round 90 entry, C1 |
| `9cf98d90` | S279 admit, S280 reject (`corpus/SOURCES.md`); routed-findings triage 34 + 46 rows (`corpus/routed-findings.jsonl`); `corpus/lessons/round-90.md` (measured tip) | LOG Round 90 entry, C3 and Sources; lesson Gate and Mistakes |
| `e2c73b68` | LOG Round 90 entry (`LOG.md:3408`); SCORECARD Round 90 section (`SCORECARD.md:4189`); `corpus/QUALITY.md` Q68 and Q69 (grounded in lesson M5 and M8); wave-1 evidence | LOG Round 90; SCORECARD Round 90 |
| `4c5d05b6` | wave-1 settled evidence (results, ScoutS279 gate note) | — |
| `a0d57153` | misroot recovery: two ReviewerPredicate probe files | lesson M12 |
| `93ff3240` | wave-1 swarm registry (validator record) | — |
| `8f5f9afd` | lesson Mistakes M12 (misroot recorded) — lane tip | lesson `corpus/lessons/round-90.md` |

L0 questions appended and pushed in fleet commit `1258e5e5` (four lines; see the L0 section).

## Before → after measurements

Counting commands: `python3 plans/round90_c1_replay.py --lane . --rev REV --work DIR`; `python3 plans/round90_counter_pin.py --lane . --rev REV --work DIR` and `--selftest --work DIR`; `python3 plans/round90_burndown.py --lane . --rev REV --work DIR --freeze-round 90` and `--selftest --work DIR`; census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`. BASE `dcdd494e`; measured tip `9cf98d90` (transcript `.ufo/waves/round-90/L1/measured-tip.txt`; BASE `.ufo/waves/round-90/L1/base-batteries.txt`).

**R90-C1 (coverage).** Before (BASE `dcdd494e`): `TARGET executed_rows=33 member=merge-diff-arc-agi-task located=1 executed=0 cases=0 legs=0 mismatches=0 defects=10`, `PREDICATE R90-C1 fail`, rc 1. After (tip `9cf98d90`): `TARGET executed_rows=34 member=merge-diff-arc-agi-task located=1 executed=1 cases=8 legs=40 mismatches=0 defects=0`, `PREDICATE R90-C1 pass`, rc 0. Ledger: executed 33 → 34 of 88; `git-plumbing` 1 → 2 of 3; `serialization-schema` 3 → 4 of 10; `file-artifact` 24 → 25 of 76; `stdout-inspection` 9 → 10 of 29; `subprocess-exec` 11 → 12 of 45. Mispredict: defects predicted 5, measured 10 (seven L7-ledger lines — the row, the executed total and five class cells — plus absent-input lines for L4, L8 and L1). Verdict: **met on the frozen predicate**; coverage stays held at its L0 cap 7 (the count moved, the score did not).

**R90-C2 (calibration).** Before (BASE): `DEFECT SETUP unreadable plans/counter-pins-r90.json`, `PREDICATE R90-C2 could-not-evaluate`, rc 2 (frozen prediction: rc 1 with `PIN-MISMATCH absent`; mispredict recorded; fail-closed holds). After (tip): `RECORD-TABLE blob=163f284316141a83 matched`, `PINS checked=7 matched=7 mismatched=0`, `PREDICATE R90-C2 pass`, rc 0; selftest `cases=5 red-green-ok=5`, rc 0. Wave controls: one-byte counter mutation rc 1; one-byte record-table mutation rc 1; absent path rc 1; incomplete set (1 of 6 and 5 of 6) rc 1; tampered pin rc 1; positive rc 0. Verdict: **met on the conjunction its frozen predicate states** (pins and selftest). Residual understated, as the claim's own wording did not state: the checker is unpinned (SentinelForge H-1; CriticFalsify F-8); the record-table constant lives in the checker, so the ledger's `record_table` entry is decorative (CriticFalsify F-9); the PREDICATE line omits the selftest (lesson M5). Score held at ceiling 10.

**R90-C3 (operability and capability).** Before (BASE `dcdd494e`): `ROWS total=133 valid=132 invalid=1 superseded=0`, `DEFECT line 125: R82-F1`, `freeze=refused oldest_pending_round=39 pending=33 malformed_unresolved=1 seeds_83_89=0 resolutions=0`, `PREDICATE R90-C3 fail`, rc 1. After (tip `9cf98d90`): `ROWS total=213 valid=212 invalid=1 superseded=34`, `DEFECT line 125: R82-F1`, `freeze=refused oldest_pending_round=51 pending=37 malformed_unresolved=1 seeds_83_89=46 resolutions=34 checks_run=117`, `PREDICATE R90-C3 fail`, rc 1. Selftest `cases=7 red-green-ok=7`, rc 0. Predicted after: `freeze=admitted pending=0`; measured `pending=37` (29 open seeds, 3 blocked seeds, the 4 blocked R51 rows, open R82-F1): mispredict. Verdict: **NOT met on its frozen predicate.** The freeze is refused by the blocked R51 rows (opened 51), the seeds opened 83–87 that remain open, and the malformed R82-F1 row, whose DEFECT blocks the PREDICATE by construction (lesson M5). The capability row `routed-findings freeze gate` is entered in SCORECARD because the refusal ran and reproduced at BASE and at the tip; the claim's pass is not established.

**Controls and batteries (all re-run after the last instrument commit; transcripts under `.ufo/waves/round-90/`).** Do-nothing at BASE: C1 rc 1, C2 rc 2 (fail-closed), C3 rc 1 (`L1/base-batteries.txt`). C1 ledger-only rc 1 (`L1-receipt`), forged tip rc 1 (`L3-tip`), forged probe rc 1 (`L8-tool`), positive probe rc 0 (`w1/ExecC1Battery`). C2 controls as above (`w1/ExecC2Battery`). C3 selftests 7/7 at BASE and at the tip; the C3 `closed-check-fails` case is red for an unrelated `AttributeError` (MutTesterR90 F-C3-1; routed).

## Sources & frontier

- **Census before → after** (the counting command, measured at round start and at the tip): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` → exit 0, `kengaku ok` (270 rows) before; exit 0, `kengaku ok` (272 rows) at `9cf98d90` and after. Manual counts: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 270 → 272.
- **Rows added by tier:** S279 tier A (member replay only, admitted); S280 tier A (rejected, verifier wrapper). Tier histogram: A 240 → 242, B 24 → 24, C 6 → 6. Status histogram: mined 245 → 246, queued 8 → 8, rejected 17 → 18.
- **Rows touched old→new:** none (no existing row's status, recheck or used-by changed).
- **Frontier rows advanced:** S279 `mined` (cited by `corpus/lessons/round-90.md`, `corpus/evidence/round90/merge-diff-probe.txt`, and the C1 claim); the ledger's `merge-diff-arc-agi-task` executed (`plans/grader-population-ledger.json`).
- **Sourced claim:** R90-C1 rests on S279 (line 13, and the five test functions at lines 10, 16, 34, 40, 52).
- **Mistake mined:** M1–M11 in `corpus/lessons/round-90.md` (`## Mistakes`), each with class, evidence, captured-by and fix; M5 (predicate-implementation gap) and M8 (selftest red for the wrong reason) are the ones the wave surfaced after scoring and are routed, not fixed.
- **Knowledge entries admitted:** none. `corpus/knowledge/` untouched.
- **considerthese:** item 1 (`considerthese/2026-10-26.md`, routed-findings burn-down) mined and implemented in part by C3 (the ledger, the gate and the triage); the freeze wiring awaits round 91 and the gate's defects are routed.
- **Assimilation:** none. `merge/kengaku/` stays held by L0 `kengaku | round-54`; nothing adopted.
- **Discernment item from round 89:** R89-D4 (the round-89 lesson had no reject row) is closed by this round's gate: one admit (S279) and one reject (S280) with reasons in the lesson Gate. The non-author check of those decisions is the round-90 spot-check.

## Trend verdicts

- **expansion: unchanged.** No `corpus/knowledge/` entry was admitted (`git diff --stat dcdd494e 9cf98d90 -- corpus/knowledge` prints nothing). The eighth executed member is coverage counted by the ledger, not expansion; S279 is a source row whose entry does not yet exist.
- **quality: unchanged.** No admitted entry was re-verified or superseded. Q68 and Q69 were added to `corpus/QUALITY.md` (criteria, grounded in lesson M5 and M8, executable halves routed); they are not a measured quality move. The routed-findings triage moved 33 pending rows to recorded states; that is a bookkeeping move (the freeze count does not measure fixing; see the L0 line).
- **discernment: unchanged.** The round's gate decisions (S279 admit, S280 reject) have no non-author verdict yet, and the lane-dispatched seats are the lane (LEARNING.md), so their findings are not a non-author judgment. The wave's findings did show the gate's own predicate gaps (M5, FE-1, F-13), which is evidence that the instruments' self-checks are weaker than their claims; that is recorded as a finding, not credited as discernment.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md (lane author assessment; no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:3408 (Round 90 entry: the eighth replay executed at the tip with its receipt, `corpus/evidence/round90/merge-diff-probe.txt`)
- [~] Instructions executable by an agent without oral context — corpus/lessons/round-8-aggregator-box3-coldrun.md:48
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md:151

## Stale-lane

Stale-lane: no other mission of this lane is open. Attempt 1 of round 90 is the only open mission and it has settled; `.ufo/watchdog.log` shows no `lane-dead-no-report kengaku round=90` line at the time of writing.

## Tool installs

None. The operator's tooling directive was read first (`/home/vgpnk/.omp/agent/RULES.md`); this round installed or upgraded nothing. Seats reported no installs either (`uv` and `bwrap` were already present on the host). No pacman transaction, no sysctl change, no host-service change.

## Host and environment

- `/proc/sys/user/max_user_namespaces` read **122865** at every probe run and in every receipt (`HOST_USERNS` line, added this round from round-89 Mistake 5). The lane changed no host setting. No kernel-level need arose this round.
- Scratch under `/fast/scratch/hyaku/kengaku-r90/`; the seats removed their trees after copying receipts. The L1 removes `kengaku-r90/` after this report lands.

## Wave shape and seats

- One v1 wave, **12 seats** (band 8–16; the L1 holds the planner seat, which the validator rejects as a swarm role). Roles: executor 5, scout 1, connector 1, scribe 1, reviewer 1, critic 1, mutation-tester 1, sentinel 1. Attack seats (reviewer, critic, mutation-tester, sentinel) 4 of 12 = 33 %, which meets the ≥ 25 % floor. Connector seats 1. No residual call.
- The frozen claim text's round-shape line (executor 3 plus labrat 1, attack 5 of 12) does not match the dispatched spec (executor 5, no labrat). The spec is the one dispatched; the claim text is routed to the L0 question on frozen-text contradictions.
- **Dead seats: none.** The results file (`w1-results.json`) holds a final output for all 12 seats; the file carries no per-seat status key.
- **Answering models** are not recorded in the results file and are not claimed here.
- **Name collision (orchestrator notice).** The `agent://CriticFalsify` read returned another lane's round-88 content (its files under `.ufo/waves/round-88/w1/CriticFalsify/`). This lane's CriticFalsify seat wrote its own files under `.ufo/waves/round-90/w1/CriticFalsify/` (critique and evidence, all round-90 subjects, committed in `e2c73b68`); this report uses those files, not the `agent://` read. The seat name recurs across lanes, which the orchestrator already flagged.

## Round admission and open claims

- R90-C1: verified on its frozen predicate. R90-C2: verified on the conjunction its frozen predicate states; its stated residual is understated (checker unpinned). R90-C3: **not met**.
- No axis harmed: coverage held at 7, calibration at 10, operability at 10; novelty 8, depth 10, freshness 10, adjacency 9 held.
- The round is **not admitted** on C3. Per the protocol this is an honest stop: C3's predicate is not met at the measured tip, and the instrument defects that block its pass are routed to round 91 under a new frozen predicate, not repaired after the wave began scoring (the frozen kill rule voids C2 on any post-B edit to a pinned counter).

## Open L0 questions (appended and pushed in `1258e5e5`)

- `kengaku | round-90 | R90-C3 … measured NOT MET … Decision: amend the instruments under a new frozen predicate in round 91, or reopen R90-C3 now?`
- `kengaku | round-90 | Pin residual for R90-C2 … accept in-tree pins as the fleet standard, or require an anchor outside the tree?`
- `kengaku | round-90 | Frozen-text contradictions in round-90-claims.md … the tip rule vs the ledger flip; the round-shape line vs the dispatched spec.`
- `kengaku | round-90 | Triage mapping … 23 accepted-risk rows restated as refused; accept as decided for the freeze gate, or keep pending?`

## Routed to round 91

1. Instrument conformance under a new frozen predicate: C3 pass path for a superseded malformed row; freeze refused on any failing check; the seed clause `seeds_83_89 >= 6` in the PREDICATE line; each override check printed and the base check also run; the `--file` stand-in given a root (F-C3-1); checks run once per finding; the kill-rule clause for an unblocked pending row (F-13). Q68 and Q69 name these.
2. C2: the selftest in the predicate path; the checker and the record-table constant pinned (or moved to a pinned gate); the fail-closed rule for absent frozen inputs (M9); `PIN-OK` emitted or dropped from the prediction; the ledger's `record_table` entry read by the checker.
3. C1: the `executed=` field 1 only when the predicate passes (F1); the stamp's `TOOL_SHA`, `CASE_TABLE_SHA` and `HOST_*` fields checked (SentinelForge 1b); the L6 sandbox-outage path classified as could-not-evaluate (CriticFalsify F-7).
4. Triage backlog: the 29 open and 3 blocked seeds need closures or named owners; R82-F1 needs its QUOTE_RE repair (`plans/anchor_line_check.py`, round 83's routed item) with its own counter; R82-V8 reads the fleet repo through `origin.parent` (path-dependent: passes in the lane, fails in clones).
5. Coverage: the next offline member from ScoutR89's class arithmetic that the ledger's captured bytes show offline-clean.

## Work not done (named)

- The C3 pass, the freeze wiring for round 91, and the instrument amendments above are not done this round (routed).
- No knowledge entry was admitted; assimilation of `merge/kengaku/` remains blocked by L0 `kengaku | round-54`.
