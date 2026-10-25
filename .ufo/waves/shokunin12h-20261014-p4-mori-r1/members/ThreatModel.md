# ThreatModel — census secret leak and accidental action

**Seat:** ThreatModel (sentinel leaf) · **Wave:** `shokunin12h-20261014-p4-mori-r1`  
**Lane:** `mori-shokunin` · **Round:** probation 1 · **Not a verdict.** Parent integrates. This seat did not edit the gate.

**Question.** Can a mori probe leak a secret through journal or `/proc` output, and can a census command act (a side effect) while claiming to be read-only?

**Short answers.**

1. **The pinned gate's own stdout does not print journal lines, cmdline, or environ.** A re-run of the command it publishes, or a `bash -x` trace of `cap()`, does. The user journal on this boot holds secret-shaped opaque runs. `/proc/<pid>/environ` and session fds are readable by this uid and are not opened by the gate; the wave contract's `ps`/`/proc` wording does not forbid them, and one member already opened environ.
2. **Default live argv does not kill, restart, fetch, or eval.** Accidental action is real on the override paths the design documents (`MORI_*_BIN`, unquoted `MORI_DISK_TARGETS`) and on `--selftest`'s scoped `rm -rf`. It was not observed on the default git/df/tmux path on this host.

## Pin and method

| Item | Value |
|---|---|
| Gate scored | `mori-shokunin/tools/mori-census.sh` |
| sha256 | `81e716de978a9540f9d310309d83660bb196650aa1ab809ae6fd6ee3cc4bfba9` |
| Lines | 885, re-read after the hash (call sites below matched that read) |
| Shape counts | `2026-10-15T00:44:33Z` |
| Code re-read | same UTC hour, after the hash; the file moved during the wave (several hashes). Line numbers are the post-hash read. |

The gate was edited while this seat was reading it. Behaviors below were true on the pin: counts-only journal stdout, a second live `journalctl -o json`, a `/sys/fs/cgroup/*` string check, unquoted target/lane loops, `MORI_*_BIN` honored in live mode, no `set +o xtrace`, no unquoted heredoc.

**Not opened.** `credentials/`, `oauth/`, `server.token`, `op.env`, session `*.jsonl` contents, `/proc/<pid>/environ` values, journal `MESSAGE` text. Counts and key lengths only. No live `bash tools/mori-census.sh`. No `--selftest` (it writes `/tmp`). No instruction-shaped artifact text was followed.

**Same-user is not a privilege expansion.** This uid can already run `journalctl --user` and read its own environ. The boundary that matters is the census artifact (stdout, committed notes, wave reports) and any command that mutates or execs.

## What the default live run actually executes

Fresh `bash tools/mori-census.sh` resolves `pgrep`, `df`, and `sort` to `/usr/bin` (procps-ng 4.0.7, GNU coreutils 9.11). The tool shell's builtins (`pgrep 0.2.0`, `df 0.8.0`) are not what the script runs. Do not "fix" the gate against those builtins.

| Probe | Argv on the pin | Printed |
|---|---|---|
| watchdog | `pgrep -af shokunin-watchdog`; `stat` mtime; `find` of `*.round` | pid **count**, path, age |
| waves | `find` + `grep -q` for a closed-token | counts; wave basename in a finding |
| journal | `journalctl --user -b --no-pager`, then (live only) `-o json COREDUMP_SIGNAL=11` | class **counts** |
| cgroup | `awk`/`head` of `memory.events` and `memory.current` | numeric fields; first line of `memory.current` |
| disk | `df -P` per target | sizes; raw line only on parse failure |
| silence | `git -C <repo> log -1 --format=%ct`; `find` mtimes | epochs stay internal; finding has lane id and epochs |
| tmux | `tmux ls` | session **count** |

Absent from the file: `eval`, `source`, `systemctl`, `pacman`, `curl`, `wget`, a `kill` invocation, `export` of `CAP_OUT`, `set -x`, `set +o xtrace`, unquoted `<<EOF`. The word `kill` appears in comments and finding ids only.

`cap()` (`tools/mori-census.sh:152-157`) is `CAP_OUT=$("$@" 2>&1)`. Journal text becomes a shell variable. It is not exported, so it is not in the census process's `/proc/self/environ`. `ptrace_scope` is `1`, so a sibling process cannot read that variable out of `/proc/<pid>/mem`. The parent, and `xtrace`, can.

## Risks

