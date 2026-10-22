# kotoba — round 49 report

Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`,
pushed lane head `9f2f1a751292a9a267ce8a83870efab76429e9e6` (jj-lane.sh `landed`; late corrections after the first report filing at lane `bfd5a58`). Attempt 1. Plan
`plans/round-49.md`. Drift guard honoured: no freshness claim, SKILL.md frontmatter unchanged.

## Work performed

Declared claims (2): **C1 adjacency** (lowest axis, 8.0; tied with freshness 8) — fleet sibling-overlap
census; **C2 operability** (8.5) — dispatch-prompt checklist boxes executed (capability). Both were
re-sized before any landing after the build-wave critics showed the first counters were content-blind
(`plans/round-49.md` re-sizing notes; `.ufo/waves/round-49/build/CriticC1Sizing.md`, `CriticC2Sizing.md`).

- C1: `corpus/knowledge/sibling-overlap-census-round49.md` — 20 sibling lanes, one build seat per lane,
  pinned sibling commits, located scope quotes, two mechanical columns; `PROVINCE.md` § Adjacent rewritten
  as a 20-row table joined to it by `verifiers/check_sibling_census.py` (landed `f054b8e`, corrected `bfd5a58`).
- C1 sources: S022 (Claude Code skills docs) and S023 (Agent Skills overview) written, S018 re-opened;
  finding: no documented tie-break between overlapping descriptions (entry § What decides).
- C2: `verifiers/verify_dispatch_prompts.py` with fixtures `verifiers/fixtures/dispatch-prompts/`,
  `--box-proof`, floored (floors guard 9 → 10 instruments); `dispatch.08` box authority re-worded from the
  frozen `.ufo/state/<id>.round` to `<id>.report-baseline` (landed `c48793d`; evidence
  `.ufo/waves/round-49/build/DispatchInstrument.md`, `PlanDataWalk.md`, blind second instrument
  `DispatchIndependent.md`).
- Routed round-48 defects: R1 fixed (`verifiers/verify_harness_independent.py` keys every root by
  frontmatter name, must-fail arm, self-test 116 → 123, `f054b8e`, `build/R1FrontmatterKey.md`; falsify `ReviewR1Patch.md` rates it HOLDS-BOUNDED: the identity arm holds, but the no-name directory fallback diverges from opencode, which skips such a skill, and the frontmatter reader misses YAML edge cases such as BOM, trailing comments and quoted keys — not fixed this round, carried); R2 →
  lesson M29 + criterion Q25; R3 correction appended `SCORECARD.md` under `Next: round 49`; R4 partly
  addressed (count-provenance section + falsify corrections in the round-48 entry; 21/23 reproduce, row 122
  and coverage sentence wrong, `falsify/ReviewR4Provenance.md`); R5 carried with a specified v2 oracle
  (`build/R5Disposition.md`).
- Frontier step: mined M29 (content-blind counter) and M30 (adjacency line written without opening the
  sibling's bytes) in `corpus/lessons/round-49.md`, each shown able to fail.
- Falsify wave corrections (`bfd5a58`): kake and kasegi reclassified `adjacent` under the stated rule
  (`falsify/CriticC1Landed.md`, `RowKake.md`, `RowKasegi.md`); guard now re-derives mechanical cells
  (self-test 39 → 44); boundary notes re-cited (`RowKengaku.md`, `RowTameshi.md`, `RowMado.md`);
  S022 teaches corrected (`ReopenS022.md`); box-proof bound stated in SKILL.md and the capability row.
- L0: two lines filed (fleet `ff3aff2`): opencode config group owner; retire round-1 `*-L1.md` prompts.

## Landed changes

| commit | carries | LOG entry |
|---|---|---|
| `f054b8e88f4c455d19a57d17e0369468ee4013dc` | C1 entry, PROVINCE table, guard, S022/S023, R1, R3, R4 section, lesson, Q25, README rows, build evidence | LOG.md § 2026-10-22 Round 49 landing |
| `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad` | C2 instrument, fixtures, map, box re-word, floors, corpus baseline re-record, SCORECARD rows and capability row | same |
| `bfd5a583a9ba5e7ab702cca301ec2c44c8bf5287` | falsify-wave corrections and evidence | LOG.md § Round 49 landing pin and falsify wave |

## Before → after measurements

- **C1** — `awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' PROVINCE.md | grep -cE '^\| (audio|chousa|game-dev-2d|game-dev-3d|kagi|kaidoku|kake|kama|kasegi|kengaku|kotodama|kumitate|lore|mado|mori|revenger|souji|tabi|tameshi|tsukuroi) \| (contested|adjacent|none) \| [0-9a-f]{40} \|'`
  → **0** at `a5adc146` → **20** at `f054b8e` and `bfd5a58`. Content guard
  `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md`
  → exit 0, `rows 20 verified 20`, `province rows 20 matched 20` at `bfd5a58`; exit 1 on the base
  PROVINCE.md and on mutants (lesson M29). Classification 9 adjacent / 11 none / 0 contested (7/13 at the
  first landing). Verdict as declared: reached. Bounds: an `adjacent` call resting on a kotoba-side or
  corpus statement is not machine-checked; four guard mutants survive (`falsify/MutCensusGuard.md`);
  two possible contested elements recorded, not ruled (kengaku census script, tameshi/kagi checklist runner).
