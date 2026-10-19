# kaika W1 — ART dossier · lane `mori` (fleet & host observability, detection/report only)

- Author: `W1ArtMori` (scout, leaf — no dispatch) · written 2026-10-19 · repo read-only: `/home/vgpnk/Projects/shokunin/mori-shokunin`
- Tools: `web_search` and page reads available. One fetch failed (ratatoskr.run, HTTP 429) → kept under Leads, not rows.
- Prompt-injection check: no instruction addressed to an agent was found in the fetched content. S030's install/enable/tune shell steps are tutorial content; I read them as data and ran none of them.
- Axes I worked to (godspeed): **coverage** (ground the corpus lacks) · **authority** (tier-A share) · **falsifiability** (every candidate entry has a recheck) · **conformance** (SOURCES.md contract, MESSAGE-free journal practice).
- Marking: plain text = observed in a file, page or command this session. `[INFERENCE]` = derived. `[UNKNOWN]` = open.

## 0. Ground measured this session (host + repo, read-only)

| fact | value — command |
|---|---|
| kernel | `7.2.3-arch1-3` — `uname -r` |
| systemd | `systemd 261 (261.2-1-arch)`, built with `+PCRE2` — `systemctl --version` |
| PSI files | 4 (`cpu io irq memory`) — `ls /proc/pressure \| wc -l` |
| host-wide OOM counter present | 1 — `grep -c '^oom_kill ' /proc/vmstat` |
| userspace OOM killers | `systemd-oomd.service` inactive and disabled; `earlyoom.service` inactive — `systemctl is-active systemd-oomd.service earlyoom.service; systemctl is-enabled systemd-oomd.service` |
| binaries | `bpftrace bpftool earlyoom otelcol otel-cli below atop` absent; `oomctl coredumpctl journalctl` present — `for b in bpftrace bpftool earlyoom oomctl coredumpctl journalctl otelcol otel-cli below atop; do command -v "$b" \|\| echo absent; done` |
| cgroup2 mount options | `nsdelegate,memory_recursiveprot,memory_hugetlb_accounting` with no `memory_localevents`, so `memory.events` is hierarchical — `grep -E '^cgroup2 ' /proc/mounts` |
| kill-class catalog entries on host | 3 — `journalctl --list-catalog fe6faa94e7774663a0da52717891d8ef d989611b15e44c9dbf31e3c81256e4ed fc2e22bc6ee647b6b90729ab34a250b1 \| wc -l` |
| kernel OOM kills, this boot / all retained boots | 0 / 5 — `journalctl -k -b 0 -q --grep='^oom-kill:constraint=' -o json --output-fields=_BOOT_ID \| wc -l` (and `-b all`). The `Killed process` line count agrees: 5 — `journalctl -k -b all -q --grep='(Out of memory\|Memory cgroup out of memory): Killed process [0-9]+' -o json --output-fields=_BOOT_ID \| wc -l` |
| unit-level OOM notices `fe6faa94…`, user / system journal | 7 / 9, all in boot `7bd93aee…`, the same boot as the 5 kernel kills — `journalctl --user -q MESSAGE_ID=fe6faa94e7774663a0da52717891d8ef -o json --output-fields=_BOOT_ID \| grep -oE '"_BOOT_ID":"[0-9a-f]{8}' \| sort \| uniq -c` (and `--system`) |
| systemd-oomd kill notices `d989611b…` | 0 in each scope — same command with `MESSAGE_ID=d989611b15e44c9dbf31e3c81256e4ed` |
| journal "messages missed" markers | 0 — `journalctl -b all -q MESSAGE_ID=e9bf28e6e834481bb6f48f548ad13606 -o json --output-fields=_BOOT_ID \| wc -l` |

Every journal query above is count-only. Each output mode restricts fields with `--output-fields`, so `MESSAGE` text is never printed. This follows the lane's exclusion of "any journal output mode that keeps `MESSAGE`" (`SKILL.md:143-145`).

## 1. Uncovered ground

### 1a. What the corpus holds (from the files named by the ART shape)

- Coverage map: 12 knowledge rows and 7 lesson rows (`grep -cE '^\| \`knowledge/' corpus/README.md` → 12; `grep -cE '^\| \`lessons/' corpus/README.md` → 7). On disk there are 14 knowledge files and 10 lessons (`ls corpus/knowledge/*.md | wc -l` → 14; `ls corpus/lessons/*.md | wc -l` → 10).
- The knowledge filenames all concern the census machine: `verdict-machine-r4/5/6`, `surfaces-r7/r8`, `observability-surfaces-r2`, `silence-*`/`lane-silence`/`progressing-weak`, `observability-census-r1`, `drift-pin-r10`, `selftest-flake-r9`, `audit-r11`.
- Domain surfaces held (`SKILL.md:15-20`):
  - watchdog liveness: pid, start time, last tick, `.ufo/state` values
  - wave settlement
  - kill events: `journalctl --user -b` plus cgroup counters
  - runway: `df`, since-boot IO average, memory PSI `avg10`, fill/avail, `memory.peak`
  - tmux relevance and freshness
  - lane silence grading
- Kill-event knowledge held:
  - the `memory.events.local` discriminator and its propagation/restart traps (`knowledge/observability-census-r1.md:134-140`, `knowledge/observability-surfaces-r2.md:205-209`)
  - the coredump `MESSAGE_ID` with a `COREDUMP_SIGNAL=11` filter (`r1:186-199`)
  - one manual attribution of a kernel OOM victim (`r1:142-146`, "cgroup path now `ENOENT`")
  - "Segfaults are a structured field, not a word." (`r1:150`)
