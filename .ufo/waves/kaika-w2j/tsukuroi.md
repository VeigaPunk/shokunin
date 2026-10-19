# kaika W2j — jj colocate probe: tsukuroi-shokunin

**Repo:** `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin` (live branch `master`)
**Scratch:** `/home/vgpnk/Projects/shokunin/.tower/jj-probe/tsukuroi-shokunin` — created per protocol, measured 4.5M total (`.git` 2.5M, `.jj` 352K), **deleted after probe** (`rm -rf`, verified gone).
**jj version:** `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`; git `2.55.0`.
**Verdict: `safe-with-config`** — per-repo lane identity must be configured before the first snapshotting command; see §4.

## Live repo facts (read-only)

- `git -C <live> branch --show-current` → `master`; `git status --porcelain` → **0 lines** (clean).
- `git ls-files | wc -l` → **86 tracked files**; `du -sh --exclude=.git` → 4.3M; `.git` → 2.4M.
- **No untracked-but-not-ignored files** (`git status --porcelain --ignored | grep -v '^!!'` empty) — a first jj command would snapshot nothing extra. `snapshot.max-new-file-size` is moot: no untracked files exist at all.
- **No FIFOs/sockets** outside `.git` (`find -type p -o -type s` empty). **No credential-looking files** (`*cred*`, `*.pem`, `*secret*`, `*.key`, `*.env*`, `*token*` → empty).
- `.gitignore` (27 bytes) contains only `.ufo/interactive-sessions/`; `.jj` needs no manual ignore — see §2.

## Checklist

### 1. Pristine baseline (scratch clone)

The repo's one gate is `tools/tsukuroi-census.sh` (2409 lines; six-plane read-only host census with a hermetic `--selftest`). It is the sole registered gate (SCORECARD.md:49 quotes `bash tools/tsukuroi-census.sh --selftest` → rc=0, plus the live run; no other `tools/`, `scripts/`, or `verifiers/` entries exist). The selftest writes only into `mktemp -d /tmp/tsukuroi-r3-2-selftest.XXXXXX` with `trap 'rm -rf'` (tool :1573-1574) — the only out-of-scratch write; verified **no residue** after the run.

- `bash tools/tsukuroi-census.sh --selftest` → **rc=0**, `TSUKUROI_CENSUS_SELFTEST: PASS (80 cases, 80 passed, 0 failed)`, 12.6 s wall.
- `bash tools/tsukuroi-census.sh` (live, read-only) → **rc=1**, `TSUKUROI_CENSUS: DEGRADED (packages=DEGRADED systemd=HEALTHY drivers=DEGRADED journal=DEGRADED update-safety=DEGRADED oom=DEGRADED)` — expected: real host findings, not a failure.
- `git status --porcelain` before/after → 0 lines (zero-mutation contract holds).

### 2. `jj git init --colocate`

- `jj git init --colocate` → rc=0, `Done importing changes... Initialized repo in "."`; set `trunk()` alias to `master@origin`, hinted to `jj bookmark track master@origin`.
- First `jj st` → **6 ms**, rc=0: `Working copy (@): utmqtuwn 99efd477 (empty)`, parent `9b70381c ... master master@origin`.
- `jj diff --stat -r @` → `0 files changed` — snapshotted nothing (clean tree).
- `git status` → 0 porcelain lines, `On branch master`; `git rev-parse --abbrev-ref HEAD` → **`master`** (still attached right after init).
- `.jj` needs **no** `.gitignore` coverage: `jj git init` writes `.jj/.gitignore` containing `*`, so `git status --ignored` shows `!! .jj/` and status stays clean. `.git/info/exclude` untouched; root `.gitignore` untouched.

### 3. Gates re-run post-init — no exit-code change

- `--selftest` → rc=0, identical `PASS (80 cases, 80 passed, 0 failed)`.
- Live census → rc=1, same rollup `TSUKUROI_CENSUS: DEGRADED (...)` (host counters drift, rollup identical).
- `git status --porcelain` → 0.
- `git grep` over tracked files: the gate script itself runs **no git commands** (`grep -n 'git '` → none); `rev-parse --abbrev-ref`/`symbolic-ref`/`git stash`/`git diff --cached`/`git add` appear only in prose docs. **No branch- or index-dependence in the tool.** No git hooks installed (`.git/hooks/` has only samples).

