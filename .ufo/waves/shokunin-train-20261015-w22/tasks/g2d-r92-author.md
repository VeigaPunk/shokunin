# g2d-r92-author — author the TileMapLayer lattice

Custody free (r91 landed 77d2f7e). Read scout reports/round-92/r92-scout.md + probe corpus/live/r92-scout/ + boundary 7a45a60 (nav row scheduler-sensitive — cold writes take 2 steps at high idle:physics ratio; update_internals/map_force_update NOT synchronous nav levers; null-TileSet SIGSEGV trigger; tombstone encoding).

- Author only boundary-surviving claims; nav rows use iteration gates/envelopes never fixed frames; SIGSEGV rows need required_stderr fragments; tombstone encoding pins.
- Insertion-only run_battery.py; land the scout probe into corpus/fixtures/.
- Battery green twice on final bytes (documented flakes only). Commit nothing. Report reports/round-92/r92-author.md. Return: report path, files, rows, blockers.
