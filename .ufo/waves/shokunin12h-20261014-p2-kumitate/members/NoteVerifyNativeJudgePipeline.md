# NoteVerifyNativeJudgePipeline

Advisory only. Not a verdict. Note was not edited. No section was added or removed.

## Question

Independently verify `corpus/knowledge/native-judge-pipeline.md`: for each `## ` section, confirm the named member exists in the live origin tree and that the section carries an anchor resolving in that member's own file. Report every section whose member is absent, every declared member with no section, and the honest count.

## Predicate used

Frozen `scripts/claims-check.mjs` (`RE_CHUNK_HEAD` `/^`([^`]+)`/`, `RE_EXT`, `RE_PATHISH`, `RE_BARE`, live test `1 ≤ a ≤ b ≤ split('\n').length` and both endpoints non-blank). A heading counts as a member section only when the text after `## ` starts with a path-like backtick. A section counts when that token resolves to exactly one origin file and at least one own-file anchor is live. The gate does not require the cited symbol to sit on the anchored line. This report does not tighten that predicate.

LSP: no `xd://lsp` device is mounted. Membership and line anchors were resolved by the same text walk the gate uses, plus `rg` for symbol homes. That is not a semantic definition lookup.

## Files inspected

- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/native-judge-pipeline.md` (sha256 `20ba66027fbaa79b651fb468e8421ab623fcba3d79322c86bd193765e4ed867f`, clean at lane HEAD)
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/scripts/claims-check.mjs` (anchor and chunk-head rules, lines 40-49, 99-106, 293-384)
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/SCORECARD.md` R1 cell (still `8 members:` plus the eight basenames)
- origin `crates/ufo-core-runtime/src/{native,native_header,native_schema,native_contract,native_scores,native_plan_digest,native_launch,native_telemetry}.rs`
- origin `crates/ufo-core-runtime/src/lane_overlay.rs` (cross-domain only; not an R1 member)

## HEADs

```
git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin rev-parse HEAD
f6d62728b2e41b8f6a0a8dfaa030c4eaa482e30b

git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9

git -C kumitate-shokunin status --porcelain -- corpus/knowledge/native-judge-pipeline.md
(empty; clean)

sha256sum corpus/knowledge/native-judge-pipeline.md
20ba66027fbaa79b651fb468e8421ab623fcba3d79322c86bd193765e4ed867f
```

Dispatch recorded lane `175de6ba`. The note was clean at `f6d62728` when hashed. Origin HEAD matches the planned stanza's `964f443e`.

## Derived member list

Declared by the R1 cell, and the only member-form headings in the note:

1. `native.rs` → `crates/ufo-core-runtime/src/native.rs` (unique)
2. `native_header.rs` → `crates/ufo-core-runtime/src/native_header.rs`
3. `native_schema.rs` → `crates/ufo-core-runtime/src/native_schema.rs`
4. `native_contract.rs` → `crates/ufo-core-runtime/src/native_contract.rs`
5. `native_scores.rs` → `crates/ufo-core-runtime/src/native_scores.rs`
6. `native_plan_digest.rs` → `crates/ufo-core-runtime/src/native_plan_digest.rs`
7. `native_launch.rs` → `crates/ufo-core-runtime/src/native_launch.rs`
8. `native_telemetry.rs` → `crates/ufo-core-runtime/src/native_telemetry.rs`

No other origin basename matched any of those eight. No invented member was added.

## Honest count

| check | result |
|---|---|
| member-form `## ` sections | 8 |
| section whose member is absent | none |
| section whose member is ambiguous | none |
| declared member with no section | none |
| extra member-form section | none |
| sections with ≥1 live own-file anchor | 8 |
| honest membership count | **8** |

Topic-form headings (chunk does not start with a path-like backtick; not members; not absent members): CLI intake; Handoff schema; Judgment order — `` `native.rs::judge_handoff` ``; Verdict vocabulary; Contract-hash mechanism (`` `native_contract.rs` `` is not the first token); Failure classifier; Traps; Members.

## Anchor tally (claims-check predicate)

`splitLen` is `split('\n').length` (the bound the gate uses). `wc` is newline count.

| member | heading line | heading L | wc | splitLen | anchors | live | dead |
|---|---:|---:|---:|---:|---:|---:|---:|
| `native.rs` | 186 | 767 | 685 | 686 | 11 | 4 | 7 |
| `native_header.rs` | 198 | 342 | 305 | 306 | 11 | 10 | 1 |
| `native_schema.rs` | 210 | 570 | 532 | 533 | 33 | 29 | 4 |
| `native_contract.rs` | 256 | 918 | 663 | 664 | 27 | 27 | 0 |
| `native_scores.rs` | 311 | 700 | 708 | 709 | 13 | 9 | 4 |
| `native_plan_digest.rs` | 323 | 809 | 676 | 677 | 10 | 10 | 0 |
| `native_launch.rs` | 337 | 582 | 380 | 381 | 6 | 3 | 3 |
| `native_telemetry.rs` | 349 | 1009 | 988 | 989 | 8 | 8 | 0 |

Live anchors that carry each section (any one is enough):

- `native.rs`: `:470` `:431` `:271` `:679`
- `native_header.rs`: `:243` `:29` `:45` `:55` `:86` `:284` `:129` `:198` `:175` and `crates/ufo-core-runtime/src/native_header.rs:243-282`
- `native_schema.rs`: 29, including `:531` `:455` `:23` `:251-253`
- `native_contract.rs`: 27, including `:69-135` `:164` is not in this list as a bare token; `:220` `:485` `:609` are
- `native_scores.rs`: `:21-28` `:35` `:60` `:267` `:308` `:499-533` `:535-546` `:468-497` (twice)
- `native_plan_digest.rs`: `:33` `:94` `:99-130` `:240-260` `:217-230` `:420-425` `:474-486` `:516-534` `:557-572`
- `native_launch.rs`: `:117` `:365` `native_launch.rs:365-369`
- `native_telemetry.rs`: `:286` `:277` `:47` `:217` `:320` `:400` `:853` `native_telemetry.rs:286-291`

Dead anchors (do not fail the section, because another own-file anchor is live):

- `native.rs`: `crates/ufo-core-runtime/src/native.rs:470-613` (end blank), `:626` blank, `:626-652` start blank, `:654` blank, `:740` `:751` `:761` past splitLen 686
- `native_header.rs`: `:284-342` end past splitLen 306
- `native_schema.rs`: `:89` blank, `:542` `:550` `:563-568` past splitLen 533
- `native_scores.rs`: `:130-133` start blank, `:177-203` start blank, `:395` blank, `:623` blank
- `native_launch.rs`: `:409` `:464` `:539` past splitLen 381

Symbol-at-line is not the membership predicate. Observed anyway, so a live anchor is not read as a true citation:

| cited | file:line text | declaration |
|---|---|---|
| `judge_handoff` :470 | `&deadlines,` | `native.rs:424` |
| `validate_header` :243 | plan-artifact comment | `native_header.rs:209` |
| `natb_validate_topology_bounds` :284 | `if handoff.agents.len() + dispatch_count != expected_total` | `native_header.rs:253`; range `:284-342` is dead (oob) |
| `is_proposal` :251 | `Distillation,` | `native_schema.rs:216` |
| `NativeRoundHandoff` :455 | mission_goal comment | `native_schema.rs:425` |
| `NATIVE_CONTRACT_FILES` :69 | `".omp/hooks/ufo-statusline.mjs",` | `native_contract.rs:46` as `[&str; 62]`, not 66 |
| `native_contract_hash` :164 | function head | matches |
| `clamp_honest_baseline_vector` :21 | function head | matches |
| `validate_integrated_candidate` :395 | blank (dead) | `native_scores.rs:396` |
| `validate_plan_binding` :33 | doc comment | `native_plan_digest.rs:104` |
| `validate_effective_launch` :365 | `natd_effective_launch_role_card(...)` | `native_launch.rs:342` |
| `validate_telemetry` :286 | `.by_seat` | `native_telemetry.rs:278` |
| `lane_timeout_seats` :277 | `#[allow(clippy::too_many_lines)]` | `native_telemetry.rs:269` |
| `reject_critical_lane_timeout` :853 | `return Err(invalid(format!(` | `native_telemetry.rs:831` |

Each of the eight sections still has at least one backticked symbol verbatim somewhere in its file (`symbolHit` true under the gate's "any qualifying backtick" test). That is not a claim that every backtick is present.

## Sections added / removed

None. This member did not edit the note. No member-form heading names a file absent from the live tree, so the removal rule does not fire.

## Cross-domain (owner named; not folded into the count)

- Registry owner: the R1 cell still backticked `` `native*.rs` ``. `familyPatterns` treats that as a glob. It does not add a section to this note and does not change the 8-count. It would re-admit every `native*.rs` if a later note section used one.
- Registry owner: the same cell backticked `knowledge/runtime-remainder-census.md`. Path-like. Not a heading in this note.
- Note integrator: preamble still cites `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`. That directory is absent. Live tree is `/home/vgpnk/Projects/ufo-fsd-alpha` (HEAD `964f443e`). Not a missing member.
- Note integrator, cross-check R4 / `lane_overlay.rs`: the `native_launch.rs` section cites `validate_launch_overlays` at `:539` and `read_resolvable_overlay_bytes` at `:464`. Both lines are past EOF (wc 380). Those functions are in `lane_overlay.rs:262` and `lane_overlay.rs:199`. `native_launch.rs` contains `validate_effective_launch` at `:342` only. Not a phantom R1 member.
- Note integrator: topic-section paths written `src/native_schema.rs:N` do not exact-match the origin index (`crates/ufo-core-runtime/src/native_schema.rs`). Those headings are topic-form, so they are not absent-member sections.

## Unresolved

- No semantic server. Symbol-at-line drift above is text evidence, not an LSP definition result.
- Lane HEAD moved during the wave (`175de6ba` at dispatch, `f6d62728` at hash time). The note file was clean at hash time. A later edit of the note would stale this report.
- This report does not run `claims-check` as a row verdict and does not say whether `coverage:runtime-layer` moves.
