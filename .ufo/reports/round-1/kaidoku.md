# kaidoku — round 1 report (2026-10-13)

**Shape:** tower-coordinated swarm on Devin — 16 read-only curation lanes
(`run_subagent`, `subagent_general`), each writing one disjoint staging file in
`.ufo/waves/kaidoku-r1/`; parent (this session) integrated.

## Axes moved

- **Expansion — improved.** 14 knowledge entries (~160 candidate facts)
  admitted across 11 coverage sections; corpus went from empty to covering
  REA service/connection, CLI/self-docs, skill contract, provider readiness,
  ELF (e2e), PE, ASAR, packages, managed assemblies, crash evidence.
- **Quality — improved.** Every admitted claim carries source + verify command
  + verified-at; 4 deliberate rejects retained as calibration; QUALITY.md grew
  3→9 admission criteria and 0→5 weak signals; PROVINCE/SKILL filled with only
  verified claims (unprobed surfaces sit in Frontier).
- **Discernment — improved (pending round-2 audit).** Admits/rejects per
  candidate are recorded; per the agreed review scheme, round 2 audits every
  moved axis.

## End-to-end task (shonen checklist)

`rea analyze`/`search`/`decompile` on `/usr/bin/jq` via Ghidra — 30 segments,
167 procedures, 190 strings, ~5.5s per call; `decompile 0x103fa0` recovered
jq's `process()` loop; session lifecycle (`/tmp/rea-ghidra-*` ephemeral) and
`--snapshot` semantics verified. Plus `analyze_javascript_application` e2e on
`default_app.asar` (evidence `ev_2628de89…`).

## Notable findings

- `~/.local/bin/jq`: unowned, statically-linked, stripped ELF shadowing the
  packaged `/usr/bin/jq` (same `jq-1.8.2` version string) — highest-value live
  target surfaced by the round.
- `doctor healthy:false` decomposed: 6 `config_drift` checks only; Ghidra
  satisfies the engine floor alone. `skill:stale` = missing `~/.claude/skills`
  destination, not content drift.
- 174 zstd coredumps retained (~4 GB, decaying oldest-first); 3 organic
  crashes (godot/waybar/localsearch) are real RE targets.
- Blocked-on-operator (documented, not worked around): pwntools Python for
  `inspect_binary_layout`; Binwalk/Unblob for `extract_firmware`; AnyCPU
  managed assemblies rejected by `inspect_managed_artifact`; IDA/Hopper absent.

## Discernment queue for round 2

Audit every round-1 admit/reject on the moved axes; spot-check verify commands
by re-running a sample; review the 4 rejects for correctness; confirm no
admitted claim lacks a resolvable source.

## Watchdog / verification

- Lane repo clean tree; commit `a43d442` on master (identity
  `kaidoku-shokunin <kaidoku@shokunin.local>`).
- No placeholder `<...>` tokens remain in SKILL.md / PROVINCE.md /
  corpus/README.md (scan run post-integration).
- All 16 lanes wrote exactly their assigned file; no stray writes
  (one `asar extract-file` cwd side-effect was self-cleaned and recorded as a
  lesson); zero `/tmp/rea-ghidra-*` orphans post-wave.
