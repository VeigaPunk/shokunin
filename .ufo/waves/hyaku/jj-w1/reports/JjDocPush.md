# JjDocPush — `jj git push` semantics in 0.45.x, and what they mean for `jj-lane.sh`

Seat: JjDocPush-2 (leaf, no subagents). Sandbox: `/fast/scratch/jj-wave/JjDocPush/`.
Binary: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` (`~/.local/bin/jj`), git 2.56.0.
Nothing was run against `/home/vgpnk/Projects/shokunin` or any lane repo: every experiment used a
fresh `git init --bare origin` + `git clone` + `jj git init --colocate` under the sandbox, with
`origin` always a sandbox bare repo (`git remote -v` checked). No installs or upgrades were needed.

Primary sources used:
- local CLI: `jj help git push`, `jj help -k bookmarks`, `jj help -k revsets` (0.45.1);
- version-matched docs: <https://docs.jj-vcs.dev/v0.45.0/bookmarks/> (this site *does* publish
  per-release docs; `/0.45/` and `/0.45.0/` are 404, `latest` is the same page);
- source at the tag: `cli/src/commands/git/push.rs`, `lib/src/git.rs`, `cli/src/git_util.rs`
  (<https://github.com/jj-vcs/jj/tree/v0.45.1>);
- `CHANGELOG.md` at the tag.

---

## 1. Which bookmarks does `jj git push` push?

**Answer.** With no selector, only *tracked* bookmarks/tags whose target is in
`remote_bookmarks(remote=<remote>)..@` — i.e. commits reachable from `@` that are not ancestors of
the last-fetched remote positions. A new local bookmark that was never pushed/fetched is *considered*
by that revset but then refused, because it is untracked. `--bookmark`, `--tag`, `--revision`,
`--change`, `--named` select explicitly; `--all`, `--tracked`, `--deleted` select sets.

Citation — `jj help git push` (local 0.45.1):
> "By default, pushes tracking bookmarks and tags pointing to `remote_bookmarks(remote=<remote>)..@`."

Source — `push.rs:1318-1331`, `find_default_target_revisions`:
```rust
// remote_bookmarks(remote=<remote>)..@
let expression = RevsetExpression::remote_bookmarks(
    RemoteRefSymbolExpression { name: StringExpression::all(), remote: StringExpression::exact(remote) },
    None,
)
.range(&RevsetExpression::working_copy(workspace_name.to_owned()))
.intersection(
    &RevsetExpression::bookmarks(StringExpression::all())
        .union(&RevsetExpression::tags(StringExpression::all())),
);
```
The `.intersection(bookmarks()|tags())` is why an unbookmarked `@` can never be pushed by the default
revset: it is in the range but not selected.

Experiment (`exp1`; origin has `c1`, local `main` moved to a fresh `c2`, `feat` on `@`=`c3` and never
tracked):
```
$ jj git push --dry-run
Warning: Refusing to create new remote bookmark feat@origin
Hint: Run `jj bookmark track feat@origin` and try again.
Changes to push to origin:
  bookmark: main [move forward from f3a5b41df38c to 5aaf446ec054]
Dry-run requested, not pushing.
$ jj git push --tracked --dry-run
Changes to push to origin:
  bookmark: main [move forward from f3a5b41df38c to 5aaf446ec054]
$ jj git push --all --dry-run
Changes to push to origin:
  bookmark: feat [add to a808367146d8]
  bookmark: main [move forward from f3a5b41df38c to 5aaf446ec054]
```

Bookmarks not reachable from `@` are excluded (`exp8`: `orphan` on `root()`, `@` back on `main`):
```
$ jj log -r 'remote_bookmarks(remote=origin)..@' --no-graph -T 'commit_id.short() ++ " " ++ bookmarks ++ "\n"'
bb4368167164
$ jj git push --dry-run
Warning: No bookmarks/tags found in the default push revset: remote_bookmarks(remote=origin)..@
Nothing changed.
$ jj git push --bookmark orphan --dry-run
Changes to push to origin:
  bookmark: orphan [add to aa00072c22d6]
