# tabi — round 66 report (attempt 1, Linux host)

Lane repo: `/home/vgpnk/Projects/shokunin/tabi-shokunin`. Base `2816adb359a50c2fd83fa975e39f0650aa189984`. Final lane tip `e54f916aa9f25fc9ba56868ce832a90817b21cbb` (`ls-remote origin refs/heads/master` matches). Round shape: ONE v1 wave `w1`, 13 seats, planner held by the L1. Attack seats 5/13 (38 %). Dead seats: none.

## Work performed

Declared claims (2, one each on a distinct axis):

- **C1 — adjacency (declared; the lowest owned axis, score 8).** Rebind the r62 sibling-overlap ledger to the live sibling heads so the frozen meter (`.ufo/waves/round-65/counters/c1-adjacency-host-v22.mjs`, unchanged) reaches predicate true with zero findings. **Verdict: VERIFIED on its frozen predicate; the axis attribution is contested** (see Trend verdicts and the L0 line).
- **C2 — calibration (score 9).** A v3 receipt-provenance gate whose predicate code is byte-identical to frozen v2, with two selftest cases for the two relative-input bases, so that each single-base mutant (M5a, M5b, plus M5c and M5d) turns the selftest red. **Verdict: VERIFIED on its frozen predicate.**

Neither claim is admitted: C1's axis is contested, and the lowest-axis obligation depends on the ruling (L0 line below).

Work items, with evidence:

- Round-start measurements: live sibling heads snapshot `.ufo/waves/round-66/measure/snapshot-live-r66.tsv` (16 of 20 sibling lanes moved since the r62 snapshot; `git -C <lane> cat-file -t`, 20 of 20 resolve). Frozen meter at live heads: predicate false, 40 findings (`.ufo/waves/round-66/measure/v22-live-r66.json`; `scored/c1-before-r62.json`, exit 1).
- Pre-freeze do-nothing controls committed at `4bea87d5` (`.ufo/waves/round-66/measure/README-do-nothing.txt`): C1 control above; C2 controls `controls/mutants/M5a-drop-repo-base.mjs` and `M5b-drop-matrix-dir-base.mjs`, each run with its own selftest, 12/12 clean, exit 0 (`controls/mutants/*.selftest.txt`).
- Rebind generator `.ufo/waves/round-66/counters/rebind-ledger-r66.mjs` (R66Executor1). Mechanical-only output and adjudicated output: `c1/mechanical/`, `c1/adjudicated/`; decisions `c1/adjudication-decisions.tsv`; rationale `c1/adjudication.md`; diff summary `c1/diff-summary.json`.
- v3 gate `.ufo/waves/round-66/counters/check-receipt-provenance-v3.mjs` (R66Executor2): `diff` against v2 is two added lines inside the selftest array (`c2/v2-v3.diff`). Four mutants generated from v3 (`c2/final/mutants/`) by the L1 and re-measured on final bytes (R66Executor3 and R66MutTester1 measurements were taken before the cases landed; superseded, see Mistakes).
- Attacks (wave `w1`): R66Reviewer (ledger attack: 22 rows changed, 0 disposition changes, independent re-derivation 10/10 sampled lanes match, moved-note recomputation confirmed), R66Reviewer2 (v3: predicate code unchanged; both new cases exercise their base), R66Critic (falsified C1 as adjacency: freshness per AXES.md; confirmed C2 survives; found the `../` escape defect F7; found the S-next overclaim F8, now corrected), R66MutTester2 (ledger: disposition vocabulary-only; 149/149 in-vocabulary flips survive), R66Connector (0 new browser-ground lines in any moved lane; only the kake quote changed), R66Scout (Node path API quote and access date), R66Sentinel (no Critical/High/Medium findings).
- Corpus: S171 row (`corpus/SOURCES.md:186`), knowledge notes `corpus/knowledge/relative-input-binding-round-66.md` and `corpus/knowledge/adjacency-ledger-live-heads-round-66.md`, lesson `corpus/lessons/round-66.md` (Gate, Mistakes, Errata for round 65, Frontier), QUALITY criteria 121 and 122.

