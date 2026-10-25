# R5MemberRecensus — advisory (unjudged fleet wave)

**Seat:** `R5MemberRecensus` (leaf). Not a judge verdict. No registry row, stanza, commit, push, or note rewrite by this seat. Parent owns `SCORECARD.md` R5 cell + `kumitate-proxy-v1` terms and note integration.
**Lane:** `/home/vgpnk/Projects/shokunin/kumitate-shokunin` HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4`
**Origin:** `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` (`964f443e`)
**Family:** R5 — seats & admission
**Note:** `corpus/knowledge/native-admission-detail.md`
**Measured:** 2026-10-14

**Axes (named, not scored here):** coverage (member sections vs live members), operability (enumeration + claims gate exit), calibration (declared count equals live set; no phantom members).

---

## Exact live membership (R5)

**Enumeration command** (stated; both sides of any `comm` use `LC_ALL=C sort`):

```bash
cd /home/vgpnk/Projects/ufo-fsd-alpha
ls -1 crates/ufo-core-runtime/src/native_seats.rs \
      crates/ufo-core-runtime/src/native_admission_text.rs \
      crates/ufo-core-runtime/src/native_admission_rules.rs \
      crates/ufo-core-runtime/src/native_text.rs \
  | LC_ALL=C sort
```

**Observed output (exact member list, N=4):**

```
crates/ufo-core-runtime/src/native_admission_rules.rs
crates/ufo-core-runtime/src/native_admission_text.rs
crates/ufo-core-runtime/src/native_seats.rs
crates/ufo-core-runtime/src/native_text.rs
```

**Basenames (authoritative R5 set):**

1. `native_admission_rules.rs`
2. `native_admission_text.rs`
3. `native_seats.rs`
4. `native_text.rs`

**Line counts (`wc -l` at origin HEAD `964f443e`):**

| Member | Live `wc -l` | sha256 (file) |
|---|---:|---|
| `native_seats.rs` | 229 | `c6d0b3e6b03f01478500a52eb74e3648e60f1d610fbd21890c09f900de9a2333` |
| `native_admission_text.rs` | 330 | `6bf0e0c8b6a3da3f554a8854b95328d86dd91fac28d233754e862d86601b464d` |
| `native_admission_rules.rs` | 243 | `27d71f38c8c5c575767ed10aba8e416c5a430d13c18682d089c8cd740758cb2a` |
| `native_text.rs` | 184 | `94f603d68db2b0131d19894c17b54f296b83a9187d3f3a25d80d24990b41c9a9` |
| **sum** | **986** | |

**Declared count the R5 registry row must carry:** **4**  
(set identity unchanged vs frozen cell; no members added or deleted; do not invent; do not widen to `native_seat_coverage.rs` — that basename is **R8**.)

**CLI surface:** R5 has **zero** members under `crates/ufo-cli/src` (family is the four runtime basenames only).

**Layer context (re-measured):**

```bash
ls crates/ufo-core-runtime/src/*.rs | wc -l   # → 88
ls crates/ufo-cli/src/*.rs | wc -l            # → 4
# R_members = 92
```

---

## Deletion probe since `5725fa7d3`

```bash
git -C /home/vgpnk/Projects/ufo-fsd-alpha diff --diff-filter=D --name-only 5725fa7d3 HEAD -- \
  crates/ufo-core-runtime/src/native_seats.rs \
  crates/ufo-core-runtime/src/native_admission_text.rs \
  crates/ufo-core-runtime/src/native_admission_rules.rs \
  crates/ufo-core-runtime/src/native_text.rs
```

**Observed:** empty (0 paths). All four R5 members exist at `5725fa7d3` and still exist at `964f443e`.

**Runtime+CLI deletions since `5725fa7d3` (not R5 — cross-family inventory only):**

```
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
```

None match the R5 four. **No R5 section removals for deleted files.** Deleted files are NOT members of R5 and must not be sectionized into this note.

---

## Registry row vs note vs live

| Source | Claim | Observed |
|---|---|---|
| `SCORECARD.md` R5 cell | `4 files (\`native_seats.rs\`, \`native_admission_text.rs\`, \`native_admission_rules.rs\`, \`native_text.rs\`)`; `yes` — native-admission-detail | Live match = **4**; cell basename set still correct |
| `corpus/README.md` map row for `knowledge/native-admission-detail.md` | Primary sources list the same four basenames | Aligns with live set |
| Note `##` headings | topic-form only: `Attributions`, `Rules worth carrying`, `⚠ Cross-domain drift` | **0** path-like member sections (`## \`…\.rs\``) |
| Historical SCORECARD in-family sum | `R5` **0** sections (topic-form) | Matches note; under-covers live 4 for the honesty term |

**Section membership `comm -3` (note pathish `## \`…\`` headings vs live basenames):**

```bash
comm -3 \
  <(printf '%s\n' native_seats.rs native_admission_text.rs \
      native_admission_rules.rs native_text.rs | LC_ALL=C sort) \
  <(rg -o '^## `([^`]+)`' -r '$1' corpus/knowledge/native-admission-detail.md \
      | sed 's|.*/||' | LC_ALL=C sort)
