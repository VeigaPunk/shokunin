# JjAuditTabi — static, read-only audit of git invocations in lane `tabi`

Seat: `JjAuditTabi-2`. Target: `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`
(`git rev-parse --abbrev-ref HEAD` → `master`; no `.jj` present at audit time; `.ufo/waves/round-16/`
untracked). Mission: classify every git invocation in the lane's executable tooling, judge it under
jj colocation (detached HEAD, jj-owned index), and find the lane's top three risks. Nothing in the
live repo was written, staged, fetched, checked out or committed; the only live-repo commands were
`git log/show/ls-files/rev-parse/status/diff/config/cat-file/check-attr`, `ls`, `find`, `grep`,
`cat`, plus `git clone` out to a sandbox.

## Scope inventory (observed)

```
$ find . -maxdepth 1 -type f \( -name '*.sh' -o -name '*.py' -o -name '*.mjs' -o -name '*.js' -o -name Makefile \) -print
(no output)
$ find . -maxdepth 1 -type d -print
./corpus ./plans ./reports ./scripts ./.git ./.ufo
$ git ls-tree -r --name-only HEAD | grep -E '^(tools|verifiers)/'
(no output)
```

`tools/` and `verifiers/` do not exist in this lane, on disk or in `HEAD`; there are no root-level
`*.sh|*.py|*.mjs|*.js|Makefile`. Executable, in-scope tooling is therefore the ten `.mjs` files in
`scripts/` plus the gates named in `SKILL.md`. Git appears in exactly three of them:

```
$ for f in scripts/*.mjs; do printf '%s ' "$f"; grep -cE "spawnSync\('git'|'git'" "$f"; done
aria-loopback-round13.mjs 0   check-aria-metadata.mjs 0   check-freshness.mjs 10
check-round-contract.mjs 15   check-sources.mjs 0          check-user-round-contract.mjs 15
pstack-aggregate.mjs 0        pstack-seat.mjs 0            user-aggregate.mjs 0
user-seat.mjs 0
```

`SKILL.md`-named gates verified for git: `check-freshness.mjs`, `check-round-contract.mjs`,
`check-user-round-contract.mjs` (the three audited), `check-sources.mjs` 0 hits,
`check-aria-metadata.mjs` 0 hits, `.ufo/waves/round-12/measure.mjs` 0 hits,
`.ufo/waves/round-12/w1/mistake/check-claim-record.mjs` 0 hits. Two of those live under
`.ufo/waves`; they are listed only to close the SKILL registry — they invoke no git.

---

## Findings (observed facts)

### F1 — After a plain `jj new`, git HEAD detaches onto an empty local commit that is on no branch; both gates still certify it

Sandbox clone `$SB/tabi2` (colocated, `snapshot.auto-track="none()"`), no working-copy edits:

```
$ jj new
$ git rev-parse --short HEAD; git rev-parse --short master
68d0582
e38d259
$ git branch -a --contains HEAD
* (no branch)
$ git merge-base --is-ancestor HEAD master; echo rc=$?
rc=1
$ git rev-parse --short refs/remotes/origin/master
e38d259
$ node scripts/check-round-contract.mjs | tail -1
ROUND_CONTRACT verdict=clean rounds=10 consequential=0
$ node scripts/check-freshness.mjs --witness HEAD | tail -1
FRESHNESS_GATE verdict=clean finding=freshness_witness matched=34 unique=34 lane=31 public=3 revision=HEAD baseline=c24eaea14dfc0c4a3848742d31673db5675f9183 profile=production
```

`ROUND_CONTRACT` and `FRESHNESS_GATE` both return clean while the revision they resolved as HEAD
(`68d0582`) is not on `master` and not on `origin/master`. `check-freshness` records the literal
string `revision=HEAD` rather than the resolved 40-hex id.

