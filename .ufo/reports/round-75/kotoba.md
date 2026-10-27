# Kotoba — round 75 (attempt 1)

## Work performed

Declared claim: **C1 depth** — make the source-backed trigger-threshold rule distinguish the guide's unqualified “above” wording from the reference runner's `>=` implementation, without presenting the guide as defining equality.

- Opened the already-registered S213 guide this round: https://agentskills.io/skill-creation/optimizing-descriptions.md, 2026-10-27; the located quote is “Use imperative phrasing.” (`corpus/lessons/round-75.md:5`). Reused S213; no registry rows added. The existing S213 row remains mined and used by the round-70 entry (`corpus/SOURCES.md:153`).
- Re-measured base claims instead of inheriting r74 targets: `python3 -B verifiers/check_spec_craft.py --rev master` → `spec craft pages backed 3 of 3`, held at base 0; `python3 -B verifiers/check_sibling_reread.py --rev master` → 20 of 20. Both were already green, so they were not reused as r75 claims; exact commands/outputs were observed in the L1 run.
- Read-only build/recon wave: 64 settled seats, with 44 scouts, 16 executors, one connector, one scribe, one critic and one reviewer (`.ufo/waves/round-75/w1-results.json`). Their findings include the threshold wording's ambiguity and a broader existing-counter limitation (`w1/R75Facet02.md:55-102`; `w1/R75Facet01.md:6-17`).
- Falsification wave: 64 settled seats—32 reviewers, 16 critics and 16 mutation-testers (`w2-results.json`). The F1 comparator concern survived as a calibration risk, not proof that the old statement was false; the missing should-not-trigger source pin was a separate actionable control gap; proposed wording/controls also received scope qualifications (`w2/R75Attack02.md:6-19`). Results were 64/64; no dead seat is reported by either results file. One W1 report was misrooted under `kotoba-shokukin/` and recovered byte-exact with `cmp`; one W2 result (`R75Attack28`) names a report path but no report file was present. Both dispositions are in `.ufo/waves/round-75/` and the first is recorded in `corpus/lessons/round-75.md`.
- Repaired the source-derived sentence in `SKILL.md` and appended its qualification to the existing round-70 knowledge entry (not a new S213 row). Updated the lesson index and corpus integrity baseline to include r75's lesson and the r74 closure spot-check (`corpus/README.md:147-150`; `verifiers/corpus-baseline.json`).
- Mined two mistakes: stale proposal premise (historical description size is not current; `considerthese/2026-10-26.md:17` versus measured current frontmatter) and seat-report attribution/misroot (`corpus/lessons/round-75.md:7-12`).
- Planner seat: L1 held canonical planner/data-walk responsibility; no validator-rejected planner role was added. The lead data-walk rode W1 scout/connector assignments (`plans/round-75.md`).
- Misroot sweep: fleet `git status --porcelain` showed only the unrelated `.scratch/closure-mado-r50.json` plus the kotoba misroot. The latter was copied byte-exact to `kotoba-shokunin/kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md`, verified with `cmp`, and the fleet-root copy was removed; the recovered path is committed.
- Tool installations/updates: none.

## Landed changes

All lane changes below are in final pushed lane commit **`ac9f29510d3914a6edb97c8dbdb3445cab9141de`** (origin/master verified at the same hash). Each is tied to `LOG.md` § Round 75:

- `SKILL.md` — threshold rule now says the guide leaves equality unspecified and names the reference `>=` comparator.
- `corpus/knowledge/skill-eval-artefacts-round70.md` — appended round-75 correction, scoped to one reference implementation.
- `plans/round-75.md`, `plans/round-75-addendum-1.md` — claim and pre-measurement literal-predicate clarification.
- `corpus/lessons/round-75.md`, `corpus/README.md` — Gate, mistake ledger and index rows, including the recovered misroot.
- `verifiers/corpus-baseline.json` — expected observations refreshed from the recorded corpus integrity output; all zero-mode expectations remain zero.
- `.ufo/waves/round-75/` — validated specs, dispatches, registries, results and seat artifacts. `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` preserves the byte-exact recovered seat report.

