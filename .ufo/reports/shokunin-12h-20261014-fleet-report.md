# Shokunin 12-hour fleet program — final report

Program: `shokunin12h20261014`. Sole L1: this Sol 6.1 session. Fleet root
`/home/vgpnk/Projects/shokunin`. Window opened 2026-10-14T23:13:34Z.
All work is local; **no pushes anywhere**, no external fetches, global
configurations byte-unchanged (`~/.omp/agent/config.yml` sha256
`08788ddcbbb48180b987e6f54b517af294c85cacceb07bdd594843a53e668dcc` before and after).

## Routing

The requested split (content → composer, audit/review/scout/critic → grok) was
realised **session-only** through existing aliases, never by editing config:
`task.agentModelOverrides` was set in memory (executor/scribe/simplifier →
`@m_composer`; scout/reviewer/critic/connector/sentinel/revenger/mutation-tester →
`@m_grok`), then the operator's later instruction was applied for the connector
seat — `connector → @m_antigravity` (Gemini 3.8 Flash) with the fallback chain
`m_antigravity → zai/glm-5.3-flash:max` (ZAI GLM-5.3 Flash) also set in memory.
Both were **not saved**; the global file's sha256 is unchanged. Provenance:
`.ufo/scopes/shokunin-12h-20261014/connector-selection-20261014.json`.

Phase 0 (contract-sync + `self-iter` smoke) was **red** at program start
(contract check exit 1; smoke exit 2 `BLOCKED: phase-0 UFO-FSD contract gate
failed`; 18 missing generated targets, 6 dependency omissions, 74
route-equivalence mismatches, sighting-surface digest drift). That is recorded,
not repaired — the UFO checkout is outside this mission's write authority.

## Phase 1 — six-lane re-census (landed)

Two 32-member waves: repair (`Shokunin12hP1Repair20261014`, 32/32 terminal) then
an independent acceptance audit (`Shokunin12hP1Audit20261014`, 31/32 delivered).

| Lane | Round | Commit(s) | Verdicts (measured) |
|---|---|---|---|
| kagi | 19 | `5b0d4b7`, `0eae46a`, `1eaf34d`, `bad9088`, `eab4bec` | all 7 safe gates green (97/13/16/61/29/34-case selftests); `CITATION_GATE: CLEAN`; no gate-default repair warranted |
| kake | 19 | `5994831`, `3ae7e6a`, `de5d762`, `e98bf20` | `--selftest` 13/13; `--offline` exit 0 partial; explicit-bad history exit 2; **code repaired** |
| kama | 4 | `84a8130`, `47f3aed`, `0505b71` | consumers 0; check 2 (DEAD, correct); snapshot pass=24 fail=0; root derivation already correct |
| kasegi | 20 | `a5cbf77`, `644ed37`, `de625f9`, `ea36dfc` | anchorcheck `7 in-range / 0 bad / 306 lost`; density 645; census regenerated |
| kengaku | 16 | `7153e67`, `2f00932`, `7cef86b`, `25819e2` | `grader.py` `n=733 mismatches=0`; selftest ALL PASS; no `--src` repair |
| kotoba | 19 | `b0c7cb2`, `cd4798b`, `b492cb2`, `b879fb5` | integrity 9/9; independent 0; fault self-test OK; **code repaired**; checklist exit 1 on a pre-existing 601>600 budget |

**Repairs landed** (not churn — each was a reproduced defect):
kake `freshness-sweep.mjs` — `probeHistoryAbsent` now suspends only the canonical
history default while an explicit override stays fail-closed, the pin joins the
consumed list, and the selftest fixture is hermetic (a `~/../../tmp` cite could
never resolve: the scanner classifies any `..` as an unexpanded range; the
fixture now lives in a per-run `$HOME` dir created and removed by the selftest);
kotoba `verify_harness_claims.py` — two permission checks moved `at_least`→`equal`
(the `at_least`+0 pair passed any non-negative count), plus the coverage-map index
row and a recorded `tracked_files` 47→48 expectation refresh; kama
`endpoint-identity.md` line ref `:481-487`→`:516`; kagi narrowed a false
describe-don't-pin claim and corrected a mis-attributed hash; kasegi census
regenerated so it matches the tree.

