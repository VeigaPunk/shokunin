# W2j jj probe — tabi-shokunin

**Verdict: safe-with-config.** Required config: `jj config set --repo user.name 'tabi-shokunin'` + `user.email 'tabi@shokunin.local'` **before** the first `jj st` (the working-copy commit's author is frozen at first snapshot; `--config` on `jj commit` only sets the committer). Top hazard: after `jj commit`, git HEAD is left **detached** and the `master` bookmark stays behind at the old commit — tools that read `git rev-parse --abbrev-ref HEAD` will see `HEAD`, not `master`, unless a `jj bookmark set master -r @-` + `git switch master` follows every commit.

- jj: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`
- Live repo: `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`, HEAD `40a6de87f72b78d90ea627ad89717e55f219001e`
- Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/tabi-shokunin`, `du -sh` = **32M**, 2,717 tracked files. Deleted after probe (`rm -rf`, verified gone).

## 1. Live-repo pre-facts (read-only)

- `git status --porcelain` → empty (clean).
- `git ls-files --others --exclude-standard` → **0 files**: nothing untracked-but-not-ignored; a colocated first `jj st` snapshots nothing new.
- Ignored: `!! .ufo/interactive-sessions/` (3.0M total; two >1 MiB JSONL transcripts, `ls -l`: 1,796,736 B and 1,323,500 B). `.gitignore` contains only `.ufo/interactive-sessions/` — exactly covers the big files, so `snapshot.max-new-file-size` never trips on real content.
- Special files: `find . -path ./.git -prune -o \( -type p -o -type s \) -print` → **none** (no FIFOs/sockets).
- Credential-looking names (glob for `*.pem`, `*.key`, `.env*`, `*credential*`, `*secret*`, `*token*`, `id_*`, keystores) → **none**.
- Hooks: `.git/hooks/` has only `*.sample`; `core.hooksPath` unset.
- Tracked non-100644 entries: only `100755` exec bits on evidence shell/py scripts — standard, no symlinks/gitlinks (`1200`/`1600`) in `git ls-files -s`.

## 2. Pristine baseline gates (scratch, before jj)

Gate registry (SKILL.md:1559) names `check-freshness.mjs`; the two contract checkers run their built-in fixture self-tests. `TMPDIR` was pinned inside the scratch (`$PWD/.jj-probe-tmp`) because self-tests create/delete their own fixture repos under `mkdtemp`. The `--worktree` mode *reads* three absolute allowlist files under `~/.kimi-code/plugins/managed/kimi-webbridge/` (read-only → allowed).

| Gate (command) | Baseline exit | Under jj exit | Under jj, detached HEAD exit |
|---|---|---|---|
| `node scripts/check-freshness.mjs --self-test` | 0 (`verdict=clean cases=12`) | 0 (identical) | 0 |
| `node scripts/check-freshness.mjs --worktree` | 0 (`matched=34 unique=34`) | 0 (identical) | 0 |
| `node scripts/check-round-contract.mjs --self-test` | 0 (`cases=4`) | 0 | 0 |
| `node scripts/check-user-round-contract.mjs --self-test` | 0 (`cases=4`) | 0 | 0 |

No exit-code change anywhere. All git calls in the scripts are object-level reads (`show`, `ls-tree`, `rev-parse --verify`, `merge-base --is-ancestor`, `diff` between commits, `grep <rev>`) — none touch the index, the branch name, or the working tree (`grep` for `rev-parse --abbrev-ref|symbolic-ref|git status|git diff --cached|git add|git stash` in `scripts/*.mjs` → no hits). This is why the repo is jj-compatible even in detached-HEAD state.

## 3. jj adoption (`jj git init --colocate`)

```
$ jj git init --colocate
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `master@origin`.
Initialized repo in "."        EXIT=0
```

- First `jj st`: **0.012s** (`time jj st`). Snapshot: `jj diff --stat -r @` → `0 files changed`; `@` = new empty working-copy commit on `40a6de87`; `master` stayed at `40a6de87`.
- `git status --porcelain` after init: clean. `git rev-parse --abbrev-ref HEAD` → **`master`** (still attached while `@` is an empty child of `master`).
- `.jj/` ignore coverage: needs **no** `.gitignore` edit — `jj` writes `.jj/.gitignore` containing `/*`; `git check-ignore -v .jj/repo/store` → `.jj/.gitignore:1:/*  .jj/repo/store`; `git status --ignored` shows `!! .jj/`.

## 4. Lane-identity commit flow

```
$ jj --config 'user.name=tabi-shokunin' --config 'user.email=tabi@shokunin.local' commit -m 'probe: lane identity commit' .jj-probe/lane-identity.txt
Working copy  (@) now at: qtwnrtrv 5d957a05 (empty) (no description set)
Parent commit (@-)      : knzknvzx bd40ff8c probe: lane identity commit
$ git log -1 --format='%an <%ae> | %cn <%ce>'
Joao Pedro Veiga <jpveigao10@gmail.com> | tabi-shokunin <tabi@shokunin.local>
```

**Author ≠ requested identity**: `jj commit`'s `--config` sets only the committer; the author is copied from the working-copy commit created at first snapshot, which used a pre-existing global `~/.config/git/config` identity (`Joao Pedro Veiga <jpveigao10@gmail.com>` — `git config --global`/`user` reads `ci`/`ci@local`, so the global user file was already populated). Fix that worked:

```
$ JJ_USER='tabi-shokunin' JJ_EMAIL='tabi@shokunin.local' jj metaedit @- --update-author   # → author fixed to tabi-shokunin <tabi@shokunin.local>
$ jj config set --repo user.name 'tabi-shokunin' && jj config set --repo user.email 'tabi@shokunin.local'
$ jj commit -m 'probe: second commit' .jj-probe/lane-identity.txt
$ git log -1 --format='%an <%ae> | %cn <%ce>'
tabi-shokunin <tabi@shokunin.local> | tabi-shokunin <tabi@shokunin.local>   # author correct from the start once repo config is set before the snapshot
```

jj 0.45.1 `describe` has **no** `--reset-author`/`--author` flag (`jj describe --help` → "unexpected argument '--reset-author'"); `jj metaedit --update-author` is the rewrite path.

Bookmark/HEAD behavior:

```
$ jj bookmark set master -r @-   → Moved 1 bookmarks to knzknvzx 74b502d5 master*
$ git branch --list -vv          → master 74b502d [origin/master: ahead 1]
$ git rev-parse --abbrev-ref HEAD → HEAD        # detached at the @ working-copy commit
$ git status -sb                 → ## HEAD (no branch)
```

A plain `git branch` can point at the jj commit (`git branch --list` shows it after `bookmark set`). Detached HEAD is colocated jj's normal state whenever the working copy isn't a bookmark tip.

## 5. Hazards

- **Detached HEAD after `jj commit`** (top hazard): any tool gating on `git rev-parse --abbrev-ref HEAD` prints `HEAD`, not `master`. Mitigation: after commits, `jj bookmark set master -r @-` and `git switch master` — or accept detachment (this repo's gates don't read the branch name; verified: gates still exit 0 in detached state).
- **Index sync**: after `jj undo`, git showed ` M .jj-probe/lane-identity.txt` — jj keeps the git index staged to match `@`; `git commit` would work but the file shows as already-staged. `git stash --include-untracked`/`git stash pop` round-tripped cleanly under jj (verified in scratch).
- **snapshot.max-new-file-size**: default 1.0 MiB. Empirical: a 2.0 MiB untracked file → `Warning: Refused to snapshot some files: .jj-probe/big.bin: 2.0MiB ... the maximum size allowed is 1.0MiB`, **exit 0** (warns, doesn't fail). Live repo has no untracked >1 MiB files; the only >1 MiB files are already gitignored. No config needed today; `jj config set --repo snapshot.max-new-file-size …` is the documented fix if a lane ever drops big artifacts unignored.
- `.ufo/interactive-sessions/` is gitignored and stays ignored for jj (jj honors `.gitignore`) — transcripts are never snapshotted.
- No hooks, no special files, no credential-named files, no submodules/symlinked-tracked-paths.

## Cleanup evidence

`du -sh` before delete: 32M. `rm -rf /home/vgpnk/Projects/shokunin/.tower/jj-probe/tabi-shokunin` executed; `ls .tower/jj-probe/` afterwards shows only sibling lane probes, `tabi-shokunin` gone. Live repo untouched (every jj/mutating command ran only inside the scratch; only `git -C <live> status|ls-files|ls-tree`, `find`, `du`, `cat` were run against the live checkout).
