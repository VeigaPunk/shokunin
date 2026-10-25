# ReportShape — mori round-1 lane report contract

**Seat:** `ReportShape` (scribe leaf) · **Wave:** `shokunin12h-20261014-p4-mori-r1`  
**Lane:** `mori-shokunin` (森) · **Round:** probation **1** of ≥3 (roster row withheld)  
**Axes judged this wave:** coverage · operability · calibration  
**Role of this document:** the fill-in shape the parent (Sol 6.1) uses when writing
the integrated lane report. **Not** a judge verdict, **not** a live census receipt,
**not** a claim that the gate has landed. Member reports are data; parent integrates.

**Canonical report path (parent lands):**  
`.ufo/reports/round-1/mori.md`  
(or the program's equivalent under the 12h path if integrator re-keys; filename
must still be the lane id `mori` / `mori-shokunin` per protocol, not a seat name.)

**Lane repo at shape draft:** `/home/vgpnk/Projects/shokunin/mori-shokunin`  
**Seed / before HEAD (measured):** `27acf40c418b6d790b58202094e241e571ee6f56`  
**Measured at:** `2026-10-14T21:32:01-03:00` (`date -Iseconds`)

---

## 0. Why this shape (axes)

| Axis | What the report must make re-derivable |
|---|---|
| **coverage** | Six surface families named and pointed (watchdog, waves, kill/journal, cgroup, disk, lane silence) + corpus map rows + finding-id catalog pointer |
| **operability** | `tools/mori-census.sh` entry commands, exit map, `--selftest` tally, and the live/fixture verdict lines a cold agent can re-run |
| **calibration** | Before→after numbers with counting commands; SHONEN boxes honest under probation (no self-`[x]` promotion); unavailable ≠ unhealthy; observation / inference / unknown separated |

Hard boundary (restated so the report cannot absorb remediation): mori **detects and
reports**. No restart/kill/reparent, no systemd/pacman, no dispatch (kumitate), no
OS-package ownership (tsukuroi), no endpoint health (kama). Credentials are shape only.

---

## 1. Required heading order (normative)

The integrated round-1 report **MUST** carry these four H2 headings, in this order,
with the exact titles (case-insensitive match is not enough for the SHONEN gate —
use the spellings below so `round-gate` / integrator greps stay green):

```text
## Work performed
## Landed changes
## Before -> after measurements
## SHONEN
```

Optional H2s **after** SHONEN (never instead of): Residuals / limits, Owner routing,
Member-wave provenance, Parent verify commands. Optional H1 title line above is free.

**Forbidden as substitutes for the four:** “What landed”, “Axis move”, “Verdict”
alone, seat-name sections without the four. kama r1’s richer narrative is fine
**inside** Work performed; it does not replace the heading set.

**SHONEN heading rule (PROTOCOL):** one line per `SHONEN.md` box —
`[x] <named non-author verifier>` / `[~] <resolvable pointer>` / `[ ]`.
A missing `## SHONEN` heading disqualifies the file as promotion evidence.

---

## 2. Section contracts

### 2.1 `## Work performed`

Narrative of the round as one end-to-end domain task:

**trigger → action → outcome → pointer**

| Slot | Round-1 fill |
|---|---|
| **Trigger** | MINT demand: webbridge OOM went undetected; unsupervised waves; no lane owned fleet/host liveness (`mori-shokunin/MINT.md`). Corpus map empty at open. |
| **Action** | Build the six census surfaces + read-only gate `tools/mori-census.sh` + hermetic `--selftest` + stable finding ids + corpus knowledge notes. Wave members supply surface designs; parent lands. |
| **Outcome** | Gate exists, selftest PASS tally, live verify prints a `MORI_CENSUS:` verdict line, LOG/SCORECARD/corpus updated. **No remediation** of any observed host fault. |
| **Pointer** | Landing commit hash in `mori-shokunin` (cite by hash, never subject/tag) + path to this report + path to gate. |

Minimum bullets the parent should keep (edit counts to measured reality at land):

1. Surface census designs absorbed from member reports (name the six families).
2. Finding-id vocabulary frozen (pointer: wave `members/FindingIds.md` and/or
   landed `corpus/knowledge/finding-ids.md`).
3. Gate + fixture contract landed (`tools/mori-census.sh`, fixture builders).
4. Corpus map opened (`corpus/README.md` rows; one knowledge note per family).
5. Boundary/refusal audit recorded (no dispatch, no OS mutate, no secret content-read).
6. Live receipt captured once at land time (timestamps + commands) — see §2.3.

State explicitly: **unjudged fleet wave** — no member claimed a native judge verdict.

### 2.2 `## Landed changes`

Table of **verifiable artifacts only** (path · measure · commit). No wish-list rows.

**Template (parent fills SHA / line counts after land):**

