# kotoba — round 89 (attempt 1)

Lane: `kotoba-shokunin` (prompt & skill craft). Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`, pushed: `refs/heads/master` = `07d87d89fd2512022c6b2b3bf28e3b8aa80bb03f` (`git ls-remote origin refs/heads/master` at report time; `jj-lane.sh state` → `ahead=0 behind=0 tracked=0 untracked=0`). Host: Linux 7.2.11, omp 18.15.0. Lane HEAD cited below is the branch tip at measurement, `99ddd746` (landing content), with the settlement commit `07d87d89` on top.

## Work performed

**Declared claims (2; both on distinct axes; one is the lowest owned axis).**

- **C1 — depth (score 9, owned lowest; claim type: capability).** A pre-freeze control executor: `verifiers/check_freeze_gate.py` runs every control a plan declares under `## Controls` and refuses a declared expectation (exit code, required stdout literal) that the observed result contradicts. Frozen predicate: `plans/round-89.md` § C1 (its sentences unchanged after the freeze; amendment `plans/round-89-addendum-1.md` A2).
- **C2 — consistency (calibration sub-axis, score 10).** The routed-repairs gate D5 at instance level: `verifiers/check_r86_routed_repairs_v3.py` compares each integrity check's value and detail entries against a base receipt pinned at a clean freeze commit (`plans/round-89.md` § C2; amendment `plans/round-89-addendum-1.md` A1).
- **Frontier step (§2b):** two sourced rows (S258 external, S259 own-work), two knowledge entries, one lesson with `## Gate`, `## Mistakes` (4 rows), `## Sources`, `## Assimilation: none`, `## Considerthese`. Assimilation: none (55 id collisions, re-derived). Considerthese: reviewed, none taken.

**Protocol and process (evidence in order).**

- Load order read: `skill://shokunin`, kimi `SKILL.md`, PROTOCOL / MISSION / AXES / CORPUS / LEARNING, lane `SKILL.md`, `SCORECARD.md`, `PROVINCE.md`, `corpus/QUALITY.md`, `corpus/README.md`, `corpus/lessons/round-88-verifier-spotcheck.md` (routed defects 1–6), `plans/round-88*.md`, the r88 wave records. Fresh-start reading recorded in `plans/round-89.md` (run-15 authorization "Authorize all").
- Plan draft and freeze protocol committed before dispatch: `43fc7840` (predicates, targets, controls, kill rules; before-state receipts `.ufo/waves/round-89/receipts/{census-before,before-c1-absence,before-v2-selftest}.txt`, assimilation id guard `.ufo/waves/round-89/assimilation/`).
- Dispatch evidence: `0f2b8668` (`.ufo/waves/round-89/r89-w1-{spec,dispatch,plan}.*`, `r89-w1.ready`, `r89-w1.ready.dispatched`, `gen-w1.py`). Validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16); spawned by the orchestrator inline handoff; **WAVE-DONE `r89-w1` received** (`r89-w1-results.json`, 12 seats).
- Seat outputs (lane-relative): `.ufo/waves/round-89/w1/` — ScoutSource (S258/S259 records), ExecFreezeGate, ExecD5Gate, ExecCtlWorlds, ReviewerFreezeGate, ReviewerD5Gate, CriticFalsify, MutTesterGates, Connector.
- Pre-score amendments from the critic and reviewer findings (all recorded before the freeze receipt): D5 A1.1–A1.6 (location class, detail identity, record-blob pins, clean-tree refusal, receipt self-digest, GIT_DIR-class env scrub); freeze gate A2.1–A2.3 (stdout literal required; the C1 headline bounded); A1.7 (the `w_healed` control re-derived; see Landed changes).
- Freeze: `39704adc` (first freeze commit; corpus, instruments, plans); freeze revision **`12f4b6b9`** (adds wave evidence only: `git diff --name-status 39704adc 12f4b6b9` lists `.ufo/waves/round-89/{controls,receipts}` only). The lane-written freeze receipt names `12f4b6b9`.
- Controls at the freeze (builder `.ufo/waves/round-89/controls/build-controls.sh`, lane-shaped worlds under scratch, removed on exit): `f062a563`.
- Landing content `99ddd746`; settlement and landing measurements `07d87d89`.