### R1 — xtrace prints the journal body the gate stored

**Severity:** high when xtrace is on; not the default path (`SHELLOPTS` here has no `xtrace`; `BASH_ENV` unset).  
**Exploit path.** `bash -x tools/mori-census.sh`, or `SHELLOPTS=xtrace` inherited from the parent. `cap()` assigns the full `journalctl` stdout to `CAP_OUT`. Bash traces that assignment.

Proof, synthetic, not a credential:

```text
bash -x -c 'CAP_OUT=$(printf %s FIXTURE_OPAQUE_NOT_A_SECRET); true'
+ CAP_OUT=FIXTURE_OPAQUE_NOT_A_SECRET
```

**Evidence.** `cap()` at `:152-157`. First journal call at `:317`: `cap "$JOURNALCTL_BIN" --user -b --no-pager`. No `set +o xtrace` anywhere in the file.  
**Impact.** Stderr receives every user-journal line this boot, including the opaque runs in R2. A harness that stores stderr stores them.  
**Mitigation in the design.** stdout findings are `count=` only. That mitigation does not cover xtrace.  
**Smallest remediation.** `set +o xtrace` as the first executable line, and do not assign the journal body to a variable: pipe `journalctl` straight into `grep -c`.

### R2 — the published command is an unfiltered journal dump

**Severity:** medium.  
**Exploit path.** The surface line prints `cmd=journalctl --user -b --no-pager`. The corpus receipt copies that command. An operator or a later agent re-runs it and gets `MESSAGE`.

**Evidence, shape only, `2026-10-15T00:44:33Z`.** `journalctl --user -b --no-pager -o json --output-fields=MESSAGE,SYSLOG_IDENTIFIER,_COMM`. No line printed.

| Observation | Count |
|---|---|
| Entries | 9166 (rc 0, stderr empty) |
| `$(` or backtick in `MESSAGE` | **0** |
| Opaque run of 32+ characters **and** a gate class regex on the same `MESSAGE` | **0** |
| `1password` entries with an opaque run | 245 / 325 |
| `gnome-keyring-daemon` entries with an opaque run | 2 / 2 |
| `systemd-coredump` entries with an opaque run | 115 / 1051 |
| Also present | `chrome` 7, `sudo` 6, `pipewire` 42, desktop generators |

Whether each opaque run is a credential, an item id, or a path fragment is **unknown**. It was not resolved by printing the line. Named receipts (`corpus/knowledge/observability-census-r1.md`, `/tmp/mori-idem-census/landed/liveb.out`) do **not** contain the identifier `1password`. The gate's own past stdout did not paste those lines.

**Mitigation in the design.** `grep -ciE` counts; findings interpolate `count=`, not `$text`. `--user` keeps the read on this uid's journal (the system journal is a larger, other-user surface; do not drop `--user` to "see more segfaults"). `--no-pager` is passed (`journalctl --help` lists it as "Do not start a pager").  
**Smallest remediation.** Publish the count pipeline as `cmd=`, not the raw dump. If a killed pid is required (`SKILL.md:27`), extract a `[0-9]+` only. Do not add CorpusMap `sample_lines` or OomClassTaxonomy "verbatim signatures" to the gate.

### R3 — live mode loads full coredump JSON into a shell variable

**Severity:** medium (memory and xtrace), not current stdout.  
**Exploit path.** When `MORI_FIXTURE` is unset, `:335` runs a command substitution that calls `cap` on `journalctl --user -b --no-pager -o json COREDUMP_SIGNAL=11` and then `grep -c` on `CAP_OUT`. `-o json` with no `--output-fields` is the whole record. xtrace prints it. The subshell discards it after the count, so the parent `CAP_OUT` stays the short journal from `:317` until a later `cap()` overwrites it.

**Evidence.** One record, keys and lengths only, not values: `COREDUMP_CMDLINE` str_len=136, `COREDUMP_OPEN_FDS` str_len=334, `COREDUMP_PROC_STATUS` str_len=1539, `MESSAGE` str_len=884, `COREDUMP_ENVIRON` null in that one record. Full signal-11 stream: 7,850,818 bytes, 656 lines. Not scanned for non-null `COREDUMP_ENVIRON` across the 656. **Unknown** whether other records carry environ.  
**Mitigation in the design.** The result that escapes the substitution is a count. There is no field allowlist.  
**Smallest remediation.** Count with `--output-fields=COREDUMP_SIGNAL` only, and do not store the stream.

