# JjAuditInlineSh — git calls in `scripts/hyaku/inline.sh` and `scripts/hyaku/status.sh` vs a jj-colocated lane

Seat: JjAuditInlineSh-2. Scope: every git invocation in the two named files, and how each behaves
against a jj-colocated lane whose git HEAD may be detached. Proposal only — no repo file was edited.

Host/versions: git 2.56.0, jj 0.45.1 (`~/.local/bin/jj`). No installs were needed, so nothing was
installed or upgraded.

Method: the two scripts were read statically (`grep -n`, `nl -ba`) and their exact command lines were
replayed against sandbox repos under `/fast/scratch/jj-wave/JjAuditInlineSh-2/` (helper copy
`helper/jj-lane.sh`, sandbox bare origins, and lanes `lane-git2`, `lane-jj`, `lane2`, `lane3`,
`lane4`). Every `jj` command ran only in that sandbox; live repos were only read with
`git -C <live> rev-parse | symbolic-ref | status | log | rev-list` — no write, commit, stage,
checkout, fetch, or push. The sandbox is preserved because it holds the failure states cited below.

## Findings

### F1. The ticket's premise is stale: neither file contains `rev-list --count '@{u}..HEAD'`, and `status.sh` has no git call at all

```
$ grep -n -E '\bgit\b' scripts/hyaku/inline.sh
33:# directive 2026-10-20). Colocated lanes leave git HEAD detached, so never read `@{u}`/HEAD
111:  if [ -n "$(git -C "$FLEET" status --porcelain -- "$rep")" ] || [ -z "$(git -C "$FLEET" log -1 --format=%H -- "$rep")" ]; then
119:    if [ -d "$cwd/.jj" ]; then pushcmd=(jjl push "$cwd"); else pushcmd=(git -C "$cwd" push -q); fi
123:  [ -n "$(git -C "$cwd" status --porcelain)" ] && echo "WARN lane repo has uncommitted changes: $(git -C "$cwd" status --porcelain | wc -l) paths"
124:  if [ "$(git -C "$FLEET" rev-list --count origin/master..HEAD 2>/dev/null || echo 0)" != 0 ]; then
129:  echo "OK $lane r$n landed: report $(git -C "$FLEET" log -1 --format=%h -- "$rep") lane tip $(lane_tip "$cwd" | cut -c1-9)"
$ grep -n -F '@{u}' scripts/hyaku/inline.sh scripts/hyaku/status.sh
scripts/hyaku/inline.sh:33:# directive 2026-10-20). Colocated lanes leave git HEAD detached, so never read `@{u}`/HEAD
$ grep -n -E '\bgit\b|rev-list|porcelain|push|HEAD' scripts/hyaku/status.sh; echo rc=$?
rc=1
```

So:

* `inline.sh` has **no** `@{u}` invocation. Its only `rev-list --count` is line 124 and it ranges
  over `origin/master..HEAD` on **`$FLEET`**, not on a lane. Lane ahead is already read from
  `jjl state` (line 117), which is pure git over `refs/heads/<branch>` and
  `refs/remotes/origin/<branch>` (comments at lines 32–34 state this deliberately).
* `status.sh` is 17 lines and contains **zero** git calls: only state files, `pool.txt`,
  `hyaku.env` and `events.log` (numbered lines 1–17; `grep` rc=1, empty output). `bash -x
  status.sh` produced no trace line containing `git` (count 0).
* The `@{u}` form the ticket describes survives only in historical generated prompt artifacts
  (33 files under `.ufo/prompts/closure/`, e.g. `kama-round-11.md`; command:
  `grep -rl -F "rev-list --count @{u}..HEAD" .ufo/prompts/closure | wc -l` → 33) and in report
  prose; the current closure contract actually **forbids** it
  (`scripts/hyaku/closure-prompt.md:24`: “test ancestry against the branch ref, never `@{u}`”).

Consequence: the line-124 `2>/dev/null || echo 0` is the only surviving silent-zero construct of the
`@{u}` family, and it is on the fleet root (a plain git repo today), not on a lane.

### F2. `@{u}` against a jj-colocated lane is state-dependent: it works after `init`, then fails the moment a jj mutation detaches HEAD

Fresh lane (sandbox `lane4`), immediately after `jj-lane.sh init`:

```
=== after init: symHEAD=master
@{u}: origin/master
@{u}..HEAD count: 0
```

