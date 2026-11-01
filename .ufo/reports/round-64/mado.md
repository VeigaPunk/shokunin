# mado — round 64 report (hyaku run 12, 2026-11-01)

Base `7fe65562c15d20e5cfdc1da536f774149ab52b7e` (the r63 closure tip);
lane head `66b8994b6397e27904779a26264c0196d2bd0368`, pushed (local ==
`ls-remote origin refs/heads/master` at round end). Four lane commits, all
through the plumbing helper with explicit file paths:
`688144573a26` (landing) → `8c5af6ad` (ledger-append repair, disclosed
red→green) → `ecfcea41` (landing counters + census receipts) → `66b8994b`
(record amendments). Scratch `scratch/mado-r64` created at round start,
deleted at round end. Security boundary held: no r56-era credential
material was opened, diffed, or surfaced; the new checker's scan scope is
caller-named paths and never touches r56-era material.

## Work performed

- **C1 — calibration: the r63 carry-in repair (the closure's routed item
  1).** The r63 spot-check (§6.1) routed the ephemeral-fixture citation:
  `windisplayconfig-error-path.txt` names `…receipts/broken-fixture.json`,
  never committed. The fixture is now committed at the cited path —
  disclosed at every claim site (entry Update §2, lesson, LOG, SCORECARD)
  as the round-64 re-creation (a truncated JSON snapshot; the r63
  original's bytes were ephemeral and are unrecoverable; the r63 receipt
  remains the record of the r63 run) — and the verdict re-derived against
  committed bytes: rc=2, the same whitelisted detail line as the r63
  receipt (`windisplayconfig-errorpath-r64.txt` + stderr). Evidence:
  `.ufo/waves/round-63/receipts/broken-fixture.json` at `688144573a26`;
  receipt `.ufo/waves/round-64/receipts/windisplayconfig-errorpath-r64.txt`.
- **C2 — coverage (sourced): the D05 flip-condition probe.** S424
  re-opened this round (page unchanged: git_commit `39f250c3…`, updated_at
  2026-05-15; flags table pins QDC_VIRTUAL_MODE_AWARE 0x10 and
  QDC_VIRTUAL_REFRESH_RATE_AWARE 0x40; the page's own example is the 0x12
  shape — the K44 transcription checked against the live page before any
  code, the M63-3 discipline, agreement recorded). One bounded read-only
  probe (`qdc-flagmatrix-probe.ps1`; getters only; no ids, no LUID halves,
  no names; no Set* verb) ran the documented shapes 0x02/0x12/0x42/0x52
  twice, byte-identical. Measured: 0x42 returns the r63 baseline verbatim
  (sentinel included — H29); 0x12/0x52 grow the mode table by a
  DESKTOP_IMAGE entry (infoType 3, the documented K51 vocabulary), set the
  documented SUPPORT_VIRTUAL_MODE path flag 0x8 (K46), and move the path's
  target `modeInfoIdx` 0 → 2 onto that non-TARGET entry, where the decode
  guard emits null (H30; the r63 rejected-row discipline kept).
  Disposition: **D05 narrowed, not flipped** — no documented shape returns
  decoded frequencies, cause stays `[UNK]`, remaining residue is the
  driver-class / second-host reading, operator-scoped (H31). Entry
  `knowledge/windows-displayconfig-r63.md` gains the append-only
  `## Update (round 64)` (rows H29-H31 + J29; 19 → 23 row sites; original
  105 lines a byte-preserved prefix). Crosscheck: 19/19 stable fields
  AGREE vs the r63 committed snapshot. Evidence: `qdc-matrix-run1/2.json`,
  `qdc-matrix-crosscheck.py` + `.txt`, `windisplayconfig-recheck-r64.txt`.
