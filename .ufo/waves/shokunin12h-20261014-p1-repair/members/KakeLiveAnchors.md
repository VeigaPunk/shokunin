# KakeLiveAnchors

Advisory census only. Not a native judge verdict, lane round report, receipt, or admission. No kake file was edited. No test, build, lint, or formatter was run. No fetch. No secret or session content was read.

## Binding

- Lane HEAD: `b0feb30886585d8df6d4671845a2d18989ca722b` (matches `baselines.json` kake.round 19). Worktree extra: untracked `plans/` only.
- Source tree: `/home/vgpnk/Projects/ufo-fsd-alpha` (the path `../ufo-fsd-alpha` from the fleet root). Measured 2026-10-14T23:40:29Z.
- Command: `git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD`
- Measured: `964f443ee53df0ce06bd689af01f0dea031b01f9` (`--short=8` = `964f443e`, unique).
- Cited scribe/charter paths are clean at that commit. The worktree is otherwise dirty (not used as a content pin): `README.md`, `config/ufo.json`, `crates/ufo-core-runtime/bundled/config.json`, `crates/ufo-core-runtime/bundled/omp-seat-routing.json`, `scripts/fleet-dispatcher.test.mjs`.
- `~/Projects/origin-work` is absent. The only `ufo-fsd-alpha` checkout under `~/Projects` is the one above.
- Round-18 migration annotations are existing state. This census does not repeat them.

## Result

No currently live OMP-derived **line** pin in kake is line-drifted against this revision. The claims that still read as current are either HOLD, stale `--src` / citation-to-deleted, a genuine runtime defect, or unprovable without a forbidden fetch. No kake gate implementation file needs a change from this seat.

## Measured claims

### LA-1 HEAD prefix — HOLD

- Cite: `SCORECARD.md:21-22`, `LOG.md:404`, `corpus/lessons/round-18.md:17-18`. Claim: live origin tree `~/Projects/ufo-fsd-alpha`, HEAD `964f443e`.
- Command / output: `git rev-parse HEAD` → `964f443ee53df0ce06bd689af01f0dea031b01f9`; `git rev-parse --short=8 HEAD` → `964f443e`; `git rev-parse --verify 964f443e^{commit}` succeeds.
- Class: HOLD. Not line drift. Not a defect of the prefix claim.
- Proposed anchor: full hash `964f443ee53df0ce06bd689af01f0dea031b01f9`. Do not treat dirty worktree bytes as that commit.
- Owner: kake prose (already correct). No gate edit.

### LA-2 ledger absent on the new tree — HOLD (negative)

- Cite: `LOG.md:404-405`, `corpus/lessons/round-18.md:18-19`, SCORECARD move-log round 18. Claim: the re-rooted tree has no `.ufo/charter-scribe/ledger.jsonl`.
- Command / output: `ls` of `/home/vgpnk/Projects/ufo-fsd-alpha/.ufo/charter-scribe` and of `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha/.ufo/charter-scribe/ledger.jsonl` → both "No such file or directory". `.ufo/` exists and contains `cache/` and `sighting/` only (names only; cache bodies not read).
- Class: HOLD. The round-18 sentence "dead, not moved" is still true. Not line drift.
- Why it stays absent: `scripts/charter-scribe/sync.mjs:25` documents telemetry at `.ufo/charter-scribe/ledger.jsonl`; `sync.mjs:595-606` writes `join(cfg.repo, ".ufo/charter-scribe")` then `ledger.jsonl`. `scripts/charter-scribe/config.json:3` still sets `"repo"` to `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`. That root does not exist, so a beat cannot land a ledger on the new tree.
- Proposed anchor: symbol `ledgerDir` at `sync.mjs:595`, configured root `config.json:3`. Do not invent a ledger on the new tree.
- Owner: upstream `ufo-fsd-alpha` (stale `repo` pin). Kake must not edit that checkout.

### LA-3 ExecStart path — stale `--src`, not line drift

