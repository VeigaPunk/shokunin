# kumitate — round 83

Lane `kumitate` (axes: operability + coverage — orchestration and tooling), round 83, attempt 1, Linux
run-15 host. Scratch root `/fast/scratch/hyaku/kumitate-r83` (deleted after the round; receipts live under
the lane). Lane tip `d5fc2c9407a75e939b332560f54548f2dd52629e` (the close set; `git ls-remote origin
refs/heads/master` prints the same hash). Measured work revision `1c1a855a0bae88d55ef141c96bef52e0fa980c23`;
freeze `eda17453517da3d9f38c708d70b00dc72cf85a33`; scaffolding `eca7debd9aa6184a81f7e4abb43d507299a31f31`;
base `eb8e00956e7a282cb2b53a5bc53e1afa1d0e7fcf` (the round-82 verifier spot-check, the remote tip at open).

Round shape: **ONE v1 wave of 15 seats** under `ufo-wave-policy.json` (band 8–16) plus the L1's canonical
planner seat; attack 4/15 = 27 % (reviewer ×2, critic, mutation-tester; sentinel and revenger are a fifth
and sixth adversarial seat), connector 1, executor 3, scribe 3, scout 2. The wave was dispatched from
`.ufo/waves/round-83/w1.ready` (taken at 09:03:31) and settled with `w1-results.json` (15 rows). **Five
seats settled without a report file:** `K83ExecHandoffV3` died on a provider limit (last error: *"429 Usage
limit reached for 5 hour … (type=1308). No answer was produced"*; it had confirmed the counter defect and
never landed its edits — the L1 took the file over), and `K83ExecEvidence`, `K83ReviewC1`, `K83ReviewC2`,
`K83CriticClaims` returned partial final texts (stored in `w1-results.json`) without writing their report
files; their findings are cited from that file below. No seat was replaced.

## Work performed

The round declared **two claims on two axes**, both measured against counters frozen before any data seat
scored:

- **C1 — operability** (the lowest non-retired axis; the integer is terminal at 9): **`ready-handoff` v3** —
  the inline-handoff gate now judges the admission the campaign dispatcher actually performs.
- **C2 — coverage:omp** (integer held at 10): **the compare path judges a receipt's self-asserted
  instant** — one clock predicate shared with `--shape`; a future instant is refused with or without
  `--max-age`.

Work items, each with its evidence pointer:

- **Freeze** `eda17453` — plan (claims, predicates, kill rules K1–K4, controls, wave shape), both frozen
  counters (`probe83-c1.mjs`, 27 declared arms; `probe83-c2.mjs`, 16 arms), the four pre-data control
  receipts and the open receipts (`.ufo/waves/round-83/{plan.md,probe/,controls/,open/}`).
- **Scaffolding** `eca7debd` — the v3 tool and the census clock, both suites (54 → 68 and 105 → 108 at that
  commit), S240–S242 with the RFC 3339 capture, the wave spec/dispatch/registry/`ready`.
- **Wave** `.ufo/waves/round-83/` — 10 seat reports under `w1/`, the results handoff `w1-results.json`, the
  dispatch marker `w1.ready.dispatched`, the campaign registry `w1/swarm-registry.json`.
- **In-round repairs the seats drove** (all in `1c1a855a`):
  - the `--agents` `{members}` branch now requires the validator's `ufo-swarm-registry-v1` schema stamp
    (scribe finding `knowledge/dispatcher-admission-surface.md` §Limits; suite case
    `agents-members-foreign-schema`);
  - `REPORT_DEST_OUTSIDE` now contains the realpath of the destination's deepest existing ancestor, so a
    planted symlink directory inside the lane cannot carry a report out of it (sentinel F-1; suite case
    `report-dest-planted-symlink`);
  - the two corpus entries the clock change falsified were amended append-only
    (`receipt-age-on-the-compare-path.md`, `self-describing-shape-receipt.md`);
  - the `ready-handoff` capability row was refreshed to v3 (R82-V3), the stale tally in
    `handoff-binding-and-liveness.md` refreshed (R82-V1), and the round-82 spot-check adopted in-round
    (map row + readme-map/source-capture pins — the 12th recurrence);
  - `considerthese/2026-10-26.md` idea 2 mined into `QUALITY.md` **Q76**, with a shown-able-to-fail receipt
    (`close/gate-registry-check.txt`: the round lesson's Gate is green, a synthetic `S999` prints
    `gate-absent:S999`).
