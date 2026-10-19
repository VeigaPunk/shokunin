# Jujutsu fleet configuration findings (v0.45.1 docs)

**Evidence scope:** checked the official `v0.45.1` source documentation, matching the fleet context's installed jj version. This is configuration guidance only; no jj commands were run and this is not a per-repository probe or an adoption certification.

## Recommended baseline

Use repo-level config for lane identity and the conservative snapshot policy:

```sh
jj config set --repo user.name "<id>-shokunin"
jj config set --repo user.email "<id>@shokunin.local"
jj config set --repo snapshot.auto-track '"none()"'
# Optional explicit reminder; 1MiB is already the documented default.
jj config set --repo snapshot.max-new-file-size '"1MiB"'
```

`jj config set` accepts a TOML expression as its value; therefore the inner double quotes make `none()` a TOML string, while the outer single quotes preserve that argument for a POSIX shell. The repo config overrides user config, but is stored outside the repo/workspace for security, so this is local configuration rather than a committed fleet policy. [`config.md`, “Config files and TOML”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/config.md#config-files-and-toml); [`cli/tests/cli-reference@.md.snap`, “jj config set”](https://github.com/jj-vcs/jj/blob/v0.45.1/cli/tests/cli-reference%40.md.snap#jj-config-set)

`none()` is the fileset function matching nothing. With `snapshot.auto-track = "none()"`, jj does not automatically track newly added, non-ignored files; files can still be explicitly added with `jj file track`. Already tracked files remain tracked. [`filesets.md`, “Functions”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/filesets.md#functions); [`working-copy.md`, “Introduction” and “Ignored files”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/working-copy.md#introduction)

## Large untracked trees: protection and limits

- **Add ignore patterns before the first snapshot** for any large or sensitive local tree. jj supports `.gitignore` files in the working-copy tree, `$GIT_DIR/info/exclude`, and `$XDG_CONFIG_HOME/git/ignore`; Git `core.excludesFile` is also respected. In a colocated repo the Git-local exclude is `.git/info/exclude`. Ignored files are never automatically tracked, regardless of `snapshot.auto-track`; already-tracked files stay tracked until `jj file untrack`. [`working-copy.md`, “Ignored files”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/working-copy.md#ignored-files); [`git-compatibility.md`, “Supported features”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/git-compatibility.md#supported-features)
- **The documented per-file guard is `snapshot.max-new-file-size` (default `1MiB`)**. It refuses to add *new* files above the configured size; files already present in the working copy are explicitly not subject to that limit. Setting it to zero disables the limit. Consequently, it is not protection for a pre-existing large untracked tree; ignore that tree before jj first snapshots it. [`config.md`, “Maximum size for new files”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/config.md#maximum-size-for-new-files)
- **Performance option:** `[fsmonitor] backend = "watchman"` lets jj snapshot without rescanning the entire working copy, and requires Watchman. The docs warn Watchman uses a per-file inotify watch and can fail or make `jj status` slower on large repos when watch limits are reached. This is a scan-performance aid, not an exclusion or tracking-safety rule. [`config.md`, “Filesystem monitor”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/config.md#filesystem-monitor)
- **Bootstrap caution:** the v0.45.1 CLI docs say commands snapshot the working copy by default; `--config` is a command-line override parsed as TOML. Thus a persisted repo setting cannot protect a snapshot taken before that setting exists. Put ignores in place before initialization/first snapshot; if needed, use a one-command override such as `jj --config 'snapshot.auto-track="none()"' …`, then persist the repo setting. This conclusion follows from the documented snapshot default and config precedence. [`cli/tests/cli-reference@.md.snap`, “jj” global options](https://github.com/jj-vcs/jj/blob/v0.45.1/cli/tests/cli-reference%40.md.snap#jj); [`config.md`, “Specifying config on the command-line”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/config.md#specifying-config-on-the-command-line)

**Conclusion on the question:** there is no documented single “safe colocation with large untracked trees” switch. `none()` limits implicit tracking, the size cap limits eligible new files, ignore rules prevent automatic tracking of ignored paths, and Watchman can reduce rescanning. **[Inference]** None of these should be treated as a substitute for ignoring a pre-existing large tree before the first snapshot; the size cap expressly excludes files already present, and Watchman is not a content-exclusion setting.

## Other requested settings

### Immutable heads

The configured set is `revset-aliases."immutable_heads()"`. The documented default is `builtin_immutable_heads()`, defined as `trunk() | tags() | untracked_remote_bookmarks() | untracked_remote_tags()`. If adding a repo-specific protected bookmark, extend rather than replace the built-in set:

```toml
[revset-aliases]
"immutable_heads()" = "builtin_immutable_heads() | stable@origin"
```

Ancestors of configured heads are immutable too; the root is always immutable. The CLI `--ignore-immutable` can bypass the rewrite check, so immutability is a guardrail, not an unbreakable policy. [`config.md`, “Set of immutable commits”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/config.md#set-of-immutable-commits); [`cli/tests/cli-reference@.md.snap`, “jj” global options](https://github.com/jj-vcs/jj/blob/v0.45.1/cli/tests/cli-reference%40.md.snap#jj)

### Conflict marker style

Available setting: `[ui] conflict-marker-style = "diff" | "snapshot" | "git"`. Use `diff` for jj's snapshot-plus-diffs representation; use `snapshot` to show each side and base; use `git` only when tools require Git diff3 markers. Git style only supports two-sided conflicts and falls back to snapshot markers for more than two sides. [`config.md`, “Conflict marker style”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/config.md#conflict-marker-style); [`conflicts.md`, “Alternative conflict marker styles”](https://github.com/jj-vcs/jj/blob/v0.45.1/docs/conflicts.md#alternative-conflict-marker-styles)

## Decision and remaining gap

**Docs-only verdict: `safe-with-config`.** Required local safeguards for a candidate colocated repo are pre-existing ignore coverage for bulky/private trees and repo-specific lane identity; `snapshot.auto-track = "none()"` is a useful fleet-wide defense when explicit tracking is acceptable. Keep the documented size cap unless a measured workflow needs a different value. Largest hazard: a first jj snapshot may discover existing unignored files, and the new-file size limit does not cover files already in the working copy. Actual per-repo untracked inventories, first-snapshot behavior, and filesystem-monitor performance remain to be established by the separate scratch-clone probes.
