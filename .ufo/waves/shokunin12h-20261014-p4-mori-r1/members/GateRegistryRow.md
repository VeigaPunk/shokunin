# GateRegistryRow — `tools/mori-census.sh` SKILL registry row (r1 draft)

**Seat:** `GateRegistryRow` (scribe)  
**Item:** `mori/GateRegistryRow`  
**Wave:** `shokunin12h-20261014-p4-mori-r1`  
**Advisory status:** Data only. Not a judge verdict, admission, or landed SKILL edit. Parent cuts the row into `mori-shokunin/SKILL.md` §Gates when the gate lands.  
**Lane bounds:** leaf member; no subagent dispatch; no product-code edit; no commit/push; host probes read-only except the gate’s own hermetic `--selftest` (writes only under `/tmp/mori-census-selftest.*`, trap-cleaned).  
**Axes:** coverage · operability · calibration  
**Schema authority:** `PROTOCOL.md` §Gate standard (registry = eight fields: name, `gate|probe`, entry command, verdict map, self-test command and spelling, pinned-value path, write scope, owner).  
**Measured-at:** `2026-10-15T00:34:56Z` (UTC)  
**Lane HEAD at draft:** `mori-shokunin` `27acf40c418b6d790b58202094e241e571ee6f56` (mint). Working-tree gate: **untracked** `tools/mori-census.sh` (parent-land candidate from GateDesign; not in seed commit).

---

## 0. Axes (godspeed)

| Axis | What this draft optimizes |
|---|---|
| **coverage** | All eight PROTOCOL registry fields filled; live + selftest exit maps declared; finding-id set named as the pin surface; peer vocabulary conflicts called out (not silently merged). |
| **operability** | Row is paste-ready for `SKILL.md`; entry/selftest commands are cold-runnable from lane root; write scope is a single fail-closed sentence. |
| **calibration** | Classification is **gate** (can fail) not probe; live DRIFT on this host is expected mint signal, not registry defect; selftest measured red on one case is reported, not greenwashed. |

---

## 1. Behavior delivered

Draft of the single SKILL gate-registry row for `tools/mori-census.sh`, grounded in:

| Source | What it supplied |
|---|---|
| `PROTOCOL.md` §Gate standard | Eight-field schema; `0=clean` / `1=failed`; other codes mapped to `clean\|failed\|could-not-evaluate`; self-test = exit **and** stable finding-id; flag spelling is lane-owned |
| `mori-shokunin/SKILL.md` §Gates (mint) | Path, `MORI_CENSUS: CLEAN\|DRIFT`, exit 0/1, `--selftest`, exit 2 setup/usage; “Registry row lands with the gate” |
| `mori-shokunin/PROVINCE.md` | Owner domain; detect/report only; refuses dispatch / OS-package / endpoint / secrets-content |
| Working-tree `tools/mori-census.sh` | Actual CLI, exit map, finding ids, selftest spelling, write fence, case table |
| `members/GateDesign.md` | Design contract the script implements |
| `members/FindingIds.md` / `FixtureDesign.md` | Peer id/fixture proposals (advisory; **script wins** for the row until parent reconciles) |

---

## 2. Canonical eight-field row (paste target)

Parent lands this table under `mori-shokunin/SKILL.md` §Gates (replace the mint prose stub). One row, eight columns — the shape D-137/D-139 docked sibling gates for missing.

| Field | Value |
|---|---|
| **name** | `mori-census` |
| **gate\|probe** | **`gate`** |
| **entry command** | `bash tools/mori-census.sh` (cwd = `mori-shokunin/`; alias `verify` / `--verify` accepted, no-op flag) |
| **verdict map** | see §3 |
| **self-test command and spelling** | `bash tools/mori-census.sh --selftest` — flag spelling **`--selftest`** (one word, no hyphen; not `--self-test`) |
| **pinned-value path** | see §4 |
| **write scope** | see §5 |
| **owner** | `mori` (`mori-shokunin` lane; detect-and-report only) |

### Compact single-line form (for narrow SKILL tables)

```text
mori-census | gate | bash tools/mori-census.sh | 0→clean(CLEAN) 1→failed(DRIFT) 2→could-not-evaluate(setup/usage) | bash tools/mori-census.sh --selftest | tools/mori-census.sh#selftest-cases (+ proposed corpus/fixtures/mori-census-selftest.expected.md) | live: none; selftest: /tmp/mori-census-selftest.* only | mori
```

