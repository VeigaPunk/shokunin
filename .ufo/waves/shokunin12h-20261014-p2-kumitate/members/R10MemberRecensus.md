# R10MemberRecensus — runtime-layer family R10 (gate)

Lane: kumitate-shokunin · wave shokunin12h-20261014-p2-kumitate · round 32 re-census  
Seat: `R10MemberRecensus` (leaf) · origin HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9`  
Origin tree: `/home/vgpnk/Projects/ufo-fsd-alpha`  
Lane HEAD at dispatch: `175de6ba2e9e904010411b19cab27e0af9aad3d4`  
This report is data, not a verdict. Parent owns registry row + stanza.

## Axes touched

- coverage (runtime-layer membership honesty for R10)
- operability (claims gate re-derive path exercised)
- calibration (declared sizes / test census vs live tree)

## Files inspected

| Path | Role |
|---|---|
| `kumitate-shokunin/SCORECARD.md` | registry row R10 + round-32 `## Planned` |
| `kumitate-shokunin/corpus/README.md` | coverage map row for `knowledge/gate-verdict.md` |
| `kumitate-shokunin/corpus/knowledge/gate-verdict.md` | R10 note (section-form) |
| `kumitate-shokunin/scripts/claims-check.mjs` | anchor/section gate semantics |
| `$ORIGIN/crates/ufo-core-runtime/src/gate.rs` | live member |
| `$ORIGIN/crates/ufo-core-runtime/src/gate_tests.rs` | live member |

## Exact commands + observed output

### Live R10 membership (family pattern `gate*`)

```
$ ORIGIN=/home/vgpnk/Projects/ufo-fsd-alpha
$ git -C "$ORIGIN" rev-parse HEAD
964f443ee53df0ce06bd689af01f0dea031b01f9

$ ls -1 "$ORIGIN/crates/ufo-core-runtime/src"/gate*.rs | xargs -n1 basename
gate.rs
gate_tests.rs

$ wc -l "$ORIGIN/crates/ufo-core-runtime/src/gate.rs" \
        "$ORIGIN/crates/ufo-core-runtime/src/gate_tests.rs"
  203 .../gate.rs
  206 .../gate_tests.rs
  409 total

$ grep -c '#\[test\]' "$ORIGIN/crates/ufo-core-runtime/src/gate_tests.rs"
12
```

### Layer universe (context only; not R10 membership)

```
$ ls -1 "$ORIGIN/crates/ufo-core-runtime/src"/*.rs | wc -l
88
$ ls -1 "$ORIGIN/crates/ufo-cli/src"/*.rs | wc -l
4
# ⇒ R_members live = 92 (matches round-32 Planned pre-registration)
```

### Deletions since `5725fa7d3` (gate family filter)

```
$ git -C "$ORIGIN" diff --diff-filter=D --name-only 5725fa7d3..HEAD -- '**/gate*.rs'
# (empty — no gate*.rs deleted)

$ git -C "$ORIGIN" diff --diff-filter=D --name-only 5725fa7d3..HEAD \
    -- 'crates/ufo-core-runtime/src/*.rs' 'crates/ufo-cli/src/*.rs'
crates/ufo-cli/src/admission.rs
crates/ufo-core-runtime/src/native_epoch.rs
crates/ufo-core-runtime/src/native_epoch_tests.rs
crates/ufo-core-runtime/src/native_launch_tests.rs
crates/ufo-core-runtime/src/replay_falsification_probes.rs
crates/ufo-core-runtime/src/rfc3339.rs
```

None of the six deleted `.rs` files are R10 members. R10 membership is unchanged by the restructure deletion set.

### Declared vs live `comm -3` (both sides `LC_ALL=C sort`)

```
$ printf '%s\n' gate.rs gate_tests.rs | LC_ALL=C sort > /tmp/r10_declared.txt
$ ls -1 "$ORIGIN/crates/ufo-core-runtime/src"/gate*.rs | xargs -n1 basename \
    | LC_ALL=C sort > /tmp/r10_live.txt
$ LC_ALL=C comm -3 /tmp/r10_declared.txt /tmp/r10_live.txt
# (empty)
```

### Registry row (SCORECARD.md:136) vs note

| Source | Claim |
|---|---|
| Registry R10 members cell | `` `gate.rs` (254 L) + `gate_tests.rs` (426 L) `` · covered `yes` · note stem `gate-verdict` |
| Note path | `corpus/knowledge/gate-verdict.md` |
| Note member headings | `## \`crates/ufo-core-runtime/src/gate.rs\`` (L14) · `## \`crates/ufo-core-runtime/src/gate_tests.rs\`` (L179) |
| Note non-member heading | `## Member-completeness probe` (L235) — not a member section |
| README map | `knowledge/gate-verdict.md` → R10, 2 of 2 |

### Claims gate (authority for section liveness)

