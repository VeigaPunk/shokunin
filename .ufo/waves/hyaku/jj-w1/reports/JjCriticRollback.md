# JjCriticRollback: attack on the jj transition and rollback story

Seat: JjCriticRollback-2 (critic, leaf). jj 0.45.1-7c41cdeb, git 2.56.0.
Sandbox: `/fast/scratch/jj-wave/JjCriticRollback-2/`.

How the tests ran:
- Every jj call ran inside the sandbox with `XDG_CONFIG_HOME=$SB/xdg` and `HYAKU_STATE=$SB/state`. The user jj config was copied in (`git.auto-local-bookmark = true`, `ui.default-command = "log"`) and so was the global git config (identity `ci <ci@local>`).
- After the runs I checked every `~/.config/jj/repos/*/metadata.binpb`. None references this sandbox, so jj wrote no config outside it.
- The helper under test is a byte-identical copy: `sha256 2479041653c6…dc2b1d` for both the live and sandbox `jj-lane.sh`.
- Each scenario uses its own bare `remote.git`. `mk()` aborts unless `git remote get-url origin` is under `$SB`.
- Live repos were read only, with `git log|status|diff|rev-parse|symbolic-ref`, `cat`, `ls` and `strings`.
- Scripts are kept in the sandbox (`t*.sh`, `env.sh`). Each finding below names the script that reproduces it.

## Severity summary

| # | Scenario | Failure observed | Sev |
|---|---|---|---|
| F1 | mid-round colocation of a diverged lane | helper exits 0 after a **sideways push that deletes an operator commit from the remote** | critical |
| F2 | mid-round: staged entries | `init` silently unstages them | high |
| F3 | mid-round: merge in progress | `init` deletes MERGE_HEAD and the conflict stages; conflict markers become ordinary content | high |
| F4 | mid-round: HEAD on a side branch | lane work is pushed to a new remote branch `wip` (exit 0), then exit 3 forever | high |
| F5 | mid-round: detached old HEAD | `bookmark set failed` (exit 1); the commit is stranded in jj | medium |
| F6 | raw `git commit` in a colocated lane | helper ships `ci <ci@local>` commits silently (identity invariant broken) | high |
| F7 | raw `git add` + helper | staged entries destroyed; the L1's later `git commit` exits 1 | medium |
| F8 | raw `git commit --amend` / `git fetch` | divergent change or sideways bookmark → `bookmark set failed` exit 1 | medium |
| F9 | seat `jj commit -m` with no paths | helper ships the **operator's personal name/email** plus a half-edited LOG.md, exit 0 | critical |
| F10 | seat `jj new` | push refused ("no description"); exit 3 until a manual squash | medium |
| F11 | seat plain `jj`/`jj st` | forks the op log (2 reconciles in a 10-commit race); index kept; no damage seen | low |
| F12 | two helper writers (`.` vs absolute path) | 10 reconciles, 10 divergent commits, **5/12 files never pushed, all 12 calls exit 0, wrong hashes cited** | critical |
| F13 | concurrent git holds `index.lock` | "nothing to commit", then `push` prints `pushed <seed hash>` exit 0 → false provenance | high |
| F14 | op-log fork → `master??` | `jj-lane.sh state` blind (ahead=0); `push` cannot heal (divergent change id) → exit 3 forever | medium |
| F15 | backout | recipe below verified; `jj git colocation disable` destroys the git checkout | n/a |
| F16 | rollback switch | `HYAKU_VCS=git` does not revert the addendum or closure prompt text (static) | medium |
| F17 | operator push, then `master??` | normal case recovers correctly | ok |
| F18 | operator **force-rewind** | helper re-publishes the dropped commit verbatim, exit 0 | high |

## Findings (observed)

### A. A lane mid-round when colocation starts (`init` on a git-era lane state)

**F1: first colocation of a diverged lane pushes sideways and erases the operator's commit.** (`t1h.sh`; also `t1b.sh` T1d)

