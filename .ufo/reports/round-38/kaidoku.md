# kaidoku — round 38 report (attempt 2)

L1 `KaidokuR38a2` holds the §3 planner seat. Lane: `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`, base `77091b492cc53f8743bd0701b1e7d5e66123dd84`. Attempt 1 (L1 `KaidokuR38`) froze both claims at `e059ca9391642d5b71b6662cabcbdce0d9308719` and ran wave 1, then died without a report (`.ufo/watchdog.log`: `lane-dead-no-report kaidoku round=38`, 03:37:05). This attempt inherited its bytes, re-verified them and landed the round. Fresh-start round under run 8.

## Work performed

Declared claims, frozen by attempt 1 and run unchanged. The first freeze is the rule (§6 item 9, §10 "Frozen and resumed rounds"):

- **R38-C1 — coverage:** standard big-endian SquashFS v4 (`squashfs_v4_be` via `sasquatch-v4be`, REA `extract-firmware`) moves from PROVINCE Frontier to Core on four frozen carriers.
- **R38-C2 — calibration:** the lane's self-assessment surfaces (SCORECARD owned axes and capabilities, SHONEN boxes, PROVINCE Core/Frontier rows) carry zero mismatches with observed repo state.

Work items:

- **Rule choice.** Attempt 1 amended the C1 predicate and counter twice, at `79f69347` (03:30:33) and `f1010f67` (03:32:55), after wave-1 seats had already scored carriers with the first-freeze counter (`.ufo/waves/round-38/w1/R38ExecAfterK1.md` §2e). Attempt 2 scores with the first-freeze bytes (counter sha256 `a7a62b09…`). Non-author check: `.ufo/waves/round-38/w2/R38W2C1RuleChoice.md` CONFIRMED.
- **C1 data and score.** The before/after receipts are `corpus/evidence/round-38/c1/K{1..4}/{before,after}.json` (landed `3b960fe5`). Four independent re-runs reproduced every payload (`w2/R38W2ReproK{1,2,3,4}.md`, all CONFIRMED). The first-freeze counter gives `carriers_matched 3`, exit 1 (`.ufo/waves/round-38/l1/scores/c1-v1-at-3b960fe5.json`, reproduced in `w2/R38W2C1RescoreV1.md`). K2's symlink resolves inside the tree, and REA records it as an `unpublished-entry` gap. **Honest stop**; no Core row was landed.
- **C2 repair and score.** The PROVINCE Core `REA MCP server` row pointer `evidence/doctor/` now points at the same document, `.ufo/waves/round-19/evidence/doctor/` (`PROVINCE.md:44`). The coverage row was re-stated to 126/126 (`SCORECARD.md:23`). The frozen counter gives 0 mismatches at `0fc61133` and at the final commit. Wave 2 showed the counter is non-discriminating: a stub written at the old path also scores 0 (`w2/R38W2C2Controls.md` §3). The claim therefore rests on two further checks: an independent re-derivation (`w2/R38W2C2Rederive.md`, CONFIRMED) and the new `tools/round-38/intended-doc.py`, which prints `bound` for the landing and `not-bound` for the base and the stub (`.ufo/waves/round-38/l1/intended-doc/`).
- **Knowledge.**
  - Frontier entry `corpus/knowledge/2026-10-26-r38-sasquatch-be-squashfs-recursion.md`: measured, not promoted. It covers the arms table, the handler argv and the AVM `-be` drop, and the two symlink outcomes. Attempt 1's draft had the title "→ Core" and a PROVINCE note claiming supersession; both were rewritten before landing.
  - Assimilated entry `corpus/knowledge/2026-10-26-unblob-format-matrix.md`. Non-author check: `w2/R38W2AssimAdmit.md` CONFIRMED.
