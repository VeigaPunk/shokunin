# tameshi — round 93 (attempt 1)

Lane `tameshi` (verification-fixture craft), base `4a7e259b407d582d2010197f32d7524d6bed5370`,
final lane tip `848412ee0d167db99cf81432d0b237fb16d2fdda` (pushed; `jj-lane.sh state` →
`ahead=0 behind=0`), freeze `978f04bc471143fae612709e4cce349358b46a2e`.

## Work performed

Two declared claims, both measured; no exploratory claim; no capability claim beyond C2's
instrument (whose row enters the capabilities table because its selftest and its real run both
executed this round).

- **R93-C1 (coverage — the lane's lowest-scoring axis; fourth attempt at certifying the
  round-90 fleet-gate mutation case).** The case note
  `corpus/knowledge/mutation-case-fleet-sources-census.md` is certified by a **verdict-content
  reader**: a table is keyed only when its *header row* carries a `verdict` cell, so an
  id-keyed table that asserts no verdict no longer refuses an honest note (the exact class
  that killed R92-C1). Instrument `.ufo/evidence/round-93/c1/measure-v93.py`
  (`855f0c1c`, sha256 `18903602aa040b7e258fd6c81491cfee4ea7bb0575784fe27e351587fe094c2d`,
  self-pin `9a073d35…99e2`), 19 conjuncts, 35-control battery
  (`.ufo/evidence/round-93/c1/controls-v93.py`, `69d377a0`, sha256 `400d8e0f…da74`).
  Evidence: `C1_R93_PASS=true` at the instrument revision and again at the landing revision
  (`.ufo/evidence/round-93/landing/measure-at-landing.txt`); battery summary
  `.ufo/evidence/round-93/pre-freeze/controls/C1-summary.txt` → `states=35 matched=35
  mismatches=0 missing=0`.
- **R93-C2 (calibration).** `tools/conjunct-disposition.py` +
  `tools/conjunct-disposition.json` (`9bf52b03`) audit the counter's own claim about what it
  measures: every one of the 19 conjuncts has a manifest row naming a committed receipt that
  moves it, or an `unfalsifiable` reason naming the mechanism that forbids a falsifier.
  Evidence: `DISPOSITION rows=19 falsifiable=17 unfalsifiable=2 findings=0`, exit 0, at the
  landing revision (`.ufo/evidence/round-93/landing/c2-at-landing.out`); `--selftest` → `6/6
  pass` (`.ufo/evidence/round-93/pre-freeze/c2-selftest.out`).
- **Frontier step.** `corpus/SOURCES.md` 180 → 182 rows: S321 (GFM tables, §4.10) and S322
  (CommonMark 0.31.2, §4.5 fenced code blocks) opened this round with located quotes in the
  lesson's Gate; S320 re-opened (byte-identical re-fetch) and its `used-by` extended, logged
  old→new in the lesson. Six rows of the Gate table (three admits, three rejects) with flip
  conditions. Census: `sources-census.sh validate --root … tameshi` → `tameshi ok`, exit 0
  (before: exit 0 at `4a7e259b`, 180 rows).
- **Mistake mined.** Ten, `corpus/lessons/round-93.md` `## Mistakes` M1-M10, each with the
  artifact that caught it and a fix shown able to fail (M1 first-run receipt, M2 `D01`
  control, M5 `R93SN1-probe18.log`, M6 `R93R1-probe4.py`, M7 the width probe, M8
  `R93M1-sharp-output.txt`, M9 the receipt-guard probes, M10 the `GIT_DIR` probe).
- **considerthese.** `considerthese/2026-11-07.md` idea 5 (receipt write safety) is
  implemented as the driver's `receipt_path()`; R93SN1 F2/F3 show the guard's two remaining
  holes, routed (M9). Idea 1 (`hardening-lint`) is re-run over the new counter and its
  defence list curated to the successor forms.
- **Assimilation: none** — no staged `merge/tameshi/` theme serves a table-shape reader; said
  here per the contract.

Wave: **one v1 wave `r93-w1`, 12 seats**, attack 4/12 = 33 % by the policy's role set
(reviewer 2, critic 1, mutation-tester 1) and 6/12 counting sentinel and connector; the L1
held the planner seat (the validator refuses `planner`). **All twelve settled; no seat died;
no residual call.** Role mix: executor 3 (R93E1 `reproduced-12/12`, R93E2 `no-regression`,
R93E3 `reproduced`), scribe 1 (R93SC1 `drafted`), scout 2 (R93S1 `agree`, R93S2
`premise-holds`), reviewer 2 (R93R1 `findings:5`, R93R2 `conforms-with-findings`), critic 1
(R93C1 `survives` over 13 counter runs), mutation-tester 1 (R93M1 `killed:17/24`, 6
inconclusive), sentinel 1 (R93SN1 `findings:10`), connector 1 (R93CN1 `no-overlap`).
Results: `.ufo/waves/round-93/r93-w1-results.json`.