Setup: the operator pushed `OPF.md`. The lane has 1 unpushed raw git commit and ran `git fetch` (behind 1, ahead 1). Then `jj-lane.sh init` and `jj-lane.sh commit`:
```
state branch=master local=16e24a88… remote=86aea2bb… ahead=1 behind=1 head=attached …   ← init prints the divergence and proceeds
pushed d7a7125edb118925e471f95d1f653213c9e13f75
helper exit=0
OPERATOR COMMIT 86aea2bb7bd5e6c71e42171b7284f704dce3ef76 OVERWRITTEN
d7a7125 kake-shokunin r1: X / 16e24a8 kake-shokunin L1 raw unpushed / 5b8966e seed seed
```
`jj git push --dry-run` from the same state (`t1g.sh`) names the mechanism:
```
bookmark: master [move sideways from c9728650cabc to 71f4872534dc]
```
- `jj git push` checks only a lease against its last-known `master@origin`. It does not require a fast-forward.
- On the first import jj has no older remote view to compare against. So the diverged local bookmark is never marked conflicted, and the lease matches the remote.
- The T1d variant (`git pull` stopped by a merge conflict) overwrote the operator commit the same way: `operator commit NOT ancestor of remote master (overwritten)`.
- Kept as evidence: `$SB/t1h`, `$SB/t1d`.

Negative control (`t2m.sh`): in a lane that was **already** colocated, raw git commits plus an operator push plus a raw `git fetch`, followed by `jj-lane.sh push`, kept the operator commit (`operator commit kept`). jj imported both moves as a bookmark conflict and rebased. The hazard exists only at first colocation.

**F2: init unstages L1 work.** (`t1.sh` T1a)
```
-- before init:  M  a.txt / A  staged.txt / ?? scratch.txt
-- after init:    M a.txt / ?? scratch.txt / ?? staged.txt
```
`jj git init --colocate` resets the index. The file bytes survive, but the staging intent is lost.

**F3: init erases an in-progress merge.** (`t1b.sh` T1d)
```
-- before:  UU a.txt   .git/MERGE_HEAD
-- after init:  M a.txt   ls: cannot access '.git/MERGE_HEAD'   git ls-files -u … 0
@ … conflict=false
```
The conflict markers are now ordinary content of a non-conflicted @. A later `jj-lane.sh commit -- a.txt` would commit them.

**F4: HEAD attached to a side branch at init.** (`t1.sh` T1b)
- `detect_branch` prefers an attached HEAD, so init sets `trunk()` to `wip@origin` ("Revision `wip@origin` doesn't exist") and tracks nothing.
- The first commit pushes a **new remote branch** and exits 0:
  ```
  pushed 855719ab…   exit=0
  refs/heads/master 6d8e3cf seed
  refs/heads/wip 855719a r1: lane
  ```
- After the first jj mutation HEAD is detached, so the next commit resolves `master`:
  ```
  Error: Non-tracking remote bookmark master@origin exists …   exit=3
  state … ahead=3
  ```
  The retry loop cannot fix this. The closure check `merge-base --is-ancestor 855719ab master` would fail.

**F5: detached HEAD on an old commit at init.** (`t1.sh` T1c)
```
Parent commit (@-) : svvsyqrl b5899feb r1: lane
jj-lane: bookmark set failed      exit=1
```
The commit exists only in jj, as a sideways sibling of `master`.

Negative (`t1b.sh` T1f): moving the repo or reaching it through a symlink keeps the repo config, because `config-id` is unchanged. `cp -a` copies receive a fresh config-id (the live `~/.config/jj/repos` metadata shows `JjRevengerLaneJjState/mado` with its own id).

### B. An L1 that still runs raw `git commit` in a colocated lane

**Live instance (read-only):**
```
$ git -C mado-shokunin symbolic-ref -q HEAD   → refs/heads/master   (.jj present, 21 refs/jj/keep/*)
$ git -C mado-shokunin log origin/HEAD..HEAD  → 8 commits, mado-shokunin <mado@shokunin.local>, 15–33 min ago, round-17
$ grep -c 'jj-lane.sh commit' .ufo/prompts/mado-round-17.md → 0
```
The prompt was committed at 10:51 (`5a228cd`); the jj addendum landed at 11:11 (`67a3123`). [INFERENCE] mado's round-17 L1 is a git-era L1 making raw git commits in a colocated lane. The helper detaches HEAD on every commit (T1a: `HEAD: detached`), so an attached HEAD with 8 new commits means none of them went through the helper. This matches the steady-state case of `t2m.sh` (which recovered fine). It is not the F1 case, because `.jj` already exists.

**F6: helper silently publishes foreign-identity raw commits.** (`t2.sh` T2a; kept at `$SB/t2a`)
```
git commit exit=0 HEAD=detached
fatal: You are not currently on a branch.          ← raw `git push` fails
pushed 9c17242c…                                    ← next helper commit
9c17242 kake-shokunin <kake@shokunin.local> r1: two
f0266d2 ci <ci@local> raw L1 commit                 ← global git identity, now on the remote
```
The official selftest case `i git-commit-import` **asserts this behaviour**: it commits as `op <op@x>` and passes when that commit reaches the remote.

