# JjTrialFleetRoot — fleet-root jj colocation trial

Seat: JjTrialFleetRoot · Date: 2026-10-20 · jj 0.45.1 (`~/.local/bin/jj`)
Sandbox: `/fast/scratch/jj-wave/JjTrialFleetRoot/` (`remote.git` = bare clone of
live fleet root; `fleet/` = clone + rsync of live untracked/ignored content,
`*-shokunin/` and `.tower/worktrees` excluded). Remote URL verified as the
sandbox bare repo before every push (`origin /fast/scratch/jj-wave/JjTrialFleetRoot/remote.git`).
Sandbox retained: it preserves the pushed empty commit `ea5e6fd` cited below.

## Findings (observed)

### F1 — Init order matters; wrong order poisons `@` and the git index
First attempt ran `jj git init --colocate`, then `jj config set` (no
`--ignore-working-copy`). Observed: `jj status` then showed 49 untracked paths
as `A` in `@`, and `git status --porcelain` jumped from 12 to **148** lines —
all ` A` (intent-to-add) entries including `.ufo/state/*` and `.tower/*`:
```
$ jj config set --repo user.name protocol-shokunin   # snapshots with default auto-track=all()
$ git status --porcelain | wc -l   → 148
```
This reproduces the exact hazard the helper's comment describes. Cleanup with
`jj file untrack` was wrong — it marks tracked files `D` in jj's view
(`.ufo/watchdog.log` showed `D` in `jj diff -r @` while still on disk).
Correct cleanup: `jj restore` after `auto-track="none()"` is persisted.
**Second attempt** (helper order: `jj --config 'snapshot.auto-track="none()"' git init --colocate .`,
then all config sets with `--ignore-working-copy`) still tracked untracked files
on the *first later* `jj status`, because `--config` on init does NOT persist —
it covered only the init snapshot. `jj restore` again cleaned it. [INFERENCE]
The helper's init works because its `--ignore-working-copy config set` lands
before any user snapshotting command; any tool that runs a snapshotting jj
command between init and the config-set will still trigger this. Recommend
jj-lane.sh init remain the only entry point, and fleet-root init use the same helper.

### F2 — `jj status` cost
~14–48 ms real on the fleet-root-shaped repo (51 dirty/untracked paths):
`real 0m0.014s`, `0m0.048s`, `0m0.020s` across three runs. Negligible.

### F3 — HEAD attachment lifecycle
- Immediately after `jj git init --colocate`: `git symbolic-ref HEAD` →
  `refs/heads/master` (attached), `HEAD == master == bee791e`.
- After pure snapshotting commands (`jj status`, `jj file track`, `jj describe`,
  `jj restore`): HEAD stayed **attached** in test A (attached through `jj status`
  after the first git commit).
- After the first `jj commit` + `bookmark set` + `jj git push`: HEAD becomes
  **detached**, pointing at the moved master tip:
  ```
  $ git symbolic-ref HEAD → fatal: ref HEAD is not a symbolic ref
  $ git rev-parse HEAD master → b794a4bc / f17486ff   (HEAD ahead, master lagged)
  ```
  Then the next `jj status` imported and moved `refs/heads/master` to HEAD's
  commit; HEAD stays detached at the master tip thereafter (verified: `git
  branch --show-current` empty, `HEAD==master==origin/master`).
- Consequence: `@{u}`, `git branch --show-current`, `symbolic-ref HEAD` all
  break permanently after the first jj writer touches the repo. `git rev-parse
  master`, `rev-list`, `log`, `status`, `push HEAD:master` all keep working —
  fleet-commit.sh's sequence is entirely HEAD-relative (`git add -- <paths>`;
  `git commit -m -- <paths>`; `git rev-list --count $REMOTE/$BRANCH..HEAD`;
  `git push HEAD:$BRANCH`) and observed working fine detached (commits
  ccf767b, bbd512d, 703b040, and a no-op `push ok` when HEAD==tip).

