# JjTrialRevenger — jj colocation trial for lane `revenger`

Live repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin` (branch `main`, remote
`https://github.com/VeigaPunk/shokunin-binary-forensics.git`).
Sandbox: `/fast/scratch/jj-wave/JjTrialRevenger/` — all jj/git mutation ran there only;
the live repo was touched by `git log|show|ls-files|rev-parse|status`, `grep`, `find`,
`cat`, and as a `git clone --bare` source. No pushes to a real remote; `origin` in the
sandbox pointed at `/fast/scratch/jj-wave/JjTrialRevenger/remote.git`.

Tool versions: `jj 0.45.1-7c41cdeb…` at `~/.local/bin/jj`, `git 2.56.0`. No installs or
updates were needed or made (helper + jj already present).

## Step 1 — sandbox build + overlay

```
git clone --bare /home/vgpnk/Projects/shokunin/revenger-shokunin remote.git
git clone remote.git lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/revenger-shokunin/ lane/
git -C lane status --porcelain | wc -l        → 0
git -C lane status --porcelain --ignored      → !! .ufo/interactive-sessions/
```

The live working tree is **clean**: zero untracked/modified, one ignored directory.
10 largest untracked-or-ignored files (only 3 exist, all inside the ignored dir):

| bytes | path |
|---|---|
| 1 482 003 | `.ufo/interactive-sessions/20261015T050057Z/…_01a13df2-….jsonl` |
| 667 434 | `.ufo/interactive-sessions/20261015T050057Z/…/__advisor.jsonl` |
| 1 390 | `.ufo/interactive-sessions/20261015T050057Z/…/9.bash-original.log` |

Note: the largest ignored file (1.41 MiB) exceeds jj's 1 MiB `max-new-file-size`, but it
is gitignored, so auto-track never offered it (verified in step 3).

## Step 2 — colocate via helper

```
HYAKU_STATE=…/state jj-lane.sh init lane revenger   → exit 0
  "Initialized repo in \".\"" · "Setting the revset alias trunk() to main@origin"
  warnings: "The author of the working copy will stay Joao Pedro Veiga <…gmail.com>"
            (×2 — expected; working-copy @ keeps host git author until a commit)
  state line: state branch=main local=cf02419… remote=cf02419… ahead=0 behind=0
              head=attached tracked=0 untracked=0
jj --ignore-working-copy config list --repo:
  revset-aliases."trunk()" = "main@origin"
  snapshot.auto-track = "none()"
  user.name = "revenger-shokunin"
  user.email = "revenger@shokunin.local"
git symbolic-ref -q HEAD   → refs/heads/main   (attached after init)
git status --porcelain | wc -l   → 0  (unchanged vs step 1)
git status --porcelain --ignored → !! .jj/   +   !! .ufo/interactive-sessions/
```

`.jj/` is ignored via an auto-written `.jj/.gitignore` containing `/*`
(`git check-ignore -v` → `.jj/.gitignore:1`), not via `.git/info/exclude` or the lane's
`.gitignore` — this is what keeps `git status` stable under colocation.

`jj status` timings from `lane/`: **9 ms, 8 ms, 8 ms** (bash `date +%s%N` deltas;
`/usr/bin/time` is not installed). Output: "The working copy has no changes."

## Step 3 — auto-track = "all()" comparison

`cp -a lane lane-autotrack` → jj warned "Your repo appears to have been copied from …"
(benign, observed). Set `snapshot.auto-track = "all()"` in that copy's repo config.

- Baseline `jj status` on clean+ignored tree: **0 files snapshot**, "no changes", 15 ms.
  `.ufo/interactive-sessions/` was **not** tracked despite being 2.1 MB total —
  ignored paths stay out even under `all()`.
- After planting `scratch-autotrack.txt` (7 B) + `bigfile.bin` (2 MiB random):
  - `scratch-autotrack.txt` tracked instantly (`A` in `jj diff --summary -r @`,
    appears in `git status --porcelain` as **` A` intent-to-add**).
  - `bigfile.bin` **refused**: "Refused to snapshot some files: bigfile.bin: 2.0MiB
    (2097152 bytes); the maximum size allowed is 1.0MiB (1048576 bytes)" — left `??`.
  - snapshot time 13 ms; steady-state `jj status` 9 ms.

