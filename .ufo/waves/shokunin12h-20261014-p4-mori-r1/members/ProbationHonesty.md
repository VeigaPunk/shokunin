# ProbationHonesty — fabricated and unprovenanced observations

Advisory data. Not a judge verdict. Not a `MORI_CENSUS` banner. Nothing was restarted, killed, deleted, or dispatched. This seat re-read files and ran read-only probes only.

**Audit close:** `2026-10-15T00:41:14Z` (`date -u` / `date -Is` → `2026-10-14T21:41:14-03:00`).
**Rule applied:** a claimed observation needs both a command and the timestamp measured. A design predicate, a proposal, or a sentence marked inference is not an observation. A file-level clock does not cover a row that names neither command nor clock. Event time inside a log line is not the measurement time.

**Set read:** the 24 member files on disk at close (`BoundaryRefusal`, `CensusIdempotence`, `CgroupMemoryEvents`, `CorpusMap`, `CounterVsLog`, `CrossDomainBoundary`, `DiskRunway`, `FalsePositiveAudit`, `FindingIds`, `FixtureDesign`, `GateDesign`, `GateRegistryRow`, `KillEventsJournal`, `LiveReceipt`, `MemoryPressureReading`, `OwnerMap`, `ReportShape`, `RerunStability`, `StateCounterAudit`, `WatchdogLiveness`, `WatchdogLogGrammar`, `WaveAgeMath`, `WaveResultJoin`, `WaveSettlement`), plus landed `mori-shokunin/{LOG,SCORECARD,corpus/README}.md`, `corpus/knowledge/observability-census-r1.md`, and `tools/mori-census.sh` blobs `8693b180` (`72da7cd`) and `43a2f5f8` (`486a4e3`). Reports written after this close are outside the set.

## Counterexample

Five claims are not reusable observations. Each is either false against a file that already existed at the claimed clock, or pinned to the wrong identity, or a number with no command.

1. **CorpusMap §5.2 settlement sketch has no command, and it is false at its own window.** Window `2026-10-15T00:28:35Z`–`00:29:28Z`. The row says train `w6`–`w10` / `w12`–`w14` are `settled`, and all `shokunin12h-*` are `dispatched-but-unsettled` or `incomplete-shape`. No `find`/`ls` is named. At that window `shokunin12h-20261014-p1-repair/results.json` already existed (WaveResultJoin `stat -c %y` → `2026-10-14 21:10:26 -0300`, before the window). Re-list at `2026-10-15T00:37:58Z`: `w6`–`w10` have `closeout.json` not `results.json`; `w12`–`w14` have `closeout.md` + `registry.json`, not `swarm-registry.json`; `w11` has `closeout.json` and is omitted from the "settled" set. One sketch, two predicates, neither commanded.

2. **Landed erratum names the wrong closeout file and the wrong five waves.** `corpus/knowledge/observability-census-r1.md` erratum 2 and `tools/mori-census.sh` (blob `43a2f5f8`, comment above the settle test) say `w5`–`w11` close out with `closeout.md` and/or `"closed": true`, and that a filename-only test aged five settled waves into `WAVE_UNSETTLED_AGE`. No command, date only (`2026-10-15`). On disk at `00:37:58Z`: `w5` has no closeout file (`ADMIT` and `"closed": true` are inside `swarm-registry.json`); `w6`–`w11` have `closeout.json`, not `closeout.md`; `closeout.md` starts at `w12`. The pasted receipt in the same file ages `shokunin-train-20261013` through `w5` (`settle=0`). Of those five, only `w5` has an ADMIT/closed token. `w1`–`w4` have neither closeout nor `"closed": true`. The causal sentence does not match the receipt it sits under.

3. **FindingIds memory anchor has no command, and the unit is wrong.** §3.4: `MemAvailable` ≈ 21.8 GiB / 32.5 GiB total. Provenance §10 does not list a meminfo command. `MemTotal` `31721780` kB (`/proc/meminfo`, re-read `2026-10-15T00:37:58Z`, and LiveReceipt / MemoryPressureReading at `00:31Z`–`00:33Z`) is 30.26 GiB and 32.48 GB. 32.5 "GiB" is decimal GB mislabeled. 21.8 is the same mislabel of ~21.7 GB, not GiB (LiveReceipt `MemAvailable` `21679656960` B ≈ 20.19 GiB at T0).

