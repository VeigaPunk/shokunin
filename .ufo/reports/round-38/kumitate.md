# kumitate — round 38 attempt 1, repair-first (2026-10-21)

Lane open `753446a829edda519c75777ce95888443f51fa94`; final measured production
`01aab4b0a9756cb0d2ebea0e073a49f50a6d0223`; pushed delivery tip
`89ff4a74d92d71575687f407311c82abfac53ff7`. Source pin
`31c465f15669f744848bd9f5d56191c5085670f7`, private read-only clones. Domain source
was not edited or pushed. Tool installs: none. L0 questions: none.
Stale-lane: respawn-per-round driver; this assignment is exactly round38 attempt1;
this worker opened no separate kumitate mission and does not advance round39.

## Work performed

Declared claims (two, distinct axes):

1. **coverage:script-layer — per-anchor repair without regression** on the fixed population
   of 811 recognized spans in four notes: remaining-scripts-census (S8), route-probe-cluster
   (S7), sighting-wall (S4), native-trial-launch. No reset, no moving a previously-true
   anchor to make a detector green. The independent old-governing-token comparison is
   **469→628 true, 159 gains, zero true→nontrue**. Under the production oracle fixed before
   final measurements: **467→777 true, 208→21 debt, 136→13 unchecked**. Both comparisons
   cover all811, not a selected subset. Integer script-layer score remains10.
2. **operability — a failure-capable per-anchor truth floor** on the lowest non-retired
   axis (8). Replace the checklist's adjacency ratchet with `anchor-truth.mjs`, a committed
   expectation per anchor and a literal immutable `--base` floor. The gate rejects shifted
   anchors/re-pins, debt growth, checked-count shrink and invalid review tokens. Its
   selftest passes22/22; three targeted logic mutants are killed and restored exactly.
   Source S033 grounds commit-specific evidence rather than moving branch links. A8/C15
   gives f_O23/26, integer still8 (before A7/C14,21/24).

### Repairs and routed r37 debts

- **R1:** wave1 returned an individual MOVE/TOKEN/MOVE_TOKEN/DEBT/SKIP decision for all342
  initially non-true/unpaired positions. The L1 applied coordinate/path fixes individually,
  checked explicit cross-file qualifiers, and retained every round-open true coordinate.
  `.ufo/waves/round-38/evidence/review-decisions.json` preserves the decisions.
- **The original62-list is not misreported as62 old-token greens.**58 now pass with the
  closure's original governing tokens held fixed. Four are pairing discrepancies:
  MAX_BYTES at fixtureDir, validateTaskReceipt at a dynamic import, spawnSync at a
  throw/retry test, agentId at an underscored conflicting-test declaration. The first
  three have reviewed correct tokens; the fourth stays marked debt. The independent
  command and full per-note results are committed in `final/independent.txt`.
- **R2/R3:** the new gate uses positional runs, shared-symbol broadcast, no lookahead
  stealing a later citation, explicit reviewed tokens, immutable committed regular source
  blobs, and a floor pinned **before** repair in `e18ff1af3392e3823227644c977c237737fe65c9`.
  No extractor/pairing/normalization change occurred after that freeze. The legacy
  `claims-check --fidelity` arm remains a 20-note adjacency diagnostic, not the new
  checklist truth claim.
- **R4:** README's clause-guarded description corrected; named SCORECARD and r37-lesson
  corrections appended. LOG received a named correction for the r37 in-place rewrites
  and stale symbol-keyed/186/1551 claims, never a rewrite. Final diff: LOG50 additions,
  zero deletions; SOURCES one addition, zero deletions.
- **R5:** all final gates, selftests, independent measurements and digest-checked frozen
  replay were run at the final measured production commit, after falsify corrections.
  Original candidate receipts remain under `candidate-c938/`; `final/revision-binding.json`
  connects unchanged oracle hashes and reviewed deltas without pretending seats measured
  a later commit.
- **R6:** AuditRemainder6 was **misrouted, not dead**: its full r37 report was at the fleet
  root. Recovered byte-exact into the lane (cmp equal, sha256 c39ed761…), stray deleted,
  stale r37 wave reservation released. This corrects the r37 closure's cause diagnosis.
- **R7:** README rows for the r37 spot-check and r38 lesson bring C2 to86/86.
- Every one of the **21 lexical debt +13 unchecked** residual entries is marked in its
  note; `final/debt-marking.txt` and `final/revision-binding.json` confirm34/34 marks.
  Q17 records the immutable truth floor; Q18 records why lexical truth is not prose proof.

### Swarms (validated plan then run, unchanged specs)

