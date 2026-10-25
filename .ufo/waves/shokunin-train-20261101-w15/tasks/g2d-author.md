# r75 AUTHOR (g2d) — deferred interior-write cells + containment lattice

Read SHARED.md + r74 author/adjudicator/critic first. The deferred
critic cells are the ordered frontier.

ARM — `love_battery.py` + `love_phys_probe/` extension (insertion-only;
prior cells byte-identical; fatal cells still last, per-cell process
isolation kept):
- critic C1 additive twins: `bc_destroy_unp` (unprotected destroy inside
  a callback — predicted deferred-drain class) and `bc_setvel_unp`
  (predicted applied). Pin the MEASURED class, falsify the prediction
  honestly if it lands elsewhere.
- critic C3 containment-level cell: pcall wrapping `world:update` vs
  pcall wrapping the interior write — the same write reads as
  `refused` under one containment and `refuse-with-step-abort` under
  the other. Pin the level-relative class partition.
- `esc_fn` pin on unp rows: the escape-function identity as evidence.
- joints surface (stretch): joint create/destroy inside callbacks;
  `Fixture:setFilterData`; `preSolve` return-false — arm only what
  lands falsifiably, record the rest as blocked.
Report -> reports/round-75/r75-author.md.
