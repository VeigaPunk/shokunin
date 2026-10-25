# Kake round 28 — citing-set gate repair and field-performance knowledge

Lane: `kake-shokunin`, branch `master`, pushed lane tip
`36b6b21022f7288200abe2ace7e686c1297588a3` (`jj-lane.sh state`: local = remote,
ahead 0). Attempt 3 of round 28, in-session L1 `KakeR28a3` (runtime model as
exposed by the host: anthropic/claude-opus-5-5). Repair-first round after the
round-26 and round-27 honest stops.

## Work performed

Declared claims (SCORECARD.md "Round 28 — declared claims", landed before
implementation at `84ea5b15f164d32907182745b7887feb40b5ddd4`, unchanged in this
attempt):

- **C1, operability, repair-first:** round-27 routed defect 1 in
  `scripts/citing_set.py`: unusable input documents yield the contracted JSON
  report and exit 2, and an absent or unreachable corpus surface does not return
  clean. Before 4/15 at `22c1669`, declared after 15/15.
- **C2, freshness, frontier (sourced claim):** field performance (Core Web
  Vitals thresholds and CrUX eligibility) enters held knowledge as
  `corpus/knowledge/field-performance-cwv.md`, grounded in S036–S039 opened this
  round. Before 0/4, declared after 4/4.

Work items:

- Inherited attempt-2 state re-verified before reuse: C1 counter re-run at
  `b5d423f` gave 15/15 with the same per-case vector as the attempt-2 receipt,
  and 4/15 at `22c1669` (`kake-shokunin/.ufo/waves/round-28/verification/c1-after-b5d423f-a3.json`,
  `c1-before-22c1669-a3.json`). C2 counter at `b5d423f` gave 0/4
  (`verification/c2-before-b5d423f-a3.json`). All four sources re-opened with one
  GET each at 09:29:23Z–09:29:26Z, HTTP 200; all 16 attempt-2 receipt quotes
  found again (`.ufo/waves/round-28/sources/receipts-a3.json`).
- Inherited, committed as evidence: attempt-2 `w1-spec.json`, `w1-dispatch.json`,
  `w1-dispatch-attempt1-refused.json` (job-limit refusal, 0 spawned),
  `w1/swarm-registry.json`, `sources/S036–S039.txt`, `sources/receipts.json`,
  `verification/c1-after-b5d423f.json`. Nothing inherited was discarded.
  Not mine and left as found: untracked `.ufo/waves/round-26/__pycache__/`.
- Wave 1 `w1a3` (38 seats, validated under v1, one task call): source mining
  for S036–S039 (8 scribes), SKILL table draft, mistake mining, QUALITY
  criteria drafts, sibling-overlap and corpus-link scans, registry scout, and
  C1 attacks: 8 hunk reviewers, 8 mutation-testers, 4 critics, 4 executors.
  Reports: `kake-shokunin/.ufo/waves/round-28/w1a3/*.md` (38 files).
- All seven C1 revert mutants were killed with exactly the predicted cases
  failing and controls still passing; a refuse-everything gate scored 11/15 and
  an always-clean gate 2/15 (`w1a3/MutRefuseAllGate.md`, `MutRevert*.md`).
- Falsifiers found an over-refusal in `b5d423f` (bare repositories and
  trailing-space top levels, `w1a3/CriticOverReject.md`) and adjacent gaps.
  Repaired in follow-up commits `8ecbefe`, `5a83d13`, `e73d48b` and recorded in
  the lesson as a mined mistake. Case matrix (27 roots and environments, four gate
  versions): `verification/c1-root-env-matrix.json`.
- No-harm on real inputs: base and repaired gates gave byte-identical JSON on
  the round-26 and round-27 frozen inputs in Git and working-tree modes
  (`w1a3/RunRealInputParity.md`); six existing suites passed identically at both
  revisions (`w1a3/RunNoHarmSuites.md`); final-revision fixture selftest 29/29.
- C2 entry, four SOURCES rows, Paths line, Search log paragraph, lesson
  `## Gate` with one located quote per source plus 11 further quotes, README
  coverage row, SKILL "Field performance triage — round 28" table, PROVINCE
  Frontier pointer (commit `e57f601`).
- Residual call (8 seats, one ordinary task call: 5 reviewers, 3 critics)
  attacked the entry against live pages, the Gate quotes, the rows, the C2
  counter, the QUALITY criteria, the C1 follow-up and the no-harm scope
  (`.ufo/waves/round-28/residual/*.md`). Its corrections landed in `36b6b21`:
  S038 user and browser eligibility, the API's two-day lag, the S038
  origin-versus-page tension, Lighthouse-only INP limit, INP poor-bound
  rationale, S037 section labels and anchor cell, QUALITY "Fails if" line.
