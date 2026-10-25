# Jujutsu (jj) adoption — kaika W2j findings and plan (2026-10-19)

Operator question: "why don't you set jujutsu as the local git manager? … wouldn't that be an
upgrade?" Answer from 32 probes (`kaika-w2j/*.md`): **a useful upgrade for isolated
repositories, not a drop-in replacement for this fleet's concurrent Git worktrees.**

## Evidence

| Finding | Evidence |
|---|---|
| Every probed repo is `safe-with-config` (tameshi `safe`); every lane gate gives identical results before and after `jj git init --colocate` | 21 per-repo probes (`kaika-w2j/<repo>.md`); e.g. kengaku `grader.py` 733/733, mori selftest 66/66 + oracle 28/28, tsukuroi 80/80, game-dev-2d 42,524 files snapshotted in 0.112 s |
| Fleet-root critical check passed: jj honours `.git/info/exclude`, so the 75 GB `.tower/` is never snapshotted; a negative control without the exclude did snapshot it | `fleet-root.md` |
| `.jj/` ignores itself (`.jj/.gitignore: /*`); FIFOs are skipped; files >1 MiB are refused by default | `mado.md`, `audio.md`, `fleet-root.md` |
| `jj commit --config user.*` sets only the committer; the author is stamped when the working-copy commit is created, so lane commits leaked the operator identity until repo config was set first | `mado.md`, `kake.md`, `kumitate.md`, `tabi.md`, `cheatsheet.md` |
| jj 0.45 stores `--repo` config outside the repo (`~/.config/jj/repos/<id>/config.toml`) | `W2jProbeKake` handoff |
| Colocated jj leaves git `HEAD` detached after mutating ops; tools that read the branch name break (souji's unpushed check) | `souji.md`, `kasegi.md`, `tsukuroi.md` |
| jj 0.45.1 does not support git linked worktrees in a colocated repo; export can detach a sibling worktree's HEAD | `docs-colocation.md`, `cheatsheet.md` |
| The op log is repository-wide: `jj undo` / `jj op restore` can revert another agent's work in the same repo | `docs-concurrency.md`, `tsukuroi.md` |
| A first snapshot sweeps untracked-but-not-ignored files into `@` (game-dev-3d 79, lore 26, kama 2 files today) | `game-dev-3d.md`, `kama.md`, `sentinel.md` |
| kimi-shokunin is a shallow clone; unshallowing a colocated repo is unsupported | `kimi-shokunin.md` |

## Why it is an upgrade here

- **Recorded jj operations are recoverable.** `jj op restore` can restore a recorded prior
  jj state. It cannot retroactively recover an unsnapshotted edit or turn the historical
  Git-only ledger clobber into a recorded jj operation.
- **Conflicts are first-class state.** Jj can record a conflicting rebase rather than
  stopping with Git's rebase workflow; existing Git-only gates still need compatibility checks.
- **Snapshots reduce loose working-copy risk.** Non-ignored files captured by a jj snapshot
  become recoverable commit state; ignored, refused or never-snapshotted files do not.

## Preconditions (per repo, before its first jj command)

1. No active git linked worktrees (`git worktree list` shows only the main checkout).
2. Untracked files dispositioned (committed, ignored, or quarantined).
3. Identity first: `jj config set --repo user.name <id>-shokunin` and
   `jj config set --repo user.email <id>@shokunin.local` (fleet root: `protocol-shokunin`).
4. Fleet root: move `.tower/` and `local/` from `.git/info/exclude` into the versioned
   `.gitignore`. kimi-shokunin: `git fetch --unshallow` first.

Recommended: `revset-aliases."immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"`
so commits a report has cited cannot be rewritten; git commit ids stay the evidence currency.

## Plan

1. **Evidence:** scratch probes completed before live adoption; no live source history was rewritten.
2. **Pilot initialized:** `mado` and `tameshi` were clean, their kaika branches merged and
   linked worktrees retired before `jj git init --colocate`. Repo-scoped lane identities and
   immutable bookmarked ancestry are configured. Empty working copies contain no source changes.
   Mado's gate remains 269/269 and tameshi's 80/80 before/after; author and committer both match
   the lane identity. Receipt: `jj-live-pilot.txt`. No live content commit or undo was attempted.
   Future craft work must advance the intended bookmark explicitly and cite the stable commit ID.
3. **Contract:** the protocol lane makes the contract VCS-neutral (git commit ids as evidence,
   ancestry checks, explicit-path commits) per `connect-protocol.md`; tower keeps git worktrees
   for concurrent writers until jj workspaces can run every lane gate (most gates call git).
4. **Rollout:** remaining repos one at a time, each with its preconditions checked.

Rules once colocated: never `jj undo` / `jj op restore` in a repo another agent is working in;
never rewrite a cited commit; never `jj git push` (no-push standing rule).
