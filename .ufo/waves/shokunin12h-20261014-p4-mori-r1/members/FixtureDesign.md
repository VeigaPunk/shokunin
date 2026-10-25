# FixtureDesign — `tools/mori-census.sh --selftest`

**Role:** executor (leaf) · **Wave:** shokunin12h-20261014-p4-mori-r1 · **Lane:** mori-shokunin  
**Axes:** coverage · operability · calibration  
**Scope:** design only. Parent lands the gate; this report is the fixture contract GateDesign / the landed script must satisfy.  
**Hard rule:** every selftest case runs over a temp tree. No live host path, journal, cgroup, `ps`, or `df` is read while `--selftest` is active.

---

## 1. Axes (what these fixtures buy)

| Axis | How the fixture set moves it |
|---|---|
| **coverage** | ≥1 FIRE + ≥1 MUST-NOT-FIRE case per surface family (watchdog, waves, kill journal, cgroup memory, disk runway, lane silence), plus control / setup / unavailable arms |
| **operability** | Cases are mktemp trees + env overrides only; a cold agent re-runs `bash tools/mori-census.sh --selftest` with no oral context and no host privileges beyond `/tmp` |
| **calibration** | Every case pins **exit code** and a **stable finding id** (or the explicit absence of any finding id on CLEAN). Thresholds used in fixtures are named constants the gate must honour, not decorative |

---

## 2. Gate contract the fixtures assume

Aligned with `mori-shokunin/SKILL.md` Gates and the GateDesign brief:

| Mode | Verdict line | Exit |
|---|---|---|
| live / fixture verify | `MORI_CENSUS: CLEAN (…)` | **0** — zero firing findings |
| live / fixture verify | `MORI_CENSUS: DRIFT (findings=N …)` | **1** — one or more firing findings; each finding printed as `FINDING <ID> …` |
| usage / broken fixture root | `MORI_CENSUS: SETUP …` | **2** |
| `--selftest` rollup | `MORI_CENSUS_SELFTEST: PASS (N cases)` / `FAIL (fail/N)` | **0** / **1** |

Finding lines (stable, comparable across runs):

```text
FINDING <ID> severity=<sev> surface=<family> obs=<short-observation>
```

Selftest assertion primitive (implement exactly this shape):

```bash
# run_case NAME WANT_EXIT WANT_ID_OR_CLEAN
# WANT_ID_OR_CLEAN is either a finding id that MUST appear, or the token CLEAN
# meaning: exit 0, verdict CLEAN, and zero FINDING lines.
run_case() {
  local name=$1 want_rc=$2 want=$3 out rc
  out=$(MORI_FIXTURE="$FX" MORI_MODE=fixture "$GATE" 2>&1) && rc=0 || rc=$?
  cases=$((cases + 1))
  if [ "$rc" -ne "$want_rc" ]; then
    bad "$name: exit $rc want $want_rc"
  elif [ "$want" = CLEAN ]; then
    printf '%s\n' "$out" | grep -q '^MORI_CENSUS: CLEAN' \
      || bad "$name: missing CLEAN verdict"
    printf '%s\n' "$out" | grep -q '^FINDING ' \
      && bad "$name: unexpected FINDING on CLEAN"
  else
    printf '%s\n' "$out" | grep -q "^FINDING ${want} " \
      || bad "$name: missing FINDING $want"
    printf '%s\n' "$out" | grep -q '^MORI_CENSUS: DRIFT' \
      || bad "$name: missing DRIFT verdict"
  fi
}
```

**Idempotence pin (shared with CensusIdempotence):** after every case, `find "$FX" -type f -exec sha256sum {} \; | sort | sha256sum` must equal the pre-run digest. Selftest fails closed if the census mutates the fixture.

---

## 3. Finding-id vocabulary the fixtures pin

Stable ids (FindingIds is the prose owner; fixtures are the machine pin). Severity: `info` does not flip CLEAN→DRIFT; `warn`/`crit` do.

