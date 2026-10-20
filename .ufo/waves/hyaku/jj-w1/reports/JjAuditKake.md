# JjAuditKake — lane `kake` git surface under jj colocation

Seat: JjAuditKake-2 (read-only reviewer, leaf). Date: 2026-10-20.
Target repo: `/home/vgpnk/Projects/shokunin/kake-shokunin` (branch `master`, HEAD `7c61c8cc`, `master...origin/master` 0/0).
Tooling: jj 0.45.1, git 2.56.0. No installs were needed; nothing was installed or upgraded.

## Scope actually present (and not)

- `tools/` — **absent**. `verifiers/` — **absent**. No `*.sh`, `*.py`, `*.mjs`, `*.js`, `Makefile` at the repo root (root holds only `.md` files and `.gitignore`).
- `find . -path ./.git -prune -o -path ./.jj -prune -o -path ./corpus -prune -o -path ./.ufo -prune -o -type f \( -name '*.sh' -o -name '*.py' -o -name '*.mjs' -o -name '*.js' -o -name 'Makefile' \) -print` → only:
  `./scripts/corpus-contract.mjs`, `./scripts/freshness-sweep.mjs`, `./scripts/probe-delta.mjs`.
- `.jj` — absent (lane not yet colocated at audit time).
- Extra executable tooling named by `SKILL.md` but living outside `scripts/` was inspected separately and is tabled in the appendix:
  `.ufo/round-20/replay-proof.mjs`, `.ufo/round-20/resume/confinement-mutants.mjs`, `.ufo/waves/round-21/{measure,anchor-census}.mjs`.
  `.ufo/round-20/resume/old-strings.sh` contains no git call. `.ufo/waves/round-21/replay-proof.mjs` contains no git call (only `spawnSync` of gate CLIs).

## Findings (observed, command + excerpt)

### F1. The entire in-scope git surface is six commands in two `execFileSync` wrappers — zero writes

`grep -n -E "git|execFile|spawn" scripts/*.mjs` yields exactly two `git` spawners:

```
scripts/freshness-sweep.mjs:699:  const g = (args) => execFileSync('git', ['-C', out.dir, ...args], {...});
scripts/freshness-sweep.mjs:852:  const g = (args) => execFileSync('git', ['-C', pins.pq2Dir, ...args], {...});
```

Their only argv uses are the same triple:

```
:700  g(['ls-remote', 'origin', 'main'])
:701  g(['rev-parse', 'HEAD'])
:702  g(['rev-list', '--count', 'origin/main..HEAD'])
:853  g(['ls-remote', 'origin', 'main'])
:854  g(['rev-parse', 'HEAD'])
:855  g(['rev-list', '--count', 'origin/main..HEAD'])
```

`corpus-contract.mjs` and `probe-delta.mjs` have **zero** git invocations (`grep -c '\bgit\b'` → 0 and 0). No `add|commit|stash|checkout|reset|rebase|push|pull|merge|clean|tag`, no `diff --cached`, `ls-files -s` or `update-index` appears in any in-scope file. The lane's own history writes happen outside its tooling (L1/closure via the wave's helper), so this audit has **no class B or C call site**.

Targets are pinned source repos, not the lane repo:
`pins.plazirSourceDir = /home/vgpnk/Projects/plazir-15-site`, `pins.pq2Dir = /home/vgpnk/Projects/ds4cc-marketplace`
(`pq2Dir` comes from `DEFAULT_PINS` at `scripts/freshness-sweep.mjs:82`, merged over the JSON at `:203`; `"pq2Dir"` does not appear in `corpus/knowledge/freshness-pins.json` — only `pq2Remote`/`pq2Unpushed` do).

### F2. `--offline` correctly suppresses both wrappers (no hidden network)

```
:695  if (offline) gate.verdict = 'skipped(offline)';            // checkPlazir returns before `g`
:771  out.pq2 = { dir: pins.pq2Dir, verdict: 'skipped(offline)' };
```
`git ls-remote` is the only network-reaching git command and it is unreachable under `--offline`.

### F3. Under colocation git HEAD is **detached at `@-`**; the branch bookmark is separate

Sandbox `/fast/scratch/jj-wave/JjAuditKake-2/t1/work` (clone of a sandbox bare `origin`, then `jj git init --colocate`), after `jj commit -m c2 -- a.txt`:

```
symbolic-ref: DETACHED
git HEAD:     2d68f82cb539...
branch main:  4d7e0e0e21d7...
jj @  :       a77440853b83
jj @- :       2d68f82cb539
```

