# JjDocConcurrency — concurrent jj processes in one repo (jj 0.45.x)

Scout: `JjDocConcurrency-2`. Scope: op-log merge semantics, working-copy locking,
when op heads diverge, safe multi-agent commit patterns, failure modes — for
jj 0.45.x, in service of moving shokunin lane-repo writes to jj.

**Environment.** `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`;
`git 2.56.0`; Linux x86_64 (kernel 7.2.11-arch1-1). Upstream source and docs are
pinned to tag `v0.45.1`, which `git ls-remote` confirms is commit
`7c41cdeb16b6b321c64e789a966b6adf723816a5` — the exact build under test. Note
that `https://docs.jj-vcs.dev/latest/` now serves **0.46.0** (released
2026-10-07), so every docs citation below uses the versioned tree
`https://docs.jj-vcs.dev/v0.45.1/…` instead. The 0.46.0 changelog was read and
contains no change to op-log merging, `working_copy.lock`, or divergence
semantics (its concurrency-adjacent items are `jj workspace add --[no-]colocate`
git worktrees and `jj undo`/`redo` refusing cross-workspace operations), so
these findings describe 0.45.x and are not contradicted by 0.46.0.

**Method.** Every behavioural claim below is backed by (a) a citation — docs URL,
`jj help` excerpt, or a source file in `v0.45.1` — and (b) a minimal experiment in
a fresh sandbox under `/fast/scratch/jj-wave/JjDocConcurrency/<eN>`, created with
`git init` + `jj git init --colocate`. No `jj` command was ever run with a working
directory or `-R` inside `/home/vgpnk/Projects/shokunin` or a live lane. Every
`origin` used for fetch/push experiments was a local bare repo inside the sandbox
and was confirmed with `git remote -v` before any push. No tool was installed or
upgraded for this report.

Confidence tags: **[EXP]** reproduced in a sandbox; **[SRC]** read in v0.45.1
source/help; **[INF]** inference, marked inline.

---

## 1. Findings

### 1.1 How the op log merges concurrent operations

#### F1. An operation is written as a child of the operation the process started from; nothing is locked during that write. **[EXP] [SRC]**

Citation — <https://docs.jj-vcs.dev/v0.45.1/technical/concurrency/#operation-log>:
> "When a command starts, it loads the repo at the latest operation."
> "When the operation completes, it is written with the start operation as parent."

and
> "It is left for the next command to notice if there were divergent operations."

Experiment E1 (`/fast/scratch/jj-wave/JjDocConcurrency/e1`) — force two
mutations from the same parent with `--at-op`:

```
$ OP=$(jj op log --no-graph -T 'id' -n 1)
$ jj --at-op=$OP describe -m 'side A'
$ jj --at-op=$OP describe -m 'side B'
$ ls .jj/repo/op_heads/heads
006e5c8c14384099becb1cdb4a97e98c3f39dc8567a5159f167a78b58926d617...
90f763ef8bbcf8c336af85eef3c957e8a6019bc13dbebddf79479f97f1ad628e...
```

Two files, no merge. `--at-op` is the documented substitute for real concurrency:
> "That works exactly the same as if any later operations had not existed when
> the command started." — <https://docs.jj-vcs.dev/v0.45.1/technical/concurrency/#operation-log>

#### F2. The merge happens lazily, in whichever process loads next, and is itself an operation named `reconcile divergent operations`. **[EXP]**

Same repo, E1, next command `jj log`:

```
Concurrent modification detected, resolving automatically.
@  3a9baaaf4b42 side A pwzyyppzstqx
│ ○  36aab0489bb4 side B pwzyyppzstqx
├─╯
○  64d4b621d147 base skzsyzowmmrp
```
```
$ ls .jj/repo/op_heads/heads | wc -l
1
$ jj op log --no-graph -T 'id.short() ++ " " ++ description ++ " p:" ++ parents.map(|p| p.id().short()).join(",")'
686944b7129c snapshot working copy p:eebdd568e4f8
eebdd568e4f8 reconcile divergent operations p:006e5c8c1438,90f763ef8bbc
```

The reconcile op has both former heads as parents. Note `jj log` also wrote a
`snapshot working copy` op — even `jj log` mutates. Source: `lib/src/repo.rs`
`load_at_head()` passes `transaction_description = Some("reconcile divergent operations")`;
the message string is in `cli/src/cli_util.rs:816`.

