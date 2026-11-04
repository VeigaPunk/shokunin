# kumitate — round 80 report (hyaku run 15, attempt 1)

Lane `kumitate-shokunin`, round 80, 2026-11-04; final lane tip **`01d12789`** (`git ls-remote origin refs/heads/master` = `01d127890b46e12a596af99b799177efb8ffea37`). Base `1968689f` (round-79 closure); freeze `c6a7ebd3`
(plan, both frozen counters, base receipts, pre-data controls); scaffolding `6d03402f` (the two
instrument changes + the re-measured stanza). Lane axes: **operability** and **coverage**; declared
claims: **C1 `operability`** — capability deepening `spotcheck-adopt` v3 (the spotcheck set and the
README map as two readings; delta-scoped `--adopt`), and **C2 `coverage:omp`** — the O terms re-derive
from the committed, pinned `kumitate-omp-shape-v1` receipt by default (`source=snapshot`), with the live
root as the explicit `--omp-live` opt-in. Both axis integers hold (operability 9, coverage:omp 10);
both moves are surface changes measured by their counters, not re-scores.

## Work performed

Declared claims: **C1 `operability`** (`spotcheck-adopt` v3 → v3.1) and **C2 `coverage:omp`**
(snapshot-bound O terms). The round's other work serves them, the frontier step and verification.

- **Froze the round before data** — plan with claim sentences, after-states, 13 + 12 counter arms, kill
  rules and controls; base receipts; two pre-data controls. `c6a7ebd3`; `.ufo/waves/round-80/plan.md`,
  `open/`, `controls/`.
- **C1 implemented** — `scripts/spotcheck-adopt.mjs` v3: `--check` prints `SPOTCHECK_COVERAGE:` (its own
  verdict, exit-bearing) and `MAP:` (disclosed, non-exit-bearing); `--adopt` validates its own delta
  (`otherFindings` equality + the target resolving) instead of `result.clean`. `6d03402f`.
- **C1's live repair** — the 9th spotcheck recurrence (`corpus/lessons/round-79-verifier-spotcheck.md`,
  landed by the r79 closure after the lane closed) adopted through the new rule:
  `SPOTCHECK_ADOPT: ADOPTED … wrote=both` → `README_MAP: CLEAN files=195 rows=195 covered=195`.
  `6d03402f`.
- **C2 implemented** — `scripts/proxy-check.mjs`: the default O source is `<self>/.ufo/pins/omp-shape.json`
  (`source=snapshot` in the verdict tail and `source: "snapshot"|"live"` + `sourceRead` in both JSON
  bodies), `--omp-live` opts into the live root, exclusive with `--omp-shape`/`--omp-root`, and an absent
  default receipt fails closed (`OMP_SHAPE_NOT_FOUND`). `OMP_SNAPSHOT: WROTE entries=65
  sha256=84e41b9f…`; `pin.omp-shape` re-pinned. `6d03402f`.
- **Wave** — ONE v1 wave of 13 seats under the hyaku v1 wave policy (band 8–16): 3 executors, 2 scribes,
  2 scouts, 1 connector, 2 reviewers, 1 critic, 1 mutation-tester, 1 revenger (`planner` is the L1's
  frozen-topology seat; the validator admits no `labrat`, so the C2 probe rides `revenger`) — attack
  4/13 = 31 %. Spec `.ufo/waves/round-80/w1-spec.json`, dispatch `.ufo/waves/round-80/w1-dispatch.json`,
  results `.ufo/waves/round-80/w1-results.json`: **all 13 settled, 13 reports, no dead seats**
  (`node scripts/wave-census.mjs --round 80 --root .` → `seats=13 attack=4 reports=13/13`).
- **Wave integration (v3.1)** — the seats found real holes; the tool was deepened once, after the wave,
  and the frozen counters re-read 13/13 and 12/12 against the final bytes:
  `recover()` now applies the delta rule (an interrupted adoption on a red map is no longer silently
  rolled back — scout C1-H1, reviewer R1); `otherFindings` is subject-exact (scout C1-L1, reviewer R2);
  an empty set reads `SPOTCHECK_COVERAGE: NONE` exit 1 (reviewer R3); `--predict` reads the oracle first
  (scout C1-M1); a README without `## Coverage map` is refused (scout C1-M2); a non-regular spotcheck
  entry is named in the coverage line (reviewer R5); both JSON bodies carry `sourceRead` (scout C2-M2).
  Rejected: promoting an absent census member to a finding (scout C2-H1 — the live root legitimately
  lacks `mcp.json.rea.backup`, so the promotion would flip the axis reading).
- **Stanza re-measured** — final close reading `A=886 C=39 C2=198/198 O_members=65`, `pin.proxy-check`
  and `pin.spotcheck-adopt` re-pinned to the final bytes; `PROXY: MATCH (…; source=snapshot)`.
- **Checklist truth restored** — item 742 now expects `SPOTCHECK_COVERAGE: CLEAN` (v3), item 745 is
  repointed from the r77 probe (its label arms assert `SPOTCHECK_MAP:`/`v2` and read 9/13 at these bytes;
  its semantic arms c2.5–c2.13 pass) to `.ufo/waves/round-80/probe/probe80-c1.mjs`; the `proxy-check` registry row documents the
  new default and `--omp-live`. `SKILL.md:610,631,742,745`.
