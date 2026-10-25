# JjDocLargeRepo — snapshot performance on large working trees (jj 0.45.x)

Seat: `JjDocLargeRepo-2` (leaf scout, no subagents).
Tooling under test: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` (binary `/home/vgpnk/.local/bin/jj`), `git 2.56.0`, Arch, 32 cores, `/fast` on nvme.
Sandbox: `/fast/scratch/jj-wave/JjDocLargeRepo/` — repos `r1`…`r19` were used; `r16`, `r18`, `r19` are retained (§6).

Docs citation policy: the site is mike-versioned; `https://jj-vcs.github.io/jj/latest/config/` currently redirects to the **v0.46.0** docs (`versions.json`: `{"version":"v0.46.0","aliases":["latest"]}`). Every doc quote below is taken from the 0.45-matching tree, <https://docs.jj-vcs.dev/v0.45.1/> (the `jj-vcs.github.io/jj/<ver>/…` forms redirect there; `…/0.45.1/…` without the `v` is a 404).

Compliance: **no `jj` command was ever run with cwd/`-R` inside `/home/vgpnk/Projects/shokunin`**; that repo was only read with `git ls-files`, `git status`, `git check-ignore`, `find`, `du`, `sed`/`grep`. No remote was contacted by any `jj git push`/`fetch` (none were run at all). No installs were performed.

Load caveat: six live lane rounds were running. `/proc/loadavg` moved between `3.35 2.55` and `9.13 3.85` during the measurements, and absolute wall times moved by 4–5x between the two regimes (see F8). The *contrasts* (10–20 ms vs seconds) reproduced in both regimes; the absolute seconds are a lower bound on a quiet host, not a spec.

---

# 1. Findings (observed facts)

## F1. `fsmonitor.backend` is opt-in; the only backends are `none` (default) and `watchman`

Citations
- `jj help -k config`, § *Filesystem monitor*:
  > This is governed by the `fsmonitor.backend` option. Currently, the valid values are `"none"` or `"watchman"`.
- Docs (0.45.1): <https://docs.jj-vcs.dev/v0.45.1/config/#filesystem-monitor>
  > In large repositories, it may be beneficial to use a "filesystem monitor" to track changes to the working copy.

Evidence — defaults (`r1`)

```
$ jj config list --include-defaults | grep -iE 'fsmonitor|snapshot.auto-track|max-new-file-size|git.colocate'
fsmonitor.backend = "none"
fsmonitor.watchman.register-snapshot-trigger = false
git.colocate = true
snapshot.max-new-file-size = "1MiB"
snapshot.auto-track = "all()"
```

Evidence — it is an ordinary setting, so it can be repo-scoped (`r3`)

```
$ jj config set --repo fsmonitor.backend '"watchman"'
$ jj debug watchman status
Watchman is enabled via `fsmonitor.backend`.
Background snapshotting is disabled. Use `fsmonitor.watchman.register-snapshot-trigger` to control it.
Internal error: Failed to access working copy state
Caused by:
1: Failed to query watchman
2: Filesystem monitor error
3: Could not connect to Watchman
4: While invoking the watchman CLI to discover the server connection details: No such file or directory (os error 2), stderr=``
```

## F2. jj does not read git's `core.fsmonitor`; the pre-0.39 jj aliases are gone

