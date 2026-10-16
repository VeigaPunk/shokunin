# g2d-r97-author — author the SceneTree groups / signal connect flags / call_deferred timing lattice

Custody free (r96 landed 89f85ed8). Read scout reports/round-97/r97-scout.md + probes corpus/live/r97-scout/ + boundary reports/round-97/r97-boundary.md — encode only boundary-surviving claims (scout: 12 rows verbatim-ready).

- Groups (add_to_group/is_in_group/remove, call_group, notify), connect flags (DEFERRED/ONE_SHOT/PERSIST/REFERENCE_COUNTED), call_deferred vs deferred-call timing.
- Insertion-only run_battery.py; land fixtures into corpus/fixtures/.
- Battery green twice on final bytes (documented flakes only). Commit nothing. Report reports/round-97/r97-author.md. Return: report path, files, rows, blockers.
