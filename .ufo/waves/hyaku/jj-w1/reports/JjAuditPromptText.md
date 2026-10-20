# JjAuditPromptText — VCS instruction audit of `templates/round-prompt.md` + `scripts/hyaku/lane-addendum.md`

Seat `JjAuditPromptText-2`, wave `hyaku/jj-w1`, 2026-10-20.
Artifact under test: jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`; helper
`scripts/hyaku/jj-lane.sh` at fleet commit `67a3123` (11:11:34 -03), with `HYAKU_VCS=jj`
(`scripts/hyaku/hyaku.env:10`).
Sandbox: `/fast/scratch/jj-wave/JjAuditPromptText` (kept; §6). Live repos were read-only:
`git log/show/status/rev-parse/config --get`, `cat` of `.jj/repo/config-id` and
`~/.config/jj/repos/*/config.toml`, and hyaku state files. **No jj command ran in a live repo, no
live lane/fleet script was executed, and no sandbox push went anywhere but a sandbox bare repo.**
`jj-lane-selftest.sh` was read, not run, because it clones a live lane (wave rule: don't execute
fleet scripts that resolve to live paths); every behavioral claim below is from an independently
rebuilt sandbox.

Deliverable: the replacement text proposal is §3.

---

## 1. Findings (observed)

| ID | Location | Sev | Finding |
|---|---|---|---|
| A1 | `templates/round-prompt.md:131-140` | High | §5 still orders a raw `git commit` + `git push` in the lane repo, which addendum §4 forbids |
| A2 | `templates/round-prompt.md:23,106-110` | High | "commit hash" is never qualified: the helper's `committed <hash>` is provisional and can be rewritten by push recovery |
| A3 | `templates/round-prompt.md:133-134` | Medium | fleet-report commit is not routed through `fleet-commit.sh`; a lane may run `git` (or `jj`) at the fleet root |
| B1 | `lane-addendum.md:116-141` | High | `snapshot.auto-track="none()"` is never stated as a precondition and `commit` does not enforce it; pre-helper colocated lanes pollute `@` on first snapshot |
| B2 | `lane-addendum.md:126-127` | High | conflict refusal (`exit 3`, "unresolved conflicts") has no recovery path; live lanes' `::bookmarks()` immutable alias makes the obvious `jj squash` fail |
| B3 | `lane-addendum.md:126,133-134` | High | `committed` vs `pushed` distinction is stated once but not enforced, and "never rewrite a pushed commit" is absent although `jj git push` is force-with-lease |
| B4 | `lane-addendum.md:127-128` | High | "a named directory commits like `git add <dir>`" is false for new files >1 MiB (silently skipped) and for already-tracked ignored files (included) |
| B5 | `lane-addendum.md:126` | Medium | `nothing to commit` still prints `pushed <oldhash>` and exits 0, inviting misattribution |
| B6 | `lane-addendum.md:104-115` | Medium | `.ufo/state/` is never stated as a never-commit invariant, and the helper's guard is bypassable with a `./` prefix |
| B7 | `lane-addendum.md:110-115` | Medium | misroot sweep does not say to commit the copied file through the helper, nor its order relative to the lane commit |
| B8 | `lane-addendum.md:142-144` | Medium | inherited-state "revert" has no jj primitives; `git checkout/stash` are banned and `jj file untrack` alone fails on non-ignored files |
| B9 | `lane-addendum.md:116-118` | Medium | jj §4 is unconditional in a roster with main-repo lanes (`repo=.`), where `LANE_CWD` is the fleet root and init would colocate it |
| B10 | `lane-addendum.md:20` | Low | the L1 return summary asks for "lane HEAD", which is always `head=detached` under jj |
| B11 | `lane-addendum.md:24-25` | Low | "run lane commands as `git -C {{LANE_CWD}} …`" conflates read-only git with writes |
| B12 | `lane-addendum.md:54` | Low | "commit them as wave evidence" does not route through the helper |
| B13 | `lane-addendum.md:126-133` | Low | `state tracked=` also counts ` A` intent-to-add entries produced by auto-track pollution |
| C1 | live | High | 0 of 190 rendered prompts carry the helper; 39 carry the old git commit order; the six running rounds predate `HYAKU_VCS=jj` |
| C2 | live | High | `mado`/`tameshi` `.jj` repo configs (2026-10-19 20:38) have no `snapshot.auto-track`; global config has none either |

### Inventory — every VCS instruction found

`templates/round-prompt.md` (canonical contract; rendered by `render_prompt`, then the addendum is
appended):

| Line | Instruction | Status |
|---|---|---|
| 1 | working dir `{{FLEET_ROOT}}/<{{LANE}}-repo>` (the lane repo path) | kept; note the template may not use `{{LANE_CWD}}` |
| 23 | "measured commit" recorded per claim | qualify: branch commit, never `HEAD` (§3.2) |
| 104-106 | evidence pointer may be "commit hash" | qualify with the pushed-hash rule |
| 107-108 | **Landed changes** tied to "the commit hash that carries it" | qualify: helper-printed `pushed <hash>` (§3.2) |
| 109-110 | measurement "commit it was measured against" | qualify: `git rev-parse <branch>` (§3.2) |
| 131-140 | §5: lane commit + push, fleet report commit + push, push scope, L0 append | rewrite (§3.1): helper for child lanes, `fleet-commit.sh` for the report, never jj at the fleet root |

The template contains **no** identity, pathspec, `.ufo/state`, misroot, or inherited-state
instruction; every such invariant exists only in the addendum. The proposed §5 adds a one-line
pointer to addendum §4 so a lane cannot miss the mechanics.

`scripts/hyaku/lane-addendum.md` (appended to the rendered template by `inline.sh:99`):

| Line | Instruction | Status |
|---|---|---|
| 20 | L1 return summary asks for "lane HEAD" | rewrite: lane tip `local=` / last pushed hash (§3.3) |
| 24-25 | run lane commands as `git -C {{LANE_CWD}} …` | limit to read-only; writes via helper (§3.3) |
| 26-29 | earlier attempt's "uncommitted outputs" are inherited | kept; primitives added in §3.6 |
| 54 | wave specs "commit them as wave evidence" | route through the helper (§3.3) |
| 88-91 | seats never run `jj` or any git write | kept as is |
| 104-109 | write scope; never edit `.ufo/state/`, watchdog, fleet scripts | kept; explicit never-commit rule added in §3.5 |
| 110-115 | misroot sweep: `git status --porcelain` at fleet root, copy→`cmp`→delete | add helper commit + `ahead=0` check (§3.4) |
| 116-121 | identity + helper-only commits + recovery semantics | kept; preconditions added (§3.5) |
| 126-127 | cite `pushed <hash>`; exit 3 → rerun push | extend: provisional `committed`, nothing-to-commit, conflict recipe (§3.5) |
| 127-128 | named-directory and >1 MiB rule | correct semantics (§3.5) |
| 128-130 | never git add/commit/stash/checkout/reset/push; index reset rationale | kept (verified) |
| 130-134 | read-only git list, detached HEAD, never `@{u}`, `--ignore-working-copy`, `jj restore` | kept; add `jj file untrack` mechanics and never-rewrite-pushed rule (§3.5) |
| 135 | git-write gates only on a sandbox clone | kept |
| 136-141 | fleet commits on git only through `fleet-commit.sh`; report lands last, cites pushed hash | kept |
| 142-148 | inherited state: commit under this round's entry or revert | add jj primitives (§3.6) |

### A. `templates/round-prompt.md` — the canonical contract still says git

**A1 [High] §5 line 133 orders exactly what addendum §4 line 128 forbids.**

```
$ nl -ba templates/round-prompt.md | sed -n '131,140p'
   131  ## 5. Commit, push scope, L0 side channel
   132
   133  - Round end: commit (`round-{{ROUND}}`) inside your lane repo, then push. Also commit and
   134    push the report on the fleet repo.
   135  - **Push scope:** only the fleet repo remote and your own {{LANE}} lane remote. Domain
   136    source trees are **read-only** — upstream work is documented in the report, never
   137    pushed.
```

and the addendum it is composed with:

```
$ nl -ba scripts/hyaku/lane-addendum.md | sed -n '116,130p'
   118  ... Commit ONLY through the
   119  lane helper, ...
   128     `git commit`, `git stash`, `git checkout`, `git reset` or `git push` in the lane: jj resets the git
   129     index on every mutation, so staged entries are destroyed. ...
```

Composition path: `inline.sh:98` `render_prompt` + `inline.sh:99` appends the addendum; the
addendum says "Sections 1–5 above are the canonical round contract; this section adds host
mechanics and never relaxes them" (`lane-addendum.md:22-23`). A lane reading §5 first is told to
run `git commit`/`git push`; the addendum then forbids it. Rendered proof (mado round 17,
`.ufo/prompts/mado-round-17.md:133`) contains the template bullet; any L1 prompt rendered after
11:11 would contain both texts side by side (no L1 prompt has been rendered since 10:51 — see C1;
closure prompts use a separate file and were updated).

Consequence measured in the sandbox: a `git add`-staged entry is destroyed by the next helper
mutation, so the "git way" silently loses staged work:

```
$ git add LOG.md; echo "staged_before=$(git diff --cached --name-only | tr '\n' ' ')"
staged_before=LOG.md
$ jj-lane.sh commit <lane> --as testlane -m "round-1: scratch2" -- scratch2.txt
committed 6c91593c382b763e7a34e0709406c3adc6981181
pushed 6c91593c382b763e7a34e0709406c3adc6981181
$ echo "staged_after_commit=$(git diff --cached --name-only | tr '\n' ' ')"; git status --porcelain
staged_after_commit=
?? .ufo/
?? LOG.md
$ git show master:LOG.md
fatal: path 'LOG.md' exists on disk, but not in 'master'
```

**A2 [High] "commit hash" is ambiguous between the helper's two printed lines.** Template line 107
("**Landed changes** — every change tied to a LOG.md entry and to the commit hash that carries it"),
line 110 ("the commit it was measured against") and line 23 ("measured commit") name no specific
hash. In a recovery, the two differ and the first is orphaned (B3/T1 below).

**A3 [Medium] fleet-report commit is not routed.** Lines 133-134 say "commit and push the report on
the fleet repo" without naming `fleet-commit.sh`; the fleet root is a plain git repo and must never
be colocated (B9). A lane that tries `jj` there gets a misleading hint:

```
$ cd <plain git clone>; jj status
Error: There is no jj repo in "."
Hint: It looks like this is a git repo. You can create a jj repo backed by it by running this:
jj git init
```

### B. `scripts/hyaku/lane-addendum.md`

**B1 [High] auto-track precondition is unstated and unenforced.**

The helper's safety note is only in its source comment, and `cmd_commit` relies on init having set
`snapshot.auto-track="none()"`. Repro in a lane colocated without the helper's init (the state of
the two live colocated lanes before today):

```
$ git init --bare remote5.git; git clone remote5.git lane5   # base commit pushed
$ cd lane5 && jj --config 'snapshot.auto-track="all()"' git init --colocate .
$ cd .. && mkdir -p lane5/seat-scratch && echo scratch > lane5/seat-scratch/notes.md && echo scratch2 > lane5/SCRATCH2.md
$ echo named >> lane5/README.md
$ jj-lane.sh commit lane5 --as testlane -m "round-1: named only" -- README.md
rc=3            # push failed for an unrelated bookmark-tracking reason in this manual setup
committed f3873ef03b08e9cb61d1345a0580d13630dc4b25
$ git -C lane5 status --porcelain
 A SCRATCH2.md
 A seat-scratch/notes.md
$ (cd lane5 && jj --ignore-working-copy file list) | grep -E 'scratch|SCRATCH'
SCRATCH2.md
seat-scratch/notes.md
```

The named-only commit did not include them, but the snapshot had already tracked them into `@`;
naming a directory later swept one in:

```
$ jj-lane.sh commit lane5 --as testlane -m "round-1: seat dir" -- seat-scratch
committed 71cc75a7fa9932a9be297a63c302803c249fbb91
$ git -C lane5 show --format= --name-only 71cc75a7...   # (local tip)
seat-scratch/notes.md
```

Live state (static file reads; no jj invoked):

```
$ cat ~/.config/jj/repos/b7d9811b7038ba799207/config.toml   # mado, mtime 2026-10-19 20:38:57
[revset-aliases]
"trunk()" = "master@origin"
"immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"
[user]
name = "mado-shokunin"
email = "mado@shokunin.local"
                               # no [snapshot] section
$ cat ~/.config/jj/config.toml                 # global: user, ui.default-command, git.auto-local-bookmark only
$ git -C mado-shokunin status --porcelain      # 4 untracked round-17 paths at read time
?? .ufo/waves/round-17/drafts/
?? .ufo/waves/round-17/evidence/measure-c1.json
?? .ufo/waves/round-17/tripwire/
?? .ufo/waves/round-17/w1/reports/
```

`mado` and `tameshi` were colocated on 2026-10-19, before the helper; their repo configs predate
it (mtimes 20:38/20:39) and carry no `auto-track` key. The helper's own `init` sets it and
`inline.sh:90` runs init at dispatch, so lanes dispatched after 11:11 are safe; these two lanes and
any skipped init are not.

**B2 [High] the conflict refusal has no recovery path in the prompt.**

```
$ jj-lane.sh commit lane2 --as testlane -m "round-1: conflicting edit" -- README.md
committed 30d0944b269d80edb0481a87d16b583040ae9048
jj-lane: local master tip has unresolved conflicts — resolve in the lane, then retry
$ echo rc=$?
rc=3
$ jj-lane.sh state lane2
state branch=master local=05b569b3422f3b351ada6c2a5d1f781f5a9bd284 remote=57cb6faf7c9a8ec7f6c213bdee1dec42ec001f7b ahead=1 behind=0 head=detached tracked=5 untracked=0
$ (cd lane2 && jj status)
Parent commit (@-): xpnnxpwk 05b569b3 master* | (conflict) round-1: conflicting edit
Warning: There are unresolved conflicts at these paths:
README.md    2-sided conflict
```

The addendum's only exit-3 advice is "rerun `jj-lane.sh push` (never force)" (line 126-127), which
cannot clear a conflicted bookmark tip. The natural resolution is blocked in live lanes because
both carry the strict immutable alias (dump above); reproduced by setting the same alias in the
sandbox lane:

```
$ (cd lane2 && jj squash)                 # @ created on top of the conflicted tip
Error: Commit 5ced14b584f1 is immutable
Hint: Could not modify commit: xpnnxpwk 5ced14b5 master | round-1: conflicting edit
$ (cd lane2 && jj --ignore-immutable squash)
Working copy  (@) now at: tokmkrlw 69dc78ee (empty)
Parent commit (@-)      : xpnnxpwk 41e2ea80 master* | round-1: conflicting edit
$ jj-lane.sh push lane2
pushed 41e2ea8039f65a27e38699ff1a4577e3be4b2ebb
$ git -C lane2 merge-base --is-ancestor 57cb6fa master && echo "operator commit still ancestor"
operator commit still ancestor
```

So the working recipe is `jj new <state local=>`, edit to the resolution, `jj --ignore-immutable
squash`, `jj-lane.sh push` — none of which the prompt says.

**B3 [High] `committed <hash>` is provisional; a rewrite of a pushed commit is force-pushed.**

Non-conflict recovery (operator push moves the remote, lane commits):

```
$ jj-lane.sh commit lane4 --as testlane -m "round-1: L4" -- L4.md
committed f0de128dd00302229083b3fb17457b7a3111bb71
pushed 8f2321f76064a7e0feccc99d37499fd1466d460d
$ git -C lane4 merge-base --is-ancestor f0de128d master && echo ancestor || echo "not an ancestor"
not an ancestor
```

`committed` is the pre-rebase commit; only `pushed` is on the branch. The addendum says "cite the
hash it prints as `pushed <hash>`" (line 126) but the helper prints `committed` first, and the
template language says "commit hash" (A2). Nothing in the text forbids a lane-side rewrite of a
pushed commit, and `jj git push` will then update the remote in place:

```
$ jj git push --help | sed -n '9,17p'
When pushing a bookmark or tag, the command pushes all commits in the range from the remote's
current position up to and including its target commit. ...
If the local reference has changed from the last fetch, push will update the remote reference to the
new position after passing safety checks. This is similar to `git push --force-with-lease` - the
remote is updated only if its current state matches what Jujutsu last fetched.
```

Observed: a pushed commit `5ced14b` was rewritten by `jj --ignore-immutable squash` and
`jj-lane.sh push` moved the sandbox remote to `41e2ea80`; `git -C remote2.git merge-base
--is-ancestor 5ced14b master` → `NOT an ancestor (rewritten on remote)`. The helper's recovery
itself is correct (it rebases only `heads(<branch>@origin..bookmarks(<branch>))`), but the prompt's
"any other jj call (yours only)" (line 133-134) is broad enough to allow a rewrite that the
protocol invariant forbids.

**B4 [High] named-directory and big-file semantics are wrong as written.**

```
$ mkdir bigdir; head -c 2097152 /dev/urandom > bigdir/MED2.bin; echo small > bigdir/small.md
$ jj-lane.sh commit lane --as testlane -m "round-1: dir commit" -- bigdir
committed 77bd1ba4489361c9161939e932ed6c7bbba0d0be
pushed 77bd1ba4489361c9161939e932ed6c7bbba0d0be
$ git ls-tree -r --name-only master -- bigdir
bigdir/small.md
$ git cat-file -s master:bigdir/MED2.bin
fatal: path 'bigdir/MED2.bin' exists on disk, but not in 'master'
```

Naming the file explicitly works (selftest j; reproduced):

```
$ jj-lane.sh commit lane --as testlane -m "round-1: big file" -- bigdir/MED2.bin
committed cc64d0fbe02d09033f56a9d286f2716f801691d9
$ git cat-file -s master:bigdir/MED2.bin
2097152
```

Also, "ignored content stays out" is true only for *untracked* ignored files; a tracked ignored
file rides a directory commit:

```
$ printf '*.tmp\n' >> .git/info/exclude; echo t > scratchdir/s.tmp
$ (cd lane4 && jj file track --include-ignored -- scratchdir/s.tmp)
$ jj-lane.sh commit lane4 --as testlane -m "round-2: tracked ignored" -- scratchdir
pushed 129ea8448715d91a03460ed28a91c9f68882cd15
$ git -C lane4 show --format= --name-status 129ea844
A       scratchdir/s.tmp
```

Deletions under a named directory *are* committed (verified: `-- docs` → `D docs/d1.md`), which the
text does not mention either way.

**B5 [Medium] `nothing to commit` still prints a `pushed` line.**

```
$ jj-lane.sh commit lane --as testlane -m "round-1: noop" -- README.md
nothing to commit
pushed 6c91593c382b763e7a34e0709406c3adc6981181
rc=0
```

That `pushed` hash is the pre-existing branch tip (`6c91593c`, from the previous commit), not this
round's work. A lane that cites "the `pushed` line" as instructed attributes stale work to this
round. The helper also exits 0 for a nonexistent path (`warn: skipping missing path …, nothing to
commit (no such paths)`), so a path typo is invisible except for that warning.

**B6 [Medium] `.ufo/state/` is never stated as an invariant, and the helper guard is bypassable.**

```
$ jj-lane.sh commit lane --as testlane -m ctrl -- .ufo/state/y.json
driver runtime is never committed by a lane: .ufo/state/y.json
rc=64
$ jj-lane.sh commit lane --as testlane -m "round-1: state bypass" -- ./.ufo/state/y.json
committed de0828e0f6f6083f3f094358040675e3a54c7e9a
pushed de0828e0f6f6083f3f094358040675e3a54c7e9a
$ git ls-tree -r --name-only master -- .ufo
.ufo/state/y.json
```

The template §5 and addendum §4 never say "`.ufo/state/` is never committed"; only §3 line 108/115
says never *edit*/touch driver files at the fleet root, which does not read as a lane-repo commit
ban.

