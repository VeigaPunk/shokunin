# BoundaryRefusal — what mori refuses, and where that refusal is enforced

**Member:** BoundaryRefusal (sentinel) · **Wave:** shokunin12h-20261014-p4-mori-r1
**Lane:** mori-shokunin (shonen probation r1) · **Axes:** coverage · operability · calibration
**Measured:** 2026-10-14T21:35:14-03:00 (`date -Is`)
**Scope:** advisory only. This report does not remediate, dispatch, or claim a census verdict.
**Not a judge verdict.** Unjudged fleet wave.

## Calibration of "enforced"

Three strengths, used exactly:

| Strength | Meaning |
|---|---|
| **closed-set** | The executable census never contains the forbidden verb. Adding it requires editing the script. This is the mechanical point. |
| **policy** | Written refusal in SKILL / PROVINCE / MINT / wave contract / roster scan. A cold agent can route on it; nothing executes it. |
| **gap** | Named hole. A later run must not treat the prose as a proof. |

The executable point is `mori-shokunin/tools/mori-census.sh` (untracked, mode `0755`, 30584 bytes, sha256 `32f804a37aebc47c1865fa124e8fe023c8ed13890d54ccea479197789ecf3047`, mtime `2026-10-14 21:35:01 -0300`). Lane HEAD is still seed `27acf40` (`git -C mori-shokunin rev-parse HEAD`); `git status --short -- tools` → `?? tools/`. The script is **not** the GateDesign fence byte-for-byte (fence sha256 prefix `ad52f5c91d0691cb`, landed prefix `dd939ec83775bf0b`). The only diff is the `--selftest` freshen opt-out (`SKIP_FRESHEN`) so stale fixtures can fire. Live probe bodies are the fence.

`PROBE_REFUSED` (`FindingIds.md:190`) is a vocabulary id, not a branch in the script. `grep` of the landed file for `refus|allowlist|deny|credential|oauth|server.token|op.env` returns **zero** lines. Enforcement is absence of the verb, not a reject path.

---

## 0. What mori refuses (the set)

The five named refusals, plus the adjacent ones the design actually states. Each row's enforcement point is proved below.

| # | Refusal | Owner of the refused act | Design strength |
|---|---|---|---|
| R1 | No restart, kill, reparent, renice, delete, resize | operator (and tsukuroi for service restart) | closed-set on the gate; policy on the lane |
| R2 | No systemd / pacman / driver / firmware / boot ownership or mutation | tsukuroi | closed-set (no such argv); policy on the claim |
| R3 | No dispatch, launch, complete, steer, reparent of a wave or lane | kumitate (mechanism); the watchdog is the actuator | closed-set: gate never calls `ufo-sighting` |
| R4 | No external fetch | chousa owns approved research fetches; mori has none | closed-set: no network binary |
| R5 | No secret / oauth / `server.token` / session **content** read | kagi | closed-set on the probe list; **gap** on journal echo and env-path override |
| R6 | No endpoint / model-health claim | kama | policy only (no `/health` probe exists; nothing stops a future one except review) |
| R7 | No remediation recommendation as an action mori takes | — | policy; finding ids name another owner |
| R8 | A probe that needs a write, a restart, or a fetch is refused and recorded | mori records, does not attempt | **gap:** no runtime refusal branch; the gate simply has no such probe |

---

## 1. R1 — no restart / kill

### Exploit the refusal exists to stop

A census that sees `oom_kill 1` or a dead watchdog pid and then `kill`, `systemctl restart`, `renice`, or reparents the driver. The 2026-10-14 webbridge OOM is the demand instance; the failure mode is "the observer becomes the actor."

### Enforcement point

**Closed-set, live path.** Every external command the live census runs is one of these `cap` sites (`mori-census.sh`):

