# jj 0.45: Git HEAD attachment in a colocated repo

Ticket: how jj 0.45 handles Git `HEAD` in a colocated repo — attached or detached after
`jj commit`, `jj new`, `jj bookmark move`; when exactly jj writes `HEAD`; CHANGELOG trace.

**Environment.** jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` (`~/.local/bin/jj`),
git `2.56.0`, linux x64. All experiments ran inside a fresh sandbox under
`/fast/scratch/jj-wave/JjDocHeadAttachment/` (`exp1`…`exp12`, plus a blobless clone of the jj
repo); every `jj` invocation had a sandbox cwd, and no live repo, lane, or fleet path was
touched. Source was read from the clone, checked against tag `v0.45.1` (the tree also
carries `v0.45.0` and `v0.46.0`). No tools were installed or upgraded; nothing was needed.

## Answer summary

| Operation (colocated repo) | HEAD afterwards | Notes |
|---|---|---|
| `jj git init --colocate` on an existing git repo | **attached** (`refs/heads/<branch>`) | No HEAD write: recorded `git_head` already equals `@-`. |
| `jj commit` (incl. `jj commit -- <paths>`) | **detached at the new commit**, i.e. at `@-` | Branch bookmark is *not* moved; HEAD is one commit ahead of the branch until `jj bookmark set`. |
| `jj new` | **detached at the old `@`** (now `@-`) | |
| `jj bookmark move` / `jj bookmark set` | **unchanged** if HEAD is already detached; if HEAD is attached to the moved bookmark, **detached at the pre-move oid** | Never re-attaches HEAD to a branch. |
| `jj status`, read-only `--ignore-working-copy` reads | unchanged | No transaction, no HEAD write. |
| `jj describe` (parent unchanged) | unchanged | Only writes when `@-` differs from the recorded `git_head`. |
| `jj git push` | unchanged | Observed mtime-stable; push drives bookmarks, not HEAD. |

jj writes HEAD from `reset_head()` — on transaction finish, when a fresh immutable
working-copy commit is created during snapshot, and in `jj workspace update-stale` — and from
`check_and_detach_head()` during ref export. `update_git_head()` always writes an object
target, i.e. a detached HEAD; jj only ever sets a symbolic HEAD for the special unborn
placeholder.

## Findings (observed)

### F1. `jj git init --colocate` leaves HEAD attached

```console
$ git init -q -b main exp1 && cd exp1
$ git config user.name T && git config user.email t@e
$ echo a > a.txt && git add a.txt && git commit -qm init
$ jj git init --colocate
Done importing changes from the underlying Git repo.
Initialized repo in "."
$ git symbolic-ref -q HEAD
refs/heads/main
$ git rev-parse --short HEAD
7620f92
$ jj log -r 'all()' --no-graph -T 'change_id.short() ++ " " ++ commit_id.short() ++ "\n"'
lqnkmynukmll be0698d99e39 empty       # @, parent 7620f92
ypnsvunwwtqz 7620f9281d1d nonempty
zzzzzzzzzzzz 000000000000 empty
```

The new working-copy commit `be0698d9` has parent `7620f92` (the Git commit); the recorded
`git_head` equals that parent, so `reset_head()` has nothing to write. In an **unborn** repo
(`git init` with no commits) HEAD also stays symbolic after init (`exp8`):

```console
$ git symbolic-ref -q HEAD
refs/heads/main
$ git rev-parse --short HEAD
fatal: Needed a single revision
```

### F2. `jj commit` detaches HEAD at the committed commit (`@-`)

```console
$ jj commit -m c1
Working copy  (@) now at: ywtzrvuq e8e953c0 (empty) (no description set)
Parent commit (@-)      : lqnkmynu 3b7aac10 (empty) c1
$ git symbolic-ref -q HEAD || echo DETACHED
DETACHED
$ git rev-parse --short HEAD
3b7aac1
$ jj log -r @- --no-graph -T 'commit_id.short()'
3b7aac10
$ git rev-parse --short main
7620f92
```

So immediately after `jj commit`: `HEAD == @- ==` the commit the helper prints, while the
branch still points at the old tip. A contiguous run (`exp12`) of `jj commit`, `jj new`,
`jj describe`, `jj bookmark move` names the writer; `describe` and `bookmark move` added no
entry:

```console
$ jj commit -m c1
$ jj new -m n1
$ jj describe -m n1-described
$ jj bookmark move main --to @-
$ git symbolic-ref -q HEAD || echo DETACHED
DETACHED
$ git rev-parse --short HEAD
464333a
$ git reflog --format='%gd %gs' | head -6
HEAD@{0} export from jj
HEAD@{1} export from jj
HEAD@{2} commit (initial): init
```

The helper-style path-limited call (`exp10`) behaves identically, and shows the author caveat
that motivated `jj metaedit --update-author`:

```console
$ jj --config user.name=lane-1-shokunin --config user.email=lane-1@shokunin.local commit -m "partial commit" -- a.txt
Parent commit (@-)      : yqvpwwyv 9aea3579 partial commit
$ git symbolic-ref -q HEAD || echo DETACHED
DETACHED
$ git rev-parse --short HEAD   # == @-
9aea357
$ git rev-parse --short main   # unchanged
aab31da
$ jj diff --summary -r @       # uncommitted remainder stays in @
M b.txt
$ jj log -r @- --no-graph -T 'author.name() ++ " <" ++ author.email() ++ ">"'
Joao Pedro Veiga <jpveigao10@gmail.com>
```

### F3. `jj new` detaches HEAD at the previous `@`

Continuing `exp1`:

```console
$ jj new -m n1
Working copy  (@) now at: rrmmrrkn b5046c30 (empty) n1
Parent commit (@-)      : ywtzrvuq e8e953c0 (empty) (no description set)
HEAD-symbolic-ref: DETACHED
HEAD-oid: e8e953c
```

`e8e953c` is exactly the commit that was `@` before the command.

### F4. `jj bookmark move` never attaches HEAD; it detaches a symbolic HEAD at the *pre-move* oid

Detached case (`exp6`, filesystem mtime of `.git/HEAD`, 1.1 s gaps):

```console
after init                   HEAD=84c456e mtime=2026-10-20 11:19:52.295325087 -0300
after jj status              HEAD=84c456e mtime=2026-10-20 11:19:52.295325087 -0300
after jj describe            HEAD=84c456e mtime=2026-10-20 11:19:52.295325087 -0300
after jj commit              HEAD=21ba900 mtime=2026-10-20 11:19:56.838144982 -0300
after jj new                 HEAD=762b5e7 mtime=2026-10-20 11:19:57.953144738 -0300
after jj bookmark move       HEAD=762b5e7 mtime=2026-10-20 11:19:57.953144738 -0300
after jj bookmark set @      HEAD=762b5e7 mtime=2026-10-20 11:19:57.953144738 -0300
```

Attached case, branch moved **backwards** (`exp2`, HEAD attached to `main` at `c2`):

```console
$ jj bookmark set main -r @-- --allow-backwards
Moved 1 bookmarks to ynxqxutl 4117ae0a main* | c1
HEAD now: DETACHED @ c2a1938       # the OLD branch tip, not the new target 4117ae0
bookmark main -> 4117ae0
```

Attached case, branch moved **forward** (`exp4`, `jj bookmark set main -r @`):

```console
HEAD=c1 9f412ee  HEAD=refs/heads/main
$ jj bookmark set main -r @
Moved 1 bookmarks to pqtuqpxt f70d2e4c main* | (empty) (no description set)
HEAD now: DETACHED @ 9f412ee       # still the old tip
main -> f70d2e4
```

### F5. `jj status` and `jj describe` do not write HEAD when `@-` is unchanged

`exp6` mtime rows above: `jj status` and `jj describe` left `.git/HEAD` byte-for-byte and
mtime-identical; only `commit` and `new` moved it. `exp1` step 6 shows the same with HEAD
temporarily re-attached by `git checkout main` where `main == @-`: after `jj describe`, HEAD
was still `refs/heads/main`.

### F6. `jj git push` does not write HEAD

`exp10` with a sandbox bare origin:

```console
$ jj commit -m second -- b.txt && jj --ignore-working-copy bookmark set main -r @-
pre-push: HEAD=bbd40c0 main=bbd40c0 remote=aab31da
$ jj git push --remote origin --bookmark main
Changes to push to origin:
  bookmark: main [move forward from aab31da15008 to bbd40c0371a1]