### Markdown table form (preferred in SKILL.md)

```markdown
## Gates

| name | kind | entry command | verdict map | self-test | pinned-value path | write scope | owner |
|---|---|---|---|---|---|---|---|
| mori-census | gate | `bash tools/mori-census.sh` | `0` clean (`MORI_CENSUS: CLEAN`) · `1` failed (`MORI_CENSUS: DRIFT`) · `2` could-not-evaluate (setup/usage) · undeclared nonzero → could-not-evaluate | `bash tools/mori-census.sh --selftest` (spelling: `--selftest`) | `tools/mori-census.sh` embedded selftest case table (assert exit + `FINDING <ID>` / CLEAN); parent SHOULD also land `corpus/fixtures/mori-census-selftest.expected.md` as the durable pin pointer | **live: zero files**. **selftest only:** `mktemp -d /tmp/mori-census-selftest.XXXXXX` (trap rm). Never remediates; never writes fleet/lane/host state | mori |
```

---

## 3. Verdict map (code → fleet class)

Fleet outer interface per PROTOCOL (`clean | failed | could-not-evaluate`). Lane vocabulary stays `CLEAN|DRIFT` on the banner line.

### 3.1 Live / default mode (`bash tools/mori-census.sh`)

| Exit | Lane banner | Fleet class | When |
|---|---|---|---|
| **0** | `MORI_CENSUS: CLEAN (findings=N drift=0 unavailable=U surfaces=S)` | **clean** | Runnable census; no severity-bearing finding (`warn`/`crit`) fired. `info` findings and `unavailable` surfaces **do not** flip the rollup. |
| **1** | `MORI_CENSUS: DRIFT (findings=N drift=M …)` | **failed** | One or more severity-bearing findings (`warn`/`crit`) fired. Stable ids on `FINDING <ID> …` lines. |
| **2** | usage / setup text on stderr (no CLEAN/DRIFT claim) | **could-not-evaluate** | Unknown CLI args; selftest harness cannot construct its temp root; gate itself cannot run. A missing *optional* live surface is **not** exit 2 — it is `unavailable` under exit 0/1. |
| other nonzero | *(undeclared)* | **could-not-evaluate** | PROTOCOL default for undeclared codes. |

Banner contract (stable compare):

```text
MORI_CENSUS: CLEAN|DRIFT (findings=N drift=M unavailable=U surfaces=S)
```

### 3.2 Selftest mode (`--selftest`) — separate rollup

| Exit | Banner | Meaning |
|---|---|---|
| **0** | `MORI_CENSUS_SELFTEST: PASS (N cases, N passed, 0 failed)` | Every hermetic case matched want-exit + want-verdict/id regexes; fixture trees byte-unchanged. |
| **1** | `MORI_CENSUS_SELFTEST: FAIL (N cases, P passed, F failed)` | Capability red — **not** a live fleet DRIFT measurement. |
| **2** | usage | Bad invocation outside the selftest path. |

Selftest is **capability evidence** (PROTOCOL “Two evidences”), not the live grade. A green selftest does not imply live CLEAN; a red selftest does not by itself mean the host is unhealthy.

### 3.3 Why `gate` not `probe`

PROTOCOL: a tool that cannot fail is a **probe**. This instrument:

- returns exit **1** on severity findings,
- asserts exit **and** stable `FINDING <ID>` strings in `--selftest`,
- is owned by the lane as a re-runnable verdict over fleet/host observability surfaces,

→ register as **`gate`**.

---

## 4. Pinned-value path

PROTOCOL: expected values are **persisted inside the owning repo**, independent of recomputation; the registry **points**, it does not restate the matrix.

### 4.1 What exists now (working tree, untracked)

| Pin surface | Path / locus | Status |
|---|---|---|
| Gate script + embedded case table | `mori-shokunin/tools/mori-census.sh` (`run_selftest`, cases ~L677–767) | **Present, untracked** at measure time |
| Script identity | sha256 `dd939ec83775bf0baf42e0d6e1ef46ebd77d4e73009499c486ca4f03f695415b` · `wc -l` → **806** · mode `0755` | Identity of the bytes this row describes |
| Separate expected file | *(none)* | **Absent** — r1 gap |
| Frozen live snapshot run | *(none under `corpus/` or `.ufo/waves/*/frozen`)* | **Absent** — second PROTOCOL evidence still owed after land (mutable fleet surfaces) |

