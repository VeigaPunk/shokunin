# chousa — round 86 report

Lane `chousa-shokunin` (deep-research method: question framing, source hierarchy, citation chaining,
claim-vs-source verification). Round 86, attempt 1. Base `3bfb6885958ad4a674ad1896f70d1e836be609e4`.

**Declared claims (2).** **C1 — operability** (the lane's lowest scored non-retired axis, historical 3/10;
capability acquisition + repair): the round-86 successor battery generates the round-85 `D1` (200-only) class from
committed bytes *inside* the frozen predicate and derives the round-85 `M17` mutant from the subject tool's own bytes,
so the battery kills the mutant instead of surviving it. **C2 — calibration**: the two curation defects the round-85
non-author check routed are closed — the `S024`/`S031` supersession inversion and the two decision-table cells that
stated a distinction their cited quotes refuse — plus the retraction of round-85's stale "verified" row.

## Work performed

- **C1 (operability)** — `corpus/evidence/round86/gate-records-r86.py`: `build_d1_203_admit()` derives an admit record
  from the committed `S021` PubMed refetch row (its `203` attempt, stored `txt_sha256`, capture key and capture body;
  quote located in the body, no literal record text) and appends it to the forged estate expected `REFETCH`;
  `build_mutant()` rewrites `r[6] == "200"` → `r[6].startswith("2")` in the **subject tool's own bytes** and the
  predicate requires the mutant to accept every positive *and* the D1 record (`MUT17_KILLED=1/1`), so a substitution
  that finds nothing scores `0/1`. Evidence: `corpus/evidence/round86/claims.md` §C1;
  `after/c1-after.txt`; `controls/receipts/c1-k0-donothing.txt`, `…/c1-k0b-frozen-instrument.txt`.
- **C1 ground** — `S216` (RFC 9110 §15.3.4) opened this round: a 203 body is a transforming proxy's representation, so
  it cannot ground a registered quote. Evidence: `corpus/lessons/round-86.md:12` (`GATE-RECORD S216 … OK`),
  `corpus/captures/b1b13a12aee75c6ecc20fb91.txt`.
- **C2 (calibration)** — `corpus/SOURCES.md`: `S031` `queued`→`mined` with `used-by` to the r85 entry; `S024` restored
  to `queued`/`—`/`2026-10-21`; `corpus/knowledge/search-transparency-reporting-r84.md` row 9 now warrants `Q13`, the
  `S023` `modified` Definition located at capture line 8786; `corpus/knowledge/provenance-recording-r85.md` row 6
  warrants `Q7 (S031)` and its `Never` states only the definition's negation. Evidence:
  `corpus/evidence/round86/curation-r86.py`, `after/c2-after.txt`, `controls/receipts/c2-d0-donothing.txt`.
- **Round-85 routed defects 1–4 closed** — 1: the `S024`/`S031` inversion and the two warrant cells (above); 2: this
  round's control receipts each name the command and the tree they ran on, and the instrument bytes are pinned beside
  them (`corpus/evidence/round86/instrument-pins.txt`); 3: the 200-only forge is now *inside* the battery (C1);
  4: `corpus/lessons/round-86.md` `## Corrections` retracts round-85's `## Claim outcomes` "verified" column without
  editing the round-85 file. Routed defect 5 (kotodama `check-gate-captures.py` false-green) stays cross-lane and is
  reconfirmed read-only by `R86ConnectorSiblings`.
- **Frontier step (§2b)** — egress table `corpus/evidence/round86/egress-approval.md` committed at `e4468752` before
  the first fetch; four GETs `2026-11-08T06:00:10–11Z` (`S216`, `S217`, `S031` re-open, `S023` re-open), all HTTP 200,
  all inside the table. `S216` admitted (tier A, `mined`), `S217` refused on content and registered `rejected` with its
  flip condition. `S023`/`S031` re-opened for this round's access date; `S023`'s capture bytes are unchanged at base and
  landing (lesson correction 1).
- **Trial run end-to-end** — the wave ran both counters on a fresh `git archive` of the landing tree and on the base
  tree, with per-field comparison against `claims.md` (`R86ExecRepro`, `R86ExecBase`), reproduced the before-side
  controls byte-for-byte, and ran the mutation probe (nine counter mutants, five kill-leg probes).