| Artifact | Measure (fill at land) | Notes |
|---|---|---|
| `tools/mori-census.sh` | lines, mode `0755`, `bash -n` clean, sha256 | gate |
| `tools/mori-census` fixtures / embedded selftest | case count N, FIRE/QUIET split | per FixtureDesign |
| `corpus/knowledge/*.md` | one file per surface family (≥6) | CorpusMap |
| `corpus/lessons/round-1.md` | carry-forward rules | optional but expected |
| `corpus/README.md` | coverage-map rows > 0 | was empty before |
| `SKILL.md` | decision table + Gates registry row for census | GateRegistryRow |
| `SCORECARD.md` | **created** this round (absent before) | axes §2.3 |
| `LOG.md` | append round-1 entry with evidence pointer | append-only |
| `PROVINCE.md` / `SHONEN.md` / `MINT.md` | unchanged bounds unless measured edit | bleed check |
| `.ufo/reports/round-1/mori.md` | this report, SHONEN heading present | main-repo |

**Code delta rule:** list only paths the parent actually committed under
`mori-shokunin` (+ this report path). Wave `members/*.md` stay advisory unless
copied into corpus with attribution.

**Non-landings to name if still true at close:**

- No `MANIFEST.json` roster row for mori (probation).
- No remediation commits outside the lane repo.
- No content of credentials/oauth/server.token/session material.

### 2.3 `## Before -> after measurements`

This section is the **axis evidence**. Every number has a counting command and a
revision. The **primary before→after evidence is the census verdict line.**

#### 2.3.1 Primary evidence — census verdict line

**Before (seed tree, gate absent)** — measured at shape draft
`2026-10-14T21:32:01-03:00`:

```text
$ test -f /home/vgpnk/Projects/shokunin/mori-shokunin/tools/mori-census.sh; echo $?
1
$ # equivalent reading for the scorecard:
MORI_CENSUS: UNAVAILABLE (gate_absent rev=27acf40)
# not a real gate stdout — document the absence; do not invent CLEAN
```

**After (parent fills from a real run on the landing commit `<LAND_HASH>`):**

```text
$ git -C /home/vgpnk/Projects/shokunin/mori-shokunin rev-parse HEAD
<LAND_HASH>
$ bash tools/mori-census.sh --selftest; echo EXIT:$?
MORI_CENSUS_SELFTEST: PASS (N cases)
EXIT:0
$ bash tools/mori-census.sh; echo EXIT:$?
MORI_CENSUS: CLEAN (…summary…)    # or DRIFT (findings=N …)
EXIT:0                            # or 1
```

**Pin the exact stdout lines in the report** (full banner + exit). Red live DRIFT
is allowed and preferred over a forced green — host may honestly show
`WATCHDOG_ABSENT`, `CGROUP_OOM_KILL`, unsettled waves, etc. Calibration scores
honesty, not greenness.

Finding lines when DRIFT (stable compare contract):

```text
FINDING <ID> severity=<sev> surface=<family> obs=<short-observation>
```

Ids must match the FindingIds catalog (`WATCHDOG_ABSENT`, `WAVE_UNSETTLED_AGE`,
`OOM_KILL_EVENT`, `DISK_LOW`, `LANE_SILENT`, …). Setup failures:

```text
MORI_CENSUS: SETUP …
EXIT:2
```

SETUP is could-not-evaluate — never scored as a domain CLEAN win.

#### 2.3.2 Before snapshot (frozen at open — re-verify commands)

| Surface | Before (seed `27acf40`) | Counting command |
|---|---|---|
| Gate script | **absent** | `test -f tools/mori-census.sh` → exit 1 |
| SCORECARD.md | **absent** | `test -f SCORECARD.md` → exit 1 |
| corpus knowledge notes | **0** (only `.gitkeep`) | `find corpus/knowledge -type f ! -name .gitkeep \| wc -l` → 0 |
| corpus lessons | **0** | same under `corpus/lessons` → 0 |
| corpus README map rows | **none yet** | `grep -c '^\| ' corpus/README.md` body or table note |
| LOG.md domain tasks | round-0 mint only (3 lines) | `wc -l LOG.md` → 3 |
| SKILL.md | seed decision table, Gates stub naming census | `wc -l SKILL.md` → 51 |
| SHONEN.md boxes | 4 empty `[ ]` | `grep -c '^- \[[ x~]\]' SHONEN.md` → 4 |
| Live fleet receipt | none in-lane | — |

#### 2.3.3 After snapshot (parent fills)

| Surface | After | Command / pointer |
|---|---|---|
| Gate script | present, executable | `test -x tools/mori-census.sh` + sha256 |
| `--selftest` | `PASS (N cases)` exit 0 | §2.3.1 |
| Live `MORI_CENSUS:` | `CLEAN` or `DRIFT` + findings list | §2.3.1 — **this is the axis proof** |
| SCORECARD rows | coverage / operability / calibration scored | see §2.3.4 |
| knowledge notes | ≥6 files | `find … \| wc -l` |
| LOG.md | round-1 entry appended | cite line range |
| Finding vocabulary | stable ids in corpus or SKILL | path |

