# JjDocWorktrees — jj 0.45.x colocated repos with `git worktree` checkouts

Seat: JjDocWorktrees-2 (leaf scout). Date: 2026-10-20.
Target question: for jj 0.45.x, how do Git worktrees and jj colocated repos interact — what breaks or is
safe when a colocated repo also has `git worktree` checkouts, as the fleet root's `.tower/worktrees` does?

## Environment and method

- `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` (`~/.local/bin/jj --version`), `git version 2.56.0`.
- All jj commands ran only in `/fast/scratch/jj-wave/JjDocWorktrees/` (`e1`–`e9`). No jj command was run
  in `/home/vgpnk/Projects/shokunin` or any live lane repo; live-repo access was read-only
  (`cat`, `grep`, `ls`, `git -C … log/show/ls-files/rev-parse/status/diff/worktree list`).
- Citations use the v0.45.1 docs (the `jj-vcs.github.io/jj/v0.45.1/*` URLs 302 to `docs.jj-vcs.dev/v0.45.1/*`;
  both were checked with `curl -w '%{http_code}'` → 200) and the pinned release source commit
  `7c41cdeb16b6b321c64e789a966b6adf723816a5`.
- Sandbox removed after reporting: `/fast/scratch/jj-wave/JjDocWorktrees` deleted, no installs needed.

## Verdict in one paragraph

jj does not support Git worktrees as jj working copies (docs: “git-worktree: No”), and a linked Git
worktree cannot host a jj repo at all. But a jj **colocated** main repo and linked Git worktrees can
coexist: jj skips nested worktree directories during snapshotting (their `.git` file marks a reserved
name), imports the branches the worktrees have checked out, and leaves their indexes alone. The sharp
edge is ref export: whenever jj moves or deletes a branch that a linked worktree has checked out — via
`jj bookmark set/delete`, a rewrite, or `jj git fetch` fast-forwarding a **tracked** bookmark — jj
updates the ref and silently **detaches that worktree's HEAD** at its old commit. The worktree then
still looks clean and `git status` passes, but `git push origin <branch>` no longer carries its work,
and commits made on that detached HEAD are invisible to jj and are not ancestors of the branch. For
shokunin: lane repos must stay real clones (the helper already requires a `.git` directory), the fleet
root should stay non-colocated while `.tower` fleets run, and `jj workspace add` cannot replace
`.tower/worktrees` because jj workspaces have no `.git` and break every git-based lane tool.

## Findings (observed)

### F1. jj cannot operate inside a linked Git worktree, and refuses to colocate one

Docs: “**git-worktree: No.** However, there's native support for multiple working copies backed by a
single repo.” — `https://docs.jj-vcs.dev/v0.45.1/git-compatibility/#supported-features` (also the
source markdown at `docs/git-compatibility.md:65` in the v0.45.1 tree). Source: `is_linked_git_worktree`
compares `repo.git_dir() != repo.common_dir()`
(`cli/src/commands/git/init.rs#L404-L412`).

```console
$ cd /fast/scratch/jj-wave/JjDocWorktrees/e1-wt   # linked worktree of the colocated e1 repo
$ ~/.local/bin/jj st
Error: There is no jj repo in "."
$ ~/.local/bin/jj root
Error: There is no jj repo in "."
$ ~/.local/bin/jj git init --colocate .
Error: Cannot create a colocated jj repo inside a Git worktree.
Hint: Run `jj git init` in the main Git repository instead, or use `jj workspace add` to create
additional jj workspaces.
```

`~/.local/bin/jj workspace add ../e5-wt --name wtasws` at an existing worktree path also fails:
`Error: Destination path exists and is not an empty directory`.

Consequence: a `.tower/worktrees/<fleet>/<id>` checkout can only ever be driven by git, never by jj.

### F2. Colocating a repo that already has linked worktrees succeeds and leaves them intact

```
$ git worktree add ../e5-wt -b feat           # before jj init
HEAD is now at c886f00 init
$ ~/.local/bin/jj git init --colocate .
Done importing changes from the underlying Git repo.
Initialized repo in "."
$ cat .git/worktrees/e5-wt/HEAD
ref: refs/heads/feat
$ ~/.local/bin/jj bookmark list
feat: pqvkqmvy c886f00a init
master: pqvkqmvy c886f00a init
$ git -C ../e5-wt status --porcelain
                                                # (empty)
```

