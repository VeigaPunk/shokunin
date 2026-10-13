# reviewer-citations — round-12 candidate audit (seat: ReviewerCitations, 2026-09-28 ~21:10–21:40 -03:00)

Target: uncommitted diff of `PROTOCOL.md`/`MANIFEST.json` + `exec-gate-standard.md` as briefed.
**Target moved twice mid-audit** (see `## Unverifiable`): candidate committed as `dddb4ec` 21:11:43
("gate-integrity axis-move"); then `df1b2c6` 21:16:51 (entries 28–29, closed_at 21:20) landed. All
findings below are against the candidate text captured at audit start.

## Re-executed

| Claim | Command | Observed | Verdict |
|---|---|---|---|
| PROTOCOL 446→514 lines | `git show 46e9ec3:PROTOCOL.md \| wc -l -c`; `wc -l -c PROTOCOL.md` | `446 39718`; `514 47874` at audit start | holds |
| census | `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md` | `93/93 obligations found; 0 MISSING`, exit 0 | holds |
| MANIFEST valid JSON | `python3 -m json.tool MANIFEST.json` | clean parse, exit 0 | holds |
| rounds[] count | `jq '.rounds\|length'` | 28 at audit start; **30** by final read (28–29 appended, `df1b2c6`) | holds (moving) |
| 25 commit hashes exist + repo | loop `git -C <repo> cat-file -t` over `.` + 6 children | all 25 resolve: main `.` = 6d27283, 46e9ec3, 392b3c7, 50b2179, f9dcfd2; kotoba = 633859f, 4dd7753, abef8aa, d49dfa5, 683d147, 7163c81, ed5c261; kasegi = 7483333, fc6d398, 9dbe69f, 2b0d869; kengaku = d8f2898, 06cdc98; kake = 69c1856, 4c9a985; kumitate = e79fefa, 23452e7, 71b5e57, 59e6c0c; kagi = e0a04d8, 7c3377c, 4391b3b | holds |
| ancestor of repo HEAD | `git -C <repo> merge-base --is-ancestor <h> HEAD` per hash | 27/27 ANCESTOR (incl. f9dcfd2, 71b5e57, 59e6c0c) | holds |
| author identities | `git log -1 --format='%an <%ae> %ai'` | 6d27283 aggregator-shokunin 20:32:43 ✓; 392b3c7 protocol-shokunin 20:27:31 ✓ (< complete line 20:28:20 ✓); 46e9ec3 operator 20:45:10 ✓; 50b2179 operator 20:48:46 ✓; 633859f kotoba-shokunin 20:27:55 ✓; 12 box-3 commits all aggregator-shokunin ✓ | holds |
| report byte counts | `wc -c` ×6 | round-7/aggregator 10695, round-11/kumitate 16341, round-11/kengaku-DRAFT 15922 (pre-rename), round-12/kotoba 14009, round-12/kagi 13620, round-14/kasegi 7338 — all exact | holds |
| SHONEN counts | `grep -cE '^#{1,6} *SHONEN' <report>` | protocol r11 = 1, kumitate r11 = 1 ("SHONEN=1" ✓), kotoba r12 = 1 ✓, kasegi r14 = 0 (ABSENT ✓), kagi r12 = 0 ✓; aggregator n/a exclusion ✓ (round-3/5/7 aggregator.md appear in raw `grep -rLE` list, filtered by `grep -vE`) | holds |
| watchdog digests (15 lines) | `grep -nF` each quoted timestamp+text | byte-exact at lines 171, 173, 181, 185, 189, 190, 192, 195, 196, 197, 198, 202, 203, 204, 205 (log 215 lines at read) | holds |
| closed_at absences | `grep -cF` + timestamps | `complete aggregator round=8` first at 21:14:05 (l.211), `complete kagi round=12` 21:06:05 (l.208), `complete kotoba round=13` 21:14:11 (l.213), `complete kengaku round=11` still 0 — all post-20:55 closed_at | holds |
| kagi r12 only-cited-hashes | `grep -oE '\b[0-9a-f]{7,40}\b' round-12/kagi.md \| sort -u` | exactly 4391b3b, 7c3377c, e0a04d8 — all aggregator-shokunin box-3 ✓; untracked ✓; mtime 21:02:57 ✓ | holds |
| kotoba r12 line 224 | `sed -n 224p` | ``- Commit: `LANE_HASH` in `kotoba-shokunin`…`` ✓; NR=225 ✓ (awk) | holds |
| kake r13 erratum | `git diff --numstat -- .ufo/reports/round-13/kake.md` | `3 1` ✓; diff carries `r14 erratum: this report first wrote 06:00:36Z` ✓ | holds |
| kengaku gate over 06cdc98 | `git archive 06cdc98 \| tar -x; python3 grader.py` | `CHECKS n=149 mismatches=0 errata_pinned=1 / VERDICT: PASS` exit 0 — exact | holds |
| self-tests (4 of 5) | run as non-owner from main repo | drift-pins `DRIFT_SELFTEST: PASS (13 cases)`; transcript-scan selftest exit 0; grader `[selftest] ALL PASS`; round-gate `ROUND_GATE_SELFTEST: 57/57 pass`; harness `0 failure(s) over 10 assertions` | holds |
| default-mode gate readings | same session | `TRANSCRIPT_SCAN: HITS=2` exit 1 ✓; `DRIFT_PINS: CLEAN (files=15 symbols=20)` ✓; round-gate default `CLEAN … checks=10 errors=0` ✓ (now `round=12`, was 10 at exec reading) | holds |
| kotoba 25/27 at r12 reading | archive `633859f` harness vs current host | `DRIFT omp.db.rows: observed=18 expected=17` (+ `rows_wellformed` same) → `25/27 checks pass` — exact (second drift line unnamed in PROTOCOL:521) | holds |
| --json vs text divergence | temp archive HEAD, baseline removed | text exit **3**, `--json` exit **0** — exact | holds |
| no-baseline exit 3 | grep + behavioral | verify_surfaces.py:174/884–889 (self-tested), integrity:1023, harness:662 | holds |
| kumitate `64` in three | grep scripts/ | proxy-check.mjs 4, round-gate.mjs 7, surface-probe.mjs 1 — three scripts ✓ | holds |
| probe-delta self-declaration | `grep -n 'not a gate' …/probe-delta.mjs` | line 26: `Exit 0 = parsed fine (this is a report, not a gate); 2 = unreadable input.` ✓ | holds |
| versions | `node/python3/sqlite3 --version` | v24.19.0 / 3.14.7 / 3.53.4 — exact | holds |
| `report_of()` | `sed -n 44p scripts/shokunin-watchdog.sh` | exact one-liner ✓; single PROTOCOL.md mention, now line 156 | holds |
| SCORECARD.md:57 stale l0 cite | `sed -n 57p`; `grep -nE kengaku\|kumitate .ufo/l0-questions.md` | cites "line 6"; live kengaku=7, kumitate=8 ✓ | holds |
| exec: kengaku `M grader.py`; closure-check.py absent | `git -C kengaku-shokunin status`; `ls` | worktree now clean; closure-check.py exists (73339 B, mtime 21:22) — both **resolved since** exec wrote | holds-then |

