# kengaku — round 24 report (kaika campaign, steered)

Lane: kengaku-shokunin (LLM/model research & evaluation; owned axes novelty + calibration).
Worktree `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kengaku-shokunin`, branch `kaika/round`,
base `99cf615`. Lane commits: **`94da19e`** (round work) and **`06872d4`** (after-census receipt measured on `94da19e`).
Collision check at start: no `.ufo/reports/round-24/kengaku.md` in the fleet root or the ledger worktree, and no
round-24 section in the lane `LOG.md`.

## Work performed

Declared claims (pre-registered in `plans/round-24-claims.md` before the swarm, amended once after the
reviewer/critic seats, §Amendment 1):

- **C1 — coverage (lowest non-retired axis, 7, tied with novelty 7) + capability `sources-registry`.** This covers
  the sourced expansion onto uncovered ground (5 knowledge entries), the SOURCES registry, index parity in both
  directions, and the province map. Tie-break: a novelty +1 needs a new probe construct, and no probe runs this
  round.
- **C2 — calibration (owned, 8).** Mine the lane's own mistakes into round-closure criteria, record round 23 as
  NOT-ADMITTED, and repair the SCORECARD state defects (D10–D14, D16).

Work items:

- Admission bar created before any admission: `corpus/QUALITY.md:10` §Admission bar Q1–Q8, each row citing its
  lesson. Citation wording was tightened before commit after PreregReviewer-3 (`plans/round-24-claims.md`
  §Amendment 1 item 3).
- SOURCES registry: `corpus/SOURCES.md:19` (25 rows), `:49` §Paths (5), `:57` §Search log (5 bounded searches),
  `:65` §Leads (unopened). Every web row was re-opened 2026-10-19. Per-row quotes, locations, sha256 and byte
  counts are in `corpus/evidence/round24-sources/gate.md`, and the same receipts appear in
  `corpus/lessons/round-24.md:79`.
- Five knowledge entries. Each opens with the `source:`/`verified-at:`/`recheck:` triad and cites mined rows:
  - `corpus/knowledge/contamination-detection-and-transparency.md` (S001, S002, S004)
  - `corpus/knowledge/llm-judge-calibration.md` (S009–S012)
  - `corpus/knowledge/benchmark-saturation-and-lifecycle.md` (S007, S008)
  - `corpus/knowledge/agent-time-horizon-and-task-validity.md` (S013, S014, S005, S006)
  - `corpus/knowledge/paired-eval-uncertainty-reporting.md` (S015–S019)
- Index parity and frontier in `corpus/README.md`: knowledge, lessons, 28 root logs, `plans/` and evidence-dir
  rows; 5 coverage-map rows (`:194`); `## Frontier` (`:229`, 5 rows).
- `PROVINCE.md:95` §Province map — round 24, with Core `:102`, Frontier `:117`, Adjacent `:125` and Historical
  (absent, not governed) `:141`. Every surface was re-verified today with `test -e`, `ss` or `sha256sum`. Absent
  surfaces stay enumerated and the old table is untouched.
- Mistakes mined: `corpus/lessons/round-24.md:7` §Mistakes (20 rows, every dossier pointer re-verified) and `:32`
  §Classes. `corpus/QUALITY.md:67` §Round-closure criteria R1–R10 covers the 12 uncaptured mistakes.
- Round 23 recorded NOT-ADMITTED at `LOG.md:208` and `SCORECARD.md:569`, quoting `attrib-r23-stream.log:239`
  `STREAM TARGET opencode-go: on-target GT n=0 … -> FAIL`.
- SCORECARD state repair:
  - re-derived 7-axis table (`SCORECARD.md:582` §Round 24)
  - capabilities ×3 (`:551`)
  - saturation line 8 / window N 4 (`:562`)
  - D14 errata (`:618`)
  - stale round-13 plan marked superseded (`:266`)
  - `## Planned (round 25)` (`:624`)
  - move-log rows (`:370-371`)