- **Wave w1 verification and repairs** — the 12-seat wave attacked both claims on committed bytes; the two
  substantive repairs it forced are in the integration commits: `R86ScribeLesson` showed that QUALITY 173 mis-stated
  the tool's record forms (three, not two) and that QUALITY 174's cited check does not witness its own sentence (both
  criteria rewritten, `c59391a1`), and that the `S023` re-open carried no record line (added and verified, same
  commit). `R86ScoutRegistry` found no registry defect of the round's class at the landing revision (0 supersession
  inversions over 10 edges, 197/197 `used-by` paths exist, 0 opened-date inversions) and confirmed the counter's
  blind spots with seven registry mutations; two `mined` rows whose `used-by` file never names the id (`S174`/`S175`,
  `corpus/evidence/round71/claims.md`) are routed as ledger drift, not repaired.
- **Mined mistake** — `corpus/lessons/round-86.md` `## Mistakes` item 1: an instrument that cannot express a decision
  the round made (a successful fetch refused on content has no `GATE-RECORD` form). Items 2–4 record a frozen
  predicate narrower than the routed defect, a case-blind comparison, and the imported-warrant class with fix and
  capture pointer. Five corrections (append-only) record this round's own deviations.
- **Criteria** — `corpus/QUALITY.md` 177–181 (immutable cells; a frozen `teaches` is not evidence; a published numeric
  floor is a conjunct of the instrument; a class is as wide as its committed instances; key-vs-content-sha identity).
- **Round-85 spot-check routed defect 6 (SHONEN boxes / promotion)** — not actionable by the lane: the four boxes are
  operator-owned and no non-author `[x]` exists, so the promotion gate stays unmet; the check did not disagree with any
  box's lane assertion, and this round adds evidence pointers to boxes 2 and 3 without promoting any.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| egress approval table (before the first fetch) | Round 86 bullet 2 | `e446875260a11e3489a0d78344d71d7fbb006a42` |
| freeze: claims, both counters, `c2-positives.tsv`, pins, three control receipts, plan | Round 86 bullet 3 | `d0b1bd06872cdf0eeb03eccd099ff69ae6704307` |
| landing: `S216`/`S217` rows, `S031` mined / `S024` restored, r84 row 9 → `Q13`, r85 row 6 → `S031`, lesson, QUALITY 173–176, after receipts, captures, refetch rows | Round 86 bullet 4 | `667a5d091dc46168ed95eda0ae7f19a9bcf139a2` |
| wave w1 spec + validated dispatch | Round 86 bullet 6 | `a9bed303f71b9b8e918992821f2b0185f709993f` |
| integration part 1: plan amendments 11–12, lesson corrections, QUALITY 177–181, `S031` anchor reverted, `S217` cell corrected, SCORECARD verdict, LOG | Round 86 bullets 7–9 | `95f0fc4468f7151ea5a6fcbaaff1722b8080ef33` |
| integration part 2: QUALITY 173/174 rewritten to what their artifacts say, `S023` re-open record line added (scribe-seat findings) | Round 86 bullet 7 | `c59391a1358c55ec500635d431a779eb63b718b1` |
| integration part 3: wave w1 official results (12 seats), `claim-falsification.tsv`, after receipts at the integration tip | Round 86 bullet 6 | `16ba033bd5446ba6e30c5c06f7c39803fda7237f` |
| wave handoff evidence (`w1.ready`, `w1.ready.dispatched`, dispatch stderr) and the measurement logs | Round 86 bullet 9 | `0cbbeb665bac00c27274f9b3560b37c9783f3f73` (final lane hash) |

## Before → after measurements

**C1 (operability).** Counting command (from the claims file):

```sh
S=$(mktemp -d -p /fast/scratch/hyaku) && git -C /home/vgpnk/Projects/shokunin/chousa-shokunin archive <rev> | tar -x -C "$S" \
  && python3 -B "$S/corpus/evidence/round86/gate-records-r86.py" --root "$S" \
       --repo /home/vgpnk/Projects/shokunin/chousa-shokunin --work "$S"
```

