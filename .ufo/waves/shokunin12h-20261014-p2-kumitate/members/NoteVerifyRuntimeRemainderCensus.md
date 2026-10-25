# NoteVerifyRuntimeRemainderCensus — R11 note vs live origin

Lane: kumitate-shokunin · wave shokunin12h-20261014-p2-kumitate · round 32 re-census
Seat: `NoteVerifyRuntimeRemainderCensus` (leaf, read-only) · origin HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`
Origin tree: `/home/vgpnk/Projects/ufo-fsd-alpha`
Note blob (unchanged since round-15 `db61be0`): `aee72117b1da5f83cc25cdf3af1c50319a24b8e1`
Note sha256: `38a11e86dbcc11765c8632e2a0b5580f51d95ac34c6f0919d83268c7a8525575`
Lane HEAD moved under other seats during this read (`0ecba269` → `cdeaa0a608f279c137ae9965a6ca91e09f19ab30`). `git diff 175de6ba2e9e904010411b19cab27e0af9aad3d4 -- corpus/knowledge/runtime-remainder-census.md` was empty. This report verifies that note, not a later edit.
This report is data, not a verdict. Parent owns the note, the registry cell, and the stanza.

## Axes touched

- coverage: which `## ` sections name a file that is still in the live origin tree
- operability: which of those sections carry an own-file anchor that resolves (claims-check rule: `1 ≤ a ≤ b ≤` split line count, both endpoint lines non-blank)
- calibration: do not count a phantom section, do not treat a blank endpoint as live, do not subtract R11 files via the leaked `` `native*.rs` `` backtick

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/corpus/knowledge/runtime-remainder-census.md` | note under test (594 L, 52 `## ` headings) |
| `kumitate-shokunin/SCORECARD.md` | R1 explicit 8-name list; R11 cell observed mid-wave already saying `41 members` |
| `kumitate-shokunin/scripts/claims-check.mjs` | frozen anchor rule (`RE_PATHISH`, `RE_BARE`, `RE_CHUNK_HEAD`, liveness at `:377-378`) |
| `$ORIGIN/crates/ufo-core-runtime/src/*.rs` | live runtime surface (88) |
| `$ORIGIN/crates/ufo-cli/src/*.rs` | live CLI surface (4) |

## What was counted

