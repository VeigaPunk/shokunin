# NoteVerifySightingWall — advisory (unjudged)

Independent read-only check of `kumitate-shokunin/corpus/knowledge/sighting-wall.md` against origin `/home/vgpnk/Projects/ufo-fsd-alpha`. This file is data, not a verdict. No note edit, no section add/remove by this member.

## Snapshot

| Tree | Observed |
|---|---|
| Origin HEAD | `964f443ee53df0ce06bd689af01f0dea031b01f9` (`git rev-parse HEAD`), status clean on `scripts/ufo-sighting`, `scripts/ufo-sighting.mjs`, `scripts/ufo-sighting-lib` |
| Lane HEAD at report write | `c64b38078871` (`git -C kumitate-shokunin rev-parse --short=12 HEAD`). Dispatch pin was `175de6ba`; HEAD moved during the wave. `git status --short -- corpus/knowledge/sighting-wall.md SCORECARD.md` printed nothing at write time |
| Note | `corpus/knowledge/sighting-wall.md`, mtime `2026-10-14 21:27:08 -0300`, 11644 bytes, 253 lines. Re-stat after the probe: same mtime, same size, same nine `## ` headings |

## Files inspected

- `kumitate-shokunin/corpus/knowledge/sighting-wall.md` (full)
- `kumitate-shokunin/SCORECARD.md` S4 cell (line 122) and round-32 `## Planned` / executed prose
- `kumitate-shokunin/scripts/claims-check.mjs` (`RE_CHUNK_HEAD`, `RE_EXT`, `RE_PATHISH`, `RE_BARE`, `familyPatterns`, `probeRow`)
- `kumitate-shokunin/scripts/proxy-check.mjs` `LAYER_PATTERNS` (`scripts/proxy-check.mjs:317-319`) and `layerTerms`
- Origin: `scripts/ufo-sighting`, `scripts/ufo-sighting.mjs`, `scripts/ufo-sighting-lib/{base,argv,observe,surface}.mjs` (cited lines, not full files)

## Commands and observed output

```sh
# origin, cwd /home/vgpnk/Projects/ufo-fsd-alpha
git rev-parse HEAD
# 964f443ee53df0ce06bd689af01f0dea031b01f9

find scripts -path './.git' -prune -o \( -name 'ufo-sighting' -o -name 'ufo-sighting.mjs' -o -path '*/ufo-sighting-lib/*' \) -print | LC_ALL=C sort
# scripts/ufo-sighting
# scripts/ufo-sighting-lib/argv.mjs
# scripts/ufo-sighting-lib/base.mjs
# scripts/ufo-sighting-lib/observe.mjs
# scripts/ufo-sighting-lib/surface.mjs
# scripts/ufo-sighting.mjs

wc -l scripts/ufo-sighting scripts/ufo-sighting.mjs scripts/ufo-sighting-lib/*
# 95 scripts/ufo-sighting
# 4714 scripts/ufo-sighting.mjs
# 510 scripts/ufo-sighting-lib/argv.mjs
# 507 scripts/ufo-sighting-lib/base.mjs
# 614 scripts/ufo-sighting-lib/observe.mjs
# 325 scripts/ufo-sighting-lib/surface.mjs
# 6765 total

find scripts/ufo-sighting-lib -type f | wc -l
# 4

git ls-tree -r --name-only 5725fa7d3 -- scripts/ufo-sighting-lib | wc -l
# 26

comm -23 \
  <(git ls-tree -r --name-only 5725fa7d3 -- scripts/ufo-sighting-lib | sed 's|.*/||' | LC_ALL=C sort) \
  <(find scripts/ufo-sighting-lib -type f -printf '%f\n' | LC_ALL=C sort)
# 22 names, identical to the note's removal list (display-overview.mjs …
# wall.mjs). comm -3 on full paths (both sides LC_ALL=C sort) is those 22
# deletions only; no live path is absent from 5725fa7d3.

for f in scripts/ufo-sighting.mjs scripts/ufo-sighting \
  scripts/ufo-sighting-lib/base.mjs scripts/ufo-sighting-lib/argv.mjs \
  scripts/ufo-sighting-lib/observe.mjs scripts/ufo-sighting-lib/surface.mjs \
  scripts/ufo-sighting-lib/wall.mjs scripts/ufo-sighting-lib/spawn-pane.mjs; do
  test -f "$f" && echo present $f || echo absent $f
done
# present: the six live paths. absent: wall.mjs, spawn-pane.mjs
```

