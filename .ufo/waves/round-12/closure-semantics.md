# Recovered closure semantics — what rounds 10/11 actually did, as an implementable spec (revenger seat)

Re-executed this session: `python3 -m json.tool MANIFEST.json` → `JSON_VALID`, 22 entries; `git show --stat 3ea42cb|6bd4f38|55e23de|392b3c7` → 30/1/2/1 files; `git show 3ea42cb -- MANIFEST.json` → +7 entries, nothing else; `wc -l .ufo/watchdog.log` → 200; `cat .ufo/state/kagi.round .ufo/state/aggregator.round` → `12 8`. `rounds[i]` = MANIFEST index; `P:n` = PROTOCOL.md line; `r10:n`/`r11:n` = the two protocol reports.

## Observed procedure

**Round 10** (commits `640a4c5`,`43342dd`,`8e32ae0`; report `.ufo/reports/round-10/protocol.md`):
1. Froze one instant for all 11 appended entries: "`closed_at` = `2026-09-28T18:21:16-03:00` … an entry freezes at `closed_at` and later terminations ride the next pass" (r10:43-44).
2. Dispatch lines extracted from tracked `.ufo/watchdog.log` and quoted by timestamp+text into §Dispatch digest (r10:75-104); line numbers distrusted — "`complete kagi round=8` read at line 124 then 135" (r10:77-78); absence proven by history, not filesystem: `git log --all --diff-filter=D -- '.ufo/prompts/*round-2*'` → 0 (r10:109); `grep -cE 'lane-dead-no-report|launch-fail'` → 0 (r10:103).
3. `not-dispatched` = no dispatch line for that lane-round as of the freeze; `lane_rounds` = counter the lane actually held at `closed_at` (r10:55-56 table; live `rounds[13]` aggregator nd/6, `rounds[14]` 7 lanes with counters 6–10). [INFERENCE] read from `.ufo/state/<lane>.round` — r10 never names the command; values cross-check against launch lines.
4. Last-wins: "last-wins over `rounds[].lanes` → 54 `ok` + 4 `failed`; 58 = 66 dispatched − 8 live at `closed_at`" (r10:26, M2).
5. Marker grading by size + claim falsification: kengaku r8 101 B "work pushed" vs HEAD `f147a27` "round-7" → `failed`; kotoba/kumitate markers naming `8c300ad`/`7a4c9a0` → `ok` + minimum-content defect (r10:113-119, M4 r10:28).
6. Verification targeted discovered contradictions, not yet per-report step-1: round-9 rows 6/8 wrong, round-1 2/8; attribution census `git log --diff-filter=A --format='%an <%ae>'` per report (r10:127-131); liveness probe re-run → rule "`in-flight` is decided from the absence of both a `complete` line and a report" (r10:139-145); prompt fidelity 1/5 items (r10:161-165). Retroactive entries typed with "presence-of-evidence only; step-1 verification did not run" notes (`rounds[6..11]`).
7. Self-check: "`python3 -m json.tool MANIFEST.json` → valid; 15 entries; `rounds[1]` is still the round-1 `work` entry" (r10:62-64); 7 in-flight + post-freeze terminations tabled as round-11 debt (r10:287-301).

