# W2j probe — kimi-shokunin (canonical protocol repo)

Repo: `/home/vgpnk/Projects/kimi-shokunin` — branch `main`, HEAD `bc7d6906`, working tree clean
(`git status --porcelain` → 0 lines). Tracked content ~200K, 29 files; docs + JSON + 3 shell scripts.
Scratch clone: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kimi-shokunin` (deleted after probe; ~640K on disk incl. `.jj/`).
jj version: `jj --version` → `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`.

## 1. Pristine baseline (scratch clone, pre-jj)

The repo's own read-only gate is `install.sh` (file-presence checks, `bash -n` on both scripts,
`kimi.plugin.json` JSON parse). No test suite, no `tools/`/`verifiers/` dir exists.

| gate | command | exit |
|---|---|---|
| install.sh | `./install.sh` | 0 (all four check groups OK) |
| mint-agent syntax | `bash -n scripts/mint-agent.sh` | 0 |
| watchdog syntax | `bash -n scripts/shokunin-watchdog.sh` | 0 |
| manifest JSON | `python3 -c "json.load(open('kimi.plugin.json'))"` | 0 |

Skipped as gates (mutating / daemon): `scripts/mint-agent.sh` (creates a lane dir, `git init`,
commits, appends `shokunin.conf` under a fleet root) and `scripts/shokunin-watchdog.sh`
(infinite loop daemon). Both were inspected statically instead.

## 2. `jj git init --colocate`

```
$ jj git init --colocate        → exit 0
  "Done importing changes from the underlying Git repo.
   Setting the revset alias `trunk()` to `main@origin`."
$ time jj st                    → real 0m0.007s, exit 0
  Working copy (@): mwsqlqzt 1bee9440 (empty) (no description set)
  Parent commit (@-): lxlpovpt bc7d6906 ... main main@origin
$ jj diff --stat -r @           → "0 files changed, 0 insertions(+), 0 deletions(-)"
$ git status                    → "On branch main / nothing to commit, working tree clean"
$ git rev-parse --abbrev-ref HEAD → "main"
```

First `jj st` snapshotted nothing new (empty wc commit on top of `main`); `git status` stayed clean
and HEAD stayed on `main` at init time. A remote-tracking ref `kaika/canon-sync@origin` was also
imported (the live repo carries that remote ref).

## 3. Gates after jj init — identical

`./install.sh` → 0; `bash -n` both scripts → 0; JSON parse → 0. No exit-code change.

Git-assumption grep across the repo: no use of `rev-parse --abbrev-ref`, `symbolic-ref`,
`git status`, `git diff --cached`, `git stash`; `.git/hooks/` contains samples only. Git commands
that DO exist and their jj-colocated risk:

- `scripts/mint-agent.sh:75-87` — `git init`, `git config user.name/email`, `git add -A`,
  `git commit -q`, `git rev-parse --short HEAD`. Runs **inside a fresh lane dir** it creates,
  never inside this repo → unaffected.
- `scripts/shokunin-watchdog.sh:99-106` — `git -C "$SHOKUNIN_ROOT" rev-parse --is-inside-work-tree`,
  `git -c user.name=... commit -- <path>`. `rev-parse` works in a colocated repo; the pathspec
  `git commit` also works **but** it runs against the *fleet root* repo, not this one. Relevant
  only if the fleet root is also colocated — then git commits while HEAD is jj-detached land as
  dangling commits until `git switch`/a branch is moved (`jj` reimports them on next command, so
  data is not lost, but the branch pointer does not advance → commits look orphaned).
  Flagged as the wave's cross-repo interaction, not a defect in this repo.
- Doc-level protocol rules (PROTOCOL.md §Lane identity, `git commit -- pathspec`,
  `git merge-base --is-ancestor`, push to `<lane>-shokunin` remotes): `merge-base`, `push`,
  pathspec commits all work in colocated mode per jj docs — but only while a real branch is
  checked out. `jj` leaves git in detached HEAD after `jj commit` (observed below).

## 4. Lane-identity commit flow

```
$ echo probe > .probe-scratch.txt
$ jj --config user.name='protocol-shokunin' --config user.email='protocol@shokunin.local' \
     commit -m 'test: lane identity probe' .probe-scratch.txt    → exit 0
