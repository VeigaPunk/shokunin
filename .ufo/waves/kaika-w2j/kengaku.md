# kaika W2j — jj colocated probe: kengaku-shokunin

**Verdict: safe-with-config.** Required config: `jj config set --repo user.name "kengaku-shokunin"` and `user.email "kengaku@shokunin.local"` (set at/after `jj git init --colocate`, before authoring any commits). Top hazard: jj detaches `git HEAD` permanently in colocated mode — even with the working copy sitting on `master`, `git rev-parse --abbrev-ref HEAD` prints `HEAD`, and `git push`/`git checkout`-style flows fail with "You are not currently on a branch". No committed tool in this repo depends on an attached HEAD, but any ad-hoc `git commit && git push` must go through `jj bookmark set` + `jj git push` (or `git push origin HEAD:master`).

## Probe environment

- Repo: `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, live branch `master` @ `99cf615c`
- Live state pre-probe: `git status --porcelain` → 0 lines (clean). `git status --porcelain=v2 --ignored=matching` → only `! .ufo/interactive-sessions/` (gitignored; nothing untracked).
- jj 0.45.1 (`jj --version` → `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, `~/.local/bin/jj`)
- Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kengaku-shokunin`, built with `git clone --local --no-checkout … && git -C … checkout master`; 11M on disk at teardown (`du -sh`); **deleted**, verified with `test ! -d` → `SCRATCH_DELETED`.
- Live repo post-probe: `status --porcelain` 0 lines, HEAD `master`. Untouched.
- Repo size: 277 tracked files (`git ls-files | wc -l`), 9.4M worktree / 3.7M `.git` (`du -sh`). Largest tracked file `corpus/evidence/round12-ladder/results-r12.jsonl` 1,427,319 B (tracked — `snapshot.max-new-file-size` only governs *new* files, so no issue).

## Step 1 — pristine baseline (scratch clone)

Gates from `SKILL.md` §Gate/probe registry (line 541ff):

| Gate | Command | Baseline |
|---|---|---|
| hermetic-grader | `python3 grader.py` | `CHECKS n=733 mismatches=0 errata_pinned=1`, `VERDICT: PASS`, exit **0** |
| hermetic-grader selftest | `python3 grader.py --selftest` | `ALL PASS` S0–S7, exit **0** |
| coverage-census | `python3 corpus/evidence/round13-coverage/coverage_census.py` | exit **0** (WORKTREE census; 12 evidence files, 24 lessons+27 knowledge rows; `unindexed` lists are the tool's normal output) |

No network, no credentials needed; all run in the scratch clone.

## Step 2 — `jj git init --colocate`

```
Initialized repo in "."      (exit 0; revset alias trunk() → master@origin)
time jj st                   real 0m0.006s   (277-file repo — negligible)
jj st → "The working copy has no changes."
jj diff --stat -r @          0 files changed   (wc commit is empty; gitignored
                             files were NOT snapshotted — .ufo/ absent)