- SKILL.md: one 2-line pointer to SOURCES and QUALITY (`SKILL.md:617-618`). No other SKILL growth.
- Census instrument: `plans/round24_census.sh`, a v2 rewritten after the reviewer found false-pass modes. Base
  receipt `corpus/evidence/round24-census/base-99cf615.txt` (run on a `git archive 99cf615` tree); after receipt
  `corpus/evidence/round24-census/after.txt` (commit `06872d4`, measured with `94da19e` checked out).
- L2 swarm: one batched call of 10 seats. The first two attempts were refused with `Background job limit reached
  (100)`, so the identical batch was retried after backoff, per the orchestrator's capacity note. Seats:
  - planner RoundPlanner-3
  - connector SiblingConnector-3
  - executors SourcesRegistry-3, KnowledgeA-3, KnowledgeB-3, IndexProvince-3
  - scribe LessonsScribe-3
  - scout Round23Scout-3
  - reviewer PreregReviewer-3
  - critic ClaimCritic-3

  Every prompt opened with `/skill:godspeed` plus the verbatim `directive.md` bytes. No model was passed. Writers
  had disjoint files and no L2 committed.
- Provider exhaustion: KnowledgeB-3 and SourcesRegistry-3 stalled on the rate-limited executor route and were
  cancelled. They were re-spawned in one call as KnowledgeB2 and SourcesGate2. KnowledgeB2 then failed (`Codex is
  at capacity … turn_rate_limit_exceeded`) and was re-spawned as KnowledgeB3, which completed. Claims were not
  shrunk.
- A post-landing pair (LandedReviewer, LandedCritic) reviewed the tree before commit. All of its fixes were
  applied: S015 quote locations, SCORECARD line pointers, the search-log count, a final contract-census receipt,
  the PROVINCE brace-check and "pending" row, S023/S006 self-report wording, R2/R7 checks, and marking the stale
  plan superseded.
- Safety: the orchestrator's `cd` notice was relayed verbatim to all 9 running L2s. No lane write landed outside
  the worktree, which every seat confirmed.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| QUALITY bar Q1–Q8 + R1–R10; SOURCES registry + gate receipts; 5 knowledge entries; README parity/coverage/Frontier; PROVINCE map; round-24 lesson; SCORECARD round-24 section, capabilities, saturation, errata, planned; SKILL pointer; claims + census | `LOG.md:231` §Round 24 | `94da19e` |
| Round 23 NOT-ADMITTED record | `LOG.md:208` §Round 23 | `94da19e` |
| After-census receipt (round census + contract census + grader + freeze-check on `94da19e`) | `LOG.md:231` (receipts named at the end) | `06872d4` |

Push: none. The standing operator rule "No push" overrides MISSION.md's commit-then-push for this campaign (prompt
§6.6; `PROTOCOL.md` operator-gated artifacts are committed, not pushed). The report is left uncommitted in the
ledger worktree for the integrator.

## Before → after measurements

Counting command for every row: `sh plans/round24_census.sh`, run from the lane root.
- Before: `corpus/evidence/round24-census/base-99cf615.txt` (tree = `git archive 99cf615`).
- After: `corpus/evidence/round24-census/after.txt` (`HEAD 94da19e`, committed in `06872d4`).

**C1 — coverage (score 7 → 7, held by the declared-but-unresolvable-surface cap; capability entered).** Measured on
`94da19e`.

| key | before | after |
|---|---|---|
| expansion_entries_on_mined_rows | 0 | 5 |
| full_triad_knowledge | 0 | 5 |
| knowledge_unindexed | 3 | 0 |
| lessons_unindexed_excl_round24 | 5 | 0 |
| root_logs_indexed | 0/28 | 28/28 |
| plans_indexed | 0/8 | 10/10 |
| dead_index_rows / dead_plans_rows | 0 / 0 | 0 / 0 |
| coverage_map_rows | 11 | 16 |
| frontier_rows | 0 | 5 |
| province_map_sections | 0 | 4 |
| sources_rows | absent | 25 |
| contract census | — | malformed 0, `A=24 C=1`, `mined=18 queued=5 rejected=2`; dup, enum and mined-path checks empty |

