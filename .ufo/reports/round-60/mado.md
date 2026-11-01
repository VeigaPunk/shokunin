# mado round 60 — the DPI-awareness join, the durable DPI observer, the r59 record corrections

Base `d1e64880b375529de185f49e124dd6cc42c58e75` (the r59 verifier spot-check).
Lane tip: `252bf383a224974e3b06b06f41755bcd1226d828` (pushed; landing
`edc2d378ba38ec760e8f964dc31be1f1e421f134` + receipts `252bf383`). Host:
Windows 11 Home, build 26200. L1-only round (no AgentSwarm dispatch surface on
this host; disclosed since r57, L0 open). Security boundary held: no r56-era
credential material was opened, excerpted or surfaced; the round touched only
the lane files named below.

## Work performed

- **Carry-in addressed first (r59 non-author closure, three items):**
  (1) SCORECARD round-59 C1 parenthetical number-shape drift — corrected
  append-only as `### Corrections (round 60)` with the measured per-file
  numbers **+17/−0** (r57 entry: trio +4 + errata +13) and **+5/−0** (r58
  entry: trio), re-derivation `git diff-tree -r --numstat 6f2e4115 25294ab3 --
  <the two entries>` (receipt `.ufo/waves/round-60/receipts/c1-counts-landing-r60.txt`);
  (2) LOG round-59 tail bullet "M59-1..M59-3" vs the lesson's four mined
  mistakes — corrected by the LOG § Round 60 correction bullet; the sweep also
  found the same-class defect in SKILL § Round 59's ground line, corrected in
  the same move (SKILL § Round 60 rule 3); both defect lines keep their
  original bytes (landing numstat: 0 deleted lines in SCORECARD.md, LOG.md,
  SKILL.md); (3) the three open L0 questions (omarchy freshness disposal;
  gate-selftest host gap; calibration resolved-active re-derivability) routed
  around, never treated as answered — named in the SCORECARD posture and the
  lesson's Rejected list. Evidence: `.ufo/waves/round-60/receipts/before-state-r60.txt`.
- **C1 calibration (claimed)** — the carry-in corrections above. Target axis:
  calibration. Evidence: `.ufo/waves/round-60/receipts/before-state-r60.txt`,
  `c1-counts-landing-r60.txt`; lesson `corpus/lessons/round-60.md` § Gate.
- **C2 coverage, sourced (claimed)** —
  `corpus/knowledge/windows-dpi-awareness-metrics-r60.md` closes the r58
  entry's named caller-branch residues in the same launch shape: the
  `powershell.exe` child measures `DPI_AWARENESS_UNAWARE` (0) (H13);
  `GetSystemMetrics(SM_CXSCREEN/SM_CYSCREEN)` = 1920x1080 equals
  `GetSystemMetricsForDpi(…, 96)` (H14, agreement — J13 names the vacuous
  shape: at effective 96 the metrics join cannot identify the branch, the
  getter does); main-window histogram 6 × `PER_MONITOR_AWARE` (H15);
  foreground window dpi 96 with window awareness 2 read against S404's return
  table (H16/J14; the r58 process context stays `[UNK]`, same-shape pin
  disclosed). 4 H + 7 K + 4 J rows, indexed. Probe committed read-only
  (`.ufo/waves/round-60/receipts/dpi-awareness-probe.ps1`), two byte-identical
  runs rc=0 (`dpi-awareness-run1.txt`/`run2.txt`). Rests on rows S406-S411
  (opened in full 2026-10-31 BEFORE any row was written) + re-used S404.
- **C3 operability, capability acquisition (claimed)** —
  `tools/mado-win-dpi.py` (`VERSION r60-v1`), the durable DPI-virtualization
  observer: selftest `MADO_WINDPI_SELFTEST: 10/10 assertions passed` rc=0
  (named assertions: the documented GetSystemMetrics 0-failure return treated
  as CHECK FAILED never a measurement; histogram-sum self-check; whitelist
  drop; static no-titles/no-names/no-handles/no-Set* pins); live
  `MADO_WINDPI: CLEAN (awareness=unaware metrics=1920x1080 dpi96=1920x1080
  windows=6 fg_dpi=96)` rc=0 twice, byte-identical; `--from-file` re-derives
  from the committed snapshot rc=0; malformed snapshot → `MADO_WINDPI: ERROR
  (stage=parse …)` rc=2, raw bytes never echoed; crosscheck 5/5 stable fields
  AGREE (`windpi-crosscheck.txt`); tool ledger population 99 → 100
  (`population=100 ledger_rows=100 … TARGET_MET`, rc=0,
  `landing-counters-r60.txt`). Ledger row + PROVINCE round-60 refinement +
  capabilities row landed in the same round.
- **L0 side channel:** one line appended (`mado | round-60`) — the
  screen-capture-scope question the r59 route named as the rendered-pixel
  precondition (candidate shape: statistics-only, no-persist capture). Routed
  around; the limit stays named in the entry § 4.
