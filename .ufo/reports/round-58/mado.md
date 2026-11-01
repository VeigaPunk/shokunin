# mado — round 58 (2026-10-31, hyaku run 12)

Base `5e483f0d1fcabbbe21cb9ade04a93c24e8224b35` (the r57 verifier spot-check) →
landing `92c4b741f717f59db678f2f052c3901b28eaaf85`, pushed to `origin/master`
(`git ls-remote` = local = `92c4b741…`). Host: Windows 11 Home, build 26200
(unchanged from r57). L1-only round again — the MISSION ≥8-L2 dispatch floor
has no reachable surface on this host (disclosed since r57, L0 line stands
open). Three claims: **C1 operability**, **C2 coverage (sourced)**, **C3
calibration**. All three claims grew out of routed carry-in: the r57 closure's
receipt gap (C3), lesson M57-1 (C1), and the r57 entry's named "future ground"
(C2).

## Work performed

- **Carry-in 1 (r57 closure route 1) — the C2 malformed-snapshot ERROR
  sub-claim now carries committed evidence both ways**: the selftest tally
  itself covers the ERROR path (`tools/mado-win-desk.py` `VERSION r58-v1`,
  10th assertion: `--from-file` on a malformed snapshot → rc=2, the
  `ERROR (stage=parse …)` line, raw payload bytes never echoed; receipt
  `.ufo/waves/round-58/receipts/windesk-selftest-10.txt`) and a committed
  ERROR run exists (`.ufo/waves/round-58/receipts/windesk-error-path.txt`,
  rc=2). Live mode re-verified CLEAN after the change
  (`windesk-live-r58.txt`). Lands as claim C3 (calibration).
- **Carry-in 2 (M57-1) — host-portable scratch policy for the fail-closed
  checkers** (claim C1, operability): `quality/check-tool-ledger.py` and
  `quality/check-wave-done.py` accept `--scratch-root <dir>` — a
  caller-declared scratch *tree* that waives only the home-directory refusal;
  the shared-scratch prefixes stay refused in every mode, and the prefix
  compare now resolves the prefix (`os.path.realpath(bad)`), which also
  closes a base-state Windows bypass where `--work C:/tmp/…` slipped past the
  literal `/tmp` rule. Selftests pin the policy (pinned counts 50 → 54 and
  58 → 62). Receipts: base-bytes refusals (`ledger-selftest-before-refusal.txt`,
  `wavedone-selftest-before-refusal.txt`), green runs
  (`ledger-selftest-after.txt` 54/54, `wavedone-selftest-after.txt` 62/62),
  and `failclosed-after.txt` (4 refusal cases + production `TARGET_MET`).
- **Carry-in 3 (L0 omarchy freshness-rubric disposal)** — routed around, never
  treated as answered; no claim depends on it. A second L0 line was appended
  for a new, measured item (below).
- **Claim C2 (coverage, sourced)**: `corpus/knowledge/windows-permonitor-dpi-r58.md`
  closes the r57 entry's named future ground — the per-monitor DPI join. 3
  host rows (H06-H08), 7 dated `[INF-docs]` rows (K08-K14), 4 joins (J05-J08),
  divergence D02 (effective 96 vs angular 91 vs raw 92 — the three documented
  modes do not collapse; raw/angular are panel facts and must never feed UI
  scale factors). Probe committed as a receipt artifact
  (`.ufo/waves/round-58/receipts/dpi-probe.ps1`, read-only; runs
  `dpi-probe-run1.txt`/`run2.txt`). Sources S402-S404 opened this round.
- **Harm-watch measurement (disclosed, routed)**: the operability rubric's own
  command is not re-derivable on this host — `bash tools/mado-verify.sh
  --selftest` → `MADO_SELFTEST: FAILED — 360 passed, 100 failed`, rc=2
  (POSIX symlink fixtures denied; receipt `gate-selftest-windows.txt`). The
  10.0000 stands as the omarchy-host value with the receipt attached; the
  gate is byte-untouched (blob `9113c7c05e58…` identical base↔landing, pinned
  in `receipts/PINS.txt`); rewriting the frozen gate was the round's named
  reject; disposal routed to L0 (fleet `.ufo/l0-questions.md`, `mado |
  round-58` line).
