# chousa — round 89 report

## Work performed

Declares two claims on distinct axes, one of them the lowest scored non-retired axis (operability, historical 3/10),
each falsifiable before→after. Both are **repairs**: round 88's wave fired both of its claims on their own
reconciliation clauses and the closure routed eight defects; this round closes seven of them on committed bytes.

- **C1 (operability) — `C1-BATTERY-R89`.** The successor battery `corpus/evidence/round89/gate-records-r89.py`
  re-derives every leg's receipt detail **in its own grammar** (`n/m`; `len/d1/div3 pinN` with all four equal and
  `pin == ROWS_203`; `derived=x killed=y` with both 1; `tool present`) and cross-checks every leg's re-derived
  numbers against the summary fields printed for it (`DIV3` is printed for that reason). The four shapes round 88's
  wave left alive — a detached width `ok` over a narrowed third derivation, a detached mutant `ok` over zeroed
  measurements, a forged width detail, a printed field detached from its measurement — are now killed by name.
  Evidence: `corpus/evidence/round89/gate-records-r89.py`, `mutate-r89.py`; receipts
  `corpus/evidence/round89/controls/receipts/c1-{landing,mutants,harm,prior-instrument}.txt`.
- **C2 (calibration) — `C2-CURATION-R89`.** The successor curation counter `corpus/evidence/round89/curation-r89.py`
  derives its verdict from the tallies the summary prints, adds a duplicate-qid guard, and matches the
  superseder-own-read clause against the **raw** cell (the round-88 clause matched a case-sensitive pattern against a
  lowercased cell and could never fire). Seven tree forgeries are refused, each accepted by the counter that preceded
  it. Evidence: `corpus/evidence/round89/curation-r89.py`, `curation-r89-controls.py`, `curation-r89-mutants.py`;
  receipts `controls/receipts/c2-{landing,controls,mutants,prior-instrument}.txt`.
- **Frontier step (§2b)** — census run at round start and round end (both exit 0, same five pre-existing `W04`
  warnings; 218 rows at both revisions); two `used-by` cells extended old→new (S216, S218) with no other cell moved;
  four mistakes mined into `corpus/lessons/round-89.md` `## Mistakes` and four criteria (QUALITY 190–193) landed; the
  round's sourced claim cites `S216` and `S218`, **re-opened this round** from committed bytes with a ≤25-word located
  quote each, verified by `tools/gate-records.py` (`GATE_RECORDS files=1 records=2 ok=2 fail=0`, exit 0).
- **Wave** — one v1 wave, 12 seats (4 executor, 2 reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 scout,
  1 connector, 1 scribe), attack share 7/12 = 58% (2 reviewer, critic, mutation-tester, sentinel, connector overlap
  scan, plus the two forge executors counted separately in the tallies).
- **Wave firings, honestly.** Six seats fired a *sentence* (never the predicate): `R89ReviewerC2` B1 and
  `R89CriticClaims` fired C2's "rather than a separate `all(ok)`" phrasing (Amendment 1); `R89ReviewerC1` F1–F3 fired
  C1's unbound `LEGS_MEASURED` cell, its "every round-88 field" universal and its non-runnable counting command
  (Amendments 4–5); `R89SentinelScope` B1–B5 fired the control-receipt discipline and C2's unprinted `VERDICT` token
  (Amendments 7–8); `R89MutBattery` fired C2's exposure to a constant-substituted detector (Amendment 9). One
  reviewer finding was **refuted** against committed bytes (Amendment 3). The frozen predicates printed PASS at the
  freeze and at the tip; no amendment moved a measured value.
- **Claims frozen before data** — `corpus/evidence/round89/claims.md` + `.ufo/waves/round-89/claims.json` (the layout
  round 88 lacked, which made its pre-file gate end `SETUP findings=1`), the six instruments, `controls/expected.tsv`,
  the receipt-vs-expectation driver and `instrument-pins.txt`, all in one commit.

## Landed changes

| Change | LOG.md entry | Commit that carries it |
|---|---|---|
| Freeze: two claims (prose + machine), six instruments, `controls/expected.tsv`, `run-controls.sh`, eight pre-freeze receipts, `instrument-pins.txt`, the two registry `used-by` cells | "Round 89" entry | `ac0a0892c15de11fb28d3208f2b287687c00477e` |
| Integration: `corpus/lessons/round-89.md` (Gate, Claim outcomes, Mistakes 1–7, Spot-check intake 1–8, Trends, Wave settlement), `LOG.md` round-89 entry, `SCORECARD.md` round-89 planned row + verdict, `plans/round-89.md` amendments 1–9, `corpus/QUALITY.md` criteria 190–195, the gate-record and registry-cell receipts | "Round 89" entry | `a72f204bfeea10fc59497e23bcbda021a1a2ced5` (pushed; `git ls-remote origin refs/heads/master` shows it) |
| Wave w1 evidence: spec, validated dispatch, `w1.ready`, `w1-results.json`, the 12 seats' reports and receipts, the falsification ledger (17 rows, 6 attack seats), census-end | "Round 89" entry | `976d422cd63fd4bcf3fb04cf8b5060a349e76382` (pushed) |

