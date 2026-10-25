# JjSentinelHelper — safety audit of scripts/hyaku/jj-lane.sh (jj 0.45.1)

Seat: JjSentinelHelper-2 (UFO-FSD sentinel, leaf). Audit only; the helper was not edited.
Audited file: `scripts/hyaku/jj-lane.sh`, sha256 `2479041653c6a77c6cca099a37948d6c16361173c68fb14c8c2e2feae9dc2b1d`.
Before running it, I copied it byte-for-byte into the sandbox (`/fast/scratch/jj-wave/JjSentinelHelper/jj-lane.sh`, same sha256).
Every repro ran inside that sandbox with these settings:
- `HYAKU_STATE=<sandbox>/state` and `JJ_BIN=~/.local/bin/jj` (`jj 0.45.1-7c41cdeb`);
- `origin` pointed at a sandbox bare repo, checked by `mk()` against the sandbox prefix;
- the user's real `~/.config/jj/config.toml` in effect (`git.auto-local-bookmark = true`, global `user.name = "Joao Pedro Veiga"`).

No jj command ran in or against /home/vgpnk/Projects/shokunin. Live access was limited to reads: `git -C <lane> symbolic-ref|check-ignore|for-each-ref` and `cat` of the live `.jj/repo/config-id` files plus the matching `~/.config/jj/repos/<id>/config.toml`.
No tools were installed.

Harness (`lib.sh`, sandbox): `mk <name> [branch]` builds `origin.git` (bare), a seed commit on `main`, and a lane clone `$L`.
`remote_log` runs `git log` on the bare origin.

## Findings (observed)

| # | Severity | Question | Result |
|---|---|---|---|
| F1 | **Critical** | force-push / rewrite a pushed or cited commit | **Yes.** `push` and `commit` ship backwards and sideways (non-fast-forward) moves of the branch. |
| F2 | **High** | push a bookmark other than the lane branch | **Yes.** Once HEAD detaches, the branch is re-resolved from `origin/HEAD`, so lane work is pushed onto `main`. |
| F3 | **High** | sweep scratch or `.ufo/state` into a commit | **Yes.** The `./`, `.ufo`, `.ufo/state` and `./.ufo/state/<f>` spellings bypass the guard. |
| F4 | Medium | wrong repo or cwd confusion | **Yes (locking).** The lock key is `basename`, so `.` and the absolute spelling use different locks. The push-error file is shared by every lane. |
| F5 | Medium | rewrite a cited commit; lane identity | The printed `committed <h>` is rewritten on retry and never lands. The retry committer is the repo identity, not the `--as` identity. |
| F6 | Medium | rewrite a pushed commit | After an external force-push of origin, the helper rebases a previously pushed (cited) commit and silently re-lands it. Exit is 0. |
| F7 | Low | fabricated landing evidence | `nothing to commit` is followed by `pushed <existing tip>` and exit 0. |
| F8 | Low | lane identity | `--as` is not bound to the lane dir; any `[a-z0-9-]` id is accepted. |
| F9 | Info | init robustness | `bookmark track` failure is swallowed (line 163). Later pushes fail closed. |
| — | holds | push `@` / other bookmarks / `--force` | Never. Six origins hold only `refs/heads/main` (and `work`, created deliberately in F2). No force flag exists. |

### F1 — Critical: the helper force-pushes non-fast-forward branch moves (lines 100–132, push at 109)

`jj git push` behaves like a lease push (`--force-with-lease`), not git's default fast-forward-only push.
`do_push` calls it first (line 109), and nothing checks beforehand that `<branch>@origin` is an ancestor of the local `<branch>`.
So any local ref move of the lane branch is pushed as-is, rewriting the remote:
- `git branch -f` / `git reset` / `git commit --amend` by a gate, an operator tool, or an L1 that breaks lane-addendum.md:128-130;
- `jj bookmark set --allow-backwards`.

When jj imports the moved ref, it also abandons the dropped commit locally.