- **Before** — round-85 instrument (`corpus/evidence/round85/gate-records-r85.py`) on the landing tool:
  `POSITIVE=15/15 FRESH_POSITIVE=5/5 FORGED_REFUSED=354/354 EXPECTED_CODE=354/354 EMPTY_REFUSED=1/1 RC=4/4 SETUP=1/1`
  / `GATE_RECORDS_R85=PASS`, exit 0, with **zero** `D1-203-admit`/`MUT17` lines in its bytes (grep count 0).
  Round-86 battery on the pre-round-85 tool (`43c3f728`, `2xx` rule):
  `FORGED_REFUSED=354/355 EXPECTED_CODE=342/355 … SETUP=0/1 D1_FORGES=1 D1_REFUSED=0/1 MUT17_KILLED=0/1` /
  `GATE_RECORDS_R86=FAIL`, exit 1 (`controls/receipts/c1-k0-donothing.txt`).
- **After** — at `667a5d09` and at the final lane hash `0cbbeb66`:
  `POSITIVE=15/15 FRESH_POSITIVE=5/5 FORGED_REFUSED=355/355 EXPECTED_CODE=355/355 EMPTY_REFUSED=1/1 RC=4/4 SETUP=1/1 D1_FORGES=1 D1_REFUSED=1/1 MUT17_KILLED=1/1`
  / `GATE_RECORDS_R86=PASS`, exit 0 (`corpus/evidence/round86/after/c1-after.txt`).

**C2 (calibration).** Counting command: `python3 -B corpus/evidence/round86/curation-r86.py --root <tree>`.

- **Before** — base tree `3bfb6885`: `SUPERSEDED_LIVE=1 UNENTAILED_TERM=2 MODIFIED_DEF_CITED=0 QUOTES_LOCATED=19/19`
  / `CURATION_R86=FAIL`, exit 1 (`controls/receipts/c2-d0-donothing.txt`; `SUPERSEDED_STILL_LIVE S024 is mined while
  S031 supersedes it and is queued`).
- **After** — at `667a5d09` and at the final lane hash `0cbbeb66`: `SUPERSEDED_LIVE=0 UNENTAILED_TERM=0 MODIFIED_DEF_CITED=1
  QUOTES_LOCATED=20/20` / `CURATION_R86=PASS`, exit 0 (`corpus/evidence/round86/after/c2-after.txt`).

**Claim verdicts.** C1 verifies as stated (every clause held under the wave: `R86ReviewerClaims` clause table;
`R86ExecRepro`/`R86ExecBase` reproduce both sides; `R86ExecHarm` shows no genuine committed record moving across 449
records; `R86ExecForge` finds no in-class admit accepted). C2 verifies on the property **narrowed in plan amendment 11**:
the wave falsified the published predicate's `total ≥ 19` floor (never implemented — `R86ReviewerEntry` §2.3,
`R86CriticClaims` V4) and the warrant-linkage reading of `MODIFIED_DEF_CITED` (`R86ReviewerEntry` §2.4); the amendment
withdraws the floor, keeps the four enforced fields, and moves the class closure of the imported-distinction defect to
review — where it held (`R86ReviewerEntry` §1: both repaired rows state only what `Q13` at S023 capture line 8786 and
`Q7` at S031 capture line 211 state; entry-wide `primary`/`tool`/`version`/`step` = 0).

**Wave shape.** One v1 wave, 12 seats (4 executor, 2 reviewer, 1 critic, 1 mutation-tester, 1 revenger, 1 scout,
1 connector, 1 scribe) under `scripts/hyaku/ufo-wave-policy.json` (band 8–16); `w1-results.json` carries 12 settled
seats, 0 dead, and every seat wrote its report in `.ufo/waves/round-86/w1/`; no residual call, round total 12.
Attack share 7/12 ≈ 58 % by the ledger's role set (6 by the gate's `ATTACK_ROLES`, which excludes scout). Pre-file
ledger gate: `PREFILE-FALSIFICATION: pass claims=2 rows=12 attack_seats=6 findings=0`, exit 0.

