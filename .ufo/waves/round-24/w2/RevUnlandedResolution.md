# RevUnlandedResolution — routed defect 2 (89 unlanded paths): closure composition

Seat `L1Tabi24.RevUnlandedResolution`, round 24 wave 2, falsification pass.
Target: lane tip `ad125e85c235e1c4ec6a08e398bd64da01f68a08` (`2026-10-25 05:41:00 -0300`).
Baseline `573c99e4885382db38babc3a6fc90e77afeb42a6`; round-23 reviewed tip `c90dffd`.
Lane root `/home/vgpnk/Projects/shokunin/tabi-shokunin`. Read-only; no tracked file touched.

## 0. Verdict

**The 89 paths themselves are resolved — every class is gone from both the tip tree and the
worktree, and nothing in the 89 is left un-disposed.** But the *statement* the lane landed in place
of the defect — `corpus/lessons/round-24.md:86`, "`git status --porcelain` empty at the round-24
tip" — **is false as a live fact**, and the numeric target that rides on the same class (`C2`
`after: 0`) is contradicted by the lane's own committed receipts and by a re-run at the tip.

Three findings, in severity order:

- **F1 (HIGH) — the closure condition does not hold: 8 untracked paths, not 0.** The tracked tree
  is byte-clean at the tip; every unlanded path is `??` and every one of them postdates the tip
  commit. The class that composed the round-23 defect is *recurring right now*, unignored.
- **F2 (HIGH) — `C2 after: 0` is unsupported and unreproducible.** The committed receipts record
  `mismatches: 1`, `clean: false`; a live re-run at the tip records `1`; the class responsible
  (`m3`) is **not revision-scoped at all**, so "before 89 / after 0" is a pair of unrelated
  working-tree snapshots, not a measured delta.
- **F3 (MEDIUM) — the landed composition of the 89 is arithmetically and factually wrong** in four
  ways: it uses a collapsed count where the closure uses an expanded one; it names a tracked file
  as untracked; it uses 66 where the spot-check counted 67; and its own numbers sum to 73, not 89.

## 1. The closure condition, measured

```
$ git -C /home/vgpnk/Projects/shokunin/tabi-shokunin rev-parse HEAD
ad125e85c235e1c4ec6a08e398bd64da01f68a08

$ git status --porcelain --untracked-files=all | wc -l
5            # at 05:46 — first read, before any sibling report landed
8            # at 05:54 — after three wave-2 seat reports landed (drift, see §5)
```

First read, expanded (`-uall`), all `??`, no `M`, no staged entry:

| mtime | path |
|---|---|
| 05:42:08 | `.ufo/waves/round-24/gen-w2.mjs` |
| 05:42:24 | `.ufo/waves/round-24/w2-dispatch.err` |
| 05:42:24 | `.ufo/waves/round-24/w2-dispatch.json` |
| 05:42:24 | `.ufo/waves/round-24/w2-spec.json` |
| 05:42:24 | `.ufo/waves/round-24/w2/swarm-registry.json` |

Later entries (05:52:59–05:53:53): `w2/ScoutReopenS105.md`, `w2/ScoutReopenS104.md`,
`w2/ExecReDerive.md`. This report is itself a ninth such path.

Tracked state is exactly the tip:

```
$ git diff HEAD --stat        -> (no output)
$ git diff --cached --stat    -> (no output)
```

So: **`M` count 0, staged 0, untracked > 0.** Every untracked path was created *after* the tip
commit — the earliest, `gen-w2.mjs`, is 68 s later; the rest 84 s later. Collapsed and expanded
disagree (5 vs 8) because `w2/` is a wholly-untracked directory that bare `--porcelain` prints as
one entry:

```
$ git status --porcelain | wc -l                     -> 5   ("?? .ufo/waves/round-24/w2/")
$ git status --porcelain --untracked-files=all | wc -l -> 8
```

That distinction is load-bearing for §3.

## 2. The 89, class by class: fate and the commit that carried it

The spot-check's composition (`corpus/lessons/round-23-verifier-spotcheck.md` §4.2) is
**2 `M` + 87 `??` = 89**. Re-derived fate of every class:

| # | class | n in the 89 | fate | commit that carried it |
|---|---|---|---|---|
| 1 | empty numeric root files (`179291*`) | 67 (spot-check) / 66 (assignment, and `CritNoHarm.md` §2 at its read) | **deleted from the worktree** | **none** — never tracked; `git rev-list --all --objects \| grep -cE ' [0-9]+$'` → `0`, so no commit ever added one, and none can record the deletion |
| 2 | `.err` captures, untracked | 3: `w1-dispatch.err`, `w1-record.err`, `w2-dispatch.err` | **deleted from the worktree** | **none** — `git log --all --diff-filter=A -- .ufo/waves/round-23/<f>` → `adds=0` for each |
| 3 | `.err` capture, tracked | 1: `w2-record.err` | **deleted from the tree** | `9e52cb2` (see F3b — it was *not* untracked at closure) |
| 4 | untracked seat scratch | 16 directory entries (residual; see §3c) | **deleted from the worktree**; the directory is gone | **none** — untracked, so no commit records it |
| 5 | assimilation mirror `.ufo/waves/round-23/assimilation/` | 1 collapsed entry, **91 files** behind it | **deleted from the worktree**; the directory is gone | **none** — `git ls-tree -r c90dffd -- .ufo/waves/round-23/assimilation` → `0` |
| 6 | rewrite-in-progress report | 1 `M`: `W2LandedCites.md` (−23/+19, 29 lines vs 34) | **restored** to the committed blob | **none** — blob `ac54b63a9229610ce9381435dc4504f1c1d9c8c9` at `e059a8f`, `c90dffd`, `16fa92f`, `9e52cb2`, `f6f7f45`, `b973fde`, `ad125e8`; worktree 34 lines, clean |
| 7 | late seat append | 1 `M`: `W2Simplifier.md` (+1) | **committed** | `16fa92f90ba6f587a53fec9bf8d7243b5d7ccf4a` (`cb95441` → `9661389`), the only round-23 path changed between `c90dffd` and `ad125e8` |

Supporting sweeps:

```
$ git ls-tree -r --name-only c90dffd -- .ufo/waves/round-23/scratch | wc -l   -> 1034
$ git ls-tree -r --name-only ad125e8 -- .ufo/waves/round-23/scratch | wc -l   -> 0
$ git diff-tree -r --no-commit-id --name-status 9e52cb2 | wc -l               -> 1035
$ ... | grep -v '^D\s\.ufo/waves/round-23/scratch/'                           -> D .ufo/waves/round-23/w2-record.err
$ ls -d .ufo/waves/round-23/{scratch,assimilation}                            -> No such file or directory (both)
$ find . -maxdepth 1 -type f -name '[0-9]*' | wc -l                           -> 0
$ git diff --name-status c90dffd ad125e8 -- .ufo/waves/round-23/w2            -> M W2Simplifier.md
```

**Nothing in the 89 was left neither-deleted-nor-restored-nor-committed.** The disposition is
complete: 86 deleted with no commit record (untracked at the time), 1 deleted by commit, 1 restored
with no commit, 1 committed.

Also outside the 89 and worth naming because a reader will conflate them: the two `M` files that
appeared **during round 24 wave 1**, `corpus/evidence/round-19/selftests/c1.json` and `c3.json`,
are **restored** and carried by **no commit** — their blob is `dd5d6f16a31b18cc9569c4aa1c14621b7242d260`
at both `c90dffd` and `ad125e8` and `git status` on that subtree is empty. The spot-check counted
only 2 `M` at closure, so these were round-24 drift, not members of the 89. `[INFERENCE]` from the
2-`M` count plus `CritNoHarm.md` §2's own observation that they appeared mid-wave.

## 3. The landed composition is wrong in four ways

The lane's superseding statement (`corpus/lessons/round-24.md:86`) reads:

> `git status --porcelain` empty at the round-24 tip; the composition (66 empty numeric files, 4 empty `.err`, untracked seat scratch deleted; 2 rewrite-in-progress files restored; 1 late seat append committed)

**(a) Different metric.** The spot-check measured `git status --porcelain` (collapsed); this
assignment's closure condition and the `m3` counter (`scripts/check-selfassessment.mjs:269`) both use
`--untracked-files=all` (expanded). Under expansion the round-23 closure number was **not 89**: the
91-file assimilation mirror alone contributes 91 entries instead of 1, so the same tree measures
≈179. "89 → empty" and "89 → 0" therefore compare two different instruments. Demonstrated live on
the current tree: 5 collapsed vs 8 expanded for the same five-plus-three files.