| ID | Surface | Severity | Fires when (observation) |
|---|---|---|---|
| `WATCHDOG_ABSENT` | watchdog | crit | no watchdog pid file / pid not alive under fixture `proc` |
| `WATCHDOG_STALE_LOG` | watchdog | warn | `watchdog.log` mtime age > `MORI_WATCHDOG_LOG_MAX_AGE_S` (default **3600**) |
| `WATCHDOG_WEDGED` | watchdog | warn | pid alive but last tick / log age > `MORI_WATCHDOG_TICK_MAX_AGE_S` (default **1800**) |
| `WATCHDOG_COUNTER_DRIFT` | watchdog | warn | `.ufo/state/<lane>.round` disagrees with log dispatch/complete counts beyond tolerance 0 |
| `WAVE_UNSETTLED_AGE` | waves | warn | wave has `swarm-registry.json` (or dispatch/run payload) and **no** results payload, and newest file age > `MORI_WAVE_UNSETTLED_MAX_AGE_S` (default **86400**) |
| `WAVE_ORPHAN_RESULTS` | waves | info | results present without registry — reported, does **not** alone force DRIFT |
| `OOM_KILL_EVENT` | kill-journal | crit | journal fixture line matches OOM-kill class |
| `SIGKILL_EVENT` | kill-journal | warn | `status=9/KILL` / killed-by-signal class |
| `SEGFAULT_EVENT` | kill-journal | warn | segfault / SIGSEGV class |
| `UNIT_FAILURE_EVENT` | kill-journal | warn | unit-failure class line |
| `CGROUP_OOM_KILL` | cgroup | crit | `memory.events` has `oom_kill` **> 0** (presence flag; value is evidence, not a rate) |
| `CGROUP_MEMORY_HIGH` | cgroup | warn | `memory.events` `high` or `max` > 0, or `memory.current` / `memory.max` ≥ `MORI_MEM_HIGH_RATIO` (default **0.90**) when max is numeric |
| `CGROUP_UNAVAILABLE` | cgroup | info | cgroup path missing/unreadable → surface `unavailable`, **not** unhealthy; does **not** force DRIFT |
| `DISK_LOW` | disk | warn | capacity % ≥ `MORI_DISK_WARN_PCT` (default **85**) and < crit |
| `DISK_CRITICAL` | disk | crit | capacity % ≥ `MORI_DISK_CRIT_PCT` (default **95**) |
| `DISK_UNAVAILABLE` | disk | info | configured root missing → `unavailable`; does **not** force DRIFT |
| `LANE_SILENT` | silence | warn | rostered lane: HEAD commit time **and** newest non-`.git` mtime both older than newest report mtime by > `MORI_LANE_SILENCE_S` (default **172800**) with no sibling-authored progress marker |
| `LANE_PROGRESSING_WEAK` | silence | info | only sibling-authored commit activity; **not** a DRIFT finder by itself |

**Unavailable ≠ unhealthy:** fixtures below that mark a surface missing must assert **no** `*_LOW` / `*_ABSENT`-as-failure id for that surface, and must keep exit **0** unless another surface fires.

---

## 4. Hermetic layout

Selftest root (only writable location):

```text
$WORK = mktemp -d /tmp/mori-census-selftest.XXXXXX
$WORK/bin/          # stub binaries on PATH: ps, journalctl, df, statvfs-helper (optional), tmux
$WORK/fx/<case>/    # per-case fixture tree
```

Per-case tree (`$FX`) — fleet root override via `MORI_FLEET_ROOT=$FX`:

```text
$FX/
  proc/                         # fake /proc: $FX/proc/<pid>/{comm,cmdline,stat}
  cgroup/
    user.slice/
      memory.events
      memory.current
      memory.max
      user-1000.slice/
        memory.events
        memory.current
        memory.max
  journal/
    user-boot.txt               # lines journalctl stub emits for --user -b
  disk/
    fleet.df                    # one `df -P` table the df stub prints
    tmp.df
    scratch.df                  # optional; absent → DISK_UNAVAILABLE path
  fleet/                        # stands in for the shokunin checkout
    .ufo/
      watchdog.log
      watchdog.pid              # optional convenience; ps stub is source of truth
      state/
        kagi.round
        kumitate.round
        …
      waves/
        wave-settled/
          swarm-registry.json
          run.json
          task-response.json    # results-class payload
        wave-unsettled/
          swarm-registry.json
          run.json
          # no results
      reports/
        round-N/
          kagi.md
          …
    lanes/                      # minimal fake lane repos for silence grading
      kagi-shokunin/
        .git/                   # or a `HEAD_TIMESTAMP` file the gate reads under fixture mode
        SKILL.md
      silent-shokunin/
        .git/
        SKILL.md
```

