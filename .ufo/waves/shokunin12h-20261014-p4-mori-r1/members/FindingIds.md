# FindingIds — mori stable finding-id vocabulary (r1 contract)

**Lane:** mori-shokunin (森) — detect and report only; never remediate.
**Role of this document:** the compare contract a later census run diffs against.
**Scope:** advisory member report only. Parent integrates gate/corpus/LOG.
**Measured at:** `2026-10-14T21:29:07-03:00` (host local). Live anchors below are
observations that calibrated this vocabulary; they are not a census verdict.

## 0. Stability rules

1. **Id form.** `UPPER_SNAKE_CASE`. No lane prefix (mori owns the vocabulary;
   gate output may print `MORI_CENSUS` as the verdict banner, not as part of the id).
2. **Stable means:** same predicate on the same normalized observation yields the
   same id across runs. Volatile fields (pid number, exact free bytes, wall clock)
   attach as **payload**, never reshape the id.
3. **One finding row = one (id, subject-key).** Subject keys are named per family
   (wave dirname, lane name, mount path, cgroup path, journal cursor/hash, path:line for shape-only secret hits).
4. **Missing surface ≠ unhealthy.** Absence emits a `*_UNAVAILABLE` id (or the
   generic `SURFACE_UNAVAILABLE`) at severity `info`. It never upgrades to
   `warn`/`high`/`critical` solely because the probe could not see the surface.
5. **Observation / inference / unknown stay separate.** Predicates below are
   observations. Inferences (e.g. "daemon died hours ago") stay in prose payload
   under `reading:`, never as a second id.
6. **No remediation verbs in ids.** Ids name the detected state, not the action. Credential/oauth/`server.token`/session material is **SHAPE ONLY**: findings may carry `path:line` and class, **never** the matched span or file body.
7. **Compare contract.** A later run reports `added` / `cleared` / `persisted` /
   `changed-payload` per id+subject. Gate DRIFT means any non-empty set of
   findings whose severity ≥ `warn` under the active profile (see §8), or any
   selftest expected-id mismatch — exact gate mapping is GateDesign's job; this
   file only freezes the ids.

## 1. Severity vocabulary

| Severity | Meaning for mori | Gate weight (proposed) |
|---|---|---|
| `critical` | Fleet driver gone with no completion evidence, active OOM kill this boot on a fleet-relevant cgroup, or disk runway exhausted on a required root | DRIFT |
| `high` | Liveness wedged (process up, tick dead), kill class confirmed this boot, disk below critical threshold, wave aged past stall bound with no progress evidence | DRIFT |
| `warn` | Aged unsettled wave, silent lane, disk below warn threshold, counter/log mismatch, memory headroom low | DRIFT (default profile) |
| `info` | progressing-weak, historical/non-fleet kill class, unavailable surface, probe refused, soft mismatches | CLEAN payload (logged; not DRIFT unless profile says otherwise) |
| *(no finding)* | Surface readable and predicate false | CLEAN |

Severity is a property of the **id definition**, not recomputed ad hoc by the
reporter. Payload may carry measured magnitudes; it does not renumber severity.

## 2. Surface families → id families

| Family | Owns (read-only) | Probe anchors | Id prefix |
|---|---|---|---|
| Watchdog liveness | driver pid/start, `.ufo/watchdog.log` freshness, `.ufo/state/*` counters | `ps`/`pgrep`/`/proc`, `stat` log, read counters | `WATCHDOG_`, `STATE_` |
| Wave settlement | `.ufo/waves/*` registry + dispatch/run + results pair + age | directory listing + JSON presence | `WAVE_` |
| Kill / OOM (journal) | `journalctl --user -b` classed lines | bounded journal grep | `JOURNAL_`, `OOM_`, `KILL_`, `SEGFAULT_`, `UNIT_FAIL_` |
| Cgroup memory | `memory.events`, `memory.current`/`memory.max` | cgroupfs read | `CGROUP_`, `MEM_` |
| Disk runway | fleet root + scratch/tmp roots | `df`/`statvfs` | `DISK_` |
| Lane silence | rostered lane grade silent / progressing / progressing-weak | HEAD time, file mtime, report dir | `LANE_` |
| Meta / census hygiene | probe refusal, secret shape, session-path hops, schema holes | gate internals + path classing | `PROBE_`, `SURFACE_`, `CENSUS_`, `SECRET_`, `SESSION_` |

## 3. Finding-id catalog

