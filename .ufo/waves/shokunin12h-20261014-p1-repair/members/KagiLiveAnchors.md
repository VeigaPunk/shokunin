# KagiLiveAnchors

Advisory measurement only. Not a native judge verdict, lane round report, receipt, or admission. No lane file was edited. Gate implementation files were left to GateRepair; this seat found no remaining gate defect in the live OMP-anchor set.

Axes judged: freshness (anchors remeasured at the current source revision), operability (claims must be re-runnable commands), calibration (literal grep versus path-shaped citations), adjacency (host pins and the UFO tree are different objects).

## Revisions

| Object | Command | Measured |
|---|---|---|
| Lane HEAD | `git -C /home/vgpnk/Projects/shokunin/kagi-shokunin rev-parse HEAD` | `fecee8743e52eb8fb5fbb40782934cb619a1a96e` (matches `baselines.json` kagi.head; subject `round-18: OMP/ufo-fsd re-census…`) |
| Lane parent | `git rev-parse HEAD^` | `4e48b771a3d8bd3a76f5ade605721d2252487ba9` (SCORECARD round-18 pre-move `4e48b77`) |
| Lane worktree | `git status --porcelain` | `?? plans/` only (parent WWKD plan; not a lane claim) |
| Source tree | first existing of `~/Projects/ufo-fsd-alpha`, `~/Projects/origin-work/ufo-fsd-alpha` | `/home/vgpnk/Projects/ufo-fsd-alpha` exists; origin-work copy absent |
| `$UFO_SRC` | shell expansion | unset. Explicit bad `--src` was not in play: no lane script reads it |
| Source HEAD | `git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD` | `964f443ee53df0ce06bd689af01f0dea031b01f9` (2026-10-12 18:32:12 -0300, `routing: regenerate omp-seat-routing mirror…`) |

## Live claim set

Currently live OMP-derived claims are the round-18 statements that this repo cites the origin tree. They are still cited as current evidence (`SCORECARD.md:314` → `corpus/lessons/round-18.md`; `corpus/README.md:75`). Host `drift-symbols.tsv` / `drift-baseline.tsv` pins are not in this set: none of their basenames or content hashes exist in the source tree (boundary section).

## Measurements

### 1. Literal count pin — `grep` empty

Claim, still live: `corpus/lessons/round-18.md:7-8` says `` `grep -r 'origin-work|ufo-fsd'` is empty ``. `SCORECARD.md:314` says zero `origin-work`/`ufo-fsd` citations exist anywhere in this repo. `LOG.md:725` repeats the empty-grep sentence.

Command at lane HEAD:

```
git grep -n -E 'origin-work|ufo-fsd' -- . ':(exclude).git'
```

Output: 9 lines, 5 files. Exit of a no-match grep is not what this returns.

- `LOG.md:722`, `:723`, `:725`
- `SCORECARD.md:314`
- `corpus/README.md:75`
- `corpus/knowledge/substrate-deferral.md:3`
- `corpus/lessons/round-18.md:1`, `:4`, `:7`

Same command at parent `4e48b771a3d8bd3a76f5ade605721d2252487ba9`: exit 1, no lines. The pin was true before the round-18 commit and false after that commit quoted its own search terms.

Classification: **genuine defect** of a re-runnable count pin. Not line-drift (no source file moved). Not stale `--src`. Not citation-to-deleted. The nine hits are narrative self-description, not paths.

Proposed correct anchor, at lane `fecee874` and source `964f443e`:

```
git grep -n -E 'origin-work/|ufo-fsd-alpha/|Projects/ufo' -- . ':(exclude).git'
```

Measured: no output, exit 1, for each of `origin-work/`, `ufo-fsd-alpha/`, `Projects/ufo`, and `~/Projects/ufo-fsd-alpha`. Keep the round-18 sentence as historical (true at `4e48b77`). Do not rewrite it to claim the literal grep is still empty.

### 2. Stale `--src`

Claim: `corpus/lessons/round-18.md:66` — stale `--src` / origin-path failures = 0.

```
git grep -n -- '--src' -- '*.sh' '*.mjs' '*.py'
git grep -n -E 'UFO_SRC|origin-work|ufo-fsd' -- '*.sh'
```

Both: no matches. No corpus script resolves a source root.

Classification: **confirmed empty**, not a defect. Vacuous satisfaction still holds. Do not add a `$UFO_SRC` resolver; there is no consumer. Explicit bad `--src` cannot be demonstrated because the flag is absent.

### 3. Citation-to-deleted

Claim: `corpus/lessons/round-18.md:67` — upstream-deleted-file citations = 0.

Path-shaped search above is empty. Additional identity tokens absent from the lane (`git grep` exit 1): `964f443`, `ee907f1`, `ACCESS.md`, `OPERATOR-CREDENTIALS`, `ufo-fsd-alpha/`.

Source files that mention the handler by name, and that kagi does **not** cite:

