# kumitate — round 76

**Claims declared (2, distinct axes).** C1 `coverage:omp` — the OMP agent plane stops being the one
live axis row `proxy-check` does not derive: it becomes registry family `O1`, the proxy imports the
census decision and derives `coverage_omp`, six additive stanza keys land, and `AXES_DRIFT` gains a
sixth row. C2 `operability` — capability acquisition `spotcheck-adopt`: the two-sided README-row +
covered-pin repair that rounds 72–75 did by hand becomes one constrained command with the unchanged
`readme-map.mjs` as its child oracle, refusals for everything outside its scope, both half-state
repairs and pre-image rollback. Lane axes per `MISSION.md`: operability + coverage (orchestration and
tooling).

**Round shape.** ONE v1 wave of 12 seats under `ufo-wave-policy.json` band 8–16: 2 scout, 2 executor,
2 scribe, 1 reviewer, 1 critic, 2 mutation-tester, 1 sentinel, 1 connector; 12 settled, 0 dead; no
residual call, round total **12**. Attack seats 5/12 = 42 % by declared role (reviewer, critic,
mutation-tester ×2, sentinel); `wave-census`'s fixed attack set counts 4/12 = 33 % (it excludes
sentinel). The canonical §3 planner seat is held by the L1 — the validator rejects `planner` as a
swarm role (orchestrator ruling 2026-10-19). Dispatch: `.ufo/waves/round-76/w1.ready` →
`w1.ready.dispatched`, payload `w1-dispatch.json` (`counts.spawn=12 resume=0`), results
`w1-results.json`, `WAVE_CENSUS: CLEAN (rounds=1 waves=1 findings=0)` (`close/gates.txt`).

## Work performed

- **Frozen plan before data** — `.ufo/waves/round-76/plan.md` committed in scaffolding
  `cabc7aefd5f1562299f757e23207710c12e4ed58` with every open/base receipt and every pre-data control
  it names; corrections (A1.1–A1.6, all pre-verdict) appended as `## Amendment 1` in `beb8a934…`.
- **C1 mechanism** — `scripts/omp-census.mjs` now exports `BASE_MEMBERS`, `CHAIN_FAMILIES`, `census`
  (the `isMain` guard keeps the CLI unchanged); `scripts/proxy-check.mjs` gains `--omp-root`
  (default `$OMP_AGENT_ROOT` or `~/.omp/agent`), the six additive terms, the `coverage:omp` axis row
  and the `OMP_ROOT_NOT_A_DIR` / `OMP_NOTE_MISSING` refusals. Evidence: `close/c1-json.txt`,
  `close/proxy-check.txt` (`PROXY: MATCH` exit 0), `close/proxy-selftest.txt` (`145/145`),
  `close/omp-selftest.txt` (`49 cases`), `close/c1-failclosed.txt`, `close/c1-negative-roots.txt`.
- **C1 registry binding** — registry family `O1` in `SCORECARD.md` (members 26 base + 9 chain
  families; note `knowledge/omp-agent-root.md`), the note's new `## Registry binding — family O1`
  section that indexes all 35 declared identifiers to their existing rows (census re-reads
  `bound=35/35`, `close/omp-census.txt`), and the `## Axes` row's evidence rewritten to the derived
  formula.
- **C2 mechanism** — new `scripts/spotcheck-adopt.mjs` (contract `kumitate-spotcheck-adopt-v1`):
  `--check`, `--adopt`, `--predict`, `--lane`, append-only two-sided writes, pre-image restore,
  oracle as a child process. Evidence: `close/spotcheck-adopt.txt` (real adoption, `wrote=both` +
  `README_MAP: CLEAN files=182 rows=182 covered=182`), `close/c2-idempotent.txt` (second run
  `ALREADY_ADOPTED`, byte-identical), `close/c2-refusals.txt` (three refusals, exit 2, zero bytes
  changed), `close/c2-after.txt` (`PENDING 76` / `COVERED 75` / `CHECK + README_MAP: CLEAN 183/183/183`),
  `close/adopt-selftest.txt` (`16/16`).
