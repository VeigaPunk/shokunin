# Kasegi identity and tree — advisory data

Seat: `KasegiIdentityAndTree`. Read-only. Not a judge verdict, receipt, or admission.
Repo under test: `/home/vgpnk/Projects/shokunin/kasegi-shokunin` (nested git; parent `shokunin` does not contain the object).
Audited object: `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc`.
Observed at: 2026-10-14. No lane file edited. No commit, push, fetch, or gate run.

## Summary

| Check | Result |
|---|---|
| Author and committer are `kasegi-shokunin <kasegi@shokunin.local>` | **agree / holds** |
| Commit pathspec is lane files only | **agree / holds** — 3 paths, 0 sibling paths |
| Working tree clean apart from untracked `plans/` | **agree / holds** — one untracked file |
| This commit is an operator-identity commit | **none** |
| This commit swept a sibling file | **none** |

HEAD is that commit. It is the only commit since `origin/master` (`0 1` ahead/behind). It is not on any remote-tracking branch. The untracked round plan says never push, so the unpushed state matches that plan rather than a pathspec or identity miss.

## Claim-by-claim

### 1. Identity of `a5cbf77` — agree with the audit contract

The lane's committed round-20 record does not assert an author string or this hash. Measurement is independent of that silence.

Raw object header (`git cat-file -p`), both identity fields byte-equal to the required string (timestamp stripped before compare):

```
author kasegi-shokunin <kasegi@shokunin.local> 1792023336 -0300
committer kasegi-shokunin <kasegi@shokunin.local> 1792023336 -0300
```

`git log -1 --format=fuller` agrees: Author and Commit are the same identity, both dated `Wed Oct 14 21:15:36 2026 -0300`. Subject: `round-20: OMP-era freshness re-census (measured gates; records + scoped repair)`. Single parent: `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1`. Reflog: `commit` (not amend) at that same timestamp.

The only configured identity is global `ci <ci@local>` from `file:/home/vgpnk/.config/git/config`. Local `user.*` is unset (exit 1). Hooks under `.git/hooks` are `*.sample` only. The object identity therefore does not match the configured default. [INFERENCE] the commit overrode identity at commit time; the command itself was not observed. The result on the object is observed.

Untracked plan `plans/wwkd-round-20-recensus.md:19` says the parent makes one pathspec-limited work commit under `kasegi-shokunin <kasegi@shokunin.local>`. **Agree** with that sentence for this object.

### 2. Pathspec limited to the lane's own files — agree

`git diff-tree --no-commit-id --name-status -r a5cbf77` (exit 0):

```
M	LOG.md
M	SCORECARD.md
A	corpus/lessons/round-20-recensus.md
```

Numstat: `7 0 LOG.md`, `6 0 SCORECARD.md`, `35 0 corpus/lessons/round-20-recensus.md`. No deletions, no renames, no mode other than the new file `100644`.

All three paths sit inside the lane repo and inside the lane allowlist used here (`LOG.md`, `SCORECARD.md`, `SKILL.md`, `PROVINCE.md`, `SHONEN.md`, `AGENTS.md`, `corpus/**`). Allowlist filter printed `ALL_IN_LANE_ALLOWLIST`. Name scan of the same list for `kagi-`, `kake-`, `kama-`, `kengaku-`, `kotoba-`, `kumitate-`, `aggregator-`, `protocol-` printed `NO_SIBLING_PATHS`.

The added lesson is `corpus/lessons/round-20-recensus.md`, not a `round-*-aggregator-*.md` file. `git log --diff-filter=A` shows this commit is the only introducer of that path, under the lane identity. It is not the historical sweep class (aggregator lesson absorbed into a lane commit; appendix cites `c80c2a1` for an older case). That older class is not this commit.

Parent repo cannot have absorbed these blobs by an ordinary add: `.gitignore:1` is `*-shokunin/`, `git check-ignore -v` matches `kasegi-shokunin` and `kasegi-shokunin/LOG.md`, and `git -C /home/vgpnk/Projects/shokunin ls-files -- kasegi-shokunin` is empty (exit 0).