Repro (sandbox):
```
. ./lib.sh; mk back; cd $L; $H init $L back
echo a >> LOG.md; $H commit $L --as back -m A -- LOG.md
echo b >> LOG.md; $H commit $L --as back -m B -- LOG.md      # pushed edbe632 (cite-able)
git -C $L branch -f main main~1                               # backwards move
$H push $L; echo rc=$?; remote_log back
T=$(git -C $L commit-tree 'main^{tree}' -p main~1 -m A-amended); git -C $L branch -f main $T   # sideways
$H push $L; echo rc=$?; remote_log back
```
Excerpt:
```
edbe632 back-shokunin|back-shokunin B          <- remote before
pushed 498d24eb664823a3006c7d7bd8c7375f0bae821a
rc=0
498d24e back-shokunin|back-shokunin A          <- B (cited) erased from origin main
pushed 4110b1f1478651655ad20fd407d1b43d58d67038
rc=0
4110b1f seed|seed A-amended                    <- A (cited) replaced; wrong identity on remote
964a5ae seed|seed seed
```
jj names the move itself (`jj git push --dry-run` after the same `git branch -f`):
```
Abandoned 1 commits that are no longer reachable.
Changes to push to origin:
  bookmark: main [move backward from 4110b1f14786 to 964a5aeaa693]
```
Impact:
- breaks "a cited hash stays an ancestor of the branch" and "pushed commits are never rewritten";
- breaks lane identity (the `seed|seed` commit landed through the helper);
- contradicts the helper's own header (lines 20–23, "the push is never forced") and lane-addendum.md:127 ("never force").

A plain `git push` would have rejected both moves.

### F2 — High: after HEAD detaches, the helper resolves and pushes the `origin/HEAD` branch (lines 53–65; used at 141/189/249; bookmark set 233; push 109)

`detect_branch` uses the attached HEAD branch only while HEAD is attached.
After the first jj mutation HEAD is detached (wave context; observed `detached` below), so later calls fall to `refs/remotes/origin/HEAD` (line 57).
For a lane on any branch other than the default branch:
- the second commit moves `main` forward onto the lane commit (a fast-forward, so the sideways guard at line 233 does not fire);
- it then pushes `main`.

Repro (sandbox; lane on `work`, origin/HEAD → `main`; `main@origin` tracked):
```
. ./lib.sh; mk wrongbr2 work; cd $L; $H init $L wb
echo w1 >> LOG.md; $H commit $L --as wb -m W1 -- LOG.md          # pushes work
jj --ignore-working-copy bookmark track main --remote origin   # any prior tracking of main@origin
echo w2 >> LOG.md; $H commit $L --as wb -m W2-lane-work -- LOG.md
remote_log wrongbr2 main; remote_log wrongbr2 work
```
Excerpt:
```
--- origin main:
3fc8fcc wb-shokunin|wb-shokunin W2-lane-work      <- lane work landed on main
a0e117f wb-shokunin|wb-shokunin W1
--- origin work:
a0e117f wb-shokunin|wb-shokunin W1
```
Without the explicit track, the same flow still moved local `main` and stopped only by accident:
`push failed after 3 attempts: Error: Non-tracking remote bookmark main@origin exists`, rc=3 (run `wrongbr`).
`init` had also set `trunk()` to `work@origin`, which did not exist:
`Warning: Failed to resolve revset-aliases.trunk(): Revision work@origin doesn't exist … temporarily set to root()`.

Live exposure: the survey found all 21 lanes with HEAD branch == origin/HEAD, which makes this latent today.
```
for d in *-shokunin; do … git -C $d symbolic-ref -q --short HEAD; git -C $d symbolic-ref -q --short refs/remotes/origin/HEAD …
audio-shokunin head=main origin/HEAD=origin/main … branches=main,wt-r100,…,wt-r99,
chousa-shokunin head=master origin/HEAD=origin/master …   (all 21 equal)
```

### F3 — High: the path guard is spelling-based, and four spellings sweep `.ufo/state` / seat scratch (lines 180–185, track 209–216, commit 228–230)

