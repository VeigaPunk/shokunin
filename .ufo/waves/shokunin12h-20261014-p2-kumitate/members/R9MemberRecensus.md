# R9MemberRecensus — round-32 unjudged re-census

Lane: kumitate-shokunin @ `175de6ba2e9e904010411b19cab27e0af9aad3d4`  
Origin (read-only): `/home/vgpnk/Projects/ufo-fsd-alpha` @ `964f443ee53df0ce06bd689af01f0dea031b01f9`  
Family: **R9 — judge test suite**  
Note under probe: `corpus/knowledge/test-inventories.md`  
This report is data for the parent integrator. Not a verdict.

---

## 1. Live membership (direct enumeration)

**Family definition (registry cell patterns).**  
`familyPatterns()` on the R9 members cell yields exactly one pattern: `` `native_tests.rs` ``.  
SCORECARD prose already states the other large test bodies sit in R2 / R6 / R7, not R9.

**Command (stated):**

```bash
ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/native_tests.rs
```

**Observed output:**

```
/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/native_tests.rs
```

**Count command:**

```bash
ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/native_tests.rs | wc -l
```

**Observed:** `1`

**Layer context (not R9 membership, boundary only):**

```bash
ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/*.rs | wc -l   # → 88
ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src/*.rs | wc -l             # → 4
# R_members live = 88 + 4 = 92 (matches round-32 Planned measurement)
```

### Exact live member list (R9)

| # | Rel path under origin |
|---|------------------------|
| 1 | `crates/ufo-core-runtime/src/native_tests.rs` |

**Declared count the registry row must carry: `1`.**

Suggested cell shape (parent-owned wording):  
`1 member: \`native_tests.rs\` (308 \`#[test]\` / 10968 L at origin HEAD; was 340 at note pin rev)`  
— or keep the single-basename form without an integer *only if* the claims gate is not asked to enforce `RE_MEMBERS` against the note’s distinct section set (see §4).

---

## 2. Deletions since `5725fa7d3` (NOT R9 members)

```bash
git -C /home/vgpnk/Projects/ufo-fsd-alpha diff --diff-filter=D --name-only \
  5725fa7d3..HEAD -- crates/ufo-core-runtime/src crates/ufo-cli/src
```

**Observed deleted paths:**

```
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
```

Of these, the two `*_tests.rs` files existed at `5725fa7d3` and are **ABSENT** now:

```bash
# both print ABSENT
for f in native_epoch_tests.rs native_launch_tests.rs; do
  test -f /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/$f \
    && echo LIVE $f || echo ABSENT $f
done
```

They were **never** R9 patterns. Live evidence they belonged to **R11** remainder note:

- `corpus/knowledge/runtime-remainder-census.md` still carries  
  `## \`crates/ufo-core-runtime/src/native_epoch_tests.rs\`` and  
  `## \`crates/ufo-core-runtime/src/native_launch_tests.rs\``  
  → owner: **R11 recensus** (remove those sections; not this lane).

`native_tests.rs` itself is **LIVE** (not in the deletion set).

---

## 3. Registry row vs note (comparison)

| Source | Claim |
|--------|--------|
| SCORECARD registry R9 members cell | `` `native_tests.rs` `` (340 cases; other big tests in R2/R6/R7) |
| SCORECARD note pointer | yes — `test-inventories` (r7) → `corpus/knowledge/test-inventories.md` |
| Live tree | sole member `native_tests.rs` still present |
| Note `##` member-file sections | 4 backtick-headed sections (see §4) |

**Membership delta vs registry:** none — still the single live file the cell names.  
**Prose/stat delta (not a membership change):** note still says **340** tests; live file has **308** `#[test]` and **10968** lines.

```bash
grep -c '#\[test\]' .../native_tests.rs   # → 308
wc -l < .../native_tests.rs               # → 10968
```

Attachment still via `#[path = "native_tests.rs"]` on `native.rs` (now ~`:684`, not the note’s historical `:765-767`).

