# UnavailableVsUnhealthy — missing surface vs degraded surface

**Seat:** `UnavailableVsUnhealthy` (reviewer leaf) · **Wave:** `shokunin12h-20261014-p4-mori-r1`
**Lane:** `mori-shokunin` · **Round:** probation 1 · **Not a judge verdict.** Parent integrates.
**Axes:** coverage · operability · calibration
**Measured:** `2026-10-14T21:41:13-03:00` (`2026-10-15T00:41:13Z`)
**Gate snapshot:** `mori-shokunin/tools/mori-census.sh` sha256 `8e655187c00da9260593b8203cea072b62549b28f267ea007f81baec5a5a6925` (866 lines, `bash -n` exit 0 at that instant). The file was still being edited during this audit (an earlier read was 870 lines, sha256 `c70fdcfb…`). Line numbers below are that snapshot. Control-flow claims are from reading the script, not from a live or `--selftest` run (selftest writes under `/tmp`; refused here).

The word `unhealthy` does not occur in the gate. It occurs as a prohibition in `SKILL.md` checklist line 43 (still `[ ]`), `FindingIds.md` rule 4, `GateDesign.md` §1, `FixtureDesign.md` §5, `ReportShape.md` §2.3.5, and `SCORECARD.md` calibration cell. Degraded, in the gate, is the token `drift`.

---

## 1. How a reader is supposed to tell them apart

Three channels. They are not the same counter.

| Channel | Missing surface | Degraded surface | Readable, predicate false |
|---|---|---|---|
| `SURFACE <name>:` state | `unavailable` | `drift` | `ok` |
| Finding severity | `info`, or no finding. `emit_finding` (118–128) flips `ROLL` only for `warn\|crit` | `warn` or `crit` → `ROLL=DRIFT`, exit 1 | no finding, or `info` that must not be read as drift |
| Banner | `unavailable=U` counts **surface lines** whose state is `unavailable` (`emit_surface` 131–137). It does not count `*_UNAVAILABLE` findings | `drift=M` counts warn/crit findings, not surface lines | `MORI_CENSUS: CLEAN` is allowed while `unavailable>0` |

`ok` is not a health grade. It means this probe did not raise warn/crit. A surface can be `ok` and still carry an `info` finding (`CGROUP_OOM_KILL_CUMULATIVE`, `SEGFAULT_JOURNAL`, `UNIT_FAILURE_*`, `DISK_UNAVAILABLE` on a sibling target). Do not rewrite `ok` as healthy, and do not rewrite `info` as unavailable.

`unavailable=0` does not mean every designed surface was present. It means none of the seven probes took the `unavailable` branch.

There is no `PROBE_REFUSED` emitter in the gate. `FindingIds.md` §3.7 defines that id. A probe that would write, restart, or fetch is simply not coded. Absence of a refused-probe line is not a measurement that no such probe was needed.

---

## 2. Surface inventory

Gate header (lines 10–17) names seven surfaces. Design docs name more. Each row is the missing report, then the degraded report, then whether those two outputs stay distinct.

### 2.1 Watchdog — not distinct when the probe itself is missing

