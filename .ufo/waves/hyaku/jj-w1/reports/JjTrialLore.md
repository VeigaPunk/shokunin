# JjTrialLore — jj colocation trial for lane `lore`

Sandbox: `/fast/scratch/jj-wave/JjTrialLore/` (lane clone `lane/`, bare `remote.git`, `lane-autotrack/`, `operator/`, `plain/`). jj 0.45.1 at `~/.local/bin/jj`. No installs performed.

## Step 1 — sandbox build

Commands:
```
git clone --bare /home/vgpnk/Projects/shokunin/lore-shokunin /fast/scratch/jj-wave/JjTrialLore/remote.git
git clone /fast/scratch/jj-wave/JjTrialLore/remote.git /fast/scratch/jj-wave/JjTrialLore/lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/lore-shokunin/ /fast/scratch/jj-wave/JjTrialLore/lane/
```

Observed:
- `git -C lane status --porcelain | wc -l` → **1** (`?? .scratch/`).
- Untracked files: **26** (`git ls-files -o --exclude-standard | wc -l`); ignored: **129**.
- 10 largest untracked/ignored files (`du -b`, sorted desc):
  ```
  2198308  .ufo/interactive-sessions/20261015T050057Z/…/__advisor.jsonl   (ignored)
  1660925  .ufo/interactive-sessions/20261015T050057Z/….jsonl             (ignored)
   34095   .scratch/v26/scratch-root/corpus/tools/dependency-freeze-contract.json
   34095   .scratch/V02/scratch-root/corpus/tools/dependency-freeze-contract.json
   30142   .scratch/v26/scratch-root/corpus/tools/dependency_freeze.py
   30142   .scratch/V02/scratch-root/corpus/tools/dependency_freeze.py
   26644   v05-self-test-scratch/redemo/corpus/tools/dependency_freeze.py   (ignored)
   26644   v05-self-test-scratch/c1probe2/selfneutral-now/…/dependency_freeze.py
   26644   v05-self-test-scratch/c1probe2/legacypin-now/…/dependency_freeze.py
   26644   v05-self-test-scratch/c1probe/selfneutral-now/…/dependency_freeze.py
  ```
  Largest tracked file: `LOG.md` at 810,268 B. The two >1 MiB files are both under ignored `.ufo/interactive-sessions/`; **no un-ignored file exceeds jj's default `snapshot.max-new-file-size` (1 MiB)**.
- `git remote -v` in `lane/` → `origin /fast/scratch/jj-wave/JjTrialLore/remote.git` (confirmed sandbox-only before any push).

## Step 2 — colocate via helper

Command: `HYAKU_STATE=/fast/scratch/jj-wave/JjTrialLore/state jj-lane.sh init lane lore` → exit 0.

- Helper state line:
  ```
  state branch=main local=01306d51252f… remote=01306d51252f… ahead=0 behind=0 head=attached tracked=0 untracked=1
  ```
- Init warnings (stderr): twice `Warning: This setting will only impact future commits. The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>".` — cosmetic; the helper re-stamps author at commit time via `metaedit --update-author` (verified in step 4).
- Repo config set (`jj config list --repo`):
  ```
  revset-aliases."trunk()" = "main@origin"
  snapshot.auto-track = "none()"
  user.name = "lore-shokunin"
  user.email = "lore@shokunin.local"
  ```
- `git symbolic-ref -q HEAD` → `refs/heads/main` (attached) after init.
- `git status --porcelain` after init → identical to step 1 (`?? .scratch/`, count 1). No intent-to-add entries.
- `jj status` timing ×3: **8 ms, 8 ms, 7 ms**. Output shows `? .scratch/` untracked, `@` empty.

## Step 3 — default auto-track alternative

```
cp -a lane lane-autotrack && cd lane-autotrack
jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'
jj status   # timed: 29 ms total including the snapshot
```
- `jj --ignore-working-copy diff --summary -r @ | grep -c '^A '` → **26** files swept into `@` (all of `.scratch/`: duplicated fixture trees, `poll.sh`, `poll.log`).
- `new file too large` refusals: **none** — every un-ignored untracked file is < 1 MiB; the 1.6–2.2 MiB interactive-session files are gitignored and respected by jj.
- Side note: `cp -a` of a `.jj` dir works but jj warns `repo appears to have been copied … The corresponding repo config file has also been copied` (harmless in sandbox; would matter if anyone cloned a live lane by copying).