---

## 4. Note sections — added / removed / retained

### Gate probe (evidence)

```bash
node scripts/claims-check.mjs --row R9 --src /home/vgpnk/Projects/ufo-fsd-alpha
```

**Observed summary:**

```
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 4
ROW R9   form=section   notes=1 sections=4 adv=3
CLAIMS  warn  SECTION_FILE_NOT_MEMBER  .../loop_driver_tests.rs
CLAIMS  warn  SECTION_FILE_NOT_MEMBER  .../local_ship_tests.rs
CLAIMS  error SECTION_DEAD_ANCHOR      .../distill_tests.rs — own-file anchors 2031-2031 are dead
CLAIMS  warn  SECTION_FILE_NOT_MEMBER  .../distill_tests.rs
CLAIMS: DRIFT (SECTION_DEAD_ANCHOR ...)
```

Per-section JSON (`--json`):

| heading | file | inFamily | live | anchors | symbolHit |
|---------|------|----------|------|---------|-----------|
| `native_tests.rs` | `crates/ufo-core-runtime/src/native_tests.rs` | **true** | **true** | 12 | true |
| `loop_driver_tests.rs` | `.../loop_driver_tests.rs` | false | true | 9 | true |
| `local_ship_tests.rs` | `.../local_ship_tests.rs` | false | true | 3 | true |
| `distill_tests.rs` | `.../distill_tests.rs` | false | **false** | 1 (`:2031`) | true |

Non-member topic heads in the same note (not gated as file sections):  
`## Pinning style (shared)`, `## Cross-suite ownership (avoid double-pinning)`.

### Sections added

**None.** The sole declared member already has:

```markdown
## `native_tests.rs` — 340 tests / 34 groups (judge pipeline pins)
```

Gate: `inFamily=true`, `live=true` (at least one own-file bare/pathish anchor resolves to a non-blank line), `symbolHit=true`.  
**No new `## \`…\`.rs` section is required for membership honesty.**

(Optional parent polish, not membership: refresh “340” → “308”, re-home dead bare anchors `:11064`/`:11101`/`:11136` which sit past EOF 10968, and `native.rs:765-767` → current `#[path]` line. Dead co-anchors do **not** fail the gate while any sibling own-file anchor stays live.)

### Sections removed (deleted-file rule)

**None for R9.**  
No R9 note section names a file deleted since `5725fa7d3`.  
`native_epoch_tests.rs` / `native_launch_tests.rs` never appeared under this note.

### Out-of-family sections (still live files — not deletions)

The three `## \`loop_driver_tests.rs\`` / `## \`local_ship_tests.rs\`` / `## \`distill_tests.rs\`` heads remain **present on disk** and are **correctly classified** as R2 / R7 / R6 territory (registry + historical SCORECARD R9 out-of-family residual). Under the round-32 rule *“remove sections for deleted files”* they are **not** removal candidates for absence.

They **do** create:

1. Three `SECTION_FILE_NOT_MEMBER` advisories on every R9 claims run (status quo since layer-axes measurement: R9 contributes **1** in-family section to `R_sections`, not 4).
2. One hard **`SECTION_DEAD_ANCHOR`** on `distill_tests.rs:2031` — file is now **1727 L** / **44** `#[test]` (note still says 57). This alone makes `CLAIMS: DRIFT` for `--row R9`.

**Parent choice (integrator-owned; this member does not edit the note):**

- **Minimal DRIFT clear:** retarget or drop the single dead bare anchor `:2031` inside the distill section (or replace with a live own-file line), keeping cross-suite inventory prose.
- **Strict family honesty / integer cell:** if the R9 cell is rewritten to `1 member`, either (a) demote the three foreign `## \`*.rs\`` heads so they are not `RE_CHUNK_HEAD` file sections, or (b) move that inventory to R2/R6/R7 notes — otherwise `MEMBER_COUNT_DRIFT` fires (`declared 1` vs `distinct sections = 4`).

