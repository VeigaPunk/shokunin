# tameshi — round 29 report (TameshiR29, attempt 1)

Final lane head (pushed): `3c16b3a649181b0dbfa386997de8c573f5bf7c3b`. Base: `367ec0f1d79cb9b67d724f2962e7554a0841b1fc`.
No lane commit lands after this report is filed (QUALITY 57).
Proposed verdict: **C1 verified (measured); C2 missed (honest stop)**. Because C2 missed, the round is not fully admitted.

## Work performed

Declared claims (2), frozen before data in `.ufo/evidence/round-29/contract.json` (`9f3084bc`). Both were re-frozen before any data seat, after the control wave: C2 in `contract-amendment-1.json` (`6ab11a62`) and C1 in `contract-amendment-2.json` (`09e4f273`).

- **C1, calibration** (lowest axis, 6; routed item 1 of `corpus/lessons/round-28-verifier-spotcheck.md`). Surface: SHONEN box 3 self-assessment against the cold-read ledger at the landed head, plus a binding of every new ledger entry to a round-29 seat report and registry member. Counter: `python3 .ufo/evidence/round-29/c1-measure-v2.py --repo CLONE --rev REV`, which runs a pinned monitor chain. Predicate `C1_R29_V2_PASS`.
- **C2, coverage, frontier F6** (never worked before; sourced on S024). Goal: a fixture built on the pinned kagi declaration that kills survivor B5, reduced by the counter's own ddmin to a 1-minimal fixture, plus an S024-sourced entry. Counter: `python3 .ufo/evidence/round-29/c2-measure-v2.py --repo CLONE --rev REV`. Predicate `C2_F6_V2_PASS`.

Work items:

- **Order fix (round-28 Mistake 1).** Every widely read input edit landed in `9f3084bc` together with the contract, before any cold read: S024 `queued→mined`, README Round-29 section (F8 wording correction and F6 pre-registration), QUALITY 55–57. Monitor at `9f3084bc`: 52/64 (`.ufo/waves/round-29/monitor-9f3084b-explain.json`).
- **Control wave**, before data (`.ufo/waves/round-29/ctl/`):
  - Call 1, 6 seats.
    - CtlC1Cheap K1–K4: `meets=no` for all four.
    - CriticC2Design met C2 v1 three ways: private controls `af694c1d`, `9ea4f2df`, `109fe613`, each PASS=true. C2 was re-designed as v2.
    - CriticC1Design found the C1 v1 executable identity unpinned. C1 was re-designed as v2.
    - CtlC1Shortcut and CtlC2Shortcut ended on a provider safety refusal (holds; see Gate).
  - Call 2, 2 seats.
    - CtlC2v2Port: V1–V7 all `meets=no`.
    - CriticC2v2 (Q5): the v2 target is unreachable. That report landed after the wave-1 dispatch (Mistake 1).
  - L1 re-score of the C1 controls under v2: `ctl/C1v2-rescore.txt`, all false.
- **Wave 1** (49 seats, policy v1, `.ufo/waves/round-29/spec-w1.json`, `dispatch-w1.json`).
  - 36 independent cold reads, three per drifted section, at `9f3084bc`. No read failed. 34 reports assembled into 32 entries; Read07A and Read10B were format rejects (`coldread/assemble-w1.out`).
  - 22 entries meet the frozen binding check and were appended (ledger 371 → 393, `git diff --numstat` `1781 0`) at `bc2058a4`.
  - 10 passing entries were not appended because they fail the frozen binding: 4 seat self-labels and 6 assembler-normalized verdicts. The list is in `.ufo/evidence/round-29/coldread/select-receipt-w1.json`. A dry run appending all 32 gave 64/64 but `bound=22`, PASS false (`coldread/c1-dry-all32.txt`).
- **C2 build.**
  - BuildF6B built the anchored original: census byte-identical to the pinned declaration, sha256 `4af0dbcc…`. The pristine gate reports only the exec-bit drift; the B5 mutant reports `(mode 644, declared 755)` and exits 1. A 512-mode sweep found no killing state (`.ufo/waves/round-29/w1/BuildF6B.md`).
  - BuildF6A was cancelled at the deadline, and its report landed later (`w1/BuildF6A.md`). It agrees. Its unanchored variant (declaration plus one probe row) reduces 100 → 2 units and kills, but `anchored=0`, so it is not counted.
  - Entry: `corpus/knowledge/survivor-fixture-minimization.md`. Finding: B5 is masked by the exact-mode check under the pinned declaration, because all exec rows declare 755.
- **Routed defects** of `round-28-verifier-spotcheck.md`:
  - (1) Done: C1 passes.
  - (2) S059 re-checked (`w1/ReopenS059.md`): the HTML is deploy-keyed and the markdown drifted. The supersedes row is deferred to round 30 as its first SOURCES edit, because an edit now would drift the restored credit.
  - (3) QUALITY 57; this report names the final head.
  - (4) README F8 corrected; QUALITY 55 amends 53/54. Runner leg-sum defect confirmed by MutateLegSum (`w1/MutateLegSum.md`; drop-a-status mutant prints `PASS (cases=9 passed=8 …)`, exit 0; unapplied diff). It is not applied because the runner is an input of most credited entries; routed to round 30.
