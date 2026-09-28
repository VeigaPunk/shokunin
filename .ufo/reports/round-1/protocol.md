# Round 1 — protocol lane findings

Stress-tested PROTOCOL.md against the six child-repo seeds (all identical
boilerplate: stub SKILL.md, PROVINCE.md, SHONEN.md, one-line LOG.md, AGENTS.md).
Landed edits in commit `eac90ae` (PROTOCOL.md, ROADMAP.md only).

## Gaps found → fixes landed

### Unverifiable promotion gates
- "demonstrably performs", "real decision tables", "a reviewer can execute" —
  no verifier, no bar, no evidence definition. Any lane could self-check its
  own SHONEN.md boxes.
- **Fix:** new `## Promotion gates` section — verifier must not be the author
  (no self-attestation); named minimum artifacts (≥1 decision table, ≥1
  error-pattern list, ≥1 checklist, each with resolvable citation; ≥1 logged
  end-to-end task; PROVINCE.md still accurate); promotion mechanics defined
  (SHONEN.md deleted, MANIFEST.json rank updated, review recorded).

### Ambiguous round-robin aggregation
- "Full round" undefined — live case: round-1 wave (`.ufo/waves/round-1.json`)
  dispatches only 5 of 6 child lanes (kagi omitted). Old text made this either
  a non-round or an implicit no-op for kagi.
- "Lane report" referenced but never defined: no location, no required content.
- `MANIFEST.json` `rounds` entries had no schema — integrator would have to
  invent a shape each round.
- **Fix:** round completeness defined (every *dispatched* lane reported or
  recorded failed; undispatched shokunin = available scope, not participant);
  report path `.ufo/reports/round-<N>/<lane>.md` codified with minimum content;
  `rounds[]` entry schema given including per-lane `ok | failed |
  not-dispatched` status; mint evidence bar set (≥2 documented demand
  instances or explicit operator directive).

### Missing evidence requirements
- "Evidence-driven" was an assertion, not a standard; "end-to-end domain task"
  undefined.
- **Fix:** new `## Evidence standard` section — evidence = resolvable pointer
  (path, command output, commit, external doc); LOG.md entry without pointer
  is not evidence; end-to-end task = trigger → action → outcome → pointer.

### Missing invariants
- LOG.md mutability: "falsifiable deltas" are meaningless if history can be
  rewritten. **Fix:** append-only invariant.
- Rank canonicality: MANIFEST.json and ROADMAP.md both carry rank → drift.
  **Fix:** MANIFEST.json canonical, ROADMAP mirrors (noted in both files).
- Write-scope: nothing stopped a lane editing another child repo or
  MANIFEST.json. **Fix:** lanes write only in their own repo + lane report;
  integrator owns MANIFEST.json/PROTOCOL.md/ROADMAP.md.
- Contested scope: "one domain per shokunin" but no arbitration path when
  provinces overlap (e.g. kasegi credential-evidence vs kagi vault ops).
  **Fix:** report in lane report, integrator arbitrates via PROVINCE.md edits,
  ruling recorded in round notes.
- Meta-domain recursion: kotoba's domain *is* SKILL.md craft — could claim the
  protocol's own files. **Fix:** meta-domain documents patterns only; does not
  own protocol files or promotions.
- Lifecycle dead end: no dormancy/retirement path. **Fix:** dormant flag after
  two consecutive completed rounds without LOG.md activity; review trigger for
  operator, never automatic retirement.

## ROADMAP.md changes
- Phase gates given concrete exits tied to the new definitions.
- Canonical-rank note under roster table.
- Watchlist gated on the new minting-evidence bar.

## Open risks / next-round watch items
- SHONEN.md checklists in child repos are fixed text; if the bar evolves,
  seeded checklists drift from PROTOCOL.md. Consider deriving SHONEN.md from
  the protocol at mint time (integrator concern, not landed).
- Dormancy trigger counts "completed rounds" — depends on integrator honestly
  recording `failed`/`not-dispatched` lanes in `rounds[]`.
- `AGENTS.md` in child repos says "Never fabricate domain knowledge" but cites
  no standard; lanes should map it to the protocol's Evidence standard section.

## Scope compliance
- Edited: `PROTOCOL.md`, `ROADMAP.md` only. Commit `eac90ae` on main repo.
- Not touched: `MANIFEST.json`, child repos (read-only inspection only).
