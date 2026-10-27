# Round 41 — kasegi (attempt 1)

## Work performed

Claims frozen before data: **C1, depth:verifiability (4 held)**, the r41 export-mode closure suite; and **C2, coverage (8 held)**, Frontier F24 / source S063 for RFC 9116 security.txt. Neither claim is verified and neither score moves.

- C1: landed `corpus/instruments/r41-closure.sh`, the I1–I12 suite, round-40 D4/D5 erratum, D6 SKILL registry repair, R38 calibration criterion, and the r40 C1 correction records. The falsify wave reproduced I1 and I3 false acceptances: I1's evidence-not-named mutation keeps the union at 3/3; I3 accepts the `closed=10/100` mangled-token fixture. The final Y receipt is an honest red transcript, not a pass. Evidence: `.ufo/waves/round-41/wave2/CritC1KillRule.md`, `RevC1Counters.md`, and `.ufo/waves/round-41/final-gates/all-gates.txt`.
- C2: opened RFC 9116 and the IETF Datatracker record; landed S063 capture, S063-only manifest, knowledge entry, registry row, F24 coverage amendment, and Gate quotes. Source recheck and all counted C2 instruments pass after correcting the manifest from nine records to the one round-41 S063 record. Wave 2 then found substantive shared RFC 9116 ground with kake's `security-txt-publishing.md`; coverage credit is withheld pending the L0 scope ruling. Evidence: `corpus/knowledge/rfc-9116-security-txt.md`, `corpus/source-snapshots/round-41/manifest.json`, `CritC2Live.md`, and the `CritProvinceBoundary` output in the wave results JSON.
- Frontier/corpus upkeep: appended the S063 search-log and registry records, appended F24 to the corpus index and PROVINCE, appended the round-40 lesson erratum and R38, and updated the expected knowledge-file list. No existing SOURCES row cells changed.
- considerthese: mined proposal 7 from `considerthese/2026-10-26.md` and appended the missing Round-40 dispositions section to `corpus/knowledge/considerthese-proposals-ledger.md`; no other proposal was mined.
- Two v1 waves: build 60 seats plus falsify 33 seats = **93 total** (within 64–128). Wave 1 roles: executor 17, scribe 6, scout 11, critic 6, reviewer 9, mutation-tester 5, simplifier 1, connector 2, sentinel 2, revenger 1. Wave 2: reviewer 7, critic 13, mutation-tester 12, scout 1. Attack roles: 20/60, 32/33, 52/93 overall. Planner seat held by the L1 per frozen topology. No residual call; 0 dead seats. Wave 2 had 0 connector seats (conformance item; wave 1 had 2).
- Wave-2 findings beyond the claim verdicts: I7 bare-pipe/leading-whitespace parser variants survive; I5/I12 declaration completeness was not established; an outside-configured-root I6 stray is not scanned (the seat classified it outside the committed-fixture kill clause); capture-binding accepts tested missing-path/URL variants; the frontier counter drops a status-flipped F24 to 26/26 with exit 0, though the frozen after-state also requires the explicit F24 PASS line and 27/27; and I12 necessity is supported by the committed T7 symlink escape. Per-seat evidence is in `.ufo/waves/round-41/wave2/` and `kasegi-r41-falsify-results.json`.

## Landed changes

- C1/C2 integration and wave-1 outputs: lane commits `03ca614e5f30a9554b33b77d13c4272c85e8ed6e` and `ad7147532cb702b0d541d40499874552183d9132`.
- Wave-2 receipts, S063-only manifest correction, proposal-ledger fill, and lesson findings: `dda0685fb76c99d6a2ccf3971809ae3beaee8ee7`.
- Judged head **J** with refreshed declared blocks: `1f7464612ac4c44e39886b82e812610d3c039b13`.
- Receipt-only **Y**: `0f64b8c5b3522d4db2160db087002e3a5f321880`.
- Post-Y SCORECARD/LOG/SHONEN and lesson closure records: final lane **Z** `7ebe3cc71b3d1c18d44155ce5f71f92e07d6c409`.
- `LOG.md` contains `## Round 41 (attempt 1, fresh-start)` at Z. All lane commits were made and pushed through `scripts/hyaku/jj-lane.sh`; the final landed hash is Z above. The fleet report and L0 question are committed separately below.
- No tools installed or updated.