- Cite: `corpus/knowledge/keeper-timer-inert.md:91`. Still live (no `r18 re-census` erratum on this line). Claim: writer `ExecStart=…/origin-work/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs`.
- Source quotation matches. `scripts/charter-scribe/systemd/charter-scribe.service:10-11` (clean at HEAD):

```
WorkingDirectory=/home/vgpnk/Projects/origin-work/ufo-fsd-alpha
ExecStart=/home/vgpnk/.local/share/fnm/aliases/default/bin/node /home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs
```

- Resolution fails. `ls` of that WorkingDirectory → absent. `config.json:6` likewise pins `charterRepo` to `/home/vgpnk/Projects/origin-work/charter-ufo-fsd`, also absent.
- The script symbol did move. Relocated file exists: `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs`, 844 lines, 37255 bytes, sha256 `66087705e69e09dc41ac23f473e9e549433432526a4e67f7f8b2e55313cf79fa`.
- Class: stale `--src` in the unit file, repeated by kake as a current writer path. Not line drift (kake cites no line number; the string is still at `service:11`). Not a kake misquote of the unit text.
- Proposed anchor if a beat is re-homed: script `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs`; unit text that must change is `service:10-11` and `config.json:3,6`. Those files are outside kake write scope.
- Owner: `ufo-fsd-alpha` for the unit/config pins. Kake erratum only (parent / HistoryClaims), not GateRepair.

### LA-4 timer "enabled, active, 6h" — genuine defect (runtime), cadence symbol HOLD

- Cite: `keeper-timer-inert.md:90` and `:108-109`. Present tense: `charter-scribe.timer` enabled, active, 6h; "the scribe keeps writing new beats".
- Source cadence HOLD: `scripts/charter-scribe/systemd/charter-scribe.timer:2` "every 6 hours"; `:6` `OnUnitActiveSec=6h`. 190 bytes, clean at HEAD.
- Runtime does not match. Commands and output:
  - `ls ~/.config/systemd/user/charter-scribe.{service,timer}` → both absent (same for `webzites-keeper.service` and `webzites-probe.timer`, already in the declared-absent set).
  - `systemctl --user show charter-scribe.timer -p Id -p UnitFileState -p ActiveState -p FragmentPath` → `Id=charter-scribe.timer`, `ActiveState=inactive`, `FragmentPath=` empty, `UnitFileState=` empty.
  - `systemctl --user show charter-scribe.service` → `ActiveState=inactive`, `FragmentPath=` empty, `WorkingDirectory=` empty.
  - `systemctl --user list-unit-files 'charter-scribe.*' 'webzites-*'` → `0 unit files listed`.
  - `systemctl --user list-timers --all` → only `ai-usage.timer`. No charter-scribe timer.
- Class: genuine defect of the still-live "enabled/active/keeps writing" claim. Not line drift: the 6h symbol is still `timer:6`. The dated verbatim block at `keeper-timer-inert.md:16` (2026-09-28T22:18Z) can stay historical; the present-tense section cannot.
- Proposed anchor: source cadence `charter-scribe.timer:6`; runtime status = not installed, inactive, as of 2026-10-14T23:40:29Z.
- Owner: kake prose erratum. Upstream unit install is operator/OMP, not this seat.

### LA-5 `docs/charter-ufo-fsd` — surviving relative path; sha inference unprovable