The guard rejects only `/*`, `*..*`, exactly `.`, the literal prefix `.ufo/state/*`, `.ufo/watchdog.log`, and glob characters.
It does not catch:
- `./` (the whole repo);
- `.ufo` or `.ufo/state` (directories, tracked like `git add <dir>`);
- `./.ufo/state/<file>` (a file, tracked with `--include-ignored`).

Repro (sandbox; `.ufo/state/run.json`, `scratch/seat.tmp`, `.ufo/notes.md` untracked, `README.md` modified):
```
for v in dotslash ufodir ufostate dotstatefile; do mk sw$v; cd $L; $H init $L sw
  mkdir -p .ufo/state scratch; echo '{"secret":1}' > .ufo/state/run.json; echo junk > scratch/seat.tmp; echo x >> README.md; echo note > .ufo/notes.md
  P=<./ | .ufo | .ufo/state | ./.ufo/state/run.json>; $H commit $L --as sw -m $v -- "$P"
  git -C $S/sw$v/origin.git show --stat main; done
```
Excerpt (all four were pushed, rc=0):
```
=== dotslash path=./           -> .ufo/notes.md | .ufo/state/run.json | README.md | scratch/seat.tmp   (4 files)
=== ufodir path=.ufo           -> .ufo/notes.md | .ufo/state/run.json
=== ufostate path=.ufo/state   -> .ufo/state/run.json
=== dotstatefile path=./.ufo/state/run.json -> .ufo/state/run.json
```
Live exposure: `.ufo/state` is **not** git-ignored in 20 of 21 lanes; only kotodama ignores it.
```
git -C $d check-ignore -q .ufo/state/x.json → audio … NOT-ign; … kotodama-shokunin … state=ign; … (20× NOT-ign)
```
lane-addendum.md:127-128 tells L1s that a named directory keeps "ignored content" out.
That assurance does not cover `.ufo/state`, which is not ignored.
`./` also breaks the "never everything" rule in the helper header (line 17).

### F4 — Medium: the lock key is not canonical; push errors are shared across lanes (lines 84–90, 109, 130)

`take_lock` keys the lock on `basename "$dir"` (line 86).
- `commit .` (from inside the lane) locks `jj-..lock`.
- `commit /abs/lane` locks `jj-<lane>.lock`.

Two such calls on the same repo therefore do not exclude each other. All lanes invoked as `.` also share one lock.

Repro (sandbox):
```
. ./lib.sh; mk lockspell; cd $L; $H init $L lk
(flock $HYAKU_STATE/jj-Llockspell.lock sleep 20) & sleep 1
echo x >> LOG.md; timeout 15 $H commit . --as lk -m via-dot -- LOG.md
```
Excerpt: `pushed 2aebd2af…  rc=0 waited=0s`, and a new `jj-..lock` appeared in the state dir.

Line 109 writes `$STATE/jj-push.err`, a single file for every lane, while holding only that lane's lock.
Line 130 reads it back into the failure message.
I did not run two concurrent failing lanes, so [INFERENCE] concurrent failures can report a sibling lane's push error.

Relative-path handling is otherwise consistent:
- `$dir` is resolved against the caller's cwd before `cd` (lines 140/188/248);
- pathspecs are lane-root-relative, and absolute and `..` paths are refused;
- `jj` runs after `cd "$dir"` with `$dir/.jj` checked first.

### F5 — Medium: the retry path rewrites the printed `committed` hash and drops the `--as` committer (lines 231–235, 121)

