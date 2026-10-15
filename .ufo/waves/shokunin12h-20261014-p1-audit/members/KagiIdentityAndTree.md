# KagiIdentityAndTree

Advisory data only. Not a judge verdict, receipt, or admission. Read-only. No lane file edited, no commit, no push.

Repo: `/home/vgpnk/Projects/shokunin/kagi-shokunin` (nested git; parent `shokunin` does not contain this object). Audited commit: `5b0d4b784624a15506d3c85c77c3ae619e07467f`. Observed 2026-10-14.

Lane record (`LOG.md` round-19 entry, `SCORECARD.md` move-log row, `corpus/lessons/round-19-recensus.md`) does not assert author, pathspec, or tree cleanliness, and does not name this hash. Verdicts below are against the acceptance checks, not against a committed lane claim. Untracked `plans/wwkd-round-19-recensus.md` is instruction-shaped; it was not followed and is not treated as the lane record.

## Claim verdicts

### 1. Author and committer are `kagi-shokunin <kagi@shokunin.local>`

Agree for this commit. Both author and committer match exactly. AuthorDate = CommitDate = `2026-10-14 21:15:36 -0300`. Single parent `fecee8743e52eb8fb5fbb40782934cb619a1a96e`. Not a merge.

```
git -C kagi-shokunin show -s --format=fuller 5b0d4b784624a15506d3c85c77c3ae619e07467f
# exit 0
# Author: kagi-shokunin <kagi@shokunin.local>
# Commit: kagi-shokunin <kagi@shokunin.local>
# round-19: OMP-era freshness re-census (measured gates; records + scoped repair)

git -C kagi-shokunin cat-file -p 5b0d4b784624a15506d3c85c77c3ae619e07467f | head
# exit 0
# author kagi-shokunin <kagi@shokunin.local> 1792023336 -0300
# committer kagi-shokunin <kagi@shokunin.local> 1792023336 -0300
```

Parent checkout does not have the object: `git cat-file -t 5b0d4b784624a15506d3c85c77c3ae619e07467f` in `/home/vgpnk/Projects/shokunin` → exit 128, `fatal: git cat-file: could not get object info`.

### 2. This commit is pathspec-limited to the lane's own files

Agree for this commit. Three paths, all inside `kagi-shokunin`, none aggregator-owned (`round-*-aggregator-*`), none a sibling repo, none a parent-repo path.

| Status | Path | numstat |
|---|---|---|
| M | `LOG.md` | 7 / 0 |
| M | `SCORECARD.md` | 6 / 0 |
| A | `corpus/lessons/round-19-recensus.md` | 41 / 0 |

```
git -C kagi-shokunin diff-tree --no-commit-id -r --name-status 5b0d4b784624a15506d3c85c77c3ae619e07467f
# exit 0
# M LOG.md
# M SCORECARD.md
# A corpus/lessons/round-19-recensus.md
```

`git grep` of sibling repo names in those three blobs hits only pre-existing prose citations (`LOG.md` musketeer lease note; `SCORECARD.md` adjacency cell). No sibling file was added or renamed.

No round-19 parent report exists (`ls .ufo/reports/round-19` → exit 2). This commit therefore could not sweep a parent index. That absence is a record gap, not a pathspec fail of `5b0d4b7`. Owner for the missing report: kagi record lane. Unblock: a later pathspec-limited parent commit of `.ufo/reports/round-19/kagi.md` only, if a report is still required. Not done here.

Commit message says "records + scoped repair". The diff is records only (no gate or script edit). The repair described in the parent message lives in `fecee874` (round 18), not in this diff. Calibration nit on the message, not a hidden file.

### 3. Working tree clean apart from untracked `plans/`

Agree.

