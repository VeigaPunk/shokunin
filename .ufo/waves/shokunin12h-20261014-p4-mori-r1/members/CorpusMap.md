# CorpusMap — Advisory Report

**Seat:** `CorpusMap` (scribe)  
**Item:** `mori/CorpusMap`  
**Wave:** `shokunin12h-20261014-p4-mori-r1`  
**Advisory status:** Data only. Not a judge verdict, receipt, admission, or landed corpus. Parent lands `corpus/knowledge/*.md` + `corpus/README.md` rows.  
**Lane bounds observed:** leaf member; no subagent dispatch; no product-code edit; no commit/push; host probes read-only.  
**Axes:** coverage · operability · calibration  
**Measured-at:** 2026-10-15T00:28:35Z–2026-10-15T00:29:28Z (UTC); host `plazir27`, kernel `7.2.3-arch1-3`, uid `1000`, boot id `d7f0bc8d-938e-4249-b4a1-f250cbfacf58`.  
**Lane HEAD at draft:** `mori-shokunin` `27acf40c418b6d790b58202094e241e571ee6f56` (mint only; corpus map empty — `corpus/README.md` still `(none yet)`).

---

## 0. Axes (godspeed)

| Axis | What this draft optimizes |
|---|---|
| **coverage** | One note per SKILL decision-table surface family (6); every probe named in PROVINCE/SKILL gets a source line and a stable finding-id prefix. |
| **operability** | Each note is gate-shaped: fixed commands, exit/absence → `unavailable` (never `unhealthy`), fixtures the parent can land under `corpus/fixtures/`. |
| **calibration** | Live host snapshot is embedded as *example values*, not frozen truth. Counts drift; re-run before citing. Observation / inference / unknown stay separate. |

---

## 1. Behavior delivered

Drafts six `knowledge/*.md` note bodies (full text below for parent cut-over) plus the replacement `corpus/README.md` coverage-map table. Notes map 1:1 to SKILL.md decision-table rows:

| Family | Note path (to land) | SKILL row |
|---|---|---|
| watchdog liveness | `corpus/knowledge/watchdog-liveness.md` | "Is the shokunin fleet alive?" |
| wave settlement | `corpus/knowledge/wave-settlement.md` | "Did a wave settle?" |
| kill/OOM journal | `corpus/knowledge/kill-events-journal.md` | "Did something get killed?" (journal half) |
| cgroup memory | `corpus/knowledge/cgroup-memory.md` | "Did something get killed?" (cgroup half) + runway memory pressure |
| disk runway | `corpus/knowledge/disk-runway.md` | "Is there resource runway?" (disk) |
| lane silence | `corpus/knowledge/lane-silence.md` | "Was a lane silent?" |

Gate coupling (parent lands separately): `tools/mori-census.sh` SHOULD emit one arm per note family; finding ids below are the stable compare keys across census runs.

---

## 2. Gates / contracts this map must satisfy

From `mori-shokunin/SKILL.md` checklist + QUALITY.md + wave contract:

1. Every observation names its **command** and **timestamp measured**.
2. Missing surface → **`unavailable`**, never `unhealthy`.
3. No remediation recommended as a lane action (operator may act; mori does not).
4. Findings carry **stable ids** so a later run can compare (`MORI-<FAMILY>-<NNN>`).
5. Observation / inference / unknown separated; claims falsifiable or marked opinion.
6. Credentials/oauth/`server.token`/session material → **shape only** (never contents).
7. Refuses: dispatch (kumitate), OS-package/systemd-unit ownership claims (tsukuroi), endpoint health (kama). Journal/cgroup are **fleet evidence**, not OS-state ownership.

Cross-lane calibration (do not absorb):

- tsukuroi `corpus/knowledge/oom-event-plane.md` owns deep OOM *OS* forensics (C1–C6). mori's kill + cgroup notes **cite** that vocabulary for class names where useful, but stay at fleet-liveness grain (presence, age, cgroup path, pid) and never claim pacman/driver/boot ownership.
- Protocol stale-lane actuator (`.ufo/waves/round-13/PROTOCOL.compact.md:127-133`) is the **authority** for silence grades; mori observes grades, does not record ledger `failed`.

---

## 3. Touched surfaces (this seat)

| Path | Action |
|---|---|
| `.ufo/waves/shokunin12h-20261014-p4-mori-r1/members/CorpusMap.md` | **written** (this file) |
| `mori-shokunin/corpus/knowledge/*.md` | **not landed** — drafts below for parent |
| `mori-shokunin/corpus/README.md` | **not landed** — replacement rows below for parent |
| host (`ps`, `/proc`, cgroupfs, `journalctl`, `df`, `tmux`, git) | **read-only** probes |