## Sources & frontier

Census command (round start and end):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

- **Start** — exit 0, five pre-existing `W04` duplicate-URL warnings (`S051`, `S053`, `S073`, `S074`, `S075`), registry
  215 rows. (Process note: the first census run of this round happened after the landing commit, not before it; the base
  row count is derived from `git show 3bfb6885:corpus/SOURCES.md` with the frozen census one-liners.)
- **End** — exit 0 at `0cbbeb66`, the same five `W04` warnings (`S051`, `S053`, `S073`, `S074`, `S075`), registry **217** rows.
- **Rows added by tier** — tier A +2: `S216` (RFC 9110, `mined`), `S217` (DCMI Namespace Policy, `rejected`).
  `217 − 215 = 2`; status 180/12/23 → 181/12/24 (`mined`/`queued`/`rejected`).
- **Rows touched old→new** — `S024`: `status mined`→`queued`, `used-by <r85 entry>`→`—`, `opened 2026-11-08`→
  `2026-10-21`, `anchor` restored (lesson correction 2); `S031`: `status queued`→`mined`, `used-by —`→
  `corpus/knowledge/provenance-recording-r85.md`; `S023`: re-opened only (no cell change, capture bytes unchanged);
  `S216`, `S217`: new rows.
- **Frontier rows advanced** — none: the round's move is instrument coverage on a surface the coverage map already
  lists, and the curation repair restores ground rather than advancing it. `corpus/README.md` frontier text is
  unchanged and still ends at round 6, a carried defect this round does not claim to fix.
- **Assimilation** — `Assimilation: none` this round: `merge/chousa/` was not adopted (the round's claims are the two
  routed defect classes), and no still-unimplemented `considerthese/` proposal was taken.

## Trend verdicts

- **expansion: unchanged** — `corpus/knowledge/*.md` 97 → 97; the registry gained one mined tier-A standards row
  (`S216`) and one refused row (`S217`), which is curation, not new held ground. Stated honestly rather than padded.
- **quality: improved** — the battery's zero-forgery 200-only class is now load-bearing inside the predicate and its
  mutant is killed by the computed bytes; two entry warrants repaired and located; five criteria mined, four from this
  round's own findings; two registry deviations (S031 anchor, S217 cell) reverted/corrected in the integration commit.
- **discernment: improved** — the wave falsified the published C2 predicate on two clauses and the lane narrowed the
  claim instead of filing it, published its own three narrative/registry deviations, and mined them as criteria; the
  one review that disagreed with the landed text (capture identity) is recorded as a correction, not defended.

## SHONEN

- [~] SKILL.md decision tables / error patterns / cited sources — `SKILL.md` Gates table, `corpus/knowledge/metadata-screen-r25.md` (lane assertion; no non-author verifier).
- [~] At least one end-to-end domain task logged — `LOG.md` Round 86 entry; `.ufo/waves/round-86/w1/R86ExecRepro.md`, `…/R86ExecBase.md` (lane assertion).
- [~] Instructions executable without oral context — `bash tools/research-gate.sh --selftest` → `PASS (283 cases, 0 skipped)`; `PREFLIGHT=8/8` (`corpus/evidence/round86/measure/`) (lane assertion).
- [~] No cross-domain bleed — `PROVINCE.md` untouched; `R86ConnectorSiblings.md` reports the kotodama false-green read-only (lane assertion).

## Extras

- **Stale-lane** — none: this is the lane's own round under the respawn-per-round driver; no other mission of this lane
  is open, and nothing from an earlier attempt of round 86 was inherited (no `.ufo/watchdog.log` `lane-dead-no-report
  chousa round=86` line).
- **Tool installs** — none this round: no tool was installed or upgraded by the L1 or by any seat; no pacman
  transaction was attempted (host-wide pause respected).
- **Misroot sweep** — `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned
  `.scratch/` / `.ufo/l0-questions.md` changes and another lane's report (`round-93/tsukuroi.md`); no file written by
  this round's seats sits at the fleet root.
- **Open questions** — none filed; the carried `8d77e6c1` general fetch-scope question is unchanged and is answered
  inside this round by its own approval table.
