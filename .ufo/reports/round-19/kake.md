# round-19 — kake · OMP-era freshness re-census

Lane: `kake-shokunin`. Steered round: 19. Axis-move: freshness (one move).
Round-work commit: `59948314e9af5dd6ef81894fc1c422b353f10938` (lane identity `kake-shokunin <kake@shokunin.local>`).
Wave: `Shokunin12hP1Repair20261014` (32 members) + independent audit wave
`Shokunin12hP1Audit20261014` (32 members). Sole L1: Sol 6.1.

## Work performed

- Full before-receipt captured per lane at the starting HEAD
  (`.ufo/waves/shokunin12h-20261014-p1-repair/evidence/<lane>-before.json`).
- Five disjoint scopes per lane: gate-default repair, citation triage,
  superseded-revision marking, live re-anchoring, record preparation — plus one
  baseline scope audit; two fleet-level seats (boundary connector, kagi secrecy
  sentinel). All advisory inventories:
  `.ufo/waves/shokunin12h-20261014-p1-repair/members/`.
- Parent executed the safe gate set after integration; full argv/exit/stdout in
  `.ufo/waves/shokunin12h-20261014-p1-repair/after-gates.json`.
- Independent audit re-ran gates, swept dead paths, checked historical marking,
  identity/pathspec and record conformance:
  `.ufo/waves/shokunin12h-20261014-p1-audit/members/`.

## Landed changes

- `corpus/lessons/round-19-recensus.md` — the round record (this report's lane-side counterpart).
- `LOG.md` — appended round entry.
- `SCORECARD.md` — appended move-log row.
- `scripts/freshness-sweep.mjs` — the scoped gate repair described below.

## Before → after measurements

`node scripts/freshness-sweep.mjs --selftest` → exit 0 **13/13**; `--offline` → exit 0 `VERDICT: OK (exit 0, partial: offline)`; explicit missing `KAKE_PROBE_HISTORY` → exit 2; no `$HOME/.kake-freshness-selftest-*` residue

- Landing: `pins.probeHistoryAbsent` now suspends ONLY the canonical default; explicit override stays fail-closed; `probeHistoryAbsent` joins the consumed-pin list; selftest fixture no longer cites a live project tree and leaves no persistent HOME state.

## SHONEN

- [~] SKILL craft present with cited sources — carried by the lane's existing skill; this round added no new decision table.
- [~] End-to-end domain task executed and logged — the round's task is the re-census measurement itself, logged in `LOG.md` + `corpus/lessons/round-19-recensus.md`.
- [~] Instructions executable without oral context — the lesson names each command and its observed verdict.
- [~] No cross-domain bleed — PROVINCE unchanged; cross-domain findings routed below.

No `[x]`: no named non-author verifier has yet signed these boxes. The audit wave
independently re-ran the gates and confirmed identity/pathspec/record conformance,
which is advisory evidence toward box 2–3, not a `[x]`.

## Carried debt (named, with unblock)

Bare online exit 1 stands (PQ-2/PQ-14 + suspended history); stale `SKILL.md:59`/`:111` webzites binaries; `freshness-sweep.md:43-53` pre-r18 pin literals; `SCORECARD.md:20` 14 children vs 30 measured.

## Cross-domain routing

- Serving-plane ownership: kengaku → kama (kama owns endpoint identity).
- `membrane-seal write` argv defect: filed, not absorbed (owner: ufo runtime).
- Musketeer profile lease: kagi ↔ kake contested, integrator ruling owed.
