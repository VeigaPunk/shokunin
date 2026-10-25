# kengaku-shokunin — round 9 report

Child-repo commit: **`2575be6`** ("round-9", 45 files, +4750/−9), pushed to
`origin/master`; parent chain `f147a27` (round-7) → `3175e69` (aggregator's own
round-6 audit lesson, committed by the aggregator per `PROTOCOL.md`) →
`2575be6`. First commit under the lane identity
(`git config --local user.name` → `kengaku-shokunin`,
`user.email` → `kengaku@shokunin.local`). Working tree clean
(`git status --porcelain` → empty) at filing time.

## Axis selected — calibration (owned pair: novelty + calibration)

`SCORECARD.md` did not exist at `f147a27`
(`git ls-tree -r f147a27 --name-only | grep -c SCORECARD` → **0**) although
`AXES.md:26-32` makes it a per-repo contract and three sibling lanes already
had one. Scored against the repo, calibration was the lowest axis at **2**, on
four re-runnable breaches: no scorecard for 8 rounds; round 8 ran a 78-job probe
with **no ex-ante predictions** (`grep -ril predict /tmp/bench-r8
corpus/evidence/round8-horizon` → 0 hits, while rounds 5–6 filed 25- and
17-line prediction files) against `SKILL.md`'s own checklist item 1; the round-8
result was never analyzed, logged or committed (`grep -c -i 'round.8\|horizon'
LOG.md` → 0; `git ls-tree -r f147a27 --name-only | grep -c evidence` → 0); and
the landed evidence copy had `raw` stripped from all 258 non-meta records
(md5 `01547cfa…` vs run `df154cb5…`), destroying the failure-class evidence.

### Before → after (measured, `SCORECARD.md` carries the full table + rubric)

| Axis | Before | After | Counting evidence |
|---|---|---|---|
| **calibration** *(owned)* | 2 | **6** | prediction coverage 0/1 probes → **1/1** filed pre-hoc *and* scored; uncommitted+unlogged artifacts 4 files → **0**; scorecard rows with re-runnable pointers 0 → 7; `sha256sum -c corpus/evidence/round9-replication/predictions-r9.sha256.repo` → `OK` |
| **novelty** *(owned)* | 7 (unpriced) | **5** | prior-art verdicts with fetched URLs 0/4 claims → **4/4**; phenomena graded new **0/4**, instruments unmatched by named suites **2/4** |
| depth | 7 | 8 | `SKILL.md` 312 → 414 lines; anti-patterns 8 → 13; cited-source bullets 16 → 20; knowledge entries 18 → 21 |
| coverage | 5 | 6 | `PROVINCE.md` surfaces enumerated 0 → 8; README lessons rows 6/8 → **11/11**, knowledge rows 21/21 |
| operability | 3 | 4 | runnable in-repo files 0 → **11** (`find . \( -name '*.py' -o -name '*.sh' \) -not -path './.git/*' | wc -l`); one self-verifies offline: `python3 corpus/evidence/round9-fleet/test_harness.py` → exit 0 |
| freshness | 4 | 5 | round-9 `LOG.md` entries carry re-verification for every claim touched; endpoint re-probed (`/v1/models`, `/health` 200) |
| adjacency | 7 | 8 | contested overlaps named with owners 0 → 4; report-outs filed 3 |

Novelty was **lowered** by evidence, which is the point of the axis pair: the
scorecard now moves in both directions.

## Work performed

**1. Round-8 debt closed by pre-registered analysis** (3 executor L2s + critic +
mutation-tester). The 78-job probe (`corpus/evidence/round8-horizon/`, 268
records, `finish=stop` 258/258, 0 parse failures) is analyzed in
`corpus/knowledge/bench-arena-round8-horizon.md`:

- **A:** INC 7/10 > CKPT 1/10 ≈ MONO 0/10; 9/10 under convention-tolerant
  grading; **15 of 19** failing INC records are the MOV-zero convention (9
  dropped zero keys, 6 left the MOV source at its pre-MOV value), 4 genuine
  drift; all **5/5** INC error onsets are MOV turns; model-initiated recovery
  **0/16**; paired sign tests (problem = unit) INC>CKPT 7:1 p=0.0703,
  INC>MONO 7:0 p=0.0156, CKPT>MONO 1:0 p=1.0 — upper bounds at ESS≈0.54·n≈5.4.