4. **RerunStability pins the run to the wrong blob.** Header: blob `43a2f5f8` = `HEAD:tools/mori-census.sh` at `72da7cd`, sha256 `7432255f…`, runs at `2026-10-15T00:37:44Z`–`00:37:59Z`, command `bash tools/mori-census.sh`. `git rev-parse 72da7cd:tools/mori-census.sh` is `8693b180`, and that blob's sha256 is `7432255f…`. Blob `43a2f5f8` is a different file (sha256 `bb839ba2…`), introduced by `486a4e3` at `2026-10-14 21:39:09 -0300`, after the claimed window. `8693b180` emits `FINDING CGROUP_OOM_KILL severity=crit obs=oom_kill=$oom_kill … path=$CGROUP_EVENTS`. `43a2f5f8` emits `CGROUP_OOM_KILL_CUMULATIVE` (info) when the service counter is 0. The pasted line is the `8693b180` format. Sha and stdout can belong to `72da7cd`; the blob id cannot. Identity in the header is false.

5. **The gate's own FINDING lines drop command and timestamp, so two segfault counts cannot be compared.** `emit_finding` writes `FINDING $id severity=$sev obs=$obs` with no `cmd=` and no `ts=`. SURFACE lines have both. GateDesign §2 says every SURFACE and FINDING line is one observation. LiveReceipt §2.6 reports 588 system segfault lines and 1044 user cores at T2, but the producing grep is only `# class greps (counts @T2)`. The landed erratum re-measures `grep -ciE 'segfault|general protection fault'` → system **626**, user **0**, and `coredumpctl list` → **1228**, dated `2026-10-15` with no clock. KillEventsJournal, with exact argv and `2026-10-14T21:36:01-03:00`, gets user `COREDUMP_SIGNAL=11` **656** and shows why a MESSAGE grep reads 0. Three counts, one missing argv, one missing clock. Not a contradiction until the command is written down. That is the defect.

## Claims with neither a command nor a usable timestamp

