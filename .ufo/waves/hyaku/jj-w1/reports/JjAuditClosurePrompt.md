# JjAuditClosurePrompt — audit of `scripts/hyaku/closure-prompt.md` steps 1 and 4 for a jj-colocated lane

Seat: reviewer/auditor (leaf, no subagent dispatch). Date: 2026-10-20.
Target: `/home/vgpnk/Projects/shokunin/scripts/hyaku/closure-prompt.md` at fleet `67a3123`
(step 1 = lines 20–29, step 4 = lines 44–54), plus its caller `scripts/hyaku/jj-lane.sh`
(read only) and `scripts/hyaku/jj-lane-selftest.sh` (read only). No file outside this report
was edited; the replacement text below is a **proposal in the report only**.

Method: the helper was exercised end-to-end in two sandboxes under
`/fast/scratch/jj-wave/JjAuditClosurePrompt/` (bare `origin.git` + clones; every remote was a
local bare repo, never GitHub). No jj command was run with cwd or `-R` anywhere in
`/home/vgpnk/Projects/shokunin`; live repos were inspected only with read-only `git` and `cat`.
The live helper's `state` was replicated by hand rather than executed against live paths.
Sandboxes were removed after the excerpts below were captured. No tool installs.

Tools used as installed: jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5, git 2.56.0.

---

## Findings

### F1 (High) — Step 4's identity claim is false on the helper's rejected-push recovery path: the committer drifts off `protocol-shokunin`

Step 4 currently says the helper "commits under the protocol identity". On the normal path that
is true (author *and* committer). On the recovery path it is not: `do_push()` rebases the
unpushed commit with

```
scripts/hyaku/jj-lane.sh:121
  "$JJ_BIN" --ignore-immutable rebase -b "$tip" -d "${BRANCH}@origin" >/dev/null 2>&1 || continue
```

with **no** per-command `--config user.name/user.email` (the metaedit/commit calls at lines
225–230 do carry them). jj rewrites the rebased commit's committer from the *current repo
config*, keeping the author.

Reproduced with a lane initialized as `lane1`, closure commit `--as protocol`, and a remote
moved by a separate clone:

```
$ jj-lane.sh commit . --as protocol -m "round-1 spotcheck followup" -- corpus/lessons/round-1-verifier-spotcheck.md
committed 757f5b4a406386dff668e2efed95d21aaa1cec7c
pushed 1c316633a1653652a83fdc72e6fe41fa173a1e8d
$ git log -1 --format='A=%an|%ae C=%cn|%ce %H'
A=protocol-shokunin|protocol@shokunin.local C=lane1-shokunin|lane1@shokunin.local 1c316633a165...
```

Worst case, with the lane's repo-level `user.*` config absent (e.g. a `.jj` colocated before
`init` set it), the rewritten committer is the **operator's personal identity**:

```
$ jj --ignore-working-copy config get user.name     # repo config unset
Joao Pedro Veiga
$ jj-lane.sh commit . --as protocol -m "…" -- corpus/lessons/round-2-verifier-spotcheck.md
committed c11b11b34d14e4de0e68f980757d3192f6c0a7b2
pushed a680112f42c65d3092c46517d225c40745c5fbaa
$ git log -1 --format='A=%an <%ae> C=%cn <%ce>'
A=protocol-shokunin <protocol@shokunin.local> C=Joao Pedro Veiga <jpveigao10@gmail.com>
```

Invariant impact: "every lane commit carries the lane identity" holds for `%an/%ae` but fails
for `%cn/%ce` on exactly the closure commit that the closure entry later cites
(`verification.spotcheck`). An author-only conformance check cannot see this.

Coverage gap that let it ship: `jj-lane-selftest.sh` case `d2` checks protocol author+committer
with **no** remote move, and recovery cases `g`/`h` commit `--as "$LANE_ID"`, i.e. the same
identity as the repo config, so a rebase-derived committer is indistinguishable:

```
# d2. --as protocol yields protocol-shokunin on author AND committer.
...
# g. remote moved by operator -> helper commit+push recovers via fetch+rebase.
out=$("$HELPER" commit "$A" --as "$LANE_ID" -m "selftest g" -- LANE-G.md 2>/dev/null)
```

### F2 (High) — Step 1's acceptance `ahead=0` is vacuously true when the state line is degenerate (`local=-`, `remote=-`, `branch=jj/root`); the prompt must fail closed on the state fields

`print_state()` only computes `ahead` when both refs resolve; otherwise `ahead` stays `0`. A
branch ref that is absent therefore reads as "pushed". Demonstrated on a sandbox whose branch
bookmark had been dropped (see mechanism below):