What the wave did to the round: it did **not** kill either claim. It killed three sentences of
the record and one of C2's, each narrowed before filing in `plans/round-93.plan.md`:

- **A1** — `coverage` is fence-blind: a fenced `corpus/README.md` row naming the note is keyed,
  contradicting the plan's blanket "a fenced block is literal text" limit (R93R1 finding 2,
  `R93R1-probe4.py`).
- **A2** — the width rules are stricter than GFM and unstated: the delimiter row's cell count
  is never checked (the guard compares the header to the first data row) and any data row of
  non-header width refuses, though S321 gives remainder rows pad/truncate semantics (R93R1
  finding 1, R93C1 finding 1, R93S1 observation, R93M1 §4.7).
- **A3** — the seal is self-referential: one lane commit repointing `census-mutants.json` and
  regenerating `pins.json` makes the counter execute a **foreign gate** while printing
  `pin=true pins=true green=true canary=true` (`R93SN1-probe18.log`). The certificate is
  revision-bound, and the record now says so.
- **A4** — C2's "names the seal" test is a substring match: a mechanism-worded
  all-unfalsifiable manifest prints `findings=0`
  (`pre-freeze/c2-cheat-all-unfalsifiable.out`); the frozen counts and kill rule (b) reject it.
- **A5/A6** — C2's `canary` reason is scoped to the frozen spec; record corrections F1-F5 from
  R93R2; M1's rule-level gap recorded.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Instrument rev A: counter, spec copy, pin generator, S321/S322 snapshots, lesson Gate, note + README status blocks | `LOG.md` `## Round 93` | `9cad4f6e` |
| `pins.json` derived from git objects (round-92 M5) | same | `90ec4b33` |
| S320 `used-by` gains the round-93 lesson (QUALITY 157 linkage) + registry-change log | same | `14021be1` |
| Battery driver (35 controls; M4 receipt guard, M1 missing-receipt row) | same | `b34c929e`, `69d377a0` |
| Counter simplified to one stray-verdict rule (M2) | same | `855f0c1c` |
| C2 instruments: checker + 19-row manifest | same | `9bf52b03` |
| `hardening-lint` defence list curated to the successor forms | same | `7626412` |
| Freeze: plan + claims + 35/35 receipts + first-run receipts + C2 controls + wave spec/dispatch | same | `978f04bc` |
| Pre-scoring wording fix (23, not 25, hostile states — M3) | same | `4643b6ff` |
| C2 control: the mechanism-worded all-unfalsifiable cheat | same | `d5bcf1db` |
| `tools/registry.json` row 86 for the C2 tool | same | `4e5515b2` |
| Records: plan A1-A6, lesson M1-M10 + measurements + routed items, QUALITY 159-162, LOG, SCORECARD (capability row), README map row, `claim-falsification.tsv`, wave artifacts + results | same | `d817ffcd` |
| Landing receipts (C1 + C2 at the landing revision) | same | `848412ee` |

## Before → after measurements

**R93-C1.** Counting command (frozen):

```
python3 -I .ufo/evidence/round-93/c1/measure-v93.py --repo . --rev <REV> --work <empty dir>
```

- Before, base `4a7e259b`: `C1_SETUP spec-absent-at-rev`, exit 2 —
  `.ufo/evidence/round-93/pre-freeze/controls/nowork-base.out`.
- After, instrument `855f0c1c` and landing `848412ee` (measured at `d817ffcd`):
  `C1_R93_PASS=true`, exit 0, `n=12 killed=5 survived=7 mismatched=0 badrows=0
  verdict_tables=1`, all 19 conjuncts true —
  `.ufo/evidence/round-93/landing/measure-at-landing.txt`.
- Battery (frozen):

```
python3 -I .ufo/evidence/round-93/c1/controls-v93.py --lane . --rev 855f0c1c \
  --base 4a7e259b --work <empty dir> --outdir <dir> --jobs 6
```

→ `C1_CONTROLS states=35 matched=35 mismatches=0 missing=0`, exit 0
(`.ufo/evidence/round-93/pre-freeze/controls/C1-summary.txt`), reproduced byte-identically
from committed bytes twice into one outdir by **R93E3** (`reproduced`, 35 `.rerun-1.out`
files, no existing receipt rewritten).

**R93-C2.** Counting command (frozen):

```
python3 -I tools/conjunct-disposition.py --lane . --rev <REV>     # and --selftest
```

- Before, base `4a7e259b`: `DISPOSITION_SETUP counter-absent-at-rev`, exit 2 —
  `.ufo/evidence/round-93/pre-freeze/c2-nowork-base.out`.
- After, landing `848412ee` (measured at `d817ffcd`): `rows=19 falsifiable=17
  unfalsifiable=2 findings=0`, exit 0 —
  `.ufo/evidence/round-93/landing/c2-at-landing.out`; `--selftest` → `6/6 pass`.
