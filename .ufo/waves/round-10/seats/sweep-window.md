# Seat `ScoutSweepWindow` — main-repo sweep of everything landed after the refresh-7 cutoff

Round-10 aggregator wave (refresh 8), L2 seat. Author: subagent `ScoutSweepWindow` (aggregator L1
identity). Write scope: this file only. Every git call below is read-only (`log`, `show`, `ls-files`,
`rev-parse`, `merge-base --is-ancestor`, `rev-list`, `cat-file`, `ls-tree`); no file outside this seat
path was written, no index or history mutation, no child-repo write.

Window stamp this seat was handed: **`2026-09-29T01:19:59Z`** (= `2026-09-28T22:19:59-03:00`), round-9's
last gate re-run. Every cell below is scoped to `>= 2026-09-29T01:19:59Z` unless the cell says otherwise.

## 0. Measurement stamps

`MANIFEST.json` and `.ufo/watchdog.log` both moved *while this seat ran*. Cells are therefore pinned to
the stamp that produced them. Five stamps, all main repo `/home/vgpnk/projects/shokunin`:

| Stamp | wall UTC | main HEAD | `MANIFEST.json` md5 | `rounds` entries | last-wins rows | tally `ok/failed/in-flight/not-dispatched` | NOW-STALE | AT-`closed_at` |
|---|---|---|---:|---:|---:|---|---:|---:|
| `S0` | `2026-09-29T01:52:33Z` | `3069841` | `df4876291b18d381975119c17a48e22b` | 37 | 112 | 83 / 4 / 7 / 18 | **10** | 0 |
| `S1` | `2026-09-29T01:53:35Z` | `3069841` | `df4876291b18d381975119c17a48e22b` | 37 | 112 | 83 / 4 / 7 / 18 | **10** | 0 |
| `S2` | `2026-09-29T01:55:54Z` | `ae19fca` | `3f6dd15c99cb97bf746a4546139e6565` | **48** | **120** | **91** / 4 / 7 / 18 | **4** | 0 |
| `S3` | `2026-09-29T01:57:18Z` | `3485880` | `3f6dd15c99cb97bf746a4546139e6565` | 48 | 120 | 91 / 4 / 7 / 18 | **5** | 0 |
| `S4` | `2026-09-29T02:00:51Z` | `b5fff81` | `3f6dd15c99cb97bf746a4546139e6565` | 48 | 120 | 91 / 4 / 7 / 18 | **5** | 0 |

`.ufo/watchdog.log` md5 `5ef78ee7a571d63d091bce91b7cfc53d` at `S0`–`S3`; `1b0da7b483d2c833e827c009b16838c9`
at `S4` (re-read `2026-09-29T02:00:19Z`). Commands: `md5sum MANIFEST.json .ufo/watchdog.log`,
`git rev-parse --short HEAD`, `date -u +'%Y-%m-%dT%H:%M:%SZ'`.

Main-repo window commit set at `S4` — `git log --since=2026-09-29T01:19:59Z --format='%h %cI %an %s'`, 11 rows:

| commit | author | committed | subject (truncated) |
|---|---|---|---|
| `b5fff81` | `protocol-shokunin` | `22:59:26-03:00` | round-13: durability commit (11 prompts, 2 orphan reports, `l0-questions`) |
| `3485880` | `Joao Pedro Veiga` | `22:56:45-03:00` | round-15 kagi report: operability 8 → 9 |
| `fcefcf5` | `protocol-shokunin` | `22:56:28-03:00` | round-13: durability sweep (diff carried 8 round-10 files, not the 11 prompts its message claims) |
| `ae19fca` | `protocol-shokunin` | `22:55:48-03:00` | round-13: closure pass at `closed_at` `22:23:00-03:00` (11 `rounds` entries) |
| `3069841` | `Joao Pedro Veiga` | `22:52:19-03:00` | round-15: kake report — freshness 8 → 9 |
| `0863746` | `integrator` | `22:51:25-03:00` | research: 3 GPT-6-Astra browse harvests |
| `2d19a64` | `integrator` | `22:44:21-03:00` | sibling-mint allowance + kama probation entry |
| `a2cac72` | `aggregator-shokunin` | `22:35:27-03:00` | round-9: connector seat evidence |
| `cc6d9d4` | `aggregator-shokunin` | `22:34:10-03:00` | round-9: aggregator lane report + ledger addendum |
| `6415a9b` | `aggregator-shokunin` | `22:29:46-03:00` | round-9: aggregator ledger refresh 7 |
| `3d20676` | `Joao Pedro Veiga` | `22:20:09-03:00` | reports: kumitate round-14 addendum |

Author split of the **main-repo window commit set**: `Joao Pedro Veiga` 3, `aggregator-shokunin` 3,
`integrator` 2, `protocol-shokunin` 2 (`git log --since=2026-09-29T01:19:59Z --format='%an' | sort | uniq -c`).

### 0.1 Measured vs `could-not-evaluate`

**Measured (command in every cell):** §1 report additions/markers/`SHONEN` (two methods), §2 prompt
untracked counts at three stamps, §3 `MANIFEST.json` last-wins tally + stale-row scan at five stamps,
§4 child window commits by author + mirror tracked at HEAD, §5 mirror containment in `origin`, §6 the
seventh lane's existence/HEAD/dirty/remote/index/`.gitignore` status and the two falsifying commands for
`fcefcf5`'s round-9 claim.

**`could-not-evaluate` / `not-run`, with reasons:**