**F7: staged entries destroyed.** (`t2.sh` T2c)
```
-- staged: STAGED.md   →  (helper commit B.md)  →  -- staged after helper: []
nothing added to commit but untracked files present …   git commit exit=1
```

**F8: amend of a cited commit, or a raw fetch.**
- `git commit --amend` of the cited, pushed `0be36b0` produced a divergent change, and the next commit failed. The cited hash stays an ancestor, but the lane is stuck. (`t2.sh` T2d)
  ```
  a0049ac6 zxtlsyqkqmtv  r1: one (amended)
  0be36b0d zxtlsyqkqmtv master r1: one
  zxtlsyqkqmtv divergent
  jj-lane: bookmark set failed   exit=1
  cited still ancestor of remote master
  ```
- Raw `git fetch` after an operator push in a colocated lane (allowed by `lane-addendum.md:128-131`): the local `master` follows the remote, @'s base is stale, and the commit fails with `jj-lane: bookmark set failed` (exit 1). The operator commit is kept. (`t6.sh` T6c)

### C. A seat that runs jj without `--ignore-working-copy`

**F11: plain `jj` or `jj st` snapshots and forks the op log.**
- `t3.sh` T3a: the index is kept (`A  STAGED.md;M  a.txt;` before and after a bare `jj`), but the op log gains `snapshot working copy`.
- `t3r.sh` ran 60 unlocked `jj st` calls while the helper made 10 commits:
  ```
  -- reconcile ops: 2    -- divergent: []    -- exits: 10 exit=0    (all 10 files on remote)
  ```
  The fork is real; this run did no damage.

**F9: a seat's `jj commit -m` (no paths) right after init publishes the operator's personal identity.** (`t3b.sh` T3b2; kept at `$SB/t3b2`)
```
pushed 483052011d65…   helper exit=0
4830520 kake-shokunin <kake@shokunin.local> "r1: X only"
08c5d35 Joao Pedro Veiga <jpveigao10@gmail.com> | committer kake-shokunin "seat wip"
   seat wip: LOG.md          ← half-edited LOG.md, not in the helper's pathspec
```
- Init's own output warns about this and leaves it in place: `The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>"`.
- The @ created at colocation carries the user-level identity.
- `metaedit --update-author` runs only on the @ that the helper itself splits.

**F10: seat `jj new`.** (`t3.sh` T3b)
```
jj-lane: push failed after 3 attempts: Error: Won't push commit ed2b8ee281ad since it has no description
```
Exit 3 repeats forever. The recovery below was verified (`t3b.sh` T3b3).

Also (`t3.sh` T3c): a raw `jj git init --colocate` tracks scratch (` A .seat/scratch.log; A notes.tmp;`). A later helper `init` only warns.

### D. Op-log divergence after two concurrent writers

**F12: the lock key is `basename "$dir"`, so `.` and the absolute path take different locks.** (`t4e.sh`; kept at `$SB/t4e`)

Six rounds of `commit .` against `commit $L` running in parallel:
```
$STATE: jj-lane.lock  jj-..lock
-- reconcile ops: 10      -- divergent: 10 commits
-- remote has: 7 of 12 lane commits
a1.out … b6.out: all "pushed <hash> exit=0"
MISSING on remote: A1.md A2.md A4.md B5.md B6.md
```
`a1.out` cites the other writer's commit as its own:
```
Parent commit (@-) : wxoxxnsu 0875d0ff r1: A1
committed 3b99fd180e72…   ← this is "r1: B1"
pushed 3b99fd180e72…
```
The lost changes remain on disk and in @ (`A A1.md … A B6.md`). After the race, `jj-lane.sh commit … -- A1.md A2.md A4.md B5.md B6.md` pushed them all. The round's citations were already wrong by then.

**F13: a concurrent git process holding `.git/index.lock` leads to a false "pushed".** (`$SB/t1e3`)
```
nothing to commit                                   ← jj diff failed; stderr is dropped and the failure reads as an empty diff
jj-lane: push failed after 3 attempts: Error: Failed to reset Git HEAD state … Could not acquire lock for index file
helper exit=3
-- lock released, helper push:
pushed 768416c0ca47…  push exit=0                   ← 768416c = "seed"; Y.md was never committed
```
An L1 following the exit-3 instruction (`jj-lane.sh push`) would cite a hash that does not contain its work.

