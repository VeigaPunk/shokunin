# Seat: g2d r88 verifier-r2 — independent verification of folded bytes

Lane: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
Head: fd59c11 (fold commit — verify THESE bytes)

You are the non-author verifier on the folded tree. The dossier needs a clean run of the actual admitted bytes, with the previously-blocking findings exercised.

## Fold contents to verify
1. F1 MP ports now pid-derived `40000 + pid % 20000`, `rc_s`/`rc_c` failure guards — run the mp_offline/mp_loopback/mp_spawner arms repeatedly under concurrent load; no ENet-create errors may pass.
2. F2 `sprite_phys`/`light_props` v!=0 sync — pins must hold across Case A/Case B startup shapes (idle hogs + `--delay` style). 17+ reps each.
3. F3 `ray_through_occluder` ray now crosses the occluder polygon.
4. F4 `audio_pos` liveness assert — prove it fails if `play()` is removed (negative control).
5. F5 `input_lattice_phys_peer` 6-payload envelope — run under heavy hog load, try to observe a 7th mode (would fail loudly) and several of {0..5}.
6. Full battery 215/215 on final bytes, ideally under load; `r88_expected_errors_all_matched` gate green.

## Deliverables
- `reports/round-88/r88-verifier2.md` — verdict (VERIFIED / VERIFIED-WITH-RESERVATIONS / FAILED), per-item evidence.
- `corpus/live/r88-verify2/` — runs, hogs log, manifest.
- No tracked writes beyond the report. Kill all hogs on exit.

Read the task file; then operate autonomously. Return: report path, verdict, files changed, blockers.