Each row: **id**, severity, surface, subject key, observation predicate that
**produces** the finding, and what is **not** this finding.

### 3.1 Watchdog liveness

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `WATCHDOG_ABSENT` | `critical` | driver process | `driver=shokunin-watchdog` | No live process matching the watchdog script/path (`pgrep -af scripts/shokunin-watchdog.sh` empty; `/proc` has no matching cmdline), **and** the log's last line is not a fleet-wrap completion for all rostered lanes in the current program window | Process is present (even if tick is stale → use `WATCHDOG_TICK_STALE`); surface unreadable → `WATCHDOG_SURFACE_UNAVAILABLE` |
| `WATCHDOG_TICK_STALE` | `high` | `.ufo/watchdog.log` | `log=.ufo/watchdog.log` | A watchdog process **is** alive, but last log mtime (or last `tick=N` line timestamp) is older than **2 × INTERVAL** (INTERVAL defaults 450s → stale bound **900s**, matching protocol "two driver ticks") | Process absent (`WATCHDOG_ABSENT`); log missing (`WATCHDOG_LOG_UNAVAILABLE`) |
| `WATCHDOG_LOG_UNAVAILABLE` | `info` | `.ufo/watchdog.log` | `log=.ufo/watchdog.log` | Path missing or unreadable (permission/IO); census cannot grade freshness | File exists and is readable (even if stale) |
| `WATCHDOG_LOG_STALE` | `high` | `.ufo/watchdog.log` | `log=.ufo/watchdog.log` | Log readable, **no** live watchdog process required, last entry age > 2 × INTERVAL, and last line is not a deliberate fleet-wrap quiescence marker covering the roster | Live process + stale tick already covered by `WATCHDOG_TICK_STALE` when process exists; prefer `WATCHDOG_ABSENT` when process gone **and** log non-wrap-stale (emit **both** only if gate profile asks dual-evidence; default profile: `WATCHDOG_ABSENT` primary, `WATCHDOG_LOG_STALE` as supporting payload field `also:`) |
| `WATCHDOG_NO_COMPLETE_LINE` | `high` | `.ufo/watchdog.log` + pid | `lane=<name>` or `driver` | Pid gone (or never observed) and log lacks a `complete`/`wrap` line for the in-flight mission — SKILL error pattern "daemon death" | Pid gone after an explicit `complete`/`wrap` (expected quiescence; no finding or `info` only) |
| `STATE_COUNTER_UNAVAILABLE` | `info` | `.ufo/state/` | `path=.ufo/state` | State dir or a rostered `<lane>.round` file missing/unreadable | File present (value may still mismatch log) |
| `STATE_COUNTER_LOG_MISMATCH` | `warn` | `.ufo/state/<lane>.round` vs log | `lane=<name>` | Parsed round counter ≠ last `launch`/`complete`/`wrap` round evidenced in watchdog.log for that lane | Counter agrees; log unavailable (then only `WATCHDOG_LOG_UNAVAILABLE`) |
| `WATCHDOG_SURFACE_UNAVAILABLE` | `info` | ps/proc aggregate | `probe=watchdog-liveness` | Entire liveness probe blocked (no `/proc`, pgrep missing) without a substitute | Partial read succeeded |

**Live calibration (observation, not verdict):** at `2026-10-14T21:29:07-03:00`,
`pgrep -af scripts/shokunin-watchdog.sh` → empty; `.ufo/watchdog.log` mtime
`2026-10-13 16:44:48-03:00` (last lines are fleet-wrap). Under this vocabulary that
pair is primarily `WATCHDOG_ABSENT` **or** wrap-quiescence with no critical if the
active program no longer expects the v4 driver — gate must take an explicit
`expect_driver=yes|no|wrap-ok` input; default for a live fleet program is
`expect_driver=yes` → `WATCHDOG_ABSENT`.

### 3.2 Wave settlement

Settlement join (two wire shapes observed on this host):

- **Train waves:** `swarm-registry.json` + `dispatch.json` (+ optional `results.json`).
- **12h/ufo-swarm waves:** `run.json` (embeds registry) + optional `results.json`
  (`schema: ufo-swarm-results-v1`) + optional `task-response.json`.