**F14: an op-log fork produces a conflicted bookmark.** (`t4b.sh`, `t4c.sh`)

A seat writer started from the same op (`--at-op`) and described @ and moved `master`:
```
Concurrent modification detected, resolving automatically.
7287fdf1 skmlppvm master?? DIVERGENT seat note
29cef0a5 skmlppvm master?? master@git master@origin DIVERGENT r1: two
state … ahead=0 behind=0                  ← pure-git state cannot see the conflict (refs/heads/master stays at last export)
```
- A following `jj-lane.sh commit` heals it, because `bookmark set` resolves the conflict.
- `jj-lane.sh push` (the exit-3 path and the `inline.sh verify` durability push) cannot heal it:
  ```
  jj-lane: push failed after 3 attempts: Error: Bookmark master is conflicted   push exit=3
  $ jj --ignore-immutable rebase -b <change_id> -d master@origin
  Error: Change ID `vsxykwnz…` is divergent
  ```
  `tip` is selected by `change_id`, which is ambiguous here, and the seat's commit is `heads(master@origin..bookmarks(master))`.
- Recovery, verified:
  ```
  jj --ignore-working-copy bookmark set master -r master@origin
  jj --ignore-working-copy abandon <stray commit_id>
  jj-lane.sh push <lane>      → pushed 564c92de… exit=0
  ```
- Immutability held. A seat's `describe -r @-` on a pushed commit is blocked with `Hint: This operation would rewrite 1 immutable commits.` (`t4.sh`).

### E. Backing jj out of a lane with git history intact (`t5.sh`)

Facts after colocation and two helper commits:
- the local git config diff is empty;
- `.git/info/exclude` is unchanged;
- jj added 12 `refs/jj/keep/*` refs;
- HEAD is detached, and `@{u}` fails with `fatal: HEAD does not point to a branch`;
- the repo config lives in `$XDG_CONFIG_HOME/jj/repos/<config-id>/`, not in `.jj`.

Recipe, verified end to end:
```
jj-lane.sh state <lane>                                   # must show ahead=0 (push first)
jj --ignore-working-copy log --no-graph -r '~::(bookmarks() | remote_bookmarks() | tags()) ~ @ ~ root()' \
   -T 'commit_id.short()++" "++description.first_line()++"\n"'   # jj-only commits: save or push them first
id=$(cat .jj/repo/config-id)
rm -rf .jj
git symbolic-ref HEAD refs/heads/<branch>                 # reattach without touching the worktree
git reset -q                                              # rebuild the index from HEAD; worktree untouched
git for-each-ref --format='delete %(refname)' refs/jj/ | git update-ref --stdin
rm -rf ~/.config/jj/repos/$id
```
Result:
```
-- HEAD: refs/heads/master @{u}: origin/master  (pre: origin/master)
-- status now == status pre-jj:  M a.txt / ?? scratch.txt
-- ahead/behind: 0 0   fsck exit=0
-- plain git round-trip: deb327a r2: three (git)
```
- In `$SB/t4e` the inventory revset lists exactly the race-orphaned commits, for example `0875d0ff8148 r1: A1 files=A1.md`.
- Each orphan is held only by a `refs/jj/keep/*` ref (`keep-ref for lost A1 commit: 1`). Running the recipe without the inventory step makes them gc-able.
- `jj git colocation disable` is **not** a rollback (`t5.sh` T5d): it reports `Workspace successfully converted into a non-colocated …`, after which `ls -a` shows no `.git` and `git status` gives `fatal: not a git repository`.

**F16: rollback switch (static, read-only).**
- `hyaku.env:10 HYAKU_VCS=jj` gates only `lane_vcs_init` (`inline.sh:38-41`).
- `lane-addendum.md:117-135` and `closure-prompt.md:24-54` hard-code `jj-lane.sh commit` and "never git commit".
- On a backed-out lane the helper fails with `not jj-colocated (run: jj-lane.sh init <dir> <id>)`, which invites the L1 to re-colocate.
- `inline.sh:119` chooses jj or git push from the presence of `.jj`, which is consistent with a per-lane backout.

### F. A conflicted branch bookmark after an operator push (`t6.sh`)