$ stat -c %y .git/HEAD      # identical before and after
2026-10-20 11:23:02.134391767 -0300
post-push: HEAD=bbd40c0 main=bbd40c0 remote=bbd40c0
```

### F7. An external `git checkout` is imported and re-parents `@`

`exp5`: after `jj commit -m lane-c1` (HEAD detached at `0923883`, `main=782f77b`), a
`git checkout main` re-attached HEAD, then `jj status` produced an `import git head` operation
and `jj describe -m lane-c2` landed on a **new** commit whose parent is `782f77b`; `lane-c1`
survived as a sibling anonymous head:

```console
$ git checkout -q main
HEAD=refs/heads/main @ 782f77b
$ jj status
$ jj describe -m lane-c2
HEAD=refs/heads/main @ 782f77b
$ jj log -r 'all()' --no-graph -T '...'
nmvlknrqvqxq 136654e79805 lane-c2 parents=782f77bc18b6
wzkqkrumlynq 092388392b04 lane-c1 parents=782f77bc18b6
mqkupnnvyxnn 782f77bc18b6 c1      parents=000000000000
$ jj op log -n 4
aa8a21465e20 describe commit ...
fea06bb3c466 import git head
55fd9b74b690 commit ...
958d6feb8a06 import git head
```

### F8. `--ignore-working-copy` does not suppress HEAD writes for mutating commands

`exp7`: `jj --ignore-working-copy new -m n` moved HEAD from `acfe9fb` to `b2483fe`
(mtime changed), because `finish_transaction()` still runs `reset_head()`.

## Mechanism (source at tag `v0.45.1`)

- `lib/src/git.rs#L1780` — `update_git_head()` doc: “Ensures Git HEAD is detached and pointing
  to the `new_oid`.” The implementation writes `gix::refs::Target::Object(oid)`; the only
  symbolic target is the unborn `UNBORN_ROOT_REF_NAME` placeholder. jj therefore **never**
  re-attaches HEAD to a branch.
