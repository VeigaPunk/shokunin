# JjTrialMado — jj colocation trial, lane `mado`

Lane repo: `/home/vgpnk/Projects/shokunin/mado-shokunin` (branch `master`, remote `origin` → github.com/VeigaPunk/mado-shokunin.git). Sandbox: `/fast/scratch/jj-wave/JjTrialMado/` (kept — see cleanup note). jj 0.45.1 at `~/.local/bin/jj`.

## Step results

### Step 1 — sandbox build

```
git clone --bare /home/vgpnk/Projects/shokunin/mado-shokunin /fast/scratch/jj-wave/JjTrialMado/remote.git
git clone /fast/scratch/jj-wave/JjTrialMado/remote.git /fast/scratch/jj-wave/JjTrialMado/lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/mado-shokunin/ /fast/scratch/jj-wave/JjTrialMado/lane/
git -C lane status --porcelain | wc -l   → 5
```

Observed porcelain (collapsed dir form; `git status --porcelain --ignored -uall` expands to **105 `??` files + 4 `!!` entries**):

```
?? .ufo/waves/round-17/drafts/
?? .ufo/waves/round-17/label-check.py
?? .ufo/waves/round-17/label-claims.json
?? .ufo/waves/round-17/tripwire/
?? .ufo/waves/round-17/w1/reports/
!! .ufo/interactive-sessions/
```

10 largest untracked/ignored files (`du -b` over `--ignored -uall` paths):

```
1652470  .ufo/interactive-sessions/20261015T050057Z/2026-10-15T05-04-03-342Z_…48a1.jsonl   (ignored)
 976700  .ufo/interactive-sessions/20261015T050057Z/…/__advisor.jsonl                     (ignored)
  39939  .ufo/waves/round-17/w1/reports/ExistingIdleNotes.md
  31594  .ufo/waves/round-17/w1/reports/RevTripwireContract.md
  26015  .ufo/waves/round-17/w1/reports/SiblingOverlap.md
  24052  .ufo/waves/round-17/w1/reports/HostIdleFiles.md
  23718  .ufo/waves/round-17/w1/reports/LessonChainJoin.md
  23343  .ufo/waves/round-17/w1/reports/SrcTerminalAlternates.md
  22691  .ufo/waves/round-17/w1/reports/RevPreRegistration.md
   7269  .ufo/waves/round-17/label-check.py
```

Note: `wc -l` on the live repo read 14 at first contact and 5 at comparison time — six lane rounds were mid-write in the live tree; the sandbox diff against a re-read of live porcelain was `NO CHANGE`.

### Step 2 — helper init

```
HYAKU_STATE=/fast/scratch/jj-wave/JjTrialMado/state scripts/hyaku/jj-lane.sh init <lane> mado
→ exit 0
state branch=master local=fc6f9609dc51… remote=fc6f9609dc51… ahead=0 behind=0 head=attached tracked=0 untracked=5
```

- Helper state line: `state branch=master local=fc6f9609dc51335458158c173af7f9891bee8e20 remote=fc6f9609dc51335458158c173af7f9891bee8e20 ahead=0 behind=0 head=attached tracked=0 untracked=5`
- Init warnings (non-fatal, expected): "The author of the working copy will stay `Joao Pedro Veiga <jpveigao10@gmail.com>`… use `jj metaedit --update-author`" — the already-open `@` keeps the operator identity until the first commit; committed output verified lane identity in step 4. Also the benign `master@origin` track hint, consumed by the helper's own `bookmark track`.
- Repo config readback (`jj --ignore-working-copy config list --repo`):

```
revset-aliases."trunk()" = "master@origin"
snapshot.auto-track = "none()"
user.name = "mado-shokunin"
user.email = "mado@shokunin.local"
```