```

**Observed (tab-prefixed = live-only / note-missing):**

```
native_admission_rules.rs
native_admission_text.rs
native_seats.rs
native_text.rs
```

No note-only phantoms (no section names a file absent from the origin tree).

---

## Claims gate (this seat, read-only)

```bash
cd /home/vgpnk/Projects/shokunin/kumitate-shokunin
node scripts/claims-check.mjs --row R5 --src /home/vgpnk/Projects/ufo-fsd-alpha
```

**Default (non-strict) observed:**

```
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 0
ROW R5   form=topic     notes=1 sections=0 adv=1
CLAIMS  warn  ROW_NO_SECTIONS          row=R5  R5 has no member section — member completeness unchecked
SUMMARY: errors=0 warnings=1
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=0 adv=1)
```

exit 0.

**`--strict` observed:**

```
CLAIMS: DRIFT (ROW_NO_SECTIONS row=R5 R5 has no member section — member completeness unchecked)
```

exit 1.

So R5 is **declared-4 / section-0**: non-strict MATCH with `ROW_NO_SECTIONS` advisory; strict DRIFT. Parent cannot claim honest full-member coverage (or credit 4 toward `R_sections`) until four `## \`<member>.rs\`` sections land with live own-file anchors + verbatim symbols.

---

## Sections added / removed (this seat’s measured delta for parent)

| Action | Section | Status |
|---|---|---|
| **ADD** (required for 4/4) | `## native_seats.rs` | **Absent.** Live member. Seat-key grammar + correlation digests. |
| **ADD** (required for 4/4) | `## native_admission_text.rs` | **Absent.** Live member. JS-parity coercions + sensitive-shape gate. |
| **ADD** (required for 4/4) | `## native_admission_rules.rs` | **Absent.** Live member. `validate_profile` profile admission. |
| **ADD** (required for 4/4) | `## native_text.rs` | **Absent.** Live member. `FAILURE_RULES` + `classify_failure_fields`. |
| **REMOVE** | _(none)_ | No deleted R5 files since `5725fa7d3`; no phantom pathish `##` headings. |
| **KEEP (non-member prose)** | `## Attributions` / `## Rules worth carrying` / `## ⚠ Cross-domain drift` | Topic headings (no `.rs` / no path ext) — gate ignores them as member sections. May stay as preamble or fold into member sections; not phantoms. |

**Sections added by this seat to the note:** **0** (report-only; parent integrates note edits).  
**Sections removed by this seat from the note:** **0**.  
**Sections parent must add before full R5 coverage:** **4** (all four live members).  
**Sections parent must remove:** **0**.

After parent adds the four sections with ≥1 own-file anchor + ≥1 verbatim symbol each, expected gate shape: `form=section`, `sections=4`, `ROW_NO_SECTIONS` cleared, `--strict` MATCH for `--row R5` (cell uses `4 files`, so `RE_FILES` path; prefer cell text `4 members` if parent wants the hard `MEMBER_COUNT_DRIFT` arm).

**R5 contribution to `R_sections` if completed:** **+4** in-family (was 0 in historical sum).

---

## Suggested live anchors for missing sections (data for parent; not applied)

Anchors verified against origin HEAD `964f443e` (line in range, non-empty endpoints). Prefer bare `:N` or `:N-M` in the section body so claims-check binds them to the section’s own file.

### `native_seats.rs` (229 L)

| Symbol (backtick) | Live anchor | Note |
|---|---|---|
| `singleton_key` | `:14` | |
| `seat_label` | `:25` | `{role}-{NN}` zero-padded |
| `seat_label_matches` | `:33` | byte twin of `seat_label` |
| `seat_id` | `:57` | `role:instance` unpadded |
| `parse_logical_lane_id` | `:117` | permissive parse |
| `logical_lane_id_recomputes` | `:125` | admission twin |
| `correlation_group_for` | `:217-229` | material order live: `(resolved_model, role.name(), assignment_lineage)` — note prose that claimed hash material order `(role, lineage, resolved_model)` is **stale** |

