# Lane silence census (advisory data)

Seat: `LaneSilence`. Read-only over the host. Not a judge verdict, not a `failed` marking, not a remediation. No process was signaled, no repo was written, no report file outside this path was touched.

Graded set: the 13 ids in `MANIFEST.json` `roster` (read 2026-10-14, lines 5–109). `shokunin.conf` `LANES` names more ids; those are outside this grade set and are not graded below.

## Rule applied

Fleet rule, `PROTOCOL.md` 159–166: progressing is a lane-authored commit, or files modified under the lane repo, since the baseline; silent is neither; a commit by another lane is not the subject lane's activity; sibling-authored activity alone is `progressing-weak` (named as such, never called progressing, never silent or `failed` on its own). Commit sparsity is normal and is not silence.

Same split as `.ufo/waves/round-15/closure-check.py` `lane_commits` / `unattr` / `sibling_authors` (lines 1374–1404): a lane-authored commit wins; an unattributed non-sibling-owned file also progresses; only then does a non-lane author become `progressing-weak`; else silent. Lane-authored means author name equals the id or starts with `<id>-`. `ci`, `Joao Pedro Veiga`, and any other name are not lane identity. They are also not automatically a sibling lane.

Skill row used: `mori-shokunin/SKILL.md` "Was a lane silent?" — lane HEAD vs last report mtime. A missing surface is `unavailable`, never silent and never unhealthy.

Baseline actually compared: mtime of the lane's own `.ufo/reports/round-<N>/<id>.md`, where N is the highest round with that file. That file lives in the lane report dir `.ufo/reports/round-<N>/`. The directory mtime is recorded and is not the grade baseline when it disagrees: a round dir is shared, and a directory mtime updates on entry create/rename, not on a write to an existing file. Using the shared dir mtime would grade kaidoku against kama's write. See MORI-R1-SILENCE-002.

HEAD time is committer date (`%cI`). On every HEAD in the freeze, `%aI` equalled `%cI`. `git log --since` is committer-date based. Newest file is the max `st_mtime` regular file under the live repo, directory named `.git` pruned, symlinks not followed.

No launch timestamp and no two-tick actuator entered the grade. `.ufo/state/*.round` was read and not used.

## Commands

Freeze walk and git reads, epoch `2026-10-14T21:36:21.987553-03:00`:

```
git -C <repo> log -1 --format='%h|%an|%ae|%aI|%cI'
git -C <repo> log --since=<report-file-mtime> --format='%an'
git -C /home/vgpnk/Projects/shokunin log -1 --format='%h|%an|%cI' -- .ufo/reports/round-<N>/<id>.md
stat mtime of that report file and of its parent directory
python os.walk of <repo>, skip a directory named .git, do not follow symlinks, regular files only, max st_mtime
git -C <repo> check-ignore -v <newest>
git -C <repo> log -1 --format='%an|%ae|%h|%cI' -- <newest>
```

Recheck, epoch `2026-10-14T21:37:23.522519-03:00`:

```
git -C kumitate-shokunin log --since=2026-10-13T16:44:48-03:00 --author=kumitate-shokunin -1 --format='%h %an %ae %cI %s'
git -C kumitate-shokunin log -1 --format='%h %an %ae %cI %s'
git -C audio-shokunin status --porcelain=v1 -uall -z
# then stat each porcelain path; count mtime > 2026-10-14T16:35:20.856810-03:00
git -C game-dev-3d-shokunin status --porcelain=v1 -uall
```

Report inventory and manifest-path check were in the batch whose `date -Is` printed `2026-10-14T21:30:51-03:00`. Repo `user.name` was read in that same post-21:30:51 HEAD pass (`git config --get user.name`).

Hashes below are `git log %h` abbreviations.

## Grades

11 progressing, 0 progressing-weak, 0 silent, 2 unavailable. All 13 rostered lanes are accounted for. Zero silent is an observation, not a claim that every lane is healthy.

