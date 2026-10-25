# JjTrialGameDev2d — jj-colocation trial for lane `game-dev-2d`

Seat: JjTrialGameDev2d-2 (leaf). Live repo `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin` (branch `main`) was never touched by `jj` and never mutated; all `jj` ran under `/fast/scratch/jj-wave/JjTrialGameDev2d/` only. The sandbox remote is the sandbox-local bare clone; `git remote -v` was verified before any push. jj 0.45.1 (`~/.local/bin/jj`), git 2.56.0. No installs were needed.

## Step 1 — sandbox build (PASS)

```
git clone --bare <live>/game-dev-2d-shokunin /fast/scratch/jj-wave/JjTrialGameDev2d/remote.git   # HEAD bce53b83 on main
git clone <sandbox>/remote.git <sandbox>/lane
rsync -a --exclude=.git --exclude=.jj <live>/ <sandbox>/lane/
git -C <sandbox>/lane status --porcelain | wc -l        → 0
```

Every extra file in the lane is **ignored**, not merely untracked: `git ls-files --others --exclude-standard` → **0**, `git ls-files --others --ignored --exclude-standard` → **13 560** (identical counts in the live repo, read-only). `git status --porcelain --ignored` collapses them to 4 directories:

```
!! corpus/live/r101-ver11/mut02run/proj/.godot/
!! corpus/live/r101-ver11/scratch/
!! corpus/live/r101-ver17/scratch/
!! corpus/live/runs/
```

10 largest ignored files (`git ls-files -z --others --ignored --exclude-standard | xargs -0 du -b | sort -rn | head`):

| bytes | path |
|---|---|
| 73 703 800 | corpus/live/runs/20261019T023223438217Z/scratch/out/fixture.x86_64 |
| 73 703 800 | corpus/live/r101-ver11/scratch/freshB/out/fixture.x86_64 |
| 73 703 800 | corpus/live/r101-ver11/scratch/freshA/out/fixture2.x86_64 |
| 73 703 800 | corpus/live/r101-ver11/scratch/freshA/out/fixture.x86_64 |
| 73 519 416 | corpus/live/r101-ver11/scratch/freshC/out2/q.x86_64 |
| 73 519 416 | corpus/live/r101-ver11/scratch/freshC/out/p.x86_64 |
| 73 519 416 | corpus/live/r101-ver11/scratch/exportproj/out/prod.x86_64 |
| 1 566 958 | corpus/live/runs/20261019T023414562462Z/verdicts.json |
| 1 566 941 | corpus/live/runs/20261019T021419889989Z/verdicts.json |
| 1 566 827 | corpus/live/runs/20261019T020131429418Z/verdicts.json |

Lane worktree ≈ 1.7 GB, `.git` 264 MB (history already contains eight committed 73.7 MB `fixture.x86_64` binaries and three 11 MB text files — big binaries are the norm for this lane, not an anomaly).

## Step 2 — helper init (PASS)

```
HYAKU_STATE=<sandbox>/state <shokunin>/scripts/hyaku/jj-lane.sh init <sandbox>/lane game-dev-2d
```

- **State line:** `state branch=main local=bce53b83… remote=bce53b83… ahead=0 behind=0 head=attached tracked=0 untracked=0`
- **Init warnings (benign, 2×):** `Warning: This setting will only impact future commits. The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>".` — cosmetic only; the commit path stamps author via `metaedit --update-author` (verified in step 4).
- **Repo config read back** (`jj --ignore-working-copy config list --repo`):
  `snapshot.auto-track = "none()"`, `user.name = "game-dev-2d-shokunin"`, `user.email = "game-dev-2d@shokunin.local"`, `revset-aliases."trunk()" = "main@origin"`. Exact lane contract.
- **git HEAD:** `git symbolic-ref -q HEAD` → `refs/heads/main` — **attached** after init.
- **porcelain delta:** `git status --porcelain | wc -l` still **0** (unchanged vs step 1). `.jj/` appears only under `--ignored` as `!! .jj/` — jj self-ignores via `.jj/.gitignore` containing `/*` (`git check-ignore -v .jj/` → `.jj/.gitignore:1:/*`). No `.git/info/exclude` or `.gitignore` edits needed.
- **`jj status` timing** (3 runs, bash `time`): 0.019 s / 0.017 s / 0.017 s — the ignore-heavy worktree costs ~17 ms warm. Cold first `jj status` after init was included in the init wall time (~seconds; not separately measured).
- `.jj/` overhead: **4.3 MB** next to the 264 MB `.git`.

## Step 3 — default `auto-track="all()"` alternative (PASS, and the data is reassuring for this lane)

```
cp -a <sandbox>/lane <sandbox>/lane-autotrack
jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'
jj status   → "The working copy has no changes."   real 0.018 s
```