## Before → after measurements

- **C1.** Counting command (from the lane root):
  `python3 -B corpus/evidence/round89/gate-records-r89.py --root . --repo . --work <scratch>` plus
  `python3 -B corpus/evidence/round89/mutate-r89.py --root . --repo . --work <scratch>` plus
  `python3 -B corpus/evidence/round89/harm-recheck.py --root . --repo . --base-tool <base blob>`.
  **Before** (the round-88 battery on the same tree): `GATE_RECORDS_R88=PASS` with no `CROSSCHECK` field, and the four
  round-88 survivor shapes accepted (`controls/receipts/c1-prior-instrument.txt`; non-vacuity is the mutant battery).
  **After** at the freeze: `GATE_RECORDS_R89=PASS`, `LEG_REREAD=16/16 RECONCILED=16/16 CROSSCHECK=15/15
  LEGS_APPENDED=16`, every round-88 field unchanged (`FORGED_REFUSED=EXPECTED_CODE=362/362`, `D1_REFUSED=3/3`,
  `D2_REFUSED=3/3`, `MUT_ADMIT_KILLED=1`, `MUT_UNREACH_KILLED=1`); mutants `MUTANTS_KILLED=11/11
  TOOL_MUTANTS_CAUGHT=2/2 TOTAL=13/13`; harm `moved=0` (`after/c1-after.txt`).
  Verdict: **verified as stated**; the wave added two narrowing notes (Amendments 1–2) and one refutation
  (Amendment 3).
- **C2.** Commands: `python3 -B corpus/evidence/round89/curation-r89.py --root .`;
  `... curation-r89-controls.py --root . --work <scratch>`; `... curation-r89-mutants.py --root . --work <scratch>`.
  **Before**: the round-88 counter on the same tree prints `CURATION_R88=PASS` with no `DUPQID` leg, no field-derived
  verdict and a dead superseder clause; it accepts the duplicate-qid cite and the superseder-clause mirror
  (`PRIOR_ACCEPTED_FORGERY=7/7`). **After**: `CURATION_R89=PASS`, `DUP_QIDS=0 WARRANT_OK=17/17 QUOTES_LOCATED=20/20
  TEACHES_FLAGGED=1 TEACHES_UNRESOLVED=0 SUP_CLAUSE_CHECKED=0 SUP_UNRESOLVED=0 VERDICT fields_hold=1`; controls
  `CONTROLS=PASS FORGERY_REFUSED=7/7`; mutants `MUTANTS_KILLED=6/6 COUNTER_DETECTED=5 BATTERY_DETECTED=1`
  (`after/c2-after.txt`). Verdict: **verified as stated on the narrowed wording of Amendment 1** (the verdict
  conjoins the field derivation with the leg accounting; it is not a parse-back of the rendered line).

## Sources & frontier

`SOURCES: registry rows before→after 218 → 218` (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ 218 at both revisions). No row was opened for the first time; **two rows were re-opened from committed bytes this
round** and their `used-by` cells extended old→new: `S216` (`…round86/claims.md, …round87/claims.md` → the same plus
`corpus/evidence/round89/claims.md`) and `S218` (`…round87/claims.md` → the same plus `…round89/claims.md`). No other
cell moved: `git diff f8fa55ec ac0a0892 -- corpus/SOURCES.md` is `1 file changed, 2 insertions(+), 2 deletions(-)`,
both in the last cell, and `corpus/evidence/round89/controls/receipts/registry-cells.txt` carries the base/freeze
`git show` of the S218 row.

Counting command, run at round start and round end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`
→ exit 0 at both, same five pre-existing `W04` warnings (`census-start.txt`, `.ufo/waves/round-89/census-end.txt`).

Rows added by tier: 0/0/0. Rows touched old→new: S216 and S218 `used-by` only. Frontier rows advanced: none — the
round's ground is instrument repair, and the lesson says so instead of counting a row as expansion.

Assimilation: **none**. No `merge/chousa/` byte was consumed: the scout re-measured the campaign package's id set
against the lane registry and reports the collision unchanged (`R89ScoutRegistry`), and no `considerthese/` proposal
was opened this round (`corpus/lessons/round-89.md` `## Gate` says why).

Tooling: nothing installed this round (stock `python3` + `git` only); the pacman pause was respected by not installing
anything.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Trend verdicts

- **expansion: unchanged** — `ls corpus/knowledge/*.md | wc -l` is 97 at both revisions; the registry is 218 rows at
  both, and the round adds no row and no entry. The two `used-by` extensions are provenance bookkeeping, not ground.