Top-level non-`.mjs` under `scripts/` includes `scripts/ufo-sighting`. `LAYER_PATTERNS.S` is `^scripts/[^/]+\.mjs$` and `^scripts/[^/]+/.+`, so the shim is **not** an `S_members` file. Walk observed `scripts/*.mjs` = 73, nested `scripts/*/` files = 18 (matches the dispatch census; not re-derived as a layer total here).

```sh
# lane
grep -n '^## ' corpus/knowledge/sighting-wall.md
# 8 Membership and measurement
# 83 `scripts/ufo-sighting.mjs`
# 121 `scripts/ufo-sighting`
# 144 `scripts/ufo-sighting-lib/base.mjs`
# 165 `scripts/ufo-sighting-lib/argv.mjs`
# 188 `scripts/ufo-sighting-lib/observe.mjs`
# 211 `scripts/ufo-sighting-lib/surface.mjs`
# 231 Boundary crossings (still true at HEAD `964f443e`)
# 243 Traps

grep -n '^| S4 |' SCORECARD.md
# 122:| S4 | sighting wall | `ufo-sighting.mjs` (396 L) + `ufo-sighting` (224 L bash) + `ufo-sighting-lib/` (4 files) | yes — sighting-wall |

node scripts/claims-check.mjs --row S4 --json --src /home/vgpnk/Projects/ufo-fsd-alpha
# verdict MATCH; sections=6; errors=0; warnings=1
# warn SECTION_FILE_NOT_MEMBER: scripts/ufo-sighting is outside S4's declared members
# inFamily true: the five *.mjs sections (anchors 19/16/13/11/12, all live, symbolHit true)
# inFamily false: scripts/ufo-sighting (anchors 9, live true, symbolHit true)
```

An independent replica of `RE_CHUNK_HEAD` / `RE_PATHISH` / `RE_BARE` / symbol filter against the same note and origin walk agreed: 6 member headings, 0 unresolved, 0 dead own-file anchors, symbolHit on every member section.

Symbol-on-cited-line spot check (80 anchors): 78 lines contain the named symbol. Two gate-live anchors do not:

- `scripts/ufo-sighting-lib/base.mjs:111` is `  }` (constructor closer). `export function emitFatal(error)` is line 116. The note says `` `:111` region ``. Gate-live; symbol is in the file, not on the cited line.
- `scripts/ufo-sighting-lib/surface.mjs:18` is `];`. The four lib paths are lines 14–17; line 13 is `const SURFACE_MODULE_PATHS = [`. The en-dash cite is a span, not a claim that line 18 contains `surface.mjs`.

## Member list derived

Live origin set the note declares, confirmed by `find` + `test -f` + `wc -l`:

1. `scripts/ufo-sighting.mjs` — 4714 L — section at note:83 — own-file anchors live — `inFamily` true
2. `scripts/ufo-sighting` — 95 L — section at note:121 — own-file anchors live — `inFamily` **false** under the current cell
3. `scripts/ufo-sighting-lib/argv.mjs` — 510 L — section at note:165 — live — `inFamily` true
4. `scripts/ufo-sighting-lib/base.mjs` — 507 L — section at note:144 — live — `inFamily` true
5. `scripts/ufo-sighting-lib/observe.mjs` — 614 L — section at note:188 — live — `inFamily` true
6. `scripts/ufo-sighting-lib/surface.mjs` — 325 L — section at note:211 — live — `inFamily` true

Gate-visible family patterns from the current S4 cell (`familyPatterns`: backtick must contain `/` or `*` or match `RE_EXT`): `ufo-sighting.mjs`, `ufo-sighting-lib/`. The backtick `` `ufo-sighting` `` is dropped (no slash, no star, no extension). That is why the shim section warns `SECTION_FILE_NOT_MEMBER` even though the cell names it in prose.

