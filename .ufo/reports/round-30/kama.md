# kama — round 30 report

Lane: `kama-shokunin` (local model serving & endpoint health). Round 30, attempt 1, steered by the
hyaku run-5 orchestrator. Base `2aa46e24`; freeze `fdf8cda1`; landing tip `026eede9` (final receipt
commit follows the same files only). Assigned axes per `../shokunin.conf`: operability + calibration.
Preregistration: `kama-shokunin/.ufo/waves/round-30/preregistration.json`.

## Work performed

Declared claims: **C1 (calibration, measured)** — the round-29 self-assessment census over its
declared recall population; **C2 (operability, capability acquisition)** — `instrument-agreement`,
a lane tool that measures instrument reproducibility across runs.

- **C1 freeze before any seat** — counter `.ufo/waves/round-30/count-c1.py` (sha256
  `c3f16ef1…9ce40d`), preregistration, base receipt and census start at `fdf8cda1`; the base run
  reads `statements 141 extracted 69 oracle 72 bound 72 unbound 0 mismatched_at_base 13 …
  unresolved 13 met False` (`c1/before/c1-base.out`). The rows-only arm at the round-29 tip reads
  `valid_corrections 11 unresolved 2 met False` (`c1/before/c1-r29-tip.json`).
- **Pre-data control call** — 14 seats (executor 7, mutation-tester 7), receipts committed at
  `14bb1a32` before any correction row: no shortcut meets the target
  (`controls/SUMMARY.md`). Highlights: `CtlNoOracle` fails three conjuncts (`oracle 32 … mismatched
  12 unresolved 1`), `CtlPasteHolds` is refused by the mismatch count (`mismatched 11`), `CtlAllQ`
  is charged 42 false rows, `CtlDuplicate` revokes the original row (`valid 11 unresolved 4`),
  `CtlBaseTree` shows evidence-at-base silently under-counts (13 → 12), `CtlTamper` proves the
  replacement-object shield load-bearing and the frozen 13-count independently blocking. The
  reference policy (`RefInstrument`) meets by design.
- **C1 data** — two appended correction rows under `## Round 30 — self-assessment corrections`
  (`SCORECARD.md`, `4d498001`): `SA30:SCORECARD.md:Q:4a6f7c911e:o0` (line 41 `file=yes`, W
  `ea72c3ea`) and `SA30:SCORECARD.md:Q:422b431349:o0` (line 901 `declared2048 = captured
  training2048`, W `92b14625`), both observed `q:no-artifact`.
- **C1 measurement** — fresh clone, `.ufo/waves/round-30/final/c1-tip.json`/`.out`: `statements 141
  extracted 69 oracle 72 bound 72 unbound 0 mismatched_at_base 13 append_only True
  valid_corrections 13 false_corrections 0 unresolved 0 met True tip 026eede9f46a`.
- **C2 instrument** — `tools/instrument-agreement.py` written and committed at `1d3e8ba4`; selftest
  `IA_SELFTEST pass=4 fail=0` exit 0 with arms deterministic / nondeterministic (`agree=2
  disagree=1`) / declared-volatile / exit-only (`agree=2 disagree=1`)
  (`.ufo/waves/round-30/c2/selftest.out`). Receipts: `receipt-a.json` (`error-verdict-census.py
  --json`, `IA runs=3 agree=3 disagree=0`, digest `24ce96bc3905`), `receipt-b.json`
  (`sources-append-only.py --from 2aa46e24 --to 52ac3af --json`, `agree=3`, digest `db4c39bbbdfd`).
- **Frontier step** — SOURCES rows S178/S179 opened this round (sibling own-work, tier A), knowledge
  entry `corpus/knowledge/instrument-run-agreement.md` (provenance trio; S178/S179 cited), QUALITY
  KQ40 (a census population declares its recall gap), README coverage row, PROVINCE frontier→core
  note, lesson `corpus/lessons/round-30.md` with `## Gate` and `## Mistakes`.
- **Round-29 spot-check repairs** — item 1 already committed at `40b122d` (verified tracked, no new
  write); item 2 LOG hash-naming note (`LOG.md` §Round 30 names `6de225c2`, `227dd1ee`); items 3–4
  appended decision-record corrections in `SOURCES.md` §Round-30 source correction; item 5 appended
  the `corpus/lessons/round-2.md:49` location in `SCORECARD.md` §Round 30.
- **Deviation from plan, disclosed** — the round shape is one 64-seat v2 wave plus a 14-seat
  ordinary control call. At report time the wave had returned its registry only
  (`.ufo/waves/round-30/w1/out/swarm-registry.json`); seat reports land under
  `.ufo/waves/round-30/w1/out/<Seat>/` and are committed as they arrive. No wave seat's output is
  cited as evidence for a claim; the claims rest on the L1's own receipts and the control call.
  Dead seats: none — all 14 control arms returned (`CtlEditInPlace` late: `append_only False … unresolved 141 met False`); all 64 wave lanes spawned.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| C1 freeze: counter, preregistration, base + rows-only receipts, census start, three preliminary defect receipts | LOG §Round 30 | `fdf8cda1` |
