# JjAuditFleetCommit — `fleet-commit.sh` + `append-closure.py` against a jj-colocated fleet root

Seat: JjAuditFleetCommit-2 (leaf reviewer). Date: 2026-10-20. Scope: the two git-based fleet-root
writers, evaluated for the conditional "fleet root becomes jj-colocated while these writers keep
running". Read-only on the live fleet root; every jj command ran in
`/fast/scratch/jj-wave/JjAuditFleetCommit-2` (jj 0.45.1-7c41cdeb, git 2.56.0).

Setup: bare clone of live HEAD → `$SB/remote.git`; work clones from that bare; every clone's
`git remote -v` printed `origin /fast/scratch/jj-wave/JjAuditFleetCommit-2/remote.git` before any
push/fetch. The live dirty state was recreated in each clone (append to `.ufo/watchdog.log`,
`.ufo/state/*.report-baseline`, `.ufo/waves/round-16/falsify/`). Colocation used the helper's exact
commands (`jj-lane.sh init` was also run for real on a fleet-shaped clone). No tool installs.

---

## Findings

### F1. Live fleet root today: attached git, no `.jj` — observed 2026-10-20 11:16–12:05

```
$ cd /home/vgpnk/Projects/shokunin
$ stat -c '%F %n' .git          → directory .git
$ test -d .jj                   → absent
$ git rev-parse --abbrev-ref HEAD → master
$ git rev-parse HEAD master origin/master
df54adf2… df54adf2… df54adf2…   (at 12:05; earlier bee791e)
$ git ls-files | wc -l          → 3302
$ git for-each-ref refs/heads --format='%(refname:short)' | wc -l → 11
$ git status --porcelain | wc -l → 11 at 11:12 (1 tracked mod + 10 untracked); 41 at 12:05 (other seats active)
$ git ls-files .ufo/state | wc -l → 64 ; git status --porcelain -uall .ufo/state | wc -l → 9
$ find . -xdev -type f | wc -l → 314209   (310707 under *-shokunin/, 4930 under .tower/)
$ ls .git/hooks | grep -v sample → (empty)
$ git config --local --list | grep -E 'hooksPath|sparse|gpgsign|fsmonitor' → (empty)
$ git check-ignore -v .tower/x → .git/info/exclude:8:.tower/
$ git check-ignore -v audio-shokunin/x → .gitignore:1:*-shokunin/
```

Lane dirs `kama-shokunin`, `mado-shokunin`, `tameshi-shokunin` are already `.jj`-colocated; the
fleet root is not. `.ufo/watchdog.log` is permanently dirty (appended by the driver), so the fleet
root is the one repo where "dirty tracked file" is the normal state.

### F2. Colocation alone (init only, no jj working-copy write) is harmless — both writers behave as today

Sandbox `fleet` colocated exactly as `jj-lane.sh init` does; HEAD stayed attached.

```
$ bash scripts/hyaku/fleet-commit.sh --as kama -m "round-99: audit probe commit" -- scripts/hyaku/_audit_probe.txt
committed 9a18f6935d6eabe49395aec7a6b4ce7e54a16842
pushed 9a18f69 (1 ahead)
$ git -C $SB/remote.git show master:scripts/hyaku/_audit_probe.txt → v1
$ git -C $SB/remote.git log -1 --format='%an <%ae> / %cn <%ce>' master
kama-shokunin <kama@shokunin.local> / kama-shokunin <kama@shokunin.local>
$ git -C $SB/remote.git show master:.ufo/watchdog.log | grep -c SNAPSHOT-MARKER → 0
```

`append-closure.py` at attached HEAD (`fleet13`):

```
$ python3 scripts/hyaku/append-closure.py --entry entry991.json
appended rounds[357] commit 1e1c493b2772045e47c68fab7a05ceb455909967
pushed
$ git rev-parse HEAD master origin/master
1e1c493b… 1e1c493b… 1e1c493b…
```

So the mere presence of `.jj` is not the breaker. Everything below needs one jj command that moves
or exports the working-copy commit.

### F3. BLOCKER — one working-copy-moving jj command makes the next git write publish the WC tree, including `.ufo/watchdog.log`

Reproduce (`fleet3`): colocate with `snapshot.auto-track="none()"`, recreate the dirty log, then one
`jj new` (equivalent surface: `jj commit`, `jj bookmark set`, any jj write that exports HEAD):

