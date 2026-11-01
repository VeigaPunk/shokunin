# mado round 61 — report (hyaku run 12)

Base `cccda4dacc1009f767799ce62fe112fd53d2d47a` (the r60 verifier spot-check);
landing `ad4e8403c1cefc803303dc4d9477f913091938da`; receipts commit / new lane
head `0c77f7266879a569f4b3097db4a8878406f6412b`, both pushed to `origin master`
(`ls-remote` = local tip at round end). Host: Windows 11 Home, build 26200.
L1-only round (no AgentSwarm dispatch surface on this host; disclosed since
r57, L0 open — unchanged). Security boundary held: no r56-era credential
material was opened, printed or surfaced; the round touched only the files
named here.

## Work performed

- **Carry-in addressed first** (the r60 non-author closure's two routed
  defects + the standing L0 set): (1) the r60 lesson's Census pointer defect —
  three receipt names that do not exist under those names — corrected
  append-only as `## Corrections (round 61)` in `corpus/lessons/round-60.md`,
  naming the supersedings (the runs live in
  `.ufo/waves/round-60/receipts/landing-counters-r60.txt`'s named sections;
  the base used-by run is `usedby-before-r60.txt`) with re-derivation
  commands; (2) the r59 lesson line-74 "+4/−0 each" number-shape drift — the
  last standing member of the class r60 corrected in SCORECARD/LOG/SKILL —
  corrected append-only as `## Corrections (round 61)` in
  `corpus/lessons/round-59.md` beside the measured per-file +17/−0 and +5/−0
  (`git diff-tree -r --numstat 6f2e4115 25294ab3 -- <the two entries>` →
  `17 0` / `5 0`); (3) the four open L0 questions (omarchy freshness rubric
  r57; gate selftest r58; calibration resolved-active r59; screen-capture
  scope r60) routed around, never treated as answered; no new L0 line — the
  fourth was already filed (r60) and nothing new needed an operator decision.
  Preservation: both lessons' original bytes byte-exact (`git show <base>:<f>
  | diff - <(head -n <base-lines> <f>)` → empty; r59 217 lines, r60 181 lines
  at base).
- **C1 calibration** — the corrections above (target axis: calibration).
  Evidence: `.ufo/waves/round-61/receipts/before-state-r61.txt` (all base
  values, including the quoted base bytes of the r59 defect line) and the
  anchored greps in the claims table below.
- **C2 coverage (sourced)** — `corpus/knowledge/windows-display-topology-r61.md`
  (target axis: coverage): the native display-topology plane and the
  display-mode layer, the one Windows-plane layer no entry held (r57 managed
  Screen, r58 per-monitor DPI, r59 DWM service model, r60 metrics/awareness).
  Rows S412-S417 opened in full BEFORE any row was written; 4 H rows
  (H17-H20: native enumeration count 1 = managed count; primary
  MONITORINFOEXW `\\.\DISPLAY1`, rcMonitor (0,0,1920,1080), MONITORINFOF_PRIMARY;
  work area (0,0,1920,1032) — 48 px band, owner `[UNK]`, taskbar never read;
  current mode 1920x1080 @ 64 Hz, 32 bpp, registry settings identical, mode
  index series exactly 1), 10 K rows (K28-K37), 4 joins (J17-J20), finding
  D03 (a 1-mode driver list beside r58's three-way DPI-mode split). Probe
  `.ufo/waves/round-61/receipts/display-probe.ps1` + run1/run2
  (byte-identical, rc=0).
- **C3 operability (capability acquisition)** — `tools/mado-win-display.py`
  `VERSION r61-v1` (target axis: operability): the durable display-topology
  observer. Selftest **10/10** exit 0 (receipt `windisplay-selftest.txt`;
  three red assertion-authoring runs printed 9/10 before it — mined M61-1,
  red side disclosed in the lesson, all four failures were assertion bugs,
  never tool bugs); live `MADO_WINDISPLAY: CLEAN (monitors=1
  primary=\\.\DISPLAY1 mode=1920x1080@64 work=1920x1032)` ×2 byte-identical
  rc=0; `--from-file` re-derivation rc=0; malformed snapshot →
  `MADO_WINDISPLAY: ERROR (stage=parse …)` rc=2, raw bytes never echoed;
  crosscheck **5/5** stable fields AGREE against the independently executed
  managed probe (crosscheck script committed beside its receipt). Ledger
  population 100 → 101; PROVINCE round-61 refinement in the same landing.
- **Frontier**: SOURCES curated (six new rows + search log; census both
  ends); mistakes mined (M61-1, M61-2 in `corpus/lessons/round-61.md`);
  considerthese re-screened (nine files; nothing new since the r58 mining;
  no adoptable proposal). At least one claim rests on rows opened this round
  (C2 rests on S412-S417).
- Claim declarations were fixed before any formal receipt run
  (declaration file quoted verbatim in this report's appendix below); no
  predicate changed after scoring.

## Landed changes

Every change below is in landing `ad4e8403` (28 files, **+1416/−0** — zero
deleted lines in the whole landing) except the last receipt (in `0c77f726`):

| file | change | LOG entry |
|---|---|---|
| `corpus/lessons/round-60.md` | +27 (append-only `## Corrections (round 61)`) | C1 bullet |
| `corpus/lessons/round-59.md` | +23 (append-only `## Corrections (round 61)`) | C1 bullet |
| `corpus/lessons/round-61.md` | new (+175; Gate, Mistakes M61-1..M61-2, Census, route) | M61 bullet |
| `corpus/knowledge/windows-display-topology-r61.md` | new (+103; trio, H17-H20, K28-K37, J17-J20, D03, limits) | C2 bullet |
| `corpus/SOURCES.md` | +33 (rows S412-S417 at their registry position + Round 61 search log) | C2/harm-watch bullets |
| `corpus/README.md` | +2 (index row 76 + Round 61 frontier bullet) | C2 bullet |
| `LOG.md` | +52 (`## Round 61` section) | — |
| `SKILL.md` | +50 (`## Round 61` section: three rules + ground) | — |
| `SCORECARD.md` | +61 (Round 61 posture, claims table, capabilities row, harm watch, planned 62) | — |
| `PROVINCE.md` | +13 (round-61 refinement + tool row) | C3 bullet |
| `quality/tool-ledger.md` | +1 (the `tools/mado-win-display.py` row) | C3 bullet |
| `tools/mado-win-display.py` | new (+576) | C3 bullet |
| `.ufo/waves/round-61/receipts/` (16 files) | display-probe.ps1 + run1/run2; windisplay-selftest.txt + stderr; live-run1/run2; snapshot.json; fromfile; error-path; display-crosscheck.py + crosscheck; census-start-r61.txt; census-after-r61.txt; before-state-r61.txt; harmwatch-selftests-r61.txt | harm-watch bullet |
| `.ufo/waves/round-61/receipts/landing-counters-r61.txt` | +11 (in `0c77f726`: navigation 76/76, used-by missing=0 TARGET_MET, ledger 101 TARGET_MET, rev-pinned `ad4e8403`) | harm-watch bullet |