- **C2** — `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json`
  → no instrument at `a5adc146` (0) → **`boxes proven 2`**, exit 0 at `c48793d` and `bfd5a58`. Supporting:
  map 8/0/33 → 8/2/31. Verdict: reached, holds-bounded — the proof covers the instrument's six named
  conjuncts, not the box text: no fixture for a variable prefix, non-digit round folder, `≤` boundary or
  legacy-state arm; map-delegation and pin checks survive mutation; no gate runs `--box-proof`
  (`falsify/ReplayC2BoxProof.md` rates the stronger "every conjunct" reading FAILS; `CriticC2Landed.md`,
  `MutDispatchInstrument.md` HOLDS-BOUNDED). Live run 11:15Z: dispatch.04 FAIL on six `*-L1.md` prompts
  with a `<lane>` report path; dispatch.08 PASS 250, N/A 29 (`build/c2-live-run-1115Z.txt`).

## Sources & frontier

- Rows 21 → 23 (`grep -c '^| S0' corpus/SOURCES.md`); tier A docs: S022, S023 (opened 2026-10-22 by
  seats, access records in `corpus/lessons/round-49.md` § Gate). Touched: S018 `used-by` old→new (adds the
  census entry), re-opened byte-identical; S022 `teaches` corrected after `ReopenS022`.
- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`: start exit 0
  (`kotoba ok`, W04 S018/S019/S021); end exit 0, same three W04.
- Frontier advanced: sibling arbitration census moved to PROVINCE Core; executed checklist coverage
  33 → 31 unexecuted boxes. Mined mistakes M29, M30; criterion Q25. Sourced claim: C1 cites S022/S023/S018.

## Trend verdicts

- **expansion: improved** — new admitted entry on frontier ground (sibling arbitration), 20/20 lanes
  classified at pins; one new capability row.
- **quality: improved** — R1 depth fix with must-fail arm; unsourced kasegi clause withdrawn; corpus
  integrity 4 DRIFT → 1 DRIFT (`falsify/NoHarmGates.md`: no check green at base and red at head).
- **discernment: improved** — both counters re-sized before landing after critics; falsify wave found and
  the round corrected a misapplied rule (7/13 → 9/11) and overclaimed proof wording; residual gaps stated.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SKILL.md` 41 boxes, 8 executed + 2 delegated; `verify_skill_checklist.py` exit 0 at `bfd5a58`.