```
$ jj new
Working copy  (@) now at: nsmuvpnq 6ee7acdc (empty) (no description set)
Parent commit (@-): ywmqrpuq 94dd8733 (no description set)
$ git symbolic-ref -q HEAD || echo DETACHED ; git rev-parse HEAD master origin/master
DETACHED  94dd8733…  9132d994…  9132d994…
$ git status --porcelain
?? .ufo/state/mori.report-baseline          # the tracked log mod is now inside HEAD, invisible
```

Then the real writer:

```
$ bash scripts/hyaku/fleet-commit.sh --as protocol -m "round-99: protocol audit probe" -- scripts/hyaku/_audit_fleet3.txt
committed f5a1de4dd5907e0f71a1e43f82667b0ae93d33c6
pushed f5a1de4 (2 ahead)
$ git -C $SB/remote.git cat-file -p f5a1de4d
parent 94dd87334809f6a721f4c34add9e55ff97f93833
author Joao Pedro Veiga <jpveigao10@gmail.com> …
change-id ywmqrpuqwwkmmtnnonvzrtmxmxtptnqu
$ git -C $SB/remote.git show --stat --oneline master^
94dd873
 .ufo/watchdog.log | 1 +
$ git -C $SB/remote.git show master:.ufo/watchdog.log | grep -c FLEET3-MARKER → 1
```

`fleet-commit.sh`'s pathspec guard (`scripts/hyaku/fleet-commit.sh:30-32`) filters only the
*arguments*; `git commit -- <paths>` (`:53`) limits only the diff against its parent, and the parent
is HEAD = the jj WC commit holding every dirty tracked file. The lane commit's own diff is clean —
`git show --stat f5a1de4` shows only `scripts/hyaku/_audit_fleet3.txt` — so the contamination hides
one level down, in the pushed history, as an undescribed commit authored by the operator identity.

`append-closure.py` does exactly the same (`fleet4`): `jj new` → HEAD detached at `98a70a9` (the WC
commit containing `FLEET4-MARKER`); `append-closure.py` printed
`appended rounds[356] commit bd2160c438b1ba46794ff730c8f01a843da15a8a` / `pushed`;
`git show --stat master^` → `.ufo/watchdog.log | 1 +`; `FLEET4-MARKER` present on the remote.

Why it lands: `fleet-commit.sh:60` counts `origin/master..HEAD`; with HEAD detached the WC commit is
counted, and `:63` pushes `HEAD:$BRANCH`, i.e. the WC commit plus the new commit.

### F4. BLOCKER — naive colocation (default `snapshot.auto-track`) makes jj itself stage driver runtime

`fleet6`, colocated with plain `jj git init --colocate .` (no helper config):

```
$ jj st
Working copy changes:
A .ufo/state/mado.report-baseline
M .ufo/watchdog.log
A .ufo/waves/round-16/falsify/note.md
$ git status --porcelain
 A .ufo/state/mado.report-baseline
 M .ufo/watchdog.log
 A .ufo/waves/round-16/falsify/note.md      # " A" = jj wrote intent-to-add entries
```

After `jj new` + fleet-commit: `remote has mado state baseline: True`, `remote has falsify note:
True`, `remote has FLEET6-MARKER: True`, and `git show --stat master^` lists all three. The lane's
`.ufo/state` argument guard is irrelevant: jj put the files in the tree, not the argument list.
The helper's init sets `snapshot.auto-track="none()"` before its first snapshot (verified via
`jj config list --repo` on `fleet11`: `snapshot.auto-track = "none()"`), so this is the failure mode
of a manual/naive init, a recreated `.jj`, or a lost repo config.

### F5. HIGH — detached HEAD breaks the "cited hash is an ancestor of the branch" invariant

`fleet4`, immediately after the successful append-closure push:

```
$ git merge-base --is-ancestor bd2160c4 master ; echo $?          → 1 (not an ancestor)
$ git merge-base --is-ancestor bd2160c4 origin/master ; echo $?   → 0
$ git log --oneline -3 master
f5a1de4 round-99: protocol audit probe
94dd873
9132d99 round-99: audit probe v2
$ git status -sb
## HEAD (no branch)
```

The cited hash is on `origin/master` but not on the local branch ref until some later jj command
runs; a later `jj st` fast-forwarded local `master` from `f5a1de4` to `bd2160c`
(`master before/after: f5a1de4dd bd2160c43`). `fleet3` shows the same after fleet-commit
(HEAD `f5a1de4`, local `master` `9132d99`). Any verifier that reads `refs/heads/master`, `@{u}`, or
`git log master` in that window sees a false "not landed"; `@{u}` is simply gone in detached HEAD.