Commits (helper-printed, both authored `mado-shokunin <mado@shokunin.local>`,
both pushed): `ad4e8403c1cefc803303dc4d9477f913091938da`,
`0c77f7266879a569f4b3097db4a8878406f6412b`.

## Before → after measurements

- **C1 calibration**: `grep -c '^## Corrections (round 61)'
  corpus/lessons/round-59.md` → **0 → 1**; same on
  `corpus/lessons/round-60.md` → **0 → 1**; `grep -c 'landing-counters-r60'
  corpus/lessons/round-60.md` → **0 → 3**; preservation
  `git diff-tree -r --numstat cccda4da ad4e8403` → **0 deleted lines in
  every file** (measured at commit; defect lines byte-preserved — the r59
  line 74 re-read from the landing commit is unchanged). Measured at
  `ad4e8403`; base values in `before-state-r61.txt`.
- **C2 coverage**: `ls corpus/knowledge/*.md | wc -l` → **75 → 76**;
  `grep -cE '^\| `+backtick+`knowledge/[^`]+\.md`' corpus/README.md` →
  **75 → 76**; `grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → **348 → 354**; entry rows
  `grep -cE '^\| [HJKD][0-9]{2} '
  corpus/knowledge/windows-display-topology-r61.md` → **19** (4 H + 10 K +
  4 J + D03); navigation counter (SCORECARD § Counting command fence,
  `python` for `python3`) at `REV=ad4e8403` → `indexed=76/76 missing=0
  dangling=0 duplicates=0 coverage=10.0000/10`, exit 0 (receipt
  `landing-counters-r61.txt`). Measured at `ad4e8403`.
- **C3 operability**: `git ls-tree cccda4da --name-only tools/ | grep -c
  win-display` → **0**, at landing → **1**; `python tools/mado-win-display.py
  --selftest` → `MADO_WINDISPLAY_SELFTEST: 10/10 assertions passed` exit 0;
  live verdict line ×2 byte-identical exit 0; `--from-file` rc=0; malformed
  → ERROR rc=2; `python .ufo/waves/round-61/receipts/display-crosscheck.py`
  → `MADO_DISPLAY_CROSSCHECK: 5/5 stable fields AGREE`; `python
  quality/check-tool-ledger.py --repo . --rev ad4e8403` → `population=101
  ledger_rows=101 uncovered=0 … verdict=TARGET_MET` (receipt
  `landing-counters-r61.txt`). Measured at `ad4e8403`.

## Sources & frontier

- SOURCES rows **348 → 354** (S412-S417, tier A, `mined`, opened 2026-11-01
  in full via fetch before any row was written; quotes verbatim; metadata
  recorded per row: ms.date 2018-12-05 with git_commit
  `9267262487657894a8af112d7165006fed5035a7` / `a9040b7bd365036907a35293e28d8cd449e31b87`
  / `fa53641576e3603fa7b66d3a4ad969d3ce49d6f3`, and DEVMODEW ms.date
  2023-06-13 with `f014fff5b27fe5eb5115f15dd6762713bc73c697`). Counting
  command: `grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → 348 at base, 354 at landing. One bounded sweep over
  the six documented functions/structures the artifacts call; no
  rejected-row event; one URL-correction event inside the sweep (windef.h
  MONITORINFO path 404 → winuser.h path; recorded in the search log, mined
  M61-2). No reused rows (none of the six URLs was previously held; no new
  census W04).
