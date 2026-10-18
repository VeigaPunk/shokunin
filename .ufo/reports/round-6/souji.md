# souji — round 6 (docs reconcile + census tool + scratch classification)

Lane HEAD at report time: `b5db5cf` (souji-shokunin identity). Single
batched dispatch: 128 seats on **xai-oauth/grok-4.7-fast**; 96 completed /
32 failed.

## Round verdict: REJECTED as a round — 2/3 claims verified at closure

Per the protocol a round admits only if every claim verifies. 15/17 final
judges found the claims NOT-MET at their measurement time; the parent
completed C1 and O1 before filing this report; K1 is an honest stop. The
judges' dissent is preserved verbatim in `census/round-6/final-*.json` —
nothing was re-rolled.

## Work performed

**C1 calibration — docs/tools reconciliation (verified at closure).**
Sixteen drift auditors found the taxonomy table misstated the installed
tools in 7+ places (fetch-based pushed commands, `origin/main`,
non-canonical ledger paths, wrong scratch classes, stale fleet facts).
Parent amendments applied to SKILL.md (taxonomy rewritten to the tool's
actual checks; surfaces refreshed: lore pruned to 1, gd2d pins, kotodama
40.4G, conf 4432B) and AGENTS.md (seat-harness clause from the r4 GUI
incident). The census tool's own docs independently confirmed the
`--branches --not --remotes` idiom.

**O1 operability — tools/souji-census.sh (verified at closure).**
Sixteen implementors, thin runner coverage (13 runner seats failed), so
the parent adjudicated: **impl-33** (selftest 32/32) installed byte-identical
(sha 11bf9cdf…). Two fleet runs diff only on live-delta rows
(gd2d/gd3d/kaidoku/kotodama mtimes + scratch bytes). First fleet picture:
21 repos; kotodama `.scratch` **40,448,039,054 bytes**, unpushed 53;
lore 3 worktrees + 218KB scratch; gd2d 5 worktrees (a new live one);
souji itself 11 unpushed bookkeeping commits.

**Parent fix during completion (new false-SAFE class).** The r6 audits
exposed that a later local-only commit touching a path still certified
SAFE(pushed). Both tools now require `git log --branches --not --remotes
-- <path>` to be empty for a pushed receipt. Verified: probe file with a
local-only second commit → NOT-SAFE(unpushed-commits-touching); clean file
→ SAFE(pushed); selftests 24/24 + 35/35. Note the pitfall: bare
`--not --remotes` silently returns nothing on git 2.55.

**K1 coverage — kotodama .scratch classification (NOT-MET; honest stop).**
Live-tree measurement defeated full classification: seat counts diverged
(535k files/17.9GiB vs 580k/20.56GiB — the tree grows ~2.3MB/s and 32 seat
failures broke shard coverage of the 388 children). Delivered instead:
parent two-pass snapshot (40.64G→40.75G in 46s), top-children table
(r28-x58 9.87G, x58 8.08G, x37 3.58G, …), and a parent-signed handoff
(`census/round-6/kotodama-scratch-handoff.md`): NOT-SAFE for all children,
hands-off until kotodama pushes, with a 3-step disposition. The growth
curve 553M→1.9G→16G→40.4G is the fleet's single largest hygiene signal.

## Landed changes

- `tools/souji-census.sh` + 15 impl variants; `census/round-6/`
  (35 seat fragments, 15 amendment diffs, census runs, handoff);
  `corpus/lessons/round-6.md`; LOG entry — commit `b5db5cf`.
- Patched `tools/souji-verify.sh` + `tools/souji-vault-verify.sh`
  (unpushed-touching receipt gate); SKILL.md + AGENTS.md reconciled.

## Before → after measurements

- C1: drift items found: 16+ across SKILL/AGENTS/PROVINCE surfaces →
  closure: taxonomy table matches installed probes (spot-re-verified);
  stale fleet facts refreshed. Judge dissent: amendments landed
  parent-side rather than from seat diffs — recorded.
- O1: before — no repeatable census (each round hand-rolled) → after —
  `tools/souji-census.sh --selftest` 32/32; two fleet runs agree except
  live deltas; 21 repos covered.
- K1: full classification NOT achieved — reported as such (honest stop);
  snapshot + handoff delivered as artifacts.

## SHONEN

- [~] SKILL.md decision tables — reconciled this round; the installed tools remain the source of truth.
- [~] End-to-end domain task — first fleet-wide census tool; kotodama handoff.
- [~] Executable without oral context — 96 zero-context seats; parent completed from their artifacts.
- [~] No cross-domain bleed — kotodama/secret-shaped names routed, not absorbed; gd2d pins untouched.