```

Descendants past the named bookmark are **not** pushed — `exp1`, after `jj git push --bookmark main`
(`main`=`c2`, `feat`/`@`=`c3` a child of `c2`):
```
$ git -C ../origin.git log --format='%h %s' --all
5aaf446 c2
f3a5b41 c1
$ git -C ../origin.git cat-file -t tuxzkkwy
fatal: Not a valid object name tuxzkkwy
```
which matches the help text:
> "Any descendant commits beyond the reference are not pushed."

Note the precise revset semantics (`jj help -k revsets`): `x..y` is `::y ~ ::x`, so the *remote
bookmark's own commit* is excluded, and its ancestors are excluded; a local bookmark pointing at or
behind the remote position is therefore never selected by the default push.

## 2. Lease and safety checks

**Answer.** The push is a **force push guarded by a lease on the last-fetched position**, not a
fast-forward push. Safety checks before any ref is moved/created/deleted: (1) lease — the remote must
still be where jj last saw it; (2) the local bookmark must not be conflicted; (3) an existing remote
bookmark must be tracked; (4) every commit being pushed must be "ready" (non-empty description unless
`--allow-empty-description`, author+committer set, no conflicts unless `--allow-conflicts`, not
private unless `--allow-private`).

Citations — `jj help git push`:
> "This is similar to `git push --force-with-lease` - the remote is updated only if its current state matches what Jujutsu last fetched."

> "If the local reference has changed from the last fetch, push will update the remote reference to the new position after passing safety checks."

Docs, v0.45.0 bookmarks → *Pushing bookmarks: Safety checks*:
> "jj will contact the remote and check that the actual state of the remote bookmark matches jj's record of its last known position."

> "The local bookmark must not be conflicted."

> "If the remote bookmark already exists on the remote, it must be tracked."

Source — `lib/src/git.rs:3421-3423`, inside `push_updates`:
```rust
// We always force-push. We use the push_negotiation callback in
// `push_refs` to check that the refs did not unexpectedly move on
// the remote.
refspecs.push(RefSpec::forced(new_target.to_string(), &update.qualified_name));
```

### 2a. The lease refuses a push when the remote moved since the last fetch (`exp3`)
Local `main` = `656fde7` (`lane c2`, child of `c1`); another actor pushed `2a2b4f2` (`remote c3`,
also child of `c1`) into origin after our clone:
```
$ jj git push --bookmark main
Changes to push to origin:
  bookmark: main [move forward from bf962669e15a to 656fde7bbd60]
Warning: The following references unexpectedly moved on the remote:
  refs/heads/main (reason: stale info)
Hint: Try fetching from the remote, then make the bookmark point to where you want it to be, and push again.
Error: Failed to push some bookmarks
[exit 1]
$ git -C ../origin.git log --format='%h %s' main
2a2b4f2 remote c3
bf96266 c1
```
The remote was untouched.

### 2b. The other checks (`exp3`, `exp6`, `exp9`, `exp10`)
Conflicted local bookmark:
```
$ jj bookmark list --all
main (conflicted):
  - qrvysvom bf962669 c1
  + myupwsom 656fde7b lane c2
  + sqszykqy 2a2b4f2a remote c3
$ jj git push --bookmark main
Error: Bookmark main is conflicted
Hint: Run `jj bookmark list` to inspect, and use `jj bookmark set` to fix it up.
[exit 1]
```
Untracked remote bookmark (`exp10`, after `jj bookmark untrack main@origin`):
```
$ jj git push --bookmark main
Error: Non-tracking remote bookmark main@origin exists
Hint: Run `jj bookmark track main@origin` to import the remote bookmark.
[exit 1]
```
Conflicted commit tree (`exp9`):
```
$ jj git push --bookmark confl
Error: Won't push commit 525014ff545c since it has conflicts
Hint: Rejected commit: lllroymy 525014ff confl | (conflict) (empty) merge-conflicted
[exit 1]
$ jj git push --bookmark confl --allow-conflicts     # then succeeds:
  bookmark: confl [add to 525014ff545c]