- Census: start `mado ok` exit 0, 36 W04 + 1 W01, tee'd to a committed
  receipt this round (`census-start-r61.txt` — closes the r59/r60 un-tee'd
  disclosure); end `mado ok` exit 0, 36 W04 + 1 W01
  (`census-after-r61.txt`), 354 rows. Both outputs committed.
- Mistake mining: M61-1 (the M60-1 class recurring three times in one
  selftest tally — static assertions written against remembered text shapes;
  each failure read against the implementation before either side was
  edited; final 10/10 receipt committed, red runs disclosed in the lesson)
  and M61-2 (struct-header locator guess 404'd inside the sweep; caught by
  open-before-write; fix: struct pages are located from the function page
  that documents the parameter taking them).
- Used-by discipline: every row this round's appends name (S412-S417)
  carries its citing paths in the used-by cell written at insertion; the
  landing used-by counter reads `missing=0 extra=0 … TARGET_MET`
  (`landing-counters-r61.txt`).

## Trend verdicts

- **expansion: improved** — a new sourced entry on ground no committed entry
  held (knowledge 75→76, index 75→76 at 76/76 reachable exit 0, registry
  348→354), plus a new capability row entered through a demonstrated run
  (ledger 100→101). All counted above.
- **quality: improved** — the capability lands with named red/green
  assertions and evidence both ways (ERROR path rc=2; crosscheck 5/5; three
  red selftest runs disclosed rather than smoothed); both routed carry-in
  defects corrected beside preserved defect lines with re-derivations; no
  admitted entry failed a re-check (navigation/used-by/ledger/census all
  green at the landing, receipts committed).
- **discernment: improved** — the corrections name where the evidence
  actually lives (the r60 pointer lesson applied to this round's own receipt
  shape by construction); the work-area band's owner stays `[UNK]` instead
  of being guessed (J17), and the mode layer's documented
  calling-context independence is pinned (J20) instead of importing the DPI
  entries' `[UNK]`; the Shell-plane widening was rejected with a named flip;
  four L0 questions routed around, never treated as answered; two mistakes
  mined including a recurrence class (M61-1) caught by its own tally.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — self-asserted; § Round 61 verified against the tool's and
  entry's actual bytes this round, but the box's historical assertions
  (`corpus/knowledge/executor-test-sufficiency.md`/MADO-R3-4) were not
  re-opened by a non-author this round; outside-lane verifier independence
  remains unestablished.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  self-asserted; the round's end-to-end observation chain (sources opened →
  probe → tool → crosscheck) is receipted, but the box's round-3 historical
  assertion was not re-verified by a non-author this round.
