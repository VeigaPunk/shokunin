# Seat: corpus-sweep — reports since the refresh-7 cutoff → routed-defect candidates + discharge verdicts

Seat: `CorpusSweepScout` · round: aggregator r11 (refresh 8) · working dir `/home/vgpnk/Projects/shokunin`
Mode: read-only on all fleet state except this file. No child-repo write, no commit, no push.
Volatile measurements stamped with `date -u` at the instant they were taken; every claim below carries its verbatim command.

**Stamp of the live measurements in §3(a), §3(g): `2026-09-29T03:27:19Z` (run from the main repo root).**
Stamp of the harness re-runs in §3(f), §3(h): `2026-09-29T03:28–03:30Z`.

---

## 1. Sweep coverage

### 1.1 Cutoff method

Declared cutoff: `2026-09-29T01:21:29Z`, declared main HEAD `383ea1a`.

```
$ date -u
Tue 29 Sep 2026 03:26:00 AM UTC
$ git log --oneline 383ea1a..HEAD | wc -l
34                       # topology delta, NOT the cutoff delta — see caveat
$ git log --since='2026-09-29T01:21:29Z' --name-only --format='%h %aI %s' -- .ufo/reports/
```

**Cutoff caveat (measured, affects who re-runs this window).** The declared HEAD `383ea1a` was created
`2026-09-28T21:51:23-03:00` = `00:51:23Z`; the declared cutoff instant `01:21:29Z` is 30 min later, so the
topology range `383ea1a..HEAD` (34 commits) is *wider* than the `--since` window and would re-sweep refresh-7's own
artifacts (`6415a9b`, `cc6d9d4`, `2d19a64`, `f3cbdcf`, …). The `--since` form is authoritative here; the topology form
is reported only so the L1 does not mistake one for the other:

```
$ git merge-base --is-ancestor 383ea1a 17c1fad && echo YES
YES
$ git merge-base --is-ancestor 2d19a64 383ea1a && echo YES || echo NO
NO                       # the kama mint entry postdates the declared refresh-7 HEAD
```

Because git's `--since` keys on committer date and reports can be committed long after they are written, the window
was **also** swept by filesystem mtime, and every file found by either method was classified by introducing commit:

```
$ find .ufo/reports -type f -name '*.md' -newermt '2026-09-29T01:21:29Z' -printf '%p %s\n' | sort
$ git ls-files --others --exclude-standard .ufo/
# → no untracked report at any contract path (untracked = 9 prompts, watchdog-driver.log, kama-shokunin/)
```

### 1.2 Files examined (23 report files in window + 14 seat-scratch files + 2 ledger/queue files; all tracked)

Every row below was verified by `git log --since` **and** by filesystem mtime; the one context-only row is marked.

| Round file | bytes | introducing commit | date | content class | defects/debts read |
|---|---:|---|---|---|---|
| `round-1/kama.md` | 10144 | `74768ab` | 23:15:55 | real report (mint round 1) | §Adjacency, §Residual gaps, §L0 (3 rows) |
| `round-9/aggregator.md` | 18604 | `cc6d9d4` | 22:34:10 | real (ledger r9 + §14.18) | D-150 carrier, 740/782 verdict |
| `round-10/aggregator.md` | 187 | `f5d8507` | 23:41:38 | **marker** (5 lines) | none — names no commit; grade = marker |
| `round-12/kagi.md` | 13620 | `b5fff81` | 22:59:26 | real (orphaned r12) | §1–§3, ceilings |
| `round-12/kotoba.md` | 14009 | `b5fff81` | 22:59:26 | real (orphaned r12, literal `LANE_HASH` frozen) | carried gap (host-anchored pointers) |
| `round-12/kengaku.md` | 274 | `17c1fad` | 00:19:02 | **marker** | none |
| `round-13/kengaku.md` | 4220 | `17c1fad` | 00:19:02 | real but **plan-only, no results** | §Data walk + plan; 0 hashes, 0 SHONEN heading → **R7** |
| `round-13/protocol.md` | 275 | `17c1fad` | 00:19:02 | **marker** | none |
| `round-14/kagi.md` | 15271 | `17c1fad` | 00:19:02 | real (§Class 6 + bounds 17–23) | §Bounds, §Adjacency, deferred D-129 pointer |
| `round-14/kotoba.md` | — | `ad73e6f` | 23:13:53 | real (inherited, `[PENDING]` verdicts + erratum at `4419fb9`) | erratum §10 of r15 |
| `round-14/protocol.md` | 340 | `ef36757` | 23:52:27 | **marker** (wrap) | names 24 modified working-tree paths |
| `round-15/kagi.md` | 13554 | `3485880` | 22:56:45 | real (operability 8→9) | §Defects 1–8, §Adjacency |
| `round-15/kake.md` | 7486 | `3069841` | 22:52:19 | real (freshness 8→9) | 5 danglers, PQ-12/5/2, L0 corroboration |
| `round-15/kasegi.md` | 15865 | `f3cbdcf` | 22:06:22 | real (root-loss forensics) — **out of window** (commit and mtime both < cutoff); read as D-135/D-150 context | §Adjacency 339 refs, §L0 3 rows |
| `round-15/kotoba.md` | **273 (HEAD)** vs **14715 (`4419fb9`)** | `17c1fad` overwrote `4419fb9` | 00:19:02 / 23:14:00 | **marker overwriting a real report** | → **R1** |
| `round-15/kumitate.md` | 9072 | `4d518fe` | 23:28:11 | real (recovered r15) | §Limits, R11 census |
| `round-15/scratch/*.md` | 14 files, 4.5–41 KB | `17c1fad` | 00:19 | kagi r15 L2 seat files | keyword sweep → E4 `op://` RED row, HITS=2 baseline |
| `round-16/kagi.md` | 15021 | `17c1fad` | 00:19:02 | real (adjacency 8→9) | §Adjacency routed `surface-census.sh:75` → **R9** |
| `round-16/kake.md` | 12005 | `c3b0c0e` | 23:44:26 | real (freshness 9→10) | PQ-14 ← **R11**, 5-instants prune regime |
| `round-16/kasegi.md` | 273 | `17c1fad` | 00:19:02 | **marker** while r16 work exists only in L0 | → **R8** |
| `round-16/kotoba.md` | 9700 | `208db49` | 23:38:21 | real (operability 8.0→8.5) | §Cross-domain R3 dead citations → **R10** |
| `round-16/kumitate.md` | 15354 | `3f2c7cf` | 23:37:48 | real (successors 6/6) | cite-check fence defect, r15-commit recovery |
| `round-17/kasegi.md` | 4708 | `17c1fad` | 00:19:02 | real but **no own commit cited** | → **R6** |
| `AGGREGATE.md` | 234064 | `cc6d9d4` | 22:31/22:34 | aggregator ledger r9 | §14.18 blast radius, D-121…D-150 |
| `.ufo/l0-questions.md` | 19 lines | `17c1fad` (last) | 00:19:02 | fleet L0 queue | → **R12** |