### `native_admission_text.rs` (330 L)

| Symbol (backtick) | Live anchor | Note |
|---|---|---|
| `contains_sensitive_shape` | `:49` | wider gate; superseded the old `is_format_char` story |
| `js_string_simple` | `:113` | `None` is load-bearing |
| `js_string_f64` | `:164` | |
| `clean_field_token` | `:192` | BYTE length ≤64; alnum + `_.:-` |
| `clean_field_value` | `:204` | routes through `contains_sensitive_shape` |

**Dead prose in current note:** `is_format_char` (`native_admission_text.rs:52-61`) — **symbol absent** from this file at HEAD `964f443e` (`rg` empty over runtime tree for `fn is_format_char`). Lines 52–61 are now body of `contains_sensitive_shape`. Cross-domain Cf/Mn/Zs drift section must be re-homed or withdrawn when parent sectionizes.

### `native_admission_rules.rs` (243 L)

| Symbol (backtick) | Live anchor | Note |
|---|---|---|
| `frozen_profile_field` | `:19` | typed freeze refusal |
| `validate_profile` | `:45-129` | first judge rule; still invoked from `native_header` |

### `native_text.rs` (184 L)

| Symbol (backtick) | Live anchor | Note |
|---|---|---|
| `json_lower` | `:17` | |
| `contains_status_code` | `:73` | |
| `FAILURE_RULES` | `:88` | 8-row first-match table |
| `classify_failure_fields` | `:105` | home of failure classification (not admission_text) |
| `classify_failure` | `:145` | thin wrapper |
| `is_exact_midpoint` | `:175` | |

**Dead prose in current note:** `native_text.rs:96-198` — **OUT_OF_RANGE** (file ends at 184). Replace with `:88-143` (table + `classify_failure_fields` body).

---

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | R5 registry cell; round-32 `## Planned`; layer formulas |
| `kumitate-shokunin/corpus/README.md` | map row for `native-admission-detail.md` |
| `kumitate-shokunin/corpus/knowledge/native-admission-detail.md` | R5 note (topic-form, 0 member sections) |
| `kumitate-shokunin/corpus/knowledge/executable-scorecard.md` | claims/proxy term semantics |
| `kumitate-shokunin/scripts/claims-check.mjs` | member-claims gate (`familyPatterns`, section probe) |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/native_seats.rs` | live member |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/native_admission_text.rs` | live member |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/native_admission_rules.rs` | live member |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/native_text.rs` | live member |

---

## Unresolved blockers

1. **Note under-sectioned (owner: parent / note editor).** All four live members lack `## \`…rs\`` sections → `ROW_NO_SECTIONS` / strict DRIFT. This seat did not edit the note (write-only report path).
2. **Stale internals pins inside topic prose (owner: parent).** `is_format_char` gone; `native_text.rs:96-198` dead; `correlation_group_for` material order flipped vs note. Not membership blockers; honesty debt when sectionizing.
3. **No R5 membership blocker from deletions.** Live set = 4 = declared cell basenames.

---

## Cross-domain findings (owner named; not absorbed)

| Finding | Owner |
|---|---|
| Note still attributes seat MODEL types to `native_schema.rs` | **R1** / schema family — correct attribution; do not pull `native_schema.rs` into R5 membership |
| `native_seat_coverage.rs` is seat-adjacent but registry R8 | **R8** — never widen R5 to absorb it |
| Cf/Mn/Zs producer screen (`ufo-credential-screen.mjs`) vs judge clean-field | Script-layer S8 / credential helpers + origin fix; report-class only in R5 note |
| Layer `R_members` 98→92 and six non-R5 `.rs` deletions | Parent stanza + other family seats |
| Topic-form R5 currently contributes **0** to `R_sections`; +4 available after sectionization | Parent coverage:runtime-layer integration |

---

## Summary for parent integration

| Field | Value |
|---|---|
| **Exact member list** | `native_admission_rules.rs`, `native_admission_text.rs`, `native_seats.rs`, `native_text.rs` |
| **Declared count row must carry** | **4** |
| **Sections present (pathish member)** | **0** |
| **Sections to add** | **4** (one per live member) |
| **Sections to remove** | **0** |
| **R5 contribution to `R_sections` if completed** | **4** in-family (was 0) |
| **This seat file edits** | report only — this path |
| **Registry/stanza edits** | none (forbidden) |
| **`claims-check --row R5`** | non-strict `CLAIMS: MATCH … sections=0 adv=1` (`ROW_NO_SECTIONS`); `--strict` → `CLAIMS: DRIFT` |

End of advisory. No verdict.
