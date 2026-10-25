# ProviderSecrecy — secret/session exposure of planned mori commands

Advisory only. Not a gate verdict, lane-round report, receipt, or admission. Named targets were not opened.

measured_at=2026-10-14T21:40:37-03:00
boot_id=d7f0bc8d-938e-4249-b4a1-f250cbfacf58
command=shape probes below; no `cat`/`jq`/`json.loads`/`sqlite3` of the named targets

## Severity

**High.** Two planned command forms can put secret-shaped journal text or a session payload on a receipt. The landed count-only stdout did not. That is not the same as "cannot print".

Named paths `credentials/`, `oauth/`, `server.token`, and `op.env` do not appear as open targets in the planned argv. That absence is not a license to add a walk, an override, or a `/proc` fd read.

## Exploit path

1. Contract probe and GateDesign `probe_journal` run `journalctl --user -b --no-pager` (`GateDesign.md:379-392`). Default short format prints `MESSAGE`. `cap()` stores that stdout in `CAP_OUT` (`GateDesign.md:241-246`).
2. This boot's user journal has `MESSAGE` lines whose identifier is `1password` or `gnome-keyring-daemon` and whose body contains an opaque run longer than a UUID. A receipt, a `bash -x` trace, or `-o cat` / `-o short-iso` prints those runs. CensusIdempotence already traces with `set -x`.
3. Separately, `omp` holds 51 readable fds whose targets are `~/.omp/agent/sessions/*.jsonl`. `cat /proc/<omp-pid>/fd/<n>` content-reads a session payload. The contract's `ps`/`/proc` wording does not name that fd, and the landed script does not open it. An unconstrained `/proc` walk does.
4. `read_file` of `MORI_CGROUP_CURRENT` interpolates the first line into the surface row (`GateDesign.md:248-251`, `:437`; live stdout field `current=`). Pointing that override at `server.token` prints the file. Default path does not.

## Evidence

Observation / inference / unknown stay separate. No named target was opened. `lstat` only.

### Named targets — not content-read

| Target | Shape at measurement | Opened by a planned argv? |
|---|---|---|
| `~/.kimi-code/credentials` | dir, mode 0700 | no |
| `~/.kimi-code/oauth` | dir, mode 0755 | no |
| `~/.kimi-code/server.token` | regular file, mode 0600, 43 bytes | no |
| `~/.config/the-janitor/op.env` | absent | no |
| `~/.omp/agent/sessions` | dir, mode 0755; 318 `*.jsonl` names, contents not read | no |
| `~/.kimi-code/sessions` | dir, mode 0700; not listed, not read | no |
| `~/.local/state/the-janitor/session-id` | absent | no |
| `~/.local/state/the-janitor/xdg-data/opencode/opencode.db` | absent | no |

Command: `lstat` on those paths; `find -P ~/.omp/agent/sessions -name '*.jsonl' -printf` count only. No `readdir` of `credentials/` or `oauth/`. No hash.

`find -P` of `.ufo/` and each `*-shokunin` checkout: `protected_symlink_hits=0`. No tracked or on-disk name `credentials`, `oauth`, `server.token`, or `op.env` under those trees. Two lane files match `*session*.jsonl` by name only (`game-dev-3d-shokunin/corpus/live/r83-simplifier/lsp_refs_r83_session{2,3}.jsonl`). Not opened. Not the omp session store.

### JOURNAL_MESSAGE_PRINT — exclude

Command measured: `journalctl --user -b --no-pager -o json --output-fields=MESSAGE,SYSLOG_IDENTIFIER` piped to a counter. Counts only. Lines not printed.

| Observation | Count |
|---|---|
| User-journal entries this boot | 9141 (later recount 8747 after the boot continued; same boot_id) |
| `MESSAGE` with an opaque run of 32+ characters | 594 |
| Of those, run longer than a UUID (36) | `1password` 221, `systemd-coredump` 29, `gnome-keyring-daemon` 2, `chrome` 7, `sudo` 5, others in the counter |
| `1password` lines that also contain the word token, password, secret, or authorization | 13; max opaque length 38 (4 lines) and 56 (9 lines); UUID-only = 0 |
| Those 13 also matching oom/segfault/`EXIT_CODE=killed` | 0 |
| `$(` or backtick in any `MESSAGE` this boot | 0 |

