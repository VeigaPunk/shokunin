# R2MemberRecensus — runtime-layer family R2 (loop driver + state)

Seat: leaf recensus member (`R2MemberRecensus`). Unjudged fleet wave. **Not a verdict.**

## Axes (named)

- **coverage** — live R2 membership vs registry/note section honesty
- **operability** — section-form note the claims gate can re-derive (one `##` per member, own-file live anchor + verbatim symbol)
- **calibration** — declared count matches measured live set; no phantom/deleted members

## Scope

| Item | Value |
|---|---|
| Family | **R2** — loop driver + state |
| Origin tree | `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` (`964f443e`) |
| Lane repo | `/home/vgpnk/Projects/shokunin/kumitate-shokunin` dispatch HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4` |
| Deletion pin | `5725fa7d3` |
| Note | `corpus/knowledge/loop-driver.md` |
| Registry row | `SCORECARD.md` \| R2 \| (line 128 at read) |
| Parent owns | registry row cell + `kumitate-proxy-v1` stanza |

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | R2 registry row + round-32 `## Planned` pre-registration |
| `kumitate-shokunin/corpus/README.md` | coverage-map → `knowledge/loop-driver.md` |
| `kumitate-shokunin/corpus/knowledge/loop-driver.md` | R2 note (was topic-form; sectionized this seat) |
| `kumitate-shokunin/scripts/claims-check.mjs` | member-section / anchor / `familyPatterns` semantics (read) |
| `kumitate-shokunin/scripts/proxy-check.mjs` | frozen derivation reference (read header only) |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/loop_driver*.rs` (10) | live members |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/state.rs` | live member |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/state_tests.rs` | live member |

## Exact commands + observed output

### Origin HEAD + layer universe

```
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse --short HEAD
964f443e

$ find /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src \
       /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src \
       -name '*.rs' -type f | LC_ALL=C sort | wc -l