#### F3. Merging is a three-way merge of *views* against their closest common ancestor; a bookmark moved on both sides becomes a conflicted bookmark that keeps all targets. **[EXP] [SRC]**

Citation — <https://docs.jj-vcs.dev/v0.45.1/technical/concurrency/#merging-divergent-operations>:
> "it will do a 3-way merge of the view objects based on their common ancestor"
> "Conflicts are recorded in the resulting view object."

Experiment E7 (`.../e7`, two workspaces, both move `main` concurrently):

```
$ jj bookmark list
main (conflicted):
  - rwwnzppx b0966f30 base
  + qrqtpmnl da0ec2a2 (empty) b
  + oskzxowl 298e31d4 (empty) a
  @git (behind by 2 commits): oskzxowl 298e31d4 (empty) a
Hint: Some bookmarks have conflicts. Use `jj bookmark set <name> -r <rev>` to resolve.
$ jj status
Warning: These bookmarks have conflicts:
  main
```

`jj log` renders both targets as `main??`. On the Git side only one target is
exported: `git rev-parse main` → `298e31d415...` (side `a`), i.e. Git sees a
single, silently chosen side. Docs confirm this is expected:
> "When a `jj` branch is conflicted, the position of the branch in the Git repo
> will disagree with one or more of the conflicted positions."
— <https://docs.jj-vcs.dev/v0.45.1/git-compatibility/#colocated-jujutsugit-workspaces>

#### F4. Merging also rebases commits whose parent was rewritten by the other side. **[EXP] [SRC]**

Experiment E19 (`.../e19`) — a commit was created at an old op while another op
rewrote its ancestor:

```
$ jj st
Concurrent modification detected, resolving automatically.
Rebased 1 descendant commits onto commits rewritten by other operation.
```