- Round-27 spot-check routed defects: 1 repaired by C1; 2 already carried by
  `corpus/QUALITY.md` strict-status refinement; 3 and 4 turned into criteria in
  `corpus/QUALITY.md` "Counters and field evidence — round 28".
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  listed only driver state files, `.scratch/goal-…`, a `__pycache__` file and
  a `write` file dated 2026-10-21; none was written by a kake round-28 seat.

### Round shape, seats and conformance

- Shape: default v1 shape, wave 1 only, plus one residual call. Wave 1 (38
  seats) produced fewer than 32 genuine new attack items beyond what it had
  already attacked, so no wave 2 was dispatched; the leftover checks went into
  one residual call of 8 seats. Round total **46 seats** (38 + 8), 0 dead,
  0 replaced, 0 refused calls in attempt 3.
- Wave 1 role mix: 11 scribe, 8 reviewer, 8 mutation-tester, 4 critic,
  4 executor, 2 connector, 1 scout. Attack roles 20/38 (53%). Residual: 5
  reviewer, 3 critic. The §3 planner seat is held by the L1; the planning data
  walk rode the connector and scout items.
- Slots: `wave-slot.sh acquire kake w1a3 38` granted (live 24, cap 85);
  `acquire kake residual 8` granted (live 60). Both released after every seat
  returned.
- Report-length overruns (`wc -l` on the committed files): wave 1 limit 100
  lines — `ReviewGitTopLevel` 123, `ReviewBlankRevision` 115,
  `ReviewGitCorpusBlob` 111, `ReviewUnreachableId` 105,
  `ReviewDocstringContract` 104; residual limit 80 lines —
  `ReviewNoHarmCorpus` 98, `ReviewSourcesRows` 85.
- Seats wrote scratch only under `/fast/scratch/hyaku/kake-r28a3/`; one
  executor's round-27 oracle selftest wrote disposable clones under
  `/fast/scratch/hyaku/kake-r27` (instrument-fixed path, disclosed in
  `w1a3/RunNoHarmSuites.md`).

## Landed changes

All through `jj-lane.sh --as kake`, each printed `landed <hash>`; LOG entry
"Round 28 — attempt 3" in `kake-shokunin/LOG.md` covers each.

| Commit | Content |
|---|---|
| `84ea5b15f164d32907182745b7887feb40b5ddd4` | (attempt 2) declarations and both counters |
| `b5d423fc02057f67a6f3a255808313ce40d29069` | (attempt 2) C1 repair; before receipts |
| `e57f601bd0148bb7dce9052f0cade3fd11751375` | C2 entry, S036–S039 rows, lesson, QUALITY criteria, README, SKILL table, PROVINCE pointer, source receipts |
| `8ecbefe31b81462239c572fbe23d21404442a177` | C1 follow-up: top-level check by `git rev-parse --show-prefix` |
| `5a83d13b28024cef461c0ef497e28681684555ac` | C1 follow-up: Git subprocesses ignore inherited `GIT_DIR`-family variables; docstring |
| `e73d48bbf20759fc7758afaebf841fa02e5cfbbf` | C1 follow-up: `MemoryError` → `document_not_json`; base reason labels for symlink or gitlink at the corpus path |
| `36b6b21022f7288200abe2ace7e686c1297588a3` | Review corrections (entry, lesson, QUALITY, S037 anchor, SKILL row), LOG, SCORECARD measured results, wave 1 and residual evidence, verification receipts |

Against the base `22c1669`, only `PROVINCE.md` (Frontier bullet rewritten, the
Core rule kept verbatim) and `scripts/citing_set.py` carry deleted lines
(`git diff --numstat 22c1669 36b6b21`); every other changed file is additions.

## Before → after measurements

