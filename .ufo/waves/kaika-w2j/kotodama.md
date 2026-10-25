# jj colocate probe — kotodama-shokunin

Date: 2026-10-19. jj 0.45.1-7c41cdeb (`jj --version`). Live repo:
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` @ `main`, HEAD
`c42d675be96b6b3957e6e5c00ab192080cb70083`.
Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/kotodama-shokunin`
(`git clone --local --no-checkout` + `git checkout main`; 103M at clone, 187M
after jj init + probe artifacts). Deleted after the probe.

## Verdict: safe-with-config

Zero gate exit-code changes under colocated jj. Required config: per-invocation
`--config user.name=<id>-shokunin --config user.email=<id>@shokunin.local` (or
repo-scoped `jj config`) — see step 4 caveat. Top hazard: after the first
`jj commit`, git HEAD goes detached; any tool that needs a branch *name*
(`rev-parse --abbrev-ref HEAD`, `symbolic-ref`) sees `HEAD`/failure. None of
this repo's shipped tools do that while HEAD is resolvable.

## 0. Live-repo facts (read-only)

- `git -C <live> status --porcelain` → 0 lines. `git ls-files` → 3466 tracked.
- `git ls-files --others --exclude-standard` → **0 untracked-not-ignored**
  files → first `jj` snapshot in the live repo would commit nothing.
- Special files: `find -type p|s|b|c` → none; `git ls-files -s` mode 120000 →
  **no tracked symlinks**.
- Largest tracked file: `reports/round-23/wording/evidence/tie-break-check-receipt.json`
  1,037,171 B — **under** jj's default `snapshot.max-new-file-size` (1 MiB), and
  it is already tracked so the cap does not apply anyway.
- Credential-like tracked names: only lore content (`corpus/knowledge/…/sacred-*`,
  `reports/round-35/scout/K03-keyerror-path.md`). Credential-like *untracked*
  names all live under ignored `.scratch/` (e.g. `.ufo/waves/…/cred-hits.txt`,
  `secrets-scan.txt`) — names only, never snapshotted.
- `.gitignore`: `.ufo/state/`, `.ufo/watchdog.log`, `*.log`, `__pycache__/`,
  `/reports/supplement-opencode-1/scratch/`, `.scratch/`.
- `.scratch/` in the live checkout: 66 GB, 2444 top-level entries, including the
  registered worktree `.scratch/ca02-wt-r34` whose `.git` file points at
  `<live>/.git/worktrees/ca02-wt-r34`.

## 1. Pristine baseline (scratch clone, `TMPDIR=$PWD/.scratch`)

All exit 0 on the clean clone:

| Command | exit |
|---|---|
| `python3 -B tools/gates/phonology-sanity-gate.py --selftest` | 0 (15/15 planted IDs, 29 controls) |
| `tools/gates/lexicon-coverage-audit.py --selftest` | 0 (14/14) |
| `tools/gates/myth-consistency-gate.py --selftest` | 0 (6 planted IDs) |
| `tools/gates/costume-era-consistency-gate.py --selftest` | 0 (10/10, 21 planted) |
| `tools/gates/naming-collision-gate.py --selftest` | 0 (12 findings / 11 ids) |
| `tools/gates/handoff-packet-check.py --selftest` | 0 (11 findings / 9 ids) |
| `tools/gates/provenance-audit.py --selftest` | 0 (6 planted IDs) |
| `tools/check-gate-battery.py` | 0 (registry 7/7 + baselines) |
| `tools/source-audit-inventory.py --selftest` | 0 |
| `tools/harness/claims-freshness.py --selftest` | 0 (registry 43/43 + seam 19/19) — **uses git plumbing** |
| `tools/harness/receipt_guard.py --selftest` | 0 — **uses rev-parse/symbolic-ref/worktree** |
| `tools/assemble-d2.py --check` | 0 byte-identical |
| `tools/assemble-d2-typed.py --selftest` | 0 (11/11) |
| `tools/assemble-culture-d3.py --check` | 0 byte-identical ×2 |
| `tools/assemble-d4-typed.py --check` | 0 byte-identical |
| `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 (20/20 legs) |
| `tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 |
| `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0 |
| `tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | 0 |
| `tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 |

`git status --porcelain` after the battery: 0 lines (all writes confined to
`.scratch/` or atomic fixture-verify paths).

## 2. `jj git init --colocate`

```
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `main@origin`.
Hint: … jj bookmark track main@origin
Initialized repo in "."
```

First `jj st` (timed): **0.007 s**. Output:

```
The working copy has no changes.
Working copy  (@) : qkspvmqk 91f44d6c (empty) (no description set)
Parent commit (@-): nyzzlmwz c42d675b kaika/round@origin main main@origin | round-49 framing …
```

`jj diff --stat -r @` → `0 files changed`. Snapshot contained nothing.

Git side immediately after init:

- `git status` → `On branch main … working tree clean` (porcelain 0).
- `git rev-parse --abbrev-ref HEAD` → **`main`** — still symbolic while @ is
  empty. The detach only happens once @ moves (step 4).
- `.jj/` costs 344K and is **invisible to git with zero config**: `jj` ships
  `.jj/.gitignore` containing `/*`; `git check-ignore -v .jj/repo` →
  `.jj/.gitignore:1:/*`, and `git status --ignored` shows `!! .jj/`. No
  `.gitignore` or `.git/info/exclude` edit is needed (verified: `info/exclude`
  unchanged, `.gitignore` unchanged).

## 3. Gates re-run under colocated jj

Every command from §1 re-run → **identical exit codes, 20/20 checks, git status
still clean.** No tool depends on branch name while `HEAD^{commit}` resolves.

Git-dependence audit of `tools/` (grep for `rev-parse|symbolic-ref|git
status|git diff|git add|git stash|git worktree|subprocess.*git`):

- `tools/harness/claims-freshness.py` — `rev-parse --show-toplevel`,
  `rev-parse --verify <rev>^{commit}`, `ls-tree`, `cat-file --batch`. All
  work under colocation; HEAD indirection never used.
- `tools/harness/receipt_guard.py` — `_head_commit` uses
  `rev-parse --verify HEAD^{commit}` **first** (succeeds on detached HEAD);
  `symbolic-ref` is only the fallback for unborn branches. Its selftest even
  exercises `git worktree add --detach` under jj — passed.
- Hooks: `.git/hooks/` holds only `.sample` files; nothing runs on jj ops.
- The only places mentioning `rev-parse --abbrev-ref` are freeze.txt
  *documentation* inside `tools/gates/expected/**` — not executable code.

## 4. Lane-identity commit flow

```
jj --config user.name="kotodama-shokunin" \
   --config user.email="kotodama@shokunin.local" \
   commit -m "probe: lane identity commit" .probe-jj/marker.txt
```

`git log -1 --format='%an <%ae> | %cn <%ce>'` on the new commit `00b645d5`:

```
Author: Joao Pedro Veiga <jpveigao10@gmail.com>
Commit: kotodama-shokunin <kotodama@shokunin.local>
```

**Caveat:** jj's `--config` overrides the *committer*; the *author* comes from
the `users`-side git config (`user.name`/`user.email` in `~/.gitconfig`). To get
the lane name into `Author:` too, either pass `--config user.name=…` AND make
that the configured default for the repo (`jj config set --repo
user.name …`), or rewrite the author post-hoc. If the fleet protocol requires
lane identity in the author field, set repo-scoped jj config once:

```
jj config set --repo user.name  "kotodama-shokunin"
jj config set --repo user.email "kotodama@shokunin.local"
```

Bookmark → git branch round-trip:

```
jj bookmark set probe-lane -r @-   → Created 1 bookmarks … 00b645d5
git branch --list                  → probe-lane, main, probe-branch (+ detached HEAD marker)
git rev-parse probe-lane           → 00b645d56bc7eac033634fb776eada1386cd1703
```

HEAD state after the commit: `git symbolic-ref HEAD` → `fatal: ref HEAD is not
a symbolic ref`; `git status` → `HEAD detached from refs/heads/main`;
`rev-parse --abbrev-ref HEAD` → `HEAD`. This is the one behavioral change a
live lane would feel — **any tool that needs the branch *name* mid-work breaks
while jj holds a non-empty working copy**; commits become reachable via
bookmarks, and `git checkout <branch>` re-attaches.

`jj op log` confirms the undo surface: `snapshot working copy`, `commit`, `point
bookmark`, `import git refs` — every step is an undoable op.

## 5. Hazards (assigned repo specifics)

- **`.scratch/` (66 GB, ignored):** reproduced inside the scratch clone —
  a 2 MiB `big-2m.bin`, `probe.txt`, and a **real registered git worktree**
  (`git worktree add .scratch/probe-wt`). `jj st` after each: `The working
  copy has no changes`; `jj file list` shows none of them; `git check-ignore`
  confirms `.gitignore:6:.scratch/`. **jj never walks ignored dirs** — the 66 GB
  (including the nested `ca02-wt-r34` worktree's full checkout + its own
  nested `.scratch`) is never hashed or copied.
- **Nested repo/worktree treatment:** an *unignored* nested git repo
  (`out/nestedrepo`, `git init` + commit) is **silently skipped** — `jj st`
  reports no changes and `jj file list` tracks nothing inside it, while
  `git status` shows `?? out/`. jj treats a directory containing `.git` as a
  repo boundary. So a nested worktree is invisible to jj **even if someone
  removes its ignore coverage** — belt-and-suspenders for the `ca02-wt-r34`
  case.
- **Branch fan-in:** `git worktree add` inside the clone made `probe-branch`
  appear in `jj st` output (`probe-branch` listed on the @- line) — jj imports
  new git refs on every command. Harmless, but any lane that creates git
  branches will see them materialize as jj bookmarks.
- **Author vs committer split** (step 4) — the only config actually needed.
- **Detached HEAD** while jj's working copy differs from a bookmark — the only
  git-visible behavior change; keep commits reachable via `jj bookmark` or run
  `jj git` flows only on lanes whose tools don't parse `--abbrev-ref`.
- `snapshot.max-new-file-size` (default 1 MiB): nothing in this repo trips it —
  largest tracked file 1,037,171 B, and every >1 MiB untracked object lives
  under ignored `.scratch/`.

## 6. Cleanup

`git worktree remove --force` on the probe worktree, `rm -rf` on the scratch
clone. Live repo verified untouched after all steps:
`rev-parse --abbrev-ref HEAD` → `main`, `status --porcelain` → 0 lines.
