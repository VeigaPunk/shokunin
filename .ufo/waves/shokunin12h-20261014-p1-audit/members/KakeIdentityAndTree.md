# KakeIdentityAndTree — advisory

Data only. Not a judge verdict, receipt, or admission. Read-only. No lane file edited, no commit, no push, no gate run.

Repo: `/home/vgpnk/Projects/shokunin/kake-shokunin` (nested git; parent `.gitignore:1` `*-shokunin/` ignores it). Audited object: `59948314e9af5dd6ef81894fc1c422b353f10938`. Acceptance item checked: lane-identity commit present, tree clean apart from untracked `plans/`, commit pathspec-limited to the lane's own files. Operator-identity commits and swept sibling files are reported where found. They are not charged to this commit unless they are in this commit.

## Axes

Adjacency (who authored, whose files landed). Calibration (lane/plan claims vs headers). Freshness of the worktree (dirt vs allowed `plans/`). Operability residual: repo-local identity still unset, so the next commit without an override would not be the lane identity.

## Commands (this seat)

| Command | Exit | Observed |
|---|---|---|
| `git -C kake-shokunin rev-parse --verify 59948314e9af5dd6ef81894fc1c422b353f10938^{commit}` | 0 | `59948314e9af5dd6ef81894fc1c422b353f10938` |
| `git -C kake-shokunin rev-parse HEAD` | 0 | same hash. Tip is the audited commit. |
| `git -C kake-shokunin rev-parse origin/master` | 0 | `b0feb30886585d8df6d4671845a2d18989ca722b` |
| `git -C kake-shokunin rev-list --count origin/master..HEAD` | 0 | `1` (not pushed; plan says never push) |
| `git -C kake-shokunin merge-base --is-ancestor 59948314… HEAD` | 0 | ancestor of HEAD (it is HEAD) |
| `git -C kake-shokunin cat-file -p 59948314…` | 0 | one parent; author and committer headers below |
| `git -C kake-shokunin diff-tree --name-status -r 59948314^ 59948314` | 0 | four paths, listed below |
| `git -C kake-shokunin status --porcelain=v1 -uall` | 0 | `?? plans/wwkd-round-19-recensus.md` only |
| `git -C kake-shokunin status --porcelain=v1 --ignored=matching --untracked-files=all` | 0 | same line; no `!!` ignored extras |
| `git -C kake-shokunin ls-files --others --exclude-standard` | 0 | `plans/wwkd-round-19-recensus.md` |
| `git -C kake-shokunin ls-files --others -i --exclude-standard` | 0 | empty |
| `git -C kake-shokunin diff-index --name-status HEAD` | 0 | empty |
| `git -C kake-shokunin diff --name-only HEAD` | 0 | empty |
| `git -C kake-shokunin diff --cached --stat` | 0 | empty |
| `git -C kake-shokunin ls-files -v` filtered to assume-unchanged / skip-worktree | 0 | empty |
| `git -C kake-shokunin check-ignore -v plans/wwkd-round-19-recensus.md` | 1 | not ignored |
| `git -C kake-shokunin config --local --get user.name` | 1 | unset |
| `git -C kake-shokunin config --local --get user.email` | 1 | unset |
| `git -C kake-shokunin config --show-origin --get-regexp '^user\.'` | 0 | `file:/home/vgpnk/.config/git/config` `user.name=ci` `user.email=ci@local` |
| `git -C /home/vgpnk/Projects/shokunin check-ignore -v kake-shokunin` | 0 | `.gitignore:1:*-shokunin/` |
| `ls .ufo/reports/round-19/kake.md` | — | absent (`round-19/` directory absent) |

No freshness-sweep / selftest was run here. That seat is `KakeGateRerun`.

## Claim-by-claim

### 1. Author identity is `kake-shokunin <kake@shokunin.local>` — agree

Raw commit header (no gpgsig, no extra whitespace):

```
tree c5b2d3cb53efd1f05effc24354264ee78af9d84c
parent b0feb30886585d8df6d4671845a2d18989ca722b
author kake-shokunin <kake@shokunin.local> 1792023336 -0300
committer kake-shokunin <kake@shokunin.local> 1792023336 -0300

round-19: OMP-era freshness re-census (measured gates; records + scoped repair)
```

Author and committer are the same string, same timestamp (`2026-10-14 21:15:36 -0300`). Single parent. Not a merge (`git rev-list --parents -n 1` prints exactly one parent). Subject is a round-19 lane commit, not an operator subject.

