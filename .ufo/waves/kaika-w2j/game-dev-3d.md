# W2j jj probe — game-dev-3d-shokunin

Repo: `/home/vgpnk/Projects/shokunin/game-dev-3d-shokunin` (live branch `main`, HEAD `7c4e5897`)
Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/game-dev-3d-shokunin` — `git clone --local --no-checkout` + `git checkout main` (1.19 s; hardlinked objects; scratch total 531 MiB, `.git` 59 MiB, `.jj` 3.0 MiB). `reports/round-107/` was copied in to reproduce live untracked state. Scratch deleted after probing.
jj version: `jj --version` → `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`. git 2.55.0.

## 1. Pristine baseline (scratch, pre-jj)

Lane read-only gates found via SKILL.md gate registry (SKILL.md:44-49, 178):

| Gate | Command | Result |
|---|---|---|
| Close-out gate CHECK 1–4 | `bash corpus/knowledge/unreal-mcp/gate/run_gate.sh` | `GATE RESULT: PASS (checks failed: 0)`; CHECK3 `CARDS=13 BAD=0`, CHECK4 `POINTERS=103 UNRESOLVED=0`, rc 0 |
| Manifest byte-identity | `(cd corpus/knowledge/unreal-mcp && sha256sum -c .manifest.d/audit-reference.sha256)` | 12 × `OK`, rc 0 |
| E-row accept | `python3 corpus/artifacts/unreal-r22/verify_descriptor.py` | `PASS local-static actual=accept`, rc 0 |
| E-row reject control | `… Headless3DFixture.bad-type.uplugin --expect-reject` | `PASS local-static actual=reject expected=reject`, rc 0 |

No non-sample hooks in `.git/hooks/` (`ls .git/hooks | grep -v sample` → empty). `git grep 'rev-parse --abbrev-ref|symbolic-ref|git status|diff --cached|git stash|git add'` → **only prose citations** in docs/lessons (e.g. gate/README.md:156 quotes `git status --porcelain` as a check humans run on a /tmp clone, not an executable gate). No branch-name dependence in tooling.

## 2. Colocated init + first snapshot

```
$ time jj git init --colocate     # real 0m0.377s
  Setting the revset alias `trunk()` to `main@origin`
  Hint: jj bookmark track main@origin …
$ time jj st                      # real 0m0.016s
  Working copy (@): opmmrkwm 9ee2d1dd (no description set)
  Parent commit  : kyzusvnk 7c4e5897 kaika/round@origin main main@origin