| id | sev | surface | subject | Produces when | Not this id when |
|---|---|---|---|---|---|
| `WAVE_REGISTRY_ABSENT` | `warn` | wave dir | `wave=<dirname>` | Dir under `.ufo/waves/` looks like a dispatched wave (has `spec.json` or `run.json` or `dispatch.json`) but has neither `swarm-registry.json` nor a `run.json` registry block | Dir is a non-wave workspace (fixtures-only, scripts-only) — classify as non-subject, no finding |
| `WAVE_DISPATCH_ABSENT` | `warn` | wave dir | `wave=<dirname>` | Registry present (or run.json present) but neither `dispatch.json` nor `run.json` carries a dispatch/taskCall payload | Pre-dispatch draft with only `spec.json` and no registry — `WAVE_SPEC_ONLY` |
| `WAVE_SPEC_ONLY` | `info` | wave dir | `wave=<dirname>` | Only `spec.json` (and maybe notes) — never dispatched | Dispatch artifacts exist |
| `WAVE_UNSETTLED` | `warn` | wave dir | `wave=<dirname>` | Dispatched (registry/run present) and **no** terminal results payload (`results.json` absent, or results members incomplete vs registry) | Results complete join (every registry member has a results row) |
| `WAVE_UNSETTLED_AGE` | `high` | wave dir | `wave=<dirname>` | `WAVE_UNSETTLED` holds **and** age since `dispatched_at` / run stamp / dir mtime ≥ stall bound. **Default stall bound (proposal, DiskThresholds/WaveAgeMath may revise):** `max(3 × watchdog INTERVAL, 1800s)` = 1800s when INTERVAL=450 | Unsettled but younger than bound → `WAVE_UNSETTLED` only; settled → no age finding |
| `WAVE_SETTLED_PARTIAL` | `warn` | results join | `wave=<dirname>` | `results.json` exists but member set ≠ registry set (unmapped member or unexpected row) | Exact join |
| `WAVE_RESULTS_SCHEMA_DRIFT` | `info` | results.json | `wave=<dirname>` | Results present but schema/string markers unrecognized | Schema matches known v1 |
| `WAVE_SURFACE_UNAVAILABLE` | `info` | `.ufo/waves` | `path=.ufo/waves` | Waves root unreadable | Root lists |

**Live calibration:** host listing at measure time showed multiple
`shokunin-train-*` dirs with registry+dispatch and **no** `results.json`
(`WAVE_UNSETTLED` / possibly `WAVE_UNSETTLED_AGE`), and
`shokunin12h-20261014-p1-repair` with `run.json`+`results.json` (settled shape).
Age math is deferred to WaveAgeMath; ids stay fixed.

### 3.3 Journal kill / OOM classes

Classes are **string-signature → class** (OomClassTaxonomy owns the table; ids
freeze the class names).

| id | sev | surface | subject | Produces when | Signature seeds (observation) |
|---|---|---|---|---|---|
| `OOM_KILL_EVENT` | `high` | journal `--user -b` | `boot=<boot-id>;cursor|ts=` | Line classifies as kernel/user OOM kill this boot | `oom-kill`, `Killed process`, `Out of memory`, systemd `Failed with result 'oom-kill'` |
| `OOM_KILL_EVENT` | *(same)* | — | — | **Fleet-relevant** if cgroup/unit path touches fleet/tmux/node/ufo/watchdog; still emit id, payload `fleet_relevant=true|false` | Example observed: `Failed with result 'oom-kill'` @ `2026-10-13T23:44:31-03:00` |
| `KILL_SIGNAL_EVENT` | `warn` | journal | `boot=…;ts=` | Process killed by signal (SIGKILL/SIGTERM) without OOM class | `killed by signal`, `signal=9`, `signal=15` |
| `SEGFAULT_EVENT` | `warn` | journal | `boot=…;ts=` | segfault / core-dump class | `segfault`, `core dumped`, `Failed with result 'core-dump'` (observed pipewire-pulse core-dump @ `2026-10-14T18:54:21-03:00`) |
| `UNIT_FAIL_EVENT` | `info` | journal | `boot=…;ts=` | systemd unit failure **not** already classified above | `Failed with result` other than oom-kill/core-dump |
| `JOURNAL_UNAVAILABLE` | `info` | journalctl | `probe=journal-user-boot` | `journalctl --user -b` fails (no access, empty, binary missing) | Readable journal (zero hits = no kill findings, not unavailable) |
| `JOURNAL_PROBE_REFUSED` | `info` | policy | `probe=journal` | Probe would require write, root escalation, or external fetch | Normal user journal read |

Dedup: one physical line → one primary class id. Do not double-fire
`OOM_KILL_EVENT` and `UNIT_FAIL_EVENT` for the same oom-kill unit failure.

### 3.4 Cgroup memory