- **Files snapshotted into @: 0.** With `all()`, jj would track every *untracked* file — but this lane has **zero non-ignored untracked files**; its 13 560 scratch files are all covered by `corpus/.gitignore` + `corpus/live/.gitignore` (which jj honours identically to git). The default-auto-track incident measured elsewhere cannot reproduce here as long as the ignore discipline holds.
- **`new file too large` refusals: 0** for existing content. Counterfactual probe: `head -c 2500000 /dev/urandom > reports/big-newfile.bin` (non-ignored dir) then `jj status` →
  `Warning: Refused to snapshot some files: reports/big-newfile.bin: 2.4MiB (2500000 bytes); the maximum size allowed is 1.0MiB` — the file stays **untracked**, exit 0. Fail-safe, not fail-dangerous: a seat that forgets to ignore a >1 MiB artifact produces a *missing* file in the commit (silently fixable by naming the file to the helper — `jj file track --include-ignored` admits it), never a 73 MB blob smuggled in.
- **Snapshot time:** 0.018 s (unchanged; ignores prune the walk before any stat storm).

## Step 4 — real helper round commit + push recovery (PASS)

Prepared: `LOG.md` append, new `corpus/lessons/round-999-jjtrial.md`, scratch `jjtrial-scratch.txt` left untracked (non-ignored dir → `??`).

```
HYAKU_STATE=<sandbox>/state <helper> commit <sandbox>/lane --as game-dev-2d \
  -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 9ad94dacc0950ebbce9b9b572177689b4c31606a
→ pushed    9ad94dacc0950ebbce9b9b572177689b4c31606a     exit=0
```

Verifications (all commands shown verbatim):

| check | result |
|---|---|
| `git log -1 --format='%an <%ae> / %cn <%ce>' $H` | `game-dev-2d-shokunin <game-dev-2d@shokunin.local>` — **author AND committer** correct |
| `git log -1 --format=%H -- LOG.md` | `9ad94dac…` — equals pushed hash |
| `git merge-base --is-ancestor $H main` | rc=0 |
| `<helper> state <lane>` | `ahead=0 behind=0 head=detached tracked=0 untracked=1` |
| `git -C <sandbox>/remote.git rev-parse main` | `9ad94dac…` — remote has the commit |
| `git status --porcelain` | `?? jjtrial-scratch.txt` — still untracked, content intact |
| `git symbolic-ref -q HEAD` | **detached** after the first jj mutation — the documented colocation tax |

**Operator-push recovery.** Second clone `<sandbox>/operator` committed+pushed `considerthese/op-note.md` (`53abffb0`). Lane appended to `LOG.md` and reran the helper:

```
→ committed cdf6e2580e8234b3792d1db7ae5e714488addc2a
→ pushed    4778e05e8fe8ce7fdbb140a6a6f6012767addd11      exit=0
```

`jj git push` was rejected, the helper fetched, rebased only the unpushed commit (`main@origin..main` → change id of the lane commit) onto the new `main@origin`, moved the bookmark, retried. Resulting remote graph: `4778e05e` → `53abffb0` (op) → `9ad94dac` → `bce53b83`. `git merge-base --is-ancestor cdf6e258 main` rc=1 (pre-rebase hash correctly superseded — the helper printed the *post-rebase* hash as `pushed`), `9ad94dac` and `53abffb0` are ancestors. **Landed = cited hash holds; remote commits never rewritten; no force-push.** `op-note.md` materialised in the lane worktree.

## Step 5 — lane git-touching checks (PASS)

This lane is **shonen seed**: no `SKILL.md`, no `tools/`, no `scripts/` (verified on the live repo). Its persistent gates live in `reports/round-*/mutations/` (selftests) and `corpus/live/*/watch.sh`/`run-reps.sh`. Three representative git-touching checks were run against the sandbox lane only (300 s timeout), then re-run in a plain-git control clone to separate colocation faults from pre-existing ones:

| # | check | git verbs used | jj-lane rc | control rc | identical? |
|---|---|---|---|---|---|
| 1 | `sh reports/round-105/r105-count.sh HEAD` (r105 counting gate; drives `r105-mapped-criteria.py`) | `rev-parse`, `show`, `ls-tree` | 0 | 0 | yes — all 15 output lines byte-identical (`res_uid 29 r105 7 total 600`; `5/3/31`) |
| 2 | `bash reports/round-102/mutations/mut06_stale_cite_resurrection.sh <scratch> <repo>` (official-S4 stale-cite gate harness, 6 arms) | `status --porcelain`, `show $REV:$f` | 0 | 0 | yes — 25-line pre-apply census, all 6 arms identical verdicts |
| 3 | `git archive HEAD corpus/fixtures \| tar -x` (the extraction primitive used by `run-reps.sh` r88/r89 baselines) | `archive` | 0 (132 files) | 0 (132 files) | yes |

**Colocation-caused failures among the three: zero.** Everything the lane's checks actually call — `rev-parse`, `show`, `ls-tree`, `status`, `log`, `archive`, `merge-base` — works on the jj-managed repo because jj exports real git refs.

**Where colocation DOES break lane primitives (measured, all on the jj lane):**

| primitive | result |
|---|---|
| `git rev-parse --abbrev-ref '@{u}'` | `fatal: HEAD does not point to a branch` (rc=128) |
| `git branch --show-current` | empty |
| `git symbolic-ref -q HEAD` | detached (after first mutation; attached between init and first commit) |
| `main@{u}` | `origin/main` — branch upstream survives; only `@{u}`/HEAD forms die |
| `git add` + `jj status` | staged entry `A  stage-test.md` **survived** a plain `jj status` — index is only reset on *mutating* jj ops (commit/rebase), not on read-only status. Still a hazard for flows that stage with git before a helper commit lands |