| wave | seats / role mix | settled results |
|---|---|---|
| build |90:41 scout,39 reviewer,3 critic,3 executor,2 scribe,1 sentinel,1 connector |89 reports; ConnSibling failed, not replaced; first two whole-call attempts refused by job cap, third dispatched unchanged; slot released |
| falsify |88:55 reviewer,27 scout,3 mutation-tester,1 critic,1 sentinel,1 connector |45 reports,43 failed seats, none replaced; first granted attempt dispatched unchanged; slot released after all settled |

Total178 seats, under200. The L1 holds the planner seat. Roles used current host routing,
no model parameter or configuration writes. Build90 fits the user's64–100 band but missed
Main's narrower64–88 dispatch context; disclosed, and Main ruled not to undo/duplicate it.
Falsify stayed88. Policy path/digest, grants, exact specs, dispatch payloads and recorded agent
ids are in `.ufo/waves/round-38/` (`evidence/wave-grants-policy.txt`).

**Dead seats, never respawned:**

- Build ConnSibling: `[openai-codex/gpt-6-luna] Interrupted OpenAI Codex response after 256
  consecutive whitespace-only tool-call argument delta events (505 chars, sequence948..1203)`.
- Falsify Codex capacity9: Check09, Check40, Check54, Check58, Check60, Check65, Check67,
  CritNoHarm, SentFinal. `Retry budget exhausted after 5 retries` (8 for CritNoHarm/SentFinal):
  `Codex is at capacity, please try again later (code=turn_rate_limit_exceeded)`.
- Falsify Zai429/1302 failures34: Check03, Check04, Check05, Check06, Check07, Check12,
  Check14, Check15, Check20, Check22, Check23, Check24, Check25, Check30, Check32, Check35,
  Check38, Check39, Check41, Check42, Check48, Check50, Check55, Check56, Check63, Check66,
  Check70, Check73, Check75, Check76, Check78, Check79, VerifyIndependent, VerifyRecords.
  `[zai/glm-5.3-flash] Retry budget exhausted after 5 retries: 429 Rate limit reached for
  requests (type=1302)`.

Check27 completed but wrote its report to the fleet root: recovered with cmp+sha256294e0cee…,
then deleted the stray. It is not a dead seat. Full accounting/error evidence is committed.
The final no-pathspec fleet sweep shows driver files only; other lanes' files were untouched.

**Falsification was not claimed fully green:**40 completed anchor/prose groups judged171ids:
158 agreed,13 refuted,0 unverified in their headers.39 such seats failed, so this is not full
fresh semantic-seat coverage. One refutation concerns already-marked #92 debt, not a true
claim. The12 actionable findings were integrated: cached-preflight guarantee/reap range,
uncoded Error, tail-file readback range, blank-route fallback, stale main intro, persisted
reason reachability/expiry, Cf-only sanitizer claims, staging dependency, and configured-model
selection/every-target range. Five raw spans and one stronger reviewed token changed; no
oracle change and no true expectation loss. Supplements confirm the source fixes.
The L1 separately reopened all811 immutable source spans using independent Python matching,
with zero mismatched true entries; that witness is not passed off as the failed reviewers.

## Landed changes

Only hashes printed by `jj-lane.sh`'s final `landed` line are cited as new landings:

- `e18ff1af3392e3823227644c977c237737fe65c9` — oracle and round-open per-anchor baseline,
  committed before final measurements.
- `c938c068f4dbf356c0884c2121bbfe087fbe3caf` — reviewed repairs, pin, registry/checklist,
  Q17, maps/source/lesson, named corrections and recovered r37 evidence. Falsify target.
- `01aab4b0a9756cb0d2ebea0e073a49f50a6d0223` — integrated semantic/range refutations,
  Q18, population limitation, settled wave evidence. **Final measured production.**
- `89ff4a74d92d71575687f407311c82abfac53ff7` — final bound receipts and frozen replay only
  under `.ufo/waves/round-38/`, after measurement. No executable/corpus/pin changes.

LOG round38 entry and appended falsify receipt tie these changes to the motivating errors.
Helper state at delivery: local=remote89ff4a74…, ahead0 behind0 tracked0 untracked0.

## Before → after measurements

All following final receipts name production `01aab4b0a9756cb0d2ebea0e073a49f50a6d0223` and
source31c465f1; they are under `.ufo/waves/round-38/final/`:

| measure / command | before | final observed |
|---|---|---|
| independent original parser, `PIN=<private pin> python3 .ufo/waves/round-38/evidence/independent-measure.py.txt <lane> <measured rev>` |469 true /811 at round open |628 true,159 gains,zero true→nontrue;62-list58 original-token true /4 pairing exceptions;exit0 |
| fixed production oracle, `node scripts/anchor-truth.mjs --base e18ff1af3392e3823227644c977c237737fe65c9` |467 true,208 debt,136 unchecked /811 (baseline commit) |777 true,21 debt,13 unchecked;CLEAN exit0;all467 open-true coordinates unchanged |
| actual legacy gate before probe (`build/ExecRatchetBefore.md`) |MANIFEST_SCHEMA41→MAX_MANIFEST_BYTES49 shifted anchor still CLEAN;nonok200→199;raising ceiling also CLEAN |new AT03/05 shift/re-pin fixtures reject;no raised ceiling substituted for a repair |
| `node scripts/anchor-truth.mjs --selftest` |no per-anchor expectation gate |22/22 PASS exit0 |
| exact selftest logic mutants, pristine→mutant→restored |wrong pairing:17/22;disabled DEBT_GREW:21/22 (AT07);disabled block presence:21/22 (AT09),all exit1 |each pristine/restored22/22 exit0;byte-exact oracle hash ecb22db0… unchanged through final production |
| `node scripts/surface-probe.mjs --checklists` |14-item legacy checklist |15/15 PASS exit0 |
| `node scripts/claims-check.mjs --selftest` |47/47 before harness-final evidence gap |47/47 PASS exit0 at final bytes |
| `node scripts/proxy-check.mjs` |A7 C14 C2=84,score8 |MATCH A8 C15 C2=86/86,S88/88,R92/92,K51/51,pins6;score8;exit0 |
| `node scripts/claims-check.mjs` |19 yes rows /27 notes /184 sections /4 advisories |MATCH same counts;exit0 |
| `node scripts/sources-check.mjs` |32 rows |CLEAN33 rows,exit0 |
| `python3 .ufo/waves/round-38/frozen/replay.py.txt <lane> <pin>` |no digest-checked frozen replay |7 lane-input +80 source-blob digests verified;expected verdict MATCH at final commit;exit0;zeroed scratch expected digest gives snapshot_tampered exit2 |

PROXY warnings remain explicit: sources-check and anchor-truth have no `pin.<name>` key in
the frozen six-key proxy stanza. The new oracle is instead digest-pinned by its frozen-run
manifest and compared byte-identically to the baseline. CLAIMS' four inherited advisories
remain, not silently promoted to0.

## Sources & frontier

SOURCES rows32→33. Start and end command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`
printed `kumitate ok …/corpus/SOURCES.md`, exit0 at both ends (`evidence/census-start.txt`,
`final/census.txt`). Tiers A31→32/B1 unchanged; mined16→17,queued14/rejected2 unchanged.
One added A/docs row: **S033**, GitHub “Getting permanent links to files”, opened this round
by the scribe and re-opened by the L1. Located quote in §“File views show the latest version
on a branch”,23 words:

> so if you were to copy the normal URL, the file contents might not be the same when someone looks at it later.

The source states file-URL stability; applying it to line anchors is explicitly inference.
S033 is mined by the r38 lesson and cited by C2. No existing row changed. Fresh falsify
VerifySource re-opened it, counted23 words/verbatim, and reran census exit0.
No new knowledge ground or source family is claimed. Frontier is the instrument's fidelity,
not expansion by source-row count.

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry or coverage family; adding a source row
  alone is not expansion.
- **quality: improved (author measurement)** — independent old-token truth469→628,zero losses;
  all34 remaining lexical debt/unchecked entries marked;12 semantic findings corrected;
  no new whole-note/prose truth claim. Non-author closure still decides admission.
- **discernment: improved in-lane** — outside r37 disagreement produced Q17, and fresh
  falsifiers produced Q18 plus concrete source corrections. Source admit and debt/reject
  decisions are explicit. This is not a non-author taste judgment and does not replace
  the independent closure.

## SHONEN

- [~] Craft — eight registered gates,15-item checklist,final22/22 suite and three killed
  mutants; lexical/prose boundary stated; no non-author r38 judgment yet.
- [~] End-to-end — two-wave repair→falsify→integration→final frozen replay→pushed lane
  receipts; report lands after all wave evidence; LOG/SCORECARD pointers above.
- [~] No oral context — recreate source pin from origin.json, literal baseline commit,
  frozen digests/replayer, independent measurement source, explicit dead seats and limits.
- [~] Province — lane orchestration/tooling files and this fleet report only; source tree
  read-only; no rank/promotion/mint/config/template/driver edits.

### Limits left explicit

Registered811 is a **frozen extraction dialect**, not all Markdown locators. ConnPopulation
reconciles legacy710-in-four/1574-in20 with ExecTruthIndep817: eight escaped-template-block
spans missed by the frozen regex, minus two basename spans omitted by the independent
extractor. Do not switch populations after seeing results. Escape-aware extraction needs a
future fixture-first version/crosswalk.21 debt +13 unchecked remain; broader inherited prose
and the other16 legacy notes are not claimed pin-true. A word on a line is not a semantic
oracle.43 falsify failures limit fresh-seat coverage; all are recorded, none respawned.
