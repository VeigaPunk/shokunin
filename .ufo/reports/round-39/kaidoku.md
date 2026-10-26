# kaidoku — round 39 report

L1 `KaidokuR39` holds the §3 planner seat. Lane: `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`. Base `a2f64e1da78afcf8cc39287106604dbcc270844c`, final lane hash `8b9634ed8253653e7eb994aad9860a624e3b0366`. This is attempt 1; the watchdog has no earlier `lane-dead-no-report kaidoku round=39` line, so nothing was inherited.

## Work performed

The round declared two claims. Both were frozen at `8fcda41c96cbf00b113d2c8e136cc14e7fcaba0b` (`plans/round-39-claims.md`):

- **R39-C1 — coverage.** Standard big-endian SquashFS v4 (`squashfs_v4_be` through `sasquatch-v4be`, REA `extract-firmware`) moves from PROVINCE Frontier to Core. It is measured on six frozen carriers, and the symlink rule is stated before any data. This is the round-38 `planned` row.
- **R39-C2 — depth.** SKILL `## Queue-drain craft` gains rule block 18, an executable SquashFS `extract-firmware` outcome-triage table. A frozen interpreter scores it on a held-out set whose seed is the freeze commit hash.

Work items:

- **Wave 1 (43 seats): pre-freeze build, recon and attack of the draft** (`.ufo/waves/round-39/w1/`, committed in the freeze).
  - Carriers K5 (BE gzip, UTF-8 names, 2 in-tree + 1 escaping link) and K6 (BE xz, compression id 4, 4 compressed xz blocks): `corpus/evidence/round-39/c1/K5,K6/`.
  - An independent SquashFS reader, `tools/round-39/sqfs-list.py`.
  - Symlink tables for K1–K6.
  - Counters `tools/round-39/c1-counter.py` (selftest 33 cases) and `tools/round-39/c2-counter.py` (27 cases), and the interpreter `tools/round-39/sqfs-triage.py` (35 cases).
  - The held-out generator `tools/round-39/heldout-gen.py`.
  - Recon of eight outcome classes on development carriers.
  - Attacks on the draft forced five freeze changes (`plans/round-39-claims.md` `## Changes from the draft`):
    - extraction-root symlink semantics, because the draft's POSIX clamp would have failed K1;
    - a run-provenance clause;
    - symlink-coverage and xz-leg bindings;
    - a fixed carrier writer, `tools/round-39/gen-squashfs.py`, after UTF-8 and xz defects in the round-37 writer;
    - the class set.
- **Controls before data** (`72359309a052284029f8e0331ef211a67fe4b13b`, `.ufo/waves/round-39/controls/`). No control meets either target.
  - C1, nine controls (do-nothing; round-38 receipts copied; fabricated with old ids; materialised link; wrong gap kind; and others): all exit 1.
  - CTL-C1-3, a re-minted fabrication, reaches 6/6 carriers. It fails only on a documentation binding, which is the limit disclosed in the freeze.
  - C2, eight shortcut tables run on 20 development envelopes: best 12/20, and the base SKILL scores 0.
- **Data.**
  - C2 held-out set: 20 carriers, seed = the freeze hash, REA run in each class's arm (`3c07eed7da595b815ce3064dcb12bd5c0788e564`, `corpus/evidence/round-39/c2/heldout/`).
  - C1: six after-receipts from `tools/round-39/c1-run.sh after`, the Core row, the round-39 frontier note, the entry `corpus/knowledge/2026-10-26-r39-be-squashfs-v4-core.md`, README rows and S122 (`6fdaf4f162aff156fcef0e52998a5469c64fd6f0`).
- **Frontier step and routed defects** (`52b0eb2907c704ed5f184c47b14c723208e5cbbc`):
  - Lesson `corpus/lessons/round-39.md`, with M39-1..M39-10, the Gate, corrections to round 38 and a routed-defect ledger.
  - QUALITY 82 (`corpus/QUALITY.md`), with its gate `tools/round-39/absence-sweep.py`. On the round-38 claims, a fleet-root-only sweep exits 0; adding the shokuknow root exits 1 (`.ufo/waves/round-39/l1/absence/summary.txt`).
  - `--selftest` added to `tools/round-38/{freeze-drift.py,intended-doc.py,registry-immutable.sh}` (8, 9 and 5 cases).
  - SKILL `### Round-35/37/38/39 instrument registry`.
