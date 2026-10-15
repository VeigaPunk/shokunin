# WaveSettlement — `.ufo/waves/*` settlement census

**Seat:** WaveSettlement (leaf, read-only). **Not a verdict.** No wave is called failed. No remediation, no dispatch, no scope-path creation.

**Census clock T0:** `2026-10-15T00:31:56Z` (`2026-10-14T21:31:56-0300`), epoch `1792024316.286`.
**Live recheck T1:** `2026-10-15T00:34:08Z`, epoch `1792024448.714`. Only the eight dirs named in §6 were re-walked. Historical ages below are T0.

Ages are `floor(T0 - st_mtime)` seconds. Newest-file age is the newest regular file under the wave dir (`os.walk`, symlinks not followed, symlink dirs not descended). This report is **not** in the measured set: it is written after T1.

## Commands

```text
# T0 directory set, from /home/vgpnk/Projects/shokunin
find .ufo/waves -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort

# T0 surface + newest-file pass (Python os.walk + json schema key + stat)
# clock printed as MEASURED_AT_UTC 2026-10-15T00:31:56Z

# pointed registry paths (same T0 pass, confirmed after)
test -f .ufo/scopes/<registry.path>   # all eight targets absent

# T1 newest-file recheck of eight dirs
# clock printed as RECHECK_UTC 2026-10-15T00:34:08Z
```

Nested search under `.ufo/waves` for `swarm-registry.json`, `swarm-dispatch.json`, `dispatch.json`, `run.json`, `results.json` below wave-root depth: **0 hits**.

## Classification (so a later run diffs the same predicate)

Observation, not inference:

| Surface | Present when | Not this surface |
|---|---|---|
| `swarm-registry.json` | exact filename at `.ufo/waves/<wave>/swarm-registry.json` | `registry.json`, `registry-record.json`, a `registry` object embedded in `run.json`/`dispatch.json`, a `registry.path` that is not a file |
| dispatch/run payload | wave-root `dispatch.json`, `run.json`, or `swarm-dispatch.json` | `spec.json`, `plan.json` (`ufo-swarm-wave-v1`), `task-response.json` |
| results payload | wave-root JSON whose `schema` is `ufo-swarm-results-v1` (observed name: `results.json`) | `closeout.json` / `closeout.md`, `mission-result.json` (`ufo-mission-result-v1`), `task-response.json` (`details.results` length 0 on every copy) |

Schema conformance is a separate observation. A named file with no `schema` key is still the named surface; it is not upgraded to `ufo-swarm-*-v1`.

Inference (class), never a health grade:

| Class | Predicate |
|---|---|
| `settled` | all three surfaces present |
| `dispatched-but-unsettled` | dispatch/run payload present **and** results payload absent |
| `results-present-named-registry-unavailable` | results payload present **and** `swarm-registry.json` absent |
| `swarm-surfaces-unavailable` | no dispatch/run payload and no results payload |

A missing surface is `unavailable`, not unhealthy. An unsettled wave is not failed. Operator closeout files are recorded beside the class; they do not flip it.

Producer note (kumitate `SKILL.md`, not re-executed): `run` is documented to persist `swarm-registry.json` + `swarm-dispatch.json`; collect joins `ufo-swarm-results-v1`. On disk the dispatch filenames are `dispatch.json` and `run.json`. `swarm-dispatch.json`: **0**.

## Coverage

**40** wave directories. One row each. None omitted.

| Count | What |
|---|---|
| 0 | `settled` (registry file + dispatch/run + `ufo-swarm-results-v1`) |
| 15 | `dispatched-but-unsettled` |
| 1 | results present, named `swarm-registry.json` unavailable (`p1-repair`) |
| 24 | swarm surfaces unavailable (no dispatch/run, no results schema) |
| 10 | `swarm-registry.json` present (2 with `schema=ufo-swarm-registry-v1`, 8 unkeyed) |
| 16 | dispatch/run payload present (8 schema `ufo-swarm-wave-dispatch-v1`, 8 named `dispatch.json` unkeyed) |
| 1 | results payload (`p1-repair/results.json`, 32 member names) |
| 0 | `swarm-dispatch.json` |
| 8/8 | `registry.path` targets under `.ufo/scopes/` absent. `.ufo/scopes` has one entry, `shokunin-12h-20261014`, and no `swarm-registry.json` anywhere under `.ufo` except the 10 wave-root copies |

