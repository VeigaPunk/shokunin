# kotodama — round 55 report (hyaku phase 4, attempt 1, L1 KotodamaR55)

Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. The lane tip is `2935c47011049527842b6d3f08691d9629c3b983` (jj-lane helper `landed`). The round started from base `89973ba7`. The claim base is `f4015e7` and the declaration is `8eda954`. No earlier attempt of this round was logged as dead.

## Work performed

**Declared claims (2):**
- **C — coverage.** A learning claim and the round's sourced claim: one new entry, `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md` (monsters and hybrid beings as a cultural category). Knowledge files go from 230 to 231. Acceptance is `python3 -B reports/round-55/accept-c.py`, with seven legs.
- **O — operability.** A capability acquisition, the Gate-line shape checker. `tools/check-gate-quotes.py` now reports the round-54 closure's two routed shapes (`doubled-locator` and registry-backed `truncated-grounds`) and four of the five carried escape shapes. Acceptance is `python3 -B reports/round-55/accept-o.py`, with eight legs.
- **Lowest-axis note.** Freshness stays paused by the open round-11 L0 question (`reports/round-55/claims.json` `lowest_axis_note`).
- **Drift sentinel.** C works myth-symbol ground; rounds 51–54 worked linguistics and culture-material.

**Work items:**
- **Instruments and declaration.** Instruments landed at `d44309a`. Two pre-dispatch critics found defects (`.ufo/waves/round-55/predispatch/CriticClauseListC.md`, `CriticClauseListO.md`): untested SWEEP conjuncts, and an acceptance script that a bad checker could pass. The instruments were revised at `f4015e7` and the declaration at `8eda954`. Receipts: C controls 14/14 (`reports/round-55/telemetry/criterion11-controls.txt`), O controls 16/16 (`criterion11-controls-o.txt`), and the dry-run two-way check exit 0 (`declaration-dry-run.txt`).
- **Spot-check routing** (`corpus/lessons/round-54-verifier-spotcheck.md`):
  - `ExecIntegrateRows.md` committed as late-seat evidence (`d44309a`).
  - Full-grounds errata for the 17 truncated rows and the 13 doubled-locator rows, in the `corpus/lessons/round-55.md` errata section.
  - S358 supersedes S256's tier, A → B.
  - Anchors S248, S254 and S275 corrected (`b9c44a2`).
  - Four of the five escape classes now caught by claim O.
  - Carried items fixed: gesture line 68 (`b9c44a2`), speech-surrogates line 79 (`81178c8`), and divination line 72, a Cicero misattribution found by the gap critic (`d52c9df`).
  - Not landed, and carried to Frontier: the S135–S159 superseding rows, and the `[S95]` entry-local key class.
- **Build wave `kotodama-r55-build`, 51 seats** (`.ufo/waves/round-55/build/`): 32 scouts, 6 reviewers, 4 critics, 3 connectors, 3 executors, 3 scribes.
  - The scouts opened 97 source blocks.
  - ExecGateShapes built the checker.
  - ExecIntegrateRows55 built a Gate generator that never cuts a Grounds.
  - CriticMistakeMining traced round 54's defects to a 220-character cut in the Gate generator plus a greedy quote parse.
- **C landed `eb0a331`.** The entry is 186 lines and cites 73 rows opened this round (S285–S357), with a §11 handoff to lore's world bible. Lore has no creature section, so beings travel as proposal-only myth-symbol register payloads under `synthesis/worldbible-integration-contract.md`, NON-CANON until lore receipts them.
- **O landed `454a2dc`.**
- **Falsify wave `kotodama-r55-falsify`, 33 seats** (`.ufo/waves/round-55/falsify/`): 23 reviewers, 6 critics, 3 mutation-testers, 1 executor.
  - Both acceptance commands and both control receipts re-ran byte-identically.
  - Mutation testing killed 12 of 12 mutants.
  - About 40 citing-sentence over-reads and wrong locators were fixed in the records commit `173cab6`: §10 restricted beings rewritten, §11 lore anchors, §14 calibration codes (griffin R→C, among others), and the Polesye and Mami Wata hedges.
  - The checker was hardened: Wayback access notes, `* S###` rows, docstring boundaries, selftest 24 → 27.
  - Five seats were cancelled unreported (see Round shape).
- **Mistakes R55-M1 to R55-M6** are in `corpus/lessons/round-55.md#mistakes`.

## Landed changes

All commits were landed by the jj-lane helper after remote verification.

| commit | what | LOG.md entry |
|---|---|---|
| `d44309a1031431506bded6a252d64805f234c94d` | instruments, start census, round-54 late seat report | round 55 |
| `662239d2c8fcb9a2b7f9ac297ca2283f36397c14` | first declaration | round 55 |
| `f4015e70b829523ed81e14ce4279bfab0e0233e4` | instruments revised after the pre-dispatch critics (claim base) | round 55 |
| `8eda9543e940bdc4938fad90182ee6a6fe271d0f` | declaration, control receipts, dry-run receipt | round 55 |
| `b9c44a218820fbe5d2befb7448a229207873bbc6`, `81178c8f42dfafdc501e2cfeb41b4ff55c31571d`, `d52c9dffbecdd957596521cc19783cc3fac12c20` | routed fixes, not claims | round 55 |
| `454a2dc813c8e4caa0b3811266bbf8864e7286f5` | claim O | round 55, O |
| `eb0a331786abee5a019308ec2ce10f141a33257b` | claim C: entry, README rev 2.12, SOURCES S285–S357 | round 55, C |
| `173cab67364b91717516963f5991ce1a4f7a331e` | records: falsify fixes, S358, lesson, lessons index rev 12, SCORECARD, LOG, SHONEN, final measures, wave records | round 55 |
| `2935c47011049527842b6d3f08691d9629c3b983` | SHONEN line 6 and SCORECARD frontier line: measured status split 313/35/10 | round 55 |