```
$ jj-lane.sh state .
state branch=jj/root local=- remote=- ahead=0 behind=0 head=attached tracked=0 untracked=3
$ git rev-parse --verify -q refs/heads/master || echo 'refs/heads/master ABSENT'
refs/heads/master ABSENT
```

`detect_branch()` returned `jj/root` because git HEAD was *attached* to `refs/jj/root`
(symbolic-ref succeeds, so the `origin/HEAD`/master/main fallbacks at lines 57–63 are never
reached). A closure
judge executing step 1 literally would see `ahead=0` and pass the push clause while the lane
branch does not exist.

How the sandbox reached that state is itself worth recording as a rule-enforcement datum: a
git ref **write** in a colocated repo (`git update-ref -d refs/remotes/origin/master`) was
amplified by the next jj call's `import git refs`, which dropped the local bookmark that was
tracking the now-missing remote bookmark and exported the deletion:

```
$ jj --ignore-working-copy op show 61e139efa70d
import git refs
args: jj file track scratch.txt
Changed local bookmarks:
master:
+ (absent)
- propntsn/0 1c316633 (hidden) round-1 spotcheck followup
Changed remote bookmarks:
master@origin:
+ untracked (absent)
- tracked propntsn/0 1c316633 (hidden) round-1 spotcheck followup
```

Live lanes forbid git writes anyway; the actionable part is that the closure must not treat a
malformed state line as a pass. Require `branch` to name an existing `refs/heads/<branch>` and
`local`/`remote` to be 40-hex.

### F3 (Medium) — `<branch>` in step 1 is unbound, and the obvious derivations are wrong in a jj lane

Step 1 says `merge-base --is-ancestor <hash> <branch>` without saying how to obtain `<branch>`.
The naive commands fail or mislead:

```
$ git rev-parse --abbrev-ref HEAD      # after any jj mutation
HEAD
$ git symbolic-ref -q --short HEAD     # normal post-commit state: detached -> empty
                                        # abnormal state: prints jj/root
```

