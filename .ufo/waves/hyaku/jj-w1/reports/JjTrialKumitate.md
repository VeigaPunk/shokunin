# JjTrialKumitate — jj-colocation trial for lane `kumitate`

jj 0.45.1 (`jj 0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`, `~/.local/bin/jj` via PATH).
Sandbox: `/fast/scratch/jj-wave/JjTrialKumitate/` (lane, lane-autotrack, lane-plain, operator-clone, remote.git).

## Findings (observed)

### Step 1 — sandbox build

```
git clone --bare /home/vgpnk/Projects/shokunin/kumitate-shokunin .../remote.git     # ok
git clone .../remote.git .../lane                                                  # ok
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/kumitate-shokunin/ .../lane/
git -C .../lane status --porcelain | wc -l   →  0
git status --porcelain --ignored             →  !! .ufo/interactive-sessions/   (only entry)
```

10 largest untracked-or-ignored files (live tree has **zero** untracked files; the only non-tracked content is the gitignored `.ufo/interactive-sessions/` dir):

```
1.8M  .ufo/interactive-sessions/20261015T050057Z/2026-10-15T05-04-01-333Z_01a13df2-….jsonl
808K  .ufo/interactive-sessions/…/__advisor.jsonl
48K   .ufo/interactive-sessions/…/2.bash-original.log
```
(The directory holds ~2.6M total; everything else is tracked.) `.gitignore` = `.ufo/interactive-sessions/` (single line). No `.gitattributes`, no nested `.git`, no symlinks, no non-sample hooks anywhere in the lane.

### Step 2 — colocate through the helper

```
HYAKU_STATE=.../state scripts/hyaku/jj-lane.sh init .../lane kumitate   → exit 0
state line: state branch=master local=1770305f… remote=1770305f… ahead=0 behind=0 head=attached tracked=0 untracked=0
```

Init warnings observed (stderr):

```
Warning: This setting will only impact future commits.
The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>".
To change the working copy author, use "jj metaedit --update-author".
```
(×2 — the @ author is only re-stamped at commit time by `metaedit --update-author`; step 4 confirms the stamp works.)

Repo config after init (`jj config list --repo`):

```
revset-aliases."trunk()" = "master@origin"
snapshot.auto-track = "none()"
user.name = "kumitate-shokunin"
user.email = "kumitate@shokunin.local"
```

`jj status` ×3 from the lane: 9 ms / 8 ms / 8 ms (measured via `date +%s%N`); output "The working copy has no changes." After init **git HEAD is attached** (`git symbolic-ref -q HEAD` → `refs/heads/master`, exit 0) and `git status --porcelain` is still 0 — no git-visible change vs step 1, even after the three `jj status` runs.

### Step 3 — default `auto-track="all()"` alternative

```
cp -a lane lane-autotrack && rm -rf lane-autotrack/.jj
jj --config 'snapshot.auto-track="all()"' git init --colocate .   → 25 ms (init+first snapshot)
jj --ignore-working-copy diff --summary -r @ | wc -l              → 0
grep -i 'too large' (init output)                                  → no match
```

`auto-track="all()"` snapshots **0 files** here: every non-tracked path is gitignored, and jj's tracker honors `.gitignore`. The 1.8M ignored jsonl never entered @, so no `new file too large` refusal was reachable on this lane's real content. The mado/tameshi scratch-tracking incident is therefore not reproducible on kumitate with default settings; the hazard only materializes if a lane adds un-ignored scratch.

### Step 4 — round-commit simulation

Preparation: appended a line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left `scratch-jjtrial.txt` untracked.

```
jj-lane.sh commit .../lane --as kumitate -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 1792faa34340d94d64fb95a808e8b028f088106a
→ pushed    1792faa34340d94d64fb95a808e8b028f088106a        exit 0
```

Verification:

| check | command | result |
|---|---|---|
| identity | `git log -1 --format='%an <%ae> / %cn <%ce>'` | author AND committer = `kumitate-shokunin <kumitate@shokunin.local>` |
| pathspec tip | `git log -1 --format=%H -- LOG.md` | `1792faa3…` = pushed hash |
| ancestor | `git merge-base --is-ancestor $H master` | exit 0 |
| helper state | `jj-lane.sh state lane` | `ahead=0 behind=0 head=detached tracked=0 untracked=1` |
| remote | `git -C remote.git log --oneline -1 master` | `1792faa round-999: jj trial` |
| scratch | `cat scratch-jjtrial.txt`; `git status --porcelain` | content intact; still `??` |

After the jj mutation, git HEAD detached (`symbolic-ref` exit 1) — expected colocated behavior; the helper's `detect_branch` still resolves `master` via `refs/remotes/origin/HEAD`, and its `state` line works.

**Operator-push recovery:**

```
# second clone "operator-clone": git commit+push considerthese/operator-push.md → remote tip 5b0ecd09
jj-lane.sh commit .../lane --as kumitate -m "round-999b: post-operator commit" -- considerthese/lane-second.md
→ committed 2027cfba83ab56e09843c7da24c35aa5f68ce449
→ pushed    04b6b9d9ae9985a7cdf2f85ca72e6adbed7808b4     exit 0
```

The helper detected the rejected push, fetched, rebased only the unpushed commit onto `master@origin`, retried. Remote log: `04b6b9d` → `5b0ecd0` (operator) → `1792faa`. `git merge-base --is-ancestor 5b0ecd09 master` → 0. **Caveat:** `committed` ≠ `pushed` when a rebase happens — `2027cfba` is the pre-rebase hash that never reached the remote; only the `pushed` hash is citable. The helper already prints the right one last.

### Step 5 — lane git-touching gates

Gates run with 300 s timeout, jj lane vs `lane-plain` (rsync'd clone, no `.jj`). round-gate invoked with `--repo/--main-repo/--reports-dir` pointed at each sandbox (its defaults resolve to the lane's *parent* — under colocation nothing changed here; the flagging below is `--close` mode).

| gate | jj lane exit | plain clone exit | colocation? |
|---|---|---|---|
| `cite-check.mjs --selftest` | 0 (`VERDICT: PASS`, 62/62) | — | no |
| `cite-check.mjs` (real) | 1 `DRIFT errors=613` | 1 `DRIFT errors=613` | pre-existing |
| `sources-check.mjs --selftest` | 0 (`46/46 pass`) | — | no |
| `sources-check.mjs` (real) | 0 `SOURCES_CHECK: CLEAN` | — | no |
| `claims-check.mjs` | 1 `DRIFT errors=6` | 1 `DRIFT errors=6` (identical) | pre-existing |
| `round-gate.mjs --close` | **fail-closed `UPSTREAM_MISSING`: `git rev-list --count @{u}..HEAD` → exit 128 "HEAD does not point to a branch"** | proceeds past upstream check (errors only on report/tree content) | **YES — caused by detached HEAD** |
| `round-gate.mjs --close` after `rm scratch` (tree fully clean) | still `UPSTREAM_MISSING` exit 128 | — | **YES** |
| `round-gate.mjs --tracked` | `NO_FILED_REPORTS` (only 1 filed round-34 report in sandbox; needs ≥2) | n/a | test-fixture artifact, not colocation |

The `UPSTREAM_MISSING` fail-closed comes from `round-gate.mjs:456` `git rev-list --count @{u}..HEAD` and again at `:483` `git log @{u}..HEAD` on `--main-repo`. On a detached HEAD `@{u}` cannot resolve, so **every `--close` round audit and every `--main-repo` pointed at a colocated lane would fail-closed** even with a clean, fully-pushed tree.

Secondary observation: `cite-check`'s index counts differ between the trees — `fleetIndexFiles=473` (jj lane) vs `573` (plain) — because `EXCLUDE_DIRS` (`cite-check.mjs:121`: `node_modules .git target .ufo`) does not prune `.jj`. jj's store adds repo internals to the scanned tree. It did not change the verdict here, but it adds scan surface and could flip a file-existence token. `.jj` is also absent from every other walker's prune list.