## Findings

Id form matches the sibling catalog where the predicate is the same (`WAVE_UNSETTLED`). Ids this seat adds are named below so a later run does not have to guess. Severity is not assigned: absence is unavailable; age is payload, not a stall grade. `WAVE_UNSETTLED_AGE` is **not** emitted (no stall bound measured here).

### `WAVE_UNSETTLED` — dispatched, no results payload

Subject: `wave=<dirname>`. Reading: dispatched-but-unsettled. **Not failed.** Newest-file age is T0. Registry-file and schema columns are observations, not a second class.

| wave | dispatch/run | schema | swarm-registry.json | registry schema | newest file | age_s | age |
|---|---|---|---|---|---|---|---|
| `shokunin-train-20261013` | `dispatch.json` | `ufo-swarm-wave-dispatch-v1` | present | `ufo-swarm-registry-v1` | `x-sentinel.md` | 95242 | 1d2h27m22s |
| `shokunin-train-20261013-w2` | `dispatch.json` | `ufo-swarm-wave-dispatch-v1` | present | `ufo-swarm-registry-v1` | `x-connector.md` | 89464 | 1d0h51m4s |
| `shokunin-train-20261013-w3` | `dispatch.json` | unkeyed | present | unkeyed | `x-connector.md` | 84294 | 23h24m54s |
| `shokunin-train-20261013-w4` | `dispatch.json` | unkeyed | present | unkeyed | `xconnector-report.md` | 81431 | 22h37m11s |
| `shokunin-train-20261013-w5` | `dispatch.json` | unkeyed | present | unkeyed | `swarm-registry.json` | 70385 | 19h33m5s |
| `shokunin-train-20261014-w6` | `dispatch.json` | unkeyed | present | unkeyed | `closeout.json` | 53137 | 14h45m37s |
| `shokunin-train-20261014-w7` | `dispatch.json` | unkeyed | present | unkeyed | `closeout.json` | 49777 | 13h49m37s |
| `shokunin-train-20261014-w8` | `dispatch.json` | unkeyed | present | unkeyed | `closeout.json` | 45297 | 12h34m57s |
| `shokunin-train-20261014-w9` | `dispatch.json` | unkeyed | present | unkeyed | `closeout.json` | 41012 | 11h23m32s |
| `shokunin-train-20261101-w10` | `dispatch.json` | unkeyed | present | unkeyed | `xsentinel-scratch/scratch-dirs-census.txt` | 36500 | 10h8m20s |
| `shokunin12h-20261014-p1-audit` | `run.json` | `ufo-swarm-wave-dispatch-v1` | unavailable | — | `members/KagiGateRerun.md` | 83 | 1m23s |
| `shokunin12h-20261014-p2-kumitate` | `run.json` | `ufo-swarm-wave-dispatch-v1` | unavailable | — | `members/KimiLayerRegression.md` | 20 | 20s |
| `shokunin12h-20261014-p3-kengaku` | `run.json` | `ufo-swarm-wave-dispatch-v1` | unavailable | — | `run.json` | 919 | 15m19s |
| `shokunin12h-20261014-p4-mori-r1` | `run.json` | `ufo-swarm-wave-dispatch-v1` | unavailable | — | `members/FindingIds.md` | 52 | 52s |
| `shokunin12h-20261014-p5-chousa-r1` | `run.json` | `ufo-swarm-wave-dispatch-v1` | unavailable | — | `run.json` | 216 | 3m36s |