So the worktree keeps its symbolic HEAD; its branch is imported as a jj bookmark. (Observed in `e5`.)

### F3. jj's snapshot never descends into a nested worktree — even with the default `all()` auto-track

```
$ cd e2 && git worktree add .tower/worktrees/lane1 -b lane1
Preparing worktree (new branch 'lane1')
$ (cd .tower/worktrees/lane1 && echo lane > lane.txt && git add lane.txt && git commit -qm "lane1 work")
$ ~/.local/bin/jj st                       # e2 has default snapshot.auto-track (all())
Done importing changes from the underlying Git repo.
The working copy has no changes.
Working copy  (@) : mwrnykux cf62af5c (empty) (no description set)
Parent commit (@-): zxykntvq ec7c5d8c master | init
$ ~/.local/bin/jj file list | grep tower
.tower/worktrees/.keep
$ git status --porcelain
?? .tower/worktrees/lane1/
```

The mechanism is the reserved-name rule in the snapshot walker: a directory containing any of
`RESERVED_DIR_NAMES = [".git", ".jj"]` is skipped
(`lib/src/local_working_copy.rs#L821`, and `#L1631-L1641`: “we ignore all nested repos entirely”).
A linked worktree's `.git` is a file, and the check is `symlink_metadata().is_ok()`, so file-vs-directory
does not matter. A nested `jj workspace` (which carries `.jj`) is skipped the same way (`e3`, `e9`).

### F4. Worktree branch commits are imported and visible to jj

```
$ ~/.local/bin/jj bookmark list         # in e2, after the lane1 commit
lane1: mzqmmwwr cf520265 lane1 work
master: zxykntvq ec7c5d8c init
$ ~/.local/bin/jj log --no-graph -r 'all()' -T 'commit_id.short() ++ " " ++ bookmarks ++ "\n"'
cf520265936e lane1
cf62af5c57be
ec7c5d8c53c4 master
```

`jj op log` in `e1`/`e5` shows the corresponding `import git refs` and `import git head` operations
(the latter matches the 0.45.0 per-worktree HEAD tracking). Repeated `jj st` with no Git-side activity
adds **no** operations: 10 ops before 3× `jj st`, 10 after; one snapshot with a modified file added
exactly 1 (`snapshot working copy`). So a busy fleet of worktrees only feeds the jj op log when it
actually commits.

### F5. Index and HEAD are per-worktree; a jj command in the main repo does not disturb them

```
$ (cd e2/.tower/worktrees/lane1 && echo staged >> lane.txt && git add lane.txt && git status --porcelain)
M  lane.txt
$ (cd e2 && ~/.local/bin/jj st >/dev/null)          # jj command in main
$ git -C e2/.tower/worktrees/lane1 status --porcelain
M  lane.txt                                          # staged entry survived
$ cat e2/.git/worktrees/lane1/HEAD
ref: refs/heads/lane1
$ (cd e2 && echo c > c.txt && ~/.local/bin/jj commit -m "main work")
$ cat e2/.git/HEAD
d7be109ba48aa021d9abcde18e738af5ab5640e5             # main detached at @-
$ cat e2/.git/worktrees/lane1/HEAD
ref: refs/heads/lane1                                # linked worktree untouched
```

This matches the design: linked worktrees have their own `HEAD` and `index` under
`.git/worktrees/<name>/`, and jj only resets the index of the workspace it runs in.

### F6. jj moving or deleting a checked-out branch detaches that worktree's HEAD (never rewrites its files)

`jj bookmark set wt-branch -r @` while `e1-wt` had `wt-branch` checked out:

```console
$ cat .git/worktrees/e1-wt/HEAD
ref: refs/heads/wt-branch
$ ~/.local/bin/jj bookmark set wt-branch -r @
Warning: Target revision is empty.
Moved 1 bookmarks to rrxpyzxm 9540ad08 wt-branch* | (empty) (no description set)
$ cat .git/worktrees/e1-wt/HEAD
2ae03ba7e178cf921e316e24428c411935958f53         # detached at the old commit
$ git -C ../e1-wt rev-parse --abbrev-ref HEAD
HEAD
$ git -C ../e1-wt status --short
                                                 # (empty)
$ git rev-parse refs/heads/wt-branch
9540ad08dc3e8c20a27ba2d071093351cb7e30b2
```