**Per-axis / learning verdicts:** freshness improved for all six (measured
before→after in each lane lesson); operability improved for kake and kotoba
(code repair verified by their own suites); calibration improved (false claims
narrowed, expectation refresh recorded); adjacency improved (dead-path populations
counted and routed). Each lane's `corpus/lessons/round-<N>-recensus.md` carries
the full erratum.

**Carried debt, with unblock.** Independent sweeps measured the live dead-path
population fleet-wide at **165 hits** (kengaku 61, kama 46, kasegi 22, kagi 18,
kotoba 10, kake 8) — the upstream restructure deleted whole trees these notes
still cite. Unblock per lane: mark the named lines historical and repoint to the
capital-P survivor; each lane's lesson lists them with `path:line`. Plus: kagi
substrate absence (reinstall), kake PQ-2/PQ-14, kotoba 601-line budget (do not
raise it), kama `34113`/`8080` dead endpoints (operator restores a serving unit).

**Process defect (recorded, not hidden).** `KengakuGateRepair` spawned a nested
`labrat` against this wave's leaf contract; its evidence is ruled inadmissible for
parent gate proof, the seat acknowledged it in an append-only erratum, and a
project-local leaf-only executor card landed at `.omp/agents/executor.md`. The
lane repos' local git identity was unset (a bare commit would have inherited the
operator identity) — fixed for all eight lanes.

## Phase 2 — kumitate (landed)

Native path blocked by the red Phase 0, so the prescribed **32-lane unjudged
fallback** ran (`Shokunin12hP2Kumitate20261014`). Round 32 was pre-registered in
`SCORECARD.md` before measuring, then executed.

Measured deletion boundary, proven by `LC_ALL=C comm -3` on both sides of every
comparison (all empty): script 114 − 41 deleted + 18 added = **91**; runtime
98 − 6 = **92**; `git diff --diff-filter=D` = 50 paths = 41 S + 6 R + 3 outside
the frozen universe.

| Term | Before | After |
|---|---:|---:|
| `coverage:script-layer` | 6 | **10** (terminal) |
| `coverage:runtime-layer` | 6 | **8** |
| `S_members` / `S_sections` | 114 / 74 | 91 / 91 |
| `R_members` / `R_sections` | 98 / 92 | 92 / 75 |

`node scripts/proxy-check.mjs` → `PROXY: MATCH (… S=91/91 coverage:script-layer=10;
R=75/92 coverage:runtime-layer=8; K=49/49 coverage:kimi-layer=10; pins=6 match)`
exit 0; `--selftest` `VERDICT: PASS`. Registry cells corrected to live membership
(S2 lib 6→5, S4 26→6, S7 9→6, S8 60→63, R11 47→41). Commits `1a162a4`,
`0ecba26`, `edfb9c5`, `5d250b4`, `c64b380`. The K-block boundary clause (census,
not exclusive ownership — webbridge→tabi, REA keys→kaidoku, skill craft→kotoba,
secret hygiene→kagi) landed per the fleet audit. Six cross-domain defects routed
to `ufo-fsd-alpha`, not absorbed. **Carried debt:** `claims-check` exits 1 on
R11's 13 dead anchors after the file shrink (unblock: re-anchor). Two
self-inflicted defects were caught and fixed in-round: my own summary table
matched the registry-row regex (inflating `C1_total`), and I edited the stanza
while the wave was still writing notes — both recorded.

## Phase 3 — kengaku telemetry (NOT executed — named debt)