Repro (sandbox; a second clone pushes first, then a closure-style commit runs):
```
. ./lib.sh; mk race; cd $L; $H init $L race
git clone -q $S/race/origin.git $S/race/other; …commit OTHER.md…; git -C $S/race/other push -q origin main
echo mine >> LOG.md; $H commit $L --as protocol -m closure-commit -- LOG.md
git -C $S/race/origin.git log -1 --format='author=%an <%ae> committer=%cn <%ce>' main
```
Excerpt:
```
committed e361425b95eaa68ec58313b824b9dc426f3a3d5c      <- never reaches origin
pushed d6c07cfdb6d1accd105a43c017165c51aaa5bacc
d6c07cf protocol-shokunin|race-shokunin closure-commit
author=protocol-shokunin <protocol@shokunin.local> committer=race-shokunin <race@shokunin.local>
```
- A reader that cites `committed <h>` cites a hash that is not an ancestor of the branch.
- The rebase at line 121 runs without the `--as` identity, so the committer comes from the repo config written by init (line 153). That contradicts header line 18 ("author AND committer are …").

lane-addendum.md:126 does tell L1s to cite `pushed <hash>`.

### F6 — Medium: an external force-push makes the helper rebase and re-land a previously pushed (cited) commit (lines 117–124)

After `fetch`, `tip = heads(<b>@origin..bookmarks(<b>))` covers every local commit not on the new remote tip.
That includes commits already pushed and cited before an operator force-push.
`--ignore-immutable rebase -b` rewrites them, and the helper re-pushes the copies with rc 0.
Nothing compares the old remote tip with the new one.

Repro (sandbox):
```
. ./lib.sh; mk forced; cd $L; $H init $L forced
echo a >> LOG.md; $H commit $L --as forced -m CITED-A -- LOG.md            # pushed af01e4c
git clone … other; git -C other reset --hard HEAD~1; …commit Z.md…; git -C other push -f origin main
echo d >> README.md; $H commit $L --as forced -m D -- README.md
git -C $S/forced/origin.git merge-base --is-ancestor af01e4c… main
```
Excerpt:
```
pushed af01e4cea5daa7863eec02db3733191bbcc29e3d
committed cbf26b0d…   pushed 1a113a52…   rc=0
1a113a5 forced-shokunin D
44b03d8 forced-shokunin CITED-A          <- rewritten copy of the cited commit
e62a347 seed external-rewrite
--- is cited A ancestor of origin main?  no (af01e4cea5daa7863eec02db3733191bbcc29e3d)
```
The external force-push started this, but the helper hides it: the cited hash silently stops being an ancestor.
Header lines 21–23 ("remote commits are never rewritten") do not hold for this case.

### F7 — Low: a `nothing to commit` run still prints `pushed <hash>` and exits 0 (lines 218–219, 238–239, 111)

Repro (sandbox; fleet-root-shaped repo whose `.gitignore` has `*-shokunin/` and a nested git repo `kama-shokunin/`):
```
$H commit $L --as fleet -m via-file -- kama-shokunin/LOG.md kama-shokunin/.env
```
Excerpt:
```
nothing to commit
pushed 7ac1f0f51b84f20e1c742a4b5d3713f855c4d184
rc=0
```
`jj file track --include-ignored -- kama-shokunin/LOG.md` silently skips files inside the nested repo (`track rc=0`).
- Good: no sibling-lane content entered the outer repo; the origin tree stayed `.gitignore LOG.md README.md`.
- Bad: the output carries a `pushed <hash>` that is not the caller's commit. lane-addendum.md:126 says to cite exactly that line.

### F8 — Low: `--as` is not bound to the lane (lines 176–177)

Any `[a-z0-9-]+` id is accepted. F5 shows `--as protocol` in lane `race`.
`--as kama` in the mado lane would produce a commit that looks valid but carries the wrong lane identity.
Closures legitimately pass `protocol` (closure-prompt.md:51), so an allow-list is {lane id, protocol}.

### F9 — Info: init swallows a `bookmark track` failure (line 163, `|| true`)

In `wrongbr`, `work@origin` did not exist and tracking failed silently.
The later push of `main` failed closed (`Non-tracking remote bookmark main@origin exists`, rc=3).

### Checked and holding (negative results)