**B7 [Medium] misroot sweep has no commit step and no ordering.**

The text (lines 110-115) copies the file, `cmp`s it, deletes the fleet copy — then stops. With
`auto-track=none()` the copy stays `??` until named; verified:

```
$ printf 'seat note\n' > lane4/MISROOTED-seat-note.md
$ git -C lane4 status --porcelain | grep MISROOT
?? MISROOTED-seat-note.md
$ jj-lane.sh commit lane4 --as testlane -m "round-2: misroot note" -- MISROOTED-seat-note.md
pushed 5b10f9acc57e21eb2c51b39c3b4b4539c60f44cf
```

Unless the lane adds the copied path to a helper commit, the closure's "no uncommitted round work"
check (`closure-prompt.md:24-27`) flags it.

**B8 [Medium] inherited-state text gives no jj primitives, and the obvious one fails.**

`jj restore -- <path>` works for tracked edits. `jj file untrack` does **not** work for non-ignored
scratch:

```
$ (cd lane5 && jj file untrack -- SCRATCH2.md seat-scratch/notes.md)
Error: 'SCRATCH2.md' and 1 other files are not ignored.
Hint: Files that are not ignored will be added back by the next command.
Make sure they're ignored, then try again.
rc=1
$ printf 'SCRATCH2.md\nseat-scratch/\n' >> .git/info/exclude
$ (cd lane5 && jj file untrack -- SCRATCH2.md seat-scratch/notes.md); echo rc=$?
rc=0
```

