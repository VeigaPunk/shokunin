# kagi — round 17 (coverage 8 → 9)

Lane: kagi (secrets & vault ops). Repo:
`/home/vgpnk/Projects/shokunin/kagi-shokunin`, commit `bc1af88`
(`round-17`), pushed to `VeigaPunk/kagi-shokunin`.

Axis moved: **coverage**. At the round-16 close depth and coverage were tied at
8; operability, freshness, calibration and adjacency stood at 9. Coverage had
the concrete, vault-free defect: four shared leaf directories contained 182
direct children, but the census represented only 8 of them and no gate checked
the remaining breadth. A new or removed unknown child left every shipped gate
green. Depth's next increment remained bounded by the no-vault-contact refusal,
so coverage was the Pareto move: measurable, reversible, privacy-preserving and
inside the existing ownership gate.

## Before → after

| Surface | Before (`8a6ec16`) | After (`bc1af88`) |
|---|---|---|
| Breadth declarations | `grep -cE '^# breadth…'` = 0; four ratios existed only in round-16 prose | 4 exact `# breadth` rows, one for every derived leaf `# no-enumerate` boundary |
| Completeness | deleting every breadth declaration was vacuously clean | required membership is derived independently; missing/extra/aggregate/out-of-scope pins fail |
| Live breadth | unknown children were invisible | `children=182 declared=8 undeclared=174`, checked on every default verify |
| Per-directory values | prose: 20/4, 105/2, 4/1, 53/1 | `--breadth` emits the same four count-only rows and an exact member-set line |
| Drift | add/remove an unknown child: no verdict | `BREADTH-CHILDREN-DRIFT`; declared-count movement has distinct `DECLARED-DRIFT` / `EXCEEDS` verdicts |
| Privacy | no mechanism | counts only; no child names, contents, hashes or recursive traversal |
| Gate proof | 43 selftest cases; 9 shipped-data mutations | 61 selftest cases; 18/18 shipped-data mutations caught |
| Axis score | coverage 8 | coverage 9; count-vs-identity and recursion ceilings remain explicit |

The committed pre/post measurement is independently visible as
`before_breadth=0`, `after_breadth=4` from `git show
8a6ec16:corpus/adjacency.tsv` versus the shipped file.

## What landed

- `corpus/adjacency.tsv`: strict four-field grammar
  `# breadth<TAB><dir><TAB>children=N<TAB>declared=M`; four leaf pins.
- `corpus/scope-gate.sh`: `--breadth`, R12/R13 breadth validation, derived
  membership, direct-child counting, census-derived declared counts, summary
  counters, 18 new selftest cases and 9 new mutations.
- Breadth verdicts: `BAD-ROW`, `BREADTH-INVALID`, `BREADTH-MISSING`,
  `BREADTH-NOENUM`, `BREADTH-SCOPE`, `BREADTH-UNVERIFIED`,
  `BREADTH-CHILDREN-DRIFT`, `BREADTH-DECLARED-DRIFT`, and
  `BREADTH-EXCEEDS`; `$HOME` itself is refused.
- `corpus/knowledge/adjacency-breadth.md`: grammar, derivation, privacy choice,
  verdict/exit table, 13 bounds, reproduction and mutation map.
- `corpus/knowledge/adjacency-scope.md`: v2 integration and corrected D-96
  attribution.
- `corpus/lessons/round-17.md`: before/after, defects, L2 dispositions, limits.
- Ledger rows `R17-01..03`; exact guards updated to 54 stamps, 32 claims, 20
  knowledge entries / 17 row-linked entries.
- `SKILL.md`, `PROVINCE.md`, `corpus/README.md`, `SCORECARD.md`, and `LOG.md`
  updated to the shipped contract and measured counts.

`declared` means distinct direct children that either are census rows or contain
at least one census row. Descendants under the same child bucket count once.
Required pins are not declared by the pins themselves: they are derived from
leaf `# no-enumerate` boundaries after excluding aggregate ancestors. This
selects exactly:

1. `$HOME/.config/opencode` — 20 / 4 / 16
2. `$HOME/.local/bin` — 105 / 2 / 103
3. `$HOME/.agents` — 4 / 1 / 3
4. `$HOME/.local/share/the-musketeer/chrome-profile` — 53 / 1 / 52

The aggregate roots `$HOME/.config`, `$HOME/.local/state`,
`$HOME/.local/share`, and `$HOME/.local/share/the-musketeer` are deliberately
exempt; pinning them is `BREADTH-SCOPE`.

