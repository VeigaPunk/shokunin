# game-dev-3d round 76 — coverage move: setter→server-sync window pinned as tracked CASES

**Stamp.** 3D lane, round 76 (devin host, wave `shokunin-train-20261014-w7`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `3ab09fd`, hygiene `8a67f71`, report-last `e417365` — identity `game-dev-3d-shokunin <g3d@shokunin.local>`.

## Work performed

The r75-measured setter→server-sync window, promoted from report-pinned to case-pinned. `navagent3d_detour.gd` +290/−6 (7 new CASES arms); `run_battery.py` +14/−0 (163 rows); new `map_active` mutate key + fs-folded setup gate. **163/163 + 4/4 probes + Node 31/31**; all 156 prior rows byte-identical.

**Per-class serve edges, strict constants** (four-way convergence — author, critic, boundary 54/54+24/24 in-process + 96 cross-process bisects, scribe own-geometry 65-run): link-class post-sync at **wait ≥ 2** (stale 0/1); region-class at **wait ≥ 3** (stale 0/1/2); agent `navigation_layers` **synchronous at 0**; `map_set_active(false)` **never transitions** — map leaves the sync iteration entirely (iter frozen, dirty never surfaces, `reachable=true` tuple served through +15f, NO latch — a permanent-stale regime distinct from `mut_latch_zombie`'s agent early-return). Reactivation flushes queued writes at the normal +2f edge. Inside-window zombie now durable: `mut_win_link` wait:0 serves AND pops idx 2→3 across the killed gate. **Same-value suppression** on all 8 probed setters (M-witness; `target_position` carve-out — unlatches+rematerializes). **Callsite qualifier**: `_physics_process` writes drain same-tick (one tick shallower).

Declared claim **CONFIRMED in substance, FALSIFIED as written twice**: "wait≥1 serves post-sync" still stale at +1f on every RID class; no single constant — per-class and callsite-scoped.

## Landed changes

- `corpus/lessons/r76-navagent-sync-window.md`; `reports/round-76/` all 9 seat reports + adjudicator.
- Twice-deferred `_check_tuple` extraction applied post-verifier (`8a67f71`, 4 copies → shared predicate; demonstrated byte-identical 78/78 + 19/19 mutants; full 163/163 re-verified on consolidated file).

## Before → after measurements

| metric | before | after |
|---|---|---|
| sync window | report-pinned "~2–3 frames" (r75) | case-pinned per-class {link:2, region:3, free_rid:2, map_off:∞, agent:0}, callsite-scoped |
| `map_set_active(false)` | scribe-noted no-bump observation | tracked permanent-stale arm (no edge, no latch, distinct regime) |
| same-value writes | unmeasured | suppression pinned on 8 setters via M-witness |
| battery | 156/156 | **163/163**, Node 31/31 |

## SHONEN

- [x] Declared falsifiable axis-move (coverage); falsified-as-written recorded honestly, corrected constants are what CASES pin
- [x] Named non-author replay — **verifier AGREE 5/5** on `3ab09fd` (163/163 + 4 probes + Node 31/31 + prior 156 unchanged)
- [x] No axis harmed — additive arms + one mutate key; consolidation byte-identical; gate semantics unchanged
- [x] Bounded claims (4.7.2.stable 60tps; coroutine/deferred context; `map_off` "permanent" = measured bound +15f, not unbounded proof)