| id | grade | report dir | report file mtime | dir mtime | HEAD (freeze 21:36:22) | HEAD vs file | newest non-.git file | newest vs file |
|---|---|---|---|---|---|---|---|---|
| kasegi | progressing | `.ufo/reports/round-20/` | 2026-10-14T21:21:34.082180-03:00 | same | `4b2e302` kasegi-shokunin 21:31:49 | newer | `corpus/lessons/round-20-recensus.md` 21:25:17 | newer |
| kengaku | progressing | `.ufo/reports/round-16/` | 2026-10-14T21:21:34.083179-03:00 | same | `3f31e54` kengaku-shokunin 21:31:49 | newer | `corpus/lessons/round-16-recensus.md` 21:25:17 | newer |
| kake | progressing | `.ufo/reports/round-19/` | 2026-10-14T21:21:38.082181-03:00 | 21:21:34.083179 (3.999s older) | `bfecbcc` kake-shokunin 21:31:49 | newer | `corpus/lessons/round-19-recensus.md` 21:28:27 | newer |
| kumitate | progressing | `.ufo/reports/round-17/` | 2026-10-13T16:44:48.523047-03:00 | same | `85b2b70` ci 21:35:41; re-read `f6d6272` ci 21:36:50 | newer | `SCORECARD.md` 21:35:41 (freeze) | newer |
| kotoba | progressing | `.ufo/reports/round-19/` | 2026-10-14T21:21:34.083179-03:00 | same | `581e293` kotoba-shokunin 21:31:49 | newer | `corpus/lessons/round-19-recensus.md` 21:25:17 | newer |
| kagi | progressing | `.ufo/reports/round-19/` | 2026-10-14T21:21:34.080180-03:00 | 21:21:34.083179 (0.003s newer) | `15ea78c` kagi-shokunin 21:31:49 | newer | `corpus/lessons/round-19-recensus.md` 21:25:17 | newer |
| kama | progressing | `.ufo/reports/round-4/` | 2026-10-14T21:21:34.082180-03:00 | same | `117c4b2` kama-shokunin 21:31:49 | newer | `corpus/lessons/round-4-recensus.md` 21:31:14 | newer |
| audio | progressing | `.ufo/reports/round-76/` | 2026-10-14T16:35:20.856810-03:00 | same | `d9aa6f9` ci 19:55:17 | newer | `corpus/fixtures/measure_audio.py` 20:55:23 | newer |
| game-dev-2d | progressing | `.ufo/reports/round-77/` | 2026-10-14T17:11:12.720326-03:00 | 17:11:12.719099 (0.001s older) | `884a4c4` ci 20:42:34 | newer | `corpus/live/r79-author/runs/20261014T235547072468Z/verdicts.json` 20:57:43 | newer |
| game-dev-3d | progressing | `.ufo/reports/round-85/` | 2026-10-14T17:11:12.720587-03:00 | 17:11:12.720326 (sub-ms older) | `db64943` ci 20:47:36 | newer | `corpus/live/r86-baseline/watch.log` 21:36:24 | newer |
| lore | unavailable | no `<id>.md` under `.ufo/reports/round-*` | — | — | `5eb9451` ci 2026-10-13T17:05:05 | no baseline | `LOG.md` 2026-10-13T17:05:05.416720 | no baseline |
| revenger | unavailable | no `<id>.md` under `.ufo/reports/round-*` | — | — | `286033c` ci 2026-10-13T17:05:06 | no baseline | `LOG.md` 2026-10-13T17:05:06.833722 | no baseline |
| kaidoku | progressing | `.ufo/reports/round-4/` | 2026-10-13T14:17:56.280056-03:00 | 2026-10-14T21:21:34.082180-03:00 | `6645585` kaidoku-shokunin 2026-10-14T05:11:55 | newer than file, older than dir | `SCORECARD.md` 2026-10-14T05:11:55.373272 | newer than file, older than dir |

kumitate's freeze HEAD moved before the recheck. The grade does not depend on that tip. It depends on lane-authored commits still in the window, reconfirmed at 21:37:23.

## Per-lane evidence

Live repo for every row is `/home/vgpnk/Projects/shokunin/<id>-shokunin` (each has a `.git` directory). Six `MANIFEST.json` `repo` fields do not exist on disk; see MORI-R1-SILENCE-001. Grades use the live path.

**kasegi, kengaku, kake, kotoba, kagi, kama — progressing.** Observation: since the report file mtime, `git log --since` author counts were only the lane identity (kasegi 4, kengaku 4, kake 4, kotoba 4, kagi 5, kama 4; other authors 0). HEAD author is that same identity and is newer than both the report file and the report dir. Newest file's last commit is also that identity. Porcelain at 21:35:11 showed no untracked or dirty paths newer than the report. Commit sparsity does not arise: the tip is minutes after the report.