---

## 5. Member list parent should pin

```
R9_members = 1
crates/ufo-core-runtime/src/native_tests.rs
```

**In-family gated sections today:** 1 (`native_tests.rs`)  
**Sections added by this wave:** 0  
**Sections removed by this wave (deleted members):** 0  
**Declared count the row must carry:** **1**

---

## 6. Unresolved blockers

| ID | Severity | Detail | Owner |
|----|----------|--------|-------|
| B1 | gate error | `SECTION_DEAD_ANCHOR` on out-of-family `distill_tests.rs:2031` (file 1727 L) blocks `CLAIMS: MATCH` for `--row R9` | parent note edit on `test-inventories.md` |
| B2 | advisory ×3 | `SECTION_FILE_NOT_MEMBER` for loop/local_ship/distill sections — expected if cross-suite inventory stays under R9’s note | parent (keep + accept adv, or demote/move) |
| B3 | prose stale | note “340 tests” vs live 308; several native_tests bare anchors past EOF; `native.rs` path cite stale | parent optional cite refresh |
| B4 | not R9 | R11 note still sections deleted `native_epoch_tests.rs` + `native_launch_tests.rs` | **R11MemberRecensus** / parent R11 row |

No blocker on **existence** of the sole R9 member or on presence of its in-family `##` section.

---

## 7. Cross-domain findings (with owner)

| Finding | Owner |
|---------|--------|
| Live `R_members` = 92 (88 runtime + 4 cli), not frozen 98 | parent stanza / proxy-check re-pin |
| Deleted `native_epoch_tests.rs`, `native_launch_tests.rs` (and non-test companions) | R11 remainder census + registry arithmetic |
| `loop_driver_tests.rs` / `local_ship_tests.rs` / `distill_tests.rs` family homes | R2 / R7 / R6 rows (already); inventory text currently housed in R9 note |
| `gate_tests.rs` is R10, not R9 (note body mentions it; no R9 `##` head) | R10 |
| `membrane-seal write` argv defect | filed out-of-province; not absorbed |

---

## 8. Files inspected

- `kumitate-shokunin/SCORECARD.md` (registry R9 row, runtime-layer math, `## Planned` round 32)
- `kumitate-shokunin/corpus/README.md` (map row for `knowledge/test-inventories.md`)
- `kumitate-shokunin/corpus/knowledge/test-inventories.md` (all `##` heads + anchors)
- `kumitate-shokunin/corpus/knowledge/runtime-remainder-census.md` (deleted-test section heads — R11)
- `kumitate-shokunin/scripts/claims-check.mjs` (`familyPatterns`, section probe, `RE_MEMBERS`)
- Origin: `crates/ufo-core-runtime/src/native_tests.rs`, `loop_driver_tests.rs`, `local_ship_tests.rs`, `distill_tests.rs`, `gate_tests.rs`, `native.rs` (`#[path]`), full `src/*.rs` + `ufo-cli/src/*.rs` listings
- `git diff --diff-filter=D 5725fa7d3..HEAD` on runtime+cli paths

## 9. Files changed by this member

- **Only** this advisory:  
  `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p2-kumitate/members/R9MemberRecensus.md`  
- Registry row, note body, and proxy stanza: **parent-owned** — not mutated here.

---

## 10. Bottom line for integrator

1. **R9 live membership = `{ native_tests.rs }` → declared count `1`.**  
2. **In-family section already present and gate-live** → sections added = 0.  
3. **No deleted-file section to strip from the R9 note** → sections removed = 0 under the deletion rule.  
4. Clear **`SECTION_DEAD_ANCHOR` on distill** (and decide fate of the three foreign `##` heads) before R9 can read `CLAIMS: MATCH`.  
5. Do **not** invent members; do **not** fold R2/R6/R7 test files into R9’s declared set.
