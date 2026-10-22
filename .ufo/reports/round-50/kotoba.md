# kotoba — round 50 report

Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`,
pushed lane head `2abd290eac782972df6a943fa8fcf8a18a41d4f2` (jj-lane.sh `landed`). Attempt 1. Plan
`plans/round-50.md`. This header is frozen; any later lane head goes in an appended addendum (routed defect D1).

## Work performed

Declared claims (2): **C1 adjacency** (lowest non-retired axis, 8.0, tied with freshness; the learning
claim) — kotoba's `SKILL.md` frontmatter `description` value names each census lane classed non-`none`,
each in a clause carrying a word from the guard's pinned marker list; **C2 operability** (8.5) — deleting
any one of the 6 must-fail cases from `verifiers/fixtures/dispatch-prompts/manifest.json` makes
`--box-proof` exit 1. Both counters were re-sized before any landing after the build critics showed the
first designs could print the target without the content (`plans/round-50.md` § Re-sizing;
`.ufo/waves/round-50/build/CriticC1Sizing.md`, `CriticC2Sizing.md`). No target value moved.

- C1: description rewritten (first 99 characters unchanged, 1,019 of 1,024 characters) to name chousa, kama,
  kotodama and tameshi alongside kagi, kake, kasegi, kengaku, kumitate; new `--skill` arm in
  `verifiers/check_sibling_census.py` (self-test 44 → 68, floored) — landed `542f515`, kengaku clause
  narrowed in `a78fec1` after `falsify/CriticC1Landed.md` and `ReviewDescAccuracy.md`.
- C1 knowledge: new entry `corpus/knowledge/skill-selection-rules-round50.md` (eight client pages; no client
  documents a rule between two differently named skills whose descriptions both match; hash recheck over
  eight pages) plus a `SKILL.md` § Anti-patterns error-pattern paragraph citing it (`a78fec1`, corrected
  `bf109ca`); census entry gained appended round-50 sections and corrections.
- C2: `verifiers/verify_dispatch_prompts.py` reads coverage from observed conjunct statuses with one pinned
  co-failure, requires a control and the N/A case, catches substrate errors (self-test 32 → 56); counter
  `verifiers/box_proof_case_deletion.py` (new); the checklist gate runs each delegated `--box-proof`
  (`verify_skill_checklist.py`, self-test 1845 → 1851) — landed `542f515`.
- Routed round-49 defects: D1 this report is append-only (rule and awk check in `corpus/lessons/round-50.md`);
  D2 docstring/help and SKILL.md bound fixed, gate wired; D3 precedence rule and rulings appended to the census
  entry, duplicate rows rejected, guard in `verifiers/floors-registry.json` (10 → 11 instruments), rule sent to
  the integrator (L0 line, fleet `8d56eb1`); D4 SCORECARD qualifiers; D5 16-row reject erratum and split
  admit/reject Gate; D6 R4, R5, R1 carried (`build/CarryD6.md`, `falsify/ReviewR6Carry.md`).
- Frontier: mined M31 (claim headline wider than its counter → criterion Q26) and M32 (misroot sweep run
  before the last seat returned); sources S024–S029 written, S019/S022 re-opened.

## Landed changes

| commit | carries | LOG entry |
|---|---|---|
| `542f515672306e1baefcb69ba79f1d4c18b6450e` | C1 description and guard, C2 instrument/driver/gate, floors, S024–S029, Q26, lesson, README, baseline | LOG.md § Round 50 landing |
| `956ee1676e4c18480bce8ac3993541462be76e11` | D3 precedence, PROVINCE rulings, SCORECARD rows, LOG | same |
| `a78fec1ff1434fbbc58f025d2662dd2cab7957ad` | new knowledge entry, SKILL.md error pattern, capability row, falsify corrections 1, round-49 misroot moved in | LOG.md § Round 50 landing pin and falsify wave |
| `bf109caccccca8459d297edf09a7dc7828396d8f`, `87eeae27d4c7a2e882d8912ddd86bcaf598f4ffd` | falsify corrections 2–3 | same |
| `1cb2e65e3908b066fcf215f7d16196a3c0d5ca77`, `2abd290eac782972df6a943fa8fcf8a18a41d4f2` | falsify evidence, LOG entry, citation fix | same |

## Before → after measurements

- **C1** — `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill <file>`
  (file = `git show <rev>:SKILL.md`, guard at `542f515` or later) → `skill description names 5 of 9 non-none lanes`,
  exit 1 at `f3046466` → `9 of 9`, exit 0 at `542f515` and `2abd290`. Replayed by `falsify/ReplayC1Counter.md`
  (also with an independent PyYAML clause split), `MutDescGuard.md` (17 of 19 mutants killed). Bound: the
  marker test is lexical (a false ownership sentence passes); no routing effect is measured on any harness.
- **C2** — `python3 -B verifiers/box_proof_case_deletion.py --rev <rev>` → `killed 0 of 6`, exit 1 at
  `f3046466` → `killed 6 of 6`, exit 0 at `542f515` and `956ee16`. Replayed without the driver by
  `falsify/ReplayC2Counter.md`. Bounds: duplicate-id or unlabelled twins launder the driver; its kill test is a
  stderr substring; 7 of 17 instrument mutants survive the driver (16 of 17 caught by the self-test,
  `MutBoxProofCode.md`).

## Sources & frontier

- Rows 23 → 29 (`grep -c '^| S0' corpus/SOURCES.md`); new tier-A docs S024 opencode, S025 VS Code, S026 Claude
  Code subagents, S027–S028 GitHub Copilot, S029 Gemini CLI (opened 2026-10-22 by build seats; access records in
  the lesson § Gate; all re-opened by falsify seats, bytes identical). Touched: S019, S022 re-opened
  byte-identical, `used-by`/`teaches` old→new logged in the lesson; S019/S022/S026/S028 cells narrowed after
  falsify. Three drafted rows rejected with reasons.
- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`: start exit 0
  (`kotoba ok`, W04 S018/S019/S021); end exit 0, same three W04.