92
```

Layer check: **R_members live = 92** (88 runtime `src/*.rs` + 4 CLI `src/*.rs`; matches dispatch planned drift vs frozen stanza 98).

### R2 live membership (direct enumeration — stated command)

```
$ cd /home/vgpnk/Projects/ufo-fsd-alpha
$ ls -1 crates/ufo-core-runtime/src/loop_driver*.rs \
       crates/ufo-core-runtime/src/state.rs \
       crates/ufo-core-runtime/src/state_tests.rs | LC_ALL=C sort
crates/ufo-core-runtime/src/loop_driver.rs
crates/ufo-core-runtime/src/loop_driver_candidate.rs
crates/ufo-core-runtime/src/loop_driver_digest.rs
crates/ufo-core-runtime/src/loop_driver_dispatch.rs
crates/ufo-core-runtime/src/loop_driver_dry.rs
crates/ufo-core-runtime/src/loop_driver_judge.rs
crates/ufo-core-runtime/src/loop_driver_open.rs
crates/ufo-core-runtime/src/loop_driver_publish.rs
crates/ufo-core-runtime/src/loop_driver_resume.rs
crates/ufo-core-runtime/src/loop_driver_tests.rs
crates/ufo-core-runtime/src/state.rs
crates/ufo-core-runtime/src/state_tests.rs

$ ls -1 … | LC_ALL=C sort | wc -l
12
```

All twelve basenames resolve under `crates/ufo-core-runtime/src/`. **Zero** resolve under `crates/ufo-cli/src/`.

Line counts (`wc -l`, same cwd):

| Member | L |
|---|---:|
| `loop_driver.rs` | 1130 |
| `loop_driver_candidate.rs` | 174 |
| `loop_driver_digest.rs` | 181 |
| `loop_driver_dispatch.rs` | 1820 |
| `loop_driver_dry.rs` | 946 |
| `loop_driver_judge.rs` | 538 |
| `loop_driver_open.rs` | 259 |
| `loop_driver_publish.rs` | 284 |
| `loop_driver_resume.rs` | 585 |
| `loop_driver_tests.rs` | 5034 |
| `state.rs` | 380 |
| `state_tests.rs` | 132 |
| **sum** | **11463** |

### Freeze comparison since `5725fa7d3` (deleted ⇒ not members)

```
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha ls-tree -r --name-only 5725fa7d3 \
    -- crates/ufo-core-runtime/src/ \
  | grep -E 'loop_driver|state\.rs$|state_tests\.rs$' | LC_ALL=C sort > /tmp/r2f.txt
$ ls -1 crates/ufo-core-runtime/src/loop_driver*.rs \
       crates/ufo-core-runtime/src/state.rs \
       crates/ufo-core-runtime/src/state_tests.rs | LC_ALL=C sort > /tmp/r2l.txt
$ LC_ALL=C comm -3 /tmp/r2f.txt /tmp/r2l.txt
# (empty)
```

**No R2 additions or deletions** between `5725fa7d3` and HEAD `964f443e`. Family size held at 12.

Layer-wide deletions in the same range (for parent arithmetic; **not** R2 members):

```
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha diff --name-status 5725fa7d3..HEAD \
    -- crates/ufo-core-runtime/src crates/ufo-cli/src | grep '^D'
D	crates/ufo-cli/src/admission.rs
D	crates/ufo-core-runtime/src/native_epoch.rs
D	crates/ufo-core-runtime/src/native_epoch_tests.rs
D	crates/ufo-core-runtime/src/native_launch_tests.rs
D	crates/ufo-core-runtime/src/replay_falsification_probes.rs
D	crates/ufo-core-runtime/src/rfc3339.rs
```

### Registry-declared ∩ live (`LC_ALL=C` both sides)

Registry cell patterns expand to the same 12 basenames (`loop_driver*.rs` ×10 via glob + `state.rs` + `state_tests.rs`).

```
$ printf '%s\n' loop_driver.rs loop_driver_candidate.rs loop_driver_digest.rs \
    loop_driver_dispatch.rs loop_driver_dry.rs loop_driver_judge.rs \
    loop_driver_open.rs loop_driver_publish.rs loop_driver_resume.rs \
    loop_driver_tests.rs state.rs state_tests.rs | LC_ALL=C sort > /tmp/r2_dec.txt
$ ls -1 crates/ufo-core-runtime/src/loop_driver*.rs \
       crates/ufo-core-runtime/src/state.rs \
       crates/ufo-core-runtime/src/state_tests.rs \
  | xargs -n1 basename | LC_ALL=C sort > /tmp/r2_live_base.txt
$ LC_ALL=C comm -3 /tmp/r2_dec.txt /tmp/r2_live_base.txt
# (empty)
```

## Exact live member list (derived)

1. `crates/ufo-core-runtime/src/loop_driver.rs`
2. `crates/ufo-core-runtime/src/loop_driver_candidate.rs`
3. `crates/ufo-core-runtime/src/loop_driver_digest.rs`
4. `crates/ufo-core-runtime/src/loop_driver_dispatch.rs`
5. `crates/ufo-core-runtime/src/loop_driver_dry.rs`
6. `crates/ufo-core-runtime/src/loop_driver_judge.rs`
7. `crates/ufo-core-runtime/src/loop_driver_open.rs`
8. `crates/ufo-core-runtime/src/loop_driver_publish.rs`
9. `crates/ufo-core-runtime/src/loop_driver_resume.rs`
10. `crates/ufo-core-runtime/src/loop_driver_tests.rs`
11. `crates/ufo-core-runtime/src/state.rs`
12. `crates/ufo-core-runtime/src/state_tests.rs`

**Declared count the SCORECARD row must carry: 12.**

## Registry row comparison

`SCORECARD.md` R2 cell (read):

| field | value |
|---|---|
| Id | R2 |
| Family | loop driver + state |
| Members cell | `12 files (`loop_driver*.rs` ×10, `state.rs`, `state_tests.rs`)` |
| Corpus note | `yes — loop-driver` |

Match vs live set: **identical 12 basenames**. No membership drop/add on this re-census.

### Parent cell recommendation (parent-owned; this seat does not edit SCORECARD)

Prefer an explicit members spelling so `RE_MEMBERS` / `MEMBER_COUNT_DRIFT` binds tightly and the glob cannot be mis-counted:

```
12 members: `loop_driver.rs` + `loop_driver_candidate.rs` + `loop_driver_digest.rs` + `loop_driver_dispatch.rs` + `loop_driver_dry.rs` + `loop_driver_judge.rs` + `loop_driver_open.rs` + `loop_driver_publish.rs` + `loop_driver_resume.rs` + `loop_driver_tests.rs` + `state.rs` + `state_tests.rs`
```

The existing `12 files` + `loop_driver*.rs` form already expands correctly under `familyPatterns()` / `globMatch`, and `RE_FILES` only yields `MEMBER_COUNT_SUSPECT` (warn) rather than `MEMBER_COUNT_DRIFT` (error). Count stays **12** either way.

### `corpus/README.md` coverage-map cell

Row for `knowledge/loop-driver.md` lists `loop_driver*.rs`, `state.rs`, `ufo-cli/src/main.rs`. CLI `main.rs` is a **consumer**, not an R2 member (CLI remainder / R11 boundary). Parent may tidy the map cell; it does not change the SCORECARD declared count.

## Note sections (`corpus/knowledge/loop-driver.md`)

### Prior state (pre-edit)

Topic-form only — headings were non-pathish:

- `## Entry points and epoch shape`
- `## Round pipeline — …`
- `## Stop vocabulary — single-sourced`
- `## Checkpoint — LoopState …`
- `## Module table`
- `## Judgment vocabulary (fixture side)`
- `## Traps`

`claims-check` would classify the row as `ROW_NO_SECTIONS` (advisory): member completeness unchecked despite `yes — loop-driver`. Stale pins in that prose included `CHECKPOINT_PROTOCOL_VERSION` as `ufo.fsd.v4` / `:121` (live is `ufo.fsd.v3` at `loop_driver.rs:110`) and several moved line numbers (`boundary_stop` now `:561`, `run_dry_until_halt` now `:943`, etc.).

### Sections added (this seat)

Twelve member sections, one per live file (first backticked token path-like `.rs`):

| `##` heading | Primary own-file anchors (verified non-blank) | Verbatim symbols |
|---|---|---|
| `loop_driver.rs` | `:110`, `:336`, `:416`, `:561` | `LoopDriver`, `CHECKPOINT_PROTOCOL_VERSION`, `boundary_stop` |
| `loop_driver_open.rs` | `:69`, `:233`, `:253` | `validate_local_roster`, `require_writer_lease` |
| `loop_driver_resume.rs` | `:127`, `:246`, `:488`, `:528` | `persist_state`, `run_epoch_from`, `run_resumed_epoch_until_halt` |
| `loop_driver_dry.rs` | `:69`, `:79`, `:300`, `:779`, `:943` | `run_dry_iteration_vs`, `ldd_dry_round_dispatch_phase`, `run_dry_until_halt` |
| `loop_driver_dispatch.rs` | `:1375`, `:1625`, `:1793` | `dispatch_specialists`, `DomainCooldowns` |
| `loop_driver_judge.rs` | `:52`, `:415`, `:527` | `judge_wave`, `membrane_touching_accepts`, `rejection_reason_code` |
| `loop_driver_candidate.rs` | `:58`, `:145` | `bind_loop_candidate`, `honest_fixture_baseline` |
| `loop_driver_publish.rs` | `:19`, `:61`, `:87`, `:113` | `loop_state_path`, `publish_guarded`, `refuse_if_membrane_sealed` |
| `loop_driver_digest.rs` | `:44`, `:138` | `lanes_protocol_projection`, `freeze_round_digests` |
| `loop_driver_tests.rs` | `:4065`, `:4621` | `unmeasured_material_axis_blocks_admission`, `membrane_seal_kind_is_pinned` |
| `state.rs` | `:21`, `:41`, `:114`, `:226`, `:357` | `LoopOutcome`, `LoopState`, `BrakeTelemetry`, `round_stop_outcome` |
| `state_tests.rs` | `:4`, `:12`, `:62` | `sound_zero_accept_converges`, `budget_halt_is_not_saturation` |

Anchor check method: read each cited line in the origin file; confirm `1 ≤ n ≤ line_count` and line non-blank; confirm each backticked symbol is a literal substring of that file.

### Sections removed

**None naming a deleted origin file** — freeze∩live for R2 is identity (comm empty).

Prior **topic** headings (non-member) were folded into the twelve member sections + retained non-member heads:

- `## Cross-family consumers (not R2 members)` — documents `gate.rs` / `report.rs` / `round.rs` / `lease.rs` / CLI `main.rs` without claiming them as R2
- `## Traps (family-level)`
- `## Re-census record (round 32, member R2MemberRecensus)`

Those three are **not** member sections (first token not path-like) and do not inflate the distinct-member count.

### Distinct member-section count after edit

**12** — equals declared live membership.

## Unresolved blockers

**None** for R2 membership or note section honesty on the measured tree.

Parent still must:

1. Accept or adjust the SCORECARD R2 members-cell spelling (count stays 12).
2. Re-pin stanza layer terms after all family seats land (`R_members` 92, `R_sections` re-derived).
3. Run `node scripts/claims-check.mjs` / `proxy-check.mjs` (this seat did not run gates per leaf rule).

## Cross-domain findings (owner)

| Finding | Owner |
|---|---|
| Live protocol pin is `ufo.fsd.v3` at `loop_driver.rs:110` (not `v4`/:121 from older corpus prose) | kumitate note (repaired in `loop-driver.md`); any SKILL/LOG cites of v4/:121 remain parent/doc debt |
| `stop_evaluation_string` now lives in `loop_driver_dispatch.rs:1793` (not `state.rs`) | R2 note updated; native-plan-digest / other notes that still point at `state.rs` for this symbol → their family seats or parent |
| `report.rs` / `round.rs` cited historically beside the loop driver are **R11** remainder, not R2 | R11 seat / parent boundary arithmetic |
| CLI `main.rs` `self-iter` drives `run_dry_until_halt` but is not an R2 member | R11 / CLI remainder; README coverage-map tidy is parent-optional |
| Layer shrink 98→92 is **not** driven by R2 (R2 held at 12); deletions are CLI `admission.rs` + five runtime non-R2 files | parent stanza + R11/other family seats |
| R9 `test-inventories.md` still describes `loop_driver_tests.rs` (out-of-family section warn historically) — membership remains R2 | R9 seat; do not move the file out of R2 |

## Summary for parent integration

| Item | Value |
|---|---|
| Live R2 members | **12** (list above) |
| Deleted R2 since `5725fa7d3` | **0** |
| Note member sections added | **12** |
| Note member sections removed (deleted-file phantoms) | **0** |
| Declared count row must carry | **12** |
| Registry cell membership edit required? | **No** for count; optional explicit-basename rewrite |
| Note edit by this seat | **Yes** — `corpus/knowledge/loop-driver.md` topic→section form |
| SCORECARD / stanza edit by this seat | **No** (parent-owned) |

End of advisory. Not a verdict.