- `git symbolic-ref -q HEAD` → `refs/heads/master` (**attached**).
- `git status --porcelain` after init: `sort | diff` vs pre-init snapshot → **NO CHANGE**, all five entries still `??`.
- `jj status` timing (3 runs, bash `time`): real 0.007 s / 0.011 s / 0.009 s. `.jj` store: 468 KiB beside a 7.7 MiB `.git`.

### Step 3 — auto-track `all()` on a copy

```
cp -a lane lane-autotrack && cd lane-autotrack
jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'
time jj status   → real 0.032 s
```

- Files snapshotted into `@`: **105 `A` entries** (the complete round-17 untracked set).
- `git status --porcelain` after the snapshot: **105 `A ` staged entries** — auto-tracked files land in the git index as additions. Under default auto-track, a later `jj`/`git` commit path anywhere near these files would sweep seat scratch into the branch.
- `new file too large` probe: created `bigscratch.bin` (2,000,000 B, untracked). `jj status` → `Warning: Refused to snapshot some files` (jj `snapshot.max-new-file-size` default 1 MiB); file remains `??`, 0 entries in `@`, not in git index.
- The ignored `.ufo/interactive-sessions/*.jsonl` (1.65 MB) is not a snapshot candidate — jj honors `.gitignore`. No refusal came from real content.

### Step 4 — round commit + race recovery

Prepare: appended a line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left `scratch-jjtrial.txt` untracked.

```
HYAKU_STATE=… scripts/hyaku/jj-lane.sh commit <lane> --as mado -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 26d5060dedac8c1e565cfdd0ed9487918f9d5ba1
→ pushed    26d5060dedac8c1e565cfdd0ed9487918f9d5ba1   exit=0
```

Verifications (hash `26d5060d…`):

- `git show -s --format=…` → author **and** committer `mado-shokunin <mado@shokunin.local>` ✓
- `git log -1 --format=%H -- LOG.md` → `26d5060d…` == pushed hash ✓
- `git merge-base --is-ancestor 26d5060d… master` → success ✓
- `jj-lane.sh state` → `… ahead=0 behind=0 head=detached tracked=0 untracked=6` ✓ (detached HEAD post-mutation is the documented colocation state)
- sandbox `remote.git` log shows `26d5060` on `master` ✓
- `scratch-jjtrial.txt` still `??`, content `scratch do not commit` intact ✓

Operator-push race: cloned `remote.git` → `operator/`, committed+pushed `considerthese/operator-note.md` (`ca766aa`). Then a second helper commit of `LOG.md` in the colocated lane:

```
→ committed 3e4cd428a3152f213d4764ac17d284859c528d9f
→ pushed    544fbe84921e4058e264cddd4bd80a6b21cdc2fb   exit=0
state … ahead=0 behind=0 head=detached
remote log: 544fbe8 / ca766aa (operator note) / 26d5060 / fc6f960
```

The first push was rejected, helper fetched, rebased the unpushed commit onto moved `master@origin`, retried, and printed the **post-rebase** hash. Operator's commit preserved beneath. [INFERENCE] The reportable hash is `pushed`, not `committed` — helper output already distinguishes them.

### Step 5 — lane git-touching checks

Registry (SKILL.md:528-545): git-on-lane-repo consumers are the `measure.py` probes (`git -C REPO rev-parse/show/ls-tree`); `mado-verify.sh` only invokes git against the *omarchy* checkout (`describe --exact-match`, `rev-parse`, `show` — never `status`/`fetch` by design, SKILL.md:3262), and `--selftest` is hermetic.

| check | colocated lane exit | plain-clone exit | colocation delta |
|---|---|---|---|
| `python3 .ufo/waves/round-14/measure.py HEAD` | 0 | 0 | none |
| `python3 .ufo/waves/round-15/measure.py HEAD` | 0 | 0 | none |
| `python3 .ufo/waves/round-16/measure.py HEAD` | 0 | 0 | none |
| `bash tools/mado-verify.sh --selftest` | 0 (`MADO_SELFTEST: 372/372 assertions passed`) | — | hermetic; unaffected |

