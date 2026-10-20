# JjRevengerLaneJjState — pre-existing `.jj` in tameshi-shokunin and mado-shokunin

Seat `JjRevengerLaneJjState-2`, wave `hyaku/jj-w1`. Scope: reverse-engineer the `.jj` state that
already existed in tameshi (`/home/vgpnk/Projects/shokunin/tameshi-shokunin`, `.jj` 2026-10-19 20:39)
and mado (`/home/vgpnk/Projects/shokunin/mado-shokunin`, 20:38), and decide whether it must be
cleaned before `scripts/hyaku/jj-lane.sh init`. jj = `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`.
No tool was installed or upgraded for this seat.

## Method (and what was never touched)

Both repos were `cp -a`'d at **2026-10-20 11:12:13 -03:00** into
`/fast/scratch/jj-wave/JjRevengerLaneJjState/{tameshi,mado}`. Every copy had `origin` repointed to a
sandbox bare repo and confirmed before any jj/git mutation:

```
$ git -C tameshi remote -v
origin  /fast/scratch/jj-wave/JjRevengerLaneJjState/tameshi-origin.git (fetch)
origin  /fast/scratch/jj-wave/JjRevengerLaneJjState/tameshi-origin.git (push)
```

No `jj` command was ever run with cwd or `-R` inside the live fleet root or the live lane repos
(only `jj --version`/`jj help` from the wave sandbox, which is not a repo). Live lanes were read
with `cat`, `grep`, `find`, and `git log|show|ls-files|rev-parse|status|diff` only. No push reached
a real remote (all pushes went to the sandbox bare repos above). The live lanes kept committing
during the study (mado's `master` was mid-operation at one recheck), so every hash below is the
frozen copy-time value.

All experiments ran in throwaway copies under the sandbox. The sandbox is retained because it holds
the two reproduced failure states cited below; path: `/fast/scratch/jj-wave/JjRevengerLaneJjState/`
(`tameshi-probe/`, `mado-probe/` = index pollution; `tameshi-ini/` = empty-remote push failure).
Reading each copy's repo config made jj create a `~/.config/jj/repos/<hash>` entry for the copy
(it warns "repo appears to have been copied"); the 16 sandbox-path entries were deleted afterwards
and the live lanes' entries (`86a634125f04a8756fc6`, `b7d9811b7038ba799207`) were left intact.

## Findings

### 1. Who created it, when, and with what

`jj op log`, oldest first (`jj --ignore-working-copy op log --reversed -G -T 'self.id().short() ++ " | " ++ self.time().start() ++ " | user=" ++ self.user() ++ " | " ++ self.description() ++ " | attrs=" ++ self.attributes() ++ "\n"'`):

mado (12 ops):
```
246524d04bc7 | 2026-10-19 20:38:49.175 -03:00 | user=vgpnk@plazir27 | add workspace 'default' | attrs=
4965836260e6 | 2026-10-19 20:38:49.182 -03:00 | user=vgpnk@plazir27 | import git refs | attrs=args: jj git init --colocate
cc5bb9e174c9 | 2026-10-19 20:38:49.191 -03:00 | user=vgpnk@plazir27 | import git head | attrs=args: jj git init --colocate
04be2ef684b2 | 2026-10-20 02:41:05.439 -03:00 | user=vgpnk@plazir27 | import git head      | attrs=args: jj log -r @ --no-graph -T 'commit_id ++ " " ++ description.first_line() ++ "\n"'
e896589aa956 | 2026-10-20 02:41:05.447 -03:00 | user=vgpnk@plazir27 | snapshot working copy | attrs=args: jj log -r @ --no-graph -T 'commit_id ++ " " ++ description.first_line() ++ "\n"'
7e6c2230b361 | 2026-10-20 02:41:05.450 -03:00 | user=vgpnk@plazir27 | import git refs      | attrs=args: jj log -r @ --no-graph -T 'commit_id ++ " " ++ description.first_line() ++ "\n"'
d8557bd94eb1 | 2026-10-20 04:24:40.825 -03:00 | user=vgpnk@plazir27 | import git head      | attrs=args: jj log -r '@|@-|@--' --no-graph
942a4f6baa51 | 2026-10-20 04:24:40.833 -03:00 | user=vgpnk@plazir27 | snapshot working copy | attrs=args: jj log -r '@|@-|@--' --no-graph
705178484894 | 2026-10-20 04:24:40.836 -03:00 | user=vgpnk@plazir27 | import git refs      | attrs=args: jj log -r '@|@-|@--' --no-graph
9618cbb9de0a | 2026-10-20 04:28:39.237 -03:00 | user=vgpnk@plazir27 | snapshot working copy | attrs=args: jj --no-pager -R . log -r @ --no-graph -T 'commit_id ++ " " ++ description.first_line()'
3662dade385c | 2026-10-20 10:21:51.010 -03:00 | user=vgpnk@plazir27 | import git head      | attrs=args: jj --no-pager log -r '@ | @- | trunk()' --no-graph -T 'change_id.short() ++ " " ++ commit_id.short() ++ " " ++ bookmarks ++ " " ++ description.first_line() ++ "\n"'
56a16b78a3f5 | 2026-10-20 10:21:51.024 -03:00 | user=vgpnk@plazir27 | import git refs      | attrs=args: jj --no-pager log -r '@ | @- | trunk()' --no-graph
```

tameshi (6 ops):
```
cfe3eb1ac4c3 | 2026-10-19 20:39:15.351 -03:00 | user=vgpnk@plazir27 | add workspace 'default' | attrs=
951afa7a7ec3 | 2026-10-19 20:39:15.355 -03:00 | user=vgpnk@plazir27 | import git refs | attrs=args: jj git init --colocate
88186501ea3f | 2026-10-19 20:39:15.359 -03:00 | user=vgpnk@plazir27 | import git head | attrs=args: jj git init --colocate
d0521bb37d97 | 2026-10-20 10:21:50.970 -03:00 | user=vgpnk@plazir27 | import git head | attrs=args: jj --no-pager log -r '@ | @- | trunk()' --no-graph ...
53c9d1a60cc2 | 2026-10-20 10:21:50.991 -03:00 | user=vgpnk@plazir27 | snapshot working copy | attrs=same argv
31e6f00fe1f6 | 2026-10-20 10:21:50.995 -03:00 | user=vgpnk@plazir27 | import git refs | attrs=same argv
```

Creation mechanism and author are unambiguous: `jj git init --colocate` run by OS user
`vgpnk@plazir27` — mado at 20:38:49, tameshi at 20:39:15. The recorded session is
`.ufo/waves/kaika/jj-live-pilot.txt` (mtime 2026-10-19 20:49:24):

```
mado $ jj git init --colocate
exit=0
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `master@origin`.
...
mado $ jj config set --repo revset-aliases."immutable_heads()" builtin_immutable_heads() | ::bookmarks()
exit=0
```
and `.ufo/waves/kaika/JJ-ADOPTION.md` §Plan step 2: "Pilot initialized: `mado` and `tameshi` …
Repo-scoped lane identities and immutable bookmarked ancestry are configured." The repo-config
files carry the same 20:38/20:39 second.

**Nothing was ever committed through jj.** There is no `commit`, `bookmark set`, `describe`,
`rebase`, `undo`, or `op restore` operation in either op log. Everything after the three init ops is
`import git head/refs` + `snapshot working copy` produced by ad-hoc `jj log` invocations.

### 2. Repo config: where it lives and what it implies

jj 0.45 stores `--repo` config *outside* the repo. Live locations (read from `metadata.binpb`):

- tameshi: `~/.config/jj/repos/86a634125f04a8756fc6/config.toml`
- mado: `~/.config/jj/repos/b7d9811b7038ba799207/config.toml`

Verbatim (both, only name/email differ):
```toml
[revset-aliases]
"trunk()" = "master@origin"
"immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"

[user]
name = "tameshi-shokunin"        # / "mado-shokunin"
email = "tameshi@shokunin.local" # / "mado@shokunin.local"
```
There is **no** `snapshot.auto-track` key — a fact with consequences in §5.

What the config implies, each point observed:

- `trunk() = master@origin` was written by `jj git init --colocate` itself (pilot transcript:
  "Setting the revset alias `trunk()` to `master@origin`"). With default
  `builtin_immutable_heads() = trunk() | tags() | untracked_remote_bookmarks() | …`, master@origin's
  ancestry is immutable.
- `immutable_heads() = builtin_immutable_heads() | ::bookmarks()` extends that to **every commit
  reachable from any local bookmark**. `master` is the only local bookmark and points into the main
  lane history, so the whole history plus the freshly pushed commit is immutable:
  ```
  $ jj describe -r master -m tamper
  Error: Commit d48ffd43554c is immutable
  $ jj rebase -r master -d '@'
  Error: Commit d48ffd43554c is immutable
  ```
  This is exactly the "a cited hash is never amended/rewritten" invariant. The helper's push-retry
  `jj --ignore-immutable rebase` is the only sanctioned escape hatch. `jj metaedit --update-author -r @`
  is unaffected (the working-copy commit is a child of the bookmark, not an ancestor).
- `user.name/user.email` = lane identity, so any jj-created commit defaults to
  `<id>-shokunin <<id>@shokunin.local>`.
- No bookmark-tracking key exists in the file; tracking lives in the jj view. `master@origin` was
  imported at init and is what the helper's `bookmark track` (re-)asserts.

### 3. Working-copy commit at copy time

(`${copy}/` = `/fast/scratch/jj-wave/JjRevengerLaneJjState/{tameshi,mado}`)

```
$ cd ${copy}/tameshi && jj --ignore-working-copy log -r '@|@-|trunk()' ...
xnlswwnklqpp 32f84145ffc2  | a=tameshi-shokunin <tameshi@shokunin.local> c=tameshi-shokunin |  | empty=false conflict=false
ulxpkkxxnoql 28aeef498cc0 master master@origin | a=protocol-shokunin <protocol@shokunin.local> | round-15 verifier spot-check (integrator, hyaku): non-author admit/reject

$ jj --ignore-working-copy diff -r @ --summary
A .ufo/evidence/round-16/coldread/SKILL.snapshot.md          # exactly one line
$ jj --ignore-working-copy file list -r @ | wc -l   -> 1070      ( @- -> 1069 )
```
```
$ cd ${copy}/mado && jj --ignore-working-copy log -r '@|@-|trunk()' ...
nptlkwtloutz 8459861625c0  | a=mado-shokunin <mado@shokunin.local> c=mado-shokunin |  | empty=true conflict=false
wwvtrsssymsx 27cd06f5067c master master@origin | a=protocol-shokunin <protocol@shokunin.local> | round-16 verifier spot-check (integrator, hyaku): non-author admit/reject
$ jj --ignore-working-copy file list -r @ | wc -l   -> 574       ( @- -> 574 )
```

- tameshi's `@` (32f8414) is a snapshot of the lane tree **as of 10:21:50** on top of 28aeef4:
  one added file, the 118,906-byte `.ufo/evidence/round-16/coldread/SKILL.snapshot.md`. That file is
  now tracked in live git (the lane committed it at 10:39/10:49), so the jj `@` is simply an older
  base than git HEAD.
- mado's `@` (8459861) is empty; its committer timestamp is 10:21:51 although the last `snapshot
  working copy` op is 04:28 — the 10:21 `import git head` reset the empty working-copy commit onto
  the new git HEAD, which re-creates the commit object (new id, new committer time).
- `jj --ignore-working-copy log -r 'conflicts()'` → **empty** in both. `ls .jj/repo/op_heads/heads |
  wc -l` → **1** in both (no divergent op heads). No tracked scratch beyond the one file above;
  `.ufo/state` does not exist in either lane, so nothing from the driver runtime is in `@`.
- Bookmarks are stale relative to git:
  ```
  tameshi: jj master/master@origin = 28aeef4   git master/origin/master = c699c8c  (3 commits behind)
  mado:    jj master/master@origin = 27cd06f   git master/origin/master = a9998d1  (4 commits behind)
  ```
  (Both git branches were in sync with their own `origin/master` at copy time.)
- `refs/jj/keep` exists: 7 refs in tameshi, 21 in mado. They keep the abandoned working-copy
  commits and imported branch tips alive, and they leak into `git log --all`:
  ```
  $ git -C tameshi-shokunin log --all --format='%h %an <%ae> %s' | head -5
  32f8414 tameshi-shokunin <tameshi@shokunin.local>
  95f951a tameshi-shokunin <tameshi@shokunin.local>
  ```
  Every keep-ref working-copy commit checked is authored by the lane identity or
  `protocol-shokunin`; none carries the operator identity.

### 4. What the *next* jj command does — the one real hazard of this state

On an untouched copy, the first jj command was a plain `jj log` **without** init:

```
$ cd ${copy}/tameshi-probe && jj --no-pager log -r '@' --no-graph -T 'commit_id.short() ...'
Reset the working copy parent to the new Git HEAD.
Done importing changes from the underlying Git repo.
f2720dacac21
$ jj --ignore-working-copy diff -r @ --summary | wc -l        -> 86
$ git status --porcelain | grep -c '^ A'                      -> 82
```
mado-probe, same procedure: `@` moved to `44969ec77c3c` on a9998d1, `@` diff = 114 paths, and
`git status --porcelain | grep -c '^ A'` = **114**. `jj diff -r @ --stat` = "86 files changed,
13028 insertions(+), 24 deletions(-)" (tameshi) / "114 files changed, 25215 insertions(+), 0
deletions(-)" (mado).

Cause: the repo config has no `snapshot.auto-track`, so jj's default `all()` applies. Every
non-ignored untracked file becomes tracked by `@`, and jj's working-copy reset rewrites the git
index with intent-to-add entries. These are not harmless: in the same probe copy,
`git commit -a --dry-run --short` lists all 86 files, i.e. a `git add -A` / `git commit -a`
follower would sweep lane scratch and evidence into a commit. (`fleet-commit.sh` uses explicit
pathspecs — `git add -- "${existing[@]}"` — so it would not; but the index stays polluted until a
git checkout/reset.)

The reset also drops staged index entries:
```
$ echo staged > s.txt && git add s.txt          # index has s.txt
$ jj log -r @ ...                               # "Reset the working copy parent to the new Git HEAD."
$ git diff --cached --name-only                 # (empty)  -> s.txt is '??' again
```
A plain snapshot *without* a git-HEAD reset preserved a staged `b.txt` in a control run. Both live
lanes had **0 staged entries** at copy time, so nothing was at risk then.

### 5. With the helper's `init` first (the intended path)

Verified on fresh copies of the real `.jj` with a sandbox bare `origin` seeded with the lane's
`master` (`git -C tameshi push -q $S/tameshi-origin.git master:master`; no real remote involved):

```
$ HYAKU_STATE=$S/state JJ_BIN=~/.local/bin/jj bash scripts/hyaku/jj-lane.sh init $S/tameshi-ini tameshi
warn: working-copy commit @ already tracks 1 added path(s); inspect: jj --ignore-working-copy diff --summary -r @
state branch=master local=c699c8c... remote=c699c8c... ahead=0 behind=0 head=attached tracked=130 untracked=13
rc=0
# "tracked=130" is the copied index as captured mid-round; a refreshed state on the same frozen
# copy reports tracked=4 untracked=13 (verified separately with `jj-lane.sh state $S/tameshi`).
$ jj --ignore-working-copy log -r '@|@-' ...
32f84145ffc2 parents=[28aeef498cc0] bk=            <- @ untouched (init uses --ignore-working-copy)
28aeef498cc0 parents=[9f2c86ffdc80] bk=master     <- local bookmark only; master@origin is a remote
                                                  <- bookmark and this template prints local ones
$ jj config list --repo
revset-aliases."trunk()" = "master@origin"
revset-aliases."immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"
user.name = "tameshi-shokunin"
user.email = "tameshi@shokunin.local"
snapshot.auto-track = "none()"
$ git status --porcelain | grep -c '^ A'          -> 0
```
With the seeded remote, the same init's git import also reconciled the bookmarks:
`master: c699c8c / @git: c699c8c / @origin: c699c8c`. So **init is itself the reconciler** — it
sets `auto-track="none()"` with `--ignore-working-copy` (no snapshot) while its jj calls import git
refs and move the bookmark to the real branch tip. The stale `@` is not moved by init; it is dropped
on the first snapshotting command afterwards, and its one tracked file remains on disk (and is
already tracked in git).

Then a real helper commit on the seeded-remote copy (`$S/tameshi-rc`):

```
$ bash scripts/hyaku/jj-lane.sh commit $S/tameshi-rc --as tameshi -m 'wave1 probe rc' -- SKILL.md
committed d48ffd43554c4a67c727932a0e292d94f6b31ecc
pushed d48ffd43554c4a67c727932a0e292d94f6b31ecc        # rc=0
$ git show --format='%h %an <%ae> / %cn <%ce> / %s' -s master
d48ffd4 tameshi-shokunin <tameshi@shokunin.local> / tameshi-shokunin <tameshi@shokunin.local> / wave1 probe rc
$ git log -2 --format=%h master
d48ffd4
c699c8c                                                # parent = the real branch tip
$ git symbolic-ref -q --short HEAD || echo DETACHED
DETACHED
$ git rev-parse master origin/master
d48ffd43554c4a67c727932a0e292d94f6b31ecc
d48ffd43554c4a67c727932a0e292d94f6b31ecc
```
It also committed only the named path (1 file changed in `git show --stat`), left 3 other paths in
`@`, and kept `master == origin/master`.

mado, same procedure (`init` + commit of `.ufo/waves/round-17/label-check.py`):
```
committed 7bfad0861dfa322e933333ce4a466a348fe26a2a
pushed 7bfad0861dfa322e933333ce4a466a348fe26a2a        # rc=0
pushed commit: 7bfad08 mado-shokunin <mado@shokunin.local> wave1 probe: mado jj state
parent: a9998d1
HEAD=DETACHED index-A=0
```
Conclusion for the ticket: **nothing in the existing `.jj` needs cleaning.** The state is internally
sound (no conflicts, one op head, no scratch beyond one now-git-tracked file), init is idempotent
and reconciles the stale bookmarks, and the first commit lands on the live branch tip and pushes.

### 6. Sandbox-only failure, for completeness (not applicable to the live lanes)

Running the same flow against an **empty** bare `origin` produced:
```
$ bash scripts/hyaku/jj-lane.sh commit $S/tameshi-ini --as tameshi -m ... -- SKILL.md
committed 3d049f123f1c...
jj-lane: push failed after 3 attempts: Warning: Failed to resolve `revset-aliases.trunk()`: Revision `master@origin` doesn't exist ...
rc=3
$ cat state/jj-push.err
Error: Bookmark master is conflicted
$ jj bookmark list --all-remotes
master (conflicted):
  - c699c8c3 ...
  + 3d049f12 ...
  @git: 3d049f12 ...
```
Mechanism: `do_push`'s fallback runs `jj git fetch`, and a fetch from a remote that lacks `master`
prunes `refs/remotes/origin/*`:
```
git: refs/remotes/origin/HEAD has become dangling after refs/remotes/origin/master was deleted
```
`master@origin` disappears, `trunk()` resolves to `root()`, and the retry cannot recover. With the
seeded (realistic) remote this never occurs. It does show that `do_push`'s recovery depends on the
remote branch existing and that a pruned/renamed remote branch fails loudly (rc=3, commit kept)
rather than forcing a push.

## Inference [INFERENCE]

- The four mado probe commands (02:41, 04:24, 04:28) were ad-hoc lane-agent checks, and the identical
  command at 10:21:50/51 in both lanes was a single orchestrator-side recon probe. No fleet script
  contains any of those argv strings (`grep -rn` over `scripts/` and `.ufo/` found none), the two
  10:21 calls are 1 s apart with identical templates, and the helper that supersedes them landed at
  11:11. They are the same class as the round-14 incident: read-looking `jj log` commands that
  snapshot the working copy.
- The pilot's own `jj config set --repo …` calls ran while both working copies were clean, so the
  default `auto-track` in effect at 20:38/20:39 did not track anything (the op log shows no snapshot
  op before 02:41).
- Working-copy commits are ephemeral by construction: jj re-creates `@` with a new id and committer
  time on every snapshot/reset, which is why tameshi has 95f951a (empty) and 32f8414 (1 file) and
  mado has four generations of empty `@` in `refs/jj/keep`.
- The 10:21 tameshi `@`'s one added file is not a leak risk: it is an untracked evidence snapshot
  that the lane later committed by git anyway; the helper's commit path is pathspec-limited.

## Recommendations

1. **Run `jj-lane.sh init <lane> <id>` in tameshi and mado before any other jj invocation.** It is
   idempotent on the existing `.jj`, rc=0, sets `snapshot.auto-track="none()"`, preserves the
   `immutable_heads()` alias, and its git import reconciles the stale `master`/`master@origin`.
   Nothing needs deleting first.
2. **Do not run ad-hoc jj in a lane whose `.jj` predates init** (`jj log`, `jj status`, `jj st`).
   That is what produced the 82/114 intent-to-add entries and the 86/114-file `@`. Read-only
   inspection must use `--ignore-working-copy`, or `jj-lane.sh state` (pure git, no jj at all).
3. **A clean re-init (`rm -rf .jj && jj-lane.sh init`) is also safe but unnecessary.** It would
   discard the op log and the 7/21 keep refs; the first snapshot drops the stale `@` either way.
4. **Keep the `immutable_heads()` alias.** It is proven to block `describe`/`rebase` on pushed
   commits, which is the cited-hash invariant. Do not add `--ignore-immutable` anywhere except the
   helper's push-retry rebase.
5. **Guard the first commit against a dirty index.** A working-copy reset discards `git add`-staged
   entries; both lanes were clean at copy time (0 staged), but the helper could reject a commit when
   `git diff --cached --name-only` is non-empty, or at least print the staged count in `state`.
6. **Exclude `refs/jj/keep` from global commit walks.** `git log --all` / `rev-list --all` now see
   jj-internal working-copy commits (7 refs in tameshi, 21 in mado) with empty messages. Any census
   or hash-enumeration tool should use explicit branch refs or filter `refs/jj/keep`.
7. If the wave wants a diagnostic, have init print the `jj master` vs `git <branch>` divergence
   (3 commits in tameshi, 4 in mado at copy time) instead of only the git-based state line; the
   current `state` line cannot show that jj's bookmark is stale before the first import.

## Reproduction

```
S=/fast/scratch/jj-wave/JjRevengerLaneJjState
cp -a /home/vgpnk/Projects/shokunin/tameshi-shokunin $S/tameshi
git -C $S/tameshi init --bare -q $S/tameshi-origin.git
git -C $S/tameshi remote set-url origin $S/tameshi-origin.git   # verify with git remote -v
( cd $S/tameshi && jj --at-op=@ --ignore-working-copy op log --reversed -G \
    -T 'self.id().short() ++ " | " ++ self.time().start() ++ " | user=" ++ self.user() ++ " | " \
       ++ self.description() ++ " | attrs=" ++ self.attributes() ++ "\n"' )
# first-command hazard: cp -a $S/tameshi $S/tameshi-probe; cd $S/tameshi-probe; jj log -r @ ...
# helper path:        cp -a $S/tameshi $S/tameshi-rc; seed the sandbox origin with master;
#                     jj-lane.sh init; jj-lane.sh commit
# scripts: $S/{probe,initprobe,reconcile,mado-rc,exp2,exp3,exp4,emptyremote}.sh
```
