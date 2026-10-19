# jj / Git-tool compatibility — docs and fleet census

## Verdict

**safe-with-config**, but not a drop-in Git-manager replacement. Keep all workspaces **colocated** (`jj git init --colocate`, or `git.colocate = true`), set Jujutsu identity explicitly per lane, preserve hook checks outside native jj commands, and make bookmark/current-branch selection explicit for branch-aware tools. **Top hazard:** jj has no active/current branch and commonly leaves colocated Git `HEAD` detached; Git scripts, editors, agents, and `gh pr create` that infer the current branch can fail or target the wrong ref. This finding uses the official v0.45.1 docs matching the installed version stated in the assignment.

## Local evidence (read-only)

**Scope/count command:** the loop below expanded `/home/vgpnk/Projects/shokunin`, each immediate `*-shokunin` directory, and `/home/vgpnk/Projects/kimi-shokunin` (23 repositories total: root + 21 lane repos + protocol repo).

```sh
for r in /home/vgpnk/Projects/shokunin /home/vgpnk/Projects/shokunin/*-shokunin /home/vgpnk/Projects/kimi-shokunin; do
  git -C "$r" config --file .gitmodules -l
  git -C "$r" submodule status
  git -C "$r" ls-files --stage | cut -d' ' -f1 | sort | uniq -c
  git -C "$r" ls-files -co --exclude-standard -- .gitattributes ':(glob)**/.gitattributes'
  git -C "$r" ls-files | git -C "$r" check-attr --stdin filter | cut -d: -f3 | sort | uniq -c
done
```

- For every repository, `.gitmodules` was absent (`test -f "$r/.gitmodules"` false) and the requested `git -C "$r" config --file .gitmodules -l` returned exit 128; `git submodule status` printed no entries. The index-mode census showed no `160000` entries (gitlinks). **No present submodule dependency found.**
- The tracked/non-ignored-untracked `.gitattributes` listing was empty in every repository. The indexed-path `check-attr filter` summary contained only `unspecified` values, with no active filter rules. **No present LFS/filter dependency found.** The `ls-files --exclude-standard` check excludes ignored untracked files; ignored `.gitattributes` files were not separately enumerated.
- No `jj` command was run and no live repository or worktree was mutated.

## Compatibility findings

### Hooks — unsupported by jj