- **B:** the manipulation **did not bind** — corrupt vs clean 0:3 discordant
  (p=0.25), `raw` byte-identical between arms in 3/8 problems per arm, 4/8
  corruptions erased by the tail ops, 2/8 fabricated `true_mid+5`, 1/8 on an
  untouched key → well-formed in **2/8**; hint null (1:1, p=1.0); the single
  `propagated` label is a frozen-key carry, and key-level retagging finds
  exactly **1** genuine propagation event, scored `other`. Claim (v) **blocked**.
- **C:** benign **0/4 strict** (shipped 1/4) vs conflict 4/4 and norule 4/4 with
  byte-identical final asks (476 chars, 296 prompt tok) → rule-integration cost,
  not transcript shape; effective n = 1–2 distinct generations per cell.
- **Fix-landing audit** of the round-8 critic's 16 defects against the code that
  shipped: **9 landed / 5 partial / 2 not landed** (#6 corrupted-key-exercised,
  #15 fixed op histogram) — `corpus/evidence/round9-fleet/critic.md`, line-cited.
- **Grader mutation battery:** 50 synthetic cases → 12 defect candidates, **1
  live** (`grade_c` computes `over_repair` then omits it from `ok`,
  `horizon.py:288`; `preserved` trusts self-declared violations, `:277-279`) →
  C-benign 1/4 is 0/4; parser fidelity 188/188 re-extractions.

**2. Predict→observe→score loop restored, with a mechanical ordering proof**
(labrat L2). Fresh seeds (`2000+pid*29`, pids 101–108), a new `A-CKPT710` dose
cell, 28 filler requests, 284 records, 0 errors —
`corpus/evidence/round9-replication/`, `corpus/knowledge/bench-arena-round9-replication.md`:

- Ordering: predictions hashed **before** the first request — sha256
  `2a4f62ef…`, `ordering.log` 21:17:48Z (before/after), first `request_ts`
  21:17:58Z. Re-checkable without `/tmp`:
  `cd corpus/evidence/round9-replication && sha256sum -c predictions-r9.sha256.repo` → `OK`.
- Observed: INC **4/8** > CKPT4710 **2/8** = CKPT710 **2/8** > MONO **0/8**
  (mean final `nwrong` 0.500 / 0.875 / 1.375 / 2.250; 0 parse failures,
  0 `finish=length`); best paired test INC>MONO 4:0 p=0.125.
- Prediction score: **2/4** cell hits, mean absolute error **0.094** of n
  (INC over-predicted 6→4, CKPT710 under-predicted 1→2), onset 5.0 predicted vs
  5.8 observed; all **4/4** directional falsifiers unfired.
- The critic's *independent* pre-registered rule (claim (i) survives iff
  CKPT ≤2/8 **and** INC ≥5/8) returned **indeterminate** — INC one problem
  short — and is filed as indeterminate, not as a replication.
- Control-arm audit: ack compliance degraded vs r8 (r8: 0 leaks beyond the
  harness-demanded turn 1; r9: **16/48** and **8/56** non-turn-1 ack turns
  emitted full states, in all 8 problems) → the r9 checkpoint cells carried
  *more* self-copy scaffold and still scored 2/8, so the scaffold reading is
  conservative.
- Net: **ordering replicates, magnitude does not** (r8 Δ=6 problems → r9 Δ=2;
  MONO failed 0/18 across both rounds).

**3. Novelty priced against public literature** (scout L2, primaries fetched
in-session) — `corpus/knowledge/eval-prior-art-calibration.md`: 3 of 4 round-8
findings known/incremental (Laban et al. ICLR 2026 SNOWBALL +15–20% and
over-reliance on prior answers; Huang et al. ICLR 2024 self-correction null;
FollowBench / Multi-IF / MultiChallenge for late rules), and the non-iid-draws
finding a **direct replication** of llama.cpp issue #7052 (same prompt + seed at
temp 0 across 8 slots → 5–8 unique completions). Surviving novelty is
instrument-level: no named suite ablates **emission granularity** on identical
problems/seeds, and none runs a **vacuously-satisfied** late rule against
matched binding/no-rule controls. Cross-cutting limit now written into the
corpus: every cell is a sub-3-bit (UD-IQ2_XXS) + llama.cpp serving-stack
observation, not a Qwen3-Coder-30B-A3B capability measurement.

