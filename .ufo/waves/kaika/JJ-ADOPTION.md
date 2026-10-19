# Jujutsu (jj) adoption — kaika W2j findings and plan (2026-10-19)

Operator question: "why don't you set jujutsu as the local git manager? … wouldn't that be an
upgrade?" Answer from 32 probes (`kaika-w2j/*.md`): **yes, an upgrade — in colocated mode, with
four preconditions, rolled out as a measured pilot, not flipped under live rounds.**

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

- **Mistakes become cheap to undo.** Today's two worst incidents — the root-ledger clobber at
  `31baf5c` and four stray fleet-root commits from a failed `cd` — are each one `jj op restore`
  in a jj-mutated repo.
- **Conflicts stop blocking.** Parallel lane work and integration merges record conflicts in
  commits instead of halting a rebase.
- **Nothing uncommitted is lost.** The working copy is a commit; abandoned rounds (kama's unrun
  round-10 plan, game-dev-3d's r107 shards) would have been recoverable state, not loose files.

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

1. **Now (done in this campaign):** evidence only; no live repo touched.
2. **Pilot — next round, two lanes** (`tameshi` `safe`, `mado` `safe-with-config`), after the
   kaika worktrees are merged and retired: colocate with the preconditions, run one craft round
   through jj (`jj commit -m … <paths>`, `jj bookmark set <branch> -r @-`, cite `commit_id`),
   and measure: gates unchanged, identity correct on author and committer, no detached-HEAD
   breakage, op-log recovery demonstrated.
3. **Contract:** the protocol lane makes the contract VCS-neutral (git commit ids as evidence,
   ancestry checks, explicit-path commits) per `connect-protocol.md`; tower keeps git worktrees
   for concurrent writers until jj workspaces can run every lane gate (most gates call git).
4. **Rollout:** remaining repos one at a time, each with its preconditions checked.

Rules once colocated: never `jj undo` / `jj op restore` in a repo another agent is working in;
never rewrite a cited commit; never `jj git push` (no-push standing rule).