- PSI held: memory `some/full avg10` is graded (`corpus/README.md:129-131`). The `io`/`memory` files were observed as free aggregates, and io PSI was classed as "stall, not bytes" (`lessons/2026-10-15-free-lunch-measurements-counter-baselines.md:57-94`, `:203`).
- External sources cited by the corpus: 1 URL in total — `grep -rhoE 'https?://[^ )>\`"]+' SKILL.md PROVINCE.md corpus/README.md corpus/QUALITY.md corpus/knowledge corpus/lessons | wc -l` → 1. It is the PSI kernel doc, cited by the free-lunch lesson.
- `QUALITY.md` has 5 criteria (`grep -cE '^[0-9]+\. ' corpus/QUALITY.md` → 5). None mentions source tier, recheck or verified-at (`grep -cE 'recheck|verified-at|tier' corpus/QUALITY.md` → 0).
- Missing structure: `corpus/README.md` has no `## Frontier` (`grep -cE '^## Frontier' corpus/README.md` → 0), and `PROVINCE.md` has no Core/Frontier/Adjacent headings (`grep -cE '^#+ (Core|Frontier|Adjacent)' PROVINCE.md` → 0).
- Scope: `PROVINCE.md:6-10` owns kill/OOM classes "from `journalctl --user` and cgroup `memory.events`". The system journal is the named unblock in `corpus/README.md:266-268`.

### 1b. What the corpus does not hold (negative claims, each with its sweep)

Sweep scope: `F="SKILL.md PROVINCE.md corpus/README.md corpus/QUALITY.md corpus/knowledge corpus/lessons"`. Count for each term: `grep -rhiE "<term>" $F | wc -l`.

| term (regex) | lines held | ground it stands for |
|---|---|---|
| `oomd` | 0 | systemd-oomd: kill mechanism, xattrs, catalog ID, 2025-26 features |
| `earlyoom` | 0 | earlyoom kill lines, `--kernel-oom` delegation |
| `bpftrace\|ebpf\|\bbpf\b` | 0 | eBPF kill/OOM tracing (`oom:mark_victim`, `signal:signal_generate`, `oomkill.bt`, `killsnoop.bt`) |
| `opentelemetry\|\botel\b\|otlp` | 0 | OTel for CLI/agent workloads |
| `\bcursor\b\|--cursor\|__CURSOR\|after-cursor` | 0 | journal cursors for new-since-pin counts |
| `pressure/cpu\|cpu\.pressure\|pressure/irq\|irq\.pressure` | 0 | CPU and IRQ PSI. The host exposes both; see §0 |
| `POLLPRI\|psi trigger\|PSI trigger` | 0 | event-driven PSI triggers |
| `/proc/vmstat` | 0 | host-wide `oom_kill` counter |
| `pidfd` | 0 | race-free process liveness handles |
| `signal_generate\|killsnoop\|mark_victim` | 0 | kernel signal and OOM tracepoints |
| `gen_ai\|invoke_agent\|cicd\.` | 0 | agent spans and CI/CD result vocabulary |
| `fe6faa94\|d989611b` (case-sensitive) | 0 | OOM-class `MESSAGE_ID`s. The only `MESSAGE_ID` lines held are coredump (3 lines) |
| `oom-kill:constraint\|Killed process\|task_memcg\|_TRANSPORT=kernel\|journalctl -k` | 1 | `r1:142`, a one-off manual attribution. The line format and its fields are not held |

A note on my own sweep: the first combined sweep counted "precursor" as `cursor`. I corrected it with `\b`. See M1 in §7.

## 2. Current art 2025–2026 not held

| item | when | source | why it matters to mori |
|---|---|---|---|
| systemd-oomd kills with the kernel's `cgroup.kill` (`cg_kill_kernel_sigkill`), falling back to a `kill()` loop; it increments `user.oomd_ooms` and `user.oomd_kill` xattrs and emits D-Bus `Killed(path, reason)` | systemd v261 (host) = main | S011 | These kills never touch `memory.events oom_kill` (K1). A kill()-syscall tracer cannot see them (M5) |
| oomd prekill varlink hook, notify-only (260); `.oomrule` rulesets with `MemoryPressureAbove=`, `SwapUsageMax=`, `Action=kill-all/kill-by-pgscan/kill-by-swap` (261); `--dry-run` short `-n` (262); SIGHUP reload (258) | 2025–2026 | S007, S008 | New kill policies mean new kill classes to detect. The prekill hook is a notification surface, but it is privileged and synchronous |
| GHSA-652q-wxr6-h5j6: unprivileged arbitrary SIGKILL via oomd varlink; affected ≥250, patched 261 / 260.3 / 259.7 / 258.9 | 2026-08-10 | S012 | Adjacency only: patch state is tsukuroi's. It documents the xattr write path |
| systemd Pressure protocol: `MemoryPressureWatch=`, `CPUPressureWatch=`, `IOPressureWatch=`; thresholds per 2 s window, default 200 ms; `sd_event_add_cpu_pressure/io_pressure`; GLib 2.90 honours it | current doc | S010 | Current practice is event-driven pressure with 2 s windows. That needs a resident consumer, not a one-shot census |
| BPF OOM RFC: `bpf_handle_psi_event`, `bpf_handle_out_of_memory` | RFC 2025 | S021 | Not in mainline `mm/oom_kill.c` at master (`curl -fsS https://raw.githubusercontent.com/torvalds/linux/master/mm/oom_kill.c \| grep -cE 'bpf_oom\|oom_policy'` → 0). A future kill class to watch |
| bpftrace v0.25–v0.27 (2026-03 → 2026-09). `oomkill.bt` gained memcg path (2025-09-03); `killsnoop.bt` gained tkill/tgkill (2025-05-27) | 2025–2026 | S017–S020 | Recipes must pin a version. Tool scope matters (M5) |
| earlyoom v1.9.0 | 2025-09-16 (releases feed, opened; not a row) | S016 | A second userspace killer. Its `--kernel-oom` mode delegates to the kernel killer, so those kills are counted (K1) |
| OTel GenAI conventions moved to `open-telemetry/semantic-conventions-genai`; `invoke_agent`, `execute_tool`, `invoke_workflow`, `plan` are at Development status | 2026 | S024 | A vendor-neutral vocabulary if lanes ever emit agent telemetry. mori would only consume it |
| OTel CI/CD semconv at Release Candidate: 6 result values, with `error` (CI system fault, e.g. worker killed) separate from `failure` | current | S022 | Vocabulary for wave and lane settlement (K6) |
| OTLP File Exporter (Development): JSONL to a file or stdout, one signal per file, no ordering guarantee | current | S023 | A network-free artifact a read-only census could count |
| `memory.peak` fd-local reset (documented); an Aug-2026 patch thread reports resets clobbering other fds' watermark | doc + 2026 lead | S002 + Lead L1 | The lane's `mem_peak` is whole-lifetime. A windowed peak needs a write (rejected, R3) |
| `/proc/pressure/irq` and `irq.pressure`, plus system-level CPU `full` "set to zero for backward compatibility" | kernel ≥5.13 behaviour, still documented | S001, S002 | CPU/IRQ saturation rows are free one-read signals by the lane's own free-lunch rule. System-level CPU `full=0` is not evidence of no stall |

