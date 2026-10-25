# WaveResultJoin — settlement join

Advisory census note. Not a judge verdict. Detection only; nothing was restarted, deleted, or dispatched.

## Finding

- **id:** `mori.wave-settlement.p1-repair.join-exact`
- **wave:** `shokunin12h-20261014-p1-repair` (`Shokunin12hP1Repair20261014`)
- **class:** observation
- **join:** exact
- **unmapped members:** none (0)
- **unexpected rows:** none (0)

Registry member names and results-row names are the same 32-element set, same order, unique on both sides. Every results `agentId` equals the registry-record `agentId` and the member name.

## Surfaces measured

| Surface | Role in the join | Present |
|---|---|---|
| `.ufo/waves/shokunin12h-20261014-p1-repair/registry-record.json` | registry (`ufo-swarm-registry-v1`) | yes |
| `.ufo/waves/shokunin12h-20261014-p1-repair/results.json` | results (`ufo-swarm-results-v1`) | yes |
| `.ufo/waves/shokunin12h-20261014-p1-repair/run.json` `registry.members` | dispatch-time registry snapshot | yes |
| `.ufo/scopes/Shokunin12hP1Repair20261014/swarm-registry.json` | path named inside the registry record | **unavailable** |

Skill decision table names `.ufo/waves/*/swarm-registry.json` plus a dispatch/results pair. This wave has no `swarm-registry.json` in the wave directory. The on-disk registry is `registry-record.json`. Its `path` field and `run.json`'s `registry.path` both name `.ufo/scopes/Shokunin12hP1Repair20261014/swarm-registry.json`. Probed with `test -e` at 2026-10-14T21:34:48-03:00: file absent, parent directory absent. That is a missing surface (`unavailable`), not an unhealthy fleet and not an unsettled wave. The join below uses the wave-local registry record, which is the registry that exists.

This wave is the only directory under `.ufo/waves/` that has both a registry document and a `results.json`. Train waves `shokunin-train-20261013` through `shokunin-train-20261101-w10` have `swarm-registry.json` plus `dispatch.json` and no results file (dispatched, unsettled — not scored here). `shokunin12h-20261014-p4-mori-r1` itself has `run.json` registry members and no `results.json` yet, so it cannot be the settled wave under test.

## Commands and timestamps

Measured 2026-10-14T21:34:48-03:00 (`date -Is`; UTC 2026-10-15T00:34:37Z). Reads were `python3` 3.14.7 (`/usr/bin/python3`) over the files below, plus `stat -c`, `sha256sum`, `test -e`, and `ls -1 | wc -l`.

| File | mtime (local, `stat -c %y`) | bytes | sha256 |
|---|---|---|---|
| `registry-record.json` | 2026-10-14 20:37:56.915415531 -0300 | 11336 | `92928c5f3d93cdcfcbb1339fabeed0ba4921880730fc786746a14360d0a9f7d1` |
| `results.json` | 2026-10-14 21:10:26.329265701 -0300 | 10098 | `d33638c25e53b0da60096f00b43aba813b2528e85ab58110efae6acce2f3c8ad` |
| `run.json` | 2026-10-14 20:36:30.653406765 -0300 | 61781 | not hashed (snapshot only) |
| `mission-result.json` | 2026-10-14 21:12:53.903157766 -0300 | 17269 | not hashed (not a join input) |

Registry record timestamps inside the file: `createdAt` `2026-10-14T23:36:30.649Z`, `updatedAt` `2026-10-14T23:37:56.911Z`. The `updatedAt` instant matches the local mtime (20:37:56 -0300). `run.json` mtime is earlier (20:36:30 -0300) and matches `createdAt`.

`members/*.md`: 32 files, `ls -1 | wc -l` = 32. Earliest mtime 2026-10-14T20:38:47 (`KamaGateRepair.md`, 6108 bytes). Latest mtime 2026-10-14T21:02:33 (`KakeGateRepair.md`, 2853 bytes). All 32 mtimes are before `results.json`. Size range 2853–33093 bytes. No empty file. No non-`.md` entry. No subdirectory.

## Join rule

- Registry side: keys of `registry-record.json` `members` (object, schema `ufo-swarm-registry-v1`, `wave` `Shokunin12hP1Repair20261014`).
- Results side: `name` of each element of `results.json` `members` (array, schema `ufo-swarm-results-v1`).
- Unmapped member = registry key with no results row of that `name`.
- Unexpected row = results `name` with no registry key.
- Duplicate `name` or duplicate `agentId` on the results array would also be an unexpected row. None observed.

Counts: registry 32, results 32, unique on both sides. Set difference both directions: empty. Order of registry keys equals results-array order.

## Identity checks (observation, not extra defects)

Compared field by field. These are not unmapped members or unexpected rows.

| Check | Result |
|---|---|
| `results.agentId` vs registry-record `agentId` | equal for all 32; each `agentId` equals the member name |
| `results.agentId` duplicates | 0 |
| registry-record vs `run.json` `registry.members` | same keys, same `kind`/`role`/`item`/`axes`/`milestone`; sole difference is `agentId` (`null` in the 20:36:30 dispatch snapshot, member name in the 20:37:56 record) |
| `spec.json` `items[].name` and `run.json` `taskCall.tasks[].name` | same 32 names, same order, same `role` and `item` as the registry record |
| `mission-result.json` `subagents[].agentId` | same 32 ids, same order; `item`, `axes`, `milestone` match the registry record; `memberIndex` is 1..32 unique |
| `results.status` vs mission `outcome` | equal: `completed` × 32 |
| `results.state` vs mission `state` | equal: `started` × 32 |
| results `result` string | matches `Advisory report: .ufo/waves/shokunin12h-20261014-p1-repair/members/<name>.md; returned after scoped work. Parent verification/admission separate.` for the same `<name>` × 32 |
| named member file | present for every results row |

