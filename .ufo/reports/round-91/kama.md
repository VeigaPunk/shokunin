# kama — round 91 report (L1 KamaR91a2, attempt 2)

Lane repo `/home/vgpnk/Projects/shokunin/kama-shokunin`, branch `master`, final pushed hash
`e4747a7add602f34eb25379d38c67faa57b3b926` (`git ls-remote origin refs/heads/master` prints it). Base
`c06838c5b94576971ea33ac465bf2c935e9037f9`; freeze `9a41912a598cad00f7ff08391586a0ef3732bbed`.

## Work performed

Declared claims (frozen in `plans/round-91-claims.md` at `9a41912a`, controls committed before freeze):
**C1 — operability** (capability `answer-time-bound`, sourced S592): a large `/v1/models` answer under the 4 MiB cap is
graded in bounded (linear) time. **C2 — depth** (lowest axis, 7; sourced S593–S595): SKILL §Serving timeout and limit
thresholds, rows bound to pinned upstream lines, kill rule K2 = a non-author reviewer finds a misstated row.

- Inherited from attempt 1 (`.ufo/watchdog.log`: `lane-dead-no-report kama round=91` 20:22:46): freeze `9a41912a`,
  C1 implementation `3decfa36` (`tools/kama-probe.sh`: one awk pass `AWK_NORM` with `ENVIRON`, `router_match`,
  `paste -sd,`), C2 table + S592–S595 + `corpus/knowledge/serving-thresholds.md` + r90 R2 correction `3f317ecd`. All
  re-verified this attempt: tip re-measurements `.ufo/waves/round-91/measured/c1-tip.out`, `c2-tip.out` (rev `3c4f6a1e`,
  both exit 0). Inherited untracked `w1-spec.json`/`w1-dispatch.json`/`w1.ready`/`measured/c2.out`: reused and committed.
- Wave `w1` (12 seats) ran and settled: `.ufo/waves/round-91/w1-results.json`, reports `.ufo/waves/round-91/w1/*.md`.
- C2 **K2 fired**: `w1/RV02ThresholdRows.md` lines 40, 52-61 (BLOCKER-1: T07 states `n_parallel` 1 from `common.h:464`;
  llama-server b12177 sets `-1` auto at `common/arg.cpp:1373`, resolved to 4 slots at `server.cpp:126-129`),
  corroborated by `w1/SC01SourceReopen.md` and by my own run of the pinned binary (`--help`:
  `-np, --parallel N number of server slots (default: -1, -1 = auto)`). C2 is recorded **not verified**.
- Dated corrections (rows unchanged): `SKILL.md` §Round 91 correction (T07 + six overreach rows + pin history),
  `corpus/knowledge/serving-thresholds.md` §Round 91 correction, `corpus/README.md` coverage correction — commit `3c4f6a1e`.
