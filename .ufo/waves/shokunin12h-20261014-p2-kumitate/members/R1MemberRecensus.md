# R1MemberRecensus — runtime-layer family R1 (judge pipeline)

Seat: leaf recensus member. Unjudged fleet wave. Not a verdict.

## Scope

- Family: **R1** judge pipeline
- Origin tree: `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443e`
- Lane repo (read-only for registry/note): `/home/vgpnk/Projects/shokunin/kumitate-shokunin` HEAD `175de6b`
- Note: `corpus/knowledge/native-judge-pipeline.md`
- Registry row: `SCORECARD.md` line 127
- Parent owns the registry row, note edits, and stanza.

## Enumeration command (stated) + observed output

```bash
ORIGIN=/home/vgpnk/Projects/ufo-fsd-alpha
for f in native.rs native_header.rs native_schema.rs native_contract.rs \
         native_scores.rs native_plan_digest.rs native_launch.rs native_telemetry.rs; do
  p="crates/ufo-core-runtime/src/$f"
  test -f "$ORIGIN/$p" && echo "$p"
done | LC_ALL=C sort
```

Observed output (8 lines):

```
crates/ufo-core-runtime/src/native.rs
crates/ufo-core-runtime/src/native_contract.rs
crates/ufo-core-runtime/src/native_header.rs
crates/ufo-core-runtime/src/native_launch.rs
crates/ufo-core-runtime/src/native_plan_digest.rs
crates/ufo-core-runtime/src/native_schema.rs
crates/ufo-core-runtime/src/native_scores.rs
crates/ufo-core-runtime/src/native_telemetry.rs
```

Count: `… | wc -l` → **8**.

None of the eight paths exist under `crates/ufo-cli/src/` (all live under `ufo-core-runtime`).

### Deletion probe since `5725fa7d3`

```bash
git -C /home/vgpnk/Projects/ufo-fsd-alpha log --diff-filter=D --name-only --pretty=format: \
  5725fa7d3..HEAD -- \
  crates/ufo-core-runtime/src/native.rs \
  crates/ufo-core-runtime/src/native_header.rs \
  crates/ufo-core-runtime/src/native_schema.rs \
  crates/ufo-core-runtime/src/native_contract.rs \
  crates/ufo-core-runtime/src/native_scores.rs \
  crates/ufo-core-runtime/src/native_plan_digest.rs \
  crates/ufo-core-runtime/src/native_launch.rs \
  crates/ufo-core-runtime/src/native_telemetry.rs \
  | LC_ALL=C sort -u | sed '/^$/d'
```

Observed: **empty** (no R1-set member deleted since `5725fa7d3`).

### Boundary `comm -3` (both sides `LC_ALL=C sort`)

Registry basenames (SCORECARD R1 cell) vs live basenames:

```
comm -3 <(reg sorted) <(live sorted)  → empty, exit 0
```

No only-in-registry phantom; no only-in-live surprise inside the declared eight.

## Exact live member list (derived)

Ordered as the SCORECARD cell names them (registry order), all present:

1. `crates/ufo-core-runtime/src/native.rs` (685 L)
2. `crates/ufo-core-runtime/src/native_header.rs` (305 L)
3. `crates/ufo-core-runtime/src/native_schema.rs` (532 L)
4. `crates/ufo-core-runtime/src/native_contract.rs` (663 L)
5. `crates/ufo-core-runtime/src/native_scores.rs` (708 L)
6. `crates/ufo-core-runtime/src/native_plan_digest.rs` (676 L)
7. `crates/ufo-core-runtime/src/native_launch.rs` (380 L)
8. `crates/ufo-core-runtime/src/native_telemetry.rs` (988 L)

**Declared count the row must carry: 8.**

## Registry row comparison

`SCORECARD.md:127`:

| field | value |
|---|---|
| Id | R1 |
| Family | judge pipeline |
| Members cell | **8 members:** `` `native.rs` `` + `` `native_header.rs` `` + `` `native_schema.rs` `` + `` `native_contract.rs` `` + `` `native_scores.rs` `` + `` `native_plan_digest.rs` `` + `` `native_launch.rs` `` + `` `native_telemetry.rs` `` (+ historical prose; no backticked `native*.rs` glob) |
| Corpus note | yes — native-judge-pipeline |

Match vs live set: **identical 8 basenames**. No membership cell edit required for R1 on this re-census.

Coverage-map third cell in `corpus/README.md:28` also lists `gate.rs` and `ufo-cli/src/main.rs` beside the eight. Those are **not** R1 members (gate → R10; CLI main is supporting context). Parent may tidy the coverage-map cell; it does not change the SCORECARD R1 declared count.

