# kama round-84 C1 independent review — CloseKamaR84.KamaC1Review

Scope: freeze-base `aca4f33ac1e2…` → terminal `ad370d57…` (10 commits, ancestor-verified via `git merge-base --is-ancestor`; `git rev-list --count aca4f33..ad370d57` = 10). Read-only; no gates/selftests executed; committed-byte measurements only.

## Independent register count (committed bytes)

- `git show aca4f33:registry/append-only-late.tsv | wc -l` → **124**; `git show ad370d57:… | wc -l` → **115** (−10 stale rows, +1 acceptance row = 11 `diff` changed lines).
- Removed rows: before lines 105–114, all `0d7c7c3ea7d1… SCORECARD.md` (10 rows).
- Rotation byte-exact: `diff <(git show aca4f33:…late.tsv | sed -n '105,114p') <(git show ad370d57:registry/append-only-late-r83-restored.tsv | sed -n '2,11p')` → empty (**IDENTICAL**); archive = header + 10 rows (11 lines); absent at base.
- New acceptance row at terminal: `96e28374593be13833aebeb70150877f58f4aadc SCORECARD.md b2d76c4c… 1 in-place-edit  round-84 accepts round-83` ✓ (frozen C1c).
- **Disclosure ledger untouched:** `git show` sha256 of `registry/append-only-disclosures.tsv` identical at base and terminal (`ef4a1330999ed482…` both); `git log aca4f33..ad370d57 -- registry/append-only-disclosures.tsv` → empty. No disclosure row landed; no audit semantics relaxed in that file.

## Frozen predicate vs receipts

Frozen C1 (`plans/round-84-claims.md`): gate `arms=13 failed=0 uncommitted=0` exit 0; real register `bad_rows=0 unaccepted=0` exit 0; fixture exactly one `note-wrong-deletion-round`, exit 1.

- `.ufo/waves/round-84/measured/after/gate-final-green.out`: `PRE_REPORT round=84 arms=13 failed=0 uncommitted=0`, 13 `PRE_REPORT_ARM` lines, `EXIT=0` — rev `b53cd336` (landing commit ad370d57's parent; jj receipt-lands-next-commit convention; rev-stamped honestly).
- `c1-debt.out`: `bad_rows=0 … unaccepted=0`, `EXIT=0`, rev `3e93febb`. `c1-fixture.out`: exactly **1** `note-wrong-deletion-round` (of 3 findings; other 2 are expected count-short in fixture context), `EXIT=1`, rev `3e93febb`.
- Implementation present at terminal: `git grep -c 'note-wrong-deletion-round|note-subject-mismatch|note-subject-unresolvable' ad370d57 -- tools/round81-append-debt.py` → 3; arm 13 `round83-instruments` in `tools/pre-report-gate.py:54` with `arms=13` docstring/selftest.
- Selftests: `gate-selftest.out` → `PRE_REPORT_SELFTEST pass=35 fail=0` (rev `3e93febb`); `c2-selftest.out` → `pass=16 fail=0`, `EXIT=0`.
- Frozen (before/) receipts: freeze commit `2d49bf70` added 5 (insertions-only), `eb03a64b` added controls + red-before (insertions-only), `3e93febb` added 2 more (insertions-only). **No frozen receipt mutated after commit**; before receipts stamped `rev=2d49bf70` (freeze tree), red-before honestly records `bad_rows=0 unaccepted=1` exit 1 per freeze amendment 1.

## Auxiliary disclosure miss — evaluation

Frozen work item (b) premise "their event is fully restored at the base" is contradicted by the freeze-tree control committed at freeze time: `measured/before/red-debt-real.out` → `unknown-event late line 105: 0d7c7c3e…`, `bad_rows=10` exit 1. The ledger is an event-loss ledger (`tools/append-only-audit.py:15-28,529-544`: a row must name an unheld graded deleted line); a metadata/rotation row naming the ungraded event cannot validate. EX02's refusal is evidence-grounded, not evasive; the lesson discloses the rotation old→new and the miss explicitly (`corpus/lessons/round-84.md:57`: "no fabricated disclosure is appended… This misses the frozen auxiliary disclosure instruction; no audit rule is changed").

**C1 grade:** agreed with parent lean — numeric predicate verified on rev-stamped receipts; auxiliary instruction missed honestly; frozen plan claims no axis move ("No axis score move is claimed"); scores remain 8/8/7/9/7/7 (`score delta0 on every axis`). Disposition **rejected-honest-stop** is correct; no unqualified round admission asserted anywhere.

## SCORECARD diff (axis harm)

`git diff aca4f33..ad370d57 -- SCORECARD.md`: all six axis scores unchanged. Evidence cells re-anchored to truthful adverse round-83 terminal values at `1d90dc81…` (operability now cites late22/bad10 exit1, window7/falls=no, delta bad10 — replacing the previously stale favorable claim; calibration keeps "round83 rejected-harmed, not admitted"; freshness cites graded=4 ungraded=1, selftest 14/0). Saturation adds round-83 capability entries (factual) and states "round84 claims no additional repertoire entry". Dated historical rows untouched; only head cells re-anchored + Round-84 sections appended + Planned→round-85. **No axis harm; adverse history preserved, not laundered.**

## Findings

- **P1/P2: none in scope.**
- P3 (wording residual): SCORECARD head authority cell still reads "C1 gate is under terminal measurement …; no green gate or admission is pre-claimed" (state at `3e93febb`) while the dated terminal section records the green gate at `b53cd336`. Resolved by the terminal section; no axis harm.
- P3 (residual gap): `gate-final-green.out` measured at `b53cd336`, landed in `ad370d57` whose delta touches selfdesc-input prose (SCORECARD +4, lesson +21; counter inputs tools/registry unchanged). Gate at the literal terminal tree not re-derived (prohibited to execute); disposition binds the receipt to `b53cd336` explicitly, so nothing is overclaimed.

## Verification gaps

Gate/selftests not executed (prohibited); `append-only-audit.py` disclosure-refusal reasoned from committed docstrings + EX02 analysis, not executed. All byte counts and receipt contents above were independently re-derived from committed objects.