- **quality: improved** — two instruments carry seven routed repairs, each with a failable witness: the four
  round-88 survivor shapes die on named lines (`UNRECONCILED D1_WIDTH detail=3/3/1 pin3`, `UNRECONCILED MUT_ADMIT
  detail=derived=0 killed=0`, `UNCROSSCHECKED … DIV3=1`), a dead detector and a detached leg now fail the curation
  verdict, the duplicate-qid cite is refused, and the superseder clause is reachable with a measured mirror. Four
  criteria mined (QUALITY 190–193); `tools/lane-preflight.py` `PREFLIGHT=8/8`; gate selftest `PASS (283 cases)`.
- **discernment: improved** — the wave fired the *sentence* rather than the predicate (Amendment 1), the lane published
  the two by-construction conjuncts as seams (Amendment 2) instead of letting them read as live checks, and it
  refuted one reviewer finding against committed bytes rather than accepting or ignoring it (Amendment 3). Four of
  this round's own errors — including the single-point mutant that proves nothing and the mirror id that collided
  with a real row — are mined with fixes shown able to fail.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  `SKILL.md` Gates table; `corpus/knowledge/metadata-screen-r25.md` (lane assertion; no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  `LOG.md` Round 9 archive verification; `corpus/fixtures/archives-r9/`; r25 explicit-root hold battery (lane assertion)
- [~] Instructions executable by an agent without oral context
  `bash tools/research-gate.sh --selftest` → `PASS (283 cases, 0 skipped)`; `python3 -B tools/lane-preflight.py` →
  `PREFLIGHT=8/8` (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  `PROVINCE.md`; `R89ConnectorSiblings` reports zero sibling ownership overlap for both instruments (lane assertion)

## Process notes

- Round shape: one v1 wave of 12 seats under `ufo-wave-policy.json` (band 8–16); roles 4 executor, 2 reviewer,
  1 critic, 1 mutation-tester, 1 sentinel, 1 scout, 1 connector, 1 scribe. Attack share 7/12 = 58% (two reviewers,
  the critic, the mutation-tester, the sentinel and the connector's overlap scan; the two forge executors are
  additional adversarial seats). Residual calls: none. Round total 12 seats.
- Planner seat: the L1 held it in-session (no planner seat dispatched, per the run-7 ruling); the bounded planning
  data-walks rode the scout and connector items.
- Frozen claims were not edited after the freeze; the two narrowing findings live in `plans/round-89.md` amendments
  1–2 and the ledger points at them, per the addendum §8 rule that a narrowing is an amendment in the plan.
- Pre-file falsification gate (addendum §8, Amendment 59):
  `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane chousa --round 89` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=17 attack_seats=6 findings=0`, exit **0**. The ledger carries exactly
  one row per (claim, seat); six attack seats appear (`R89ReviewerC1`, `R89ReviewerC2`, `R89CriticClaims`,
  `R89SentinelScope`, `R89MutBattery`, `R89ConnectorSiblings`).
- Control-receipt discipline (round-88 routed defect 5):
  `bash corpus/evidence/round89/controls/run-controls.sh <lane> <scratch>` → `RECEIPT_OK` on all eight rows and
  `CONTROL_RECEIPTS=PASS`, exit **0**.
- Wave settlement: `WAVE-DONE chousa r89 w1` from the orchestrator; `.ufo/waves/round-89/w1-results.json` records
  `seats=12`, 12 reports on disk, **0 dead**. The results file's `output` fields are `null` with the kernel's note
  that it restarted mid-wave and did not retain seat stdout; every seat's report and receipts are in
  `.ufo/waves/round-89/w1/`, and the ledger's artifact column points at them — so the wave's adversarial output is
  the committed files, not a transcript. Recorded here rather than hidden.
- Census (round end): `sources-census.sh validate --root <fleet> chousa` → exit **0**, 218 rows, same five
  pre-existing `W04` warnings (`.ufo/waves/round-89/census-end.txt`, `# computed_against=ac0a0892…`).
- Straight line committed through the lane helper (`jj-lane.sh`); only the pushed hashes at
  `git ls-remote origin refs/heads/master` are cited. Lane HEAD at filing:
  `a72f204bfeea10fc59497e23bcbda021a1a2ced5`, `ls-remote` identical, `ahead=0 behind=0`, working tree clean.
- The wave's attack seats fired on **sentence wording and control discipline**, never on a measured predicate: the
  frozen predicates print PASS at the freeze and at the tip, and every amendment names the artefact that fired.
- Carried debt named, not repaired backwards: the round-74 source-blind order oracle; QUALITY 173's
  successful-refused record form; the r80 backlog Gate ids; this round's control-discipline package (Amendment 7);
  the unbound `LEGS_MEASURED` cell and the unprinted `VERDICT` token (Amendments 4 and 8); C2's
  measurement-substitution exposure (Amendment 9). Each is a round-90 route, not a claim. Purpose: close the round.
