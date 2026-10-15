# WaveAgeMath — falsification of the wave-age rule

Advisory data for the parent integrator. Not a judge verdict. Not a fleet grade. No wave is called failed. This lane does not remediate, dispatch, kill, or rewrite a registry.

**Finding ids (stable, for a later run to compare):** `WAVE_AGE_RESULTS_ABSENT_AFTER_CLOSE`, `WAVE_AGE_REGISTRY_STATUS_STALE`, `WAVE_AGE_PATH_DANGLING`, `WAVE_AGE_TASK_RESPONSE_FROZEN_PENDING`, `WAVE_AGE_DIR_MTIME_NOT_PROGRESS`, `WAVE_AGE_DECLARED_CLOCK_FUTURE`, `WAVE_AGE_CHECKOUT_STAMP`, `WAVE_UNSETTLED_PROGRESSING`, `WAVE_UNSETTLED_SURFACE_SILENT`.

**Axes hit if the rule is implemented as written:** coverage (the named file pair is not the set of waves), operability (the documented registry path is absent on the live dispatches), calibration (age and `pending` both mis-grade observed waves).

## Rule under attack

Quoted from `mori-shokunin/SKILL.md` (lane file, not a host measurement):

- Decision row: settle by `.ufo/waves/*/swarm-registry.json` plus a dispatch/results pair; never assume an unsettled wave is a failed one; output per-wave settled/unsettled **with age**.
- Error row: registry present, no results → dispatched but never settled — **age it, do not call it failed**.

No numeric age threshold is defined in that file. The protocol stale-lane rule (open > two driver ticks, 900 s, progressing = files newer than launch) is a different surface (watchdog missions). It is not imported here. `WAVE_UNSETTLED_AGE` appears only as an example id in this wave's spec, not as a landed gate.

**Candidate rule R-age, stated so it can be wrong:** a wave is unsettled iff `swarm-registry.json` exists and a results file does not; the grade is the age of that absence (or of the newest file in the wave dir). Older absence means more stalled. A results file means settled.

## Clock and commands

Host clock is `date -u`. First stamp `2026-10-15T00:29:34Z`. All ages below are against the stamp named in that row, not against a single frozen now.

| Stamp (UTC) | Command (read-only) | What it measured |
|---|---|---|
| 2026-10-15T00:29:34Z | `date -u`; `find /home/vgpnk/Projects/shokunin/.ufo/waves -mindepth 1 -maxdepth 1 -type d` | 40 wave dirs |
| 2026-10-15T00:29:57Z | `tmux ls` | one session: `ufo_sighting` (created Wed Oct 14 20:14:40 2026). Not per-wave. Wave attribution from tmux: **unavailable** |
| 2026-10-15T00:30:18Z | python `os.walk` of each wave dir; marker filenames; newest mtime | marker census below |
| 2026-10-15T00:31:00Z | `find /home/vgpnk/Projects -maxdepth 3 -type d -name waves -path '*/.ufo/waves'` | only `/home/vgpnk/Projects/shokunin/.ufo/waves`. Other roots not searched below depth 3: **unknown**, not claimed absent on the whole host |
| 2026-10-15T00:31:44Z | `ps -eo pid,lstart,etime,cmd` filtered for ufo/omp/swarm | `omp` pid 935236 since Wed Oct 14 20:10:28 2026; many `omp` workers and one `ufo-sighting.mjs`. Cmdlines did not name a wave |
| 2026-10-15T00:32:57Z | second `os.walk` of live and candidate dirs | mtime delta |
| 2026-10-15T00:35:09Z | `task-response.json` `details.progress[].status`; member-name set vs `run.json` `taskCall.tasks` | pending-stamp vs files on disk |
| 2026-10-15T00:35:29Z | JSON keys `closed`/`settled`/`status` on every registry and closeout; `/proc/<pid>/cmdline` substring scan | contradictions; attribution |
| 2026-10-15T00:36:25Z | third sample of the five live 12h dirs; `ls` of named lane `reports/round-*` dirs | progressing vs surface-silent |

