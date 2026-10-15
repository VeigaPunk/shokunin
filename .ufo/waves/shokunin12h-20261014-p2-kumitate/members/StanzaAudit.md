# StanzaAudit — falsification of the round-32 stanza update

Leaf advisory only. Did not edit `SCORECARD.md`, notes, or gates. No lane bytes were mutated, so there is nothing to restore. This report is data, not a round verdict.

## Identity

| Field | Value |
|---|---|
| Member | `StanzaAudit` |
| Lane | `/home/vgpnk/Projects/shokunin/kumitate-shokunin` |
| Lane HEAD at final command | `ccd82e4476d3327a29930eae0176170fcf4824ab` |
| Dispatch lane HEAD | `175de6ba2e9e904010411b19cab27e0af9aad3d4` |
| Origin `--src` | `/home/vgpnk/Projects/ufo-fsd-alpha` |
| Origin HEAD | `964f443ee53df0ce06bd689af01f0dea031b01f9` |
| `$UFO_SRC` | unset; gate default is the first existing `SRC_CANDIDATES` entry (`scripts/proxy-check.mjs` `resolveSrcDefault`) |
| Stale origin path | `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha` absent |
| Contract | `kumitate-proxy-v1` |
| Final command window | `2026-10-15T00:29:57.904Z` probe, then `node scripts/proxy-check.mjs` on a clean `SCORECARD.md` + `corpus/knowledge` + `corpus/lessons` worktree |

## Files inspected

- `SCORECARD.md` — `<!-- kumitate-proxy-v1` block, `## Axes` integer cells, `## Planned` round-32 pre-registration, `## Retired` successor formulas
- `scripts/proxy-check.mjs` — `LAYER_PATTERNS` (317–320), `layerCoverage` (567–570), `layerTerms` (581–605), `compareAxes` (915–934)
- `scripts/claims-check.mjs` — `walkFiles` (`isFile` only; prunes `.git` `.ufo` `target` `node_modules`), `probeSections`, section push at 352–392 (`inFamily` is set only after a unique resolve; unresolved sections have no `inFamily` key; `SECTION_NO_ANCHOR` / `SECTION_DEAD_ANCHOR` do not clear `inFamily`)
- `corpus/knowledge/executable-scorecard.md` — term table (frozen 114/74/98/69 arithmetic; not re-measured there)
- `.ufo/waves/shokunin12h-20261014-p2-kumitate/members/StanzaDerivation.md` — the first proposed replacement lines
- `.ufo/waves/shokunin12h-20261014-p2-kumitate/evidence/kumitate-proxy-before.json` — wave-start gate snapshot

## What was proposed

Three successive writes of the same six keys. Only the last one is what the producing command returns.

| Snapshot | `S_members` | `S_sections` | `R_members` | `R_sections` | `coverage_script` | `coverage_runtime` | Where |
|---|---:|---:|---:|---:|---:|---:|---|
| Frozen at dispatch `175de6b` | 114 | 74 | 98 | 69 | 6 | 7 | stanza before round 32 |
| StanzaDerivation proposal, landed in `1a162a4` | 91 | 56 | 92 | 63 | 6 | 6 | `StanzaDerivation.md` lines 142–147; that report's own `--json` |
| Intermediate worktree write | 91 | 91 | 92 | 74 | 10 | 8 | uncommitted `SCORECARD.md` observed while notes were still landing; `node scripts/proxy-check.mjs --json` then printed `R_SECTIONS_DRIFT declared=74 computed=75` |
| Landed at final command `ccd82e4` | 91 | 91 | 92 | 75 | 10 | 8 | `git show HEAD:SCORECARD.md` and worktree, identical; `git status --short` on `SCORECARD.md` and `corpus/knowledge` + `corpus/lessons` empty |

`compareAxes` reads only the integer cell (`^\|\s*<axis>\s*\|\s*(\d+)\s*\|`). Those cells are now `coverage:script-layer` **10** and `coverage:runtime-layer` **8**. The evidence prose in the same cells was not rewritten: it still says ``floor(10 × 8/8 × 74/114) = 6`` and ``floor(10 × 11/11 × 69/98) = 7``. The gate does not read that prose.