$ jj diff --stat -r @             # 79 files changed, 14592 insertions
$ git status --porcelain | grep -c '^ A'   → 79   (all of reports/round-107/ staged as ` A`)
$ git rev-parse --abbrev-ref HEAD → main   (still attached right after init)
```

**Snapshot finding:** first `jj st` committed all 79 untracked `reports/round-107/` files (988 KiB total, largest 39 KiB — well under default `snapshot.max-new-file-size` = 1 MiB) into working-copy commit `@`. Git sees them as staged index adds (` A` ×79). `.jj/` does NOT appear in `git status`: `jj git init` writes `.jj/.gitignore` containing `/*`, so git ignores every entry inside `.jj` and shows nothing for it (`git status | grep -v '^ A'` → empty; `git check-ignore -v .jj` → no match needed at root). **No root `.gitignore` change required** (though adding `.jj/` wouldn't hurt).

## 3. Gates re-run under jj (post-init, detached-HEAD state)

Same commands, same results — all four gates PASS, rc 0. No exit-code change. (One manifest re-run printed `error: command not found: __fnmcd` rc 127 — shell env transient in the probe harness, re-run passed rc 0; not a gate/jj interaction.) Conclusion: this lane's gates are branch- and index-agnostic.

## 4. Lane-identity commit flow

First attempt `jj --config user.name=… --config user.email=… commit -m 'test: jj probe lane identity' .jj-probe-tmp/probe.txt` **FAILED**: `Error: Failed to reset Git HEAD state — Could not acquire lock for index file … index.lock … after 1 attempt(s)` — a concurrent `git status` in the same scratch repo held `.git/index.lock`; jj retries once and gives up (transient, not corruption: `jj op log` showed no partial commit, retry succeeded).

Retry (serial), with `JJ_USER='game-dev-3d-shokunin' JJ_EMAIL='game-dev-3d@shokunin.local'`:

```
$ jj commit -m 'test: jj probe lane identity' .jj-probe-tmp/probe.txt   → rc 0
$ jj metaedit --update-author -r @-                                     → Modified 1 commits
$ git log -1 --format='%an <%ae> | %cn <%ce>' probe-test
  → game-dev-3d-shokunin <game-dev-3d@shokunin.local> | game-dev-3d-shokunin <game-dev-3d@shokunin.local>
$ jj bookmark set probe-test -r @-   → Created 1 bookmarks … probe-test
$ git branch --list → probe-test 2bad4bc  (git branch points at the jj commit, both identities correct)
$ jj undo            → removes bookmark AND the git branch (export stays in sync)
```

**Caveat (confirmed live):** `jj commit --config user.name/email` sets the **committer only**; the author is fixed when `@` was snapshotted (machine default). Lane identity needs `JJ_USER`+`JJ_EMAIL` env (or repo `~/.config/jj/config.toml`) **plus** `jj metaedit --update-author -r @-` after committing — or set `jj new --config user.name…` before snapshotting.

## 5. Hazards

1. **`git rev-parse --abbrev-ref HEAD` prints `HEAD`, not `main`.** After `jj commit`, git HEAD is detached at `@-` (`git symbolic-ref HEAD` → `fatal: ref HEAD is not a symbolic ref`; `git status` → `HEAD detached from refs/heads/main`). jj advances no branch automatically — `main` stayed at `7c4e5897` while HEAD moved to `2bad4bc`. Any git-side tooling that requires an attached branch or expects `main` == work tip breaks silently; jj bookmarks must be maintained (`jj bookmark set`/`git push -u` equivalents) and git HEAD is permanently detached while jj owns the checkout.
2. **Index-lock races.** jj writes the git index on every exported commit and retries lock acquisition **once**. Parallel git commands in the same repo (fleet tooling running `git status` while jj commits) produce hard failures. Mitigation: serialize jj vs git invocations per repo, or accept retry loops.
3. **Untracked-file sweep.** Every `jj` command snapshots: 79 files / 988 KiB landed in `@` instantly. Repo has **no untracked >1 MiB files** (`find reports/round-107 -size +1M` → none; all big binaries live under ignored `corpus/live/` and `corpus/fixtures/three/node_modules/`). Ignored coverage is good: `corpus/.gitignore`=`live/ __pycache__/ *.pyc`; `corpus/fixtures/three/.gitignore`=`node_modules/`; all `find -size +1M` hits are inside ignored dirs. `git status --porcelain` in live = 1 line only.
4. **No credential-named files** among untracked paths (`find … -iname '*cred*|*secret*|*token*|*.env|*key*|*pem*|id_rsa'` → none). Only `?? reports/round-107/` untracked in live.
5. **No FIFOs/sockets** in live checkout. One symlink `corpus/live/r101-sentinel/probes/sym/Link.uproject` sits inside ignored `corpus/live/` — never snapshotted.
6. Scale: `.jj/` cost is tiny (3.0 MiB on a 59 MiB `.git`, 531 MiB total worktree; live repo is 2.2 GiB mostly-ignored `corpus/live/runs`).

## Verdict

**safe-with-config.** Gates pass identically pre/post; lane identity achievable; `jj undo`/`op restore` work and export to git correctly. Required config/protocol: `JJ_USER`+`JJ_EMAIL` env (or jj config) + `jj metaedit --update-author` per commit, plus a `jj bookmark set` discipline to keep a git ref on the work tip since HEAD is always detached. Top hazard: **permanently detached `refs/heads` HEAD + single-retry index-lock** — any git tooling that runs `rev-parse --abbrev-ref` or `git commit/push` in this repo must be retired or wrapped; jj does not advance `main` by itself.