### F6. HIGH — a jj export inside fleet-commit's add→commit window yields "nothing to commit" + an unauthored push, exit 0

`fleet7`: a PATH shim ran `jj new` immediately before the script's `git diff --cached` call
(`fleet-commit.sh:50`) — i.e. the interleaving a concurrent jj write can produce, since jj takes no
fleet lock (F8):

```
$ bash scripts/hyaku/fleet-commit.sh --as kama -m "round-99: fleet7 probe" -- scripts/hyaku/_audit_fleet7.txt
nothing to commit
pushed 1a05844 (1 ahead)          # exit 0
$ git -C $SB/remote.git cat-file -e master:scripts/hyaku/_audit_fleet7.txt → absent
$ git -C $SB/remote.git log -2 --format='%h %an|%cn|%s' master
1a05844 Joao Pedro Veiga|Joao Pedro Veiga|
bedbb30 kama-shokunin|kama-shokunin|round-99: fleet6 probe
$ git -C $SB/remote.git show master:.ufo/watchdog.log | grep -c FLEET7-MARKER → 1
```

jj's export reset the staged entry, `git diff --cached --quiet` became true, so no commit was made;
but the push stage still saw the WC commit as "ahead" and pushed it. The lane's work is not in the
repo, the report would cite `pushed 1a05844`, and the exit code is 0. The shim forces the
interleaving; it does not invent the window.

### F7. MEDIUM — index-reset semantics are export-tied, narrower than the lane addendum states

`fleet3` (`staged` = `git diff --cached --name-only`):

```
after git add        staged='scripts/hyaku/_audit_fleet3.txt'
after jj st          staged='scripts/hyaku/_audit_fleet3.txt'   # snapshot keeps the index
after jj git push    staged='scripts/hyaku/_audit_fleet3.txt'   # no reset
after jj bookmark set master -r @  staged=''                    # reset
```

`jj new` cleared it in `lane2`. So "jj resets the index on every mutation"
(`scripts/hyaku/lane-addendum.md:129`) is too broad as written; the destructive set is the
exporting mutations (`jj new`, `jj commit`, `jj bookmark set`), which is precisely the set a
concurrent writer can hit between `fleet-commit.sh:49` and `:50`.

### F8. MEDIUM — lock interplay: one git lock, two jj lock namespaces, and jj takes neither

```
fleet-commit.sh:37   flock -w 1200 "$lk"        # $STATE/fleet-git.lock
append-closure.py:85 fcntl.flock(lk, LOCK_EX|LOCK_NB)   # same file, 1200 s deadline
jj-lane.sh:88        exec {lk}>"$STATE/jj-$base.lock"   # → jj-shokunin.lock for the fleet root
jj-lane.sh:89        flock -w 300 "$lk"
```

The two git writers exclude each other (verified: `flock -w 1 $STATE/fleet-git.lock true` → rc=1
while a Python `fcntl.flock` held it). jj takes neither: `jj new` returned rc=0 in 0.01 s while
`fleet-git.lock` was held exclusively. jj does honor `.git/index.lock`:

```
$ touch .git/index.lock ; jj bookmark set master -r @-
Error: Failed to reset Git HEAD state
Caused by: 1: Could not acquire lock for index file    (rc=1, HEAD/master unchanged)
```

so a jj export fails closed while a git process is mid-write, but there is no ordering after the
git process releases the lock and before its next git command. Additionally, `inline.sh:117-125`
runs `jjl push "$cwd"` for any lane whose cwd contains `.jj`; for repo-`.` lanes `cwd == FLEET`, so
that push would run under `jj-shokunin.lock`, not `fleet-git.lock`.

### F9. MEDIUM — latent accidental fleet-root colocation path already exists in the code

```
shokunin.conf:20-21   protocol|.|fleet-meta: …        aggregator|.|cross-lane quality …
watchdog.sh:77-78     repo "." → LANE_CWD[id] = $SHOKUNIN_ROOT
inline.sh:38-40       lane_vcs_init() { jjl init "$2" "$1" … }   # $2 = LANE_CWD
inline.sh:90,142      lane_vcs_init "$lane" "${LANE_CWD[$lane]}"  # dispatch and closure, no guard
hyaku.env:10          HYAKU_VCS=jj
```