`p1-audit`, `p2-kumitate`, and `p4-mori-r1` were still receiving member writes at T0. Their newest-file age is a liveness snapshot, not evidence the wave died, and not evidence it settled. See §6.

Surface ages (T0), so member writes are not mistaken for settlement-file ages:

| wave | dispatch/run age_s | registry file age_s | results |
|---|---|---|---|
| `shokunin-train-20261013` | 95765 | 95577 | unavailable |
| `shokunin-train-20261013-w2` | 89853 | 89853 | unavailable |
| `shokunin-train-20261013-w3` | 86248 | 86248 | unavailable |
| `shokunin-train-20261013-w4` | 82807 | 82807 | unavailable |
| `shokunin-train-20261013-w5` | 79698 | 70385 | unavailable |
| `shokunin-train-20261014-w6` | 70227 | 70227 | unavailable |
| `shokunin-train-20261014-w7` | 52984 | 52984 | unavailable |
| `shokunin-train-20261014-w8` | 49484 | 49484 | unavailable |
| `shokunin-train-20261014-w9` | 45226 | 45226 | unavailable |
| `shokunin-train-20261101-w10` | 39459 | 39459 | unavailable |
| `shokunin12h-20261014-p1-audit` | 969 | unavailable | unavailable |
| `shokunin12h-20261014-p2-kumitate` | 931 | unavailable | unavailable |
| `shokunin12h-20261014-p3-kengaku` | 919 | unavailable | unavailable |
| `shokunin12h-20261014-p4-mori-r1` | 242 | unavailable | unavailable |
| `shokunin12h-20261014-p5-chousa-r1` | 216 | unavailable | unavailable |

### `WAVE_SETTLED`

No subject. The triple did not occur in any of the 40 dirs.

### `WAVE_RESULTS_PRESENT` + `WAVE_REGISTRY_FILE_UNAVAILABLE`

Subject: `wave=shokunin12h-20261014-p1-repair`.

- `run.json` schema `ufo-swarm-wave-dispatch-v1`, age_s 3325.
- `results.json` schema `ufo-swarm-results-v1`, 32 member names, age_s 1289. Status/state shape: `completed` / `started` on all 32 rows. That pair is payload shape, not a class.
- `swarm-registry.json`: **unavailable**.
- `registry-record.json` schema `ufo-swarm-registry-v1` (different filename), 32 member names, age_s 3239. Name set equals `results.json` members and equals `run.json` `registry.members`. This is a local name-set observation, not a claim that the missing scope file would have matched.
- `mission-result.json` schema `ufo-mission-result-v1` (collect envelope, not the results payload). Count fields: `completed=32`, `failed=0`, `aborted=0`, `total=32`. The key `failed` is a count, not a wave classification.
- `plan.json` schema `ufo-swarm-wave-v1` (plan, not dispatch/run).
- `task-response.json`: `details.results` length 0.
- Newest file T0: `after-gates.json`, age_s 1063 (17m43s).
- Pointed path `.ufo/scopes/Shokunin12hP1Repair20261014/swarm-registry.json`: absent.

Not `settled` (named registry file missing). Not `dispatched-but-unsettled` (results payload exists). Not failed.

### `WAVE_SWARM_SURFACES_UNAVAILABLE`

No `dispatch.json`, `run.json`, `swarm-dispatch.json`, or `ufo-swarm-results-v1`. Not dispatched-but-unsettled. Not failed. Newest-file age is still recorded so a later run can see the dir was alive as a directory.