**F17: normal case (ok).**
- Setup: a lane commit was left unpushed (exit 3), then the operator pushed `master` and `hotfix`, then `jj git fetch`:
  ```
  bookmark: hotfix@origin [new] untracked
  master (conflicted): - r1: one  + r1: two  + operator hotfix
  git view: refs/heads/master=bfb1af0 origin/master=93fde5f    state … ahead=1 behind=1
  ```
- `jj-lane.sh push` → `pushed 10968142…` exit 0, with history `r1: two → operator hotfix → r1: one`.
- The pre-recovery `committed bfb1af00` hash was rewritten (to 1096814). Only the pushed hash is citable, which is what the protocol already requires.

**F18: the operator force-rewinds a pushed lane commit; the helper re-publishes it.** (kept at `$SB/t6b`)
```
pushed bad=ed62eeae…
operator rewound remote to: 171ad87 r1: one
pushed 56b81a78…   push exit=0
56b81a7 r1: three / ed62eea r1: bad (operator will drop) / 171ad87 r1: one
```
`master@origin..bookmarks(master)` contains the dropped commit, and `rebase -b` is a no-op for it because its parent is unchanged. It goes back to the remote with the same hash.

## Guard trial (sandbox copy only; live helper untouched)

`$SB/patched/jj-lane.sh` is the live helper plus `$SB/guards.diff` (144 diff lines). Changes:
- the lock key is the physical path;
- `init` refuses first colocation on MERGE_HEAD, CHERRY_PICK_HEAD or REVERT_HEAD, a rebase in progress, staged entries, a detached HEAD, HEAD ≠ `origin/HEAD`, or ahead>0 && behind>0;
- `init` runs `jj metaedit --update-author` on @ after the repo config is set;
- a failing `jj diff` is an error;
- when `bookmark set` fails, `rebase -s <new> -d <branch>` and retry;
- `push` has four gates:
  - fast-forward: `<b>@origin ~ ::bookmarks(exact:"<b>")` must be empty;
  - identity and description: everything in `<b>@origin..<b>` must be by the repo user.email or protocol and have a non-empty description;
  - rewind: the last pushed tip, recorded in `$STATE/jj-<key>.pushed`, must be an ancestor of the remote after fetch;
  - a divergent tip is refused;
- after the push, the own change id must be in `::<b>@origin`.

The same scenario scripts were re-run with `HOVR=$SB/patched/jj-lane.sh PFX=P_`:

| Case | Patched result |
|---|---|
| F1 T1h | `jj-lane: master has diverged from origin/master: rebase it first (jj would push it sideways)`, init exit=1, operator commit kept |
| F2 T1a | `staged git index entries would be destroyed by jj` (index intact: `M  a.txt / A  staged.txt`) |
| F3 T1d | refused; `.git/MERGE_HEAD` and the 3 conflict stages kept |
| F4 T1b | `HEAD is on 'wip', lane branch is 'master'`; remote has only `master` |
| F5 T1c | `detached git HEAD: check out master before colocating` |
| F6 T2a | `refusing to publish commits without lane identity or description: 5f60ef394bb4 ci@local`; recovery `jj --config user.name=kake-shokunin --config user.email=kake@shokunin.local metaedit --update-author -r <c>` + `push` → `0a32f15 kake-shokunin … raw L1 commit` |
| F8 T2d | auto `rebase -s` → `pushed 72132bd3…`, cited hash still an ancestor |
| F8 T6c | auto `rebase -s` → pushed; operator commit kept |
| F9 T3b2 | "seat wip" now authored `kake-shokunin <kake@shokunin.local>`. **Residual:** LOG.md is still shipped; the pathspec rule is not enforceable against a seat's correctly-identified `jj commit` |
| F12 T4e | `remote has: 12 of 12`, `reconcile ops: 0`, divergent: none |
| F13 T1e | `jj-lane: jj diff failed: Error: Failed to reset Git HEAD state` (exit 1, no false "nothing to commit") |
| F14 T4c | `unpushed master target … is divergent (concurrent jj writer): resolve with jj bookmark set / jj abandon` (exit 3, explicit) |
| F17 T6a | still recovers: `pushed 33ad8a5…` |
| F18 T6b | `origin/master no longer contains last pushed cd164e2e… (operator rewind): not re-publishing`; operator recovery verified: `jj rebase -s <keep> -d master@origin; jj abandon <dropped>; jj bookmark set master -r <keep>`; acknowledge by writing the remote tip to `$STATE/jj-<key>.pushed`; `push` → `369859d r1: three / 4bf7027 r1: one` |