`state: started` together with `status: completed` is recorded as the row's own fields. It is the same pair on every row and on the mission file. It is not read as a missing member or as a failed wave. No status other than `completed` appears, so this join cannot show what an unmatched or failed row looks like.

## Members (registry order = results order)

| # | name | registry role | item | results status | results state | agentId |
|---|---|---|---|---|---|---|
| 1 | KagiGateRepair | executor | kagi/GateRepair | completed | started | KagiGateRepair |
| 2 | KagiHistoryClaims | revenger | kagi/HistoryClaims | completed | started | KagiHistoryClaims |
| 3 | KagiLiveAnchors | scout | kagi/LiveAnchors | completed | started | KagiLiveAnchors |
| 4 | KagiRecordPrep | scribe | kagi/RecordPrep | completed | started | KagiRecordPrep |
| 5 | KagiScopeAudit | reviewer | kagi/ScopeAudit | completed | started | KagiScopeAudit |
| 6 | KakeGateRepair | executor | kake/GateRepair | completed | started | KakeGateRepair |
| 7 | KakeHistoryClaims | revenger | kake/HistoryClaims | completed | started | KakeHistoryClaims |
| 8 | KakeLiveAnchors | scout | kake/LiveAnchors | completed | started | KakeLiveAnchors |
| 9 | KakeRecordPrep | scribe | kake/RecordPrep | completed | started | KakeRecordPrep |
| 10 | KakeScopeAudit | reviewer | kake/ScopeAudit | completed | started | KakeScopeAudit |
| 11 | KamaGateRepair | executor | kama/GateRepair | completed | started | KamaGateRepair |
| 12 | KamaHistoryClaims | revenger | kama/HistoryClaims | completed | started | KamaHistoryClaims |
| 13 | KamaLiveAnchors | scout | kama/LiveAnchors | completed | started | KamaLiveAnchors |
| 14 | KamaRecordPrep | scribe | kama/RecordPrep | completed | started | KamaRecordPrep |
| 15 | KamaScopeAudit | reviewer | kama/ScopeAudit | completed | started | KamaScopeAudit |
| 16 | KasegiGateRepair | executor | kasegi/GateRepair | completed | started | KasegiGateRepair |
| 17 | KasegiHistoryClaims | revenger | kasegi/HistoryClaims | completed | started | KasegiHistoryClaims |
| 18 | KasegiLiveAnchors | scout | kasegi/LiveAnchors | completed | started | KasegiLiveAnchors |
| 19 | KasegiRecordPrep | scribe | kasegi/RecordPrep | completed | started | KasegiRecordPrep |
| 20 | KasegiScopeAudit | reviewer | kasegi/ScopeAudit | completed | started | KasegiScopeAudit |
| 21 | KengakuGateRepair | executor | kengaku/GateRepair | completed | started | KengakuGateRepair |
| 22 | KengakuHistoryClaims | revenger | kengaku/HistoryClaims | completed | started | KengakuHistoryClaims |
| 23 | KengakuLiveAnchors | scout | kengaku/LiveAnchors | completed | started | KengakuLiveAnchors |
| 24 | KengakuRecordPrep | scribe | kengaku/RecordPrep | completed | started | KengakuRecordPrep |
| 25 | KengakuScopeAudit | reviewer | kengaku/ScopeAudit | completed | started | KengakuScopeAudit |
| 26 | KotobaGateRepair | executor | kotoba/GateRepair | completed | started | KotobaGateRepair |
| 27 | KotobaHistoryClaims | revenger | kotoba/HistoryClaims | completed | started | KotobaHistoryClaims |
| 28 | KotobaLiveAnchors | scout | kotoba/LiveAnchors | completed | started | KotobaLiveAnchors |
| 29 | KotobaRecordPrep | scribe | kotoba/RecordPrep | completed | started | KotobaRecordPrep |
| 30 | KotobaScopeAudit | reviewer | kotoba/ScopeAudit | completed | started | KotobaScopeAudit |
| 31 | FleetBoundaryConnector | connector | fleet/BoundaryConnector | completed | started | FleetBoundaryConnector |
| 32 | KagiSecrecySentinel | sentinel | kagi/SecrecySentinel | completed | started | KagiSecrecySentinel |

All 32 `kind` values are `spawn`. `run.json` `counts` is spawn 32, resume 0, total 32.

## Not claimed

- Member-report contents were not graded. File presence and size only.
- `process-defects.json` describes a nested spawn under `KengakuGateRepair`. That file is not a results row and is not part of this name join. No results `name` is unexpected because of it.
- No remediation. Missing scope registry stays `unavailable`.
- This note does not say the wave failed or succeeded as a program. It says the registry/results name join is exact.

## Later-run compare

Recompute set(registry `members` keys) against set(results `name`), and compare `agentId`. Stable id: `mori.wave-settlement.p1-repair.join-exact`. A later drift is a non-empty unmapped set, a non-empty unexpected set, a duplicate `name`/`agentId`, or an `agentId` that no longer equals the member name.
