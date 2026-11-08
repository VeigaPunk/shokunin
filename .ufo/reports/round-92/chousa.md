# chousa — round 92: the pins file is pinned like any other instrument; empty cells are not separators and the tally scope is an ATX boundary

## Work performed

Declares 3 claims on 3 axes (no exploratory claim). Round 91 was admitted, so this is not a fresh-start round.

- **C1 operability** — the C1 repairs the r91 spot-check routed: `emit` wired to refuse without an explicit
  `--receipts` (exit 2), a duplicate pin path refusing at exit 2 (`SETUP PIN_DUPLICATE` previously exit 1),
  `rel_for` refusing paths that escape `--root`, the pins file self-pinned by its minus-self digest, and every
  `.sh`/`.py` command token pinned. Evidence: `corpus/evidence/round92/after/c1-verify.txt` (`control-driver-r92.py`
  verify at `95bbbd0f`, `CONTROL_DRIVER_R92=PASS`, `COMMITTED_OK=6/6 EXACT_OK=6/6 PIN_OK=6/6 FRESH_OK=6/6`,
  `SELF_PIN OK rev=95bbbd0f receipts_rev=2a9d1773`), `corpus/evidence/round92/after/c1-forgeries.txt`
  (`FORGERY_REFUSED=3/3 POSITIVE=pass`), `corpus/evidence/round92/after/c1-procedure.txt`, and the wave reports
  `R92ExecC1Repro.md` §(c), `R92ExecMutations.md` M1–M3, `R92ReviewerC1.md` F1–F4, `R92SentinelScope.md` F2/F3/F4/F5.
  Source grounding S070 (installed `sha256sum(1)`, `93c17dffe9f25d56291113d566a7de3ff65c29f8cc32c381801c49cf27e8403f`,
  line 11, re-opened this round by `R92ScoutRegistry.md` and the sentinel, and by the lesson's Gate record) grounds
  the digest and self-pin rules.
- **C2 calibration** — the C2 repairs the r91 spot-check routed: an empty first cell is no longer skipped as a
  separator in either table (a quote row with a first-cell `""` now reaches QSHAPE), the structural header skip
  requires the literal `qid|source|quote` row, the decision count reads pipe-leading rows the table holds, and
  TFREQ's universe (rows whose named qids all resolve) is stated. Evidence:
  `corpus/evidence/round92/after/c2-counter.txt` (`CURATION_R92=PASS`, `LEGS_MEASURED=14/14`),
  `corpus/evidence/round92/after/c2-controls.txt` (`CONTROLS=PASS FORGERY_REFUSED=4/4 PRIOR_ACCEPTED=4/4`), the
  wave's `R92ExecC2Repro.md` §(c)(d), `R92ReviewerC2.md` F2/F3/F4 (wired) and F5/F6/F7 (narrowed), and
  `R92ExecMutations.md` M4/M5/M6/M8.
- **C3 freshness** — the C3 repairs the r91 spot-check routed: the tally scope stops at the next ATX heading of
  depth ≤ 2 at column 0 (`# ` or `## `) with a `SCOPE_BLEED` setup diagnostic on an unterminated scope, and the
  `^ok-case` enumeration is pinned against the verdict count (distinct numbers, six `accepted=` lines included).
  Evidence: `corpus/evidence/round92/after/c3-counter.txt` (`SKILL_TALLY_R92=PASS`, `TALLY_ROWS=8`,
  `OTHER_OCCURRENCES=2`, `OTHERS_OK=1 LEGS=3/3`),
  `corpus/evidence/round92/after/c3-controls.txt` (`CONTROLS=PASS OLDPROSE_REFUSED=1/1 PRIOR_ACCEPTED=1/1
  STALE_REFUSED_BOTH=1/1`), `R92ExecC3Repro.md` §(c)(d), `R92ReviewerC3.md` A1→Amendment 8 and A3→Amendment 9,
  `R92ConnectorSiblings.md` §5.
- **Frontier step (§2b)** — census run at round start and round end (both exit 0, 219 rows, five pre-existing
  `W04` warnings; the 215-tail tally is the out-of-section historical occurrence the C3 report names under its
  named limits). One mistake mined (see lesson §Mistakes, 10 classes) and C1's sourced claim rests on the S070
  re-open confirmed this round. Assimilation: none (no merge theme adopted, no considerthese proposal mined — the
  three claims are full).
- **Status of the two sentence ends to track:** the wave attacked the F5 freeze; the round now lands at F7/C8 after
  the F6 instrumentation edits (Amendments 1–9) and a C7/C8 receipt re-cut to drop the three unscored
  before-receipts from the scored directory. The measurements quoted above were taken at F6/C6; the F7/C8 pair
  itself was verified green before landing (`SELF_PIN OK rev=7901eb23 receipts_rev=9ab1dbec`,
  `CONTROL_DRIVER_R92=PASS`).

## Landed changes

- `corpus/evidence/round92/control-driver-r92.py` — C1 guards: `emit` requires explicit `--receipts` (exit 2),
  `read_pins` prints `SETUP PIN_DUPLICATE` to stdout and exits 2, `rel_for` refuses escapes, every `.sh`/`.py`
  command token is pinned, the pins file's minus-self self-pin (commits `95bbbd0f`, `b73a0dce`).
- `corpus/evidence/round92/forgeries-r92.py` — the 3-class battery asserts the new exit code for `PIN_DUPLICATE`
  (commit `95bbbd0f`).
- `corpus/evidence/round92/curation-r92.py` — `_is_separator` (non-empty cells only), first-line structural header
  as the literal `qid|source|quote` row, device-count decision rows (commit `95bbbd0f`).
- `corpus/evidence/round92/curation-controls-r92.py` — 4 S-classes + r90-battery replay (commit `95bbbd0f`).
- `corpus/evidence/round92/skill-tally-r92.py` — ATX depth-≤2 scope boundary with `SCOPE_BLEED`, `^ok-case`
  enumeration pinned (commit `95bbbd0f`).
- `corpus/evidence/round92/skill-tally-r92-controls.py`, `controls/expected.tsv` (carried from F1), `controls/selftest-r92.txt`,
  `instrument-pins.txt` (16 rows, minus-self self-pin), `claims.md`/`claims.json` (Amendment 1 filename
  correction + narrowings, Amendments 2–9 in `plans/round-92.md`), `controls/receipts/` (six scored receipts),
  `evidence-before/` (three do-nothing-control before receipts, outside the scored directory) — frozen at
  `95bbbd0f`/`2a9d1773`, re-cut `9ab1dbec`/`692acef3`.
- `corpus/lessons/round-92.md` — the round lesson (Gate, claim outcomes, ten mistakes, spot-check intake, wave
  settlement, trends, routed work; commit `d379a535`).
- `SCORECARD.md`, `LOG.md`, `corpus/QUALITY.md` (criteria 211–216), `corpus/evidence/round92/after/*`,
  `census-start.txt`/`census-end.txt` — commit `d379a535`.
- `.ufo/waves/round-92/` — build spec, spec, validated dispatch, 12 seat reports and receipts, results,
  24-row `claim-falsification.tsv` — commit `a900b2ef`.

## Before → after measurements

- **C1.** Before (round-91 driver): `emit` without `--receipts` exited 0 and overwrote the committed receipts in
  the tree; a duplicated pin path raised `SystemExit` with exit 1; `read_pins` last-wins; `instrument_rel` first
  token only; the pins file absent from the pin set; `rel_for` escapes unguarded (`R92ReviewerC1.md` F1–F4,
  `R92SentinelScope.md` F2–F5). Counting command:
  `python3 -B corpus/evidence/round92/control-driver-r92.py verify --root . --repo . --rev F --receipts-rev C --work <scratch>`:
  before (at the pre-fix tree run by R92ExecC1Repro) the driver's own self-run prints `CONTROL_DRIVER_R92=FAIL`;
  after (at freeze `95bbbd0f`, carrier `2a9d1773`, and re-verified at `7901eb23`/`9ab1dbec`):
  `CONTROL_DRIVER_R92=PASS` with `COMMITTED_OK=6/6 EXACT_OK=6/6 PIN_OK=6/6 FRESH_OK=6/6` and
  `SELF_PIN OK rev=95bbbd0f receipts_rev=2a9d1773` (receipts: `corpus/evidence/round92/after/c1-verify.txt`,
  measured at `95bbbd0f`); plus `FORGERY_REFUSED=3/3 POSITIVE=pass` from
  `python3 -B corpus/evidence/round92/forgeries-r92.py --work <scratch>` (receipt
  `corpus/evidence/round92/after/c1-forgeries.txt`).
- **C2.** Before (round-91 counter): `CURATION_R91=PASS` (`LEGS_MEASURED=13/13`) on all four S forged trees
  (`PRIOR_ACCEPTED=4/4`, measured by the r92 battery and by `R92RevPrior.md` independently). After:
  `python3 -B corpus/evidence/round92/curation-r92.py --root .` → `CURATION_R92=PASS` with
  `LEGS_MEASURED=14/14 Q_ROWS=20 Q_SHAPE_FAIL=0 SOURCE_STATUS_OK=20/20 USED_BY_OK=20/20 TFREQ_OK=17/17
  TFREQ_MAX_DF=3 UNENTAILED_TERM=0 WARRANT_OK=17/17 DUP_QIDS=0` (receipt `corpus/evidence/round92/after/c2-counter.txt`,
  measured at landing `60f81ecf` with `CURATION_R92=PASS` exit 0) and
  `CONTROLS=PASS FORGERY_REFUSED=4/4 PRIOR_ACCEPTED=4/4 DUPCOUNT_R91=1 DUPCOUNT_R92=1` with `PRIOR_REGRESSION=4/4`
  on the summary line and `FORGERY_REFUSED=7/7 PRIOR_REGRESSION=7/7` on the regression line (receipt
  `corpus/evidence/round92/after/c2-controls.txt`, measured at `95bbbd0f`).
- **C3.** Before (round-91 counter): `SKILL_TALLY_R91=PASS` (`TALLY_ROWS=9 STALE_TALLIES=0/9 OTHER_OCCURRENCES=3
  LEGS=2/2`) on the deleted-161 tree, document-wide and unpinned (`controls/receipts/c3-before.txt` is the emitted
  before receipt — see the evidence-before corpus). After: `python3 -B corpus/evidence/round92/skill-tally-r92.py
  --root . --selftest corpus/evidence/round92/controls/selftest-r92.txt` → `SKILL_TALLY_R92=PASS` with
  `TALLY_ROWS=8 STALE_TALLIES=0/8 EXPECTED_CASES=283 EXPECTED_SKIPPED=0 OTHER_OCCURRENCES=2 CASE_RANGE_BASHENV=273-275
  CASE_RANGE_BASH_PIN=282-283 CASE_RANGE_OK=2/2 MISLABELED=0 OTHERS_OK=1 LEGS=3/3` (receipt
  `corpus/evidence/round92/after/c3-counter.txt`, measured at `95bbbd0f` and re-verified at landing
  `60f81ecf` — identical) and `python3 -B corpus/evidence/round92/skill-tally-r92-controls.py --root . --work
  <scratch>` → `CONTROLS=PASS OLDPROSE_REFUSED=1/1 PRIOR_ACCEPTED=1/1 STALE_REFUSED_BOTH=1/1` (receipt
  `corpus/evidence/round92/after/c3-controls.txt`).

## Sources & frontier

Assimilation: none (no `merge/chousa/` theme adopted, no `considerthese/` proposal mined — the three claims are
full). `SOURCES: unchanged —` registry 219 → 219 rows; census start exit 0 (219 rows, five pre-existing `W04`
warnings) and census end exit 0 (219 rows, same five `W04` warnings). The 215-tail tally `PASS (215 cases, 0
skipped)` at `SKILL.md:640` (outside `## Gates`, after `## Round26`) is deliberately out of scope and counted as
another omitted occurrence — it is not a touched row. No frontier row advanced; the S070 (installed `sha256sum(1)`,
sha re-verified identical) and S001 rows were re-opened with their status unchanged and with Gate records in
`corpus/lessons/round-92.md` (S070 in prose + locate note; S001 in rev form). QUALITY criteria 211–216 mined.

## Trend verdicts

- **expansion: unchanged** — registry 219 → 219 rows; no new `corpus/knowledge/` entry; the source work is two
  re-opens (S070 with sha re-verified identical, S001 with a rev-form Gate record) and no fetch.
- **quality: improved** — three instruments re-frozen with guards ordered by ten falsification artifacts; the
  mutation battery killed 9/9 mutants with one surviving rename-only control proving detection is behavioural,
  and every repaired class carries a red-before witness (the r91-mechanism attestation for C1, the r91 counter
  PASS on all four S trees for C2, the r91 `PASS` on the deleted-161 tree for C3).
- **discernment: improved** — the freeze was cut eight times (F1–F8) before any settled scoring, every superseded
  pair named in `plans/round-92.md`; the wave's nine amendments were published before filing as narrowings or
  wired guards instead of filing the wider sentences; the `PRIOR_REGRESSION=4/4` summary token, the
  missing-before-receipts sentence and the S070 record shape were named rather than smoothed over.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  `SKILL.md` Gates table (lane assertion, verified by `corpus/evidence/round92/skill-tally-r92.py` re-running its tallies; no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  `LOG.md` Round 92 entry; `corpus/evidence/round92/after/` receipts (lane assertion)
- [~] Instructions executable by an agent without oral context
  `bash tools/research-gate.sh --selftest` (283 cases, receipt `corpus/evidence/round92/controls/selftest-r92.txt`); `python3 tools/gate-records.py verify --root . --repo . corpus/lessons/round-92.md` (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  `PROVINCE.md`; `R92ConnectorSiblings.md` §4 (lane assertion)

## Prefile falsification

`python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane chousa --round 92` → exit 0,
`PREFILE-FALSIFICATION: pass claims=3 rows=24 attack_seats=8 findings=0` (10 `falsifies-wording` rows, each naming
its `plans/round-92.md` amendment; 8 `neutral` rows).

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Installed tooling: none.