**Round 11** (`3ea42cb` closure 20:13:40 → `6bd4f38` compaction 20:15:40 → `55e23de`; report `.ufo/reports/round-11/protocol.md`):
1. Evidence first, as committed artifacts: `scout-closure.md` 19:02 (six reports: size/mtime; `grep -c '^#\{1,6\} *SHONEN'`; tokens via `grep -oE '[0-9a-f]{7,40}'` with 64-hex recombination; per token `git -C <repo> cat-file -t` + `merge-base --is-ancestor <tok> HEAD; echo exit=$?` across 13 repos; add-commit identity), `verify2.md` (seven newest terminations: same + `ls-files --error-unmatch` tracked status, /tmp pointer sweep, ordering = report-mtime − own-commit-time in epoch s), `stale2.md` 19:49 (live-set = launch lines minus `complete` greps → "0 matches").
2. Froze `closed_at` 20:10:00 for all 7 entries `rounds[15..21]` (r11:81-82).
3. Resolved all 7 carried in-flight rows via `closure-correction` entries carrying `supersedes` (observed live on `rounds[15..19]`, plus r10's `rounds[4]`,`[12]`); recorded 16 terminations 18:27:54–20:05:46, "each step-1 verified (ancestry, SHONEN, ordering, marker screen — **0 markers this round**)" (r11:82-84, 183-184); wrote 4 new in-flight rows, all live at the freeze (`rounds[19]` protocol/kengaku/kumitate; `rounds[20]` kotoba); opened first entries for rounds 12/13 (`rounds[20]`,`[21]`).
4. Digest per-line, timestamp+text, plus totals "`launch 69, complete 68, steer 15`" (r11:106-122).
5. Post-freeze band left to round 12: "aggregator r7 (complete 20:13:17 …), kagi r11 complete line (20:13:19 — status already recorded `ok` on completion evidence)" (r11:102-104; re-run `grep -nE 'complete (aggregator round=7|kagi round=11)' .ufo/watchdog.log` → lines 189/191, same timestamps).
6. Durability: 3 untracked reports of terminated missions committed by `3ea42cb`; live-mission reports deliberately NOT swept (r11 §Conformance 8).
7. Self-check: "valid; 22 entries; `rounds[1]` still the round-1 `work` entry …; last-wins tally 73 ok / 4 failed / 4 in-flight / 23 not-dispatched" (r11:98-101).
8. Sequencing: closure commit landed before the PROTOCOL.md edit it was verified against (`git show --stat` dates 20:13:40 < 20:15:40; CriticPlan "closure-before-compaction sequencing", r11 §L2 record).

## Semantics spec (checker acceptance criteria)

1. **Shape/vocabulary**: `lanes` values ∈ `ok|failed|not-dispatched|in-flight`; `closed_at` REQUIRED on any entry carrying `not-dispatched` or `in-flight` (P:206, P:211-213, P:241-242). Ex: `rounds[20]` has both + `closed_at`.
2. **Freeze**: one `closed_at` per pass; lane-rounds terminating after it get no row in that pass (r10:43-44). Ex: aggregator r7 complete 20:13:17 (`watchdog.log:189`) appears in no `rounds[15..21]` lane set.
3. **Dispatch evidence** = `launch <lane> round=N` or `steer <lane> -> round N` line; prompt with no line = attempted dispatch → `failed` (P:215-221). Ex: `rounds[5]` — only kagi steered to round 2; other 7 `not-dispatched`, `lane_rounds` 1.
4. **Completion evidence** = report satisfying the contract; contentless marker → `failed`; marker naming a real committed hash → `ok` + minimum-content defect; marker naming nothing checkable → `failed` (P:151-155). Ex: `rounds[11]` kengaku `failed` (101 B, false claim); `rounds[10]` kumitate `ok` (122 B, names `7a4c9a0`).
5. **Termination evidence** = `complete <lane> round=N` line or counter passing N (P:223-224); a late complete line never reopens a status written on completion evidence. Ex: kagi r11 `ok` in `rounds[19]`, complete 20:13:19.
6. **in-flight** decided from absence of BOTH a `complete` line and a report at `closed_at`, never from a status probe (P:224-228). Ex: `rounds[19]` protocol `in-flight` (launched 18:50:31; report lands later as the closure artifact).
7. **Debt**: every in-flight row answered next pass by an appended `closure-correction`; still-live → re-confirm `in-flight` + launch pointer (P:233-240). Ex: `rounds[9]` aggregator in-flight → `rounds[15]` `ok`; `rounds[19]` kengaku/kumitate re-confirmed (launches `watchdog.log:181,187`).
8. **Append-only + last-wins**: corrections appended with `supersedes:{round,type,date}`, never in-place/prepended; consumers read in order, last row per (lane, N) wins (P:256-260). Ex: `rounds[4]` supersedes `rounds[1]`; `rounds[1]` untouched (13 index citations keep resolving).
9. **lane_rounds**: required on every `not-dispatched` row; elsewhere only where it differs from the entry's `round` (P:244-249). Ex: `rounds[14]` 7×nd with counters <11; `rounds[17]` records only kumitate.
10. **not-dispatched** requires no dispatch line for (lane,N) as of `closed_at` AND counter < N; a dispatch line contradicts the row (P:241-243). Ex: `rounds[13]` aggregator nd/`lane_rounds` 6.
11. **Retroactive typing**: pre-integrator terminations → `type:"retroactive-closure"` + notes "presence-of-evidence only; step-1 did not run; pre-fleet-2 (`609ecb6`) no axis duty" (P:250-255). Ex: `rounds[7]`.
12. **Step-1 at pass time** (P:178-186), defects status-neutral (P:155): (a) each cited child-repo hash: `git -C <lane-repo> cat-file -t <h>` = `commit` AND `git -C <lane-repo> merge-base --is-ancestor <h> HEAD` exit 0; unattributed tokens searched across main + all 6 child repos (+ external read-only; no fetch into mid-rebase repos); (b) no uncommitted round work; (c) `grep -cE '^#{1,6} *SHONEN' <report>` ≥ 1; (d) dispatched prompt carried the 5 items + route map matches `MISSION.md`; (e) report mtime ≥ its own cited commit's time; (f) marker screen per item 4. Ex: `rounds[18]` kagi `ok` with defects in notes; `rounds[21]` kasegi `ok` with dead hash `d7dbd9a` in notes.
13. **Hash classes** (verify2.md §2): dead = `cat-file -t` fatal in every local odb → defect; orphan = resolves but is-ancestor exit 1 → defect; other hex = sha256/md5 pin or runId → verify against named file (`sha256sum <file> | cut -c1-12`) or ignore. Ex: `3d28a716` orphan of bounties HEAD, ancestor of `main`; `2586de87081a` = kagi `corpus/surface-census.sh` pin.
14. **Digest duty**: committed timestamp+text of every dispatch/complete line a status rests on; never line numbers (P:229-232). Ex: r11:107-122.
15. **Self-check**: JSON parses; `rounds[1]` still the round-1 `work` entry; per-pass last-wins tally published (r10:62-64; r11:98-101).

## Drift between rounds

1. **Correction width**: all corrections (`rounds[4]`,`[12]`,`[15..19]`) carry only changed lanes (`rounds[15]` = aggregator alone); first entries (`rounds[13]`,`[14]`,`[20]`,`[21]`) carry full 8-lane maps. Matches the correction shape at P:234-235 + last-wins. **Winner: partial corrections, full maps only for first entries** — repeating `not-dispatched` rows would demand fresh `closed_at` evidence for lanes not re-examined.
2. **`supersedes`**: actually written — present on all 7 corrections (live JSON, observed). Not drift; the checker should assert it on every `closure-correction`.
3. **lane_rounds redundancy**: `rounds[18]`/`[19]` repeat counters equal to the entry round; `rounds[17]` has kumitate 9 (= entry round) while omitting kengaku/kotoba/kagi (also 9). Inconsistent. **Winner: P:244-246** — include where it differs or the row is `not-dispatched`; equal-value repeats are tolerated noise, not obligation.
4. **Digest granularity**: r10 compressed ranges ("15:56:51-16:17:23 complete <lane> round=3 (all 8)", r10:87-102); r11 line-per-line (r11:107-122). P:230 says "every dispatch/complete line a status rests on". **Winner: r11 per-line** — only per-line quotes re-resolve against the mutable log.
5. **Step-1 depth**: r10 verified discovered contradictions and typed retroactive rows un-verified; r11 ran step-1 on every newly recorded termination with per-lane defect notes. **Winner: r11 for live terminations; r10's disclaimer discipline stays for genuinely retroactive bands** (P:250-255 keeps both).
6. **Sequencing**: r11 committed closure before editing PROTOCOL.md; r10 landed entries + protocol edit in one commit (`640a4c5`). **Winner: r11** — statuses verified against the text that governed them; the checker run must not depend on same-pass protocol edits.

## Inference vs observation

- Observed this session (command → output): JSON validity + 22 entries; the `3ea42cb` +7 MANIFEST hunk; `supersedes` keys on all 7 corrections; watchdog lines 178-198; kagi r11 report tracked, added by `029c474` / operator identity / 20:09:05 (`git log --diff-filter=A --format='%h %an <%ae> %cI'` → that line); counters `12 8`; every `P:n`/`rN:n` quote above via grep.
- [INFERENCE] r10 sourced `lane_rounds` from `.ufo/state/<lane>.round` (no command quoted in r10; values consistent with launch lines and today's counters).
- [INFERENCE] verify2's table column order = execution order (artifact presents one table; r10's conformance numbering is presentation order, not a proven sequence).
- [INFERENCE] Marker size thresholds (101–254 B vs 4370–16486 B) are observed outcomes, not codified cutoffs; the codified test is content-bearing vs not (P:151-155).

## Gaps

- `hexcheck.sh` (verify2 §7 reproduce block) lived under `/tmp/shokunin-r11/` and was never committed; the per-hash mechanics survive only as `verify2.md` §2 prose — the round-12 checker must re-implement them (spec items 12–13 are the recovery).
- MANIFEST `notes` tails beyond ~768 chars were display-truncated in my dump; spec items depend only on keys/lanes/lane_rounds/supersedes, read in full.
- r10's `640a4c5` MANIFEST hunk not re-shown (git show ran for `3ea42cb` only); its 11 entries are attested by the live array + r10 report table.
- Whether r10 read `.ufo/state/` live or from a snapshot is unrecorded (inference 1); the checker should derive lane_rounds from dispatch/complete lines, which both rounds' published data support.
- The post-20:10 band (protocol r11/kotoba r12 completes ~20:28, plus all launches after) was seen via the brief + partial grep only; I did not enumerate it exhaustively — the checker's log sweep will.
