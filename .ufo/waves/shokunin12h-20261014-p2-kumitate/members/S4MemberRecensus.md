# S4MemberRecensus — round-32 script-layer re-census (family S4)

**Seat:** `S4MemberRecensus` (leaf). **Family:** S4 sighting wall.  
**Lane:** `kumitate-shokunin` HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4`.  
**Origin:** `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443e` (`964f443ee53df0ce06bd689af01f0dea031b01f9`).  
**Scope:** live membership + note section honesty only. Registry row / proxy stanza not edited (parent-owned).

## Axes (named, not judged)

- **coverage:** S4 live set vs note `##` member sections vs claims gate.
- **operability:** every count carries its command; anchors re-open in origin files.
- **calibration:** frozen registry cell (28-path / “26 files” reading) vs live 6.

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | registry row S4; round-32 `## Planned` |
| `kumitate-shokunin/corpus/README.md` | map row → `knowledge/sighting-wall.md` (stale “26 files”) |
| `kumitate-shokunin/corpus/knowledge/sighting-wall.md` | S4 family note (edited this seat) |
| `kumitate-shokunin/scripts/claims-check.mjs` | member-section gate |
| origin `scripts/ufo-sighting.mjs` | S4 member |
| origin `scripts/ufo-sighting` | S4 member (bash shim) |
| origin `scripts/ufo-sighting-lib/argv.mjs` | S4 member |
| origin `scripts/ufo-sighting-lib/base.mjs` | S4 member |
| origin `scripts/ufo-sighting-lib/observe.mjs` | S4 member |
| origin `scripts/ufo-sighting-lib/surface.mjs` | S4 member |

## Live membership (origin tree)

**Command (exact list + sort):**

```bash
cd /home/vgpnk/Projects/ufo-fsd-alpha
{ printf '%s\n' scripts/ufo-sighting.mjs scripts/ufo-sighting
  find scripts/ufo-sighting-lib -type f
} | LC_ALL=C sort -u
```

**Observed output:**

```
scripts/ufo-sighting
scripts/ufo-sighting-lib/argv.mjs
scripts/ufo-sighting-lib/base.mjs
scripts/ufo-sighting-lib/observe.mjs
scripts/ufo-sighting-lib/surface.mjs
scripts/ufo-sighting.mjs
```

**Count command:**

```bash
{ printf '%s\n' scripts/ufo-sighting.mjs scripts/ufo-sighting
  find scripts/ufo-sighting-lib -type f
} | LC_ALL=C sort -u | wc -l
```

**Observed:** `6`

**Sizes (`wc -l` at origin HEAD `964f443e`):**

```bash
wc -l scripts/ufo-sighting.mjs scripts/ufo-sighting \
  scripts/ufo-sighting-lib/argv.mjs scripts/ufo-sighting-lib/base.mjs \
  scripts/ufo-sighting-lib/observe.mjs scripts/ufo-sighting-lib/surface.mjs
```

| Member (repo-relative) | Live `wc -l` |
|---|---:|
| `scripts/ufo-sighting.mjs` | 4714 |
| `scripts/ufo-sighting` | 95 |
| `scripts/ufo-sighting-lib/argv.mjs` | 510 |
| `scripts/ufo-sighting-lib/base.mjs` | 507 |
| `scripts/ufo-sighting-lib/observe.mjs` | 614 |
| `scripts/ufo-sighting-lib/surface.mjs` | 325 |
| **total** | 6765 |

### Exact member list (authoritative for this seat)

1. `scripts/ufo-sighting.mjs`
2. `scripts/ufo-sighting`
3. `scripts/ufo-sighting-lib/argv.mjs`
4. `scripts/ufo-sighting-lib/base.mjs`
5. `scripts/ufo-sighting-lib/observe.mjs`
6. `scripts/ufo-sighting-lib/surface.mjs`

**Declared count the registry row must carry:** **6**

## Registry row S4 (read-only compare)

**Source:** `SCORECARD.md` surface registry, row `| S4 | sighting wall | … |`

**Frozen cell (unchanged by this seat):**

```
`ufo-sighting.mjs` (396 L) + `ufo-sighting` (224 L bash) + `ufo-sighting-lib/` (26 files / 10620 L)
```

| Claim in frozen cell | Live measurement | Delta |
|---|---|---|
| `ufo-sighting.mjs` 396 L | 4714 L | +4318 (lib inlined into entry) |
| `ufo-sighting` 224 L bash | 95 L | −129 |
| `ufo-sighting-lib/` 26 files / 10620 L | 4 files / 1956 L | −22 files |
| Implied path members ≈ 1+1+26 = **28** | **6** | −22 |

