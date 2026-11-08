# chousa — round 88 report

## Work performed

Declares two claims on distinct axes (one of them the lowest scored non-retired axis, operability), each falsifiable
before→after:

- **C1 (operability)** — the 203 class is bound to `http == "203"` in both independent derivations, the width legs
  are pinned against a third derivation plus `ROWS_203 = 3`, and the verdict re-reads each leg's own receipt file and
  reconciles its detail against its value (`corpus/evidence/round88/gate-records-r88.py`; freeze
  `4ea9d008abfd2e09cb51649a42678a78f52ac530`).
- **C2 (calibration)** — the curation counter closes the four round-87 routed defects: every named qid must share a
  term (`WARRANT` every-qid), the floor pins the per-entry qid set and a per-row token floor of 7, and a superseder
  disposes only when `mined` (`corpus/evidence/round88/curation-r88.py`), plus the disclosed entry repair
  (`corpus/knowledge/provenance-recording-r85.md` row "Naming what a resource derives from" `Q1, Q3 (S215)` →
  `Q1 (S215)`).

- Base `f484d94f` (round-87 landing + `corpus/lessons/round-87-verifier-spotcheck.md`), freeze `4ea9d008`
  (pushed), integration `f7cedcad`, wave w1 evidence `f84286d5`, falsification ledger `bb21673b`.
- Wave: one v1 wave, 12 seats (4 executor, 1 reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 scout,
  1 connector, 1 scribe), 0 dead; every L2 floor role met inside the single wave (the L1 holds the canonical
  planner seat in-session; no planner seat was dispatched, per the run-7 ruling). Attack share 6/12 = 50%
  (reviewer, critic, mutation-tester, the two forge seats, sentinel). Round total 12 seats.
- **Premise register (gate-format records, at base):**

## Landed changes

| Change | LOG.md entry | Commit that carries it |
|---|---|---|
| Freeze: the two counters, the control batteries, `controls/expected.tsv`, the pre-freeze receipts, `instrument-pins.txt`, the provenance row repair | "Round 88" entry (frozen intent) | `4ea9d008abfd2e09cb51649a42678a78f52ac530` (pushed; `git ls-remote origin refs/heads/master` shows it) |
| Integration: `corpus/lessons/round-88.md` (Gate, Mistakes 1–5, Corrections 1–4, Spot-check intake, Trends), `LOG.md` round-88 entry, `SCORECARD.md` round-87 corrections (13→12 seats; eight criteria), `plans/round-88.md` amendments 1–2, `corpus/evidence/round88/after/` and `census-end.txt` | "Round 88" entry | `f7cedcadd121473eedc6ff3ec395109a87943443` (pushed; remote tip at filing) |
| Wave w1: `w1-spec.json`, validated `w1-dispatch.json`, `w1.ready`, `w1.ready.dispatched`, `w1-results.json`, and the 12 seats' reports and receipts under `.ufo/waves/round-88/w1/` | "Wave w1" entry | `f84286d56653cbbfca5ff1a95269e6da5687f8b7` (pushed) |
| Wave evidence: `claim-falsification.tsv` (17 rows, every attack seat) | "Wave w1" entry | `bb21673b97eaa71a2bb8cd648240e094fbd14119` (pushed) |

## Before → after measurements