## Before → after measurements

- **C:** `python3 -B reports/round-55/accept-c.py`.
  - Before, at `f4015e7`: exit 1. SET FAIL (count 230), SWEEP FAIL (rows 230 files 230) and FLOOR FAIL (cited 0).
  - After, at `eb0a331`: exit 0. All seven legs pass: count 231, rows 231 files 231, cited 73, ACCESS pass. This was re-run by RerunAcceptC.
  - Also exit 0 at `173cab6` (`reports/round-55/telemetry/final-measures.txt`).
- **O:** `python3 -B reports/round-55/accept-o.py`.
  - Before, at `f4015e7`: exit 1. DOUBLED 0, TRUNC 0, EXIT FAIL, ESCAPE 4 missing.
  - After, at `454a2dc`: exit 0. All eight legs pass: exactly the routed 13 and 17 rows, ESCAPE S901, S902, S904 and S905, and selftest 24/24. This was re-run by RerunAcceptO.
  - Also exit 0 at `173cab6`, with selftest 27/27.
- **Separability, defect disclosed:** `python3 -B tools/check-claim-separability.py reports/round-55/separability-manifest.json` exits 1 at the landed tree.
  - The static finding is O→C: C's export regex was declared as S285–S999, and it matches the selftest fixture id S900 inside O's tool. This is a false dependency from an over-broad declared input (R55-M5).
  - CriticClaimC showed that the exact-range regex exits 0. The manifest was not re-declared after measuring.

## Sources & frontier

- **Census at round start:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, `ok`, 9 W04 warnings (`reports/round-55/telemetry/census-start.txt`).
- **Census at round end:** the same command → exit 0, `ok` (`final-measures.txt`).
- **Rows:** 284 → 358 (`grep -cE '^\| S[0-9]+ ' corpus/SOURCES.md`).
  - Added: S285–S357, 73 rows, all `mined` and used-by the entry. By tier: A 56, B 17.
  - Added: S358, `queued`, used-by `—`. It supersedes S256's tier.
  - Status totals moved from 240/34/10 to 313/35/10.
- **Rows touched old → new, logged in the lesson:**
  - Anchor cells of S248, S254 and S275.
  - Scope cells of S278 (a draft id corrected to S277) and S342.
  - The S313 teaches cell: "headless" tripped the access checker.
  - The teaches cells of S311, S325, S330, S332 and S349 after falsify.
- **Gate:** 74 lines, `check-gate-quotes.py` → 0 findings. Grounds are whole teaches cells.
- **Mined mistake:** R55-M1, the integration-shape class. Its fix is claim O, shown able to fail.
- **Sourced claim:** C.
- **Frontier rows advanced:** monsters and hybrid beings now have an owner.
- **Misroot sweep:** one seat report (ScoutWondersEast) had been written to the fleet root. It was moved byte-exact into the lane (`cmp` equal) and the fleet copy deleted (R55-M2). The fleet status shows no other file written by this round's seats.

## Trend verdicts

- **expansion: improved.** A new owner for unowned ground (0 filename owners at base), 231 files, 73 new mined rows, and one new capability.
- **quality: improved, bounded.** All acceptance legs pass, mutation testing killed 12/12, and about 40 falsify findings were fixed. Bounds: the declared separability command exits 1 (false finding, R55-M5); five falsify slices went unreported (S290–S294, S305–S309, S320–S324, S355–S358, and the Gate-line seat); several checker limits are carried (KEEP53 scope, entity decoding).
- **discernment: improved.** The checker turns the closure's routed shapes into mechanical findings. It uses a registry-backed rule rather than the closure's regex, which would have given 165 false positives on rounds 51–53. The pre-dispatch critics caught a passable acceptance script before dispatch.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SHONEN.md:6` updated to 358 rows and 313/35/10 (`2935c47`). No non-author verifier is on record.
- [~] End-to-end domain task logged in LOG.md — `LOG.md`, round-55 entry (sources → entry → falsify → fixes `173cab6`).
- [~] Instructions executable without oral context — falsify seats re-ran every counting command from committed paths in sandbox clones (`.ufo/waves/round-55/falsify/Rerun*.md`).
- [~] No cross-domain bleed — `.ufo/waves/round-55/build/ConnectSiblingMonsters.md` found no sibling owner. Canon stays with lore (entry §11).

## Round shape and seats

- **Shape:** the default two v1 waves, plus one pre-dispatch call.
  - Pre-dispatch call: 2 critic seats. This is the criterion-11 non-author check, counted as a residual call.
  - Build wave: 51 seats.
  - Falsify wave: 33 seats.
  - Round total: 86.
- **§3 L2 floor:** met in the build wave. The L1 holds the canonical planner seat, and the planning data-walk rode ScoutEntryMechanics and ConnectInLaneMonsters.
- **Dead seats:** none died. No refusals or holds.
- **Cancelled at wrap-up, never reported:** ReviewRowsS290toS294, ReviewRowsS305toS309, ReviewRowsS320toS324, ReviewRowsS355toS358 and ReviewGateLines55.
- **Late report:** ScoutYokaiScholarship reported after integration and is not cited.
- **Exclusion:** `kotodama51-prereg-critic` was not recreated.
- **Tool installs:** none by the L1 or any reporting seat; the pacman pause was respected.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Open L0 questions:** none new. The round-11 freshness question stays open.