After one helper commit (which sets the bookmark and pushes):

```
=== after helper commit: symHEAD=DETACHED
@{u}: fatal: HEAD does not point to a branch
@{u}..HEAD count: fatal: HEAD does not point to a branch
rc=128
masked: 0
refs count: 0
```

The masking pattern is the dangerous one. In sandbox `lane-jj`, which had two genuinely unpushed
commits:

```
colocated, detached? detached
$ git rev-list --count "@{u}..HEAD" 2>/dev/null || echo 0 -> 0
real local-vs-remote ahead: 2
```

`2>/dev/null || echo 0` turns a hard failure (rc 128) into “nothing ahead”, i.e. a skipped push and a
false `ahead=0` durability verdict. Any future edit that reintroduces `@{u}` for lane state
reintroduces this exact class.

Live sample (`mado-shokunin`, read-only): HEAD is currently **attached** and 8 commits ahead, so
`@{u}` works there right now and will start failing after the next jj mutation:

```
symHEAD: master
@{u}: origin/master
@{u}..HEAD: 8
refs ahead: 8
```

### F3. `inline.sh:118–121` makes a failed durability push non-fatal; `verify` still reports `OK … landed` with the tip absent from origin

Clean reproducer (`lane2`): helper commit with an unreachable origin exits 3 after keeping the
commit:

```
stdout: committed 17c7a68be5d88ba15b69de781708712cb8b0ad7d
rc: 3
stderr: … jj-lane: push failed after 3 attempts: … Error: Could not find repository at '…/does-not-exist.git'
state branch=master local=17c7a68… remote=9163925… ahead=1 behind=0 head=detached …
HEAD state: detached
hash on origin? no
```

Replaying the exact verify block (lines 117–129) with that lane:

```
ahead=1
WARN lane push failed
push stderr: jj-lane: push failed after 3 attempts: … Error: Could not find repository at '…/does-not-exist.git'
leftover: (clean)
VERIFY FINAL: OK jj2 r2 landed: report <x> lane tip 17c7a68be
post-verify ahead=1 origin-has-hash=no
```

`"${pushcmd[@]}" >/dev/null && {…} || { ev push-failed; echo WARN; }` has no `exit`, so the later
`log complete`/`ev complete`/`echo OK` run unconditionally. The helper's own exit 3 (“committed but
push failed”) is also collapsed into the same WARN. This directly contradicts the stated invariant
“landed = committed AND pushed before a report cites the hash”; the closure prompt would catch it one
step later, but `verify` has already emitted a false landed line and a `complete` event.

### F4. `inline.sh:117` treats an unreadable lane state as “nothing ahead”

`ahead=$(st_field "$(jjl state "$cwd" 2>/dev/null)" ahead)` then `[ "${ahead:-0}" != 0 ]`:
`jjl state`'s stderr is discarded and an empty result becomes 0. With a missing lane directory:

```
ahead='' (empty -> :-0 is 0)
push SKIPPED
leftover: (no lane to read) (empty -> no warning)
VERIFY FINAL: OK jjtest r1 landed: report <x> lane tip <-- empty
```

The command still exits 0 and prints `OK … landed` with an empty tip. The same masking applies to any
state failure: helper missing, repo corrupt, or a state line that no longer carries `ahead=`.

### F5. `inline.sh:123` (`git status --porcelain`) is *not* broken by jj — but it is warn-only, and its count conflates tracked leftovers with seat scratch

In a colocated lane with HEAD detached, `git status --porcelain` still reflects jj's working-copy
changes correctly. After a helper commit of `f.txt` only, with `sub/a.txt` also modified:

```
-- after partial commit (sub/a.txt should be leftover)
   ahead(@{u}):  fatal: HEAD does not point to a branch
   ahead(refs):  0
   porcelain(1 lines):
      M sub/a.txt
```

But the exact line-123 block on a dirty colocated lane:

```
symHEAD=DETACHED
--- exact old line 123 ---
WARN lane repo has uncommitted changes: 1 paths
rc_after_warn=0
--- old line 129 shape; $rep substituted with a lane path for the sandbox ---
OK jj3 r3 landed: report 31d8758 lane tip 31d8758cf
verify_would_exit=0
```