`/proc` cmdline scan at 00:35:29Z: 0 hits for `p3-kengaku`, `p5-chousa`, `p1-audit`, `p2-kumitate`, `p4-mori`, `KakeDeadPathSweep`, `w19`, `w20`. **Observation:** those substrings are not in cmdline. **Unknown:** whether an `omp` worker is that wave. Zero cmdline hits is not "no agent".

## Universe (observation)

40 directories. Two genera, not one age clock.

**Genus A — archived seat/round dirs.** No `swarm-registry.json`, no `dispatch.json`, no `run.json`, no `results.json`, no `closeout.*`. `round-9` through `round-15` share newest-file mtime `2026-10-13T19:44:48Z` exactly (census 00:30:18Z, age 103530 s). `git ls-files .ufo/waves` tracks them. That shared mtime is a materialization stamp, not activity. kaidoku-r1..r5 and aggregator-r11 are the same genus (seat notes / a gate script), with their own mtimes. R-age must not age "no results file" over this genus. A missing settlement pair here is **unavailable**, not unsettled.

**Genus B — dispatch dirs.** A registry, a `dispatch.json`/`run.json`, a `spec.json`, or a `closeout.*` is present. This is the set R-age claims to grade. It does not grade it.

`git ls-files` also tracks genus B, including the live 12h dirs. Tracking is not settlement.

## Counterexamples that make R-age wrong

These are host facts. Each one is a case where age-of-(registry ∧ no results file), or age of the newest wave-dir file, grades the wrong state.

### 1. Settled wave, no results file — `WAVE_AGE_RESULTS_ABSENT_AFTER_CLOSE`

No wave dir in the 40 contains `swarm-results.json`. The only `results.json` is `shokunin12h-20261014-p1-repair/results.json` (`schema` `ufo-swarm-results-v1`, 32 members, every `status` `completed`, measured 00:31:44Z). Sibling `mission-result.json` is `ufo-mission-result-v1`, `completed` 32, `failed` 0, `aborted` 0, `total` 32.

Every other settlement token on disk is a different filename:

| Wave dir | Settlement token observed | `results.json` | What R-age does |
|---|---|---|---|
| `shokunin-train-20261013-w5` | `swarm-registry.json` `closed: true`, `closed_at: 2026-10-14T04:58:50Z`, `verdicts` audio-r66/g2d-r65/g3d-r74 all `ADMIT`. File mtime equals `closed_at` | absent | ages a closed wave forever |
| `shokunin-train-20261014-w6` | `closeout.json` `settled: 2026-10-14` | absent | same |
| `w7` | `closeout.json` `settled: 2026-10-14` | absent | same |
| `w8` | `closeout.json` `settled: 2026-10-14` (mtime 2026-10-14T11:56:58Z) | absent | same |
| `w9` | `closeout.json` `settled: 2026-10-14` | absent | same |
| `shokunin-train-20261101-w10` | `closeout.json` `closed_utc: 2026-10-14T14:20Z` | absent | same |
| `w11` | `closeout.json` `closed_utc: 2026-10-14T14:45Z`. **No** `swarm-registry.json` | absent | invisible to R-age (no registry) and also not settled by a results file |
| `w12` | `closeout.md` first lines: "Closed 2026-10-14 ~15:15Z". Registry file is `registry.json`, not `swarm-registry.json` | absent | invisible |
| `w13`, `w14`, `w17` | `closeout.md` present | absent | invisible if the rule requires `swarm-registry.json` |
| `w15` | no closeout file. `registry.json` embeds per-lane `verdict` / `closed` (`ADMIT-corr`, work commits). Newest file is that registry, mtime `2026-10-14T19:35:36Z` | absent | either ages it as unsettled, or misses it because the filename is not `swarm-registry.json` |
| `shokunin12h-20261014-p1-repair` | `results.json` + `mission-result.json` + `registry-record.json` (`ufo-swarm-registry-v1`). **No file named** `swarm-registry.json` | present | a name-locked rule misses the one wave that actually has the results schema |

