# JjTrialKotoba — jj colocation trial for lane `kotoba`

Seat: `JjTrialKotoba-2`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (branch `master`, remote `github.com/VeigaPunk/kotoba-shokunin`). jj 0.45.1 at `~/.local/bin/jj`, git 2.56.0. All jj work ran in `/fast/scratch/jj-wave/JjTrialKotoba/`; the live repo was only read (`git -C … log|ls-files|check-ignore|status`).

## Step 1 — sandbox build

Commands (exact, all ran clean):

```
git clone --bare /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/jj-wave/JjTrialKotoba/remote.git
git clone /fast/scratch/jj-wave/JjTrialKotoba/remote.git /fast/scratch/jj-wave/JjTrialKotoba/lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/kotoba-shokunin/ /fast/scratch/jj-wave/JjTrialKotoba/lane/
git -C /fast/scratch/jj-wave/JjTrialKotoba/lane remote -v   # origin -> sandbox remote.git, verified before any push
```

Observed:

- `git -C lane status --porcelain | wc -l` → **0**. Also `0` in the live repo. Everything overlaid is either tracked-clean or gitignored.
- `git status --porcelain --ignored` → **1** entry: `!! .ufo/interactive-sessions/` (the whole ignored tree; 2 files inside).
- 10 largest untracked-or-ignored files — the ignored population is only 2 files, both under `.ufo/interactive-sessions/`:
  - `1 586 302 B` `.ufo/interactive-sessions/20261015T050057Z/2026-10-15T05-04-01-070Z_01a13df2-…aa7.jsonl`
  - `727 810 B` `.ufo/interactive-sessions/20261015T050057Z/…/__advisor.jsonl`
- Largest **tracked** files (lane hazard surface): `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt` **47 815 579 B**, `.ufo/round-46/evidence/g1/final5/gate-battery.json` 1 908 226 B, `LOG.md` 425 KB. `git ls-files` total = **10 016** files; **6 039 symlinks** (0 broken), all under `.ufo/round-*/drafts/…/verifiers` test-case trees.

## Step 2 — helper init

Command:

```
HYAKU_STATE=/fast/scratch/jj-wave/JjTrialKotoba/state scripts/hyaku/jj-lane.sh init /fast/scratch/jj-wave/JjTrialKotoba/lane kotoba
```

Observed output (exit 0):

```
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `master@origin`.
…
state branch=master local=c61a973… remote=c61a973… ahead=0 behind=0 head=attached tracked=0 untracked=0
```

- State line: `ahead=0 behind=0 head=attached tracked=0 untracked=0`.
- Init warnings: two "Warning: This setting will only impact future commits. The author of the working copy will stay 'Joao Pedro Veiga <jpveigao10@gmail.com>'" (from the two `config set user.*` calls) — benign; helper's `metaedit --update-author` fixes @ at commit time (verified in step 4).
- Repo config confirmed: `jj config list --repo` → `snapshot.auto-track="none()"`, `user.name="kotoba-shokunin"`, `user.email="kotoba@shokunin.local"`, `revset-aliases."trunk()"="master@origin"`.
- **Config location discovery**: `jj config path --repo` → `/home/vgpnk/.config/jj/repos/<config-id>/config.toml`. jj 0.45.1 writes repo config OUTSIDE the repo, keyed by `.jj/repo/config-id`. Copying the repo (step 3) prints "Your repo appears to have been copied … The corresponding repo config file has also been copied" and jj auto-derives a fresh config-id — copying preserves config, but the config does NOT live under `.jj/` and would not survive a naive `rm -rf`-and-reinit or an unrelated host.
- `git symbolic-ref -q HEAD` → `refs/heads/master` — HEAD still attached after init.
- `git status --porcelain` after init → 0 (diff vs step-1 capture: identical, `PORCELAIN UNCHANGED`).
- `jj status` timing (bash `date +%s%N` deltas; `/usr/bin/time` absent on host): run1 **17 ms**, run2 **12 ms**, run3 **11 ms**. With `auto-track="none()"` the snapshot never hashes the 6k-symlink `.ufo/` tree.

## Step 3 — auto-track `all()` alternative

Commands:

```
cp -a lane lane-autotrack
jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'
jj status            # timed
dd if=/dev/urandom of=scratch-tmp/bigfile.bin bs=1M count=2
jj status            # timed
echo scratch > scratch-tmp/small.txt && jj status
```

Observed:

