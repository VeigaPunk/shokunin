# scout.md — aggregator L1 round 10, seat `CorpusSurface`

Read-only reconnaissance of the 13 omitted child corpora named in
`.ufo/waves/aggregator-r10/before.json`, plus the discovery/conf cross-check the
selection contract needs. No code edits, no tests, no config execution.
Paths / counts / revisions only — no corpus prose, no credential material.

## Axis named

Axis 9 (corpus review coverage). Move: make default fleet corpus selection the
set of local child lanes, so the corpus-review axis stops reporting a 6/19
coverage that is an artifact of a hardcoded list.

## Commands used (all read-only)

```
# discovery regex, physical dirs only, no traversal of symlinks
find . -maxdepth 1 -type d -regextype posix-extended \
  -regex '\./[a-z0-9][a-z0-9-]*-shokunin' -printf '%f\n' | sort
# symlinked candidates (must be excluded from discovery)
find . -maxdepth 1 -type l -regextype posix-extended \
  -regex '\./[a-z0-9][a-z0-9-]*-shokunin' -printf '%f\n'
# conf roster, parsed with grep only (never shell-sourced)
grep -oE '^[a-z0-9-]+\|[^|]+\|' shokunin.conf
# per-lane surfaces / volume / git state
ls -1 <lane>/corpus ; find <lane>/corpus -type f | wc -l
find <lane>/corpus -type l | wc -l
git -C <lane> rev-parse --short HEAD ; git -C <lane> status --porcelain | wc -l
git -C <lane> ls-files -- corpus/ | wc -l
git -C <lane> ls-files --others --exclude-standard -- corpus/ | wc -l
# gate source read (not run against the 20 GB trees)
read .ufo/waves/round-9/corpus-gate.mjs:165 (DEFAULT_REPOS), :317 (gradeCorpus), :806 (main)
```

`DEFAULT_REPOS` (`.ufo/waves/round-9/corpus-gate.mjs:165`) is a hardcoded list of 6:
`kasegi, kengaku, kake, kumitate, kotoba, kagi`. `main()` `--all` uses
`o.repos || DEFAULT_REPOS` (`:851`); there is **no** dynamic discovery.

## Cross-check: local dirs vs `shokunin.conf` child IDs

- `shokunin.conf` `LANES` entries: 21 total; `protocol|.` and `aggregator|.` map to
  the fleet repo itself; **19** entries name a `*-shokunin` child dir.
- Physical top-level dirs matching the selection regex: **19**.
- `comm` set-diff in both directions: **empty**. conf-only 0, dirs-only 0.
- Regex-matching dirs that are symlinks: **0** (so physical-only discovery loses nothing).
- `shokunin.conf` and the `shokunin.conf.full-roster-20261015` backup are byte-identical.

⇒ **No name/count discrepancy.** Discovery-by-regex (19) is exactly the conf roster,
and is a strict superset of the hardcoded 6. The only missing surface is exactly the
13 lanes listed in `before.json`.

## Per-surface map — the 13 omitted lanes

`README`/`QUALITY` = `corpus/README.md` / `corpus/QUALITY.md`; `knowledge`/`lessons` =
directory presence; `lessons(n)` = lesson files present. `files`/`text` = recursive
corpus file count / subset with a gate TEXT_EXT extension (r8 scope).

| lane | rev | br | dirty | README | QUALITY | knowledge | lessons(n) | other corpus entries | files | text | tracked/untracked |
|---|---|---|---|---|---|---|---|---|---|---|---|
| audio-shokunin | d9aa6f9 | main | 463 | **MISS** | **MISS** | ok | **MISS** | artifacts, fixtures, live | 123860 | 65747 | 21637 / 6681 |
| chousa-shokunin | 34774a1 | master | 1 | ok | ok | ok | ok(**0**) | — | 4 | 2 | 4 / 0 |
| game-dev-2d-shokunin | 884a4c4 | main | 76 | ok | **MISS** | ok | ok | fixtures, live | 691718 | 58471 | 44317 / 228338 |
| game-dev-3d-shokunin | db64943 | main | 1 | ok | **MISS** | ok | ok | artifacts, fixtures, live, predecessor | 89626 | 19707 | 226 / 0 |
| kaidoku-shokunin | 6645585 | main | 0 | ok | ok | ok | ok | — | 80 | 78 | 80 / 0 |
| kama-shokunin | c390918 | master | 0 | ok | **MISS** | ok | ok | — | 16 | 16 | 16 / 0 |
| lore-shokunin | 5eb9451 | main | 3 | ok | **MISS** | ok | **MISS** | fixtures, live | 1532 | 1532 | 1532 / 0 |
| mado-shokunin | bb08dd5 | master | 0 | ok | ok | ok | ok | — | 25 | 25 | 25 / 0 |
| mori-shokunin | 0715198 | master | 0 | ok | ok | ok | ok(**0**) | — | 5 | 3 | 5 / 0 |
| revenger-shokunin | 286033c | main | 0 | **MISS** | **MISS** | ok | ok | fixtures, live, 11 `verify_*.py` at corpus root | 457 | 365 | 457 / 0 |
| tabi-shokunin | c24eaea | master | 0 | ok | ok | ok | ok | evidence, handoffs | 1818 | 1388 | 1818 / 4 |
| tameshi-shokunin | 284ab0f | master | 0 | ok | ok | ok | ok | — | 22 | 22 | 22 / 0 |
| tsukuroi-shokunin | 0ecf3ff | master | 0 | ok | ok | ok | ok(**0**) | — | 26 | 26 | 26 / 0 |

