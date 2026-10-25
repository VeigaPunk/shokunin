# Kasegi round 30

Round 30, attempt 1. Lane base `a94871315cafa368f79c17d8c62d71fddd967986`; freeze commit `3c5573541300ba0fd3d89372dda3d841172eaa3f`; wave dispatch commit `002e92ce07ed398334ef7cd8ca08d3fd99631351`; round work committed in `5703f9fbf70ba0717e5c6890f4c338cd5be00b7b`, final close-out commit `bc1a1e140914e65673daa586232128c964216ceb` (lane tip and pushed master). Claims frozen before data at `.ufo/waves/round-30/claims.json`.

## Work performed

Declared claims: **C1 depth:verifiability** (lowest owned non-retired axis, score 4 held) and **C2 coverage** (score 7 held), distinct axes and independent frozen predicates.

- C1 hardened `frontier-recheck-count.py` to name missing-entry rows and reject duplicate realpaths; hardened `source-recheck.py` to bind ID to capture stem and fail non-unique quotes without a verified anchor. Evidence: `.ufo/waves/round-30/c1-controls/before.txt`, `wave1/ExecImplFrontierHarness.md`, `wave1/ExecImplSourceRecheck.md`, `wave1/ExecMutantsC1.md`; implementation landed in `5703f9f`.
- C2 assimilated F14 “Japanese severity vocabulary and the handling-priority model” from the read-only `merge/kasegi/` package; opened/captured S046/S047 this round and reused S041. Evidence: `corpus/knowledge/japanese-severity-vocabulary-and-impact-model.md`, `corpus/source-snapshots/round-30/manifest.json`, `wave1/ExecCaptureAssim.md`; landed in `5703f9f`.
- Mined considerthese proposal 4 as `corpus/knowledge/considerthese-proposals-ledger.md`; evidence `wave1/ExecConsiderthese.md`; final corrected recheck form is in `bc1a1e1`.
- Curated source registry and frontier (SOURCES rows 45→47; F14 13→14); re-grounded rows are documented in `corpus/SOURCES.md:89-91`; F14 appendix in `corpus/README.md`.
- Mined mistakes M30-1…M30-5 in `corpus/lessons/round-30.md` §Mistakes; final-state errata follow in §Close-out erratum.
- Validated one v2 wave, `kasegi-r30-build`, 64 seats. Role composition from validated dispatch: scout 6, connector 4, executor 18, scribe 13, reviewer 11, critic 4, mutation-tester 4, sentinel 2, revenger 1, simplifier 1. m_flash-routed roles (executor/scribe/critic/sentinel/revenger/simplifier) = 39/64 (60.9%); attacks (reviewer/critic/mutation-tester) = 19/64 (29.7%). Planner was the L1's canonical seat; bounded data-walk rode `ScoutDatawalk`. Evidence: `.ufo/waves/round-30/wave1-spec.json`, `wave1-dispatch.json`, `wave1/swarm-registry.json`.
- Result aggregator `wave1-results.json` and `WAVE-DONE` were not present/received at close-out; therefore actual settled/dead-seat counts and answering model identities are **unavailable**, not inferred from dispatch. Seat report files are committed as wave evidence. No replacement seats were spawned.
- Tool installs/upgrades: none; no pacman transaction.

## Landed changes

- C1 instrument changes — tied to intended round-30 LOG entry, **not landed**: LOG append failed because `read` repeatedly returned stale tag `#B26C` while `edit` rejected the current file hash `#114E`; no LOG bytes changed. This is an explicit protocol conformance defect. Evidence: `corpus/lessons/round-30.md` §Close-out erratum. Changes themselves landed at `5703f9f`.
- C2 F14 admission, captures/manifest, registry/frontier, proposal ledger, and SCORECARD round result — tied to intended round-30 LOG entry, **not landed for the same editor hash inconsistency**; changes landed in `5703f9f` and `bc1a1e1`. SCORECARD appended the round results; no capabilities added.
- Final lesson, recheck repair, and post-commit receipt — `bc1a1e1`; `corpus/lessons/round-30.md`, `.ufo/waves/round-30/post-commit-recheck.sh`, `.ufo/waves/round-30/post-commit-recheck-output.txt`.

## Before → after measurements

**C1 — depth:verifiability, 4 held.** Frozen counters from `.ufo/waves/round-30/claims.json` and fixtures in `c1-controls/`:

- A1 missing entry: traceback/no F98 → named `FAIL F98 … problems=missing-entry`, exit 1.
- A2 duplicate target: pass=2/exit 0 → `DUPLICATE-ENTRY F98,F97`, exit 1.
- B1 ID/stem mismatch: exit 0 → `reason=stem-mismatch`, exit 1.
- B2 repeated quote: exit 0 → frozen fixture exit 1, but its mismatched stem causes B1 to fire first. B2 itself is isolated by `source-recheck.py --selftest` and a same-stem repeated-quote fixture (live exit 1 `occurrence-not-unique`; mutant exit 0). This is the disclosed frozen-fixture discrimination gap, not hidden as a clean B2 counter.
- `python3 corpus/instruments/source-recheck.py --selftest` → `selftest cases=9 failures=0`, exit 0. Real frontier harness: before 16/16 → after 17/17 (F14 now exists).
- Do-nothing/freeze controls miss the target on all four limbs; four mutations were tested. Evidence: `c1-controls/before.txt`, `before-run-2.txt`, `wave1/ExecMutantsC1.md`, `wave1/CritC1Kill.md`.

**C2 — coverage, 7 held.** Frozen counters in `claims.json`; before receipt `c2-controls/before.txt`; final measurement at lane commit `bc1a1e1` via `.ufo/waves/round-30/post-commit-recheck-output.txt`:

- Frontier admitted: 13 → 14.
- Knowledge entries citing S046/S047: 0 → 1 (F14 entry).
- S046/S047 registry rows: 0 → 2; total SOURCES rows: 45 → 47.
- Sources census: exit 0 → exit 0; W04 duplicate-URL warnings S028/S029 are unchanged.
- Frontier harness: 16/16 → 17/17, exit 0; F14 binds S041/S046/S047.
- Round-30 source-recheck for S046/S047/S041: no round-30 manifest → all exit 0 on manifest with verified anchors for the two repeated S047 quotes.
- Ancillary knowledge recheck audit: after proposal-ledger recheck fix, `python3 corpus/instruments/recheck-audit.py --quiet` → `strict pass=43/43`, `executes=19 gated=24 broken=0`, `expect=present expected=43 missing=0 unexpected=0 exit=0`.

## Sources & frontier

`corpus/SOURCES.md`: 45 → 47 rows; added tier A/mined S046 and S047; no existing row cells touched. Changelog says staged IDs S049→S046 and S050→S047 by document, not arithmetic. Census command (run at round start and end): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`; before output/exit in `.ufo/waves/round-30/census-before.txt` (45 rows, exit 0), final output/exit in post-commit receipt (47 rows, exit 0). Frontier advanced 13/13→14/14 with F14. Assimilation: one matching merge theme admitted; proposal 4 mined from `considerthese/2026-10-25.md`. Quarantine slice: seven rows hand-checked, none appended; outcomes in `corpus/lessons/round-30.md` §Gate and `wave1/ScribeQuarantine.md`.

## Trend verdicts

- **expansion: improved** — F14 adds one admitted knowledge entry on new frontier ground with newly opened/mined rows S046/S047; frontier 13→14.
- **quality: improved** — F14 source rechecks and all 17 admitted-frontier rechecks pass; census clean; the two instruments close the M29-3/M29-4 failures. The B2 fixture isolation caveat is disclosed and does not erase the exercised B2 fix.
- **discernment: unchanged** — non-author `RevC2Entry` agrees with F14 admission; `RevQuarantineInd` disagrees with S037's prior ABSENT label and qualifies S054's. These disagreements are recorded, but no new QUALITY criterion was landed to convert them into a discernment improvement. Evidence: `wave1/RevC2Entry.md`, `wave1/RevQuarantineInd.md`, lesson §Close-out erratum.

No scalar axis increase is claimed, and no owned axis is claimed harmed. No-harm reviewer noted that independent final PROVINCE comparison was not complete; see `wave1/RevNoHarm.md` and lesson §Census, density, and no-harm.

## SHONEN

- `[~]` SKILL decision tables/patterns/checklists — existing evidence `corpus/instruments/density.py SKILL.md`; round-30 gate row appended in SKILL.md (density/anchorcheck evidence in `wave1/ScribeSkillGate.md`).
- `[~]` End-to-end domain task logged — prior round-25 task evidence at `LOG.md` round 25 and `.ufo/reports/round-25/kasegi.md`; round-30 LOG append is blocked as disclosed above.
- `[~]` Instructions executable without oral context — `recheck-audit.py` final 43/43 strict pass; `frontier-recheck-count.py` 17/17; `wave1/ExecSelftestProbe.md`.
- `[~]` No cross-domain bleed / PROVINCE accurate — `PROVINCE.md`; `wave1/ScoutAdjacency.md`; final independent no-harm comparison remains incomplete.

**Stale-lane:** No separate open mission; this report closes the dispatched round. **Tool installs:** none. **L0 questions:** none opened.