### R4 — `/proc` leak is in the contract, not in the gate argv

**Severity:** high if a probe follows `ps`/`/proc` literally; **not present** in the pinned gate.  
**Exploit path.** `ps e` / `ps eww`, reading `/proc/<pid>/environ`, or `cat /proc/<pid>/fd/<n>` where the fd points at a session jsonl. `ls -l /proc/<pid>/fd` prints the path even without reading the file.

**Evidence.** Gate uses `pgrep -af` and emits `pids=` (`:184`, surface detail). This seat did not read environ values.

| Surface | Measured `2026-10-15T00:44:33Z` | Gate opens it? |
|---|---|---|
| `/proc/<pid>/cmdline` secret-shaped (`bearer`, `api_key`, `password=`, `sk-`, `ghp_`, …) | 0 / 584 readable | read by `pgrep -af`, count only |
| cmdline containing `shokunin-watchdog` | 0 | same |
| `/proc/<pid>/environ` readable | 95 readable, 489 not | **no** |
| fd target `sessions/*.jsonl` | 26 (readlink only, not opened) | **no** |
| fd target `server.token` / `op.env` / `credentials/` / `oauth/` | 0 | **no** |
| `/proc` mount | `rw,nosuid,nodev,noexec,relatime` — no `hidepid` | — |

`DiskRunway.md` reports reading `/proc/<pid>/environ` for `TMPDIR` presence (97 readable, key unset). That is a census-practice open, outside the gate. ProviderSecrecy counted token-shaped environ **keys** and did not print values; this seat did not repeat that read.

**Mitigation in the design.** Closed argv: no `environ`, no `fd`, no `mem`, no `maps`. There is no denylist, so the next probe can add one. `MEMINFO` defaults to `/proc/meminfo` (`:74`) and is never read. Dead config, not a leak, not a control.  
**Smallest remediation.** In the skill and the gate header, deny `/proc/<pid>/{environ,fd,mem,maps,cwd}` and `ps e`. Allow pid, comm, and a count. Never paste `pgrep -af` stdout.

### R5 — cgroup "outside sysfs" check is a string prefix, not a path

**Severity:** medium. Same-user read, artifact exfiltration.  
**Exploit path.** `MORI_CGROUP_CURRENT` is echoed by `read_file` (`head -n1`) into `current=` on the surface line. The guard is a glob, not `realpath`:

```text
case "$CGROUP_CURRENT" in
  /sys/fs/cgroup/*) cur=$(read_file "$CGROUP_CURRENT") ;;
  *) cur='refused:outside-sysfs-cgroup' ;;
esac
```

(`tools/mori-census.sh:407-409`.)

The glob is not `realpath`. Proof, no file read:

```text
p=/sys/fs/cgroup/../../etc/passwd
case match: CASE_MATCH
realpath -m /sys/fs/cgroup/../../../etc/passwd → /etc/passwd
```

A path that string-matches `/sys/fs/cgroup/*` and then `..` out of that tree is read, and its first line is printed. Default path is `memory.current` (a byte counter). This seat did not point the override at a token file.

`MORI_CGROUP_EVENTS` / `MORI_CGROUP_LOCAL_EVENTS` are not fully echoed; `cgroup_field` prints only `oom_kill`/`oom`/`high`/`max`. A secret file that does not have those keys does not leak through that awk. The path string is still printed on the unavailable branch.

**Mitigation in the design.** The prefix case is a real refusal for a path that does not start with `/sys/fs/cgroup/`. It is not an allowlist. GateDesign.md:92 says "path allowlist"; the script has no allowlist function.  
**Smallest remediation.** `realpath -e` and require the canonical path to stay under `/sys/fs/cgroup/` and to be named `memory.current` or `memory.events`. Refuse if the string contains `..`. Do not read on failure.

### R6 — live mode will execute `MORI_*_BIN`

**Severity:** high if the environment is hostile; medium as an operator footgun.  
**Exploit path.** `export MORI_JOURNALCTL_BIN=/some/executable` then a live run. `:75-79` apply the override in every mode. `cap()` runs that path with fixed trailing args (`--user -b --no-pager`, and the json argv). The binary can ignore the args. This is not shell injection: a value containing `; rm` is looked up as a command name, not evaluated. The binary itself is the act.

Selftest sets these on purpose under `env -i` (`:680`). Live mode does not clear a leftover export from that shell.