**Round shape.** One v1 wave, `r89-w1`, 12 seats: 1 scout, 3 executor, 3 scribe, 2 reviewer, 1 critic, 1 mutation-tester, 1 connector. Attack seats 4 of 12 (33 %, ≥25 %). Connector 1 (≤2). Planner: held by the L1 (the validator excludes `planner`, as recorded in r88). No residual call, no resend, no second wave. Seat routing is the operator's `task.agentModelOverrides`; the results file records no answering model per seat, so no per-seat model claim is made.

**Seat accounting.** `r89-w1-results.json` carries `output: null` for every seat ("orchestrator kernel restarted mid-wave; seat output was delivered to the orchestrator session but not retained"); seat outputs were read from the wave directory instead. Seats that left **no landed artifact**: ScribeEntry-19 and ScribeLesson-50 (no output directory under `.ufo/waves/round-89/w1/`) and ScribeSources-26 (receipts only, no registry rows). The L1 performed their work (both knowledge entries, the registry rows, the index rows, the lesson) and says so in `corpus/lessons/round-89.md` § Seat record. No seat is counted as delivering the corpus content. The wave evidence records no per-seat provider-error text, and it does not establish why the three scribe seats left no artifact; the report assigns no cause.

## Landed changes

Every change, with its LOG entry and landing commit (`plans/round-89.md`; `corpus/lessons/round-89.md`; LOG `## Round 89 — freeze entry` and `### Round 89 — landing settlement`):

| change | file(s) | commit | LOG entry |
|---|---|---|---|
| freeze gate (C1 instrument, 30 self-test assertions) | `verifiers/check_freeze_gate.py`, `verifiers/fixtures/freeze-gate/*` | `39704adc` (content), `12f4b6b9` (evidence) | freeze entry |
| instance-level D5 v3 gate (C2 instrument, 37 self-test assertions) | `verifiers/check_r86_routed_repairs_v3.py`, `verifiers/fixtures/d5v3/fixture_integrity.py` | `39704adc` | freeze entry |
| floors row for the freeze gate | `verifiers/floors-registry.json` | `39704adc` | freeze entry |
| plan + pre-score addendum (A1.1–A1.7, A2.1–A2.4) | `plans/round-89.md`, `plans/round-89-addendum-1.md` | `43fc7840`, `39704adc` | freeze entry |
| SOURCES rows S258 (external, PMC5856500, tier A scoped) and S259 (own-work, tier A scoped) | `corpus/SOURCES.md` | `39704adc` | freeze entry |
| knowledge: freeze gate; instance-level D5 | `corpus/knowledge/freeze-gate-round89.md`, `corpus/knowledge/instance-d5-round89.md` | `39704adc`; rewritten `99ddd746` | landing settlement |
| lesson with `## Gate`, `## Mistakes` (4 rows), `## Sources`, `## Assimilation: none`, `## Considerthese`, `## Seat record` | `corpus/lessons/round-89.md` | `39704adc`; `99ddd746` | landing settlement |
| criterion Q81 (filed round reports are immutable) | `corpus/QUALITY.md` | `39704adc` | freeze entry |
| coverage-map index rows: two round-87/88 spot-checks that were unindexed (`unindexed 2` → 0), plus three round-89 rows | `corpus/README.md` | `39704adc` | freeze entry |
| registry rows for both instruments; SKILL.md at 600 lines (one blank line removed, two wrapped intro lines joined, to stay within the 600-line box) | `SKILL.md` | `39704adc`; pinned-path cells corrected `99ddd746` | freeze entry; landing settlement |
| SCORECARD: round-89 axis annotation; capability row `freeze-gate execution of declared controls` (first working round 89) | `SCORECARD.md` | `99ddd746` | landing settlement |
| control builder and final control receipts | `.ufo/waves/round-89/controls/*` | `12f4b6b9`, `f062a563` | freeze entry; landing settlement |
| wave evidence | `.ufo/waves/round-89/w1/*`, `receipts/*`, `assimilation/*` | `0f2b8668`, `12f4b6b9`, `43fc7840` | freeze entry |

