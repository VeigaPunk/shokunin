# game-dev-2d — round 105 (kaika)

## Work performed

Declared claims: **C1 coverage — restore retired ResourceUID rows with explicit project/cache preconditions; C2 calibration — learn from rejected/HOLD/errata rounds through a lesson-backed QUALITY bar; C3 depth — acquire the curated SOURCES capability and admit three executable, source-linked knowledge entries.** No exploratory claim. Depth is the lowest-axis proxy: its axis-table evidence was oldest (r49, versus calibration r56/coverage r61). All numeric scores were unscored at entry; no arbitrary scalar was invented.

Lane write scope: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/game-dev-2d-shokunin` (all lane paths below are relative to it). Final lane HEAD **`b0d2c499`**, implementation **`ff32e252`**, initial work **`7d9d9741`**, base **`e8990516`**.

- **C1:** re-admitted eight ResourceUID rows (seven retired rows plus repaired createid), supplying a cache-less pre-CASES project copy, unique XDG and resource scratch per row; added forward/reversed ordering and a discriminating export-writer→UID-reader control. Createid now checks distinct paths as well as repeatability, round-trip and non-registration; a constant-return mutant is rejected. **21→29 UID CASES, 585→600 total CASES.** Evidence: `corpus/lessons/r105-res-uid-isolation.md:352-369`; `reports/round-105/r105-battery-receipts.json`; commits `7d9d9741`, `ff32e252`.
- **C2:** mined **32 grounded mistake classes**, mapped **32/32** to **23 QUALITY criteria**, including mistakes discovered during this round. Corrected r104's claimed 23 UID rows to 21 actually landed; clarified cache-regime confounding, duplicate meta results, constant-return blind spot and finite-life probe scheduling. Evidence: `corpus/lessons/round-105.md:3-38`; `corpus/QUALITY.md`; `LOG.md:1384-1428`.
- **C3:** created **31 opened SOURCES rows** with scoped tiers, rejection reasons/flips, four study paths and bounded search logs; admitted three knowledge entries. K1 corrects r92's wrong-RID interpretation; K2 curates UID authority/lossy text; K3 distinguishes host-observed replay identity from an engine determinism guarantee. Seven new fixture rows pass serially. Evidence: `corpus/SOURCES.md`, `corpus/lessons/round-105.md` §Gate, `corpus/knowledge/2026-10-19-*.md`, `reports/round-105/r105-claim-tuples.json`.
- Appended a current coverage map and Frontier, clarified Core/Frontier/Adjacent/write isolation, and regenerated canonical SHONEN text without any `[x]`. No SKILL claim or promotion. Evidence: `corpus/README.md:26-72`, `PROVINCE.md:14-38`, `SHONEN.md`; `LOG.md:1371-1382`.
- Dispatched **10 L2 leaves in one batched task call**: planner, connector, four executor seats, scribe, scout, reviewer, critic. No model override. One executor died `resource_exhausted` before writes and was freshly replaced; two later within-lane review seats found actionable defects. Reports are committed under `reports/round-105/r105-R105*.md`, with complete final-review text in `r105-final-review-raw.json`. These reviewers are still the lane, not outside verifiers.
- A committed iteration **failed** and was rejected, not retried unchanged: at `7d9d9741`, new probe work expired a detached descendant before its `sleep 8` liveness check (600 CASES passed; two meta failures). `ff32e252` moves that work before the descendant tail, preserves every prior lifetime/pin/discrimination, and learns M32→Q23. Evidence: `reports/round-105/r105-scheduling-failure.json`, `r105-pre-scheduling-fix-receipts.json`, `LOG.md:1411-1428`.
- Final two full serial replays at corrected commit `ff32e252`: **621/621 PASS each** (600 CASES + 21 unique meta rows), no missing/duplicate identities, **29/29 UID and 7/7 r105 each**, exact reverse UID order, eight runtime-captured source blobs matching committed bytes. Both previously failed meta guards are true. Shape: 602 audited/0 flags; evasion: 10 shapes/0 probe flags. Evidence: final receipts JSON; `LOG.md:1430-1466`.

## Landed changes

| Change | LOG tie | Carrying commit(s) |
|---|---|---|
| Per-row UID project/XDG/root preconditions; eight re-admissions; createid repair; 4 tile-RID + 3 replay rows; precise control and source-byte binding | `LOG.md:1341-1370`, review correction `1384-1409` | `7d9d9741` |
| Move shared probe outside detached-liveness window; retain failed evidence; add Q23/M32 | `LOG.md:1411-1428` | `ff32e252` |
| SOURCES, QUALITY, three knowledge entries, Gate quotes, coverage/province/checklist corrections, L2 evidence | `LOG.md:1351-1382`, `1384-1409` | `7d9d9741`; Q23/M32 in `ff32e252` |
| Final committed receipts, per-axis scorecard/capability/current plan, explicit replay bounds and outside-check status, shared-source validation | `LOG.md:1430-1466` | `b0d2c499` |

All commits use `game-dev-2d-shokunin <game-dev-2d@shokunin.local>`. Pathspec-limited staging/commits; required staged credential sweep printed nothing. **No push**: the standing operator rule overrides MISSION's push instruction. No fleet-ledger commit by this lane; the integrator commits this report. No domain or sibling checkout writes.

## Before → after measurements

Measured baseline `e8990516`, corrected implementation `ff32e252`, and final record HEAD `b0d2c499`. Command (from lane root):

```sh
sh reports/round-105/r105-count.sh e8990516
sh reports/round-105/r105-count.sh ff32e252
sh reports/round-105/r105-count.sh b0d2c499
```

The committed script contains the exact AST and row/header-count commands, accepting the measured git revision rather than reading a moving worktree. Output for baseline/implementation is committed in `reports/round-105/r105-measurements.txt`; final-HEAD execution reproduced the same after values.

| Claim | Before → after | Score delta / self-verdict |
|---|---|---|
| C1 coverage | UID CASES **21→29**; all CASES **585→600**; r105 fixture rows **0→7**; final UID rows **29/29 ×2** in exact reversed order | Numeric **unscored→unscored**, delta undefined; **improved**, pending outside verification |
| C2 calibration | QUALITY criteria **0→23**; mined M classes **0→32**; captured **0→32/32** | Numeric unscored→unscored; **improved**, pending outside verification |
| C3 depth + source capability | knowledge entries **2→5**; entries with all three required headers **0→3**; source rows **0→31** | Numeric unscored→unscored; **improved**, pending outside verification |

Behavioural command (run once per ORDER, serial, at `ff32e252`):

```sh
ORDER=forward  # second invocation: ORDER=reversed
 timeout --signal=TERM --kill-after=2s 1700s python3 corpus/fixtures/run_battery.py \
  --godot /usr/bin/godot --probe-failing --probe-unrelated-error \
  --probe-export-launch --probe-godot-error --probe-stream-attribution \
  --probe-crash-exit --probe-timeout --res-uid-order "$ORDER" --probe-res-uid-shared
