# kumitate — round 36 (hyaku block 35–44, attempt 1), 2026-10-21

Lane: `kumitate-shokunin`. Base master `0614092e0804aaca06642cb3a263a05c1cacc98e`. Landed work:
`3d5760a8a4746a2fd18eb0f7bad1ec716d421987` (branch tip after the helper's `landed` line). Source pin:
private read-only clone `/fast/scratch/kumitate-r36/src` @ `31c465f15669f744848bd9f5d56191c5085670f7`
(`src-rev=31c465f15669`), detached, `chmod a-w`; the operator checkout was never a measurement source.
Wave evidence: `.ufo/waves/round-36/` (baseline, frozen populations, claims, build reports, final,
falsify spec + plan). Stale-lane: respawn-per-round driver; no other mission of this lane is open
(single launch line `launch kumitate round=36 … 00:47:22`, no earlier lane-dead line). Tool installs:
none. L0 questions appended: none.

## Work performed

Two declared claims, frozen before implementation (`.ufo/waves/round-36/claims.md`):
**C1 operability** (lowest live axis, 8) and **C2 coverage:runtime-layer** (9 → 10).

- **C1 — operability, one axis, one claim.** (a) `scripts/surface-probe.mjs` concatenates the
  manifest's declared `digestInputs` order instead of a re-sorted one — `RevManifestDigest` and
  `ScoutSurfaceDigest` independently re-derived `sha256:b36559d0…` (declared) vs `sha256:f17d1547…`
  (sorted, the false mismatch). (b) `readDispatcherStatus`/`readSightingSurface` spawn origin verbs
  with `UFO_STATE_DIR`/`UFO_PENDING_WORK_PATH`/`NODE_COMPILE_CACHE` under `mkdtemp` and remove them —
  `ExecSurfaceDispatcherState` (read-only pin reachable, writable-copy fingerprint unchanged). (c)
  `--known .ufo/pins/surface-known.json` pins the one upstream finding
  (`{sighting, VERB_UNDECLARED, VERB_DISPATCH, surface}`; upstream re-proved by `ScoutUpstreamVerb`,
  `ufo-sighting.mjs:4484-4492` dispatches it, `surface.mjs:74` omits it) with strict staleness. (d)
  PIN v1 in `claims-check`, `proxy-check`, `surface-probe` (`--pin`, full 40-hex
  `git rev-parse --verify HEAD` assertion with a scrubbed git env, `SRC_REV_MISMATCH` /
  `SRC_REV_UNVERIFIABLE` exit 2, `src-rev=` inside the verdict). (e) `claims-check --fidelity`
  (FIDELITY v1: member-section universe from the registry parse, clause-guarded adjacent-symbol pairing,
  `nonok = elsewhere + absent`, revision-bound per-note ratchet) plus re-anchoring.
  (f) `SKILL.md` checklist 13 → 14 items (item 14 = the fidelity sweep).
- **C2 — coverage:runtime-layer.** R5's 4 members (`native_admission_rules.rs`,
  `native_admission_text.rs`, `native_seats.rs`, `native_text.rs`) and R7's 5 (`bounded_fs.rs`,
  `bounded_fs_tests.rs`, `fs_durability.rs`, `local_ship.rs`, `local_ship_tests.rs`) gained one
  internals-level `## ` section each at the pin (`ScoutR5Members`, `ScoutR7Members`,
  `ExecR5Sections`, `ExecR7Sections`), with `CriticR5R7Claim`'s four text defects corrected before
  landing. 80/80 new anchors sit on their symbol's line.
- **Routed-defect dispositions** (`corpus/lessons/round-35-verifier-spotcheck.md`): (1) anchor
  fidelity is now a gate term with a ratchet; `dead`/`noid` stay diagnostics and a dead/noid ceiling
  is pre-registered for round 37 (partial, stated). (2) the two unbacked comparisons are reproduced
  and committed in `build/ScoutCiteProvenance.md` (S regressed 223 → 182, net over a changed note
  population; S8 note 91 → 30, rose=0) with the pin named. (3) the 624 S1–S7 figure is superseded by
  the delivered arm's own measure (`nonok=543` at 0614092 → 0); three notes without member sections
  are named as not measurable by this arm. (4) `final/cite.txt` provenance is recorded and the round's
  own evidence names the pin; `cite-check` itself stays unpinned — a why-not, pre-registered.
- **Prompt/inherited state.** Prompt `.ufo/prompts/kumitate-round-36.md` carried the five child-lane
  items (report path, commit-before-report, `SHONEN` heading, commit-hash rule, write scope) and the
  campaign addendum. No earlier attempt existed (no lane-dead line for round 36); the only inherited
  non-author file, `corpus/lessons/round-35-verifier-spotcheck.md` (commit `0614092`), was read and
  answered above, never edited.
