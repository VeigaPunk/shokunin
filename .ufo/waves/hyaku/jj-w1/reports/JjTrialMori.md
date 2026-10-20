# JjTrialMori — empirical jj-colocation trial for lane `mori`

Seat: JjTrialMori-2 · Date: 2026-10-20 · jj 0.45.1-7c41cdeb (~/.local/bin/jj)
Live repo (read-only): /home/vgpnk/Projects/shokunin/mori-shokunin, branch `master`
Sandbox: /fast/scratch/jj-wave/JjTrialMori/ (removed after trial; no failures needed it)

No tool installs performed. No `jj` command ever ran inside a live repo; all jj
work happened under /fast/scratch/jj-wave/JjTrialMori/. The sandbox remote was a
bare clone of the live repo (`git remote -v` confirmed before every push:
`origin /fast/scratch/jj-wave/JjTrialMori/remote.git`). No real remote touched.

## Findings (observed)

### Step 1 — sandbox build

Commands:

    git clone --bare /home/vgpnk/Projects/shokunin/mori-shokunin /fast/scratch/jj-wave/JjTrialMori/remote.git
    git clone remote.git lane
    rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/mori-shokunin/ lane/
    git -C lane status --porcelain | wc -l        → 0
    git -C lane status --porcelain --ignored      → !! .ufo/interactive-sessions/

- `git status --porcelain` = **0** (live repo was already clean; the only
  non-tracked content is the gitignored `.ufo/interactive-sessions/` tree).
- Largest untracked-or-ignored files (all ignored, under
  `.ufo/interactive-sessions/20261015T050057Z/`):
  1. `…/2026-10-15T05-04-04-449Z_01a13df2-…jsonl` — 1,612,301 B
  2. `…/__advisor.jsonl` — 909,162 B
  3. `…/5.eval.log` — 44,822 B
  4. `…/2.bash-original.log` — 1,934 B
- Largest *tracked* files (context for max-new-file-size): `.ufo/waves/round-15/evidence/r14-preserved/evidence.json` 2,324,511 B; `r13-preserved/evidence.json` 1,976,018 B; `round-14/evidence/green-after-accepted/evidence.json` 1,354,213 B; `round-15/evidence/green-after/run-manifest.json` 1,255,789 B.
- Repo shape: no nested `.git` dirs, no symlinks (`find -type l` → none),
  no `.gitattributes` (no LFS), no hooks beyond `*.sample`, single remote
  `origin`, `.gitignore` contains exactly `.ufo/interactive-sessions/`.
  `.ufo/state/` does not exist in this lane (watchdog state lives in the
  fleet root), and `git ls-files .ufo` shows 2,691 tracked paths —
  `.ufo/waves/**` evidence IS committed by this lane.

### Step 2 — helper init (`jj-lane.sh init lane mori`, HYAKU_STATE=sandbox)

- Helper output tail: `state branch=master local=24526ea9… remote=24526ea9…
  ahead=0 behind=0 head=attached tracked=0 untracked=0` (rc=0).
- Init warnings (stderr, non-fatal): `Warning: This setting will only impact
  future commits. The author of the working copy will stay
  "Joao Pedro Veiga <jpveigao10@gmail.com>". To change the working copy
  author, use "jj metaedit --update-author".` — emitted twice, once per
  `config set user.*`. The helper already compensates via metaedit at commit.
- Repo config confirmed. `jj config set --repo` in jj 0.45.1 does NOT write a
  TOML inside the repo: `.jj/repo/` contains only `config-id` (content
  `2890bc18b6d3dc0d9b17`). `jj config path --repo` resolves to
  **`$HOME/.config/jj/repos/2890bc18b6d3dc0d9b17/config.toml`**, which holds:

      [revset-aliases] "trunk()" = "master@origin"
      [snapshot] auto-track = "none()"
      [user] name = "mori-shokunin"  email = "mori@shokunin.local"

  [INFERENCE] Repo-scoped jj config lives outside the repo, keyed by config-id.
  Wiping `~/.config/jj/repos/` or `cp -a`-ing `.jj` without that file silently
  drops auto-track="none()" — the next snapshot reverts to default `all()`.
  jj warns "Your repo appears to have been copied…" but still proceeds.
- git HEAD attached: `git symbolic-ref -q HEAD` → `refs/heads/master` (rc 0).
- `git status --porcelain` after init = **0** — unchanged vs step 1.
  `.jj/` itself is invisible to git because `jj git init --colocate` writes
  `.jj/.gitignore` containing `/*` (verified via
  `git check-ignore -v .jj/repo → .jj/.gitignore:1:/*`).
- `jj status` timings (from lane dir): 12 ms, 7 ms, 7 ms over 3 runs.

### Step 3 — default auto-track="all()" control (lane-autotrack copy)

Setup: `cp -a lane lane-autotrack`; `jj config set --repo snapshot.auto-track '"all()"'`.
With a 2 MiB untracked binary plus a small untracked text file:

    jj status → 25 ms; "Working copy changes: A seat-scratch.txt";
    "Untracked paths: ? big-scratch.bin"
    Warning: Refused to snapshot some files:
      big-scratch.bin: 2.0MiB (2097152 bytes); the maximum size allowed
      is 1.0MiB (1048576 bytes)