- **Records**: SKILL.md § Round 58 (four rules; corrects the r57 sentence
  scope on selftest runnability), `corpus/README.md` (index row + frontier
  bullet), `quality/tool-ledger.md` (observer row assertion count 9 → 10,
  version noted), r57 entry `## Errata (round 58)` block (append-only),
  lesson `corpus/lessons/round-58.md` (M58-1..M58-4), LOG.md round-58 entry,
  SCORECARD round-58 section.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| checker scratch policy + selftest pins (C1) | `## Round 58` bullet 2 | `92c4b741f717f59db678f2f052c3901b28eaaf85` |
| per-monitor DPI entry + S402-S404 (C2) | `## Round 58` bullet 3 | `92c4b741f717f59db678f2f052c3901b28eaaf85` |
| observer tally fold + ERROR receipt (C3) | `## Round 58` bullet 1 | `92c4b741f717f59db678f2f052c3901b28eaaf85` |
| gate-selftest host-gap receipt + L0 line | `## Round 58` bullets 4 | `92c4b741f717f59db678f2f052c3901b28eaaf85` (receipts); L0 line in the fleet working tree, orchestrator commits it |
| SKILL/README/ledger-row/errata/lesson/LOG/SCORECARD | all bullets | `92c4b741f717f59db678f2f052c3901b28eaaf85` |

`git diff 5e483f0d...92c4b741 --stat`: 27 files changed, +914/−37 (12
work artifacts + 15 receipts incl. PINS/census).

## Before → after measurements

- **C1 (operability)**: `python quality/check-tool-ledger.py --selftest --work
  <scratch>` at base bytes → rc=2 `refusing work dir inside the home
  directory` (receipt); same for `check-wave-done.py` → rc=2. After:
  `python quality/check-tool-ledger.py --selftest --scratch-root <scratch>` →
  `LEDGER_SELFTEST: 54/54 passed`, exit 0; `python quality/check-wave-done.py
  --selftest --scratch-root <scratch>` → `MADO_WAVE_DONE_SELFTEST: 62/62
  passed`, exit 0. Fail-closed preserved: default `--work` under home → rc=2;
  `--work C:/tmp/…` → rc=2 `refusing work dir under /tmp`; `--work` +
  `--scratch-root` → usage error rc=2; production mode → `LEDGER:
  population=99 ledger_rows=99 … verdict=TARGET_MET` rc=0 (all in
  `failclosed-after.txt`). Measured commit `92c4b741…`.