| Where | Claim presented as observed | What is missing |
|---|---|---|
| `CorpusMap.md` §5.1 | last log lines are fleet-wrap + `tick=3` at `2026-09-28T23:55:00-03:00`; 9 state pairs all mtime `2026-10-13 16:44:48`; no driver in `ps`; tmux created `20:14:40`; pids `937995/938031/938122`, kernel `watchdogd` `237`, Hyprland `1203316` | no command on those rows (section clock only). Later seats re-measured several of these with commands; this row still does not |
| `CorpusMap.md` §5.2 | 40 wave dirs; 10 `swarm-registry.json`; settlement sketch above | no command. Counts 40 and 10 matched a later `iterdir` at `00:37:58Z`; the sketch did not |
| `CorpusMap.md` §5.3 | boot id; journal oom/kill "non-zero"; example `Failed with result 'oom-kill'` at `2026-10-13T23:44:31-03:00`; kernel journal "readable" | boot id and the example line have no command. The example time is the event, not the measure. "non-zero" is not a count |
| `CorpusMap.md` §5.4 | full `memory.events` line, `memory.current` `24668520448`, swap, PSI | path is not a command (`cat` is not written). Section clock only |
| `CorpusMap.md` §5.6 | mori HEAD author/date; tsukuroi HEAD date; MANIFEST 13; 19 `*-shokunin` dirs | no `git`/`jq`/`ls` on the rows. 13 and 19 matched a later read; the rows still have no command |
| `FindingIds.md` §3.2–§3.5 | "two wire shapes observed"; train dirs with no `results.json`; `Failed with result 'oom-kill'` @ `2026-10-13T23:44:31-03:00`; pipewire-pulse core-dump @ `2026-10-14T18:54:21-03:00`; `oom_kill 1`; MemAvailable; fleet 10% / 835G; `/tmp` 60%; `/scratch/tmp` absent | §10 covers pgrep, log `stat`, a vague "listing", `df -P` → "10% / 60%", and `test -e`. It does not cover the journal examples, MemAvailable, or 835G. The "at" column says `live`, not a timestamp (header clock is `2026-10-14T21:29:07-03:00` only) |
| `CrossDomainBoundary.md` §1.2 | pasted `oom_kill` 1/0/0 for user slice, `user@1000.service`, and two `tmux-spawn-*.scope` paths; "every active fleet process" has `oom_kill = 0`; "scope exited over 24 hours ago" | no command, no measured-at. The universal fleet claim is not the two scopes pasted. The 24h sentence cites tsukuroi `oom-event-plane.md:28`, not a probe |
| `FalsePositiveAudit.md` FP-4, FP-5, FP-9 | w12 `closeout.md` age 33755 s; w11 36054 s; w1–w5 ages 95414–70557 s; p1-audit newest age 284 s; p4 age ~59 s; p3 age 1121 s; cgroup `oom_kill 1` and MemAvailable `21371900` kB | file clock `2026-10-14T21:40:00-03:00` only. FP-1 has a command table; these anchors do not |
| `LiveReceipt.md` §2.6, §2.10 | class counts 1/1/1/588/1044/2; `docker ps` empty; docker pid `737528` | ledger rows 6/10/13 say "grep oom/core" and "class counts" without the argv. `docker ps` is not in §5 and has no T0/T1/T2 |
| `WaveResultJoin.md` | only one wave has a registry document and `results.json`; train `20261013` through `w10` have registry+dispatch and no results; 32 member mtimes, earliest `KamaGateRepair.md` `20:38:47`, latest `KakeGateRepair.md` `21:02:33`; python 3.14.7 | clock `2026-10-14T21:34:48-03:00` and `stat`/`sha256sum`/`test -e`/`ls -1 \| wc -l` cover four files and a count. They do not cover the fleet walk, the 32 mtimes, or `python3 --version`. "Reads were python3" is not an argv |
| `WaveSettlement.md` §Coverage | `.ufo/scopes` has one entry, `shokunin-12h-20261014` | eight `test -f` calls do not prove cardinality. No `ls`. Not falsified: the other scope dirs' mtimes are `2026-10-14 21:37:10`, after T1 `2026-10-15T00:34:08Z` |
| `LOG.md` round 1, `SCORECARD.md` move log | live `MORI_CENSUS: DRIFT (findings=10 drift=9 unavailable=0 surfaces=7)`; `--selftest` 14/14 PASS; prose `WATCHDOG_STALE age_s=103830`, oldest wave `95445` | command named, no timestamp, no script sha. Pasted receipt in the knowledge file is `ts=2026-10-15T00:35:31Z` with `age_s=103843` and oldest `95458`. Prose numbers are not that receipt and are not a second stamped run. GateRegistryRow at `2026-10-15T00:34:56Z` measured selftest **FAIL 13/14** on sha `dd939ec8…`. A later PASS is a different byte string. The log does not say which |
| `corpus/README.md` known gap; knowledge erratum | user segfault 0, system 626, `coredumpctl` 1228 | grep pattern is named; no clock. `coredumpctl` has no timestamp |
| `tools/mori-census.sh` comments (blobs `43a2f5f8` and later `8dd5c167`) | "Measured 2026-10-15: w5..w11 are closed with ADMIT"; "user@1000.service started 2026-10-14 13:11:07"; "walk of 101 cgroups"; "measured: pipewire-pulse.service core-dump" | comments are not a probe log. 101 cgroups is CgroupMemoryEvents' walk at `2026-10-15T00:33:03Z` (that seat did record the command). The script comment does not cite it |
| `GateDesign.md` header | "Measured: `2026-10-15T00:28:58Z`" | timestamp, no command, no stated observation. Design text below is not a host reading |

`emit_finding` at `mori-census.sh:119-122` (still true on current HEAD `0cdb305`, blob `8dd5c167`) never stamps a finding. A missing `pgrep` emits `WATCHDOG_LOG_UNAVAILABLE` (`:182`) for a missing binary. That id is a false observation the gate will print with no clock.

## Not fabricated (time-scoped; do not "correct" them from a later listing)

