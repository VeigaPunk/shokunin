# mado — round 59 (2026-10-31, hyaku run 12)

Base `6f2e4115dc1ebeb87c4d1aba9803c04c82dc4c80` (the r58 verifier spot-check). Lane head
`25294ab3e426903c18f16ad98db76e5e24147a98`, pushed to origin master (local == remote,
`git ls-remote` verified). Landing commits, all through the plumbing helper, all shas
helper-printed: `054dcecf17dcc9ad3723fa10a642f741b6e75bcd` (main landing, 26 files,
+888/−17), `3eb5f5ee805469a221ea07347fa0395961ca8f4f` (used-by completion + landing
receipts, pushed), `25294ab3e426903c18f16ad98db76e5e24147a98` (corrected usedby-after
receipt, pushed). Host: Windows 11 Home build 26200, as r57/r58. Security boundary held:
no r56-era credential material opened, excerpted or surfaced; only the files named here
were touched.

**Claims (declared before the formal receipt runs; no predicate changed after scoring).**
C1 **calibration** — the r58 carry-in corrections (stale gate identity; missing provenance
trios). C2 **operability** — the carry-in's case-variation residual in the checker prefix
rule, hardened with a named test. C3 **coverage** (sourced) — the DWM service model,
closing the r57 entry's finding D01. Axis posture: no distinctly lowest axis (all published
scored sub-axes at finite maxima; same posture as r56/r58); the carry-in routed C1's open
ground, C2/C3 are real axis moves. L2 disclosure: the MISSION ≥8-L2 batched-dispatch floor
is not met — no AgentSwarm dispatch surface on this host (unchanged since r57; L0 open).
The two open L0 questions (omarchy freshness-rubric disposal; gate-selftest host gap) were
routed around, never treated as answered; a third same-class item (calibration
resolved-active NOT-RE-DERIVABLE per `check-axis-scores.py` at base) was filed to L0 this
round.

## Work performed

- Carry-in addressed first (r58 non-author closure routing): (1) the stale `93e43f8f…`
  gate identity in `corpus/lessons/round-58.md` corrected append-only — measured current
  identity: blob `9113c7c05e586328f44ed6822a3d12ff34c47a36`, sha256
  `050efc720599345a73bdce6c1d13d50eadeee9769c2ece02462223d0156703f1`, 4,194 L,
  byte-unchanged since round 19 (`7b4839d3`); receipt
  `.ufo/waves/round-59/receipts/gate-identity-r59.txt`. (2) Provenance trios (`source:` /
  `verified-at:` / `recheck:`) inserted above the titles of both Windows entries (pure
  insertions: +17/−0 and +5/−0 in the landing diff, which also carries the r57 errata
  append). (3) The C:/TMP case-variation residual hardened (C2 below). (4) The two open
  L0 questions routed around.
- C2 red-before at base bytes: both fail-closed checkers ACCEPTED `C:/DEV/shm/…`
  (`realpath` cannot case-fold an absent prefix; rc=1, bypasses=2). The carry-in's
  `C:/TMP` spelling is REFUSED at base on this host — masked because `C:\tmp` exists with
  third-party content (`kake-r16`, `openclaw`, `pi-github-repos`; other lanes' artifacts,
  left untouched) and `realpath` true-cases existing prefixes on both sides; per-prefix
  table in the receipt. Fix: `os.path.normcase` in the prefix compare (identity on POSIX),
  named pin `refuse-work-casefold` in each selftest (Windows-conditional; `SELFTEST_CHECKS`
  host-derived, 54 → 55 and 62 → 63), CLI refusals ×4 receipted, home and canonical
  `/tmp` refusals intact, production mode TARGET_MET, host left clean (`C:/DEV` verified
  absent after; probe removes every directory it creates).
- C3: `corpus/knowledge/windows-dwm-service-model-r59.md` — row S405 (Microsoft Learn
  Compatibility Cookbook, opened in full 2026-10-31) + re-opened S399/S400; host probes
  (`dwm-service-probe.ps1`, two byte-identical runs): `SERVICES 0`, `sc query UxSms` rc
  1060, dwm.exe services N/A point-in-time, composition `hr=0 enabled=True`. D01 closed
  flip-met with the named residue (no Win11-labeled model sentence in the bounded sweep).