### F4 — Mixed writers, serialized (no interleave): PASS
- git writer while colocated (HEAD attached): `git add -- f && git commit -m --
  f` → `[master f17486f]`, push `bee791e..f17486f HEAD -> master`. Next `jj
  status` imported cleanly: `@` rebased to `f17486f`, master bookmark moved.
- git writer while HEAD detached (after jj commit): identical — `[detached HEAD
  ccf767b]`, push `b794a4b..ccf767b`, jj import moved `refs/heads/master` to
  `ccf767b`. No lost commit, no divergent bookmark.
- jj writer (`file track --include-ignored` → `metaedit --update-author` →
  `commit -m -- <paths>` → `bookmark set master -r @-` → `jj git push
  --bookmark master`): commit `b794a4b` author `protocol-shokunin
  <protocol@shokunin.local>`, remote moved `f17486f..b794a4b`. Pathspec-limited
  confirmed: only the named file in the commit.

### F5 — The git-index reset race: FAIL (the decisive result)
- A jj **mutation** between `git add` and `git commit` resets the git index
  (`jj --rebuild-index`-style sync). Observed twice:
  1. `git add JjFleetRootRaceY.md` → `jj describe -m desc` → staged count
     `1 → 0`, file → `??`. Harmless on its own (file still on disk; `git add`
     + commit afterward worked).
  2. Real race (scripted: git writer `add` → sleep 0.3 → `commit`; jj writer
     `file track`/`describe` inside the window):
     ```
     staged-at-commit-time: 0
     error: pathspec '.ufo/.../JjRaceGitY.md' did not match any file(s) known to git
     ```
     The git commit was **not made at all**. The file stranded on disk until
     later recovered via `jj file track` + `jj commit`.
- `jj status` alone did NOT destroy staged entries (staged blob survived; `AM`
  state preserved). Only jj mutations do.
- Corollary: `jj file track` writes the tracked file into the git index as
  ` A` (observed `JjRaceJjX.md` as ` A` right after `jj describe` re-exported).
  A pathspec-limited `git commit -- <paths>` does NOT sweep it (verified in
  `703b040`: tree contains only Y, not X). A bare `git commit`/`-a` would.