Also read as primary (not report files, read-only): `MANIFEST.json`, `SCORECARD.md`, `CORPUS.md`, `PROTOCOL.md`
(grep only), `.ufo/watchdog.log`, `.ufo/state/*`, `kama-shokunin/{MINT,LOG,SCORECARD,SHONEN}.md`.

**Zero report files landed outside these 36; zero untracked reports.**

### 1.3 Routed-defect inventory already in the ledger (cross-checked, do not re-file)

`D-135` (kasegi `PROVINCE.md`+`SKILL.md` still name the absent root; 740/782 unresolvable) · `D-150` (four other
surfaces cite it) · `D-143` (stale `rounds` rows) · `D-144`/`D-145`/`D-146` (untracked report/prompt durability) ·
`D-147` (axis switched without amending §Planned) · `D-148`/`D-149` (`SHONEN.md` form) · `D-96` (`~/.config/opencode`
ownership; kagi r16 re-raises it) · `D-78` (AXES.md↔MISSION.md naming; kotoba r15/r16 + kengaku re-raise it) ·
`D-87` (queue-key reuse). **Max existing key is `D-150`, not `D-149`** — `D-150` landed in `cc6d9d4` (22:34, inside
this window):

```
$ grep -oE 'D-[0-9]{2,3}' .ufo/reports/AGGREGATE.md | sort -u -t- -k2 -n | tail -3
D-148
D-149
D-150
$ grep -c 'D-150' .ufo/reports/AGGREGATE.md
2
```

⇒ the L1 assigns the rows below **from `D-151`**.

---

## 2. Proposed new D-rows (text only — L1 assigns keys)

Severity on the ledger's 1–4 scale (4 = blocking the fleet's own accounting, 1 = cosmetic).

**R1 — target: `.ufo/reports/round-15/kotoba.md` (integrator / wrap process). Severity 4.**
*The wrap process overwrote a landed lane report with a 273-byte closeout marker at the report's contract path; the
real 225-line report survives only inside `4419fb9`.* Unique instance fleet-wide (checked over every tracked report).