### 4.2 Registry pin pointer (what the row should name)

**Primary (honest for r1 land):**  
`tools/mori-census.sh` — the embedded hermetic cases **are** the committed expected values once the parent tracks the file. Each case pins:

- want **exit code**,
- want **`MORI_CENSUS: CLEAN|DRIFT`** (or CLI usage for setup cases),
- want **`FINDING <ID>`** presence/absence (stable id strings below).

**Recommended durable extract (parent SHOULD add on land, same commit as the gate):**  
`corpus/fixtures/mori-census-selftest.expected.md` (or `.tsv`) — a pointer table of `case_id → exit → verdict → finding_id_or_CLEAN`, so SCORECARD/LOG can cite a path that is not “the whole script”. Until that file exists, the registry row’s pinned-value path remains the script’s selftest section.

### 4.3 Finding ids the pin must keep stable

From the script header / emitters (GateDesign-landed set). **These are the machine contract**; FindingIds peer prose that diverges is advisory until parent reconciles.

| ID | Role in pin |
|---|---|
| `WATCHDOG_ABSENT` | DRIFT selftest case |
| `WATCHDOG_STALE` | DRIFT selftest case |
| `WATCHDOG_LOG_UNAVAILABLE` | info / unavailable path (not sole DRIFT) |
| `WAVE_UNSETTLED_AGE` | DRIFT selftest case |
| `OOM_KILL_JOURNAL` | DRIFT selftest case |
| `KILL_SIGNAL_JOURNAL` | declared emitter (observe/DRIFT per severity in script) |
| `SEGFAULT_JOURNAL` | declared (r1 severity info in GateDesign) |
| `UNIT_FAILURE_JOURNAL` | declared (r1 severity info) |
| `CGROUP_OOM_KILL` | DRIFT selftest case |
| `CGROUP_UNAVAILABLE` | info; selftest asserts **CLEAN** rollup |
| `DISK_LOW` | DRIFT when warn band |
| `DISK_CRITICAL` | DRIFT selftest case |
| `DISK_UNAVAILABLE` | info; not sole DRIFT |
| `LANE_SILENT` | DRIFT selftest case (see §7 — currently red) |

**Do not** put CorpusMap’s `MORI-WD-010` style ids in the registry pin unless/until the gate emits them. Two id schemes in one round = compare breakage.

### 4.4 Embedded selftest case matrix (pin contents summary)

| # | case label (script) | want exit | want verdict / id |
|---:|---|---:|---|
| 1 | `clean: all quiet` | 0 | `CLEAN` (no DRIFT findings) |
| 2 | `drift: WATCHDOG_ABSENT` | 1 | `FINDING WATCHDOG_ABSENT` + `DRIFT` |
| 3 | `drift: WATCHDOG_STALE` | 1 | `FINDING WATCHDOG_STALE` + `DRIFT` |
| 4 | `drift: WAVE_UNSETTLED_AGE` | 1 | `FINDING WAVE_UNSETTLED_AGE` |
| 5 | `clean: unsettled young wave does not fire` | 0 | `CLEAN` / waves ok |
| 6 | `drift: OOM_KILL_JOURNAL` | 1 | `FINDING OOM_KILL_JOURNAL` + `DRIFT` |
| 7 | `drift: CGROUP_OOM_KILL` | 1 | `FINDING CGROUP_OOM_KILL` |
| 8 | `drift: DISK_CRITICAL` | 1 | `FINDING DISK_CRITICAL` |
| 9 | `clean: disk under warn` | 0 | disk ok / `CLEAN` |
| 10 | `drift: LANE_SILENT` | 1 | `FINDING LANE_SILENT` |
| 11 | `clean: CGROUP_UNAVAILABLE is not DRIFT` | 0 | `FINDING CGROUP_UNAVAILABLE` + `CLEAN` |
| 12 | `clean: empty journal` | 0 | journal ok / `CLEAN` |
| 13 | `cli: unknown arg exit 2` | 2 | usage / `mori-census:` |
| 14 | `cli: --help exit 0` | 0 | `usage: mori-census` |

