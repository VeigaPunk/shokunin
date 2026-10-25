# kotodama — round 56 report (hyaku phase 4, attempt 1, L1 KotodamaR56)

Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. The lane tip is `6386218a3d00bec2fa6295a40ee8ff07164ccb2b` (jj-lane helper `landed`). The round started from base `0daf89fe`. The claim base is `045f458` and the declaration is `b4b7db9`. No earlier attempt of this round was logged as dead.

## Work performed

**Declared claims (2):**
- **C — coverage.** This is a learning claim and the round's sourced claim. It adds one civilizations entry, `corpus/knowledge/civilizations/kongo-kingdom.md`, a reference base on the Kingdom of Kongo. Knowledge files go from 231 to 232. Acceptance is `python3 -B reports/round-56/accept-c.py`, with seven legs. The entry may cite only C's reserved export block, S359–S418.
- **O — operability.** This is a capability acquisition: `tools/check-gate-quotes.py` reports Gate rows that carry an HTML character reference (`html-entity`), applies its quote and Grounds rules to the decoded row, and exits 2 on invalid UTF-8. Acceptance is `python3 -B reports/round-56/accept-o.py`, with eight legs. This routes spot-check §5 item 6.
- **Lowest-axis note:** freshness stays paused by the open round-11 L0 question (`reports/round-56/claims.json`, `lowest_axis_note`).
- **Area move:** C works civilizations ground. Rounds 51–53 worked linguistics, 54 culture-material and 55 myth-symbol. The lore handoff is entry §14: a NON-CANON reference dossier. Lore's own policy, not its checker, keeps real polities out of the bible.

**Work items:**
- **Instruments.** Instruments landed at `052f145`. Two pre-dispatch critics found 7 and 6 defects (`.ufo/waves/round-56/predispatch/`), and the instruments were revised at `045f458`. The declaration landed at `b4b7db9`. The receipts at `456f5ad` are C controls 18/18, O controls 23/23, and a dry run whose `# measured-revision` names `b4b7db9`.
- **Build wave `kotodama-r56-build`, 46 seats** (`.ufo/waves/round-56/build/`):
  - 26 scouts opened about 60 sources.
  - ExecGateEntity built O.
  - ExecIntegrateRows56 built an integrator that writes no entities.
  - CriticMistakeMining56 traced round 55's entities to its integrator (R56-M1).
- **O landed `7576fd4`. C landed `767040e`.** C added 54 rows, S359–S412, all cited. Before landing, two third-party journal scans were rejected and the uncited blocks were not registered.
- **Falsify wave `kotodama-r56-falsify`, 37 seats** (`.ufo/waves/round-56/falsify/`). The falsify fixes were applied in the records commit `c8af23f`:
  - entry §14 handoff (CriticHandoff56);
  - 8 calibration sentences (CriticClaimC56);
  - the era table (CriticEraTable56);
  - the §13 bank and §1 (CriticCalibrationBank56);
  - merged-row anchors S361, S384 and S404 (ReviewExcludedSources56);
  - row cells S376, S386 and S406.
- **Spot-check routing** (`corpus/lessons/round-56.md`, Spot-check intake):
  - §5 item 1: the exact export block, plus a QUALITY criterion 7 amendment.
  - item 2: appended SCORECARD correction rows.
  - item 3 and the §2 Gaps note: a revision-naming dry run, shown able to fail on the round-55 receipt.
  - item 4: S290, S292, S293, S306, S307, S320, S323 and S356 re-opened. S292, S293 and S306 were corrected.
  - item 5: the S309 access note.
  - item 6: claim O.
- **Mistakes R56-M1 to R56-M4** are in `corpus/lessons/round-56.md#mistakes`.

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `052f145cbcff6996c153d460d81ce346ce74bfbc` | instruments, start census | round 56 |
| `045f458ceaa35d40baa7c56727c346d60ae210bf` | instruments revised after the pre-dispatch critics (claim base) | round 56 |
| `b4b7db91a38447bb2c07b0ef436fc9654dcec89c` | declaration and manifest | round 56 |
| `456f5adc021346e7e9e7ce17a50d4bb1d208abbc` | pre-dispatch receipts | round 56 |
| `7576fd43bbbe34a00341e4b1956c907f2760e7d8` | claim O | round 56, O |
| `767040e0d8b9f9fe9e69b9a7ab8bc75a93b33b6b` | claim C: entry, README rev 2.13, SOURCES S359–S412 | round 56, C |
| `c8af23f3d0282cd1f6945b9bf54670a8478447a1` | records: lesson, falsify and routed fixes, QUALITY c7, SCORECARD, LOG, SHONEN, lessons index rev 13, wave records | round 56 |
| `3569d24444ebfa4c88d9f24c836de3c671c54387` | final measures receipt (measured-revision `c8af23f`) | round 56 |
| `6386218a3d00bec2fa6295a40ee8ff07164ccb2b` | late falsify reports and the moved misroot | round 56 |

## Before → after measurements

- **C:** `python3 -B reports/round-56/accept-c.py`.
  - Before, at `045f458`: exit 1, with SET, SWEEP and FLOOR FAIL (count 231, cited 0).
  - After, at `767040e`: exit 0, seven legs PASS (count 232, rows 232 files 232, cited 54). RerunAcceptC56 re-ran it in a sandbox.
  - Also exit 0 at `c8af23f` (`reports/round-56/telemetry/final-measures.txt`).
