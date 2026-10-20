# JjDocRecovery — rollback/backout in jj 0.45.x, removing `.jj`, divergence and conflicted bookmarks

Seat: JjDocRecovery-2 · Date: 2026-10-20 · Tool versions: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, `git 2.56.0`.
Sandboxes: `/fast/scratch/jj-wave/JjDocRecovery/{A,A2,A3,B,C1,C2,C3,C4}`. No tool installs or upgrades were needed. No `jj` command was run with cwd/`-R` under `/home/vgpnk/Projects/shokunin`; live repos were only read with `git -C … log/rev-parse`.

All sandbox repos were configured with `snapshot.auto-track="none()"` and per-repo `user.name`/`user.email`, mirroring `scripts/hyaku/jj-lane.sh`. The operator's global jj config contributed `git.auto-local-bookmark = true` to these tests (it is in the output excerpts, e.g. automatic bookmark tracking).

---

## Findings

### 0. Premise correction: `jj op undo` does not exist in 0.45.1

```
$ jj help op undo
error: unrecognized subcommand 'undo'

  tip: a similar subcommand exists: 'abandon'

Usage: jj operation [OPTIONS] <COMMAND>
```

`jj operation --help` lists exactly: `abandon`, `diff`, `integrate`, `log`, `restore`, `revert`, `show`.