## Evidence — shipped revision

```text
$ bash corpus/scope-gate.sh
BREADTH_AUDIT: CLEAN (required=4 pins=4 checked=4 ok=4 children=182 declared=8 undeclared=174 missing=0 invalid=0 drift=0 exceeds=0 unverified=0)
ADJACENCY_ABSTAIN: rows=1
ADJACENCY_SCOPE: CLEAN (census=35 owned=27 shared=8 groups=4 owners=4 unresolved=1 contested=1 escapes=0 inbound=0 foreign=0 orphans=0 stale_basis=0 basis_escape=0 own_unlisted=0 breadth_required=4 breadth_pins=4 breadth_checked=4 breadth_ok=4 breadth_missing=0 breadth_invalid=0 breadth_drift=0 breadth_exceeds=0 breadth_unverified=0)

$ bash corpus/scope-gate.sh --breadth
ADJACENCY_BREADTH: dir=$HOME/.config/opencode children=20 declared=4 undeclared=16
ADJACENCY_BREADTH: dir=$HOME/.local/bin children=105 declared=2 undeclared=103
ADJACENCY_BREADTH: dir=$HOME/.agents children=4 declared=1 undeclared=3
ADJACENCY_BREADTH: dir=$HOME/.local/share/the-musketeer/chrome-profile children=53 declared=1 undeclared=52
ADJACENCY_BREADTH_SET: dirs=$HOME/.agents,$HOME/.config/opencode,$HOME/.local/bin,$HOME/.local/share/the-musketeer/chrome-profile
BREADTH_AUDIT: CLEAN (required=4 pins=4 checked=4 ok=4 children=182 declared=8 undeclared=174 missing=0 invalid=0 drift=0 exceeds=0 unverified=0)

$ bash corpus/scope-gate.sh --selftest
SCOPE_SELFTEST: PASS (61 cases)

$ bash corpus/scope-gate.sh --falsify
SCOPE_FALSIFY: PASS (caught=18/18 failed=0)

$ bash corpus/claim-ledger.sh verify
CLAIM_LEDGER: CLEAN (claims=32 stamped=54 ids=32 cited=32 labeled_ids=17 orphans=0)

$ bash corpus/claim-ledger.sh cells
CELL_AUDIT: CLEAN (cells=108 row_pointed=64 stamp_pointed=64 uncited=0 missing_ids=0 rows_run=28 row_failures=0 stale_pointers=0 self_skipped=4 orphans=0)

$ bash corpus/claim-ledger.sh docs
DOC_AUDIT: CLEAN (entries=20 row_linked=17 by_hand=3 undeclared=0 missing_ids=0 unpinned=0 duplicate_reasons=0)

$ bash corpus/claim-ledger.sh citations
CITATION_GATE: CLEAN (cites=891 docs=51 unresolved=0 ephemeral=0 labeled=13)

$ bash corpus/drift-pins.sh
DRIFT_PINS: CLEAN (files=15 symbols=20)

$ bash corpus/surface-census.sh
SURFACE_CENSUS: CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0)

$ bash corpus/checklist-run.sh
CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6
CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)
```

`git diff --check` and `bash -n corpus/scope-gate.sh` also returned zero.

## Failure proof

The 18 shipped-data mutations include the original nine partition mutations and
nine breadth mutations. Every breadth mutation returned exit 1 with the named
verdict:

- remove a required pin → `BREADTH-MISSING`;
- change the live-child pin → `BREADTH-CHILDREN-DRIFT`;
- pin fewer/more declared children → `BREADTH-EXCEEDS` /
  `BREADTH-DECLARED-DRIFT`;
- set declared greater than children → `BREADTH-INVALID`;
- pin an aggregate root → `BREADTH-SCOPE`;
- pin a directory lacking `# no-enumerate` → `BREADTH-NOENUM`;
- add a fifth field → `BAD-ROW`;
- add `# no-enumerate $HOME` → whole-HOME refusal;
- add a newly census-declared direct child without moving the pin →
  `BREADTH-EXCEEDS`.

All fixtures are `mktemp` copies. The repo and host are not mutated.

## L2 wave

The required dispatch happened as one eight-task batch: scout, critic,
sentinel, mutation-tester, connector, executor, reviewer, and scribe. A planner
was dispatched separately first, making nine L2 participants total. Every lane
was scratch/read-only; no vault, handler, Chrome, `op`, `op.env`, secret or host
state was touched.