The initial baseline-edit commit `d118a3b12565333b8b8bd72f45df87828da00faf` contained a JSON trailing comma. The corpus gate exposed it; it was corrected and rechecked in `14ab41594b0cbea5bac5566cb6eb24b0d8f75386`. The final recovered-report commit is `ac9f29510d3914a6edb97c8dbdb3445cab9141de`; all three commits are ancestors of the pushed branch. No lane-authored leftovers remain.

## Before → after measurements

| Claim | Counting command | Before | After | Verdict / bound |
|---|---|---:|---:|---|
| C1 — depth, source-grounded S213 rule | `grep -Fc 'The guide says a should-trigger rate must be *above* the threshold but does not specify equality' SKILL.md` | `0` (exit 1) at base `65a5c7a663249e0522cc49e4a148424200d9ddfe` | `1` (exit 0) after correction, final lane commit `ac9f29510d3914a6edb97c8dbdb3445cab9141de` | **Measured improvement, pending independent closure/admission.** The count proves the literal appears; it does not prove semantic adequacy or general client behavior. W2 supports the limited distinction and also identifies an unpinned should-not-trigger branch as a separate gap (`R75Attack02.md:10-19`). Score remains depth 9 (delta 0); no score increase claimed from this literal counter alone. |

Counter control: the same fixed-string count on base committed `SKILL.md` prints 0, while the edited worktree prints 1. This is a narrow content change measurement, not a semantic source checker. No-harm corpus gate results after landing: `python3 -B verifiers/verify_corpus_integrity.py` → `9/9 checks pass`; `python3 -B verifiers/verify_corpus_independent.py` → `exit 0`, with `unindexed=0`, `stale=0`, `missing=0`, `report_dead=0`, `commit_unresolvable=0`. The r74 counters remained green at base (3/3 and 20/20); no broader tip-battery improvement is claimed.

## Sources & frontier

- `corpus/SOURCES.md` rows before → after: **151 → 151**; command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`.
- Census before: exit **0**, `kotoba ok`, with W04 duplicate-URL warnings S018, S019, S021, S054-S056, S065, S086, S103-S104, S106, S110-S111, S114-S115, S118, S207-S208, S212-S213; 151 rows.
- Census after: exit **0**, same W04 warning set; 151 rows. Added this round by tier: **0**. Rows touched/status/recheck/used-by changes: **none**. Frontier rows advanced: **none**. S213 was opened and reused; the existing row was not changed. Assimilation: none (the current source row already exists; no staged package entry was adopted). Considerthese was mined without editing it.
- `corpus/lessons/round-75.md:5-12` records this round's located quote, candidate reject, both mistakes, and captured-by/fix statements. Non-author admit/reject spot-check remains pending; wave seats are lane agents, not non-author verifiers.

## Trend verdicts

- **expansion — unchanged.** No new knowledge entry or uncovered ground was admitted; no source rows were added. S213 already existed.
- **quality — improved (bounded).** `SKILL.md` now distinguishes the guide's unspecified equality case from the one reference runner's `>=` behavior; the corpus integrity gates pass 9/9 after the baseline refresh. This does not establish trigger performance in a live client.
- **discernment — unchanged.** The L1 and dispatched seats are not outside reviewers; no qualifying non-author Gate spot-check has occurred in this round yet.

## SHONEN

- [~] Box 1 — existing author assessment; the r75 one-sentence clarification is not a fresh non-author audit. Pointer: `SHONEN.md:5-6`.
- [~] Box 2 — round-75 sourced skill-craft task was executed and logged, but only by the lane; pointer: `LOG.md` § Round 75.
- [~] Box 3 — unchanged; no fresh non-author cold run. Pointer: `SHONEN.md:9-10`.
- [~] Box 4 — unchanged author assessment; no non-author cross-domain review this round. Pointer: `SHONEN.md:11-12`.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Round shape: two validated v2 waves, 64 seats each; total 128. W1 role mix 44 scout / 16 executor / 1 connector / 1 scribe / 1 critic / 1 reviewer; W2 32 reviewer / 16 critic / 16 mutation-tester. All 128 seats settled in results; no dead seat recorded. W2 has one result whose expected report file is absent (`R75Attack28`), and W1's `R75Facet48` was recovered under the lane typo path noted above. The W1 wave was primarily build/recon, not a 25%-attack v2 mix; W2 is the falsify wave. Independent non-author closure and Gate spot-check remain outstanding.
