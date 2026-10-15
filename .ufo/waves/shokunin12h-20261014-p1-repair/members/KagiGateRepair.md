# KagiGateRepair — advisory (wave shokunin12h-20261014-p1-repair)

Seat: `KagiGateRepair` (GateRepair leaf). Lane: `kagi-shokunin`. Round steered: **19**.  
Starting HEAD (baselines.json + live): `fecee8743e52eb8fb5fbb40782934cb619a1a96e`.  
Before receipt: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kagi-before.json`  
(`bash corpus/claim-ledger.sh citations` → exit **0**, `CITATION_GATE: CLEAN (cites=912 docs=53 unresolved=0 ephemeral=0 labeled=13)`).

This report is advisory data only — not a native judge verdict, lane round report, receipt, or admission.

## Axes in scope

freshness · operability · calibration · adjacency

## Gate registry (from SKILL / PROVINCE)

Discovered implementation files only (no SCORECARD/LOG/notes mutation):

| Gate | Path | SHA-256 (this tree) |
|---|---|---|
| surface census | `corpus/surface-census.sh` | `275d8294a94e9eb74caa72043607e9ff12a30414c2d6298a37cbd62ddb53009f` |
| drift pins | `corpus/drift-pins.sh` | `c138d34c7f0dfe950fce0e5e6672cc788b5ad080bc388d4aef118db0e6c70feb` |
| transcript scan | `corpus/transcript-scan.sh` | `2d60981b198cef41b9263a1427b41f92d98b65eb26ff71c28057bea0ad823a23` |
| op-ref probe | `corpus/op-ref-probe.sh` | `509f084ad33229db5b7421e1da948c02f9d191a6098f7a449341cf9adc95da1c` |
| checklist run | `corpus/checklist-run.sh` | `7e5ec98b9e1d0afaa4d4d0f0d91f897236e8a8b4c7912ccad94d86492fd576bf` |
| scope / adjacency | `corpus/scope-gate.sh` | `078a260184e25282096ef5f611b01ac1fb97deddb52d78facc1d551ff61f8082` |
| claim ledger | `corpus/claim-ledger.sh` | `93c5827202b9cdecd6874e75c5dac5281eeae07eddeeff3883bd0da14bfbcd29` |

SKILL decision-table command surfaces: `SKILL.md` rows for `surface-census.sh`, `scope-gate.sh`, `checklist-run.sh`, `op-ref-probe.sh`, `transcript-scan.sh`, `drift-pins.sh`, `claim-ledger.sh` (PROVINCE.md “Gates in this repo” mirrors the same seven).

## `--src` / source-root resolution — measured

### Established fleet pattern (sibling reference, not applied here)

kama `tools/kama-probe.sh:527-551` documents the authorized derivation:

1. explicit `--ufo-src` / flag override (fail closed if not a directory)
2. else `$UFO_SRC` env when it names an existing directory
3. else first existing of `~/Projects/ufo-fsd-alpha`, `~/Projects/origin-work/ufo-fsd-alpha`
4. else empty → consumer path resolves as missing (no silent guess)
5. explicit bad override stays bad

Host measurement this session:

- `DIR /home/vgpnk/Projects/ufo-fsd-alpha`
- `NODIR /home/vgpnk/Projects/origin-work/ufo-fsd-alpha`

### kagi gate inventory

Command evidence (repo root `kagi-shokunin`):

```text
rg -n 'UFO_SRC|--src|--ufo-src|origin-work|ufo-fsd' corpus/*.sh
# → no matches for UFO_SRC / --src / --ufo-src / origin-work / ufo-fsd
#    (only generic “resolve” wording in claim-ledger/scope-gate/checklist headers)
```

Broader tree (excluding historical lessons/LOG/SCORECARD/plans/README round-18 prose):

```text
rg -n 'origin-work|ufo-fsd|UFO_SRC|--src' \
  --glob '!corpus/lessons/round-18.md' --glob '!LOG.md' --glob '!SCORECARD.md' \
  --glob '!plans/*' --glob '!corpus/README.md' .
# sole live hit: corpus/knowledge/substrate-deferral.md:3 source-basis prose
#   ("OMP/ufo-fsd re-census") — not a path pin and not a gate default
```

Per-gate root defaults actually present:

| Gate | Root / path knobs | Default semantics |
|---|---|---|
| `surface-census.sh` | `--root` (default `$HOME`); `$STATE`/`$HOME` templates; `THE_JANITOR_BIN` | host home + janitor binary on PATH |
| `drift-pins.sh` | `$HOME` expand on `$HOME/...` baseline rows | host files under home |
| `transcript-scan.sh` | `--db` / `THE_JANITOR_STATE_DIR` → `~/.local/state/the-janitor/...` | janitor state DB |
| `op-ref-probe.sh` | `OP_REF_JANITOR_BIN` default `~/.local/bin/the-janitor` | janitor + `op` fixtures |
| `checklist-run.sh` | lane `ROOT=$(…/..)` + optional `--tsv`/`--skill` | in-repo only |
| `scope-gate.sh` | `--root`/`--basis-root`/`--lane-root` (`$HOME`, lane repo, sibling fleet root) | partition over census paths |
| `claim-ledger.sh` | `--root` (lane repo); `cite_target` classes: `corpus/*`, shorthand, sibling `*-shokunin/*`, `.ufo/*`/`ufo/*`, root docs (`claim-ledger.sh:442-467`) | **no** `$UFO_SRC` / origin-work class |

**Conclusion:** there is no gate-default `--src` / `$UFO_SRC` derivation in this lane to repair. Inventing one would add a non-consumer path resolver against a domain that censes the-janitor host surface, not ufo-fsd-alpha. Round-18 already closed this class as **vacuous** (`corpus/lessons/round-18.md:66-70`: stale `--src` failures **0**).

## Earlier repairs treated as existing state (not re-done)

Round-18 class-(d) lane defects already on HEAD `fecee874…`:

1. `surface-census.sh --selftest` substrate-absent skip for non-hermetic verb cases (still present in script).
2. `claim-ledger.sh` `substrate_present()` + `[substrate]` row `DEFER` + `KAGI_SUBSTRATE=present|absent` override (`claim-ledger.sh:138+`, selftest cases `defer-substrate-*` at `:1313-1315`).

No remaining falsified root-default defect reproduced against those paths for this GateRepair seat.

## Code delta

**None.** Gate implementation files unchanged. No SCORECARD/LOG/notes/expected-value edits (forbidden and unnecessary).

```text
git -C kagi-shokunin rev-parse HEAD  → fecee8743e52eb8fb5fbb40782934cb619a1a96e
git -C kagi-shokunin status -sb      → ## master...origin/master ; ?? plans/ only
```

## Proposed delta

*No gate-script implementation change this seat.*

1. **`--src` class:** still vacuous — do not invent `$UFO_SRC` resolution in kagi gates.
2. **Peer finding (`KagiScopeAudit`) — data/notes class, out of GateRepair write scope:**
   Over-broad `[substrate]` tags hide measurable DEFECT. Wave contract forbids changing persisted expected values / notes / SCORECARD / LOG, so this seat does **not** retag `claim-ledger.tsv`. Parent/record owner should consider a later reviewed data edit:

   | Row | Command | Why tag is wrong / partial |
   |---|---|---|
   | `R11-03` | `surface-census.sh --selftest` | Script already `skip-case` verbs when handler absent (`surface-census.sh:817-846`) and still prints `SELFTEST: PASS (16 cases)`; tag prevents verify from re-proving that fix |
   | `R16-01` | `scope-gate.sh` | Breadth/partition uses host dirs only (`scope-gate.sh:546-591`); no `the-janitor` binary |
   | `R17-01` | `scope-gate.sh --breadth` | same |
   | `R16-03` | `scope-gate.sh --falsify` | mostly scratch mutations; note itself admits partial live-count dependence — retag only after parent decides |
   | `R13-03` | `claim-ledger.sh cells` | meta audit; tag cascades deferral of the rows above |

   Keep tags on genuinely handler/state dependent rows: `R11-01`, `R11-02`, `R11-04`, `R11-06`, `R12-01`, `R15-01`.

   Any retag must also move `R18-02` expect `^11$` (tag-count pin) and refresh stamps — that is **RecordPrep / parent**, not GateRepair.

3. **`R18-01` note prose vs shape:** expectation `files_ok=0 files_bad=15` can still hold under mixed GONE+mode-DRIFT; note text “all-GONE” is imprecise. Live shape 2026-10-14 this session: `~/.config/opencode/opencode.json` **EXISTS mode=600** (baseline pin mode **644** in `drift-baseline.tsv`), so not pure missing. Do **not** edit the expect line here; parent may append errata later.

## Unresolved debt (named; not repaired here)

| Debt | Evidence | Unblock owner / action |
|---|---|---|
| Total janitor substrate absence | `ABSENT` `~/.local/bin/the-janitor`, `~/.config/the-janitor`, `~/.local/state/the-janitor`; `MISSING` `~/.agents/AGENTS.md` (parent dir `~/.agents` still present) | **operator / substrate install** |
| Over-broad `[substrate]` deferral | `claim-ledger.sh:138-144` + `claim-ledger.sh:397` defers on missing executable only; tags on `R11-03`/`R16-01`/`R17-01` (and `R13-03` cascade). Shape-only breadth 2026-10-14 (recount after ScopeAudit correction): `~/.config/opencode` **DIR children=3** (pin 20), `~/.local/bin` **DIR children=34** (pin 105), `~/.agents` **DIR mode=755 children=1** (pin 4; **not** NODIR — `AGENTS.md` alone is MISSING), chrome-profile **NODIR** (pin 53) — measurable DEFECT/drift if scope rows ran | **parent / RecordPrep** retag notes + `R18-02` count; **not** GateRepair (notes/expect forbidden this wave) |
| `R18-01` “all-GONE” prose vs mixed drift | `opencode.json` exists mode 600 vs pin 644; other pins still missing | **parent** errata on note; keep expect until re-measured under `verify` |
| Live gate DRIFT/DEFECT/SETUP | fail-closed readings; do not re-pin baselines to empty/partial host | **kagi** baselines stay historical record |
| CDP 9222 + musketeer profile contested | PROVINCE / adjacency | **integrator** + **kake** |
| Global `~/.config/opencode/opencode.json` ownership | adjacency `owner=integrator`; file present mode 600 | **integrator** ruling |
| Offline / secret-touching modes | op.env / session material | **named exclusion** on parent gate run |

## Cross-domain owner map

| Topic | Owner |
|---|---|
| Gate scripts + `substrate_present()` mechanism | **kagi** (implementation OK as written; detection = one exec bit per contract) |
| `[substrate]` row tags + `R18-02` count expect | **parent / RecordPrep** (data) — GateRepair blocked this wave |
| ufo-fsd-alpha checkout location | fleet/runtime (`~/Projects/ufo-fsd-alpha` live; origin-work copy gone) |
| the-janitor binary/config/state | operator substrate |
| musketeer chrome profile lease | **kake** |
| always-on `~/.agents/AGENTS.md` shape | **kotoba** (shared-read) |
| ScopeAudit corroboration source | peer `KagiScopeAudit` (report-only) |
| Wave integration, commits, SCORECARD/LOG append, parent gate execution | **Main / Sol 6.1 L1** |

## Parent must run (exact commands)

After integration (no worker gate runs this wave). From lane root:

```bash
cd /home/vgpnk/Projects/shokunin/kagi-shokunin
git rev-parse HEAD
git status -sb

# Calibration / citations (matches before-receipt argv)
bash corpus/claim-ledger.sh citations
bash corpus/claim-ledger.sh verify
# Expect DEFER lines for current [substrate] set while handler absent;
# after any approved retag, R16-01/R17-01/R11-03 should RUN and likely FAIL/DEFECT, not DEFER.
bash corpus/claim-ledger.sh cells
bash corpus/claim-ledger.sh docs
bash corpus/claim-ledger.sh --selftest

# Freshness / surface / adjacency (record full verdict lines even when red)
bash corpus/drift-pins.sh
bash corpus/drift-pins.sh --selftest
bash corpus/surface-census.sh
bash corpus/surface-census.sh --selftest
bash corpus/scope-gate.sh
bash corpus/scope-gate.sh --breadth
bash corpus/scope-gate.sh --selftest

# Operability
bash corpus/checklist-run.sh
bash corpus/checklist-run.sh --selftest
bash corpus/op-ref-probe.sh --selftest
bash corpus/op-ref-probe.sh || true

# Transcript: DB absent → SETUP/exit 2 expected; no credential content reads
bash corpus/transcript-scan.sh --selftest
bash corpus/transcript-scan.sh || true

# Explicit exclusions: no --deep surface verbs unattended; no content-read of
# credentials/, oauth/, server.token, op.env values, or session material.
```

Save full stdout/stderr, exit codes, and measured revision on each verdict line. Do not suppress red substrate DRIFT to force green. Do not retag or re-pin inside the gate-execution pass without a reviewed data commit.

## Verdict for this seat

**Measured unchanged (implementation).** No root-default `--src`/source-root defect; no GateRepair mutation of `corpus/*.sh`.

**Corroborated residual calibration debt (not fixed here):** `[substrate]` over-tags on measurable scope/selftest rows per `KagiScopeAudit` + shape-only host counts above. Fix is **data retag** (forbidden to this seat this wave), not a gate-default derivation repair.