- **`@` or another bookmark is never pushed; nothing is forced by flag.**
  `git for-each-ref` on the origins after the back, race, forced, swdotslash and side runs shows only `refs/heads/main`.
  wrongbr2 shows `main work`, both pushed by the helper's `--bookmark`, as F2 explains.
  No `--force`, `--allow-new` or `git push` appears in the file.
- **`bookmarks(<branch>)` is an exact match in 0.45.1, not a substring match.**
  `bookmarks(main)` returned only `9a52cc5 main`, with `main-old` and `xmainx` present. `heads(main@origin..bookmarks(main))` was empty.
- **jj refuses to push conflicted ancestors even when the helper's tip-only check (line 105) passes.**
  Run `conf`: commit X conflicts after the rebase, then a resolving commit Z lands at the tip.
  Result: `Error: Won't push commit 968557dc9452 since it has conflicts`, rc=3, and origin is unchanged.
  Operational side effect: following the helper's "resolve in the lane, then retry" advice leaves an exit-3 loop until the conflicted ancestors are fixed.
- **The sideways `bookmark set` in the commit path is refused.**
  Run `side`: `git checkout --detach HEAD~1`, then commit `sideways-Z`.
  Result: `jj-lane: bookmark set failed`, rc=1. Origin stayed `98cf5ac A`.
- **Two `jj undo`s after a push do not force.**
  Undo also restored `main@origin`, so the lease check rejected the push and the fetch+rebase recovery landed on top of the cited commit.
  Result: `b3af972 C / 507c72c B-cited / 6b4dcf5 A`.
- **A `cp -a` copy of a jj repo does not share repo config in 0.45.1.**
  jj re-keyed the copy's `config-id` (`2e2c313627af0ee36a2f` → `8cf75d95fdc3a5e53752`), and the original kept `user.name = alpha-shokunin`.
  No `.jj/repo/config-id` under /fast/scratch matches live mado (`b7d9811b7038ba799207`) or tameshi (`86a634125f04a8756fc6`).
- **Live mado and tameshi repo configs** set `immutable_heads() = builtin_immutable_heads() | ::bookmarks()` and do **not** yet set `snapshot.auto-track = "none()"`.
  The helper's `init` adds the auto-track setting (line 152). Until then, a non-helper jj call in those lanes snapshots with the default auto-track.

## Inference

- [INFERENCE] F1 is the most likely to fire in practice.
  - Lane gates and selftests that run git writes are only told (lane-addendum.md:135), not forced, to use a sandbox clone.
  - Before this wave, operator tooling and L1 habits were all git (`git reset`, `git commit --amend`).
  - Once a lane is colocated, one stray `git commit --amend` or `git reset --hard origin/…~1`, followed by any helper commit or push, rewrites GitHub history with no `--force` anywhere in the command line.
- [INFERENCE] F2 becomes live as soon as any lane works on a non-default branch.
  - Fallback ordering at line 62 (`for-each-ref … | head -1`, alphabetical) adds risk when `origin/HEAD` is missing, e.g. a remote added by hand after `git clone --bare`.
  - audio-shokunin already has 13 `wt-r*` branches; today `main` wins because `origin/HEAD` exists.
- [INFERENCE] With F3, `./` is a plausible L1 shorthand ("commit my lane changes").
  Every `.ufo/state` run file and any non-ignored seat scratch would then be pushed to GitHub.
- [INFERENCE] The sandbox repo configs created in `~/.config/jj/repos/` (one per sandbox repo) remain after the sandbox is removed. jj owns them; I did not delete them, to keep my writes inside the sandbox.

## Recommendations (smallest remediation first)

1. **F1 (must, before rollout).** At the top of each `do_push` attempt, before line 109, refuse non-fast-forward pushes.
   Exit 1 with "local <b> is not a descendant of <b>@origin" unless `jj --ignore-working-copy log -r "${BRANCH}@origin & ::${BRANCH}"` is non-empty, or the remote branch is absent.
   A git-side equivalent: `git merge-base --is-ancestor refs/remotes/origin/$BRANCH refs/heads/$BRANCH`, after jj's export.
   Add one selftest: `git branch -f <b> <b>~1` then `push` → expect rc≠0 and origin unchanged.