| Sub-surface | Missing (should be `unavailable`, info, no DRIFT) | Degraded (should be `drift` + warn/crit) | Distinct? |
|---|---|---|---|
| `pgrep` binary | Lines 180–183 emit `SURFACE watchdog: unavailable` and `WATCHDOG_LOG_UNAVAILABLE` info ("pgrep binary missing"). **No `return`.** `pid_n` stays 0. | Lines 206–207 then emit `WATCHDOG_ABSENT` **warn**. Lines 210–211 set `st=drift`. Line 218 emits a **second** `SURFACE watchdog: drift`. | **No.** Missing tool is also daemon-absent. Two surface lines. `N_SURFACES` increments twice. `unavailable` increments once, then `ROLL` becomes DRIFT. The finding id is the log id (`FindingIds.md` defines `WATCHDOG_LOG_UNAVAILABLE` as path missing/unreadable, and `WATCHDOG_SURFACE_UNAVAILABLE` as pgrep missing). |
| `pgrep` ran, empty match | Not this case. | `WATCHDOG_ABSENT` warn + surface `drift`. Correct degraded observation **if** `pgrep` actually ran. | Yes, against a real unavailable branch — but that branch does not stay unavailable (row above). |
| `pgrep` rc > 1 (error, not "no match") | Journal treats rc>1 as unavailable (309–311). Watchdog never reads `CAP_RC`. | Empty output from a failed `pgrep` falls through to `WATCHDOG_ABSENT` warn. | **No.** Probe error and true absence share an id. |
| `watchdog.log` missing or unreadable | `WATCHDOG_LOG_UNAVAILABLE` info (186–191). Comment 213 says this is `unavailable` when pid assessment is also missing. The branch at 212–214 assigns `st=drift`, which 211 already assigned. There is no assignment of `unavailable` after the early emit. | Log readable and age > `MORI_WATCHDOG_STALE_S` (default 900): `WATCHDOG_STALE` warn, surface `drift`. | Partial. Log absence is an info id, not a surface state. If a pid was found, surface stays `ok` (not called drift). If no pid was assessed, surface is `drift` via `WATCHDOG_ABSENT`, so the missing log is not the thing that flips the rollup — the invented absence is. |
| `.ufo/state/` missing or unreadable | No finding. `state_n` stays 0 (201–204). `find` stderr discarded. Detail says `state_rounds=0`. | No counter-mismatch id is implemented (`STATE_COUNTER_LOG_MISMATCH` is design-only). | **Not reported.** Missing is neither `unavailable` nor `drift`. A later compare cannot see it. `FindingIds.md` wants `STATE_COUNTER_UNAVAILABLE` info. |

Live host, this seat, same timestamp: `command -v pgrep` resolved, so the missing-binary collapse is **latent**, not the live `WATCHDOG_ABSENT` in `corpus/knowledge/observability-census-r1.md`. That receipt's absent+stale pair is a degraded observation (log readable, no matching pid). Do not reclassify it as unavailable. The erratum in that note (driver halted 2026-09-28, wrap line present) is a reading of cause, not a surface-class change. Cause is inference; the ids are the observation.

No selftest removes `pgrep`. The absent case (`drift: WATCHDOG_ABSENT`, line 743) stubs `pgrep` present with rc 1 and empty output. That proves the degraded arm, not the missing-tool arm.

### 2.2 Waves — missing directory is distinct; unreadable directory is not

| Sub-surface | Missing | Degraded | Distinct? |
|---|---|---|---|
| `WAVES_DIR` not a directory | Line 235–237: `SURFACE waves: unavailable`, `return`, no finding, no DRIFT. | `WAVE_UNSETTLED_AGE` warn only when a dir has registry/dispatch/run, no settle token, and age > `MORI_WAVE_UNSETTLED_S` (default 7200). Young unsettled stays `ok` (selftest line 782). | **Yes** for a missing directory. No stable id (`FindingIds.md` wants `WAVE_SURFACE_UNAVAILABLE`). Compare-by-finding-id will not see it; compare-by-banner `unavailable=` will. Not fixture-proved. |
| Directory exists, unreadable | `[ ! -d ]` is false. Unquoted glob does not match. Loop adds nothing. Surface `ok`, `total=0`. | Aged unsettled is `drift`. | **No.** Permission failure looks like an empty readable root (`ok`), not `unavailable` and not `drift`. False clean. |
| Empty readable root | `ok`, `total=0`. | Not degraded. | Empty is not missing. Correct if the directory was listed. |

Unsettled is not `failed`. The gate does not emit `failed`. That is a separate rule and it holds in `probe_waves`.

### 2.3 Journal — missing binary is distinct; rc=1 is an unproved middle