- **Wave 2 (39 seats): falsify the landing** (`.ufo/waves/round-39/w2/`). Neither claim was falsified:
  - Six independent REA re-runs reproduce every C1 receipt (`w2/R39W2ReproK{1..6}.md`).
  - Four seats reproduce all 20 held-out envelopes and their labels (`w2/R39W2HeldRepro{A,B,C,D}.md`).
  - K5/K6 rebuild byte-for-byte, and the held-out set regenerates from the seed.
  - The claims are separable (`w2/R39W2Separability.md`).
  - Defects found, and the repairs landed in `2b0b6a29578c0b8917f677321557d96a444e994e`:
    - SCORECARD/LOG were not yet updated;
    - PROVINCE `:157` and `:376` still said BE stays Frontier;
    - S112 used-by was missing the triage entry;
    - the registry-immutable registry cell was wrong;
    - entry wording;
    - one misrooted report;
    - late post-freeze edits by two wave-1 seats.
  - Kept open with their pointers: see Trend verdicts and the lesson's `## Wave 2`.

## Landed changes

All on lane `main`. LOG entry: `LOG.md`, `## 2026-10-26 — round 39 …` (the last section).

| commit | what |
|---|---|
| `8fcda41c96cbf00b113d2c8e136cc14e7fcaba0b` | **Freeze**: claims; `tools/round-39/*`; carriers.json; K5/K6 carriers, oracles, src and symlink tables; SKILL triage block (rule 18); triage entry; README rows; SOURCES S118–S121; census start; wave-1 spec, dispatch and reports |
| `72359309a052284029f8e0331ef211a67fe4b13b` | pre-data control receipts (C1 ×9, C2 ×8) and the wave-1 results ledger |
| `3c07eed7da595b815ce3064dcb12bd5c0788e564` | R39-C2 held-out data (manifest and 20 envelopes) |
| `6fdaf4f162aff156fcef0e52998a5469c64fd6f0` | R39-C1 receipts K1–K6; `## Round-39 additions to Core`; frontier note; BE entry; README rows; S122 |
| `52b0eb2907c704ed5f184c47b14c723208e5cbbc` | lesson, QUALITY 82, SKILL instrument registry, round-38 gate selftests, R36-CL2 pointer, scores at `6fdaf4f1` |
| `e40a25df3987d881513de581112d2dad30605673` | wave-2 spec, generator and validated dispatch |
| `2b0b6a29578c0b8917f677321557d96a444e994e` | wave-2 repairs: SCORECARD `## Round 39` with owned-axes and capability rows; SHONEN; LOG; PROVINCE pointers; S112 used-by; entry notes; lesson M39-9/10 and `## Wave 2`; wave-2 reports; end census; post-freeze-edit quarantine |
| `8b9634ed8253653e7eb994aad9860a624e3b0366` | final wave-2 report, wave-2 results ledger, scores at `2b0b6a29` |

## Before → after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| R39-C1 | `python3 -I -B tools/round-39/c1-counter.py --root <lane> --rev <REV> --freeze 8fcda41c96cbf00b113d2c8e136cc14e7fcaba0b --pkg65 /home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents --json-out <OUT>` | `carriers_matched 0`, `met_target false`, exit 1 at the freeze (`.ufo/waves/round-39/controls/ctl-c1-0-do-nothing.json`) | `carriers_matched 6`, every binding true, `frozen_path_changed []`, exit 0 (`.ufo/waves/round-39/l1/scores/c1-at-6fdaf4f1.json`); same at `2b0b6a29` (`c1-at-2b0b6a29.json`) | `6fdaf4f1`, `2b0b6a29` |
| R39-C2 | `python3 -I -B tools/round-39/c2-counter.py --root <lane> --rev <REV> --freeze 8fcda41c96cbf00b113d2c8e136cc14e7fcaba0b --json-out <OUT>` | exit 2 `no_manifest_at_rev` at the freeze (`l1/scores/c2-at-freeze.json`); the base SKILL has no table and the interpreter exits 2 (`controls/ctl-c2-dev-scores.json` `CTL-C2-0`) | `matched 20` of `n 20`, every binding true, `met_target_consistent`, exit 0 (`l1/scores/c2-at-6fdaf4f1.json`); same at `2b0b6a29` | `6fdaf4f1`, `2b0b6a29` |