**Mitigation in the design.** Trailing argv is fixed. No basename check. Documented as "selftest / operator pin".  
**Smallest remediation.** In live mode, ignore `MORI_*_BIN` unless `MORI_ALLOW_OVERRIDES=1`. Reject basenames `kill`, `pkill`, `killall`, `systemctl`, `pacman`, `curl`, `wget`, `ssh`, `nc`, `bash`, `sh`.

### R7 — unquoted targets can `df` or `find` somewhere else

**Severity:** low on the default; medium with a hostile or globbed override.  
**Exploit path.** `:434` `for t in $DISK_TARGETS` and `:495` `for lane in $ROSTER_LANES` are unquoted. Word-split and glob run. A `MORI_DISK_TARGETS` of `*` iterates matches and `df`s them. `df` of a path that is an unmounted autofs mount **mounts** it. On parse failure, `:458` prints `line=$line` (the raw df row) into a finding.

**Evidence.** Defaults are `$ROOT` and `/tmp`. `findmnt` at `2026-10-15T00:44:33Z`: `/home` btrfs `rw,relatime`; `/tmp` tmpfs `rw,relatime`. Only autofs target: `/proc/sys/fs/binfmt_misc`. `/scratch` and `/scratch/tmp` absent. Default targets are already mounted. relatime can bump atime on read; that is metadata, not a fleet mutation.  
**Mitigation in the design.** Defaults are local and mounted. No `df -l`, no mountinfo check before `df`.  
**Smallest remediation.** Use an array. Refuse a target that is not already listed in `/proc/self/mountinfo` (do not `stat` an unmounted autofs path). On parse failure emit `df_parse` without `line=`.

### R8 — `--selftest` is the only intentional write, and it is fenced

**Severity:** low.  
**Exploit path.** `:586-587` `mktemp -d /tmp/mori-census-selftest.XXXXXX` and `trap 'rm -rf -- "${work:-}"' EXIT INT TERM`. `work` comes only from `mktemp`. A failed `mktemp` trips `set -e` before the trap. This is not `rm -rf /`. `SIGKILL` can leave the temp dir; its contents are synthetic fixtures, not the host journal.

`fx_no_mutation` hashes the fixture tree, not the rest of the host. A regression that writes outside the fixture is not caught by that hash. `check()` uses `env -i`. `check_cli` does not, and only passes `--help` / `--bogus`, which exit before probes. Top-level `id -u` still runs.

**Mitigation in the design.** Live mode has no redirect to a file. The header claim "live mode creates no files" holds for the script's own writes. GNU `sort` 9.11 can spill to `TMPDIR` if a sort exceeds its buffer. Measured inputs are small: 1339 files under `.ufo/waves`, 13 non-`.git` files in `mori-shokunin`. [INFERENCE] that does not trip the spill. Not measured against a huge lane tree.  
**Smallest remediation.** None required for the default. Optional: compute the newest mtime in `awk` so `sort` never runs.

### R9 — `git log` did not write, on this host

**Severity:** residual. Not observed.  
**Exploit path.** `core.fsmonitor` or `GIT_CONFIG_COUNT` / `GIT_CONFIG_KEY_*` can make a git read-command execute a helper or write a trace file. The gate does not unset those.

**Evidence.** `git -C mori-shokunin log -1 --format=%ct`: index mtime/ctime/size unchanged (`1792025047`, 1249 bytes, before = after). `core.fsmonitor` and `maintenance.auto` are unset on the fleet root and on every `*-shokunin` checkout listed (20 repos). Format is `%ct` only. The pipe in `cap()` is not a tty, so the pager does not start. No `commit`, `status`, `clean`, `reset`, or `push`.  
**Mitigation in the design.** Read-only subcommand, epoch only, not printed as a message.  
**Smallest remediation.** Optional: `git --no-optional-locks -c core.fsmonitor= -c maintenance.auto=false log -1 --format=%ct`. Not a measured defect.

### R10 — `tmux ls` is not `tmux`

**Severity:** low.  
**Exploit path.** Bare `tmux` can create a session. The gate passes `ls` (`:545`) and prints a count, not names. rc ≠ 0 is `unavailable`, not a `new-session`. Socket `/tmp/tmux-1000/default` was present, so this host's run talks to an existing server. This seat did not run `tmux ls`.  
**Mitigation in the design.** Explicit `ls`. Names not interpolated.  
**Smallest remediation.** Keep `ls`. Do not add `tmux new` or `tmux kill-session`.

