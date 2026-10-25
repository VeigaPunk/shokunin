# JjDocImmutable — `immutable_heads()`, `builtin_immutable_heads()`, `trunk()`, `--ignore-immutable`, per-command `--config`

Seat: JjDocImmutable-2 · Wave: hyaku/jj-w1 · Target: jj 0.45.x (installed: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, git 2.56.0, Linux x64).

Method: read `jj help` / `jj help -k revsets` / `jj help -k config` from `/fast/scratch/jj-wave/JjDocImmutable/`; versioned docs at tag `v0.45.1`; `cli/src/config/revsets.toml`, `cli/src/commands/git/init.rs`, and `CHANGELOG.md` at the same tag. Every behavioral claim below was reproduced in a throwaway sandbox under `/fast/scratch/jj-wave/JjDocImmutable/s*` (bare remote + `git init` + `jj git init --colocate`); no live lane or fleet-root repo was touched by jj, and no remote outside the sandbox was pushed to. No tool installs/upgrades were needed.

## Answer in one screen

| Question | Answer (0.45.x) |
|---|---|
| `immutable_heads()` | Revset alias naming the **heads** of the protected set. Default value: `builtin_immutable_heads()`. The protected set is `::immutable_heads()` (= `immutable()`). |
| `builtin_immutable_heads()` | `trunk() \| tags() \| untracked_remote_bookmarks() \| untracked_remote_tags()`. Documented as "not recommended to redefine". |
| `trunk()` | Repo-level alias, normally written at `jj git init` from `refs/remotes/<remote>/HEAD`; global fallback is `latest(remote_bookmarks(exact:main/exact:master/exact:trunk on origin/upstream) \| root())`. |
| "Pushed history is immutable" | `[revset-aliases] "immutable_heads()" = "builtin_immutable_heads() \| remote_bookmarks()"`. `remote_bookmarks()` covers remote targets only (local bookmarks and `@git` excluded); `immutable()` closes over ancestors, so all pushed-and-fetched history is protected while descendants stay mutable. |
| Controlled rebase of unpushed commits | Plain `jj rebase -b <unpushed-tip> -d <branch>@origin` works with the config above; no flag needed (destination = remote tip keeps the `-b` set to unpushed commits only). |
| `--ignore-immutable` | Global flag that disables the immutability **check** for that one command. Does not change `immutable_heads()`/`immutable()`/template `immutable`; root stays immutable; allows rewriting pushed commits. |
| Per-command `--config key=value` | Highest-precedence config layer for one invocation. For `revset-aliases` it overrides just that key (map merge) and does not persist. Used to *narrow* immutability, the narrowed set stays enforced for that command. |

## Findings

### F1 — `immutable_heads()` is a frontier; `immutable()` is its ancestry

`jj help -k revsets` (lines 653–658):

```
* `immutable_heads()`: The heads of the set of immutable commits (not "heads
  that are immutable"). Resolves to `trunk() | tags() |
  untracked_remote_bookmarks() | untracked_remote_tags()` by default. It is
  actually defined as `builtin_immutable_heads()`, and can be overridden as
  required. The full set of immutable commits is `::immutable_heads()` (i.e.,
  `immutable()`).
```

Same file, `immutable()`: "This is equivalent to `::(immutable_heads() | root())`." Built-in config confirms the alias chain (`jj config list --include-defaults`):

```
revset-aliases."builtin_immutable_heads()" = '''
trunk() | tags() | untracked_remote_bookmarks() | untracked_remote_tags()
revset-aliases."immutable_heads()" = 'builtin_immutable_heads()'
revset-aliases."immutable()" = '::(immutable_heads() | root())'
```

Docs, https://docs.jj-vcs.dev/v0.45.1/config/#set-of-immutable-commits (canonical target of `https://jj-vcs.github.io/jj/v0.45.1/config/`):

> Ancestors of the configured set are also immutable. The root commit is always immutable even if the set is empty.

Experiment (sandbox `s1`; `master` is the only branch, pushed to sandbox `origin`):

```
$ jj --ignore-working-copy log --no-graph -r 'immutable_heads()' -T 'commit_id.short() ++ " " ++ bookmarks ++ " " ++ description.first_line() ++ "\n"'
a8619659a262 master master@origin base

$ jj --ignore-working-copy log --no-graph -r 'immutable()' -T '...'
a8619659a262 master master@origin base
000000000000
```