`jj bookmark delete feat` while `e5-wt` had `feat` checked out: `Deleted 1 bookmarks.`, worktree HEAD
became `c886f00a04cb39befaf1b21c2d9ed48f82b9f295`, `git show-ref | grep refs/heads/feat` → no such ref,
worktree status still empty. Source: `export_refs` enumerates every worktree and calls
`check_and_detach_head`, which calls `update_git_head(...)` when the checked-out ref's new oid differs
(`lib/src/git.rs#L1348-L1399`). Changelog 0.39.0: “`jj` now safely detaches the `HEAD` of alternate Git
worktrees if their checked-out branch is moved or deleted during Git export.”
(`https://github.com/jj-vcs/jj/blob/v0.45.1/CHANGELOG.md`.) This is file-safe but silent: nothing is
printed, `git status` stays clean, and the checkout silently stops being on its branch.

### F7. `jj git fetch` triggers the same detach when the bookmark is tracked

`e4` has a bare `origin`; `lane1` is tracked (`jj bookmark track lane1@origin`). After advancing
`origin`'s `lane1` via `git commit-tree` + `update-ref`:

```console
$ R=../e4-remote.git
$ base=$(git --git-dir=$R rev-parse refs/heads/lane1)
$ tree=$(git --git-dir=$R rev-parse 'refs/heads/lane1^{tree}')
$ c=$(git --git-dir=$R -c user.name=remote -c user.email=r@e commit-tree $tree -m "remote advance" -p $base)
$ git --git-dir=$R update-ref refs/heads/lane1 $c
remote lane1 advanced to 38bb351f43d5faebe1dcbbe1457a5b47dc2b9e3d
$ ~/.local/bin/jj git fetch --remote origin
bookmark: lane1@origin [updated] tracked
$ git rev-parse refs/heads/lane1
38bb351f43d5faebe1dcbbe1457a5b47dc2b9e3d        # was 39f85ca5…
$ cat .git/worktrees/l1/HEAD
39f85ca59ac2f75d63a6cd3a4ad8fb649f37f474        # detached at the pre-fetch commit
$ git -C .tower/worktrees/l1 rev-parse --abbrev-ref HEAD
HEAD
$ git -C .tower/worktrees/l1 status --porcelain
                                                 # (empty)
```

Counter-case: with the bookmark **untracked** (`jj bookmark untrack`, then remote advanced again),
`jj git fetch` reported `bookmark: lane1@origin [updated] untracked`, local `refs/heads/lane1` stayed at
`38bb351f…`, and `cat .git/worktrees/l1/HEAD` stayed detached as before — no new detach, no local ref
move. So fetch-side detach risk exists only for tracked bookmarks that jj fast-forwards.

### F8. After a detach, a branch push silently succeeds while carrying nothing

From the detached `e4` lane worktree after making a commit there:

```console
$ git rev-parse HEAD
342eb55c6ee5330b9e156088074829abad07dfad
$ git push origin lane1
Everything up-to-date
$ git --git-dir=/fast/scratch/jj-wave/JjDocWorktrees/e4-remote.git rev-parse refs/heads/lane1
38bb351f43d5faebe1dcbbe1457a5b47dc2b9e3d
$ git --git-dir=... merge-base --is-ancestor 342eb55c… refs/heads/lane1
fatal: Not a valid commit name 342eb55c6ee5330b9e156088074829abad07dfad
NO - detached lane work never landed
```

Plain `git push` in that state prints Git's detached-HEAD error (loud), but an explicit
`git push origin <branch>` is the silent form. This is the exact failure shape that would break the
shokunin invariant “landed = committed AND pushed before a report cites the hash”.

### F9. Commits reachable only from a worktree's detached HEAD are invisible to jj

