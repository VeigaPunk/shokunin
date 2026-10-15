# Selection seat — round-10 corpus-review axis (2026-10-15)

Single move: replace the six-name hardcoded default of
`.ufo/waves/round-9/corpus-gate.mjs` with physical lane discovery per the
CONTEXT.md discovery contract. File edited in place (snapshot E132 → 9708,
977 lines). No other file written except this report. No build, lint, test,
formatter or gate run by this seat; parent owns all verification.

## What changed (behavior)

- **Default `--all` (no `--repos`)** now calls `discoverLanes(MAIN_ROOT)`:
  `readdirSync(withFileTypes)`, filter `isDirectory() && !isSymbolicLink()`,
  anchored `LANE_DIR_RE = /^[a-z0-9][a-z0-9-]*-shokunin$/` (the former
  DEFAULT_REPOS list is deleted; only a historical comment names it), plain
  code-unit sort (same comparator as `walk()`, no localeCompare), no caching —
  re-discovered every invocation. MAIN_ROOT stays script-derived (`:113`), so
  a `--gate` replay copy under a fixture tree discovers THAT tree.
- **Membership is name-based only** — never filtered on corpus or git
  presence: a qualifying dir without `corpus/` still gets its per-lane exit-2
  row (gradeCorpus, unchanged), and the enum-time-race absent-dir row is kept.
- **Parent Git inheritance rejected, default-only**: before grading a
  discovered lane, `ownGitRoot()` compares realpath of
  `git rev-parse --show-toplevel` against realpath of the lane dir; mismatch
  or failure → visible per-lane exit-2 note (`revision=no-own-git`), never a
  silent omission and never a fleet-HEAD stamp. A legitimate `.git` gitfile
  (linked worktree) passes because the lane itself is the top level.
  `--repo`, `--repos`, `--snapshot` keep round-9 behavior exactly (their
  inheritance was prior behavior; critic C6 / Main accepted that scope).
- **Empty or unreadable default discovery** emits
  `# coverage could-not-evaluate: …` + `# process-exit 2 (could-not-evaluate)`
  and exits 2 with ZERO child/summary rows — the vacuous-clean
  `combineExit([])→0` hole is closed on the default path — and fabricates no
  child row.
- **Explicit `--repos` preserved byte-for-byte**: caller order kept; legacy
  empty list (`--repos ''`) is truthy so it selects the explicit branch →
  zero lanes, no discovery, clean exit 0 as before; missing dirs still emit
  per-lane exit-2 rows; own-git guard not applied.
- **Coverage positive line**: successful discovery prints one
  `# coverage OK: default discovery selected <n> physical lane dir(s) …`
  comment line (names are lane dir names only — metadata, no corpus bytes).

## What was preserved (invariants)

- All grade rules r2/r4/r7/r8/r10/shonen, finding-id scheme
  `CR-<label>-<rule>-<n>`, `# tree` / `# verdict` / `# summary` / `# json`
  line shapes, exit precedence 2 > 3 > 1 > 0, `--round` selector (default 9),
  `--snapshot` frozen-drift path, `--selftest`, `--registry`.
- `corpus-gate.expected.json` untouched (12 selftest cases, 8 frozen keys).
- No exported symbols (file has none); no second hardcoded lane list; no
  semantic rules added.
- Gate id kept `corpus-gate-v1` deliberately: ledger rows and expected.json
  `_provenance.gate` cite that id; records are parent-owned. The rationale is
  recorded in the file header (lines 9-13) so a reviewer sees why a behavior
  change carries no id change — selection set ≠ grading rules.

## Documentation updated (this gate only)

Header block: fleet-of-six → discovered fleet; round-10 change note; verdict
map exit-2 causes extended; new `discovery` registry row; `--repos` added to
entry commands. `REGISTRY.entry.repos` + `REGISTRY.default_discovery` fields,
echoed by `printRegistry()` (`--registry`). `usage:` line now shows
`--all [--repos <dir,dir,...>]` and the discovery default.

## Read-only inspection performed (metadata only, not a gate run)

- 19 physical direct child dirs of MAIN_ROOT match the pattern; none is a
  symlink (`find -maxdepth 1` kind census: 19 × `d`).
- Every one of the 19 already owns its git top level
  (`git rev-parse --show-toplevel` = the lane dir), so on today's fleet the
  own-git guard rejects nothing and all 19 lanes are graded — expected
  default-mode shape: 19 per-lane rows + 19 summary rows + coverage OK line.
- Custody boundary honored: `audio-shokunin`, `game-dev-2d-shokunin`,
  `game-dev-3d-shokunin` are selected by the physical scan (they match the
  pattern and own git roots); the gate reads no shokunin.conf, so the
  discovered local set is NOT equated to the configured 16-lane fleet —
  recorded as a boundary, not a code filter or mint/dormancy item.

## Risks / notes for parent and sibling seats

- Broad corpus score stays 9; only directory coverage changes. Coverage
  semantics: "represented" now = discovered; the 6/19 → 19/19 delta is the
  whole expected scorecard-visible improvement.
- Regression replay of OLD default `--all` at HEAD still shows 6 lanes;
  post-patch shows 19 — expected, not drift. `--repos <six names>` reproduces
  the historical lane set on demand.
- Lanes lacking `corpus/` (unknown to this seat; census will show) surface as
  per-lane exit-2 rows → whole-run process-exit 2 by precedence. That is the
  contract's "failures visible", not a gate bug.
- If MAIN_ROOT itself is unreadable, discovery returns ok:false → same exit-2
  coverage diagnostic, no uncaught stack (main has no try/catch by design).

## Checks the parent should run after integration

`node --check`, `--selftest` (expect 12/12), frozen `--snapshot` re-run
(expect 8 MATCH, exit precedence intact), `--registry`, before/after `--all`
replay via `selection-regression.mjs --gate`, redacted `measure-corpus.mjs`
capture of default `--all` (expect one summary row per qualifying dir, sorted,
coverage OK line, no config-based filtering), explicit `--repos ''` → exit 0,
explicit `--repos` order + legacy missing-dir rows unchanged.