So uncommitted tracked round work coexists with `OK landed` and exit 0. Additionally the single
`wc -l` counts `??` scratch (seat notes, caches) exactly like a tracked modification: on a clean
detached lane with one untracked file the exact line 123 printed `WARN … 1 paths` (the proposed
split on the same tree gives `tracked=0 untracked=1`). jj-specific correctness is fine here; the
defect is the warn-only semantics.

### F6. `inline.sh:124` (`rev-list --count origin/master..HEAD` on the fleet root) is attachment-independent, but its `|| echo 0` masks any resolution failure, and it hardcodes `origin/master`

Detached HEAD does **not** break this range:

```
$ git rev-list --count origin/master..HEAD
2
[rc=0]
```

but deleting `refs/remotes/origin/master` (or any typo/missing ref) silently yields the “caught up”
answer:

```
old  origin/master..HEAD (ref deleted)  : 0
new  refs/...:refs/... (ref deleted)    : 1
```

The in-repo precedent is already correct: `fleet-commit.sh:60–63` uses
`git rev-list --count "$REMOTE/$BRANCH..HEAD" 2>/dev/null || echo 1` (fail-**open** to “push”) and
`git push -q "$REMOTE" "HEAD:$BRANCH"` (refspec pushed from HEAD, no attachment or upstream
required). `inline.sh` should mirror that.

### F7. `inline.sh:119` selects the VCS by `.jj` presence, and the `git push -q` fallback is fatal from a detached HEAD

The selection itself is fine in practice (colocated lanes have `.jj`; the helper writes it), but the
fallback is not attachment-safe:

```
HEAD: HEAD
$ git push -q
fatal: You are not currently on a branch.
To push the history leading to the current (detached HEAD)
state now, use

    git push origin HEAD:<name-of-remote-branch>
[rc=128]
```

and the same on a git-only lane an operator detached (`jjl state` still resolves the branch via
`origin/HEAD`, `head=detached`, `ahead=0`). Because the fallback is only reached when `.jj` is
absent (a partially initialized lane, or a rollback), this is an edge — but under F3 the failure
would then be swallowed anyway.

### F8. Helper edge (out of file scope): `detect_branch` trusts a symbolic HEAD whose ref is unborn, producing `branch=jj/root local=- ahead=0`

Reproduced artificially by deleting `refs/remotes/origin/master` and then failing a push:

```
$ git for-each-ref --format='%(refname)' refs/heads/
refs/heads/master
$ cat .git/HEAD
ref: refs/jj/root
$ git symbolic-ref -q --short HEAD
jj/root
state branch=jj/root local=- remote=- ahead=0 head=attached
```

`jj-lane.sh` prefers `symbolic-ref --short HEAD` without verifying `refs/heads/<b>` exists. `local=-`
then feeds line 117 (`ahead=0`, push skipped) and line 129 (empty tip). This is the same fail-silent
class as F4; the proposal below rejects `local=-`. `jj-lane.sh` is the helper owner's file — I did not
edit it.

### F9. `inline.sh:111` and `:129` (fleet-root report checks) are jj-safe today

The fleet root is plain git (live read-only check: `HEAD=master`, `origin/master` present,
`rev-list --count origin/master..HEAD` = 0; the report path has a commit and an empty status), and
both commands are attachment-independent — a detached sandbox clone still returned the report
commit:

```
detached symHEAD= DETACHED
status --porcelain -- r.md : []
log -1 --format=%H -- r.md : d50a7d8780ff63836019e8e7ca24ae6cd55c6085
```

No change is required for jj; an optional hardening is in R4.

### Behavior matrix (measured)

| command | git-only, attached | colocated, attached | colocated, detached | failure mode |
|---|---|---|---|---|
| `rev-list --count '@{u}..HEAD'` (absent from both files) | 0 (works) | 0 / 8 (works) | `fatal: HEAD does not point to a branch`, rc 128 | masked to `0` by `2>/dev/null \|\| echo 0`; true ahead can be 2 |
| `status --porcelain` (lane, :123) | works | works | works (` M sub/a.txt`) | warn-only; untracked scratch counted |
| `git push -q` (lane fallback, :119) | works | works | fatal rc 128 | only reached when `.jj` is absent |
| `rev-list --count origin/master..HEAD` (fleet, :124) | works | n/a | works (2) | missing ref/typo → `0` via `\|\| echo 0` |
| `jjl state` ahead (:117) | works (`ahead=1`) | works | works (`ahead=0`) | empty on state failure; `local=-` on unborn symbolic HEAD |

