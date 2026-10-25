# R6MemberRecensus — advisory (unjudged fleet wave)

**Seat:** `R6MemberRecensus` (leaf). Not a judge verdict. No registry row, stanza, commit, push, or gate run by this seat. Parent owns `SCORECARD.md` R6 cell + `kumitate-proxy-v1` terms.
**Lane:** `/home/vgpnk/Projects/shokunin/kumitate-shokunin` HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4`
**Origin:** `/home/vgpnk/Projects/ufo-fsd-alpha` HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`
**Family:** R6 — dedupe + L3
**Note:** `corpus/knowledge/distill-and-l3.md`
**Measured:** 2026-10-14

**Axes (named, not scored here):** coverage (member sections vs live members), operability (enumeration + claims gate exit), calibration (declared count equals live set; no phantom members).

---

## Exact live membership (R6)

**Enumeration command** (stated; both sides of any `comm` use `LC_ALL=C sort`):

```bash
ls -1 "$UFO_SRC/crates/ufo-core-runtime/src/"{distill,l3_swarm}*.rs \
  | xargs -n1 basename | LC_ALL=C sort
```

with `UFO_SRC=/home/vgpnk/Projects/ufo-fsd-alpha`.

**Observed output (exact member list, N=4):**

```
distill.rs
distill_tests.rs
l3_swarm.rs
l3_swarm_tests.rs
```

**Line counts (`wc -l`):**

| Member | Lines |
|---|---:|
| `distill.rs` | 1146 |
| `distill_tests.rs` | 1727 |
| `l3_swarm.rs` | 496 |
| `l3_swarm_tests.rs` | 267 |
| **sum** | **3636** |

**Declared count the R6 registry row must carry:** **4** (unchanged from the cell’s “4 files (`distill*`, `l3_swarm*`)” — the glob still matches exactly these four basenames; no widen, no invent).

**CLI surface:** R6 has **zero** members under `crates/ufo-cli/src` (family is runtime `distill*` + `l3_swarm*` only).

---

## Deletion probe since `5725fa7d3`

```bash
git -C "$UFO_SRC" diff --diff-filter=D --name-only 5725fa7d3..HEAD -- \
  'crates/ufo-core-runtime/src/distill*' 'crates/ufo-core-runtime/src/l3_swarm*'
```

**Observed:** empty (0 paths).

```bash
comm -3 \
  <(git -C "$UFO_SRC" ls-tree --name-only 5725fa7d3 crates/ufo-core-runtime/src/ \
      | grep -E 'distill|l3_swarm' | xargs -n1 basename | LC_ALL=C sort) \
  <(ls -1 "$UFO_SRC/crates/ufo-core-runtime/src/"{distill,l3_swarm}*.rs \
      | xargs -n1 basename | LC_ALL=C sort)
```

**Observed:** empty. All four R6 members present at `5725fa7d3` and still present at `964f443e`.

**Runtime+CLI deletions since `5725fa7d3` (not R6 — cross-family inventory only):**

```
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
```

None match `distill*` / `l3_swarm*`. **No R6 section removals for deleted files.**

Layer context (dispatch-stated, re-measured): `ls crates/ufo-core-runtime/src/*.rs | wc -l` → **88**; `ls crates/ufo-cli/src/*.rs | wc -l` → **4**; **R_members = 92**.

---

## Registry row vs note vs live

| Source | Claim | Observed |
|---|---|---|
| `SCORECARD.md` R6 cell | 4 files (`distill*`, `l3_swarm*`); `yes` — distill-and-l3 (r7) | Glob live match = 4; cell arithmetic still correct |
| `corpus/README.md` map row for `knowledge/distill-and-l3.md` | Primary sources cite `distill.rs` (1553 L), `l3_swarm.rs` (591 L), plus `live.rs` / `native_contract.rs` | Line counts **stale** (now 1146 / 496). `live.rs` is **R4**, not R6 — map prose only |
| Note `##` sections | 2: ``## `distill.rs` …`` (L3), ``## `l3_swarm.rs` …`` (L78) | **Missing** `distill_tests.rs`, `l3_swarm_tests.rs` |
| Historical SCORECARD in-family sum | `R6` **2** sections | Matches note; under-covers live 4 |

**Section membership `comm -3` (note headings vs live members):**