**Corpus map:** `corpus/README.md` still says primary sources
`scripts/ufo-sighting-lib/` (26 files) — stale map prose; parent may refresh.

**Parent action (not done here):** rewrite the S4 members cell to the six live
paths and **declared count 6**. Prefer path-form backticks so the bash shim is
visible to `familyPatterns` (see claims warnings below): e.g.
`` `scripts/ufo-sighting.mjs` + `scripts/ufo-sighting` + `scripts/ufo-sighting-lib/` (4 files) ``
or an explicit `6 members: …` integer the gate can read.

## Historical lib deletion set (for parent boundary arithmetic)

```bash
comm -23 \
  <(git -C /home/vgpnk/Projects/ufo-fsd-alpha ls-tree -r --name-only 5725fa7d3 -- scripts/ufo-sighting-lib \
      | sed 's|.*/||' | LC_ALL=C sort) \
  <(find /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-sighting-lib -type f -printf '%f\n' | LC_ALL=C sort)
```

**Observed (22 basenames only-in-historical):**

```
display-overview.mjs
environment.mjs
launch-verb.mjs
layout.mjs
mission-identity.mjs
options.mjs
pane-register.mjs
pane-run.mjs
queue.mjs
resume-verb.mjs
runner-attach.mjs
spawn-pane.mjs
status-verb.mjs
status-view.mjs
steer-peek.mjs
stop-restore.mjs
twins.mjs
verbs-core.mjs
wall-display.mjs
wall-schema.mjs
wall-verbs.mjs
wall.mjs
```

**Still live in lib (4):** `argv.mjs`, `base.mjs`, `observe.mjs`, `surface.mjs`.

## Family note — section honesty

**Note:** `corpus/knowledge/sighting-wall.md` (**edited this seat**)

### Pre-edit state

- **Topic-form only.** Headings were `## Module map`, `## Wall persistence`,
  `## Lifecycle internals`, `## The display is an evidence projection, never telemetry`,
  `## Boundary crossings (verified)`, `## Traps`.
- **Path-like member sections:** **0** (SCORECARD pre-measure: `S4` 0 in-family sections).
- Intro claimed `scripts/ufo-sighting-lib/` — 26 `.mjs` files, 10,620 lines; entry
  `scripts/ufo-sighting.mjs` (396 lines) — all stale vs HEAD `964f443e`.
- Prose cited deleted lib paths (`wall.mjs`, `spawn-pane.mjs`, `steer-peek.mjs`, …)
  as if live.

### Sections added (6)

| Heading | Own-file anchors (samples) |
|---|---|
| `## \`scripts/ufo-sighting.mjs\`` | `validateManifest` `:279`, `writeManifest` `:548`, `acquireOperationLock` `:663`, `spawnPaneForMission` `:2225`, `launchMissionLocked` `:2347`, `completeMission` `:3339`, `main` `:4399` |
| `## \`scripts/ufo-sighting\`` | `SCRIPT_SOURCE` `:10`, `NODE_COMPILE_CACHE` `:24`, `UFO_SIGHTING_ATTACH` `:26`, `--ufo-sighting-inquiry-direct` `:38`, `--ufo-sighting-native-direct` `:68`, exec entry `:95` |
| `## \`scripts/ufo-sighting-lib/base.mjs\`` | `MANIFEST_SCHEMA` `:41`, `MAX_MANIFEST_BYTES` `:49`, `LOCK_TIMEOUT_MS` `:73`, `SightingError` `:105` |
| `## \`scripts/ufo-sighting-lib/argv.mjs\`` | `optionValue` `:22`, `parseOpenCodeArgv` `:37`, `isOmpExecutable` `:135`, `preflightArgvDispatch` `:455` |
| `## \`scripts/ufo-sighting-lib/observe.mjs\`` | `observeMissionTasks` `:384`, `levelStatus` `:561`, `statusPhase` `:606` |
| `## \`scripts/ufo-sighting-lib/surface.mjs\`` | `SURFACE_KIND` `:24`, `surfaceScriptDigest` `:31`, `surfaceManifest` `:59` |

### Sections removed

**Path-form phantoms removed: 0** — none existed before the rewrite.

**Topic headings retired (replaced by member sections; not claims-gate members):**
`Module map`, `Wall persistence`, `Lifecycle internals`,
`The display is an evidence projection, never telemetry`,
`Boundary crossings (verified)`, `Traps` (boundary/traps retained as
non-member trailing sections without path tokens).

**Census removals recorded in the note (22 deleted lib basenames):** full list
in note § “Round-32 removal record” and in this report above — never re-added
as `##` member sections.

### Boundary probe (`LC_ALL=C sort` both sides)

