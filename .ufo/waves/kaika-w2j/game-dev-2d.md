# kaika W2j probe — game-dev-2d-shokunin

**Repo:** `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin` (live branch `main`, HEAD `e89905162b3a630a599607279681b30572010724` — "round-104 record")
**Scratch:** `/home/vgpnk/Projects/shokunin/.tower/jj-probe/game-dev-2d-shokunin` (deleted; 1.3 GB on disk at deletion)
**jj:** `jj 0.45.1-7c41cdeb…` · **git:** `2.55.0` · **date:** 2026-10-19

## Verdict: **safe-with-config**

Colocated jj works on this lane: clean 42.5k-file import, snapshot cost negligible, every read-only gate output-identical before/after. Two configuration/behavior items are required knowledge before lane agents run jj commands.

## Baseline facts (live repo, read-only)

- `git rev-parse --abbrev-ref HEAD` → `main`; `git status --porcelain` → **0 entries** (fully clean).
- `git ls-files | wc -l` → **42,524** tracked files; worktree 1.7 GB, `.git` 337 MB.
- Special files: `find -type p` → **0 FIFOs**, `-type s` → **0 sockets**, `-type l` → **34 symlinks, all absolute, all pointing into the live repo** (e.g. `corpus/live/r67-simplifier/del-measure/fixtures/*.gd -> /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin/corpus/fixtures/*`). jj tracks them identically (`jj st` clean after init).
- Untracked-but-not-ignored files: **0** (`git ls-files -o --exclude-standard | wc -l` → 0). 5 ignored entries: `corpus/fixtures/__pycache__/`, `corpus/live/r101-ver11/{mut02run/proj/.godot,scratch}/`, `corpus/live/r101-ver17/scratch/`, `corpus/live/runs/` — covered by `corpus/.gitignore` (`runs*/`, `**/__pycache__/`, `**/.godot/`). Nothing untracked for a first jj snapshot to sweep up.
- Credential-named files: none (scan for `*key*/ *secret*/ *token*/ *.pem/ *cred*/ .env*` hit only `key-shas.txt`, `case_keyed_diff.py`, `key_and_pin_census.py` — evidence files, no secrets).
- Untracked files >1 MiB: none → `snapshot.max-new-file-size` config **not needed**.
- `.jj/` git-ignore coverage: **automatic** — `jj git init` writes `.jj/.gitignore` containing `/*` (verified: `git check-ignore -v .jj/repo/store` → `.jj/.gitignore:1:/*`; `git status` stays clean).
- Repo-local `git config` already carries lane identity `user.name=game-dev-2d-shokunin`, `user.email=game-dev-2d@shokunin.local`. No hooks installed (`ls .git/hooks` — samples only).
- Lane docs: no `SKILL.md`, no `tools/`/`scripts/`/`verifiers/` top-level dirs; self-tests live under `corpus/live/rNN-<role>/`. Lane remote: `github.com/VeigaPunk/shokunin-godot-2d`.

## Step 1 — pristine baseline (scratch clone)

Clone: `git clone --local --no-checkout` → 10 ms; `git checkout main` → 2.33 s.

Gates used (read-only; battery/Godot runners excluded — they spawn Godot/write `runs/`):
| gate | result |
|---|---|
| `git status --porcelain` | 0 lines |
| `git rev-parse HEAD` | `e8990516…` |
| `git diff HEAD --stat` | 0 lines |
| `git fsck --no-dangling` | rc=0, no output |
| `sha256sum -c corpus/live/{r97,r98,r99}-{scout,boundary}/manifest.sha256` | all tracked files `: OK` (rc=1 only because gitignored `runs/`/`scratch/` files absent — identical failure set every run, e.g. r99-scout 30 OK/575 absent) |
| `python3 corpus/live/r99-scout/verify_rows.py` | rc=0 (`ROWS 0/0`, `ROWS_PREFIX 0/0`, classifier sha `749fa060…`) — thin: its `runs/` data is gitignored |
| `python3 corpus/live/r95-simplifier/head_check.py` (uses `git rev-parse HEAD`, `git show`) | rc=0, deterministic output |
| `python3 corpus/live/r95-verifier/probes/verify_laws.py` | **rc=1 KeyError `r95b_order_celloff_y1000`** — *pre-existing stale script*, not a jj finding: LOG.md r103 records that case was deliberately RETIRED; committed script never updated |

## Step 2 — `jj git init --colocate`

- `time jj git init --colocate` → **0.563 s** ("Done importing changes from the underlying Git repo"; `trunk()` alias → `main@origin`; also imported remote bookmark `kaika/round@origin` from an existing `origin/kaika/round` ref).
- First `jj st` → **0.017 s** (snapshot already folded into init; op log shows `import git refs` 8 ms + `import git head` 25 ms).
- Dirty-worktree snapshot measured separately: appended a line to `SHONEN.md`, `time jj st` → **0.112 s**; warm re-scan → 0.020 s. **First-snapshot cost on 42,524 files ≈ 0.1 s — negligible.**
- `jj diff --stat -r @` → `0 files changed`; `git status` → clean; `git rev-parse --abbrev-ref HEAD` → `main` (still attached at this point).
- Store sizes: `.jj/` total **4.0 MB** (`.jj/repo/store` 64 KB — colocated mode reuses `.git` objects; `op_store` 92 KB after ~13 ops). jj does **not** duplicate the 337 MB object store.

