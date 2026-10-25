# g2d-r99-reviewer

Lane repo: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Round: 99 | Author landing: 254e79dd (committed on main)
Gate role: reviewer

Independently re-derive every author claim from committed bytes: re-run the battery, re-derive law rows, check receipts. PASS/FAIL + findings.

Contract:
- Work on the lane's committed HEAD, not the author's worktree.
- File report at reports/round-99/r99-reviewer.md in the lane repo (do NOT commit; orchestrator commits).
- Full battery: `python3 corpus/fixtures/run_battery.py` from lane repo root; archive-tree runs go in a fresh git archive checkout under /tmp.
- Record load/host caveats honestly; never call a row green that measured nothing.
- Report must name the commit sha verified.
