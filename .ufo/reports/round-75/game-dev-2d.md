# Fleet report — game-dev-2d round 75 (wave-15)

Lane: `game-dev-2d-shokunin` | Round: 75 | Wave `shokunin-train-20261101-w15`
Verdict: **ADMIT-corr** (Sol) — `2e3ae8e` (work) + `be79ad1` (folds) + `ddd455b` (report-last)

## Move

Deferred/uncontained callback-write axes + joints/return surface —
the r74 critic-deferred cells (C1 twins, C3 update-level containment,
C4 `esc_fn` pinning) plus joints, `setFilterData`, and preSolve return.

## Landed

- 7 new `IW_CELLS` (+422/−11): `bc_setpos_wp`, `bc_joint_new`,
  `bc_joint_destroy`, `bc_setfilter`, `pre_retfalse`,
  `bc_destroy_unp`, `bc_setvel_unp`; `esc_fn` pinned on uncontained rows.
- **2 new classes**: `refused_abort` (assert-gated write contained one
  level up by `pcall(world.update)` — step aborts, transient lock,
  collateral exterior refusal, next-step recovery) and `ignored`
  (preSolve `return false` unconsumed — impulse lands; source-anchored
  `World.cpp:98` `lua_call(L, args, 0)`).
- **C1 confirmed strongest-form**: unp twins byte-identical to contained
  twins modulo labels — fatal is derived (`assert-gated × uncontained`),
  not a property of uncontained writes.
- Joints: `newDistanceJoint` refused (world-level assert);
  `joint:destroy` deferred — drain *point* inferred (no locked=false
  event for joints, unlike bodies).
- 44/44 ×5+ independent runs; concat iw sha `74db3f10…9004`.

## Wave-B

verifier AGREE 18/18 · reviewer ACCEPT 6-LOW · critic F1–F6 ·
simplifier C3 + 5 correct keeps · scribe zero-drift (2,101 rows) ·
baseline zero-drift (1 SIGKILL flake documented, rerun passed)

## Folds (`be79ad1`)

F2 gate defect (key-presence → `update_ok=="false"`; 18/130 scout
receipts recovered, 0 regressions) · F1 arm identity (`fire.kind` ×21 +
`mode=unp`) · R1 collateral pins (`wpext.err`/`pos_after`, `fire.pos`) ·
F3 epilogue-inference wording · F6a/R2 fatal-cells-last comments ·
F6d `after_update.b1vel` on contained twin (closes r74 rank-5) ·
R4 per-cell `rc` persisted · C3 docstring

## Deferred to r76

drain-deferral hazard cell (queued destroy + throw skips epilogue
drain); `world:destroy()` in-callback; SayGoodbye drain observers;
per-contact retfalse; `wp_abort` last-wins hardening (optional).