- Baseline snapshot under `all()`: **15 ms**, "The working copy has no changes." **auto-track does NOT override .gitignore** — the 1.58 MB `interactive-sessions` jsonl stayed untracked. Nothing would be snapshotted on this lane because there are zero unignored untracked files.
- 2 MiB unignored scratch file → refusal (exit still 0, file left `?` untracked):
  ```
  Warning: Refused to snapshot some files:
    scratch-tmp/bigfile.bin: 2.0MiB (2097152 bytes); the maximum size allowed is 1.0MiB (1048576 bytes)
  ```
- Small unignored file auto-tracks instantly (28 ms) and git sees it as ` A` intent-to-add — the documented " A pollution" hazard, on this lane only reachable via unignored scratch.
- Snapshot times: 15 ms (clean), 12 ms (with refused file), 28 ms (tracked small file). No snapshot-cost hazard on this lane even under `all()` — the win from `none()` is safety, not speed.

## Step 4 — round-commit simulation

Prep: appended line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left `seat-scratch.txt` untracked.

Command:

```
HYAKU_STATE=$S/state scripts/hyaku/jj-lane.sh commit $S/lane --as kotoba -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
```

Output: `committed f38cbafaf64976408a73f8e6fea8022e55dbe055` / `pushed f38cbafaf64976408a73f8e6fea8022e55dbe055`, exit 0.

Verifications (all observed):

| Check | Result |
|---|---|
| `git log -1 --format` | author=`kotoba-shokunin <kotoba@shokunin.local>`, committer identical |
| `git log -1 --format=%H -- LOG.md` | `f38cbafa…` = pushed hash |
| `git merge-base --is-ancestor f38cbafa master` | exit 0 |
| helper `state` | `ahead=0 behind=0 head=detached tracked=0 untracked=1` (the 1 = seat-scratch) |
| `remote.git log` | tip `f38cbafa … kotoba-shokunin round-999: jj trial` |
| `seat-scratch.txt` | still `??`, content intact |
| `git symbolic-ref HEAD` | detached (expected post-mutation); `git rev-parse master` works |

Operator-push recovery: second clone `operator/` pushed `c80d1b7` ("operator: add considerthese note") to sandbox master. Helper commit of `corpus/lessons/round-999-jjtrial.md` printed:

```
committed 70b8452f966cc76a28a9648d1873aa2fd247d382
pushed    6d8f0fabde9a8fe8b6564b4d5c7d311e1c4a2647
```

`committed` ≠ `pushed` — the fetch+rebase rewrote the local commit (correct: only the unpushed commit, hash reported post-push). Remote history after: `6d8f0fa → c80d1b7(operator) → f38cbaf → c61a973`; `git merge-base --is-ancestor c80d1b7 master` → 0; helper `state` → `ahead=0`. Recovery works exactly as designed.

## Step 5 — lane git-touching gates

No `tools/` or `scripts/` in the lane; git users are in `verifiers/` (`git ls-files`, `cat-file -e`, `rev-parse`, `clone --no-hardlinks`, `checkout --detach`, `git add`). Ran three, 300 s timeouts, sandbox only:

| Gate (command vs `$S/lane`) | jj-lane exit | plain-git control exit | Classification |
|---|---|---|---|
| `python3 verifiers/verify_corpus_integrity.py --repo $S/lane --json` | **1** | **1** (identical verdicts) | Pre-existing/content, not colocation |
| `python3 verifiers/verify_corpus_independent.py --repo $S/lane --json` | **1** | **1** | Same |
| `bash verifiers/fault_injection_corpus.sh --repo $S/lane` | **1** | **1** (identical verdict grid) | Same |

Detail: integrity reports exactly 2 DRIFTs — `corpus.index.tracked_files 60→58` and `corpus.index.unindexed 2→0`. The two unindexed files are `corpus/lessons/round-46-verifier-spotcheck.md` (**committed at live HEAD `c61a973` by the integrator without a README index row — pre-existing failure before any jj involvement**) and my `round-999-jjtrial.md`. `fault_injection_corpus.sh` fails on `fault-0-control | FAIL-control-dirty` for the same reason; every downstream verdict is byte-identical between jj and plain worlds, including `git clone --no-hardlinks` out of the colocated `.git` and `checkout --detach` — both work fine under colocation. `verify_corpus_independent` resolved `head=6d8f0fa` via `rev-parse --short HEAD` on the detached HEAD and all 29 `cat-file -e <hex>^{commit}` citation checks passed.

## PASS/FAIL table (steps 2–5)