**4. Contract repairs** (reviewer + scribe + connector L2s, integrator-applied):
`SCORECARD.md` created (owned pair + six axes, fixed measurement proxies, ±1
rubric, `planned` = the hermetic in-repo grader, `retired` = none);
`SHONEN.md` regenerated byte-identical to the `PROTOCOL.md` canonical seed — the
dropped "instructions executable without oral context" box restored, marks
`[~] [~] [ ] [~]`, zero self-attested `[x]` (normalized diff vs seed → `True`);
`PROVINCE.md` enumerates 8 resolving surfaces + refusals + 3 report-outs;
`corpus/README.md` index complete in both directions plus an `evidence/`
section; `SKILL.md` gained §"Planning-horizon & transcript-shape probes"
(cell-semantics table + 9 measurement rules), anti-patterns 9–13, and the
prediction-ordering gate in checklist item 1.

**5. Routed-defect closure** from the aggregator's round-6 audit
(`corpus/lessons/round-6-aggregator-audit.md`, filed mid-round and committed by
the aggregator as `3175e69`): majors 1–5 closed (appended errata
`0/12`→`0/17` in `bench-arena-round7-noise-n25.md`; the append-only violation
named in an appended entry rather than undone; the orphaned `85b22e3` citation
resolved to the live hash `f147a27`; index rows added; `SCORECARD.md` created
with a recorded `novelty` sub-axis mapping), minors 6–10 and 12 closed
(terminology swept, ledger drift 7,218 → **7,224** with its counting command,
`/tmp` pointers labelled, `SHONEN.md` canonical, lane commit identity
configured, provenance reconciled in
`corpus/evidence/round9-fleet/INTEGRATOR-NOTES.md` §1 — the "different
execution" reading in `probeB.md:7,130` is **falsified**: key-set delta exactly
`{raw}`, 0 semantic differences over 268 records). One reviewer defect
**rejected** with evidence: `SKILL.md:24` prefers SWE-Bench Pro *because*
Verified is contaminated, matching
`benchmark-shortlist-for-godspeed-research.md:37-38`.

## Changes landed ↔ `LOG.md`

| `LOG.md` line | Content | Files |
|---|---|---|
| 13 | round-8 retrospective (probe design, 78/78 run, SUMMARY, three non-closures) | `corpus/evidence/round8-horizon/*` |
| 14 | round-9 calibration axis-move (a–g: fleet, r8 analysis, r9 replication, novelty pricing, contract repairs, endpoint re-verification, reviewer triage) | `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md`, `SKILL.md`, `corpus/knowledge/{bench-arena-round8-horizon,bench-arena-round9-replication,eval-prior-art-calibration}.md`, `corpus/lessons/{round-8,round-9}.md`, `corpus/evidence/round9-{replication,fleet}/` |
| 15 | corrections + routed-defect closure (majors 1–5, minors 6–10, 12; one rejection) | errata in `bench-arena-round7-noise-n25.md`, `ledger-route-telemetry.md`, `lessons/round-5.md`; `INTEGRATOR-NOTES.md` |
| 16 | count reconciliation (19 fleet files; 11/11 lessons rows; 21/21 knowledge rows) | `corpus/README.md` |

## Cross-domain evidence — reported, not absorbed

| Evidence | Belongs to | Disposition |
|---|---|---|
| Keep an explicit output-contract system prompt whenever tool affordances are exposed, else a benchmark records `finish=tool_calls` instead of capability (`corpus/knowledge/bench-arena-round7-scaffold-ablation.md`) | **kotoba** (prompt/skill craft) | reported out; kengaku keeps the measured effect and the score |
| `~/Projects/bounties/ledger/telemetry.jsonl` semantics: mission-state/dispatcher vs route-resolution/failure taxonomy | **kasegi** / **kumitate** | split recorded in `PROVINCE.md` + `corpus/evidence/round9-fleet/sibling-overlap.md`; kengaku keeps model×lane and reroute inference only |
| Janitor consumer-side endpoint config; and the model-serving plane (`:34113` flags `--cont-batching`, `-np`, slot count) which **no lane owns** | **kagi** / **protocol** (unowned surface) | escalated, not remediated here |
| `AXES.md` defines six axes while `MISSION.md:14` assigns this lane `novelty` (`grep -n novelty ../AXES.md` → 0 hits) | **protocol** | either add `novelty` to `AXES.md` or ratify the recorded sub-axis mapping at `SCORECARD.md:9-17`; until then that mapping is this repo's definition of record |