Routed or changed after the freeze, disclosed: (i) `w_healed` re-derived as an isolating heal (addendum A1.7; the wave-era `w_healed` repaired a pinned record and was unsatisfiable under the amendment, which is recorded as a mined mistake); (ii) registry pinned-path cells corrected from directory/glob to literal paths (registry-form correction; no predicate or gate byte changed; verified below). The kill-rule check `git diff --stat 12f4b6b9 07d87d89 -- verifiers verifiers/fixtures plans` prints nothing.

## Before → after measurements

Counting commands and commits. Landing measurements are in `.ufo/waves/round-89/receipts/landing-measure.txt` (measured revision `99ddd746`).

**C1 — freeze gate (depth).**

- Before: no instrument. `git grep -n 'freeze_gate\|freeze-gate' -- verifiers plans` at `a5b3b15c` → exit 1 (`.ufo/waves/round-89/receipts/before-c1-absence.txt`). The round-88 declaration `w_added_red` (expect `exit 0; stdout contains D5=FAIL`) shipped unexecuted.
- After at `99ddd746`: `python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls.md` → `REFUSED control w_added_red (line 36): declared "exit 0; stdout contains D5=FAIL"; observed exit=0 stdout=w_added_red D5=PASS`, **exit 1**. `… --plan r88-controls-fixed.md` → `freeze gate: 4 control(s) held`, **exit 0**. `… --self-test` → `0 failure(s) over 30 assertions`, **exit 0**.
- Predicate verdict: all three arms met on the frozen predicate. The mutation leg is **carried**: the battery (`.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv`) ran on pre-A2 bytes and is not re-run.

**C2 — D5 instance level (consistency).**

- Before (frozen v2 gate = do-nothing control): tip `python3 -B verifiers/check_r86_routed_repairs_v2.py --rev 12f4b6b9 --repo <tip>` → `r86 routed defects closed 5 of 5`, exit 0; added-instance world (one lesson line citing an unresolvable hash) → `closed 5 of 5`, **exit 0** (blind). v2 `--self-test` → `1 failure(s) over 16 assertions` (the frozen `w_added_red` arm). Records: `controls/v2-before-tip.txt`, `controls/v2-before-addinst.txt`, `.ufo/waves/round-89/receipts/before-v2-selftest.txt`.
- After (v3 at `99ddd746`, receipt `12f4b6b9`): `python3 -B verifiers/check_r86_routed_repairs_v3.py --base-receipt .ufo/waves/round-89/receipts/d5v3-base-receipt.json` → `r86 routed defects closed 5 of 5`, `instance drift 0`, **exit 0**; `--self-test` → `0 failure(s) over 37 assertions`, **exit 0**.
- Controls (same gate): `w_tip` 0 ✓; `w_healed` 0 ✓ (`closed 5 of 5`, drift 0); `w_added_instance` **1** ✓ (`FAIL d5iii`, `instance drift 2`); `w_silenced` 1 ✓ (`FAIL d5i`, `FAIL snapshot_tampered`); `w_rerecorded` 1 ✓ (`FAIL snapshot_tampered`); equivalence lane vs lane-shaped clone identical ✓. Records `controls/final-*.txt`, `controls/equivalence.txt`.
- Predicate verdict: the frozen predicate (`exit 0 iff N == 5 AND K == 0 AND digests match`) is met at the landing revision, and v3 discriminates the world the round-88 gate could not see.

