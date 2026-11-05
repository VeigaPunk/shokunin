# mori — round 96 report (attempt 1)

Lane: mori (森, fleet and host observability). Lane HEAD at filing: `167325885f0ca840f408b1a8bc15f981e170ea3e` (branch `master`, pushed). Entering HEAD `66c5518e239eeacd6070be26d78085ef702392cb`. Freeze `b88c8ae8` (contract, before-receipts, wave-1 spec and dispatch). Landing commit `9bde9322` (tool, SCORECARD cells, pins, lesson, LOG, wave-1 evidence). Evidence commit `16732588` (wave-1 results, landing receipts).

## Work performed

**Declared claims (2, frozen before any wave output; `.ufo/waves/round-96/contract.md`):**

- **C1 — calibration (score 5; lowest-scoring non-retired axis).** SCORECARD `Last change` cells against the admitted mori closures in `MANIFEST.json`. **Verdict: met by its counting command at the landing revision; the calibration score is not moved in this report (held at 5 pending closure).** Predicate P1, before→after: `mismatches=5` → `mismatches=0`, `columns_unchanged=yes`. Evidence: `.ufo/waves/round-96/w1/calib/base-run.txt` (`C1=unmet mismatches=5`), `.ufo/waves/round-96/evidence/landing-c1-new-counter.txt` (`C1=met mismatches=0 columns_unchanged=yes rows=6 rev=9bde9322d78a`). Cause of the gap: the frozen round-79 counter fixes `THROUGH = 78` (`.ufo/waves/round-79/count-c2.py:33`) and reads `met` at its default bound (`evidence/before-c1-count-c2-default.txt`); with `--through 95` the same counter reads `mismatches=5` (`evidence/before-c1-count-c2-through95.txt`). Remedy: new unbounded counter `tools/mori-scorecard-calibration.py` (selftest 11/11, stale-cell arm red-before). The frozen r79 counter is not amended. At the landing revision the frozen counter, run with `--through 95`, also reads met (`evidence/landing-c1-frozen-r79-through95.txt`).
- **C2 — freshness (score 5).** SOURCES digest re-verification. **Verdict: unmet — honest stop under the frozen kill rule.** `unpinned=6` → `unpinned=3`; `ok=86` → `ok=89`; `mismatch=0`, `prefix_only=31`, `superseded=1` unchanged. Pinned (live bytes hash to the recorded digest): S125, S612, S622. Stale, not pinned (live bytes differ from the recorded digest; recorded digests not edited): S615, S616, S623. Evidence: `w1/digest/DigestExec.md`, `w1/rev/DigestRev.md` (independent non-author re-fetch, same verdicts), `w1/lab/Lab-digest-stability.md` (two fetches 60 s apart, byte-stable per URL; S615/S616/S623 fail to match their recorded digests), `evidence/landing-c2-digest.txt`. Target was `unpinned=0`; the frozen predicate was not rescoped after data.

**Work items (each with its evidence pointer):**

