# R7MemberRecensus — runtime family R7 (local ship + fs layer)

Lane: `kumitate-shokunin` @ `175de6ba2e9e904010411b19cab27e0af9aad3d4`  
Origin: `/home/vgpnk/Projects/ufo-fsd-alpha` @ `964f443ee53df0ce06bd689af01f0dea031b01f9`  
Pin baseline for deletion set: `5725fa7d3`  
Note under probe: `corpus/knowledge/local-ship.md`  
Registry row (SCORECARD, parent-owned): `| R7 | local ship + fs layer | 5 files (\`local_ship*\`, \`bounded_fs*\`, \`fs_durability.rs\`) | yes — local-ship (r7) |`  
This report is data only. Parent owns the registry cell, the note edit, and the stanza.

## Axes named (godspeed)

- **coverage** — honest live membership vs note member-sections  
- **operability** — claims-check row form (`topic` → section-form)  
- **calibration** — declared count, patterns, and section count must agree

## Files inspected

| Path | Role |
|---|---|
| `SCORECARD.md` (registry R7 + round-32 `## Planned`) | declared cell + freeze context |
| `corpus/README.md` map row for `knowledge/local-ship.md` | primary-sources prose |
| `corpus/knowledge/local-ship.md` | R7 note (topic-form) |
| `corpus/knowledge/test-inventories.md` (`## local_ship_tests.rs`) | cross-family section (R9 note) |
| `scripts/claims-check.mjs` header + live `--row R7` | section/anchor contract |
| Origin `crates/ufo-core-runtime/src/{local_ship,bounded_fs,fs_durability}*.rs` | live members |
| Origin git `5725fa7d3..HEAD` deleted `.rs` under runtime+cli | deletion filter |

## Exact commands + observed output

### Live R7 membership (authoritative enumeration)

```text
$ ORIGIN=/home/vgpnk/Projects/ufo-fsd-alpha
$ ls -1 "$ORIGIN/crates/ufo-core-runtime/src" \
    | grep -E '^(local_ship|bounded_fs|fs_durability)' \
    | LC_ALL=C sort
bounded_fs.rs
bounded_fs_tests.rs
fs_durability.rs
local_ship.rs
local_ship_tests.rs

$ ls -1 "$ORIGIN/crates/ufo-core-runtime/src" \
    | grep -E '^(local_ship|bounded_fs|fs_durability)' \
    | wc -l
5
```

Layer context (not R7-local, for parent stanza):

```text
$ ls -1 "$ORIGIN/crates/ufo-core-runtime/src"/*.rs | wc -l
88
$ ls -1 "$ORIGIN/crates/ufo-cli/src"/*.rs | wc -l
4
# ⇒ R_members live = 92 (matches round-32 Planned measurement)
```

### Pattern expansion (SCORECARD cell backticks → live basenames)

Cell patterns: `` `local_ship*` ``, `` `bounded_fs*` ``, `` `fs_durability.rs` ``  
Expanded against `crates/ufo-core-runtime/src/*.rs` + `crates/ufo-cli/src/*.rs`:

```text
bounded_fs.rs
bounded_fs_tests.rs
fs_durability.rs
local_ship.rs
local_ship_tests.rs
```

Empty `comm -3` vs the `ls | grep` set (both sides `LC_ALL=C sort`). No CLI file matches R7 patterns.

### Deletion filter since `5725fa7d3` (R7 patterns)

```text
$ git -C "$ORIGIN" diff --diff-filter=D --name-only 5725fa7d3..HEAD \
    -- 'crates/ufo-core-runtime/src/*.rs' 'crates/ufo-cli/src/*.rs' | LC_ALL=C sort
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
```

None of the six deletions match `local_ship*` / `bounded_fs*` / `fs_durability.rs`.

```text
$ # pin vs live R7 basenames
$ pin=$(git -C "$ORIGIN" ls-tree -r --name-only 5725fa7d3 -- crates/ufo-core-runtime/src/ \
    | xargs -n1 basename | grep -E '^(local_ship|bounded_fs|fs_durability)' | LC_ALL=C sort)
$ live=$(ls -1 "$ORIGIN/crates/ufo-core-runtime/src" \
    | grep -E '^(local_ship|bounded_fs|fs_durability)' | LC_ALL=C sort)
$ comm -3 <(echo "$pin") <(echo "$live")
# (empty)
```

**Deleted files since `5725fa7d3` are NOT members — and R7 lost none.**

### Line counts (live HEAD)

```text
  149  bounded_fs.rs
  107  bounded_fs_tests.rs
  198  fs_durability.rs
 2281  local_ship.rs
 2737  local_ship_tests.rs
```