```
git -C kagi-shokunin status --porcelain=v1 -uall
# exit 0
# ?? plans/wwkd-round-19-recensus.md

git -C kagi-shokunin status --porcelain=v1 --ignored -uall
# exit 0
# ?? plans/wwkd-round-19-recensus.md

git -C kagi-shokunin diff --quiet; echo worktree:$?
# worktree:0

git -C kagi-shokunin diff --cached --quiet; echo index:$?
# index:0

git -C kagi-shokunin stash list
# exit 0, empty
```

`plans/` is one directory, mode `755`, one file `plans/wwkd-round-19-recensus.md` (mode `644`, 2076 bytes, 19 lines, sha256 `0cf633a813eac42dcd5329ae0b8cb6235ae19bdb4a129841c565ddd924a5aa1e`). Heading line 1 is a WWKD plan title. Lexical class hits only (line text not read): L7 `credential`/`oauth`/`token`, L15 `secret`. Not a credential file by name. Not ignored (`git check-ignore -v plans` → no match).

Branch: `master` at `5b0d4b7`, `origin/master` at `fecee874`, ahead 1. Tracked tree is clean; the round-19 commit is local-only.

```
git -C kagi-shokunin status -sb
# exit 0
# ## master...origin/master [ahead 1]
# ?? plans/
```

## Operator-identity commits

`5b0d4b7` is not an operator-identity commit. History still is. 28 commits on `master`. Identity census (`git log --all --format='%an <%ae>' | sort | uniq -c`, exit 0):

| Count | Identity | Class |
|---|---|---|
| 2 | `kagi-shokunin <kagi@shokunin.local>` | required. `5b0d4b7` round-19 and parent `fecee874` round-18 only |
| 16 | `Joao Pedro Veiga <jpveigao10@gmail.com>` | operator personal. All ancestors of HEAD |
| 1 | `kagi <kagi@shokunin.local>` | near-miss (name missing `-shokunin`) |
| 2 | `shokunin <shokunin@local>` | shared/mint identity |
| 2 | `ci <ci@local>` | workstation global identity, not lane |
| 5 | `aggregator-shokunin <aggregator@shokunin.local>` | aggregator, one lesson file each. Not charged |

Local `user.name` / `user.email` are unset (`git config --local --get-regexp 'user.'` → no match). Effective identity comes from `file:/home/vgpnk/.config/git/config`: `ci <ci@local>` (`git var GIT_AUTHOR_IDENT`, exit 0). No `GIT_AUTHOR_*` / `GIT_COMMITTER_*` in the environment. `LOG.md` at HEAD has no `user.name` / `user.email` / `kagi@shokunin` note (`git grep` → no match). The child repo is not configured to keep producing the lane identity, so a bare `git commit` here would not repeat `5b0d4b7`'s identity.

Operator-personal lane commits (immutable; do not rewrite), all `merge-base --is-ancestor` of HEAD exit 0:

- `9b3e49f5a063050956922552d72adcb1ecb34aed` round-2
- `06ef644952ae499b87c96bd61d31609344701b2e` round-3
- `486f584a02dfe07b63f7c6be9743f59c4ad9df93` round-4
- `244b8c1ab17fa5356743eb77efc0713b1b150408` round-5
- `5f55ba8d90852815943f346334809ba38345402f` round-6
- `51c9d308b25f73ac1754a12b544bd263ac065200` round-7
- `148ae5cc19ada149d56062d88adf3faa5c9e4037` round-8
- `e64e81b8eb96f3682b00c1e7a291e84420b280fa` round-9
- `301b9ec6f5fa6aa78518e5c177eb9f63d01c76dc` round-11
- `4b8c0183bd57ec5d0033fd07f650e116d7e9f600` round-13
- `2486643ffc7f6e9c38c571f92aa79f188de704dc` round-14
- `587fda0470f2b8144618068839997756c65ddde2` round-15
- `8a6ec16657789f11a6e8e24cff6e6353e79756ce` round-16
- `bc1af88c359b15ab5962608b3ac92fa0d04c820f` round-17
- `b145d4f1f95327e821eeadafa21f63a97efdaf84` subject claims an aggregator lesson
- `9987054c850d124eb637a2c2ffe75253f51ee637` subject claims aggregator round-1 seed