## Before → after measurements

**C1 — depth:verifiability.** Before: at the frozen base, the suite was absent and the do-nothing control could not print `closed=12/12` (`.ufo/waves/round-41/c1-controls/do-nothing.txt`; exit 127). At Y, `bash corpus/instruments/r41-closure.sh --export-ref 0f64b8c5b3522d4db2160db087002e3a5f321880` emitted `closed=10/12 exit=1`; `bash corpus/instruments/r41-closure.sh --selftest --export-ref 0f64b8c5b3522d4db2160db087002e3a5f321880` emitted `selftest cases=12 failures=6` and exited 1. The final receipt is 31 lines, sha256 `0915f51d774e5f4bd744912b6b2a87b7387f5437730bef166457766ca10b9e94`, and records `export-ref=1f7464612ac4c44e39886b82e812610d3c039b13`, `run-utc=2026-10-27T12:16:34Z`, and `closed=10/12 exit=1`. The receipt-at-Y replay also exits 1. Its I10 payload records base and r40 exports red (3/12 each); plain run refuses with exit 2. The I1 and I3 surviving mutations violate C1's frozen kill rule, so C1 is not verified.

**C2 — coverage.** Before (`.ufo/waves/round-41/c2-controls/before.txt`): F24 absent, frontier 23, registry 62, knowledge 59, harness 26/26, binding 54/54, audit expected 59, queued 0, census exit 0. After at Y: `grep -cE '^\| F[0-9]+ \|' corpus/README.md` → 24; `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 63; S063 mined rows → 1; knowledge files → 60; source-recheck Q1/Q2/Q3 pass at anchors 330/270/235; frontier `entries=27 pass=27 exit=0`; capture binding `records=55 bound=55 unbound=0`; audit `strict pass=60/60`, `expected=60 missing=0 unexpected=0`; census exit 0 with the two standing warnings; r22 measure `44/44`. The frozen C2 outputs are reached, but coverage credit is not verified because of the unresolved sibling overlap.

## Sources & frontier

`corpus/SOURCES.md` registry rows 62→63, command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; one new tier-A spec row, S063, status mined, opened 2026-10-27, recheck `on-release`, used by the RFC 9116 entry. No pre-existing status/recheck/used-by cell changed. Frontier rows 23→24 (`grep -cE '^\| F[0-9]+ \|' corpus/README.md`); F24 admitted. Search log and coverage/province amendments are appended. Census before and after both report only W04 S028/S029 duplicate-URL warnings and `kasegi ok` (exit 0). Assimilation: none; no shokuknow package rows or entries were adopted. Proposal 7's ledger upkeep was mined from `considerthese/2026-10-26.md` and filed as described above.

The L0 question is appended at `.ufo/l0-questions.md` (kasegi / round-41): whether F24 should retain only researcher-side triage/discovery content and treat shared RFC 9116 rules as adjacent, or whether the publisher/researcher split is sufficient.

## Trend verdicts

- **Expansion — unprovable-but-better:** F24/S063 adds a captured primary source and knowledge entry, but the non-author scope challenge found overlapping RFC 9116 ground in kake; no coverage score is claimed pending the L0 ruling.
- **Quality — unchanged:** the S063 capture, manifest, source-recheck, harness, binding, audit and census checks pass; the closure suite did not verify C1 and no quality-axis score move is claimed.
- **Discernment — unprovable-but-better:** the round corrected the r40 overclaim and reported the r41 I1/I3 survivors and F24 overlap without promoting either claim. The suite's own evidence test remains defective, so no stronger verdict is claimed.

## SHONEN

- `[~]` SKILL.md decision tables/checklists/cited sources — the r41 suite row and D6 table repair are present; no final green non-author closure.
- `[~]` End-to-end domain task — none ran; this round added reference knowledge, not an authorized live domain task.
- `[~]` Executable instructions — C2 commands pass, but the C1 suite receipt/selftest are red.
- `[~]` No cross-domain bleed — F24 has unresolved shared ground with kake; the L0 ruling is pending.