The report file's own last main-repo commit is not the lane. For these six, `git log -1` on the report path is `cb3c103` `protocol-shokunin` `2026-10-14T21:24:03-03:00` (`ops: phase 1 — six-lane re-census closure, mint scaffolds, wave evidence`). That is a sibling landing of the report in the main repo. It is not activity in the child repo, and it is not used as the child repo's author. File mtime (21:21:34, kake 21:21:38) is before that commit. Lane commits at 21:23 and 21:31 are after the file mtime. Grade is stable against either the file mtime or the content-commit time.

**kumitate — progressing, not progressing-weak.** Observation: report content commit is `bfc5db9` `Joao Pedro Veiga` `2026-09-29T01:32:37-03:00` (`round-17 kumitate report`). Stat mtime is `2026-10-13T16:44:48.523047-03:00`, same as the directory, with a clean index path (`git status --porcelain` empty on that path at the 21:30 batch). The inode was refreshed after the content commit. Grade uses the stat mtime, as measured. Since that mtime: 19 commits by `kumitate-shokunin`, 11 by `ci` (freeze). Recheck at 21:37:23 still has `175de6b` `kumitate-shokunin` `kumitate@shokunin.local` `2026-10-14T06:56:19-03:00`. A lane-authored commit in the window is progressing. The tip being `ci` (`f6d6272`, `2026-10-14T21:36:50-03:00`, subject `round-32: record the independent S8 verification and its two anchor nits`) does not erase those commits and is not itself the grade. Repo `user.name` is `ci`. `corpus/README.md` mtime `2026-10-14T21:31:18` matches the sibling-owned pattern; it is extra, not the grade.

**audio — progressing on unattributed files; zero lane-identity commits.** Observation: since the report file, 6 commits, all `ci <ci@local>`, 0 `audio-shokunin`. HEAD `d9aa6f9` is `ci`. Report content commit is also `ci` (`b14098a`, `2026-10-14T16:35:36-03:00`). Newest file `corpus/fixtures/measure_audio.py` is tracked; `git log -1` on it is `ci` `d9aa6f9` `19:55:17`, but the file mtime is `20:55:23`, so the working tree is ahead of that commit. `file_author` of that path is therefore `ci`, not unattributed. Recheck at 21:37:23: `git status --porcelain=v1 -uall` plus stat found 2164 untracked paths and 1 dirty tracked path with mtime newer than the report. Samples: `corpus/live/gst-scout/gst_probe.py` 16:53:40, `corpus/live/gst-scout/probe-control-r77.json` 16:49:38, `corpus/live/gst-scout/probe-errors-r77.json` 16:53:41. None matched `corpus/(README.md|lessons/round-.*aggregator)`. Unknown: who wrote the untracked files. Not inferred: that `audio-shokunin` committed, or that a sibling lane wrote them. Mechanical grade is progressing because unattributed files under the repo are newer than the report. Counterfactual, not the grade: if those untracked files were ignored, the row would be `progressing-weak` (ci commits and a ci-authored dirty file only), not silent. HEAD is newer than the report, so this is not a sparsity case.

**game-dev-2d — progressing on an unattributed newest file.** Observation: since the report, 3 commits, all `ci`, 0 `game-dev-2d-shokunin`. Newest file is gitignored (`corpus/live/.gitignore:1:runs/`) and has no commit (`git log -1` empty), mtime `20:57:43` > report `17:11:12`. That is unattributed file activity. Status scan at 21:35:11 also counted 46259 untracked paths newer than the report, 1 dirty tracked (`corpus/fixtures/run_battery.py`), and 1 sibling-owned regex hit. The regex hit is `corpus/live/r79-baseline/freeze/extract/corpus/README.md` at the HEAD commit time `20:42:34` — a path match inside a frozen extract, not an identified write to the lane's own `corpus/README.md`. Writer of the ignored `verdicts.json` is unknown. Not silent. Not progressing-weak: the newest file is not a sibling-authored commit.

**game-dev-3d — progressing on an unattributed newest file.** Observation: since the report, 6 commits, all `ci`, 0 `game-dev-3d-shokunin`. Newest file `corpus/live/r86-baseline/watch.log` is gitignored (`corpus/.gitignore:1:live/`), `git log -1` empty, mtime `21:36:24` during the walk that started at `21:36:22` (the log was being written during the measurement). Status at 21:37:23 still showed three untracked, non-ignored files: `reports/round-88/r88-baseline.md`, `r88-scout.md`, `r88-scribe.md`. Sibling-owned regex hits under `corpus/live/*/frozen-extract/corpus/README.md` are the same extract-path match as game-dev-2d, not an identified aggregator write. Writer of `watch.log` is unknown. A later run must not expect this mtime to hold. The class that should compare is: an ignored file under the repo newer than the report, plus zero lane-identity commits in the window.