| Line | Call | Effect |
|---|---|---|
| 174 | `cap "$PGREP_BIN" -af shokunin-watchdog` | read process table |
| 291 | `cap "$JOURNALCTL_BIN" --user -b --no-pager` | read this-boot user journal |
| 366 | `cap "$DF_BIN" -P "$t"` | read filesystem stats |
| 430 | `cap "$GIT_BIN" -C "$repo" log -1 --format=%ct` | read one commit timestamp |
| 471 | `cap "$TMUX_BIN" ls` | list sessions |

Plus non-`cap` reads: `stat -c %Y` (163), `head -n1` (152), `awk` field extract on a cgroup file (158), `find` mtimes (203, 252, 436). `cap` itself (142–147) is `"$@" 2>&1` with no wrapper that could add a verb — the argv is the literal above.

Non-comment scan of `probe_watchdog` (167–229), `probe_waves` (230–279), `probe_cgroup` (324–350), `probe_disk` (351–408), `probe_silence` (416–464), `probe_tmux` (465–482), `run_census` (483–509), and `cap` (142–148): **zero** hits for `kill|pkill|systemctl|pacman|curl|wget|ssh|renice`. The only `kill` token inside `probe_journal` is the grep class at line 300 (`oom-kill|Killed process`) — a pattern match on text already read, not an invocation.

Writes inside the live functions: none. `mkdir` / `touch` / `chmod` / `rm` / `ln` all sit inside `run_selftest` (from line 510). Live mode's only outputs are stdout lines (`run_census` 485–500) then `exit 0|1` (502–505).

### Policy points (necessary, not sufficient)

- `SKILL.md:15` Never column: "restarting a daemon; killing a pid".
- `SKILL.md:17`: "remediating, renicing, killing".
- `SKILL.md:32–33`: does not start, steer, or reparent.
- `SKILL.md:44`: "No remediation is performed or recommended as an action this lane takes."
- `PROVINCE.md:16`: "Detection and report only — never remediation."
- Wave contract (`spec.json` context): "no restarting or killing a process, no reparenting, … no deleting or resizing anything."
- `CorpusMap.md` cgroup boundary draft: "No `echo` to cgroup files, no oom_score_adj writes, no kills."

### What is not enforced

Nothing in the script rejects a future probe that shells out to `kill`. The GateDesign table (`GateDesign.md:88`) says "no `kill`, `systemctl`, `tmux kill-*`" — that sentence is a description of the source, not a check the source performs. `tmux` is called only as `ls` (471). `tmux kill-session` is absent, not denied.

`scripts/shokunin-watchdog.sh` **does** act (`launch_lane` at 65–84 calls `"$UFO" launch`; `complete` at 105 and 108). That file is the fleet driver, not a mori tool. mori is allowed to `stat` its log and `pgrep` its pid. It is not allowed to be that script. The closed-set above is what keeps the census from becoming it.

---

## 2. R2 — no systemd / pacman

### Exploit

Reading `oom_kill` and then `pacman -Syu`, `systemctl restart`, or claiming "the package is corrupt / the unit is failed, mori owns the fix." That claim collides with tsukuroi, whose census **does** run those probes.

### Enforcement point

**Closed-set.** Landed mori script: no `PACMAN` variable, no `SYSTEMCTL` variable, no `pacman`/`systemctl` argv. Confirmed by the same non-comment scan as R1.

The contrast is the enforcement proof, not a metaphor. `tsukuroi-shokunin/tools/tsukuroi-census.sh` (sha256 prefix `1045244387ff`, 126075 bytes) sets:

- `PACMAN=${TSUKUROI_PACMAN:-pacman}` (line 327) and calls `pacman -Qq`, `-Qkk`, `-Qm`, `-Qu`, `-Sup`, `-Suu`, `-Sl`, `-Q`.
- `SYSTEMCTL=${TSUKUROI_SYSTEMCTL:-systemctl}` (line 331) and probes `systemctl --user`.

mori's journal probe is `journalctl --user -b --no-pager` (291) and then four `grep -ciE` counts (300–305). It does not call `systemctl is-system-running`, `list-units`, or `is-active`. Its cgroup probe reads two files (324–350): `memory.events` and `memory.current` under the user slice default `/sys/fs/cgroup/user.slice/user-$(id -u).slice/`. It does not write controllers and does not enumerate unit files.