So the prompt's "revert" needs three named primitives (`jj restore`, ignore-then-`jj file untrack`,
`rm`), plus the warning that `jj status` snapshots (rewriting `@` and clearing the git index).

**B9 [Medium] the jj text is unconditional in a roster with main-repo lanes.**

```
$ sed -n '19,21p' shokunin.conf
LANES="
protocol|.|fleet-meta: protocol soundness, gate integrity
aggregator|.|cross-lane quality, mint and dormancy calls, corpus review
```

`LANE_CWD` for `repo=.` is `$SHOKUNIN_ROOT` (`shokunin-watchdog.sh:76-78`), and
`inline.sh:90` calls `lane_vcs_init "$lane" "${LANE_CWD[$lane]}"` for any dispatched lane, i.e.
`jj-lane.sh init` on the fleet root would colocate it. The fleet root has no `.jj` (`ls -d .jj` →
"cannot access"), and jj's hint invites exactly that (`jj git init`, excerpt in A3). The hyaku pool
(`scripts/hyaku/pool.txt`) currently excludes protocol/aggregator, so this is latent, not live —
but the addendum is generic and the template is shared.

**B10-B13 [Low] smaller wording defects.**
`lane-addendum.md:20` asks the L1 to return "lane HEAD"; under jj `state` reports `head=detached`
after any helper commit, and `git rev-parse HEAD` is `@-`, not the branch. `:25` prescribes
`git -C {{LANE_CWD}} …` as the lane-command form without limiting it to reads. `:54` says "commit
them as wave evidence" without the helper. `:126-133` relies on `state tracked=`, which counts
` A` intent-to-add entries produced by auto-track pollution (B1) indistinguishably from lane work.