- **Falsification** — 13-mutant battery on the final bytes, `MUTANTS76: ALL-KILLED killed=13/13`
  (`close/mutants.txt`, pristine pairs in `close/mutants-pristine.txt`, battery itself
  `close/mutants76.mjs`): C1-M1 drops the findings subtraction, C1-M2 is the constant-10 printer,
  C1-M3 scores an unreadable root as clean, C1-M4 drops the note refusal, C1-M5 drops the AXES row,
  C1-M6 inflates `C1o` from legacy rows; C2-M1/M2 are the two one-sided writes, C2-M3 a symlink
  escape, C2-M4 accepts any lessons file, C2-M5 loses idempotency, C2-M6 predicts an absent artifact
  as covered, C2-M7 drops the pre-image restore. Two seats' own batteries (design-level, against
  stand-ins) are in `build/K76MutProxyO/`, `build/K76MutAdopt/`; the receipt that binds the claims
  is the final-bytes one.
- **Wave seats' independent records** — `w1/*.md`: freeze review (6 FREEZE-FIX items, all
  dispositioned in `Amendment 1` or disclosed), critic (`CLAIMS: BROKEN C1` on the literal JSON
  count — recorded, not smoothed), sentinel boundary probes, scout design map, source row draft,
  note draft, learning-record draft, connector overlap scan (a round-63 archived two-sided-writer
  proposal named as C2's local precursor, not absorbed).
- **Routed repairs (not claims)** — the 5th spotcheck-coverage recurrence repaired **by C2's tool**;
  SKILL gate rows for `harm-matrix` and `make-dispatch-actual` (Q68 debt from rounds 65/62), the
  `spotcheck-adopt` row and two checklist items; stanza re-measure; re-pins; R75-spotcheck D1/D2
  errata; four mistakes mined in `corpus/lessons/round-76.md ## Mistakes` (control-fixture path
  shape, predicate-count-vs-schema, freeze-under-red-map, control-token spelling) plus the
  adopt-appends-at-eof placement limit.
- **Wave evidence committed** — spec, dispatch payload, registry, 12 seat reports, results, build
  artifacts and every close receipt under `.ufo/waves/round-76/` (`wave-census` CLEAN).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| frozen plan + open/base receipts + pre-data controls; validated 12-seat spec + dispatch | round-76 entry, `LOG.md` | `cabc7aef…` (scaffolding), `0ee0b2a7…` (wave payload) |
| C1 derivation + registry `O1` + note section + SCORECARD/SKILL/stanza/pins; C2 `spotcheck-adopt`; lesson, SOURCES S226, capture, README rows, LOG, round section, plan Amendment 1 | round-76 entry, `LOG.md` | `beb8a934e9b2d0bb45c64e11c38d4fb370d3205f` (work) |
| close receipt set at the work revision (strict MATCH, 35/35 checklists, 13/13 mutants, gate sweep, census end, seat census) + wave markers/results | round-76 entry, `LOG.md` | `cf1cdc5ae8540de75b3d783a85ce57af99424738` (close) |

Lane tip at filing: **`cf1cdc5ae8540de75b3d783a85ce57af99424738`**; `jj-lane.sh state` reads
`local=cf1cdc5a remote=cf1cdc5a ahead=0 behind=0` and `git ls-remote origin refs/heads/master`
prints the same hash.

## Before → after measurements

| claim | counting command | before (base `ebfcedfa`) | after (work `beb8a934`) | verdict |
|---|---|---|---|---|
| C1 | `node scripts/proxy-check.mjs --json \| grep -c '"coverage_omp"'`; `grep -c '^\| O1 \|' SCORECARD.md` | `0`; `0` (`open/proxy-json-open.txt`) | `2`; `1`; terms `C1o=1 C1o_total=1 O_members=64 O_findings=0 O_bound=35 coverage_omp=10`, `PROXY: MATCH --strict` exit 0 (`close/c1-json.txt`, `close/proxy-check.txt`) | **literal clause (a) does not verify** (2 ≠ 1, `terms.declared` duplicate; A1.1) — every other clause verifies ⇒ claim reported as *improved, literal miss disclosed* |
| C1 (negatives) | `node scripts/proxy-check.mjs --omp-root <shape root>` | no `--omp-root` option (exit 64) | +1 member → `65/1/9` drift; +10 → `74/10/8`; both fail-closed arms exit 2; 6/6 C1 mutants killed (`close/c1-negative-roots.txt`, `close/mutants.txt`) | verifies |
| C2 | `node scripts/readme-map.mjs`; `node scripts/spotcheck-adopt.mjs --check`; `--adopt corpus/lessons/round-75-verifier-spotcheck.md` | `README_MAP: DRIFT files=182 rows=181 covered=181 bad=2 first=uncovered:lessons/round-75-verifier-spotcheck.md` exit 1; no tool (`MODULE_NOT_FOUND`) (`open/maps-open.txt`, `open/adopt-absent.txt`) | `README_MAP: CLEAN files=183 rows=183 covered=183` exit 0; `SPOTCHECK_MAP: CLEAN spotchecks=42 uncovered=0`; adoption `ADOPTED … wrote=both`; second run `ALREADY_ADOPTED` byte-identical; 7/7 C2 mutants killed (`close/spotcheck-adopt.txt`, `close/spotcheck-adopt-at-M.txt`, `close/c2-idempotent.txt`, `close/mutants.txt`) | **improved** (capability acquisition) |
| axes | `node scripts/proxy-check.mjs --strict` | `PROXY: DRIFT` (C2_total 181/182, retired-coverage AXES row) | `PROXY: MATCH (A=847 C=35 operability=9; C1=19/19 C2=183/183 coverage=10; … O=1/1 … coverage:omp=10; pins=6 match)` exit 0 | no axis harmed |

Checklists: `CHECKLIST: 31/33 pass` at open (`open/checklists-open.txt`, red: proxy recompute and
readme-map) → `CHECKLIST: 35/35 pass`, `VERDICT: PASS` at the work revision
(`close/checklists-AFTER.txt`). Proxy suite 132 → 145 cases; adopt suite 16/16 new.

## Sources & frontier

`corpus/SOURCES.md` 164 → **165** rows; tier A 140 → **141** (S226 `code`), tier B 16 unchanged,
tier C 8 unchanged. Command:
`node scripts/sources-check.mjs` → `SOURCES_CHECK: CLEAN (rows=165 tiers=A:141,B:16,C:8 …)`; fleet
census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate` exit 0 at
round start (`open/sources-census-open.txt`) and at round end (`close/census-end.txt`), six carried
W04 duplicate-URL warnings unchanged.

- Rows added: **S226** — oh-my-pi `packages/utils/src/dirs.ts` at `v18.15.0`, tier A, `mined`, used
  by `corpus/knowledge/omp-agent-root.md`. Opened 2026-11-04 (HTTP 200, 52434 bytes, sha256
  `2d423f4f…`, byte-identical to S053's `v18.12.6` file — `cmp` on two independent fetches exits 0);
  located quotes at lines 949, 991-992, 1052-1054, each ≤ 25 words. Capture
  `.ufo/waves/round-76/build/K76ScoutDirsRelease/dirs-v18.15.0.ts`, `SOURCE_CAPTURE: CLEAN
  captures=57 exemptions=108`.
- Rows touched old→new: none (no `status`/`recheck`/`used-by` changes; S226 is the only edit).
- Frontier rows advanced: the OMP agent plane's `## Frontier` line records that its living axis is
  now registry-bound and derived (family `O1`, `coverage_omp`), with S226 re-grounding the member
  file at the installed release; a named coverage gap stays open (five `agentSubdir` names the census
  does not declare — `modules`, `omp-crash.log`, `omp-debug.log`, `python-gateway`,
  `secret-placeholder.key` — all absent on this host).
- **Assimilation: none** — the `merge/kumitate/` package now reads 161 rows / 70 entries, larger than
  the 155/70 the round-75 spot-check measured; admitted as a *carried reject* with the flip "a
  dedicated assimilation round that re-grounds entries one at a time". `considerthese/2026-10-26.md`:
  proposals 1/2/3/4 are already criteria Q70/Q71/Q68/Q69; proposal 5 is the closure judge's format,
  not the lane's; proposal 6 (counter trend series) is not implementable at this lane's bar without a
  new counter — no still-unimplemented proposal adopted this round (none is claimed as executed).

## Trend verdicts

- **expansion: improved.** The OMP plane moves from an axis row outside the registry to registry
  family `O1` derived by the proxy (six terms, AXES-checked), and the lane's repair surface gains one
  standing constrained command. SOURCES 164 → 165 with S226 admitted on a byte-identical
  installed-release file; the frontier line records both the advance and the five undeclared members.
- **quality: improved.** Checklists 31/33 → 35/35; proxy suite 132 → 145; the new tool's 16/16 suite
  includes both half-states, three refusals, the symlink escape and byte restoration; a 13-mutant
  battery kills every arm on the final bytes; `PROXY: MATCH --strict` and every gate in
  `close/gates.txt` read or explain their state (the two red legs are the pre-filing report and the
  red-at-freeze map arm, both named).
- **discernment: improved.** The reviewer's six FREEZE-FIX items were dispositioned before verdicts
  (A1.1–A1.6 or disclosed), the critic's `CLAIMS: BROKEN C1` is reported rather than argued away, a
  seat battery that did not align with final literals is disclosed and superseded by the final-bytes
  receipt, and four own mistakes plus one placement limit are mined with captured-by fields.

## Limits, disclosed

- **C1(a)`s literal predicate missed** (2 ≠ 1); the corrected reading is the operative one and both
  are printed above (Amendment 1 A1.1).
- **C1's integer is host-bound**: `coverage_omp` reads the live `~/.omp/agent` shape, so a closure
  re-runs it on this host rather than re-deriving it from committed bytes; the shape-only negative
  roots are committed receipts, not the root itself.
- **C2's two renames are not a transaction**: a kill between them leaves a half-state a later adopt
  repairs; no stronger guarantee is claimed (round-77 candidate).
- **`plan-before-ready --round 76` reads `FAIL … map=DRIFT`**: the plan was committed while
  `README_MAP` was red; the close is green, the plan archive stays red by design
  (`close/gates.txt`; mistake mined).
- **`round-gate --round 76` reads `DRIFT … REPORT_MISSING`** in `close/gates.txt` because it was run
  before this report was filed; the round record otherwise passes (no other findings).
- Seats observed node `v26.12.0` on their PATH; every lane receipt was run with `v24.21.0` and says
  so in its header (Amendment 1 A1.5).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — gate
  registry now 27 rows over 26 files, 35/35 checklist items execute (`close/checklists-AFTER.txt`),
  S226 grounds the new row (`corpus/SOURCES.md:181`).
- [~] At least one end-to-end domain task executed and logged — C2 adopted the round-75 closure lesson
  end-to-end on the live tree (`close/spotcheck-adopt.txt`) and LOG.md round 76 records it.
- [~] Instructions executable by an agent without oral context — frozen plan + `## Amendment 1` +
  the 12 seat prompts (`w1-spec.json`) + `w1/*.md` reports; no step requires the conversation.
- [~] No cross-domain bleed — `PROVINCE.md` unchanged; OMP member content stays out of scope by design;
  the connector's sibling scan is read-only and reports, never absorbs
  (`build/K76ConnectorOverlap/revisions.txt`, `w1/K76ConnectorOverlap.md`).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none. (Tooling authorization noted in every seat context; `pacman` stayed paused; no
`uv`/`npx`/binary install was needed.)
