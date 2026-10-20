# JjDocAutoTrack — snapshot.auto-track, `jj file track`/`untrack`, max-new-file-size, snapshotting commands, `--ignore-working-copy` (jj 0.45.x)

Seat: JjDocAutoTrack-2 · Date: 2026-10-20
Binary: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, `git 2.56.0`
Sandbox: `/fast/scratch/jj-wave/JjDocAutoTrack/` (fresh `git init -b main` + `jj git init --colocate` per experiment; a bare repo in the sandbox served as `origin` for the fetch/push checks). No live lane or fleet repo was given to any `jj` command; no installs or upgrades were needed. Source citations are from a `git clone --depth 1 --branch v0.45.1 https://github.com/jj-vcs/jj.git` into the sandbox; docs citations are the versioned v0.45.0 site (the same pages the binary's `jj help -k config` renders).

Method: docs answer → source confirmation → minimal experiment. Every behavioral statement below has a command and its output. Anything not run is listed under **Open uncertainties**.

---

## Findings

### 1. `snapshot.auto-track` — which *new* paths become tracked, as a fileset

**Observed facts**

- The default is `all()` and the size default is `1MiB`:

```
$ jj config get snapshot.auto-track
all()
$ jj config list --include-defaults | grep -i snapshot
fsmonitor.watchman.register-snapshot-trigger = false
snapshot.max-new-file-size = "1MiB"
snapshot.auto-track = "all()"
snapshot.auto-update-stale = false
```

- It is a fileset expression, so `all()`, `none()`, `glob:**/*.md`, unions and exclusions are legal (`jj help -k filesets`; `- `all()`: Matches everything.` / `- `none()`: Matches nothing.`).
- With the default, a new file is tracked by the next snapshotting command (`jj st` was enough):

```
$ echo hi > a.txt && jj st
Working copy changes:
A a.txt
Working copy  (@) : mwnoptwm 7e69b43f (no description set)
Parent commit (@-): oltykxqp 3e3cf506 main | (empty) base
```

- With `none()`, new files are not tracked and `jj st` reports them under a separate `Untracked paths:` section:

```
$ jj --ignore-working-copy config set --repo snapshot.auto-track '"none()"'
$ echo a > a.txt; mkdir sub; echo b > sub/b.txt; jj st
Untracked paths:
? a.txt
? sub/
Working copy  (@) : uxxklvks 6bf86046 (empty) (no description set)
Parent commit (@-) : uyyouovx 6e619e10 main | (empty) base
$ jj --ignore-working-copy file list -r @
(no output)
```

- A selective pattern tracks only matches:

```
$ jj --ignore-working-copy config set --repo snapshot.auto-track '"glob:**/*.md"'
$ echo m > notes.md; echo t > code.txt; mkdir docs; echo d > docs/design.md; jj st
Working copy changes:
A docs/design.md
A notes.md
Untracked paths:
? code.txt
```

- The config is consulted only for files that are **new to the working copy** (no file state yet), not for already-tracked files. Switching to `none()` after a file was tracked leaves it tracked and its later modification still snapshots:

```
$ echo m > notes.md; jj st            # A notes.md
$ jj --ignore-working-copy config set --repo snapshot.auto-track '"none()"'
$ echo more >> notes.md; jj st
Working copy changes:
A notes.md
```

- Ignore rules win over `auto-track` (see §5), and an already-tracked file that becomes ignored stays tracked (see §5).
- `jj git init --colocate` itself snapshots the working copy with the config in effect, so the per-command `--config` on init is load-bearing, not cosmetic:

```
# with --config snapshot.auto-track="none()"
$ echo pre > preexisting.txt; mkdir loose; echo q > loose/q.txt
$ jj --config 'snapshot.auto-track="none()"' git init --colocate .
Done importing changes from the underlying Git repo.
Initialized repo in "."
$ jj --ignore-working-copy file list -r @
(no output)

# without it (default all())
$ jj git init --colocate .
Done importing changes from the underlying Git repo.
Initialized repo in "."
$ jj --ignore-working-copy file list -r @
pre.txt
scratch/s.txt
```

**Citations**

- `jj help -k config`, “Paths to automatically track”: “You can set the `snapshot.auto-track` to set which paths get automatically tracked when they're added to the working copy.” (19 words)
- https://docs.jj-vcs.dev/v0.45.0/config/#paths-to-automatically-track — same sentence, plus “Files with paths matching ignore files are never tracked automatically.”
- https://docs.jj-vcs.dev/v0.45.0/working-copy/ — “If you set `snapshot.auto-track` to a non-default value, untracked files can be tracked with `jj file track`.”
- CHANGELOG 0.22.0 (https://github.com/jj-vcs/jj/blob/v0.45.1/CHANGELOG.md): “The new config option `snapshot.auto-track` lets you automatically track only the specified paths (all paths by default).” (20 words)
- Source: `snapshot_working_copy()` builds `auto_tracking_matcher` from `snapshot.auto-track` and passes it as `start_tracking_matcher` (`cli/src/cli_util.rs:2088-2100`, https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/cli_util.rs#L2088-L2100); `SnapshotOptions.start_tracking_matcher` is documented “For new files that are not already tracked” (`lib/src/working_copy.rs:214-226`, https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/working_copy.rs#L210-L246).

**Consequence for the integration.** Lanes must persist `snapshot.auto-track="none()"` in the repo config *before* any snapshot-capable command, and must keep passing it to `jj git init --colocate`; otherwise init itself registers every pre-existing scratch file in `@` (second block above), and the subsequent export writes intent-to-add entries into the Git index. `jj-lane.sh init` does exactly this; do not “simplify” the per-command `--config` away.

---

### 2. `jj file track` — records tracking state, does **not** rewrite `@`

**Observed facts**

- Help text and flag:

```
$ jj help file track
Start tracking specified paths in the working copy
Without arguments, all paths that are not ignored will be tracked.
By default, new files in the working copy are automatically tracked, so this command has no effect.
...
      --include-ignored
          Track paths even if they're ignored or too large
```

  The “Without arguments” sentence is stale: the positional argument is required in 0.45.1.

```
$ jj file track
error: the following required arguments were not provided:
  <FILESETS>...
...
rc=2
```

- `jj file track <path>` updates the working copy's tracking state immediately, but the path only enters `@` at the **next snapshot**. Immediately after tracking, a `--ignore-working-copy` read still shows an empty commit; the next normal command folds it in:

```
$ echo x > f.txt
$ jj file track f.txt; echo rc=$?
rc=0
$ jj --ignore-working-copy file list -r @
(no output)
$ jj --ignore-working-copy diff -r @ --summary
(no output)
$ jj st
Working copy changes:
A f.txt
$ jj --ignore-working-copy file list -r @
f.txt
```

  Source confirms it: `cmd_file_track` snapshots with the matcher as `start_tracking_matcher` and discards the returned tree (`let (_tree, track_stats) = ...`) instead of calling `set_wc_commit`; only the file state persists (`cli/src/commands/file/track.rs:55-78`, https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/commands/file/track.rs#L55-L70).

- `--include-ignored` sets `force_tracking_matcher`, which overrides **both** ignore rules and the size limit (`lib/src/local_working_copy.rs:1640-1710`, https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/local_working_copy.rs#L1640-L1710):

```
$ jj file track --include-ignored i.log     # i.log matches *.log
rc=0
$ jj st
Working copy changes:
A .gitignore
A i.log
A t.txt
```

- Without the flag, tracking an ignored path is a **silent no-op with exit 0** — no warning, file remains ignored and absent from `@`:

```
$ jj file track i.log; echo rc=$?
rc=0
$ jj st
Working copy changes:
A .gitignore
(no i.log)
$ git status --porcelain
 A .gitignore
$ git ls-files
.gitignore
```

- Tracking an ignored **directory** is likewise a silent no-op (the visitor only re-walks already-tracked files under an ignored dir):

```
$ printf 'cachedir/\n' > .gitignore; mkdir cachedir; echo x > cachedir/x.txt; jj st   # A .gitignore
$ jj file track -- cachedir; echo rc=$?
rc=0
$ jj --ignore-working-copy file list -r @
.gitignore
```

- Tracking a normal directory tracks its non-ignored files and skips ignored ones:

```
$ mkdir dir; echo keep > dir/keep.txt; printf '*.log\n' > .gitignore; echo skip > dir/skip.log
$ jj file track -- dir
$ jj st
Working copy changes:
A dir/keep.txt
Untracked paths:
? .gitignore
```

- But `--include-ignored` on a directory force-tracks *everything* beneath it, including ignored and oversized files — the exact opposite of the “like `git add <dir>`” intent:

```
$ head -c 2097152 /dev/zero | tr '\0' 'w' > d/big.bin; echo i > d/i.log; echo k > d/keep.txt
$ jj file track --include-ignored -- d
$ jj st
Working copy changes:
A d/big.bin
A d/i.log
A d/keep.txt
```

- Tracking a path that does not exist also exits 0 with no output:

```
$ jj file track -- nope.txt; echo rc=$?
rc=0
```

**Citations**

- `jj help file track`: “By default, `jj file track` will not track files that are ignored by .gitignore or exceed the maximum file size.” (20 words) and “`--include-ignored`: Track paths even if they're ignored or too large”.
- CHANGELOG 0.35.0: “`jj file track` now accepts an `--include-ignored` flag to track files that are ignored by `.gitignore` or exceed the `snapshot.max-new-file-size` limit.” (21 words)
- Source: `start_tracking_matcher` / `force_tracking_matcher` semantics, `lib/src/working_copy.rs:210-246`; visitor branches `local_working_copy.rs:1646-1705`.

**Consequence for the integration.** `jj-lane.sh commit` is correct to pass `--include-ignored` **only for files** and to track directories without it; passing it for a directory would sweep caches and >1 MiB artifacts into the commit (last-but-one experiment). The helper’s follow-up `jj diff --summary -- <paths>` is essential: it is the snapshot that actually moves the newly tracked paths into `@`, and it is also the “nothing to commit” probe. Treat “track exited 0” as “state recorded”, never as “path is in the commit”; the only reliable signal is the non-empty diff. Because all failure modes except missing args exit 0, the helper cannot rely on the exit code to detect ignored/oversized/nonexistent paths — its pre-check for path existence and its diff gate are the real guards.

---

### 3. `jj file untrack` — removes from `@`, keeps the file, requires that it won't come back

**Observed facts**

- On a tracked, non-ignored file under the default `all()`, untrack refuses and the file would be re-added:

```
$ jj file untrack note.txt
Error: 'note.txt' is not ignored.
Hint: Files that are not ignored will be added back by the next command.
Make sure they're ignored, then try again.
rc=1
```

- After adding it to `.gitignore`, untrack succeeds; the file stays on disk and leaves `@`:

```
$ printf 'note.txt\n' > .gitignore
$ jj file untrack note.txt; echo rc=$?
rc=0
$ jj st
Working copy changes:
A .gitignore
$ ls
note.txt
```

- The actual acceptance condition is “the next snapshot would not re-add it”, not literally “is ignored”. With `snapshot.auto-track="none()"`, untracking a **non-ignored** file succeeds (docs/help are stricter than the implementation):

```
# auto-track=none(); f.txt and note.txt were tracked explicitly
$ jj file untrack note.txt; echo rc=$?
rc=0
```

- Source: untrack rewrites the working-copy commit without the matched paths, resets the working copy, re-snapshots with the *auto-track* matcher, and only errors if a path comes back; it then calls `export_working_copy_changes_to_git` in colocated repos (`cli/src/commands/file/untrack.rs:49-124`, https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/commands/file/untrack.rs#L49-L100).

**Citations**

- `jj help file untrack`: “Paths to untrack. They must already be ignored.” (8 words) — contradicted by the auto-track-`none()` experiment.
- https://docs.jj-vcs.dev/v0.45.0/working-copy/ — “You can use `jj file untrack` to untrack a file while keeping it in the working copy.” and “first ignore them or remove them from the `snapshot.auto-track` patterns”.

**Consequence for the integration.** Lanes do not currently call untrack, so nothing to change. If a lane ever needs to drop a path from `@`, the safe recipe is: add it to `.gitignore` first, then `jj file untrack <path>`; with `auto-track="none()"` the ignore step is redundant. The help text’s “must already be ignored” is not the real rule; do not build logic that assumes an untrack refusal when the path is not ignored.

---

### 4. `snapshot.max-new-file-size` — anti-footgun cap for *new* files, warning not error

**Observed facts**

- Default 1 MiB (`snapshot.max-new-file-size = "1MiB"` from `jj config list --include-defaults`, above). A 2 MiB new file is refused with a warning and left untracked; the command still succeeds:

```
$ head -c 2097152 /dev/zero | tr '\0' 'x' > big.bin
$ jj st
Warning: Refused to snapshot some files:
  big.bin: 2.0MiB (2097152 bytes); the maximum size allowed is 1.0MiB (1048576 bytes)
Hint: This is to prevent large files from being added by accident. To fix this:
  * Add the file(s) to `.gitignore`
  * Run `jj config set --repo snapshot.max-new-file-size 2097152`
  * Run `jj --config snapshot.max-new-file-size=2097152 status`
Untracked paths:
? big.bin
```

  The same warning (plus a `jj file track --include-ignored big.bin` hint) is printed by `jj file track big.bin`, which exits 0 without tracking it.

- Human-readable sizes are accepted, and the configured cap applies at snapshot time:

```
$ jj --ignore-working-copy config set --repo snapshot.max-new-file-size '"3MiB"'
$ jj st
Working copy changes:
A big.bin
```

- `0` disables the limit; already-tracked files are exempt even with a 1-byte cap:

```
$ jj --config snapshot.max-new-file-size=0 file track big.bin
$ jj st
Working copy changes:
A big.bin
$ echo more >> big.bin
$ jj --config snapshot.max-new-file-size=1 st
Working copy changes:
A big.bin          # tracked file still snapshotted
```

**Citations**

- `jj help -k config`, “Maximum size for new files”: “`jj` will refuse to add new files to the snapshot that are larger than a certain size; the default is 1MiB” (21 words), “Files that already exist in the working copy are not subject to this limit.” (14 words), “Setting this value to zero will disable the limit entirely.” (10 words).
- https://docs.jj-vcs.dev/v0.45.0/config/#maximum-size-for-new-files — same paragraphs.
- CHANGELOG 0.35.0: `--include-ignored` overrides the size limit (quote in §2).

**Consequence for the integration.** The helper’s `--include-ignored` on named files is the *only* reason a lane can commit a >1 MiB generated artifact it explicitly named. Without it, the snapshot warning is not an error and the file silently stays out of the commit, so a success report could cite a hash that lacks the artifact. For directories, the cap is the correct behavior (large build products stay untracked with a warning) — keep directories unforced.

---

### 5. Ignored vs untracked files

**Observed facts**

- Ignored files are never auto-tracked, are omitted from `@`, and are not even listed under `Untracked paths:`:

```
$ printf '*.log\n' > .gitignore; echo tracked > t.txt; echo ignored > i.log; jj st
Working copy changes:
A .gitignore
A t.txt
$ jj --ignore-working-copy file list -r @
.gitignore
t.txt
```

- A file that is already tracked stays tracked after it matches an ignore pattern:

```
$ echo t > tracked.log && jj st            # A tracked.log
$ printf '*.log\n' > .gitignore && jj st
Working copy changes:
A .gitignore
A tracked.log
$ jj --ignore-working-copy file list -r @
.gitignore
tracked.log
```

- Untracked files are reported by `jj status` (`? path`, directories collapsed to `? dir/`), never enter `@`, and are invisible to pathspec commits. Committing a path that was never tracked warns and still creates an empty commit, exit 0:

```
$ jj --ignore-working-copy config set --repo snapshot.auto-track '"none()"'
$ echo u > untracked.txt
$ jj commit -m msg -- untracked.txt
Warning: The given paths do not match any file: untracked.txt
Working copy  (@) now at: mxrkuyqu fbaf11fa (empty) (no description set)
Parent commit (@-)      : pswmlyzo 1f69c414 (empty) msg
rc=0
```

  `jj-lane.sh` avoids this trap with its `jj diff --summary` gate, which is empty for untracked paths.

- `jj git init --colocate` snapshots pre-existing files under the default `all()` (see §1); the per-command `--config` prevents that.

**Citations**

- https://docs.jj-vcs.dev/v0.45.0/working-copy/#ignored-files — “Ignored files are never tracked automatically (regardless of the value of `snapshot.auto-track`)” (12 words) and “files that were already tracked will remain tracked even if they match ignore patterns” (15 words).
- https://docs.jj-vcs.dev/v0.45.0/working-copy/ — “Most `jj` commands you run will commit the working-copy changes if they have changed.” (15 words)
- Source: the ignore check precedes the `start_tracking_matcher` check and applies only when `maybe_current_file_state.is_none()` (`lib/src/local_working_copy.rs:1670-1705`).

**Consequence for the integration.** With `auto-track="none()"`, ignored and untracked files are both outside `@`; the only difference is visibility (`jj st` lists untracked, not ignored) and that `jj file track` can be forced over either. Seat scratch that matches `.gitignore` is invisible to every lane command; seat scratch that does not match is listed by `jj st` but never committed unless named. Neither case can leak into a pathspec-limited commit.

---

### 6. Which commands snapshot the working copy

**Observed facts (matrix).** One repo, default `all()`; before each command a fresh `probe-<name>.txt` was created; after the command, `jj --ignore-working-copy file list -r @` was checked for the probe, then the probe was deleted and a snapshot taken to reset.

```
jj status                    rc=0 SNAPSHOTTED
jj log                       rc=0 SNAPSHOTTED
jj diff                      rc=0 SNAPSHOTTED
jj show                      rc=0 SNAPSHOTTED
jj bookmark list             rc=0 SNAPSHOTTED
jj file list                 rc=0 SNAPSHOTTED
jj config list               rc=0 not-snapshotted
jj op log                    rc=0 SNAPSHOTTED
jj root                      rc=0 not-snapshotted
jj debug working-copy        rc=0 not-snapshotted
jj sparse list               rc=0 SNAPSHOTTED
jj workspace list            rc=0 SNAPSHOTTED
jj tag list                  rc=0 SNAPSHOTTED
jj operation log             rc=0 SNAPSHOTTED
jj util snapshot             rc=0 SNAPSHOTTED
```

Additional observations:

- `jj git fetch` and `jj git push` snapshot before doing their work (probe file present in `@` afterwards; push reported its bookmark-tracking error *after* the snapshot).
- `jj config set --repo user.name …` / `user.email` snapshots, because the author warning calls `command.workspace_helper()`; other keys (e.g. `ui.color`, `snapshot.auto-track`) do not:

```
$ echo p > probe.txt
$ jj config set --repo ui.color never          # no snapshot
$ jj --ignore-working-copy file list -r @
(no output)
$ jj config set --repo user.name Tester2
Warning: This setting will only impact future commits. ...
$ jj --ignore-working-copy file list -r @
probe.txt
```

- `jj util snapshot` exists precisely to force a snapshot from scripts: “Snapshots the working copy and updates the working-copy commit if the working copy has changed since the last snapshot.”

**Citations**

- https://docs.jj-vcs.dev/v0.45.0/working-copy/ — “Almost all commands go through three main steps: Snapshot the working copy (which gets recorded as an operation)”.
- `jj help` global options — “By default, Jujutsu snapshots the working copy at the beginning of every command.”
- Source: `workspace_helper()` → `workspace_helper_with_stats()` → `snapshot_impl()`; the latter performs Git HEAD import, the working-copy snapshot, then Git ref import (`cli/src/cli_util.rs:1331-1372`, https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/cli_util.rs#L1331-L1372). Commands that must not snapshot call `workspace_helper_no_snapshot()`: “Loads workspace and repo, but never snapshots the working copy.” (16 words) — used by `jj root`, `jj debug object`, `jj debug working-copy`, `jj operation integrate`, `jj util backend name`, `jj bench revset` (https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/cli_util.rs#L523).
- Commands that never load a workspace (`jj git init`, `jj git clone`, `jj config list`, `jj help`, `jj version`, `jj util completion`) therefore do not snapshot. `jj config set` is the exception described above (`cli/src/commands/config/set.rs:95-115`).

**Consequence for the integration.** “Read-only” is not the same as “does not mutate the working copy state”: `jj log`, `jj diff`, `jj bookmark list`, `jj op log`, `jj git fetch` and `jj git push` all write a snapshot operation and export working-copy changes to the Git index first. Lane scripts that want a pure read must pass `--ignore-working-copy` (the helper does for `jj_ids`, `state`, and bookmark/config writes). Conversely, anything that must see fresh working-copy content (the helper’s `jj diff --summary` gate and `jj commit`) must *not* pass the flag.

---

### 7. `--ignore-working-copy` — exactly what it skips

**Observed facts**

- Global option text:

```
      --ignore-working-copy
          Don't snapshot the working copy, and don't update it
          By default, Jujutsu snapshots the working copy at the beginning of every command. The
          working copy is also updated at the end of the command, if the command modified the
          working-copy commit (`@`).
...
          Loading the repository at a specific operation with `--at-operation` implies
          `--ignore-working-copy`.
```

- It skips the **snapshot**, so reads are stale: after modifying `f.txt` from `v1` to `v2`, the flag reports `v1`; the next normal command reports `v2`:

```
$ jj --ignore-working-copy diff -r @
Added regular file f.txt:
        1: v1
$ jj diff -r @
Added regular file f.txt:
        1: v2
```

- It skips the **implicit Git import** in colocated repos. A branch created with plain `git` is invisible to flagged commands and appears only after a normal command:

```
$ git checkout -b side && git commit -m gitside
$ jj --ignore-working-copy log -r side
Error: Revision `side` doesn't exist
$ jj --ignore-working-copy bookmark list
main: xvxlqrmm d8b37cdf (empty) base
$ jj log -r side
Reset the working copy parent to the new Git HEAD.
Done importing changes from the underlying Git repo.
○ krtmyttv t@example.com 2026-10-20 11:13:53 side d914286c
│ (empty) gitside
```

- It skips **Git HEAD import** too: after `git checkout main`, a flagged read still shows the old parent; the next normal command resets `@`'s parent to the new HEAD:

```
$ git checkout main
$ jj --ignore-working-copy log -r '@-' --no-graph -T 'commit_id.short() ++ " " ++ bookmarks ++ "\n"'
d914286c8592 side
$ jj st
Reset the working copy parent to the new Git HEAD.
Working copy  (@) : lvzkynqy e7cf1225 (empty) (no description set)
Parent commit (@-): xvxlqrmm d8b37cdf main | (empty) base
$ jj --ignore-working-copy log -r '@-' --no-graph -T ...
d8b37cdf9198 main
```

- It skips the **export of working-copy changes to the Git index**: a new file stays `??` under the flag and becomes intent-to-add (` A`) only on a normal snapshot:

```
$ git status --porcelain          # after normal snapshot
 A a.txt
$ echo n > newfile.txt
$ jj --ignore-working-copy st
$ git status --porcelain
 A a.txt
?? newfile.txt
$ jj st
$ git status --porcelain
 A a.txt
 A newfile.txt
```

- It does **not** disable an explicit `jj git import`: the command still imports Git refs (but not HEAD):

```
$ git checkout -b newgit && git commit -m fromgit
$ jj --ignore-working-copy git import
bookmark: newgit@git [new] tracked
rc=0
$ jj --ignore-working-copy log -r newgit
○ ppxolnyl t@example.com ... newgit de35531c
```

- It does **not** suppress Git ref export for bookmark writes: `jj --ignore-working-copy bookmark set main -r @-` updated `.git/refs/heads/main` (verified with `git for-each-ref`/`git log main`), so git-based fleet tools keep seeing lane bookmarks.

- It skips the **working-copy update** after a mutating command, leaving the workspace stale and normal commands erroring:

```
$ jj --ignore-working-copy edit @--        # @ moves to c1 (tree has A); file stays B
$ cat a.txt
B
$ jj st
Error: The working copy is stale (not updated since operation ea271c766aba).
Hint: Run `jj workspace update-stale` to update it.
$ jj --ignore-working-copy log -r @        # flagged reads still work
c13f3e59ee0d
$ jj workspace update-stale
...
Updated working copy to fresh commit c13f3e59ee0d
$ cat a.txt
A
```

- Source confirmation: `maybe_snapshot()` returns immediately when `may_snapshot_working_copy` is false (`= !ignore_working_copy`), so the whole `snapshot_impl()` — `import_git_head()`, `snapshot_working_copy()`, `import_git_refs()` — is skipped (`cli/src/cli_util.rs:1364-1372`, https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/cli_util.rs#L1364-L1372). `may_update_working_copy = may_snapshot_working_copy && should_commit_transaction()` (`cli/src/cli_util.rs:1279-1280`), so the end-of-command checkout is skipped as well.

**Citations**

- `jj help` global options (excerpts above, 10 and 13 words).
- Source comment on `maybe_snapshot()`: “Snapshots the working copy if allowed, and imports Git refs if the working copy is colocated with Git.” (20 words) — the expiry of the early return is the whole story.
- https://docs.jj-vcs.dev/v0.45.0/working-copy/#stale-working-copy — “If step 3 doesn't happen for some reason, the working copy is considered "stale".”

**Consequence for the integration.** `--ignore-working-copy` is safe and correct for the helper’s pure reads (`jj_ids` log calls, `print_state` is git-only anyway) and for config/bookmark writes, because bookmark writes still export to `.git` and HEAD/refs import is only skipped, not lost. It is unsafe on any command that moves `@` (edit/rebase/commit/new/abandon) — it would leave the lane stale and every subsequent un-flagged command would fail with the stale error. Two specific lane hazards follow from the skip list: (a) a raw `git fetch` in a colocated lane is invisible to the helper’s flagged reads of `main@origin` until some snapshotting jj command runs, so lanes must fetch through `jj git fetch` only; (b) a raw `git commit`/`git checkout` changes Git HEAD and the next jj snapshot silently resets `@`’s parent (observed above), so lane writes must stay in jj. `jj-lane.sh` currently follows both rules.

---

### 8. Adjacent observation: `jj git push` needs the remote bookmark tracked

Not part of the assigned questions but hit while testing push:

```
$ jj git push --bookmark main
Error: Non-tracking remote bookmark main@origin exists
Hint: Run `jj bookmark track main@origin` to import the remote bookmark.
```

`jj bookmark track main@origin` then makes push a clean no-op/push. `jj-lane.sh init` runs `bookmark track "${branch}@origin" … || true`, so a failed or skipped track is swallowed at init and every later push fails with this error (the retry loop does not re-run tracking). Worth an explicit post-track verification in init rather than `|| true`. [INFERENCE: track fails when the remote bookmark does not exist yet at init time; the helper should treat that as “push will need tracking after the first fetch”.]

---

## Consequence summary for the planned shokunin integration

1. **Keep `--config snapshot.auto-track="none()"` on `jj git init --colocate` and the repo-config write before any other jj command.** Init itself snapshots (observed); without the config it registers every pre-existing seat-scratch file in `@`. The `--ignore-working-copy` on the config writes is still worth keeping: `jj config set --repo user.name|user.email` snapshots (author check), other keys do not — but the flag makes the sequence order-independent and cheap.
2. **`jj file track` is a state write, not a commit write.** The path enters `@` only at the next snapshot. The helper’s `jj diff --summary -- <paths>` is load-bearing both as the snapshot and as the nothing-to-commit gate.
3. **Exit codes lie for `jj file track`.** Ignored, oversized, and nonexistent paths all exit 0 (missing args exits 2). Only a non-empty `jj diff --summary` proves the path is in `@`.
4. **Files may use `--include-ignored`; directories must not.** For a directory, the flag force-tracks ignored and oversized descendants — caches and large artifacts would land in the commit. The current helper matches this rule.
5. **>1 MiB named files rely on `--include-ignored`.** Without it they are warned about and silently left untracked (exit 0); a “committed” report could omit the artifact.
6. **Untracked ≠ ignored, but with `auto-track="none()"` both are outside `@`.** Ignored files are invisible to `jj st`; untracked files are listed (`? path`) but never committed by a pathspec commit (which warns and creates an empty commit if you force it). The diff gate prevents empty lane commits.
7. **“Read-only” jj commands still snapshot and export to the Git index.** `jj log`, `jj diff`, `jj status`, `jj bookmark list`, `jj op log`, `jj git fetch`, `jj git push` all mutate working-copy state. Pure reads must use `--ignore-working-copy`; content checks must not.
8. **`--ignore-working-copy` skips snapshot, Git HEAD import, Git ref import, working-copy checkout, and index export.** It does not skip explicit `jj git import`, nor Git ref export for bookmark writes. Therefore: never mix raw `git fetch`/`git commit`/`git checkout` into a lane; use `jj git fetch` and jj mutations. Never put the flag on commands that move `@`, or the lane goes stale.
9. **Track `origin/<branch>` at init and verify it.** A non-tracking remote bookmark makes every `jj git push` fail with `Non-tracking remote bookmark … exists`; `|| true` on the track call hides that failure.
10. **No behavior in this report requires `snapshot.max-new-file-size` changes.** Default 1 MiB plus `--include-ignored` for named files is exactly what the lane contract needs; `0` would disable the anti-footgun for every unnamed file and is not recommended.

---

## Open uncertainties

- Binary tested is 0.45.1; the versioned docs are v0.45.0. CHANGELOG 0.45.1 lists only crate-publishing and SHA-256 signature fixes, so behavior is expected identical. [INFERENCE, not separately executed on 0.45.0.]
- The silent no-op of `jj file track` for ignored/oversized/nonexistent paths is observed; whether it is intended UX or a bug is not stated by the docs (the docs only say such files “will not” be tracked). No warning is printed, which is an easy way for a script to believe it tracked something it did not.
- `jj help file track` says “Without arguments, all paths that are not ignored will be tracked”, but the argument is required (`rc=2`). Help-text inconsistency in 0.45.1; no “track all” path exists.
- `jj help file untrack` says “They must already be ignored”, but the code accepts any path the next snapshot will not re-add (observed with `auto-track="none()"`). Docs are stricter than the implementation.
- Not tested: `fsmonitor.backend="watchman"`, watchman snapshot triggers, sparse patterns, multiple workspaces, stale-workspace auto-update (`snapshot.auto-update-stale=true`), submodules, symlinks, non-UTF-8 filenames, case-insensitive filesystems.
- Not tested: invalid `snapshot.auto-track` expressions (parse-error text), and interaction of `auto-track` with `.gitignore` negation patterns.
- Not tested: `jj file track --include-ignored` combined with `jj file untrack` on the same path in one session; and whether an explicitly force-tracked ignored file is re-snapshotted after it is removed from disk and recreated with a new mtime.
- Repo-config precedence over user-config for `snapshot.auto-track` was not tested against a conflicting user-level value; the helper sets repo scope, which is expected to win. [INFERENCE from jj config layering.]
- The push/tracking observation (§8) was reproduced once; the exact condition under which `bookmark track` fails at lane-init time (remote bookmark absent, no `origin` remote refs yet) was not enumerated.

---

## Environment / installs

- No packages installed or upgraded. `jj 0.45.1` and `git 2.56.0` were already present; versioned docs and the v0.45.1 source were fetched into the sandbox for citation.
- Experiments ran only in `/fast/scratch/jj-wave/JjDocAutoTrack/exp/e1..e35`; the only remote was `../remote.git` (a sandbox bare repo), confirmed with `git remote -v` before any push. No live lane repo or fleet-root repo received a `jj` invocation.
- Sandbox removed after the report was written; all commands and outputs needed to reproduce it are in this file.