- Frontier advanced: sibling arbitration — kotoba's own description now names its 9 adjacent lanes; new entry on
  how clients choose between skills. Sourced claim: C1 entry cites S024–S029.

## Trend verdicts

- **expansion: improved** — one new admitted knowledge entry (36 → 37), six new source rows, one capability row
  ("sibling-description check").
- **quality: improved** — base corpus-integrity red (unindexed round-49 spot-check) repaired; every cited count
  re-run by falsify seats; overstated sentences corrected by appended text; no gate green at base is red at head
  (`falsify/NoHarmGates.md`).
- **discernment: improved** — both counters re-sized before landing; the falsify wave's 38 seats found and the
  round corrected the kengaku clause, two census universals, the D3 basis labels and three ruling premises;
  `falsify/CalibrationRecords.md` counted 5 mismatches of 51 statements at `956ee16`, all fixed after.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — new § Anti-patterns error pattern citing `corpus/knowledge/skill-selection-rules-round50.md`; `verify_skill_checklist.py` exit 0, 11/11 at `2abd290`.
- [~] End-to-end domain task executed and logged — LOG.md § Round 50 landing (description guard and box-proof driver run at base and head).
- [~] Instructions executable without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md` (no fresh non-author cold run this round).
- [~] No cross-domain bleed — `PROVINCE.md` § Adjacent rows re-reasoned on sibling bytes; boundary rule sent to the integrator, not decided as settled.

## Round shape and seats

- Shape: default two v1 waves, each validated under `scripts/hyaku/ufo-wave-policy.json` and sent as one `task`
  call carrying the validator's `taskCall`; seat gate granted both (build 33, falsify 38). The L1 held the
  planner seat.
- Wave 1 build: **33 seats** — scribe 12, scout 7, executor 5, critic 3, reviewer 3, mutation-tester 2, connector 1.
  0 died; 2 cancelled by the L1 after an hour without a report (`DescDraft`, `D2D4Wording`; their work was done by
  the L1); `FloorsRegister` and `PrecedenceDraft` returned late and were superseded.
- Wave 2 falsify: **38 seats** — reviewer 26, critic 6, mutation-tester 5, scout 1. 38 returned, 0 dead.
- **Round total 71 seats**, no residual call. Attack roles 8 + 37 = 45 of 71 (63%). Both gate reservations released
  after every seat returned or was cancelled.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs/updates: none by the L1 or any seat that reported.
- L0: one line appended (fleet `8d56eb1`): integrator ruling on kotoba's boundary rule and its three closures.
- Carried to round 51: checklist gate fail-open on unprobeable delegates (`falsify/ReviewBoxProofGate.md`),
  driver laundering paths, guard mutant survivors, F30–F33 floors arms offered by `build/FloorsRegister.md`,
  R1/R4/R5, omp 18.12.6 re-pin.
- Observed, not caused: `verify_surfaces.py`, `verify_harness_claims.py`, `check_substrate_pins.py` red at base and
  head (omp 18.12.6); `report_dead 2` from the closure-owned round-48 spot-check.
- Misroot sweep (run after every seat returned): one round-49 kotoba seat report found in the fleet root, moved into
  the lane byte-exact and removed (lesson M32); nothing from round-50 seats. Remaining fleet-root changes belong to others.
- Driver completion is not admission; the non-author closure judges both claims.