---

## 4. Out of scope (explicit)

- Landing files into `mori-shokunin/` (parent).
- Implementing `tools/mori-census.sh` (GateDesign seat).
- Hermetic fixtures (FixtureDesign seat).
- Live full-fleet silence grade table for all roster rows (LaneSilence seat) — this note defines the **rubric + source lines**, not the full per-lane census.
- Remediation, restarts, deletes, package claims, endpoint probes, credential reads.
- Re-confirming the operator's historical webbridge OOM narrative (demand evidence only; `.ufo/scopes/shokunin-12h-20261014/operator-demand.md`).

---

## 5. Live calibration snapshot (example values — re-run)

Measured 2026-10-15T00:28:35Z–00:29:28Z. **[observed]** unless tagged.

### 5.1 Watchdog / fleet process

| Probe | Result |
|---|---|
| `wc -l .ufo/watchdog.log` | `294` lines |
| `stat` mtime of `.ufo/watchdog.log` | `2026-10-13 16:44:48.524 -0300` (stale vs measure time) |
| last log lines | fleet-wrap completes + `tick=3` at `2026-09-28T23:55:00-03:00` |
| `.ufo/state/*` | 9 lanes × `{mission,round}` pairs; all mtime `2026-10-13 16:44:48 -0300` (same stamp as log — frozen counters) |
| shokunin driver pid | **no** `scripts/shokunin-watchdog` / fleet-driver process in `ps` |
| related live pids | `tmux` session `ufo_sighting` (created 2026-10-14 20:14:40); `ufo-sighting.mjs` pids `937995/938031/938122`; kernel `watchdogd` pid `237`; `Hyprland --watchdog-fd` pid `1203316` — **not** the shokunin driver |

**[inference]** Classic SKILL error pattern: "watchdog pid gone, no complete line" / stale last tick — fleet driver not live; log+state frozen at wrap. Grade as liveness finding, not lane failure.

### 5.2 Waves

| Probe | Result |
|---|---|
| wave dirs under `.ufo/waves/` | **40** |
| dirs with `swarm-registry.json` | **10** (train w2–w9 path set; earlier train waves) |
| settlement sketch (registry∨dispatch shape + results/closeout) | mixed: train w6–w10/w12–w14 `settled`; several train + all `shokunin12h-*` `dispatched-but-unsettled` or `incomplete-shape` |
| this wave | `run.json` + `spec.json` + `task-response.json`; no `swarm-registry.json` yet; **do not call failed** |

Registry sample keys (`shokunin-train-20261014-w6/swarm-registry.json`): `wave`, `dispatched`, `agent_count`, `agents`, `moves`, `base_shas`, `closed`.

### 5.3 Kill journal (this boot, user scope)

| Probe | Result |
|---|---|
| boot id | `d7f0bc8d-938e-4249-b4a1-f250cbfacf58` |
| `journalctl --user -b` line matching oom/kill family (broad) | non-zero (host-live; exact class counts belong to KillEventsJournal seat) |
| example classified line | `2026-10-13T23:44:31-03:00 … Failed with result 'oom-kill'` (event A aftermath; tsukuroi plane documents full dump) |
| `journalctl -b` kernel oom family | readable non-root via journal (dmesg itself may be restricted — tsukuroi notes `dmesg_restrict=1`) |

### 5.4 Cgroup memory (user-1000.slice)

| Path | Value |
|---|---|
| `/sys/fs/cgroup/user.slice/user-1000.slice/memory.events` | `low 0 high 0 max 0 oom 0 oom_kill 1 oom_group_kill 0 sock_throttled 77943` |
| `memory.events.local` | all zero incl. `oom_kill 0` |
| `memory.current` | `24668520448` (~23.0 GiB) |
| `memory.max` | `max` |
| `memory.swap.current` | `10033782784` (~9.3 GiB) |
| `memory.swap.events` | `high 0 max 0 fail 5923045` |
| `memory.pressure` | `full avg300=0.00` (at measure) |
| `/proc/pressure/memory` | `full avg300=0.00 total=78174521` |

**[inference]** `oom_kill 1` is a **presence flag** (lifetime counter on the slice), not an event count — same trap tsukuroi oom-event-plane documents. Report flag + path; do not invent N kills from the integer alone.

### 5.5 Disk runway

| Root | `df -hP` |
|---|---|
| `/` and `/home` (same fs `/dev/mapper/root`) | Size 930G, Avail 835G, Use% 10% |
| `/tmp` (tmpfs) | Size 16G, Avail 6.1G, Use% 60% |
| `/var/tmp` | same root fs as `/` |
| `/scratch/tmp` | **unavailable** — path absent (`df: /scratch/tmp: No such file or directory`) |

