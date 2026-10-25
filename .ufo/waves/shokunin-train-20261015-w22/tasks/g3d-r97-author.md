# g3d-r97-author — author the RID/refcounting lattice

Custody free (r96 landed dd054a2). Read scout reports/round-97/r97-scout.md + probes corpus/live/r97-scout/ + boundary reports/round-97/r97-boundary.md (headline: rc=1 is a fresh-allocate property; deferred free survives ONLY without load; decode non-zero DOES wait; pin the three-guard witness).

- Author only boundary-surviving claims; insertion-only run_battery.py; land fixture(s) into corpus/fixtures/.
- Battery green twice on final bytes (documented flakes only — navagent retarget/joints knife-edge classes). Commit nothing. Report reports/round-97/r97-author.md. Return: report path, files, rows, blockers.
