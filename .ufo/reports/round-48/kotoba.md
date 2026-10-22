# kotoba — round 48 report

Round 48, attempt 2 (hyaku phase 3, in-session L1 lane subagent `KotobaR48`). Attempt 1 (a stale
2026-10-21 author identity) was failed at T0 and was not resumed. Lane repository
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`. Base `75f671b109d8eddd0d64c1429bd6379fe577175a`.
**Pushed lane tip: `e5c926c5f9d4c32446de5107d35ec8f5c8e924fb`** (`jj-lane.sh state`: local = remote, ahead 0).
Plan: `plans/round-48.md`. Lesson: `corpus/lessons/round-48.md`. LOG: the two round-48 entries at the end of `LOG.md`.

## Work performed

Declared claims (two, distinct axes, causally separable — separate commits, separate counting commands):

- **C1 — freshness (all-axes lowest, 8); repair-first claim; learning claim.** New knowledge entry
  `corpus/knowledge/frontmatter-rule-authorities-round48.md`: which authority imposes which SKILL.md
  frontmatter rule (open spec S018, its reference validator skills-ref S017, Anthropic docs S019,
  Anthropic's packager S012, Codex docs S021) against what the lane's lexical `trigger.no_xml_tag`
  executes (S020), with the round-47 YAML-alias, Unicode-name and escaped-value counterexamples run.
  It repairs routed item 3 of `corpus/lessons/round-47-verifier-spotcheck.md`. Declared after-value:
  knowledge Markdown entries 34 → **35**.
- **C2 — depth (owned-axis lowest, 9); improved-bounded.** `verifiers/verify_harness_independent.py`
  also enumerates direct-child `SKILL.md` directories under `--oc-config/skill` and `--oc-config/skills`
  when the opencode log does not name them. Declared after-value: committed config-root ruler target
  failures 5 → **0** (ruler exit 1 → 0). It does **not** resolve routed defect 1 (see below).

Order change, recorded before any landing: the first plan framed C2 as "repair routed defect 1,
configured-root half". Build critic `C1ClaimCritic` and revenger `C1JoinDefinitionHistory` showed the
round-47 join drop comes from the producer's `customize-opencode` byte probe, which C2 does not touch.
The entry, which does repair a routed item, became the first claim (`plans/round-48.md` re-ordering
note; lesson M26; `corpus/QUALITY.md` Q21). Targets were not changed.

Work items (evidence pointers under `.ufo/waves/round-48/` in the lane unless stated):

- Inherited state re-verified before reuse: attempt 1's `c0185da` (ruler, oracle, instrument record) and
  `75f671b` (before receipt) — every hash matches committed bytes and a fresh base run reproduces the 5
  target failures (`build/FrAttempt1Audit.md`, `build/C1RulerRerun.md`). Attempt 1's private-tree
  pointers (superseded ruler copies, `initial-census.json`, void ledger) are named as not re-verifiable
  from the lane. Nothing from `/fast/scratch/hyaku/kotoba-r48-author*` was continued.
- C2 implementation: L1 candidate, competing implementation (`build/C1AltImplementation.md`), regression
  arm with a nested-skill discriminator that kills the recursive mutant the frozen oracle cannot see
  (`build/C1RegressionArm.md`, `build/C1RulerTargetMutants.md`), floors ratchet, landed `d1ae458`;
  ruler on the landed commit exit 0, clean (`.ufo/round-48/verification/after-configured-root.json`).
- C2 falsify follow-ups: an unreadable configured root aborted the run with exit 2 where base ran clean
  (`falsify/A24UnreadableRoot.md`, Q05) — fixed in `48819b9` with its own arm (self-test 115 → 116);
  arm assertions tightened in `03f5394` (`falsify/A25ArmReview.md`, `falsify/A19ArmMutants.md`). Ruler
  re-run clean at both (`.ufo/round-48/verification/after-configured-root-48819b9.json`, `…-03f5394.json`).
- C1 sources opened 2026-10-22 by build seats: spec and client guide (`build/C2SpecScribe.md`), skills-ref
  at upstream commit 69ef37e9 (`build/C2SkillsRefSource.md`, run in `build/C2SkillsRefRun.md`), packager
  pin still `main` HEAD (`build/C2QuickValidateFresh.md`), Anthropic docs drift (`build/C2ClaudeDocs.md`),
  Codex and opencode docs (`build/C2CodexOpencodeDocs.md`), omp 18.12.6 loader (`build/C2OmpLoaderRules.md`),
  lane checker on 10 fixtures (`build/C2LaneCheckerRun.md`), 24-fixture table (`build/C2EntryScaffoldScribe.md`).
- C1 landed `887b6af`; `SKILL.md` § Portability floor rewritten (it called the packager simply
  "stricter"; the lane check disagrees with it in both directions); `PROVINCE.md` Core gained the entry.
- Falsify-wave corrections landed in `d28b16b`, `2788704`, `eb5a80f`, `03f5394`: the check's FAIL detail
  string and docstrings, `PROVINCE.md` wording, entry sweeps moved to footnotes with file operands,
  untabled rules listed, per-source rechecks, README qualifications corrected, S001/S003/S012/S018/S019
  `used-by` moves logged, Q22–Q24 (`corpus/lessons/round-48.md` § Falsify-wave corrections).
- Routed round-47 items: 1 not resolved (C2 narrows one input gap in the same row; built-in marker
  disagreement stays routed); 2 repaired (S018–S021 supersede S001/S003/S010/S013, README live-24/24 rows
  qualified, erratum horizon recorded); 3 repaired by C1; 4 → Q22 (M28), no cleanup ran; 5 no new
  criterion (the observed class is caught by both corpus instruments), no frozen input edited.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — 0 untracked files written by
  round-48 seats (`falsify/A31MisrootSweep.md`); nothing copied or deleted.

## Landed changes

All lane commits through `jj-lane.sh`, author `kotoba-shokunin <kotoba@shokunin.local>`, each printed
`landed <hash>` after remote verification:

| commit | content | LOG entry |
|---|---|---|
| `d1ae45830235c38320b31032b57a8323cbf90b17` | C2: configured-root enumeration, arm, floor 104 → 115 | § Round 48 landing |
| `887b6af54d3f4446f1fe51dc16f26b2e83bc82e1` | C1: entry, SOURCES S016–S021, lesson, Q20–Q21, README, SKILL.md:151, baseline 61 → 63 | § Round 48 landing |
| `84b9c9ba89559b51a72c83c2b9605b184df4ae9e` | records: LOG, SCORECARD, plan, wave-1 evidence, C2 receipt | § Round 48 landing |
| `d28b16b644754c19aa4996db7577e975f77e76a2` | corrections 1 (detail string, PROVINCE, Q22/Q23, M28) | § Round 48 landing pin |
| `27887041bd82f2de31cf33bb223783749fb5cbc9` | corrections 2 (entry source line, S012 used-by) | § Round 48 landing pin |
| `48819b9f80c197fcaac4acb26bf25e83eaf3ae7e` | C2 follow-up: unreadable root, arm 116, floor 116 | § Round 48 landing pin |
| `eb5a80fed97c9ea2c649c6a2e1dc04a0ec80adaa` | corrections 3 (sweeps, untabled rules, Paths, search log, baseline report_total 40 → 41) | § Round 48 landing pin |
| `03f5394d66bdd6de6138743bd74b6ac7ecb9e0d0` | corrections 4 (arm assertions, docstrings, Q24, README, rechecks) | § Round 48 landing pin |
| `e5c926c5f9d4c32446de5107d35ec8f5c8e924fb` | landing pin: LOG, SCORECARD, last receipt and reports | § Round 48 landing pin |

## Before → after measurements

- **C1:** `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` → **34** at `75f671b`,
  **35** at `887b6af` and at tip `e5c926c` (the 35th is the entry; `git diff --stat 75f671b 887b6af -- corpus/knowledge`
  shows one added file). Re-derived by `falsify/A09ClaimSizingC1.md`.
- **C2:** `python3 -B .ufo/round-48/tools/config-root-ruler.py --repo <lane> --revision <rev> --consumer-sha256 <sha256 of the consumer at rev> --oracle .ufo/round-48/oracle/config-root-cases.json --oracle-sha256 1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883 --scratch <new /fast/scratch dir> --baseline-receipt .ufo/round-48/verification/before-configured-root.json --baseline-sha256 8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312`
  (ruler file sha256 `01af33a6…` = committed bytes) → before at `197b5a4`: exit 1, verdict failed,
  **5** target failures (committed receipt); after at `d1ae458` (consumer `d67b1b6e…`): exit 0, verdict
  clean, **0** target failures, 0 behavioral mismatches, 13/13 settled. Same result at `48819b9`
  (`0f33f600…`) and `03f5394` (`f576c23f…`). Independently re-run by `falsify/A18RulerRerun.md`.
- Gates at tip `e5c926c` (L1 run): sources census validate exit 0; checklist `--json` exit 0;
  corpus integrity exit 0; corpus independent exit 0; floors 116/116 PASS; checker self-test 1845
  assertions, 0 failures; pins exit 1 and surfaces exit 1 (omp 18.12.6, red at base too).

## Sources & frontier

- Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`:
  round start `kotoba ok`, exit 0 (`.ufo/waves/round-48/census-start.txt`); round end `kotoba ok`, exit 0,
  with three W04 same-URL warnings from the superseding rows S018, S019, S021.
