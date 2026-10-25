# JjRevengerPriorProbe — reverse-engineering the 2026-10-19 jj probe

Scope: the two surviving probe repos under `/home/vgpnk/Projects/shokunin/.tower/jj-probe/`
(`chousa-shokunin`, `kotoba-shokunin`), created 2026-10-19 18:29–18:44. Every jj command in this
investigation ran on `cp -a` copies at `/fast/scratch/jj-wave/JjRevengerPriorProbe-2/probe-copy/`
with `origin` repointed to sandbox bare repos first (`git remote -v` verified). Live probe repos were
read only; a 4,793-file sha256 manifest of `.tower/jj-probe` was taken before and after and is
byte-identical (`diff -q … && echo UNCHANGED` → `UNCHANGED`). Tooling: jj
`0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, git `2.56.0`. No installs were needed.

The probe itself is the direct ancestor of `scripts/hyaku/jj-lane.sh`: every identity/metaedit/undo
behavior encoded in that helper is visible here as a numbered experiment.

---

## 1. Inventory and provenance

Two directories survive; 21 sibling probes named in `.ufo/waves/kaika-w2j/*.md` (audio, game-dev-2d/3d,
kagi, kaidoku, kake, kama, kasegi, kengaku, kimi-shokunin, kotodama, kumitate, lore, mado, mori,
revenger, sentou, souji, tabi, tameshi, tsukuroi) were deleted. Neither survivor has a report in
`.ufo/waves/kaika-w2j/`.

Both are **full clones of the live lane repos** (not worktrees, not `--local`):

```
$ git -C .tower/jj-probe/chousa-shokunin reflog show --all --date=iso | tail -4
ab19cff refs/heads/master@{2026-10-19 18:29:10 -0300}: clone: from /home/vgpnk/Projects/shokunin/chousa-shokunin
ab19cff refs/remotes/origin/HEAD@{2026-10-19 18:29:10 -0300}: clone: from /home/vgpnk/Projects/shokunin/chousa-shokunin
...
$ git -C .tower/jj-probe/kotoba-shokunin reflog show --all --date=iso | head -4
78ee57e refs/heads/master@{2026-10-19 18:29:08 -0300}: clone: from /home/vgpnk/Projects/shokunin/kotoba-shokunin
...
```

- chousa base: `ab19cff` ("Merge remote-tracking branch 'origin/master'", 2026-10-19 17:05).
- kotoba base: `78ee57e` ("Merge remote-tracking branch 'origin/master'", 2026-10-19 17:09).
- `.jj` created in chousa at 18:30:14, in kotoba at 18:33:20 (`stat` on
  `.jj/repo/op_store/operations/*`; both within milliseconds of the first three ops).
- `origin` in both clones still points at the *live* lane paths. No push ever happened: the op logs
  contain no `push`/`fetch` op, and the live lanes have no `*probe*` refs (§7).

Why the copies matter: `.tower/` is excluded in the fleet root's local exclude file, so nothing here
was ever tracked:

```
$ sed -n '8p' .git/info/exclude
.tower/
$ git -C /home/vgpnk/Projects/shokunin log --all --oneline -- .tower | wc -l
0
```

## 2. Chousa — the op log (17 operations, 16 views, 1 op head)

`jj --ignore-working-copy op log` in the copy; newest first, with the recorded argv of each op:

```
@  3e1831711afb  commit 1b2aea926df0e17b48a1e78b57ee37c159acf18d
│                args: jj commit -m 'test5: repo-config identity' jj-probe-scratch5.txt
○  fa47b6a59200  snapshot working copy
│                args: jj status
○  66bb6d42e82f  undo: restore to operation 4c401f7ff223af05…
│                args: jj undo
○  7f074c937ad5  edit commit metadata for commit 11c580f81633…
│                args: jj --config 'user.name=chousa-shokunin' --config 'user.email=chousa@shokunin.local' metaedit --update-author -r jj-probe-test2
○  4c401f7ff223  commit f364fd39f96c7debc85b018c8434c8e50e12c70f
│                args: jj --config 'user.name=chousa-shokunin' --config 'user.email=chousa@shokunin.local' commit -m 'test4: lane identity deterministic' jj-probe-scratch4.txt
○  1398c43ca5f6  snapshot working copy            (same test4 argv)
○  ce2d35632a15  point bookmark jj-probe-test2 to commit 11c580f81633…
│                args: jj bookmark set jj-probe-test2 -r @-
○  570502db4153  commit ad51c712be1b9e16cf7a4b277696d0b7bd91596f
│                args: jj --config user.name/email --config 'git.author={ name="chousa-shokunin", email="chousa@shokunin.local" }' commit -m 'test3: full lane identity probe' jj-probe-scratch3.txt
○  152b37a8cc6c  snapshot working copy            (same test3 argv)
○  e39db2d50f0c  commit fbe95253a9b3f7c510d4532db3e7708ddad27d12
│                args: jj --config 'git.author={…}' --config 'git.committer={…}' commit -m 'test2: jj lane identity both-fields probe' jj-probe-scratch2.txt
○  ff4d1624f6ce  snapshot working copy            (same test2 argv)
○  9e992761cfb6  point bookmark jj-probe-test to commit 5b875ca054bd…
│                args: jj bookmark set jj-probe-test -r @-
○  03ab1a72bfe5  commit 3d54b2209fed3ce03e70de6de2849b6628ebf8f6
│                args: jj --config user.name/email commit -m 'test: jj colocate lane identity probe' jj-probe-scratch.txt
○  ceb8bb70d3ac  snapshot working copy            (same test1 argv)
○  1384873e2c06  import git head                 args: jj git init --colocate
○  faffdc3aba56  import git refs                 args: jj git init --colocate
○  3d3461484bd4  add workspace 'default'
○  000000000000  root()
```

Absolute times from the operation-object mtimes (the op log itself only prints "16 hours ago"):

| time (2026-10-19 -03) | op | meaning |
|---|---|---|
| 18:30:14.772–.781 | 3 init ops | `jj git init --colocate` |
| 18:30:58.467/.471 | snapshot + commit `3d54b22` | test1 |
| 18:30:58.482 | bookmark `jj-probe-test` → `5b875ca` | export check |
| 18:31:36.372/.378 | snapshot + commit `fbe9525` | test2 |
| 18:31:44.787–.803 | snapshot + commit `ad51c71`, bookmark `jj-probe-test2` → `11c580f` | test3 + export |
| 18:40:29.140/.159 | snapshot + commit `f364fd3` | test4 |
| 18:43:41.371 | `metaedit --update-author -r jj-probe-test2` | rewrote `11c580f` → `457d2a4` |
| 18:43:41.397 | `jj undo` → restore `4c401f7` | reverted the metaedit |
| 18:44:35.929 | snapshot (`jj status`) | post-undo inspection |
| 18:44:35.954 | commit test5 → `e5c930a` | repo-config identity |

Note the gap 18:31:44 → 18:40:29 (nine minutes) between test3 and test4/metaedit; the identity work was
not continuous.

## 3. Chousa — what each test demonstrated (observed author/committer)

Resulting git commits, `git log -1 --format='%h A:%an <%ae> C:%cn <%ce> %s'`:

| test | command identity config | commit | author | committer | file added |
|---|---|---|---|---|---|
| 1 | `--config user.name/email` | `5b875ca` | Joao Pedro Veiga | chousa-shokunin | `jj-probe-scratch.txt` |
| 2 | `--config git.author={…}`, `git.committer={…}` | `46d2526` | chousa-shokunin | Joao Pedro Veiga | `jj-probe-scratch2.txt` |
| 3 | `--config user.name/email` + `git.author={…}` | `11c580f` | Joao Pedro Veiga | chousa-shokunin | `jj-probe-scratch3.txt` |
| 3′ | `metaedit --update-author -r jj-probe-test2` | `457d2a4` | chousa-shokunin | chousa-shokunin | (same tree) |
| 4 | `--config user.name/email` | `b397ad5` | chousa-shokunin | chousa-shokunin | `jj-probe-scratch4.txt` |
| 5 | repo config only (no flags) | `e5c930a` | chousa-shokunin | chousa-shokunin | `jj-probe-scratch5.txt` |

The A/C alternation is not noise; it is the whole lesson:

- `--config user.name/email` on `jj commit` sets the **committer** of the exported git commit and the
  author of the **new working-copy commit** that `jj commit` creates — not the author of the commit
  being finalized (test1: A default, C lane).
- test2 produced A=lane because the `@` it finalized was created by test1's `jj commit` under
  `--config user.name=chousa-shokunin`; its C went back to the default because test2 passed no
  `user.name`. `git.author`/`git.committer` are **not jj config keys** (the `--include-defaults` list
  contains no such keys; jj accepted them silently and ignored them).
- test3 therefore finalized an `@` created by test2 (default identity) → A default; its own
  `user.name` made C lane and seeded the next `@` with lane identity.
- test4 is A+C lane because its `@` was created by test3's commit under the lane identity. test5 is
  A+C lane for the same inherited reason plus the repo-config committer.

The sequence is reproduced exactly by a controlled experiment on a fresh sandbox repo (jj 0.45.1):

```
T1 A:Joao Pedro Veiga <…> C:Joao Pedro Veiga <…>   # default
T2 A:Joao Pedro Veiga <…> C:Lane <lane@x>          # --config user.name/email
T3 A:Lane <lane@x>        C:Joao Pedro Veiga <…>   # git.author/git.committer: inert
T4 A:Joao Pedro Veiga <…> C:Lane2 <lane2@x>        # repo config set, existing @ unchanged
T5 A:Lane2 <lane2@x>      C:Lane2 <lane2@x>        # after jj new under Lane2
```

`jj config set --repo user.name Lane2` prints the warning that matters for the helper:

```
Warning: This setting will only impact future commits.
The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>".
```

[INFERENCE] test5's name "repo-config identity" overstates what it isolates: the author was already
lane identity from test4's `@`, so it proves the repo-config **committer** path and that repo config
keeps future `@`s correct, not that repo config alone repairs an existing `@`. Repo config alone would
have required `jj new` or `metaedit --update-author` first (T4 vs T5 above). `scripts/hyaku/jj-lane.sh`
already does the metaedit in `cmd_commit`, which is the correct fix.

## 4. Metaedit + undo: a cited hash is rewritten, then orphaned

`metaedit --update-author -r jj-probe-test2` rewrote the already-exported bookmark tip `11c580f` into
`457d2a4`: same tree, same parent, only the author header changed.

```
$ git rev-parse 11c580f^{tree} 457d2a4^{tree}
c5cae55afbec58bf110354b8047e402a28769456
c5cae55afbec58bf110354b8047e402a28769456
$ git diff --stat 11c580f 457d2a4        # (no output)
```

`jj undo` then restored the repo to op `4c401f7` (the test4 commit): the bookmark `jj-probe-test2`
went back to `11c580f`, but `457d2a4` did not disappear — it is still reachable through
`refs/jj/keep/457d2a419233…` (and still shows in `git log --all`). This is the concrete evidence
behind the fleet invariant "a cited hash must never be amended": jj will happily rewrite a hash that a
report could already have cited, and undo restores refs without removing the rewritten object.

[INFERENCE] the undo at 18:43:41 was a reaction to exactly that risk (metaedit had just changed the
hash of a bookmark that was already exported to git at 18:31:44), not a planned part of the identity
test.

## 5. Scratch files — pathspec-limited commits, one file per commit

Contents are trivial payloads: `jj probe scratch file`, `… v2`, `… v3`, `… v4`, `v5`.

Every commit adds exactly one path (`git diff-tree --no-commit-id --name-status -r <c>`):

```
3d54b22 A jj-probe-scratch.txt     (pre-description snapshot of 5b875ca)
5b875ca A jj-probe-scratch.txt
46d2526 A jj-probe-scratch2.txt
11c580f A jj-probe-scratch3.txt
b397ad5 A jj-probe-scratch4.txt
e5c930a A jj-probe-scratch5.txt
```

Parent chain (post-undo, branch-visible): `5b875ca → 46d2526 → 11c580f → b397ad5 → e5c930a`, and the
final tree contains all five files (`git ls-tree -r --name-only e5c930a | grep jj-probe` → 5 lines).
So the probe demonstrated that `jj commit -m … <path>` is pathspec-limited: committing scratch4 left
scratch5 (created later) out, and each intermediate commit stayed a clean ancestor chain.

The `@` after the last commit is `6fd2908` — empty, no description — and is *not* on any branch; git
HEAD is `e5c930a` (`@-`). That is the hash a lane would cite.

## 6. Git-visible state after the probe

```
$ cat .git/HEAD                      # raw hash → detached
e5c930a423e9a85ec15d3695a3ff15af26b86032
$ git rev-parse --abbrev-ref HEAD
HEAD
$ git rev-parse @{u}
fatal: HEAD does not point to a branch
$ git rev-parse master
ab19cff53c0d4c1254d9d877a616e0cdbc3de993
$ git branch -vv
* (HEAD detached from refs/heads/master) e5c930a test5: repo-config identity
  jj-probe-test  5b875ca test: jj colocate lane identity probe
  jj-probe-test2 11c580f test3: full lane identity probe
  master         ab19cff [origin/master] Merge remote-tracking branch 'origin/master'
```

- Bookmark→branch export works: `refs/heads/jj-probe-test` and `refs/heads/jj-probe-test2` exist and
  resolve. `master` was never advanced by jj.
- The index matches HEAD exactly: all five scratch files are at stage 0 with the same blob ids as the
  HEAD tree, and `git status --porcelain` is empty.
- **refs/jj/keep noise:** 21 keep refs in chousa. `git rev-list --count --all` = 117 vs
  `git rev-list --count master` = 97. `git log --all` therefore shows the messy rewrite graph
  (empty-message snapshot commits, rewritten test3 twin, current empty `@`).

## 7. Kotoba — an init-only probe on the largest lane

Op log has exactly three ops, 18:33:20.983–.996 (2–5 ms each), and nothing after:

```
77c53c338c96  import git head   args: jj git init --colocate   (lasted 5 ms)
c9c73333d21f  import git refs   args: jj git init --colocate
c38fdcccf239  add workspace 'default'
```

- 9,892 tracked files, 110 commits on `master`; `.jj` 944 K; `.jj/working_copy/tree_state` 818,558 B.
  tree_state materialized at 18:33:21.127; config written at 18:33:21. [INFERENCE] init wall time
  ≈150 ms, from the op/file mtimes; the probe's point looks like a scale check on the biggest lane.
- `master` bookmark stays at `78ee57e`; `git status` clean; no branches or identities written.
- Two synthetic commits exist in `.git` purely from init, both held by `refs/jj/keep`:
  - `769ce8c` — jj's rewrite of HEAD `78ee57e` with a `change-id rykxslmz…` header, empty diff vs its
    parent; this is jj's `@` (`jj log` prints `@ = 769ce8cc (empty)`);
  - `53ab7a3` — a parentless root commit with the **empty tree** (`4b825dc…`) and `change-id rxnx…`,
    i.e. the initial working-copy commit abandoned when HEAD was imported.
  The same abandoned-empty-root pattern reproduces in a fresh sandbox repo (`9840d86`, tree
  `4b825dc…`, no parent) after `jj git init --colocate` → it is an init artifact, not probe damage.
- Config for live kotoba (`~/.config/jj/repos/3ce4bddc93d8053821ec/config.toml`, mtime 18:33:21)
  contains only `trunk() = master@origin`; no `user.*`. Consistent with zero commits.

## 8. Per-repo config lives outside the repo (correction to the kaika report)

`.jj/repo` contains **no** `config.toml`. `jj config path --repo` resolves to the user config tree,
keyed by a hash of the absolute repo path:

```
$ jj config path --repo
/home/vgpnk/.config/jj/repos/<16-hex>/config.toml
```

- Live chousa config (`9abecfe1ed81c6829735`, config.toml mtime **18:44:35**, i.e. exactly test5):

```
[revset-aliases]
"trunk()" = "master@origin"
[user]
name = "chousa-shokunin"
email = "chousa@shokunin.local"
```

- `~/.config/jj/repos/<id>/metadata.binpb` stores the repo's absolute path
  (`strings` → `/home/vgpnk/…/.tower/jj-probe/chousa-shokunin/.jj/repo`).
- Copy/move behavior: the first jj command in the `cp -a` copy printed
  `Warning: Your repo appears to have been copied from … The corresponding repo config file has also
  been copied.`, rewrote `.jj/repo/config-id` **inside the copy**, and created a new
  `~/.config/jj/repos/<new-id>/config.toml` with the source identity. This happened even for
  `jj --ignore-working-copy op log`; i.e. after a move, a nominally read-only jj call is not
  filesystem-read-only.
- Cleanup debt already visible on the host: **25** `~/.config/jj/repos/*` dirs (2.3 MB) carry
  `.tower/jj-probe` paths — most belong to probes deleted in the kaika W2j wave. Deleting a probe
  directory does not delete its jj repo config.

This directly contradicts `.ufo/waves/kaika-w2j/revenger.md` §4 ("`jj config set --repo …` writes
`.jj/repo/config.toml`, repo-local"). Under jj 0.45.1 the value is stored per host path, not in the
lane repo; a lane repo copied/rsynced to another host or path loses the binding (jj re-creates it only
through its copy-detection, which relies on the old config dir still existing).

## 9. Git index / HEAD mechanics (refinement of the phase-2 claim)

`PHASE2.md` says "jj resets the git index on every mutation". Measured behavior is narrower:

- Snapshot-only command (`jj status`) on staged state left the index intact:
  `M  base.txt`, `A  f6.txt` before and after.
- HEAD-moving command (`jj commit <path>`) reset the index to the new HEAD: a staged modification to a
  file **outside** the pathspec became unstaged (` M`, `git diff --cached` empty), while the content
  remained in jj's `@` (`jj diff --stat` still showed it). Untracked paths committed by jj appear in
  the index with the HEAD blob.
- `jj new` collapsed staged content into the previous `@` commit; afterwards `git status` was clean
  and the content was present in git HEAD.

So the git-index staging boundary is destroyed by commit/new (all content is snapshotted and then
exported), not by every jj invocation. The practical rule is unchanged — no `git add`-based workflow
inside a colocated lane — but the reason should be stated correctly.

## 10. Fleet history search

- `git -C /home/vgpnk/Projects/shokunin log --all --oneline -- .tower` → **0 lines** (`.tower/` is in
  `.git/info/exclude:8`).
- `grep -rn 'jj-probe' .ufo/reports LOG.md` → **0 hits**;
  `grep -rn 'chousa-shokunin\|kotoba-shokunin' .ufo/waves/kaika-w2j` → **0 hits**.
- `git log --all --oneline -S'.tower/jj-probe'` → 3 commits:
  - `7ba8d97` (2026-10-19 19:03) — the kaika W2j evidence commit (21 probe reports + JJ-ADOPTION).
    It mentions `.tower/jj-probe` generally but contains **no** report for chousa or kotoba:
    `git grep -n 'jj-probe/chousa\|jj-probe/kotoba' 7ba8d97 -- .ufo` → nothing.
  - `67a3123` (2026-10-20 11:11) — `jj-lane.sh` + this jj-w1 wave spec (this task).
  - `bee791e` (2026-10-20 11:12) — `PHASE2.md`, whose only reference is: "Prior jj state: tameshi and
    mado already carried `.jj/` from 2026-10-19 …; `.tower/jj-probe/` holds an earlier probe."
    Verified: among live lanes only `mado-shokunin/.jj` and `tameshi-shokunin/.jj` exist; live chousa
    and kotoba have no `.jj`.

Net: the prior probe is essentially undocumented. The artifacts are the only record; PHASE2's
one-liner is the only prose that acknowledges it.

## 11. Live-side safety check

- 4,793-file sha256 manifest of `.tower/jj-probe` before/after this investigation: `UNCHANGED`.
- No jj `push`/`fetch` op exists in either probe, and the probe op logs never mention the remote.
- Live chousa: HEAD `d730ae4`, `git branch -a --list '*probe*'` empty. Live kotoba: HEAD `c61a973`,
  no probe refs. Both HEADs moved past the probe bases (`ab19cff`/`78ee57e`) because rounds kept
  landing; nothing from the probe reached them.

## 12. What was learned (and what the helper already encodes)

1. Author is fixed when `@` is created; `jj commit` finalizes that author. `--config user.name/email`
   at commit time fixes only the committer and seeds the *next* `@`. `jj-lane.sh`'s
   `metaedit --update-author` before every content commit is the correct fix.
2. `git.author` / `git.committer` are inert keys in jj 0.45.1 — passing them (as test2/test3 did) is a
   no-op.
3. `metaedit --update-author` rewrites a commit hash even after bookmark export; `jj undo` restores
   refs but leaves the rewritten object under `refs/jj/keep`. Never amend a hash that may be cited.
4. Bookmark→branch export is immediate and reliable; the working branch itself is not advanced.
   `jj commit`/`new` detach git HEAD at `@-`; `@{u}` and `--abbrev-ref HEAD` break while
   `git rev-parse <branch>` works.
5. Colocated housekeeping refs (`refs/jj/keep/*`) inflate `git log --all` / `rev-list --all`
   (chousa: 21 refs, 117 vs 97 commits). Fleet tools must use `refs/heads/<branch>`.
6. Repo config is host state keyed by absolute path, not lane-repo state; copying/moving a lane
   triggers copy detection that writes a new config dir and rewrites `.jj/repo/config-id`.
7. Colocation is cheap at scale: 9,892 files → `.jj` 944 K, tree_state 818 K, init ops in the
   millisecond range.
8. Git staging is destroyed by HEAD-moving jj ops (commit/new), not by snapshots; content is preserved
   in jj's `@`/commit.

## 13. Recommendations

- **Keep the helper's metaedit-before-commit.** Add a cheap post-commit assertion:
  `jj --ignore-working-copy log -r @- -T 'author.email() ++ " " ++ committer.email()'` compared to
  `<id>@shokunin.local`, failing hard on mismatch. The probe shows how easily a missing metaedit slips
  through when `@` was created under a different identity.
- **Do not add `git.author`/`git.committer` anywhere** (in the helper, docs or closure prompt); they
  do nothing under 0.45.1 and create a false sense of identity control.
- **Treat `jj config set --repo` as host state.** Document that lane identity lives in
  `~/.config/jj/repos/<hash>/config.toml`; re-run `jj-lane.sh init` after any move/copy; expect the
  "repo appears to have been copied" warning; never assume `.jj/` carries identity to another path.
  Optionally have `init` print `jj config path --repo` so the binding is visible.
- **Add a teardown cleanup** for `~/.config/jj/repos/<id>` when a probe/lane directory is deleted.
  25 stale dirs (2.3 MB) from the kaika wave already demonstrate the leak; `metadata.binpb` (repo
  path) makes them safely identifiable.
- **Never amend after a report cites a hash** — the existing invariant is correct and now has direct
  evidence (11c580f → 457d2a4 + keep ref). If identity is wrong after a push, land a follow-up commit;
  do not metaedit the cited one.
- **Fleet scanning must ignore `refs/jj/keep/*`** (`git rev-list --all` is not "all lane commits" in
  a colocated repo). Use `refs/heads/<branch>` / `git rev-list <branch>`.
- **Keep the git-index prohibition but state it precisely**: HEAD-moving jj ops flatten staged state;
  snapshot-only reads do not. The helper's `state` (pure git, read-only) remains safe.
- **Probe hygiene**: the two survivor dirs and their host config entries are the only record. If they
  are deleted, capture `jj op log` and `git for-each-ref refs/jj/keep` first (the op log argv is the
  only exact command record; nothing in `.ufo/` reproduces it).
- Documentation fix: `.ufo/waves/kaika-w2j/revenger.md` §4's "repo-local `.jj/repo/config.toml`"
  claim should be corrected wherever the fleet relies on it.

## 14. Cleanup

Sandbox `/fast/scratch/jj-wave/JjRevengerPriorProbe-2/` (copies, bare remotes, controlled experiment,
checksum manifests) was removed after this report. The three host config dirs created by running jj in
the moved copies (`b2d152…` chousa copy, `4419a5…` kotoba copy, `e84080…` experiment) were removed too;
the pre-existing probe dirs and their original `9abecfe…`/`3ce4bdd…` config entries were left untouched.