`w11` is the sharp form of the prompt's example: a wave whose closeout says closed, with neither `swarm-registry.json` nor a results file.

`w5` is the sharp form inside the filename the rule does look at: the registry file itself carries `closed` and `verdicts`, and there is still no results file. The newest file in that dir **is** the registry (mtime `2026-10-14T04:58:50Z`, age 70446 s at 00:32:57Z). Newest-file age after close is bookkeeping age, not stall age.

### 2. Registry status field contradicts the closeout — `WAVE_AGE_REGISTRY_STATUS_STALE`

Measured 00:35:29Z by reading the JSON keys, not by mtime:

- `w6/swarm-registry.json` has `closed: false`. `w6/closeout.json` has `settled: 2026-10-14`. Same directory. Trusting `closed` ages a wave the closeout calls settled. Trusting the closeout means a results file is not required.
- `w8/swarm-registry.json` is 160 bytes, `status: "live"`, `dispatched: 26` (a count, not a timestamp). Closeout mtime `2026-10-14T11:56:58Z` is later than the registry mtime `2026-10-14T10:47:11Z`. The status field was not updated.
- `w9/swarm-registry.json` is the same `status: "live"` shape. Its closeout also says `settled: 2026-10-14` and, in the g3d lane note, "simplifier in flight at closeout". A closeout token is a claim. It is not proof every seat was terminal. R-age cannot see that distinction at all, because it never opens the closeout.

### 3. Live dispatch registry path does not exist — `WAVE_AGE_PATH_DANGLING`

All six `shokunin12h-20261014-p*` `run.json` files are `schema: ufo-swarm-wave-dispatch-v1`, `counts.total` 32, embedded `registry.schema` `ufo-swarm-registry-v1`, `registry.path` `.ufo/scopes/<WaveName>/swarm-registry.json`. Stat at 00:34:15Z: **every one of those six paths is absent, and the parent scope directory is absent.** `find` under `.ufo/scopes` for a filename containing `registry` returned no file.

So the SKILL path `.ufo/waves/*/swarm-registry.json` is not where these dispatches say the registry is, and the path they do name is a dangling pointer. p1-repair settled anyway, via `registry-record.json` in the wave dir (updatedAt `2026-10-14T23:37:56.911Z`), not via the declared path.

A gate that ages "registry path missing" marks the settled repair wave and the three progressing waves with the same finding.

Train wave 1's `dispatch.json` embeds `registry.path` `.ufo/scopes/shokunin-train-20261013/swarm-registry.json`. Stat at 00:32:57Z: that path is absent. A copy with `schema: ufo-swarm-registry-v1` sits in the wave dir instead. Two authorities, one missing.

### 4. `task-response.json` stays `pending` after settlement and during writes — `WAVE_AGE_TASK_RESPONSE_FROZEN_PENDING`

At 00:35:09Z, `details.results` length 0 and `details.progress` status counts:

| Wave | progress n | status | file mtime |
|---|---|---|---|
| p1-repair (results already 32 completed) | 32 | `pending` 32 | 2026-10-14T23:36:41Z |
| p1-audit (31 member files on disk) | 32 | `pending` 32 | 2026-10-15T00:15:50Z |
| p2-kumitate (members still landing) | 32 | `pending` 32 | 2026-10-15T00:23:55Z |
| p4-mori-r1 (members landing) | 32 | `pending` 32 | 2026-10-15T00:28:03Z |

The repair wave's task-response mtime is before `results.json` (`2026-10-15T00:10:26Z`) and before `after-gates.json` (`2026-10-15T00:14:12Z`). Reading `pending`, or aging the task-response file, calls a settled wave unsettled and a writing wave stalled.

p3 and p5 have no `task-response.json`. Absence is **unavailable** for this snapshot, not `pending` and not `failed`.

### 5. Wave-dir silence is not stall — `WAVE_AGE_DIR_MTIME_NOT_PROGRESS`