## 3. SOURCES.md rows (contract format; all opened 2026-10-19)

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | PSI - Pressure Stall Information (kernel docs) — https://docs.kernel.org/accounting/psi.html | docs | A | some/full avg10/60/300 plus total in µs (total catches spikes the averages miss); poll() triggers with 500 ms to 10 s windows, unprivileged windows must be multiples of 2 s, a trigger dies with its fd; per-cgroup *.pressure files share the format; system-level CPU full is always 0 | queued | 2026-10-19 | on-release | lessons/2026-10-15-free-lunch-measurements-counter-baselines.md |
| S002 | Control Group v2 (kernel admin guide) — https://docs.kernel.org/admin-guide/cgroup-v2.html | docs | A | memory.events fields oom / oom_kill ("any kind of OOM killer") / oom_group_kill, hierarchical unless memory_localevents; memory.peak fd-local reset; cgroup.events populated with poll and inotify; cgroup.kill; cgroup.pressure; irq.pressure | queued | 2026-10-19 | on-release | — |
| S003 | Linux mm/oom_kill.c at v7.2 (identical lines at master) — https://raw.githubusercontent.com/torvalds/linux/v7.2/mm/oom_kill.c | code | A | :935-936 count_vm_event(OOM_KILL) and memcg_memory_event_mm(MEMCG_OOM_KILL) fire inside __oom_kill_process before SIGKILL; :447 one-line oom-kill:constraint summary ending task=, pid=, uid=; :945 Killed process line with UID | queued | 2026-10-19 | on-release | — |
| S004 | Linux mm/memcontrol.c (master) — https://raw.githubusercontent.com/torvalds/linux/master/mm/memcontrol.c | code | A | :1820 and :1825 append oom_memcg= and task_memcg= cgroup paths to the OOM summary; :4966 is the file's only MEMCG_OOM_KILL use (printing memory.events) | queued | 2026-10-19 | on-release | — |
| S005 | Linux include/trace/events/oom.h — https://raw.githubusercontent.com/torvalds/linux/master/include/trace/events/oom.h | code | A | oom:mark_victim carries pid, comm, total_vm, anon/file/shmem rss, uid, pgtables, oom_score_adj; reaper tracepoints wake_reaper, start/finish/skip_task_reaping | queued | 2026-10-19 | on-release | — |
| S006 | Linux include/trace/events/signal.h — https://raw.githubusercontent.com/torvalds/linux/master/include/trace/events/signal.h | code | A | signal:signal_generate records sig, errno, code (SI_USER vs SI_KERNEL), target comm and pid, group and result for every generated signal; signal_deliver may not match generate | queued | 2026-10-19 | on-release | — |
| S007 | systemd-oomd.service(8) — https://www.freedesktop.org/software/systemd/man/latest/systemd-oomd.service.html | docs | A | polls PSI for units set to kill, then SIGKILLs every process of one selected descendant cgroup (leaf or memory.oom.group only); --dry-run since 253 (-n since 262); SIGHUP reload since 258; swap strongly advised | watch | 2026-10-19 | on-release | — |
| S008 | oomd.conf(5) — https://www.freedesktop.org/software/systemd/man/latest/oomd.conf.html | docs | A | defaults SwapUsedLimit=90%, DefaultMemoryPressureLimit=60% of PSI full avg10 sustained for DefaultMemoryPressureDurationSec=30s; privileged varlink prekill notify hook (260); .oomrule rulesets with Action=kill-all / kill-by-pgscan / kill-by-swap (261) | watch | 2026-10-19 | on-release | — |
| S009 | oomctl(1) — https://www.freedesktop.org/software/systemd/man/latest/oomctl.html | docs | A | oomctl dump prints the cgroup and system contexts systemd-oomd holds (since 247), a read-only view of what oomd monitors | queued | 2026-10-19 | on-release | — |
| S010 | Resource Pressure Handling in systemd — https://systemd.io/PRESSURE/ | docs | A | the *PressureWatch= protocol: a $MEMORY/CPU/IO_PRESSURE_WATCH path plus a base64 _WRITE threshold, POLLPRI on PSI files; thresholds per 2 s window, default 200 ms; the per-cgroup PSI file is delegated to the service | queued | 2026-10-19 | on-release | — |
| S011 | systemd src/oom/oomd-util.c at v261 (identical lines at main) — https://raw.githubusercontent.com/systemd/systemd/v261/src/oom/oomd-util.c | code | A | oomd_cgroup_kill: :269 increments xattr user.oomd_ooms; :274 kills through cg_kill_kernel_sigkill with a kill() fallback; :306 adds the killed-PID count to user.oomd_kill; :316 emits D-Bus signal Killed(path, reason) | queued | 2026-10-19 | on-release | — |
| S012 | GHSA-652q-wxr6-h5j6 systemd-oomd advisory (2026-08-10) — https://github.com/systemd/systemd/security/advisories/GHSA-652q-wxr6-h5j6 | docs | A | maintainer-published: oomd's world-accessible varlink ReportManagedOOMCGroups allowed path traversal to arbitrary SIGKILL; affected ≥250, patched 261 / 260.3 / 259.7 / 258.9; shows the user.oomd_* xattr write path | watch | 2026-10-19 | on-release | — |
| S013 | systemd journal message catalog — https://raw.githubusercontent.com/systemd/systemd/main/catalog/systemd.catalog.in | code | A | stable MESSAGE_IDs: :66 fc2e22bc… core dump; :604 fe6faa94… a process of a unit killed by the kernel OOM killer; :884 d989611b… systemd-oomd killed processes in a unit | queued | 2026-10-19 | on-release | — |
| S014 | journalctl(1) — https://www.freedesktop.org/software/systemd/man/latest/journalctl.html | docs | A | --after-cursor and --show-cursor (206), --cursor-file (242); -k adds _TRANSPORT=kernel and implies -b 0; --output-fields always adds __CURSOR, __REALTIME_TIMESTAMP, __MONOTONIC_TIMESTAMP, _BOOT_ID; --list-catalog; -I invocation (257); system journal readable by systemd-journal, adm, wheel | queued | 2026-10-19 | on-release | — |
| S015 | systemd.journal-fields(7) — https://www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html | docs | A | MESSAGE is not to be parsed for metadata; MESSAGE_ID is the 128-bit type key; trusted _TRANSPORT (kernel, stdout, journal), _BOOT_ID, _SYSTEMD_USER_UNIT, _SYSTEMD_INVOCATION_ID; address fields __CURSOR and __SEQNUM / __SEQNUM_ID | queued | 2026-10-19 | on-release | — |
| S016 | earlyoom (README) — https://github.com/rfjakob/earlyoom | code | A | userspace killer polling MemAvailable and SwapFree up to 10 times a second: SIGTERM at 10 percent / 10 percent, SIGKILL at 5 percent / 5 percent, to the highest oom_score; logs sending SIGTERM to process … uid … to stderr and its unit journal; --kernel-oom delegates to the kernel killer via sysrq f; -N and -P hooks get EARLYOOM_PID and friends | queued | 2026-10-19 | on-release | — |
| S017 | bpftrace (repo README) — https://github.com/bpftrace/bpftrace | tool | A | eBPF tracing language over kprobes, uprobes, tracepoints and USDT; distro packages; tells users to check bpftrace --version against the docs; user tools live in bpftrace/user-tools | queued | 2026-10-19 | on-release | — |
| S018 | bpftrace releases — https://github.com/bpftrace/bpftrace/releases | tool | A | v0.27.0 2026-09-10, v0.26.0 2026-05-26, v0.25.0 2026-03-13, v0.24.x 2025: roughly quarterly minor releases with breaking changes, so pin the version in any recipe | watch | 2026-10-19 | on-release | — |
| S019 | bpftrace tools/oomkill.bt — https://raw.githubusercontent.com/bpftrace/bpftrace/master/tools/oomkill.bt | code | A | kprobe:oom_kill_process prints the triggering PID and comm, the victim PID and comm, pages and loadavg; memcg cgroup path added 2025-09-03 | queued | 2026-10-19 | on-release | — |
| S020 | bpftrace tools/killsnoop.bt — https://raw.githubusercontent.com/bpftrace/bpftrace/master/tools/killsnoop.bt | code | A | probes only the kill, tkill and tgkill syscall tracepoints (tkill and tgkill added 2025-05-27): sender PID and comm, signal, target, result | queued | 2026-10-19 | on-release | — |
| S021 | LWN: Custom out-of-memory killers in BPF (Corbet, 2025-05-01) — https://lwn.net/Articles/1019230/ | community | B | Gushchin's RFC: bpf_handle_psi_event and bpf_handle_out_of_memory hooks; the kernel checks memory was really freed before falling back to its own killer; why userspace killers lag | watch | 2026-10-19 | on-release | — |
| S022 | OTel semconv: CI/CD spans — https://opentelemetry.io/docs/specs/semconv/cicd/cicd-spans/ | spec | A | Release Candidate: pipeline and task results are success / failure / error / timeout / cancellation / skip; error means a CI-system fault such as a killed worker, failure means a tool's non-zero exit | queued | 2026-10-19 | on-release | — |
| S023 | OTel spec: OTLP File Exporter — https://opentelemetry.io/docs/specs/otel/protocol/file-exporter/ | spec | A | Development: OTLP JSON lines to a file or stdout, one signal type per file, no ordering or monotonic-timestamp guarantee; a network-free artifact | watch | 2026-10-19 | on-release | — |
| S024 | OTel GenAI agent spans (semantic-conventions-genai) — https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-agent-spans.md | spec | A | Development: create_agent, invoke_agent (client and internal), invoke_workflow, plan and execute_tool spans; span status follows Recording Errors; the GenAI conventions now live outside the core semconv repo | watch | 2026-10-19 | 30d | — |
| S025 | otel-cli — https://github.com/equinix-labs/otel-cli | tool | A | emits spans from shell scripts (exec, span background with events); non-recording when no endpoint is set; server json writes received traces to a directory; experimental stability badge | queued | 2026-10-19 | 90d | — |
| S026 | OTel Collector hostmetrics receiver README — https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector-contrib/main/receiver/hostmetricsreceiver/README.md | docs | A | 11 scrapers (cpu, disk, load, filesystem, memory, network, nfs, paging, processes, process, system), none of which reads PSI; default collection_interval 1m; metrics beta, logs development | queued | 2026-10-19 | on-release | — |
| S027 | pidfd_open(2) — https://man7.org/linux/man-pages/man2/pidfd_open.2.html | docs | A | a pidfd is pollable: EPOLLIN when the task terminates, EPOLLHUP when it is reaped; a PID-reuse-proof handle (Linux 5.3, PIDFD_THREAD 6.9) that only helps a process holding it over time | queued | 2026-10-19 | on-release | — |
| S028 | Kubernetes: Liveness, Readiness, and Startup Probes — https://kubernetes.io/docs/concepts/workloads/pods/probes/ | docs | A | the startup probe suspends liveness until start succeeds; liveness targets running-but-not-progressing (deadlock); an Unknown result means take no action; maps to mori's young, wedged and unavailable | queued | 2026-10-19 | 180d | — |
| S029 | Google SRE Book ch. 6, Monitoring Distributed Systems (2016) — https://sre.google/sre-book/monitoring-distributed-systems/ | book | B | symptoms vs causes; black-box vs white-box; four golden signals including saturation and its prediction (disk full in 4 hours); avoid magic learned thresholds | queued | 2026-10-19 | 365d | — |
| S030 | OneUptime blog: Configure systemd-oomd on Ubuntu (2026-03-02) — https://oneuptime.com/blog/post/2026-03-02-how-to-configure-systemd-oomd-for-out-of-memory-handling-on-ubuntu/view | community | C | rejected: restates oomd.conf(5) defaults; its detection recipe is a free-text grep over journal MESSAGE where the catalog MESSAGE_ID d989611b… is the stable key; a remediation how-to (install, enable, tune) outside a detection-only lane | rejected | 2026-10-19 | — | — |

