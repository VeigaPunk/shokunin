# souji — Round 41 (attempt 1)

## Work performed

**Declared claims (frozen before any wave file, `souji-shokunin/census/round-41/preregistration.txt`, first added at `e2a74312af4233963e44e4dbb38838ece07b8bd2`):** C1 — calibration: three filed round-40 statements (I1 "worktree.c appears in 9 rows", I3 before/after arms over different registers, I4 dead-seat error text) get a CORRECTION line each, bound to values the counter re-derives at `bffcc0f660ff36eb8add3f61582748a7af019a5b`; I1 cites a new tier-A registry row. C2 — operability: `tools/souji-freeze-check.py` makes the "freeze before data" rule runnable. C3 — coverage: a 19-site / 21-probe battery for `tools/souji-worktree-drift.py`, scored by per-site label mutation. Residual R1 (routed defect R40-D-TOTAL, not a claim): TOTAL repair plus a record-order/root-repo fixture. Fresh-start posture: each target is unreachable by the do-nothing control committed with the freeze (`census/round-41/controls/*-control.txt`).

- **Read first:** `corpus/lessons/round-40-verifier-spotcheck.md` (R40-D-PRUNE → I1 + Q98 + S258; R40-D-C1-BEFORE → I3; R40-D-FREEZE → C2 tool + Q99; R40-D-TOTAL → tool repair + R1).
- **C1** landed at `31e4d3e758bb903808a9270018d7e5be99ce38a4`: `corpus/lessons/round-41.md` (CORRECTION lines, Gate, Mistakes M41-1…M41-4, limits N1-N19, errata E1/E2), registry row S258 with pinned snapshots (`census/round-41/sources/SHA256SUMS`). Receipt `census/round-41/records/c1-after.txt`.
- **C2** landed at `119c26fa3bbb85e215824de9538bd2eb34e9f874` (candidate R41executor07), then hardened (`383972ce…`, `c98fa5f1…`, `72e8a0b637ca6243857571d0433fcf7329fe4615`) after wave-2 attacks — a disclosed deviation (lesson E1); counters/populations/kill rules untouched. Receipts `records/c2-after.txt`, `c2-after-hardened.txt`, `hidden-audit-hardened.txt`.
- **C3** landed at `a1144120611b00091ac4839559d8ebf38aa9a83a` (R41executor04, smallest all-target candidate; shim audit `records/shim-audit.txt`: 21 tool invocations for 21 probes in every candidate). **R1** at `97eeb01e73a9baa3e4191b9052fed9e505c70215` (R41executor13).
- **Planner seat** held by the L1 (validator rejects `planner`); recon rode scouts/connectors.
- Instruments `6682b98175b995ee4646ffd1ea6bd8a12cd353dd`; freeze `e2a74312af4233963e44e4dbb38838ece07b8bd2`; tip `0c9581a44a2eaa7350b4699e64dcdfbe07fec0d5`.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| drift-tool TOTAL repair, counters, populations, score harness | Round 41 entry | `e9dc38daa67f437fcf1518e4117d684a543ad32d`, `6682b98175b995ee4646ffd1ea6bd8a12cd353dd` |
| preregistration + do-nothing controls | Round 41 entry | `e2a74312af4233963e44e4dbb38838ece07b8bd2` |
| C3 fixture / R1 fixture / C2 tool | Round 41 entry | `a1144120611b00091ac4839559d8ebf38aa9a83a` / `97eeb01e73a9baa3e4191b9052fed9e505c70215` / `119c26fa3bbb85e215824de9538bd2eb34e9f874` |
| C1 lesson + S258 + snapshots | Round 41 entry | `31e4d3e758bb903808a9270018d7e5be99ce38a4` |
| receipts, C2 hardening ×3, SKILL rows, QUALITY Q98-Q102 | Round 41 entry | `1d41c13574db80fdd9a4bde490b712da7ce2a85f`, `383972cee75dc22187da25baad432a60e88aca7d`, `c98fa5f1d2e508269c0aea0a225c1e756dab1bb3`, `832b7bbe1ac43c03fb1e5f5b9cc7bc01f6868dfe`, `72e8a0b637ca6243857571d0433fcf7329fe4615` |
| errata, wave evidence (1332 records) | Round 41 entry | `716eaa9e35ffc2643b5cb28981ee474b81b58bf8` |
| LOG, SCORECARD, README, final census, tip re-measurement | Round 41 entry | `0c9581a44a2eaa7350b4699e64dcdfbe07fec0d5` (`git ls-remote origin refs/heads/master` prints it) |

## Before → after measurements

