# JjTrialTabi — jj colocation trial for lane `tabi`

Seat: `JjTrialTabi-2`. Sandbox: `/fast/scratch/jj-wave/JjTrialTabi/` (removed after the trial; no cited failure needed preservation). Live repo `/home/vgpnk/Projects/shokunin/tabi-shokunin` was only read/cloned. jj 0.45.1 (`/home/vgpnk/.local/bin/jj`, `7c41cdeb`). No tools installed.

## Step 1 — Sandbox build

Commands (exactly as assigned):
```
git clone --bare /home/vgpnk/Projects/shokunin/tabi-shokunin /fast/scratch/jj-wave/JjTrialTabi/remote.git
git clone /fast/scratch/jj-wave/JjTrialTabi/remote.git /fast/scratch/jj-wave/JjTrialTabi/lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/tabi-shokunin/ /fast/scratch/jj-wave/JjTrialTabi/lane/
```
`git -C lane status --porcelain | wc -l` → **1**:
```
?? .ufo/waves/round-16/
```
Identical to the live repo's porcelain output (1 line; `--ignored` adds 3 `!!` lines: `.ufo/interactive-sessions/`, `corpus/evidence/round-13/aria/artifacts/`, `corpus/evidence/round-13/aria/node_modules/`).

10 largest untracked/ignored files (`git ls-files -o -i --exclude-standard -z | xargs -0 du -b | sort -rn | head -10`):

| bytes | path |
|---|---|
| 3,584,989 | corpus/evidence/round-13/aria/node_modules/playwright-core/lib/coreBundle.js |
| 3,085,095 | corpus/evidence/round-13/aria/node_modules/playwright-core/lib/utilsBundle.js |
| 2,825,513 | corpus/evidence/round-13/aria/node_modules/playwright/lib/transform/babelBundle.js |
| 1,796,736 | .ufo/interactive-sessions/20261015T050057Z/2026-10-15T05-04-04-073Z_….jsonl |
| 1,323,500 | .ufo/interactive-sessions/20261015T050057Z/…/__advisor.jsonl |
| 1,150,893 | corpus/evidence/round-13/aria/node_modules/playwright-core/types/types.d.ts |
| 819,286 | corpus/evidence/round-13/aria/node_modules/playwright-core/types/protocol.d.ts |
| 667,649 | corpus/evidence/round-13/aria/node_modules/playwright-core/lib/vite/traceViewer/assets/defaultSettingsView-*.js |
| 565,369 | corpus/evidence/round-13/aria/node_modules/playwright-core/lib/webp_codec.wasm |
| 547,222 | corpus/evidence/round-13/aria/node_modules/playwright/lib/matchers/expect.js |

Sandbox remote check: `git -C lane remote -v` → `origin /fast/scratch/jj-wave/JjTrialTabi/remote.git` only. No real remote was ever touched.

## Step 2 — `jj-lane.sh init`

Command:
```
HYAKU_STATE=/fast/scratch/jj-wave/JjTrialTabi/state \
  /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh init lane tabi
```
Output:
```
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `master@origin`.
Initialized repo in "."
Warning: This setting will only impact future commits.
The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>".
To change the working copy author, use "jj metaedit --update-author".   (×2)
state branch=master local=e38d2599…b4fef0 remote=e38d2599…b4fef0 ahead=0 behind=0 head=attached tracked=0 untracked=1
```
- **State line** (final line, above): clean, ahead=0/behind=0.
- **Init warning**: the working-copy author stays the *global* jj identity, not the lane's git identity — the helper's `commit` path compensates via `metaedit --update-author` (verified in step 4), but any jj write path that skips metaedit would ship `jpveigao10@gmail.com`.
- **git HEAD attached**: `git symbolic-ref -q HEAD` → `refs/heads/master` immediately after init. (It detaches later, after the first jj mutation — see step 4.)
- **`git status --porcelain` unchanged**: still exactly `?? .ufo/waves/round-16/` (1 line). No intent-to-add entries (`git ls-files --stage | grep -c intent` → 0 after `jj status` too).
- **Repo config set** (`jj --ignore-working-copy config list --repo`):
  ```
  snapshot.auto-track = "none()"
  user.name = "tabi-shokunin"
  user.email = "tabi@shokunin.local"
  revset-aliases."trunk()" = "master@origin"
  ```
- **`jj status` timing** (3 runs, `date +%s%N` deltas): **8 ms / 7 ms / 9 ms**. Output shows only `? .ufo/waves/round-16/` under Untracked paths; @ is `(empty)`, @- = `e38d2599 master`. With auto-track disabled, snapshot cost is negligible even on this tree.

## Step 3 — auto-track = `all()` control