**C2 — calibration (score 8 → 8, held).** Measured on `94da19e`.

| key | before | after |
|---|---|---|
| lesson_mistake_rows | absent | 20 (0 duplicate ids) |
| closure_criteria_citing_round24 | absent | 10 |
| round23_sections (LOG, SCORECARD) | 0 0 | 1 1 |
| round23_not_admitted_with_fail_quote | 0 | 1 |
| saturation_declared | 0 | 1 |
| capability_rows | 0 | 3 |
| scorecard_state_defects_open | 6/6 | 0/6 |

Harm checks, all on `94da19e`:
- `python3 grader.py` → `CHECKS n=733 mismatches=0 errata_pinned=1`, `VERDICT: PASS`.
- `freeze-check` → OK.
- `git diff --diff-filter=D --name-only 99cf615 -- corpus/knowledge` is empty.
- The only removed line in the diff is the SCORECARD capabilities placeholder row (LandedReviewer).
- SKILL.md grew by 2 lines.

## Sources & frontier

- **SOURCES rows: absent → 25.** Command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Rows added by tier:** A 24, B 0, C 1 (S023).
  - Kinds: paper 19 (A), docs 2 (A, S005/S006) + 1 (C, S023), dataset 1 (A, S014), own-work 2 (A, S024/S025).
  - The A rows are scoped narrowly: the two OpenAI posts (S005, S006) are A only for "what OpenAI reports about
    its own evaluation"; preprints are A only for their own method and results; S024 and S025 are the lane's own
    gate outputs.
- **Rejected (2):**
  - S003, the DCR factor as general decontaminated accuracy (flip: validation on frontier-scale generative tasks).
  - S023, the Scale SWE-Bench Pro blog as evidence (flip: a peer-reviewed paper or audit trail).
- **Rows touched old→new:** none after creation. Before commit, SourcesGate2 corrected anchors on re-open for S006,
  S007, S009, S013, S014 (anchor + teaches), S015 and S023 (listed old→new in its report and summarized in
  `corpus/lessons/round-24.md` §Gate). After review, I also rewrote the S023 teaches and search-log wording from
  "independent audit"/"falsified" to "OpenAI self-reported audit"/"contradicted".
- **Frontier advanced:**
  - Five ground areas moved from ART-dossier leads into the core coverage map, as 5 admitted entries.
  - Five new frontier rows (`corpus/README.md:229`, `PROVINCE.md:117`): agentic task-spec audits; contamination
    transparency cards; judge calibration applied inward; an identity-verified endpoint for novelty probes;
    non-karpathy wiki topics (source absent).
- **Leads left unopened:** 3 (`corpus/SOURCES.md:65`).

## Mistakes

- **Classes mined:** 20 mistakes (`corpus/lessons/round-24.md:7`): PRED 3, LAND 7, MEAS 3, PROC 4, STOP 2, DISC 1.
  - Captured 3, partial 3, protocol-captured 2, uncaptured 12.
  - Two are new this round: M19, the stale round-23 premise; and M20, a census prefix match counting `## Gated
    steps` as `## Gate`.
- **Criteria added:** 18.
  - Admission bar Q1–Q8 (round start).
  - Round-closure criteria R1–R10, which cover all 12 uncaptured mistakes. Each cites `corpus/lessons/round-24.md`
    M-ids plus the source lesson where one exists.
  - LandedCritic found no criterion without a lesson behind it.

## Trend verdicts

- **Expansion: improved.** 5 admitted `knowledge/` entries on uncovered coverage-map ground, each citing `mined`
  SOURCES rows (`C1.expansion_entries_on_mined_rows` 0 → 5). No row quota was used; the registry is 25 opened rows.
