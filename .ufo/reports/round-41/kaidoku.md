# kaidoku — round 41 report

L1 `KaidokuR41` held the §3 planner seat. Lane `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`. Base `49096c7e6f226af0c750c4b003be58883cb6049f`; lane hash at filing `740644747865c1c331bfacaf4daf46ea218762c3`. Attempt 1; the watchdog has no `lane-dead-no-report kaidoku round=41` line, so nothing was inherited.

## Work performed

The round declared two claims, frozen at `d764389e9cbe61b9d1b07538ff3bff02d50bb34f` (`plans/round-41-claims.md`):

- **R41-C1 — coverage.** Genuine AVM-layout big-endian SquashFS v4 moves from Frontier to Core. It is scored on four carriers that no REA or unblob run touched before the freeze:
  - V3: the FRITZ!Box 5490 07.31 wrapper member.
  - V4: the FRITZ!Box 5491 07.31 nested `filesystem_core` rootfs, 6349 files.
  - L3 and L4: lane-built, with nested-name path collisions in both directions.
  
  The counter is a round-41 port with an exact extract-root path rule (fixes R40-CL1) and a `member_sha256`/nested fetch chain (fixes R40-CL6).
- **R41-C2 — depth.** SKILL rule block 20 adds outcome-triage table v3. It is scored against an independent evaluator written from the frozen precedence text (round-40 closure D3), on 40 named-class carriers plus 12 combo carriers whose factors are seeded by the freeze hash.

Work items:

- **Wave 1 (41 seats), build and attack of the draft** (`.ufo/waves/round-41/w1/`):
  - tools now in `tools/round-41/`;
  - V3 and V4 provenance and oracles: 0 mismatches against a direct `sasquatch-v4be` extraction (`w1/R41C1VendorV3.md`, `R41C1VendorV4.md`);
  - the exact-path rule from source (`w1/R41C1Revenger.md` §1);
  - the rootfs removal disposition (`w1/R41C1DevCore.md` §7);
  - precedence ambiguities resolved in the frozen text (`w1/artifacts/R41C2Eval/precedence-ambiguities.md`);
  - critics changed the draft (`w1/R41CritC1Draft.md`, `R41CritC2Draft.md`, `R41C2Shortcuts.md`, `R41C2AxisFit.md`). Every change is listed in the plan's `## Changes from the draft`.
- **Freeze** `d764389e`. **Controls before data** `9a8fb260`:
  - C1 do-nothing: 0/4.
  - C1 with the round-40 receipts relabelled: 0/4.
  - C2 counter at the freeze: exit 2.
  - C2 dev controls: 0, 4, 34, 2, 38, 31, 42 and 44 of 52; SKILL v3 scored 52/52 on the same set.
  - Selftests passed: c1-counter 97, c2-counter 70, interpreter 69, c1-extra 17, fetch-vendor 16, gate 23.
- **Data:**
  - C1 receipts at `5ca6941b`. V4's `after.json` landed later, at `e9a24d07` (see M41-3).
  - C2 held-out set, seed = freeze, at `8a1f4c73`.
- **Landing documents** at `042b8769`: PROVINCE `## Round-41 additions to Core` and the frontier note, the entry, README rows, S127 and S128.
- **Scores** at `bf5286c9`.
- **Assimilation** at `e1c83313`.
- **Lesson and ledgers** at `74064474`.
- **Wave 2 (33 seats), falsify** (`.ufo/waves/round-41/w2/`). 26 reports had landed at filing; see Round shape.

## Landed changes

LOG entry: `LOG.md` `## 2026-10-26 — round 41 …`.

