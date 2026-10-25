# JjDocGitIndex — jj 0.45 and `.git/index`

Scope: jj 0.45.x in a **colocated** repo — what jj does to `.git/index` on snapshot, export and
checkout, and what happens to entries a separate `git` process staged. Leaf seat, no subagents.

Environment: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` (`~/.local/bin/jj`),
`git 2.56.0`, Linux. All experiments in a throwaway sandbox
`/fast/scratch/jj-wave/JjDocGitIndex/` (removed after this report; outputs pasted below).
Source: `git clone --depth 1 --branch v0.45.1 https://github.com/jj-vcs/jj` — HEAD
`7c41cdeb16b6b321c64e789a966b6adf723816a5`, the same commit hash embedded in the release
binary's version string. To attribute index writes I built that source as a debug binary with four
`eprintln!("TRACE …")` markers (`reset_index`, `update_intent_to_add`, `reset_head`,
`import_head`); nothing else changed. Behavior reported below was reproduced with both the
release binary and the instrumented build.

No tools were installed or upgraded. `cargo build` (dev profile, 50 s) used the host toolchain.

## The model in one sentence

After any jj **transaction** in a colocated repo, `.git/index` is the merged **parent** tree of the
working-copy commit `@` plus intent-to-add entries for paths that are new in `@`; jj never reads
the index as content, and user staging survives only read-only (snapshot-only) commands.

---

## 1. Snapshot

**Answer.** Snapshot **rewrites** `.git/index` but does **not** reset it. `update_intent_to_add`
loads the existing index (`index_or_empty()`), adds intent-to-add entries for paths that are newly
tracked in `@` and not already in the index, removes ITA entries for paths deleted from `@`, and
then writes the file unconditionally. Existing entries keep their blob, mode, stage and flags;
only ITA bookkeeping and file-format bytes change.

Citations:

- Docs: "The staging area will be ignored. For example, `jj diff` will show a diff from the Git
  HEAD to the working copy." — <https://jj-vcs.github.io/jj/v0.45.0/git-compatibility/#supported-features>
- Docs: "There's no index (staging area). Because the working copy is automatically committed, an
  index-like concept doesn't make sense." — <https://jj-vcs.github.io/jj/v0.45.0/git-comparison/#the-index>
- Source: `update_intent_to_add` reads `git_repo.index_or_empty()` and always calls
  `.write(gix::index::write::Options::default())` —
  <https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/git.rs#L2100-L2122>
- `jj help` global option: "Don't snapshot the working copy, and don't update it. By default,
  Jujutsu snapshots the working copy at the beginning of every command."

Evidence — staged modification survives `jj st` (E1):

```
$ git status --porcelain; git ls-files -s a.txt      # staged a2
M  a.txt
100644 c1827f07e114c20547dc6a7296588870a4b5b62c 0	a.txt
$ jj st
Working copy changes:
M a.txt
Working copy  (@) : ktmzlqww 8e17618a (no description set)
Parent commit (@-): qqsknokk 00e9c6b0 main | base
$ git status --porcelain; git ls-files -s a.txt      # unchanged
M  a.txt
100644 c1827f07e114c20547dc6a7296588870a4b5b62c 0	a.txt
```

Same for `jj log`/`jj diff` (E1c: blob still `c1827f0…`), a staged deletion (`D  a.txt` before
and after `jj st`, E9), and a fully staged new file (`A  new.txt`, real blob `d5a09df…`, E24).

Newly *tracked* untracked files get an intent-to-add entry (E8: `git status` shows ` A new.txt`,
`git ls-files -s new.txt` shows the empty blob `e69de29…`) — the " A" entries described in the
helper's comment.

Instrumented trace for `jj st` (release semantics): `TRACE update_intent_to_add`, and no
`reset_index`.

Byte-level caveat (observed on gix 0.87.1, not a jj contract): on a snapshot where the working-copy
tree changed the file is rewritten even with no add/remove — sha256 changed and an `EOIE`
extension was added (`TREE`+`EOIE`, same entries/blobs). When ITA entries are actually mutated,
`index.remove_tree()` drops the cache-tree and the index becomes version 3 with no extensions
(E8b). This is the 0.45.1 duplicateEntries fix:

> "In colocated repos, an external `git add` after a `jj` command no longer produces a tree with
> duplicate entries" — <https://github.com/jj-vcs/jj/blob/v0.45.1/CHANGELOG.md#L107-L113>

## 2. Export

**Answer.** Nothing. In a colocated repo `jj git export` is a no-op ("No export needed in
colocated workspaces."); refs are exported automatically at the end of each command that commits a
transaction. It does not read or write `.git/index`, even when forced with
`--ignore-working-copy`.

Citations:

- `jj help git export`: "By default, this command does nothing in colocated workspaces because the
  export happens automatically. Use `--ignore-working-copy` to forcibly export changes."
- Docs: "Jujutsu will import and export from and to the Git repo on every `jj` command
  automatically." — <https://jj-vcs.github.io/jj/v0.45.0/git-compatibility/#colocated-jujutsugit-workspaces>
- Source: the snapshot-time export helper is `update_intent_to_add` + `export_refs`
  (<https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/cli_util.rs#L2702-L2715>); `reset_index` is
  reached only through `reset_head`.

Evidence (E5):

```
$ jj git export
No export needed in colocated workspaces.
$ git ls-files -s a.txt
100644 c1827f07e114c20547dc6a7296588870a4b5b62c 0	a.txt     # staged a2 preserved
```

Forced export (t6): `jj --ignore-working-copy git export` → no trace line, index blob unchanged.

## 3. Checkout

**Answer.** A checkout — or any other command that commits a jj transaction — rebuilds
`.git/index` from scratch. `finish_transaction` calls `try_reset_git_head` → `reset_head` →
`reset_index`, which writes the **merged parent tree** of the (new) working-copy commit `@` as the
index and adds ITA entries for paths that are new in `@` relative to its parent. All previous index
state (staged blobs, stage entries, assume-unchanged/skip-worktree flags) is discarded.
`reset_head` also clears git operation state (MERGE_HEAD, MERGE_MSG, rebase-merge, rebase-apply,
sequencer, …; source-read: `clear_operation_state`, lib/src/git.rs#L1894-L1922 — not exercised in
these experiments) and moves `.git/HEAD` to `@-`, detaching it if it was attached.

Citations:

- Source `reset_index`: "Use the merged parent tree as the Git index, allowing `git diff` to show
  the same changes as `jj diff`." —
  <https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/git.rs#L1932-L1934>
- Source `reset_head` ends with `reset_index(...)` —
  <https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/git.rs#L1841-L1891>
- Source `finish_transaction` resets HEAD+index for the working-copy commit —
  <https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/cli_util.rs#L2393-L2407>
- Docs colocated: "`jj` commands will usually put the Git repo in a "detached HEAD" state" —
  <https://jj-vcs.github.io/jj/v0.45.0/git-compatibility/#colocated-jujutsugit-workspaces>

Evidence — staged a2, worktree a3 (E2b):

```
$ git status --porcelain; git ls-files -s a.txt
MM a.txt
100644 c1827f07e114c20547dc6a7296588870a4b5b62c 0	a.txt
$ jj st                                    # snapshot only
MM a.txt
100644 c1827f07e114c20547dc6a7296588870a4b5b62c 0	a.txt
$ jj bookmark set foo -r @-                # no HEAD move at all
Created 1 bookmarks pointing to prwvkkqn cd88299e foo main | base
$ git status --porcelain; git ls-files -s a.txt
 M a.txt
100644 78981922613b2afb6025042ff6bd878ac1994e85 0	a.txt   # reset to the parent blob
$ git diff --cached                        # empty
```

The result is jj's invariant, not a bug (E23): after the reset `jj diff` and `git diff` show the
same a→a3 change, `git diff --cached` is empty, `git status --porcelain` shows only ` M a.txt`.

Other checkouts: `jj new` → index = new `@-` tree, worktree clean (E14); `jj edit @-` → index = the
edited commit's parent tree while the worktree keeps that commit's files, so `git status` shows
` M a.txt` and `git ls-files -s` shows the parent blob (E14).

Instrumented traces, all `TRACE reset_index` (and no `reset_index` when the command makes no repo
change, e.g. a second `jj bookmark track` prints "Nothing changed."):
`jj new`, `jj edit`, `jj describe`, `jj squash`, `jj abandon`, `jj commit` (including empty
commits), `jj bookmark set`, a real `jj bookmark track`, a real `jj git import`, a real
`jj git push`, a `jj git fetch` that imports new commits, and importing an external `git commit`
or `git checkout`.

Edge cases: `jj commit -m x -- b.txt` with a nonexistent path warns and still creates an empty
commit and resets the index (E18). `jj --ignore-working-copy bookmark set bar -r @-` **also** resets
the index — `--ignore-working-copy` skips the snapshot, not the finish (E6: sha256 of `.git/index`
changed, staged blob `c1827f0…` replaced by `789819…`).

## 4. Entries staged by a separate git process

**Answer.**

- **Content is ignored.** With a2 staged and a3 in the worktree, `jj commit -- a.txt` commits
  **a3** (E4: `jj file show -r @- a.txt` → `a3`; index after = the new parent tree, `d616f73…`).
  jj reads the working tree, never the index.
- **Snapshot-only commands preserve them**, including stage entries and blobs: `jj st`, `jj log`,
  `jj diff` (E1, E1b, E1c, E9, E24).
- **Any committed transaction destroys them** — including transactions that do not move HEAD or
  touch the path. E3: a.txt→a2 and b.txt→b2 both staged, `jj commit -m only-a -- a.txt`; afterwards
  `git status` shows only ` M b.txt`, `git ls-files -s b.txt` → `6178079…` (base blob).
- **`jj git init --colocate` preserves them** (E7: `MM a.txt` and staged blob `c1827f0…` unchanged;
  trace shows only `update_intent_to_add`). The helper's later `jj bookmark track` (a real one) is
  what resets (t2).
- **Index-neutral commands**: `jj --ignore-working-copy config set --repo …`, `jj file track`
  (no-op or real — it uses a raw `tx.commit`, not `finish`), no-op `jj git import/export/fetch`,
  and forced `jj git export` leave the index untouched (E12, E15, t4, t6).
- **With `snapshot.auto-track="none()"`** (the lane setting) a git-staged new file that jj does not
  track is dropped to `??` untracked by the next transaction (E25), whereas with default
  auto-track it becomes intent-to-add ` A` (E24).
- **External HEAD moves are imported and reset the index** on the next jj command: `git commit`
  then `jj st` printed "Reset the working copy parent to the new Git HEAD." and wrote the index
  (E21, T3); same for `git checkout -b side HEAD~1` with staged junk (T3: staged `dbe2bc1…` lost,
  index back to parent, ` M a.txt`).
- **Index flags are lost**: `git update-index --skip-worktree b.txt` (`S b.txt`) becomes `H b.txt`
  after `jj bookmark set` (E27).
- **Cache-tree is sane afterwards**: after a jj commit, `git add -A` + `git write-tree` +
  `git fsck` were clean (E19), matching the 0.45.1 changelog entry quoted in §1.

Citations:

- Docs: "Jujutsu will ignore Git's staging area." —
  <https://jj-vcs.github.io/jj/v0.45.0/git-compatibility/#colocated-jujutsugit-workspaces>
- Changelog (duplicateEntries fix): see §1.

[INFERENCE] Concurrency: the index is read at snapshot start and written at transaction finish; the
`strace` shows only a short `index.lock` → `index` rename for the write. A concurrent `git add`
landing inside that window can therefore be overwritten (last writer wins). The helper's flock
serializes `jj-lane.sh` callers only; it does not exclude other git processes.

---

## Consequences for the planned shokunin integration

1. **Lanes must not stage.** The lane contract cannot rely on `git add` as an input to a jj commit:
   jj either commits the whole working-tree content of the named paths (E4) or erases the staged
   entries at the next transaction (E2b/E3/E6). The helper's current usage — whole files, no
   staging, pathspec-limited — is the only safe pattern. Any fleet tool that stages a subset in a
   lane and then expects `jj-lane.sh commit` to commit exactly that subset would silently commit
   more (whole files) or lose the staging.
2. **Pathspec-limiting survives at path granularity only.** `jj commit -- <paths>` keeps the commit
   limited to those paths (E3: b.txt stayed out), but hunk/stage granularity is not representable.
   The helper's `-- <path>...` contract still means what it says; it does not mean "commit only the
   staged part of those paths".
3. **Read-only probes.** After any jj transaction, `git diff --cached` is always empty and
   `git status --porcelain` shows worktree status only (` M`/` D`/`??`). Monitoring or fleet code
   must not interpret an empty staged column as "nothing changed"; use `git status --porcelain`
   worktree column, `git diff` (which equals `jj diff` against `@-`, E23), or `jj diff`.
4. **`jj-lane.sh state` is safe.** It is pure git and writes nothing. Every mutating helper path
   (init's first-time `bookmark track`, commit's `metaedit` when it changes anything, `jj commit`,
   `bookmark set`, push, and the fetch-then-rebase retry) resets the index; that is acceptable only
   because the lane contract forbids staging. The helper's commit flow starts with `jj file track`
   (index-neutral); the first destructive step is `metaedit` (if it rewrites) or `jj commit`.
5. **`.ufo/state/` stays out of the index.** With `auto-track="none()"` jj never puts it in `@`;
   `reset_index` only adds ITA entries for paths present in `@`, and snapshot's ITA pass only
   considers paths that changed in `@`. It therefore never appears as an index entry.
6. **Do not use index flags or sparse checkout in lanes.** skip-worktree / assume-unchanged are
   dropped by the next jj transaction (E27); `jj sparse` is jj's own mechanism, not git's.
7. **Keep the fleet root on `fleet-commit.sh` (git).** The same mechanics that make lane commits
   work would silently erase staged state in the fleet root on any jj command; per the plan, jj
   never runs there. Never colocate the fleet root while `fleet-commit.sh` stages.
8. **Serialize index writers per lane.** Do not run `git add`/`git commit` in a lane concurrently
   with a `jj-lane.sh` commit. The helper's flock covers jj-lane.sh invocations but not external
   git processes, and the index read-modify-write window spans the command. [INFERENCE]

## Open uncertainties

- gix byte-level details (EOIE extension, index v3, TREE dropping) are gix 0.87.1 implementation
  behavior under jj 0.45.1, not a stable jj contract; only entry semantics should be relied on.
- Conflicted working-copy parents: `build_index_from_merged_tree` writes conflict stages into the
  index; not exercised here. Lane `@` can transiently hold conflicts after a push-retry rebase, so
  the index shape in that state is untested.
- Multi-workspace repos (`jj workspace`), `jj sparse`, Windows and NFS/Dropbox were not tested.
- The concurrent `git add` vs jj snapshot race is inferred from code and the `index.lock` rename,
  not reproduced.
- `jj git export` in non-colocated repos was out of scope and not tested.
- jj ≥0.46 behavior is unknown; the snapshot/finish code paths are under active development and
  this fork may carry patches.
- One subtlety seen but not fully investigated: the index write on snapshot adds an `EOIE`
  extension even when no entries change. Harmless in all tests here (`git add`/`write-tree`/`fsck`
  clean), but it means `.git/index`'s sha256/mtime changes on most jj commands even when the index
  is semantically identical — do not use index mtime as a change signal.

## Experiment index

All commands ran under `/fast/scratch/jj-wave/JjDocGitIndex/<case>/` with `git init` +
`jj git init --colocate`; user identity via a sandbox `--config-file`, never repo-global config.
The sandbox (including the `v0.45.1` clone and the instrumented debug build) was removed after this
report; outputs are quoted above.