| claim | before | after | counting command | commit |
|---|---|---|---|---|
| C1 calibration | do-nothing `corrected=0 uncorrected=3`; junk lesson `junk=3` | `items=3 mismatched=3 corrected=3 uncorrected=0 junk=0 rewritten=0 sourced=1`, rc 0 | `python3 -B census/round-41/c1-counter.py --root . --rev <full40>` | `31e4d3e…`; tip re-run rc 0 |
| C2 operability | tool absent `pass=0`; always-clean stub `pass=2/21` | `cases=21 pass=21 fail=0 control_clean=REJECTED control_findings=REJECTED real=ok retro=red`, rc 0 | `python3 -B census/round-41/c2-counter.py --root . --rev <full40> --scratch <dir>` | `119c26f…` (first), `72e8a0b…` (hardened) |
| C3 coverage | fixture absent; all-PASS stub survives 19/19 | `sites=19 probes=21 pristine=ok killed=19 survived=0 misattributed=0 docclasses=10`, rc 0 | `python3 -B census/round-41/c3-counter.py --root . --rev <full40> --scratch <dir>` | `a114412…` |
| R1 (residual) | fixture absent; stub kills 8, new 0/3 | `mutants=11 killed=11 survived=0 pristine=ok regress=8/8 new_killed=3/3 old_fixtures_killed_new=0 prior=6/6` | `python3 -B census/round-41/r1-counter.py --root . --rev <full40> --scratch <dir>` | `97eeb01…` |

All four re-run at tip `716eaa9…`: `census/round-41/records/tip-remeasure.txt` (the final commit changes only docs/receipts). **Honest reading, from wave 2 (lesson N1-N19):** every counter scores shape — wave 1/2 built fooling artifacts (C1 corrections with retracting prose/fences, C2 memorising tools, C3 label-sniffing fixtures) that reach the targets; C3 is class-level (8 of 29 behavioural mutants survive); R1 is not exhaustive (15 of 24 extra mutants survive); the C2 tool needed post-landing hardening (hidden-case audit strict 79/83 → 80/83, 57-case crafted battery 23 false greens → 11). The lane records these as named limits and reports the claims as **measured on the frozen counters, with substance caveats**; admission is the operator's call. Axes: no owned score changed (calibration 7, operability 8, coverage 8); no harm observed (59/61 gate rows identical base vs tip, the one difference a flake; six r36-r40 drift fixtures unchanged — R41w2executor03/04).

## Sources & frontier

- Census command (both ends): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`. **Before:** `souji ok`, exit 0, 181 rows (`records/census-before.txt`). **After:** `souji ok`, exit 0, 182 rows, W04 52 → 52 (`records/census-final.txt`).
- Rows added: S258 (tier A, `mined`, git v2.56.0 `builtin/worktree.c`; quote "prune missing working trees older than <time>", line 255, sha256 `af2bd523e1c89e33…` re-derived; a seat's transposed hash was caught). No old row's status/recheck/used-by changed. Sourced claim: C1 item I1 (counter requires S258). Search-log note added.
- Mistake mined: M41-1 (r40 pre-data-freeze) with captured-by sweep and fix shown able to fail (C2 controls); M41-2…M41-4 also filed.
- Frontier: F1 not promoted (library `worktree.c` recheck of S009 still open, lesson Gate). Assimilation: none (S160 re-decided as curation from upstream; `shokuknow` not read). `considerthese/` does not exist in this lane.

## Trend verdicts

- **expansion — unchanged.** One row on held F1 ground; no coverage-map ground promoted.
- **quality — improved.** Wave-2 reviewers found nine misstatements in the lesson's own text and the L1 corrected them append-only (E2); S258 hash typo caught; Q98-Q102 added with lessons; hardened tool measured twice.
- **discernment — unprovable-but-better.** The lane's seats found and routed the counters' substance gaps (N1-N19, Q100/Q102), but no non-author closure spot-check exists yet for this round's gate (lane seats are still the lane).

## SHONEN

- [~] SKILL.md contains decision tables, error patterns and checklists — SKILL.md Gate registry rows `souji-freeze-check`…`r41-c1-corrections`; QUALITY Q98-Q102.
- [~] End-to-end domain task executed and logged — LOG.md Round 41 entry (instrument/measurement work; no deletion authority exercised).
- [~] Instructions executable without oral context — `census/round-41/preregistration.txt`, counters and `score-candidate.sh`.
- [~] No cross-domain bleed — `census/round-41/waves/w1/R41connector01.md`, `w2/R41w2connector01.md`; sibling freeze tools (kasegi, mori) reported, not absorbed.

## Round shape, seats, deviations

- **Shape:** two v1 waves (policy v1, band 32–64): W1 build+attack-frozen = 43 seats (executor 15, scribe 9, critic 7, reviewer 5, scout 3, sentinel 2, connector 2; attack 12/43 = 27.9 %); W2 falsify = 37 seats (reviewer 8, critic 7, mutation-tester 6, executor 6, scribe 5, scout 2, sentinel 2, connector 1; attack 21/37 = 56.8 %). **Total 80** (band 64–128), no residual call. Both `results.json` list every seat settled (`census/round-41/waves/` capture, `--verify --rev` records=1332 failed=0); no dead seat is recorded in results. The dispatcher sat idle 18:42–19:39 (L0 line filed; wave then dispatched).
- **Deviations:** (1) C2 tool hardened after wave 2 (E1). (2) Selection rule applied as preregistered (smallest all-target); the sentinel-flagged executor07 limits were repaired after landing rather than by choosing another candidate. (3) The frozen counters' gaps were not amended (N1-N16).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec): 45 entries, none naming souji/round 41; nothing moved. **Scratch:** `/fast/scratch/hyaku/souji-r41` removed.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open; round 41 progressing through recorded commits. **Tools installed:** none; pacman paused. **Open L0:** `souji | round-41` dispatcher-stall line (fleet commit `9bcf1f95e0d9affdcd9494de1c50861d6c10bc82`), not blocking.