**Inference:** `journalctl --user -b` default short, `-o cat`, `-o short-iso`, `-o verbose`, `-o export`, and `-o json` that includes `MESSAGE` can print a token. The property "cannot print a token" is false for those forms.

**Unknown:** whether each opaque run is a credential, an item id, a build-id, or a path fragment. Not resolved. Must not be resolved by printing the line.

Today's three kill-class lines are systemd catalog templates (`CODE_FUNC=unit_log_failure` / `unit_log_process_exit`, `EXIT_CODE=dumped`). Redacted shape only: unit failure `oom-kill`, process `code=dumped, status=11/SEGV`, unit failure `core-dump`. No opaque run. A narrow class grep does not select the 13 `1password` lines today. The command still prints `MESSAGE`, so a later matching line can carry a token.

KillEventsJournal already ran `journalctl --user -b --no-pager -o cat EXIT_CODE=killed` and `journalctl --user -b --no-pager -o short-iso -g …`. Those print `MESSAGE`. Exclude them from the gate and from any receipt paste. OomClassTaxonomy's planned "verbatim signatures" is the same exclude.

GateDesign live stdout at `/tmp/mori-idem-census/landed/liveb.out` (ts inside the file `2026-10-15T00:37:57Z`) emits counts only (`oom_kill=1`, `unit_failure=2`). It does not contain the identifier `1password` or `server.token`. **Observation:** that receipt did not print a token. **Inference:** the `cap` form can still print one under `set -x`, because `CAP_OUT=$(journalctl …)` puts `MESSAGE` in a shell variable the trace expands.

Scratch draft `/tmp/mori-idem-census/mori-census.sh:202` and `:208-221` is worse: it feeds `$out` through an unquoted heredoc, so a future `$(…)` in `MESSAGE` executes as the census user. Substitution count this boot is 0, so that exec path is latent, not live. Do not land that draft. The parent script is the one in `GateDesign.md`.

### PROC_ENVIRON_TOKEN — exclude

Command: read `/proc/<pid>/environ`, count key names and value shape, print neither values nor prefixes.

| comm | key | value shape | processes |
|---|---|---|---|
| omp | `HL_INITIAL_WORKSPACE_TOKEN` | opaque, length 36 | 8 |
| bash | `HL_INITIAL_WORKSPACE_TOKEN` | opaque, length 36 | 7 |
| python3 | `HL_INITIAL_WORKSPACE_TOKEN` | opaque, length 36 | 3 |
| python | `PI_TOOL_BRIDGE_TOKEN` | opaque, length 36 | 9 |
| watchdogd | environ | unreadable | 1 |

`ps e`, `ps eww`, `ps auxe`, and `tr < /proc/<pid>/environ` print those values. The landed script does not run them. It runs `pgrep -af shokunin-watchdog` and emits `pids=` count only (`GateDesign.md:273-277`, `:316`).

`/proc/*/cmdline` token-pattern hits this boot: 0 of 599 readable cmdlines. **Inference:** `pgrep -af` does not currently print a token. It can, if a later argv contains one. Do not paste `pgrep -af` stdout. Prefer `pgrep -x` or `ps -o pid=,comm=`.

### PROC_FD_SESSION — exclude

Command: `readlink` of `/proc/<pid>/fd/*`, class by path suffix, `access(R_OK)` only. Targets not opened.

`fd_class_counts=omp_session_jsonl:51`, all `comm=omp`, all readable by this uid. No fd target was `server.token`, `op.env`, `credentials/`, `oauth/`, or `opencode.db`.

**Inference:** `cat /proc/<omp-pid>/fd/<n>` content-reads a session payload. `ls -l /proc/<pid>/fd` prints the session path. Neither is in the landed argv. Both are in scope for a literal `ps`/`/proc` census. Exclude them.

### CGROUP_OVERRIDE_ECHO — exclude the override, keep the default

Default files, `lstat` plus a numeric-shape read (these are not the named targets):

| Path | kind | mode | numeric shape |
|---|---|---|---|
| `/sys/fs/cgroup/user.slice/user-1000.slice/memory.events` | file, not a symlink | 0444 | yes (`key N`) |
| `…/memory.current` | file | 0444 | yes |
| `…/memory.max` | file | 0644 | yes |
| `/proc/meminfo` | file | 0444 | yes; defined as `MORI_MEMINFO` and not read by the probe functions |