### F6 — jj can create and PUSH an empty commit: FAIL-grade footgun
When `jj commit -m ... -- <path>` ran on a path that was (by then) untracked in
jj's view, jj produced an **empty** commit and `jj git push` pushed it:
```
commit ea5e6fda74cc — parent 703b040, tree fc2547c == parent's tree  (EMPTY)
$ git cat-file -p ea5e6fd → parent 703b040… ; tree identical to parent's
Changes to push to origin:  bookmark: master [move forward from 703b040 to ea5e6fd]
```
No error anywhere; the commit message claims content that is not there. The
helper is protected by its `jj diff --summary -- <paths>` gate ("nothing to
commit"); a bare `jj commit -- <path>` has no such gate, and `git commit`'s
analogous protection ("pathspec did not match") actively *fails* rather than
silently no-ops. [INFERENCE] A fleet-root `jj commit` path copied from the
helper but missing the diff gate (or `file track`) would cite pushed hashes for
changes that never landed — direct violation of the `landed` invariant.

### F7 — Concurrency under one flock (serialized): mixed results
Serialized flock sequence `git add+commit+push` then `file track+commit+
bookmark+push` landed both commits (`703b040`, then real X commit `6d0af81`
after the earlier empty one). BUT the empty-commit incident happened *inside
this serialized sequence* because the two writers' views of "tracked" diverge:
`jj commit` emptiness must be detected and retried, exactly like the helper does.

## PASS/FAIL table

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | `jj git init --colocate` on fleet-root clone | PASS | init ok; but see #2 |
| 2 | auto-track isolation from first snapshot | PASS* | only via helper order + `--ignore-working-copy` config sets; one careless command poisons `@` (F1) |
| 3 | `jj status` cost | PASS | 14–48 ms |
| 4 | git commit lands on master (attached HEAD) | PASS | `f17486f` on master, pushed |
| 5 | git commit lands correctly with detached HEAD | PASS | `ccf767b` → `push HEAD:master` ff'd remote; `master` caught up on next jj import |
| 6 | next jj command imports git commit cleanly | PASS | `@` rebased, bookmark moved, no conflicts |
| 7 | jj writer full cycle (track/metaedit/commit/bookmark/push) | PASS | `b794a4b` pushed, correct author |
| 8 | `@{u}`-style tooling survives | FAIL | detached HEAD breaks `symbolic-ref HEAD`, `@{u}`; only head-agnostic git ops survive (F3) |
| 9 | git staged entries survive jj snapshot | PASS | `jj status` preserved staged blob |
|10 | git staged entries survive jj **mutation** | FAIL | index reset → `commit -- <path>` hard-fails "pathspec did not match"; commit lost (F5) |
|11 | parallel writers under one flock, serialized | PARTIAL | both landed, but produced a pushed **empty** commit `ea5e6fd` when tracked-state diverged (F6/F7) |
|12 | `jj commit` refuses no-change pathspec | FAIL | silently creates empty commit; `jj git push` ships it (F6) |
|13 | pathspec-limit invariant | PASS | `git commit -- <paths>` did not sweep jj's ` A` staged entries |
|14 | pushed-hash citeable / no rewrite | PASS | all pushes fast-forward; no amend observed |

## Recommendation: **colocate the fleet root, keep git-only writers** (option 3)

Converting fleet-root commits to jj is not safe yet:

- F5 is a live-gun race: jj lane commits already run inside the fleet repo's
  parent process space in six concurrent rounds; any colocated-jj mutation at
  the fleet root between fleet-commit.sh's `git add` and `git commit` loses
  that commit silently-ish (commit errors, but the file becomes `??` and the
  run continues). Fleet-root jj usage would multiply the exposure surface, not
  reduce it.
- F6 shows a bare `jj commit -- <paths>` can push an *empty* commit while
  claiming content — only the helper's diff-gate prevents it. Replicating the
  helper's discipline into every fleet-root writer site is new code that gains
  nothing over the existing, tested `fleet-commit.sh`.
- Detached HEAD (F3/F4) is survivable for fleet-commit.sh specifically because
  it is HEAD-relative, but only because nothing in `scripts/` reads
  `symbolic-ref HEAD`/`@{u}` for the fleet root (verified: only jj-lane.sh
  does, for lanes, with a fallback).

Colocating while keeping writers git-only buys: `jj log`/`jj status`
introspection for the orchestrator, and a colocated lane ecosystem that matches
the lane repos. Costs: the permanent detached HEAD (harmless to
fleet-commit.sh, verified), and the standing requirement that **no jj mutation
command ever runs at the fleet root during a fleet commit** — enforce by making
fleet-root jj usage read-only (`--ignore-working-copy`) by convention, since a
snapshotting command alone does not damage the index but every mutation does.
If fleet-root jj writes are ever wanted, they must go through a helper with the
same diff-gate + flock + bookmark-set + conflict-check shape as jj-lane.sh —
NOT ad-hoc `jj commit`.

## Installs
None (jj 0.45.1 already at `~/.local/bin/jj`; pacman transactions paused host-wide).

## Residual risks / blockers
- [INFERENCE] jj's index reset is atomic against git's view but git's `add` is
  not retried by fleet-commit.sh; a lost-commit window exists whenever any jj
  mutation overlaps the ~ms-scale add→commit gap. Rate is low (mutations are
  rare vs. read-only snapshots) but nonzero.
- Empty-commit hazard (F6) needs a regression guard if any future fleet-root jj
  writer is added: assert `jj diff --summary` non-empty pre-commit AND assert
  `git ls-tree <hash> <path>` post-push before citing a hash.
- Sandbox at `/fast/scratch/jj-wave/JjTrialFleetRoot/` retained (contains the
  pushed empty commit `ea5e6fd` on `remote.git` as evidence).