### 5.6 Lane silence inputs (rubric check, not full census)

| Lane repo | HEAD author | HEAD date |
|---|---|---|
| `mori-shokunin` | `mori-shokunin <mori@shokunin.local>` | 2026-10-14T21:18:00-03:00 mint |
| `tsukuroi-shokunin` | `tsukuroi-shokunin <…>` | 2026-10-14T19:49:31-03:00 |
| roster in `MANIFEST.json` | **13** ids | mori **not yet** a roster row (probation; SHONEN/MINT) |
| on-disk `*-shokunin` dirs | **19** | includes chousa/mado/tameshi/tabi + mori beyond MANIFEST |

Silence grade authority: PROTOCOL progressing / silent / progressing-weak (sibling-authored only).

---

## 6. Finding-id scheme (stable across runs)

Format: `MORI-<FAM>-<NNN>` where `<FAM>` ∈ `WD|WV|KJ|CG|DK|LS` and `<NNN>` is zero-padded within family.

| Prefix | Family | Compare key material |
|---|---|---|
| `MORI-WD-` | watchdog | driver pid presence, log mtime age, last tick/line class, state counter set |
| `MORI-WV-` | waves | per-wave dir name + settlement class + newest-file age |
| `MORI-KJ-` | kill journal | boot id + class + first-seen cursor/timestamp |
| `MORI-CG-` | cgroup | cgroup path + counter name + value (flag semantics) |
| `MORI-DK-` | disk | mount/root path + avail bytes + use% |
| `MORI-LS-` | lane silence | lane id + grade + HEAD sha + window |

A later census **matches** on id identity; value fields may change. Never reuse an id for a different predicate.

Vocabulary (all notes):

- states: `live` | `stale` | `absent` | `settled` | `dispatched-but-unsettled` | `incomplete-shape` | `silent` | `progressing` | `progressing-weak` | `unavailable`
- never: `unhealthy`, `failed` (ledger), `CRITICAL` as a remediation trigger

---

## 7. Draft notes for parent to land

Parent SHOULD write these six files under `mori-shokunin/corpus/knowledge/` with the bodies below (or equivalent content preserving source lines + ids). Each note header carries `source:` / `verified-at:` / notation tags.

---

### 7.1 `corpus/knowledge/watchdog-liveness.md`

