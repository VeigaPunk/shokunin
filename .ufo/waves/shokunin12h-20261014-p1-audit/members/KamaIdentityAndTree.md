# KamaIdentityAndTree — advisory

**Seat:** identity and tree only. Not a judge verdict, receipt, or admission. No lane file edited. No commit, push, gate, lint, or formatter run. LSP not used: the question is git object identity, not a symbol.

**Repo:** `/home/vgpnk/Projects/shokunin/kama-shokunin` (nested repo; parent ignores `*-shokunin/`).
**Audited commit:** `84a81304d7b0c77c84fe495f3bb728e8729faaff`
**Observed HEAD:** same hash. `master`, ancestor of itself, single parent `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21`.
**Measured:** 2026-10-14, this seat, read-only.

**Axes:** freshness (HEAD is the named commit, not a stale pin), operability (object resolves; status/diff exits recorded), calibration (lane record does not invent an identity the object lacks; subject overclaims a repair), adjacency (no sibling path in the commit; parent index does not embed the lane).

---

## Claim-by-claim

The committed round-4 record (`LOG.md`, `SCORECARD.md`, `corpus/lessons/round-4-recensus.md`) does **not** assert author, committer, hash, or pathspec. Nothing there to agree or disagree with on identity. The untracked plan `plans/wwkd-round-4-recensus.md:19` is the contract this seat checked.

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| I1 | Author and committer are `kama-shokunin <kama@shokunin.local>` | **agree** | `git cat-file -p` lines 3–4, byte match. Both timestamps `1792023336 -0300` (`2026-10-14T21:15:36-03:00`). Not a rebase that kept author and swapped committer. |
| I2 | One pathspec-limited commit of the lane's own files | **agree** | `git diff-tree` names exactly `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-4-recensus.md`. No `160000` gitlink. No sibling-named path. Parent `git ls-files --error-unmatch kama-shokunin` exit 1 (not in the parent index). |
| I3 | Working tree clean apart from untracked `plans/` | **agree** | `git status --porcelain=v1` → `?? plans/` only (exit 0). `git diff` and `git diff --cached` exit 0. Worktree blobs of the three committed files equal `HEAD`. |
| I4 | Operator-identity commit on the audited object | **none** | Author and committer are the lane identity. Global git identity is `ci <ci@local>` (`/home/vgpnk/.config/git/config`); this commit did not use it. |
| I5 | Swept sibling file in `84a81304` | **none** | Path list above. Diff adds a kama LOG tail, a kama move-log row, and a new kama lesson. No file from kagi/kake/kasegi/kengaku/kotoba/kumitate/kaidoku or another `*-shokunin` tree. |
| I6 | Plan clause “then files the report with the actual hash” | **not this predicate** | `.ufo/reports/round-4/kama.md` absent (`test -f` exit 1). Record-conformance seat owns that surface. Named below so it is not dropped. |
| I7 | Commit subject “records + scoped repair” | **disagree** (message only) | Lesson says “No repair warranted” and “Re-repairing it would be churn.” Diff touches zero files under `tools/` or `registry/`. Records landed; no repair landed. Not an identity or pathspec failure. |

---

## Commands (this seat)

Run from `kama-shokunin` unless noted. Exits are the command's own.

| Command | Exit | Observed |
|---|---|---|
| `git rev-parse HEAD` | 0 | `84a81304d7b0c77c84fe495f3bb728e8729faaff` |
| `test "$(git rev-parse HEAD)" = 84a81304d7b0c77c84fe495f3bb728e8729faaff` | 0 | HEAD is the named commit |
| `git merge-base --is-ancestor 84a81304d7b0c77c84fe495f3bb728e8729faaff HEAD` | 0 | contained |
| `git rev-list --parents -n 1 84a81304d7b0c77c84fe495f3bb728e8729faaff` | 0 | one parent: `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21` |
| `git log -1 --format='%an <%ae>' 84a81304…` vs `kama-shokunin <kama@shokunin.local>` | 0 | `AUTHOR_MATCH` |
| `git log -1 --format='%cn <%ce>' 84a81304…` vs same | 0 | `COMMITTER_MATCH` |
| `git diff-tree --no-commit-id --name-status -r 84a81304…` | 0 | `M LOG.md`; `M SCORECARD.md`; `A corpus/lessons/round-4-recensus.md` |
| `git status --porcelain=v1` | 0 | `?? plans/` |
| `git ls-files --others --exclude-standard` | 0 | `plans/wwkd-round-4-recensus.md` only |
| `git diff --exit-code` | 0 | no worktree delta vs HEAD |
| `git diff --cached --exit-code` | 0 | index matches HEAD |
| `git rev-list --left-right --count origin/master...HEAD` | 0 | `0 1` (ahead 1, not pushed) |
| `git -C /home/vgpnk/Projects/shokunin check-ignore -v kama-shokunin` | 0 | `.gitignore:1:*-shokunin/	kama-shokunin` |
| `git -C /home/vgpnk/Projects/shokunin ls-files --error-unmatch kama-shokunin` | 1 | not in parent index |
| `test -f /home/vgpnk/Projects/shokunin/.ufo/reports/round-4/kama.md` | 1 | report file absent |

`git cat-file -p 84a81304d7b0c77c84fe495f3bb728e8729faaff` (headers only):