### C. Live operational state

**C1 [High] every currently rendered prompt carries the pre-jj commit order.**

```
$ ls .ufo/prompts/*.md | wc -l                     # 190
$ grep -l 'jj-lane.sh commit' .ufo/prompts/*.md | wc -l   # 0
$ grep -l 'Lane-repo commits carry' .ufo/prompts/*.md | wc -l  # 39
$ ls -t .ufo/prompts/*.md | head -1
.ufo/prompts/mado-round-17.md                      # mtime 10:51:17
$ sed -n '253,259p' .ufo/prompts/mado-round-17.md
4. **Commit order (landed = committed and pushed).** Lane-repo commits carry
   `mado-shokunin <mado@shokunin.local>` (check `git config user.name`), are
   pathspec-limited (never `add -A` / `commit -a`), and are pushed (`git push`) BEFORE the report is
   written. ...
```

The six live claims (`~/.local/state/shokunin-hyaku/claims/*`) are kaidoku r17, kama r16, mado r17,
souji r16, tabi r16, tameshi r16, all dispatched 10:14 or 10:51 — before the helper commit at 11:11
and `HYAKU_VCS=jj` at 11:10. mado and tameshi are the colocated lanes; their old prompts tell them
to commit with git and check `git config user.name` (both identities are set: `mado-shokunin
<mado@shokunin.local>`, `tameshi-shokunin <tameshi@shokunin.local>`). mado's HEAD was still
`attached` at read time (`HEAD=master=3e9848a`), so its old-path `git commit`+`git push` would still
work until any jj call detaches HEAD. Closure prompts are consistent going forward: 1 of 34
contains the helper text (kama's closure, rendered 11:16).

**C2 [High] the colocated lanes carry no auto-track setting and the strict immutable alias.**
Excerpts in B1; also `tameshi-shokunin` config mtime 20:39:15, same shape. Both configs are the
2026-10-19 manual colocation, not helper `init` output (the helper would have added `[snapshot]`).

---

## 2. Inference [INFERENCE]

- [INFERENCE] The template/addendum contradiction (A1) is a contract defect, not a wording
  preference: the addendum declares the template canonical and non-relaxable, and the template's §5
  is the first VCS instruction in the composed prompt. A lane cannot satisfy both texts without
  knowing which wins.
- [INFERENCE] For mado r17 and tameshi r16, the stale git instructions are benign only while HEAD
  stays attached. One jj invocation detaches HEAD (`git symbolic-ref` → DETACHED after the first
  helper commit; `git rev-parse @{u}` → `fatal: HEAD does not point to a branch`), after which a
  git commit would land on a detached HEAD. I did not exercise that exact chain (the wave forbids
  git writes in live lanes and the sandbox has no detached-HEAD git-commit case); the `@{u}`
  failure is measured, the commit consequence is inferred from git semantics.
- [INFERENCE] B1's live impact: if mado r17 runs the helper before its next `init`, the helper's
  first snapshotting call (`jj diff --summary -- <paths>`) will track its four untracked round-17
  paths into `@`; whether any are committed depends on the paths the lane names. Round evidence
  under `.ufo/waves/round-17/` is intended to be committed, so the damage is bounded to what a
  later directory commit sweeps — but a `corpus/` or `scripts/` directory commit could carry
  unrelated tracked-in-`@` scratch.
- [INFERENCE] Hardening `commit` to pass `--config 'snapshot.auto-track="none()"'` on its own
  snapshotting calls is strictly safer than trusting `init`, because the helper is the only code
  path guaranteed to run in every lane, and `init` demonstrably did not run for the two pre-existing
  lanes.
- [INFERENCE] The helper's `state tracked=` remains the only cheap leftover check because
  `git status` is read-only and `jj` reads are forbidden to seats; B13 is a precision warning, not
  a reason to drop `state`.
- [INFERENCE] The `jj git init` hint printed in a plain git repo is the most dangerous string in
  this whole surface: a lane that reads it and runs it at the fleet root would colocate the live
  fleet repo. The prompt must name that prohibition explicitly.

---

## 3. Proposed replacement text (deliverable)

Rendering constraints verified first:

- The **template** is rendered by `render_prompt` (`scripts/shokunin-watchdog.sh:166-181`), which
  substitutes only `{{FLEET_ROOT}}/<{{LANE}}-repo>`, `<{{LANE}}-repo>`, `{{LANE_REPO}}`,
  `{{LANE}}`, `{{ROUND}}`, `{{AXES}}`, `{{FLEET_ROOT}}`. **It does not substitute `{{LANE_CWD}}`,
  `{{PREV}}`, `{{ATTEMPT}}` or `{{BASE}}`** — the proposed §5 below therefore uses
  `{{FLEET_ROOT}}/<{{LANE}}-repo>` only.
- The **addendum** is rendered by `subst` (`scripts/hyaku/inline.sh:43-57`), which does substitute
  `{{LANE_CWD}}`, `{{PREV}}`, `{{ATTEMPT}}` and the rest.
- I replayed the exact `render_prompt` substitution sequence on the proposed §5 text: 0 leftover
  `{{` tokens.

### 3.1 `templates/round-prompt.md` — replace §5 (lines 131-140) with

```markdown
## 5. Commit, push scope, L0 side channel

- **Child lanes (`repo != .`):** the lane repo is git-backed and jj-colocated, and every lane VCS
  write goes through the helper — never `git add`, `git commit`, `git stash`, `git checkout`,
  `git reset` or `git push` there (jj resets the git index on every mutation, so staged entries
  are destroyed):

      {{FLEET_ROOT}}/scripts/hyaku/jj-lane.sh commit {{FLEET_ROOT}}/<{{LANE}}-repo> --as {{LANE}} \
        -m "round-{{ROUND}}: <what>" -- <repo-relative path>...

  It tracks exactly the named paths, commits under
  `{{LANE}}-shokunin <{{LANE}}@shokunin.local>`, moves the branch bookmark, and pushes.
  **Landed = pushed:** cite only the helper's
  `pushed <hash>` line, and only after it prints. The `committed <hash>` it prints first is
  provisional — a push-recovery rebase rewrites it and the old hash is not an ancestor of the
  branch. `nothing to commit` means the named paths produced no change; the `pushed <hash>` after
  it is a pre-existing tip, not this round's commit. Read the lane tip with
  `jj-lane.sh state {{FLEET_ROOT}}/<{{LANE}}-repo>` (`local=`, `ahead=`) or
  `git rev-parse <branch>` — git HEAD is detached at `@-` and `@{u}` fails. Pathspec limits,
  exit 3 and conflict recovery: addendum §4.
- **Main-repo lanes (`repo = .`):** the fleet root is plain git and is never jj-colocated. Commit
  only your own paths through `{{FLEET_ROOT}}/scripts/hyaku/fleet-commit.sh` (never
  `git add -A`/`git commit -a`, and never run `jj` at the fleet root).
- **Push scope:** only the fleet repo remote and your own {{LANE}} lane remote. Domain
  source trees are **read-only** — upstream work is documented in the report, never pushed.
- **L0 side channel:** if you need an operator decision, append
  `<lane> | round-<N> | <question>` to `{{FLEET_ROOT}}/.ufo/l0-questions.md`, then commit that
  append through `fleet-commit.sh` (never `git commit` in the fleet root). Do not block the round
  on an answer; note the open question in the report and route around it.
```

### 3.2 `templates/round-prompt.md` — qualifying edits elsewhere

- Line 23: "command, and the branch commit it was measured against (`git rev-parse <branch>`,
  never `HEAD`); append the motivating evidence to LOG.md."