| Step | Check | Verdict |
|---|---|---|
| 2 | helper init, exit 0, state line correct | PASS |
| 2 | HEAD attached after init | PASS |
| 2 | porcelain unchanged by init | PASS |
| 2 | repo config set (auto-track/identity/trunk) | PASS (but see config-location finding) |
| 3 | auto-track=none avoids all snapshot tracking | PASS; `all()` refused 2 MiB file, auto-tracked 5-byte file as ` A` |
| 4 | committed/pushed hashes, lane identity, ancestor, ahead=0, remote, scratch intact | PASS (all sub-checks) |
| 4 | fetch+rebase recovery after operator push | PASS |
| 5 | gates behave identically jj vs plain git | PASS — all failures reproduced in plain control |

## Colocation hazards specific to `kotoba`

1. **Symlink forest**: 6 039 symlinks under `.ufo/round-*/drafts/` (0 broken). Harmless under `auto-track="none()"` (11–17 ms status); under `all()` still only 15–28 ms, but each snapshot re-stats them — cost is latent if the draft tree grows.
2. **Big tracked files**: 47.8 MB `omp-live-18.12.2-strings.txt` and ~2 MB `gate-battery.json` are already tracked. `max-new-file-size` only gates NEW files, so edits to them are fine; but if such a file is ever deleted and re-created, `file track`/`auto-track` will refuse at 1 MiB — the helper's `--include-ignored` path also bypasses the limit ONLY for files named literally (good).
3. **Ignored dir with >1 MiB content**: `.ufo/interactive-sessions/` (1.58 MB jsonl). `jj file track <dir>` (directory form) skips ignored content — verified live. `file track <file>` WITH `--include-ignored` would admit it; the helper only applies `--include-ignored` to non-directory args, so a pathspec naming the jsonl directly WOULD commit it. Recommend keeping `.ufo/interactive-sessions/` in `.gitignore` (already is).
4. **`git add` staging destroyed by jj mutations**: verified — `git add staged-probe2.txt` then one `jj-lane.sh commit` → file back to `??`, entry gone from index (content intact). Plain `jj status` alone did NOT destroy staging (file stayed `A `). Any gate/script mixing `git add` with jj commits races; `fault_injection_corpus.sh` clones worlds so its `git add` is unaffected.
5. **Detached HEAD after mutations**: `@{u}` → "fatal: HEAD does not point to a branch"; `git rev-parse master` fine. Gate `verify_corpus_independent` reads `rev-parse --short HEAD` and gets the working-copy commit hash, not the branch tip — for cited-hash purposes always use `git rev-parse <branch>`.
6. **Repo config lives outside the repo** (`~/.config/jj/repos/<id>/config.toml`, keyed by `.jj/repo/config-id`): `cp -a` triggers jj's "repo copied" handling and re-keys correctly (verified), but a `tar`-style archive or `rm -rf .jj` loses the auto-track/identity/trunk config entirely.
7. **No nested .git, no .gitattributes/LFS, no hooks** — none of those hazard classes present.
8. **`.ufo/state/` absent in this lane** and NOT gitignored; if a driver ever writes it here, nothing stops it being untracked-visible, but the helper's pathspec guard (`.ufo/state/*` → exit 64) covers it.

## Recommended per-lane config/ignore additions

1. **No `.gitignore` changes required** for kotoba: zero unignored untracked files, ignored dir already correct. [INFERENCE: adding `.ufo/state/` to `.gitignore` would be harmless belt-and-suspenders but is currently unnecessary.]
2. **Per-lane config is already optimal**: `snapshot.auto-track="none()"`, `trunk()=master@origin`, lane identity — all confirmed effective. Keep `max-new-file-size` at default 1 MiB so oversized new evidence files surface as explicit `file track` decisions.
3. **Operational**: fleet tooling reading "current commit" should use `git rev-parse master` (not HEAD/`@{u}`) once the lane is colocated; any caller relying on `git add`-staged state across a lane commit must stop staging or restage after.

## Blockers / notes

- `/usr/bin/time` absent on host — used `date +%s%N` deltas instead.
- Pre-existing lane bug (not mine to fix): `c61a973` landed `corpus/lessons/round-46-verifier-spotcheck.md` without a `corpus/README.md` index row, so `verify_corpus_integrity.py` is already red at live HEAD. The next real round must index it (and my `round-999` file exists only in the sandbox remote).
- No installs needed; no tools updated. Sandbox left at `/fast/scratch/jj-wave/JjTrialKotoba/` (contains the pushed-history evidence: `lane`, `lane-plain`, `lane-autotrack`, `lane-pristine`, `operator`, `remote.git`).