Plain-clone baseline used the `operator/` clone (no `.jj`). Zero failures attributable to colocation.

## PASS/FAIL table

| step | result | evidence |
|---|---|---|
| 2 helper init | PASS | state line above; config readback; HEAD attached; porcelain unchanged |
| 3 auto-track contrast | PASS (hazard quantified) | 105 files → `@` and staged `A` in git; 2 MiB file refused; 0.032 s snapshot |
| 4 commit/push/invariants | PASS | identity, ancestry, ahead=0, remote tip, scratch intact — all verified |
| 4 race recovery | PASS | fetch+rebase retry; pushed `544fbe8` above `ca766aa`; remote commits untouched |
| 5 lane checks | PASS | 3 probes exit 0 in both trees; selftest 372/372; no colocation-caused failure |

## Colocation hazards specific to this lane

- **Unignored `.ufo/` growth is the top risk.** `.gitignore` covers only `.ufo/interactive-sessions/`. `.ufo/waves/round-17/` carried **105 untracked files** mid-round — under default `snapshot.auto-track` all 105 enter `@` and become staged `A` entries (measured, step 3). The helper's `none()` init plus pathspec-limited commits prevents this; nothing else does.
- **`git add` staging is silently destroyed.** `git add scratch-jjtrial.txt` → `jj status` keeps `A ` staged; `jj describe` (a real mutation) → `A ` becomes `??`, `git diff --cached` empty. Seats staging with git then running any mutating jj command lose the index. Mitigation already in helper: `jj file track <paths>` inside `commit` replaces the git-add idiom; document that lane seats must not `git add`.
- **Detached HEAD after every mutation.** `HEAD` attached post-init, detached on `@` post-commit; `git rev-parse '@{u}'` → `fatal: HEAD does not point to a branch`. Any lane tooling using `@{u}`/`HEAD` symbolic-ref breaks; `git rev-parse <branch>` works (helper `detect_branch` handles it; measure probes unaffected — they take explicit REV args).
- **`.ufo/state/` not ignored and not covered.** `git check-ignore .ufo/state/x` → no match; dir absent today. If a seat writes `.ufo/state/` it will be a `??` swarm like round-17. Protocol says never commit it — add the ignore rule.
- **Big files:** only ignored content exceeds 1 MiB (1.65 MB JSONL). Any *unignored* >1 MiB scratch would be refused by jj's `max-new-file-size` under `all()` — fine, but leaves it as durable `??` noise.
- **None of:** nested `.git` dirs, symlinks in worktree, `.gitattributes`/LFS (none; git-lfs binary exists but repo has no attributes), active git hooks, generated dirs outside `.ufo/`. Clean profile.
- **`@` author identity:** init leaves `@` authored by the operator until first mutation; helper `commit` sets author+committer per-command (verified `mado-shokunin` on both). Cosmetic on the empty working-copy commit only.

## Recommendations

1. Adopt `jj-lane.sh` for `mado` lane writes — all five steps pass with zero colocation-caused failures.
2. Add to `mado-shokunin/.gitignore`:
   ```
   .ufo/state/
   ```
   (keep `.ufo/interactive-sessions/`). This narrows the `??` surface and closes the never-commit-`.ufo/state` invariant at the ignore layer rather than by convention.
3. Fleet doc note: lane seats must not `git add` — staged entries vanish on any jj mutation; use `jj file track` (as the helper does) or rely on the helper's pathspec commit.
4. No per-lane jj config beyond what `init` already sets is needed for `mado`; repo config `snapshot.auto-track="none()"`, lane identity, and `trunk()="master@origin"` are confirmed correct.
5. Tooling: no installs performed — jj 0.45.1 and git-lfs 3.8.0 already present; pacman paused host-wide per operator note (no transaction attempted).

## Sandbox

`/fast/scratch/jj-wave/JjTrialMado/` removed after the run — nothing it held is cited as a failure. No live repo was mutated; all jj ran under the sandbox.
