# JjCriticProtocol — protocol attack on jj colocation + `jj-lane.sh`

Seat: JjCriticProtocol-2 (critic, leaf). Date: 2026-10-20. jj 0.45.1 (`~/.local/bin/jj --version` →
`jj 0.45.1-7c41cdeb…`). Helper under test: `scripts/hyaku/jj-lane.sh` sha256 `2479041653c6…dc2b1d`.
I ran a byte-identical copy of the helper from the sandbox, with `HYAKU_STATE=<sandbox>/state` so its
lock file and push-error file never touch live state. No jj command ran in or against
`/home/vgpnk/Projects/shokunin`. Live repos got read-only git, `cat` and `grep` only. Every push went
to a sandbox bare repo (`git remote -v` → `origin /fast/scratch/jj-wave/JjCriticProtocol/e1/remote.git`).
No tools were installed.

Protocol clauses attacked (PROTOCOL.md):
- L117–137: lands last; landed means committed; cited hash is HEAD and an ancestor; no amend; LOG.md
  corrections by append; report carries the lane identity.
- L230–239: closure step 1.
- L431 and L463: LOG.md is append-only.
- L493–499: lane identity.
- Wave invariants: landed = committed AND pushed; commits are pathspec-limited; `.ufo/state/` is never
  committed.

Reproduction harness (the sandbox was removed; this recreates every case):

```bash
SB=/fast/scratch/jj-wave/JjCriticProtocol; export HYAKU_STATE=$SB/state JJ_BIN=$HOME/.local/bin/jj
H=$SB/jj-lane.sh; JJ=$JJ_BIN   # H = cp of scripts/hyaku/jj-lane.sh
mk() { local n=$1; rm -rf $SB/$n; mkdir -p $SB/$n; git init -q --bare -b master $SB/$n/remote.git
  git clone -q $SB/$n/remote.git $SB/$n/seed
  ( cd $SB/$n/seed && git config user.name seed && git config user.email s@x \
    && printf '# LOG\n\n## r1\nentry one\n' > LOG.md && mkdir -p .ufo/state corpus \
    && echo tick > .ufo/state/lane.round && echo k > corpus/a.md \
    && git add -A && git commit -qm seed && git push -q origin master )
  git clone -q $SB/$n/remote.git $SB/$n/lane; git clone -q $SB/$n/remote.git $SB/$n/op
  git -C $SB/$n/op config user.name operator; git -C $SB/$n/op config user.email op@x; }
oppush() { ( cd $SB/$1/op && git pull -q --rebase origin master && printf '%s\n' "$3" >> "$2" \
  && git add "$2" && git commit -qm "operator: $2" && git push -q origin master ); }
# every case: mk eN; L=$SB/eN/lane; $H init $L kotoba
```

## Findings (observed)

### F1 — The "committed" hash is rewritten whenever the push needs recovery. A lane can cite a hash its branch does not contain (cited-hash ancestry, landed)

```
mk e2; $H init …; oppush e2 OP.md "operator line"; echo "lane work" > $L/corpus/w.md
$H commit $L --as kotoba -m "round-9: work" -- corpus/w.md
committed 3e98333cb4d48abd510be59b1583150389908a35
pushed aaf4ab1146124cb40e9febf8ef1138df8017f55e
committed==pushed? NO
C NOT ancestor of master (orphaned citation)
C NOT ancestor of HEAD
git cat-file -t $C → commit        # kept alive by refs/jj/keep/3e98333…
```

- On any rejected push, the helper prints two different hashes, and the first is orphaned at once.
- `git cat-file` still finds the orphan through `refs/jj/keep/*`, so an existence-only check passes.
- Selftest g (`fetch-rebase-recovery`) never asserts that committed ≠ pushed.

### F2 — The `inline.sh verify` durability push orphans a hash *after* the report has landed (lands last, ancestry)