Official selftest, run on a `git clone` of live kake-shokunin with `HOME` and `XDG_CONFIG_HOME` inside the sandbox:
```
orig/    selftest 16/16
patched/ selftest 15/16   FAIL i git-commit-import
```
Case `i` fails because it asserts that a commit by `op <op@x>` is published (F6). This is a tradeoff the judge must decide: either case `i` changes to expect a refusal, or the lane-identity invariant is relaxed in writing.

## Inference

- [INFERENCE] F1 is the most likely live failure. Every git-era lane gets its first colocation at its next dispatch or closure (`inline.sh:90,142`). A git-era L1 that ran `git pull` or `git fetch` with unpushed commits leaves exactly that state. Today's read-only survey shows no live lane in that state: all non-colocated lanes are `+0 -0` except `souji-shokunin +1 -0` (ahead only, safe). The window reopens every round until all lanes are colocated.
- [INFERENCE] mado's 8 unpushed round-17 commits are rewritten if the closure's helper push has to rebase (F17 showed `committed` hashes changing). Any round-17 report that cites those hashes before the push will fail `merge-base --is-ancestor`.
- [INFERENCE] `jj op restore <op-before-fork>` would also undo F14, but it also rewinds jj's `master@origin` view. Not tested; the bookmark set + abandon recipe above is verified and narrower.
- [INFERENCE] F12's trigger needs a seat to pass `.` or a symlinked or alternate path. The templates use absolute `{{LANE_CWD}}`, so it is rare, but a seat editing commands by hand reaches it. Different `HYAKU_STATE` values also split locks (not run).

## Recommendations (smallest safe corrections, in priority order)

1. **Fast-forward gate in `do_push`** (F1, and defense in depth for F18): never call `jj git push` while `jj log -r '<b>@origin ~ ::bookmarks(exact:"<b>")'` is non-empty; go to fetch+rebase instead. **Diverged-lane refusal at first `init`**: refuse when ahead>0 && behind>0. Both verified above.
2. **First-colocation preconditions in `init`**: refuse on MERGE_HEAD, CHERRY_PICK_HEAD or REVERT_HEAD, a rebase in progress, `git diff --cached` non-empty, detached HEAD, or HEAD ≠ `origin/HEAD` (F2–F5). The failure surfaces at dispatch as `jj-init-failed`; the recovery is the operator's.
3. **Lock by physical path** (`pwd -P`), not `basename` (F12). Also verify that the pushed tip contains the helper's own change id before printing `pushed` (F12, F13).
4. **Never treat a jj failure as "nothing to commit"**: check `jj diff`'s exit status (F13).
5. **Identity and description gate before push**, plus `jj metaedit --update-author` on @ during `init` (F6, F9). Rewrite selftest `i` to expect a refusal followed by the metaedit recovery, or record an explicit identity exemption.
6. **Rewind gate**: persist the last pushed tip and refuse to republish when the remote no longer contains it (F18).
7. **Divergent-tip refusal** in the push recovery path, with the verified recovery commands in the error text (F14). Teach `jj-lane.sh state` to report `conflict=yes` from `jj --ignore-working-copy bookmark list` or a `<b>??` check; pure git cannot see it.
8. **Rollback switch** (F16): make `lane-addendum.md` and `closure-prompt.md` branch on `HYAKU_VCS`, and make the helper's "not jj-colocated" error say "use git (HYAKU_VCS=git)" instead of inviting `init`. Ship the backout recipe in §E as `jj-lane.sh uncolocate <lane>`, with the jj-only-commit inventory as a refusal precondition.
9. **Prompt text**: add `git fetch`, `git pull` and `git commit --amend` to the addendum's forbidden list (F1, F8). Name `jj new`, `jj commit` without paths, and `jj describe` as forbidden seat writes (F9, F10), because pathspec-limited commits cannot be enforced by the helper once a seat makes a correctly-identified jj commit (the residual in F9).

## Housekeeping

- Installs or upgrades: none.
- Kept in the sandbox as cited evidence: `t1d`, `t1h`, `t1e3`, `t2a`, `t3b2`, `t4e` (it also holds the recovery commit), `t6b`, `patched/`, `guards.diff`, the scenario scripts `t*.sh`, `env.sh`, `xdg/` (jj repo configs for the kept lanes), and `state/`. Everything else was removed, 8.7 MB remaining.
- No jj command ran in or under `/home/vgpnk/Projects/shokunin`. The only write there is this report.