| id | sev | surface | subject | Produces when | Not |
|---|---|---|---|---|---|
| `CGROUP_OOM_KILL` | `high` | `memory.events` | `cgroup=<path>` | Field `oom_kill` **increases** vs census baseline, or absolute `oom_kill > 0` on first run with `baseline=boot-zero` profile | `oom` counter without `oom_kill` → `CGROUP_OOM_EVENT` |
| `CGROUP_OOM_EVENT` | `warn` | `memory.events` | `cgroup=<path>` | `oom > 0` (pressure trip) while `oom_kill == 0` | kill happened |
| `CGROUP_MEM_HIGH` | `warn` | `memory.events` | `cgroup=<path>` | `high > 0` or `max > 0` events non-zero since baseline | clean zeros |
| `CGROUP_MEM_CURRENT_UNAVAILABLE` | `info` | `memory.current` | `cgroup=<path>` | File missing/unreadable | Readable |
| `MEM_HEADROOM_LOW` | `warn` | host + cgroup | `scope=host` or `cgroup=` | `MemAvailable` / `memory.current` vs `memory.max` below headroom warn ratio (**proposal default:** available < 15% of total **or** current > 85% of max when max ≠ max) | Above ratio; unknown max → unavailable not low |
| `MEM_HEADROOM_CRITICAL` | `high` | host + cgroup | `scope=host` | Available < 5% total **or** current ≥ 95% max (proposal) | — |
| `MEM_PRESSURE_UNAVAILABLE` | `info` | `/proc/meminfo` / cgroup | `probe=mem` | Cannot read MemAvailable and cgroup current | Partial read: report what exists |

**Live calibration:** `/sys/fs/cgroup/user.slice/memory.events` showed
`oom_kill 1` at measure time → predicate for `CGROUP_OOM_KILL` is true under
`baseline=boot-zero` absolute profile. Host `MemAvailable` ≈ 21.8 GiB / 32.5 GiB
total → not `MEM_HEADROOM_LOW` at 15% warn.

### 3.5 Disk runway