**Env overrides (complete set — if live mode reads it, fixture mode overrides it):**

| Env | Replaces |
|---|---|
| `MORI_FLEET_ROOT` | shokunin checkout root (`.ufo/…`) |
| `MORI_PROC_ROOT` | `/proc` |
| `MORI_CGROUP_ROOT` | `/sys/fs/cgroup` |
| `MORI_JOURNAL_FILE` | path the journalctl stub cats (or `MORI_JOURNALCTL=$WORK/bin/journalctl`) |
| `MORI_DF_CMD` / `MORI_DF_TABLE_DIR` | `df` binary or dir of per-target tables |
| `MORI_PS_CMD` | `ps` stub |
| `MORI_NOW_EPOCH` | frozen clock for age math (required in selftest; kills nondeterminism) |
| `MORI_WATCHDOG_LOG_MAX_AGE_S` | stale-log threshold |
| `MORI_WATCHDOG_TICK_MAX_AGE_S` | wedged threshold |
| `MORI_WAVE_UNSETTLED_MAX_AGE_S` | unsettled-wave age |
| `MORI_DISK_WARN_PCT` / `MORI_DISK_CRIT_PCT` | disk thresholds |
| `MORI_MEM_HIGH_RATIO` | cgroup high ratio |
| `MORI_LANE_SILENCE_S` | silence window |
| `MORI_ROSTER` | space-separated lane ids for silence/counter cases |
| `MORI_WATCHDOG_COMM` | expected comm/cmdline match (default `watchdogd` / `shokunin-watchdog`) |

Frozen clock for all cases unless noted: **`MORI_NOW_EPOCH=1760472000`** (2025-10-14T20:00:00Z — arbitrary fixed pin; gate must not call `date` without honouring this).

---

## 5. Fixture builders (shared helpers)

```text
fx_clean(FX)     → full healthy tree (see §6 control)
fx_touch_age(PATH, AGE_S) → mtime = MORI_NOW_EPOCH - AGE_S  (touch -d @…)
fx_journal_line(CLASS, TEXT) → append classified line to journal/user-boot.txt
fx_df_row(FILE, FSTYPE, SIZE, USED, AVAIL, PCT, TARGET) → one df -P data row
fx_cgroup_events(PATH, oom=0, oom_kill=0, high=0, max=0)
fx_wave_settled(NAME) / fx_wave_unsettled(NAME, AGE_S)
fx_lane(NAME, HEAD_AGE_S, FILE_AGE_S, REPORT_AGE_S, author=self|sibling)
```

`fx_clean` baseline (MUST-NOT-FIRE substrate every FIRE case starts from, then mutates one axis):

- `proc/4242/comm` = `watchdogd`; pid listed by ps stub
- `watchdog.log` mtime age 60s; contains one `launch` and one `complete` line per roster lane
- `state/<lane>.round` = `16` matching log completes
- one settled wave; zero unsettled
- journal empty (or only non-class noise)
- cgroup `oom_kill 0`, `high 0`, `max 0`; `current=1_000_000_000`, `max=10_000_000_000`
- df fleet 10%, tmp 40%; scratch present 20%
- every roster lane `progressing` (HEAD age 1h, file age 1h, report age 2h)

---

## 6. Case table

**Legend:** FIRE = must produce DRIFT exit 1 + named id. QUIET = must produce CLEAN exit 0 and **must not** emit that surface’s fire ids. SETUP = exit 2.

Minimum required by the brief is covered; extras calibrate unavailable/ wedged/ counters.

### 6.0 Control & setup

| # | case id | expect exit | expect id / CLEAN | Fixture mutation from `fx_clean` |
|---|---|---|---|---|
| 0 | `control-clean` | 0 | CLEAN | none |
| 0b | `setup-no-fleet-root` | 2 | *(no FINDING; SETUP line)* | unset `MORI_FLEET_ROOT` / point at missing path |
| 0c | `setup-bad-flag` | 2 | SETUP | invoke gate with `--not-a-flag` (no fixture read) |

### 6.1 Watchdog liveness