## Landed changes

| Commit | Content | LOG / SCORECARD |
|---|---|---|
| `4bea87d5` | pre-freeze do-nothing controls and live-head measurements | LOG round 66 |
| `b1ecd665` | frozen claims (`claims.json`, 14 pins), wave `w1` evidence (spec, dispatch, results, all seat reports, instruments, ledgers, mutants) | SCORECARD round 66 block |
| `950626dc` | corpus (S171 row, two knowledge notes, lesson, QUALITY 121–122, README round-66 section), SCORECARD round-66 block, LOG round-66 entry, census-end | LOG round 66; SCORECARD round 66 |
| `e54f916a` | post-freeze scored receipts (`scored/`) | — |
| fleet `40d089a9` | L0 question line (C1 axis ruling) in `.ufo/l0-questions.md` | — |

## Before → after measurements

Counting commands are frozen in `.ufo/waves/round-66/claims.json`. Commit for every scored receipt: `e54f916a` (scored at `b1ecd665`).

C1 (`--rev b1ecd665`, `--snapshot .ufo/waves/round-66/measure/snapshot-live-r66.tsv`):

| Input | Command | Exit | Predicate | findingCount |
|---|---|---|---|---|
| r62 ledger at live heads (before) | `node .ufo/waves/round-65/counters/c1-adjacency-host-v22.mjs --repo . --rev b1ecd665… --fleet /home/vgpnk/Projects/shokunin --snapshot … --json` | 1 | false | 40 (head 21, sha 9, lines 8, quote 1, audit note 1) |
| mechanical-only rebind | same, `--audit c1/mechanical/… --delta c1/mechanical/…` | 1 | false | 1 (quote, kake-shokunin:SKILL.md:1358) |
| adjudicated rebind (after) | same, `--audit c1/adjudicated/… --delta c1/adjudicated/…` | 0 | true | 0 |

Disposition changes r62 → adjudicated: 0 (`grep`/`python` count over 149 line rows, independently by the L1 and by R66Reviewer). Quote changes: 1. Audit-note changes: 1. Lane-row changes: 21 (provenance columns). Receipts: `scored/c1-*.json`.

C2 (v3 selftest, `node <gate> --selftest --scratch <abs>`):

| Gate | Before (v2 or v2-with-mutant) | After (v3 or v3-with-mutant) |
|---|---|---|
| unmutated | v2 12/12 clean, exit 0 | v3 14/14 clean, exit 0 |
| M5a drop repo base | 12/12 clean, exit 0 (survives) | 13/14 red, exit 1 (killed) |
| M5b drop matrix-dir base | 12/12 clean, exit 0 (survives) | 13/14 red, exit 1 (killed) |
| M5c cwd base | not measured before | 13/14 red, exit 1 (killed) |
| M5d absolute only | not measured before | 12/14 red, exit 1 (killed) |

Receipts: `controls/mutants/*.selftest.txt` (before), `scored/c2-*.txt` (after). Predicate code: `diff` two added lines in the selftest array.

## Sources & frontier