### 4. Lane-identity commit flow

- `jj --config user.name=tsukuroi-shokunin --config user.email=tsukuroi@shokunin.local commit -m "..." PROBE-SCRATCH-ONLY.md` → rc=0, but `git log -1 --format='%an <%ae> | %cn <%ce>'` → `Joao Pedro Veiga <jpveigao10@gmail.com> | tsukuroi-shokunin <tsukuroi@shokunin.local>`: the working-copy change had already been snapshotted by the earlier `jj st` under the user's global jj config, and `jj commit` preserves the existing change's **author**, applying `--config` only to the committer.
- Fix: pass `--config` to the *first* snapshotting command (or use `jj config set --repo`). Verified: with `--config` on the snapshotting `jj st`, `git log` → `tsukuroi-shokunin <tsukuroi@shokunin.local> | tsukuroi-shokunin <tsukuroi@shokunin.local>` (author **and** committer).
- `jj config set --repo user.name/user.email` → writes `~/.config/jj/repos/<config-id>/config.toml` (keyed by `.jj/repo/config-id`, here `651a7d15952d5938a4eb`; config-id survives clone→clone? — it is generated per-repo at init, so **each lane repo needs the `--repo` config set once**; it does not travel in `.git`). Verified contents: `[user] name = "tsukuroi-shokunin" email = "tsukuroi@shokunin.local"`. Then plain `jj commit` produces `tsukuroi-shokunin <tsukuroi@shokunin.local>` as author+committer.
- `jj bookmark set probe-test -r ec65c1d4` → `git branch --list` shows `probe-test` at that commit. Bookmark↔branch sync confirmed. (`jj describe`/`jj commit` have **no `--author` flag** in 0.45.1.)
- Git-side interop: `git switch master` + a plain `git -c user.name=... commit` was imported by the next `jj st` (`Reset the working copy parent to the new Git HEAD`; `master | git-side commit interop test`). Mixing git and jj in one repo works.

### 5. Hazards found

1. **Detached HEAD after `jj commit`/`jj new`/`jj undo` on non-bookmarked parents.** After `jj commit`, `git rev-parse --abbrev-ref HEAD` → `HEAD` and `git status` shows `HEAD detached`. `jj new master` left `HEAD detached at refs/heads/master` — jj exports a detached HEAD pointing at @- unless @- carries a bookmark it can attach to. Any tooling reading the branch name (or scripts that `git commit` expecting a branch) silently commits detached. Mitigation: always `jj bookmark` the parent, or `git switch <branch>` after jj ops; `jj` re-imports the reattachment cleanly.
2. **`jj undo` rewinds exported git refs.** Two `jj undo`s in sequence restored the op log past the git-side commit: `git log -1` went `e5ad13c git-side commit interop test` → `9b70381 tsukuroi: fleet-r1...` — i.e., **`master`'s branch tip moved backwards**, leaving `e5ad13c` dangling. Powerful safety net, but an accidental `jj undo` can revert a git-made commit without any reflog-visible "delete" (it is visible via `jj op log`/`git reflog`).
3. **Author-identity trap (above):** `jj st`/`jj commit` sequence snapshots with whatever `user.name` is configured *at snapshot time* — a bare `jj st` before the lane config would pin the operator's real identity as author of everything snapshotted.
4. No special files, no large untracked files, no credential-looking files in the live checkout — the snapshot hazards (max-new-file-size, special files) do not apply here.
5. Per-repo jj config lives outside the repo (`~/.config/jj/repos/<id>/`); cloning/recloning a lane loses it and `jj` silently falls back to the operator's global identity.

## Bottom line

`safe-with-config`: set `jj config set --repo user.name tsukuroi-shokunin` + `user.email tsukuroi@shokunin.local` **before the first jj command** (or pass `--config` to every snapshotting command). Gates unaffected (tool is git-free; zero-mutation contract holds). Top hazard: **detached HEAD after jj ops** — pair every working-copy move with a bookmark or a `git switch` to keep branch-name consumers correct; second-order: `jj undo` rewinds git-exported branch tips.