```
$ node scripts/claims-check.mjs \
    --self /home/vgpnk/Projects/shokunin/kumitate-shokunin \
    --src /home/vgpnk/Projects/ufo-fsd-alpha \
    --row R10
ROWS: 1  YES: 1  NOTES: 1  SECTIONS: 2
ROW R10  form=section   notes=1 sections=2 adv=0
SUMMARY: errors=0 warnings=0
CLAIMS: MATCH (rows=1 yes=1 notes=1 sections=2 adv=0)
```

JSON section rows (abbreviated):

| heading | file | anchors | live | symbols | symbolHit | inFamily |
|---|---|---:|---|---:|---|---|
| `crates/ufo-core-runtime/src/gate.rs` | same | 94 | true | 76 | true | true |
| `crates/ufo-core-runtime/src/gate_tests.rs` | same | 23 | true | 13 | true | true |

Gate rule satisfied: ≥1 own-file anchor live (1 ≤ line ≤ file length, non-blank) and ≥1 backticked symbol verbatim in the member file, per section.

## Derived member list

**R10 live members (ordered, basename):**

1. `gate.rs` — `crates/ufo-core-runtime/src/gate.rs` (203 L)
2. `gate_tests.rs` — `crates/ufo-core-runtime/src/gate_tests.rs` (206 L)

**Declared count the registry row must carry: `2`**

No phantom members. No widening into other families. No CLI members in R10.

## Sections added / removed

| Action | Section | Reason |
|---|---|---|
| **none added** | — | both live members already have one `## \`crates/ufo-core-runtime/src/<member>\`` heading |
| **none removed** | — | no R10 member file deleted since `5725fa7d3`; both headings resolve under `--src` |

Leaf seat wrote **only** this advisory report. Note body was **not** rewritten here (parent integrates). Membership honesty does not require a section edit for R10.

## Size / pin drift inside the still-valid note (parent hygiene, not membership)

The claims gate still MATCHEs because enough own-file anchors remain live, but the note and registry cell still quote the **pre-restructure** sizes and test census:

| Claim (note / registry) | Live at `964f443e` |
|---|---|
| `gate.rs` 254 L | **203 L** |
| `gate_tests.rs` 426 L | **206 L** |
| 19 `#[test]` | **12** `#[test]` |
| origin path prose `origin-work/ufo-fsd-alpha` @ `daa371583` | live tree is `~/Projects/ufo-fsd-alpha` @ `964f443e` |

Many historical line citations in the note body are past EOF (e.g. bare `:212+` on a 203-line `gate.rs`); they are inert under the gate’s “≥1 live” rule but are stale calibration debt. Parent may refresh anchors/sizes when editing the cell; not required to keep R10’s member count honest.

Live symbol anchors that still resolve (sample, for parent re-pin if desired):

- `gate.rs`: `GateDecision` :15 · `ParetoGate` :44 · `new` :52 · `decide` :70 · `decide_with_deltas` :89 · `scan` :112 · `verdict` :155 · `validate_vector` :171 · `#[path = "gate_tests.rs"]` :201–203
- `gate_tests.rs`: `filled` :3 · `admits_strict_improvement` :12 · `rejects_no_improvement` :39 · `regression_is_not_rescued_by_a_large_gain` :141 · 12× `#[test]`

## Unresolved blockers

**None for R10 membership / section completeness.**

- Member list stable at 2.
- Sections = 2, both in-family, both live under claims-check.
- No deleted-member section to strip.
- Declared count for the row: **2**.

## Cross-domain findings (owner: parent / other seats)

1. **Registry cell line counts stale (owner: parent SCORECARD edit).** Cell still prints `(254 L)` / `(426 L)`; live is 203 / 206. Does not change member cardinality.
2. **Note HEAD/path pin stale (owner: parent note integrate).** Header still cites `origin-work/ufo-fsd-alpha` and `daa371583`.
3. **Test-census prose stale (owner: parent note).** “19-`#[test]`” / registry cell “19-`#[test]` census” → live 12.
4. **Layer `R_members` 98→92 is real (owner: StanzaDerivation / parent).** Confirmed 88+4; R10 contributes 2 unchanged. Deletion set of 6 `.rs` is entirely outside R10 (R11/CLI seats).
5. **OOB cite residue (owner: parent, optional).** High dead-anchor count with still-`live: true` sections — gate honesty holds; depth/freshness of internals prose is separate from this membership re-census.

## Summary for parent integrate

```
R10_members_live = [gate.rs, gate_tests.rs]
R10_declared_count = 2
R10_sections_added = 0
R10_sections_removed = 0
R10_claims_row = MATCH sections=2 adv=0
R10_note = corpus/knowledge/gate-verdict.md
R10_sizes_live = gate.rs:203 gate_tests.rs:206
R10_tests_live = 12
```

No leaf note mutation. Parent may optionally refresh size/test/pin prose when rewriting the R10 cell; membership and gated section count are already correct at **2 / 2**.
