# StanzaDerivation — round-32 layer-term re-derivation

Leaf advisory only. Did **not** edit `SCORECARD.md`. Parent lands the stanza.

## Identity

| Field | Value |
|---|---|
| Member | `StanzaDerivation` |
| Lane | `/home/vgpnk/Projects/shokunin/kumitate-shokunin` |
| Lane HEAD | `175de6ba2e9e904010411b19cab27e0af9aad3d4` |
| Origin `--src` | `/home/vgpnk/Projects/ufo-fsd-alpha` |
| Origin HEAD | `964f443ee53df0ce06bd689af01f0dea031b01f9` (`964f443e`) |
| Contract | `kumitate-proxy-v1` / `kumitate-claims-v1` |
| Scope | Re-derive `S_members S_sections R_members R_sections coverage_script coverage_runtime` only |

## Files inspected

- `SCORECARD.md` — current `<!-- kumitate-proxy-v1` block (lines 276–300) and `## Planned` round-32 pre-registration (1364–1409)
- `scripts/proxy-check.mjs` — `LAYER_PATTERNS` (317–320), `layerOf` / `layerCoverage` / `layerTerms` (554–605)
- `scripts/claims-check.mjs` — `probeSections` import surface (used by proxy in-process)
- `corpus/knowledge/executable-scorecard.md` — term → frozen command table

## Commands + observed output

### 1. Live origin member enumeration (layer universe)

```text
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/scripts/*.mjs | wc -l
73
$ find /home/vgpnk/Projects/ufo-fsd-alpha/scripts -mindepth 2 -type f | wc -l
18
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/*.rs | wc -l
88
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src/*.rs | wc -l
4
```

Independent layer-filter replication of `LAYER_PATTERNS`:

- `S`: `^scripts/[^/]+\.mjs$` ∪ `^scripts/[^/]+/.+` → **91** (= 73 + 18)
- `R`: `^crates/ufo-core-runtime/src/[^/]+\.rs$` ∪ `^crates/ufo-cli/src/[^/]+\.rs$` → **92** (= 88 + 4)

Matches dispatch census (`S_members 91`, `R_members 92`) and Planned pre-registration.

### 2. `node scripts/claims-check.mjs --json`

```text
cwd: /home/vgpnk/Projects/shokunin/kumitate-shokunin
exit: 1
src: /home/vgpnk/Projects/ufo-fsd-alpha
verdict: DRIFT
totals: rows=19 yes=19 notes=27 sections=146 errors=32 warnings=14 adv=14
```

Per-row **in-family** section counts (`s.inFamily === true` only — the proxy numerator):

| row | form | n sections | inFamily | notes |
|---|---|---:|---:|---|
| S1–S5 | topic | 0 | 0 | `ROW_NO_SECTIONS` |
| S6 | section | 5 | **5** | all live |
| S7 | section | 9 | **6** | 3 unresolved: `probe-ufo-route-health.test.mjs`, `probe-redact.test.mjs`, `atomic-write.mjs` |
| S8 | section | 60 | **45** | 15 unresolved (mostly deleted `*.test.mjs` + `charter-scribe/sync.test.mjs`) |
| R1 | section | 8 | **8** | |
| R2,R5,R7 | topic | 0 | 0 | |
| R3 | section | 2 | **2** | |
| R4 | section | 3 | **3** | |
| R6 | section | 2 | **2** | |
| R8 | section | 4 | **4** | |
| R9 | section | 4 | **1** | 3 out-of-family (`loop_driver_tests`, `local_ship_tests`, `distill_tests`) excluded |
| R10 | section | 2 | **2** | |
| R11 | section | 47 | **41** | 6 unresolved: `native_epoch.rs`, `native_epoch_tests.rs`, `native_launch_tests.rs`, `replay_falsification_probes.rs`, `rfc3339.rs`, `ufo-cli/src/admission.rs` |

Layer sums from claims JSON:

- `S_sections` = 5 + 6 + 45 = **56**
- `R_sections` = 8 + 2 + 3 + 2 + 4 + 1 + 2 + 41 = **63**

(Gate raw `sections=146` still counts unresolved + out-of-family headings; proxy does not.)

### 3. `node scripts/proxy-check.mjs` / `--json`

Text verdict (exit 1):

```text
PROXY  error  S_MEMBERS_DRIFT  S_members: declared=114 computed=91 delta=-23
PROXY  error  S_SECTIONS_DRIFT  S_sections: declared=74 computed=56 delta=-18
PROXY  error  R_MEMBERS_DRIFT  R_members: declared=98 computed=92 delta=-6
PROXY  error  R_SECTIONS_DRIFT  R_sections: declared=69 computed=63 delta=-6
PROXY  error  COVERAGE_RUNTIME_DRIFT  coverage_runtime: declared=7 computed=6 delta=-1
PROXY  error  AXES_DRIFT  coverage:runtime-layer: ## Axes row=7 derived=6
PROXY: DRIFT (S_MEMBERS_DRIFT term=S_members declared=114 computed=91 delta=-23; S_SECTIONS_DRIFT term=S_sections declared=74 computed=56 delta=-18; R_MEMBERS_DRIFT term=R_members declared=98 computed=92 delta=-6; R_SECTIONS_DRIFT term=R_sections declared=69 computed=63 delta=-6; COVERAGE_RUNTIME_DRIFT term=coverage_runtime declared=7 computed=6 delta=-1; AXES_DRIFT term=coverage:runtime-layer declared=7 computed=6)
```

`--json` `terms` (layer keys only):

```json
{
  "S_members": 91,
  "S_sections": 56,
  "R_members": 92,
  "R_sections": 63,
  "coverage_script": 6,
  "coverage_runtime": 6
}
```