### F2 — After `jj commit`, HEAD detaches at the new local commit; `master` stays at the old tip, `@{u}` dies, and a clean `git status` does not reveal the divergence

Sandbox clone `$SB/tabi`, after `jj file track` + `jj commit -m probe -- sandbox-probe.txt`:

```
$ git rev-parse --abbrev-ref HEAD; git rev-parse --short HEAD; git rev-parse --short master
HEAD
4372d82
e38d259
$ git rev-parse --abbrev-ref '@{u}'
fatal: HEAD does not point to a branch
$ git status --porcelain=v1 | head -5
(no output)
$ node scripts/check-freshness.mjs --worktree | tail -1
FRESHNESS_GATE verdict=clean finding=freshness_worktree matched=34 unique=34 lane=31 public=3 revision=worktree baseline=c24eaea14dfc0c4a3848742d31673db5675f9183 profile=production
$ node scripts/check-round-contract.mjs | tail -1
ROUND_CONTRACT verdict=clean rounds=10 consequential=0
```

Both gates pass on `4372d82`, a commit the bookmark does not name (the helper closes this window with
its own `bookmark set` immediately after `jj commit`; a bare `jj commit`, as in this sandbox, leaves
it indefinitely). A porcelain-clean `git status` is therefore
compatible with `HEAD != master != origin/master`. Note: `:215` of the brief's expectation ("HEAD
stays attached right after init") is confirmed — `jj git init --colocate` left
`git rev-parse --abbrev-ref HEAD` → `master`; detachment begins at the first `jj commit`/`jj new`.

### F3 — HEAD can carry never-committed working-copy content; the gates read it, and the witness `committed` flag can be a false positive

Sandbox clone `$SB/tabi`, edit of a **tracked** file with no commit to `master`:

```
$ printf '\nprobe-edit\n' >> SHONEN.md
$ git status --porcelain=v1
 M SHONEN.md
$ jj st                 # snapshot absorbs the edit into @
$ jj new                # HEAD now names that snapshot commit
$ git rev-parse --short HEAD; git rev-parse --short master
3aa39dc
e38d259
$ git hash-object SHONEN.md; git rev-parse HEAD:SHONEN.md; git rev-parse master:SHONEN.md
5b58313999cb54214c77964841c61483f7859f50
5b58313999cb54214c77964841c61483f7859f50
9dcb2687d3083f696b57032389eed7349e03893e
$ node scripts/check-round-contract.mjs | tail -1
ROUND_CONTRACT verdict=failed finding=shonen_policy detail=SHONEN.md has non-canonical prose after the four boxes:
```

The gate parsed unlanded working-copy bytes as committed lane state (it failed on them here; with
benign edits the same path yields clean). This is also the exact comparison the witness modes use
for `committed`:

`scripts/check-user-round-contract.mjs:793-795`
```js
const worktreeBlob = gitBlobSha1(scriptBytes);
const headBlob = blob(defaultRoot, 'HEAD', USER_SCRIPT);
const committed = headBlob !== null && headBlob === worktreeBlob;
```
Same pattern at `:877-879` and `:952-954`; `scripts/check-round-contract.mjs:990,996,1000,1004`
reads HEAD before/after and asserts `headStable`. Under jj, `worktreeBlob === HEAD:blob` while `master:blob` differs — so
`committed=yes` can be printed for checker bytes that are on no branch and were never pushed.
[INFERENCE] In receipt form this is a false "committed" attestation; I did not run the full witness
mode, because that mode pins the live gate bytes and its outputs only after a real witness run.

### F4 — No git hooks, no attributes filters, no eol rules; jj bypasses nothing that exists