Why older sources are kept:
- S029 (2016) is still the canonical statement of the symptom/cause and saturation framing, and nothing in 2025–26 has replaced it.
- S001 is dated 2018 but is maintained in-tree, so it is authoritative for the current kernel.

Opened, not rowed (to keep the table at ≤30):
- earlyoom releases feed, https://github.com/rfjakob/earlyoom/releases — v1.9.0 tagged 2025-09-16
- Prometheus query functions, https://prometheus.io/docs/prometheus/latest/querying/functions/ — `absent_over_time()` as windowed absence detection
- the opentelemetry.io "Moved" notice for GenAI agent spans

### Leads (unopened)

- L1 `[PATCH v3 0/2] mm, memcg: fix memory.peak reset clobbering other fds' watermark` (2026-08), https://ratatoskr.run/cgroups/2026/08/17410441/t. The fetch returned HTTP 429; known only from a search snippet.
- L2 LWN "mm: BPF OOM", https://lwn.net/Articles/1034293/; LKML `[PATCH v2 06/23] mm: introduce BPF struct ops for OOM handling` (2025-10), https://lkml.iu.edu/2510.3/11375.html.
- L3 systemd issue #22903 "systemd-oomd: Detecting OOM kills in delegated sub-trees", https://github.com/systemd/systemd/issues/22903. Directly on mori's detection problem.
- L4 systemd.resource-control(5): `ManagedOOM*`, `OOMRules=`, `*PressureWatch=`, https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html.
- L5 org.freedesktop.oom1(5): the `Killed` D-Bus signal contract.
- L6 sd_journal_get_seqnum(3): seqnum semantics across rotation, needed by K5's unknowns.
- L7 capabilities(7): `CAP_BPF` and `CAP_PERFMON` privilege for eBPF.
- L8 iovisor/bcc `tools/oomkill.py` and `exitsnoop`; Brendan Gregg, *BPF Performance Tools* (2019).
- L9 facebookincubator/below: a recorder that keeps PSI and cgroup history.
- L10 Agent-CLI telemetry docs (Claude Code monitoring/OTel, Codex CLI `[otel]`, Gemini CLI telemetry). These are the emitters, if the fleet ever enables them.
- L11 prometheus/node_exporter `pressure` collector; hakavlad/nohang.
- L12 Honeycomb "Instrumenting AI Agents"; Dash0 and other secondary GenAI-semconv explainers (tier C/B candidates).

