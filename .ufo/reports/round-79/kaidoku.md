# kaidoku — round 79 report

Lane: `kaidoku-shokunin` · round 79 (attempt 1; campaign target round 100) · 2026-11-04
Lane tip: `369fa6e7fe1af5c65f1014da2ef509e379ea9a10` (`git ls-remote origin refs/heads/main` at filing;
`jj-lane.sh state` local=remote, ahead=0, tree clean).
Base `29d2ca30b83a6a0d85b0aa979de0138fde1660e6`; declaration `a1f9b81cf0cd5065df3a9b25b30ce2eb184d012d`;
freeze `ed68cd0a6cc790cca342380a2d80d1927a668c8c`; landing `868710d6`; final record `369fa6e7`.

## Work performed

Two claims on two distinct axes (calibration + freshness), both capability acquisitions, causally separable.

- **R79-C1 (calibration) — the round-78 gate's selftest mutation survivors close.** `tools/round-79/gate-mutation.py`
  applies eight exact single-occurrence edits to `tools/round-78/attack-gate.py` at `--rev` and kills each mutant
  only when its ONE declared selftest case is present and failing; an absent case is a survivor.
  `tools/round-78/attack-gate.py` gains the three cases (`red-near-miss-unparsed`, `red-atom-absent`,
  `red-validate-refused-no-reason`). Evidence: `l1/scores/c1-at-base-final.json` (survivors 3: `m03`, `m05`,
  `m08`), `l1/scores/c1-at-landing.json` (8/8, survivors 0, sole detectors true), `pre/selftest-c1.json`
  (14 cases), `pre/selftest-gate.txt` (29 cases, round-78 spot-check item 4).