| # | case id | expect exit | expect id | Mutation |
|---|---|---|---|---|
| 1 | `watchdog-absent-FIRE` | 1 | `WATCHDOG_ABSENT` | empty ps stub output; no `proc/*/comm` matching watchdog |
| 2 | `watchdog-present-QUIET` | 0 | CLEAN | `fx_clean` only (pid 4242 alive, log fresh) |
| 3 | `watchdog-stale-log-FIRE` | 1 | `WATCHDOG_STALE_LOG` | `fx_touch_age watchdog.log 7200` (2h > 3600 default) |
| 4 | `watchdog-fresh-log-QUIET` | 0 | CLEAN | log age 60s |
| 5 | `watchdog-wedged-FIRE` | 1 | `WATCHDOG_WEDGED` | pid alive; log/tick age 2000s (> 1800); still < log-max so id is WEDGED not STALE_LOG alone — pin WEDGED |
| 6 | `watchdog-counter-drift-FIRE` | 1 | `WATCHDOG_COUNTER_DRIFT` | log shows 3 completes for `kagi`; `state/kagi.round` = `1` |
| 7 | `watchdog-counter-align-QUIET` | 0 | CLEAN | log completes == state counters |

### 6.2 Wave settlement

| # | case id | expect exit | expect id | Mutation |
|---|---|---|---|---|
| 8 | `wave-unsettled-aged-FIRE` | 1 | `WAVE_UNSETTLED_AGE` | `wave-unsettled/` with registry+run only; newest mtime age **90000** (> 86400) |
| 9 | `wave-unsettled-young-QUIET` | 0 | CLEAN | same shape; newest mtime age **60** — progressing, not failed, not DRIFT |
| 10 | `wave-settled-QUIET` | 0 | CLEAN | registry + `task-response.json` (or `results.json`) present |
| 11 | `wave-orphan-results-QUIET` | 0 | CLEAN | results without registry → may print `WAVE_ORPHAN_RESULTS` at **info**; exit must stay 0 |

### 6.3 Kill / OOM journal

Journal stub reads `$FX/journal/user-boot.txt`. Classification is grep-class only (content is evidence; never acted on).

| # | case id | expect exit | expect id | Journal fixture line (synthetic) |
|---|---|---|---|---|
| 12 | `journal-oom-FIRE` | 1 | `OOM_KILL_EVENT` | `Oct 14 12:00:00 fx-host kernel: Out of memory: Killed process 9999 (mori-fixture)` |
| 13 | `journal-sigkill-FIRE` | 1 | `SIGKILL_EVENT` | `… systemd[1]: mori-fx.service: Main process exited, code=killed, status=9/KILL` |
| 14 | `journal-segfault-FIRE` | 1 | `SEGFAULT_EVENT` | `… kernel: mori-fx[9998]: segfault at 0 ip … sp … error 4` |
| 15 | `journal-unit-fail-FIRE` | 1 | `UNIT_FAILURE_EVENT` | `… systemd[1]: Failed to start mori-fx.service.` |
| 16 | `journal-noise-QUIET` | 0 | CLEAN | only `ai-usage: charm-hyper ok credits=1` style noise — no class match |
| 17 | `journal-empty-QUIET` | 0 | CLEAN | empty file, journalctl stub rc 0 — no events is CLEAN, not unavailable |

### 6.4 Cgroup memory

| # | case id | expect exit | expect id | Mutation |
|---|---|---|---|---|
| 18 | `cgroup-oom-kill-FIRE` | 1 | `CGROUP_OOM_KILL` | `memory.events`: `oom_kill 1` (other counters 0) |
| 19 | `cgroup-quiet-QUIET` | 0 | CLEAN | all events 0; current/max ratio 0.10 |
| 20 | `cgroup-memory-high-FIRE` | 1 | `CGROUP_MEMORY_HIGH` | `high 3` **or** current/max = 0.95 |
| 21 | `cgroup-missing-QUIET` | 0 | CLEAN | `MORI_CGROUP_ROOT` points at absent dir → surface `unavailable`; **must not** emit `CGROUP_OOM_KILL` / `CGROUP_MEMORY_HIGH` |

### 6.5 Disk runway

`df -P` shaped tables (1024-blocks). Gate parses Capacity % and target.