## Step 4 — round-commit simulation

Prepared: appended a line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left `scratch-untracked-jjtrial.txt` untracked.

```
jj-lane.sh commit lane --as lore -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 33d08cd461190b3617fec6a14a419cb030534d03
→ pushed    33d08cd461190b3617fec6a14a419cb030534d03   exit 0
```

Verified:
- `git log -1 --format='author…committer…'` → `author=lore-shokunin <lore@shokunin.local>`, `committer=lore-shokunin <lore@shokunin.local>` — both identities stamped.
- `git log -1 --format=%H -- LOG.md` → `33d08cd…` == pushed hash.
- `git merge-base --is-ancestor 33d08cd… main` → exit 0.
- `git show --stat` → exactly `LOG.md | 2 ++` and `corpus/lessons/round-999-jjtrial.md | 3 +++`. Pathspec-limited.
- `jj-lane.sh state` → `ahead=0 behind=0 head=detached untracked=2`.
- Sandbox remote: `git -C remote.git log -1 main` → `33d08cd… lore-shokunin round-999: jj trial`.
- `cat scratch-untracked-jjtrial.txt` → `do-not-commit-me`; still `??` in git status.
- HEAD now **detached** at `33d08cd…` (the `@-` position); `git rev-parse @{u}` → `fatal: HEAD does not point to a branch` while `git rev-parse main` works.

**Operator-push recovery:** second clone `operator/` committed+pushed `considerthese/op-file.md` (tip `fe9754b…`). Then:
```
jj-lane.sh commit lane --as lore -m "round-999b: jj trial after operator push" -- LOG.md corpus/lessons/round-999b-jjtrial.md
→ committed 314dea897a2c73daf71f756986f780b74c5921a2
→ pushed    89188c4b5ab6904952cff7e78ff0b5b1d2d3d751   exit 0, ~1.3 s
```
- `committed` ≠ `pushed`: the rejected push triggered fetch + rebase of the one unpushed commit onto `main@origin`, minting `89188c4b`. The helper prints the pushed (citeable) hash — reports must cite `pushed`, not `committed`.
- Remote log: `89188c4b` → `fe9754b` (operator) → `33d08cd`. `git merge-base --is-ancestor` confirms both ancestors; pushed commit contains only `LOG.md | 1 +` + `round-999b | 1 +`. `state` → `ahead=0`.

**Index-reset probe (extra):** `git add git-staged-probe.txt` (shown `A `), then a helper commit of `LOG.md` → after the jj mutation the file is `??` again — **jj resets the git index on every mutation; staged content silently becomes untracked**. Probe commit pushed `d1a9242b` containing only `LOG.md | 1 +`.

## Step 5 — lane's git-touching checks

Lane SKILL.md registers 5 gates in `corpus/tools/`. Only three invoke git: `boundary_doc_check.py` (`git show`/`git ls-tree` of pinned revisions), `discriminate_check.py` (`git show e97613c:…`), `dependency_freeze.py` (`git rev-parse HEAD` inside `--freeze`). `map_obligations.py` (no git) run as a control; `support_check.py` shells out to `grep` only — skipped.

| Check | Colocated lane/ | Plain clone (no jj) | Colocation-caused? |
|---|---|---|---|
| `python3 corpus/tools/boundary_doc_check.py --self-test` | exit 0 — `SELF-TEST PASS` (8/8 cases) | exit 0 — `SELF-TEST PASS` | no |
| `python3 corpus/tools/discriminate_check.py` | exit 0 — `DISCRIMINATION HELD` | exit 0 — identical | no |
| `python3 corpus/tools/map_obligations.py --self-test` | exit 0 — `RESULT PASS` (25/25) | not rerun (no git usage) | no |
| `python3 corpus/tools/dependency_freeze.py --self-test` | exit 0 — `SELF-TEST 19/19 RESULT PASS` | exit 0 — `SELF-TEST 19/19` | no |

No colocation-attributable failure found. Residual note: `dependency_freeze.py --freeze` records `git rev-parse HEAD` as the pin revision. In a colocated repo HEAD is detached at `@-`; the hash currently equals the branch tip, so freezing still records a real pushed commit — but it is one mutation away from recording an unpushed `@`/`@-` position. Not exercised (freeze mutates the contract); flagged for the pin contract rather than observed breakage.

## PASS/FAIL table

