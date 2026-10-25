# Fleet identity and tree audit (advisory data)

Seat: `FleetIdentityAudit`. Read-only. Not a judge verdict, receipt, or admission.

Observed: 2026-10-14T21:18:11-0300, rechecked `git status -sb` immediately after.
Identity contract used (re-derived, not taken from the lesson files): author and committer are both `<lane>-shokunin <lane>@shokunin.local`, the commit is a single-parent commit on that lane's own git toplevel, and its delta paths stay inside that toplevel and do not include `plans/`. Operator identities observed on older commits in these same repos (`Joao Pedro Veiga <jpveigao10@gmail.com>`, `ci <ci@local>`, `shokunin <shokunin@local>`, `aggregator-shokunin <aggregator@shokunin.local>`) are not lane identity for these six.

## Verdict

No violation. All six named commits are HEAD of their own repos, carry lane author and committer, touch only that lane's files, and leave a porcelain tree whose only untracked path is `plans/`.

| Lane | Commit | HEAD equals named SHA | Author = committer | Delta paths | Porcelain besides `plans/` |
|---|---|---|---|---|---|
| kagi | `5b0d4b784624a15506d3c85c77c3ae619e07467f` | yes | `kagi-shokunin <kagi@shokunin.local>` | `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-19-recensus.md` | none |
| kake | `59948314e9af5dd6ef81894fc1c422b353f10938` | yes | `kake-shokunin <kake@shokunin.local>` | those three plus `scripts/freshness-sweep.mjs` | none |
| kama | `84a81304d7b0c77c84fe495f3bb728e8729faaff` | yes | `kama-shokunin <kama@shokunin.local>` | `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-4-recensus.md` | none |
| kasegi | `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` | yes | `kasegi-shokunin <kasegi@shokunin.local>` | `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-20-recensus.md` | none |
| kengaku | `7153e671b1581a4b705583656883b6af158257df` | yes | `kengaku-shokunin <kengaku@shokunin.local>` | `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-16-recensus.md` | none |
| kotoba | `b0c7cb2e248bccf692cf10e4d3c394e09944e83d` | yes | `kotoba-shokunin <kotoba@shokunin.local>` | those three plus `verifiers/verify_harness_claims.py` | none |

Each commit has one parent (the pre-repair HEAD in `.ufo/waves/shokunin12h-20261014-p1-repair/baselines.json`). AuthorDate and CommitDate are both `Wed Oct 14 21:15:36 2026 -0300` (`1792023336 -0300`). Same clock, different identities. No `gpgsig`, no `Co-authored-by`, no extra body. Not merges.

Each repo is its own toplevel (`git rev-parse --git-common-dir` → `.git`, not a linked worktree). Parent `/home/vgpnk/Projects/shokunin` gitignores `*-shokunin/` (`.gitignore:1`) and does not track these directories (`git ls-files --error-unmatch` exit 1). A parent index cannot have swept these lane files, and a lane index cannot have swept a sibling repo.

`plans/` is untracked, not ignored, and absent from each commit tree (`git ls-tree -r --name-only <sha> plans` empty; `git ls-files plans` empty). That is the allowed exception, and it is evidence the commit was not `git add -A` / `git commit -a`.

## Claim-by-claim

Lane lessons do not state author, committer, or the commit hash. Agreement below is with the wave's named SHAs and with the repair deltas the lessons do state. Silence on identity is a verification gap, not a false claim.

| Claim | Verdict | Evidence |
|---|---|---|
| Named SHA exists and is that lane's HEAD | agree, all six | `git rev-parse HEAD` exit 0 equals the named SHA; `git rev-parse <sha>^{commit}` exit 0; `git merge-base --is-ancestor <sha> HEAD` exit 0 |
| Author and committer are lane identity, not operator identity | agree, all six | `git show --format=fuller` Author and Commit lines above. No counterexample |
| Pathspec limited to that lane's files; no sibling path | agree, all six | `git diff-tree --raw` paths listed above. Every mode is `100644` or preserved `100755`. No `160000` gitlink, no `../`, no other lane prefix, no `plans/` |
| kake lesson: landed change is one file, `scripts/freshness-sweep.mjs` | agree | Only non-record path in `59948314`. Record files in the same commit are the round log, scorecard, and lesson, still inside `kake-shokunin` |
| kotoba lesson: landed change is one file, 2 lines, `verifiers/verify_harness_claims.py` | agree | Only non-record path in `b0c7cb2`. `git show --stat` on that file: 2 insertions, 2 deletions |
| Working tree clean apart from untracked `plans/` | agree, all six | `git diff --exit-code` exit 0; `git diff --cached --exit-code` exit 0; `git status --porcelain=v1 -uall` is exactly one `?? plans/wwkd-round-<N>-recensus.md`; `git ls-files -v` has no skip-worktree (`S`) and no assume-unchanged (lowercase) flag; `core.sparseCheckout` unset (exit 1) |
| `plans/` was not committed | agree, all six | `git ls-tree` / `git ls-files` empty, as above |

