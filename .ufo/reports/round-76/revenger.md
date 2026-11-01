# revenger — round 76 report (hyaku run 15)

## Work performed

Carry-in (addressed first, both items from the r75 non-author closure):

- **Item 1 — S444 per-leg correction.** Re-ran both legs on this host before
  writing anything: `rea --llms | grep -cE 'inspect_'` → **2**
  (`inspect_macho`, `inspect_signature`); `rea doctor | grep -cE 'inspect_'`
  → **0**. Correction row **S445** (`supersedes S444`) records the exact
  per-leg values and is machine-checked (`reports/round-76/receipt_probe.sh`).
  One number in the carry-in itself corrected: the substance was stated as
  "all 14 frozen-F family names absent"; the frozen counter counts **11
  operation names across 8 families** (SCORECARD F; `reports/round-71/measure.py:161`)
  — all 11 absent from the manifest text, substance stands, and the absence
  proved to be a representation artifact (kebab vs snake), not name drift.
  Evidence: `corpus/SOURCES.md` S445; `reports/round-76/receipt-before.log`.
- **Item 2 — F-counter amendment (sanctioned): not executed, premise
  refuted.** The premise "the frozen F counter's operation names no longer
  exist in the rea 6.8.0 producer" fails on three independent surfaces: (a)
  the 6.8.0 manifest declares kebab-case equivalents for every F family
  (`inspect-managed-artifact`, `inspect-android-package`,
  `capture-browser-scenario`, `inspect-web-page`, `observe-web-session`,
  `inspect-firmware-regions`, `inspect-artifact`, `inspect-evm-interface`,
  `analyze-javascript-application`); (b) the producer's own provider-gate
  payloads carry snake_case `details.operation: inspect_android_package` /
  `inspect_firmware_regions`; (c) a real 6.8.0 record writes
  `operation: inspect_managed_artifact` into the exact field the frozen
  predicate reads. The counter's name space is the producer's record
  vocabulary; F was **provider-gated per family** (android: caller-supplied
  `REA_JADX_MCP_JAR`; firmware 6.8.0 route: Linux + caller-supplied
  `REA_BINWALK_COMMAND`; browser: caller-supplied CDP endpoint; managed:
  works via built-in `rea-dotnet-static`), not name-drifted. Predicate
  unchanged, families unchanged, frozen counter bytes unchanged — per the
  lane's frozen-instrument discipline (r69; M50). The amendment's red-before
  duty is honored (`f-before.log`). Evidence: `reports/round-76/claims.md`
  §carry-in; `corpus/lessons/round-76.md`.

Declared claims (frozen at `68feeca6`, before any after-run):

- **C1 — coverage, criterion F (selected-family record presence).** Authored
  `corpus/fixtures/managed-r76/`: a 924-byte inert minimal managed PE/CLI
  (i386, IL-only DLL, COR20 header + BSJB metadata v4.0.30319, streams
  `#~ #Strings #US #GUID #Blob`, module `r76-managed.dll`, assembly
  `r76-managed` 1.2.3.4; generator self-check re-derives every premise from
  the built bytes, regen byte-identical, truth pin sha256
  `25ece37da2e0effbe313662d81469371d59a1de4c610ed081b8a68bcdd75733c`), then
  one real `rea inspect-managed-artifact <fixture> --format json` run (rea
  6.8.0, built-in `rea-dotnet-static`, no external engine), saved as
  producer-emitted bytes at `corpus/live/runs/round-76/` with receipt +
  LEDGER; identity oracle `ORACLE OK (10/10 checks)`
  (`corpus/fixtures/managed-r76/oracle_check.py`). Evidence:
  `reports/round-76/f-after.log`; S446.
- **C2 — calibration, new bounded criterion R (SOURCES-row receipt
  fidelity).** The S445 correction row + `receipt_probe.sh`, which re-runs
  both producer legs and machine-checks the row's recorded values, with a
  negative control that flags the base S444 row. Evidence:
  `reports/round-76/receipt-after.log`.

Fresh-start §7 spot-check (the three rejected closures re-read this round):
**K-map admissions (C05/C15)** ruled out — every admission path requires the
wave Q-review surface, absent on this host (r74 L0 re-checked this round,
still unanswered); r71's C05 kill defects are scope-sentence repairs needing
that same surface. **C10** ruled out — disposed `rejected` by the frozen kill
rule in r74; no repair-and-revote. **r73 C1** ruled out — unresolved by wave
release, its pin is the already-disposed candidate. Declared claims are
reachable by neither a do-nothing control nor those routes.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: claims + sha-pinned probes + red-befores | round-76 entry (freeze line) | `68feeca6b625dc94d31de3954cac75391cc22146` |
| landing: managed-r76 fixture (4 files) + round-76 producer run (4 files) + S445/S446 + lesson | round-76 entry (C1/C2 lines) | `9116ddd662b56b8a93232359e63525c53909b4ff` |
| adjudication: SCORECARD section, LOG entry, after/separability/no-harm/census receipts | round-76 entry (holds line) | `2316649a36ebe4344fc1aa0f65b4d0a8e35dddff` |

(`c21e5a42db4c84419adc6f12118b1ea18dd9aa21`, immediately before the freeze
content, is an empty-path treecommit — absolute paths instead of
repo-relative — caught by the mandated diff check and mined as
`corpus/lessons/round-76.md` mistake 3; no content was lost.)

All cited shas are ancestors of pushed `origin/main` = `2316649a…ddff`.

## Before → after measurements