Task files under `shokunin-train-20261101-w19/tasks/` and `w20/tasks/` are prompts ("Report -> reports/round-…"), not results. `w19/SHARED.md` (mtime `2026-10-14T21:29:23Z`) still says seats are `running`. That prose is older than later files. It is not a live probe.

External report dirs, stat 00:36:25Z (path = `<lane>/reports/<round>/`):

| Prompt dir newest | External reports after that freeze |
|---|---|
| w19 tasks newest `audio-r78-verifier.md` `2026-10-14T22:59:41Z` | `audio-shokunin/reports/round-78` n=10, newest `r78-simplifier.md` `2026-10-14T23:48:58Z`. `game-dev-3d-shokunin/reports/round-87` n=9, newest `r87-adjudicator.md` `2026-10-14T23:47:22Z` |
| w20 tasks all one second `2026-10-14T23:48:37Z` (6 prompt files, no `spec.json`, no registry) | `game-dev-2d-shokunin/reports/round-79` n=3, newest `r79-baseline.md` `2026-10-14T23:56:43Z`. `game-dev-3d-shokunin/reports/round-88` n=3, newest `r88-baseline.md` `2026-10-15T00:01:24Z` |

An age rule on the wave dir would have called w19 stalled in the 49 minutes between `22:59:41Z` and `23:48:58Z`, while the named report dir was still receiving files. w20's wave dir never moved after the prompt burst; a report named by the scribe prompt (`r79-scribe.md`, mtime `2026-10-14T23:56:14Z` at the 00:35:09Z stat) landed outside the dir.

Same shape for the early train waves, which have `swarm-registry.json` and no results file and no closeout (so R-age marks them unsettled and ages them ~19–27 h):

| Wave dir registry | Lane report dirs (00:36:25Z) |
|---|---|
| `shokunin-train-20261013` registry `updatedAt` `2026-10-13T21:58:44.911Z`, no `closed` key. Newest wave-dir file `x-sentinel.md` `2026-10-13T22:04:33Z` (early-wave baseline, its own text says lanes were already working) | audio `round-62`, g2d `round-61`, g3d `round-70`: 10 files each, including `*-adjudicator.md`. Newest adjudicators `2026-10-13T23:24:01Z` / `23:25:49Z` / `23:27:12Z`, after the wave-dir freeze |
| w2 registry `updatedAt` `2026-10-13T23:34:22.800Z`, no `closed` | audio `round-63`, g2d `round-62`, g3d `round-71`: 10 files each, adjudicators present. Newest `2026-10-14T00:38:13Z` |
| w3 registry `status: "dispatched"` only | audio `round-64`, g2d `round-63`, g3d `round-72`: 10 files each. Newest `2026-10-14T01:31:10Z` |
| w4 registry `dispatched: 2026-10-14T01:35Z` only | audio `round-65`, g2d `round-64`, g3d `round-73`: 10 files each. Newest `2026-10-14T02:21:12Z` |

**Observation:** those report files exist and are newer than the wave-dir registry. **Inference, one file only:** `audio-shokunin/reports/round-62/r62-adjudicator.md` line 3 reads "Verdict: ADMIT the bounded R62 depth move." **Unknown:** the verdict word inside the other adjudicator files (not read). Do not promote "adjudicator file exists" to "wave settled" for w2–w4. Do record that R-age, which never looks at those paths, would age w1–w4 as unsettled for a day after the report dirs filled.

w5's own `xsentinel-report.md` says "The wave settled during the census" while verifier writes were still in flight at `04:55Z`. The registry `closed_at` is `04:58:50Z`. Settlement and in-flight writes overlapped. Age from dispatch `2026-10-14T02:30Z` would have fired during that overlap.

### 6. Declared timestamps are not clocks — `WAVE_AGE_DECLARED_CLOCK_FUTURE`