- **Quality: improved.**
  - All 5 new entries carry the triad, and 23 web sources were re-opened with digests.
  - Two quote-location errors found by LandedReviewer were corrected before landing.
  - Stale state was marked rather than left: the round-23 premise is M19, and the 149-checks errata is D14.
  - No admitted entry fails its re-check (LandedReviewer re-opened 5 sources and 4 entry quotes: 7 agree, 1
    location disagree, fixed).
- **Discernment: unchanged, pending.**
  - The bar exists and its rejections are recorded (2 rows, 7 rejected inferences).
  - The required outside non-author spot-check (≥1 admit, ≥1 reject) has not run; it is the orchestrator's, after
    landing.
  - Lane L2 reviews are advisory (R6).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:617-618`
  pointer to `corpus/SOURCES.md` (25 opened, tiered rows); the decision tables in the 5 new entries (`## How kengaku
  applies it`); no non-author review.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:208` (r23 executed run, recorded
  NOT-ADMITTED), `LOG.md:231` (r24 sourced-research task); no new model run this round.
- [~] Instructions executable by an agent without oral context — `corpus/evidence/round24-census/after.txt`
  (census, grader and freeze-check re-run by commands in-repo); no fresh outside executability review.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:95` §Province map round 24
  (Core/Frontier/Adjacent/Historical, re-verified 2026-10-19); SiblingConnector-3 found 0 URL collisions and no
  duplication.

## Verdicts (self, pending non-author verification)

- **C1 coverage: verifies-with-fix → fixes applied.** The score holds at 7 under ClaimCritic-3's binding ruling: a
  Historical-absent section does not clear the cap. The counts moved as pre-registered, and the `sources-registry`
  capability entered with a clean census.
- **C2 calibration: counts verify; score held 8.** ClaimCritic-3 and LandedCritic judge C2 "honest closeout
  bookkeeping", not a calibration axis-move ("fails as registered" under rubric clause (d)), and RoundPlanner-3
  concurs that "improved" is unsupported for the score. SCORECARD records C2 as "counts moved (closeout and
  SCORECARD state accuracy, not demonstrated discernment); score held". That dissent stands unresolved. Admission
  depends on whether C2 counts as a verified axis-move; the operator rules.
- **Harm:** none observed. Depth gained a 2-line pointer, operability's grader PASS holds, freshness re-verified,
  adjacency got report-outs, and novelty made no claim.

## Adjacency report-outs (SiblingConnector-3)

- **kotoba:** its ACES lead (scan-vs-judge ρ=0.14) can use `llm-judge-calibration.md` and
  `paired-eval-uncertainty-reporting.md` for skill-lift trials.
- **tameshi:** S005/S006 task-validity audits and S016 nondeterminism bear on its LLM test-generation studies.
- **chousa:** contract rule 3 is PASS (QUALITY.md defers the research method to chousa). Kengaku may cite chousa
  `corpus/QUALITY.md` criterion 8 (four support states) in a later Q-row supersession.

## L0 questions

- kengaku | round-24 | Coverage cap: does a surface explicitly retired to `PROVINCE.md` §Historical — absent, not
  governed (dated `test -e` receipt, still enumerated) still count as "declared-but-unresolvable" for the coverage
  rubric cap? Until ruled, kengaku coverage stays capped at 7 regardless of index/expansion work.
- kengaku | round-24 | Novelty r21: the r21 "novelty axis-move — improved" verdict was never converted to a number
  (anchor still 7). Should verdict-only rounds be converted retroactively (and by whom), or stay verdict-only?
- kengaku | round-24 | C2 admission: is a measured closeout/state-accuracy calibration claim with score held (8→8)
  an admissible axis-move, or bookkeeping that should not be declared as a claim?

## Integrator notes

- The orchestrator's non-author spot-check for this round should sample ≥1 admit (e.g.
  `llm-judge-calibration.md`) and ≥1 reject (S003 or S023), re-open ≥3 SOURCES rows, and re-run
  `sh plans/round24_census.sh` plus the contract census.
- Round 23 still has no fleet report file (`.ufo/reports/round-23/kengaku.md` absent). Its disposition is recorded
  in the lane LOG/SCORECARD this round; whether the ledger needs a round-23 row is the integrator's call.
- Defect D15 is outside lane scope: reports for 19–22 exist only lane-local, and MANIFEST cites
  `kengaku-shokunin/.ufo/rounds/round-22/kengaku.md`.
- `SHONEN.md` still violates the canonical one-evidence-line form (D17), and SKILL frontmatter lacks the contract's
  triggers and anti-trigger (D18). Neither was touched this round.
- Base-tree census receipts used `/tmp/k24base` (a `git archive` extract). The contract census was run from
  `/tmp/k24-contract-census.sh`, whose commands are verbatim from the contract and whose output is in
  `after.txt`/`gate.md`. Neither temp file is evidence of record.

## Post-review fixes

Lane commit **`e21f9ea`** ("round-24: post-review fixes", pathspec-limited, lane identity). These fixes were
required by the orchestrator's adjudication, which records: non-author reviewer = return, critic = reject, and C2
ruled a real calibration move. All changes are append-only except the recheck cells, which contract rule 2 allows to
be edited in place.

1. **SOURCES recheck cells (E09), 21 changed in place.**
   - S001–S004, S007–S013, S015–S022: `2027-01-17 (90d)` → `2027-01-17`.
   - S024, S025: `each round` → `90d`.
   - Every old→new pair is logged in `corpus/lessons/round-24.md` §Post-review corrections.
   - Validator: `TZ=UTC bash …/fleet-census/scripts/sources-census.sh validate <worktree>` → `ok`, exit 0.
2. **Quote-location slips.** Each sentence below is corrected by an appended `## Corrections` section in its entry.
   - S002 "Table 2" → Figure 2 (§3.1).
   - The S002 quoted sentence: §4 → §1. The Table 5 caption uses different wording.
   - S012 "repetitive list" quote: Abstract → §3.3.
   - S005: the two quotes come from the opening summary items 1–2, not the section headings.
   - Entries touched: `contamination-detection-and-transparency.md`, `llm-judge-calibration.md`,
     `agent-time-horizon-and-task-validity.md`.