- `docs/ACCESS.md:14` — historical presence-only note that `the-janitor` was under `~/.local/bin`. File header marks the snapshot historical (2026-09-10). Not a line pin.
- `docs/OPERATOR-CREDENTIALS.md:17` — same class, host-bin name only. Content not read past that grep line.

Classification: **confirmed empty**. The origin-work tree is absent, but this lane never cited a file inside it, so there is no deleted-file citation to repair. Not line-drift.

### 4. Moved-file line drift

Claim: `corpus/lessons/round-18.md:68` — moved-file line drift = 0.

Live symbol pins (`corpus/drift-symbols.tsv`, 20 data rows) name these basenames: `the-janitor`, `client.py`, `opencode.json`, `op.env`, `janitor.md`, `janitor_auth.ts`, `tac-check`, `handoff-status.json`.

Against source `964f443e`:

```
git ls-files | rg 'janitor|tac-check|fnm-nudge|1password'
git grep -l MODEL_ENDPOINT
git grep -l -e 'exec op run --env-file'
git grep -l THE_JANITOR_REQUEST_TIMEOUT
```

All empty (`MODEL_ENDPOINT` file count 0; janitor-named tracked paths 0). No `file:line` token in the lane points at `crates/`, `packages/`, `ports/`, or `scripts/` inside the source tree.

Classification: **confirmed empty**. Not line-drift: there is no source object that moved. There is also no proposed replacement line. Inventing one would fabricate an anchor.

### 5. Hash pins versus source blobs

The nine non-withheld hashes in `corpus/drift-baseline.tsv` (`2408b0c9…`, `8179b241…`, `a318e719…`, `b270d762…`, `c17e2638…`, `2382d5af…`, `0d8b7c16…`, `af95ca97…`, `05e1cd94…`) were compared to sha256 of tracked source files.

Command: Python `hashlib.sha256` over `git ls-files` regular files, skipping path components `credentials`/`oauth` and `*.token` (8 skipped, contents not read). `git grep` of those hash prefixes across the source tree: exit 1.

Measured: `tracked_files=1717 hashed=1709 skipped_secretish=8 pin_matches=0`.

The lesson's `2eb86e1f…` (`corpus/lessons/round-18.md:60`) is not an OMP hash and is not in `corpus/stamps.tsv` or `corpus/drift-baseline.tsv`. Current pin-file prefixes are `90c2d7a52360` (`drift-baseline.tsv`), `dca651da9183` (`drift-symbols.tsv`), `6846f16e4664` (`stamps.tsv`). The lesson already says the prefix is not re-derivable. Left as historical host narrative.

Classification: **not OMP hashes**. No hash drift against this tree, because none of the pins are this tree.

## Boundary — declared host surfaces are not OMP anchors

Shape only. No `op.env`, oauth, token, or session bytes were read. `~/.config/opencode/opencode.json` is mode `600` now, so its bytes and line count were not hashed into this report (lane hash policy already withholds 0600 content).

`os.lstat` of the 15 `drift-baseline.tsv` paths: 14 absent. The survivor is `$HOME/.config/opencode/opencode.json` (`file`, mode `600`; pin says `644`). `$HOME/.config/opencode` direct child count = 3 (names withheld), matching the round-18 host note of 20→3, not a source-tree count.

Those absences are the already-named substrate debt. They are not line-drift against `964f443e`.

## Proposed delta

No implementation change. No baseline re-pin. No `--src` addition.

Parent/record owner, append-only erratum only: the literal `origin-work|ufo-fsd` grep is no longer empty (9 narrative lines at `fecee874`); the path-shaped anchor above is the re-runnable form and is empty. Do not delete the round-18 sentence.

GateRepair: no remaining defect in this cluster. Do not invent a source-root default.

## Unresolved debt

- Literal grep self-invalidation. Unblock: append the erratum and cite the path-shaped command. Owner: kagi record / parent, not GateRepair.
- Substrate absence (14/15 pin paths gone; one survivor mode `644`→`600`, content unread). Unblock: reinstall the handler tree, or a reviewed host re-pin if the loss is permanent. Already carried in SCORECARD round-18 debt. Owner: operator / kagi province. Not an OMP anchor.
- `docs/ACCESS.md:14` and `docs/OPERATOR-CREDENTIALS.md:17` are uncited historical host-presence notes. Not defects. Owner: UFO docs, outside this lane.

## Cross-domain owner

Source relocation (`origin-work/ufo-fsd-alpha` absent, tree now `~/Projects/ufo-fsd-alpha` at `964f443e`) belongs to the fleet/kumitate source checkout, not kagi. This lane has no path citation to retarget. Contested host surfaces (opencode ownership, musketeer profile) stay with the integrator / kake as already partitioned; this measurement does not adjudicate them.

Confidence: high on the empty path-citation, empty `--src`, empty basename, and zero hash-match results (commands above, this revision pair). The literal-grep defect is also high: parent exit 1 versus HEAD 9 lines.