```
tree 378f6aefe833410d460a0dbb74305e17ece51491
parent ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21
author kama-shokunin <kama@shokunin.local> 1792023336 -0300
committer kama-shokunin <kama@shokunin.local> 1792023336 -0300

round-4: OMP-era freshness re-census (measured gates; records + scoped repair)
```

No gpgsig, no extra header. Reflog `HEAD@{0}` is `commit` of this hash, not an amend.

Worktree blob equality for the three paths: `git rev-parse HEAD:<path>` equals `git hash-object <path>` for each (`a9b2ad80…`, `f05c29a6…`, `21958109…`). File mtimes `2026-10-14 21:15:32 -0300`, four seconds before the commit timestamp. `plans/wwkd-round-4-recensus.md` mtime `20:36:30 -0300`, still untracked.

---

## Operator-identity commits (not the audited object)

Full author census of `git log --all`:

| Count | Identity |
|---|---|
| 5 | `kama-shokunin <kama@shokunin.local>` (seed, round-1, round-2, round-3 `ea72c3e`, round-4 `84a81304`) |
| 2 | `ci <ci@local>` |

`ci <ci@local>` is the host global identity, not the lane identity and not `Joao Pedro Veiga <jpveigao10@gmail.com>`. This fleet treats that default as non-lane / operator-side identity. Both objects are ancestors of `origin/master` (`merge-base --is-ancestor` exit 0). They are historical. They are not `84a81304`.

| Commit | Date | Subject | Paths |
|---|---|---|---|
| `33b167ecccab9059da0c65c3b60d9b19f233ceb0` | 2026-10-13T16:56:38-03:00 | `HOURS.md: craft-hours ledger opened (§Craft-hours canon)` | `HOURS.md`, `LOG.md` |
| `ed135b3cb869c5d8a6c9d3b32dac02fb7e551ebd` | 2026-10-13T17:04:57-03:00 | `Revert "HOURS.md: craft-hours ledger opened (§Craft-hours canon)"` | `HOURS.md`, `LOG.md` |

Counterexample to “these swept a sibling”: both path lists are inside `kama-shokunin` only. Net tree of the pair equals the pre-pair tree: `git rev-parse 83bee7f^{tree}` and `ed135b3^{tree}` are both `be181d4f468f4657989afbdf8bbfd138a0444f36`. `HOURS.md` is not in `HEAD`. `git grep -i HOURS HEAD -- LOG.md SCORECARD.md` finds nothing.

No human-operator (`Joao Pedro Veiga` / `jpveigao10@gmail.com`) commit exists in this repo.

---

## Swept sibling file

None in `84a81304`. None in the two `ci` commits.

Parent embedding check, so a later `git add` in the fleet root is not confused with this commit: `kama-shokunin` matches `.gitignore:1` and is absent from the parent index. This seat did not re-walk parent history for the old gitlink (`17c1fad` / `8afbc8f`); that is not this commit.

`LOG.md` cites `.ufo/waves/shokunin12h-20261014-p1-repair/members/` as text. That string is not a file this commit added. Whether it resolves from the lane root is the record-conformance seat's break, not a sweep.

---

## Tree cleanliness detail

Default porcelain dirt: untracked `plans/` only. That is the allowed exception. The plan file is the lane's own WWKD brief, not a sibling file, and it was not committed.

Ignored, not porcelain dirt (`git status --porcelain=v1 --ignored=matching`):

- `registry/history/.lock`
- `registry/history/20261014T124232Z.json`
- `registry/history/20261014T124525Z.json`

Covered by tracked `registry/history/.gitignore` (`*.json`, `.lock`). Not a cleanliness failure under the stated criterion. Do not `git add -f` them.

Not pushed: `origin/master` is `ea72c3e`. Plan says never push. Ahead-by-1 is compliance, not debt.

Parent fleet working tree is dirty (untracked `.ufo/`, `.omp/`, logs). That is not the kama tree. This seat did not stage or clean it.

---

## Findings by severity

No actionable defect on `84a81304` identity, pathspec, or tree cleanliness.

1. **Low — commit subject overclaims a repair.** Subject says “scoped repair”. Diff is three record files. Lesson says no repair. Owner: whoever writes the next kama subject line. Unblock: do not rewrite `84a81304` (it is the cited identity). A later record may say the round-4 diff was records only.
2. **Info — historical non-lane identity, already net-zero.** `33b167e` and `ed135b3`, `ci <ci@local>`, published on `origin/master`. Owner: none for a rewrite (already on origin; trees match). Unblock: none. Residual: global identity is still `ci <ci@local>`, so the next commit without `-c user.name=kama-shokunin -c user.email=kama@shokunin.local` will not be lane identity.
3. **Adjacent, not an identity failure — round report not filed.** Plan `:19` says file the report with the actual hash. `.ufo/reports/round-4/kama.md` is absent. Owner: parent / record path, not this seat. Unblock: file that report citing `84a81304` if the program still requires it. Do not amend this commit to add the citation.

---

## Residual risk and gaps

- Git does not record whether the invocation was `git commit -- <path>` or a full-index commit that happened to be clean. The file set matches the plan's record trio, `plans/` stayed out, and ignored snapshots stayed out. That is the evidence for pathspec limitation. It is not a stored argv.
- Gates were not re-run here. Identity does not speak to `kama-probe.sh` exit codes.
- `resume_continuity_v1` does not appear in this commit. Not checked; not a kama identity surface.
- Parent-repo dirt and the missing round-4 report were observed, not repaired.