- **Frontier step** — S119 re-opened (Kubernetes probes page; `used-by` extended old→new), S234 admitted
  (Terraform dependency lock file, capture bound), S235 rejected with reason + flip, S233 written then
  withdrawn after `source-dupes` caught it as a duplicate of S119. Two knowledge entries and this
  lesson landed; the round-start and round-close sources censuses are committed.
- **Record repairs routed by the r79 spot-check** — the r79 report carries an appended erratum (D1, D2,
  D8), `corpus/lessons/round-79.md` carries Erratum 2 (D3, D4) and Erratum 3 (the D3 sentence's reach),
  `SCORECARD.md` carries the D5 correction and the round-78 placeholder correction, and the round-80
  receipts all carry `rev=` (D6) with the round-start census committed (D7). `K80ExecRepairs` audited
  all eight.
- **Honesty amendments** — the plan carries two appended amendments (Amendment 1: the `spotchecks=47`
  count and the `C2=197` stanza; Amendment 2: the `controls/*-base.txt` pointers, the census's late
  capture, the lane-state-dependent base counts, the preservation arms, the selftest floor, the
  synthetic arm 12, the recovery-arm wording, and the `A` move) — both name the superseded text.

## Landed changes

Every change is tied to its `LOG.md` entry (`LOG.md`, the round-80 section) and to the commit that
carries it.

| change | commit | evidence |
|---|---|---|
| freeze: plan, counters, base receipts, controls | `c6a7ebd3` | `.ufo/waves/round-80/plan.md`; `open/`; `controls/` |
| `spotcheck-adopt` v3 (two readings, delta-scoped adopt) + the r79 spotcheck adoption + stanza/pins | `6d03402f` | `scripts/spotcheck-adopt.mjs`; `corpus/README.md`; `.ufo/pins/`; `SCORECARD.md`; `SKILL.md` |
| `proxy-check` snapshot default + `--omp-live` + four selftest arms | `6d03402f` | `scripts/proxy-check.mjs`; `close/proxy-selftest.txt` |
| wave spec + validated dispatch (13 seats) | `ed64ddca` | `w1-spec.json`; `w1-dispatch.json` |
| two sourced knowledge entries + captures + SOURCES rows (S234 admitted, S235 rejected, S119 `used-by`) + r79 lesson erratum + round-start census | `509afb1d` | `corpus/knowledge/*.md`; `corpus/SOURCES.md`; `corpus/lessons/round-79.md`; `open/sources-census.txt` |
| v3.1 integration + final pins + lesson + LOG + SCORECARD + PROVINCE + plan amendments + control sources | `42d93b95` | `scripts/*.mjs`; `corpus/lessons/round-80.md`; `LOG.md`; `SCORECARD.md`; `PROVINCE.md`; `controls/` |
| S233 withdrawal landed (S119 `used-by`, entry A, capture entry) | `6cbd6750` | `corpus/SOURCES.md`; `corpus/knowledge/two-reading-verdicts.md`; `.ufo/pins/source-captures.json` |
| close receipts, re-measured at the final tip and `rev=`-stamped | `01d12789` | `.ufo/waves/round-80/close/` |
| report (this file, filed on the fleet repo) | fleet commit | the report path named in the round prompt |

## Before → after measurements

**C1 — `operability`** (integer held 9; `f_O` is terminal). Counting command:
`node .ufo/waves/round-80/probe/probe80-c1.mjs --set c1`.
- Base `1968689f` (`--tool <git archive>`): `C80_C1: HELD held=6/13`, exit 1 (`open/c1-base.txt`);
  constant-CLEAN control stub `held=3/13` (`controls/c1-stub.txt`, source committed at
  `controls/c1-stub.mjs.txt`).
- Final bytes: `C80_C1: HELD held=13/13`, exit 0 (`close/c1-probe.txt`). The discriminating pair: the same
  command reads `SPOTCHECK_COVERAGE: CLEAN … uncovered=0` + `MAP: DRIFT first=uncovered:knowledge/late.md`
  exit 0 on a green-spotcheck/red-map fixture, and `SPOTCHECK_COVERAGE: DRIFT … uncovered=1` exit 1 on an
  uncovered spotcheck; the critic's conflated candidate scores 10/13 and fails exactly arms 3, 4 and 8.
- Lane reading: `SPOTCHECK_COVERAGE: CLEAN spotchecks=46 uncovered=0` + `MAP: CLEAN` exit 0
  (`close/spotcheck-check.txt`); `--selftest` 34/34 (`close/spotcheck-selftest.txt`).

**C2 — `coverage:omp`** (integer held 10; the axis's measurement becomes offline re-derivable).
Counting command: `node .ufo/waves/round-80/probe/probe80-c2.mjs --set c2`.
- Base `1968689f`: `C80_C2: HELD held=4/12`, exit 1 (`open/c2-base.txt`); constant-JSON control stub
  `held=1/12` (`controls/c2-stub.txt`, source committed at `controls/c2-stub.mjs.txt`).
- Final bytes: `C80_C2: HELD held=12/12`, exit 0 (`close/c2-probe.txt`). Arm 1 vs 2 is the
  discrimination: the same 68-member fixture root reads `O_members=65 source=snapshot` (default) and
  `O_members=68 source=live` (`--omp-live`); arm 3 reads MATCH with `OMP_AGENT_ROOT=/nonexistent`.
- Lane reading: `PROXY: MATCH (A=886 C=39 operability=9; C1=19/19 C2=198/198 coverage=10; S=88/88
  coverage:script-layer=10; R=92/92 coverage:runtime-layer=10; K=55/55 coverage:kimi-layer=10; O=1/1
  O_members=65 O_findings=0 O_bound=35 coverage:omp=10; pins=6 match; src-rev=31c465f15669;
  source=snapshot)` exit 0 (`close/proxy-check.txt`); `OMP_CENSUS: CLEAN (source=snapshot entries=65
  findings=0 bound=35/35)` and `OMP_SHAPE_COMPARE: IN_SYNC entries=65 receipt=65`
  (`close/census-shape.txt`); the real live root under `--omp-live` reads `O_members=65`
  (`close/omp-live-real.txt`).

## Sources & frontier

Counting command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`
— round open: exit 0, rows 171, tier A 146 / B 16 / C 9 (`open/sources-census.txt`, captured after the
freeze at tip `ed64ddca` — plan Amendment 2 discloses the late capture); round close: exit 0, rows 173,
tier A 147 / B 16 / C 10 (`close/sources-census.txt`).

- Rows added by tier: **A +1** (S234), **C +1** (S235, rejected), **A ±0** for S119 (re-opened, no new
  row; `status`/`recheck` unchanged, `used-by` extended).
- Rows touched old→new: **S119 `used-by`** `corpus/knowledge/worker-heartbeat-liveness.md` →
  `…, corpus/knowledge/two-reading-verdicts.md` (logged in `corpus/lessons/round-80.md` §Gate).
  **S233 written then withdrawn** — `source-dupes` read `new-duplicate … ids=S119,S233`; the row is gone,
  the entry cites S119, and the withdrawal is a `## Mistakes` row. No other `status` or `recheck` changed.
- Frontier rows advanced: `PROVINCE.md`'s round-80 addition names the two entries (two-reading verdicts
  S119; snapshot-bound derived scores S234) as the band's advance, with the adjacent boundaries stated
  (kotoba's report-pointer ground stays reported, never absorbed).
- Assimilation (`§10`): **none** — `merge/kumitate/` was not taken; the work is the lane's own
  instruments. The census gate is clean at both ends (`census_exit=0`).

## Trend verdicts

- **expansion — improved.** Two admitted `knowledge/` entries on ground the README map did not hold,
  each citing a row opened (S119 re-opened, S234 admitted) this round; README map 195 → 198 files
  (`close/readme-map.txt`); SOURCES 171 → 173 by
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; tier A 146 → 147; the
  rejection S235 is kept with its flip condition.
- **quality — improved.** Two instruments gained discriminating behavior the base and a constant printer
  cannot reach (C1 base 6/13, stub 3/13; C2 base 4/12, stub 1/12); both selftests grew (spotcheck-adopt
  26 → 34 cases, proxy 159 → 163); the wave's own findings were integrated into the tool rather than
  transcribed (v3.1), and the counters re-read 13/13 and 12/12 against the final bytes; the r79 record
  defects D1–D8 are repaired by appended errata and by this round's regime (`rev=` receipts, committed
  start census).
- **discernment — improved.** The round's own gates caught the author three times: `source-dupes` killed
  the duplicate S233 row; the close sweep caught the r77 probe's label arms red; the wave's critic and
  mutation-tester showed that four mutant classes and one candidate still pass the frozen counters (now
  in `## Limits`), and the freeze reviewer showed three plan prose errors (now Amendment 2). An outside
  (non-author) spot-check of this round is still owed by the closure; this report does not claim it.

## SHONEN

All four boxes are author-asserted (`[~]`); the promotion gate requires a named non-author verifier for
`[x]`, and none has been recorded for this round.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the gate
  registry carries `spotcheck-adopt` v3 (two readings, delta rule) and the `proxy-check` row documents
  the receipt default and `--omp-live`; items 742/745 were corrected and re-run (`SKILL.md:610,631,742,745`;
  `close/checklists.txt`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the 9th spotcheck recurrence
  was repaired through the new delta rule and the O terms now re-derive offline from the pinned receipt
  (`LOG.md` round-80 section; `close/c1-probe.txt`, `close/c2-probe.txt`, `close/omp-live-real.txt`).
- [~] Instructions executable by an agent without oral context — plan + counters + close sweep re-run
  from a fresh clone; every close receipt carries `rev=` naming the measured revision.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the two entries are orchestration/tooling
  ground; report-pointer resolution stays kotoba's (reported, never absorbed) and the round-80 addition
  states the boundary.

**Stale-lane:** none — respawn-per-round driver; this round is the lane's only mission.

**Tool installs:** none this round (no tool was needed; pacman untouched).