## Step 3 — re-run gates after init

Every gate **bit-identical to baseline**: same manifest OK/absent counts (`diff` of r99-scout output → IDENTICAL), `verify_rows.py` rc=0 same sha, `head_check.py` rc=0 same output (HEAD unchanged `e8990516`), `git status`/`git diff HEAD` clean, `fsck` clean. Grep for branch/index-dependent tool code: `rev-parse --abbrev-ref|symbolic-ref|git status|diff --cached|git add|git stash` → 18 files, all `corpus/live/*/watch.sh` monitoring scripts (see hazards).

## Step 4 — lane-identity commit flow

1. `mkdir jj-probe-scratch; echo … > probe.txt` → `jj st` shows `A jj-probe-scratch/probe.txt` instantly.
2. `jj --config user.name=… --config user.email=… commit` alone is **insufficient**: author is fixed when @ is created (machine default `Joao Pedro Veiga <jpveigao10@gmail.com>` observed via `jj log -r @ -T 'author'`).
3. Fix: `JJ_USER=game-dev-2d-shokunin JJ_EMAIL=game-dev-2d@shokunin.local jj metaedit --update-author -r @`, then `jj --config user.name=game-dev-2d-shokunin --config user.email=game-dev-2d@shokunin.local commit -m 'test: jj probe scratch commit' jj-probe-scratch`.
4. `git log -1 --format='%an <%ae> | %cn <%ce>'` → **`game-dev-2d-shokunin <game-dev-2d@shokunin.local> | game-dev-2d-shokunin <game-dev-2d@shokunin.local>`** — both identities correct.
5. `jj bookmark set jj-probe-test -r @-` → `git branch --list` → `jj-probe-test` exists, points at `c3c5a775`. Bookmark→branch export works.

## Step 5 — hazards

1. **Detached HEAD after jj commits (TOP HAZARD).** `jj git init` left HEAD on `main`, but after `jj commit` / `jj new`, `git rev-parse --abbrev-ref HEAD` → `HEAD` (detached at the new commit). `jj bookmark set main -r @-` did **not** reattach. Docs confirm this is by design: "jj commands will usually put the Git repo in a 'detached HEAD' state … Before doing mutating Git commands, you may need to tell Git what the current branch should be with a `git switch` command" — https://jj-vcs.github.io/jj/latest/git-compatibility/ (Git compatibility → "Using both jj and Git"). Impact here: 18 `corpus/live/*/watch.sh` scripts run `git status`/`git diff`-class commands; `head_check.py` uses `git rev-parse HEAD` (works — prints sha, unaffected by attachment). Anything parsing `rev-parse --abbrev-ref` output or doing `git switch`/`commit` unconditionally will break or commit to a detached HEAD. Mitigation: lane agents must run `git switch main` before pure-git mutating flows, or do all mutations through jj and move `main` with `jj bookmark`.
2. **34 absolute symlinks into the live repo.** Tracked symlinks in `corpus/live/r6x…/fixtures/` resolve to `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin/corpus/fixtures/*` — absolute, so in any clone/worktree they dereference into the live checkout, not the clone. Read-only ops fine (all gates passed); any tool that *writes through* a fixture symlink would mutate the live repo. jj preserves them as symlinks (no change in `jj st`). Not a jj regression — a pre-existing repo property every probe/lane must respect.
3. **`jj commit` author trap (config item).** Lane must set author before commit (`jj metaedit --update-author` or `jj new` with `--config user.name/email` at change-creation, or repo-level `jj config set --repo user.name/user.email` once — simplest, since `.git/config` already has the values and jj reads `--repo` config persistently). Otherwise author leaks the host user's real name/email into commits.
4. Remote bookmark `kaika/round@origin` exists alongside `main` — jj `trunk()` defaulted to `main@origin`, correct.
5. No FIFOs/sockets, no untracked files, no big untracked files, `.jj/` auto-ignored — items all clean.

## Evidence pointers

- Op log at deletion: 13 ops, `op_store` 92 KB, whole `.jj` 4.0 MB vs `.git` 265 MB (scratch clone) — op-log overhead negligible.
- `jj undo` verified: undid `jj new`, restored op `785e8b73…`; git view consistent throughout.
- Scratch deleted: `rm -rf .tower/jj-probe/game-dev-2d-shokunin` (1.3 GB); live repo untouched (`git status` there still 0 entries — verified before cloning, no writes ever performed against it).

## Verdict detail

**safe-with-config.** Required before lane use: (a) repo-level `jj config set --repo user.name/user.email` (or the metaedit step per commit) for lane identity; (b) lane-agent rule "run `git switch main` before any pure-git mutating command, or stay entirely in jj + `jj bookmark`" — because jj deliberately leaves git HEAD detached. Top hazard: the detached-HEAD state breaking `rev-parse --abbrev-ref`-style tooling (18 watch.sh scripts use git-status-class calls) combined with absolute symlinks that dereference into the live checkout from any clone.
