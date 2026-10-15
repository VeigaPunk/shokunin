# r87 BASELINE (g2d) — frozen-tree regression replay

Repo: `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin`, HEAD at
dispatch = reconcile commit `fad0b1e` (pin the sha you froze).

Copy the tracked tree into `corpus/live/r87-baseline/tree/` (do not
mutate the worktree). Run `corpus/fixtures/run_battery.py` inside the
frozen tree **twice** (see `reports/round-86/r86-baseline.md` or
`reports/round-81/r81-baseline.md` for the established invocation and
row-count convention).

Report: rows replayed, byte-identical count vs committed receipts, any
drift row named individually. Write `reports/round-87/r87-baseline.md`.
Scratch only under `corpus/live/r87-baseline/`. No tracked writes, no
commits. All godot runs `timeout`-bounded and `--headless`.