## Commands that produce each changed term

Origin tree is read-only. `find -type f` and the gate's `e.isFile()` walk agree here: 0 symlinks under `scripts/`, runtime `src/`, and CLI `src/`; 0 `node_modules` / `target` / `.git` / `.ufo` under `scripts/`.

### `S_members` — command produces **91**. Stale hand-type produces **114** or **87**.

```text
$ find /home/vgpnk/Projects/ufo-fsd-alpha/scripts -maxdepth 1 -type f -name '*.mjs' | wc -l
73
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/scripts/*.mjs | wc -l
73
$ find /home/vgpnk/Projects/ufo-fsd-alpha/scripts -mindepth 2 -type f | wc -l
18
```

`LAYER_PATTERNS.S` is `^scripts/[^/]+\.mjs$` ∪ `^scripts/[^/]+/.+`. In-process filter over `probeSections().files`: 73 + 18 = **91**. `node scripts/proxy-check.mjs --json` `terms.S_members` = **91**.

Stale / hand-typed alternatives, same tree:

| Hand-type | Command | Value | What it does to the score if substituted |
|---|---|---:|---|
| Frozen stanza / `## Retired` prose | remembered `72 + 42` | **114** | `floor(10 × 91/114) = 7`, not the live 10 |
| Depth-1 trap (recorded in `## Limits`) | `find scripts -mindepth 2 -maxdepth 2 -type f \| wc -l` | **14**, so 73+14 = **87** | `floor(10 × 91/87) = 10` — the score does not move |
| `find -L` top-level `*.mjs` | follows symlinks | **73** | no change here; 0 symlinks |

The four files the depth-1 count drops (so 87 is not a recount of 91):

```text
scripts/charter-scribe/prompts/kimi-update.prompt.txt
scripts/charter-scribe/systemd/charter-scribe.service
scripts/charter-scribe/systemd/charter-scribe.timer
scripts/lean-cargo/bin/cargo-shim.sh
```

Recursive runtime `*.rs` is **not** a different number on this tree (`find crates/ufo-core-runtime/src -type f -name '*.rs'` = 88, same as `-maxdepth 1`). That trap is live in the rule and empty in the result.

Sorted member-list digests (`LC_ALL=C sort`, paths relative to origin):

- script layer sha256 `1395a6d5316c67f55a0e2f8efc5c3dfade840cc5d3b739cf25933219dc716f6a` (73 + 18 lines)
- runtime layer sha256 `7a0863ac95df43b9190afee9f623c53b6c21df1d1e43ab0d72a79303134d37d9` (88 + 4 lines)

### `R_members` — command produces **92**. Stale hand-type produces **98** or **93**.

```text
$ find /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src -maxdepth 1 -type f -name '*.rs' | wc -l
88
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/*.rs | wc -l
88
$ find /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src -maxdepth 1 -type f -name '*.rs' | wc -l
4
$ ls -1 /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src/*.rs | wc -l
4
```

CLI names: `main.rs`, `main_tests.rs`, `titanium.rs`, `titanium_tests.rs`. Gate filter: **92**. Frozen hand-type is 93+5 = **98**. Keeping the old CLI 5 with the live runtime 88 is **93**; `floor(10 × 75/93) = 8`, so that denominator error is invisible in the score and visible only as `R_MEMBERS_DRIFT`.

### `S_sections` — command produces **91**. Stale hand-types produce **74**, **56**, or **93**.

Producing rule, not a sum of family declared counts: `layerTerms` increments once per section with `inFamily === true` (`scripts/proxy-check.mjs:595`). Unresolved headings never get that flag.

In-process `probeSections` at `2026-10-15T00:29:57.904Z`, then the same numbers from `node scripts/proxy-check.mjs --json` in that process (`agreesWithProbe: true`), and again from the text gate on the clean tree:

| Row | raw headings | `inFamily === true` | excluded |
|---|---:|---:|---|
| S1 | 1 | 1 | |
| S2 | 8 | 7 | `scripts/ufo-mission-result.mjs` (`inFamily` false) |
| S3 | 2 | 2 | |
| S4 | 6 | 5 | 1 not-member |
| S5 | 2 | 2 | |
| S6 | 5 | 5 | |
| S7 | 6 | 6 | |
| S8 | 63 | 63 | |
| **Σ** | **93** | **91** | |

`1+7+2+5+2+5+6+63 = 91`. Distinct in-family files = 91 (no duplicate-section inflation on S). Live-anchor in-family = 91.

| Hand-type | Value | Score it produces at `S_members=91` |
|---|---:|---|
| Frozen numerator | 74 | `floor(10 × 74/91) = 8` |
| StanzaDerivation / `kumitate-proxy-before.json` / `1a162a4` | 56 | `floor(10 × 56/91) = 6` |
| Raw headings, including not-member | 93 | `floor(10 × 93/91) = 10` — score matches, term does not |
| Planned threshold written in as if measured | 64 | `floor(10 × 64/91) = 7` |
| One below that threshold | 63 | `floor(10 × 63/91) = 6` |

The 56 was a real command output when StanzaDerivation ran (their table: S6 5 + S7 6 + S8 45, S1–S5 at 0). It is not a command output after the note edits. Copying it forward is the hand-type.

### `R_sections` — command produces **75**. Stale hand-types produce **69**, **63**, **74**, **84**, or **67**.

Same rule. Probe row sum, agreed with `proxy-check --json` in the same process, and with the later text gate (`R=75/92`):

| Row | raw | `inFamily` | live anchor | excluded |
|---|---:|---:|---:|---|
| R1 | 8 | 8 | 8 | |
| R2 | 12 | 12 | 11 | `loop_driver.rs` is in-family with `anchors=0`, `live=false` — still counted |
| R3 | 2 | 2 | 2 | |
| R4 | 3 | 3 | 3 | |
| R5 | 0 | 0 | 0 | topic-form |
| R6 | 2 | 2 | 2 | |
| R7 | 0 | 0 | 0 | topic-form |
| R8 | 4 | 4 | 4 | |
| R9 | 4 | 1 | 1 | 3 `SECTION_FILE_NOT_MEMBER` |
| R10 | 2 | 2 | 2 | |
| R11 | 47 | 41 | 34 | 6 unresolved (no `inFamily`); 7 in-family dead anchors still counted |
| **Σ** | **84** | **75** | **67** | |

`8+12+2+3+0+2+0+4+1+2+41 = 75`.

The intermediate proposal `R_sections=74` is exactly `75 − 1`, dropping the one in-family section with `anchors === 0` (`crates/ufo-core-runtime/src/loop_driver.rs`). The proxy does not drop it. That write was killed:

```text
R_SECTIONS_DRIFT term=R_sections declared=74 computed=75 delta=+1
```

`coverage_runtime` did **not** drift on that write. `floor(10 × 74/92) = 8` and `floor(10 × 75/92) = 8`. 74 is the smallest integer that still scores 8 (`floor(10 × 73/92) = 7`). The off-by-one sat on the score boundary. The term detector sees it; the score detector does not.

| Hand-type | Value | Score at `R_members=92` |
|---|---:|---|
| Frozen numerator | 69 | `floor(10 × 69/92) = 7` |
| StanzaDerivation / proxy-before / `1a162a4` | 63 | `floor(10 × 63/92) = 6` |
| Exclude the no-anchor in-family section | 74 | `floor(10 × 74/92) = 8` — score matches, term drifts |
| Historical correction "raw minus R9's 3" | 84 − 3 = 81 | `floor(10 × 81/92) = 8` — score matches, term does not |
| Raw headings | 84 | `floor(10 × 84/92) = 9` |
| Live-anchor only | 67 | `floor(10 × 67/92) = 7` |
| Planned threshold written in as if measured | 65 | `floor(10 × 65/92) = 7` |
| One below that threshold | 64 | `floor(10 × 64/92) = 6` |