```

Final runs `20261019T233501498056Z` / `20261019T234607282166Z`, combined wall **1325s**, exit 0. Reconstruct the compact committed receipt with:

```sh
python3 reports/round-105/r105-receipts.py \
 corpus/live/runs/20261019T233501498056Z/verdicts.json \
 corpus/live/runs/20261019T234607282166Z/verdicts.json
```

The final JSON is self-contained for the claims (focus signatures, source blobs, unique identity checks, meta verdicts, unchanged regression guards, clean-shared/export-writer/seeded-reader outputs). Ignored live scratch is not the closure pointer.

**Control interpretation:** clean shared UID rows pass 8/8 with no cache before/after; the actual export writer creates the cache; seeded readers reproduce UID diagnostic/cache-signature mismatches in path/missing/s01_diag. This proves preceding-writer cache-regime interference. It does **not** prove within-UID row-order leakage; neither ordering of the cache-less shared arm exhibited it. Claims are checked separately: C1 runtime preconditions, C2 evidence-to-criterion mapping, C3 source/fixture facts; QUALITY is shared admission infrastructure, not the behavioural premise of the other claims.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md remains absent; no claim on this box.
- [~] At least one end-to-end domain task executed and logged in LOG.md — final 621/621 serial replays, `LOG.md:1430-1466`, `reports/round-105/r105-battery-receipts.json`.
- [~] Instructions executable by an agent without oral context — three bounded lane-root recheck commands, exact linked tuples, `reports/round-105/r105-count.sh`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — appended Core/Frontier/Adjacent/isolation clarification and connector report `reports/round-105/r105-R105Connector.md`.

No named outside verifier yet; lane subagents do not qualify. Orchestrator must check ≥1 admit/≥1 reject, reopen ≥3 source rows and rerun every count. Lesson Gate explicitly records this pending status.

## Sources & frontier

- **Registry rows 0→31**: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Added **A=30, B=1, C=0**; statuses **mined=10, queued=19, rejected=2**.
- All frozen census commands run clean: `sh reports/round-105/r105-sources-census.sh` → malformed 0; duplicate IDs, enum/tier inflation and dead mined paths print nothing. Output committed as `r105-sources-census.txt`.
- **Actual current shared validator**, executed again on final HEAD `b0d2c499`:
  `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/game-dev-2d-shokunin --today 2026-10-19 --verbose` → **ok, exit 0**. Persistent output: `reports/round-105/r105-fleet-source-validation.txt`. No retired fleet-census worktree path is the validation authority.
- Existing rows touched: none (registry first created this round). Before initial landing, S015/S031 recheck cells were corrected **`—`→`180d`**, logged in lesson Gate; revision anchors were tightened to commits/Git blobs. Both rejected rows retain explicit reasons and flips. All 31 Gate records contain round-local opened dates and anchored short quotes.
- **Frontier advanced: two rows** — TileMapLayer collider-RID attribution (S002/S005/S027/S029/S030, K1), physics replay boundary (S009/S010/S025/S030, K3). K1 is scoped to measured cells; no universal quadrant-coordinate formula. K3's eight-body+character scenario was host-identical but the engine gives no guarantee; a different six-body critic probe is corroboration only. K2 is curation, not new frontier expansion.
- Still open: clean-checkout import→export→launch, rendered canary/performance, engine-version matrix, reusable input recording, localization wiring, shader output and multiplayer beyond loopback. Explicit sweeps/pointers in `corpus/README.md` §Frontier.

## Mistakes

**32 classes mined, 23 criteria, 32/32 captured** (`r105-count.sh` C2 block at `b0d2c499`). Classes cover contaminated negatives, unresolved causal fixes, pre-fix verification, overstated resolution/scope, falsified/dead pins, fixed global resources, broken links, orphan ownership, cache state, post-run retirement, write-scope and broad staging mistakes, evidence overwrites, identity, stale curation, runtime-token errors, count-from-patch inflation, confounded controls, duplicate meta names, constant-return blind spots and finite-life scheduling. Every row has its motivating path/revision and Q mapping in `corpus/lessons/round-105.md`.

This round learned from its own errors: final review caught M29–M31; the actual committed run caught M32. The harmed `7d9d9741` iteration stays rejected and preserved. The scheduling fix did not widen a lifetime, suppress a guard or alter a prior expected CASES string; both full corrected replays pass all old and new rows.

## Trend verdicts

- **Expansion: improved (self-verdict)** — two admitted entries on previously open coverage-map ground (K1/K3); K2 additional curation. Not claimed merely from 31 source rows.
- **Quality: improved (self-verdict)** — wrong-RID interpretation explicitly corrected, claims scoped to measured data, precise controls and source-byte provenance, final 621/621 rechecks twice. Legacy two entries remain explicitly unretrofitted, not silently admitted under the new bar.
- **Discernment: unchanged / pending outside spot-check** — grounded criteria and preserved reject/harm lessons improve calibration, but taste is not certified from the lane's own reviewers. Await orchestrator admit/reject judgment.

## L0 questions

`game-dev-2d | round-105 | Numeric axis scores remain unscored without an adopted domain rubric. Should the re-derivable unit-fraction rubric proposed in reports/round-105/r105-R105Planner.md be adopted, or should canonical per-axis verdicts remain the authority? Depth was worked using the explicit stale-evidence proxy; no scalar score was fabricated.`

Do not block integration on the answer; per-axis measured evidence and self-verdicts are recorded. Integrator owns any append to the fleet L0 file.

## Integrator notes

- **Ready for non-author verification; no runtime blocker.** Final lane HEAD `b0d2c499`; measured code `ff32e252`. Commit this report as `game-dev-2d-shokunin <game-dev-2d@shokunin.local>`; this lane did not commit the ledger worktree and did not push.
- Preserve the initial and failed receipts as adverse history; final evidence is `r105-battery-receipts.json`, not the initial 622-row receipts or the failed committed run.
- Inherited defects intentionally not claimed fixed: absent SKILL.md, numeric-score rubric, legacy metadata/Gates/citations, duplicate historical Saturation placeholder, 40,677 tracked live files, historical round/manifest gaps. No live files were newly staged; all generated scratch remains ignored. None is a fabricated capability or a reason to erase knowledge.
- 3D's r107 side-round was aborted (wrong-cwd spawn) and is owned by 3D to retry; this lane only recorded disposition. No sibling/domain mutation. Root-ledger kotoba clobber remains fleet-owned.
- Provider exhaustion was handled by a fresh executor spawn on the host-assigned route, not a model override or scope reduction. The broken-shell `cd` hazard was relayed; writes used isolated cwd/absolute paths, and the lane found no own fleet-root stray writes.

## Outside adjudication and final closure correction — supersedes provisional admission status

**Final lane HEAD: `546db8d771a189e4455813efbad59fa70cbc8c2c`. Parent Main's
disposition: REJECT ROUND 105 AS DECLARED / HONEST STOP.** This is not an admitted
round despite the preserved positive runtime and corpus observations.

W3ReviewGameDev2d recommends ADMIT and agrees with sampled admits K1/K2 and
rejects ART C4/C5/S031. W3CriticGameDev2d corroborates the sampled source/runtime
facts but identifies the binding frozen-claim dependency: **C2 creates QUALITY,
which is required for the knowledge-admission component of C3.** Therefore C3
cannot verify as declared independently of C2. Calling QUALITY shared admission
infrastructure did not cure the causal-separability violation. Parent selects
rejection; the original declaration and dissent are preserved, not rewritten.

Persistent outside evidence:
- `reports/round-105/r105-outside-review.md` — ADMIT recommendation, independent
  source/runtime checks and agreement on candidate admits/rejects.
- `reports/round-105/r105-outside-critic.md` — causal-separability counterexample
  and provenance/counter defects.
- `LOG.md:1468-1523` and `SCORECARD.md` §Round 105 outside disposition — explicit
  parent rejection/HONEST STOP and reachable corrections.

The verified UID **21→29**, CASES **585→600**, two **621/621** receipts, **31**
source rows and **three** knowledge notes remain intact. C1's bounded improvement
is corroborated; C2/C3 are **not admitted as independent frozen claims**.
No post-hoc source-only C3, deleted knowledge, invented numeric rubric, promotion,
or automatic next-round progression. Evidence age remains a work-selection
heuristic, not proof of the lowest scalar axis.

### Reachable corrections landed in `546db8d7`

- **QUALITY provenance:** append-only correction labels Q1–Q3 as **three inherited
  mandatory contract baselines**, not lesson-derived credit. Q4–Q23 are **20**
  lesson-derived rows; total remains **23**, with no new/fake Q rows. Canonical
  provenance is cited in the QUALITY/lesson append (paths fleet-root-relative).
- **Counter:** every captured-by Q ID now joins against actual QUALITY IDs at
  the measured revision. Distinct counts: **32 syntactic**, **32 joined-valid**,
  **32 metadata-pointer-backed**. The last means a resolvable
  criterion-why→lesson M-row→evidence chain, **not substantive grounding**.
  `reports/round-105/r105-mapped-criteria.py` implements the join.
- **Invalid-criterion negative:** an in-memory `Q999` appended to M1 leaves
  syntactic mappings **32→32**, reduces joined-valid **32→31**, and diagnoses
  **`Q999 via M1`**, without modifying corpus files. Commands and outputs:
  `reports/round-105/r105-closure-counter-checks.txt`.
- **Search-log correction:** appended disjoint named sets Sweep1 S001–S025
  (**25**), Sweep2 S026–S030 (**5**), Sweep3 S031 (**1**). Union **31**, overlaps
  **0**, missing/extra none, **29** non-rejected/**2** rejected; S025's note is
  an existing-row re-screen. Earlier double-counting notes and all registry rows
  are retained. Named-set sweep/output lives in `corpus/SOURCES.md:58-80`.

Final scoped checks, rerun on **`546db8d7`**:

```sh
sh reports/round-105/r105-count.sh 546db8d7
python3 reports/round-105/r105-mapped-criteria.py 546db8d7 --self-test-invalid Q999
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
 /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/game-dev-2d-shokunin \
 --today 2026-10-19 --verbose
