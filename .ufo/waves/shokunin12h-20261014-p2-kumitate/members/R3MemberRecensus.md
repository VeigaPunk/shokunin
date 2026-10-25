# R3MemberRecensus — runtime family R3 (profile & cost)

Seat: `R3MemberRecensus` · wave `shokunin12h-20261014-p2-kumitate` · round 32 re-census  
Lane HEAD: `175de6ba2e9e` · origin HEAD: `964f443ee53d` (`/home/vgpnk/Projects/ufo-fsd-alpha`)  
Baseline pin for deletion filter: `5725fa7d3`  
This report is data for the parent integrator. Not a verdict. Registry row + stanza remain parent-owned. Note body not mutated by this seat (write path = this report only).

---

## 1. Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | registry row R3; `## Planned` round-32 pre-registration; R_sections arithmetic |
| `kumitate-shokunin/corpus/README.md` | map row for `knowledge/cost-and-profile.md` |
| `kumitate-shokunin/corpus/knowledge/cost-and-profile.md` | R3 note (current sections) |
| `kumitate-shokunin/corpus/knowledge/executable-scorecard.md` | layer-term grammar |
| `kumitate-shokunin/scripts/claims-check.mjs` | `familyPatterns` / section-form contract |
| origin `crates/ufo-core-runtime/src/{cost_ledger,cost_ledger_validation_tests,execution_profile,execution_profile_tests,native_profile}.rs` | live members + anchors |
| origin `crates/ufo-core-runtime/src/lib.rs` | `#[path]` inclusion of cost_ledger_validation_tests; `profile_shape_refusal_tests` is **not** R3 |
| origin `crates/ufo-cli/src/*.rs` | layer universe only (no R3 members) |

Lane checkout has **0** `crates/**/*.rs` (mirror-less); all membership is from the origin tree.

---

## 2. Exact commands + observed output

### 2.1 Live R3 membership (registry globs, origin tree)

Registry cell patterns: `` `execution_profile*` ``, `` `cost_ledger*` ``, `` `native_profile.rs` ``.

```sh
ORIGIN=/home/vgpnk/Projects/ufo-fsd-alpha
( ls -1 "$ORIGIN/crates/ufo-core-runtime/src/"execution_profile*.rs \
      "$ORIGIN/crates/ufo-core-runtime/src/"cost_ledger*.rs \
      "$ORIGIN/crates/ufo-core-runtime/src/native_profile.rs" 2>/dev/null ) | LC_ALL=C sort
```

**Observed:**
```
/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/cost_ledger.rs
/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/cost_ledger_validation_tests.rs
/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/execution_profile.rs
/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/execution_profile_tests.rs
/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/native_profile.rs
```

```sh
( ls -1 ...same... ) | wc -l
```
**Observed:** `5`

```sh
wc -l $ORIGIN/crates/ufo-core-runtime/src/{cost_ledger,cost_ledger_validation_tests,execution_profile,execution_profile_tests,native_profile}.rs
```
**Observed:**
```
  490 cost_ledger.rs
  306 cost_ledger_validation_tests.rs
  656 execution_profile.rs
  560 execution_profile_tests.rs
  276 native_profile.rs
 2288 total
```

### 2.2 Layer universe (context only)

```sh
ls -1 "$ORIGIN/crates/ufo-core-runtime/src/"*.rs | wc -l   # → 88
ls -1 "$ORIGIN/crates/ufo-cli/src/"*.rs | wc -l             # → 4
# R_members live = 88 + 4 = 92 (matches Planned; frozen stanza still 98)
```

### 2.3 Deletion filter since `5725fa7d3` (R3 patterns)

```sh
comm -3 \
  <(git -C "$ORIGIN" ls-tree -r --name-only 5725fa7d3 -- crates/ufo-core-runtime/src/ \
      | grep -E 'execution_profile|cost_ledger|native_profile' | LC_ALL=C sort) \
  <(git -C "$ORIGIN" ls-tree -r --name-only HEAD -- crates/ufo-core-runtime/src/ \
      | grep -E 'execution_profile|cost_ledger|native_profile' | LC_ALL=C sort)
```

**Observed:** empty (no adds, no deletes in R3 patterns).

Full runtime+CLI deletions since `5725fa7d3` (none are R3):
```
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
```

### 2.4 Non-member near-miss (do not widen R3)

```sh
ls -1 "$ORIGIN/crates/ufo-core-runtime/src/"*profile*
```
includes `profile_shape_refusal_tests.rs`. It does **not** match `execution_profile*` / `cost_ledger*` / `native_profile.rs`. It is already R11 remainder inventory (`runtime-remainder-census.md`). **Not an R3 member.**

