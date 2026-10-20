# JjTrialTameshi — jj colocation trial for lane `tameshi`

Seat: JjTrialTameshi-2 · jj 0.45.1 (`~/.local/bin/jj`) · sandbox `/fast/scratch/jj-wave/JjTrialTameshi/` (removed on completion) · helper `scripts/hyaku/jj-lane.sh` read-only.

No tools installed (jj 0.45.1 already present; git/rsync/flock host-provided). No live-repo mutations; live repo read via `git clone --bare` + `rsync` only.

## Step 1 — sandbox build

Commands:

```
git clone --bare /home/vgpnk/Projects/shokunin/tameshi-shokunin /fast/scratch/jj-wave/JjTrialTameshi/remote.git
git clone remote.git lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/tameshi-shokunin/ lane/
```

Observed:

- `git -C lane status --porcelain | wc -l` → **21** (7 ` M`, 14 `??`); with `--ignored` → 22 (one `!! .ufo/interactive-sessions/`).
- `git remote -v` → `origin /fast/scratch/jj-wave/JjTrialTameshi/remote.git` (confirmed before any push).
- 10 largest untracked-or-ignored entries:

```
2746481  .ufo/interactive-sessions/          (ignored dir, contains one 1.8 MB .jsonl)
 824290  .ufo/waves/round-16/w2/             (untracked dir)
 344142  .ufo/waves/round-16/spawn2.json
 108034  .ufo/waves/round-16/dispatch2.json
  87475  .ufo/waves/round-16/spec2.json
  24185  .ufo/evidence/round-16/measure-repair/
   9461  .ufo/evidence/round-16/coldread/anchor-check.txt
   9395  .ufo/waves/round-16/record2.json
   8790  .ufo/evidence/round-16/coldread/anchor-check.py
   5809  .ufo/evidence/round-16/round-gate/survivor-probes/c1059-probe.sh
```

The modified tracked files are rsync'd uncommitted live work (SKILL.md, LOG-adjacent corpus/tools edits) — the trial deliberately inherited them.

## Step 2 — colocate through the helper

Command:

```
HYAKU_STATE=/fast/scratch/jj-wave/JjTrialTameshi/state scripts/hyaku/jj-lane.sh init lane tameshi
```

Output (excerpt):

```
Done importing changes from the underlying Git repo.
Setting the revset alias `trunk()` to `master@origin`.
Initialized repo in "."
Warning: This setting will only impact future commits.
The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>".
To change the working copy author, use "jj metaedit --update-author".   (×2)
state branch=master local=c699c8c… remote=c699c8c… ahead=0 behind=0 head=attached tracked=7 untracked=14
```