| Step | Result |
|---|---|
| 2 helper init: config set, HEAD attached, status unchanged, jj status ≤ ~10 ms | PASS |
| 3 auto-track=all(): 26 files swept, no size refusal, 29 ms | PASS (measured) |
| 4 helper commit+push: lane identity, pathspec-limited, ancestor of main, ahead=0, remote updated, scratch intact | PASS |
| 4 operator-push recovery: fetch+rebase, pushed≠committed correctly reported | PASS |
| 5 lane gates: 4/4 exit 0, identical in plain clone | PASS |

## Colocation hazards specific to `lore`

1. **Untracked `.scratch/` tree (26 files)** — the lane's only un-ignored untracked dir. With default jj auto-track it silently enters `@` (measured). `snapshot.auto-track="none()"` in the helper prevents this; the `.gitignore` does not cover `.scratch/` (only `*-self-test-*/` and `.ufo/waves/**/*-scratch/`).
2. **No oversized un-ignored files** — the only >1 MiB working-tree files live under ignored `.ufo/interactive-sessions/` (2.2 MB `__advisor.jsonl`, 1.7 MB session `.jsonl`). `jj file track --include-ignored` in the helper only applies to explicitly named files, so a commit path naming one of these would track it — that's by design, but lane seats should never pass `.ufo/interactive-sessions/` paths to the helper.
3. **Detached HEAD post-mutation** — `git rev-parse @{u}` fails; `git status -sb` shows `## HEAD (no branch)`. Only `dependency_freeze.py --freeze` reads HEAD in this lane; it would record whatever `@-` is. Fleet tooling must use `git rev-parse <branch>` / `refs/heads/main`, never `@{u}` or bare `HEAD`.
4. **Index reset** — jj wipes `git add` staging on every mutation (measured above). Lane seats must never rely on git staging; always commit through the helper pathspec.
5. **committed ≠ pushed on rejection** — after a competing remote push the helper's `committed` line is a pre-rebase hash; only `pushed` is citeable (measured: `314dea89` vs `89188c4b`).
6. **No nested .git dirs, no symlinks, no hooks, no .gitattributes/LFS** in the live tree (`find` + `ls .git/hooks` empty of non-samples). `.jj/` needs no ignore rule — git natively ignores it via `.jj/.gitignore` (`/*`), confirmed `git check-ignore -v .jj/repo` → `.jj/.gitignore:1`.
7. `LOG.md` is 810 KB and grows append-only; `jj file track` + `jj commit LOG.md` took <2 s each round-trip — no perf issue at current size.

## Recommended per-lane config / ignore additions

- **Keep** helper-set `snapshot.auto-track="none()"`, `trunk()=main@origin`, lane identity — sufficient as shipped.
- **Add `.scratch/` to `.gitignore`** (or rename seat scratch to `*-self-test-*/`): it is the only un-ignored untracked content; ignoring it hardens the lane against any future `auto-track=all()` drift and keeps `jj status`/`git status` clean.
- **Lane code change (optional, bounded):** in `dependency_freeze.py:429` prefer `git rev-parse refs/heads/main` (or `@{u}`-fallback) so `--freeze` pins record the branch tip, not the detached `@-` working-copy parent.
- Document "cite `pushed`, never `committed`" in lane reporting docs; `state`'s `head=detached` is normal colocated state, not an error.

## Inference and risks

- [INFERENCE] `git rev-parse HEAD` in a colocated repo returns the `@-` hash, which equals the branch tip only because the helper re-points the bookmark after each commit; a seat that snapshots without committing (e.g. bare `jj status` after edits) would leave `@` as a fresh unreferenced commit — `HEAD` then resolves to the last real commit, still safe for reads, but any `git commit` run directly would orphan work onto detached HEAD.
- [INFERENCE] Self-test scratch dirs created under the repo root by `--self-test` modes matched the existing `*-self-test-*/` ignore rule (e.g. `v05-self-test-scratch` appears ignored, not `??`), so gate runs do not pollute the jj working copy.
- Risk: a live lane with pre-existing `.jj` from earlier trials would get the helper's `warn: working-copy commit @ already tracks N added path(s)` — the init warns but does not untrack; cleanup is a lane decision (helper leaves it intact by design).
- Risk: `cp -a`/`rsync -a` copies of a colocated lane carry `.jj/` state — the remote-tracking bookmarks inside travel with it (observed warning). Fleet tooling that backs up lanes should exclude `.jj` or re-run `jj-lane.sh init` (idempotent, skips `.jj` when present).