**Verdicts (author):** R39-C1 **met**; R39-C2 **met**. Admission is the closure's call.

Disclosed limits:

- **C1 counter.** It cannot refuse a fabricated receipt with a re-minted evidence id (`w2/R39W2C1Fabricate.md`). C1's provenance therefore rests on the six independent re-runs.
- **C2 depth increment.** Wave 2 contests it (`w2/R39W2C2AxisFit.md`):
  - the depth proxy was already saturated (17/17 → 18/18, score 10 → 10);
  - a table with no `-be` and no symlink-removed cell reaches 16/20, so those two features decide 4 envelopes;
  - the cause → action column is not scored.

**Owned scores:**

- coverage 10 → 10 (map 126/126 → 128/128);
- depth 10 → 10 (18/18 rule blocks; command A at `2b0b6a29`);
- calibration 10 → 10.

No axis is harmed (`w2/R39W2HarmCheck.md`; the stale self-assessment statements it found were restated in `2b0b6a29`). Two capability rows entered: BE SquashFS v4 recursion, and executable outcome triage.

## Sources & frontier

- **Census** (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`):
  - start: exit 0, 11× W04 (`.ufo/waves/round-39/census-start.txt`);
  - end: exit 0, 12× W04 (`.ufo/waves/round-39/census-end.txt`). The new warning is S119's cross-scope reuse of the rea-agents 6.5.0 tarball URL.
- **Rows:** 117 → 122 (`grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md`). All five added are tier A, `mined`, opened 2026-10-26:
  - S118: unblob `extractor.py`, the symlink sanitiser;
  - S119: the rea-agents 6.5.0 tarball, gap schema;
  - S120: unblob `report.py` and `command.py`;
  - S121: sasquatch `unsquashfs.c` at `sasquatch-v4.5.1-6`;
  - S122: unblob `file_utils.py` `is_safe_path`.
- **Rows touched old→new:** S112 used-by `corpus/knowledge/2026-10-26-r38-sasquatch-be-squashfs-recursion.md` → that entry plus `corpus/knowledge/2026-10-26-r39-sqfs-outcome-triage.md`. Logged in the lesson's Gate; `registry-immutable.sh` permits used-by changes.
- **Frontier advanced:**
  - The PROVINCE Frontier sasquatch bullet's big-endian part is superseded by `## Round-39 additions to Core`, with dated pointers at `PROVINCE.md:157` and `:376`.
  - The README `## Frontier` has a round-39 line.
  - AVM-BE bodies and vendor-mangled images stay Frontier.
- **Sourced claim:** the R39-C1 entry cites S122, and the R39-C2 entry cites S118–S121. All of these rows were opened this round.
- **Mined mistakes:** M39-1..M39-10 in `corpus/lessons/round-39.md` `## Mistakes`, each with a fix that can fail. Examples: R38-CL1 false absence → QUALITY 82 and `absence-sweep.py`; routed-ledger lapse; uncommitted wave checkpoint; the draft symlink-clamp error; writer defects; misroots.
- **Round-38 spot-check (`corpus/lessons/round-38-verifier-spotcheck.md`):** R38-CL1..CL4 are fixed and the routed ledger records them. R36-CL2/4/6 are fixed, R36-CL3 is superseded, and R36-CL5 is still open.
- **Assimilation: none adopted.** Theme AVM, from `merge/kaidoku/`:
  - Rejected: `avm-image-build-blocker` and `avm-le-variant-reachability`.
  - Deferred: `avm-firmware-image-unblob` and `avm-image-extraction`, where the two wave-1 seats disagree.
  - The quarantine slice is 5 rows, byte-identical to round 38. Wave 2 found that S150's "refuse" should be "re-anchor"; this is recorded in the lesson.
- **considerthese:** no `considerthese/` directory exists in this lane.

## Trend verdicts

- **expansion: improved** (author). Standard BE v4 is now Core on six carriers, including two new ones:
  - K5, with UTF-8 names and two in-tree links;
  - K6, with real xz compression.

  Both new entries are mapped (128/128). AVM-BE was not touched.
- **quality: improved** (author).
  - Every C1 receipt and held-out envelope was reproduced independently.
  - The round-38 false-absence claims were corrected, and QUALITY 82 carries a gate.
  - Three QUALITY-bound gates gained selftests, and the instrument registry was completed.
  - Still open:
    - the `heldout-gen.py` `corruption_bad_minor` docstring erratum (frozen bytes);
    - four minor triage-entry citation-precision items (`w2/R39W2C2EntryReview.md`);
    - surviving interpreter and counter mutants (`w2/R39W2TriageMutants.md`, `w2/R39W2C2Mutants.md`);
    - two loose source quote anchors (`w2/R39W2SrcReopen.md`).
- **discernment: improved** (author; outside spot-check pending).
  - Five draft defects were caught before the freeze. One of them, the clamp, would have failed an honest carrier.
  - The re-minted-fabrication limit was disclosed instead of listed as a kill control.
  - The AVM entries were deferred where the seats disagreed.
  - The wave-2 limits of the C2 table are recorded against interest in the entry and the SCORECARD.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:81-343` (18/18 rule blocks resolve; rule 18 is the executable triage table, interpreter selftest 35/35). `SHONEN.md:6`. No non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — REA `extract-firmware` on six BE v4 carriers, receipts `corpus/evidence/round-39/c1/`, LOG round-39 entry, reproduced by wave-2 seats `w2/R39W2ReproK*.md`. These seats were dispatched by this lane, so they are not outside verifiers.
- [~] Instructions executable by an agent without oral context — the SKILL triage table runs through a frozen interpreter and labels 20/20 held-out envelopes (`SHONEN.md:10`). No outside verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:97-125` Adjacent is unchanged. The round-39 Core row and frontier pointers are at `:157`, `:376` and `:378-384`. No promotion verifier.

## Round shape, seats, extras

- **Shape:** two v1 waves (policy `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`), both dispatched through the inline spawn handoff.
  - **Wave 1** `r39-w1`: 43 seats — executor 18, scout 7, critic 6, reviewer 3, scribe 3, connector 2, revenger 1, mutation-tester 1, sentinel 1, simplifier 1. Ledger `.ufo/waves/round-39/r39-w1-results.json`; 43/43 reports.
  - **Wave 2** `r39-w2`: 39 seats — executor 14, critic 6, reviewer 6, mutation-tester 5, scout 2, connector 2, scribe 2, sentinel 1, simplifier 1. Ledger `r39-w2-results.json`; 39/39 reports.
  - **Round total:** 82 seats. No residual call.
  - **Dead seats:** 0, judged by report presence; the ledgers' per-seat `status` field is null for every seat.
  - The L1 holds the planner seat; `labrat` and `planner` are not swarm roles in the validator, so falsifiable probes rode executor seats.
  - Routing: the run-8 role map; no `model` was passed.
- **Misroot sweep:** wave-2 seat `R39W2HeldReproB` wrote its report to `/home/vgpnk/Projects/shokunin/.ufo/waves/round-39/w2/R39W2HeldReproB.md`. It was copied byte-exact into the lane (`cmp` equal, sha256 `d37db669…482a`) and the fleet copy and its empty dirs were deleted (M39-9). Wave-1 seat `R39SrcSasquatch` self-reported and self-removed three curl outputs in the fleet root (M39-8). The final `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no round-39 kaidoku file; the remaining untracked `.ufo/reports/round-48/tameshi.md` belongs to another lane and was not touched.
- **Other cleanup:**
  - A seat copy (over 1 MiB) of the public rea-agents 6.5.0 tarball (sha256 `531717a0…e699`, identical to the S119 anchor) was skipped by the commit helper and then deleted.
  - Scratch `/fast/scratch/hyaku/kaidoku-r39` was removed after landing; it held 876 entries, mostly leaked `gen.*` fixture dirs from seats (`w2/R39W2Sentinel.md` F3).
- **Tool installs:** none by the L1 or any seat (seat reports say nothing was installed). No pacman.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Open L0 questions:** none added.
- **Pre-report gate:** `git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin ls-remote origin refs/heads/main` → `8b9634ed8253653e7eb994aad9860a624e3b0366 refs/heads/main` (jj-lane state: local = remote, ahead 0).