- **Mistakes mined:** M60-1 (selftest assertions written against an imagined
  output shape — three red assertions, all assertion-authoring bugs, one of
  which forced a real improvement: the file-mode line now carries the
  awareness name), M60-2 (the M58-4 class re-armed: an rc read through a
  pipeline tail printed RC=0 beside a 7/10 selftest line — a
  self-contradicting receipt; the rule is now "a receipt whose verdict line
  and rc disagree is malformed by construction", and the affected receipts
  were regenerated with owned rcs), M60-3 (a heredoc append truncated
  SCORECARD.md mid-line; caught by the anchored section-count greps and a
  line-count check; the file was truncated back to the byte-exact original
  3057 lines — `head -3057 | diff` against `git show <base>:SCORECARD.md`,
  ORIGINAL_PRESERVED — and the section re-appended from a written file). All
  in `corpus/lessons/round-60.md` § Mistakes with class, evidence pointer,
  captured-by and fix.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| SOURCES rows S406-S411 + S404 used-by extension (old→new logged in the lesson) + search-log § Round 60 | Round 60, C2 bullet | `edc2d378` |
| `corpus/knowledge/windows-dpi-awareness-metrics-r60.md` (new entry, trio first) | Round 60, C2 bullet | `edc2d378` |
| corpus/README.md index row + Round 60 frontier bullet | Round 60, C2 bullet | `edc2d378` |
| `tools/mado-win-dpi.py` + quality/tool-ledger.md row + PROVINCE round-60 refinement | Round 60, C3 bullet | `edc2d378` |
| SCORECARD `### Corrections (round 60)` + `## Round 60` section + capabilities row + planned r61 | Round 60, C1 bullet | `edc2d378` |
| LOG `## Round 60` section incl. the round-59 tail-bullet correction | Round 60 header + correction | `edc2d378` |
| SKILL § Round 60 (three rules + ground) | Round 60, C1 bullet | `edc2d378` |
| `corpus/lessons/round-60.md` (Gate, Admitted, Rejected ×3, Mistakes M60-1..3, Census, Considerthese, route) | Round 60 (mined mistakes) | `edc2d378` |
| receipts (16 files, `.ufo/waves/round-60/receipts/`) | Round 60, harm-watch bullet | `edc2d378` |
| landing-revision counter receipts + C1/C2/C3 landing counts | Round 60, harm-watch bullet | `252bf383` |

