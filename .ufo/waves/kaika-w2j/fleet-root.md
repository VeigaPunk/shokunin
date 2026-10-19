# W2j probe — fleet root `/home/vgpnk/Projects/shokunin` (branch `master` @ `31baf5cb`)

**Verdict: safe-with-config.** Required: `.git/info/exclude` must contain `.tower/` **before the first jj command** — it does in the live repo (line 8), so the only real prerequisite is verifying it's still there (and adding `local/` if that dir ever gains files). Top hazard: `jj` leaves git HEAD **detached** after export ops — `git rev-parse --abbrev-ref HEAD` prints `HEAD` instead of `master`, and anything snapshotted once stays in @ even if you later ignore it.

Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/shokunin`, 42 MB (clone of a 29 MB tracked tree; `.git` pack 7214 objects). Deleted after probe.
jj 0.45.1 at `~/.local/bin/jj`. Live repo untouched; all jj ran in scratch only.

## Context corrections
- Assignment said exclude covers `.tower/` **and `local/`** — actual live `.git/info/exclude` has only `.devin/mcp_config.local.json` and `.tower/` (verified `git check-ignore -v`; `local/` is **not** ignored anywhere). Live `local/` contains only the empty dir `local/fleet-analysis`, which is why `git status` is clean anyway.
- Assignment said 26 worktrees under `.tower/` — actually **27 entries** in `.tower/worktrees/kaika/` (21 `*-shokunin` lanes + fleet-census/contract/driver/ledger/protocol/kimi-shokunin-canon). `.tower/` is **75 GB** (`du -sh`).

## 1. Baseline gates
Repo has **no runnable test/gate infrastructure**: no Makefile, package.json, tests/, verifiers/, or SKILL.md gate registry; only script is `scripts/shokunin-watchdog.sh` (mutates `.ufo/state`, launches processes — skipped per protocol). Baseline = git invariants on the pristine scratch clone:
- `git status --porcelain` → 0 lines (clean)
- `git fsck --no-progress` → exit 0, dangling commits only (pre-existing)
- `git rev-parse --abbrev-ref HEAD` → `master`; `git symbolic-ref HEAD` → `refs/heads/master`
- Hooks: none installed (only *.sample)
- Watchdog grep for `rev-parse --abbrev-ref|symbolic-ref|git status|git diff --cached|git add|git stash` → **0 hits**; it does no git ops itself.

## 2. `jj git init --colocate`
- Output: "Done importing changes from the underlying Git repo." + `trunk()` alias → `master@origin`; hint to `jj bookmark track master@origin`.
- **First `jj st`: 13 ms** (timed `date +%s%N` delta; snapshot happened at init-import). Result: `@` empty, parent = `31baf5cb`, `master` + 4 `kaika/*@origin` remote bookmarks visible.
- `jj diff --stat -r @` → `0 files changed`. `git status` after → clean, still `On branch master`. `abbrev-ref` → `master`, `symbolic-ref` → `refs/heads/master` (HEAD intact *after init* — it detaches later, see §6).
- `jj file list` → **2856 files, exactly the git-tracked set** (`.ufo/` = 2128 = `git ls-files .ufo | wc -l`); **0 under `.tower/` or `local/`**.

## THE critical check — jj does NOT snapshot `.tower/` / `local/`
Decoys planted in scratch: `.tower/worktrees/kaika/fake-lane/decoy.md`, `local/fleet-analysis/decoy.md` (with `local/` appended to scratch's `.git/info/exclude`).
- With exclude in place: `jj st` → "no changes"; `jj file list | grep -E '^\.tower|^local'` → 0. **`.tower/` (75 GB live) never enters jj's working-copy commit.**
- **Negative control**: deleted `.tower/` line from exclude → `jj st` instantly showed `A .tower/worktrees/kaika/fake-lane/decoy.md`. Restored exclude → **file stayed in @** (re-ignoring does not untrack a snapshotted file; needs `jj file untrack` or delete). `git status` simultaneously showed ` A .tower/…decoy.md` — jj had **staged it into the git index**, so a stray `git commit -a`-style flow would have committed it.
- Docs cite: https://docs.jj-vcs.dev/latest/git-compatibility/ § ".gitignore: Yes" — "ignores in `.git/info/exclude`… are supported… you might need to run `jj file untrack` to exclude newly ignored files".
- `.jj/` needs **no** `.gitignore` coverage: init writes `.jj/.gitignore` containing `/*` (`git check-ignore -v .jj/repo` → `.jj/.gitignore:1:/*`).

## 3. Post-init gates — all unchanged
`git status` 0, `abbrev-ref` → `master` (at that point), `fsck` clean-but-dangling. No exit-code changes; watchdog has no branch deps.

## 4. Lane-identity commit flow — author caveat is REAL
`jj commit --config user.name=… --config user.email=…` sets the **committer only**; @'s author is fixed at creation (per W2jScribe; confirmed by `jj metaedit --help` showing `--update-author` exists for this).
Working recipe (both identities verified):
```
JJ_USER='protocol-shokunin' JJ_EMAIL='protocol@shokunin.local' jj metaedit --update-author -r @
jj --config user.name='protocol-shokunin' --config user.email='protocol@shokunin.local' commit -m 'test lane identity' jj-probe-scratch/lane-test.md
```
→ `git log -1 --format='%an <%ae> | %cn <%ce>'` = `protocol-shokunin <protocol@shokunin.local> | protocol-shokunin <protocol@shokunin.local>` ✔
`jj bookmark set master -r ccfd4509` → `git branch -v` shows `master ccfd450 [ahead 1]`; git log shows the lane commit ✔.
Plain `git -c user.name='fleet-root-shokunin' … commit` also works in the colocated repo and round-trips both identities ✔.

## 5. Hazards
- **HEAD detaches on jj export ops** (the top hazard). After `jj commit`/`metaedit`: `.git/HEAD` = raw sha `ccfd4509` (@-), `git status` → "HEAD detached from 31baf5c", `abbrev-ref` → `HEAD`, `symbolic-ref` → fatal. `git checkout master` reattaches and *stays* attached until the next mutating jj op. Documented: git-compatibility § Colocated — "jj commands will usually put the Git repo in a 'detached HEAD' state… you may need to tell Git what the current branch should be with `git switch`". Any tool doing `git rev-parse --abbrev-ref HEAD` for lane identity **breaks**; none found in this repo, but the 21 running lanes' tooling must be audited before enabling jj on live.
- **`snapshot.max-new-file-size` = 1 MiB default**: a 2 MiB `big-decoy.bin` → "Warning: Refused to snapshot some files… maximum 1.0MiB", left untracked (`?`). Max tracked file here is 307 KB (`MANIFEST.json`), 0 tracked files >1 MiB — fine today, but any future big artifact needs `snapshot.max-new-file-size` config or `.gitignore`.
- Special files: `find -type p -o -type s` → **none**.
- Credentials: `.devin/mcp_config.local.json` (MCP config, 8 KB `.devin/`) is properly excluded → never snapshotted. No untracked-but-not-ignored files exist at all in the live root (`git status --porcelain` = 0). Credential-named files under `.ufo/waves/*-scratch/` are already `.gitignore`d; `research/…/census/raw/` has its own `.gitignore`.
- **`local/` not excluded in live repo** — empty today, but if it ever gains files they'll be snapshotted into commits. Add `local/` to `.git/info/exclude` (cheap insurance).
- git worktrees unsupported by jj — **fine here**: the 27 `.tower` worktrees are *nested checkouts* inside a normal dir, invisible to jj both by exclude and because jj never descends into nested `.git`. Fleet worktree traffic unaffected.
- Hooks: jj doesn't run them (docs + none installed anyway).

## 6. Op log / undo (the upgrade payoff — verified)
- `jj op log` recorded init-import, snapshot, metaedit, commit, bookmark-set as separate ops (~8 ms each).
- `jj undo` after `jj bookmark set` → `master` instantly back to `31baf5c`, git status clean.
- A raw `git commit` imports as an "import git head" op; `jj undo` doesn't remove it (git-side is truth), but `git reset --hard 31baf5c` re-imports cleanly and jj lands back on the same state — mixing worked flawlessly.
- jj writes change-id + `refs/jj/` headers to git commits; `git cat-file -p` shows them.

## Recommended config for this repo
```
# .git/info/exclude (already has .tower/): add
local/
# optional repo config if big artifacts expected:
jj config set --repo snapshot.max-new-file-size 10485760
```