Commit-subject vs diff: the subject says `records + scoped repair`. This diff is records only. The lesson in the same commit says `No gate change` and that the suffix-join root-default change was left unlanded. Instrument edits live in parent `d1e6e8f` (round 19, also `kasegi-shokunin <kasegi@shokunin.local>`, 21 files). **Disagree** with reading this subject as "this commit contains a repair." Not a pathspec breach.

### 3. Tree clean apart from untracked `plans/` — agree

`git status --porcelain=v1 -uall` (exit 0; exit 0 does not mean clean — the porcelain line is the evidence):

```
?? plans/wwkd-round-20-recensus.md
```

`git status --porcelain=v2 -uall --ignored` shows the same single `?` line. `git diff --cached --exit-code --quiet` exit 0. `git diff --exit-code --quiet` exit 0. `git clean -nd` exit 0, stdout `Would remove plans/`. `git ls-files --others --exclude-standard` lists only that file. No `MERGE_HEAD`, `CHERRY_PICK_HEAD`, `REBASE_HEAD`, `rebase-merge`, `rebase-apply`, or `sequencer`. One worktree: `/home/vgpnk/Projects/shokunin/kasegi-shokunin a5cbf77 [master]`.

`plans/wwkd-round-20-recensus.md` is 2084 bytes, mtime `2026-10-14 20:36` (before the 21:15 commit). It is untracked, not ignored. That is the allowed exception, not extra dirt.

Parent `shokunin` status is a different tree: many untracked `.ufo/` and `.omp/` entries (porcelain count 126 at sample time), none of them `kasegi-shokunin` content. Not charged to this lane tree.

### 4. Operator-identity commit or swept sibling file — none on this object

Audited commit author and committer are the lane identity. Its three paths are lane files. No sibling path, no aggregator-owned lesson, no parent-repo path.

Ancestry is not this commit. Reported so "any operator-identity commit" is not silently dropped:

| Identity | Count on `master` | Relation to `a5cbf77` |
|---|---|---|
| `Joao Pedro Veiga <jpveigao10@gmail.com>` | 17 | ancestors only; newest is `ed44a923e465c3cf509898a26a6c6fe082df6851` `round-18` |
| `ci <ci@local>` | 2 | ancestors only; `b71b76b` adds `HOURS.md`+`LOG.md`, `7906aa1` reverts both; `HOURS.md` absent at HEAD (`git cat-file -e HEAD:HOURS.md` exit 128) |
| `aggregator-shokunin <aggregator@shokunin.local>` | 4 | ancestors; aggregator subject, not this commit |
| `shokunin <shokunin@local>` | 4 | early seed / rounds 1 and 3 |
| `kasegi-shokunin <kasegi@shokunin.local>` | 2 | `d1e6e8f` round 19 and `a5cbf77` round 20 |

`ci <ci@local>` is the unconfigured default, not the personal operator address. Neither `ci` commit nor any personal-operator commit is `a5cbf77`. The pre-amend round-19 object `a1ecc8d` (reflog `commit`, then `commit (amend)` to `d1e6e8f`) is also lane identity on both author and committer. It is not the audited hash.

### 5. Lane record vs this measurement

| Lane text | Verdict |
|---|---|
| Committed `LOG.md` round-20 entry (lines 819–824) and `SCORECARD.md` move-log row | silent on author, pathspec, and hash. No identity claim to agree or disagree with. Pointers name the lesson and the repair-wave member dir, not `a5cbf77`. |
| Committed lesson | silent on author and hash. `No gate change` **agrees** with this diff not touching instruments. |
| Untracked plan, identity + pathspec + never-push | **agree** (see checks 1–2 and the ahead-1 note). |
| Untracked plan, "files the report with the actual hash" | **disagree** inside the lane commit. `git grep -n -F a5cbf77 HEAD` exit 1. A repo-wide search under `/home/vgpnk/Projects/shokunin` hits only this audit wave's own spec/run/task text and a sibling seat file, not a lane-filed report. |
| `corpus/lessons/round-6-aggregator-audit.md:112-114` ("commit identity… none use `kasegi-shokunin`/`kasegi@shokunin.local`") | **disagree if read as current.** Rounds 19 and 20 use that identity. The local-config half of that sentence is still true (`git config --local user.name` unset). Dated round-6 lesson; marking it historical is not this seat's edit. |

## Commands and exits

Run from the lane repo unless noted. Read-only.

