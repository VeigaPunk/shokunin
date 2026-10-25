# kaidoku — round 2 report (2026-10-13)

**Shape:** tower-coordinated swarm on Devin — 16 lanes (`run_subagent`,
`subagent_general`), disjoint staging files in `.ufo/waves/kaidoku-r2/`;
parent integrated. Per the agreed review scheme, lanes 01–04 audited round 1
on every axis that moved; lanes 05–17 expanded.

## Axes moved

- **Discernment — verified by audit.** ~100 round-1 verify commands re-run:
  55+ byte-exact confirmations, **0 claims disproven**, every admit and every
  reject verdict upheld (the "entry point = main" reject was shown
  affirmatively false via `_start` prologue disassembly). Found: 1 factual
  erratum (34 Ghidra features), 2 defective verify commands, 1 systemic gap
  (criterion-5 labels not applied uniformly in same-day r1 entries — kept the
  criterion, recorded errata).
- **Expansion — improved.** 12 new knowledge entries; coverage map grew 11 →
  18 sections. Promoted to Core: **PE-via-Ghidra** (was inferred), **version
  compare machinery**, **recorded-crash mechanism**. New sections: Evidence
  schema, provider/capability matrix, firmware probe, frontier prerequisites.
- **Quality — improved.** Errata appended (append-only, no rewrites); audit
  upgraded a deferred inference to verified (full RELRO); r2 entries carry
  evidence_id-level citations throughout.

## Headline results

- **`~/.local/bin/jq` is benign**: sha256 byte-identical to the official
  jqlang/jq `jq-linux-amd64` 1.8.2 release binary; upstream build config
  literal in strings; textbook `main`. (07-jq-shadow)
- **PE proven on Ghidra without wine**: `rea analyze cli-64.exe` → 8 segments,
  142 procedures, deterministic re-run. (05-pe-e2e)
- **jq shadow + libjq context**: static jq = 2,279 procs vs libjq.so.1's 924
  (`.dynsym` exports 181 API syms; REA rebases .so vaddrs +0x100000). (17)
- **`inspect_recorded_crash` held but capped at 32 MiB** — all organic cores
  too big; pwntools provisioned ad-hoc via uv (recipe in lessons). (06)
- **Firmware needs `REA_BINWALK_COMMAND`** (3.1.x-gated) — catalog prose was
  misleading; REA has no firmware fallback path at all. (09)
- **Obsidian app.asar full graph**: 170-node app graph + 6,710-node semantic
  graph; summary→page→item paging demonstrated; ev_ refs are
  MCP-session-scoped. (10)
- **Version compare machinery held**: 8-dimension `compare_functions`;
  `record_pairs` verdicts are MCP-only; >40MB targets need
  `REA_GHIDRA_STARTUP_TIMEOUT_MS`. (08)

## Registry refresh (zero drift)

All r1-pinned values re-verified: doctor 18-check matrix identical, catalog
digest `85d80276…` intact, registrations aligned, env keys in place.
(audit 15)

## Discernment queue for round 3

Audit every r2 admit (especially the live-probe claims: ev ids, sizes,
timeouts); re-run a sample of r2 verify commands; check errata blocks landed
correctly; candidate frontier pushes: runtime-observation via self-launched
debug port, APK archive inventory, EVM synthetic carrier, organic-core
>32 MiB path.