```
cp -a lane lane-autotrack
cd lane-autotrack && jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'
jj status   # timed
```
- **Snapshot time**: 18 ms.
- **Files jj snapshotted into @**: 7 — the entire untracked `.ufo/waves/round-16/` tree (6 files: PLAN.md, w1/dispatch-result.json, w1/spec.json, w1/swarm-registry.json, w1/validation.json, w1/validation.stderr.txt) plus my own `autotrack-err.txt` scratch.
- **`new file too large` refusals**: **none**. The >1 MiB files are all inside ignored dirs (`node_modules/`, `.ufo/interactive-sessions/`), which auto-track skips. The lane's largest *tracked* file is 663 KB, so even `jj file track` (no `--include-ignored`) stays under the default `snapshot.max-new-file-size` (1 MiB).
- **git-view consequence**: `git status --porcelain` in lane-autotrack shows all 7 as `" A"` (staged-for-add but not committed). Default auto-track would make git status constantly dirty and would put untracked seat scratch into every @ snapshot. Confirmed the helper's `none()` choice is required for this lane.
- jj also printed the expected "repo appears to have been copied" warning on first run in the copy.

## Step 4 — helper commit + push + remote-move recovery

Prepare:
```
echo "jj-trial line …" >> LOG.md
mkdir -p corpus/lessons && printf 'round-999: jj colocation trial (sandbox)\n' > corpus/lessons/round-999-jjtrial.md
printf 'scratch content %s\n' "$(date +%s)" > scratch-jjtrial.txt   # left untracked
```

Commit:
```
HYAKU_STATE=…/state jj-lane.sh commit lane --as tabi -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 918129d556cd797968a763093e40c7ecc3051ca5
→ pushed    918129d556cd797968a763093e40c7ecc3051ca5   (exit 0)
```

Verifications (`H=918129d5…`):
- `git show -s --format='%an <%ae> / %cn <%ce>'` → `tabi-shokunin <tabi@shokunin.local>` for **both** author and committer.
- `git log -1 --format=%H -- LOG.md` → `918129d5…` == pushed hash. ✔
- `git merge-base --is-ancestor $H master` → exit 0. ✔
- `jj-lane.sh state .` → `state branch=master local=918129d5… remote=918129d5… ahead=0 behind=0 head=detached tracked=0 untracked=2`. ✔
- `git -C remote.git log -1 master` → `918129d5… round-999: jj trial`. ✔
- `scratch-jjtrial.txt` still `??` in `git status`, content intact (`scratch content 1792505970`); `git ls-files --error-unmatch` fails → never tracked. ✔
- HEAD became **detached at f8380e3…/working-copy parent** after the mutation (expected colocation behavior; see hazards).

Remote-move recovery:
```
git clone remote.git lane2 && cd lane2
git config user.name operator && git config user.email op@x
mkdir considerthese && echo "operator notes" > considerthese/op-1.md
git add . && git commit -qm "operator: considerthese note" && git push origin master   # → e2036b35…
```
Then in the colocated lane (LOG.md + `corpus/lessons/round-999b-jjtrial.md`):
```
jj-lane.sh commit lane --as tabi -m "round-999b: jj trial after remote move" -- LOG.md corpus/lessons/round-999b-jjtrial.md
→ committed 5b63f7b00f348f32baa5ed3325c217372fbc8557
→ pushed    f8380e382896cbda476b498f1b1bb2112454abb2   (exit 0)
```
Recovery worked exactly as designed: push rejected → `jj git fetch` → rebase of only the unpushed commit onto `master@origin` → repush.
- `git log master`: `f8380e3 (tabi) → e2036b3 (operator) → 918129d (tabi) → e38d259`; `git show -s --format=%P f8380e3` = `e2036b3…` (linear history preserved, operator commit is a strict ancestor).
- `git -C remote.git cat-file -t 5b63f7b0…` → "could not get object info": the pre-rebase hash **never reached the remote**, so the cited-hash invariant is safe.
- `state` after: `ahead=0 behind=0 local=remote=f8380e3`.
- Output shape note: `committed <hash>` prints the **pre-rebase** hash and can differ from `pushed <hash>` whenever recovery rewrites. Anything citing "committed" would be wrong; only the `pushed` line is citable. [INFERENCE] Consider suppressing the `committed` line when its hash isn't what got pushed, or printing it only after the final push succeeds.

## Step 5 — lane's own git-touching checks in the sandbox

SKILL.md gate registry (§1555–1828) lists the lane's gates. The git-spawning scripts (`grep -n "spawnSync('git'" scripts/*.mjs`): `check-freshness.mjs` (git show/ls-tree/merge-base), `check-round-contract.mjs` (git rev-parse/show), `check-user-round-contract.mjs` (git show of archived blobs). `check-sources.mjs` and `check-aria-metadata.mjs` do not invoke git. Ran the three git-touching ones, each `timeout 300`, in the colocated lane, then re-ran in `lane-plain` (fresh `git clone` of the sandbox remote, no `.jj`):

| gate | command | colocated exit | plain exit | same? |
|---|---|---|---|---|
| freshness (worktree) | `node scripts/check-freshness.mjs --worktree` | 0 (`FRESHNESS_GATE verdict=clean … matched=34`) | 0 (identical verdict line) | yes |
| pstack contract | `node scripts/check-round-contract.mjs` | 0 (`ROUND_CONTRACT verdict=clean rounds=10`) | 0 | yes |
| user contract | `node scripts/check-user-round-contract.mjs` | 1 (`verdict=failed finding=round_count "Found 6 user rounds, expected 10"`) | 1 (identical) | yes |