| wave | newest file | age_s | age | adjacent, not a surface |
|---|---|---|---|---|
| `aggregator-r11` | `seats/cross-lane-quality.md` | 9832 | 2h43m52s | gate script + seats |
| `kaidoku-r1` | `16-province-draft.md` | 119934 | 1d9h18m54s | numbered notes only |
| `kaidoku-r2` | `08-version-diff.md` | 118429 | 1d8h53m49s | numbered notes only |
| `kaidoku-r3` | `10-renderer-asar.md` | 117172 | 1d8h32m52s | numbered notes only |
| `kaidoku-r4` | `14-libsignal.md` | 110234 | 1d6h37m14s | numbered notes only |
| `kaidoku-r4u` | `06-adb-surface.md` | 113236 | 1d7h27m16s | numbered notes only |
| `kaidoku-r5` | `05-riscv-deep.md` | 105129 | 1d5h12m9s | numbered notes only |
| `round-9` | `seats/critic.md` | 103627 | 1d4h47m7s | gate + seats |
| `round-10` | `seats/gate-movement.md` | 103627 | 1d4h47m7s | gate + seats |
| `round-11` | `ledger-status.md` | 103627 | 1d4h47m7s | notes |
| `round-12` | `mutation-gate.md` | 103627 | 1d4h47m7s | notes + fixtures |
| `round-13` | `sentinel-trust.md` | 103627 | 1d4h47m7s | notes + fixtures |
| `round-14` | `scratch/lifecycle-correction.md` | 103627 | 1d4h47m7s | plan + scratch |
| `round-15` | `mutation-gate.md` | 103627 | 1d4h47m7s | notes + fixtures |
| `shokunin-train-20261101-w11` | `closeout.json` | 35853 | 9h57m33s | `closeout.json` keys include `closed_utc` |
| `shokunin-train-20261101-w12` | `xconnector.md` | 33260 | 9h14m20s | `registry.json` (not `swarm-registry.json`); `closeout.md` |
| `shokunin-train-20261101-w13` | `closeout.md` | 30610 | 8h30m10s | `registry.json`; `closeout.md` |
| `shokunin-train-20261101-w14` | `closeout.md` | 25631 | 7h7m11s | `registry.json`; `closeout.md` |
| `shokunin-train-20261101-w15` | `registry.json` | 17780 | 4h56m20s | `registry.json` only |
| `shokunin-train-20261101-w16` | `registry.json` | 17780 | 4h56m20s | `registry.json` only |
| `shokunin-train-20261101-w17` | `closeout.md` | 10905 | 3h1m45s | `closeout.md`; no registry file |
| `shokunin-train-20261101-w18` | `closeout.md` | 10905 | 3h1m45s | `closeout.md`; `tasks/` only otherwise |
| `shokunin-train-20261101-w19` | `tasks/audio-r78-verifier.md` | 5534 | 1h32m14s | `spec.json` + `tasks/` + `SHARED.md` |
| `shokunin-train-20261101-w20` | `tasks/g2d-r79-scribe.md` | 2598 | 43m18s | `tasks/` only |

`round-9` through `round-15` share newest mtime `2026-10-13T19:44:48Z` (age_s 103627). That is the observed timestamp, not a claim they were written by one command.

### Supporting ids (info-level observations; do not replace the class)

| id | subjects | observation |
|---|---|---|
| `WAVE_REGISTRY_PATH_ABSENT` | the two schema train waves + six `shokunin12h-20261014-p*` | `registry.path` (or `registry-record.json` `path`) names `.ufo/scopes/.../swarm-registry.json` and that file is not on disk |
| `WAVE_DISPATCH_SCHEMA_UNKEYED` | `w3` `w4` `w5` `w6` `w7` `w8` `w9` `w10` | `dispatch.json` exists; top-level `schema` key absent. Keys are dispatch-shaped (`dispatched` / `dispatched_at` / `dispatched_utc`, plus `count` or `seats` or `agents`) |
| `WAVE_REGISTRY_SCHEMA_UNKEYED` | same eight | `swarm-registry.json` exists; `schema` key absent |
| `WAVE_CLOSEOUT_NOT_RESULTS` | `w6`–`w10` `closeout.json`; `w11` `closeout.json`; `w12` `w13` `w14` `w17` `w18` `closeout.md` | closeout file exists. `w6`–`w9` have a `settled` key (value `2026-10-14`). `w10` and `w11` have `closed_utc`. None is `ufo-swarm-results-v1`. Not counted as the results payload. Not counted as failure |
| `WAVE_REGISTRY_CLOSE_MARKERS` | `shokunin-train-20261013-w5` | registry keys include `closed`, `closed_at`, `verdicts`, `verifier_verdicts`. Values not copied. File remains the registry surface, not a results payload. Its mtime is the wave's newest file |