**(b) A tracked file is named as untracked.** The spot-check lists `w2-record.err` among the 87 `??`,
but at the reviewed tip it was **tracked**:

```
$ git rev-parse c90dffd:.ufo/waves/round-23/w2-record.err
e69de29bb2d1d6434b8b29ae775ad8c2e48c5391        # empty blob, 0 bytes
$ git cat-file -s c90dffd:.ufo/waves/round-23/w2-record.err   -> 0
```

It was added by `7ac9fff` (ancestor of `c90dffd`: `git merge-base --is-ancestor 7ac9fff c90dffd` →
YES) and deleted by `9e52cb2`. A tracked file cannot appear as `??`, so either the enumeration is
generic or the count includes a path it does not name. Consequence: the 89 cannot be trusted
path-by-path, only class-by-class — and the three genuinely-untracked `.err` captures are three, not
four.

**(c) The numbers do not sum.** 66 numerics + 4 `.err` = 70 of the 87 `??`; the lesson names no
count for scratch or for the assimilation mirror, and its three `M` (2 restored + 1 committed) exceed
the spot-check's two `M`. Residual by my arithmetic: `87 − 67 − 3 − 1 = 16` untracked scratch
directory entries, which the spot-check names only by subtree
(`CritDeterminism/proof/`, `ExecBlobReader/lane-clone/`, `W2C2Counter/`, `W2Determinism/clone/`,
`sibling/`, `W2LandedCites/*.mjs|json`, `W2Log/SOURCES-base.md`, `W2NoHarm/strace*.txt`,
`W2SelfAudit/final-head.json`) — fewer than 16 entries. **The per-path identity of those 16 is
unrecoverable**: they were untracked, are deleted, and were never recorded. That is an unknown, not a
discrepancy I can close.

**(d) "2 rewrite-in-progress files restored" matches no measurable pair.** Under the spot-check's own
2-`M` composition, exactly **one** `M` file was restored (`W2LandedCites.md`) and the other was
committed (`W2Simplifier.md`). The only other restored pair in the repo is the round-19 receipts,
which are not "rewrite-in-progress" and not in the 89. The sentence is unreconciled with either
reading.

## 4. F2 — `C2 after: 0` is contradicted by the lane's own receipts

`claims.json` C2: `"after": 0`, counter field `mismatches`. What the receipts say:

```
$ python3 -c '...corpus/evidence/round-24/c2-tip.json...'
rev=b973fde3c89fb2d3476ad0b6002791b75ec87a27  mismatches=1  clean=False
  counted=[{class: m3-unlanded-paths, claimed: landed, observed: 4}]  superseded=5  couldNotEvaluate=75

$ ...c2-measurements.json...  after = {rev: b973fde…, mismatches: 1, counted:[m3 observed 4], …}
$ ...c2-measurements.json...  before = {rev: 573c99e…, mismatches: 5, …}   # claim says before: 4
```

Live re-runs (with `TMPDIR=/home/vgpnk/tmp-tabi24`, `/tmp` full):

```
$ node scripts/check-selfassessment.mjs --rev ad125e8… --json   -> exit 1
mismatches 1  clean False  couldNotEvaluate 79  superseded 5
counted [{class: m3-unlanded-paths, doc: SCORECARD.md, claimed: landed, observed: 5}]

$ node scripts/check-selfassessment.mjs --rev 573c99e… --json   -> exit 1
mismatches 5  counted [4 × m1-selftest-tally, {m3-unlanded-paths … observed: 5}]
```

Three separate defects here:

1. **The after value is 1, not 0, in every committed artifact and in every re-run.** No receipt in
   `corpus/evidence/round-24/` records `mismatches: 0`. The claim's `after: 0` is unsupported.
2. **The file named `c2-tip.json` records a non-tip revision.** It carries `rev: b973fde`, which is
   `ad125e8`'s parent; the receipt was captured before the tip commit and then committed *at* the
   tip. A receipt named for the tip does not measure the revision that carries it.
3. **`m3` is not revision-scoped.** `m3Findings(repo, docText)` takes no `rev`; line 269 runs
   `git -C repo status --porcelain --untracked-files=all` on the **live worktree**. Hence
   `--rev 573c99e` and `--rev ad125e8` both report the *current* count (`observed: 5` at both). The
   "before 89 / after 0" delta is not a measurement over revisions at all; it is two snapshots of a
   moving worktree, and the baseline value is unreproducible by construction. The baseline receipt's
   `m3 observed: 4` and the tip receipt's `4` likewise reproduce as `5` today.

