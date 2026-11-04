# Round 89 — kake (attempt 2)

Lane `kake` · operability + freshness axes (calibration sub-axis) · lane repo `/home/vgpnk/Projects/shokunin/kake-shokunin` · branch `master`.
Attempt 1 ended `lane-dead-no-report` at 18:04:14 (`.ufo/watchdog.log`); `.ufo/waves/round-89/` did not exist when attempt 2 started, so nothing was inherited.
Stale-lane: no (respawn-per-round driver; no other mission of this lane is open).
Tool installs or upgrades: none (no pacman; no network beyond the two named RFC GETs).

## Work performed

**Declared claims (2; distinct axes; frozen before any after-state data, `.ufo/waves/round-89/freeze.md`, freeze commit `08ab46a1`):**

1. **C1 — calibration** (the lane's lowest owned non-retired axis, 2 HOLD): close the six defects the round-88 outside spot-check routed (R88-A…F). Before → after: `open=6 closed=0 met=false` (base) → `open=1 closed=5 met=false` (tip). **Not admitted.** Item A stays open (its frozen form demands an in-line tag on filed round-88 lines, which the append-only rule forbids). The wave review shows the counter's B–F verdicts are not sound.
2. **C2 — freshness, bounded capability** (declared freshness; the critic places it under operability/coverage, see Trend verdicts): a conservative Vary-nominated cache-key constructor. Before → after: candidate absent `frozen=0/16 props=0/200 refuse=0/9 met=false` (base) → `frozen=16/16 props=200/200 refuse=9/9 controls=5/5 met=true` (tip, under both the frozen v1 and the committed v2 counter). **Not admitted.** The wave review shows the counter admits reference copies, import shortcuts and a hybrid table, and seven contract clauses have no coverage.

**Work items, with evidence:**

- Protocol load: `MISSION.md`, `AXES.md`, lane `SCORECARD.md`, `corpus/QUALITY.md`, `corpus/README.md` `## Frontier`, `corpus/lessons/round-88.md` and `round-88-verifier-spotcheck.md` (closure admitted; routed defects R88-A…F).
- Source census before: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` → exit 0, 25 × W04 (`.ufo/waves/round-89/controls/census-before.txt`).
- Frontier step: S465 (RFC 9110 §5.6.2 and §5.6.1.2, `https://www.rfc-editor.org/rfc/rfc9110.txt`, HTTP 200, 502 941 B, sha256 `21c1cdce…7232a`, opened 2026-11-04 21:16 UTC). The §4.1 ground for the key is S463 (already held at the httpwg URL; a drafted duplicate S464 was dropped, see Landed changes). Retained bodies at `.ufo/waves/round-89/L1/src/`. Knowledge entry `corpus/knowledge/cache-key-construction.md` cites S463 and S465; the ScribeEntry candidate was adopted (`## Limits` heading, exact quote lines, U+001D named by code point), and its runnable checklist was re-run, and each command matches its expected output.
- Mistakes mined: `corpus/lessons/round-89.md` §Mistakes, eight rows, each with captured-by, fix and witness; the wave review adds more (below).
- Gate: `corpus/lessons/round-89.md` §Gate, two admits (S463 §4.1, S465 §5.6.2) and two rejects, each with a ≤25-word quote and line number. Item B of C1 reads this gate's round-88 twin and matches it (`gate-sample: admits=2 rejects=2`).
- C1 counter `.ufo/waves/round-89/c89_defect_queue.py`, selftest 12/12 (`controls/c1-selftest.txt`); base control `controls/base-c1.txt` (`open=6`, exit 1); tip `controls/final2-c1-at-tip.txt` (`open=1`, exit 1).
- C2 counter `.ufo/waves/round-89/c89_key.py`, selftest 43/43 (`controls/c2-selftest.txt`; re-run at the tip `93475f7e` printed the same line); base controls `controls/base-c2.txt` (v2 re-run) and `controls/base-c2-freeze-v1.txt` (freeze-time bytes, restored); tip `controls/final2-c2-at-tip.txt` (v2) and `controls/final2-c2-frozen-v1-at-tip.txt` (v1, extracted from `08ab46a1`).
- Candidate `scripts/cache_key.py` (commit `9784ad54`, 132 lines, stdlib, reads one JSON object on stdin, `{"key": …}` or `invalid_input:` with exit 1); the ExecKey seat's final bytes, sha256 `3a658326…e7da996`, integrated unchanged.
- Real-data trial: six recorded `vary` cases (R1–R6) from the round-61 and round-81 captures through the integrated key construction (`w1/ExecTrial.md`). No recorded capture carries `*`; the round-23 captures carry no response headers.
- Wave 1: one v1 wave, 14 seats, dispatched via `.ufo/waves/round-89/w1.ready` at 18:13:46. `WAVE-DONE` received (`[15c16ef4…] Main: WAVE-DONE kake r89 w1: all 14 seats settled`). See Wave shape.
- Wave review (attack seats; their findings are recorded in the lesson and bind the verdicts, not hidden):
  - `ReviewCounterC1` (`w1/ReviewCounterC1.md`, 38 receipts): RC-1…RC-10. E reads HEAD, not `--revision`; A's tag exemption, scope and self-report; B's substring parse; C sees 5 of 21 receipt names; F's header substring; mirror mode skips E. The B–F verdicts are unsound.
  - `ReviewCounterC2` (`w1/ReviewCounterC2.md`): nine findings. A reference copy, aliased and runtime imports, `file://` exec and a hybrid table all reach `met=true`. The property classes never assert key strings; every-header CR/LF and case-duplicate refusals are untested; U+001D is undefined in the contract.
  - `CriticClaims` (`w1/CriticClaims.md`): C1 is not separable from C2; its do-nothing mirror control reaches `open=0 closed=6 met=true` with `scripts/` and `.ufo/` byte-identical to base; C2's target certifies the instrument's sample, not the capability; the axis is mislabelled.
  - `ExecControls` (`w1/ExecControls.md`, 15 stubs): seven contract clauses with zero coverage; each stub reaches `met=true`.
  - `MutKey` (`w1/MutKey.md`): 37 single-point mutants of the integrated candidate; 27 killed (73.0 %), 27/34 (79.4 %) excluding three equivalent mutants. The seven real survivors are counter gaps, not candidate defects.
  - `ScoutRFC` (`w1/ScoutRFC.md`): registry facts for S463/S465; found the round-88 lesson's stale S463 statements (appended correction, `2342c3a4`).
  - `ScribeEntry` (`w1/ScribeEntry.md`): F1 (S464 duplicates S463), F2 (URL status), F3–F5 (`## Limits`, quote lines, U+001D), F6–F7 (counter gaps). F1 and F3–F5 were adopted; F6–F7 route to round 90.
  - `ConnectorScope` (`w1/ConnectorScope.md`): zero contested scope across 20 sibling lanes; its §5 carries UFO-FSD material outside kake's domain, not absorbed.
  - `ExecDefects` (`w1/ExecDefects.md`): fix bytes for the six routed defects. Not applied: its in-place edits to filed round-88 bytes conflict with the append-only rule, so the lesson's tagged tails were used instead. Its findings 1, 2, 5 and 6 are carried into the routing.
  - `ExecKey`, `ExecTrial`: candidate and trial (above). `ScoutGround`, `ScribeLesson`, `ScribeLedger`: findings and drafts; the lesson, SCORECARD, LOG and SKILL/README/PROVINCE rows were written by L1, so their drafts were not adopted.
- L0 questions appended (`.ufo/l0-questions.md`, fleet commit `ca57a223`): (1) the C1 item-A rule; (2) the C2 guard amendment after dispatch; (3) the C2 instrument gap, for a round-90 counter revision.

## Landed changes

Each commit is on lane `master`; the round's LOG entry is `LOG.md` `## Round 89` (commit `28532540`), amended in `f63b7ecd`.

| Commit | Change | Evidence |
|---|---|---|
| `08ab46a1` | Freeze: two claims, both counters, contract, frozen cases, base controls | `freeze.md`, `c2-contract.md` |
| `2e700b9a` | Wave-1 dispatch evidence (spec, validated payload, empty validator error file, ready marker) | `w1-spec.json`, `w1-dispatch.json`, `w1.ready` |
| `46a43e94` | Freeze v2: C2 shortcut guard amended after dispatch (false positive on a correct candidate); disclosed | `corpus/lessons/round-89.md` §Mistakes |
| `fcb615c6` | S464 and S465 rows; knowledge entry; round-88 tagged tails (append-only) | `corpus/SOURCES.md`; `corpus/knowledge/cache-key-construction.md` |
| `f62e7954` | Evidence: RFC bodies, r88 C1 re-run at carrier, census after append, assimilation id check, L1 reference candidate | `controls/r88-c1-rerun-at-55d67f15.txt`, `census-after-append.txt`, `assimilation/` |
| `9784ad54` | `scripts/cache_key.py` (C2 candidate) | `corpus/knowledge/cache-key-construction.md` |
| `21770586` | Carrier receipts for C2 under v1 and v2 | `controls/c2-carrier-*.txt` |
| `28532540` | Lesson, SCORECARD round-89 section, LOG round-89 entry, SKILL registry rows, README frontier row, PROVINCE ground | `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-89.md` |
| `d9c972da` | Lesson `## Markers` block (gate-sample, r88 summary correction, r88 re-run retraction, controls-count) | `corpus/lessons/round-89.md` |
| `a225647f` | Lesson: wave review, C1 counter defects RC-1…RC-10 | `corpus/lessons/round-89.md` §Wave review |
| `658f72f8` | SCORECARD planned section routes the wave-review defects | `SCORECARD.md` |
| `1b0f1008` | Final measurement receipts at `658f72f8` | `controls/final-*-at-tip.txt`, `census-final-tip.txt` |
| `08ce630d` | Knowledge entry checklist corrected (the tool has no selftest; the gate is the counter's) | `corpus/knowledge/cache-key-construction.md` |
| `acc69ba5` | Lesson: wave review C2; freeze-time `base-c2` restored beside the v2 re-run | `controls/base-c2-freeze-v1.txt` |
| `2342c3a4` | Round-88 lesson: tagged tail, the S463 statements describe the pre-integration state (ScoutRFC finding 6) | `corpus/lessons/round-88.md` |
| `f63b7ecd` | Duplicate S464 dropped (same §4.1 section as S463); S463 `used-by` extended, logged old → new; candidate entry adopted | `corpus/SOURCES.md`; `corpus/lessons/round-89.md` §Registry; `ScribeEntry` F1 |
| `93475f7e` | Wave-1 evidence: 14 seat reports and receipts, results index, dispatch marker | `.ufo/waves/round-89/w1/` |
| `a33e20d4` | Final receipts at `93475f7e` (C1, C2 v2 and v1, census, both selftests) | `controls/final2-*.txt` |

Reverted before commit: my in-place edits to round-88 `SCORECARD.md` cells and lesson line 265 (filed bytes). Round-88 files now differ from base by appended tails only (`git diff --numstat 76225160 -- SCORECARD.md corpus/lessons/round-88.md`: SCORECARD 46 insertions and 0 deletions, the appended round-89 section; the round-88 lesson 16 insertions and 0 deletions).

## Before → after measurements

Base `76225160d0dff8d2042fbcd037bd08b0971d5e07`; tip measured at `93475f7e2fea29c287b5c677b80c43244f2024e0` (receipts committed at `a33e20d4`).

| Claim | Base | Tip | Counting command |
|---|---|---|---|
| C1 six routed defects | `open=6 closed=0 met=false`, exit 1 (`controls/base-c1.txt`) | `open=1 closed=5 met=false`, exit 1 (`controls/final2-c1-at-tip.txt`) | `python3 -B .ufo/waves/round-89/c89_defect_queue.py --root . --revision <REV> --work <scratch>` |
| C2 conservative key, v2 counter | candidate absent: `frozen=0/16 props=0/200 refuse=0/9 controls=5/5 met=false`, exit 1 (`controls/base-c2.txt`) | `frozen=16/16 props=200/200 refuse=9/9 controls=5/5 met=true`, exit 0 (`controls/final2-c2-at-tip.txt`) | `python3 -B .ufo/waves/round-89/c89_key.py --root . --revision <REV> --candidate scripts/cache_key.py --work <scratch>` |
| C2 conservative key, frozen v1 counter | candidate absent, exit 1 (`controls/base-c2-freeze-v1.txt`) | same line, exit 0 (`controls/final2-c2-frozen-v1-at-tip.txt`) | the v1 counter extracted from `08ab46a1` with the same arguments |
| Registry (`corpus/SOURCES.md`) | 201 rows; 176 tier-A; knowledge `.md` 76 | 202 rows; 177 tier-A; knowledge `.md` 77 | `git show <rev>:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`; `git ls-tree -r --name-only <rev> -- corpus/knowledge \| grep -c '\.md$'` |

## Sources & frontier

- `corpus/SOURCES.md` rows before → after: 201 → 202 (command above); tier-A rows 176 → 177; knowledge `.md` 76 → 77.
- Rows added by tier: A +1 (S465; kind spec). Rows touched old → new: S463 `used-by` `corpus/knowledge/vary-matching.md` → `corpus/knowledge/vary-matching.md, corpus/knowledge/cache-key-construction.md` (logged in `corpus/lessons/round-89.md` §Registry). No other existing row changed.
- Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` exit 0 before (`controls/census-before.txt`, 25 × W04) and at the tip (`controls/final2-census.txt`, exit 0, 26 × W04: the one new W04 is S465's duplicate URL across scopes, not an error). The S464 draft was gated on a full mirror (`validate --file`, exit 0 with its one W04).
- Frontier rows advanced: `corpus/README.md` `## Frontier` gains "Cache-key construction (Vary-nominated stored-response key; key only)" → S463 S465, round 89. PROVINCE round-89 section records the ground as held but not admitted.
- Sourced claim: C2's construction ground cites S463 and S465, both opened or re-opened this round.
- Assimilation: none. `merge/kake` collides on eight ids (S312, S329, S367, S372, S373, S374, S390, S409; `.ufo/waves/round-89/assimilation/collisions`). Nothing adopted.
- considerthese: none taken. `considerthese/2026-10-26.md` proposal 5 is already adopted (`corpus/knowledge/gate-status-ledger.md:7`); proposals 1 and 3 are not mined.
- Frontier stays open: cache-key storage, revalidation, freshness and serving; browser Vary and Pragma behaviour.

## Trend verdicts

- **expansion: improved (provisional).** New ground (cache-key construction) with one new registry row (S465) and one new knowledge entry (76 → 77), plus a new cross-link on S463. Not admitted by an outside closure.
- **quality: unchanged.** Filed bytes were not rewritten after the revert; corrections are appended tails; the registry change is append-only and census-clean. The counters shipped this round are weaker than their first-draft verdicts claimed (wave review); that is recorded under discernment, not here.
- **discernment: harmed.** My first-draft verdicts called C1 and C2 `met`. The wave review (ReviewCounterC1, ReviewCounterC2, CriticClaims) falsified both instruments: ten C1 defects (RC-1…RC-10), and a C2 instrument that admits reference copies and hybrid tables. This report corrects those verdicts rather than keeping them; neither claim is admitted.

## SHONEN

Count of `## SHONEN` headings: 1. Box verdicts (`SHONEN.md`, four boxes; none is `[x]`):

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `corpus/knowledge/shonen-ledger.json` row `box 1`; round 89 adds `corpus/knowledge/cache-key-construction.md` (decision table, error patterns, runnable checklist, S463/S465).
[~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` `## Round 89` (real-data trial), `.ufo/waves/round-89/w1/ExecTrial.md`; the historical round-47 receipt gap in `shonen-ledger.json` row `box 2` is unchanged.
[~] Instructions executable by an agent without oral context — pointer: `corpus/knowledge/cache-key-construction.md` runnable checklist (four commands re-run, outputs match); `scripts/cache_key.py`.
[~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `corpus/knowledge/*.md` sibling-path census (`shonen-ledger.json` row `box 4`); the connector's §5 UFO-FSD section is in the wave directory only, not in the corpus.

## Wave shape

- Shape: one v1 wave, 14 seats (inside the 8–16 band). No second wave: the falsify work ran inside wave 1 (ReviewCounterC1, ReviewCounterC2, CriticClaims, MutKey), and the claims are small. No residual call.
- Roles: scout 2 (ScoutGround, ScoutRFC); executor 4 (ExecKey, ExecDefects, ExecTrial, ExecControls); scribe 3 (ScribeEntry, ScribeLesson, ScribeLedger); reviewer 2 (ReviewCounterC1, ReviewCounterC2); critic 1 (CriticClaims); mutation-tester 1 (MutKey); connector 1 (ConnectorScope). Attack seats 4/14 (28.6 %). L1 holds the planner seat (the validator forbids a planner swarm role).
- Dispatch: `.ufo/waves/round-89/w1.ready` at 18:13:46; WAVE-DONE received, all 14 seats settled.
- Results and dead seats: `w1-results.json` carries no per-seat output (`output: null`; its note says the orchestrator kernel restarted mid-wave and seat output was delivered to the session but not retained). Each seat's report file in `.ufo/waves/round-89/w1/<Seat>.md` is present and non-empty (14/14, 2 756 B to 27 504 B). No dead seat is identified. Per-seat answering models were not recorded, and no claim depends on them.

## Honesty and limits

- C1 item A is open by its frozen form, which demands an in-line tag on filed round-88 lines that the append-only rule forbids. The frozen counter was not amended after scoring; the item is routed.
- C1's other five items are decided by prose and by an instrument the wave review shows to be unsound (RC-1…RC-10). The C1 `open=1` reading is therefore not a calibration gain.
- C2's `met=true` is measured on the frozen predicate only. The reviewers' reference copies and hybrid tables reach it, so the verdict is not a conformance result, and the axis label is disputed.
- C2's `props` population is generated from the printed seed; a hybrid table defeats it, because the property classes assert relations, not key strings.
- The shortcut guard is textual and disclosed as such.
- Freeze v2 (`46a43e94`) amended the C2 guard after dispatch. The integrated candidate meets the frozen v1 counter too (`controls/final2-c2-frozen-v1-at-tip.txt`), so the amendment does not decide the verdict; the procedure is still disclosed as a post-dispatch change.
- The base control `controls/base-c1.txt` was produced with HEAD at a later commit; E reads HEAD (RC-1), so that line is not a pure base measurement.
- The round-89 `controls/base-c2.txt` was overwritten by the v2 re-run; the freeze-time bytes are restored as `controls/base-c2-freeze-v1.txt`.
- No storability, freshness, revalidation, reuse, serving or browser claim is made.

## Routed to round 90 (no fix applied this round)

R89-1 (C1 item A: appended-tail acceptance); RC-1 (E reads `--revision`); RC-2 and RC-3 (E claim decisions); RC-4 (mirror mode); RC-5…RC-7 (A: tag, scope, self-report); RC-8 (B substring parse); RC-9 (C regex and brace parsing); RC-10 (F header test); the C2 clause gaps (URI escaping, name escaping, SP/HTAB trim, CR-only, missing `request_headers`, malformed JSON, case-sensitive member order); the C2 shortcut-guard replacement (execution-time sandbox); C2 property classes that assert key strings; U+001D and duplicate-JSON-member contract definitions; the C2 axis label; the MutKey survivors (seven counter gaps). Operator rulings are requested in `.ufo/l0-questions.md` (three lines, fleet commit `ca57a223`).

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at the fleet root shows orchestrator `.scratch/` state, a sibling's `.ufo/reports/round-84/kama.md` edit, and an untracked `after` (dated 2026-11-03, content `== SCORECARD diff base-`). None names kake round 89; nothing was copied or deleted. No misroot to record.

## Pre-report gate

- `git ls-remote origin refs/heads/master` → `a33e20d41a4b13b71b45bb69a5d83c69da6426b4` (equal to the lane tip before this report commit).
- `grep -c '^## SHONEN'` → 1; four `[~]` box lines.