- `w10/dispatch.json` (83 bytes, keys `dispatched_utc`, `count`, `verifier_phase` only — not `ufo-swarm-wave-dispatch-v1`) has `dispatched_utc: "2026-11-01"`. File mtime `2026-10-14T13:34:16Z`. Closeout `closed_utc` `2026-10-14T14:20Z`. Age from the declared date is negative on this clock.
- `w12/registry.json` `dispatched_utc: "2026-11-01T15:06Z"`. `closeout.md` says closed `2026-10-14 ~15:15Z`. The declared dispatch is after the closeout text.
- `w8`/`w9` `dispatched: 26` is a seat count. Subtracting it from now is a type error.
- `w15` and `w16` `registry.json` share mtime `2026-10-14T19:35:36Z` exactly (age 17841 s at 00:32:57Z, unchanged on that resample). One writer touched both files. Identical mtime is not two waves progressing.

### 7. Checkout stamp — `WAVE_AGE_CHECKOUT_STAMP`

`round-9` through `round-15`: newest file in each dir is `2026-10-13T19:44:48Z`. An age rule on "every dir under `.ufo/waves`" would emit one stall age for committed archives. They are genus A. Not unsettled.

### 8. A closeout file can name unfinished work

`w18/closeout.md` title is "g3d r86 wave-A/B + g2d r78 wave-A". Body: "Wave-B folded into w19 bookkeeping". `w9` closeout names a simplifier in flight. `w19/SHARED.md` carry-in says g2d r78 verifier+simplifier were in flight and g3d r87 seats were in flight, while `w18` already had a closeout. **Inference:** closeout existence is not "every member terminal". **Unknown:** whether those in-flight seats later finished (round-87 now has an adjudicator file; that file was not read for a verdict word).

### 9. Importing the 900 s stale-lane threshold would already be wrong on a live wave

p2 `run.json` mtime `2026-10-15T00:16:24Z`. At the 00:36:25Z sample that file is ~1200 s old, past two 450 s ticks. Member file `members/PinAudit.md` was 59 s old in the same sample, and the member count rose 24 → 26 → 26 across 00:32:57Z / 00:35:09Z / 00:36:25Z while the newest name changed (`NoteVerifySightingWall.md` → `StanzaAudit.md` → `PinAudit.md`). Age since dispatch ≥ 900 s and the wave is progressing. The threshold is also the wrong surface (driver ticks reset; documented in protocol reports, not re-measured here).

## Unsettled waves — progressing versus stalled

**Classification used in this section (inference, not R-age):** no settlement token in the wave dir (`results.json` schema, `mission-result.json`, `closeout.json` `settled`/`closed_utc`, `closeout.md`, or registry `closed: true` / embedded `verdicts`). Genus A excluded. p1-repair excluded (token present). w5–w15, w17, w18 excluded as token-present, with the contradictions above. w16 kept, because its registry is mixed and it has no closeout.

Progress evidence is a **second sample of an output path**, not age. Stall is not inferred from age alone. Surface silence with no process attribution stays `WAVE_UNSETTLED_SURFACE_SILENT`, not failed, not unhealthy.

### `shokunin12h-20261014-p2-kumitate` — progressing (`WAVE_UNSETTLED_PROGRESSING`)

- Dispatch: `run.json` `2026-10-15T00:16:24Z`, 32 tasks. Declared scope registry **absent**. No results file. No closeout.
- `task-response.json` mtime `2026-10-15T00:23:55Z`, still 32 `pending` (the frozen snapshot). Not used as the progress clock.
- Member files: 24 at 00:32:57Z (newest `NoteVerifySightingWall.md` `00:32:24Z`), 26 at 00:35:09Z (newest `StanzaAudit.md` `00:34:47Z`, age 21 s), 26 at 00:36:25Z (newest `PinAudit.md` `00:35:25Z`, age 59 s). Missing names at 00:35:09Z: `SectionHonestyAudit`, `BoundaryReenumerationAudit`, `NoteVerifyRemainingScriptsCensus`, `NoteVerifyRuntimeRemainderCensus`, `NoteVerifyRouteProbeCluster`, `NoteVerifyNativeJudgePipeline`.
- **Observation:** member files appeared and the newest name changed across three samples. **Inference:** the wave is progressing. **Unknown:** whether the six missing names are running (cmdline attribution unavailable). **Not** stalled. Age of `run.json` (~20 min at the last sample) would have said otherwise.