## PASS/FAIL table

| step | verdict | notes |
|---|---|---|
| 1 sandbox build | PASS | clone+rsync faithful; 0 porcelain |
| 2 helper init | PASS | correct repo config, attached HEAD, no git-visible change, jj status 8–9 ms |
| 3 auto-track="all()" | PASS (informative) | 0 files snapshotted, 25 ms, no too-large refusals — all scratch is gitignored |
| 4 commit/push + recovery | PASS | identities, pathspec limit, ancestor invariant, ahead=0, fetch+rebase recovery all verified; cite `pushed`, not `committed` |
| 5 lane gates | **FAIL — one colocation-caused** | `round-gate --close` fail-closes on `@{u}` with detached HEAD; all other gate results identical to plain clone |

## Lane-specific colocation hazards

1. **`@{u}` / detached HEAD (real, verified):** any tool using `HEAD@{u}` — `round-gate.mjs --close` and `--main-repo` checks (`rev-list @{u}..HEAD`, `log @{u}..HEAD`), plus generic `git pull`/`git status -sb` workflows — fails after the first jj mutation. `detect_branch`-style fallback (origin/HEAD → master) is required.
2. **`.jj` tree not pruned (verified index-count delta):** every lane walker (`cite-check`, `claims-check`, `proxy-check`, `surface-probe`, `sources-check`, `kimi-census`, `round-gate` selftest fixture walkers) prunes `.git` but not `.jj` (404K here). Same class of hazard as the `.git` prune.
3. **Git index destruction:** jj resets the index on mutation; no lane tool stages via `git add` (all commits go through the helper/fleet-commit), so impact is nil for this lane, but any human `git add` in the lane is silently undone.
4. **Ignored big file:** `.ufo/interactive-sessions/` jsonl (1.8M) is ignored, so `auto-track` never sees it; if it were ever named as a commit path, the helper's `file track --include-ignored` would admit it anyway (helper comment documents this). Lane policy should keep `.ufo/interactive-sessions/` out of commit pathspecs.
5. **Non-hazards verified:** no symlinks, no nested `.git`, no `.gitattributes`/LFS, no hooks, no tracked file >1 MiB (largest tracked = SCORECARD.md 153K), no `jj`-visible conflict state (`::bookmarks(master) & conflicts()` empty).
6. **`committed` vs `pushed` hash divergence on rebase:** reports citing the first hash would name a commit that is not on the remote. The helper's output order already handles this; consumers must take the last `pushed` line.

## Recommendations (per-lane config / ignores)

- `scripts/round-gate.mjs`: resolve ahead/behind as `<branch>@origin..<branch>` (or `origin/<branch>..<branch>` in git terms) using a `detect_branch` fallback instead of `@{u}..HEAD`; apply the same fix at `:456` and `:483`. This is the one blocking fix for `kumitate` round close under colocation.
- Add `'.jj'` to `EXCLUDE_DIRS`/`PRUNE_DIRS` in `cite-check.mjs`, `claims-check.mjs`, `proxy-check.mjs`, `surface-probe.mjs`, `sources-check.mjs`, `kimi-census.mjs`, and the selftest fixture walkers in `round-gate.mjs`.
- `.gitignore`: no additions needed for jj itself (colocated `.jj` is invisible to git); consider keeping `.ufo/interactive-sessions/` ignored (already is) and ensure `.ufo/state/` stays out of pathspecs — the helper already refuses it.
- No jj repo-config additions needed beyond what `init` already sets; `snapshot.auto-track="none()"` is sufficient because all lane scratch is gitignored.

## Cleanup

Sandbox `/fast/scratch/jj-wave/JjTrialKumitate/` retained for integrator spot-checks; safe to remove.
No installs performed (jj 0.45.1 already present; `/usr/bin/time` absent — timings taken with `date +%s%N`).
