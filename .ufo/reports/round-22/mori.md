# mori — round 22 report

Lane `mori-shokunin`, L1 MoriR22 (claim mori=22 attempt1, sole owner after resume). Entering branch `77a5bbe8a0b41dfbfd2546d024d36e294b814bd0`; landed lane tip **`1bfe708a170c877db3319060d0ab38771efe03ac`** (measured revision `da40bb20f81da125d798f73cd1653655be1255ca`; later commits add evidence/ledgers only, tool bytes unchanged).

## Work performed

Declared claims (1): **C1 — calibration capability: retention receipt reconciliation** (calibration 5→5 held; lowest non-retired tie with depth/freshness; sourced on S064). It independently recounts a committed retention receipt's measured Git tree and reports exact identity agreement, policy-membership exclusions and the red state — accounting agreement, never privacy clearance. Open debt carried, not cleared: r21 admission granted no privacy clearance; 4 unallowlisted retention hits remain; original permission control RED 11/12; R21 C1 two dispositions remain explicitly unknown, baseline acceptance pin-blocked.

- Contract + 24 finite requirement IDs frozen before any implementation: `.ufo/waves/round-22/contract.md`, `frozen/requirements.json` (landed `df880b4`).
- L1 mistake caught by wave1 identity audits (RawPartition, ReportContract, PriorMistake, ConnectSouji, QualityDenom…): I had read "5 policy-excluded" as hits in the policy source file. Receipt identities show 95 = 86 allowlisted + 4 unallowlisted + 5 **non-author-glob** exclusions; the policy file holds 4 allowlisted hits; the 4 red hits sit in a byte-identical nested policy copy (`.ufo/waves/round-20/falsify/NoHarmRun/rg/…/c1-policy.json`). The operator's 95/5/90/4 totals were right; my interpretation was wrong. Original contract retained; correction + v2 builder/oracle/requirements frozen **before implementation** at `e2f549b` (`denominator-correction.md`, `frozen/fixture-builder-v2.py`, `oracle-reconcile-v2.py`, `frozen/requirements-v2.json`).
- Shipping tool `tools/mori-retention-reconcile.py` (L1-authored; all three executor seats died) — first landed `8cb4afb`, hardened through `3985b3d`, `50b6f75`, `da40bb2`; final sha256 `0795bac9367c33e534b79599114c1635d83c4b0e4a57fbbe235644858a59de32`.
- Wave2 falsification (41 surviving reports under `.ufo/waves/round-22/falsify/`) showed frozen arms check exit+finding only and that mutant kills were credited for "any unmet row". Folded without touching frozen v2 bytes: distinct reason tokens (`measured_not_ancestor`, `receipt_revision`, `repo_not_absolute`, `repo_not_toplevel`, strict UTF-8/BOM-free JSON, `-h`→usage exit 2, regex Overflow/Recursion→`policy_regex`, closed stdout/MemoryError never exit 1), receipt policy/allowlist path binding, truthful `raw_not_allowlisted` beside the frozen alias `raw_unallowlisted`; 52 co-evolved controls (`refinement-reconcile.py`); 22 mutants each scored only on named target rows (`measure-round22.py`).
- Measurement driver binds every executing input to the measured commit and the freeze inputs to `e2f549b`: `evidence/measure3/summary.json` (`executing_input_bindings`, `all_claim_checks_pass: true`).
- Planner mapping: the L1 held the frozen-topology planner seat (validator rejects `planner`); planning data-walks rode scouts (RequirementTrace, RawPartition) — recorded here per ruling.
- Source spot-check: Main (non-author) agreed S064 admit / S065 reject — `evidence/source-spotcheck.json`.

## Landed changes

All via `jj-lane.sh`, lane identity, each tied to `LOG.md` round-22 entries (`LOG.md:1442–1520`):

| Commit | Content | LOG entry |
|---|---|---|
| `df880b4` | contract, requirements, wave1 spec/dispatch/taskcall | Round22 declaration |
| `306e06e` | red→green dispatch context checks (CONTEXT_MISSING 7 → CONTEXT_OK 12) | Round22 declaration / lesson M2 |
| `e825c7f` | v1 fixture builder/oracle (retained, superseded) | pre-implementation correction |
| `e2f549b` | denominator correction + v2 freeze | pre-implementation correction |
| `8cb4afb` | reconciler, SKILL/PROVINCE/QUALITY Q70/README/SOURCES/lesson/knowledge | pre-implementation correction and implementation provenance |
| `3985b3d` | path binding, refinements, measurement driver | author-side falsifier refinements |
| `b095ecc` | parent-requested wip checkpoint of my in-flight files (folded) | final measured outcome |
| `4f7cfce`, `94b9014`, `5888b56` | wave1 reports, identity expectations, measure1, wave2 dispatch binding | final measured outcome |
| `50b6f75`, `da40bb2` | wave2-driven hardening, controls, targeted mutants, measure2 | final measured outcome |
| `2e73ecc`, `1bfe708` | measure3, deaths, settlement, misroot receipt, SCORECARD/LOG | final measured outcome |

## Before → after measurements

C1 counting command (lane root), same frozen v2 oracle and inputs both sides:

