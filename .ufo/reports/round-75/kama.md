# kama round 75 — interpretation pins, survivor certification, accepted-history accounting

Lane: kama (`/home/vgpnk/Projects/shokunin/kama-shokunin`). Round 75 attempt 1. Base
`dc58e51315e79d36df5fc530c95fbd3aecbf7593`; freeze `0908bab5cbf0ab6b435144fc525a3e18443dc08f`
(`plans/round-75-claims.md`); measured work revision `c9ab73d842051db5f8320bced4357bf13cf14108`;
final lane tip `2ef8dc2ee1b87ce69db3e066d0d158b16c87cfa1` (branch `master`, `origin/master`
`2ef8dc2ee1b87ce69db3e066d0d158b16c87cfa1`). Assigned axes operability + calibration; claims C1
calibration, C2 operability, C3 freshness. Round shape: ONE v1 wave, 13 seats.

## Work performed

Declared claims (frozen before any seat scored): **C1 calibration** — the two routed interpretation
debts (F1b older-demonstrated `total`, F2c revision-mention context) become declared readings with
mutation kill arms; **C2 operability** — five named source mutants of the committed receipt-claim
module are each caught by their owning selftest arm (two were unarmed); **C3 freshness** — every
audit-undisclosed deletion event is graded as accepted history by a committed, hash- and
class-bound register, and every append-only contract declaration binds.

- C1 build and measurement: `tools/round75-interpretation-pins.py` (2 pins, declared + mutated
  reading per pin) — `INTERPRETATION_PINS pins=2 declared=2 killed=2 escaped=0`, exit 0
  (`.ufo/waves/round-75/measured/after/c1-pins.out`); selftest `INTERPRETATION_PINS_SELFTEST pass=3
  fail=0` with the cheat arm red (`measured/after/selftests.out`).
- C1 attack: RV01PinsReview rebuilt both boundary fixtures independently (pristine `total=3` vs
  mutant `total=5`; pristine exit 0 vs literal-hex mutant `stale-revision`) and attacked the landed
  counter with four controls — hardcoded module output (`declared=2 killed=1 escaped=1`, exit 1),
  mutant-equals-declaration (`declared=1 … escaped=1`), distinct-byte no-op mutants (`escaped=2`),
  non-discriminating fixtures (`escaped=2`); verdict `P1 load-bearing`, `P2 load-bearing`
  (`.ufo/waves/round-75/w1/RV01PinsReview.md` §Addendum).
- C2 build: the two missing arms `conflicting-headers` and `header-window-fifth-line` in
  `tools/round74-receipt-claim-binding.py` (selftest `RECEIPT_CLAIM_V2_SELFTEST pass=11 fail=0`) and
  `tools/round75-survivor-probe.py` — `SURVIVORS2 mutants=5 killed=5 escaped=0`, exit 0
  (`measured/after/c2-survivors.out`), selftest `SURVIVORS2_SELFTEST pass=5 fail=0`.
- C2 decision (round-74 hand-off): the same-line inherited kind keeps its existing r74 arm
  (`same-line-stale-claim`); the probe certifies it load-bearing via `kind-boundary`; no new fixture
  added. Recorded in `.ufo/waves/round-75/w1/EX02Survivors.md` and the lesson.
- C3 build: `registry/append-only-declarations.md` (six explicit declarations), the five unbound
  `declared_at` cells in `registry/append-only-contract.tsv` re-pointed (plus the SCORECARD exempt
  region pointer and a contract row for the register itself), `registry/append-only-accepted.tsv`
  (389 rows over 53 events, 463 line occurrences, all class `in-place-edit`), and
  `tools/round75-append-accepted.py` — `APPEND_ACCEPTED events=53 accepted=53 unaccepted=0
  bad_rows=0 bad_declarations=0`, exit 0 (`measured/after/c3-append-accepted.out`); selftest
  `APPEND_ACCEPTED_SELFTEST pass=12 fail=0`.
- C3 attack adopted: sentinel SN01Register demonstrated that a register row could bless a deletion
  made *after* the register's introduction (fresh-damage, high) and that the register was read from
  the worktree (provenance). Both fixed in the landed counter: every row's commit must precede the
  register's introduction commit (`post-introduction` finding, selftest arm) and the register is
  read from the audit's `to` revision via `git show` (`.ufo/waves/round-75/w1/SN01Register.md`).