```
mk e11; init; mv remote.git remote.off; commit … → committed 5d5174a8…; jj-lane: push failed after 3 attempts … (exit 3)
mv remote.off remote.git; oppush e11 OP.md …; $H push $L        # = inline.sh:119 durability push
pushed 1e65f3b5175d3d086cadaafc1b47c32e28237c9f
C NOT ancestor of master: cited hash orphaned AFTER report landed
git -C remote.git cat-file -t $C → fatal: could not get object info
```

After an exit 3, `git rev-parse HEAD` = C. The canonical check (`is-ancestor C HEAD`) passes when
the report is written. Then `inline.sh verify` runs in this order:

1. sweep or accept the report (L111–116);
2. `jjl push` (L117–121), which rebases C into a new hash;
3. print `PUSHED lane repo` with no warning.

The lane takes a defect the driver caused. A fresh clone of the real remote never contains C.

### F3 — If a commit is stranded, a rerun of the helper reports `pushed <stale tip>` with rc=0, and every closure check passes (landed means committed AND pushed)

The case reproduces the helper's own sequence and stops between `jj commit` and `bookmark set`, the
window a SIGTERM or tool timeout can hit. The lane then retries the identical command:

```
nothing to commit
pushed abe5af640709b722594ed26d3de66b38b46f503a        # == old remote tip
rc=0
state branch=master local=abe5af64… remote=abe5af64… ahead=0 behind=0 head=detached tracked=0 untracked=0
HEAD: cf95c09 [round-9: work]   HEAD (the real work) NOT in master/remote
```

- The closure-prompt checks all pass: cited hash ancestor of `<branch>`, `ahead=0`, and empty
  `status --porcelain`.
- The canonical `is-ancestor <hash> HEAD` also passes.
- The work was never pushed.
- Guard probe that catches it: `git rev-list --count refs/remotes/origin/master..HEAD` → `1`. The jj
  form `jj --ignore-working-copy log -r 'master..@-'` → `cf95c09d96ec round-9: work`.

### F4 — The helper's fileset parsing drops real paths silently and still prints `pushed <stale>` rc=0 (landed, pathspec)

```
mk e17; for f in "corpus/my notes.md" "corpus/a~b.md" "corpus/x|y.md" "corpus/all().md" "corpus/q'uote.md"; do … done
[corpus/my notes.md] rc=0 :: committed 9a90a614… pushed 9a90a614…
[corpus/a~b.md]      rc=0 :: pushed 9a90a614…                 # file NOT committed
[corpus/x|y.md]      rc=0 :: pushed 9a90a614…                 # file NOT committed
[corpus/all().md]    rc=1 :: jj-lane: jj file track failed
git status --porcelain → ?? corpus/a~b.md  ?? corpus/x|y.md …
```

- The helper passes bare paths to `jj file track` and `jj commit`, and jj parses them as **fileset
  expressions**: `a~b.md` means "a minus b.md". The path matches nothing and jj raises no error.
- The helper's `*?[` filter does not cover `~ | & ( ) ' "`.
- Live exposure today: no lane has tracked paths with `~|&()'"*?[`. souji-shokunin has 2 paths with
  embedded newlines (`tests/vault/vadv54-run/r/nl/first\nsecond.md`). The defect is latent.

### F5 — The pathspec and `.ufo/state` guards are bypassable (pathspec-limited, `.ufo/state` never committed)

```
mk e1; init; echo tick2 > .ufo/state/lane.round; echo new > corpus/b.md
-- .ufo/state/lane.round   → "driver runtime is never committed by a lane" (64)   # guarded
-- .ufo/state              → committed ef8978c… pushed; stat: .ufo/state/lane.round | 2 +-
-- ./.ufo/state/lane.round → committed 604d27f… pushed; stat: .ufo/state/lane.round | 2 +-
-- ./                      → committed fb80f6a… pushed; stat: .ufo/state/lane.round | 2 +-, corpus/b.md | 1 +
```

- `.` is rejected, but `./` commits the whole repo and tracks untracked files (`corpus/b.md`).
- Live exposure: no lane repo has a `.ufo/state` (scan of `*-shokunin`: none). It is tracked in the
  fleet root (`.ufo/state/.gitkeep`, `aggregator.mission`, …). The state bypass becomes live if the
  fleet-root trial moves the fleet root onto this helper.