- **Other wave-1 seats:**
  - CriticRound (`w1/CriticRound.md`): one blocking read vetoes passes.
  - ConnectorOverlap (`w1/ConnectorOverlap.md`): kake, kotoba, kagi and kumitate overlaps, report-only.
  - ScoutF6Next (`w1/ScoutF6Next.md`): 24 fixture-absent survivors ranked.
  - RegistryNoHarm (`w1/RegistryNoHarm.md`): `sources-census` row red at `9f3084bc` only (Mistake 2).
  - RerunCensusA, ReopenS024, ReviewR1Edits (two stale counter pointers in README/QUALITY, recorded in the lesson), ScribeEntryF6, ScribeMistakes.
- **Residual call** (8 attack seats, `.ufo/waves/round-29/res/`): RerunC1Head, CriticSelectBound, SampleBoundReads, RerunC2Head, ReviewEntryF6, CriticNoHarm, ReviewControls, ReviewLessonGate. Dispositions are in the lesson `## Residual review`. Four entry wording defects were corrected in `6892c3ee`.
- **Round shape:** default two-wave shape, with the second wave replaced by one residual call because fewer than 32 attack items remained.
  - Control calls: 6 + 2. Wave 1: 49 (reviewer 39, executor 4, scribe 2, mutation-tester 1, connector 1, scout 1, critic 1). Residual: 8 (reviewer 6, critic 2). **Round total 65.**
  - Planner seat: held by the L1. The planning data walk rode the scout ScoutF6Next.
  - Dead or held seats, never replaced:
    - CtlC1Shortcut and CtlC2Shortcut: `Codex error event: This content was flagged for possible cybersecurity risk … (code=cyber_policy)`.
    - BuildF6A: cancelled at the 02:47Z deadline, but the session kept running and rewrote its report. It was killed again at the 03:03Z freeze, and that last revision landed in `3c16b3a6`. Its processes had been killed earlier by BuildF6B (Mistake 4).
    - CriticC2v2: ended "without a final message", but its report exists.
- Misroot sweep: one fleet-root file, `.ufo/waves/round-29/w1/Read10C.md` (written by seat Read10C). Copied byte-exact into the lane (sha256 `fafd4c36…`, `cmp` clean), fleet copy deleted, recorded as Mistake 3. No other untracked fleet-root file names this lane.

## Landed changes

| Commit (landed, pushed) | Content | LOG.md entry |
|---|---|---|
| `9f3084bc60ad56aac01e4556ef4c7653df2f65e5` | contract, v1 counters, S024 snapshot, census start, all input edits (SOURCES, README, QUALITY 55–57) | "Round 29" bullet 2 |
| `6ab11a6274d6111deb2b31b2ba6b4f742603bd49` | C2 counter v2 + amendment 1, control receipts | bullet 3 |
| `09e4f273dd54edea382ea03f098eecb3628331c3` | C1 counter v2 + amendment 2, control receipts, wave-1 generator | bullet 3 |
| `bc2058a405fadfc1594c4ee764988902c09525ee` | wave-1 reports, traces, registry, assembly, 22 bound entries appended | bullet 4 |
| `7a45f7b9d6a2542a553276330c8b02ac2e28c7ef` | F6 fixture (anchored), entry, C1 receipt | bullets 4–5 |
| `9bb699ad2d9f795dff95df85eb967129c54927d6` | lesson, SCORECARD and LOG blocks, head receipts | bullet 5 |
| `6892c3eee465dda72d0977d1f259ab282b0d3ebe` | residual reports, entry corrections, lesson residual section | — (review record) |
| `1a1e8b22dd070c7b5265be81a6f37a8afe2ae92a` | late BuildF6A report and fixtures, lesson note | — (wave record) |
| `3c16b3a649181b0dbfa386997de8c573f5bf7c3b` | BuildF6A's final report revision (the cancelled seat kept writing; stopped again at the 03:03Z freeze) | — (wave record) |

Every hash is from the `jj-lane.sh` `landed` line.

## Before → after measurements

| Claim | Command | Before (367ec0f1) | After | Measured commit |
|---|---|---|---|---|
| C1 | `python3 .ufo/evidence/round-29/c1-measure-v2.py --repo CLONE --rev REV` | `covered=63/64 restraint=6 box3_mismatch=1`, PASS false, exit 1 | `covered=64/64 restraint=8 box3_mismatch=0 appended=22 bound=22 prefix_equal=1`, `C1_R29_V2_PASS=true`, exit 0 | `7a45f7b9` (`c1-at-E.stdout`), `6892c3ee`, `1a1e8b22`, `3c16b3a6` |
| C2 | `python3 .ufo/evidence/round-29/c2-measure-v2.py --repo CLONE --rev REV` | `fixture=absent`, PASS false, exit 1 | `fixture=present anchored=1 kill_original=0 units_original=105 units_minimized=105 ddmin_match=0 kill=0 one_minimal=0 entry_sourced=1 quote_located=1`, PASS false, exit 1 — **missed** | `6892c3ee`, `1a1e8b22`, `3c16b3a6` |