- **C1 (F):** `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <git-archive
  tree>/corpus` — before (`f-before.log`, archive of `6f3a646c`):
  `F_COVERAGE=5/8 score=6.25`, `F_FAMILIES=['archives', 'evm', 'firmware',
  'javascript', 'native-static']`; after (`f-after.log`, archive of
  `9116ddd6`; re-run at final tip `2316649a`, same output): `F_COVERAGE=6/8
  score=7.50`, `F_FAMILIES` += `managed`; the operation histogram changes by
  exactly one record (`inspect_managed_artifact: 1`), all other counts
  byte-identical to red. Measured commits `6f3a646c` → `2316649a`.
- **C2 (criterion R):** `bash reports/round-76/receipt_probe.sh` — before
  (`receipt-before.log`): exit 1, `RECEIPT_LEG3=FAIL (S445 row absent)`,
  `RECEIPT_LEG4=S444_MISMATCH_FLAGGED (base row records 'prints 0'; actual
  llms leg prints 2)`; after (`receipt-after.log`): exit 0, LEG1/LEG2/LEG3
  pass, LEG4 still firing, `RECEIPT_VERDICT=green`. Same measured commits.
- **Separability:** C1-only tree (landing archive with SOURCES reverted to
  base) still prints 6/8 (`f-separability.log`); C2's before-run executed
  with zero C1 bytes in the tree and the probe references no fixture/run path
  (`r-separability.log`).
- **Holds:** FRESH_ROWS 18/18; no-harm diff — knowledge, README, all verifiers
  untouched; additions only in the new fixture/run dirs (`noharm-diff.txt`).

## Sources & frontier

`corpus/SOURCES.md` rows 444 → 446: +**S445** (own-work tier A, supersedes
S444 — per-leg census correction; carries the kebab-case manifest lines and
the snake_case payload evidence) and +**S446** (own-work tier A — the real
6.8.0 managed-artifact record; grounds C1). Both opened this round; both
claims are sourced claims (C1 → S446, C2 → S445). No existing row changed in
place. Census: round start exit 0 (31 W, disclosed W01/W04 classes, final
line `ok …/corpus/SOURCES.md`); round end exit 0, same 31 warnings, final
`ok …/corpus/SOURCES.md` (`reports/round-76/census-after.log`); row count
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 444
→ 446. Mistakes mined this round (four, full table
`corpus/lessons/round-76.md` `## Mistakes`): aggregated per-leg receipts (the
carry-in class), routing on an un-re-derived premise, treecommit
absolute-path empty commit (self-caught), generator metadata-layout asserts
(self-caught, Q06 held).

## Trend verdicts

- **expansion — unchanged.** No knowledge entry admitted; K stays 8/15
  (5.3); the F row's new record is evidence ground for an existing criterion,
  not a new domain surface.
- **quality — improved.** A false registry record (S444's aggregated claim)
  is corrected and machine-policed (criterion R), and F's ground moved from a
  stale premise to real current-producer evidence with a byte-derived
  identity oracle.
- **discernment — improved.** The round's own carry-in instruction (revise
  the F counter) was re-derived before execution and found premised on a
  false record; the refutation and the corrected carry-in number (11 names,
  not 14) are recorded rather than smoothed over.

No axis harmed: K/F holds green, no protected byte changed, no verifier or
gate touched, freshness hold intact.

Round shape: L1-only (this host has no L2/AgentSwarm dispatch surface; the
r74 L0 stands, re-checked, unanswered; receipts are L1-authored and
disclosed — the counter and oracle re-derive every verdict from committed
bytes). No tool installed or updated. No new L0 question filed (the open r74
L0 already covers the operator-supplied-provider class that gates F's
remaining families). considerthese reviewed (2026-10-28.md, 5 proposals):
none adopted this round. Assimilation: none — shokuknow unreachable.

CLOSURE-PREP: re-derive C1 by `git archive 2316649a36ebe4344fc1aa0f65b4d0a8e35dddff corpus`, extract, run `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <extracted>/corpus` (expect `F_COVERAGE=6/8 score=7.50`), then `python -B corpus/fixtures/managed-r76/oracle_check.py corpus/fixtures/managed-r76/truth.json corpus/live/runs/round-76/inspection.json corpus/fixtures/managed-r76/fixture.dll` (expect `ORACLE OK (10/10 checks)`); re-derive C2 by `bash reports/round-76/receipt_probe.sh` (expect exit 0, `RECEIPT_VERDICT=green`, LEG4 firing); the F-counter carry-in disposition to check is claims.md §carry-in: revision NOT executed because the producer evidence refutes its premise.

## SHONEN

- `[~]` SKILL.md real decision tables/checklists — unchanged this round; the
  box's non-lane re-confirmation debt stands (`SHONEN.md` box 1; no outside
  verifier available this round).
- `[~]` At least one end-to-end domain task executed and logged —
  strengthened this round: a real producer run on an authored managed
  artifact with a 10/10 identity oracle, logged (`corpus/live/runs/round-76/LEDGER.md`,
  `LOG.md` round-76 entry); L1-authored receipt disclosed.
- `[~]` Instructions executable without oral context — the round's probes run
  verbatim from committed bytes (`receipt-after.log`, `f-after.log`); no
  independent outside instruction verifier this round.
- `[~]` No cross-domain bleed — PROVINCE.md untouched this round; no engine
  readiness claimed (provider presence, not readiness — Q05); `grep -c
  ADJ-06 corpus/README.md` = 0 unchanged.