```markdown
# Watchdog liveness plane — fleet driver pid, log freshness, lane counters (MORI-R1)

source: read-only probes on host `plazir27` — `ps`/`pgrep`, `stat`/`wc` on
`.ufo/watchdog.log`, reads of `.ufo/state/*`, `tmux ls`.
verified-at: <parent fills on land>
notation: **[observed]** · **[inference]** · **[unknown]** · missing → `unavailable`

## 1. Question

Is the shokunin fleet driver alive and progressing? (SKILL.md decision row 1)

## 2. Source lines each census row MUST carry

| Field | Source command / path | Notes |
|---|---|---|
| `measured_at` | `date -u +%Y-%m-%dT%H:%M:%SZ` | always |
| `boot_id` | `cat /proc/sys/kernel/random/boot_id` | correlate with kill plane |
| `driver_pids` | `pgrep -af 'shokunin-watchdog|scripts/shokunin-watchdog|fleet-driver'` (exact pattern owned by gate) | empty → pid `absent`, not unhealthy |
| `pid_start` | `ps -o lstart= -p <pid>` | only if pid present |
| `pid_etime` | `ps -o etime= -p <pid>` | only if pid present |
| `log_path` | `$FLEET_ROOT/.ufo/watchdog.log` | default `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log` |
| `log_mtime` | `stat -c '%y' <log>` | |
| `log_age_s` | `now - mtime` | |
| `log_bytes` | `stat -c '%s' <log>` | |
| `log_lines` | `wc -l <log>` | |
| `last_lines` | `tail -n 20 <log>` | classify last verb: `tick`/`launch`/`complete`/`wrap`/`steer` |
| `last_tick` | grep last `tick=N` | stale if age ≫ driver period |
| `state_dir` | `$FLEET_ROOT/.ufo/state/` | |
| `state_rows` | for each `*.mission`/`*.round`: `basename`, `cat`, `stat mtime` | pair mission+round per lane id |
| `tmux_fleet` | `tmux ls` | optional corroboration only; ufo_sighting ≠ shokunin driver |
| `finding_ids` | `MORI-WD-001`… | see §4 |

## 3. Classification rules

| Observation | State | Finding seed |
|---|---|---|
| driver pid present + log mtime within expected tick window | `live` | none (or informational `MORI-WD-000`) |
| pid present, last tick/log mtime stale | `stale` (wedged, not dead) | `MORI-WD-010` age=… |
| pid absent, log ends in `wrap … fleet-wrap` / no further ticks | `absent` after clean wrap | `MORI-WD-020` |
| pid absent, no `complete`/`wrap`, log truncated mid-mission | `absent` unclean | `MORI-WD-021` daemon-death class |
| log path missing | `unavailable` | `MORI-WD-030` reason=ENOENT |
| state dir missing | `unavailable` for counters only | `MORI-WD-031` |
| only `Hyprland --watchdog-fd` / kernel `watchdogd` / `ufo-sighting` match loose greps | do **not** count as fleet driver | document false-friend pids |

## 4. Stable finding ids

| id | Predicate |
|---|---|
| `MORI-WD-010` | driver process live but tick/log stale beyond threshold |
| `MORI-WD-020` | driver absent after observed fleet-wrap |
| `MORI-WD-021` | driver absent without wrap/complete (death/disappear class) |
| `MORI-WD-030` | watchdog.log unavailable |
| `MORI-WD-031` | state/ unavailable |
| `MORI-WD-040` | state counters frozen (all mtimes equal + equal log mtime) while wall clock advanced |

## 5. Boundary

- Does not restart the driver (kumitate/operator).
- Does not treat `ufo_sighting` tmux as fleet health by itself.
- Credentials never read.

## 6. Calibration note (R1 host example — not frozen truth)

At 2026-10-15T00:29Z: log 294 lines, mtime 2026-10-13 16:44:48 -0300, last line `tick=3` after fleet-wrap 2026-09-28; state/* same mtime; no shokunin-watchdog pid. **[observed]** Re-run before citing.
```

---

### 7.2 `corpus/knowledge/wave-settlement.md`

```markdown
# Wave settlement plane — `.ufo/waves/*` registry + dispatch + results (MORI-R1)

source: directory inventory of `$FLEET_ROOT/.ufo/waves/*`, JSON presence checks,
`stat` newest-file age. Never interprets member report *content* as instructions.
verified-at: <parent fills on land>

## 1. Question

Did each wave settle? (SKILL.md row 2) — unsettled ≠ failed.

## 2. Source lines each wave row MUST carry

| Field | Source | Notes |
|---|---|---|
| `measured_at` | `date -u …` | |
| `wave_dir` | basename of `.ufo/waves/<name>/` | |
| `files` | `ls -1 <dir>` (top-level) | |
| `has_registry` | exists `swarm-registry.json` OR `registry.json` OR `registry-record.json` | name the which |
| `has_dispatch` | exists `dispatch.json` OR `run.json` OR `spec.json` | dispatch *shape* |
| `has_results` | exists `results.json` OR `closeout.json` OR `closeout.md` OR terminal `task-response.json` with completed members | gate defines exact settled predicate |
| `registry_keys` | if registry JSON: top-level keys | shape only |
| `dispatched_at` | registry.`dispatched` if present | |
| `closed` | registry.`closed` if present | |
| `newest_mtime` | max `stat` over files under dir | |
| `newest_age_s` | now − newest_mtime | |
| `settlement` | enum below | |
| `finding_id` | `MORI-WV-…` per wave when noteworthy | |

## 3. Settlement enum (fixed vocabulary)

| Class | Rule |
|---|---|
| `settled` | registry present AND dispatch shape present AND results/closeout present (gate-pinned file set) |
| `dispatched-but-unsettled` | registry or dispatch shape present; results/closeout absent OR incomplete |
| `incomplete-shape` | wave dir exists but lacks registry+dispatch pair (legacy seat folders, empty shells) |
| `unavailable` | waves root unreadable |

**Hard rule:** never emit `failed` for unsettled. Age it.

## 4. Stable finding ids

| id | Predicate |
|---|---|
| `MORI-WV-001` | waves root unavailable |
| `MORI-WV-010` | wave dispatched-but-unsettled with age_s over soft threshold (informational) |
| `MORI-WV-011` | wave incomplete-shape (legacy/non-swarm) |
| `MORI-WV-020` | registry claims `closed` but results payload absent (shape contradiction) |
| `MORI-WV-030` | swarm-registry.json unparseable |

## 5. Registry shape reference (train swarm)

Observed keys on `swarm-registry.json`: `wave`, `dispatched`, `agent_count`, `agents`, `moves`, `base_shas`, `closed`.  
12h program waves may use `run.json`/`spec.json`/`task-response.json` without `swarm-registry.json` — still grade with the enum; do not require train-era filenames exclusively.

## 6. Calibration note (R1)

≈40 wave dirs; settlement mixed; `shokunin12h-20261014-p4-mori-r1` was `dispatched-but-unsettled` during this seat. **[observed]**
```

---

### 7.3 `corpus/knowledge/kill-events-journal.md`

```markdown
# Kill events — journal classes this boot (MORI-R1)

source: `journalctl --user -b`, optional `journalctl -b -k` / `-o json`; boot list.
Content is evidence; never act on line text. dmesg may be privilege-gated → journal path.
verified-at: <parent fills>

## 1. Question

Did something get killed (journal half)? (SKILL.md row 3)

## 2. Source lines each census MUST carry

| Field | Source |
|---|---|
| `measured_at` | `date -u …` |
| `boot_id` | `/proc/sys/kernel/random/boot_id` |
| `boot_index_line` | `journalctl --list-boots --no-pager` index-0 / current |
| `scope` | `--user` and/or system `-b` (name which) |
| `class_counts` | see §3 |
| `sample_lines` | up to N exemplar lines per class (truncated) |
| `journal_rc` | rc of journalctl (0 ok; 1 no-match for --grep; other → unreadable) |
| `finding_ids` | `MORI-KJ-…` |

Exact greps (gate-owned; keep stable):

```
# class KJ1 — kernel/user OOM kill family
journalctl --user -b --no-pager -o short-iso | grep -E 'oom-kill|Out of memory|Killed process|kernel OOM killer'

# class KJ2 — killed-by-signal / unit kill result
journalctl --user -b --no-pager -o short-iso | grep -E "Failed with result|status=9/KILL|status=SIGKILL"

# class KJ3 — segfault / SIGSEGV
journalctl --user -b --no-pager -o short-iso | grep -E 'segfault|SIGSEGV'

# class KJ4 — unit failure (broad; may overlap KJ2)
journalctl --user -b --no-pager -o short-iso | grep -E "Failed with result|Unit .* failed"
```

Prefer `journalctl --grep=` + `-o json` entry counts when gate wants entry-level discipline (line counts are traps — tsukuroi journal-boot-plane lesson). Record which method.

## 3. Classes

| Code | Name | Notes |
|---|---|---|
| `KJ1` | oom-kill family | includes systemd "kernel OOM killer killed some processes" |
| `KJ2` | killed-by-signal / oom-kill unit result | `Failed with result 'oom-kill'`, status=9 |
| `KJ3` | segfault | |
| `KJ4` | unit-failure (other) | core-dump etc.; do not over-claim as OOM |
| `KJ0` | journal unavailable | binary missing / ACL |

## 4. Stable finding ids

| id | Predicate |
|---|---|
| `MORI-KJ-001` | journalctl unavailable/unreadable |
| `MORI-KJ-010` | KJ1 count > 0 this boot |
| `MORI-KJ-020` | KJ2 count > 0 this boot |
| `MORI-KJ-030` | KJ3 count > 0 this boot |
| `MORI-KJ-040` | KJ4 count > 0 (informational) |
| `MORI-KJ-050` | cross-ref: KJ hit without matching cgroup oom_kill flag (or reverse) — unknown until both planes read |

## 5. Boundary vs tsukuroi

Deep dump parsing, victim RSS tables, driver/firmware causation → tsukuroi oom-event-plane. mori records **class + timestamp + boot id + unit name shape** for fleet liveness. Does not install earlyoom, does not reset units.

## 6. Calibration note (R1)

Boot `d7f0bc8d-…`; example KJ2 line at 2026-10-13T23:44:31-03:00 `Failed with result 'oom-kill'`. Re-count on land. **[observed]**
```

---

### 7.4 `corpus/knowledge/cgroup-memory.md`

```markdown
# Cgroup memory plane — memory.events / current / pressure (MORI-R1)

source: cgroupfs reads under `/sys/fs/cgroup/user.slice/…`, `/proc/pressure/memory`.
verified-at: <parent fills>

## 1. Question

Memory kill flags + runway pressure for the user/fleet slice (SKILL rows 3–4 memory half).

## 2. Source lines each row MUST carry

| Field | Source path / command |
|---|---|
| `measured_at` | date -u |
| `uid` | `id -u` |
| `slice_path` | `/sys/fs/cgroup/user.slice/user-<uid>.slice` |
| `service_path` | `…/user@<uid>.service` if readable |
| `memory.events` | `cat <path>/memory.events` → low,high,max,oom,oom_kill,oom_group_kill,sock_throttled |
| `memory.events.local` | `cat …/memory.events.local` |
| `memory.current` | cat |
| `memory.max` | cat (`max` means unlimited) |
| `memory.high` | cat if present |
| `memory.peak` | cat if present — **lifetime max, not datable kill** |
| `memory.swap.current` | cat |
| `memory.swap.events` | cat (fail/high/max) |
| `memory.pressure` | cat (PSI some/full avg10/60/300/total) |
| `proc_pressure_memory` | `cat /proc/pressure/memory` |
| `oom_group` | `cat memory.oom.group` |
| `readable` | per-file success/errno |
| `finding_ids` | `MORI-CG-…` |

Fleet-relevant extra paths (if present; else `unavailable` per path): cgroups of known driver pids via `/proc/<pid>/cgroup`.

## 3. Reading rules (calibration traps)

1. `oom_kill` is a **presence flag / monotonic counter**, not "number of kills this hour".
2. `memory.peak` / `swap.peak` are not timestamps.
3. Missing file → `unavailable` for that field; do not invent zeros.
4. Non-root may read user slice; other scopes may be blocked → record errno.

## 4. Stable finding ids

| id | Predicate |
|---|---|
| `MORI-CG-001` | user slice path unavailable |
| `MORI-CG-010` | `oom_kill` > 0 on slice `memory.events` |
| `MORI-CG-011` | `oom` > 0 (OOM events without kill distinction) |
| `MORI-CG-012` | `oom_group_kill` > 0 |
| `MORI-CG-020` | swap.events `fail` > 0 (pressure signal) |
| `MORI-CG-030` | PSI full avg300 over soft threshold (gate-defined) |
| `MORI-CG-040` | memory.current / memory.max ratio over soft threshold when max ≠ max |

## 5. Boundary

Report only. No `echo` to cgroup files, no oom_score_adj writes, no kills.
OS-plane deep analysis → tsukuroi; mori keeps fleet-runway grain.

## 6. Calibration note (R1)

user-1000.slice: `oom_kill 1`, `memory.current≈24GB`, `swap.current≈9GB`, `swap.fail≈5.9e6`, PSI full avg300=0.00 at measure. **[observed]**
```

---

### 7.5 `corpus/knowledge/disk-runway.md`

```markdown
# Disk runway plane — fleet + scratch roots (MORI-R1)

source: `df -hP` / `df -B1 -P`, `statvfs` equivalent; path existence tests.
verified-at: <parent fills>

## 1. Question

Is there disk runway on fleet and scratch roots? (SKILL.md row 4 disk half)

## 2. Source lines each root MUST carry

| Field | Source |
|---|---|
| `measured_at` | date -u |
| `root` | path requested |
| `exists` | `test -e` / `test -d` |
| `df_ok` | df exit code |
| `filesystem` | df column 1 |
| `size_bytes` | `df -B1` size |
| `used_bytes` | |
| `avail_bytes` | |
| `use_pct` | Capacity column |
| `mounted_on` | |
| `state` | `ok` \| `unavailable` \| `full-soft` \| `full-hard` (gate thresholds) |
| `finding_id` | |

## 3. Default roots (probe list)

| Root | Role |
|---|---|
| `$FLEET_ROOT` (e.g. `/home/vgpnk/Projects/shokunin`) | fleet tree |
| `/` | root fs |
| `/home` | home (may alias same device) |
| `/tmp` | scratch tmpfs |
| `/var/tmp` | durable tmp |
| `/scratch/tmp` | optional scratch — **absent → unavailable, not unhealthy** |

Gate MAY accept env `MORI_DF_ROOTS` override for fixtures.

## 4. Stable finding ids

| id | Predicate |
|---|---|
| `MORI-DK-001` | df binary missing |
| `MORI-DK-010` | root unavailable (ENOENT) |
| `MORI-DK-020` | use_pct ≥ soft threshold (default 90, gate-pinned) |
| `MORI-DK-021` | use_pct ≥ hard threshold (default 95) |
| `MORI-DK-030` | avail_bytes under soft byte floor |

## 5. Boundary

Never delete, truncate, docker-prune, or journal-vacuum. Missing scratch is not a defect.

## 6. Calibration note (R1)

`/` 10% used ~835G avail; `/tmp` tmpfs 60% ~6.1G avail; `/scratch/tmp` unavailable. **[observed]**
```

---

### 7.6 `corpus/knowledge/lane-silence.md`

```markdown
# Lane silence plane — silent / progressing / progressing-weak (MORI-R1)

source: `MANIFEST.json` roster ∪ on-disk lane repos, `git log` / `git show`,
`find -newermt`, report paths under `.ufo/reports/`.
Authority for grades: fleet protocol stale-lane actuator
(`.ufo/waves/round-13/PROTOCOL.compact.md:127-133`), not commit sparsity folklore.
verified-at: <parent fills>

## 1. Question

Was a lane silent? (SKILL.md row 5) — commit sparsity is normal; sparsity ≠ silence.

## 2. Source lines each lane row MUST carry

| Field | Source |
|---|---|
| `measured_at` | date -u |
| `lane_id` | MANIFEST `roster[].id` or dirname stem |
| `repo_path` | `roster[].repo` resolved under fleet root / adjacent path |
| `in_manifest` | yes/no |
| `repo_exists` | test -d |
| `head_sha` | `git -C <repo> rev-parse HEAD` |
| `head_author` | `git log -1 --format='%an <%ae>'` |
| `head_committer` | `git log -1 --format='%cn <%ce>'` |
| `head_date` | `git log -1 --format='%cI'` |
| `lane_identity_match` | author/committer == `<lane>-shokunin <lane>@shokunin.local` (or roster rule) |
| `window_start` | launch timestamp if known; else census window / last report mtime |
| `lane_commits_in_window` | `git log --since=<ts> --format=…` filtered to lane identity |
| `sibling_commits_in_window` | commits in repo by other `-shokunin` / aggregator / operator identities |
| `files_newermt` | `find <repo> -newermt <ts> -type f -not -path '*/.git/*'` count + sample |
| `newest_file_mtime` | max mtime non-git |
| `report_path` | `.ufo/reports/round-*/<lane>.md` if applicable |
| `report_mtime` | stat if present |
| `grade` | `progressing` \| `progressing-weak` \| `silent` \| `unavailable` |
| `finding_id` | |

## 3. Grade rules (protocol)

| Grade | Rule |
|---|---|
| `progressing` | lane-authored commit in window **or** files modified under repo attributable to lane work |
| `progressing-weak` | **only** sibling/aggregator/operator-authored activity in window — named as such; never called progressing; never silent/failed alone |
| `silent` | neither lane activity nor sibling activity in window |
| `unavailable` | repo missing, git unreadable, or window undefined |

**Anti-rules:**

- Absence of commits alone must **not** trigger failed/silent if protocol window not exceeded / if sibling activity exists.
- mori **reports** grade; integrator ledger `failed` is not mori's act.
- Probation lanes (e.g. mori) may be on-disk without MANIFEST row — list under `in_manifest=no`, still grade if repo exists.

## 4. Stable finding ids

| id | Predicate |
|---|---|
| `MORI-LS-001` | MANIFEST unreadable |
| `MORI-LS-010` | lane repo unavailable |
| `MORI-LS-020` | grade=silent |
| `MORI-LS-021` | grade=progressing-weak (informational compare key) |
| `MORI-LS-030` | HEAD author is operator identity while files changing (identity drift signal) |
| `MORI-LS-040` | roster id without on-disk repo (or reverse: on-disk shokunin dir not in roster) |

## 5. Boundary

Does not steer, respawn, or close missions (kumitate/driver). Does not rewrite reports.

## 6. Calibration note (R1)

MANIFEST roster 13; on-disk `*-shokunin` 19; mori on disk + mint HEAD lane-identity, not in roster (probation). **[observed]** Full per-lane table is LaneSilence seat's product; this note owns the rubric.
```

