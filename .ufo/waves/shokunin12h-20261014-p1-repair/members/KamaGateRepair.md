# KamaGateRepair — advisory (wave shokunin12h-20261014-p1-repair)

Seat: `KamaGateRepair` (L2 leaf, gate-implementation only).  
Lane: `kama-shokunin` @ HEAD `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21` (matches `baselines.json`).  
Plan: `kama-shokunin/plans/wwkd-round-4-recensus.md`.  
Before receipt: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kama-before.json` (`consumers` exit 0).

## Verdict

**Measured unchanged — no gate implementation edit.**  
Round-3 already landed the `$UFO_SRC` / `--ufo-src` derivation. Re-measurement against the live tree finds no remaining root-default defect. Inventing a second repair would be fabrication.

## Gate registry (discovered)

| Artifact | Role | md5 / notes |
|---|---|---|
| `tools/kama-probe.sh` | sole runtime gate (`listeners` / `consumers` / `check` / `snapshot`) | `1f81e859c2d7f43f87d1f7e01327b2cf`, 1092 lines |
| `tools/test-snapshot.sh` | hermetic snapshot suite (24 cases) | `860f26ac05938cdfc1a8816eff1570b4` |
| `registry/endpoint-consumers.tsv` | 3 LIVE/LOADABLE rows; 2 cite `$UFO_SRC/…` | shape only for this seat |
| `SKILL.md` checklist | documents `--ufo-src` > `$UFO_SRC` env > first-existing candidates | docs out of GateRepair write scope |

No other gate scripts under `kama-shokunin/tools/`.

## Source-root resolution — measured

Implementation: `tools/kama-probe.sh:527-570` (`ufo_src`, `expand_path`) + CLI `parse_args` `:133-143`.

| Priority (contract) | Live behavior | Evidence |
|---|---|---|
| 1. Explicit `--ufo-src DIR` | Required; non-dir → `die` exit 1 (`--ufo-src is not a directory`) | `:141-142` |
| 2. `$UFO_SRC` env | Used only when non-empty **and** `[ -d ]`; bad/non-dir env does **not** stick — falls through | `:542-543` |
| 3. First existing candidate | `$HOME/Projects/ufo-fsd-alpha` then `$HOME/Projects/origin-work/ufo-fsd-alpha` | `:546-548` |
| 4. Fail-closed | Empty cache → `expand_path` returns `""` → `resolve_row` sets `file_match=missing` (never a guessed path) | `:559-560`, `:714-717` |

Host facts (this box, 2026-10-14):

- `test -d ~/Projects/ufo-fsd-alpha` → **yes** (relocated tree present).
- `test -d ~/Projects/origin-work/ufo-fsd-alpha` → **no**.
- `UFO_SRC` env → **unset**.
- Default `ufo_src()` offline replay → `/home/vgpnk/Projects/ufo-fsd-alpha`.
- Consumer targets exist: `config/the-tick.machine.json`, `scripts/local-helper.mjs`.
- Explicit bad flag path: `--ufo-src /nonexistent` fails closed at parse (not a silent default).
- Explicit bad env `UFO_SRC=/tmp/does-not-exist-ufo` falls through to first existing candidate (matches “$UFO_SRC → first existing → fail-closed”; only **flag** override stays hard-fail).

Hardcoded absolute `origin-work/` consumer paths: **absent** from gate code (only candidate list + comments). Registry rows already use `$UFO_SRC/…` (`endpoint-consumers.tsv:36-37`).

## Before-receipt alignment

`kama-before.json` ran `bash tools/kama-probe.sh consumers` → exit 0; stdout shows `ufo-fsd-thetick` / `ufo-fsd-local-helper` with `file_match=yes` and resolver URL pins at 34113 — consistent with default derivation hitting `~/Projects/ufo-fsd-alpha`. Endpoint verdicts `DEAD` are live-port absence (SCORECARD debt), not source-root failure.

## Code delta

**None.** GateRepair did not modify `tools/kama-probe.sh`, `tools/test-snapshot.sh`, registry, SCORECARD, LOG, or notes.

## Proposed delta (only if a future host falsifies)

None pending on this host. If both candidate trees vanish and no valid `$UFO_SRC`/`--ufo-src` is supplied, current fail-closed `file=missing` is the correct honest outcome — do not invent a third search path without a measured miss.

## Unresolved debt (not this seat)

| Debt | Owner / unblock |
|---|---|
| Positive-control rows `DEAD` (ports 34113/8080 refuse) | Operator: restore model unit or retire province; not a probe default bug |
| Eight deleted consumer files (already cut from registry; DELTA transitions recorded r3) | Historical; corpus errata only |
| Endpoint liveness ≠ source-root | kama domain runtime; GateRepair N/A |

## Cross-domain

- Origin tree layout / member claims under `ufo-fsd-alpha` → kumitate cite/claims gates (read-only here).
- Credential/session surfaces → kagi (shape-only; not opened).
- No kake `--src` overlap in this lane (kama flag is `--ufo-src`).

## Parent commands (post-integration; this seat did not run them)

From `kama-shokunin` root, preserve full stdout/stderr + exit + `git rev-parse HEAD`:

```bash
cd /home/vgpnk/Projects/shokunin/kama-shokunin
git rev-parse HEAD
bash tools/kama-probe.sh consumers; echo EXIT:$?
bash tools/kama-probe.sh check; echo EXIT:$?
bash tools/kama-probe.sh check --json; echo EXIT:$?
bash tools/kama-probe.sh listeners; echo EXIT:$?
# optional isolation (must not write default history if used only for proof):
# bash tools/kama-probe.sh snapshot --history /tmp/kama-wave-hist-$$ ; echo EXIT:$?
bash tools/test-snapshot.sh; echo EXIT:$?
bash -n tools/kama-probe.sh tools/test-snapshot.sh; echo EXIT:$?
# fail-closed override proof:
bash tools/kama-probe.sh consumers --ufo-src /nonexistent; echo EXIT:$?
# default derivation still reaches relocated tree (expect file_match=yes on ufo-fsd-*):
bash tools/kama-probe.sh consumers --ufo-src "$HOME/Projects/ufo-fsd-alpha"; echo EXIT:$?
```

Expect (unchanged shape vs r3 / before-receipt, ports still down): `consumers` exit 0 with 3 rows; `check` exit 2 (`drift=3`, `model_ok=0`); bad `--ufo-src` exit 1; `test-snapshot.sh` `RESULT pass=24 fail=0`.

## Axes touch (advisory only — not a lane round admission)

| Axis | This seat |
|---|---|
| freshness | Re-verified live derivation against relocated tree; no stale hardcoded root in gate |
| operability | Default bare invocation still resolves without flags on this host |
| calibration | Fail-closed explicit override preserved; no expectation re-pin |
| adjacency | No edits outside gate impl; no SCORECARD/LOG/notes mutation |

## Files changed

- **Lane implementation:** none  
- **This report only:** `.ufo/waves/shokunin12h-20261014-p1-repair/members/KamaGateRepair.md`