- **O:** `python3 -B reports/round-56/accept-o.py`.
  - Before, at `b4b7db9`: exit 1. ENTITY count 0; EXIT, DECODE and BADUTF8 FAIL.
  - After, at `7576fd4`: exit 0, eight legs PASS, selftest 38/38. RerunAcceptO56 re-ran it.
  - Also exit 0 at `c8af23f`.
- **Separability:** `python3 -B tools/check-claim-separability.py reports/round-56/separability-manifest.json` gives `SEPARABILITY: 0 findings`, exit 0, at `c8af23f` (final-measures). RerunSeparability56 independently got 0 at `767040e`.

## Sources & frontier

- **Census at round start:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, `ok` (`reports/round-56/telemetry/census-start.txt`).
- **Census at round end:** the same command → exit 0, `ok` (`final-measures.txt`).
- **Rows:** 358 → 412 (`grep -c '^| S[0-9]' corpus/SOURCES.md`).
  - Added: S359–S412, all `mined` and used-by the entry.
  - Status totals moved from 313/35/10 to 367/35/10.
  - S413–S418 stay unassigned.
- **Rows touched old → new, logged in the lesson:** S292 (feminine → neuter), S293 (access note), S306 (comma), S309 (access note), S361, S384 and S404 (merged anchors), S376 (pages), S386 (label) and S406 (Ré).
- **Gate:** 54 lines, plus rejects with reasons: Thornton 1991 and 2001 third-party JSTOR scans, Glottolog koon1244, and the Persée copy. `check-gate-quotes.py` reports 0 findings.
- **Mined mistake:** R56-M1. Round 55's integrator wrote the entities. The fix is claim O, shown able to fail.
- **Sourced claim:** C.
- **Frontier rows advanced:** the Kingdom of Kongo now has an owner. Lore handoff is §14.
- **Misroot sweep:** two seat reports had been written to the fleet root, ScoutCavazzi (build) and ReviewRowsS386toS388 (falsify). Both were moved byte-exact into the lane (`cmp` equal) and the fleet copies deleted (R56-M2). The remaining untracked fleet files are not this lane's.

## Trend verdicts

- **expansion: improved.** Kongo has a new owner (0 filename owners at base), 232 files, 54 new mined rows, and one new capability.
- **quality: improved, bounded.**
  - All acceptance legs pass, separability is 0, and 6 falsify critics' fixes were applied.
  - Bounds: two mutation survivors on O (double decoding, stop-at-first-bad-file) and the shortcut blindness of accept-o (R56-M3). Several row findings were carried, not applied: S359 pages 469/470, S360, S383–S385, S392, S395–S397, S399, S407, S379 tier and S367. Five seats were cancelled at filing.
- **discernment: improved.**
  - Two scans of uncertain licence were rejected before landing, and the falsify wave agreed.
  - The round-55 entity defect was traced to its tool, and the checker now catches all 16 rows; the spot-check counted 6.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SHONEN.md:6` now reads 412 rows, 367/35/10 (`c8af23f`). No non-author verifier is on record.
- [~] End-to-end domain task logged in LOG.md — the round-56 LOG entry: sources → entry → falsify → fixes `c8af23f`.
- [~] Instructions executable without oral context — falsify seats re-ran every counting command from committed paths in sandbox clones (`.ufo/waves/round-56/falsify/Rerun*.md`).
- [~] No cross-domain bleed — `.ufo/waves/round-56/build/ConnectSiblingKongo.md` found no sibling owner. Canon stays with lore (entry §14).

## Round shape and seats

- **Shape:** the default two v1 waves, plus one pre-dispatch call.
  - Pre-dispatch: 2 critics (the residual call).
  - Build wave: 46 seats. 26 scouts, 6 reviewers, 5 critics, 3 connectors, 3 executors, 3 scribes.
  - Falsify wave: 37 seats. 29 reviewers, 5 critics, 3 mutation-testers.
  - Round total: 85.
- **§3 L2 floor:** met in the build wave. The L1 holds the planner seat, and the planning data-walk rode ConnectInLaneKongo.
- **Dead seats:** none.
- **Cancelled at filing, never reported:** ReviewRowsS371toS373, ReviewRowsS380toS382, ReviewRowsS410toS412, RerunControls56 and ReviewSectionsCapitalKinFaith.
- **Late build reports, not integrated:** ScoutCavazzi and ScoutLamanDictionary. They are listed in the lesson Frontier.
- **Exclusion:** `kotodama51-prereg-critic` was not recreated.
- **Task tool:** the `task` tool requires `solutionSpace`, so one role-level `solutionSpace` was added per task. The validator's `{name, agent, task}` and `context` were otherwise sent unchanged (`*-sent-payload.json`).
- **Tool installs:**
  - seat ReviewRowsS401toS403 installed pypdf 6.21.2 and pdfplumber 5.14.0 via `uv` to read PDFs;
  - no other installs;
  - the pacman pause was respected.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Open L0 questions:** none new. The round-11 freshness question stays open.