- [~] End-to-end domain task executed and logged — LOG.md § Round 49 landing (dispatch-prompt instrument run over the fleet prompts, 11:15Z).
- [~] Instructions executable without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md` (no fresh non-author cold run this round).
- [~] No cross-domain bleed — `PROVINCE.md` § Adjacent rebuilt from the census at pinned sibling commits; contested items routed, not absorbed.

## Round shape and seats

- Shape: default two v1 waves, each validated under `scripts/hyaku/ufo-wave-policy.json` and sent as one
  `task` call carrying the validator's `taskCall`; seat gate granted both (build 36, falsify 38).
- Wave 1 build: **36 seats** — scout 23, scribe 4, executor 4, reviewer 2, critic 2, connector 1; 36
  returned, 0 dead. §3 floor met in wave 1; the L1 held the planner seat, data-walk on scout `PlanDataWalk`.
- Wave 2 falsify: **38 seats** — reviewer 29, mutation-tester 3, critic 2, scout 2, connector 1, plus
  `CriticBoxReword` (critic) = 3 critics; the labrat probe was re-roled reviewer (validator rejects labrat).
  0 dead. **12 seats were still running when this report was filed** (rows chousa, game-dev-2d, kama, lore,
  mori, souji; `MutR1Keying`, `CrossCheckC2Live`, `ReviewEntryRules`, `ReviewLessonQ25`,
  `CalibrationRecords`; `ReviewR1Patch` returned after the lane commit and is summarised above); their reports will land in
  `.ufo/waves/round-49/falsify/` uncommitted and are not judged here. The falsify gate reservation is
  therefore not yet released.
- **Round total 74 seats**, 0 dead, no residual call. Attack roles 4 + 34 = 38 of 74 (51%).

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs/updates: none by the L1 or any seat that reported.
- L0: two lines appended (`ff3aff2`). kaidoku/revenger overlap points to existing line 42, not re-filed.
- Observed, not caused: omp 18.12.6 keeps `check_substrate_pins.py`, `verify_surfaces.py`,
  `verify_harness_claims.py` red at base and head; `report_dead=2` from the closure-owned round-48
  spot-check's repo-relative pointers (indexed this round, not masked).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file from this
  round's seats (a staged `write` file holds another agent's id; untouched).
- Driver completion is not admission; the non-author closure judges both claims.

## Addendum (late falsify seats, after the first report filing)

- `RowSouji` HOLDS; `RowLore` and `RowGameDev2d` HOLDS-BOUNDED (rule wording: the arbitration cell leaves out
  the row's own lane name; game-dev-2d's "generic harness/evidence audits → their owning lanes" not ruled on).
- `RowKama` FAILS on the kama row's basis: the PROVINCE note misquoted kama's split (corrected verbatim at
  lane `b38bc0d`), and kama's `consumer-registry.md` audits agent prompt text and a sibling SKILL.md, a
  possible `contested` element under a literal reading; the rule has no precedence between arms. Recorded
  for the integrator; row stays `adjacent`. C1's declared after-value (20 rows) and guard output are unchanged.
- Lane commits this round: `f054b8e`, `c48793d`, `bfd5a58`, `b38bc0d` (all pushed). Still running at this
  filing: `RowChousa`, `RowMori`, `MutR1Keying`, `CrossCheckC2Live`, `ReviewEntryRules`, `ReviewLessonQ25`,
  `CalibrationRecords`; not judged here.
- Second late batch (lane `2272019`): `ReviewLessonQ25` FAILS two lesson statements — M30 wrongly said the
  round-46 scout file lacked the kasegi clause (it carries it and mis-cites kasegi), and the C2 proof does not
  enforce its own fixture coverage; both corrected in `corpus/lessons/round-49.md` (append-only). It also found
  the census guard accepts duplicated rows (carried). `RowMori` and `CrossCheckC2Live` HOLDS-BOUNDED
  (literal dispatch.04 count is 7, not 6, because `aggregator-L1.md` is exempted). Lane commits this round:
  `f054b8e`, `c48793d`, `bfd5a58`, `b38bc0d`, `2272019`. Still running: `RowChousa`, `MutR1Keying`,
  `ReviewEntryRules`, `CalibrationRecords`.
- Third late batch (lane `9f2f1a7`): `CalibrationRecords` FAILS with 6 self-assessment mismatches judged at
  `c48793d`. Fixed in `9f2f1a7`: README checklist count (33 → 31 of 41, dispatch boxes delegated), SCORECARD
  blind-instrument sentence (7 dispatch.04 and 168 frozen-authority dispatch.08 failures now stated), kumitate
  citation. Already fixed in `bfd5a58`: PROVINCE Frontier count and arbitration wording, the pending LOG
  falsify entry. That seat overwrote `DispatchIndependent`'s scratch `indep.json` (disclosed by the seat).
  `RowChousa` HOLDS-BOUNDED on the row; its chousa boundary note ("claim admission stays here" is a fleet
  rule, "kotoba cites it" uncited) is not corrected this round. Still running: `MutR1Keying`,
  `ReviewEntryRules`.