- **C2 (coverage)**: `ls corpus/knowledge/*.md | wc -l` → 72 → **73**;
  `grep -cE '^\| `knowledge/[^`]+\.md`' corpus/README.md` → 72 → **73**;
  `grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → 338 → **341**; navigation counter (SCORECARD §
  Counting command, fleet round 1, `python` for `python3`) at the landing
  revision → `indexed=73/73 missing=0 dangling=0 duplicates=0
  coverage=10.0000/10`, exit 0. Entry rows
  `grep -cE '^\| [HJK][0-9]{2} ' corpus/knowledge/windows-permonitor-dpi-r58.md`
  → 14 (3 H + 7 K + 4 J). Measured commit `92c4b741…`.
- **C3 (calibration)**: `python tools/mado-win-desk.py --selftest` →
  `MADO_WINDESK_SELFTEST: 10/10 assertions passed`, exit 0 (base receipt
  `.ufo/waves/round-57/receipts/selftest.txt` records 9/9);
  `grep -rc "MADO_WINDESK: ERROR" .ufo/waves/round-57/receipts/` → 0
  matching files; `grep -c "MADO_WINDESK: ERROR"
  .ufo/waves/round-58/receipts/windesk-error-path.txt` → 1 (rc=2 recorded);
  ledger row consistency at the landing revision → `LEDGER: population=99
  ledger_rows=99 … verdict=TARGET_MET`. Measured commit `92c4b741…`.

## Sources & frontier

- SOURCES 338 → 341 rows (`grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md`, base `5e483f0d…` vs landing `92c4b741…`). New rows
  S402 (`MONITOR_DPI_TYPE`, quote "This value is the linear DPI of the screen
  as measured on the screen itself."), S403 (`GetDpiForMonitor`, archived
  previous-versions page — status carried in the row; quote "Queries the
  specified monitor for the dots per inch (dpi) horizontal and vertical
  values."), S404 (`GetDpiForWindow`, quote "Returns the dots per inch (dpi)
  value for the specified window."). All three tier A, `mined`, opened
  2026-10-31 in full, ms.date/git_commit recorded. No rejected-row event —
  the sweep was bounded to the three surfaces the probe rests on (search log
  § Round 58). Sourced claim: C2 rests on S402-S404. Census before → after:
  both `mado ok`, exit 0, emits byte-identical (36 W04 + 1 W01, all
  pre-existing); receipts `census-before.txt`/`census-after.txt`.
- Mistake mining: M58-1..M58-4 in `corpus/lessons/round-58.md` (the gate
  selftest host gap + the wrong r57 SKILL sentence; the probe's
  enum-order mislabel caught by opening sources before writing rows; the
  waiver-as-candidate design that broke the ledger P-rule, red before
  landing; an exit code read through a pipeline tail).

## Trend verdicts

- **expansion: improved** — one new declared-surface layer observed and
  sourced on the live host (per-monitor DPI: knowledge files 72 → 73,
  indexed and reachable, registry 338 → 341); the r57 entry's named future
  ground is closed by measurement (D02), not by deleting the note.
- **quality: improved** — the two fail-closed checkers are host-portable
  again with the fail-closed side receipted (refusals red, greens 54/54 and
  62/62, prefix-bypass closed); the r57 evidence gap is closed inside the
  tally itself; no frozen byte changed (gate blob identical; the r57 entry
  gained an append-only errata block).
- **discernment: improved** — the round's own probe mislabel (M58-2) was
  caught by the sourced-row discipline and kept visible in the entry; the
  operability rubric's host-gap was measured and routed to L0 instead of
  being papered over or unilaterally re-baselined; the rejected list names
  three declines with flip conditions (gate rewrite; unilateral rubric
  re-baseline; SetProcessDpiAwareness probe). All self-graded: no non-author
  reviewer was reachable this round (no dispatch surface), so these verdicts
  are the author's, ready for the closure's re-derivation.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — unchanged this round (`corpus/knowledge/executor-test-sufficiency.md`
  historical assertion stands; § Round 58 appended).
- [~] At least one end-to-end domain task executed and logged — unchanged
  (`corpus/knowledge/config-health-report-r3.md`, LOG round 3); no new
  end-to-end desktop task this round.
- [~] Instructions executable by an agent without oral context — unchanged
  (`corpus/knowledge/executor-test-sufficiency.md`); this round's artifacts
  carry re-derivation commands (entry § 5, receipts), but the outside-lane
  promotion rule is not satisfied by the author.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — unchanged
  (`corpus/knowledge/province-accuracy-selfaudit.md` round-5 receipt);
  PROVINCE needed no r58 correction (the Windows desktop plane group already
  covers the DPI join; no surface changed state).

Assimilation: `considerthese/` re-mined (all nine files, nothing new since
the r57 mining; no adoptable proposal in the lane's write surface) —
Assimilation: none — shokuknow unreachable.

Scratch dir `…/workspace/…/scratch/mado-r58` deleted at round end; the
committed receipts in `.ufo/waves/round-58/receipts/` carry the evidence.