- **Frontier step.**
  - SOURCES S112–S117 (`corpus/SOURCES.md:118-123`).
  - Lesson `corpus/lessons/round-38.md`: mistakes M38-1..M38-9 and the Gate.
  - QUALITY 79–81 (`corpus/QUALITY.md:87-89`).
  - Tools, each shown able to fail: `tools/round-38/freeze-drift.py`, `intended-doc.py`, `registry-immutable.sh`.
- **Wave-2 corrections, landed `7a1ac7fe`.**
  - First-freeze bytes restored at `tools/round-38/c1-counter.py` and `plans/round-38-claims.md` (M38-9).
  - An in-place S110 scope edit reverted byte-exact; the README "78+" sentences moved to their own row, S117 (M38-8).
  - A false admission-time "correction" of the staged vendor count reversed (M38-5).
  - The symlink generalisation made precise; a PROVINCE round-38 note added on the stale "unmeasured" aside.
  - `freeze-drift.py` now reports `ships_freeze_bytes` and treats a failing git call as unevaluable.
- **Inherited state from attempt 1.**
  - Reused after re-verification: the C2 pointer repair, SOURCES rows S112–S115, the receipts (reproduced in wave 2), and the 40 wave-1 reports plus artifacts, all committed at `3b960fe5`.
  - Discarded or rewritten: the frontier-supersession note and the entry's Core framing.
  - Attempt-1 scratch leftovers (`/fast/scratch/hyaku/kaidoku-r38/{l1-*,dbg*,…}`) were listed in `.ufo/waves/round-38/l1/attempt1-scratch-leftovers.txt`, then removed.

## Landed changes

All on lane `main`; LOG entry `LOG.md:3126-3135`.

| commit | what |
|---|---|
| `3b960fe5f9a7f1dfa22819f98dc0fa983f4260a8` | C1 receipts; C2 pointer repair and frontier note; the two entries; SOURCES S112–S116; QUALITY 79–80; `freeze-drift.py`; wave-1 evidence and ready/dispatched stamps; assimilation scratch |
| `0fc6113376a156fddc3ec385386d71c3a4a9f690` | SCORECARD coverage row 126/126 and `## Round 38` section, LOG entry, lesson, README lessons row, first-freeze C1 scores (C2 measured here) |
| `e265533ea3a7cd4d9a75a24ef737c2ff0e98e95f` | wave-2 spec, generator and validated dispatch (44 seats, policy v1) |
| `7a1ac7fe39410a3c9df13d97c14ba17f4d036ab6` | wave-2 corrections (list above), QUALITY 81, `intended-doc.py`, `registry-immutable.sh`, C2 receipt at `0fc61133`, wave-1 results ledger, misroot `unblob.log` |
| `7e97951460647e4fc39542b7a4f0255b5bf1af17` | final receipts (C2/C1 at `7a1ac7fe`, `freeze-drift`, `registry-immutable`, `intended-doc`), end census, wave-2 reports (44/44), artifacts, results ledger and stamps. C2 re-checked at this hash: 0 mismatches, `guards_ok`. Nothing on any scored surface changed after `7a1ac7fe` |

## Before → after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| R38-C1 | `python3 -I -B tools/round-38/c1-counter.py --root <lane> --rev <REV> --freeze e059ca9391642d5b71b6662cabcbdce0d9308719 --pkg65 /home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents --json-out <OUT>` (first-freeze bytes, sha256 `a7a62b09…`) | `carriers_matched 0`, exit 1 (CTL-C1-0 as scored at `efd5c47a`) | `carriers_matched 3`, `met_target false`, exit 1 (`.ufo/waves/round-38/l1/scores/c1-v1-at-3b960fe5.json`; same at `7a1ac7fe`: `c1-v1-at-final.json`). Informational, not the rule: the attempt-1 v3 counter gives 4/4 (`c1-v3-at-3b960fe5-NOT-THE-RULE.json`) | `3b960fe5`, `7a1ac7fe` |
| R38-C2 | `python3 -I -B tools/round-38/c2-counter.py --root <lane> --rev <REV> --base 77091b492cc53f8743bd0701b1e7d5e66123dd84 --json-out <OUT>` | 1 mismatch, exit 1 at base | 0 mismatches, `guards_ok`, exit 0 (`.ufo/waves/round-38/l1/scores/c2-at-0fc61133.json`, `c2-final.json` at `7a1ac7fe`); `intended-doc.py` → `bound` (`l1/intended-doc/final.json`) | `0fc61133`, `7a1ac7fe` |

