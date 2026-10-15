# round-19 — kotoba · OMP-era freshness re-census

Lane: `kotoba-shokunin`. Steered round: 19. Axis-move: freshness (one move).
Round-work commit: `b0c7cb2e248bccf692cf10e4d3c394e09944e83d` (lane identity `kotoba-shokunin <kotoba@shokunin.local>`).
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
- `verifiers/verify_harness_claims.py` — the scoped comparator repair described below.

## Before → after measurements

`python3 verifiers/verify_corpus_integrity.py` → exit 0 9/9; `verify_surfaces.py` → exit 0; `verify_corpus_independent.py` → exit 0; `fault_injection_corpus.sh --self-test` → OK; `verify_harness_claims.py --self-test` → 0 failures/10 assertions

- Landing: `verify_harness_claims.py`: two permission CHECKS rows moved `at_least`→`equal` (expect stays 0) — the `at_least`+0 pair passed any non-negative count.

## SHONEN

- [~] SKILL craft present with cited sources — carried by the lane's existing skill; this round added no new decision table.
- [~] End-to-end domain task executed and logged — the round's task is the re-census measurement itself, logged in `LOG.md` + `corpus/lessons/round-19-recensus.md`.
- [~] Instructions executable without oral context — the lesson names each command and its observed verdict.
- [~] No cross-domain bleed — PROVINCE unchanged; cross-domain findings routed below.

No `[x]`: no named non-author verifier has yet signed these boxes. The audit wave
independently re-ran the gates and confirmed identity/pathspec/record conformance,
which is advisory evidence toward box 2–3, not a `[x]`.

## Carried debt (named, with unblock)

`verify_skill_checklist.py` exit 1 `trigger.line_budget 601>600` (pre-existing); stale v1 opencode model prose; lowercase `/home/vgpnk/projects/...` cites; baseline documentary mode strings stale.

## Cross-domain routing

- Serving-plane ownership: kengaku → kama (kama owns endpoint identity).
- `membrane-seal write` argv defect: filed, not absorbed (owner: ufo runtime).
- Musketeer profile lease: kagi ↔ kake contested, integrator ruling owed.