```
$ (cd e1-wt && echo detached >> a.txt && git -c user.name=lane -c user.email=l@e commit -qam "detached lane work")
$ git rev-parse HEAD
03134e381aab8a78f8f04389f1b534400bf815d5
$ ~/.local/bin/jj log --no-graph -r 'all()' -T 'commit_id.short() ++ " " ++ bookmarks ++ "\n"'
9540ad08dc3e wt-branch
2ae03ba7e178 master
000000000000
$ ~/.local/bin/jj log -r 03134e381aab8a78f8f04389f1b534400bf815d5
Error: Revision `03134e381aab8a78f8f04389f1b534400bf815d5` doesn't exist
$ git merge-base --is-ancestor 03134e38… master; echo rc=$?
rc=1
```

The object exists in the shared object database (`git cat-file`/`git rev-parse` still resolve it), but
nothing in `refs/*` points at it, so jj's ref scan never imports it and it is not an ancestor of any
branch. A lane reporting such a hash would fail both a jj-based and a git-ancestor gate.

### F10. A worktree directory that loses its `.git` pointer is snapshotted as ordinary files

Removing only the `.git` file of `e2/.tower/worktrees/lane1` (e.g. a partially cleaned/pruned
worktree with files left behind), with default auto-track:

```console
$ rm .tower/worktrees/lane1/.git
$ ~/.local/bin/jj st
Working copy changes:
A .tower/worktrees/lane1/.tower/worktrees/.keep
A .tower/worktrees/lane1/a.txt
A .tower/worktrees/lane1/lane.txt
```

