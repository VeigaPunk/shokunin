# g2d-r98-simplifier

Lane repo: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Round: 98 | Author landing: 9d421fb2 (committed on main)
Gate role: simplifier

Find behavior-preserving folds in the new block; prove each with a fresh run before/after. PROVEN/REFUTED per fold + net line delta.

Contract:
- Work on the lane's committed HEAD, not the author's worktree.
- File report at reports/round-98/r98-simplifier.md in the lane repo (do NOT commit; orchestrator commits).
- Full battery: `python3 corpus/fixtures/run_battery.py` from lane repo root; archive-tree runs go in a fresh git archive checkout under /tmp.
- Record load/host caveats honestly; never call a row green that measured nothing.
- Report must name the commit sha verified.
