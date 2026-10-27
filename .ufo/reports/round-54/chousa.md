# chousa — round 54

## Work performed

This round declared two claims. Both were frozen before any seat scored: `chousa-shokunin/corpus/evidence/round54/claims.md`, commit `5a1a20630d8176a816a60bb43b0d0e7ee2db19a0`.

- **R54-C1, operability.** This is the lowest scored non-retired axis (3/10). The claim is a capability acquisition: `tools/capture-text.py` gains a defined text form for OLE Word 97+ `.doc` captures.
- **R54-C2, depth.** This is the sourced claim. It adopts theme C, the PRC citation standard GB/T 7714-2025, by document.

Work items:

- **C1 baseline and controls.**
  - The base tool refuses every OLE file: `LEGS=1/6 C1=FAIL` on three unseeded runs and on `--seed 7` (`controls/c1-before.txt`).
  - Control scores: CONST 0/6, NAIVE (UTF-16LE decode) 0/6, REFUSEALL 1/6. SHELL (shells to LibreOffice; the audit hook blocks it) scores 1/6 (`controls/c1-controls.txt`).
- **C1 candidate.** CFB reader, FIB, Clx piece table, cp1252/UTF-16LE pieces, main story, field results. Commit `8a7d0f137a352000d78704ba5695ded8857104fe`.
- **Post-candidate tool fixes from W1 (claims-erratum E2), landed `447cf7ed4dc1a3708518b99e9a5e62e177c11ce9`.**
  - The signed Prc `cbGrpprl` is now bounded. `R54ReviewOleTool` F1 and `R54ExecOleFuzz` found 37/600 Tracebacks at the candidate.
  - Tracked-deletion runs are now dropped through the CHPX FKPs. `R54ReviewOleSpec` found them; `tracked-deletion-check.py` FAILs on the candidate and PASSes on the landed tool.
  - Text forms of the five pinned captures are byte-identical before and after both fixes.
- **The frozen C1 counter is forgeable (E1).** `R54CritForgeC1` passed it 6/6 with a tool that reads the HTML the counter leaves beside each generated document and returns canned REAL output keyed by digest. I rebuilt that forge (`controls/build-c1-forge.py`) and added a post-freeze supplement, `c1-supplement.py` (ISOLATED, RESAVE, HELDOUT):
  - landed tool: 3/3;
  - rebuilt forge: 0/3, and CONST, NAIVE, REFUSEALL and SHELL also 0/3 (`controls/c1-forge.txt`).
- **C2 entries and rows.**
  - Entries: `corpus/knowledge/source-type-taxonomy-r36.md` (S121 SAMR record, S122 openstd notice) and `…-r37.md` (S123 JMU reproduction, tier B).
  - Rows S121–S123, 33 located quotes, and spans with `build-spans --check` → `STALE=0`.
  - The W1 S101 leg was cut, because its anchors used the undefined UTF-16LE form (E3).
  - Integrated at `6af11e9f4123b5f1115ff67b8507f612833fb216`.
- **Calibration.**
  - Nine anchored `correction:` lines re-point the S100/S101 anchors into tool dumps: `pointer-anchor-check.py` → `ANCHORED=16/16`.
  - QUALITY 97–100 and the SKILL gate rows are landed (gate registry `REGISTERED=144/144 MISMATCHES=0`).
  - The README round-54 section is landed.
  - `pdf-crosscheck.py` (NFKC) → `PDF_QUOTES=21 NOT_IN_INDEPENDENT=0 RAW_NOT_IN=14`.
- **Inherited state.**
  - The uncommitted `.ufo/waves/round-53/w2/swarm-registry.json` was committed in the freeze `5a1a2063`.
  - Round-53 W2 was never dispatched: there is no `w2.ready.dispatched` and no results file. Lesson Mistakes row 1 and QUALITY 99 record it.

## Landed changes

| commit | change | LOG |
|---|---|---|
| `5a1a20630d8176a816a60bb43b0d0e7ee2db19a0` | freeze: claims, counters, controls, before receipts, census start, inherited round-53 W2 registry | `chousa-shokunin/LOG.md` Round 54 |
| `8a7d0f137a352000d78704ba5695ded8857104fe` | C1 candidate (OLE `.doc` text form) | same |
| `9caf8fc6e9113c8135f930503102eef0dd909e2e` | W1 spec/dispatch (49 seats), section-10 collision/quarantine scratch | same |
| `6af11e9f4123b5f1115ff67b8507f612833fb216` | W1 integration: entries, rows, spans, lesson, QUALITY 97–100, SKILL/README, corrections, Prc bound, supplement + forge, ledger, pdf crosscheck | same |
| `447cf7ed4dc1a3708518b99e9a5e62e177c11ce9` | tracked-deletion drop + fixture/check, re-measure | same |
| `178667dc2c9d1656e864abfdc251c68757428613` | W1 reports/results, W2 spec/dispatch (38 seats) | same |
| `25abbe82b9f2b7c6e24580ac3f028611ba21f01f` | SCORECARD verdict + capability row, LOG, census end, W2 markers | same |

Final lane hash `25abbe82b9f2b7c6e24580ac3f028611ba21f01f`. `git ls-remote origin refs/heads/master` prints that hash.

## Before → after measurements

