# jj colocated probe — `kama-shokunin` (live branch `master`)

Repo: `/home/vgpnk/Projects/shokunin/kama-shokunin` · Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kama-shokunin` (removed after probe) · jj `0.45.1-7c41cdeb` · git `2.55.0`

## Verdict: safe-with-config

Colocated jj is functionally safe for this repo — every gate exit code is identical before and after `jj git init --colocate`, and `jj bookmark` ↔ git branch interop works. **But the default commit path leaks the ambient operator identity (`Joao Pedro Veiga <jpveigao10@gmail.com>`) into the author field** unless the working-copy commit is described with the lane identity before `jj commit`. Required config below.

## 1 · Pristine baseline (scratch clone)

Repo is small and clean: `.git` 1.2 M, 66 tracked files, no worktrees/submodules/LFS (`.gitattributes`/`gitmodules` absent). Gates are in `tools/` (per SKILL.md "Local gate/probe registry").

| Gate | Command | Exit | Notes |
|---|---|---|---|
| self-test | `bash tools/test-snapshot.sh` | `0` | `RESULT pass=24 fail=0`; hermetic, only writes to mktemp dir it removes |
| reconciliation gate | `bash tools/kama-probe.sh check` | `2` | `registry_rows_evaluated=3 model_ok=0 drift=3 exit=2` — all 3 consumers `DEAD`/`connection-refused` (expected drift) |
| machine output | `bash tools/kama-probe.sh check --json` | `2` | schema `kama-probe/v1` |
| consumer provenance | `bash tools/kama-probe.sh consumers` | `0` | `consumer_rows_evaluated=3` |
| listener census | `bash tools/kama-probe.sh listeners` | `0` | `probed=16 model_endpoints=7 … dead=3` |
| snapshot/persist | `bash tools/kama-probe.sh snapshot --history $PWD/probe-history` | `2` | `transitions=0`; wrote history inside scratch |

`check`/`snapshot` connect only to declared loopback endpoints (refused instantly, rc=7); `test-snapshot.sh` binds an ephemeral `http.server` on `127.0.0.1:0`. Read-only, in-scope.

## 2 · `jj git init --colocate` + first `jj st`

```
$ jj git init --colocate
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `master@origin`
Initialized repo in "."
$ time jj st        → real 0m0.007s   (.jj = 140K)
```

First `jj st` auto-snapshotted the untracked `probe-history/` files (created by my baseline `snapshot` run) into the working-copy commit: `jj diff -r @` showed `A probe-history/{.lock,…tsv,…json,DELTA.md}`.
- `git status` afterwards: files appear **staged** (` A …`) — git sees jj's WC commit as index+worktree state. Interop intact.
- `git rev-parse --abbrev-ref HEAD` → `master` immediately after init.

## 3 · Re-run gates post-jj — zero exit-code drift

| Gate | Baseline exit | Post-jj exit | Δ |
|---|---|---|---|
| `test-snapshot.sh` | `0` (24/24) | `0` (24/24) | none |
| `check` | `2` | `2` | none |
| `check --json` | `2` | `2` | none |
| `consumers` | `0` | `0` | none |
| `listeners` | `0` | `0` | none (`probed=15` vs `16` = live-host socket churn, not jj) |
| `snapshot --history` | `2` | `2` | none |

`grep` over `tools/*.sh` + `SKILL.md` for `rev-parse|symbolic-ref|git status|git diff|git add|git stash|git checkout|git log|git branch` found **only comments** — the lane's tools are git-state-independent (pure registry/curl/ss), so colocation cannot perturb them. No git hooks installed (`.git/hooks/` has only samples).

## 4 · Lane-identity commit flow — split-identity hazard found & fixed

**First attempt** (`jj --config user.name='kama-shokunin' --config user.email='kama@shokunin.local' commit -m … <path>`):

```
$ git log -1 --format='%an <%ae> | %cn <%ce>' 66f52e7
Joao Pedro Veiga <jpveigao10@gmail.com> | kama-shokunin <kama@shokunin.local>
```
`--config` on `commit` only set the **committer**. The **author** of the finalized WC commit was frozen when jj auto-created it during `init`/`st`, inheriting the *ambient global* user (`Joao Pedro Veiga <jpveigao10@gmail.com>`, confirmed via `jj config get user.name`). Conversely the *new* WC commit (`8a90420`) got lane-author + ambient-committer.

**Working recipe** — describe the WC with identity *before* committing:
```
jj --config user.name='kama-shokunin' --config user.email='kama@shokunin.local' describe -m '…'
jj --config user.name='kama-shokunin' --config user.email='kama@shokunin.local' commit -m 'test2' <path>
```
→ `git log` then shows `4c520c3 | A:kama-shokunin <kama@shokunin.local> | C:kama-shokunin <kama@shokunin.local>`. Cleaner still: `jj config set --repo user.name kama-shokunin; jj config set --repo user.email kama@shokunin.local` once after init so every auto-created WC commit is lane-attributed (repo config verified present at `.jj/repo/config.toml`).

**Bookmark→branch:** `jj bookmark set master -r 4c520c3` → `git branch -v` shows `master 4c520c3 [ahead 2] test2`; `git log master` walks the lane commits. Branch interop confirmed. `git rev-parse --abbrev-ref HEAD` prints `HEAD` (detached at the WC commit) after commits — normal colocated-jj behavior; `master` itself moved correctly.

## 5 · Hazards

- **Author-identity leak (top hazard):** see §4 — naive `jj commit` records the operator's global identity as *author*. Mitigate with `--repo user.*` config at init or `describe` before commit.
- **Untracked live files get snapshotted into `@`:** live checkout has `.ufo/round-10/{plan.json(1711B),SEAT-PROTOCOL.md(4413B)}` not-ignored (`git ls-files --others --exclude-standard`). First jj command in live repo would stage them into the WC commit and `git status` would show them as staged `A` — could confuse an agent expecting a clean status. All `.ufo/round-*` prior rounds are *tracked*; round-10 is the only untracked payload. Both files < 1 MiB → within `snapshot.max-new-file-size`.
- **Special files:** none — `find … -type p -o -type s -o -type b -o -type c` empty; no symlinks (`-type l` empty). 
- **Credentials:** no `*cred*|*.pem|*.key|*secret*|*.env|*token*` names found in live checkout.
- **`.jj/` in git:** jj auto-excludes it — `git status` and `git ls-files .jj` both clean, `git check-ignore .jj` matched. **No `.gitignore` change needed.** Live `.gitignore` contains only `.ufo/interactive-sessions/`.

## Bottom line
**safe-with-config.** Set repo-level `user.name`/`user.email` to the lane at init (or describe-then-commit) to avoid ambient-author leakage; everything else — gates, bookmarks↔branches, `.jj` git-hiding — is clean. Top residual hazard: colocated jj silently snapshots any untracked-but-not-ignored files (like live `.ufo/round-10/`) into `@` on its first command.
