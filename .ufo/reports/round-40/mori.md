# mori round 40 report — attempt 1 (resumed)

Lane: mori-shokunin. Entering tip `bb1f2457bb8d3e8d5dfe98488b91e8c02e378ca3`
(round 39 admitted, closure `corpus/lessons/round-39-verifier-spotcheck.md`).
Round tip: `ede486b7a09afbacfb380d5871c46a8051a6dc2e` (local=remote, ahead=0).
Instrument commit T1 `265a955cc67be4eae97d2dc5a9338a25f31eb29b`; evidence commit T2
`8d3badd0647c5dbfaf5f5a1443c5d4d5109a8d21`; registry-placement repair T3
`ede486b7a09afbacfb380d5871c46a8051a6dc2e`.

## Work performed

Declared claims (frozen in `.ufo/waves/round-40/contract.md`):

1. **C1 — operability (7): conformance checker v3** (scope-aware timeout
   resolution, per-Popen drain binding, own-table selftest conjunct) — r39 w1
   findings 4/8/12, closure routed defects 1–2.
2. **C2 — depth (5, tied lowest with calibration): append-only gate v3 (P-C11)**
   (eligible set = every superseded id present at R; edits measured against the
   first parent's own state only; re-add contributes no changed event) — r39 w1
   findings 2/5, closure routed defects 3–4.

- Resumed a dead launch: re-verified every inherited byte (gate v3 partial diff,
  conform v3 draft selftest at pass=9 fail=2, contract, fixtures), completed the
  unfinished work (gate selftest arms 12→15 with three new P-C11 DAG fixtures;
  dag-r redesigned so the re-add defect is visible; survivor fixtures regenerated
  from the counter of record). Evidence: `.ufo/waves/round-40/evidence/` (37
  receipts), lesson `corpus/lessons/round-40.md` M23.
- C1 evidence: before receipts run the r39 checker bytes extracted via
  `git show bb1f2457:` (`fixtures/extracted/conform-v2-r39.py`, sha
  fe0be179…); after receipts run the landed v3 at T1. `evidence/c10-*.txt`.
- C2 evidence: before receipts run the v2 gate bytes (`fixtures/extracted/
  gate-v2-bb1f2457.py`, sha 62cd4132…); after receipts run landed v3 at T1.
  `evidence/c11-*.txt`.
- Frontier: opened S229 (Python execution model §4.2.2, copy
  `corpus/evidence/sources-r40/S229.src`), knowledge entry
  `corpus/knowledge/conform-scope-r40.md` (grounds C1), lesson
  `corpus/lessons/round-40.md`, erratum `corpus/lessons/round-39-erratum.md`
  (S227 17-word label; C2 bypass-wait wording; stale r39 contract citations).
- Wave: one v2 wave spec prepared and validated — 66 seats, 32 attack (48.5%),
  `w1-spec.json` + `evidence/wave-plan.txt` (plan exit 0, one batched task
  call). **Prepared-but-undispatched under the accepted host mapping** (this
  seat has no dispatch tool; the orchestrator dispatches prepared waves between
  rounds — reported as the accepted mapping, not a conformance defect).
- Misroot sweep at the fleet root: no mori-authored stray files (only other
  lanes'/driver files, untouched).
- Inherited strays deleted: `count-c1-r38.py` (byte-size-exact extract of the
  committed `.ufo/waves/round-38/count-c1.py`), `bypass-none.py` /
  `bypass-wait.py` (in no commit; bytes unrecoverable, class recipes remain
  committed — honest disposition in the lesson).

## Landed changes

- T1 `265a955cc` — `tools/mori-sources-appendonly.py` (gate v3, P-C11),
  `.ufo/waves/round-40/{contract.md,count-c8.py,conform.py,fixtures/}`,
  `corpus/knowledge/conform-scope-r40.md`, `corpus/lessons/round-39-erratum.md`,
  `corpus/evidence/sources-r40/S229.src`, `corpus/SOURCES.md`, `SKILL.md`
  (conformance v3 + gate v3 registry rows). LOG.md entry "## Round 40".
- T2 `8d3badd0` — `.ufo/waves/round-40/evidence/` (37 receipts incl.
  census-start/end, freeze-r40, wave-plan), `w1-spec.json`,
  `gen-wave-spec.py`, `scratch/` drafts, `SCORECARD.md`, `LOG.md`,
  `corpus/lessons/round-40.md`.
- T3 `ede486b7` — `corpus/SOURCES.md` (S229 row moved inside ## Registry; T1's
  jj snapshot had captured the pre-move EOF position, caught by post-landing
  `git status`; census E12 is now clean at the tip), and
  `fixtures/generated/conform-v3-conjunct-gutted.py` (referenced by
  `c10-after-conjunct.txt`).

## Before → after measurements

- **C1** — before: `python3 fixtures/extracted/conform-v2-r39.py bb1f2457
  --counter <survivor>` → `CONFORM=met` exit 0 on nine survivors + the
  two-counter audit; conjunct-gutted r39 copy → `pass=8 fail=0`
  (`evidence/c10-red-*.txt`). After, measured at T1 `265a955cc`:
  `python3 .ufo/waves/round-40/conform.py 265a955cc67be4eae97d2dc5a9338a25f31eb29b`
  → `CONFORM=met` exit 0 (`c10-after.txt`);
  `… --selftest` → `CONFORM_SELFTEST pass=11 fail=0` (`c10-after-selftest.txt`);
  every survivor + multicounter → `CONFORM=unmet` exit 1 with the named check
  (`c10-after-{shadow-none,shadow-neg,cond,inf,divzero,decoy,underscore,
  second-popen,tuple,multicounter}.txt`); gutted v3 copy → `pass=0 fail=10`
  (`c10-after-conjunct.txt`). Counter parity: count-c7 vs count-c8 receipts
  byte-identical (`c10-parity.txt`).
- **C2** — before: `python3 fixtures/extracted/gate-v2-bb1f2457.py bb1f2457
  --repo .` → 18 as-of ids, S226 absent (`c11-before-lane.txt`); v2 on the new
  DAGs omits the never-edited superseded row / fabricates the merge edit +
  stale verdict (`c11-red-{neveredited,firstparent,readd}.txt`). After, measured
  at T1: `python3 tools/mori-sources-appendonly.py --selftest` →
  `pass=15 fail=0` (`c11-after-selftest.txt`); gate at T1 → **34** as-of ids
  incl. S226, `stale_supersede=[]` (`c11-after-lane.txt`); at `e37dcc6` →
  `stale_supersede=[S069]` (`c11-after-e37dcc6.txt`); dag-n/dag-p/dag-r →
  P-C11 verdicts (`c11-after-fixture-{n,p,r}.txt`). **Correction:** the
  contract/P-C11 parenthetical "(19 ids)" mis-predicted — the eligible-set
  extension admits 16 never-edited superseded rows (S226 plus 15 earlier);
  measured 34, corrected in SCORECARD and lesson M24.
- Kill-rule spot checks (do-nothing controls): the r39 checker on the
  round-40 survivors is the committed "met" control; the v2 gate on the
  round-40 DAGs is the committed wrong-verdicts control; a v3 with fewer
  selftest arms prints a different `pass=` than the frozen receipts.

## Sources & frontier

`SOURCES.md` rows 228 → 229 (+S229, tier A scoped to Python name-resolution for
static folds; opened 2026-10-24; copy `corpus/evidence/sources-r40/S229.src`;
15-word located quote in the round-40 lesson Gate). No existing row's
status/recheck/used-by changed in place. Rows touched: none old→new; S229
added (placement repaired at T3). Frontier rows advanced: S229 (opened+mined,
used-by `corpus/knowledge/conform-scope-r40.md`). Census:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin mori` → exit 0 at start and at end
(`evidence/census-start.txt`, `census-end.txt`; re-verified at the round tip,
exit 0); the 16 standing W04 duplicate-URL warnings are pre-existing fleet debt
(r39 closure routed defect 6, owning lane). Sourced claim: C1 rests on S229.

## Trend verdicts

- **expansion — improved**: +1 admitted tier-A row (S229), +1 knowledge entry
  (conform-scope-r40.md), +2 capability rows (conformance v3; ancestry
  supersede reading v3); no deletions or registry cell edits.
- **quality — improved**: every claim has committed red and after receipts
  naming command, measured rev and exit; both selftests re-derived at the
  landed tip (pass=11, pass=15); the two routed wording defects are corrected
  by an append-only erratum; counter parity proven byte-identical.
- **discernment — improved**: two mined mistakes (M23 inherited-unverified-freeze;
  M24 predicate parenthetical number-drift — caught by measurement, corrected
  by record); the dead launch's inherited bytes were re-verified before reuse
  and its uncommitted strays honestly disposed (one unrecoverable, recorded).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources — pointer: `SKILL.md` Gates registry rows for conformance v3 /
  gate v3 (added this round); no named non-author verifier in-round.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  pointer: LOG.md "## Round 40" (C1+C2 end-to-end with receipts).
- [ ] Instructions executable by an agent without oral context — the wave spec
  carries absolute-path bounds; not externally verified this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer:
  `corpus/lessons/round-39-erratum.md` + connector items W1/W2 in
  `w1-spec.json` (sibling-overlap scan prepared; no absorption: routed
  defects named to owning lanes).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs this round: none (curl fetch of S229 source copy only; no
package installs). L0 questions: none new (debt (f) SIGTERM/grace tradeoff
remains OPEN/operator-owned from round 37).