## Step 4 — round-commit simulation (real helper)

Setup: appended line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`,
left `scratch-leaveme.txt` untracked.

```
jj-lane.sh commit lane --as revenger -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
  → committed 40335433b38b1fd2acfecd5e0147df101e51a484
  → pushed    40335433b38b1fd2acfecd5e0147df101e51a484   (exit 0)
```

Verification of `40335433`:
- `git show -s --format=…` → author **and** committer `revenger-shokunin <revenger@shokunin.local>` ✓
- `git log -1 --format=%H -- LOG.md` = `40335433…` = pushed hash ✓
- `git merge-base --is-ancestor 40335433 main` → exit 0 ✓
- `jj-lane.sh state lane` → `ahead=0 behind=0 head=detached tracked=0 untracked=1` ✓
- `git -C remote.git log -1 main` = `40335433…`; `cat-file -e` ok ✓
- `scratch-leaveme.txt` still `??`, content `leave me untracked` intact ✓
- HEAD became **detached at the pushed hash** after the jj mutation (expected colocation behavior).

### Operator-push recovery

Second clone `operator-push/` committed `considerthese/op-note.md` and pushed
(`34e1ec0f…`). Then, without fetching in `lane/`:

```
jj-lane.sh commit lane --as revenger -m "round-999: jj trial part 2" -- LOG.md
  → committed 7f94bad8391ec213d91aeb75a99543fc49e4b83d
  → pushed    73a6a62981e2bc328ccd68273318788dfda76759   (exit 0, wall 1.17 s)