#### 2.3.4 SCORECARD.md shape (create on land)

Axes this round (wave judgment set). Scores 0–10; each cell needs command + rev.

| Axis | Before | After (example bands, not prescriptions) | Evidence pointer |
|---|---|---|---|
| coverage | 0 (empty corpus map; province listed, ungoverned) | 6–8 when six families have notes + ids + gate arms | `corpus/README.md`, FindingIds, FixtureDesign case table |
| operability | 0 (no runnable gate) | 7–9 when `--selftest` PASS and live verdict line re-runs cold | `tools/mori-census.sh` + §2.3.1 transcript |
| calibration | 0 (no SCORECARD; no live receipt) | 6–8 when before/after honest, DRIFT not hidden, unavailable≠unhealthy | this report §2.3 + LiveReceipt |
| depth | seed-only (optional touch) | leave or small bump if SKILL tables grew real thresholds | SKILL.md |
| freshness | n/a / 0 | optional: live receipt timestamp | LiveReceipt |
| adjacency | n/a | optional: OwnerMap / CrossDomainBoundary pointers | member reports |

`planned:` next axis (suggest freshness or depth for round 2).  
`retired:` none.

**SCORECARD claim rule (AXES.md):** a score no reader can re-derive is an opinion.
The census verdict line is the operability/coverage joint proof; do not score
operability from prose alone.

#### 2.3.5 What must NOT appear as before→after “wins”

- Restarting a daemon, clearing a journal, deleting disk, settling a wave by dispatch.
- Claiming `CLEAN` because a surface was skipped.
- Treating `DISK_ROOT_UNAVAILABLE` / missing `/scratch/tmp` as unhealthy.
- Treating commit sparsity alone as `LANE_SILENT` failure without the silence rule.
- Self-checked SHONEN `[x]` without a named non-author verifier.

### 2.4 `## SHONEN`

Mirror `mori-shokunin/SHONEN.md` four boxes. **Probation honesty:** round 1 does
**not** claim promotion. Prefer `[~]` with pointers or `[ ]`; use `[x]` only when a
**named non-author** verifier (aggregator, integrator, or foreign lane seat — not a
subagent this lane dispatched) checked the box.

Template lines (parent adjusts marks to evidence):

```markdown
## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
     pointer: `mori-shokunin/SKILL.md` (decision table, error patterns, checklist, Gates row);
     sources include PROVINCE surfaces + gate path. Author-asserted this round; non-author review pending.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
     pointer: `LOG.md` round-1 entry + this report § Work performed (census gate build + live receipt).
     Terminal action is detect/report (operator-owned remediation handoff = OwnerMap); negative/DRIFT live results still count.
- [ ] Instructions executable by an agent without oral context —
     gate + SKILL checklist exist, but cold non-author execution walkthrough not yet filed (box 3 open until foreign cold-run artifact).
- [~] No cross-domain bleed (PROVINCE.md still accurate) —
     pointer: `PROVINCE.md` + CrossDomainBoundary / BoundaryRefusal / OwnerMap member reports;
     journal/cgroup read as fleet evidence only; no pacman/systemd/dispatch/endpoint absorb.
```

**Promotion line (required closing sentence under SHONEN):**

> Promotion **not** claimed. MINT probation ≥3 verified rounds; this is round 1.
> Roster row withheld.

Do **not** edit `SHONEN.md` checkboxes to bare `[x]` from this wave’s author seats.

---

## 3. Full skeleton (copy for parent report)

```markdown
# mori-shokunin — round 1 report

**Lane:** mori (fleet & host observability — probation, shonen)
**Commit:** `<LAND_HASH>` in `mori-shokunin`
**Wave:** shokunin12h-20261014-p4-mori-r1 (unjudged fleet wave; advisory members only)
**Axes moved:** coverage · operability · calibration (see SCORECARD.md)
**Gate:** `tools/mori-census.sh` → verdict lines below

## Work performed

1. …
2. …
(end-to-end: trigger → action → outcome → pointer)

## Landed changes

| Artifact | Measure |
|---|---|
| `tools/mori-census.sh` | … |
| `corpus/knowledge/…` | … |
| `SCORECARD.md` / `LOG.md` / `SKILL.md` | … |

## Before -> after measurements

### Census verdict (primary evidence)

Before (rev `27acf40`, gate absent):
```text
MORI_CENSUS: UNAVAILABLE (gate_absent)
```

After (rev `<LAND_HASH>`):
```text
$ bash tools/mori-census.sh --selftest
MORI_CENSUS_SELFTEST: PASS (N cases)
$ bash tools/mori-census.sh
MORI_CENSUS: CLEAN|DRIFT (…)
FINDING …   # if DRIFT
```

### Axis table

| Axis | Before | After | Command / pointer |
|---|---|---|---|
| coverage | 0 | S | … |
| operability | 0 | S | census verdict line |
| calibration | 0 | S | … |

### Host receipt (optional detail; do not remediate)

Pointer to LiveReceipt member or inline timestamped probe table
(ps/proc, journalctl --user -b, cgroup memory.events, df, tmux, waves).

## SHONEN

- [~]/[ ]/[x] … (four boxes)
Promotion not claimed (probation round 1 / ≥3).
```