```
$ find .git/hooks -maxdepth 1 -type f ! -name '*.sample' -print
(no output)
$ git config --get core.hooksPath; echo rc=$?
rc=1
$ git config --global --get core.hooksPath; echo rc=$?
rc=1
$ ls .gitattributes; git ls-files | grep -E '\.gitattributes$|\.git/info'
(absent / no output)
$ cat .git/info/attributes
NONE
$ git config --global --get-regexp '^filter\.'
filter.lfs.clean git-lfs clean -- %f
filter.lfs.smudge git-lfs smudge -- %f
filter.lfs.process git-lfs filter-process
filter.lfs.required true
$ git check-attr --all -- scripts/check-sources.mjs SKILL.md
(no output)
$ git config --get core.autocrlf; git config --get core.eol
(unset / unset)
```

Only `*.sample` hooks exist; `core.hooksPath` is unset in repo and global config; there is no
`.gitattributes`, no `.git/info/attributes`, no tracked attributes file; the global LFS filter
definitions have no attribute assignment, so they are inert; no autocrlf/eol conversion. Therefore
jj's "no hooks, no attributes" behavior currently skips no gate that git would have run in this
lane. It also means a future hook added to this repo would be silently skipped by `jj-lane.sh
commit` — the helper runs no hook and does not run `git commit`.

### F5 (adjacent, fleet helper — not lane tooling) — `jj-lane.sh state` is not read-only: `git status --porcelain` rewrites `.git/index`

`scripts/hyaku/jj-lane.sh:67` (`print_state`) claims "Pure-git, read-only state line (safe for
`state`; no jj calls at all)" but calls `git status --porcelain` at `:78`:

```
$ stat -c '%y %s' .git/index            # 2026-10-20 11:15:55.918847054 -0300 375096
$ git status --porcelain >/dev/null
$ stat -c '%y %s' .git/index            # 2026-10-20 11:16:14.605739129 -0300 375096
$ GIT_OPTIONAL_LOCKS=0 git status --porcelain >/dev/null
$ stat -c '%y' .git/index               # unchanged 11:16:14.605739129
```

The index mtime moves on the plain call and not under `GIT_OPTIONAL_LOCKS=0`. `state` therefore
takes `.git/index.lock` inside a repo where jj also writes the index. It is safe with respect to
*data* (git only refreshes stat info) but the read-only claim is false, and the helper's flock does
not serialize jj calls made by other seats. Also class A in the helper: `detect_branch` uses
`git symbolic-ref -q --short HEAD` (`:55`) with fallbacks to `origin/HEAD` → `master`/`main` →
first local branch, and `print_state` uses `git symbolic-ref -q HEAD` (`:77`) to report
`head=attached|detached`; both are correct precisely *because* they handle jj's detached HEAD.

### F6 — `check-freshness --witness` accepts a non-hex revision (`HEAD`); the sibling gates do not

`scripts/check-freshness.mjs:51` accepts `--witness <anything>` (only a leading `--` is refused);
`scripts/check-round-contract.mjs:211` and `scripts/check-user-round-contract.mjs:291,295` require
`/^[a-f0-9]{7,40}$/`. The run in F1 (`--witness HEAD`) succeeded and printed `revision=HEAD`. No
option injection is possible (`git` is spawned with an argv array, and values starting with `--` are
rejected), but a freshness receipt can name an unpushed jj snapshot by symbolic name and cannot be
replayed from a clone.

---

## Classified git call sites

Class definitions as assigned: **A** attached-HEAD/upstream assumption; **B** history/index/worktree
mutation; **C** index/staging read; **D** read-only, commit-addressed. "Risk" is the risk under jj
colocation with detached HEAD and jj-owned index. `$FIX` = a fresh `/var/tmp/tabi-*` or
`/tmp/tabi-freshness-*` tmpdir initialized by the gate itself with plain `git init` (no `.jj`).

Risk codes: **R1** HEAD is jj-owned (detached after `jj commit`, may name an empty/local-only
commit after `jj new`, may contain unlanded `@-` snapshot content); **R2** the hash is printed into a
receipt as a live diagnostic and may be unpushed/non-reproducible; **F** fixture-only, plain git;
**—** explicit revision or otherwise unaffected.