3. **S009 range.** "~45–48%" is corrected to the exact Table 3 Ref-5 flip rates: BiGGen 35.40–45.54% and FLASK
   40.53–48.58%.
4. **S023 rejection reason.** New row **S026** (rejected, tier C) supersedes S023.
   - The rejection stands: Scale's contamination-resistance claim is unreviewed vendor self-description.
   - The correction: S006 is about Pro task validity, not contamination.
   - S026 was re-opened today; its receipt (quote, location, sha256 `171087c5…`) is in
     `corpus/evidence/round24-sources/gate.md`.
   - This spot-check disagreement becomes mistake **M21** → `corpus/QUALITY.md` **Q9** (a rejection's reason must
     follow from its evidence).
   - The location and number slips become **M22** → **Q10** (a second seat re-reads every location and number).
   - Both criteria cite the lesson.

Re-measured on `e21f9ea`:
- `sh plans/round24_census.sh`: unchanged except `sources_rows` 25 → 26 and `lesson_mistake_rows` 20 → 22.
- `python3 grader.py` → PASS.
- The only removed lines in the diff are the 21 edited recheck rows.
- Credential sweep: empty.

Trend update: discernment moves from **unchanged** to **improved per LEARNING.md**. The non-author spot-check
disagreed on 1 admit (partial) and 1 reject. Each disagreement became a lesson (M21, M22) and a grounded
`QUALITY.md` criterion (Q9, Q10).