- **Counter defect disclosed, not edited** — `probe83-c1.mjs` declares `ARMS = 27` while carrying 28
  `arm()` call sites, and its `band-total-resumes` fixture (6 spawns, attack 2) trips `ATTACK_SHARE`
  (2/12 = 16.7 %) before the band is judged, so the frozen `HELD held=27/27` verdict is reached with that
  arm red. Found independently by `w1/K83ScoutAdmission.md` §6.1–6.2, `K83ReviewC1` and
  `K83CriticClaims` (`.ufo/waves/round-83/w1-results.json`). A disclosed repair probe
  (`probe83-c1-repair.mjs`, corrected fixture, `ARMS = 28`) re-measures the same behaviour:
  `C83_C1R: HELD held=28/28` at M and `UNMET held=15/28` at the base tree
  (`close/c1-repair.txt`, `close/c1-repair-base.txt`). The claim's rule stays the frozen bytes; the
  defect is mined in `corpus/lessons/round-83.md` §Mistakes and pre-registered for round 84.

## Landed changes

Every change is tied to the round-83 `LOG.md` entry (one section plus the gate-required one-line record).

| change | commit |
|---|---|
| plan, both frozen counters, four controls, open receipts | `eda17453` |
| `ready-handoff` v3, `omp-census` clock, suites, S240–S242 + capture, wave payload and `ready` | `eca7debd` |
| work: the two seat-driven repairs and their suite cases, the two knowledge entries, the lesson, SCORECARD/LOG/SKILL, QUALITY Q76, the map row and three pins, wave results | `1c1a855a` |
| close receipts stamped `rev=1c1a855a` (probes, suites, checklists, every gate, harm matrix) | `d5fc2c94` |

## Before → after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| C1 | `node .ufo/waves/round-83/probe/probe83-c1.mjs --set c1 --lane .` | `C83_C1: UNMET held=15/27` (`controls/c1-base.txt`, v2); constant-`READY` stub `3/27` (`controls/c1-stub.txt`) | `C83_C1: HELD held=27/27` exit 0 (`close/c1-probe.txt`) — with the disclosed red arm | M `1c1a855a`; base `eb8e0095` |
| C1 (repair) | `node .ufo/waves/round-83/probe/probe83-c1-repair.mjs --set c1 --lane .` | `C83_C1R: UNMET held=15/28` (`close/c1-repair-base.txt`) | `C83_C1R: HELD held=28/28` exit 0 (`close/c1-repair.txt`) | M `1c1a855a` |
| C2 | `node .ufo/waves/round-83/probe/probe83-c2.mjs --set c2 --lane .` | `C83_C2: UNMET held=13/16` (`controls/c2-base.txt`); stub `3/16` (`controls/c2-stub.txt`) | `C83_C2: HELD held=16/16` exit 0 (`close/c2-probe.txt`) | M `1c1a855a` |

