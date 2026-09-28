# kagi — round 10 (coverage axis-move)

Lane: kagi (secrets & vault ops) · axis owned: **freshness + calibration**;
this round moved **coverage 6 → 8** (lowest post-move cell). Repo:
`/home/vgpnk/projects/shokunin/kagi-shokunin`. Branch/commit: `round-10`.

## Move

`PROVINCE.md` §Surfaces was prose; nothing fired when a path disappeared,
changed mode, or when a file was **added** next to a declared one (the round-6
vector: `OPENCODE_CONFIG` is additive, discovery is not disabled, so a dropped
`~/.config/the-janitor/` file is loaded by the handler). The two `xdg-data`
artifacts were named "mutates legitimately; not pinned" — unfalsifiable.

Landed `corpus/surface-census.sh` v1 (868 lines) + `corpus/surface-census.tsv`
(35 rows: 20 asset / 15 runtime) + `corpus/state-shape.tsv` (22 rows) +
`corpus/knowledge/surface-census.md` (285 lines) + `corpus/lessons/round-10.md`
(140 lines).

- `verify` (default): declared kind + exact mode per path (`OK`/`DIVERGED`/
  `GONE`/`LINK`), `UNLISTED` for any undeclared direct child of the 4 enumerable
  dirs, 22 runtime shape pins (`SHAPE`/`ABSENT`/`SKIP`/`UNVERIFIED`), and a
  `CROSSCHECK` invariant against `drift-baseline.tsv` (one fact, one owner).
- `--verbs`: 7 probes over the handler's write-side verbs, scratch overrides
  only, no `op` exec. `--verbs --deep`: +3 probes with a real-world effect
  (`op run` plain/ref, `tac-register` no-replace) — operator-present by design.
- `--selftest`: 16 cases on a scratch tree.

## Measured before → after

| Claim | Before | After |
|---|---|---|
| Surfaces verified | none (prose) | `SURFACE_CENSUS: CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0)` exit 0 · sha256 `2586de87081a…` (script), `f8114ee44b15…` (census), `c84939050de8…` (shapes) |
| Undeclared-child detection | none | `UNLISTED` over 4 dirs, 16/16 children declared → 0 on a clean host; selftest case 5 proves it fires |
| Runtime state (db/log/locks/custody JSON) | unpinned | 22 shape rows: sqlite magic byte-exact, modes, table floor 12 (observed 20), row floors at ⅓ of observed (2/13/18/79), log size floor, JSON key names |
| Write-side verbs exercised | none | `--verbs` `CLEAN (pass=7 skip=3)`; `--verbs --deep` `CLEAN (pass=10 skip=0)`; `--selftest` `PASS (16 cases)` |
| Sibling gates | — | `DRIFT_PINS: CLEAN (files=15 symbols=19)` + `DRIFT_SELFTEST: PASS (13 cases)`; `TRANSCRIPT_SCAN: HITS=2 warns=2 cells=888` (known `xai-` prose collision, credential tables empty) |
| Reviewer adjudication | — | 62 claims: 49 VERIFIED / 0 WRONG / 9 STALE / 4 UNCHECKABLE; 5 stale prose items corrected in-repo |

## Findings (new corpus claims, all probe-backed)

1. `cmd_refs` redaction is a **prefix match** (`awk` L234): a value whose first
   five bytes are the ref scheme is echoed whole, plaintext tail included; and
   `export K=v` / ` K=v` / `lower_case=v` lines are silently *omitted* from the
   inventory. → SKILL decision table + anti-pattern, `op-cli-surface.md`.
2. `run` over a ref while signed out is non-deterministic: exit 1 in ~4 s, or
   **silent block** (exit 124 at a 25 s bound, both streams empty). Bound it.
3. A refused `cdp-bridge ensure` still creates the NMH **directory**
   (`mkdir -p` precedes the `-x` guard) — assert the file, not the tree.
4. A `?mode=ro` read of the live DB advances `opencode.db-shm`; the gate reads a
   `mktemp` copy of db+wal+shm instead.
