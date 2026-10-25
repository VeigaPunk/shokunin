# JjTrialChousa — jj colocation trial for lane `chousa`

Sandbox: `/fast/scratch/jj-wave/JjTrialChousa/` (removed after trial) · lane: `lane/` ·
control clone: `lane-plain/` · auto-track probe: `lane-autotrack/` · remote: `remote.git`
(bare clone of the live lane). jj 0.45.1 (`jj 0.45.1-7c41cdeb...`),
`scripts/hyaku/jj-lane.sh` as shipped. No installs.

## Findings

### Step 1 — sandbox build

```
git clone --bare /home/vgpnk/Projects/shokunin/chousa-shokunin /fast/scratch/jj-wave/JjTrialChousa/remote.git
git clone /fast/scratch/jj-wave/JjTrialChousa/remote.git /fast/scratch/jj-wave/JjTrialChousa/lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/chousa-shokunin/ /fast/scratch/jj-wave/JjTrialChousa/lane/
```

- `git -C lane status --porcelain | wc -l` → **0**. The live working tree has zero
  untracked/modified files; the only non-tracked content is the ignored dir
  `.ufo/interactive-sessions/` (`git status --porcelain --ignored` → `!! .ufo/interactive-sessions/`).
- `.gitignore` contains exactly `.ufo/interactive-sessions/`. `git ls-files` = 249 files,
  including 63 tracked files under `.ufo/` (reports, evidence, plans — `.ufo/` is only
  *partially* ignored).
- Largest untracked/ignored files (only 2 exist; both ignored, under
  `.ufo/interactive-sessions/20261015T050057Z/`):

| bytes | path |
|---|---|
| 2 097 818 | `.ufo/interactive-sessions/20261015T050057Z/2026-10-15T05-04-00-611Z_01a13df2-…-1857.jsonl` |
| 2 011 292 | `…/01a13df2-…-1857/__advisor.jsonl` |

Both exceed jj's default `snapshot.max-new-file-size` (1 MiB); they are safe **only** because
`.gitignore` covers them. (For size context the largest tracked file is
`.ufo/evidence/round-1/wave-plan.json` at 33 555 bytes.)

### Step 2 — `jj-lane.sh init`

```
HYAKU_STATE=/fast/scratch/jj-wave/JjTrialChousa/state jj-lane.sh init …/lane chousa   →  exit 0
```

- Helper's state line:
  `state branch=master local=d730ae4c… remote=d730ae4c… ahead=0 behind=0 head=attached tracked=0 untracked=0`
- Init warnings: the expected two
  `Warning: This setting will only impact future commits. The author of the working copy will
  stay "Joao Pedro Veiga <jpveigao10@gmail.com>"` — cosmetic; `@` keeps the host git identity
  until the first commit (helper fixes it via `metaedit --update-author` at commit time).
- Repo config after init (`jj config list --repo`):
  `snapshot.auto-track = "none()"`, `user.name = "chousa-shokunin"`,
  `user.email = "chousa@shokunin.local"`, `revset-aliases."trunk()" = "master@origin"`.
- `git symbolic-ref -q HEAD` → `refs/heads/master` — **HEAD attached** after init.
- `git status --porcelain` → **0, unchanged** from step 1 (expected: no change ✓). The only
  new ignored entry is `!! .jj/` (jj writes `.jj/.gitignore` with `/*`, self-excluding —
  verified via `git check-ignore -v .jj/`).
- `jj status` timings from the lane dir: **9 ms, 7 ms, 7 ms** (3 runs; 249-tracked-file repo).

### Step 3 — default `auto-track = "all()"` (lane-autotrack copy)

- `jj status` with `all()`: **15 ms**, snapshotted **2 files** into `@` (two scratch redirect
  files present at the call). Ignored paths are *not* auto-tracked:
  `.ufo/interactive-sessions/` (the two 2 MB JSONLs) did **not** enter `@`.
- `new file too large` refusal: provoked deliberately with a 2 MB *unignored* file — jj
  reports it under `Untracked paths:` and warns
  `Refused to snapshot some files: big-untracked.bin: 2.0MiB … maximum size allowed is 1.0MiB`;
  snapshot still completes (16 ms), the file stays untracked. With `none()` this warning
  class is unreachable.
- Measured consequence of `all()`: every transient file any tool writes between jj calls
  enters `@`; in this lane that would have been only the 2 scratch files, but the default
  would also have snapshotted during `jj config set` (the bug the helper's
  `--ignore-working-copy` guards against).