Roots in scope: fleet root (`$SK` → `/home/vgpnk/Projects/shokunin`'s fs),
`/tmp`, `/scratch/tmp` if present. Additional roots only if gate config lists them.

| id | sev | surface | subject | Produces when | Not |
|---|---|---|---|---|---|
| `DISK_LOW` | `warn` | `df`/`statvfs` | `mount=<path>` | Used% ≥ warn threshold **or** available bytes ≤ warn floor | Below thresholds |
| `DISK_CRITICAL` | `critical` | same | `mount=<path>` | Used% ≥ critical threshold **or** available ≤ critical floor | — |
| `DISK_ROOT_UNAVAILABLE` | `info` | path | `mount=<path>` | Root not present (e.g. `/scratch/tmp` absent) or not mounted — **unavailable, never unhealthy** | Present |
| `DISK_PROBE_UNAVAILABLE` | `info` | `df` | `probe=disk` | `df`/`statvfs` failed entirely | Partial |

**Thresholds (proposals until DiskThresholds falsifies; pinned as named constants):**

| constant | default | applies |
|---|---|---|
| `DISK_WARN_PCT` | `85` | all in-scope roots |
| `DISK_CRIT_PCT` | `95` | all in-scope roots |
| `DISK_WARN_AVAIL_BYTES` | `5 GiB` | fleet + scratch |
| `DISK_CRIT_AVAIL_BYTES` | `1 GiB` | fleet + scratch |
| `DISK_TMP_WARN_PCT` | `80` | `/tmp` (tmpfs; tighter because swap-backed pressure couples to MEM_*) |

Either pct **or** avail-bytes trip fires the id (OR). Payload records both.

**Live calibration:** fleet fs 10% used / 835G avail → clean; `/tmp` 60% used →
clean under defaults; `/scratch/tmp` absent → `DISK_ROOT_UNAVAILABLE`
(`mount=/scratch/tmp`), not `DISK_LOW`.

### 3.6 Lane silence

Grades mirror protocol stale-lane actuator (silent / progressing /
progressing-weak). **Commit sparsity alone is never failure** (SKILL + protocol).

| id | sev | surface | subject | Produces when | Not |
|---|---|---|---|---|---|
| `LANE_SILENT` | `warn` | lane repo + reports | `lane=<name>` | Mission open longer than **two ticks (900s)** from launch/report baseline **and** no lane-authored commit **and** no lane-owned file mtime activity in write scope since launch | Activity exists; sibling-only activity → `LANE_PROGRESSING_WEAK` |
| `LANE_PROGRESSING_WEAK` | `info` | lane repo | `lane=<name>` | Only sibling/operator-identity activity in the lane tree since launch; no lane-authored commit/file | Lane-authored activity → no finding (grade progressing is CLEAN) |
| `LANE_REPORT_ABSENT` | `warn` | `.ufo/reports/…` | `lane=<name>;round=N` | Counter/log says round N in flight or completed without a report file where the driver expects one | Report file exists (content quality is out of mori grade except emptiness markers left to protocol) |
| `LANE_GRADE_UNAVAILABLE` | `info` | git/fs | `lane=<name>` | Cannot read HEAD or mtimes (missing repo, not a git dir) | Readable |

`LANE_SILENT` is the prompt's exemplar id; it is the only silence grade that
DRIFTs by default. `LANE_PROGRESSING_WEAK` is informational compare-fodder.

### 3.7 Meta / census hygiene

| id | sev | surface | subject | Produces when |
|---|---|---|---|---|
| `SURFACE_UNAVAILABLE` | `info` | any | `surface=<name>` | Generic fallback when a family-specific `*_UNAVAILABLE` does not apply |
| `PROBE_REFUSED` | `info` | policy | `probe=<name>;reason=` | Probe would write, restart, kill, dispatch, pacman/systemd-mutate, or external-fetch. Credential/session path hops use `SESSION_READ` instead (do not double-fire). |
| `SECRET_SHAPED` | `warn` | path classing (no content read of secret body) | `path=<path>;line=<n>;class=<token-class>` | A census path/list/journal *name* or line **shape** matches a credential-class pattern (e.g. path under `credentials/`, `oauth/`, `op.env`, basename `server.token`, or a redacted journal field class). Payload **MUST** print `path:line` and `class` only — **NEVER** the matched span, secret bytes, or token value. File body is not opened for content. |
| `SESSION_READ` | `warn` | hop policy | `probe=<name>;path=<path>;class=session|credential` | A planned probe hop **would** open a credential or session path (`credentials/`, `oauth/`, `server.token`, session store, cookie/token file). Finding fires on the hop intent; **the file is not opened**. Prefer this over generic `PROBE_REFUSED` for secret paths. |
| `CENSUS_PAYLOAD_VOLATILE` | `info` | gate | `field=<name>` | Field excluded from compare normalization (pid, free bytes raw, timestamps) — documentation id for selftest, rarely emitted live |
| `CENSUS_SELFTEST_DRIFT` | `high` | fixtures | `case=<name>` | `--selftest` expected id set ≠ actual (gate-internal) |

**Secret payload contract (normative):** `SECRET_SHAPED` payload fields allowed: `path`, `line`, `class`, `probe`, `measured_at`. Forbidden in payload and logs: matched substring, file slice, env value, token, cookie, authorization header. `SESSION_READ` payload: `probe`, `path`, `class`, `measured_at` only — no open, no stat-of-contents beyond path existence classing if already known without read.

## 4. Clean (non-finding) states — named for selftest NO-FIRE cases

These are **not** finding ids. FixtureDesign / GateDesign assert they produce
**empty** finding lists:

| clean label | observation |
|---|---|
| `WATCHDOG_ALIVE_FRESH` | pid present; last tick age ≤ 2 × INTERVAL |
| `WAVE_SETTLED_JOIN` | registry/run members == results members |
| `JOURNAL_QUIET_BOOT` | journal readable; zero class hits this boot |
| `CGROUP_EVENTS_ZERO` | oom/oom_kill/high/max all 0 (or unchanged vs baseline) |
| `DISK_RUNWAY_OK` | all present roots under warn thresholds |
| `LANE_PROGRESSING` | lane-authored activity within window |
| `MEM_HEADROOM_OK` | available above warn ratio |

## 5. Owner routing (report-only pointer; OwnerMap expands)

| id pattern | remediation owner (not mori) |
|---|---|
| `WATCHDOG_*`, `STATE_*`, `WAVE_*`, `LANE_*` | operator / kumitate (dispatch mechanism) |
| `JOURNAL_*`, `OOM_*`, `KILL_*`, `SEGFAULT_*`, `UNIT_FAIL_*`, `CGROUP_*`, `MEM_*` | operator / tsukuroi (OS planes) — mori only reports fleet-relevant evidence |
| `DISK_*` | operator |
| `PROBE_REFUSED`, `SURFACE_*`, `CENSUS_*`, `SECRET_SHAPED`, `SESSION_READ` | mori gate maintainers (shape/refusal); kagi owns credential *custody*, not these detections |

mori **never** appears as remediation owner.

## 6. Compare algorithm (contract)

Input: previous receipt `F0`, current receipt `F1`, each a set of
`{id, subject, sev, payload}`.

```
key(f)       = id + "\0" + subject
added        = keys(F1) - keys(F0)
cleared      = keys(F0) - keys(F1)
persisted    = keys(F0) ∩ keys(F1)
changed-payload = persisted where payload_norm differs
```

`payload_norm` drops volatile fields (`pid`, `available_bytes_raw`,
`measured_at`, `cursor`) and keeps magnitudes binned if needed
(e.g. disk used% integer).

Gate banner:

- `MORI_CENSUS: CLEAN` — no findings with sev ∈ {`warn`,`high`,`critical`}
  (default profile), selftest green.
- `MORI_CENSUS: DRIFT` — any such finding, or selftest id mismatch.
- exit `2` — setup/usage (not a finding id).

## 7. Exemplars from the prompt (normative)

| exemplar | status in this catalog |
|---|---|
| `WATCHDOG_ABSENT` | §3.1 critical |
| `WAVE_UNSETTLED_AGE` | §3.2 high |
| `OOM_KILL_EVENT` | §3.3 high |
| `DISK_LOW` | §3.5 warn |
| `LANE_SILENT` | §3.6 warn |

## 8. Profiles (gate knobs; ids unchanged)

| profile | effect |
|---|---|
| `default` | DRIFT on sev ≥ `warn` |
| `strict` | DRIFT on sev ≥ `info` (except pure `*_UNAVAILABLE` / `PROBE_REFUSED`; `SECRET_SHAPED` and `SESSION_READ` still weigh at `warn`) |
| `liveness-only` | only `WATCHDOG_*` + `STATE_*` + `LANE_SILENT` weigh |
| `boot-zero-cgroup` | absolute cgroup counters (first-run) |
| `delta-cgroup` | only counter increases vs last receipt |

## 9. Out of vocabulary (explicit non-ids)

Do **not** invent findings for:

- pacman/systemd unit enablement state (tsukuroi)
- endpoint/model health (kama)
- credential *validity* or vault unlock (kagi) — mori only emits `SECRET_SHAPED` / `SESSION_READ` shape+hop detections, never validates secrets
- dispatch start/stop success (kumitate)
- "should restart X" recommendations phrased as ids

## 10. Provenance anchors (this drafting run)

| claim | command / path | at |
|---|---|---|
| measure timestamp | `date -Iseconds` → `2026-10-14T21:29:07-03:00` | live |
| watchdog process count | `pgrep -af scripts/shokunin-watchdog.sh` → empty | live |
| watchdog log mtime | `stat` → `2026-10-13 16:44:48-03:00` | live |
| user.slice oom_kill | `cat …/user.slice/memory.events` → `oom_kill 1` | live |
| disk fleet / tmp | `df -P` → 10% / 60% | live |
| scratch absent | `test -e /scratch/tmp` → exit 1 | live |
| wave wire shapes | listing under `.ufo/waves/*` | live |
| INTERVAL / two-tick bound | `scripts/shokunin-watchdog.sh` `INTERVAL=450`; protocol two ticks = 900s | source |
| province surfaces | `mori-shokunin/{PROVINCE,SKILL}.md` | source |
| demand (historical OOM) | `.ufo/scopes/shokunin-12h-20261014/operator-demand.md` — demand evidence, not re-run | source |

## 11. Limits

- Threshold constants marked **proposal** until DiskThresholds / WaveAgeMath /
  MemoryPressureReading land revisions; **id strings do not change** when
  thresholds do — only predicates' numeric bounds.
- Journal class signatures are seeds; OomClassTaxonomy may extend signature
  lists without renaming ids.
- This report does not implement `tools/mori-census.sh` and does not claim a
  live `MORI_CENSUS: CLEAN|DRIFT` verdict.
- No remediation was performed.

---

**Axes self-check (advisory):**

| axis | how this artifact serves it |
|---|---|
| coverage | all six probe families + meta; five prompt exemplars normative |
| operability | subject keys, compare algorithm, gate banner mapping, selftest clean labels |
| calibration | unavailable≠unhealthy; silence≠commit sparsity; wrap-quiescence vs absent; proposal thresholds labeled; live anchors separated from inferences |
