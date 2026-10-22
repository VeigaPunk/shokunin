# kaidoku — round 25 report (attempt 3)

Lane repo `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`. Pushed lane tip at filing: `cce7504ac1f4e1abe703edbdfc3a8c9f55bfc13a` (every lane commit below came from `jj-lane.sh` printing `landed <hash>` after remote verification). Attempt 3 was dispatched at 2026-10-22T09:19:46Z; Main froze scope at 11:20Z.

## Work performed

Declared claims, frozen by attempt 2 at `7ef837a473ae65d924b9ea34e7748f722a6cd7d5` (`.ufo/waves/round-25/a2/claims.json`) with instruments committed earlier at `9dcd11ecb412fe4828f274580018039b8edbc05a`, kept unchanged by attempt 3:

- **R25-C1, calibration** (repair-first: the round-24 closure was rejected-honest-stop). Counts mismatches between five fixed lane self-assessment statements (SCORECARD, LOG, QUALITY, SHONEN) and observed repo state. Target: 5 → 0.
- **R25-C2, coverage** (learning claim, sourced claim). New knowledge entry on PROVINCE Frontier ground: EVM selector naming. Target: knowledge Markdown 107 → 108 and entry sourced by a SOURCES row opened 2026-10-22, 0 → 1.

Work items:

- Re-verified inherited attempt-2 state: instrument digests equal the claims pins at every revision (seat report `.ufo/waves/round-25/a3/w1/C1Rerun.md`, `C2Rerun.md`); the 138 saved lookups match their manifests (`EvidenceIntegrity.md`); REA 6.5.0 replays of the six saved envelopes are byte-equal (`corpus/evidence/round-25/a3/c2/rea-replay/compare.json`, `runs.txt` with argv; seats `C2ReaReplayA.md`, `C2ReaReplayB.md`).
- R25-C1 repair, commit `0e333eb2fc25f538a99058761f379845f2534c42`: SCORECARD and LOG lines recording the round-24 outside decision (`SCORECARD.md:3048`, `LOG.md:2954`); QUALITY row 34 from the round-24 spot-check disagreement (`corpus/QUALITY.md:44`); coverage row 78/78 → 107/107, true by command A (`SCORECARD.md:23`); SHONEN boundary pointer 88-116 → 95-116 inside `## Adjacent` (`SHONEN.md:12`).
- R25-C2 entry, commit `08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76`: `corpus/knowledge/2026-10-22-r25-evm-selector-name-resolution.md`; new rows S075–S077 (`corpus/SOURCES.md:81-83`); README map and knowledge rows (`corpus/README.md:74,164`); PROVINCE Frontier line 93 reworded in place; offline tally tool `tools/round-25/a3/tally-resolution.py` and its output `corpus/evidence/round-25/a3/c2/analyze/tally.json`; attempt-2 resolver and saved evidence committed.
- Wave 1 (33 seats) attacked and extended both claims; the L1 landed its corrections at `dc31f9c441528cfff1070c0574eea9669fd47e64` and `1e064f9b203a012c4d3d33be87a9f3d0039d135f`: rules disclosed as chosen on their own scoring rows (`C2EntryOverreach.md`); distinct-selector counts and their dedupe scope (`C2IndependentTally.md`); two Vyper carriers, not one (`PriorEvmEntries.md`); REA's argument misses on 12 of 69 rows with the traced cause, EVMole 0.9.3 reading no `SHR` address check (`VyperArgsCause.md`), fixed in EVMole 0.9.4 while every REA release pins 0.9.3 (`C2EvmoleDirect.md`, `C2Rea67.md`); `filter=true` equals the local `filtered=false` subset on all 43 selectors, saved in `corpus/evidence/round-25/a3/c2/filter-true/` (`C2FilterTrue.md`); 4byte default order is newest `created_at` first (`C2FourbyteOrder.md`); S075 and S077 wording narrowed and S078 added (`LessonGateDraft.md`, `SourcesOverlap.md`, `C2SourcifyService.md`); resolver `fetch` now refuses pagination URLs outside www.4byte.directory (`Sentinel.md`; selftest 9/9 and tally byte-identical after the change).
- Independent recomputation: a second Keccak (pycryptodome and @noble/hashes) found 0 label disagreements over 344 candidates (`C2IndependentKeccak.md`); a from-scratch scorer reproduced all 40 table cells (`C2IndependentTally.md`); every ABI is a compiler output (`C2AbiTruth.md`); a live re-fetch at 10:45Z was byte-identical (`C2LiveDrift.md`).
- Instrument attacks: both frozen instruments can fail on each item (`C1Mutation.md`: I1–I5 each flipped by one edit) and both have false accepts (`C1Mutation.md` 6, `C2Mutation.md` including "opened" not checked). These are disclosed in `SCORECARD.md:3059`, not repaired, because QUALITY row 33 forbids changing frozen instruments after the freeze.
- Self-assessment beyond the five items: `C1Cherrypick.md` found more stale statements; the depth row was recounted 9/9 → 17/17 (`SCORECARD.md:24`), the rest are disclosed as open.
- Claim-freeze ledger: added the missing round-25 row (`corpus/claim-freezes.tsv`, FLAGGED for attempt 1's absent instrument); `freeze-gate.py` at `1e064f9b` now reports disclosures exact 12 of 12, missing [] (`corpus/evidence/round-25/a3/after/freeze-gate-at-1e064f9b.json`).

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `46d2613d505181bbe7ab1ad1e338399ba9b0be26` | attempt-2 wave-1 spec, dispatch, registry and job-limit refusal (0 spawned) committed as evidence | `LOG.md:2952` section; report |
| `0e333eb2fc25f538a99058761f379845f2534c42` | R25-C1 repair (SCORECARD, LOG, QUALITY 34, SHONEN) | `LOG.md:2954-2955` |
| `08c7a7299ed61c3fdc30ddb0adfe4e812d5eac76` | R25-C2 entry, S075–S077, README, PROVINCE line, attempt-2 c2 evidence and resolver, replay and tally | `LOG.md:2956` |
| `dc31f9c441528cfff1070c0574eea9669fd47e64` | wave-1 corrections, S078, depth recount, lesson Gate and Mistakes M25-5 to M25-9, filter=true evidence, saved source copies | `LOG.md` "Wave 1 (33 seats …)" line |
| `1e064f9b203a012c4d3d33be87a9f3d0039d135f` | late corrections, resolver pagination check, claim-freeze row, SCORECARD disclosures and planned row, lesson M25-10 | `LOG.md` "Later wave-1 corrections" line |
| `ad73b90e3f1af4cbdebaa4a92f258f60fd780bb5` | wave evidence (specs, dispatch, registry, task result, 33 reports), final receipts, census | `LOG.md` "Wave 2 … not dispatched" line |
| `cce7504ac1f4e1abe703edbdfc3a8c9f55bfc13a` | final `SiblingOverlap.md` seat report after its last search returned (no finding changed) | same wave-evidence line |

Inherited leftovers named: attempt-2 `.ufo/waves/round-25/a2/` (committed `46d2613d`), `corpus/evidence/round-25/a2/c2/` and `tools/round-25/a2/resolve-selectors.py` (committed `08c7a729`, re-verified, resolver patched at `1e064f9b`). Nothing reverted. Attempt-1 files (`.ufo/waves/round-25/claims.json`, `tools/round-25/instrument-custody.py`, lesson sections above "Attempt 3") untouched; `corpus/lessons/round-24-verifier-spotcheck.md` untouched. Attempt 1's prospective 34-case custody claim was not continued and has no after value; it is reported as not pursued, not as met.

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| R25-C1 | `python3 -I -B tools/round-25/a2/c1-calibration.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>` | 5 mismatches of 5, exit 1 at `9dcd11ec` (`corpus/evidence/round-25/a2/before/c1-calibration.json`) | 0 of 5, exit 0 | `0e333eb2` (C1 alone), `08c7a729`, `dc31f9c4`, `1e064f9b` (`corpus/evidence/round-25/a3/after/c1-at-*.json`) |
| R25-C2 | `python3 -I -B tools/round-25/a2/c2-coverage.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>` | knowledge_md 107, entry_sourced 0, exit 1 at `9dcd11ec` | 108, 1 (S075–S077 at `08c7a729`; S075–S078 at `1e064f9b`), exit 0 | `08c7a729`, `dc31f9c4`, `1e064f9b` (`c2-at-*.json`) |

Both claims reached their declared after-values. Owned-axis finite proxies stay 10 → 10 (delta 0). Command A at `1e064f9b`: mapped 108/108, missing [], dangling [], rule blocks 17/17 (`commandA-at-1e064f9b.json`). No-harm clause: `git diff --name-status 18e7eb6d 1e064f9b -- corpus/knowledge corpus/lessons corpus/QUALITY.md` lists only `A` for the new entry and the round-25 lesson and `M` for QUALITY with 0 removed lines (`noharm-name-status.txt`). Both instruments carry the disclosed false-accept gaps above; the landed bytes were checked by command A, saved page copies and seat re-derivations, not by the instruments alone.

## Sources & frontier

- Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`: start exit 0 (five W04 duplicate-URL warnings S033, S047, S054, S062, S069; `ok`); end exit 0, same five warnings (`corpus/evidence/round-25/a3/census-end.txt`).
- Rows 74 → 78 (`git show <REV>:corpus/SOURCES.md | grep -cE '^\| S[0-9]{3} \|'` at `7ef837a4` and `1e064f9b`). Added by tier: A +4 (S075 4byte.directory API docs, S076 Sourcify 4byte OpenAPI, S077 EVMole interpretation reference, S078 Sourcify 2025 recap); B +0; C +0.
- Rows touched old → new: S075–S077 none → `mined`, then S075 and S077 `teaches` narrowed after wave 1; S078 none → `mined`. No older row changed. Logged in `corpus/lessons/round-25.md` "Attempt 3 … Gate", with URL, access date and a located quote per row; saved page copies with sha256 in `corpus/evidence/round-25/a3/sources/SHA256SUMS`.
- Frontier: PROVINCE Frontier "EVM bytecode (extended)" line moved from "selectors stay bare hashes (no signature DB → no name resolution)" to labelled candidates from saved lookups, never verified (`PROVINCE.md:93`); it stays in Frontier, not Core.
- Mined mistakes: `corpus/lessons/round-25.md` M25-5 to M25-10 (stale coverage row, outside verdict not recorded, argv not retained, post-hoc rule, wording stronger than sources, seat counts from rosters). M25-5 and M25-6 fixes are shown able to fail by the before receipt; M25-10 by a seat check; M25-8 and M25-9 are stated as not yet shown able to fail.
- Sourced claim: R25-C2's entry cites S075–S078, all opened 2026-10-22.

## Trend verdicts

- **expansion: improved.** One new knowledge entry on ground PROVINCE listed as missing (EVM selector naming), with five scored rules, three error patterns and a traced REA argument-inference cause (`corpus/knowledge/2026-10-22-r25-evm-selector-name-resolution.md`). Bounded to six lane-compiled carriers and one lookup snapshot.
- **quality: improved.** Five frozen self-assessment mismatches 5 → 0 plus the depth row recount; QUALITY row 34; resolver pagination host check; entry corrections from wave 1. Instrument false accepts and the other stale statements are disclosed, not fixed.
- **discernment: improved.** The round-24 spot-check disagreement became QUALITY row 34; wave-1 attacks led to narrowed source wording (S075, S077), a maintainer source for the openchain takeover (S078) and an explicit post-hoc disclosure (M25-8). This is author-assessed; the closure decides.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md:5-6`; not touched this round (a draft SKILL row was not landed because it would shift pinned SKILL lines, `SkillRowDraft.md`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `SHONEN.md:7-8`; untouched.
- [~] Instructions executable by an agent without oral context — `SHONEN.md:9-10`; untouched.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `SHONEN.md:12`, pointer refreshed to `PROVINCE.md:95-116`; no non-author verifier named, so not `[x]`.

## Round shape, seats and conformance

- Shape: default two v1 waves, but only wave 1 ran. A 65-seat v2 wave was validated first (`.ufo/waves/round-25/a3/v2-undispatched-spec.json`) and waited 3600 s at the seat gate without a grant (live estimate 71–81 of cap 85); it was reshaped before any dispatch into two v1 waves of 33 and 32. Wave 1 dispatched at 10:42Z as one `task` call carrying the validator's `taskCall` unchanged (`w1-task-result.json`); all 33 seats returned reports, 0 dead, 0 refused; the seat-gate reservation was released after the last seat returned (11:45Z). Wave 2 (32 attack seats, `w2-spec.json`, validated) was not dispatched because Main froze scope at 11:20Z. No residual call. **Round total: 33 seats.**
- Wave-1 role mix: executor 14, scout 5, reviewer 4, scribe 4, mutation-tester 2, critic 2, connector 1, sentinel 1. Attack seats 8 of 33 (24%): **below the 25% attack floor by one seat**, a conformance miss caused by the cancelled wave 2. The §3 L2 floor is met (planner held by the L1, with the planning data walk on scout `PlannerWalk`; connector `SiblingOverlap`; executors, scribes, scouts, reviewers and critics present).
- The wave-1 registry `.ufo/waves/round-25/a3/w1/swarm-registry.json` lists 65 members because the v2 validation wrote into the same report directory; only the 33 with an agent id were spawned (lesson M25-10).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no file written by this round's seats at the fleet root (also `FleetMisrootPrecheck.md`); nothing moved or deleted.
- Sibling overlap: no sibling lane holds selector-name resolution (`SiblingOverlap.md`). No sibling sources admitted.
- Installs: the L1 installed nothing. Seats, scratch-only under `/fast/scratch/hyaku/kaidoku-r25-a3/seats/`: pycryptodome 4.1.0 (uv venv, PyPI) and @noble/hashes 2.4.0 (npm prefix) for independent Keccak; evmole 0.9.4 (npm/npx) for the upstream comparison; rea-agents 6.5.0 and 6.7.0 via npx; vyper 0.4.3 with pycryptodome 3.24.1 (uv venv) to recompile ABIs; local builds of the evmole 0.9.3/0.9.4 crate sources for tracing. No pacman transaction, no service restart.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open L0 questions: none added this round.
- Planned next (`SCORECARD.md:3061`): depth — one-pin evidence-id identity table for eight native readers at `rea-agents@6.5.0`, with the counting script and expected values committed before any REA run.