Source: `lib/src/repo.rs`, `merge_operations()`:
`num_rebased += tx.repo_mut().rebase_descendants().await?;`
This is the same rule `jj undo` uses (CHANGELOG 0.x: "if one operation added B on
top of A, and one operation rebased A as A', then B would be automatically
rebased on top of A'").

#### F5. Operation objects and views are content-addressed and safely writable; only the head marker set is a directory of empty files (add new, then delete old). **[SRC]**

Citation — <https://docs.jj-vcs.dev/v0.45.1/technical/concurrency/#storage>:
> "The operation objects and view objects are stored in content-addressed storage"
> "we add a file pointing to the new operation and then remove the file pointing
> to the old operation"

Source `lib/src/simple_op_heads_store.rs`: `update_op_heads()` calls
`add_op_head(new_id)` first, then `remove_op_head(old_id)`; a missing old head is
explicitly tolerated ("It probably means that we're on a distributed file system
where the locking doesn't work"). Consequence: writing the new head is what makes
the operation visible, and a failed removal leaves two heads — exactly what F1
shows.

#### F6. The op-heads lock only prevents duplicate *merge* work; it is not required for correctness. **[SRC] [EXP]**

Citation — `lib/src/op_heads_store.rs`, `OpHeadsStore::lock` doc comment:
> "The purpose of the lock is to prevent concurrent processes from resolving the
> same divergent operations. It is not needed for correctness"

Experiment E12 (`.../e12`) — two divergent heads, then eight simultaneous
`jj --ignore-working-copy log` loads:

```
$ ls .jj/repo/op_heads/heads | wc -l   # before
2
$ for i in $(seq 1 8); do jj --ignore-working-copy log -r @ --no-graph -T commit_id.short() & done; wait
$ ls .jj/repo/op_heads/heads | wc -l   # after
1
$ jj --ignore-working-copy op log --no-graph -T 'if(description.contains("reconcile"),"x\n","")' | wc -l
1
```

Eight races, exactly one reconcile op. The lock is a `flock` on
`.jj/repo/op_heads/lock` (`simple_op_heads_store.rs`, `lock()`), and the resolver
re-reads the head list after taking it ("We take a lock, then check if there are
still no/multiple heads").

#### F7. `--ignore-working-copy` skips the snapshot and the working-copy lock, but it does **not** skip op-head integration. **[EXP] [SRC]**

`jj -h` excerpt:
```
--ignore-working-copy   Don't snapshot the working copy, and don't update it
```
E12 proves the second half: all eight commands were `--ignore-working-copy log`
and they still created the reconcile op. `--at-op` implies `--ignore-working-copy`
(`jj help`), and `--at-op=@` additionally *disables* merging: with two heads,

```
$ jj op log --at-op=@
Error: The "@" expression resolved to more than one operation
Hint: Try specifying one of the operations by ID: 9d08641ad9d2, 456d44f5b1f6
$ ls .jj/repo/op_heads/heads | wc -l
2
```

This is the expected behaviour, not a bug — the same snapshot exists in
`cli/tests/test_concurrent_operations.rs:33-43`. It is the cheapest way to detect
divergence without resolving it (the hint lists the divergent op ids).

#### F8. A computed op can be withheld from the op log and published later. **[EXP] [SRC]**

`jj help op integrate`:
> "By default, operations are automatically integrated into the operation log,
> but `--no-integrate-operation` or internal errors may cause that to not happen."

Experiment E21 (`.../e21`):

```
$ jj describe -m staged2 --no-integrate-operation
Operation left uncommitted because --no-integrate-operation was requested: 0324ccde4f9e
$ ls .jj/repo/op_heads/heads | wc -l
1
$ jj --at-op=0324ccde4f9e log -r @ --no-graph -T description
staged2
$ jj log -r @ --no-graph -T description      # still unpublished
(empty)
$ jj op integrate 0324ccde4f9e
$ jj log -r @ --no-graph -T description
staged2
```

---

### 1.2 How the working copy is locked

#### F9. Each workspace has its own `working_copy.lock` path; acquisition is a **blocking** `flock`, and the state is re-read after the lock is taken. **[EXP] [SRC]**

Citation — `lib/src/local_working_copy.rs`, `start_mutation()`:
```rust
let lock_path = self.state_path.join("working_copy.lock");
let lock = FileLock::lock(lock_path)...
// Re-read the state after taking the lock
```
Citation — `lib/src/lock/unix.rs`:
> "Acquire an exclusive lock on `path`, blocking until it's available."

Experiment E5 (`.../e5`) — a detached `flock` holds `.jj/working_copy/working_copy.lock` for 4 s:

```
$ setsid nohup flock "$LOCK" sleep 4 ... & sleep 0.5
$ jj new -m fourth
rc=0 elapsed_ms=3422
$ jj --ignore-working-copy log -r @ --no-graph -T commit_id.short()
rc=0 elapsed_ms=7 out=973a7deb9bfd
```

The snapshotting command blocked for almost the full hold time; the
`--ignore-working-copy` read did not touch the lock. E18 repeats it with
`jj status`: `jj status rc=0 elapsed_ms=2604` against a 3 s hold.

#### F10. The lock is per workspace, not per repository. **[SRC]**

`lock_path = self.state_path.join("working_copy.lock")`, where `state_path` is
the workspace's own `.jj/working_copy/`. Two workspaces of one repo therefore do
not serialize on each other's file-level state. E6 (`.../e6`) runs `jj new`
simultaneously in the default workspace and in `w2`; both exit 0 and both commits
are visible:

```
rc w1=0 w2=0
@  from-w1 | rzkoqyvwqkln
○   | pszkmyvsnyl
│ ○  from-w2 | urwmvkxomrnx
│ ○   | tzxylwmplqxz
├─╯
○  base | wxloqzlvroqu
```

#### F11. The working-copy lock is held only for the working-copy mutation, not for the whole command — so it cannot by itself serialize two `jj` processes. **[SRC] [EXP]**

Source path per command (`cli/src/cli_util.rs`):

* `snapshot_working_copy()` acquires the lock at line 2103, writes the
  `snapshot working copy` op, then `locked_ws.finish(...)` at ~2266 drops it.
* the command then builds its own transaction (`jj commit` rewrites `@`);
* `WorkspaceCommandTransaction::finish()` re-acquires the git import/export lock
  and calls `finish_transaction` → `update_working_copy` → `check_out` →
  `start_working_copy_mutation()` — the wc lock is taken a **second** time.

Between those two windows another process can load, write an op, and check out.
That is why a lock exists yet divergence is still normal. Experiment E2
(`.../e2`, six simultaneous `jj new` in one workspace):

```
$ for i in $(seq 1 6); do (jj new -m "c$i" > out.$i 2>&1; echo $? > rc.$i) & done; wait
$ grep -h -i 'error\|stale\|concurrent' out.* | sort | uniq -c
      2 Caused by: Concurrent checkout
      1 Concurrent modification detected, resolving automatically.
      1 Internal error: Failed to check out commit 4a7cb007e6473001c7c56f9b46542d7300717799
      1 Internal error: Failed to check out commit f64a3924aec2845e68424e7ff910d19a8ab3f2f6
$ ls .jj/repo/op_heads/heads | wc -l
3
```

The `Concurrent checkout` check is `lib/src/workspace.rs::check_out()`:
```rust
if let Some(old_tree) = old_tree
    && old_tree.tree_ids_and_labels() != locked_ws.locked_wc().old_tree().tree_ids_and_labels()
{
    return Err(CheckoutError::ConcurrentCheckout);
}
```
with the source comment "It's safe to check out another commit regardless, but
it's probably not what the caller wanted", and a `TODO` in `cli_util.rs` that it
"should probably just result in a warning for most commands" — in 0.45.1 it is
still `internal_error_with_message("Failed to check out commit …")`.

#### F12. In a colocated repo `jj` additionally takes `<repo>/git_import_export.lock` around the snapshot/import window and again around the transaction-finish/export window; that only serializes jj-vs-jj. **[SRC] [EXP]**

Source `cli/src/cli_util.rs:480-486`:
```rust
// Acquire the lock to ensure that the loaded repo points to the head
// operation whose refs should be synchronized with the Git repo. This
// prevents races with other processes during Git HEAD and refs
// import/export.
```
It is a no-op for non-colocated workspaces (`working_copy_shared_with_git`).
Concurrent jj processes still produced Git-HEAD export failures — E2 and E14:

```
Warning: Failed to update Git HEAD ref
Caused by: The reference "HEAD" should have content 711fc8607205..., actual content was d5dbccf23821...
```

This is consistent with the 0.36.0 CHANGELOG entry
(<https://github.com/jj-vcs/jj/blob/v0.45.1/CHANGELOG.md>):
> "Fixed race condition that could cause divergent operations when running
> concurrent `jj` commands in colocated repositories."

and with the docs' broad caveat:
> "There may still be bugs when interleaving mutating `jj` and `git` commands"
— <https://docs.jj-vcs.dev/v0.45.1/git-compatibility/#colocated-jujutsugit-workspaces>

#### F13. After concurrent mutations, a workspace can be left "stale", and *every* command then fails until `jj workspace update-stale`. **[EXP] [SRC]**

E2, immediately after the six-way race:

```
$ jj log
Concurrent modification detected, resolving automatically.
Error: The working copy is stale (not updated since operation 2dd91108c144).
Hint: Run `jj workspace update-stale` to update it.
```

Even `jj file list -r @` failed the same way. Citation —
<https://docs.jj-vcs.dev/v0.45.1/working-copy/#stale-working-copy>:
> "If step 3 doesn't happen for some reason, the working copy is considered "stale"."

The freshness decision is `lib/src/working_copy.rs::WorkingCopyFreshness`:
`Fresh` / `Updated(op)` (reload at the wc's newer op) / `WorkingCopyStale`
("The working copy is behind the latest operation.") / `SiblingOperation`
("The working copy is a sibling of the latest operation."). The sibling case has
its own hint: "Run `jj op integrate …` to add the working copy's operation to the
operation log."

#### F14. `jj workspace update-stale` can delete files that appeared between racing snapshots — including files another process created. **[EXP]** (mechanism **[INF]**)

E2 continuation:

```
$ jj workspace update-stale
Parent commit (@-)      : zsxrpzqw d5dbccf2 (no description set)
Added 0 files, modified 6 files, removed 4 files
Updated working copy to fresh commit f64a3924aec2
$ git ls-files
f
out.1
out.2
out.3
out.4
out.5
out.6
$ ls
f  out.1  out.2  out.3  out.4  out.5  out.6  rc.2  rc.3  rc.5  rc.6
```

Two files the shell wrote during the race (`rc.1`, `rc.4`) were gone afterwards,
and four files were reported "removed". The `out.*` files that a racing snapshot
captured were auto-tracked (`git ls-files` lists them), which is the documented
default: "added files are implicitly tracked by default"
(<https://docs.jj-vcs.dev/v0.45.1/working-copy/>). Mechanism [INF]: a snapshot in
process A captures a file that process B's in-flight checkout does not know
about (or vice versa); after the op merge, `update-stale` checks out the winning
working-copy commit and removes paths absent from it that the stale working-copy
state considered tracked. The victims are timing-dependent; the run above is one
observed outcome, not a deterministic repro.

---

### 1.3 When op heads diverge

#### F15. Divergence condition (precise). **[SRC] [EXP]**

An op is written as a child of the op the process loaded (F1). Therefore two op
heads exist whenever either:

1. **two mutating processes overlap in time** and both loaded the same op (E2, E6,
   E7, E14, E17 all show this; op heads = 2 or 3 before the next command);
2. **a mutating command is run with `--at-op=<op that is not the sole head>`** —
   documented: "If the command is mutational, that will result in a fork in the
   operation log" (<https://docs.jj-vcs.dev/v0.45.1/technical/concurrency/#operation-log>);
   E1 and E19 use this as a deterministic reproducer;
3. **the head-marker update is not atomic across a filesystem boundary**
   (`add_op_head` then `remove_op_head`, F5): rsync/NFS/Dropbox copies, or a
   crash between the two syscalls. Docs: "it's possible to update copies of the
   clone on different machines and then let `rsync` … merge them"
   (<https://docs.jj-vcs.dev/v0.45.1/technical/concurrency/#syncing-with-rsync-nfs-dropbox-etc>).

Non-causes, checked: a single held `working_copy.lock` does not prevent (1) —
F11; `--ignore-working-copy` does not prevent (2) — F7/E12; a merge is not
required for the repo to stay usable — F2/F3.

Heads are visible without merging as files, or through the `--at-op=@` error hint
(F7), or as `@` becoming ambiguous:
```
$ jj --at-op=@ describe -m x
Error: The "@" expression resolved to more than one operation
Hint: Try specifying one of the operations by ID: 5b599c0cbe9b, 270d7792f64e
```

#### F16. Divergent *commits* (same change id twice) are the commit-level analogue, and are marked `(divergent)`. **[EXP]**

E1 after the view merge: `side A` and `side B` are two visible commits with the
same change id `pwzyyppzstqx`. E18's `jj status` shows the marker directly:

```
The working copy has no changes.
Working copy  (@) : svvytxmt/1 669f864a (divergent) (empty) A
Parent commit (@-): vtzkuzul 386cde13 base
```

0.45.0 added the remedy, `jj converge`
(<https://github.com/jj-vcs/jj/blob/v0.45.1/CHANGELOG.md>):
> "The new `jj converge` command attempts to automatically resolve divergence"
`jj help converge`: "Attempts to resolve divergence by replacing two or more
visible revisions for a given change with a single revision."

---

## 2. Failure modes (named, with the run that shows each)

| # | Failure mode | Observed evidence | Consequence |
|---|---|---|---|
| FM1 | **Silent branch/commit loss under unguarded concurrent commits.** Four agents each `jj commit -- <own file>` + `jj bookmark set main -r @-` + push, no external lock (E14). | `main` and `origin/main` ended at `a4` (`3bcfc13`); `a1`, `a2`, `a3` are visible in `all()` but **not ancestors of `main`**: `jj log -r 'all() ~ ::main'` lists `5542e90a a1`, `34fc75b75cce a3`, `d015f2df5ef5 a2`. | A commit hash an agent could cite is not on the branch and was never pushed. This directly breaks the "cited hash is an ancestor of the branch" invariant. |
| FM2 | **Remote lease rejection.** Concurrent pushes of the same branch (E14). | `remote: error: cannot lock ref 'refs/heads/main': is at 3bcfc13b5e15... but expected 6eb3c0275601...` / `Error: Failed to push some bookmarks`. | Push must be retried after fetch+rebase (the helper does this); a caller that ignores the push rc will report a hash that is not on the remote. Docs: "If there is a conflict, `jj` will refuse to push the bookmark" (<https://docs.jj-vcs.dev/v0.45.1/bookmarks/#pushing-bookmarks-safety-checks>). |
| FM3 | **Conflicted bookmark.** Two processes move the same bookmark from the same base (E7). | `main (conflicted)` with three targets; `main??`; `jj log -r main` → `Error: Name 'main' is conflicted`; `jj git push` → `Error: Bookmark main is conflicted`. | Push is impossible until `jj bookmark set`; revsets naming the branch become ambiguous. Docs: "Both can end up in that state if concurrent operations were run in the repo" (<https://docs.jj-vcs.dev/v0.45.1/bookmarks/#conflicts>). |
| FM4 | **Divergent commits** (same change id twice). E1, E18. | Two visible `side A`/`side B` with one change id; `(divergent)` marker in `jj status`. | Ambiguous working-copy history; needs `jj converge`/`jj abandon`; `jj new <change>`-style selection can resolve to multiple revisions. |
| FM5 | **Stale working copy blocks everything.** E2. | `Error: The working copy is stale (not updated since operation 2dd91108c144)` for `jj log`, `jj file list`, etc. | Any automation that runs `jj` in that workspace fails until `jj workspace update-stale`; the helper's `--ignore-working-copy` reads keep working, its `commit` does not. |
| FM6 | **`Internal error: Concurrent checkout`.** E2 (2 of 6 processes). | `Internal error: Failed to check out commit … / Caused by: Concurrent checkout`; the CLI wraps it as an internal error and does not retry (source TODO confirms). | A mutation that already wrote its op can still fail to leave the working copy consistent; exit status alone is not enough to know whether the op landed. |
| FM7 | **File loss / auto-track capture.** E2. | `removed 4 files` from `update-stale`; `rc.1`/`rc.4` missing; `git ls-files` shows the racy `out.*` files were auto-tracked. | A racing snapshot can swallow another process's in-progress files into a commit, and a later checkout/repair can delete them from disk. Mitigated by `snapshot.auto-track="none()"` (helper) but not by locking alone. |
| FM8 | **Colocated Git HEAD export failure.** E2, E14. | `Warning: Failed to update Git HEAD ref / Caused by: The reference "HEAD" should have content …, actual content was …`. | Non-fatal warning, but Git-eyes state (HEAD) can disagree with jj; harmless for the helper, which reads branches/bookmarks, not HEAD. |
| FM9 | **`--ignore-working-copy` still writes (reconcile op).** E12. | Eight "read-only" loads produced one `reconcile divergent operations` op. | "Read-only" jj calls are not side-effect-free with respect to the op log; running them outside the lane lock can interleave with a commit's op. |
| FM10 | **Lock starvation / no timeout.** E5, E18. | `jj new` waited 3422 ms for a 4 s hold; `jj status` waited 2604 ms for a 3 s hold. `FileLock::lock` has no timeout. | A hung jj process holding `working_copy.lock` blocks every other jj command in that workspace indefinitely; the helper's own `flock -w 300` bounds its wait, not jj's. |

---

## 3. Safe patterns for several agents committing in one repo

### P1. One external exclusive lock around every jj mutation of a repo — **the pattern the helper already uses**. **[EXP]**

Replicated the helper's sequence by hand (E15, `.../e15`): 4 agents, disjoint
files, each block wrapped in `flock <lock> bash -c 'jj file track … && jj commit -m … -- <file> && jj bookmark set main -r @- && jj git push --remote origin --bookmark main'`.

```
$ ls .jj/repo/op_heads/heads | wc -l
1
$ git -C ../e15-remote.git log --oneline main
68f7b23 a2
d63620d a4
c1cd402 a3
02d2e0d a1
a30a053 base
$ git -C ../e15-remote.git show --stat --format= 02d2e0d
 f1 | 1 +
```
All four commits form one linear chain, all four are on `main` locally and on the
remote, and each commit contains exactly its own path (pathspec limiting held).
Contrast E14 (same workload, no flock): only `a4` reached the branch.

### P2. One workspace per agent (`jj workspace add`), with **per-agent bookmarks**. **[EXP]**

E17 (`.../e17`): two workspaces `w1`/`w2`, each committing its own file and
pushing its own bookmark (`lane-w1`, `lane-w2`):

```
heads before integration: 2
$ jj bookmark list
lane-w1: nomuqqkk 4a27ba55 one
lane-w2: wlkskrxr 306f82c3 two
main: qzwvnxoo d719ab95 base
$ git -C ../e17-remote.git for-each-ref --format='%(refname:short) %(objectname:short)'
lane-w1 4a27ba5
lane-w2 306f82c
main d719ab9
```
No errors, no conflicted bookmark, both commits pushed. Op heads did diverge
transiently (2) and were reconciled by the next command — that is expected and
harmless when the refs are disjoint.

Caveat for 0.45.x: `jj workspace add` creates a jj-only workspace with no `.git`
of its own, so `git` commands do not work there. 0.46.0 adds
`jj workspace add --[no-]colocate` (a Git worktree); that variant was not tested
here (see §5 item 8).

### P3. Do not share a bookmark between concurrent agents. **[EXP]**

E6 shows separate workspaces committing concurrently is fine; E7 shows the same
setup moving one shared bookmark produces `main??` and a push refusal (FM3). If
two agents must advance one branch, serialize the bookmark move + push (P1), or
have each push its own bookmark and merge afterwards with `jj rebase`/PR flow.

### P4. Treat every jj invocation in a shared repo as a mutation; use pure Git or `--ignore-working-copy` for inspection. **[EXP] [SRC]**

* `jj log` in E1 wrote `snapshot working copy` (and would have created a
  reconcile op had the heads diverged).
* `jj status` in E18 under a held lock waited and then reconciled.
* `jj --ignore-working-copy log` still creates the reconcile op (E12).
* The helper's `state` is pure `git` (`print_state` never calls jj) — correct.
  Its `jj_ids` calls use `--ignore-working-copy`, so they skip the wc lock but can
  still integrate ops; that is only safe because they run inside the lane flock.

### P5. Verify what you cite, after the push. **[EXP]**

E14 is the counter-example that motivates it: the local commit `a1` existed but
was unreachable from the branch, and two pushes were rejected. The helper's
`do_push` prints `pushed $(heads($BRANCH@origin))` — the remote tip, not the
local `@-` — which is the right anchor. A cheap extra assertion
(`git merge-base --is-ancestor <hash> refs/heads/<branch>`) would close the gap
if anything ever bypasses the lock. [INF]

### P6. Prefer `--no-integrate-operation` + `jj op integrate` when an operation must be prepared and published as one step. **[EXP]**

E21 shows it works: the op is computed (visible via `--at-op=<id>`), the head is
untouched, and `jj op integrate` publishes it. Not needed by the current helper
(it holds a lock instead), but it is the only jj-native way to stage a mutation
without making it visible.

---

## 4. Consequence for the planned shokunin integration

1. **The helper's external `flock` is necessary, and sufficient within the tested
   lane workload.** P1/E15 replicate its jj sequence (`jj file track` →
   `jj commit -m … -- <paths>` → `jj bookmark set` → `jj git push`) with four
   concurrent writers and produce a single linear, fully-pushed chain. Without it, E14 shows the invariant "a cited hash stays an
   ancestor of the branch" failing: three of four commits were orphaned while
   `main`/`origin/main` moved to the fourth.
2. **The jj locks cannot replace the helper's lock.** `working_copy.lock` is
   held only around the snapshot and the checkout (F11) and is per workspace
   (F10); `git_import_export.lock` is jj-vs-jj only (F12); the op-heads lock only
   de-duplicates merges (F6). All three are about internal consistency, not about
   serializing an agent's read-decide-write sequence.
3. **Every jj call in a lane must stay inside the flock, including "read-only"
   ones.** `jj log`/`jj status` snapshot (F11/F12, E1/E18) and
   `--ignore-working-copy` still integrates divergent ops (E12). Any seat, hook,
   or fleet tool that runs bare `jj` in a lane during a commit re-introduces the
   E2 failure class (`Concurrent checkout`, stale wc, file loss). The helper
   should remain the only jj entry point for lane repos; diagnostics should use
   `jj-lane.sh state` (pure Git) or explicit `--ignore-working-copy`.
4. **Keep `snapshot.auto-track="none()"`.** It is the only thing between the
   helper and FM7: with default `all()`, a racing snapshot auto-tracks whatever a
   seat just wrote (`out.*` in E2) and a later checkout/repair can delete it.
   The helper's explicit `jj file track` list is the right model.
5. **Push is the remaining non-serializable step.** Two different lane repos can
   push the same branch concurrently; jj refuses with FM2. The helper's
   fetch → rebase-only-unpushed → re-push loop is the documented recovery
   (<https://docs.jj-vcs.dev/v0.45.1/bookmarks/#pushing-bookmarks-safety-checks>)
   and its post-push readback of `heads($BRANCH@origin)` gives the hash a report
   may cite. Two notes:
   * on rejection the helper's `tip` revset uses `bookmarks($BRANCH)`; if that
     bookmark ever became *conflicted*, `bookmarks()` resolves to multiple
     revisions and `| head -1` picks one arbitrarily [INF]. The helper's current
     conflict guard checks `conflicts()` on `heads(bookmarks(...))` — i.e. tree
     conflicts, not bookmark conflicts. A `jj bookmark list --conflicted` guard
     before the retry loop would fail fast instead of retrying three times.
   * `jj commit -- <paths>` does not move bookmarks (`jj help commit`: "`jj
     commit` doesn't move bookmarks forward."), so the explicit `bookmark set …
     -r @-` after commit is required and must stay inside the lock.
6. **The lane flock key is `basename(lane-dir)`** (`$STATE/jj-$base.lock`), not
   the repo's absolute path. Two lanes with the same basename serialize
   needlessly (harmless); two paths to the *same* repo with different basenames
   would not serialize at all [INF]. In the current layout (distinct lane
   directories) this is not a correctness risk, but keying on
   `realpath(lane-dir)` would be strictly safer.
7. **Recovery playbook if a lane is ever left divergent** (e.g. a bypassed
   lock): `jj op log --at-op=@` (or `ls .jj/repo/op_heads/heads`) to confirm;
   any normal command merges the views; `jj status` to find `main??` /
   `(divergent)`; `jj bookmark list --conflicted`; `jj workspace update-stale`
   for a stale wc; `jj converge` for divergent commits. Do not run
   `jj op abandon`/`jj undo` across rounds — the op log is the audit trail and
   undo semantics can rebase commits created by other operations (F4).

---

## 5. Open uncertainties

1. **Mechanism of the file loss in E2 is not fully traced.** The observation is
   solid (`removed 4 files`, `rc.1`/`rc.4` missing, `out.*` auto-tracked), but
   the exact interleaving that chooses the victims was not reproduced
   deterministically. A deterministic repro would need an injection point inside
   `snapshot_working_copy` or an LD_PRELOAD delay around `check_out`; both were
   out of scope.
2. **Distributed filesystems.** rsync/NFS/Dropbox behaviour (docs § "Syncing with
   rsync, NFS, Dropbox") was read, not tested. The docs themselves warn that the
   Git backend "is not entirely lock-free" and that corruption is possible
   (issue #2193, recovery `jj debug reindex`), and that colocated repos are
   "less resilient to concurrency" — none of this was exercised.
3. **`jj op integrate` under concurrency.** E21 ran it single-process. Whether two
   processes integrating different unpublished ops (or the same op) race safely
   was not tested.
4. **`--at-op=@` documentation drift.** `cli/tests/test_concurrent_operations.rs:33`
   says it "prints head operation ids", but in 0.45.1 it exits 1 with
   `The "@" expression resolved to more than one operation` and prints the ids in
   the hint. The behaviour is consistent between test and binary; only the
   comment is stale. Treat the error+hint as the detection recipe.
5. **Concurrent read-only `jj log` (without `--ignore-working-copy`) against a
   mutating process** was not isolated. The 0.36.0 changelog claims that case is
   now safe in colocated repos; our concurrent runs involved mutating commands
   and still produced `Failed to update Git HEAD ref` warnings. Whether a
   read-only `jj log` alone can still trigger FM8 on 0.45.1 is untested.
6. **Helper-vs-helper on one lane** is covered by the flock by construction;
   a helper-vs-foreign-jj race is not, and no credential/ownership boundary
   enforces it. That is a policy gap, not a jj gap.
7. **Bookmark-pointer loss across machines** is warned about in the docs ("might
   conceivably lose some bookmark pointers") but was not reproduced; our merges
   produced conflicts, never silent loss.
8. **0.46.0 changes `jj workspace add` colocation.** 0.46.0 can create child
   workspaces as Git worktrees (`jj workspace add --[no-]colocate`, `git.colocate`),
   which 0.45.1 did not do. Our P2 experiments used 0.45.1 plain workspaces; the
   per-workspace `working_copy.lock` should carry over, but the extra Git worktree
   layer (shared `.git`, its own index/HEAD) is untested here. Re-check P2 if the
   fleet ever upgrades past 0.45.x.

---

## 6. Artifacts kept

Sandboxes are removed except the two that preserve cited failures, as required:

* `/fast/scratch/jj-wave/JjDocConcurrency/e14` (+ `e14-remote.git`) — unguarded
  4-agent run: `main`/`origin` at `3bcfc13` (`a4`), `a1`/`a2`/`a3` orphaned
  (`jj log -r 'all() ~ ::main'`), two rejected pushes.
* `/fast/scratch/jj-wave/JjDocConcurrency/e7` (+ `e7-remote.git`, and `e7-w2`,
  its second workspace) — conflicted bookmark `main` with three targets;
  `jj git push` refusal; Git side exporting only `298e31d`.

All other experiment directories (`e1`, `e2`, `e5`, `e6`, `e12`, `e15`, `e17`,
`e18`, `e19`, `e20`, `e21`) and the `v0.45.1` source clone were deleted.