5. `handler-on-disk-state.md`'s bound conflated content staleness with file
   mtime: `max(session.time_updated)` = 2026-09-21T04:57:08Z and rows 7/39/55/238
   are unchanged, while the DB *file* mtime reads 2026-09-28T19:59Z (a reader
   effect). Shape pins therefore use rows/tables, never mtime.

## L2 wave (9 lanes, one batched call)

planner · scout(surfaces) · scout(runtime state) · executor(verb probes) ·
executor(entry draft) · critic · sentinel · connector · reviewer — routes per
MISSION (planner/connector lunamax; scout/executor flash; critic/sentinel/
reviewer zfl).

What the wave actually bought:

- **Two gate defects caught before landing** by my own selftest: a dropped
  required table read as exit-neutral `SKIP` (false clean — a single combined
  sqlite query failed as a whole), and a fixture that did not scan the directory
  its case mutated. Both now pinned (cases 11, 5).
- **A third defect caught in a shipped data file**: the scouts and the sentinel
  independently reproduced that `state-shape.tsv` declared 22 rows while the
  loader saw 21 — a fused line (no trailing newline before an appended block)
  silently dropped the `daybreak-blue-access.json mode 600` assertion while the
  summary still read `CLEAN`. Fixed by splitting the row **and** adding a
  >5-field `die` guard to both loader loops (selftest case 14).
- **Critic CE3/CE5 real, fixed**: `SKIP` was fail-open on infra failure (now
  `UNVERIFIED`, exit 1; only `locked`/`busy` stays neutral) and the `--deep`
  custody check printed both sha256 digests (now digest-free). Four further
  clauses described a stale snapshot and are recorded as stale with reasons.
- **Sentinel: ship-with-changes**, with its `SKIP`-neutrality dissent recorded
  in `knowledge/surface-census.md` rather than resolved; it also flagged two
  dead knobs (`CENSUS_SELFTEST`, `THE_JANITOR_BIN`) — both fixed (`--deep` gates
  the probes now; `$JANITOR` is used by every probe invocation and `SQLITE3_BIN`
  is documented for the fail-closed selftest).
- **Connector**: no fleet-wide gate/exit-code convention exists (kagi's 0/1/2 is
  local); the global `~/.config/opencode/opencode.json` needs an integrator
  ownership ruling; kotoba owns the `AGENTS.md` checklist reading; kake keeps the
  profile lease (kagi's census keeps that dir presence-only).

## Safety

No vault read, no `op` exec in the default probe set, no `start`/`request`/
`stop`/`_serve`, no Chrome/CDP launch, no tmux session created, no write to the
real profile or state dir (scratch roots only). The `--deep` `tac-register`
re-run left the custody record byte-identical (`sha 8d57f3cd…`, mode 600, 545 B,
mtime unchanged) and refuses to create a record if none exists. No secret value,
ref path, account identifier or transcript cell entered any artifact.

## Residuals (named, not hidden)

Nothing schedules the gates; enumeration is one level deep over 4 dirs
(`~/.config/opencode` has 20 children and 4 declared, `~/.local/bin`, `~/.agents`
and the profile subtree are deliberately out); `xdg-cache`/`xdg-state` subtrees
(the hash-named `bun/@t@/*.pile`) are unpinned; row floors sit at ⅓ of observed
so a moderate shrink stays green; a hardlink is indistinguishable from the file
itself; 3 of 10 verb probes are `--deep`. Next planned move: **calibration**
(freeze the artifact revision before review — the critic burned a lane on a
stale snapshot; each cited artifact should carry its hash + line count).

## Report artifact hashes

`corpus/surface-census.sh` `2586de87081a…` 868 lines · `corpus/surface-census.tsv`
`f8114ee44b15…` 54 lines · `corpus/state-shape.tsv` `c84939050de8…` 48 lines ·
`corpus/knowledge/surface-census.md` 285 lines · `corpus/lessons/round-10.md`
140 lines.