```
$ git show 4419fb9:.ufo/reports/round-15/kotoba.md | wc -l      # 225
$ git show HEAD:.ufo/reports/round-15/kotoba.md | wc -l         # 5
$ git log -S 'kotoba round-15 closeout (marker)' --format='%h %aI %s' -- .ufo/reports/round-15/kotoba.md
17c1fad 2026-09-29T00:19:02-03:00 fleet relaunch: ...
# uniqueness sweep (every tracked report: HEAD bytes vs the largest revision ever committed at that path)
$ for f in $(git ls-files '.ufo/reports/**/*.md'); do cur=$(git show HEAD:"$f" | wc -c); if [ "$cur" -lt 500 ]; then big=$(git log --format=%H -- "$f" | while read c; do n=$(git show $c:"$f" 2>/dev/null | wc -c); echo "$c $n"; done | sort -k2 -n | tail -1); echo "$f head=$cur max=$big"; fi; done
.ufo/reports/round-10/aggregator.md head=187 max=f5d8507... 187
.ufo/reports/round-12/kengaku.md head=274 max=17c1fad... 274
.ufo/reports/round-13/protocol.md head=275 max=17c1fad... 275
.ufo/reports/round-14/protocol.md head=340 max=ef36757... 340
.ufo/reports/round-15/kotoba.md head=273 max=4419fb9... 14715     ← the only overwrite
.ufo/reports/round-16/kasegi.md head=273 max=17c1fad... 273
.ufo/reports/round-5/aggregator.md head=254 max=0a30b44... 254
.ufo/reports/round-7/kumitate.md head=122 max=0a30b44... 122
.ufo/reports/round-8/kengaku.md head=101 max=0a30b44... 101
.ufo/reports/round-8/kotoba.md head=120 max=0a30b44... 120
```

**R2 — target: closure ledger (`MANIFEST.json` `rounds[]`) / protocol lane. Severity 4. Extends D-143; new class.**
*The ledger has no closure entry for any lane-round terminated after `2026-09-28T22:23:00-03:00`: 39 terminations
follow that instant (wrap lines 23:39:57–23:55:00, relaunch lines 00:19:29–00:19:34) and every post-wrap report
(kake r16, kagi r16, kotoba r16, kumitate r16, kasegi r16/r17, kama r1/r2, aggregator r10) is unclosed.*

```
$ python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print(len(r),max(x['closed_at'] for x in r if x.get('closed_at')))"
48 2026-09-28T22:23:00-03:00
$ awk '$1>="2026-09-28T22:23:00"' .ufo/watchdog.log | grep -cE 'wrap .* complete|complete .*respawning'
39
$ grep -c kama MANIFEST.json      # 1 — only the round-11.5 mint note; no closure row names the lane
```

**R3 — target: the aggregator's own standing metric "Mints executed" (aggregator/operator). Severity 3.**
*The mint is recorded as `rounds[].type == "mint"`; every published metric counts the `minted` array, so it reports
0 over 48 entries and the ledger's own "0 mints executed" is a metric artifact, not a fact.*

```
$ python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print([x['round'] for x in r if x.get('type')=='mint'], sum(1 for x in r if x.get('minted')))"
[11.5] 0
$ grep -n 'mints executed\|Mints executed' .ufo/reports/AGGREGATE.md
1291:**Mints executed: 0** — `python3 -c "...sum(1 for x in r if x.get('minted'))"` → 0 over **22** entries
1720:- **Mints executed: 0** over **36** `rounds` entries (... → 36 × `[]`)
```

**R4 — target: `MANIFEST.json` `roster` vs the 7-lane fleet (aggregator/operator). Severity 3.**
*The roster names 6 lanes while 7 lane repos exist; the kama row is deliberately withheld under the new sibling-mint
clause (probation, ≥3 verified self-iteration rounds), but no standing table records that probation gate, so the
dormancy table (7 rows) and the roster (6 rows) cannot be reconciled by a non-author.*

```
$ python3 -c "import json;print([r['id'] for r in json.load(open('MANIFEST.json'))['roster']])"
['kasegi','kengaku','kake','kumitate','kotoba','kagi']
$ ls -d *-shokunin
kagi-shokunin kake-shokunin kama-shokunin kasegi-shokunin kengaku-shokunin kotoba-shokunin kumitate-shokunin
$ python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print([x['notes'] for x in r if x.get('type')=='mint'][0][:120])"
sibling-mint allowance landed in PROTOCOL.md Lifecycle; kama-shokunin minted in probation ...
```

**R5 — target: main-repo `.gitignore` (operator meta-file). Severity 3. kama r1 L0 line 17, still open.**
*`8afbc8f` untracked the embedded kama gitlink but the ignore rule was never added, so the nested repo is untracked
again and a main-repo `git add -A` re-stages it as a gitlink.*

```
$ git check-ignore -v kumitate-shokunin                     # .gitignore:4:kumitate-shokunin/
$ git check-ignore -v kama-shokunin || echo NOT-IGNORED     # NOT-IGNORED (exit 1)
$ git status --porcelain | grep kama-shokunin               # ?? kama-shokunin/
$ git show --stat --format='%h %aI %s' 8afbc8f              # kama-shokunin | 1 -
$ sed -n '17p' .ufo/l0-questions.md                         # kama r1 hygiene-gap row, unacked
```

**R6 — target: kasegi r16/r17 child work (kasegi). Severity 4.**
*`kasegi-shokunin` has 27 modified + 2 untracked paths (round-16/17 work) against a HEAD whose newest commit is
`b021dc9` (22:19, a round-9 aggregator lesson); the round-17 report claims changed files but cites no lane commit —
the D-144/D-145 non-durability class, now live and larger.*