The 32-lane secondary-lane telemetry wave is **specified and validated but not
dispatched** (`.ufo/waves/shokunin12h-20261014-p3-kengaku/spec.json`, 32 members:
18 per-lane definition scopes, 3 per-key telemetry scopes, the filter-failure
dataset, bucket syntheses and 6 audits). Unblock: dispatch it; the boundary
against kumitate's file census is stated in the spec context.

## Phase 4 — mori-shokunin (minted; round 1 dispatched, partial)

**Mint landed.** `mori-shokunin/` scaffolded from the canonical seed, real
`SKILL.md`/`PROVINCE.md`/`SHONEN.md`/`MINT.md`/`corpus/` written, lane git
identity set, wired into `shokunin.conf` (now 21 entries; `bash -n` clean; 17
child lanes + protocol + aggregator + mori + chousa), seed commit `27acf40`,
MANIFEST `type: "mint"` entry appended, **no roster row**. `MINT.md` carries the
operator directive, three demand instances (the undetected webbridge OOM-death,
unsupervised fleet waves, no owner of fleet health) and the 17-lane roster scan
(`.ufo/scopes/shokunin-12h-20261014/mint-roster-scan.json`). Boundary: detection
and report only; refuses dispatch (kumitate) and OS-package state (tsukuroi).

**Probation round 1** (`Shokunin12hP4MoriR1`, 32 members) is **dispatched and
still running** at report time — 1 of 32 reports delivered. Deliverables in flight:
the observability census (watchdog liveness, wave settlement, kill/OOM classes,
cgroup memory, disk runway, lane silence), the `tools/mori-census.sh` gate design,
fixture set, finding-id vocabulary, corpus map and a live census receipt. No
round-1 verdict is claimed.

## Phase 5 — chousa-shokunin (minted; round 1 specified, not dispatched)

**Mint landed.** `chousa-shokunin/` scaffolded identically (seed commit
`02a615a`), real seed files written, lane identity set, wired into `shokunin.conf`,
MANIFEST `type: "mint"` entry appended, **no roster row**. `MINT.md` carries the
operator directive, two demand instances (`research/deep-research-2026-09-28/`
with no owning lane; kasegi is bounty-scoped only) and the roster scan. Boundary:
refuses external live-target research without operator approval, bounty scope
(kasegi) and model-quality claims (kengaku). Round 1 (research-craft survey) is
specified and validated at `.ufo/waves/shokunin12h-20261014-p5-chousa-r1/spec.json`
(32 members) but **not dispatched**.

Neither mint has earned probation credit: protocol requires ≥3 verified rounds
before a roster row, and only mori's round 1 was dispatched.

## Wave machinery

| Wave | Members | Status |
|---|---|---|
| `Shokunin12hP1Repair20261014` | 32 | 32/32 terminal; envelope `completed: 32, failed: 0, aborted: 0` |
| `Shokunin12hP1Audit20261014` | 32 | 31/32 reports delivered |
| `Shokunin12hP2Kumitate20261014` | 32 | 23/32 reports delivered; round integrated and green |
| `Shokunin12hP4MoriR1` | 32 | dispatched, running |
| `Shokunin12hP3Kengaku20261014` / `Shokunin12hP5ChousaR1` | 32 each | validated, not dispatched |

Filter-failure reroutes observed: **none** — no lane died on a route; the
requested composer/grok split was satisfied by session-only alias selection, and
the connector seat later moved to Antigravity with a ZAI fallback as instructed.
Wave dispatch used the canonical planner (`plan`/`run`/`record`) for every wave;
no wave was split across task calls. Two waves (kumitate and mori) overlapped
because the budget forced it — recorded as a deliberate deviation from strict
wave sequencing, with the harness queueing beyond the 32-lane concurrency window.

## Honest stop

This is **not** saturation and not budget exhaustion of the 12-hour window: it is
the point at which the remaining reachable work (Phases 3 and 5 dispatches, mori
rounds 2, chousa round 2) exceeded what this session could integrate with the care
the protocol requires. Every claim above is tied to a measured command; nothing
unrun is reported as passed, and no promotion, roster row, or native verdict is
claimed.