So the routed defect's own counter cannot certify its closure, and the claim built on it
(`calibration 5 → 0`) is falsified on its stated metric. `[OBSERVATION]` for all numbers above;
the causal reading — that `m3` is a census of the worktree rather than a calibration signal — is
`[INFERENCE]`, and it is what `CritProvince.md` §3.2 predicted before the code shipped.

## 5. Durability: the guard does not cover the class it is credited with

Round 23's routed defect 3 was 1,034 **committed** scratch paths, closed by deletion at `9e52cb2`
plus the structural rule at `2d76938`:

```
$ cat .gitignore
.ufo/interactive-sessions/
# Round 24 (M5, routed defect 3): …
.ufo/waves/*/scratch/
```

That rule covers **only** `scratch/`. Routed defect 2's classes were **not** scratch:

```
$ git check-ignore -q .ufo/waves/round-24/w2-dispatch.err      -> NOT-IGNORED
$ git check-ignore -q .ufo/waves/round-24/gen-w2.mjs           -> NOT-IGNORED
$ git check-ignore -q .ufo/waves/round-24/w2-spec.json         -> NOT-IGNORED
$ git check-ignore -q .ufo/waves/round-24/w2-dispatch.json     -> NOT-IGNORED
$ git check-ignore -q .ufo/waves/round-24/w2/swarm-registry.json -> NOT-IGNORED
$ git check-ignore -q .ufo/waves/round-23/scratch/x            -> IGNORED (.gitignore:5)
```

The `*.err` capture, the `*-dispatch.*` / `*-spec.json` scaffolding, the numeric-named scratch files
(which were written at the **repo root**, outside `.ufo` entirely) and the assimilation mirror are all
unguarded. They are also already back: `w2-dispatch.err` (0 bytes, the exact shape of three of the
89) exists at the tip and is unignored. Wave-2 seats writing into `w2/` grew the untracked set from 5
to 8 in eight minutes. **The structural claim "the over-commit class cannot recur" is true for
`scratch/` only; the unlanded-path class of routed defect 2 has no structural guard and is
reproducing at the tip.** `[OBSERVATION]` for every check-ignore and count.

## 6. What was neither

Among the 89: **nothing.** All seven classes resolve to deleted, restored, or committed (§2).

Outside the 89: the **8 currently untracked paths** (§1) are neither — they are unlanded at the tip
right now, 0 of them committed, 0 of them ignored, and none of them exists in any round-23 class
list. Wave-1's dispatch artifacts (`gen-w1.mjs`, `w1-dispatch.json`, `w1-spec.json`) *were*
committed at `f6f7f45`; the wave-2 equivalents were not. Whether the L1 commits or removes them at
closure is the open question, and the answer decides whether defect 2 reopens with a different count.

## 7. Residual risk and verification gaps

- **Cannot be closed by me:** the per-path identity of the 16 residual untracked-scratch entries
  (§3c) and the exact file list behind the round-23 assimilation entry. Both were untracked, both are
  deleted, neither was recorded. Their absence is verified; their identity is an unknown.
- **Snapshot, not a reproduction:** every statement about the worktree here is a moment-in-time
  observation that drifts while the wave writes (5 → 8 during this review). Only the committed-bytes
  statements (§2 commit/blobs, §4 receipts) are stable.
- **Not verified:** whether the two differing assimilation files (`corpus/SOURCES.md`,
  `csrf-defense-shape-boundary.md`) lost anything unique when deleted — `RevScratchCleanup.md` (d)
  shows the committed counterparts supersede them, which I did not re-run.
- **Not verified:** `check-selfassessment.mjs --selftest` (13 cases per the claim). Its `m3-clean-tree`
  case (`:409`) tests a clean tree only, which is why `m3`'s revision-blindness survived the matrix —
  `[INFERENCE]` from the case id and the absent `rev` parameter, not from running it.
- **Deliberately out of scope:** the `couldNotEvaluate: 79` surface and the `superseded: 5`
  semantics (C2's kill rule), and C1/C3's own claims. One observation that belongs to whoever owns
  C2: `couldNotEvaluate` grew 75 → 79 between the two receipts with no stated cause.

No tool was installed or upgraded; no service, browser, or network call was made; no git write, no
tracked file edited.