| commit | what |
|---|---|
| `d764389e9cbe61b9d1b07538ff3bff02d50bb34f` | freeze: claims, tools, C1 carriers/oracles/gap rule, SKILL block 20 + v3 entry, controls + dev set, wave-1 evidence |
| `9a8fb26001307bc2159934ed53c5fc43e5c8d615` | pre-data control receipts, selftests, wave-1 results |
| `5ca6941b061591748c6755c1dcfc188941fcbd35` | C1 REA receipts (V3, L3, L4; V4 log only) |
| `8a1f4c73057405a4b470af11d1d351a0f03f6c34` | C2 held-out data |
| `042b87697e7d94e9fc2d3cbcf03541bfd5c03b98` | C1 landing documents, S127–S128 |
| `e9a24d07256d1606f01aa4d2d65f74e649c5f3d4` | V4 `after.json` (measured revision) |
| `bf5286c9832142a2ceabe2076883dfa2a8e99356` | scores |
| `7a24ff74736e84b1903db7ba01891c406a6e32a2` | large wave-1 artifacts; R41C1Counter's post-freeze rewrites set aside |
| `e1c83313f33a3d97edbd8fef402db2d06172fcdc` | assimilation: binwalk v3 entry, S129 |
| `740644747865c1c331bfacaf4daf46ea218762c3` | lesson, QUALITY 84, SCORECARD `## Round 41`, LOG, SHONEN, entry citation fix, end census, wave-2 reports so far |

## Before → after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| R41-C1 | `python3 -I -B tools/round-41/c1-counter.py --root <LANE> --rev <REV> --freeze d764389e… --pkg65 /home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents --carrier-cache <CACHE> --json-out <OUT>`, plus `c1-extra.py … --base 49096c7e…`. The cache is filled by `tools/round-41/fetch-vendor.py --rev d764389e…` | `carriers_matched 0`, exit 1 (`.ufo/waves/round-41/controls/c1/ctl-c1-0-do-nothing.json`) | `carriers_matched 4` of 4, every binding true, exit 0; `c1-extra` met (`.ufo/waves/round-41/l1/scores/c1-at-e9a24d07.json`) | `e9a24d07` |
| R41-C2 | `python3 -I -B tools/round-41/c2-counter.py --root <LANE> --rev <REV> --freeze d764389e… --json-out <OUT>` | exit 2, `no_manifest_at_rev` (`controls/c2-counter-at-freeze.json`) | matched 52/52 and `distinct_decisions 13`, but `observed_features_match_declared` is false, exit 1 (`l1/scores/c2-at-e9a24d07.json`) | `e9a24d07` |

**Verdicts (author).**

- **R41-C1: met.**
  - Wave 2 reproduced V3 (`w2/R41W2ReproV3.md`) and the oracles (`w2/R41W2C1Oracle.md`).
  - The removal disposition held against 8 mutations (`w2/R41W2C1Removal.md`).
  - Wave 2 confirmed this is a coverage move (`w2/R41W2C1AxisFit.md`).
  - Disclosed limit (R40-CL2): oracle-only fabrications pass the rerun projection on 3 of 4 carriers, but none reaches the target (`w2/R41W2C1Fabricate.md`).
- **R41-C2: not met, honest stop.** The 12 combo carriers carry their declared feature tuple under the manifest key `declared`, which the frozen counter does not read. Wave 2 confirmed the stop and its cause (`w2/R41W2C2Rescore.md`, `R41W2C2AxisFit.md`). It also showed the combo family is weaker than claimed: the lookup control scores 8/12 on the combos (`w2/R41W2C2Combos.md`).

Owned scores:

- coverage 10 → 10 (map 130/130 → 133/133);
- depth 10 → 10 (rule blocks 19/19 → 20/20; no depth improvement is claimed, because C2 stopped);
- calibration 10 → 10.

No harm was found (`w2/R41W2Harm.md`). One capability row entered: genuine AVM-layout BE SquashFS v4 recursion.

## Sources & frontier