Aggregator-owned files: `corpus/lessons/round-6-aggregator-audit.md` was found
uncommitted mid-round, indexed by this lane (the index is lane-owned) and left
for the aggregator, which committed it itself as `3175e69` before this lane's
commit — no misattribution, nothing swept.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — 2 decision tables, 13 anti-patterns, 9-step checklist, 20 cited-source bullets (counting commands in the box's evidence line); 0 dangling citations of 129 swept (`corpus/evidence/round9-fleet/review.md` §2)
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — round-4 4-task slice, round-5 33-task battery, round-8 78-job horizon probe, round-9 pre-registered replication (284 records, `corpus/evidence/round9-replication/results-r9.jsonl`)
- `[ ]` Instructions executable by an agent without oral context — **never tested**; no cold-agent execution of `SKILL.md`/`corpus/` has been run or logged. Partial: `corpus/evidence/round9-fleet/test_harness.py` runs hermetically (exit 0), but no in-repo gate exists (`SCORECARD.md` operability 4, planned move)
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — 8 surfaces re-verified resolving this round; 21 knowledge entries cite in-province sources; 3 items reported out with named owners (`corpus/evidence/round9-fleet/sibling-overlap.md`)

No box can be `[x]` this round: all ten verification L2s were dispatched by this
lane, and "a subagent the lane dispatched is still the lane" (`PROTOCOL.md`,
promotion gates).

## Mission-age actuator (open > 2 driver ticks = 900 s; tick 450 s)

Ages computed from the launch epoch embedded in `.ufo/state/<lane>.mission`,
`now=1790632474`; activity = commits authored since launch + files modified
under the lane's write scope (`find <repo> -newermt @<launch> -type f -not -path '*/.git/*'`).

| Lane | Mission | Age | Verdict | Evidence |
|---|---|---|---|---|
| aggregator | `shokunin-r6-aggregator-r1790629072` | 57 min | **progressing** | 25 main-repo files modified since launch; 4 child-repo commits authored by `aggregator-shokunin` within the last 3 min (`3175e69`, `ad694a2`, `ab8c9e2`, `d341b48`, `778310d`) |
| kengaku (this lane) | `shokunin-r9-kengaku-r1790629072` | 57 min | **progressing → filing** | 44 files modified; commit `2575be6` authored by `kengaku-shokunin` |
| kagi | `shokunin-r10-kagi-r1790630877` | 27 min | **progressing** | 10 files modified under `kagi-shokunin/` since launch (incl. `corpus/knowledge/surface-census.md`, `corpus/lessons/round-10.md`, 2 `.tsv`), uncommitted `PROVINCE.md`/`SKILL.md` edits staged |
| kake | `shokunin-r11-kake-r1790630876` | 27 min | **no lane-authored activity yet** (not silent-by-choice, not a `failed` trigger) | the only file modified under `kake-shokunin/` since launch is the aggregator-owned `corpus/lessons/round-6-aggregator-audit.md`; kake's own last commit `dd4eabf` predates this launch by ~3 min — within the fleet's normal commit sparsity (34–47 min observed) |
| kasegi | `shokunin-r13-kasegi-r1790630874` | 27 min | **progressing** | untracked `kasegi-shokunin/artifact_probe.txt` modified since launch; last lane commit `fc6d398` 20 min ago |
| kotoba | `shokunin-r10-kotoba-r1790631328` | 19 min | **progressing** | 18 files modified since launch (`LOG.md`, `SCORECARD.md`, `SHONEN.md`, `SKILL.md`, 2 knowledge entries), staged |
| kumitate | `shokunin-r9-kumitate-r1790631779` | 12 min | below the 900 s threshold | — |
| protocol | `shokunin-r11-protocol-r1790632230` | 4 min | below the 900 s threshold | — |

## L2 fleet (10 agents, one batched call, MISSION bucket routes)

executor ×3 (probe A / B / C analyses), labrat (pre-registered replication —
the only agent permitted to touch `:34113`), critic (16-defect fix-landing audit
+ claim triage + the pre-registered replication falsifier), reviewer (citation /
state / endpoint audit, 8-defect queue), mutation-tester (50-case grader/parser
battery), scout (prior-art pricing, primaries fetched in-session), connector
(sibling-overlap map + SCORECARD convention), scribe (scorecard / LOG / SHONEN
drafts). Every artifact committed verbatim under
`corpus/evidence/round9-fleet/` (19 files) with integrator corrections in
`INTEGRATOR-NOTES.md`; no L2 wrote into the repo (single integration owner).

## Next move (recorded in `SCORECARD.md` §Planned)

Lowest post-move axis is **operability (4)**: promote the stored-run analysis
into a committed hermetic grader that replays
`corpus/evidence/round8-horizon/results.jsonl` and
`round9-replication/results-r9.jsonl` offline, recomputes every SUMMARY count,
and exits 1 on disagreement. Falsifiable target: runnable in-repo files ≥12,
exit 0 on the committed bytes and exit 1 on a copy with one flipped `ok` field,
both runs recorded in `LOG.md`.
