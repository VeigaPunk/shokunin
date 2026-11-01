# mado — round 62 (2026-11-01, hyaku run 12)

Base `4c5435d8bb3dd108f1dba4998de73c514609d885` (the r61 verifier
spot-check). Host: Windows 11 Home, build 26200. L1-only round again (no
AgentSwarm dispatch surface on this host; disclosed since r57, the
L2-floor L0 open — unchanged, routed around, never treated as answered).
Security boundary held: no r56-era credential material was opened or
surfaced; the round touched only the files named below.

## Work performed

Claims declared before the formal receipt runs in
`.ufo/waves/round-62/claims-declaration-r62.md` (committed at the landing),
with a disclosed amendment (dated, pre-receipt) fixing the C3 selftest
count 10→11 and narrowing the C3 live-receipt shape to the census's real
property (churning counters; verdict lines stable). Three claims:

- **C1 calibration — the r61 carry-in corrections (append-only).**
  (a) The r61 closure's routed report-table number drift (see Erratum
  below) dispositioned by `## Corrections (round 62)` in
  `corpus/lessons/round-61.md` naming the superseded table rows beside the
  numstat re-derivation; the fleet-root report file is not lane-edited.
  (b) The same-correction family's section-name nit: the exact receipt
  header is `-- navigation counter (SCORECARD fence, python for python3) --`
  (re-derivation `git show 4c5435d8:.ufo/waves/round-60/receipts/landing-counters-r60.txt | grep -n '^--'`
  → line 2), corrected by `## Corrections (round 62)` in
  `corpus/lessons/round-60.md`; the LOG round-62 correction bullet names
  the short form's second site (LOG's own round-61 bullet). Defect bytes
  preserved: `git show <base>:<lesson> | diff - <(head -n N)` — r60 lesson
  208 lines, r61 lesson 175 lines at base, both ORIGINAL_PRESERVED.
  Evidence: `.ufo/waves/round-62/before-state-r62.txt` (measured at round
  start, before any edit, including both numstat re-derivations).
- **C2 coverage (sourced) — the DWM client-attribute plane.** Entry
  `corpus/knowledge/windows-dwm-attributes-r62.md`: 4 host rows H21-H24
  (composition TRUE re-measured beside r59's pin; the cloaked-window
  census — 14 cloaked of 161-170 top-level in every committed execution,
  reasons **7 app + 7 shell + 0 inherited** in every execution,
  `attr_failed` 0, counts only, never handles/titles/per-window rows; the
  frame-bounds join — `GetWindowRect` beside `DWMWA_EXTENDED_FRAME_BOUNDS`
  on the probe's own console window, a **7 px inset left/right/bottom,
  0 px top** in every execution; finding **D04** —
  `DwmGetCompositionTimingInfo` fails with undocumented `0x88980090` in
  BOTH documented call shapes, cbSize 320 per the documented layout,
  deterministic, cause `[UNK]`), 6 dated `[INF-docs]` rows K38-K43, 4 joins
  J21-J24, indexed (README row 77). Evidence: probe
  `.ufo/waves/round-62/receipts/dwm-attributes-probe.ps1` + `dwm-run1/2.txt`
  (rc=0 ×2, byte-identical except the census counters); entry at
  `19407ef2:corpus/knowledge/windows-dwm-attributes-r62.md`.
- **C3 operability (capability acquisition) — `tools/mado-win-dwm.py`.**
  Selftest **11/11** exit 0 after three red assertion-authoring runs
  (disclosed in lesson M62-3); live
  `MADO_WINDWM: CLEAN (composition=on reasons=app+shell timing=unavailable(hr=0x88980090))`
  rc=0 ×2 with **byte-identical verdict lines** while the JSON census
  churns on exactly the named field (`windows.top_level` 168→170 — receipt
  `windwm-live-churn-diff.txt`); `--from-file` re-derives from the
  committed snapshot rc=0; malformed snapshot → `ERROR (stage=parse …)`
  rc=2, raw bytes never echoed; crosscheck **5/5** stable fields AGREE
  against the independently executed probe (+ census structure, no equality
  claim on churn-prone counters); no Set*/Move*/Change* verb exists in the
  tool; ledger population 101 → 102. Evidence:
  `.ufo/waves/round-62/receipts/windwm-*.txt`, `dwm-crosscheck.py` +
  `windwm-crosscheck.txt`; tool at
  `19407ef2:tools/mado-win-dwm.py` (sha256 prefix `8a8ddf2be6833603`).