| # | case id | expect exit | expect id | df Capacity |
|---|---|---|---|---|
| 22 | `disk-critical-FIRE` | 1 | `DISK_CRITICAL` | fleet row **96%** |
| 23 | `disk-low-FIRE` | 1 | `DISK_LOW` | fleet row **90%** (warn band; not crit) |
| 24 | `disk-ok-QUIET` | 0 | CLEAN | fleet 10%, tmp 40%, scratch 20% |
| 25 | `disk-scratch-missing-QUIET` | 0 | CLEAN | no scratch table / path → `DISK_UNAVAILABLE` info only; exit 0 |
| 26 | `disk-tmp-critical-FIRE` | 1 | `DISK_CRITICAL` | tmp **97%**, fleet ok — any configured root may fire |

Synthetic full-disk row example:

```text
Filesystem 1024-blocks Used Available Capacity Mounted on
tmpfs 1048576 1048576 0 100% /fx/tmp
```

(Use 96%/90% in cases 22–23 so threshold boundaries stay testable without relying on 100% edge parsing.)

### 6.6 Lane silence

Roster under fixture: `kagi kumitate silent` via `MORI_ROSTER`.

| # | case id | expect exit | expect id | Mutation |
|---|---|---|---|---|
| 27 | `lane-silent-FIRE` | 1 | `LANE_SILENT` | `silent-shokunin`: HEAD age 10d, newest file age 10d, report mtime age 1d (report newer than work → silent) |
| 28 | `lane-progressing-QUIET` | 0 | CLEAN | HEAD age 1h, file age 1h, report age 2h |
| 29 | `lane-progressing-weak-QUIET` | 0 | CLEAN | HEAD authored by sibling marker file `AUTHOR=sibling`; may emit info `LANE_PROGRESSING_WEAK`; exit 0 |
| 30 | `lane-report-absent-QUIET` | 0 | CLEAN | no report file → silence grade `unavailable` for that lane, not `LANE_SILENT` |

---

## 7. Case count & rollup

| Family | FIRE | QUIET / non-fire | Subtotal |
|---|---:|---:|---:|
| control/setup | 0 | 3 | 3 |
| watchdog | 4 | 3 | 7 |
| waves | 1 | 3 | 4 |
| kill-journal | 4 | 2 | 6 |
| cgroup | 2 | 2 | 4 |
| disk | 3 | 2 | 5 |
| lane silence | 1 | 3 | 4 |
| **Total** | **15** | **18** | **33** |

Brief minimum satisfied: every surface has ≥1 FIRE and ≥1 MUST-NOT-FIRE; explicit synthetic **kill event** (cases 12–15, 18), **stale log** (3), **full/critical disk** (22, 26).

Rollup line:

```text
MORI_CENSUS_SELFTEST: PASS (33 cases)
```

Any `bad` → `FAIL (k/33)` exit 1. Selftest itself must not leak fixture paths into live mode and must `rm -rf "$WORK"` on EXIT.

---

## 8. Stub binary contracts

Minimal `ps` stub (`$WORK/bin/ps`):

- If `$FX/ps.out` exists, cat it and exit 0
- Else synthesize from `$FX/proc/*/comm`: `PID ETIME CMD`

Minimal `journalctl` stub:

- Require `--user` and `-b` in argv (or fixture mode ignores and always cats `$FX/journal/user-boot.txt`)
- Exit rc from `$FX/journal/user-boot.rc` (default 0)
- **Never** read the real journal

Minimal `df` stub:

- Map path args to `$FX/disk/<name>.df` (fleet / tmp / scratch)
- Missing file → exit 1 empty (gate → `DISK_UNAVAILABLE`)

PATH for selftest: `export PATH="$WORK/bin:$PATH"` with stubs only — no fallback to system `journalctl`/`df` if stub missing (fail SETUP).

---

## 9. Multi-finding & ordering pins (calibration)

| # | case id | expect exit | expect ids (all must appear) | Purpose |
|---|---|---|---|---|
| 31 | `multi-fire-order` | 1 | `WATCHDOG_STALE_LOG` + `DISK_LOW` + `OOM_KILL_EVENT` | DRIFT with `findings=3`; ids emitted in **surface order**: watchdog → waves → journal → cgroup → disk → silence |
| 32 | `threshold-honour-disk` | 0 | CLEAN | fleet **84%** with defaults (warn 85) — boundary must not fire |
| 33 | `threshold-honour-disk-env` | 1 | `DISK_LOW` | same 84% row but `MORI_DISK_WARN_PCT=80` — proves threshold is live, not decorative |

