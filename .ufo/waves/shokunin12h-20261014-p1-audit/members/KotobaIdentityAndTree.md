# KotobaIdentityAndTree — advisory

**Seat:** identity and tree only. Not a judge verdict, receipt, or admission. No lane file edited. No commit, push, gate, lint, or formatter run. LSP not used: the question is git object identity, not a symbol.

**Repo:** `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (nested repo; parent ignores `*-shokunin/`).
**Audited commit:** `b0c7cb2e248bccf692cf10e4d3c394e09944e83d`
**Observed HEAD:** same hash. `master`, ancestor of itself, single parent `02302c521b933c55fc4be79193e61537e3380751`. `origin/master` is that parent; this checkout is ahead 1. Not pushed.
**Measured:** 2026-10-14, this seat, read-only.

**Axes:** freshness (HEAD is the named commit, not a stale pin), operability (object resolves; status/diff exits recorded; local `user.*` does not), calibration (lane record mis-attributes an old sweep; “one file” is the verifier delta, not the commit pathspec), adjacency (no sibling path in this commit; parent index does not embed the lane).

---

## Claim-by-claim

The committed round-19 record (`LOG.md`, `SCORECARD.md`, `corpus/lessons/round-19-recensus.md`) does **not** assert author, committer, or this hash. The untracked plan `plans/wwkd-round-19-recensus.md:19` is the contract this seat checked. Historical LOG identity/sweep sentences are judged below; they are not claims about `b0c7cb2`.

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| I1 | Author and committer are `kotoba-shokunin <kotoba@shokunin.local>` | **agree** | `git cat-file -p` author/committer lines. Byte match on both. Both timestamps `1792023336 -0300` (`2026-10-14T21:15:36-03:00`). Not a rebase that kept author and swapped committer. |
| I2 | One pathspec-limited commit of the lane's own files | **agree** | `git diff-tree -r --name-status` names exactly `M LOG.md`, `M SCORECARD.md`, `A corpus/lessons/round-19-recensus.md`, `M verifiers/verify_harness_claims.py`. No `160000` gitlink. No sibling-named path, no `plans/`, no `HOURS.md`, no `round-*-aggregator-*`. Parent `git ls-files --error-unmatch kotoba-shokunin` exit 1; `.gitignore:1` `*-shokunin/` ignores the lane. |
| I3 | Working tree clean apart from untracked `plans/` | **agree** | `git status --porcelain=v1 -uall` → `?? plans/wwkd-round-19-recensus.md` only (exit 0). `git diff --exit-code` and `git diff --cached --exit-code` exit 0. Worktree blobs of the four committed files equal `HEAD`. |
| I4 | Operator-identity commit on the audited object | **none** | Author and committer are the lane identity. Global git identity is `ci <ci@local>` (`/home/vgpnk/.config/git/config`). This commit did not use it. |
| I5 | Swept sibling file in `b0c7cb2` | **none** | Path list above. Diff appends a kotoba LOG tail, one kotoba move-log row, a new kotoba lesson, and two `CHECKS` rows in `verifiers/verify_harness_claims.py`. No file from kagi/kake/kama/kasegi/kengaku/kumitate or another `*-shokunin` tree. |
| I6 | Plan clause “then files the report with the actual hash” | **not this predicate** | `.ufo/reports/round-19/kotoba.md` absent (`test -f` exit 1). Record-conformance / lands-last owns that surface. Named below so it is not dropped. |
| I7 | Lesson “Landed change (one file, 2 lines)” | **agree for the verifier delta; disagree if read as the commit pathspec** | `verifiers/verify_harness_claims.py` numstat `2 2` (the two `at_least` → `equal` rows). The commit is four lane files, `41 insertions, 2 deletions`. Not a sibling sweep. |
| I8 | Subject “records + scoped repair” | **agree** | Records are the LOG/SCORECARD/lesson paths. The scoped repair is the two `CHECKS` rows. Unlike a records-only commit, a repair file is in the diff. |
| I9 | LOG round-9 “Lane identity fixed” as a current checkout fact | **disagree as current** | `LOG.md:170-172` says repo-local `user.name=kotoba-shokunin` / `user.email=kotoba@shokunin.local`. This checkout’s `.git/config` has no `user.*`. Reflog: `fad752b HEAD@{4}: clone`. Local config does not survive clone. The round-19 object is still lane identity (I1). |
| I10 | LOG “`0089974` used a `corpus/` pathspec, which swept in `corpus/lessons/round-9-aggregator-corpus-verdict.md`” | **disagree** | `0089974^` is `0f658ff` (`aggregator-shokunin <aggregator@shokunin.local>`). That parent tree already has the path, same blob `b594ff470e9c62ffa54672cba2c96c06bfdbcfea`. `git diff-tree -r --name-only 0089974` has no aggregator path. The file is in the tree because the owner committed it, not because `0089974` added it. |

---

## Commands (this seat)

Run from `kotoba-shokunin` unless noted. Exits are the command's own.

| Command | Exit | Observed |
|---|---|---|
| `git rev-parse HEAD` | 0 | `b0c7cb2e248bccf692cf10e4d3c394e09944e83d` |
| `git merge-base --is-ancestor b0c7cb2e… HEAD` | 0 | contained |
| `git rev-list --parents -n 1 b0c7cb2e…` | 0 | one parent: `02302c521b933c55fc4be79193e61537e3380751` |
| `git log -1 --format='%an <%ae>'` / `'%cn <%ce>'` vs `kotoba-shokunin <kotoba@shokunin.local>` | 0 | both match |
| `git diff-tree -r --name-status b0c7cb2e…` | 0 | four lane paths listed in I2 |
| `git show --numstat --format='' b0c7cb2e…` | 0 | `7 0 LOG.md`; `1 0 SCORECARD.md`; `31 0 corpus/lessons/round-19-recensus.md`; `2 2 verifiers/verify_harness_claims.py` |
| `git status --porcelain=v1 -uall` | 0 | `?? plans/wwkd-round-19-recensus.md` |
| `git status --porcelain=v1 --ignored` | 0 | same untracked row, plus `!! verifiers/__pycache__/verify_surfaces.cpython-314.pyc` (ignored by `.gitignore` `__pycache__/`) |
| `git diff --exit-code` / `git diff --cached --exit-code` | 0 / 0 | index and worktree match HEAD |
| `git hash-object` vs `git rev-parse HEAD:<path>` for the four committed paths | 0 | four blob matches |
| `git config --local --list` | 0 | no `user.name` / `user.email` |
| `git config --show-origin --get-regexp '^user\.'` | 0 | `global file:/home/vgpnk/.config/git/config user.name ci` and `user.email ci@local` only |
| `git rev-parse origin/master` | 0 | `02302c521b933c55fc4be79193e61537e3380751` |
| `git rev-list --count origin/master..HEAD` | 0 | `1` |
| parent `git ls-files --error-unmatch kotoba-shokunin` | 1 | path not in parent index |
| parent `git check-ignore -v kotoba-shokunin` | 0 | `.gitignore:1:*-shokunin/` |
| `test -f /home/vgpnk/Projects/shokunin/.ufo/reports/round-19/kotoba.md` | 1 | report file absent |
| `test -e HOURS.md` / `git ls-files HOURS.md` | 1 / empty | reverted; not in the tree |
| `git cat-file -e 0089974^:corpus/lessons/round-9-aggregator-corpus-verdict.md` | 0 | parent already had the file |
| `git diff-tree -r --name-only 0089974 \| grep aggregator` | 1 | no aggregator path in that commit’s diff |
| `git diff-tree -r --name-status 397b29c -- corpus/lessons/round-1-aggregator-audit.md` | 0 | `A` that path; parent `229b687` does not contain it (`cat-file -e` exit 128) |

Reflog does not store the commit argv. `HEAD@{0}` is `commit: round-19: …`. Pathspec limitation is the resulting diff, plus the plan file’s mtime `2026-10-14 20:36:30 -0300` (before the commit) and its absence from the commit. An `add -A` would have taken `plans/`. The exact flags are not in the object.

---

## Operator-identity commits

**None on `b0c7cb2`.**

Ancestry still contains them. History is not rewritten here. `PROTOCOL-APPENDIX.md` “Lane identity” names only `3b029b8`. The other seven personal-identity commits are the same class and are not that row.

Lane-round subjects under `Joao Pedro Veiga <jpveigao10@gmail.com>` (author and committer):

| Commit | Date | Subject |
|---|---|---|
| `1d931827ba3c40767a928e7cc793cba874942a67` | 2026-09-28T15:41:35-03:00 | round-1 |
| `229b687fb7a4f82bafb9aa61c2f775f61dce16ed` | 2026-09-28T15:57:23-03:00 | round-3 |
| `397b29c5bc59bf22fe7a15c475585ce5c61e5409` | 2026-09-28T16:07:29-03:00 | round-4 — also the sweep below |
| `4002b9f62e839528461785bd403dd45806a4e83b` | 2026-09-28T16:24:41-03:00 | round-5 |
| `3b029b8b75d954f003b8a185870b06f342b08148` | 2026-09-28T17:27:37-03:00 | round-7 — the recorded conformance defect |

Aggregator-subject commits under the same personal identity (not lane-round subjects; still not lane identity):

| Commit | Date | Path in `git log --name-only` |
|---|---|---|
| `456284d6d68ea5d341ef80c70925cf569cffde86` | 2026-09-28T16:12:38-03:00 | `M corpus/lessons/round-1-aggregator-audit.md` (ancestor is `397b29c`, which added it) |
| `9a74726c9cdb06ffb9ad5be06ba9a130306a9390` | 2026-09-28T16:37:56-03:00 | `corpus/lessons/round-4-aggregator-audit.md` |
| `23ae30129f44b95d53df91847d313b6ec0b8515b` | 2026-09-28T17:47:18-03:00 | `corpus/lessons/round-5-aggregator-audit.md` |

Not operator personal identity, and not this commit: `shokunin <shokunin@local>` on `43e0c0224876da4a7ba0a86d852b6f621cfecd67` (seed) and `8c300ad88ad6b67b6c26477a0da955b0bb360e51` (round-8 corpus entries). Live global identity `ci <ci@local>` on `21936672ee63fa138ec09fbf5aa80b6a60095417` and its revert `1fbf02bc15619f7e797cd3e38351cf280ba09171` (2026-10-13, this clone, before round-18). Those two touched `HOURS.md` and `LOG.md`. `HOURS.md` is absent after the revert.

Census of `git log --format='%an <%ae>'` on HEAD (44 commits): 26 lane, 8 personal operator, 6 `aggregator-shokunin <aggregator@shokunin.local>`, 2 `shokunin <shokunin@local>`, 2 `ci <ci@local>`.

---

## Swept sibling file

**None in `b0c7cb2`.**

Historical, not introduced by this commit:

- **`397b29c`** added `corpus/lessons/round-1-aggregator-audit.md`. That name is aggregator-owned (`PROTOCOL.md:479`, `round-<N>-aggregator-*.md`). Parent `229b687` does not have the path. The commit is a round-4 lane commit under operator identity and also changes `LOG.md`, `SKILL.md`, `corpus/README.md`, `corpus/knowledge/agent-defs-commands-and-round-prompts.md`, and `corpus/lessons/round-4.md`. That is the sweep.
- **`0089974` is not a sweep** of `corpus/lessons/round-9-aggregator-corpus-verdict.md`. See I10. `d6177f4` later deletes that path. `911b870` (`kotoba-shokunin`, subject “restore the aggregator's committed corpus lesson”) adds it again, blob `0d7ada3c31052a8e092223bf3f0da102a237c547`, not the aggregator blob `b594ff47…`. That is a later lane commit of an aggregator-owned path, recorded as a restore, not an unlogged pathspec accident and not part of `b0c7cb2`.

---

## Findings by severity

No finding fails I1–I5. The audited object is lane identity, lane-pathspec, and clean apart from untracked `plans/`.

1. **Record mis-attribution (calibration, not this commit’s pathspec).** `LOG.md:655-660` says `0089974` swept the round-9 aggregator lesson. The parent already had the same blob. Do not treat that sentence as evidence of a sweep.
2. **Historical operator-identity lane rounds and one historical sweep** remain in ancestry (`3b029b8` and the table above; sweep is `397b29c`). Not repaired by `b0c7cb2`. Protocol says not to rewrite them.
3. **Local identity is unset in this checkout.** The round-19 object did not inherit `ci <ci@local>`, but the next commit without an explicit `-c` / env override would. The two `ci` commits in this clone are the demonstration.

---

## Named debt

| Debt | Owner | Unblock |
|---|---|---|
| Repo-local `user.name` / `user.email` absent after clone | kotoba lane | Set them once to `kotoba-shokunin` / `kotoba@shokunin.local` and note it in `LOG.md`. Not done here. |
| Historical operator-identity commits and `397b29c` sweep | already in history; appendix names only `3b029b8` | No rewrite. An append-only note can name the other seven personal-identity commits and the `397b29c` add. Not this seat. |
| `LOG.md:655-660` false sweep attribution | kotoba record | Append-only correction. Do not rewrite the round-15 entry in place. |
| `.ufo/reports/round-19/kotoba.md` absent | whoever files the round report | File it citing `b0c7cb2`, lane identity, pathspec-limited to that report. Not an identity failure of the child commit. |
| Ignored `verifiers/__pycache__/verify_surfaces.cpython-314.pyc` (mtime 2026-10-14 09:58:31 -0300) | none | Already gitignored. Not untracked dirt. Do not commit it. |

Ahead 1 and not pushed matches the plan’s “Never push”. Not debt.

---

## Residual risk and verification gaps

- Commit argv is not stored. Pathspec limitation is inferred from the four-path diff and the excluded pre-existing `plans/` file, not from a recorded `git commit -- …`.
- This seat did not re-run gates, did not read session/secret content, and did not judge lesson pointer resolution.
- Parent-repo dirt and the missing round-19 report were observed, not repaired.
- `911b870`’s restore blob was not diffed line-by-line against `0f658ff`. Ownership and blob inequality are established; content drift inside that historical restore is outside this commit.