One `scripts/hyaku/inline.sh closure protocol` (or a protocol/aggregator round dispatched that way)
would run `jj-lane.sh init /home/vgpnk/Projects/shokunin protocol` and colocate the live fleet root,
setting repo config `user.name=protocol-shokunin`. Today it has not fired: `.jj` absent at the root,
no `protocol`/`aggregator` claim dirs, `pool.txt` excludes the meta-lanes. `inline.sh:124` also
reads `git -C "$FLEET" rev-list --count origin/master..HEAD`, which under a colocated root counts
`@` as unpushed and triggers `fleet-commit.sh --as <lane> -m unused -- "$rep"` — the F3/F6
amplifier.

### F10. LOW — jj's push guard is real and git's is absent

```
$ bash scripts/hyaku/jj-lane.sh push fleet3
jj-lane: push failed after 3 attempts: Error: Won't push commit 1772b7fd… since it has no description
```

`jj git push --bookmark` refuses undescribed commits; `git push -q "$REMOTE" "HEAD:$BRANCH"`
(`fleet-commit.sh:63`) and `git push -q origin HEAD:master` (`append-closure.py:122`) do not. This
is the one guard that catches the F3/F6 WC commit — and it is not on the path these writers use.

### F11. LOW — snapshot cost and ignore coverage are not the objection

`fleet10`, auto-track none, 3,300 tracked files: `jj st` 0.007 s; +20k files in a `*-shokunin/`
ignored dir 0.009 s; +20k files in an unignored untracked dir 0.018 s; `jj git init --colocate`
0.05 s. `fleet9` shows jj honors `.gitignore`, `.git/info/exclude` and `core.excludesFile`: with
default auto-track it added only `scratchplain/p.txt`, not `.tower/sub/a.txt`,
`audio-shokunin/lane.txt` or `x.ignored`. So the live root's 310k ignored files should not make jj
reads expensive [INFERENCE from a 20k-file sample, not a full-scale run].

### F12. LOW — colocation imports every local branch as a bookmark and can conflict it

`fleet13` with 3 local branches: after `jj st`, `jj bookmark list` shows 3 bookmarks. The live root
has 11 branches. `fleet12` shows the conflict mode: after `jj bookmark set master -r @` plus one
git commit+push, the next `jj st` printed `Warning: These bookmarks have conflicts: master`,
`jj log -r master` failed with `Error: Name 'master' is conflicted`, and `jjl push` exited 3
(`Won't push commit … since it has no description`). `jj git init --colocate` itself leaves
`.git/config` unchanged (no hooksPath/gpgsign/sparse added).

---

## [INFERENCE]

- **Trigger frequency.** Today's scripts touch the fleet root with jj only through `jjl init`
  (`jj git init`, then `--ignore-working-copy config set`) and `jjl push` (`jj git push`); neither
  detaches HEAD in my runs, so with the current code and no manual jj use the root would *usually*
  keep working. The blocker needs one working-copy-moving command (`jj new`, `jj commit`,
  `jj bookmark set`, or a rebase) in the root — a single operator `jj new`, a confusingly-scoped
  `jjl commit`, or the F9 meta-lane path. Once `.jj` exists, that is one command away, permanently.
- **Severity of F3 in practice.** The fleet root's `.ufo/watchdog.log` is dirty by design and
  appended continuously, so every WC snapshot carries a driver-log delta; there is no "clean
  moment" that would make the inherited-tree problem intermittent. The only reason F3 did not fire
  in F2 is that no jj WC write had happened yet.
- **jj locking internals.** The observed fail-closed behavior on `.git/index.lock` is git2's
  index lock; ref updates are likewise lock-protected, but no shared lock exists with
  `fleet-git.lock`. A future jj release could change the export timing.
- **append-closure liveness (pre-existing).** If the push exits 3, the MANIFEST row is already in
  the local file; a rerun hits `die("duplicate hyaku closure …")` (`append-closure.py:102`), so the
  row can only reach origin via a later fleet commit or a manual push. Not caused by jj, but a
  colocated root raises non-FF push failures.
- **Hooks.** No hooks are installed in the live repo, so no hook divergence is observable today;
  jj commits do not run git hooks, which would matter if a pre-commit gate were added later.

---

## Recommendation: keep the fleet root on git; do not colocate it

