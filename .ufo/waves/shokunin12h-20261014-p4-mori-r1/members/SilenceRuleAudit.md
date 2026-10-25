# SilenceRuleAudit — lane-silence rule vs PROTOCOL.md

Advisory only. No ledger failed, no remediation, no script invocation. The gate grade below is the branch probe_silence takes on the measured inputs, not a live mori-census.sh run.

Observation clock: `date +%s` returned 1792024860 = 2026-10-14T21:41:00-03:00 (2026-10-15T00:41:00Z). Implementation under test: `mori-shokunin/tools/mori-census.sh` at `dccea91` (mori-shokunin, 2026-10-14T21:42:01-03:00, clean index on that path). Protocol text: `PROTOCOL.md` lines 155-168, read at the same clock.

## 1. Protocol rule (cite)

`PROTOCOL.md:155-168`, the rule in force:

A mission still open more than two driver ticks after its steer is a stale-lane review trigger; the integrator may record it failed. The trigger needs an actuator: every dispatched lane's report must list any mission open longer than two driver ticks — age from the launch timestamp, not the tick counter (it resets when the driver restarts) — and must say whether it is progressing or silent. Progressing means observable activity in the lane's write scope since its launch — a commit authored by the lane, or files modified under its repo (`find REPO -newermt LAUNCH-TS -type f -not -path '*/.git/*'`); silent means neither. A commit authored by another lane is not the subject lane's activity, since the aggregator writes into every child repo, so sibling-authored activity alone is a third grade, progressing-weak: named as such in the row, never called progressing, and never silent or failed on its own. Commit sparsity is the norm (Appendix, "Stale-lane actuator"), so the absence of a commit is not silence and must not trigger failed. The integrator-of-record records failed only for silent missions and flags progressing ones in the round notes. Recording failed is a ledger act, not a kill (`PROTOCOL.md:168`).

Driver tick: `scripts/shokunin-watchdog.sh:10` `INTERVAL=450`. Two ticks = 900 s. The actuator applies only to a mission still open. Age is from the launch line, not from a report mtime and not from a rolling window.

## 2. Rule as implemented

`mori-census.sh:85` sets `LANE_SILENCE_S` default 7200.

`mori-census.sh:466-470` claims `PROTOCOL.md:158-167`, then states the approximation: window = NOW - LANE_SILENCE_S. No launch line is read.

`lane_repo` (471-475): protocol and aggregator both resolve to ROOT (the fleet root). Every other roster id resolves to ROOT/LANE-shokunin.

`probe_silence` (478-524), the branch that decides the grade:

- head_t = `git -C REPO log -1 --format=%ct` (0 if that fails). Author is not read.
- newest_t = max `%T@` of `find REPO -type f -not -path '*/.git/*'`, integer seconds. No author, no write-scope filter, no gitignore filter.
- If newest_t >= window_start: grade progressing (509-510). Comment at 505-508: author check deferred; any in-window file is progressing.
- Else if head_t >= window_start: grade progressing-weak (512-513). This is not an author test. A lane-authored tip with no newer file takes this branch.
- Else: `LANE_SILENT` severity warn (518), and `emit_finding` (118-126) flips the census roll to DRIFT.

Default roster (86) is the nine driver lanes. Later `MANIFEST.json` roster ids are not graded unless `MORI_ROSTER_LANES` is set. That coverage gap is not exercised by the two lanes below; both are in the default list.

`mori-shokunin/SKILL.md:19` states a third procedure — lane HEAD vs last report mtime — and does not mention launch timestamp, file mtime, or progressing-weak. The gate does not execute that row. It is cited so the lane's own decision table is not mistaken for the script.

## 3. Two lanes

Window used by the script at this clock: window_start = 1792024860 - 7200 = 1792017660 (2026-10-14T19:41:00-03:00).

Commands (read-only), both lanes:

- `git -C REPO log -1 --format=%ct %h %an %ae %cI %s`
- `find REPO -type f -not -path '*/.git/*' -printf '%T@ %p\n'` (max `%T@`)
- `git -C REPO log --since=@1792017660 --format=%h %an %ae %cI %s`
- last launch / wrap for the lane in `.ufo/watchdog.log` (294 lines; last line `2026-09-28T23:55:00-03:00 tick=3`; no later launch)

The script was not executed. The implemented grade is the branch at 502-518 on these integers.

### 3.1 kasegi — activity grade agrees; applicability does not

| Input | Observation |
|---|---|
| Repo the script uses | `/home/vgpnk/Projects/shokunin/kasegi-shokunin` |
| head_t | `1792024309` `4b2e302` `kasegi-shokunin` `kasegi@shokunin.local` `2026-10-14T21:31:49-03:00` |
| newest_t | `1792023917` `kasegi-shokunin/corpus/lessons/round-20-recensus.md` |
| Newest-file last commit | `ea36dfc` `kasegi-shokunin` `2026-10-14T21:25:17-03:00` |
| Commits with `--since=@1792017660` | 5, all `kasegi-shokunin`. Zero other authors. |
| Porcelain on that lesson, `SCORECARD.md`, `LOG.md` | empty |
| Last launch | `.ufo/watchdog.log:266` `2026-09-28T23:15:03-03:00 launch kasegi round=17` |
| Last termination | `.ufo/watchdog.log:287` `2026-09-28T23:54:59-03:00 wrap kasegi round=17 complete; NOT respawning (fleet-wrap)`. No later launch kasegi. |
| Open mission | no |

Implemented grade: progressing. Both timestamps are >= 1792017660, so the file branch (509-510) fires. Author is not consulted. `LANE_SILENT` does not fire.

Protocol grade: the actuator does not assign a grade. Round 17 is wrapped. There is no mission open more than two ticks, so there is nothing to list as progressing or silent, and failed is not available. That is a divergence of applicability, not of the activity label.

If the activity test is applied anyway to the window the script actually uses: a commit authored by kasegi-shokunin is inside the window, and the newest file's last commit is the same identity. Protocol activity label: progressing. The two labels match. The match does not depend on the deferred author check, because the author is the lane. It does not use the protocol baseline: the script never read line 266.

Commit sparsity does not arise. Absence of a commit is not what saved this lane.

### 3.2 aggregator — grades diverge

| Input | Observation |
|---|---|
| Repo the script uses | ROOT = `/home/vgpnk/Projects/shokunin` (lane_repo maps aggregator to the fleet root, same as protocol) |
| head_t at the scan | `1792024849` `d3bc444` `protocol-shokunin` `protocol@shokunin.local` `2026-10-14T21:40:49-03:00` |
| newest_t at the scan | `1792024857` `game-dev-3d-shokunin/corpus/live/r87-baseline/watch.log` |
| That path in the main repo | `git check-ignore -v` returns `.gitignore:1:*-shokunin/`. `git log -1` on that path is empty. A follow-up `stat` at 21:41:37-03:00 showed mtime 1792024897 (the file was still being written). Still inside the window. Still not an aggregator commit. |
| Commits on ROOT with `--since=@1792017660` | 17 `protocol-shokunin`, 1 `shokunin-fleet`. Zero `aggregator-shokunin`. |
| aggregator-shokunin commits in the same window in 19 child repos | none (`git log --since=@1792017660 --author=aggregator` per child repo) |
| Last launch | `.ufo/watchdog.log:247` `2026-09-28T22:37:21-03:00 launch aggregator round=10` |
| Last termination | `.ufo/watchdog.log:286` `2026-09-28T23:54:59-03:00 wrap aggregator round=10 complete; NOT respawning (fleet-wrap)`. No later launch aggregator. |
| Open mission | no |
| Aggregator-authored commit after that launch, outside the script window | `b159992` `aggregator-shokunin` `2026-09-29T01:24:49-03:00` `round-11` on the main repo. After the wrap. Not an open-mission signal. Not inside 1792017660..1792024860, so the script did not use it. |

