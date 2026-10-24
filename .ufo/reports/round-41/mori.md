# mori — round 41 report

Lane: mori-shokunin (fleet/host observability 森). Round: 41, attempt 3 of 3
(attempt 1 dead session post-freeze pre-report; attempt 2 Devin rate wall
post-dispatch pre-report). Lane tip at report: `46275ca4ed2f07a72d9707709f92be19ab7dca1a`
(pushed, `ahead=0`). Attempt lineage: r40 closure `62a207f7` → `d72ac16`
(attempt-1 freeze) → `aa161e99`/`c5326c61` (attempt-2 claim work) → `7450722e`
(attempt-2 receipts + declaration) → `46275ca4` (this attempt's evidence commit).

## Work performed

Declared claims (contract `.ufo/waves/round-41/contract.md`, frozen at attempt 1,
pins `evidence/freeze-r41.txt` — 19/19 re-verified byte-exact at `7450722e` by
attempt 2 (`freeze-verify.txt`) and again at tip by attempt 3
(`evidence/freeze-verify-attempt3.txt`)):

1. **C1 — operability 7 (capability acquisition):** conformance binding model v4
   (P-C10 r41) — source-ordered function-local binding inventory
   (`Assign`/`AnnAssign`, `NamedExpr`, tuple/list destructuring, for/with targets);
   fail-closed on unresolved targets, unsupported stores, `global`/`nonlocal`
   rebinds, disagreeing multi-bindings. Closes r40 routed defect 1 (C1 falsified by
   the new-survivor class); sourced S230.
2. **C2 — depth 5 (tied lowest, capability acquisition):** append-only gate P-C12 —
   eligible pair = both rows present at R; per-commit header maps; ancestry-grounded
   landing selection (maximal candidates; superseder-id then hash tie-break);
   delete/re-add = new landing; never-edited edit = first-sighting commit. Closes
   r40 routed defects 2a–c (C2 falsified by DAG counterexamples).
3. **C3 — calibration 5 (tied lowest):** append-only correction records reconcile
   the r40 self-assessment (34 as-of/16 extension) to the frozen r40 gate's 35/17.
   Closes r40 routed defect 3 (correction-layer number-drift).

Work items (attempt 3 unless noted; evidence pointers lane-relative):

- Re-verified all inherited attempt-1/2 bytes before reuse: 19/19 freeze pins at
  `7450722e` (`.ufo/waves/round-41/evidence/freeze-verify-attempt3.txt`);
  named discard: none — every inherited byte reused was re-verified.
- Re-ran all three counters live in a disposable sandbox clone at the tip
  (commands in Before → after below; frozen-target results reproduced exactly).
- Dispatched-wave inheritance: attempt 2 spawned the 64-seat v2 wave
  (`evidence/wave-run.json`, spawn=64, policy v2 band); 19/64 seat reports
  returned before the session died and are now committed under
  `.ufo/waves/round-41/w1/` (registry `w1/swarm-registry.json`).
- Receipt repairs from w1 scribe findings: `evidence/census-end.txt` regained its
  command/exit header and manual row-count (`ROWS=231`; finding F2);
  `evidence/calibration-after.txt` re-issued with the measured-revision header
  (finding F3) — counter values byte-identical to the attempt-2 receipt.
- Lesson-layer adjudication (w1 scribe drafts vs landed rows): appended M27
  (count-universe conflation) and M28 (silent-survivor, the r40 C1 falsification
   class) to `corpus/lessons/round-41.md` with fresh ids — no landed row rewritten;
  recorded the M-id collision resolution; appended the S230 located-quote erratum
  (landed Gate text said "22 words"; measured 34 tokens; corrected 20-word
  verbatim quote at `S230.src:301-303`).
- M27 fix demonstrated able to fail: in the sandbox, committing the r40 lesson
  record drifted to `observed_as_of=36` makes the frozen counter report
  `mismatches=1` exit 1 (probe commit `d4475417…`, disposable, never pushed).
- Frontier step: SOURCES.md census 229 → 231 rows (S230, S231 admitted, tier A);
  knowledge entry `corpus/knowledge/conform-bindings-r41.md`; source copies
  `corpus/evidence/sources-r41/{S230,S231}.src`; mistakes M25–M28 on record.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
  only `.ufo/state/*` driver files (untouched) and pre-existing Oct 22–23 HTML
  strays (`bm.json`, `live.html`, `live_s228.html`) that predate round 41 and
  name no mori r41 content — left untouched. No seat files landed at fleet root.

## Landed changes

All under lane commits (jj helper, `mori-shokunin <mori@shokunin.local>`; branch
tip `46275ca4ed2f07a72d9707709f92be19ab7dca1a`, pushed):

- `7450722e` (attempt 2, reused after verification) — after-measurement receipts
  `evidence/{control-after,calibration-after,census-end}.txt`, SCORECARD r41
  declaration, lesson fix — LOG.md "Round 41" entry §C1–C3.
- `46275ca4` (attempt 3) — `LOG.md` + `SCORECARD.md` attempt-3 notes;
  `corpus/lessons/round-41.md` (M27, M28, adjudication, S230 erratum);
  `evidence/census-end.txt` (repaired), `evidence/calibration-after.txt`
  (re-issued), `evidence/freeze-verify-attempt3.txt` (new),
  `evidence/wave-run.json` + `evidence/wave-run.stderr` (dispatch record),
  `.ufo/waves/round-41/w1/` (19 seat reports + registry) — LOG.md attempt-3
  paragraph names each.
- Earlier attempt-2 claim commits reused after verification: `aa161e99`
  (C3 correction records 35/17, S230/S231 copies, freeze-verify + attempt-1
  receipt, round-22 stray resolution), `c5326c61` (single-line calibration
  records), `d72ac16` (attempt-1 freeze: contract, conform.py, both tools,
  fixtures, extracted v3 bytes, w1-spec).
- Not edited (external, named): `corpus/lessons/round-40-verifier-spotcheck.md`
  (r40 closure), `.ufo/state/*`, fleet `templates/`, `scripts/`, MANIFEST.json.

## Before → after measurements

Counting commands over committed bytes in a disposable clone whose HEAD equals the
measured revision (`46275ca4` final tip; `7450722e` identical results — receipts
committed at both layers):

- **C1 (operability):** before — `python3 fixtures/extracted/conform-v3-r40.py`
  (frozen r40 v3 bytes) prints `CONFORM=met` exit 0 on each of the three routed
  survivors (`evidence/control-before.txt` §C1). After —
  `python3 .ufo/waves/round-41/conform.py 46275ca4… --repo . --contract .ufo/waves/round-39/contract.md --counter <fixture>`:
  honest counter `CONFORM=met` exit 0 (all nine checks PASS); each of
  walrus/tupleunpack/deadloop survivors `CONFORM=unmet` exit 1 with **only**
  `timeout_scope` FAIL (`evidence/control-after.txt` §C1; re-run live by attempt 3
  at `7450722e` and `46275ca4`). No-harm guards: `--selftest` →
  `CONFORM_SELFTEST pass=14 fail=0` (re-run live, 67s); early-continue mutant fails
  `selftest_conjunct` only (receipt §"C1 after early-continue", EXIT=1).
  Frozen target `survivor_failures=3` — met; do-nothing control cannot reach it
  (v3 bytes pass all three survivors, `control-before.txt`).
- **C2 (depth):** before — frozen v3 gate fabricates dag-h changes, misses dag-h2's
  pair, times dag-z/z2's absent superseder, flips dag-2l on commit date, misses
  dag-x's re-add landing (`evidence/control-before.txt` §C2). After —
  `python3 tools/mori-sources-appendonly.py --selftest` →
  `MORI_SOURCES_APPENDONLY_SELFTEST pass=22 fail=0` (live, exit 0); lane line at
  tip: `supersede_timing superseded_as_of=[36 ids incl. S229] stale_supersede=[]`;
  at `e37dcc6`: `stale_supersede=[S069]`; all seven routed DAG fixtures print the
  P-C12 verdicts (`evidence/control-after.txt` §C2; live re-run of selftest + lane
  line + e37dcc6 by attempts 2 and 3).
- **C3 (calibration):** before — `python3 tools/mori-round41-calibration.py 62a207f… --repo . --reference-rev 62a207f…` → `mismatches=6` (`control-before.txt` §C3). After — same counter at tip → `MORI_R41_CALIBRATION mismatches=0 observed_as_of=35 extension_rows=17` exit 0 (`evidence/calibration-after.txt`, re-issued with measured-revision header; live at `7450722e` and `46275ca4`). Able-to-fail: drifted record probe reports `mismatches=1` exit 1.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` — start exit 0, `ROWS=229` (`evidence/census-start.txt`); end exit 0, `ROWS=231` (`evidence/census-end.txt`, repaired receipt). Same 16 pre-existing W04 duplicate-URL warnings both ends; no new warnings.
- Rows added by tier: **tier A +2** (S230 Python 3.13 §7.2 assignment statements — grounds C1's binding inventory; S231 Python 3.15.1 §4.2.2 — located-quote correction superseding S229, 17 words at `S229.src:294-296`). No tier B/C rows.
- Rows touched old→new: none in place; S230/S231 added `queued`→`mined` at admission with `used-by` → `corpus/knowledge/conform-bindings-r41.md` (recorded in the lesson Gate).
- Frontier rows advanced: S230, S231 (opened, gated, mined, used this round). Knowledge entry `corpus/knowledge/conform-bindings-r41.md` cites both (sourced-claim requirement: C1 rests on S230/S231).
- Lesson erratum: S230 located quote corrected to a 20-word verbatim quote (see Work performed); registry immutable cells unaffected.

## Trend verdicts

- **Expansion — improved:** two tier-A sources admitted with committed copies and a new knowledge entry; the binding-inventory capability (C1 v4) and the P-C12 ancestry reading (C2) are new demonstrated capabilities recorded in SCORECARD's capabilities table; census +2 rows.
- **Quality — improved:** the r40 C1/C2 falsifications are repaired with frozen before/after receipts, a do-nothing control, a kill rule per claim, and a 14/22-arm selftest layer whose mutants are demonstrated killed (w1 mutation seats: 8/8 mutants killed); the r40 correction-layer number-drift is reconciled by a frozen counter (`mismatches=0`, able-to-fail shown).
- **Discernment — improved:** the round mined four mistake classes (M25 number-drift, M26 landing-without-copies, M27 count-universe conflation, M28 silent-survivor) including two surfaced by its own wave's scribes, and the lesson records the M-id adjudication rather than silently merging; the 35-vs-36 count tension is explicitly resolved as different revisions of one ledger, not competing measurements.

## SHONEN

- [ ] SKILL.md real decision tables, error patterns, checklists, cited sources — artifacts resolve (`SKILL.md:11` decision table, 169 rows; `corpus/knowledge/conform-bindings-r41.md`), but no named non-author verifier in-round.
- [ ] End-to-end domain task executed and logged — LOG.md round-41 entry + receipts resolve; same standing verifier gap.
- [ ] Instructions executable without oral context — contract Counter lines and receipt commands run verbatim from committed bytes (attempt 3 ran them in a fresh disposable clone); no independent non-author execution record.
- [ ] No cross-domain bleed; PROVINCE.md accurate — r41 work stayed inside the sources/census/conformance province; PROVINCE.md Adjacent table byte-unchanged; no verifier named.

(No box is ticked: promotion-level verification is the external non-author
closure's duty; wave seats sample but none is a named verifier for promotion.)

## Extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Wave shape:** ONE v2 wave (`mori-r41-v2`, policy v2 band 64–128, plan exit 0 at `evidence/wave-plan.json`), 64 seats: 22 scout, 12 reviewer, 11 critic, 8 mutation-tester, 7 scribe, 3 executor, 1 connector = 34 attack seats (53%); §3 L2 floor met inside the wave (planner seat held by L1 per orchestrator ruling; planning data-walk rode scout/connector items). 19/64 seats returned reports (1 connector, 3 executors, 8 mutation-testers, 1 reviewer, 2 scouts, 4 scribes — by role: attack seats returned 9/34); 45 seats died with the attempt-2 session — the wave runner's own stderr is empty (`evidence/wave-run.stderr`, 0 bytes) and no per-seat error text survives; the session-level cause per the dispatch record is the Devin free-tier rate wall (13:14Z, reset sliding) — dead seats stay dead in the evidence, per policy not replaced. No residual call (no ≥32 distinct attack items remained for a wave 2; the 19 returned reports were consumed by attempt-3 verification and the lesson adjudication). Round total: 64 seats.
- **Attempt-2 inherited uncommitted outputs** (`.ufo/waves/round-41/w1/`, `wave-run.json`, `wave-run.stderr`): reused after re-verification (seat reports cross-checked against committed receipts; ScrReport's findings F2/F3/F6 acted on), committed at `46275ca4`. Nothing discarded.
- **Tool installs:** none this attempt (no pacman — host-wide pause respected; nothing needed installing).
- **Open L0 questions:** none appended; none blocking.
- **Refusals:** none (no wave re-dispatch attempted — inheriting the dispatched wave was the verified-correct action).