(Cases 31–33 fold into the 33-count as the last three calibration arms; if GateDesign prefers a leaner suite, 0–30 are the coverage floor and 31–33 are RECOMMENDED.)

**Counting rule for implementers:** the landed `--selftest` MUST include at least cases **0–30** (31 cases) and SHOULD include **31–33**. Report the exact N in `MORI_CENSUS_SELFTEST: PASS (N cases)` and pin N in SCORECARD.

---

## 10. What selftest MUST NOT do

- Read `/proc`, `/sys/fs/cgroup`, live `.ufo/`, real `journalctl`, real `df`, real lane git repos
- Write outside `$WORK`
- Restart, kill, `systemctl`, `pacman`, dispatch, network fetch
- Content-read credentials, oauth, `server.token`, `op.env`, session payloads (no such files in fixtures; stubs must not open them if present)
- Treat `unavailable` as `DRIFT`
- Treat a young unsettled wave as failed
- Remediate any FIRE observation

---

## 11. Proof commands (for parent / mutation seats)

```bash
# after tools/mori-census.sh lands
bash tools/mori-census.sh --selftest
# expect: MORI_CENSUS_SELFTEST: PASS (N cases)  exit 0

# single-case debug (optional flag GateDesign may add)
MORI_SELFTEST_ONLY=journal-oom-FIRE bash tools/mori-census.sh --selftest
```

Idempotence (CensusIdempotence can reuse):

```bash
# inside one case: digest before == after
```

---

## 12. Hand-off to GateDesign / FindingIds / parent

| Owner | Owes |
|---|---|
| **GateDesign** | implement `tools/mori-census.sh` so cases 0–30 (and ideally 31–33) pass; env override surface complete; FINDING line grammar exact |
| **FindingIds** | prose for each id in §3; keep spellings byte-identical to this table |
| **CorpusMap** | knowledge notes may cite case ids as falsifiers |
| **FalsePositiveAudit** | cases 9, 11, 21, 25, 29, 30 are the deliberate non-fire anchors |
| **Parent** | land script + optional `corpus/fixtures/README.md` pointer; pin selftest N on SCORECARD |

---

## 13. Risks / blockers

| Risk | Mitigation in this design |
|---|---|
| GateDesign picks different id spellings | §3 is the pin; diverge → selftest red |
| Live `date` makes age flaky | `MORI_NOW_EPOCH` required in selftest |
| `df` locale / header variance | fixtures ship full header + one data row; parser accepts `df -P` |
| Sibling GateDesign not landed yet | this report is the contract; no script written here (leaf bounds) |
| Over-long suite | floor = cases 0–30; 31–33 optional calibration |

**Blockers:** none for this seat. No live host dependency; no missing prerequisite beyond parent landing the gate against this table.

---

## 14. Evidence retained (design-time only)

| Fact | Source |
|---|---|
| Surfaces owned | `mori-shokunin/{SKILL,PROVINCE,MINT}.md` |
| Gate exit vocabulary | SKILL.md Gates + wave spec GateDesign item |
| Sibling hermetic pattern | `tsukuroi-shokunin/tools/tsukuroi-census.sh` selftest (dispatcher + fx_default + check exit/verdict); `kagi-shokunin/corpus/{drift-pins,surface-census}.sh` run_case exit+token |
| Brief FIRE examples | wave item FixtureDesign: synthetic kill, stale log, full disk |
| Finding id examples | wave item FindingIds: `WATCHDOG_ABSENT`, `WAVE_UNSETTLED_AGE`, `OOM_KILL_EVENT`, `DISK_LOW`, `LANE_SILENT` |

No live census was required for this design seat; path samples under `.ufo/` informed fixture *shape* only and are not asserted as round evidence here.

---

## 15. Summary

Deliverable: **33-case (31 floor + 3 calibration) hermetic fixture contract** for `tools/mori-census.sh --selftest`, covering all six mori surfaces with paired FIRE / MUST-NOT-FIRE arms, each asserting **exit code + stable finding id**, zero live host reads, zero remediation.
