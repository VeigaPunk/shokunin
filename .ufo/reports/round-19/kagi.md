# round-19 — kagi · OMP-era freshness re-census

Lane: `kagi-shokunin`. Steered round: 19. Axis-move: freshness (one move).
Round-work commit: `5b0d4b784624a15506d3c85c77c3ae619e07467f` (lane identity `kagi-shokunin <kagi@shokunin.local>`).
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
- No implementation file changed: the scoped repair was measured as already present or unwarranted.

## Before → after measurements

`bash corpus/claim-ledger.sh citations` → exit 0 `CITATION_GATE: CLEAN (cites=912 docs=53 unresolved=0 ephemeral=0 labeled=13)`; `docs` → exit 0 `DOC_AUDIT: CLEAN (entries=21 row_linked=18 by_hand=3)`; seven selftests exit 0 (97/13/16/61/29/34 cases + transcript seeded-hit)

- Landing: No gate-default `$UFO_SRC`/`--src` derivation exists to repair; inventing one would add a resolver no caller consumes.

## SHONEN

- [~] SKILL craft present with cited sources — carried by the lane's existing skill; this round added no new decision table.
- [~] End-to-end domain task executed and logged — the round's task is the re-census measurement itself, logged in `LOG.md` + `corpus/lessons/round-19-recensus.md`.
- [~] Instructions executable without oral context — the lesson names each command and its observed verdict.
- [~] No cross-domain bleed — PROVINCE unchanged; cross-domain findings routed below.

No `[x]`: no named non-author verifier has yet signed these boxes. The audit wave
independently re-ran the gates and confirmed identity/pathspec/record conformance,
which is advisory evidence toward box 2–3, not a `[x]`.

## Carried debt (named, with unblock)

Substrate absence (11 deferred rows); stale SKILL counts 54/32/94 vs live 56/35/97; missing-file hash prefixes asserted as current; lowercase `~/projects/shokunin` strings; `<FILL ON STAMP>` never filled.

## Cross-domain routing

- Serving-plane ownership: kengaku → kama (kama owns endpoint identity).
- `membrane-seal write` argv defect: filed, not absorbed (owner: ufo runtime).
- Musketeer profile lease: kagi ↔ kake contested, integrator ruling owed.