```

The local commit was rebased onto the moved remote tip, so **committed ≠ pushed**
— the helper correctly reports/cites the pushed hash. Verified:
`73a6a629`'s parent is `34e1ec0f` (operator commit, author preserved as
`operator`), remote `main` = `73a6a629`, `merge-base --is-ancestor` holds, helper
state shows `ahead=0`, rebased commit still authored `revenger-shokunin`.

## Step 5 — lane git-touching checks

**Registry reality:** `SKILL.md` is **absent** in this lane (SHONEN.md lists it as
unchecked debt). No `tools/` or `scripts/` dir. Gate registry = two README replay
commands. Neither invokes git (`replay_scenarios.py` mentions git only in a help
string; `verify_named_multi_icon_states.py` uses `Path(__file__).resolve().parent`
— path-relative, VCS-agnostic). No lane script calls `git` at all — the closest to
"git-touching" checks are these filesystem verifiers, run in both the colocated
sandbox and a plain clone `lane-plain/`:

| command (300 s timeout) | colocated lane | plain clone |
|---|---|---|
| `python3 -B corpus/verify_named_multi_icon_states.py` | exit 0 — `PASS: 139 positive checks; 2/2 forged claims rejected` | exit 0 — identical output |
| `python3 -B reports/round-1/replay_scenarios.py` | exit 0 — `POSITIVES 3/3 · EXPECTED_REJECTIONS 6/6 · INPUTS 9/9 · RESULT PASS` | exit 0 — identical (differs only in embedded corpus path) |

Zero colocation-attributable failures; no pre-existing failures either. The scenario
battery exercises renames/copies of fixtures and left `git status --porcelain` =
just `?? scratch-leaveme.txt` afterwards.

## PASS/FAIL table

| check | result |
|---|---|
| 2 init exit 0, repo config = 4 expected keys | PASS |
| 2 HEAD attached after init; porcelain unchanged | PASS |
| 2 `jj status` fast (8–9 ms ×3) | PASS |
| 3 all() tracks untracked, skips ignored, refuses >1 MiB | PASS (hazard quantified) |
| 4 helper commit: lane identity, pathspec-limited, pushed hash = ancestor of main, ahead=0, scratch preserved | PASS |
| 4 rejected-push recovery: fetch+rebase unpushed only, pushed hash reported | PASS |
| 5 README verifiers identical under colocation vs plain git | PASS |
| 5 lane has git-invoking gates to test | N/A — none exist (no SKILL.md, no gate registry, no git calls) |

## Lane-specific colocation hazards

1. **Detached HEAD breaks `@{u}`/`HEAD` refs** — after any helper commit,
   `git rev-parse --abbrev-ref @{u}` → `fatal: HEAD does not point to a branch`.
   Anything in this lane (or fleet tooling pointed at it) that resolves upstream via
   `@{u}`/`HEAD` must use `refs/heads/main`/`main` instead. `git rev-parse main`,
   `git log main`, `merge-base` all work.
2. **jj resets the git index on every mutation** — `git add` staging in the lane is
   destroyed by each helper commit; fleet code must never pre-stage.
3. **` A` intent-to-add pollution only under default `all()`** — the helper's
   `none()` is what keeps `git status --porcelain` clean; verified contrast in step 3
   (one planted file → ` A` row). Losing `none()` would make every seat-scratch file
   look "staged".
4. **`snapshot.max-new-file-size` = 1 MiB** — the lane's largest ignored file is
   1.41 MiB (`.ufo/interactive-sessions/*.jsonl`). Under `all()` it is safe only
   because it is gitignored; any *unignored* >1 MiB seat artifact triggers
   "Refused to snapshot" warnings and is silently left untracked (never committed).
   Under `none()` this is moot — nothing is auto-tracked.
5. **`.ufo/` is partially tracked** — `.ufo/waves/`, `.ufo/continuations/`,
   `.ufo/plans/`, `.ufo/reports/` are committed corpus in this lane, while
   `.ufo/interactive-sessions/` is the only ignored subdir. A stray
   `.ufo/state/` or `watchdog.log` would be *unignored* here; the helper's path
   guard covers `.ufo/state/` and `.ufo/watchdog.log` only — other runtime dumps
   under `.ufo/` would be committable if a pathspec named them. Lane `.gitignore`
   currently has exactly one line; it does **not** exclude `.ufo/state/`.
6. **No nested `.git`, symlinks, `.gitattributes`/LFS, or custom hooks** — verified
   with `find` (none present); clean profile for colocation.
7. **`committed` ≠ `pushed` hash on rejected pushes** — reports must cite the
   `pushed` line (helper already does); any seat habit of citing `jj log @-` or
   the pre-push hash would cite a hash that is not on the remote.

## Recommended per-lane config / ignore additions

- `snapshot.auto-track = "none()"` — keep helper default (already set); it is the
  load-bearing setting for this lane.
- Add to lane `.gitignore`: `.ufo/state/`, `.ufo/watchdog.log`, `.ufo/interactive-sessions/`
  (already there), and a catch-all for seat scratch such as `scratch-*` /
  `*.scratch` if seat conventions produce it — belt-and-suspenders against any
  future auto-track regression, and so `jj file track` on a directory can't sweep
  them in.
- Optional: `snapshot.max-new-file-size` left at default 1 MiB — the lane's real
  artifacts (corpus JSON, LOG.md ≤ ~365 KB) are well under it; raising it would
  only invite binary session dumps into history.
- No `.gitattributes`, hooks, or gitignore hygiene changes needed beyond the above;
  remote and branch settings unchanged (jj reuses `origin`).

## [INFERENCE]

- The 1.17 s total for a rejected-push recovery (fetch + rebase + push) suggests
  colocated commits stay cheap even under concurrent remote writers on this lane's
  history size (~small). [INFERENCE]
- Because no lane gate invokes git, colocation risk for `revenger` is dominated by
  **fleet-side** git readers (`@{u}` upstream refs, index staging) rather than
  lane-local checks — this lane is a low-risk adoption candidate. [INFERENCE]
- `jj status` at 8–9 ms vs typical `git status` cost means per-commit overhead is
  negligible; the only real cost observed was the one-time init import. [INFERENCE]

## Cleanup

Sandbox `/fast/scratch/jj-wave/JjTrialRevenger/` removed after reporting (no cited
failure required preserving it).