- `not-run` — **the `kama-shokunin` corpus-gate verdict.** The seat contract permits only read-only
  sibling gates *named in the task*, and this task names none. The L1's own numbers (`--repo kama-shokunin
  --round 10` → exit 1, 12 findings; `corpus/knowledge/` + `corpus/lessons/` untracked at `9cee9fc`) are
  cited as L1-measured, not as cells this seat executed.
- `could-not-evaluate` — **the legality of the root-level `PROTOCOL-APPENDIX.md`** that appeared between
  the `S4` and final re-reads (`git status --porcelain | grep '^??'` → `?? PROTOCOL-APPENDIX.md`). No
  command in the repo assigns a writer for it, and this seat did not read a file outside its task's
  sources.
- `could-not-evaluate` — **the truth of `round-15/kumitate.md`'s `ROUND_GATE: CLEAN` output.** Re-running
  `node scripts/round-gate.mjs --close` in a child repo is a sibling gate this task does not name; the
  contradiction reported in §7 is between the report's *claim of a `round-15` commit* and `git log`, which
  needs no gate to falsify.
- **Marker adjudication is size-and-structure based.** All 22 window files were measured by `stat`/`wc`
  and scanned for headings; the 6 report-path files among them were read in substance, and 3 of the 14
  scratch files were head-read. A full-text read of all 22 was not performed — the `<400 B` predicate is
  decisive here (smallest file 4,500 B), so the residual risk is a large file with no substance, which the
  line counts and heading scans exclude.

## 1. Reports landed in the window

Two independent methods, both run at `S4`: (a) `git log --diff-filter=A --since=2026-09-29T01:19:59Z
--format='%h %aI %an' --name-only -- .ufo/reports`, (b) `git ls-files -o --exclude-standard .ufo/reports`.

### 1.1 Tracked additions — 5 files

```console
$ git log --diff-filter=A --since=2026-09-29T01:19:59Z --format='%h %aI %an' --name-only -- .ufo/reports
b5fff81 2026-09-28T22:59:26-03:00 protocol-shokunin
.ufo/reports/round-12/kagi.md
.ufo/reports/round-12/kotoba.md
3485880 2026-09-28T22:56:45-03:00 Joao Pedro Veiga
.ufo/reports/round-15/kagi.md
3069841 2026-09-28T22:52:19-03:00 Joao Pedro Veiga
.ufo/reports/round-15/kake.md
cc6d9d4 2026-09-28T22:34:10-03:00 aggregator-shokunin
.ufo/reports/round-9/aggregator.md
```

| file | introducing commit | author | bytes (`stat -c%s`) | lines (`wc -l`) | marker? | `^#{1,6} *SHONEN` at |
|---|---|---:|---:|---:|---|---|
| `.ufo/reports/round-9/aggregator.md` | `cc6d9d4` | `aggregator-shokunin` | 18,604 | 201 | no | `:147` |
| `.ufo/reports/round-15/kake.md` | `3069841` | `Joao Pedro Veiga` | 7,486 | 135 | no | absent |
| `.ufo/reports/round-15/kagi.md` | `3485880` | `Joao Pedro Veiga` | 13,554 | 139 | no | absent |
| `.ufo/reports/round-12/kagi.md` | `b5fff81` | `protocol-shokunin` | 13,620 | 220 | no | absent |
| `.ufo/reports/round-12/kotoba.md` | `b5fff81` | `protocol-shokunin` | 14,009 | 224 | no | `:139` |

The two `round-12` files were **untracked at `S0`/`S1`** (they were the round-9 `D-144`/`D-145` cells) and
were swept into git at `S4` by `b5fff81` (author `protocol-shokunin`). That is a status move *inside* this
window, not a new report; `b5fff81`'s own message freezes `round-12/kotoba.md` "as-is, defect recorded,
attribution stays the lanes'".

Also modified (not added) in the window: `.ufo/reports/AGGREGATE.md` (`6415a9b`, `cc6d9d4`, both
`aggregator-shokunin`) and `.ufo/reports/round-14/kumitate.md` (`3d20676`, `Joao Pedro Veiga`) —
`git log --diff-filter=M --since=2026-09-29T01:19:59Z --format='%h %an' --name-only -- .ufo/reports`.

### 1.2 Untracked at contract paths — 17 files at `S4`

```console
$ git ls-files -o --exclude-standard .ufo/reports | wc -l
17
```

3 at a report contract path, 14 under `.ufo/reports/round-15/scratch/`:

| file | bytes | SHONEN |
|---|---:|---|
| `.ufo/reports/round-14/kagi.md` | 15,271 | absent |
| `.ufo/reports/round-14/kotoba.md` | 9,463 | absent |
| `.ufo/reports/round-15/kumitate.md` | 9,072 | `:147` |
| `.ufo/reports/round-15/scratch/LiveLabrat.md` | 4,500 | absent |
| `.ufo/reports/round-15/scratch/CheckPlanner.md` | 5,721 | absent |
| `.ufo/reports/round-15/scratch/TsvMutator.md` | 6,663 | absent |
| `.ufo/reports/round-15/scratch/SiblingConnector.md` | 8,656 | absent |
| `.ufo/reports/round-15/scratch/WaveDistiller.md` | 8,899 | absent |
| `.ufo/reports/round-15/scratch/ClassCritic.md` | 9,260 | absent |
| `.ufo/reports/round-15/scratch/PolicySentinel.md` | 10,294 | absent |
| `.ufo/reports/round-15/scratch/ItemReviewer.md` | 19,409 | absent |
| `.ufo/reports/round-15/scratch/DedupeSimplifier.md` | 20,813 | absent |
| `.ufo/reports/round-15/scratch/LogScribe.md` | 30,952 | absent |
| `.ufo/reports/round-15/scratch/ItemsScout.md` | 33,551 | absent |
| `.ufo/reports/round-15/scratch/HostScout.md` | 37,020 | absent |
| `.ufo/reports/round-15/scratch/ReportDraftExecutor.md` | 37,024 | absent |
| `.ufo/reports/round-15/scratch/EntryDraftExecutor.md` | 41,169 | absent |

mtime split against the cutoff (`ls -la --time-style=full-iso`): **16 of the 17 appeared after**
`22:19:59-03:00` (14 scratch files, mtimes `22:30:32`–`22:50:22`; plus `round-14/kagi.md` `22:21:02` and
`round-15/kumitate.md` `22:47:01`). The single carry-over is `.ufo/reports/round-14/kotoba.md`
(mtime `21:36:23`). At `S0` the untracked set was 19 = 5 report-path + 14 scratch; the two report-path
files that left the set during the run are `round-12/kagi.md` (`21:02:57`) and `round-12/kotoba.md`
(`20:25:33`), both swept by `b5fff81`.

### 1.3 Marker and `SHONEN` classification over the 22-file window set

Window set = the 5 tracked additions of §1.1 ∪ the 17 untracked files of §1.2 = **22 files**
(`git log --diff-filter=A --since=… --name-only .ufo/reports | grep -v '^$'` ∪
`git ls-files -o --exclude-standard .ufo/reports`, `sort -u`, `wc -l` → 22).

- **Markers: 0 of 22.** `<400 B` count = 0; every file is ≥ 4,500 B with a document body (headings,
  tables, cited commands). Per `PROTOCOL.md:176-181` the marker predicate is a contract-path file with no
  work behind it; nothing in the set qualifies. The round-8 marker class did not recur — a third
  consecutive refresh.
- **`SHONEN` heading: 3 of 22 carry it; 19 do not.** Two independent methods agree exactly:

```console
$ echo "$LIST" | xargs grep -lE '^#{1,6} *SHONEN' | wc -l          # method 1
3
$ echo "$LIST" | python3 -c "…pat=re.compile(r'^#{1,6} *SHONEN')…"  # method 2
3
.ufo/reports/round-12/kotoba.md
.ufo/reports/round-15/kumitate.md
.ufo/reports/round-9/aggregator.md
```

`PROTOCOL.md:139-142` makes the heading load-bearing: *"a report missing the `SHONEN` heading is a
conformance defect AND disqualified as evidence"*.

## 2. Untracked dispatch prompts (the `D-146` class)

```console
$ git ls-files -o --exclude-standard .ufo/prompts | wc -l
```

| stamp | count | list |
|---|---:|---|
| `S0` (`01:52`) | **10** | aggregator-round-10, kagi-round-14, kagi-round-15, kake-round-15, kama-round-1, kasegi-round-16, kotoba-round-15, kumitate-round-14, kumitate-round-15, protocol-round-13 |
| peak (`01:54`) | **11** | + `kumitate-round-16` (created `22:51:39-03:00`) |
| `S4` (`02:00`) | **2** | `kagi-round-16`, `kake-round-16` |

`D-146` was filed at round 9 with **5** prompts and owner *integrator*. This window: the count went
5 → 11 (six new dispatches between `22:22` and `22:51 -03:00`) and then **2**, because `b5fff81`
(author `protocol-shokunin`, `22:59:26-03:00`) committed **all 11** — so the durability fix was performed
by the **protocol** lane, not by the integrator `D-146` names. It was also performative-adjacent:
`fcefcf5` (`22:56:28-03:00`) *claimed* "11 generated prompts committed" while its diff carried **0**
prompt paths —

```console
$ git show --name-only --format='' fcefcf5 | grep -c prompts
0
$ git show --stat --format='' b5fff81 | grep -c '\.ufo/prompts/'
11
```

Which prompt disappeared when: the **five window-dispatched** prompts are `aggregator-round-10`
(mtime `22:37:20`), `kagi-round-15` (`22:22:18`), `kama-round-1` (`22:44:07`), `kumitate-round-15`
(`22:22:15`) and `kumitate-round-16` (`22:51:39`); `kasegi-round-16` (`22:14:43`) predates the cutoff. The
five carried from round 9 (`kagi-round-14` `21:52:08`, `kake-round-15` `21:44:24`, `kotoba-round-15`
`21:36:52`, `kumitate-round-14` `21:52:02`, `protocol-round-13` `21:51:57`) were the round-9 `D-146` list
itself — all swept by `b5fff81`, so that set is now closed.

## 3. `MANIFEST.json` — last-wins recompute and the `D-143` re-test

### 3.1 Keying rule, quoted

`PROTOCOL.md:265-270`: *"**A row names the lane-round it describes.** `lanes` values stay status strings;
the optional `lane_rounds: {<id>: <n>}` map records a lane's own counter where it differs from the entry's
`round` … so last-wins is computed over `(id, entry.round)`; reading the map as the key erases in-flight
debt"*. Both keyings are computed below; the protocol-correct one is `(id, entry.round)`.

### 3.2 Script (runtime commands are python3-only; this is the exact text executed)

```python
#!/usr/bin/env python3
"""MANIFEST.json `rounds` last-wins tally + M3 stale-row scan.  Keying: (id, entry.round)."""
import json, re, os, sys, subprocess, datetime
from collections import Counter, defaultdict

def dt(s): return datetime.datetime.fromisoformat(s)

rounds = json.load(open(sys.argv[1]))["rounds"]
print("entries=%d HEAD=%s" % (len(rounds),
      subprocess.run(["git","rev-parse","--short","HEAD"],capture_output=True,text=True).stdout.strip()))

wl = open(".ufo/watchdog.log", encoding="utf-8", errors="replace").read().splitlines()
launch, complete, steers = {}, {}, defaultdict(list)
for l in wl:
    ts = l.split(" ")[0]
    for pat, d in ((r"launch (\w+) round=(\d+)", launch), (r"complete (\w+) round=(\d+)", complete)):
        m = re.search(pat, l)
        if m: d[(m.group(1), int(m.group(2)))] = ts
    m = re.search(r"steer (\w+) -> round (\d+)", l)
    if m: steers[(m.group(1), int(m.group(2)))].append(ts)

def terminated(lane, n):
    if (lane, n) in complete: return ("complete", complete[(lane, n)])
    later = [r for (la, r) in launch if la == lane and r > n]
    if later: return ("counter-passed", launch[(lane, min(later))])
    return (None, None)

tracked = set(subprocess.run(["git","ls-files",".ufo/reports"],capture_output=True,text=True).stdout.split())
def rpath(lane, n): return ".ufo/reports/round-%d/%s.md" % (n, lane)

lw, hist = {}, defaultdict(list)
for i, e in enumerate(rounds):
    for lane, st in (e.get("lanes") or {}).items():
        lw[(lane, e["round"])] = st; hist[(lane, e["round"])].append(i)
print("last-wins rows=%d tally=%s" % (len(lw), dict(sorted(Counter(lw.values()).items()))))

lw2 = {}
for e in rounds:
    lr = e.get("lane_rounds") or {}
    for lane, st in (e.get("lanes") or {}).items():
        lw2[(lane, lr.get(lane, e["round"]))] = st
print("lane_rounds-keyed rows=%d tally=%s" % (len(lw2), dict(sorted(Counter(lw2.values()).items()))))

viol = 0; stale = 0
for (lane, n), st in sorted(lw.items()):
    e = rounds[hist[(lane, n)][-1]]
    closed = e.get("closed_at")
    if closed is None: continue
    c = dt(closed); tk, tt = terminated(lane, n)
    lts = launch.get((lane, n)) or (steers.get((lane, n)) or [None])[0]
    rp = rpath(lane, n); landed = rp in tracked
    why = None
    if st == "not-dispatched":
        if lts and dt(lts) <= c: why = "AT closed_at: vs dispatch %s" % lts; viol += 1
        elif lts: why = "NOW STALE: dispatch exists %s" % lts; stale += 1
    elif st == "in-flight":
        if tt and dt(tt) <= c: why = "AT closed_at: vs termination %s" % tt; viol += 1
        elif tt: why = "NOW STALE vs termination(%s) %s" % (tk, tt); stale += 1
        elif landed: why = "NOW STALE vs landed report %s" % rp; stale += 1
    elif st == "ok":
        if tk is None: why = "ok but no termination evidence"; viol += 1
        elif not os.path.exists(rp): why = "ok but no report at %s" % rp; viol += 1
    if why: print("  (%s,%d) [%s] entry#%d  %s" % (lane, n, st, hist[(lane, n)][-1], why))
print("contradictions=%d  (AT-closed_at=%d, NOW-STALE=%d)" % (viol + stale, viol, stale))
```