- `./` is live for every lane.

### F6 — A native jj commit by any seat goes into the next helper push with the operator author, unlimited pathspec and a half-written LOG.md (identity, pathspec, LOG.md)

```
mk e4b; init; printf 'HALF-WRITTEN entry, not for commit\n' >> LOG.md
(cd $L && jj commit -m "wip checkpoint")            # any seat; the addendum permits jj calls that "must snapshot"
echo "lane work" > corpus/w.md; $H commit $L --as kotoba -m "round-9: work" -- corpus/w.md  → rc=0, pushed dd9e7d2…
remote: dd9e7d2 an=kotoba-shokunin [round-9: work]  corpus/w.md
        ce36ee0 an=Joao Pedro Veiga cn=kotoba-shokunin [wip checkpoint]  LOG.md | 1 +
```

- The operator author comes from the post-init `@`. jj creates it under the global
  `~/.config/jj/config.toml` `[user] name = "Joao Pedro Veiga"` before init writes the repo
  identity. Init itself warns: `The author of the working copy will stay "Joao Pedro Veiga"`.
- The closure checks all pass: `ahead=0` and clean status, because the half-written edit now lives in
  a commit.
- jj blocks one variant: a bare `jj new` gives an undescribed commit, and push refuses it with
  `Won't push commit 78dbe91a3f4c since it has no description` (exit 3, lane stuck).
- `git log --all` in a colocated lane also lists snapshot commits authored `Joao Pedro Veiga` (e2:
  `4dd8095`, `ce0de50`, `eb5a0bb`) through `refs/jj/keep/*`. No gate under `scripts/` or `.ufo/gates/`
  uses `--all` today (grep: none).

### F7 — A git commit on the detached HEAD passes the canonical PROTOCOL check, and `git push` says up-to-date (cited-hash ancestry, duplicate authority)

```
mk e5; init; helper commit (HEAD now detached)
git add corpus/g.md && git -c user.name=kotoba-shokunin … commit -qm "round-9: git habit" -- corpus/g.md
git push origin master → Everything up-to-date (rc 0)
PROTOCOL.md check (vs HEAD): PASS
closure-prompt check (vs branch): FAIL
remote cat-file → fatal; state … ahead=0 … tracked=0 untracked=0
```

- PROTOCOL.md:119–121 (and the canonical `kimi-shokunin/…/PROTOCOL.md:121–123`) still define the
  cited hash as `HEAD` and the check as `is-ancestor <hash> HEAD`. Step 1 (L230–231) says "ancestor
  of the lane repo's HEAD".
- `closure-prompt.md:22` silently overrides this with `<branch>`, yet tells the closure seat to
  "Load … PROTOCOL.md (§Round-robin closure steps 1 and 4)".
- So two authorities disagree. Read literally, the protocol passes F3 and F7.
- `templates/round-prompt.md:133` still says only "commit … inside your lane repo, then push" (git
  habit). The jj-only rule lives only in the appended addendum.

### F8 — A silent push recovery rewrites working-tree files under live seats. A stale-buffer write then deletes an appended LOG.md entry, rc=0 (LOG.md append-only)

```
mk e18; init; cp LOG.md seatA-buffer                   # seat A has LOG.md loaded
oppush e18 LOG.md "## 2026-10-20 operator erratum: r1 claim superseded"
seat B: $H commit … -- corpus/w.md → pushed 2f664902…  # rejected → fetch → rebase of @ → working LOG.md rewritten
seat A: { cat seatA-buffer; printf '\n## r2\nlane entry two\n'; } > LOG.md; $H commit … -- LOG.md → pushed 8ca300de…, rc=0
pushed diff:  entry one
             -## 2026-10-20 operator erratum: r1 claim superseded
             +## r2
```

[INFERENCE] With git, a dirty tree blocks `pull --rebase`, and a later push turns this into a LOG.md
conflict. jj converts it into a silent deletion of an append-only entry.

