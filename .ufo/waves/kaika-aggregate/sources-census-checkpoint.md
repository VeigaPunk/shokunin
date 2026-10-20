# Provisional SOURCES census checkpoint — not final

**Status:** provisional only. The exact `FINAL LANES READY` signal is still outstanding; audio and game-dev-2d have no registry in the original HEADs captured here. Do not copy these totals into the final round report or README. This checkpoint records a run with the corrected fleet-root script after it was activated in the original root, to preserve outputs while the two lane revisions remain in flight.

## Script and population identity

- Script: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`
- Fleet HEAD observed: `88b130fbd7b7430ac400b4b7498beeaec4bbabe9`
- Script blob: `55c886d1f67e41a84db2ac5a97fac591d1f14fe8`
- Script SHA-256: `a621fe0ec8a946430e4956353717c97a2029b9fa85b9a8721cf4f363e1beead7`
- `git status --porcelain -- scripts/sources-census.sh` → empty; exit 0.
- Input set: 21 explicit original directories `/home/vgpnk/Projects/shokunin/<id>-shokunin`, not `shokunin.conf` declarations and not lane worktrees. Each exact HEAD/blob binding and `corpus/SOURCES.md` path state was read before running; 19 files were present at HEAD and two were missing (`audio-shokunin`, `game-dev-2d-shokunin`). `kaidoku` and `kumitate` were already closed and fast-forwarded to their new originals.

## Commands and observed outputs

The four invocations used this common shape (with the same explicit 21-directory list appended in each case):

```sh
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh <census|validate|shared|overdue> \
  --root /home/vgpnk/Projects/shokunin --today 2026-10-19 \
  /home/vgpnk/Projects/shokunin/audio-shokunin \
  /home/vgpnk/Projects/shokunin/chousa-shokunin \
  /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin \
  /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin \
  /home/vgpnk/Projects/shokunin/kagi-shokunin \
  /home/vgpnk/Projects/shokunin/kaidoku-shokunin \
  /home/vgpnk/Projects/shokunin/kake-shokunin \
  /home/vgpnk/Projects/shokunin/kama-shokunin \
  /home/vgpnk/Projects/shokunin/kasegi-shokunin \
  /home/vgpnk/Projects/shokunin/kengaku-shokunin \
  /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  /home/vgpnk/Projects/shokunin/kotodama-shokunin \
  /home/vgpnk/Projects/shokunin/kumitate-shokunin \
  /home/vgpnk/Projects/shokunin/lore-shokunin \
  /home/vgpnk/Projects/shokunin/mado-shokunin \
  /home/vgpnk/Projects/shokunin/mori-shokunin \
  /home/vgpnk/Projects/shokunin/revenger-shokunin \
  /home/vgpnk/Projects/shokunin/souji-shokunin \
  /home/vgpnk/Projects/shokunin/tabi-shokunin \
  /home/vgpnk/Projects/shokunin/tameshi-shokunin \
  /home/vgpnk/Projects/shokunin/tsukuroi-shokunin
```

### `census` — exit 1 because registries are missing

```text
FLEET rows=530
FLEET tier.A=459 tier.B=30 tier.C=41 tier.invalid=0
FLEET status.queued=201 status.mined=283 status.rejected=46 status.invalid=0
FLEET missing=2
missing: audio-shokunin/corpus/SOURCES.md, game-dev-2d-shokunin/corpus/SOURCES.md
```

Per-lane `rows/tier A/B/C/status mined/queued/rejected` output was emitted for the 19 present files; see the immediate L1 tool transcript for the verbatim TSV. This is not the final lane set.

### `validate` — exit 2, not clean

- Two `missing` results cause exit 2; that exit is not a clean-validation result.
- No `E##` validation findings were emitted for the 19 present registry files.
- Warnings (non-failing by script contract): `W04` ×3 (`lore S017`, `lore S032`, `mado S030`) and `W01` ×1 (`lore S027`). They remain warnings, not errors, and are not promoted to an all-clear.

### `shared` — exit 2, because of the same two missing registries

```text
kubernetes.io/docs/concepts/workloads/pods/probes shared kama-shokunin,mori-shokunin
```

Only that shared URL was printed from the 19 present registries; the missing two were not counted.

### `overdue --today 2026-10-19` — exit 2, because of the same two missing registries

```text
cadence rows=511
  30d=2; 90d=99; 180d=85; 365d=70; 730d=10;
  on-release=236; on-change=5; on-commit=2; on-gate-change=1; every=1
overdue rows=0
```

Symbolic cadence rows are reported, not judged overdue. Zero ISO/`NNd` overdue rows is not proof that all sources are fresh.

## Exact limits / final rerun boundary

- These commands read working trees; they do not grade a frozen 21-commit archive. The per-file `HEAD` and `corpus/SOURCES.md` blob pins above bind this checkpoint only; rebind all 21 after `FINAL LANES READY` and run the corrected script against exact archive snapshots for final totals.
- No child file was edited. Audio's branch-only round-101 source registry was not substituted for its missing original-HEAD file; the same applies to game-dev-2d's in-flight registry.
- The source index/census checks table structure, permitted enums, dates/cadences, and `used-by` path existence. It does not establish that a URL/anchor was opened, that `teaches` is supported, that a `used-by` file actually cites the row ID, or that a Path is semantically sound. `SOURCES.md` cleanliness is separate from each lane's corpus-gate verdict.
- This checkpoint is not a final report or baseline and does not change the single R12 claim, numeric score, roster, or any child corpus.

## Per-lane census rows (same stdout, compacted)

The command emitted these exact lane totals for the 19 present files; two missing lanes emitted `missing` and contributed no rows.

| lane | rows | tier A | tier B | tier C | mined | queued | rejected |
|---|---:|---:|---:|---:|---:|---:|---:|
| chousa-shokunin | 18 | 14 | 1 | 3 | 8 | 7 | 3 |
| game-dev-3d-shokunin | 36 | 33 | 2 | 1 | 6 | 28 | 2 |
| kagi-shokunin | 16 | 14 | 0 | 2 | 14 | 1 | 1 |
| kaidoku-shokunin | 22 | 20 | 1 | 1 | 21 | 0 | 1 |
| kake-shokunin | 18 | 16 | 0 | 2 | 14 | 2 | 2 |
| kama-shokunin | 30 | 27 | 0 | 3 | 17 | 8 | 5 |
| kasegi-shokunin | 27 | 25 | 0 | 2 | 15 | 10 | 2 |
| kengaku-shokunin | 26 | 24 | 0 | 2 | 18 | 5 | 3 |
| kotoba-shokunin | 11 | 10 | 0 | 1 | 4 | 6 | 1 |
| kotodama-shokunin | 47 | 34 | 6 | 7 | 20 | 22 | 5 |
| kumitate-shokunin | 20 | 19 | 1 | 0 | 9 | 9 | 2 |
| lore-shokunin | 32 | 24 | 3 | 5 | 12 | 17 | 3 |
| mado-shokunin | 39 | 35 | 1 | 3 | 27 | 9 | 3 |
| mori-shokunin | 34 | 31 | 2 | 1 | 12 | 21 | 1 |
| revenger-shokunin | 15 | 14 | 0 | 1 | 12 | 1 | 2 |
| souji-shokunin | 33 | 29 | 3 | 1 | 16 | 15 | 2 |
| tabi-shokunin | 28 | 22 | 4 | 2 | 20 | 6 | 2 |
| tameshi-shokunin | 44 | 37 | 5 | 2 | 12 | 29 | 3 |
| tsukuroi-shokunin | 34 | 31 | 1 | 2 | 26 | 5 | 3 |
