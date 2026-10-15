# round-4 — kama · OMP-era freshness re-census

Lane: `kama-shokunin`. Steered round: 4. Axis-move: freshness (one move).
Round-work commit: `84a81304d7b0c77c84fe495f3bb728e8729faaff` (lane identity `kama-shokunin <kama@shokunin.local>`).
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

- `corpus/lessons/round-4-recensus.md` — the round record (this report's lane-side counterpart).
- `LOG.md` — appended round entry.
- `SCORECARD.md` — appended move-log row.
- No implementation file changed: the scoped repair was measured as already present or unwarranted.

## Before → after measurements

`bash tools/kama-probe.sh consumers` → exit 0 (`$UFO_SRC` rows `file_match=yes`); `check` → exit 2 (DEAD, correct); `listeners` → exit 0; `bash tools/test-snapshot.sh` → `RESULT pass=24 fail=0`

- Landing: No repair warranted: the authorized root-derivation order is already implemented (`--ufo-src` → `$UFO_SRC` → first existing → fail-closed).

## SHONEN

- [~] SKILL craft present with cited sources — carried by the lane's existing skill; this round added no new decision table.
- [~] End-to-end domain task executed and logged — the round's task is the re-census measurement itself, logged in `LOG.md` + `corpus/lessons/round-4-recensus.md`.
- [~] Instructions executable without oral context — the lesson names each command and its observed verdict.
- [~] No cross-domain bleed — PROVINCE unchanged; cross-domain findings routed below.

No `[x]`: no named non-author verifier has yet signed these boxes. The audit wave
independently re-ran the gates and confirmed identity/pathspec/record conformance,
which is advisory evidence toward box 2–3, not a `[x]`.

## Carried debt (named, with unblock)

Dead endpoints (34113/8080; `qwen-coder.service` gone); `endpoint-identity.md` line refs drifted (`:481-487` vs real `:513-517`); province still owns deleted host pins.

## Cross-domain routing

- Serving-plane ownership: kengaku → kama (kama owns endpoint identity).
- `membrane-seal write` argv defect: filed, not absorbed (owner: ufo runtime).
- Musketeer profile lease: kagi ↔ kake contested, integrator ruling owed.
