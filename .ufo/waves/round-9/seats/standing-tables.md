# Round-9 seat evidence — `StandingTables` (L2, aggregator lane)

**Assignment.** Re-run `AGGREGATE.md` §12.1 (7 dormancy rows), §12.2 (5 mint/watchlist rows) and the §12.5 /
§13.6 re-run blocks R0–R5 + K/S/U/G/A **in-refresh**, reporting each row's observed cell against its stamped cell
(`unchanged` / `moved` / `unrunnable-on-this-host`), deriving dormancy rather than asserting it, testing the kama
L0 line for byte-identity, and reporting `minted` over every `rounds` entry.

**Authorship note (seat contract rule 7).** This seat is aggregator-lane. Every row I re-run is authored by the
lane I belong to, so this is an **author-side re-run**, not a non-author audit; the non-author audit of the
aggregator's own artifacts was `.ufo/reports/round-8/aggregator.md` §13.5 (reviewer/critic seats).

## Measurement stamp (cells below name the revision they were measured against)

| Field | Value |
|---|---|
| Wall window | `2026-09-29T00:45:54Z` (first command) → `2026-09-29T00:51:38Z` (final stamp), local `-0300` |
| Main HEAD at final stamp | `383ea1a` `2026-09-28T21:51:23-03:00` (`git log -1 --format='%h %aI %an'`) |
| Main HEAD drift observed **in this session** | `91d0178` (task text) → `1dc7f6b` → `62fdfbe` (L1 amendment 1) → `a197445` → `383ea1a`. Every §-table cell below is a claim about *the revision named in its own command's output*, and the fleet committed ~1 commit/minute across the window. |
| Child HEADs used (final) | kasegi `b7180b0` (dirty 7) · kengaku `f09ff1f` (dirty 2) · kake `a209441` (clean) · kumitate `7a099b2` (clean; `e0e5de1` earlier in-session) · kotoba `63ceba7` (clean) · kagi `4b8c018` (clean; `4391b3b` earlier in-session) |
| Counters `cat .ufo/state/<lane>.round` | kasegi 15 · kengaku 12 · kake 15 · kumitate 13 · kotoba 15 · kagi 13 · aggregator 9 · protocol 12 |
| Host caveat | `grep` is pi-uu-grep 0.2.0; `grep -oE '[0-9]+$'` emits zero-length matches — re-verified below (§R4). |

Per the seat contract's dirty-tree rule (round-8 critic ruling), `kasegi` and `kengaku` carry live missions
(r15 / r12) and their worktree deltas are marked **provisional**; every box-3 or corpus cell for them is read at
the landed HEAD (`git show <HEAD>:<path>`), never the worktree.

---

## 1. §12.1 standing dormancy table — re-run (7 rows)

§12.1 stamped its cells at cutoff `2026-09-28T22:55:03Z`, HEAD `f9dcfd2`. Cells below are the **observed** values
from R1/R2/R3/R5 (§2), stamped at `2026-09-29T00:45–00:51Z` / child HEADs as listed.