### 3.3 `S4` rows that are stale at read time, against live evidence

Report-path existence and the watchdog launch/complete lines (`grep -nE '<lane>' .ufo/watchdog.log | tail`):

| lane | round | row status | entry# | `closed_at` | report path exists | watchdog evidence (file:line) |
|---|---|---:|---:|---|---|---|
| `aggregator` | 9 | `in-flight` | #43 | `2026-09-28T22:23:00-03:00` | `.ufo/reports/round-9/aggregator.md` **True** (18,604 B) | `watchdog.log:246` `22:37:20 complete aggregator round=9; respawning` |
| `aggregator` | 10 | `not-dispatched` | #13 | `2026-09-28T18:21:16-03:00` | `.ufo/reports/round-10/aggregator.md` **False** | `watchdog.log:247` `22:37:21 launch aggregator round=10 runId=shokunin-r10-aggregator-r1790645840` |
| `kagi` | 15 | `in-flight` | #45 | `2026-09-28T22:23:00-03:00` | `.ufo/reports/round-15/kagi.md` **True** (13,554 B) | `watchdog.log:256` `22:59:14 complete kagi round=15; respawning` |
| `kake` | 15 | `in-flight` | #45 | `2026-09-28T22:23:00-03:00` | `.ufo/reports/round-15/kake.md` **True** (7,486 B) | `watchdog.log:254` `22:59:12 complete kake round=15; respawning` |
| `kumitate` | 15 | `in-flight` | #45 | `2026-09-28T22:23:00-03:00` | `.ufo/reports/round-15/kumitate.md` **True** (9,072 B, *untracked*) | `watchdog.log:251` `22:51:39 complete kumitate round=15; respawning` |

`AT-closed_at = 0` at every stamp: each closure pass wrote rows internally consistent at its own
`closed_at`; the drift is the runtime that outran them. Row count is **120** (not 112) since `ae19fca`,
because the closure pass appended **11 entries** — 1 `closure` (round 15) + 10 `closure-correction`
(entries #37–#47, all carrying `closed_at 2026-09-28T22:23:00-03:00`; `python3 -c "import json; r=json.load(open('MANIFEST.json'))['rounds']; [print(i,e['round'],e['type'],e.get('closed_at'),e.get('lanes')) for i,e in enumerate(r[36:],36)]"`).

`lane_rounds`-keyed tally at `S4` — **101 rows, 83 ok / 3 failed / 4 in-flight / 11 not-dispatched**, i.e.
the diagnosed trap's shape reproduced (it erases 4 of the 7 `in-flight` rows and 7 of the 18
`not-dispatched` rows). `not-dispatched` rows missing a required `lane_rounds` map: **0 of 18**.

### 3.4 `D-143` re-test — two stamps ≥ 60 s apart, and what actually moves the count

| interval | wall gap | stale count | moved? | what landed in the interval |
|---|---:|---|---|---|
| `S0 → S1` | **62 s** | 10 → 10 | **no** | nothing: last watchdog event `22:51:41-03:00` (`01:51:41Z`), before both stamps |
| `S1 → S2` | 2 m 19 s | **10 → 4** | **yes, −6** | `ae19fca` closure pass, 11 `rounds` entries appended (37 → 48), 8 corrections |
| `S2 → S3` | 84 s | **4 → 5** | **yes, +1** | `.ufo/reports/round-15/kagi.md` landed and was committed (`3485880`) |
| `S3 → S4` | 3 m 33 s | 5 → 5 | **no** | watchdog completed kagi/kake r15 (`22:59:12/14`) but those rows were already counted stale |