Implemented grade: progressing. newest_t >= window_start, so the file branch fires. The tip author protocol-shokunin is never read. The winning file is a gitignored child-repo runtime log, outside the aggregator write scope at `PROTOCOL.md:310-317` (child corpus/ files the aggregator itself commits, its own report, AGGREGATE.md — not another lane's watch.log).

Protocol grade: no open mission, so the actuator does not list aggregator and must not record failed. On the evidence the script used for its window, there is no commit authored by the aggregator, and the file the script counted is not aggregator write-scope activity. The commits in that window are protocol-shokunin and shokunin-fleet. `PROTOCOL.md:162-165`: a commit authored by another lane is not the subject lane's activity; sibling-authored activity alone is progressing-weak, never called progressing, never silent, never failed on its own. Protocol activity label for that window: progressing-weak. Implemented label: progressing. They do not agree.

The script would still have said progressing if d3bc444 had not existed, because watch.log alone satisfies lines 509-510. That is the r12 failure mode named in `PROTOCOL-APPENDIX.md` (Stale-lane actuator, round 12): the file-mtime half attributes another lane's work to the subject.

## 4. Divergences

Fired on these two lanes:

1. Baseline. Protocol: launch timestamp of an open mission (`.ufo/watchdog.log:266` and `:247`). Script: now - 7200, and it does not open the log. 7200 / 450 = 16 driver ticks, not two (900 s).
2. Applicability. Both missions wrapped at `.ufo/watchdog.log:286-287`. Protocol assigns no stale-lane grade. The script grades both.
3. Authorship, on aggregator only. Protocol: other-lane commits are not the subject's activity; sibling-only activity is progressing-weak and must not be called progressing. Script: any in-window file mtime is progressing (505-510). kasegi does not show this, because its in-window commits and the newest file are kasegi-shokunin.
4. Repo scope, on aggregator only. lane_repo points aggregator at the fleet root, so find walks gitignored `*-shokunin/` trees. Protocol write scope for aggregator does not include `game-dev-3d-shokunin/corpus/live/.../watch.log`.

Not fired on these two lanes, still in the function:

5. The progressing-weak branch (512-513) is "HEAD in window, files not", not "author is not the lane". A lane-authored tip with a quiet tree would be called progressing-weak. Protocol would call that progressing. Neither sample took this branch.
6. `LANE_SILENT` warn flips DRIFT (118-126, 518). Protocol failed is a ledger act for a silent open mission only, and this lane must not record it. A closed lane with both timestamps outside 7200 s would still be emitted as drift. Neither sample was outside the window, so this false drift was not observed tonight.
7. `SKILL.md:19` (HEAD vs last report mtime) is not the script and is not the protocol. Both sample lanes have a HEAD newer than their report file, so that row would also not call them silent. It has no progressing-weak test.

Commit-sparsity clause: the script's file-mtime half does refuse "no commit means silent", which matches `PROTOCOL.md:165-167` for a lane that has actually modified its own files. On aggregator that half is what creates the false progressing, so the clause is implemented as a mtime test without the authorship exception the same paragraph requires.

## 5. Residual

- Unknown, not measured: a live `mori-census.sh` stdout line. The grades above are the function on the recorded integers. A run after 21:41:00 can move watch.log and HEAD (a later `git log -1` on the fleet root already showed `2d6dcd6` `protocol-shokunin` at 21:41:38). Author of that tip remains not the aggregator, so lane 2's disagreement does not depend on d3bc444 specifically.
- Not a silence grade: no watchdog pid was probed here. The log's last line is `2026-09-28T23:55:00-03:00 tick=3`. Whether a driver is running is a liveness observation, not an input to probe_silence.
- `b159992` shows aggregator did commit, once, after the wrap and outside the script window. Using "since launch" while ignoring the wrap would call aggregator progressing and hide the disagreement. The protocol subject is the open mission. There isn't one.
- This report does not record failed and does not recommend a kill, restart, or rewrite. The disagreement is the finding.
