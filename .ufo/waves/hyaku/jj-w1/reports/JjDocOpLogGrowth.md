# JjDocOpLogGrowth — op-log & storage growth, `jj op abandon`, `jj util gc`, maintenance (jj 0.45.1)

**Verdict.** The operation log grows **linearly and forever at ≈21 KiB of allocated disk per
operation** — four ~250-byte files per op (op, view, index segment, index op-link), all block-rounded
— and **nothing prunes it automatically**.
`jj op abandon` + `jj util gc --expire=now` + `jj debug reindex` reclaims essentially all of it
(measured: 85,048 KiB → 588 KiB at 4,001 ops) in ~0.5 s. Ordinary command latency is **flat** out to
4,000 ops, so the reason to maintain is disk and ref count, not speed. `jj util gc` with its
default 2-week threshold reclaims **nothing** in an active campaign.

- Toolchain: `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, `git 2.56.0`, xfs 4 KiB blocks.
- Docs: version-exact pages at `https://docs.jj-vcs.dev/v0.45.1/…` (the `latest` alias currently
  points at **v0.46.0**: `https://docs.jj-vcs.dev/versions.json` lists
  `{"version":"v0.46.0","aliases":["latest"]}`). `https://jj-vcs.github.io/jj/latest/…` answers
  301 → `https://docs.jj-vcs.dev/latest/…`; `https://jj-vcs.github.io/jj/v0.45/` is a 404, and
  `docs.jj-vcs.dev/v0.45/` is a 404 — the usable pinned prefix is **`/v0.45.1/`**.
- Source: `https://github.com/jj-vcs/jj/tree/v0.45.1` (line numbers below are from that tag; the
  working tree is `/tmp/jjsrc/jj-0.45.1`).
- All probes ran in `/fast/scratch/jj-wave/JjDocOpLogGrowth/`. Every repo is a fresh
  `git init` + `jj git init --colocate`. Every `origin` is a sandbox bare repo; `git remote -v`
  confirmed it before any push. No live repo was read for anything except the read-only
  `scripts/hyaku/jj-lane.sh`, and no `jj` command was ever run against one.
- No tool was installed or upgraded for this ticket (jj, git, coreutils were already present).
- In the transcripts, `…` marks output trimmed only where stated; no command output was otherwise
  edited.

---

## F1 — What grows, and how fast

**Citation (mechanism).** <https://docs.jj-vcs.dev/v0.45.1/operation-log/>:
> Jujutsu records each operation that modifies the repo in the "operation log".

> Each operation object contains a snapshot of how the repo looked at the end of the operation.

The snapshot is a separate "view" object, so each mutating operation writes an op object **and** a
view object — measured exactly 1:1 at every checkpoint (`op_files == view_files`). Measured growth
(one `jj new -m` per op, `du -sk .jj` at checkpoints):

```console
$ ./grow.sh
n=0    op_files=1    view_files=1    jj_KiB=92
n=500  op_files=501  view_files=501  jj_KiB=10624
n=1000 op_files=1001 view_files=1001 jj_KiB=21268
n=2000 op_files=2001 view_files=2001 jj_KiB=42508
n=3000 op_files=3001 view_files=3001 jj_KiB=63852
n=4000 op_files=4001 view_files=4001 jj_KiB=85048
```

Marginal cost is **21.2 KiB per operation**, dead linear (21.06 / 21.29 / 21.24 / 21.34 / 21.20 KiB
per 500/500/1000/1000/1000 ops). The *payload* is tiny; the cost is allocation granularity:

```console
$ du -sh --apparent-size .jj/repo/op_store .jj/repo/store .jj/repo/index
1.5M    .jj/repo/op_store
1.9M    .jj/repo/store
2.7M    .jj/repo/index
$ ls -l .jj/repo/op_store/operations | head -3     # op files
-rw------- 1 vgpnk vgpnk 269 … fd39c6da…
-rw------- 1 vgpnk vgpnk 266 … 169230b7…
$ stat -c '%n blocks=%b size=%s' .jj/repo/op_store/operations/000a96…
….jj/repo/op_store/operations/000a96… blocks=8 size=269
```

