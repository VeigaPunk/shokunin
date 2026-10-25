# S3MemberRecensus — script-layer family S3 (swarm path)

Advisory only. Not a verdict. Parent owns registry row / stanza integration.

## Scope

- Lane: `kumitate-shokunin` @ `175de6ba2e9e904010411b19cab27e0af9aad3d4`
- Origin (READ-ONLY): `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` (`964f443e`)
- Family: **S3** swarm path
- Notes cited by registry cell: `dispatch-shapes` · `swarm-wave-lifecycle`
  → `corpus/knowledge/dispatch-shapes.md`, `corpus/knowledge/swarm-wave-lifecycle.md`

## Files inspected

| Path | Role |
|---|---|
| `SCORECARD.md:121` | registry row S3 (read-only; not edited) |
| `corpus/README.md` | coverage-map cites for swarm notes |
| `corpus/knowledge/swarm-wave-lifecycle.md` | **edited** — sectionized |
| `corpus/knowledge/dispatch-shapes.md` | read; left topic-form (no member `##`) |
| `corpus/knowledge/remaining-scripts-census.md` | confirmed test companions are S8 |
| `corpus/knowledge/ops-watchers.md` / `gate-verdict.md` | section-form pattern reference |
| `scripts/claims-check.mjs` | gate probe (familyPatterns / section arms) |
| origin `scripts/ufo-swarm-wave.mjs` | live member (1907 L) |
| origin `scripts/ufo-swarm-collect.mjs` | live member (842 L) |

## Exact commands + observed output

### Live membership enumeration

```
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs \
        /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-collect.mjs \
  | sed 's|.*/scripts/|scripts/|' | LC_ALL=C sort
scripts/ufo-swarm-collect.mjs
scripts/ufo-swarm-wave.mjs

$ wc -l /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs \
        /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-collect.mjs
 1907 /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs
  842 /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-collect.mjs
 2749 total
```

### Boundary probe (`comm -3`, both sides `LC_ALL=C sort`)

Declared set = the two paths named by the registry cell (basename tokens
`ufo-swarm-wave.mjs` + `ufo-swarm-collect.mjs` under `scripts/`).

```
$ printf '%s\n' scripts/ufo-swarm-collect.mjs scripts/ufo-swarm-wave.mjs | LC_ALL=C sort > /tmp/s3-decl.txt
$ ls -1 …/ufo-swarm-collect.mjs …/ufo-swarm-wave.mjs | sed 's|.*/|scripts/|' | LC_ALL=C sort > /tmp/s3-live.txt
$ LC_ALL=C comm -3 /tmp/s3-decl.txt /tmp/s3-live.txt
# (empty)
$ wc -l < /tmp/s3-live.txt
2
```

### Sibling swarm files (NOT S3)

```
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm*.mjs | LC_ALL=C sort
…/scripts/ufo-swarm-collect.mjs
…/scripts/ufo-swarm-collect.test.mjs
…/scripts/ufo-swarm-wave.mjs
…/scripts/ufo-swarm-wave.test.mjs
```

The two `*.test.mjs` files are owned by **S8** (`remaining-scripts-census.md`
already carries `## scripts/ufo-swarm-wave.test.mjs` and
`## scripts/ufo-swarm-collect.test.mjs`). S3 was not widened.

### Claims gate (post-edit)

```
$ node scripts/claims-check.mjs --src /home/vgpnk/Projects/ufo-fsd-alpha --row S3
ROWS: 1  YES: 1  NOTES: 2  SECTIONS: 2
ROW S3   form=section   notes=2 sections=2 adv=0
SUMMARY: errors=0 warnings=0
CLAIMS: MATCH (rows=1 yes=1 notes=2 sections=2 adv=0)
```

Pre-edit baseline (same command): `form=topic sections=0 adv=1` with
`ROW_NO_SECTIONS`.

## Derived member list

Exact live S3 membership (ordered):

1. `scripts/ufo-swarm-collect.mjs` (842 L)
2. `scripts/ufo-swarm-wave.mjs` (1907 L)

**Declared count the registry row must carry: `2`.**