So with default config the immutable set is *all ancestors of the pushed trunk tip plus root*, not just the tip.

Citation for root permanence is also in `jj --help` under `--ignore-immutable`: "lets you rewrite any commit but the root commit" (see F7), and practice: `jj describe -r 'root()' -m x --ignore-immutable` → `Error: The root commit 000000000000 is immutable` (sandbox `s12`).

### F2 — `builtin_immutable_heads()` = trunk + tags + *untracked* remote bookmarks/tags

`jj help -k revsets` (lines 648–651):

```
* `builtin_immutable_heads()`: Resolves to `trunk() | tags() |
  untracked_remote_bookmarks() | untracked_remote_tags()`. It is used as the
  default definition for `immutable_heads()` below. It is not recommended to
  redefine this alias. Prefer to redefine `immutable_heads()` instead.
```

Source at tag: https://raw.githubusercontent.com/jj-vcs/jj/v0.45.1/cli/src/config/revsets.toml

```toml
'builtin_immutable_heads()' = '''
trunk() | tags() | untracked_remote_bookmarks() | untracked_remote_tags()
'''
'immutable_heads()' = 'builtin_immutable_heads()'
```

CHANGELOG 0.45.0 (https://github.com/jj-vcs/jj/blob/v0.45.1/CHANGELOG.md):

> The default `immutable_heads()` set now includes `untracked_remote_tags()`.

The word **untracked** is the load-bearing part: `untracked_remote_bookmarks()` is "All targets of untracked remote bookmarks" (`jj help -k revsets`), and `jj help -k revsets` for `remote_bookmarks()` says: "Git-tracking bookmarks are excluded by default." Local bookmarks are not part of the built-in set at all.

### F3 — What `trunk()` resolves to, and when it becomes repo config

`jj help -k revsets` (lines 625–633):

```
* `trunk()`: Resolves to the head commit for the default bookmark of the default
  remote, or the remote named `upstream` or `origin`. This is set at the
  repository level upon initialization of a Jujutsu repository.
```

Global fallback value (`revsets.toml`, v0.45.1):

```toml
'trunk()' = '''
latest(
  remote_bookmarks(exact:"main", exact:"origin") |
  remote_bookmarks(exact:"master", exact:"origin") |
  remote_bookmarks(exact:"trunk", exact:"origin") |
  remote_bookmarks(exact:"main", exact:"upstream") |
  remote_bookmarks(exact:"master", exact:"upstream") |
  remote_bookmarks(exact:"trunk", exact:"upstream") |
  root()
)
'''
```

Init behaviour (`cli/src/commands/git/init.rs`, v0.45.1, `maybe_set_repository_level_trunk_alias`):

```rust
// Set repository level `trunk()` alias to the default branch.
// Checks "upstream" first, then "origin" as fallback.
...
    let ref_name = format!("refs/remotes/{remote}/HEAD");
    if let Some(reference) = git_repo.try_find_reference(&ref_name)...
        write_repo_presets(ui, config_env, RepoPresets { ..., trunk: Some(symbol), })?;
```

Experiment (sandbox `s13`: seed remote with `master` and `topic`, then `git clone` so `origin/HEAD` exists, then `jj git init --colocate`):

```
$ git symbolic-ref refs/remotes/origin/HEAD
refs/remotes/origin/master

$ jj config path --repo
/home/vgpnk/.config/jj/repos/209baa95127783d61f06/config.toml
$ cat "$(jj config path --repo)"
#:schema https://docs.jj-vcs.dev/latest/config-schema.json

[revset-aliases]
"trunk()" = "master@origin"

$ jj log --no-graph -r 'trunk()' -T 'commit_id.short() ++ "  " ++ remote_bookmarks ++ "\n"'
762a39508e7c  master@git master@origin
```

Counter-case (`s6`): a repo created with `git init` + `git remote add origin` + `git push` has no `refs/remotes/origin/HEAD` ref, so `jj git init --colocate` wrote **no** repo config; `trunk()` was resolved purely by the global alias. So the "set at the repository level upon initialization" happens only when a remote `HEAD` ref can be read. This is why shokunin's helper explicitly sets `trunk()` per lane instead of relying on init.

`trunk()` is the alias operators are told to override per repo (config docs example):

```toml
[revset-aliases]
'trunk()' = 'your-bookmark@your-remote'
```

which is exactly what `jj-lane.sh init` already does:
`jj --ignore-working-copy config set --repo 'revset-aliases."trunk()"' "\"${branch}@origin\""`.

### F4 — Default config does **not** mean "all pushed history is immutable"

This is the gap the planned integration has to close.

**Case A — own branch pushed from a repo (`s6`, pristine `JJ_CONFIG=/dev/null`):**

```
$ jj git push --remote origin --bookmark feature
Changes to push to origin:
  bookmark: feature [add to eab4869d8242]

$ jj log --no-graph -r 'untracked_remote_bookmarks()' -T '...'
2994b6459375  master master@origin  base          # feature@origin absent

$ jj log --no-graph -r 'immutable_heads()' -T '...'
2994b6459375  master master@origin  base          # feature@origin absent

$ jj --ignore-working-copy describe -r 'feature@origin' -m hacked
exit=0                                             # pushed commit rewritten
```

Reason: `jj git push --bookmark <name>` auto-tracks the new remote bookmark (CHANGELOG 0.38.0: "`jj git push --bookmark <name>` will now automatically track the bookmark if it isn't tracked with any remote already."). The next `jj bookmark track feature@origin` therefore says:

```
Warning: Remote bookmark already tracked: feature@origin
Nothing changed.
```

**Case B — someone else's branch, fetched (`s13b`):**

```
$ jj log --no-graph -r 'immutable_heads()' -T 'commit_id.short() ++ "  " ++ remote_bookmarks ++ "  " ++ description.first_line() ++ "\n"'
a70ee0914ba3  master@git master@origin  M
5cf79a4ddcfb  topic@origin  T

$ jj --ignore-working-copy describe -r 'topic@origin' -m x
Error: Commit 5cf79a4ddcfb is immutable        # exit=1

$ jj bookmark track topic@origin
Started tracking 1 remote bookmarks.

$ jj log --no-graph -r 'immutable_heads()' -T '...'
a70ee0914ba3  master@git master@origin  M      # topic@origin gone

$ jj --ignore-working-copy describe -r 'topic@origin' -m y
exit=0                                             # now mutable
```

So the default set protects *untracked* remote branches (other people's work you haven't claimed) and `trunk()`, but **tracking a branch removes it from the immutable set**. A lane that tracks `branch@origin` (the helper does) is protected only because `trunk()` was repointed at `branch@origin` — not because "pushed" means immutable.

### F5 — Planned config: pushed history immutable, unpushed descendants mutable

Config (repo level, verified accepted by `jj config set --repo` in `s3`):

```toml
[revset-aliases]
"immutable_heads()" = "builtin_immutable_heads() | remote_bookmarks()"
```

This is the documented extension pattern (docs, v0.45.1, same section):

```toml
[revset-aliases]
"immutable_heads()" = "builtin_immutable_heads() | release@origin"
```

Experiment (`s9`, pushed feature branch on top of `master`, `feature@origin` tracked):

```
$ jj log --no-graph -r 'immutable_heads()' -T 'commit_id.short() ++ "  " ++ bookmarks ++ "  " ++ description.first_line() ++ "\n"'
d4c700676074  feature  F
32ef884daf4c  master  base

$ jj --ignore-working-copy describe -r 'feature@origin' -m nope
Error: Commit d4c700676074 is immutable
Hint: Could not modify commit: kpuzruvm d4c70067 feature | F
Hint: Immutable commits are used to protect shared history.
exit=1
```

`s7` confirms the same set (`immutable_heads()` = `{feature, master}`) and refuses `jj rebase -b @ -d dest`, which would include the pushed `F`, with exit 1. Local bookmarks are untouched by `remote_bookmarks()`: `jj bookmark set feature -r @` succeeds (`s4`, `s5`), so the lane can advance its bookmark onto each new commit.

### F6 — Controlled rebase of unpushed commits needs no escape hatch

Replication of `jj-lane.sh do_push`'s recovery path (`s4`): `F` pushed as `feature`; `U` created on top and bookmarked; a second clone pushes `W` on `feature`; local `jj git fetch` moves `feature@origin` to `W`.

```
$ jj --ignore-working-copy log --no-graph -r 'heads(feature@origin..bookmarks(feature))' -T 'change_id.short() ++ "  " ++ commit_id.short() ++ "\n"'
kzxtmtstlwxm  b798754cbde1
TIP=kzxtmtstlwxm

$ jj rebase -b "$TIP" -d 'feature@origin'
Rebased 1 commits to destination.
Working copy  (@) now at: kzxtmtst c2d7044d feature* | U
Parent commit (@-)      : tkumwyoo 74d37c6d feature@origin | W
Added 1 files, modified 0 files, removed 0 files
exit=0

$ jj log --no-graph -r 'all()' -T '...'
c2d7044dd4bd  feature*  U
74d37c6dd45a  feature@origin  W
25f37ac40809    F
0207dac06e26  master  base

$ jj --ignore-working-copy bookmark set feature -r "$TIP"   # exit 0
$ jj git push --remote origin --bookmark feature
Changes to push to origin:
  bookmark: feature [move forward from 74d37c6dd45a to c2d7044dd4bd]
push_exit=0
```

Only `U` was rewritten; `F` and `W` (pushed) are byte-identical before/after. Before the rebase, `jj git push` correctly refuses because the local bookmark is conflicted after the fetch:

```
$ jj git push --remote origin --bookmark feature
Error: Bookmark feature is conflicted
Hint: Run `jj bookmark list` to inspect, and use `jj bookmark set` to fix it up.
exit=1
```

Why no immutability trip: `-b` is destination-relative. `jj rebase --help`:

```
With `--branch/-b`, the command rebases the whole "branch" containing the
specified revision. A "branch" is the set of revisions that includes:
* the specified revision and ancestors that are not also ancestors of the destination
* all descendants of those revisions
In other words, `jj rebase -b X -o Y` rebases revisions in the revset `(Y..X)::`
```

With `Y = branch@origin`, the set is exactly `branch@origin..tip` plus descendants, i.e. unpushed commits. Pushed ancestors are in the destination's ancestry and are excluded before the immutable check runs. `--ignore-immutable` is not needed for this path.

### F7 — What `--ignore-immutable` actually does

`jj --help` (Global Options, lines 99–106):

```
      --ignore-immutable
          Allow rewriting immutable commits

          By default, Jujutsu prevents rewriting commits in the configured set of immutable commits.
          This option disables that check and lets you rewrite any commit but the root commit.

          This option only affects the check. It does not affect the `immutable_heads()` revset or
          the `immutable` template keyword.
```

Docs warning (v0.45.1 config page):

> Using `--ignore-immutable` will allow you to rewrite any commit in the history, and all descendants, without warning.

Experiments:

```
# s1: blocked without flag, accepted with flag (flag accepted both before and after the subcommand)
$ jj describe -r 'master@origin' -m hack
Error: Commit a8619659a262 is immutable
Hint: ... This operation would rewrite 1 immutable commits.
exit=1

$ jj describe --ignore-immutable -r 'master@origin' -m hack2
Rebased 1 descendant commits.
exit=0

# s12: root is still protected
$ jj describe -r 'root()' -m rootmutation --ignore-immutable
Error: The root commit 000000000000 is immutable
exit=1
```

The dangerous shape, measured (`s7`): destination `dest` (a mutable commit on `master`) is *not* an ancestor of the pushed `F`, so the `-b` set is `master..@ = {F, U}`:

```
$ jj rebase -b @ -d dest
Error: Commit a733589d0cf1 is immutable
Hint: This operation would rewrite 1 immutable commits.
exit=1

$ jj rebase -b @ -d dest --ignore-immutable
Rebased 2 commits to destination.
Working copy  (@) now at: onzppvvv de932dbd U
Parent commit (@-)      : yktmkksw fd97c85f feature* | F
exit=0

$ jj log --no-graph -r 'all()' -T '...'
de932dbdae9c    U
fd97c85fe322  feature*  F        # F has a NEW commit id
f0fa6de2c28e  dest  D
32ef884daf4c  master  base

$ git for-each-ref ...
dest f0fa6de
feature fd97c85
master 32ef884
origin/feature a733589          # remote still points at the old, published F
origin/master 32ef884
```

Also measured: `jj abandon -r master@origin` and `jj squash --into master@origin` are blocked with the same error and exit 1 (`s12`); `--ignore-immutable` on root is refused (`s12`).

### F8 — What a per-command `--config` override actually does

`jj help -k config`, "Specifying config on the command-line":

```
You can use one or more `--config`/`--config-file` options on the command line
to specify additional configuration settings. This overrides settings defined in
config files or environment variables.
```

`jj --help` (lines 150–155): "The name should be specified as TOML dotted keys. The value should be specified as a TOML expression." It is a full config **layer above** user/repo/workspace config, for that invocation only.

Experiments (`s3`; repo config = `builtin_immutable_heads() | remote_bookmarks()`, plus an extra alias `lanealias()`):

```
$ jj --ignore-working-copy config get 'revset-aliases."immutable_heads()"'
builtin_immutable_heads() | remote_bookmarks()

$ jj --config 'revset-aliases."immutable_heads()"=builtin_immutable_heads()' \
     --ignore-working-copy log --no-graph -r 'immutable_heads()' -T '...'
caf1e5c72b98  master  base          # feature@origin excluded: override won

$ jj --config 'revset-aliases."immutable_heads()"=builtin_immutable_heads()' \
     --ignore-working-copy log --no-graph -r 'lanealias()' -T '...'
774c63d1bd03  feature  F            # other keys in the map survive (merge per key)

$ jj --config 'revset-aliases."immutable_heads()"=builtin_immutable_heads()' \
     --ignore-working-copy describe -r 'feature@origin' -m allowed
Rebased 1 descendant commits.
exit=0

$ jj --ignore-working-copy describe -r 'feature@origin' -m again
Error: Commit 774c63d1bd03 is immutable          # override did not persist
exit=1

$ jj --ignore-working-copy log -r 'immutable_heads()' --config 'revset-aliases."immutable_heads()"=builtin_immutable_heads()' ...
# also accepted after the subcommand
```

Persistence check (`s10a`): after several per-command overrides, `jj config path --repo` file still reads

```toml
[revset-aliases]
"immutable_heads()" = "builtin_immutable_heads() | remote_bookmarks() | bookmarks()"
"trunk()" = "master@origin"
```

Both quoting forms work for revset values (`s3`, `s10a`): `--config 'revset-aliases."immutable_heads()"=builtin_immutable_heads()'` and `--config 'revset-aliases."immutable_heads()"="builtin_immutable_heads() | remote_bookmarks()"'`.

**Crucial difference from `--ignore-immutable`** (`s10b`, repo alias includes `bookmarks()`):

```
$ jj --config 'revset-aliases."immutable_heads()"="builtin_immutable_heads() | remote_bookmarks()"' \
     rebase -s 'feature@origin' -d dest
Error: Commit 0465c6abaa19 is immutable
exit=1                                       # narrowed set is still ENFORCED

$ jj rebase -s 'feature@origin' -d dest --ignore-immutable
Rebased 1 commits to destination.
exit=0                                       # flag disables the check wholesale
```

So `--config` changes *which* commits are protected for that command (and the new set is enforced); `--ignore-immutable` removes enforcement for the command. For a lane whose config over-blocks an intended rebase, the config override is the strictly narrower tool.

### F9 — Which operations the immutability check does and does not block

Measured in sandboxes `s4`, `s5`, `s8`, `s12` with the planned config:

- `jj bookmark set feature -r @` (moving a bookmark off an immutable target) → exit 0, allowed.
- `jj bookmark set feature -r <unpushed tip>` + `jj git push --bookmark feature` → exit 0, allowed. If the push makes `@` itself immutable, jj self-heals: `Warning: The working-copy commit became immutable; a new commit has been created on top of it.` (`s4.9`), exit 0.
- `jj commit -m X -- path` with `@` a mutable child of an immutable commit → exit 0, pathspec honored (`jj diff --summary -r @-` → `A x.txt`) (`s8`).
- `jj abandon` / `jj squash --into` / `jj describe` / `jj rebase -s|-b` targeting an immutable commit → exit 1 (`s12`, `s7`, `s3`).
- `jj git push` is unaffected (it does not rewrite commits; pushes succeed in `s4.9`). [INFERENCE] `--ignore-immutable` does not disable jj's own push safety checks (conflicted tree, empty description); not tested in this seat. The helper's conflicted-tree guard is a separate revset check and is unaffected either way.

### F10 — Durability limit: "pushed" means "reachable from a fetched remote ref"

`s9`: delete the remote branch, then fetch; the previously pushed commit becomes mutable again:

```
$ jj bookmark delete feature
Deleted 1 bookmarks.
$ jj git push --remote origin --deleted
Changes to push to origin:
  bookmark: feature [delete from d4c700676074]
$ jj git fetch --remote origin

$ jj log --no-graph -r 'remote_bookmarks()' -T '...'
32ef884daf4c  master  base                    # feature@origin gone

$ jj --ignore-working-copy log --no-graph -r 'immutable_heads()' -T '...'
32ef884daf4c  master  base

$ jj --ignore-working-copy describe -r d4c700676074 -m revived
Rebased 1 descendant commits.
exit=0                                          # former pushed tip is mutable
```

`remote_bookmarks()` is evaluated against the local remote-tracking view, so protection is exactly "ancestors of fetched remote tips". A remote force-push/rewrite moves commits out of that set; a fetch that prunes a deleted branch releases its commits. That is also why the invariant "a cited hash is never rewritten" must be enforced by *push policy* (no force pushes, rebase only the unpushed range), not by immutability alone.

### F11 — Repo config lives outside the repo; every lane/clone must be initialised

`jj config path --repo` in every sandbox printed `/home/vgpnk/.config/jj/repos/<hash>/config.toml` (`s4`: `.../169cce44b9bfbb329a6e/config.toml`). The `immutable_heads()`/`trunk()` settings are not inside `.git`/`.jj` and are not committed, so a re-cloned lane repo (and every new lane) needs `jj-lane.sh init` to set them again.

## Consequences for the planned shokunin integration

1. **Add the immutable_heads key in `jj-lane.sh init`.** Currently `cmd_init` sets `snapshot.auto-track`, `user.name`, `user.email`, `trunk()`, and `bookmark track`, and deliberately leaves an existing `immutable_heads()` untouched. The planned invariant needs it set explicitly, e.g.:
   ```sh
   "$JJ_BIN" --ignore-working-copy config set --repo \
     'revset-aliases."immutable_heads()"' '"builtin_immutable_heads() | remote_bookmarks()"'
   ```
   This is the same `config set --repo` mechanism already proven for `trunk()` (`s3.1`, `s13b.2`); the exact quoted-value form above was verified in `s14.1` (`config get` → `builtin_immutable_heads() | remote_bookmarks()`, and the repo config file shows the quoted value). Keeping `trunk() = <branch>@origin` is still worthwhile: it protects the lane branch even in a repo where a hand-edited `immutable_heads()` was reset, and it makes `builtin_log()`/`trunk()` behave for lane users.
2. **Drop `--ignore-immutable` from `do_push`'s retry rebase.** With destination `<branch>@origin`, `jj rebase -b "$tip" -d "${BRANCH}@origin"` rewrites only `branch@origin..tip`; `s4.7` shows it succeeds with the pushed tip immutable and `s4.8` shows pushed commits unchanged. Removing the flag makes jj enforce the "pushed commits are never amended" invariant instead of trusting the revset.
3. **If a lane carries a legacy `bookmarks()` (or similar) alias, do not widen to `--ignore-immutable`.** It blocks the retry because the local branch bookmark sits on the tip being rebased (`s10a.1` shows `U` in `immutable_heads()`; `s10a.4` shows `rebase -b` blocked). Replace the flag with the per-command narrowing:
   ```sh
   "$JJ_BIN" --config 'revset-aliases."immutable_heads()"="builtin_immutable_heads() | remote_bookmarks()"' \
     rebase -b "$tip" -d "${BRANCH}@origin"
   ```
   Measured: retry then succeeds (`s10a.5`, exit 0) while rewriting a pushed commit is still refused (`s10a.7`, exit 1). This is strictly narrower than `--ignore-immutable` (`s10b.1` vs `s10b.2`).
4. **Never use `bookmarks()` in a lane's `immutable_heads()`.** The lane's own bookmark points at the commit it just created, so every new commit would be immutable and the retry rebase would be blocked (`s10a.4`). `remote_bookmarks()` is the correct selector: remote targets only, `@git` excluded by default (`jj help -k revsets`), local bookmarks untouched.
5. **Keep the retry destination at `<branch>@origin`.** `-b` is destination-relative (`(dest..tip)::`); with a destination that does not contain the pushed tip (e.g. trunk), the set silently includes pushed commits — loud failure without the flag (`s7.2`), silent rewrite with it (`s7.3`/`s7.4`). If a rebase onto trunk is ever needed, select the unpushed commits explicitly with `-r`/`-s` and do not pass `--ignore-immutable`.
6. **Do not rely on default config for "pushed is immutable".** Default only covers `trunk()`, tags, and *untracked* remote bookmarks/tags. Pushing a bookmark auto-tracks it (CHANGELOG 0.38 quote; `s6`), and explicitly tracking a branch removes it from the default immutable set (`s13b`). Any lane branch that is not the `trunk()` target is mutable by default.
7. **Understand what the flag does not buy.** `--ignore-immutable` is per-command, root-exempt, and does not change revsets/templates (`jj --help`); it also does not replace the helper's conflicted-tree guard or the no-force-push policy. The durability caveat (F10) means immutability cannot substitute for never force-pushing and never rebasing outside the unpushed range.
8. **Operational notes.** `jj config set --repo` writes `~/.config/jj/repos/<hash>/config.toml` (outside the repo, not committed); a lane clone must be re-initialised. `bookmark set`, `jj commit -- <paths>`, and `jj git push` are unaffected by immutability (`s4`, `s5`, `s8`). If a push makes `@` immutable, jj creates a new empty `@` and warns — benign for the helper, which commits first so `@` is empty at push time.

## Open uncertainties

- **jj 0.46.0 not tested.** Installed binary is 0.45.1. The 0.46.0 CHANGELOG section contains no `immutable`-related entries, so I expect identical behaviour, but that is inference, not measurement.
- **`remote_bookmarks()` vs `@git` isolation.** `jj help -k revsets` states git-tracking bookmarks are excluded by default, and the built-in alias relies on that; my sandboxes could not construct a commit that exists *only* as `@git` (template output showed `@git` and `@origin` on the same commits), so the exclusion is doc-backed only.
- **Stale/rewritten remote state.** F10 covers deletion+fetch. I did not test a true remote force-push/rewrite followed by fetch, nor `jj git push` behaviour when the remote rewrote history. Expect: previously pushed commits leave the immutable set, and push refuses without force — unverified.
- **Multi-head lane branches.** The helper takes `head -1` of `heads(branch@origin..bookmarks(branch))`; if the unpushed range has multiple heads, only one branch is rebased per attempt. Not tested; outside this seat's question but relevant to the retry loop.
- **Concurrency.** The helper's `flock` serialises helper invocations; jj has its own repo lock, but I did not test concurrent jj writers plus the helper in one repo. Another seat owns that.
- **Per-command `--config` + `--ignore-immutable` combined** was not tested together; each was tested independently.
- **Long-lived lanes and remote tracking changes.** `jj git fetch` after a remote bookmark moves backward is untested; F10's deletion case is the measured proxy.

## Reproduction (load-bearing experiments)

Setup used everywhere (`/fast/scratch/jj-wave/JjDocImmutable/setup.sh`): `git init --bare <remote>`, `git init` + one commit + `git push -u origin master` in `<repo>`, `jj git init --colocate .`, `jj bookmark track master@origin`.

1. **Default immutability** (`s1`, `s13b`): `jj log -r 'immutable_heads()'`, `jj log -r 'immutable()'`, `jj describe -r 'master@origin' -m x`.
2. **Default gap** (`s13b`, `s6`): push/fetch a second branch, check `untracked_remote_bookmarks()`, `bookmark track` it, then `jj describe -r 'topic@origin'`.
3. **Planned config** (`s3`, `s9`): `jj config set --repo 'revset-aliases."immutable_heads()"' 'builtin_immutable_heads() | remote_bookmarks()'`, then `describe` a pushed commit and a pushed-commit `rebase -s`.
4. **Controlled retry** (`s4`): push `F`, add unpushed `U`, second clone pushes `W`, `jj git fetch`, `jj rebase -b <U-change> -d feature@origin`, `jj bookmark set`, `jj git push`.
5. **`--ignore-immutable` danger** (`s7`): `jj rebase -b @ -d dest` (blocked) vs `... --ignore-immutable` (rewrites published `F`; `origin/feature` unchanged).
6. **`--config` vs `--ignore-immutable`** (`s3`, `s10a`, `s10b`): override `immutable_heads()` per command; verify revision-set narrowing, map merge, no persistence, and that the narrowed set still blocks rewriting pushed commits.
7. **Root/edge commands** (`s12`): `jj abandon -r master@origin`, `jj squash --into master@origin`, `jj describe -r 'root()' --ignore-immutable`.
8. **Durability** (`s9`): `jj bookmark delete`, `jj git push --deleted`, `jj git fetch`, then `describe` the formerly pushed commit.

No tool installs or upgrades were performed for this seat. All sandboxes were under `/fast/scratch/jj-wave/JjDocImmutable/` and were removed after the outputs above were captured.