$ git -C ../origin.git ls-tree --name-only confl
.jjconflict-base-0
.jjconflict-side-0
.jjconflict-side-1
JJ-CONFLICT-README
c.txt
f1
```
Empty description (`exp5`):
```
$ jj git push --named wc=@
Error: Won't push commit 56a1dfad1a04 since it has no description
Hint: Rejected commit: mkrsxlqz 56a1dfad (empty) (no description set)
[exit 1]
```

### 2c. The checks are *not* a fast-forward requirement — a push can move a branch backwards (`exp4`, `exp11`)
There is no fast-forward requirement in the push path: the only guard is the lease.
`lib/src/refs.rs::classify_ref_push_action` compares the local and remote targets only for equality,
conflicts and trackedness — never for ancestry — and the sole `is_ancestor` call in `push.rs` (line
936) exists to label the plan line as "move forward/backward/sideways". The experiment confirms it:
`exp4`, origin `main` at `c3`, local bookmark moved back to `c2` with `--allow-backwards`:
```
$ jj bookmark set main -r 'main@origin-' --allow-backwards
Moved 1 bookmarks to wkspnztv 09850669 main* | c2
$ jj git push --bookmark main
Changes to push to origin:
  bookmark: main [move backward from 8ccb07a92043 to 09850669f6fa]
[exit 0]
$ git -C ../origin.git log --format='%h %s' main
0985066 c2
cf8b5cc c1
```
The default revset cannot do this (the behind commit is an ancestor of the remote bookmark and is
filtered out) — `exp11`:
```
$ jj bookmark set main -r 'main@origin-' --allow-backwards   # main = c1, main@origin = c2
$ jj git push --dry-run
Warning: No bookmarks/tags found in the default push revset: remote_bookmarks(remote=origin)..@
Nothing changed.
$ jj git push --bookmark main --dry-run
Changes to push to origin:
  bookmark: main [move backward from 3fe6d2f8b4e9 to 42bf55911e83]
```
So: **explicitly naming a bookmark is what gives you force-push authority over it.**

### 2d. A no-op push never contacts the remote (`exp6`)
Local `main` == `main@origin` == `b770bdf`; the remote had advanced to `b0c6139`:
```
$ jj git push --bookmark main
Bookmark main@origin already matches main
Nothing changed.
[exit 0]
$ jj log --no-graph -T 'commit_id ++ "\n"' -r 'heads(main@origin)'
b770bdf3adbd7fb896bc21afb4018bf62c95d725
$ git -C ../origin.git rev-parse main
b0c6139b7df3f6dd61f19e0d069abb129623cfb6
```
`--dry-run` behaves the same way: it prints the plan and never contacts the remote (`exp7`, with a
rejecting pre-receive hook installed: dry-run `rc=0`, real push `rc=1`).

## 3. How it handles a rejection

**Answer.** No retry, no rebase, no force upgrade. The command reports which refs were refused and
exits 1; the remote, the local bookmarks and the remote-bookmark records are left as they were. The
user (or the helper) must `jj git fetch`, reconcile, and push again.

Two distinct rejection classes, with different messages (`cli/src/git_util.rs`, `print_push_stats`):

- **lease failure** (`stats.rejected`): `Warning: The following references unexpectedly moved on the
  remote:` / `refs/heads/main (reason: stale info)` / hint "Try fetching from the remote…".
- **remote-side refusal** (`stats.remote_rejected`): `Warning: The remote rejected the following
  updates:` / `refs/heads/main (reason: pre-receive hook declined)` / hint "Try checking if you have
  permission…".

Both end in `Error: Failed to push some bookmarks`, exit 1 (see 2a for the lease case). Remote
rejection, isolated in `exp7` with `hooks/pre-receive` = `echo "policy: main is protected" >&2; exit 1`:
```
$ jj git push --bookmark main
Changes to push to origin:
  bookmark: main [move forward from 34b2b9f95730 to e4e8c98b4db0]
remote: policy: main is protected
Warning: The remote rejected the following updates:
  refs/heads/main (reason: pre-receive hook declined)
Hint: Try checking if you have permission to push to all the bookmarks.
Error: Failed to push some bookmarks
[exit 1]
$ git -C ../origin.git log --format='%h %s' main
34b2b9f c1
$ jj bookmark list --all
main: vmnvmksl e4e8c98b lane change
  @origin (behind by 1 commits): nxuunyyk 34b2b9f9 c1