## 4. Candidate knowledge entries (6)

### K1 `oom-kill-counter-is-kernel-only`

- **Claim:** On kernel v7.2, `memory.events`/`memory.events.local` `oom_kill` and `/proc/vmstat` `oom_kill` are incremented only inside `__oom_kill_process`, i.e. by the kernel OOM killer: global, memcg, cpuset/mempolicy, and sysrq-f (which also enters `oom_kill_process`). A process killed by a userspace killer does not move either counter. That covers systemd-oomd (`cgroup.kill` or `kill()`) and earlyoom (SIGTERM/SIGKILL), except earlyoom `--kernel-oom`, which delegates to the kernel.
- **Consequence for mori:** `oom_kill=0` means "no kernel OOM kills", not "no memory kills". The SKILL error pattern at `SKILL.md:28` needs this converse.
- **Sources and quotes:**
  - S003 `mm/oom_kill.c:935-936` (v7.2 = master): `count_vm_event(OOM_KILL);` and `memcg_memory_event_mm(mm, MEMCG_OOM_KILL);`
  - S004 sweep: the file's only `MEMCG_OOM_KILL` use is the print at `:4966` (`curl -fsS https://raw.githubusercontent.com/torvalds/linux/master/mm/memcontrol.c | grep -c MEMCG_OOM_KILL` → 1). v7.2 `oom_kill.c` has exactly 1 such site (`curl -fsS https://raw.githubusercontent.com/torvalds/linux/v7.2/mm/oom_kill.c | grep -c MEMCG_OOM_KILL` → 1).
  - Doc trap, S002 memory.events: "The number of processes belonging to this cgroup killed by any kind of OOM killer."
  - Userspace paths: S011 `:274` (oomd); S016 README "Why not trigger the kernel oom killer?" (earlyoom `--kernel-oom`).
- **Observed / inference / unknown:**
  - Observed: the two files above.
  - `[INFERENCE]`: no other kernel file increments `MEMCG_OOM_KILL`. Not swept tree-wide. Recheck: `git grep -n 'MEMCG_OOM_KILL\|count_vm_event(OOM_KILL)' v7.2 -- mm include` on a kernel checkout.
  - `[UNKNOWN]`: whether a merged BPF OOM (S021) would count. Watch.
- **Fills:** the `SKILL.md:28` error-pattern row and the decision-table row "Did something get killed?" (`SKILL.md:17`). New coverage-map row; Frontier F1.
- **Recheck:** the two `curl … | grep` commands above. Optional hermetic canary, a lane decision: SIGKILL a child in a throwaway user scope and re-read `memory.events.local` → `oom_kill` unchanged.
- **Clears QUALITY.md:** #1 (falsifiable by grep and canary), #2 (path:line plus command), #3 (tree-wide claim marked `[INFERENCE]`). The doc-wording trap is recorded rather than dropped (#5 spirit).

### K2 `kernel-oom-line-carries-attribution`

- **Claim:** Each kernel OOM kill logs two kernel-transport lines:
  - a one-line summary `oom-kill:constraint=<C>,nodemask=…[,cpuset/mems_allowed],(oom_memcg=<path> | global_oom),task_memcg=<path>,task=<comm>,pid=<pid>,uid=<uid>`
  - then `<Out of memory | Memory cgroup out of memory>: Killed process <pid> (<comm>) … UID:<uid> …`

  Together these carry the PID, uid, victim cgroup path and an entry timestamp. Those are the three facts `SKILL.md:28` says counters lack ("counters alone identify neither the killed PID, event time nor fleet membership"). The lines live in the system journal with `_TRANSPORT=kernel`, readable by `systemd-journal`/`adm`/`wheel`. They outlive the victim's transient scope (`r1:143-144`: "cgroup path now `ENOENT`").