### Step 4 — round commit + push + operator-race recovery

Setup: appended a line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left
`scratch-jjtrial.tmp` untracked.

```
HYAKU_STATE=…/state jj-lane.sh commit …/lane --as chousa -m "round-999: jj trial" \
  -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 83b3ecd5e70d0a13f49e8557e4ac650cb2ae3095
  pushed    83b3ecd5e70d0a13f49e8557e4ac650cb2ae3095      exit 0
```

Verifications:

- `git log -1 --format='%H %an <%ae> | %cn <%ce>'` →
  `83b3ecd5 chousa-shokunin <chousa@shokunin.local> | chousa-shokunin <chousa@shokunin.local>`
  — **author and committer both the lane identity** ✓
- Commit content (`git show --stat`) = exactly `LOG.md | 2 ++` +
  `corpus/lessons/round-999-jjtrial.md | 3 +++` — pathspec-limited ✓
- `git log -1 --format=%H -- LOG.md` = pushed hash ✓
- `git merge-base --is-ancestor 83b3ecd5… master` → exit 0 ✓
- Remote (`remote.git`): `83b3ecd` is the new `master` tip ✓
- `jj-lane.sh state` → `ahead=0 behind=0 head=detached tracked=0 untracked=1` ✓
- `scratch-jjtrial.tmp` still `??`, content `scratch-payload-42` intact ✓
- After the push, `git symbolic-ref -q HEAD` → **detached** at `83b3ecd5…` (the branch tip);
  `git rev-parse @{u}` → `fatal: HEAD does not point to a branch`; `git rev-parse master`
  works. Confirms: HEAD detaches on the *first jj mutation*, not on init.

Operator-race recovery:

```
# second clone of remote.git: commit + push considerthese/op-note.md as "operator" → b14f4d1
# back in lane/, append line to LOG.md, helper commit:
→ committed df397e5000efeb951f1d9c30ebd639c52f1856c9
  pushed    36809752c003c9f2eb0fdeec5a844f7d922326cc      exit 0
```

- `committed` ≠ `pushed`: the helper detected the moved remote, fetched, rebased the unpushed
  commit onto `b14f4d1`, and pushed `36809752` — **the `pushed` line correctly reports the
  rebased remote-tip hash**, so a report citing `pushed` stays truthful.
- `git log --oneline` in remote: `3680975 → b14f4d1 → 83b3ecd → d730ae4` — operator commit
  retained, lane commit rebased on top, nothing force-pushed/rewritten ✓
- `state` → `ahead=0 behind=0` after recovery ✓

### Step 5 — lane git-touching checks

`chousa` has **no gate that invokes git**: `grep '\bgit\b' tools/research-gate.sh` → only a
comment; the sole `.sh` outside tools is `corpus/evidence/round24-measure.sh`, which takes a
tree root as `$1` and mentions `git archive` in a usage comment only. The three most
repo-sensitive checks were run in the colocated lane and in `lane-plain` (fresh clone, no
`.jj`), each under a 300 s timeout:

| check | colocated lane rc | plain clone rc | identical output? | reading |
|---|---|---|---|---|
| `bash tools/research-gate.sh --selftest` | 0 — `RESEARCH_GATE_SELFTEST: PASS (136 cases, 0 skipped)` (20.0 s) | 0 — PASS (18.9 s) | yes | **PASS, colocation-neutral** |
| `verify-all corpus/fixtures/full-r6.md --claims corpus/fixtures/full-r6.claims.jsonl --root .` | 1 — DRIFT (`drift-sections=3 findings=13`; `CLAIM_SOURCE_OUT_OF_CORPUS`/`CHAIN_SOURCE_OUT_OF_CORPUS` ×3 each; `VERIFY_ALL_SECTION_UNAVAILABLE` on structure) | 1 — byte-identical except `ts=` | yes | **environmental**: fixtures cite `research/deep-research-2026-09-28/*.md`, which live at the *fleet root*; a sandbox lacking `--root ..`-to-fleet DRIFTs identically without jj |
| `verify-claims corpus/fixtures/claims-r2.jsonl --root .` | 1 — DRIFT `refused=17` (same out-of-corpus class) | 1 — identical | yes | **environmental**, not colocation |
| `verify-integrity corpus/fixtures/integrity-r7.md --root .` | 0 — `CLEAN (refs=16 resolved=15 unresolved=0)` | 0 — identical | yes | **PASS** |