### scripts/check-freshness.mjs

| site | command (argv) | cls | risk | jj-safe replacement |
|---|---|---|---|---|
| 65 | `git show -s --format=%ct <witness>` | D | — | unchanged (rev-pinned) |
| 68 | `git merge-base --is-ancestor <baseline> <witness>` | D | — | unchanged |
| 71 | `git show <witness>:<path>` (witness mode; worktree mode reads bytes directly) | D | — | unchanged |
| 78 | `git ls-tree -r --name-only <baseline> -- corpus/knowledge reports SKILL.md` | D | — | unchanged |
| 88 | `git show <baseline>:<SKILL.md\|SCORECARD.md\|LOG.md>` | D | — | unchanged |
| 94 | `git show <baseline>:<target>` | D | — | unchanged |
| 126 | `git -c user.name=… -c user.email=… commit -qm <subject>` | B | F | unchanged; keep plain git and assert fixture root has no `.jj` |
| 131 | `git rev-parse HEAD` | D | F | unchanged (fixture tip) |
| 133 | `git init -q` | B | F | unchanged |
| 140 | `git add -- SKILL.md corpus reports SCORECARD.md` | B | F | unchanged |
| 163 | `git add -- SKILL.md pins.tsv` | B | F | unchanged |

### scripts/check-round-contract.mjs

| site | command (argv) | cls | risk | jj-safe replacement |
|---|---|---|---|---|
| 71 | `git rev-parse --verify <rev>:<path>` | D | — | unchanged |
| 77 | `git show <rev>:<path>` | D | — | unchanged |
| 89 | `git ls-tree -r --name-only <rev> -- <prefix>` | D | — | unchanged |
| 119 | `git --literal-pathspecs ls-tree HEAD -- <path>` | D | **R1** | resolve once `rev-parse --verify refs/heads/master^{commit}`, pass that rev |
| 231 | `git rev-parse HEAD` | D | **R1** | resolve `refs/heads/master` (or `origin/master` for landed claims) |
| 232 | `git merge-base --is-ancestor <baseline> <head>` | D | **R1** | use the resolved branch rev, not HEAD |
| 415 | `git ls-tree -r --name-only <rev>` (SCORECARD count) | D | — | unchanged (rev comes from the scorecard) |
| 433 | `git grep -h -e <pattern> <rev> -- <paths>` | D | — | unchanged |
| 504 | `git merge-base --is-ancestor <measured> HEAD` | D | **R1** | `… <measured> refs/heads/master` |
| 612 | `git -c user.name=… -c user.email=… commit -qm <subject>` | B | F | unchanged |
| 614 | `git rev-parse HEAD` | D | F | unchanged |
| 622 | `git init -q` | B | F | unchanged |
| 629 | `git add -- .` | B | F | unchanged |
| 675 | `git add -- .` | B | F | unchanged |
| 693 | `git add -- .` | B | F | unchanged |
| 831 | `git add -- .` | B | F | unchanged |
| 884 | `git add -- .` | B | F | unchanged |
| 947 | `git add -- .` | B | F | unchanged |
| 988 | `git add -- .` | B | F | unchanged |
| 990 | `git rev-parse HEAD` (fixture pre-head) | D | F | unchanged |
| 996 | `git rev-parse HEAD` (fixture old gate) | D | F | unchanged |
| 1000 | `git rev-parse HEAD` (fixture new gate) | D | F | unchanged |
| 1007 | `git rev-parse HEAD` (live `code_revision=` receipt field) | D | **R2** | print the resolved `refs/heads/master`/`origin/master` hash |

### scripts/check-user-round-contract.mjs