The v0.45.1 [Git compatibility page](https://docs.jj-vcs.dev/v0.45.1/git-compatibility/) → **Supported features** says **Hooks: No**. Do not rely on `.git/hooks` (including pre-commit or pre-push) being invoked by jj commit/push; run required checks through an explicit wrapper/alias or CI. An actual Git CLI command such as `git commit` remains a Git operation and follows Git's hook mechanism. Local `.git/hooks` contents were not inspected.

### Git index and stash — not transparent

The same compatibility page says the staging area is ignored. In v0.45.1 [Git command table](https://docs.jj-vcs.dev/v0.45.1/git-command-table/) and [Git comparison](https://docs.jj-vcs.dev/v0.45.1/git-comparison/) → **The index**, Git's `git add -p; git commit` maps to `jj split`; selectively moving work to a parent maps to `jj squash -i`. The command table maps temporary stash to `jj new @-`; recover the prior working-copy revision with `jj edit <old-revision>`. jj snapshots changed working-copy contents on most commands and implicitly tracks added files ([working-copy Introduction](https://docs.jj-vcs.dev/v0.45.1/working-copy/)). Therefore `git add`, `git diff --cached`, and `git stash` are not an index/staging workflow that jj understands; prefer jj-native operations and avoid interleaving pending Git index mutations with jj snapshots.

**Concrete source dependency:** `kimi-shokunin/scripts/shokunin-watchdog.sh::commit_evidence` (lines 101–106) runs path-limited `git add` followed by `git commit`; `advance` calls it (line 111), and the success paths call `advance` (lines 132 and 138). This runner intentionally uses a Git index/commit operation. It needs an explicit policy if the protocol repo is jj-enabled: keep this path Git-only or adapt/guard it rather than assuming jj hooks or staged-state behavior. `kimi-shokunin/scripts/mint-agent.sh` (lines 74–79) also provisions new lane repositories with `git init`, Git identity, `git add -A`, and `git commit`; it will not create a jj workspace unless provisioning is separately changed. Its `git rev-parse --short HEAD` (line 87) is hash-based, not a current-branch lookup.

### LFS and submodules — unsupported, absent locally

The v0.45.1 [Git compatibility page](https://docs.jj-vcs.dev/v0.45.1/git-compatibility/) → **Supported features** lists `.gitattributes`, submodules, and Git LFS as unsupported. Submodules will not appear in a jj working copy (though the Git data is not lost); Git LFS/attribute filters must not be assumed to smudge, clean, or otherwise behave under jj. The census above found no current repo dependency, so these are latent compatibility limits rather than present blockers. If either is introduced, keep the relevant workflow Git-only until separately qualified.

### GitHub CLI

Colocation keeps a regular `.git` repository visible to Git-aware tools ([Git compatibility → Colocated Jujutsu/Git workspaces](https://docs.jj-vcs.dev/v0.45.1/git-compatibility/)). But jj has bookmarks, not a currently checked-out bookmark ([bookmarks → Introduction and Mapping to Git branches](https://docs.jj-vcs.dev/v0.45.1/bookmarks/)); jj commands commonly leave Git `HEAD` detached. GitHub CLI's [`gh pr create`](https://cli.github.com/manual/gh_pr_create) defaults `--head` to the current branch. In jj use an explicit bookmark/ref and push it first, e.g. `jj bookmark set feature -r @`, `jj git push --bookmark feature`, then `gh pr create --head feature --base main`. `--head` suppresses gh's automatic push/fork prompt, so the jj push is required. Other gh commands that do not need the current branch can still use the colocated Git repo.

### Editors, agents, and shell tools on detached `HEAD`

- **Observed docs:** colocated jj commands usually leave Git `HEAD` detached because jj has no current branch; before mutating Git commands the docs say a `git switch` may be needed ([Git compatibility → Colocated Jujutsu/Git workspaces](https://docs.jj-vcs.dev/v0.45.1/git-compatibility/)). Git `symbolic-ref` documents that detached `HEAD` is not a symbolic ref and returns nonzero (`git-symbolic-ref` **OPTIONS/NOTES**, https://git-scm.com/docs/git-symbolic-ref). Read-only Git tools can still inspect the repository/commit; branch-sensitive operations and UI state cannot infer a checked-out jj bookmark.
- **Inference:** branch probes such as `git symbolic-ref --short HEAD` fail; `git rev-parse --abbrev-ref HEAD` identifies `HEAD`, not the jj bookmark. Editors and agents that assume `git branch --show-current` is populated, or use branch name for task identity, base selection, or branch switching, need an explicit bookmark/name input or a deliberate `git switch <branch>`. Some IDEs auto-fetch in the background; jj's compatibility docs explicitly warn this can create confusing branch/ref conflicts when Git and jj are interleaved.
- Literal search over fleet/protocol `scripts`, `tools`, and `verifiers` (LSP device unavailable: `xd://lsp` was not mounted) found the concrete Git operations above; it did not surface a `git stash`, `git diff --cached`, or explicit current-branch-name consumer. This is grep evidence only, not a semantic proof that no such consumer exists elsewhere.

## Required setup and remaining gaps

```toml
[git]
colocate = true

[user]
name = "<lane>-shokunin"
email = "<lane>@shokunin.local"
```

The Git compatibility page says only a limited subset of Git config is read (remotes and `core.excludesFile`); it does not promise that per-repo Git `user.name`/`user.email` become Jujutsu identity. Set the Jujutsu `[user]` identity explicitly (or supply `JJ_USER`/`JJ_EMAIL`); current `mint-agent.sh` only writes Git identity. Colocation is the default for Git-backed workspaces, but make it explicit for this fleet. There is no native hook setting: enforce required checks through an explicit command/CI path. For current-branch-dependent tools, pass the bookmark explicitly or attach Git `HEAD` with `git switch` only when intentionally using Git mutation.

No scratch runtime test was part of this documentation/source scout; exact behavior of the watchdog's `git add`/`git commit` sequence after jj initialization remains for the isolated scratch probe. The LSP server was unavailable, so source-search negatives are not semantic absence claims. The local submodule/LFS census above is current-worktree evidence, not a guarantee against ignored files or future additions.
