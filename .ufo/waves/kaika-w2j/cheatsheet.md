# git → jj cheat sheet for shokunin lanes (colocated repos)

Status: docs-derived + scratch-probed, 2026-10-19. jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`.
Audience: a shokunin lane (`<id>-shokunin <id>@shokunin.local`) whose repo has already been colocated with
`jj git init --colocate` (or `jj git init`, which is colocated by default unless `git.colocate = false`).
Every `jj` command below was executed in a disposable synthetic repo under
`/home/vgpnk/Projects/shokunin/.tower/jj-probe/` — no live repo, worktree, `.git` dir, or branch was touched.
Docs citations use the official site `https://jj-vcs.github.io/jj/latest/` (it canonically redirects to
`https://docs.jj-vcs.dev/latest/`).

---

## 0. Preconditions (do these once, before the first content commit)

### 0.1 Colocate

```sh
cd <repo>
jj git init --colocate
```

- Docs: [Git compatibility § Creating an empty repo](https://jj-vcs.github.io/jj/latest/git-compatibility/#creating-an-empty-repo),
  [Colocated Jujutsu/Git workspaces](https://jj-vcs.github.io/jj/latest/git-compatibility/#colocated-jujutsugit-workspaces),
  [CLI reference § jj git init](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-init).
- Probe: `jj git init --colocate` exit 0; `.jj/.gitignore` was created containing exactly `/*`; `git status`
  stayed clean; first `jj st` took 0.01 s on a tiny repo (lane repos will differ).
- **Do not colocate a repo that active git worktrees depend on.** Docs:
  [Git compatibility § Supported features](https://jj-vcs.github.io/jj/latest/git-compatibility/#supported-features)
  says `git-worktree: No` (jj has its own `jj workspace` instead:
  [Working copy § Workspaces](https://jj-vcs.github.io/jj/latest/working-copy/#workspaces)).
  The fleet currently runs lanes in git worktrees under `.tower/worktrees/kaika/`; adoption must wait until
  those are retired or replaced by jj workspaces.

### 0.2 Pin the lane identity on the working-copy commit

```sh
JJ_USER='<lane>-shokunin' JJ_EMAIL='<lane>@shokunin.local' \
  jj metaedit --update-author -r @
```

or persist the identity for all future commits first:

```sh
jj config set --repo user.name '<lane>-shokunin'
jj config set --repo user.email '<lane>@shokunin.local'
JJ_USER='<lane>-shokunin' JJ_EMAIL='<lane>@shokunin.local' \
  jj metaedit --update-author -r @
```

- Docs: [Configuration § User settings](https://jj-vcs.github.io/jj/latest/config/#user-settings)
  (`JJ_USER`/`JJ_EMAIL` override config), [CLI reference § jj metaedit](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-metaedit)
  (`--update-author` "Update the author to the configured user"; `--author` is also available).
- **Why this step is mandatory:** `jj commit` does not rewrite the author of the commit it is describing.
  Passing `--config user.name/--config user.email` to `jj commit` changes only the **committer** of that
  already-created working-copy commit. Probe (author default, lane identity passed to commit):

  ```
  $ jj --config user.name=scribe-shokunin --config user.email=scribe@shokunin.local \
       commit -m 'scribe: probe a only' a.txt
  $ jj show @-
  Author   : Joao Pedro Veiga <jpveigao10@gmail.com>
  Committer: scribe-shokunin <scribe@shokunin.local>
  ```

  The same holds for `JJ_USER`/`JJ_EMAIL` on `jj commit`. `jj config set --repo ...` warns:
  `This setting will only impact future commits. The author of the working copy will stay ... use
  "jj metaedit --update-author"`. Fix `@` with `jj metaedit --update-author` **before** committing content.
- Probe: after `JJ_USER`/`JJ_EMAIL` + `metaedit --update-author`, both author and committer were
  `<lane>-shokunin <lane>@shokunin.local>`.

### 0.3 Snapshot limits

- Every jj command snapshots the working copy, including untracked non-ignored files:
  [Working copy § Introduction](https://jj-vcs.github.io/jj/latest/working-copy/#introduction).
- Default refusal threshold is 1 MiB:
  [Configuration § Maximum size for new files](https://jj-vcs.github.io/jj/latest/config/#maximum-size-for-new-files).
  Probe: `jj st` with an untracked 2 MiB file printed `Refused to snapshot some files` (exit 0) and left it
  untracked; `jj config set --repo snapshot.max-new-file-size 4MiB` then `jj st` snapshotted it.
- Prefer ignoring build outputs via `.gitignore` over raising the limit
  ([Working copy § Ignored files](https://jj-vcs.github.io/jj/latest/working-copy/#ignored-files)).

---

## 1. Lane-identity commit of an explicit path set

```sh
cd <repo>
jj --config user.name='<lane>-shokunin' \
   --config user.email='<lane>@shokunin.local' \
   commit -m '<lane>: <subject>' -- <path> [<path>...]
```

- Docs: [CLI reference § jj commit](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-commit)
  (`<FILESETS> — Put these paths in the current commit`; with path arguments "the selected changes stay in
  the current commit while the remaining changes are moved to a new working-copy commit on top";
  "jj commit doesn't move bookmarks forward").
- The `--` separator is not a jj feature; it keeps shell paths from being parsed as options. `jj commit`
  accepts `[FILESETS]...`.
- Probe: `a.txt` was committed, `b.txt` remained in `@`; `git log -1` showed the committed hash;
  `git rev-parse --abbrev-ref HEAD` printed `HEAD` (detached) afterwards.
- Verify the identity before citing:

  ```sh
  jj log --no-graph -r @- -T 'author.name() ++ " <" ++ author.email() ++ "> | " ++ committer.name() ++ " <" ++ committer.email() ++ ">\n"'
  ```

  Docs: [CLI reference § jj log](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-log) (`-r`, `-T`).
- If the author is wrong, **do not** rewrite a commit that has already been cited. Fix the working-copy
  author with `jj metaedit --update-author` (step 0.2) before the content commit.

---

## 2. Citing a commit hash

Immediately after `jj commit`, the stable commit is `@-` (the new `@` is the empty mutable working-copy
commit):

```sh
jj log --no-graph -r @- -T 'commit_id ++ "\n"'
```

- Docs: [CLI reference § jj log](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-log);
  [Revsets § Symbols](https://jj-vcs.github.io/jj/latest/revsets/#symbols) — a full commit ID or a unique
  prefix refers to one commit, and `commit_id(prefix)` should be used in scripts because a bookmark can
  shadow a hash (priority: tag → bookmark → commit/change ID).
- Inspect it: `jj show @-` — [CLI reference § jj show](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-show).
- The lane protocol's ancestry gate still applies: `git merge-base --is-ancestor <hash> HEAD` must exit 0
  (`PROTOCOL.md`, "A lane report lands last … cite that commit's hash"). Probe: exit 0 before a rewrite,
  exit 1 after `jj describe -r` rewrote the cited commit.
- **Never cite `@`.** `@` is the working-copy commit; its commit ID changes whenever jj snapshots or rewrites
  it ([Working copy § Introduction](https://jj-vcs.github.io/jj/latest/working-copy/#introduction)).
- `jj log -r <old-hash>` can still resolve a rewritten/hidden commit when it is explicitly named
  ([Revsets § Hidden revisions](https://jj-vcs.github.io/jj/latest/revsets/#hidden-revisions)); that is not
  proof of ancestry. Use `git merge-base --is-ancestor`.
- Colocated caveat: after a jj command, git is usually detached
  ([Git compatibility § Colocated Jujutsu/Git workspaces](https://jj-vcs.github.io/jj/latest/git-compatibility/#colocated-jujutsugit-workspaces)).
  Probe: `git rev-parse --abbrev-ref HEAD` → `HEAD`; `git branch --show-current` → empty.

---

## 3. Viewing and undoing an operation

```sh
jj op log --no-graph -n 8 -T 'id.short() ++ " " ++ description.first_line() ++ "\n"'
jj undo                    # undo the last operation
jj op restore <op-id>      # restore the repo state at an older operation (creates a new operation)
jj op revert <op-id>       # invert one specific operation (creates a new operation)
jj --at-op=<op-id> log     # inspect an old state without mutating
```

- Docs: [Operation log § Introduction](https://jj-vcs.github.io/jj/latest/operation-log/#introduction);
  [Operation log § Loading an old version of the repo](https://jj-vcs.github.io/jj/latest/operation-log/#loading-an-old-version-of-the-repo);
  [CLI reference § jj operation log](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-operation-log),
  [§ jj undo](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-undo),
  [§ jj operation restore](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-operation-restore),
  [§ jj operation revert](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-operation-revert).
- Operation templates use `id`; commit templates use `commit_id`/`change_id`. Probe: reusing `id` in a
  commit template fails with `Keyword 'id' doesn't exist`.
- Probe: `jj op revert <bookmark-set-op>` removed the bookmark; `jj undo` restored it. `jj op restore
  <describe-op>` restored the rewritten commit; `jj undo` returned to the cited hash and
  `git merge-base --is-ancestor <cited> HEAD` went back to exit 0.

---

## 4. Resolving a conflict

A rebase that conflicts still succeeds and records the conflict in the commit
([First-class conflicts § Introduction](https://jj-vcs.github.io/jj/latest/conflicts/#introduction);
[CLI reference § jj rebase](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-rebase)):

```sh
jj rebase -s <change-id-or-hash> -d <destination>
jj new <conflicted-rev>     # materialize the conflict in a working-copy child
jj resolve --list           # e.g. "c.txt    2-sided conflict"
# edit the file: replace jj's conflict markers with the resolved text
jj st                       # snapshot; prints "Conflict in parent commit has been resolved in working copy."
jj diff                     # inspect the resolution
jj squash                   # move the resolution into the conflicted parent
jj resolve --list           # exits 2 with "No conflicts found at this revision" when clean
```

- Docs: [Working copy § Conflicts](https://jj-vcs.github.io/jj/latest/working-copy/#conflicts)
  (`jj new <commit>` → resolve → `jj squash`), [First-class conflicts § Conflict markers](https://jj-vcs.github.io/jj/latest/conflicts/#conflict-markers),
  [CLI reference § jj resolve](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-resolve)
  (`-l/--list`, `--tool=:ours` / `:theirs`).
- Probe: rebase exit 0 + `New conflicts appeared in 1 commits`; `jj resolve --list` listed
  `c.txt 2-sided conflict`; after editing markers, `jj st` printed the resolution hint; `jj squash` cleared
  it and `conflicts=false`. `jj resolve --list` exits **2** when there are no conflicts — do not treat that
  as a crash in a gate, but do not treat it as "clean" without reading stderr either.
- jj markers are not git's markers; snapshot-style/diff-style variants are configurable
  ([First-class conflicts § Alternative conflict marker styles](https://jj-vcs.github.io/jj/latest/conflicts/#alternative-conflict-marker-styles)).
- Never `git switch`/`git checkout` a conflicted jj commit: git sees `.jjconflict-base-*`/`.jjconflict-side-*`
  directories, and a later snapshot can commit them
  ([Git compatibility § Format mapping details](https://jj-vcs.github.io/jj/latest/git-compatibility/#format-mapping-details)).

---

## 5. Creating a bookmark that git sees as a branch

```sh
jj bookmark set kaika/<lane-slug> -r <rev>
git branch --list 'kaika/*'
git rev-parse 'kaika/<lane-slug>'
```

- Docs: [Bookmarks § Mapping to Git branches](https://jj-vcs.github.io/jj/latest/bookmarks/#mapping-to-git-branches)
  (bookmarks map to git branches; in a colocated workspace the import/export on every jj command makes the
  branch visible), [CLI reference § jj bookmark set](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-bookmark-set)
  (`-r/--revision`, `-B/--allow-backwards`). Use `jj bookmark create` when the bookmark must not already exist
  ([§ jj bookmark create](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-bookmark-create)).
- Probe: `jj bookmark set kaika/cheat -r @-` created git branch `kaika/cheat` immediately; `git branch --list`
  and `git rev-parse` both resolved it.
- `jj commit` does **not** move bookmarks forward
  ([CLI reference § jj commit](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-commit)); set the bookmark
  explicitly after the commit. Bookmarks move automatically when a commit is rewritten
  ([Bookmarks § Bookmark updates](https://jj-vcs.github.io/jj/latest/bookmarks/#bookmark-updates)) — which is
  why a bookmark cannot protect a cited hash from a rewrite.
- `kaika/*` matches the fleet's lane branch namespace (`kaika/census`, `kaika/contract`, …).

---

## 6. Never do

1. **Never rewrite an already-cited commit.** This includes `jj describe -r <cited>`,
   `jj squash --into <cited>`, `jj rebase -s/-d` over it, `jj metaedit -r <cited>`,
   `jj abandon <cited>`, and anything with `--ignore-immutable`.
   - Probe: `jj describe -r 6bbac725 -m '...'` changed the commit to `1473a46b`; the old hash remained a git
     object but `git merge-base --is-ancestor 6bbac725 HEAD` flipped from exit 0 to exit 1.
   - Docs: [Git compatibility § Format mapping details](https://jj-vcs.github.io/jj/latest/git-compatibility/#format-mapping-details)
     ("Change IDs … are not preserved through a rebase operation"),
     [Configuration § Set of immutable commits](https://jj-vcs.github.io/jj/latest/config/#set-of-immutable-commits)
     (`--ignore-immutable` rewrites any commit and all descendants; "remember `jj undo`").
   - Correct form of a correction: land a **new descendant** —
     `jj new <cited>` → edit → `jj commit -m '<lane>: correction' -- <paths>`
     ([CLI reference § jj new](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-new),
     [§ jj commit](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-commit)).
     The fleet protocol already requires this: corrections land as new commits, never by amending a cited one.
   - Recovery if it already happened: `jj op log` → `jj undo` or `jj op restore <op-id>`; probe verified this
     restores the cited hash as an ancestor of `HEAD`.
2. **Never `jj git push` from a lane.**
   - Docs: [CLI reference § jj git push](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-push);
     [Bookmarks § Pushing bookmarks: Safety checks](https://jj-vcs.github.io/jj/latest/bookmarks/#pushing-bookmarks-safety-checks)
     (remote-state checks, tracked-bookmark requirement, force-with-lease-like behavior).
   - It publishes lane branches/remote bookmarks before the operator releases the gate. The fleet rule is
     commit locally, push only on operator release (`PROTOCOL.md`).
   - In colocated repos, the push updates remote-tracking bookmarks; a later `jj git fetch` can then create
     bookmark conflicts in a live lane.
3. **Never `jj op abandon` or `jj util gc` while a cited hash may still need recovery.**
   - Docs: [CLI reference § jj operation abandon](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-operation-abandon)
     ("Previous versions … are also discarded if they become unreachable from the operation history. The
     abandoned operations, commits, and other unreachable objects can later be garbage collected by using
     `jj util gc`").
4. **Never colocate a repo that active git worktrees depend on.**
   - Docs: [Git compatibility § Supported features](https://jj-vcs.github.io/jj/latest/git-compatibility/#supported-features)
     (`git-worktree: No`). This is the current fleet blocker: 21 lane worktrees are live under
     `.tower/worktrees/kaika/`.
5. **Never use mutating git commands in a colocated lane** (`git add`, `git commit`, `git switch`, `git reset`).
   - Docs: [Git compatibility § Colocated Jujutsu/Git workspaces](https://jj-vcs.github.io/jj/latest/git-compatibility/#colocated-jujutsugit-workspaces)
     ("mostly use read-only git commands and use jj to make changes"; jj usually leaves git detached; mutating
     git can create confusing branch/divergence states) and
     [§ Supported features](https://jj-vcs.github.io/jj/latest/git-compatibility/#supported-features)
     (the staging area is ignored). Read-only `git log/status/rev-parse/merge-base` is fine and is what the
     protocol's checks use.
6. **Never assume git reports a branch name after a jj commit.** Probe: `git rev-parse --abbrev-ref HEAD`
   prints `HEAD`; `git branch --show-current` prints empty. Docs: the colocated section says jj commands
   "will usually put the Git repo in a 'detached HEAD' state". Gates that hard-code a branch can flip exit
   codes; e.g. `souji-shokunin/tools/souji-verify.impl-09.sh:444` calls
   `git symbolic-ref HEAD refs/heads/master` in its fixtures.

---

## 7. Gate-survival notes

Documented but not probed here (mark as docs-only when reporting):

- Git hooks do not run: [Git compatibility § Supported features](https://jj-vcs.github.io/jj/latest/git-compatibility/#supported-features)
  (`Hooks: No`).
- `.gitattributes` unsupported; submodules, partial clones, Git LFS unsupported; sparse checkouts are jj-native
  (`jj sparse`) — same section.
- The git staging area is ignored — same section; `git diff --cached` is not a jj concept.
- Ignored files are never auto-tracked; `jj file untrack` requires the path to be ignored
  ([Working copy § Ignored files](https://jj-vcs.github.io/jj/latest/working-copy/#ignored-files),
  [CLI reference § jj file untrack](https://jj-vcs.github.io/jj/latest/cli-reference/#jj-file-untrack)).
- `.jj/` is self-ignored by `.jj/.gitignore` containing `/*` (probed); the docs' manual conversion writes the
  same file ([Git compatibility § Converting a workspace into a colocated workspace](https://jj-vcs.github.io/jj/latest/git-compatibility/#converting-a-workspace-into-a-colocated-workspace)).

---

## 8. Command → docs citation index

| Command | Official docs (URL + heading) |
|---|---|
| `jj git init --colocate` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-init ; https://jj-vcs.github.io/jj/latest/git-compatibility/#creating-an-empty-repo |
| `jj metaedit --update-author` / `--author` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-metaedit |
| `JJ_USER` / `JJ_EMAIL` | https://jj-vcs.github.io/jj/latest/config/#user-settings |
| `jj config set --repo snapshot.max-new-file-size` | https://jj-vcs.github.io/jj/latest/config/#maximum-size-for-new-files |
| `jj commit -m … -- <paths>` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-commit |
| `jj log -r @- -T 'commit_id'` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-log ; https://jj-vcs.github.io/jj/latest/revsets/#symbols |
| `jj show @-` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-show |
| `jj op log` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-operation-log ; https://jj-vcs.github.io/jj/latest/operation-log/#introduction |
| `jj undo` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-undo ; https://jj-vcs.github.io/jj/latest/operation-log/#introduction |
| `jj op restore <op-id>` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-operation-restore |
| `jj op revert <op-id>` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-operation-revert |
| `jj --at-op=<op-id> log` | https://jj-vcs.github.io/jj/latest/operation-log/#loading-an-old-version-of-the-repo |
| `jj rebase -s … -d …` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-rebase ; https://jj-vcs.github.io/jj/latest/conflicts/#introduction |
| `jj new <conflicted-rev>` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-new ; https://jj-vcs.github.io/jj/latest/working-copy/#conflicts |
| `jj resolve --list` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-resolve |
| resolve by editing markers + `jj st` | https://jj-vcs.github.io/jj/latest/working-copy/#conflicts ; https://jj-vcs.github.io/jj/latest/conflicts/#conflict-markers |
| `jj squash` (resolution into parent) | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-squash ; https://jj-vcs.github.io/jj/latest/working-copy/#conflicts |
| `jj bookmark set <name> -r <rev>` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-bookmark-set ; https://jj-vcs.github.io/jj/latest/bookmarks/#mapping-to-git-branches |
| `jj bookmark create <name> -r <rev>` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-bookmark-create |
| `jj describe -r <rev>` (rewrite; forbidden on cited) | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-describe |
| `jj abandon <rev>` (rewrite; forbidden on cited) | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-abandon |
| `--ignore-immutable` (forbidden) | https://jj-vcs.github.io/jj/latest/config/#set-of-immutable-commits |
| `jj git push` (forbidden from lanes) | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-push ; https://jj-vcs.github.io/jj/latest/bookmarks/#pushing-bookmarks-safety-checks |
| `jj op abandon` / `jj util gc` (forbidden while cited hashes matter) | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-operation-abandon |
| `jj file untrack` | https://jj-vcs.github.io/jj/latest/cli-reference/#jj-file-untrack ; https://jj-vcs.github.io/jj/latest/working-copy/#ignored-files |
| git-worktree limitation | https://jj-vcs.github.io/jj/latest/git-compatibility/#supported-features |
| colocated git interleaving / detached HEAD | https://jj-vcs.github.io/jj/latest/git-compatibility/#colocated-jujutsugit-workspaces |

---

## 9. Probe record (scratch only)

| Probe | Command | Exit | Observation |
|---|---|---|---|
| colocate | `jj git init --colocate` | 0 | `.jj/.gitignore` = `/*`; `git status` clean; first `jj st` 0.01 s |
| identity | `jj --config user.name=… commit -m … a.txt` | 0 | author stayed default; committer became lane |
| identity fix | `JJ_USER=… JJ_EMAIL=… jj metaedit --update-author -r @` | 0 | author and committer both lane |
| explicit paths | `jj commit -m … -- a.txt` | 0 | `a.txt` committed; `b.txt` left in `@` |
| cite | `jj log -r @- -T 'commit_id'` | 0 | stable hash; `git rev-parse HEAD` matched after commit |
| detached git | `git rev-parse --abbrev-ref HEAD` | 0 | `HEAD`; `git branch --show-current` empty |
| op log | `jj op log --no-graph -n 8 -T 'id.short() …'` | 0 | operations listed; `id` is op-only |
| op revert | `jj op revert <bookmark-op>` | 0 | bookmark removed |
| undo | `jj undo` | 0 | bookmark restored |
| rewrite cited | `jj describe -r <cited> -m …` | 0 | commit ID changed; ancestry check 0 → 1 |
| restore | `jj op restore <describe-op>` | 0 | rewritten state restored |
| undo restore | `jj undo` | 0 | cited hash current again; ancestry check 1 → 0 |
| conflict | `jj rebase -s <b> -d <a>` | 0 | conflict recorded; warning printed |
| conflict list | `jj resolve --list` | 0 | `c.txt 2-sided conflict` |
| resolve | edit markers; `jj st`; `jj squash` | 0 | `conflicts=false`; `resolve --list` exit 2 |
| bookmark | `jj bookmark set kaika/cheat -r @-` | 0 | `git branch --list kaika/cheat` and `git rev-parse` resolve immediately |
| large file | `jj st` with untracked 2 MiB file | 0 | refused snapshot with warning; config 4MiB then snapshotted |

Scratch dirs (deleted after use, sizes recorded before deletion):
`.tower/jj-probe/cheatsheet-scribe` (356K), `cheatsheet-scribe2` (912K), `cheatsheet-scribe3` (2.5M).
Live fleet repos, main checkouts, `.git` dirs, and branches were not modified (`git status --porcelain` on
the fleet root was empty at start and after cleanup).

---

## 10. Bottom line

For a shokunin lane in a colocated repo, jj is **safe-with-config** once these hold:

1. No active git worktrees (jj does not support them).
2. Lane identity is pinned with `jj metaedit --update-author` (not just `--config` on `jj commit`).
3. Untracked-file exposure is controlled (`snapshot.max-new-file-size` / `.gitignore`).
4. Cited commits are never rewritten; corrections are descendants; `jj git push` is never run from a lane.

Top hazard: **rewriting an already-cited commit silently changes its commit ID and its bookmark moves with
it**, so the lane report's hash stops being an ancestor of `HEAD` — and `jj git push` / `jj op abandon` can
make the old object unrecoverable.