## Dead or wrong

- **`46e9ec3` l0 numstat (PROTOCOL.md:524, "L0 durability" row): claimed `+5/-1`, observed `+4/-1`** — `git show --numstat 46e9ec3` → `4 1 .ufo/l0-questions.md`. Off by one on insertions. LOW.
- **19 min 17 s gap (entry #22 notes + PROTOCOL.md:523): actual 19 min 26 s** — complete line 20:13:17 (log l.189) → 6d27283 author= committer= 20:32:43. Off by 9 s. LOW.
- **Entry #24 "kumitate… lane then added 71b5e57/59e6c0c at 20:46"** — confirmed 20:46:01/20:46:28 ✓; "23452e7 was HEAD when the report was written" ✓ (20:44:26 < 46e9ec3 20:45:10 < 71b5e57). Cleared.
- **Aggregator box-3 list (entry #23): CLEARED** — all 12 commits exist in the named repos, all aggregator-shokunin-authored, window 20:33:25 (9dbe69f) → 20:41:28 (4c9a985) exactly as claimed; entry attributes them to the aggregator, not the lanes. No misattribution.
- **`4028846`**: confirmed dead in all 7 local ODBs; `~/Projects/bounties` now **gone from the filesystem** (`test -d` fails) — entry #27's "mid-rebase, read-only" premise was true at write, state since moved (l0 kasegi-r15 row records the same). Verdict stands.
- **`391a54f4`**: confirmed dead in main + 6 child repos; cited at `.ufo/reports/round-12/kotoba.md:81` as "committed blob". Defect belongs to the kotoba r12 report; the candidate does not assert it resolves.
- **kengaku worktree FAIL (PROTOCOL.md:521, `n=280 mismatches=1`)**: no longer reproduces — post-ExecChecker worktree run: `CHECKS n=280 mismatches=0 … PASS` exit 0. n=280/n=149 figures both confirmed; the mismatch was real at write time (unreproducible now — tree landed).
- **Entry #24 kengaku-DRAFT `{{N}}`**: unverifiable — see below; final `kengaku.md` (18585 B) contains 0 `{{N}}`.
- Stale line cites observed (file churn, not author error): Gate standard heading now **346** (brief said 319; 342 at session start); appendix rows now **520–526** (brief: 447–452/512–514); `report_of` mention now 156; round-gate.mjs header still cites `PROTOCOL.md:263-267` (verified stale — step 1 is 192–200) → routed finding stands.

## MANIFEST evidence

Every status in entries 22–27 rests on a quoted timestamp+text digest (PROTOCOL.md step 4, lines 241–248), every `in-flight` row carries its launch pointer, every `not-dispatched` row has `lane_rounds`, every `ok` row's report is derivable:

- **#22 r7 aggregator `ok`**: digests l.171/l.189 ✓; report exists 10695 B ✓; uncommitted-at-completion derivable (file added by 6d27283 at 20:32:43 > complete 20:13:17) ✓.
- **#23 r8 aggregator `in-flight`**: launch digest l.190 ✓; absence of complete+report at closed_at ✓ (complete 21:14:05).
- **#24 r11**: protocol `ok` digest l.195 ✓, report exists ✓; kumitate `ok` digest l.204 ✓, report 16341 B ✓; kengaku `in-flight` launch l.181 ✓. "Every main-repo hash it cites resolves and is an ancestor" — swept all 37 hash tokens in round-11/protocol.md: 21 resolve+ANCESTOR in main; 13 of the 16 dead-in-main are child-repo cites (resolve in their repos); 3 nowhere (`e66e614`, `3d28a716`, `d7dbd9a`) are quoted **as recorded defects D-51/D-52/D-53** (report lines 159–164, 211–213), not evidence — claim holds in scope.
- **#25 r12**: kotoba `ok` digest l.197 ✓ + report 14009 B/225 lines ✓; protocol/kagi/kumitate `in-flight` launches l.196/l.192/l.205 ✓; kagi "no report at closed_at" true (mtime 21:02:57 > 20:55) ✓.
- **#26 r13**: kotoba `in-flight` launch l.198 ✓; absence ✓ (complete 21:14:11); "no kotoba-authored commit since launch" true at closed_at (first kotoba-authored commit 21:04:30) ✓; 683d147/7163c81/ed5c261 aggregator-authored 20:33:45–20:37:06 ✓.
- **#27 r14**: kasegi `ok` digest l.202 ✓ + report 7338 B ✓; kake `in-flight` launch l.185 ✓, no complete/report ✓; all six `not-dispatched` rows covered by the 8-lane `lane_rounds` map ✓; no round-15 entry, trigger correctly unfired ✓.
- Forward debt created post-closed_at (not this candidate's defect, owed by next pass): aggregator r8 (21:14:05), kotoba r13 (21:14:11), kengaku r11 (report landed 21:17:49, r12 launched 21:21:48) have terminated without rows; kagi r12 resolved by entry #28.

## Unverifiable

- **Moving tree**: PROTOCOL.md 514→526 lines (49041 B, still `M`) and MANIFEST 28→30 entries (`df1b2c6`) during the audit; kengaku-DRAFT.md renamed to kengaku.md (15922 B observed pre-rename; final 18585 B) — the `{{N}}`-in-DRAFT claim can no longer be checked against the named bytes; closure-check.py rewritten at 21:22 by its author seat (frozen-run verification is ExecChecker's, not re-run here); kotoba worktree dirty (3 files `M`) during harness runs.
- **"14 committed verdict scripts / 13 declare 0/1"** (PROTOCOL.md:520): census reproducible = **15** tracked `.sh`/`.py`/`.mjs` (kagi 4, kake 1, kasegi 0, kengaku 1, kotoba 5, kumitate 4; `corpus/evidence/` excluded); 14 is reachable if probe-delta self-excludes as non-gate, and "six child lanes" is loose (kasegi contributes 0). The 13-declare figure is classifier-sensitive (several scripts compute exits; mechanical grep confirms 7 of 15 declare literal 0-and-1) — PARTIAL, not falsified. Also "no-baseline 3 in two scripts" was true at the r12 reading; verify_surfaces.py is r13-new and makes it three.
- **kengaku "30 files newer than launch"** — measured 40 (mission landed meanwhile); drift makes the entry-time count unreproducible. The cited analysis artifacts exist (`bench-arena-round11-power.md`, ESTABLISHED/3.431 grep hits).
- **≈8.4 s selftest tally** — individual runs observed green; the aggregate timing not re-taken.
- Historical M6/M11 figures pinned to `0a30b44` not re-executed (pre-candidate rows, out of diff scope); live M6 grep = 56, exclusion mechanism verified.

## Gaps

- `4028846` ancestry beyond local ODBs is permanently unverifiable: the bounties repo is gone, so "resolves only in un-fetched origin" (protocol r11 D-52 reasoning) can never be confirmed or refuted locally.
- The `--json` divergence was reproduced on `verify_harness_claims.py`; I did not isolate which r12-era script the row meant (integrity's no-baseline path exited 2/2 in my one attempt — possibly wrong invocation).
- Entry #28's `supersedes.entry` disambiguator and the 514→526 PROTOCOL delta (`df1b2c6`) post-date the briefed candidate and were not audited as candidate text.
- aggregator r8, kotoba r13, kengaku r11 terminations (21:14–21:21) owe rows in the next closure pass; kagi r13 `in-flight` is already carried by entry #29.