Zero failures attributable to colocation; every non-zero exit reproduced identically in the
plain clone. Separability confirmed.

## PASS/FAIL

| step | verdict |
|---|---|
| 1 sandbox build + content survey | **PASS** (0 untracked diff, 2 ignored >1 MiB files catalogued) |
| 2 helper init: config set, HEAD attached, status unchanged | **PASS** |
| 3 auto-track measurement: file count, size refusal, timing | **PASS** (2 tracked / 2-MiB refusal demonstrated / 15–16 ms) |
| 4 helper commit+push, identity, ancestry, remote, scratch intact, race recovery | **PASS** (incl. `pushed` ≠ `committed` hash after rebase; remote tip = pushed) |
| 5 lane checks colocated vs plain clone | **PASS** — no colocation-caused failure; `--selftest` and `verify-integrity` green; verify-all/claims DRIFT is environmental (missing fleet `research/` corpus) and pre-existing |

## Colocation hazards specific to this lane

1. **`.ufo/` is split-brained**: `.ufo/interactive-sessions/` ignored (contains the only
   >1 MiB files in the lane — 2 × ~2 MB JSONL, *over* jj's `max-new-file-size`), while 63
   other `.ufo/` files (round reports/evidence/plans, incl. `.ufo/round-*/goal-wave/report-draft.md`
   drafts) are **tracked**. A lane commit with a directory pathspec like `.ufo/` would pull in
   every draft — the helper's file-path-only `--include-ignored` escape plus the pathspec
   contract are what keep this safe. Do not loosen `.gitignore` here.
2. **Detaching HEAD**: `@{u}` breaks after the first jj mutation (`fatal: HEAD does not point
   to a branch`); `git rev-parse master`, `git log`, `merge-base` all still work. No lane
   tooling uses `@{u}` or HEAD-as-branch (grep-negative).
3. **jj resets the git index on mutation**: a staged `git add` entry survived `jj status`
   (auto-track `none()` left `A  scratch2.tmp` intact) but was wiped by a `jj commit` run
   (`git diff --cached --name-only` → empty, file back to `??`). Mixing `git add` + helper
   commits loses staged state — content is not lost, but staged work must be re-added.
   [INFERENCE: consistent with the brief's "jj resets the git index" observation; measured
   here that `jj status` alone does *not* reset it under `auto-track="none()"`.]
4. **`.jj/` self-ignores** via `.jj/.gitignore` (`/*`) — `git status` stays clean; no
   `.gitignore` edit needed for jj itself.
5. **Clean of classic hazards**: two tracked 100755 scripts (`tools/research-gate.sh`,
   `corpus/evidence/round24-measure.sh`); no symlinks, no hardlinks, no nested `.git` dirs, no
   `.gitattributes`/`.gitmodules`/LFS, no active hooks (only `*.sample`).
6. **Fleet-root coupling**: fixtures cite `research/deep-research-2026-09-28/` at the fleet
   root via `--root ..` — the lane expects its checkout to sit inside the shokunin fleet tree;
   jj colocation preserves repo-relative work but a detached checkout layout must keep that
   parent relationship for gates to resolve.

## Recommendations

- **Adopt** `jj-lane.sh` for `chousa` as-is; measured behavior satisfies every protocol
  invariant (lane identity on author+committer, pathspec-limited commits, `pushed` hash is
  the remote tip, fetch+rebase-on-reject works, `.ufo` drafts and scratch stay out).
- Per-lane config: **keep `snapshot.auto-track = "none()"`** (default `all()` would track
  every transient file; the two 2 MB ignored JSONLs are protected only by `.gitignore`, and
  any future unignored large artifact would hit the 1 MiB refusal warning on every jj call).
- Optional, not required: ignore `*.tmp` or `.ufo/round-*/goal-wave/` for belt-and-suspenders
  beyond the helper's file-path tracking rule — current `.gitignore` + helper is sufficient
  [INFERENCE].
- No `.gitattributes`, hook, or per-lane jj additions needed beyond what `init` writes.
- Note for the L1 contract: cite the **`pushed`** hash (verified: `committed df397e5` ≠
  `pushed 3680975` after the simulated operator race).

## Sandbox disposition

`/fast/scratch/jj-wave/JjTrialChousa/` removed after the trial (no failures needed
preserving). The rebase-recovery history is reproducible from the commands above; remote tip
was `3680975 → b14f4d1 → 83b3ecd → d730ae4` at teardown.