**Policy / ownership points:**

- `PROVINCE.md:12–14`: refuses OS package, systemd unit, driver/firmware, boot state → tsukuroi. Journal and cgroup are "fleet evidence," not ownership.
- `SKILL.md:34–36`: "never claims OS-state ownership and never repairs."
- `SKILL.md:3` anti-trigger: "NOT OS package/systemd/driver state (tsukuroi)".
- `tsukuroi-shokunin/PROVINCE.md:5–16`: owns pacman, systemd user units, journal/boot triage, driver/firmware; "Never installs, upgrades, or removes packages; never restarts services."
- Roster scan row `tsukuroi` (`mint-roster-scan.json`, `province_sha256` `6758f53da6cf…`, matches `sha256sum` of that PROVINCE): "OS package/systemd/driver/boot state remains tsukuroi. Mori only collects fleet-relevant liveness/OOM/resource observations and reports; never remediates or claims OS-state ownership."
- `shokunin.conf:66`: lane blurb ends "detection and report only". The watchdog `LANES=` string (`scripts/shokunin-watchdog.sh:14`) does **not** include mori — probation, not a dispatch seat.

### Gap (calibration)

`UNIT_FAILURE_JOURNAL` (`mori-census.sh` grep at the unit_failure class, severity `info`) reports a unit-failure **line** as fleet evidence. That is allowed. It is one edit away from a `systemctl` status probe. Nothing but review stops that edit. FindingIds routes `JOURNAL_*` / `OOM_*` / `CGROUP_*` remediation to tsukuroi (`FindingIds.md:214`), and "mori never appears as remediation owner" (`FindingIds.md:218`). Those are compare-contract sentences, not code.

---

## 3. R3 — no dispatch

### Exploit

An unsettled wave (`registry` present, no `results`) causes mori to call `ufo-sighting launch` or `complete`, or to write `.ufo/state/<lane>.round`. That is kumitate's mechanism and the watchdog's actuator. Ageing a wave is not steering it.

### Enforcement point

**Closed-set.** `probe_waves` (230–271) only `find`s `$WAVES_DIR` and tests `-f` on `swarm-registry.json`, `dispatch.json`, `run.json`, `results.json`, `closeout.json`, `mission-result.json`. The word `dispatch` there is a filename. No `ufo-sighting`, no `launch`, no write to `.ufo/state`. `grep` of the whole script for `ufo-sighting` is empty.

The actuator mori must not call is concrete:

```
scripts/shokunin-watchdog.sh:8   UFO=.../scripts/ufo-sighting
scripts/shokunin-watchdog.sh:70  out=$("$UFO" launch \
scripts/shokunin-watchdog.sh:105 "$UFO" complete --mission "$mid" ...
scripts/shokunin-watchdog.sh:108 "$UFO" complete --mission "$mid" ...
```

mori's watchdog surface (`probe_watchdog`, 167–229) reads pid + log mtime + `*.round` count. It does not invoke `$UFO`.

**Policy points:**

- `SKILL.md:32–33`: "Refuses dispatch mechanism — that is kumitate."
- `SKILL.md:3` anti-trigger: "NOT dispatch/orchestration (kumitate)".
- `MINT.md:27–28`: "Refuses dispatch (kumitate)".
- Roster row `kumitate`: "Dispatch mechanism is complementary; mori observes and never dispatches." (`province_sha256` `caa83fde27c0…` matches `kumitate-shokunin/PROVINCE.md`).
- `PROTOCOL.md:168`: recording `failed` "is a ledger act, not a kill." mori's silence probe emits `LANE_SILENT`; it does not write the ledger. Commit sparsity is not silence (`PROTOCOL.md:165–167`); the gate's own approximation is documented as r1-weak (`mori-census.sh` silence comment block above `probe_silence`).

