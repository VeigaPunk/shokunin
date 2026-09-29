# Round-13 measurement worksheet — `protocol` lane

Read-only measurement pass. Every figure below was produced by the command shown, in this session,
on the tree at `/home/vgpnk/projects/shokunin`. The tree moves (eight lanes commit concurrently), so
**`git rev-parse --short HEAD` is recorded per item**. Nothing here is written from memory; every
block is a verbatim paste. Where an output is long, the trim is stated in the block.

Method: `date -Is` and `git rev-parse --short HEAD` were run immediately before each measurement, in
the same shell invocation, so an item's instant and revision are the same moment.

---

## 1. Baseline figures

### 1.1 Size of the live `PROTOCOL.md`

Instant `2026-09-28T22:10:59-03:00`, HEAD `f3cbdcf`.

```bash
date -Is && git rev-parse --short HEAD && wc -l -c PROTOCOL.md
```

```
2026-09-28T22:10:59-03:00
f3cbdcf
  526 49269 PROTOCOL.md
```

Re-checked once at `2026-09-28T22:12:55-03:00`, HEAD `f3cbdcf`:

```bash
wc -l -c PROTOCOL.md | awk '{print $1" / "$2}'
```

```
526 / 49269
```

Baseline to beat: **526 lines / 49269 bytes**; target **≤470 lines**.

### 1.2 Body inline round-incident refs

Instant `2026-09-28T22:11:03-03:00`, HEAD `f3cbdcf`.

```bash
awk 'NR<487' PROTOCOL.md | grep -o 'round-[0-9][0-9.]*' | wc -l
```

```
4
```

`487` is the 1-based line of `## Appendix — incident digest (why these rules exist)` (section map in
§1.6). Rule: this number must **not rise** during compaction.

### 1.3 Appendix round-incident refs

Same instant as §1.2 (`2026-09-28T22:11:03-03:00`, HEAD `f3cbdcf`).

```bash
awk 'NR>=487' PROTOCOL.md | grep -o 'round-[0-9][0-9.]*' | wc -l
```

```
18
```

### 1.4 Obligation census — run

Instant `2026-09-28T22:11:03-03:00`, HEAD `f3cbdcf`.

```bash
sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md > /tmp/census.out 2>&1; echo "EXIT=$?"; wc -l /tmp/census.out; awk 'NR<=5' /tmp/census.out; tail -5 /tmp/census.out
```

```
EXIT=0
95 /tmp/census.out
PASS L1
PASS L2
PASS L3
PASS L4
PASS L5
PASS V3
PASS V4
PASS V5

93/93 obligations found; 0 MISSING
```

(Output trimmed: first 5 lines and last 5 lines of the 95-line run; the elided middle is 85 further
`PASS <id>` lines, no `MISS`.)

```bash
grep -c '^MISS' /tmp/census.out
```

```
0
```

### 1.5 Census predicate count

Instant `2026-09-28T22:11:40-03:00`, HEAD `f3cbdcf`.

```bash
wc -l .ufo/waves/round-11/obligation-census.tsv
```

```
94 .ufo/waves/round-11/obligation-census.tsv
```

94 = 1 header row + **93 predicates**, matching the `93/93` denominator. Section tally of the
predicate rows (`awk -F'\t' 'NR>1{print $2}' … | sort | uniq -c`):

```
      5 Aggregator
     11 Evidence
      6 FileContract
      5 Fleet-2
     13 Invariants
      3 Lifecycle
      4 Promotion
     33 Rounds
      1 Step1
      1 Step2
      1 Step3
     10 Step4
```

### 1.6 Section line map (live `PROTOCOL.md`)

Instant `2026-09-28T22:10:59-03:00`, HEAD `f3cbdcf`.

```bash
grep -n '^## ' PROTOCOL.md
```

```
8:## Lifecycle
29:## Promotion gates
55:## Round-robin rounds
306:## Evidence standard
346:## Gate standard
386:## File contract per shokunin repo
412:## Invariants
465:## Fleet-2 conventions (adopted)
487:## Appendix — incident digest (why these rules exist)
```

---

## 2. Ledger figures

### 2.1 `MANIFEST.json` — entries, status tallies, sha256

Instant `2026-09-28T22:11:08-03:00`, HEAD `f3cbdcf`.

```bash
python3 -c "
import json,collections
d=json.load(open('MANIFEST.json'))
r=d['rounds']
print('entries',len(r))
c=collections.Counter()
for e in r:
    for ln,st in (e.get('lanes') or {}).items():
        c[st]+=1
print('lane-status tallies',dict(sorted(c.items())))
top=collections.Counter(e.get('status') for e in r)
print('round-level status',dict(sorted(top.items())))
" && sha256sum MANIFEST.json
```

```
entries 36
lane-status tallies {'failed': 4, 'in-flight': 26, 'not-dispatched': 41, 'ok': 84}
round-level status {None: 36}
db69d052c39d0dbb5bbe30de944c0ac7c65729f2217a49f26ddaa2321cd2477f  MANIFEST.json
```