- **Constraint (essence):** `MESSAGE` is never echoed (`SKILL.md:131-145`). A probe may emit only shape-validated tokens (digits for `pid`/`uid`, a strict cgroup-path shape for `task_memcg`), otherwise `shape-refused`. This is the same rule r7/r8 applied to PSI tokens (`SKILL.md:138-141`).
- **Sources and quotes:**
  - S003 `mm/oom_kill.c:447`: `pr_info("oom-kill:constraint=%s,nodemask=%*pbl",`; `:945` "Killed process" format.
  - S004 `mm/memcontrol.c:1825`: `pr_cont(",task_memcg=");` and `:1820` `",oom_memcg="`.
  - S014 `-k`: "This adds the match "_TRANSPORT=kernel"."; access: 'Members of the groups "systemd-journal", "adm", and "wheel" can read all journal files.'
- **Measured (count-only, MESSAGE-free):** 5 summaries and 5 `Killed process` lines across retained boots, all in boot `7bd93aee…`; 0 this boot (§0 commands).
- **Fills:** `corpus/README.md:266-268` Journal scope (system-journal probe is the named unblock); `SKILL.md:28`; Frontier F2. Scope note: `PROVINCE.md:8` names `journalctl --user` only, so wave 2 decides the province wording.
- **Recheck:** `journalctl -k -b all -q --grep='^oom-kill:constraint=' -o json --output-fields=_BOOT_ID | wc -l` → 5 at 2026-10-19; `curl -fsS https://raw.githubusercontent.com/torvalds/linux/v7.2/mm/oom_kill.c | grep -n 'oom-kill:constraint'` → `447:`.
- **Clears QUALITY.md:** #1, #2 and #3 (attribution design is proposed, not measured, and labeled so).

### K3 `kill-classes-by-message-id-not-text`

- **Claim:** The host catalog (systemd 261) defines `fe6faa94e7774663a0da52717891d8ef` (process of a unit killed by the kernel OOM killer), `d989611b15e44c9dbf31e3c81256e4ed` (systemd-oomd killed processes in a unit) and `fc2e22bc6ee647b6b90729ab34a250b1` (core dump; already used by the census, `r1:193`). Counting by `MESSAGE_ID` with `-o json --output-fields=…` never emits `MESSAGE` and survives message rewording. It is `r1:150`'s lesson ("Segfaults are a structured field, not a word.") applied to the OOM classes.
- **Second, measured claim — the unit of count:** `fe6faa94…` notices are per unit, not per kill. Boot `7bd93aee…` holds 5 kernel kills but 7 user-journal plus 9 system-journal `fe6faa94…` notices. Summing scopes, or equating notices with kills, over-counts (16 vs 5).
- **Sources and quotes:**
  - S013 `:604-605`: "Subject: A process of @UNIT@ unit has been killed by the OOM killer."; `:884-885`: "Subject: systemd-oomd killed one or more processes in unit @UNIT@".
  - S015: MESSAGE_ID is "A 128-bit message identifier ID for recognizing certain message types"; MESSAGE "is not supposed to be parsed for metadata".
  - S014 `--output-fields`: the `__CURSOR`, `__REALTIME_TIMESTAMP`, `__MONOTONIC_TIMESTAMP` and `_BOOT_ID` "fields are always printed".
- **Observed / inference / unknown:**
  - Observed: 3 catalog IDs; 5 vs 7+9; 0 oomd notices (oomd disabled).
  - `[UNKNOWN]`: the fan-out mechanism, i.e. which ancestor units each manager notices. The 16/5 ratio is not an integer, so fan-out is not uniform. Recheck by grouping with `--output-fields=_BOOT_ID,UNIT,USER_UNIT` (unit names only, no MESSAGE).
- **Fills:** `SKILL.md:17` "journal class counts"; Frontier F1/F2; the lesson class from r1 Erratum 4.
- **Recheck:** `journalctl --list-catalog fe6faa94e7774663a0da52717891d8ef d989611b15e44c9dbf31e3c81256e4ed fc2e22bc6ee647b6b90729ab34a250b1 | wc -l` → 3; per-scope counts as in §0.
- **Clears QUALITY.md:** #1, #2 and #3 (mechanism kept `[UNKNOWN]`). The over-count is a measured mistake class (M3).

### K4 `oomd-records-kills-on-the-cgroup`

