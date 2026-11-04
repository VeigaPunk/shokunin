# kumitate round 77 — offline OMP shape receipt (coverage:omp) and a crash-recoverable adopt journal (operability)

Declared claims (2, frozen before data in `.ufo/waves/round-77/plan.md`):

- **C1 — coverage:omp.** The plane's score stops being a live-host term: a canonical,
  committed and pinned `kumitate-omp-shape-v1` receipt (`omp-census --snapshot` / `--shape`,
  `proxy-check --omp-shape`, `pin.omp-shape`) is judged offline, and the six O terms follow the
  receipt rather than the live root. Integer pre-registered to stay 10 (64/64 already saturates).
- **C2 — operability.** Capability deepening `spotcheck-adopt` v1 → v2
  (`kumitate-spotcheck-adopt-v2`): a versioned adopt journal makes the two-file adoption
  crash-recoverable (exact `RECOVERED <target> rolled-back|complete`, stale/stale-tmp,
  foreign-journal and corrupt-pre-image refusals), canonicalises destination parents, and places
  the map row after the last lessons row. Operability integer stays 9 (`f_O` is terminal).

Lane: `/home/vgpnk/Projects/shokunin/kumitate-shokunin`, base `a321ed80`, scaffolding `4dc470a1`,
work commit M = `e47266ae`; close receipts `7316b0ce` + cited-receipt commit `640cadf1`; lane tip at filing `3231b11c`. Host: Linux 7.2.11-arch1-1,
node v24.21.0, harness `omp/18.15.0`.

## Work performed

- **C1 contract and counter.** `scripts/omp-census.mjs` gained `--snapshot FILE [--root DIR]`
  (canonical receipt: sorted `{name,kind,mode}` entries only, staged then renamed, one
  `OMP_SNAPSHOT: WROTE entries=<n> sha256=<hex> path=<p>` line) and `--shape FILE` (the unchanged
  rule tables over the receipt, `OMP_CENSUS: CLEAN|DRIFT (source=snapshot …)`,
  `SHAPE_INVALID`/`SHAPE_NOT_FOUND` exit 2). `scripts/proxy-check.mjs` gained `--omp-shape FILE`
  (six O terms offline, `source=snapshot` in JSON and the line, `OMP_SHAPE_INVALID`/
  `OMP_SHAPE_NOT_FOUND`, exclusive with `--omp-root`) and `GATE_PINS['pin.omp-shape']`
  (`scripts/proxy-check.mjs:541`). The committed receipt is `.ufo/pins/omp-shape.json`
  (64 entries, sha256 `5980a0c8…`), pinned in the lane-owned gate block; evidence
  `.ufo/waves/round-77/close/c1-probe.txt` (`C77_C1: HELD held=12/12`), `close/c1-json.txt`,
  `close/proxy-check.txt` (`PROXY: MATCH`, exit 0).
- **C2 journal.** `scripts/spotcheck-adopt.mjs` v2 publishes
  `.ufo/pins/adopt-journal/<uuid>/` (manifest + both pre-images) before either destination write,
  recovers on every non-selftest arm, retires a journal by rename before deletion, inserts the
  row after the last lessons row, and refuses a symlinked destination parent
  (`REFUSED_PATH_ESCAPE`). Evidence `close/c2-probe.txt` (`C77_C2: HELD held=13/13`),
  `close/adopt-selftest.txt` (`SPOTCHECK_ADOPT_SELFTEST: PASS (26/26)`), `close/mutants77-c2.txt`
  (`ALL-KILLED killed=8/8`), `close/spotcheck-check.txt` (`CLEAN spotchecks=43 uncovered=0`).
- **Pre-data falsification.** One v1 wave, 13 seats: the freeze reviewer built a constant printer
  that met the v1 kill rule's `c1.5`/`c1.6` (`build/K77ReviewFreeze/printer-c1.txt`, `held=5/10`),
  the C1 reviewer and critic independently found the unregistered `c2.11` name
  (`build/K77CriticClaims/predicate-name-mismatch.txt`), and the sentinel confirmed an
  outside-lane write through a symlinked `.ufo/pins` (`build/K77SentinelBoundary/report.md`).
  All three became pre-verdict counter amendments or routings (below), not silent fixes.