$ git log -1 --format='%an <%ae> | %cn <%ce>'
  Joao Pedro Veiga <jpveigao10@gmail.com> | protocol-shokunin <protocol@shokunin.local>
```

**Finding:** `jj commit --config user.name/email` sets only the COMMITTER; the author is frozen
into `@` when the wc commit is created (machine default). Corrected flow:

```
$ JJ_USER='protocol-shokunin' JJ_EMAIL='protocol@shokunin.local' jj metaedit --update-author -r @-
$ git log -1 --format='%an <%ae> | %cn <%ce>'
  protocol-shokunin <protocol@shokunin.local> | protocol-shokunin <protocol@shokunin.local>
$ jj bookmark set probe-test -r @-          → "Created 1 bookmarks ..."
$ git branch --list                         → "* (HEAD detached from refs/heads/main)\n  probe-test\n  main"
$ git status                                → "HEAD detached from refs/heads/main / working tree clean"
```

Bookmark export to a git branch works. Git HEAD ends **detached** (jj docs §Colocated
Jujutsu/Git workspaces: "jj commands will usually put the Git repo in a 'detached HEAD' state";
a `git switch` is needed before mutating git commands). Nothing in this repo reads the branch
name, so no gate impact — but any future tool that assumes `HEAD == main` would break.

## 5. Hazards inventory (live checkout)

| check | command | result |
|---|---|---|
| FIFOs/sockets | `find -type p -o -type s` (excluding `.git`) | none |
| symlinks | `find -type l` | none |
| untracked-not-ignored | `git ls-files -o --exclude-standard` | 0 files |
| ignored files present | `git status --porcelain --ignored` | none (gitignore covers only `.DS_Store`, `*.log`, `node_modules/`) |
| untracked >1MiB | n/a (zero untracked files); `jj config get snapshot.max-new-file-size` → `1MiB` | no risk |
| credential-looking names | `git ls-files -o --exclude-standard` + ignored scan | none |
| `.jj/` gitignore coverage | `git check-ignore -v .jj/repo/store/git_target` → `.jj/.gitignore:1:/*` | covered — jj writes `.jj/.gitignore` itself; `.gitignore` needs no change |
| git hooks | `ls .git/hooks` | samples only; jj runs no hooks anyway |
| shallow clone | `git rev-parse --is-shallow-repository` → `true`, `.git/shallow` = 1 entry, 4 commits total, remote `origin` = GitHub | **see below** |

## Verdict: safe-with-config

- **Safe**: zero gates/scripts depend on branch name or index state; `.jj/` self-ignored; no
  special/untracked/large files; first `jj st` 7ms on a 200K repo; bookmark↔branch round-trip works.
- **Required config/knowledge for adoption**:
  1. Lane-identity commits need `JJ_USER`/`JJ_EMAIL` (or `--config`) **plus**
     `jj metaedit --update-author` — plain `jj commit --config …` alone yields
     author = machine default (observed: `Joao Pedro Veiga`, not the lane).
  2. Git-side mutating tools need `git switch <branch>` first — jj leaves HEAD detached.
- **Top hazard**: the repo is a **shallow clone** (`--depth`-style, 4 commits, `.git/shallow`
  present, GitHub remote). jj docs §Git compatibility → "Shallow clones: Kind of … deepening or
  fully unshallowing a repository is currently not yet supported and will cause issues."
  jj imported the truncated history fine (boundary commit `459b02b2` treated as root), so daily
  work is unaffected, but `git fetch --unshallow` inside a jj-colocated repo is untested/broken
  per docs → unshallow *before* colocating, or never.

Sources: commands+outputs above; https://docs.jj-vcs.dev/latest/git-compatibility/ (headings
"Colocated Jujutsu/Git workspaces", "Supported features → Shallow clones", "Format mapping details").