`plans/wwkd-round-19-recensus.md` (untracked parent plan, line 19) says the parent makes one pathspec-limited work commit under that identity. That claim matches this object. The lesson `corpus/lessons/round-19-recensus.md` does not itself name the hash or the identity. Absence of that sentence is not a contradiction.

[INFERENCE] The commit did not inherit the host default `ci <ci@local>`. Local `user.name` / `user.email` are unset (exit 1) and the host file is `ci`, yet both headers are the lane identity. The override command was not observed.

### 2. Pathspec-limited to the lane's own files — agree for this commit

`git diff-tree -r --raw` (modes unchanged, no rename, no delete, no gitlink):

| Path | Mode | Status | Numstat |
|---|---|---|---|
| `LOG.md` | 100644 | M | +7 / 0 |
| `SCORECARD.md` | 100644 | M | +1 / 0 |
| `corpus/lessons/round-19-recensus.md` | 100644 | A | +40 / 0 |
| `scripts/freshness-sweep.mjs` | 100755 | M | +121 / -14 |

Allowlist used: lane root records (`LOG.md`, `SCORECARD.md`, and the usual `SKILL.md` / `PROVINCE.md` / `SHONEN.md` / `AGENTS.md` / `MINT.md`), `corpus/**` that are not aggregator-owned lessons, and lane instruments under `scripts/`. Excluded as not the lane's: `corpus/lessons/*aggregator*`, sibling-lane trees, parent `.ufo/**`, `HOURS.md`.

All four paths are inside the allowlist. Zero names match `aggregator`, `HOURS`, `.ufo/`, or another lane id. The new lesson is `round-19-recensus.md`, not an aggregator audit file. The LOG hunk is an append at the end (round-19 pointer only). The SCORECARD hunk is one move-log row. No sibling report, no parent runtime file, and no untracked `plans/` file is in the commit.

The lesson sentence "Landed change (one file): `scripts/freshness-sweep.mjs`" is the mechanism delta, not the commit pathspec. The other three paths are the lane's own record appends, not swept sibling files. Whether that sentence underspecifies the commit is `KakeRecordConformance`'s seat, not a pathspec fail here.

### 3. Working tree clean apart from untracked `plans/` — agree

One worktree: `/home/vgpnk/Projects/shokunin/kake-shokunin 5994831 [master]`. Porcelain, ignored-matching, and `ls-files --others` agree: the only dirt is untracked `plans/wwkd-round-19-recensus.md`. `find plans` shows that one file. Index matches HEAD. No assume-unchanged or skip-worktree bits. No ignored untracked residue.

`plans/` is not gitignored (`check-ignore` exit 1). That is allowed by the acceptance exception. It is also the residual sweep hazard below.

The parent fleet worktree was not treated as this lane's worktree. `kake-shokunin` is gitignored there. `.ufo/reports/round-19/kake.md` does not exist, so there is no main-repo kake report commit to classify as operator-identity or as a swept sibling pathspec. Not a defect of `59948314`. Owner of the missing report, if one is still owed: parent integrator. Unblock: file it pathspec-limited, or record that no report was required. This seat did not file it.

## Operator-identity commit

None in `59948314`. None in `origin/master..HEAD` (that range is this one commit).

Ancestry still contains them. Not introduced by this commit. Not rewritten. `git log --format='%an <%ae>' | sort | uniq -c` over 27 commits:

| Count | Identity | Class |
|---|---|---|
| 17 | `Joao Pedro Veiga <jpveigao10@gmail.com>` | operator personal. Round commits `cd5b381b7687338d5578019d50b6c1732504b614` (round-1) through `72eb11262b1e3506ea53d12f17c78736cf099629` (round-17), plus the two aggregator-file commits below |
| 2 | `ci <ci@local>` | host default, not lane. `160bd8ab35f721c1dd9496a1005575975afed6d3` added `HOURS.md` + `LOG.md`; `c00c6656826ab34ed8299ce045f1257cd8d53dde` deleted `HOURS.md` + edited `LOG.md`. `HOURS.md` is absent at HEAD |
| 2 | `kake-shokunin <kake@shokunin.local>` | conforming. `b0feb30886585d8df6d4671845a2d18989ca722b` (round-18) and `59948314` (round-19) |
| 1 | `kake-shokunin <kake-shokunin@local>` | lane name, non-conforming email. `83d08e47118845b93083b5c812af14e81a87f9b7` (round-7) |
| 1 | `shokunin <shokunin@local>` | mint seed `11261443ec6a1748fdeab9c3fc85e7f6c06ed530`. Not a round commit |
| 4 | `aggregator-shokunin <aggregator@shokunin.local>` | aggregator-owned lessons, correctly attributed (rounds 6, 8, 9) |