- **Claim:** systemd-oomd v261 (identical at main) records each kill on the killed cgroup:
  - `user.oomd_ooms` += 1 before the kill (`oomd-util.c:269`)
  - `user.oomd_kill` += number of PIDs killed after it (`:306`)

  The kill itself is `cg_kill_kernel_sigkill` with a `kill()`-loop fallback on `EOPNOTSUPP` (`:274`; the function's own comment reads "Just for safety, in case group.kill is used"). It then emits D-Bus `org.freedesktop.oom1.Manager.Killed(path, reason)` (`:316`). None of this moves `memory.events oom_kill` (K1). On this host oomd is inactive and disabled, so a probe must render `unavailable (oomd-inactive)`, never `0`. That is the lane's own "unavailable ≠ unhealthy" rule (`SKILL.md:51`).
- **Sources and quotes:**
  - S011 `:269`: `r = increment_oomd_xattr(ctx->path, "user.oomd_ooms", 1);`
  - S007: "select a cgroup to terminate, and send `SIGKILL` to all processes in it."
  - S012 (maintainer-published advisory) shows the same xattr path.
- **`[INFERENCE]`:**
  - The xattrs vanish when a transient unit's cgroup is removed. Analogous to r1's measured `ENOENT` scope; not measured for oomd. So the durable record is K3's `d989611b…`.
  - Reading `user.*` xattrs on cgroupfs needs only read access to the directory. Not measured; `getfattr` is not used here.
  - The D-Bus signal needs a resident listener.
- **Fills:** Frontier F1; `SKILL.md:28`.
- **Adjacency, reported not absorbed:** the host systemd version against GHSA-652q-wxr6-h5j6 is tsukuroi's (OS package state). Enabling or tuning oomd is operator/tsukuroi.
- **Recheck:** `curl -fsS https://raw.githubusercontent.com/systemd/systemd/v261/src/oom/oomd-util.c | grep -nE '"user\.oomd_(ooms|kill)"'` → `269`, `306`; `systemctl is-active systemd-oomd.service` → `inactive`.
- **Clears QUALITY.md:** #1, #2 and #3.

### K5 `journal-cursor-new-since-pin`

- **Claim:** `--after-cursor=<C>` starts strictly after the entry at C. `-o json --output-fields=…` always includes `__CURSOR`, and `--show-cursor` prints the last cursor. So the r10 `--pin`, which already writes the lane baseline, can store one cursor per journal scope. `--drift` can then count kill-class entries (K3 IDs, K2 kernel summaries) strictly newer than the pin, read-only and MESSAGE-free.
- **Why it matters:** this closes, for kill classes, the r10 blind spot where "a count-only change reads `none` by construction" (`corpus/README.md:254-256`). A new kill inside an existing finding id would become visible as `new_since_pin=N`.
- **Sources and quotes:** S014 `--after-cursor`: "Start showing entries from the location in the journal after the location specified by the passed cursor."; `--cursor-file` (242): "Use this option to continually read the journal by sequentially calling journalctl."; S015 `__CURSOR`, `__SEQNUM`/`__SEQNUM_ID`.
- **`[UNKNOWN]`:** behaviour when the cursor's entry has been vacuumed or rotated away, and ordering across reboots. Lead L6.
- **Fills:** the `knowledge/drift-pin-r10.md` named blind spot (coverage-map row 18); `SKILL.md:17`; Frontier F3.
- **Recheck (wave 2):**
  1. `C=$(journalctl --user -q -n 1 -o json --output-fields=_BOOT_ID | grep -oE '"__CURSOR":"[^"]+"' | cut -d'"' -f4)`
  2. `journalctl --user -q --after-cursor="$C" MESSAGE_ID=fe6faa94e7774663a0da52717891d8ef -o json --output-fields=MESSAGE_ID | wc -l` → expect 0 immediately.

  A positive control would write a test line with `systemd-cat`. That is a journal write, so the lane decides.
- **Clears QUALITY.md:** #1, #2 and #3 (unknowns named).

### K6 `settlement-vocabulary-cicd-results`

- **Claim:** OTel CI/CD semconv (Release Candidate) defines exactly six well-known results for pipeline runs and for task runs: success, failure, error, timeout, cancellation, skip. The spec has 12 value rows in total (`curl -fsS https://opentelemetry.io/docs/specs/semconv/cicd/cicd-spans/index.md | grep -cE '^\| \`(cancellation|error|failure|skip|success|timeout)\` \|'` → 12). It separates `error` (CI system fault, e.g. a killed worker) from `failure` (tool non-zero exit). No value means "unsettled", because a result exists only once a run ends. That matches mori's rule to age an unsettled wave and never call it failed (`SKILL.md:27`).
- **Opinion (QUALITY #1 label):** a lane or wave whose process was OOM-killed maps to `error`, not `failure`.
- **Source and quote:** S022 `error` row: "The pipeline run failed due to an error in the CI/CD system, eg. due to the worker being killed."
- **Fills:** `SKILL.md:16` "Did a wave settle?" vocabulary; Frontier F6.
- **Recheck:** the `curl | grep -c` above; on-release.
- **Clears QUALITY.md:** #1 (the mapping is labeled opinion; the facts are falsifiable) and #2.

## 5. Paths

- **kill-event attribution — S003 → S004 → S002 → S013 → S015 → S014 → S011 → S016.** Start at the kernel's single increment and print sites, then the counters they feed and their scope, then the journal keys that carry identity, then query mechanics. End with the userspace killers that bypass the counters.
- **pressure as runway — S001 → S002 → S010 → S008 → S007 → S021 → S029.** The kernel interface first (averages, totals, triggers, per-cgroup files). Then how systemd consumes it (2 s windows; full avg10 60% for 30 s), then the BPF-OOM frontier. Last, the saturation and prediction framing that justifies runway rows.
- **agent-fleet telemetry vocabulary — S029 → S028 → S022 → S024 → S023 → S025 → S026.** Principles (symptom/cause), then probe-state vocabulary (startup, liveness, Unknown), then settlement results, then agent spans. Then the network-free artifact and the shell emitter. Close with why a collector adds no PSI.

## 6. Rejected candidates (kept as evidence of taste)

- **R1 — eBPF kill attribution inside the census** (`oomkill.bt`, `killsnoop.bt`, `signal:signal_generate`).
  - bpftrace is absent on the host (§0).
  - eBPF needs privilege `[INFERENCE; L7]`.
  - A resident tracer contradicts the gate's "one process, no resident sampler, no state file" (`lessons/2026-10-15-free-lunch-measurements-counter-baselines.md:22-23`).
  - `killsnoop.bt` probes only kill/tkill/tgkill ("Trace signals issued by the kill(),tkill(),tgkill() syscall.", S020 header). It cannot see oomd's `cgroup.kill` path (S011 `:274`) `[INFERENCE]`; `signal_generate` (S006) would.
  - Kept as frontier knowledge (F5).
- **R2 — PSI trigger watcher as a census probe.**
  - "The trigger will de-register when the file descriptor used to define the trigger is closed." (S001, "Monitoring for pressure thresholds").
  - "Unprivileged users can also create monitors, with the only limitation that the window size must be a multiple of 2s" (same section).
  - Event-driven pressure is a resident instrument with its own contract, not the census. Supervising one is kumitate's or the operator's job. Frontier F4.
- **R3 — windowed `memory.peak` via the fd-local reset** (S002: "A write of any non-empty string to this file resets it to the current memory usage for subsequent reads through the same file descriptor.").
  - It needs a write to a cgroup control file, which breaches "live mode writes nothing" (free-lunch lesson `:23`).
  - A 2026 patch thread reports resets clobbering other fds' watermark (L1, unopened). Not relied on.
- **R4 — OTel Collector `hostmetrics` as the runway source.** None of its 11 scrapers reads PSI (`curl -fsS …/hostmetricsreceiver/README.md | grep -cE '^\| \[[a-z]+\] +\|'` → 11). It adds a resident daemon at a 1m default interval to obtain less than one read of `/proc/pressure/*` gives.
- **R5 — learned or auto-tuned thresholds.** The lane forbids "tuning a labeled-local threshold to fit one observation" (`SKILL.md:18`). SRE ch. 6 (S029): "We avoid "magic" systems that try to learn thresholds or automatically detect causality."
- **R6 — pidfd-based watchdog liveness in the census.** A pidfd's value (exit notification, reuse-proofing; S027: readable "(EPOLLIN)" on termination) needs the fd held over time. The one-shot census's pid + start time (`SKILL.md:15`) is the stateless equivalent. Kept for any future resident watcher.
- **R7 — S030 OneUptime blog as a source.** Tier C, restatement only; reason recorded in its row.

## 7. Mistakes mined

| # | class | evidence | captured already? (sweep) | proposed criterion |
|---|---|---|---|---|
| M1 | lexical sweep false positive (`cursor` ⊂ `precursor`) — my own | first combined sweep hit 3 files via "precursor"; `\bcursor\b` → 0 (§1b) | no — `grep -ciE 'word.?boundary\|false positive' corpus/QUALITY.md` → 0 | "A sweep's nonzero hits are inspected before the count is cited; regexes use word boundaries" |
| M2 | text grep vs structured field | `r1:150` "Segfaults are a structured field, not a word."; the OneUptime recipe (S030) repeats the mistake for oomd | partly: r1 erratum, not a criterion — `grep -c 'structured' corpus/QUALITY.md` → 0 | "A journal class is counted by `MESSAGE_ID` or trusted field when one exists" (K3) |
| M3 | notice ≠ event (unit fan-out) | 5 kernel kills vs 7 + 9 `fe6faa94…` notices, boot `7bd93aee…` (§0) | no — `grep -rhiE 'fan-?out\|per.unit' $F \| wc -l` → 0 | "A kill count names its unit (kill vs notice) and its journal scope; scopes are never summed" |
| M4 | doc wording read as wider than code | S002 "killed by any kind of OOM killer" vs S003 `:935-936` single site | no — `grep -rhiE 'any kind of OOM' $F \| wc -l` → 0 | "A counter's semantics cite its increment site, not only its doc line" (K1) |
| M5 | tracer scope narrower than the event | S020 probe list vs S011 `:274` `cgroup.kill` | partly, as practice rather than criterion: 6 lines already state instrument blind spots — `grep -rhiE 'delivery path\|cannot see' $F \| wc -l` → 6 (e.g. `knowledge/drift-pin-r10.md:284`, `knowledge/surfaces-r8.md:91`, `SKILL.md:162`, `lessons/2026-10-15-run-order-spoofing-shuffle-nonce-limits.md:190-191`). None covers kill-delivery paths: eBPF terms → 0 (§1b) | promote the practice to a criterion: "A detection recipe states which delivery paths it cannot see" |
| M6 | post-hoc attribution by re-reading a dead cgroup | `r1:143-144` "cgroup path now `ENOENT`" | partly, r1 erratum only — `grep -rhiE 'ENOENT' $F \| wc -l` → 1 | "Attribution comes from records written at event time (K2), never from re-reading the victim's cgroup" |

## 8. Defects found (contract, read-only)

- D1 — no `## Frontier` in `corpus/README.md`: `grep -cE '^## Frontier' corpus/README.md` → 0.
- D2 — no Core/Frontier/Adjacent headings in `PROVINCE.md`: `grep -cE '^#+ (Core|Frontier|Adjacent)' PROVINCE.md` → 0.
- D3 — 5 corpus files missing from the coverage map: `audit-r11.md`, `lane-silence-r2.md`, `lessons/…free-lunch…`, `lessons/…oracle-honesty-crash-masking…`, `lessons/…settle-evidence-references-with-artifacts…`. Command: ``for f in corpus/knowledge/*.md corpus/lessons/*.md; do grep -qF "\`${f#corpus/}\`" corpus/README.md || echo "unindexed: $f"; done``.
- D4 — `QUALITY.md` has 5 criteria and none on source tier, recheck or verified-at (→ 0, §1a).
- D5 — no source registry: 1 external URL across the whole corpus (§1a), and there is no `corpus/SOURCES.md` (corpus listing: `README.md QUALITY.md knowledge/ lessons/ evidence/`).
- Scope note, not a defect: `PROVINCE.md:8` scopes kill classes to `journalctl --user`, while K2's evidence lives in the system journal (`corpus/README.md:266-268` already names this).

## 9. Proposed `## Frontier` rows (for wave 2)

| id | frontier | first evidence | boundary |
|---|---|---|---|
| F1 | userspace OOM killers (systemd-oomd xattrs and `d989611b…`; earlyoom `sending SIG…` lines) | K1, K3, K4; S007, S011, S016 | report `unavailable (inactive)` on this host; enabling is operator/tsukuroi |
| F2 | kernel OOM attribution from the system journal, shape-validated tokens only | K2; S003, S004, S014 | never echo MESSAGE (`SKILL.md:131-145`) |
| F3 | new-since-pin kill counts through journal cursors | K5; S014, S015 | read-only; the cursor lives in the pin baseline |
| F4 | event-driven pressure (PSI triggers, systemd PressureWatch); CPU/IRQ PSI rows (free one-read signals, 0 lines held, §1b); system CPU `full` is always 0 (S001: "CPU full is undefined at the system level, but has been reported since 5.13, so it is set to zero for backward compatibility.") | S001, S002, S010 | a trigger watcher is resident (R2); the CPU/IRQ rows fit the census |
| F5 | eBPF kill and OOM tracing (`signal_generate`, `mark_victim`, `oomkill.bt`) | S005, S006, S017–S020 | privileged; pin bpftrace version; knowledge only (R1) |
| F6 | agent-workload telemetry (GenAI agent spans, CI/CD results, OTLP files, otel-cli) | K6; S022–S026 | consume-only; emission in lanes belongs to kumitate and the lanes |