### Gap

`kumitate-shokunin/PROVINCE.md` is still the generic seed ("Refuses: anything outside this domain"). The complementary split is enforced by **mori's** anti-trigger and by the roster-scan sentence, not by kumitate's province text. A router that only reads kumitate cannot see the boundary. mori's frontmatter is the side that names it (`SKILL.md:3`).

Wave member prompts say "leaf member — no subagent dispatch." That binds this round's seats, not the landed gate. The gate's closed-set is the durable point.

---

## 4. R4 — no external fetch

### Exploit

A "fleet health" question that `curl`s a model endpoint, a webhook, or an upstream status page, then treats the HTTP body as a liveness fact. That is also an R6 crossing into kama, and a chousa-shaped fetch without an approval table.

### Enforcement point

**Closed-set.** No `curl`, `wget`, `ssh`, or `nc` in the landed script (secret/network scan: zero matches on `curl|wget|ssh|nc|fetch|http|https` in the live spans). No URL literal. Disk, journal, cgroup, proc, and git are local.

**Policy points:**

- Wave contract: "A probe that would need a write, a restart, or an external fetch is REFUSED and recorded as a blocker."
- `FindingIds.md:120` `JOURNAL_PROBE_REFUSED`: "Probe would require write, root escalation, or external fetch."
- `FindingIds.md:190` `PROBE_REFUSED` includes `external-fetch`.
- `chousa-shokunin` is the lane that even discusses external fetches, and it refuses them without operator approval (`chousa-shokunin/PROVINCE.md`). mori has no approval table because it has no fetch.

### Gap — the refusal is not a runtime branch

Nothing prints `PROBE_REFUSED` today. If a probe needed a fetch, the current script would not attempt it **only because nobody wrote that probe**. There is no allowlist checker that fails closed on an unexpected argv. `MORI_JOURNALCTL_BIN` / `MORI_DF_BIN` / `MORI_PGREP_BIN` / `MORI_TMUX_BIN` / `MORI_GIT_BIN` (75–79) are path overrides. Pointing `MORI_DF_BIN` at a wrapper that fetches is an operator/env supply, not a path the script selects. The script will `cap` whatever path it was given, with the **fixed argv** in the table in §1. A wrapper can still do anything. That is the residual: argv is closed; the binary path is trusted.

`--selftest` does not close this further for live mode. Its stub dispatcher (`mori-census.sh:518–544`) only implements `pgrep|journalctl|df|tmux|git` and only when `--selftest` puts `$work/bin` on `PATH`. Live mode does not install that stub.

---

## 5. R5 — no secret read

### Exploit

A liveness probe that `cat`s `op.env`, `server.token`, `credentials/`, an oauth blob, or `session-id`, and prints the value into a `SURFACE`/`FINDING` line. The census transcript would then be the leak. kagi's rule is shape, never content (`kagi-shokunin/PROVINCE.md:23`: `op.env` "values never read into an artifact").

### Enforcement point

**Closed-set on the probe list.** Secret-pattern scan of the whole landed file (`credential|oauth|server.token|op.env|session-id|opencode.db|.ssh|id_rsa|password|Authorization|Bearer|op://`) → **no matches**. The paths the live gate opens are:

| Surface | Paths | Content taken |
|---|---|---|
| watchdog | `$ROOT/.ufo/watchdog.log` (mtime only, 163), `$ROOT/.ufo/state/*.round` (count only, 203) | no file body from state; log body is not read (mtime via `stat`) |
| waves | `$ROOT/.ufo/waves/*/*.json` | existence only (`-f`), not JSON values |
| journal | `journalctl --user -b --no-pager` stdout | full line text, then class counts |
| cgroup | `memory.events`, `memory.current` | numeric fields |
| disk | `df -P` | filesystem stats |
| silence | `git log -1 --format=%ct`, `find` mtimes | epoch integers |
| tmux | `tmux ls` | session names |

`read_file` (149–152) is used for `memory.current` (first line). It is not pointed at a credential path by any caller.