The round's own handoff, judged at M: `READY_HANDOFF: READY wave=w1 seats=15 resumes=0 total=15
attack=4/15 connector=1 roles=scout=2,executor=3,scribe=3,connector=1,reviewer=2,critic=1,mutation-tester=1,
sentinel=1,revenger=1 policy=ufo-wave-policy.json agents=none` exit 0 (`close/handoff-admission.txt`).

Same-commit re-measure of the stanza at M (`close/proxy-check.txt`): `PROXY: MATCH (A=896 C=43
operability=9; C1=19/19 C2=210/210 coverage=10; S=88/88 coverage:script-layer=10; R=92/92
coverage:runtime-layer=10; K=55/55 coverage:kimi-layer=10; O=1/1 O_members=65 O_findings=0 O_bound=35
coverage:omp=10; pins=6 match; source=snapshot)`; `A` 891 → 896 (two counters, the repair probe, the
close-battery script, the spec generator), `C` 42 → 43 (the compare-clock checklist item),
`C2/C2_total` 206 → 210; `pin.ready-handoff` `7e9827ad…` → `d6e6ba8a…`, `pin.omp-census` `92180f3c…` →
`f6ace3e2…`.

Other close readings at M: `READY_HANDOFF_SELFTEST: 70/70 pass`; `VERDICT: PASS (108 cases)`;
`CHECKLIST: 43/43 pass`; `CLAIMS: MATCH (rows=19 yes=19 …)`; `SOURCES_CHECK: CLEAN (rows=180, tiers
A:153)`; `TRUTH: CLEAN (anchors=811 true=778 debt=20)`; `SOURCE_CAPTURE: CLEAN captures=70 exemptions=110`;
`README_MAP: CLEAN files=210 rows=210 covered=210`; `SPOTCHECK_COVERAGE: CLEAN spotchecks=49 uncovered=0`;
`COUNTER_PINS: CLEAN pins=44`; `CITE_SOURCES: CLEAN cited=232`; `KIMI_CENSUS: CLEAN 55/55`;
`OMP_SHAPE_COMPARE: IN_SYNC … receipt_captured=2026-11-04 age_days=0`; sources census exit 0;
`HARM_MATRIX: CLEAN gates=36 held=31 repaired=2 carried=2 moved=1 new=0 gone=0 harm=0 harm_absent=0
new_red=0 unmeasured=1 ancestor=yes base=eb8e0095 tip=1c1a855a` (the unmeasured gate is
`harm-matrix-selftest`, which exceeds the matrix's 60 s per-gate budget, carried from base).

**The one red gate is disclosed, not repaired:** `plan-before-ready.sh --round 83` reads
`FAIL … reason=MAP_DRIFT map_first=uncovered:lessons/round-82-verifier-spotcheck.md`
(`close/plan-before-ready.txt`). The map arm judges the archive of the *plan's own commit*; the round-82
spot-check file landed at the base commit without a `corpus/README.md` row, and the row and pin were
adopted in this round's work commit — after the freeze and the marker. The class is mined in the lesson
and pre-registered for round 84 (repair as the round's first commit). `round-gate --round 83` was red at
the close battery only because the report did not yet exist; it is green after filing (see below).

## Sources & frontier

`SOURCES.md` rows **177 → 180** (`grep -cE '^\| ?S[0-9]{3,}' corpus/SOURCES.md`), tier A 150 → 153,
status `mined` 145; three rows opened and admitted this round, none rejected:

| row | kind | tier | what it grounds | anchor / quote |
|---|---|---|---|---|
| S240 | code (own-work) | A | the dispatcher's admission arithmetic — band over spawns + resumes, cap clamp, role set, counts | `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs` @ `fb7157fc`, lines 1085-1091: "a wave with spawn lanes needs at least ${laneFloor} lanes (got ${total})" |
| S241 | code (own-work) | A | the registry shape the dispatcher writes | `.../ufo-swarm-registry.mjs` @ `fb7157fc`, line 27: `export const SWARM_REGISTRY_SCHEMA = "ufo-swarm-registry-v1";` |
| S242 | spec | A | what a timestamp denotes | RFC 3339 §1 p.2: "Date and time expressions indicate an instant in time." (capture `.ufo/waves/round-83/build/L1/captures/rfc3339.html`, sha256 `c53b2d12…`, 44,033 bytes) |

Rows touched old→new: S240/S241 `queued → mined`, `used-by — → corpus/knowledge/dispatcher-admission-surface.md`;
S242 `queued → mined`, `used-by — → corpus/knowledge/self-asserted-instants.md` (logged in
`corpus/lessons/round-83.md` §Gate status changes). Two knowledge entries admitted
(`dispatcher-admission-surface.md`, `self-asserted-instants.md`) and their map rows land with the round;
the frontier band "dispatcher admission surface" gains its first entry, and the receipt-clock principle
becomes a named corpus invariant. **The sourced claim is C1**: its evidence rests on S240/S241, both
opened this round. Census
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`
→ `kumitate ok`, exit 0 at open and at close (six carried W04 warnings; no E03/E04).
**Assimilation: none** — the `merge/kumitate/` package's 155 staged rows begin at S195 and collide with
the lane's own S195–S239; renumbering is a dedicated round, so no package row or entry was appended.