- Line 107: "**Landed changes** — every change tied to a LOG.md entry and to the helper-printed
  `pushed <hash>` that carries it."
- Line 110: "commit it was measured against (`git rev-parse <branch>`; in a jj lane `HEAD` is
  `@-`)."

### 3.3 `scripts/hyaku/lane-addendum.md` — line-level fixes

- Line 20: "lines: claims with verdicts, lane tip (`jj-lane.sh state` `local=` and the last
  `pushed <hash>`), report commit, wave sizes and seat-role mix, dead seats, open"
- Lines 24-25: "**Working directory:** your tools start at the fleet root, not the lane repo — run
  read-only lane commands as `git -C {{LANE_CWD}} …` / `cd {{LANE_CWD}} && …` and use absolute paths
  for every read/edit/write; every lane VCS write goes through the helper (§4)."
- Line 54: "… and commit them as wave evidence through the lane helper (§4)."
- Line 90-91 keeps its rule as is ("never run `jj` or any git write") — the new §4 is the only
  place an L1, not a seat, is given jj commands.

### 3.4 `scripts/hyaku/lane-addendum.md` — replace the misroot-sweep paragraph (§3, lines 110-115) with

```markdown
   **Misroot sweep before the report:** run `git -C {{FLEET_ROOT}} status --porcelain` (no
   pathspec — seat notes have landed as plain files at the fleet root). For every untracked file one
   of your seats wrote into the fleet root (check its content names your lane/round), copy it
   byte-exact into the same relative path under {{LANE_CWD}}, verify with `cmp`, then delete the
   fleet copy (the one fleet-root deletion you may make) and record the misroot under `## Mistakes`.
   Add the copied paths to your next helper commit (or commit them now, §4) — a copied file left
   unnamed stays `??` and is later reported as leftover round work. Confirm with
   `jj-lane.sh state {{LANE_CWD}}` that round work shows `ahead=0` before you write the report.
   Never touch files another lane's seats wrote, and never touch `.ufo/state/*` driver files.