```

All exited **0**. Counter output: UID29/r1057/total600; criteria23 =
baseline3+lesson-derived20; M32/syntactic32/joined32/metadata-backed32; knowledge5/
full-header3/SOURCES31. The negative produced the one-row loss above. Actual
registry validator printed **`game-dev-2d-shokunin ok`**; rejected source rechecks
remain legitimate `180d` cadences. **No Godot/full battery was rerun** for these
metadata/counter corrections; old runtime code and receipts are unchanged.

### Final trend/disposition note

- **Expansion:** verified positive knowledge signal (K1/K3 frontier entries), but
  this does not make the frozen round admissible.
- **Quality:** positive bounded artifact/source verification remains preserved;
  baseline provenance, joins and search accounting were corrected rather than
  credited as new discoveries.
- **Discernment:** the outside candidate admit/reject sample agrees; the critic
  still refutes round-level separability. Record both, without averaging away the
  conformance failure. Parent controls final trend/admission classification.

**Closure authority remains the parent's REJECT / HONEST STOP.** Commit
`546db8d7` uses lane author/committer identity and passed an empty staged
credential sweep. This report append remains uncommitted for the integrator.
No push, routing/model change, runtime rewrite, promotion or scope expansion.

## Integration simplification — final lane HEAD f67c64ae

Parent integration review found that the new generic pointer resolver and
metadata-backed metric exceeded the requested captured-by ID join.
Commit **`f67c64ae`** replaces that helper with the local two-blob counter and
appends the withdrawal to LOG, SCORECARD and the lesson. **The metadata-backed
metric is withdrawn**, not renamed or retained as grounding evidence.

The counter reads only `corpus/QUALITY.md` and `corpus/lessons/round-105.md` at
the given Git revision, parses Q IDs/captured-by IDs, counts syntax versus
all-IDs-existing joins, and names unknown IDs. Q1–Q3 inherited-baseline3 and
Q4–Q23 lesson-derived20 remain labels for existing rows, not new learning credit.
No generic evidence-path resolver, BARE_PATHS, blob cache, metadata-grounding
proxy or test-mode CLI remains. The former `--self-test-invalid` commands in
the earlier record are historical, not current reproduction instructions.

Only two scoped checks were run after the final helper replacement:

1. `sh reports/round-105/r105-count.sh 546db8d7` → exit 0; Q23 =
   baseline3+lesson20, M32, syntactic32/join-valid32, unknown none; unchanged
   UID29/r1057/CASES600 and knowledge5/full-header3/SOURCES31.
2. The **external in-memory Q999 negative** in
   `reports/round-105/r105-simple-counter-checks.txt` → exit 0; syntax32→32,
   valid32→31, **`Q999 via M1`**, no corpus mutation. It uses the ordinary parsing
   function, not production test instrumentation.

Exact commands/output are committed in that evidence file; the old counter
records remain intact. Parent can rerun command 1 at `f67c64ae` and the same
external negative recipe. No broader checks or Godot/full battery were rerun.
No runtime, fixture, knowledge, source row or 621-pass receipt was changed.

Only the counter, its scoped evidence file and append-only LOG/SCORECARD/lesson
notes were committed, using lane identity after an empty staged credential
sweep. This fleet report append remains uncommitted for the integrator.
**REJECT AS DECLARED / HONEST STOP remains unchanged; no claim rescope,
promotion, numeric rubric, push or routing change.**