Other legacy/K terms unchanged vs stanza (`A=6 C=11 C1=19 C1_total=19 C2=74 C2_total=74` observed; no drift findings on them).

### 4. Score arithmetic (frozen `layerCoverage`)

`C1s/C1s_total = 8/8`, `C1r/C1r_total = 11/11` (all S/R registry cells still `yes`).

```text
coverage_script  = floor(10 × 8/8 × 56/91) = floor(6.1538…) = 6
coverage_runtime = floor(10 × 11/11 × 63/92) = floor(6.8478…) = 6
```

Round-32 move targets (for parent / census peers, **not** current stanza truth):

- script score 7 needs `S_sections ≥ 64` of 91 (`floor(10 × 64/91) = 7`)
- runtime score 7 needs `R_sections ≥ 65` of 92 (`floor(10 × 65/92) = 7`)

Current live numerators (56 / 63) are **below** those floors; both scores stay **6** until notes drop phantoms and/or add honest sections.

## Before → after (layer keys only)

| Term | Stanza **before** (declared) | Live **after** (computed) | Δ |
|---|---:|---:|---:|
| `S_members` | 114 | **91** | −23 |
| `S_sections` | 74 | **56** | −18 |
| `R_members` | 98 | **92** | −6 |
| `R_sections` | 69 | **63** | −6 |
| `coverage_script` | 6 | **6** | 0 |
| `coverage_runtime` | 7 | **6** | −1 |

## Exact replacement lines for `kumitate-proxy-v1`

Parent substitutes **only** these six body lines inside the existing `<!-- kumitate-proxy-v1 … -->` block (pins and non-layer terms untouched by this derivation):

```text
S_members=91
S_sections=56
R_members=92
R_sections=63
coverage_script=6
coverage_runtime=6
```

Full layer-relevant fragment as it should read after land (context only; parent owns the file):

```text
S_members=91
S_sections=56
R_members=92
R_sections=63
coverage_script=6
coverage_runtime=6
```

**Also required for `PROXY: MATCH` after land (out of this leaf's write scope, named for parent):**

1. `## Axes` row `| coverage:runtime-layer | 7 |` → **`6`** (else `AXES_DRIFT` remains even if stanza matches).
2. Prose measurements that still say `74/114` and `69/98` / runtime score 7 will be documentation drift relative to the machine block; parent decides whether to rewrite them in the same commit.
3. After census peers raise `S_sections`/`R_sections`, **re-run** this derivation — do not freeze 56/63 if notes change mid-round.
4. No pin re-hash required from this leaf (`proxy-check.mjs` / `claims-check.mjs` bytes not modified here).

## Member list derived (layer universe)

Not a family partition — the frozen **layer denominators** only:

- **S_members (91):** every `scripts/<name>.mjs` (73) + every file under `scripts/<dir>/` recursive (18)
- **R_members (92):** every `crates/ufo-core-runtime/src/<name>.rs` (88) + every `crates/ufo-cli/src/<name>.rs` (4)

Family-level membership re-census is owned by `S*MemberRecensus` / `R*MemberRecensus` peers; this leaf does not invent family members.

## Sections added/removed

**None by this leaf.** Observed live gate state only:

- Script in-family sections effective **74 → 56** because 18 section headings no longer resolve under `--src` (3 in S7, 15 in S8) and therefore never get `inFamily: true`.
- Runtime in-family sections effective **69 → 63** because 6 R11 headings no longer resolve (unresolved sections are not in-family). R9 still contributes 1 in-family + 3 out-of-family (unchanged exclusion rule).

## Unresolved blockers

- **Stanza land alone does not reach Planned falsifiable claim** (`coverage_script`/`coverage_runtime` each ≥ 7). Live ratios yield 6/6. Score-7 needs census peers to produce ≥64 S and ≥65 R honest in-family sections, then a second stanza re-derive.
- **CLAIMS: DRIFT remains** until phantom section headings are removed from notes (and/or live members sectionized). Stanza alignment fixes `PROXY` layer-term drift only.
- **AXES_DRIFT** on `coverage:runtime-layer` must flip with the stanza (row currently 7).
- Mid-round note edits by sibling recensus members will move `S_sections`/`R_sections`; parent must re-run `node scripts/proxy-check.mjs --json` immediately before commit.

## Cross-domain findings (owner)

| Finding | Owner |
|---|---|
| Origin tree membership shrink 114→91 / 98→92 since frozen stanza | origin/`ufo-fsd-alpha` restructure (recorded Planned); kumitate parent updates claims |
| Deleted origin members still headed in S7/S8/R11 notes | kumitate census peers + note authors |
| `membrane-seal write` argv defect | filed external; never absorbed (Planned halt) |
| R9 out-of-family sections still in note | historical; proxy correctly excludes; optional note hygiene |

## Retained evidence summary

| Source | Result |
|---|---|
| `node scripts/proxy-check.mjs --json` | `S_members=91 S_sections=56 R_members=92 R_sections=63 coverage_script=6 coverage_runtime=6` exit 1 DRIFT |
| `node scripts/claims-check.mjs --json` | inFamily Σ S=56 R=63; totals.sections=146 (raw); verdict DRIFT exit 1 |
| Origin `ls`/`find` | 73 + 18 = 91; 88 + 4 = 92 |
| Stanza before | 114 / 74 / 98 / 69 / 6 / 7 |

## Risk

Landing the six replacement lines without the Axes row edit leaves one `AXES_DRIFT`. Landing them while census is still rewriting notes freezes a transitional numerator. Prefer: census → claims MATCH (or measured residual) → proxy `--json` → stanza + Axes in one parent commit.

---

End advisory. No SCORECARD mutation. No commit.