Variant (e7): when seat A's LOG.md draft is uncommitted at the moment seat B's commit triggers
recovery, the push succeeds (rc=0). Seat A's working LOG.md is rewritten in place with
`<<<<<<< conflict 1 of 1 … %%%%%%% … >>>>>>>`. Seat A then appends with `>>` and commits LOG.md, and
the helper refuses: `local master tip has unresolved conflicts`, rc=3.

### F9 — The helper's own rebase creates a LOG.md conflict whose prescribed remedy cannot succeed (landed)

```
mk e6; init; oppush e6 LOG.md "## operator erratum (appended)"; printf '\n## r2\nlane entry two\n' >> LOG.md
$H commit … -- LOG.md → committed 5d62f72c…; jj-lane: local master tip has unresolved conflicts — resolve in the lane, then retry
C NOT anc HEAD; working LOG.md has conflict markers; git HEAD tree has .jjconflict-base-0/…, JJ-CONFLICT-README;
git status: D  .jjconflict-… (10 staged deletions) + UU LOG.md; state … ahead=1 … tracked=11
resolve LOG.md by hand → $H commit … -- LOG.md → committed 7746f89e…, rc=3
jj-push.err: Error: Won't push commit 0255fd40a0eb since it has conflicts
```

- The helper's guard checks only `heads(bookmarks(BRANCH)) & conflicts()`, not the ancestors.
- jj itself refuses the conflicted ancestor, so nothing bad ships.
- The lane cannot land, though. The fix needs a native `jj squash`, plus `--ignore-immutable` on
  tameshi and mado, whose live repo config has `"immutable_heads()" = "builtin_immutable_heads() | ::bookmarks()"`.
- Every round appends LOG.md, so this is the most likely conflict shape.

### F10 — The push-recovery rebase changes the committer from `--as` to the init identity (lane identity attribution)

```
mk e10; init kotoba; oppush …; $H commit $L --as protocol -m "round-9 verifier spot-check" -- corpus/lessons/…
8fc00ef author=protocol-shokunin <protocol@shokunin.local> committer=kotoba-shokunin <kotoba@shokunin.local>
control (no rebase): aa2524c author=protocol-shokunin committer=protocol-shokunin
```

- `do_push`'s rebase carries no `--config user.*`.
- The helper header promises "author AND committer are <id>-shokunin". Selftest d2 tests only the
  no-rebase path.
- If the repo identity is ever absent, the committer becomes the global operator identity.

### F11 — The lane branch flips once HEAD detaches (helper invariant, landed)

```
mk e13; git checkout -qb feature-x; git push origin feature-x; $H init $L kotoba → state branch=feature-x … head=attached
commit one → pushed 538291c (feature-x); commit two → no "pushed"
jj-push.err: Error: Non-tracking remote bookmark master@origin exists
state branch=master local=6dc3a27… ahead=2 … head=detached;  trunk() = feature-x@origin
```

- `detect_branch` prefers the attached HEAD. After the first jj mutation HEAD is detached, and the
  function falls back to `origin/HEAD`.
- The second commit stacked feature-x work onto `master` locally, and the lane got stuck at exit 3.
- Live exposure: every lane is attached to its default branch today. audio-shokunin (`wt-r90…100`)
  and game-dev-2d (`wt-r98…100`, locked git worktrees) carry extra local branches.

### F12 — `jj undo` desynchronizes the local refs that closure trusts (false closure failures)

```
mk e15; init; commit → pushed P=336dff1e…; (cd $L && jj undo) → state … remote=8107e849 ahead=1   # remote really has P
jj undo; jj undo → state … local=8107e849 remote=8107e849 ahead=0 tracked=1;  " A corpus/w.md"
closure check (P anc <branch>): FAIL though P is on the real remote
```

`ahead=` and the ancestry check both read the jj-exported local refs, never the real remote.

### F13 — The recovery re-pushes a rewritten copy of an already-cited commit after a remote rewrite (no-rewrite claim)

```
mk e16; init; commit → cited P=c05b6e68; operator: reset --hard HEAD~1, commit, push -f
$H commit … -- corpus/n.md → committed 64bfa133… pushed fcb99825…
remote: fcb9982 [round-10: next] / 2e90d37 [round-9: work (cited)] / 8440862 [operator: rewrite] / seed
```