Case count **14** (12 fixture + 2 CLI). FixtureDesign’s 33-case matrix is a **superset proposal**; registry pins what the script actually asserts until parent expands both together.

---

## 5. Write scope

| Mode | Allowed writes | Forbidden |
|---|---|---|
| **live** (default) | **None.** Creates zero files. | Any write under fleet root, lane repos, `/etc`, cgroup controllers, pid files, journals |
| **`--selftest`** | Only `$work` from `mktemp -d /tmp/mori-census-selftest.XXXXXX`; removed on exit (trap). Per-case fixture trees under `$work/fx/…`; stub bins under `$work/bin/`. | Mutation of fixture bytes across a case (asserted via pre/post digest); any path outside `$work` |
| **remediation** | **None always.** No `kill`, `systemctl`, `tmux kill-*`, pacman, dispatch (`ufo-sighting`), curl/wget, secret open | — |
| **secrets** | Shape/path allowlist only; never open `credentials/`, `oauth/`, `server.token`, `op.env`, session payloads | Content reads |

Registry sentence (SKILL cell):

> **live: zero files. selftest: `/tmp/mori-census-selftest.*` only (trap-cleaned). Read-only over every fleet/host surface. Never remediates; never dispatches; never claims OS-package ownership.**

---

## 6. Owner

| Field | Value |
|---|---|
| **owner** | `mori` |
| **repo** | `mori-shokunin` |
| **domain** | fleet & host observability (森) — PROVINCE.md |
| **not owner of remediation** | operator / kumitate (dispatch, driver restart) · tsukuroi (OS package/systemd/driver planes) · kama (endpoints) · kagi (credential content) |

A red live census is a **finding routed outward**; mori does not appear as remediation owner (FindingIds §5).

---

## 7. Operability evidence (this seat — capability check only)

Commands run read-only / hermetic at `2026-10-15T00:34:56Z`:

```text
$ bash /home/vgpnk/Projects/shokunin/mori-shokunin/tools/mori-census.sh --selftest
PASS clean: all quiet (exit 0 CLEAN)
PASS drift: WATCHDOG_ABSENT (exit 1 DRIFT)
PASS drift: WATCHDOG_STALE (exit 1 DRIFT)
PASS drift: WAVE_UNSETTLED_AGE (exit 1 DRIFT)
PASS clean: unsettled young wave does not fire (exit 0 CLEAN)
PASS drift: OOM_KILL_JOURNAL (exit 1 DRIFT)
PASS drift: CGROUP_OOM_KILL (exit 1 DRIFT)
PASS drift: DISK_CRITICAL (exit 1 DRIFT)
PASS clean: disk under warn (exit 0 CLEAN)
FAIL drift: LANE_SILENT: exit 0 want 1; … MORI_CENSUS: CLEAN …
PASS clean: CGROUP_UNAVAILABLE is not DRIFT (exit 0 CLEAN)
PASS clean: empty journal (exit 0 CLEAN)
PASS cli: unknown arg exit 2 (exit 2)
PASS cli: --help exit 0 (exit 0)
MORI_CENSUS_SELFTEST: FAIL (14 cases, 13 passed, 1 failed)
exit=1

$ sha256sum …/tools/mori-census.sh
dd939ec83775bf0baf42e0d6e1ef46ebd77d4e73009499c486ca4f03f695415b

$ git -C mori-shokunin status --short tools/
?? tools/
```

**Calibration notes for parent:**

1. **Selftest is red on `LANE_SILENT`** at these bytes — do not claim `MORI_CENSUS_SELFTEST: PASS` in SCORECARD/LOG until GateDesign/parent fixes silence fixture wiring (freshen/PIN_NOW/`MORI_LANE_SILENCE_S` interaction) and re-runs green.
2. **Live DRIFT on this host is expected** (watchdog absent/stale, user-slice `oom_kill≥1` per CorpusMap/GateDesign live snapshots) — that is the mint demand signal, not a broken verdict map.
3. **Gate file is untracked** — registry row in SKILL without a tracked `tools/mori-census.sh` would be D-101-class (docs cite missing tool). Land script + row + pin pointer in one commit.
4. **Second evidence** (frozen snapshot run over committed fleet-shaped inputs) is still open after r1 land; selftest alone is capability, not measurement of `.ufo/` live state.