R9's three excluded files are still `loop_driver_tests.rs`, `local_ship_tests.rs`, `distill_tests.rs`. Subtracting only those three from today's raw 84 does not recover 75 or 69.

### `coverage_script` / `coverage_runtime` — the scores are the floor, not a target

Frozen function (`scripts/proxy-check.mjs:567-570`):

```text
coverage = floor(10 × C1_layer/C1_total_layer × sections/members)
```

A zero denominator scores 0. `C1s/C1s_total = 8/8`, `C1r/C1r_total = 11/11` (registry lines matching `^\| (S|R)\d+ \|`: exactly S1–S8 and R1–R11, all `covered`). The first factor is 1, so the live scores reduce to `floor(10 × sections/members)`.

`Math.floor(10 × (sections/members))` and integer `floor(10 × sections / members)` agreed on the live pair and on every alternative in the table above.

```text
coverage_script  = floor(10 × 8/8 × 91/91) = floor(10) = 10
coverage_runtime = floor(10 × 11/11 × 75/92) = floor(750/92) = floor(8.1521…) = 8
```

Gate text, clean tree, exit 0:

```text
PROXY: MATCH (A=6 C=11 operability=8; C1=19/19 C2=74/74 coverage=10; S=91/91 coverage:script-layer=10; R=75/92 coverage:runtime-layer=8; K=49/49 coverage:kimi-layer=10; pins=6 match)
```

Hand-typed scores that do **not** follow from the live ratio:

| Hand-type | Script | Runtime | Why it is not the derivation |
|---|---:|---:|---|
| Frozen stanza | 6 | 7 | `floor(10 × 74/114)=6`, `floor(10 × 69/98)=7` — old tree |
| StanzaDerivation proposal | 6 | 6 | follows from 56/91 and 63/92, which the command no longer returns |
| `## Axes` evidence prose, copied into the integer cell | 6 | 7 | same frozen ratios; the integer cells say 10 and 8; the gate does not parse the prose, so this residue survives `AXES_DRIFT` |
| Planned "at least 7" written as the score | 7 | 7 | `floor(10 × 64/91)=7` and `floor(10 × 65/92)=7` are thresholds, not measurements |
| Live-anchor numerator | 10 | 7 | `floor(10 × 67/92)=7`; the gate counts dead-anchor in-family sections |

`1a162a4` also set the runtime axis integer to 6 while leaving the prose at `= 7`. That integer matched the then-computed 6. It does not match a later ratio. The current integer 8 matches `floor(10 × 75/92)`. The prose beside it still does not.

## Detector

Expected detector: `node scripts/proxy-check.mjs` (exit 0 match, exit 1 naming `S_SECTIONS_DRIFT` / `R_SECTIONS_DRIFT` / `COVERAGE_*_DRIFT` / `AXES_DRIFT`).

| Mutant (hand-typed stanza) | Detector output | Killed? |
|---|---|---|
| Frozen 114/74/98/69/6/7 | wave-start and StanzaDerivation text: `S_MEMBERS_DRIFT -23`, `S_SECTIONS_DRIFT -18`, `R_MEMBERS_DRIFT -6`, `R_SECTIONS_DRIFT -6`, `COVERAGE_RUNTIME_DRIFT -1` | yes |
| StanzaDerivation 91/56/92/63/6/6, re-checked after note edits | later `--json`: `S_SECTIONS_DRIFT declared=56 computed=72` then computed 91; `R_SECTIONS_DRIFT declared=63 computed=74` then 75; scores moved 6/6 → 7/8 → 10/8 | yes, once notes moved |
| Intermediate 91/91/92/74/10/8 | `R_SECTIONS_DRIFT declared=74 computed=75 delta=+1`; no `COVERAGE_RUNTIME_DRIFT` | term killed, score survived |
| Landed `ccd82e4` 91/91/92/75/10/8 | `PROXY: MATCH` exit 0 | not killed at this snapshot |

