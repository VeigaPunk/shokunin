# kaidoku — round 3 report (2026-10-13)

**Shape:** tower-coordinated swarm on Devin — 16 lanes (`run_subagent`,
`subagent_general`), disjoint staging files in `.ufo/waves/kaidoku-r3/`;
parent integrated. Lanes 01–04 audited round 2 on every moved axis; lanes
05–16 expanded.

## Axes moved

- **Discernment — verified by audit.** ~31+ verify groups re-run: 29+
  confirmed, 0 contradictions, every r2 admit/reject verdict upheld. Audit
  surfaced 4 real errata (jq-shadow search mechanism, `capability_unavailable`
  exit-code, firmware verify defect, `compare_functions` "on CLI" attribution)
  — all appended as `## Errata (round 3)` blocks, nothing rewritten. The
  consistency audit caught index/province drift (filename break, stale pins)
  — all fixed.
- **Expansion — improved.** 12 new knowledge entries; coverage map 18 → 23
  sections. New held surfaces: runtime observation (CDP, both legs), EVM
  selectors, PE-ARM64, synth-carrier macOS ops ×3, .node addon taxonomy, APK
  inventory + archive→native bridge, AppImage shape, MCP retained-evidence
  session incl. real `record_pairs` verdict, 6 verb families.
- **Quality — improved.** 2 new admission criteria (10: available≠exercised;
  11: zero-findings vs inventory-exclusion). SKILL.md grew real decision
  table + typed error-pattern table + checklists — all SHONEN gates now
  closed; lane is eligible for roster promotion.

## Headline results

- **jq-shadow provenance RESOLVED**: installed 2026-10-03 18:34 by agent-2
  of the kimi-code bootstrap swarm (wire.jsonl transcript + same-second
  cohort + gh device-id timestamp). Benign, intentional.
- **obsidian.asar is the real app**: 45 literal `ipcMain` ops verified 1:1,
  permissive BrowserWindow prefs with live mitigations documented; 47.7MB
  evidence bundle; honest coverage ceiling (app.js OOMs at 8GiB).
- **Evidence ids are content-addressed**: identical `ev_*` reproduced on
  re-analysis across sessions (libjq, jq-shadow, obsidian).
- **`record_pairs` `status:changed` reached via live MCP session** — requires
  ALL bundle members paired; partial → `unknown`.
- **typora app.asar** = bytenode `.jsc` loader (99.4% of bytes) — zero-IPC
  summary was exclusion, not finding. New frontier: bytecode decompile.

## Errors found & corrected in-flight

`capability_unavailable` exits 1 not 0 (retryable field is the real
differentiator); `search` needs `--mode regex --pattern '.*'` for full
enumeration; `--encoding`/`--archive`/`--address` are positional on several
verbs; `inputJson` refuses `/dev/stdin`; `pkill -f` self-matches.

## Roster status

All four SHONEN.md gates are checked. Probation rounds complete (r1 curation,
r2+r3 audit-and-expand). **Eligible for shokunin promotion — operator
decision required** (protocol's non-author review was served by the fresh
audit lanes each round).