No-harm: depth command D `recorded_cases=9 depth_score=9` at base and head. CriticNoHarm found the registry rows it checked held, and no protected path edited after `9f3084bc`.

## Sources & frontier

- Census start (base, `.ufo/evidence/round-29/census-start.stdout`): exit 0, `tameshi ok`, 7 W04 warnings (S047, S048, S075–S078, S081). At `9f3084bc`: exit 1 (E11 S024 used-by missing; Mistake 2). Census end (head): exit 0, `tameshi ok`, the same 7 W04 warnings. Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`.
- Rows 89 → 89 (`grep -c '^| S[0-9]' corpus/SOURCES.md`). Added by tier: none. Touched: S024 `status` queued → mined, `used-by` — → `corpus/knowledge/survivor-fixture-minimization.md`. The change log is in lesson `## Gate`.
- S024 re-opened 2026-10-23T01:09Z. Snapshot sha256 `3abede35…e99`. Quote (section "Delta Debugging"): "Its result is 1-minimal, meaning that every character contained is required to produce the error" (15 words). Seat ReopenS024 re-fetched byte-identical bytes.
- Frontier: F6 stays **open**. The F6 move was measured and missed. Its knowledge (B5 masked under the pinned declaration; the reachable unanchored 2-unit variant) is in the entry and lesson. F8 wording corrected (README Round-29 section).
- Sourced claim: C2 rests on S024, opened this round.

## Trend verdicts

- **expansion: improved.** New entry `corpus/knowledge/survivor-fixture-minimization.md` on ground no entry covered (F6). It is source-headed on S024, which is now mined. It records a measured finding: B5 is masked by the exact-mode check under the pinned declaration.
- **quality: improved.** The restored cold-read coverage rests on 36 fresh reads at the content revision (64/64 monitor credit). The four sampled entries hold (SampleBoundReads). The entry was corrected after review.
- **discernment: improved.** The control wave caught a met counter (C2 v1) and an unpinned counter (C1 v1) before data. The admit/reject record: S024 admitted (re-open agreed by ReopenS024); the S059 supersedes row deliberately not written (reasoned deferral); 2 reports rejected by the assembler; 10 entries excluded by the binding gate with reasons. This is offset by Mistake 1: unreachable target dispatched before a control report landed.

## Gate

- Admit: S024 re-open → mined (quote verbatim in snapshot; ReopenS024 agrees).
- **Reject:** C2 counter v1 — met by three skip-the-work controls (CriticC2Design: `af694c1d`, `9ea4f2df`, `109fe613`, each PASS=true). Re-designed before data.
- Reject: C1 counter v1 — executable identity unpinned (CriticC1Design). Re-designed before data.
- Reject: 2 cold-read reports (Read07A: non-hex input digest; Read10B: URL in `external_inputs`) and 10 unbound entries (binding gate).
- Holds (provider safety refusals, never retried): CtlC1Shortcut, CtlC2Shortcut — `code=cyber_policy`. So the "shortcut keyed on ids or labels" control class was never scored by a seat (ReviewControls).

## Mistakes (lesson `corpus/lessons/round-29.md` `## Mistakes`)

1. Data dispatched before the control call settled (CriticC2v2 report 6 min after dispatch). Result: C2 unreachable and missed.
2. A pre-registered `used-by` named a file not yet landed, so the census was red at the content revision.
3. Misrooted seat report (Read10C).
4. Seat containment breach (BuildF6B killed BuildF6A's processes).
5. A binding check was frozen without testing the assembler's output shape.

Each row has captured-by and a fix shown able to fail.

## SHONEN

- [~] Box 1 (decision tables, error patterns, checklists, cited sources) — lane assertion; evidence `SKILL.md`, `corpus/knowledge/`; no independent promotion verifier.
- [~] Box 2 (end-to-end domain task logged) — lane assertion; `LOG.md` "Round 29"; no independent promotion verifier.
- [~] Box 3 (executable without oral context) — the input-keyed monitor credits the full page at `3c16b3a6` (64/64; `c1-measure-v2.py`, box3_mismatch 0). The independent readers are seats dispatched by the L1, so this is not an independent promotion verifier.
- [~] Box 4 (no cross-domain bleed) — lane assertion; `PROVINCE.md` unchanged; no independent promotion verifier.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (L1 and every seat that reported).
- L0 questions: none.
- Scope: dispatched 01:03Z; freeze 03:03Z; this report was filed just after the freeze, and no new work started after it.