## Inference

* **[INFERENCE]** `jjl state`'s `ahead` is the correct attachment-agnostic substitute for
  `@{u}..HEAD` because it ranges `refs/remotes/origin/<branch>..refs/heads/<branch>`; the
  measurements above show it tracking true ahead in both attached and detached states.
* **[INFERENCE]** `verify`'s un-locked `git status` / `git rev-list` reads can race a concurrent jj
  mutation that resets the git index; a torn/partially written index would surface as an empty
  status (missed WARN). Not reproduced deterministically; the helper's flock covers only helper
  mutations, and `verify` takes no lock.
* **[INFERENCE]** The WARN-only push is not currently catastrophic because the closure prompt
  (`closure-prompt.md:24–26`) requires `jj-lane.sh state` to show `ahead=0` before a closure admits
  a round; the false `OK landed` is a one-round-delayed defect rather than silent loss of a commit.
* **[INFERENCE]** If the fleet root were ever colocated, `fleet-commit.sh`'s `git commit` would run
  on a detached HEAD (creating a detached commit) while `git push HEAD:master` moves the remote;
  local `master` would stay stale. Current plan keeps the fleet root git-only, so this is not active.

## Recommendations (proposal only — nothing was edited)

### R1. Replace `inline.sh:117–122` (durability push) with a fail-loud, post-verified block

```bash
  st=$(jjl state "$cwd" 2>/dev/null) || st=
  ahead=$(st_field "$st" ahead); local_h=$(st_field "$st" local); remote_h=$(st_field "$st" remote)
  if [ -z "$local_h" ] || [ "$local_h" = - ] || [ -z "$ahead" ]; then
    ev "lane-state-unreadable lane=$lane round=$n"
    echo "FAIL lane state unreadable: $cwd"; exit 1
  fi
  if [ "$ahead" != 0 ] || [ -z "$remote_h" ] || [ "$remote_h" = - ]; then
    if [ -d "$cwd/.jj" ]; then pushcmd=(jjl push "$cwd"); else pushcmd=(git -C "$cwd" push -q); fi
    "${pushcmd[@]}" >/dev/null 2>&1 \
      || { ev "push-failed lane=$lane round=$n"; echo "FAIL lane push failed: tip $local_h not on origin"; exit 1; }
    st=$(jjl state "$cwd" 2>/dev/null) || st=
    ahead=$(st_field "$st" ahead); local_h=$(st_field "$st" local); remote_h=$(st_field "$st" remote)
    if [ "$ahead" != 0 ] || [ -z "$local_h" ] || [ "$local_h" = - ] \
       || [ -z "$remote_h" ] || [ "$remote_h" = - ] \
       || ! git -C "$cwd" merge-base --is-ancestor "$local_h" "$remote_h" 2>/dev/null; then
      ev "push-unverified lane=$lane round=$n"
      echo "FAIL lane push unverified (ahead=$ahead local=$local_h remote=$remote_h)"; exit 1
    fi
    ev "durability-push lane=$lane round=$n"; echo "PUSHED lane repo (L1 left it unpushed)"
  fi
```

Why each change: `st` is captured once so a failed/empty state cannot become `ahead=0`; `local=-`
(the F8 sentinel) is rejected; the push's rc 0 is required (exit 3 no longer passes); after the push
the state is re-read and the cited tip must be reachable from the remote-tracking ref, so the OK line
cannot cite an unpushed hash. Colocated and git-only lanes both flow through `jjl state`; only the
push command differs, as today.

### R2. Replace `inline.sh:123` (leftover check) with tracked-vs-untracked semantics

```bash
  tracked=$(git -C "$cwd" status --porcelain 2>/dev/null | grep -c '^[ MADRCU][MADRCU ]')
  untracked=$(git -C "$cwd" status --porcelain 2>/dev/null | grep -c '^??')
  if [ "${tracked:-1}" != 0 ]; then
    ev "lane-dirty lane=$lane round=$n tracked=$tracked untracked=$untracked"
    echo "FAIL lane repo has uncommitted tracked changes: $tracked paths"; exit 1
  fi
  [ "${untracked:-0}" != 0 ] && echo "WARN lane repo has $untracked untracked path(s)"
```