Registry cell still prints historical sizes `(2711 L)` / `(988 L)`; live
sizes are **1907** / **842**. Parent owns the cell text update — this member
did not edit `SCORECARD.md`.

## Registry row vs note vs tree

| Source | Claim |
|---|---|
| `SCORECARD.md` S3 members cell | `ufo-swarm-wave.mjs` + `ufo-swarm-collect.mjs` (2) |
| `SCORECARD.md` S3 notes cell | `yes — dispatch-shapes · swarm-wave-lifecycle` |
| Live origin tree | both files present; `comm -3` empty |
| Pre-round notes | both topic-form; **0** member `##` sections |
| Post-round `swarm-wave-lifecycle.md` | **2** member `##` sections, anchors+symbols live |
| `dispatch-shapes.md` | left topic-form on purpose (no double-count) |

## Sections added / removed

### Added (in `corpus/knowledge/swarm-wave-lifecycle.md`)

| Heading | Own-file anchors (sample) | Verbatim symbols (sample) |
|---|---|---|
| `## scripts/ufo-swarm-wave.mjs` | `:3`, `:143`, `:258`, `:768`, `:1307`, `:1464`, `:1801` | `planSwarmWave`, `SWARM_ROLES`, `planToDispatchPayload`, `persistWaveRegistry`, `MIN_HOIST_SAVINGS` |
| `## scripts/ufo-swarm-collect.mjs` | `:3`, `:54`, `:93`, `:111`, `:567`, `:582`, `:659` | `collectEntries`, `STATUS_OUTCOME`, `FAILURE_CLASS_REASON`, `SwarmCollectError`, `RESULTS_SCHEMA` |

### Removed

**None.** Pre-round note had zero path-like `##` member headings, so there
was no phantom section naming a deleted file to strip.

### Topic-prose corrections recorded inside the note (not section removals)

| Stale topic claim | Live observation |
|---|---|
| Wave CLI verb `settle` mints `ufo-swarm-results-v1` | `main` admits only `plan` / `run` / `record` (`ufo-swarm-wave.mjs:1801`–`:1807`); settlement is operator-supplied results input to collect |
| Collector refusal `stale_dispatch_pair` | no such token in live collect; join uses `unmapped_member` / `unexpected_member` / identity conflicts in `collectEntries` |

## Files changed (this seat)

1. `kumitate-shokunin/corpus/knowledge/swarm-wave-lifecycle.md` — sectionized S3 (2/2)
2. `.ufo/waves/shokunin12h-20261014-p2-kumitate/members/S3MemberRecensus.md` — this report

Not changed (parent-owned): `SCORECARD.md` registry row, frozen stanza,
`corpus/README.md`, `dispatch-shapes.md`.

## Behavior for parent integration

- S3 contributes **+2** in-family member sections toward `S_sections` (was 0
  topic-form; now 2 section-form).
- Row declared member count stays **2** (no membership drift vs frozen family
  definition; only line-count pins drifted).
- After parent re-pins cell sizes optionally: claims already
  `MATCH … sections=2 adv=0` for `--row S3`.

## Unresolved blockers

None for S3 membership honesty.

## Cross-domain findings (owner)

| Finding | Owner |
|---|---|
| Registry cell still cites sizes 2711/988 vs live 1907/842 | parent (SCORECARD S3 members cell) |
| Topic claim of `settle` / `stale_dispatch_pair` was stale before this round | recorded in note; origin scripts unchanged (read-only) |
| `ufo-swarm-*.test.mjs` remain S8 | S8 recensus / remaining-scripts-census (already sectioned) |
| Sister note `dispatch-shapes.md` still topic-form and also names native-trial / sighting entry points | leave as comparative C2 note; do not sectionize under S3 (would `SECTION_FILE_NOT_MEMBER` or double-count) |

## Calibration notes

- Axes for this seat: coverage (member sections gated), operability (claims
  gate green on the row), calibration (declared count = live count = 2;
  no invented members; tests not absorbed).
- Occurrence discipline: member sections live in **one** of the two cited
  notes only, so proxy `S_sections` occurrence count and claims distinct
  count stay aligned at +2 for this family.