### `shokunin12h-20261014-p4-mori-r1` — progressing (`WAVE_UNSETTLED_PROGRESSING`)

This wave. Dispatch `run.json` `2026-10-15T00:27:54Z`. `task-response.json` `2026-10-15T00:28:03Z` (9 s later), 32 `pending`, `results` n=0. Declared scope registry absent. No results file.

Member dir was empty at the 00:30:18Z walk (`files=3`, the three JSON files only). Then: 3 member files at 00:32:57Z (newest `CorpusMap.md` `00:32:28Z`), 5 at 00:35:09Z (newest `ReportShape.md` `00:33:48Z`), 7 at 00:36:25Z (newest `GateDesign.md` `00:36:14Z`, age 10 s). This file is not in that count.

**Observation:** member count rose 0 → 3 → 5 → 7 inside six minutes. **Inference:** progressing. An age threshold of a few minutes on "no results file" would have fired while the first member files were being created. **Unknown:** the other seats (cmdline unavailable).

### `shokunin12h-20261014-p1-audit` — writes paused, wave not stalled (`WAVE_UNSETTLED_PROGRESSING`)

- Dispatch `run.json` `2026-10-15T00:15:46Z`, 32 tasks. `task-response.json` `2026-10-15T00:15:50Z`, 32 `pending`. Declared scope registry absent. No results file.
- Members: 31 files from the 00:32:57Z sample through the 00:36:25Z sample. Newest stayed `members/KagiGateRerun.md` `2026-10-15T00:30:32Z` (age 144 s, then 276 s, then 352 s). Missing name at 00:35:09Z: `KakeDeadPathSweep` only.
- **Observation:** 31/32 named member files exist. No new member file across a 6-minute resample. Earlier census at 00:30:18Z had newest `KakeHistoricalMarking.md` `00:28:15Z`, so the dir was still changing before `00:30:32Z`. **Inference:** wave-dir progress for 31 seats has landed; one named file has not appeared, and the dir has been quiet since `00:30:32Z`. That is not "the wave is stalled", and it is not "the missing seat is dead". **Unknown:** whether `KakeDeadPathSweep` is still running. Cmdline attribution unavailable. Do not age the whole wave off the dispatch file (`00:15:46Z`, ~21 min at the last sample) — 31 files landed during that age.

### `shokunin12h-20261014-p3-kengaku` — surface-silent (`WAVE_UNSETTLED_SURFACE_SILENT`)

- `run.json` + `spec.json` only. `run.json` mtime `2026-10-15T00:16:36Z`, unchanged at 00:30:18Z (age 822 s), 00:32:57Z (age 981 s), and 00:36:25Z (age 1188 s). No `members/`, no `task-response.json`, no closeout, no results. Declared scope registry absent. Top listing stayed `['run.json', 'spec.json']`.
- Sibling p4, dispatched later (`00:27:54Z`), had a task-response 9 s later and member files by `00:32Z`. p3 has had neither for ~20 min.
- **Observation:** no wave-dir file newer than the dispatch across three samples. **Inference:** the harness has not recorded a task return in this directory. **Unknown:** whether 32 agents are alive outside this dir. `/proc` cmdline did not name the wave. That is **unavailable**, not unhealthy, not failed. Age of `run.json` is a description of the silence, not a proof of stall cause. A later sample that finds `members/` or a task-response would falsify "stalled" the same way w19's external reports falsified wave-dir age.

### `shokunin12h-20261014-p5-chousa-r1` — surface-silent, shorter window (`WAVE_UNSETTLED_SURFACE_SILENT`)