- `lib/src/git.rs#L1839-L1888` — `reset_head()` doc: “Sets Git HEAD to the parent of the
  given working-copy commit and resets” the Git index. It computes
  `new_head_target = first_parent(@)` (absent when the parent is the root) and writes only
  when `mut_repo.git_head(workspace)` differs from it. This comparison is against the
  *recorded view*, not the file on disk; external git changes are imported first (F7).
- `cli/src/cli_util.rs#L2394-L2395` — `finish_transaction()` calls `try_reset_git_head()` for
  every committed colocated transaction; `try_reset_git_head` (`#L2727`) is a thin wrapper
  around `reset_head()`.
- `cli/src/cli_util.rs#L2190` — the snapshot path calls `try_reset_git_head()` when the
  working-copy commit became immutable and a fresh one was created on top (the #9827 fix).
- `cli/src/cli_util.rs#L695` — `jj workspace update-stale` resets Git HEAD to the parent of
  the fresh working-copy commit (the #9936 fix).
- `lib/src/git.rs#L1348` — `check_and_detach_head()` inside `export_some_refs()`: if HEAD is
  symbolic to a bookmark/tag that this export updates or deletes, it rewrites HEAD to the
  ref's **current (pre-export) oid**, i.e. detaches without moving the checked-out commit.
- `lib/src/git.rs#L1174` — `import_head()` only records the new HEAD in the view; the CLI's
  `import_git_head()` (`cli/src/cli_util.rs#L1385`) additionally `check_out`s the new HEAD
  commit, re-parenting `@` and abandoning a discardable working-copy commit, then prints
  “Reset the working copy parent to the new Git HEAD.”

## CHANGELOG trace

Cited against `https://github.com/jj-vcs/jj/blob/v0.45.1/CHANGELOG.md`; line numbers are for
that tag's file.

- **0.6.0 — 2022-12-05, L5279:** “We now keep it if a detached HEAD refers to it.” First
  changelog recognition that a detached Git HEAD is a normal, importable state.
- **0.7.0 — 2023-02-16, L5262:** first colocation mention (bug in branch export “when running
  in a working copy colocated with Git”). Detached-HEAD-on-export behavior is already implicit.
- **0.8.0 — 2023-07-09, L4910:** “`git checkout` (without using `jj`) in colocated repo no
  longer abandons the previously checked-out anonymous branch” (#1042); internal
  `set_git_head_target()` unification (`5218591a`, first tag `v0.8.0`).
- **0.9.0 — 2023-09-06:** docs begin advertising colocation and warn about the detached HEAD
  (“docs: make co-located repos more prominent, more details”, `18bcc877`, first tag
  `v0.9.0`). No dedicated changelog entry.
- **0.10.0 — 2023-10-04:** `reset_head()` extracted as a function (`7ccbc042`, first tag
  `v0.10.0`) — refactor of existing behavior, not a behavior change.
- **0.15.0 — 2024-03-06, L4128:** “`jj git init --colocate` can now import an existing Git
  repository” — the lane setup path used by shokunin.
- **0.23.0 — 2024-11-06, L3150:** “The `HEAD@git` symbol no longer resolves to the Git HEAD
  revision.” `HEAD` becomes bookkeeping, not a revset.
- **0.26.0 — 2025-02-05, L2709:** “the Git index now contains the changes from all parents of
  the working copy instead of just the first parent (`HEAD`)” — index still jj-managed.
- **0.39.0 — 2026-03-04, L838:** “`jj` now safely detaches the `HEAD` of alternate Git
  worktrees if their checked-out branch is moved or deleted during Git export.”
- **0.44.0 — 2026-08-05, L252:** “Fixed Git HEAD mismatch after the working copy became
  immutable.” (#9827)
- **0.45.0 — 2026-09-02, L51:** “`jj git import` in non-colocated repositories no longer
  imports commits from a detached Git HEAD branch.” (colocated repos still import them).
  L68-L71: “Git HEAD state is now tracked per worktree internally.” L97: “In colocated
  workspaces, `jj workspace update-stale` now correctly resets the Git HEAD” (#9936).
- **0.45.1 — 2026-09-03:** packaging/signature fixes only; `lib/src/git.rs` and
  `cli/src/cli_util.rs` are untouched by `git diff v0.45.0 v0.45.1`, so HEAD behavior is
  identical to 0.45.0.
- **0.46.0 — 2026-10-07:** per-workspace colocation (`jj workspace add --[no-]colocate`);
  not present in 0.45.

## Documentation citations

- https://docs.jj-vcs.dev/v0.45.1/git-compatibility/#colocated-jujutsugit-workspaces
  (requested `https://jj-vcs.github.io/jj/v0.45.1/git-compatibility/` 301-redirects here;
  file `docs/git-compatibility.md:114-116`): “jj commands will usually put the Git repo in a
  "detached HEAD" state” — followed by “since in `jj` there is not concept of a "currently
  tracked branch"”.
- https://docs.jj-vcs.dev/v0.45.1/github/ (file `docs/github.md:77-78`): “jj commit updates
  the HEAD of the Git repository, enabling an incremental migration.”
- https://docs.jj-vcs.dev/v0.45.1/git-comparison/ (file `docs/git-comparison.md:26-28`):
  “This is the normal state in Jujutsu (there's actually no way -- yet, at least -- to have
  an active branch/bookmark).”
- `jj help git init --colocate` (local 0.45.1): “Specifies that the `jj` repo should also be
  a valid `git` repo, allowing the use of both `jj` and `git` commands in the same
  directory.” No CLI help text in 0.45.1 documents HEAD attachment; `jj help -k git` does not
  exist (`possible values: bookmarks, config, filesets, glossary, revsets, templates,
  tutorial`).

## [INFERENCE]

- The deterministic rule is: **`HEAD` is rewritten whenever the transaction-finish view
  records a different `git_head` than `first_parent(@)`, and the rewrite always detaches.**
  A command is "HEAD-moving" only insofar as it changes `@`'s first parent (commit/new/edit/
  squash), not because of its name.
- Because the comparison uses the recorded view, a symbolic HEAD is left alone precisely when
  its commit equals `@-`; that is why `describe` after an external `git checkout` at `@-` is
  inert (F5) but any `@`-moving command detaches (F2/F3).
- `check_and_detach_head` deliberately detaches at the *old* oid so that moving a branch does
  not silently drag the Git checkout along with it; this is the same rationale as the 0.39
  worktree safety fix, generalized to the main worktree.
- A HEAD rewrite during `jj git push` would be gratuitous (push operates on bookmarks), so the
  mtime-stable observation (F6) is expected from the source shape, not a coincidence.

## Consequences for the planned shokunin integration

1. **The helper's branch detection is correct but load-bearing.** `detect_branch()` tries
   `git symbolic-ref -q --short HEAD` first, which only works while HEAD is attached — true
   after `init` (F1) and false after the first `commit` (F2). In steady state it falls
   through to `refs/remotes/origin/HEAD`, then `master`/`main`/first local branch. If a lane
   clone lacks `refs/remotes/origin/HEAD` and has more than one local branch, the fallback
   could bookmark/push the wrong branch. Recommend asserting `origin/HEAD` exists at lane
   init, or pinning the branch in lane metadata.
2. **Never use git's upstream shorthand in lanes.** Observed after detachment:
   `git rev-parse @{u}` → `fatal: HEAD does not point to a branch`;
   `git rev-parse main@{u}` → `fatal: no upstream configured for branch 'main'`. Use explicit
   `refs/heads/<branch>` / `refs/remotes/origin/<branch>` (the helper does), and
   `git status -sb` will print `## HEAD (no branch)`.
3. **HEAD is a safe post-commit receipt only while the lock is held.** Right after
   `jj commit`, `HEAD == @- ==` the printed hash (F2, `exp10`), and the helper's immediate
   `bookmark set -r "$hash"` then makes `HEAD == branch` again. Any later `jj new`/`edit`
   moves HEAD, so durable hashes must come from `<branch>@origin` (helper does).
4. **Do not mix `git add` with lane work.** Every mutating jj command resets the Git index:
   `git diff --cached` was empty after `jj describe`, `jj commit`, and `jj new`, while
   `jj status` and `jj log --ignore-working-copy` left a staged entry intact (`exp3`,
   `exp11`). Lane tooling that stages then asks jj to commit will lose the staging.
5. **Ban `git checkout`/`git switch` in lanes.** Imported HEAD changes re-parent `@`
   (F7): a described-but-unbookmarked commit ends up as a sibling head and `@` moves to a
   child of the new HEAD. The helper's bookmark-then-push ordering keeps commits reachable,
   but a checkout between `jj commit` and `bookmark set` would strand the lane commit off the
   `@` line. This matches the upstream advice to use jj for mutations in colocated repos.
6. **`jj git push` is HEAD-neutral** (F6): pushing from a detached-HEAD lane is safe, and the
   helper's push/retry path needs no `git switch` preparation. `jj --ignore-working-copy`
   reads are also HEAD-neutral and index-neutral, so `state` is cheap and side-effect-free.
7. **Do not put `--ignore-working-copy` on commit/new in the helper** (it would not prevent
   the HEAD write — F8 — and would skip the snapshot those commands need). The helper's
   current placement (config/log/bookmark only) is correct.
8. **Fleet-root `fleet-commit.sh` can stay git-based** as planned, but it must not be pointed
   at a colocated lane: a `git commit` on detached HEAD is imported by jj as a new head on
   the next jj command, and bookmarks will not follow it automatically.

## Open uncertainties

- The helper was read, not executed (hard rule), and no live lane was inspected beyond
  `cat`/`grep`-level reads; the integration consequences above are derived from its code
  plus the sandbox experiments, not from an end-to-end lane round.
- Tested only Linux x64 with jj 0.45.1 and git 2.56.0. 0.45.0 was not executed (the
  `v0.45.0..v0.45.1` diff contains no HEAD-code changes), and 0.46+ was not tested.
- Multi-worktree behavior and `jj workspace update-stale` were not exercised; 0.45 moved
  `git_head` tracking to per-worktree state, and lanes are single-workspace.
- Concurrent `git` and `jj` processes were not raced. The view-vs-file comparison and the
  documented `git-head` lock are read from source, not stress-tested.
- `jj git fetch` moving a bookmark while HEAD is attached (rather than `bookmark set/move`)
  was not observed; it shares the `check_and_detach_head` export path, so the predicted
  detach-at-pre-move-oid is [INFERENCE].
- SHA-256 Git repositories and Windows/macOS path handling were not tested.
- No release note pins the exact version where jj first began writing HEAD on each command;
  the changelog only shows the docs claim from 0.9.0 and refactors at 0.8.0/0.10.0. The
  behavior itself is verified here for 0.45.x only.