**kaidoku — progressing. Sparsity is not silence.** Observation: 16 commits since the report file, all `kaidoku-shokunin`, 0 other. HEAD `6645585` `2026-10-14T05:11:55-03:00` is about 16.4 hours before the freeze. Newest file `SCORECARD.md` has that same timestamp and that same author. No dirty or untracked path newer than the report file. The gap is real and is not a silent grade. Report content commit is the lane: `415666f` `kaidoku-shokunin` `2026-10-13T14:17:56-03:00`. `corpus/README.md` at `2026-10-14T05:11:06` matches the sibling-owned pattern and is newer than the report file; lane commits still win.

**lore, revenger — unavailable, not silent.** Observation: no `lore.md` and no `revenger.md` under `.ufo/reports/round-*` at the 21:30:51 inventory (0 files each). No `.ufo/prompts/lore-round-*` or `revenger-round-*` in that inventory (`matched 0` for the prompt filter that also covered kaidoku and audio). No `.ufo/state/lore.round` or `revenger.round` (state dir listing). HEAD and newest file are both the 2026-10-13T17:05 ci revert of `HOURS.md` (`5eb9451`, `286033c`). That age is not a silence grade. Silence requires a report baseline to compare against. The baseline is missing. Calling this silent would treat a missing surface as unhealthy and would treat an old tip as failure. Both are refused.

## Findings

Ordered by how badly a later run mis-grades if it ignores them.

### MORI-R1-SILENCE-002 — shared report-dir mtime false-silences kaidoku

Observation. `round-4/` holds both `kaidoku.md` (mtime 2026-10-13T14:17:56.280056) and `kama.md` (mtime 2026-10-14T21:21:34.082180). Directory mtime equals kama's file mtime, not kaidoku's. kaidoku HEAD and newest file are both `2026-10-14T05:11:55`, older than the directory and newer than kaidoku's own report file. Grading against the directory yields silent. Grading against the lane report file yields progressing (16 lane-authored commits). The directory comparison is rejected. kake's file is 4s newer than its dir and kagi's file is 3ms older; those deltas do not change any other grade. Sub-millisecond dir/file deltas on game-dev-2d and game-dev-3d do not either.

### MORI-R1-SILENCE-004 — lore report surface missing

Observation. No report file, so no comparison. Grade `unavailable`. Not silent. See the lore row.

### MORI-R1-SILENCE-005 — revenger report surface missing

Observation. Same shape as 004. Grade `unavailable`. Not silent.

### MORI-R1-SILENCE-001 — manifest repo path absent for six rostered lanes

Observation. `MANIFEST.json` `repo` values `shokunin-game-audio`, `shokunin-godot-2d`, `shokunin-3d-engines`, `shokunin-world-bible`, `shokunin-binary-forensics`, `shokunin-reverse-engineering` are absent both under `/home/vgpnk/Projects/shokunin/` and under `/home/vgpnk/Projects/` (tested 21:30:51). Live checkouts are `audio-shokunin`, `game-dev-2d-shokunin`, `game-dev-3d-shokunin`, `lore-shokunin`, `revenger-shokunin`, `kaidoku-shokunin`, matching `shokunin.conf` `LANES` and `closure-check.py` `lane_repo` (`<id>-shokunin`). Grading the manifest path would mark these six `unavailable` for a missing repo, which is the wrong missing surface. lore and revenger are unavailable because the report is missing, not because the repo is missing.

### MORI-R1-SILENCE-006 — three progressing rows have no lane-identity commit since the report

Observation. audio, game-dev-2d, and game-dev-3d: commit authors since the report file are only `ci <ci@local>` (6, 3, 6). Repo `user.name` is `ci` on all three. Historical logs do contain `<id>-shokunin` commits; the window after the report does not. The progressing grade is the file half (untracked or ignored files newer than the report), not a lane-identity commit. Unknown: the writer of those files. Inference refused: "the lane identity is committing" and "a sibling lane authored the tip." Counterfactual, labeled as such: drop the unattributed files and these three become `progressing-weak`, still not silent. kumitate is not in this set; it has 19 `kumitate-shokunin` commits in the window despite a `ci` tip.