- Frozen contract and before-receipts at `b88c8ae8` (`.ufo/waves/round-96/contract.md`, `evidence/before-*.txt`).
- Calibration counter build, selftest 11/11, base and head runs at `66c5518e` and `9bde9322` (`w1/calib/`, `tools/mori-scorecard-calibration.py`).
- Derived expectations for the five Last-change cells (`w1/calib/derived-cells.txt`); cells edited in `SCORECARD.md` `## Axes` (rows coverage, operability, depth, freshness, calibration), Score and Evidence cells untouched.
- Digest pins: fetches and copies (`w1/digest/fetched/`, `w1/digest/pinned/`, landed as `corpus/evidence/git-log-docs.html`, `corpus/evidence/posix-shell-v3-chap02.html`, `corpus/evidence/.ufo/waves/round-25/capture/{capture,capture-earlyoom}.txt`). The two S125 receipts are byte-identical copies of tsukuroi-shokunin files (`cmp`, read-only), pinned as evidence for the registry's named copy; not absorbed knowledge (PROVINCE adjacency).
- Mutation probe of the frozen r79 selftest: M1, M3, M4 killed; **M2 (min vs max), M5 (any verdict word), M6 (skipped adjacency) survive** (`w1/mut/MutCalib.md`). Carried to round 97.
- Critic review of both predicates before data (`w1/crit/CritRound.md`): C1 flagged for the contract trap (default-bound met on the unedited scorecard) and the bookkeeping concern; addressed by the unbounded counter and by the landing-revision check above. C2 flagged as unsatisfiable under the frozen rules; recorded as the honest stop.
- Scout reconnaissance: `w1/scout/CalibScout.md` (MANIFEST `admitted` semantics; no duplicate admitted round; one closure-correction row, admitted false) and `w1/scout/DigestScout.md` (copy-resolution branches per row).
- Connector sibling-overlap scan: `w1/conn/ConnRound.md`.
- Scribe drafts: `w1/scribe/lesson-draft.md`, `w1/scribe/scorecard-draft.md` (fed the lesson; SCORECARD round section is the L1's, written in the landing commit).
- Lesson `corpus/lessons/round-96.md` (Gate, Mistakes, Frontier step).
- SCORECARD round-96 verdict section and a refreshed Planned (round 97).

**Round shape.** One v1 wave, `w1`, **10 seats**: executor ×2 (CalibExec, DigestExec), scout ×2 (CalibScout, DigestScout), connector ×1 (ConnRound), scribe ×1 (ScribeDraft), critic ×1 (CritRound), reviewer ×1 (DigestRev), mutation-tester ×1 (MutCalib), revenger ×1 (DigestLab, the labrat-class probe; `labrat` is a frozen-topology role and the validator refuses it as a swarm role). Attack seats: critic, reviewer, mutation-tester = 3/10 (30 %, ≥25 %). Connector 1 (≤2). Planner held by the L1 by disclosure (validator refuses `planner`; L0 D1 open). Dead seats: **none** (`w1-results.json`, 10 settled). Residual call: **none dispatched.** A planned 2-seat attack wave on the new counter (`w2`) was refused by the validator (`too_few_lanes`, floor 8; `.ufo/waves/round-96/w2-validator.err`, file since removed); the new counter therefore received no post-build mutation attack this round (carried to round 97).

**Validator/route notes.** Route preflight was not run by the L1. Routing is the operator's `task.agentModelOverrides`; no model was passed.

**Stale-lane.** Not applicable: this round's mission closed within the round (no other mission of this lane is open).

**Tool installs.** None. Read `/home/vgpnk/.omp/agent/RULES.md`; no tool was installed or upgraded in this round. `curl`, `python3`, `git`, `jj` were already present. No pacman transaction. No host sysctl touched.

## Landed changes

| change | file(s) | LOG.md | commit |
|---|---|---|---|
| new calibration counter (C1 instrument) | `tools/mori-scorecard-calibration.py` | Round 96 entry | `9bde9322` |
| Last-change cells, five axes (C1 correction) | `SCORECARD.md` `## Axes` | Round 96 entry | `9bde9322` |
| round-96 verdict section and round-97 Planned | `SCORECARD.md` (appended) | Round 96 entry | `9bde9322` |
| pinned copies (C2, three rows) | `corpus/evidence/git-log-docs.html`, `corpus/evidence/posix-shell-v3-chap02.html`, `corpus/evidence/.ufo/waves/round-25/capture/*` | Round 96 entry | `9bde9322` |
| round-96 lesson (Gate, Mistakes, Frontier) | `corpus/lessons/round-96.md` | Round 96 entry | `9bde9322` |
| wave-1 evidence, landing receipts | `.ufo/waves/round-96/**` | Round 96 entry | `9bde9322`, `16732588` |

Frozen contract and before-receipts: `b88c8ae8`. No SOURCES row was added or edited in place (`corpus/SOURCES.md` bytes unchanged this round).

## Before → after measurements

| claim | counting command | before (`66c5518e`) | after (`9bde9322`) |
|---|---|---|---|
| C1 | `python3 tools/mori-scorecard-calibration.py <rev> --manifest /home/vgpnk/Projects/shokunin/MANIFEST.json` | `C1=unmet axes=6 mismatches=5 columns_unchanged=yes rows=6` | `C1=met axes=6 mismatches=0 columns_unchanged=yes rows=6 rev=9bde9322d78a` |
| C1 cross-check (frozen r79 counter) | `python3 .ufo/waves/round-79/count-c2.py <rev> --through 95 --manifest …` | `C2=unmet … mismatches=5 … through=95` | `C2=met axes=6 mismatches=0 errors=0 rows=58 through=95 rev=9bde9322d78a` |
| C2 | `python3 tools/mori-source-digest.py corpus/SOURCES.md corpus/evidence` | `DIGEST_CHECK rows=124 ok=86 mismatch=0 superseded=1 prefix_only=31 unpinned=6` (exit 1) | `DIGEST_CHECK rows=124 ok=89 mismatch=0 superseded=1 prefix_only=31 unpinned=3` (exit 1) |
| new counter selftest | `python3 tools/mori-scorecard-calibration.py --selftest` | — | `CALIB_SELFTEST pass=11 fail=0` (exit 0) |

Counts re-run at the landing revision by the L1 (`evidence/landing-*.txt`). Digest exit is 1 because three rows stay stale; the frozen C2 target was `unpinned=0`.

## Sources & frontier

- **SOURCES rows, before→after.** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: before exit 0 (`mori ok`, 42 W04 duplicate-URL warnings; `evidence/before-census.txt`); after exit 0 (re-run at `9bde9322`, `mori ok`). Rows: 124 before, 124 after. Rows added by tier: none. Rows touched old→new: none (no in-place edit). Digest verdicts: `ok` 86 → 89; `unpinned` 6 → 3 (S615, S616, S623 remain stale).
- **Sourced claim.** C2's evidence cites `S622`, `S612`, `S125`, each re-opened this round with URL, access date (2026-11-05, 12:20–12:22 UTC) and a located quote (`corpus/lessons/round-96.md` Gate table).
- **Mistakes mined.** Five, in `corpus/lessons/round-96.md`: (1) stale frozen `THROUGH = 78` bound — captured-by none; fixed by the unbounded counter. (2) r95 lesson's `unpinned=3` with no command, measured 6 — captured-by the CORPUS count rule (not applied). (3) frozen r79 selftest survivors M2, M5, M6 — captured-by none; carried to r97. (4) contract trap (default-bound met on unedited scorecard) — captured-by QUALITY 208, applied only to the frozen counter. (5) residual attack wave below validator band — captured-by the validator; carried to r97.
- **Frontier rows advanced:** none in `corpus/README.md ## Frontier`.
- **Knowledge entries admitted:** none.
- **Assimilation:** none (the round's inputs were the registry's own rows and the lane's own evidence; no `merge/mori/` or `considerthese/` theme was taken). Assimilation: none.

## Trend verdicts

- **expansion: unchanged.** No admitted `knowledge/` entry; no new registry row; no capability entered.
- **quality: improved (narrow).** Three rows re-verified against live bytes and pinned (S125, S612, S622, byte-identical receipts/copies); three rows found stale and named with their footer-level causes, not silently left (`corpus/lessons/round-96.md` Gate). Stale rows are flagged in the lesson, not edited in the registry. Evidence: `w1/digest/DigestExec.md`, `w1/rev/DigestRev.md`, `w1/lab/Lab-digest-stability.md`.
- **discernment: unchanged.** The non-author reviewer (DigestRev) agreed with the gate on all six rows; the critic's bookkeeping objection and the needs-amend verdicts are on record (`w1/crit/CritRound.md`). The closure's non-author spot-check is pending, so no `improved` is claimed.

Axis reading (not a score move): calibration — the Last-change mismatch count fell 5 → 0 with a non-author-critiqued counter; score held at 5 pending closure. Freshness — unpinned 6 → 3 with three stale rows named; score held at 5.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` decision and error-pattern tables (existing); this round added no SKILL.md text. Evidence: `SHONEN.md` box 1 pointers, unchanged.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 96 entry (C1 counter run at both revisions, C2 digest run) with `.ufo/waves/round-96/evidence/`.
- [~] Instructions executable by an agent without oral context — `python3 tools/mori-scorecard-calibration.py --selftest` (11/11) and `python3 tools/mori-source-digest.py --selftest` (11/11, exit 0 in `w1/digest/DigestExec.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — S125 receipts are sibling-owned copies pinned as evidence; PROVINCE adjacency rows unchanged; `corpus/lessons/round-96.md` Gate.

No `[x]` box: no non-author promotion verifier.

## Open items and L0

- L0 appended this round (operator ruling): stale recorded digests S615, S616, S623 — choose supersession per CORPUS rule 2 or a recheck cadence (`.ufo/l0-questions.md`).
- Carried to round 97: mutation sweep of the new counter (never run post-build this round); survivors M2, M5, M6 of the frozen r79 selftest; r95 routed items (m8/m10/m11 survivors, dormant `census_path` arm, `## Gate` heading); D1 planner binding.
- Fleet-root note: `.ufo/l0-questions.md` already carried two uncommitted lines from another writer at filing time. The L0 append is committed with `fleet-commit.sh --as mori`, which commits the whole file. Those two lines were not written by this lane.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` before filing: `.scratch/run15-state.json` (orchestrator-owned, not swept) and `.ufo/l0-questions.md` (see the note above). No seat wrote an untracked file into the fleet root; no misroot to move.

## Pre-report gate

`git ls-remote origin refs/heads/master` → `167325885f0ca840f408b1a8bc15f981e170ea3e` (matches lane HEAD; `jj-lane.sh state` ahead=0 behind=0). `grep -c '^## SHONEN'` → 1; four `[~]` box lines, no `[x]`. The L0 question was committed separately as `0ddb53f7` (fleet repo, pushed).