- Cite: `corpus/knowledge/origin-repos.md:22`. Claim: `plazir27.kimi.page` maps to `repos/ufo-fsd-alpha/docs/charter-ufo-fsd`, inferred sha mismatch vs both charter clones. The `webzites/repos` host is already marked absent at `origin-repos.md:5`. Line 22 itself has no r18 erratum.
- Local tree exists: `/home/vgpnk/Projects/ufo-fsd-alpha/docs/charter-ufo-fsd`, 22 files. `index.html` 53047 bytes, 714 lines, sha256 `43d321f91cf018dc75d6f0052a573e3f198b0c1a159e0615574f8e0eecc5296b`. `vessel.webp` 121710 bytes, sha256 `d32af1edf0e9b7b0e3669bfd2939cde60447f9d7b802b90d5a9e1c733cae1954`.
- `rg -n 'scribe beat' docs/charter-ufo-fsd` → no matches. This copy is not the beat-stamped page the PQ-12 pin describes.
- Charter clones `~/Projects/charter-ufo-fsd` and `~/Projects/origin-work/charter-ufo-fsd` are absent. No fetch was made, so the sha-mismatch inference was not remeasured.
- Class: citation-to-deleted for the `webzites/repos/ufo-fsd-alpha` host. Not line drift (no line number). Sha mismatch is unprovable, not a proven genuine defect.
- Proposed anchor: `/home/vgpnk/Projects/ufo-fsd-alpha/docs/charter-ufo-fsd/index.html` at the sha256 above. Do not pin the old inference as current.

### LA-6 charter commit hashes — not in this tree; unprovable

- Cites: `61d0ce6` at `keeper-timer-inert.md:92`; pin `charterGhpDeploy` `9c28d293de181d14898570264d2c4e523ce34255` in `freshness-pins.json:30`. These are charter-repo commits, not claimed as alpha HEAD.
- Command: `git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse --verify <sha>^{commit}` for `61d0ce6`, `9c28d29`, `9c28d293`, `a8f1e2b`, `7c243a1d`, `fb365e38` → `fatal: Needed a single revision` for each. `964f443e` is the only one that resolves.
- Class: not line drift. Not a falsified alpha hash. Unprovable locally because the charter checkout is gone and fetch is forbidden.
- Owner: kake armed-watch pins stay historical until a local charter checkout exists. Do not re-pin them from memory.

### LA-7 selftest path — HOLD

- Cite: `scripts/freshness-sweep.mjs:1063` and `:1106`. Fixture requires `~/Projects/ufo-fsd-alpha` to resolve.
- Measured: directory exists; HEAD as in LA-1.
- Class: HOLD. The gate has no `--src` / `UFO_SRC` resolver (`rg` over `scripts/freshness-sweep.mjs` hits only this fixture). It does not evaluate OMP line pins, so a missing source-root fallback is not a defect of this instrument.
- Owner: GateRepair should not invent a resolver from this census.

### LA-8 `omp usage --json` / `omp stats.db` — not an alpha line pin

- Cite: `corpus/knowledge/speedrun-pipeline.md:18-19`. Names `omp usage --json` (30s cache) and `omp stats.db` as webzites speedrun sources. `speedrun.mjs` is already declared absent (`speedrun-pipeline.md:4`).
- No kake line number. `rg 'usage --json'` under `ufo-fsd-alpha/scripts` and `packages` → no match. `stats.db` occurs as an isolation exclude name (`config/ephemeral-fleet.machine.json:30`), not as a cited line. Unrelated `30_000` timeouts in `fleet-dispatcher.mjs` were not treated as this cache.
- `command -v omp` → `/home/vgpnk/.local/bin/omp` (binary, not read; `omp usage` not run — it can touch credentials).
- Class: citation-to-deleted webzites behavior, not OMP line drift, not a proven symbol defect.
- Owner: HistoryClaims for the already-annotated webzites cite. No new alpha anchor.

## Explicit non-claims (basename collision rejected)

Standing `src/cli.mjs:<line>` / `src/fleet.mjs` / `src/probe.mjs` / `src/reconcile.mjs` pins are webzites cites. The host is already in the declared-absent set (`kake-before.json` stdout: `~/Projects/webzites/src/cli.mjs` and siblings). They are not OMP-derived.

`rg` for `loadFleetConfig|mergeProbeResults|cmdProbe|function saveProbe` in `/home/vgpnk/Projects/ufo-fsd-alpha` → no matches. `src/cli.mjs` does not exist in that tree. Substrate `bin/cli.mjs` files share a basename only. Classifying those pins as line drift against `substrates/*/bin/cli.mjs` would be a false measurement.