- Rows 15 → 21 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); census at end:
  tier A 20, C 1; mined 12, queued 8, rejected 1. Added by tier: 6 × A — S016 code (opencode v1.19.3 skill
  discovery), S017 code (skills-ref), S018 spec (supersedes S001), S019 docs (supersedes S003), S020
  own-work (supersedes S010), S021 docs (supersedes S013). Gate lines (URL, access time, quote ≤ 25 words)
  in the lesson § Gate; all six re-opened by `falsify/A17GateLines.md`.
- Rows touched old → new (`used-by`, contract rule 2, logged in the lesson): S001 `SKILL.md` →
  `corpus/lessons/round-46.md`; S003 `SKILL.md` → `corpus/lessons/round-46.md, corpus/lessons/round-47.md`;
  S012 `SKILL.md` → `SKILL.md, <entry>`; S018 and S019 `<entry>` → `SKILL.md, <entry>`. No `status` or `recheck` moved.
- Sourced claim: C1's entry cites S017–S021 (all `mined`, opened this round).
- Mined mistakes: M24 rule credited to the wrong authority → Q20, superseded by Q23; M25 source-name-only
  sweep; M26 repair named after the row, not the cause → Q21; M27 self-hash through a pipe → Q24; M28
  hash match read as custody → Q22. Each "shown able to fail" is in the lesson.