- **Waves.** Build wave: 96 seats in ONE `task` call (scout 23, connector 8, executor 17, scribe 10,
  critic 8, reviewer 16, mutation-tester 4, revenger 4, sentinel 3, simplifier 3), validated under
  policy v2 (`plan`/`run`) and recorded at `.ufo/waves/round-36/build/swarm-registry.json`; reports in
  `.ufo/waves/round-36/build/`. Falsify wave: 81 seats validated (`.ufo/waves/round-36/falsify-spec.json`,
  plan 81) but NOT dispatched — the run hit its request budget before the falsify slot was acquired, so
  the wave-2 attack was not run; this is the round's largest verification gap and is reported, not
  hidden. No seat was replaced; dead seats: none observed (all dispatch items produced a report).
  L1 planner seat mapping: the validator rejects `planner` as a frozen role; the L1 held the canonical
  planner seat and the bounded data-walk rode `ScoutFidelityUniverse`, `ScoutProxyC2`, `ScoutProxyAxes`.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` → 15 entries, all
  `.ufo/watchdog.log` (driver) and `.ufo/state/*` driver files; no round-36 seat file landed at the
  fleet root.
- **Cross-domain / upstream (reported, never absorbed):** U1 the sighting manifest omits the `surface`
  verb it dispatches (`ufo-sighting.mjs:4484-4492` vs `ufo-sighting-lib/surface.mjs:74`), filed in
  `.ufo/reports/round-35/kumitate.md` §Routed; U2 `fleet-dispatcher status` mkdirs `<src>/.ufo` unless
  redirected (upstream-owned; the lane now redirects); U3 the moving operator checkout remains the
  legacy default for `cite-check`/`round-gate --origin` (host/operator scope).

## Landed changes

All in `3d5760a8`, tied to the `LOG.md` entry `- 2026-10-21 — round 36`:

- `scripts/surface-probe.mjs` — declared-order digest concat, mkdtemp origin verbs, `--known`, `--pin`,
  scrubbed git env; `--selftest` 61/61.
- `scripts/proxy-check.mjs` — PIN v1, prefix-7 mutation case, scrubbed git env; `--selftest` 117/117.
- `scripts/claims-check.mjs` — PIN v1 and FIDELITY v1 (`--fidelity`, `--fidelity-ratchet`), clause-guarded
  pairing, scrubbed git env; `--selftest` green.
- `.ufo/pins/{origin,surface-known,fidelity-ratchet}.json` — the pin, the one upstream expectation, the
  all-zero ratchet over the 15 debt notes.
- `SKILL.md` — 14-item checklist, gate-registry rows with the new flags, PIN + FIDELITY working rules,
  named-gap retirement scoped to the three pinned gates.
- `corpus/knowledge/native-admission-detail.md`, `corpus/knowledge/local-ship.md` — nine R5/R7 sections
  and the C2 text corrections.
- `corpus/knowledge/*.md` anchor repairs (ops-watchers, remaining-scripts-census, sighting-wall,
  native-trial-launch, route-probe-cluster, live-surface-probe and the small notes).
- `corpus/knowledge/pinned-evidence.md` (new; S031/S032), `corpus/lessons/round-36.md`,
  `corpus/SOURCES.md` S029–S032, `corpus/README.md` map rows, `SCORECARD.md` (stanza, Axes, Move log,
  limits/planned), `LOG.md`.
- `.ufo/waves/round-36/` — baseline, frozen populations, claims, dispatch/spec/registry, final evidence.

## Before → after measurements

Counting commands were run from the lane root; the pinned commands resolve the origin through
`.ufo/pins/origin.json` (src-rev printed in each verdict). "Before" was measured on the pristine
`0614092` tree with the delivered tools; "after" on the delivered tree at `3d5760a8`.

| Claim | Before | After | Commands |
|---|---|---|---|
| C1 (fidelity) | `FIDELITY_TOTAL anchors=1494 ok=317 elsewhere=461 absent=82 dead=168 noid=466 nonok=543` → `FIDELITY: DRIFT (nonok=543)` exit 1 | `FIDELITY: CLEAN (notes=20 anchors=1574 src-rev=31c465f15669)` exit 0 | `node scripts/claims-check.mjs --fidelity --fidelity-ratchet .ufo/pins/fidelity-ratchet.json` (after); pristine export + delivered arm (before) |
| C1 (checklist) | `CHECKLIST: 11/13 pass` (620, 625 red) | `CHECKLIST: 14/14 pass` | `node scripts/surface-probe.mjs --checklists` |
| C1 (surface) | `SURFACE_PROBE: DRIFT (surfaces=2 checks=12 errors=3 warnings=1)` at the pin | `SURFACE_PROBE: CLEAN (surfaces=2 checks=12 errors=0 warnings=1 known=1 src-rev=31c465f15669)` | `node scripts/surface-probe.mjs --known .ufo/pins/surface-known.json` |
| C1 (proxy) | `PROXY: DRIFT (C2_TOTAL_DRIFT declared=79 computed=80; AXES_DRIFT coverage 10 vs 9; PIN_UNPINNED sources-check)` | `PROXY: MATCH (A=7 C=14 operability=8; C1=19/19 C2=82/82 coverage=10; S=88/88 coverage:script-layer=10; R=92/92 coverage:runtime-layer=10; K=51/51 coverage:kimi-layer=10; pins=6 match; src-rev=31c465f15669)` | `node scripts/proxy-check.mjs` |
| C2 | `CLAIMS: MATCH (… sections=175 adv=6)`, R5/R7 `form=topic sections=0`, R 83/92 | `CLAIMS: MATCH (rows=2 yes=2 notes=2 sections=9 adv=0 src-rev=31c465f15669)`; R 92/92 ⇒ 10 | `node scripts/claims-check.mjs --src /fast/scratch/kumitate-r36/src --row R5 --row R7 --strict`; `node scripts/proxy-check.mjs` |

No axis harmed: operability 8 held (`f_O` 20/23 → 21/24), coverage 10, coverage:script-layer 10,
coverage:kimi-layer 10, coverage:runtime-layer 9 → 10. Command transcripts:
`.ufo/waves/round-36/{baseline,final}/`.

## Sources & frontier

`corpus/SOURCES.md` rows 28 → 32 (S029 own-work pinned census; S030 pytest strict xfail; S031
git-rev-parse; S032 Reproducible Builds "Recording the build environment"), all `mined`, tiers A:31 /
B:1, opened 2026-10-21 with URL, anchor and ≤25-word quote recorded in `corpus/lessons/round-36.md`
§Gate. Counting command (both runs exit 0): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --root /home/vgpnk/Projects/shokunin kumitate` → `kumitate ok … SOURCES.md`; lane gate
`SOURCES_CHECK: CLEAN (rows=32 …)`. Rows touched: none changed status/used-by outside the four new rows;
no rejection added this round (S019/S020 stay rejected with their flip conditions). Frontier rows
advanced: `pinned-evidence.md` moves the frontier's provenance ground into core; claim→S### mapping:
C1 rests on S031 + S032 (pin/verdict revision) and S023 (mutation-outcome definitions), C2 rests on
S029 (pinned census). Census before→after: 28 → 32 rows, exit 0 → exit 0.

## Trend verdicts

- **expansion: improved.** Two new knowledge structures on ground the coverage map did not hold —
  `knowledge/pinned-evidence.md` (new) and the fidelity gate recorded across SKILL/SCORECARD/lesson —
  and four new mined source rows; the runtime coverage map now holds R5 and R7 at member level.
- **quality: improved.** Before/after gate lines above: the false digest mismatch gone, the read-only
  tree no longer mutated by the probe, anchor debt `nonok` 543 → 0 under a revision-bound ratchet, the
  C2 notes' four false claims corrected, and 168 dead anchors stay printed rather than hidden.
- **discernment: unprovable-but-better.** Inside the round, two independent critic seats falsified the
  pairing rule (19/40 wrong pairings; a widened-range counterexample reaching nonok=0) and the lane
  changed the rule before landing; whether that agrees with the non-author closure spot-check is not
  self-assessable, so the lane does not claim `improved`.

## SHONEN

- [~] `SHONEN.md:5` craft — `SKILL.md` decision table / failure patterns / anti-patterns / gate registry / 14-item checklist; `corpus/SOURCES.md` 32 rows; `surface-probe --checklists` 14/14 at `src-rev=31c465f15669`. Outside check: a cold-run reviewer re-executes the 14 items.
- [~] `SHONEN.md:6` end-to-end — `LOG.md` round-36 entry + `SCORECARD.md` Move-log rows + this report citing `3d5760a8`; `round-gate --round 36` run after the report lands. Missing: the non-author closure's independent re-run.
- [~] `SHONEN.md:7` no oral context — checklist preamble + literal commands, PIN/FIDELITY working rules, and the pin's recreate one-liner are self-contained; `cite-check`'s explicit `--src` remains the one command a reader must supply (named limit). Missing: a fresh-session cold run.
- [~] `SHONEN.md:8` province — every changed path is under the lane repo; upstream defects reported, never patched; `PROVINCE.md` untouched and still accurate (`.ufo/pins/` sits in the lane's own instrument band).