```bash
NOTE=corpus/knowledge/sighting-wall.md
{ printf '%s\n' scripts/ufo-sighting.mjs scripts/ufo-sighting
  find /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-sighting-lib -type f -printf 'scripts/ufo-sighting-lib/%f\n'
} | LC_ALL=C sort -u > /tmp/s4-live.txt
grep -E '^## `scripts/' "$NOTE" | sed 's/^## `//;s/`.*$//' | LC_ALL=C sort > /tmp/s4-sec.txt
comm -3 /tmp/s4-live.txt /tmp/s4-sec.txt
```

**Observed:** empty (no only-live, no only-section). `comm` exit 0.

### Anchor / claims gate

```bash
node /home/vgpnk/Projects/shokunin/kumitate-shokunin/scripts/claims-check.mjs \
  --self /home/vgpnk/Projects/shokunin/kumitate-shokunin \
  --row S4 --src /home/vgpnk/Projects/ufo-fsd-alpha
```

**Observed:**

```
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 6
ROW S4   form=section   notes=1 sections=6 adv=2
CLAIMS  warn  SECTION_FILE_NOT_MEMBER  row=S4  scripts/ufo-sighting is outside S4's declared members
CLAIMS  warn  MEMBER_COUNT_SUSPECT     row=S4  declared 26, found 6 distinct sections
SUMMARY: errors=0 warnings=2
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=6 adv=0)
```

(exit 0; `adv=2` on the ROW line — two warnings.) Gate confirms ≥1 live
own-file anchor + ≥1 verbatim symbol per member section under current `--src`.

**Warning attribution (parent owns the fix via the registry cell, not the note):**

1. **`SECTION_FILE_NOT_MEMBER` on `scripts/ufo-sighting`:**
   `familyPatterns` only keeps backticked tokens with `/`, `*`, or a known
   extension (`claims-check.mjs` `familyPatterns`). Frozen cell token
   `` `ufo-sighting` `` has neither path nor extension, so the bash shim is
   invisible to `inFamily` even though it is a real S4 member. Cell should
   name `` `scripts/ufo-sighting` `` (or another path-like form).
2. **`MEMBER_COUNT_SUSPECT` declared 26 vs 6 sections:** gate still parses
   **26** from the frozen “26 files” cell prose. Parent rewrite to **6**
   clears this.

## Cross-domain findings (owner: parent / other families)

- **S-layer universe drift (round-32 Planned):** origin `S_members` live **91**
  vs frozen stanza **114**. S4 alone drops **28 → 6** (−22), matching the
  Planned note that “most of `scripts/ufo-sighting-lib/` (S4)” deleted since
  `5725fa7d3`.
- **Entry absorption:** lifecycle symbols formerly cited under deleted lib
  files (`wall.mjs`, `spawn-pane.mjs`, `steer-peek.mjs`, …) now live in
  `scripts/ufo-sighting.mjs` (4714 L). Cite-check / SKILL.md “26 files /
  10.6k lines” prose (if still present) is foreign debt — owner: doc pass /
  cite-check consumers, not this seat’s registry edit ban.
- **`corpus/README.md` coverage-map row** for `knowledge/sighting-wall.md`
  still says `(26 files)` — map honesty, parent/doc.
- **S8 `ufo-state-retention.mjs`** remains cited as a boundary crossing from
  the wall; it is **not** an S4 member (already has its own S8 section per
  README gaps text).
- No live S4 path was widened into S6/S7/S8; no foreign file section added.

## Unresolved blockers

**None that block note honesty.** Live set = 6 note sections = claims
sections **6**, errors **0**. Remaining `CLAIMS` warnings are **registry-cell
drift** the parent must clear when rewriting the S4 row (shim path-form +
declared count 6). No phantom path-section left in the note; 22 deleted lib
files recorded as census removals only.

## Summary for parent integration

| Field | Value |
|---|---|
| Family | S4 sighting wall |
| Live members | 6 paths listed above |
| Declared count row must carry | **6** |
| Sections added | **6** (first path-form member sections) |
| Path-form sections removed | **0** (none existed) |
| Topic headings retired | 6 (replaced; see above) |
| Lib census removals recorded | **22** basenames |
| Note edits by this seat | `corpus/knowledge/sighting-wall.md` rewritten to section-form |
| Registry/stanza edits by this seat | **none** (forbidden) |
| `claims-check --row S4` | `CLAIMS: MATCH … sections=6` errors=0 warnings=2 (cell drift) |
| Cell rewrite hints | count **6**; include path-like `` `scripts/ufo-sighting` ``; drop “26 files / 10620 L”; sizes 4714 / 95 / 510 / 507 / 614 / 325 |

End of advisory. Not a verdict.