`HEAD` as the anchor happened to equal the tip in the clean case, but it is `@-` (the working-copy
commit's parent) in general, and in the `refs/jj/root` state it is not a commit at all:

```
$ git rev-parse HEAD
fatal: ambiguous argument 'HEAD': unknown revision ...
fatal: your current branch 'refs/jj/root' does not have any commits yet
```

`@{u}` and `--abbrev-ref HEAD` are unusable; `state`'s `branch=` field is the only stable source,
and it must be validated (F2).

### F4 (Medium) — Step 4's citation rule is incomplete: `committed` and `pushed` can differ, exit 3 emits only `committed`, and one exit-0 path pushes nothing

The helper prints `committed <hash>` (line 235) then, after `do_push`, `pushed <hash>`
(line 111). On a rejected push the first hash is rewritten by the recovery rebase, so only the
second is citable — observed above: `committed 757f5b4a…` → `pushed 1c31663…`; the old hash still
exists as an object but is no longer an ancestor, which is exactly what the step-1 ancestry check
must reject:

```
$ git cat-file -e 757f5b4a406386dff668e2efed95d21aaa1cec7c^{commit} && echo EXISTS
EXISTS
$ git merge-base --is-ancestor 757f5b4a406386dff668e2efed95d21aaa1cec7c refs/heads/master \
    && echo ANCESTOR=yes || echo ANCESTOR=no
ANCESTOR=no
```

Failure-path outputs the current text does not cover:

```
# exit 3: committed, not pushed — only "committed" was printed (no "pushed" line)
committed 89b01a43d724ee45bda1959c100cfa48bc6474f6
jj-lane: push failed after 3 attempts: ... 
$ echo $?
3

# exit 0 and NO push at all: path missing (line 199)
$ jj-lane.sh commit . --as protocol -m probe -- corpus/lessons/does-not-exist.md
warn: skipping missing path corpus/lessons/does-not-exist.md
nothing to commit (no such paths)
exit=0

# exit 0, nothing to commit but push ran (valid idempotent rerun)
nothing to commit
pushed 1c316633a1653652a83fdc72e6fe41fa173a1e8d
```

"Exit 0" alone is therefore not "landed"; the rule must be exit 0 **and** a `pushed <hash>` line,
with `nothing to commit (no such paths)` treated as nothing landed.

### F5 (Low) — "jj resets the git index on every mutation" is imprecise; only snapshotting mutations reset it

Confirmed that a snapshotting jj call destroys a staged entry (`git add f1.txt` → `M  f1.txt`;
after the helper's commit → ` M f1.txt`, `git diff --cached` empty). But a read-only call with
`--ignore-working-copy` does **not** reset it (staged entry survived
`jj --ignore-working-copy file track …`). The practical instruction (never `git add` in a lane)
is unchanged; the parenthetical should say *snapshotting* mutation so it does not misdescribe
`--ignore-working-copy` calls.

### F6 (Low) — "Commit and push only that path" overstates the push: the push ships the branch tip, including any earlier unpushed lane commit

`do_push` pushes the bookmark, not the new commit. If the lane left an unpushed commit (exit 3),
step 4's push lands it too. Reproduced: `jj-lane.sh push .` after an exit-3 commit printed
`pushed 6bc244ce…` without a new commit. This is correct helper behavior (the branch must
converge), but the closure should notice `ahead>0` before step 4 and name what it is publishing.

### F7 (Low) — Step 1 checks the *report's* identity but never the lane commits' identity

Step 1's identity clause is fleet-side only (`git log --format='%an %H' -- <report>`). Nothing
asserts that cited lane hashes carry `{{LANE}}-shokunin`, so the F1 drift and any accidental
foreign-identity commit pass. Add a per-cited-hash author+committer read.

### F8 (Info) — `git status --porcelain` in a colocated lane reports jj-tracked-in-`@` new files as `??`

After `jj file track leftover.md`, git still showed `?? corpus/lessons/leftover.md` (the git
index is not the `@` tree). This is conservative for the leftover check — such a file still
appears — but `state`'s `untracked=` count is the same `??` count, so the two agree; no change
needed beyond not interpreting `??` as "never seen by jj".

### F9 (Info) — The fleet repo is not colocated; fleet-side checks stay plain git

```
$ ls -d /home/vgpnk/Projects/shokunin/.jj
ls: cannot access ...: No such file or directory
```

`git log --format='%an %H' -- <report>` and `fleet-commit.sh` remain correct as written.

### F10 (Info) — A live lane can have HEAD attached or detached; both are fine for the branch-ref check

Read-only replication of `print_state` over the live lanes: `mado-shokunin` HEAD attached to
`master`, `ahead=6` (mid-round), `tameshi-shokunin` attached, `ahead=0`; both keep
`refs/remotes/origin/master`. Sandbox post-commit state was `head=detached`,
`local=remote=pushed`, `ahead=0`. Conclusion: anchor ancestry on `refs/heads/<branch>`, never on
HEAD's attachment state.

---

## Inference

- [INFERENCE] jj 0.45.1 stores repo-level config in the op store keyed by `.jj/repo/config-id`
  (no `config.toml` on disk, even in the sandbox where `init` set it; `jj config list --repo`
  shows the four keys). Live lane repo config therefore could not be audited without running jj,
  which the rules forbid.
- [INFERENCE] In a live lane the F1 drift will read `<lane>-shokunin <lane@shokunin.local>`
  (init sets repo config); the operator-identity outcome needs a `.jj` that never received
  repo config.
- [INFERENCE] The recovery rebase does not rewrite pushed commits: `rebase -b <head of
  <branch>@origin..<branch>>` with `<branch>@origin` as destination; the operator commit
  `bee5c5e5` stayed in the pushed history and the new tip descends from it.
- [INFERENCE] `behind>0` after an operator push is informational for step 1: ancestry of a cited
  hash still holds as long as the operator only added commits; a force-push that drops the cited
  hash must fail the ancestry check (correctly).
- [INFERENCE] The `nothing to commit` path still calls `do_push`, so a rerun of step 4 after a
  successful commit is a safe no-op that reprints the current remote tip.

---

## Recommendations

R1. **Fix the helper's recovery identity (owner: orchestrator; helper is out of my edit scope).**
   In `do_push()`, carry the identity of the commit being rebased into the rebase call, e.g.
   resolve `$id` from the commit's author before rebasing and pass
   `--config user.name=${id}-shokunin --config user.email=${id}@shokunin.local` (or thread the
   `--as` value from `cmd_commit` into `do_push`). Add a selftest case that cannot pass today:
   `init <dir> laneX`, `commit --as protocol`, move the remote from a second clone,
   then assert `%an|%ae|%cn|%ce` all read `protocol-shokunin|protocol@shokunin.local|…`.

R2. **Add a state-line validator to the closure (or to the helper's `state`).** Acceptance requires
   `branch` ∈ `refs/heads/*`, `local` and `remote` matching `^[0-9a-f]{40}$`, `ahead=0`;
   `ahead=0` with `remote=-` is not evidence. `behind>0` is reported, not failing.

R3. **Replace step 1** with the block below (keeps every original clause: report identity +
   SHONEN heading, cited-hash existence + ancestry, no leftover round work, pushed state,
   template contract, marker→failed, status-neutral notes, no jj in the lane).

R4. **Replace step 4** with the block below (keeps: artifact path/heading/content list, the exact
   helper command, push-before-cite, exit-3 recovery, never git add/commit/push).

R5. **Optional live cross-check:** `git -C {{LANE_CWD}} ls-remote origin "refs/heads/$branch"`
   (read-only, no fetch) as a second witness that the cited hash is the remote tip; treat network
   failure as inconclusive, not as a defect.

### Proposed step 1 (replacement text)

```
1. **Step-1 conformance.** The report is committed in the fleet repo by the lane identity
   (`git log --format='%an %H' -- <report>` — the fleet repo is plain git, not colocated) and has
   the `SHONEN` heading with one line per box. In the lane repo (jj-colocated; read-only git only,
   never jj) take one state line and keep its fields:
   `ST=$({{FLEET_ROOT}}/scripts/hyaku/jj-lane.sh state {{LANE_CWD}})` with
   `branch=$(printf '%s\n' "$ST" | sed -n 's/^state branch=\([^ ]*\).*/\1/p')` (same pattern for
   `local`, `remote`, `ahead`, `behind`). Fail closed: `branch` must name an existing
   `refs/heads/<branch>` (never `jj/root`, `?`, or `HEAD`) and `local`/`remote` must be 40-hex
   hashes — `ahead=0` is vacuous when either is `-` or the branch ref is gone (observed). For
   every lane commit `<hash>` cited by the report: it exists
   (`git -C {{LANE_CWD}} cat-file -e "<hash>^{commit}"`; a jj *change id* does not resolve and is
   a defect) and it is an ancestor of the branch
   (`git -C {{LANE_CWD}} merge-base --is-ancestor "<hash>" "refs/heads/$branch"`), never `HEAD` and
   never `@{u}` — after jj mutations git HEAD is detached at `@-` (or attached to `refs/jj/root`),
   and a hash that was committed and then rewritten by the helper's recovery rebase still exists
   as a git object but is no longer an ancestor — exactly the pre-push hash a report may not
   cite — which this check must reject. Ancestry is not push evidence (a locally committed,
   never-pushed hash is an ancestor too): push evidence is the state line with `ahead=0`, a
   non-`-` `remote`, and `git -C {{LANE_CWD}} status --porcelain` empty of round work (new files
   the lane tracked in jj still show as `??`; `behind>0` is an informational operator push, not a
   defect). Identity: for each cited hash
   `git -C {{LANE_CWD}} log -1 --format='%an <%ae> | %cn <%ce>' "<hash>"` must read
   `{{LANE}}-shokunin <{{LANE}}@shokunin.local>` for author and committer; a committer naming
   another identity is the helper's recovery-path defect (step 4) — name it in notes,
   status-neutral. The prompt carries the template contract. Marker report (no checkable
   work/commit) → status `failed`. Defects are named in notes, status-neutral. Never run `jj`
   against the lane — not from the lane cwd, not with `-R`; even `jj log` without
   `--ignore-working-copy` snapshots the lane's working copy. The helper's `state` is pure git and
   is the only lane introspection allowed.
```

### Proposed step 4 (replacement text)

```
4. **Write `{{LANE_CWD}}/corpus/lessons/round-{{ROUND}}-verifier-spotcheck.md`** (non-author;
   headed `author: hyaku closure (non-author integrator, {{JUDGE_MODEL}})`): conformance results,
   per-claim re-check with commands and observed output, per-axis verdicts, spot-check table
   (item · decision · re-opened source · agree/disagree · reason), trend verdicts with evidence,
   and routed defects the lane must fix next round. Commit exactly that path through the jj lane
   helper (never a directory; commits are path-limited, the push ships the branch tip):
   `{{FLEET_ROOT}}/scripts/hyaku/jj-lane.sh commit {{LANE_CWD}} --as protocol -m "round-{{ROUND}} verifier spot-check (integrator, hyaku): non-author admit/reject" -- corpus/lessons/round-{{ROUND}}-verifier-spotcheck.md`
   Success is exit 0 **and** a `pushed <hash>` line: cite only that hash, as `pushed <hash>`. The
   `committed <hash>` line printed before the push is not citable — on a rejected push the helper
   fetches, rebases only the unpushed commit, and retries, so the committed hash is rewritten and
   the pushed hash differs (observed: committed 757f5b4a… → pushed 1c31663…; the old hash survives
   as an object but is no longer an ancestor). Exit 3 = committed but not pushed: do not cite;
   rerun `jj-lane.sh push {{LANE_CWD}}` and cite the `pushed` hash that run prints (the commit may
   again have been rewritten). Exit 0 with `nothing to commit (no such paths)` and no `pushed`
   line = nothing landed (usually the file was not written): write it and rerun. Exit 0 with
   `nothing to commit` plus `pushed <hash>` is a valid rerun (path already committed); cite that
   hash. Before writing the closure entry, confirm the landed state: `jj-lane.sh state {{LANE_CWD}}`
   shows `ahead=0` with a 40-hex `local`, the cited hash is an ancestor of
   `refs/heads/<branch>`, and
   `git -C {{LANE_CWD}} log -1 --format='%an <%ae> | %cn <%ce>' <hash>` reads
   `protocol-shokunin <protocol@shokunin.local>` for author and committer. If the committer names
   another identity, the helper's recovery rebase ran without the per-command identity (known
   helper defect): the commit landed and is still cited, and the drift goes in notes for the
   orchestrator. If `state` showed `ahead>0` before this step, the push also lands those earlier
   commits — name them in notes. Never `git add`/`git commit`/`git push`/`git stash`/`git
   checkout`/`git reset` in a jj-colocated lane (a snapshotting jj mutation resets the git index
   and destroys staged entries) and never run any other jj command in the lane.
```

---

## Verification log (all commands in the sandboxes unless marked live)

| # | Check | Result |
|---|---|---|
| 1 | `jj-lane.sh init` on a fresh clone | `state … ahead=0 head=attached tracked=0 untracked=0` |
| 2 | helper commit of one new file, other tracked file modified, unrelated new files present | commit contains only the named path (`jj diff -r master --summary` → `A corpus/lessons/round-1-verifier-spotcheck.md`); `M README.md`, `?? leftover.md`, `?? scratch.txt` remain outside |
| 3 | identity of that commit | `A=protocol-shokunin|protocol@shokunin.local C=protocol-shokunin|protocol@shokunin.local` |
| 4 | `committed` vs `pushed` | identical on the normal path (`ee8e30fb…`) |
| 5 | push blocked (origin → nonexistent path) | exit 3, only `committed 89b01a43…`, `state … ahead=1`, bare remote still at `ee8e30fb…` |
| 6 | ancestry of that unpushed hash | `merge-base --is-ancestor 89b01a43… master` → true (ancestry alone is not push proof) |
| 7 | remote moved by a second clone, then helper commit | `committed 757f5b4a…` then `pushed 1c31663…`; operator commit kept; old hash exists but `ANCESTOR=no` |
| 8 | identity after that recovery | `A=protocol… C=lane1-shokunin|lane1@shokunin.local` (**F1**) |
| 9 | same with repo `user.*` unset | `A=protocol… C=Joao Pedro Veiga <jpveigao10@gmail.com>` (**F1 worst case**) |
| 10 | idempotent step-4 rerun | `nothing to commit` + `pushed 1c31663…`, exit 0 |
| 11 | missing path | warn, `nothing to commit (no such paths)`, exit 0, no push (**F4**) |
| 12 | `git add` then helper commit | `M  f1.txt` → ` M f1.txt`, `git diff --cached` empty (**F5**) |
| 13 | `git add` then `--ignore-working-copy file track` | staged entry survives (**F5 precision**) |
| 14 | jj change id as a cited hash | `git cat-file -e "<changeid>^{commit}"` fails; commit id resolves |
| 15 | `git rev-parse --abbrev-ref HEAD` post-mutation | `HEAD` (**F3**) |
| 16 | degenerate repo (branch ref dropped; see F2 mechanism) | `state branch=jj/root local=- remote=- ahead=0 …`, `refs/heads/master` absent (**F2**) |
| 17 | live `mado-shokunin` (read-only replication) | HEAD attached `master`, `ahead=6`, live leftovers visible; spotcheck `27cd06f` is protocol/protocol |
| 18 | live `tameshi-shokunin` | HEAD attached `master`, `ahead=0`; spotcheck `28aeef4` is protocol/protocol |
| 19 | fleet root | no `.jj`; fleet-side git checks unaffected |
| 20 | selftest coverage read | `d2` = protocol identity without rejection; `g`/`h` = rejection with `--as "$LANE_ID"` (gap) |

## Unrun checks (explicitly not passing)

- No jj command was run in `/home/vgpnk/Projects/shokunin` or any lane repo; live jj repo config
  was not inspected (jj 0.45.1 keeps it in the op store, not `config.toml`).
- The helper was not executed against live paths; `state` was replicated by hand there.
- Step 5 (`append-closure.py`) was read, not run; no closure entry was written.
- No verification of GitHub-side state: all pushes went to sandbox bare repos.