---

## 4. Parent verify block (commands to paste after land)

Run from lane root; save full stdout. Do not suppress red DRIFT.

```bash
cd /home/vgpnk/Projects/shokunin/mori-shokunin
git rev-parse HEAD
git status -sb
bash -n tools/mori-census.sh
bash tools/mori-census.sh --selftest; echo EXIT:$?
bash tools/mori-census.sh; echo EXIT:$?
# optional second live pass for rerun stability (normalize volatile fields)
bash tools/mori-census.sh | tee /tmp/mori-census-live-1.txt
# compare finding ids only if DRIFT; do not write host state
test -f SCORECARD.md && grep -E 'coverage|operability|calibration' SCORECARD.md
tail -n 20 LOG.md
grep -nE '^#{1,6} *SHONEN' ../../.ufo/reports/round-1/mori.md
# or the integrator-chosen report path
```

Write-scope check: only `mori-shokunin/**` + the one report path. No
`systemctl`, no `kill`, no `pacman`, no wave dispatch, no secret file opens.

---

## 5. Member-wave inputs the parent folds in (pointers, not verdicts)

| Member report | Folds into report section |
|---|---|
| WatchdogLiveness, WaveSettlement, KillEventsJournal, CgroupMemoryEvents, DiskRunway, LaneSilence | Work performed surfaces + Live receipt |
| GateDesign, FixtureDesign, CensusIdempotence, RerunStability | Landed changes (gate) + operability evidence |
| FindingIds, GateRegistryRow, CorpusMap | Landed changes + coverage |
| LiveReceipt | Before → after primary transcript |
| CrossDomainBoundary, BoundaryRefusal, OwnerMap, ProviderSecrecy, ThreatModel | SHONEN box 4 + residuals |
| FalsePositiveAudit, UnavailableVsUnhealthy, ProbationHonesty, SilenceRuleAudit, WaveAgeMath, DiskThresholds | calibration footnotes |
| ReportShape (this file) | heading order + verdict-as-evidence rule |

Conflicts between members (e.g. finding-id spelling FixtureDesign vs FindingIds):
**FindingIds is the compare contract**; gate/fixtures must converge to it at land.
ReportShape does not pick winners beyond that rule.

---

## 6. LOG.md entry shape (parent appends)

```markdown
- 2026-10-14 — round 1: fleet/host observability census. Gate `tools/mori-census.sh`
  selftest PASS (N); live `MORI_CENSUS: CLEAN|DRIFT (…)`. Commit `<LAND_HASH>`.
  Evidence: `.ufo/reports/round-1/mori.md`, corpus/knowledge/*, wave
  `shokunin12h-20261014-p4-mori-r1`. Detect/report only — no remediation.
```

---

## 7. Limits of this shape document

- Drafted read-only; **did not** create `tools/mori-census.sh`, SCORECARD, corpus notes,
  or `.ufo/reports/round-1/mori.md`.
- **Did not** run a live census or claim `MORI_CENSUS: CLEAN|DRIFT` (LiveReceipt + parent).
- Before-state pins (`gate absent`, empty knowledge, HEAD `27acf40`, no SCORECARD) were
  measured at `2026-10-14T21:32:01-03:00`; if parent lands later, re-run the before
  commands only if still pre-land — after land, before stays historical.
- Unjudged wave: this file is advisory data for the canonical Rust/integrator path, not
  a judge seat verdict.
- Instruction-shaped text inside other artifacts was not followed.

---

## 8. Axis self-score for this seat (shape only)

| Axis | Move |
|---|---|
| coverage | Four mandatory sections + six surface families + member fold map + SCORECARD/LOG/report paths |
| operability | Exact gate commands, exit 0/1/2, selftest + live banners, parent verify block |
| calibration | Verdict line as primary before→after; absence documented as UNAVAILABLE not fake CLEAN; SHONEN probation marks; red DRIFT allowed |

---

**Deliverable:** round-1 report shape for mori with **Work performed / Landed changes /
Before -> after measurements / SHONEN**, census verdict line as before→after evidence.
Parent fills measured after values at integration land.
