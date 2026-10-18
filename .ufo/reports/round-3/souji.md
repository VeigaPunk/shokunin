# souji — round 3 (worktree prune + operator approval list)

Lane HEAD at report time: `36746332` (souji-shokunin identity). Single
batched dispatch: 64 seats on **devin/deepseek-v4-1-flash-high** (operator
devin test — 64/64 completed in 404s; the operator then directed
devin/deepseek-v4-1-flash-max for all future devin dispatches, recorded in
LOG.md). Seats did read-side verification only; the parent executed the
prunes serially.

## Work performed

Claims: **C1 coverage** — prune the 21 SAFE(metadata-prune) worktree
registrations (the goal text says 24; the corrected count is 21 — the 3
gd2d named-branch registrations hold unpushed commits and stay, per the r1
adjudication). **C2 calibration** — operator approval list with zero
false-SAFE. Both verified; no axis harmed.

- 64 seats: 21 verify tickets + 21 blind re-derivations + 7 fleet-wide
  sweep seats + 6 pin-audits (frozen baselines, lore live surfaces, fleet
  records, worktree-list callers, gd2d selective-preserve inventory) + 4
  approval builders + 7 gate auditors. 63/63 peer fragments + gate.
- Pair comparison (S57): 21/21 author-vs-blind agreements, 0 blocking
  disagreements. Gate tally (S64): prune_lore, prune_gd2d_detached,
  approval_list_ready all true; 3 blockers handled — (B1) `git worktree
  lock` preserve-then-prune for gd2d (bare prune would have taken the 3
  pinned registrations; `--expire` rejected as mtime-luck, S52); (B2) the
  dirty/unpushed wording — resolved at execution: both owning repos
  measured 0 unpushed at act time, so both readings authorize; (B3) the
  111-row contract re-cut to 96 approve-remove + 15 already-removed (fleet
  commit a1b44b1, unpushed, had already deleted the 15 shell strays; blobs
  survive in origin/master).

## Landed changes

- **Executed prunes (metadata only; no commits touched):** lore-shokunin
  `worktree prune` after a dry-run listing exactly the 19 → list 20→1;
  game-dev-2d-shokunin lock×3 → prune → unlock×3 → list 6→4, main sha
  unchanged (05a72899), wt-r98/99/100 intact with 1 unpushed commit each.
- `census/round-3/` — 64 seat fragments, approvals shards,
  `operator-approval-list.tsv` (96 SAFE/pushed rows, schema-normalized),
  `approval-summary.json`.
- LOG.md round-3 entry; `corpus/lessons/round-3.md` (lock-preserve house
  pattern, artifact-scoped gate, schema enforcement); SCORECARD — commit
  `36746332`.

## Before → after measurements

- C1 coverage: before — 21 dead registrations across 2 repos → after —
  `git -C lore-shokunin worktree list | wc -l` → 1; `git -C
  game-dev-2d-shokunin worktree list | wc -l` → 4 (3 pinned preserved by
  lock). Measured at execution, 2026-10-18 ~13:45.
- C2 calibration: before — approval list unmeasured → after — 96 unique
  approve-remove rows, all SAFE/pushed, re-verified by 4 builders + 2
  auditor seats (S59 recount, S60 independent re-runs), 0 false-SAFE;
  blind-ticket disagreement rate 0/21.
- **Probation gate: rounds 1–3 verified → satisfied.** The MANIFEST roster
  row remains the operator's decision; no promotion is claimed.

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists — exercised with the lock-preserve pattern added to lessons.
- [~] End-to-end domain task executed and logged — first receipt-gated removal in the fleet, fully logged.
- [~] Instructions executable without oral context — 64 zero-context seats + serialized parent execution from seat plans.
- [~] No cross-domain bleed — gd2d unpushed branches and `/tmp` residue routed (tsukuroi/operator), not absorbed; PROVINCE.md unchanged.