- **C3 — operability (capability acquisition):
  `tools/mado-receipt-citecheck.py`.** The routed defect class mechanized:
  extracts repo-relative committed file-path citations from caller-named
  artifacts (strict anchored grammar — bare-directory, rev-prefixed,
  absolute and URL forms are not citations), verifies each against one
  `git ls-tree -r --name-only` child, names MISSING with citing files,
  4 MiB cap, hermetic 12-assertion `--selftest` under a caller-declared
  `--scratch-root` (spawns nothing). Red demonstration at the base rev:
  the checker over the r63 receipts at `7fe65562` reports
  `citations=9 resolved=8 missing=1 … TARGET_MISSED` rc=1 — the missing
  citation is exactly the routed one. Green at the landing state:
  16/16 over the r63+r64 receipt trees (landing counters receipt). Ledger
  row + PROVINCE round-64 refinement in the same round. Evidence:
  `citecheck-red-base-rev.txt`, `citecheck-selftest.txt`,
  `landing-counters-r64.txt`.
- **Carry-in item 2 (the five L0 questions): routed around, never
  answered.** Omarchy freshness disposal, gate-selftest host gap,
  calibration resolved-active re-derivability, screen-capture scope, the
  L2 dispatch floor — all operator-owned (filed r57/r58/r59/r60 + the
  standing L2 line); the SCORECARD posture restated at base with fresh
  measurements (`before-state-r64.txt`); the rendered-pixel observation
  stayed unworked (no ruling). L1-only round (no dispatch surface on this
  host; disclosed since r57).
- **Axis posture (the lowest-axis obligation):** no axis is distinctly
  lowest — at base every published scored sub-axis sat at its finite
  maximum (navigation 78/78 = 10.0000, used-by TARGET_MET, ledger 103
  TARGET_MET, registry 371; freshness 8/8 = 10.0000; calibration
  resolved-active 86/86 published r56-era; the two omarchy rubrics dormant
  with receipts); stagnation nudge not applicable (last capability r63,
  gap 1 < N=3). The same posture rounds 56 and 58-63 ran under.
- **Considerthese:** mined again (nine files, mtimes unchanged since the
  r63 screen) — no adoptable proposal.

## Landed changes

