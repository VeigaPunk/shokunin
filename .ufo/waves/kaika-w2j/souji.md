# kaika W2j — jj colocate probe: souji-shokunin

Repo: `/home/vgpnk/Projects/shokunin/souji-shokunin` (branch `master`, HEAD `dcc8b9e8`, clean).
Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/souji-shokunin` (80 MB incl. `.jj` 384 KB; deleted after probe).
jj: `jj 0.45.1-7c41cdeb` at `~/.local/bin/jj`.

## Live-repo pre-flight (read-only)
- `git status --porcelain` → empty (clean, no untracked, no ignored surprises).
- No sockets/FIFOs: `find . -path ./.git -prune -o \( -type s -o -type p \) -print` → nothing.
- No untracked files at all (`git ls-files --others --exclude-standard` → 0), so none >1 MiB and none credential-shaped (name grep of the empty set).
- No `.gitignore` file in repo; `.scratch/` is *tracked* (`s29-freeze-dir.txt`), `.ufo-reports-placeholder` tracked.
- No live git hooks (`ls .git/hooks | grep -v sample` → empty).

## Step 1 — pristine baseline (scratch)
Gate used: `tools/souji-round9-selftest.sh <kind> <tool>` (self-contained: fixtures in mktemp,
`GIT_CONFIG_NOSYSTEM=1`, no network, no fleet reads). Runners 23/32 read the real fleet
(`FLEET_ROOT=$(REPO/..)`, `kotodama-shokunin`) — in scratch that resolves to the jj-probe dir,
so they are not portable baselines; skipped.

| Tool | result |
|---|---|
| `tools/souji-verify.sh` | rc=0, 16 PASS / 0 FAIL |
| `tools/souji-vault-verify.sh` | rc=0, 16 PASS / 0 FAIL |
| `tools/souji-quarantine.sh` | rc=0, 28 PASS / 0 FAIL |

(Note: `tools/souji-vault.sh` does not exist; vault tool is `souji-vault-verify.sh`.)

## Step 2 — `jj git init --colocate`
- Init output: hint that `master@origin` is not tracked (`jj bookmark track master@origin` suggested); repo initialized.
- First `jj st`: **0.006 s** (snapshot already done at init; repo is small, 1546 tracked files). "The working copy has no changes."
- `jj diff --stat -r @` → `0 files changed`. Working-copy commit `xqylrwup 21fe50fd` (empty), parent = `dcc8b9e8` = master tip.
- `git status` after init: clean, "On branch master". `git rev-parse --abbrev-ref HEAD` → `master`.
- `.jj/` ignore coverage: jj writes `.jj/.gitignore` containing `/repo` and `/working_copy`; `git status --ignored` shows `.jj/*` ignored. **No .gitignore change needed.**

## Step 3 — gates after init
Identical results: verify 16/0, vault-verify 16/0, quarantine 28/0, all rc=0. **No exit-code change.**

Tooling dependence scan (live repo `tools/`):
- No reader of the local branch name: zero hits for `rev-parse --abbrev-ref` / `branch --show-current`. The ~10 `symbolic-ref HEAD refs/heads/$b` hits (souji-census.sh, impl-35/47, cand-*) are all fixture *writers* inside mktemp repos, never run against the lane repo.
- Receipt logic is remote-ref based and fail-closed: `pushed` requires the introducing commit to be an ancestor of `origin/HEAD` / `origin/*` and `git log --branches --not --remotes -- <path>` empty — both unaffected by how the local HEAD is attached.
- Quarantine flow (`impl-04.sh` comment: "Git mutations are exactly: git mv, git add -A -- .ufo-quarantine, git commit") — plain `git add`/`git commit` still work in the colocated clone (verified in step 4).

## Step 4 — lane-identity commit flow
- `jj --config user.name=… --config user.email=… commit` → **committer correct, author leaked the global git identity** (`author=Joao Pedro Veiga <jpveigao10@gmail.com>`): the working-copy snapshot had already captured the fallback identity before `--config` applied. `--config` on the commit command is NOT sufficient.
- Correct methods (both verified, `git log -1 --format='%an <%ae> | %cn <%ce>'` → `souji-shokunin <souji@shokunin.local> | souji-shokunin <souji@shokunin.local>`):
  - env: `JJ_USER=souji-shokunin JJ_EMAIL=souji@shokunin.local jj commit …`
  - persistent: `jj config set --repo user.name souji-shokunin` + `user.email souji@shokunin.local`
- `jj bookmark set probe-branch -r @-` → `git branch --list` shows `probe-branch` at the jj commit. Bookmark→branch works.
- Git-side flow while colocated: `git add` + `git commit` succeed; next `jj st` prints "Reset the working copy parent to the new Git HEAD" and imports it. No index-lock problems observed (shared index).

## Step 5 — hazards
1. **Detached git HEAD (top hazard).** After `jj commit`, git HEAD detaches: `git rev-parse --abbrev-ref HEAD` → `HEAD`; `git symbolic-ref HEAD` → `fatal: ref HEAD is not a symbolic ref`; `master` stays at `dcc8b9e8` (jj does not advance the checked-out branch; known upstream behavior — https://jj-vcs.github.io/jj/latest/git-compatibility/ "the Git HEAD will be detached"). Any `git log --branches --not --remotes` run on a colocated repo **misses detached-head commits** — souji-verify's unpushed check undercounts. Impact is bounded (the `pushed` receipt still fails closed via merge-base, yielding `pushed-unverifiable`), but census/verify scripts read `.git` facts directly and will under-report.
2. `.scratch/` is tracked, so working-copy writes there are snapshotted normally — fine; but first `jj st` on a dirty live checkout would snapshot whatever is dirty into `@` (live repo currently clean, so a non-issue today).
3. `master@origin` untracked on init — cosmetic hint, but fleet tooling relying on `jj` sees remote bookmark drift until `jj bookmark track` is run.
4. Author leak without env/repo config (step 4) — required config, see verdict.

## Verdict
**safe-with-config.**

Required config/usage for this lane:
- `jj config set --repo user.name souji-shokunin` + `jj config set --repo user.email souji@shokunin.local` (or `JJ_USER`/`JJ_EMAIL` env on every jj call) — bare `--config` on `jj commit` leaves the author as the OS-global git identity.
- Treat git-side `git log --branches --not --remotes` as unreliable in a colocated repo (detached HEAD commits excluded); use `jj log`/`jj op log` for lineage or `git log --all --not --remotes` if git-side.

Scratch clone deleted: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/souji-shokunin` removed (was 80 MB).
