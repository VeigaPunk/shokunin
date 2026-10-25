# Closure evidence sweep — lane-round band for the round-12 pass (read-only map)

Scope: read-only mapping to derive the `MANIFEST.json` `rounds[]` appends the round-12 pass owes. Nothing outside this file was written. Measurement clock 2026-09-28 20:45–20:47 -03:00; `wc -l .ufo/watchdog.log` → 201.

## Method

Band = every lane-round dispatched at/after 19:00:00 plus every older lane-round still carrying an unresolved `in-flight` row (that set is exactly one: protocol r11, launched 18:50:31). Last pass `closed_at` = 2026-09-28T20:10:00-03:00 (`rounds[19..21]`; 22 entries total).

- `grep -nE '^(2026-09-28T(19|20))' .ufo/watchdog.log | grep -E 'launch|steer|complete'` → every dispatch/termination line quoted in the table. Totals: `grep -c 'launch '` 73, `'complete '` 72, `'steer '` 15, `grep -cE 'lane-dead-no-report|launch-fail'` 0.
- `ls -la .ufo/reports/round-*/`; `git ls-files .ufo/reports`; `git ls-files -o --exclude-standard .ufo/`; `git status --short` → one report dirty (`.ufo/reports/round-13/kake.md`).
- `python3 -c "import json,collections; r=json.load(open('MANIFEST.json'))['rounds']; …"` → 22 entries, 127 `(entry,lane)` rows, 104 distinct `(lane, entry.round)` keys; both keyings below.
- Per report: byte size, `grep -cE '^#{1,6} *SHONEN'`, `git log --diff-filter=A --format='%h|%an <%ae>|%ad|%s' -1 -- <path>`, and for every hex token `git cat-file -e <h>^{commit}` + `git merge-base --is-ancestor <h> HEAD` in the cited repo.
- `cat .ufo/state/<lane>.round` → protocol 12, aggregator 8, kasegi 14, kengaku 11, kake 14, kumitate 11, kotoba 13, kagi 12.
- Live fact that changed *during* the sweep: kumitate r11 filed its report 20:45:10 (commit `46e9ec3`; HEAD moved `6d27283`→`46e9ec3`). Row 11 below is the post-landing state.

## Lane-round table

`cite` = the report's own-round child-repo commit citation (line no. in that report); ancestry re-executed in the lane's repo, not read from the report.