The two writers are correct only while `HEAD` is attached to `master`. Colocation changes HEAD
semantics for the whole repo (detached WC commits, index export, bookmarks vs branch refs), and the
fleet root is the worst possible place for that: it has a permanently dirty tracked driver log, 11
branches, and multiple unserialized writers. jj's benefits (undo/op-log, auto-snapshot, rebase
recovery) are unused on a linear, already-serialized, pathspec-only, push-immediately workflow; its
costs are paid on every commit.

What would change if it were colocated anyway, per writer:

| writer | attached git (today) | colocated, no jj WC write | colocated + one jj WC write |
|---|---|---|---|
| `fleet-commit.sh` | correct, pathspec-only, identity correct | unchanged (F2) | publishes WC tree incl. `.ufo/watchdog.log`; local `master` stale; race → "nothing to commit" + unauthored push, exit 0 (F3/F6) |
| `append-closure.py` | correct | unchanged (F2) | same inherited-tree publication; cited hash missing from local branch (F3/F5) |
| `watchdog.sh commit_evidence` | already outside the fleet lock | same | same inherited-tree publication (no lock at all) |
| `inline.sh verify` | reads `origin/master..HEAD` | same | counts WC commits as unpushed → triggers a fleet push (F9) |

Keep the current split: **lanes on jj (helper contract), fleet root on git.** If the operator
nevertheless wants jj at the fleet root, it must be a full-writer conversion, not coexistence:

1. Move all four writers (fleet-commit, append-closure, watchdog `commit_evidence`, inline verify's
   rev-list/push) to jj under one lock (`fleet-git.lock`), with `snapshot.auto-track="none()"`
   enforced, `jj commit -m … -- paths` + `bookmark set` + `jj git push` (description guard), and a
   preflight that refuses when `bookmark master` is conflicted or diverged from `master@origin`.
2. Replace `inline.sh:124`'s HEAD-based count with a refs/bookmark comparison.

Cheap fail-closed hardening that is worth doing regardless of the decision:

- `fleet-commit.sh`: after taking the flock, require
  `test "$(git symbolic-ref -q HEAD)" = "refs/heads/$BRANCH"` and
  `test "$(git rev-parse HEAD)" = "$(git rev-parse refs/heads/$BRANCH)"`; abort 1 otherwise. Re-check
  immediately before `git commit` and before `git push`. Push a refspec
  (`refs/heads/$BRANCH:refs/heads/$BRANCH`) instead of `HEAD:$BRANCH` so a detached HEAD fails
  closed instead of publishing the WC commit.
- `append-closure.py`: the same `git symbolic-ref` preflight before `git commit` and `git push`;
  exit 1 on detached HEAD.
- `fleet-commit.sh` / `append-closure.py`: hard-error if `-d "$FLEET/.jj"` exists (with an explicit
  opt-out only for a real migration), so an accidental colocation cannot silently change semantics.
- `inline.sh`: skip or error on `lane_vcs_init` when `realpath(LANE_CWD) == realpath(FLEET)`; make
  `jj-lane.sh init` refuse the fleet root outright.
- `lane-addendum.md`: correct the index-reset sentence to "exporting mutations (`jj new`,
  `jj commit`, `jj bookmark set`) reset the index; snapshot-only reads keep staged entries but still
  write `@` and can fast-forward tracked bookmarks."

---

## Verification gaps / residual risk

- No command was run against the live fleet root (forbidden); all evidence is from a bare clone of
  live HEAD plus a recreated dirty state. Live content moved during the audit (11 → 41 dirty paths,
  HEAD `bee791e` → `df54adf`), so exact live numbers are timestamped above.
- F6's interleaving was forced with a `git` PATH shim; no natural race was observed. Its frequency
  therefore depends entirely on whether a WC-moving jj command ever runs in the fleet root.
- Full-scale colocation (314k files, 6.4 G worktree) was not attempted; ignore pruning and snapshot
  cost were measured on the 3,300-file clone with 20k-file synthetic dirs.
- jj 0.45.1 only; export/detach behavior is version-specific and should be re-checked before any
  future migration.
- Hooks: none installed in the live repo, so hook interaction is untested.
- The sandbox is retained at `/fast/scratch/jj-wave/JjAuditFleetCommit-2` because it preserves the
  failure evidence (`remote.git` plus `fleet3`, `fleet4`, `fleet6`, `fleet7`, `fleet12` clones).
  Nothing outside it was written except this report. No tools were installed or upgraded.