### MORI-R1-SILENCE-003 — kumitate report mtime is not the content commit

Observation. Content commit `bfc5db9` at `2026-09-29T01:32:37-03:00`; stat mtime `2026-10-13T16:44:48.523047-03:00`; index clean on that path. A later checkout or extract refreshed the inode. This run's grade is progressing under both timestamps, because lane commits exist after both. A later run that treats stat mtime as authoring time will mis-state when the report was written. It should not, on these numbers, flip the grade.

### MORI-R1-SILENCE-007 — no rostered lane graded silent

Observation at the freeze, unchanged by the 21:37:23 recheck. silent=0, progressing-weak=0, progressing=11, unavailable=2. kaidoku's 16-hour tip gap is the sparsity case the rule forbids calling silent. lore and revenger are the missing-surface case the rule forbids calling silent.

### MORI-R1-SILENCE-008 — sibling-owned regex matches frozen extracts

Observation. `SIBLING_OWNED_RE` (`corpus/(README.md|lessons/round-.*aggregator)`) matches paths under `game-dev-2d-shokunin/corpus/live/.../extract/corpus/README.md` and `game-dev-3d-shokunin/corpus/live/.../frozen-extract/corpus/README.md`, at the ci HEAD timestamps. That is a path match. It is not evidence that aggregator wrote the lane's `corpus/README.md`. These hits do not decide the grade. kumitate's `corpus/README.md` at `21:31:18` and kaidoku's at `05:11:06` and kotoba's at `21:23:07` are real top-level `corpus/README.md` paths; lane-authored commits still decide those rows.

### MORI-R1-SILENCE-009 — six report files were last committed by protocol-shokunin

Observation. kasegi, kengaku, kake, kotoba, kagi, kama report paths last change in the main repo at `cb3c103` `protocol-shokunin` `2026-10-14T21:24:03-03:00`. That attributes the report landing, not the child-repo work after 21:21. Child-repo grades above do not use that author as the lane's author.

### MORI-R1-SILENCE-010 — driver round counters are not the baseline

Observation. `.ufo/state/*.round` contents at the 21:30:51 batch: kasegi 17, kengaku 13, kake 16, kumitate 16, kotoba 16, kagi 16, kama 1, plus protocol 14 and aggregator 10. Latest report rounds are higher (kasegi 20, kengaku 16, kake 19, kumitate 17, kotoba 19, kagi 19, kama 4). No state file for audio, game-dev-2d, game-dev-3d, lore, revenger, kaidoku. Counters were not the comparison baseline. Using them would compare HEAD against a stale driver number, not against the report dir.

## Outside the grade set

Not graded. Inventory only, from the 21:30:51 report scan, not rechecked at the freeze.

`shokunin.conf` `LANES` also names protocol, aggregator, tameshi, mado, tsukuroi, tabi, mori, chousa. protocol had a report at `.ufo/reports/round-15/protocol.md` (mtime 2026-10-13T16:44:48.522301). aggregator had `.ufo/reports/round-11/aggregator.md` (mtime 2026-10-14T18:50:11.719144). tameshi, mado, tsukuroi, tabi, mori, chousa had zero `<id>.md` under `.ufo/reports/`. A missing report for a non-roster id is not a silent grade in this seat. mori is on probation and is not in `MANIFEST.json` `roster`.

## Limits

- The freeze is not an atomic snapshot. kumitate HEAD moved from `85b2b70` (21:35:41) to `f6d6272` (21:36:50) during measurement. game-dev-3d `watch.log` was written during the walk. Grades that depend on a lane commit in the window, or on a file class newer than the report, held at the recheck. Exact tip hashes will not.
- `git log %h` abbreviations are not full object ids.
- Unattributed means `git log -1` empty or porcelain `??`, not a witnessed writer. progressing on audio, game-dev-2d, and game-dev-3d does not identify who wrote the new files.
- Ignored files are included, because the protocol probe is `find -not -path '*/.git/*'`, not `git ls-files`.
- This seat did not apply the two-tick stale actuator, did not read launch lines as the baseline, and did not record `failed`.

## What would change a later comparison

Keep the ids. Compare again against each lane's own report file mtime, not the shared directory mtime. Treat a missing report as `unavailable`. Do not flip kaidoku, or any other row, to silent because the tip is hours old. Do not call a `ci` tip progressing-weak when unattributed files under that repo are newer than the report, and do not call that tip a lane-identity commit.