### Missing paths, explicit

- `corpus/README.md` **absent** → `audio-shokunin`, `revenger-shokunin`.
  Gate effect: r7 finding "corpus/README.md is absent — no index exists"
  (`gradeCorpus`, README branch). `revenger` also has no index to resolve r7 rows
  against, so its `corpus/fixtures/**` + root `verify_*.py` never get index rows.
- `corpus/lessons/` **dir absent** → `audio-shokunin`, `lore-shokunin`.
- `corpus/lessons/` **present but no lesson `.md`** → `chousa-shokunin` and
  `mori-shokunin` hold a lone `.gitkeep`; `tsukuroi-shokunin` is bare empty.
  Gate effect identical in all three: r2 sees no `lessons/*.md` to check, r10 still
  fires (no round-10 aggregator lesson).
- `corpus/QUALITY.md` **absent** → `audio`, `game-dev-2d`, `game-dev-3d`, `kama`,
  `lore`, `revenger` (6 of 13; 6 of 19 fleet-wide). **The gate never grades
  QUALITY.md** — no rule reads it: r4 scans only `knowledge/`, `lessons/` and
  `corpus/README.md`, r7 reads only `corpus/README.md`, and r8 only counts
  credential shapes. So this layout hole is invisible to any verdict the gate
  can emit.
- `corpus/lessons/round-10-aggregator-*.md` **absent in all 13** (and in the 6
  covered lanes). Every one of the 19 lanes will emit exactly one r10 finding.
- All 19 lanes have `corpus/` and an own `.git` **directory** (independent repo, not
  a worktree/submodule gitfile); none is a symlink.

## Layout / volume anomalies the gate handles unexpectedly

1. **Live vs frozen asymmetry (ignored scratch trees).** `walk()` recurses the whole
   `corpus/` tree, so live mode grades ignored/untracked scratch bytes that
   `--snapshot` (`git archive`) cannot see:
   - `audio`: 21637 tracked + 6681 untracked, but 123860 files on disk
     (≈95542 gitignored). `corpus/.gitignore` + nested `corpus/live/*/…` ignores.
   - `game-dev-2d`: 44317 tracked + 228338 untracked vs 691718 on disk
     (≈419063 ignored; 29 nested `.gitignore` files under `corpus/`).
   - `game-dev-3d`: 226 tracked, 0 untracked, 89626 on disk (≈89400 ignored;
     58 nested `.gitignore` files). Snapshot corpus is ~0.25% of live corpus.
   ⇒ Live and snapshot verdicts for these three are not comparable, and r8/r7 scan
   cost differs by 2–4 orders of magnitude between modes.
2. **Mirrored nested corpora inside `corpus/live/**`.** `find <lane>/corpus -type f
   -path '*/live/*/corpus/*'`:
   - audio 92290 files (nested lesson `.md` 0), max path depth 14;
   - game-dev-2d 588874 files, 904 nested lesson `.md`, depth 16;
   - game-dev-3d 28713 files, 1745 nested lesson `.md`, depth 15.
   These are real files (not symlinks) in `live/rNN-{baseline,frozen,replica,simplifier,tree}/corpus/…`.
   Gate effect: they enter r8 (text-ext scan) and inflate the r7 under-coverage
   `# note`, but do **not** create false r2/r4/r10 findings — those rules filter
   `f.startsWith('lessons/')` / `'knowledge/'` / `^lessons/round-N-aggregator-`, and the
   nested paths are relative-prefixed with `live/…`, so they are skipped. That
   prefix scoping is the only reason these mirrors are not graded as lane corpus.
