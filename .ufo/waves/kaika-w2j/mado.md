# kaika W2j jj-probe — mado-shokunin

- **Repo**: `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, HEAD `e1d81d4` ("mado: ignore interactive session logs"), 80 tracked files, working tree clean (`git status --porcelain` → 0 lines).
- **Scratch**: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/mado-shokunin`, `git clone --local --no-checkout` + `git checkout master`, 4.6 MiB at deletion. **Deleted after probe.**
- **jj**: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5` at `~/.local/bin/jj`.
- **Verdict: `safe-with-config`.**

## Step 1 — pristine baseline gate

Gate: `tools/mado-verify.sh` (3,232 lines; the repo's own verdict gate). Its live mode reads
`$HOME/.config`, `hyprctl`, `systemctl`, `busctl` — outside scratch scope — so the in-repo,
write-isolated detector is `--selftest` (hermetic fixtures under `/tmp/w5-mado-m52-*`, stubbed
`omarchy`/`git` PATH shims; touches nothing in the repo or substrate).

```
$ bash tools/mado-verify.sh --selftest        # in scratch, pre-jj
MADO_SELFTEST: 268/268 assertions passed
rc=0
```

Note: the selftest stubs `git` itself (fixture `runner-stub.sh`, `MADO_R8_GIT_STUB`), so it never
inspects the enclosing repo — exit code cannot differ due to jj by construction; still verified
empirically below.

## Step 2 — `jj git init --colocate`

```
$ jj git init --colocate
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `master@origin`.
Initialized repo in "."                                     rc=0

$ time jj st                    # first status, includes snapshot
The working copy has no changes.
Working copy  (@) : kznltwyx ec1f32f5 (empty) (no description set)
Parent commit (@-): mozrrzzv e1d81d48 kaika/round@origin master master@origin | mado: ignore interactive session logs
real    0m0.006s

$ jj diff --stat -r @
0 files changed, 0 insertions(+), 0 deletions(-)

