# kumitate-shokunin — round 1 report

**Lane:** orchestration & tooling (OMP task/hub dispatch, ufo-fsd scripts,
`crates/ufo-core-runtime`)
**Scope inspected:** `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`
`scripts/` (74 entries, incl. `ufo-sighting-lib/` 25 files,
`collect-omp-native-handoff-lib/` 6 files), `config/ufo.json`
`sighting.dispatch`, `crates/ufo-cli` command surface, `crates/ufo-core-runtime`
(93 .rs files, lib.rs module map).

## Deliverables

- `SKILL.md` rewritten from seed stub → sourced playbook: dispatch-shape
  decision table (4 shapes), per-script vocabulary, failure-telemetry
  vocabulary with sources, 16 anti-patterns, working rules.
- `corpus/` seeded per `/home/vgpnk/projects/shokunin/CORPUS.md`: README
  index + 4 `knowledge/` notes + `lessons/round-1.md` (gaps filed).
- `LOG.md` round-1 entry appended. Commit `round-1` in the child repo.

## Key findings

1. **Three dispatch shapes, one judge.** Swarm wave (one batched `task`
   call, ≤100 lanes, advisory evidence only), sighting mission (tmux wall
   lifecycle, display-only), native judged round (frozen topology 6–16
   proposal seats + 4 core ≤ 20, `ufo judge-handoff` sole judge). Fixture
   `self-iter` is never native evidence.
2. **Wave lifecycle is plan/run/record/settle/collect** with a
   registry+dispatch file pair published sidecar-first; the collector's
   `stale_dispatch_pair` refusal covers the crash window. `settle` mints
   honest `cancelled`→`aborted`, never `failed` from absence.
3. **Telemetry vocabularies are single-sourced**: `ENTRY_FAILURE_CLASSES`
   (7 classes) in `ufo-mission-result.mjs`; `CAPACITY_FAILURES` (3
   classes) is the only fallback-advance justification; `lane_timeout` is
   never capacity. `classifyFailure` mirrors Rust `native_text.rs`
   exactly — needle table, digit-guarded codes, word-boundary scan.
4. **Singleton discipline is mechanical**: `acquireSingletonLock` binds
   pid+starttime+bootId via inode hardlink under a `.takeover` ticket;
   fleet-dispatcher solely owns `pending-work.json`; watchdogs repend
   through it. The "never spawn a second L1" anti-pattern is enforced by
   I1 + twin semantics (sibling mission gets its own sole L1, judges never
   merge).
5. **Drift found:** installed `ufo` skill text says 128 swarm lanes; the
   script header and `config/ufo.json` say 100 (operator contract stricter
   than kimi's 128). Config also carries `minLanes: 64` (round target)
   beside the `waveMinLanes 16`/`waveMaxLanes 100` band —
   `ufo-stale-watchdog` already burned once on a hardcoded floor.

## Gaps filed (corpus/lessons/round-1.md)

fleet-dispatcher settle/successor internals, `ufo-core-runtime`
loop-driver + native admission internals, native-trial launch sequence,
the-tick ops beyond `path_ping`, `omp-global-config.mjs` alias resolution.