**Policy points:**

- `SKILL.md:38`: "Credentials, oauth, `server.token` and session material are SHAPE ONLY."
- `PROVINCE.md:15`: "credential material (→ kagi)".
- Roster row `kagi`: "Credential custody remains kagi; mori reads no credential or session contents."
- `FindingIds.md:270`: "credential validity (kagi) — shape-only if ever touched."
- Wave contract: "Credentials/oauth/server.token/session material are SHAPE ONLY."
- ProviderSecrecy seat (sibling, not this report) is tasked to exclude any command that content-reads those paths. This seat did not open those targets.

### Gaps (do not over-claim)

1. **Journal echo.** `probe_journal` stores the entire `journalctl --user -b` stream in `CAP_OUT` (291–293) and greps it. It prints counts, not matched lines (`emit_finding` at the class block passes `count=` only). But the full text is in the process's memory for the run, and a one-line change to put `$text` on a `FINDING` would publish whatever the user journal holds. User journals can contain command lines. There is no redaction step. Mitigation in the current design is "counts only" — true of the print path, not a filter.

2. **No path denylist.** `MORI_SHOKUNIN_ROOT`, `MORI_UFO_DIR`, `MORI_WATCHDOG_LOG`, `MORI_CGROUP_EVENTS`, `MORI_MEMINFO` (67–74) will `stat` / `read` / `find` whatever path the environment supplies. Default paths are fleet-local. An operator who points `MORI_WATCHDOG_LOG` at `op.env` gets an mtime, not the body (watchdog uses `epoch_mtime` only). Pointing `MORI_CGROUP_CURRENT` at a secret file **would** print its first line via `read_file` into the `current=` field of `CGROUP_OOM_KILL` (the emit at the cgroup finding). That is env-supplied, not a default. The script does not refuse it.

3. **`MEMINFO` is assigned (74) and never read** by a probe. Dead config, not a secret path. Not an enforcement mechanism either.

4. **GateDesign.md:92** says "path allowlist; no `credentials`, `op.env`, `server.token`." The landed script has **no allowlist function**. The safety is the default path list plus "the body never names those files." Calling it an allowlist overstates the code. This report does not.

---

## 6. Adjacent refusals (same design, not in the five-name list)

| Refusal | Where enforced | Strength |
|---|---|---|
| Do not call an unsettled wave failed | `probe_waves` comment + finding id `WAVE_UNSETTLED_AGE` only (`mori-census.sh` around 260–263). `SKILL.md:16,26`. | closed-set: no `failed` status string in the emitter |
| Missing surface is `unavailable`, not unhealthy | `emit_surface` (131–137) increments `N_UNAVAIL` and does not flip `ROLL`. `CGROUP_UNAVAILABLE` is severity `info` (`emit_finding` 118–127: only `warn|crit` set `ROLL=DRIFT`). Selftest case "clean: CGROUP_UNAVAILABLE is not DRIFT". `SKILL.md:43`. | closed-set |
| No endpoint/model health (kama) | No `/health`, `/v1/models`, or baseURL probe. `SKILL.md:37`. Roster row `kama`. `kama-shokunin/PROVINCE.md` owns those surfaces. | policy + absence |
| Selftest must not write the host | `run_selftest` `mktemp -d /tmp/mori-census-selftest.XXXXXX` (512), `trap 'rm -rf -- "${work:-}"'` (513), fixture mutation check `fx_no_mutation` (549+). Writes (`mkdir/touch/rm/chmod/ln`) are under `$work` or `$FX` inside it. | closed-set for the harness; trap is the cleanup |
| mori is not the remediation owner | `FindingIds.md:211–218` routes every id family to operator / kumitate / tsukuroi / kagi-shaped owners. | policy (compare contract) |
| Lane does not absorb another province | `PROVINCE.md:18` "Out of province → report, never absorb." | policy |

---

## 7. What would falsify this report

