# r87 AUTHOR (g2d) — input event/action lattice (20 verbatim arms + bimodal envelopes)

Arm the r87 scout's lattice: `reports/round-87/r87-scout.md` + evidence
`corpus/live/r87-scout/` — `proj/input_lattice.gd` (854 lines, 23 arms,
sha256 2b68531d…), `run_arms.py`/`gen_pins.py`/`pins.json`,
`author-rows.py.txt` + `make_author_rows.py` (**20 verbatim CASES rows +
`null_edge` whitelist, exec-checked**), `arms-flaky-r10.json` (×10 mode
census), `proj/r87_edge.gd` (`jpbe`, `jmode`), `ei_bound.gd`.

Repo: `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin`. Harness:
`corpus/fixtures/run_battery.py` + `.gd` probes (182 rows green at HEAD).
Land the probe at `corpus/fixtures/input_lattice.gd`; append CASES rows
insertion-only. Cosmetic note: the probe prints `R83 arm=…` banners —
harmless, upstream of the PASS line.

Author directives from the scout (binding):
- Land the 20 verbatim rows from `author-rows.py.txt`.
- **Do NOT pin `press_phys`, `release_edge`, `ui_ns` as constants.** Each
  is bimodal with both payloads enumerated in `arms-flaky-r10.json` — arm
  them as mode-envelope cells (both payloads whitelisted, per the r90
  bimodal lesson; ≥6 reps each before you write the envelope).
- The `event_index` refusal boundary (§4) needs 1 whitelisted ERROR —
  arm it as an edge arm if you take it.
- `jpbe`/`jmode` edge arms (`r87_edge.gd`) are deterministic refusals —
  optional bonus cells, byte-stable ×3 already.

After landing: run the FULL Godot battery ≥2× — prior 182 rows
byte-identical; new arms rep-stable ≥3 reps (envelopes: distribution
stable). Report → `reports/round-87/r87-author.md` with counts, the
counting commands, and any scout-claim correction (disclose). Do NOT
commit.