| C2 tool + selftest + first receipt; v2 wave spec/taskCall/dispatch; control-call items and taskCall | LOG §Round 30 | `1d3e8ba4` |
| 14-arm pre-data control receipts + summary | LOG §Round 30 | `14bb1a32` |
| Two SA30 correction rows; S178/S179; KQ40; knowledge entry; README/PROVINCE; C2 receipts; LOG entry | LOG §Round 30 | `4d498001` |
| SCORECARD §Round 30 (claims, capability row, planned); lesson with seat findings | LOG §Round 30 | `026eede9` |
| Final C1 receipt at `026eede9`, census end, control summary corrections, lesson append | LOG §Round 30 | `d0e8c4c4` |

## Before → after measurements

**C1 (calibration).** Command:
`/usr/bin/python3 .ufo/waves/round-30/count-c1.py --repo <fresh clone> --tip <commit> --out <receipt>`.
- before, base `2aa46e24`: `statements 141 extracted 69 oracle 72 bound 72 unbound 0
  mismatched_at_base 13 … valid_corrections 0 … unresolved 13 met False` (`c1/before/c1-base.out`).
- before, round-29 tip `52ac3af` (rows-only): `valid_corrections 11 … unresolved 2 met False`
  (`c1/before/c1-r29-tip.json`).
- after, measured commit `026eede9f46abd4eeea204eb4262bbbb31a4facb`: `mismatched_at_base 13 …
  valid_corrections 13 false_corrections 0 unresolved 0 met True` (`final/c1-tip.out`).
Score: calibration 7 → 7; the author does not self-promote (closure rules). The command that shows
the surface unmoved is the same counter at base.

**C2 (capability).** Commands: `python3 tools/instrument-agreement.py --selftest` (exit 0,
`IA_SELFTEST pass=4 fail=0`) and `python3 tools/instrument-agreement.py --runs 3 --out <receipt> --
<instrument>`. Before: `git cat-file -e 2aa46e24:tools/instrument-agreement.py` exits 128 (tool
absent; no lane receipt existed). After, measured at `1d3e8ba4` (tool) and `4d498001` (receipts):
two receipts read `IA runs=3 agree=3 disagree=0` (`c2/receipt-a.json`, `c2/receipt-b.json`), and the
corpus guard's refusal receipt reads `agree=1 disagree=2`
(`c2/receipt-b-corpusguard-refused.json`). Operability 8 → 8; a capability row enters SCORECARD
(§capabilities, first-working round 30).

## Sources & frontier

Census before → after, command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kama`
(and `validate …`): start rows 177, exit 0; end rows 179, exit 0
(`.ufo/waves/round-30/census-start.out`, `census-end.out`, `census-validate-end.out`; the end run
reports `FLEET status.invalid 0`, `FLEET missing 0`).
- Rows added by tier: A +2 (S178, S179, both `own-work`), B +0, C +0. Statuses: both `mined`.
- Rows touched old→new: none (no `status`/`recheck`/`used-by` cell of an existing row changed); two
  appended decision-record corrections cover S174's verbatim label and S176's decision mismatch
  (`SOURCES.md` §Round-30 source correction).
- Frontier rows advanced: `corpus/knowledge/instrument-run-agreement.md` cites S178/S179 (cross-lane
  instrument transfer, with the boundary that kumitate owns counter mechanics and mori owns network
  re-fetch); the round-29 recall gap is now a pinned population with per-item checks (README
  §Round-30). K05 and registered-consumer reconciliation remain operator-runtime dependent.

## Trend verdicts

- **expansion: improved** — one net-new admitted knowledge entry on ground the coverage map did not
  hold (`corpus/knowledge/instrument-run-agreement.md`, source: S178/S179), two mined SOURCES rows,
  and one capability admitted to SCORECARD's table.
- **quality: improved** — KQ40 added; the corpus guard's path-dependent digest was refused as a
  measurement rather than normalized away; three instrument defects (oracle revision pin, sid
  collision, 64-char digest token) found and fixed with the failing receipts committed; the S174/S176
  source-record claims corrected by appended records.
- **discernment: unprovable-but-not-yet** — the 14-arm control call agrees with the gate on every
  shortcut (none meets) and the arms sharpened the reading (`unresolved == 0` alone is not
  load-bearing; `mismatched_at_base == 13` is). The outside non-author spot-check of this round's
  gate decisions does not exist yet; the lane reports discernment **unchanged** pending it.

## SHONEN

- [~] SKILL.md real decision tables/error patterns/checklists → author assertion; `SKILL.md`
  §§Decision table, Error signatures, Checklist; no named non-author verifier.
- [~] End-to-end domain task logged → `LOG.md` §Round 30 (C1 measurement at `026eede9`, C2 receipts);
  lane-owned instruments only, no registered consumer sampled; no non-author mark.
- [~] Instructions executable without oral context → `corpus/knowledge/instrument-run-agreement.md`
  §Run it; `.ufo/waves/round-30/preregistration.json` commands; independent execution review open.
- [~] No cross-domain bleed → `PROVINCE.md` round-30 note and `corpus/knowledge/internal` boundary
  lines in `instrument-run-agreement.md` §Cross-lane boundary; siblings' implementations not adopted.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (system `python3`, `git`; no network fetch this round).