- New QUALITY criterion KQ146 (default must be the binary's own; `corpus/QUALITY.md:696-702`) with a falsifier that fails
  on T07: `.ufo/waves/round-91/measured/kq146-help-check.out` (`KQ146_ROW T07 … DISAGREE`, `disagree=1`, exit 1).
- Harm found and repaired: the C1 probe change staled the round-90 reason-row receipt (`measured/r90-reason-rows-stale.out`,
  `bound=0 receipt=stale`, exit 1 at `3c4f6a1e`; found by `w1/SC02QuadraticSweep.md` F6). Re-captured with identical 24
  (cell, reason, verdict) triples (`measured/r90-reason-recapture.out`, prior copy `r90-reason-cells-prior.jsonl`), re-bound
  24/24 at `ba91b699` (`measured/r90-reason-rows-tip.out`, exit 0) — commits `ba91b699`, `d9ce93fc`.
- Record: SCORECARD §Round 91 (claims, measured results, canonical capability list with `answer-time-bound`, disclosed
  limits), §Planned (round 92), banner/calibration/coverage/depth rows; lesson `corpus/lessons/round-91.md`; LOG.md round 91;
  PROVINCE round-91 line — commits `3c4f6a1e`, `ba91b699`, `718018eb`, `96f645fe`, `75a875a6`.
- Terminal pre-report gate `.ufo/waves/round-91/measured/gate-final.out` (`# rev=75a875a6…`, committed `e4747a7a`):
  `PRE_REPORT round=91 arms=14 failed=1 uncommitted=0`, exit 1; sole red arm the carried `round75-instruments`
  (`bad_rows=19`, L0 open since r87).
- Planner seat: held by the L1 (validator rejects `planner`); no planning item rode a seat.

**Round shape:** ONE v1 wave, `w1`, 12 seats under `ufo-wave-policy.json`: reviewer 2, critic 2, mutation-tester 2,
executor 2, scout 2, connector 1, scribe 1; attack share 6/12; 0 dead. **Duplicate:** I validated and wrote `w1a2.ready`
(same 12 items, `w1a2/` out dirs) because `w1.ready` (l1 `KamaR91`) was marked `.partial.dead`; the orchestrator had already
re-spawned `w1` under my label (driver-side, orchestrator ruling). `w1a2` spawned 12 seats; the orchestrator cancelled 5
(RV01, MT01, EX01, EX02, SC02 `-2`); 7 finished and are kept as independent replicates (`w1a2-results.json`). Twin seats
shared scratch paths, and one `rm -rf` wiped its twin's files (every seat re-ran). Round total: 12 canonical seats plus a
duplicate of 12 (7 finished, 5 cancelled). No residual call.

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `9a41912a598cad00f7ff08391586a0ef3732bbed` | freeze: plan, counters, controls (attempt 1) | LOG §Round 91 |
| `3decfa36b0eba7e5197c034dd1547146bca1568a` | C1 probe linear-time grading | LOG §Round 91, C1 bullet |
| `3f317ecd211e80929c673e306e3230be287fdf20` | C2 table, S592–S595, knowledge entry, r90 R2 correction | LOG §Round 91, C2 bullet |
| `3c4f6a1ec9b0faa60b04d508f43fe6c8a4c92e1f` | record, corrections, KQ146 + falsifier, w1a2 evidence | LOG §Round 91 |
| `ba91b69970e9821a98715fae227cb9794179fa01` | w1 evidence, r90 receipt re-capture, lesson M4, tip receipts, census-end | LOG §Round 91 (lesson pointer) |
| `d9ce93fc9fe8bda66607525e0ec610869a8b4f74` | r90 reason-rows re-bound receipt | lesson M4 |
| `718018eb`, `96f645fe`, `75a875a6` | SCORECARD head caps / coverage / depth rows | LOG §Round 91 |
| `e4747a7add602f34eb25379d38c67faa57b3b926` | terminal gate receipt | — |

## Before → after measurements

| Claim | Counting command | Before (base `c06838c5`) | After | Measured commit | Verdict (author) |
|---|---|---|---|---|---|
| C1 operability | `python3 tools/round91-answer-time.py --repo . --rev <M> --work <scratch>` | `cells=12 mismatches=5 positive_mismatches=0`, exit 1 (`controls/c1-base.out`; T1/T2/T4/T5 killed at 120 s) | `cells=12 mismatches=0 positive_mismatches=0 probe=rev`, exit 0, all cells ≤ 2.1 s (`measured/c1.out`); tip same (`measured/c1-tip.out`) | `3decfa36b0eba7e5197c034dd1547146bca1568a` | verified (K1 0; K2 harm suites unchanged `measured/harm-M.out`; K3 counter unchanged). Disclosed: counter does not own the rule (w1 CR01, MT01); three super-linear paths remain, present at base (w1 SC02) |
| C2 depth | `python3 tools/round91-threshold-rows.py --repo . --rev <M2>` | `rows=0`, exit 1 (`controls/c2-base.out`) | `rows=14 bound=14 unbound=0 duplicates=0 engines=3 fetch_failures=0`, exit 0 (`measured/c2.out`) | `3f317ecd211e80929c673e306e3230be287fdf20` | **not verified** — K2 fired (T07 misstates; 6 overreach rows) |

Do-nothing and forgery controls ran before freeze: `controls/c1-f1-count-cap.out`, `c1-f2-exact-match.out`,
`c2-forgeries.out` (all exit 1).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.
  Start: exit 0, `kama ok` (`.ufo/waves/round-91/controls/census-start.out`). End: exit 0, `kama ok` (warnings W04 only,
  pre-existing) (`.ufo/waves/round-91/measured/census-end.out`).
- Rows 331 → 335 (`grep -cE '^ {0,3}\| S[0-9]{3,}' corpus/SOURCES.md` at base vs tip). Added by tier: A +4 (S592 POSIX awk,
  S593 llama.cpp `common.h` @ b12177, S594 Ollama `envconfig/config.go` @ v0.40.11, S595 vLLM `envs.py` @ v0.32.0); B 0; C 0.
  Tier totals now A 319, B 11, C 5. Rows touched old→new: none. Rejections recorded in the lesson Gate: GNU gawk manual
  (unreachable, rc=28) and SGLang v0.5.22 `server_args.py` (not mined).
- Sourced claims: C1 rests on S592; C2 on S593–S595. All four re-opened by wave seats SC01 and SB01 (digests equal).
- Frontier advanced: the engines' default timeouts/limits moved into the held reading rules (with the round-91 correction);
  SGLang v0.5.22 candidate rows T15–T22 staged in `w1/out/SC01SourceReopen/` (frontier, KQ146 first).
- Mistake mined: `corpus/lessons/round-91.md` `## Mistakes` M1 (struct default read as the binary's default; fix KQ146,
  shown able to fail by `kq146-help-check.out`), M2, M3, M4.
- Assimilation: none (frozen claims from attempt 1; §10 frozen-round clause). considerthese: not mined this round.
- Previous closure `corpus/lessons/round-90-verifier-spotcheck.md`: R2 fixed (`3f317ecd`); R5 addressed by C1; R1, R3, R4,
  R6 carried with dispositions in the lesson.

## Trend verdicts

- **expansion: improved** — new knowledge ground (the engines' default limits, S593–S595; the time bound in
  `probe-answer-bounds.md`, S592) and one capability (`answer-time-bound`, green at `3decfa36` and tip). C2's table is
  not verified, so its rows carry no verified credit.
- **quality: improved** — base T1/T2/T4/T5 killed at 120 s → ≤ 2.1 s with harm suites unchanged; the r90 reason-receipt
  staleness the change caused was found and repaired in-round; C2's misstatement is corrected with a dated note. Offset:
  C2 itself is not verified.
- **discernment: improved** — the frozen K2 rule fired on a row the counter called bound, and the lane records the miss
  instead of re-scoring; KQ146 converts it into a criterion with a falsifier that fails on exactly T07.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Serving timeout and limit thresholds + §Round 91 correction; no non-author verifier named.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 91; `.ufo/waves/round-91/measured/c1.out` (probe graded on 12 stub listeners).
- [~] Instructions executable by an agent without oral context — counting commands in `plans/round-91-claims.md` re-run by wave seats from text alone (`w1/RV01ProbeDiff.md`, `w1/SC01SourceReopen.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-91 line; `w1/CN01SiblingOverlap.md` (no sibling contradiction).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (no seat reported an install). Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
shows untracked `trail-ids.txt` (1 byte, `,`, 20:36) — content names no lane; not attributed to kama seats, left untouched.
Open L0 questions: none new; `round75-instruments` L0 (r87) still open.
