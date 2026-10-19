# kaika W2j — jj colocated probe: `mori-shokunin`

**Repo:** `/home/vgpnk/Projects/shokunin/mori-shokunin` (branch `master`, tip `20e2255e`)
**Scratch:** `/home/vgpnk/Projects/shokunin/.tower/jj-probe/mori-shokunin` — `git clone --local --no-checkout` + `checkout master`; ~6.0 MB total (`.git` 3.6 M, `.jj` 340 K). **Deleted after probing.**
**jj:** `~/.local/bin/jj` 0.45.1-7c41cdeb
**Live-repo pre-state:** `git status --porcelain` → empty (clean). Untracked-not-ignored files: **0** (`git ls-files -o --exclude-standard | wc -l` → 0). Ignored: 4 files, all under `.ufo/interactive-sessions/` (ignored by the repo's one-line `.gitignore`: `.ufo/interactive-sessions/`).

## Verdict: **safe-with-config**

Required config: per-repo jj identity (`jj config set --repo user.name mori-shokunin` and `user.email mori@shokunin.local`). Top hazard: **jj leaves git HEAD detached** after every history-advancing op; any tool reading `git rev-parse --abbrev-ref HEAD` or parsing `git status` for a branch name sees `HEAD`, not `master`. Mori's gates are unaffected (measured), but it is a fleet-wide contract change.

## 1. Pristine baseline (scratch clone, before jj)

| Gate | Command | Result | rc |
|---|---|---|---|
| Selftest | `bash tools/mori-census.sh --selftest` | `MORI_CENSUS_SELFTEST: PASS (66 cases, 66 passed, 0 failed)` | 0 |
| Oracle | `bash tools/mori-silence-cases.sh` | `MORI_SILENCE_CASES: matched=28 total=28` | 0 |
| Live census (scratch-scoped) | `MORI_SHOKUNIN_ROOT=<probe-parent> MORI_ROSTER_LANES=mori MORI_DISK_TARGETS="<probe-parent> /tmp" bash tools/mori-census.sh` | `MORI_CENSUS: DRIFT (findings=3 drift=1 unavailable=3 surfaces=7)` — watchdog/waves/lane `unavailable` (probe parent has no `.ufo`); journal/cgroup/disk read the host | 1 |
| Pin+drift same-root | `… --pin /tmp/jj-probe-mori-pin.txt` then `… --drift /tmp/jj-probe-mori-pin.txt` | `MORI_PIN: ok`; `MORI_DRIFT: none` | 0 / 0 |
| Drift vs committed r10 baseline | `… --drift corpus/evidence/baseline-r10-20261015T2231Z.json` | `MORI_DRIFT: +FINDING:… -FINDING:… ±SURFACE:lane.* …` — expected: different root/roster/host state | 1 |

`MORI_SHOKUNIN_ROOT` is needed because the census derives the fleet root as the parent of a `*-shokunin` lane dir (`tools/mori-census.sh:320-325`); under `.tower/jj-probe/` the parent is the probe dir, which is honest — the lanes correctly grade `unavailable`, never `silent`.

## 2. `jj git init --colocate` + first snapshot

- `jj git init --colocate` → `Done importing changes from the underlying Git repo. … Initialized repo in "."` (rc 0). It set `trunk()` = `master@origin` and hinted to `jj bookmark track master@origin`.
- First `jj st`: **6 ms** (`time` → real 0.006 s). Output: `@ znqtsqvr d3116772 (empty) (no description set)`; parent `20e2255e` `master`.
- `jj diff --stat -r @` → `0 files changed` — snapshotted nothing (clean checkout, 0 untracked files; the 4 ignored session logs were not snapshotted — `.gitignore` is honored).
- After init: `git status` → `On branch master … working tree clean`; `git rev-parse --abbrev-ref HEAD` → `master` (still symbolic; `master`/`HEAD` at `20e2255e`).
- `.jj/` needs **no** `.gitignore` entry: `jj` writes `.jj/.gitignore` containing `/*`, self-ignoring the whole dir; `git status --porcelain` stayed clean and `git ls-files -o` (no excludes) is the only listing that shows `.jj` paths.

## 3. Post-init gate re-runs — zero behavior change

| Gate | Result | rc | Δ vs baseline |
|---|---|---|---|
| `--selftest` | `PASS (66 cases, 66 passed, 0 failed)` | 0 | none |
| `mori-silence-cases.sh` | `matched=28 total=28` | 0 | none |
| live census (same env) | `MORI_CENSUS: DRIFT (findings=3 drift=1 unavailable=3 surfaces=7)` — identical findings | 1 | none |
| `--drift` vs pristine pin | `MORI_DRIFT: none` | 0 | none |

Why: the census's only git calls are `git cat-file -e HEAD:<path>`, `git log --format=%ct`, `git rev-parse --git-dir`, `git rev-parse --verify -q HEAD`, `git ls-files -mo --exclude-standard` — all under `GIT_OPTIONAL_LOCKS=0`, none branch-name-dependent (`tools/mori-census.sh:1253-1356`). No `symbolic-ref`, `--abbrev-ref`, `git status`, `git add`, `git stash`, or hooks anywhere in `tools/`; `.git/hooks/` has samples only. The oracle builds fixture repos under `/tmp/mori-silence-cases.XXXXXX` and is path-blind to the host repo (selftest likewise under `/tmp/mori-census-selftest.XXXXXX`).

## 4. Lane-identity commit flow

- `jj --config user.name=mori-shokunin --config user.email=mori@shokunin.local commit -m test JJ_PROBE.md` → commit `1a1db2f0`. `git log -1 --format='%an <%ae> | %cn <%ce>'` → **`Joao Pedro Veiga <jpveigao10@gmail.com> | mori-shokunin <mori@shokunin.local`** — `--config` on the CLI set the *committer* only; the *author* came from global gitconfig (`jj config get user.name` → `Joao Pedro Veiga`). No `GIT_AUTHOR_*`/`JJ_*` env vars were set.
- Fix measured: `jj config set --repo user.name mori-shokunin; jj config set --repo user.email mori@shokunin.local` → next `jj commit -m test2` produced `84f65d29` with `an=mori-shokunin ae=mori@shokunin.local cn=mori-shokunin ce=mori@shokunin.local`. **Repo-level config is required; `--config` CLI overrides are unreliable for the author field on this version.**
- `jj bookmark set master -r @-` → `Moved 1 bookmarks to vswtpruv 84f65d29 master*`; `git branch --list` → `master` (points at the jj-made commit); `git log` shows `(HEAD, master)`. Git can push that branch normally.

## 5. Detached-HEAD lifecycle (the top hazard)

Measured sequence: `jj commit` → `cat .git/HEAD` = raw sha (`ref HEAD is not a symbolic ref`); `git status` → `HEAD detached from refs/heads/master`; `rev-parse --abbrev-ref HEAD` → literal `HEAD`. `jj` deliberately keeps HEAD detached at `@-` (documented colocated behavior, https://jj-vcs.github.io/jj/latest/git-compatibility/ — "the Git HEAD will be detached"). `git checkout master` re-attaches cleanly and jj tolerates the symbolic HEAD; the next `jj commit` re-detaches. Index stays coherent either way: a filesystem edit snapshotted by `jj st` appears to git as ` M <file>` vs HEAD — `git diff` and jj agree on content.

`jj undo` verified end-to-end: undid `commit test3` (`Restored to operation: 3b77c4a6bbc9`), worktree change preserved as `M JJ_PROBE.md`, git log/git status consistent. `jj op log` shows per-op entries with args and durations — the upgrade value is real.

## 6. Hazards checklist

- **Special files (FIFO/socket/device):** none — `find . -path ./.git -prune -o -type p/s/b/c` → empty.
- **Untracked files >1 MiB:** none unignored; one ignored `.ufo/interactive-sessions/…/*.jsonl` is 1,612,301 B > `snapshot.max-new-file-size` (jj reports `1MiB`). Irrelevant while ignored (verified: a 2 MiB ignored `big.bin` was not snapshotted); if the `.gitignore` rule were ever removed, jj would leave new >1 MiB files untracked rather than snapshot them.
- **Credential-looking names:** none — name scan over all 156 files for `cred|secret|token|pem|key|passwd|password|.env|id_rsa|netrc` matched only the tracked lesson `corpus/lessons/2026-10-15-run-secret-timing-and-content-freshness-limits.md` (a doc, name-only match). Ignored `.ufo` session logs exist on disk (4 files) — jj never snapshots them.
- **`.jj/` gitignore coverage:** not needed — jj self-ignores via `.jj/.gitignore` = `/*`.
- **Branch/index dependence in gates:** none found (see §3); the oracle's fixture git usage is hermetic (`env -i`, fresh repos under `/tmp`).
- **Census live sweep:** running the production census with default `MORI_SHOKUNIN_ROOT` reads sibling lane `.git`s read-only — unaffected by a colocated `.jj` in the mori lane.
