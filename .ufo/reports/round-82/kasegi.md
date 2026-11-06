# kasegi — round 82 report (attempt 1)

Lane HEAD `4576a88e85d0ee67197cf36f9f2b533040b840dd` (master, pushed; `git ls-remote origin refs/heads/master` prints it). Base `1a50638edabb9bd1a4a4784774fc984cb5f2360f`, freeze `b9589300810a477f4d6794bfabc24b22fb50b846`, landing `4576a88e` (it also carries the wave evidence and results).

## Work performed

Declared claims (frozen in `.ufo/waves/round-82/claims.json` at `b9589300`):
- **C1 — depth:verifiability (lowest non-retired axis, 4, nominal per R58; the scored `resolve.py` census does not read this instrument):** land the recheck-cwd census successor `81677e9d…e050`. It adds `conform_ok` with a bucket-sum conjunct used by `main()`, plus two checks, bucket-sum and main-default. It is scored by a new r82 counter with a counter-owned decoy limb (D1 `ast.unparse`, D2 local-identifier rename) over a 63-row table: the 59 r81 rows (S04/S05 re-anchored) plus J1 (the r81 junk edit), S07M (the main()-site survivor), B1 and B2. Two table-reading forgeries (F6, F7) that the r81 counter scores rc 0 must exit 1 under the r82 counter. F8 (AST-embedding) is the declared limit. **VERIFIED (P1–P9)**, with the limits below.
- **C2 — coverage (8):** admit Frontier F58 on S116 (OSV.dev "Properties of a High Quality OSV Record", opened this round; the round's sourced claim). An r82 entry gate with a content limb (G5) must reject the r81 labelled six-quote dump that the r81 gate passed. **VERIFIED (B0–B8).**

Work items:
- History read before the freeze: r81 closure (admitted), `corpus/lessons/round-81-verifier-spotcheck.md` routed defects 1–7.
- Candidate `.ufo/waves/round-82/c1/recheck-cwd-census.py`, counter `c1/mutbat.py` (`a7d4db43…`), builder `c1/build-table.py`, table `c1/mutant-table.json` (`045edc07…`), forgery driver `controls/c1-forgeries-r82.py`, entry gate `c2/entry-gate.py`.
- Controls executed and committed in the freeze (`.ufo/waves/round-82/controls/`):
  - r81 bytes under the r82 counter: `baseline=bad killed=54 survived=2 notderived=4 neutral_ok=0/3 decoy=broken`, rc 1 (`c1-donothing-r82.txt`)
  - candidate: `killed=60 neutral_ok=3/3 decoy=ok decoy_hidden=59/60`, rc 0 (`c1-candidate-r82.txt`)
  - r81 junk edit conformant rc 0 on the lane; J1-edited candidate nonconformant rc 1 (`c1-junkedit-r82.txt`)
  - F6/F7 rc 0 under r81 and rc 1 `decoy=broken` under r82; F8 rc 0 under both (`c1-forgeries-r82.txt`)
  - C2: S116 recheck OK, base knowledge 95, frontier 57, literal sweep 0 (`c2-prefreeze-r82.txt`); labelled dump r81 gate pass / r82 gate fail, F57/F56/F55 entries pass r82 (`c2-b8-controls-r82.txt`)
- Captured S116 (`corpus/source-snapshots/round-82/S116.txt`, sha256 `2198d329…9ca0`, HTTP 200) with a six-quote manifest.
- Wave `w1` (12 seats) scored and attacked both claims; reports in `.ufo/waves/round-82/w1/`. Entry fixes applied before landing: ExecC2Gate D1, ReviewC2 H1/M1–M4/L1–L4/N1, ScoutDistinct D1/D2 (B8 re-run: pass).
- Landing receipt `.ufo/waves/round-82/l1/L1-landing-r82.txt`: 9× `FROZEN-OK`; P1–P9 and B0–B8 all hold.
- Wave findings that falsify parts of the claims' prose (frozen predicates hold; recorded, routed to r83):
  - **CriticClaims F1:** the counter names mutant temp dirs after the row id (`mutbat.py:221`) and decoy dirs `mutbat-decoy-` (`:189`). A path-reading forgery scores rc 0 under r82 (`w1/CriticClaims-receipts/mutbat-pathforge-table.txt`). F8 is therefore not the only residual class. Mined as M82-2, with a fix shown to fail and to pass (`l1/M82-2-constprefix-r82.txt`: constant prefix → forgery `killed=0` rc 1, candidate still rc 0).
  - **ReviewC1 Major 1:** the decoys are unkeyed. A hash-whitelisting forgery would pass; this is simulated, `[INFERENCE]`.
  - **CriticClaims F2:** P1/P5/P6/P8 are stub-satisfiable; P2's pin carries the anti-junk force.
  - **CriticClaims F4 / MutEntryGate:** G5 is lexical. Filler, boilerplate and copied rules pass; 8/14 G5 mutants survive.
  - **MutC1Hunt:** 22 rows, 14 killed, 4 real gaps (G1–G4).
  - **MutCounter:** 18 decoy-limb mutants, 8 survive; none makes a frozen predicate false.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: claims, c1 bytes, c2 gate, controls, assimilation check, S116 snapshot + manifest, S116 row `queued` | LOG.md `## Round 82` bullets 1–2 | `b9589300810a477f4d6794bfabc24b22fb50b846` |
| `corpus/instruments/recheck-cwd-census.py` → `81677e9d…`; SKILL.md and instruments/README pin rows `cases=24` | LOG.md `## Round 82` bullet 4 | `4576a88e85d0ee67197cf36f9f2b533040b840dd` |
| F58 entry `corpus/knowledge/osv-high-quality-record-import-bar.md`; S116 `mined`; knowledge-expected; README F58 rows; PROVINCE F58 line; two new leads | LOG.md `## Round 82` bullet 5 | `4576a88e` |
| Appended correction in `corpus/knowledge/osv-determineversion-cc-library-versioning.md` (r81 routed defect 1) | LOG.md `## Round 82` bullet 6 | `4576a88e` |
| `corpus/lessons/round-82.md` (M82-1, M82-2, M82-3); QUALITY R133; SCORECARD `## Round 82`; wave spec/dispatch/results/seat reports; L1 receipts | LOG.md `## Round 82` bullet 7 | `4576a88e` |

## Before → after measurements

- **C1** (measured at landing `4576a88e`). Counting command: `python3 -B .ufo/waves/round-82/c1/mutbat.py --target corpus/instruments/recheck-cwd-census.py --table .ufo/waves/round-82/c1/mutant-table.json --expect-cases 24 --work $SCRATCH`
  - Before (base `1a50638e`, r81 bytes `a3b58aa5`): `baseline=bad rows=63 killed=54 survived=2 miskilled=0 dirty=0 notderived=4 neutral_ok=0/3 decoy=broken`, rc 1
  - After: `baseline=ok rows=63 killed=60 survived=0 miskilled=0 dirty=0 notderived=0 neutral_ok=3/3 decoy=ok decoy_hidden=59/60`, rc 0
  - Selftest `cases=22` → `cases=24 failures=0`
  - J1 junk edit on the lane: conformant rc 0 (r81) → nonconformant rc 1 (r82)
  - F6/F7: rc 0 (r81 counter) → rc 1 (r82 counter); F8 rc 0 under both (declared limit)
  - Score 4 → 4 (nominal per R58)
- **C2** (measured at landing `4576a88e`). Counting command: `python3 corpus/instruments/frontier-recheck-count.py | grep FRONTIER-CENSUS ; ls corpus/knowledge/*.md | wc -l ; grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  - Before (freeze `b9589300`): `rows=57 admitted=57 … registry=116`, knowledge 95, S116 `queued`
  - After: `FRONTIER-CENSUS rows=58 admitted=58 closed=58 problem-rows=0 registry=116`, `FRONTIER-PASS F58 ids=S116`, knowledge 96, S116 `mined`
  - B8: entry `ruleless=0` pass; labelled dump `ruleless=6` fail rc 1
  - Score 8 → 8 (the coverage denominator is operator-owned)
- **No axis harmed:**
  - depth:density SKILL.md mean 272.8 before and after
  - SCORECARD/LOG additions only

## Sources & frontier

- **Census command:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`
  - Round start: `kasegi ok`, six inherited W04 (S028 S029 S072 S076 S080 S085), rc 0 (`.ufo/waves/round-82/controls/census-start-r82.txt`)
  - Round end (after landing): `kasegi ok`, the same six W04, rc 0
- **Registry rows:** 115 → 116 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). One row added, tier A `docs`: **S116**, OSV.dev data_quality page, opened 2026-11-06, HTTP 200.
- **Rows touched (old → new):** S116 status `queued` → `mined`; used-by `—` → `corpus/knowledge/osv-high-quality-record-import-bar.md`. Logged in SOURCES `## Registry changes` and in the lesson.
- **Frontier advanced:** F57 → F58. This opened the r81 lead "Properties of a High Quality OSV Record".
- **New leads (unopened):** "Managing the Perishability of OSV Records" (S116.txt:27) and the OSV JSON Schema artifact (S116.txt:64).
- **Sourced claim:** C2 rests on S116.
- **Mistakes mined** (`corpus/lessons/round-82.md`):
  - M82-1 `scribe-placeholders-landed-in-gate-body`: check prints 18 on round-81.md and 0 on round-82.md; backs QUALITY R133.
  - M82-2 `harness-leaks-verdict-label-to-target`: constant-prefix fix rejects the path forgery and passes the candidate.
  - M82-3 `stated-command-output-not-run`: stated-output check fails on the draft Limits line and passes the landed entry.
