# round-20 — kasegi · OMP-era freshness re-census

Lane: `kasegi-shokunin`. Steered round: 20. Axis-move: freshness (one move).
Round-work commit: `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` (lane identity `kasegi-shokunin <kasegi@shokunin.local>`).
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

- `corpus/lessons/round-20-recensus.md` — the round record (this report's lane-side counterpart).
- `LOG.md` — appended round entry.
- `SCORECARD.md` — appended move-log row.
- No implementation file changed: the scoped repair was measured as already present or unwarranted.

## Before → after measurements

`python3 corpus/instruments/anchorcheck.py SKILL.md` → exit 0 `7 in-range / 0 bad / LOST-RECORDED=306 / PIN-BROKEN=0 / OUTSIDE-BASE=0 / BASE-ABSENT=0`; `density.py` → 645 instances; `resolve.py .` → regenerated census

- Landing: No gate change: both instruments already derive `$KASEGI_MIRROR`/`$KASEGI_ORIGIN_ROOT` with explicit-bad retained.

## SHONEN

- [~] SKILL craft present with cited sources — carried by the lane's existing skill; this round added no new decision table.
- [~] End-to-end domain task executed and logged — the round's task is the re-census measurement itself, logged in `LOG.md` + `corpus/lessons/round-20-recensus.md`.
- [~] Instructions executable without oral context — the lesson names each command and its observed verdict.
- [~] No cross-domain bleed — PROVINCE unchanged; cross-domain findings routed below.

No `[x]`: no named non-author verifier has yet signed these boxes. The audit wave
independently re-ran the gates and confirmed identity/pathspec/record conformance,
which is advisory evidence toward box 2–3, not a `[x]`.

## Carried debt (named, with unblock)

Six new debt ids + three standing losses; the 50-deletion sentence does not reproduce (reachable history is an orphan 3-commit line; cross-history diff = 970); scorecard rates 116/1142,132/1469 vs census 116/1144,132/1471.

## Cross-domain routing

- Serving-plane ownership: kengaku → kama (kama owns endpoint identity).
- `membrane-seal write` argv defect: filed, not absorbed (owner: ufo runtime).
- Musketeer profile lease: kagi ↔ kake contested, integrator ruling owed.