- Init warnings: the two "working copy author stays Joao Pedro Veiga" notices (expected; `@`'s author is stamped later by `metaedit --update-author` inside `commit`). No "already tracks N added paths" warning — the first snapshot ran with `auto-track="none()"`.
- Repo config after init (`jj --ignore-working-copy config list --repo`):

```
revset-aliases."trunk()" = "master@origin"
snapshot.auto-track = "none()"
user.name = "tameshi-shokunin"
user.email = "tameshi@shokunin.local"
```

- `git symbolic-ref -q HEAD` → `refs/heads/master` (attached) right after init.
- `git status --porcelain` → still 21 lines, byte-identical set to step 1 (every untracked path still `??`).
- `jj status` ×3: **11 ms / 10 ms / 10 ms** (1280 files on disk outside .git/.jj).

## Step 3 — default auto-track alternative

`cp -a lane lane-autotrack`, then `jj config set --repo snapshot.auto-track '"all()"'` + `jj status`.

- jj snapshotted **82 added paths** into `@` (`jj diff --summary -r @ | grep -c '^A '`) in **54 ms**.
- **No `new file too large` refusals** — the only >1 MiB file sits inside the *ignored* `.ufo/interactive-sessions/` and jj honored `.gitignore` (0 matches for `interactive` in the @ diff).
- Side effect on git's view: `git status --porcelain` flipped all 82 entries plus one modified-file line to intent-to-add (` A`) — **83 staged-looking entries**. This confirms the documented "default snapshot tracks every untracked file, git shows ` A`" hazard: under `all()`, seat scratch silently becomes jj-tracked and git-staged.
- Note: `cp -a` of a live `.jj` repo prints "repo appears to have been copied" — a cosmetic warning only.

## Step 4 — simulated round commit

Prep: appended one line to LOG.md, created `corpus/lessons/round-999-jjtrial.md`, left `scratch-jjtrial.txt` untracked.

```
jj-lane.sh commit lane --as tameshi -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 7821a8c7ace5bf08a1dc58a94cbf472499df3380
  pushed    7821a8c7ace5bf08a1dc58a94cbf472499df3380   (exit 0)
```

Verifications (all in sandbox):

| Check | Result |
|---|---|
| `git log -1 --format='%an <%ae> / %cn <%ce>'` | `tameshi-shokunin <tameshi@shokunin.local>` for **both** author and committer |
| `git log -1 --format=%H -- LOG.md` | `7821a8c7…` == pushed hash |
| `git merge-base --is-ancestor 7821a8c7 master` | exit 0 |
| `jj-lane.sh state` | `local=7821a8c7 remote=7821a8c7 ahead=0 behind=0 head=detached` |
| `git -C remote.git cat-file -t` / `rev-parse master` | `commit` / `7821a8c7…` |
| scratch file | still `?? scratch-jjtrial.txt`, content intact |
| HEAD | `git symbolic-ref -q HEAD` → exit 1 (**detached**, as predicted); `git rev-parse '@{u}'` → `fatal: HEAD does not point to a branch` |
| other uncommitted work | the 7 inherited ` M` files and 14 `??` paths all preserved |

Operator-push simulation: second clone committed `considerthese/jj-trial-operator.md` and pushed `ebc3b699…` to master. Then a second helper commit:

```
→ committed e8585fc3b49abcac82f4a2e72fb67660addb5841
  pushed    7cf8c52980fea6693d04e85c6f7e48a1677d6d23   (exit 0)
```

The push was rejected once; the helper fetched, rebased the unpushed commit onto the moved `master@origin`, and repushed. Verified: `git log` shows `7cf8c529`'s parent is `ebc3b699`; author stayed `tameshi-shokunin`; remote tip = `7cf8c529`; the pre-rebase `e8585fc3` **does not exist on the remote** (`cat-file` → fatal). Caveat: the helper prints `committed` before push — a report must cite the `pushed` line, which the helper already prints correctly.

## Step 5 — lane's own git-touching checks

Registry scan: `tools/` has 7 tools; only `mutate-and-run.sh`, `pin-disposition.py`, `bash-witness-study.py`, `context-capture.py` reference git, and `context-capture` *never executes git* (receipt re-derivation only — docstring line 8). All live-mode git gates target **sibling lane repos** at pinned commits (`git show <rev>:<path>`), never the tameshi lane itself. So I cloned the four siblings into a sandbox fleet root (`git clone <live-repo>`, worktrees included) and ran the real gates:

| Gate | Command (cwd = colocated lane) | Result |
|---|---|---|
| mutate-and-run selftest | `timeout 300 tools/mutate-and-run.sh --selftest` | `MUTATE_SELFTEST: 83/83 pass` / `VERDICT: PASS`, exit 0, 5.2 s |
| pin-disposition selftest | `python3 tools/pin-disposition.py --selftest` | `SELFTEST: PASS (18/18)`, exit 0 |
| pin-disposition live mode | `python3 tools/pin-disposition.py --manifest .ufo/evidence/round-13/pin-manifest.json --root /fast/scratch/jj-wave/JjTrialTameshi/fleet` | exit 0, `status: ok`; legs: `bash-surface-census`, `bash-checklist-run`, `js-claims-check` = `unchanged`; `js-kimi-census`, `bash-tsukuroi-census`, `bash-mado-verify` = `changed` (pre-existing upstream drift — sibling HEADs moved past round-13 pins, not a colocation effect) |

Colocation isolation run: colocated `fleet/kagi-shokunin` (`jj git init --colocate`, auto-track none) and re-ran the live-mode gate → **byte-identical output except `observed_at` timestamp**. Zero colocation-caused failures observed; no plain-clone control needed since output matched 1:1.

The tameshi lane itself being colocated is invisible to these gates: they run `git -C <sibling>` and `git rev-parse --show-toplevel`, `git show`, `cat-file`, lstat — none of which touch HEAD or the index.

## PASS/FAIL table

| Step | Item | Verdict |
|---|---|---|
| 2 | helper init, repo config, HEAD attached, porcelain unchanged, `jj status` 10–11 ms | PASS |
| 3 | auto-track=all() measurement: 82 files, 54 ms, no size refusals | PASS (as measurement; mode itself is hazardous) |
| 4 | commit identity, pathspec limit, pushed hash ancestor, remote synced, scratch intact, fetch+rebase recovery | PASS |
| 5 | 2 selftests + live-mode pin-disposition under colocation, incl. colocated sibling re-run | PASS |

## Colocation hazards specific to this lane

1. **`.ufo/` is the hot untracked surface** (observed 21/22 status lines under `.ufo/`). `.ufo/waves/`, `.ufo/evidence/` are written constantly by the driver; most is untracked on purpose. Under `auto-track=all()` all of it enters `@` and git's index (82 files here). The helper's `none()` is load-bearing for this lane.
2. **Ignored 1.8 MB jsonl in `.ufo/interactive-sessions/`**: under `none()`, `jj file track` on a *named file* uses `--include-ignored` — committing a path inside an ignored dir silently admits it (verified: probe file tracked). `--include-ignored` also bypasses `snapshot.max-new-file-size`. Path discipline at commit-callsites is the only guard.
3. **No symlinks, no nested `.git`, no hooks, no `.gitattributes`/LFS** in this lane (verified by `find`/`ls .git/hooks`) — the cleanest hazard profile.
4. **Detached HEAD is permanent after the first mutation**: `@{u}` broken, `git rev-parse HEAD` still resolves. Anything in lane tooling using `@{u}`/`HEAD` symbolics would break — grep shows none does (all lane tools take explicit `<rev>` pins).
5. **`git add` staging semantics shift**: a staged file survives `jj status` as ` A` but is absorbed into `@`; after a pathspec-limited `jj commit` it reverts to `??` — so mixed `git add` + helper-commit workflows lose the staged set silently (verified: `staged-probe.txt` never reached `master`, ended as `??` again, content intact).
6. **jj leaves dangling objects** (`git fsck`: 3 dangling commits + blobs) — normal jj bookkeeping noise; a gate that treats fsck output as fatal would trip (none in this lane).
7. **`jj file track <dir>`** acts like `git add <dir>` but respects `.gitignore` for dirs — verified `interactive-sessions` stayed out. Still, any future `jj commit` *without* a pathspec would ship whatever is tracked; the helper always pathspec-limits.
8. LOG.md append-only and `.ufo/state/` no-commit are policy invariants, not VCS-enforced. `.ufo/state/` doesn't exist in this lane yet and isn't gitignored — a bare `jj file track .` / unpathed `jj commit` would admit it; the helper's pathspec-blocklist covers `.ufo/state/*` and `.ufo/watchdog.log`.

## Recommendations (per-lane)

- Keep `snapshot.auto-track="none()"` — mandatory here given the `.ufo/` scratch volume; `all()` absorbed 82 files in one snapshot.
- Add to `.gitignore`: `.ufo/state/` and `.ufo/watchdog.log` (defense-in-depth behind the helper's pathspec blocklist; costs nothing, closes the only never-commit surface that isn't yet ignored).
- Lane tooling needs no changes: every git-touching gate resolves sibling repos by explicit pinned commit (`git show <rev>:<path>`, `rev-parse --show-toplevel`) — colocation-transparent on both sides, verified byte-identical.
- Report convention: always cite the helper's `pushed` hash, never `committed` — they differ exactly when fetch+rebase fired.
- No per-lane jj config beyond what `init` already sets (`trunk()` alias, identity, auto-track). `snapshot.max-new-file-size` needn't change — nothing here exceeds 1 MiB outside the ignored dir.

[INFERENCE] The `changed` dispositions for `js-kimi-census`, `bash-tsukuroi-census`, `bash-mado-verify` are sibling-repo content drift past the round-13 pins (their lanes have advanced since); they reproduce identically on plain clones, so they're substrate truth, not jj effects. [INFERENCE] For lane-repo writes, tameshi is a low-risk adopter: small tree, no exotic filesystem features, all git gates rev-pinned rather than HEAD-dependent.
