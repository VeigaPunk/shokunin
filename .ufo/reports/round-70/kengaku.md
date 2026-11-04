# kengaku — round 70 (hyaku run 15, attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/kengaku-shokunin` (branch `master`). Base `502893ad`
(round-69 verifier spot-check tip); freeze `384e9c76`; A2 `0ef40526`; landings `3fc7bd75`
(round) and `cf32a9c4` (receipts on the committed tip). Report committed on the fleet repo.

## Work performed

The round declared two claims, each a distinct axis with its own falsifiable before→after:
**R70-C1** — coverage, the lowest owned non-retired axis (L0-capped at 7): replay the
`nginx-request-logging` TB2 grader offline under a seven-case table re-frozen with the two red
witnesses round 69 lacked; **R70-C2** — calibration (held at its ceiling, exercised): close the
round-69 non-author closure's eight routed defects D1–D8 with a re-deriving gate. Claims doc
`plans/round-70-claims.md` (frozen `384e9c76`; Amendments A1–A4, each dated and
predicate-preserving).

- **Freeze with controls.** `plans/round-70-claims.md` carries both predicate sentences, the
  seven-case table, the frozen staged-input digests, the freeze-time leg arithmetic
  (`LEG-COVERAGE-FROZEN legs=8 seen_p=8 seen_f=8`, printed by `--render-table`), the kill rules,
  the do-nothing control (`.ufo/waves/round-70/c1-control.txt`: `SETUP receipt-missing`, rc 2 at
  base) and the C2 red-before (`.ufo/waves/round-70/c2-red-before.txt`: `DEFECTS n=8`, rc 1 at
  `502893ad`).
- **C1 instrument.** `plans/round70_c1_nginx_probe.py`: staged-input `case_sha256` over configs,
  web root, shim, grader and `run/bodies.json` (excluding the work path and the server-written
  log), a `PROBE_BLOB` binding to the committed blob, a re-hash of the lane's grader file,
  `--render-table --stage-sha`, and `--selftest` arms for path independence and byte sensitivity
  (`corpus/evidence/round70/nginx/selftest.txt`).
- **C1 battery of record.** `corpus/evidence/round70/nginx/receipt.txt` — seven `VECTOR …
  agree=True`, `LEG-COVERAGE legs=8 seen_p=8 seen_f=8`, `SUMMARY cases=7 legs=56 mismatches=0
  setup=0`, `PREDICATE R70-C1 pass`; checker on the landing tip `CHECK ok cases=7 legs=8
  seen_p=8 seen_f=8`, rc 0 (`corpus/evidence/round70/nginx/check.txt`, REV `3fc7bd75`); seven
  per-case sandbox captures. Two more batteries (`BatteryReplicate`) reproduce every vector and
  digest.
- **C1 landing.** `SKILL.md:78` class row `executed 2 of 8` → `executed 3 of 8`; the knowledge
  entry gained a round-70 addendum; `corpus/README.md`'s entry row and `PROVINCE.md`'s stale
  "nginx blocked on this host" clause corrected; `S242` (instruction file) added.
- **C2 instrument and corrections.** `plans/round70_c2_routed_defects.py` (E1–E8 over D1–D8,
  `--selftest`, `--mutants`). Corrections: depth-gate provenance labels + the single changed line
  (D1, `corpus/evidence/round70/c2/depth-gate-provenance.txt`), the new entry's trio receipt (D2,
  `corpus/evidence/round70/gates/trio-nginx.txt`), S242 (D3), S243 (D4), the round-69 lesson index
  row and block (D5), the round-69 gate's green run at `4038bb11` (D6,
  `corpus/evidence/round70/gates/r69-c2-landing.txt`), the lesson's Gate reject + S244 (D7), and
  the wave-validation receipts (D8).
- **C2 green.** `corpus/evidence/round70/c2-green.txt` — `E1..E8 ok`, `DEFECTS n=0`,
  `PREDICATE R70-C2 pass`, rc 0 on the landing tip (gate blob `367ce58e…`); controls
  `corpus/evidence/round70/c2-controls.txt` (`defects-in-fake=8 want=8 all-fail=True`;
  `E2 byte-flip red`; `MUTANTS total=8 killed=8`); the A4 red arm
  `corpus/evidence/round70/c2/a4-usedby-arm.txt` (both `used-by` clauses fire on blanked cells).