### 2.5 Claims gate (current note, pre-integration)

```sh
node scripts/claims-check.mjs --row R3 --src /home/vgpnk/Projects/ufo-fsd-alpha
```

**Observed:**
```
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 2
ROW R3   form=section   notes=1 sections=2 adv=1
CLAIMS  warn  MEMBER_COUNT_SUSPECT     row=R3  declared 5, found 2 distinct sections
SUMMARY: errors=0 warnings=1
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=2 adv=1)
```

Exit 0 with `MEMBER_COUNT_SUSPECT`: cell claims 5, note only gates 2 member sections. That is the honesty gap this re-census names.

### 2.6 Note headings vs live members

```sh
rg -n '^## ' corpus/knowledge/cost-and-profile.md
```
**Observed:**
```
6:## `cost_ledger.rs` (737 L) — wire types + admission validator
63:## `execution_profile.rs` (689 L) — route catalog + FailureClass
100:## Traps
```

`## Traps` is topic prose (no path-like first backtick token) — not a member section; leave it.

---

## 3. Derived member list (authoritative for parent)

Exact live R3 membership, basenames, sorted `LC_ALL=C`:

1. `cost_ledger.rs` (490 L)
2. `cost_ledger_validation_tests.rs` (306 L)
3. `execution_profile.rs` (656 L)
4. `execution_profile_tests.rs` (560 L)
5. `native_profile.rs` (276 L)

**Declared count the registry row must carry: `5`.**

Cell may keep the glob shorthand  
`5 files (\`execution_profile*\`, \`cost_ledger*\`, \`native_profile.rs\`)`  
— it still expands to exactly these five under the live tree — or enumerate the five basenames explicitly (preferred after round-17 `familyPatterns` lesson: every backtick in the members cell is a pattern).

Unchanged vs `5725fa7d3`. No deleted-member section to remove.

---

## 4. Sections added / removed

### 4.1 Applied by this seat

**None.** Write path is this advisory only; parent integrates `corpus/knowledge/cost-and-profile.md`.

### 4.2 Required delta (parent must land for honest `yes`)

| Action | Section heading | Status |
|---|---|---|
| **KEEP** | `## \`cost_ledger.rs\`` | present; refresh stale size 737→**490** L and dead line cites against live file |
| **KEEP** | `## \`execution_profile.rs\`` | present; refresh stale size 689→**656** L; **`permits_advance` live at `:429`** (note still says `:448` — post-restructure shift) |
| **ADD** | `## \`cost_ledger_validation_tests.rs\`` | missing |
| **ADD** | `## \`execution_profile_tests.rs\`` | missing |
| **ADD** | `## \`native_profile.rs\`` | missing (named in prose of other sections only — does not count) |
| **REMOVE** | — | **none** (zero R3 deletions since `5725fa7d3`) |
| leave | `## Traps` | non-member topic block; not a phantom member |

After parent lands the three ADDs with live own-file anchors + verbatim symbols:

- expected `claims-check --row R3` → `sections=5`, `adv=0` (no `MEMBER_COUNT_SUSPECT`)
- R3 contribution to `R_sections` moves **2 → 5** (+3), subject to parent’s full-layer re-sum

### 4.3 Draft sections (verified anchors at origin `964f443ee53d`)

Parent may paste/adapt. Each carries ≥1 own-file anchor and ≥1 symbol present verbatim in that file.

#### `## \`native_profile.rs\` (276 L) — extends one-hop + bounds`

- `native_profile_entry` at `native_profile.rs:21` — resolves one `nativeProfiles` entry; `extends` pointer exactly one hop; refuses self-cycle, multi-hop, and inline keys other than `extends`/`note`.
- `NativeProfileBounds` at `native_profile.rs:118` — deadlines + backpressure bundle for the admitted profile.
- `NativeProfileBounds::from_parsed` at `native_profile.rs:175` — parse path used by the judge (`cost_ledger` / native judgment order cites this, not `execution_profile.rs`).
- `omp_bare_selector` at `native_profile.rs:260`.
- Included as `pub(crate) mod native_profile` from `lib.rs:20`.

#### `## \`cost_ledger_validation_tests.rs\` (306 L) — lineage + v1 budget pins`