| Lane | Counter stamped → obs | Last dispatched stamped → obs | Last report landed stamped → obs | Newest `round[- ]N` in `LOG.md` stamped → obs | Last lane-authored commit stamped → obs | Dormancy verdict |
|---|---|---|---|---|---|---|
| kasegi | 14 → **15** | r14 @19:50:43 → **r15 @20:50:55** | r13 9964 B → **r14 7338 B** | round 13 → **round 14** | `7483333` 11m → **`b7180b0` 58m** | **ACTIVE** — pair r13+r14, LOG carries both (`— round 12/13/14`) |
| kengaku | 11 → **12** | r11 @19:50:44 → **r12 @21:21:48** | r10 13160 B → **r11 18585 B** (landed `e0170cd` 21:18:11) | round 10 → **round 11** | `0c51208` 12m → **`f09ff1f` 31m** | **ACTIVE** — pair r10+r11, LOG carries `— round 9/10/11` |
| kake | 13 → **15** | r13 → **r15 @21:44:25** | r12 15348 B → **r14 10417 B** (r13 5878 B also on disk) | round 12 → **round 14** | `a642f93` 9m → **`a209441` 4m** | **ACTIVE** — pair r13+r14, LOG carries both |
| kumitate | 10 → **13** | r10 → **r13 @21:21:51** | r9 → **r13 16347 B** (landed `a197445` 21:49:18) | round 9 → **round 13** | `d65aa24` 45m → **`7a099b2` 4m** | **ACTIVE** — pair r12+r13, LOG carries `— round 11/12/13` |
| kotoba | 12 → **15** | r12 → **r15 @21:36:53** | r11 → **r14 9463 B** — **untracked** on disk | round 11 → **## Round 13** | `7d15407` 8m → **`63ceba7` 2m** | **ACTIVE** — pair r13+r14; r14 report durability defect (§5) |
| kagi | 11 → **13** | r11 → **r13 @21:06:34** | r10 7178 B → **r12 13620 B** — **untracked** | round 10 → **round 13** | `03477c0` 46m → **`301b9ec` 2h** | **ACTIVE** — pair r11+r12, LOG carries `— round 11/12/13` |
| aggregator | 7 → **9** | r7 @19:35:39 → **r9 @21:14:10** | r6 15931 B → **r8 24058 B** | Round 6 (`LOG.md:62`) → **Round 8** (`LOG.md:213`) | `e333e7c` 27m → **`a5d6a7e` 38m** (last aggregator-authored) | **ACTIVE** — pair r7+r8 |

**All 7 rows moved.** Counters advanced +1…+5 per lane; 5 of 7 report cells advanced; every LOG cell advanced
except the aggregator's pair (r9's LOG entry is pending this round).

### 1.1 Dormancy derived, not asserted

Rule (`PROTOCOL.md` "Promotion gates" preamble, quoted in §12.1): a shonen records no `LOG.md` activity across
**two consecutive rounds it was dispatched and reported in**. Marker grading: a filed report recording no lane
work is a *marker* (excluded); a short report naming a real committed hash is a *defective report* that counts.

Derivation command (rounds dispatched ∩ rounds reported, consecutive pairs):

```sh
python3 - <<'PY'
import os,re,glob,collections
rep=collections.defaultdict(set)
for p in glob.glob('.ufo/reports/round-*/*.md'):
    rep[os.path.basename(p)[:-3]].add(int(re.search(r'round-(\d+)/',p).group(1)))
disp=collections.defaultdict(set)
for line in open('.ufo/watchdog.log',errors='ignore'):
    f=line.split()
    if len(f)>=4 and f[1]=='launch':
        m=re.match(r'round=(\d+)',f[3])
        if m: disp[f[2]].add(int(m.group(1)))
for l in ['kasegi','kengaku','kake','kumitate','kotoba','kagi','aggregator']:
    both=sorted(rep[l]&disp[l]); pairs=[(a,b) for a,b in zip(both,both[1:]) if b==a+1]
    print(l, 'both=',both,'consec=',pairs[-3:])
PY
```

Observed:

```
kasegi     both=[4..14]  consec=[(11,12),(12,13),(13,14)]
kengaku    both=[4..11]  consec=[(8,9),(9,10),(10,11)]
kake       both=[4..14]  consec=[(11,12),(12,13),(13,14)]
kumitate   both=[4..13]  consec=[(10,11),(11,12),(12,13)]
kotoba     both=[4..14]  consec=[(11,12),(12,13),(13,14)]
kagi       both=[3..12]  consec=[(9,10),(10,11),(11,12)]
aggregator both=[4..8]   consec=[(5,6),(6,7),(7,8)]
```

Marker ledger re-measured (only four marker-sized reports exist fleet-wide; none in rounds 9–15):

```sh
for f in .ufo/reports/round-{8,9,10,11,12,13,14,15}/*.md; do b=$(wc -c <"$f"); [ "$b" -le 300 ] && printf '%6s B %s\n' "$b" "$f"; done
```
```
   101 B .ufo/reports/round-8/kengaku.md     (no commit → failed, excluded)
   120 B .ufo/reports/round-8/kotoba.md      (`8c300ad` resolves → ok+defect, counted)
   122 B .ufo/reports/round-7/kumitate.md    (`7a4c9a0` resolves → ok+defect, counted)
   254 B .ufo/reports/round-5/aggregator.md  (no commit → failed, excluded)
```
All other reports in rounds 8–14 are ≥ 2357 B. So no `ok`-graded pair in any lane is broken by a marker.

