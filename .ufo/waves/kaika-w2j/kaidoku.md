# kaika W2j — jj colocate probe: kaidoku-shokunin

Repo: `/home/vgpnk/Projects/shokunin/kaidoku-shokunin` (live branch `main`, HEAD `de77d754523afb673b4421d363fe89311644af4f`)
Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kaidoku-shokunin` (git clone --local --no-checkout + `git checkout main`; 193M on disk; **deleted after probe**)
jj: `~/.local/bin/jj` = `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`

## Live-repo read-only facts (pre-clone)

- `git status --porcelain` → **0 lines** (clean). `git ls-files` → **14,849 tracked** (`.ufo/` = 14,731, corpus = 104).
- Untracked-but-not-ignored files: **0** (`git ls-files -o --exclude-standard | wc -l` → 0). Nothing for a colocated first snapshot to sweep up.
- Special files: `find … \( -type p -o -type s \)` → none outside `.git`. Two tracked symlinks (mode 120000): `.ufo/waves/arc3-loop1-round4/claims/c3/EX-25/fixtures/scratch/alias-{1,2}.conf` → `/var/tmp/ex25-r4/...` (dangling; snapshot stores link text only — fine).
- No submodules (no mode-160000 entries). `.gitignore` = `__pycache__/`, `*.pyc` only.
- Largest tracked files ~6.2 MB (`.ufo/…/function-copy.json` etc.) — all already tracked, so `snapshot.max-new-file-size` is a non-issue here.

## 1. Pristine baseline (scratch clone, pre-jj)

| Gate | Command | Exit |
|---|---|---|
| interactive-r1-recovery | `python3 .ufo/rounds/interactive-r1/verify-recovery.py` | **0** — `RECOVERY_EVIDENCE: CLEAN finding=pinned_package_consistent author_review=9/9 coverage=70/72` |
| citation-drift | `python3 .ufo/gates/citation-drift/citation-drift-probe.py --root . --rev de77d75… --table .ufo/gates/citation-drift/pointer-table.json --expected .ufo/gates/citation-drift/expected.json` | **0** — `findings=0` |
| c1-census-v10 | `python3 .ufo/gates/c1-census-v10.py --root $PWD` | **0** — `VERDICT: PASS (stale=0 ambiguous=0 undeclared=0 unresolved=0)`, G21 frontier 14 rows, errors [] |
| custody-pair | `python3 .ufo/gates/custody-pair/custody-pair.py capture --out <probe-root>/custody-kaidoku-pristine.txt --label jj-probe-pristine` | **0** — `OK paths=5/5` |

## 2. `jj git init --colocate`

- Output: `Initialized repo in "."` + hint to `jj bookmark track main@origin` (only a hint; nothing auto-tracked).
- First `jj st`: **0.010s** real — "The working copy has no changes." `@` = `szqtysms 847a6481 (empty)`, parent = `de77d754` carrying bookmarks `kaika/round@origin main main@origin`.
- `jj diff --stat -r @` → `0 files changed`. `git status --porcelain` → **0 lines**.
- `git rev-parse --abbrev-ref HEAD` → `main`; `git symbolic-ref HEAD` → `refs/heads/main` (**immediately after init, HEAD still on branch**).

## 3. Gates re-run post-init — identical exit codes

recovery → 0 (CLEAN, same findings); citation-drift → 0 (findings=0); census → 0 (PASS); custody capture → 0 (OK 5/5, new receipt sha b834ffca… vs pristine d6d84cfe… — receipts differ only in label/timestamps as designed).
Branch/index dependence grep over all four gate scripts (`rev-parse --abbrev-ref`, `symbolic-ref`, `git status`, `git diff --cached`, `git add`, `git stash`): **no hits**. Gate logic is `--rev`-pinned (`git rev-parse --verify <rev>^{commit}`), not branch-dependent. No `.git/hooks` besides samples.

## 4. Lane-identity commit flow

- `jj commit` with `--config user.name=kaidoku-shokunin --config user.email=kaidoku@shokunin.local` wrapping the **commit** itself: `git log -1 --format='%an <%ae> | %cn <%ce>'` → **`kaidoku-shokunin <kaidoku@shokunin.local> | kaidoku-shokunin <kaidoku@shokunin.local>`** ✓
- ⚠ Caveat measured, not asserted: author is stamped when the *working-copy change is created* (first `jj st`), not at commit. `jj st` run without `--config` then `jj commit` with `--config` produced `git log` → `Joao Pedro Veiga <jpveigao10@gmail.com> | kaidoku-shokunin <kaidoku@shokunin.local>` (git-global author, lane committer). Per-repo fix: `jj config set --repo user.name kaidoku-shokunin` + `user.email` in `.jj/repo/config.toml`, so every jj invocation in the repo inherits identity.
- `jj commit --author` / `jj describe --author`: **not supported in 0.45.1** (`--help` shows no `--author` on either; usage error when tried).
- Bookmark → git branch: `jj bookmark set jjprobe-test -r @-` → `git branch --list` shows `jjprobe-test` pointing at the new commit. ✓
- `jj op log` works: shows `commit`, `point bookmark`, `snapshot working copy` ops → `jj undo`/`jj op restore` available.
- **HEAD detachment**: after `jj commit`, `git symbolic-ref HEAD` fails (`fatal: ref HEAD is not a symbolic ref`); `git status -sb` → `## HEAD (no branch)`; `rev-parse --abbrev-ref HEAD` → literal `HEAD`. In colocated mode jj leaves Git HEAD detached at the working-copy's parent after any history-mutating op (documented colocation behavior, https://jj-vcs.github.io/jj/latest/git-compatibility/ — "colocated" section). `git checkout main`/`jj git export` restores it, but tools that read the branch name after a jj op see `HEAD`, not `main`.

## 5. Hazards

- None found: no FIFOs/sockets, no untracked files (so nothing >1 MiB to hit `snapshot.max-new-file-size`, no credential-looking names), clean status, `.gitignore` needs no `.jj/` entry (jj stores state in `.jj/` which git never sees as tracked; `git status` stayed 0 lines throughout).
- Residual risk classes (for fleet adoption note, not blockers): (a) detached HEAD after jj ops — any tool polling `git rev-parse --abbrev-ref HEAD` mid-session reads `HEAD`; (b) author identity must be pinned per-repo in `.jj/repo/config.toml` or the git-global identity leaks into jj-authored commits; (c) 2 dangling tracked symlinks are carried as link text, harmless.

## Verdict

**safe-with-config** — all four read-only gates byte-identical in exit code and verdict pre/post init; snapshot clean (0 files); lane identity achievable and verifiable in git. Required config: `jj config set --repo user.name <id>-shokunin && jj config set --repo user.email <id>@shokunin.local` before the first `jj st` (or pass `--config` on every jj command *starting with* the first snapshot op). Top hazard: **jj detaches git HEAD after each mutating op** — callers relying on `rev-parse --abbrev-ref HEAD` = `main` will silently read `HEAD`; harmless to these gates (they pin `--rev`) but a real interface change for any branch-aware tooling.