- [~] Instructions executable by an agent without oral context —
  self-asserted; the entry's § Verify commands re-run green on this host
  (probe, tool selftest/live/from-file, crosscheck), but no non-author
  executed them.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — self-asserted;
  the round-61 refinement records the new tool inside the existing
  read-only boundary and absorbs nothing from other lanes, but no fresh
  outside-lane audit ran this round.

SHONEN: no box reached `[x]` (no named non-author verifier ran this round);
each `[~]` carries its resolvable evidence pointer above.

Assimilation: none — considerthese re-screened (nine files, 2026-10-19
through 2026-10-28; nothing new since the r58 mining; no adoptable proposal;
the r57-r60 dispositions stand) — shokuknow unreachable.

## Appendix — the claims declaration (fixed before any formal receipt run)

The declaration file (written at round start, before the probe/tool receipt
runs; predicates verbatim):

```
# mado round 61 — claims declared BEFORE any formal receipt run (predicates fixed here; no predicate changes after scoring)

Base: cccda4dacc1009f767799ce62fe112fd53d2d47a (the r60 verifier spot-check commit).
Declared: 2026-11-01, before probe/tool receipt runs.

## C1 calibration — the r60 carry-in corrections (routed defects, fixed append-only)

(a) `corpus/lessons/round-60.md` § Census names three receipt files that do not exist under
those names — `navigation-landing-r60.txt`, `usedby-after-r60.txt`, `ledger-landing-r60.txt`.
The runs they describe live inside `.ufo/waves/round-60/receipts/landing-counters-r60.txt`
(sections `-- navigation counter --`, `-- used-by counter --`, `-- tool ledger production --`);
the base used-by run is `usedby-before-r60.txt`. Correction block `## Corrections (round 61)`
appended to the r60 lesson naming the three supersedings; filed bytes untouched.
(b) `corpus/lessons/round-59.md` line 74 reads "(diff shape +4/−0 each, checked at commit time
in the report)" — the same number-shape drift the r60 SCORECAD correction block measured
(measured per-file insertions at the r59 landing: +17/−0 and +5/−0; re-derivation
`git diff-tree -r --numstat 6f2e4115 25294ab3 -- corpus/knowledge/windows-desktop-plane-r57.md corpus/knowledge/windows-permonitor-dpi-r58.md`
→ `17 0` / `5 0`). Correction block `## Corrections (round 61)` appended to the r59 lesson
(the r59→r58-lesson corrections-block precedent); defect line bytes untouched.

[Counting commands: corrections-61 greps 0→1 in both lessons; landing-counters-r60 mentions
0→≥1; preservation 0 deleted lines in each.]

## C2 coverage (sourced) — the native display-topology plane: enumeration, work area, display modes

New knowledge entry `corpus/knowledge/windows-display-topology-r61.md` … sources opened
2026-11-01 in full BEFORE any row was written: S412 EnumDisplayMonitors, S413 GetMonitorInfoW,
S414 MONITORINFO, S415 MONITORINFOEXW, S416 EnumDisplaySettingsA, S417 DEVMODEW …
[Counting commands: knowledge 75→76; README index 75→76; SOURCES 348→354; entry rows ≥12;
navigation counter indexed=76/76 exit 0 at landing.]

## C3 operability (capability acquisition) — `tools/mado-win-display.py`

… selftest N/10 rc=0; live CLEAN ×2 byte-identical; --from-file; ERROR rc=2; crosscheck 5/5;
ledger 100→101 …
[Counting commands: ls-tree win-display 0→1; selftest 10/10 exit 0; ledger population=101 TARGET_MET.]
```

(The declaration file's own text is quoted trimmed of its counting-command
detail blocks, which are reproduced in full in the measurements section
above; the file itself was scratch and is deleted at round end per the
contract — its predicates are fixed here and in the SCORECARD section, which
was appended unchanged from it.)
