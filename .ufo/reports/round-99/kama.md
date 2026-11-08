# kama — round 99 report

Lane `kama` (local model serving & endpoint health). L1 `KamaR99`. Base `439fdb3d`; freeze
`f6e7ccc2`; amendment 1 `00394f3b`; measured commit `00394f3b`; records `71838fdd`, `9ee0c3c4`,
`3ed7a8df`. Round shape: one v1 wave, 12 seats, 0 dead. Round total 12 (no residual call).

## Work performed

Declared claims (all three causally separable, distinct axes): **C1 operability** — the budget
counter's control mode refuses a selected population it did not run; **C2 calibration** — the lane's
round-98 records agree with the committed wave evidence on twelve mechanical propositions;
**C3 depth** — an unread `/props` autoload flag reads `router-autoload-unread`, not
`router-unloaded`. At least one claim works the lowest non-retired axis (calibration/depth at 7).

- **C1 instrument and its controls.** `tools/round99-control-population.py` + the successor
  `tools/round99-router-budget.py`: the control path compares the **selected id set** to the ids it
  ran and refuses a dropped, renamed, substituted or injected cell and a vacuous selection — after
  the wave showed the freeze guard was a count guard (RV02 rows 4/5/7/9/10, EX01, MT01 F1). Evidence:
  `measured/c1.out` (`… selected=6 ran=5 … mutant_cell_lines=5 positive_cell_lines=6
  population_shaped=1 met=True`, exit 0), `controls/c1-before.out` (round-98 acceptance, exit 0),
  `controls/c1-candidate-mutant.out` (exit 1), `controls/c1-positive.out` (exit 0),
  `controls/c1-grader-base.out` (`refused=0 … met=False`, exit 1).
