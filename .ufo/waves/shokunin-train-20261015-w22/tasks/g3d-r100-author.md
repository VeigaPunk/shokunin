# g3d-r100-author — CAPSTONE: author the --fixed-fps scheduler lattice (final round)

Custody free (r99 landed f1ff626). Read scout reports/round-100/r100-scout.md + probes corpus/live/r100-scout/ + boundary reports/round-100/r100-boundary.md — encode only boundary-surviving claims.

- The headless main-loop rate surface: --fixed-fps N as a deterministic scheduler, incl. proj_cap (max_physics_steps_per_frame=1), proj_jit0, proj_dsfalse bakes.
- Insertion-only run_battery.py; land fixtures into corpus/fixtures/.
- Battery green twice on final bytes (documented flake classes only). Commit nothing. Report reports/round-100/r100-author.md. Return: report path, files, rows, blockers.
