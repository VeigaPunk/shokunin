# game-dev-2d round 74 — LOVE physics interior-write lattice

**Stamp.** g2d lane, round 74 (wave `shokunin-train-20261101-w14`; recovery dispatch — gen-1 seats died 16:10Z, respawned 16:20Z; model mix: swe-2 author, deepseek-flash analysis seats, swe-2 baseline/verifier). Lane commits `ae6cb16` (arm) + `35dcbf7` (folds) + `b2b20f2` (report-last).

## Work performed

`love_battery.py` +292/−0 + new `corpus/fixtures/love_phys_probe/` (conf.lua + main.lua): 18 IW cells — Box2D writes inside beginContact/preSolve/postSolve vs exterior controls; cells spawned last, `*_unp` last; per-cell process isolation with partial-capture FAIL classification.

## Measured (independent verifier + boundary convergence)

- **Partition confirmed:** refused ×7 (catchable `IsLocked()==false` loveAssert — this build redefines b2Assert as a throw), deferred ×3 (destroy drains in the update epilogue, synthesized EndContact at `locked=false`), applied ×5 (setLinearVelocity; `contact:setEnabled` measurably suppresses impulse), fatal(lua) ×2, captured ×1.
- **Corrections folded:** `fatal` scoped to fatal(lua) — the boundary's uncontainable own-fixture sensor→solid morph is SIGABRT→`died` (critic C1/C2); drain wording fixed (inside update, not after — reviewer D1); simplifier D1–D3 byte-identical (`58af4e7e` preserved).
- **Boundary extensions:** re-entrancy defeats the lock (nested `world:update` inside beginContact → subsequent setPosition *applied*); destroyed handles totally unusable; carried fifo-SIGTERM-immune guard falsified for LOVE (EINTR, receipt completeness is the verdict carrier).
- **Falsified honestly:** the brief's containment assumption — same write is refused in-callback, escape-and-recover at pcall(update), fatal uncontained (containment-level-relative; C3 additive cell deferred to r75).

## Remaining / next frontier

- r75 seeds: critic C1 additive twins (`bc_destroy_unp`, `bc_setvel_unp` → deferred/applied rows), C3 update-level containment cell, `esc_fn` pin on unp rows, joints/setFilterData/preSolve-return-false, `world:destroy()` double-destroy.
- Bounded: LOVE 11.5-3 (Arch), LuaJIT 2.1.1788460057, pygame 2.6.1 control untouched, this host.

## Seat record

9/9 landed: author, scout (prior-gen verified), boundary, critic, reviewer, simplifier, scribe (superseded dead draft), verifier, baseline. Verifier AGREE 13/13 on `ae6cb16`; baseline zero-drift on freeze `1275746` (godot 88, love 19, pygame 80). Adjudicator: ADMIT-corr.