```
(`remote: …` lines are git's stderr relayed verbatim, so hook output is visible.)

A second, cheaper rejection path exists *before* any network I/O: commit validation and
conflicted/untracked bookmarks are refused with `Error: …` and exit 1 (§2b), and the same warning
appears in `--dry-run` with **exit 0** (`exp1`: "Refusing to create new remote bookmark feat@origin",
"Nothing changed.", rc 0).

Deletion is a normal push: a locally deleted bookmark named via `--bookmark` (which implies
`allow_delete`, `push.rs:448`) pushes `[delete from <oid>]`; a remote that protects its default branch
answers `refs/heads/main (reason: deletion of the current branch prohibited)`, exit 1 (`exp7`).

## 4. `--allow-new`

**Answer: it does not exist in 0.45.x.** It was deprecated in 0.36.0 and removed in 0.42.0, together
with the `git.push-new-bookmarks` config.

Local evidence (`exp1` sandbox):
```
$ jj git push --allow-new --dry-run
error: unexpected argument '--allow-new' found

  tip: a similar argument exists: '--all'

Usage: jj git push --all
[exit 2]
$ jj config get git.push-new-bookmarks
Config error: Value not found for git.push-new-bookmarks
```
The 0.45.0 versioned CLI reference contains zero occurrences of `allow-new`
(<https://docs.jj-vcs.dev/v0.45.0/cli-reference/>, `grep -c` → 0).

CHANGELOG at v0.45.1, `## [0.42.0]` → *Breaking changes*:
> "The following deprecated command options have been removed:"
```
  - `jj git push --allow-new`
…
* The following deprecated config options have been removed:
  - `git.auto-local-bookmark`
  - `git.push-new-bookmarks`
```
(and `## [0.36.0]`: "The flag `--allow-new` on `jj git push` is deprecated.")

**What replaces it.** Tracking. Per `jj help git push`, `--bookmark` auto-tracks a bookmark that is
not tracking anything, and `--all`/`--change`/`--named` create+track. The rule is narrower than it
sounds — `push.rs:446-451`:
```rust
// Override allow_new if the bookmark is not tracked with any remote
// already. The user has specified --bookmark, so their intent which
// bookmarks to push is clear.
let allow_new = !has_tracked_remote_bookmarks(tx.repo(), name);
```
i.e. `--bookmark X` may *create* `X@origin` only if `X` tracks no remote at all. Experiment (`exp10`,
`main` tracks `origin`, a second remote `backup` added):
```
$ jj git push --remote backup --bookmark main
Error: Refusing to create new remote bookmark main@backup
Hint: Run `jj bookmark track main@backup` and try again.
[exit 1]
```
Versus `exp1`, where `feat` tracked nothing and `--bookmark feat` created and tracked it:
```
$ jj git push --bookmark feat
Changes to push to origin:
  bookmark: feat [add to a808367146d8]
[exit 0]
$ jj bookmark list --all
feat: tuxzkkwy a8083671 c3
  @origin: tuxzkkwy a8083671 c3
```

## 5. Remote tracking

**Answer.** A successful push updates the record of the remote bookmark (`<name>@<remote>`) and marks
it tracked; that record is what the next lease compares against. Pushing does not touch the local
bookmark. `--remote` picks the remote; it is *not* derived from what the bookmark tracks.

Citations — `jj help git push`:
> "Unlike in Git, the remote to push to is not derived from the tracked remote bookmarks."

Docs, v0.45.0 bookmarks → *Automatic tracking*:
> "When you push a local bookmark, the newly created bookmark on the remote is marked as tracked."

Experiments: §4 (`feat` becomes `@origin: …` with no explicit `bookmark track`); `exp1` after pushing
`main`, `main@origin` shows the pushed hash `5aaf446e c2`; `exp10` after `--bookmark main`:
```
$ git -C . rev-parse refs/heads/main refs/remotes/origin/main; git -C . symbolic-ref -q HEAD || echo DETACHED
aa9bb1fac3116f0e43aeb8dd273b23ddd0b33c86
aa9bb1fac3116f0e43aeb8dd273b23ddd0b33c86
DETACHED
```
The colocated Git refs are exported on push, so `git rev-parse refs/heads/<branch>` agrees with
`heads(<branch>@origin)` immediately afterwards — which is what `jj-lane.sh state` reads.