Citation — CHANGELOG 0.39.0 (https://github.com/jj-vcs/jj/blob/v0.45.0/CHANGELOG.md):
> The deprecated command `jj op undo` has been removed. Use `jj op revert` or `jj undo`/`redo` instead.

So the 0.45.x rollback surface is four commands, not two:

| command | scope |
|---|---|
| `jj undo` | revert the **last** operation (repeat to walk backwards) |
| `jj redo` | re-apply the most recently undone operation |
| `jj op restore <op-id>` | restore the **whole repo** to any earlier operation |
| `jj op revert <op-id>` | apply the inverse of **one specific** operation, anywhere in history |

`jj help undo`:
> If used once after a normal (non-`undo`) operation, this will undo that last operation by restoring its parent.

`jj help op restore`:
> This restores the repo to the state at the specified operation, effectively undoing all later operations.

Citation — Operation log docs (https://docs.jj-vcs.dev/latest/operation-log/):
> It also lets you restore the entire repo to the way it looked at an earlier point (`jj op restore`).

---

### 1. `jj undo` / `jj redo` — exact behaviour

Recipe:
```sh
jj --ignore-working-copy op log --no-graph -T 'id ++ "\n"'   # newest first, full operation ids
jj --ignore-working-copy op log -d                          # what each operation changed
jj undo                       # undo the newest operation
jj undo                       # undo the one before it, etc.
jj redo                       # put the most recently undone operation back
```

Experiment A (`A/work`: origin bare repo; `c1` committed and pushed; bookmark `main` moved by hand — the helper's sequence):

```
$ jj undo
Warning: Undoing a push operation often leads to conflicted bookmarks.
Hint: To avoid this, run `jj redo` now.
Undid operation: 74fe5e1affdc (…) push bookmark main to git remote origin
Restored to operation: 8cecdb6d19f5 (…) point bookmark main to commit 12f3aac7…
--- jj bookmarks ---
main: mxlonrsn 12f3aac7 c1
  @git: mxlonrsn 12f3aac7 c1
  @origin (behind by 1 commits): mxmnlkrz f01b1723 base
--- git refs ---
refs/heads/main 12f3aac
refs/remotes/origin/main f01b172
--- remote main ---
12f3aac c1
```

Observed: `jj undo` of a push keeps the **local** bookmark at the pushed commit but rolls the recorded `main@origin` (and git's `refs/remotes/origin/main`) back to the pre-push position, while the **real remote still has the pushed commit**. jj's own warning says this "often leads to conflicted bookmarks".

Recovery from that state is a push or fetch that re-syncs the record:

```
$ jj git push --remote origin --bookmark main
Changes to push to origin:
  bookmark: main [move forward from f01b17234222 to 12f3aac718a6]
exit=0
--- bookmark list ---
main: mxlonrsn 12f3aac7 c1
  @git: mxlonrsn 12f3aac7 c1
  @origin: mxlonrsn 12f3aac7 c1
```

Second and later undos walk further back. Two undos from the state `main → c2 (eb5e81e), pushed`:

```
$ jj undo     # undoes the push
$ jj undo     # undoes "point bookmark main to c2"
Undid operation: 8c909e1b352b (…) point bookmark main to commit eb5e81ee…
Restored to operation: a0afba21c4bc (…) commit 72a36e0d…
--- bookmarks ---
main: mxlonrsn 12f3aac7 c1
--- git ---
refs/heads/main 12f3aac
refs/remotes/origin/main 12f3aac
--- remote ---
eb5e81e c2
--- worktree files ---
f.txt
f2.txt
f3.txt          # c2's file was moved back into the working copy, not lost
```

So undo of a `jj commit` is an "uncommit": the commit's content is restored as uncommitted working-copy changes (`jj commit` was the operation, not the file contents).

#### `jj undo` also rewinds mutating **git** commands

Docs (https://docs.jj-vcs.dev/latest/git-compatibility/):
> You can undo the results of mutating `git` commands using `jj undo` and `jj op restore`.

Experiment (A/work): `git switch main`, then `git commit -m g1` (8ea5876), then a `jj` command imports it ("Reset the working copy parent to the new Git HEAD"). `jj undo` undid the `import git refs` operation:

```
$ jj undo
Undid operation: c3611ee03049 (…) import git refs
Restored to operation: 082ac4401629 (…) import git head
--- git rev-parse main / HEAD ---
eb5e81e
DETACHED
--- git status ---
## HEAD (no branch)
?? f4.txt
--- jj ---
main: vnsxtyyz eb5e81ee c2
```

`refs/heads/main` was rewritten from `8ea5876 g1` back to `eb5e81e c2`; HEAD was detached at g1 (`git rev-parse --short HEAD` → `8ea5876`, reflog shows `8ea5876 HEAD@{0}: export from jj`), and g1 survives only because jj holds it:

```
$ git for-each-ref --contains 8ea5876e --format='%(refname)'
refs/jj/keep/815a07881747e2012a1453dd5b4bd20b181f5de3
refs/jj/keep/8ea5876eb857d7fc6885a78e4b7d1f6333e31626
```

`jj redo` restores the undone operation:

```
$ jj redo
Restored to operation: ca68c7a0ff1f (…) restore to operation 4451c1394dc4…
Working copy  (@) now at: nvtxmuxr 304a42f1 (empty)
Parent commit (@-)      : qvquxzqo afbecd08 main | base
Added 0 files, modified 0 files, removed 2 files
```

#### Undo rewrites the working copy

Experiment A3: a tracked, uncommitted file `u.txt` was created, then `jj op restore <op before u.txt>`:

```
$ jj op restore c6c2a8432078…
Restored to operation: c6c2a8432078 (…) revert operation 818fd0e70d66…
Working copy  (@) now at: qxzpxzqz 0c998b2d (empty)
Parent commit (@-)      : wknwsxwv f295acd4 c3
Added 0 files, modified 0 files, removed 1 files
--- files ---
base.txt f1.txt f2.txt f3.txt          # u.txt deleted from disk

$ jj undo
Added 1 files, modified 0 files, removed 0 files
--- files ---
base.txt f1.txt f2.txt f3.txt u.txt
$ cat u.txt
uncommitted work
```

Uncommitted-but-tracked work is removed from disk by `undo`/`op restore` and comes back with `jj undo`. Untracked files are not part of jj's trees and are untouched (B: `wip.txt` survived `rm -rf .jj`; A/work's untracked `f4.txt` survived the restores).

---

### 2. `jj op restore` — whole-repo rollback, `--what` matters

Recipe:
```sh
jj --ignore-working-copy op log --no-graph -T 'id ++ "\n"'        # full ids
jj --ignore-working-copy op log -d                                # inspect op diffs
jj --at-op=<op-id> --ignore-working-copy log -r 'all()'           # preview state at that op (read-only)
jj op restore <op-id> --what repo                                 # local state only; remote-tracking kept
jj op restore <op-id>                                             # default: repo + remote-tracking
```

`jj help op restore` lists `--what repo` and `--what remote-tracking`, default `repo remote-tracking`, and for `remote-tracking`:
> Do not restore these if you'd like to push after the undo

Experiment A (`--what repo`, restoring from `c3` pushed back to the op before `c3`):

```
$ jj op restore 258d407895c6 --what repo
Restored to operation: 258d407895c6 (…) snapshot working copy
Working copy  (@) now at: lvylnsqq d5f7b88f (no description set)
Parent commit (@-)      : vnsxtyyz eb5e81ee main* | c2
--- bookmarks ---
main: vnsxtyyz eb5e81ee c2
  @git: vnsxtyyz eb5e81ee c2
  @origin (ahead by 1 commits): lvylnsqq/0 21ca16a9 (hidden) c3
--- git refs ---
refs/heads/main eb5e81e
refs/remotes/origin/main 21ca16a
--- remote ---
21ca16a c3
```

Then, because the tracking record still equals the real remote and the local bookmark is behind:

```
$ jj git push --remote origin --bookmark main
Changes to push to origin:
  bookmark: main [move backward from 21ca16a927d3 to eb5e81ee3291]
exit=0
--- remote still ---
eb5e81e c2
```

**`jj git push` force-rewound the remote branch backwards with no flag and exit 0**, dropping `c3` from the branch tip. The bare origin had no reflog (`git -C origin.git reflog show main` printed nothing), so the dropped commit was an unreferenced object there (`git -C origin.git cat-file -t 21ca16a927d3` → `commit` at the time, GC-able).

Experiment A2 (default `--what`, restoring past the push of `c1`):

```
$ jj op restore 4451c1394dc4
Restored to operation: 4451c1394dc4 (…) track paths
Working copy  (@) now at: nvtxmuxr 304a42f1 (empty)
Parent commit (@-)      : qvquxzqo afbecd08 main | base
Added 0 files, modified 0 files, removed 2 files
--- bookmarks ---
main: qvquxzqo afbecd08 base
  @git: qvquxzqo afbecd08 base
  @origin: qvquxzqo afbecd08 base
--- git refs ---
refs/heads/main afbecd0
refs/remotes/origin/main afbecd0
--- real remote ---
477d6c6
```

The default restore rolled back **both** the local bookmark and the remote-tracking record (jj's and git's), even though the remote still had `c1`. The next push then silently did nothing:

```
$ jj git push --remote origin --bookmark main
Bookmark main@origin already matches main
Nothing changed.
exit=0
--- remote ---
477d6c6 c1
```

The message compares the local bookmark with jj's recorded `@origin` position; the real remote was never updated (it still held `c1`), and no push happened. This is the exact state in which the helper's `do_push` would print `pushed $(heads(<branch>@origin))` — a hash that the remote does **not** have — and return success.

`jj undo` after the restore recovered everything, including files:

```
$ jj undo
Parent commit (@-)      : zmtnssxq 3e78d229 main* | c2
Added 2 files, modified 0 files, removed 0 files
--- worktree ---
f.txt one.txt two.txt
```

---

### 3. `jj op revert` — invert one operation anywhere

`jj help op revert`:
> This reverts an individual operation by applying the inverse of the operation.

Recipe: `jj op revert <op-id>` (default `@`).

Experiment A3: history `base ← c1 ← c2 ← c3 ← @`; revert the `commit c2` operation:

```
$ jj op revert 818fd0e70d66
Reverted operation: 818fd0e70d66 (…) commit 899dc1879720…
Rebased 2 descendant commits.
Working copy  (@) now at: qxzpxzqz 0c998b2d (empty)
Parent commit (@-)      : wknwsxwv f295acd4 c3
--- log ---
0c998b2d040e
f295acd4a5fe c3
899dc1879720
4964b5dfa2c0 c1
c265d736575d base
--- worktree ---
base.txt f1.txt f2.txt f3.txt
$ jj show 899dc1879720 --summary
Commit ID: 899dc1879720c4f7a5979b359791515a199ad106
Change ID: lvxlvwyptoytmttvxnprnorppmzpzqnq
    (no description set)
A f2.txt
```

The revert did **not** delete c2's content. It inverted the operation's view change: c2's description was dropped and the pre-commit working-copy commit (with `f2.txt`) was restored into the chain, with c3 and `@` rebased onto it. `jj op revert <commit-op>` is therefore **not** a content backout tool. For dropping content use `jj abandon <rev>`; for inverting a change on top of history use a normal revert commit.

[INFERENCE] Reverting a `bookmark set` operation should behave the same way — the bookmark returns to its previous target — but that specific revert was not executed; only the commit-op revert above was.

---

### 4. Removing `.jj` from a colocated repo while keeping git intact

Recipe (verified end to end):
```sh
rm -rf .jj
git switch <branch>        # HEAD is normally detached in a colocated repo
# optional: drop jj's GC-protection refs so git log --all / fsck stay clean
git for-each-ref --format='delete %(refname)' refs/jj | git update-ref --stdin
# optional: prune the now-unreferenced jj objects
git gc --prune=now -q
```

Experiment B before removal (`main` = c1, one untracked `wip.txt`, HEAD detached):

```
--- before removal ---
1c810df c1
11cfd2a
2257f07
6aa7a9a
839d4d3 base
d1fbb94
refs/heads/main
refs/jj/keep/11cfd2a38059d00c39d1dc1cd6b2ac8a619aee85
refs/jj/keep/1c810dfbdc4b301f75747f64f619e54d61e0392e
refs/jj/keep/2257f07f2172c5e4357e290df300934a0864d716
refs/jj/keep/6aa7a9aa6fb918d94538021b19a74e85b48cf6cb
refs/jj/keep/839d4d3e217415f9a4fb1a3b2fa5a99b2f8f8e04
refs/jj/keep/d1fbb94b13531c3f55433c25fbaecc57900449f9
DETACHED
1c810df
```

After `rm -rf .jj`:

```
$ rm -rf .jj && ls -a
.  ..  .git  base.txt  one.txt  wip.txt
$ git status --porcelain=v1 -b
## HEAD (no branch)
?? wip.txt
$ git log --oneline main
1c810df c1
839d4d3 base
$ git fsck --no-progress
dangling blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
dangling tree 77c90b773bcdc8967fe0712c45319ee0ac6634a8
# both are dangling-object notices; `git fsck`'s own exit status is 0 (measured separately)
```

`.git` was untouched; the only jj remnant is `.git/refs/jj` (no jj entries in `.git/config`). `git log --all` showed 6 commits for a 2-commit repo because of the keep refs. After dropping them and gc'ing:

```
$ git for-each-ref --format='delete %(refname)' refs/jj | git update-ref --stdin
$ git for-each-ref --format='%(refname)'
refs/heads/main
$ git log --oneline --all
1c810df c1
839d4d3 base
$ git gc --prune=now -q
$ git cat-file -t 2257f07f2172c5e4357e290df300934a0864d716
fatal: git cat-file: could not get object info
```

So the keep refs are the only thing protecting unbookmarked jj commits after `.jj` is gone; deleting them plus gc discards those commits permanently.

Uncommitted work survives removal (second B pass, `base.txt` modified and `new.txt` added/tracked):

```
$ jj status
Working copy changes:
M base.txt
A new.txt
A wip.txt
$ rm -rf .jj
$ git status --porcelain=v1 -b
## main
 M base.txt
 A new.txt
 A wip.txt
$ cat base.txt
modified base
$ git add -A && git commit -qm 'post-jj git commit' && git log --oneline -2
de11866 post-jj git commit
1c810df c1
$ git fsck --no-progress   # only "dangling" object lines, exit 0
```

Re-adopting the git repo afterwards (`jj git init --colocate .`) creates a **fresh** jj repo: main is imported, and the operation log contains only init operations — the old undo history is gone:

```
$ jj git init --colocate .
Done importing changes from the underlying Git repo.
Initialized repo in "."
$ jj --ignore-working-copy op log --no-graph -T 'id.short() ++ "  " ++ description ++ "\n"' | head -5
36db564f9384  snapshot working copy
71cb47905956  import git head
877f525fa9f9  import git refs
05982bbf4227  add workspace 'default'
000000000000
```

Citations: https://docs.jj-vcs.dev/latest/git-compatibility/
> Jujutsu reuses the existing Git repository as its backing store
> Commits created by `jj` have a ref starting with `refs/jj/` to prevent GC.
> jj commands will usually put the Git repo in a "detached HEAD" state

---

### 5. Divergent changes — detection and resolution

Reproduction (C2) by simulating a concurrent process with the documented `--at-op` mechanism (https://docs.jj-vcs.dev/latest/operation-log/: "There's practically no good reason to do that other than to simulate concurrent commands"):

```sh
jj describe -m 'change A'                                   # op X
jj --at-op=<op-before-X> --no-integrate-operation describe -m 'change B'
# → Operation left uncommitted because --no-integrate-operation was requested: 2581aac82c9c
jj op integrate 2581aac82c9c
```

```
$ jj log --limit 6
@  nylwpyrq/1 … b7e18542 (divergent)
│  change A
│ ○  nylwpyrq/0 … a7705b90 (divergent)
├─╯  change B
○  vllvzsqn … main f0f8a142
│  base
$ jj log -r 'divergent()' --no-graph -T 'commit_id.short() ++ " / " ++ change_id.short() ++ " " ++ description.first_line() ++ "\n"'
a7705b901d9a / nylwpyrqkxkz change B
b7e18542e2ba / nylwpyrqkxkz change A
$ jj status
Working copy  (@) : nylwpyrq/1 b7e18542 (divergent) change A
```

Resolution recipes, all exercised:

1. **Abandon the unwanted revision** (works, simplest):
```
$ jj abandon a7705b901d9a
Abandoned 1 commits:
  nylwpyrq/0 a7705b90 (divergent) change B
$ jj log -r 'divergent()' --no-graph -T 'commit_id.short() ++ "\n"'
(no output)
$ jj log --limit 4
@  nylwpyrq … b7e18542
│  change A
```
Citation — https://docs.jj-vcs.dev/latest/guides/divergence/:
> If one of the divergent commits is clearly obsolete or incorrect, simply abandon it:

2. **Give one commit a new change id** (keeps both versions):
```
$ jj metaedit --update-change-id 987105a8
Modified 1 commits:
  mxkzvlnx 4b5cff8e change D
$ jj log --limit 5
@  nylwpyrq … change A2
│ ○  mxkzvlnx … change D
```
Both commits stayed visible under distinct change ids; `divergent()` became empty.

3. **`jj converge --no-interactive`** (new in 0.45) is **not reliable unattended**. On a divergence with two different descriptions it aborted:
```
$ jj converge --no-interactive
Found 1 divergent change(s) in the specified revset:
- Change: nylwpyrqkxkz with 2 commits:
    nylwpyrq/0 a7705b90 (divergent) change B
    nylwpyrq/1 b7e18542 (divergent) change A
Attempting to converge change nylwpyrqkxkz...
Could not determine which description to use.
Error: Could not converge change
exit=1
```
`jj converge --help` says it "falls back to prompting the user if the heuristics are inconclusive"; `--no-interactive` turns that into the warning/failure seen above. The 0.45.0 CHANGELOG lists `jj converge` as the release highlight, so it is new and heuristic.

4. `jj squash --from <A> --into <B>` (documented strategy 4) — not exercised.

Revset behaviour while divergent (all verified):
```
$ jj log -r nylwpyrqkxkz
Error: Change ID `nylwpyrqkxkz` is divergent
Hint: Use change offset to select single revision: nylwpyrqkxkz/0, nylwpyrqkxkz/1
Hint: Use `change_id(nylwpyrqkxkz)` to select all revisions
Hint: To abandon unneeded revisions, run `jj abandon <commit_id>`
```
Bookmark-based revsets are equally ambiguous (`jj new main` → "Name `main` is conflicted").

---

### 6. Conflicted bookmarks — push refuses, rebase resolves

Reproduction (C1: origin bare repo, `w1` and `w2` both colocated and tracking `main@origin`). `w1` commits X and pushes; `w2` commits Y locally and then fetches:

```
$ jj git fetch --remote origin
bookmark: main@origin [updated] tracked
$ jj bookmark list --all
main (conflicted):
  - wnxknsxv e4d76d94 base
  + xvzouonu 35510ae2 Y
  + vnotnqpy ef284dc7 X
  @git (behind by 1 commits): xvzouonu 35510ae2 Y
  @origin (behind by 1 commits): vnotnqpy ef284dc7 X
Hint: Some bookmarks have conflicts. Use `jj bookmark set <name> -r <rev>` to resolve.
$ jj status
Working copy  (@) : zsytywlw d0bbf902 (empty)
Parent commit (@-): xvzouonu 35510ae2 main?? main@git | Y
Warning: These bookmarks have conflicts:
  main
```

`jj log -r main`:
```
Error: Name `main` is conflicted
Hint: Use commit ID to select single revision from: 35510ae279c8, ef284dc7880b
Hint: Use `bookmarks(main)` to select all revisions
Hint: To set which revision the bookmark points to, run `jj bookmark set main -r <REVISION>`
```

`jj git push --bookmark main`:
```
Error: Bookmark main is conflicted
Hint: Run `jj bookmark list` to inspect, and use `jj bookmark set` to fix it up.
exit=1
```

This matches the documented safety check (https://docs.jj-vcs.dev/latest/bookmarks/, same text as `jj help -k bookmarks`):
> The local bookmark must not be conflicted.

**Resolution that worked (the lane's own retry shape)** — rebase the unpushed commit onto the remote position, then push:

```
$ jj rebase -r 35510ae279c8 -d main@origin
Rebased 1 commits to destination.
Rebased 1 descendant commits.
Working copy  (@) now at: zsytywlw 1f45aec5 (empty)
Parent commit (@-)      : wnxknsxv e4d76d94 base
--- bookmarks after rebase ---
main: xvzouonu 041fc783 Y
  @git: xvzouonu 041fc783 Y
  @origin (behind by 1 commits): vnotnqpy ef284dc7 X
$ jj git push --remote origin --bookmark main
Changes to push to origin:
  bookmark: main [move forward from ef284dc7880b to 041fc783162b]
exit=0
```

The conflict collapsed as soon as the local target was rewritten onto `main@origin` (all three components — base, Y, X — resolved to the rewrite of Y). A second reproduction produced the same outcome (`main: tkxvwmzq 7256aa05 W2 / @origin (behind by 1)`).

**Discarding the local position and adopting the remote** is a single command, verified on a live conflict (C1/w2: `main (conflicted): - Z + W2 + Z2`):

```
$ jj bookmark set main -r main@origin
Moved 1 bookmarks to mxtuqoqp 6a7b4755 main* | Z2
exit=0
$ jj bookmark list --all
main: mxtuqoqp 6a7b4755 Z2
  @git: mxtuqoqp 6a7b4755 Z2
  @origin: mxtuqoqp 6a7b4755 Z2
```

This is the runtime's own hint (`Use `jj bookmark set <name> -r <rev>` to resolve`). Note the asymmetry: on a **conflicted** bookmark the fast-forward check does not block the move (the target set is ambiguous), whereas on a clean bookmark the same command refuses sideways/backward moves (next paragraph). The abandoned local commit (`W2`) stays in the repo (hidden, protected by `refs/jj/keep`) — nothing is deleted.

On a clean (unconflicted) bookmark, both `set` and `move` refuse anything but a fast-forward:

```
$ jj bookmark set main -r 2708519efd81
Error: Refusing to move bookmark backwards or sideways: main
Hint: Use --allow-backwards to allow it.
exit=1
$ jj bookmark move main --to 2708519efd81
Error: Refusing to move bookmark backwards or sideways: main
Hint: Use --allow-backwards to allow it.
exit=1
```
`jj bookmark set --help`: `-B, --allow-backwards   Allow moving the bookmark backwards or sideways`.

---

### 7. Side finding that hits the helper's push-retry directly: rebase leaves the empty working-copy commit behind

Reproduction (C4, minimal): `base ← A ← B ← @(empty)`, destination `C` also a child of `A`:

```
$ jj rebase -r 3fd08722 -d 26951bde
Rebased 1 commits to destination.
Rebased 1 descendant commits.
Working copy  (@) now at: zlnnyxxl 07c205f9 (empty)
Parent commit (@-)      : xspzrtyl 32fe1014 A
--- after ---
@  07c205f9 (empty)
│ ○  bbb2e093 B          # B' correctly rebased onto C
│ ○  26951bde C
├─╯
○  A
```

`B'` landed on `C`, but `@` was rebased onto **A** (B's old parent), not onto `B'`. The same pattern reproduced independently in C1 (`W2` rebased onto `Z`, `@` left on `Y`) and C3 (`B` rebased onto `base`, `@` left on `A`).

Consequence for a lane: after such a rebase, the next `jj commit` creates a **sibling** of the branch tip, and the helper's next step fails:

```
$ jj bookmark set main -r bbb2e093        # main -> B' (forward, fine)
$ printf 'd\n' > d.txt; jj file track d.txt; jj commit -m D -- d.txt
$ jj bookmark set main -r @-
Error: Refusing to move bookmark backwards or sideways: main
Hint: Use --allow-backwards to allow it.
exit=1
```

This is exactly the shape of `cmd_commit`: the commit is created, then `bookmark set` fails → `err "bookmark set failed"; exit 1`, leaving a created-but-unbookmarked, unpushed commit. In `do_push` the same failure just `continue`s through its three attempts and finally reports `push failed after 3 attempts`.

Why jj places the empty WC commit on the old parent is not explained by `jj help rebase`; mechanism unresolved (see uncertainties).

---

## Consequences for the planned shokunin integration

1. **Ban `jj undo` and `jj op restore` inside live lanes.** Both rewrite the working copy (deleting tracked-uncommitted files, A3 `u.txt`), roll bookmarks and git refs, and can leave remote-tracking records inconsistent with the real remote. A lane round has subagents writing files; an undo is a data-loss event for that window. Recovery in a lane should be forward-only: `jj abandon` for unpushed commits, a new commit for backouts, and `jj op restore <op> --what repo` only with the lane quiesced.

2. **The helper's "pushed hash" is only trustworthy if the record is fresh.** Two verified traps:
   - `jj undo` of a push or any restore past a push rolls `<branch>@origin` back while the remote keeps the commit.
   - With local == record != real remote, `jj git push` prints `Bookmark …@origin already matches …` / `Nothing changed.` and exits 0 **without contacting the remote** (A2). `do_push` then prints `pushed $(heads(<branch>@origin))`, a hash the remote does not have — it violates "landed = committed AND pushed".
   - With local behind and record == real remote, `jj git push` performs a **backward (force) push** and exits 0 (A: `[move backward from 21ca16a9… to eb5e81e…]`), dropping commits from the remote branch tip. That violates "pushed commits are never amended or rewritten".
   - Fix: before printing the pushed hash, or on entry to `do_push` when `state` shows anything odd, run `jj git fetch --remote origin` and read the real tip with `git ls-remote origin refs/heads/<branch>` (or at minimum `git -C <lane> rev-parse refs/remotes/origin/<branch>` *after* a fetch). Never cite `heads(<branch>@origin)` without a preceding fetch.

3. **`jj op undo` must not appear in plans, scripts, or docs** — it is gone since 0.39.0. Use `jj undo`/`jj redo` for the last op, `jj op restore` for whole-state rollback, `jj op revert` for one op. Note `jj op revert <commit-op>` is not a content backout (A3): it restores the pre-commit WC commit and rebases descendants.

4. **Conflicted bookmarks are not fatal for the lane** as long as the lane only ever rebases its unpushed commits onto `<branch>@origin` (helper's `do_push` does exactly this) — the conflict collapses and the subsequent push is a clean fast-forward (C1). But the helper must never need `bookmark set`/`move` to move sideways: if the WC commit is not at/above the bookmark target, `bookmark set` exits 1 with "Refusing to move bookmark backwards or sideways". The helper currently reports that as `bookmark set failed` after having created the commit (`cmd_commit`) — consider re-anchoring with `jj new <branch>` before the next commit, or `--allow-backwards` only with a deliberate decision (it is the flag that permits rewriting the branch).

5. **The retry path leaves the lane's working copy behind** (finding 7). After `do_push`'s fetch+rebase, `@` can sit on the pre-rebase parent while the bookmark is on the rebased commit. The next lane commit is then a sibling and its `bookmark set` fails. Recommend `do_push` end with a re-anchor (e.g. `jj new "$BRANCH"` when `@` is empty and not a parent of the branch tip) and the selftest cover "commit → push rejected → retry → commit again".

6. **Dropping jj from a colocated lane is safe and complete** for git state (B): `rm -rf .jj`, `git switch <branch>`, optionally delete `refs/jj/*` so `git log --all`/`fsck` are not polluted, then `git gc`. Costs: the operation log and change ids are gone forever, and any jj commit not reachable from a git branch/remote/keep ref is prunable. Useful as the emergency exit if jj misbehaves mid-round; it cannot be used to "roll back" jj state.

7. **Do not use `jj op restore` as a ledger for the fleet root.** The plan already keeps fleet-root commits on `scripts/hyaku/fleet-commit.sh`; this report adds no reason to change that: jj's undo/restore path can force-rewind shared branches, and `jj git push`'s safety model is "force-with-lease against jj's record", not "fast-forward only".

---

## Open uncertainties

1. **Mechanism of the empty-WC rebase placement** (finding 7). Observed in three independent sandboxes but not explained by `jj help rebase`; I did not trace it into `lib/src/rewrite.rs` far enough to name the rule. Consequence for the helper is verified; the reason is not.
2. **Undo/restore under concurrent jj processes** was not tested (that is the JjDocConcurrency seat's question). The op log is explicitly lock-free; what an `op restore` does to a concurrently running lane process is unknown here.
3. **`jj converge` on realistic lane divergence** (same description, different content; same content, different description) is untested beyond the one failing case. It prompts in interactive mode; `--no-interactive` aborted on differing descriptions.
4. **Whether a backward `jj git push` can be blocked by configuration.** I found no option in `jj git push --help`; only the record-vs-actual check exists. Not exhaustively searched.
5. **Remote-side durability of a force-rewound branch** depends on the remote's `core.logAllRefUpdates`/forge behavior. My bare test remote kept no reflog, so the dropped commit was unreferenced there; GitHub may retain it via reflogs/PR refs — unverified.
6. **`jj op revert` of a push** was inferred from the shared `--what` machinery and the undo-of-push evidence, not executed.
7. **`.jj` removal with an in-progress jj operation** (e.g. a running `jj` child) is untested; removal was done with no jj process running.
8. The docs site `latest` currently serves the 0.45.0 documentation (`https://docs.jj-vcs.dev/v0.45.0/operation-log/` serves identical content and canonicals to `latest`); if `latest` advances, the cited pages may drift. Local `jj help` excerpts are pinned to 0.45.1.
