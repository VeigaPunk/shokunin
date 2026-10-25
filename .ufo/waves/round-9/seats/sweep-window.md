# Seat `SweepWindow` — main-repo sweep of everything landed since the round-8 cutoff

Round-9 aggregator wave (fleet-2), L2 seat. Author: subagent `SweepWindow` (aggregator L1 identity).
Write scope: this file only. Read-only git throughout (`log`, `show`, `rev-list`, `ls-files`, `rev-parse`);
the only writes are two `/tmp/m_<rev>.json` blobs produced by `git show <rev>:MANIFEST.json >`, which the
seat contract permits for archive-style extraction and which this seat cannot delete without a host mutation.

## 0. Measurement stamp

| Field | Value |
|---|---|
| Wall time of final stamp | `2026-09-29T00:50:37Z` |
| Main HEAD measured for §1–§7 | `a197445` (`a197445d0b06f463a188d22a28218cd10c302f15`), stamped `2026-09-29T00:50:37Z` |
| Main HEAD at first measurement | `1dc7f6b`, then `62fdfbe`, then `a197445` — HEAD moved twice inside this seat's run |
| Main HEAD at the last re-check | `383ea1a`, stamped `2026-09-29T00:52:45Z` — **moved a third time**; §10 records the delta and which cells moved |
| Revision pin | §1–§7 cells are pinned to `a197445`; §10 re-measures the moving cells at `383ea1a`. The `MANIFEST.json` tally is identical at both (no `rounds` entry was appended between them). |
| Window cutoff | `2026-09-28T23:46:28Z` (= `20:46:28 -03:00`) |
| Commits in window | **20** (was 18 when the task text was written; 19 at the L1's amendment) |
| `MANIFEST.json` md5 | `9e30d57824f110d0faad18812150d9b0` |
| `.ufo/watchdog.log` md5 | `5c32b8de74adf10806c55acd1ad887f9` |
| `MANIFEST.json` `rounds` length | **36** entries |

Per `PROTOCOL.md` §Gate standard ("a verdict names the revision it was measured against"), every count below
was re-read at `a197445` unless it is explicitly labelled with another revision. The two counts that moved
while this seat ran are named in Findings F1 and F10.

Child HEADs observed at the final stamp (orientation only; this seat's scope is the main repo):

| Repo | HEAD | Note |
|---|---|---|
| `kasegi-shokunin` | `b7180b0` | — |
| `kengaku-shokunin` | `f09ff1f` | — |
| `kake-shokunin` | `a209441` | moved from the `4c9a985` in the task text (parent amendment 1) |
| `kumitate-shokunin` | `ed991d0` | moved from `e0e5de1` in amendment 1 — **moved again after the amendment** |
| `kotoba-shokunin` | `63ceba7` | matches amendment 1 |
| `kagi-shokunin` | `4391b3b` | matches amendment 1 |

Earlier `rev-parse` of the same set (before the final stamp) returned `b7180b0 / f09ff1f / a209441 / …`
identically except that `kumitate-shokunin` read `ed991d0` both times while amendment 1 named `e0e5de1`;
both hashes are recorded so a stranger can tell which cell belongs to which revision.

---

## 1. Every file added under `.ufo/reports/` since the cutoff, with introducing commit, author, timestamp

Command (the shape the brief names):

```console
$ git log --diff-filter=A --since=2026-09-28T23:46:28Z \
    --format='C|%H|%an|%aI' --name-only -- .ufo/reports
```

Output — **8** tracked additions (observed verbatim):

```
C|a197445d0b06f463a188d22a28218cd10c302f15|Joao Pedro Veiga|2026-09-28T21:49:18-03:00 -> .ufo/reports/round-13/kumitate.md
C|62fdfbed93d7a48837554b6a4db3669f057d63f5|protocol-shokunin|2026-09-28T21:46:25-03:00 -> .ufo/reports/round-12/protocol.md
C|1dc7f6b81f86606e19d9c6c72f0a336bce4c291f|Joao Pedro Veiga|2026-09-28T21:42:48-03:00 -> .ufo/reports/round-14/kake.md
C|e0170cd33850016beb53cbe9066fefcd3ef17712|Joao Pedro Veiga|2026-09-28T21:18:11-03:00 -> .ufo/reports/round-11/kengaku.md
C|c41e197ac83cf4062742f7284bcfa2299ef08342|Joao Pedro Veiga|2026-09-28T21:15:59-03:00 -> .ufo/reports/round-12/kumitate.md
C|a5d6a7e42854a223baee206c7231924289e89297|aggregator-shokunin|2026-09-28T21:13:01-03:00 -> .ufo/reports/round-8/aggregator.md
C|98735cc60d5dc05864652d61a4b460bd85ccf025|Joao Pedro Veiga|2026-09-28T21:11:33-03:00 -> .ufo/reports/round-13/kotoba.md
C|50b2179ee2501c38d9b6f38898950a2950551118|Joao Pedro Veiga|2026-09-28T20:48:46-03:00 -> .ufo/reports/round-14/kasegi.md
```

Untracked report files in the window:

```console
$ git ls-files -o --exclude-standard .ufo/reports .ufo/prompts .ufo/waves
.ufo/prompts/kake-round-15.md
.ufo/prompts/kotoba-round-15.md
.ufo/reports/round-12/kagi.md
.ufo/reports/round-12/kotoba.md
.ufo/reports/round-14/kotoba.md
.ufo/waves/round-9/CONTEXT.md
.ufo/waves/round-9/lessons/round-9-aggregator-corpus-verdict-kake.md
.ufo/waves/round-9/seats/distiller-queue.md
.ufo/waves/round-9/seats/l0-forensics.md
.ufo/waves/round-9/seats/sentinel-scope.md
.ufo/waves/round-9/seats/verdict-kake.md
```

(`.ufo/waves/round-9/seats/*` and `lessons/*` are the live wave's sibling artifacts, untracked while the wave
runs; outside this seat's scope.)

### 1.1 Classification — contract path, marker, `SHONEN` heading

Bytes measured twice, independently — `stat -c%s` and a Python `len(open(p,'rb').read())` — agreeing on every
row. `SHONEN` measured twice, independently — awk `/^#{1,6} *SHONEN/` and a Python `(?m)^#{1,6} *SHONEN` regex —
agreeing on every row.

```console
$ awk '/^#{1,6} *SHONEN/{c++} END{print c+0}' <file>   # + stat -c%s <file>
```

| # | path | introducing commit | author identity | authored | bytes | contract path? | marker <400 B? | `^#{1,6} *SHONEN`? |
|---|---|---|---|---|---|---|---|---|
| 1 | `.ufo/reports/round-8/aggregator.md` | `a5d6a7e` | `aggregator-shokunin` | 21:13:01 -03 | 24058 | yes | no — real report | **yes** (L190) |
| 2 | `.ufo/reports/round-11/kengaku.md` | `e0170cd` | `Joao Pedro Veiga` | 21:18:11 -03 | 18585 | yes | no | no |
| 3 | `.ufo/reports/round-12/kumitate.md` | `c41e197` | `Joao Pedro Veiga` | 21:15:59 -03 | 14986 | yes | no | **yes** (L212) |
| 4 | `.ufo/reports/round-12/kagi.md` | *(untracked)* | *(unlanded)* | — | 13620 | yes | no | no |
| 5 | `.ufo/reports/round-12/kotoba.md` | *(untracked)* | *(unlanded)* | — | 14009 | yes | no | **yes** (L139) |
| 6 | `.ufo/reports/round-12/protocol.md` | `62fdfbe` | `protocol-shokunin` | 21:46:25 -03 | 39404 | yes | no | **yes** (L445) |
| 7 | `.ufo/reports/round-13/kotoba.md` | `98735cc` | `Joao Pedro Veiga` | 21:11:33 -03 | 10116 | yes | no | no |
| 8 | `.ufo/reports/round-13/kumitate.md` | `a197445` | `Joao Pedro Veiga` | 21:49:18 -03 | 16347 | yes | no | **yes** (L219) |
| 9 | `.ufo/reports/round-14/kasegi.md` | `50b2179` | `Joao Pedro Veiga` | 20:48:46 -03 | 7338 | yes | no | no |
| 10 | `.ufo/reports/round-14/kake.md` | `1dc7f6b` | `Joao Pedro Veiga` | 21:42:48 -03 | 10417 | yes | no | no |
| 11 | `.ufo/reports/round-14/kotoba.md` | *(untracked)* | *(unlanded)* | — | 9463 | yes | no | no |

Tallies: **reports in window = 11** (8 landed + 3 unlanded); **all 11 conform to the contract path
`.ufo/reports/round-<N>/<lane>.md`**; **markers = 0** (no file is under 400 B; smallest is `round-14/kasegi.md`
at 7338 B); **`SHONEN` heading missing on 6 of 11** (rows 2, 4, 7, 9, 10, 11).

Drift at `383ea1a` (stamped `00:52:45Z`): one further report landed — `.ufo/reports/round-13/kagi.md`
(`383ea1a`, `Joao Pedro Veiga`, 21:51:23 -03) — taking the window to **9 landed adds + 3 unlanded = 12**.
Its size/SHONEN are not re-measured here (it landed after the §1.1 pass); §10 names it as the delta.

Author-identity note: 8 of the 11 are authored `Joao Pedro Veiga` (operator identity), not a lane identity —
the recurring "attribution defect" the ledger already tracks. The two-lane exception is
`round-8/aggregator.md` (`aggregator-shokunin`) and `round-12/protocol.md` (`protocol-shokunin`).

---

## 2. `MANIFEST.json` `rounds` last-wins recompute

### 2.1 The keying rule, quoted

`PROTOCOL.md:265-270` decides the key, verbatim:

> **A row names the lane-round it describes.** `lanes` values stay status strings; the optional
> `lane_rounds: {<id>: <n>}` map records a lane's own counter where it differs from the entry's `round` and is
> required on every `not-dispatched` row — the counter the lane actually held is what makes such a row
> falsifiable. The row describes lane-round `(<id>, round)`: `lane_rounds` annotates it and never re-keys it,
> so last-wins is computed over `(id, entry.round)`; reading the map as the key erases in-flight debt and
> manufactures rows out of the pre-fleet-2 fleet-keyed entries, which carry no `lane_rounds` and are
> `unadjudicable` as lane-rounds

So the tally is over `(id, entry.round)`. `PROTOCOL.md:522` records the same trap as a measured appendix row:
keying by `lane_rounds` "yields 66 ok / 3 failed / 13 not-dispatched / 1 in-flight over 83 rows, erasing 3 of
the 4 carried `in-flight` rows". Both keyings are computed below.

### 2.2 Script (full)

```python
#!/usr/bin/env python3
"""Recompute MANIFEST.json `rounds` last-wins tally + M3-shape contradiction scan.

Keying (PROTOCOL.md L265-270): a row describes lane-round (id, entry.round);
`lane_rounds` annotates and NEVER re-keys it -> last-wins over (id, entry.round).

Status rules re-derived from PROTOCOL.md L222-273:
  termination  := `complete <lane> round=N` line, OR the lane's counter passing N
                  (a later `launch <lane> round=N'>`, N'>N)
  in-flight    := launches has (lane,N) AND NOT terminated AND NO *landed* report
                  (an uncommitted file at the report path does NOT end in-flight)
  not-dispatched := no launch/steer evidence for (lane,N)
  now-stale     := a row whose value was valid at its closed_at but is contradicted by
                   evidence that has appeared since (the M3 shape; PROTOCOL.md L261)
"""
import json, re, os, sys, subprocess, datetime
from collections import Counter, defaultdict

def dt(s): return datetime.datetime.fromisoformat(s)
src = sys.argv[1]
rounds = json.load(open(src))["rounds"]
print("source=%s entries=%d  (main HEAD %s)" % (
    src, len(rounds),
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
        lw[(lane, e["round"])] = st
        hist[(lane, e["round"])].append(i)
print("last-wins rows=%d tally=%s" % (len(lw), dict(sorted(Counter(lw.values()).items()))))

lw2 = {}
for e in rounds:
    lr = e.get("lane_rounds") or {}
    for lane, st in (e.get("lanes") or {}).items():
        lw2[(lane, lr.get(lane, e["round"]))] = st
print("lane_rounds-keyed rows=%d tally=%s   <- the diagnosed trap (PROTOCOL Appendix 'Row identity')"
      % (len(lw2), dict(sorted(Counter(lw2.values()).items()))))

print("\n-- not-dispatched rows: is `lane_rounds` present (required by L265-266)? --")
miss = 0
for (lane, n), st in sorted(lw.items()):
    if st != "not-dispatched": continue
    e = rounds[hist[(lane, n)][-1]]
    if lane not in (e.get("lane_rounds") or {}):
        print("  MISSING lane_rounds: (%s,%d) entry#%d" % (lane, n, hist[(lane,n)][-1])); miss += 1
print("not-dispatched rows total=%d  missing lane_rounds=%d"
      % (sum(1 for v in lw.values() if v == "not-dispatched"), miss))

print("\n-- M3 shape: last-wins rows contradicting durable evidence --")
viol = 0; stale = 0
for (lane, n), st in sorted(lw.items()):
    e = rounds[hist[(lane, n)][-1]]
    closed = e.get("closed_at")
    if closed is None: continue
    c = dt(closed)
    tk, tt = terminated(lane, n)
    lts = launch.get((lane, n)) or (steers.get((lane, n)) or [None])[0]
    rp = rpath(lane, n); landed = rp in tracked
    why = None
    if st == "not-dispatched":
        if lts and dt(lts) <= c: why = "AT closed_at: not-dispatched vs dispatch %s" % lts; viol += 1
        elif lts: why = "NOW STALE: not-dispatched but dispatch exists %s" % lts; stale += 1
    elif st == "in-flight":
        if tt and dt(tt) <= c: why = "AT closed_at: in-flight vs termination %s" % tt; viol += 1
        elif tt: why = "NOW STALE vs termination(%s) %s" % (tk, tt); stale += 1
        elif landed: why = "NOW STALE vs landed report %s" % rp; stale += 1
    elif st == "ok":
        if tk is None: why = "ok but no termination evidence"; viol += 1
        elif not os.path.exists(rp): why = "ok but no report at %s" % rp; viol += 1
    if why:
        print("  (%s,%d) [%s] entry#%d @%s  %s" % (lane, n, st, hist[(lane,n)][-1], closed, why))
print("contradictions=%d  (AT-closed_at=%d, NOW-STALE=%d)" % (viol + stale, viol, stale))
```

### 2.3 Observed output — at `a197445` (stamped `00:50:37Z`)

```console
$ python3 - MANIFEST.json <<'PY' … PY
source=MANIFEST.json entries=36  (main HEAD a197445)
last-wins rows=112 tally={'failed': 4, 'in-flight': 7, 'not-dispatched': 18, 'ok': 83}
lane_rounds-keyed rows=94 tally={'failed': 3, 'in-flight': 6, 'not-dispatched': 9, 'ok': 76}   <- the diagnosed trap

-- not-dispatched rows: is `lane_rounds` present (required by L265-266)? --
not-dispatched rows total=18  missing lane_rounds=0

-- M3 shape: last-wins rows contradicting durable evidence --
  (kake,14) [in-flight] entry#27  NOW STALE vs termination(complete) 2026-09-28T21:44:24-03:00
  (kotoba,14) [in-flight] entry#35  NOW STALE vs termination(complete) 2026-09-28T21:36:52-03:00
  (kumitate,13) [in-flight] entry#34  NOW STALE vs landed report .ufo/reports/round-13/kumitate.md
  (protocol,12) [in-flight] entry#25  NOW STALE vs landed report .ufo/reports/round-12/protocol.md
contradictions=4  (AT-closed_at=0, NOW-STALE=4)
```

### 2.3b Same script — at `383ea1a` (stamped `00:52:45Z`), with the now-stale `not-dispatched` branch added

```console
$ python3 - MANIFEST.json <<'PY' … PY
entries=36 HEAD=383ea1a
last-wins rows=112 tally={'failed': 4, 'in-flight': 7, 'not-dispatched': 18, 'ok': 83}
  (kagi,13)     [in-flight]      entry#29  NOW STALE vs termination(complete) 2026-09-28T21:52:08-03:00
  (kagi,14)     [not-dispatched] entry#27  NOW STALE: not-dispatched but dispatch exists 2026-09-28T21:52:12-03:00
  (kake,14)     [in-flight]      entry#27  NOW STALE vs termination(complete) 2026-09-28T21:44:24-03:00
  (kotoba,14)   [in-flight]      entry#35  NOW STALE vs termination(complete) 2026-09-28T21:36:52-03:00
  (kumitate,13) [in-flight]      entry#34  NOW STALE vs termination(complete) 2026-09-28T21:52:02-03:00
  (kumitate,14) [not-dispatched] entry#27  NOW STALE: not-dispatched but dispatch exists 2026-09-28T21:52:06-03:00
  (protocol,12) [in-flight]      entry#25  NOW STALE vs termination(complete) 2026-09-28T21:51:57-03:00
  (protocol,13) [not-dispatched] entry#21  NOW STALE: not-dispatched but dispatch exists 2026-09-28T21:52:01-03:00
contradictions=8  (AT-closed_at=0, NOW-STALE=8)
```

**The tally is stable; the staleness is not.** Between the two stamps the `MANIFEST.json` `rounds` array did not
grow (no closure pass ran), so the last-wins tally stayed `83 / 4 / 7 / 18` at 112 rows — but the stale-row count
**doubled from 4 to 8** as three missions respawned (`kagi r13→r14`, `kumitate r13→r14`, `protocol r12→r13`).
That is metric M3's shape measured live: the respawn cadence outruns the closure cadence, and every respawn
stales one more row (an `in-flight` row whose mission terminated, or a `not-dispatched` row whose dispatch now
exists, violating `PROTOCOL.md:261`).

**Last-wins tally (protocol-correct keying, `MANIFEST.json` @ `a197445`, 36 entries):**

$$\text{112 rows} \;=\; \underbrace{83}_{\texttt{ok}} + \underbrace{4}_{\texttt{failed}} + \underbrace{7}_{\texttt{in-flight}} + \underbrace{18}_{\texttt{not-dispatched}}$$

**Contradicting rows = 4 at `a197445`, 8 at `383ea1a`.** Every one is a row whose status was *valid at its
`closed_at`* and has been superseded by durable evidence since; **0 rows are contradicted at their own
`closed_at`** (so the three closure passes each wrote internally consistent rows, and the drift is the runtime
that outran them). Each is what ledger metric M3 counts — a row whose stated value no longer matches a log line
or a report path. The count is a function of *when* you look, which is why the revision pin is load-bearing.

### 2.4 Historical comparison (same script, older blobs)

```console
$ git show 7c56d1e:MANIFEST.json > /tmp/m_7c56d1e.json ; git show 91d0178:MANIFEST.json > /tmp/m_91d0178.json
```

| revision named | `rounds` len | `(id, entry.round)` tally | `lane_rounds`-keyed tally |
|---|---|---|---|
| `7c56d1e` | 28 | **78 ok / 4 failed / 7 in-flight / 23 not-dispatched** (112 rows) | 71 ok / 3 failed / 2 in-flight / 14 not-dispatched (90 rows) |
| `91d0178` | 30 | 79 ok / 4 failed / 7 in-flight / 22 not-dispatched (112 rows) | 72 ok / 3 failed / 3 in-flight / 13 not-dispatched (91 rows) |
| `a197445` | **36** | 83 ok / 4 failed / 7 in-flight / 18 not-dispatched (112 rows) | 76 ok / 3 failed / 6 in-flight / 9 not-dispatched (94 rows) |

The `7c56d1e` commit message claims "last-wins 78 ok / 4 failed / 7 in-flight" — the script reproduces
`78 / 4 / 7` exactly; the message simply omits the `not-dispatched` limb (23). The row count is stable at 112
across all three revisions because `lane_rounds` never re-keys. The brief's "30 entries" is the `91d0178`
figure; the current array is **36** (F1).

---

## 3. Round-8's falsification test — which lanes consumed round-8 verdicts

### 3.1 The test, quoted by file and line

The clause exists in three places, identically:

- `SCORECARD.md:230-231` — "Falsified if a provisional verdict is restated without a re-run at the lane's new
  HEAD, **or if the round ends with 0 lanes citing a round-8 verdict.**"
- `LOG.md:273-276` — "falsified if a provisional verdict is restated without a re-run at the lane's new HEAD,
  **or if the round ends with zero lanes citing a round-8 verdict.**"
- `.ufo/reports/round-8/aggregator.md:252-253` — "Falsified if a provisional verdict is restated without a
  re-run at the lane's new HEAD, or **if the round ends with zero lanes citing a round-8 verdict.**"

The citation limb is a *falsifier of round 8's own move*: **0 lanes citing would falsify it**. So the round-9
sweep must count how many lanes actually consumed a round-8 verdict.

### 3.2 The artifact set

Round-8's verdicts are carried by (a) the six child-repo lessons
`corpus/lessons/round-8-aggregator-box3-coldrun.md`, (b) ledger §13 (AGGREGATE.md L1057 "## 13. Refresh 6 —
round-8 aggregator audit"), and (c) the lane report + its landing commit `a5d6a7e`.

```console
$ find . -name '*box3*' -o -name '*coldrun*' -o -name '*cold-run*'
./kasegi-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md
./kengaku-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md
./kake-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md
./kumitate-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md
./kotoba-shokunin/corpus/knowledge/cold-run-round11.md
./kotoba-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md
./kagi-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md
```

(the seventh hit, `kotoba-shokunin/corpus/knowledge/cold-run-round11.md`, is kotoba's **own** round-11 cold-run
record, not a round-8 aggregator verdict — see §3.4.)

### 3.3 Citation census over the 11 window reports

```console
$ python3 -c "… re.findall(r'round-8-aggregator-box3-coldrun|§13|a5d6a7e|AGGREGATE\.md', <each window report>)"
file                                     box3-coldrun-filename / §13 / a5d6a7e / AGGREGATE.md
.ufo/reports/round-8/aggregator.md       [2, 22, 0, 1]
.ufo/reports/round-11/kengaku.md         [1, 0, 0, 0]
.ufo/reports/round-12/kumitate.md        [1, 0, 0, 0]
.ufo/reports/round-12/kagi.md            [0, 0, 0, 0]
.ufo/reports/round-12/kotoba.md          [0, 0, 0, 0]
.ufo/reports/round-12/protocol.md        [0, 0, 2, 0]
.ufo/reports/round-13/kotoba.md          [0, 0, 0, 0]
.ufo/reports/round-13/kumitate.md        [1, 0, 0, 0]
.ufo/reports/round-14/kasegi.md          [0, 0, 0, 1]
.ufo/reports/round-14/kake.md            [0, 0, 0, 0]
.ufo/reports/round-14/kotoba.md          [0, 0, 0, 0]
```

Filename matches understate the census: two lanes cite the verdict by commit or by prose. The literal
citation lines:

| lane | report | line | citation |
|---|---|---|---|
| kengaku r11 | `round-11/kengaku.md` | L93 | cites `corpus/lessons/round-8-aggregator-box3-coldrun.md` ("the aggregator's non-author cold run of `SKILL.md`") — plus L34 and L70 on "the unindexed aggregator box-3 lesson row" |
| kumitate r12 | `round-12/kumitate.md` | L107 | cites `corpus/lessons/round-8-aggregator-box3-coldrun.md 12` |
| kumitate r13 | `round-13/kumitate.md` | L98 | cites `corpus/lessons/round-8-aggregator-box3-coldrun.md 12` |
| kagi r12 | `round-12/kagi.md` | L196-197 | cites it **by commit** — "(`e0a04d8 corpus: round-8 aggregator box-3 non-author cold run`, `7c3377c`, `4391b3b` — the aggregator lane's box-3 audit lesson)" |
| kotoba r13 | `round-13/kotoba.md` | L102, L148 | cites it **by prose** — "The aggregator lane landed a round-8 box-3 cold run **inside this repo**" / "the aggregator lane's round-8 cold run, which graded box 3" |
| protocol r12 | `round-12/protocol.md` | L109, L298 | cites the landing commit `a5d6a7e` — "aggregator r8 (`complete` 21:14:05, report `a5d6a7e` 21:13:01)" / "r8's own landing (`a5d6a7e`, lane identity, SHONEN=1) is clean." |

### 3.4 Result

**Lanes that consumed a round-8 verdict artifact: 5** — `kengaku`, `kumitate`, `kagi`, `kotoba`, `protocol`.

The falsifier therefore **did not trigger**: the round did *not* end with 0 lanes citing a round-8 verdict. On
this limb round 8's move is validated. Two asymmetries worth recording:

1. **The ledger §13 refresh itself was consumed by no lane.** `§13` appears 22× inside the aggregator's own
   report and **0× in every other window report**. The routed-defect queue and standing tables of refresh 6
   reached no downstream lane within the window.
2. **The round-8 report's landing commit `a5d6a7e` is cited only in `round-12/protocol.md`** (2×) — and there
   only as *landing evidence in a closure record*, not as a verdict the lane acted on. So the 5-lane count
   rests on the child-repo lesson artifact, not on the report.
3. `round-12/kotoba.md` cites `corpus/knowledge/cold-run-round11.md` (kotoba's own round-11 cold run), which
   is **not** a round-8 aggregator verdict — recorded here so the count is not inflated.

---

## 4. `.ufo/prompts/*.md` untracked count (metric M5) and round-9 dispatch-prompt durability

M5's shape, per `SCORECARD.md:35`:

```
| M5 | untracked dispatch-evidence prompt files | 8 / 58 | 0 / 58 | `git ls-files -o --exclude-standard .ufo/prompts | wc -l` |
```

Observed:

```console
$ git ls-files -o --exclude-standard .ufo/prompts
.ufo/prompts/kake-round-15.md
.ufo/prompts/kotoba-round-15.md
$ git ls-files -o --exclude-standard .ufo/prompts | wc -l
2
$ git ls-files .ufo/prompts | wc -l
87
```

So **M5 = 2 untracked / 89 present** (87 tracked + 2 untracked). Both untracked files are `round-15` prompts
generated by the live respawns (`launch kake round=15` 21:44:25, `launch kotoba round=15` 21:36:53) — i.e. the
prompt-before-launch ordering of `lane_prompt()`, not a lost dispatch.

**Are the round-9 dispatch prompts durable?** Yes for the five that shipped with the third closure pass:

```console
$ for p in aggregator-round-9 kagi-round-13 kengaku-round-12 kotoba-round-14 kumitate-round-13 kake-round-15 kotoba-round-15; do
    git ls-files --error-unmatch .ufo/prompts/$p.md >/dev/null 2>&1 && echo "$p TRACKED" || echo "$p untracked"; done
aggregator-round-9     TRACKED
kagi-round-13          TRACKED
kengaku-round-12       TRACKED
kotoba-round-14        TRACKED
kumitate-round-13      TRACKED
kake-round-15          untracked
kotoba-round-15        untracked
```

All five committed in **`cab25dd`** (`protocol-shokunin`, 2026-09-28T21:35:25-03:00) — the same commit that
took `rounds` to 36. Note the granularity: `cab25dd` is the commit that committed the round-9 *dispatch*
prompts, while `aggregator-round-9.md` is the prompt this very wave rides.

---

## 5. Live-mission set from `.ufo/state/*` + `.ufo/watchdog.log` tail

### 5.1 `.ufo/state/*`

```console
$ for f in .ufo/state/*.mission .ufo/state/*.round; do printf '%s => ' "$f"; cat "$f"; done
.ufo/state/aggregator.mission => shokunin-r9-aggregator-r1790640845     .ufo/state/aggregator.round => 9
.ufo/state/kagi.mission       => shokunin-r13-kagi-r1790640365         .ufo/state/kagi.round       => 13
.ufo/state/kake.mission       => shokunin-r15-kake-r1790642664         .ufo/state/kake.round       => 15
.ufo/state/kasegi.mission     => shokunin-r15-kasegi-r1790639453       .ufo/state/kasegi.round     => 15
.ufo/state/kengaku.mission    => shokunin-r12-kengaku-r1790641306      .ufo/state/kengaku.round    => 12
.ufo/state/kotoba.mission     => shokunin-r15-kotoba-r1790642212       .ufo/state/kotoba.round     => 15
.ufo/state/kumitate.mission   => shokunin-r13-kumitate-r1790641309     .ufo/state/kumitate.round   => 13
.ufo/state/protocol.mission   => shokunin-r12-protocol-r1790638100     .ufo/state/protocol.round   => 12
```

### 5.2 Watchdog launches with no `complete` line (the open set)

Derived from `.ufo/watchdog.log`: the open set is the set of `launch <lane> round=N` keys with no
`complete <lane> round=N` key. (The two set sizes are not offset by the open count: several early lane-rounds
were dispatched by `steer <lane> -> round N` rather than `launch`, so they `complete` without ever appearing in
the launch set — e.g. `complete kengaku round=3` against `steer kengaku -> round 3`.) At the final stamp the
script reports 85 launch keys / 84 complete keys and the launch-keys-without-complete list

```
[('aggregator', 9), ('kagi', 1), ('kagi', 14), ('kake', 15), ('kasegi', 15),
 ('kengaku', 12), ('kotoba', 15), ('kumitate', 14), ('protocol', 13)]
```

`('kagi', 1)` is the historical pair recorded in `PROTOCOL.md` §Appendix ("kagi `not-dispatched` against
`launch kagi round=1` (15:50:56)") and is **not** a live mission — kagi's counter has long passed 1. Removing
it leaves **8 live launch-without-complete pairs**, which the state files below name 8/8 and which are the
8 live missions at the final stamp. The `.ufo/state/*` set moved during the run (kagi `13→14`, kumitate
`13→14`, protocol `12→13`); §10 records that.

Table pinned to the §5.1 state read; the 8 launch lines are the ones each lane's live round rides.

| lane | open round | launch line (quoted) | state file agrees? |
|---|---|---|---|
| aggregator | 9 | `2026-09-28T21:14:10-03:00 launch aggregator round=9 runId=shokunin-r9-aggregator-r1790640845` | yes |
| kagi | 13 | `2026-09-28T21:06:34-03:00 launch kagi round=13 runId=shokunin-r13-kagi-r1790640365` | yes |
| kake | 15 | `2026-09-28T21:44:25-03:00 launch kake round=15 runId=shokunin-r15-kake-r1790642664` | yes |
| kasegi | 15 | `2026-09-28T20:50:55-03:00 launch kasegi round=15 runId=shokunin-r15-kasegi-r1790639453` | yes |
| kengaku | 12 | `2026-09-28T21:21:48-03:00 launch kengaku round=12 runId=shokunin-r12-kengaku-r1790641306` | yes |
| kotoba | 15 | `2026-09-28T21:36:53-03:00 launch kotoba round=15 runId=shokunin-r15-kotoba-r1790642212` | yes |
| kumitate | 13 | `2026-09-28T21:21:51-03:00 launch kumitate round=13 runId=shokunin-r13-kumitate-r1790641309` | yes |
| protocol | 12 | `2026-09-28T20:28:21-03:00 launch protocol round=12 runId=shokunin-r12-protocol-r1790638100` | yes |

**8 open missions; the state files and the watchdog open set agree 8/8** at the §5.1 read. Live then: kasegi r15,
kumitate r13, kagi r13, kotoba r15, protocol r12, kake r15, kengaku r12, aggregator r9.

At `383ea1a` (`00:52:45Z`) the same 8 lanes are live but three have respawned, so the live set reads: aggregator
r9, **kagi r14**, kake r15, kasegi r15, kengaku r12, kotoba r15, **kumitate r14**, **protocol r13** — verified by
`cat .ufo/state/*.round` → `aggregator=9 kagi=14 kake=15 kasegi=15 kengaku=12 kotoba=15 kumitate=14 protocol=13`,
with each lane's newest `launch` line having no `complete`. The 8-lane *membership* is stable; only the round
counter moves.

### 5.3 Tail, with launch/complete lines quoted

```console
$ python3 -c "print(open('.ufo/watchdog.log').read().splitlines()[-20:])"
2026-09-28T21:14:05-03:00 complete aggregator round=8; respawning
2026-09-28T21:14:10-03:00 launch aggregator round=9 runId=shokunin-r9-aggregator-r1790640845
2026-09-28T21:14:11-03:00 complete kotoba round=13; respawning
2026-09-28T21:14:16-03:00 launch kotoba round=14 runId=shokunin-r14-kotoba-r1790640851
2026-09-28T21:14:16-03:00 tick=28
2026-09-28T21:21:46-03:00 complete kengaku round=11; respawning
2026-09-28T21:21:48-03:00 launch kengaku round=12 runId=shokunin-r12-kengaku-r1790641306
2026-09-28T21:21:49-03:00 complete kumitate round=12; respawning
2026-09-28T21:21:51-03:00 launch kumitate round=13 runId=shokunin-r13-kumitate-r1790641309
2026-09-28T21:21:51-03:00 tick=29
2026-09-28T21:29:22-03:00 tick=30
2026-09-28T21:36:52-03:00 complete kotoba round=14; respawning
2026-09-28T21:36:53-03:00 launch kotoba round=15 runId=shokunin-r15-kotoba-r1790642212
2026-09-28T21:36:53-03:00 tick=31
2026-09-28T21:44:24-03:00 complete kake round=14; respawning
2026-09-28T21:44:25-03:00 launch kake round=15 runId=shokunin-r15-kake-r1790642664
2026-09-28T21:44:25-03:00 tick=32
```

The last two ticks are the decisive ones for §2.3: `complete kotoba round=14` (21:36:52) and
`complete kake round=14` (21:44:24) both postdate the third closure pass's `closed_at` `21:30:00`, which is
why `(kotoba,14)` and `(kake,14)` are stale-but-not-at-closure.

---

## 6. Hygiene note on the parent's amendment 2 (CORPUS.md rule 8) — out of this seat's scope

Amendment 2 directs rule-8 grading to the corpus-review seats. This seat produces **no rule-8 cell** and
attests no rule-8 verdict. As a courtesy over its own window, it counted the secret-class tokens in the 11
window reports (counts, file:line and class only; no value printed):

```console
$ python3 -c "… re.search('op://|sk-[A-Za-z0-9]{8,}|xox[bap]-|(?i)bearer\\s+\\S{10,}|(?i)password\\s*=\\s*\\S+|(?i)token\\s*=\\s*\\S+') …"
.ufo/reports/round-12/kagi.md   {'op://': [163]}     ← all other 10 window reports: none
TOTAL hits over 11 window reports = 1
```

The single hit is `round-12/kagi.md:163`, inside a falsification description
(`` `KAGI12_POISON=op://…` appended ``): the token after `op://` is an ellipsis (`op://` + `…` + closing
backtick). Class: **`schematic-placeholder`**, not a `real-vault-path`. No secret value was observed or
printed. This is a courtesy count, not a rule-8 verdict; the authoritative landed-corpus sweep is
`SentinelSeat`'s.

---

## 7. Findings

| id | rule | owner | sev | claim | command | observed |
|---|---|---|---|---|---|---|
| F1 | queue | protocol | 2 | The brief's (and the L1's) "30 `rounds` entries" is stale: the array is **36** at `a197445`, appended by three closure passes. | `python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['rounds']))"` | `36` (was `30` at `91d0178`, `28` at `7c56d1e`) |
| F2 | queue | protocol | 4 | Last-wins rows now stale vs durable evidence **doubled from 4 to 8** between two stamps minutes apart while the `rounds` array did not grow — the respawn cadence outruns the closure cadence, so every respawn stales one more row. | §2.2 script at both revisions | `a197445`: 4 stale (`(kake,14)`, `(kotoba,14)`, `(kumitate,13)`, `(protocol,12)`); `383ea1a`: 8 stale (adds `(kagi,13)`, `(kagi,14)`, `(kumitate,14)`, `(protocol,13)`); **0** ever contradicted at its own `closed_at` |
| F3 | box-3 | operator | 2 | **6 of 11** window reports carry no `^#{1,6} *SHONEN` heading; the defect is the existing D-120 (no seed for the two main-repo lanes). | `awk '/^#{1,6} *SHONEN/{c++} END{print c+0}' <file>` | missing on kengaku r11, kagi r12, kotoba r13, kasegi r14, kake r14, kotoba r14 |
| F4 | queue | aggregator | 3 | Round-8's citation falsifier did **not** trigger: **5 lanes** consumed a round-8 verdict artifact. | §3.3 census | kengaku, kumitate, kagi, kotoba, protocol |
| F5 | queue | aggregator | 3 | Ledger **§13 (refresh 6)** reached **no** downstream lane: 22 self-citations, 0 elsewhere. The round-8 report's landing commit `a5d6a7e` is cited only in `round-12/protocol.md` (2×) and only as landing evidence. | §3.3 census | `[2,22,0,1]` in the report; `0` §13 in all other window reports |
| F6 | queue | protocol | 2 | M5 = **2** untracked prompts / 89 present at `a197445` (**5** / 92 at `383ea1a`). All 5 round-9-wave dispatch prompts are durable (`cab25dd`); the untracked ones are the newest respawn prompts written before their launch. | `git ls-files -o --exclude-standard .ufo/prompts \| wc -l`; `git ls-files .ufo/prompts \| wc -l` | `2` / `87` at `a197445`; `5` untracked (`kagi-round-14`, `kake-round-15`, `kotoba-round-15`, `kumitate-round-14`, `protocol-round-13`) at `383ea1a` |
| F7 | queue | protocol | 2 | **Round 15 has never closed**: `kasegi r15`, `kake r15`, `kotoba r15` are live with no MANIFEST round-15 entry, so the partial-entries trigger has nothing to fire on. | `git rev-list HEAD --since=… \| wc -l` + §2.2 script | 36 entries, max `round` = 14; 8 open missions incl. three r15 |
| F8 | queue | aggregator | 3 | Main HEAD moved **three** times inside this seat's run (`1dc7f6b` → `62fdfbe` → `a197445` → `383ea1a`) and the window grew 18 → 19 → 20 → 21 commits, so any window count written before `00:52:45Z` is superseded. The task text's own "18 commits" and "30 entries" were already stale when read. | `git rev-parse --short HEAD`; `git rev-list HEAD --since=2026-09-28T23:46:28Z \| wc -l`; `len(rounds)` | `383ea1a`; `21`; `36` — three of the four figures in the brief were wrong on arrival |
| F9 | secrets | kagi | 1 | One `op://` occurrence in the window reports, class `schematic-placeholder` (ellipsis), no real vault path. | §6 count | `round-12/kagi.md:163` only |
| F10 | queue | kasegi | 2 | `round-8/aggregator.md` is authored `aggregator-shokunin` (correct) but **8 of 11** window reports carry the operator identity `Joao Pedro Veiga` — the recurring attribution defect. | `git log --diff-filter=A --format='%an' --name-only -- .ufo/reports` | 8/11 operator-identity |
| F11 | queue | protocol | 2 | The 8 stale rows at `383ea1a` split into two classes, both fixed by the round-9 closure: 5 `in-flight` rows whose mission terminated (`(kagi,13)`, `(kake,14)`, `(kotoba,14)`, `(kumitate,13)`, `(protocol,12)`) and 3 `not-dispatched` rows whose dispatch now exists (`(kagi,14)`, `(kumitate,14)`, `(protocol,13)`), the latter a direct violation of `PROTOCOL.md:261`. | §2.2 script (now-stale `not-dispatched` branch) | 5 in-flight + 3 not-dispatched = 8 |

Axis note: **all three aggregator axes are tied at 8** per `CONTEXT.md`; nothing in this sweep moves an axis
score, and F4/F5 are the only cells that bear on the round-8 move's own falsification.

## 8. Candidate ledger rows (distiller assigns `D-` keys)

| owner | sev | claim | evidence | command |
|---|---|---|---|---|
| protocol | 4 | `MANIFEST.json` last-wins already carries **8** rows contradicted by durable evidence at `383ea1a` (4 at `a197445`) — and the count grows with every respawn inside the wave. Round 9's closure must answer all 8: 5 `in-flight` rows whose mission terminated (`(kagi,13)` complete 21:52:08; `(kake,14)` complete 21:44:24; `(kotoba,14)` complete 21:36:52; `(kumitate,13)` complete 21:52:02; `(protocol,12)` complete 21:51:57) and 3 `not-dispatched` rows whose dispatch now exists (`(kagi,14)` launch 21:52:12; `(kumitate,14)` launch 21:52:06; `(protocol,13)` launch 21:52:01) — the last three violating `PROTOCOL.md:261`. | §2.2 script output at `383ea1a`: 8 rows, 0 at-closed_at, 8 now-stale | `python3 - MANIFEST.json <<'PY' … PY` |
| protocol | 2 | The L1's round-9 context and this seat's brief both state `MANIFEST.json` holds 30 `rounds` entries; it holds 36. Any figure re-derived from the brief will be wrong by 6 rows. | `len(json.load(open('MANIFEST.json'))['rounds'])` → 36; at `91d0178` → 30 | `python3 -c ...` |
| aggregator | 3 | Ledger §13 (refresh 6, AGGREGATE.md L1057) was consumed by zero downstream lanes inside the window; the round-8 box-3 lesson was the only artifact that propagated. | `§13` count = 22 in `round-8/aggregator.md`, 0 in the other 10 window reports | §3.3 census |
| operator | 2 | 6 of 11 window reports omit the `^#{1,6} *SHONEN` heading; ledger D-120 records that the main-repo lanes have no seed for it. | missing in `round-11/kengaku.md`, `round-12/kagi.md`, `round-13/kotoba.md`, `round-14/kasegi.md`, `round-14/kake.md`, `round-14/kotoba.md` | `awk '/^#{1,6} *SHONEN/{c++} END{print c+0}'` |
| protocol | 2 | Round 15 has never closed and no r15 lane-round has terminated for `kasegi`/`kake`/`kotoba`, so no partial entry can fire; three live missions are unrowed. | max `round` in `rounds` = 14; open set contains kasegi 15, kake 15, kotoba 15 | §2.2 script + §5.2 |
| kagi | 1 | `round-12/kagi.md:163` embeds an `op://` token in a falsification description; class `schematic-placeholder` (ellipsis), not a real vault path — recorded so the sentinel sweep and this seat's count reconcile. | 1 hit / 11 window reports, all other reports clean | §6 count |

## 9. Re-run recipe (stranger-facing)

```bash
cd /home/vgpnk/projects/shokunin
# 0. stamp: confirm you are at a197445 (or say which revision your cells name)
git rev-parse --short HEAD            # -> a197445 (383ea1a at the later stamp; pin and say which)
md5sum MANIFEST.json .ufo/watchdog.log   # -> 9e30d578… / 5c32b8de…  (at a197445)
# 1. window commit set (two independent methods must agree)
git rev-list HEAD --since=2026-09-28T23:46:28Z | wc -l        # -> 20 at a197445, 21 at 383ea1a
# 2. report adds + untracked
git log --diff-filter=A --since=2026-09-28T23:46:28Z --format='C|%H|%an|%aI' --name-only -- .ufo/reports
git ls-files -o --exclude-standard .ufo/reports .ufo/prompts .ufo/waves
# 3. per-file size + SHONEN (two methods)
for f in .ufo/reports/round-*/*.md; do echo "$f $(stat -c%s "$f") $(awk '/^#{1,6} *SHONEN/{c++} END{print c+0}' "$f")"; done
# 4. MANIFEST last-wins: paste the §2.2 script and run `python3 - MANIFEST.json`
# 5. citation census: §3.3 one-liner over the 11 window reports listed in §1.1
# 6. live missions: `cat .ufo/state/*.round` + the §5.2 open-set extraction
```

Nothing in this file needs a mutating verb. Where a decisive check would have needed one, none arose; there
are **no `gated-without-artifact` cells** in this seat.

---

## 10. Drift log — every cell that moved while this seat ran

The wave committed live, so this seat measured a moving target. Pinning to a revision is what makes the cells
comparable (`PROTOCOL.md` §Gate standard: "a verdict names the revision it was measured against"). Three
revisions were observed:

| stamp (UTC) | HEAD | window commits | `rounds` len | landed report adds | untracked prompts | stale M3 rows |
|---|---|---|---|---|---|---|
| `~00:45Z` | `1dc7f6b` | 18 | 36 | 6 | 2 | — |
| `00:50:37Z` | `a197445` | 20 | 36 | 8 | 2 | **4** |
| `00:52:45Z` | `383ea1a` | 21 | 36 | 9 | 5 | **8** |

Deltas, each with its command and observed output:

1. **One new commit** — `git log --oneline a197445..HEAD` → `383ea1a round-13: kagi report (calibration 8 -> 9;
   claim ids resolve, scorecard cells audited)`.
2. **One new report add** — `git log --diff-filter=A --format='%h|%an|%aI' --name-only a197445..HEAD -- .ufo/reports`
   → `383ea1a|Joao Pedro Veiga|2026-09-28T21:51:23-03:00` + `.ufo/reports/round-13/kagi.md`.
3. **Three new untracked prompts** — `git ls-files -o --exclude-standard .ufo/prompts` now lists
   `kagi-round-14.md`, `kake-round-15.md`, `kotoba-round-15.md`, `kumitate-round-14.md`, `protocol-round-13.md`
   (5 total; M5 `2 → 5`).
4. **Three respawns** — `cat .ufo/state/*.round` → `aggregator=9 kagi=14 kake=15 kasegi=15 kengaku=12 kotoba=15
   kumitate=14 protocol=13` (kagi `13→14`, kumitate `13→14`, protocol `12→13`).
5. **The M3 stale count doubled** — §2.2 script: `4 → 8`, while the last-wins tally stayed
   `{'failed': 4, 'in-flight': 7, 'not-dispatched': 18, 'ok': 83}` at both revisions because no `rounds` entry
   was appended between them.

**Which cells belong to which revision** — §1.1 (11 reports, sizes, SHONEN, authors), §2.3 (`a197445` run),
§3 (citation census), §4 (`M5 = 2`), §5.1/§5.2 (state read + 8-mission table), §6 — all pinned to `a197445` or
the §5.1 read. §2.3b, §10, and every "at `383ea1a`" figure are pinned to `383ea1a`. The **tally**
(`83 / 4 / 7 / 18`) and the **contract-path / marker** verdicts are revision-stable between the two stamps;
the **stale-row count, the window commit count, and M5** are not.

Residual limit: the wave was still live at the last stamp, so a reader re-running §9 at a later HEAD will get
different counts for those three cells. That is the property, not a defect: metric M3 measures a race between
the respawn cadence and the closure cadence, and inside round 9 the respawn cadence was winning.