Same shape as p3: `run.json` + `spec.json` only, mtime `2026-10-15T00:28:20Z`. Ages 118 s / 277 s / 485 s across the three samples. No task-response, no members, declared scope registry absent. Sibling p4 wrote task-response in 9 s. 485 s is outside that sibling pattern and still a short window next to p3's 1188 s.

**Observation:** no new file across three samples. **Inference:** no harness return recorded here yet. **Unknown:** agent liveness. Not failed. Not the same confidence of prolonged silence as p3. A gate that uses one age cutoff for both would erase that difference.

### `shokunin-train-20261101-w19` — was progressing outside the dir; both surfaces now quiet

No `swarm-registry.json`, no `closeout.*`, no `results.json`. `spec.json` lists seat ids. `SHARED.md` says `running` and is stale relative to later mtimes (see counterexample 5). Wave-dir newest file unchanged between 00:30:18Z and 00:32:57Z (`tasks/audio-r78-verifier.md` `2026-10-14T22:59:41Z`).

External `round-78` (10 files) and `round-87` (9 files, including an adjudicator) have newest mtimes `23:48:58Z` and `23:47:22Z`. At 00:36:25Z those are also ~1.8 h old. No second sample of those report dirs was taken, so "still quiet" is one stat, not a delta.

**Observation:** progress happened on the report paths after the wave dir froze, and those report paths are now also old on a single stat. **Inference:** R-age on the wave dir was already false during 22:59Z–23:48Z. **Unknown:** whether the round is admitted (adjudicator text not read) and whether any seat is still running. Not a results-file settlement. Not failed.

### `shokunin-train-20261101-w20` — partial external landing, then quiet

Six prompt files, one mtime `2026-10-14T23:48:37Z`. No spec, no registry, no closeout, no results. R-age does not see this directory at all (`WAVE_AGE_RESULTS_ABSENT_AFTER_CLOSE` coverage hole, inverted: an unsettled partial dispatch with no registry).