**Required pair (`S0`/`S1`, 62 s): the stale count did not move.** Across the four intervals it *did* move,
in both directions, and the direction is explained by which cadence fired: a closure pass cuts it (10 → 4
in 2 m 19 s), ordinary lane activity raises it (+1 per report landing or respawn). `D-143`'s round-9
wording — "8 rows stale, **doubling** 4 → 8 in 2 m 08 s **with no entry appended**" — is **not**
reproduced in this window: the only large move came *with* eleven entries appended. What is reproduced is
the underlying defect: `MANIFEST.json` still carried **10** stale rows at the top of the window and still
carries **5**, two of which (`aggregator` 9 and `aggregator` 10, this lane's own pair) are the aggregator's
own respawn at `22:37:20-03:00` never being closed. Net: **still open**, magnitude cadence-driven rather
than monotone.

## 4. Child corpora since the cutoff (the six rostered-at-cutoff repos)

`git -C <repo> log --since=2026-09-29T01:19:59Z --format='%h %aI %an %s'`, stamped `S4`
`2026-09-29T02:00:51Z`. Scope note: **six** = the repos in `MANIFEST.json` `roster` at the cutoff
(`kasegi,kengaku,kake,kumitate,kotoba,kagi`); the seventh lane minted mid-wave is §6.

| child repo | live HEAD at `S4` | dirty (`status --porcelain`) | commits in window | author split |
|---|---|---:|---:|---|
| `kasegi-shokunin` | `b021dc9` | 1 | **0** | — |
| `kengaku-shokunin` | `e171cdf` | 4 | **0** | — |
| `kake-shokunin` | `88a4f4e` | 0 | **1** | `Joao Pedro Veiga <jpveigao10@gmail.com>` 1 |
| `kumitate-shokunin` | `637d181` | 7 | **1** | `Joao Pedro Veiga <jpveigao10@gmail.com>` 1 |
| `kotoba-shokunin` | `0f658ff` | 11 | **0** | — |
| `kagi-shokunin` | `587fda0` | 0 | **2** | `Joao Pedro Veiga <jpveigao10@gmail.com>` 2 |

The four window commits:

- `kake` `88a4f4e` `2026-09-28T22:52:13-03:00` "round-15: freshness 8->9 — citation-base re-sweep caught FS drift …"
- `kumitate` `637d181` `2026-09-28T22:19:59-03:00` "round-14 close evidence: --close CLEAN (round=14 checks=13 errors=0) …"
- `kagi` `2486643` `2026-09-28T22:27:11-03:00` "round-14: freshness axis-move — knowledge-entry re-verification declarations …"
- `kagi` `587fda0` `2026-09-28T22:56:34-03:00` "round-15: operability axis-move — the credential-hygiene checklist becomes an executed declaration …"

**Attribution: 4 of 4 window child commits carry the operator identity, 0 carry a lane identity** —
`git -C <repo> log --since=… --format='%an <%ae>'`. That restates the `D-111`/`D-112`/`D-113`/`D-115`/`D-92`
class at r14/r15 rather than closing it. Orientation only: dirty counts move while the fleet runs
(`kake` 0 → 0, `kumitate` 6 → 7, `kagi` 6 → 12 → 0 across the three reads; `P-s`).

**Round-9 mirror still tracked at HEAD — 6 of 6:**

```console
$ git -C <repo> ls-files corpus/lessons | grep round-9-aggregator
corpus/lessons/round-9-aggregator-corpus-verdict.md      # kasegi, kengaku, kake, kumitate, kotoba, kagi
```

And the mirrored bytes are a faithful copy of the aggregator's committed lesson, 6 of 6
(`cmp -s .ufo/waves/round-9/lessons/round-9-aggregator-corpus-verdict-<r>.md <r>-shokunin/corpus/lessons/round-9-aggregator-corpus-verdict.md`
→ BYTE-IDENTICAL; sha256 prefixes `c4786b889bc083d9` / `8cfce8ccbd275324` / `f72837aae404a3de` /
`2cb6fe086a4c52a6` / `51b1dfedbfc02254` / `9105581bc3b6fd80` for kasegi/kengaku/kake/kumitate/kotoba/kagi).

## 5. Did the round-9 mirror become durable?

```console
$ git -C <repo> merge-base --is-ancestor <sha> origin/master && echo YES || echo NO
$ git -C <repo> rev-parse --short origin/master
```

| repo | mirror sha | `origin/master` at `S4` | contained? | verdict |
|---|---|---|---|---|
| `kasegi` | `b021dc9` | `0f2dca0` | **NO** | local-only; `origin/master..master` = 1 |
| `kengaku` | `e171cdf` | `f09ff1f` | **NO** | local-only; behind by 1 |
| `kake` | `4214101` | `88a4f4e` | **YES** | durable — but **only because the lane pushed its own `88a4f4e`** (`22:52:13-03:00`, inside this window), which carries `4214101` as ancestor |
| `kumitate` | `93b0567` | `637d181` | **YES** | durable since round 9 (the lane's `637d181` rode it) |
| `kotoba` | `0f658ff` | `3ea0e08` | **NO** | local-only; behind by 3 |
| `kagi` | `baec94f` | `587fda0` | **YES** | durable — flipped **inside this window** by the lane's own `587fda0` push (`22:56:34-03:00`) |

**3 of 6 contained, 3 of 6 local-only** (was 1 of 6 at round 9's end). Both new flips are incidental: the
mirror became durable because a *lane* happened to commit on top of it and push, not because the
aggregator took an action. `MISSION.md:49-56` gives this lane no sibling remote — *"Lanes push ONLY to
`VeigaPunk/shokunin` (main repo) or their own `VeigaPunk/<lane>-shokunin` remote"* — so the three
remaining mirrors (`kasegi`, `kengaku`, `kotoba`) survive only in one local object database, and the
round-9 verdict lesson for those three is one `git gc`/re-clone away from being non-re-derivable.

## 6. Mid-round scope change (folded in per the L1's `01:59:54Z` note)

**A seventh lane was minted while this wave ran.** `2d19a64` (author `integrator`,
`2026-09-28T22:44:21-03:00`, "sibling-mint allowance + kama probation entry") corresponds to
`kama-shokunin/`, measured by this seat at `S4`:

```console
$ git -C kama-shokunin rev-parse --short HEAD          -> 9cee9fc
$ git -C kama-shokunin ls-files | wc -l                -> 7
$ git -C kama-shokunin status --porcelain | wc -l      -> 9
$ git -C kama-shokunin remote -v                       -> origin https://github.com/VeigaPunk/kama-shokunin.git
$ git ls-files kama-shokunin | wc -l                   -> 0      # not in main index
$ grep -c kama .gitignore                              -> 0      # .gitignore lists only the six
```

**Correction to the L1 note's wording:** `MANIFEST.json` `roster` **does not** contain `kama`. The mint
entry (`rounds[36]`, `round 11.5`, type `mint`) records it in `notes` only —
*"kama-shokunin minted in probation … **Roster row withheld until >=3 verified self-iteration rounds per
the new clause**"* — and `python3 -c "…[r['name'] for r in json.load(open('MANIFEST.json'))['roster']]"`
returns exactly the six. So the roster is correctly still six; `kama` is a probationary lane wired into
the watchdog (`.ufo/state/kama.{mission,round}` untracked; `22:44:08 launch kama round=1
runId=shokunin-r1-kama-r1790646247`). Every "six child repos" cell in §4/§5 above is therefore the
*rostered-at-cutoff* six, and `kama` is outside them — `not-run` by this seat: the seat contract permits
only read-only sibling gates named in the task, and this task names none. The L1's own gate measurement
(`--repo kama-shokunin --round 10` → exit 1, 12 findings, `dirty=9 provisional=1`,
`corpus/knowledge/` + `corpus/lessons/` untracked at `9cee9fc`) is cited as L1-measured, not as a cell
this seat executed.

**Cross-lane attribution incident, verified from this seat:**

```console
$ git show --stat --format='%h %an %aI' fcefcf5
fcefcf5 protocol-shokunin 2026-09-28T22:56:28-03:00
 .ufo/waves/round-10/CONTEXT.md                     |  81 ++++
 ...-shokunin-round-10-aggregator-corpus-verdict.md | 175 ++++++++
 .ufo/waves/round-10/scratch/ledger-15-skeleton.md  | 479 +++++++++++++++++++++
 .ufo/waves/round-10/seats/distiller-queue.md       |  76 ++++
 .ufo/waves/round-10/seats/labrat-probes.md         | 126 ++++++
 .ufo/waves/round-10/seats/revenger-rule4-intent.md |  66 ++++
 .ufo/waves/round-10/seats/reviewer-citations.md    |  47 ++++
 .ufo/waves/round-10/seats/sentinel.md              |  51 ++++
 8 files changed, 1101 insertions(+)
$ git log --diff-filter=A --format='%h %an' -1 -- .ufo/waves/round-10/CONTEXT.md
fcefcf5 protocol-shokunin
```

`fcefcf5` committed **8 files of this lane's in-flight `.ufo/waves/round-10/` including `CONTEXT.md`** —
a lane main-repo commit carrying non-report paths, the `D-83` class — while its message claims *"11
generated prompts committed"* (diff carries 0 prompt paths) and *"`.ufo/waves/round-9 + round-10` … which
the aggregator's ledger 14 claimed committed while `git ls-files` returned 0"*. **That second claim is
false**, and the two commands that falsify it are:

```console
$ git log --diff-filter=A --format='%h %aI %an' -1 -- .ufo/waves/round-9/corpus-gate.mjs
6415a9b 2026-09-28T22:29:46-03:00 aggregator-shokunin
$ git ls-tree -r a2cac72 --name-only .ufo/waves/round-9 | wc -l
25
```

`b5fff81` (same lane, 3 m later) self-reports the miss: *"corrects fcefcf5, whose message claimed 11
prompts + 2 orphan reports + round-9/round-10 waves but whose diff carried only 8 round-10 files — a
`git add` aborted on a mistyped pathspec and the error was swallowed by `2>/dev/null`"*. The wave files
that were genuinely uncommitted are the `round-10/lessons/*-shokunin-round-10-aggregator-corpus-verdict.md`
set — **3** still untracked at `S4` (kake, kengaku, kumitate), **4** at the final re-read (kotoba added),
`git status --porcelain | grep '^??'` — which is this lane's own durability defect, not round-9's.

## 7. New defect candidates read out of the newest lane reports

Read at `S4`: `.ufo/reports/round-13/*.md` (5), `round-14/*.md` (5), `round-15/*.md` (4 — kagi landed at
`3485880` before `S4`). Candidates only — **no `D-` keys assigned here** (the distiller seat assigns them).

Every banned token quoted in this section (`LANE_HASH`, `{{…}}`, `TODO`, `[PENDING]`) appears in *this*
file only inside a quotation of another artifact's text, with the source path and line given; none is an
unfilled slot of this deliverable.

- **`round-15/kumitate.md` is an unlanded report.** It claims a `round-15` commit and a push that do not
  exist. `git -C kumitate-shokunin log --all --grep='round-15'` → **empty**; `rev-parse --short HEAD` →
  `637d181` (whose subject is the *round-14* close); the round's own artifact
  `corpus/knowledge/runtime-remainder-census.md` and `corpus/lessons/round-15.md` are still untracked in
  the worktree (`status --porcelain` → 7 lines, two `??`). Evidence pointer the report gives for the
  claim: `.ufo/reports/round-15/kumitate.md:130` "Close evidence (lane HEAD after the `round-15` commit,
  pushed):". Same class as `PROTOCOL.md:541` (kagi r12).
- **`round-14/kotoba.md` is a draft filed at the contract path.** Title: *"kotoba — round 14 report
  (DRAFT — pending batch-2 verdicts)"*; nine lines carry a `PENDING` token — `grep -n 'PENDING'
  .ufo/reports/round-14/kotoba.md` → `:4` (`**[PENDING \`R14Critic\`]**`), `:11`, `:52` (heading "## 4.
  Non-author verification (L2 batch 2) — [PENDING]"), `:54-58` (all five batch-2 lanes), `:131` (trailer
  `[PENDING: final score, critic verdict, rebuilder numbers, post-mutation escapes]`) — of which the
  literal bracket form `[PENDING]` appears 7 times (`grep -noE '\[PENDING\]' | wc -l`). The driver read the
  path's existence as completion: `grep -n 'complete kotoba round=14' .ufo/watchdog.log` →
  `222:2026-09-28T21:36:52-03:00 complete kotoba round=14; respawning`, i.e. 29 s after the file's mtime
  (`21:36:23`).
- **`LANE_HASH` placeholder still committed.** `grep -rln 'LANE_HASH' .ufo/reports` →
  `.ufo/reports/round-12/kotoba.md:224` *("- Commit: \`LANE_HASH\` in \`kotoba-shokunin\`…")* and
  `.ufo/reports/round-12/protocol.md` (5 mentions, incl. `:232`). `LANE_HASH` is one of the three tokens
  the round contract names as a placeholder. `b5fff81` swept both files into git "as-is, defect recorded".
- **`{{…}}` draft slots in the r15 scratch set.** `round-15/scratch/LogScribe.md` 37 × `{{`, and
  `ReportDraftExecutor.md` 143 × `{{` + 3 × `TODO` — a shared draft-report template with unfilled slots
  (`{{WAVE_OTHER}}` `LogScribe.md:158`, `{{ROUND15_COMMIT}}` `ReportDraftExecutor.md:12`, where the
  template text already reads "commit **`round-15`** (`{{ROUND15_COMMIT}}`)"); scratch, not a contract-path
  report, so the placeholder ban is at most advisory here — but it is the same unfilled-slot pattern the
  kumitate claim above exhibits.
- **The `SHONEN`-heading debt is stationary.** 11 of the 14 child-lane reports in rounds 13–15 lack the
  heading —

```console
$ ls .ufo/reports/round-1[345]/*.md | xargs grep -LE '^#{1,6} *SHONEN' | wc -l
11     # of 14; kumitate is the only lane carrying it in all three rounds
```

  and the delivery channel does not carry it either: `grep -l 'SHONEN' .ufo/prompts/*.md | wc -l` → **1
  of 100** prompt files (`.ufo/prompts/kasegi-L1.md`); the other four elements `PROTOCOL.md:89` requires
  a child prompt to embed are also absent from the generated template — `grep -liE 'commit-before-report|before the report'`
  → 0 of 100, `grep -liE 'commit hash|hash citation|commit-hash'` → 0 of 100. `kagi-round-16.md` (untracked,
  read in full) carries the report path and an informal "commit 'round-16' inside the repo then push; also
  commit+push the main-repo report", and no `SHONEN` requirement at all. This is the `PROTOCOL.md:517`
  appendix row ("Prompt embeds contract") re-measured: it was 0 of 58 prompts, it is 1 of 100.
- **Report-before-commit at ≈6–7 s.** `.ufo/reports/round-15/kake.md` mtime `22:52:05.590`, its child work
  commit `88a4f4e` at `22:52:13-03:00` (−7.4 s); `.ufo/reports/round-15/kagi.md` mtime `22:56:27.668`, child
  work commit `587fda0` at `22:56:34-03:00` (−6.3 s). `ls -la --time-style=full-iso` +
  `git -C <repo> log -1 --format='%cI' <sha>`.
- **`~/Projects/bounties` is still cited everywhere.** `round-15/kasegi.md` measures 339 references across
  the 8 lane repos + main (221 path-shaped, 133 inside `corpus/knowledge/`), 704 genuine citations pointing
  at files that no longer exist, `0/18` surfaces present — and its own `PROVINCE.md` is unchanged
  (`D-135`/`D-150` restated).
- **The aggregator's mirrored artifacts are the only remaining hard error in a sibling gate.**
  `round-15/kumitate.md` verification section: *"the repo-wide `errors=14` remain exactly the two
  third-party aggregator artifacts"* — i.e. this lane's own two files in `kumitate-shokunin` are that
  repo's entire error set.
- **Resolved inside this window (recorded for the tally, not as new debt):** `D-144`
  (`.ufo/reports/round-12/kagi.md` untracked) and the whole `D-146` prompt list — `b5fff81` committed
  `round-12/kagi.md`, `round-12/kotoba.md` (the other round-12 orphan, not previously keyed) and all 11
  prompts. **`D-145` is *not* resolved**: `.ufo/reports/round-14/kotoba.md` is still untracked at `S4`.
  Round 14's kake-side self-report (`.ufo/reports/round-14/kake.md:108-112`: its own `round-13/kake.md`
  "commits in both repos" claim was false on the main-repo half) is repaired, `round-13/kake.md` being
  tracked at `S4`.

## Findings

1. **`D-143` holds but its shape changed.** Two stamps 62 s apart: 10 → 10, no movement. Over the whole
   window it moved in both directions — 10 → 4 when `ae19fca` appended 11 `rounds` entries, 4 → 5 when one
   lane report landed. The row count itself grew 112 → 120, so the round-9 "no entry appended" doubling
   shape did not recur; the residue (5 stale rows, 2 of them this lane's own `aggregator 9`/`aggregator 10`
   pair) is real and unfixed.
2. **The window's durability wins were all incidental.** Untracked files at contract paths went 19 → 17,
   and the prompts 11 → 2, but the moves were made by `protocol-shokunin` committing *other* lanes'
   artifacts, and the mirror's `origin` durability for `kake`/`kagi` came from those lanes' own pushes —
   not from any owner or from this lane.
3. **Zero markers for the third consecutive refresh, and 0 of 22 window files below 400 B.**
4. **The `SHONEN` heading debt did not move**: 11 of 14 in rounds 13–15, 3 of 22 in the window set,
   1 of 100 prompts carrying the requirement.
5. **`round-15/kumitate.md` is the sharpest new cell**: a report asserting a pushed `round-15` commit that
   `git log --all --grep` cannot find, with the round's artifact untracked.
6. **A seventh lane appeared mid-wave and is correctly *not* on the roster** (probation clause); main-repo
   `.gitignore` and the index know nothing about `kama-shokunin/`, so it shows as an untracked nested repo.
7. **This lane's own window debt, and the incident it caused**: the round-10 wave files were left
   uncommitted, so `fcefcf5` (protocol) swept them — including `CONTEXT.md` — and
   `round-10/lessons/{kake,kengaku,kumitate}-shokunin-round-10-aggregator-corpus-verdict.md` are still
   untracked at `S4` (a fourth, kotoba, at the final re-read); `git status --porcelain | grep '^??'`.

## Drift log — cells that moved while this seat ran

| cell | value at `S0` (`01:52`) | value at `S4` (`02:00`) | cause |
|---|---|---|---|
| main HEAD | `3069841` | `b5fff81` | 6 commits landed inside the seat's run |
| `MANIFEST.json` md5 / entries / last-wins rows | `df487629…` / 37 / 112 | `3f6dd15c…` / 48 / 120 | `ae19fca` closure pass (11 entries) |
| last-wins tally | 83 / 4 / 7 / 18 | **91** / 4 / 7 / 18 | same closure pass |
| NOW-STALE count | 10 | 5 | closure pass (−6), one report landing (+1) |
| untracked reports | 19 (5 report-path + 14 scratch) | 17 (3 report-path + 14 scratch) | `b5fff81` swept `round-12/{kagi,kotoba}.md` |
| untracked prompts | 10 | 2 | `b5fff81` committed all 11 of the peak set (2 new r16 prompts appeared after) |
| child `kagi` mirror in `origin` | NO | YES | kagi pushed its own `587fda0` |
| child `kake` mirror in `origin` | NO | YES | kake pushed its own `88a4f4e` |
| `kagi-shokunin` HEAD / dirty | `2486643` / 12 | `587fda0` / 0 | lane committed and pushed r15 |

`P-s` applies to every child row: the audit identity is the revision *and* the dirty count observed.

## Candidate rows

No keys — the distiller seat assigns them. Severity 1 (cosmetic) … 5 (blocking).

| # | owner | sev | defect | evidence (command or `file:line`) |
|---|---|---:|---|---|
| C1 | kumitate | 4 | r15 report asserts a `round-15` commit + push that do not exist; the round's artifact and lesson are untracked worktree files | `.ufo/reports/round-15/kumitate.md:130`; `git -C kumitate-shokunin log --all --grep='round-15'` → empty; `git -C kumitate-shokunin rev-parse --short HEAD` → `637d181`; `git -C kumitate-shokunin status --porcelain` → 7 lines |
| C2 | kumitate | 3 | `.ufo/reports/round-15/kumitate.md` (9,072 B) untracked at its contract path while the driver completed the round on it | `git ls-files -o --exclude-standard .ufo/reports`; `grep -n 'complete kumitate round=15' .ufo/watchdog.log` → `:251` |
| C3 | kagi | 3 | `.ufo/reports/round-14/kagi.md` (15,271 B) untracked at its contract path (`D-144` restated at r14) | `git ls-files -o --exclude-standard .ufo/reports` |
| C4 | kotoba | 4 | `.ufo/reports/round-14/kotoba.md` is a DRAFT filed at the contract path (9 `PENDING` lines, 5 of 5 batch-2 lanes unresolved) and the driver completed the round on its existence; also untracked | `.ufo/reports/round-14/kotoba.md:1,4,11,52,54-58,131`; `grep -n 'PENDING' .ufo/reports/round-14/kotoba.md`; `watchdog.log:222` |
| C5 | kotoba + protocol | 3 | committed report carries the literal `LANE_HASH` placeholder; protocol swept it in "as-is" | `grep -rln 'LANE_HASH' .ufo/reports` → `round-12/kotoba.md:224`, `round-12/protocol.md:232`; `b5fff81` message |
| C6 | aggregator (+ operator, per `MISSION.md:49-56`) | 4 | round-9 lesson mirror still local-only in 3 of 6 repos; the 2 new durable ones became so incidentally via lane pushes | `git -C <repo> merge-base --is-ancestor <sha> origin/master` → NO for kasegi `b021dc9`, kengaku `e171cdf`, kotoba `0f658ff` |
| C7 | integrator (prompt template) + every child lane | 4 | 11 of 14 child-lane reports in rounds 13–15 carry no `^#{1,6} *SHONEN` heading; 1 of 100 prompts embeds the requirement (`PROTOCOL.md:89`, `:139-142`) | `ls .ufo/reports/round-1[345]/*.md \| xargs grep -LE '^#{1,6} *SHONEN' \| wc -l` → 11; `grep -l 'SHONEN' .ufo/prompts/*.md \| wc -l` → 1 of 100 |
| C8 | protocol-shokunin | 4 | `fcefcf5` committed 8 files of another lane's in-flight `.ufo/waves/round-10/` incl. `CONTEXT.md` (`D-83` class); its message's claim that round-9's wave was uncommitted is false | `git show --stat fcefcf5`; `git log --diff-filter=A -1 -- .ufo/waves/round-10/CONTEXT.md` → `fcefcf5`; `git ls-tree -r a2cac72 --name-only .ufo/waves/round-9 \| wc -l` → 25 |
| C9 | protocol | 4 | this lane's own pair of MANIFEST rows unchanged across the window: 5 stale rows at `S4`, incl. `aggregator 9` (`in-flight`) and `aggregator 10` (`not-dispatched`) | §3.3 table; `seats/sweep-window.md` §3.2 script |
| C10 | kagi, kake, kumitate (operator-identity commits) | 3 | all 4 window child commits carry `Joao Pedro Veiga <jpveigao10@gmail.com>`, none a lane identity | `git -C <repo> log --since=2026-09-29T01:19:59Z --format='%an <%ae>'` |
| C11 | kake, kagi | 2 | r15 reports filed ≈7 s / ≈6 s before their own round-work commits (commit-before-report ordering) | `ls -la --time-style=full-iso .ufo/reports/round-15/{kake,kagi}.md`; `git -C kake-shokunin log -1 --format='%cI' 88a4f4e` |
| C12 | kasegi (+ every lane citing the absent root) | 3 | `~/Projects/bounties` still named; 704 genuine citations point into absent files; `PROVINCE.md` unchanged (`D-135`/`D-150` restated) | `.ufo/reports/round-15/kasegi.md` §Scorecard + §Adjacency |
| C13 | integrator | 2 | `kama-shokunin/` absent from main `.gitignore` and index ⇒ untracked nested repo in the main tree; `.ufo/state/kama.{mission,round}` untracked | `.gitignore` (6 lines, no `kama`; `grep -c kama .gitignore` → 0); `git ls-files kama-shokunin \| wc -l` → 0; `git status --porcelain \| grep -c '^??'` → **14 at `S4` (`02:00:19Z`), 20 at the final re-read (`02:07:54Z`)** — the growth is sibling seat files, a new root `PROTOCOL-APPENDIX.md`, and a fourth `round-10/lessons/kotoba-shokunin-…` file |
| C14 | kotoba, kagi | 3 | lane-authored scratch under the reports tree carries unfilled draft slots (`{{…}}` ×180, `TODO` ×3) — advisory only, scratch is not a contract-path report | `grep -cE '\{\{' .ufo/reports/round-15/scratch/{LogScribe,ReportDraftExecutor}.md` → 37, 143 |
| C15 | aggregator | 2 | this lane's own mirrored round-10 lessons are untracked — **3** at `S4` (kake, kengaku, kumitate), **4** at the final re-read (kotoba added) (the same durability class it files against others) | `git status --porcelain \| grep '^??'` |

## Re-run commands

```bash
# 0. stamp: confirm you are at b5fff81 (or say which revision your cells name)
cd /home/vgpnk/projects/shokunin && date -u +'%Y-%m-%dT%H:%M:%SZ' && git rev-parse --short HEAD

# 1. window commit set (main) — two independent methods must agree
git log --since=2026-09-29T01:19:59Z --format='%h %cI %an %s'
git log --diff-filter=A --since=2026-09-29T01:19:59Z --format='%h %aI %an' --name-only -- .ufo/reports
git log --diff-filter=M --since=2026-09-29T01:19:59Z --format='%h %aI %an' --name-only -- .ufo/reports

# 2. untracked sets
git ls-files -o --exclude-standard .ufo/reports
git ls-files -o --exclude-standard .ufo/prompts        # D-146 class

# 3. per-file size + marker + SHONEN (two methods)
LIST=$( { git log --diff-filter=A --since=2026-09-29T01:19:59Z --name-only --format='' -- .ufo/reports \
          | grep -v '^$'; git ls-files -o --exclude-standard .ufo/reports; } | sort -u )
echo "$LIST" | xargs stat -c '%s B %n' | sort -n            # marker = any < 400 B
echo "$LIST" | xargs grep -lE '^#{1,6} *SHONEN' | wc -l     # method 1
echo "$LIST" | xargs grep -LE '^#{1,6} *SHONEN' | wc -l     # complement (19)

# 4. MANIFEST last-wins + stale rows: paste the §3.2 script and run
python3 - MANIFEST.json <<'PY'
# … §3.2 script verbatim …
PY

# 5. child corpora since the cutoff, by author, + mirror tracked
for r in kasegi kengaku kake kumitate kotoba kagi; do
  git -C $r-shokunin log --since=2026-09-29T01:19:59Z --format='%h %aI %an <%ae> %s'
  git -C $r-shokunin ls-files corpus/lessons | grep round-9-aggregator
done

# 6. mirror durability in origin
for pair in kasegi:b021dc9 kengaku:e171cdf kake:4214101 kumitate:93b0567 kotoba:0f658ff kagi:baec94f; do
  r=${pair%%:*}; s=${pair##*:}
  printf '%-9s %s in_origin=%s\n' "$r" "$s" \
    "$(git -C $r-shokunin merge-base --is-ancestor $s origin/master && echo YES || echo NO)"
done

# 7. stale-row live evidence
for lane in aggregator kagi kake kotoba kumitate protocol; do echo "== $lane"; grep -nE "$lane" .ufo/watchdog.log | tail -4; done

# 8. seventh lane (outside the six)
git -C kama-shokunin rev-parse --short HEAD; git -C kama-shokunin ls-files | wc -l
git ls-files kama-shokunin | wc -l; grep -c kama .gitignore
python3 -c "import json;print([r['name'] for r in json.load(open('MANIFEST.json'))['roster']])"

# 9. attribution incident
git show --stat --format='%h %an %aI' fcefcf5
git ls-tree -r a2cac72 --name-only .ufo/waves/round-9 | wc -l
```