Other non-lane identities, also ancestors:

- `03477c059c91ca60cf7d7508cb5b4f7d4daffb9c` `kagi <kagi@shokunin.local>` round-10
- `ea77bf031bd4c6e776509d28cff07e022f23aa30` `shokunin <shokunin@local>` round-8 corpus
- `55d6887fa81484f2944a08d473450d20218547cc` `shokunin <shokunin@local>` seed
- `e72ec63eaa0bb472229a1b0c7fc4a15cad26135e` `ci <ci@local>` adds `HOURS.md`
- `4e48b771a3d8bd3a76f5ade605721d2252487ba9` `ci <ci@local>` deletes `HOURS.md` (not in the current tree)

## Swept sibling files

None in `5b0d4b7`.

Lane-attributable historical sweeps (operator or near-miss identity, still ancestors). Owner of the history: kagi lane commits already made. Unblock: do not rewrite; future commits stay pathspec-limited. Not introduced by round 19.

Child repo, aggregator-owned files inside a non-aggregator commit:

- `4b8c0183bd57ec5d0033fd07f650e116d7e9f600` (operator, round-13) edits `corpus/lessons/round-8-aggregator-box3-coldrun.md` (3/3)
- `51c9d308b25f73ac1754a12b544bd263ac065200` (operator, round-7) adds `corpus/lessons/round-5-aggregator-audit.md` and `corpus/lessons/round-5-aggregator-mirror-bare-path-and-unclosed-prereq.md`
- `9b3e49f5a063050956922552d72adcb1ecb34aed` (operator, round-2) adds `corpus/lessons/round-1-aggregator-audit.md`
- `b145d4f1f95327e821eeadafa21f63a97efdaf84` (operator) adds `corpus/lessons/round-4-aggregator-audit.md` (74 lines). Subject says aggregator; author is operator
- `9987054c850d124eb637a2c2ffe75253f51ee637` (operator) adds `corpus/lessons/round-1-aggregator-seed.md` and edits `corpus/README.md`

Parent repo, commits whose subject is a kagi report but whose pathspec is not only `.ufo/reports/round-<N>/kagi.md`:

- `ade32e49725a244c492da19d202a2156f456552e` author `kagi <kagi@shokunin.local>` (not `kagi-shokunin`). Swept sibling: rename `.ufo/reports/round-2/AGGREGATE.md` → `.ufo/reports/AGGREGATE.md` (aggregator ledger, 0-line rename) plus `M .ufo/l0-questions.md`, beside `A .ufo/reports/round-10/kagi.md`. This is the swept sibling file.
- `34858801b48279e96c5227c1f7d070f76d8132d6` operator. Pathspec overrun: `A .ufo/history-pin.json` beside `A .ufo/reports/round-15/kagi.md`. Fleet pin, not another lane's report.
- `e8cd25eb877d7d047588ad62fd17f0cbf042e3fb` operator. Pathspec overrun: `M .ufo/l0-questions.md` beside `A .ufo/reports/round-9/kagi.md`. Shared queue, not a sibling lane file.

Not charged to kagi as a lane commit, recorded so the reports are not mistaken for pathspec-clean lane commits:

- `17c1fadfddc5ecbfa5ef362ef44d111792fa3e94` operator, subject `fleet relaunch`. Lands `.ufo/reports/round-14/kagi.md` and `.ufo/reports/round-16/kagi.md` in the same commit as kake/kasegi/kengaku/kotoba/protocol prompts and reports, `.ufo/state/*` for every lane, and `.ufo/watchdog.log`. Owner: operator/integrator. Unblock: immutable.
- `609ecb6e09c5d3f7029b538895808c403446b203` and `6565e89904005d24421f77f6a79c73ade89ccdb2` are shared-identity / operator fleet commits that include early `kagi.md` files among other lanes. Not kagi lane commits.
- `f284c98f4e48978fbb095aa85d04245d2aaa418c` operator, subject `round-17`, pathspec is only `.ufo/reports/round-17/kagi.md`. Identity defect, not a sibling sweep.
- `44cc0bbf18da9c0462755fd08b3d42d946c0f509` `shokunin <shokunin@local>`, one file `.ufo/reports/round-8/kagi.md`. Identity defect, not a sibling sweep.
- `383ea1ac252ee4b1a9ed6700eb6aa981a3992d8b`, `029c474e85f515d1907260e451c5552cd13a3e80`, `8f5aa84c555ccb39aa849daadb750174891a6d71` are operator-identity and pathspec-clean (only that round's `kagi.md`).

Aggregator commits `baec94f`, `4391b3b`, `7c3377c`, `e0a04d8`, `ad694a2` each touch one `corpus/lessons/*aggregator*` file under `aggregator-shokunin`. Not a sweep.

## Axes

- Freshness: local HEAD is the named commit, dated today. Remote `origin/master` is the parent (`fecee874`). The lane record says "measured at HEAD" and does not pin `5b0d4b7`, so that phrase is true only while HEAD stays this commit.
- Operability: this commit's identity is the required one and is usable as a lane commit. The repo is not configured to keep producing it. Effective identity is `ci <ci@local>`.
- Calibration: no committed lane claim about identity or tree to disagree with. Commit message "scoped repair" is not in this diff. Historical operator count (16 personal + near-miss + `ci` + `shokunin@local`) is measured, not inferred from the lesson.
- Adjacency: `5b0d4b7` touches no sibling path. `ade32e4` remains the named sibling sweep (aggregator ledger rename). Round-19 has no parent report, so it did not repeat that class.

## Named debt

| Debt | Owner | Unblock |
|---|---|---|
| Local git identity unset; next bare commit would be `ci <ci@local>` | kagi lane | Set local `user.name` to `kagi-shokunin` and `user.email` to `kagi@shokunin.local`, plus a LOG note. Not done (read-only). |
| 16 operator-personal commits, plus `03477c0` near-miss, plus `ci`/`shokunin@local` commits, all ancestors of HEAD | kagi lane (history) | Immutable. Do not rewrite. New commits must use the lane identity explicitly until local config exists. |
| `ade32e4` swept `.ufo/reports/AGGREGATE.md` (rename from `round-2/`) and `.ufo/l0-questions.md` | kagi round-10 parent commit, near-miss identity | Immutable. Do not move the ledger back. |
| Operator lane commits that added or edited `corpus/lessons/*aggregator*` (`4b8c018`, `51c9d30`, `9b3e49f`, `b145d4f`, `9987054`) | those commits | Immutable. Later aggregator commits did not replace these blobs. |
| `5b0d4b7` not on `origin/master` (ahead 1) | kagi lane | Push to `VeigaPunk/kagi-shokunin` only if the driver allows. Not done. |
| No `.ufo/reports/round-19/kagi.md` | kagi record lane | Separate from this commit's pathspec. A later parent commit, if any, must be pathspec-limited to that report. |
| Untracked `plans/wwkd-round-19-recensus.md` | kagi lane working tree | Allowed by the cleanliness check. Leaving it untracked is the observed state, not a fail. |

## Residual risk

The identity on `5b0d4b7` was an override, not repo config. It will not survive the next commit unless the override is repeated or local config is set. Ahead-1 means another clone of `origin/master` still sees round 18 as HEAD.

## Verification gaps

Did not push, did not run gates, did not read session or credential content, did not read plan body lines past the heading and a class-only token scan. Did not audit whether round-18's own diff is pathspec-clean beyond confirming its author identity. Parent fleet commits `17c1fad` / `609ecb6` / `6565e89` were identified by path and author, not re-diffed file-by-file beyond the kagi-report paths named above.