```
$ git -C kasegi-shokunin status --porcelain | awk '{print substr($0,1,2)}' | sort | uniq -c
     27  M
      2 ??
$ git -C kasegi-shokunin log --format='%h %aI %s' -1
b021dc9 2026-09-28T22:19:05-03:00 corpus: round-9 aggregator corpus-verdict lesson (...)
$ grep -o -E '\b[0-9a-f]{7,40}\b' .ufo/reports/round-17/kasegi.md | sort -u
1307b8b                      # the read-only source repo's HEAD, not a kasegi commit
```

**R7 — target: kengaku r13 report (kengaku + protocol's `report_of()`). Severity 3.**
*A round report with a data walk and a plan but no results, no cited commit and no SHONEN heading closed a
lane-round on file existence (kengaku r13→14 launched 00:19:30).*

```
$ grep -c -E '^#+ SHONEN' .ufo/reports/round-13/kengaku.md                  # 0
$ grep -o -E '\b[0-9a-f]{7,40}\b' .ufo/reports/round-13/kengaku.md | wc -l  # 0
$ grep -n -E '^#+' .ufo/reports/round-13/kengaku.md                          # 3 headings, last = '## WWKD plan'
$ git -C kengaku-shokunin log --format='%h %aI %s' -1                      # e171cdf 22:19:06 (round-9 lesson)
```

**R8 — target: kasegi r16 report (protocol marker grading / kasegi). Severity 2.**
*`round-16/kasegi.md` is a 273-B marker naming no commit although the round did verifiable work (the groknight
source-loss forensics survive only as L0 line 16) — marker grade, excluded from dormancy pairs.*

```
$ cat .ufo/reports/round-16/kasegi.md | wc -c   # 273; 5 lines; no hash
$ sed -n '16p' .ufo/l0-questions.md | cut -c1-120
kasegi | round-16 | SECOND in-round source loss on a surviving domain root: ...
```

**R9 — target: `kagi-shokunin/corpus/surface-census.sh:75` (kagi). Severity 3. Routed by kagi's own r16 report.**
*The bootstrap silent-death class fixed in `scope-gate.sh` at r16 still stands in the sibling gate: an unresolvable
script dir exits 1 with no verdict line, so a broken environment is indistinguishable from "drift found".*

```
$ sed -n '74,75p' kagi-shokunin/corpus/surface-census.sh
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
CENSUS="$SCRIPT_DIR/surface-census.tsv"          # resolved with no guard on the resolution
$ grep -c 'SETUP' kagi-shokunin/corpus/surface-census.sh ; grep -c 'SETUP' kagi-shokunin/corpus/scope-gate.sh
0
3                                                # the sibling gate carries the guard (r16 §Evidence: exit 2)
$ sed -n '/Routed defect (same class, another gate)/,+3p' .ufo/reports/round-16/kagi.md
```

**R10 — target: six sibling `SKILL.md` files via kotoba's R3 predicate (kumitate/protocol + each owning lane).
Severity 2.**
*Dead path citations under the landed `citation_resolves` predicate: kagi 2, kake 1, kasegi 1, kengaku 1,
kumitate 5; the two checklist dialects' consolidation (kotoba map+registry vs kumitate box grammar) is the
unrouted half.*

```
$ sed -n '86,95p' .ufo/reports/round-16/kotoba.md            # the routed paragraph, verbatim
$ sed -n '167,171p' <(git show 4419fb9:.ufo/reports/round-15/kotoba.md)   # the dialect split + kagi corpus/claim-ledger.sh example
```
*(Not re-derived here: the sibling scan was a scratch probe inside kotoba's own verifier; the fleet-wide count is
report-attested only.)*

**R11 — target: `plazir-15-site` live/source drift (operator gate / kake). Severity 3.**
*kake r16 caught PQ-14 (live serves a 5-commit-older tree; `/tetris/` loc exists live, missing from `origin/main`)
and ledgered it in its own publish-queue, but no fleet D-row exists — a row that exists in one lane's queue and in
no ledger row is not routable by the integrator.*

```
$ grep -c 'PQ-14' .ufo/reports/AGGREGATE.md       # 0
$ sed -n '/The move, part 3 — in-round domain drift caught (PQ-14)/,+6p' .ufo/reports/round-16/kake.md
```

**R12 — target: `.ufo/l0-questions.md` retraction discipline (protocol/integrator + operator). Severity 2.**
*Line 2 (kama mint-or-reject) is answered in substance (`rounds[11.5]` + the PROTOCOL sibling-mint clause) yet is
byte-identical to `e333e7c`; 7 lines are new since refresh 7 and none carries a disposition field.*

```
$ diff <(git show e333e7c:.ufo/l0-questions.md | sed -n '2p') <(sed -n '2p' .ufo/l0-questions.md) && echo IDENTICAL_LINE2
IDENTICAL_LINE2
$ git show e333e7c:.ufo/l0-questions.md | wc -l ; wc -l < .ufo/l0-questions.md
6
19
$ cat -n .ufo/l0-questions.md | cut -c1-60 | sed -n '13,19p'    # the seven rows added since refresh 7
```

**R13 — target: `SCORECARD.md` header vs its own aggregator sections (protocol/aggregator). Severity 2.**
*The header asserts the aggregator's axes "are not scored here" while §Round 7/8/9 in the same file are exactly
those axis cells (D-77's ruled form); a non-author reading the header concludes the aggregator sections do not
exist.*

```
$ sed -n '3,8p' SCORECARD.md
$ grep -n '^### Round [789]' SCORECARD.md
181:### Round 7 (refresh 5) — mint/dormancy axis-move
199:### Round 8 (refresh 6) — cross-lane-quality axis-move
231:### Round 9 (refresh 7) — corpus-review axis-move
```

**R14 — target: `kama-shokunin/SCORECARD.md` before-values (kama/aggregator). Severity 1.**
*Six axes carry non-zero "before" values (depth 1→7, coverage 1→8, calibration 1→7, adjacency 1→7) in a repo whose
report states it had no `SCORECARD.md` at round start — pre-scores asserted where nothing had been measured.*

```
$ sed -n '7,15p' kama-shokunin/SCORECARD.md
$ grep -n 'no .SCORECARD.md. at round start' .ufo/reports/round-1/kama.md
```

---

## 3. Discharge / re-test verdicts

### (a) kama endpoint state (kama r1 L0 repoint question, lines 13/15) — **OPEN, unchanged**

```
$ date -u; echo "== 34113 health"; curl -s -m3 http://127.0.0.1:34113/health; echo
Tue 29 Sep 2026 03:27:19 AM UTC
== 34113 health
{"status":"ok"}
$ curl -s -o /dev/null -w '%{http_code}\n' -m3 http://127.0.0.1:8080/v1/models
404
$ curl -s -o /dev/null -w '%{http_code} %{content_type}\n' -m3 http://127.0.0.1:8080/
404 text/html;charset=iso-8859-1
$ curl -s -o /dev/null -w '%{http_code} %{content_type}\n' -m3 http://127.0.0.1:8080/metrics
200 application/openmetrics-text;charset=utf-8;version=1.0.0
$ for p in ~/.config/opencode/opencode.json ~/.config/opencode/agents/janitor.md ~/.config/the-janitor/opencode.json; do printf '%s | ' "$p"; grep -o -E '127\.0\.0\.1:8080|localhost:8080|127\.0\.0\.1:34113' "$p" | sort -u | tr '\n' ' '; echo; done
/home/vgpnk/.config/opencode/opencode.json | localhost:8080
/home/vgpnk/.config/opencode/agents/janitor.md | 127.0.0.1:8080
/home/vgpnk/.config/the-janitor/opencode.json | 127.0.0.1:8080
```

Verdict: **D-39/D-85 re-confirmed at `2026-09-29T03:27:19Z`** — 34113 healthy, 8080 HTTP-alive-but-foreign (404 root,
**200** `/metrics` ⇒ status-only liveness still false-passes), all three operator pins still `:8080`, janitor still
`enabled_providers: ["qwen-local"]`-only (fails closed). kama r1's L0 repoint questions (lines 13, 15) are **unacked**;
the fix is one line per pin and remains operator-side.

### (b) kama r1 hygiene gap (.gitignore) — **PARTIALLY DISCHARGED, one half open** → R5

The state-file half was discharged (`17c1fad` added `.ufo/state/kama.{mission,round}`, both now tracked; the
`??` marker is gone). The `.gitignore` half is **open** and now *worse in form*: `8afbc8f` removed the gitlink from
the index without adding the rule, so `git status` shows `?? kama-shokunin/` and `git check-ignore` still returns no
match (commands in R5). Evidence:

```
$ git status --porcelain | grep -E 'kama|gitignore'
?? kama-shokunin/
 M .ufo/state/kama.mission
 M .ufo/state/kama.round
```

### (c) kama r1/r2 dispatch state — **kama is live at round 2** (dormancy relevance)

```
$ cat .ufo/state/kama.round          # 2
$ grep -n 'kama' .ufo/watchdog.log | tail -4
249:2026-09-28T22:44:08-03:00 launch kama round=1 runId=shokunin-r1-kama-r1790646247
293:2026-09-28T23:55:00-03:00 wrap kama round=1 complete; NOT respawning (fleet-wrap)
311:2026-09-29T00:19:33-03:00 complete kama round=1; respawning
312:2026-09-29T00:19:34-03:00 launch kama round=2 runId=shokunin-r2-kama-r1790651973
$ tail -2 .ufo/watchdog.log
2026-09-29T00:19:34-03:00 tick=1
2026-09-29T00:27:04-03:00 tick=2
```

⇒ kama r1 dispatched 22:44:08 and **reported** (`.ufo/reports/round-1/kama.md`, 10144 B, cites `c6199a2` ⇒ real
report, not a marker); r2 dispatched 00:19:34 and live at write time. The lane's dispatch pair (`r1`,`r2`) is
therefore **in-dispatch**, not a dormancy case.

### (d) protocol closure ledger — **mint recorded at `rounds[]` level, closures not** → R2/R3/R4

- The kama mint **is** recorded: `rounds[11.5]`, `type: "mint"`, added by `2d19a64`
  (`2026-09-28T22:44:21-03:00`, message "sibling-mint allowance + kama probation entry"), which also amended
  `PROTOCOL.md` (Lifecycle). **This is 95 min before `17c1fad`,** so the refresh brief's "minted at `17c1fad`"
  framing is imprecise: `17c1fad` relaunched the lane and added the two state files, it did not create the mint record.
- The three-plus lanes' post-wrap activity is **not** recorded: max `closed_at` = `2026-09-28T22:23:00-03:00` over 43
  dated entries (5 undated), while 39 terminations follow that instant.
- Protocol r13/r14 "reports" are 275 B and 340 B markers — they carry no closure content by construction.

```
$ python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print(max(x['closed_at'] for x in r if x.get('closed_at')), sum(1 for x in r), sum(1 for x in r if not x.get('closed_at')))"
2026-09-28T22:23:00-03:00 48 5
$ awk '$1>="2026-09-28T22:23:00"' .ufo/watchdog.log | grep -cE 'wrap .* complete|complete .*respawning'
39
$ git show --name-status --format='%h %aI %s' 2d19a64
M MANIFEST.json
M PROTOCOL.md
```

### (e) kake r15/r16 continuing-deletion corroboration — **no fleet row exists for PQ-14** → R11

kake r16 re-derived all five r15 danglers as still absent and bounded five deletion instants (W1 ≤23:51:31Z,
W2 00:42:39Z, W3 01:45:06Z, W4 ≤02:05:07Z, W5 02:19:20Z). kake's r16 §Adjacency explicitly reports it to
kasegi's r15/r16 L0 carrier, and the prune regime has no committed actor evidence (all `.git` mtimes contaminated).
The only fleet-side gap found is routing, not evidence: `grep -c 'PQ-14' AGGREGATE.md` → 0 (command in R11).

### (f) D-133 — kagi box-3 `[x]` vs red gates — **DISCHARGED (gates cleared)**

D-133's condition was "downgrade the mark **or** clear the gates". Re-test at kagi HEAD (the only revision the
read-only contract permits — running at `587fda0` would require a checkout of the child repo, i.e. a write):

```
$ git -C kagi-shokunin log --format='%h %aI %s' -1
8a6ec16 2026-09-29T00:27:10-03:00 round-16: adjacency axis-move ...
$ timeout 300 bash corpus/claim-ledger.sh verify 2>&1 | tail -2
CLAIM_LEDGER: CLEAN (claims=29 stamped=52 ids=29 cited=29 labeled_ids=17 orphans=0)
EXIT=0
$ timeout 240 bash corpus/claim-ledger.sh citations 2>&1 | tail -1
CITATION_GATE: CLEAN (cites=866 docs=49 unresolved=0 ephemeral=0 labeled=13)     # exit 0
$ timeout 240 bash corpus/transcript-scan.sh 2>&1 | tail -1
TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2 schema-absent=0 db=.../opencode.db)   # exit 1
$ grep -n 'transcript-scan' kagi-shokunin/corpus/claim-ledger.tsv | head -2
20:R11-06  bash corpus/transcript-scan.sh  ^TRANSCRIPT_SCAN: HITS=2 \(cells=[1-9][0-9]*  1  300  known baseline 2026-09-28: 2 prose collisions, 5 credential tripwires empty
```

Read-out: all three gates D-133 named are green — the two that were `exit 1 FAIL/BROKEN` at `4391b3b`/`4b8c018`
(`claim-ledger verify`: 17→29 claims, **CLEAN exit 0**; `citations`: 33 unresolved → **0, CLEAN exit 0**), and
`transcript-scan`, whose `exit 1` is now a **declared, pinned expectation** (`R11-06`, expected pattern
`^TRANSCRIPT_SCAN: HITS=2 …`, note "known baseline 2026-09-28: 2 prose collisions, 5 credential tripwires empty")
inside a ledger that itself verifies CLEAN. Residual for the L1 to word: D-133 is discharged at `8a6ec16`; the
`587fda0` (r15-close) instance is **could-not-evaluate** under the read-only contract, not tested-and-failed.

### (g) D-40 — kama mint-or-reject — **DISCHARGED as a ruling; two ledger artifacts remain** → R3/R4/R12

The question "mint or reject?" is answered: **minted**, by the sibling-mint clause with a probation condition, and
the lane has run a full reported round.

```
$ python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print([x for x in r if x.get('type')=='mint'][0]['notes'][:200])"
sibling-mint allowance landed in PROTOCOL.md Lifecycle; kama-shokunin minted in probation (local model serving &
endpoint health — aggregator mint-eligible r4/r6/r7, demand instances: kagi r3 + kengaku r4 endpoint-drift 8080->34113).
Roster row withheld until >=3 verified self-iteration rounds per the new clause; lane wired into watchdog (m_flash, axes operability+freshness).
$ git show --stat --format='%h %aI %s' 2d19a64 | head -4
$ git -C kama-shokunin log --format='%h %aI %s'
c6199a2 2026-09-28T23:15:05-03:00 round-1: operability axis — runnable endpoint-identity gate ...
9cee9fc 2026-09-28T22:42:49-03:00 seed: kama shonen (sibling mint; see MINT.md)
```

**Not discharged:** (i) the roster row is withheld ⇒ R4; (ii) every "mints executed" metric still reads 0 because it
counts `minted` arrays ⇒ R3; (iii) the L0 sentence is unretracted and byte-identical to `e333e7c` ⇒ R12. The
aggregator's §13.3 line "D-40 stays OPEN, blocked-external" is therefore **falsified in substance** this refresh:
correct wording is *"ruling executed (`rounds[11.5]`, probation; roster row withheld by the clause) — the row's
blocking condition is gone, the ledger's record of it is incomplete."*

### (h) D-77 — SCORECARD collision — **DISCHARGED** (ruled) + one wording residue → R13

```
$ grep -n 'D-77 (`SCORECARD.md` collision)' .ufo/reports/AGGREGATE.md
1235:| D-77 (`SCORECARD.md` collision) | **RULED** | `.ufo/reports/round-11/protocol.md` §Contested-scope rulings 4: per-lane sections in the single canonical path, each lane committing only its own section's hunks; `55e23de` is the reference method. This round complied — its `SCORECARD.md`/`LOG.md` edits touch only the aggregator section |
$ grep -n '^### Round [789]' SCORECARD.md          # the aggregator's own sections, in the same file
$ sed -n '3,8p' SCORECARD.md                       # header still says "are not scored here"
```

Verdict: **DISCHARGED** — the ruling exists (protocol r11) and the practice holds (round 9's §Round 9 section is the
aggregator's own cell in the single canonical path). Residue = the header sentence, filed as R13 (severity 2, one
line). Note this round's L1 must commit only the aggregator's own hunks into that file (the ruling's method).

### (i) D-125 / D-126 / D-141 / D-142 — CORPUS amendments — **ALL OPEN, blocked-external, unamended**

`CORPUS.md` was **not touched at all** in this window and not since round 3:

```
$ ls -l --time-style=+%Y-%m-%dT%H:%M CORPUS.md
-rw-r--r-- 1 vgpnk vgpnk 2926 2026-09-28T16:08 CORPUS.md
$ git log --format='%h %aI %s' -2 -- CORPUS.md
6565e89 2026-09-28T16:13:26-03:00 aggregator round 3: fleet quality review, corpus audit rules, round record versioned
3ff12e0 2026-09-28T15:37:24-03:00 corpus contract, aggregator prompt, 450s watchdog
$ sed -n '43,46p' CORPUS.md            # D-125's rule text, verbatim and unamended
$ grep -nE '^[0-9]+\.|^### |Rule [0-9]' CORPUS.md ; echo "exit=$?"
exit=1                                  # D-126 confirmed: CORPUS.md still numbers no rule
```

- **D-125** (rule 8 bans `op://…` "including this one's examples" while all six corpora carry them) — rule text
  unchanged; still the only rule that every repo's corpus violates literally.
- **D-126** (CORPUS.md numbers no rule, yet every verdict cites a number) — still unnumbered.
- **D-141** (rules 4/9 collide by construction) / **D-142** (rule 7 phantom-only text vs under-coverage practice) —
  operator/integrator text rows; nothing measured this window changes them; the gate's own verdicts
  (`corpus-gate.mjs` self-test 12/12 + 8/8 frozen MATCH at refresh 7) stand unrefreshed.

The L0 carrier for these four is **line 12** (aggregator r9, "CORPUS.md amendment set — four measured
conflicts"), not line 11:

```
$ cat -n .ufo/l0-questions.md | sed -n '11,12p' | cut -c1-90
    11  kotoba | round-13 | Axis-accounting ratification, two items. (1) This round worked the *lowest* axis ...
    12  aggregator | round-9 | CORPUS.md amendment set — four measured conflicts, all operator-side text ...
```

Line 11 (kotoba r13 axis ratification) is a different, also-unacked item; line 12 is the CORPUS set. Both are
byte-stable since introduction (`git log --format='%h %aI' -- .ufo/l0-questions.md` → last touch `17c1fad`), so
nothing was answered or retracted.

### (j) D-129 — round-8 record repair — **DISCHARGED (landed at `17c1fad`, i.e. inside this window)**

D-129 asked for the round-8 X2/X3/X4/X8 cells to be repaired *in place where the file allows it*. The repair is in
the tree at HEAD and was introduced by this window's relaunch commit:

```
$ git log -S 'Round-10 in-place repair of the round-8 record' --format='%h %aI %s' -- SCORECARD.md
17c1fad 2026-09-29T00:19:02-03:00 fleet relaunch: all L1 lanes -> @m_swe; ...
$ git log -S 'repaired at r10 (D-129)' --format='%h %aI' -- SCORECARD.md
17c1fad 2026-09-29T00:19:02-03:00
$ sed -n '215p;221p;223,228p' SCORECARD.md | cut -c1-190
| X2 | cold-run commands executed with exit codes | 0 | **115** (105 ok / 10 fail) ... **repaired at r10 (D-129):** re-derived **99** ...
| X8 | non-author re-executions ... — **repaired at r10 (D-129):** no committed cell ledger exists
> **Round-10 in-place repair of the round-8 record (D-129, queued by §Planned round 9).** ...
```

Four cells now carry the published figure **and** the re-derived figure (X2 115→99, X3 28→17, X4 30→uncountable,
X8 41→unreproducible), plus the explicit statement that the original evidence is permanently unrecoverable:

```
$ ls -d .ufo/waves/round-8
ls: cannot access '.ufo/waves/round-8': No such file or directory
```

Verdict: **DISCHARGED** — the repairable half is repaired in place (at `17c1fad`), and the unrepairable half
(`.ufo/waves/round-8/` absent) is named in-file rather than left implied. One residual, cheap: the round-9
section's "Owed from round 9 (do not let it age) … (D-129); and re-test D-133" line (`SCORECARD.md:276-277`) is now
historically stale on both counts (D-129 repaired at `17c1fad`; D-133 re-tested here as green) — §3(f)/§3(j) are the
re-test; a one-line disposition note in that section would close the loop. Not filed as its own row (sub-cosmetic;
fold into the round's own §Planned hygiene).

---

## 3(k) Addendum — in-flight working-tree delta (measured after §1–§3 were composed)

`.ufo/l0-questions.md` was **modified in the working tree during this sweep** (19 → 20 lines) by a lane that is live
right now; line numbering in §1.2/§3(i) is unaffected because the row was appended last, and line 2 is still
byte-identical:

```
$ date -u
Tue 29 Sep 2026 03:34:18 AM UTC
$ git diff --stat .ufo/l0-questions.md
 .ufo/l0-questions.md | 1 +
$ wc -l < .ufo/l0-questions.md
20
$ diff <(git show e333e7c:.ufo/l0-questions.md | sed -n '2p') <(sed -n '2p' .ufo/l0-questions.md) && echo IDENTICAL_LINE2
IDENTICAL_LINE2
$ sed -n '20p' .ufo/l0-questions.md | cut -c1-160
kake | round-17 | FS-prune regime W6: `~/projects` (lowercase twin of ~/Projects, distinct inode 27238 per r16) vanished between kake r16 sweep ~02:4xZ and r17 baseline 03:20:19Z ...
```

Material for the ledger: this is a **seventh** deletion instant in the `~/Projects` prune regime (W1–W5 were
ledgered by kake r16; `~/projects` lowercase is the *twin* the lane's own FS-trap rule names) and it arrives by
the L0 channel, not by a report — i.e. after `round-17/kake.md` does not exist, a kake r17 finding is already in
the queue. It strengthens §3(e)/R11 (the regime is escalating, still actor-undetermined) and it is the second
instance this round of an L0 row that outruns the report. If the L1 wants a row, it belongs beside R11:
**"W6 (`~/projects` lowercase twin) vanished 02:4x–03:20:19Z; kake r17 L0 line 20; regime now W1–W6"**
(severity 2, owner: operator/L0 durability + kasegi's r15/r16 carrier). It is *not* counted as a finding of this
seat's cutoff window — it landed after §1's enumeration closed.

Also new in the working tree during composition (not mine, not reports): `.ufo/poll.log` (untracked), and the
9 untracked dispatch prompts for the live round-17/18 + aggregator r11 (D-146's class, refreshed).

## 4. Unknowns

- **`kagi` r15-close revision (`587fda0`) gate state** — could-not-evaluate under the read-only contract (would need
  a working-tree checkout of the child repo). Affects: D-133's wording if the L1 wants a revision-by-revision claim;
  the HEAD instance is tested and green.
- **kumitate's cite-check fence defect** (```-fence tokenization, medium severity, "queued with the mutation
  survivors") — no fleet row seen and it is lane-local; affects: whether the integrator wants a routed row for a
  medium-severity sibling-gate defect (I did not file one; the lane names it in its own r16 §Limits with a proposed
  fix).
- **Actor of the `~/Projects` prune regime (W1–W5)** — kasegi r15/r16 + kake r15/r16 both leave it UNDETERMINED by
  design; affects: D-135/D-150 dispositions (the loss is evidence-complete, the cause is not).
- **kasegi r16/r17 work preservation** — after R6 is filed, whether the L1 wants the dirty tree committed by the
  lane or re-derived; affects: D-144/D-145-class durability for two rounds of kasegi work (27 M paths).