| Change | Commit |
|---|---|
| Fixture `broken-fixture.json` at its cited path; error-path re-derivation receipt; claims declaration; 18 round-64 receipt files; entry Update; ledger row; PROVINCE refinement; SCORECARD r64 section; LOG entry; lesson round-64.md; the new tool | `688144573a2605704dfeb2bbca2d5bd6a06bf938` |
| Ledger-append repair (the landing's glued row split; r63 row bytes restored byte-exact, head-prefix cmp vs base; trailing newline added) — red `TARGET_MISSED` at the landing disclosed in the commit message | `8c5af6ad67007c6c77c3f71c689684e5fd626c2d` |
| Landing counters receipt (navigation 78/78; used-by TARGET_MET; ledger red@landing/green@repair in named sections; citecheck green 16/16; harmwatch 55/55 + 63/63; mado-verify sha `050efc720599345a`; prefix preservation 5/5), ledger red-leg rc file, census-after receipt | `ecfcea41697c5f6d709c010126743e1eca94cc55` |
| Lesson Addendum + LOG amendment + SCORECARD § Corrections (round 64) disclosing the red→green and the class rule | `66b8994b6397e27904779a26264c0196d2bd0368` |

Every change above has its LOG.md entry (round-64 entry + the amendment
bullet). Range numstat `7fe65562..66b8994b`: 30 files, +1192/−1 — the −1
is the ledger split repair (one glued line replaced by two); every other
file is a pure append or a new file.

## Before → after measurements

- **C1** — `git ls-tree <rev> --name-only -- .ufo/waves/round-63/receipts/broken-fixture.json | wc -l`:
  **0** at base `7fe65562` (before-state receipt) → **1** at the landing
  `688144573a26`; verdict re-derivation
  `python tools/mado-win-displayconfig.py --from-file .ufo/waves/round-63/receipts/broken-fixture.json`
  → rc=2, the r63 receipt's detail line verbatim (measured at
  `688144573a26`'s tree contents; receipt committed at the landing).
- **C2** — `grep -cE '^\| [HJK][0-9]{2} ' corpus/knowledge/windows-displayconfig-r63.md`:
  **19** at base (git-show form, before-state receipt) → **23** at
  `688144573a26`; `grep -c '^## Update (round 64)' <entry>`: **0 → 2**;
  probe determinism `cmp qdc-matrix-run1.json qdc-matrix-run2.json` →
  identical (rc 0 ×2); crosscheck
  `python -I .ufo/waves/round-64/receipts/qdc-matrix-crosscheck.py .` →
  19/19 AGREE, exit 0 (measured at `688144573a26`).
- **C3** — `git ls-tree <rev> --name-only tools/ | grep -c citecheck`:
  **0** at base → **1** at the landing; `python tools/mado-receipt-citecheck.py --selftest --scratch-root <scratch>`
  → `MADO_CITECHECK_SELFTEST: 12/12 assertions passed`, exit 0; red:
  checker at `--rev 7fe65562` over `.ufo/waves/round-63/receipts` →
  `missing=1 … TARGET_MISSED` rc=1;
  `python quality/check-tool-ledger.py --repo . --rev <rev>` →
  population=103 TARGET_MET at base → **population=104 TARGET_MET at the
  repair `8c5af6ad`** (the landing's red run recorded in the same
  receipt).

## Sources & frontier

SOURCES.md registry rows: **371 → 371** — counting command
`grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
(before-state receipt 371; landing counters receipt 371). Why: the r64
probe's entire documented surface is the eleven rows the r63 sweep opened
(S424-S434); no new URL entered the sweep, so no row was written (CORPUS
rule 1 — a row only after its source is opened this round), no
rejected-row event, and no cell edit (rule 2). The frontier step this
round is the **S424 re-open**: the page fetched in full on this host
(2026-11-01), metadata unchanged, the flag table's two virtual flags and
the page's own example call shape verified and quoted in the lesson Gate
before any probe ran — the sourced claim (C2) rests on it. Census:
start exit 0 (`mado ok`, 36 W04 + 1 W01, tee'd to
`census-start-r64.txt`) → end exit 0 (identical warning set,
`census-after-r64.txt` at `ecfcea41`); no new W04.

## Trend verdicts

- **expansion: improved** — the D05 flip-condition dimension of the CCD
  plane is measured ground now (entry 19 → 23 row sites on the flag-shape
  question the r63 closure routed in; S424 re-opened and its example call
  shape verified against the live page); the citecheck capability extends
  what the lane can do (record-hygiene verification) rather than what it
  knows.
- **quality: improved** — a routed citation now resolves to committed
  bytes with the verdict re-derived; a durable read-only instrument where
  the closure had a manual find; both prior Windows observers re-verified
  unchanged (D04 verdict and the D05 baseline); the round's three
  work-window write defects (M64-1 quoting, M64-2 truncated heredoc, the
  ledger glue) were each caught by a gate or read-back, disclosed, and
  repaired with byte-exact restoration — no defect smoothed.
- **discernment: improved** — D05 recorded "narrowed, not flipped" against
  a result (a structural change under the virtual-mode shapes) that would
  have tolerated a flipped headline; the probe's decode guard emitted
  null rather than decoding an undocumented union member; the red ledger
  state at the landing is recorded in the receipt, the SCORECARD
  Corrections block, the LOG amendment and the lesson Addendum instead of
  being repaired silently; rejected rows kept (DESKTOP_IMAGE decode, tool
  evolution, screen-capture probe, the five L0s) with flip conditions.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — historical assertion
  (corpus/knowledge/executor-test-sufficiency.md); outside-lane verifier
  independence still not established; this round adds measured, sourced
  rows but no non-author verdict.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  historical assertion (config-health-report-r3.md, VER-M3); this round's
  work is observer/record craft, not a new end-to-end desktop task.
- [~] Instructions executable by an agent without oral context —
  historical assertion (executor-test-sufficiency.md); the entry's Verify
  blocks and receipt re-derivation commands remain re-runnable from
  committed bytes (this round's own receipts follow the form), but the
  standing non-author check is still operator-uncommissioned.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — historical
  assertion (province-accuracy-selfaudit.md VER-M4B); PROVINCE gained only
  the append-only round-64 tool refinement, no boundary change.

Assimilation: none — shokuknow unreachable.
