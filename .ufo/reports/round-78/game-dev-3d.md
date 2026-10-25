# game-dev-3d round 78 — depth move: map-off permanence bounded to a measured +1200f (falsifier wired); callsite pair = sample-base shift

**Stamp.** Game-dev-3d lane, round 78 (devin host, wave `shokunin-train-20261014-w9`, 8-lane seat set + Sol adjudication). Lane commits: work `efcf33c`, report-last `87b456b`.

## Work performed

Extended the r76 `map_set_active(false)` permanent-stale finding into a falsifiable ladder + pinned the callsite pair as CASES. `navagent3d_detour.gd` +243: `mut_mapoff_ladder` (bound=5, groups=2 sizes=5,1 — per-rung `map_iter`/`link_iter` falsifier pins + 600f `iter_watch` canary), callsite pair `mut_ctx_resume` bound=2 / `mut_ctx_phys` bound=1 via `PhysMutator` (drains inside the firing tick), `_read_srv` gained the `map_iter` pin (the falsifier gap the scout/reviewer flagged). CASES +3 rows insertion-only → 176.

**Measured: permanence is a bounded regime, not a claim.** Link-kill under map-off stays stale through +1200f (boundary — zero `map_changed` emissions; bound extended 80x over r76's +15f); scribe's own harness (56 receipts, fresh-rung {0..600}f) agrees byte-exact. Reactivation replays the standard window: on+1 stamp / on+2 fresh serve, **wait-length-independent** — queued writes survive inactivity. `map_force_update` on an inactive map stamps the object iter without publishing; NO mark-vs-phase under inactivity (no sync phase to race) — cumulative ≡ fresh-rung protocols.

**Callsite pair = sample-base shift (critic correction absorbed).** bound=2 vs bound=1 is NOT an absolute latency fork: both writes apply at the same per-tick sync drain — the phys arm's drain-await consumes the pending-state sample a parked coroutine can't observe. Fixture comments corrected to same-drain/sample-base semantics. The full callsite boundary remains two-band {pre-sync +2, post-sync +3} (boundary) — the landed pair spans the pre-sync band.

## Landed changes

- `navagent3d_detour.gd` +243 (3 arms + PhysMutator + map_iter pin); `run_battery.py` +6 CASES.
- `corpus/lessons/r78-mapoff-permanence-callsite.md`; `reports/round-78/` 6 reports + adjudicator.

## Before → after measurements

| metric | before | after |
|---|---|---|
| map-off permanence bound | +15f (r76, "permanent" untested past it) | **+1200f** measured (boundary; arm ladder bound=5 rungs, falsifier wired via map_iter/link_iter pins) |
| callsite finding | r76-critic "+1 tick" prose | tracked CASES — resolved to **sample-base shift** (same sync drain; not an absolute latency) |
| falsifier witness | none in `_read_srv` | `map_iter` pin per rung + iter_watch canary + boundary's 1200f emission monitor |

## SHONEN

- [x] Declared falsifiable axis-move (depth); permanence confirmed as bounded regime — falsifier armed per rung
- [x] Non-author replay — verifier seat lost to rate limits; operator adjudicator replay on `efcf33c` = 176/176 + all 3 arms byte-verbatim on fresh scratch; critic independently verified merged diff 176/176
- [x] No axis harmed — 173 prior rows + 4 probes + Node 31/31 byte-stable (baseline 0-drift over 173×12 fields; operator replay)
- [x] Bounded claims (Godot 4.7.2 / 60tps / this host; +1200f is measured not "never"; callsite constants context-specific)
