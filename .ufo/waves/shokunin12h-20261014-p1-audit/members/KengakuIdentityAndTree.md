# KengakuIdentityAndTree

Advisory data only. Not a native judge verdict, receipt, or admission. No lane file was edited. No commit, push, gate, build, or formatter was run.

Axes: freshness, operability, calibration, adjacency.
Object: `kengaku-shokunin` commit `7153e671b1581a4b705583656883b6af158257df`.
Repo: `/home/vgpnk/Projects/shokunin/kengaku-shokunin` (nested; parent `.gitignore:1` `*-shokunin/`).

LSP: not used. The object is a git commit, not a source symbol. `xd://lsp` was not consulted. Path evidence below is `git` output, not semantic proof.

## Claim-by-claim

| Claim | Verdict | Evidence |
|---|---|---|
| Author and committer of `7153e671` are `kengaku-shokunin <kengaku@shokunin.local>` | **Agree** | `git log -1 --format` on that hash: both fields exact. Byte compare in this session: `author_match True`, `committer_match True`. No trailer. AuthorDate = CommitDate = `2026-10-14 21:15:36 -0300`. |
| That commit is the lane HEAD | **Agree** | `git rev-parse HEAD` → `7153e671b1581a4b705583656883b6af158257df`, exit 0. `git cat-file -t` → `commit`, exit 0. Single parent `d84e48d525d6af6b1d137d608aea8c726f8bead4`; `merge-base --is-ancestor` exit 0. Reflog: `HEAD@{2026-10-14 21:15:36 -0300}: commit:` (not amend, rebase, or cherry-pick). One worktree. |
| Pathspec-limited to this lane's files | **Agree** | `git diff-tree --no-commit-id --name-only -r` count 3, exit 0: `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-16-recensus.md`. Sibling-path grep exit 1 (no match). No `../`, no other `*-shokunin/`, no `.ufo/` path. `grader.py` blob identical to parent (`4811bce1409c912ad4e326703bb542351955e6a4` both sides). |
| Working tree clean apart from untracked `plans/` | **Agree** | `git status --porcelain=v1 -uall` exit 0, sole line `?? plans/wwkd-round-16-recensus.md`. `git diff --quiet HEAD` exit 0. `git diff --quiet --cached` exit 0. `git ls-files --others --exclude-standard` is that one file. `--ignored` adds no `!!` lines. No assume-unchanged / skip-worktree. |
| This commit is an operator-identity commit | **Disagree with that reading; none found** | Author filter against the required identity returned the commit. No `Joao Pedro Veiga`, `João Pedro Veiga`, or `ci <ci@local>` on this object. |
| This commit swept a sibling file | **Disagree with that reading; none found** | Path list above. Parent repo cannot have absorbed it after the fact: parent HEAD `5ec4b43280e5cad3698a7e71b7b301e5ccdb0883` is `2026-10-14 20:26:16 -0300`, 49 minutes before this commit. Parent `ls-files kengaku-shokunin` count 0. `check-ignore -v` exit 0 on `.gitignore:1:*-shokunin/`. |
| Round-16 LOG / SCORECARD / lesson assert this identity, pathspec, or clean tree | **No such sentence** | Those three files do not contain `7153e671`, `kengaku-shokunin <kengaku@shokunin.local>`, or `pathspec`. Silence is not a false identity claim. |
| Commit subject "records + scoped repair" means an implementation repair landed | **Disagree** | Diff is +43/−0 across the three record files only. Lesson title and body say no `--src` repair. **Agree** with that lesson sentence as a description of the diff, not as a re-run of `grader.py` (not run here). |
| SCORECARD move-log row identifies the measured revision | **Disagree** | `SCORECARD.md:364` says `measured at HEAD (see lesson)` and cites the lesson, which also does not name a hash. Current HEAD happens to be `7153e671`. The row does not pin it. |
| Living round-9 LOG sentence "local user.name/user.email configured once" is true of this checkout | **Disagree as a current fact** | `git config --local --get user.name` exit 1. `user.email` exit 1. `git config --local --list` has no identity keys. Reflog clone `2026-10-13 16:51:01 -0300` from `https://github.com/VeigaPunk/kengaku-shokunin.git` replaced this `.git`. The round-9 action is not in the commit object. Not re-proven for the pre-clone checkout. |

`origin/master` is the parent `d84e48d`. `git rev-list --left-right --count HEAD...origin/master` → `1 0`, exit 0. Ahead 1 is the audited commit, unpushed. That is branch state, not a dirty tree. Repair contract said not to push. Not scored as dirt.

## Operator-identity commits

None on `7153e671`. Ancestors still reachable, not introduced by this commit, not rewritten here:

| Hash | Identity | Subject | In this commit's pathspec? |
|---|---|---|---|
| `f147a270696116579519e5a836663da33af06e1c` | `Joao Pedro Veiga <jpveigao10@gmail.com>` | round-7 | no |
| `91f021c5c2fdc735c01605965c1852a465121bdd` | same | corpus: round-4 aggregator audit lesson | no |
| `d5f1cadc58a0784fbad2e9512989fdb430d2f968` | same | round-6 | no |
| `782dd2d2c923c0d3a9b87e6055ac78511065e97d` | same | round-5 | no |
| `a1af83c1752ebe8ff6d949a1b8bbd35f256a4501` | same | round-4 | no |
| `a4c056e6155297d7f0069473cd11fe2ddd124ba6` | same | round-3 | no |
| `24ff62edeebd0753fd024dcfa23435f932161f73` | same | round-1 | no |
| `90a5ce865f845d17e9fd4a33130bdc097d8861f2` | same | round-1 | no |

`git log --author=João` in this repo: no hits. The accented operator string appears on the parent repo, not on these objects.

Not personal-operator, also not lane identity, also not in this commit:

| Hash | Identity | Pathspec |
|---|---|---|
| `1d56b855d6b24032136ad0e5b4c8c55f8a7a70fd` | `ci <ci@local>` | `A HOURS.md`, `M LOG.md` |
| `28a2fbfb3e53be0efc762d2e0b8a4258fbae341c` | `ci <ci@local>` | `D HOURS.md`, `M LOG.md` |
| `ae8a7bd98f799aa8fcfd64e8b9cf98fab3af0079` | `shokunin <shokunin@local>` | seed |

`ci <ci@local>` is the current global `user.name` / `user.email`. The HOURS pair is in-lane only; the revert removed `HOURS.md` (`git ls-files -- HOURS.md` empty). Not a sibling sweep. Five `aggregator-shokunin <aggregator@shokunin.local>` ancestors are the aggregator's own subject, not an operator sweep by this commit.

Reachable author histogram: lane 6, personal operator 8, aggregator 5, `ci` 2, `shokunin <shokunin@local>` 1.

## Swept sibling file

None in `7153e671`. None in the post-clone `ci` pair. No parent-repo round-16 report exists to have swept one: `test -e /home/vgpnk/Projects/shokunin/.ufo/reports/round-16/kengaku.md` exit 1. `git diff-tree` of this commit does not include `corpus/README.md` (grep exit 1). That omission is an unindexed lesson, not a sibling file.

## Named debt

| Debt | Owner | Unblock |
|---|---|---|
| Local identity unset after the 2026-10-13 clone. Next bare `git commit` inherits global `ci <ci@local>`, not the lane identity. This commit itself overrode that. | kengaku | Set local `user.name` / `user.email` once and append a LOG note. Do not amend `7153e671`. |
| Move-log / lesson do not pin `7153e671`. Parent report that should cite it is absent. | parent integrator, after record seat | New main-repo commit, pathspec-limited to `.ufo/reports/round-16/kengaku.md`, under the lane identity. Do not amend the child commit. |
| `corpus/lessons/round-16-recensus.md` is the 18th tracked lesson; `git grep -c` of lesson rows in `corpus/README.md` is 17. Name is absent from README. | kengaku record (not this seat) | Append an index row in a later lane-identity commit. Not a reason to widen `7153e671`. |
| Eight personal-operator ancestors (rounds 1-7 and the round-4 aggregator lesson under that identity) | historical; already named in `corpus/lessons/round-6-aggregator-audit.md` | Do not rewrite. Describe-don't-pin. |
| Subject line says "scoped repair"; no implementation file changed | kengaku, if a later note is filed | Append, do not amend. The lesson already says no `--src` repair. |

## Residual risk

A reader of `git log -1` can treat "scoped repair" as a `grader.py` change. The blob hash says otherwise. A later commit without an explicit identity override will not repeat this commit's identity, because local config is empty and global config is `ci <ci@local>`. `SCORECARD.md:364` will become false of a newer HEAD without a hash pin. Ahead 1 is expected until a push the repair contract forbade; it is not evidence the commit is missing.

## Verification gaps

- Did not run `python3 grader.py` or `--selftest`. Gate lines in the lesson were not re-measured.
- Did not content-read credentials, oauth, `server.token`, or session text.
- Did not fetch or push. `origin/master` equality is the local remote-tracking ref.
- Pre-clone local config was not recovered. The round-9 "configured once" sentence is unverified for that older checkout and false here.
- An unsorted `comm` over README lesson names is not cited. The unindexed-file claim uses the name grep plus the 17-vs-18 count.