`corpus/lessons/round-6-aggregator-audit.md` still carries the open row that lane identity is unused and that `git config --local user.name` is unset. The unset-config half still reproduces (exit 1). The "identity not used" half is no longer true of round-18/19. That row was not updated by `59948314`.

## Swept sibling file

None in `59948314`.

Historical, still in the tree, not touched by `59948314`:

- `6b1cd0792cef73e8368bc64880d209c950c5b922` (`Joao Pedro Veiga`, subject `round-4`) added `corpus/lessons/round-1-aggregator-audit.md`. Lane round commit, operator identity, aggregator-owned path.
- `ac5ff82c03fc24bf581917eb30a2abdb0109387b` (`Joao Pedro Veiga`, subject `corpus: round-4 aggregator audit lesson`) added `corpus/lessons/round-4-aggregator-audit.md`.
- `1395393d889027cb46d4d905c1c510538d20b317` (`Joao Pedro Veiga`, subject `corpus: round-5 aggregator audit lesson`) added `corpus/lessons/round-5-aggregator-audit.md` and `corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md`.

Later aggregator commits under `aggregator-shokunin` introduced the round-6/8/9 lessons themselves. Those are not sweeps.

Parent commit `b0feb30886585d8df6d4671845a2d18989ca722b` is lane identity, but it modified four aggregator-owned lessons (`round-1` +4/-5, `round-4` +3/-3, `round-5` +1/-1, `round-6` +3/-3). The hunks are HTML comments dated `r18 re-census 2026-10-14` marking deleted `~/Projects/webzites` cites as historical. Not a bulk absorb of new aggregator prose. Still a lane commit of aggregator-owned files. Not in `59948314`.

## Named debt

| Item | Owner | Unblock | Charged to `59948314`? |
|---|---|---|---|
| Repo-local `user.name` / `user.email` unset; host default is `ci <ci@local>` | kake | set local git identity to `kake-shokunin` / `kake@shokunin.local` and note it in `LOG.md`. Do not rely on the host file | no (this commit's headers are already the lane identity) |
| `plans/wwkd-round-19-recensus.md` untracked and not ignored | whoever makes the next kake commit | pathspec-limit, or ignore `plans/` | no (not in this commit; explicitly allowed dirt) |
| Operator-identity round commits `cd5b381` through `72eb112`, plus non-conforming `83d08e4` | kake / history | do not rewrite. Mark the round-6 identity row historical; new rounds keep an override until local config is set | no |
| `ci` commits `160bd8a` / `c00c665` (HOURS add/revert) | whoever owns craft-hours bookkeeping | leave reverted. Do not re-add `HOURS.md` under `ci` | no |
| Operator commits that added aggregator lessons: `6b1cd07`, `ac5ff82`, `1395393` | aggregator owns the files; kake owns the mis-attributed commits | do not move them in this audit. A later aggregator commit may annotate authorship; a lane commit must not edit them again | no |
| Round-18 edited four aggregator lessons | kake (commit `b0feb30`) | stop editing aggregator lesson paths. Further absent-path notes belong in a kake lesson, or in an aggregator commit | no |

## Residual risk and gaps

- Next `git commit` without an identity override will be `ci <ci@local>`. Local config exit 1 is the evidence.
- `git add -A` would stage `plans/wwkd-round-19-recensus.md`. This commit did not.
- Not pushed (`ahead 1`). Matches the plan's never-push line. Not independently required by the identity check.
- Main-repo round-19 report is absent. No operator-identity report commit exists to fail. Also no proof one was filed elsewhere.
- Gate argv/exit lines were not re-run. Identity of `59948314` does not depend on them.
- The commit command line was not recovered from a reflog or process table. The identity conclusion is from the commit object, not from an observed override invocation.

## This commit

`59948314e9af5dd6ef81894fc1c422b353f10938`: lane identity, four lane files, worktree clean except untracked `plans/`. No operator-identity header. No swept sibling path.