Untracked `plans/` files observed:

- `kagi-shokunin/plans/wwkd-round-19-recensus.md`
- `kake-shokunin/plans/wwkd-round-19-recensus.md`
- `kama-shokunin/plans/wwkd-round-4-recensus.md`
- `kasegi-shokunin/plans/wwkd-round-20-recensus.md`
- `kengaku-shokunin/plans/wwkd-round-16-recensus.md`
- `kotoba-shokunin/plans/wwkd-round-19-recensus.md`

`git status -sb` collapses each of those to `?? plans/` and also reports `## master...origin/master [ahead 1]`. Ahead-of-origin is not dirt and was not treated as a violation. Push was out of scope.

## Commands and exit codes

Run from each `/home/vgpnk/Projects/shokunin/<lane>-shokunin`. Exit codes were identical across the six unless noted.

| Command | Exit | Result |
|---|---|---|
| `git rev-parse --show-toplevel` | 0 | that lane's directory |
| `git rev-parse --git-dir` / `--git-common-dir` | 0 | `.git` / `.git` |
| `git rev-parse --abbrev-ref HEAD` | 0 | `master` |
| `git rev-parse HEAD` | 0 | named SHA |
| `git rev-parse <sha>^{commit}` | 0 | same SHA |
| `git merge-base --is-ancestor <sha> HEAD` | 0 | empty |
| `git config --local --get user.name` | 1 | unset |
| `git config --local --get user.email` | 1 | unset |
| `git config --get core.sparseCheckout` | 1 | unset |
| `git diff --exit-code` | 0 | empty |
| `git diff --cached --exit-code` | 0 | empty |
| `git status --porcelain=v1 -uall` | 0 | only `?? plans/wwkd-round-…md` |
| `git diff-tree --no-commit-id --name-status -r -m <sha>` | 0 | paths in the table |
| `git show --format=fuller --stat --no-renames <sha>` | 0 | identity and stat above |
| `git status -sb` | 0 | `ahead 1`, `?? plans/` |
| `git rev-parse --abbrev-ref --symbolic-full-name @{u}` | 0 | `origin/master` |
| `git ls-tree -r --name-only <sha> plans` | 0 | empty |
| `git ls-files plans` | 0 | empty |

Parent repo, exit 0 ignore / exit 1 not tracked, all six:

- `git -C /home/vgpnk/Projects/shokunin check-ignore -v <lane>-shokunin` → `.gitignore:1:*-shokunin/`
- `git -C /home/vgpnk/Projects/shokunin ls-files --error-unmatch <lane>-shokunin` → exit 1

## Not violations (so they are not dropped)

Ignored residue does not appear in `git status --porcelain` without `--ignored`. It is not the allowed `plans/` exception, and it is not a dirty tracked path.

- kama: `!! registry/history/.lock`, `!! registry/history/20261014T124232Z.json`, `!! registry/history/20261014T124525Z.json`. `git check-ignore -v` exit 0, rule `registry/history/.gitignore:2:*.json` and `:3:.lock`. The two JSON names are the round-3 snapshot ids already written in `LOG.md` (12:42Z and 12:45Z), before this commit (21:15:36-0300).
- kotoba: `!! verifiers/__pycache__/verify_surfaces.cpython-314.pyc`. `git check-ignore -v` exit 0, rule `.gitignore:1:__pycache__/`.

No other lane printed `!!` lines.

## Counterexamples

None. No operator-identity author or committer on these six SHAs. No path outside the lane toplevel. No swept `plans/`. No tracked or untracked dirt outside `plans/`.

## Named debt

None on this axis.

Residual, not a failed check:

- Local `user.name` / `user.email` are unset in all six (exit 1). These commit objects still carry lane identity, which is what the check requires. A later commit that omits `-c user.name` / `-c user.email` would not. Owner: each lane. Unblock: set the local identity once, or keep passing `-c` at commit time. Not a reason to rewrite `5b0d4b7`, `5994831`, `84a8130`, `a5cbf77`, `7153e67`, or `b0c7cb2`.
- Lessons do not record the SHA or the identity string. A reader of the lesson alone cannot re-derive this audit. Owner: the lane record, not this commit. Unblock: not required to make these objects lane-identified.

## Axes

- Freshness: measurement is the live HEAD, taken about three minutes after the commit timestamp. The named SHAs are current, not historical pins.
- Operability: each tree is on `master`, diff-clean, and the identity is in the commit object rather than only in an unset local config.
- Calibration: kake's "one file" and kotoba's "one file, 2 lines" match the non-record deltas. The lessons do not over-claim a hash or an identity they do not state.
- Adjacency: no sibling path in any delta; parent repo does not contain these checkouts as tracked files.