- **Wave shape.** One v1 wave, **14 seats** (band 8–16): executor 4 (`NginxBatteryR70`,
  `BatteryReplicate`, `LegWitnessProof`, `DepthGateRerun`), reviewer 3 (`ReceiptReview70`,
  `CaseTableAudit`, `DefectGateReverify`), critic 1 (`ClaimFalsify70`), mutation-tester 2
  (`CounterMutate70`, `GateMutate70`), scribe 2 (`CorrectionDraft-2`, `Lesson70Draft`), scout 1
  (`SourceOpen70`), connector 1 (`SiblingOverlap70`). Attack roles `{reviewer, critic,
  mutation-tester}` = 6/14 = **43 %** (≥25 %); connector 1 (≤2). **14 of 14 settled with output**
  (`.ufo/waves/round-70/w1-results.json`); **0 dead seats**; no residual call; round total **14**.
  The L1 held the canonical planner seat (the validator rejects `planner`); bounded planning
  data-walks rode the scout and critic items.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| freeze: claims doc, both instruments, wave spec + validated dispatch (`w1-validate.rc` = 0), census-before, C2 red-before, C1 control | `LOG.md` `## Round 70` bullet 1 | `384e9c76` |
| A2: duplicate-line defects in the C1 checker (ReceiptReview70 A-1) + v1 receipt preserved | `LOG.md` `## Round 70` bullet 2 | `0ef40526` |
| round landing: SKILL class row, entry addendum, SOURCES S242–S244, README/PROVINCE corrections, QUALITY Q52, lesson, SCORECARD, evidence, wave artifacts and `w1-results.json` | `LOG.md` `## Round 70` bullets 2–5 | `3fc7bd75` |
| receipts re-derived on the committed tip (gate blob `367ce58e…`, probe blob `9c9effeb…`) | `LOG.md` `## Round 70` verification bullet | `cf32a9c4` |

## Before → after measurements

| claim | before (base `502893ad`) | after (landing) | counting command | measured at |
|---|---|---|---|---|
| **R70-C1** | `git cat-file -e 502893ad:corpus/evidence/round70/nginx/receipt.txt` → rc 128; `grep -c 'executed 2 of 8' SKILL.md` → 1; `grep -cE '^\|[[:space:]]*S242[[:space:]]*\|' corpus/SOURCES.md` → 0 | `CHECK ok cases=7 legs=8 seen_p=8 seen_f=8` / `PREDICATE R70-C1 pass` / rc 0; `grep -c 'executed 3 of 8' SKILL.md` → 1 and `executed 2 of 8` → 0; seven `VECTOR … agree=True`; `LEG-COVERAGE legs=8 seen_p=8 seen_f=8` | `python3 plans/round70_c1_nginx_probe.py --check-receipt corpus/evidence/round70/nginx/receipt.txt`; the `grep -c` pairs; `--render-table` (`LEG-COVERAGE-FROZEN legs=8 seen_p=8 seen_f=8`) | receipt `corpus/evidence/round70/nginx/receipt.txt`; check `…/check.txt` at `3fc7bd75` |
| **R70-C2** | `python3 plans/round70_c2_routed_defects.py` → `DEFECTS n=8`, `PREDICATE R70-C2 fail`, rc 1 (`.ufo/waves/round-70/c2-red-before.txt`) | same command → `E1..E8 ok`, `DEFECTS n=0`, `PREDICATE R70-C2 pass`, rc 0; selftest 8/8; mutants 8/8 | the gate command; `--selftest --work <scratch>`; `--mutants --work <scratch>` | `corpus/evidence/round70/c2-green.txt`; `…/c2-controls.txt` at `3fc7bd75` |

## Sources & frontier