Pointed paths confirmed absent:

- `.ufo/scopes/shokunin-train-20261013/swarm-registry.json`
- `.ufo/scopes/shokunin-train-20261013-w2/swarm-registry.json`
- `.ufo/scopes/Shokunin12hP1Audit20261014/swarm-registry.json`
- `.ufo/scopes/Shokunin12hP1Repair20261014/swarm-registry.json`
- `.ufo/scopes/Shokunin12hP2Kumitate20261014/swarm-registry.json`
- `.ufo/scopes/Shokunin12hP3Kengaku20261014/swarm-registry.json`
- `.ufo/scopes/Shokunin12hP4MoriR1/swarm-registry.json`
- `.ufo/scopes/Shokunin12hP5ChousaR1/swarm-registry.json`

`task-response.json` on `p1-audit`, `p1-repair`, `p2-kumitate`, `p4-mori-r1`: no `schema` key; `details.results` length 0. Spawn ack, not a results payload.

## Live recheck (T1)

Same walk, eight dirs only. Surface files were not re-parsed; newest-file path was.

| wave | T0 newest | T0 age_s | T0 files | T1 newest | T1 age_s | T1 files |
|---|---|---|---|---|---|---|
| `p1-audit` | `members/KagiGateRerun.md` | 83 | 34 | same path, mtime unchanged | 215 | 34 |
| `p1-repair` | `after-gates.json` | 1063 | 77 | same path, mtime unchanged | 1196 | 77 |
| `p2-kumitate` | `members/KimiLayerRegression.md` | 20 | 28 | `members/NoteVerifySightingWall.md` | 104 | 29 |
| `p3-kengaku` | `run.json` | 919 | 2 | same path | 1052 | 2 |
| `p4-mori-r1` | `members/FindingIds.md` | 52 | 5 | `members/ReportShape.md` | 19 | 8 |
| `p5-chousa-r1` | `run.json` | 216 | 2 | same path | 348 | 2 |
| `w19` | `tasks/audio-r78-verifier.md` | 5534 | 17 | same path | 5667 | 17 |
| `w20` | `tasks/g2d-r79-scribe.md` | 2598 | 6 | same path | 2731 | 6 |

`p2-kumitate` and `p4-mori-r1` moved between T0 and T1. That is in-flight member writes. It does not settle either wave and it is not a failure. This file's write is a further newest-file change on `p4-mori-r1` after T1.

## Unknowns

- Whether the eight missing scope registries were never written or were removed. Absence has no mtime. Not graded.
- Whether unkeyed `dispatch.json` / `swarm-registry.json` (w3–w10) were emitted by a different writer than `ufo-swarm-wave.mjs`. Filename and keys observed; producer not traced.
- Whether `closeout.json` / `closeout.md` was intended as a substitute results payload. Not treated as one. Not treated as failure.
- Whether w11–w20 were dispatched by a mechanism that left no `dispatch.json`/`run.json` in the wave dir. Dispatch surface unavailable. Not inferred from closeout prose.
- `results.json` rows say `status=completed` and `state=started` together. Meaning of `state` not resolved. Does not remove the results surface.
- Member-join against a missing scope registry: not evaluated. Local name-set equality on `p1-repair` is not a join to the absent path.
- Stall bound not applied. Age is the measurement the seat was asked for.

## Non-claims

No process was restarted, killed, or reparented. No file under `.ufo/waves` was modified except this report. No credential, oauth, token, or session file was opened. Agent ids inside registries were not copied. This report does not admit, fail, or settle any wave.