### R11 — untrusted wave names can forge a report line, not a command

**Severity:** low.  
**Exploit path.** `wave=$base` is unsanitized (`basename` of a directory the census user can create). A newline in the name splits a `FINDING` line. `grep -q` on registry JSON does not print and does not exec. A symlink at `swarm-registry.json` is followed by `[ -f` / `grep -q` (content read, no output).  
**Mitigation in the design.** No `source`, no `jq` eval, no unquoted heredoc in the landed file.  
**Smallest remediation.** Restrict `base` to `[A-Za-z0-9._-]`.

### R12 — scratch draft does not execute journal text

**Severity:** do not treat as RCE. Same xtrace class as R1 if that draft is what gets run.  
**Exploit path claimed elsewhere.** `/tmp/mori-idem-census/mori-census.sh:219-221` is an unquoted heredoc whose body is `$out`. A sibling inferred that a `$(...)` inside `MESSAGE` would run as the census user.

**Falsified.** Synthetic, no journal involved:

```text
out='$(echo MARKER_RAN)'
unquoted <<EOF  →  $(echo MARKER_RAN)
quoted   <<'EOF' →  $out
```

Bash expands `$out` once. It does not rescan the value for command substitution. This boot also has 0 `MESSAGE` values containing `$(` or a backtick, so the latent text is absent as well as non-executing. The draft's `case` arms emit fixed `class=` strings, not the line.  
**Mitigation in the design.** That draft is not `tools/mori-census.sh` (no `<<EOF` in the pin).  
**Smallest remediation.** Do not land the scratch file. The landed gate is the one to fence (R1–R6).

## What not to "fix"

- Do not remove `--user`. That widens the read to the system journal (other users, kernel lines) and is the opposite of a secrecy fix. The coverage gap (user journal vs host segfaults) is real and is not this seat's bug to close by dropping the bound.
- Do not add verbatim journal lines to satisfy `SKILL.md:27` or a corpus `sample_lines` field. Class regex intersection with opaque runs is 0 today; the next matching line can carry one.
- Member `sk-` pattern hits in this wave's reports are the substring inside `task-response`, not tokens. `Bearer`, `ghp_`, and `key=value` scans of `members/*.md` had no hits. Pasted oom lines in sibling reports are unit names (`app-Hyprland-…`, `pipewire-pulse.service`), not credentials. KillEventsJournal withheld an account identifier. That is the right shape rule.
- In-memory possession of the journal during `probe_journal` is not, by itself, an exfiltration. It becomes one under R1 or R2.

## Enforcement the design already has

| Claim | Where it actually holds |
|---|---|
| No remediation verbs | No `kill` / `systemctl` / `pacman` / `curl` / `wget` invocation in the pin |
| Journal content is not acted on | Fixed `grep -ciE` patterns; journal text is the subject, not the pattern; no `eval` |
| Counts, not lines | Journal findings interpolate counts and `rc`, not `$text` |
| `--user` | `:317` and `:335` |
| `--no-pager` | same |
| Cgroup body echo limited | Prefix case `:407-409` (incomplete, R5); default file is a counter |
| Selftest write fence | `mktemp` + trap `:586-587`; fixture hash after each `check` |
| Secret paths not in default argv | No `credentials`, `oauth`, `server.token`, `op.env`, `environ` |

`PROBE_REFUSED` is not a branch in this script. Refusal of restart, fetch, and secret paths is absence of the verb, plus the incomplete cgroup prefix. A new `cap` line is enough to break that.

## Smallest fence for the parent

Do not patch in this seat. If the parent touches the gate, the fence that closes the measured holes without widening the read is:

1. `set +o xtrace` first. Never assign journal or coredump JSON to a shell variable.
2. Coredump count uses `--output-fields=COREDUMP_SIGNAL` only.
3. Printed `cmd=` is the count pipeline.
4. `realpath` allowlist for cgroup files; refuse `..`.
5. Live mode ignores `MORI_*_BIN` unless `MORI_ALLOW_OVERRIDES=1`, and rejects act-binary basenames.
6. Arrays for disk targets and lane ids; no `df` of a path that is not already mounted.
7. Skill text: pid digits only; never paste `MESSAGE`, `pgrep -af`, or `/proc/<pid>/environ`.

That set does not remediate the host. It stops the census from becoming the leak or the actor.