- Gate wiring: `tools/pre-report-gate.py` gains arm 8 `round75-instruments` composing the three
  counters; `PRE_REPORT_SELFTEST pass=18 fail=0` (was 15).
- Contract declarations: `python3 tools/append-only-audit.py --repo .` now prints
  `bad_declarations=0` with `unrestored=53` unchanged (`measured/after/append-only-audit.out`); the
  audit's nonzero exit is its `unrestored` population, which the register grades and never erases.
- Frontier: S547 appended (`gitattributes(5)`, tier A, `mined`), retained bytes and quote in
  `.ufo/waves/round-75/w1/sources/gitattributes.html` + `measured/before/source-gitattributes.receipt`;
  knowledge entry `corpus/knowledge/append-only-accepted-history.md`; census exit 0 over 287 rows.
- Round-74 routed duties: coverage-map block (§"Coverage map — round 74 addition", 7 remaining gaps),
  three new `corpus/QUALITY.md` criteria KQ123–KQ125, calibration-row closure pointer re-anchored to
  `round-74-verifier-spotcheck.md`, RVW01 exit-map note pinned in the lesson, erratum and
  cross-domain line below.
- Attack seats on record: RV01 (above), CR01Falsify (C1 repo-identity gap, C2 holds, C3 offline-
  authority gap), MT01Mutants75 (9 mutants of the three new tools: 34 killed of 26 applied across
  three modules — 7 escapes, all composed-counter/leg-wiring/selftest-oracle classes, routed),
  SN01Register (two findings, both adopted), REV01Semantics (independent line-cited derivation of
  both readings), SC01Recon (source and audit re-derivation), CON01Overlap (sibling scan).
- No tool installs or upgrades ran; pacman stayed untouched.

## Landed changes

Every change is tied to the `LOG.md` round-75 entry and to the commit that carries it.

| Change | Commit |
|---|---|
| Frozen claims, control script, base receipts | `0908bab5cbf0ab6b435144fc525a3e18443dc08f` |
| Three new instruments, C2 arms, gate arm 8, register + declarations + contract, S547, knowledge entry, QUALITY/criteria + coverage map, SKILL registry rows, wave evidence | `10f37171fb696c542586cbee96ea4a509ab74afc` |
| SCORECARD exempt region bound to its own declaration line | `b8ed256829589a13a0ba2249a8ae9e2b8800fb5a` |
| SCORECARD §Round 75, capability canon (28), LOG entry, lesson, after receipts | `ba9f724800b7385fc3b732924ffebd143344367d` |
| Calibration closure pointer; lesson reword | `900e31b762d51b155fe79f2ef689ca52143e391e` |
| Record corrections; settled wave reports committed | `b982a4afdff72592cda2edabce37642fb7203c9a` |
| Superseded lesson bytes restored | `bd1198ab9e63ecb337bffb53bad857eddbace860` |
| Closure-count phrase; mistake 5 | `11c08bdc0064b9566dc220821db8b9116c6cf788` |
| PROVINCE capability evidence row names the three instruments | `c9ab73d842051db5f8320bced4357bf13cf14108` |
| Record pinned to `c9ab73d8`; supporting receipts re-measured | `ff63bce24e59571af7e9e59956a3783fb0cdf5c4` |
| Self-description reconciled (banner, canon mirror, saturation, planned) | `e87f1f3c2ad78da5d031d4e7836fb9a09466d4f9` |
| Depth/coverage rows re-anchored; planned pointer | `b919f0cb35f40e444899b8de70ea79b813ece678` |
| Operability run facts re-anchored (gate 18, claim-v2 11) | `ac1c8538e391bb76cf1118da10d375b95cc4c1e9` |
| Superseded head/axes lines held verbatim | `74a470bcf463a7d03158757b88d6a69aaf055ea5` |
| Gate receipt at `74a470bc` | `2ef8dc2ee1b87ce69db3e066d0d158b16c87cfa1` |

## Before → after measurements

