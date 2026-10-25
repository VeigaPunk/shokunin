# Fleet report — game-dev-2d round 76 (wave-16)

Lane: `game-dev-2d-shokunin` | Round: 76 | Wave `shokunin-train-20261101-w16`
Verdict: **ADMIT-corr** (Sol) — `6ca715d` (work) + `c8fa307` (folds) + `aa4d567` (report-last)

## Move

The r75 boundary's drain-deferral hazard made a first-class cell, plus
destroy edges (`world:destroy`, double-destroy), joint drain observers,
and per-contact `preSolve return false` discrimination.

## Landed

- 5 new `IW_CELLS` (+174/−1 battery, +131/−3 probe): `bc_draindefer`,
  `bc_destroy2`, `bc_worlddestroy`, `bc_jwatch`, `pre_retfalse1`.
- **New class `deferred_abort`**: accepted queued destroy + escaped
  throw → epilogue drain skipped, catches up one update late. Third
  abort-adjacent class; ablation matrix proves each leg load-bearing.
- `bc_worlddestroy` → `died`: deferral via `destructWorld`
  (`World.cpp:578-581`), death at next world access
  (`esc_fn=getBodyCount`). Scout's harder edge: `world:release()`
  in-cb = **SIGSEGV** (only corrupt class on the surface; r77 seed).
- `bc_destroy2` → `deferred`: double-destroy split — inert in-cb,
  lifetime-guard error post-drain (`wrap_Body.cpp:31-37`).
- `bc_jwatch` → `deferred`, drain bounded inside the update-73
  epilogue (`jwlive`→`jdrain`, both step 73; cite `World.cpp:289-294`).
- `pre_retfalse1` → `ignored`: critic's 3-granularity control refutes
  masking — return inert at every granularity (`World.cpp:98`).
- 49/49 ×4 author + verifier ×2 + critic ×4 replays; concat sha
  `d1cbc1f8…` across 8 independent dirs.

## Wave-B

verifier AGREE all claims · reviewer ACCEPT (F1 fail-open + F2 stale
enum + F3 anchor, all folded) · critic (4 hunts, D1/D2 folded, D3
declined — `anomaly` is fail-loud; strongest attack self-refuted) ·
simplifier (P1 `abort_w` hoist + P2 enum→pointer, both byte-identical
+ 200k-case fuzz; W1 declined — would edit prior lines) · baseline
zero-drift both phases · scribe (228/228 pins post-fold; absent
`api_probe/` cite caught; r74 poller orphan flagged + reaped).

## Corrections of record

- Critic D1/D2 jwatch bracket + cite + measured-vs-inferred scoping.
- `died` is text-keyed (`assert_txt` absence separates it from `fatal`)
  — named discrimination hazard, pins carry independent provenance.
- Boundary seat ran a read-only substrate (`ufo-labrat` toolset) —
  produced a full source trace + falsifiable predictions instead of
  live cells. Profile note: boundary needs exec-capable seats.
- Baseline caveat: new cells insert inside the fatal tail per
  fatal-cells-last ordering (sequence-exact insertion, not block end).

## Next (r77 seeds)

`world:release()` in-cb SIGSEGV cell (fatal-tail); `setCallbacks`
mid-dispatch swap; `Fixture:destroy` drain member; drain-EC throw
retry + drain-EC write legality (boundary predictions);
`destroyb3` `isDestroyed` ordering; throw-before-queue ordering;
coroutine-wrap containment; `setMeter` under lock. r77 scout already
dispatched (`5d89aede`, wave-17 prep).