External: round-79 n=3, newest `23:56:43Z`; round-88 n=3, newest `00:01:24Z`. Not a full seat set (compare round-62's 10). Single stat, no delta. **Observation:** some named reports landed after the prompt burst; the set is incomplete; both surfaces are older than 30 min at 00:36:25Z. **Unknown:** whether more seats will write. Not failed. Wave-dir age alone would have called it stalled at `23:48:37Z`, eight minutes before `r79-scribe.md` landed.

### `shokunin-train-20261101-w16` — mixed registry, surface quiet

No closeout, no results file. `registry.json` mtime `2026-10-14T19:35:36Z`, shared with w15, unchanged on the 00:32:57Z resample (age 17841 s). Top-level keys include `wave17_prep`. g2d-r76 object includes `verdict: ADMIT-corr`. g3d-r85 object in the same file has `work_commit` and notes and no `verdict` key in the parsed object. audio-r76 value is the string "continues under wave-15".

**Observation:** one file mixes a verdict, a continuation pointer, and a next-wave prep note. Newest-file age is the age of that mixed write, shared with w15. **Inference:** R-age ("no results file") calls the whole dir unsettled, which is wrong for the g2d verdict and uninformative for g3d. **Unknown:** whether g3d-r85 was later adjudicated in a report file (not stat'd). Not progressing on this dir since `19:35:36Z`. Not failed.

### `shokunin-train-20261013` and `w2`, `w3`, `w4` — wave-dir quiet; report dirs already full

R-age marks these unsettled (registry present, no results file) and would age them from registry mtimes on 2026-10-13/14, i.e. tens of hours at this clock. No closeout. No `closed` key (w3 `status` is still `"dispatched"`).

**Observation:** each corresponding lane `reports/round-*` dir has 10 files, including an adjudicator, with mtimes after the wave-dir registry (table in counterexample 5). Wave-dir newest files did not move on the 00:32:57Z resample of w1. **Inference:** the wave dir is not the progress surface for these waves, and it is not moving now. **Unknown:** verdict words except audio r62 ADMIT (read). Calling them stalled because the wave dir is old is the rule's error. Calling them settled because an adjudicator file exists is an inference this report does not make, except for the one file whose verdict line was read.

## What would make an age rule wrong — checklist

A later gate is wrong if any of these grade as `WAVE_UNSETTLED_AGE`:

1. A wave with `closeout.json` `settled` or `closed_utc`, or `closeout.md`, and no results file (w6–w14, w17, w18, and w11 which also lacks `swarm-registry.json`).
2. A registry with `closed: true` and `verdicts`, and no results file (w5). The newest file being that registry does not reopen it.
3. A registry `status: "live"` or `closed: false` beside a newer closeout that says settled (w6, w8, w9).
4. A `run.json` whose `registry.path` is absent (all six 12h waves), including the one that already has `results.json` (p1-repair).
5. `task-response.json` still all `pending` (repair wave after 32 completed; p2/p4 while members are landing).
6. Newest wave-dir mtime old while the report path named in the task file is newer (w19, w20, w1–w4).
7. Declared `dispatched_utc` of `2026-11-01` on a file written `2026-10-14` (w10, w12).
8. Identical mtime `2026-10-13T19:44:48Z` on `round-9`..`round-15` (checkout stamp, not a wave).
9. Age since `run.json` > 900 s on p2 while a member file is < 60 s old.
10. A settled-looking token that is not terminal: w9 "simplifier in flight at closeout"; w18 closeout deferring wave-B to w19. The inverse error — treating closeout as done — is also an age-rule failure if age stops at the closeout mtime.

A results file is also not a sufficient "stop the clock" by itself without a count check. p1-repair is the only positive control on this host: 32 dispatch tasks, 32 results rows, all `completed`, mission-result `total` 32. `after-gates.json` is newer than `results.json` (`00:14:12Z` vs `00:10:26Z`) and did not change between samples (age 1125 s at 00:32:57Z). Post-settlement writes exist. They are not a reason to put the wave back in the unsettled bucket, and they are not member progress (member newest `KakeGateRepair.md` `2026-10-15T00:02:33Z`).

## Smallest safe correction

Do not implement `WAVE_UNSETTLED_AGE` as "(`swarm-registry.json` present) and (results file absent), grade = now − newest mtime", and do not invent a numeric cutoff. None is in the skill.

Detection-only replacement, still read-only:

1. A missing named file is `unavailable` for that name. It is not unsettled and not unhealthy. The live 12h `registry.path` values are unavailable. Genus A dirs are unavailable for settlement, not aged.
2. A settlement **claim** is a typed token, and the filename is not stable. Observed tokens: `results.json` / `ufo-swarm-results-v1`, `mission-result.json` / `ufo-mission-result-v1`, `closeout.json` keys `settled` or `closed_utc`, `closeout.md`, registry keys `closed` / `closed_at` / `verdicts` / `outcomes`. Record which token fired. Do not require the pair the skill names; that pair is not what this host writes.
3. A settlement claim is not a terminal bijection unless the results schema's member count equals the dispatch count and every status is terminal (p1-repair is the only observed case). A closeout that says a seat is in flight stays a claim with that limit attached (w9, w18).
4. Progress is a second sample, with both commands and both timestamps, of the output path the dispatch actually writes: `members/<Name>.md`, or the `reports/round-*` path named in the task file. One sample of mtime is not progress and not stall.
5. Do not read `task-response.json` `progress[].status` on this host. It was `pending` for 32/32 after settlement.
6. Do not subtract a declared `dispatched_utc` or a `dispatched: 26` count from now. Prefer file mtime of the token, and say which file.
7. Do not import the protocol two-tick rule onto wave dirs.

If a later run repeats the three-sample member walk on p3 and p5 and still finds only `run.json`+`spec.json`, the stable id remains `WAVE_UNSETTLED_SURFACE_SILENT`. That is still not a failed wave.

## Blockers

None for this report. Probes that would need a write, a restart, or a fetch were not run. Process-to-wave attribution is unavailable, not blocked: `/proc` cmdline does not carry the wave id, and no other read-only join was found in the wave dir.