This seat did **not** run a live census for a verdict claim (LiveReceipt owns the receipt). Selftest was run only to bind the registry’s self-test spelling and case count to measured output.

---

## 8. Kind decision record (`gate` vs `probe`)

| Test | Result |
|---|---|
| Can the tool return a non-clean verdict on purpose? | Yes — exit 1 `DRIFT` |
| Selftest asserts exit **and** finding-id? | Yes — `FINDING <ID>` regexes in cases |
| Expected values intended in-repo? | Yes — embedded now; extract path proposed |
| Read-only over non-owned surfaces? | Yes — live zero-write; refuses remediation |
| Would “probe” fit? | No — a pure probe cannot fail closed on DRIFT |

→ **`gate`**.

---

## 9. Peer conflicts (report, do not absorb)

| Peer | Divergence | Registry disposition |
|---|---|---|
| FindingIds | Broader id set (`WATCHDOG_TICK_STALE`, `OOM_KILL_EVENT`, `MORI-*` prefixes in CorpusMap, etc.) | Pin **script-emitted** ids until parent unifies; note dual-scheme risk in LOG |
| FixtureDesign | 33-case matrix, different threshold env names (`MORI_WATCHDOG_LOG_MAX_AGE_S` vs script `MORI_WATCHDOG_STALE_S`), id spellings (`WATCHDOG_STALE_LOG` vs `WATCHDOG_STALE`) | Registry follows **landed script**; FixtureDesign is expansion backlog |
| GateDesign | Matches script; registry row sketch in §6 item 5 | Adopted and expanded to full eight fields |
| CorpusMap | `MORI-<FAM>-<NNN>` compare keys | Not gate banner ids; keep out of registry pin |

---

## 10. Touched surfaces (this seat)

| Path | Action |
|---|---|
| `.ufo/waves/shokunin12h-20261014-p4-mori-r1/members/GateRegistryRow.md` | **written** (this file) |
| `mori-shokunin/SKILL.md` | **not edited** — draft row above for parent |
| `mori-shokunin/tools/mori-census.sh` | **read + hermetic `--selftest` only**; not modified |
| host fleet paths | not written |

---

## 11. Out of scope

- Landing the row into `SKILL.md` or tracking `tools/` (parent).
- Fixing the red `LANE_SILENT` selftest case (GateDesign / parent).
- Expanding to FixtureDesign’s 33 cases.
- Unifying FindingIds vs script id spellings.
- Live `MORI_CENSUS:` verdict as a claimed score (LiveReceipt / parent SCORECARD).
- Remediation, dispatch, package claims, credential reads.
- Subagent dispatch (leaf).

---

## 12. Parent cut-over checklist

1. Ensure `tools/mori-census.sh` is the reviewed GateDesign body; `chmod 0755`; **git add** with the SKILL row.
2. Paste §2 markdown table into `SKILL.md` §Gates (replace mint stub lines 47–51).
3. Re-run `bash tools/mori-census.sh --selftest` → require `MORI_CENSUS_SELFTEST: PASS` before claiming operability green; fix `LANE_SILENT` first if still red.
4. Optionally land `corpus/fixtures/mori-census-selftest.expected.md` and retarget the pinned-value cell to that path (pointer only; do not duplicate full matrices in PROTOCOL/aggregator).
5. Record script sha256 + selftest tally + measured revision in `LOG.md` / `SCORECARD.md`.
6. Schedule frozen-snapshot evidence for mutable `.ufo` surfaces (PROTOCOL two-evidences) in a later round if live grade becomes a conformance claim.

---

## 13. Axis self-check (advisory)

| Axis | Draft posture |
|---|---|
| **coverage** | Eight fields present; live + selftest maps; 14-case pin inventory; id list; owner/refusal boundaries |
| **operability** | Copy-paste SKILL table; exact flag spelling; cwd; write fence; cold commands |
| **calibration** | `gate` justified; live DRIFT ≠ broken gate; selftest FAIL on LANE_SILENT reported honestly; peer id conflicts explicit; untracked tool called out |

---

**End of advisory report.** No judge verdict claimed. No remediation performed.