Citations
- CHANGELOG 0.39.0 (<https://github.com/jj-vcs/jj/blob/v0.45.1/CHANGELOG.md>):
  > The following deprecated config options have been removed: … `core.fsmonitor` … `core.watchman.register-snapshot-trigger`

Source (0.45.1, read-only copy in sandbox)
- `lib/src/fsmonitor.rs` `FsmonitorSettings::from_settings` reads exactly one key: `"fsmonitor.backend"` (`none` | `watchman`; `"test"` is rejected with *"Cannot use test fsmonitor in real repository"*).
- `lib/src/git_subprocess.rs:124` forces `-c core.fsmonitor=false` on every git subprocess it spawns (workaround for jj issue #6440; comment: *"Nothing we're doing in `jj` interacts with this daemon"*).
- `grep -rn "core.fsmonitor\|untrackedCache" --include=*.rs` over the 0.45.1 tree: only that one hit.

Evidence (`r12`)

```
$ jj config set --repo core.fsmonitor watchman     # accepted as an inert key
$ jj config list --repo | grep fsmonitor
core.fsmonitor = "watchman"
$ jj debug watchman status | head -1
Watchman is disabled. Set `fsmonitor.backend="watchman"` to enable.
```

## F3. A missing/broken watchman is a **silent** fallback; every command still succeeds

Source: `lib/src/local_working_copy.rs::make_fsmonitor_matcher`

```rust
FsmonitorSettings::Watchman(config) => match self.query_watchman(config).await {
    Ok((watchman_clock, changed_files)) => (Some(watchman_clock.into()), changed_files),
    Err(err) => {
        tracing::warn!(?err, "Failed to query filesystem monitor");
        (None, None)
    }
}
```

`(None, None)` becomes `EverythingMatcher` — i.e. a full working-copy walk. Only `--debug` surfaces it:

```
$ jj st                                  # r3, backend=watchman, no watchman installed
The working copy has no changes.
Working copy  (@) : knvzowlz b1e69094 (empty) (no description set)
$ echo $?
0
$ jj --debug st 2>&1 | grep -i watchman
… WARN … snapshot:make_fsmonitor_matcher: jj_lib::local_working_copy: Failed to query filesystem monitor
   err=Fsmonitor(WatchmanConnectError(ConnectionDiscovery { watchman_path: "watchman",
   reason: "No such file or directory (os error 2)", stderr: "" }))
```

Cost of the failed probe: 7–8 ms per command on an empty repo (`real 0m0.007s` ×3) — the CLI is spawned/dialed and fails each time.

## F4. jj's watchman query excludes only `.git` and `.jj`; `.gitignore` is *not* translated to watchman

Source `lib/src/fsmonitor.rs:317-336`:

```rust
fn build_exclude_expr(&self) -> expr::Expr {
    // TODO: consider parsing `.gitignore`.
    let exclude_dirs = [Path::new(".git"), Path::new(".jj")];
```

So watchman watches `node_modules/`, `target/`, `.venv/`, build output, etc. — exactly the inotify pressure the docs warn about:

> Note: `watchman` heavily uses `inotify` and sets up a user watch per-file. — <https://docs.jj-vcs.dev/v0.45.1/config/#watchman>

(jj still applies its own gitignore matcher to whatever watchman reports, so correctness is preserved; the cost lands on watchman/inotify.)

## F5. Any untracked path blocks the watchman clock from advancing

Source `lib/src/local_working_copy.rs:1413-1422`:

```rust
// Since untracked paths aren't cached in the tree state, we'll need to
// rescan the working directory changes to report or track them later.
// TODO: store untracked paths and update watchman_clock?
if (stats.untracked_paths.is_empty() && stats.invalid_utf8_paths.is_empty())
    || watchman_clock.is_none()
{ self.watchman_clock = watchman_clock; }
else { tracing::info!("not updating watchman clock because there are untracked files"); }
```

`stats.untracked_paths` is non-empty whenever jj has to show `? path` / `? dir/` — including every snapshot under `snapshot.auto-track = "none()"` (see F9 evidence: `? scratch/`). Since jj-lane.sh sets `auto-track = "none()"`, this applies to every lane.

## F6. Ignore handling: `.gitignore` anywhere, `.git/info/exclude`, `$XDG_CONFIG_HOME/git/ignore`, **and** undocumented git `core.excludesFile`

Citations
- <https://docs.jj-vcs.dev/v0.45.1/working-copy/#ignored-files>:
  > `.gitignore` files are supported in any directory in the working copy, as well as in `$XDG_CONFIG_HOME/git/ignore` and `$GIT_DIR/info/exclude`.
  > Ignored files are never tracked automatically (regardless of the value of `snapshot.auto-track`)
  > there's no such thing as `.jjignore` yet

Source `cli/src/cli_util.rs:1674-1712` (`base_ignores`): for a git-backed/colocated repo it reads `core.excludesFile` from the git config snapshot, **else** falls back to `$XDG_CONFIG_HOME/git/ignore` (or `~/.config/git/ignore`), then chains `.git/info/exclude`; per-directory `.gitignore` files are applied during the walk. Relative `core.excludesFile` paths resolve against the workspace root (note at line 1671).

Evidence — one repo, every source at once (`r5`)

```
$ cat .gitignore                     # root
gen/
*.log
neg/*
!neg/keep.me
$ cat sub/.gitignore ; cat .git/info/exclude ; cat $XDG_CONFIG_HOME/git/ignore
*.tmp                ; secret.txt            ; *.globalign
$ touch gen/g1.txt plain.txt sub/a.tmp sub/b.txt neg/n1.txt neg/keep.me d/secret.txt d/g.globalign logged.log
$ jj st | head -7
Working copy changes:
A .gitignore
A neg/keep.me          <- negation works
A plain.txt            <- positive control
A sub/.gitignore
A sub/b.txt
```

(`gen/g1.txt`, `logged.log`, `sub/a.tmp`, `neg/n1.txt`, `d/secret.txt`, `d/globalign` all absent from status. Both `.gitignore` files were themselves new and not yet committed, so ignore rules are read from the working tree, never from a commit.)

Evidence — git `core.excludesFile` is honored, though the docs never say so (`r9`, fresh repo, `core.excludesFile=…/customignore` containing `*.custom`)

```
$ jj st
Working copy changes:
A visible.txt
$ git status --short
 A visible.txt
```

`e.custom` is absent from both, then reappears as `A c.custom` after `git config --unset core.excludesFile` (`r7`). Note the one-way ratchet: once a file has been auto-tracked, adding an ignore rule later does **not** untrack it (same `r7`: `c.custom` stayed `A` after re-setting `core.excludesFile`; docs: *"files that were already tracked will remain tracked"*).

## F7. Ignoring a *directory* prunes it completely; a shell-glob ignore still lists it

`r16` — dirty repo (a tracked file modified, so no early-exit shortcut), `.gitignore = gen/`, 20 000 files under `gen/`:

```
$ jj st
Working copy changes:
M a.txt
real 0m0.011s
$ strace -f -qq -e trace=openat,newfstatat,getdents64 -o /tmp/r16.trace jj st
gen/ references in trace: 0
total traced syscalls: 34
```

`r19` — same 20 000 files, first ignored by the file glob `*.log`, then by the directory `logs/`:

| ignore pattern | `jj st` | syscalls | `getdents64` | `stat`-family |
|---|---|---|---|---|
| `*.log` | 0.011–0.018 s | 348 | 328 | 10 |
| `logs/` | 0.008–0.013 s | 34 | 14 | 10 |

Both are fast at 20 k files, but the file-glob form must read the directory (≈313 `getdents64` calls of 64 entries); the directory form never opens it. Directory-level ignores are the ones that stay O(1) as a build tree grows.

## F8. `snapshot.auto-track = "all()"` (the default) is what makes big generated trees expensive

Citations
- `cli/src/config-schema.json`: `"auto-track": { … "description": "Fileset pattern describing what new files to automatically track on snapshotting. By default all new files are tracked.", "default": "all()" }`
- <https://docs.jj-vcs.dev/v0.45.1/config/#paths-to-automatically-track>:
  > All new files in the working copy that don't match the ignore patterns are tracked by default.

Controlled matrix (`r18`), four fresh colocated repos, **identical 20 000-file `gen/` tree** (64-byte files), load 3.35→9.13:

```
$ jj st        # first run, then two warm runs; and `jj diff --summary -r @`
ignored ( `.gitignore=gen/` )          first 0.013  warm 0.009/0.007  diff 0.007
notrack ( auto-track="none()" )        first 0.017  warm 0.017/0.015  diff 0.015
fileset ( auto-track="all() ~ root:gen") first 0.015 warm 0.016/0.016 diff 0.016
default ( auto-track="all()" )         first 6.918  warm 6.868/6.810  diff 6.990
```

Same experiment under lighter load (`r1`, 20 000 files of 84 B each, 79 MB on disk, `snapshot.auto-track` default): first snapshot `2.370s`, then `1.430 / 1.523 / 1.518 / 1.418s` per command. Scaling point (`r17`, 2 000 files): first `0.086s`, warm `0.077s`, diff `0.075s` — i.e. ≈40–390 µs *per added tree entry*, load-dependent.

Where the time goes (`r1`, `r18/default`) — the **snapshot is cheap, the status/diff is not**:

```
$ jj util snapshot                                  # nothing new to snapshot
real 0m0.014s          (r18: 0.020s)
$ jj st --ignore-working-copy                       # snapshot skipped entirely, diff still computed
real 0m1.499s          (r18: 8.425s)
$ jj diff --summary -r @
real 0m1.500s          (r18: 7.843s)
$ jj log -r @ --no-graph
real 0m0.015s
$ jj ci -m 'track 20k' && jj st                     # delta committed → no diff
real 0m0.012s
```

So the failure mode is: a big non-ignored, auto-tracked tree lands in `@` as an N-entry delta, and **every** later command pays for diffing it until it is committed (or untracked+ignored); `--ignore-working-copy` does not help, because the cost is the `@` vs `@-` diff, not the snapshot. This is not colocation-specific (F12).

Also observed — what each state costs in syscalls (`strace -f -e openat,newfstatat,getdents64` on a warm `jj st`, 20 000 files in one directory):

| state of the 20 k files | `jj st` | readdir on the dir | `stat` on the files | content opens |
|---|---|---|---|---|
| ignored (`r16`, `.gitignore=gen/`) | 0.011 s | 0 calls (dir pruned unopened) | 0 | 0 |
| untracked, `auto-track="none()"` (`r2`) | 0.017 s | 312 calls × 64 entries | 0 | 0 |
| tracked/auto-tracked, no delta (`r1`) | 0.026 s | — | 20 002 | 0 |

So `none()` skips the per-file `stat` and collapses the directory to `? scratch/`; a *directory* ignore skips even the `readdir`. Neither reads file content. What costs seconds is only the **delta** in `@` (diff), never the walk.

## F9. `snapshot.auto-track` as a fileset is the no-`.gitignore` alternative, with the same cheapness

`r15`: `jj config set --repo snapshot.auto-track '"all() ~ root:generated"'` + 20 000 files in `generated/`:

```
$ jj st
Working copy changes:
A src/b.txt
Untracked paths:
? generated/
real 0m0.017s   (run 2: 0.017s)
```

Same 15–20 ms cost band as `none()` (F8 table). `jj file list` shows only `src/b.txt`, so `generated/` never enters `@`.

## F10. Oversized new files are *warned about*, not fatal; `--include-ignored` overrides

Citation — <https://docs.jj-vcs.dev/v0.45.1/config/#maximum-size-for-new-files>:
> the default is 1MiB … `jj` will refuse to add new files to the snapshot that are larger than a certain size

`r8`, 2 MiB `big.bin`, default config:

```
$ jj st
Warning: Refused to snapshot some files:
  big.bin: 2.0MiB (2097152 bytes); the maximum size allowed is 1.0MiB (1048576 bytes)
Hint: This is to prevent large files from being added by accident. To fix this:
  * Add the file(s) to `.gitignore`
  * Run `jj config set --repo snapshot.max-new-file-size 2097152`
Untracked paths:
? big.bin
$ echo $?
0
$ jj ci -m 'commit small stuff'          # succeeds; creates an EMPTY commit
Working copy (@) now at: kwuxvtsr a9f5dba3 (empty) (no description set)
Parent commit (@-)      : vlwsnqqn 9d65e38b (empty) commit small stuff
$ jj file track --include-ignored big.bin && jj file list -r @
big.bin
```

Two consequences: (a) the warning repeats on every command while the file sits there, (b) `jj commit` can produce an **empty** commit when the only new content was refused — a lane "committed <hash>" report would then cite a hash with no changes.

## F11. Tracking rules the lane helper depends on — all confirmed

`jj file untrack` refuses non-ignored files (`r6`):

```
$ jj file untrack plain.txt
Error: 'plain.txt' is not ignored.
Hint: Files that are not ignored will be added back by the next command.
Make sure they're ignored, then try again.
$ jj st | head -3
Working copy changes:
A .gitignore
A plain.txt        <- still tracked
```

`jj file track` on an ignored path is a **silent no-op** (exit 0) without `--include-ignored` (`r11`):

```
$ jj file track gen/a.txt ; echo $?
0
$ jj st | head -3
Working copy changes:
A .gitignore                     <- gen/a.txt absent
$ jj file track --include-ignored gen/a.txt ; jj st | head -3
Working copy changes:
A .gitignore
A gen/a.txt                      <- tracked despite matching `gen/`
```

`jj file track <dir>` does not pull in ignored children (`r13`, `.gitignore = build/`, `pkg/main.go` + `pkg/build/out.bin`):

```
$ jj file track pkg && jj file list -r @
.gitignore
pkg/main.go
```

`jj commit -- <path>` on an untracked path is a no-op with a warning (`r14`, `auto-track=none()`):

```
$ jj commit -m 'lane work' -- report.md
Warning: The given paths do not match any file: report.md
```

⇒ the helper's ordering (`file track` then `commit -- paths`) is required, not cosmetic.

## F12. Colocation: documented caveat, but not where the snapshot cost lives

Citation — <https://docs.jj-vcs.dev/v0.45.1/config/#default-colocation>:
> Colocation allows some amount of two-way interoperability, but it can perform worse in large repos.

FAQ: *"Jujutsu commands may be a little slower in very large repositories due to importing and exporting changes to Git."*

`r10` — non-colocated `jj git init` with the same 20 000-file tree: `st` first `2.401s`, warm `1.496s`, `diff --summary` `1.500s`, `st --ignore-working-copy` `1.593s` — indistinguishable from colocated `r1`. The doc's colocation penalty is git import/export, not the working-copy scan.

## F13. Scale of the live fleet root (read-only, for context)

```
$ git -C /home/vgpnk/Projects/shokunin ls-files | wc -l
3302
$ du -sh --exclude=.git /home/vgpnk/Projects/shokunin
6.4G
$ git status --porcelain | wc -l
14
$ git check-ignore -v game-dev-3d-shokunin audio-shokunin
.gitignore:1:*-shokunin/	game-dev-3d-shokunin
.gitignore:1:*-shokunin/	audio-shokunin
$ find game-dev-3d-shokunin -type f | wc -l ; find audio-shokunin -type f | wc -l
145606 ; 50687
```

So the fleet root is 3 302 tracked files over a 6.4 G worktree whose bulk (≈250 000 files across just the three biggest `*-shokunin/` dirs) sits behind one directory-level ignore rule — the F7 happy path. It is still the wrong place to put jj (see §3).

---

# 2. Inference ([INFERENCE] — not directly measured)

1. **Watchman's win is skipping the root walk.** In `snapshot()`, if `matcher.visit(root).is_nothing()` jj returns `SnapshotStats::default()` before touching the filesystem; with `fsmonitor.backend=none` the matcher is `EverythingMatcher`, which is never nothing. A healthy watchman reporting "no changes since clock" yields an empty `FilesMatcher` ⇒ early return with zero directory I/O. This is the mechanism behind the docs' "without having to rescan the entire working copy"; I could not run it (see §5).
2. **watchman + `auto-track=none()` do not compose well.** Because every snapshot under `none()` yields untracked paths, `watchman_clock` is never stored (F5), so each snapshot re-queries from the same old clock and the changed-file set monotonically grows. I expect correctness to hold but the incremental benefit to erode; unmeasured.
3. **Lane cost model.** Lane repos are small (the whole fleet repo has 3 302 tracked files; a lane carries a subset of that). With `auto-track="none()"` the per-command snapshot is a handful of `readdir`+`stat`s ⇒ the 10–20 ms band. `watchman` cannot improve on 10 ms meaningfully, and its failure modes (daemon, inotify, silent fallback) are new operational surface.
4. **A single stray big file is enough to poison a lane.** A 900 KB artifact is *under* the 1 MiB cap, so it is auto-tracked rather than refused; 20 000 of them is ~18 GB hashed on the first snapshot and a 20 000-entry diff on every command afterwards, until committed or untracked+ignored.
5. **`register-snapshot-trigger` is wrong for the lanes** even if watchman were installed: it runs `jj util snapshot` out-of-band (CHANGELOG 0.39: *"The Watchman integration has also been updated to use this command instead"*), i.e. an asynchronous writer taking the working-copy lock that jj-lane.sh's `flock` does not coordinate with.

---

# 3. Consequence for the planned shokunin integration

1. **jj-lane.sh already contains the correct large-tree defenses; do not weaken them.** `--config 'snapshot.auto-track="none()"'` at init plus `--ignore-working-copy` on every config read is exactly what keeps a lane at 15–20 ms/command with 40 k generated files present (`r14` evidence: `jj st` 0.016 s, pathspec `jj commit` 0.032 s). If that repo config is ever lost or overridden (`jj --config snapshot.auto-track=all() …`, or a lane whose `.jj` predates the fix), the next command auto-tracks the whole tree into `@` and the lane drops to seconds/command until someone commits or untracks it — the helper's `warn: working-copy commit @ already tracks N added path(s)` check is the right detector; keep it.
2. **Do not enable `fsmonitor.backend = "watchman"` for lanes.** (a) 10–20 ms is already the floor jj can offer; (b) watchman is not installable from any allowed channel here (no Linux asset in the official release, pacman paused — §5); (c) a broken/missing watchman is silent (F3); (d) `auto-track=none()` prevents the clock from advancing (F5); (e) watchman ignores only `.git`/`.jj` (F4) so it would add an inotify watch over every build tree in every lane.
3. **Keep `.gitignore` as belt-and-braces in lane repos** for `node_modules/`, `target/`, `.venv/`, `.next/`, `dist/`, `build/`, `*.log`→`logs/`. Ignore is the only guard that holds *regardless* of `snapshot.auto-track` (*"Ignored files are never tracked automatically (regardless of the value of `snapshot.auto-track`)"*), so it survives a mistaken `--config` override. Prefer **directory** patterns over `*.ext` globs (F7: 34 vs 348 syscalls, and only the directory form is O(1) in tree size).
4. **`.ufo/state/` invariant.** Under `auto-track=none()` nothing is ever auto-committed, so the invariant holds structurally; the risk is only the F8 failure mode (someone runs jj with `all()`). Adding `.ufo/state/` to the ignore set (or relying on the helper's explicit path validation, which already rejects `.ufo/state/*`) is the second layer. Note jj-lane.sh's explicit rejection remains the load-bearing control, because `jj file track --include-ignored` will happily track an ignored path (F11).
5. **`jj file track --include-ignored` bypasses `max-new-file-size` (verified, F10).** The helper relies on this for named files. That is fine by design, but it means the 1 MiB anti-footgun does not protect a lane commit; if a size ceiling matters, the helper would need an explicit `stat` guard (recommendation, not a defect).
6. **Fleet-root commits stay on `fleet-commit.sh` (git).** The fleet root is 6.4 G / 250 k files behind one ignore rule — ignoring works (F7) so jj *could* walk it cheaply, but jj adds an op log, an index, and git import/export on every command for zero benefit, and the protocol (LOG.md append-only under `flock`, `.ufo/state/` never committed, cited-hash-must-be-pushed) is already encoded in the git path. Nothing in this study argues for moving it.
7. **Operational check if watchman is ever turned on:** `jj debug watchman status`; a healthy setup prints the backend and `Background snapshotting is disabled/enabled`, a broken one prints `Could not connect to Watchman` with the exact `os error`. Also `jj --debug <cmd> 2>&1 | grep 'Failed to query filesystem monitor'`.

---

# 4. Recommendations (settings, for repos with big untracked/generated directories)

| Situation | Setting | Why (evidence) |
|---|---|---|
| Any repo with generated output | put it in `.gitignore` as a **directory** (`build/`, `node_modules/`) | prunes the walk entirely: 11 ms + 0 syscalls for 20 k files (F7) |
| Can't edit `.gitignore` (e.g. it is generated) | `snapshot.auto-track = "all() ~ root:<dir>"` | 15–17 ms for 20 k files, dir stays untracked (F9) |
| Seat/agent scratch repos, lanes | `snapshot.auto-track = "none()"` + explicit `jj file track` | 15–20 ms with 40 k untracked files; nothing enters `@` (F8, r14) |
| Large monolithic repo, interactive use, watchman installed | `[fsmonitor] backend = "watchman"` (optionally `register-snapshot-trigger = true`) | docs F1; mechanism [INFERENCE] #1; needs `jj debug watchman status` |
| Watchman present but the repo also has huge build dirs | add a `.watchmanconfig` with `ignore_dirs` — jj does not do it for you (<https://facebook.github.io/watchman/docs/config.html>: `ignore_vcs`/`ignore_dirs`, local scope) | F4 (`// TODO: consider parsing .gitignore`) |
| Large artifacts expected | leave `snapshot.max-new-file-size` at 1 MiB (or lower); fix the ignore | F10 — the warning is not fatal but repeats and can yield empty commits |
| Colocated repos | keep the working tree small; expect git import/export overhead, not snapshot overhead | F12 |
| Don't | set `core.fsmonitor` anywhere and expect jj to use it | F2 |

---

# 5. Open uncertainties (explicit)

1. **No watchman runtime measurement.** There is no `watchman` on this host, and it is not installable through the allowed channels: `pacman` transactions are paused host-wide; `facebook/watchman` release `v2026.10.19.00` exposes **no Linux asset** (the expanded-assets page has no `*-linux*` download); `uv tool`/`npm` ship only clients (`fb-watchman` is a JS client). Therefore: no measured snapshot time with watchman, no verification of the clock-not-advancing behaviour (F5) or of `register-snapshot-trigger`, and no check of the inotify-limit failure mode. All watchman statements above are *docs + source read*, marked [INFERENCE] where behavioural.
2. **`fsmonitor.backend="test"` is not usable as a stand-in**: `Cannot use test fsmonitor in real repository` (source, F2). So the "empty matcher ⇒ skip the whole walk" path could not be demonstrated, only read.
3. **Absolute timings are load-sensitive.** 20 k auto-tracked files measured 1.5 s/command at load ≈2.5 and 7–10 s/command at load ≈9. The 2 k point (77 ms) and the 20 k point (1.5 s) suggest a super-linear component in the status/diff of a large added subtree; I did not isolate whether that is `MergedTree` diff materialisation, copy detection, or allocator pressure, and I am not asserting a cause.
4. **Why the diff is expensive at all** (≈40–390 µs per added entry with zero file reads: `openat` on the added dir = 0) is unexplained by the code I read; `jj st`/`jj diff` compute the `@` vs `@-` delta, and that delta alone is the cost. No profile was taken.
5. **Ignore-rule changes under watchman**: CHANGELOG 0.38 says `.gitignore` changes trigger a subtree rescan so newly unignored files are found (`#8427`); unverified here. Without watchman I confirmed the plain behaviour: a freshly written `.gitignore` takes effect on the next command (F6 evidence, both `r5` and `r11`).
6. **Fileset edge cases**: only `root:gen` was tested in `snapshot.auto-track`. Whether `root-glob:`/negations behave identically for deeply nested generated dirs was not exercised.
7. **`core.excludesFile` precedence** (repo git config vs global git config vs `$XDG_CONFIG_HOME/git/ignore`) was tested only as: repo-level value honored, unset ⇒ XDG file honored. The exact layering when both are set (and when the global git config sets it) follows `git_repo.config_snapshot()` in source but was not tested experimentally.

---

# 6. Tooling record

- No installs, no upgrades. `jj 0.45.1` and `git 2.56.0` were already present.
- Channels attempted for watchman (kept, because they are the only way to close uncertainty #1): `pacman` (paused host-wide by operator instruction — not attempted), official GitHub release assets (no Linux asset for `v2026.10.19.00`), `uv tool`/`npm` (client-only packages). Nothing was left installed.
- Sandbox: `/fast/scratch/jj-wave/JjDocLargeRepo/` (574 MB after trimming). It retains exactly the cited evidence cases — `r18/` (the four-strategy timing matrix incl. the `default` 20 k-file slowdown), `r16/` and `r19/` (the syscall-pruning evidence) — plus the unpacked `0.45.1` source tree used for line-accurate citations (`jj-0.45.1/`). Delete with `rm -rf /fast/scratch/jj-wave/JjDocLargeRepo`.