```

### 3.5 `scripts/hyaku/lane-addendum.md` — replace §4 (lines 116-141) with

```markdown
4. **Commit order (landed = committed and pushed) — jj lane VCS** (operator 2026-10-20: "let's try
   to also implement using jj as git manager from now on on shokunin runs"). The lane repo is
   jj-colocated (jj 0.45.1; git stays the backend and the GitHub remote); the driver runs
   `jj-lane.sh init` at dispatch — never run `jj git init`/`--colocate` yourself, and never run
   `jj` in the fleet root or another lane. Commit ONLY through the lane helper, which tracks
   exactly the listed paths, commits under `{{LANE}}-shokunin <{{LANE}}@shokunin.local>`, moves the
   branch bookmark and pushes (recovering from an operator push by fetch + rebase of your unpushed
   commits only):

       {{FLEET_ROOT}}/scripts/hyaku/jj-lane.sh commit {{LANE_CWD}} --as {{LANE}} \
         -m "round-{{ROUND}}: <what>" -- <repo-relative path>...

   **Cite only the `pushed <hash>` line it prints.** `committed <hash>` is provisional: a
   push-recovery rebase rewrites the commit, so the `committed` hash is no longer an ancestor of
   the branch. If it prints `nothing to commit`, nothing was committed — its trailing
   `pushed <hash>` is a pre-existing tip; fix the paths instead of citing it. A named directory
   commits every tracked change and every new non-ignored file under it, like `git add <dir>` with
   one difference: **new files over 1 MiB stay out silently**, so name big files explicitly.
   Deletions of tracked paths are committed when the deleted path (or its directory) is named. A
   previously tracked ignored file rides a directory commit — untrack it first if it must not.

   **Exit 3 = committed, not pushed.** If the message is `local <branch> tip has unresolved
   conflicts`, the conflicted tip is unpushed; resolve it before retrying — take `local=` from
   `jj-lane.sh state`, run `jj new <local>`, edit the conflicted paths to the resolution, then
   `jj --ignore-immutable squash` (the lanes colocated on 2026-10-19 carry
   `immutable_heads() = builtin_immutable_heads() | ::bookmarks()` and the helper preserves it, so
   a plain `jj squash` refuses there; `--ignore-immutable` is harmless where the alias is absent —
   verified in a lane without it), and
   `jj-lane.sh push {{LANE_CWD}}`. Any other failure: rerun `jj-lane.sh push {{LANE_CWD}}`.
   Never `jj git push` yourself — jj's push is force-with-lease and would rewrite remote history
   after any lane-side rewrite. Never describe, squash, rebase, abandon or otherwise rewrite a
   commit already on `<branch>@origin`; the helper's recovery rebases only the unpushed ones.

   **Never** `git add`, `git commit`, `git stash`, `git checkout`, `git reset` or `git push` in the
   lane: jj resets the git index on every mutation, so staged entries are destroyed. Read-only git
   (log, show, diff, status, ls-files, rev-parse, merge-base) stays fine, but git HEAD is `@-` and
   may be detached: read the lane tip with
   `{{FLEET_ROOT}}/scripts/hyaku/jj-lane.sh state {{LANE_CWD}}` (`local=`, `ahead=`) or
   `git rev-parse <branch>`, never `@{u}` or `HEAD`. Any other jj call (yours only) carries
   `--ignore-working-copy` unless it must snapshot, and is limited to read-only inspection plus
   `jj restore -- <path>`, `jj file track/untrack`, and the conflict resolution above. Revert a
   tracked change with `jj restore -- <path>`; to drop scratch an earlier snapshot tracked, ignore
   it first (append its path to `.git/info/exclude`), then `jj file untrack -- <path>` — without
   the ignore rule the next snapshot re-adds it. **`.ufo/state/` is never committed** from a lane.
   A lane gate or selftest that runs git writes must run on a sandbox clone, never in the lane.

   Fleet-repo commits stay on git, only through the serialized helper, which pushes origin:

       {{FLEET_ROOT}}/scripts/hyaku/fleet-commit.sh --as {{LANE}} -m "round-{{ROUND}}: {{LANE}} report" \
         -- .ufo/reports/round-{{ROUND}}/{{LANE}}.md

   (also for an l0-questions append). The report lands last and cites the pushed lane hash. Before
   writing it, `jj-lane.sh state {{LANE_CWD}}` must show `ahead=0` and `git -C {{LANE_CWD}} status
   --porcelain` must show no tracked entries for round work.
```

### 3.6 `scripts/hyaku/lane-addendum.md` — replace §5 (lines 142-144) with

```markdown
5. **Inherited state.** In a jj lane "uncommitted" means changes in the working-copy commit `@`.
   Inspect them with `{{FLEET_ROOT}}/scripts/hyaku/jj-lane.sh state {{LANE_CWD}}` (pure git;
   `tracked=` counts modified entries) and `jj --ignore-working-copy diff --summary -r @` (the last
   snapshot; run `jj status` once — it snapshots, rewriting `@` and clearing the git index — if you
   need the current disk state). Resolve lane-authored leftovers under this round's entry: commit
   them through the helper (§4), revert tracked edits with `jj restore -- <path>`, and drop scratch
   an earlier snapshot tracked by ignoring it and then `jj file untrack -- <path>`. Remove untracked
   leftovers with `rm`; never `git checkout`/`git stash`. If `jj diff --summary -r @` shows `A`
   entries you did not author, untrack them before naming a directory — a named directory commits
   every tracked change under it. Name what you kept and what you discarded in the report. Files
   you did not author (operator sweeps, `round-*-aggregator-*`,
   `round-*-verifier-spotcheck.md`) → never edit; name them. Read
   `corpus/lessons/round-{{PREV}}-verifier-spotcheck.md` if it exists: it is the outside
   discernment check of your previous round — turn every disagreement or routed defect into a
   lesson-backed `QUALITY.md` criterion or fix, or say in the report why not. Also honor any
   `corpus/lessons/operator-*.md` teaching not yet reflected.
```

---

## 4. Recommendations

1. **Helper hardening (owner: orchestrator; I did not edit the helper):**
   - Pass `--config 'snapshot.auto-track="none()"'` on every snapshotting call (`jj diff`,
     `metaedit`, `commit`), or fail closed when the repo config lacks it. This closes B1 for
     pre-existing `.jj` lanes and for any skipped `init`.
   - Normalize before matching paths: strip a leading `./` and reject any path whose first
     component is `.ufo/state` (B6). Current guard is `case $p in .ufo/state/*)`.
   - On nothing-to-commit, print only `nothing to commit` (drop the trailing `pushed` line, or
     print `pushed <hash> (unchanged)`) so a lane cannot cite a stale tip (B5).
   - In `commit`, assert the remote bookmark is tracked and print the exact fix
     (`jj bookmark track <branch>@origin`) when it is not; the sandbox's un-initialized lane
     failed pushes with `Error: Non-tracking remote bookmark master@origin exists` (three attempts,
     ~6 s of sleeps, then exit 3).
   - Keep the recovery rebase scoped to `heads(<branch>@origin..bookmarks(<branch>))` (verified) and
     consider refusing `commit` when the working copy itself is conflicted.
2. **Driver (owner: orchestrator):** gate `lane_vcs_init` on `LANE_REPO != .` (`inline.sh:90,142`)
   so a main-repo lane can never colocate the fleet root (B9); re-render prompts for the six live
   rounds or steer them, because 0 of 190 rendered prompts carry the helper (C1); running
   `jj-lane.sh init` is idempotent and safe mid-round when `.jj` already exists, but the prompt
   should not ask a lane to create `.jj`.
3. **Prompt changes:** apply §3.1-3.2 (template) and §3.3-3.6 (addendum) together. The template
   must not use `{{LANE_CWD}}`; only the addendum may.
4. **Selftest additions (`jj-lane-selftest.sh`):** auto-track pollution (repo without `auto-track`),
   the `./.ufo/state/...` bypass, the `nothing to commit` output, the conflict-recovery recipe
   (`jj new` + edit + `--ignore-immutable squash` + push with the operator commit still an
   ancestor), and a rewrite-pushed-commit case proving jj force-with-lease (so the invariant is
   documented and guarded, not assumed).
5. **Text-level invariant to add to `closure-prompt.md` Step-1** (currently correct on branch
   ancestry, lines 22-27): explicitly check that every cited hash is on the branch (`merge-base
   --is-ancestor <hash> <branch>` already does it) and that the report cites no `committed` hash
   from a recovery; the closure's current form is sufficient, but the report contract should say
   so once.

---

## 5. Verification gaps (unrun checks have not passed)

- Did not run `scripts/hyaku/jj-lane-selftest.sh`: it clones the live `kake-shokunin` and the wave
  rule forbids executing fleet scripts that resolve to live paths. Its cases were read and are
  cited as author claims, not as my evidence.
- Did not inspect live lanes with jj (`jj log`, `jj bookmark list`, `jj status`) — forbidden. So
  whether mado/tameshi's `master@origin` is tracked, and whether `@` already carries auto-tracked
  paths, is unknown; their `git status` showed no ` A` entries at read time (mado) but a running
  lane's tree changes.
- The "old prompt + detached HEAD → `git push` fails" chain is [INFERENCE] from the measured
  `@{u}` failure and git semantics; I did not run a git commit on a detached HEAD in a colocated
  repo.
- Conflict recovery verified for a same-hunk text conflict only; delete/modify, rename, and
  directory conflicts were not exercised, and `jj resolve` tooling was not used.
- Live figures (mado `ahead=8`, four `??` paths, tameshi status) are snapshots taken while lanes
  were running.

---

## 6. Sandbox and tooling

- Kept `/fast/scratch/jj-wave/JjAuditPromptText` because it preserves cited failures: `lane5`
  (auto-track pollution + non-tracking-bookmark push failure), `lane2` + `remote2.git`
  (force-with-lease rewrite of a pushed commit), `lane` (index reset, `.ufo/state` bypass, big-file
  skip). All other directories are disposable.
- No tool installs or upgrades were performed; jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`
  was already present at `~/.local/bin/jj`.