- **R79-C2 (freshness) — the record's pointers bind at the lines they name.** `tools/round-79/pointer-bind.py`
  binds `PROVINCE.md`'s five pointer cells at their 1-based line/range, requires each pointer to name the
  declared live object (round 78's `same_path` rule) and each token to occur there, and retains only a digest
  of the pointed lines. `PROVINCE.md`'s OMP and Kimi pointers are rebound `:8 → :12` and `:4126 → :4722` with a
  round-79 recheck pointer. Evidence: `l1/scores/c2-at-base-final.json` (mismatches 2: `omp-pin`, `kimi-pin`),
  `l1/scores/c2-at-landing.json` (5/5, 0 mismatches), `l1/scores/c2-path-only-final.json` (control: 0 mismatches
  but `ok false`), `pre/selftest-c2.json` (21 cases).
- **Wave (L2 floor).** `r79-w1`: 12 seats in ONE v1 wave under policy v1 (band 8–16) — 3 executor, 2 reviewer,
  1 critic, 1 mutation-tester, 1 sentinel, 1 scout, 1 connector, 2 scribe; attack roles 4/12 = 33 %, one
  connector; the L1 held the planner seat (the validator rejects a planner role). All 12 settled, 12 non-empty
  reports, 0 dead (`r79-w1-results.json`; reports under `w1/`). No residual call.
- **Independent re-derivation (seats).** `ExecBaseArm` re-implemented the mutation application (8 mutants,
  survivor set identical); `ExecCaseInventory` re-derived 26 → 29 cases with each added case the sole failure of
  its mutant; `ExecRebind` re-implemented the binder (digests converge; base 2 mismatches, freeze 5/5);
  `ReviewerC1` refused 17 forged C1 receipts; `ReviewerC2` ran sixteen attack shapes and found the
  counting-command defect; `MutInstruments` mutated both instruments (four `validate_receipt` guards and the
  `battery()` cell survive — routed); `SentinelScope` found no secret-bearing receipt field and routed path /
  scratch / `--rev` findings; `ScribeSources` re-fetched both sources byte-identically; `ScribeLesson` and the
  `ScoutRouted`/`ConnectorSibling` reports as filed.
- **In-round repairs the wave forced** (disclosed in `claims.json` `instrument_supersessions`, commit
  `868710d6`): the frozen R79-C2 counting command omitted `--battery` (battery is now the default when `--rev`
  is supplied, so the frozen sentence runs verbatim); a `--control` receipt records `would_pass` and never `ok`;
  each pointer must name the declared live object (red self-pointer case); R79-C1's `ok`/`--validate` score the
  pristine `29 cases` and the three named sole detectors; both receipts carry the producing instrument's digest,
  a timestamp and a 40-hex rev; the dead `line_count` parameter is removed. Predicates, counters, kill rules and
  targets are unchanged.
- **Frontier step.** `corpus/SOURCES.md` curated (S295, S296; pre-append check at `.ufo/…/l1/pre-append-url-check.txt`);
  one knowledge entry `corpus/knowledge/2026-11-04-r79-mutation-and-pointers.md`; coverage map row added;
  mistake rows M79-1…M79-6 in `corpus/lessons/round-79.md`; QUALITY rows 138–140; coverage self-check
  `162/162` mapped, `mismatches 0` (`l1/scores/coverage-selfcheck-at-record.json`).
- **Spot-check of round 78.** Routed items 1, 2, 5, 6 closed in this record/report; item 3 rides R79-C2; item 4
  closed by `pre/selftest-gate.txt`; the round-78 freeze container gains its fifth supersession (`da8e5d5e`).
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/*`
  (orchestrator-owned), `.ufo/l0-questions.md` and `scripts/hyaku/*` (other lanes/operator),
  `.ufo/reports/round-82/kama.md` (sibling lane) and a Nov-3 `after` file (not this round); no seat wrote into
  the fleet root. Nothing moved.

## Landed changes

Each change is in the lane repo and tied to the round-79 LOG entry (`LOG.md`, heading
`## 2026-11-04 — round 79 …`) and a commit:

| change | commit | LOG entry |
|---|---|---|
| two instruments, three new gate cases, `PROVINCE.md` pointer rebind, `plans/round-79-claims.md`, base receipts, selftests, controls, census-start, two source snapshots | `a1f9b81c` | Round 79 — claims / the three new selftest cases / record repair |
| frozen `claims.json` with both predicates, kill rules and instrument pins | `ed68cd0a` | Round 79 — claims |
| wave spec, generator and validated 12-seat dispatch | `e0c19339` | Round 79 — wave |
| round-78 freeze container: fifth supersession for the round-79 gate revision | `da8e5d5e` | Round 79 — record repair |
| hardened instruments, `SCORECARD` round-79 section + capability rows, `LOG`, `SKILL` rows, SOURCES/README/QUALITY/knowledge/lesson, wave evidence (`w1/`, results, ready, receipts) | `868710d6` | Round 79 — claims → wave |
| both post-freeze instrument revisions disclosed with forced reasons | `1caf23ed` | Round 79 — in-round repairs |
| freeze ledger row + end census (exit 0, 202 rows, 23 W04) | `4e23255a` | Round 79 — filing |
| record gate receipt (both freezes CLEAN, disclosures exact 54/54) | `eb301514` | Round 79 — filing |
| prefile PASS receipt + filing pointers | `dd10ffd3` | Round 79 — filing |
| coverage row cites the round-79 self-assessment | `954ed89c` | (standing duty, Round 79 — sources) |
| coverage self-check receipt at the record (162/162, mismatches 0) | `369fa6e7` | Round 79 — sources |

## Before → after measurements

**R79-C1 (counter `survivors`).**
Command: `python3 -I -B tools/round-79/gate-mutation.py --root . --rev <measured> --work <scratch> --battery --json-out <receipt>`
then `… --validate <receipt>`.

- Before, base `29d2ca30` (`l1/scores/c1-at-base-final.json`): exit 1, `mutants_total 8`, `killed 5`,
  **`survivors 3`** naming `m03-near-miss-re-dead`, `m05-atom-absent-bound`,
  `m08-validate-no-refusal-guard`; `declared_case_hits 5`; `target_pin.matched false`; pristine 26 cases.
- After, record `ed68cd0a` measured with the final instrument bytes (`l1/scores/c1-at-landing.json`,
  committed at `868710d6`): exit 0, `mutants_total 8`, `killed 8`, **`survivors 0`**, `declared_case_hits 8`,
  `target_pin.matched true`, pristine `cases 29 failures 0`, `sole_detector true` for `m03`/`m05`/`m08`;
  `--validate` → `{"defects": [], "mutants": 8, "survivors": 0}` exit 0.
- Controls: empty set `mutants_total 0, ok false` exit 1 (`l1/scores/c1-empty-set-final.json`); the base arm
  itself is the do-nothing control (survivors 3, target missed).

**R79-C2 (counter `mismatches`).**
Command: `python3 -I -B tools/round-79/pointer-bind.py --root . --rev <measured> --json-out <receipt>`
then `… --validate <receipt>`.

- Before, base `29d2ca30` (`l1/scores/c2-at-base-final.json`): exit 1, `checks_total 5`, `matched 3`,
  **`mismatches 2`** naming `omp-pin` (record `:8`, pin at `:12`) and `kimi-pin` (record `:4126`, pin at `:4722`),
  `unparsed 0`.
- After, record `ed68cd0a` with the final instrument bytes (`l1/scores/c2-at-landing.json`, committed at
  `868710d6`): exit 0, `checks_total 5`, `matched 5`, **`mismatches 0`**, `unparsed 0`; `--validate` →
  `{"checks": 5, "defects": [], "matched": 5}` exit 0.
- Control: `--control path-only` at base (`l1/scores/c2-path-only-final.json`) reports `mismatches 0` on the
  stale record but `ok false` / `would_pass true` — the rule that cannot fail, and it is never a pass.

## Sources & frontier

- **Census.** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` — start: exit 0,
  200 rows, 23 W04 warnings (`l1/census-start.txt`); end: exit 0, 202 rows, the same 23 W04 and none added
  (`l1/census-end.txt`). Counting command:
  `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 200 → 202.
- **Rows added by tier.** tier A: 1 (S295 POSIX.1-2024 `grep` OPTIONS `-n`, the 1-based per-file line numbering
  a `path:line` pointer inherits); tier B: 1 (S296 cargo-mutants book, the surviving-mutant vocabulary).
  Mined 2, rejected 0. Pre-append check at the freeze rev: neither host present, 200 rows
  (`l1/pre-append-url-check.txt`); both snapshots byte-identical to the source seat's independent fetches.
- **Rows touched old→new.** None: no existing row's `status`, `recheck` or `used-by` changed.
- **Frontier rows advanced.** None: the new knowledge entry sits on the lane's own instrument/record layer
  (coverage-map row "Instrument and record layer, round 79" says held, not a new carrier class). The knowledge
  entry is `corpus/knowledge/2026-11-04-r79-mutation-and-pointers.md`; the coverage self-check reports
  `162/162` mapped, `mismatches 0`.
- **Assimilation: none.** The stage package `merge/kaidoku/` was not drawn on: this round's moves are the gate's
  selftest detectors and the record's pointer cells, and the package's staged ground (carriers, vendors,
  toolchain surveys) fits neither claim. `considerthese/` does not exist in this lane.
- **Sourced claim.** R79-C2's line rule rests on S295 (opened this round, 18-word located quote at snapshot line
  97); R79-C1's survivor rule rests on S296 (17-word quote, snapshot lines 184-186). Both rows are cited by the
  knowledge entry.

## Trend verdicts

- **expansion: unchanged.** Two rows enter (S295/S296, 200 → 202, census exit 0 both ends) and one knowledge entry
  lands, but on already-mapped instrument/record ground; no frontier → core move, no new carrier class.
- **quality: improved.** Two real defects in the round-78 record are fixed with dated receipts (the two stale
  pointers and the blind pointer rule); the gate's selftest gains three behavioural cases and the mutation
  question becomes a committed battery; the wave forced five in-round repairs, each disclosed with unchanged
  predicates. No admitted entry failed a re-check; the coverage self-check is green at 162/162.
- **discernment: improved.** The outside attacks are answered honestly: ReviewerC2, CriticClaims and ScribeLesson
  found the counting-command defect, the control that self-declared `ok`, the dropped declared-path pin (a
  regression against round 78) and two recorded-but-unscored predicate conjuncts; all were closed in-round and
  disclosed. What was *not* adopted is named: a declared case may assert source text rather than behaviour;
  `--validate` is internal consistency, not authenticity; the Critic's §9 reading that R79-C2 is a strictness
  increment on the round-78 pointer rule (the capability row is worded as a revision), and that `freshness` is a
  fleet axis rather than a lane-owned proxy; MutInstruments' four surviving `validate_receipt` guards and the
  `battery()` cell; SentinelScope F2–F8. No claim was contradicted by a seat.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.

**Tool installs:** none this round (no pacman transaction; no tool installed or upgraded).

**Routed to round 80:** (a) one isolating selftest case per surviving `validate_receipt` guard and for the
`battery()` unparsable-copy cell, with a mutation patch set that scores them; (b) a case-behaviour check for
declared detectors (CriticClaims Q2) and a receipt-authenticity step (a receipt that re-derives its own
selftest); (c) duplicate-cell precedence and an anchored (word-boundary) pin match in `pointer-bind.py`, each
with a red case; (d) execute every plan's printed counting command verbatim at the freeze via
`tools/round-76/plan-command.py`; (e) SentinelScope F2–F8; (f) standing duties every round that lands receipts;
the r63 record-section sweep and the r58/r60/r64 items stay named debt.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the round-79
  instrument rows cite `tools/round-79/*.py` and their selftest runs; the craft/decision tables are the
  round-73–78 blocks (unchanged this round).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round-79 LOG entry records both
  gated tasks end to end (`LOG.md` `## 2026-11-04 — round 79`, receipts `l1/scores/c1-at-landing.json`,
  `c2-at-landing.json`).
- [~] Instructions executable by an agent without oral context — the two claim predicates run as printed
  (`plans/round-79-claims.md`; receipts above); the frozen R79-C2 text now runs verbatim after the disclosed
  mode default.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` re-read through the pointer binder
  (5/5 bound, `l1/scores/c2-at-landing.json`); the sibling-lane precedents found by `ConnectorSibling`
  (`tameshi-shokunin/tools/pointer-recheck.py`, `mutate-and-run.sh`) are reported as contention, not absorbed.