Surviving mutant that is still on disk: the `## Axes` evidence formulas (`74/114 → 6`, `69/98 → 7`) next to integer cells 10 and 8. `compareAxes` cannot see them. A reader who copies the formula instead of the cell types the frozen scores.

`node scripts/claims-check.mjs` on the same tree is not a stanza detector and does not match:

```text
SUMMARY: errors=14 warnings=10
CLAIMS: DRIFT (SECTION_DEAD_ANCHOR row=R11 …; SECTION_FILE_UNRESOLVED row=R11 …; +8 more)
```

Those errors do not subtract from `R_sections`. That is why proxy can read MATCH while claims reads DRIFT.

## Member list derived

Layer denominators only. Not a family partition; family rows stay with the census peers.

- **S_members 91** = 73 `scripts/<name>.mjs` + 18 files under `scripts/<dir>/` (recursive). Depth-1 is 14, not an equivalent reading.
- **R_members 92** = 88 `crates/ufo-core-runtime/src/<name>.rs` + 4 `crates/ufo-cli/src/<name>.rs`.

## Sections added/removed

None by this leaf.

Observed numerator movement while other members edited notes (same commands, different times):

| When | `S_sections` | `R_sections` | scores |
|---|---:|---:|---|
| `kumitate-proxy-before.json` / StanzaDerivation | 56 | 63 | 6 / 6 |
| First in-process probe this leaf | 58 | 63 | 6 / 6 |
| Mid-wave `proxy-check --json` (stanza then still declared 56/63) | 72 | 74 | 7 / 8 |
| Probe at `2026-10-15T00:29:57.904Z` and final text gate | 91 | 75 | 10 / 8 |

A stanza line copied from any earlier row of that table is a hand-type relative to a later command.

## Unresolved blockers

- Section numerators are note-derived. This MATCH is against a clean worktree at `ccd82e4`. If a note lands after that commit, `S_sections` / `R_sections` move and the six lines must be re-derived; they must not be retyped from this file.
- `## Axes` evidence cells still cite 114/74 and 98/69 and scores 6 and 7. The integer cells and the stanza do not. Parent owns that prose; the gate will not fail it.
- `CLAIMS: DRIFT` remains (14 errors, 10 warnings), including R11 unresolved headings and dead anchors, and R2 `loop_driver.rs` with no own-file anchor. Those do not change the stanza terms. They do block a claims MATCH.
- R5 and R7 are still topic-form (0 in-family sections). The runtime score 8 is what 75/92 floors to, not a claim that every runtime family is sectionized.

## Cross-domain findings (owner)

| Finding | Owner |
|---|---|
| Origin membership 114→91 and 98→92 since the frozen stanza | origin tree `ufo-fsd-alpha` at `964f443e`; kumitate parent already wrote 91/92 |
| `R_sections=74` hand-count that drops `loop_driver.rs` because it has no anchor | whoever wrote the intermediate stanza; proxy counts `inFamily === true` regardless of `SECTION_NO_ANCHOR` |
| Axes prose still stating `floor(10 × 74/114)=6` and `floor(10 × 69/98)=7` beside integers 10 and 8 | kumitate parent (`compareAxes` will not catch it) |
| R11 dead anchors and six unresolved headings; R5/R7 still topic-form | census peers for those families; not a stanza-key defect |
| `membrane-seal write` argv defect | filed external; not absorbed |

## Retained command summary

| Command | Observed |
|---|---|
| `find`/`ls` origin membership | 73+18=91; 88+4=92; depth-1 nested=14 |
| `node scripts/proxy-check.mjs` at `ccd82e4`, clean notes | `PROXY: MATCH (… S=91/91 coverage:script-layer=10; R=75/92 coverage:runtime-layer=8; …)` exit 0 |
| `node scripts/claims-check.mjs` | `CLAIMS: DRIFT` exit 1; does not own the stanza keys |
| Ratio check | `floor(10 × 8/8 × 91/91)=10`; `floor(10 × 11/11 × 75/92)=8`; integer division agrees |