- The cited commit came back under a new hash with no signal to the lane.
- `--ignore-immutable` plus `rebase -b` covers everything in `new_origin..tip`, which includes
  previously pushed commits whenever the remote stops being a fast-forward of its old position.

### F14 — Directory commits silently leave new files over 1 MiB behind (landed, partial)

```
mk e9; corpus/knowledge/{note.md, dataset.csv (1,621,053 B)}; $H commit … -- corpus/knowledge → rc=0 pushed 478584a3
pushed tree: corpus/knowledge/note.md only;  status: ?? corpus/knowledge/dataset.csv
```

- The `jj file track` stderr for directories is sent to `/dev/null`.
- The addendum documents "name big files explicitly", but the helper says nothing when it drops one.

### Falsified hypotheses (they held)

- **`bookmarks(master)` substring capture:** 0.45.1 matches exactly (`bookmarks(master)` →
  `master` only; `substring:master` adds `old-master`).
- **Concurrent unlocked `jj st` versus 15 helper commits (40 s loop):** fails=0, no `divergent()`, no
  conflicted bookmark, 15/15 commits landed, 0 drafts of the dirty `LOG.md` pushed. The op log showed
  `27 reconcile divergent operations`.
- **`cp -a` of a colocated lane sharing the jj repo config through `config-id`:** jj 0.45.1 re-keys
  the copy (`851408910c31` → `5d5a239e5efa`). Running `init copy tabi` left the original at
  `kotoba-shokunin`.
- **Seats in git worktrees:** the helper refuses (`.git` is a file), and jj errors with
  `There is no jj repo in "."`. Nothing was written.
- **Spaces in paths:** these work (`corpus/my notes.md` committed).

## Inference

- [INFERENCE] F1, F2, F3 and F4 share one cause. The helper's stdout carries no single,
  post-verified landing token. `committed X`, `pushed Y` and `nothing to commit`+`pushed <tip>` all
  look like citable hashes. Lanes under time pressure will cite whichever they saw first.
- [INFERENCE] F3, F6 and F7 together show that `jj-lane state` (`ahead`, `tracked`, `untracked`) plus
  `is-ancestor <hash> <branch>` cannot certify "landed". In colocated mode, work can sit in a commit
  at or below `@` that is neither in the working tree diff nor on the branch. The missing probe is
  "HEAD (= `@-`) is contained in the real remote branch".
- [INFERENCE] F8 is the largest regression against git. Under git, a lane's working tree changes only
  when the lane acts. Under jj, any seat's helper commit that needs recovery rebases `@` and rewrites
  shared working files under every other seat mid-round. That is the "heavy swarming" condition the
  operator asked for.
- [INFERENCE] The lanes are not at fault in F2, F9 and F13; driver or helper behavior causes them.
  Under closure-prompt rules they would still be recorded as lane conformance defects. That is false
  provenance in the closure record.

## Recommendations (smallest safe corrections, each guard checked against its counterexample)

1. **Single landing token (F1, F2, F3, F4).**
   - `commit` and `push` print exactly one citable line, `landed <hash>`, and only after
     `git ls-remote origin refs/heads/<branch>` returns a hash that has `<hash>` as an ancestor.
   - On recovery, print `rewritten <old> -> <new>`.
   - `nothing to commit` prints no hash and exits non-zero when `git status --porcelain -- <paths>` is
     non-empty.
   - Update the addendum and the closure prompt: "cite only `landed <hash>`".
2. **Stranded-commit preflight (F3, F6, F7).** Before committing, the helper refuses when
   `bookmarks(exact:<branch>)..@-` is non-empty, or equivalently
   `git rev-list --count refs/remotes/origin/<branch>..HEAD` ≠ 0 (verified: e3 → 1, e5 → 1). It
   lists those commits with their authors instead of sweeping them in. This replaces selftest i's
   "import and push" behavior, which is the F6 carrier.