| Sub-surface | Missing | Degraded | Distinct? |
|---|---|---|---|
| `journalctl` binary absent | 300–302: `SURFACE journal: unavailable`, `return`, no finding, no DRIFT. | `OOM_KILL_JOURNAL` crit or `KILL_SIGNAL_JOURNAL` warn sets `st=drift`. | **Yes.** No `JOURNAL_UNAVAILABLE` id. Not fixture-proved. |
| `journalctl` rc > 1 | 309–311: `unavailable`, `return`, no finding. | Same degraded ids, only reached when rc is 0 or 1. | **Yes** for rc>1. |
| rc = 1 | Treated as a successful read (comment 308). | Grep runs on stdout+stderr (`cap` merges them). A failure text that matches a class regex can become a kill finding. | **Unknown on this host for a failed open.** `man journalctl` EXIT STATUS (read at this timestamp) says any non-zero is failure and does not define an empty code. A filtered no-match, `journalctl --user -b --no-pager -n 1 -g '___mori_census_no_such_token_7f3a___'`, exited **1**. So rc=1 is at least the empty-match code here. It is not proved to be only that. |
| Empty readable journal | Surface `ok`, no finding. Selftest `clean: empty journal` (837–838) asserts `SURFACE journal: ok`. | Not this case. | **Yes.** Empty-but-read is not unavailable. `FindingIds.md` row `JOURNAL_UNAVAILABLE` contradicts itself: "fails (no access, empty, binary missing)" vs "zero hits = not unavailable". The gate follows the second clause. |
| Segfault / unit failure | Not unavailable. | `SEGFAULT_JOURNAL` and both unit-failure ids are **info**. They do not set `st=drift`. Surface stays `ok` unless oom/kill also fired. | Third bucket, not a collapse into unhealthy. `FindingIds.md` wanted `SEGFAULT_EVENT` at warn. The gate deliberately does not. Do not call info+`ok` either missing or degraded. |
| System journal | Not probed. `corpus/README.md` Known gaps names the user-only scope. | Not labeled `drift` for lines it never read. | **Omission.** `unavailable=0` does not record this blindness. The knowledge-note erratum already says so. Not a mislabel as unhealthy. |

### 2.4 Cgroup — one proved arm; field absence is invented zero

| Sub-surface | Missing | Degraded | Distinct? |
|---|---|---|---|
| `memory.events` unreadable | 359–362: `SURFACE cgroup: unavailable`, `CGROUP_UNAVAILABLE` info, `return` before any oom id. | `CGROUP_OOM_KILL` crit only if the local/service counter is numeric and > 0 (395–397). | **Yes.** Only fixture-proved arm: selftest `clean: CGROUP_UNAVAILABLE is not DRIFT` (830–833) expects that finding, `^SURFACE cgroup: unavailable`, and `CLEAN`. |
| `memory.current` unreadable while events are readable | `read_file` returns empty; detail prints `current=?` (402). No finding. Not counted in `unavailable=`. | Does not by itself set `drift`. | Partial. `?` is an unknown marker, not the `unavailable` token. `FindingIds.md` wants `CGROUP_MEM_CURRENT_UNAVAILABLE` info. Not called unhealthy. |
| `oom_kill` key absent inside a readable events file | `oom_kill=${oom_kill:-0}` (392) invents 0. | A real `oom_kill>0` on the local/service file is crit. | **No, the other direction.** Unknown field becomes a clean zero, not `unavailable` and not `drift`. CorpusMap rule "do not invent zeros" is not what this line does. |
| `memory.events.local` and `user@UID.service/memory.events` both unreadable | `service_oom_kill` stays empty (386–391). No surface `unavailable`. No `CGROUP_UNAVAILABLE`. If parent `oom_kill>0`, the word `unavailable` is interpolated into the **payload** of `CGROUP_OOM_KILL_CUMULATIVE` (399: `service_scope_oom_kill=${service_oom_kill:-unavailable}`). That does not increment `N_UNAVAIL`. Surface stays `ok`. If parent `oom_kill` is 0, the missing local/service files are silent. | Local/service counter > 0 → crit + `drift`. Parent counter > 0 with a readable zero local counter → info, surface `ok`. | The payload word `unavailable` is not the surface state. A grep for the token will false-hit a cumulative-info line. |
| `/proc/meminfo` | `MEMINFO` is assigned (line 74) and passed in the selftest env. No probe reads it. | `MEM_HEADROOM_LOW` / `MEM_HEADROOM_CRITICAL` are not implemented. | **Omission.** `MemoryPressureReading.md` defines class `unavailable` vs `low-headroom` vs `healthy`. The gate emits none of those three words for memory. A CLEAN rollup is not a headroom grade. |

### 2.5 Disk — surface `unavailable` only when zero targets exist; scratch is outside the probe set