Lane scripts actually at risk: the `watch.sh`/`wait_for_landing.sh` family uses `git rev-parse --show-toplevel`, `git status --porcelain`, `git log -1 --format=%h` — **all safe under colocation**. `run-reps.sh` uses `git rev-parse HEAD` — safe. Nothing in the lane greps `@{u}` or `branch --show-current`. Detection in the helper (`detect_branch`) already compensates via `origin/HEAD`.

## PASS/FAIL table

| step | check | verdict |
|---|---|---|
| 2 | init, config keys, attached HEAD, zero porcelain delta, fast `jj status` | **PASS** |
| 3 | `all()` would track 0 files; 1 MiB refusal is warn-not-commit | **PASS** |
| 4 | commit identity, pathspec-limit, ancestor, pushed==cited, op-push rebase recovery, scratch untouched | **PASS** |
| 5 | 3 git-touching checks identical to plain-git control; only `@{u}`/`--show-current` break | **PASS** |

## Lane-specific colocation hazards

1. **Big files:** history already carries 8× 73.7 MB `fixture.x86_64`; ~512 MB of ignored 73 MB binaries sit in `corpus/live/*/scratch/`. The 1 MiB `snapshot.max-new-file-size` refusal protects against accidental ingestion, but a seat committing a *legitimate* new >1 MiB artifact via a directory pathspec (`-- corpus/live/r106/foo/`) silently loses it. `--include-ignored` only fires for named **files** in the helper.
2. **Absolute symlinks (34):** e.g. `corpus/live/r67-simplifier/del-measure/fixtures/animation_property.gd → /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin/corpus/fixtures/…`. Pre-existing repo hazard, jj-agnostic — `git archive` exports the link text; they dangle on any foreign clone and **follow into the live repo** even inside a sandbox copy (measured: `readlink` resolves to the live path). Nothing mutates through them, but a lane tool that `rm`/`write`s a fixture through the link would touch the live tree.
3. **Ignored-dir depth:** `**/.godot/`, `**/scratch/`, `runs*/`, `live/**/*tree*/` patterns carry 13.5k ignored files. If a new generated dir lands outside these globs, default `all()` auto-track would ingest it — the `none()` init is the right pin.
4. **Detached HEAD:** anything upstream-tracking (`@{u}`, `pull`, `push` bare) dies after the first helper mutation. The lane's real scripts are unaffected; ad-hoc operator `git pull` habits are.
5. **Index reset on mutation:** `git add`-staged work must be committed by git (or re-staged) before a helper commit — mixing `git add` staging with `jj commit` loses the stage.
6. **No hooks, no LFS, no `.gitattributes` filters** (`.git/hooks/` contains only samples; `git lfs` installed but unused). Nothing fires behind jj's back.
7. **Hardcoded absolute `REPO=` paths** in older harnesses (`r102-ver9-run.py`, `r102-w3-census.py`) point at the live lane — a pre-existing anti-pattern; they'd bind to the live repo even from a clone. jj-neutral but worth noting for tooling hygiene.

## Recommended per-lane config / ignore additions

The helper's init keys (`auto-track="none()"`, lane identity, `trunk()=main@origin`) are sufficient as-is for this lane. Recommendations:

1. **No `.jjignore` needed** — the existing nested `.gitignore` pair already covers all generated content; `all()` measured 0 files.
2. **No `snapshot.max-new-file-size` bump** — keep the 1 MiB refusal; the lane's 73 MB artifacts are correctly ignored, and the refusal is fail-safe.
3. **Optional `.gitignore` belt:** add `*.x86_64`, `*.exe`, `verdicts.json` outside `runs*/` is over-broad — instead recommend one line `live/**/out/` if run-output dirs start appearing outside `scratch/`; **not required now** (measured: every ignored binary already sits under an ignored dir).
4. **[INFERENCE]** Convert the 34 absolute fixture symlinks to relative at the next corpus-maintenance round — unrelated to jj, but it is the lane's one real cross-checkout hazard.
5. **[INFERENCE]** `jj` is safe for this lane's write path via the helper; fleet-root `fleet-commit.sh` can stay git — no evidence here changes that split either way.

## Verdict

**Colocation is a clean fit for `game-dev-2d`.** All four protocol invariants held under test (pushed==cited, cited stays ancestor, lane identity on author+committer, pathspec-limited commits; LOG.md append-only and `.ufo/state` never committed — LOG.md append confirmed byte-wise, `.ufo/` does not exist in this lane). The lane's unusually strict ignore hygiene means even the default `auto-track` would be harmless here; the helper's `none()` pin removes the residual risk class entirely. Sandbox retained at `/fast/scratch/jj-wave/JjTrialGameDev2d/` pending integrator review (contains the full evidence trail: `remote.git`, `lane`, `lane-autotrack`, `operator`, `control`, `state/`, `scratch-out/`); it is fully disposable.