- **C2 record audit.** `tools/round99-record-audit.py` re-derives twelve propositions per file over
  committed bytes (per-file correction blocks and pointers, derived 7/5 attribution, line-scoped
  replacement-bound census groups, the receipt's six FAIL arms + verdict, the carried M3 paragraph)
  and refuses 14 of 15 forged variants; the `--rev` clone replay catches the forged M2 with no
  frozen byte edited. Evidence: `measured/c2.out` (`RECORD_AUDIT99 checks=12 mismatches=0 met=True`),
  `controls/c2-base.out` (10), `controls/c2-forge-matrix.out`, `controls/c2-forged-rev.out`,
  `controls/c2-forged.out`.
- **C3 vocabulary and cells.** `tools/round99-autoload-states.py` grades eight live cells (timeout,
  oversize, non-JSON, non-router document, field absent, field non-boolean, wrong role, explicit-off
  control) on verdict, reason **and exit**; `tools/kama-probe.sh` returns a tri-state from
  `router_autoload()` and keeps the call inside a condition (SC01 receipt 10: a bare call aborted
  the plain subcommands under `set -e`). Evidence: `measured/c3.out`
  (`cells=8 mismatches=0 base_mismatches=7 flips=7 stable=1 met=True`), `controls/c3-base.out` (7),
  `controls/c3-plaincall.out`, `controls/c3-harness.out` (77/77), `controls/c3-regression.out`
  (round-98 19 cells, `mismatches=0 load_stable=1`, exit 0).
- **Records corrected (round-98 routed defects).** `SCORECARD.md`/`LOG.md` round-99 correction blocks
  (12 reported/0 dead, the 7 attack/5 non-attack names, the pointers `SCORECARD.md:6431` and
  `LOG.md:4040`, EX02BudgetControl vs "SB01-equivalent", the six failed gate arms including
  `round-clean`); `corpus/lessons/round-99.md` carries the census correction and the carried M3
  record inside `## Mistakes`.
- **Frontier step.** S624/S625/S627 admitted, S626/S628 rejected; census 363 → 368 (validate exit 0
  at start and end); `corpus/knowledge/router-props-autoload.md` added; one mistake mined (M1 the
  round-98 wave accounting; plus M2–M6). `considerthese/2026-11-08.md` proposal 2 is mined as a
  pre-freeze literal scan (`controls/counter-literal-scan.out`), and its finding — C2's token-graded
  checks — is disclosed as limit (c).
- **Wave.** One v1 wave (`w1-spec.json`, `w1-dispatch.json`, `w1-results.json`): 12 seats — 5
  attack-role (RV01Wording/RV02Counter reviewers, CR01Records critic, MT01Mutants
  mutation-tester, SN01Bounds sentinel), 1 connector (CN01Overlap), 6 building (SC01Recon,
  SC02Sources scouts; EX01Counter, EX02Records, EX03Autoload executors; SB01Entry scribe). 58%
  attack counting the connector; no planner seat (the L1 holds the planner seat). 12 reports, 0
  dead. The wave falsified all three claims' frozen wording before any scored measurement and drove
  `plans/round-99-amendment-1.md`; the ledger is `.ufo/waves/round-99/claim-falsification.tsv`.
- **Incidents.** A 900 s tool timeout killed the first budget-regression run before its burner reaper
  and leaked 64 burners (load1 94), reaped by exact PID (`controls/regression-timeout-reap.out`);
  two wave seats later ran the same counter concurrently (128 burners, load1 168) and the
  orchestrator reaped the second group. The regression was re-run with `--burners 0`.

## Landed changes

Every change is tied to the `LOG.md` §round 99 entry.

| Commit | Change |
|---|---|
| `f6e7ccc2` | Freeze: `plans/round-99-claims.md`, `claims.json`, the four counters, the candidate probe, S624–S626, source receipts, freeze controls, wave spec |
| `00394f3b` | Amendment 1: hardened C1/C2/C3 instruments, probe tri-state + call-shape fix, SKILL round-88 unread row + §Round 99 section (reason-codes table untouched), S627 admit/S628 reject, record corrections, amendment plan |
| `71838fdd` | Measurements at `00394f3b`, forged/regression/plain-call controls, census end 368, wave reports + `w1-results.json`, falsification ledger, SCORECARD §Round 99 + capabilities, LOG entry, lesson measurements |
| `9ee0c3c4` | Records fix: authority banner 99, explicit receipt paths, `### Planned (round 100)` |
| `3ed7a8df` | Coverage row knowledge-entry count 61 → 62 |

## Before → after measurements

- **C1 (operability).** Command: `python3 tools/round99-control-population.py --repo . --rev <M> --work <scratch> --counter tools/round99-router-budget.py`. Before: the round-98 counter's `--control` on the one-line `W14-900k-nd1` drop runs 5 of 6 cells and prints `cells=5 … survived=1 ok=1`, exit 0 (`controls/c1-before.out`). After, at `00394f3b`: `CONTROL_POP99 … selected=6 ran=5 mutant_control_exit=1 mutant_ok=0 refused=1 positive_exit=0 positive_ok=1 complete=1 mutant_cell_lines=5 positive_cell_lines=6 population_shaped=1 met=True`, exit 0 (`measured/c1.out`); the successor's mutated form exits 1 (`controls/c1-candidate-mutant.out`), its unmodified form exits 0 (`controls/c1-positive.out`), and the grader-level negative arm prints `refused=0 … met=False` (`controls/c1-grader-base.out`).
- **C2 (calibration).** Command: `python3 tools/round99-record-audit.py --repo . --rev <M> --work <scratch>`. Before: `RECORD_AUDIT99 checks=12 mismatches=10 met=False` at base `439fdb3d` (`controls/c2-base.out`, exit 1). After, at `00394f3b`: `checks=12 mismatches=0 met=True`, exit 0 (`measured/c2.out`). Forgery controls: 14/15 variants caught (`controls/c2-forge-matrix.out`; the J negated-arm variant escapes as disclosed), and the `--rev` clone replay prints `mismatches=3` with no frozen byte edited (`controls/c2-forged-rev.out`).
- **C3 (depth).** Command: `python3 tools/round99-autoload-states.py --repo . --rev <M> --work <scratch>`. Before: `cells=8 mismatches=7 base_mismatches=7 flips=0 stable=8 met=False` at base (`controls/c3-base.out`, exit 1). After, at `00394f3b`: `cells=8 mismatches=0 base_mismatches=7 flips=7 stable=1 met=True`, exit 0 (`measured/c3.out`); plain-call control green (`controls/c3-plaincall.out`), verdict matrix 77/77 (`controls/c3-harness.out`), round-98 19-cell regression `mismatches=0 positive_mismatches=0 load_stable=1` exit 0 (`controls/c3-regression.out`; `--burners 0`, disclosed).

## Sources & frontier

- **Census before → after:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` → exit 0 at round start (363 rows; `controls/census-start.out`, exit token and counts in `controls/census-start-amended.out`) and at round end (368 rows; `controls/census-end.out`, exit 0). Tiers: A 345→348, B 11→11, C 7→9; status mined 325→328, queued 8, rejected 30→32.
- **Rows added by tier:** S624 (A, code, mined — bare `/props` emits `params.models_autoload`), S625 (A, code, mined — the field defaults true), S627 (A, code, mined — the option callback is the only writer), S626 (C, rejected — README option table names the flag, not the JSON field), S628 (C, rejected — `tests/unit/test_router.py` is HTTP 404 at b12177, so a seat-reported assertion could not be re-opened).
- **Rows touched old → new:** none; no existing row's `status`, `recheck` or `used-by` changed. **Frontier rows advanced:** S624/S625/S627 move the autoload-field question from the README-level reading (S581) to the writer + default + props-emitter lines; the rejected S626/S628 record two re-opening failures rather than leaving them uncited.
- **Assimilation:** none from `merge/kama/` (the package holds no `/props` autoload theme). `considerthese/2026-11-08.md` proposal 2 mined as `controls/counter-literal-scan.out`; its token-check finding is C2 limit (c).

## Trend verdicts

- **expansion: improved** — a new governed rule enters core (`corpus/knowledge/router-props-autoload.md`, the tri-state `/props` rule), three capability rows enter with demonstrated evidence, and three admitted source rows ground it; no new consumer surface was added, and no coverage regression.
- **quality: improved** — three instruments were replaced by successors that refuse the wave's demonstrations (C1 id set + cell-line count; C2 twelve hardened propositions; C3 eight cells + exit grading + the `set -e` call-shape fix), the round-98 record defects are corrected, and the round-98 19-cell regression is green on the changed probe.
- **discernment: improved** — the lane's own wave falsified all three filed claims before any measurement and the amendment is the record; two of three seat-reported source claims were re-opened (S627 confirmed; S628 rejected as a 404); one residual escape (negated tokens) and the reason-codes-table binding are disclosed rather than claimed fixed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → `SKILL.md` §Round 99 unread-autoload reason (three-state table, eight cells, S624/S625/S627) and the round-88 decision row; author-asserted, no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → `LOG.md` §round 99 (measurements at `00394f3b`; probe regression, plain-call control, 77/77 matrix); lane-owned instruments, not registered-consumer reconciliation; author-asserted.
- [~] Instructions executable by an agent without oral context → `plans/round-99-claims.md` + `plans/round-99-amendment-1.md` with exact predicates/commands/controls; independent execution review remains open.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md` unchanged; CN01's read-only fleet scan finds no other owner/parser of the router reason vocabulary (`w1/CN01Overlap.md` §Ownership); author-asserted.

## Extras

- **Prefile falsification ledger:** `python3 scripts/hyaku/prefile-falsification.py --lane kama --round 99` → `PREFILE-FALSIFICATION: pass claims=3 rows=9 attack_seats=6 findings=0`, exit 0 (ledger `.ufo/waves/round-99/claim-falsification.tsv`; every attack seat read, each `falsifies-wording` row points at `plans/round-99-amendment-1.md`).
- **Pre-report gate:** `PRE_REPORT round=99 arms=14 failed=5 uncommitted=1` (`measured/pre-report-gate.out`; failed arms: `newest-closure` carried — the round-97 closure carries no ISO date; `round-scope` and `round-clean` on the gate's own untracked receipt; `round75-instruments` carried `bad_rows=19` (L0 r87/r89 open); `round78-instruments` carried host Ollama listener on 127.0.0.1:8080). `selfdesc` and `receipt-audit` pass after the round-99 record fixes.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none by the L1 or reported by any seat; pacman untouched.