| Sub-surface | Missing | Degraded | Distinct? |
|---|---|---|---|
| `df` binary absent | 410–412: `SURFACE disk: unavailable`, `return`, no finding, no DRIFT. | `DISK_LOW` warn / `DISK_CRITICAL` crit. | **Yes.** No `DISK_PROBE_UNAVAILABLE` id. Not fixture-proved. |
| Every configured target `! -e` | Per-target `DISK_UNAVAILABLE` info `target_absent` (417), then surface `unavailable` because `target_found` stays 0 (451–452). Info does not flip `ROLL`. | Not `DISK_LOW`. | **Yes** for the all-absent case. Not fixture-proved. |
| One target absent, another present | Absent target: `DISK_UNAVAILABLE` info. Surface state comes from the present target (`ok` or `drift`). | Present target over threshold: `DISK_LOW` / `DISK_CRITICAL`. | **Yes** at id level (absent path is not rewritten as low). Surface line is not `unavailable`. |
| Target exists, `df` rc ≠ 0, empty, or unparsable | Same id `DISK_UNAVAILABLE` info (`df_failed` / `df_empty` / `df_parse`). `target_found=1`, so surface is `ok` unless another target drifted. | Over-threshold is a different id. | **Collapsed ids.** Path-absent and probe-failed share `DISK_UNAVAILABLE`. Surface state differs only when **no** target existed. A single present path whose `df` fails is surface `ok` plus an info finding: failed read looks clean at the surface token. `FindingIds.md` splits `DISK_ROOT_UNAVAILABLE` vs `DISK_PROBE_UNAVAILABLE`. The gate does not. |
| `/scratch`, `/scratch/tmp` | **Not in the default set.** Line 80: `DISK_TARGETS=${MORI_DISK_TARGETS:-"$ROOT /tmp"}`. Header line 15 calls scratch optional. This seat: `test -e /scratch` exit 1, `test -e /scratch/tmp` exit 1, `test -e /tmp` exit 0, at `2026-10-14T21:41:13-03:00`. | Not labeled `DISK_LOW`. | **Omission, not a mislabel.** `FindingIds.md` §3.5, `DiskRunway.md`, `ReportShape.md` §2.3.5, and `FixtureDesign.md` case 25 require an info unavailable row for the absent scratch root and forbid calling it unhealthy. The gate does not call it unhealthy. It also does not emit the row. Live `unavailable=0` cannot be cited as that classification. |

### 2.6 Lane silence — no `unavailable` state exists