`ufo-sighting-lib/` matches the four live lib files only. No fifth lib file exists.

## Sections

| `## ` heading | Names a member? | Member in live tree? | Own-file anchor live? |
|---|---|---|---|
| Membership and measurement | no (topic) | n/a | n/a |
| `` `scripts/ufo-sighting.mjs` `` | yes | present | yes (19/19) |
| `` `scripts/ufo-sighting` `` | yes | present | yes (9/9); not an S4 pattern token |
| `` `scripts/ufo-sighting-lib/base.mjs` `` | yes | present | yes (16/16) |
| `` `scripts/ufo-sighting-lib/argv.mjs` `` | yes | present | yes (13/13) |
| `` `scripts/ufo-sighting-lib/observe.mjs` `` | yes | present | yes (11/11) |
| `` `scripts/ufo-sighting-lib/surface.mjs` `` | yes | present | yes (12/12) |
| Boundary crossings (still true at HEAD `` `964f443e` ``) | no (`RE_CHUNK_HEAD` requires the chunk to start with a backtick; `964f443e` is not a path) | n/a | n/a |
| Traps | no | n/a | n/a |

**Sections whose member is absent:** none. No `## ` heading names a file missing from origin HEAD `964f443e`. The 22 deleted lib basenames appear only in the removal record (note:56-61), not as member headings. `test -f` on `wall.mjs` and `spawn-pane.mjs` is false.

**Declared members with no section:**

- Note-declared live 6: none missing.
- Gate-pattern live 5 (`ufo-sighting.mjs` + four under `ufo-sighting-lib/`): none missing.
- The shim is named in the cell and has a section; it is not a missing section. It is an uncounted pattern.

**Sections added/removed by this member:** none.

## Honest count

- Member-form `## ` sections that resolve to a live file and carry ≥1 live own-file anchor: **6**
- Of those, `inFamily === true` (what `layerTerms` adds to `S_sections`): **5**
- Absent-member sections: **0**
- Live declared members lacking a section: **0**
- Phantom member headings: **0**
- Topic `## ` headings (not member sections): **3**

Do not read the note's "6 of 6" as +6 `S_sections`. The frozen layer walk will credit **5** from this note until the S4 cell's shim token is path-like. Making it path-like (`` `scripts/ufo-sighting` ``) would flip `inFamily` to true and add 1 to `S_sections` for a file `LAYER_PATTERNS` does not count in `S_members`.

Registry cell line counts are stale relative to this measurement: cell says `ufo-sighting.mjs` 396 L and `ufo-sighting` 224 L; live `wc -l` is 4714 and 95. Lib count in the cell is already `(4 files)`, which matches `find … | wc -l`. The note's membership prose still quotes the pre-restructure `(26 files / 10620 L)` cell; that quote is not the cell on disk now.

`RE_FILES` sees `4 files`. Distinct sections are 6, which is not `< 4`, so `MEMBER_COUNT_SUSPECT` did not fire. There is no `N members` token, so `MEMBER_COUNT_DRIFT` did not fire. `--row S4` was `MATCH` with the one warn above. Not a round verdict.

## Unresolved

- Whether the parent should keep the shim section out of `S_sections` (current gate behavior) or change the cell token. Not decided here.
- `emitFatal` cite is five lines above the function. Gate does not care; a stricter symbol-on-line rule would.
- Non-verbatim backticks that do not fail the gate because other symbols hit: `UFO_SIGHTING_ATTACH=1` (file has `UFO_SIGHTING_ATTACH:-`), `unavailable(…)`, `queued|working|suspended|completed|unknown`, `fail("CODE"`.

## Cross-domain (owner)

- **Parent / stanza:** S4 cell still carries 396 L and 224 L; shim backtick is invisible to `familyPatterns`; crediting the shim as in-family would increment `S_sections` without incrementing `S_members`. Note quote of the 26-file cell is behind the cell now on disk (`(4 files)`).
- **S1 / S6 / S8:** Boundary section names `fleet-dispatcher.mjs`, `ufo-l0-watch.mjs`, `ufo-state-retention.mjs`, `run-omp-native-trial.mjs` as other families, with no own-file anchors in this note. Not S4 members. No defect measured.
