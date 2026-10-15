# r89 SCOUT (g2d) — forward reconnaissance from the r88 authorability census

Repo: `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin`. You are the
r89 scout. First read `reports/round-88/r88-scout.md` — it is an
**authorability census** of candidate surfaces. Take its top-ranked
authorable candidate (or the census's own recommendation) and pre-measure
it: build probes, run cells ×3 reps (×6 for lifecycle/teardown cells),
byte-stability, per-backend or per-runtime splits where relevant.

Also read `reports/round-87/r87-scout.md` remaining unknowns — if its
unanswered edges (joypad device filter, SubViewport cursor, exact_match
granularity, `event_is_action`) rank above the census pick, you may split
the round's scout between both; name your choice and reason in the
report.

Contract: leaf seat — zero tracked writes; scratch under
`corpus/live/r89-scout/` (`probes/`, driver, `runs/` with per-cell
rc/stdout/stderr sidecars, `manifest.sha256`, `RECEIPTS.md`); report →
`reports/round-89/r89-scout.md` with headline claims table, measured
values verbatim, author directives (verbatim-ready vs bimodal →
envelope), remaining unknowns. All godot runs `--headless`,
`timeout`-bounded; no stray processes at exit. [O]/[I]/[?] labels.