## Note sections (`corpus/knowledge/native-judge-pipeline.md`)

Member sections present (one `## \`<member>.rs\`` each), registry order:

| heading line | section | status |
|---:|---|---|
| 186 | `## \`native.rs\`` | keep — file live |
| 198 | `## \`native_header.rs\`` | keep — file live |
| 210 | `## \`native_schema.rs\`` | keep — file live |
| 256 | `## \`native_contract.rs\`` | keep — file live |
| 311 | `## \`native_scores.rs\`` | keep — file live |
| 323 | `## \`native_plan_digest.rs\`` | keep — file live |
| 337 | `## \`native_launch.rs\`` | keep — file live |
| 349 | `## \`native_telemetry.rs\`` | keep — file live |

### Sections added

**None.** All eight declared members already have a member section.

### Sections removed

**None.** No deleted-file phantoms in the member-section set (deletion probe empty; `comm -3` empty).

### Anchor / symbol resolution (measured)

Gate rule: own-file pathish or bare `:N` anchors with non-blank lines in range + ≥1 backticked symbol verbatim in the file.

```bash
node scripts/claims-check.mjs --row R1 --src /home/vgpnk/Projects/ufo-fsd-alpha
```

Observed:

```
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 8
ROW R1   form=section   notes=1 sections=8 adv=0
SUMMARY: errors=0 warnings=0
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=8 adv=0)
```

So for claims-gate purposes every section has a resolving own-file anchor and a verbatim symbol hit.

### Calibration debt (not membership; parent may refresh)

Probe line numbers and parenthetical line counts in the note are **stale relative to HEAD `964f443e`**, but still inside file length (so not `SECTION_DEAD_ANCHOR`):

| member | note L claim | live `wc -l` | probe symbol | note line | live def line |
|---|---:|---:|---|---:|---:|
| native.rs | 767 | 685 | `judge_handoff` | 470 | **424** |
| native_header.rs | 342 | 305 | `validate_header` | 243 | **209** |
| native_schema.rs | 570 | 532 | `is_proposal` | 251 | **216** |
| native_contract.rs | 918 | 663 | `NATIVE_CONTRACT_FILES` | 69 | **46** (len now **62**, not 66) |
| native_scores.rs | 700 | 708 | `integrated_seat_admission_reason` | 468 | **474** |
| native_plan_digest.rs | 809 | 676 | `native_stop_evaluation` | 516 | **470** |
| native_launch.rs | 582 | 380 | `validate_effective_launch` | 365 | **342** |
| native_telemetry.rs | 1009 | 988 | `validate_telemetry` | 286 | **278** |

Membership census does **not** require removing or adding sections for this; refresh is optional parent calibration work so prose line cites match the tree the gate already accepts.

## Files inspected

- `skill://godspeed`
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/SCORECARD.md` (R1 row + round-32 Planned)
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/README.md` (coverage map row for native-judge-pipeline)
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/native-judge-pipeline.md` (full member sections)
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/scripts/claims-check.mjs` (anchor/symbol rules)
- Origin: all eight `crates/ufo-core-runtime/src/native{,_header,_schema,_contract,_scores,_plan_digest,_launch,_telemetry}.rs`

## Unresolved blockers

**None** for R1 membership honesty: live set = declared set = 8; note has 8/8 member sections; `claims-check --row R1` → MATCH adv=0; no deletions since `5725fa7d3` in the R1 set.

## Cross-domain findings (owner: parent / other families)

1. **Parent / note hygiene:** stale probe lines and `(N L)` headings in `native-judge-pipeline.md` (table above). Does not flip R1 membership or the claims gate today.
2. **Parent / coverage map:** `corpus/README.md` knowledge row for this note still trails `gate.rs` and `ufo-cli/src/main.rs` after the eight R1 basenames — those belong to R10 / CLI context, not the R1 declared count.
3. **Layer arithmetic (parent stanza):** this seat only certifies R1 = **8** live members with **8** sections. `R_members` 92 and `R_sections` ≥ 65 targets are whole-layer; other R* seats + parent integration own the roll-up.
4. **No ownership conflict** with R10 (`gate.rs`) or CLI seats: R1 does not claim them.

## Summary for parent integration

| item | value |
|---|---|
| Live R1 members | 8 (list above) |
| Declared count row must carry | **8** |
| Sections added | **0** |
| Sections removed | **0** |
| SCORECARD R1 cell change | **none required** (already matches live) |
| Note member-section change | **none required** for membership |
| `claims-check --row R1` | `CLAIMS: MATCH … sections=8 adv=0` |
| Deleted since `5725fa7d3` in R1 set | **none** |

End of advisory. Not a verdict.