| Sub-surface | Missing | Degraded | Distinct? |
|---|---|---|---|
| Lane repo directory absent | `n_skip++`, `continue` (478–480). No finding. Surface can stay `ok` with `skipped=N` in the detail string. If every roster lane is missing, surface is still `ok`. | `LANE_SILENT` warn when both head epoch and newest non-git mtime are outside the window (511–512). | **Not reported as unavailable.** Not called `LANE_SILENT` either, for a missing directory. `FindingIds.md` wants `LANE_GRADE_UNAVAILABLE` info ("missing repo, not a git dir"). |
| `git` missing, git rc ≠ 0, or no `.git` | `head_t` is initialized to 0 (482) and stays 0. | If newest file mtime is also outside the window, `LANE_SILENT` warn fires with `head_epoch=0`. | **Partial collapse.** Fresh files still grade `progressing` without git, so a missing git binary does not by itself DRIFT. Old files plus an unread HEAD share the silent id with a truly old HEAD. `head_epoch=0` is not an `unavailable` token; it is an epoch that fails every window test. The in-window-HEAD / old-files case (the comment's `progressing-weak` path, 476–485) cannot be reached when git was not read, and becomes `LANE_SILENT` instead. |
| Report file absent | Gate does not read report mtimes. | Cannot be distinguished from any other grade. | `FixtureDesign.md` case 30 required silence grade `unavailable`, not `LANE_SILENT`. Not implemented. |

`skipped=` in the detail string is the only missing-repo signal. It does not change surface state and does not increment `unavailable=`.

### 2.7 tmux — distinct, and there is no degraded class

| Sub-surface | Missing | Degraded | Distinct? |
|---|---|---|---|
| `tmux` binary absent | 522–524: `unavailable`, `return`, no finding, no DRIFT. | No degraded id exists. | **Yes.** Not fixture-proved. |
| `tmux ls` rc ≠ 0 | 528–530: `unavailable`, comment says rc 1 is "no server", but **any** non-zero rc takes this branch. | Not rewritten as `drift`. | Conservative. A real tmux error is not called degraded. It is also not distinguished from "no server". Acceptable under the rule; lossy for compare. |
| rc 0, zero sessions | Surface `ok`, `sessions=0`. | Not degraded. | `tmux ls` with no server is rc 1 on this tool's own comment, so the zero-session `ok` path is the unusual one. |

### 2.8 Design surfaces with no gate line

These are in member designs or the corpus gap list. The gate neither marks them `unavailable` nor `drift`. That satisfies "never unhealthy" and fails "a missing surface is `unavailable`".

| Surface | Where specified | What the gate emits |
|---|---|---|
| System journal / coredumpctl | `corpus/README.md` Known gaps; knowledge-note erratum | nothing |
| `/proc/meminfo`, `memory.max`, pressure | `FindingIds.md` §3.4; `MemoryPressureReading.md` | nothing (`MEMINFO` unused) |
| `/scratch/tmp` | `FindingIds.md` §3.5; `DiskRunway.md`; `ReportShape.md` §2.3.5 | nothing, unless `MORI_DISK_TARGETS` adds it |
| `.ufo/state/*.round` as its own surface | header line 11; `FindingIds.md` `STATE_COUNTER_UNAVAILABLE` | a count, or 0 |
| `PROBE_REFUSED` | `FindingIds.md` §3.7 | nothing |
| Gate binary absent | `ReportShape.md` §2.3.1 `MORI_CENSUS: UNAVAILABLE (gate_absent)` | cannot self-report. That line is a document convention for the seed tree, not a gate branch. Do not invent it as live stdout. |

---

## 3. Findings (audit severity, not gate severity)

### High — missing watchdog probe is reported as a dead daemon

`probe_watchdog` else-branch (180–183) does not return. Lines 206–218 then treat `pid_n=0` as `WATCHDOG_ABSENT` warn and emit a second surface line in state `drift`. The comment at 213 claims the missing-log-and-missing-pid case is `unavailable`; both assignments in that function set `drift`.

Effect on a receipt: `MORI_CENSUS: DRIFT` with `unavailable≥1` and two `SURFACE watchdog:` lines, one of each state. A reader who trusts the later line, or the warn finding, will call a missing `pgrep` a fleet-liveness failure. That is the prohibited collapse.

The observation text "no shokunin-watchdog process matched by pgrep -af" is false when `pgrep` did not run. Unknown is printed as an observation.

Same shape for a `pgrep` that ran and failed (rc not inspected).

Not the live receipt. `pgrep` is on `PATH` here. The landed selftest does not construct the missing binary.

### Medium — silence encodes an unread HEAD as epoch 0, then may call the lane silent

`probe_silence` has no `unavailable` branch. A missing repo is `skipped` inside an `ok` line. An unread HEAD is `head_epoch=0`, which loses to every silence window, so old files plus a missing `git` become `LANE_SILENT` warn. `FindingIds.md` `LANE_GRADE_UNAVAILABLE` (info) is the id that would have kept those apart. It is not emitted.

### Medium — disk failed-read and scratch absence do not use the unavailable surface token

- Present path + failed `df`: `DISK_UNAVAILABLE` info and surface `ok` (420–424, 451–454).
- Absent scratch roots: not in the default target list (line 80). Measured absent at `2026-10-14T21:41:13-03:00`. Design requires an info row and forbids `DISK_LOW`. The gate does the second and not the first.
- One id covers `target_absent`, `df_failed`, `df_empty`, and `df_parse`.

### Medium — cgroup missing field becomes a healthy zero; the word `unavailable` leaks into a payload

Line 392. Line 399. A token search for `unavailable` is not a search for the surface state. The events-file arm (359–362) is the counterexample that does it correctly, and it is the only selftest that locks the rule.

### Low — several correct unavailable branches have no stable finding id

Waves-dir missing, journalctl missing, journal rc>1, df missing, tmux missing. The surface line and the banner counter carry the distinction. `FindingIds.md` compare is by id+subject. Those branches disappear from a finding-set diff. `SURFACE_UNAVAILABLE` (FindingIds §3.7) is defined and not emitted.

### Claim check — "fixture-proved" is one arm

`SCORECARD.md` calibration cell: "unavailable ≠ unhealthy is enforced and fixture-proved".

Selftest cases in this snapshot: 12 domain checks + 2 CLI checks. Unavailable-and-not-DRIFT is asserted once (`CGROUP_UNAVAILABLE`, lines 830–833). Empty-journal asserts the inverse (readable empty is `ok`). There is no case for missing `pgrep`, missing waves dir, missing `journalctl`, missing `df`, absent disk target, missing `tmux`, or missing lane repo.

`FixtureDesign.md` cases 21, 25, and 30 required those arms. They are not in the landed `check` list.

`emit_surface` not flipping `ROLL` is necessary and not sufficient. The watchdog fall-through adds a warn finding after the unavailable line. A closed-set claim that stops at `emit_surface` misses that.

`SKILL.md:43` is still an unchecked box. That matches the code better than the scorecard sentence does.

---

## 4. What already stays distinct (do not fold these into DRIFT)

- `emit_surface` state `unavailable` increments `N_UNAVAIL` only. It does not set `ROLL`.
- `emit_finding` severity `info` does not set `ROLL`.
- Cgroup events unreadable: early return, info id, selftest expects CLEAN.
- Waves directory missing: early return, no `WAVE_UNSETTLED_AGE`.
- `journalctl` missing or rc>1: early return, no kill id.
- `df` missing: early return, no `DISK_LOW`.
- All configured disk targets absent: surface `unavailable` plus info findings, not `DISK_LOW` / `DISK_CRITICAL`.
- tmux missing or any non-zero `tmux ls`: `unavailable`, not `drift`.
- Empty journal (rc 0 in the fixture): surface `ok`, not `unavailable`.
- Young unsettled wave: surface `ok`. Not `failed`, not `unavailable`.
- Live `WATCHDOG_ABSENT` when `pgrep` ran and matched nothing is a degraded observation. It is not an unavailable surface.

---

## 5. Operable read of a receipt

1. Classify from the `SURFACE` state token, not from the prose in the parentheses and not from the presence of the substring `unavailable` (it also appears as a cgroup payload default).
2. A missing surface is one `SURFACE` line in state `unavailable`, no second line for that name, and no warn/crit finding whose predicate is "the probe did not run".
3. A degraded surface is state `drift` plus at least one warn/crit finding whose predicate was actually measured (pid unmatched **after** `pgrep` ran, log age over threshold, aged unsettled wave, oom/kill class count, local cgroup `oom_kill>0`, disk percent over threshold, lane files and HEAD both outside the window).
4. `info` + surface `ok` is a third class. Not missing. Not degraded.
5. Banner `unavailable=` counts surface lines, not families. Two watchdog lines make `surfaces=` 8 for 7 families.
6. `unavailable=0` on a live run does not classify `/scratch/tmp`, system journal, meminfo, or a missing state dir.

---

## 6. Observation / inference / unknown

**Observed (this seat, this timestamp):**

- Gate text and line numbers at sha256 `8e655187c00da9260593b8203cea072b62549b28f267ea007f81baec5a5a6925`.
- `bash -n` on that snapshot: exit 0.
- `test -e /scratch` exit 1, `test -e /scratch/tmp` exit 1, `test -e /tmp` exit 0.
- `command -v pgrep` resolved (missing-pgrep path not live).
- `journalctl` filtered no-match exit 1; man page does not define that code.
- `SKILL.md:43` still `[ ]`. Scorecard claims the distinction is fixture-proved. Selftest source contains one unavailable-not-DRIFT assertion.

**Not observed:**

- This seat did not run `tools/mori-census.sh` or `--selftest`. Exit tallies in `SCORECARD.md` and the knowledge note are prior receipts, and the knowledge note's own erratum 2 says the cgroup probe changed after the quoted live line. Do not treat `unavailable=0` in that receipt as a proof of the current branches.
- Whether a journalctl permission failure is rc 1 or rc>1. Unknown. Not scored as a confirmed collapse.

**Inference (labeled, not an id):**

- A missing `pgrep` would produce DRIFT. That follows from the control flow above. It was not executed.
- An unreadable waves directory would look like `total=0` / `ok`. Same: control flow, not a chmod experiment (that would be a write).

---

## 7. Residual risk

The gate file moved during this audit. If a later edit adds `return` after the watchdog unavailable emit, finding 1 is stale — re-read `probe_watchdog` before landing. The fall-through was present in every read this seat took, including the pinned snapshot.

Parent integrates. This file does not patch the gate, does not score a round, and does not remediate the host.
