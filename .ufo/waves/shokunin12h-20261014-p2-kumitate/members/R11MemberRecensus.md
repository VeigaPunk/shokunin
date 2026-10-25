# R11MemberRecensus — runtime remainder + CLI (round 32)

Advisory only. Not a verdict. Parent owns `SCORECARD.md` row `R11`, the
`kumitate-proxy-v1` stanza, and note integration.

## Axes touched

- **coverage** — live R11 membership vs frozen 47
- **operability** — note `##` sections must name live members with own-file anchors
- **calibration** — registry declared count must equal measured remainder

## Origin pin

| fact | value |
|---|---|
| origin tree | `/home/vgpnk/Projects/ufo-fsd-alpha` |
| HEAD | `964f443ee53df0ce06bd689af01f0dea031b01f9` (`964f443ee`) |
| base pin (SCORECARD) | `5725fa7d3ebdc6fe6e9cc07ed81999f8863dca70` (`5725fa7d3`) |
| ancestry note | `5725fa7d3` is **not** an ancestor of HEAD (lives on `remotes/cursor/*` clean/selfrefine lines). Tree-to-tree `git diff` / `git diff-tree` still defines “since base”. |
| lane HEAD (read-only context) | kumitate-shokunin `175de6ba2e9e904010411b19cab27e0af9aad3d4` |

## Commands + observed output

```text
$ cd /home/vgpnk/Projects/ufo-fsd-alpha && git rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9

$ find crates/ufo-core-runtime/src -maxdepth 1 -type f -name '*.rs' | wc -l
88

$ find crates/ufo-cli/src -maxdepth 1 -type f -name '*.rs' | wc -l
4
# ⇒ R_members layer total = 88 + 4 = 92 (matches SCORECARD Planned dispatch)

$ git rev-parse --short=9 5725fa7d3ebdc6fe6e9cc07ed81999f8863dca70
5725fa7d3

$ git diff --diff-filter=D --name-only \
    5725fa7d3ebdc6fe6e9cc07ed81999f8863dca70 HEAD \
    -- crates/ufo-core-runtime/src crates/ufo-cli/src | LC_ALL=C sort
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs

$ git ls-tree -r --name-only 5725fa7d3ebdc6fe6e9cc07ed81999f8863dca70 \
    crates/ufo-core-runtime/src | grep -c '\.rs$'
93
$ git ls-tree -r --name-only HEAD crates/ufo-core-runtime/src | grep -c '\.rs$'
88
# 93 − 88 = 5 runtime deletions; plus admission.rs on CLI ⇒ 6 deleted .rs
```

### R1–R10 union (SCORECARD cells expanded against **live** tree)

Explicit basename union (51), `LC_ALL=C sort`, then:

```text
$ comm -23 <(live runtime basenames) <(R1–R10 union) | wc -l
37
$ comm -23 <(R1–R10 union) <(live runtime basenames)
# empty — every R1–R10 declared basename still exists live
```

Family expansion used (SCORECARD `##` registry cells):

| id | live match count |
|---|---|
| R1 | 8 named `native_*.rs` core |
| R2 | 12 (`loop_driver*.rs` ×10 + `state.rs` + `state_tests.rs`) |
| R3 | 5 (`execution_profile*`, `cost_ledger*`, `native_profile.rs`) |
| R4 | 6 (`lane_overlay*`, `lease*`, `live*`) |
| R5 | 4 |
| R6 | 4 (`distill*`, `l3_swarm*`) |
| R7 | 5 (`local_ship*`, `bounded_fs*`, `fs_durability.rs`) |
| R8 | 4 |
| R9 | 1 (`native_tests.rs`) |
| R10 | 2 (`gate.rs`, `gate_tests.rs`) |
| **union** | **51** |

Arithmetic: `88 − 51 = 37` runtime remainder; CLI live `4`; **R11 = 41**.

### Note vs live (`LC_ALL=C sort` both sides)

```text
$ grep -E '^## `crates/' corpus/knowledge/runtime-remainder-census.md \
    | sed -E 's/^## `([^`]+)`.*/\1/' | LC_ALL=C sort > note-sections.txt
# note_sections = 47

$ comm -13 live-r11-fullpaths note-sections   # phantoms (note only)
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs

$ comm -23 live-r11-fullpaths note-sections   # missing sections
# empty