**Dormant count: 0 / 7 — derived, not asserted.** Each lane's last two dispatched-and-reported rounds are
consecutive and each carries a durable report ≥ 2357 B plus a consecutive `LOG.md` entry pair.
**Positive dormancy case: NO** — the dormancy rule is still untested in the one direction that matters
(7th consecutive refresh at 0/7; §12.6 residual gap stands, unbroken).

Nearest watch row: **kotoba**, whose r14 report (`9463 B`) is real but **untracked** while its counter reads 15;
and **kagi/kasegi**, whose untracked reports do not affect dormancy (§5). kengaku's round-8 §13.3 watch row is now
**closed**: its r11 report exists at the contract path and is tracked (`e0170cd`) — D-90's core defect is
repaired (residue: the two round-12 evidence dirs are untracked and the r11 report carries one literal `{{}}`
which is a narrative reference to its own draft skeleton, not an unfilled token).

---

## 2. §12.5 / §13.6 re-run blocks — executed row by row

`grep` on this host is pi-uu-grep 0.2.0. Every block below was executed in this session; "stamped cell" = the
value in §12.1/§12.2/§13.3; "observed" = this session's output.

| Block | Row | Stamped cell | Observed (this session) | Verdict |
|---|---|---|---|---|
| **R0** | main HEAD | `f9dcfd2` @22:55:03Z (§12.5) / `46e9ec3` @23:46:28Z (§13) | `1dc7f6b` → … → `383ea1a` @00:51:38Z | **moved** (fleet committing ~1/min) |
| **R1** | counters | 14/11/13/10/12/11/7 | **15/12/15/13/15/13/9** | **moved** (all 7) |
| **R2** | last launch | kasegi r14, kengaku r11, kake r13, kumitate r10, kotoba r12, kagi r11, agg r7 | **kasegi r15 @20:50:55, kengaku r12 @21:21:48, kake r15 @21:44:25, kumitate r13 @21:21:51, kotoba r15 @21:36:53, kagi r13 @21:06:34, agg r9 @21:14:10** | **moved** (all 7) |
| **R3** | newest report per lane | kasegi r13 9964 B, kengaku r10 13160 B, kake r12 15348 B, kumitate r9, kotoba r11 12397 B, kagi r10 7178 B, agg r6 15931 B | **kasegi r14 7338 B, kengaku r11 18585 B, kake r14 10417 B, kumitate r13 16347 B, kotoba r14 9463 B, kagi r12 13620 B, agg r8 24058 B** | **moved** (all 7) |
| **R3** | marker ledger | 101/120/122/254 B | **101/120/122/254 B** | **unchanged** |
| **R4** | LOG token scan `grep -oiE 'round[- ]+[0-9]+' \| grep -oE '[0-9]+$'` | kotoba `round-9`-class drift | **empty for all six lanes** (`token-scan=''`) | **unrunnable-on-this-host** — pi-uu-grep emits zero-length matches for the anchored `-oE '[0-9]+$'`; reproduced `printf 'abc 123\n' \| grep -oE '[0-9]+$' \| od -c` → `\n`. Confirms §13.5 item 14. §13.6-R's entry-scan form **is** runnable. |
| **R4** | LOG entry scan `grep -oE '^## Round [0-9]+\|— round [0-9]+' \| tail -1` | kasegi r13, kengaku r10, kake r12, kumitate r9, kotoba Round 11, kagi r11 | **kasegi `— round 14`, kengaku `— round 11`, kake `— round 14`, kumitate `— round 13`, kotoba `## Round 13`, kagi `— round 13`** | **moved** (all 6) |
| **R4** | aggregator LOG `^#{2,3} Round [0-9]+ — aggregator` | `LOG.md:115` Round 7 | **`LOG.md:115` Round 7, `:213` Round 8** | **moved** (Round 8 landed); no Round 9 entry yet |
| **R4** | marker-hash resolvability | `8c300ad`, `7a4c9a0` resolve | **both `commit`** | **unchanged** |
| **R5** | lane-authored commit age (`--perl-regexp --author='^(?!aggregator-shokunin)'`) | kasegi `7483333` 11m, kengaku `0c51208` 12m, kake `a642f93` 9m, kumitate `d65aa24` 45m, kotoba `7d15407` 8m, kagi `03477c0` 46m | **kasegi `b7180b0` 58m, kengaku `f09ff1f` 31m, kake `a209441` 4m, kumitate `7a099b2` 4m, kotoba `63ceba7` 2m, kagi `301b9ec` 2h** | **moved** (all 6) — and the filter **works**: unfiltered kagi HEAD is `4b8c018` (operator identity), filtered is `301b9ec`. |
| **R5** | aggregator last-authored | `e333e7c` 27m | **`a5d6a7e` 21:13:01 -03, 38m** (main HEAD is shared: `383ea1a`, author `Joao Pedro Veiga`) | **moved** |
| **K** | 34113 health | `{"status":"ok"}` | **`{"status":"ok"} HTTP:200`** | **unchanged** |
| **K** | 8080/v1/models | `404` | **`8080=404`** | **unchanged** |
| **K** | config baseURLs | janitor `:16` → `127.0.0.1:8080/v1`; opencode `:158` → `localhost:8080/v1` | **identical** (`~/.config/the-janitor/opencode.json:16`, `~/.config/opencode/opencode.json:158`) | **unchanged** — D-85 drift persists |
| **K** | kama L0 line vs `e333e7c` | `kama-line-UNANSWERED` | **`kama-line-UNANSWERED`** (md5 `643e7114dd5f9286cdf27a4a654bc800` for `e333e7c` line 2, HEAD line 2, worktree line 2) | **unchanged** |
| **K** | `minted` over `rounds` | 0 over 22 (§13.3) | **0 over 36** (see §3) | **moved** (entry count), minted constant |
| **K** | kama ancestors | `06ef644`, `a1af83c` | **both `merge-base --is-ancestor … → OK`, `cat-file -t` → `commit`** | **unchanged** |
| **S** | 6-artifact list | all exist | **all 6 exist (exit 0)** | **unchanged** |
| **S** | extended list (round-gate, claim-ledger, kotoba `verifiers/*.py`) | per §13.6 | **10 files exist (exit 0)** — kotoba now has 4 `.py` + `fault_injection_corpus.sh`, kumitate 4 scripts, kagi 2 (claim-ledger, drift-pins) | **moved** (kotoba grew: `verify_surfaces.py` @ `5cc1340`, `verify_corpus_independent.py`) |
| **S** | `no sibling owns` in kengaku r10 | present | not re-run in-scope (sibling seats) — §12.2's kessho ruling retained | n/a |
| **U/G** | `grep -rn -i 'umihotaru\|kagemusha' .ufo/reports/round-{9..13}/` | `exit 1` | **`exit 1`** (rounds 9–13) | **unchanged** — 0 new instances |
| **U/G** | same over **all** rounds | not run in §12.5 | 5 hits, **all inside aggregator-authored reports** (`round-6/protocol.md:88-89`, `round-7/aggregator.md:31,57-58,76`) = self-references, no new demand | **unchanged** |
| **A** | `grep -rn -i -e axis-framework -e stewardship .ufo/reports/round-1[1-9]/` | `exit 1` (§13.3 discharged) | **`exit 1`** | **unchanged / discharged** |
| **A** | same over all rounds | — | 12 matches: `AGGREGATE.md` self-references + `round-10/protocol.md:380` (the known incidental census, adoption 2/6) + `round-6/aggregator.md:123`, `round-7/aggregator.md:31,57`, `round-8/aggregator.md:133` — **no new demand** | **unchanged** |
| **B** | box-3 operative grade per lane | 4 `[x]` / 2 `[~]` / 0 `[ ]` (§13.1) | **kasegi `[~]`, kengaku `[x]`, kake `[x]`, kumitate `[ ]`(tail-match)/`[x]`(operative block), kotoba `[~]`, kagi `[x]`** — set is **4 `[x]` / 2 `[~]`** on the operative blocks | **set unchanged**, but the **resolver rule is broken** (§4) |
| **B2** | provisional markers | kasegi/kumitate "provisional until the lane commits", kagi "remains provisional", kengaku/kotoba "not provisional", kake none | **identical** at fresh HEADs | **unchanged** |
| **B2** | kumitate proxy re-execution | `PROXY: MATCH`, exit 0 | **`PROXY: MATCH (A=4 C=9 operability=8; C1=18/19 C2=45/45 coverage=9; pins=4 match)` `exit=0`** (values differ from the round-8 cell `C1=14/18 C2=39/39 coverage=7` because the lane's cite-check grew) | **moved** (numbers), verdict constant |
| **W** | untracked reports/prompts | `round-11/kengaku-DRAFT.md`, `round-12/kotoba.md` (D-90/D-91) | **`round-12/kagi.md`, `round-12/kotoba.md`, `round-14/kotoba.md`** (+ 2 `.ufo/prompts/*-round-15.md`); **`round-11/kengaku-DRAFT.md` is gone** | **moved** — D-90 resolved, D-91 persistent |
| **W** | highest `D-` key | D-120 (next free D-87 at refresh 6) | **D-120 → next free D-121** | **unchanged** since refresh 6 |
| **Q** | `grep -c 'PROTOCOL\.md:[0-9]' AGGREGATE.md` | target 0 (P-p) | **0** | **unchanged** |

**Unrunnable-on-this-host: exactly one row** — §12.5-R4's token scan (host-broken, above). Everything else in
§12.5 and §13.6 executed and reproduced its own cell shape (§13.6's corrections all hold: the 8080 pointer is
`~/.config/opencode/opencode.json:158`, and the entry-scan form is host-independent).

---

## 3. `minted` over every `rounds` entry

```sh
python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print(len(r),'rounds;',sum(1 for x in r if x.get('minted')),'minted')"
```
`36 rounds; 0 minted` — values array is `[None, [], None, [], …]`: 2 entries carry an empty list `[]`, 34 carry
`None` (absent key), **0 truthy**.

**Moved:** §13.3 stamped "0 over **22** entries"; the task text said 30; observed **36**. `minted` is constant at
**0** (M2 stands and is correct — the bar is met only by kama and the ruling is operator-side).

---

## 4. Findings

### F1 — §13.6-B's operative-grade resolver mis-resolves kumitate to the **withdrawn** mark (sev 3, rule `gate`/P-q)
§13.6-B defines "operative grade = **LAST** match" of `grep -oE '\*\*\[[x~ ]\]\*\*' "$f" | tail -1` (D-110).
Re-run:

```sh
grep -nE '\*\*\[[x~ ]\]\*\*' kumitate-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md
```
```
36:**[ ]** — decided by: command table rows 1+8+10, i.e. `node scripts/proxy-check.mjs` …exit 1 `PROXY: DRIFT (A_DRIFT …)`
121:The `## Box-3 verdict` line above reads `**[ ]**` and is **WITHDRAWN** by `## Round-8 amendment
```
Only two bold grade marks exist; the later (line 121) is the **withdrawn** mark quoted *inside prose*, so
`tail -1` returns `[ ]` — the opposite of the file's last-section operative block, which reads
"**Operative box-3 grade: `[x]` — non-provisional at `59e6c0c`**". A rule that resolves grades tail-anchored
still fails on this file because the last *mark* is not the last *verdict*. Impact: any consumer of §13.6-B
(routed with D-110) will read kumitate `[ ]`. kumitate's live tree is also dirty in-session (`e0e5de1` dirty 7),
so this file is being edited again.

### F2 — §13.3's kessho builder cell is a count without its command, and is not reproducible (sev 3, rule 4)
§13.3 stamped "**6 lanes / 9 artifacts** (was 5/6)". Re-derivation with an explicit rule — *tracked executable
verification/gate harness* under `scripts/`, `verifiers/`, or `corpus/*.{sh,tsv}`:

```sh
for d in kengaku kake kumitate kotoba kagi; do git -C $d-shokunin ls-files | grep -E '(^|/)(scripts|verifiers)/.*\.(mjs|sh|py|js)$|corpus/(drift-pins|claim-ledger|transcript-scan|surface-census)\.sh$|^grader\.py$'; done
```
- kengaku **1** (`grader.py`) · kake **1** (`scripts/probe-delta.mjs`) · kumitate **4** (`cite-check.mjs`,
  `proxy-check.mjs`, `round-gate.mjs`, `surface-probe.mjs`) · kotoba **5** (`verify_harness_claims.py`,
  `verify_corpus_integrity.py`, `verify_corpus_independent.py`, `verify_surfaces.py`,
  `fault_injection_corpus.sh`) · kagi **4** (`claim-ledger.sh`, `drift-pins.sh`, `surface-census.sh`,
  `transcript-scan.sh`) · **kasegi 0** (`git -C kasegi-shokunin ls-files ops/` → empty; its whole `ops/` harness
  set is untracked — see F3).
- **Total: 5 lanes / 15 tracked harnesses.** Restricting to §13.6-S's canonical nine files gives **5 lanes /
  9 artifacts**. §13.3's own artifact list names five lanes (kumitate, kagi, kake, kotoba, kengaku); the sixth
  lane is unaccounted for. **Unreproducible as written**; the trigger itself needs no repair (builder count only
  grows), but the cell violates CORPUS rule 4.

### F3 — kasegi's box-3 verdict is decided by scripts that are **absent from the landed tree** (sev 4, `box-3`)
kasegi's box-3 verdict (§13.1) rested on `node ops/ev-report.mjs` → exit 0 where `SKILL.md:588` documents exit 2,
and `node ops/check-freshness.mjs` → exit 0 where `SKILL.md:113-114` documents exit 1. At kasegi's landed HEAD:

```sh
git -C kasegi-shokunin cat-file -e b7180b0:ops/ev-report.mjs
```
```
fatal: path 'ops/ev-report.mjs' does not exist in 'b7180b0'   (exit 128)
```
`git -C kasegi-shokunin ls-files ops/` → empty. **The decisive scripts are worktree-only**, while the lane's r15
mission is live (`dirty 7`). PROTOCOL.md §Gate standard: *"A verdict names the revision it was measured
against … a run over a moving worktree is not comparable to one over the cited commit."* kasegi's `[~]`
therefore **stays provisional** — it cannot be firmed or broken by any non-author at the landed revision until
the harness lands. This is the single most decision-relevant cell for the round-9 move (c).

### F4 — reference assembly: what firmed / stays provisional for the three round-8 provisional verdicts (sev 2, `box-3`)
- **kasegi** `[~]` — **stays provisional** (F3: harness untracked at HEAD; dirty 7).
- **kake** `[x]` — **firmable**: `git -C kake-shokunin status --porcelain | wc -l` → **0** at `a209441`
  (the round-8 seat graded HEAD `2a5502c` with worktree deltas; `git diff --stat 2a5502c a209441 -- SKILL.md` →
  `13 ++++++++---`, 10 insertions / 3 deletions — the lane's r14 commit landed the graded rows). Its own lesson
  carries **no** provisional marker, so the aggregator-side "provisional" tag is the only one to lift.
- **kagi** `[x]` — **stays provisional**: its own lesson still reads "remains provisional" (`grep -oiE …` →
  `remains provisional`) and the lane's HEAD moved `4391b3b` → `4b8c018` (r13 in-session, clean).
- **kumitate** `[x]` — non-provisional at `59e6c0c` per the file's own operative block; re-execution
  `node scripts/proxy-check.mjs` → `PROXY: MATCH … exit=0` on a clean tree (`7a099b2`).
- **kengaku** `[x]`, **kotoba** `[~]` — unchanged, not provisional.
Operative grade set: **4 `[x]` / 2 `[~]`** — unchanged from §13.1.

### F5 — kama row: unchanged, still `blocked-external`, never re-flagged (sev 1, `queue`/`l0`)
- Bar test: 2 documented unplaceable instances, both ancestors at current HEADs —
  `git -C kagi-shokunin merge-base --is-ancestor 06ef644 HEAD` → **OK**;
  `git -C kengaku-shokunin merge-base --is-ancestor a1af83c HEAD` → **OK**.
- Unplaceable test: `grep -il 'model serving\|endpoint health' *-shokunin/PROVINCE.md` → **exit 1** (0 owners).
- L0 line byte-identity: `sed -n '2p' .ufo/l0-questions.md` vs `git show e333e7c:.ufo/l0-questions.md | sed -n '2p'`
  → **diff empty** → `kama-line-UNANSWERED`; md5 of the line is `643e7114dd5f9286cdf27a4a654bc800` in `e333e7c`,
  in HEAD, and in the worktree. **Unanswered ⇒ the row stays `blocked-external` and is never re-flagged as new.**
- Live drift persists (D-85/D-39): `127.0.0.1:34113/health` → `{"status":"ok"} HTTP:200`;
  `localhost:8080/v1/models` → `404`; both configs still pin 8080.

### F6 — `minted` = 0 over 36 `rounds` entries (sev 1, rule 4)
See §3. The entry count itself moved 22 → 30 → 36 across refreshes; `minted` constant 0.

### F7 — report durability: three filed reports are untracked while their lanes are active (sev 5, `gate`)
```sh
git ls-files -o --exclude-standard .ufo/reports .ufo/prompts
```
```
.ufo/prompts/kake-round-15.md
.ufo/prompts/kotoba-round-15.md
.ufo/reports/round-12/kagi.md
.ufo/reports/round-12/kotoba.md
.ufo/reports/round-14/kotoba.md
```
`git log --diff-filter=A … -- .ufo/reports/round-12/kagi.md` and `… round-14/kotoba.md` → **empty (never
committed)**. kotoba's counter reads 15 and its r15 report is not yet on disk; its r12 and r14 reports exist
only as worktree bytes. D-91's class (a filed report that is not durable) is **persistent and growing**:
2 kotoba reports + 1 kagi report now. Note kagi's `round-11/kagi.md` (10163 B) *is* tracked.

### F8 — rule-8 literal grading (per L1 amendment 2) — FAIL-literal / PASS-intent, 6/6 (sev 3, `secrets`)
Measured on the **landed** corpus (`git -C <repo> grep 'op://' <HEAD> -- corpus/`), never the worktree:

| Lane | HEAD | `op://` lines | `op://` occurrences | classes present (all classified) | other secret classes | grade |
|---|---|---|---|---|---|---|
| kasegi | `b7180b0` | 2 | 2 | 2 prose (aggregator-authored lessons quoting the sweep) | 0 | **FAIL-literal / PASS-intent** |
| kengaku | `f09ff1f` | 1 | 1 | 1 prose (sweep command quoted) | 0 | **FAIL-literal / PASS-intent** |
| kake | `a209441` | 2 | 2 | 2 prose/pattern (lessons) | 0 | **FAIL-literal / PASS-intent** |
| kumitate | `7a099b2` | 1 | 1 | 1 prose | 0 | **FAIL-literal / PASS-intent** |
| kotoba | `63ceba7` | 3 | 3 | 3 prose/surface-description | 0 | **FAIL-literal / PASS-intent** |
| kagi | `4b8c018` | 53 | 54 | all schematic (`op://vault/item/field`, `KEY=op://…`), class prose, or **fake fixtures** (`FAKE_REF=op://FakeVault/FakeItem/F3` in `surface-census.sh:608`; `fake op://vault/item/field marker` in `transcript-scan.sh:202`; `fake op://wal/resident` `:242`) | `xox[abp]-` 3 (the pattern list in `transcript-scan.sh:88`), `Bearer` 3 (`jt-test-pw`, `pw` — test strings), `token=` 2 (shell locals in `surface-census.sh:748,755`), `sk-`/`ghp_`/`password=`/private-key **0** | **FAIL-literal / PASS-intent** |

No **real vault path** (a resolvable item/field pair) appears in any landed corpus; **no secret value was
printed** — file:line and at most a 4-byte class marker only. Per the literal text of rule 8
(`CORPUS.md:43-46`), every literal `op://` string is a violation ⇒ **6/6 FAIL-literal**; per the round-6
interpretation (§11.1: "placeholders are prose") ⇒ **6/6 PASS-intent**. The conflict is routed as a row (D-

- **Reconciliation with `SentinelSeat`'s early stamp** (landed-corpus counts 2/1/2/1/3/**55**): I measure
  `kasegi 2, kengaku 1, kake 2, kumitate 1, kotoba 3` — **agree**; kagi I measure **54 occurrences / 53 lines**
  vs SentinelSeat's **55**. **Named disagreement, kagi Δ1** — most likely a worktree-vs-`git show` read (kagi
  moved `4391b3b` → `4b8c018` mid-session) or a line-vs-occurrence unit difference; both readings are far above
  zero and both are schematic-only, so the grade is unaffected. I did not re-derive SentinelSeat's other classes;
  my independent kagi classes (`xox` 3 / `Bearer` 3 / `token=` 2) match its report that they exist.

### F9 — §12.5's "copy-paste runnable" label was false for exactly one command (sev 2, P-q) — reconfirmed
See §2 / §R4: the token scan is empty for all six lanes on this host. §13.5 item 14 already recorded this;
this session re-confirms it and confirms §13.6-R's replacement form runs.

---

## 5. Candidate ledger rows (`d_rows`; the distiller assigns `D-` keys)

| owner | sev | claim | evidence | command |
|---|---|---|---|---|
| aggregator | 3 | §13.6-B's tail-anchored grade resolver returns kumitate's *withdrawn* `[ ]` (last bold mark is the withdrawal quoted in prose at `:121`), contradicting the file's own operative block `[x]` — D-110's rule is insufficient | `grep -nE '\*\*\[[x~ ]\]\*\*' kumitate-shokunin/corpus/lessons/round-8-aggregator-box3-coldrun.md` → only `:36 [ ]` and `:121 [ ]`(quoted) | as shown |
| aggregator | 3 | §13.3's kessho cell "6 lanes / 9 artifacts" carries no command and names only five lanes; re-derivation gives 5 lanes / 15 tracked harnesses (5 / 9 on the §13.6-S canonical subset) | kengaku 1, kake 1, kumitate 4, kotoba 5, kagi 4, kasegi 0 tracked; canonical subset = 9 files | `for d in kengaku kake kumitate kotoba kagi; do git -C $d-shokunin ls-files \| grep -E '(^\|/)(scripts\|verifiers)/.*\.(mjs\|sh\|py\|js)$\|^grader\.py$'; done` |
| kasegi | 4 | kasegi's box-3 verdict is decided by `ops/ev-report.mjs` / `ops/check-freshness.mjs`, **absent from the landed tree**; the verdict measures a worktree, contra PROTOCOL §Gate standard "a verdict names the revision it was measured against" | `git -C kasegi-shokunin cat-file -e b7180b0:ops/ev-report.mjs` → `fatal … does not exist` (128); `git -C kasegi-shokunin ls-files ops/` → empty; HEAD `b7180b0` dirty 7 | as shown |
| kotoba | 5 | two kotoba reports (`round-12/kotoba.md`, `round-14/kotoba.md`) exist on disk but were never committed while the counter reads 15 | `git ls-files -o --exclude-standard .ufo/reports` lists both; `git log --diff-filter=A … -- <path>` → empty | as shown |
| kagi | 4 | `round-12/kagi.md` (13620 B) exists on disk but was never committed; the lane's r12 report is off-tree | same command; kagi HEAD `4b8c018` clean while the report is untracked | as shown |
| operator | 3 | rule 8's literal text ("vault ref paths (`op://…`) stay out of every corpus") is violated by 6/6 landed corpora (0 real paths; all schematic/prose/fake fixtures), so either the rule means what it says (6 fails) or it needs an amendment distinguishing a secret value from a pointer to one | landed-HEAD `op://` counts 2/1/2/1/3/53 lines (54 occ); classification table §F8 | `git -C <repo> grep -c 'op://' <HEAD> -- corpus/` |

---

## 6. Blockers / gates

- **`gated-without-artifact`**: none required. All §12.5/§13.6 rows ran; the only failure is a host-broken
  `grep` form (unrunnable, replaced by a runnable equivalent), not a host verb gate.
- **Provisional cells**: every `kasegi` and `kengaku` cell is read from the landed HEAD; their worktree deltas
  (kasegi dirty 7, kengaku dirty 2, both with live missions) would change the `dirty` column only, and are
  marked provisional. `kumitate` and `kagi` HEADs moved **inside this session** (`e0e5de1`→`7a099b2`,
  `4391b3b`→`4b8c018`); the cells above name the revision each was measured at.
- **Known blocker for the round-9 move**: the three provisional box-3 verdicts cannot all be firmed — kasegi's
  decisive text is not in its landed tree at all (F3), so box 3 for kasegi is un-re-runnable by a non-author
  until the lane commits `ops/`.
- **Method caveat**: the fleet committed ~1 commit/minute during this window (main HEAD `1dc7f6b` → `383ea1a`
  in ~6 minutes). Any cell here is a claim about its named revision; re-run §13.6 rather than quoting this file.