| Lane | Evidence/result | Disposition |
|---|---|---|
| planner | exact four-field grammar; derived leaf-membership rule; strict arithmetic and host-root verdicts | core grammar and derived completeness landed |
| scout | independently measured all eight no-enumerate roots; confirmed the four selected ratios; documented dotfile, whitespace, dangling-symlink and volatility hazards | four selected ratios landed; aggregate measurements retained as evidence, not pins |
| critic | proved opt-in pins could all be deleted; proved same-cardinality swaps pass; challenged hard-failing volatile foreign churn | completeness and identity bound landed; hard-fail retained as an intentional reviewed drift signal |
| sentinel | demonstrated name-manifest disclosure, forged newline output, pipeline error masking, root-symlink and hostile-name hazards | count-only output, strict arity, fail-closed enumeration and no names landed |
| mutation-tester | 18 breadth mutation designs across membership, schema, arithmetic and count directions | nine independent shipped-data mutations plus 18 selftest additions landed |
| connector | found no sibling host-breadth duplicate; falsified the D-96 attribution | overlap reported; D-96 corrected—its row concerns sibling skill discovery, not opencode ownership |
| executor | scratch implementation plus 28-case fixture | parser/counting/test shape reused; opt-in completeness and neutral missing-root behavior rejected |
| reviewer | confirmed all eight baselines and aggregate/whole-HOME counterexamples | four leaf pins and aggregate/root refusals landed |
| scribe | report/knowledge/scorecard structures; highlighted the two possible meanings of `declared` | structure reused; wording fixed to direct census-linked child buckets |

## Defects found while landing

1. Old selftest fixtures had no breadth rows, so seven previously clean cases
   failed under derived completeness. Fixtures now carry exact pins.
2. The asset-absent fixture removed a census child but retained the old declared
   pin. Its count now moves with the fixture.
3. A diagnostic host probe twice timed out because it combined enumeration with
   a per-child text search. Isolated direct-child counting completed in ~0.01 s;
   the shipped gate only counts and compares in-memory census paths.
4. The final corpus audit caught two stale exact-count rows introduced by the
   round: 52→54 stamps and 19/16→20/17 knowledge entries/row-linked. Both were
   corrected before the final clean ledger run.
5. The connector showed that round 16's D-96 attribution was false. The current
   knowledge entry states the actual fact; `$HOME/.config/opencode` ownership
   remains unresolved rather than being papered over.

## Calibration, bounds and hygiene

Coverage moves to 9, not 10:

- count-only pins detect cardinality drift, not same-cardinality name swaps;
- 174 direct children remain deliberately unnamed and unclaimed;
- direct-child counts do not inspect recursive descendants or contents;
- a census row is evidence of declared coverage, not proof that the handler
  reads the path or that a foreign owner claim is true;
- Chrome-profile and shared-bin churn can make the gate red; re-pinning requires
  inspection and is never automatic;
- ownership truth and the `$HOME/.config/opencode` ruling remain outside this
  gate.

No child names are printed or committed. The gate does not follow child
symlinks, open files, read vault references, start/stop the handler, launch
Chrome, contact 1Password, or change host state.

## Routing/fallback observation

Effective OMP config maps `m_swe` to `devin/swe-2:max`. The inspected
`retry.fallbackChains.m_swe` value is null, so the requested
`m_swe → openai-codex/gpt-daybreak-blue-latest:max` hop was **not visible**.
No genuine `m_swe` capacity failure occurred, so no fallback advancement was
observed. No config or frozen mission contract was changed.

## Adjacency

No sibling lane implements this host-directory breadth contract. Nearby sibling
mechanisms inventory skill roots or compare docs/source and therefore do not
duplicate Kagi's unit. The opencode ownership question remains reported to the
integrator. No upstream/domain-source tree was edited or pushed.

## Next target

Depth is now the sole lowest score at 8; all other axes stand at 9. Round 18
should re-measure the standing vault-refusal ceiling using only generated
plain-value fixtures or error classification. A move is valid only if it finds
an `op.env` consumption behavior not already covered by
`corpus/knowledge/op-ref-consumption.md`; otherwise record the exact negative
probe and leave depth unchanged. Ref-resolved masking, `op read`, `op inject`,
item paths and secret values remain refused.