- Included via `lib.rs:1175-1176`: `#[path = "cost_ledger_validation_tests.rs"] mod cost_ledger_validation_tests;`.
- `validate_cost_ledger_rejects_fabricated_mission_cumulative_with_prior_lineage` at `cost_ledger_validation_tests.rs:143`.
- `validate_cost_ledger_accepts_mission_cumulative_continuing_prior_lineage` at `:183`.
- `validate_cost_ledger_prior_lineage_falls_back_to_prior_round_totals` at `:214`.
- `require_cost_ledger_when_budgeted_names_v1_profile_trap` at `:279`.

#### `## \`execution_profile_tests.rs\` (560 L) — catalog + FailureClass matrix pins`

- Included via `execution_profile.rs:655-656`: `#[path = "execution_profile_tests.rs"] mod tests;`.
- `substrate_enum_is_exactly_the_seven_supported_surfaces` at `execution_profile_tests.rs:4`.
- `only_capacity_failures_advance_and_last_route_never_wraps` at `:287` (pins `permits_advance` / non-wrapping `next_route`).
- `failure_class_action_matrix_is_pinned_for_every_variant` at `:340`.
- `gemini_is_rejected_at_the_typed_route_boundary` at `:371`; `google_antigravity_is_admitted_by_the_typed_route_boundary` at `:386`.

### 4.4 Stale cites inside existing KEEP sections (repair while integrating)

| Note claim | Live at `964f443ee53d` |
|---|---|
| `cost_ledger.rs` (737 L) | **490 L** |
| `execution_profile.rs` (689 L) | **656 L** |
| `permits_advance` at `:448` | **`:429`** (`#[must_use]` on preceding lines; fn body starts 429) |
| `is_temporary` `:458` / `is_authorization` `:466` / `next_route` `:475-486` | live **`:439` / `:447` / `:456+`** (re-pin on integrate) |
| `ServiceTier` `:173` | live **`:168`** empty enum |
| `FailureClass` `:402-412` | live **`:397`** |
| `include!` omp chains `:572` | live **`:548`** |
| lineage walk `(:405-717)` under 490 L file | bounds must be re-measured; do not keep 717 |
| seat/totals pass line ranges | re-open against live `validate_cost_ledger_seats` `:120`, `validate_cost_ledger_totals` `:221` |

---

## 5. Registry / stanza (parent-only; this seat does not edit)

| Item | Current | Measured / required |
|---|---|---|
| R3 members cell count | `5 files (…)` | **5** (globs still exact; optional explicit 5-basename list) |
| R3 note gated sections | 2 | **5** after ADD drafts land |
| R3 deleted members | n/a | **0** |
| `R_members` stanza | 98 | live **92** (layer-wide; not R3-local) |
| R3’s share of `R_sections` | 2 (in SCORECARD arithmetic) | **5** once note is honest |

---

## 6. Unresolved blockers

**None for R3 membership.**  
All five glob members exist on disk; none deleted since `5725fa7d3`; no phantom section names a missing file.

**Integration dependency (parent):** three missing member sections must be written into `corpus/knowledge/cost-and-profile.md` before the row’s `yes` is section-honest at count 5. Until then `MEMBER_COUNT_SUSPECT` remains the correct gate reading. This seat did not edit the note.

**Stale internal line pins** in the two KEEP sections will fail `cite-check` / dead-anchor paths if those lines are treated as own-file anchors after size collapse; parent should refresh them in the same integrate pass.

---

## 7. Cross-domain findings (owner)

| Finding | Owner |
|---|---|
| Live `permits_advance` moved `:448` → `:429` (and sibling FailureClass lines). Historical aggregator ratification of `:448` (`D-50` era) is now stale against HEAD `964f443e`. | **kumitate** note repair on integrate; do not re-open aggregator lesson rewrite |
| `profile_shape_refusal_tests.rs` lives next to R3 profile files but is **R11** remainder — do not pull into R3 | **R11** census seat / parent boundary arithmetic |
| Layer `R_members` 98→92 and six deleted runtime/CLI files are outside R3 | sibling R* seats + parent stanza |
| Lane tree carries no `crates/` sources; all R3 evidence is origin-only | expected; not a defect |

---

## 8. Summary for parent

- **Member list (5):** `cost_ledger.rs`, `cost_ledger_validation_tests.rs`, `execution_profile.rs`, `execution_profile_tests.rs`, `native_profile.rs`
- **Declared count row must carry:** **5**
- **Sections removed:** **0**
- **Sections to add:** **3** (`cost_ledger_validation_tests.rs`, `execution_profile_tests.rs`, `native_profile.rs`) — drafts + live anchors above
- **Sections kept (refresh pins):** **2** (`cost_ledger.rs`, `execution_profile.rs`)
- **R3 contribution to `R_sections` after honest note:** **5** (from 2)
- **Files changed by this seat:** only this report