- **C1.** Counting command (run from a `git archive` tree at each revision):
  `python3 -B corpus/evidence/round88/gate-records-r88.py --root DIR --repo <lane> --work DIR`; mutants
  `corpus/evidence/round88/mutate-r88.py`; controls `corpus/evidence/round88/curation-r88-controls.py`.
  Before: the round-87 battery, which cannot bind the class to 203 (`controls/receipts/c1-k0b-frozen-instrument.txt`,
  no `LEG_REREAD` field, no width pin); the round-88 battery pointed at the same tool passes byte-identically
  because the tool is unchanged this round (`controls/receipts/c1-k0-donothing.txt`, exit 0 — the sentinel's F7,
  so C1's non-vacuity is carried by the mutants). At the freeze `4ea9d008`: `GATE_RECORDS_R88=PASS`,
  `TOOL=present POSITIVE=15/15 FRESH_POSITIVE=5/5 FORGED_REFUSED=362/362 EXPECTED_CODE=362/362 EMPTY_REFUSED=1/1
  RC=4/4 SETUP=1/1 D1_EXPECTED=3 D1_FORGES=3 D1_REFUSED=3/3 D2_FORGES=3 D2_REFUSED=3/3 MUT_ADMIT_DERIVED=1
  MUT_ADMIT_KILLED=1 MUT_UNREACH_DERIVED=1 MUT_UNREACH_KILLED=1 DERIVE_NEG=1 LEGS=15/15`,
  `LEG_REREAD=15/15 RECONCILED=15/15 LEGS_APPENDED=15`, exit 0 (`after/c1-after.txt`). Verdict: **verified as
  stated** on the measured property; **fired on K4** by two seats (the detached-`ok` class), honestly reported.
- **C2.** Commands: `python3 -B corpus/evidence/round88/curation-r88.py --root DIR` and
  `curation-r88-controls.py --root DIR --work DIR`. Before: the round-87 counter accepts all five round-87 outliers
  (`FORGERY_REFUSED=5/5 R87_ACCEPTED_FORGERY=5/5`, `controls/receipts/c2-controls.txt`) and prints
  `CURATION_R87=PASS` on the round-88 tree (`controls/receipts/c2-d0-donothing.txt`). At the freeze `4ea9d008`:
  `SUPERSEDED_LIVE=0 UNENTAILED_TERM=0 MODIFIED_DEF_CITED=1 QUOTES_LOCATED=20/20 WARRANT_OK=17/17
  TEACHES_CHECKED=1 TEACHES_FLAGGED=1 TEACHES_UNRESOLVED=0 LEGS=7/7`, `CURATION_R88=PASS`, exit 0
  (`after/c2-after.txt`); the unrepaired base tree prints `CURATION_R88=FAIL` with the `Q1, Q3` warrant link
  (`WARRANT_OK=16/17`), so the entry repair is load-bearing. Verdict: **verified as stated** on the measured
  property; the routed repairs (per-format reconciliation, duplicate-qid guard, live superseder-own-read clause) are
  named for round 89 in the plan's amendment 1, not amended beside a scored run.

## Sources & frontier

`SOURCES: registry rows before→after 218 → 218 (no row opened; the round repaired one knowledge-entry row, disclosed
in plans/round-88.md §Pre-freeze repairs 6). Census command run at round start and round end (census-start.txt
computed_against=f484d94f, census-end.txt at the integration tip; both exit 0, same five pre-existing W04 warnings).
Rows added by tier: 0/0/0. Rows touched old→new: none in corpus/SOURCES.md. Frontier rows advanced: none.

Assimilation: none (the `merge/chousa/` package still collides — the scout measured 113/113 campaign ids colliding,
109 hard — and no information from the package was consumed; no new `considerthese/` proposal was consumed this
round; the daemon-owner cross-tool watch in `considerthese/2026-11-07.md` is cited as the independent statement of
the reconciliation class, not as evidence).

Tooling: nothing installed this round (stock python3 + git only); the pacman pause was respected by not
installing anything.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Conformance notes:

1. The `claims.json` wording in the round-88 plan was carried from round 87; neither a `claims.json` nor an
   egress table exists for round 88 (a loopback-only window needs none). The plan's amendments 1–2 correct the
   freeze sentences and name the repair set; nothing is lost.
2. The `controls/expected.tsv` `c1-do-nothing` row expects exit 1 while its own committed receipt prints PASS —
   the subject tool is byte-identical at base and freeze, so the expectation is unsatisfiable as written; the
   round-87 counter cannot express the target either way. Routed to round 89's control-receipt discipline (the
   frozen `control-receipt-vs-expectation` gate).
3. `.ufo/prompts/chousa-round-88.md:143` (the addendum's run-15 quote; byte-identical to the round-87 prompt by
   template, operator-owned) corrupts the run-15 quote mid-word: the fragment reads `…on the hyaku style but using
   these models and conc` / `…re each` (not "shokunin style bu" as the round-87 conformance note mis-quoted; the
   round-87 lesson's `## Corrections` 3 now cites the real bytes). Substance unchanged; the plan's literal
   description is corrected, not the template.

## Trend verdicts

- **expansion: unchanged** — `ls corpus/knowledge/*.md | wc -l` is 97 at both revisions; the registry stays at 218
  rows (no row opened or re-opened; the round fetched nothing). The round's gain is the two instruments' four routed
  repairs, and the lesson says so (evidence: `corpus/lessons/round-88.md` `## Trends`).
- **quality: improved** — the two instruments carry four routed repairs each with failable witnesses: the
  203-bound class (both derivations plus the third pin), the leg-receipt reconciliation, and on C2 the
  every-qid warrant, the qid-set pin plus the 7-word token floor, and the mined-superseder disposal; five
  round-87 forgeries are refused with named legs; `tools/gate-records.py` selftest `PASS (283 cases, 0 skipped)`,
  and the lane preflight `PREFLIGHT=8/8` at the tip.
- **discernment: improved** — the wave fired both claims on their own reconciliation and wording clauses with
  receipts (`R88ReviewerC1`, `R88CriticClaims`, `R88ExecC2Forge`, `R88ScoutRegistry`), and the round published the
  firings, the dead clause and the control-receipt defects in its own lesson and its plan's amendments rather than
  arguing them away; the per-format reconciliation, the verdict-vs-field reconciliation, the duplicate-qid guard
  and the live superseder-own-read clause are routed to round 89 with their seats and receipts named.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  `SKILL.md` Gates table; `corpus/knowledge/metadata-screen-r25.md` (lane assertion; no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  `LOG.md` Round 9 archive verification; `corpus/fixtures/archives-r9/`; r25 explicit-root hold battery (lane assertion)
- [~] Instructions executable by an agent without oral context
  `bash tools/research-gate.sh --selftest`; `corpus/evidence/round25-measure-after.log`, `corpus/evidence/round25-meta-differential.log` (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  `PROVINCE.md`; `corpus/knowledge/metadata-screen-r25.md` Limits; `.ufo/waves/round-25/build/ConnectorMetaSiblings.md` (lane assertion)

## Process notes

- Round shape: one v1 wave of 12 seats (policy band 8–16, `ufo-wave-policy.json`); attack share 6/12 = 50%
  (reviewer, critic, mutation-tester, the two forge seats, sentinel); 1 connector seat. Residual calls: none.
- Planner seat: the L1 held it in-session (no planner seat dispatched, per the run-7 ruling); the bounded planning
  data-walks rode the scout and connector items.
- Straight line committed through the lane helper (`jj-lane.sh`); only the pushed hashes at `git ls-remote
  refs/heads/master` are cited below. Draft notes L1-side: `plans/round-88.md` (the plan, amendments 1–2),
  `corpus/evidence/round88/claims.md` (the frozen predicate set).
- The `R88ExecForge` seat shipped no `VERDICT:` trailer; its content (28 probes, zero accepted forgeries) reads
  C1 held, and the scribe's tally counts it so; the missing trailer is logged as a seat-discipline finding in the
  lesson and is not hidden.