Gate receipts:

- `freeze-drift.py --freeze e059ca93 --rev 7a1ac7fe` → exit 1 (3 commits: `79f69347`, `f1010f67`, `7a1ac7fe`), `ships_freeze_bytes true` (`l1/freeze-drift-final.json`). At `0fc61133` it gives `ships_freeze_bytes false` (`l1/freeze-drift-0fc61133.json`).
- `registry-immutable.sh` → exit 1 at `0fc61133` (S110 column 6) and exit 0 at `7a1ac7fe` (`l1/registry-immutable/`).

**Verdicts (author):** R38-C1 **honest stop**. R38-C2 **met by its frozen counter**, but the counter is shown non-discriminating, so the claim rests on the re-derivation and the intended-document gate; admission is the closure's call. Separability: C1's verdict does not depend on C2. As landed, C2's coverage count includes the C1 entry. In the counterfactual where C1 never landed and the coverage prose is restated, C2 still verifies (`w2/R38W2Separability.md`). No axis is harmed: coverage, depth and calibration all stay 10 → 10.

## Sources & frontier

- **Census** (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`):
  - Start: exit 0, 9× W04 (`.ufo/waves/round-38/census-start.txt`).
  - End: exit 0, 11× W04 (`.ufo/waves/round-38/census-end.txt`). The new warnings are S112, a second scope row on S108's handler URL, and S117, a second scope row on S110's README URL; both are cross-scope URL reuse.
- **Rows:** 111 → 117 (`grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md`).
  - By tier/status: A/mined +4 (S112, S113, S116, S117), A/rejected +1 (S115, the 7-Zip refusal as oracle), B/mined +1 (S114).
  - Rows touched old→new: none at the final commit. The `3b960fe5` in-place S110 scope/used-by edit was reverted (M38-8; `tools/round-38/registry-immutable.sh` exit 0 at `7a1ac7fe`).
- **Frontier:**
  - BE SquashFS v4 is measured but stays Frontier (C1 honest stop). README `## Frontier` and PROVINCE `:157` and `:376` carry dated notes.
  - AVM-BE branch evidence: `w2/R38W2AvmProbe.md` and `w2/R38W2AssimRejects.md` F1 show the `-be` drop destroys a plain-BE image. This is recon for round 39.
- **Sourced claim:** R38-C1's entry cites S113 and S114, both opened this round (S112 too).
- **Mined mistakes:** M38-1..M38-9, each with class, evidence, captured-by and a fix shown able to fail (`corpus/lessons/round-38.md` `## Mistakes`).
- **Assimilation:** theme sasquatch/unblob from `merge/kaidoku/`.
  - Admit: `unblob-format-matrix` (staged S122 → S116, staged S106 → S117, renumbered by document).
  - Refuse: `sasquatch-unblob-compatibility-precondition` and `sasquatch-unblob-avm-branch`.
  - The id-collision check before the append gave 6 collisions, S106–S111. The guard was proven on an indented fixture.
  - Reg/staged lists: `.ufo/waves/round-38/assimilation/{reg-ids,staged-ids,collisions}`.
  - The scratch-mirror census exited 0 in wave 1, and wave 2 re-ran it (`w2/R38W2AssimMirror.md`).
  - Quarantine slice: 5 rows hand-checked. Staged S150 is refused (fabrication class), staged S117 is unverifiable, and staged S113/S136/S147 are adopt-with-anchor but not appended.
- **considerthese:** `considerthese/` does not exist in this lane.

## Trend verdicts

- **expansion: improved** (author). Two mapped entries on ground the lane did not hold: measured BE v4 behaviour, and the producer's format matrix naming `v4-BE` and the vendor-mangled variants. The coverage map went 124 → 126. No Frontier → Core move, because C1 stopped.
- **quality: improved** (author). The stale PROVINCE "unmeasured" aside was superseded by a dated note. Every new row and entry was re-opened by non-author wave-2 seats, and two defects they found were corrected before close: the vendor count and the symlink universal. Three criteria (79–81) came from mined mistakes, each with an executable fix.
- **discernment: improved** (author; outside spot-check pending). The lane refused the attempt-1 post-scoring amendment that would have turned C1 green (v3: 4/4) and judged by the first freeze. It disclosed that its own C2 counter is non-discriminating instead of crediting the green, and it reverted its own registry violation.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — not touched this round; no verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — REA `extract-firmware` on four BE v4 carriers, before/after, logged at `LOG.md:3129`; receipts `corpus/evidence/round-38/c1/`; reproduced by non-author wave-2 seats `w2/R38W2ReproK*.md` (dispatched by this lane, so not an outside verifier).
- [ ] Instructions executable by an agent without oral context — not re-verified this round; no verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:97-125` Adjacent range unchanged (C2 check R3 passes at `7a1ac7fe`, `l1/scores/c2-final.json`). Round-38 PROVINCE edits are the doctor pointer and two dated frontier notes; no promotion verifier.

## Round shape, seats, extras

- **Shape:** two v1 waves (policy `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`, band 32–64), dispatched through the inline spawn handoff.
  - **Wave 1** (`r38-w1`, attempt 1, L1 `KaidokuR38`): 40 seats — executor 17, reviewer 5, scribe 4, scout 4, critic 3, connector 2, mutation-tester 2, revenger 1, sentinel 1, simplifier 1 (`.ufo/waves/round-38/r38-w1-results.json`). Dead: 0 (40/40 reports present).
  - **Wave 2** (`r38-w2`, attempt 2, falsify the landing): 44 seats — executor 11, critic 8, reviewer 7, scout 6, scribe 3, connector 3, revenger 2, mutation-tester 2, sentinel 1, simplifier 1. The m_flash-routed roles hold 26/44 (59%) and the attack roles 17/44 (39%) (`.ufo/waves/round-38/w2-spec.json`, `.ufo/waves/round-38/r38-w2-results.json`). Dead: 0 (44/44 reports present; WAVE-DONE received). The manifest's per-seat `status` field is null for every seat in both waves, so liveness is judged by report presence.
  - **Round total:** 84 seats. No residual call. The planner seat is held by the L1; the validator refuses `planner` as a swarm role.
- **Routing:** run-8 global role map; no `model` passed.
- **Misroot sweep:**
  - `/home/vgpnk/Projects/shokunin/unblob.log` (written by seat `R38W2SymlinkUnblob`'s unblob run) was copied byte-exact to the lane `unblob.log`, checked with `cmp` (sha256 `2d651a4a…9299`), and deleted from the fleet root (M38-7).
  - The lane-root `paths_raw.txt` (86 lines, 04:01, a wave-2 seat path dump; the author seat is not identified) was moved under `.ufo/waves/round-38/w2/artifacts/_misroot/`.
  - The final `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file from this round's seats.
- **Tool installs:** none by the L1 or any seat. Seat reports say "nothing installed"; sasquatch/sasquatch-v4be 4.5.1 date from round 36. No pacman.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Open L0 questions:** none added.
- **Pre-report gate:** `git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin ls-remote origin refs/heads/main` → `7e97951460647e4fc39542b7a4f0255b5bf1af17 refs/heads/main` (jj-lane state: local = remote, ahead 0, untracked 0).