- Files snapshotted into @: every untracked non-ignored file (here 1,
  `seat-scratch.txt`; earlier runs also tracked redirect leftovers). The
  ignored `.ufo/interactive-sessions/` tree (incl. the 1.6 MiB jsonl) stayed
  untracked — jj honors `.gitignore` before auto-track.
- `new file too large`: yes — refusal shown above; the file stays untracked
  (warning only, not an error).
- **Index hazard measured:** `jj file track`/`all()` tracking writes
  intent-to-add entries into the git index:
  `git status --porcelain` in lane-autotrack showed ` A seat-scratch.txt`
  (git's "added, intent to add" row) for a file never `git add`ed.
- Snapshot time ~23–32 ms.

### Step 4 — round commit through the helper

Inputs: appended one line to LOG.md; created
`corpus/lessons/round-999-jjtrial.md`; left `jjtrial-scratch.txt` untracked.

    jj-lane.sh commit lane --as mori -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
    → committed 6deb9abbcdb291077d6fa0566296a18723fbbe15
      pushed    6deb9abbcdb291077d6fa0566296a18723fbbe15   (rc=0)

Verification (all in sandbox lane):

- `git log -1 --format='%an <%ae> | %cn <%ce>' 6deb9ab` →
  `mori-shokunin <mori@shokunin.local> | mori-shokunin <mori@shokunin.local>` —
  author AND committer carry the lane identity.
- `git log -1 --format=%H -- LOG.md` → `6deb9ab…` = pushed hash. ✓
- `git merge-base --is-ancestor 6deb9ab master` → rc 0. ✓
- `jj-lane.sh state lane` → `… ahead=0 behind=0 head=detached
  tracked=0 untracked=1`. Note: HEAD is now **detached** (first jj mutation
  detaches it; it sits on the branch tip) but `detect_branch` still resolves
  `master` via `origin/HEAD`, so the state line is correct.
- `git -C remote.git rev-parse master` → `6deb9ab…` — remote has it. ✓
- `cat jjtrial-scratch.txt` → intact; `git status --porcelain` →
  `?? jjtrial-scratch.txt` only. Pathspec limit held (commit diff = LOG.md +
  the lesson file only).

Operator-push race:

    # in a second clone "operator": committed considerthese/2026-10-20-jjtrial-sim.md → a430f83, pushed
    jj-lane.sh commit lane --as mori -m "round-999b: …" -- LOG.md corpus/lessons/round-999-jjtrial-b.md
    → committed 66c79bdefc6f067a7518dcae9c1ab52556d4f8c2
      pushed    5eb0cb3f955dbf20de0478c307d530d7285f149e   (rc=0)

- Push was rejected (non-FF), helper fetched, rebased the unpushed change onto
  `master@origin`, retried, succeeded on attempt 2.
- `git log --oneline -4 master`: `5eb0cb3 round-999b… / a430f83 considerthese:
  simulated operator push / 6deb9ab round-999… / 24526ea round-16…` — remote
  history preserved, no rewrite of the operator commit.
- Rebased commit `5eb0cb3` keeps `mori-shokunin <mori@shokunin.local>` as both
  author and committer; `git diff-tree` shows only LOG.md + lesson-b.
- **Discrepancy:** the printed `committed` hash (66c79bd) ≠ `pushed` hash
  (5eb0cb3). `git cat-file -t 66c79bd` still resolves (loose object) but no
  ref reaches it — it is an abandoned draft. Any report that cited
  `committed` would name a non-ancestor of master → would FAIL the
  `merge-base --is-ancestor` check. Only the `pushed` hash is citeable.

### Step 5 — lane's own git-touching checks (300 s timeouts, colocated lane)

| check | command | rc | result |
|---|---|---|---|
| census selftest | `bash tools/mori-census.sh --selftest` | 0 | `MORI_CENSUS_SELFTEST: PASS (113 cases, 113 passed, 0 failed)` |
| silence oracle | `bash tools/mori-silence-cases.sh` | 0 | `MORI_SILENCE_CASES: matched=28 total=28` |
| r14 regressions | `python3 tools/mori-round14-regressions.py --selftest` | 0 | `SELFTEST: pass checks=20 (parsers + real-gate red rc1/tamper rc2)` |

All three pass under colocation; zero failures to separate from baseline.
The regression harnesses record `git rev-parse HEAD` and
`git status --porcelain` — both keep working with the detached HEAD (`git
rev-parse HEAD` → `5eb0cb3`, correct). What DOES break after jj mutations:
`git rev-parse '@{u}'` → `fatal: HEAD does not point to a branch`.
`git rev-parse master` still works. I did not find a lane tool that uses
`@{u}` (census uses `git ls-files -mo --exclude-standard` and `git log`
against lane dirs — both colocation-safe).

## PASS/FAIL table

| step | criterion | verdict |
|---|---|---|
| 2 | init rc=0, state line emitted | PASS |
| 2 | repo config set (auto-track none, identity, trunk) | PASS (but stored in ~/.config/jj/repos/, not in-repo — see hazard H2) |
| 2 | git HEAD attached after init | PASS |
| 2 | `git status --porcelain` unchanged | PASS (0 → 0) |
| 3 | all() snapshots every non-ignored untracked file | PASS (measured; 1-file sample + redirect files) |
| 3 | >1 MiB new file refused with warning | PASS (2 MiB file refused, stayed untracked) |
| 4 | `committed`+`pushed` printed, rc=0 | PASS |
| 4 | author+committer = lane identity | PASS |
| 4 | `git log -1 --format=%H -- LOG.md` == pushed | PASS |
| 4 | merge-base ancestor of master | PASS |
| 4 | state shows ahead=0 | PASS |
| 4 | remote has commit; scratch untracked+intact | PASS |
| 4 | recovery on moved remote (fetch+rebase) | PASS — but `committed` hash orphaned (see H1) |
| 5 | 3 git-touching checks green under colocation | PASS (3/3) |

## Colocation hazards specific to this lane

- **H1 — citeable hash moves on rebase.** When the remote advances mid-round
  (operator `considerthese/` pushes are routine in this lane — e.g. 786ebed,
  a430f83), a rejected push rewrites the lane commit; the `committed` line
  then names an abandoned object. Callers MUST cite only the `pushed` line.
- **H2 — repo config lives outside the repo** (`~/.config/jj/repos/<id>/`).
  Copying `.jj` (or losing that file) silently restores auto-track=all();
  the next jj mutation then intent-to-adds every non-ignored untracked file —
  which is what sprays ` A` rows into `git status` and could slip files into
  a later `jj file track` commit if a pathspec names a directory.
- **H3 — intent-to-add index pollution under all().** Measured: tracked-by-jj
  files appear as ` A` in `git status`. Any lane/closure flow that commits a
  DIRECTORY pathspec via the helper runs `jj file track <dir>` — ignored
  children are excluded but non-ignored scratch under the dir is committed.
- **H4 — detached HEAD after first mutation.** `@{u}` breaks
  (`fatal: HEAD does not point to a branch`); `git rev-parse <branch>` and
  `origin/HEAD` resolution still work. The mori checks measured here do not
  use `@{u}`.
- **H5 — index reset on every jj mutation.** Known property; mori's gates
  are read-only so unexercised here, but any lane script that `git add`s then
  runs a jj command loses staged entries. None found in tools/.
- **Lane-specific content hazards — none blocking:** largest ignored file is
  1.6 MiB but it is `.gitignore`d so neither snapshot mode touches it; no
  symlinks, no nested .git, no LFS/.gitattributes, no active hooks. Tracked
  evidence.json files up to 2.3 MiB are already tracked, so
  `snapshot.max-new-file-size` never applies to them — BUT a *new* >1 MiB
  file explicitly named to `jj-lane.sh commit` IS force-tracked via
  `file track --include-ignored` (the helper's own flag). That's intended for
  lessons; it means an accidentally named large artifact bypasses the 1 MiB
  guard.
- **`.ufo/` nuance for this lane:** `.ufo/waves/**` and `.ufo/reports/**` are
  TRACKED and committed per round (2,691 paths); only
  `.ufo/interactive-sessions/` is ignored and `.ufo/state/` doesn't exist
  here. The helper's `.ufo/state/*` refusal is correct to keep anyway.

## Recommendations

1. No per-lane ignore additions needed for mori: the single ignore
   `.ufo/interactive-sessions/` already covers its only large untracked
   content. Do NOT add a jj-specific ignore; `.jj/.gitignore` (`/*`) already
   hides jj internals from git.
2. Per-lane jj config to keep exactly as the helper sets:
   `snapshot.auto-track="none()"`, `trunk()="master@origin"`,
   user.name/email = mori lane identity. Add nothing else.
3. Consumer-facing rule for all lanes (helper already enforces it; keep in
   docs): cite ONLY the `pushed` hash; treat `committed` as advisory. A cheap
   guard: reports verify `git merge-base --is-ancestor <cited> master`.
4. [INFERENCE] Because `init`/`commit` resolve the branch via origin/HEAD
   when HEAD is detached, a fresh clone that never had origin/HEAD (local-only
   remote like this sandbox's) still worked — detect_branch fell through to
   `refs/heads/master`. No change needed for mori; note for lanes whose only
   remote is a real GitHub remote: ensure `git remote set-head origin` or a
   first `jj git fetch` exists before init so `origin/HEAD` resolves.
5. Consider documenting that jj repo config is NOT in-repo (H2): any wave
   that rsyncs lanes between hosts must re-run `jj-lane.sh init` on the
   destination, not rely on copied `.jj`.

## Cleanup

Sandbox /fast/scratch/jj-wave/JjTrialMori/ removed after the report was
written; the bare remote and both clones were disposable. Live repo untouched
(read-only probes only).
