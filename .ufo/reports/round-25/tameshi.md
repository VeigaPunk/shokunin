# tameshi — round 25 report (attempt 2)

Author: TameshiR25, a fresh in-session L1 lane subagent of the hyaku orchestrator, dispatched 2026-10-22T08:02:57Z. The attempt-1 author from 2026-10-21 was not resumed. Lane HEAD after the round: `f4e8f7d835a8e33c64a87ff93e79da32264f031c` (pushed, `jj-lane.sh state`: local = remote, ahead 0). Base: `1f7315732e0cfe0ba9dfe0fff2ef36d1c8481bb5`.

## Work performed

The round declared two claims. Both were frozen in `.ufo/evidence/round-25/contract.json` at `2a97ec1` before any seat ran:

- **C1, calibration (repair-first).** Calibration is the lowest owned numeric axis, tied with depth at 8. The three round-23 closure-routed items that round 24 left unrecorded were the multi-token stdout fixture in the ruler, the re-run guard sweep, and the dead-falsifier coverage gap. That omission was routed by `corpus/lessons/round-24-verifier-spotcheck.md:37,63`. Each item now has a SCORECARD disposition row and an executed check. The claim counts mismatches between the lane's record and the routed state.
- **C2, coverage (capability acquisition; learning claim; frontier F1 report interop).** `tools/mte-interop.py` emits the eight recorded mutation-ledger legs as mutation-testing-elements reports. It validates them against the official schema 3.9.0 and scores them with the official metrics library 3.9.0. Both packages are vendored and sha512-pinned in `tools/vendor/`. The new admitted knowledge entry is `corpus/knowledge/mte-report-interop.md`, and it cites the new sources S086 and S087.

Work items:

- **Fixtures and rulers.** I wrote the C1 ruler fixtures, both mutant specs, the suite, the counter and the before receipts. Paths: `.ufo/evidence/round-25/{multitoken-cases.json,multitoken-mutants.spec,guard-mutants.spec,c1-suite.py,c1-measure.py,c1-before.json}` (commit `2a97ec1`).
- **Interop tool.** I wrote `tools/mte-interop.py`, the vendored tarballs and `c2-before.json` (`2a97ec1`). Amendment 1 (`c9ff09f`, recorded in `contract-amendment-1.json`) added `--fleet-root` staging, because at `2a97ec1` a clone returned `MTE_INTEROP: SETUP (regression exit 2)`.
- **Wave.** One v2 wave of 65 seats, validated under policy v2 (`.ufo/waves/round-25/spec.json`, `dispatch.json`, `record.json`). All 65 seats returned callbacks and none died. Reports are in `.ufo/waves/round-25/w1/`.
- **Amendment 2, before any after measurement** (`09dc114`, `contract-amendment-2.json`). The wave showed the frozen rulers were weaker than the routed items, so I added checks:
  - Seat MtWeakerGate showed four strictly weaker token matchers survived. Fixtures 8–11 and mutants M7–M10 were added.
  - Seats QualityCriterion and C1Framing showed that only four of round 23's ten guard anchors had been re-run verbatim. G9–G14 now cover all ten.
  - Seats MeasureVacuity and C1Framing showed the counter checked no input pins. I added the `c1-pins.py` input-pin check.
  - Seat C2Tautology showed score equality holds by construction. I added the `ledger` check (against the runner's REGRESSION_TABLE) and the `per_mutant` check (against the committed TABLE_* per-defect verdicts).
- **Amendment 3** (`77302fa`, `contract-amendment-3.json`):
  - The C2 leg set must equal the eight ledger legs (seat C2TarSafety: one-leg PASS).
  - The tar member guard was tightened, and node timeout now reports SETUP.
  - A narrow score-delta selftest case was added (seat C2Mutants: tolerance mutant).
  - c1-pins P5 now requires the exact row shape (seats DraftLesson and C1BeforeRerun: a row reading "NOT dispositioned" passed).
  - No target, claim population or frozen-counter byte changed; the c1-measure.py sha256 is unchanged in every amendment.
- **Dead-falsifier disposition.** All 34 round-23 wave-2 seats that died were re-attacked by fresh seats. Result: 20 AGREE and 14 FINDING (`.ufo/evidence/round-25/dead-falsifier-disposition.json`). The 14 findings are routed in `corpus/lessons/round-25.md`, under "Wave findings routed forward".
- **Corpus.**
  - New entry `corpus/knowledge/mte-report-interop.md`, which includes a decision table.
  - SOURCES rows S086 and S087.
  - QUALITY 50, a routed-item ledger by identity: `corpus/QUALITY.md`, tail.
  - Lesson `corpus/lessons/round-25.md`.
  - README coverage row and F1 status correction.
  - PROVINCE Core append.
  - SCORECARD round-25 section, with rows R23-ROUTED-1/2/3 and a capability row.
  - LOG entry.
- **Harm found and restored.** At `77302fa` the strict cold-read monitor read 45/62, restraint 6. The base read 62/62, restraint 8. Corpus edits had drifted the traced inputs of 17 SKILL.md sections. Both harmed readings are retained: `after/monitor-harmed-77302fa.json` and `after/monitor-harmed-154bf4d.json`. I restored the monitor with seventeen actual traced L1 source reads, using the round-23 re-anchor tool (`3b20f07`). The ledger's 287-entry byte prefix is unchanged (`source-prefix-preservation.json`). These are author source reads, not independent cold-reads.
- **Planner seat.** The L1 held the canonical planner seat; the validator refuses `planner` as a swarm role. Planning data-walks rode connector seat RoutingCarry and scout or reviewer items.
- **Inherited state.**
  - The lane was clean at start: `jj-lane.sh state` showed untracked 0, and there were no lane-dead leftovers in the lane repo.
  - The private trees `/fast/scratch/hyaku/tameshi-r25-author*` (a 52-case pre-registration) were not reused. Nothing from them was re-verified or continued.
  - I did not edit the operator-authored `round-24-verifier-spotcheck.md`. Its routing item 1 is C1. Items 2–4 stay open, with path:line evidence in seat SpotRouting2. Item 5 is fleet scope.

## Landed changes

Every change is pushed through `jj-lane.sh`. LOG.md carries the round-25 entry (LOG tail, "Round 25 — 2026-10-22").

| Commit | What |
|---|---|
| `2a97ec1782424f5fc0281e3ed08f89a2ee3dbdb9` | freeze: contract, rulers, fixtures, interop tool, vendored packages, before receipts |
| `c9ff09fb41fb8aac5fc335faf10858ff606bd5df` | interop `--fleet-root` staging |
| `5b69fb23a9c4a27ea13fabf966d131be169846a6` | amendment 1, validated 65-seat wave spec and dispatch |
| `09dc114da9002525d31985c14093d32c6712bff4` | amendment 2: M7–M10, G9–G14, c1-pins, ledger and per-mutant checks, census start receipt |
| `77302fa8f79144d06c1d2d2e2d2898c44b459bda` | wave reports, disposition, knowledge entry, S086/S087, QUALITY50, lesson, SCORECARD rows, amendment 3 (C1 and C2 measured here) |
| `154bf4d7bb6efdbb1678813322a17c161a08db96` | after receipts, emitted reports, measured SCORECARD rows, LOG, harmed intermediate retained |
| `3b20f073c7305a582562cd323982991464c324f3` | 17 traced re-anchors appended to the cold-read ledger |
| `d8fd1f2b3935e78d69c789c1aaf7cf7f0f3606fe` | final no-harm receipts and lesson record |
| `f4e8f7d835a8e33c64a87ff93e79da32264f031c` | late SiblingOverlap seat report |

## Before → after measurements

| Claim | Counting command | Before | After | Measured commit |
|---|---|---|---|---|
| C1 | `python3 .ufo/evidence/round-25/c1-measure.py --repo CLONE_AT_REV` | `C1_ROUTED: dispositioned=0/3`, exit 1 at `1f73157` (`c1-before.json`) | `C1_ROUTED: dispositioned=3/3`, exit 0 (`after/c1-measure.stdout`) | `77302fa`; re-checked 3/3 at `3b20f07` |
| C1 companion | `python3 .ufo/evidence/round-25/c1-pins.py --repo CLONE_AT_REV` | (new) | `C1_PINS: HOLD (0 failures)`, 10 pinned files | `77302fa`, `3b20f07` |
| C2 | `uv run --no-project --with jsonschema==4.25.1 python3 tools/mte-interop.py --check --fleet-root /home/vgpnk/Projects/shokunin` | tool absent at `1f73157`: exit 2, no file (`c2-before.json`), 0/8 | `MTE_INTEROP: PASS legs_conforming=8/8`, exit 0; every leg `per_mutant=ok failed=none`; selftest 17/17 | `77302fa`; the tool is byte-identical at `3b20f07` |

**Negative controls**, run in a scratch clone at `77302fa`:
- **One disposition row dropped:** C1 gives 2/3 and pins FAIL.
- **R23-ROUTED-2 row rewritten as "NOT dispositioned":** pins FAIL, but the frozen counter still says 3/3. That is a stated limit of the frozen counter.

**What the claims do not show:**
- C1's population is three fixed labels.
- The gate is unchanged since base, so the R1 and R2 kills are controls, not repairs (QUALITY48). Numeric calibration stays 8.
- In C2, score equality is only a sanity check; the `ledger` and `per_mutant` checks are the ones that carry information.

**No-harm, final, at `3b20f07`:**
- strict monitor 62/62, restraint 8, depth 8, overrides false;
- registry held 47/47, superseded 7, exit 0;
- census exit 0.

The harmed intermediates are retained, as described above.

## Sources & frontier

**Census.**
- Start: exit 0, 83 rows, seven W04 warnings (`.ufo/evidence/round-25/census-start.stdout`).
- End: exit 0, 85 rows, the same seven W04 warnings (`after/census-end.stdout`).
- Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`.

**Rows.**
- Added: two tier A rows, status mined, recheck 180d. S086 is the npm mutation-testing-report-schema 3.9.0 package; S087 is the npm mutation-testing-metrics 3.9.0 package. Each is used by `knowledge/mte-report-interop.md`.
- Opened: 2026-10-22, by the L1 (`npm pack` and `npm view dist.integrity`) and re-opened by seats C2SchemaSource, C2Integrity and DraftSources.
- Located quotes: in `corpus/lessons/round-25.md` `## Gate`.
- Touched: no existing row changed.

**Frontier.**
- F1's report-interop half moves to Core (README round-25 section, PROVINCE round-25 append).
- F1b, the NoCoverage classification of the 35 recorded survivors, stays open.
- The sourced claim is C2, which cites S086 and S087.

**Mined mistake** (lesson `## Mistakes`): round 24 declared a routed population that omitted three closure items. Fix: QUALITY 50, plus `c1-pins.py` P3/P5, shown able to fail.

## Trend verdicts

- **expansion: improved.** The F1 report interop moves to Core through an admitted, sourced entry, and two new mined source rows were added. Evidence: C2 8/8 and the README and PROVINCE appends.
- **quality: improved.** Stronger rulers: M1–M10 and all ten round-23 guard anchors are killed with witnesses. The interop has an independent per-defect check. Thirty-four dead falsifiers were re-run, finding 14 open defects. The no-harm monitor was restored to 62/62. Evidence: `after/`, the disposition file.
- **discernment: unprovable-but-better.** The round recorded and repaired its own weak rulers before measuring: amendments 2 and 3, plus two retained harmed intermediates. That is self-assessment, not an outside judgment, so it needs the closure to rule.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion; this round's decision table lives in `corpus/knowledge/mte-report-interop.md`; no independent promotion verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-25 entry; C2 counter `after/c2-check.stdout`; no independent promotion verifier.
- [~] Instructions executable by an agent without oral context — `.ufo/evidence/round-21/coldread/ledger.json` (restored 62/62, `after/monitor-final-3b20f07.json`); input-keyed monitor only.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — seat SiblingOverlap found no contested scope (`.ufo/waves/round-25/w1/SiblingOverlap.md`); no independent promotion verifier.

## Round shape, seats and conformance

- **Shape:** one v2 wave of 65 seats (policy v2, band 64–100). Wave 1 carried the build and attack items together. There was no residual call, so the round total is 65 seats.
- **Role mix:** reviewer 28, critic 16, mutation-tester 4, scout 5, executor 6, scribe 4, connector 2. Attack roles total 48 of 65 (74 %).
- **Seats:** 0 dead. Seat C2Determinism returned a garbled final message (a tool call as text), but its report file exists.
- **Seat gate:** `wave-slot.sh acquire tameshi round-25-w1 65 1800` → granted; then released.
- **Bounds breaches by seats, all disclosed in their reports:**
  - ReReplay14 ran `jj log` at the fleet root, which printed a working-copy reset and a git import. Fleet `git status` now shows intent-to-add entries. Main was told at the time; the lane made no repair.
  - ReOutputComplete ran `jj st` in the lane.
  - Several seats ran `git status` without `GIT_OPTIONAL_LOCKS=0`.
  - ReReplay14 and ReReplay13 ran more suites than their items allowed, in /tmp only.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked files from this lane's seats. The fleet-root file `write` dates from 2026-10-21 and is not this round's.
- **Wave findings routed forward, not claimed:**
  - Seat MtGuardGaps: 17 weakenings of `command-binding.py` `evaluate()` that the gate selftest does not kill.
  - The 14 re-attack findings.
  - Seat SiblingOverlap: emitted reports name targets without lane, revision or pin, so the mado 4/10 leg can be misread against mado's current gate.
  - Spot-check items 2–4.
- **Tool installs:** none by the L1. Ephemeral `uv run --with jsonschema==4.25.1` (PyPI). The npm tarballs were vendored as lane files. Seat C2HtmlRender installed `puppeteer-core@23.11.1` via npm in /tmp scratch. No pacman transaction.
- **Open L0 questions:** none new. The round-18 helper-recovery question remains open, as before.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