Minimal isolation of the same mechanism (`e8`): `mkdir leftover; echo secret > leftover/f.txt`;
`jj st` → `A leftover/f.txt`; git index → `100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0 leftover/f.txt`
(the empty blob = Git intent-to-add, which the helper's init comment also describes), then
`git commit -qam "fleet commit"` committed `leftover/f.txt` into HEAD (`git ls-tree -r --name-only HEAD`
contains it). Guards:
- `snapshot.auto-track="none()"` (`e6`): `jj st` printed `Untracked paths: ? .tower/worktrees/l1/` and
  `jj file list` had no `worktrees/l1` entries — no auto-add.
- `.git/info/exclude` containing `.tower/` (`e7`): `jj st` → “The working copy has no changes.” and
  `jj file list | grep tower` → none. jj honors the repo exclude file for untracked discovery.

Docs context: “All new files in the working copy that don't match the ignore patterns are tracked by
default.” — `https://docs.jj-vcs.dev/v0.45.1/config/#snapshotauto-track`.

### F11. A jj mutation detaches the main repo's Git HEAD; a later `git commit` then commits off-branch

```
$ # e9, fresh colocated repo, HEAD attached to master at init
$ cat .git/HEAD              → ref: refs/heads/master
$ jj st                      → ref: refs/heads/master
$ jj describe -m described   → ref: refs/heads/master
$ jj new                     → 7a4b732768483965aa55090a0ba95d22b7aeaa8e   (detached)
$ git switch -q master       → ref: refs/heads/master
$ jj st                      → ref: refs/heads/master
$ jj new -m x                → 13a3ed09a0fd1390b194d6a785c1d8b8c6adb851   (detached again)
```

In `e2`, after `jj commit`, `git commit -qam` created `001c91f…`; `git rev-parse master` was still
`ec7c5d8c…` and `git merge-base --is-ancestor 001c91f master` exited 1 (`NO - detached git commit is
not on master`). Docs: “Before doing mutating Git commands, you may need to tell Git what the current
branch should be with a `git switch` command.”
(`https://docs.jj-vcs.dev/v0.45.1/git-compatibility/#colocated-jujutsugit-repos`.)

### F12. jj workspaces are not git worktrees and cannot carry git-based tooling

```
$ ~/.local/bin/jj workspace add ../e3-ws --name ws1
Created workspace in "../e3-ws"
$ ls -la ../e3-ws
drwxr-xr-x .jj
-rw-r--r-- a.txt
$ ls ../e3-ws/.jj
repo
working_copy
$ ls -d ../e3-ws/.git
ls: cannot access '../e3-ws/.git': No such file or directory
$ git -C ../e3-ws status
fatal: not a git repository (or any parent up to mount point /)
$ git -C . worktree list
/fast/scratch/jj-wave/JjDocWorktrees/e3 8a76d4d [master]     # jj workspace absent
$ ~/.local/bin/jj workspace list
default: . mlzonrxn 35f643ba (empty) (no description set)
ws1: ../e3-ws vrulnzrv ab9b6fda (empty) (no description set)
```

`jj workspace --help`: “Workspaces let you add additional working copies attached to the same repo.”
Glossary: “This is what Git calls a ‘worktree’.” and for colocated repos “`jj` and `git` commands can be
used interchangeably.” (`https://docs.jj-vcs.dev/v0.45.1/glossary/#workspace` and `#colocated-repos`).
A nested jj workspace (`.tower/ws2`) is also skipped by the main snapshot (`jj st` no changes) and
appears to git only as `?? .tower/`.

### F13. In a colocated repo, explicit `jj git import` / `jj git export` are no-ops

```
$ ~/.local/bin/jj git export
No export needed in colocated workspaces.
$ ~/.local/bin/jj git import
No import needed in colocated workspaces.
```

Changelog 0.44.0: “`jj git import` and `export` in colocated workspaces are now disabled by default.”
Import/export happen automatically on every jj command instead.

## jj workspace vs `git worktree` — comparison

| Axis | jj workspace (`jj workspace add`) | linked `git worktree` |
| --- | --- | --- |
| Documented as | “native support for multiple working copies backed by a single repo” | “git-worktree: No” for jj |
| Metadata in the directory | `.jj/` only (`repo` pointer + `working_copy`) | `.git` **file** pointing to `.git/worktrees/<name>` |
| Usable by git tools | No (`fatal: not a git repository`) | Yes |
| Usable by jj | Yes (own `@`, `jj workspace list/update-stale/forget`) | No (`Error: There is no jj repo in "."`) |
| Branch model | no branch needed; each workspace has its own working-copy commit | must check out a branch or detached commit |
| Shared state | repo, commits, bookmarks, operation log, sparse patterns per workspace | objects and `refs/*`; per-worktree `HEAD`, index, reflog |
| jj's view of the other | — | branch refs imported as bookmarks; per-worktree HEAD imported |
| jj ref export touching it | n/a | moving/deleting its checked-out ref detaches its HEAD (F6) |
| Nested inside a working copy | skipped by snapshot (`.jj` reserved) | skipped by snapshot (`.git` reserved) |
| Convert between them | no; `jj git init --colocate` refuses in a worktree; `jj workspace add` refuses a non-empty dir | — |

## Consequences for the planned shokunin integration

1. **Lane repos must remain standalone clones — not `git worktree` checkouts.** jj cannot colocate a
   linked worktree (F1), and `scripts/hyaku/jj-lane.sh` already enforces the same by requiring a real
   `.git` directory: `[ -d "$dir/.git" ] || { err "not a git repo: $dir"; exit 1; }` (`cmd_init`).
   The live probe lane is consistent: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/chousa-shokunin`
   has `.git/` as a directory (config `remote.origin.url = /home/vgpnk/Projects/shokunin/chousa-shokunin`),
   so it is a clone, not a worktree. If a lane were ever provisioned as a worktree, `jj-lane.sh init`
   would refuse at its first check — good, but dispatchers should not rely on that error as the design.
2. **Keep the fleet root non-colocated while `.tower` fleets run (this wave's plan is supported).**
   The live root has no `.jj` and one worktree (`git worktree list` → only the main checkout). The
   moment a jj mutation runs in a colocated root, Git HEAD detaches (F11); `fleet-commit.sh` then does
   `git add` + `git commit` + `git push origin HEAD:master`, producing a commit that is on the remote
   `master` but **not** on the local `master` ref. Local ancestor checks, `git merge-base`, and the
   “cited hash stays an ancestor of the branch” invariant would then disagree with the remote. If the
   root is ever colocated, restrict jj there to read-only commands (`jj st/log/bookmark list`), which
   F11 shows do not detach HEAD.
3. **`.tower/worktrees` checkouts are safe from snapshot absorption, but not from ref export.**
   Creating a tower-style worktree from a colocated root works normally
   (`git worktree add -b tower/fleet/m1 ../e2-tower-m1 HEAD` succeeded; jj then showed
   `tower/fleet/m1` as a bookmark), and jj never walks into the tree (F3). But any jj command in the
   root that moves or deletes a `tower/*` branch — `jj bookmark set/delete`, a rebase rewriting the
   checked-out commit, or `jj git fetch` fast-forwarding a **tracked** bookmark of that name (F6/F7) —
   silently detaches that mission's worktree HEAD. Tower's own verification
   (`git -C <worktree> status --porcelain`) stays clean, so the detach is invisible; a later
   `git push origin tower/<fleet>/<id>` can then report success while carrying nothing (F8). Tower
   branches are normally local-only (never tracked), which bounds the fetch path, but explicit
   bookmark operations must be forbidden in a colocated root.
4. **Do not substitute `jj workspace add` for `.tower/worktrees`.** A jj workspace has no `.git`, so
   every tower/fleet contract that shells out to git in the checkout (status gates, `fleet-commit.sh`,
   push, `merge-base` checks, `git rev-parse HEAD`) fails outright (F12). jj workspaces are only usable
   by jj-driven work; Git worktrees remain the only substrate that both git and the fleet tooling can
   read.
5. **Keep the two-layer orphan guard if the root is ever colocated.** `.tower/` is already in the live
   root's `.git/info/exclude` (line 8), and F10/e7 shows jj honors that exclude file, so leftover tower
   directories are not auto-tracked. Add repo config `snapshot.auto-track="none()"` as the belt-and-
   braces equivalent of `jj-lane.sh init`'s setting: without either guard, an orphaned worktree
   directory (`.git` file lost during a failed cleanup) is absorbed into `@`, written to Git's index as
   intent-to-add, and a later broad `git commit -a` lands its files in the fleet repo (F10/e8).
6. **Worktree-only hashes must never be cited.** If a worktree is detached (by jj or by anything else),
   commits made there are outside jj's `all()` and outside every branch (F9). A lane closure that cites
   one fails the “ancestor of the branch” gate; the wave's existing rule “landed = committed and pushed
   before citing” remains the right guard, and `jj-lane.sh`'s post-push re-read of
   `<branch>@origin` is the correct pattern.

## Open uncertainties

- **Concurrency race (untested under load).** Docs: “bugs when interleaving mutating `jj` and `git`
  commands, usually having to do with a branch pointer”
  (`…/git-compatibility/#colocated-jujutsugit-repos`). I did not reproduce a concurrent
  `jj bookmark/fetch` vs. worktree `git commit` race; the observed detach behavior is sequential. A
  root-level fetch racing a worktree commit on the same tracked branch could plausibly leave the pointer
  at either commit. [INFERENCE]
- **Inaccessible worktrees.** `into_repo_with_possibly_inaccessible_worktree()` silently skips a
  worktree jj cannot open (`lib/src/git.rs#L1396-L1398`), so its checked-out ref could be moved without
  the detach step. Not tested (requires permissions setup). [INFERENCE]
- **Unborn-branch worktrees.** A worktree whose branch has no commit (rare here) was not tested; the
  detach code treats an unborn ref as absent.
- **`jj git push` while a worktree has the pushed branch checked out.** Not tested; jj does not move
  local refs on push, so no detach is expected. [INFERENCE]
- **`git worktree prune`/`repair` paths.** I simulated the dangerous end state by deleting the `.git`
  file (F10) but did not run `git worktree prune` itself; a pruned registration whose directory remains
  is exactly the F10 absorption case.
- **Version drift.** 0.45.0's changelog says per-worktree Git HEAD tracking “prepares colocated
  repositories for support of multiple Git worktrees” — i.e. real multi-worktree colocation is future
  work, not present support. Behavior may change in 0.46+; re-test before adopting.
- **Scope.** Linux only (no Windows/macOS); git 2.56 only (jj's minimum is 2.41); no measurement of
  import/op-log cost with dozens of worktrees and hundreds of refs, beyond the “import ops only on
  actual Git changes” observation in F4.

## Tooling installs

None. No pacman/uv/npx/cargo/npm installs or upgrades were performed. All documentation was fetched
with `curl` and parsed with the system `python3`; the sandbox used the already-installed
`jj 0.45.1` and `git 2.56.0`.

## Sandbox

Removed: `/fast/scratch/jj-wave/JjDocWorktrees/` (all experiments `e1`–`e9` were self-contained; every
cited output is reproduced verbatim above, so no failure state needed preserving).