A bookmark that is *untracked on the remote side* blocks the push even when named (§2b: "Non-tracking
remote bookmark main@origin exists"), because jj will not silently adopt a remote position it has
never agreed with.

## 6. Pushing after the remote moved

Four cases, all reproduced:

1. **No fetch, local commit, remote moved** → lease refusal (`stale info`), exit 1, remote untouched
   (§2a, `exp3`).
2. **Fetch, no local commits** → the tracked local bookmark fast-forwards to the remote, push is a
   no-op, exit 0 (`exp8`):
```
$ jj git fetch --remote origin
bookmark: main@origin [updated] tracked
$ jj bookmark list --all
main: ussszzts bb2558ac other lane c2
  @origin: ussszzts bb2558ac other lane c2
$ jj git push --bookmark main
Bookmark main@origin already matches main
Nothing changed.
[exit 0]
```
3. **Fetch, local commit diverged** → the local bookmark becomes *conflicted* (3-way: base, local
   side, remote side), and push refuses until it is resolved (§2b). Note this is a **bookmark**
   conflict, not a commit conflict: no commit has a conflicted tree, so a
   `heads(bookmarks(X)) & conflicts()` guard does not see it.
4. **Fetch + rebase the unpushed commit + push** → clean forward move (`exp3`, emulating
   `jj-lane.sh`'s retry):
```
$ tip=$(jj --ignore-working-copy log --no-graph -T 'change_id ++ "\n"' -r 'heads(main@origin..bookmarks(main))' | head -1)
$ jj --ignore-immutable rebase -b "$tip" -d main@origin
Rebased 1 commits to destination.
Working copy  (@) now at: myupwsom 42e838da main* | lane c2
Parent commit (@-)      : sqszykqy 2a2b4f2a main@origin | remote c3
$ jj --ignore-working-copy bookmark set main -r "$tip"
Nothing changed.                      # the bookmark already followed the rewrite
$ jj git push --bookmark main
Changes to push to origin:
  bookmark: main [move forward from 2a2b4f2aab45 to 42e838da1a50]
[exit 0]
$ git -C ../origin.git rev-parse main
42e838da1a50d581daa49fa88db8bca90d98360c
```
Two details worth keeping: the bookmark follows the rewritten commit automatically (so
`bookmark set` is usually a no-op there), and after the push `@` became immutable (it is now trunk) and
jj auto-created a new empty working-copy commit above it:
`Warning: The working-copy commit became immutable; a new commit has been created on top of it.`

## 7. Can it ever push the working-copy commit `@`?

**Yes.** `@` is an ordinary commit; anything that names it can push it. Three routes, all reproduced in
`exp5`/`exp11`: a bookmark placed on `@` and pushed, `--named X=@`, and `-c @` (which creates
`push-<change_id>`).

```
$ jj git push --named wc=@
Error: Won't push commit 56a1dfad1a04 since it has no description     # default guard: @ is usually empty
[exit 1]
$ jj describe -m 'wc commit'
$ echo uncommitted > dirty.txt
$ jj git push --named wc=@
Changes to push to origin:
  bookmark: wc [add to c479a2b7bd78]
[exit 0]
$ git -C ../origin.git ls-tree --name-only wc
dirty.txt
f1
```

Three consequences that matter:

- **The push snapshots the working copy first**, so uncommitted changes ride along. `--ignore-working-copy`
  pushes the previous snapshot instead (`exp11`): `--named wcopy=@` produced a tree of `f1 f3.txt`,
  the normal `--named wcsnap=@` produced `f1 f3.txt f4.txt`, and afterwards **both bookmarks pointed at
  the newer commit** (`1a380ee0a27e wcopy* wcsnap`) — i.e. the snapshot rewrote the commit that had
  just been pushed.
- **A post-push rewrite moves the remote branch** because the bookmark follows rewrites and the next
  push is a force push-with-lease (`exp5`):
```
$ jj describe -m 'amended after push'
$ jj bookmark list --all
wc: mkrsxlqz 2738f9c7 amended after push
  @origin (ahead by 1 commits, behind by 1 commits): mkrsxlqz/1 c479a2b7 (hidden) wc commit
$ jj git push --bookmark wc
  bookmark: wc [move sideways from c479a2b7bd78 to 2738f9c7937b]
$ git -C ../origin.git merge-base --is-ancestor c479a2b7bd780d3610ed78d62079203c1a52cdeb wc; echo $?
1
```
  The lease passed (the remote was exactly where jj recorded it) and the previously pushed commit
  stopped being an ancestor of the branch.
- `-c @` (`exp5`) created `push-sulroqznksqx` and pushed the WC commit under that generated name.

**By default, `@` alone is never pushed** — the default revset intersects with `bookmarks()|tags()`, so
an unbookmarked `@` is not selected (`exp8`: "No bookmarks/tags found in the default push revset").

## 8. Exit-code table (for the helper's `if jj git push …; then`)

| situation | rc | distinguishing output |
|---|---|---|
| pushed | 0 | `Changes to push to origin:` + `bookmark: X [...]` |
| nothing to do (`local == remote record`) | 0 | `Bookmark X@origin already matches X` + `Nothing changed.` **no remote contact** |
| untracked new bookmark in default set | 0 | `Warning: Refusing to create new remote bookmark X@origin` + `Nothing changed.` |
| named bookmark does not exist | 0 | `Warning: No matching bookmarks for names: X` + `Nothing changed.` |
| `--dry-run` | 0 | `Dry-run requested, not pushing.` **no remote contact** |
| lease failure | 1 | `The following references unexpectedly moved on the remote:` … `(reason: stale info)` |
| remote refused (hook/permissions) | 1 | `The remote rejected the following updates:` … `(reason: pre-receive hook declined)` |
| bookmark conflicted | 1 | `Error: Bookmark X is conflicted` |
| remote bookmark untracked | 1 | `Error: Non-tracking remote bookmark X@origin exists` |
| commit not ready (desc/conflict/private) | 1 | `Error: Won't push commit …` |
| `--allow-new` | 2 | `error: unexpected argument '--allow-new' found` |

End-to-end helper emulation (`exp10`, lane `tabi`, pathspec-limited commit + bookmark set + push):
```
$ jj --config user.name=tabi-shokunin --config user.email=tabi@shokunin.local commit -m 'lane: add lane.txt' -- lane.txt
$ jj --ignore-working-copy bookmark set main -r "$(jj --ignore-working-copy log -r '@-' -T 'commit_id' --no-graph)"
Moved 1 bookmarks to yvroqmmz aa9bb1fa main* | lane: add lane.txt
$ jj git push --remote origin --bookmark main
Changes to push to origin:
  bookmark: main [move forward from cb63dea8eb44 to aa9bb1fac311]
[exit 0]
$ git -C ../origin.git log --format='%H %an <%ae> / %cn <%ce> %s' main
aa9bb1fa… tabi-shokunin <tabi@shokunin.local> / tabi-shokunin <tabi@shokunin.local> lane: add lane.txt
$ git -C ../origin.git ls-tree --name-only main
f1
lane.txt
```
The untracked `untracked.txt` in the working copy did not reach the remote, because the commit was
pathspec-limited and the push targets `@-`, not `@`.

---

## 9. Consequences for the planned shokunin integration

**[OBSERVED unless marked]**

1. **`--allow-new` cannot appear anywhere in the integration.** It is gone in 0.42.0+; `jj-lane.sh`
   does not use it and its `init` already runs `bookmark track <branch>@origin`, which is the correct
   0.45 mechanism. Nothing to change here, but any *other* lane script that still passes `--allow-new`
   dies with exit 2 before doing anything.

2. **The lease is not a fast-forward guard, so `do_push` needs an explicit ancestry guard.** `jj` will
   happily move `main` backwards (exp4) or sideways (exp5) when the remote still matches the recorded
   position. `jj-lane.sh`'s first attempt sets the bookmark to the new `@-` and pushes without first
   checking that `<branch>@origin` is an ancestor of the new tip. If a lane repo's base is behind what
   it has already fetched (e.g. `init` on a stale clone, or a lane whose bookmark was reset), the
   lease *passes* and the shared branch is rewound, breaking "a cited hash stays an ancestor of the
   branch". One pre-flight line closes it, e.g.
   `git -C "$dir" merge-base --is-ancestor refs/remotes/origin/$branch refs/heads/$branch` (the
   colocated refs are kept in sync by jj — `exp8` after a fetch: `git rev-parse refs/heads/main
   refs/remotes/origin/main` printed the same new commit for both, and `exp10` after a push likewise),
   or the equivalent revset
   `jj log -r 'heads(<branch>@origin) & ::<branch>'` being non-empty. If the check fails: fetch,
   rebase, retry — never push.

3. **Never push `@`; only push the committed `@-`.** The helper already does this correctly (exp10:
   only the pathspec-limited commit is pushed, `untracked.txt` stays local). But it is worth writing
   down *why*: pushing `@` snapshots the dirty working copy into the pushed commit (exp5 `dirty.txt`)
   and any later `jj` command that rewrites `@` drags the bookmark along, so the next push rewrites
   the remote branch "sideways" and the cited hash stops being an ancestor (exp5). The same applies to
   `jj metaedit`/`jj describe`/`jj rebase` on any already-pushed commit. The helper's
   `metaedit --update-author` runs on `@` *before* committing, which is safe; it must never be added
   after a push.

4. **`do_push` should distinguish the two rejection classes.** On a lease failure, fetch + rebase +
   retry is exactly right (exp3 case 4 works). On `The remote rejected the following updates` (hook,
   protection rule, permissions, `denyDeleteCurrent`) the retry loop rebases a no-op and burns three
   attempts before exiting 3. Recommend failing fast on that string with exit 3 and a message that
   names the remote reason. The stderr file is already captured in `$STATE/jj-push.err`, so the match
   is cheap.

5. **"pushed" is not proven by exit 0.** Three exit-0 paths push nothing: `already matches`,
   `No matching bookmarks`, and `--dry-run` (the latter never contacts the remote). The helper prints
   `pushed $(heads(<branch>@origin))`, and in the `already matches` case the record may be stale
   relative to the real remote (exp6: printed `b770bdf`, remote was `b0c6139`). Since "landed =
   committed AND pushed before a report cites the hash", either (a) require
   `Changes to push to origin:` in the output before printing `pushed`, or (b) after an `already
   matches`, treat the hash as "was pushed earlier" rather than "just pushed", or (c) re-fetch before
   citing. Also: `do_push` currently prints `pushed ` with an empty hash if the push was a no-op for a
   bookmark revset that does not resolve — guard on a non-empty hash.

6. **A failed `--named` push leaves no bookmark behind**, and a failed push leaves the remote
   record unchanged (exp7, exp11), so retries are safe and idempotent by construction. That is the property the
   helper's 3-attempt loop depends on.

7. **`@` changes identity around a push.** When the pushed commit becomes `trunk()`'s tip, jj reports
   "The working-copy commit became immutable; a new commit has been created on top of it" (exp3,
   exp10). Anything that caches `@` across a `do_push` call is wrong; the helper's `commit` re-reads
   `@-` after its own `jj commit`, so it is unaffected.

8. **Fleet-root commits** should stay on `scripts/hyaku/fleet-commit.sh` (git + flock): nothing in this
   study shows jj push is safer there, and the rewind property (§2c) makes a shared root branch more,
   not less, dangerous under a force-push-with-lease model. `jj-lane.sh`'s use on lane branches, with
   the ancestry guard from (2), is the narrow safe surface.

## 10. Open uncertainties

- Only `jj 0.45.1` was exercised (no 0.45.0 binary available); the 0.45.0 docs page was used for
  citations and matches the 0.45.1 source at the tag, but I did not diff 0.45.0 vs 0.45.1 behavior.
- Not tested: tags, `--option`, `--allow-private`, partial success when several bookmarks are pushed
  and only some are refused, HTTPS/auth remotes, `git.push` config precedence, remote-side deletion
  of the branch between fetch and push, and pushes where the remote updates only some refs.
- Not tested: `sign_commits_before_push` (source `push.rs` `sign_commits_before_push`) — it *rewrites*
  commits immediately before pushing when signing is configured, which would make a hash read before
  the push stale. The lane repos have no signing config, so this is [INFERENCE] from source only.
- The docs' "a few cases where `jj git push` will succeed even though the remote bookmark is in an
  unexpected location" were not enumerated experimentally.
- Concurrency between two lanes pushing the same branch at the same time was not raced on purpose; the
  lease makes one of them lose with `stale info` [INFERENCE from §2a], and `jj-lane.sh`'s `flock` only
  serializes pushes inside one host.
- `--bookmark` patterns are globs (`jj help git push`); I tested only exact names. A branch name
  containing `*`/`?` would not be passed by `jj-lane.sh` (lane ids are `[a-z0-9-]`), but `detect_branch`
  derives the name from git, so an unusual branch name is untested.

---

Preserved sandboxes for the two hazards cited above:
`/fast/scratch/jj-wave/JjDocPush/exp4` (backward push) and `/fast/scratch/jj-wave/JjDocPush/exp11`
(default push cannot rewind; `--ignore-working-copy` pushes the stale `@`; post-push snapshot rewrites
the pushed commit). All other experiment directories were removed.