- **Assimilation: none.** 116 registry ids, 94 staged, 86 collisions (`.ufo/waves/round-82/assimilation/`); r77 L0 question pending. ConnectorOverlap shows the count tracks id labels, not sources: 1 same-source pair, 85 different-source pairs, 20 same-source pairs missed.
- **considerthese:** read by ConnectorOverlap; no still-unimplemented `2026-10-26.md` proposal fits.

## Trend verdicts

- **expansion: improved.** F58 adds ground the corpus did not hold: OSV.dev's import bar for a record. Literal sweep of the six quotes over the 95 other entries = 0. Frontier 57 → 58, knowledge 95 → 96. ConnectorOverlap: no sibling lane holds this page.
- **quality: improved.**
  - The landed gate kills 60/60 case-matched mutants plus both decoys, against `baseline=bad killed=54` on the base bytes.
  - The r81 junk edit is now nonconformant.
  - The r82 counter rejects two forgeries the r81 counter accepted.
  - Carried limits, recorded rather than hidden: the path-label forgery (M82-2), the unkeyed decoys, G5 being lexical, MutC1Hunt G1–G4.
- **discernment: improved.**
  - Seat findings were applied before landing; each is grounded by a re-run command: D1/H1 Limits receipt, Appendix A attribution, the self-matching sweep.
  - The r81 spot-check's routed defects 1 and 6 became an appended correction and R133.
  - Needs the non-author closure check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: SKILL.md; recheck-cwd pin row updated this round (`SKILL.md:982`); author assertion.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched (`corpus/lessons/round-61.md`).
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-47-verifier-spotcheck.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` F58 line appended within OSV ground (ConnectorOverlap: lane-unique, fits by precedent).

## Round shape and other items

- **Shape:** one v1 wave `w1` of 12 seats (`w1-results.json`: `seats 12`, 12 outputs).
  - Roles: executor×3, scribe×1, scout×1, reviewer×2, mutation-tester×3, critic×1, connector×1.
  - Attack seats: 6/12.
  - Dead seats: 0.
  - No residual call. Round total: 12.
- **Planner seat:** held by the L1, because the validator rejects `planner`.
- **Routed to round 83:**
  - counter: constant run-dir prefix, keyed decoys, path-guard toy
  - MutC1Hunt G1–G4
  - a G5 limb that ties each rule to its cited line
  - the stated-output check as a lane instrument
  - lead: Perishability page
- **Misroot sweep:** `git status --porcelain` on the fleet root shows only orchestrator `.scratch/` entries; no kasegi misroots. Scratch `/fast/scratch/hyaku/kasegi-r82` was removed.
- **Inherited state:** none; the lane was clean at round start. No earlier attempt of r82 in the watchdog log.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Open L0 questions:** r77 staged-package id collisions (R-77-E) and the source-recheck anchor window (R-77-D), both carried and not re-filed.
