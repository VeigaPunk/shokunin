# JjTrialKagi — jj colocation trial, lane `kagi`

Seat: JjTrialKagi-2. Live repo `/home/vgpnk/Projects/shokunin/kagi-shokunin` (branch `master`,
tip `c2cab35bc92e` at trial start, remote `github.com/VeigaPunk/kagi-shokunin.git`) was read-only
throughout; all jj commands ran only in `/fast/scratch/jj-wave/JjTrialKagi/`. jj 0.45.1
(`~/.local/bin/jj`, version `0.45.1-7c41cdeb`). No tools installed.

## Step 1 — sandbox build

Commands:
```
git clone --bare /home/vgpnk/Projects/shokunin/kagi-shokunin /fast/scratch/jj-wave/JjTrialKagi/remote.git
git clone /fast/scratch/jj-wave/JjTrialKagi/remote.git /fast/scratch/jj-wave/JjTrialKagi/lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/kagi-shokunin/ /fast/scratch/jj-wave/JjTrialKagi/lane/
git -C /fast/scratch/jj-wave/JjTrialKagi/lane status --porcelain | wc -l   → 0
```

Live `git status --porcelain | wc -l` is also `0`; live `--ignored` shows exactly one entry:
`!! .ufo/interactive-sessions/` (only pattern in `.gitignore`: `.ufo/interactive-sessions/`).
100 tracked files, 6.6 MB total tree.

Largest untracked/ignored files (all ignored, none untracked; `du -b`):
```
2024931  .ufo/interactive-sessions/20261015T050057Z/…01a13df2….jsonl   (1.93 MB — over jj 1 MiB default)
 739704  .ufo/interactive-sessions/20261015T050057Z/…/__advisor.jsonl
  11673  .ufo/interactive-sessions/20261015T050057Z/…/2.bash-original.log
```
Largest tracked files (would matter only if rewritten): SCORECARD.md 87 kB, corpus/claim-ledger.sh 79 kB,
LOG.md 75 kB — all far under any jj limit.

## Step 2 — `jj-lane.sh init` colocation — PASS

```
HYAKU_STATE=/fast/scratch/jj-wave/JjTrialKagi/state scripts/hyaku/jj-lane.sh init …/lane kagi
→ exit 0
state branch=master local=c2cab35b… remote=c2cab35b… ahead=0 behind=0 head=attached tracked=0 untracked=0
```

- Helper state line: `state branch=master local=c2cab35bc92e57e39e5489bac3386db078345b3f remote=c2cab35bc92e57e39e5489bac3386db078345b3f ahead=0 behind=0 head=attached tracked=0 untracked=0`
- Init warnings (stderr): `Warning: This setting will only impact future commits. The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>".` — expected; the helper stamps author via `metaedit --update-author` at commit time (verified in step 4). No "already tracks added paths" warning (`warn: working-copy commit @ already tracks …`) — @ was empty.
- `git symbolic-ref -q HEAD` → `refs/heads/master` — HEAD attached after init.
- `git status --porcelain` before and after init: identical, 0 lines — every path still `??`/`!!` as before (no intent-to-add leakage).
- Repo config confirmed (`jj config list --repo`):
  `snapshot.auto-track = "none()"`, `user.name = "kagi-shokunin"`,
  `user.email = "kagi@shokunin.local"`, `revset-aliases."trunk()" = "master@origin"`.
- `jj status` timed 3 runs from the lane dir: 7 ms, 7 ms, 7 ms (working copy clean, @ empty).

## Step 3 — default `auto-track="all()"` alternative — measured

`cp -a` of the colocated lane → `lane-autotrack`, then
`jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'` (warned the repo was copied;
harmless in sandbox). First `jj status` after the flip: **9 ms, 0 files added** — the only overlay content
is *ignored*, and auto-track honors `.gitignore`. To measure the real default-auto-track hazard the
helper's comment describes, I then added `seat-scratch.txt` (untracked), `big-untracked.bin` (1 600 000 B),
and `.ufo/igtest/big-ignored.bin` (1 600 000 B, ignored). Second `jj status`: **14 ms**, result:

```
Warning: Refused to snapshot some files:
  big-untracked.bin: 1.5MiB (1600000 bytes); the maximum size allowed is 1.0MiB (1048576 bytes)
Working copy changes: M .gitignore / A seat-scratch.txt / ? big-untracked.bin
```

- Files snapshotted into @: 1 (`seat-scratch.txt`), plus the `.gitignore` modification.
- `new file too large` refusal: yes, one — `big-untracked.bin` left as `?` (untracked), warning on every
  subsequent jj command.
- Ignored big file: silently skipped by auto-track.
- Git view after snapshot: ` A seat-scratch.txt` — an **intent-to-add index entry**, exactly the failure
  the helper's `--ignore-working-copy` config calls prevent.

## Step 4 — round-commit simulation — PASS

Prepared: appended line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md` (new dir), left
`seat-scratch.txt` untracked. Helper run:

```
jj-lane.sh commit …/lane --as kagi -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed f5683d6a4a886f10e0a9cc75a5f5e5e0441a90d1
→ pushed    f5683d6a4a886f10e0a9cc75a5f5e5e0441a90d1   exit=0
```

Verifications:
- `git log -1 --format='%an <%ae> | %cn <%ce>'` → `kagi-shokunin <kagi@shokunin.local> | kagi-shokunin <kagi@shokunin.local>` — author **and** committer carry lane identity.
- `git log -1 --format=%H -- LOG.md` = `f5683d6a…` = pushed hash.
- `git merge-base --is-ancestor f5683d6a… master` → exit 0.
- `jj-lane.sh state` → `… ahead=0 behind=0 head=detached tracked=0 untracked=1`.
- Remote: `git -C remote.git rev-parse refs/heads/master` = `f5683d6a…`.
- `seat-scratch.txt`: still `??`, content `scratch` intact; `git ls-files --error-unmatch` rejects it.
- **HEAD detached** after the commit (`git symbolic-ref -q HEAD` fails) — the documented @-worktree state.

Concurrent-push recovery (operator pushes `considerthese/2026-10-19.md` change from a second clone,
tip `1ae55780`, then a second lane commit races it):

```
jj-lane.sh commit … -- LOG.md plans/jj-trial-plan.md
→ committed 7279db5e058b855ea1b0930741d9561998a0982e
→ pushed    2b6cb6b811b6bc10a7af6d242cbbed29d51c894c   exit=0
```

Push was rejected, helper fetched, rebased only the unpushed commit onto `master@origin`, retried,
landed. Remote `master` = `2b6cb6b8…`; history linear: `2b6cb6b → 1ae5578(operator) → f5683d6 → c2cab35`.
`git merge-base --is-ancestor 2b6cb6b8… master` exit 0; `state` ahead=0. Rebased commit keeps
`kagi-shokunin` author. Both lane files (`plans/jj-trial-plan.md`) and operator file present in remote tree.

**Protocol hazard (confirmed live):** after a rebase-recovery push, `committed <hash>` ≠ `pushed <hash>`,
and the `committed` hash is **not** an ancestor of the branch — `merge-base --is-ancestor 7279db5e…` fails.
A report or parser citing the `committed` line would cite an unlanded hash. Callers MUST take the `pushed`
line only. The helper already prints it correctly and last; nothing to fix in the helper, but fleet
callers/scrapers should be pinned to the `pushed` token.

## Step 5 — lane's own git-touching checks — PASS (vacuous for git, parity-verified)

`grep` for git invocations across every lane script (`corpus/*.sh`, SKILL.md registry): **zero real
`git` calls** — all matches are the substrings `digits`, `legitimately`, `github_pat_`. The lane's gate
suite (scope-gate, claim-ledger, drift-pins, surface-census, checklist-run, op-ref-probe, sources-census,
transcript-scan) is pure-filesystem; nothing reads HEAD, index, or remotes. Detached HEAD and the jj-owned
index are therefore non-issues for this lane today.

Parity selftests (300 s timeout each), colocated lane vs fresh plain clone (`lane` vs `plain`):

| selftest | jj-colocated exit | plain-git exit | output |
|---|---|---|---|
| `bash corpus/scope-gate.sh --selftest` | 0 | 0 | identical — `SCOPE_SELFTEST: PASS (61 cases)` |
| `bash corpus/claim-ledger.sh --selftest` | 0 | 0 | identical — `SELFTEST: PASS (97 cases)` |
| `bash corpus/drift-pins.sh --selftest` | 0 | 0 | identical — `DRIFT_SELFTEST: PASS (13 cases)` |

No failures, so no colocation/pre-existing split was needed. (Note: the selftests write scratch trees —
run under `--selftest` they were non-mutating to the repo: `git status` stayed clean apart from the
pre-existing `?? seat-scratch.txt`.)

## PASS/FAIL summary

| step | result |
|---|---|
| 2 init (state line, config, HEAD attached, status unchanged) | PASS |
| 3 auto-track measurement (tracked count, size refusal, timing) | measured — 1 tracked / 1 refused / 9–14 ms |
| 4 commit+push, identity, ancestry, ancestor check, ahead=0, remote, scratch intact, rebase recovery | PASS |
| 5 lane checks (3 selftests, jj vs plain parity) | PASS — no git-touching gate exists |

## Colocation hazards specific to kagi

1. **Detached HEAD after every jj mutation.** Any lane/fleet tool using `@{u}`, `HEAD`-relative revs,
   or `git status -sb` upstream info breaks post-commit. `git rev-parse master`, `merge-base`,
   `rev-list origin/master..master` all keep working — the helper's `state` already avoids HEAD.
2. **`committed` vs `pushed` divergence on rebase recovery** (step 4). Cite only `pushed`.
3. **Git index is reset by jj mutations** — `git add`-staged entries vanish. Nothing in this lane stages.
4. **Large ignored files**: `.ufo/interactive-sessions/*.jsonl` (~2 MB) exceeds jj's 1 MiB
   `snapshot.max-new-file-size`. Harmless only *because* it is ignored; if `.gitignore` were weakened,
   auto-track or a `file track --include-ignored` on a directory would refuse/bloat. Keep the ignore.
5. **`.ufo/` is partially tracked** (round-20 wave files are committed) — pathspec-limited commits are
   mandatory here; the helper's `.ufo/state/` block covers the driver-runtime subset. `LOG.md` append-only
   is preserved (appends committed fine).
6. **Absent hazard inventory** (checked, all negative): no nested `.git` dirs, no symlinks, no
   `.gitattributes`/LFS, no non-sample git hooks, no generated build dirs. Lane scripts never call git.
7. **`jj git init` warned about the copied repo config** in lane-autotrack — only relevant to `cp -a`
   clones of colocated lanes; fresh inits unaffected.
8. Working-copy author warning at init (step 2) is cosmetic but means a *manual* `jj` mutation before the
   first helper commit would stamp the operator identity into @; helper commits self-heal via metaedit.

## Recommendations (per-lane config/ignores)

- Repo config (already set by helper, keep as-is): `snapshot.auto-track="none()"`,
  `revset-aliases."trunk()"="master@origin"`, user.name/email lane identity.
- **Keep** `.gitignore` pattern `.ufo/interactive-sessions/` — it is the load-bearing guard that keeps
  2 MB transcript dumps out of every jj snapshot; do not narrow it to per-file names.
- **Add** to lane `.gitignore` (defense-in-depth, zero cost): `seat-scratch*`, `*.tmp`, and
  `.ufo/state/` — protects against any future default-auto-track slip or bare `jj file track` on a dir.
- Optionally raise nothing: do **not** bump `snapshot.max-new-file-size`; the 1 MiB ceiling is a
  feature for this lane (round docs are ≤90 kB).
- Pin consumers to the `pushed <hash>` line of helper output; never parse `committed`.
- If future lane tooling needs `@{u}` upstream, have it use `master@origin` / `refs/remotes/origin/master`
  explicitly instead — colocated HEAD stays detached by design.

Sandbox `/fast/scratch/jj-wave/JjTrialKagi/` removed on completion (no failure artifacts to preserve).
