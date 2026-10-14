# game-dev-3d round 77 — depth move: mutation apply-order (doomed-RID voiding) + map_force_update reach + wait-ladder verdict groups

**Stamp.** 3D lane, round 77 (devin host, wave `shokunin-train-20261014-w8`, 8-lane seat set + named non-author verifier + Sol adjudication). Lane commits: work `35dfbe2`, hygiene `565318c` + `5e02b25` (comment corrections — falsified force-edge wording + mark-vs-phase mechanism), report-last pending.

## Work performed

Made mutation apply-order a measured axis: `mutate` accepts arrays of ordered sub-dicts through `_apply_mutation`'s unchanged fixed order; plus `map_force_update` getter/serve reach and wait-ladder verdict-groups derived from observed `_tuple_sig` partitions. `navagent3d_detour.gd` +501/−33 (`_mut_list` fan-out, `srv_get`/`ladder`/`_tuple_sig` schema, `map_force` key, 10 arms); `run_battery.py` +20/−0 (10 new CASES — pure additive). Battery 173/173 + 4 probes + Node 31/31; 163 prior rows byte-stable vs the r76 verifier's independent receipt.

**Measured: apply-order is load-bearing only through RID lifecycle — dead-write voiding, not emergence** (critic correction absorbed). `mut_ord_xform_renew` (transform then delete+recreate) serves the unmoved corridor + `region_transform=(0,0,0)` — the write dies with the freed RID; `mut_ord_renew_xform` serves moved + `(5,0,0)`. Verifier reproduced both directions on own geometry; boundary's all-6-perm census of {Rdel,Rrec,Rx03} gives THREE outcome classes (moved/unmoved/region-gone — `rec→del` frees the NEW region) plus a 2-frame empty-path interlude before recreate lands at f4. Order sensitivity decomposes **pairwise** (RID-rebinding adjacency + same-field last-wins); the one non-pairwise observable (+1 flush coupling) is order-inert; surviving-object and cross-object pairs converge.

**`map_force_update`**: getter edge collapses to same-turn (link stamped; region value same-turn but region_iter w1). Serve edge is a **mark-vs-phase race** (scribe mechanism): force drains the setter stage deterministically; a prior forcing READ marking the stamped-dirty map pulls the publish one frame early — cumulative read-every-frame callers see link jittered {w1 ~15-20%, w2} and region deterministic 3f→2f (9/9); **single-read-per-rung probes see NO collapse**. Mid-window second force collapses residual to 0. The tracked arm honestly skips the jittered w1 cell (author self-corrected after scout+critic caught it flaking inside the official battery).

**Verdict groups**: link bound=2 groups [2,2]; region bound=3 groups [3,2] — r76 edges re-derived from observed tuples. Groups are a serve-surface projection only (boundary masking witness: identical served tuple, divergent internals) — truth digests named as the open frontier.

## Landed changes

- `corpus/lessons/r77-mutation-apply-order.md`; `reports/round-77/` seat reports + adjudicator.
- Scribe: distinct dock-and-raft geometry + fresh-rung vs cumulative protocols — resolved the jitter to a mechanism (read-history perturbs the measured edge under force).
- Two post-verifier comment hygiene commits (`565318c`, `5e02b25`) — critic-falsified "unmoved" wording + scribe mechanism.

## Before → after measurements

| metric | before | after |
|---|---|---|
| apply-order | untested (fixed order assumed inert) | mechanism pinned: load-bearing only via doomed-RID voiding; 6-perm census → 3 outcome classes; pairwise decomposition |
| map_force_update | untracked | getter edge same-turn; serve edge = mark-vs-phase race, per-class (link {1,2} jitter / region −1f deterministic); read-history dependence documented |
| window edges | hand-pinned per-class constants | verdict-groups re-derive edges from data (link [2,2] bound 2; region [3,2] bound 3) |
| battery | 163/163 | **173/173** (+10 additive CASES) |

## SHONEN

- [x] Declared falsifiable axis-move (depth); "emergent seam" wording falsified → dead-write voiding (useful correction)
- [x] Named non-author replay — **verifier AGREE 6/6** on `35dfbe2` (own-geometry probe both directions; jitter reproduced 6/10-vs-4/10; 173×12 + prior-163×12 zero-mismatch)
- [x] No axis harmed — additive CASES; prior 163 rows byte-stable vs independent receipt; Node 31/31; seeds unchanged
- [x] Bounded claims (Godot 4.7.2 / 60tps; w1 jitter host-phase-biased ~15-20%; read-history perturbs forced edges; verdict groups hide non-serve state)