**Integrity (the corpus gate's observation; not a claim target, measured because D5 reads it).**

- `python3 -B verifiers/verify_corpus_integrity.py` at `a5b3b15c` (base, scratch clone) → 5 DRIFT names (`.ufo/waves/round-89/controls/base-a5b3b15c-write.txt`: "9 names, 5 DRIFT"). At `99ddd746` → 4 DRIFT names: `corpus.index.tracked_files`, `corpus.pointers.report_total`, `corpus.pointers.commit_total`, `corpus.pointers.commit_unresolvable`. `corpus.index.unindexed` 2 → 0; `corpus.index.stale_patterns` 0.
- The round-base receipt judged on the freeze tip reads exit 1 (`tracked_files 180>177`, `report_total 144>141`): the round's own three new corpus files, disclosed as informational (`controls/final-info_round_base_vs_tip.txt`).

**Sources.**

- `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: **183 → 185**. Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`: **exit 0** before (`census-before.txt`) and at `99ddd746` (`landing-measure.txt`). Duplicate-URL warnings (W04) pre-existing and unchanged.

**Registry and budget.**

- `python3 -B verifiers/check_gate_registry.py --rev 99ddd746` → `gate registry rows conformant 73 of 73 lane verifiers; phantom 0`, exit 0. (Before: the round-88 record reads `71 of 71`; not re-measured at `a5b3b15c`.)
- `SKILL.md`: 600 lines before and after (`trigger.line_budget` PASS, 600 within budget).

## Sources & frontier

- **SOURCES rows before → after:** 183 → 185 (command above). Rows added by tier: **A: 2** (S258 external, tier A scoped to the preregistration-before-data principle; S259 own-work, tier A scoped to the round-88 requirement record). Tier B/C: 0. Rows touched old→new: **none** (no `status`, `recheck` or `used-by` change to an existing row).
- Sourced claims: S258 — admitted with located quotes (HTML lines 1451 and 1472 of `pmc.ncbi.nlm.nih.gov/articles/PMC5856500/`, access 2026-11-05, sha256 `ee0d0560…f51`); the critic re-matched both lines and the sha256 (`.ufo/waves/round-89/w1/CriticFalsify/attacks.md` § 4). The PMC5813543 route was rejected (a different article, `.ufo/waves/round-89/w1/ScoutSource/SOURCE_ROW.md` route ledger); routes (b)/(c) returned HTTP 403. The lane's inference "a control whose expectation cannot be observed is not a confirmation" is labelled as the lane's, not the paper's.
- Frontier rows advanced: coverage map +5 rows (two knowledge entries, the round-89 lesson, two previously unindexed round-87/88 spot-checks). `corpus/README.md` § Frontier not edited.
- Mistakes mined (lesson `## Mistakes`): (1) report immutability (Q81); (2) the MERGE-REPORT count (named artifact and command: `wc -l MERGE-REPORT.md` → 155; `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' SOURCES.append.md` → 188); (3) the unsatisfiable `w_healed` control (a repair of a pinned record); (4) the base-to-tip growth read as a heal.
- Assimilation: **none.** `/home/vgpnk/Projects/shokuknow/merge/kotoba/` re-read (read-only): reg 183 ids, staged 188, **collisions 55** (`.ufo/waves/round-89/assimilation/collisions`). Not adopted; L0 `kotoba | round-88` open.
- Considerthese: `considerthese/2026-10-26.md` read; proposal 4 applied as Q80 in this round's wave design; none taken as a claim (2 is blocked by L0 `kotoba | round-73`; 3 and 5 do not fit the claim cap).

## Trend verdicts

- **expansion — `improved` (provisional).** Two admitted knowledge entries on uncovered ground (freeze-gate execution of declared controls; instance-level D5 against a receipt), each `source:` citing a `mined` row (S258; S259). Provisional because the non-author spot-check is pending (see Open below). Evidence: `corpus/knowledge/freeze-gate-round89.md`, `corpus/knowledge/instance-d5-round89.md`, SOURCES rows.
- **quality — `unchanged`.** No admitted entry failed a re-check; none superseded. Routed defects 1 and 5 of the round-88 spot-check are answered (Q81; the MERGE-REPORT count correction), and two unindexed corpus files are now indexed (gate `unindexed` 2 → 0). Evidence: `corpus/lessons/round-89.md` § Mistakes; `corpus/README.md`.
- **discernment — `unprovable-but-better`.** The lane's own gates caught, before any candidate score, an unsatisfiable freeze control (r88 F1 class, reproduced mechanically by the freeze gate), a dirty-tree receipt path, an exit-only declaration, and a Q79 location flip (critic N1–N10, reviewer F1–F3, addendum 1). The change is measured as better (before: unexecuted control shipped; after: refused). No non-author reviewer is on record for this round: the reviewers and the critic are seats this lane dispatched, so the judgment is not a non-author verdict. Named reviewer pointer for the closure: `corpus/lessons/round-89.md` § Gate (S258 and S259 quotes) and the freeze gate's attack fixtures (`.ufo/waves/round-89/w1/ReviewerFreezeGate/`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  evidence: `SHONEN.md` (round-88 pointers, unchanged this round); this round adds two gate registry rows to `SKILL.md` § Gate registry (`check_gate_registry.py --rev 99ddd746` → 73 of 73).
- [~] At least one end-to-end domain task executed and logged in LOG.md
  evidence: `corpus/knowledge/cold-run-round11.md` (per `SHONEN.md`, unchanged); this round's end-to-end run of both new instruments at the freeze and landing is logged at `LOG.md` § Round 89 landing settlement.
- [~] Instructions executable by an agent without oral context
  evidence: `corpus/lessons/round-8-aggregator-box3-coldrun.md` (per `SHONEN.md`, unchanged); the new `verifiers/check_freeze_gate.py` and `verifiers/check_r86_routed_repairs_v3.py` run from the repo root with the commands in `SKILL.md` § Gate registry.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  evidence: `PROVINCE.md` § Adjacent (round-74 census, `corpus/knowledge/sibling-overlap-census-round74.md`, unchanged this round); the connector's sibling scan for freeze-gate/D5 ground is `.ufo/waves/round-89/w1/Connector/overlap.md`.

No `[x]` box: no non-author verifier has checked a box this round.

## Open, routed, and disclosed

- **Non-author closure pending:** the spot-check (LEARNING discernment: one admit and one reject) and the verdicts above are the closure's to give. Admission is not claimed here.
- **Carried:** the C1 mutation battery on pre-A2 bytes; the D5 population is corpus `*.md` only (addendum A1 bound; a dead citation in `LOG.md` is a named residual).
- **Integrity reds left honest:** `pointers.commit_unresolvable` = 1 (`corpus/lessons/round-81.md:8`, pinned record, Q64); `tracked_files` and `report_total`/`commit_total` counts reflect the round's own additions by design (the baseline is not re-recorded).
- **Pre-existing red, not introduced:** `verifiers/verify_skill_checklist.py` → one FAIL, `governance.citation_resolves` (dead historical LOG citations); red at `a5b3b15c` too (measured in a scratch clone).
- **Frozen do-nothing control stays red:** `verifiers/check_r86_routed_repairs_v2.py --self-test` → `1 failure(s) over 16 assertions` (`w_added_red`), kept as the recorded control; not repaired.
- **Routed to round 90 (not repaired):** duplicate control names in the freeze gate (documented invalid, processed as re-runs; A2.4); the `report_dead` symlink class (Q79 location flip); the mutation battery re-run on final bytes.
- **L0 questions open, not answered by the lane:** `kotoba | round-88` (assimilation renumber-or-retire; C1 kill ruling), `kotoba | round-73` (gate-registry home).
- **Host incident need (named, not acted on):** on 2026-11-05 `user.max_user_namespaces` was set to 0 by wave seats, and every bwrap sandbox then failed with ENOSPC. This lane's wave context forbade sysctl writes (`/proc/sys`, `sysctl -w`). The lane did not run sudo or change any host sysctl. The need: a sandbox runtime whose configuration does not write kernel parameters at run time, so that seats can run sandboxed commands without a host-level change.
- **Tool installs:** none this round.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` → only `M .scratch/run15-state.json` (orchestrator-owned; not touched). No seat file was written at the fleet root; no misroot to copy.
- **Stale-lane:** no other mission of this lane is open.
- **Wave-file hygiene:** the wave's `gen-w1.py` (spec generator) and `r89-w1-results.json` are committed as wave evidence.

**Commits cited (all ancestors of the pushed `master`):** `43fc7840` (plan draft), `0f2b8668` (dispatch), `39704adc` (freeze commit), `12f4b6b9` (freeze revision), `f062a563` (controls), `99ddd746` (landing content, measured revision), `07d87d89` (settlement and landing measurements; lane tip).

**Pre-report gate:** `git ls-remote origin refs/heads/master` = `07d87d89fd2512022c6b2b3bf28e3b8aa80bb03f` = the lane tip.
