# Mori — round 59, attempt 2

## Work performed

C1 targeted **calibration**: a frozen counter plus a pinned tool
(`tools/mori-register-check.py`, sha256 `38b733d8…472b8`) that verifies the two round-56 rows in
the unique self-declaring `## Capabilities` register — exact row keys/names, evidence-pointer
existence and materialized equality, MANIFEST `rounds[832]` binding at fleet `2807c6ab` — against
13 committed hostile fixtures. C2 targeted **depth**: a pinned `tools/mori-settlement-scan.py`
(sha256 `4c04bf21…ac9a9`), a quote-bound entry
`corpus/knowledge/wave-settlement-artifacts-r59.md` (13 claims over 6 pinned artifact copies), and
mined S553–S559 registry rows. At entry (`2b9f03975bfb6e508f35074ac8181ec8bf54e805`), depth,
freshness and calibration were tied lowest at 5 (coverage 6, operability 7, adjacency 6). C1 was
verified `met`; C2 measured `met` but was left **unverified** by verified met-flip counterexamples
— no scalar score delta is claimed.

Freeze `ccfd554e64084a0b4370806dd12a850e0a7bd7db` was amended to
`60b3a76ad0524c8978cc51922940be1c8c388915` before any data or seat scored (counter scratch-mkdir,
`git ls-tree` listing fix, register name-boundary fix and tool re-pin; receipts in
`.ufo/waves/round-59/evidence/`). Validated dispatch `8ff344ff18924c1ea63d46c3b3969f9fea05bc51`;
the 64-seat v2 wave `w1` ran through the orchestrator handoff (`w1.ready` →
`w1.ready.dispatched` 2026-10-28T02:53:55). Mix: reviewer 20, critic 10, mutation-tester 8,
executor 8, scribe 4, scout 4, connector 2, sentinel 2, revenger 4, simplifier 2 — attack seats
40/64 = 62.5%; L1 held planner. Data `be7372114ded3075e5f5a15227ffec977df22f7d` plus one data
correction `7b86704d7c0754a09958d131b64dbfa2a6d3eaed` (claim K11 demoted to prose — it cited the
r53 copy, which sits outside the counter's frozen `ARTIFACTS` map: `files:outside`).

## Landed changes

- Freeze + counters + 25 committed controls: `60b3a76ad0524c8978cc51922940be1c8c388915`
  (contract, `count-c1.py`, `count-c2.py`, `fixtures-c1/` 13 arms, `trees-c2/` 12 arms).
- Spec + validated dispatch + ready: `8ff344ff18924c1ea63d46c3b3969f9fea05bc51`
  (`build-w1-spec.py`, `w1-spec.json`, `w1-dispatch.json`, `w1.ready`, do-nothing receipts).
- Data: `be737211` (depth entry, 7 artifact copies under `corpus/evidence/sources-r59/`,
  S553–S560 rows, quarantine slice) + `7b86704d` (K11→prose correction).
- Wave reports, settlement/selftest/census receipts, lesson, LOG/SCORECARD/SHONEN/QUALITY-155,
  `tools/` (register-check, settlement-scan): `08127c99c2f28115a4e7bd3bb48f24593bdfd483` (lane tip).

## Claim measurements and verdicts
**C1 — calibration: verified `met`.** Before (entering `2b9f0397`):
`C1=unmet … failed=tool_absent,selftest,fixtures_absent,real,pointers`, rc 1 — the capability is
demonstrably absent pre-round. After (data `7b86704d`):
`C1=met selftest=ok fixtures=ok real=ok pointers=ok rev=7b86704d…`, rc 0. No met-flip was found:
Mo59Critic24 exercised the MANIFEST arm end-to-end (pure function of the pinned historical blob;
a post-pin MANIFEST append cannot alter the verdict), Mo59Reviewer05/06 replayed the receipt,
Mo59Executor41 re-ran all 13 hostile fixtures (13/13 still UNMET with expect matched), and the
do-nothing control at entering still fails five ways. **Routed robustness defects (do not flip
`met`)**: Mo59Sentinel57/58 HIGH — the sha pin is advisory at *execution* time (unpinned blob runs
as the operator with inherited env, and materialization writes follow symlinks out of scratch);
fixture `expect.txt` files are attacker-controlled committed bytes (empty expect neutralizes a
frozen control); Mo59Critic27 — the counter's semantic arms delegate to the same-author tool's
JSON (self-graded); Mo59Critic26 — C1 was already `met` at the freeze revision itself
(provenance/one-PR class; the claim's real do-nothing control is the *entering* revision, which
fails); Mo59MutationTester38 — selftest-consistency mutants survive `--selftest` but are killed
by `measure`; Mo59MutationTester36 — one emitted reason can satisfy a multi-prefix expect.

**C2 — depth: measured `met`, unverified (met-flip counterexamples).** Before (entering
`2b9f0397`): `C2=unmet … failed=copy_absent:…,entry_absent,tree`, rc 1. After (`7b86704d`):
`C2=met selftest=ok scan=ok drift=ok trees=ok entry=ok rows=ok pins=ok tree=ok claims=13 files=6`,
rc 0. **Unverified** — three verified counterexamples land on the frozen predicate:
Mo59Critic22 built a semantically-empty entry (`x.`×9 + one false sentence, all 10 claims quoting
the same 6-byte `"lane"` span, plus a malformed `K99` line and one fabricated S900 row covering
five copies) scoring `C2=met` — demonstrating orphaned `grammar:` reasons, no distinct-span bound
and no row↔copy binding (D1–D5); Mo59Reviewer08 confirmed `grammar:` reasons are unrouted in
`measure()` end-to-end; Mo59Critic23 showed `line:`≡`offset:` aliasing and vacuous claim sets
score `eval_entry ok`; Mo59Critic25 showed the drift arm accepts any nonzero exit (M1
filename-heuristic and M2 wrong-axis mutants both pass); Mo59MutationTester37's committed-symlink
copy survives `eval_entry` (latent). The landed entry's own 13 claims are honest and
byte-verified (Mo59Scribe47/48, Executor44/45), but the instrument cannot certify the class, so
no depth score change is claimed.

## Wave w1 settlement and integration

64 seats dispatched, 62 report files present at filing (missing: Mo59Executor40,
Mo59MutationTester31, Mo59MutationTester32 — partial; missing reports are not labeled dead).
Key integrated findings beyond the claim verdicts:
Mo59Reviewer12 surveyed all 10 committed `*-results.json` (r50–r58) and found two falsifiers of
the "note null / output nonempty" invariant — r50-a2w1 members carry non-null `note` and null
`output` 64/64, and r53 members carry extra key `report_file` (already recorded drift);
Mo59Revenger62 found a committed r55 member whose `output` is a non-JSON truncated blob naming a
report file that was never written (`Mo55Rc14.md` absent) — settlement artifacts record
*partial* settlement honestly but carry no status/verdict field; Mo59Executor46 confirmed the
S552↔S478 duplicate and that S560 reconciliation + W04 warning shape is correct;
Mo59Executor43 found and confirmed the landed fix for the K11 `files:outside` defect;
Mo59Connector55/56 flagged the settlement-vocabulary boundary with kumitate — kept clean: the
entry states artifact-shape facts only and never calls scan-OK a settlement verdict
(PROVINCE:119-120, 150/153 honored); Mo59Scout51 fresh-fetched all three quarantine rows;
Mo59Scout52 cross-checked sibling settlement schemas (tsukuroi's P55 mismatch routed as a
dispatch-mechanism defect to mori — the JSON counterexample reads "a lane silence or
wave-settlement question without a dispatch-mechanism defect goes to mori").

## Sources and frontier

Census 325 → 333 rows, validator exit 0. Added S553–S557 (A, own-work artifact copies), S558/S559
(B, own-work), and S560 (C, `rejected` — append-only reconciliation of the round-58 routed defect
2: S552 duplicates S478's DOI/PDF-sha; QUALITY criterion 155 now requires the DOI/sha sweep before
a new row). Quarantine slice re-derived identical to round 58 (S244, S262, S268): S244
**unverifiable** (ACM DOI 403 here; arXiv carrier reachable but the row carries no locator — no
quote exists to check); S262 **present** (live OpenAlex byte-equal to committed copy); S268
**present** (fresh IEEE VOR PDF fetch, sha `1603404d…` identical to the S478/S552 pin).
Assimilation: none. No frontier movement claimed.

## Considerthese and L0

`considerthese/2026-10-26.md` curation: suggestion 2 (carry-over ledger of unfixed critic flags)
was executed in the round-59 lesson — 9 unfixed ids swept, C1-F1 and RH-F2 have dispositions
(routed r57 / QUALITY 152), 7 ids remain open, carried to round 60. Suggestions 1 (implemented),
3 (recurring practice, not taken) and 4 (adopted) unchanged. L0: the open mori round-58 question
(calibration sub-axis ownership / route-map divergence) was noted, not re-filed; no new L0
question filed this round. Host routing note stands from r58 (actual `config.yml` routes
connector `@m_haiku`, reviewer/mutation-tester `@m_zfl`, critic/scout `@m_kfc`).

## Controls and receipts

`.ufo/waves/round-59/evidence/`: `c1-entering.txt`, `c2-entering.txt` (do-nothing controls),
`c1-at-freeze.txt`, `c2-at-freeze.txt`, `selftests.txt` (`REGCHECK_SELFTEST pass=12`,
`SETSCAN_SELFTEST pass=10`, `C1_SELFTEST pass=6`, `C2_SELFTEST pass=9`), `controls.txt`,
`census-start.txt`, plus `w1-dispatch.json`/`w1.ready`/`w1.ready.dispatched`. Both counters honor
`--scratch` and `TMPDIR` (the round-58 routed defect is closed); seat scratch roots were under
`/fast/scratch/hyaku/mori-r59/` per the reaper notice — no `/tmp` citations anywhere.

Attempt-1 leftovers (`.ufo/waves/round-59/count-c{1,2}.py` at selftest 21/24, never frozen or
dispatched) were discarded and replaced; nothing was reused as evidence. Watchdog line
`lane-dead-no-report mori round=59` (2026-10-28T02:30:35) names that attempt.

## Trend verdicts

- **Expansion — improved:** new depth entry with 13 byte-exact claims over 6 pinned artifact
  copies, 8 new source rows, 2 new instrument tools; the entry content is honest even though the
  instrument is decertified.
- **Quality — unprovable-but-better:** C1 is the lane's first *verified* instrument claim (no
  met-flip after a 40-seat attack share), but the sentinel execution-boundary HIGHs and C2's
  met-flips show the instrument class still needs hardening; no score raised.
- **Discernment — improved:** routed defects 1–4 all addressed (instrument grounding, route-map
  reconciliation, S552/S478 reconciliation + QUALITY 155, honest K-claim grammar); S244 kept
  unresolved rather than upgraded without a locator; quarantine verdicts match round 58 with a
  fresh independent fetch.

## SHONEN

- [~] `SKILL.md` decision tables, error patterns, checklists, cited sources — `SKILL.md:1211`,
  `SKILL.md:1178`; `corpus/QUALITY.md` criteria 148–155 (155 added this round).
- [~] End-to-end domain task executed and logged — `LOG.md` Round59 section (this round);
  `.ufo/waves/round-59/evidence/` receipts.
- [~] Instructions executable without oral context — `tools/mori-register-check.py --selftest`
  (12/12), `tools/mori-settlement-scan.py --selftest` (10/10), plus carried r56/r58 tools
  (`mori-vote-bind.py` 16/16, `mori-pin-check.py` 125/125); receipts in
  `evidence/selftests.txt`.
- [~] No cross-domain bleed — `corpus/knowledge/wave-settlement-artifacts-r59.md` Limits:
  artifact-shape facts only; settlement semantics stay kumitate-owned (PROVINCE:119-120);
  connector finding F4 boundary held.