8 blocks = 4 KiB allocated for 269 bytes: **≈384 bytes of real data per op, 8 KiB of disk**.
The four files per operation (model derived from the measurements below):

| location | files per op | allocated |
|---|---|---|
| `.jj/repo/op_store/operations/` | 1 | 4 KiB |
| `.jj/repo/op_store/views/` | 1 | 4 KiB |
| `.jj/repo/index/segments/` | 1 | 4 KiB |
| `.jj/repo/index/op_links/` | 1 | 4 KiB |
| `.jj/repo/store/extra/` | 1 per **commit** | 4 KiB |

`store/extra` holds jj's change-id metadata, one file per commit:

```console
$ # after 500 ops
$ find .jj/repo/store/extra -type f | wc -l
503
$ du -sk .jj/repo/store
2140
```

Projection per lane repo: **5,000 ops ≈ 104 MiB, 20,000 ops ≈ 414 MiB**. Measured 4,001 ops =
85,048 KiB (83 MiB).

---

## F2 — `jj op abandon`: what it does, and what it refuses

**Citation (`jj util gc --help`, 0.45.1; identical text at
<https://docs.jj-vcs.dev/v0.45.1/cli-reference/#jj-util-gc>):**
> To garbage-collect old operations and the commits/objects referenced by them, run `jj op abandon
> ..<some old operation>` before `jj util gc`.

**Citation (`jj op abandon --help`; identical at
<https://docs.jj-vcs.dev/v0.45.1/cli-reference/#jj-operation-abandon>):**
> To discard old operation history, use `jj op abandon ..<operation ID>`. It will abandon the
> specified operation and all its ancestors. The descendants will be reparented onto the root
> operation.

Confirmed on 4,005 ops, and it is cheap:

```console
$ jj op abandon '..@-'
Abandoned 4005 operations and reparented 1 descendant operations.
abandon_ms=15
$ jj op log --no-graph
ca4f9ec67a81 … now, lasted 1 millisecond
│  new empty commit
000000000000 root()
```

Note what it does **not** do: it is a *metadata* operation. Every commit stays visible — right after
the abandon, `jj log -r 'all()' --no-graph -T 'commit_id.short() ++ "\n"' | wc -l` returned
**4012**, i.e. the whole 4,012-commit chain was still reachable — and bookmarks were untouched. Only
the operation/view objects become garbage.

Partial ranges work as documented; keeping the newest 20 ops:

```console
$ jj op abandon '..6646eb38e507'
Abandoned 285 operations and reparented 21 descendant operations.
```

Error paths (all verbatim):

```console
$ jj op abandon @
Error: Cannot abandon the current operation 3dbdf423e6d4
Hint: Run `jj undo` to revert the current operation, then use `jj op abandon`
```

---

## F3 — `jj util gc`: the 2-week default makes it a no-op in an active campaign

**Citation (`jj util gc --help`, 0.45.1):**
> By default, only obsolete objects and operations older than 2 weeks are pruned.

> Only the string "now" can be passed to this parameter.

Source agrees exactly — `cli/src/commands/util/gc.rs:54-65`
(<https://github.com/jj-vcs/jj/blob/v0.45.1/cli/src/commands/util/gc.rs#L54-L65>):

```rust
let keep_newer = match args.expire.as_deref() {
    None => SystemTime::now() - Duration::from_secs(14 * 86400),
    Some("now") => SystemTime::now() - Duration::ZERO,
    _ => return Err(user_error("--expire only accepts 'now'")),
};
…
repo.op_store().gc(slice::from_ref(repo.op_id()), keep_newer).await?;
repo.store().gc(repo.index(), keep_newer)?;
```

Pruning is **mtime-based**, not operation-time-based (`lib/src/simple_op_store.rs:286-295`,
<https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/simple_op_store.rs#L277-L355>) — and it is
**relative to the current head op**, so an op reachable from `@` is never pruned no matter how old
it is.

Measured consequences:

```console
$ # 4,001 ops, default gc
$ jj util gc ; echo exit=$?
gc_default_ms=353
n_ops_after_gc_default=4007          # unchanged (4001 + probes)
du -sk .jj
85408                                 # grew, did not shrink

$ jj util gc --expire=now
gc_now_ms=275
n_ops_after_gc_now=1
n_views_after_gc_now=1
du -sk .jj
34844                                 # only the index is left

$ # without abandon, --expire=now cannot prune reachable ops:
$ jj util gc --expire=now ; find .jj/repo/op_store/operations -type f | wc -l
101                                   # was 101 before; ops are reachable from @
```

So the pairing is mandatory and ordered: **abandon first, then gc**. `--expire=now` is the only
value that reclaims anything within a campaign.

Invalid/unsupported invocations:

```console
$ jj util gc --expire=1d
Error: --expire only accepts 'now'
$ jj util gc --at-op=44932e1c2b01
Error: Cannot garbage collect from a non-head operation
```

There is **no automatic GC and no configuration knob**: `jj config list --include-defaults | grep -i
gc` prints nothing, and `gc.rs` is only reachable from `jj util gc`.

`jj util gc` also runs `git gc` on the backing repo
(`lib/src/git_backend.rs:970-989`: `git --git-dir=. gc --prune=@<unix> +0000`) and packs refs.

---

## F4 — Performance impact of a long op log: none measurable on normal commands

Minimum of 5 runs each, 4,001 ops in the repo (before/after full maintenance):

```console
$ ./timegc.sh
=== BEFORE gc: n_ops=4001 ===
st min_ms=6            log_all min_ms=5        op_log_no_graph min_ms=25
op_log_default min_ms=26                        new_empty min_ms=10
=== AFTER abandon + gc --expire=now ===
st min_ms=6            log_all min_ms=5        op_log_no_graph min_ms=5
new_empty min_ms=10
```

Only the command that actually walks the whole op log (`jj op log`) paid anything: 25 ms at 4k
ops vs 5 ms at 2 ops — 5 ms of extra work per 4,000 operations ≈ **1.2 µs per historical op**.
`jj st`, `jj log -r all()` and `jj new` did not move. Measured upkeep cost at the same size:
abandon 15 ms + gc 275 ms = 290 ms; adding `jj debug reindex` 230 ms → **~0.5 s total**.

This falsifies the hypothesis that a long op log degrades ordinary lane work. The real costs are
disk (F1) and the ref count (F6).

---

## F5 — `jj util gc` does **not** compact the index; `jj debug reindex` does

After abandon+gc the repo was still 34,844 KiB, almost all index:

```console
$ du -sk .jj/repo/*
34600   .jj/repo/index
76      .jj/repo/op_store
236     .jj/repo/store
$ find .jj/repo/index/segments -type f | wc -l ; find .jj/repo/index/op_links -type f | wc -l
4013
4013
```

The default index writes **one segment file and one op-link file per operation**
(`lib/src/default_index/store.rs:230-256`
<https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/default_index/store.rs#L230-L256>:
`tracing::info!("scanning operations to index")` — it iterates *operations*, not commits).
`jj debug reindex` collapses them:

```console
$ jj debug reindex
Finished indexing 4012 commits.
reindex_ms=230
$ find .jj/repo/index/segments -type f | wc -l ; find .jj/repo/index/op_links -type f | wc -l
1
1
$ du -sk .jj/repo/index ; du -sk .jj
244
588
```

**85,048 KiB → 588 KiB** end to end. Reindex also rebuilds the *content* of the index from the surviving
operations, so commits that only appeared in abandoned operations' views drop out. Measured in a
6-op repo with 3 `jj describe` rewrites of one commit:

```console
$ jj log -r 'all()' --no-graph -T 'commit_id ++ "\n"' | sort -u | wc -l
3
$ jj debug reindex
Finished indexing 11 commits.
$ jj op abandon '..@-'
Abandoned 6 operations and reparented 1 descendant operations.
$ jj debug reindex
Finished indexing 5 commits.
```

So the **pairing** matters: `op abandon` removes the views that referenced the old versions, and
reindex is what rebuilds the index without them (and collapses the segment/op-link files). Reindex
alone, without abandon, keeps every commit any operation still references.

Caveat: `jj debug reindex` is in the `debug` namespace and is not a stability-guaranteed interface
(`jj debug reindex --help`: "Rebuild commit index").

---

## F6 — Every commit adds a `refs/jj/keep/*` ref; only `--expire=now` prunes them

`write_commit()` (starts at `lib/src/git_backend.rs:1320`; the ref edit is line 1466,
<https://github.com/jj-vcs/jj/blob/v0.45.1/lib/src/git_backend.rs#L1466>) adds a no-GC ref for every
commit jj writes, and `recreate_no_gc_refs()` (line 902) deletes the stale ones **only if their
loose-ref mtime is older than `keep_newer`** (lines 939-946). Hence:

```console
$ # 2,000 commits
$ git for-each-ref refs/jj/keep --format='%(refname)' | wc -l
2001
$ jj util gc                     # default 2 weeks
keep_refs_after_default_gc=2006  # nothing pruned
$ jj util gc --expire=now
keep_refs_after_now_gc=1
```

This is exactly the mechanism the docs point at for colocated repos
(<https://docs.jj-vcs.dev/v0.45.1/git-compatibility/>):

> In colocated workspaces with a very large number of branches or other refs, jj commands can get
> noticeably slower because of the automatic jj git import executed on each command. This can be
> mitigated by occasionally running jj util gc to speed up the import (that command includes
> packing the Git refs).

**Measured caveat:** I could not reproduce the slowdown at campaign scale. At 2,000 refs,
`jj st --ignore-working-copy` was 5 ms both before and after pruning, and `jj new` was 9 ms. So the
doc's "very large number" is above 2k refs; the import cost is theoretical at shokunin scale.

---

## F7 — Safety for the lane invariants (pushed hash survives; evolog does not)

Scenario: colocated repo, commit `H1`, bookmark `main`, push to a sandbox bare `origin`, then 100
more ops, `jj op abandon '..@-'`, `jj util gc --expire=now`, `jj debug reindex`.

```console
$ git -C ../origin2.git for-each-ref
refs/heads/main ff3a26e
$ # after abandon + gc + reindex
$ git cat-file -e $H1 && echo local_git_has_H1=yes
local_git_has_H1=yes
$ jj log -r $H1 --no-graph -T 'commit_id.short() ++ " " ++ description.first_line()'
ff3a26ee7bf6 first
$ git -C ../origin2.git cat-file -e $H1 && echo origin_has_H1=yes
origin_has_H1=yes
```

A pushed commit survives because it is reachable from `refs/heads/<branch>` and
`refs/remotes/origin/<branch>` (both observed after the sweep:
`refs/heads/main ff3a26e`, `refs/remotes/origin/main ff3a26e`). A bookmarked side commit that is not
an ancestor of `@` also survived `jj util gc --expire=now` (`side_resolves=d5829a09c92a`).

What **is** lost is evolution history. Changelog 0.32.0
(<https://github.com/jj-vcs/jj/blob/v0.45.1/CHANGELOG.md>, section `[0.32.0] - 2025-08-06`):
> `jj op abandon` now discards previous versions of a change (or predecessors) if they become
> unreachable from the operation history.

Measured — same change, 6 evolog entries before, 1 after:

```console
$ jj evolog -r $CUR --no-graph -T 'commit.commit_id() ++ "\n"' | wc -l
6
$ jj op abandon '..@-' ; jj util gc --expire=now
Abandoned 56 operations and reparented 1 descendant operations.
$ jj evolog -r $CUR --no-graph -T 'commit.commit_id() ++ "\n"' | wc -l
1
```

`jj undo` still worked after the sweep (`Undid operation: … new empty commit`), but only for
operations created after it — the pre-abandon undo stack is gone by construction.

---

## Consequence for the planned shokunin integration

1. **The helper's per-round op cost is small, but it is permanent.** Measured with the
   helper-style sequence in a fresh colocated repo: `init` 1 op; three `jj config set` +1;
   `jj file track` +2; `jj commit -m --path` +1; `jj git push -b` +2; read-only `jj st`/`jj log`
   with `--ignore-working-copy` **+0**. A steady-state commit cycle is **~3–5 ops**, so 100 rounds
   ≈ 300–500 ops ≈ 6–10 MiB per lane repo. "Thousands of ops per repo" requires ~2,000+ cycles, but
   the growth is unbounded and never reclaimed without intervention.
2. **`jj evolog` is not an audit trail** once maintenance runs (F7). Shokunin's durable record must
   stay `LOG.md` + the pushed commit graph, which the design already assumes.
3. **The landed-hash invariant is safe under gc** *because* the invariant is "pushed": the commit
   is reachable from `refs/heads/<branch>` and the remote-tracking ref (F7). It would **not** be
   safe for a hash that was cited before a successful push — e.g. the commit the helper's
   reject-retry rebases away. The helper already prints only the pushed hash; keep that.
4. **Fleet-root commits are unaffected** (`scripts/hyaku/fleet-commit.sh` stays git-only); none of
   this maintenance applies there.
5. **`jj util gc` runs `git gc`** inside `.git` (packs refs, repacks objects, takes the git lock).
   In a colocated lane this mutates the same `.git` the fleet's git tooling reads, so it must run
   between rounds, never mid-round.

### Recommended maintenance (between rounds, under the lane flock)

```sh
# Same lock the helper's init/commit/push take: $STATE/jj-<basename>.lock
# (scripts/hyaku/jj-lane.sh:84-89, STATE=$HYAKU_STATE)
flock "$HYAKU_STATE/jj-$(basename "$lane").lock" sh -c '
  jj -R "$lane" op abandon "..@-"        # or "..<op older than N>"; ~15 ms
  jj -R "$lane" util gc --expire=now     # ~275 ms at 4k ops
  jj -R "$lane" debug reindex            # ~230 ms; collapses index to 1 segment
'
```

- Trigger it when `find "$lane/.jj/repo/op_store/operations" -type f | wc -l` exceeds ~4,000, or
  when `.jj` exceeds ~100 MiB — not every round. At ≤500 ops the whole sweep is tens of ms, so
  "once per campaign" is also defensible if the campaign is short.
- If op-level undo across rounds has any value, use a bounded range
  (`jj op abandon "..<op>"`, keeping the last N) instead of `..@-`; the reclaim is proportional.
- Do **not** use plain `jj util gc`: it is a measured no-op for anything younger than 2 weeks
  (F3) and leaves every `refs/jj/keep/*` ref in place (F6).
- Treat `jj debug reindex` as optional/experimental (debug namespace). Everything else works
  without it; it only buys the index compaction.

---

## Open uncertainties

1. **Concurrent maintenance.** I did not test `jj op abandon`/`jj util gc` racing a second jj
   process in the same repo (divergent op heads, lock contention, whether gc's "non-head operation"
   guard trips). The helper's flock covers commits; the maintenance command must take the same
   lock. Deferred to the concurrency seat.
2. **Ref-import slowdown threshold.** 2,000 refs showed no measurable cost; the documented
   "very large number" is unquantified. If a lane ever accumulates tens of thousands of keep refs,
   re-measure before trusting the flatness result.
3. **`--expire=now` safety on other object kinds.** I verified commits and bookmarks; I did not
   test tags, submodule gitlinks, or `store/extra` entries for commits referenced only by a
   `--at-op` inspection. `jj util gc` refuses non-head operations, which limits the blast radius.
4. **`jj debug reindex` guarantees.** It is documented only as "Rebuild commit index". After
   `op abandon` I observed the indexed commit count fall (11 → 5 in a 6-op repo), but I did not
   test it on a repo with divergent change IDs or a legacy index layout.
5. **Filesystem dependence of the 21 KiB/op figure.** xfs 4 KiB blocks; the figure is block-rounded
   (`stat` showed 8 blocks for a 269-byte file). Compression (btrfs zstd) or larger block sizes
   will change the constant, not the linearity. Not tested.
6. **Repeated full sweeps.** I ran one sweep per repo. I did not measure whether running
   abandon+gc+reindex every round has any accumulating side effect (e.g. extra metadata table
   churn) beyond the measured cost.