- Do-nothing control that skips the work: a committed manifest of 19 mechanism-worded
  `unfalsifiable` rows prints `rows=19 falsifiable=0 unfalsifiable=19 findings=0`, exit 0
  (`.ufo/evidence/round-93/pre-freeze/c2-cheat-all-unfalsifiable.out`) — the frozen counts and
  kill rule (b), not `findings`, are what reject it (A4).

Verdicts: **C1 verified, wording narrowed by A1-A3** (the twelve cells and the 23 named states
hold; the three narrowed sentences were wider than the instrument). **C2 verified at conjunct
granularity**; rule-level falsifiability is incomplete and stated (A6, M8). No axis harmed:
the standing sweeps are byte-identical at base and landing (`R93E2` `no-regression`:
`SELFSTATE rows=26 match=24 stale=2`, `RECEIPT_BIND receipts=12 bound=4 corrected=8 unbound=0`,
`POINTER_RECHECK rows=12 met=12`, `WAVE_RECONCILE rows=6 met=6`, `REGISTRY_CHECK held=74/78`
with the same four pre-existing `differs` rows).

## Sources & frontier

`SOURCES.md` rows **180 → 182**, counting command (frozen in `CORPUS.md`):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

- Round start (at `4a7e259b`): 180 rows, exit 0 (21 pre-existing W04 duplicate-URL warnings).
- Round end (at `d817ffcd`): 182 rows, `tameshi ok …/corpus/SOURCES.md`, exit 0, the same
  warning set.
- Rows added by tier: **A 2** (S321 GFM tables, S322 CommonMark fenced blocks), B 0, C 0.
- Rows touched old→new: S320 `used-by` `round-92.md, knowledge/…census.md` → `round-92.md,
  round-93.md, knowledge/…census.md` (status, tier and recheck unchanged), logged in the
  lesson's `## Registry changes logged this round`.
- Frontier rows advanced: F1/F2 untouched; the round's ground is the **reader** (a verification
  instrument), not a new frontier ground. No `knowledge/` entry enters, so no coverage-map row
  beyond the status row appended to `corpus/README.md`.
- Assimilation: none (see *Work performed*).

## Trend verdicts

- **expansion: unchanged.** Two sourced rows (S321, S322) and one instrument pair
  (reader + disposition checker) entered; no `knowledge/` entry and no frontier ground moved to
  Core. A source row is not expansion on its own (AXES.md: expansion ↔ coverage + adjacency).
- **quality: improved.** The lane now holds a reader that refuses on verdict content instead
  of id shape (QUALITY 154-155 implemented and both directions controlled: `pos-honest-a13`,
  `pos-honest-verdict-cell` against `hidden-c001`, `renamed-result`, `pseudo-row`), a
  documentation-linkage rule that rejects a denying README row (QUALITY 157), four new criteria
  (159-162) each with a receipt that can fail, and a curated lint whose sibling instrument still
  reads 5/8. Evidence: `C1_CONTROLS states=35 matched=35`; `pre-freeze/controls-firstrun/`
  keeps the first run's 34/35 as the record of what the controls caught.
- **discernment: improved.** The round's own wave falsified four sentences of its own record
  before filing (A1-A4), the lane narrowed each to what its instruments enforce, and it filed
  two HIGH instrument defects (A3's self-referential seal, M9's receipt-guard holes) rather
  than reporting them as passes. Calibration score stays 8: conjunct-level falsifiability is
  complete, rule-level is not, and the row says which one it is.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  lane assertion, unchanged this round; pointers unchanged (`reports/round-1-calibration.md#box-1`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — v1 wave `r93-w1`
  (12 seats, one instrument pair) under `LOG.md` `## Round 93`; no independent promotion verifier.
- [~] Instructions executable by an agent without oral context — plan + dispatch + receipts
  resolve from committed bytes (`R93E3` reproduced the battery from committed bytes alone);
  input-keyed monitor only, no independent promotion verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round read one fleet gate
  read-only and one sibling scan reported `no-overlap` (`R93CN1`); no sibling artifact edited;
  lane assertion.

**Stale-lane:** respawn-per-round driver; this is one steered round, no other mission of this
lane is open.

**Tool installs:** none (no pacman, no uv/npm/cargo). `hardening-lint`, the runner and the
registry are the lane's own tools.

**L0:** no new question; nothing blocked. (Carried, unresolved: the tsukuroi-r86 UKI incident
on the L0 file is not this lane's.)

**Pre-file falsification gate:**

```
python3 scripts/hyaku/prefile-falsification.py --lane tameshi --round 93 --wave r93-w1
PREFILE-FALSIFICATION: pass claims=2 rows=13 attack_seats=6 findings=0      (exit 0)
```

Ledger `.ufo/waves/round-93/claim-falsification.tsv`: 13 rows, both claim ids, all six attack
seats (R93R1, R93R2, R93C1, R93M1, R93SN1, R93CN1) present for each claim; four
`falsifies-wording` rows each naming its plan amendment (A1, A2, A3, A4), the rest `neutral`
with the reason.