| Claim | Axis | Before | After | Counting command | Measured commit |
|---|---|---|---|---|---|
| C1 | calibration (7 → 7) | both mutated readings ship green under the modules' own selftests: `CONTROL_C1 killed=0 escaped=2` (`.ufo/waves/round-75/measured/before/c1-mutants.out`) | `INTERPRETATION_PINS pins=2 declared=2 killed=2 escaped=0`, exit 0 (`measured/after/c1-pins.out`) | `python3 tools/round75-interpretation-pins.py --repo .` | `c9ab73d842051db5f8320bced4357bf13cf14108` |
| C2 | operability (8 → 8) | `CONTROL_C2 killed=3 escaped=2 c2_conflict_off=escaped c2_header_window=escaped` (`measured/before/c2-mutants.out`) | `SURVIVORS2 mutants=5 killed=5 escaped=0`, exit 0 (`measured/after/c2-survivors.out`) | `python3 tools/round75-survivor-probe.py --repo .` | `c9ab73d842051db5f8320bced4357bf13cf14108` |
| C3 | freshness (8 → 8) | `unrestored=53 … bad_declarations=5`, no register (`measured/before/c3-audit.out`) | `APPEND_ACCEPTED events=53 accepted=53 unaccepted=0 bad_rows=0 bad_declarations=0`, exit 0 (`measured/after/c3-append-accepted.out`); audit `bad_declarations=0`, `unrestored=53` (`measured/after/append-only-audit.out`) | `python3 tools/round75-append-accepted.py --repo .` | `c9ab73d842051db5f8320bced4357bf13cf14108` |

Pre-report gate at `74a470bcf463a7d03158757b88d6a69aaf055ea5` (clean tree, `uncommitted=0`):
`PRE_REPORT round=75 arms=8 failed=1 uncommitted=0` (`measured/after/pre-report-gate.out`). **Arm 7
is red for a non-claim cause**: the round's own record cites the spec generator, a `.py` control
input, and the receipt-binding counter refuses any cited path whose extension is not
`.out/.txt/.log/.json` (`RECEIPT_CLAIM_V2 CouldNotEvaluate … cited path is not a receipt file (.py)`).
The append-only contract forbids dropping the line once filed, so the bytes are held and the record
exits 2 until the counter-scope question is ruled (routed to round 76). Arms 1–6 and 8 are green;
arms 8's three counters are the three claim measurements above.

Axis harm check: operability 8, freshness 8, depth 7, coverage 9, calibration 7, adjacency 7 — no
score dropped, no axis retired. Population at the measured revision
(`measured/after/population.out`): gate registry `registered 92 unregistered 0 defective 0`; sources
census exit 0 over 287 rows; filtered knowledge entries 45 (base 44); `SKILL.md` 1736 lines sha256
`f18c9bcc…`; `PROVINCE.md` 322 lines sha256 `af459acf…`.

## Sources & frontier

`SOURCES: 286 → 287` (`scripts/sources-census.sh census --file corpus/SOURCES.md`: rows 287, tier A
273, B 10, C 4, mined 259, queued 8, rejected 20, missing 0). Census before and after:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`
→ `kama ok …/corpus/SOURCES.md`, **exit 0** at round start (286 rows) and at round end (287 rows);
no exit-2 start state (the registry already existed).

- Rows added by tier: A +1 (S547).
- Rows touched old→new: S547 `absent → mined` (the only row added or changed; no status, recheck or
  used-by cell of an existing row moved this round).
- Frontier rows advanced: `knowledge/append-only-accepted-history.md` is new and cites S547; it
  converts the audit's `unrestored` population from an ungraded red into a graded class. Coverage-map
  block for the round-74 entry appended (7 map gaps remain, named in `corpus/README.md`).
- Assimilation: `Assimilation: none`. `merge/kama/` was re-derived read-only at
  `.ufo/waves/round-75/assimilation/summary.out`: `reg_ids 286 · staged_ids 142 · collisions 9
  (S330 S333 S334 S335 S346 S347 S352 S353 S363) · quarantine_rows 7`; the nine staged-id collisions
  are still mass drift the read-only merge cannot resolve, so nothing is adopted.
- considerthese: one still-unimplemented proposal mined (`considerthese/2026-10-26.md` proposal 2,
  tracking one's own proposals); the lesson's §considerthese table dispositions all eight proposals
  of the two newest files, each re-opened this round.
- Source opened this round: `https://git-scm.com/docs/gitattributes`, access 2026-11-04, located
  ≤25-word quote "Line endings are normalized to LF in the index every time the file is checked in"
  (16 words), retained bytes sha256 `ceb3351f931ae86283f51416cf0042fd78265eda59e5af7d09e17581ec0f77f7`.