| Claim | Counting command | Before | After | Measured commit |
|---|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-28/c1_interface_count.py --root . --revision <commit>` | 4/15, exit 1 at `22c1669` | 15/15 (11/11 defect, 4/4 control), exit 0 | `b5d423f`; again 15/15 at `8ecbefe`, `5a83d13`, `e73d48b` and the lane tip `36b6b21` |
| C2 | `python3 -B .ufo/waves/round-28/c2_source_count.py --root . --revision <commit>` | 0/4, exit 1 at `b5d423f` | 4/4, exit 0 | `e57f601`; again 4/4 at the lane tip `36b6b21` |

Receipts: `kake-shokunin/.ufo/waves/round-28/verification/` (`c1-before-22c1669-a3.json`,
`c1-after-b5d423f-a3.json`, `c1-after-8ecbefe.json`, `c1-after-5a83d13.json`,
`c1-after-e73d48b.json`, `c2-before-b5d423f-a3.json`, `c2-after-e57f601.json`).
Per-case reason codes at `e73d48b` match each attacked defect (for example U1
`document_not_regular_file`, A4 `not_a_directory`, A7
`root_not_repository_top_level`). Independent re-runs by seats agree
(`w1a3/RunC1Counter.md`: 0 differences; `residual/CriticC2Counter.md`).

Counter limits stated, not hidden: the C1 counter checks finding ids, not
reason codes, and K4 trusts the measured commit's own fixture runner
(`w1a3/CriticCommittedBytes.md`); the C2 counter checks quote shape, not quote
truth (`residual/CriticC2Counter.md`). Quote truth was checked outside it:
15/15 Gate quotes are exact substrings of the retained and live visible text
(`residual/ReviewGateQuotes.md`, my own check at `36b6b21`).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`.
  Round start: exit 0, output `kake W04 S033 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes` / `kake ok …/corpus/SOURCES.md`.
  Round end (lane tip): exit 0, the same two lines (W04 is pre-existing).
- Rows 35 → 39. Added by tier: 4 tier A (S036 web.dev Web Vitals, S037 web.dev
  thresholds methodology, S038 CrUX methodology, S039 CrUX API), status
  `mined`, opened 2026-10-22, recheck 90d. Rows touched old → new: none of the
  35 prior rows; the S037 anchor cell (new this round) was corrected before the
  report and logged in `corpus/lessons/round-28.md`.
- Frontier advanced: field performance moved from open ground to a first held
  entry; it stays in `PROVINCE.md` Frontier (knowledge without a gate). New
  Paths line "Field performance — S036 → S037 → S038 → S039".
- Sourced claim: C2 cites S036–S039 opened this round.
- Mined mistakes (lesson `## Mistakes`): (1) proxy counter that a constant
  could satisfy, fix shown able to fail by `w1a3/MutRefuseAllGate.md`; (2) the
  C1 repair's own over-refusal, fix shown able to fail by
  `verification/c1_root_env_matrix.py` (gate `b5d423f` refuses rows B1 and T1).

## Trend verdicts

- **expansion: improved** — new knowledge entry on previously uncovered
  ground (`corpus/knowledge/field-performance-cwv.md`) with four new tier-A rows;
  `git diff --name-status 22c1669 36b6b21 -- corpus/knowledge` shows one `A`.
- **quality: improved** — round-27 routed defect 1 repaired with measured
  15/15 and killed mutants; falsifier findings repaired and re-measured; the
  entry was corrected against live pages by two non-author reviewers.
- **discernment: improved** — two lesson-backed QUALITY criteria (counter must
  reject a constant, with a "Fails if" line; no field data is not a pass) and
  the round-27 defects 3 and 4 as criteria; open findings named rather than
  narrowed. Admission is the non-author closure's call.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` "Field performance triage — round 28" (S036–S039); no non-author `[x]` sign-off.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 28 — attempt 3": source opening → entry → falsification → corrections; no live property measured.
- [~] Instructions executable by an agent without oral context — entry "How kake uses this" steps and counters with commands; residual reviewers executed them; no `[x]` verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — entry boundary paragraph routes lab runs to tabi, API keys to operator and kagi, source ranking to chousa (`w1a3/ConnectSiblingOverlap.md`).

## Open items

- Not repaired, outside the declared C1 set: `S01`-style population ids,
  repeated CLI options, duplicate or nonfinite JSON (`w1a3/CriticCounterFaithful.md`);
  deep corpus walk traceback, missing `O_NOCTTY`, stack-dependent JSON depth
  (pre-existing; lesson "Open findings").
- Round-24 policy stop, round-27 strict C1 unknowns (7 units in 3 pairs) and
  the out-of-population debt are unchanged.
- L0 questions: none new. The round-24 policy-stop line
  (`.ufo/l0-questions.md:80`) stays open.

Stale-lane: respawn-per-round driver; attempt 3 progressed through pushed
commits to `36b6b21`; no other kake mission is open and no round 29 was started.

Tool installs: none (curl 8.23.0, Python 3.14.8, git 2.56.0 already present).
No pacman, no service action, no API call, no MANIFEST edit.