README map still cites stale sizes (`local_ship.rs` 2489 L, `bounded_fs.rs` 155 L, `fs_durability.rs` 277 L). Parent may refresh prose; sizes are not the claims gate.

### claims-check `--row R7` (observed)

```text
$ cd /home/vgpnk/Projects/shokunin/kumitate-shokunin
$ UFO_SRC=/home/vgpnk/Projects/ufo-fsd-alpha node scripts/claims-check.mjs --row R7
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 0
ROW R7   form=topic     notes=1 sections=0 adv=1
CLAIMS  warn  ROW_NO_SECTIONS          row=R7  R7 has no member section — member completeness unchecked
SUMMARY: errors=0 warnings=1
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=0 adv=1)
```

Under non-strict mode the row is `MATCH` **while contributing 0 in-family sections** to `R_sections`. That is the honesty gap this re-census names.

### Note headings today (none are path-like member sections)

```text
## Refusal order (pinned by conformance `local-ship.json`, 39 cases)
## Verdict asymmetry — the core contract
## Apply lock — cooperative election, NOT mutual exclusion (:760-987)
## Journal recovery (`recover_apply_journal` :1167-1336)
## Verifier grammar (:2061-2291) — denylist, never inference
## External-effect target table (:2001-2059)
## `bounded_fs` (155 lines) + `fs_durability` (277 lines)   ← NOT path-like (.rs missing)
## `run_verifier` (:2455-2485)
## Bounds table
## Defects flagged this round (report-class, not owned)
```

`claims-check` only treats a `##` heading as a member section when the first backticked token is path-like (contains `/` or ends in an allowed extension including `.rs`). `` `bounded_fs` `` / bare topic titles do **not** count. No heading names a deleted basename.

### Stale own-file anchors inside the topic note (calibration debt)

Several bare `local_ship.rs:N` cites in the topic body are past EOF on live HEAD (file = 2281 L). Examples verified dead: `:2317`, `:2345`, `:2464`. Live symbols (for parent re-anchor work):

| Symbol | Live line |
|---|---|
| `claim_apply_lock` | `local_ship.rs:707` |
| `recover_apply_journal` | `local_ship.rs:1098` |
| `apply_local_ship` | `local_ship.rs:1568` |
| `refuse_shell_or_inferred_verifier` | `local_ship.rs:2018` |
| `atomic_write` | `local_ship.rs:2161` |
| `read_bounded_ident` | `bounded_fs.rs:112` |

## Exact live member list (R7)

Ordered `LC_ALL=C`:

1. `bounded_fs.rs` (149 L) — `crates/ufo-core-runtime/src/bounded_fs.rs`
2. `bounded_fs_tests.rs` (107 L, 5 `#[test]`) — `…/bounded_fs_tests.rs`
3. `fs_durability.rs` (198 L) — `…/fs_durability.rs`
4. `local_ship.rs` (2281 L) — `…/local_ship.rs`
5. `local_ship_tests.rs` (2737 L, 77 `#[test]`) — `…/local_ship_tests.rs`

**Declared count the registry row must carry: `5`**  
(patterns may stay `` `local_ship*` `` / `` `bounded_fs*` `` / `` `fs_durability.rs` ``, or be expanded to five explicit basenames; either form must resolve to this set only. Do not invent members. Do not pull CLI files in.)

## Sections added / removed (note obligations for parent)

### Sections to ADD (5) — one `## \`<member>.rs\`` per live member

None of these exist today. Each needs ≥1 **live own-file** anchor (endpoints non-blank, `1 ≤ a ≤ b ≤ linecount`) and ≥1 backticked symbol verbatim in that file. Verified live anchor candidates on HEAD `964f443e`:

| Section heading to add | Verified live anchor(s) | Verbatim symbol candidates |
|---|---|---|
| `## \`bounded_fs.rs\`` (149 L) | `bounded_fs.rs:27`, `:70`, `:112-146`, `:142` | `BoundReadError`, `open_nonblock_read`, `read_bounded_ident`, `read_bounded` |
| `## \`bounded_fs_tests.rs\`` (107 L) | `bounded_fs_tests.rs:8-15`, `:18-27`, `:77-106` | `read_bounded_accepts_exact_ceiling`, `read_bounded_ident_rejects_swapped_identity_and_accepts_match` |
| `## \`fs_durability.rs\`` (198 L) | `fs_durability.rs:14-27` needs non-blank end — use `:14`, `:30`, `:66`, `:83`, `:93-97`, `:101-107` | `fsync_dir`, `TmpGuard`, `create_0600_tmp`, `hard_link_tmp`, `now_nanos`, `now_millis` |
| `## \`local_ship.rs\`` (2281 L) | `local_ship.rs:26-28`, `:32-48`, `:51`, `:71`, `:1568` (`apply_local_ship`), `:1098`, `:2161` | `HARD_MAX_REPLACEMENT_BYTES`, `LocalShipRequest`, `LocalShipState`, `apply_local_ship`, `recover_apply_journal`, `atomic_write` |
| `## \`local_ship_tests.rs\`` (2737 L) | `local_ship_tests.rs:47-79`, `:82-111`, `:211-283` | `commits_when_real_grep_sees_candidate`, `rolls_back_when_real_grep_misses_preimage`, `refuses_path_escape_symlink_hash_and_external_effect` |

