# kasegi-shokunin — round 7 report

Commit: `round-7` (`4ff0296`) in `kasegi-shokunin`. 6 files, +373.

## Gap closed: the ops tail (last name-only surface)

Six `ops/` scripts plus four `sighting*.sh` wrappers and the `shared.mjs`
constants were cited in corpus but never read. All read in full this round:

- **`corpus/knowledge/ops-invariants.md`** — shared constants
  (`BANNED=[cursor,opencode]`, `PARKED=[]` since the chatgpt lift → parked
  checks vacuous, `K3_SEATS=[judge,planner]`, `K3_TOKEN`, `TELEMETRY_EVENTS`,
  `gitMutationBlocker` codes); `validate.mjs` (schema-subset + lane
  referential + strict RFC3339); `registry-check.mjs` (7-check deep
  bijection — lane↔kx-card with the `mission_l1`→`mission-template.md`
  exception, `@role`→primary resolution, judge empty-bucket+honest.halt,
  grok `:low` pin); `reroute-drill.mjs` (simulation-only identity proof,
  `simulated:true` telemetry); `check-freshness.mjs` (26 h threshold, exit 1
  only on live-source staleness); sighting window semantics + the
  dead-glob caveat (0 uncompressed `.log`, 537 `.log.gz` → missions window
  is dead post-rotation; `sighting-missions.sh` capture-pane is the live
  view).
- **`corpus/knowledge/intake-and-finalize.md`** — the only two ops scripts
  that write beyond `ledger/`: `import-board.mjs` (pre-write binding —
  dataset sha256+count+refresh_run_id vs `refresh_evidence.json`; only the
  independent dataset filters records; per-source live/retained/stale
  freshness; past-DISCOVERED files byte-protected but S4 provenance drift →
  `provenance_drift` telemetry; two-phase writes, conflicts exit 1; new
  records land `lane:"executor"/DISCOVERED`) and `finalize-all.mjs` (batch
  claim sweep: DONE-filter → claim-check → commit → byte-proof →
  `claim-ready/` tag; sha-conflict never rewrites; single `--atomic` push).
- `SKILL.md` gained the "Ops integrity layer" section + 3 cited paths;
  `corpus/README.md` coverage map updated, gap marked closed; `LOG.md` +
  `corpus/lessons/round-7.md` recorded.

## Live-verification finding (cross-domain — reported, not fixed)

`node ops/registry-check.mjs` **fails today**: exit 1, seven `@role`
mismatches — one per kx card. The bugs are in the checker, not the fleet:

1. Nested `modelRoles` aliases resolve one hop only and keep YAML quotes:
   `fleet_volume` → `'"@ufo_deepseek_max"'` (literal double-quotes in the
   compared string), never re-resolved to `alibaba-token-plan/…`.
2. Cards pinned to `devin/swe-2:max` under the frozen 2026-09-15 charter
   mismatch registry primaries (`alibaba-token-plan/*`, `xai-oauth/*`).

Effect: the M4 deep-invariant gate is permanently red → treated as noise →
a real lane/card drift would land invisibly. `.omp/` + registry semantics
are kumitate's surface; fix belongs there.

`node ops/validate.mjs` → `OK (1088 programs, 10 lanes, 0 errors)`.

## Domain state

Corpus coverage of `~/Projects/bounties` ops/docs/ledger/claims/ is now
near-total: every `ops/*.mjs`/`*.sh` first-read; remaining depth is
per-program claim anatomy (274 program dirs, ~8 sampled) — diminishing
returns. Next-round candidates: `fleets/ufo-archive-2026/` (10 subdirs,
historical), or deepen claim-package sampling for new pattern classes.