## Trend verdicts

- **expansion — improved.** Two admitted `knowledge/` entries on ground the coverage map did not hold,
  each `source:` citing a row opened this round; SOURCES 177 → 180 (tier A +3); the coverage map
  206 → 210 rows (two entries + this lesson + the adopted spot-check row); the capability table gains no
  new name (this is a deepening, claimed as quality, per AXES.md).
- **quality — improved.** Both instruments gained behaviour the base tree and the frozen constant printers
  cannot reach (C1 15/27 → 27/27, stub 3/27; repair 15/28 → 28/28; C2 13/16 → 16/16, stub 3/16); suites
  54 → 70 and 105 → 108; two real defects were found by seats and repaired in-round (registry schema
  stamp; report-destination realpath containment) with regression cases; the counter-arithmetic defect was
  disclosed with a repair receipt rather than hidden; the two corpus entries the change falsified were
  amended append-only; `HARM_MATRIX: CLEAN harm=0`; the whole gate battery is green except the disclosed
  map arm.
- **discernment — improved.** The wave's scout and reviewer independently caught the counter defect before
  the closure; the sentinel found a containment gap last round's repair left; the revenger classified eight
  gate↔dispatcher differences (four gate defects — resume ownership/shape, duplicate expansions, the
  unclamped band floor — and four truthful divergences) and named them as limits, not absorbed; the
  connector ruled three sibling overlaps (mori's wave settlement is resume-blind, tabi's `c2-wave-caps`
  carries a latent false-positive class, the origin constants are operator-owned) as report-only; the
  critic caught a second tally drift (a probe header claiming `15/15` against `ARMS = 16`). Caveats: no
  non-author spot-check of this round exists yet (the closure writes it), and the counter defect is a
  discernment debt the lane made itself, disclosed rather than excused.

## SHONEN

One line per box of `SHONEN.md` (4 boxes):

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `SKILL.md` gate-registry rows `ready-handoff` (v3) and `omp-census` (round-83 clock note) plus checklist
  items 755/756/757; author-attested, no non-author verifier this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: the round-83 LOG entry
  (`ready-handoff` v3 and the census clock, with the frozen counters, suites and gates); author-attested.
- [~] Instructions executable by an agent without oral context — pointer: `.ufo/waves/round-83/plan.md`
  plus the frozen counters, from which 15 seats executed without further hand-holding; author-attested.
- [~] No cross-domain bleed (PROVINCE.md accurate) — pointer: `w1/K83Connector.md` (`OVERLAP: 3, absorb 0`)
  and the round's Limits naming operator-owned upstream ground; author-attested.

## Stale-lane

Respawn-per-round driver; `.ufo/watchdog.log` carries `launch kumitate round=83 pgid=3737310
driver=hyaku-inline attempt=1` at 08:55:37 and no earlier `lane-dead-no-report` line for round 83. No other
mission of this lane is open; this round is *progressing* (commits `eda17453`, `eca7debd`, `1c1a855a`,
`d5fc2c94` and files under the lane since launch), not silent.

## Tooling and housekeeping

- No installs or upgrades this round (node v24.21.0, jj 0.45.1-7c41cdeb; the origin validator was read at
  `fb7157fc`, never executed). pacman stayed paused.
- Misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain`: `.scratch/*` (orchestrator-owned,
  never a misroot) and `.ufo/reports/round-81/mado.md` (another lane) are not this round's; a stray
  fleet-root file `after` (24 bytes, dated 2026-11-03 20:05, content `== SCORECARD diff base-`) names no
  lane or round and predates this round — left untouched and recorded here.