3. **Symlinks dropped from the graded set.** `walk()` uses `readdirSync(withFileTypes)`
   and only recurses `isDirectory()` / collects `isFile()`; a symlink dirent is
   neither, so symlinked files/dirs are skipped silently. Counts inside `corpus/`:
   audio 325, game-dev-2d 410, game-dev-3d 2. Examples: audio
   `corpus/live/r74-simplifier/tree/corpus/live/round-10 -> ../../../../round-10`;
   game-dev-2d `corpus/live/r66-simplifier/tree/lessons -> <lane>/corpus/lessons`;
   game-dev-3d `corpus/live/r*/head/corpus/fixtures/three/node_modules -> …`. The
   contract's "no symlink traversal" is satisfied by accident of Node dirent
   semantics, not by an explicit guard — a symlinked *file* is also invisible even
   though it may be the only copy of a corpus entry.
4. **Non-canonical bulk at corpus root.** `revenger` carries 11 `verify_*.py` plus
   `fixtures/` and `live/` at `corpus/` root; `.py` is in `TEXT_EXT`, so r8 scans
   them while r4/r7 never do (not canonical surfaces). Tabi adds `evidence/`,
   `handoffs/` (both in `INDEX_SUBDIRS`, so r7 does resolve rows under them).
5. **`dirty` is worktree-wide, not corpus-scoped.** `revisionStamp` counts
   `git status --porcelain` over the whole lane, so `audio` dirty=463 and
   `game-dev-2d` dirty=76 are dominated by non-corpus user changes; a lane with a
   dirty worktree prints `provisional=1` in the `# tree` line. Corpus-only untracked
   is reported separately (`untrackedCorpus`/`deletedCorpus`, all `deleted=0` here).

## Limits to claiming full semantic CORPUS conformance

- The selection claim is **coverage of local child directories**, not CORPUS
  conformance: 19/19 dirs is reachable, but `gradeCorpus` itself declares r1, r3,
  r5, r6, r9, box-3 verifier independence, and shonen-semantics **not evaluated**;
  r8's schematic-vs-real classification is a declared could-not-evaluate.
- Even with 19/19 selection, three layout surfaces remain ungraded: `QUALITY.md`
  (6 lanes lack it), the `corpus/evidence/**` / root data files that CORPUS.md:9-15
  does not list, and any lane whose only corpus copy is a symlink (item 3).
- Empty `lessons/` dirs (chousa, mori, tsukuroi) and missing `lessons/` dirs
  (audio, lore) are indistinguishable in the emitted verdict: both yield the same
  single r10 row, so the gate cannot distinguish "no round-10 duty emitted" from
  "this lane has no lessons surface at all".
- Live-mode verdicts for audio/game-dev-2d/game-dev-3d rest on gitignored scratch
  bytes, so a live `clean`/`failed` result for those three is not reproducible from
  the lane's committed revision; only `--snapshot <commit>` is revision-anchored.
- Exit semantics to preserve: `2 > 3 > 1 > 0`; a discovered dir with corpus absent
  yields CNE (2) inside `gradeCorpus`; an independent repo whose `git rev-parse HEAD`
  fails yields CNE (2) in `runLive`. All 19 lanes currently pass both preconditions,
  so post-fix `--all` exit stays 1 (r10 fires everywhere) and the summary line count
  becomes 19 — [INFERENCE] from the source read; not measured (grading the 20 GB
  live trees was deliberately not run).

## Pointers for the regression seat

- Selection fix site: `.ufo/waves/round-9/corpus-gate.mjs:165` (`DEFAULT_REPOS`) and
  the `--all` branch at `:851`; empty discovery must exit 2 with an explicit
  coverage note (contract), and `--repos` must stay a literal override.
- Preconditions every discovered lane satisfies today: `corpus/` exists, `.git/` is a
  real dir, `rev-parse HEAD` succeeds (revisions in the table above).
- Baseline: `.ufo/waves/aggregator-r10/before.json` (covered=6, omitted=13) and
  `.ufo/waves/aggregator-r10/before-summaries.log`.
- Do not regenerate frozen snapshots by grading the big lanes live; use
  `--snapshot <lane> <commit>` if a revision-anchored verdict is needed.