2. **F2.** Do not re-detect the branch after init.
   In `commit` and `push`, read it from the alias that init wrote (line 155): `jj --ignore-working-copy config get 'revset-aliases."trunk()"'`, then strip `@origin`. Fail if it is unset.
   Also make line 163 fail when `<b>@origin` exists but cannot be tracked (F9).
3. **F3.** Canonicalize each path after `cd` (`q=$(realpath -m --relative-to=. -- "$p")`) and run the checks on `q`.
   Reject: `q` = `.`, `.ufo`, `.ufo/state`, `.ufo/state/*`, `.ufo/watchdog.log`, and any directory that contains `.ufo/state`.
   Belt and braces: before line 233, abort (and reset `@-` back into `@`) if `jj --ignore-working-copy diff --summary -r @-` lists any `.ufo/state/` path.
4. **F4.** Key the lock and the error file on `$(cd "$dir" && pwd -P)` (hash it for the filename), e.g. `jj-<sha8>.lock` and `jj-push-<sha8>.err`.
5. **F6.** Record `<b>@origin` before `git fetch` (line 117).
   After the fetch, if the old remote tip is not an ancestor of the new one, stop with exit 1 ("remote rewritten") instead of rebasing with `--ignore-immutable`.
6. **F5 / F7.** Make the citation line unambiguous:
   - print `local <h>` instead of `committed <h>`;
   - print `pushed <h>` only when this run's commit was the one pushed;
   - otherwise print `nothing to commit; remote tip <h>`.
   Pass the `--as` identity (`--config user.name/user.email`) to the rebase at line 121 so the committer matches the author.
7. **F8.** Accept `--as` only for the lane id (derived from the dir name, e.g. `<id>-shokunin`) or `protocol`.
8. Keep the fleet root on `fleet-commit.sh`.
   The helper has no guard against being pointed at `$SHOKUNIN_ROOT`: `init` only requires a `.git` dir.
   A one-line refusal in `cmd_init` and `cmd_commit` closes that.

Sandbox `/fast/scratch/jj-wave/JjSentinelHelper/` is removed. Every finding above can be rebuilt from the repro blocks plus `lib.sh` (`mk`: bare origin + seed + clone).

## Appendix — sandbox harness `lib.sh` (verbatim)

```bash
# sandbox-only harness; every path below lives under $S
set -u
S=/fast/scratch/jj-wave/JjSentinelHelper
export HYAKU_STATE=$S/state JJ_BIN=$HOME/.local/bin/jj
H=$S/jj-lane.sh
JJ=$HOME/.local/bin/jj
export GIT_AUTHOR_NAME=seed GIT_AUTHOR_EMAIL=seed@x GIT_COMMITTER_NAME=seed GIT_COMMITTER_EMAIL=seed@x
# mk <name> [branch]: bare origin + lane clone ($L) with one seed commit on main
mk() {
  local n=$1 br=${2:-main} R=$S/$1
  rm -rf "$R"; mkdir -p "$R"
  git init -q --bare -b main "$R/origin.git"
  git init -q -b main "$R/seed"
  printf 'seed\n' > "$R/seed/README.md"; printf 'log\n' > "$R/seed/LOG.md"
  git -C "$R/seed" add -A && git -C "$R/seed" commit -qm seed
  git -C "$R/seed" remote add origin "$R/origin.git"
  git -C "$R/seed" push -q origin main
  git clone -q "$R/origin.git" "$R/L$n"
  [ "$br" = main ] || git -C "$R/L$n" checkout -qb "$br"
  case $(git -C "$R/L$n" remote get-url origin) in "$S"/*) ;; *) echo "ORIGIN NOT SANDBOX"; exit 9;; esac
  L=$R/L$n
}
remote_log() { git -C "$S/$1/origin.git" log --format='%h %an|%cn %s' "${2:-main}"; }
```