```bash
comm -3 \
  <(rg -o '^## `([^`]+)`' -r '$1' corpus/knowledge/distill-and-l3.md | LC_ALL=C sort) \
  <(ls -1 "$UFO_SRC/crates/ufo-core-runtime/src/"{distill,l3_swarm}*.rs \
      | xargs -n1 basename | LC_ALL=C sort)
```

**Observed:**

```
	distill_tests.rs
	l3_swarm_tests.rs
```

(tab-prefixed = live-only / note-missing). No note-only phantoms.

---

## Claims gate (this seat, read-only)

```bash
cd /home/vgpnk/Projects/shokunin/kumitate-shokunin
node ./scripts/claims-check.mjs --row R6 --src /home/vgpnk/Projects/ufo-fsd-alpha
```

**Default (non-strict) observed:**

```
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 2
ROW R6   form=section   notes=1 sections=2 adv=1
CLAIMS  warn  MEMBER_COUNT_SUSPECT     row=R6  declared 4, found 2 distinct sections
SUMMARY: errors=0 warnings=1
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=2 adv=1)
```

**`--json` section facts:** both existing sections `live=true`, `inFamily=true`, `symbolHit=true` (`distill.rs` anchors=22 symbols=31; `l3_swarm.rs` anchors=10 symbols=21).

**`--strict` observed:**

```
CLAIMS: DRIFT (MEMBER_COUNT_SUSPECT row=R6 declared 4, found 2 distinct sections)
```

So R6 is the classic **declared-4 / section-2** hole: non-strict MATCH with advisory; strict DRIFT. Parent cannot claim honest `yes` at full member coverage until the two missing sections land.

---

## Sections added / removed (this seat’s measured delta for parent)

| Action | Section | Status |
|---|---|---|
| **KEEP** | `## distill.rs` | Present; `live=true`; keep. Heading still advertises “1553 lines” — **stale** (file is 1146). Many `:line` anchors predate the shrink (see calibration note). |
| **KEEP** | `## l3_swarm.rs` | Present; `live=true`; keep. Heading still advertises “591 lines” — **stale** (file is 496). |
| **ADD** (required for 4/4) | `## distill_tests.rs` | **Absent.** Live member. 44 `#[test]` cases; path companion via `distill.rs` cfg. |
| **ADD** (required for 4/4) | `## l3_swarm_tests.rs` | **Absent.** Live member. 12 `#[test]` cases; `#[path = "l3_swarm_tests.rs"]` at `l3_swarm.rs:494-496`. |
| **REMOVE** | _(none)_ | No deleted R6 files since `5725fa7d3`; no phantom `##` headings naming absent files. |

**Sections added by this seat to the note:** **0** (report-only; parent integrates note edits).
**Sections removed by this seat from the note:** **0**.
**Sections parent must add before re-claiming full R6 coverage:** **2** (`distill_tests.rs`, `l3_swarm_tests.rs`).
**Sections parent must remove:** **0**.

After parent adds the two sections with ≥1 own-file anchor + ≥1 verbatim symbol each, expected gate shape: `sections=4`, `MEMBER_COUNT_SUSPECT` cleared, `--strict` MATCH for `--row R6`.

---

## Suggested live anchors for missing sections (data for parent; not applied)

### `distill_tests.rs` (1727 L, 44 tests)

Resolving symbols in **that file** (examples):

- `dispatch_lane_uses_honest_local_collapse` `:22`
- `local_dedupe_normalizes_claim_and_evidence_order_not_author` `:211`
- `local_dedupe_binds_declared_write_bytes_not_scores` `:222`
- `high_confidence_requires_two_distinct_known_route_groups` `:446`
- `source_map_is_sealed_until_idempotent_post_score_reveal` `:882`
- `distill_result_admits_bound_candidate_receipts` `:1178`
- `qwen_output_must_classify_once_and_supply_nonempty_reasons` `:631`

Census needle: `rg -c '#\[test\]' distill_tests.rs` → **44**.

### `l3_swarm_tests.rs` (267 L, 12 tests)

- `parses_chain_and_rejects_primary_fallback_keys` `:16`
- `concurrency_ceiling_is_not_clamped_to_native_32` `:48`
- `chain_length_is_bounded` `:68`
- `walks_chain_only_on_capacity_failures_and_never_wraps` `:154`
- `non_capacity_failure_does_not_advance` `:198`
- `rejects_opencode_and_native_handoff_admission` `:224`
- `every_chain_step_is_a_served_provider_model_effort` `:259`

Census needle: `rg -c '#\[test\]' l3_swarm_tests.rs` → **12**.

### Existing sections — calibration drift (not blockers for membership)

Gate still reports `symbolHit=true` / `live=true`, but prose line pins predate the restructure. Spot-check against HEAD `964f443e`:

| Note claim | Live fact |
|---|---|
| `distill.rs` 1553 L | **1146** L |
| `identity_key` / `mediated_class_vector` / `SynthesisFailure` named | **MISSING** as identifiers (`rg` empty); survivor path now centers `dedupe` `:…`, `run_phase` `:969`, `validate_qwen_synthesis` `:627`, `reveal_source_map_after_score` `:175`, `admit_integrated_candidate` `:220` |
| contract `ufo.dedupe.v4` in narrative | live brief/contract string observed `ufo.dedupe.v3` at `distill.rs:472` ([INFERENCE] full contract story needs parent re-read, not asserted here) |
| `run_phase` `:1348-1498` | **OUT_OF_RANGE** (file ends 1146); live `run_phase` at `:969` |
| `l3_swarm.rs` 591 L | **496** L |
| `apply_reroute` `:479-540` | live `apply_reroute` at `:431` |
| `refuse_native_handoff_admission` `:578-591` | live at `:483` (module ends `:496` with `#[path = "l3_swarm_tests.rs"]`) |
| `L3_CONCURRENCY_CEILING` `:24` | live `:20` |
| `CANONICAL_L3_CHAIN` bare model tags in note | live routes are **provider-qualified** (`openai-codex/…`, `xai-oauth/…`, `alibaba-token-plan/…`) at `:28-38` |

Parent should re-anchor when touching the note; membership recensus does **not** require rewriting the two existing sections to close `MEMBER_COUNT_SUSPECT` — only the two missing member headings.

---

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | R6 registry cell; round-32 `## Planned` / retired successors; layer formulas |
| `kumitate-shokunin/corpus/README.md` | map row for `distill-and-l3.md` |
| `kumitate-shokunin/corpus/knowledge/distill-and-l3.md` | R6 note (2 sections) |
| `kumitate-shokunin/scripts/claims-check.mjs` | member-claims gate |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/distill.rs` | live member |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/distill_tests.rs` | live member (no section) |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/l3_swarm.rs` | live member |
| `ufo-fsd-alpha/crates/ufo-core-runtime/src/l3_swarm_tests.rs` | live member (no section) |

---

## Unresolved blockers

1. **Note under-sectioned (owner: parent / note editor).** `distill_tests.rs` + `l3_swarm_tests.rs` lack `##` sections → `MEMBER_COUNT_SUSPECT` / strict DRIFT. This seat did not edit the note (write-only report path).
2. **Stale line/symbol pins inside kept sections (owner: parent).** Gate still accepts via other anchors/symbols; honesty of internals prose is degraded post-restructure.
3. **No R6 membership blocker from deletions.** Live set = 4 = declared glob.

---

## Cross-domain findings (owner named; not absorbed)

| Finding | Owner |
|---|---|
| Note + README still cite `live.rs` `QWEN_RESPONSE_FORMAT` / `ufo_dedupe_v2` schema staleness as distill-adjacent defect | **R4** (`live*` family) for the code; kumitate note may keep report-class cite but must not pull `live.rs` into R6 membership |
| `native_contract.rs` 63rd-entry ordinal cited from R6 note | **R1** / contract registry owner; verify ordinal after runtime file deletions |
| Layer `R_members` 98→92 and six non-R6 `.rs` deletions | Parent stanza + other family seats (R1/R8/R11/CLI), not R6 |
| R9 historically carries out-of-family `distill_tests.rs` section (`SECTION_FILE_NOT_MEMBER`) | **R9** note owner (`test-inventories.md`) — confirm whether that out-of-family heading still exists; R6 adding a proper section does not auto-remove R9’s |

---

## Summary for parent integration

| Field | Value |
|---|---|
| **Exact member list** | `distill.rs`, `distill_tests.rs`, `l3_swarm.rs`, `l3_swarm_tests.rs` |
| **Declared count row must carry** | **4** |
| **Sections present** | 2 (`distill.rs`, `l3_swarm.rs`) |
| **Sections to add** | 2 (`distill_tests.rs`, `l3_swarm_tests.rs`) |
| **Sections to remove** | 0 |
| **R6 contribution to `R_sections` if completed** | **4** in-family (was 2 in historical sum) |
| **This seat file edits** | report only — this path |

End of advisory. No verdict.