- WaveResultJoin `test -e` at `2026-10-14T21:34:48-03:00`: repair scope path absent, parent absent. Those scope directories were created at `21:37:10`. Absence at the earlier clock is not a lie.
- LiveReceipt T2 `2026-10-15T00:33:23Z`: `tools/mori-census.sh` absent, worktree clean, HEAD `27acf40`. BoundaryRefusal at `21:35:01`–`21:35:14` saw an untracked script (sha `32f804a3…`, then a later rewrite). Different clocks, different bytes. Each claim stands only with its clock.
- CensusIdempotence sha `7432255f…` at `21:35:14` matches `72da7cd`'s script, not blob `43a2f5f8`. That sha pin is the one that matches the file. RerunStability reused the sha and attached the wrong blob id.

## Seats whose observations carry command and timestamp

These were read. Their live rows name a command and a clock. They are not cleared of every number; they are not the defect this rule catches.

`DiskRunway` (published `/usr/bin/df` transcript, `2026-10-14T21:34:29-03:00`), `StateCounterAudit` (`2026-10-14T21:35:33-03:00` plus earlier `od`/`sha256sum`), `WatchdogLiveness`, `WatchdogLogGrammar`, `WaveAgeMath` (per-stamp command table), `KillEventsJournal` (exact `journalctl` argv and rc), `CgroupMemoryEvents` (probe log), `BoundaryRefusal` (evidence index), `GateRegistryRow` §6 (selftest transcript at `2026-10-15T00:34:56Z`), `CensusIdempotence`, `CounterVsLog`, `RerunStability` runs A–D (the blob-id sentence excepted), `ReportShape` §2.3.2 (before snapshot; the `MORI_CENSUS: UNAVAILABLE` line is marked not real stdout).

Partial, not a hard miss: `MemoryPressureReading` stamps t0/t1 and names the path (`/proc/meminfo`, `/proc/vmstat`) but calls the read "command-equivalent", not an argv. `systemd-analyze` / `sysctl` / `oomctl` / `systemctl show` in that file do have clocks.

Design-only, no host reading claimed: `FixtureDesign`. `OwnerMap` is a routing table; its "observed live" scratch cell and the wrap sentence cite siblings rather than a command. The restart/`echo > .ufo/state`/`sudo mkdir` strings in that file are prescriptions, not observations, and they are outside mori's detect-only boundary — parent should not land them as census procedure.

## Impacted axes

- **Calibration.** The round's compare contract is "same predicate, same id". CorpusMap's settled set, the erratum's `closeout.md` sentence, FindingIds' GiB label, and RerunStability's blob pin would make a later diff chase a state that was never measured. LOG prose ages (`103830`, `95445`) already disagree with the only stamped receipt (`103843`, `95458`).
- **Operability.** A cold re-run cannot reproduce LiveReceipt's 588, the erratum's 1228, or CorpusMap §5.2, because the argv is absent. FINDING lines cannot be joined to a clock except by assuming the banner `ts=` applies, which the emitter does not say.
- **Coverage.** Unstamped journal examples (pipewire core-dump, oom-kill line) and the unbounded "every fleet process" sentence look like fleet evidence and are not. KillEventsJournal and CgroupMemoryEvents already hold the stamped versions. Landing the unstamped copies creates a second authority.

## Smallest safe correction

Do not add a probe. Do not retune a threshold in this pass.

1. Refuse to land, as observation, any row that is not `command | measured_at | output`. That drops CorpusMap §5.2's sketch, FindingIds' untabled journal/meminfo anchors, CrossDomainBoundary's cgroup paste, FalsePositiveAudit FP-4/FP-5/FP-9 ages, LiveReceipt's uncommented class counts, and the erratum sentences in counterexamples 2 and 5. Keep the seats that already have the triple.
2. In `emit_finding`, append `cmd=` and `ts=$TS_UTC` the same way `emit_surface` already does. Stop emitting `WATCHDOG_LOG_UNAVAILABLE` for a missing `pgrep`.
3. In LOG/SCORECARD, cite the receipt timestamp and the script sha next to the banner. Do not treat GateRegistryRow's 13/14 FAIL and a later 14/14 PASS as one run.
4. Replace the script comment "w5..w11 closeout.md / five settled waves aged" with the filenames actually present, or delete the comment. `w1`–`w4` stay age findings until a settle token is shown.

No remediation of the host. No census verdict claimed.