- **Census before → after.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
  --root /home/vgpnk/Projects/shokunin kengaku` → **exit 0 at round start** (233 data rows, 24
  W04 warnings, 0 E-codes; `.ufo/waves/round-70/census-before.txt`) and **exit 0 at round end**
  (236 data rows, 25 W04 warnings — the new one names S243's superseding row — 0 E-codes;
  `corpus/evidence/round70/census-after.txt`).
- **Rows added by tier.** tier A ×2 (S242, S243); tier C ×1 (S244, a kept rejection).
- **Rows touched old→new.** S241 unchanged (append-only; its misstated summary cell is superseded
  by S243, never edited). S242/S243/S244 are new; their `used-by` resolves to
  `corpus/knowledge/tb2-nginx-request-logging-offline.md`.
- **Frontier rows advanced.** `network-service` executed members 2 → 3 (`kv-store-grpc` round 64,
  `pypi-server` round 68, `nginx-request-logging` round 70); the class row carries the move and
  `corpus/README.md`'s coverage bullet names it.
- **Gate.** Three sourced decisions with ≥1 admit and ≥1 reject, reasons and flips recorded in
  `corpus/lessons/round-70.md` `## Gate`: S242 admit, S243 admit, S244 reject.
- **Assimilation: none** — one `merge/kengaku` entry (`grader-fixture-coverage`) was opened and
  refused: its triad is offset by a leading blank line (Q1), its cited `S155` resolves in this
  lane to a different source, and its runnable probe is not held here, so the tier-A `own-work`
  claim is not re-derivable (Q2); flip named. `considerthese/` exists (2026-10-19 … 2026-10-26);
  no still-unimplemented proposal was mined this round because the claim cap is consumed by the
  re-freeze and the eight routed defects — recorded, not hidden.

## Trend verdicts

- **expansion: improved** — the `network-service` class moves `executed 2 of 8` → `3 of 8` on a
  passing frozen predicate; two new tier-A rows are cited by the admitted entries.
- **quality: improved** — eight routed defects closed by a gate that moves `n=8` → `n=0` and is
  killed 8/8 under single-check deletion; Q52 enters with its lesson; the instrument's
  staged-digest and blob-binding defects are repaired with two-direction selftest arms.
- **discernment: unchanged** — no exploratory claim; eight self-caught or seat-found landing
  defects are lesson rows and named limitations, not self-attested improvement; the outside
  spot-check remains the non-author closure's duty.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `SKILL.md:78` class row moved with its evidence; depth gate `PREDICATE R63-C2 pass`
  (`ROWS n=16 class_match=True count_mismatch=0 paths total=34 resolved=34 share=1.00`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md`
  `## Round 70` (receipt, checker, three batteries, gate, census exits).
- [~] Instructions executable by an agent without oral context — pointer:
  `plans/round-70-claims.md` (commands, digests, kill rules) and the 14 seat reports under
  `.ufo/waves/round-70/w1/`, each run from its prompt alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` corrected (nginx
  no longer "blocked on this host"); `SiblingOverlap70` counted 48 term-level and 6 surface-level
  hits, none owned by a sibling, none absorbed.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.

**Tool installs/upgrades:** none this round (no `pacman`, `uv tool`, `npx` or binary install).

**Named limitations carried (not smoothed).** (i) `--check-receipt` re-derives text fields and
cannot prove a live run — `ClaimFalsify70` accepted a hand-written receipt with impossible
live-witness fields; the sandbox captures and `server_pid` lines are the live witness. (ii) The
`nginx` binary is a lane-written shim answering `-t`. (iii) K6's five reds are one grader
`AssertionError` and four `ConnectionError`s inside the grader's own requests; the receipt folds
exceptions into `F` (pytest-equivalent) and cannot distinguish them. (iv) K6's leg 4 red is a
connection red, not the body assertion; K7 is the only witness of `:53`. (v) R70-C2's checks are
largely token/structure presence: a wholly synthetic lane prints `DEFECTS n=0`
(`ClaimFalsify70`), so the gate prices this lane's corrections, not their provenance. (vi) The
class-row count (`executed 3 of 8`) is editorial in the row's wording, guarded by no instrument;
the counting commands are in the row's evidence. (vii) The shipped `--mutants` matrix generates
only single-entry deletion; `GateMutate70` shows an always-`True` check (H1/H3) or a
control-constant rewrite (H6) can survive it — named, matrix unchanged.