- **Registry and record.** `SKILL.md` gate-registry rows for the new arms and two executable
  checklist items (`SKILL.md:742-743`); `SCORECARD.md` axis evidence, capability-deepening note,
  limits, round-78 pre-registration and the round-77 section; `corpus/knowledge/
  crash-recoverable-two-file-adoption.md` (S227) and an `## Offline shape receipt (round 77)`
  section on `corpus/knowledge/omp-agent-root.md`; `corpus/lessons/round-77.md`; `LOG.md`
  round-77 entry; Q72 in `corpus/QUALITY.md` (per-round counter series, from
  `considerthese/2026-10-26.md` proposal 6) and Q22-C1 (the round-41 axis-set command mis-parses
  escaped pipes; the corrected extraction matches the report's six axes).
- **Routed repairs (not claims).** The 6th spotcheck recurrence and `readme-map.json`'s lost final
  newline (r76 D4) repaired in the scaffolding commit, so the freeze's map arm is GREEN
  (`open/plan-before-ready-freeze.txt`: `map=CLEAN`; at M `PLAN_BEFORE_READY: pass=1`); the
  cleanup half-journal window (retire-by-rename) and the symlinked-pin escape (canonical parents)
  fixed in the work commit; r76 FREEZE-FIX 6 disposition with the real loader diagnostic
  (`open/r76-freeze-fix-6-disposition.txt`); the r76 carried-reject count corrected to **155 rows
  / 161 lines / 70 entries** (unchanged, not larger) in `corpus/lessons/round-77.md`; R75 D4's
  why-not (operator-owned instrument) recorded there.
- **Wave shape.** 13 seats, all settled, 0 dead, 13/13 reports (`close/seat-census.txt`,
  `close/wave-census.txt`, `w1-results.json`). The L1 held the canonical planner seat (the
  validator rejects `planner` as a swarm role). No tools installed.

## Landed changes

| commit | content | LOG entry |
|---|---|---|
| `4dc470a1` | frozen plan + v1 counter + open/base receipts + pre-data controls + S227 row/capture + routed map/pin repair | LOG.md round 77 |
| `794704aa` | counter amendment A1 (placement fixture + registry name) | same entry |
| `9bb6f5b2` | counter amendment A2 (v2: discriminating offline arms; v1 printer kill-rule hit disclosed; v1 bytes preserved) | same entry |
| `d5f91f90` | A2.4 (c2.12 adjacency self-comparison) | same entry |
| `e47266ae` | **M** — C1 + C2 instruments, receipt/pins, SKILL rows + 2 checklist items, SCORECARD, corpus entry/extension/lesson, LOG, Q72, wave evidence | same entry |
| `3231b11c` | close receipts at M (probes, selftests, strict gate, maps, sources, batteries, checklists, plan gate); Q22-C1 (axis-set extraction corrected for escaped pipes) | same entry |

## Before → after measurements

**C1** — counting command
`node .ufo/waves/round-77/probe/probe77.mjs --set c1 --lane <tree>`:

- before, base tree `a321ed80`: `C77_C1: UNMET held=1/12` (`controls/c77-c1-base.txt`);
  `--snapshot`/`--shape`/`--omp-shape` are usage 64 (`controls/c1-usage-base.txt`).
- after, M `e47266ae` (re-verified from `git archive 3231b11c`): `C77_C1: HELD held=12/12` (`close/c1-probe.txt`) — the committed receipt
  equals the independent open lstat receipt and replays byte-identically from a materialised root
  (`5980a0c8…`); `--shape` reads `CLEAN (source=snapshot entries=64 findings=0 bound=35/35)`; the
  six O terms are `1/1 64/0/35 10` offline and from the materialised root, and a trimmed 63-entry
  receipt yields `O_members=63`; a stray member and a 0604 `agent.db` each read
  `O_findings=1 coverage_omp=9`; malformed/absent/content-key receipts, malformed proxy receipt and
  both flags fail closed; a zeroed `pin.omp-shape` reads `GATE_PIN_DRIFT`. Selftest 58 cases;
  `MUTANTS77_C1: ALL-KILLED killed=6/6` (`close/mutants77-c1.txt`).
- control: a hand-typed receipt + constant printer reads `held=4/12`
  (`controls/c1-constant-printer.txt`).

**C2** — `… --set c2 --lane <tree>`:

- before, base tree: `C77_C2: UNMET held=2/13` (`controls/c77-c2-base.txt`; only the two trivial
  negatives); the live map was red (`SPOTCHECK_MAP: DRIFT uncovered=1`,
  `README_MAP: DRIFT files=184 rows=183`).
- after, M: `C77_C2: HELD held=13/13` (`close/c2-probe.txt`) — three real SIGKILL windows converge
  with one exact `RECOVERED <target> rolled-back|complete` line, byte-exact; a corrupt pre-image is
  `REFUSED_ORACLE` with journal and destinations retained; a foreign journal is
  `REFUSED_JOURNAL_FOREIGN`; `--predict` recovers first; the adopted row is adjacent to the last
  lessons row; the lane map reads `files=186 rows=186 covered=186`; a symlinked destination parent
  is `REFUSED_PATH_ESCAPE` (the sentinel's attack now refuses, external file untouched). Selftest
  26/26; `MUTANTS77_C2: ALL-KILLED killed=8/8` (`close/mutants77-c2.txt`).
- control: an unconditional `RECOVERED` printer reads `held=0/13`
  (`controls/c2-constant-printer.txt`).

**Cross-terms at M** (`close/proxy-check.txt`, `close/proxy-json.txt`; the same values and both probes reproduce from `git archive 3231b11c`): A 847 → 857, C 35 → 37,
C2/C2_total 183 → 186, `PROXY: MATCH` strict exit 0; checklists 32/35 at open → 37/37 at close
(`close/checklists.txt`); census 64/0/35 both ends.

## Per-axis verdicts

| axis | verdict | claims | basis |
|---|---|---|---|
| operability | improved | C2 | capability deepening `spotcheck-adopt` v2; integer held 9 (terminal); counter held 13/13, selftest 26/26, battery 8/8 |
| coverage | unchanged | — | retired aggregate; derived 10 at M; no change |
| coverage:script-layer | unchanged | — | 88/88 at the pinned origin `31c465f1`; `PROXY: MATCH` |
| coverage:runtime-layer | unchanged | — | 92/92; `PROXY: MATCH` |
| coverage:kimi-layer | unchanged | — | 55/55; `PROXY: MATCH` |
| coverage:omp | improved | C1 | score re-derivable offline from the pinned receipt; integer held 10; counter held 12/12, battery 6/6 |

counted claims=2 (two distinct axes; no axis harmed — every derived term matches its declaration at M).

## Round shape

WAVE kumitate-r77-w1 payload=13 spawned=13 returned=13 dead=0 gate=granted

FLOOR wave1 spawned executor=2/3 scribe=2/1 scout=2/1 connector=1/1 reviewer=2/1 critic=1/1 verdict=met

spawned total=13 (<=128)
- Deviation: none from the allowed shapes. Attack share 6/13 = 46 % by declared role
  (`reviewer` ×2, `critic`, `mutation-tester` ×2, `sentinel`); the lane's `wave-census` fixed attack
  set excludes `sentinel` and reads 5/13 (`close/wave-census.txt`), disclosed.

## Sources & frontier

`SOURCES.md` rows **165 → 166** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`);
census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kumitate` → exit **0** at round end (`close/sources.txt`, six carried
W04 warnings; exit 0 at open too, `open/sources-census-open.txt`). Rows added by tier: **A +1**
(S227, 142 total). Rows touched old→new: S227 `status` `queued` → `mined`, `used-by` `—` →
`corpus/knowledge/crash-recoverable-two-file-adoption.md` (logged in the lesson); S226 re-opened,
no change. Frontier rows advanced: the `coverage:omp` evidence band now carries the offline receipt
(`corpus/knowledge/omp-agent-root.md` § Offline shape receipt), and the durable-execution/adoption
band gains the journal entry on S227. `SOURCE_CAPTURE: CLEAN captures=58 exemptions=108`;
`SOURCE_DUPES: CLEAN groups=6 known=6`.

Assimilation: **none**. `merge/kumitate/` re-opened read-only: `SOURCES.append.md` 155 S-rows over
161 lines, `MERGE-REPORT.json` 70 entries, `accepted=155`, `refused=[]`, `renumbered=0` — unchanged
from round 75 (r76's "larger" reading corrected). Refused as a bulk append on §10 proportionality
and CORPUS.md rule 4; flip is a dedicated assimilation round. `considerthese/2026-10-26.md`
proposal 6 mined as Q72; proposals 1–5 remain open.

## Trend verdicts

- **expansion: improved.** One admitted entry (`crash-recoverable-two-file-adoption.md`) citing the
  mined S227 row, one gallery extension on the OMP-plane note, SOURCES 165 → 166, and a capability
  deepening entered in the same round that ran it; the coverage map is 186/186 with no uncovered
  file.
- **quality: improved.** `PROXY: MATCH` strict at M with the stanza re-measured in the same
  commit; checklists 32/35 → 37/37; selftests 49 → 58 cases (census) and 145 → 151 (proxy);
  adopt selftest 16 → 26; both mutant batteries all-killed on the final bytes; `README_MAP: CLEAN
  186/186`; no admitted entry failed a re-check.
- **discernment: improved.** Pre-data falsifiers found four real instrument/predicate defects
  (constant printer vs the v1 kill rule, unregistered check name, cleanup half-journal, symlinked
  pin escape); each became a counter amendment, a routed fix or a disclosed limit, and all are
  mined in `corpus/lessons/round-77.md ## Mistakes`. The outside closure spot-check of the two
  gate decisions (S227 admit, package reject) is pending its file.

## Limits, disclosed

Receipt age vs drift: the shape receipt proves the plane at capture and does not track later root
changes (the live default remains the live reading). The adopt journal assumes one writer per lane
and claims process-crash recovery, not power-loss durability or concurrency safety. Pre-images copy
the two destination files whole. The frozen counter measures its named arms; a mutant anchored to
bytes the integration changed reads NO-MATCH, never a kill (the C2 battery's d/e re-anchor is
committed). The fleet-root stray `after` (mtime 2026-11-03 20:05, before this round) is not this
lane's and was left untouched; `.scratch/` is orchestrator-owned and untouched. `plan-before-ready` readiness evidence was produced at the freeze and committed with
the work (A2.2), not inside the frozen tree. Wave attack share differs by the tool's fixed role set
(5/13) and the declared roles (6/13), both reported.

## SHONEN

- `[~]` SKILL.md real decision tables/error patterns/checklists/sources — gate registry rows and
  the 37-item executable checklist landed at M; `close/checklists.txt` 37/37; pointer
  `SKILL.md:610,617,631,742-743`.
- `[~]` one end-to-end domain task logged — C1 and C2 ran end-to-end on the lane at M
  (`close/c1-probe.txt`, `close/c2-probe.txt`) and the LOG entry records it; pointer
  `LOG.md` round 77.
- `[~]` instructions executable without oral context — the frozen plan + counter + checklist items
  are re-runnable; `PLAN_BEFORE_READY: pass=1` at M.
- `[~]` no cross-domain bleed — `PROVINCE.md` byte-unchanged; sibling material read-only
  (`build/K77ConnectorOverlap/report.md`); pointer
  `.ufo/waves/round-77/build/K77ConnectorOverlap/report.md`.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Tool installs: none.