- Frontier: `PROVINCE.md` Core gained the frontmatter-rule-authorities line. The Loader-rule freshness
  frontier row is now stale again (omp 18.12.6); left for round 49 (SCORECARD `Next: round 49`).

## Trend verdicts

- **expansion: improved (bounded).** One admitted-candidate entry on ground no coverage-map row held,
  citing mined rows opened this round (34 → 35). About 12 of its 60 cells repeat facts held at base and
  six rule classes are untabled (`falsify/A10FillerHunt.md`, `falsify/A12OmittedRules.md`).
- **quality: improved (bounded).** C2 closes one input-class gap with an arm and a crash-class fix; stale
  `SKILL.md`, `PROVINCE.md`, detail-string and SOURCES claims corrected. Not resolved: routed defect 1,
  the oracle's nested and frontmatter-name gaps, several entry counts without command and date (Q13).
- **discernment: improved (bounded).** Claims re-ordered before landing when a critic refuted the first
  framing; five new criteria grounded in mined mistakes; every falsify finding either corrected or listed
  as open in LOG and SCORECARD. Disputed by the round's own critic: C1's axis label (`falsify/A09ClaimSizingC1.md`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:151` now cites S018/S019/S012 and the round-48 entry; 41 boxes, checklist `--json` 11/11 at `e5c926c`.
- [~] End-to-end domain task executed and logged — `LOG.md` § Round 48 landing (C2 ruler red → green on committed bytes; C1 counterexamples run through three validators).
- [~] Instructions executable without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md` (no fresh non-author cold run this round).
- [~] No cross-domain bleed — `PROVINCE.md` Core updated round 48; sibling scan `build/FrSiblingOverlap.md` found no sibling knowledge to cite instead.

## Round shape and seats

- Shape: default two v1 waves, validated under `scripts/hyaku/ufo-wave-policy.json`, each one `task` call
  carrying the validator's `taskCall` unchanged; seat gate `wave-slot.sh` granted both (build 33, falsify 34).
- Wave 1 build: **33 seats** — executor 9, scout 8, scribe 5, reviewer 4, mutation-tester 2, critic 2,
  connector 2, revenger 1. 33 reported, 0 dead.
- Wave 2 falsify: **34 seats** — reviewer 19, critic 8, mutation-tester 3, scout 3, sentinel 1; every item
  names its target. 34 reported, 0 dead.
- **Round total 67 seats**, 0 dead, no residual call. Attack roles (reviewer, critic, mutation-tester):
  8 + 30 = 38 of 67 (57%). §3 floor met inside wave 1 (connector, executor, scribe, scout, reviewer,
  critic). The L1 held the planner seat; the planning data-walk rode `C1ClaimCritic`, `C2UncoveredSweep`
  and `FrRoutedDefectPattern`.
- Process note: I released the build-wave seat slot when dispatching the falsify gate while 7 build seats
  were still running, so for about 40 minutes the gate under-counted kotoba's live seats by up to 7.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs/updates: L1 none. Seats: `skills-ref` 0.1.1 via `uv tool install skills-ref` (PyPI;
  reference validator for C1 fixtures; `build/C2EntryScaffoldScribe.md`, `build/C2SkillsRefRun.md`), plus
  a scratch venv of skills-ref from upstream commit 69ef37e9 (`build/C2SkillsRefRun.md`); scratch-only npm
  packages `glob@13.0.5`, `minimatch@10.2.5` (`falsify/A14S016Row.md`). No pacman transaction.
- L0: none appended this round. The round-47 open question (all-axes versus owned-only reading of the
  lowest-axis rule) is carried: C1 targets the all-axes lowest (freshness), C2 the owned lowest (depth);
  `falsify/A09ClaimSizingC1.md` argues C1's counter is the expansion observable, not freshness.
- Observed, not caused by this round: omp 18.12.6 (`check_substrate_pins.py` exit 1 DRIFT 2/3,
  `verify_surfaces.py` exit 1 at base and tip); the live harness join exits 1 or 2 from run to run on the
  same commit (session-store race, HIGH-3); adjacency replay `instrument_drift` at base and tip.
- Driver completion is not admission; the non-author closure judges both claims.
