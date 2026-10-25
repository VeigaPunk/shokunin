# g2d-r97-authorfinish — finish the r97 SceneTree lattice author round (edits already in tree)

Lane: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Original contract: `.ufo/waves/shokunin-train-20261015-w22/tasks/g2d-r97-author.md`
(scout `reports/round-97/r97-scout.md`, boundary `reports/round-97/r97-boundary.md`).

State found at resume — the author seat's edits are IN THE WORKING TREE, uncommitted:
- `corpus/fixtures/stree_lattice.gd` (fold of the frozen scout probe, per its header comment)
- `corpus/fixtures/r97_scene_a.tscn`, `r97_scene_b.tscn`, `r97_scene_marker.gd`
- `corpus/fixtures/run_battery.py` +65 lines: the `stree_lattice_*` case rows with pinned signatures
No `reports/round-97/r97-author.md` exists; the seat died before the green-x2 + report steps.

Your job:
1. `python3 -m py_compile`-equivalent sanity on the battery list + confirm every r97 row's
   fixture exists and arm tokens are intact (`--arm=` present per row).
2. Run the FULL battery twice on the working tree
   (`python3 corpus/fixtures/run_battery.py --godot godot --runs corpus/live/r97-author/runs`):
   both runs must be green, modulo documented flake classes only — record any flake with its
   evidence, never silently. All godot runs timeout-bounded and `--headless` (harness already does).
3. If a row fails on real defect: fix it in the author's spirit (boundary-surviving claims only)
   and document the fix; if an arm is flaky beyond documented classes, say so in the report —
   do not weaken pins to force green.
4. Write `reports/round-97/r97-author.md`: rows added, fixture provenance (scout sha), green-run
   receipt pointers, blockers. Zero commits. Return: report path, row count, green-run dirs, blockers.