```sh
python3 .ufo/waves/round-22/measure-round22.py --revision da40bb20f81da125d798f73cd1653655be1255ca --output <absent-dir>
jq -c '[.before.capability_absent,.after.capability_absent,.after.pass,.all_claim_checks_pass]' <absent-dir>/summary.json
# observed (evidence/measure3): [24,0,24,true]   rc=0
```

Before = capability absent at entering `77a5bbe` (`git cat-file -e` rc≠0), not 24 production defects. Measured at `da40bb2`: selftest 4/4; refinements 52/52; 22/22 targeted mutants killed, unmutated frozen+refinement controls green; all-arm output safety true; real r21 receipt → exit 0 `RETENTION_RECONCILED`, raw 95 / policy_excluded 5 (non_author_paths_glob) / scanner 90 / unallowlisted 4 / raw_not_allowlisted 9, retention red, `privacy_clearance: false`, identity digests match, swapped twin rejected; contradictory entering receipt rejected (`receipt_revision_conflict`). Retention floor at tip `1bfe708`: `RETENTION_FINDINGS` metric 4, 95 hits, 0 new/0 missing — still red. Earlier runs measure1 (`4f7cfce`) and measure2 (`50b6f75`) also `all_claim_checks_pass: true`, retained. Limits: frozen R13–R21 prove exit class only (reasons rest on co-evolved controls); `expected-real.json` was committed with the implementation, not pre-build; residual: lone `\u` surrogate escapes, per-blob `cat-file` cost, strict non-UTF-8 path refusal, mode `100664` refusal.

## Sources & frontier

Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: start rc 0 (`evidence/sources-start.json`), end rc 0; rows **76 → 76**, A62/B6/C8, mined42/queued25/rejected9 both ends. Rows added: A0/B0/C0. Touched: S064 used-by `corpus/lessons/round-19.md` → `+ corpus/lessons/round-22.md, corpus/knowledge/freeze-order-r18.md, corpus/knowledge/retention-reconciliation-r22.md` (logged in `corpus/lessons/round-22.md`). S064 re-admitted (commit-resolution scope), S065 re-rejected; ≤25-word located quotes in lesson Gate; Main agreed both. Mistakes mined: M1 scalar-vs-identity population, M2 dispatch context omissions (red→green shown), M3 contradictory wrapper revision, M4 mutants credited by any unmet row (fixed by targeted rows, shown able to fail). Sourced claim: C1 cites S064. Frontier rows advanced: none (calibration of existing own-evidence ground).

## Trend verdicts

- **expansion: unchanged** — one new knowledge note on existing own-evidence retention ground; no uncovered coverage-map ground, no new source rows.
- **quality: improved** — the r21 retention receipt's accounting is now independently re-verified by identity at its measured commit; superseded source-file interpretation retained and corrected; carried red debt re-measured unchanged.
- **discernment: improved** — Main's non-author agree/agree on the S064 admit / S065 reject sample; QUALITY criterion 70 lesson-backed (M1/M3).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:534–564` registry row + caveats; `corpus/knowledge/retention-reconciliation-r22.md`
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:1498–1520`; `.ufo/waves/round-22/evidence/measure3/summary.json`
- [~] Instructions executable by an agent without oral context — registry entry command and counting command above, `SKILL.md:534–564`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` "Round22 own-evidence accounting boundary"; connector reports `build/Connect{Kagi,Kumitate,Souji}.md`

## Swarm, deaths, inherited state

- Wave1 `mori-r22-build`: 64 seats (22 scout, 20 reviewer, 12 critic, 3 executor, 3 connector, 2 scribe, 1 mutation-tester, 1 sentinel); 56 reports; 8 deaths: ImplReconcile/OracleReconcile/FixtureReconcile/SafetyReview — "Codex is at capacity (code=turn_rate_limit_exceeded)"; LessonDraft/KnowledgeDraft — Anthropic 429 rate_limit_error; AttackR22/ReviewErrors — lost with the L1 (Devin weekly-quota stream error). `dead-seats-wave1.json`.
- Wave2 `mori-r22-falsify`: 64 seats (28 scout, 22 critic, 10 reviewer, 3 connector, 1 mutation-tester); 41 reports; 23 deaths: 20 "Devin … weekly usage quota has been exhausted", 2 commandcode "weekly usage limit" 429, 1 Devin "free model rate limit". `dead-seats-wave2.json`. Round total 128 seats; no replacements. Both waves validated (policy v2), one task call each, wave-slot acquired/released. Settlement scan: wave1 56/64, wave2 41/64 partial (`evidence/settlement-final.json`).
- Inherited: Main's `b095ecc` wip checkpoint of my uncommitted files — folded (later commits carry and supersede it). Misroot sweep: one candidate, `.ufo/reports/round-22/souji.md` — souji's own report, not a mori seat file, untouched (`evidence/misroot-sweep.json`). Untracked `.scratch/` is lane scratch (not evidence).
- Stale-lane: respawn-per-round driver; no other mori mission open.
- Tool installs/updates: none. L0 questions: none new. Ruling requested of the outside closure (not L0): keep frozen `raw_unallowlisted` alias or re-freeze to the raw complement (now emitted separately as `raw_not_allowlisted`).
- Procedural disclosures: one SOURCES used-by cell edited via a python string replacement (bytes verified); the L1 died mid-round and was resumed by Main.