git status                   clean (0 porcelain lines)
git rev-parse --abbrev-ref HEAD → master     (still attached at init)
```

`.jj/` handling: no `.gitignore` edit needed. jj writes `.jj/.gitignore` containing `/*` inside its own dir; `git check-ignore -v .jj/repo/store` → `.jj/.gitignore:1:/*` — git sees `.jj` as ignored (`!! .jj/` in `status --ignored`), not untracked.

## Step 3 — gates re-run after init

| Gate | After jj init |
|---|---|
| `python3 grader.py` | `CHECKS n=733 mismatches=0`, exit **0** — identical |
| `python3 grader.py --selftest` | `ALL PASS` — identical |
| `coverage_census.py` | exit **0** — identical JSON output |

`coverage_census.py` is the only committed tool that shells to git (`git rev-parse --verify`, `git ls-tree`, `git show` — all detached-HEAD-safe; grep: `coverage_census.py:43-110`). `grader.py` invokes only `sys.executable` for selftest subprocs (line 5537). No hooks installed (`.git/hooks/` = samples only). No branch/index dependence found in the gate surface.

## Step 4 — lane-identity commit flow

First attempt showed a pitfall:

```
jj --config user.name=kengaku-shokunin --config user.email=kengaku@shokunin.local commit -m test <path>
git log -1 --format='%an <%ae> | %cn <%ce>'
→ Joao Pedro Veiga <jpveigao10@gmail.com> | kengaku-shokunin <kengaku@shokunin.local>
```

`--config` applies only to that one command and only as *committer*: the empty working-copy commit was **authored at `jj git init` time** under the machine-global identity, and `jj commit` preserves the existing author. Fix — repo-level config makes author and committer correct:

```
jj config set --repo user.name "kengaku-shokunin"
jj config set --repo user.email "kengaku@shokunin.local"
jj new && jj commit -m "test2" <path>
git log -1 --format='%an <%ae> | %cn <%ce>'
→ kengaku-shokunin <kengaku@shokunin.local> | kengaku-shokunin <kengaku@shokunin.local>
```

(Only the author of the ephemeral init-time wc commit carries the global identity; every subsequent commit is correct. Pre-seeding `~/.config/jj/config.toml` or passing `--config` on the `jj git init` line itself would eliminate even that.)

Bookmark→branch export:

```
jj bookmark set jj-probe-test -r @-
git branch --list jj-probe-test  → jj-probe-test
git rev-parse jj-probe-test      → c7872155de3f…  ("test2: lane identity via repo config")
```

## Step 5 — hazards

- **Detached git HEAD (main finding).** After the first `jj commit`, `git rev-parse --abbrev-ref HEAD` → `HEAD` (detached at `@-`). `jj new master` does **not** reattach: `git status` reports `HEAD detached at refs/heads/master`. `git push --dry-run` → `fatal: You are not currently on a branch.` This is documented colocated behavior — jj exports the wc-parent to detached HEAD (https://jj-vcs.github.io/jj/latest/git-compatibility/ — "colocated repos" / HEAD handling). Any fleet tooling or human habit relying on `git rev-parse --abbrev-ref HEAD` == lane branch, `git push`, `git stash`, or `git rebase` must move to `jj` equivalents (`jj st`, `jj git push -b`, `jj op restore`, `jj rebase`). Verified none of the repo's committed gates do this.
- **Git-native commits still work** but are absorbed: `git commit` on the detached HEAD + `jj st` → "Reset the working copy parent to the new Git HEAD"; the commit is reachable only via reflog/`jj op log` unless a bookmark is set — orphan risk for scripts that commit then push by branch name.
- **Special files:** `find <live> \( -type p -o -type s \)` → none. `find -type l` → no symlinks. No FIFOs/sockets.
- **Untracked-but-not-ignored in live checkout:** none (`status --porcelain` clean; only ignored `.ufo/interactive-sessions/`). jj's first snapshot would capture nothing; confirmed by `jj diff --stat -r @` = 0 files.
- **Untracked >1 MiB:** none (no untracked files at all). Largest tracked file 1.4 MB — already in history, unaffected by `snapshot.max-new-file-size` (default 1 MiB applies to *new* files only).
- **Credential-looking names:** `find -iname '*secret*' -o -iname '*token*' -o -iname '*cred*' -o -name '.env*' -o -name '*.pem' -o -name '*.key'` → none.
- **`.gitignore` for `.jj/`:** not required — jj self-excludes via `.jj/.gitignore` (`/*`); verified with `git check-ignore -v`. Adding `.jj/` to the repo `.gitignore` is harmless but unnecessary.
- **`jj op log`** works as advertised: init, snapshot, commit, bookmark-set, and `import git head` ops all recorded with timestamps (sampling shown in session).

## Notes for fleet rollout

- Colocation order that gives clean lane identity: `jj git init --colocate` → `jj config set --repo user.name/user.email <lane>` → (optional `jj bookmark track master@origin`).
- Anything in other lanes grepping for `git symbolic-ref`/`--abbrev-ref HEAD` should be flagged — pattern will read `HEAD` under jj.
