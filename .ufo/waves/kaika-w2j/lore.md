# kaika W2j — jj colocate probe: `lore-shokunin`

Repo: `/home/vgpnk/Projects/shokunin/lore-shokunin` (live branch `main`, HEAD `6cec83ae` — "gitignore: stop re-tracking per-seat wave scratch and baseline copies").
Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/lore-shokunin` (76M after probe files removed; **deleted** after run; live repo re-verified: `git status --porcelain` shows only pre-existing `?? .scratch/`, HEAD unchanged at `6cec83ae`).

## Verdict: `safe-with-config`

Required before any `jj` command in the live main checkout:

1. **`jj config set --repo user.name lore-shokunin` + `--repo user.email lore@shokunin.local`** — jj authors from `~/.config/jj/config.toml` (`Joao Pedro Veiga <jpveigao10@gmail.com>`), NOT `git config` (`ci <ci@local>`). One-shot `--config user.name=…` flags set only the *committer* on the resulting git commit; author fell back to the jj user config (observed: `9047dcf Joao Pedro Veiga <jpveigao10@gmail.com> | lore-shokunin <lore@shokunin.local>` in `git log --format='%an <%ae> | %cn <%ce>'`). With repo-scoped config: `1715d62 lore-shokunin <lore@shokunin.local> | lore-shokunin <lore@shokunin.local>` — both fields correct.
2. **Add `.scratch/` to `.gitignore` first** — the 26 untracked `.scratch/` files would otherwise be snapshotted into jj's working-copy commit *and* staged into git's index on the first `jj st` (see hazards). Largest untracked file is `.scratch/*/scratch-root/corpus/tools/dependency-freeze-contract.json` at 34,095 bytes — far under the 1MiB snapshot cap, so no `snapshot.max-new-file-size` override needed for what exists today.
3. No `.gitignore` entry needed for `.jj/` itself: `jj git init --colocate` writes `.jj/.gitignore` containing `/*`, and `git check-ignore -v .jj/repo` confirms git already ignores everything under it.

## Checklist results

### 1. Pristine baseline (scratch clone, HEAD `6cec83ae`)

All lane gate-registry entries from `SKILL.md` run from repo root:

| Command | Baseline exit |
|---|---|
| `python3 corpus/tools/boundary_doc_check.py` | 0 (`CERTIFIED`, replay_receipts=3/3, anchors=2/2) |
| `python3 corpus/tools/boundary_doc_check.py --self-test` | 0 (8/8 cases PASS) |
| `python3 corpus/tools/discriminate_check.py` | 0 (`DISCRIMINATION HELD`) |
| `python3 corpus/tools/discriminate_check.py --checker e97613c` | 2 (`REGRESSION-DETECTED` — expected negative control) |
| `python3 corpus/tools/map_obligations.py --self-test` | 0 (`SELF-TEST CASES 25/25 pinned`, `RESULT PASS`) |
| `python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review` | 0 (`RESULT PASS`, raw=22 mapped=22) |
| `python3 corpus/tools/dependency_freeze.py --self-test` | 0 (`SELF-TEST 19/19`, `RESULT PASS`) |
| `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review` | 0 (`RESULT PASS`, events 9/9, edges 8/8) |
| `python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review` | 0 (`CLEAN: … 0 violations`) |
| `python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review` | 0 (`RESULT PASS`, VALIDATED-ROWS 24/24) |

### 2. `jj git init --colocate` (jj 0.45.1, `~/.local/bin/jj`)

- `jj git init --colocate` → `Done importing changes… Initialized repo in "."` (rc 0). Set `trunk()` = `main@origin`.
- First `jj st`: **0.007s** (real) on clean tree. Output: working copy `37b221e9 (empty)`, parent `6cec83ae` carrying `main`, `main@origin`, `kaika/round@origin` bookmarks.
- `jj diff --stat -r @`: `0 files changed` — nothing snapshotted (scratch was clean).
- `git status` after init: clean, `On branch main`, `up to date with 'origin/main'`. `git rev-parse --abbrev-ref HEAD` → `main`; `git rev-parse HEAD` → `6cec83ae…`. Git did not observe `.jj/` at all.

### 3. Gates re-run under colocated jj

Every command above re-run → **identical exit codes** (0/0/0/2/0/0/0/0/0/0). No branch- or index-dependence finding.

Git-dependence grep over `corpus/tools/*.py` + `corpus/fixtures/check_bible.py` found only content-addressed calls, all safe in colocate:
- `boundary_doc_check.py:416,495` `git show <rev>:<path>`; `:527` `git ls-tree -r --name-only <rev>` (SHA-pinned revisions, never `HEAD`-by-name).
- `discriminate_check.py:47` `git show e97613c:corpus/fixtures/check_bible.py` (literal pinned SHA).
- `dependency_freeze.py:429` `git rev-parse HEAD` — needs only a valid HEAD; in colocate HEAD follows jj's working-copy parent (see step 4), still a valid SHA.
- No `symbolic-ref`, `--abbrev-ref`, `git status`, `git diff --cached`, `git add`, `git stash`, or hook usage anywhere in the lane tools. No git hooks installed (`.git/hooks/` has only `*.sample`; `core.hooksPath` unset).

### 4. Lane-identity commit flow

- `jj --config user.name=lore-shokunin --config user.email=lore@shokunin.local commit -m … <path>` → commit `9047dcfb` with **wrong author**: `git log -1 --format='%an <%ae> | %cn <%ce>'` → `Joao Pedro Veiga <jpveigao10@gmail.com> | lore-shokunin <lore@shokunin.local>`. The `--config` flags applied only to the committer of the ephemeral command.
- Fix verified: `jj config set --repo user.name lore-shokunin && jj config set --repo user.email lore@shokunin.local`, then `jj commit` → `git log -1` → `lore-shokunin <lore@shokunin.local> | lore-shokunin <lore@shokunin.local>` (author AND committer).
- `jj bookmark set w2j-probe -r 'description("w2j probe 2*")'` → `Created 1 bookmarks pointing to xkzlsylr 1715d625`; `git branch --list -v` shows `w2j-probe 1715d62` — git branch materializes immediately.
- HEAD behavior: after `jj commit` where `@`'s new parent holds no local bookmark, `git rev-parse --abbrev-ref HEAD` prints `HEAD` (detached, "HEAD detached from refs/heads/main") — jj does NOT auto-advance `main`; `main` stayed at `6cec83a`. `git status` still clean; `git rev-parse HEAD` returns the jj commit SHA. Any fleet tooling keyed on `--abbrev-ref` would read `HEAD` instead of `main` (lane's own tools: none use it — verified above).
- Reverse direction verified: `git switch main` + git-side commit `837a1bb` → next `jj st` printed `Reset the working copy parent to the new Git HEAD. Done importing changes from the underlying Git repo.` and `jj log` shows `mosksnnl 837a1bb0 main`. Bidirectional colocate works as documented (https://jj-vcs.github.io/jj/latest/git-compatibility/ — "colocated workspaces").

### 5. Hazards

- **Linked git worktree (TOP HAZARD):** `git worktree list` shows `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/lore-shokunin` on branch `kaika/round` with *live untracked round files* (`.ufo/waves/round-103/`, `corpus/QUALITY.md`, `corpus/knowledge/r103-*.md`, `corpus/lessons/` — all `??` in that worktree's own status). jj has no worktree support (docs: git worktrees unsupported; jj workspaces are the analog). Colocating the main checkout is safe *for the main checkout* — the kaika worktree keeps working via pure git — but **no `jj` command may ever be run inside the worktree**, and anything that exports/rewrites bookmarks (`jj bookmark move/delete`, `jj git push`) could move `kaika/round` under a live craft round. `main` itself stayed put in my probes.
- **Stealth snapshot of untracked files:** `echo stealth > STEALTH-UNTRACKED.txt` → `git status` shows `??`; after `jj st`, git status shows ` A` — the file is committed into jj's `@` commit AND staged into git's index. `git show HEAD:STEALTH-UNTRACKED.txt` → `exists on disk, but not in 'HEAD'`. Consequence for the live repo: the first `jj st` there commits all 26 `.scratch/` files into `@` and stages them; a subsequent git-side `git commit -a` or rebase in the main checkout would drag them along. Same probe with a planted `jj-probe-secret.env` (`PASSWORD=hunter2`): snapshotted silently with no credential warning.
- **`snapshot.max-new-file-size`:** planted 2MiB `jj-probe-large.bin` → `jj st` printed `Warning: Refused to snapshot some files: jj-probe-large.bin: 2.0MiB … maximum … 1.0MiB`, left it `?` untracked (default 1MiB cap, matching docs https://jj-vcs.github.io/jj/latest/config/#maximum-size-of-new-files). Live checkout: **no untracked files >1MiB** (`git ls-files --others --exclude-standard | xargs du -b` → max 34,095 B). The >1MiB `.ufo/interactive-sessions/*.jsonl` files are gitignored (`.gitignore:1 .ufo/interactive-sessions/`) and jj respects `.gitignore` — they are not snapshotted.
- **`git stash` degraded:** `git stash -u -- STEALTH-UNTRACKED.txt` on a jj-snapshotted file → `error: Entry 'STEALTH-UNTRACKED.txt' not uptodate. Cannot merge. Cannot save the current worktree state`. jj's index projection breaks stash on snapshotted paths (stash list stayed empty).
- **Special files:** none — `find` over live checkout for `-type p` (FIFO) / `-type s` (socket) returned zero hits.
- **Credential-name scan:** `git ls-files --others --exclude-standard | grep -iE 'secret|token|cred|\.env|\.pem|\.key|id_rsa|password'` → no matches.
- **Self-test scratch dirs:** `map_obligations.py --self-test` / `dependency_freeze.py --self-test` create `*-self-test-*/` dirs at repo root (gitignored via `*-self-test-*/` rule; live `v05-self-test-scratch` is such a dir, 948K, untracked). Under jj in live, these transient dirs would still be ignored — consistent.

## Evidence snippets

```
$ jj op log --limit 5   (proves snapshot-per-command + undoability)
@  e075c6680f0f vgpnk@plazir27 default@ now, lasted 14 ms  │ snapshot working copy │ args: jj status
○  ca891a680209 … import git refs │ args: jj status
○  8bf60d913c36 … import git head │ args: jj status
○  490a33aaaf0c … point bookmark w2j-probe to commit 1715d625…

$ jj undo → "Undid operation: e075c6680f0f … snapshot working copy"
  → STEALTH-UNTRACKED.txt (deleted by rm before the undone snapshot) restored: "Added 2 files"
```

## Restoration evidence

Scratch clone deleted: `rm -rf /home/vgpnk/Projects/shokunin/.tower/jj-probe/lore-shokunin` (size at deletion: 76M — after removing probe files; `.scratch/w2j-probe/` was a dir I created inside scratch, not live). Live repo post-check: HEAD `6cec83ae…`, `git status --porcelain` → only `?? .scratch/` (pre-existing, 26 files, unchanged).