- Mined M59-1..M59-4 in `corpus/lessons/round-59.md`, including M59-4: the r58 landing's
  own errata append named S402-S404 inside the r57 entry without extending their used-by
  cells — the frozen r56 counter read `missing=2 … TARGET_MISSED` at base; repaired this
  round; the same rule then caught THIS round's errata naming S405 (landing counter
  `missing=1`) and the cell was completed in the follow-up commit — final tip:
  `missing=0 … TARGET_MET`.
- L0 side channel: one append-only line (calibration resolved-active NOT-RE-DERIVABLE,
  third host-change rubric item).

## Landed changes (LOG entry per change; commits `054dcecf` → `3eb5f5ee` → `25294ab3`)

- `quality/check-tool-ledger.py`, `quality/check-wave-done.py` — case-folded prefix
  compare + named pins + host-derived `SELFTEST_CHECKS` (LOG round-59 C2 bullet).
- `corpus/knowledge/windows-dwm-service-model-r59.md` (new, indexed) — LOG C3 bullet;
  `corpus/README.md` index row 73 → 74 + frontier bullet.
- `corpus/SOURCES.md` — row S405; used-by cells of S399/S400/S402/S404/S405 extended
  (the used-by contract's consistency moves, including the M59-4 repair); search-log
  § Round 59.
- `corpus/lessons/round-58.md` `## Corrections (round 59)` (append-only);
  `corpus/lessons/round-59.md` (new: Gate, Mistakes M59-1..4, Census, Considerthese,
  route to r60).
- `corpus/knowledge/windows-desktop-plane-r57.md` — provenance trio (insertion) +
  `## Errata (round 59)` (D01 closure pointer); `windows-permonitor-dpi-r58.md` — trio
  (insertion).
- `SKILL.md` § Round 59 (three rules + ground); `LOG.md` round-59 entry; `SCORECARD.md`
  round-59 section (posture, three claim rows, harm watch, planned r60).
- `.ufo/waves/round-59/receipts/` — casefold-probe.py, casefold-before.txt (rc=1 BYPASS
  at base bytes), casefold-after.txt (rc=0), ledger-selftest-after.txt (55/55),
  wavedone-selftest-after.txt (63/63), casefold-cli-refusals.txt (4 × rc=2),
  failclosed-after-r59.txt (home refusal rc=2), ledger-production-r59.txt +
  ledger-landing-r59.txt (TARGET_MET), gate-identity-r59.txt, dwm-service-probe.ps1 +
  dwm-service-run1/run2.txt (byte-identical), census-after.txt, usedby-before/after-r59.txt,
  navigation-landing-r59.txt.

## Before → after measurements

- **C1 calibration**: `grep -c '## Corrections (round 59)' corpus/lessons/round-58.md`
  base → **0**, landing → **1**; `grep -c '9113c7c05e58' corpus/lessons/round-58.md`
  base → **0**, landing → **1**; `grep -c '^source:' corpus/knowledge/windows-desktop-plane-r57.md`
  base → **0**, landing → **1** (same shape for the r58 entry); landing diff for the two
  entries: +17/−0 and +5/−0 (insertions only). Measured at `054dcecf`.
- **C2 operability**: `python .ufo/waves/round-59/receipts/casefold-probe.py` at base →
  `CASEFOLD_PROBE: BYPASS (bypasses=2)` rc=**1**; at landing → `CASEFOLD_PROBE: NO-BYPASS
  (bypasses=0)` rc=**0**; `python quality/check-tool-ledger.py --selftest --scratch-root
  <scratch>` → **54/54 → 55/55** rc=0; `python quality/check-wave-done.py --selftest
  --scratch-root <scratch>` → **62/62 → 63/63** rc=0 (re-confirmed at the final tip);
  CLI variant refusals rc=2 ×4; home refusal rc=2 preserved; `python
  quality/check-tool-ledger.py --repo . --rev <landing>` → `population=99 ledger_rows=99
  … TARGET_MET`. Measured at `054dcecf` (selftests re-confirmed at `25294ab3`).
- **C3 coverage**: `ls corpus/knowledge/*.md | wc -l` **73 → 74**; `grep -cE '^\|
  `knowledge/[^`]+\.md`' corpus/README.md` **73 → 74**; `grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` **341 → 342**; entry rows `grep -cE '^\| [HJK][0-9]{2} '
  corpus/knowledge/windows-dwm-service-model-r59.md` → **14** (4 H + 6 K + 4 J);
  navigation counter (SCORECARD § Counting command, fleet round 1, `python` for `python3`)
  at the landing revision → `indexed=74/74 missing=0 dangling=0 duplicates=0
  coverage=10.0000/10`, exit 0; probe re-run rc=0 (`SERVICES 0`, `SC_UXSMS_RC=1060`,
  `DWM_COMPOSITION hr=0 enabled=True`). Measured at `054dcecf`/`3eb5f5ee`.

## Sources & frontier

- SOURCES.md rows 341 → 342 (counting command above): **S405** added (tier A, `mined`,
  opened 2026-10-31 — https://learn.microsoft.com/en-us/windows/compatibility/desktop-window-manager-is-always-on,
  opened in full; ms.date 2018-07-11, git_commit 40f2250e…, updated_at 2021-11-17;
  located quote: "In Windows 8, Desktop Window Manager (DWM) is always ON and cannot be
  disabled by end users and apps."). S399/S400 re-opened this round (K20 re-quotes S400's
  note from its page). No rejected-row event: one bounded sweep (search log § Round 59 in
  SOURCES.md), the one surfaced candidate opened and included; the sweep reports
  honestly that a Win11-labeled model sentence did not surface. C3 rests on S405 + the
  re-opened rows. Census: round-start run `mado ok` exit 0 (341-row state; warning set
  36 W04 + 1 W01; quoted here because the run was not tee'd to a file — disclosed), end
  receipt `.ufo/waves/round-59/receipts/census-after.txt` → same warning set, exit 0,
  342 rows; used-by `TARGET_MISSED missing=2` at base → `TARGET_MET missing=0` at the
  final tip (receipts committed).
- Mistake mined: M59-1 (an rc=1 crash indistinguishable from the bypass verdict — the
  exit-code vocabulary itself must be crash-safe), M59-2 (the masking host state:
  `C:\tmp`/`C:\var` exist; the demonstrable residual was the absent `/dev/shm` prefix),
  M59-3 (`git status` `MM` noise vs byte-identical `git show HEAD:`), M59-4 (r58's
  errata named S402-S404 without their used-by cells; same-round recurrence on S405 —
  rule re-proven against its own author).

## Trend verdicts

- **Expansion: improved** — the Windows plane's third sourced entry lands (registry
  341 → 342, knowledge 73 → 74, index 74/74 reachable); D01, the oldest open
  Windows-plane finding, closes on sourced ground.
- **Quality: improved** — the fail-closed checkers survive a demonstrated bypass class
  (red/green receipted, named pins, POSIX behavior untouched by construction); the DWM
  model is grounded by a sourced row joined to host probes rather than prose.
- **Discernment: improved** — the records were corrected to observed state (stale gate
  identity; missing trios; used-by missing 2 → 0), the closure carries its named residue
  (no Win11-labeled sentence) instead of smoothing it, and four mistakes are mined —
  including one caught against this round's own work.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  unchanged this round; historical assertion `corpus/knowledge/executor-test-sufficiency.md`
  (MADO-R3-4); outside-lane verifier independence still not established (L1-only round,
  no dispatch surface; L0 open).
- [~] At least one end-to-end domain task executed and logged — historical assertion
  (`config-health-report-r3.md`, VER-M3); no new end-to-end desktop task on this host.
- [~] Instructions executable by an agent without oral context — historical assertion
  (MADO-R3-4); dispatched-subagent independence rule unchanged.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — historical assertion
  (`province-accuracy-selfaudit.md` VER-M4B); this round touched only lane files; the
  `C:\tmp`/`C:\var` third-party content was observed, not touched (adjacency respected).

Assimilation: none — shokuknow unreachable (considerthese re-screened: nine files,
nothing new since the r58 mining; no adoptable proposal).

CLOSURE-PREP: re-derive at lane head `25294ab3e426903c18f16ad98db76e5e24147a98` — C1:
the three grep pairs above + `git diff 6f2e4115..25294ab3 -- corpus/knowledge/windows-desktop-plane-r57.md corpus/knowledge/windows-permonitor-dpi-r58.md` (insertions only);
C2: run `python .ufo/waves/round-59/receipts/casefold-probe.py` (rc=0 NO-BYPASS), both
selftests via `--scratch-root <scratch>` (55/55, 63/63), and the base-bytes red from the
committed receipt; C3: the three counting commands above + the probe re-run (rc=0);
harm: `git diff 6f2e4115..25294ab3 -- tools/` is empty, census exit 0, used-by
`missing=0 … TARGET_MET`, ledger 99/99 TARGET_MET. Spot-check the S405 quote against the
named page and the D01 closure reasoning in the entry § 4 against S399/S400/S405.