| lane | lr | dispatch (`launch` line, ts) | termination | report (bytes) | tracked / landing commit | cite → exists / ancestor | `SHONEN` |
|---|---|---|---|---|---|---|---|
| protocol | 11 | `launch protocol round=11 …r1790632230` 18:50:31 | `complete protocol round=11` 20:28:20 | round-11/protocol.md 29338 | yes — `392b3c7` protocol-shokunin 20:27:31 (self-landed) | `55e23de` L3 → ancestor; all 20 main-repo-resolvable cited hashes are ancestors (the other 16 hex tokens name sibling-repo commits) | 1 |
| kake | 12 | `launch kake round=12 …r1790633584` 19:13:05 | `complete kake round=12` 19:43:10 | round-12/kake.md 15348 | yes — `9af7245` operator 19:46:14 | `0262681` L177 (=r11's commit) → ancestor; own `a642f93` **uncited** | 0 |
| kagi | 11 | `launch kagi round=11 …r1790633585` 19:13:06 | `complete kagi round=11` 20:13:19 | round-11/kagi.md 10163 | yes — `029c474` operator 20:09:05 | **none**: L5 names branch `round-11`; L153-158 hexes are artifact sha256s. Own `301b9ec` exists/ancestor, uncited | 0 |
| kumitate | 10 | `launch kumitate round=10 …r1790634036` 19:20:37 | `complete kumitate round=10` 20:05:46 | round-10/kumitate.md 13507 | yes — `4f76d3b` operator 20:00:31 | `c91fe96` L6 → ancestor (child commit under operator identity) | 1 |
| aggregator | 7 | `launch aggregator round=7 …r1790634938` 19:35:39 | `complete aggregator round=7` 20:13:17 | round-7/aggregator.md 10695 | yes — `6d27283` aggregator-shokunin 20:32:43 (self-landed) | `e333e7c` L90 ancestor; `f9dcfd2` L5 ancestor | 0 |
| kotoba | 12 | `launch kotoba round=12 …r1790634939` 19:35:40 | `complete kotoba round=12` 20:28:22 | round-12/kotoba.md 14009 | **NO — untracked** | `4dd7753` L21 ancestor; own `633859f` **uncited** — L224 holds literal `LANE_HASH` | 1 |
| kake | 13 | `launch kake round=13 …r1790635390` 19:43:11 | `complete kake round=13` 20:05:45 | round-13/kake.md 5878 disk / 5739 committed | yes — `3ea42cb` protocol sweep 20:13:40, **then modified in worktree** (+3/−1) | `a642f93` L81 ancestor; own `2a5502c` **uncited** | 0 |
| kasegi | 14 | `launch kasegi round=14 …r1790635842` 19:50:43 | **live** (counter 14) | — | — | — | — |
| kengaku | 11 | `launch kengaku round=11 …r1790635843` 19:50:44 | **live** (counter 11) | round-11/kengaku-**DRAFT**.md 15922 — non-conforming name | **NO — untracked** | `0c51208` L7 ancestor; own token is an unfilled `{{HASH}}` | 0 |
| kake | 14 | `launch kake round=14 …r1790636745` 20:05:46 | **live** (counter 14) | — | — | — | — |
| kumitate | 11 | `launch kumitate round=11 …r1790636746` 20:05:47 | no `complete` line; report landed 20:45:10 = completion evidence | round-11/kumitate.md 15963 | yes — `46e9ec3` operator 20:45:10 | `23452e7` L6/L255 → ancestor; lane tree CLEAN | 1 |
| aggregator | 8 | `launch aggregator round=8 …r1790637197` 20:13:18 | **live** (counter 8) | — | — | — | — |
| kagi | 12 | `launch kagi round=12 …r1790637199` 20:13:20 | **live** (counter 12) | — | — | — | — |
| protocol | 12 | `launch protocol round=12 …r1790638100` 20:28:21 | **live** (this mission) | — | — | — | — |
| kotoba | 13 | `launch kotoba round=13 …r1790638102` 20:28:23 | **live** (counter 13) | — | — | — | — |

No dispatch fell between 19:00:00 and 19:13:05 (`sed -n '155,160p' .ufo/watchdog.log` = ticks only). Child-repo trees for terminated rounds are clean except kasegi/kake/kotoba/kagi/kengaku, whose diffs are `find … -newermt <launch-ts>`-dated after their **live** r14/r12/r13 launches — next-round work, not round debt.

## Last-wins ledger

Counting command (verbatim; `A` = the row describes lane-round `entry.round`, per PROTOCOL §step 4 "**A row names the lane-round it describes**", with `lane_rounds` the lane's *counter* recorded only where it differs):

```
python3 -c "import json,collections
r=json.load(open('MANIFEST.json'))['rounds']
A={}
for i,e in enumerate(r):
    for l,st in e.get('lanes',{}).items(): A[(l,e['round'])]=(i,st)
print(len(A), dict(collections.Counter(v[1] for v in A.values())))"
```

Observed: `104 {'ok': 73, 'failed': 4, 'in-flight': 4, 'not-dispatched': 23}` over the 127 `(entry,lane)` rows of 22 entries. This reproduces the tally `SCORECARD.md` M8 / gate-integrity already quotes (`73 ok / 4 failed / 4 in-flight / 23 not-dispatched`), so `A` is the fleet's standing convention. Tally under `A`: **ok 73 / failed 4 / in-flight 4 / not-dispatched 23**.

- `failed` (4): aggregator r1 (idx4), aggregator r5 (idx8), kagi r1 (idx4), kengaku r8 (idx11).
- `in-flight` (4) — the entire carried debt: `rounds[19]` protocol r11, kengaku r11, kumitate r11; `rounds[20]` kotoba r12.

**Schema hazard: the naive keying invents 4 contradictions.** Keying `B` (key = `lane_rounds[lane]`, which the redundant `lane_rounds == round` annotation on ok rows invites) gives `83 {'ok': 66, 'failed': 3, 'not-dispatched': 13, 'in-flight': 1}` and reads `rounds[21]`'s six `not-dispatched`/`lane_rounds` pairs as rows about lane-rounds 11/12/13/7 — flipping kagi r11 (ok), kengaku r11, kumitate r11, protocol r11 and kotoba r12 (in-flight) to `not-dispatched`, and leaving aggregator r9 stuck at `rounds[3]`'s stale `in-flight` (`rounds[12]`'s aggregator pair is keyed away to r6, where it collides with `rounds[9]`). It also drops all 7 round-2 rows (`B` = MISSING) and every `not-dispatched` row whose counter equals an already-keyed round. Do not run `B`; one round-notes line naming the hazard is warranted, since `lane_rounds` duplicating the entry round is noise that flips the reading.

## Debt

**(a) Unresolved `in-flight` rows, state now.** (1) `rounds[19]` protocol r11 — terminated: `complete protocol round=11` 20:28:20, report `392b3c7` 20:27:31 → `ok`. (2) `rounds[19]` kumitate r11 — terminated in effect: no `complete` line, but the contract-path report landed 20:45:10 (`46e9ec3`); completion evidence is the report, not the line → `ok`. (3) `rounds[19]` kengaku r11 — **live** (19:50:44, no `complete`, counter 11), no contract-path report → `in-flight`. (4) `rounds[20]` kotoba r12 — terminated: `complete kotoba round=12` 20:28:22, report untracked → `ok` + landing debt.

**(b) Status contradictions (one) and note-level contradictions (two).**
- **`rounds[10]` (round-7 entry, `closed_at` 18:21:16) `aggregator: not-dispatched`** contradicts `launch aggregator round=7 …r1790634938` 19:35:39 + `complete aggregator round=7` 20:13:17 + a report committed under lane identity `6d27283`. PROTOCOL: "No lane may be recorded `not-dispatched` while dispatch evidence for that lane-round exists." It is the only status-level contradiction among the 22 entries; the row rode no correction because the dispatch postdates the entry.
- `rounds[19]` kagi r11 note "report on disk **UNTRACKED** at `closed_at`" is false: `029c474` added it 20:09:05, ~55 s before `closed_at` 20:10:00 (`git log --diff-filter=A -1 -- .ufo/reports/round-11/kagi.md`). Status `ok` unaffected; the round-11 report §Conformance 3 corrects the phrasing but the entry text still stands and needs superseding.
- `rounds[21]` kasegi r13 note "report landed 19:44:05, committed `0933e84` 19:44:22 - 15 s BEFORE its own child commit `7483333`" is imprecise: `7483333` is 19:44:20, so the report *file* precedes it by 15 s while the report *commit* follows it by 2 s. Falsifiable as written; status unaffected.
- Recorded only to block a false accusation: `round-10/kumitate.md` L93 quotes `COMMIT_CITED_NOT_ANCESTOR … [d65aa24 31f09cd 0ac2272]` from a doctored throwaway clone at `efe19da` (its own fixture, L92-93). Re-executed in `kumitate-shokunin`: all three are ancestors of HEAD.

**(c) Lane-rounds dispatched after their own round closed, with no row anywhere** — per PROTOCOL they "ride the next closure-correction for `N` — never dropped, never folded into `N+1`": aggregator r7 (19:35:39, after the round-7 entry closed 18:21:16) holds only the contradicted row → round-7 correction, `ok`; aggregator r8 (20:13:18, after the round-8 correction closed 20:10) → round-8 correction, `in-flight`; kagi r12 (20:13:20) and protocol r12 (20:28:21), after the round-12 entry closed 20:10 → round-12 correction, `in-flight` each; kotoba r13 (20:28:23, after the round-13 entry closed 20:10) → round-13 correction, `in-flight`.

**Round-14 band ruled explicitly: no round-14 entry is warranted.** kasegi r14 (19:50:43) and kake r14 (20:05:46) were dispatched, but round 14 was never closed (no round-14 entry exists), so the ride rule does not reach them, and the trigger is "Write the entry for round `N` as soon as one lane's Nth lane-round terminates" — neither has terminated: `complete kasegi round=14` and `complete kake round=14` are absent from the log and `.ufo/reports/round-14/` is empty (`ls -la` → `total 0`). There is no `N` to write; both enter the first round-14 entry when one lands.

**(d) Non-conforming report filename.** `.ufo/reports/round-11/kengaku-DRAFT.md` is not `<id>.md`, and PROTOCOL is flat: "A report under any other name does not satisfy the contract." Its title self-identifies as a draft with `{{HASH}}` unfilled and it carries no `SHONEN` heading. Consequences: (1) kengaku r11 has no report, so it cannot be recorded `ok` on it and stays `in-flight` while live; (2) the driver's completion signal is `report_of()` = the exact contract path, so the DRAFT never advances kengaku's counter — the mission stays open until a conforming `.ufo/reports/round-11/kengaku.md` lands; (3) it is disqualified as promotion evidence in any case (`SHONEN`=0).

New debt in no entry: `.ufo/reports/round-13/kake.md` was **modified in place** after its `3ea42cb` sweep and is uncommitted — a durability gap plus an in-place rewrite of a filed report; and `.ufo/reports/round-12/kotoba.md` (14009 B) is untracked at its mission's completion, so the integrator lands it for durability (`3ea42cb` precedent) and records the landed-by-the-lane attribution defect.

## Required appends

Five `closure-correction` entries. `closed_at` = this pass's instant and MUST be ≥ `20:45:10` (kumitate r11's landing commit) — recommend `2026-09-28T20:47:00-03:00` or the actual write time. No `lane_rounds` is needed on any row below: each row's lane holds a counter equal to its entry's `round`.

1. `{round: 7, type: "closure-correction", closed_at: …, supersedes: {round: 7, type: "retroactive-closure", date: "2026-09-28"}, lanes: {aggregator: "ok"}}` — idx 10's `not-dispatched` is falsified by the 19:35:39 dispatch; terminated 20:13:17; report 10695 B, `SHONEN`=0, `e333e7c`/`f9dcfd2` ancestors, self-landed `6d27283`. Pointer: `complete aggregator round=7` 20:13:17 + `6d27283`.
2. `{round: 8, type: "closure-correction", closed_at: …, supersedes: {round: 8, type: "retroactive-closure", date: "2026-09-28"}, lanes: {aggregator: "in-flight"}}` — post-closure dispatch riding round 8, live at `closed_at`. Pointer for `notes`: `launch aggregator round=8 runId=shokunin-r8-aggregator-r1790637197` 20:13:18; counter 8; no report.
3. `{round: 11, type: "closure-correction", closed_at: …, supersedes: {round: 11, type: "closure-correction", date: "2026-09-28"}, lanes: {protocol: "ok", kumitate: "ok", kengaku: "in-flight", kagi: "ok"}}` — resolves 3 of the 4 carried `in-flight` rows; re-asserts kagi `ok` to carry the note correction from (b). Pointers: protocol `complete … round=11` 20:28:20 + `392b3c7`; kumitate report 20:45:10 + `46e9ec3` + `23452e7` ancestor; kengaku `launch … round=11 …r1790635843` 19:50:44, counter 11, no contract-path report.
4. `{round: 12, type: "closure-correction", closed_at: …, supersedes: {round: 12, type: "closure", date: "2026-09-28"}, lanes: {kotoba: "ok", kagi: "in-flight", protocol: "in-flight"}}` — kotoba r12 terminated 20:28:22, report 14009 B, `SHONEN`=1, `4dd7753` ancestor, **untracked → landed by this pass** (defects: `LANE_HASH` uncited, filed before its own `633859f`); kagi r12 (`…r1790637199` 20:13:20) and protocol r12 (`…r1790638100` 20:28:21) are post-closure dispatches, live, no report.
5. `{round: 13, type: "closure-correction", closed_at: …, supersedes: {round: 13, type: "closure", date: "2026-09-28"}, lanes: {kotoba: "in-flight"}}` — kotoba r13 (`…r1790638102` 20:28:23) rides round 13; live at `closed_at`, counter 13, no report. kasegi r13 / kake r13 rows in idx 21 need no restatement (statuses unchanged); kake's dirty report should be landed by this pass.

No `round: 14` entry. **No `not-dispatched` row appears in these five entries**, so the `lane_rounds` requirement ("required on every `not-dispatched` row") is not triggered by any of them; the six `not-dispatched` rows already in `rounds[20]`/`rounds[21]` keep their `lane_rounds` and stay true (no such lane's counter has moved).

## Gaps

- `supersedes: {round, type, date}` is not a unique key: entries 3 and 5 name a `closure-correction` target, and a second round-11 or round-13 correction written in the same pass would collide on an identical triple. The integrator must disambiguate in `notes` (index or `closed_at`); I did not verify how any consumer resolves it.
- "Live" in the table means "no `complete` line and no contract-path report". Whether kengaku r11 / aggregator r8 / kagi r12 / protocol r12 / kotoba r13 are *progressing* or *silent* per the stale-lane actuator is not fully resolved: I probed file mtimes per repo, not the full per-lane `find <repo> -newermt <launch-ts> -type f -not -path '*/.git/*'` sweep that the actuator names.
- `d7dbd9a` (kasegi r13) and `e66e614` (kengaku r10) stay unresolvable in every local object database; whether they exist in un-fetched remotes is unknowable here (read-only surfaces, no fetch).
- Whether the driver's next tick `complete`s `kumitate round=11` on the evidence measured above, and whether the live in-flight missions terminate before this pass closes, are timing facts a read-only vantage cannot pin.