| claim | before | after | counting command | measured revision / verdict |
|---|---|---|---|---|
| R54-C1 operability | `LEGS=1/6 C1=FAIL` (base `c49ffc6c`); controls 0–1/6 | `LEGS=6/6 C1=PASS` on three unseeded runs and `--seed 7`; supplement 3/3 ×4; `TRACKED_DELETION=PASS` | `python3 corpus/evidence/round54/c1-count.py` (post-freeze: `c1-supplement.py`) | Tool sha256 recorded in `corpus/evidence/round54/measure-after.txt` (landed `447cf7ed`). **Improved narrowly**: the frozen counter also passes a forge (E1), and 7/16 W1 mutants survive it (`R54MutOle`). |
| R54-C2 depth | `ENTRIES=0/2 BOUND=0/3 QUARANTINE_VERDICTS=0/3 C2=FAIL`; staged control `REF_ID_UNBOUND=6`; adopter control `BOUND=3/3 ANCHOR_BOUND=0/3 C2=FAIL` | `ENTRIES=2/2 BOUND=3/3 REF_ID_UNBOUND=0 QUOTE_ROWS=33 CAPTURE_BOUND=33/33 ANCHOR_BOUND=3/3 INFERENCE_GROUNDED=2/2 QUARANTINE_VERDICTS=3/3 C2=PASS` | `python3 corpus/evidence/round54/c2-count.py` | `measure-after.txt` at `447cf7ed`. **Improved**, as presence, binding and located support. Entailment is not counted (`R54CritForgeC2`). |

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.

- **Census.**
  - Start: exit 0, with five pre-existing W04 (S051 S053 S073 S074 S075) (`corpus/evidence/round54/census-start.txt`).
  - End: exit 0, the same five W04 (`census-end.txt`).
- **Rows:** 120 → 123. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
  - Added by tier: A S121, S122; B S123.
  - Rows touched old→new: none. The S101 `used-by` is unchanged because the leg was cut.
- **Frontier advanced.**
  - Source-tier adjudication: an authority that serves a document's identity, set against a third-party copy that carries its text.
  - A new capture form: OLE `.doc`.
- **Assimilation.**
  - Theme C: two staged entries admitted, narrowed.
  - Collisions: 39 (S082–S120), guard proved (`.ufo/waves/round-54/assimilation/`).
  - Renumber map: S085→S121, S086→S122, S093→S123; S101 held.
  - Refused: the S101 leg (undefined form) and grey-literature-r40 (outside the frozen set). The text-form half of its flip now fires.
  - Quarantine: 24 slice rows, of which 3 are on theme URLs (S080, S088, S096). All three are `absent-as-written`, confirmed by `R54ExecQuarantineTheme`.
- **considerthese:** CT-20261026-1 (stable ids) is implemented as `considerthese-ledger.tsv` plus a checker → `PROPOSALS=35 … BAD=0`.
- **Sourced claim:** C2 rests on S121–S123, which were opened this round.

## Trend verdicts

- **expansion — improved.** Three documents absent at base are now bound, plus one new capture form. S101 earns no credit.
- **quality — improved.** The entries were re-grounded and narrowed. Undefined-form anchors were corrected. QUALITY 97–100 landed. The OLE reader was hardened (Prc bound, tracked deletions). No admitted entry was found false.
- **discernment — unchanged pending non-author closure.** The S101 cut, the S130 refusal and the quarantine verdicts are lane-dispatched judgements.

## SHONEN

- [~] Decision tables, error patterns, cited sources — `SKILL.md` round-54 gate rows; `corpus/QUALITY.md` 97–100.
- [~] End-to-end task executed and logged — `LOG.md` Round 54; `corpus/evidence/round54/measure-after.txt`.
- [~] Instructions executable without oral context — the counter and check commands in the round-54 SKILL rows.
- [~] Province fit — `PROVINCE.md`; `R54ReviewProvince` (no sibling claim); lesson `## Gate`.

## Round shape, stale lane, tooling, L0

- **Shape:** two v1 waves. The L1 held the planner seat.
  - **W1:** 49 seats (15 scribe, 14 executor, 6 critic, 5 reviewer, 3 scout, 2 mutation-tester, 2 connector, 1 sentinel, 1 simplifier). WAVE-DONE was received and `w1-results.json` is committed. 44 seats wrote reports. R54ExecNegSweep, R54ExecPdfForm and R54SentCounters went silent and the orchestrator cancelled them. R54CritSeparable and R54ConnSiblings died on a refused model fallback.
  - **W2:** 38 seats (14 executor, 8 critic, 5 reviewer, 4 scribe, 2 mutation-tester, 2 connector, 1 sentinel, 1 simplifier, 1 scout), dispatched (`w2.ready.dispatched`).
  - **The report was filed before W2 WAVE-DONE,** under the run's request-budget wrap. That is a conformance defect, disclosed here: W2 findings are not integrated, and no falsification credit is taken from W2.
  - Total dispatched: 87.
- **Routing:** the mid-round map changes were reported by the orchestrator. `model` was never passed.
- **Stale-lane:** respawn-per-round. This lane holds no other mission.
- **Misroot sweep:** the fleet-root untracked files are `.ufo/reports/round-45/kengaku.md` and `.ufo/waves/round-51/w2/T51W2Read14.md`, both from other lanes and left untouched. No chousa misroot.
- **Tooling:** no install. `pypdf` was run ephemerally with `uv run --with pypdf` (PyPI) for the independent PDF check. LibreOffice is the existing system install.
- **L0:** `8d77e6c1` (fetch scope) is still open. No new question.