| Command | Exit | Observed tail |
|---|---|---|
| `git -C /home/vgpnk/Projects/shokunin cat-file -t a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` | 128 | `fatal: git cat-file: could not get object info` (parent object database) |
| `git -C kasegi-shokunin cat-file -t a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` | 0 | `commit` |
| `git -C kasegi-shokunin rev-parse HEAD` | 0 | `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` |
| `git -C kasegi-shokunin diff-tree --no-commit-id --name-status -r a5cbf77…` | 0 | `M LOG.md`, `M SCORECARD.md`, `A corpus/lessons/round-20-recensus.md` |
| `git -C kasegi-shokunin diff --cached --exit-code --quiet` | 0 | empty |
| `git -C kasegi-shokunin diff --exit-code --quiet` | 0 | empty |
| `git -C kasegi-shokunin status --porcelain=v1 -uall` | 0 | `?? plans/wwkd-round-20-recensus.md` |
| `git -C kasegi-shokunin clean -nd` | 0 | `Would remove plans/` |
| `git -C kasegi-shokunin config --local --get-regexp '^user\.'` | 1 | empty |
| `git -C kasegi-shokunin config --show-origin --get user.name` | 0 | `file:/home/vgpnk/.config/git/config	ci` |
| `git -C kasegi-shokunin config --show-origin --get user.email` | 0 | `file:/home/vgpnk/.config/git/config	ci@local` |
| `git -C kasegi-shokunin rev-list --left-right --count origin/master...HEAD` | 0 | `0	1` |
| `git -C kasegi-shokunin branch -r --contains a5cbf77…` | 0 | empty (no remote branch contains it) |
| `git -C kasegi-shokunin grep -n -F a5cbf77 HEAD` | 1 | hash absent from the committed tree |
| `git -C kasegi-shokunin rev-list --count a5cbf77 ^d1e6e8f` | 0 | `1` |
| `git -C /home/vgpnk/Projects/shokunin ls-files -- kasegi-shokunin` | 0 | empty |

Identity compare (author and committer, timestamp stripped): both `match=True` against `kasegi-shokunin <kasegi@shokunin.local>`.

## Named debt

| Debt | Owner | Unblock | Blocks this commit's identity? |
|---|---|---|---|
| Lane repo has no local `user.name` / `user.email`. Effective identity remains global `ci <ci@local>`. `PROTOCOL.md` invariants (lane authorship) say an unconfigured child repo is set once and noted in `LOG.md`. Round-20 LOG does not note it. A later commit without an override would land as `ci`, the same class as `b71b76b` / `7906aa1`. | kasegi lane; mint-time config also sits with whoever left the clone unconfigured (`reflog` `clone` at 2026-10-13 16:50:59 -0300 from `https://github.com/VeigaPunk/kasegi-shokunin.git`) | set local `user.name=kasegi-shokunin` and `user.email=kasegi@shokunin.local`, and append a LOG note. Not done here. | no — `a5cbf77` already carries the lane identity |
| Committed round-20 record does not cite `a5cbf77`, despite the untracked plan's "file the report with the actual hash" | kasegi record owner (record-conformance seat owns the pointer audit) | append the hash to the round report the plan required. Not done here. | no |
| `origin/master` is parent `d1e6e8f`; this commit is local-only | none while the round plan's "Never push" stands. If a later driver requires push: kasegi, push only `VeigaPunk/kasegi-shokunin` | not performed (audit forbids push) | no |

## Residual risk

- Durable config is still the default that produced the two `ci <ci@local>` commits. Those commits did not sweep a sibling repo; they touched `HOURS.md` and `LOG.md`, and the revert removed `HOURS.md` from HEAD. They remain in history under a non-lane identity.
- Seventeen personal-operator commits remain in ancestry, ending at round 18. They are not rewritten by `a5cbf77` and are not a defect of this object.
- Round-6 lesson defect 11 still says no commit uses the lane identity. That sentence is false for HEAD. Leaving it unmarked is a historical-marking item, not a live citation inside `a5cbf77`.
- Parent working tree dirt is outside this lane and did not enter this commit.

## Not in this seat

Gates, live citation sweep, and lesson-claim resolution were not re-run. No counterexample was found to the three checks on `a5cbf77` itself.