| site | command (argv) | cls | risk | jj-safe replacement |
|---|---|---|---|---|
| 127 | `git rev-parse --verify <rev>:<path>` | D | — | unchanged |
| 133 | `git show <rev>:<path>` | D | — | unchanged |
| 139 | `git ls-tree -r --name-only <rev> -- <prefix>` | D | — | unchanged |
| 167 | `git --literal-pathspecs ls-tree HEAD -- <path>` | D | **R1** | resolve once from `refs/heads/master`, pass that rev |
| 237 | `git log --no-show-signature --format=%H <pstackPin>..HEAD -- scripts/check-round-contract.mjs` | D | **R1** | `<pstackPin>..refs/heads/master` |
| 255 | `git log --no-show-signature -m --no-renames --diff-filter=MDRT --format=%H <pstackPin>..HEAD -- <path>` | D | **R1** | `<pstackPin>..refs/heads/master` |
| 308 | `git rev-parse HEAD` | D | **R1** | resolve `refs/heads/master` / `origin/master` |
| 309 | `git merge-base --is-ancestor <baseline> <head>` | D | **R1** | use the resolved branch rev |
| 325 | `git merge-base --is-ancestor <pin> <head>` | D | **R1** | use the resolved branch rev |
| 327 | `git diff --no-renames --name-status <pin> <head> -- <PSTACK_PATHS>` | D | **R1** | `<pin> refs/heads/master` |
| 425 | `git ls-tree -r --name-only <target>` / `git --literal-pathspecs grep -h -e <pattern> <target> -- <path>` | D | — | unchanged (target is the scorecard's measured commit) |
| 529 | `git merge-base --is-ancestor <measured> HEAD` | D | **R1** | `… <measured> refs/heads/master` |
| 631 | `git -c user.name=… -c user.email=… commit -qm <subject>` | B | F | unchanged |
| 633 | `git rev-parse HEAD` | D | F | unchanged |
| 641 | `git init -q` | B | F | unchanged |
| 648 | `git add -- .` | B | F | unchanged |
| 702 | `git add -- .` | B | F | unchanged |
| 720 | `git add -- .` | B | F | unchanged |
| 789 | `git rev-parse --verify <rev>^{commit}` (live) | D | — | unchanged |
| 790 | `git rev-parse HEAD` → `codeRevision=` receipt | D | **R2** | resolved branch hash |
| 813 | `git add -- .` | B | F | unchanged |
| 865 | `git rev-parse --verify <rev>^{commit}` (live) | D | — | unchanged |
| 874 | `git rev-parse HEAD` → `codeRevision=` receipt | D | **R2** | resolved branch hash |
| 890 | `git add -- .` | B | F | unchanged |
| 944 | `git rev-parse --verify 5c7710d7…^{commit}` (live) | D | — | unchanged |
| 955 | `git rev-parse HEAD` → `codeRevision=` receipt | D | **R2** | resolved branch hash |
| 978 | `git add -- .` | B | F | unchanged |
| 993 | `git add -- .` | B | F | unchanged |
| 1114 | `git rev-list --max-parents=0 HEAD` | D | F | unchanged (fixture root commit) |
| 1159 | `git mv corpus/lessons/round-1.md corpus/lessons/round-13.md` | B | F | unchanged |
| 1214 | `git add -- .` | B | F | unchanged |
| 1219 | `git add -- .` | B | F | unchanged |

Transport wrappers (not counted as call sites): `check-freshness.mjs:39`,
`check-round-contract.mjs:60`, `check-user-round-contract.mjs:117` — each is
`spawnSync('git', argv, { cwd: root })`, argv arrays only, no shell, no `env` override.

### Input-driven shell git (executed by `pstack-seat.mjs` / `user-seat.mjs`)

`scripts/pstack-seat.mjs:34` and `scripts/user-seat.mjs:34` run `bash -c <slice.command>` with
`cwd = root`. Three reachable slices contain git (all class D, explicit revision):

| site | command | cls | risk | note |
|---|---|---|---|---|
| `corpus/evidence/pstack-20261015-r01/slices.json:115` | `git rev-parse HEAD:corpus/lessons/round-1.md && git rev-parse HEAD:.ufo/reports/…/tabi.md` | D | **R1** | resolves a tree entry from the live HEAD; detached-safe, but HEAD-name drift applies |
| `corpus/evidence/pstack-20261015-r02/slices.json:108` | `git rev-parse HEAD:corpus/lessons/round-{1..10}.md` | D | **R1** | same |
| `corpus/evidence/pstack-20261015-r04/slices.json:128` | `git rev-parse HEAD:corpus/lessons/round-1.md HEAD:corpus/lessons/round-10.md` | D | **R1** | same |

These are shell-executed (`bash -c`), so they are the only shell `git ` surface in the lane. They
are read-only and use `HEAD:<path>` (commit-addressed, not branch-addressed), so they work on a
detached HEAD; the only exposure is the same moving-HEAD risk as R1. `pstack-seat`/`user-seat` also
write `result.json` into `corpus/evidence/<round>/seats/<seat>/`; with `snapshot.auto-track="none()"`
those new paths stay untracked until the helper's `jj file track`, which is expected but means a lane
must pass the evidence paths explicitly to `jj-lane.sh commit`.

## Counts per class

| class | count | detail |
|---|---|---|
| A — attached HEAD / upstream | **0** | no `symbolic-ref`, `@{u}`, `--abbrev-ref HEAD`, `branch --show-current`, or HEAD-as-branch-name in lane tooling |
| B — mutates history/index/worktree | **25** | check-freshness 4 · check-round-contract 9 · check-user-round-contract 12; all inside `$FIX` tmpdirs; none reachable from `--repo` |
| C — reads index/staging | **0** | no `diff --cached`, `ls-files -s`, `update-index`; no working-tree `git diff` (the only diff is two-rev at `check-user-round-contract.mjs:327`) |
| D — read-only, commit-addressed | **41** | check-freshness 7 · check-round-contract 14 · check-user-round-contract 20; +3 input-driven slice commands |
| transport wrappers | 3 | `spawnSync('git', argv)` at freshness:39, round:60, user:117 |

Of the 41 D sites: 12 are live HEAD-anchored (R1), 4 are live `rev-parse HEAD` receipt fields (R2),
7 are fixture-only (F), 18 are explicit-revision (—).

## lane top three risks

1. **The two round-contract gates anchor on a jj-owned `HEAD`, so they can accept and certify an
   unlanded revision** (`check-freshness` adopts it only in `--witness` mode; its `--worktree` mode
   reads bytes directly). After `jj commit`, `HEAD` is the just-created local commit while `master`
   still points at the old tip and nothing has been pushed (F2); after `jj new`, `HEAD` is an empty
   commit on no branch (`git branch --contains HEAD` → `* (no branch)`) and `merge-base
   --is-ancestor HEAD master` fails, yet `check-round-contract` and `check-freshness --witness HEAD`
   both report clean (F1). Twelve in-repo call sites consume that pointer. The lane invariant
   "landed = committed AND pushed before a report cites the hash" is not checked anywhere; a clean
   gate receipt is compatible with `HEAD != master != origin/master`.
2. **`HEAD` can contain working-copy content that jj snapshotted but never landed, and the witness
   `committed` flag compares against exactly that HEAD blob.** F3 shows `git hash-object SHONEN.md
   == git rev-parse HEAD:SHONEN.md` (`5b58313`) while `master:SHONEN.md` differs (`9dcb268`), and
   `check-round-contract` failed on that unlanded edit. The same equality at
   `check-user-round-contract.mjs:793-795/877-879/952-954` can print `committed=yes` for checker
   bytes on no branch — a false attestation in a witness receipt.
3. **Receipt fields and witness selectors can name unpushed hashes.** Four live
   `git rev-parse HEAD` diagnostics (`check-round-contract.mjs:1007`,
   `check-user-round-contract.mjs:790,874,955`) print `code_revision=<hash>`; under jj that hash may
   be an empty or detached local commit. Separately, `check-freshness --witness` accepts the literal
   `HEAD` (F6) and records `revision=HEAD` instead of a 40-hex id, so the receipt cannot be replayed
   from a clone.

## Inference (not directly observed)

- **[INFERENCE]** Each `show(root, 'HEAD', …)` resolves HEAD per subprocess, not once per gate. If a
  concurrent jj command in the same lane rewrites `@` between two gate reads, the gate can mix
  revisions inside one verdict. I did not reproduce the race; the per-call resolution is source fact,
  the race is a consequence.
- **[INFERENCE]** `jj-lane.sh`'s `pushed $(jj_ids "heads(${BRANCH}@origin)" commit_id | head -1)`
  (helper `:116`) assumes a single head; a divergent remote branch would make `head -1` ambiguous.
  Also, `echo "committed $hash"` (`:196`) is printed before `do_push`, which may `jj rebase`
  (`:121`) the unpushed commit; only the `pushed` line is safe to cite. No lane tool parses either
  line today, so this is an integration hazard, not a live defect.
- **[INFERENCE]** `git status` writing `.git/index` while jj writes it can collide on
  `.git/index.lock`; the helper's flock serializes helper invocations only, not other seats' direct
  jj calls. Low severity because git degrades to a non-refreshing status, but the "read-only" label
  is wrong.

## Recommendations

1. **Resolve the anchor once and thread it through.** In each gate replace the literal `'HEAD'` with
   a single `const rev = gitOk(root, ['rev-parse','--verify','refs/heads/master^{commit}'])` (or
   `refs/remotes/origin/master` when the claim is "landed") and pass `rev` to every
   `show`/`ls-tree`/`log`/`diff`/`merge-base`. This is the jj-safe form of all twelve R1 rows and
   does not change behavior on a plain-git checkout where HEAD is `master`'s tip.
2. **Fail closed on anchor drift.** Add `git merge-base --is-ancestor HEAD refs/remotes/origin/master`
   (when the remote ref exists) and emit a distinct finding before any clean verdict. Today a
   detached or empty HEAD is indistinguishable from a landed tip.
3. **Fix the receipt identities.** Print the resolved 40-hex hash for `code_revision=`, and make
   `check-freshness --witness` validate `/^[a-f0-9]{7,40}$/` like the sibling gates (or resolve and
   print the commit id next to the selector).
4. **Compute witness `committed` against the branch, not HEAD.** Use
   `blob(defaultRoot, 'refs/heads/master', script)` (or `origin/master`) so a jj working-copy
   snapshot can never make unlanded checker bytes look committed.
5. **Keep all fixture commits on plain git, with a guard.** The 25 B sites are safe today because
   every fixture root is a fresh tmpdir with `git init`. Add a one-line assertion that
   `<root>/.jj` does not exist before `git init`/`add`/`commit`/`mv`, so a future `--repo` wiring
   mistake cannot commit into a colocated lane.
6. **Adjacent helper fixes:** add `GIT_OPTIONAL_LOCKS=0` (or `--no-optional-locks`) to `print_state`'s
   `git status`, or drop the "read-only" claim; and print `committed` only after a successful push,
   or document that only `pushed` is citable.

## Appendix — audit hygiene

- Live lane untouched: no writes, staging, commits, fetches, checkouts, or stashes. `git` was used
  read-only; `git clone` was used only to copy the repo out.
- No tools installed or upgraded; used the host `git`, `node`, and `jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`
  at `~/.local/bin/jj`.
- Sandbox preserved because it holds the F1/F2/F3 failure states:
  `/fast/scratch/jj-wave/JjAuditTabi-2/` (`t1`, `tabi`, `tabi2`); re-run the quoted commands there.
- Every command shown above was executed; no unrun check is reported as passed.