3. **Fileset-literal paths (F4, F5).**
   - Pass every path as `root-file:"<escaped>"` (or `file:`) to `jj file track` and `jj commit`.
   - Normalize with `realpath -m --relative-to=. -- "$p"` before the guards.
   - Reject `.`, `./`, the empty path, the repo root and any path whose normalized form equals or
     contains `.ufo/state` or `.ufo/watchdog.log` (as itself or as an ancestor directory).
   - After the commit, assert that `git status --porcelain -- <paths>` is empty (this also catches
     F14).
4. **Append-only guard (F8).** For `LOG.md`, `corpus/SOURCES.md` and other declared append-only
   files in the commit, refuse unless the `<branch>@origin` blob is a byte prefix of the new blob
   (verified: e18 → "NOT a byte prefix → refuse").
5. **No silent working-copy rebase (F8, F9).**
   - Any rebase that moves `@` rewrites the shared working tree, whether it uses `-b`, or `-r` plus
     descendant re-parenting. So before recovering, compute the files the incoming remote commits
     touch: `git diff --name-only <old origin> <new origin>`.
   - If that set intersects the uncommitted changes in `@` (`jj diff -r @ --name-only`, or
     `git status --porcelain`), refuse with exit 3 and name the files. Do not rebase into a seat's
     working files.
   - [INFERENCE, untested] A `--ignore-working-copy` recovery only defers the rewrite: the next
     snapshotting command reports a stale working copy, and `workspace update-stale` rewrites the
     files anyway.
   - Refuse and `jj op restore` to the pre-rebase operation if any rebased commit is conflicted.
   - The documented remedy must be something the helper can complete.
6. **Non-fast-forward refusal (F13).** Record `<branch>@origin` before the fetch. If the old value is
   not an ancestor of the new one, abort with `remote rewritten` and never rebase.
7. **Committer identity (F10).** Pass the same `--config user.name/email` from `--as` to every
   mutating jj call in `do_push`: rebase, bookmark set and push.
8. **Branch pinning (F11).**
   - `init` writes the branch once to repo config, e.g. a `shokunin.branch` key or the `trunk()`
     alias it already sets. Every later call reads it from there instead of calling `detect_branch`.
   - `init` refuses when an attached HEAD differs from `origin/HEAD`.
   - `init` also stamps the post-init `@` with `jj metaedit --update-author` under the lane identity
     (F6 carrier).
9. **Single authority for step 1 (F7, F12).** Amend PROTOCOL.md L119–121 and L230–231 so that a
   colocated lane's cited hash is checked with
   `git merge-base --is-ancestor <hash> $(git ls-remote origin refs/heads/<branch> | cut -f1)`, plus
   `git rev-list --count origin/<branch>..HEAD == 0`, never `HEAD` or local refs alone. PROTOCOL.md is
   protocol-lane owned, so the integrator names this amendment and the closure prompt cites it.
   Closure also audits `git log --format='%an %ae %cn %ce' BASE..origin/<branch>` against
   `{lane, protocol}`.
10. **Driver order (F2).** In `inline.sh verify`, push the lane *before* accepting or sweeping the
    report. If the push rewrote anything, record it as a driver-caused orphan in the closure notes,
    not a lane defect.
11. **Addendum (F6, F12).** Replace "any other jj call … unless it must snapshot" with an explicit
    allow-list: the helper, `jj restore -- <path>`, and read-only calls with `--ignore-working-copy`.
    Forbid `jj commit/new/describe/squash/undo/op restore/edit/abandon` in lanes.
12. **Selftest additions.** Assert committed == landed or an explicit `rewritten` line (F1); add cases
    for e3, e4b, e17, e18 and e10-with-rebase.

Tradeoff for the canonical judge: recommendation 2 deliberately breaks selftest i ("plain git commit
imported by next helper commit"). That sweep is the mechanism behind F6 and F7, so a direct git or
native jj commit should block the helper rather than ship silently.

Sandbox: `/fast/scratch/jj-wave/JjCriticProtocol` removed after this report. Every case reproduces from
the harness above.