After these five land as path-like member sections with live anchors+symbols, `claims-check --row R7` should move `form=topic sections=0` → `form=section sections=5` and clear `ROW_NO_SECTIONS` (strict-clean expected if anchors hold).

### Sections to REMOVE

**None.**

- No R7 member was deleted since `5725fa7d3`.
- No note `##` heading names a phantom/deleted `.rs` basename.
- Topic headings are not gated member sections; converting the note to section-form is additive. Parent may keep topic prose under the new member sections or retire redundant topic heads — either is note craft, not a deleted-member removal.

Do **not** remove content solely because line cites drifted; re-anchor or drop dead cites when rewriting under the five member sections.

## Registry / README compare (report only — parent edits)

| Surface | Current | Required after honesty pass |
|---|---|---|
| SCORECARD R7 members cell | `5 files (\`local_ship*\`, \`bounded_fs*\`, \`fs_durability.rs\`)` | Keep **5**; set already matches live tree |
| SCORECARD R7 note claim | `yes — local-ship (r7)` | `yes` only after 5 gated member sections exist (else keep topic / accept `ROW_NO_SECTIONS` and **0** toward `R_sections`) |
| `corpus/README.md` primary sources | names `local_ship.rs`, `bounded_fs.rs`, `fs_durability.rs` (+ CLI `main.rs`); omits both `*_tests.rs`; stale L counts | Parent refresh optional; tests are full R7 members under the cell globs |
| Note member sections | **0** | **5** (list above) |

## R_sections contribution (calibration)

- Today: R7 contributes **0** in-family member sections.  
- After parent lands 5 honest sections: R7 contributes **5**.  
- Round-32 target narrative (`coverage:runtime-layer` ≥ 7 needs `R_sections` ≥ 65 of 92) is parent/stanza math; this leaf only certifies R7’s +5 opportunity and that membership is already correct at 5/5 files.

## Unresolved blockers

- **None for membership enumeration.** Live set is closed and equals the pin set for R7 globs.
- **Note rewrite is parent-owned.** This leaf did not mutate `local-ship.md` or `SCORECARD.md` (contract: write only this advisory path).
- **Topic→section conversion** must re-pin anchors; many historical line numbers in the topic body are dead against 2281-L `local_ship.rs`.

## Cross-domain findings (owner named)

| Finding | Owner |
|---|---|
| `knowledge/test-inventories.md` still carries `## \`local_ship_tests.rs\`` while SCORECARD historically flags that file as R7 (not R9); gate emits `SECTION_FILE_NOT_MEMBER` on R9 for this basename | **R9** / test-inventories maintainer — do not double-count; R7 must own the gated member section; R9 may keep inventory prose without a path-like member heading, or demote the heading |
| Same pattern historically listed for `loop_driver_tests.rs` (R2) and `distill_tests.rs` (R6) inside R9 | **R9** + **R2** / **R6** peers |
| Six runtime/CLI deletions since `5725fa7d3` are outside R7 (`admission.rs`, `native_epoch*.rs`, `native_launch_tests.rs`, `replay_falsification_probes.rs`, `rfc3339.rs`) | **R11** remainder census / CLI family owners |
| `corpus/README.md` local-ship primary-sources L counts stale vs HEAD | **Parent** README refresh (cosmetic) |
| Live `R_members=92` vs frozen stanza `98` | **Parent** stanza re-pin (Planned already states DRIFT is correct) |

## Summary for parent integration

| Field | Value |
|---|---|
| Family | R7 — local ship + fs layer |
| Live members | `bounded_fs.rs`, `bounded_fs_tests.rs`, `fs_durability.rs`, `local_ship.rs`, `local_ship_tests.rs` |
| Count row must declare | **5** |
| Deleted-since-pin members | **∅** |
| Sections added (required for section-form `yes`) | **5** (all members; none present) |
| Sections removed | **0** |
| claims-check now | `form=topic`, `sections=0`, `ROW_NO_SECTIONS` advisory, exit 0 non-strict |
| Enumeration command | `ls -1 $ORIGIN/crates/ufo-core-runtime/src \| grep -E '^(local_ship\|bounded_fs\|fs_durability)' \| LC_ALL=C sort` |

End of advisory. No verdict claimed.