All three read objects by hash/ref (`git show <rev>:<path>`, `ls-tree <baseline>`), never `HEAD` or the index — colocation-transparent. The user-contract `failed` verdict is **pre-existing and documented**: SKILL.md:1800 says "expected10 stays fixed and current production remains failed6/10". No colocation-caused failures.

## PASS/FAIL summary

| step | result |
|---|---|
| 2 init (config, HEAD attached, status unchanged, state line) | PASS |
| 3 auto-track measurement | PASS (7 files would enter @; 0 size refusals; 18 ms) |
| 4 helper commit/push + verify + remote-move recovery | PASS (all invariants held) |
| 5 lane gates in colocated repo | PASS (3/3 parity with plain clone; the one `failed` verdict is pre-existing) |

## Colocation hazards specific to `tabi`

1. **Ignored oversized trees** — `corpus/evidence/round-13/aria/node_modules/` (playwright, up to 3.5 MB/file) and `.ufo/interactive-sessions/*.jsonl` (up to 1.8 MB). Harmless today *because* they are gitignored (nested `.gitignore` at `corpus/evidence/round-13/aria/.gitignore:1`). If a seat ever removes that ignore or passes one of these files as a named pathspec to `jj-lane.sh commit`, `--include-ignored` will track it (>1 MiB allowed via `--include-ignored`) and it will be committed and pushed. The helper's file-vs-dir split makes *named files* the risk, not dirs.
2. **Untracked-but-not-ignored `.ufo/waves/`** — live repo has `.ufo/waves/round-16/` (248 KB, 6 files) as `??`. Under default auto-track it silently enters @ (measured); under the helper it stays untracked. Any seat that runs a raw `jj` command without `--ignore-working-copy` *inside the live lane* would, even with repo `auto-track=none()`, be fine — but with the default it would stage these. This is the " A" status-pollution hazard observed in lane-autotrack.
3. **Detached HEAD after first jj mutation** — `git symbolic-ref HEAD` fails post-commit; `@{u}`/`git pull`/`git status -sb` upstream displays break. All three lane gates are immune (hash-anchored reads), but `detect_branch`'s origin/HEAD→master fallback is load-bearing: keep `remote.origin.HEAD` set (it is, via clone) and do not delete the `master` local ref.
4. **Index destruction on jj mutation** — jj resets the git index each snapshot/commit; any workflow that `git add`s in the lane between helper calls loses its staging. The lane gates don't stage; fine today.
5. **Working-copy author leak** — init warning showed @'s author is the operator's global jj identity (`jpveigao10@gmail.com`), not `tabi-shokunin`. Only `metaedit --update-author` (inside `commit`) fixes it; a hypothetical helper path that commits without metaedit would violate the lane-identity invariant.
6. **Symlinks inside ignored node_modules** (`node_modules/.bin/playwright`) — never enter jj while ignored; harmless.
7. **git-lfs filters configured, zero LFS files** — repo config has `filter.lfs.*` (global LFS install) but no `.gitattributes` anywhere (`find -name .gitattributes` empty; `check-attr filter` → unspecified). If an LFS attributes file ever lands, jj does not run clean/smudge filters: blobs would be committed as LFS pointer text or raw bytes inconsistently with git clones. Recommend never adding `.gitattributes` to this lane.
8. **`committed` vs `pushed` hash divergence on recovery** — observed live (5b63f7b0 vs f8380e3). Reports must cite the `pushed` line only.

No nested `.git` dirs found outside `.git/`; no hooks in `.git/hooks/` beyond samples; no generated directories that gates rebuild inside the repo.

## Recommendations (per-lane)

- Keep `snapshot.auto-track = "none()"` (mandatory for this lane — step 3 shows immediate ` A` pollution otherwise).
- Add to repo `/.gitignore`: `scratch-*` or a documented `scratch/` seat-scratch convention, so helper `commit` pathspecs can't silently sweep named scratch into a commit; `.ufo/waves/` may stay untracked (helper protects it) but ignoring it removes the step-3 staging hazard entirely if auto-track is ever flipped.
- Keep `corpus/evidence/round-13/aria/.gitignore` (`node_modules/`) forever; consider adding `.ufo/interactive-sessions/` protection awareness to `jj file track` callers — never pass a `*.jsonl` session file as a pathspec.
- Helper-side (fleet, not lane): have `commit` print `pushed` as the only hash, or reprint `committed` post-push.
- Do not introduce `.gitattributes`/LFS, hooks, or submodule dirs into this lane; none exist and jj would not honor them.

## [INFERENCE] summary

- The failed user-contract gate is environmental by design (documented failed6/10), not a colocation regression — identical verdict and finding in the plain clone.
- `jj status` at ~8 ms with auto-track off means the helper adds no measurable per-call latency versus git-native commits on this tree.
- The largest realistic `jj file track --include-ignored` accident is a multi-MB evidence file passed as a named path; a per-commit `--max-new-file-bytes` guard in the helper would close that residual without affecting normal rounds.