`df -P` prints filesystem columns, not file bytes. `tmux ls` is captured and the script emits `sessions=` count only. `git -C <repo> log -1 --format=%ct` emits an epoch. `find` uses `%T@` or `[ -f ]` on wave json names. None of these content-read the named targets.

`MORI_CGROUP_CURRENT` / `MORI_CGROUP_EVENTS` are honored in live mode. `read_file` prints the first line into the surface row. That is the content-read switch. `MORI_JOURNALCTL_BIN` can be any executable; its stdout is grepped, not blindly echoed, so it is a weaker form of the same hole.

## Impact

A parent that pastes `journalctl --user -b`, lands the `cap` form and traces it, or runs the census with `MORI_CGROUP_CURRENT` aimed at `server.token`, writes secret-shaped bytes into a wave receipt. A `/proc` fd read of `omp` loads operator session jsonl into the census process. The live count-only receipt already on disk does not do this. The named directories were not walked.

## Smallest remediation

Do not edit the gate in this seat. Parent excludes the printing forms before landing `tools/mori-census.sh`.

Exclude:

| Command | Why |
|---|---|
| `journalctl --user -b` and any `-o cat\|short\|short-iso\|verbose\|export\|json` that keeps `MESSAGE` | prints the `1password` / `gnome-keyring-daemon` runs |
| `journalctl … -o cat EXIT_CODE=killed` and `journalctl … -o short-iso -g …` | same; already used by KillEventsJournal |
| verbatim journal signatures in a receipt | OomClassTaxonomy prompt |
| `CAP_OUT=$(journalctl --user -b --no-pager)` under `set -x` or an unquoted heredoc | trace or expansion prints or executes `MESSAGE` |
| `/tmp/mori-idem-census/mori-census.sh` journal function | unquoted `$out` heredoc; do not land |
| `ps e` / `ps eww` / `ps auxe` / `/proc/<pid>/environ` | prints opaque `*_TOKEN` values |
| `cat /proc/<pid>/fd/*`, `ls -l /proc/<pid>/fd` | session-payload content-read or path disclosure |
| `cat` / `jq` / `json.loads` / `sqlite3` of `credentials/`, `oauth/`, `server.token`, `op.env`, `~/.omp/agent/sessions/*.jsonl`, `~/.kimi-code/sessions/`, `opencode.db` | named-target content-read |
| live `MORI_CGROUP_CURRENT`, `MORI_CGROUP_EVENTS`, `MORI_MEMINFO`, `MORI_JOURNAL_FILE` outside an allowlist | turns `read_file` into a secret printer |
| `tmux capture-pane`, `tmux show-environment`, `tmux show-buffer` | session payload; not in the planned argv |

Keep, stdout already closed or metadata-only:

- journal class counts from a pipe whose stdout is only `oom-kill`, `sigkill`, `segfault`, `unit-failure`, and an integer. The shell must never see `MESSAGE`. Do not run that pipe under `set -x`.
- `pgrep -x` or `ps -o pid=,lstart=,comm=` for the watchdog. `pgrep -af` only if the receipt keeps the count.
- `stat` of `.ufo/watchdog.log`; `find` count of `.ufo/state/*.round`.
- `[ -f ]` plus mtime on `.ufo/waves/*/{swarm-registry,dispatch,run,results,closeout,task-response,mission-result}.json`. Do not `cat` or `jq` them. Six older wave markdown seats contain `op://` or assignment-shaped text; a body dump reprints that.
- `cat` of the default `memory.events` / `memory.current` only. Refuse the path unless it stays under `/sys/fs/cgroup/`.
- `df -P` on the fleet root and `/tmp`.
- `git -C <repo> log -1 --format=%ct` and `find -printf '%T@'`. Not `git show`, not `git log -p`.
- `tmux ls` reduced to a session count.

Shape-only, if a later round must mention the named files: `lstat` mode and size. No hash, no `find` inside `credentials/` or `oauth/`, no byte read.

## Unresolved

Whether the 221 `1password` opaque runs and the 2 `gnome-keyring-daemon` runs are credentials or ids. Left unknown on purpose.

`op.env` is absent, so a content-read would fail closed today. The exclude still stands.

A leak scan that prints `MESSAGE` to prove a token is not a shape-only measurement. It stays out of this wave. Owner: kagi, operator-present, not this seat.