`git status --porcelain` is the right primitive in a colocated lane (F5): jj keeps HEAD at `@-`, so
the working-copy diff is visible. The split keeps seat scratch (untracked) advisory while making
uncommitted round work fatal, matching “landed”. `grep -c` failing (git error) yields an empty value
and `${tracked:-1}` fails closed. If behavior must stay advisory, line 123 needs **no** jj change;
only the false `OK` is the issue.

### R3. Replace `inline.sh:124–126` (fleet-root pending-push flush)

```bash
  fleet_ahead=$(git -C "$FLEET" rev-list --count refs/remotes/origin/master..refs/heads/master 2>/dev/null) || fleet_ahead=1
  if [ "${fleet_ahead:-1}" != 0 ]; then
    "$H/fleet-commit.sh" --as "$lane" -m "round-$n: $lane report" -- "$rep" >/dev/null 2>&1 \
      || ev "fleet-push-pending lane=$lane round=$n ahead=$fleet_ahead"
  fi
```

Refs-only range (no HEAD/upstream), failure defaults to “pending” (fail-open) instead of 0, and the
commit message is no longer `unused` if the sweep path ever creates a commit here. Matches
`fleet-commit.sh`'s own `|| echo 1` convention.

### R4. Optional (`inline.sh:111`): anchor “committed” to the branch tip tree instead of “some commit reachable from HEAD”

```bash
  if [ -n "$(git -C "$FLEET" status --porcelain -- "$rep")" ] \
     || ! git -C "$FLEET" cat-file -e "refs/heads/master:$rep" 2>/dev/null; then
```

Not jj-required (F9); it additionally catches a report that was committed and later deleted in the
tip, which `git log -1 -- path` cannot.

### R5. `status.sh`: no jj replacement exists or is needed; optionally surface lane VCS state

The file has no git calls, so there is nothing to make detached-HEAD-safe. It is also VCS-blind: an
operator cannot see `ahead`, a detached HEAD, or a failed push from `status.sh`. If that visibility is
wanted, an optional read-only block after the lane loop (after current line 13):

```bash
echo "== lane VCS (jj-lane.sh state: pure git, read-only; attached/detached agnostic)"
while read -r l _; do
  case $l in ''|\#*) continue ;; esac
  d=${SHOKUNIN_ROOT:-/home/vgpnk/Projects/shokunin}/$l-shokunin
  [ -d "$d/.git" ] && printf '  %-10s %s\n' "$l" "$("$H/jj-lane.sh" state "$d" 2>/dev/null)"
done < "$H/pool.txt"
```

Caveat: this assumes the `<id>-shokunin` naming used by every current `pool.txt` lane; the driver's
`LANES` table is authoritative if a fleet meta-lane is ever added to the pool. It runs one
`git status` per lane (`jj-lane.sh state` is pure git), so it is read-only and cannot snapshot jj.

### R6. Helper-owner note (not this seat's file): validate the symbolic HEAD

`jj-lane.sh`'s `detect_branch` should treat a symbolic HEAD as a branch only if
`git show-ref -q --verify refs/heads/<b>` succeeds; otherwise fall through to `origin/HEAD` /
`master` / `main`. Today an unborn `refs/jj/root` yields `branch=jj/root local=-` (F8), which R1's
`local=-` guard converts into a loud FAIL instead of a false OK.

## Residual risks / verification gaps

* The index-race between `verify`'s unlocked `git status` and a concurrent jj mutation (F5 note) was
  reasoned, not reproduced; a torn index would currently look like “clean” and only matter if R2 is
  adopted (which fails closed).
* `jjl state` runs `git status --porcelain` internally; in the idle sandbox the index bytes and mtime
  were unchanged across the call (`md5sum .git/index` identical, mtime unchanged), but git may
  refresh a dirty stat cache in general.
* The F8 reproducer used an artificial `git update-ref -d refs/remotes/origin/master`; normal helper
  flows never delete remote refs, so treat it as a robustness edge, not a live incident.
* Live lane evidence is a snapshot: only `mado` and `tameshi` are colocated today, both attached at
  read time; `mado` was 8 ahead, `tameshi`/`tabi`/`kama` in sync.
* All commands and failure states are preserved in `/fast/scratch/jj-wave/JjAuditInlineSh-2/`
  (`phase1.sh`–`phase5.sh` and their lanes). Live repos were never written.