A heading is a **member section** when its first backticked token contains `/` or ends in a claims-check extension (the gate's `RE_CHUNK_HEAD` + `RE_EXT` rule). Five headings are not member sections:

| Line | Heading |
|---|---|
| 32 | `## Size and class census` |
| 47 | `## How each member is named (the gate's contract)` |
| 66 | `## Members` |
| 526 | `## Member-completeness probe` |
| 584 | `## Sources` |

Member sections: **47**. Total `## ` headings: **52** (`grep -c '^## '` → 52, `grep -c '^## \`' ` → 47).

**Declared live membership** is the note's own subtraction, re-measured, using the explicit R1–R10 names — not `familyPatterns()` on the current R1 cell. That cell still backticks `` `native*.rs` `` inside the round-17 historical parenthetical (`SCORECARD.md` R1 cell, observed this read). Feeding that token to `familyPatterns()` re-admits every `native*.rs` and steals five live R11 files (`native_agents.rs`, `native_continuity.rs`, `native_digests.rs`, `native_evidence.rs`, `native_route.rs`) plus files that belong to R3/R5/R8/R9. Those five are sectioned only in this note, exist, and have a live anchor. They stay in R11. The explicit R1 list is the eight names the cell declares.

**Honest section** = member section whose heading token exists as a file under the origin tree AND at least one own-file anchor is live. A section with only dead anchors is not honest. A section whose file is absent is not honest.

## Exact commands + observed output

### Pins

```
$ git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9

$ git -C /home/vgpnk/Projects/shokunin/kumitate-shokunin rev-parse HEAD:corpus/knowledge/runtime-remainder-census.md
aee72117b1da5f83cc25cdf3af1c50319a24b8e1

$ sha256sum kumitate-shokunin/corpus/knowledge/runtime-remainder-census.md
38a11e86dbcc11765c8632e2a0b5580f51d95ac34c6f0919d83268c7a8525575

$ wc -l kumitate-shokunin/corpus/knowledge/runtime-remainder-census.md
594

$ git -C kumitate-shokunin diff --stat 175de6ba2e9e904010411b19cab27e0af9aad3d4 -- corpus/knowledge/runtime-remainder-census.md
# empty
```

### Live layer surface

```
$ ls -1 $ORIGIN/crates/ufo-core-runtime/src/*.rs | wc -l
88
$ ls -1 $ORIGIN/crates/ufo-cli/src/*.rs | wc -l
4
# CLI basenames: main.rs main_tests.rs titanium.rs titanium_tests.rs
```

### Explicit R1–R10 union, then remainder (`LC_ALL=C sort` both sides)

R1 names were the eight literals, not `native*.rs`. R2–R10 globs were expanded with `ls` against the live tree (`loop_driver*.rs`, `execution_profile*`, `cost_ledger*`, `lane_overlay*`, `lease*`, `live*`, `distill*`, `l3_swarm*`, `local_ship*`, `bounded_fs*`) plus the explicit basenames in those cells.

```
$ echo "runtime $(wc -l < runtime.txt)"
runtime 88
$ echo "r1_r10 $(wc -l < r1_r10.txt)"
r1_r10 51
$ LC_ALL=C uniq -d r1_r10.txt
# empty
$ LC_ALL=C comm -23 runtime.txt r1_r10.txt | wc -l
37
$ ls -1 $ORIGIN/crates/ufo-cli/src/*.rs | wc -l
4
# r11_live = 37 runtime remainder + 4 CLI = 41
```

`88 − 51 = 37`, plus 4 CLI = **41**. The historical `93 − 51 = 42` plus 5 CLI = 47 is the round-15 tree, not this one.

### Note sections vs live R11 (`LC_ALL=C sort` both sides)

```
$ LC_ALL=C comm -3 note_sections.txt r11_live.txt
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
```

Left side only (section, no live file): those 6. Right side (live member, no section): **empty**.

### Absence is not a rename

```
$ for f in crates/ufo-core-runtime/src/native_epoch.rs \
           crates/ufo-core-runtime/src/native_epoch_tests.rs \
           crates/ufo-core-runtime/src/native_launch_tests.rs \
           crates/ufo-core-runtime/src/replay_falsification_probes.rs \
           crates/ufo-core-runtime/src/rfc3339.rs \
           crates/ufo-cli/src/admission.rs; do
    test -e "$ORIGIN/$f" && echo PRESENT $f || echo ABSENT $f
  done
ABSENT  (all six)

$ find $ORIGIN/crates \( -name native_epoch.rs -o -name native_epoch_tests.rs \
    -o -name native_launch_tests.rs -o -name replay_falsification_probes.rs \
    -o -name rfc3339.rs -o -name admission.rs \)
# empty

$ git -C $ORIGIN diff --diff-filter=D --name-only 5725fa7d3..HEAD \
    -- 'crates/ufo-core-runtime/src/*.rs' 'crates/ufo-cli/src/*.rs'
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
```

The deletion set and the phantom-section set are the same six paths. No seventh runtime/CLI `.rs` was deleted in that range.

### Anchor rule, independent of the gate, then the gate

Own parser used the same `RE_PATHISH` / `RE_BARE` / split-line liveness as `scripts/claims-check.mjs:102-103` and `:377-378`. Result: 47 member sections, 6 unresolved, 7 dead, 0 with no anchor at all, **34** with ≥1 live own-file anchor. Symbol-hit was true on every resolved section, including the 7 dead ones (some other backticked identifier still occurs; that is not the same as the probe name still existing — see below).

Cross-check:

```
$ node scripts/claims-check.mjs \
    --self /home/vgpnk/Projects/shokunin/kumitate-shokunin \
    --src /home/vgpnk/Projects/ufo-fsd-alpha \
    --row R11 --json
# exit 1
# totals: rows=1 yes=1 notes=1 sections=47 errors=14 warnings=0 adv=0
# verdict: DRIFT
```

Gate findings (14), matching the independent pass:

| Kind | Detail |
|---|---|
| `SECTION_FILE_UNRESOLVED` | `native_epoch.rs`, `native_epoch_tests.rs`, `native_launch_tests.rs`, `replay_falsification_probes.rs`, `rfc3339.rs`, `admission.rs` (6) |
| `SECTION_DEAD_ANCHOR` | `build_json.rs` `78-350,350-352`; `config_tests.rs` `500-709,709-712`; `fixture_spawn.rs` `95-141,141-145`; `lanes_tests.rs` `28-149,73-77`; `profile_shape_refusal_tests.rs` `36-45,5-27,36-45`; `round_digest.rs` `193-198`; `main_tests.rs` `564-601` (7) |
| `MEMBER_COUNT_DRIFT` | `declared 41 members, found 47 distinct sections` |

The note's own probe section (`## Member-completeness probe`, lines 531-538) still quotes `CLAIMS: MATCH (… sections=47 adv=0)`. That quote is the round-15 run, not this tree.

`wc -l` on the seven dead-anchor files (gate line count is `split('\n').length`, one higher when the file ends in a newline):

```
305 build_json.rs          # note heading says 1213 L
503 config_tests.rs        # note heading says 724 L
731 fixture_spawn.rs       # note heading says 820 L
132 lanes_tests.rs         # note heading says 202 L
333 profile_shape_refusal_tests.rs  # note heading says 608 L
384 round_digest.rs        # note heading says 609 L
422 main_tests.rs          # note heading says 685 L
```

## Sections whose member is absent (6)

Remove these headings. The file is not in the live tree under that path or any other name under `crates/`.

| Note line | Heading token | Note's claimed size |
|---|---|---|
| 244 | `crates/ufo-core-runtime/src/native_epoch.rs` | 295 L |
| 250 | `crates/ufo-core-runtime/src/native_epoch_tests.rs` | 520 L |
| 262 | `crates/ufo-core-runtime/src/native_launch_tests.rs` | 319 L |
| 335 | `crates/ufo-core-runtime/src/replay_falsification_probes.rs` | 1453 L |
| 363 | `crates/ufo-core-runtime/src/rfc3339.rs` | 194 L |
| 455 | `crates/ufo-cli/src/admission.rs` | 311 L |

No section was added by this seat.

## Declared live members with no section

**None.** `LC_ALL=C comm -3` right side was empty. All 41 live R11 members already have a `## ` heading in this note.

## Sections whose file exists but no own-file anchor resolves (7)

These are not phantoms and not missing sections. They fail the second condition. All seven have `symbolHit: true` under the gate (some backticked identifier still occurs). Two probe names the note treats as the pin do not occur anywhere under `$ORIGIN/crates`: `mirror_body_digest`, `validate_accepts_declared_ceiling_boundaries` (`rg` → no matches).

Blank-endpoint deaths were read, not inferred. A range dies if either endpoint line is blank, even when the other endpoint and the symbol are present.

| Note line | File | Why every own-file anchor is dead | Observed live cite (not applied) |
|---|---|---|---|
| 128 | `build_json.rs` | `78-350` and `350-352` end past EOF (`wc -l` 305) | `parse_json` is `build_json.rs:64-72` (line 64 `pub(crate) fn parse_json`, line 72 `}`). `mirror_body_digest` is gone. |
| 148 | `config_tests.rs` | `500-709` and `709-712` end past EOF (`wc -l` 503) | Probe name `validate_accepts_declared_ceiling_boundaries` is gone from the tree. Do not re-pin that name. |
| 158 | `fixture_spawn.rs` | `95-141` and `141-145` are in range; line 141 is blank | `LaneDispatchFailure` enum head is `fixture_spawn.rs:113-124` (line 113 `pub(super) enum LaneDispatchFailure`, line 114 `LaneTimeout`). |
| 196 | `lanes_tests.rs` | `28-149` ends past EOF (`wc -l` 132); `73-77` is in range but line 77 is blank | `73-76` is non-blank at both ends. Function head `capacity_advance_keeps_same_identity_and_separate_provider_flag` is line 45. |
| 298 | `profile_shape_refusal_tests.rs` | `:5-27` dies on blank line 27; `:36-45` dies on blank line 45. Both starts are non-blank | `5-26` and `36-44` (or `35-44`, `fn expect_refusal`) are non-blank at both ends. |
| 389 | `round_digest.rs` | `193-198` is in range; line 198 is blank | `193-197` is non-blank at both ends. Function head `proposal_digest` is line 189. |
| 484 | `main_tests.rs` | `564-601` ends past EOF (`wc -l` 422) | `sigint_handler_sets_interrupt_flag` is `main_tests.rs:8-11`. |

## Honest count

| Quantity | N | Rule |
|---|---:|---|
| `## ` headings in the note | 52 | `grep -c '^## '` |
| member sections (path token) | 47 | gate heading rule |
| sections whose member is absent | 6 | `test -e` fail + `comm -3` left |
| live R11 members with no section | 0 | `comm -3` right empty |
| live R11 members | 41 | 37 runtime remainder + 4 CLI |
| member sections with a resolving own-file anchor | **34** | 47 − 6 absent − 7 dead |
| member sections that exist but fail the anchor test | 7 | table above |

**Honest count = 34.** That is the number of `## ` member sections that both name a file in the live origin tree and carry an anchor resolving in that file.

34 is not the count the row should declare. The row's live membership is **41**. All 41 have a section. 7 of those sections do not yet have a live anchor, so a `yes` claim over 41 is not honest until those seven anchors are repaired (or the sections are dropped, which would then make seven declared members lack a section). Dropping the six phantom sections moves the note from 47 sections to 41 and clears the phantom half of `MEMBER_COUNT_DRIFT`; it does not by itself make the seven dead anchors live.

`inFamily` on the gate's R11 row is the cell glob `crates/ufo-core-runtime/src/*.rs` plus `crates/ufo-cli/src/*.rs`, which matches every runtime and CLI `.rs`, not the remainder. The six unresolved sections are stored with `file: null` and no `inFamily`. The seven dead-anchor sections are `inFamily: true`. A numerator that sums `inFamily === true` therefore still counts those seven. Repairing them changes claims-check errors, not that numerator, unless the parent also drops them.

Spot-check that "live" means ≥1 anchor, not every cite: `axes.rs` is `wc -l` 520. Note cites `axes.rs:94-214` (both endpoints non-blank: line 94 is a comment, line 214 is `pub against_side: Option<SubjectiveArgumentSide>,`) and `axes.rs:611-617` (past EOF). Gate reports `anchors: 2, live: true`. The section is in the 34. Secondary cites inside otherwise-honest sections were not re-walked.

## Derived member list (live R11, 41)

Runtime remainder (37), explicit R1–R10 subtracted:

`axes.rs`, `axes_tests.rs`, `axis_checks.rs`, `axis_checks_tests.rs`, `bounded_fixture.rs`, `bounded_fixture_tests.rs`, `build_json.rs`, `config.rs`, `config_tests.rs`, `fixture_spawn.rs`, `godspeed.rs`, `godspeed_tests.rs`, `lanes.rs`, `lanes_tests.rs`, `lib.rs`, `mutation.rs`, `native_agents.rs`, `native_continuity.rs`, `native_digests.rs`, `native_evidence.rs`, `native_route.rs`, `operator_guidance.rs`, `probe.rs`, `process_group.rs`, `process_group_tests.rs`, `profile_shape_refusal_tests.rs`, `proposal.rs`, `proposal_tests.rs`, `provenance.rs`, `provenance_tests.rs`, `report.rs`, `round.rs`, `round_digest.rs`, `round_digest_tests.rs`, `rules.rs`, `specialist.rs`, `test_env.rs`

CLI (4): `main.rs`, `main_tests.rs`, `titanium.rs`, `titanium_tests.rs`

Anchor-honest subset (34) = that list minus `build_json.rs`, `config_tests.rs`, `fixture_spawn.rs`, `lanes_tests.rs`, `profile_shape_refusal_tests.rs`, `round_digest.rs`, `main_tests.rs`.

## Sections added / removed

| Action | Section | Reason |
|---|---|---|
| none added | — | leaf seat; no live member lacks a section |
| none removed | — | read-only; the six phantom headings are named above for the parent to remove |

## Unresolved blockers

None for the verification itself. The note on disk is the round-15 blob; the live tree has moved under it.

What this seat did not do: edit the note, edit the registry cell, re-pin the stanza, or claim a score.

## Cross-domain findings (owner named)

1. **Parent / note integrate.** Remove the six phantom sections and record the removal. Re-anchor the seven dead sections before the row claims `yes` over 41. Two probe names are gone (`mirror_body_digest`, `validate_accepts_declared_ceiling_boundaries`) — do not re-pin them. Four of the seven die only because an endpoint line is blank (`fixture_spawn.rs:141`, `lanes_tests.rs:77`, `profile_shape_refusal_tests.rs:27` and `:45`, `round_digest.rs:198`); tightening the range by that blank line makes the existing cite live.
2. **Parent / SCORECARD R11 cell.** Observed this read already saying `41 members (round-32 measurement)` while the same cell still carries `93 − 51 = 42` and `47 of 47` / round-15 `CLAIMS: MATCH`. The 41 matches this seat's explicit subtraction. The 47 and the MATCH quote do not. Gate on the current cell: `MEMBER_COUNT_DRIFT` declared 41, found 47.
3. **R1 cell owner.** `` `native*.rs` `` is still backticked in the R1 historical parenthetical. `familyPatterns()` will re-admit every `native*.rs`. Round-17 prose says those backticks were removed; the explanation put them back. Do not use that glob to shrink R11. The five `native_{agents,continuity,digests,evidence,route}.rs` files are R11 on the explicit list, sectioned only here, and anchor-live.
4. **Stanza / executed-prose owner.** `SCORECARD.md` `## Round 32 — executed` (read this wave) says `SECTION_FILE_UNRESOLVED` R11 ×7 and `SECTION_DEAD_ANCHOR` R11 ×4. A fresh `--row R11` against this note is unresolved ×6 and dead-anchor ×7, plus `MEMBER_COUNT_DRIFT`. Do not integrate from the ×7/×4 sentence.
5. **StanzaDerivation.** R11 cannot supply new `R_sections` by sectionizing a missing member: there is no missing member. The six phantoms are not `inFamily` (file unresolved). The seven dead sections already count as `inFamily`. Honesty work here clears claims errors; it does not raise the runtime numerator.

## Summary for parent integrate

```
R11_note = corpus/knowledge/runtime-remainder-census.md
R11_note_blob = aee72117b1da5f83cc25cdf3af1c50319a24b8e1
R11_origin = 964f443ee53df0ce06bd689af01f0dea031b01f9
R11_headings = 52
R11_member_sections = 47
R11_sections_member_absent = 6
R11_live_members = 41
R11_live_members_without_section = 0
R11_sections_anchor_dead = 7
R11_honest_sections = 34
R11_claims_row = DRIFT sections=47 errors=14 (unresolved 6, dead-anchor 7, MEMBER_COUNT_DRIFT 41≠47)
R11_sections_added = 0
R11_sections_removed = 0
```