Entry count **36**; sha256 **`db69d052c39d0dbb5bbe30de944c0ac7c65729f2217a49f26ddaa2321cd2477f`**.
Last-wins census over the entry-keyed adjudicated rows (the gate's own §Tallies, §2.2):
`ok=75 failed=4 in-flight=7 not-dispatched=18 rows=104`.

### 2.2 Live gate — first line + exit code

Instant `2026-09-28T22:11:08-03:00`, HEAD `f3cbdcf`.

```bash
python3 .ufo/waves/round-12/closure-check.py --no-citations; echo "EXIT=$?"
```

First line and exit (full run is 200+ lines):

```
closure-check: debt debt=6 contradictions=0 unrowed_terminated=1 pending_round=5
EXIT=1
```

> **Tree moved since the task fact sheet.** The fact sheet recorded `debt=5 … pending_round=6` at
> ~21:57. At 22:11 the live gate reports **`debt=6` / `unrowed_terminated=1` / `pending_round=5`**.
> The new debt row is `unrowed_terminated kasegi r15` (§2.5), which was previously only a
> `pending_round` row. Both readings are from the same committed checker
> (`.ufo/waves/round-12/closure-check.py`, sha256 below); only the tree changed.

Gate revision measured against, instant `2026-09-28T22:13:59-03:00`:

```bash
sha256sum .ufo/waves/round-12/closure-check.py && git rev-parse --short HEAD
```

```
d1b6ed929bbcd769a604e649dd0c8f288498641518a36fa2d46048e0741fc273  .ufo/waves/round-12/closure-check.py
f3cbdcf
```

Instants for the §2/§3 live runs (`22:11:08`, `22:11:13`, `22:11:19`, `22:11:25`) all carried HEAD
`f3cbdcf`; the `.ufo/waves/round-12/` tree was never written by any command in this pass (read-only
scope), so this hash applies to every run posted above.

### 2.3 `--json` `counts` object

Instant `2026-09-28T22:11:13-03:00`, HEAD `f3cbdcf`.

```bash
python3 .ufo/waves/round-12/closure-check.py --no-citations --json | python3 -c "
import json,sys; d=json.load(sys.stdin)
print('counts:',json.dumps(d.get('counts'),sort_keys=True,indent=2))
print('verdict:',json.dumps(d['verdict'])); print('exit:',d['exit']); print('meta:',json.dumps(d['meta'],sort_keys=True))
"
```

```
counts: {
  "by_class": {
    "stale_in_flight": 5,
    "unrowed_terminated": 1
  },
  "contradictions": 0,
  "debt": 6,
  "live_in_flight": 2,
  "pending_round": 5,
  "prompt_orphan": 0,
  "stale_in_flight": 5,
  "unrowed": 6,
  "unrowed_terminated": 1
}
verdict: "debt"
exit: 1
meta: {"complete_events": 84, "dispatch_events": 100, "entries": 36, "kind": "live", "lanes_with_counters": ["aggregator", "kagi", "kake", "kasegi", "kengaku", "kotoba", "kumitate", "protocol"], "log_lines": 236, "repo": "/home/vgpnk/projects/shokunin"}
```

Top-level JSON keys present:
`after_closure, citation_scope, citation_tally, citations, contradictions, counts, debt, exit,
keying_tallies, ledger, live_in_flight, live_missions, meta, pending_round, stale_missions, tallies,
unadjudicable, unlanded_report_at_path, unrowed, unrowed_terminated, verdict` (21 keys; no
`exit_code` field — the code is under `exit`).

### 2.4 `--show-keying`

Instant `2026-09-28T22:11:13-03:00`, HEAD `f3cbdcf`.

```bash
python3 .ufo/waves/round-12/closure-check.py --no-citations --show-keying | grep -A4 -i 'keying\|Tallies' | head -30
```

```
keying: entry-keyed (a row names (lane, entry.round); lane_rounds annotates, never re-keys)

== Ledger (last-wins, entry-keyed): 104 status rows ==
lane       round  status         entry  type                closed_at                 counter
protocol       2  not-dispatched     5  retroactive-closure 2026-09-28T18:21:16-03:00 1
--
== Tallies ==
entry-keyed, adjudicated (closure*) entries only: ok=75 failed=4 in-flight=7 not-dispatched=18 rows=104
entry-keyed, all entries incl. legacy fleet-keyed rows: ok=83 failed=4 in-flight=7 not-dispatched=18 rows=112
lane_rounds-keyed (non-authoritative, --show-keying): ok=76 failed=3 in-flight=6 not-dispatched=9 rows=94
unadjudicable rows: 16 (entries #1, #3)
live missions: 7 (stale > 900 s: 7)
```

The non-authoritative `lane_rounds` keying differs from the authoritative entry-keyed one on every
figure (76/3/6/9 over 94 rows vs 75/4/7/18 over 104) — this is the "naive keying" hole the round-12
*pin 1 — Row identity* closed.

### 2.5 Citation tally line

Instant `2026-09-28T22:11:19-03:00`, HEAD `f3cbdcf`.

```bash
python3 .ufo/waves/round-12/closure-check.py --json | python3 -c "
import json,sys; d=json.load(sys.stdin)
print('citation_tally:',json.dumps(d['citation_tally'],sort_keys=True))
print('citation_scope:',json.dumps(d['citation_scope'],sort_keys=True))
"
```

```
citation_tally: {"commit": 372, "dead": 105, "non-commit": 0, "orphan": 5, "pin": 25, "placeholder": 2, "runId/date": 21}
citation_scope: "107 lane-rounds / 83 reports on disk / 507 tokens / 9 repos, identity resolved by full-odb cat-file per repo"
```

Text-mode header line, same instant:

```bash
python3 .ufo/waves/round-12/closure-check.py | grep -i 'cited\|citation'
```

```
    cited 1 token(s): 1 resolve in kotoba-shokunin [29c17be by kotoba-shokunin], 0 in other repos; lane-authored 1/1
== Report citations (107 lane-rounds / 83 reports on disk / 507 tokens / 9 repos, identity resolved by full-odb cat-file per repo) ==
```

### 2.6 Live debt rows (verbatim from the run)

From the §2.2 run at HEAD `f3cbdcf` (6 rows; the `== Debt (exit-1 drivers): 6 ==` list, abridged to
the 6 header lines):

```
stale_in_flight        protocol   r12   entry=25   in-flight row (entry #25); mission terminated since closed_at: report .ufo/reports/round-12/protocol.md (39404 B)
stale_in_flight        kake       r14   entry=27   in-flight row (entry #27); mission terminated since closed_at: report .ufo/reports/round-14/kake.md (10417 B)
stale_in_flight        kumitate   r13   entry=34   in-flight row (entry #34); mission terminated since closed_at: report .ufo/reports/round-13/kumitate.md (16347 B)
stale_in_flight        kotoba     r14   entry=35   in-flight row (entry #35); mission terminated since closed_at: report .ufo/reports/round-14/kotoba.md (9463 B)
stale_in_flight        kagi       r13   entry=29   in-flight row (entry #29); mission terminated since closed_at: report .ufo/reports/round-13/kagi.md (9441 B)
unrowed_terminated     kasegi     r15   entry=-    dispatch `2026-09-28T20:50:55-03:00 launch kasegi round=15 runId=shokunin-r15-kasegi-r1790639453` with termination evidence and no row: no complete line, counter 15 (not past 15)
```

The first 5 match the fact sheet's 5 `stale_in_flight`, each `suggested status: ok`. The 6th
(`kasegi r15`) is new at this instant.

---

## 3. Gate self-verification

### 3.1 `--selftest`

Instant `2026-09-28T22:11:13-03:00`, HEAD `f3cbdcf`.

```bash
python3 .ufo/waves/round-12/closure-check.py --selftest; echo "EXIT=$?"
```

Last 7 lines of output (fixture list abridged to the final two rows + tally):

```
  unknown-lane                           pass  exit=1 debt=1 contradictions=1 unrowed_terminated=0 pending_round=0
  unrowed                                pass  exit=0 debt=0 contradictions=0 unrowed_terminated=0 pending_round=1
selftest: 15/15 passed
EXIT=0
```

**Tally: `15/15 passed`, exit 0.**

### 3.2 `--frozen pre`

Instant `2026-09-28T22:11:13-03:00`, HEAD `f3cbdcf`.

```bash
python3 .ufo/waves/round-12/closure-check.py --frozen pre; echo "EXIT=$?"
```

Tail:

```
  stale_in_flight    kotoba     r12   in-flight row (entry #20); mission terminated since closed_at: report .ufo/reports/round-12/kotoba.md (14009 B)
      pinned from: scout-closure §Required appends 4 + reviewer: `ok` + durability defect (report 14009 B untracked, landed by the pass)
baseline: match  expected exit=1  analyzed exit=1
EXIT=1
```

**`baseline: match`, expected exit=1, analyzed exit=1, exit code 1.**

### 3.3 `--frozen post-actual`

Instant `2026-09-28T22:11:25-03:00`, HEAD `f3cbdcf`.

```bash
python3 .ufo/waves/round-12/closure-check.py --frozen post-actual; echo "EXIT=$?"
```

Tail:

```
  stale_in_flight    kotoba     r13   in-flight row (entry #26); mission terminated since closed_at: report .ufo/reports/round-13/kotoba.md (10116 B)
      pinned from: entry #26 in-flight; complete kotoba round=13 21:14:11 (<= 21:20) + landed report .ufo/reports/round-13/kotoba.md (add 98735cc, 10116 B, added 21:11:33)
baseline: match  expected exit=1  analyzed exit=1
EXIT=1
```

**`baseline: match`, expected exit=1, analyzed exit=1, exit code 1.**

### 3.4 `--frozen post`

Instant `2026-09-28T22:11:13-03:00`, HEAD `f3cbdcf`.

```bash
python3 .ufo/waves/round-12/closure-check.py --frozen post; echo "EXIT=$?"
```

Full tail:

```
closure-check: ok debt=0 contradictions=0 unrowed_terminated=0 pending_round=3
frozen snapshot: post  mode: frozen  entries: 34  log lines: 215
debt set (0):
  none
baseline: match  expected exit=0  analyzed exit=0
EXIT=0
```

**`baseline: match`, expected exit=0, analyzed exit=0, exit code 0.**

Baseline expected-verdict summary (read from each dir's `expected.json`):

| dir | `exit` | `debt` rows |
|---|---|---|
| `frozen/pre` | 1 | 5 |
| `frozen/post-actual` | 1 | 4 |
| `frozen/post` | 0 | 0 |

`--frozen NAME` resolution is **hard-coded to `.ufo/waves/round-12/frozen/<NAME>`**
(`closure-check.py:1355-1356`: `os.path.join(repo, ".ufo", "waves", "round-12", "frozen", which)`);
`--help` still reads `re-run against .ufo/waves/round-12/frozen/<NAME>`. See §7.

### 3.5 Wall time — full live run with citations

Instant `2026-09-28T22:11:25-03:00`, HEAD `f3cbdcf`.

```bash
python3 -c "
import subprocess,time
t=time.time()
p=subprocess.run(['python3','.ufo/waves/round-12/closure-check.py'],capture_output=True,text=True)
print('exit=%d wall_s=%.2f'%(p.returncode,time.time()-t))
print('stdout_lines=%d stderr_lines=%d'%(p.stdout.count(chr(10)),p.stderr.count(chr(10))))
"
```

```
exit=1 wall_s=0.42
stdout_lines=212 stderr_lines=0
```

**Full live run with citations: exit 1, wall 0.42 s, 212 stdout lines.**

---

## 4. Durability figures

Instant for §4.1–§4.4: `2026-09-28T22:11:25-03:00`, HEAD `f3cbdcf`.
Instant for §4.5–§4.6: `2026-09-28T22:11:31-03:00`, HEAD `f3cbdcf`.

### 4.1 Untracked prompts

```bash
git ls-files -o --exclude-standard .ufo/prompts | wc -l && git ls-files -o --exclude-standard .ufo/prompts
```

```
5
.ufo/prompts/kagi-round-14.md
.ufo/prompts/kake-round-15.md
.ufo/prompts/kotoba-round-15.md
.ufo/prompts/kumitate-round-14.md
.ufo/prompts/protocol-round-13.md
```

### 4.2 Untracked reports

```bash
git ls-files -o --exclude-standard .ufo/reports
```

```
.ufo/reports/round-12/kagi.md
.ufo/reports/round-12/kotoba.md
.ufo/reports/round-14/kotoba.md
```

Three untracked reports — `kotoba r14` is the one the gate names as the *unlanded report at the
contract path* (driver signal vs ledger mismatch).

### 4.3 Tracked `.ufo/state` files

```bash
git ls-files .ufo/state | wc -l
```

```
16
```

### 4.4 `watchdog.log` tracked

```bash
git ls-files .ufo/watchdog.log | wc -l
```

```
1
```

### 4.5 Child-report SHONEN sweep

```bash
grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md | grep -vE 'protocol|aggregator|AGGREGATE' | wc -l
```

```
60
```

File list (60 paths, `round-1` … `round-15`; pasted in full because it is the durable artifact of
this sweep):

```
.ufo/reports/round-1/kasegi.md
.ufo/reports/round-1/kengaku-shokunin.md
.ufo/reports/round-1/kotoba.md
.ufo/reports/round-1/kumitate.md
.ufo/reports/round-1/web-properties-publishing.md
.ufo/reports/round-10/kagi.md
.ufo/reports/round-10/kake.md
.ufo/reports/round-10/kasegi.md
.ufo/reports/round-11/kagi.md
.ufo/reports/round-11/kake.md
.ufo/reports/round-11/kasegi.md
.ufo/reports/round-11/kengaku.md
.ufo/reports/round-12/kagi.md
.ufo/reports/round-12/kake.md
.ufo/reports/round-12/kasegi.md
.ufo/reports/round-13/kagi.md
.ufo/reports/round-13/kake.md
.ufo/reports/round-13/kasegi.md
.ufo/reports/round-13/kotoba.md
.ufo/reports/round-14/kake.md
.ufo/reports/round-14/kasegi.md
.ufo/reports/round-14/kotoba.md
.ufo/reports/round-15/kasegi.md
.ufo/reports/round-2/kagi.md
.ufo/reports/round-3/kagi.md
.ufo/reports/round-3/kake.md
.ufo/reports/round-3/kasegi.md
.ufo/reports/round-3/kengaku.md
.ufo/reports/round-3/kumitate.md
.ufo/reports/round-4/kagi.md
.ufo/reports/round-4/kake.md
.ufo/reports/round-4/kasegi.md
.ufo/reports/round-4/kengaku.md
.ufo/reports/round-4/kotoba.md
.ufo/reports/round-4/kumitate.md
.ufo/reports/round-5/kagi.md
.ufo/reports/round-5/kake.md
.ufo/reports/round-5/kasegi.md
.ufo/reports/round-5/kengaku.md
.ufo/reports/round-5/kotoba.md
.ufo/reports/round-5/kumitate.md
.ufo/reports/round-6/kagi.md
.ufo/reports/round-6/kake.md
.ufo/reports/round-6/kengaku.md
.ufo/reports/round-6/kumitate.md
.ufo/reports/round-7/kagi.md
.ufo/reports/round-7/kake.md
.ufo/reports/round-7/kasegi.md
.ufo/reports/round-7/kengaku.md
.ufo/reports/round-7/kumitate.md
.ufo/reports/round-8/kagi.md
.ufo/reports/round-8/kake.md
.ufo/reports/round-8/kasegi.md
.ufo/reports/round-8/kengaku.md
.ufo/reports/round-8/kotoba.md
.ufo/reports/round-8/kumitate.md
.ufo/reports/round-9/kagi.md
.ufo/reports/round-9/kake.md
.ufo/reports/round-9/kasegi.md
.ufo/reports/round-9/kumitate.md
```

Denominator: `ls .ufo/reports/round-*/*.md | wc -l` → **91**. So 60 / 91 reports carry no
`SHONEN` heading; 31 do (or are `protocol`/`aggregator`-named and excluded by the `grep -vE`).

### 4.6 Report files added under a lane identity

```bash
for f in .ufo/reports/round-*/*.md; do git log --diff-filter=A --format='%an' -1 -- "$f"; done | sort | uniq -c
```

```
     50 Joao Pedro Veiga
      2 aggregator-shokunin
      1 kagi
      1 kengaku-shokunin
      1 kotoba-shokunin
      1 kumitate
      6 protocol-shokunin
     26 shokunin
```

(91 values total, one per report file. `Joao Pedro Veiga` and `shokunin` are non-lane identities →
76 of 91 report-adds were **not** made under a lane identity.)

---

## 5. Fleet state

Instant mixed: §5.1 `2026-09-28T22:11:31-03:00`, §5.2 `2026-09-28T22:11:40-03:00`, §5.3
`2026-09-28T22:11:40-03:00`. HEAD `f3cbdcf` at all three.

### 5.1 Eight `.ufo/state/*.round` counters

```bash
for f in .ufo/state/*.round; do printf '%s = ' "$f"; cat "$f"; done
```

```
.ufo/state/aggregator.round = 9
.ufo/state/kagi.round = 14
.ufo/state/kake.round = 15
.ufo/state/kasegi.round = 15
.ufo/state/kengaku.round = 12
.ufo/state/kotoba.round = 15
.ufo/state/kumitate.round = 14
.ufo/state/protocol.round = 13
```

Companion listing (`ls -la .ufo/state/`) shows eight `.round` files and eight `.mission` files,
mtime `21:14`–`21:52`:

```
-rw-r--r-- 1 vgpnk vgpnk  35 Sep 28 21:14 aggregator.mission
-rw-r--r-- 1 vgpnk vgpnk   2 Sep 28 21:14 aggregator.round
-rw-r--r-- 1 vgpnk vgpnk  30 Sep 28 21:52 kagi.mission
-rw-r--r-- 1 vgpnk vgpnk   3 Sep 28 21:52 kagi.round
-rw-r--r-- 1 vgpnk vgpnk  30 Sep 28 21:44 kake.mission
-rw-r--r-- 1 vgpnk vgpnk   3 Sep 28 21:44 kake.round
-rw-r--r-- 1 vgpnk vgpnk  32 Sep 28 20:50 kasegi.mission
-rw-r--r-- 1 vgpnk vgpnk   3 Sep 28 20:50 kasegi.round
-rw-r--r-- 1 vgpnk vgpnk  33 Sep 28 21:21 kengaku.mission
-rw-r--r-- 1 vgpnk vgpnk   3 Sep 28 21:21 kengaku.round
-rw-r--r-- 1 vgpnk vgpnk  32 Sep 28 21:36 kotoba.mission
-rw-r--r-- 1 vgpnk vgpnk   3 Sep 28 21:36 kotoba.round
-rw-r--r-- 1 vgpnk vgpnk  34 Sep 28 21:52 kumitate.mission
-rw-r--r-- 1 vgpnk vgpnk   3 Sep 28 21:52 kumitate.round
-rw-r--r-- 1 vgpnk vgpnk  34 Sep 28 21:52 protocol.mission
-rw-r--r-- 1 vgpnk vgpnk   3 Sep 28 21:52 protocol.round
```

### 5.2 Live missions and ages (from `--json`)

```bash
python3 .ufo/waves/round-12/closure-check.py --no-citations --json | python3 -c "
import json,sys; d=json.load(sys.stdin)
for k in ('live_missions','stale_missions'):
    print('==',k,len(d[k]),'==')
    for m in d[k]: print('%-11s r%-3s age=%-5s %s | %s'%(m['lane'],m['lane_round'],m['age_seconds'],m['verdict'],m['launch']))
"
```

```
== live_missions 7 ==
protocol    r13  age=1179  progressing | 2026-09-28T21:52:01-03:00 launch protocol round=13 runId=shokunin-r13-protocol-r1790643117
aggregator  r9   age=3450  progressing | 2026-09-28T21:14:10-03:00 launch aggregator round=9 runId=shokunin-r9-aggregator-r1790640845
kengaku     r12  age=2992  progressing | 2026-09-28T21:21:48-03:00 launch kengaku round=12 runId=shokunin-r12-kengaku-r1790641306
kake        r15  age=1635  silent | 2026-09-28T21:44:25-03:00 launch kake round=15 runId=shokunin-r15-kake-r1790642664
kumitate    r14  age=1174  progressing | 2026-09-28T21:52:06-03:00 launch kumitate round=14 runId=shokunin-r14-kumitate-r1790643122
kotoba      r15  age=2087  progressing | 2026-09-28T21:36:53-03:00 launch kotoba round=15 runId=shokunin-r15-kotoba-r1790642212
kagi        r14  age=1168  progressing | 2026-09-28T21:52:12-03:00 launch kagi round=14 runId=shokunin-r14-kagi-r1790643128
== stale_missions 7 ==
protocol    r13  age=1179  progressing | 2026-09-28T21:52:01-03:00 launch protocol round=13 runId=shokunin-r13-protocol-r1790643117
aggregator  r9   age=3450  progressing | 2026-09-28T21:14:10-03:00 launch aggregator round=9 runId=shokunin-r9-aggregator-r1790640845
kengaku     r12  age=2992  progressing | 2026-09-28T21:21:48-03:00 launch kengaku round=12 runId=shokunin-r12-kengaku-r1790641306
kake        r15  age=1635  silent | 2026-09-28T21:44:25-03:00 launch kake round=15 runId=shokunin-r15-kake-r1790642664
kumitate    r14  age=1174  progressing | 2026-09-28T21:52:06-03:00 launch kumitate round=14 runId=shokunin-r14-kumitate-r1790643122
kotoba      r15  age=2087  progressing | 2026-09-28T21:36:53-03:00 launch kotoba round=15 runId=shokunin-r15-kotoba-r1790642212
kagi        r14  age=1168  progressing | 2026-09-28T21:52:12-03:00 launch kagi round=14 runId=shokunin-r14-kagi-r1790643128
```

`live_missions` and `stale_missions` are the same 7 objects at this instant (every live mission is
> 900 s, so all are flagged stale); the gate's §Tallies line reads
`live missions: 7 (stale > 900 s: 7)`. Six grade `progressing`; **kake r15 grades `silent`**.

### 5.3 `tail -20 .ufo/watchdog.log`

```bash
tail -20 .ufo/watchdog.log
```

```
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
2026-09-28T21:51:57-03:00 complete protocol round=12; respawning
2026-09-28T21:52:01-03:00 launch protocol round=13 runId=shokunin-r13-protocol-r1790643117
2026-09-28T21:52:02-03:00 complete kumitate round=13; respawning
2026-09-28T21:52:06-03:00 launch kumitate round=14 runId=shokunin-r14-kumitate-r1790643122
2026-09-28T21:52:08-03:00 complete kagi round=13; respawning
2026-09-28T21:52:12-03:00 launch kagi round=14 runId=shokunin-r14-kagi-r1790643128
2026-09-28T21:52:12-03:00 tick=33
2026-09-28T21:59:42-03:00 tick=34
2026-09-28T22:07:12-03:00 tick=35
```

`wc -l .ufo/watchdog.log` → **236** (matches the gate's `log_lines: 236`).

---

## 6. Round-13 wave inventory (pinned at run instant)

Instant `2026-09-28T22:12:55-03:00`, HEAD `f3cbdcf`. **This directory is a live write target** —
siblings were landing artifacts between 22:11 and 22:13, so a later re-run WILL differ; the hashes
below pin the wave as of this instant.

```bash
ls -la .ufo/waves/round-13/
```

```
total 192
drwxr-xr-x 1 vgpnk vgpnk   254 Sep 28 22:12 .
drwxr-xr-x 1 vgpnk vgpnk    86 Sep 28 21:58 ..
-rw-r--r-- 1 vgpnk vgpnk 49269 Sep 28 22:11 PROTOCOL.compact.md
drwxr-xr-x 1 vgpnk vgpnk    66 Sep 28 22:12 __pycache__
-rwxr-xr-x 1 vgpnk vgpnk 75819 Sep 28 22:12 closure-check.r13.py
-rw-r--r-- 1 vgpnk vgpnk 10944 Sep 28 22:11 critic-plan.md
-rw-r--r-- 1 vgpnk vgpnk  8741 Sep 28 22:12 labrat.md
drwxr-xr-x 1 vgpnk vgpnk   258 Sep 28 22:12 mutants
-rw-r--r-- 1 vgpnk vgpnk 11213 Sep 28 22:12 reviewer-step1.md
-rw-r--r-- 1 vgpnk vgpnk 13575 Sep 28 22:12 sentinel-trust.md
-rw-r--r-- 1 vgpnk vgpnk  9778 Sep 28 22:12 simplifier.md
```

```bash
for f in .ufo/waves/round-13/*; do if [ -f "$f" ]; then sha256sum "$f"; wc -c "$f"; fi; done
```

```
22cb61ce89ce6af42dfb7b753d952ca0cbc7a22532c5a01b0c9aca72b8ac4638  .ufo/waves/round-13/PROTOCOL.compact.md
49269 .ufo/waves/round-13/PROTOCOL.compact.md
5e53d62c90c06b231027f8e5b34e930148be1f2544f81d9b8f58979dbb1ff921  .ufo/waves/round-13/closure-check.r13.py
75819 .ufo/waves/round-13/closure-check.r13.py
1f96e572dc816b3ee9d743f5cf97c594ff6a557f4da59602ac7dd67d9c13f4c3  .ufo/waves/round-13/critic-plan.md
10944 .ufo/waves/round-13/critic-plan.md
ad5516e5c6101ee3d4f12833202365853e2a145d39e1235cb0db8ebf9b05c4c8  .ufo/waves/round-13/labrat.md
8741 .ufo/waves/round-13/labrat.md
95ce59774fcfd09442db21c9af7c411833bf71716b50dca22ae0bf18dc0c931f  .ufo/waves/round-13/reviewer-step1.md
11213 .ufo/waves/round-13/reviewer-step1.md
b1a0003440a5eb055dfaabb6890b69ce2d654c8fe8af21fde87ff179e3b39d12  .ufo/waves/round-13/sentinel-trust.md
13575 .ufo/waves/round-13/sentinel-trust.md
84de9c3d47a47072eabc0c9a41e2743af6b664b4c19e4b415a647f4541090e96  .ufo/waves/round-13/simplifier.md
9778 .ufo/waves/round-13/simplifier.md
```

Two subdirectories (`__pycache__/` from the r13 checker import, `mutants/`) hold no listed files at
this instant (`find .ufo/waves/round-13/mutants -maxdepth 2 -type f` at 22:12:09 returned nothing).

**State of the two coupled moves, as measured here:**

```bash
sha256sum PROTOCOL.md; cmp -s PROTOCOL.md .ufo/waves/round-13/PROTOCOL.compact.md && echo IDENTICAL || echo DIFFER
```

```
22cb61ce89ce6af42dfb7b753d952ca0cbc7a22532c5a01b0c9aca72b8ac4638  PROTOCOL.md
IDENTICAL
```

`PROTOCOL.compact.md` is currently a **byte-identical seed copy** of `PROTOCOL.md` (same sha256, same
526/49269). It carries the census at `93/93 obligations found; 0 MISSING`, exit 0 — but that is
predicate preservation of the *uncompacted* text, not the compaction result. See §7.

`.ufo/waves/round-13/history-pin.json` **does not exist**:

```bash
ls -la .ufo/waves/round-13/history-pin.json
```

```
ls: cannot access '.ufo/waves/round-13/history-pin.json': No such file or directory
```

`closure-check.r13.py` is `closure-check.py` + 28 diff lines adding `_history_pin_finding()`, which
reads `.ufo/waves/round-13/history-pin.json` and hashes canonical JSON of `rounds[0:k]`. Live run at
HEAD `f3cbdcf` (r13 checker, instant `2026-09-28T22:12:03-03:00`):

```bash
python3 .ufo/waves/round-13/closure-check.r13.py --no-citations; echo "EXIT=$?"
```

```
closure-check: debt debt=7 contradictions=0 unrowed_terminated=1 pending_round=5
== Debt (exit-1 drivers): 7 ==
history_pin_unavailable -          rNone entry=-    cannot evaluate append-only history pin: missing /home/vgpnk/projects/shokunin/.ufo/waves/round-13/history-pin.json
```

So the r13 checker currently reports `debt=7` (the live 6 + the unavailable pin) — the m1 detector
exists in code but is **unusable until the pin file is committed** (§7).

---

## 7. PENDING — figures that cannot be taken yet

Each entry names what must exist first and the exact command to run at that time.

### P1 — Compacted `PROTOCOL.md` size (blocks the axis-move claim)

*Must exist first:* `PROTOCOL.md` rewritten to the compacted form and committed (i.e.
`.ufo/waves/round-13/PROTOCOL.compact.md` must no longer be byte-identical to the pre-compaction
file). At this instant `cmp -s PROTOCOL.md .ufo/waves/round-13/PROTOCOL.compact.md` → identical.

```bash
date -Is && git rev-parse --short HEAD && wc -l -c PROTOCOL.md
awk 'NR<487' PROTOCOL.md | grep -o 'round-[0-9][0-9.]*' | wc -l      # must be <= 4
awk 'NR>=487' PROTOCOL.md | grep -o 'round-[0-9][0-9.]*' | wc -l
```

Pass condition: lines **≤ 470**, bytes recorded, body refs **≤ 4**. Note the `## Appendix` line may
move under compaction — re-derive it with `grep -n '^## Appendix' PROTOCOL.md` and use that line
number in place of `487` before these two `awk` commands are meaningful.

### P2 — Extended census (blocks "93/93 AND covering the seven pins + `## Gate standard`")

*Must exist first:* a committed census diff adding, per `.ufo/waves/round-13/critic-plan.md`
§Blocker 3, **seven named pin predicates** plus a `^## Gate standard` predicate. Measured now:
`grep -c 'Gate standard' .ufo/waves/round-11/obligation-census.tsv` → **0**, and the seven pin names
from `.ufo/reports/round-12/protocol.md` §"Protocol amendments — seven pins" match **0** census rows
each (`Row identity` 0, `Orphaned-report` 0, `Filed-report` 0, `progressing-weak` 0, `landed report`
0; only generic `append-only` 3 / `supersedes` 1).

```bash
sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md > /tmp/census2.out 2>&1; echo "EXIT=$?"
tail -3 /tmp/census2.out
grep -c '^MISS' /tmp/census2.out
wc -l .ufo/waves/round-11/obligation-census.tsv
grep -c 'Gate standard' .ufo/waves/round-11/obligation-census.tsv
```

Pass condition: exit 0, `0 MISSING`, denominator ≥ 101 (93 + seven pins + Gate standard), and the
`Gate standard` grep ≥ 1.

### P3 — `MANIFEST.json` after the closure entries are appended

*Must exist first:* the closure-correction that closes the stale rows (protocol r12, kake r14,
kumitate r13, kotoba r14, kagi r13) and that rows `kasegi r15` terminally — i.e. the live gate's
`debt` must fall to 0.

```bash
date -Is && git rev-parse --short HEAD
python3 .ufo/waves/round-12/closure-check.py --no-citations; echo "EXIT=$?"
python3 .ufo/waves/round-12/closure-check.py --no-citations --json | python3 -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d['counts'],sort_keys=True))"
python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['rounds']))"
sha256sum MANIFEST.json
git ls-files -o --exclude-standard .ufo/reports .ufo/prompts
```

Pass condition: `debt=0 contradictions=0 unrowed_terminated=0`; new entry count, new sha256, and the
emptied untracked-report/prompt list recorded.

### P4 — `--frozen` generalization (baselines outside `.ufo/waves/round-12/`)

*Must exist first:* a checker in which `do_frozen()` resolves the snapshot directory from a
configurable root. Measured now: `.ufo/waves/round-12/closure-check.py:1355-1356` hard-codes
`os.path.join(repo, ".ufo", "waves", "round-12", "frozen", which)`, and `--help` still prints
`re-run against .ufo/waves/round-12/frozen/<NAME>`. **`--frozen` with a round-13 path is PENDING**
until that line changes; there is no round-13 frozen snapshot yet either.

```bash
date -Is && git rev-parse --short HEAD
python3 .ufo/waves/round-13/closure-check.r13.py --help | grep -A2 -- '--frozen'
ls -la .ufo/waves/round-13/frozen/ 2>&1
python3 .ufo/waves/round-13/closure-check.r13.py --frozen <NAME>; echo "EXIT=$?"
```

Pass condition: `--help` no longer names `round-12`; a non-`round-12` baseline resolves; each
`--frozen <NAME>` run prints `baseline: match` with the pinned exit code.

### P5 — History pin / m1 detector armed

*Must exist first:* a committed `.ufo/waves/round-13/history-pin.json` containing integer `k` and a
sha256 of canonical `rounds[0:k]`. Measured now: the file is absent, and the r13 checker reports
`history_pin_unavailable` (debt 6 → 7). This is the detector for mutant **m1**, which round 12 left
`not-applicable (legacy unadjudicable entry)` / survived
(`.ufo/waves/round-12/mutants/mutant-score.json`).

```bash
date -Is && git rev-parse --short HEAD
ls -la .ufo/waves/round-13/history-pin.json
python3 .ufo/waves/round-13/closure-check.r13.py --no-citations --json | python3 -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d['counts'],sort_keys=True))"
# m1 kill proof: flip the legacy status under the pin, expect history_pin_mismatch
jq '(.rounds[3].lanes.aggregator) = "ok"' MANIFEST.json > /tmp/m1.json   # mutated copy only, never the live file
```

Pass condition: pin present; unmutated live run shows no `history_pin_*` debt; the mutated copy makes
the checker emit `history_pin_mismatch` (m1 killed, not survived).

### P6 — Round-13 closure verdicts for the ledger rows

*Must exist first:* all round-13 lane reports and missions terminated, then the round-13 closure
entries committed.

```bash
date -Is && git rev-parse --short HEAD
for f in .ufo/reports/round-13/*.md; do printf '%s  %s\n' "$(wc -c <"$f")" "$f"; done
python3 .ufo/waves/round-12/closure-check.py --no-citations | head -1
```

Pass condition: one row per dispatched round-13 lane; first line reads `debt=0`.

### P7 — Report-authoring identities after round-13 lands

*Must exist first:* the round-13 reports committed (the §4.6 tally is a moving target).

```bash
for f in .ufo/reports/round-*/*.md; do git log --diff-filter=A --format='%an' -1 -- "$f"; done | sort | uniq -c
grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-13/*.md | grep -vE 'protocol|aggregator|AGGREGATE' | wc -l
```

### P8 — Round-13 wave inventory, final

*Must exist first:* all round-13 seats stopped writing.

```bash
date -Is && git rev-parse --short HEAD && ls -la .ufo/waves/round-13/
for f in .ufo/waves/round-13/*; do if [ -f "$f" ]; then sha256sum "$f"; wc -c "$f"; fi; done
```

Not-yet-existing artifacts referenced by round-13 docs, so their figures are PENDING:
`.ufo/waves/round-13/history-pin.json` (§P5), `.ufo/waves/round-13/mutants/*` (the r13 mutant
fixtures; the dir exists but `find … -type f` returns nothing), and a round-13 frozen snapshot dir.

---

## Cross-reference — this worksheet's `scribe-measurements.md` instant

This file was written after the §6 inventory instant; its own hash is therefore **not** in §6. Pin it
when citing the worksheet itself:

```bash
sha256sum .ufo/waves/round-13/scribe-measurements.md && wc -c .ufo/waves/round-13/scribe-measurements.md
```

`PENDING: <hash>` — cannot be self-measured by the writing process; run the command above to fill it.