Landing diff shape (commit-to-commit, `git diff d1e64880..edc2d378`):
26 files, +1200/−1; the one deleted line is the S404 row's old used-by cell
(the SOURCES contract's allowed in-place move, logged old→new in the lesson).
SCORECARD.md +82/−0, LOG.md +67/−0, SKILL.md +50/−0, PROVINCE.md +18/−0,
README +2/−0, ledger +1/−0 — insertions only. `tools/mado-verify.sh` bytes
untouched (frozen instrument; not in the changed set).

## Before → after measurements

Measured commit: `edc2d378` (counters), receipts `252bf383`.

- **C1 (calibration):** `grep -c '^### Corrections (round 60)' SCORECARD.md`
  → 0 at base `d1e64880`, **1** at landing; `grep -c '^## Round 60' LOG.md` →
  0 → **1**; `grep -c '^## Round 60' SKILL.md` → 0 → **1**; preservation:
  `git diff d1e64880..edc2d378 --numstat -- SCORECARD.md LOG.md SKILL.md` →
  **0 deleted lines in each**; measured numbers re-derived:
  `git diff-tree -r --numstat 6f2e4115 25294ab3 -- corpus/knowledge/windows-desktop-plane-r57.md corpus/knowledge/windows-permonitor-dpi-r58.md`
  → `17 0` / `5 0`; lesson mistake count `grep -c '^- \*\*M59-'
  corpus/lessons/round-59.md` → **4**. Receipts: `before-state-r60.txt`,
  `c1-counts-landing-r60.txt`. (Note: unanchored greps for the defect strings
  count 3 at landing — the corrections themselves quote the strings; the
  preservation proof is the numstat, the movement proof is the anchored
  block count.)
- **C2 (coverage, sourced):** `ls corpus/knowledge/*.md | wc -l` → 74 → **75**;
  `grep -cE '^\| `knowledge/[^`]+\.md`' corpus/README.md` → 74 →
  **75**; `grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → 342 → **348**; entry rows `grep -cE '^\| [HJK][0-9]{2} '
  corpus/knowledge/windows-dpi-awareness-metrics-r60.md` → **15** (4 H + 7 K +
  4 J); navigation counter (SCORECARD § Counting command, fleet round 1, with
  `python` for `python3`) at `edc2d378` → `indexed=75/75 missing=0 dangling=0
  duplicates=0 coverage=10.0000/10`, exit 0. Probe re-run rc=0,
  `thread.awareness=0`, runs byte-identical.
- **C3 (operability, capability):** `git ls-tree d1e64880 --name-only tools/ |
  grep -c win-dpi` → **0**; at `edc2d378` → **1**; selftest 10/10 rc=0; live
  CLEAN ×2 byte-identical rc=0; `--from-file` rc=0; ERROR path rc=2;
  crosscheck 5/5; `python quality/check-tool-ledger.py --repo . --rev
  edc2d378` → `LEDGER: population=100 ledger_rows=100 uncovered=0 dangling=0
  bad_pointer=0 empty_desc=0 verdict=TARGET_MET`, rc=0.

Harm watch (all at the landing, rc-owned, receipted): used-by counter at base
`missing=0 … TARGET_MET` (74/342) and at landing `missing=0 … TARGET_MET`
(75/348) — the M59-4 rule held proactively (every row the round's appends name
— S404, S406-S411 — carries the citing paths in the same landing); ledger at
base 99/99 `TARGET_MET`; navigation at base 74/74; both fail-closed checkers'
selftests at current bytes 55/55 and 63/63 (`harmwatch-selftests-r60.txt`);
census exit 0 both ends, warning set 36 W04 + 1 W01 unchanged, no new W04 for
S406-S411 (start run quoted in the lesson — not tee'd, disclosed; end receipt
`census-after-r60.txt`).

## Sources & frontier

SOURCES: 342 → 348 rows — counting command
`grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
at base `d1e64880` → 342, at landing `edc2d378` → 348. New rows S406-S411
(tier A, `mined`, opened 2026-10-31 in full on this host before any row was
written; ms.date 2018-12-05 with git_commit `fa53641576e3603fa7b66d3a4ad969d3ce49d6f3`
for S406-S409/S411 and `9267262487657894a8af112d7165006fed5035a7` for S410;
every located quote a verbatim ≤25-word substring of the opened body — the
lesson's Gate table carries URL, access date and quote per row). S404 re-used
for the J14 join (re-opened at its held URL; used-by cell extended in place,
old→new logged). One bounded sweep, no rejected-row event (the sweep was
bounded to the six documented getters the probe invokes; search-log § Round 60
appended). The lesson's `## Gate` records the opening per the census contract.

## Trend verdicts

- **expansion: improved** — new sourced entry on previously-uncovered ground
  (the DPI-awareness layer; the r58 entry's named residues close), knowledge
  74 → 75, index rows 74 → 75 (75/75 reachable, exit 0), registry 342 → 348.
- **quality: improved** — the durable capability lands with named red/green
  assertions (the documented 0-failure return is CHECK FAILED, never a
  measurement) and evidence both ways (ERROR path receipted rc=2, crosscheck
  5/5); the records were corrected to observed state with defect lines
  preserved; no admitted entry failed a re-check (navigation, used-by, ledger,
  census all green at the landing).
- **discernment: improved** — corrections carry re-derivation commands beside
  preserved defect lines; the vacuous metrics join is named rather than read
  as branch identification (J13) and the r58 process context stays `[UNK]`
  rather than being overwritten (J14); screen-capture scope went to L0 instead
  of self-authorization; three mistakes mined including a recurrence of M58-4
  (M60-2) caught by its own self-contradicting receipt, and a landing defect
  (M60-3) caught by anchored counts.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — historical assertion (corpus/knowledge/executor-test-sufficiency.md,
  MADO-R3-4); outside-lane verifier independence not established; this round
  adds § Round 60 (append-only) and does not change the verdict.
- [~] At least one end-to-end domain task executed and logged — historical
  assertion (config-health-report-r3.md, VER-M3); no new end-to-end desktop
  task this round (L1-only; the DPI join is observation-plane work).
- [~] Instructions executable by an agent without oral context — historical
  assertion (MADO-R3-4); dispatched subagents do not satisfy the
  outside-lane promotion rule; no change this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — historical
  assertion (province-accuracy-selfaudit.md, VER-M4B); this round appends the
  round-60 instrument paragraph + tool row (insertions only, +18/−0) and
  absorbs nothing from other lanes (third-party `C:\tmp` content untouched,
  as in r59).

Assimilation: none — shokuknow unreachable (considerthese re-screened: nine
files, 2026-10-19 through 2026-10-28, nothing new since the r58 mining; no
adoptable proposal).

Outside spot-check pending (not obtainable this round — no non-author reviewer
reachable; L1-only). Ready items: (a) the six S406-S411 quotes against the
named pages (ms.date/git_commit in each row); (b) `python
tools/mado-win-dpi.py --selftest` and the
live/from-file/error receipts (re-derivation commands in the entry § 5);
(c) the probe runs byte-compare; (d) the C1 numstat + anchored counts against
`git show <rev>:<path>`; (e) the counters at `edc2d378`
(`landing-counters-r60.txt`).