- SOURCES rows: 170 → 171 (S171 added, tier A, `docs`, `mined`, used by `corpus/knowledge/relative-input-binding-round-66.md` and `corpus/lessons/round-66.md`). Command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 170 (start), 171 (end). Rows added by tier: A +1. Rows touched old→new: none. Frontier rows advanced: none (Node path docs are an existing source kind; S157 is the same URL for a different scope, hence the W04 warning below).
- Census start: `.ufo/waves/round-66/census-start.txt`, exit 0. Census end: `.ufo/waves/round-66/census-end.txt`, exit 0 (`sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`). W04 duplicate-URL warning on S171 (same URL as S157, different scope; warnings allowed).
- Sourced claim: C2's knowledge note cites S171 for `path.join` semantics. The claim's kill rests on the executed fixtures, not on S171 (critic F8 corrected the draft's wording).
- Mistake mined (round-66 lesson `## Mistakes`): six rows, with red and green states for the ones that have an instrument.
- Assimilation: none (`considerthese/` absent; the r57 quarantine register shift is unresolved, per the open L0 line for round 57).
- Corpus knowledge notes: 77 → 79. Lesson `corpus/lessons/round-66.md`. Spot-check: pending (non-author closure).

## Trend verdicts

- **expansion — unchanged.** Two knowledge entries, both on ground the coverage map already holds (gate calibration and the sibling ledger); S171 is an existing source kind. No new uncovered ground.
- **quality — unchanged.** The 21 lane rows of the ledger were brought current with live bytes, but the ledger is a measurement artifact, not an admitted knowledge entry, and the disposition column is unchanged; no admitted entry was superseded or found false. Gate v3 closes one untested branch; the repo-escape defect (critic F7) is open.
- **discernment — unchanged.** No non-author spot-check of this round's gate decisions has been recorded yet. The wave's critic and reviewers are seats this lane dispatched, so they do not count as non-author. The closure session owes the sample.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Approval table (`:697`), §Evidence ladder, §Runbook, `:1598-1617`; not non-author this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/knowledge/multi-step-journey.md` §1–§2, §7; logged in `LOG.md` round-3 entry; round-66 C2 executed the v3 gate on committed fixtures (`scored/c2-v3-selftest.txt`).
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/executor-test-sufficiency.md` §0, §4; the v3 selftest is re-runnable from `claims.json` argv.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19`; the R66Connector scan (`.ufo/waves/round-66/w1/R66Connector.md` §4) found no moved-lane browser-ground line claiming tabi ground.

No `[x]` line is written: promotion is operator-owned and no non-author verifier has checked these boxes.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. pacman stays paused. Node v24.21.0 was already present and used as is.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at the fleet root before the report: `.scratch/run15-state.json` (orchestrator state, not touched by this lane) and `.ufo/l0-questions.md` (the L0 line added by this lane, committed as `40d089a9`). No untracked file written by a seat of this lane sits at the fleet root.

## Mistakes

Six rows in `corpus/lessons/round-66.md` `## Mistakes`: class · evidence · captured-by · fix. Summary: round-65 selftest count drift (46 committed vs 47 live; errata in the lesson); v2 relative branch untested (fixed by v3 cases; red 12/12, green 13/14 kills); stale survivor table from R66MutTester1 (superseded by L1 re-measurement); claim sourcing overclaim (corrected); C1 axis label (dissent recorded, QUALITY 121); meter disposition-blindness (QUALITY 122; no instrument repair this round).

## Open L0 questions

- `tabi | round-66 | C1 axis ruling` (appended, committed `40d089a9`): adjacency or freshness. Round 66 is not admitted until ruled.
- Existing open questions from rounds 44, 57, 59, 60, 61 and 65 remain open and unruled; routed around.

## Round shape

ONE v1 wave `w1`, 13 seats: scout 1, connector 1, executor 3, scribe 2, reviewer 2, critic 1, mutation-tester 2, sentinel 1. Attack seats 5 (reviewer 2, critic 1, mutation-tester 2) of 13 = 38 %. L1 planner seat. Residual call: none. Round total: 13 seats. Dead seats: none (`w1-results.json`, WAVE-DONE received). Scribe drafts (`w1/R66Scribe*`, `w1/R66Scribe2*`) were used as input only; the lesson and knowledge notes were written by the L1 from the committed measurements.

## Verdict

Not admitted. C1 verified on its frozen predicate with the axis contested; C2 verified on its frozen predicate. No axis harmed, no score moved, no capability entered. The round lands as an honest stop pending the operator's ruling on C1's axis.