Owner: KakeHistoryClaims. Not GateRepair.

## Adjacent count (not an alpha source line)

`SCORECARD.md:20` still says `~/Projects` holds 14 children. Pin `projectsChildrenSet` is 14 names (`freshness-pins.json:114-129`), including `ufo-fsd-alpha` (membership HOLD).

- Command: `ls -1 /home/vgpnk/Projects | wc -l` → 30. Removed from the pin: none. Added (16): `omegag`, `omegag-ds-feedback-01a13c4b`, `omegag-ds-gui-actions-01a13c4b`, `omegag-ds-gui-audio-01a13c4b`, `omegag-ds-gui-device-01a13c4b`, `omegag-ds-gui-profiles-01a13c4b`, `omegag-ds-gui-shell-01a13c4b`, `omegag-ds-haptics-01a13c4b`, `omegag-ds-hid-01a13c4b`, `omegag-ds-inject-01a13c4b`, `omegag-ds-input-01a13c4b`, `omegag-ds-mapper-01a13c4b`, `omegag-ds-mic-01a13c4b`, `omegag-ds-voice-01a13c4b`, `omegag-dualsense-linux-01a13c4b`, `omegag-dualsense-packaging-01a13c4b`.
- The before receipt already printed this at 2026-10-14T23:34:59Z (`children: 30 (informational) — added: …`) and exited 0. `freshness-sweep.mjs:459-463` and `:878-879` declare the child set informational, never gating.
- Class: genuine count drift in standing prose versus the world. Not line drift. Not a reason to re-pin the gate green. `freshness-sweep.md:44` still says the pin is 36 entries; that table is also stale relative to the pins file (r17 literals). Calibration debt, not an alpha source defect.
- Owner: parent, if it re-pins prose and `freshness-pins.json` together. Do not fit the baseline to hide the +16.

## Proposed delta

No implementation change. No persisted-pin edit. No repeat of the round-18 absent-path annotations.

If parent lands an erratum, append-only, on `keeper-timer-inert.md:90-91` and `:108-109` only:

- Installed `charter-scribe.timer` / `.service` absent at 2026-10-14T23:40:29Z (`FragmentPath` empty, not in `list-timers`).
- Source unit still pins the deleted root at `ufo-fsd-alpha/scripts/charter-scribe/systemd/charter-scribe.service:10-11` and `config.json:3,6` (HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`).
- Relocated script exists at `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/charter-scribe/sync.mjs` (844 lines, sha256 `66087705e69e09dc41ac23f473e9e549433432526a4e67f7f8b2e55313cf79fa`). Ledger path remains `sync.mjs:595` under `cfg.repo`, which does not resolve.

Do not describe the deleted `origin-work` unit path as the current runtime root.

## Unresolved debt

- LA-4 runtime: scribe timer not installed. Unblock: operator reinstalls the unit against the live checkout, or kake marks the timer era ended. Not a kake gate bug.
- LA-3 / LA-2 upstream stale `--src` inside read-only `ufo-fsd-alpha`. Unblock: that repo retargets `service:10-11` and `config.json:3,6`. This wave must not edit it.
- LA-5 and LA-6: charter checkout absent, fetch forbidden. Unblock: a local `charter-ufo-fsd` checkout, then remeasure. Do not recall `61d0ce6` / `9c28d29` as current.
- Carried from round 18, not re-diagnosed here: PQ-2, PQ-14, §history `probeHistoryAbsent`.
- SCORECARD "14 children" vs measured 30. Informational. Unblock: parent re-pin plus prose, or leave the drift printed. Do not silence it.

## Cross-domain owner

`ufo-fsd-alpha` owns the stale WorkingDirectory, ExecStart, `repo`, and `charterRepo` pins. Kake owns only the unannotated present-tense sentences that still quote them as live. GateRepair owns no file from this census.