$ comm -12 live-r11-fullpaths note-sections | wc -l   # retained
41
```

The phantom set **equals** the base→HEAD deletion set (6/6).

## Exact live R11 member list (41)

Declared count the registry row **must** carry: **41**
(= 37 runtime remainder + 4 CLI; was 47 = 42 + 5).

### Runtime remainder (37)

```
crates/ufo-core-runtime/src/axes.rs
crates/ufo-core-runtime/src/axes_tests.rs
crates/ufo-core-runtime/src/axis_checks.rs
crates/ufo-core-runtime/src/axis_checks_tests.rs
crates/ufo-core-runtime/src/bounded_fixture.rs
crates/ufo-core-runtime/src/bounded_fixture_tests.rs
crates/ufo-core-runtime/src/build_json.rs
crates/ufo-core-runtime/src/config.rs
crates/ufo-core-runtime/src/config_tests.rs
crates/ufo-core-runtime/src/fixture_spawn.rs
crates/ufo-core-runtime/src/godspeed.rs
crates/ufo-core-runtime/src/godspeed_tests.rs
crates/ufo-core-runtime/src/lanes.rs
crates/ufo-core-runtime/src/lanes_tests.rs
crates/ufo-core-runtime/src/lib.rs
crates/ufo-core-runtime/src/mutation.rs
crates/ufo-core-runtime/src/native_agents.rs
crates/ufo-core-runtime/src/native_continuity.rs
crates/ufo-core-runtime/src/native_digests.rs
crates/ufo-core-runtime/src/native_evidence.rs
crates/ufo-core-runtime/src/native_route.rs
crates/ufo-core-runtime/src/operator_guidance.rs
crates/ufo-core-runtime/src/probe.rs
crates/ufo-core-runtime/src/process_group.rs
crates/ufo-core-runtime/src/process_group_tests.rs
crates/ufo-core-runtime/src/profile_shape_refusal_tests.rs
crates/ufo-core-runtime/src/proposal.rs
crates/ufo-core-runtime/src/proposal_tests.rs
crates/ufo-core-runtime/src/provenance.rs
crates/ufo-core-runtime/src/provenance_tests.rs
crates/ufo-core-runtime/src/report.rs
crates/ufo-core-runtime/src/round.rs
crates/ufo-core-runtime/src/round_digest.rs
crates/ufo-core-runtime/src/round_digest_tests.rs
crates/ufo-core-runtime/src/rules.rs
crates/ufo-core-runtime/src/specialist.rs
crates/ufo-core-runtime/src/test_env.rs
```

### CLI (4)

```
crates/ufo-cli/src/main.rs
crates/ufo-cli/src/main_tests.rs
crates/ufo-cli/src/titanium.rs
crates/ufo-cli/src/titanium_tests.rs
```

## Registry / note comparison

| surface | frozen (row + note) | measured live | delta |
|---|---|---|---|
| R11 declared members | **47** (42 runtime + 5 CLI) | **41** (37 + 4) | −6 |
| runtime `src/*.rs` universe | 93 | 88 | −5 |
| CLI `src/*.rs` | 5 | 4 | −1 |
| R1–R10 named union | 51 | 51 (all still live) | 0 |
| note `## \`crates/...\`` sections | 47 | should be 41 | −6 phantoms |
| sections for live members | 41 present | 41 | **add 0** |

### Sections **removed** (parent must delete from `runtime-remainder-census.md`)

Recorded removals (heading line in current note):

| note line | section heading (phantom / deleted since `5725fa7d3`) |
|---|---|
| 244 | `## \`crates/ufo-core-runtime/src/native_epoch.rs\`` |
| 250 | `## \`crates/ufo-core-runtime/src/native_epoch_tests.rs\`` |
| 262 | `## \`crates/ufo-core-runtime/src/native_launch_tests.rs\`` |
| 335 | `## \`crates/ufo-core-runtime/src/replay_falsification_probes.rs\`` |
| 363 | `## \`crates/ufo-core-runtime/src/rfc3339.rs\`` |
| 455 | `## \`crates/ufo-cli/src/admission.rs\`` |

Each path is ABSENT under origin HEAD and appears in
`git diff --diff-filter=D` base→HEAD. **Not members.**

### Sections **added**

**None.** `comm -23` (live − note) was empty: every live R11 path already has a
`##` section.

## Anchor operability (retained 41)

Shape probe over retained sections vs origin file bytes (own-file
`path:line` / `path:start-end`, non-blank endpoints, in-range):

| result | count |
|---|---|
| live section, ≥1 own-file anchor OK | 28 |
| live section, anchor dead/out-of-range/blank endpoint | **13** |
| phantom sections (file gone) | 6 |

Dead-anchor members (parent re-pin when integrating — else `SECTION_DEAD_ANCHOR`
under `claims-check`):

- `axes.rs` (probe cites :611–617; file n=520)
- `axes_tests.rs` (:244–267; n=260)
- `axis_checks.rs` (blank endpoint)
- `build_json.rs` (:78–350 / :350–352; n=305)
- `config_tests.rs` (:500–709; n=503)
- `fixture_spawn.rs` (blank endpoints)
- `lanes.rs` (blank endpoint)
- `lanes_tests.rs` (out of range + blank)
- `process_group.rs` (blank endpoint)
- `profile_shape_refusal_tests.rs` (blank endpoint)
- `provenance.rs` (blank endpoint)
- `round_digest.rs` (blank endpoint)
- `crates/ufo-cli/src/main_tests.rs` (:564–601; n=422)

This is **operability residue**, not membership drift. Membership census does
not invent replacement anchors.

## What the parent must write (this leaf does not)

1. **SCORECARD row R11** members cell: **41** (37 runtime remainder + 4 CLI),
   with boundary prose `88 − 51 = 37` (not `93 − 51 = 42`) and CLI `4` (not `5`).
2. **`corpus/knowledge/runtime-remainder-census.md`**: delete the six phantom
   `##` sections above; retitle 47→41; fix size/class census totals; re-pin
   dead anchors on the 13 retained files before claiming `yes` under strict gate.
3. **README map row** for `runtime-remainder-census.md` (still says 47 of 47).
4. **Stanza** `R_members` already expected 92 at dispatch; R11’s share of
   section numerator drops by 6 when phantoms die (parent re-derives
   `R_sections` via `claims-check`, does not hand-count).

## Retired-family boundary arithmetic (for stanza log)

```
base tree runtime .rs     93
HEAD runtime .rs          88
deleted runtime .rs        5   (native_epoch, native_epoch_tests,
                                native_launch_tests, replay_falsification_probes,
                                rfc3339)
base CLI .rs               5
HEAD CLI .rs               4
deleted CLI .rs            1   (admission.rs)
R1–R10 union (live)       51
R11 runtime remainder     37 = 88 − 51
R11 CLI                    4
R11 total                 41 = 37 + 4
prior R11 claim           47 = 42 + 5
delta                     −6 = exactly the deletion set
```

## Files inspected

- `/home/vgpnk/Projects/ufo-fsd-alpha` crates trees (read-only enumeration)
- `kumitate-shokunin/SCORECARD.md` (R1–R11 rows + Planned round-32)
- `kumitate-shokunin/corpus/README.md` (R11 map row)
- `kumitate-shokunin/corpus/knowledge/runtime-remainder-census.md` (47 sections)
- `kumitate-shokunin/corpus/knowledge/executable-scorecard.md` / `layer-axes.md` (term defs)
- `kumitate-shokunin/scripts/proxy-check.mjs` (SRC candidates / layer filter — read only)

## Unresolved blockers

- None for **membership enumeration**. Live set is closed and reproducible.
- **Note cannot stay `yes` under strict claims** until parent removes 6 phantoms
  and repairs 13 dead anchors. Leaf scope = advisory report only (no corpus edit).
- Base pin `5725fa7d3` is not on HEAD’s first-parent ancestry; deletion evidence
  is tree-diff, not a single deleting commit on `main`.

## Cross-domain findings (owner)

| finding | owner |
|---|---|
| R11 cell still claims 47 / note still 47 sections after upstream 6-file delete | kumitate parent (round-32 integrate) |
| 13 retained R11 sections fail own-file anchor bounds against HEAD bytes | kumitate parent (note re-anchor); upstream churn owner is origin runtime |
| `5725fa7d3` not ancestor of origin HEAD `964f443e` (pin on cursor clean/selfrefine lines) | scorecard pin hygiene — parent; optional origin-history owner if a reachable merge-base pin is preferred |
| CLI lost `admission.rs`; any script/doc still teaching `ufo-cli` admission module path | origin + any lane citing admission.rs (native-trial / failure-telemetry residue) |
| Layer `R_members=92` confirmed; frozen stanza 98 is DRIFT for the right reason | parent stanza rewrite |

## Leaf actions taken

- Enumerated live R11 by direct origin commands (stated above).
- Diffed note sections with `LC_ALL=C sort` + `comm`.
- Recorded six section removals; zero additions.
- **Did not** edit `SCORECARD.md`, stanza, or `runtime-remainder-census.md`
  (parent-owned).
- **Did not** invent members or widen into R1–R10 files.

## Declared count (authoritative for parent row)

**`R11` must declare `41` members.**