- **Census** (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`):
  - start: exit 0 (`.ufo/waves/round-41/census-start.txt`);
  - end: exit 0 (`census-end.txt`). Warnings are W04 only.
- **Rows:** 126 → 129, counted with `grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md`. All three are tier A, `mined`, opened 2026-10-26:
  - S127, S128: AVM 5490 and 5491 download directories, identity only;
  - S129: binwalk v3 README, commit-pinned.
  
  No existing row was touched.
- **Sourced claim:** the R41-C1 entry cites S127 and S128, both absent at the base (`c1-extra` `sourced_new` true).
- **Mined mistakes:** M41-1..M41-5 in `corpus/lessons/round-41.md` `## Mistakes`. M41-1 and M41-3 have checks shown red and green (`.ufo/waves/round-41/l1/mistakes/`).
- **QUALITY 84** added.
- **Round-40 closure D1 (S126):** fixed by an in-lane copy, a map and `local-source-gate.py`; confirmed by `w2/R41W2LocalSrc.md`. 18 other host-local rows are routed as R41-CL3.
- **Assimilation**, theme: domain guard (`merge/kaidoku/`).
  - Admit: `firmware-region-vocabulary`, landed as `2026-10-26-binwalk-v3-unit-of-work`, staged S109 → lane S129 by document.
  - Reject: `unblob-sasquatch-dependency`, because it duplicates ground the lane already holds.
  - Id-collision check: `reg-ids` 126, `staged-ids` 132, 21 collisions, all positional drift. The 0–3-space guard was proven on an indented fixture.
  - Quarantine slice: 5 rows, sha256 `7383a90e…28e6a`, byte-identical to round 40. Nothing was appended from it.
- **considerthese:** no `considerthese/` directory exists in this lane.

## Trend verdicts

- **expansion: improved.** AVM-BE moved from Frontier to Core with a first full vendor rootfs (6349 files). Three entries are mapped (133/133). One capability row entered.
- **quality: improved.** Fixed: R40-CL1, CL3, CL4, CL6 and D1, plus the R40-CL5 prose. QUALITY 84 came from this round's own mistakes. Every receipt has an exit code. The v3 table remains unscored because of the C2 stop.
- **discernment: improved** (author; outside spot-check pending). C2 was stopped under its frozen rule rather than repaired after scoring. The transient 3/4 at `042b8769` is recorded, and wave 2's combo-strength finding is reported.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:81-449`, 20/20 rule blocks resolve (`SHONEN.md:6`). No non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — REA `extract-firmware` on V3, V4, L3 and L4 (`corpus/evidence/round-41/c1/`, LOG round-41 entry), reproduced by wave-2 seats. Those seats are lane-dispatched, so they are not outside verifiers.
- [~] Instructions executable by an agent without oral context — the frozen v3 interpreter labels 52/52 held-out envelopes the same as the independent evaluator (`l1/scores/c2-at-e9a24d07.json`), but the claim stopped. No outside verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `## Adjacent` is unchanged. The round-41 section was appended at the end of `PROVINCE.md`. No promotion verifier.

## Round shape, seats, extras

- **Shape:** two v1 waves under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`, both dispatched through the inline spawn handoff.
  - **Wave 1** `r41-w1`: 41 seats, all settled (WAVE-DONE; `r41-w1-results.json`). Mix: executor 15, critic 8, scribe 5, connector 3, mutation-tester 2, revenger 2, reviewer 2, scout 2, sentinel 1, simplifier 1.
  - **Wave 2** `r41-w2`: 33 seats. Mix: critic 10, executor 7, reviewer 6, mutation-tester 3, scout 2, connector 2, sentinel 1, scribe 1, simplifier 1.
  - **Round total:** 74 seats. No residual call. The L1 holds the planner seat.
- **Dead seats:** none observed.
- **Conformance defect — report filed before wave 2's WAVE-DONE.** 26 of 33 wave-2 reports had landed when this report was filed. The L1 run hit its request budget. Late wave-2 reports are uncommitted, and stray seat files sit in the lane (`green.err`, `red.err` in the lane root and in `corpus/evidence/round-41/c1/V4/`).
- **Wave-2 findings routed:**
  - `fetch-vendor.py` follows symlinks on write (`w2/R41W2C1Chain.md`);
  - the path rule accepts a non-segment-bounded diagnostic root (`w2/R41W2C1PathRule.md`).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` printed nothing.
- **Cleanup:** scratch `/fast/scratch/hyaku/kaidoku-r41` is left for `inline.sh advance` to purge. It holds the vendor cache, which must never be committed.
- **Tool installs:** none by the L1, and no pacman transaction.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Open L0 questions:** none added. R40-CL7 and D2 remain operator rulings.
- **Pre-report gate:** `git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin ls-remote origin refs/heads/main` prints `740644747865c1c331bfacaf4daf46ea218762c3 refs/heads/main`.