- **L0 routing:** the four open L0 questions (omarchy freshness-rubric
  disposal; gate-selftest host gap; calibration resolved-active
  re-derivability; screen-capture scope) routed around, never answered; no
  new L0 line — D04 is recorded as a host finding with cause `[UNK]`, not
  an operator question (its flip is named in the lesson's Rejected list).
- **Considerthese mined** (nine files, 2026-10-19 → 2026-10-28; the newest
  reflects on Linux-host rounds 44-54, pre-dating the host change): no
  adoptable proposal; the r57-r61 dispositions stand.
  **Assimilation: none — shokuknow unreachable.**
- **Mistakes mined:** M62-1 (the number-shape drift class recurring in the
  r61 report's own table), M62-2 (a struct-slug hyphen/underscore 404 —
  the M61-2 class, caught by open-before-write), M62-3 (three red
  selftest runs — the M61-1 class, third round running; each read against
  the implementation; every fixed count assertion carries its site list)
  in `corpus/lessons/round-62.md`.

## Landed changes

Four commits, all pushed to `origin master` by the plumbing helper (the
helper printed each sha):

| commit | change |
|---|---|
| `19407ef2` | the landing: 34 files, **+1768/−0** — SOURCES.md +37 (S418-S423 + Round 62 search log), README +2 (index row 77 + Round 62 frontier bullet), entry new +72, lesson r62 new +217 (later +40 in the addenda), lessons r60 +25 / r61 +28 (`## Corrections (round 62)` blocks), LOG +73 (Round 62 section), SKILL +70 (Round 62 section), SCORECARD +65 (Round 62 posture/claims/capabilities/harm watch/planned 63), PROVINCE +22 (round-62 refinement + tool row), tool-ledger +1, tool new +714, claims declaration +70, before-state +37, 18 receipt files |
| `f300b2ce` | used-by repair attempt: S400 cell extension **mis-aimed at S405** (the matched suffix belongs to S405) + lesson Addendum |
| `bd06d021` | used-by repair corrected: S400's cell extended (keyed on the row id), S405's mis-aimed extension reverted exactly + lesson Addendum 2 |
| `df415ef3` | record amendments before closure: LOG + SCORECARD harm-watch sentences corrected append-only (the S400 used-by cell move old→new logged) |
| `4fe4544` | receipts: `landing-counters-r62.txt` (the red-amber-green used-by record + navigation 77/77 + ledger 102) |

Full-range numstat (base `4c5435d8` → receipts tip `4fe4544`):
**34 files, +1806/−1 across the landing commits plus the receipts commit**
— the single −1 is row S400's line, the used-by cell moved in place
(old suffix `…windows-dwm-service-model-r59.md, corpus/lessons/round-59.md |`
→ new suffix `…corpus/lessons/round-59.md, corpus/knowledge/windows-dwm-attributes-r62.md |`;
proposition text untouched; the used-by contract's own consistency move,
disclosed in the lesson Addendum/Addendum 2 and now in the LOG/SCORECARD
amendments). Per-file (counting command `git diff 4c5435d8..4fe4544
--numstat`): LOG +73/−0, PROVINCE +22/−0, SKILL +70/−0, SCORECARD +65/−0,
SOURCES +38/−1, README +2/−0, entry +72/−0, lesson-r62 +254/−0, lesson-r60
+25/−0, lesson-r61 +28/−0, tool-ledger +1/−0, tool +714/−0, wave receipts
+441/−0. Every count in this table is re-derived by that one command at
closure.

## Erratum (round-61 report number drift — carry-in item 1)

The r61 closure routed, and this round confirms and corrects: the round-61
report's "Landed changes" table printed per-file counts of LOG "+52",
PROVINCE "+13", SKILL "+50" against measured **+64, +19, +55** (totals "28
files, +1416/−0" were correct). Re-derivation: `git diff-tree -r --numstat
cccda4da ad4e8403 -- LOG.md PROVINCE.md SKILL.md` → `64 0` / `19 0` /
`55 0`; totals `git diff-tree -r --numstat cccda4da ad4e8403 | awk '{a+=$1;
d+=$2; n++} END {print n" files "a" added "d" deleted"}'` → `28 files 1416
added 0 deleted`. The three table rows for these files are superseded; the
correction lives in `corpus/lessons/round-61.md` § Corrections (round 62)
(append-only, defect report bytes untouched — the lane does not edit
fleet-root reports), restated here as the erratum. This is the same
number-shape drift class r60 corrected in SCORECARD/LOG/SKILL and r61 in
the r59 lesson — the class rule now carried in SKILL § Round 62 rule 3: a
number asserted without its counting command is the defect, whatever
surface it sits on. (This round's own Landed-changes table above is
written under that rule — every number carries `git diff … --numstat`.)

## Before → after measurements

- **C1 (calibration).** `grep -c '^## Corrections (round 62)'
  corpus/lessons/round-61.md` → **0** at base `4c5435d8`, **1** at
  `df415ef3`; same grep on `corpus/lessons/round-60.md` → **0 → 1**;
  numstat re-derivation → `64 0` / `19 0` / `55 0` (command above);
  preservation ORIGINAL_PRESERVED both lessons (commands in the C1 row of
  the SCORECARD section). Measured at `df415ef3`.
- **C2 (coverage, sourced).** `ls corpus/knowledge/*.md | wc -l` →
  **76** at base, **77** at the landing; `grep -cE '^\| `knowledge/[^`]+\.md`'
  corpus/README.md` → **76 → 77**; `grep -cE
  '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  → **354 → 360**; entry rows `grep -cE '^\| [HJK][0-9]{2} '
  corpus/knowledge/windows-dwm-attributes-r62.md` → **14** (4 H + 6 K +
  4 J; D04 is a Findings bullet); navigation counter at the final revision
  `bd06d021` → `indexed=77/77 missing=0 dangling=0 duplicates=0
  coverage=10.0000/10`, exit 0. Measured at `19407ef2` (entry) and
  `bd06d021` (counters).
- **C3 (operability, capability).** `git ls-tree 4c5435d8 --name-only
  tools/ | grep -c win-dwm` → **0**; `python tools/mado-win-dwm.py
  --selftest` → `MADO_WINDWM_SELFTEST: 11/11 assertions passed`, exit 0;
  `python tools/mado-win-dwm.py` → verdict line above, exit 0 ×2,
  verdict lines byte-identical (`cmp` on the verdict lines), JSON churn
  named per field in `windwm-live-churn-diff.txt`; `--from-file` rc=0;
  malformed → rc=2; `python .ufo/waves/round-62/receipts/dwm-crosscheck.py
  .` → `CROSSCHECK: 5/5 stable fields AGREE`; `python
  quality/check-tool-ledger.py --repo . --rev bd06d021` →
  `population=102 ledger_rows=102 … verdict=TARGET_MET`. Measured at
  `19407ef2` (tool) / `bd06d021` (ledger).

## Sources & frontier

SOURCES.md rows **354 → 360** (counting command `grep -cE
'^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
Rows **S418-S423** (tier A, `mined`, opened 2026-11-01 in full via fetch
BEFORE any row was written; every located quote a verbatim substring):
S418 DwmGetWindowAttribute, S419 DWMWINDOWATTRIBUTE, S420
DwmGetCompositionTimingInfo, S421 DWM_TIMING_INFO, S422 UNSIGNED_RATIO,
S423 GetWindowRect. One bounded sweep (search log § Round 62), no
rejected-row event; one URL-correction event (hyphen slug 404 → underscore
slug, mined M62-2); no reused rows (S399/S400 re-quoted from held pages,
not re-fetched; S400's used-by cell extended — see Landed changes).
Census: start exit 0 tee'd to `receipts/census-start-r62.txt` (36 W04 +
1 W01, identical to r57-r61; 354 rows), end exit 0
`receipts/census-after-r62.txt` (same warning set; 360 rows), re-verified
byte-identical at the final tree before closure. Frontier: the DWM
client-attribute plane moves from unheld to sourced-and-measured; D04's
residue (a documented getter for the compositor refresh) and the rendered
pixel (behind the screen-capture L0) stay named in planned-63.

## Trend verdicts

- **expansion — improved.** One new sourced plane (6 new registry rows,
  1 new entry, 1 new capability) with the used-by contract held to
  `TARGET_MET`; knowledge files 76 → 77, index 77/77 reachable.
- **quality — improved.** The DWM layer now has a durable observer with
  red/green-disclosed assertions, a named-churn receipt discipline (the
  verdict line built from structure), and a crosscheck; the record-side
  drift class gained a carried rule (SKILL § Round 62 rule 3) with three
  rounds of instances corrected append-only.
- **discernment — improved.** D04 recorded as a host finding with cause
  `[UNK]` instead of a guessed cause; the mis-aimed used-by repair was
  disclosed amber and corrected within the round; three red selftest runs
  disclosed rather than smoothed; the amendment to the claims declaration
  (selftest count, receipt shape) was dated before the formal receipts.

## SHONEN

SHONEN: `[~]` ×4, unchanged — the four boxes remain lane-asserted with
historical assertions (SKILL tables, end-to-end task, no-oral-context,
no-cross-domain-bleed); no named non-author verifier ran this round, and
the lane-dispatched-seat rule keeps them `[~]`. Evidence pointers unchanged
from `SHONEN.md` (the round landed no event that upgrades any box).