After `jj new -m wip` and after `jj edit @-`, HEAD tracked `@-` every time and stayed detached. `git rev-parse HEAD` resolves fine; only `git symbolic-ref` / `--abbrev-ref` would break (the lane has none).

### F4. The helper's commit→bookmark-move→push flow keeps the gate triple correct

Same sandbox, `jj bookmark move main --to @-` then `jj git push -b main` (after `jj bookmark track main@origin`, which the helper's init performs):

```
Changes to push to origin:
  bookmark: main [move forward from 4d7e0e0e21d7 to 2d68f82cb539]
origin/main: 2d68f82cb539...        # jj imports the pushed ref into git
ls-remote:   2d68f82cb539...
unpushed via HEAD: 0
```

Pre-push the count was `1` (correct: one committed, unpushed commit). So for the exact flow the wave prescribes, `rev-list --count origin/main..HEAD` returns the right number, and a post-push lane reads `0`.

### F5. **Failure: an off-branch working copy makes `origin/main..HEAD` over-count**

`jj new 4d7e0e0e -m side` + `jj commit -m side-commit -- side.txt` (working copy parked off `main`; `main` fully pushed):

```
main=2d68f82cb539...
HEAD=7ca2e68 (@- = 7ca2e68)
count origin/main..HEAD = 1
count origin/main..main = 0
```

Second measurement (`work2`, an unpushed orphan chain off the branch tip):

```
git HEAD-count:   3
git branch-count: 1
jj native (main@origin..main): 1
```

The gate would report `unpushed=3` while the branch is 1 behind. For the plazir arm that is `UNPUSHED-CHANGED` → `driftReasons` → `§armed ok=false` → sweep exit 1: a **false drift alarm** from a purely local `jj edit`/`jj new <rev>`.

### F6. Unborn HEAD fails closed, not silently

`jj new -m rooted 'root()'` in `work3`:

```
git HEAD: fatal: ambiguous argument 'HEAD': unknown revision ...
symbolic: refs/jj/root
rev-list: fatal: ambiguous argument 'origin/main..HEAD': unknown revision ...
```
Both commands throw → the wrapper's `catch` sets `verdict='ANOMALY'` / pushes `plazir-gate-anomaly`. Loud, not a false pass.

### F7. The six gate commands never touch `.git/index`

In the colocated sandbox, running the exact six commands then hashing the index:

```
before=fe084755ba1f...5c35
after =fe084755ba1f...5c35
INDEX UNCHANGED
```
`git ls-files` (appendix call site) equals `git ls-tree -r --name-only HEAD` both in the sandbox (`a.txt knowledge.md side.txt`) and on the live lane repo (`ls-files: 254`, `ls-tree HEAD: 254`). jj's index reset therefore does not corrupt the read-only surface.

### F8. Pushed commits are immutable; a forced rewrite does not kill the pinned hash

`jj describe -r <pushed main tip> -m rewritten`:

```
Hint: This operation would rewrite 1 immutable commits.
```
With `--ignore-immutable` the rewrite succeeds, but the old git sha still resolves (`git show <old>:a.txt` → `one`) because `refs/remotes/origin/main` still points at it, and it survives `jj util gc --expire=now`. An unpushed rewritten commit likewise survived `jj util gc --expire=now`. Bounded claim: a git-hash pin survives while the object is reachable or still in git's odb; only `git gc --prune` of an unreachable object would kill it (not exercised).

### F9. Hooks and attributes: nothing to bypass today

```
$ ls .git/hooks          → 14 files, all *.sample
$ find .git/hooks -maxdepth 1 -type f ! -name '*.sample'   → (none)
$ git config --get core.hooksPath                          → exit 1
$ git config --global/--system --get core.hooksPath        → exit 1 / exit 1
$ git config --get init.templateDir                        → exit 1
```
- No active hook, no `core.hooksPath` at any scope.
- **No `.gitattributes` anywhere** in the worktree (`find . -name .gitattributes -not -path './.git/*'` → empty), never in history (`git log --all -- .gitattributes` → empty), no `.git/info/attributes`, no `core.attributesFile`, no `core.autocrlf`, no `core.eol`.
- A global LFS filter exists (`file:/home/vgpnk/.config/git/config`: `filter.lfs.clean/smudge/process`, `required=true`, git-lfs 3.8.0) but **no attribute activates it**, and `git grep -l 'git-lfs.github.com/spec/v1' HEAD` finds no pointer files.
- jj has its own EOL mechanism, `working-copy.eol-conversion = "none"` (default; jj's own help maps it to `core.autocrlf=false`). Any future `text`/`eol` attribute the lane adds would be ignored by jj's checkout/commit path — irrelevant today because the repo declares none.

### F10. Both git arms are currently non-evaluable on this host

```
$ ls -d /home/vgpnk/Projects/plazir-15-site /home/vgpnk/Projects/ds4cc-marketplace
ABSENT /home/vgpnk/Projects/plazir-15-site
ABSENT /home/vgpnk/Projects/ds4cc-marketplace
```
`git -C <absent>` throws → `PQ-2 ANOMALY` / `plazir-gate-anomaly`. Fail-closed, but a "push gate green" claim today would be false: the check does not run. This matches the r18 re-census annotations in `SKILL.md`.

### F11. Appendix call sites are all read-only and revision-addressed

| site | command | note |
|---|---|---|
| `.ufo/round-20/replay-proof.mjs:25` | `git show 20d1311…:scripts/freshness-sweep.mjs` (`cwd=root`) | pin is an ancestor of `master` (`git merge-base --is-ancestor` → yes); `git show` yields 80556 bytes |
| `.ufo/round-20/resume/confinement-mutants.mjs:86` | `git -C <lane-root> show cb807bc…:scripts/freshness-sweep.mjs` | `L` resolves to the live lane repo; `cb807bc` is an ancestor of `master` |
| `.ufo/waves/round-21/measure.mjs:182` | `git -C <root> rev-parse --verify <revision>^{commit}` | explicit revision |
| `.ufo/waves/round-21/measure.mjs:190` | `git -C <root> ls-tree -r --name-only <resolved> -- knowledge lessons` | commit tree, not index |
| `.ufo/waves/round-21/anchor-census.mjs:473` | `git rev-parse --verify --quiet <base>^{commit}` (`cwd=root`) | explicit revision |
| `.ufo/waves/round-21/anchor-census.mjs:475` | `git ls-files -z` (`cwd=root`) | only index reader in the repo; equals `ls-tree HEAD` (F7) |
| `.ufo/waves/round-21/anchor-census.mjs:98` | `git show <base>:<relPath>` (`cwd=root`) | explicit revision |

None of these resolve a branch name, an upstream, or `HEAD`; none mutate.

## Classified table — in-scope (`scripts/`)

| file:line | command | class | risk under jj colocation | jj-safe replacement |
|---|---|---|---|---|
| `scripts/freshness-sweep.mjs:700` | `git -C <plazirSourceDir> ls-remote origin main` | D (remote-ref read) | none: no HEAD/index dependency; needs network + `origin`; skipped under `--offline` | keep as is |
| `scripts/freshness-sweep.mjs:701` | `git -C <plazirSourceDir> rev-parse HEAD` | D | resolves a detached HEAD fine (F3); fails only on unborn HEAD → gate ANOMALY (F6); the recorded `head` is `@-`, **not** the branch tip | `git rev-parse refs/heads/main` (or `jj log -r main --no-graph -T commit_id`) |
| `scripts/freshness-sweep.mjs:702` | `git -C <plazirSourceDir> rev-list --count origin/main..HEAD` | **A** (HEAD used as the branch tip) | correct in the helper flow (F4), **over-counts when the working copy is off-branch** (F5: 1 vs 0, 3 vs 1) → false `plazir-unpushed-changed` drift | `jj log -r 'main@origin..main' --no-graph -T 'commit_id ++ "\n"' \| wc -l` (verified) |
| `scripts/freshness-sweep.mjs:853` | `git -C <pq2Dir> ls-remote origin main` | D (remote-ref read) | none (same as :700) | keep as is |
| `scripts/freshness-sweep.mjs:854` | `git -C <pq2Dir> rev-parse HEAD` | D | same as :701; `pq2.head` is reported in `--json` output and would be mistaken for the branch head | `git rev-parse refs/heads/main` |
| `scripts/freshness-sweep.mjs:855` | `git -C <pq2Dir> rev-list --count origin/main..HEAD` | **A** | same as :702; PQ-2 only annotates (`note`), it does not fail the verdict, so this is a reporting-accuracy risk here | same revset replacement |

**Counts (in scope): A = 2 · B = 0 · C = 0 · D = 4 (2 remote-ref reads + 2 HEAD reads). Total 6 commands, 0 mutating.**

Appendix (named tooling outside `scripts/`, `.ufo/…`): **A = 0 · B = 0 · C = 0 · D = 7** — `git show` ×2, `rev-parse --verify` ×2, `ls-tree` ×1, `ls-files` ×1 (plain, index read), `show <rev>:path` ×1.

Combined: 13 git commands across the lane, **zero** that write history, index or worktree.

## Top three risks

1. **Class-A HEAD-as-branch over-count → false drift.** `origin/main..HEAD` is the only call site whose correctness depends on jj placing the working copy on the branch tip. Any `jj edit <rev>` / `jj new <rev>` in a colocated gate target inflates `unpushed`, flips the plazir arm to `UNPUSHED-CHANGED`, and fails `§armed` (exit 1). Measured: `1` vs true `0`; `3` vs true `1`. Replace with the branch-scoped jj revset or `origin/main..<branch>`.
2. **The two git arms cannot evaluate on this host.** Both pinned target dirs are absent, so every git call throws and PQ-2/PQ-14 report `ANOMALY`. A lane report claiming the push gate is green would be reporting an unrun check. The wave must not read `ANOMALY` as "unchanged" and must not read an `--offline` `skipped(offline)` as a pass either.
3. **`head` is now `@-`, not the branch tip — a citation hazard.** Under colocation `git rev-parse HEAD` returns the working copy's parent (F3), and that value is written into `--json` (`pq2.head`, `gate.head`). The protocol says a report may only cite a hash that is committed *and pushed* and remains an ancestor of the branch. A `head` captured mid-`jj new`/`jj edit` is neither. Prefer citing `git rev-parse refs/heads/main` or the hash the helper prints after push; never quote `pq2.head` as "the landed commit".

## [INFERENCE]

- [INFERENCE] The gate targets are non-lane source repos that the current wave does not colocate, so risks 1 and 3 are latent, not live. They become live the moment `~/Projects/plazir-15-site` or `~/Projects/ds4cc-marketplace` is `jj git init --colocate`d, or if the same triple is copied onto lane repos.
- [INFERENCE] Because jj exports refs into git, `origin/main` in a colocated repo is a reliable stand-in for the pushed branch state; F4/F8 show it updating on push and retaining rewritten-away shas.
- [INFERENCE] `jj util gc` alone does not prune git's object db; a pinned sha dies only if it is simultaneously unreachable *and* git prunes it. The helper's no-amend rule keeps cited hashes reachable via `origin/<branch>`, so pins like `pq2Remote`, `plazirRemote`, `20d1311…`, `cb807bc…` are stable under the prescribed flow.
- [INFERENCE] `freshness-sweep.mjs --selftest` spawns child runs of the script; whether those children reach `§armed` depends on their section args. I did not execute the selftest (it is a gate, not mine to run, and it writes only temp fixtures). The git classification above does not depend on it: the wrappers are the same code path regardless of caller.

## Recommendations

1. Replace both `rev-list --count origin/main..HEAD` calls with `jj log -r '<branch>@origin..<branch>' --no-graph -T 'commit_id ++ "\n"'` counted in JS, with a `git rev-list --count origin/main..<branch>` fallback for non-colocated targets. Keep `rev-parse HEAD` only as an informational field and rename it (`worktree_parent`) or switch to `refs/heads/<branch>`.
2. Add a guard before each wrapper: if `<dir>/.jj` exists, take the jj path; otherwise keep the git path. That makes the gate colocation-aware without requiring jj for the source repos.
3. Treat `ANOMALY` from a missing `-C` dir as `could-not-evaluate`, not as drift, so the exit map matches the gate's own contract (`2`/`64` for could-not-evaluate vs `1` for failed). Today both conditions collapse into the `1` bucket via `driftVerdicts`.
4. Do not add hooks or `.gitattributes` to this lane while it is colocated unless something reads them through git: jj runs neither, and `working-copy.eol-conversion = "none"` means EOL attributes would be silently ignored.

## Verification gaps

- I did not run `node scripts/freshness-sweep.mjs`, its `--selftest`, `corpus-contract.mjs`, `probe-delta.mjs`, or either `replay-proof.mjs` (gates are not mine to run; the pin targets are absent anyway). All git-call claims are static reads of the source plus faithful argv replication in a sandbox.
- `git gc --prune=now` of an unreachable rewritten commit was not exercised; the F8 claim is bounded to `jj util gc`.
- Remote behaviour was tested against a local bare repo only; no real remote was contacted or pushed.

## Sandbox

Retained because it preserves the F5 false-positive state (and F3/F6 rewrite states), as allowed for cited failures:
`/fast/scratch/jj-wave/JjAuditKake-2/` — `t1/origin.git` (bare), `t1/work` (forced rewrite + off-branch), `t1/work2` (unpushed orphan chain), `t1/work3` (unborn HEAD). Total 1.8 MB. No live repo was written, fetched, staged or jj'd.