| Claim | Falsifier |
|---|---|
| Live `cap` sites are only the five argv rows in §1 | Any new `cap ` line, or any live function calling a binary without `cap` |
| No secret path in the default tree | A default (unset env) that opens `op.env`, `credentials/`, `server.token`, oauth, or a session file |
| Journal output is counts, not lines | A `FINDING` or `SURFACE` format string that interpolates `$text` or a matched journal line |
| No dispatch | A call whose argv contains `ufo-sighting`, `launch`, or `complete` |
| Selftest writes stay in the temp dir | A selftest path not prefixed by `$work` / `$FX` |
| `PROBE_REFUSED` is vocabulary, not code | A branch that actually emits `PROBE_REFUSED` — that would **raise** strength, not break the refusal |

Re-check command (read-only), from the fleet root:

```
python3 -c '
import re
from pathlib import Path
p=Path("mori-shokunin/tools/mori-census.sh")
lines=p.read_text().splitlines()
for i,l in enumerate(lines,1):
    if l.strip().startswith("#"): continue
    if re.search(r"\bcap ", l) or re.search(r"\b(kill|systemctl|pacman|curl|wget|ufo-sighting)\b", l):
        print(f"{i}|{l}")
'
```

Expected: the five `cap` lines in §1, plus journal grep lines whose pattern text contains `kill`, and **no** `systemctl|pacman|curl|wget|ufo-sighting`.

---

## 8. Smallest remediation (for the parent, not done here)

Do not add a remediation path. If the parent wants the prose claims to become checks, the smallest patch is one denylist in front of `cap` and `read_file`:

- Reject binary basenames `kill`, `pkill`, `killall`, `systemctl`, `pacman`, `curl`, `wget`, `ssh`, `nc`.
- Reject paths matching `op.env`, `server.token`, `credentials`, `oauth`, `session`.
- On reject: print `FINDING PROBE_REFUSED` (severity `info`, already in the FindingIds contract) and skip the probe.
- Add one `--selftest` case that sets `MORI_DF_BIN` to a fixture named `curl` and expects `PROBE_REFUSED` plus exit 0 (the refusal itself must not be DRIFT).

Until that lands, the honest statement is: **the five refusals hold because the live probe list cannot express them, not because a guard rejects them.** Policy text is real and routed; it is not the enforcement point.

## 9. Evidence index

| Fact | Where | When |
|---|---|---|
| Lane HEAD `27acf40`, tools untracked | `git -C mori-shokunin rev-parse HEAD`; `git status --short -- tools` → `?? tools/` | 2026-10-14T21:34:50-03:00 |
| Script sha256 `32f804a3…c3047`, 30584 bytes, mode 0755 | `sha256sum` + `stat` on `mori-shokunin/tools/mori-census.sh` | mtime 21:35:01-0300; hashed same minute |
| Fence ≠ landed; diff is `SKIP_FRESHEN` only | `difflib` of GateDesign bash fence vs landed file | same measurement |
| Five `cap` argv sites | lines 174, 291, 366, 430, 471 | file as hashed |
| Zero secret-literals | pattern scan, no matches | same |
| tsukuroi owns pacman/systemctl probes | `tsukuroi-census.sh:327,331` | file sha prefix `1045244387ff` |
| Watchdog is the dispatcher | `scripts/shokunin-watchdog.sh:8,70,105,108` | file sha prefix `b8b01a78b9f6` |
| Roster refusals for kumitate, tsukuroi, kama, kagi | `.ufo/scopes/shokunin-12h-20261014/mint-roster-scan.json` | `observed_at` `2026-10-14T23:39:59Z`; province sha256s matched this seat |
| Anti-triggers | `mori-shokunin/SKILL.md:3,15–18,30–38` | sha prefix `c9cc37f18d5f` |
| Province refuses | `mori-shokunin/PROVINCE.md:12–18` | sha prefix `aac98b22bb83` |

No host process was restarted, killed, or signalled. No journal line was acted on. No credential file was opened. No network client was run. No census verdict is claimed.