$ git status --porcelain        # → empty (clean); full status: "On branch master … nothing to commit"
$ git rev-parse --abbrev-ref HEAD
master                        # unchanged — git tooling still sees a normal branch checkout
```

Snapshot semantics confirmed: jj created a fresh empty `@` commit on top of `master` and moved
nothing; `git` still reports `master` at `e1d81d4`. `.jj/` contents are git-invisible because
`jj git init` writes `.jj/.gitignore` containing `/*` — verified:
`git check-ignore -v .jj/repo` → `.jj/.gitignore:1:/*`. **No root `.gitignore` edit needed.**

## Step 3 — gate re-run after jj init

```
$ bash tools/mado-verify.sh --selftest        # post-init
MADO_SELFTEST: 268/268 assertions passed      rc=0
$ diff baseline.out postjj.out  → identical   SELFTEST_OUTPUT_IDENTICAL
```

No branch/index dependence: `grep -n 'git' tools/mado-verify.sh` shows every real `git` call is
`git -C "$ROOT/.local/share/omarchy" describe|rev-parse|show` (omarchy checkout, not this repo);
no `rev-parse --abbrev-ref`, `symbolic-ref`, `git status`, `git add`, `git stash` against the
enclosing repo. No git hooks active in the live repo (`.git/hooks/` = samples only).

## Step 4 — lane-identity commit flow

Required identity: `mado-shokunin <mado@shokunin.local>`.

**Finding (checklist-prescribed command is insufficient):**

```
$ echo … > .jj-probe-scratch/probe.txt
$ jj --config user.name=mado-shokunin --config user.email=mado@shokunin.local \
     commit -m "test: mado-shokunin jj colocate probe" .jj-probe-scratch/probe.txt
$ git log -1 --format='%an <%ae> | %cn <%ce>'
Joao Pedro Veiga <jpveigao10@gmail.com> | mado-shokunin <mado@shokunin.local>
```

`--config user.*` set only the **committer**; the author came from global gitconfig, because the
author of the working-copy commit is stamped at snapshot/`jj new` time and `jj commit`/`describe`
retains it (no `--author`/`--reset-author` flag on `commit` or `describe` in 0.45.1; verified via
`jj help commit|describe`).

**Two working remediations (verified):**

```
$ JJ_USER=mado-shokunin JJ_EMAIL=mado@shokunin.local jj metaedit --update-author -r kznltwyx
$ git log -1 --format='%an <%ae> | %cn <%ce>'
mado-shokunin <mado@shokunin.local> | mado-shokunin <mado@shokunin.local>

$ JJ_USER=mado-shokunin JJ_EMAIL=mado@shokunin.local \
     jj commit -m "test: second probe via JJ_USER env" .jj-probe-scratch/probe2.txt
$ git log -2 --format='%h %an <%ae> | %cn <%ce>'
f89ad83 mado-shokunin <mado@shokunin.local> | mado-shokunin <mado@shokunin.local>
9f417f9 mado-shokunin <mado@shokunin.local> | mado-shokunin <mado@shokunin.local>
```

`JJ_USER`/`JJ_EMAIL` env (documented in `jj help metaedit` and
https://jj-vcs.github.io/jj/latest/config/#user -- "user.name/user.email … JJ_USER, JJ_EMAIL")
sets both author and committer in one shot. A repo-scoped `jj config set --repo user.name …`
would also work but persists state; env vars are the clean per-invocation answer for the lane
commit flow.

**Git branch points at the jj-made commit:**

```
$ jj bookmark set jj-probe-mado -r @-
Created 1 bookmarks pointing to unptlpvk f89ad83f jj-probe-mado
$ git branch --list jj-probe-mado -vv
  jj-probe-mado f89ad83 test: second probe via JJ_USER env
$ git log -1 jj-probe-mado → resolves
```

Bonus: `jj op log` shows the full recorded operation history (snapshot, commit, metaedit,
bookmark set) — the undo/restore surface works in colocated mode.

## Step 5 — hazards (live checkout)

| Hazard | Result | Command |
|---|---|---|
| FIFOs / sockets | none | `find … -type p -o -type s` → empty |
| Symlinks | none | `find … -type l` → empty |
| Untracked files >1 MiB | none untracked at all | `git ls-files --others --exclude-standard` → empty; `git status --porcelain` → 0 lines |
| Large file present but ignored | `.ufo/interactive-sessions/…/…jsonl` 1.6 MiB; dir 2.6 MiB | `find -size +1M`, `du -sh` — covered by `.gitignore:1` `.ufo/interactive-sessions/` (`git check-ignore -v` confirms), so jj will not snapshot it |
| Credential-shaped names | none (`corpus/knowledge/keybind-rule-semantics.md` matched `*key*` — a doc, names-only scan) | `find -iname '*cred*'/'*secret*'/'*token*'/'*.pem'/'*.env'` |
| `.gitignore` for `.jj/` | auto-covered by `.jj/.gitignore` (`/*`), written by `jj git init` itself | `cat .jj/.gitignore`; `git check-ignore -v .jj/repo` |
| Git hooks | none active (`.git/hooks/` samples only) | `ls .git/hooks | grep -v .sample` → empty |

## Conclusion

**`safe-with-config`.** Colocate is clean for this repo: zero behavior change to git
(`master` stays checked out, `git status` clean, gate byte-identical), `.jj/` self-ignored,
the only >1 MiB file already ignored. **Required config**: lane identity must be exported as
`JJ_USER`/`JJ_EMAIL` (or repo-scoped `jj config`) — `--config user.*` alone leaves the author as
the host's global gitconfig identity. **Top hazard**: that author-identity asymmetry — a lane
using the checklist's bare `--config` command would publish commits authored `Joao Pedro Veiga
<jpveigao10@gmail.com>` (committed `mado-shokunin`), breaking the lane-identity contract on
every commit.