- Cross-domain evidence: the accepted-history/append-only accounting question is a fleet-meta
  (protocol/aggregator) surface — a lane-owned register only frames its own history; kama reports the
  pattern and keeps it lane-local (`corpus/knowledge/cross-lane-scope.md`).

## Trend verdicts

- **expansion — improved.** Knowledge entries 44 → 45, registry 286 → 287 (one tier-A row), canonical
  capability list 25 → 28 (`interpretation-pins`, `survivor-probe`, `append-accepted`), each entering
  through a round that ran it (`measured/after/population.out`, `measured/after/selftests.out`).
- **quality — improved.** Two unarmed documented rules and two ungraded interpretations now have red
  mutation receipts and green real runs (before receipts `c1-mutants.out`, `c2-mutants.out`; after
  `c1-pins.out`, `c2-survivors.out`); all ten contract declarations bind (`bad_declarations 5 → 0`);
  three QUALITY criteria (KQ123–KQ125) and the gate's eighth arm landed. Bounded: arm 7 stays red for
  the record-citation cause above, and MT01's seven escapes are named, not hidden.
- **discernment — improved.** A non-author critic/sentinel pair overrode the author on substance:
  SN01's fresh-damage finding changed the landed counter (temporal cutoff), and CR01's repo-identity
  and offline-authority gaps are recorded as `under-specified` rather than passed. RV01's four counter
  attacks were each scored red on the landed instrument. One satisfied prediction would have been
  cheaper; the record keeps the disagreements.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — three new
  registry rows and the eight-arm gate row landed (`SKILL.md:303-322`); no non-author promotion review
  this round, so not `[x]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the three instruments ran
  end to end on the lane (`measured/after/*.out`), LOG entry appended.
- [~] Instructions executable by an agent without oral context — the wave's 13 seats ran from the
  written spec alone; the two arms were added from the item text.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE row extended with the three
  instruments only; the fleet-meta observation stays reported, not absorbed.

## Extras

- **Erratum (round-74 report):** `.ufo/reports/round-74/kama.md:102` says the receipt audit printed
  `cited=200 resolved=182`; the receipt committed at `8020b2f2` (`measured/after/pre-report-gate.out`)
  says `cited=202 resolved=184`. The receipt is authoritative; the report text is superseded here.
- **Stale-lane line:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (no `uv`, `npx`, `cargo`, `npm` or binary installs; pacman never
  invoked).
- **Wave shape:** one v1 wave (`ufo-wave-policy.json`, band 8–16), 13 seats — 3 executor, 3 scribe,
  1 scout, 1 connector, 1 reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 revenger; attack share
  5/13 = 38 % (≥25 %); 1 connector (≤2); planner seat held by the L1 per the standing L0 answer.
  No residual call was made. Round total: 13 seats.
- **Dead seats:** none — all 13 settled and filed a report (`w1-results.json`, 13 results).
- **Disclosed claim limits:** C1's counter resolves modules beside itself and accepts any `--repo`
  directory (CR01Falsify §C1, routed); C3's `--audit-json` override accepts an unauthenticated audit
  (CR01 §C3, routed); MT01's seven escapes are composed-counter/leg-wiring/selftest-oracle classes
  and need the arms it names. None of these changes the three measured values above.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only the round's
  report plus orchestrator-owned `.scratch/` paths and one fleet-root stray named `after` (24 bytes,
  mtime 2026-11-03 20:05, before this wave, naming no lane or round); it is not mine and was left
  untouched. No seat of this wave wrote into the fleet root.
- **L0 questions:** none opened this round; the round-65 NTFS-path and MISSION/AXES freshness
  questions stay open and unanswered, routed around as before.
