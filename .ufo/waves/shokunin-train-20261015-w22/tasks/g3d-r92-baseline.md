# r92 BASELINE (g3d) — frozen-tree regression replay

Repo: `/home/vgpnk/Projects/shokunin/game-dev-3d-shokunin`, HEAD at
dispatch = reconcile commit `c218823` (pin the sha you froze).

Copy the tracked tree into `corpus/live/r92-baseline/tree/` (do not
mutate the worktree). Run `corpus/fixtures/run_battery.py` inside the
frozen tree **twice** (see `reports/round-90/`/`r91` baseline reports or
the battery README for the established invocation; backend projects are
generated per battery convention).

Report: rows replayed, byte-identical count vs committed receipts, drift
rows named individually. Write `reports/round-92/r92-baseline.md`.
Scratch only under `corpus/live/r92-baseline/`. No tracked writes, no
commits. All godot runs `timeout`-bounded and `--headless`.