---

## 8. Draft `corpus/README.md` rows (parent lands)

Replace the empty coverage map with:

```markdown
# mori-shokunin — corpus

## Coverage map

| Note | Holds | Sources |
|---|---|---|
| `knowledge/watchdog-liveness.md` | Fleet driver liveness: pid/start/etime, `.ufo/watchdog.log` mtime/age/last tick class, `.ufo/state/*` mission+round counters, false-friend pid exclusion (Hyprland watchdog-fd, kernel watchdogd, ufo_sighting). States `live`/`stale`/`absent`/`unavailable`. Finding ids `MORI-WD-*`. | `ps`/`pgrep`/`stat`/`wc`/`tail`/`tmux ls`; SKILL.md row 1; PROVINCE owns-list |
| `knowledge/wave-settlement.md` | Per-dir settlement enum `settled` / `dispatched-but-unsettled` / `incomplete-shape` over `.ufo/waves/*`; registry+dispatch+results shape; newest-file age; never grades unsettled as failed. Ids `MORI-WV-*`. | directory inventory + JSON key shape; SKILL.md row 2 |
| `knowledge/kill-events-journal.md` | This-boot kill/OOM/segfault/unit-failure classes from `journalctl --user -b` (+ optional `-k`); boot id; entry-vs-line count discipline; exemplars shape-only. Ids `MORI-KJ-*`. | `journalctl`; SKILL.md row 3; adjacent tsukuroi oom-event-plane (not absorbed) |
| `knowledge/cgroup-memory.md` | user slice `memory.events`/`events.local`/`current`/`max`/`swap.*`/`pressure` + `/proc/pressure/memory`; oom_kill as presence flag; errno→unavailable. Ids `MORI-CG-*`. | cgroupfs + proc; SKILL.md rows 3–4 |
| `knowledge/disk-runway.md` | df runway for fleet root, `/`, `/home`, `/tmp`, `/var/tmp`, optional `/scratch/tmp`; missing root = unavailable. Ids `MORI-DK-*`. | `df -hP`/`df -B1 -P`; SKILL.md row 4 |
| `knowledge/lane-silence.md` | Grades `silent` / `progressing` / `progressing-weak` from HEAD identity, window commits, `find -newermt`, report mtime; protocol actuator authority; roster vs on-disk delta. Ids `MORI-LS-*`. | `git` + `find` + MANIFEST.json; SKILL.md row 5; PROTOCOL.compact.md:127-133 |
| `../tools/mori-census.sh` (parent/GateDesign) | Read-only census gate over the six surfaces; `MORI_CENSUS: CLEAN\|DRIFT`; exit 0/1/2; `--selftest` hermetic fixtures; never remediates. | SKILL.md Gates; wave contract |

## Known gaps

- Notes and gate not yet landed at CorpusMap draft time (probation round 1 opens the map).
- Soft/hard thresholds (tick staleness, disk %, PSI, unsettled age) are gate-pinned constants — record defaults in the gate header when landed; notes stay threshold-agnostic except by reference.
- Full live per-lane silence table and full per-wave age table are sibling scout products; notes define schema + ids for compare.
- Historical operator webbridge OOM (demand doc) is not a live journal row until re-observed; do not freeze it as current evidence.
- mori not on MANIFEST roster yet (probation ≥3 rounds); silence plane must still accept on-disk-only lanes.
- Credential paths appear only as shape refusals.

## Quality bar

See `QUALITY.md` (falsifiable, source-cited; observation/inference/unknown split; append-only errata; rejections kept).
```

---

## 9. Operability checklist for parent land

When landing, parent SHOULD:

1. Write six knowledge files + README rows exactly once (no duplicate families).
2. Point `SKILL.md` Gates + checklist at the same finding-id prefixes.
3. Ensure `tools/mori-census.sh` arms emit the six family headers and only the vocabulary in §6.
4. Add hermetic fixtures: fake watchdog.log, state/, waves/{settled,unsettled,incomplete}, cgroup text files, df stub, fake git repos for silence grades — **FixtureDesign**.
5. LOG.md append: "round 1: corpus map opened (6 surfaces)".
6. Keep tsukuroi/kama/kumitate boundaries quoted in each note §Boundary.

---

## 10. Findings (map-level, this seat)

| id | Kind | Statement |
|---|---|---|
| `MORI-MAP-001` | **[observed]** | `corpus/README.md` still `(none yet)`; `knowledge/` only `.gitkeep` at draft time. |
| `MORI-MAP-002` | **[observed]** | Six SKILL surfaces have no knowledge notes yet — this draft supplies them. |
| `MORI-MAP-003` | **[observed]** | Live host shows fleetside driver **absent/stale** (WD calibration), cgroup `oom_kill=1` (CG), `/scratch/tmp` **unavailable** (DK), waves mixed settlement (WV). |
| `MORI-MAP-004` | **[inference]** | Gate selftest MUST fixture stale-log + missing-scratch + oom_kill flag so CLEAN/DRIFT does not depend on live host luck. |
| `MORI-MAP-005` | **[unknown]** | Exact settled-file predicate for 12h waves (`task-response.json` vs `results.json` vs member count) — GateDesign owns final rule; wave note allows both shapes. |

---

## 11. Artifact paths

| Artifact | Path |
|---|---|
| This advisory report | `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p4-mori-r1/members/CorpusMap.md` |
| Lane corpus (unlanded targets) | `/home/vgpnk/Projects/shokunin/mori-shokunin/corpus/knowledge/{watchdog-liveness,wave-settlement,kill-events-journal,cgroup-memory,disk-runway,lane-silence}.md` |
| Lane README (unlanded) | `/home/vgpnk/Projects/shokunin/mori-shokunin/corpus/README.md` |
| Contracts cited | `mori-shokunin/{SKILL,PROVINCE,MINT,QUALITY}.md`; `.ufo/waves/round-13/PROTOCOL.compact.md:127-133`; tsukuroi `oom-event-plane.md` (adjacent) |
| Demand evidence (not live proof) | `.ufo/scopes/shokunin-12h-20261014/operator-demand.md` |

---

## 12. Limits

- Single measure window (~1 min); counters drift.
- Kill class counts intentionally not frozen here (KillEventsJournal owns the full grep table).
- Settlement classifier used for calibration is a sketch; GateDesign may tighten file predicates without changing the three-way enum.
- No native judge verdict is claimed.
- Read-only guarantee: no host mutation beyond creating this members report path.

---

**End of advisory report.** Parent integrates corpus notes, gate, SCORECARD/LOG, and round report.
